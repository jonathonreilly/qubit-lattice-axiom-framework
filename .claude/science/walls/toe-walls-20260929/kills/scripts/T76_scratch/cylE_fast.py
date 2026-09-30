#!/usr/bin/env python3
"""Rule E (forbidden k = 1 only): fast row-transfer with determined entries.  Periodic (or open) width m.
Empty site j of row c needs exactly one recorded neighbour: n_j = 1 - p_j - h_j must be 0 or 1, else state dead."""
import sys, time
from math import log

def run(m, n, periodic=True):
    full = (1 << m) - 1
    def hmask(c):
        if periodic:
            l = ((c << 1) | (c >> (m - 1))) & full
            r = ((c >> 1) | ((c & 1) << (m - 1))) & full
            return l, r
        else:
            return (c << 1) & full, c >> 1
    def succ(p, c):
        # for each empty site j of c: need p_j + l_j + r_j + n_j == 1, where l,r horizontal nbrs of c.
        l, r = hmask(c)
        # per-bit sum s_j = p_j + l_j + r_j  (0..3)
        # empty sites: need s_j <= 1 ; n_j = 1 - s_j
        empty = ~c & full
        # s>=2 at empty site -> dead
        two = (p & l) | (p & r) | (l & r)
        if two & empty: return []
        one = (p ^ l ^ r) & ~two   # exactly one of the three set (given no two): parity 1 and not two
        # exactly-one bits: s==1
        s1 = (p ^ l ^ r) & ~two & full
        # for empty j: n_j = 1 - s_j  => n_j=1 where s==0, 0 where s==1
        s0 = ~(p | l | r) & full
        forced1 = empty & s0
        # forced0 = empty & s1 (n_j=0)
        free = c  # positions under recorded sites are free
        res = []
        # enumerate submasks of free
        sub = free
        while True:
            res.append(forced1 | sub)
            if sub == 0: break
            sub = (sub - 1) & free
        return res
    cnt = {(0, c): 1.0 for c in range(1 << m)}
    logs = []
    cache = {}
    for it in range(n):
        nxt = {}
        for s, v in cnt.items():
            t = cache.get(s)
            if t is None:
                p, c = s
                t = [(c, x) for x in succ(p, c)]
                cache[s] = t
            for u in t:
                nxt[u] = nxt.get(u, 0.0) + v
        tot = sum(nxt.values())
        for u in nxt: nxt[u] /= tot
        logs.append(log(tot))
        cnt = nxt
        if it % 8 == 0: cache = {} if len(cache) > 500000 else cache
    return sum(logs[-6:]) / 6, len(cnt)

if __name__ == "__main__":
    mmin, mmax, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    per = sys.argv[4] == "per" if len(sys.argv) > 4 else True
    for m in range(mmin, mmax + 1):
        t0 = time.time()
        ll, S = run(m, n, per)
        print(f"m={m:2d} {'per' if per else 'open'} ln lambda={ll:.4f} per-site={ll/m:.4f} states={S} ({time.time()-t0:.1f}s)", flush=True)
