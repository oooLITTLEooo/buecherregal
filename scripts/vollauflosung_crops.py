#!/usr/bin/env python3
"""Make legible native-resolution crops ONLY of Git-originals explicitly queued.

This does not modify photos and does not infer or inventory books.
"""
import base64
import csv
import io
from pathlib import Path
from PIL import Image, ImageOps

ROOT=Path(__file__).resolve().parents[1]
QUEUE=ROOT/"daten/bildanalyse/crop_queue.txt"
CSVFILE=ROOT/"daten/fotos.csv"
OUT=ROOT/"daten/bildanalyse/fullres"
OUT.mkdir(parents=True,exist_ok=True)
with CSVFILE.open(newline="",encoding="utf-8") as stream:
    inventory={r["foto_id"]:r for r in csv.DictReader(stream,delimiter=";")}
requested=[x.strip() for x in QUEUE.read_text(encoding="utf-8").splitlines()
           if x.strip() and not x.strip().startswith("#")]
if len(requested)!=len(set(requested)):
    raise ValueError("duplicate queue IDs")
if len(requested)>16:
    raise ValueError("Process max 16 originals per run")
for image_id in requested:
    if image_id not in inventory:
        raise ValueError("Missing image in CSV: "+image_id)
    original=ROOT/inventory[image_id]["dateiname_git"]
    if not original.is_file() or not original.resolve().is_relative_to((ROOT/"bilder/originale").resolve()):
        raise ValueError("Invalid original path")
    with Image.open(original) as raw:
        im=ImageOps.exif_transpose(raw).convert("RGB")
        w,h=im.size
        # Four crops, each at its natural pixel resolution, retaining shelf spines.
        # Vertical crop 5%...90% to remove unrelated adjacent shelves.
        top=int(h*0.05)
        bottom=int(h*0.90)
        for index in range(4):
            left=round(w*index/4)
            right=round(w*(index+1)/4)
            crop=im.crop((left,top,right,bottom))
            buffer=io.BytesIO()
            crop.save(buffer,"JPEG",quality=76,optimize=True,subsampling=0)
            name=f"{image_id}_teil_{index+1:02d}.jpg.base64.txt"
            (OUT/name).write_text(base64.b64encode(buffer.getvalue()).decode("ascii")+"\n",encoding="ascii")
            print(image_id,name,"native pixels",crop.size,"JPEG bytes",len(buffer.getvalue()))
