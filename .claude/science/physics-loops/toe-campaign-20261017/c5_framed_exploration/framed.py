"""Levin-Wen style framed hopping operators: U_(v,a) = Z on edge (v,a) times X on framing edges S_a + v.
Plaquettes W_p = product of U around p; vertex A_v = X on the 6 edges at v. Search single-edge framings
S_a = {(delta_a, b_a)} for each edge direction a; keep commuting codes; T-junction sign of the vertex charge."""
import itertools, sys, pickle
import numpy as np
sys.path.insert(0, '../c4')
from stats import t_junction
X, Z = 1, 3
E = [(1,0,0),(0,1,0),(0,0,1)]
def add(p, q): return tuple(a + b for a, b in zip(p, q))
def mul(g, p, q, lab):
    g.setdefault(p, [0,0,0]); cur = g[p][q]
    if cur == 0: g[p][q] = lab
    elif cur == lab: g[p][q] = 0
    else: g[p][q] = 6 - cur - lab
def U(v, a, S):
    g = {}; mul(g, v, a, Z)
    for (d, b) in S[a]: mul(g, add(v, d), b, X)
    return g
def plaq(c, S):
    a, b = [k for k in range(3) if k != c]; g = {}
    for (v, e) in (((0,0,0), a), (E[a], b), (E[b], a), ((0,0,0), b)):
        for p, labs in U(v, e, S).items():
            for q, l in enumerate(labs):
                if l: mul(g, p, q, l)
    return {p: tuple(l) for p, l in g.items() if any(l)}
A = {}
for a in range(3):
    mul(A, (0,0,0), a, X); mul(A, tuple(-c for c in E[a]), a, X)
A = {p: tuple(l) for p, l in A.items()}
def anticomm(g1, g2, s):
    n = 0
    for p, l1 in g1.items():
        l2 = g2.get(tuple(x - t for x, t in zip(p, s)))
        if l2 is None: continue
        n += sum(1 for q in range(3) if l1[q] and l2[q] and l1[q] != l2[q])
    return n % 2
SH = list(itertools.product(range(-4, 5), repeat=3))
def commute(gs):
    for i in range(len(gs)):
        for j in range(i, len(gs)):
            if any(anticomm(gs[i], gs[j], s) for s in SH): return False
    return True
cands = [()] + [((d, b),) for d in itertools.product((-1,0,1), repeat=3) for b in range(3)]
found, n = [], 0
for Sx in cands:
    for Sy in cands:
        for Sz in cands:
            S = [Sx, Sy, Sz]
            P = [plaq(c, S) for c in range(3)]
            if not commute(P): continue
            n += 1
            r = t_junction([A] + P, 3, 0, [(1,0,0),(0,1,0),(0,0,1)], R=3)
            if r[0] == -1:
                found.append(S); print('FERMION', S, r, flush=True)
            if n % 200 == 0: print('commuting', n, 'fermions', len(found), flush=True)
print('commuting framed codes', n, 'fermionic', len(found))
pickle.dump(found, open('framed_fermions.pkl', 'wb'))
