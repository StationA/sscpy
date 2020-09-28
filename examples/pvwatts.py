from ssc.api import PVWatts

import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pvwatts.py <TMY3_CSV>")
        sys.exit(255)

    tmy3_file = sys.argv[1]
    pvwatts = PVWatts()
    params = {
        "solar_resource_file": tmy3_file,
        "tilt": 11,
        "azimuth": 180,
        "dc_ac_ratio": 1.2,
        "inv_eff": 96,
        "losses": 7.8,
        "system_capacity": 1000,
        "module_type": 0,
        "adjust:constant": 0.0,
        "array_type": 1,
    }
    results = pvwatts.run(**params)
    ac_output = [x / 1000.0 for x in results["ac"]]  # W to kW
    print(f"Annual solar output (kWh AC): {sum(ac_output)}")
