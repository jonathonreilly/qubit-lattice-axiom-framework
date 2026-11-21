# Map Dimock 1712.10029 TeX source to equation and lemma numbers (bookkeeping only).
import re, sys
src = open(sys.argv[1]).read()
lines = src.split('\n')
# positions of numbered items
eq = 0; lem = 0
out = []
for i, line in enumerate(lines, 1):
    # strip comments
    l = re.sub(r'(?<!\\)%.*', '', line)
    for m in re.finditer(r'\\be\b(?!a)|\\begin\{equation\}|\\begin\{lem\}|\\label\{([^}]*)\}', l):
        t = m.group(0)
        if t.startswith('\\be') or t.startswith('\\begin{equation'):
            eq += 1; out.append((i, 'eq', eq, ''))
        elif t.startswith('\\begin{lem'):
            lem += 1; out.append((i, 'lem', lem, ''))
        else:
            out.append((i, 'label', None, m.group(1)))
lo, hi = int(sys.argv[2]), int(sys.argv[3])
for (i, k, n, lab) in out:
    if lo <= i <= hi:
        print(i, k, n if n is not None else '', lab)
