from ssc.core import Data
from ssc.modules import SSCModule


class PVWattsV5(SSCModule):
    """
    SSCModule implementation of the PVWatts (v5) interface
    """
    def __init__(self):
        super().__init__('pvwattsv5')

    def run(self, **inputs):
        d = Data()
        d.update(inputs)
        self.execute(d)
        return d
