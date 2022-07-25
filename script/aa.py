import yaml
from yaml.loader import SafeLoader

with open(r'documents/OPIN-Cliente.yaml', encoding='utf8') as f:
    data = yaml.load(f, Loader=SafeLoader)
    for a in data['components']['schemas']:
        try:
            for b in data['components']['schemas'][a]:
                for y in data['components']['schemas'][a][b]:
                        print(a + " " + b + " " +y)
        except:
            print("sou lindo")