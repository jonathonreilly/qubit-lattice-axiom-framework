#!/usr/bin/env python3
"""J:derive:odds-field-second-order-mass-channel:a4 - checks for ATTEMPT.md (same directory).

Blocks 41-42 (supplied reading, not adopted): six-axis rule, omega = p, q, r for equal, opposite, orthogonal contents,
T = p+q+4r, K1 = omega/T, l1 = (p-q)/T (vector channel), l2 = (p+q-2r)/T (quadrupole channel); self-consistent odds
pi_x(s) ~ prod_{y~x} sum_b omega(s,b) pi_y(b); a record is the point mass at its content. A departure delta_y (zero sum)
has lean m_y = sum_s delta_y(s) e(s) and axis weights w_y,i = delta_y(+e_i) + delta_y(-e_i) (sum 0);
delta(s) = (1/2) m.e(s) + (1/2) w_axis(s). Exact (Fractions / sympy) unless labelled.
"""
import itertools
import math
import random
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg, flush=True)
    if not good:
        FAILS.append(tag)


E6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def omega(p, q, r):
    return [[p if s == b else (q if s == b ^ 1 else r) for b in range(6)] for s in range(6)]


def polymul(a, b, n):
    out = [Fr(0)] * n
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if i + j < n:
                    out[i + j] += x * y
    return out


def factor_poly(W, T, dep, s, n):
    """(6/T) sum_b omega(s,b) (1/6 + eps dep(b)) as a polynomial in eps"""
    return [Fr(6, 1) / T * sum(W[s][b] * Fr(1, 6) for b in range(6)), Fr(6, 1) / T * sum(W[s][b] * dep[b] for b in range(6))]


def lean(d):
    return [sum(d[s] * E6[s][i] for s in range(6)) for i in range(3)]


def axw(d):
    return [d[2 * i] + d[2 * i + 1] for i in range(3)]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


# ------------------------------------------------------------------ A1: the normalizer to third order, both channels
random.seed(8)
a1_ok, a1_vec_ok, third_nonzero = True, True, False
for (p, q, r) in ((Fr(5), Fr(2), Fr(4)), (Fr(3), Fr(1), Fr(2)), (Fr(7), Fr(1), Fr(1)), (Fr(2), Fr(1), Fr(3))):
    W = omega(p, q, r)
    T = p + q + 4 * r
    l1, l2 = (p - q) / T, (p + q - 2 * r) / T
    for trial in range(3):
        deps = []
        for _ in range(6):
            v = [Fr(random.randint(-9, 9), 7) for _ in range(6)]
            m = sum(v) / 6
            deps.append([x - m for x in v])
        Z = [Fr(0)] * 4
        for s in range(6):
            f = [Fr(1)]
            for y in range(6):
                f = polymul(f, factor_poly(W, T, deps[y], s, 4), 4)
            Z = [z + fi / 6 for z, fi in zip(Z, f)]
        pred2 = 3 * sum(l1 ** 2 * dot(lean(deps[y]), lean(deps[yy])) + l2 ** 2 * dot(axw(deps[y]), axw(deps[yy]))
                        for y in range(6) for yy in range(y + 1, 6))
        a1_ok &= Z[0] == 1 and Z[1] == 0 and Z[2] == pred2
        third_nonzero |= Z[3] != 0
        vdeps = [[Fr(1, 2) * dot(lean(d), E6[s]) for s in range(6)] for d in deps]     # purely vector parts
        Zv = [Fr(0)] * 4
        for s in range(6):
            f = [Fr(1)]
            for y in range(6):
                f = polymul(f, factor_poly(W, T, vdeps[y], s, 4), 4)
            Zv = [z + fi / 6 for z, fi in zip(Zv, f)]
        a1_vec_ok &= Zv[1] == 0 and Zv[3] == 0
ok("A1", a1_ok and a1_vec_ok and third_nonzero,
   "exact, four triples x three random departures of the six neighbours: the normalizer against the void is "
   "Z = 1 + 0 eps + 3 sum_{y<y'} (l1^2 m_y.m_y' + l2^2 w_y.w_y') eps^2 + O(eps^3); the quadrupole channel enters with "
   "the same 3; for purely vector departures the eps and eps^3 terms vanish, with quadrupole parts eps^3 is nonzero")

# ------------------------------------------------------------------ A2: the first-order factor of a content, and its average
a2_ok = True
for (p, q, r) in ((Fr(5), Fr(2), Fr(4)), (Fr(2), Fr(1), Fr(3))):
    W = omega(p, q, r)
    T = p + q + 4 * r
    l1, l2 = (p - q) / T, (p + q - 2 * r) / T
    deps = []
    for _ in range(6):
        v = [Fr(random.randint(-9, 9), 5) for _ in range(6)]
        m = sum(v) / 6
        deps.append([x - m for x in v])
    avg = [Fr(0)] * 3
    for b in range(6):
        f = [Fr(1)]
        for y in range(6):
            f = polymul(f, factor_poly(W, T, deps[y], b, 3), 3)
        pred1 = 3 * l1 * sum(dot(lean(d), E6[b]) for d in deps) + 3 * l2 * sum(axw(d)[b // 2] for d in deps)
        a2_ok &= f[0] == 1 and f[1] == pred1
        avg = [a + x / 6 for a, x in zip(avg, f)]
    Z = [Fr(0)] * 3
    for s in range(6):
        f = [Fr(1)]
        for y in range(6):
            f = polymul(f, factor_poly(W, T, deps[y], s, 3), 3)
        Z = [z + x / 6 for z, x in zip(Z, f)]
    a2_ok &= avg == Z and avg[1] == 0
ok("A2", a2_ok, "exact: a record of content b at x carries the factor 1 + eps (3 l1 b.sum_y m_y + 3 l2 sum_y w_y,axis(b)) "
   "+ O(eps^2); its average over the six contents is Z itself, so the first-order term averages to zero exactly")

# ------------------------------------------------------------------ A3: one record on the 5^3 torus, exact fields
L = 5
p, q, r = 5, 2, 4
T = p + q + 4 * r
l1, l2 = sp.Rational(p - q, T), sp.Rational(p + q - 2 * r, T)
sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
free = [s for s in sites if s != (0, 0, 0)]
pos = {s: i for i, s in enumerate(free)}


def nbrs(s):
    return [tuple((s[i] + e[i]) % L for i in range(3)) for e in E6]


def field(lam):
    Mx = sp.zeros(len(free), len(free))
    rhs = sp.zeros(len(free), 1)
    for s in free:
        i = pos[s]
        Mx[i, i] += 1
        for t in nbrs(s):
            if t == (0, 0, 0):
                rhs[i] += lam
            else:
                Mx[i, pos[t]] -= lam
    from sympy.polys.matrices import DomainMatrix
    sol = DomainMatrix.from_Matrix(Mx).to_field().lu_solve(DomainMatrix.from_Matrix(rhs).to_field()).to_Matrix()
    out = {(0, 0, 0): sp.Integer(1)}
    for s in free:
        out[s] = sol[pos[s]]
    return out


u = field(l1)
psi = field(l2)
ident = all(sum(u[t] for t in nbrs(s)) == u[s] / l1 and sum(psi[t] for t in nbrs(s)) == psi[s] / l2 for s in free)
Wf = omega(Fr(p), Fr(q), Fr(r))
wa = [Fr(2, 3), Fr(-1, 3), Fr(-1, 3)]                      # axis weights of the record's departure, content a = +x
checks = 0
a3_ok = ident
for x in [(1, 0, 0), (2, 0, 0), (1, 1, 0), (2, 1, 1), (2, 2, 2)]:
    deps = []
    for t in nbrs(x):
        ut, pt = Fr(str(u[t])), Fr(str(psi[t]))
        deps.append([Fr(1, 2) * ut * E6[s][0] + Fr(1, 2) * wa[s // 2] * pt for s in range(6)])
    Z = [Fr(0)] * 3
    for s in range(6):
        f = [Fr(1)]
        for y in range(6):
            f = polymul(f, factor_poly(Wf, Fr(T), deps[y], s, 3), 3)
        Z = [z + c / 6 for z, c in zip(Z, f)]
    ux, px = Fr(str(u[x])), Fr(str(psi[x]))
    L1, L2 = Fr(p - q, T), Fr(p + q - 2 * r, T)
    V2 = -(Fr(3, 2) * (ux ** 2 - L1 ** 2 * sum(Fr(str(u[t])) ** 2 for t in nbrs(x)))
           + (px ** 2 - L2 ** 2 * sum(Fr(str(psi[t])) ** 2 for t in nbrs(x))))
    a3_ok &= Z[1] == 0 and -Z[2] == V2
    for b in range(6):
        f = [Fr(1)]
        for y in range(6):
            f = polymul(f, factor_poly(Wf, Fr(T), deps[y], b, 2), 2)
        a3_ok &= f[1] == 3 * E6[b][0] * ux + 3 * wa[b // 2] * px
        checks += 1
ok("A3", a3_ok, f"exact rational fields of one record (content +x) on the 5^3 torus at (5,2,4) (l1 = 3/23, l2 = -1/23): "
   "lean u = 1 at the record, u = l1 sum u off it; quadrupole psi likewise with l2; the identities sum_y u_y = u_x/l1 and "
   "sum_y psi_y = psi_x/l2 hold at all 124 sites; at five sites the second-order potential is exactly "
   "V = -(3/2)[u_x^2 - l1^2 sum_y u_y^2] - [psi_x^2 - l2^2 sum_y psi_y^2], and the first-order factor of content b is "
   f"exactly 1 + 3 (a.b) u_x + 3 (w_a)_axis(b) psi_x ({checks} content checks)")

# ------------------------------------------------------------------ A4: the far constants (floating point, Bessel integrals)
from scipy.integrate import quad
from scipy.special import ive


def Gk(x, lam):
    a = [abs(int(c)) for c in x]
    c = 1 - 6 * lam
    f = lambda t: math.exp(-c * t) * ive(a[0], 2 * lam * t) * ive(a[1], 2 * lam * t) * ive(a[2], 2 * lam * t)
    s, lo = 0.0, 0.0
    for hi in (10, 100, 1000, 10000, np.inf):
        s += quad(f, lo, hi, limit=500, epsabs=1e-16, epsrel=1e-13)[0]
        lo = hi
    return s


def V_ratio(x, lam):
    g0 = Gk((0, 0, 0), lam)
    ux = Gk(x, lam) / g0
    s2 = sum((Gk(tuple(x[i] + e[i] for i in range(3)), lam) / g0) ** 2 for e in E6)
    return ux, -1.5 * (ux * ux - lam * lam * s2) / (ux * ux)


lam0 = 1 / 6
u16, r16 = V_ratio((16, 0, 0), lam0)
u66, r66 = V_ratio((6, 6, 6), lam0)
g0w = Gk((0, 0, 0), lam0) / 6
cmass = 1.25 / (4 * math.pi * g0w) ** 2
lam5 = 3 / 23
ka = math.acosh((1 / lam5 - 4) / 2)
kd = math.acosh(1 / (6 * lam5))
pa, pd = 1.5 * (1 - 2 * lam5 ** 2 * (math.cosh(2 * ka) + 2)), 1.5 * (1 - 2 * lam5 ** 2 * 3 * math.cosh(2 * kd))
_, s16 = V_ratio((16, 0, 0), lam5)
_, s66 = V_ratio((6, 6, 6), lam5)
ok("A4", abs(r16 + 1.25) < 0.002 and abs(r66 + 1.25) < 0.002 and abs(s16 + pa) < 0.04 and abs(s66 + pd) < 0.02,
   f"floating point: on the massless surface (3,1,2) (l2 = 0) V/u^2 = {r16:.4f} at (16,0,0), {r66:.4f} at (6,6,6), -> "
   f"-(3/2)(1 - 6 l1^2) = -5/4, so V = -(5/4)/(4 pi G(0))^2 r^-2 = -{cmass:.5f} r^-2 (G(0) = {g0w:.10f}); screened "
   f"(5,2,4): V/u^2 = {s16:.4f} along the axis at 16, {s66:.4f} on the diagonal at (6,6,6), approaching the lattice "
   f"constants -(3/2)[1 - 2 l1^2 sum_j cosh 2k_j] = -{pa:.4f}, -{pd:.4f} (not -45 l1^2 = -{45 * lam5 ** 2:.4f})")

# ------------------------------------------------------------------ A5: two bodies (floating point): mutual capacitance
import scipy.sparse as sps
import scipy.sparse.linalg as spl

Lb = 32
lamb = 1.95 / 11.95                                           # (2.95, 1, 2): 6 l1 = 0.979, range 2.79
nb = Lb ** 3
idx = np.arange(nb).reshape(Lb, Lb, Lb)
rows, cols = [], []
for ax in range(3):
    for sh in (1, -1):
        rows.append(idx.ravel())
        cols.append(np.roll(idx, sh, axis=ax).ravel())
Adj = sps.csr_matrix((np.ones(6 * nb), (np.concatenate(rows), np.concatenate(cols))), shape=(nb, nb))
Mb = sps.identity(nb, format='csr') - lamb * Adj


def held_solve(held, vals):
    fr = np.ones(nb, bool)
    fr[held] = False
    sol = spl.cg(Mb[fr][:, fr], -(Mb[fr][:, held] @ vals), rtol=1e-12, maxiter=20000)[0]
    out = np.zeros(nb)
    out[held] = vals
    out[fr] = sol
    return out


def cube(c, k):
    return np.array([idx[(c[0] + i) % Lb, (c[1] + j) % Lb, (c[2] + l) % Lb] for i in range(k) for j in range(k) for l in range(k)])


cb = Lb // 2
caps = {}
for k in (1, 2):
    Bk = cube((cb, cb, cb), k)
    hk = held_solve(Bk, np.ones(len(Bk)))
    caps[k] = (hk - lamb * (Adj @ hk))[Bk].sum()
e0 = np.zeros(nb)
e0[idx[cb, cb, cb]] = 1.0
gk = spl.cg(Mb, e0, rtol=1e-12, maxiter=20000)[0]
ratios, Qs = {}, {}
for k in (1, 2):
    d = 10
    B1, B2 = cube((cb - 5, cb, cb), k), cube((cb + 5, cb, cb), k)
    h = held_solve(np.concatenate([B1, B2]), np.concatenate([np.ones(len(B1)), np.zeros(len(B2))]))
    Qs[k] = lamb * (Adj @ h)[B2].sum()
    ratios[k] = Qs[k] / (caps[k] ** 2 * gk[idx[cb + d, cb, cb]])
ok("A5", abs(ratios[1] - 1) < 1e-3 and abs(ratios[2] - 1) < 0.05,
   f"floating point, 32^3 torus at (2.95,1,2): with both bodies held (lean 1 on B1, 0 on B2) the charge induced on B2, "
   f"Q12 = l1 sum_(x in B2) sum_(y~x) h(y), is the mutual capacitance; at 10 steps it equals cap1 cap2 G(d) times "
   f"{ratios[1]:.4f} for single records and {ratios[2]:.4f} for 2x2x2 cubes (a Yukawa form factor of the cube); "
   f"cube/record strength ratio {Qs[2] / Qs[1]:.2f} against (cap_8/cap_1)^2 = {(caps[2] / caps[1]) ** 2:.2f} and N^2 = 64 "
   f"(capacities {caps[1]:.4f}, {caps[2]:.4f})")

# ------------------------------------------------------------------ A6: covariance - the only invariant direction is constant
G48 = []
for sig in itertools.permutations(range(3)):
    for fl in itertools.product((0, 1), repeat=3):
        G48.append([2 * sig[i // 2] + ((i % 2) ^ fl[i // 2]) for i in range(6)])
Pavg = sp.zeros(6, 6)
for g in G48:
    for i in range(6):
        Pavg[g[i], i] += sp.Rational(1, 48)
inv_rank = Pavg.rank()
Wsym = omega(sp.Symbol('p'), sp.Symbol('q'), sp.Symbol('r'))
omega_inv = all(Wsym[g[s]][g[b]] == Wsym[s][b] for g in G48 for s in range(6) for b in range(6))
ok("A6", inv_rank == 1 and Pavg * sp.ones(6, 1) == sp.ones(6, 1) and omega_inv and len({tuple(g) for g in G48}) == 48,
   "exact: omega is invariant under the 48 signed permutations acting on contents alone, so the odds map commutes with "
   "them at every site; the average of their permutation matrices has rank 1 (the constants): the only invariant "
   "direction in content space is the constant one, orthogonal to every departure")

label = "PARTIAL" if not FAILS else "PARTIAL (failed: " + ", ".join(FAILS) + ")"
print(f"SUMMARY: {label} (a)-(d) with the quadrupole channel: Z = 1 + 3 sum_(y<y') (l1^2 m.m' + l2^2 w.w') + O(3); the "
      "content-blind potential of one record is exactly -(3/2)[u^2 - l1^2 sum u_y^2] - [psi^2 - l2^2 sum psi_y^2] at "
      "second order, far constant -(3/2)(1 - 6 l1^2) near the massless surface (-5/4; -0.1239/r^2 on it) and "
      "direction-dependent when screened; the first-order term of content b is -3 (a.b) u - 3 (w_a)_axis(b) psi; "
      "two bodies couple through their mutual capacitance -> cap1 cap2 G(d); no content-blind clause is first order "
      "(only a seventh outcome, zero at the neutral scale)")
if not FAILS:
    print("HIT: for the self-consistent odds of the six-axis rule, a record of unread content weighted by the "
          "normalizer feels, at second order in a first record's field, V = -(3/2)[u^2 - l1^2 sum_(y~x) u_y^2] - "
          "[psi^2 - l2^2 sum psi_y^2] exactly (u the lean, psi the quadrupole field, sum_y u_y = u/l1); far away "
          "V -> -(3/2)[1 - 2 l1^2 sum_j cosh 2k_j] u^2, which is -(5/4) u^2 = -0.1239/r^2 on the massless surface "
          "(3,1,2); a record of content b feels -3 (a.b) u - 3 (w_a)_axis(b) psi at first order (orthogonal contents "
          "feel the quadrupole field when l2 != 0); two bodies couple through their mutual capacitance, cap1 cap2 G(d) "
          "far apart; content-blind clauses of the six-outcome odds have no first-order term")
