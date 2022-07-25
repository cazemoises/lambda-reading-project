import yaml
from box import Box

# Load from yaml file
# Here it is also possible to use PyYAML arguments, 
# for example to specify different loaders e.g. SafeLoader or FullLoader
conf = Box.from_yaml(filename="class/OPIN-Cliente.yaml", Loader=yaml.FullLoader) 

print(len(conf.components.schemas))

lineValue = ""
qtdErro = 0
buscando = ""

def printLine(line):
    print(line)

def getSchema(confV, schema, schemaBefore):
    try:
         for prop in conf.components.schemas[schema].properties:
            try:
                getSchema(confV, confV.components.schemas[schema].properties[prop]['items']['$ref'].split("/")[-1], schema + ".")
            except:
                printLine(schemaBefore + schema + "." + prop + ";" + str(confV.components.schemas[schema].properties[prop].description) + "\n")
        #print("Buscar ", confV.components.schemas[schema].properties[prop]['items']['$ref'])
    except:
        try:
           enumD = conf.components.schemas[schema].enum
           printLine(schemaBefore + schema + ";" + str(confV.components.schemas[schema].description) + "\n")
        except:    
            print("deu ruim, estudar\n")

for schema in conf.components.schemas:
    try: 
        lineValue += conf.components.schemas[schema].description + "\n"  
        getSchema(conf, schema, "")
    except:
        qtdErro += 1

#print(lineValue)