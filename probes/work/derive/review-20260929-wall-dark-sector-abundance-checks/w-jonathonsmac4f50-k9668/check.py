#!/usr/bin/env python3
"""J:derive:review-20260929-wall-dark-sector-abundance-checks:a1

One obligation: dark-sector-alone accounting.  (A) exact charge census of the
eight-state taste cube in the base x fibre embedding; (B) an independent
derivation of the s-wave Coulomb (Sommerfeld) normalisation under an explicit
velocity convention; (C) propagation of that normalisation through the supplied
Kolb-Turner freeze-out formula and through a Boltzmann equation, with every
cosmological / thermal / coupling / mass premise written down as a constant
below.

Machinery is disjoint from the landed scripts (scripts/dm_dark_candidate_
consistency_check.py, scripts/dm_sommerfeld_kernel_radial_schrodinger_
verification.py): sympy exact algebra for A; Gamma/Kummer functions in mpmath
and sympy for B; a Radau Boltzmann solver with its own K_2 equilibrium for C.

Same-family check by its author, not an independent referee.
"""
import math
import sys
import time

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
from scipy.special import kve

T_START = time.time()
PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if cond else "FAIL ") + name + ((" | " + detail) if detail else ""))
    return cond


# ----------------------------------------------------------------------------
# PART A.  Exact charge census (sympy, exact radicals / rationals)
# ----------------------------------------------------------------------------
R2, R3 = sp.sqrt(2), sp.sqrt(3)


def kron(a, b):
    ra, ca = a.shape
    rb, cb = b.shape
    m = sp.zeros(ra * rb, ca * cb)
    for i in range(ra):
        for j in range(ca):
            m[i * rb:(i + 1) * rb, j * cb:(j + 1) * cb] = a[i, j] * b
    return m


def zero(M):
    return all(sp.simplify(e) == 0 for e in M)


def comm(a, b):
    return a * b - b * a


I2 = sp.eye(2)
I4 = sp.eye(4)
sx = sp.Matrix([[0, 1], [1, 0]]) / 2
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]) / 2
sz = sp.Matrix([[1, 0], [0, -1]]) / 2

# Gell-Mann matrices, exact
lam = [None] * 8
lam[0] = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
lam[1] = sp.Matrix([[0, -sp.I, 0], [sp.I, 0, 0], [0, 0, 0]])
lam[2] = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
lam[3] = sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
lam[4] = sp.Matrix([[0, 0, -sp.I], [0, 0, 0], [sp.I, 0, 0]])
lam[5] = sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
lam[6] = sp.Matrix([[0, 0, 0], [0, 0, -sp.I], [0, sp.I, 0]])
lam[7] = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / R3

# base C^4 basis |b1 b2>, index 2*b1+b2: symmetric triplet e1,e2,e3 and antisymmetric a
e1 = sp.Matrix([1, 0, 0, 0])
e2 = sp.Matrix([0, 1, 1, 0]) / R2
e3 = sp.Matrix([0, 0, 0, 1])
ea = sp.Matrix([0, 1, -1, 0]) / R2
SYM = sp.Matrix.hstack(e1, e2, e3)  # 4 x 3
P_sym = SYM * SYM.T
P_anti = ea * ea.T


def build_embedding():
    """ordering (base1, base2, fibre): index 4 b1 + 2 b2 + b3"""
    T = [kron(SYM * (l / 2) * SYM.T, I2) for l in lam]
    J = [kron(I4, s) for s in (sx, sy, sz)]
    Y = kron(P_sym / 3 - P_anti, I2)
    return T, J, Y


T, J, Y = build_embedding()
C3 = sum((t * t for t in T), sp.zeros(8, 8))
C2 = sum((j * j for j in J), sp.zeros(8, 8))
Psym8 = kron(P_sym, I2)
Panti8 = kron(P_anti, I2)

check("A1 su(3), su(2), Y mutually commute (exact)",
      all(zero(comm(t, j)) for t in T for j in J) and all(zero(comm(t, Y)) for t in T)
      and all(zero(comm(j, Y)) for j in J))
check("A1b generators close: [J1,J2]=iJ3 and [T1,T2]=iT3 (exact)",
      zero(comm(J[0], J[1]) - sp.I * J[2]) and zero(comm(T[0], T[1]) - sp.I * T[2]))
check("A1c Tr Y = 0 and Tr(Y) split 6*(1/3)+2*(-1) (exact)", sp.simplify(Y.trace()) == 0)
check("A2 C_3 = (4/3) P_sym x 1 and C_2 = (3/4) 1 on all of C^8 (exact matrix identity)",
      zero(C3 - sp.Rational(4, 3) * Psym8) and zero(C2 - sp.Rational(3, 4) * sp.eye(8)))
# a vector invariant under su(3)+su(2) would satisfy C_2 v = 0; C_2 = 3/4 * 1 forbids it
check("A3 no gauge singlet exists: C_2 has the single eigenvalue 3/4 > 0 (so ker = {0})",
      set(C2.eigenvals().keys()) == {sp.Rational(3, 4)})

# rational version: basis (e1,e2,e3,a) x (up,down); matrix units generate sl(3), sigma_{+-,z} generate sl(2)
def Eij(n, i, j):
    m = sp.zeros(n, n)
    m[i, j] = 1
    return m


gens_rat = []
for i in range(3):
    for j in range(3):
        if i != j:
            gens_rat.append(kron(Eij(4, i, j), I2))
gens_rat.append(kron(Eij(4, 0, 0) - Eij(4, 1, 1), I2))
gens_rat.append(kron(Eij(4, 1, 1) - Eij(4, 2, 2), I2))
for m_ in (Eij(2, 0, 1), Eij(2, 1, 0), Eij(2, 0, 0) - Eij(2, 1, 1)):
    gens_rat.append(kron(I4, m_))
stack = sp.Matrix.vstack(*gens_rat)
check("A4 rational basis: stacked generators have rank 8 (joint null space of G x S is {0})",
      stack.rank() == 8, f"rank={stack.rank()}")
xs = sp.symbols("x0:64")
X = sp.Matrix(8, 8, xs)
rows = []
for g in gens_rat:
    rows.extend(list(comm(g, X)))
Amat = sp.Matrix([[sp.diff(r, v) for v in xs] for r in rows])
ns = Amat.nullspace()
check("A5 Schur: commutant of su(3) x su(2) in M_8 has dimension 2 (= span{P_sym x 1, P_anti x 1})",
      len(ns) == 2, f"dim={len(ns)}")
a_, b_ = sp.symbols("a b")
Ygen = a_ * Psym8 + b_ * Panti8
sol = sp.solve(sp.Eq(Ygen.trace(), 0), b_)
check("A6 tracelessness fixes Y up to scale: b = -3a, so a = 1/3 gives the embedding's Y = diag(1/3 on quarks, -1 on leptons)",
      sol == [-3 * a_] and zero(Ygen.subs(b_, -3 * a_).subs(a_, sp.Rational(1, 3)) - Y))

# electric charge Q = T3 + Y/2 (T3 = J3), exact spectrum
Q = J[2] + Y / 2
qv = Q.eigenvals()
check("A7 charges Q = T3 + Y/2: {2/3 x3, -1/3 x3, 0 x1, -1 x1}",
      qv == {sp.Rational(2, 3): 3, sp.Rational(-1, 3): 3, 0: 1, -1: 1}, str(qv))
nu_vecs = Q.nullspace()
nu = nu_vecs[0]
nu = nu / sp.sqrt((nu.H * nu)[0])
chars = tuple(sp.simplify((nu.H * M * nu)[0]) for M in (C3, C2, Y))
check("A8 the Q=0 eigenspace is 1-dim and its state has (C_3, C_2, Y) = (0, 3/4, -1): the electrically neutral colour-singlet is "
      "the T3=+1/2 member of a weak doublet, not a gauge singlet (exact)",
      len(nu_vecs) == 1 and chars == (0, sp.Rational(3, 4), -1), str(chars))


def lab_ops_for_axis(axis):
    """conjugate the (base1, base2, fibre) operators to the lab ordering with `axis` as fibre qubit"""
    others = [i for i in range(3) if i != axis]
    perm = sp.zeros(8, 8)  # |base1 base2 fibre> -> |lab>
    for b1 in range(2):
        for b2 in range(2):
            for bf in range(2):
                lab = [0, 0, 0]
                lab[others[0]], lab[others[1]], lab[axis] = b1, b2, bf
                perm[4 * lab[0] + 2 * lab[1] + lab[2], 4 * b1 + 2 * b2 + bf] = 1
    return perm


ok_axes = True
detail = []
for axis in range(3):
    Pm = lab_ops_for_axis(axis)
    Tl = [Pm * t * Pm.T for t in T]
    Jl = [Pm * j * Pm.T for j in J]
    Yl = Pm * Y * Pm.T
    C3l = sum((t * t for t in Tl), sp.zeros(8, 8))
    C2l = sum((j * j for j in Jl), sp.zeros(8, 8))
    for lab_idx, name in ((0, "000"), (7, "111")):
        v = sp.zeros(8, 1)
        v[lab_idx] = 1
        trip = ((v.T * C3l * v)[0], (v.T * C2l * v)[0], (v.T * Yl * v)[0])
        trip = tuple(sp.nsimplify(sp.simplify(t)) for t in trip)
        detail.append((axis, name, trip))
        ok_axes &= trip == (sp.Rational(4, 3), sp.Rational(3, 4), sp.Rational(1, 3))
    ok_axes &= zero(C2l - sp.Rational(3, 4) * sp.eye(8))
check("A9 for each of the 3 choices of weak-fibre qubit, |000> and |111> have (C_3,C_2,Y)=(4/3,3/4,1/3) exactly "
      "(READING: axis permutation is a relabelling, so this cannot fail; it is not a discriminating test)", ok_axes)

# counter-embedding (kill-check observation): same C^8, same su(3), weak su(2)' acting only on the symmetric-base sector
Jp = [kron(P_sym, s) for s in (sx, sy, sz)]
C2p = sum((j * j for j in Jp), sp.zeros(8, 8))
ok = all(zero(comm(Jp[0], Jp[1]) - sp.I * Jp[2]) for _ in [0]) and all(zero(comm(t, j)) for t in T for j in Jp)
sing = (C3 + C2p)
ev = sing.eigenvals()
check("A10 counter-embedding: su(2)' = P_sym x spin on the same C^8 is a valid su(2) commuting with su(3); "
      "C_3 + C_2' has eigenvalue 0 with multiplicity 2, i.e. two true SU(3) x SU(2)' singlets",
      ok and ev.get(0, 0) == 2, str(ev))
# hypercharge on that content: Y' commuting, traceless, quark value a, singlet values c,d => 6a + c + d = 0
a_, c_, d_ = sp.symbols("a c d")
check("A11 in the counter-embedding both singlets can be Y-neutral only if the quark hypercharge is 0 "
      "(6a + c + d = 0 with c=d=0 gives a=0); with a = 1/3 the singlet charges satisfy c + d = -2",
      sp.solve(sp.Eq(6 * a_ + 0 + 0, 0), a_) == [0] and sp.solve(sp.Eq(6 * sp.Rational(1, 3) + c_ + d_, 0), d_) == [-2 - c_])

# ----------------------------------------------------------------------------
# PART B.  Coulomb (Sommerfeld) normalisation, independent derivation
# ----------------------------------------------------------------------------
mp.mp.dps = 50
PI = mp.pi


def S_exact(eta):  # attractive eta = alpha / v_rel > 0 ; repulsive eta < 0
    y = 2 * PI * eta
    if abs(y) < mp.mpf("1e-40"):
        return mp.mpf(1)
    return y / (1 - mp.e ** (-y))


# B1: Gamow factor from the Gamma function: C_0^2(eta_C) = e^{-pi eta_C} |Gamma(1+i eta_C)|^2 = 2 pi eta_C/(e^{2 pi eta_C}-1)
ok = True
for etaC in ("0.05", "0.3", "1", "2.5", "7"):
    e = mp.mpf(etaC)
    lhs = mp.e ** (-PI * e) * abs(mp.gamma(1 + 1j * e)) ** 2
    rhs = 2 * PI * e / (mp.e ** (2 * PI * e) - 1)
    ok &= abs(lhs - rhs) < mp.mpf("1e-40")
check("B1 Gamow factor: e^{-pi eta}|Gamma(1+i eta)|^2 = 2 pi eta/(e^{2 pi eta}-1) to 1e-40", ok)

# B2: regular solution of u'' + (1 + 2 eta/r) u = 0 (k=1; eta = mu alpha / k = alpha/v_rel, attractive) via Kummer
def u_reg(r, eta):
    return mp.re(r * mp.e ** (-1j * r) * mp.hyp1f1(1 + 1j * eta, 2, 2j * r))


def residual(eta, r):
    d2 = mp.diff(lambda t: u_reg(t, eta), r, 2)
    return d2 + (1 + 2 * eta / r) * u_reg(r, eta)


mp.mp.dps = 30
ok_res = all(abs(residual(mp.mpf(e), mp.mpf(r))) < mp.mpf("1e-18") for e in ("0.4", "2") for r in ("0.7", "3.1", "9"))
slope0 = mp.diff(lambda t: u_reg(t, mp.mpf("0.9")), mp.mpf("1e-12"))
check("B2a Kummer form r e^{-ir} 1F1(1+i eta;2;2ir) solves u''+(1+2 eta/r)u=0 and has u'(0)=1",
      ok_res and abs(slope0 - 1) < mp.mpf("1e-9"))
ok_amp = True
amps = []
for etaS in ("0.1", "0.5", "1", "2"):
    eta = mp.mpf(etaS)
    vals = []
    for R in (400, 800, 1600):
        R = mp.mpf(R)
        u = u_reg(R, eta)
        up = mp.diff(lambda t: u_reg(t, eta), R)
        kap = mp.sqrt(1 + 2 * eta / R)
        vals.append(u * u * kap + up * up / kap)  # WKB invariant, free value 1 (k=1, u'(0)=1)
    # Richardson in 1/R^2 (invariant is even in 1/R at leading order)
    inv = (4 * vals[2] - vals[1]) / 3
    S_num = 1 / inv
    err = abs(S_num / S_exact(eta) - 1)
    amps.append(float(err))
    ok_amp &= err < mp.mpf("1e-5")
check("B2b |psi(0)|^2/|psi_free(0)|^2 from the Kummer solution's asymptotic amplitude equals 2 pi eta/(1-e^{-2 pi eta}) "
      "(eta=alpha/v_rel, k=mu v_rel) to 1e-5", ok_amp, "rel errors " + ", ".join(f"{a:.1e}" for a in amps))

# B3: velocity-convention table, symbolic
al, v, beta = sp.symbols("alpha v beta", positive=True)
S_rel = lambda a, vr: (2 * sp.pi * a / vr) / (1 - sp.exp(-2 * sp.pi * a / vr))   # alpha / v_rel convention
S_cm = lambda a, b: (sp.pi * a / b) / (1 - sp.exp(-sp.pi * a / b))               # textbook: per-particle CM speed beta
S_old = lambda a, vr: (sp.pi * a / vr) / (1 - sp.exp(-sp.pi * a / vr))           # archived lane form, v_rel in weight
check("B3a convention identity: S_cm(alpha, beta = v_rel/2) == S_rel(alpha, v_rel) (symbolic)",
      sp.simplify(S_cm(al, v / 2) - S_rel(al, v)) == 0)
check("B3b archived lane form with v = v_rel equals the correct kernel at HALF the coupling: S_old(alpha,v) == S_rel(alpha/2,v) (symbolic)",
      sp.simplify(S_old(al, v) - S_rel(al / 2, v)) == 0)
check("B3c reduced mass: mu = m/2, k = mu v_rel, Bohr momentum mu alpha, eta = mu alpha/k = alpha/v_rel (symbolic)",
      sp.simplify((sp.Symbol("m", positive=True) / 2 * al) / (sp.Symbol("m", positive=True) / 2 * v) - al / v) == 0)

# B4: Maxwell-Boltzmann relative speed.  each component of v1,v2 has variance T/m; v1-v2 has variance 2T/m
x_, vv, uu = sp.symbols("x v u", positive=True)
pdf = 4 * sp.pi * vv ** 2 * (x_ / (4 * sp.pi)) ** sp.Rational(3, 2) * sp.exp(-x_ * vv ** 2 / 4)
norm = sp.integrate(pdf, (vv, 0, sp.oo))
mean_v2 = sp.integrate(pdf * vv ** 2, (vv, 0, sp.oo))
check("B4a relative-speed density 4 pi v^2 (x/4pi)^{3/2} e^{-x v^2/4} is normalised and has <v^2> = 6/x (x = m/T) (symbolic)",
      sp.simplify(norm) == 1 and sp.simplify(mean_v2 - 6 / x_) == 0)
pdf_u = sp.simplify(pdf.subs(vv, 2 * uu) * 2)
check("B4b in the per-particle CM speed u = v_rel/2 the weight is u^2 e^{-x u^2}: the density transforms to "
      "4 pi u^2 (x/pi)^{3/2} e^{-x u^2} (symbolic)",
      sp.simplify(pdf_u - 4 * sp.pi * uu ** 2 * (x_ / sp.pi) ** sp.Rational(3, 2) * sp.exp(-x_ * uu ** 2)) == 0)

# B5: thermal averages in the two consistent conventions agree; wrong pairing equals half coupling
mp.mp.dps = 25


def Sbar_rel(alpha, x, form="rel"):
    alpha = mp.mpf(alpha)
    x = mp.mpf(x)
    if form == "rel":
        f = lambda t: t * t * mp.e ** (-t * t / 4) * S_exact(alpha * mp.sqrt(x) / t)
    else:  # archived: pi-form with v_rel in the relative weight
        f = lambda t: t * t * mp.e ** (-t * t / 4) * (lambda y: y / (1 - mp.e ** (-y)))(PI * alpha * mp.sqrt(x) / t)
    return mp.quad(f, [0, 1, 4, 10, 40, 120]) / (2 * mp.sqrt(PI))


def Sbar_cm(alpha, x):
    alpha = mp.mpf(alpha)
    x = mp.mpf(x)
    # weight u^2 e^{-x u^2}, per-particle speed u; S = pi alpha/u form
    f = lambda t: t * t * mp.e ** (-t * t) * (lambda y: y / (1 - mp.e ** (-y)))(PI * alpha * mp.sqrt(x) / t)
    return mp.quad(f, [0, 0.5, 2, 5, 20, 60]) / (mp.sqrt(PI) / 4)


ALPHA_LM = 1 / (4 * float(mp.pi) * 0.5934 ** 0.25)  # canonical plaquette 0.5934, g_bare = 1 (supplied, not derived)
sb_rel = Sbar_rel(ALPHA_LM, 25)
sb_cm = Sbar_cm(ALPHA_LM, 25)
sb_old = Sbar_rel(ALPHA_LM, 25, "old")
sb_half = Sbar_rel(ALPHA_LM / 2, 25)
check("B5a <S> at x=25, alpha=alpha_LM: relative-speed convention == CM-speed convention (25 digits agree to 1e-15)",
      abs(sb_rel - sb_cm) < mp.mpf("1e-15"), f"<S>={mp.nstr(sb_rel, 12)}")
check("B5b archived pairing (pi-form with relative-speed weight) equals the correct <S> at alpha/2 (to 1e-15)",
      abs(sb_old - sb_half) < mp.mpf("1e-15"), f"archived={mp.nstr(sb_old, 10)} correct={mp.nstr(sb_rel, 10)}")
big = Sbar_rel(ALPHA_LM, 1e12)
check("B5c large-x limit <S> -> 2 sqrt(pi) alpha sqrt(x) (1/v enhancement law) within 1e-5 at x=1e12",
      abs(big / (2 * mp.sqrt(PI) * ALPHA_LM * mp.sqrt(mp.mpf(1e12))) - 1) < mp.mpf("1e-5"))

# ----------------------------------------------------------------------------
# PART C.  Freeze-out propagation.   Premises are the constants below.
# ----------------------------------------------------------------------------
MPL = 1.2209e19            # GeV  (scale_reference_primitive; non-reduced Planck mass as in the lane)
GSTAR = 106.75             # SM above the top threshold, held constant (assumption)
KT_K = 1.07e9              # GeV^-1 Kolb-Turner constant as supplied in the bypass note
XF = 25.0                  # supplied freeze-out coefficient
V_EW = 246.28              # GeV (supplied by the lane)
M_DM = 16 * V_EW           # supplied candidate mass
PI_F = math.pi
KB_EV = 8.617333262e-5     # eV/K
T0_GEV = 2.7255 * KB_EV * 1e-9
GS0 = 3.909                # g_*s today
HBARC_CM = 1.973269804e-14 # GeV cm
S0 = (2 * PI_F ** 2 / 45) * GS0 * T0_GEV ** 3 / HBARC_CM ** 3   # cm^-3
RHOC_H2 = 1.05367e-5       # GeV cm^-3 (critical density / h^2)
OMEGA_OBS = 0.1200         # Planck 2018 comparator, external, not re-fetched


def Sf(y):
    if abs(y) < 1e-12:
        return 1.0
    if y < -700:
        return 0.0
    return y / (-math.expm1(-y))


def Sbar_fast(alpha, x, factor=2 * PI_F):
    f = lambda t: t * t * math.exp(-t * t / 4) * Sf(factor * alpha * math.sqrt(x) / t)
    return quad(f, 0, 70, limit=400, epsabs=0, epsrel=1e-12, points=[1, 5, 12])[0] / (2 * math.sqrt(PI_F))


chk = Sbar_fast(ALPHA_LM, 25.0)
check("C0 scipy thermal average used in the ODE equals the mpmath one of Part B (1e-10)",
      abs(chk - float(sb_rel)) < 1e-10, f"{chk:.12f}")


def KT_omega(m, alpha, sbar=1.0, dirac=False):
    sigma = PI_F * alpha ** 2 / m ** 2 * sbar
    om = KT_K * XF / (math.sqrt(GSTAR) * MPL * sigma)
    return om * (2 if dirac else 1)


om_lane = KT_omega(M_DM, ALPHA_LM)
check("C1 supplied Kolb-Turner formula at (16 v, alpha_LM, S=1, self-conjugate counting) gives 0.1275 (as in the bypass note)",
      abs(om_lane - 0.1275) < 5e-4, f"{om_lane:.5f}")

XS = np.geomspace(1.0, 1e8, 420)
_sb_cache = {}


def spline_sbar(alpha, factor):
    key = (alpha, factor)
    if key not in _sb_cache:
        vals = np.array([Sbar_fast(alpha, x, factor) for x in XS]) if alpha != 0 else np.ones_like(XS)
        _sb_cache[key] = CubicSpline(np.log(XS), vals)
    return _sb_cache[key]


def boltzmann(m, alpha, with_S, factor=2 * PI_F, g=2, gstar=GSTAR, snaps=(1e3, 1e4, 1e6, 1e8)):
    """dY/dx = -(Lambda <sigma v>/x^2)(Y^2 - Yeq^2), T_chi = T, radiation domination, constant g_*.
    returns Y(x) at snapshots (per-species yield)."""
    Lam = (2 * PI_F ** 2 / 45) * gstar * m * MPL / math.sqrt(4 * PI_F ** 3 * gstar / 45)
    sig0 = PI_F * alpha ** 2 / m ** 2
    spl = spline_sbar(alpha, factor) if with_S else None

    def yeq(x):
        return 45 * g / (4 * PI_F ** 4 * gstar) * x * x * kve(2, x) * math.exp(-x)

    def rhs(x, y):
        s = float(spl(math.log(x))) if with_S else 1.0
        return [-Lam * sig0 * s / x ** 2 * (y[0] ** 2 - yeq(x) ** 2)]

    x0 = 3.0
    sol = solve_ivp(rhs, [x0, max(snaps)], [yeq(x0)], method="Radau", rtol=1e-11, atol=1e-40,
                    t_eval=sorted(snaps))
    ys = dict(zip(sol.t, sol.y[0]))
    # freeze-out point: first x where Y > 1.5 Yeq  (diagnostic only)
    return ys, Lam, sig0


def omega_from_Y(m, Y, dirac):
    return (2 if dirac else 1) * m * Y * S0 / RHOC_H2


ys1, _, _ = boltzmann(M_DM, ALPHA_LM, False)
om_ode_S1 = omega_from_Y(M_DM, ys1[1e8], False)
check("C2 Boltzmann solve with S=1, self-conjugate counting gives Omega h^2 within 3% of the Kolb-Turner closed form "
      "(validates the solver against the supplied model)",
      abs(om_ode_S1 / om_lane - 1) < 0.03, f"ODE={om_ode_S1:.5f} KT={om_lane:.5f}")
# two-species check of the Dirac reduction: dY1/dx = -L(Y1 Y2 - Yeq^2)/x^2, dY2/dx = same, Y1(3)=Y2(3)=Yeq
def two_species(m, alpha, xmax=1e3):
    Lam = (2 * PI_F ** 2 / 45) * GSTAR * m * MPL / math.sqrt(4 * PI_F ** 3 * GSTAR / 45)
    sig0 = PI_F * alpha ** 2 / m ** 2
    yeq = lambda x: 45 * 2 / (4 * PI_F ** 4 * GSTAR) * x * x * kve(2, x) * math.exp(-x)
    def rhs(x, y):
        r = -Lam * sig0 / x ** 2 * (y[0] * y[1] - yeq(x) ** 2)
        return [r, r]
    sol = solve_ivp(rhs, [3.0, xmax], [yeq(3.0)] * 2, method="Radau", rtol=1e-11, atol=1e-40)
    return sol.y[0, -1], sol.y[1, -1]


y1, y2 = two_species(M_DM, ALPHA_LM, 1e8)
om_two = m_total = M_DM * (y1 + y2) * S0 / RHOC_H2
check("C3 counting: two-species (chi, chibar) solve with n_chi = n_chibar gives total Omega = 2 x the one-species result "
      "(S=1, same sigma v; PROVED by the symmetric reduction, CHECKED numerically)",
      abs(y1 / y2 - 1) < 1e-9 and abs(om_two / (2 * om_ode_S1) - 1) < 1e-6, f"{om_two:.5f} vs {2 * om_ode_S1:.5f}")

ys_c, _, _ = boltzmann(M_DM, ALPHA_LM, True, 2 * PI_F)
ys_p, _, _ = boltzmann(M_DM, ALPHA_LM, True, PI_F)
om_c = {xm: omega_from_Y(M_DM, ys_c[xm], True) for xm in (1e3, 1e4, 1e6, 1e8)}
om_p = {xm: omega_from_Y(M_DM, ys_p[xm], True) for xm in (1e3, 1e4, 1e6, 1e8)}
print("INFO Dirac pair, attractive U(1)_D at alpha_X = alpha_LM, 16 v:  Omega h^2 (correct kernel) by T_chi = T cutoff x_max: "
      + ", ".join(f"{k:.0e}:{v:.4f}" for k, v in om_c.items()))
print("INFO same with archived half-argument kernel: " + ", ".join(f"{k:.0e}:{v:.4f}" for k, v in om_p.items()))
check("C4 monotone: later cutoff of the Coulomb-enhanced annihilation lowers Omega (Omega(1e3) > Omega(1e4) > Omega(1e6) >= Omega(1e8))",
      om_c[1e3] > om_c[1e4] > om_c[1e6] >= om_c[1e8])
check("C5 dark pair alone, Dirac counting, correct kernel, same alpha_X in sigma v and in the Coulomb force: "
      "Omega h^2 lies in [0.070, 0.088] for every cutoff 1e3..inf, so it misses the lane's 0.1275 by -33% to -43% "
      "and Planck 0.120 by -29% to -40%",
      all(0.070 < v < 0.088 for v in om_c.values()), f"min={min(om_c.values()):.4f} max={max(om_c.values()):.4f}")
check("C6 closed-form Kolb-Turner with S(x_F=25) in sigma v and Dirac counting is NOT a valid propagation of a 1/v-growing sigma v: "
      "it overstates the Boltzmann result by more than 40% for every cutoff",
      all(KT_omega(M_DM, ALPHA_LM, float(sb_rel), dirac=True) / v - 1 > 0.40 for v in om_c.values()),
      f"KT(S_25)={KT_omega(M_DM, ALPHA_LM, float(sb_rel), dirac=True):.4f}")
check("C7 archived half-argument kernel in the same Dirac model gives 0.12-0.14 for cutoffs 1e3..1e4 "
      "(the number the lane's 'S_dark = 1, Dirac' picture can be confused with; READING: coincidence of two errors, not a result)",
      0.115 < om_p[1e4] < 0.145 and 0.115 < om_p[1e3] < 0.15, f"{om_p[1e3]:.4f} {om_p[1e4]:.4f}")

# mass that would give Omega = 0.12 in the dark-alone model: Omega scales as m^2 at fixed alpha, g_*, S(alpha)
ratios = {xm: math.sqrt(OMEGA_OBS / v) for xm, v in om_c.items()}
mstar = {xm: M_DM * r / V_EW for xm, r in ratios.items()}
print("INFO m*(Omega=0.12)/v for Dirac + correct kernel: " + ", ".join(f"{k:.0e}:{v:.1f}" for k, v in mstar.items()))
# check the m^2 law by a second solve at 1.3 m
ys_m, _, _ = boltzmann(1.3 * M_DM, ALPHA_LM, True, 2 * PI_F, snaps=(1e4,))
om_m = omega_from_Y(1.3 * M_DM, ys_m[1e4], True)
check("C8 Omega ~ m^2 at fixed alpha up to the logarithmic shift of the freeze-out point: Omega(1.3 m)/Omega(m) = 1.69 within 1%",
      abs(om_m / om_c[1e4] / 1.69 - 1) < 0.01, f"{om_m / om_c[1e4]:.4f} (so m* by the m^2 law is good to about 0.3%)")
check("C9 the mass needed for Omega = 0.12 is 19.0-20.7 v (not 16 v) in the dark-alone Dirac model with the correct kernel",
      all(18.5 < v < 21.0 for v in mstar.values()), f"{min(mstar.values()):.2f}-{max(mstar.values()):.2f} v")

# sensitivity to the two thermal premises that are inputs here (g spin degeneracy, g_*)
ys_g, _, _ = boltzmann(M_DM, ALPHA_LM, True, 2 * PI_F, g=4, snaps=(1e4,))
ys_gs, _, _ = boltzmann(M_DM, ALPHA_LM, True, 2 * PI_F, gstar=100.0, snaps=(1e4,))
d_g = omega_from_Y(M_DM, ys_g[1e4], True) / om_c[1e4] - 1
d_gs = omega_from_Y(M_DM, ys_gs[1e4], True) / om_c[1e4] - 1
check("C10 premise sensitivity at cutoff 1e4: spin degeneracy g=2->4 changes Omega by less than 12%, g_*=106.75->100 by less than 5%",
      abs(d_g) < 0.12 and abs(d_gs) < 0.05, f"dg={d_g:+.3f} dgstar={d_gs:+.3f}")

# reproduce the corrigendum's visible-sector numbers independently (the lane's S_vis/S_dark with S_dark = 1)
def Rratio(alpha, factor=2 * PI_F):
    s1 = Sbar_fast(4 / 3 * alpha, 25.0, factor)
    s8 = Sbar_fast(-alpha / 6, 25.0, factor)
    sv = (8 * s1 + s8) / 9
    return sv, 31 / 9 * sv


sv, R = Rratio(ALPHA_LM)
svp, Rp = Rratio(ALPHA_LM, PI_F)
check("C11 archived endpoint reproduced: pi-form kernel gives R(alpha_LM) = 5.44202 (archived 5.442020)",
      abs(Rp - 5.442019868) < 1e-6, f"{Rp:.9f}")
check("C12 corrected kernel: S_vis = 2.3143, R(alpha_LM) = 7.9716 (corrigendum 2.314 / 7.972)",
      abs(sv - 2.3143) < 5e-4 and abs(R - 7.9716) < 2e-3, f"S_vis={sv:.5f} R={R:.5f}")


def eta_pred(m, alpha, R_):
    return KT_K * XF * m * m / (math.sqrt(GSTAR) * MPL * PI_F * alpha ** 2 * R_ * 3.65e7)


e_one = eta_pred(M_DM, ALPHA_LM, R)
m_match = brentq(lambda mm: eta_pred(mm, ALPHA_LM, R) - 6.12e-10, 1000, 9000)
check("C13 eta_pred(16 v) = 4.38e-10 (-28.4%) and the matching mass is 4657 GeV = 18.9 v (corrigendum)",
      abs(e_one / 6.12e-10 - 1 + 0.284) < 0.002 and abs(m_match - 4657) < 3 and abs(m_match / V_EW - 18.9) < 0.05,
      f"eta={e_one:.4e} m={m_match:.1f}")
sv2, R2_ = Rratio(0.0454)
check("C14 single comparator-reproducing coupling alpha=0.0454 gives eta_pred about 2.56e-9 (+318%); corrigendum quotes 2.55e-9 (+317%): "
      "difference is the rounding of 0.0454",
      abs(eta_pred(M_DM, 0.0454, R2_) / 2.55e-9 - 1) < 0.01, f"eta={eta_pred(M_DM, 0.0454, R2_):.4e}")

print(f"INFO runtime {time.time() - T_START:.1f}s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("SUMMARY: exact charge census shows no SU(3)xSU(2) singlet on the base x fibre taste cube (and exhibits the counter-embedding "
      "that has two), derives S=2*pi*alpha/v_rel/(1-exp(-2*pi*alpha/v_rel)) from the Kummer/Gamma solution and shows the archived "
      "form is the same kernel at half the coupling, and shows a dark Dirac pair feeling alpha_X=alpha_LM gives Omega h^2 of "
      "0.072-0.085 at 16 v (not 0.1275) with the Kolb-Turner closed form overstating it by over 40%.")
sys.exit(0 if FAIL == 0 else 1)
