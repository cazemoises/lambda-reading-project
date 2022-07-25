import yaml
from yaml.loader import SafeLoader

# entryValues = input("Digite os valores de entrada, os separando por vírgulas \n ex: valor1,valor2,valor3:\n")
entryValues = 'components,schemas'
array = entryValues.split(',')
print(array)
with open(r'documents/OPIN-Cliente.yaml', encoding='utf8') as f:
    data = yaml.load(f, Loader=SafeLoader)