"""A48 Q1: classify 'turns up to a local relabeling'.

A looser action = site permutation + an on-site rotation S_g(y) in SO(3) = Aut(M_2(C)), with the
group law S_gh(y) = S_g(y) S_h(g^-1 y).  Shapiro-type reduction: it is a frame change of a uniform
action given by a homomorphism rho: Stab -> SO(3).  Here:
 (1) exact count of Hom(H, SO(3))/conjugacy for H = O, T, D4 by real characters and determinants;
 (2) brute-force list of all homomorphisms O -> (24 Clifford rotations), sorted into those classes
     by traces (every class is realized by Pauli-preserving relabelings);
 (3) reconstruction check of the reduction on a 4^3 torus for random frames (one per class),
     with a non-cocycle control;
 (4) the Klein frame of A44: its twists are Pauli-valued and its translation twists are uniform.
"""
import itertools, signal
import numpy as np
from a48lib import *

signal.alarm(240)
rng = np.random.default_rng(48)

# ---------- (1) characters ----------
print("(1) Hom(H, SO(3)) up to conjugacy, by real characters (det must be trivial)")
# O = S4: classes [e, C3 (8), C2 axis (3), C4 (6), C2' face-diagonal (6)]
O_irr = {'A1': ([1, 1, 1, 1, 1], 'A1'), 'A2': ([1, 1, 1, -1, -1], 'A2'),
         'E': ([2, -1, 2, 0, 0], 'A2'), 'T1': ([3, 0, -1, 1, -1], 'A1'), 'T2': ([3, 0, -1, -1, 1], 'A2')}
# det of each irrep as a 1-dim character name; group of 1-dim chars {A1, A2} = Z2
def count_reps(irr, onedim_mult, dims_needed=3):
    names = list(irr)
    # enumerate multisets with total dimension 3
    res = []
    def rec(start, dim_left, cur):
        if dim_left == 0:
            res.append(tuple(cur)); return
        for k in range(start, len(names)):
            d = irr[names[k]][0][0]
            if d <= dim_left:
                rec(k, dim_left - d, cur + [names[k]])
    rec(0, dims_needed, [])
    good = []
    for c in res:
        det = onedim_mult['unit']
        for n in c:
            det = onedim_mult[(det, irr[n][1])]
        if det == onedim_mult['unit']:
            good.append(c)
    return res, good
O_mult = {'unit': 'A1', ('A1', 'A1'): 'A1', ('A1', 'A2'): 'A2', ('A2', 'A1'): 'A2', ('A2', 'A2'): 'A1'}
allO, goodO = count_reps(O_irr, O_mult)
print("   O: 3-dim real reps %d, with det = 1: %d -> %s" % (len(allO), len(goodO), goodO))
# T = A4: real irreps A (1), R2 (2-dim real = E'+E''), T (3); no nontrivial real 1-dim character
T_irr = {'A': ([1], 'A'), 'R2': ([2], 'A'), 'T': ([3], 'A')}
T_mult = {'unit': 'A', ('A', 'A'): 'A'}
allT, goodT = count_reps(T_irr, T_mult)
print("   T: 3-dim real reps %d, with det = 1: %d -> %s" % (len(allT), len(goodT), goodT))
# D4: 1-dim chars A1,A2,B1,B2 (Klein group under product), E with det = A2
k4 = {'A1': (0, 0), 'A2': (0, 1), 'B1': (1, 0), 'B2': (1, 1)}
inv4 = {v: k for k, v in k4.items()}
D4_mult = {'unit': 'A1'}
for a in k4:
    for b in k4:
        D4_mult[(a, b)] = inv4[((k4[a][0] + k4[b][0]) % 2, (k4[a][1] + k4[b][1]) % 2)]
D4_irr = {'A1': ([1], 'A1'), 'A2': ([1], 'A2'), 'B1': ([1], 'B1'), 'B2': ([1], 'B2'), 'E': ([2], 'A2')}
allD, goodD = count_reps(D4_irr, D4_mult)
print("   D4: 3-dim real reps %d, with det = 1: %d -> %s" % (len(allD), len(goodD), goodD))

# ---------- (2) brute force into the Clifford rotations ----------
print("(2) all homomorphisms O -> 24 Clifford rotations, classified by traces on C4 and C3")
Ogrp = GROUPS['O (24 turns)']
H = homs(Ogrp, [C4[2], C3d])
def classify(phi):
    t4 = int(np.trace(ROT[phi[C4[2]]])); t3 = int(np.trace(ROT[phi[C3d]]))
    return {(3, 3): 'trivial', (-1, 3): 'sign twist', (-1, 0): 'axis soldering (D3)',
            (1, 0): 'soldered (Q3 class)'}.get((t4, t3), 'other(%d,%d)' % (t4, t3))
from collections import Counter
cnt = Counter(classify(p) for p in H)
print("   number of homomorphisms: %d; by class: %s" % (len(H), dict(cnt)))
print("   soldered-class homs = conjugates of the identity: %s" %
      (sorted(tuple(p[g] for g in Ogrp) for p in H if classify(p).startswith('soldered')) ==
       sorted(tuple(MUL[MUL[c][g]][INV[c]] for g in Ogrp) for c in range(24))))
for name, grp, gens in [('T (12 even turns)', GROUPS['T (12 even turns)'], [C2[2], C3d]),
                        ('D2', GROUPS['D2 (3 axis half-turns)'], [C2[0], C2[2]])]:
    Hs = homs(grp, gens)
    print("   homs %s -> Clifford rotations: %d" % (name, len(Hs)))

# ---------- (3) reduction check on a 4^3 torus ----------
print("(3) frame-change reduction on a 4^3 torus (random frames, one rep per class)")
L = 4
sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
sidx = {s: k for k, s in enumerate(sites)}
def act(g, s):
    t, k = g
    v = ROT[k] @ np.array(s) + np.array(t)
    return tuple(int(c) % L for c in v)
def compose(g, h):  # (g h)(s) = g(h(s))
    tg, kg = g; th, kh = h
    t = tuple(int(c) % L for c in (ROT[kg] @ np.array(th) + np.array(tg)))
    return (t, MUL[kg][kh])
def ginv(g):
    t, k = g; ki = INV[k]
    tt = tuple(int(c) % L for c in (-(ROT[ki] @ np.array(t))))
    return (tt, ki)
def rand_so3():
    q = rng.normal(size=4); q /= np.linalg.norm(q)
    a, b, c, d = q
    return np.array([[a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c)],
                     [2*(b*c+a*d), a*a-b*b+c*c-d*d, 2*(c*d-a*b)],
                     [2*(b*d-a*c), 2*(c*d+a*b), a*a-b*b-c*c+d*d]])
reps = {}
for p in H:
    reps.setdefault(classify(p), p)
G_elems = [((tx, ty, tz), k) for tx in range(L) for ty in range(L) for tz in range(L) for k in range(24)]
for cname, rho in reps.items():
    F = [rand_so3() for _ in sites]
    def S(g, y):
        gi = ginv(g)
        return F[sidx[y]] @ ROT[rho[g[1]]] @ F[sidx[act(gi, y)]].T
    worst = 0.0
    for _ in range(400):
        g = G_elems[rng.integers(len(G_elems))]; h = G_elems[rng.integers(len(G_elems))]
        y = sites[rng.integers(len(sites))]
        lhs = S(compose(g, h), y); rhs = S(g, y) @ S(h, act(ginv(g), y))
        worst = max(worst, np.linalg.norm(lhs - rhs))
    # reconstruction: F'(y) = S_{t_y}(y), rho'(k) = S_k(0) = F(0) rho F(0)^T
    Frec = [S((y, ID), y) for y in sites]
    rec_err = max(np.linalg.norm(Frec[sidx[y]] - F[sidx[y]] @ F[0].T) for y in sites)
    rho_err = max(np.linalg.norm(S(((0, 0, 0), k), (0, 0, 0)) - F[0] @ ROT[rho[k]] @ F[0].T) for k in Ogrp)
    print("   %-24s cocycle residual %.1e; F recovered up to F(0): %.1e; rho recovered: %.1e" %
          (cname, worst, rec_err, rho_err))
# control: an on-site twist that is not a cocycle (random per (g, y)) breaks the group law
tw = {}
def Sbad(g, y):
    kk = (g, y)
    if kk not in tw:
        tw[kk] = rand_so3()
    return tw[kk] @ ROT[g[1]]
bad = 0.0
for _ in range(50):
    g = G_elems[rng.integers(len(G_elems))]; h = G_elems[rng.integers(len(G_elems))]
    y = sites[rng.integers(len(sites))]
    bad = max(bad, np.linalg.norm(Sbad(compose(g, h), y) - Sbad(g, y) @ Sbad(h, act(ginv(g), y))))
print("   control (random twists, no group law): residual %.2f" % bad)

# ---------- (4) Klein frame ----------
print("(4) A44's Klein frame V_x = (i s1)^x1 (i s2)^x2 (i s3)^x3 on an 8^3 torus")
L8 = 8
def Rk(s):
    x1, x2, x3 = s
    return np.diag([(-1) ** (x2 + x3), (-1) ** (x1 + x3), (-1) ** (x1 + x2)])
vals = set(); trans = {}
for k in range(24):
    for s in itertools.product(range(L8), repeat=3):
        gs = tuple(int(c) % L8 for c in ROT[k] @ np.array(s))
        Sg = Rk(gs) @ ROT[k] @ Rk(s).T            # twist at target site gs
        tw_ = Sg @ ROT[k].T
        vals.add(key(tw_))
for a in range(3):
    e = np.zeros(3, dtype=int); e[a] = 1
    tws = set()
    for s in itertools.product(range(L8), repeat=3):
        ys = tuple(int(c) % L8 for c in np.array(s) + e)
        tws.add(key(Rk(ys) @ Rk(s).T))
    trans[a] = tws
print("   distinct on-site twists used by the 24 turns: %d, all diagonal +-1 (Pauli relabelings): %s" %
      (len(vals), all(np.count_nonzero(np.array(v).reshape(3, 3) - np.diag(np.diag(np.array(v).reshape(3, 3)))) == 0 for v in vals)))
for a in range(3):
    print("   translation e_%d twist: %s (uniform over sites: %s)" % (a + 1, [np.diag(np.array(v).reshape(3, 3)).tolist() for v in trans[a]], len(trans[a]) == 1))
print("done")
