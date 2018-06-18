from ssc.core import Data
from ssc.modules import SSCModule


class BattWatts(SSCModule):
    """
    SSCModule implementation of the BattWatts interface
    """
    def __init__(self):
        super().__init__('battwatts')

    def run(self, **inputs):
        d = Data()
        d.update(inputs)
        self.execute(d)
        return d
