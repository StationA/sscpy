from setuptools import setup, find_packages


setup(
    name='sscpy',
    version='0.1.7',
    description='Python bindings for SAM Simulation Core (SSC)',
    author='Station A',
    author_email='software@stationa.com',
    url='https://github.com/StationA/sscpy',
    packages=find_packages(exclude=['*tests*']),
    package_data={
        'ssc': ['_ffi.py'],
    },
    zip_safe=False,
    setup_requires=['cffi>=1.0.0'],
    install_requires=['cffi>=1.0.0'],
    tests_require=['cffi>=1.0.0'],
    cffi_modules=['ssc/ffibuilder.py:_FFI'],
    license='License :: OSI Approved :: MIT License',
)
