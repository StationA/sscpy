# sscpy

[![PyPI version](https://badge.fury.io/py/sscpy.svg)](https://badge.fury.io/py/sscpy)

Python bindings to SAM Simulation Core (SSC)

# Installation

### Requirements

* [SAM Simulation Core (SSC)](https://github.com/NREL/ssc) native libraries
* Python 2.7+

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
results = pvwatts.run('weather_data.csv')

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
