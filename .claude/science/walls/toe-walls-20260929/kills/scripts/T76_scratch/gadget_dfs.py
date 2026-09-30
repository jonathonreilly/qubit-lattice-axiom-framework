#!/usr/bin/env python3
"""Gadget search by DFS over window patterns with early sealed pruning; leaf test = peelable in isolation."""
import itertools, sys, time
from gadget_search import window, peelable

def find(shape, A, cap=300000, need=2):
    Aset = set(A)
    d = len(shape)
    sites, nb, o = window(shape)
    n = len(sites)
    nbm = [sum(1 << u for u in nb[v]) for v in range(n)]
    badk = []
    for v in range(n):
        s = set()
        for kk in range(2 * d + 1):
            if any((kk + j) in Aset for j in range(o[v] + 1)): s.add(kk)
        badk.append(s)
    # sites completed when index max(v, nb[v]) assigned
    ready = [[] for _ in range(n)]
    for v in range(n):
        last = max([v] + nb[v])
        ready[last].append(v)
    good = []
    leaves = [0]
    capped = [False]
    assign = [0] * n
    def rec(i, mask):
        if capped[0] or len(good) >= need: return
        if i == n:
            leaves[0] += 1
            if leaves[0] > cap: capped[0] = True; return
            if mask == 0 or peelable(mask, nb, Aset, None):
                good.append(mask)
            return
        for val in (1, 0):
            m2 = mask | (val << i)
            ok = True
            for v in ready[i]:
                if not (m2 >> v) & 1:
                    k = bin(m2 & nbm[v]).count("1")
                    if k in badk[v]: ok = False; break
            if ok: rec(i + 1, m2)
    rec(0, 0)
    return good, leaves[0], capped[0]

if __name__ == "__main__":
    d = int(sys.argv[1]); shape = tuple(int(x) for x in sys.argv[2].split("x"))
    A = tuple(int(c) for c in sys.argv[3])
    t0 = time.time()
    g, lv, cp = find(shape, A)
    print(d, A, shape, "good", len(g), "leaves", lv, "capped", cp, f"{time.time()-t0:.1f}s")
