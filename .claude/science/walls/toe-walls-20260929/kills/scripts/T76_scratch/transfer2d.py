#!/usr/bin/env python3
"""Frozen-state counts f(m x n) for count-threshold rule A on the sealed m x n box, by transfer over rows (width m)."""
import sys, time
import numpy as np
from math import log

def build(m, A):
    Aarr = np.zeros(8, dtype=bool)
    for a in A: Aarr[a] = True
    bits = np.array([[(x >> j) & 1 for j in range(m)] for x in range(1 << m)], dtype=np.int8)
    def ok(prev, cur):  # returns bool array over nxt masks
        b = bits[cur]
        h = np.zeros(m, dtype=np.int8); h[1:] += b[:-1]; h[:-1] += b[1:]
        k = (h + bits[prev])[None, :] + bits
        bad = Aarr[k] & (b[None, :] == 0)
        return ~bad.any(axis=1)
    return ok, bits, Aarr

def count(m, A, nmax):
    ok, bits, Aarr = build(m, A)
    # states (prev, cur); start prev=0
    cache = {}
    def trans(s):
        if s not in cache:
            prev, cur = s
            cache[s] = [(cur, x) for x in np.nonzero(ok(prev, cur))[0].tolist()]
        return cache[s]
    def endok(s):
        prev, cur = s
        b = bits[cur]
        h = np.zeros(m, dtype=np.int8); h[1:] += b[:-1]; h[:-1] += b[1:]
        k = h + bits[prev]
        return not (Aarr[k] & (b == 0)).any()
    # n = 1 rows: state (0,cur): valid iff endok
    cur_counts = {(0, c): 1 for c in range(1 << m)}
    res = {}
    for n in range(1, nmax + 1):
        res[n] = sum(v for s, v in cur_counts.items() if endok(s))
        if n == nmax: break
        nxt = {}
        for s, v in cur_counts.items():
            for t in trans(s):
                nxt[t] = nxt.get(t, 0) + v
        cur_counts = nxt
        if len(cur_counts) > 400000:
            print("state blowup", len(cur_counts)); break
    return res, len(cur_counts)

if __name__ == "__main__":
    A = tuple(int(c) for c in sys.argv[1])
    mmax = int(sys.argv[2]); nmax = int(sys.argv[3])
    for m in range(1, mmax + 1):
        t0 = time.time()
        res, S = count(m, A, nmax)
        sq = res.get(m)
        # growth rate per row for long boxes
        ns = sorted(res)
        r = [log(res[n + 1] / res[n]) for n in ns[-4:-1] if res[n] > 0 and res[n + 1] > 0]
        print(f"m={m:2d} states~{S:6d} f(m x m)={sq} ln f/m={log(sq)/m if sq else 0:.3f} ln f/m^2={log(sq)/m**2 if sq else 0:.3f}  rowgrowth ln(f_{{n+1}}/f_n) last={['%.3f'%x for x in r]}  ({time.time()-t0:.1f}s)", flush=True)
