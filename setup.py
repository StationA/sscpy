from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession


SESSION = PipSession()
INSTALL_REQUIRES = [str(r.req) for r in
                    parse_requirements('./requirements.txt', session=SESSION)]
TESTS_REQUIRE = [str(r.req) for r in
                 parse_requirements('./test_requirements.txt', session=SESSION)]


setup(
    name='sscpy',
    version='0.1.4',
    description='SAM Simulation Core (SSC) API for Python',
    author='Station A',
    author_email='StationAOps@nrg.com',
    url='https://github.com/StationA/sscpy',
    packages=find_packages(exclude=['*tests*']),
    package_data={
        'ssc': ['_ffi.py'],
    },
    zip_safe=False,
    setup_requires=['cffi>=1.0.0'],
    cffi_modules=['ssc/ffibuilder.py:_FFI'],
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    license='License :: OSI Approved :: MIT License',
)
