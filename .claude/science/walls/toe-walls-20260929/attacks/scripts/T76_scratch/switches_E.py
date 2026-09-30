#!/usr/bin/env python3
"""Rule E: are there local switches (two reachable frozen states differing on a small cluster) far from the box boundary?"""
import sys, collections
import reachE_fast as F, reachE as R
L = int(sys.argv[1]); maxd = int(sys.argv[2])
fs = F.frozen_all(L)
nbs = R.make(L); memo = {}
rs = [rows for rows in fs if R.reachable(rows, L, nbs, memo)]
print("L", L, "frozen", len(fs), "reachable", len(rs))
def tomask(rows):
    m = 0
    for r, rm in enumerate(rows): m |= rm << (r * L)
    return m
ms = [tomask(r) for r in rs]
def depth(i):  # distance from box boundary of site index i
    r, q = divmod(i, L)
    return min(r, q, L - 1 - r, L - 1 - q)
best = collections.Counter()
ex = {}
for a in range(len(ms)):
    for b in range(a + 1, len(ms)):
        x = ms[a] ^ ms[b]
        pc = x.bit_count()
        if pc <= maxd:
            sites = [i for i in range(L * L) if (x >> i) & 1]
            dmin = min(depth(i) for i in sites)
            key = (pc, dmin)
            best[key] += 1
            ex.setdefault(key, (a, b))
print("diff size, min depth of diff sites -> number of pairs")
for k in sorted(best): print(k, best[k])
deepest = max((k[1] for k in best), default=None)
print("deepest local switch (min depth of its sites):", deepest)
