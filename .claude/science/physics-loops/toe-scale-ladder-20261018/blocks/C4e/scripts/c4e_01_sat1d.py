#!/usr/bin/env python3
"""1D intuition probe (not part of the 3D claim).
SAT search: reversible CA F on {0,1}^Z with radius r (F and inverse G both radius r),
number conserving, F(0)=0, isolated single magnons frozen, isolated adjacent pair '11'
moves right by 1.  Usage: c4e_01_sat1d.py r
"""
import sys, itertools
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool

r = int(sys.argv[1]); W = 2*r+1
pool = IDPool()
def fv(w): return pool.id(('f', w))
def gv(w): return pool.id(('g', w))
cls = []
pats = list(itertools.product((0, 1), repeat=W))
zero = (0,)*W
cls += [[-fv(zero)], [-gv(zero)]]
# composition G(F(u)) center = u center, for every window u of length 4r+1; and F(G(u)).
for (A, B) in ((fv, gv), (gv, fv)):
    for u in itertools.product((0, 1), repeat=4*r+1):
        subs = [u[i:i+W] for i in range(2*r+1)]  # windows for F values at positions r..3r
        c = u[2*r]
        # for each possible output z of the middle window: (A(subs)=z) -> B(z)=c
        for z in itertools.product((0, 1), repeat=W):
            lits = [(-A(s) if zi else A(s)) for s, zi in zip(subs, z)]
            lits.append(B(z) if c else -B(z))
            cls.append(lits)
# number conservation on all periodic configs of period p<=P
P = 4*r+2
top = [pool.top]
def card_eq(lits, k):
    global cls
    e = CardEnc.equals(lits=lits, bound=k, top_id=pool.top, encoding=EncType.seqcounter)
    pool.occupy(pool.top+1, e.nv); pool.top = max(pool.top, e.nv)
    cls += e.clauses
for p in (range(1, P+1) if len(sys.argv)<3 else []):
    for cfg in itertools.product((0, 1), repeat=p):
        lits = [fv(tuple(cfg[(x+j-r) % p] for j in range(W))) for x in range(p)]
        k = sum(cfg)
        # merge duplicate lits by counting? CardEnc handles repeated lits fine only if distinct; use multiset trick
        card_eq(lits, k)
# finite-config spec
def F_constraint(cfg_set, img_set, lo, hi):
    for x in range(lo, hi):
        w = tuple(1 if (x+j-r) in cfg_set else 0 for j in range(W))
        v = fv(w)
        cls.append([v] if x in img_set else [-v])
F_constraint({0}, {0}, -3*r, 3*r)
F_constraint({0, 1}, {1, 2}, -3*r, 3*r+2)
s = Cadical153(bootstrap_with=cls)
ok = s.solve()
print('r=%d SAT=%s' % (r, ok))
if ok:
    m = set(l for l in s.get_model() if l > 0)
    f = {w: int(fv(w) in m) for w in pats}
    def F(cfg, L=40):
        return {x for x in range(-L, L) if f[tuple(1 if (x+j-r) in cfg else 0 for j in range(W))]}
    for start in ({0, 1, 5}, {0, 1, 3}, {0, 1, 4, 5}, {0, 1, 2}, {0, 1, 6, 7, 9}):
        c = start; traj = []
        for t in range(14):
            traj.append(''.join('1' if x in c else '.' for x in range(-4, 30)))
            c = F(c)
        print('\n'.join(traj)); print()
    nonid = {w: v for w, v in f.items() if v != w[r]}
    print('non-identity entries:', len(nonid))
    for w, v in sorted(nonid.items()): print(''.join(map(str, w)), '->', v)
