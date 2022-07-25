import OpenAPI

conf = OpenAPI.conf
qtdErro = 0


for schema in conf.components.schemas:
    try: 
        OpenAPI.getSchema(conf, schema, "")
    except:
        qtdErro += 1