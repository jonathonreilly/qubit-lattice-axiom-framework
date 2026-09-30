#!/usr/bin/env python3
"""Gadget search v2: DFS over sealed patterns; leaf test = reachability (peelability) with component memo and a node budget."""
import sys, time, re
from gadget_search import window
sys.setrecursionlimit(1000000)

class Budget(Exception): pass

def peel(mask, nb, Aset, budget=30000):
    n = len(nb)
    memo = {}
    cnt = [0]
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
        cnt[0] += 1
        if cnt[0] > budget: raise Budget()
        deg = {v: sum(1 for u in nb[v] if u in comp) for v in comp}
        ok = False
        for v in sorted(comp, key=lambda v: -deg[v]):
            if deg[v] in Aset:
                if all(rc(c) for c in comps(comp - {v})):
                    ok = True; break
        memo[comp] = ok
        return ok
    S = {v for v in range(n) if (mask >> v) & 1}
    try:
        return all(rc(c) for c in comps(S))
    except Budget:
        return None

def find(shape, A, cap=20000, need=2):
    Aset = set(A); d = len(shape)
    sites, nb, o = window(shape); n = len(sites)
    nbm = [sum(1 << u for u in nb[v]) for v in range(n)]
    badk = []
    for v in range(n):
        badk.append({kk for kk in range(2 * d + 1) if any((kk + j) in Aset for j in range(o[v] + 1))})
    ready = [[] for _ in range(n)]
    for v in range(n): ready[max([v] + nb[v])].append(v)
    good = []; leaves = [0]; unk = [0]; capped = [False]
    def rec(i, mask):
        if capped[0] or len(good) >= need: return
        if i == n:
            leaves[0] += 1
            if leaves[0] > cap: capped[0] = True; return
            r = True if mask == 0 else peel(mask, nb, Aset)
            if r: good.append(mask)
            elif r is None: unk[0] += 1
            return
        for val in (1, 0):
            m2 = mask | (val << i); ok = True
            for v in ready[i]:
                if not (m2 >> v) & 1 and (m2 & nbm[v]).bit_count() in badk[v]: ok = False; break
            if ok: rec(i + 1, m2)
    rec(0, 0)
    return good, leaves[0], unk[0], capped[0]

if __name__ == "__main__":
    d = int(sys.argv[1]); A = tuple(int(c) for c in sys.argv[2])
    shapes = [tuple(int(x) for x in s.split("x")) for s in sys.argv[3].split(",")]
    for sh in shapes:
        t0 = time.time()
        g, lv, unk, cp = find(sh, A)
        print(d, "A=", "".join(map(str, A)), sh, "good", len(g), "leaves", lv, "unknown", unk, "capped", cp, f"{time.time()-t0:.1f}s", flush=True)
        if len(g) >= 2: break
