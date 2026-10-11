import sys; sys.path.append('/Users/jonBridger/Library/Python/3.12/lib/python/site-packages')
import sys, pypdf
r = pypdf.PdfReader(sys.argv[1])
with open(sys.argv[2], 'w') as f:
    for i, p in enumerate(r.pages):
        f.write(f"\n=== page {i+1} ===\n")
        f.write(p.extract_text() or "")
