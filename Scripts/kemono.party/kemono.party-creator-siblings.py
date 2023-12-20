import requests, json, os

creators = json.loads(requests.get('https://kemono.party/api/v1/creators').text)
with open("kemono.party_siblings.txt", 'a', encoding="utf-8") as file:
    for creator in creators:
        name = creator['name']
        id = creator['id']
        service = creator["service"]
        if name and id != "":
            if service == "fanbox": continue
            file.write(service + " id:" + id + "\ncreator:" + name.replace('\n', ' ') + "\n")

