#!/usr/bin/env python3
"""B4 / kernel 2: the curvature member (blocks 62 / 101 and the 2026-09-24 constraint-algebra note).

Objects restated from docs (symbols, block 62 placement, p_j = 2 sin(k_j/2)):
  R1 = p^2 tr h - p.h.p
  R2 = -(p^2/4) tr(h h) + (1/2)|h p|^2 - (1/2)(p.h.p) tr h + (p^2/4) tr(h)^2
  L  = (1/wbar)[kinetic] + K wbar (u R1 + R2),   wbar = 1
  rotation-invariant kinetic: alpha h'_ij h'_ij + beta (tr h')^2      (repo's choice)
  cube-only kinetic family:   M1 sum h'_jj^2 + M2 sum_{i<j} h'_ii h'_jj + M3 sum_{i<j} h'_ij^2
  ('rotation-invariant' is M3 = 2 M1 - M2; block 62 states this).
Lagrangian-side cubic anisotropy  eps3 := M3/(2 M1 - M2) - 1  equals the probe's Hamiltonian g3/g1
(probe P-G1b: G = g1 Id + g2 tr x tr + g3 sum E_ii^2 is proportional to the inverse kinetic matrix).

Checks (exact sympy/Fraction arithmetic unless stated):
  C1 gauge: R1, R2 invariant under h -> h + p xi^T + xi p^T for all real p, xi (static null directions);
     the kinetic term is NOT invariant under time-dependent xi (no shift multiplier).
  C2 the potential R2 is the unique O_h (and S3) gauge-invariant two-derivative form: proportional to
     3D linearised EH -> no 'magnetic' g3 at O(k^2).
  C3 the repo's kinetic family has eps3 = 0 identically (all alpha, beta, incl. beta = -alpha).
  C4 exact TT speeds for general (M1, M2, M3) along [100],[110],[111]; eps3 = 0.1 reproduces the probe's
     {1, 1.10}/{1, 1.0747}/{1.0333, 1.0333} (independent implementation: lattice member + u constraint).
  C5 does constraint closure force eps3 = 0?  Generalise the 09-24 runner's lattice bracket to separate
     diagonal / face kinetic scales (alpha_d, alpha_f) and test whether {C[N],C[M]} (linear in P, flat
     strain) lies in the span of ALL relabellings, exactly, on 3^3 / 4^3 tori.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction as F
from itertools import product

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common_spin2 import (check_factory, eh_tensor, gauge_invariant_subspace, invariant_forms,  # noqa: E402
                          matrix_symbol_to_tensor, perm_matrices)

check, ST = check_factory()

p1, p2, p3 = sp.symbols("p1 p2 p3", real=True)
P = sp.Matrix([p1, p2, p3])
hs = sp.symbols("h11 h22 h33 h12 h13 h23", real=True)
h11, h22, h33, h12, h13, h23 = hs
H = sp.Matrix([[h11, h12, h13], [h12, h22, h23], [h13, h23, h33]])
psq = (P.T * P)[0]


def R1f(Hm):
    return psq * Hm.trace() - (P.T * Hm * P)[0]


def R2f(Hm):
    hp = Hm * P
    return (-(psq / 4) * (Hm * Hm).trace() + sp.Rational(1, 2) * (hp.T * hp)[0]
            - sp.Rational(1, 2) * (P.T * Hm * P)[0] * Hm.trace() + (psq / 4) * Hm.trace() ** 2)


# ---------------------------------------------------------------- C1 gauge
print("== C1: relabelling null directions ==")
xi = sp.Matrix(sp.symbols("x1 x2 x3", real=True))
dH = P * xi.T + xi * P.T
c1a = sp.expand(R1f(H + dH) - R1f(H)) == 0
c1b = sp.expand(R2f(H + dH) - R2f(H)) == 0
check("C1a R1 and R2 are exactly invariant under h -> h + p xi^T + xi p^T for all real p, xi "
      "(symbol identity; holds at every lattice wave vector via p_j = 2 sin(k_j/2))", c1a and c1b)
# kinetic not invariant under time-dependent xi: the variation is 2 alpha * |p xi'^T + xi' p^T|^2 != 0
al, be = sp.symbols("alpha beta", real=True)
xid = sp.Matrix(sp.symbols("y1 y2 y3", real=True))
dHd = P * xid.T + xid * P.T
kin_var = sp.expand(al * (dHd * dHd).trace() + be * dHd.trace() ** 2)
check("C1b the kinetic term is not invariant under time-dependent relabellings (no shift multiplier): "
      "longitudinal modes are zero-frequency modes, not a redundancy of the full dynamics",
      kin_var != 0, f"kinetic change for xi' : {sp.factor(kin_var)}")

# ---------------------------------------------------------------- C2 potential = unique gauge-invariant form
print("\n== C2: the potential's O_h decomposition ==")
hc3 = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
hsym = [h11, h22, h33, h12, h13, h23]
R2poly = sp.Poly(sp.expand(R2f(H)), *hsym)


def R2mat(k):
    sub = {p1: k[0], p2: k[1], p3: k[2]}
    Mx = np.zeros((6, 6))
    for i, a in enumerate(hsym):
        for j, b in enumerate(hsym):
            Mx[i, j] = float(sp.diff(R2f(H), a, b).subs(sub)) / 2.0
    return Mx


T_R2 = matrix_symbol_to_tensor(R2mat, 3).real
EH3 = eh_tensor(3)
c = (T_R2 @ EH3) / (EH3 @ EH3)
res = np.linalg.norm(T_R2 - c * EH3) / np.linalg.norm(T_R2)
B_oh = invariant_forms(3, perm_matrices(3, signed=True))
G_oh = gauge_invariant_subspace(B_oh, 3)
B_s3 = invariant_forms(3, perm_matrices(3, signed=False))
G_s3 = gauge_invariant_subspace(B_s3, 3)
print(f"   O_h forms {B_oh.shape[1]} (gauge-inv {G_oh.shape[1]}); S3-only forms {B_s3.shape[1]} "
      f"(gauge-inv {G_s3.shape[1]})")
check("C2 R2 = c * (3D linearised EH) with zero residual, and this is the unique O_h / S3 gauge-invariant "
      "two-derivative form: no magnetic cubic invariant at O(k^2)",
      res < 1e-12 and G_oh.shape[1] == 1 and G_s3.shape[1] == 1, f"c = {c:+.6f}, residual {res:.1e}")

# ---------------------------------------------------------------- C3 kinetic eps3 for the repo family
print("\n== C3: the repo's kinetic family ==")
hd = sp.symbols("d11 d22 d33 d12 d13 d23", real=True)
Hd = sp.Matrix([[hd[0], hd[3], hd[4]], [hd[3], hd[1], hd[5]], [hd[4], hd[5], hd[2]]])
kin_rot = sp.expand(al * (Hd * Hd).trace() + be * Hd.trace() ** 2)
M1 = sp.Poly(kin_rot, *hd).coeff_monomial(hd[0] ** 2)
M2 = sp.Poly(kin_rot, *hd).coeff_monomial(hd[0] * hd[1])
M3 = sp.Poly(kin_rot, *hd).coeff_monomial(hd[3] ** 2)
eps3 = sp.simplify(M3 / (2 * M1 - M2) - 1)
print(f"   alpha tr(h'^2) + beta (tr h')^2  ->  M1 = {M1}, M2 = {M2}, M3 = {M3};  eps3 = {eps3}")
check("C3 the repo's kinetic family has eps3 = M3/(2M1-M2) - 1 = 0 identically in (alpha, beta), "
      "including the closing ratio beta = -alpha", eps3 == 0)

# ---------------------------------------------------------------- C4 exact TT speeds, general cubic kinetic
print("\n== C4: TT speeds for the cube-only kinetic family ==")
m1, m2, m3, X, Kc = sp.symbols("M1 M2 M3 X K", real=True)
kin_cub = m1 * sum(d ** 2 for d in hd[:3]) + m2 * (hd[0] * hd[1] + hd[0] * hd[2] + hd[1] * hd[2]) \
    + m3 * (hd[3] ** 2 + hd[4] ** 2 + hd[5] ** 2)
Kin = sp.Matrix(6, 6, lambda i, j: sp.diff(kin_cub, hd[i], hd[j]) / 2)        # L_kin = h'^T Kin h'
Vq = sp.Matrix(6, 6, lambda i, j: sp.diff(R2f(H), hsym[i], hsym[j]) / 2)     # R2 = h^T Vq h
r1 = sp.Matrix([sp.diff(R1f(H), a) for a in hsym])
# EOM for e^{-i w t}: X Kin h + K Vq h + (K/2) u r1 = 0 ;  r1.h = 0   (from L = h'Kin h' + K(u R1 + h Vq h))
Mfull = sp.zeros(7, 7)
Mfull[:6, :6] = X * Kin + Kc * Vq
Mfull[:6, 6] = Kc * r1 / 2
Mfull[6, :6] = r1.T


def tt_roots(direction, M1v, M2v, M3v):
    sub = {p1: direction[0], p2: direction[1], p3: direction[2], m1: M1v, m2: M2v, m3: M3v, Kc: 1}
    det = sp.factor(Mfull.subs(sub).det())
    pp = sum(sp.Integer(v) ** 2 for v in direction)
    roots = [r for r in sp.roots(sp.Poly(det, X)).items()]
    nz = sorted([(sp.nsimplify(r / pp), mult) for r, mult in roots if r != 0], key=lambda t: float(t[0]))
    return det, nz


# rotation-invariant case, symbolic alpha, beta: reproduce block 62's determinant shape
sub_rot = {m1: al + be, m2: 2 * be, m3: 2 * al}
for name, dv in (("[100]", (1, 0, 0)), ("[110]", (1, 1, 0)), ("[111]", (1, 1, 1)), ("(1,2,2)", (1, 2, 2))):
    det = sp.factor(Mfull.subs(sub_rot).subs({p1: dv[0], p2: dv[1], p3: dv[2], Kc: 1}).det())
    pp = sum(v * v for v in dv)
    sols = sp.roots(sp.Poly(det, X))
    nz = {sp.simplify(r / pp): mm for r, mm in sols.items() if r != 0}
    print(f"   rotation-invariant kinetic {name}: det = {det};  nonzero X/p^2 roots {nz}")
    check(f"C4a rotation-invariant kinetic, {name}: single TT root X = K p^2/(4 alpha) with multiplicity 2",
          nz == {1 / (4 * al): 2})

# probe-equivalent cubic witness: eps3 = 0.1 (M3 = 1, 2M1 - M2 = 1/1.1, M2 = 0)
# (a) WITHOUT the lapse multiplier u: this is the probe's model class (spatial gauge only) -> must
#     reproduce probe P-G1b exactly (independent implementation of the same object);
# (b) WITH the member's u-constraint R1 = 0: the member's own numbers.
expect = {"[100]": (1.0, 1.1), "[110]": (1.0, 1.07471), "[111]": (1.03333, 1.03333)}
for with_u in (False, True):
    tag = "member (with u constraint)" if with_u else "no lapse multiplier (probe's model class)"
    print(f"   cube-only witness eps3 = 1/10 (M1 = 5/11, M2 = 0, M3 = 1), {tag}; omega^2 / (K p^2/(2 M3)):")
    for name, dv in (("[100]", (1, 0, 0)), ("[110]", (1, 1, 0)), ("[111]", (1, 1, 1))):
        Mm = Mfull if with_u else Mfull[:6, :6]
        sub = {p1: dv[0], p2: dv[1], p3: dv[2], m1: sp.Rational(5, 11), m2: 0, m3: 1, Kc: 1}
        det = sp.factor(Mm.subs(sub).det())
        pp = sum(v * v for v in dv)
        vals = []
        for r, mult in sp.roots(sp.Poly(det, X)).items():
            if r != 0:
                vals += [float(r / pp) * 2] * mult
        vals = sorted(vals)
        print(f"     {name}: {[round(v, 6) for v in vals]}  (probe P-G1b: {expect[name]})")
        if not with_u:
            pos = [v_ for v_ in vals if v_ > 0]
            check(f"C4b no-multiplier eps3 = 0.1 {name}: the positive (TT) roots reproduce the probe's g3 = 0.1 "
                  f"values (probe also drops the non-positive trace root)",
                  len(pos) == 2 and all(abs(a - b) < 1e-4 for a, b in zip(pos, expect[name])),
                  f"non-TT root(s) {[round(v_, 6) for v_ in vals if v_ <= 0]} (conformal-sign scalar, removed by u)")
        else:
            check(f"C4b' member with u constraint, eps3 = 0.1 {name}: two TT roots, split (birefringent) "
                  f"except along [111]", len(vals) == 2 and ((abs(vals[0] - vals[1]) < 1e-12) == (name == "[111]")),
                  f"split = {vals[-1] - vals[0]:.6f}")
# general [100] formula
_, nz100 = None, None
det100 = sp.factor(Mfull.subs({p1: 1, p2: 0, p3: 0, Kc: 1}).det())
print(f"   general cube-only [100] determinant: {det100}")
check("C4c along [100] the two TT roots are X = 1/(2 M3) and X = 1/(2(2M1 - M2)) (times K p^2): "
      "degenerate iff eps3 = 0",
      sp.simplify(det100.subs(X, 1 / (2 * m3))) == 0 and sp.simplify(det100.subs(X, 1 / (2 * (2 * m1 - m2)))) == 0)


# ---------------------------------------------------------------- C5 closure vs eps3 (exact lattice bracket)
print("\n== C5: does lapse-constraint closure force eps3 = 0? (exact Fraction lattice bracket) ==")
PAIRS = ((0, 1), (0, 2), (1, 2))
ZERO = F(0)


def unit(j):
    return tuple(1 if k == j else 0 for k in range(3))


def torus(side):
    sites = list(product(range(side), repeat=3))

    def sh(x, v, s=1):
        return tuple((x[k] + s * v[k]) % side for k in range(3))
    return sites, sh


def lapse_bracket(sites, sh, n, m, alpha_d, alpha_f, c):
    """As the 09-24 runner's lapse_bracket (four-corner timing), but with independent kinetic scales:
    dH/dP_jj = (P_jj - c sum P)/(2 alpha_d),  dH/dP_ij = P_ij/(4 alpha_f).  alpha_d = alpha_f is the
    runner's object; alpha_d != alpha_f is the cube-only family with eps3 = alpha_d/alpha_f - 1."""
    coef = {}
    for x in sites:
        second = [n[sh(x, unit(i))] - 2 * n[x] + n[sh(x, unit(i), -1)] for i in range(3)]
        grads = [-sum(second, ZERO) + second[j] for j in range(3)]
        total = sum(grads, ZERO)
        for j in range(3):
            coef[("d", x, j)] = m[x] / (2 * alpha_d) * (grads[j] - c * total)
    for y in sites:
        for (i, j) in PAIRS:
            corners = [y, sh(y, unit(i)), sh(y, unit(j)), sh(sh(y, unit(i)), unit(j))]
            mean = sum((m[z] for z in corners), ZERO) / 4
            mixed = n[y] - n[sh(y, unit(i))] - n[sh(y, unit(j))] + n[sh(sh(y, unit(i)), unit(j))]
            coef[("f", y, (i, j))] = mean / (4 * alpha_f) * 2 * mixed
    return coef


def relabelling(sites, sh, xi):
    coef = {}
    for x in sites:
        for j in range(3):
            coef[("d", x, j)] = 2 * (xi[(x, j)] - xi[(sh(x, unit(j), -1), j)])
    for y in sites:
        for (i, j) in PAIRS:
            coef[("f", y, (i, j))] = xi[(sh(y, unit(i)), j)] - xi[(y, j)] + xi[(sh(y, unit(j)), i)] - xi[(y, i)]
    return coef


def rank_of(rows):
    M = sp.Matrix(rows)
    return M.rank()


def closes(side, n, m, alpha_d, alpha_f, c, kk=F(5, 11)):
    sites, sh = torus(side)
    b1 = lapse_bracket(sites, sh, n, m, alpha_d, alpha_f, c)
    b2 = lapse_bracket(sites, sh, m, n, alpha_d, alpha_f, c)
    keys = sorted(b1)
    br = [kk * (b1[k] - b2[k]) for k in keys]
    cols = []
    for x in sites:
        for j in range(3):
            xi = {(z, l): (F(1) if (z, l) == (x, j) else ZERO) for z in sites for l in range(3)}
            g = relabelling(sites, sh, xi)
            cols.append([g[k] for k in keys])
    base = rank_of(cols)
    ext = rank_of(cols + [br])
    return ext == base, base, ext


s3, _ = torus(3)
d0 = {x: F(1) if x == (0, 0, 0) else ZERO for x in s3}
d1 = {x: F(1) if x == (1, 0, 0) else ZERO for x in s3}
s3b = {x: F((2 * x[0] + 3 * x[1] + 5 * x[2] + 1) % 7 - 3) for x in s3}
s3c = {x: F((x[0] * x[1] + 4 * x[2] + 2) % 5 - 2) for x in s3}
a = F(3, 7)
rows = []
for label, ad, af, cc in (("DeWitt, eps3 = 0 (runner object)", a, a, F(1, 2)),
                          ("c = 1/2, eps3 = +1/10", a * F(11, 10), a, F(1, 2)),
                          ("c = 1/2, eps3 = -1/5", a * F(4, 5), a, F(1, 2)),
                          ("c = 1/3, eps3 = 0", a, a, F(1, 3))):
    ok1, b1_, e1_ = closes(3, d0, d1, ad, af, cc)
    ok2, b2_, e2_ = closes(3, s3b, s3c, ad, af, cc)
    rows.append((label, ok1 and ok2))
    print(f"   {label:36s}: delta-lapse pair closes={ok1} (rank {b1_}->{e1_}); generic pair closes={ok2} "
          f"(rank {b2_}->{e2_})")
check("C5a control: the 09-24 object (eps3 = 0, c = 1/2) closes onto relabellings on the 3^3 torus "
      "(two lapse pairs)", rows[0][1])
check("C5b eps3 = +1/10 and eps3 = -1/5 at c = 1/2 do NOT close: the bracket leaves the span of all "
      "relabellings -- closure of the lapse-constraint algebra forces eps3 = 0 (no kinetic birefringence)",
      (not rows[1][1]) and (not rows[2][1]))
check("C5c c = 1/3 at eps3 = 0 does not close (reproduces the note's c = 1/2 requirement)", not rows[3][1])

# continuum-symbol version of C5 (leading derivative order): which (a_off, b_diag, c_tr) admit eta?
ka = sp.symbols("k1 k2 k3", real=True)
v = sp.Matrix(sp.symbols("v1 v2 v3"))
eta = sp.Matrix(sp.symbols("e1 e2 e3"))
A_, B_, C_ = sp.symbols("A B C")       # inverse kinetic: off-diag scale A, diag B*T_ii + C*tr T
kv = sum(ka[i] * v[i] for i in range(3))
Tm = sp.Matrix(3, 3, lambda i, j: (ka[i] * v[j] + ka[j] * v[i]) / 2 - (kv if i == j else 0))
GT = sp.Matrix(3, 3, lambda i, j: (A_ * Tm[i, j] if i != j else B_ * Tm[i, i] + C_ * Tm.trace()))
eqs = []
for i in range(3):
    for j in range(i, 3):
        target = (ka[i] * (A_ * v[j] + eta[j]) + ka[j] * (A_ * v[i] + eta[i])) / 2
        eqs.append(sp.expand(GT[i, j] - target))
sol = sp.solve(eqs, list(eta), dict=True)
cond = None
if not sol:
    # eta must solve the off-diagonal equations -> eta = 0 generically; impose and read the conditions
    off = [e for e in eqs]
    sub0 = {eta[0]: 0, eta[1]: 0, eta[2]: 0}
    rem = [sp.expand(e.subs(sub0)) for e in off]
    coeffs = set()
    for e in rem:
        for mon_coeff in sp.Poly(e, *ka, *v).coeffs():
            coeffs.add(sp.factor(mon_coeff))
    cond = sp.solve(list(coeffs), [B_, C_], dict=True)
print(f"   continuum symbol: solutions for eta: {sol}; conditions for closure: {cond}")
check("C5d continuum leading-order symbol: closure for arbitrary lapses requires B = A (eps3 = 0) and "
      "C = -A/2 (DeWitt) -- the hypersurface-deformation closure is the protecting symmetry",
      cond == [{B_: A_, C_: -A_ / 2}])

print(f"\nTOTAL: PASS={ST['PASS']} FAIL={ST['FAIL']}")
