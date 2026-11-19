import sys
sys.path.append("LOCAL:Library/Python/3.13/lib/python/site-packages")
import pypdf
src, out = sys.argv[1], sys.argv[2]
r = pypdf.PdfReader(src)
with open(out, "w") as fh:
    for i, p in enumerate(r.pages, 1):
        try:
            t = p.extract_text() or ""
        except Exception as e:
            t = f"[extract error {e!r}]"
        fh.write(f"\n=== PAGE {i} ===\n{t}\n")
print(src, len(r.pages), "pages ->", out)
