import yaml
from box import Box

conf = Box.from_yaml(filename="documents\class\OPIN-Cliente.yaml", Loader=yaml.FullLoader) 

def getEnum(confV, schema, prop):
    str1 = ""
    try:
        for i in confV.components.schemas[schema].properties[prop].enum:
            str1 += i + ", "
    except:
        for i in confV.components.schemas[schema].enum:
            str1 += i
    return str1[0:len(str1) - 2]

def getRef(schemaBefore, confV, schema, prop):
    printLine(confV +"." + schemaBefore + "." + schema + "." + prop + ";Não há detalhes.")

def printLine(line):
    a = str(line)
    with open('wiuolhaisso.csv', 'a', encoding='UTF8') as f:
        f.write(a + "\n")
   
def getSchema(confV, schema, schemaBefore):

    propertyExcept = ""
    try:
         for prop in conf.components.schemas[schema].properties:
            propertyExcept = prop
            try:
                getSchema(confV, confV.components.schemas[schema].properties[prop]['items']['$ref'].split("/")[-1], schema + ".")
            except:
                printLine(schemaBefore + schema + "." + prop + ";" + str(confV.components.schemas[schema].properties[prop].description))
    except:
        try:
           enumD = conf.components.schemas[schema].enum
           printLine(schemaBefore + schema + ";" + str(confV.components.schemas[schema].description))
        except:   
            try:
                resp = getEnum(confV, schema, propertyExcept) 
                printLine(schemaBefore + schema + ";" + str(confV.components.schemas[schema]) + resp)
            except:      
                try:
                   getRef(schemaBefore, confV, schema, prop) 
                except:
                    printLine('Não existe esse parâmetro ' + prop)



