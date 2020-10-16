# sscpy

[![PyPI version](https://badge.fury.io/py/sscpy.svg)](https://badge.fury.io/py/sscpy)

Python bindings to SAM Simulation Core (SSC)

## Installation

### Requirements

- [SAM Simulation Core (SSC)](https://github.com/NREL/ssc) native libraries
- Python 3+

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

## Usage

### Example running PVWatts (v7)

```python
from ssc.api import PVWatts

pvwatts = PVWatts()
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

## Contributing

When contributing to this repository, please follow the steps below:

1. Fork the repository
1. Submit your patch in one commit, or a series of well-defined commits
1. Submit your pull request and make sure you reference the issue you are addressing

### Installing for development

```
pip install --editable .
```

### Running tests

```
tox -e dev
```
