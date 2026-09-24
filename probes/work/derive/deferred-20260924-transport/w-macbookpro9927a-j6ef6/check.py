#!/usr/bin/env python3
"""deferred-20260924-transport, first pass a1 (worker w-macbookpro9927a-j6ef6, claude-opus-5-5).

PR8558's deferred collision sentence ("collisions restore a first-harmonic wind and with it one coefficient in every
direction"), under the landed streaming law of block 44's sphere menu (axis hops at rates |s_k|/sqrt3) and its bond
re-draw (a pair re-draws on its momentum class: P/2 +- r w, w uniform on the unit circle orthogonal to P).  At leading
order in the density (product closure) and first order about local equilibrium: every harmonic l >= 2 relaxes (the first
half holds), but the collisional viscosity is isotropic, nu_coll = 1/(45 gamma rho), so block 51's cubic part survives
with eta = nu_lat/(nu_lat + nu_coll) = 45 sqrt3 gamma rho/(45 sqrt3 gamma rho + 16) in (0, 1).  Exact families use
fractions and sympy; one labelled float family samples the actual re-draw rule.
"""
import itertools
import os
import sys
import time
from fractions import Fraction as Fr

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np  # noqa: E402
import sympy as sp  # noqa: E402

T0 = time.time()
FAILS = []


def check(tag, ok, msg=""):
    print(("PASS " if ok else "FAIL ") + tag + (": " + msg if msg else ""))
    if not ok:
        FAILS.append(tag)


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


# ---------------------------------------------------------------- E1: the re-draw rule and its second-moment average
units = set()
for p in range(-4, 5):
    for q in range(-4, 5):
        for den in (1, 2, 3):
            u, v = Fr(p, den), Fr(q, den)
            nn = 1 + u * u + v * v
            units.add((2 * u / nn, 2 * v / nn, (1 - u * u - v * v) / nn))
units = sorted(units)
ok, cnt = True, 0
for s1, s2 in itertools.product(units[:14], units[14:28]):
    c = sum(x * y for x, y in zip(s1, s2))
    if c == -1:
        continue
    P = [x + y for x, y in zip(s1, s2)]
    D = [x - y for x, y in zip(s1, s2)]
    X = cross(s1, s2)
    P2 = sum(x * x for x in P)
    for i in range(3):
        for j in range(3):   # theta-average of s s^T, s = P/2 + cos(th) D/2 - sin(th) (s1 x s2)/|P|
            ok &= (P[i] * P[j] / 4 + D[i] * D[j] / 8 + X[i] * X[j] / (2 * P2)) == \
                  (Fr(1 - c, 4) * (i == j) + (1 + 3 * c) / (8 * (1 + c)) * P[i] * P[j])
    cnt += 1
th = sp.symbols("theta", real=True)
for i1, i2 in ((3, 20), (5, 17), (9, 26)):
    s1, s2 = [sp.Rational(x) for x in units[i1]], [sp.Rational(x) for x in units[i2]]
    P = [a + b for a, b in zip(s1, s2)]
    D = [a - b for a, b in zip(s1, s2)]
    X = cross(s1, s2)
    nP = sp.sqrt(sum(x * x for x in P))
    s = [P[i] / 2 + sp.cos(th) * D[i] / 2 - sp.sin(th) * X[i] / nP for i in range(3)]
    ok &= sp.simplify(sum(x * x for x in s) - 1) == 0 and sp.simplify(sum(x * y for x, y in zip(s, P)) - nP ** 2 / 2) == 0
check("E1 re-draw", ok, "the re-drawn content P/2 + r w is a unit vector on the momentum class; averaged over the circle, "
      "E[s s^T] = (1-c)/4 I + (1+3c)/(8(1+c)) P P^T exactly at %d rational pairs (c = s1.s2): it sees only P and c, "
      "no lattice axis" % cnt)

# ---------------------------------------------------------------- E2: the relaxation eigenvalues of the linearized re-draw
cc, uu = sp.symbols("c u", real=True)
xx = (1 + cc) / 2 + (1 - cc) / 2 * sp.cos(th)
a1, a2 = [], []
for l in range(0, 9):
    Pl = sp.legendre(l, xx)
    a1.append(sp.nsimplify(2 * sp.integrate(sp.integrate(sp.expand(Pl), (th, 0, 2 * sp.pi)) / (2 * sp.pi), (cc, -1, 1)) / 2))
    a2.append(sp.nsimplify(4 * sp.integrate(uu * sp.legendre(l, uu) ** 2, (uu, 0, 1))))
ok = a1 == a2 and a1[:3] == [2, 1, sp.Rational(1, 2)]
ok &= all(4 * sp.integrate(uu * sp.legendre(l, uu) ** 2, (uu, 0, 1)) < sp.Rational(4, 2 * l + 1) for l in range(2, 21))
check("E2 relaxation", ok, "per collision the linearized re-draw multiplies a degree-l harmonic by a_l = 2E[P_l(s.s1)] = "
      "4 int_0^1 u P_l(u)^2 du (Legendre addition theorem on the circle; both routes agree for l <= 8): a = %s; a_0 = 2 and "
      "a_1 = 1 (number, momentum), and a_l < 4/(2l+1) <= 4/5 for l >= 2 (checked to l = 20), so every l >= 2 relaxes at "
      "6 gamma rho (1 - a_l) > 0: collisions DO restore a first-harmonic local law" % [str(v) for v in a1[:6]])

# ---------------------------------------------------------------- E3: the second harmonics relax at one rate (no cubic part)
al, be, ps = sp.symbols("alpha beta psi", real=True)
b11, b22, b12, b13, b23 = sp.symbols("b11 b22 b12 b13 b23", real=True)
B = sp.Matrix([[b11, b12, b13], [b12, b22, b23], [b13, b23, -b11 - b22]])
S1 = sp.Matrix([sp.sin(al) * sp.cos(be), sp.sin(al) * sp.sin(be), sp.cos(al)])
e1 = sp.Matrix([sp.cos(al) * sp.cos(be), sp.cos(al) * sp.sin(be), -sp.sin(al)])
f1 = sp.Matrix([-sp.sin(be), sp.cos(be), 0])
S2 = cc * S1 + sp.sqrt(1 - cc ** 2) * (sp.cos(ps) * e1 + sp.sin(ps) * f1)
Pv = S1 + S2
avg = sp.integrate(sp.expand((Pv.T * B * Pv)[0, 0]), (ps, 0, 2 * sp.pi)) / (2 * sp.pi)
ok = sp.simplify(sp.expand(sp.expand_trig(avg - (S1.T * B * S1)[0, 0] * (1 + cc) * (1 + 3 * cc) / 2))) == 0
quot = sp.integrate((1 + 3 * cc) / (8 * (1 + cc)) * (1 + cc) * (1 + 3 * cc) / 2, (cc, -1, 1)) / 2
ok &= quot == sp.Rational(1, 4)
check("E3 isotropic stress relaxation", ok, "for EVERY traceless symmetric B (both cubic irreps, x^2-y^2 and xy types) "
      "E[phi_B(s) phi_B(s1)] = (1/4) E[phi_B(s1)^2]: with E1, E_psi[P^T B P] = s1^T B s1 (1+c)(1+3c)/2 and "
      "E_c[(1+3c)^2/16] = 1/4, so a_2 = 1/2 on all five second harmonics and the stress relaxes at 3 gamma rho in every "
      "direction")

# ---------------------------------------------------------------- E4: Chapman-Enskog: the collisional viscosity
sx, sy, sz = sp.symbols("sx sy sz", real=True)
S = [sx, sy, sz]
TH, PH = sp.symbols("TH PH", real=True)
sph = {sx: sp.sin(TH) * sp.cos(PH), sy: sp.sin(TH) * sp.sin(PH), sz: sp.cos(TH)}


def sphere_int(expr):
    e = sp.expand(expr).subs(sph)
    return sp.simplify(sp.integrate(sp.integrate(e * sp.sin(TH), (PH, 0, 2 * sp.pi)), (TH, 0, sp.pi)))


gam, rho = sp.symbols("gamma rho", positive=True)
Gm = sp.Matrix(3, 3, lambda i, j: sp.Symbol("G%d%d" % (i, j)))     # G_ij = d_i g_j
Ssym = (Gm + Gm.T) / 2 - sp.eye(3) * Gm.trace() / 3
src = sp.sqrt(3) / (4 * sp.pi) * sum((S[i] * S[j] - (sp.Rational(1, 3) if i == j else 0)) * Ssym[i, j] for i in range(3) for j in range(3))
f1 = -src / (3 * gam * rho)                                          # C = -3 gamma rho on second harmonics
ok = True
for (i, j) in ((0, 0), (0, 1), (1, 2), (2, 2)):
    Pi = sphere_int(S[i] * S[j] * f1) / sp.sqrt(3)
    ok &= sp.simplify(Pi + 2 * Ssym[i, j] / (45 * gam * rho)) == 0
kx, ky, kz = sp.symbols("kx ky kz", real=True)
gx, gy, gz = sp.symbols("gx gy gz", real=True)
kv, gv = sp.Matrix([kx, ky, kz]), sp.Matrix([gx, gy, gz])
Gw = sp.I * kv * gv.T                                                # plane wave: d_i g_j -> i k_i g_j
Sw = (Gw + Gw.T) / 2 - sp.eye(3) * Gw.trace() / 3
force = sp.Matrix([sum(sp.I * kv[j] * 2 * Sw[i, j] / (45 * gam * rho) for j in range(3)) for i in range(3)])
want = (-(kv.dot(kv)) * gv - kv * kv.dot(gv) / 3) / (45 * gam * rho)
ok &= sp.simplify(force - want) == sp.zeros(3, 1)
check("E4 collisional viscosity", ok, "the l=2 source of (1/sqrt3) s.grad f_le is (sqrt3/4pi)(s_i s_j - d_ij/3) S_ij[g]; with "
      "the rate 3 gamma rho, f1 = -source/(3 gamma rho) and Pi_ij = (1/sqrt3) int s_i s_j f1 = -(2/(45 gamma rho)) S_ij[g] "
      "(sphere integrals, symbolic): the viscous force is (1/(45 gamma rho))(Lap g_i + (1/3) d_i div g), isotropic, with no "
      "d_i^2 g_i term")

# ---------------------------------------------------------------- E5: block 51's lattice term, recomputed; E6: eta
t3 = sp.integrate(sp.cos(TH) ** 3 * sp.sin(TH), (TH, 0, sp.pi / 2)) * 2 * 2 * sp.pi / (4 * sp.pi)        # <|s_z|^3>
t21 = sp.integrate(sp.integrate(sp.sin(TH) ** 3 * sp.cos(TH) * sp.cos(PH) ** 2, (TH, 0, sp.pi / 2)) * 2, (PH, 0, 2 * sp.pi)) / (4 * sp.pi)
nu_lat = sp.nsimplify(3 / (2 * sp.sqrt(3)) * t21)                     # (3/2) d_k d_l T_ijkl g_j, speed 1/sqrt3
ok = t3 == sp.Rational(1, 4) and t21 == sp.Rational(1, 8) and sp.simplify(nu_lat - sp.sqrt(3) / 16) == 0
ok &= sp.simplify(3 / (2 * sp.sqrt(3)) * (t3 - t21) - nu_lat) == 0    # the d_i^2 g_i coefficient equals the Laplacian one
check("E5 lattice term", ok, "<|s_z|^3> = 1/4, <s_x^2|s_z|> = 1/8, so the second-order axis streaming gives nu_lat (Lap g_i + "
      "d_i^2 g_i) with nu_lat = sqrt3/16 (block 51, recomputed in the same momentum equation)")
xg = sp.symbols("x", positive=True)                                   # x = gamma rho
nu_coll = 1 / (45 * xg)
eta = sp.simplify(nu_lat / (nu_lat + nu_coll))
ok = sp.simplify(eta - 45 * sp.sqrt(3) * xg / (45 * sp.sqrt(3) * xg + 16)) == 0
ok &= sp.simplify(sp.diff(eta, xg) - 720 * sp.sqrt(3) / (45 * sp.sqrt(3) * xg + 16) ** 2) == 0
ok &= sp.limit(eta, xg, sp.oo) == 1 and sp.limit(eta, xg, 0) == 0 and sp.limit(eta / xg, xg, 0) == 45 * sp.sqrt(3) / 16
e1v, e2v = eta.subs(xg, sp.Rational(1, 5)), eta.subs(xg, sp.Rational(3, 10))
kk = sp.symbols("k", positive=True)                                   # transverse waves: axis vs face diagonal
nu_c = nu_lat + nu_coll


def damping(kvec, gvec):
    op = nu_c * kk ** 2 * gvec + nu_lat * sp.Matrix([kvec[i] ** 2 * gvec[i] for i in range(3)]) + nu_coll / 3 * kvec * kvec.dot(gvec)
    return sp.simplify(gvec.dot(op) / gvec.dot(gvec))


d_axis = damping(sp.Matrix([kk, 0, 0]), sp.Matrix([0, 1, 0]))
d_diag = damping(sp.Matrix([kk, kk, 0]) / sp.sqrt(2), sp.Matrix([1, -1, 0]) / sp.sqrt(2))
ok &= sp.simplify(d_axis - nu_c * kk ** 2) == 0 and sp.simplify(d_diag - d_axis - nu_lat * kk ** 2 / 2) == 0
ok &= 0 < e1v < 1 and 0 < e2v < 1
check("E6 eta", ok, "eta = nu_lat/(nu_lat + nu_coll) = 45 sqrt3 gamma rho/(45 sqrt3 gamma rho + 16): 0 < eta < 1 for every "
      "gamma rho > 0, strictly increasing (derivative 720 sqrt3/(45 sqrt3 gamma rho + 16)^2), -> 1 as gamma rho -> oo, "
      "~ (45 sqrt3/16) gamma rho as gamma rho -> 0; at (rho, gamma) = (0.1, 2) and (0.3, 1): %.4f and %.4f.  The in-plane "
      "transverse wave along a face diagonal decays faster than along an axis by nu_lat k^2/2 at every gamma"
      % (float(e1v), float(e2v)))

# ---------------------------------------------------------------- N1 (float): the actual re-draw rule, sampled
rng = np.random.default_rng(20260924)
Nn = 200000
s1 = rng.normal(size=(Nn, 3))
s1 /= np.linalg.norm(s1, axis=1)[:, None]
s2 = rng.normal(size=(Nn, 3))
s2 /= np.linalg.norm(s2, axis=1)[:, None]
Pn = s1 + s2
Ph = Pn / np.linalg.norm(Pn, axis=1)[:, None]
w = rng.normal(size=(Nn, 3))
w -= (w * Ph).sum(1)[:, None] * Ph
w /= np.linalg.norm(w, axis=1)[:, None]
rr = np.sqrt(np.clip(1 - (Pn * Pn).sum(1) / 4, 0, None))
sn = Pn / 2 + rr[:, None] * w
p2 = (1.5 * (sn * s1).sum(1) ** 2 - 0.5).mean()
qE = ((sn[:, 0] ** 2 - sn[:, 1] ** 2) * (s1[:, 0] ** 2 - s1[:, 1] ** 2)).mean() / ((s1[:, 0] ** 2 - s1[:, 1] ** 2) ** 2).mean()
qT = ((sn[:, 0] * sn[:, 1]) * (s1[:, 0] * s1[:, 1])).mean() / ((s1[:, 0] * s1[:, 1]) ** 2).mean()
print("N1 (float, 200000 sampled re-draws of the rule as written): <P2(s.s1)> = %.4f, E_g quotient %.4f, T_2g quotient %.4f "
      "(exact 1/4); |s| - 1 max %.1e, momentum error max %.1e" % (p2, qE, qT, np.abs(np.linalg.norm(sn, axis=1) - 1).max(),
                                                                  np.abs(sn + (Pn - sn) - Pn).max()))
onclass = np.abs(np.linalg.norm(sn, axis=1) - 1).max() < 1e-9 and np.abs((sn * Pn).sum(1) - (Pn * Pn).sum(1) / 2).max() < 1e-9
check("N1 sampled re-draw", onclass and abs(p2 - 0.25) < 0.01 and abs(qE - 0.25) < 0.01 and abs(qT - 0.25) < 0.01,
      "every sampled content is a unit vector on its momentum class, and an independent code path agrees with E2-E3")

print("time %.0f s" % (time.time() - T0))
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS))
    sys.exit(1)
print("SUMMARY: PARTIAL (first pass on batch 6; PR8558's deferred collision sentence). At leading order in density and "
      "first order about local equilibrium, block 44's sphere-menu re-draw multiplies a degree-l harmonic by "
      "a_l = 4 int_0^1 u P_l(u)^2 du per collision (2, 1, 1/2, 3/8, ...): every l >= 2 relaxes, so collisions do restore a "
      "first-harmonic local law; but the re-draw sees only P and s1.s2, the second harmonics relax at the single rate "
      "3 gamma rho, and the collisional viscosity is isotropic, nu_coll = 1/(45 gamma rho). Block 51's cubic lattice term "
      "survives with eta = 45 sqrt3 gamma rho/(45 sqrt3 gamma rho + 16) in (0,1), increasing with gamma rho: no collision "
      "rate gives one coefficient in every direction.")
print("HIT: in block 44's inertial gas (sphere menu, axis streaming, bond re-draw) at small density the collisional "
      "viscosity is exactly isotropic, nu_coll = 1/(45 gamma rho) (second-harmonic relaxation 3 gamma rho; per-collision "
      "multipliers 4 int_0^1 u P_l(u)^2 du), so eta = 45 sqrt3 gamma rho/(45 sqrt3 gamma rho + 16) lies in (0,1) for every "
      "collision rate and grows with it: collisions dilute but never cancel the lattice's cubic viscosity")
