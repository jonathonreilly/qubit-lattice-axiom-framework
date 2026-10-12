import sys
try:
    import fitz
    d = fitz.open(sys.argv[1]); txt = "".join(f"\n=== page {i+1} ===\n" + p.get_text() for i, p in enumerate(d))
except ImportError:
    from pypdf import PdfReader
    r = PdfReader(sys.argv[1]); txt = "".join(f"\n=== page {i+1} ===\n" + (p.extract_text() or "") for i, p in enumerate(r.pages))
open(sys.argv[2], "w").write(txt)
