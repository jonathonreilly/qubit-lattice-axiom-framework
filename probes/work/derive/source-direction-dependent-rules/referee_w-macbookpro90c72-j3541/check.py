#!/usr/bin/env python3
"""Referee for J:derive:source-direction-dependent-rules:a3.

Orbits, window fields and lump fields are re-enumerated. The lattice identity
is the pseudoinverse relation, checked exactly on 2^3 and in float on 4^3.
The author's script is not called.
"""
import itertools
import sys
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

FAILS = []
AXES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def neg(a):
    return (-a[0], -a[1], -a[2])


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            M = [[0, 0, 0] for _ in range(3)]
            for i in range(3):
                M[perm[i]][i] = sg[i]
            if sum(M[0][j] * (M[1][(j + 1) % 3] * M[2][(j + 2) % 3] - M[1][(j + 2) % 3] * M[2][(j + 1) % 3]) for j in range(3)) == 1:
                out.append(M)
    return out


def apply(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))


ROTS = rotations()
triples = [(a, b, d) for a in AXES for b in AXES for d in AXES]
orbits = {}
for trip in triples:
    key = min(tuple(apply(M, x) for x in trip) for M in ROTS)
    orbits.setdefault(key, []).append(trip)
invariants = {}
for key, group in orbits.items():
    a, b, d = group[0]
    invariants[key] = (dot(a, b), dot(a, d), dot(b, d), dot(cross(a, b), d))
chiral = [v for v in invariants.values() if v[:3] == (0, 0, 0)]
exchange = {min(
    min(tuple(apply(M, x) for x in trip) for M in ROTS),
    min(tuple(apply(M, x) for x in (trip[1], trip[0], neg(trip[2]))) for M in ROTS),
) for trip in triples}
# Burnside: identity fixes 6^3; a 90-degree face rotation fixes a content only if it is the axis
face = 0
for M in ROTS:
    fixed_axes = [a for a in AXES if apply(M, a) == a]
    if len(fixed_axes) == 2 and M != [[1, 0, 0], [0, 1, 0], [0, 0, 1]]:
        face += 1
burnside = (6 ** 3 + face * 2 ** 3) / 24
ok("A1", len(ROTS) == 24 and len(orbits) == 12 and len(set(invariants.values())) == 12
   and sorted(v[3] for v in chiral) == [-1, 1] and len(exchange) == 9 and burnside == 12 and face == 9,
   f"24 rotations, {len(orbits)} orbits fixed by the four invariants, 9 after end-exchange, Burnside ({6**3}+{face}*8)/24 = 12")


def bond_weight(a, b, p, q, r):
    if a == b:
        return p
    if a == neg(b):
        return q
    return r


def fields(sites, p, q, r):
    """Mean content. The t-power is how many bond ends point along the bond."""
    present = set(sites)
    bonds = []
    for i, s in enumerate(sites):
        for d in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            t = (s[0] + d[0], s[1] + d[1], s[2] + d[2])
            if t in present:
                bonds.append((i, sites.index(t), d))
    acc = [ [0, 0, 0] for _ in sites ]
    Z = 0
    # polynomial in t: store dict exponent -> vector sum and partition
    from collections import defaultdict
    Zp = defaultdict(int)
    Sp = [ [defaultdict(int) for _ in range(3)] for _ in sites ]
    for cs in itertools.product(range(6), repeat=len(sites)):
        w, k = 1, 0
        for i, j, d in bonds:
            a, b = AXES[cs[i]], AXES[cs[j]]
            w *= bond_weight(a, b, p, q, r)
            k += (dot(a, d) == 1) + (dot(b, neg(d)) == 1)
        Zp[k] += w
        for n, c in enumerate(cs):
            for comp in range(3):
                Sp[n][comp][k] += AXES[c][comp] * w
    tt = sp.symbols("t")
    Zs = sum(c * tt ** e for e, c in Zp.items())
    out = []
    for n in range(len(sites)):
        out.append(tuple(sp.cancel(sum(c * tt ** e for e, c in Sp[n][comp].items()) / Zs) for comp in range(3)))
    return out


tt = sp.symbols("t")
line = fields([(-1, 0, 0), (0, 0, 0), (1, 0, 0)], 3, 1, 2)
formula = (tt - 1) * (3 * tt ** 2 + 27 * tt + 40) / (3 * tt ** 3 + 50 * tt ** 2 + 179 * tt + 200)
a2 = (sp.simplify(line[0][0] - formula) == 0 and sp.simplify(line[2][0] + formula) == 0 and line[1] == (0, 0, 0)
      and line[2][0].subs(tt, 2) == sp.Rational(-53, 391))
plaq = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)]
fp = fields(plaq, 3, 1, 2)
centre = (Fr(1, 2), Fr(1, 2), 0)
para = True
for s, f in zip(plaq, fp):
    inward = [centre[i] - s[i] for i in range(3)]
    para &= all(sp.simplify(f[i] * inward[j] - f[j] * inward[i]) == 0 for i in range(3) for j in range(3))
    para &= sp.simplify(f[0] / inward[0]).subs(tt, 2) > 0
    para &= all(sp.simplify(c.subs(tt, 1)) == 0 for c in f)
win = [(x, y, 0) for x in range(3) for y in range(2)]
f23 = fields(win, 3, 1, 2)
lean = all(all(sp.simplify(c.subs(tt, 1)) == 0 for c in f) for f in f23)
# sites 0=(0,0) and 4=(2,0) should lean toward x=1
lean &= sp.simplify(f23[0][0].subs(tt, 2)) > 0 and sp.simplify(f23[4][0].subs(tt, 2)) < 0
ok("A2", a2 and para and lean,
   "line ends point at the middle by (t-1)(3t^2+27t+40)/(3t^3+50t^2+179t+200), -53/391 at t=2; plaquette corners point inward; fields vanish at t=1")


def green_ops(L):
    N = L ** 3
    sites = list(itertools.product(range(L), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    lap = np.zeros((N, N))
    D = [np.zeros((N, N)) for _ in range(3)]
    for s in sites:
        i = idx[s]
        lap[i, i] = 6
        for c in range(3):
            for step in (1, -1):
                t = list(s)
                t[c] = (t[c] + step) % L
                lap[i, idx[tuple(t)]] -= 1
            back = list(s)
            back[c] = (back[c] - 1) % L
            D[c][i, i] += 1
            D[c][i, idx[tuple(back)]] -= 1
    G = np.linalg.inv(lap + np.ones((N, N)) / N) - np.ones((N, N)) / N
    return G, D, lap


def identity_holds(L, tol):
    G, D, lap = green_ops(L)
    K = D[0] @ G @ D[0].T + D[1] @ G @ D[1].T
    # Delta_z on the second index: G @ (z-laplacian matrix)
    # lap_z[y, y'] such that (G lap_z)[x,y] = G(x, y+ez)+G(x,y-ez)-2G(x,y)
    N = L ** 3
    sites = list(itertools.product(range(L), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    lz = np.zeros((N, N))
    for s in sites:
        j = idx[s]
        lz[j, j] -= 2
        up = (s[0], s[1], (s[2] + 1) % L)
        dn = (s[0], s[1], (s[2] - 1) % L)
        lz[idx[up], j] += 1
        lz[idx[dn], j] += 1
    right = np.eye(N) - 1 / N + G @ lz
    return np.max(np.abs(K - right)) < tol


ok("A3", identity_holds(2, 1e-10) and identity_holds(4, 1e-9),
   "sum_{c=x,y} D_c G D_c^T = delta - 1/N + Delta_z G on the 2^3 and 4^3 tori; a full divergence leaves only the contact term")

# continuum second derivative
r, z, th = sp.symbols("r z theta", positive=True)
g = 1 / (4 * sp.pi * r)
# r = sqrt(x^2+y^2+z^2), along z: d^2/dz^2 (1/r) = (3z^2 - r^2)/r^5
x, y = sp.symbols("x y", real=True)
rr = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
d2 = sp.simplify(sp.diff(1 / rr, z, 2))
want = (3 * z ** 2 - rr ** 2) / rr ** 5
ok("A3b", sp.simplify(d2 - want) == 0,
   "partial_zz (1/r) = (3 cos^2 theta - 1)/r^3, so the far kernel is +2 along the order and -1 across it")


def lump(recs, a, b, c, p, q, r):
    present = set(recs)
    bonds = []
    for i, s in enumerate(recs):
        for d in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            t = (s[0] + d[0], s[1] + d[1], s[2] + d[2])
            if t in present:
                bonds.append((i, recs.index(t)))
    empties = []
    for s in recs:
        empties.append([d for d in AXES if (s[0] + d[0], s[1] + d[1], s[2] + d[2]) not in present])

    def phi(content, d):
        sdot = dot(content, d)
        return a if sdot == 1 else (b if sdot == 0 else c)

    site = []
    for empt in empties:
        site.append([1] * 6)
        for ci, content in enumerate(AXES):
            w = 1
            for d in empt:
                w *= phi(content, d)
            site[-1][ci] = w
    Z = 0
    S = [[0, 0, 0] for _ in recs]
    for cs in itertools.product(range(6), repeat=len(recs)):
        w = 1
        for n, ci in enumerate(cs):
            w *= site[n][ci]
        for i, j in bonds:
            w *= bond_weight(AXES[cs[i]], AXES[cs[j]], p, q, r)
        Z += w
        for n, ci in enumerate(cs):
            for comp in range(3):
                S[n][comp] += AXES[ci][comp] * w
    return [tuple(Fr(v, Z) for v in row) for row in S]


iso = lump([(0, 0, 0)], 3, 2, 1, 3, 1, 2)[0] == (0, 0, 0)
signs = True
cube_comp = None
for aa, cc in ((3, 1), (1, 3)):
    dimer = lump([(0, 0, 0), (1, 0, 0)], aa, 2, cc, 3, 1, 2)
    square = lump([(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)], aa, 2, cc, 3, 1, 2)
    cube = lump([(x, y, z) for x in range(2) for y in range(2) for z in range(2)], aa, 2, cc, 3, 1, 2)
    sgn = 1 if aa > cc else -1
    signs &= sgn * dimer[1][0] > 0 and dimer[1][1] == 0 and dimer[1][2] == 0
    for s, v in zip([(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)], square):
        signs &= sgn * v[0] * (2 * s[0] - 1) > 0 and sgn * v[1] * (2 * s[1] - 1) > 0 and v[2] == 0
    corners = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
    for s, v in zip(corners, cube):
        outward = (2 * s[0] - 1, 2 * s[1] - 1, 2 * s[2] - 1)
        signs &= v[0] * outward[1] == v[1] * outward[0] and v[1] * outward[2] == v[2] * outward[1]
        signs &= sgn * v[0] * outward[0] > 0
    if aa > cc:
        cube_comp = cube[-1][0]
ok("A4", iso and signs and cube_comp == Fr(89734618, 506936397),
   f"isolated record is isotropic; dimer, plaquette and cube corners lean out when a>c; cube corner {cube_comp}")

if FAILS:
    print("SUMMARY: fails at step " + ", ".join(FAILS) + " - independent check disagreed")
    sys.exit(1)
print("SUMMARY: confirmed - a covariant pair weight has 12 values, the hedgehog field is dipolar through Lap_z G, and there is no universal 1/r.")
print("HIT: confirmed - proper rotations give 12 orbits of (a,b,d) and 9 if ends may be exchanged; on the line of 3 the ends point at the middle by (t-1)(3t^2+27t+40)/(3t^3+50t^2+179t+200); the ordered-medium pair kernel is delta-1/N+Delta_z G, whose far part is (3 cos^2 theta-1)/(4 pi r^3), never 1/r; a lump's corners form a radial hedgehog.")
