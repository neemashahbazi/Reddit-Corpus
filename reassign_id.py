import json

data_file = 'data/scraper/data.json'
with open(data_file, 'r') as file:
    data_content = file.read()
    data = json.loads(data_content)
    for item in data['data']:
        item.update({"id": "Author_" + str(data['data'].index(item) + 1)})
    open(data_file, "w").write(
        json.dumps(data, sort_keys=True, indent=4)
    )
