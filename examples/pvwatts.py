from ssc.api import PVWattsV5

from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import sys


TS = []
start = datetime(2018, 1, 1, 0)
for h in range(8760):
    TS.append(start + timedelta(hours=h))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python pvwatts.py <TMY3_CSV>')
        sys.exit(255)

    tmy3_file = sys.argv[1]
    pvwatts = PVWattsV5()
    params = {
        'solar_resource_file': tmy3_file,
        'tilt': 11,
        'azimuth': 180,
        'dc_ac_ratio': 1.2,
        'inv_eff': 96,
        'losses': 7.8,
        'system_capacity': 1000,
        'module_type': 0,
        'adjust:constant': 0.0,
        'array_type': 1
    }
    results = pvwatts.run(**params)
    ac_output = [x/1000. for x in results['ac']]  # W to kW
    plt.plot(TS, ac_output, label='Solar AC (kW)', color='y')
    plt.title('Solar Output')
    plt.legend()
    plt.show()
