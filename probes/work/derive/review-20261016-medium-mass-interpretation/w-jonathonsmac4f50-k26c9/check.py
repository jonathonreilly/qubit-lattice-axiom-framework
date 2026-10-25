#!/usr/bin/env python3
"""
check.py for J:derive:review-20261016-medium-mass-interpretation:a1

Scope: the finite-layer wave problem behind the strain-induced "mass" inference.
Everything here is a statement about a SUPPLIED comparator model (Fierz-Pauli-type
tensor field with a position-dependent mass term m^2(x) = sigma*mu*rho(x)), not
about the four framework axioms.  Output: one PASS/FAIL line per check, then
TOTAL, then HIT (only if all pass), then SUMMARY.
"""
import sys
import time
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp

T0 = time.time()
RESULTS = []


def rec(ok, label):
    RESULTS.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + label)


# ----------------------------------------------------------------------------
# Section A.  Fierz-Pauli-type operator with m^2(x): parity sectors
# ----------------------------------------------------------------------------
t, x, y, z = sp.symbols("t x y z", real=True)
X = [t, x, y, z]
eta = sp.diag(-1, 1, 1, 1)
m2 = sp.Function("m2")(x)
w, q = sp.symbols("omega q", positive=True)


def fp_residual(h):
    """E_{mn}(h) - m2(x) (h_{mn} - eta_{mn} tr h);  E = linearised Einstein operator
    (overall normalisation chosen so that TT modes obey (box - m2) h = 0)."""
    tr = sum(eta[a, a] * h[a, a] for a in range(4))
    box = lambda f: sum(eta[a, a] * sp.diff(f, X[a], 2) for a in range(4))
    div = [sum(eta[a, a] * sp.diff(h[a, n], X[a]) for a in range(4)) for n in range(4)]
    ddh = sum(eta[a, a] * sp.diff(div[a], X[a]) for a in range(4))
    R = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            R[mu, nu] = (box(h[mu, nu]) - sp.diff(div[nu], X[mu]) - sp.diff(div[mu], X[nu])
                         + sp.diff(tr, X[mu], X[nu]) + eta[mu, nu] * (ddh - box(tr))
                         - m2 * (h[mu, nu] - eta[mu, nu] * tr))
    return R


# A1: y-odd sector (components h_{mu y}, mu in t,x,z; fields independent of y) is Proca(2+1)
Af = sp.Function("A")(t, x, z)
Bf = sp.Function("B")(t, x, z)
Cf = sp.Function("C")(t, x, z)
h_odd = sp.zeros(4, 4)
for (i, f) in ((0, Af), (1, Bf), (3, Cf)):
    h_odd[i, 2] = f
    h_odd[2, i] = f
R_odd = fp_residual(h_odd)
# expected Proca: d^nu F_{nu mu} - m2 V_mu on (t,x,z), V=(A,B,C)
V = {0: Af, 1: Bf, 3: Cf}
Xc = {0: t, 1: x, 3: z}
sg = {0: -1, 1: 1, 3: 1}


def Fm(n, m_):
    return sp.diff(V[m_], Xc[n]) - sp.diff(V[n], Xc[m_])


ok = True
for mu in (0, 1, 3):
    proca = sum(sg[n] * sp.diff(Fm(n, mu), Xc[n]) for n in (0, 1, 3) if n != mu) - m2 * V[mu]
    ok &= sp.simplify(R_odd[mu, 2] - proca) == 0
    ok &= sp.simplify(R_odd[2, mu] - proca) == 0
for (i, j) in [(a, b) for a in range(4) for b in range(4) if a != 2 and b != 2]:
    ok &= sp.simplify(R_odd[i, j]) == 0
ok &= sp.simplify(R_odd[2, 2]) == 0
rec(ok, "A1 (sympy, arbitrary m2(x)): y-odd sector of the Fierz-Pauli-type operator equals Proca d^nu F_{nu mu} - m2(x) V_mu on (t,x,z); every other component vanishes identically")

# A2: first-order form Y'=A(x)Y, Y=(Vt,Vz,Gt,Gz), G=F_{x.}, V_x=-i(w Gt+q Gz)/m2
Vt, Vz, Gt, Gz = [sp.Function(n)(x) for n in ("Vt", "Vz", "Gt", "Gz")]
Vx = -sp.I * (w * Gt + q * Gz) / m2
rhs = {
    Vt: Gt - sp.I * w * Vx,
    Vz: Gz + sp.I * q * Vx,
    Gt: (m2 + q**2) * Vt + q * w * Vz,
    Gz: (m2 - w**2) * Vz - w * q * Vt,
}


def reduce_derivs(e):
    for f in (Vt, Vz, Gt, Gz):
        e = e.subs(sp.Derivative(f, (x, 2)), sp.diff(rhs[f], x))
    for _ in range(2):
        for f in (Vt, Vz, Gt, Gz):
            e = e.subs(sp.Derivative(f, x), rhs[f])
    return e


E_ = sp.exp(-sp.I * w * t + sp.I * q * z)
h_fo = sp.zeros(4, 4)
for (i, f) in ((0, Vt * E_), (1, Vx * E_), (3, Vz * E_)):
    h_fo[i, 2] = f
    h_fo[2, i] = f
R_fo = fp_residual(h_fo)
ok = True
for mu in (0, 1, 3):
    r_ = reduce_derivs(R_fo[mu, 2].doit() / E_)
    ok &= sp.simplify(r_) == 0
rec(ok, "A2 (sympy, arbitrary m2(x)): Y'=A(m2)Y with V_x=-i(w Gt+q Gz)/m2 solves all three Fierz-Pauli odd-sector equations identically")

lam = sp.symbols("lam")
Amat = sp.Matrix([
    [0, 0, 1 - w**2 / m2, -w * q / m2],
    [0, 0, w * q / m2, 1 + q**2 / m2],
    [m2 + q**2, q * w, 0, 0],
    [-w * q, m2 - w**2, 0, 0],
])
# check Amat equals the rhs table
chk = sp.Matrix([[sp.diff(rhs[f], g_) for g_ in (Vt, Vz, Gt, Gz)] for f in (Vt, Vz, Gt, Gz)])
okA = sp.simplify(chk - Amat) == sp.zeros(4, 4)
cp = sp.simplify((lam * sp.eye(4) - Amat).det() - (lam**2 - (m2 + q**2 - w**2)) ** 2)
rec(okA and cp == 0, "A3 (sympy): characteristic polynomial of A(m2) is (lam^2-(m2+q^2-w^2))^2, i.e. two polarizations share k_x^2 = w^2-q^2-m2")

# A4: the s-mode V=(q f,0,-w f) is an exact solution for arbitrary profile m2(x)
f = sp.Function("f")(x)
h_s = sp.zeros(4, 4)
for (i, val) in ((0, q * f * E_), (1, 0), (3, -w * f * E_)):
    h_s[i, 2] = val
    h_s[2, i] = val
R_s = fp_residual(h_s)
wave = sp.diff(f, x, 2) - (q**2 + m2 - w**2) * f
ok = (sp.simplify(R_s[0, 2] / E_ - q * wave) == 0 and sp.simplify(R_s[3, 2] / E_ + w * wave) == 0
      and sp.simplify(R_s[1, 2]) == 0)
rec(ok, "A4 (sympy): V=(q f,0,-w f)e^{-iwt+iqz} (polarization normal to the plane of incidence) solves the full odd sector iff f''=(q^2+m2-w^2)f, for ANY m2(x)")

# A5: junction conditions inherited by the s-mode: Vt,Vz continuous, Gt=Vt', Gz=Vz' continuous <=> f, f' continuous,
# Gauss w Gt + q Gz = w q f' - q w f' = 0 holds identically (so V_x = 0 at every interface)
fp_ = sp.Symbol("fprime")
Gt_s, Gz_s = q * fp_, -w * fp_
rec(sp.simplify(w * Gt_s + q * Gz_s) == 0, "A5 (sympy): s-mode satisfies the interface Gauss condition w Gt + q Gz = 0 (V_x=0 on the massive side) identically; junction = continuity of f and f'")

# A6: helicity-2 closure at normal incidence: EH operator on h_yy=-h_zz=f(t,x), h_yz=g(t,x)
ff = sp.Function("f")(t, x)
gg = sp.Function("g")(t, x)
h2 = sp.zeros(4, 4)
h2[2, 2] = ff
h2[3, 3] = -ff
h2[2, 3] = gg
h2[3, 2] = gg
R2 = fp_residual(h2)
box2 = lambda u: -sp.diff(u, t, 2) + sp.diff(u, x, 2)
ok = (sp.simplify(R2[2, 2] - (box2(ff) - m2 * ff)) == 0 and sp.simplify(R2[3, 3] + (box2(ff) - m2 * ff)) == 0
      and sp.simplify(R2[2, 3] - (box2(gg) - m2 * gg)) == 0)
for (i, j) in [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3)]:
    ok &= sp.simplify(R2[i, j]) == 0
rec(ok, "A6 (sympy): helicity-2 fields (h_yy=-h_zz, h_yz) at q=0 form a closed subsystem; each obeys (box - m2(x)) h = 0 with no other component sourced")

# ----------------------------------------------------------------------------
# Section B.  Even (p) sector: structural facts that fix part of the junction data
# ----------------------------------------------------------------------------
names = {"tt": (0, 0), "tx": (0, 1), "tz": (0, 3), "xx": (1, 1), "xz": (1, 3), "zz": (3, 3), "yy": (2, 2)}
Fe = {}
H_e = sp.zeros(4, 4)
for k_, (i, j) in names.items():
    Fe[k_] = sp.Function("h" + k_)(t, x, z)
    H_e[i, j] = Fe[k_]
    H_e[j, i] = Fe[k_]
R_e = fp_residual(H_e)


def xsec_coeffs(expr):
    """coefficients of second x-derivatives of each even-sector field in expr"""
    out = {}
    for k_, fn in Fe.items():
        c = sp.expand(expr).coeff(sp.Derivative(fn, (x, 2)))
        if c != 0:
            out[k_] = c
    return out


# B1: E_xx - Pi_xx contains no x-derivative of anything and no normal component
exx = sp.expand(R_e[1, 1])
has_x = any(any(v == x for v, c in d.variable_count) for d in exx.atoms(sp.Derivative))
has_normal = any(exx.has(Fe[k_]) for k_ in ("tx", "xz", "xx"))
tr_perp = -Fe["tt"] + Fe["yy"] + Fe["zz"]
S_perp = (sp.diff(Fe["tt"], z, 2) - sp.diff(Fe["yy"], z, 2) + sp.diff(Fe["yy"], t, 2)
          + sp.diff(Fe["zz"], t, 2) - 2 * sp.diff(Fe["tz"], t, z))
ok = (not has_x) and (not has_normal) and sp.simplify(exx - (m2 * tr_perp + S_perp)) == 0
rec(ok, "B1 (sympy): the (x,x) equation is m2(x)*tr_perp(h) + S[h_perp] = 0 with NO x-derivatives and no normal components (tr_perp=-h_tt+h_yy+h_zz)")

# B2: the x'' part of the tangential equations is an invertible matrix on (h_tt,h_yy,h_zz) and h_tz
rows = {}
for nm, (i, j) in (("tt", (0, 0)), ("zz", (3, 3)), ("yy", (2, 2)), ("tz", (0, 3))):
    rows[nm] = xsec_coeffs(R_e[i, j])
Mx = sp.Matrix([[rows[r_].get(c_, 0) for c_ in ("tt", "yy", "zz")] for r_ in ("tt", "zz", "yy")])
ok = (Mx.det() == 2) and rows["tz"] == {"tz": 1}
for nm, (i, j) in (("xx", (1, 1)), ("tx", (0, 1)), ("xz", (1, 3))):
    ok &= xsec_coeffs(R_e[i, j]) == {}
rec(ok, "B2 (sympy): x'' enters only the tangential equations, through an invertible operator (det=2 on tt,yy,zz; unit on tz); the normal equations contain no x''")

# B3: consequence (proved from B1,B2): with a bounded m2 jump at x_i, h_perp must be continuous (else delta' appears),
# so m2_L*tr+S = 0 = m2_R*tr+S forces tr_perp = 0 = S at the interface.  Check the algebra symbolically.
mL, mR, trs, Ss = sp.symbols("mL mR trs Ss")
sol = sp.solve([mL * trs + Ss, mR * trs + Ss], [trs, Ss], dict=True)[0]
rec(sol == {trs: 0, Ss: 0}, "B3 (sympy): two different m2 values with the same continuous (tr_perp,S) force tr_perp=0 and S=0 at the interface")

# ----------------------------------------------------------------------------
# Section C.  Exact slab scattering for the odd sector vs the scalar slab (mpmath, 50 digits)
# ----------------------------------------------------------------------------
mp.mp.dps = 50


def Amat_num(wv, qv, m2v):
    wv, qv, m2v = mp.mpf(wv), mp.mpf(qv), mp.mpf(m2v)
    return mp.matrix([[0, 0, 1 - wv * wv / m2v, -wv * qv / m2v],
                      [0, 0, wv * qv / m2v, 1 + qv * qv / m2v],
                      [m2v + qv * qv, qv * wv, 0, 0],
                      [-wv * qv, m2v - wv * wv, 0, 0]])


def odd_slab(wv, qv, m2v, d):
    """vacuum | slab(m2,d) | vacuum, s-polarisation from the full 4-state Proca slab with the
    junction rules: Vt,Vz,Gt,Gz continuous; vacuum side carries g=f', B=qVt+wVz and Gauss."""
    wv, qv = mp.mpf(wv), mp.mpf(qv)
    kv = mp.sqrt(wv * wv - qv * qv)
    P = mp.expm(Amat_num(wv, qv, m2v) * d)
    n = qv * qv + wv * wv
    M = mp.zeros(6, 6)
    rhs_ = mp.zeros(6, 1)
    M[0, 2], M[0, 3] = wv, qv
    M[1, 2], M[1, 3], M[1, 4] = qv / n, -wv / n, -1
    rhs_[1] = 1
    M[2, 0], M[2, 1], M[2, 4] = qv, wv, 1j * kv
    rhs_[2] = 1j * kv
    for j in range(4):
        M[3, j] = wv * P[2, j] + qv * P[3, j]
        M[4, j] = (qv * P[2, j] - wv * P[3, j]) / n
        M[5, j] = qv * P[0, j] + wv * P[1, j]
    ph = mp.e ** (1j * kv * d)
    M[4, 5] = -ph
    M[5, 5] = -1j * kv * ph
    u = mp.lu_solve(M, rhs_)
    return u[4], u[5], mp.det(M)


def scalar_layers(wv, qv, layers):
    """exact scalar transmission/reflection through piecewise-constant layers [(m2,d),...]
    in vacuum, f''=-(w^2-q^2-m2) f, f and f' continuous.  t is relative to free propagation."""
    wv, qv = mp.mpf(wv), mp.mpf(qv)
    kv = mp.sqrt(wv * wv - qv * qv)
    Mt = mp.eye(2)
    D = mp.mpf(0)
    for (m2v, d) in layers:
        ks = mp.sqrt(wv * wv - qv * qv - m2v + 0j)
        if ks == 0:
            Mj = mp.matrix([[1, d], [0, 1]])
        else:
            Mj = mp.matrix([[mp.cos(ks * d), mp.sin(ks * d) / ks], [-ks * mp.sin(ks * d), mp.cos(ks * d)]])
        Mt = Mj * Mt
        D += d
    Mi = Mt ** -1  # (f,f')(0) = Mi (f,f')(D)
    # unknown r, X=tau e^{i kv D}: (1+r, i kv (1-r)) = Mi (X, i kv X)
    a = Mi[0, 0] + 1j * kv * Mi[0, 1]
    b = Mi[1, 0] + 1j * kv * Mi[1, 1]
    X_ = 2 / (a + b / (1j * kv))
    r_ = X_ * a - 1
    return r_, X_ * mp.e ** (-1j * kv * D)


cases = [(1, 0, "0.7", 3), (1, 0, "-0.7", 3), (1, "0.5", "0.3", 2), (1, "0.5", "-0.3", 2),
         (1, "0.8", -2, "1.5"), (1, "0.8", "0.6", "1.5"), (1, "0.5", 5, 1), (1, "0.3", "2.5", "0.8"),
         (1, "0.95", "-4", "3.3"), ("0.7", "0.6", "0.9", "2.1")]
maxdiff = mp.mpf(0)
maxflux = mp.mpf(0)
mindet = mp.inf
for (wv, qv, m2v, d) in cases:
    wv, qv, m2v, d = mp.mpf(wv), mp.mpf(qv), mp.mpf(m2v), mp.mpf(d)
    r1, t1, det = odd_slab(wv, qv, m2v, d)
    rs, ts = scalar_layers(wv, qv, [(m2v, d)])
    maxdiff = max(maxdiff, abs(t1 - ts), abs(r1 + rs))  # vacuum field g=f' flips the sign of r relative to f
    maxflux = max(maxflux, abs(abs(r1) ** 2 + abs(t1) ** 2 - 1))
    mindet = min(mindet, abs(det))
rec(maxdiff < mp.mpf(10) ** -35, "C1 (mpmath 50 dps): full odd-sector Proca slab (4-state transfer, junction rules of A2/A5) reproduces the scalar slab r,t exactly at 10 incidence/mass/sign points, incl. oblique and evanescent: max|diff|=%s" % mp.nstr(maxdiff, 3))
rec(maxflux < mp.mpf(10) ** -35, "C2 (mpmath): flux conservation |r|^2+|t|^2=1 holds for the Proca slab (independent of the scalar formula): max error %s" % mp.nstr(maxflux, 3))
rec(mindet > mp.mpf(10) ** -6, "C3 (mpmath): the 6x6 matching determinant is nonzero at every tested point (min |det|=%s), so the matched solution is unique there" % mp.nstr(mindet, 3))

# C4: generic scalar-layer solver vs closed-form single slab (disjoint formula)
ok = True
for (wv, qv, m2v, d) in [(1, "0.3", "-1.7", "2.2"), (1, 0, "0.4", 5), ("0.8", "0.2", "-3", "1.1")]:
    wv, qv, m2v, d = mp.mpf(wv), mp.mpf(qv), mp.mpf(m2v), mp.mpf(d)
    kv = mp.sqrt(wv**2 - qv**2)
    ks = mp.sqrt(wv**2 - qv**2 - m2v + 0j)
    t_cf = mp.e ** (-1j * kv * d) / (mp.cos(ks * d) - 1j * (kv**2 + ks**2) / (2 * kv * ks) * mp.sin(ks * d))
    ok &= abs(scalar_layers(wv, qv, [(m2v, d)])[1] - t_cf) < mp.mpf(10) ** -40
rec(ok, "C4 (mpmath): layered scalar solver equals the closed-form slab t = e^{-ikd}/(cos ks d - i(kv^2+ks^2)/(2 kv ks) sin ks d)")

# ----------------------------------------------------------------------------
# Section D.  Sign scope of the dispersion inference (first order)
# ----------------------------------------------------------------------------
eps = sp.symbols("eps")


def sym_t(layers_, kvv, eps_):
    """transmission (relative to free propagation) through layers [(m_j, d_j)] with m2 = eps*m_j; exact rationals in the parameters"""
    Mt_ = sp.eye(2)
    D_ = 0
    for (mj, dj) in layers_:
        ks_ = sp.sqrt(kvv**2 - eps_ * mj)
        Mj = sp.Matrix([[sp.cos(ks_ * dj), sp.sin(ks_ * dj) / ks_], [-ks_ * sp.sin(ks_ * dj), sp.cos(ks_ * dj)]])
        Mt_ = Mj * Mt_
        D_ += dj
    Mi_ = Mt_.inv()
    a_ = Mi_[0, 0] + sp.I * kvv * Mi_[0, 1]
    b_ = Mi_[1, 0] + sp.I * kvv * Mi_[1, 1]
    return 2 / (a_ + b_ / (sp.I * kvv)) * sp.exp(-sp.I * kvv * D_)


R_ = sp.Rational
sets = [([(R_(3, 10), R_(7, 10)), (R_(-1, 5), R_(9, 10))], R_(1)),
        ([(R_(1, 2), R_(3, 2)), (R_(2, 3), R_(1, 4))], R_(3, 4)),
        ([(R_(-2, 5), R_(11, 10)), (R_(1, 7), R_(5, 3))], R_(6, 5))]
okD1 = True
for (lay, kvv) in sets:
    tf = sym_t(lay, kvv, eps)
    t0v = tf.subs(eps, 0)
    d1v = sp.diff(tf, eps).subs(eps, 0)
    expect = -sp.I * sum(mj * dj for mj, dj in lay) / (2 * kvv)
    okD1 &= abs(sp.N(d1v / t0v - expect, 30)) < 1e-25
rec(okD1, "D1 (sympy, exact rational parameters, 3 two-layer sets incl. mixed sign): d ln t/d eps at 0 = -i (m1 d1 + m2 d2)/(2k): first order sees only the SIGNED column integral")

# counterexample: equal and opposite signed columns -> first-order term vanishes, second order does not
okD2 = True
shown = []
for (mu_v, dd_v, kvv) in [(R_(1), R_(7, 10), R_(1)), (R_(1), R_(3, 2), R_(1, 2)), (R_(2), R_(1, 3), R_(9, 10))]:
    tf2 = sym_t([(mu_v, dd_v), (-mu_v, dd_v)], kvv, eps)
    t0v = tf2.subs(eps, 0)
    d1v = sp.N(sp.diff(tf2, eps).subs(eps, 0) / t0v, 30)
    d2v = sp.N(sp.diff(tf2, eps, 2).subs(eps, 0) / t0v, 30)
    okD2 &= abs(d1v) < 1e-25 and abs(d2v) > 1e-6
    shown.append(sp.N(abs(d2v), 4))
rec(okD2, "D2 (sympy, exact rationals): with columns +mu d and -mu d the O(eps) term of t vanishes while the O(eps^2) term is nonzero (|t''/t| = %s)" % ", ".join(str(v) for v in shown))

# numerics: phase/eps -> 0 although the unsigned budget is 2 mu d
wv0, mu0, d0 = mp.mpf(1), mp.mpf(1), mp.mpf("0.7")
vals = []
for e in (mp.mpf("1e-3"), mp.mpf("1e-4")):
    _, tt_ = scalar_layers(wv0, 0, [(e * mu0, d0), (-e * mu0, d0)])
    vals.append(abs(mp.arg(tt_)) / e)
_, tt_ = scalar_layers(wv0, 0, [(mp.mpf("1e-3") * mu0, 2 * d0)])
single = abs(mp.arg(tt_)) / mp.mpf("1e-3")
rec(vals[1] < vals[0] / 5 and vals[1] < mp.mpf("1e-2") * single, "D3 (mpmath): for the +/- pair phase/eps = %s (eps=1e-3), %s (1e-4) -> 0, versus %s for one same-sign layer of equal unsigned budget" % (mp.nstr(vals[0], 3), mp.nstr(vals[1], 3), mp.nstr(single, 3)))

# D4: radius of convergence of the small-mass (1/f) expansion of k=sqrt(w^2-A): |A| < w^2, both signs
Asym, wsym = sp.symbols("A wsym")
ser = sp.series(sp.sqrt(1 - Asym), Asym, 0, 40).removeO()
coeffs = [sp.Rational(ser.coeff(Asym, n)) for n in range(1, 40)]
ratio = abs(coeffs[-1] / coeffs[-2])
rec(abs(float(ratio) - 1.0) < 0.06 and all(c < 0 for c in coeffs), "D4 (sympy): sqrt(1-A) series has all coefficients negative and convergence radius 1 (ratio %.3f at order 39): the 1/f small-mass phase is valid only for |A|<w^2, in the tachyonic sign as well" % float(ratio))

# D5: Earth numbers (Fractions): core mass vs band edge at the quoted bound
hbar_eVs = Fraction("6.582119569e-16")
hbarc_eVm = Fraction("1.973269804e-7")
mu_bound = Fraction("1.5e-29")  # eV^2 m^3/kg, source row 1
rho_core = Fraction(13000)      # kg/m^3, RECALLED PREM-like core density (input, not derived here)
f_lo = Fraction(30)
w_lo = 2 * Fraction(314159265358979, 10**14) * f_lo * hbar_eVs
Mcore2 = mu_bound * rho_core
ratio_Mw = Mcore2 / (w_lo**2)
mu_pert = (w_lo**2) / rho_core
rec(ratio_Mw > 1 and float(mu_pert) < float(mu_bound),
    "D5 (Fractions): at the quoted 1.5e-29 the core has M^2/w^2 = %.1f at 30 Hz (>1, outside the small-mass regime); the 1/f form needs mu <= %.2e (30 Hz, core)" % (float(ratio_Mw), float(mu_pert)))

# ----------------------------------------------------------------------------
# Section E.  Finite-layer resonances (tachyonic sign)
# ----------------------------------------------------------------------------
s_ = sp.symbols("s_", positive=True)
phi_ = sp.symbols("phi_", real=True)
I_pi = sp.integrate(1 / (1 + s_**2 * sp.sin(phi_) ** 2), (phi_, 0, sp.pi))
okI = all(abs(mp.quad(lambda p: 1 / (1 + mp.mpf(sv) ** 2 * mp.sin(p) ** 2), [0, mp.pi]) - mp.pi / mp.sqrt(1 + mp.mpf(sv) ** 2)) < mp.mpf(10) ** -40 for sv in ("0.3333333333", 2, 10, 123))
rec(okI, "E1 (mpmath): over one period of the slab phase, int |t|^2 dphi = pi/sqrt(1+s^2), s=(ks/kv-kv/ks)/2 (exact; the 'period average' 2 kv ks/(kv^2+ks^2))")

# tooth area: q=0, w0=100, M=1000, d=20 (units arbitrary), integrate |t|^2 over one comb period
mp.mp.dps = 30
w0, Mt0, dl = mp.mpf(100), mp.mpf(1000), mp.mpf(20)


def T2(om):
    kv = om
    ks = mp.sqrt(om * om + Mt0**2)
    return 1 / (1 + ((ks * ks - kv * kv) / (2 * kv * ks)) ** 2 * mp.sin(ks * dl) ** 2)


ks0 = mp.sqrt(w0 * w0 + Mt0**2)
n_c = mp.floor(ks0 * dl / mp.pi)
# resonance omega_n: ks(om_n) d = n pi
om_n = mp.sqrt((n_c * mp.pi / dl) ** 2 - Mt0**2)
Dom = mp.pi * ks0 / (w0 * dl)  # comb spacing
lo, hi = om_n - Dom / 2, om_n + Dom / 2
pts = [lo] + [om_n + k_ * mp.mpf("0.05") for k_ in range(-6, 7)] + [hi]
area = mp.quad(T2, pts, maxdegree=10)
pred = (mp.pi * ks0 / (w0 * dl)) * (2 * w0 * ks0 / (w0**2 + ks0**2))
iso = 2 * mp.pi * w0 / (w0 * dl)  # 2 pi kv/(w d) -> 2pi/d at q=0, M>>w
rel = abs(area - pred) / pred
rec(rel < 0.02 and abs(pred - iso) / iso < 0.06,
    "E2 (mpmath): one comb tooth's |t|^2 area = %s (pred %s, 2pi/d limit %s): width ~2/d independent of M" % (mp.nstr(area, 5), mp.nstr(pred, 5), mp.nstr(iso, 5)))
mp.mp.dps = 50

# E3: |t|=1 exactly on the comb, for any M and thickness: omega_n^2 = (n pi/d)^2 - M^2
ok = True
for (Mv, dv, nv) in [(1000, 20, 7000), (mp.mpf("2.5"), mp.mpf(11), 40), (mp.mpf("0.01"), mp.mpf(3), 3)]:
    Mv, dv = mp.mpf(Mv), mp.mpf(dv)
    if (nv * mp.pi / dv) ** 2 > Mv**2:
        omn = mp.sqrt((nv * mp.pi / dv) ** 2 - Mv**2)
        r_, t_ = scalar_layers(omn, 0, [(-Mv**2, dv)])
        ok &= abs(abs(t_) - 1) < mp.mpf(10) ** -35 and abs(r_) < mp.mpf(10) ** -35
rec(ok, "E3 (mpmath): every comb frequency w_n=sqrt((n pi/d)^2-M^2) is perfectly transmitting (|t|=1,r=0), so no single-frequency |t| bound can exclude large tachyonic M")

# E4: Earth-chord numbers (Fractions): comb phase span across 30-1000 Hz at the placeholder, and tooth area in Hz
c_ms = Fraction(299792458)
chord = Fraction("11260.65e3")  # H1 chord of the source (taken from the source note, not re-derived)
M_ph = Fraction("2.36e-9")      # eV, source placeholder in rock
d_nat = chord / hbarc_eVm       # eV^-1
pi_ = Fraction(314159265358979, 10**14)
w_hi = 2 * pi_ * 1000 * hbar_eVs
span = d_nat * (w_hi**2 - w_lo**2) / (2 * M_ph)  # approx ks(w2)-ks(w1) for M>>w
tooth_Hz = c_ms / chord
rec(span < pi_ and 26 < float(tooth_Hz) < 27,
    "E4 (Fractions): at M=2.36e-9 eV the comb phase advance over 30-1000 Hz is %.3f rad < pi (at most one tooth), tooth area c/d = %.1f Hz" % (float(span), float(tooth_Hz)))

# E5: PSD-agnostic bound: with weight w(f)>=0, S^2 = int w|t|^2/int w <= (c/d) w_max/int w df for isolated teeth
# toy illustration of the effective bandwidth with an analytic aLIGO-like fit (RECALLED form; illustration only)
f_arr = np.linspace(30.0, 1000.0, 20000)
xx = f_arr / 215.0
Sn = 1e-49 * (xx ** -4.14 - 5 * xx ** -2 + 111 * (1 - xx**2 + 0.5 * xx**4) / (1 + 0.5 * xx**2))
wts = f_arr ** (-7.0 / 3.0) / Sn
Beff = float(np.sum(0.5 * (wts[1:] + wts[:-1]) * np.diff(f_arr)) / wts.max())
S2max = float(tooth_Hz) / Beff
rec(Beff > 0 and S2max < 1.0,
    "E5 (numpy, toy PSD): effective SNR bandwidth %.1f Hz -> isolated-tooth capture S^2 <= %.2f (PSD-dependent; the bound is (c/d)/B_eff)" % (Beff, S2max))

# ----------------------------------------------------------------------------
# Section F.  Instability scope: plane layer versus bounded body
# ----------------------------------------------------------------------------
def kappa_layer(Mv, dv):
    Mv, dv = mp.mpf(Mv), mp.mpf(dv)
    fcn = lambda kap: mp.sqrt(Mv**2 - kap**2) * mp.tan(mp.sqrt(Mv**2 - kap**2) * dv / 2) - kap
    # root in (0,M): fcn(0+) = M tan(Md/2) > 0 (if Md/2<pi/2), fcn(M-) = -M
    lo_, hi_ = mp.mpf(0), Mv * (1 - mp.mpf(10) ** -30)
    return mp.findroot(fcn, (lo_ + mp.mpf(10) ** -20, hi_), solver="anderson", tol=1e-30, maxsteps=200)


mp.mp.dps = 40
okk = True
for (Mv, dv) in [(1, 2), ("0.3", "1.0"), ("0.01", "1.0"), ("1e-3", "2.0")]:
    kap = kappa_layer(Mv, dv)
    Mv_, dv_ = mp.mpf(Mv), mp.mpf(dv)
    kk = mp.sqrt(Mv_**2 - kap**2)
    okk &= (0 < kap < Mv_) and abs(kk * mp.tan(kk * dv_ / 2) - kap) < mp.mpf(10) ** -25
kap_small = kappa_layer("1e-4", "1.0")
okk &= abs(kap_small / (mp.mpf("1e-4") ** 2 * 1 / 2) - 1) < 1e-3
rec(okk, "F1 (mpmath): a tachyonic plane layer of ANY depth/strength has an even bound state with growth rate kappa in (0,M); kappa -> M^2 d/2 at weak coupling (ratio-1 = %s)" % mp.nstr(kap_small / (mp.mpf("1e-4") ** 2 / 2) - 1, 3))
mp.mp.dps = 50

# F2/F3: disjoint finite-difference check (tridiagonal solver) of kappa^2 as the lowest eigenvalue of -d2/dx2 + q^2 - M^2 theta
from scipy.linalg import eigh_tridiagonal

Mv, dv = 1.0, 2.0
kap = float(kappa_layer(Mv, dv))


def lowest_ev(h_, qq_=0.0, Lbox=40.0):
    n_ = int(round(2 * Lbox / h_)) + 1
    xs = np.linspace(-Lbox, Lbox, n_)
    hh = xs[1] - xs[0]
    V = np.where(np.abs(xs) < dv / 2 - 1e-12, -Mv**2, 0.0) + np.where(np.abs(np.abs(xs) - dv / 2) < 1e-9, -Mv**2 / 2, 0.0) + qq_**2
    dg = 2.0 / hh**2 + V
    of = -np.ones(n_ - 1) / hh**2
    return eigh_tridiagonal(dg, of, select="i", select_range=(0, 0))[0][0]


errs = [abs(lowest_ev(h_) + kap**2) for h_ in (0.02, 0.01, 0.005)]
rec(errs[2] < errs[1] < errs[0] and errs[2] < 1e-3 * kap**2,
    "F2 (scipy tridiagonal finite difference, disjoint): lowest eigenvalue converges to -kappa^2=%.6f for M=1,d=2 (errors %.1e, %.1e, %.1e at h=0.02,0.01,0.005)" % (-kap**2, errs[0], errs[1], errs[2]))

# F3: with transverse wavenumber q the lowest mode has Gamma^2 = kappa^2 - q^2
qq = 0.3
ev_q = lowest_ev(0.005, qq)
rec(abs(ev_q - (qq**2 - kap**2)) < 1e-3 * kap**2 and (qq**2 - kap**2) < 0,
    "F3 (scipy): with q=0.3 the lowest mode has Gamma^2 = kappa^2 - q^2 = %.5f (numerical %.5f): a body of transverse size L (q>=pi/L) is unstable only above a threshold" % (kap**2 - qq**2, -ev_q))

# F4: uniform ball l=0 threshold M R = pi/2 (u=sin Mr inside, u'(R)=0 at Gamma=0), vs source 'pi/2 rule'
Rsym, Msym = sp.symbols("R M", positive=True)
r_sym = sp.symbols("r", positive=True)
u = sp.sin(Msym * r_sym)
thr = sp.solve(sp.Eq(sp.diff(u, r_sym).subs(r_sym, Rsym), 0), Msym)
M_sph = sp.pi / (2 * Rsym)
rec(any(sp.simplify(s_th - M_sph) == 0 for s_th in thr), "F4 (sympy): uniform ball l=0 zero-energy threshold is M R = pi/2 (matches the source's pi/2 rule); a plane layer has none -> the 1D estimate cannot supply an instability threshold")

# ----------------------------------------------------------------------------
# Section G.  One-sided limits and hot-era scaling
# ----------------------------------------------------------------------------
mp.mp.dps = 30
Phi = lambda v: mp.ncdf(v)


def upper_bound(ahat, sig=1.0, cl=0.9):
    # flat prior on A>=0, Gaussian likelihood N(A; ahat, sig)
    Z = 1 - Phi((0 - ahat) / sig)
    return mp.findroot(lambda u_: (Phi((u_ - ahat) / sig) - Phi((0 - ahat) / sig)) / Z - cl, 2.0)


def lower_bound(ahat, sig=1.0, cl=0.9):
    # flat prior on A<=0
    Z = Phi((0 - ahat) / sig)
    return mp.findroot(lambda l_: (Z - Phi((l_ - ahat) / sig)) / Z - cl, -2.0)


up0, lo0 = upper_bound(0.0), lower_bound(0.0)
up1, lo1 = upper_bound(1.0), lower_bound(1.0)
rec(abs(up0 + lo0) < 1e-20 and abs(up1 + lo1) > 0.5, "G1 (mpmath, toy Gaussian): one-sided 90%% bounds are mirror images only for a null measurement (%.3f vs %.3f); for a measured offset of 1 sigma they differ (%.3f vs %.3f)" % (up0, -lo0, up1, -lo1))
mp.mp.dps = 50

# G2: exact hot-era super-horizon exponents when m^2 = A H^2
Ap, tt_ = sp.symbols("A tt", positive=True)
pp = sp.Symbol("p")
hrad = tt_**pp
ode_rad = sp.diff(hrad, tt_, 2) + sp.Rational(3, 2) / tt_ * sp.diff(hrad, tt_) + Ap / (4 * tt_**2) * hrad
pol_rad = sp.simplify(ode_rad / hrad * tt_**2)
roots_rad = sp.solve(sp.Eq(pol_rad, 0), pp)
hmat = tt_**pp
ode_mat = sp.diff(hmat, tt_, 2) + 2 / tt_ * sp.diff(hmat, tt_) + 4 * Ap / (9 * tt_**2) * hmat
roots_mat = sp.solve(sp.Eq(sp.simplify(ode_mat / hmat * tt_**2), 0), pp)
re_rad = [sp.simplify(sp.re(r_.subs(Ap, 3))) for r_ in roots_rad]
re_mat = [sp.simplify(sp.re(r_.subs(Ap, 3))) for r_ in roots_mat]
rec(all(r_ == sp.Rational(-1, 4) for r_ in re_rad) and all(r_ == sp.Rational(-1, 2) for r_ in re_mat),
    "G2 (sympy): for m^2=A H^2, super-horizon tensors go as t^{-1/4}=a^{-1/2} (radiation, A>1/4) and t^{-1/2}=a^{-3/4} (matter, A>9/16), independent of A -- not the constant-mass a^{-3/2}")

N_rad = mp.log(mp.mpf("1.5e11") / mp.mpf("0.8"))
N_mat = mp.log(mp.mpf(3400))
src_exponent = mp.mpf(3) / 2 * (N_rad + N_mat)
corr_exponent = mp.mpf(1) / 2 * N_rad + mp.mpf(3) / 4 * N_mat
rec(abs(src_exponent - 51) < 0.7 and corr_exponent < 20 and corr_exponent > 17,
    "G3 (mpmath arithmetic): 150 GeV->today, a^{-3/2} over %.1f e-folds gives e^-%.1f (the source figure); the exact exponents give e^-%.1f -- conclusion 'r~0' unchanged, magnitude changed" % (N_rad + N_mat, src_exponent, corr_exponent))

# ----------------------------------------------------------------------------
# Totals
# ----------------------------------------------------------------------------
npass = sum(RESULTS)
nfail = len(RESULTS) - npass
print("TOTAL: PASS=%d FAIL=%d" % (npass, nfail))
if nfail == 0:
    print("HIT: scoped result (supplied Fierz-Pauli-type comparator, unrefereed) -- the 1D scalar layer model is exact for the polarization normal to the plane of incidence at every angle and for both helicity-2 polarizations at normal incidence; the in-plane polarization at oblique incidence is the only unreduced channel (interface constraint tr_perp=0 derived, matching not completed); tachyonic finite-layer teeth have M-independent area c/d; a plane tachyonic layer is unstable at any strength, so a 1D estimate gives no instability threshold")
print("SUMMARY: exact scope of the 1D layer model for the medium-mass inference -- exact for s-polarization and normal incidence, open for oblique p-polarization; sign, resonance, instability and hot-era-exponent limits stated with checks (runtime %.1f s)." % (time.time() - T0))
sys.exit(0 if nfail == 0 else 1)
