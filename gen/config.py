import os
import pathlib
import yaml


with open(os.path.join(pathlib.Path(__file__).parent.absolute(), 'config_default.yml')) as f:
    config = yaml.safe_load(f)
