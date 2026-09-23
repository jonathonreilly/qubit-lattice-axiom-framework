"""Refuting pass, block 24 (supervisor seat, disjoint machinery from the runner's checks):
(R1) the plaquette-plus-site and cube witnesses by floating-point tensor contraction (numpy einsum) against the exact rationals;
(R2) one-attachment constancy on random pendant components (random connected subsets of Z^3 of 2-4 sites attached to one recorded site
     through all their bonds to it) at random positive weights: the factor's spread over the six values (should be ~1e-12 relative);
(R3) two-attachment nonconstancy on random bridging components (attached to two recorded sites) at random positive weights, through the
     isotypic eigenvalues lambda_odd, lambda_even of the factor as a 6x6 matrix; also the degenerate rule p = q = r (both vanish);
(R4) the sphere factor 4 pi sinh(beta|w|)/(beta|w|) by quadrature at v_x.v_y in {-1, 0, 1/2, 1} (at -1 the factor is 4 pi);
(R5) the average identity mu_W^R2 = sum_omega mu(omega) mu_W^R3(.|omega) on the plaquette-plus-site in floats."""
import math
import random
from fractions import Fraction as F
from itertools import product

import numpy as np

random.seed(24); np.random.seed(24)
M = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def rel(v, w):
    if v == w: return 0
    if tuple(-c for c in v) == w: return 1
    return 2
def phi_mat(p, q, r):
    return np.array([[ [p, q, r][rel(v, w)] for w in M] for v in M], dtype=float)
# R1 plaquette + site: sites c0..c3 ring, x adjacent to c0, c1
def tv(a, b): return 0.5 * np.abs(a - b).sum()
for pqr, exact in (((3,1,2), F(78621, 4563820)), ((5,2,4), F(675203620, 64463986907)), ((2,1,2), F(221667, 30063356))):
    A = phi_mat(*pqr)
    ring = np.einsum("ab,bc,cd,da->abcd", A, A, A, A)
    R1 = ring / ring.sum()
    withx = np.einsum("abcd,ax,bx->abcd", ring, A, A)
    R2 = withx / withx.sum()
    print(f"R1 plaquette+site at {pqr}: TV float = {tv(R1, R2):.9f} vs exact {float(exact):.9f}: {abs(tv(R1,R2) - float(exact)) < 1e-9}")
A = phi_mat(3, 1, 2)
bottom = np.einsum("ab,bc,cd,da->abcd", A, A, A, A)
top = np.einsum("ab,bc,cd,da->abcd", A, A, A, A)
full = np.einsum("abcd,efgh,ae,bf,cg,dh->abcd", bottom, top, A, A, A, A)
print(f"R1 cube at (3,1,2): TV float = {tv(bottom/bottom.sum(), full/full.sum()):.9f} vs exact {float(F(9778807, 1312253264)):.9f}")
# R2 / R3 random components
def neighbors(s):
    for d in range(3):
        for e in (1, -1):
            y = list(s); y[d] += e; yield tuple(y)
def random_component(n):
    comp = {(1, 0, 0)}
    while len(comp) < n:
        s = random.choice(sorted(comp)); y = random.choice(list(neighbors(s)))
        if y != (0, 0, 0) and y not in comp: comp.add(y)
    return sorted(comp)
def factor(comp, attach, A):
    # attach: dict recorded-site -> list of comp sites adjacent; returns array over recorded values (6^len(attach))
    sites = comp; idx = {s: i for i, s in enumerate(sites)}
    bonds = [(idx[s], idx[y]) for s in sites for y in neighbors(s) if y in idx and idx[s] < idx[y]]
    rec = sorted(attach)
    out = np.zeros([6] * len(rec))
    for vals in product(range(6), repeat=len(rec)):
        tot = 0.0
        for u in product(range(6), repeat=len(sites)):
            w = 1.0
            for a, b in bonds: w *= A[u[a], u[b]]
            for k, x in enumerate(rec):
                for a in attach[x]: w *= A[vals[k], u[idx[a]]]
            tot += w
        out[vals] = tot
    return out
ok2 = True; worst = 0.0
for trial in range(6):
    n = random.randint(2, 4); comp = random_component(n)
    pqr = tuple(random.uniform(0.5, 3) for _ in range(3)); A = phi_mat(*pqr)
    att = {(0, 0, 0): [s for s in comp if (0, 0, 0) in neighbors(s)]}
    f = factor(comp, att, A)
    spread = (f.max() - f.min()) / f.mean(); worst = max(worst, spread); ok2 = ok2 and spread < 1e-10
print(f"R2 one-attachment factors on 6 random pendant components (2-4 sites, all bonds to the origin): constant to relative {worst:.1e}: {ok2}")
def isotypic(Fm):
    ones = np.ones(6) / math.sqrt(6)
    P0 = np.outer(ones, ones)
    odd = np.zeros((6, 6)); 
    for i in range(3): odd[2*i, 2*i] = odd[2*i+1, 2*i+1] = 0.5; odd[2*i, 2*i+1] = odd[2*i+1, 2*i] = -0.5
    Peven = np.eye(6) - P0 - odd
    lo = np.trace(Fm @ odd) / 3; le = np.trace(Fm @ Peven) / 2
    return lo, le
ok3 = True
for trial in range(6):
    # bridging component between x = origin and y = (2,0,0) (distance 2): a path through (1,0,0) plus random extra sites
    comp = {(1, 0, 0)}
    while len(comp) < random.randint(1, 3):
        s = random.choice(sorted(comp)); yv = random.choice(list(neighbors(s)))
        if yv not in ((0, 0, 0), (2, 0, 0)) and yv not in comp: comp.add(yv)
    comp = sorted(comp)
    pqr = tuple(random.uniform(0.5, 3) for _ in range(3)); A = phi_mat(*pqr)
    att = {(0, 0, 0): [s for s in comp if (0, 0, 0) in neighbors(s)], (2, 0, 0): [s for s in comp if (2, 0, 0) in neighbors(s)]}
    f = factor(comp, att, A)
    lo, le = isotypic(f)
    ok3 = ok3 and (abs(lo) + abs(le)) > 1e-8 * f.mean()
A = phi_mat(1.7, 1.7, 1.7); f = factor([(1, 0, 0)], {(0, 0, 0): [(1, 0, 0)], (2, 0, 0): [(1, 0, 0)]}, A); lo, le = isotypic(f)
print(f"R3 two-attachment factors on 6 random bridging components have a nonzero isotypic eigenvalue: {ok3}; at p = q = r both vanish: {abs(lo) < 1e-12 and abs(le) < 1e-12}")
nodes, weights = np.polynomial.legendre.leggauss(200)
beta = 1.3
for t in (-1.0, 0.0, 0.5, 1.0):
    w = math.sqrt(max(0.0, 2 + 2 * t))
    quad = 2 * math.pi * sum(wt * math.exp(beta * w * s) for s, wt in zip(nodes, weights))
    closed = 4 * math.pi * (math.sinh(beta * w) / (beta * w) if w > 0 else 1.0)
    print(f"R4 sphere two-attachment factor at v_x.v_y = {t}: quadrature {quad:.9f} closed form {closed:.9f}")
A = phi_mat(3, 1, 2)
ring = np.einsum("ab,bc,cd,da->abcd", A, A, A, A)
joint = np.einsum("abcd,ax,bx->abcdx", ring, A, A); joint /= joint.sum()
R2 = joint.sum(axis=4)
mix = np.zeros_like(R2)
for x in range(6):
    cond = joint[..., x] / joint[..., x].sum()
    mix += joint[..., x].sum() * cond
print(f"R5 average identity on the plaquette+site: max |R2 - sum_omega mu(omega) R3(.|omega)| = {np.abs(R2 - mix).max():.1e}")
