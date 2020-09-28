from ssc.core import Data
from ssc.modules import SSCModule


class PVWatts(SSCModule):
    """
    SSCModule implementation of the PVWatts interface
    """

    def __init__(self, version="7"):
        super().__init__(f"pvwattsv{version}")

    def run(self, **inputs):
        d = Data()
        d.update(inputs)
        self.execute(d)
        return d
