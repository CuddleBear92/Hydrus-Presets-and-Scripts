import requests, json, os, sys

API_URL = 'https://kemono.party/api/v1/creators'
OUT_FILE = 'kemono.party_siblings.txt'

def get_creators():
    creators = None
    try:
        creators = json.loads(requests.get(API_URL).text)
    except Exception as exc:
        with sys.stderr as dest:
            print(exc, file=dest)
        print(f'Error fetching creators. Ensure URL "{API_URL}" is correct.')
    return creators

creators = get_creators()
if creators is None: exit(1)
with open(OUT_FILE, 'a', encoding="utf-8") as file:
    for creator in creators:
        name = creator['name']
        id = creator['id']
        service = creator["service"]
        if name and id:
            if service == "fanbox": continue
            creator_name = name.replace('\n', ' ')
            file.write(f"{service} id:{id}\ncreator:{creator_name}\n")

