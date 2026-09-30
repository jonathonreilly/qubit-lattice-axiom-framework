#!/usr/bin/env python3
"""Rule E (A={0,2,3,4}, forbidden k=1): enumerate ALL frozen states of the sealed LxL box by row DFS (bit ops), test reachability by
reverse peeling (component memo).  Reports N_frozen(L), N_reach(L)."""
import sys, time
from math import log
import reachE as R
sys.setrecursionlimit(100000)

def frozen_all(L):
    full = (1 << L) - 1
    out = []
    def succ(p, c):
        l = (c << 1) & full; r = c >> 1
        empty = ~c & full
        two = (p & l) | (p & r) | (l & r)
        if two & empty: return None
        s0 = ~(p | l | r) & full
        forced1 = empty & s0
        return forced1, c
    def rec(rows, p, c):
        if len(rows) == L:
            s = succ(p, c)
            if s is not None and s[0] == 0:   # next row = 0 must be allowed: no empty site needs a recorded southern neighbour
                out.append(tuple(rows))
            return
        s = succ(p, c)
        if s is None: return
        f1, free = s
        sub = free
        while True:
            nxt = f1 | sub
            rec(rows + [nxt], c, nxt)
            if sub == 0: break
            sub = (sub - 1) & free
    for c0 in range(1 << L):
        rec([c0], 0, c0)
    return out

if __name__ == "__main__":
    Lmin, Lmax = int(sys.argv[1]), int(sys.argv[2])
    memo = {}
    for L in range(Lmin, Lmax + 1):
        t0 = time.time()
        fs = frozen_all(L)
        t1 = time.time()
        nbs = R.make(L)
        n = sum(1 for rows in fs if R.reachable(rows, L, nbs, memo))
        print(f"L={L:2d} frozen={len(fs):8d} reachable={n:6d} ln N={log(n) if n else 0:.3f} lnN/L={log(n)/L if n else 0:.3f} lnN/L^2={log(n)/L**2 if n else 0:.4f}  (enum {t1-t0:.1f}s, reach {time.time()-t1:.1f}s, memo {len(memo)})", flush=True)
