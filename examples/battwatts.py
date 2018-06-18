from ssc.api import enable_logging, BattWatts, PVWattsV5

from dateutil import parser
import matplotlib.pyplot as plt
import pandas as pd
import sys


enable_logging()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python battwatts.py <TMY3_CSV> <LOAD_CSV>')
        sys.exit(255)

    load_file = sys.argv[2]
    load = pd.read_csv(load_file)
    ts = load['Date'].apply(parser.parse).tolist()

    # First simulate the solar
    tmy3_file = sys.argv[1]
    pvwatts = PVWattsV5()
    params = {
        'solar_resource_file': tmy3_file,
        'tilt': 11,
        'azimuth': 180,
        'dc_ac_ratio': 1.2,
        'inv_eff': 91,
        'losses': 7.8,
        'system_capacity': 7783,
        'module_type': 0,
        'adjust:constant': 0.0,
        'array_type': 1
    }
    pv_results = pvwatts.run(**params)
    pv_ac_output = [x/1000. for x in pv_results['ac']]  # W to kW

    # Then use the PVWatts output to input into the battery simulation
    battwatts = BattWatts()
    params = {
        'load': load['kW'].tolist(),
        'batt_simple_enable': 1,
        'batt_simple_kwh': 6517,  # 2 hour battery
        'batt_simple_kw': 3258,
        'batt_simple_chemistry': 1,
        'batt_simple_dispatch': 1,
        'batt_simple_meter_position': 0,
        'dc': pv_results['dc'],
        'ac': pv_results['ac'],
        'inverter_model': 0,
        'inverter_efficiency': 91
    }
    batt_results = battwatts.run(**params)
    new_load = load - pd.DataFrame({'kW': [float(x) for x in batt_results['gen']]})

    batt_power = batt_results['batt_power']
    plt.plot(ts, load['kW'].tolist(), label='Original Load (kW)', color='gray')
    plt.plot(ts, new_load['kW'].tolist(), label='New Load (kW)', color='#33cadd')
    plt.plot(ts, pv_ac_output, label='Solar AC (kW)', color='y')
    plt.plot(ts, batt_power, label='Battery DC (kW)', color='orange')
    plt.title('Solar + Battery Output')
    plt.legend()
    plt.show()
