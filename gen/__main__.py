from . import styles
from .modules import sensors


for i in styles.fg.keys():
    print(styles.fg[i] + 'Test!')

sensors.SensorsModule()