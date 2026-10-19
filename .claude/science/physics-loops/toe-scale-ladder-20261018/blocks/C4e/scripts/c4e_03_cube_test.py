#!/usr/bin/env python3
"""Exhaustive test of G(F(c)) = c and F(G(c)) = c for the cube rule on all k-magnon
configurations inside a box (lex-min magnon fixed at the origin; translation invariance).
Usage: c4e_03_cube_test.py k boxside [rule]
Prints the first failures (if any)."""
import sys, os, itertools, time
sys.path.insert(0, os.path.dirname(__file__))
from c4e_cube import F, G
k = int(sys.argv[1]); L = int(sys.argv[2]); rule = sys.argv[3] if len(sys.argv) > 3 else 'v1'
O = (0, 0, 0)
sites = [v for v in itertools.product(range(-L + 1, L), repeat=3) if v > O and max(map(abs, v)) < L]
sites = [v for v in sites if all(abs(x) < L for x in v)]
n = bad = 0; t0 = time.time(); ex = []
for rest in itertools.combinations(sites, k - 1):
    # keep only configs whose bounding box side <= L (diameter <= L-1)
    pts = (O,) + rest
    if max(max(p[i] for p in pts) - min(p[i] for p in pts) for i in range(3)) > L - 1: continue
    c = frozenset(pts); n += 1
    f = F(c, rule)
    ok = (G(f, rule) == c) and (F(G(c, rule), rule) == c)
    if not ok:
        bad += 1
        if len(ex) < 8: ex.append((sorted(c), sorted(f), sorted(G(f, rule))))
print('rule=%s k=%d diameter<=%d: configs=%d failures=%d (%.0fs)' % (rule, k, L - 1, n, bad, time.time() - t0))
for e in ex: print('  c=%s\n   F(c)=%s\n   G(F(c))=%s' % e)
