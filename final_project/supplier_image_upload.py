#!/usr/bin/env python3

import os
import requests
import json


def image_upload():

    user = os.getenv("USER")
    url = "http://localhost/upload/"
    path = f"/home/{user}/supplier-data/images"

    files = sorted(os.listdir(path))

    for file in files:
        if file.endswith(".jpeg"):
            with open(f"{path}/{file}", "rb") as opened:
                res = requests.post(url, files={"file": opened})


image_upload()
