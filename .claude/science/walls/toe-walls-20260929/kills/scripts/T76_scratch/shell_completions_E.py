#!/usr/bin/env python3
"""Map's conditional test on rule E: fix the outermost shell of a reachable frozen state; count interior completions.
Also with a thicker shell (depth 2)."""
import sys, collections
from math import log
import reachE_fast as F, reachE as R
for L in range(3, int(sys.argv[1]) + 1):
    fs = F.frozen_all(L)
    nbs = R.make(L); memo = {}
    rs = [rows for rows in fs if R.reachable(rows, L, nbs, memo)]
    out = []
    for depth in (1, 2):
        groups = collections.defaultdict(list)
        for rows in rs:
            key = tuple((r, q, (rows[r] >> q) & 1) for r in range(L) for q in range(L) if min(r, q, L - 1 - r, L - 1 - q) < depth)
            groups[key].append(rows)
        mx = max(len(v) for v in groups.values())
        out.append((depth, len(groups), mx))
    print(f"L={L:2d} reachable={len(rs):5d} | shell depth1: distinct shells={out[0][1]:5d} max completions={out[0][2]:3d} | depth2: distinct={out[1][1]:5d} max completions={out[1][2]:3d}", flush=True)
