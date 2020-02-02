from ..utils import Module, bar
from .. import styles
import re


class SensorsModule(Module):
    def __init__(self, height=3):
        super().__init__(height)
        temp = float(self.get('sensors').decode().split('Tdie:')[1].split('°')[0].strip())
        print(styles.fg['normal'] + str(temp))
        print(bar(34, temp, 100))