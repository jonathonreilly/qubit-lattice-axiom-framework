#!/usr/bin/env python3
"""check.py -- J:derive:review-20260929-tensor-effective-stiffness:a1

Does the helicity-one 'partner' bound for an effective tensor stiffness need a
finite positive Gram of move amplitudes, or only positivity of the symbol?

Self-contained (sympy only; exact rational arithmetic throughout).  Machinery is
deliberately disjoint from the landed runners
(scripts/tensor_symbol_rational_review_controls_2026_09_29.py and
 scripts/tensor_trace_schur_review_controls_2026_09_29.py), which use
 double-factorial monomial moments and an LDL^T pivot test.  Here:
   * sphere averages come from symbolic integration in spherical coordinates;
   * positivity/rank come from the characteristic polynomial sign pattern;
   * helicity weights are first validated against explicit projectors;
   * the new content is an exact perfect-square identity and its consequences.
All objects are supplied mathematical comparators; no axiom or physical carrier
is asserted.  Output: one PASS/FAIL line per check, TOTAL, optional HIT, SUMMARY.
"""
import itertools
import random
import sys
import time
from functools import lru_cache

import sympy as sp
from sympy import Rational as R

T0 = time.time()
RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name + ((" | " + str(detail)) if detail != "" else ""), flush=True)


# ---------------------------------------------------------------------------
# 0. exact sphere averages by symbolic integration in spherical coordinates
# ---------------------------------------------------------------------------
nx, ny, nz = sp.symbols("nx ny nz", real=True)
NV = sp.Matrix([nx, ny, nz])
th, ph = sp.symbols("theta phi", real=True)


@lru_cache(maxsize=None)
def mono_avg(a, b, c):
    if a % 2 or b % 2 or c % 2:
        return sp.Integer(0)
    # integrand over (theta, phi) of nx^a ny^b nz^c sin(theta)
    ph_part = sp.integrate(sp.cos(ph) ** a * sp.sin(ph) ** b, (ph, 0, 2 * sp.pi))
    th_part = sp.integrate(sp.sin(th) ** (a + b + 1) * sp.cos(th) ** c, (th, 0, sp.pi))
    return sp.nsimplify(sp.simplify(ph_part * th_part / (4 * sp.pi)))


def avg(expr):
    p = sp.Poly(sp.expand(expr), nx, ny, nz)
    tot = sp.Integer(0)
    for mon, coeff in p.terms():
        tot += coeff * mono_avg(*mon)
    return sp.expand(tot)


check("0.1 sphere averages <nx^2>,<nx^4>,<nx^2 ny^2>,<nx^6>,<nx^2 ny^2 nz^2>",
      (avg(nx**2), avg(nx**4), avg(nx**2 * ny**2), avg(nx**6), avg(nx**2 * ny**2 * nz**2))
      == (R(1, 3), R(1, 5), R(1, 15), R(1, 7), R(1, 105)))

# ---------------------------------------------------------------------------
# 1. helicity weight formulas vs explicit projectors (exact, rational unit vectors)
# ---------------------------------------------------------------------------
COMPS = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
U = sp.symbols("u0:6")


def sym_from_u(u):
    M = sp.zeros(3)
    for a, (i, j) in enumerate(COMPS):
        M[i, j] = u[a]
        M[j, i] = u[a]
    return M


MU = sym_from_u(U)
Z = MU * NV
F = (NV.T * Z)[0]
TRM = MU.trace()
H1 = 2 * (Z.dot(Z) - F**2)
TT = (MU * MU).trace() - 2 * Z.dot(Z) + F**2 - (TRM - F) ** 2 / 2

unit_vectors = [
    sp.Matrix([R(2, 3), R(2, 3), R(1, 3)]),
    sp.Matrix([R(1, 3), R(2, 3), R(-2, 3)]),
    sp.Matrix([R(6, 7), R(2, 7), R(3, 7)]),
    sp.Matrix([R(4, 9), R(-4, 9), R(7, 9)]),
    sp.Matrix([0, 0, 1]),
]
Ms = [
    sp.Matrix([[1, 2, -1], [2, 3, 5], [-1, 5, -2]]),
    sp.Matrix([[0, 1, 4], [1, -3, 2], [4, 2, 7]]),
    sp.Matrix([[2, -1, 0], [-1, 5, 3], [0, 3, 1]]),
]
ok = True
for n in unit_vectors:
    assert sp.simplify(n.dot(n) - 1) == 0
    P = sp.eye(3) - n * n.T
    for M in Ms:
        # TT: transverse-traceless part of P M P
        PMP = P * M * P
        ttp = PMP - (PMP.trace() / 2) * P
        tt_norm = (ttp * ttp).trace()
        # helicity-one part: n w^T + w n^T with w the transverse part of M n
        w = P * (M * n)
        h1p = n * w.T + w * n.T
        h1_norm = (h1p * h1p).trace()
        sub = {NV[0]: n[0], NV[1]: n[1], NV[2]: n[2]}
        uvals = {U[a]: M[i, j] for a, (i, j) in enumerate(COMPS)}
        ok = ok and sp.simplify(TT.subs(sub).subs(uvals) - tt_norm) == 0
        ok = ok and sp.simplify(H1.subs(sub).subs(uvals) - h1_norm) == 0
check("1.1 H1(M,n)=2(|Mn|^2-f^2), TT(M,n) equal the squared norms of the explicit helicity-1 / TT projections (5 directions x 3 tensors)", ok)

# ---------------------------------------------------------------------------
# 2. the exact quarter functional as an 18x18 form; perfect-square identity
# ---------------------------------------------------------------------------
def hess_half(expr):
    return sp.Matrix(6, 6, lambda a, b: sp.expand(sp.diff(expr, U[a], U[b]) / 2))


PI_H1 = hess_half(H1)
PI_TT = hess_half(TT)
PI_Q = PI_H1 - PI_TT / 4

G = (NV.T * MU * NV)[0] - TRM / 3          # f - trM/3 (linear in u, cubic-ish in n)
XI = [sp.expand(sp.diff(G, U[a])) for a in range(6)]   # covector Y(n)=nn^T-I/3 in u-coordinates

nn = [nx, ny, nz]
Qm = sp.zeros(18, 18)
Q2 = sp.zeros(18, 18)
for a in range(6):
    for b in range(a, 6):
        for k in range(3):
            for l in range(k, 3):
                v1 = avg(PI_Q[a, b] * nn[k] * nn[l])
                v2 = R(9, 4) * avg(XI[a] * XI[b] * nn[k] * nn[l])
                for (aa, kk, bb, ll) in {(a, k, b, l), (a, l, b, k), (b, k, a, l), (b, l, a, k)}:
                    Qm[3 * aa + kk, 3 * bb + ll] = v1
                    Q2[3 * aa + kk, 3 * bb + ll] = v2
entries_equal = (Qm - Q2) == sp.zeros(18, 18)
check("2.1 PERFECT-SQUARE IDENTITY, entrywise: <(Pi_H1 - Pi_TT/4)_ab n_k n_l> = (9/4) <Y_a Y_b n_k n_l>, Y(n)=nn^T-I/3 (all 6x6x3x3 entries)",
      entries_equal)
check("2.2 Q symmetric 18x18 rational", Qm == Qm.T)

x = sp.symbols("x")
cp = Qm.charpoly(x).all_coeffs()      # det(xI - Q): signs (-1)^k e_k
e_k = [(-1) ** k * c for k, c in enumerate(cp)]
psd = all(c >= 0 for c in e_k)
rank = max(k for k, c in enumerate(e_k) if c != 0)
check("2.3 Q is positive semidefinite (all elementary symmetric functions of the spectrum >= 0, exact)", psd)
check("2.4 rank Q = 10 (= dim of odd cubic functions on S^2, spin 1 + spin 3); kernel dimension 8",
      rank == 10 and len(Qm.nullspace()) == 8, f"rank={rank}")
# cross-validation of the spherical-coordinate integration against the closed double-factorial moment formula
import math


def _df(k):
    return math.prod(range(k, 0, -2)) if k > 0 else 1


def avg_closed_form(expr):
    p = sp.Poly(sp.expand(expr), nx, ny, nz)
    return sum(c * R(math.prod(_df(k - 1) for k in mon), _df(sum(mon) + 1))
               for mon, c in p.terms() if all(k % 2 == 0 for k in mon))


random.seed(11)
vrand = [random.randint(-6, 6) for _ in range(18)]
Mrand = sp.zeros(3)
for a, (i, j) in enumerate(COMPS):
    val = sum(vrand[3 * a + k] * nn[k] for k in range(3))
    Mrand[i, j] = val
    Mrand[j, i] = val
zr = Mrand * NV
fr = NV.dot(zr)
h1r = 2 * (zr.dot(zr) - fr**2)
ttr = (Mrand * Mrand).trace() - 2 * zr.dot(zr) + fr**2 - (Mrand.trace() - fr) ** 2 / 2
vv_ = sp.Matrix(vrand)
quad_form = (vv_.T * Qm * vv_)[0]
check("2.5 the 18x18 matrix reproduces <H1-TT/4> for a random integer first-moment vector, matching an independent closed-form moment formula",
      quad_form == avg_closed_form(h1r - ttr / 4) == avg(h1r - ttr / 4))

# sharpness: M(n)=sym([n]x A) has f=trM=0, so <H1> = <TT>/4 exactly
aa = sp.symbols("A0:5")
Amat = sp.Matrix([[aa[0], aa[2], aa[3]], [aa[2], aa[1], aa[4]], [aa[3], aa[4], -aa[0] - aa[1]]])
cross = sp.Matrix([[0, -nz, ny], [nz, 0, -nx], [-ny, nx, 0]])
xis = sp.Matrix(sp.symbols("x0:3"))
Mn = (NV * xis.T + xis * NV.T) / 2 + (cross * Amat - Amat * cross) / 2


def weights_of_Mn(Mn):
    z = Mn * NV
    f = NV.dot(z)
    trM = Mn.trace()
    h1 = 2 * (z.dot(z) - f**2)
    tt = (Mn * Mn).trace() - 2 * z.dot(z) + f**2 - (trM - f) ** 2 / 2
    return avg(h1), avg(tt), avg(R(9, 4) * (f - trM / 3) ** 2)


h1a, tta, sqa = weights_of_Mn(Mn)
check("2.6 scalar-compatible family sym(n xi)+sym([n]xA): <H1>-<TT>/4 = |xi|^2/3 = (9/4)<(f-trM/3)^2> (symbolic in xi, A)",
      sp.expand(h1a - tta / 4 - (xis.dot(xis)) / 3) == 0 and sp.expand(sqa - xis.dot(xis) / 3) == 0)
Ain = {aa[0]: 1, aa[1]: -1, aa[2]: 0, aa[3]: 0, aa[4]: 0, xis[0]: 0, xis[1]: 0, xis[2]: 0}
h1s, tts = h1a.subs(Ain), tta.subs(Ain)
check("2.7 the 1/4 is attained: M=sym([n]x diag(1,-1,0)) has <TT> > 0 and <H1> = <TT>/4",
      tts > 0 and sp.simplify(h1s - tts / 4) == 0, f"<H1>={h1s}, <TT>={tts}")

# ---------------------------------------------------------------------------
# 3. extension from Gram sums to arbitrary positive (non-Gram) quadratic symbols
# ---------------------------------------------------------------------------
# A quadratic symbol is V(n)^{ab}=sum_{k<=l} c^{ab}_{kl} n_k n_l, contravariant on the u-coordinates.
# Its H1 / TT weights are tr(Pi V(n)).  Entrywise equality 2.1 gives, by linearity,
#   <H1>_V - <TT>_V/4 = (9/4) < xi(n)^T V(n) xi(n) >  for EVERY such V.
Vtest = sp.Matrix(6, 6, lambda a, b: 0)
import random
random.seed(7)
coef = {}
for a in range(6):
    for b in range(a, 6):
        for k in range(3):
            for l in range(k, 3):
                coef[(a, b, k, l)] = random.randint(-9, 9)
Vtest = sp.zeros(6, 6)
for (a, b, k, l), c in coef.items():
    Vtest[a, b] += c * nn[k] * nn[l]
    if a != b:
        Vtest[b, a] += c * nn[k] * nn[l]
lhs = avg(sum(PI_Q[a, b] * Vtest[a, b] for a in range(6) for b in range(6)))
rhs = R(9, 4) * avg(sum(XI[a] * XI[b] * Vtest[a, b] for a in range(6) for b in range(6)))
check("3.1 random indefinite quadratic symbol (126 integer coefficients): L(V)=(9/4)<xi^T V xi>", sp.simplify(lhs - rhs) == 0)

# ---------------------------------------------------------------------------
# 4. positive-but-not-Gram: Choi's biquadratic form inside the tensor space
# ---------------------------------------------------------------------------
cx = sp.symbols("c1:4")      # momentum-like variable (x)
cy = sp.symbols("d1:4")      # tensor amplitudes  (y)
f_choi = (sum(cx[i] ** 2 * cy[i] ** 2 for i in range(3))
          - 2 * sum(cx[i] * cx[(i + 1) % 3] * cy[i] * cy[(i + 1) % 3] for i in range(3))
          + sum(cx[i] ** 2 * cy[(i + 1) % 3] ** 2 for i in range(3)))
Nmat = sp.hessian(f_choi, cy) / 2          # PSD matrix in cy for each cx
ok = True
for r in (1, 2, 3):
    for S in itertools.combinations(range(3), r):
        m = sp.expand(Nmat.extract(list(S), list(S)).det())
        if r < 3:
            P = sp.Poly(m, *cx)
            ok = ok and all(c >= 0 for c in P.coeffs()) and all(all(e % 2 == 0 for e in mon) for mon in P.monoms())
det_N = sp.expand(Nmat.det())
a1_, a2_, a3_ = sp.symbols("a1 a2 a3", positive=True)
uu, vv, ww = a1_**2 * a2_, a1_ * a3_**2, a2_**2 * a3_       # cube roots of the three positive monomials
s1, s2, s3 = cx[0] ** 2, cx[1] ** 2, cx[2] ** 2
T_poly = s1**2 * s2 + s1 * s3**2 + s2**2 * s3 - 3 * s1 * s2 * s3
amgm = sp.expand(uu**3 + vv**3 + ww**3 - 3 * uu * vv * ww
                 - sp.Rational(1, 2) * (uu + vv + ww) * ((uu - vv) ** 2 + (vv - ww) ** 2 + (ww - uu) ** 2))
sub_cube = {s1: a1_**3, s2: a2_**3, s3: a3_**3}
check("4.1 Choi form PSD: every principal minor of N(x) >= 0 (3x3 det via cube-AM/GM identity u^3+v^3+w^3-3uvw = (u+v+w)*sum (u-v)^2/2)",
      ok and sp.expand(det_N - T_poly) == 0 and amgm == 0
      and sp.expand(T_poly.subs(sub_cube, simultaneous=True) - (uu**3 + vv**3 + ww**3 - 3 * uu * vv * ww)) == 0)

# non-SOS: any bilinear l(x,y)=x^T A y in a sum of squares equal to f must vanish on the zeros of f
Asym = sp.Matrix(3, 3, sp.symbols("A11 A12 A13 A21 A22 A23 A31 A32 A33"))
zeros = [(sp.Matrix([1, 0, 0]), sp.Matrix([0, 0, 1])), (sp.Matrix([0, 1, 0]), sp.Matrix([1, 0, 0])),
         (sp.Matrix([0, 0, 1]), sp.Matrix([0, 1, 0]))]
for sg in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]:
    zeros.append((sp.Matrix(sg), sp.Matrix(sg)))
is_zero = all(sp.expand(f_choi.subs({**dict(zip(cx, z[0])), **dict(zip(cy, z[1]))})) == 0 for z in zeros)
eqs = [(z[0].T * Asym * z[1])[0] for z in zeros]
sol = sp.linsolve(eqs, list(Asym))
sol = list(sol)[0]
free = sorted(set().union(*[e.free_symbols for e in sol]), key=str)
Asol = sp.Matrix(3, 3, list(sol))
is_diag_traceless = all(Asol[i, j] == 0 for i in range(3) for j in range(3) if i != j) and sp.simplify(Asol.trace()) == 0
ell = sum(Asol[i, j] * cx[i] * cy[j] for i in range(3) for j in range(3))
coef_x1y2 = sp.Poly(sp.expand(ell**2), *cx, *cy).as_dict().get((2, 0, 0, 0, 2, 0), 0)
coef_f = sp.Poly(f_choi, *cx, *cy).as_dict().get((2, 0, 0, 0, 2, 0), 0)
check("4.2 Choi form is NOT a sum of squares of bilinear forms: forms vanishing on its 7 zeros are diag(a1,a2,a3), a1+a2+a3=0; their squares never contain x1^2 y2^2, f does",
      is_zero and is_diag_traceless and len(free) == 2 and coef_x1y2 == 0 and coef_f == 1,
      f"free parameters={len(free)}, coeff of x1^2y2^2: in any SOS=0, in f={coef_f}")

# embed in tensor space: amplitudes y = (u_xy, u_xz, u_yz); momentum x = n.  Contravariant 6x6 symbol:
Wsym = sp.zeros(6, 6)
Nn = Nmat.subs({cx[0]: nx, cx[1]: ny, cx[2]: nz})
for i in range(3):
    for j in range(3):
        Wsym[3 + i, 3 + j] = Nn[i, j]
xi_off = sp.Matrix([XI[3], XI[4], XI[5]])
L_choi = avg(sum(PI_Q[a, b] * Wsym[a, b] for a in range(6) for b in range(6)))
sq_choi = R(9, 4) * avg((xi_off.T * Nn * xi_off)[0])
H1_choi = avg(sum(PI_H1[a, b] * Wsym[a, b] for a in range(6) for b in range(6)))
TT_choi = avg(sum(PI_TT[a, b] * Wsym[a, b] for a in range(6) for b in range(6)))
check("4.3 the Choi symbol (positive, not Gram) obeys <H1> >= <TT>/4 with <H1>-<TT>/4 = (9/4)<xi^T W xi> > 0",
      L_choi == sq_choi and L_choi > 0 and H1_choi - TT_choi / 4 == L_choi,
      f"<H1>={H1_choi}, <TT>={TT_choi}, L={L_choi}")

# finite-range lattice symbol with one gapped (trace) channel; exact Schur complement
q1, q2, q3 = sp.symbols("q1 q2 q3", real=True)
qs = [q1, q2, q3]
sins = [sp.sin(q) for q in qs]
Wlat = Nmat.subs({cx[0]: sins[0], cx[1]: sins[1], cx[2]: sins[2]})
beta = sp.Matrix(sins)
Vlat = sp.zeros(4, 4)
Vlat[0, 0] = 1
Vlat[0, 1:] = beta.T
Vlat[1:, 0] = beta
Vlat[1:, 1:] = beta * beta.T + Wlat
Lfac = sp.eye(4)
Lfac[1:, 0] = beta
Dfac = sp.diag(1, *[0] * 3)
Dfac[1:, 1:] = Wlat
factor_ok = sp.simplify(Lfac * Dfac * Lfac.T - Vlat) == sp.zeros(4, 4)
Schur = sp.simplify(Vlat[1:, 1:] - Vlat[1:, 0] * Vlat[0, 1:] / Vlat[0, 0])
schur_ok = sp.simplify(Schur - Wlat) == sp.zeros(3, 3)
eps = sp.symbols("epsilon", positive=True)
S2 = (Schur.subs({q: eps * q for q in qs}, simultaneous=True)).applyfunc(lambda e: sp.series(e, eps, 0, 4).removeO().coeff(eps, 2))
S2_ok = sp.simplify(S2 - Nmat.subs({cx[0]: q1, cx[1]: q2, cx[2]: q3})) == sp.zeros(3, 3)
v0 = Vlat.subs({q1: 0, q2: 0, q3: 0})
check("4.4 lattice symbol V(q)=[[1,b^T],[b,bb^T+N(sin q)]], b=sin q: entries trigonometric polynomials; V=L diag(1,N) L^T (PSD); V(0)=diag(1,0,0,0); exact Schur complement N(sin q) with leading O(q^2) part the Choi matrix",
      factor_ok and schur_ok and S2_ok and v0 == sp.diag(1, 0, 0, 0))

# unreduced vs reduced weights (gapped trace coupling b b^T not removed)
beta_n = sp.Matrix([nx, ny, nz])
Braw = Wsym.copy()
for i in range(3):
    for j in range(3):
        Braw[3 + i, 3 + j] = Nn[i, j] + beta_n[i] * beta_n[j]
H1_raw = avg(sum(PI_H1[a, b] * Braw[a, b] for a in range(6) for b in range(6)))
TT_raw = avg(sum(PI_TT[a, b] * Braw[a, b] for a in range(6) for b in range(6)))
check("4.5 measuring helicity BEFORE eliminating the gapped channel changes the weights (raw <H1>,<TT> differ from reduced); both still satisfy the quarter bound",
      (H1_raw, TT_raw) != (H1_choi, TT_choi) and H1_raw - TT_raw / 4 >= 0 and H1_choi - TT_choi / 4 >= 0,
      f"raw H1/TT = {H1_raw}/{TT_raw}; reduced H1/TT = {H1_choi}/{TT_choi}")

# a finite positive Gram with one gapped column gives an SOS effective stiffness (so non-SOS symbols have no such Gram)
random.seed(3)
eps_ = sp.symbols("e_", positive=True)
Q3 = sp.Matrix(qs)
ok46 = True
for trial in range(3):
    rows = 5
    a_ = sp.Matrix([random.randint(1, 5) for _ in range(rows)])
    Cc = sp.Matrix(rows, 3, lambda i, j: random.randint(-4, 4))
    Dc = sp.Matrix(rows, 3, lambda i, j: random.randint(-4, 4))
    Bs = [sp.Matrix(rows, 3, lambda i, j: random.randint(-4, 4)) for _ in range(3)]
    Es = [sp.Matrix(rows, 3, lambda i, j: random.randint(-4, 4)) for _ in range(3)]
    col0 = a_ + eps_ * Cc * Q3 + eps_**2 * Dc * Q3
    cols = [eps_ * Bs[j] * Q3 + eps_**2 * Es[j] * Q3 for j in range(3)]
    Rm = sp.Matrix.hstack(col0, *cols)
    Vg = (Rm.T * Rm)
    Sg = Vg[1:, 1:] - Vg[1:, 0] * Vg[0, 1:] / Vg[0, 0]
    S2g = Sg.applyfunc(lambda e: sp.cancel(sp.together(e) / eps_**2).subs(eps_, 0))
    Bq = sp.Matrix.hstack(*[Bs[j] * Q3 for j in range(3)])
    Pproj = sp.eye(rows) - a_ * a_.T / (a_.T * a_)[0]
    pred = (Pproj * Bq).T * (Pproj * Bq)
    ok46 = ok46 and sp.simplify(S2g - pred) == sp.zeros(3, 3)
check("4.6 finite Gram with one gapped column: leading Schur complement is exactly (PB)^T(PB) with B linear in q (sum of squares of linear forms), incl. random O(q^2) and O(q) trace corrections (3 exact trials)", ok46)

# ---------------------------------------------------------------------------
# 5. SO(3)-isotropic leading symbols on traceless tensors: PSD cone = Gram cone
# ---------------------------------------------------------------------------
def so3_gen(a):
    return sp.Matrix(3, 3, lambda i, j: -sp.LeviCivita(a, i, j))


I3 = sp.eye(3)
Ltot = []
for a in range(3):
    g = so3_gen(a)
    Ltot.append(sp.kronecker_product(g, I3, I3) + sp.kronecker_product(I3, g, I3) + sp.kronecker_product(I3, I3, g))
CAS = -(Ltot[0] ** 2 + Ltot[1] ** 2 + Ltot[2] ** 2)
eigs = CAS.eigenvals()
check("5.1 Casimir of 3 (x) 3 (x) 3 has J(J+1) spectrum {0,2,6,12}", set(eigs.keys()) == {0, 2, 6, 12})


def proj_J(J):
    lam = J * (J + 1)
    P = sp.eye(27)
    for mu in eigs:
        if mu != lam:
            P = P * (CAS - mu * sp.eye(27)) / (lam - mu)
    return P


def vec27(Y, q):
    return sp.Matrix([Y[i, j] * q[k] for i in range(3) for j in range(3) for k in range(3)])


zhat = sp.Matrix([0, 0, 1])
hel_basis = [sp.diag(-1, -1, 2), sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]), sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
             sp.diag(1, -1, 0), sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])]
vs = [vec27(Y, zhat) for Y in hel_basis]
norms = [(v.T * v)[0] for v in vs]
rays = {}
diag_ok = True
for J in (1, 2, 3):
    PJ = proj_J(J)
    Bm = sp.Matrix(5, 5, lambda a, b: (vs[a].T * PJ * vs[b])[0] / sp.sqrt(norms[a] * norms[b]))
    lam = [Bm[0, 0], Bm[1, 1], Bm[3, 3]]
    pairs_equal = Bm[1, 1] == Bm[2, 2] and Bm[3, 3] == Bm[4, 4]
    offdiag_zero = all(Bm[a, b] == 0 for a in range(5) for b in range(5) if a != b)
    diag_ok = diag_ok and pairs_equal and offdiag_zero
    rays[J] = lam
check("5.2 each spin-J channel's symbol at q=z is diagonal in the helicity basis with equal +-m eigenvalues",
      diag_ok, f"(lam0,lam1,lam2): {rays}")
polyrel = all(4 * l[1] - l[2] - 3 * l[0] == 0 for l in rays.values())
check("5.3 locality relation 4*lam1 = lam2 + 3*lam0 (helicity-1 eigenvalue is fixed by the other two) in every channel", polyrel)

# translate to the two local isotropic invariants a1 tr(y^2) q^2 + a2 q y^2 q
a1s, a2s = sp.symbols("a1s a2s")


def lam_from_a(a1, a2):
    vals = []
    for Y in (hel_basis[0], hel_basis[1], hel_basis[3]):
        vals.append((a1 * (Y * Y).trace() + a2 * (zhat.T * Y * Y * zhat)[0]) / (Y * Y).trace())
    return vals


lam_sym = lam_from_a(a1s, a2s)
expected = [a1s + 2 * a2s / 3, a1s + a2s / 2, a1s]
check("5.4 isotropic invariants give (lam0,lam1,lam2) = (a1+2a2/3, a1+a2/2, a1)",
      [sp.simplify(x_ - y_) for x_, y_ in zip(lam_sym, expected)] == [0, 0, 0])
ray_a = {}
for J, lam in rays.items():
    sol_a = sp.solve([sp.Eq(lam_sym[0], lam[0]), sp.Eq(lam_sym[2], lam[2])], [a1s, a2s])
    consistent = sp.simplify(lam_sym[1].subs(sol_a) - lam[1]) == 0
    ray_a[J] = (sol_a[a1s], sol_a[a2s], consistent)
# PSD cone {a1>=0, a1+2a2/3>=0} has extreme rays (0,1) and (1,-3/2): write each ray as s*(0,1)+t*(1,-3/2)
inside = True
for J, (p, q_, cons) in ray_a.items():
    t_c = p
    s_c = q_ + R(3, 2) * t_c
    inside = inside and cons and s_c >= 0 and t_c >= 0
ends = {J: ray_a[J][:2] for J in ray_a}
check("5.5 the Gram cone (spin-channel rays J=1,2,3) equals the PSD cone {a1>=0, a1+2a2/3>=0}: J=1 and J=2 are its two extreme rays, J=3 lies inside",
      ends[1][0] == 0 and ends[1][1] > 0 and ends[2][0] > 0 and sp.simplify(ends[2][1] / ends[2][0] + R(3, 2)) == 0 and inside,
      f"rays (a1,a2): {ends}")

# isotropic stiffness weights via the Pi machinery
def ximat(xi_vec):
    Y = sp.zeros(3)
    for a, (i, j) in enumerate(COMPS):
        if i == j:
            Y[i, i] = xi_vec[a]
        else:
            Y[i, j] = xi_vec[a] / 2
            Y[j, i] = xi_vec[a] / 2
    return Y


xs_ = sp.symbols("w0:6")
Yc = ximat(xs_)
Yt = Yc - Yc.trace() / 3 * sp.eye(3)
Fiso = a1s * (Yt * Yt).trace() * (nx**2 + ny**2 + nz**2) + a2s * (NV.T * Yt * Yt * NV)[0]
Viso = sp.Matrix(6, 6, lambda a, b: sp.expand(sp.diff(Fiso, xs_[a], xs_[b]) / 2))
H1iso = avg(sum(PI_H1[a, b] * Viso[a, b] for a in range(6) for b in range(6)))
TTiso = avg(sum(PI_TT[a, b] * Viso[a, b] for a in range(6) for b in range(6)))
Liso = sp.expand(H1iso - TTiso / 4)
sqiso = sp.expand(R(9, 4) * avg(sum(XI[a] * XI[b] * Viso[a, b] for a in range(6) for b in range(6))))
lam0, lam1, lam2 = expected
check("5.6 isotropic symbol: <H1> = 2*lam1, <TT> = 2*lam2, <H1>-<TT>/4 = (3/2)*lam0 = (9/4)<xi^T V xi>",
      sp.expand(H1iso - 2 * lam1) == 0 and sp.expand(TTiso - 2 * lam2) == 0
      and sp.expand(Liso - R(3, 2) * lam0) == 0 and sp.expand(Liso - sqiso) == 0,
      f"<H1>={H1iso}, <TT>={TTiso}")

# ---------------------------------------------------------------------------
# 6. gauge corollary and isotropic-inertia dispersion consequence (supplied comparator K = kappa * 1)
# ---------------------------------------------------------------------------
# gauge-invariant PSD: lam1 = 0 forces lam0 = lam2 = 0
lamvec = sp.symbols("L0 L1 L2", nonnegative=True)
rel = sp.Eq(4 * lamvec[1], lamvec[2] + 3 * lamvec[0])
l2_sol = sp.solve(rel.subs(lamvec[1], 0), lamvec[2])[0]
check("6.1 isotropic PSD symbol annihilating the helicity-one (pure gauge) tensors: lam1=0 gives lam2 = -3*lam0, so lam0,lam2 >= 0 force lam0=lam2=0 (no TT stiffness at O(q^2))",
      sp.simplify(l2_sol + 3 * lamvec[0]) == 0)
kappa = sp.symbols("kappa", positive=True)
w0s, w1s, w2s = [l / kappa for l in (lam0, lam1, lam2)]
check("6.2 inertia K=kappa*1: omega_1^2 = (3 omega_0^2 + omega_TT^2)/4 exactly; with omega_0^2>=0 this gives omega_1 >= omega_TT/2",
      sp.simplify(4 * w1s - w2s - 3 * w0s) == 0)

# ---------------------------------------------------------------------------
# summary
# ---------------------------------------------------------------------------
npass = sum(RESULTS)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}", flush=True)
print(f"runtime {time.time() - T0:.1f}s", file=sys.stderr, flush=True)
if nfail == 0:
    print("HIT: (scoped, same-family, unrefereed) the angular bound <H1> >= <TT>/4 is an exact perfect-square identity <H1>-<TT>/4 = (9/4)<Y^T V Y>, Y=nn^T-I/3, valid for every positive-semidefinite quadratic tensor symbol (no finite Gram needed), and a positive finite-range symbol with a gapped trace channel and no finite Gram of moves exists (Choi form).")
print("SUMMARY: exact check that the angular helicity-one >= TT/4 bound equals (9/4) times the stiffness on the helicity-zero tensor nn^T-I/3 and therefore holds for every positive-semidefinite quadratic tensor symbol after gapped-sector elimination, with no finite Gram needed, together with an exact positive finite-range symbol (Choi form with a gapped trace) that has no finite Gram of moves.")
sys.exit(0 if nfail == 0 else 1)
