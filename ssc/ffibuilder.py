import os.path

from cffi import FFI


CURDIR = os.path.dirname(__file__)
_FFI = FFI()
_FFI.set_source("ssc._ffi", None)

with open(os.path.join(CURDIR, "sscapi.h")) as header_file:
    _FFI.cdef(header_file.read())
