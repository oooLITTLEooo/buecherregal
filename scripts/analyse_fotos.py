#!/usr/bin/env python3
"""Inventory only the real photos in bilder/originale, without modifying them."""
import base64
import csv
import hashlib
import io
import itertools
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
IMAGE_DIR=ROOT/"bilder/originale"
CSV=ROOT/"daten/fotos.csv"
GENERATED=ROOT/"bilder/generiert/kontaktboegen"
ANALYSIS=ROOT/"daten/bildanalyse"
PREVIEWS=ROOT/"daten/bildvorschau"
TYPES={".jpg",".jpeg",".png",".webp",".heic",".heif",".tif",".tiff"}
NEW_FIELDS=["breite_px","hoehe_px","exif_datetime","git_blob_sha_berechnet","dhash64","lesbarkeit_technisch","analyse_utc"]
NOW=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def hashes(p):
    sha=hashlib.sha256()
    git=hashlib.sha1()
    git.update(b"blob "+str(p.stat().st_size).encode()+b"\0")
    with p.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):
            sha.update(block)
            git.update(block)
    return sha.hexdigest(),git.hexdigest()

def dhash(im):
    gr=ImageOps.exif_transpose(im).convert("L").resize((9,8))
    px=list(gr.getdata())
    result=0
    for y in range(8):
        for x in range(8):
            result=(result<<1)|int(px[y*9+x]>px[y*9+x+1])
    return f"{result:016x}"

def save_b64(p,bytes_value):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(base64.b64encode(bytes_value).decode("ascii")+"\n",encoding="ascii")

def main():
    pictures=sorted((p for p in IMAGE_DIR.rglob("*") if p.is_file() and p.suffix.lower() in TYPES))
    root_pictures=[p for p in ROOT.iterdir() if p.is_file() and p.suffix.lower() in TYPES]
    if root_pictures or not pictures:
        raise ValueError("Root images or missing originals: "+str(root_pictures))
    with CSV.open(encoding="utf-8",newline="") as f:
        reader=csv.DictReader(f,delimiter=";")
        fields=list(reader.fieldnames)
        rows=list(reader)
    indexed={r["dateiname_git"]:r for r in rows}
    names={p.relative_to(ROOT).as_posix() for p in pictures}
    if len(rows)!=len(indexed) or names!=set(indexed):
        raise ValueError("Photo files differ from CSV: "+str(names.symmetric_difference(indexed)))
    fields+= [f for f in NEW_FIELDS if f not in fields]
    cards=[]
    unreadable=[]
    for path in pictures:
        rel=path.relative_to(ROOT).as_posix()
        row=indexed[rel]
        sha,git=hashes(path)
        if git!=row["git_blob_sha"]:
            import subprocess
            git_cli=subprocess.run(["git","hash-object",str(path)],capture_output=True,text=True)
            git_index=subprocess.run(["git","ls-files","--stage",rel],capture_output=True,text=True)
            raise ValueError("Git hash mismatch: "+rel+" expected="+row["git_blob_sha"]+" calculated="+git+" git_hash_object="+git_cli.stdout.strip()+" index="+git_index.stdout.strip()+" bytes="+str(path.stat().st_size))
        row["sha256"]=sha
        row["groesse_bytes"]=str(path.stat().st_size)
        row["git_blob_sha_berechnet"]=git
        row["analyse_utc"]=NOW
        try:
            with Image.open(path) as original:
                original.load()
                row["breite_px"],row["hoehe_px"]=map(str,original.size)
                exif=original.getexif()
                row["exif_datetime"]=str(exif.get(36867) or exif.get(306) or "")
                row["dhash64"]=dhash(original)
                row["lesbarkeit_technisch"]="ja"
                preview=ImageOps.exif_transpose(original).convert("RGB")
                preview.thumbnail((1300,1300))
                buff=io.BytesIO()
                preview.save(buff,format="JPEG",quality=72,optimize=True)
                save_b64(PREVIEWS/(row["foto_id"]+".jpg.base64.txt"),buff.getvalue())
                cards.append((row["foto_id"],path.name,preview))
        except Exception as exc:
            row["lesbarkeit_technisch"]="fehler"
            unreadable.append((rel,str(exc)))
    GENERATED.mkdir(parents=True,exist_ok=True)
    ANALYSIS.mkdir(parents=True,exist_ok=True)
    try:
        font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",16)
    except OSError:
        font=ImageFont.load_default()
    for offset in range(0,len(cards),16):
        canvas=Image.new("RGB",(1600,1240),"white")
        draw=ImageDraw.Draw(canvas)
        for n,(ident,name,preview) in enumerate(cards[offset:offset+16]):
            x=(n%4)*400
            y=(n//4)*310
            thumb=preview.copy()
            thumb.thumbnail((380,268))
            canvas.paste(thumb,(x+(400-thumb.width)//2,y+(268-thumb.height)//2))
            draw.text((x+8,y+276),ident+" "+name,fill="black",font=font)
            draw.rectangle((x,y,x+399,y+309),outline="#999999")
        buff=io.BytesIO()
        canvas.save(buff,format="JPEG",quality=72,optimize=True)
        name=f"kontaktbogen_{1+offset//16:02d}.jpg"
        (GENERATED/name).write_bytes(buff.getvalue())
        save_b64(ANALYSIS/(name+".base64.txt"),buff.getvalue())
    candidates=[]
    for a,b in itertools.combinations(rows,2):
        same=a["sha256"]==b["sha256"]
        dist=(int(a["dhash64"],16)^int(b["dhash64"],16)).bit_count() if a.get("dhash64") and b.get("dhash64") else 999
        if same or dist<=8:
            candidates.append((a["foto_id"],b["foto_id"],dist,same))
    report=[
      "# Technische Bildinventur",
      "",
      "Zeitpunkt (UTC): "+NOW,
      "Originaldateien: "+str(len(pictures)),
      "Technisch unlesbar: "+str(len(unreadable)),
      "Identische oder aehnliche Kandidaten: "+str(len(candidates)),
      "",
      "Die Originale wurden nicht veraendert. dHash ist nur ein Vergleichsindikator, kein Loeschkriterium.",
      "Die tatsaechliche Regalposition muss anhand sichtbarer Motive ermittelt werden.",
      "",
      "## Kandidaten",
      "",
      "| Foto-ID A | Foto-ID B | dHash Abstand | SHA-256 identisch |",
      "| --- | --- | ---: | --- |",
    ]
    report += [f"| {a} | {b} | {dist} | {'ja' if same else 'nein'} |" for a,b,dist,same in candidates]
    report += ["","## Unlesbare Fotos",""]
    report += [f"- {a}: {b}" for a,b in unreadable]
    (ANALYSIS/"technische_inventur.md").write_text("\n".join(report)+"\n",encoding="utf-8")
    with CSV.open("w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=fields,delimiter=";",lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Originals: {len(pictures)}; errors: {len(unreadable)}; candidates: {len(candidates)}; contact sheets: {(len(cards)+15)//16}")

if __name__=="__main__":
    main()
