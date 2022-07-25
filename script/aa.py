import yaml
from yaml.loader import SafeLoader


with open('./') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)