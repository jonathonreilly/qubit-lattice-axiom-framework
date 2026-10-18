#!/usr/bin/env python3
"""Summarise orders_<variant>.out files: orders seen, distinct orders per spurion, saturation, Dirac order patterns."""
import ast, glob, re
from collections import Counter

for f in sorted(glob.glob('orders_A?-??.out')):
    lines = open(f).read().splitlines()
    pats = Counter(); orders = set(); maxd = 0; nent = 0; nmass = 0
    for ln in lines:
        m = re.match(r'\s*(\S+)\s+(\S+)\s+dir(\d+)\s+\|Stab\|=(\d+)\s+charge=(.*?) orders s1=(\[.*?\]) s2=(\[.*?\])', ln)
        if not m: continue
        nent += 1
        s1 = ast.literal_eval(m.group(6)); s2 = ast.literal_eval(m.group(7))
        def cls(x):
            return 'inf' if x == 'inf' else str(int(round(float(x))))
        c1 = sorted(cls(x) for x in s1); c2 = sorted(cls(x) for x in s2)
        if c1 != c2: print(f"{f}: seed disagreement {m.group(1)} {m.group(2)} dir{m.group(3)}: {c1} vs {c2}")
        fin = [x for x in c1 if x != 'inf']
        if fin: nmass += 1
        orders |= set(fin)
        maxd = max(maxd, len(set(fin)))
        cnt = Counter(c1)
        pats[tuple(sorted((k, v // 2) for k, v in cnt.items()))] += 1
    tail = [ln for ln in lines if ln.startswith(('odd single', 'multi-charge', 'max number', 'all finite', 'distinct finite'))]
    print(f"\n{f}: entries {nent}, with masses {nmass}; orders seen {sorted(orders)}; max distinct finite orders per spurion {maxd}")
    for t in tail: print("   ", t)
    print("    Dirac-unit order patterns (order: count of Dirac pairs) and how often:")
    for p, c in sorted(pats.items(), key=lambda x: -x[1]): print(f"      {dict(p)}  x{c}")
