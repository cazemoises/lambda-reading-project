import yaml
with open(r'documents/OPIN-Cliente.yaml', encoding="utf8") as file:
    documents = yaml.safe_load_all(file)
    for a in documents:
        for i in a:
            if i == 'components':
                for j in a[i]['schemas']:
                    try:
                        print(a[i]['schemas'][j]['description'])
                    except:
                        print('esse não tem descrição')