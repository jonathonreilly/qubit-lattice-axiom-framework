#!/usr/bin/env python3
"""Checker for J:derive:review-20261012-wilson-physical-bridge:a1  (same-family, unrefereed).

Setting (supplied, see ATTEMPT.md): continuous-time spatial Wilson fermion h(p)=a*alpha.sin p + beta*(m+W(p)),
W=sum(1-cos p_i), literal link exp(i e A), noncompact Maxwell + Gauss sector, filled negative band, photon
omega(k)=2|sin(k/2)|.  Order-e^2 energy shift of the one-electron state in the Gauss-law subspace, with the
additive-mass counterterm  -e^2 dE(0) beta  (rest-energy calibration).

Sections
  A  exact algebra / exact angular integrals (sympy, mpmath, Fractions)
  B  Euclidean local coefficient re-computation (independent quadrature)
  C  on-shell calibrated shift: gauge equality, rest shift, convergence to the local coefficient
  D  hard/soft decomposition of the on-shell shift
  E  infrared meaning: energy IR-finite, residue log divergent (gauge dependent)
  F  cone-mismatch dependence (a != 1): continuum log running vs lattice on-shell data
  G  domain of the fixed-order expansion
No downloads, numpy/scipy/sympy/mpmath only.  One process.
"""
import sys, time
from itertools import product
from fractions import Fraction
import numpy as np
from numpy.polynomial.legendre import leggauss
import sympy as sp
import mpmath as mp

T0 = time.time()
RESULTS = []


def chk(name, ok, detail=""):
    RESULTS.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name + ((" | " + detail) if detail else ""), flush=True)


# ---------------------------------------------------------------------------------------------
# Values SUPPLIED by the landed note (docs/SPATIAL_WILSON_OBSERVATION_MAP_AND_MASS_MATCHING_BOUNDED_THEOREM_NOTE_2026-10-12.md)
# used only as comparators, never fitted:
LANDED_MASSLESS_FF = -0.13699805078154      # massless integral before conversion constants, eq. (18) text
LANDED_DELTA_F = -0.1327763348              # eq. (18)
LANDED_DELTA_GAMMA = 0.0118573122           # eq. (18)
LANDED_CW = 0.37434747251955                # eq. (13)
LANDED_CW_FEYN_SPLIT = (0.341508038733323, 0.032839433786227)
ALPHA_INV = 137.035999                      # Thomson-limit calibration (supplied data, magnitude only)

# =============================================================================================
# A. exact algebra
# =============================================================================================
# A1 Clifford algebra of the four band matrices Gamma=(alpha_1,alpha_2,alpha_3,beta)
s0 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
kp = sp.kronecker_product
Gam = [kp(sx, sx), kp(sx, sy), kp(sx, sz), kp(sz, s0)]
ok = all((Gam[i] * Gam[j] + Gam[j] * Gam[i]) == (2 * sp.eye(4) if i == j else sp.zeros(4)) for i in range(4) for j in range(4))
chk("A1 four Hermitian band matrices obey the Clifford relations (exact)", ok)

# A2 exact projector-trace identities used for the vertex sums  S = tr(P_q J P_p J)
def Gdot(v):
    return sum((Gam[i] * v[i] for i in range(4)), sp.zeros(4))

quads = [(1, 2, 2, 4), (2, 2, 4, 5), (1, 1, 1, 1), (2, 3, 6, 0), (1, 4, 8, 0), (4, 4, 7, 4)]
qn = [sp.sqrt(sum(c * c for c in q)) for q in quads]
okp = okm = True
rng = np.random.default_rng(1)
cnt = 0
for i, q1 in enumerate(quads):
    for j, q2 in enumerate(quads):
        n1 = [sp.Rational(c) / qn[i] for c in q1]; n2 = [sp.Rational(c) / qn[j] for c in q2]
        v = [sp.Rational(int(a), int(b)) for a, b in zip(rng.integers(-9, 10, 4), rng.integers(1, 6, 4))]
        Pp = (sp.eye(4) + Gdot(n1)) / 2; Pq = (sp.eye(4) + Gdot(n2)) / 2
        Pqm = (sp.eye(4) - Gdot(n2)) / 2
        J = Gdot(v)
        vv = sum(a * a for a in v); nv1 = sum(a * b for a, b in zip(n1, v)); nv2 = sum(a * b for a, b in zip(n2, v))
        nn = sum(a * b for a, b in zip(n1, n2))
        t_pp = sp.simplify((Pq * J * Pp * J).trace() - (vv * (1 - nn) + 2 * nv1 * nv2))
        t_pm = sp.simplify((Pqm * J * Pp * J).trace() - (vv * (1 + nn) - 2 * nv1 * nv2))
        okp &= (t_pp == 0); okm &= (t_pm == 0); cnt += 1
chk("A2 tr(P+ J P+ J)=|v|^2(1-n.n')+2(n.v)(n'.v) and tr(P- J P+ J)=|v|^2(1+n.n')-2(n.v)(n'.v), exact, %d cases" % cnt, okp and okm)

# A3 bookkeeping of the calibrated shift: naive vs additive-mass-subtracted, and group velocity
E, M, p, K, dE0, c2 = sp.symbols('E M p K dE0 c2', positive=True)
Ep = sp.sqrt(M ** 2 + p ** 2)
dEcal = K * p ** 2 / Ep                            # form implied by a pure shift of the p^2 coefficient
# E_cal = E+e^2 dEcal ; E_cal^2 = M^2+p^2+2 e^2 K p^2  ==> delta(c^2)=2 e^2 K  (exact to first order in e^2)
first_order = sp.simplify(sp.diff(sp.sqrt(M ** 2 + p ** 2 + 2 * sp.Symbol('g') * K * p ** 2), sp.Symbol('g')).subs(sp.Symbol('g'), 0) - dEcal)
vg = sp.simplify(sp.diff(dEcal, p))
lim = sp.limit(vg / K, M, 0, '+')
chk("A3a first-order shift of E^2=M^2+(1+2e^2K)p^2 equals K p^2/E, group-velocity shift -> K as M/p->0 (exact)",
    first_order == 0 and sp.simplify(lim - 1) == 0)
chk("A3b without the additive-mass counterterm the apparent K changes by M*dE(0)/p^2 (exact identity)",
    sp.simplify((Ep * sp.Symbol('dEp') / p ** 2) - ((Ep * sp.Symbol('dEp') - M * dE0) / p ** 2) - M * dE0 / p ** 2) == 0)

# A4 exact angular integrals for the continuum log coefficients (Feynman gauge, photon Lorentz invariant,
#    fermion speed c).  Euclidean: Gamma = g0 p0 (1+e^2 z_t) + c g.p (1+e^2 z_s) ; coefficients of ln(Lambda/mu).
th, c = sp.symbols('theta c', positive=True)
k0, kv2 = sp.cos(th), sp.sin(th) ** 2
Q = k0 ** 2 + c ** 2 * kv2
Ft = (1 - 3 * c ** 2) * (1 / Q - 2 * k0 ** 2 / Q ** 2)
Fs = -c * (1 + c ** 2) * (1 / Q - sp.Rational(2, 3) * c ** 2 * kv2 / Q ** 2)
meas = 4 * sp.pi * sp.sin(th) ** 2
def angint(expr):
    return sp.integrate(sp.expand(sp.simplify(expr * meas)), (th, 0, sp.pi))
norm = (2 * sp.pi) ** 4
zt1 = sp.simplify(-angint(Ft.subs(c, 1)) / norm)
zs1 = sp.simplify(-angint((Fs / c).subs(c, 1)) / norm)
chk("A4a at c=1 z_t=z_s=1/(8 pi^2) (Feynman-gauge Z2, exact)", zt1 == sp.Rational(1, 8) / sp.pi ** 2 and zs1 == zt1)
# direct: D(c)=z_s-z_t = (-int(Fs/c) + int(Ft))/norm ; differentiate under the integral sign (integrand rational in cos, sin)
dD = sp.simplify(sp.integrate(sp.expand(sp.simplify(sp.diff(-(Fs / c) + Ft, c).subs(c, 1) * meas)), (th, 0, sp.pi)) / norm)
chk("A4b d(z_s-z_t)/dc at c=1 equals -1/(3 pi^2) (exact)  [electron speed runs toward the photon speed]",
    sp.simplify(dD + 1 / (3 * sp.pi ** 2)) == 0, "value=%s" % dD)

# A5 photon speed induced by a Dirac loop with fermion speed c: rescaling x=c x' gives (E^2/c - c B^2) kappa/2
kap, cc = sp.symbols('kappa cc', positive=True)
cgam2 = (1 + kap * cc) / (1 + kap / cc)
dgam = sp.series(sp.sqrt(cgam2), kap, 0, 2).removeO().coeff(kap, 1)
chk("A5a photon speed shift = kappa*(c-1) to first order in kappa, kappa=e^2 ln(Lambda/mu)/(6 pi^2)  [continuum, textbook coefficient e^2/(12 pi^2) per ln Lambda^2 ASSUMED]",
    sp.simplify(dgam.subs(cc, c) - (c - 1 / c) / 2) == 0 and sp.simplify(sp.diff((c - 1 / c) / 2, c).subs(c, 1) - 1) == 0)
mism = sp.simplify(-(dD * sp.pi ** 2) + sp.Rational(1, 6))          # (1/3 + 1/6) / pi^2 ... in units 1/pi^2
chk("A5b mismatch (c_e-c_gamma) decays as 1-(e^2/(2 pi^2)) ln(Lambda/mu): coefficient 1/3+1/6=1/2 (exact)", sp.simplify(mism - sp.Rational(1, 2)) == 0)

# A6 local mismatch arithmetic from the landed coefficients (supplied numbers)
Df, Dg, Cw = [Fraction(str(x)) for x in (LANDED_DELTA_F, LANDED_DELTA_GAMMA, LANDED_CW)]
dA = Df - Dg / 2                    # setting a=1  : (c_e - c_gamma)/e^2
dB = dA + Cw / 2                    # setting a^2=1-m_bare through the critical mass
e2 = 4 * np.pi / ALPHA_INV
chk("A6 local relative-speed signs: a=1 -> c_e<c_gamma (photon pair decay side), bare curve -> c_e>c_gamma (electron Cherenkov side); both nonzero",
    dA < 0 < dB, "dA/e^2=%.10f dB/e^2=%.10f ; c_e-c_gamma = %.6f , %.6f" % (float(dA), float(dB), float(dA) * e2, float(dB) * e2))
# robustness of the signs against an error xi (in units of e^2) of the photon term X'=Dg/2+xi: A needs xi > -|dA|, B needs xi < dB
chk("A6b sign of c_e-c_gamma is unchanged for any photon-term error xi (units e^2) with  -%.4f < xi (setting a=1)  and  xi < %.4f (bare curve); the on-shell photon term has not been computed" % (abs(float(dA)), float(dB)),
    abs(float(dA)) > 0.1 and float(dB) > 0.04 and abs(float(dA) + float(Dg) / 2 - float(Df)) < 1e-12)
cB = 1 + float(dB) * e2; cA = 1 + float(dA) * e2
kstarA = 2 / np.sqrt(2 * abs(float(dA)) * e2)     # in units of M
pstarB = 1 / np.sqrt(2 * float(dB) * e2)
chk("A6c thresholds in the local EFT (prepass formulas): photon pair edge k*=%.2f M (a=1), electron Cherenkov p*=%.2f M (curve), cutoff independent" % (kstarA, pstarB),
    9 < kstarA < 16 and 8 < pstarB < 14)


# =============================================================================================
# quadrature on the torus: 24 cube sectors, k=(t, t u, t v) in the sector, weight t^2 / (2 pi)^3
# =============================================================================================
def gl(n):
    z, w = leggauss(n)
    return (z + 1) / 2, w / 2


def nodes(breaks, n, nr, tmin=0.0, tmax=np.pi, axis_gamma=1.0):
    u0, wu0 = gl(n); zr, wr = gl(nr)
    blocks = []
    if tmin == 0.0:
        br = [b for b in breaks if b < tmax]
        edges = [0.0] + br + [tmax]
        blocks.append((edges[1] * zr, edges[1] * wr))
        for a_, c_ in zip(edges[1:-1], edges[2:]):
            L = np.log(c_ / a_); t = a_ * np.exp(L * zr); blocks.append((t, t * L * wr))
    else:
        br = [b for b in breaks if tmin < b < tmax]
        edges = [tmin] + br + [tmax]
        for a_, c_ in zip(edges[:-1], edges[1:]):
            L = np.log(c_ / a_); t = a_ * np.exp(L * zr); blocks.append((t, t * L * wr))
    for t, wt in blocks:
        for imax in range(3):
            for signs in product([-1, 1], repeat=3):
                if imax == 0 and signs[0] == 1 and axis_gamma != 1.0:
                    g = axis_gamma; U = u0 ** g; WU = g * u0 ** (g - 1) * wu0; V, WV = U, WU
                else:
                    U, WU, V, WV = u0, wu0, u0, wu0
                tt, uu, vv = np.meshgrid(t, U, V, indexing='ij')
                ww = (wt[:, None, None] * WU[None, :, None] * WV[None, None, :] * tt ** 2).ravel() / (2 * np.pi) ** 3
                base = np.stack([tt.ravel(), (tt * uu).ravel(), (tt * vv).ravel()], axis=1)
                yield np.roll(base, imax, axis=1) * np.array(signs), ww


# ---------------------------------------------------------------------------------------------
# B. Euclidean local coefficient z_s - z_t at positive bare IR regulator m (landed eq. (15))
# ---------------------------------------------------------------------------------------------
def fF(k, m):
    c_ = np.cos(k); s_ = np.sin(k); W = np.sum(2 * np.sin(k / 2) ** 2, axis=1); Mm = m + W
    E2 = np.sum(s_ * s_, axis=1) + Mm * Mm; E_ = np.sqrt(E2); om = np.sqrt(2 * W)
    I1 = 1 / (2 * E_ * om * (E_ + om)); I2 = (2 * E_ + om) / (4 * E_ ** 3 * om * (E_ + om) ** 2)
    A = 1 - 2 * c_ * c_ + 3 * c_ - 2 * Mm[:, None] * c_
    B = 2 * s_ * s_ * (Mm[:, None] - 3 + c_) * (Mm[:, None] + c_)
    zt_ = -2 * I1 + 4 * E2 * I2
    zs_ = A.mean(axis=1) * I1 + B.mean(axis=1) * I2 - 1 / (4 * om)
    return zs_ - zt_


def zdiff(m, n=24, nr=48, t0=None):
    tot = 0.0
    for k, w in nodes([max(m, 1e-9) if t0 is None else t0], n, nr):
        tot += np.sum(w * fF(k, m))
    return tot


mass0 = zdiff(0.0, t0=1e-7)
conv = 1 / (24 * np.pi ** 2)
chk("B1 independent quadrature reproduces the landed massless integral to 1e-11", abs(mass0 - LANDED_MASSLESS_FF) < 1e-11, "%.14f" % mass0)
chk("B2 massless integral + 1/(24 pi^2) reproduces landed Delta_f to 2e-10", abs(mass0 + conv - LANDED_DELTA_F) < 2e-10, "%.12f" % (mass0 + conv))
Df_num = mass0 + conv
okB = True; prev = None; rows = []
for m in [1e-3, 1e-4, 1e-5, 1e-6]:
    d = zdiff(m) - Df_num
    rows.append((m, d))
    okB &= (abs(d) <= 0.03 * m * np.log(1 / m))
chk("B3 Euclidean z_s-z_t(m) -> Delta_f with |remainder| <= 0.03 m ln(1/m) (m=1e-3..1e-6)", okB,
    "; ".join("m=%g:%.2e" % r for r in rows))


# =============================================================================================
# C. on-shell calibrated shift
# =============================================================================================
def parts(k, p_, m, a, gauge):
    sp_ = a * np.sin(p_); cp = np.cos(p_); Wp = np.sum(2 * np.sin(p_ / 2) ** 2); Mp = m + Wp
    Ep_ = np.sqrt(sp_ @ sp_ + Mp * Mp); npv = np.r_[sp_, Mp] / Ep_
    q = p_ - k; sq = a * np.sin(q); Mq = m + np.sum(2 * np.sin(q / 2) ** 2, axis=1)
    Eq = np.sqrt(np.sum(sq * sq, axis=1) + Mq * Mq)
    nq = np.column_stack([sq, Mq]) / Eq[:, None]; dot = nq @ npv
    hk = 2 * np.sin(k / 2); om = np.sqrt(np.sum(hk * hk, axis=1)); kh = hk / om[:, None]
    ca = a * np.cos(p_ - k / 2); sa = np.sin(p_ - k / 2)
    bp = ca * npv[:3] + sa * npv[3]; bq = ca * nq[:, :3] + sa * nq[:, 3, None]
    sea_vec = -npv[:3] * sp_ + npv[3] * cp
    if gauge == 'feynman':
        C3 = np.sum(ca * ca + sa * sa, axis=1); bb = np.sum(bp * bq, axis=1)
        splus = C3 * (1 - dot) + 2 * bb - (1 + dot)
        sminus = C3 * (1 + dot) - 2 * bb - (1 - dot)
        sea = np.sum(sea_vec) / (4 * om); coul = np.zeros_like(om)
    else:
        cV = np.sum(ca * ca * (1 - kh * kh), axis=1) + np.sum(sa * sa, axis=1) - np.sum(sa * kh, axis=1) ** 2
        bpbq = np.sum(bp * bq, axis=1) - np.sum(bp * kh, axis=1) * np.sum(bq * kh, axis=1)
        splus = cV * (1 - dot) + 2 * bpbq; sminus = cV * (1 + dot) - 2 * bpbq
        sea = np.sum((1 - kh * kh) * sea_vec, axis=1) / (4 * om); coul = dot / (2 * om * om)
    den = Ep_ - Eq - om
    exch = (splus / den + sminus / (Ep_ + Eq + om)) / (4 * om)
    return sea, coul, exch, Ep_, Mp, den


def onshell(m, x, a2=1.0, n=16, nr=32, gauge='feynman', pdir=(1., 0., 0.), axis_gamma=3.0, tmin=0.0, tmax=np.pi):
    a = np.sqrt(a2); pd = np.array(pdir, float); pd /= np.linalg.norm(pd); p_ = m * x * pd
    br = sorted(set([m] + ([m * x] if x > 1 else [])))
    accE = 0.0; rest = 0.0; acc = 0.0; naive = 0.0; maxden = -1e9; zero = np.zeros(3)
    parts_rest = np.zeros(3)
    for k, w in nodes(br, n, nr, tmin=tmin, tmax=tmax, axis_gamma=axis_gamma):
        A = parts(k, p_, m, a, gauge); B = parts(k, zero, m, a, gauge)
        maxden = max(maxden, A[5].max())
        sa_ = A[0] + A[1] + A[2]; sb_ = B[0] + B[1] + B[2]
        acc += np.sum(w * sa_); rest += np.sum(w * sb_)
        naive += np.sum(w * sa_ * A[3])
        accE += np.sum(w * (sa_ * A[3] - sb_ * A[4]))
        for j in range(3):
            parts_rest[j] += np.sum(w * B[j])
    pp = p_ @ p_
    return dict(K=accE / pp, Knaive=naive / pp, shift=acc, rest=rest, maxden=maxden, parts_rest=parts_rest,
                Mp=m + np.sum(2 * np.sin(p_ / 2) ** 2), pp=pp)


# C1 gauge equality for several bare cone speeds
okG = True; det = []
for a2 in [1.0, 0.99, 0.9767, 0.9]:
    rf = onshell(1e-3, 2.0, a2, gauge='feynman'); rc = onshell(1e-3, 2.0, a2, gauge='coulomb')
    d = abs(rf['K'] - rc['K']); okG &= d < 1e-8 and abs(rf['rest'] - rc['rest']) < 1e-9
    det.append("a2=%g:%.1e" % (a2, d))
chk("C1 Feynman-gauge (3 pol. - temporal) and Coulomb-gauge (2 pol. + instantaneous) calibrated shifts agree for a^2 in {1,.99,.9767,.9}, tol 1e-8", okG, " ".join(det))

# C2 rest shift reproduces the landed C_W and the landed Feynman split (m -> 0)
r0 = onshell(1e-7, 1.0, 1.0, n=20, nr=40)
chk("C2 rest-energy shift dE(0) at m=1e-7 equals landed C_W to 1e-5 (including Feynman split)",
    abs(r0['rest'] - LANDED_CW) < 1e-5 and abs(r0['parts_rest'][0] - LANDED_CW_FEYN_SPLIT[0]) < 1e-5
    and abs(r0['parts_rest'][2] - LANDED_CW_FEYN_SPLIT[1]) < 1e-5,
    "rest=%.9f seagull=%.9f exchange=%.9f" % (r0['rest'], r0['parts_rest'][0], r0['parts_rest'][2]))

# C3 quadrature self-convergence + convergence to the local coefficient with an explicit remainder law
okC = True; rows = []; Ks = {}
for m in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
    r16 = onshell(m, 2.0, 1.0, n=16, nr=32); r24 = onshell(m, 2.0, 1.0, n=24, nr=40)
    Ks[m] = r24['K']
    d = r24['K'] - Df_num
    okC &= abs(r24['K'] - r16['K']) < 1e-7 and abs(d) <= 0.06 * m * np.log(1 / m) and r24['maxden'] < 0
    rows.append("m=%g:%.2e" % (m, d))
r32 = onshell(1e-6, 2.0, 1.0, n=32, nr=48)['K']
okC &= abs(r32 - Ks[1e-6]) < 2e-8
chk("C3 K(m,x=2) -> Delta_f with |K-Delta_f| <= 0.06 m ln(1/m); quadrature orders 16/24/32 agree (<=1e-7, <=2e-8 at m=1e-6); denominators negative", okC, "; ".join(rows) + "; |K32-K24|(1e-6)=%.1e" % abs(r32 - Ks[1e-6]))
chk("C3b remainder decreases monotonically with m", all(abs(Ks[a] - Df_num) > abs(b - Df_num) for a, b in zip([1e-2, 1e-3, 1e-4, 1e-5], [Ks[1e-3], Ks[1e-4], Ks[1e-5], Ks[1e-6]])))

# C4 p/m independence inside the stable window (group velocity = K)
Kx = [onshell(1e-4, x, 1.0, n=24, nr=40)['K'] for x in [1, 4, 16, 64]]
chk("C4 K(m=1e-4,x) is flat in x=1..64 (spread < 5e-6): shift is a pure p^2/E term, group-velocity shift = K", max(Kx) - min(Kx) < 5e-6,
    "spread=%.2e" % (max(Kx) - min(Kx)))

# C5 necessity of the additive-mass counterterm (numerical)
rr = onshell(1e-3, 2.0, 1.0)
chk("C5 without the counterterm the apparent K is %.1f (identity K_naive-K=M*dE(0)/p^2 holds to 1e-9)" % rr['Knaive'],
    abs((rr['Knaive'] - rr['K']) - rr['Mp'] * rr['rest'] / rr['pp']) < 1e-9 * abs(rr['Knaive']) and abs(rr['Knaive']) > 50 * abs(rr['K']))


# =============================================================================================
# D. hard / soft decomposition of the on-shell shift  (cube max-norm split at t=eps)
# =============================================================================================
m = 1e-6
tot = onshell(m, 2.0, 1.0, n=20, nr=40)['K']
okD = True; rows = []
for eps in [0.003, 0.01, 0.03]:
    soft = onshell(m, 2.0, 1.0, n=20, nr=40, tmax=eps)['K']
    hard = onshell(m, 2.0, 1.0, n=20, nr=40, tmin=eps, axis_gamma=1.0)['K']
    okD &= abs(soft - conv) <= 0.05 * eps ** 2 + 1e-6 and abs(hard - mass0) <= 0.05 * eps ** 2 + 1e-6 and abs(soft + hard - tot) < 1e-8
    rows.append("eps=%g: soft-1/(24pi^2)=%.1e hard-massless=%.1e" % (eps, soft - conv, hard - mass0))
chk("D1 on-shell shift = [massless hard Euclid integral over t>=eps] + [soft region t<eps = 1/(24 pi^2)] with O(eps^2) remainders (m=1e-6, p=2m)", okD, "; ".join(rows))
spread = [onshell(m, x, 1.0, n=20, nr=40, tmax=0.01)['K'] for x in [0.5, 2.0, 8.0, 32.0]]
chk("D2 the soft constant is independent of p/M (x=0.5..32) to 2e-6: it is not a regulator artifact", max(spread) - min(spread) < 2e-6,
    "spread=%.1e" % (max(spread) - min(spread)))


# =============================================================================================
# E. infrared meaning: energy IR finite, residue log divergent with the standard exponent in Coulomb gauge
# =============================================================================================
s1 = onshell(1e-6, 2.0, 1.0, n=20, nr=40, tmax=1e-9)['K'] * 1.0
s2 = onshell(1e-6, 2.0, 1.0, n=20, nr=40, tmax=1e-8)['K'] * 1.0
chk("E1 energy-shift contribution of photons with |k|_max<eps scales linearly in eps for eps<<p,M (eps=1e-9 vs 1e-8, p=2M=2e-6): IR-finite at order e^2",
    abs(s2 / s1 - 10) < 0.05 and abs(s2) < 1e-3 * abs(Df_num), "ratio=%.4f, soft(1e-8)/K=%.1e (K-normalised)" % (s2 / s1, s2 / Df_num))


def shell_nodes(lo, hi, n=20, nr=24):
    u, wu = gl(n); zr, wr = gl(nr); L = np.log(hi / lo); t = lo * np.exp(L * zr); wt = t * L * wr
    for imax in range(3):
        for signs in product([-1, 1], repeat=3):
            tt, uu, vv = np.meshgrid(t, u, u, indexing='ij')
            ww = (wt[:, None, None] * wu[None, :, None] * wu[None, None, :] * tt ** 2).ravel() / (2 * np.pi) ** 3
            base = np.stack([tt.ravel(), (tt * uu).ravel(), (tt * vv).ravel()], axis=1)
            yield np.roll(base, imax, axis=1) * np.array(signs), ww


def residue_slope(m, x, gauge, lo=1e-9, hi=1e-8):
    p_ = np.array([m * x, 0., 0.]); tot_ = 0.0
    for k, w in shell_nodes(lo, hi):
        sp_ = np.sin(p_); Wp = np.sum(2 * np.sin(p_ / 2) ** 2); Mp = m + Wp
        Ep_ = np.sqrt(sp_ @ sp_ + Mp * Mp); npv = np.r_[sp_, Mp] / Ep_
        q = p_ - k; sq = np.sin(q); Mq = m + np.sum(2 * np.sin(q / 2) ** 2, axis=1)
        Eq = np.sqrt(np.sum(sq * sq, axis=1) + Mq * Mq)
        nq = np.column_stack([sq, Mq]) / Eq[:, None]; dot = nq @ npv
        hk = 2 * np.sin(k / 2); om = np.sqrt(np.sum(hk * hk, axis=1)); kh = hk / om[:, None]
        ca = np.cos(p_ - k / 2); sa = np.sin(p_ - k / 2)
        bp = ca * npv[:3] + sa * npv[3]; bq = ca * nq[:, :3] + sa * nq[:, 3, None]
        if gauge == 'feynman':
            C3 = np.sum(ca * ca + sa * sa, axis=1)
            splus = C3 * (1 - dot) + 2 * np.sum(bp * bq, axis=1) - (1 + dot)
        else:
            cV = np.sum(ca * ca * (1 - kh * kh), axis=1) + np.sum(sa * sa, axis=1) - np.sum(sa * kh, axis=1) ** 2
            splus = cV * (1 - dot) + 2 * (np.sum(bp * bq, axis=1) - np.sum(bp * kh, axis=1) * np.sum(bq * kh, axis=1))
        den = Ep_ - Eq - om
        tot_ += np.sum(w * splus / (4 * om * den ** 2))
    return tot_ / np.log(hi / lo)


okE = True; rows = []
for x in [1.0, 3.0, 10.0]:
    mm = 1e-3; pp_ = mm * x
    Etr = np.sqrt(np.sin(pp_) ** 2 + (mm + 1 - np.cos(pp_)) ** 2)
    vg = (np.sin(pp_) * np.cos(pp_) + (mm + 1 - np.cos(pp_)) * np.sin(pp_)) / Etr      # lattice group velocity
    pred = (1 / (2 * np.pi ** 2)) * ((1 / (2 * vg)) * np.log((1 + vg) / (1 - vg)) - 1)
    sc = residue_slope(mm, x, 'coulomb'); okE &= abs(sc / pred - 1) < 0.01
    rows.append("x=%g ratio=%.4f" % (x, sc / pred))
chk("E2 Coulomb-gauge residue slope d(dZ)/d ln(1/lambda) equals the infraparticle exponent (1/2pi^2)[ln((1+v)/(1-v))/(2v)-1] at the lattice group velocity, tol 1%", okE, "; ".join(rows))
sf = residue_slope(1e-3, 3.0, 'feynman'); sc = residue_slope(1e-3, 3.0, 'coulomb')
chk("E3 the residue's IR log is gauge dependent (Feynman %.4f vs Coulomb %.4f per e-fold) while the energy shift is not (C1): no isolated finite-residue pole, but E(p) and its derivative are defined" % (sf, sc),
    abs(sf - sc) > 0.05 * abs(sc))


# =============================================================================================
# F. cone mismatch (a^2 = 1 - eta): the 'floating on-shell trend' is the continuum log running
# =============================================================================================
mp.mp.dps = 25
def D_of_c(cv):
    f = lambda expr: sp.lambdify(th, expr.subs(c, cv), 'mpmath')
    ft, fs = f(Ft), f(Fs)
    zt_ = -mp.quad(lambda t: ft(t) * 4 * mp.pi * mp.sin(t) ** 2, [0, mp.pi]) / (2 * mp.pi) ** 4
    zs_ = -mp.quad(lambda t: fs(t) * 4 * mp.pi * mp.sin(t) ** 2, [0, mp.pi]) / cv / (2 * mp.pi) ** 4
    return zs_ - zt_

xs = np.array([10, 31.6228, 100, 316.228, 1000, 3162.28, 10000.0])
okF = True; rows = []
for eta in [0.02, 0.05]:
    a2 = 1 - eta; cv = mp.sqrt(a2)
    Kv = np.array([onshell(1e-7, x, a2, n=24, nr=40)['K'] for x in xs])
    X = np.vstack([np.ones(len(xs)), np.log(xs), 1 / xs ** 2]).T
    sol = np.linalg.lstsq(X[1:], Kv[1:], rcond=None)[0]
    pred = float(-cv ** 2 * D_of_c(cv))
    okF &= abs(sol[1] / pred - 1) < 0.01
    rows.append("eta=%g: fitted dK/dln(p/M)=%.6e predicted -c^2 D(c)=%.6e ratio=%.4f" % (eta, sol[1], pred, sol[1] / pred))
chk("F1 lattice on-shell dK/d ln(p/M) = -c^2 D(c) (continuum Feynman-gauge log coefficient) within 1% for eta=0.02,0.05", okF, "; ".join(rows))
Ka1 = np.array([onshell(1e-5, x, 1.0, n=24, nr=40)['K'] for x in [1, 10, 100, 300]])
chk("F2 for a=1 (no tree mismatch) there is no p/M trend: |dK/d ln x| < 1e-6 over x=1..300", abs(Ka1[-1] - Ka1[0]) / np.log(300) < 1e-6,
    "K(1)-K(300)=%.2e" % (Ka1[0] - Ka1[-1]))
# sensitivity of K to the unperturbed cone speed: its own log slope is again the continuum coefficient
def dK_da2(mm):
    Kq = [onshell(mm, 2.0, a2_, n=24, nr=40)['K'] for a2_ in (1.0, 0.99, 0.98)]
    return 0.5 * ((Kq[1] - Kq[0]) / -0.01 + (Kq[2] - Kq[1]) / -0.01), Kq
sA, KqA = dK_da2(1e-3); sB, KqB = dK_da2(1e-5)
logslope = (sB - sA) / np.log(100.0)
pred_ls = -1 / (6 * np.pi ** 2)
chk("F3 dK/d(a^2) = %.4f (m=1e-3), %.4f (m=1e-5): its slope per e-fold of ln(1/m) is %.5f vs continuum -1/(6 pi^2)=%.5f (within 3%%); i.e. the O(e^4) feedback of the cone shift is itself the leading-log running" % (sA, sB, logslope, pred_ls),
    abs(logslope / pred_ls - 1) < 0.03)


# =============================================================================================
# G. domain of the fixed-order expansion
# =============================================================================================
ok_stab = True
for x in [3.0, 3000.0, 10000.0]:
    r = onshell(1e-7, x, 0.9767, n=16, nr=32); ok_stab &= r['maxden'] < 0
chk("G1 for a^2=0.9767 (net-subluminal organization) all emission denominators stay negative up to p/M=1e4 (stable-branch expansion is uniform in p/M)", ok_stab)
mq = 1e-4
neg = onshell(mq, 60, 1.0, n=24, nr=40, pdir=(1, 1, 1), axis_gamma=1.0)['maxden']
pos = onshell(mq, 150, 1.0, n=24, nr=40, pdir=(1, 1, 1), axis_gamma=1.0)['maxden']
pos2 = onshell(mq, 150, 1.0, n=24, nr=40, pdir=(1, 1, 0), axis_gamma=1.0)['maxden']
axis = onshell(mq, 150, 1.0, n=16, nr=32)['maxden']
chk("G2 for a=1 the tree electron radiates off-axis for |p| >~ sqrt(m) (denominator turns positive: |p|=0.6 sqrt(m): %.1e, 1.5 sqrt(m): %.1e/%.1e) -- the fixed-order O(e^2) coefficient is not defined there; the axis stays marginal (%.1e)" % (neg, pos, pos2, axis),
    neg < 0 and pos > 0 and pos2 > 0 and axis < 0)
sup = onshell(1e-4, 10.0, 1.0 + float(Cw) * e2, n=16, nr=32)['maxden']
chk("G3 for the bare-curve setting (a^2 = 1+e^2 C_W = %.4f) the tree electron is superluminal on the axis (denominator > 0: %.1e): real-energy fixed order fails; width must be computed" % (1 + float(Cw) * e2, sup), sup > 0)

# =============================================================================================
n_pass = sum(RESULTS); n_fail = len(RESULTS) - n_pass
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
if n_fail == 0:
    print("HIT: electron-sector bridge at order e^2 shown on the lattice: calibrated on-shell shift = massless hard integral + physical soft constant 1/(24 pi^2) (O(eps^2) remainders), gauge-equal for all cone speeds, remainder <= 0.06 m ln(1/m); p/M trend for a!=1 is the continuum log running -c^2 D(c) (D'(1)=-1/(3 pi^2), mismatch rate e^2/(2 pi^2) with photon half assumed); fixed order ends at |p|~sqrt(M) off-axis; photon-sector bridge NOT done")
print("SUMMARY: For the electron sector at order e^2, the gauge-independent, mass-calibrated on-shell shift equals the landed local coefficient Delta_f (hard massless integral + 1/(24 pi^2) soft constant) with a computed O(m ln m) remainder, its p/M trend at nonzero cone mismatch is the continuum log running (so the local number is the cutoff-scale value, not the physical low-energy one), and the fixed-order expansion's domain ends at |p|~sqrt(M); the photon-side on-shell bridge and e^4 non-log remainders remain open (runtime %.0f s)." % (time.time() - T0))
sys.exit(0 if n_fail == 0 else 1)
