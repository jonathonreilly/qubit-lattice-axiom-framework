#!/usr/bin/env python3
"""Entropy of the frozen-state SFT of rule A on a cylinder (periodic width m): ln lambda(m) from power iteration of the (prev,cur)-row transfer."""
import sys, time
import numpy as np
from math import log

def lam(m, A, n=60, periodic=True):
    Aarr = np.zeros(8, dtype=bool)
    for a in A: Aarr[a] = True
    bits = np.array([[(x >> j) & 1 for j in range(m)] for x in range(1 << m)], dtype=np.int8)
    def hor(b):
        h = np.roll(b, 1) + np.roll(b, -1) if periodic else None
        return h
    def ok(prev, cur):
        b = bits[cur]; h = np.roll(b, 1) + np.roll(b, -1)
        if m == 1: h = 2 * b
        if m == 2: h = 2 * np.roll(b, 1)
        k = (h + bits[prev])[None, :] + bits
        return ~((Aarr[k]) & (b[None, :] == 0)).any(axis=1)
    cache = {}
    def trans(s):
        if s not in cache:
            p, c = s
            cache[s] = [(c, x) for x in np.nonzero(ok(p, c))[0].tolist()]
        return cache[s]
    # cylinder open in the row direction: start with prev=0 (outside), use long n and take ratio of totals.
    cnt = {(0, c): 1.0 for c in range(1 << m)}
    logs = []
    tot_prev = None
    lognorm = 0.0
    for it in range(n):
        nxt = {}
        for s, v in cnt.items():
            for t in trans(s):
                nxt[t] = nxt.get(t, 0.0) + v
        tot = sum(nxt.values())
        if tot == 0: return None
        for t in nxt: nxt[t] /= tot
        logs.append(log(tot))
        cnt = nxt
    return logs[-1], np.mean(logs[-6:]), len(cnt)

if __name__ == "__main__":
    A = tuple(int(c) for c in sys.argv[1]); mmax = int(sys.argv[2]); n = int(sys.argv[3])
    prev = None
    for m in range(3, mmax + 1):
        t0 = time.time()
        r = lam(m, A, n)
        if r is None: print(m, None); continue
        ll = r[1]
        print(f"m={m:2d} ln lambda_per={ll:.4f} per-site={ll/m:.4f} delta_vs_prev={'' if prev is None else '%.4f'%(ll-prev)} states={r[2]} ({time.time()-t0:.1f}s)", flush=True)
        prev = ll
