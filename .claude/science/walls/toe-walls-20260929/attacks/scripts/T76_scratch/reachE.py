#!/usr/bin/env python3
"""Reachability for rule E (forbidden k=1): reverse-peeling; delete v if its current degree != 1.  Component-wise memo."""
import sys, time, itertools
import counts2d as c
from math import log
sys.setrecursionlimit(100000)

def comps(S, nbs):
    S = set(S); out = []
    while S:
        s = S.pop(); comp = {s}; st = [s]
        while st:
            x = st.pop()
            for y in nbs[x]:
                if y in S:
                    S.discard(y); comp.add(y); st.append(y)
        out.append(frozenset(comp))
    return out

def make(L):
    nbs = {}
    for r in range(L):
        for q in range(L):
            nbs[(r, q)] = [(r + a, q + b) for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)) if 0 <= r + a < L and 0 <= q + b < L]
    return nbs

def reach_comp(comp, nbs, memo):
    # normalise by translation
    mr = min(r for r, q in comp); mq = min(q for r, q in comp)
    key = frozenset((r - mr, q - mq) for r, q in comp)
    if key in memo: return memo[key]
    if len(comp) == 1: memo[key] = True; return True
    if len(comp) == 2: memo[key] = False; return False
    # try each deletable vertex (deg != 1 within comp)
    deg = {v: sum(1 for u in nbs[v] if u in comp) for v in comp}
    ok = False
    # prefer deg 0 (impossible in connected comp>1) then deg>=2
    for v in sorted(comp, key=lambda v: -deg[v]):
        if deg[v] == 1: continue
        rest = comp - {v}
        if all(reach_comp(cc, nbs, memo) for cc in comps(rest, nbs)):
            ok = True; break
    memo[key] = ok
    return ok

def reachable(rows, L, nbs, memo):
    S = {(r, q) for r in range(L) for q in range(L) if (rows[r] >> q) & 1}
    return all(reach_comp(cc, nbs, memo) for cc in comps(S, nbs))

if __name__ == "__main__":
    Lmax = int(sys.argv[1])
    memo = {}
    for L in range(2, Lmax + 1):
        t0 = time.time()
        fs = c.frozen_states(L, (0, 2, 3, 4)) if L <= 12 else None
        nbs = make(L)
        n = sum(1 for rows in fs if reachable(rows, L, nbs, memo))
        print(f"L={L} frozen={len(fs)} reachable={n}  ({time.time()-t0:.1f}s, memo={len(memo)})", flush=True)
