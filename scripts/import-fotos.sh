#!/usr/bin/env bash
# Importiert unveränderte Regal-Originalfotos aus dem Chat-ZIP in dieses private Git-Repository.
# Verwendung innerhalb eines Git-Clones: bash scripts/import-fotos.sh /pfad/zum/fotoarchiv.zip
set -euo pipefail

if [[ $# -ne 1 ]]; then
  printf 'Verwendung: bash scripts/import-fotos.sh /pfad/zum/fotoarchiv.zip\n' >&2
  exit 2
fi
ARCHIV="$(realpath "$1")"
[[ -f "$ARCHIV" ]] || { echo "Archiv fehlt: $ARCHIV" >&2; exit 2; }
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
[[ -d .git ]] || { echo "Nur in einem geklonten Git-Repository ausfuehren." >&2; exit 2; }
ORIGIN="$(git remote get-url origin)"
case "$ORIGIN" in
  *oooLITTLEooo/buecherregal* ) ;;
  * ) echo "Abbruch: unerwartetes Git-Repository ($ORIGIN)" >&2; exit 2 ;;
esac
[[ -z "$(git status --porcelain)" ]] || { echo "Bitte zuerst uncommittete Aenderungen sichern." >&2; exit 2; }

echo "1/4 Git: sync / pull --ff-only"
git pull --ff-only

echo "2/4 Verifizierter Fotoimport"
python3 - "$ARCHIV" <<'PY'
from pathlib import Path
from zipfile import ZipFile, BadZipFile
import csv, hashlib, io, sys
archive = Path(sys.argv[1])
root = Path.cwd()
manifest = root / "daten/fotos.csv"
with manifest.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f, delimiter=";")
    columns = reader.fieldnames
    assert columns and {"dateiname_git","sha256","upload_status"}.issubset(columns)
    rows = list(reader)
count = 0
try:
    with ZipFile(archive, "r") as z:
        names = set(z.namelist())
        for row in rows:
            filename = row["dateiname_git"]
            if not filename or "/" in filename or "\\" in filename or filename.startswith("."):
                continue
            rel = f"bilder/originale/{filename}"
            if rel not in names:
                continue
            data = z.read(rel)  # Keine ungepruefte Entpackung von ZIP-Pfaden
            digest = hashlib.sha256(data).hexdigest()
            if digest.lower() != row["sha256"].lower():
                raise RuntimeError(f"SHA256 passt nicht zu {filename}: {digest}")
            dst = root / rel
            if dst.exists() and dst.read_bytes() != data:
                raise RuntimeError(f"Bestehendes Original unterscheidet sich: {dst}")
            dst.parent.mkdir(parents=True, exist_ok=True)
            if not dst.exists():
                dst.write_bytes(data)
            row["upload_status"] = "im_git"
            count += 1
except BadZipFile as e:
    raise SystemExit(f"Ungueltiges ZIP-Archiv: {e}")
if count == 0:
    raise SystemExit("Keines der Fotos im ZIP ist in daten/fotos.csv eingetragen.")
buf = io.StringIO()
writer = csv.DictWriter(buf, columns, delimiter=";", lineterminator="\n")
writer.writeheader()
writer.writerows(rows)
manifest.write_text(buf.getvalue(), encoding="utf-8")
print(f"{count} Originalfotos verifiziert und im Git-Arbeitsverzeichnis abgelegt.")
PY

echo "3/4 Git: commit"
git add -- daten/fotos.csv bilder/originale
if git diff --cached --quiet; then
    echo "Keine neuen Aenderungen."
else
    git commit -m "photos: import and verify original bookshelf images"
    echo "4/4 Git: sync / push"
    git push
fi
echo "Fotoimport abgeschlossen. GitHub-Dateien nach Push pruefen."
