from os import path
from setuptools import setup, find_packages


curdir = path.abspath(path.dirname(__file__))
with open(path.join(curdir, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="sscpy",
    version="0.2.0",
    description="Python bindings for SAM Simulation Core (SSC)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Station A",
    author_email="software@stationa.com",
    url="https://github.com/StationA/sscpy",
    packages=find_packages(exclude=["*tests*"]),
    package_data={
        "ssc": ["_ffi.py", "sscapi.h"],
    },
    zip_safe=False,
    setup_requires=["cffi>=1.0.0"],
    install_requires=["cffi>=1.0.0"],
    tests_require=["cffi>=1.0.0"],
    cffi_modules=["ssc/ffibuilder.py:_FFI"],
    license="License :: OSI Approved :: MIT License",
)
