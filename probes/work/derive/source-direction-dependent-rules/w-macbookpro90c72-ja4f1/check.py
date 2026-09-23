#!/usr/bin/env python3
"""J:derive:source-direction-dependent-rules:a3 -- worker w-macbookpro90c72-ja4f1 (claude-opus-5-5).

Direction-dependent pair weights on the six-axis menu (blocks 39-41). 'ok' lines exact (integers, Fractions, sympy);
one 'note' line floating point.
"""
import itertools, math, sys, time
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

T0 = time.time(); FAILS = []
def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)

axes = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
neg = lambda a: tuple(-x for x in a)
cross = lambda a, b: (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = [[0] * 3 for _ in range(3)]
        for i in range(3):
            M[i][perm[i]] = sg[i]
        if sp.Matrix(M).det() == 1:
            rots.append(M)
app = lambda M, v: tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))

# ------------------------------------------------------------------ D.a: covariant direction-dependent pair weights
triples = [(a, b, d) for a in axes for b in axes for d in axes]
canon = lambda t: min(tuple(app(M, x) for x in t) for M in rots)
orbits = {}
for t in triples:
    orbits.setdefault(canon(t), []).append(t)
inv = {k: (dot(v[0][0], v[0][1]), dot(v[0][0], v[0][2]), dot(v[0][1], v[0][2]), dot(cross(v[0][0], v[0][1]), v[0][2])) for k, v in orbits.items()}
good = len(rots) == 24 and len(orbits) == 12 and len(set(inv.values())) == 12
# every orbit is fixed by (a.b, a.d, b.d, (a x b).d), and the two with a, b, d mutually orthogonal differ only by handedness
chiral = [v for v in inv.values() if v[:3] == (0, 0, 0)]
good &= sorted(x[3] for x in chiral) == [-1, 1]
sym = {min(canon(t), canon((t[1], t[0], neg(t[2])))) for t in triples}
good &= len(sym) == 9
pr, qr, rr, tt = sp.symbols("p q r t", positive=True)
def prod_w(a, b, d):
    om = pr if a == b else (qr if a == neg(b) else rr)
    hh = lambda u: tt if u == 1 else 1
    return om * hh(dot(a, d)) * hh(dot(b, neg(d)))
good &= all(sp.simplify(prod_w(*t) - prod_w(t[1], t[0], neg(t[2]))) == 0 for t in triples)          # symmetric
good &= all(len({prod_w(*t) for t in ts}) == 1 for ts in orbits.values())                              # covariant
vals = {inv[k]: prod_w(*orbits[k][0]) for k in orbits}
good &= vals[(0, 0, 0, 1)] == vals[(0, 0, 0, -1)] and len(set(vals.values())) == 6
ok("D.a", good, "under the 24 proper rotations acting on sites and contents together, (a, b, d) falls into 12 orbits, each fixed by "
   "(a.b, a.d, b.d, (a x b).d): a covariant pair weight on the six-axis menu has 12 free values, the two orthogonal-triad orbits "
   "differing only by handedness; exchange of the ends with d -> -d leaves 9; the product h(a.d) h(-b.d) omega(a.b) with "
   "h(1) = t, h(0) = h(-1) = 1 is covariant, symmetric and blind to handedness, taking 6 distinct values: pt, p, rt, r, qt^2, q")

# ------------------------------------------------------------------ D.b: the content field in small occupied windows (exact in t)
def fields_t(sites, p, q, r):
    sset = set(sites); idx = {s_: i for i, s_ in enumerate(sites)}
    bonds = [(i, idx[tuple(x + e for x, e in zip(s_, d))], d) for i, s_ in enumerate(sites) for d in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
             if tuple(x + e for x, e in zip(s_, d)) in sset]
    Z = {}; S = [[{} for _ in range(3)] for _ in sites]
    for cs in itertools.product(range(6), repeat=len(sites)):
        w = 1; k = 0
        for (i, j, d) in bonds:
            a, b = axes[cs[i]], axes[cs[j]]
            w *= p if a == b else (q if a == neg(b) else r)
            k += (dot(a, d) == 1) + (dot(b, neg(d)) == 1)
        Z[k] = Z.get(k, 0) + w
        for n_, c in enumerate(cs):
            for comp in range(3):
                if axes[c][comp]:
                    S[n_][comp][k] = S[n_][comp].get(k, 0) + axes[c][comp] * w
    Zp = sum(c * tt ** e for e, c in Z.items())
    return [tuple(sp.factor(sp.cancel(sum(c * tt ** e for e, c in S[n_][comp].items()) / Zp)) for comp in range(3)) for n_ in range(len(sites))]
line = [(-1, 0, 0), (0, 0, 0), (1, 0, 0)]
fl = fields_t(line, 3, 1, 2)
line_formula = (tt - 1) * (3 * tt ** 2 + 27 * tt + 40) / (3 * tt ** 3 + 50 * tt ** 2 + 179 * tt + 200)
good = sp.simplify(fl[2][0] + line_formula) == 0 and sp.simplify(fl[0][0] - line_formula) == 0 and fl[1] == (0, 0, 0)
good &= fl[2][0].subs(tt, 2) == sp.Rational(-53, 391)
plaq = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)]
fp = fields_t(plaq, 3, 1, 2)
centre = (sp.Rational(1, 2), sp.Rational(1, 2), 0)
for s_, f in zip(plaq, fp):
    inward = [c - x for c, x in zip(centre, s_)]
    good &= all(sp.simplify(f[i] * inward[j] - f[j] * inward[i]) == 0 for i in range(3) for j in range(3))   # parallel to the inward direction
    good &= sp.simplify(f[0] / inward[0]).subs(tt, 2) > 0 and all(sp.simplify(c.subs(tt, 1)) == 0 for c in f)
g23 = [(x, y, 0) for x in range(3) for y in range(2)]
f23 = fields_t(g23, 3, 1, 2)
good &= all(all(sp.simplify(c.subs(tt, 1)) == 0 for c in f) for f in f23)
good &= f23[2][0] == 0 and sp.simplify(f23[0][0].subs(tt, 2)) > 0 and sp.simplify(f23[4][0].subs(tt, 2)) < 0
ok("D.b", good, "with (p, q, r) = (3, 1, 2) and the product rule, exact as functions of t: on the line of 3 the ends carry "
   "-+(t - 1)(3t^2 + 27t + 40)/(3t^3 + 50t^2 + 179t + 200) along the line (-53/391 at t = 2, block 41's refuter's value), pointing "
   "at the middle record; on the plaquette every corner points at the centre; on the 2x3 window every record leans towards the "
   "window's middle; every field vanishes exactly at t = 1 (block 41's isotropic rule)")

# ------------------------------------------------------------------ D.c: a hedgehog coupling in an ordered medium (exact lattice kernel)
L = 4; Nn = L ** 3
sites = list(itertools.product(range(L), repeat=3)); idx = {s_: i for i, s_ in enumerate(sites)}
def mat_add(A, B, f=1):
    return [[a + f * b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]
lap = [[Fr(0)] * Nn for _ in range(Nn)]                                                               # -Delta
Dm = []                                                                                                # backward differences
for c in range(3):
    D = [[Fr(0)] * Nn for _ in range(Nn)]
    for s_ in sites:
        t_ = list(s_); t_[c] = (t_[c] - 1) % L
        D[idx[s_]][idx[s_]] += 1; D[idx[s_]][idx[tuple(t_)]] -= 1
    Dm.append(D)
for s_ in sites:
    i = idx[s_]; lap[i][i] += 6
    for c in range(3):
        for dd in (1, -1):
            t_ = list(s_); t_[c] = (t_[c] + dd) % L
            lap[i][idx[tuple(t_)]] -= 1
def inverse(A):
    n = len(A); M_ = [row[:] + [Fr(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M_[r][c] != 0); M_[c], M_[p] = M_[p], M_[c]
        pv = M_[c][c]; M_[c] = [x / pv for x in M_[c]]
        for r in range(n):
            if r != c and M_[r][c] != 0:
                f = M_[r][c]; M_[r] = [x - f * y for x, y in zip(M_[r], M_[c])]
    return [row[n:] for row in M_]
P0 = [[Fr(1, Nn)] * Nn for _ in range(Nn)]
G = mat_add(inverse(mat_add(lap, P0)), P0, -1)                                                         # zero-mean Green function
def matmul(A, B):
    Bt = list(zip(*B))
    return [[sum(a * b for a, b in zip(ra, cb)) for cb in Bt] for ra in A]
def transpose(A):
    return [list(r) for r in zip(*A)]
Kxy = mat_add(matmul(matmul(Dm[0], G), transpose(Dm[0])), matmul(matmul(Dm[1], G), transpose(Dm[1])))   # sum_c D_c G D_c^T over c = x, y
LapzG = [[Fr(0)] * Nn for _ in range(Nn)]
for s_ in sites:
    for s2 in sites:
        up = idx[((s2[0]), s2[1], (s2[2] + 1) % L)]; dn = idx[(s2[0], s2[1], (s2[2] - 1) % L)]
        LapzG[idx[s_]][idx[s2]] = G[idx[s_]][up] + G[idx[s_]][dn] - 2 * G[idx[s_]][idx[s2]]
good = all(Kxy[i][j] == (Fr(int(i == j)) - Fr(1, Nn)) + LapzG[i][j] for i in range(Nn) for j in range(Nn))
o = idx[(0, 0, 0)]; vz = LapzG[o][idx[(0, 0, 2)]]; vx = LapzG[o][idx[(2, 0, 0)]]
good &= vz != vx
ok("D.c", good, "for an ordered medium (contents near +z) a hedgehog rule couples a record linearly to the in-plane divergence of the "
   "tilt, -lambda n (div_perp pi); minimising (K/2) sum |grad pi|^2 against it gives the pair kernel -(lambda^2/K) sum_{c=x,y} "
   "D_c G D_c^T, and on the 4^3 torus exactly sum_{c=x,y} D_c G D_c^T = delta - 1/N + Lap_z G: two records interact only through "
   "Lap_z G, which differs along the axis and across it, and a three-component (isotropic) divergence leaves only delta - 1/N")
# floating: the far form on a large torus
Lb = 32; k = 2 * np.pi * np.arange(Lb) / Lb
KX, KY, KZ = np.meshgrid(k, k, k, indexing="ij")
E = 2 * (3 - np.cos(KX) - np.cos(KY) - np.cos(KZ)); E[0, 0, 0] = np.inf
Vk = -2 * (1 - np.cos(KZ)) / E                                                                          # Lap_z G in Fourier
Vr = np.real(np.fft.ifftn(Vk))
rows = []
for r_ in (4, 6, 8):
    along = Vr[0, 0, r_]; across = Vr[r_, 0, 0]
    rows.append(f"r = {r_}: along {along * 4 * math.pi * r_ ** 3:+.2f}, across {across * 4 * math.pi * r_ ** 3:+.2f}")
print("note (floating) Lap_z G(r) x 4 pi r^3 on a 32^3 torus (continuum 3cos^2(theta) - 1 = +2 along, -1 across): " + "; ".join(rows))

# ------------------------------------------------------------------ D.d: absence factors (block 01's reading (ii)) on lumps
def lump_field(recs, aa, bb, cc, p, q, r):
    rset = set(recs); idx_ = {s_: i for i, s_ in enumerate(recs)}
    bonds = [(i, idx_[tuple(x + e for x, e in zip(s_, d))]) for i, s_ in enumerate(recs) for d in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
             if tuple(x + e for x, e in zip(s_, d)) in rset]
    phi = lambda s_, d: aa if dot(s_, d) == 1 else (bb if dot(s_, d) == 0 else cc)
    site_f = []
    for s_ in recs:
        empt = [d for d in axes if tuple(x + e for x, e in zip(s_, d)) not in rset]
        site_f.append([math.prod(phi(axes[c], d) for d in empt) for c in range(6)])
    W = [[p if axes[i] == axes[j] else (q if axes[i] == neg(axes[j]) else r) for j in range(6)] for i in range(6)]
    comp_of = [(c // 2, 1 if c % 2 == 0 else -1) for c in range(6)]           # each content has one nonzero component
    Z = 0; S = [[0, 0, 0] for _ in recs]
    for cs in itertools.product(range(6), repeat=len(recs)):
        w = 1
        for n_, c in enumerate(cs):
            w *= site_f[n_][c]
        for (i, j) in bonds:
            w *= W[cs[i]][cs[j]]
        Z += w
        for n_, c in enumerate(cs):
            k_, sg_ = comp_of[c]
            S[n_][k_] += sg_ * w
    return [tuple(Fr(x, Z) for x in s_) for s_ in S]
good = lump_field([(0, 0, 0)], 3, 2, 1, 3, 1, 2)[0] == (0, 0, 0)                                      # an isolated record: no preference
res = {}
for aa, cc in ((3, 1), (1, 3)):
    fd = lump_field([(0, 0, 0), (1, 0, 0)], aa, 2, cc, 3, 1, 2)
    fq = lump_field([(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)], aa, 2, cc, 3, 1, 2)
    fc = lump_field([(x, y, z) for x in range(2) for y in range(2) for z in range(2)], aa, 2, cc, 3, 1, 2)
    res[(aa, cc)] = (fd, fq, fc)
    sgn = 1 if aa > cc else -1
    good &= sgn * fd[1][0] > 0 and fd[1][1] == 0 and fd[1][2] == 0                                   # the outer end leans out (a > c)
    good &= all(sgn * v[0] * (2 * s_[0] - 1) > 0 and sgn * v[1] * (2 * s_[1] - 1) > 0 and v[2] == 0
                for s_, v in zip([(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)], fq))
    corners = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
    good &= all(v[0] == v[1] * (2 * s_[0] - 1) * (2 * s_[1] - 1) and v[1] == v[2] * (2 * s_[1] - 1) * (2 * s_[2] - 1)
                and sgn * v[0] * (2 * s_[0] - 1) > 0 for s_, v in zip(corners, fc))                  # along the outward body diagonal
cube_out = res[(3, 1)][2][7][0]
ok("D.d", good, "with absence factors phi(s, d) = (a, b, c) for s.d = 1, 0, -1 towards an empty neighbour and (p, q, r) = (3, 1, 2): an "
   "isolated record has no preference (each content meets a, c and b^4 once); a dimer's ends, a plaquette's corners and the corners "
   "of a 2x2x2 lump lean outward when a > c and inward when a < c, the cube's corners exactly along the body diagonals "
   f"({cube_out} per component at (a, b, c) = (3, 2, 1)): a closed lump carries a hedgehog of content with zero vector sum")
print(f"runtime {time.time() - T0:.0f} s")

if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS)); sys.exit(1)
print("SUMMARY: PARTIAL direction-dependent rules give contents a hedgehog around records and lumps but no universal 1/r pull: 12 "
      "covariant pair values, exact content fields as functions of t, and in an ordered medium a pair interaction through Lap_z G "
      "only, whose far form (3cos^2(theta) - 1)/r^3 averages to zero")
print("HIT: covariant pair weights on the six-axis menu have 12 free values (orbits of (a, b, d) fixed by a.b, a.d, b.d and the "
      "handedness (a x b).d), 9 once symmetric; the product rule h(a.d)h(-b.d)omega(a.b), h(1) = t, is symmetric and achiral, and on "
      "the line of 3 the ends' contents lean at the middle by (t - 1)(3t^2 + 27t + 40)/(3t^3 + 50t^2 + 179t + 200) (53/391 at t = 2).")
print("HIT: in an ordered medium a hedgehog rule couples occupancy linearly to the in-plane divergence of the tilt, and the pair "
      "kernel is exactly -(lambda^2/K)(delta - 1/N + Lap_z G): far away -(lambda^2/K)(3cos^2(theta) - 1)/(4 pi r^3), attractive along "
      "the order and repulsive across it with zero angular mean, and only a contact term if the tilt has three components: direction-"
      "dependent rules give no universal 1/r attraction.")
