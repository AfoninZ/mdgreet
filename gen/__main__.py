from . import styles
from .modules import sensors, pitemp


for i in styles.fg.keys():
    print(styles.fg[i] + 'Test!')

sensors.SensorsModule()
pitemp.PiTempModule()