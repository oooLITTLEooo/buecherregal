#!/usr/bin/env python3
"""Native-pixel enlarged and rotated individual views for each open book ID.

Only derive from existing Git SVGs, which embed JPEG source pixels.
Never modify the original photos, shelf order or inventory content.
"""
import base64
import csv
import io
from pathlib import Path
import xml.etree.ElementTree as ET

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "daten/nachkontrolle/nicht-erkannt-quellen.csv"
SVG_DIR = ROOT / "bilder/nachkontrolle"
OUT_DIR = ROOT / "bilder/nachkontrolle-zoom"
B64_DIR = ROOT / "daten/nachkontrolle/zoom-b64"
OUT_DIR.mkdir(parents=True, exist_ok=True)
B64_DIR.mkdir(parents=True, exist_ok=True)

def make_view(svg_path: Path):
    tree = ET.parse(svg_path)
    root = tree.getroot()
    vb = [float(v) for v in root.attrib["viewBox"].replace(",", " ").split()]
    if len(vb) != 4:
        raise ValueError(f"Unexpected viewBox {svg_path}")
    vx, vy, vw, vh = vb
    w, h = round(vw), round(vh)
    if not (100 <= w <= 6000 and 100 <= h <= 7500):
        raise ValueError(f"Crop size out of bounds: {svg_path} {w}x{h}")
    canvas = Image.new("RGB", (w, h), "#fafafa")
    hit = 0
    for el in root.iter():
        if el.tag.split("}")[-1] != "image":
            continue
        href = el.get("href") or el.get("{http://www.w3.org/1999/xlink}href")
        prefix = "data:image/jpeg;base64,"
        if not href or not href.startswith(prefix):
            continue
        x, y = float(el.get("x", "0")), float(el.get("y", "0"))
        iw, ih = float(el.get("width")), float(el.get("height"))
        jpeg = base64.b64decode(href[len(prefix):], validate=True)
        with Image.open(io.BytesIO(jpeg)) as im:
            im.load()
            source = im.convert("RGB")
        scale_x, scale_y = source.width / iw, source.height / ih
        ix0, iy0 = max(vx, x), max(vy, y)
        ix1, iy1 = min(vx + vw, x + iw), min(vy + vh, y + ih)
        if ix0 >= ix1 or iy0 >= iy1:
            continue
        crop = source.crop((round((ix0 - x) * scale_x),
                            round((iy0 - y) * scale_y),
                            round((ix1 - x) * scale_x),
                            round((iy1 - y) * scale_y)))
        dest_x, dest_y = round(ix0 - vx), round(iy0 - vy)
        canvas.paste(crop, (dest_x, dest_y))
        hit += 1
    if hit == 0:
        raise ValueError(f"No visible embedded JPEG: {svg_path}")
    return canvas

def save_jpeg_and_b64(book_id: str, suffix: str, im: Image.Image):
    preview = im.copy()
    preview.thumbnail((3500, 1400), Image.Resampling.LANCZOS)
    data = io.BytesIO()
    preview.save(data, "JPEG", quality=78, optimize=True, subsampling=0)
    payload = data.getvalue()
    if len(payload) > 750_000:
        data = io.BytesIO()
        preview.save(data, "JPEG", quality=62, optimize=True)
        payload = data.getvalue()
    out = OUT_DIR / f"{book_id}-{suffix}.jpg"
    out.write_bytes(payload)
    (B64_DIR / f"{book_id}-{suffix}.jpg.base64.txt").write_text(
        base64.b64encode(payload).decode("ascii") + "\n", encoding="ascii")
    print(f"{book_id} {suffix}: {preview.size}, {len(payload)} bytes")

def main():
    with QUEUE.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream, delimiter=";"))
    seen = set()
    for row in rows:
        book_id = row["buch_id"]
        if book_id in seen or not book_id.startswith("B") or len(book_id) != 6:
            raise ValueError(f"Invalid book ID {book_id}")
        seen.add(book_id)
        canvas = make_view(SVG_DIR / f"{book_id}.svg")
        # Both rotations: publishers print vertical spine text in both directions.
        save_jpeg_and_b64(book_id, "links", canvas.rotate(90, expand=True))
        save_jpeg_and_b64(book_id, "rechts", canvas.rotate(270, expand=True))
    print(f"Finished {len(seen)} original-pixel crop views; source photos unchanged.")

def make_neighbor_crops():
    """For every still-open ID use the COMPLETE original shelf photo, not the old SVG's embedded tile.

    Existing SVG viewBoxes provide approximate locations only; add generous extra
    photo pixels on BOTH sides to retain the requested neighboring books.
    Save both a close view and a broad verification view for safe manual checking.
    Never edit originals, invent titles, or renumber inventory IDs.
    """
    pending = ROOT / "daten/nachkontrolle/nicht-erkannt.csv"
    with pending.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter=";"))
    inventory = ROOT / "daten/buecher.csv"
    with inventory.open(newline="", encoding="utf-8") as fh:
        books = {r["buch_id"]: r for r in csv.DictReader(fh, delimiter=";")}
    if len(rows) != 30:
        raise ValueError(f"Expected 30 still-open IDs; got {len(rows)}. Check queue first.")

    for row in rows:
        book_id = row["ID"]
        if book_id not in books:
            raise ValueError(f"Missing inventory entry: {book_id}")
        original_rel = books[book_id]["foto_referenz"]
        original = ROOT / original_rel
        if not original.is_file() or not original.resolve().is_relative_to((ROOT / "bilder/originale").resolve()):
            raise ValueError(f"Missing or invalid original for {book_id}: {original_rel}")
        root = ET.parse(SVG_DIR / f"{book_id}.svg").getroot()
        vx, vy, vw, vh = [float(x) for x in root.attrib["viewBox"].replace(",", " ").split()]
        with Image.open(original) as original_photo:
            original_photo.load()
            im = original_photo.convert("RGB")
        w, h = im.size
        if w < 2000 or h < 2000:
            raise ValueError(f"Original resolution unexpected for {book_id}: {im.size}")
        # The historic SVG focus can exclude the preceding book. Anchor 350 px
        # further left, then include plenty of native pixels in BOTH directions.
        center_x = vx + vw / 2 - 350
        top = max(0, int(vy) - 120)
        bottom = min(h, int(vy + vh) + 120)
        for suffix, width, quality in (("nah-mit-nachbarn", 2300, 86),
                                       ("kontext-gesamt", 3800, 82)):
            left = max(0, min(int(round(center_x - width / 2)), w - width))
            right = min(w, left + width)
            if right - left < 1000 or bottom - top < 1500:
                raise ValueError(f"Invalid crop for {book_id}: {left},{top},{right},{bottom}")
            picture = im.crop((left, top, right, bottom))
            dest = OUT_DIR / f"{book_id}-{suffix}.jpg"
            picture.save(dest, "JPEG", quality=quality, optimize=True, subsampling=0)
            print(f"{book_id} {suffix}: {left},{top} - {right},{bottom} -> {picture.size}, {dest.stat().st_size} bytes")
    print(f"Generated {len(rows) * 2} neighbor/context views directly from full-resolution originals.")

if __name__ == "__main__":
    main()
    make_neighbor_crops()
