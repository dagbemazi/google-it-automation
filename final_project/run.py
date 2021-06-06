# Upload description of fruits to server's localhost.
#!/usr/bin/env python3
import json
import os
import requests


def upload_desc():
    url = "http://localhost/fruits/"

    user = os.getenv("USER")
    path = f"/home/{user}/supplier-data/descriptions"

    files = os.listdir(path)
    for file in files:
        with open(f'{path}/{file}') as f:
            desc = {}
            lines = f.read().splitlines()
            description = "".join(lines[2:]).strip("\n").replace(u"\xa0", u"")
            desc["name"] = lines[0].strip("\n")
            desc["weight"] = int(lines[1].strip("\n").strip(" lbs"))
            desc["description"] = description
            desc["image_name"] = file.replace("txt", "jpeg")

            res = requests.post(url, json=desc)


upload_desc()
