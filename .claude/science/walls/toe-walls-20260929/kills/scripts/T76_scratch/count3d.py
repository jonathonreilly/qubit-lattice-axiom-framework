#!/usr/bin/env python3
"""3D sealed L^3 box, count-threshold rule A: enumerate frozen sets by site DFS with early frozen pruning; reachable via component peeling memo.
Usage: count3d.py <A digits> <Lmax> [cap]"""
import sys, time, itertools
from math import log
sys.setrecursionlimit(1000000)

def grid(L):
    sites = list(itertools.product(range(L), repeat=3)); idx = {s: i for i, s in enumerate(sites)}
    nb = []
    for s in sites:
        lst = []
        for k in range(3):
            for dv in (-1, 1):
                t = list(s); t[k] += dv; t = tuple(t)
                if t in idx: lst.append(idx[t])
        nb.append(lst)
    return sites, nb

def frozen_all(L, A, cap):
    Aset = set(A)
    sites, nb = grid(L); n = len(sites)
    nbm = [sum(1 << u for u in nb[v]) for v in range(n)]
    ready = [[] for _ in range(n)]
    for v in range(n):
        ready[max([v] + nb[v])].append(v)
    out = []
    def rec(i, mask):
        if len(out) >= cap: return
        if i == n:
            out.append(mask); return
        for val in (0, 1):
            m2 = mask | (val << i)
            ok = True
            for v in ready[i]:
                if not (m2 >> v) & 1 and (m2 & nbm[v]).bit_count() in Aset:
                    ok = False; break
            if ok: rec(i + 1, m2)
    rec(0, 0)
    return out, sites, nb

def reachable_set(mask, nb, Aset, memo):
    # component-wise reverse peeling: delete v if deg_in_comp(v) in A (k = number of present neighbours excluding itself)
    n = len(nb)
    def comps(S):
        S = set(S); out = []
        while S:
            s = S.pop(); comp = {s}; st = [s]
            while st:
                x = st.pop()
                for y in nb[x]:
                    if y in S: S.discard(y); comp.add(y); st.append(y)
            out.append(frozenset(comp))
        return out
    def rc(comp):
        if comp in memo: return memo[comp]
        ok = False
        if len(comp) >= 1:
            deg = {v: sum(1 for u in nb[v] if u in comp) for v in comp}
            for v in sorted(comp, key=lambda v: -deg[v]):
                if deg[v] in Aset:
                    rest = comp - {v}
                    if all(rc(c) for c in comps(rest)):
                        ok = True; break
        memo[comp] = ok
        return ok
    S = {v for v in range(n) if (mask >> v) & 1}
    return all(rc(c) for c in comps(S))

if __name__ == "__main__":
    A = tuple(int(c) for c in sys.argv[1]); Lmax = int(sys.argv[2]); cap = int(sys.argv[3]) if len(sys.argv) > 3 else 300000
    Aset = set(A)
    for L in range(2, Lmax + 1):
        t0 = time.time()
        fs, sites, nb = frozen_all(L, A, cap)
        t1 = time.time()
        memo = {}
        nr = sum(1 for m in fs if reachable_set(m, nb, Aset, memo)) if len(fs) < cap else None
        print(f"A={A} L={L} frozen={len(fs)}{'+' if len(fs)>=cap else ''} reachable={nr}  ({t1-t0:.1f}s,{time.time()-t1:.1f}s)", flush=True)
