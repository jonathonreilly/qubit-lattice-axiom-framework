import sys
sys.path.append("LOCAL:Library/Python/3.13/lib/python/site-packages")
from pypdf import PdfReader
src, dst = sys.argv[1], sys.argv[2]
r = PdfReader(src)
with open(dst, "w") as f:
    for i, p in enumerate(r.pages):
        f.write(f"\n=== PAGE {i+1} ===\n")
        try:
            f.write(p.extract_text() or "")
        except Exception as e:
            f.write(f"[extract error {e}]")
print(len(r.pages))
