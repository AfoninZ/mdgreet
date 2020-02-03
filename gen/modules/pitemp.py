from ..utils import Module, bar
from .. import styles
import re


class PiTempModule(Module):
    def __init__(self, height=3):
        super().__init__(height)
        temp = float(self.get('vcgencmd measure_temp').decode().strip('temp=')[:-2])
        print(styles.fg['normal'] + str(temp))
        print(bar(34, temp, 100))