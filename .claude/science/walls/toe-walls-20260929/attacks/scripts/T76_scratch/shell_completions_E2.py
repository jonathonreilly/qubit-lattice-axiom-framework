import sys, collections
import reachE_fast as F, reachE as R
Ls = [int(x) for x in sys.argv[1].split(",")]
for L in Ls:
    fs = F.frozen_all(L)
    nbs = R.make(L); memo = {}
    rs = [rows for rows in fs if R.reachable(rows, L, nbs, memo)]
    res = []
    for name, states in (("frozen", fs), ("reachable", rs)):
        for depth in (1, 2, 3):
            groups = collections.defaultdict(int)
            for rows in states:
                key = tuple((rows[r] >> q) & 1 for r in range(L) for q in range(L) if min(r, q, L - 1 - r, L - 1 - q) < depth)
                groups[key] += 1
            res.append(f"{name} d{depth}: shells={len(groups)} max={max(groups.values())}")
    print(f"L={L}: " + " | ".join(res), flush=True)
