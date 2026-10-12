import sys
import fitz
src, dst = sys.argv[1], sys.argv[2]
d = fitz.open(src)
with open(dst, "w") as f:
    for i, p in enumerate(d):
        f.write(f"\n=====PAGE {i+1}=====\n")
        f.write(p.get_text())
print(src, len(d))
