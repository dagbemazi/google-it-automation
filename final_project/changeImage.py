#!/usr/bin/env python3

import os
from PIL import Image


def change_image():
    user = os.getenv("USER")

    src = f"/home/{user}/supplier-data/images"
    os.chdir(src)

    for root, dirs, file in os.walk(src):
        for infile in file:
            f, e = os.path.splitext(infile)
            outfile = f + ".jpeg"
            try:
                with Image.open(f"{src}/{infile}").convert("RGB").resize((600, 400)) as im:
                    im.save(
                        f"/home/{user}/supplier-data/images/{outfile}", "JPEG")
            except Exception as e:
                print(e)


change_image()
