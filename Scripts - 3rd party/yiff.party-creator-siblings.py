import requests, json, os

creators = json.loads(requests.get('https://yiff.party/json/creators.json').text)
file = open("yiff_siblings.txt", 'a')

for creator in creators['creators']:
    name = creator['name']
    id = creator['id']
    if name and id != "":
        file.write("yiff id:"+str(id)+"\ncreator:"+name+"\n")
