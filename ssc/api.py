try:
    from UserDict import DictMixin
except ImportError:
    from collections import MutableMapping as DictMixin
from ssc._ffi import ffi


try:
    _LIB = ffi.dlopen('libssc.so')  # Linux
except Exception:
    _LIB = ffi.dlopen('ssc.dylib')  # OSX
_LIB.ssc_module_exec_set_print(1)
__buildinfo__ = ffi.string(_LIB.ssc_build_info())
__version__ = _LIB.ssc_version()


def list_modules():
    modules = []
    i = 0
    while True:
        mod = _LIB.ssc_module_entry(i)
        if mod == ffi.NULL:
            break
        mod_name = _LIB.ssc_entry_name(mod)
        modules.append(ffi.string(mod_name))
        i += 1
    return modules


class ModuleRunError(Exception):
    """
    Generic error which occurs while a module is running
    """
    pass


class Data(DictMixin):
    """
    Dict-like wrapper for the SSC data table type `ssc_data_t`
    """
    def __init__(self):
        self._data = _LIB.ssc_data_create()

    def _get_data_type(self, name):
        for key in self.keys():
            if key == name:
                return _LIB.ssc_data_query(self._data, key)

        raise KeyError(name)

    def __getitem__(self, name):
        name = bytes(name, 'utf-8')
        type_ = self._get_data_type(name)
        if type_ == _LIB.SSC_STRING:
            return self._get_string(name)
        if type_ == _LIB.SSC_NUMBER:
            return self._get_number(name)
        if type_ == _LIB.SSC_ARRAY:
            return self._get_array(name)
        if type_ == _LIB.SSC_MATRIX:
            return self._get_matrix(name)
        if type_ == _LIB.SSC_TABLE:
            return self._get_table(name)

        raise TypeError('Unsupported SSC data type \'%s\'' % type_)

    def __setitem__(self, name, v):
        name = bytes(name, 'utf-8')
        if type(v) is str:
            v = bytes(v, 'utf-8')
            return _LIB.ssc_data_set_string(self._data, name, v)
        if type(v) is int or type(v) is float:
            return _LIB.ssc_data_set_number(self._data, name, v)

        raise TypeError('Unsupported Python data type \'%s\'' % type(v))

    def __delitem__(self, name):
        # Used to check for key existence
        name = bytes(name, 'utf-8')
        self._get_data_type(name)
        _LIB.ssc_data_unassign(self._data, name)

    def _get_string(self, name):
        s = _LIB.ssc_data_get_string(self._data, name)
        return ffi.string(s)

    def _get_number(self, name):
        n = ffi.new('ssc_number_t *')
        _LIB.ssc_data_get_number(self._data, name, n)
        return n[0]

    def _get_array(self, name):
        len_ = ffi.new('int *')
        arr = _LIB.ssc_data_get_array(self._data, name, len_)
        return [arr[i] for i in range(0, len_[0])]

    def _get_matrix(self, name):
        # TODO: Support actual matrices!
        return self._get_array(name)

    def _get_table(self, name):
        t = _LIB.ssc_data_get_table(self._data, name)
        return t

    def keys(self):
        keys_ = []
        key = _LIB.ssc_data_first(self._data)
        while key != ffi.NULL:
            keys_.append(ffi.string(key))
            key = _LIB.ssc_data_next(self._data)
        return keys_

    def __iter__(self):
        for k in self.keys():
            yield (k, self.__getitem__(k))

    def __len__(self):
        return len(self.keys())


class SSCModule(object):
    """
    Generic base class for SSC modules
    """
    def __init__(self, mod_name):
        mod_name = bytes(mod_name, 'utf-8')
        self._module = _LIB.ssc_module_create(mod_name)

    def _module_data(self):
        i = 0
        while True:
            info = _LIB.ssc_module_var_info(self._module, i)
            if info == ffi.NULL:
                break
            var_type = _LIB.ssc_info_var_type(info)
            name = _LIB.ssc_info_name(info)
            yield var_type, ffi.string(name)
            i += 1

    @property
    def inputs(self):
        """
        Returns a list of the module's expected inputs
        """
        inputs_ = []
        for var_type, name in self._module_data():
            if var_type in (_LIB.SSC_INPUT, _LIB.SSC_INOUT):
                inputs_.append(name)
        return inputs_

    @property
    def outputs(self):
        """
        Returns a list of the module's expected outputs
        """
        outputs_ = []
        for var_type, name in self._module_data():
            if var_type in (_LIB.SSC_OUTPUT, _LIB.SSC_INOUT):
                outputs_.append(name)
        return outputs_

    def execute(self, data):
        """
        Provided a data table with inputs, executes the module and fills in the data table with any
        generated outputs
        """
        success = _LIB.ssc_module_exec(self._module, data._data)
        if not success:
            raise ModuleRunError
        return data


class PVWattsV5(SSCModule):
    """
    SSCModule implementation of the PVWatts (v5) interface
    """
    def __init__(self):
        super(PVWattsV5, self).__init__('pvwattsv5')

    def run(self, **inputs):
        d = Data()
        d.update(inputs)
        self.execute(d)
        return d
