import requests, json, os

creators = json.loads(requests.get('https://kemono.party/api/creators').text)
file = open("yiff_siblings.txt", 'a',encoding="utf-8")

for creator in creators:
    name = creator['name']
    id = creator['id']
    service = creator["service"]
    if name and id != "":
        if service == "fanbox": continue
        file.write(str(service)+" id:"+str(id)+"\ncreator:"+name+"\n")

file.close()