from ssc.core import _LIB
from ssc._ffi import ffi


class ModuleRunError(Exception):
    """
    Generic error which occurs while a module is running
    """
    pass


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
