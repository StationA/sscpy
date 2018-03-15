# sscpy

[![PyPI version](https://badge.fury.io/py/sscpy.svg)](https://badge.fury.io/py/sscpy)

Python bindings to SAM Simulation Core (SSC)

# Installation

### Requirements

* [SAM Simulation Core (SSC)](https://github.com/NREL/ssc) native libraries
* Python 3+

### Install from PyPI (recommended)

```
pip install sscpy
```

### Installing from Github

```
pip install git+https://github.com/StationA/sscpy.git#egg=sscpy
```

### Installing from source

```
git clone https://github.com/StationA/sscpy.git
cd sscpy
pip install .
```

# Usage

### Example running PVWatts (v5)

```python
from ssc.api import PVWattsV5

pvwatts = PVWattsV5()
params = {
    'solar_resource_file': 'weather_data.csv',
    'system_capacity': 1.0,
    'losses': 14.0,
    'array_type': 0,
    'tilt': 20,
    'azimuth': 180,
    'adjust:constant': 0
}
results = pvwatts.run(**params)

for output in results['ac']:
    print(output)
```


# Contributing

### Installing for development

```
pip install --editable .
```

### Running tests

```
tox -e dev
```
