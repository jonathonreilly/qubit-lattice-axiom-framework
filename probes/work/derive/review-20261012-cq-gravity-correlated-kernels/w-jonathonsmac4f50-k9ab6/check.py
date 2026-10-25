#!/usr/bin/env python3
"""check.py for J:derive:review-20261012-cq-gravity-correlated-kernels:a1

Self-contained (numpy, scipy, sympy, mpmath, fractions only).  No repository access.
Units: hbar = 1 unless a symbol hbar is used.  Every finite algebraic claim is checked
with Fractions or sympy; the finite-bandwidth radiation-integral section (D) is numerical
quadrature and is labelled as such.

Sections
 A  stationary two-point positivity: the product bound, the exact sub-floor (non-additive)
    counterexample to the pointwise additive floor, and the emission-silent minimum
 B  Lorentz-invariant measure lemma (boost orbit) and what an emission-silent kernel does to it
 C  channels: Maxwell stress is traceless and pure spin-2 (exact coefficient), scalar
    cross-check, Barnes-Rivers contractions for the scalar and the spin-2 channel
 D  light-cone prescription: Holder-continuous form factor versus a jump, on a
    finite-bandwidth pulse (numerical)
 E  one explicit kernel (emission-silent, saturated) through the noise integrals
"""
import itertools
import math
import random
import sys
import time
import warnings
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
import sympy as sp
from scipy import integrate

warnings.filterwarnings("ignore")
T0 = time.time()
results = []


def rec(ok, name):
    results.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name)
    sys.stdout.flush()


# ----------------------------------------------------------------------------------------
# A. Stationary two-point positivity
# ----------------------------------------------------------------------------------------
# Data at one 4-momentum p (timelike) for a Hermitian operator f and a self-commuting
# classical record J:  S_ff(+-p) = a_pm >= 0, S_JJ(+p) = S_JJ(-p) = P (J classical),
# S_fJ(+-p) = z_pm.  Wightman positivity: a_pm * P >= |z_pm|^2.  Commutator (Kubo gain F):
# C_fJ(p) = z_p - conj(z_m) = i*hbar*F.

a_p, a_m, P_, hb = sp.symbols("a_p a_m P hbar", positive=True)
sa, sb = sp.symbols("sa sb", positive=True)           # sa = sqrt(a_p), sb = sqrt(a_m)
rec(sp.simplify(2 * (sa**2 + sb**2) - (sa + sb)**2 - (sa - sb)**2) == 0,
    "A1 exact identity 2(a+b)-(sqrt a+sqrt b)^2=(sqrt a-sqrt b)^2 (step of the product bound)")


def cmul(x, y):                 # complex numbers as (re, im) pairs of Fractions
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def cabs2(x):
    return x[0] * x[0] + x[1] * x[1]


# A2: exact equality instance.  P=4, a+=a-=1/4, z+=i, z-=i  => C = z+ - conj(z-) = 2i, hbar F = 2
P = Fr(4); ap = Fr(1, 4); am = Fr(1, 4)
zp = (Fr(0), Fr(1)); zm = (Fr(0), Fr(1))
C = (zp[0] - zm[0], zp[1] + zm[1])                      # z+ - conj(z-)
hF2 = cabs2(C)
psd_p = ap * P - cabs2(zp) >= 0 and ap >= 0 and P >= 0
psd_m = am * P - cabs2(zm) >= 0 and am >= 0
rec(psd_p and psd_m and hF2 == 4 and (ap + am) * P * 2 == hF2,
    "A2 equality case of (a++a-)P >= (hbar F)^2/2 is attained exactly (rational data)")

# A3: random exact rational feasible data never violate the product bound
rng = random.Random(20261012)
worst = None
viol = 0
for _ in range(6000):
    P = Fr(rng.randint(1, 60), rng.randint(1, 12))
    zp = (Fr(rng.randint(-30, 30), rng.randint(1, 9)), Fr(rng.randint(-30, 30), rng.randint(1, 9)))
    zm = (Fr(rng.randint(-30, 30), rng.randint(1, 9)), Fr(rng.randint(-30, 30), rng.randint(1, 9)))
    ap = cabs2(zp) / P + Fr(rng.randint(0, 20), rng.randint(1, 7))
    am = cabs2(zm) / P + Fr(rng.randint(0, 20), rng.randint(1, 7))
    C = (zp[0] - zm[0], zp[1] + zm[1])
    hF2 = cabs2(C)
    if hF2 == 0:
        continue
    ratio = (ap + am) * P * 2 / hF2
    worst = ratio if worst is None else min(worst, ratio)
    if ratio < 1:
        viol += 1
rec(viol == 0 and worst >= 1, "A3 6000 random exact PSD data: (a++a-)P*2/(hbar F)^2 >= 1 (min ratio %.6f)" % float(worst))

# A3b: emission silence (a- = 0 forces z- = 0): a+ P >= (hbar F)^2
viol = 0
worst = None
for _ in range(6000):
    P = Fr(rng.randint(1, 60), rng.randint(1, 12))
    zp = (Fr(rng.randint(-30, 30), rng.randint(1, 9)), Fr(rng.randint(-30, 30), rng.randint(1, 9)))
    ap = cabs2(zp) / P + Fr(rng.randint(0, 20), rng.randint(1, 7))
    hF2 = cabs2(zp)
    if hF2 == 0:
        continue
    ratio = ap * P / hF2
    worst = ratio if worst is None else min(worst, ratio)
    if ratio < 1:
        viol += 1
rec(viol == 0 and worst >= 1, "A3b emission-silent data: a+ P >= (hbar F)^2, 6000 exact draws (min ratio %.6f)" % float(worst))

# A4: exact counterexample to "CP/positivity implies the pointwise ADDITIVE floor on the
# emission side".  Felt field f = B + G J with real gain G (timelike: G = -g/s), record J.
G, P, phi = sp.symbols("G P phi", real=True)            # phi = hbar*F >= 0
P_pos, phi_pos = sp.symbols("P_pos phi_pos", positive=True)
Gs = sp.symbols("Gs", real=True, nonzero=True)
# emission side (-p): rank-one Gram matrix with null vector (1, G):  Sigma_- = P [[G^2,-G],[-G,1]]
Sm = sp.Matrix([[Gs**2 * P_pos, -Gs * P_pos], [-Gs * P_pos, P_pos]])
# absorption side (+p): S_BJ(p) = i*phi + S_JB(-p) = i*phi - G P ; minimal S_BB = |S_BJ|^2 / P
SBJp = sp.I * phi_pos - Gs * P_pos
SBBp = sp.simplify((SBJp * sp.conjugate(SBJp)) / P_pos)
Sp = sp.Matrix([[SBBp, SBJp], [sp.conjugate(SBJp), P_pos]])
w = sp.Matrix([[1, Gs]])                                 # f = B + G J
Sff_m = sp.simplify((w * Sm * w.T)[0])
Sff_p = sp.simplify((w * Sp * w.T)[0])
rec(sp.simplify(Sm.det()) == 0 and sp.simplify(Sp.det()) == 0, "A4a both 2x2 Gram matrices are singular PSD (det = 0, positive diagonal)")
rec(Sff_m == 0, "A4b emission-side felt noise S_ff(-p) = 0 exactly")
rec(sp.simplify(Sff_p - phi_pos**2 / P_pos) == 0, "A4c absorption-side felt noise S_ff(+p) = (hbar F)^2/P exactly")
# commutator constraint C_BJ(p) = S_BJ(p) - conj(S_BJ(-p)) = i phi   (S_BJ(-p) = -G P real)
rec(sp.simplify(SBJp - (-Gs * P_pos) - sp.I * phi_pos) == 0, "A4d Kubo commutator constraint C_BJ = i hbar F holds")
# additive floor: S_BB*P >= phi^2/4, symmetric (no B-J correlation): K = S_BB + G^2 P >= |G| phi
Dd = sp.symbols("Dd", positive=True)
Kadd = Dd + Gs**2 * P_pos
Pstar = phi_pos / (2 * sp.Abs(Gs))                       # stationary point of phi^2/(4P) + G^2 P
Ksat = Kadd.subs(Dd, phi_pos**2 / (4 * P_pos))
rec(sp.simplify(sp.diff(Ksat, P_pos).subs(P_pos, Pstar)) == 0, "A5a stationary point P* = hbar F/(2|G|) of the additive total noise")
Kmin = sp.simplify(Ksat.subs(P_pos, Pstar))
rec(sp.simplify(Kmin - sp.Abs(Gs) * phi_pos) == 0, "A5 additive (uncorrelated) minimum of the emission-side noise is |G| hbar F")
rec(sp.simplify((sp.Abs(Gs) * phi_pos) - Sff_m).is_positive is True, "A6 exact: the correlated emission-side value 0 lies strictly below the additive floor |G| hbar F, so the pointwise additive floor is not implied by positivity+commutator")
rec(sp.simplify((Sff_p + Sff_m) * P_pos - phi_pos**2) == 0, "A7 the product bound survives: (S+ + S-) P = (hbar F)^2 >= (hbar F)^2/2 (ratio 2, emission-silent value)")

# ----------------------------------------------------------------------------------------
# B. Lorentz-invariant measure lemma
# ----------------------------------------------------------------------------------------
L, m = sp.symbols("Lambda m", positive=True)
V = sp.pi * (L * sp.sqrt(L**2 + m**2) - m**2 * sp.asinh(L / m))
rec(sp.simplify(sp.diff(V, L) - 2 * sp.pi * L**2 / sp.sqrt(L**2 + m**2)) == 0,
    "B1 invariant shell measure inside |p|<Lambda: V' = 2 pi Lambda^2/E (exact)")
rec(sp.limit(V / L**2, L, sp.oo) == sp.pi, "B2 V/Lambda^2 -> pi, so the shell measure diverges quadratically")

# disjoint boosted copies, exact: u_n = e^{eta_n} integers, copy n has p0 in [a(u+1/u)/2, b u]
a_, b_ = Fr(1), Fr(2)
u = [Fr(1)]
for _ in range(8):
    u.append(Fr(math.floor(2 * b_ * u[-1] / a_)) + 1)
ok = all(b_ * u[i] < a_ * (u[i + 1] + 1 / u[i + 1]) / 2 for i in range(len(u) - 1))
ok = ok and all(b_ * u[i] < a_ * (u[j] + 1 / u[j]) / 2 for i in range(len(u)) for j in range(i + 1, len(u)))
rec(ok, "B3 nine boosted copies of an energy window are pairwise disjoint (exact integers): an invariant positive measure has infinite mass")
W_ = sp.symbols("W", positive=True)
rec(sp.integrate(sp.Integer(0) * W_, (W_, 0, sp.oo)) == 0, "B4 (bookkeeping) a kernel with S_ff(-p) = 0 on V+ has vacuum-excitation integrand identically 0, hence rate 0 at golden-rule order")

# ----------------------------------------------------------------------------------------
# C. Channels
# ----------------------------------------------------------------------------------------
th, ph_, E = sp.symbols("theta phi E", positive=True)
eta = sp.diag(1, -1, -1, -1)
n = sp.Matrix([sp.sin(th) * sp.cos(ph_), sp.sin(th) * sp.sin(ph_), sp.cos(th)])
e1 = sp.Matrix([sp.cos(th) * sp.cos(ph_), sp.cos(th) * sp.sin(ph_), -sp.sin(th)])
e2 = sp.Matrix([-sp.sin(ph_), sp.cos(ph_), 0])
w_ = E / 2
k1 = sp.Matrix([w_, *(w_ * n)])
k2 = sp.Matrix([w_, *(-w_ * n)])


def Fmat(k, e):
    ev = sp.Matrix([0, *e])
    return k * ev.T - ev * k.T


def Pi2(i, j, k, l):
    d = lambda x, y: 1 if x == y else 0
    return sp.Rational(1, 2) * (d(i, k) * d(j, l) + d(i, l) * d(j, k)) - sp.Rational(1, 3) * d(i, j) * d(k, l)


amps = {}
for ia, ea in enumerate((e1, e2)):
    for ib, eb in enumerate((e1, e2)):
        F1 = Fmat(k1, ea)
        F2 = Fmat(k2, eb)
        M = F1 * eta * F2.T
        FF = sum((eta * F2 * eta)[i, j] * F1[i, j] for i in range(4) for j in range(4))
        amps[(ia, ib)] = (-(M + M.T) + sp.Rational(1, 2) * eta * FF).applyfunc(sp.simplify)
tr_ok = all(sp.simplify(sum(eta[i, i] * A[i, i] for i in range(4))) == 0 for A in amps.values())
cons_ok = all(all(sp.simplify(A[0, j]) == 0 for j in range(4)) for A in amps.values())
rec(tr_ok, "C1 two-photon matrix element of the Maxwell stress is traceless (exact)")
rec(cons_ok, "C2 it is conserved in the pair rest frame (A^{0 nu} = 0), so only the spin-2 channel is populated")
tot = 0
for A in amps.values():
    for i, j, k, l in itertools.product(range(3), repeat=4):
        tot += Pi2(i, j, k, l) * A[i + 1, j + 1] * A[k + 1, l + 1]
tot = sp.simplify(tot)
angint = sp.integrate(sp.integrate(tot * sp.sin(th), (th, 0, sp.pi)), (ph_, 0, 2 * sp.pi))
Wmax = sp.simplify(sp.Rational(1, 2) * angint / (32 * sp.pi**2))        # W^{ijkl} Pi2_{ijkl}
a_max = sp.simplify(Wmax / (5 * E**4))
rec(a_max == 1 / (40 * sp.pi), "C3 Maxwell spin-2 spectral weight W = a s^2 Pi2 with a = 1/(40 pi) (identical-photon factor 1/2, dPhi2 = dOmega/(32 pi^2), exact)")

# conformally coupled real scalar cross-check: expect a_scalar = a_Maxwell/12
As = (sp.Rational(1, 2) * E**2 * sp.Matrix(3, 3, lambda i, j: n[i] * n[j]) - sp.Rational(1, 6) * E**2 * sp.eye(3))
tr_s = sp.simplify(As.trace())
tot_s = sum(Pi2(i, j, k, l) * As[i, j] * As[k, l] for i, j, k, l in itertools.product(range(3), repeat=4))
Ws = sp.simplify(sp.Rational(1, 2) * sp.integrate(sp.integrate(sp.simplify(tot_s) * sp.sin(th), (th, 0, sp.pi)), (ph_, 0, 2 * sp.pi)) / (32 * sp.pi**2))
a_sc = sp.simplify(Ws / (5 * E**4))
rec(tr_s == 0 and a_sc == 1 / (480 * sp.pi) and sp.simplify(a_max / a_sc) == 12,
    "C4 conformal real scalar gives a = 1/(480 pi); Maxwell/scalar = 12 (the standard c_T ratio): the machinery reproduces a known number")

# Barnes-Rivers contractions at p = (0,0,0,kz): spacelike static transfer
kz = sp.symbols("kz", positive=True)
p4 = sp.Matrix([0, 0, 0, kz])
p2 = (p4.T * eta * p4)[0]                                  # = -kz^2
theta_u = eta - (p4 * p4.T) / p2                           # theta^{mu nu}, upper
etal = eta


def lower(T):
    return etal * T * etal


def contract(T1, T2):
    # P2 and P0 contractions of two symmetric tensors (upper indices)
    T1l, T2l = lower(T1), lower(T2)
    # theta^{mu rho} theta^{nu sigma} T1_{mu nu} T2_{rho sigma}
    TT = sum(theta_u[i, k] * theta_u[j, l] * T1l[i, j] * T2l[k, l] for i in range(4) for j in range(4) for k in range(4) for l in range(4))
    t1 = sum(theta_u[i, j] * T1l[i, j] for i in range(4) for j in range(4))
    t2 = sum(theta_u[i, j] * T2l[i, j] for i in range(4) for j in range(4))
    P2 = sp.simplify(TT - sp.Rational(1, 3) * t1 * t2)
    P0 = sp.simplify(sp.Rational(1, 3) * t1 * t2)
    return P2, P0


Msym = sp.symbols("M", positive=True)
Tmass = sp.diag(Msym, 0, 0, 0)
lvec = sp.Matrix([1, 1, 0, 0])                              # null beam along x, p.l = 0
Tphot = sp.Symbol("rho", positive=True) * lvec * lvec.T
P2mm, P0mm = contract(Tmass, Tmass)
trT = sum(eta[i, i] * Tmass[i, i] for i in range(4))
gr_mm = sp.simplify(sum(lower(Tmass)[i, j] * Tmass[i, j] for i in range(4) for j in range(4)) - sp.Rational(1, 2) * trT * trT)
rec((P2mm, P0mm, gr_mm) == (sp.Rational(2, 3) * Msym**2, sp.Rational(1, 3) * Msym**2, sp.Rational(1, 2) * Msym**2),
    "C5 mass-mass static exchange: spin-2 contraction 2/3, scalar 1/3, GR numerator 1/2 (units M^2)")
P2mp, P0mp = contract(Tmass, Tphot)
rho = sp.Symbol("rho", positive=True)
trTp = sum(eta[i, i] * Tphot[i, i] for i in range(4))
gr_mp = sp.simplify(sum(lower(Tmass)[i, j] * Tphot[i, j] for i in range(4) for j in range(4)) - sp.Rational(1, 2) * trT * trTp)
rec(P0mp == 0 and sp.simplify(P2mp - gr_mp) == 0 and sp.simplify(gr_mp - Msym * rho) == 0,
    "C6 mass-photon exchange: the scalar channel contributes exactly 0 and the spin-2 channel alone equals the GR amplitude M rho (a scalar-only kernel cannot bend light)")
rec(sp.Rational(3, 2) * sp.Rational(1, 3) == sp.Rational(1, 2), "C7 a scalar-channel coefficient 3/2 reproduces the Newtonian numerator 1/2 with the spin-2 form factor set to 0 (so Newton alone does not fix the spin-2 factor; light bending/GW emission do)")

# ----------------------------------------------------------------------------------------
# D. Light-cone prescription on a finite-bandwidth pulse (numerical quadrature)
# ----------------------------------------------------------------------------------------
# h(omega,r) is proportional to I(omega) = int_0^inf dk k sin(kr) e^{-(k/K)^2} F(omega^2-k^2) / (k^2-omega^2 - i eps).
# F=1 gives (pi/2) e^{i omega r}.  A pulse is int d omega A(omega) I(omega), A Gaussian.
R_ = 3.0
KC = 40.0
MU = 1.3
KMAX = 150.0
OM0, DOM = 2.0, 0.35


def inner(wv, eps, kind):
    b = wv * wv - MU * MU

    def f(k):
        s = wv * wv - k * k
        d = k * k - wv * wv
        base = k * math.sin(k * R_) * math.exp(-(k / KC) ** 2) / (d - 1j * eps)
        if kind == "gr":
            Fv = 1.0
        elif kind == "kink":
            Fv = 1.0 if s <= 0 else math.exp(-s / 0.05)          # continuous, one-sided derivative jump
        elif kind == "jump":
            Fv = 1.0 if s < 0 else 0.0                           # spacelike projector
        else:                                                    # "mass": F = mu^2/(mu^2 - s), retarded
            Fv = MU * MU / (k * k - b - 1j * eps)
        return base * Fv

    sw = math.sqrt(eps)
    pts = [wv - sw, wv, wv + sw]
    if kind == "mass" and b > 0:
        sb_ = math.sqrt(b)
        pts += [sb_ - sw, sb_, sb_ + sw]
    pts = sorted(p for p in pts if 0 < p < KMAX)
    edges = [0.0] + pts + list(np.linspace(pts[-1], KMAX, 14)[1:])
    tot = 0j
    for lo, hi in zip(edges[:-1], edges[1:]):
        vr, _ = integrate.quad(lambda k: f(k).real, lo, hi, limit=600, epsabs=1e-11, epsrel=1e-11)
        vi, _ = integrate.quad(lambda k: f(k).imag, lo, hi, limit=600, epsabs=1e-11, epsrel=1e-11)
        tot += vr + 1j * vi
    return tot


xg, wg = np.polynomial.legendre.leggauss(28)
wlo, whi = OM0 - 5 * DOM, OM0 + 5 * DOM
wnodes = 0.5 * (whi - wlo) * xg + 0.5 * (whi + wlo)
wweights = 0.5 * (whi - wlo) * wg * np.exp(-((wnodes - OM0) ** 2) / (2 * DOM**2))


def pulse(eps, kind):
    return sum(wt * inner(wv, eps, kind) for wv, wt in zip(wnodes, wweights))


def closed(kind):
    """Residue evaluation with the Gaussian cutoff g(k)=exp(-(k/K)^2) evaluated at the poles."""
    g = lambda k: math.exp(-(k / KC) ** 2)
    tot = 0j
    for wv, wt in zip(wnodes, wweights):
        if kind == "gr":
            val = (math.pi / 2) * np.exp(1j * wv * R_) * g(wv)
        else:
            q = wv * wv - MU * MU
            if q > 0:
                sec = np.exp(1j * math.sqrt(q) * R_) * g(math.sqrt(q))
            else:
                sec = np.exp(-math.sqrt(-q) * R_) * math.exp((math.sqrt(-q) / KC) ** 2)
            val = (math.pi / 2) * (np.exp(1j * wv * R_) * g(wv) - sec)
        tot += wt * val
    return tot


E1, E2, E3 = 1e-4, 1e-6, 1e-8
res = {}
for kind in ("gr", "kink", "mass", "jump"):
    res[kind] = [pulse(e, kind) for e in (E1, E2, E3)]
rec(abs(res["gr"][2] - closed("gr")) < 1e-6 * abs(closed("gr")), "D1 F=1 (GR): pulse integral reproduces the cutoff-weighted residue (pi/2)e^{i w r} g(w) to 1e-6 (numerical)")
rec(abs(res["mass"][2] - closed("mass")) < 1e-6 * abs(closed("mass")) and abs(res["mass"][2] - res["mass"][1]) < 1e-5,
    "D2 retarded massive-pole form factor: pulse response equals the massless-minus-massive residue form to 1e-6 and is eps-independent (numerical)")
dk = abs(res["kink"][2] - res["kink"][1])
rec(dk < 5e-3 and abs(res["kink"][2] - res["gr"][2]) > 1e-2,
    "D3 continuous (kink) form factor: eps-limit exists (|I(1e-8)-I(1e-6)|=%.2e) and differs from GR (numerical)" % dk)
# predicted log slope for the jump: dRe/dln(1/eps) = int A(w) sin(w r)/2 e^{-(w/K)^2} dw
slope_pred = float(sum(wt * 0.5 * math.sin(wv * R_) * math.exp(-(wv / KC) ** 2) for wv, wt in zip(wnodes, wweights)))
slope_obs = (res["jump"][2].real - res["jump"][1].real) / math.log(E2 / E3)
slope_obs2 = (res["jump"][1].real - res["jump"][0].real) / math.log(E1 / E2)
rec(abs(slope_obs - slope_pred) < 0.02 * abs(slope_pred) and abs(slope_obs2 - slope_pred) < 0.02 * abs(slope_pred) and abs(slope_pred) > 1e-3,
    "D4 jump of F at the cone: finite-bandwidth pulse still grows as ln(1/eps) with slope %.5f (predicted %.5f), no eps-limit (numerical)" % (slope_obs, slope_pred))
rec(abs(res["jump"][2].imag - res["jump"][1].imag) < 5e-3, "D5 the divergence of the jump case is in the real (cone-delta) part only; imaginary part converges (numerical)")

# Holder lemma (analytic part of D): for F in C^{0,alpha} near s=0,  (F(s)-F(0))/s is locally integrable
s_, al = sp.symbols("s alpha", positive=True)
rec(sp.integrate(s_**(al - 1), (s_, 0, 1), conds="none") == 1 / al,
    "D6 integrability behind the prescription lemma: int_0^1 s^(alpha-1) ds = 1/alpha < oo, so (F(s)-F(0))/s is locally integrable for Holder F (the Plemelj step itself is argued in ATTEMPT.md step 6)")
Fjump_log = sp.integrate(1 / s_, (s_, sp.Symbol("eta", positive=True), 1))
rec(sp.limit(Fjump_log, sp.Symbol("eta", positive=True), 0, "+") == sp.oo, "D7 a jump leaves int ds/s, which diverges logarithmically as the lower limit goes to 0")

# ----------------------------------------------------------------------------------------
# E. One explicit kernel (emission-silent, saturated), noise integrals
# ----------------------------------------------------------------------------------------
s, g, lam, mu, Fa, hbar = sp.symbols("s g lambda mu F hbar", positive=True)
P_plus = hbar * Fa * (s + mu**2) / (2 * g * lam)            # record noise on V+ (null-cone regulator mu)
S_abs = sp.simplify(hbar**2 * Fa**2 / P_plus)               # absorption-side felt noise
rec(sp.simplify(S_abs - 2 * hbar * g * lam * Fa / (s + mu**2)) == 0, "E1 absorption noise of the saturated emission-silent kernel is 2 hbar g lambda F/(s+mu^2)")
Mrec = (g / s) ** 2 * P_plus                                # |G|^2 P: metric-record covariance density
rec(sp.simplify(S_abs * Mrec - hbar**2 * g**2 * Fa**2 / s**2) == 0, "E2 profile-independent product: sigma * M = hbar^2 g^2 F^2/s^2 exactly (saturates Cauchy-Schwarz for every mu, lambda)")
eta_ = sp.symbols("eta_", positive=True)
dlt = sp.symbols("delta", positive=True)
Mint = sp.integrate(sp.expand(Mrec), (s, eta_, dlt))
rec(sp.limit(Mint, eta_, 0, "+") == sp.oo, "E3 metric-record covariance int M ds diverges at the cone even with mu>0 (1/eta term): record is not locally finite")
Mint0 = sp.integrate(sp.expand(Mrec.subs(mu, 0)), (s, eta_, dlt))
rec(sp.limit(Mint0, eta_, 0, "+") == sp.oo, "E4 with mu=0 the divergence is logarithmic: (hbar g F/2 lambda) ln(delta/eta)")
# absorption of a finite-bandwidth source: weight e^{-s/s0} (s0=1) on the timelike side
mp.mp.dps = 30
def Iabs(m2):
    return mp.e ** m2 * mp.expint(1, m2)                 # int_0^inf e^{-x}/(x+m2) dx, exact
qchk = mp.quad(lambda x: mp.e ** (-x) / (x + mp.mpf("0.01")), [0, 0.01, 0.1, 1, 10, 60])
rec(abs(qchk - Iabs(mp.mpf("0.01"))) < mp.mpf("1e-12"), "E5a quadrature agrees with e^{m2}E1(m2) at m2=0.01")
incs = [Iabs(mp.mpf(10) ** (-(k_ + 2))) - Iabs(mp.mpf(10) ** (-k_)) for k_ in (4, 6, 8, 10)]
rec(all(abs(d - 2 * mp.log(10)) < mp.mpf("0.002") for d in incs),
    "E5 absorption of a smooth finite-bandwidth source grows as ln(1/mu^2) (increment per two decades in mu^2 -> 2 ln 10): the null regulator mu cannot be removed")
s0 = sp.symbols("s0", positive=True)
Eabs = sp.integrate(2 * hbar * g * lam * Fa / (s + mu**2), (s, 0, s0))
rec(sp.simplify(sp.expand_log(Eabs - 2 * hbar * g * lam * Fa * sp.log((s0 + mu**2) / mu**2), force=True)) == 0,
    "E6 exact: int_0^{s0} S_abs ds = 2 hbar g lambda F ln((s0+mu^2)/mu^2)")
# vacuum excitation: emission side identically zero
rec(sp.simplify(Sff_m) == 0, "E7 vacuum excitation rate = int S_ff(-p) W(p) = 0 for the explicit kernel at every p in V+ (golden-rule order, any W)")
# CP at each p: Gram determinants are exactly zero (PSD) for all parameter values
rec(sp.simplify(Sm.det()) == 0 and sp.simplify(Sp.det()) == 0, "E8 Gram matrices of the explicit kernel are PSD at every p (rank one), pointwise in p")

total_pass = sum(results)
total_fail = len(results) - total_pass
print("TOTAL: PASS=%d FAIL=%d" % (total_pass, total_fail))
print("runtime_seconds=%.1f" % (time.time() - T0))
print("SUMMARY: exact and numerical checks show that positivity plus commutator data allow the vacuum-side noise to be exactly zero strictly below the pointwise additive floor, that a Holder-continuous cone form factor gives a regulator-independent finite response to a finite-bandwidth pulse while a jump gives ln(1/eps), and that the saturated explicit kernel has sigma*M = hbar^2 g^2 F^2/s^2 so its classical metric-record covariance is non-locally-finite at the cone; Maxwell spin-2 weight is a = 1/(40 pi) and the scalar channel is inert for photons.")
sys.exit(0 if total_fail == 0 else 1)
