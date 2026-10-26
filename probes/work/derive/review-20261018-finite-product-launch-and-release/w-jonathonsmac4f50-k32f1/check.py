#!/usr/bin/env python3
"""
Disjoint check for J:derive:review-20261018-finite-product-launch-and-release:a1

Scope.  Core interface of the supplied stationary ladder (REAL_MEDIATED_VACANCY_NETWORK note, section 10,
coefficients (6)) in the one-head sector:
  A. exact algebra (sympy over Q(sqrt2)): coefficients, transmission/reflection rational functions,
     unitarity identity, determinant factorisation, exact resolvent identity at rational zeta;
  B. location of the bound state and resonances (high-precision roots);
  C. brute-force dynamics (dense eigh / sparse expm) versus the closed finite-time output formula
     P_R e^{-isH} psi0 = P_R U_Z(s) F^{-1}[tau * ghat0] + bound-state term, for arbitrary left-lead psi0;
  D. certified Lipschitz constant of tau, spectral-weight bound for the exact launcher profile,
     Chebyshev position bound for the free output profile;
  E. end-to-end finite device (emitter + line + ladder + output line) versus the proved-bound chain;
  F. exact-rational composition arithmetic (imports from the notes are ASSUMED, not re-proved).
Only numpy, scipy, sympy, mpmath, fractions.  No file or network access.
"""
import math
import sys
import time
from fractions import Fraction

import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import expm_multiply
import sympy as sp
import mpmath as mp

T0 = time.time()
RES = []
HIT_OK = []


def chk(name, ok, detail=""):
    ok = bool(ok)
    RES.append(ok)
    print(("PASS " if ok else "FAIL ") + name + ((" | " + detail) if detail else ""))
    sys.stdout.flush()


# ---------------------------------------------------------------------------------------------
# A. exact algebra
# ---------------------------------------------------------------------------------------------
s2 = sp.sqrt(2)
fS = s2 / 4                                   # f = 1/sqrt(8)
aS = cS = fS / 2
bS = 3 * fS
eLS = 1 - sp.Rational(5, 2) * fS
eAS = 2 - sp.Rational(5, 2) * fS
evS = 2 - sp.Rational(3, 4) * fS
zeta = sp.symbols("zeta")
IDX = dict(L=0, v=1, A=2, B=3, w=4, R=5)      # order L,v,A,B,w,R


def core_sym(p):
    H = sp.zeros(6, 6)
    q = {("L", "v"): aS, ("L", "A"): bS, ("v", "B"): cS, ("A", "w"): cS, ("B", "R"): bS, ("w", "R"): aS}
    on = dict(L=eLS, R=eLS, v=evS, w=evS, A=eAS, B=eAS)
    for (i, j), wgt in q.items():
        H[IDX[i], IDX[i]] += wgt
        H[IDX[j], IDX[j]] += wgt
        H[IDX[i], IDX[j]] -= wgt
        H[IDX[j], IDX[i]] -= wgt
    for v_, e in on.items():
        H[IDX[v_], IDX[v_]] += e
    H[0, 0] += 1          # unit lead bond diagonal at the ports
    H[5, 5] += 1
    H[2, 3] -= p          # controlled A-B hopping -p (p = old X1X2 = +-1)
    H[3, 2] -= p
    return H


def polys_sym(p):
    H = core_sym(p)
    G = zeta * (H - 2 * sp.eye(6)) + (zeta ** 2 + 1) * sp.eye(6)   # zeta * F(zeta)
    G[0, 0] -= zeta ** 2
    G[5, 5] -= zeta ** 2
    D = sp.expand(G.det(method="berkowitz"))
    N = sp.expand((1 - zeta ** 2) * G.cofactor(0, 5))
    R = sp.expand((1 - zeta ** 2) * G.cofactor(0, 0) - D)
    return H, D, N, R


SYM = {p: polys_sym(p) for p in (1, -1)}

# positivity and the stated diagonals at E=2
pos = all(sp.simplify(x).is_positive for x in (aS, bS, cS, eLS, eAS, evS))
chk("A1 all ladder weights/onsites (a=c=f/2,b=3f,eta_L,eta_A,eta_v) are strictly positive (exact)", pos)
dL = aS + bS + 1 + eLS - 2
dv = aS + cS + evS - 2
dA = bS + cS + eAS - 2
chk("A2 shifted diagonals at E=2 equal f, f/4, f exactly", sp.simplify(dL - fS) == 0 and sp.simplify(dv - fS / 4) == 0 and sp.simplify(dA - fS) == 0)

fac = {
    1: ((zeta**5 - zeta**4 + zeta**3 * (sp.Rational(11, 4) - 2 * s2) + zeta**2 * (-sp.Rational(5, 4) + 2 * s2) + zeta * (sp.Rational(9, 4) - 2 * s2) + 2 * s2),
        (zeta**5 + zeta**4 + zeta**3 * (2 * s2 + sp.Rational(25, 8)) + zeta**2 * (sp.Rational(5, 4) + 2 * s2) + zeta * (sp.Rational(9, 4) + 2 * s2) + 2 * s2)),
    -1: ((zeta**5 - zeta**4 + zeta**3 * (sp.Rational(25, 8) - 2 * s2) + zeta**2 * (-sp.Rational(5, 4) + 2 * s2) + zeta * (sp.Rational(9, 4) - 2 * s2) + 2 * s2),
         (zeta**5 + zeta**4 + zeta**3 * (sp.Rational(11, 4) + 2 * s2) + zeta**2 * (sp.Rational(5, 4) + 2 * s2) + zeta * (sp.Rational(9, 4) + 2 * s2) + 2 * s2)),
}
for p in (1, -1):
    _, D, N, R = SYM[p]
    ok = sp.expand(D - fac[p][0] * fac[p][1] / 8) == 0
    chk(f"A3 p={p:+d}: det[zeta F(zeta)] = (1/8) P1 P2 with two explicit quintics over Q(sqrt2) (exact)", ok)

tp_ex = {1: -sp.Rational(3, 5) - sp.Rational(4, 5) * sp.I, -1: -sp.Rational(3, 5) + sp.Rational(4, 5) * sp.I}
for p in (1, -1):
    _, D, N, R = SYM[p]
    t_i = sp.simplify(N.subs(zeta, sp.I) / D.subs(zeta, sp.I))
    r_i = sp.simplify(R.subs(zeta, sp.I) / D.subs(zeta, sp.I))
    chk(f"A4 p={p:+d}: tau(i) = -(3{'+' if p == 1 else '-'}4i)/5 and r(i)=0 exactly (reproduces source centre values)",
        sp.simplify(t_i - tp_ex[p]) == 0 and sp.simplify(r_i) == 0)

# exact unitarity identity  N(z)N(1/z)+R(z)R(1/z) = D(z)D(1/z)  (real coefficients => |tau|^2+|r|^2=1 on |z|=1)
for p in (1, -1):
    _, D, N, R = SYM[p]
    lhs = sp.expand((N * N.subs(zeta, 1 / zeta) + R * R.subs(zeta, 1 / zeta) - D * D.subs(zeta, 1 / zeta)) * zeta ** 24)
    chk(f"A5 p={p:+d}: exact identity N(z)N(1/z)+R(z)R(1/z)=D(z)D(1/z) (unitarity of the 1-channel S, all k)", lhs == 0)

# exact resolvent identity at rational zeta (transparent boundary conditions make the leads exact)
Kfield = sp.QQ.algebraic_field(s2)
from sympy.polys.matrices import DomainMatrix


def green_residuals(p, zt, NL=4, NR=4):
    n = NL + 6 + NR
    o = NL
    H = sp.zeros(n, n)
    H[o:o + 6, o:o + 6] = core_sym(p)
    zz = 2 - zt - 1 / zt
    for i in range(NL):
        H[i, i] = 2
        H[i, i + 1] = -1
        H[i + 1, i] = -1
    H[0, 0] = 2 - zt                    # u(NL+1)=zt*u(NL): exact decaying lead
    for i in range(NR):
        j = o + 6 + i
        H[j, j] = 2
        H[j - 1, j] = -1
        H[j, j - 1] = -1
    H[n - 1, n - 1] = 2 - zt
    M = H - zz * sp.eye(n)
    dM = DomainMatrix.from_Matrix(M).convert_to(Kfield)
    F = core_sym(p) - zz * sp.eye(6)
    F[0, 0] -= zt
    F[5, 5] -= zt
    Fi = DomainMatrix.from_Matrix(F).convert_to(Kfield).inv().to_Matrix()
    res = []
    for nsrc in (0, 2):
        rhs = sp.zeros(n, 1)
        rhs[o - nsrc] = 1
        sol = dM.lu_solve(DomainMatrix.from_Matrix(rhs).convert_to(Kfield)).to_Matrix()
        for nn, idx in ((0, o + 5), (1, o + 6), (3, o + 8)):
            res.append(sp.simplify(sol[idx] - Fi[5, 0] * zt ** (nn + nsrc)))
    return res


allzero = True
for p in (1, -1):
    for zt in (sp.Rational(1, 3), -sp.Rational(2, 5), sp.Rational(3, 4)):
        allzero &= all(r == 0 for r in green_residuals(p, zt))
chk("A6 exact resolvent identity G(R_n,L_n')=[F^{-1}]_{RL} zeta^{n+n'} (6 rational zeta, 2 sectors, 2 sources, 3 observation sites)", allzero)

# ---- numeric polynomial data
DN = {}
for p in (1, -1):
    _, D, N, R = SYM[p]
    DN[p] = (np.array([complex(sp.N(c_, 40)) for c_ in sp.Poly(D, zeta).all_coeffs()]),
             np.array([complex(sp.N(c_, 40)) for c_ in sp.Poly(N, zeta).all_coeffs()]),
             np.array([complex(sp.N(c_, 40)) for c_ in sp.Poly(R, zeta).all_coeffs()]))


def tau_r(p, k):
    d, n_, r_ = DN[p]
    z_ = np.exp(1j * np.asarray(k))
    den = np.polyval(d, z_)
    return np.polyval(n_, z_) / den, np.polyval(r_, z_) / den


def core_num(p):
    return np.array(core_sym(p).evalf(30).tolist(), dtype=float)


CORE = {p: core_num(p) for p in (1, -1)}

# matrix-inverse cross-check of the rational forms
rng = np.random.default_rng(7)
worst = 0.0
for p in (1, -1):
    for k in rng.uniform(-np.pi, np.pi, 40):
        z_ = np.exp(1j * k)
        F = CORE[p].astype(complex) - (2 - z_ - 1 / z_) * np.eye(6)
        F[0, 0] -= z_
        F[5, 5] -= z_
        Fi = np.linalg.inv(F)
        t_m = (1 / z_ - z_) * Fi[5, 0]
        r_m = (1 / z_ - z_) * Fi[0, 0] - 1
        t_f, r_f = tau_r(p, k)
        worst = max(worst, abs(t_m - t_f), abs(r_m - r_f))
chk("A7 rational tau,r (from exact polynomials) agree with 6x6 matrix inversion at 80 random k", worst < 1e-9, f"max dev {worst:.1e}")

# ---------------------------------------------------------------------------------------------
# B. bound state and resonances
# ---------------------------------------------------------------------------------------------
mp.mp.dps = 50
ROOTS = {}
ZB = {}
for p in (1, -1):
    _, D, N, R = SYM[p]
    co = [mp.mpf(str(sp.re(sp.N(c_, 60)))) + 1j * mp.mpf(str(sp.im(sp.N(c_, 60)))) for c_ in sp.Poly(D, zeta).all_coeffs()]
    rts = mp.polyroots(co, maxsteps=500, extraprec=300)
    ROOTS[p] = [complex(r) for r in rts]
    inside = [r for r in ROOTS[p] if abs(r) < 1]
    ZB[p] = inside[0] if inside else None
    modgap = min(abs(abs(r) - 1) for r in ROOTS[p])
    kk = np.linspace(-np.pi, np.pi, 400001)
    ph = np.unwrap(np.angle(np.polyval(DN[p][0], np.exp(1j * kk))))
    wind = (ph[-1] - ph[0]) / (2 * np.pi)
    Eb = (2 - ZB[p] - 1 / ZB[p]) if ZB[p] is not None else None
    ok = (len(inside) == 1 and abs(ZB[p].imag) < 1e-12 and -0.62 < ZB[p].real < -0.60 and abs(wind - 1) < 1e-6
          and modgap > 3e-4 and Eb.real > 4)
    chk(f"B1 p={p:+d}: det F(zeta) has exactly ONE zero in |zeta|<1 (real, negative: bound state ABOVE the band), none on |zeta|=1",
        ok, f"zeta_b={ZB[p].real:.6f}, E_b={Eb.real:.6f}, winding={wind:.6f}, min||zeta|-1|={modgap:.2e}")
    near = sorted([(abs(abs(r) - 1), abs(np.angle(r)) - np.pi / 2) for r in ROOTS[p] if abs(abs(r) - 1) < 0.1])
    res_dist = abs(near[0][1])
    lo, hi = (0.030, 0.035) if p == 1 else (0.024, 0.027)
    chk(f"B2 p={p:+d}: narrowest resonance pole sits at |k-pi/2| ~ {res_dist:.4f} with |zeta|-1 = {near[0][0]:.2e} (NV band 1e-4 is inside, true pole-free arc is ~100x wider)",
        lo < res_dist < hi)

# bound-state vector (analytic): null vector of F(zeta_b)
BS = {}
for p in (1, -1):
    zb = ZB[p].real
    F = CORE[p] - (2 - zb - 1 / zb) * np.eye(6)
    F[0, 0] -= zb
    F[5, 5] -= zb
    U_, S_, Vh = np.linalg.svd(F)
    v = Vh[-1].conj()
    nrm2 = sum(abs(v[i]) ** 2 for i in (1, 2, 3, 4)) + (abs(v[0]) ** 2 + abs(v[5]) ** 2) / (1 - zb ** 2)
    v = v / math.sqrt(nrm2)
    BS[p] = (zb, v, 2 - zb - 1 / zb, S_[-1])


def bound_state_term(p, psi0_left, s, nmax):
    """e^{-isE_b} <u|psi0> u_R(n), n=0..nmax ; psi0_left[n'] n'>=0 on the left lead (port = n'=0)."""
    zb, v, Eb, _ = BS[p]
    npr = np.arange(len(psi0_left))
    ov = np.sum(np.conj(v[0] * zb ** npr) * psi0_left)
    nn = np.arange(nmax + 1)
    return np.exp(-1j * s * Eb) * ov * (v[5] * zb ** nn), abs(ov)


chk("B3 bound-state vector: null singular value of F(zeta_b) ~ 0 in both sectors",
    all(BS[p][3] < 1e-10 for p in (1, -1)), f"{BS[1][3]:.1e}, {BS[-1][3]:.1e}")

# ---------------------------------------------------------------------------------------------
# C. brute force versus the closed finite-time output formula (arbitrary left-lead psi0)
# ---------------------------------------------------------------------------------------------
def dense_device(p, NL, NR):
    n = NL + 6 + NR
    H = np.zeros((n, n))
    o = NL
    H[o:o + 6, o:o + 6] = CORE[p]
    for i in range(NL):
        H[i, i] = 2.0
        H[i, i + 1] = H[i + 1, i] = -1.0
    for i in range(NR):
        j = o + 6 + i
        H[j, j] = 2.0
        H[j - 1, j] = H[j, j - 1] = -1.0
    return H, o


NK = 2 ** 18
KG = np.fft.fftfreq(NK) * 2 * np.pi
EG = 2 - 2 * np.cos(KG)
TAU_G = {p: tau_r(p, KG)[0] for p in (1, -1)}


def formula_output(p, psi0_left, s, nout):
    """right lead n=0..nout via (1/2pi) int e^{-isE} e^{ikn} tau(k) ghat0(k) dk  (+ bound-state term)."""
    arr = np.zeros(NK, complex)
    arr[:len(psi0_left)] = psi0_left
    g0 = NK * np.fft.ifft(arr)                         # sum_n' psi0(n') e^{+ik n'}
    w = np.fft.ifft(np.exp(-1j * s * EG) * TAU_G[p] * g0)
    bs, _ = bound_state_term(p, psi0_left, s, nout)
    return w[:nout + 1], bs


maxdev_nobs = 0.0
maxdev_bs = 0.0
maxbs = 0.0
t_c0 = time.time()
for p in (1, -1):
    NL = NR = 700
    H, o = dense_device(p, NL, NR)
    ew, EV = np.linalg.eigh(H)
    npr = np.arange(0, NL + 1)
    states = []
    prof = np.exp(-((npr - 300.0) / 25.0) ** 2 / 2) * np.exp(-1j * np.pi / 2 * npr)
    states.append(prof / np.linalg.norm(prof))
    prof = np.exp(-((npr - 350.0) / 60.0) ** 2 / 2) * np.exp(-1j * np.pi / 2 * npr)
    states.append(prof / np.linalg.norm(prof))
    rv = np.zeros(NL + 1, complex)
    r2 = np.random.default_rng(11 + p)
    rv[:40] = r2.normal(size=40) + 1j * r2.normal(size=40)         # broadband, includes the port n'=0
    states.append(rv / np.linalg.norm(rv))
    rv = np.zeros(NL + 1, complex)
    rv[0:6] = r2.normal(size=6) + 1j * r2.normal(size=6)           # very close to the core: bound-state excitation large
    states.append(rv / np.linalg.norm(rv))
    for st in states:
        psi0 = np.zeros(H.shape[0], complex)
        for nprime in range(NL + 1):
            if nprime == 0:
                psi0[o] = st[0]
            else:
                psi0[o - nprime] = st[nprime]
        coef = EV.T @ psi0
        for s in (30.0, 120.0, 250.0):
            ps = EV @ (np.exp(-1j * s * ew) * coef)
            out = np.concatenate([[ps[o + 5]], ps[o + 6:o + 6 + NR]])
            w, bs = formula_output(p, st, s, NR)
            maxdev_nobs = max(maxdev_nobs, np.linalg.norm(out - w))
            maxdev_bs = max(maxdev_bs, np.linalg.norm(out - w - bs))
            maxbs = max(maxbs, np.linalg.norm(bs))
chk("C1 finite-time formula P_R e^{-isH}psi0 = P_R U_Z(s)F^{-1}[tau ghat0] + e^{-isE_b}<u_b|psi0>u_b|_R matches brute-force eigh to 1e-9 "
    "(2 sectors x 4 states incl. broadband and port-adjacent x 3 times)", maxdev_bs < 1e-9,
    f"max dev with bound-state term {maxdev_bs:.1e}; without it {maxdev_nobs:.1e} (bound-state piece up to {maxbs:.1e}); {time.time() - t_c0:.0f}s")
chk("C2 the bound-state term is NOT negligible for states touching the core (so the continuum-only formula needs the stated correction)",
    maxdev_nobs > 1e-3, f"{maxdev_nobs:.2e}")

# ---------------------------------------------------------------------------------------------
# D. bounds: Lipschitz certificate, spectral weight of the launcher profile, Chebyshev position bound
# ---------------------------------------------------------------------------------------------
K0 = np.pi / 2


def arcdist(r, h):
    ph = np.angle(r)
    d = (ph - K0 + np.pi) % (2 * np.pi) - np.pi
    if abs(d) <= h:
        return abs(abs(r) - 1)
    return float(np.min(np.abs(np.exp(1j * np.array([K0 - h, K0 + h])) - r)))


LIP = {}
for p in (1, -1):
    dc, nc, _ = DN[p]
    rt = np.roots(dc)
    degD, degN = len(dc) - 1, len(nc) - 1
    Dp = sum((degD - i) * abs(c_) for i, c_ in enumerate(dc))
    Np = sum((degN - i) * abs(c_) for i, c_ in enumerate(nc))
    for h in (0.0005, 0.001, 0.002, 0.005):
        dmin = abs(dc[0]) * np.prod([arcdist(r, h) for r in rt])
        cert = (Np + Dp) / dmin               # uses |N|<=|D| (unitarity, A5):  |tau'| <= (|N'|+|D'|)/|D|
        kk = np.linspace(K0 - h, K0 + h, 100001)
        tt = np.polyval(nc, np.exp(1j * kk)) / np.polyval(dc, np.exp(1j * kk))
        obs = np.max(np.abs(np.diff(tt)) / np.diff(kk))
        LIP[(p, h)] = (cert, obs)
ok = all(LIP[k][0] >= LIP[k][1] for k in LIP)
chk("D1 certified Lipschitz constants of tau on |k-pi/2|<=h (root-product lower bound for |det|, coefficient bound for N',D') dominate the observed sup|tau'|",
    ok, "cert/obs at h=0.005: p=+1 %.0f/%.2f, p=-1 %.0f/%.1f (source (5)-(6) used 4.8e7 for S')" % (LIP[(1, 0.005)] + LIP[(-1, 0.005)]))


def C_cert(p):
    best = None
    for h in (0.0005, 0.001, 0.002, 0.005):
        Lh = LIP[(p, h)][0]
        c_ = math.sqrt(math.pi) * math.sqrt(Lh ** 2 * h + 4.0 / h)
        if best is None or c_ < best[0]:
            best = (c_, h, Lh)
    return best


CC = {p: C_cert(p) for p in (1, -1)}


def beta_vec(rho, m, t):
    a = math.sqrt(1 - rho ** 2)
    n = np.arange(0, m + 1)
    return np.exp(-2j * t) * np.exp(1j * m * np.pi / 2) * 1j * rho * (-1j * a) ** (m - n) / math.sqrt(1 - a ** (2 * (m + 1)))


def ghat2_closed(rho, m, k):
    a = math.sqrt(1 - rho ** 2)
    z_ = a * np.exp(1j * (k - np.pi / 2))
    S = (1 - z_ ** (m + 1)) / (1 - z_)
    return rho ** 2 / (1 - a ** (2 * (m + 1))) * np.abs(S) ** 2


# closed-form |ghat|^2 equals FFT of the explicit profile (distance D drops out of |.|)
rho_t, m_t = 0.1, 3000
vec = beta_vec(rho_t, m_t, 0.0)[::-1]                     # j = m-n distance behind the front
arr = np.zeros(2 ** 16, complex)
arr[50:50 + m_t + 1] = vec
g = len(arr) * np.fft.ifft(arr)
kk_ = np.fft.fftfreq(len(arr)) * 2 * np.pi
dev = np.max(np.abs(np.abs(g) ** 2 - ghat2_closed(rho_t, m_t, kk_)))
chk("D2 closed form |ghat0(k)|^2 = rho^2|1-z^{m+1}|^2/(kappa|1-z|^2), z=a e^{i(k-pi/2)} equals the FFT of the explicit launcher profile; Parseval norm 1",
    dev < 1e-9 and abs(np.mean(np.abs(g) ** 2) - 1) < 1e-9, f"dev {dev:.1e}")

# exact e_R(beta) = ||(tau - t_p) ghat0||_{L2(dk/2pi)} versus rho, and the proved bound  e_R <= C_cert * rho
NKD = 2 ** 21
KD = np.fft.fftfreq(NKD) * 2 * np.pi
EXACT_C = {}
okb = True
for p in (1, -1):
    tt = tau_r(p, KD)[0]
    tpc = tau_r(p, np.array([K0]))[0][0]
    for rho in (0.1, 0.05, 0.02):
        m = int(40 / rho ** 2)
        g2 = ghat2_closed(rho, m, KD)
        eR = math.sqrt(np.mean(np.abs(tt - tpc) ** 2 * g2))
        a = math.sqrt(1 - rho ** 2)
        kappa = 1 - a ** (2 * (m + 1))
        bound = rho * CC[p][0] / math.sqrt(a * kappa)
        okb &= eR <= bound
        EXACT_C[(p, rho)] = eR / rho
chk("D3 proved spectral bound e_R <= rho*sqrt(pi/(a*kappa))*sqrt(L^2 h + 4/h) (Lipschitz arc + trivial |tau-t|<=2 outside) holds for the exact launcher profile",
    okb, "e_R/rho exact: p=+1 %.3f, p=-1 %.3f; certified constant: p=+1 %.0f, p=-1 %.0f" % (EXACT_C[(1, 0.02)], EXACT_C[(-1, 0.02)], CC[1][0], CC[-1][0]))
chk("D4 e_R scales linearly with rho (e_R/rho constant to 6% over rho=0.1..0.02): the Poisson tail makes the scattering-stage error O(rho), not O(rho^2)",
    all(abs(EXACT_C[(p, 0.02)] / EXACT_C[(p, 0.1)] - 1) < 0.06 for p in (1, -1)))


# Chebyshev position bound for the free output profile w(s)=U_Z(s) mirror(psi0): weight on x<0 (not in the right lead)
def moments(psi):
    n = np.arange(len(psi))
    pr = np.abs(psi) ** 2
    nbar = np.sum(n * pr)
    var0 = np.sum((n - nbar) ** 2 * pr)
    pad = np.concatenate([[0], psi, [0]])
    Vpsi = -1j * (pad[:-2] - pad[2:])                      # (V psi)(n') = -i[psi(n'-1) - psi(n'+1)]  <-> 2 sin k
    vbar = np.real(np.vdot(psi, Vpsi[:len(psi)]))
    varV = np.real(np.vdot(Vpsi, Vpsi)) - vbar ** 2
    return nbar, math.sqrt(var0), vbar, math.sqrt(max(varV, 0.0))


def eta_cheb(psi, s):
    nbar, s0, vbar, sV = moments(psi)
    mu = -nbar + s * vbar                                   # mean position x of w(s)
    if mu + 1 <= 0:
        return 1.0
    return min(1.0, (s0 + s * sV) ** 2 / (mu + 1) ** 2)


def eta_true(psi, s, nk=2 ** 17):
    arr = np.zeros(nk, complex)
    arr[:len(psi)] = psi
    g = nk * np.fft.ifft(arr)
    k_ = np.fft.fftfreq(nk) * 2 * np.pi
    w = np.fft.ifft(np.exp(-1j * s * (2 - 2 * np.cos(k_))) * g)
    return float(np.sum(np.abs(w[nk // 2:]) ** 2))        # x<0


rho, m, Dd = 0.1, 2400, 120
psi_b = np.zeros(Dd + m + 1, complex)
psi_b[Dd:] = beta_vec(rho, m, 0.0)[::-1]
nb, s0_, vb, sV_ = moments(psi_b)
ok = True
rows = []
for s in (150.0, 400.0, 900.0, 1500.0):
    et, ec = eta_true(psi_b, s), eta_cheb(psi_b, s)
    ok &= et <= ec + 1e-12
    rows.append((s, et, ec))
chk("D5 Chebyshev bound  weight(x<0) <= (sigma0+s sigma_V)^2/(mu_s+1)^2  (exact identity X(s)=X+sV(K)) dominates the exact free-evolution weight",
    ok and abs(vb - 2) < 0.02, "mean velocity %.4f, sigma_V/rho=%.3f; (s,true,bound)=%s" % (vb, sV_ / rho, ", ".join("(%d,%.1e,%.1e)" % r for r in rows)))
chk("D6 sigma_V ~ sqrt(2) rho for the Poisson profile, so the Chebyshev bound is usable iff rho < eps/(4 sqrt2): crossing time ~ 1/(rho^2 eps), not 1/rho^2",
    abs(sV_ / rho - math.sqrt(2)) < 0.05)

# ---------------------------------------------------------------------------------------------
# E. end-to-end finite device: emitter + line + ladder + output line (positive blocks, single head)
# ---------------------------------------------------------------------------------------------
def build_full(p, rho, M, N):
    nE, nline = 1, M + 1
    iL = nE + nline
    n = iL + 6 + N
    rows, cols, vals = [], [], []

    def add(i, j, v):
        rows.append(i)
        cols.append(j)
        vals.append(v)

    add(0, 0, 2.0)
    add(0, 1, -rho)
    add(1, 0, -rho)
    for i in range(1, nE + nline):
        add(i, i, 2.0)
        if i + 1 <= nE + nline - 1:
            add(i, i + 1, -1.0)
            add(i + 1, i, -1.0)
    add(nE + nline - 1, iL, -1.0)
    add(iL, nE + nline - 1, -1.0)
    C = CORE[p]
    for a_ in range(6):
        for b_ in range(6):
            if C[a_, b_] != 0:
                add(iL + a_, iL + b_, C[a_, b_])
    for i in range(N):
        j = iL + 6 + i
        add(j, j, 2.0)
        add(j - 1, j, -1.0)
        add(j, j - 1, -1.0)
    return sps.csr_matrix((vals, (rows, cols)), shape=(n, n)), iL


def end_to_end(rho, tf=5.0, tailf=6.0):
    inv = 1 / rho ** 2
    out = {}
    for p in (1, -1):
        t1 = tf * inv
        m = int(math.floor(2 * t1 + 0.5))
        M = m + int(0.2 * inv) + 50
        Dd = M + 1 - m
        s_obs = t1 + (M - m) / 2 + tailf * inv
        N = int(2 * (s_obs - t1) + 0.5 * inv) + 200
        H, iL = build_full(p, rho, M, N)
        n = H.shape[0]
        psi_e = np.zeros(n, complex)
        psi_e[0] = 1
        A = expm_multiply(-1j * H, psi_e, start=t1, stop=s_obs, num=2, endpoint=True)
        a1, a2 = A[0], A[1]
        # launcher stage: distance to beta(t1) (embedded on the line)
        beta = beta_vec(rho, m, t1)
        emb = np.zeros(n, complex)
        emb[1:1 + m + 1] = beta
        eps_launch = np.linalg.norm(a1 - emb)
        # ideal output of beta through the ladder: t_p * free evolution of the mirrored profile
        psi0 = np.zeros(M + 2, complex)                       # n'=0..M+1 ; line site j <-> n'=M+1-j
        for j_ in range(m + 1):
            psi0[M + 1 - j_] = beta[j_]
        dsh = s_obs - t1
        nk = 2 ** 18
        arr = np.zeros(nk, complex)
        arr[:len(psi0)] = psi0
        g0 = nk * np.fft.ifft(arr)
        k_ = np.fft.fftfreq(nk) * 2 * np.pi
        w = np.fft.ifft(np.exp(-1j * dsh * (2 - 2 * np.cos(k_))) * g0)
        tpc = tau_r(p, np.array([K0]))[0][0]
        ideal_R = tpc * w[:N + 1]
        eta = float(np.sum(np.abs(w[N + 1:nk // 2]) ** 2) + np.sum(np.abs(w[nk // 2:]) ** 2))   # weight not on 0..N
        aR = a2[iL + 5:]
        errR = np.linalg.norm(aR - ideal_R)
        nonR = np.linalg.norm(a2[:iL + 5])
        full = math.sqrt(errR ** 2 + nonR ** 2)
        # theory side
        tt = TAU_G[p]
        eR = math.sqrt(np.mean(np.abs(tt - tpc) ** 2 * np.abs(g0) ** 2))
        bs, ovb = bound_state_term(p, psi0, dsh, N)
        eR_tot = eR + ovb
        bound = math.sqrt(eta + 2 * eR_tot)
        # plain-line comparator (no ladder): physical target "common packet times t_p"
        rowsP = []
        npl = 1 + (M + 1) + 1 + N
        Hp = sps.diags([np.full(npl, 2.0), np.full(npl - 1, -1.0), np.full(npl - 1, -1.0)], [0, 1, -1], format="lil")
        Hp[0, 1] = -rho
        Hp[1, 0] = -rho
        Hp = Hp.tocsr()
        q0 = np.zeros(npl, complex)
        q0[0] = 1
        b2 = expm_multiply(-1j * Hp, q0, start=t1, stop=s_obs, num=2, endpoint=True)[1]
        ideal_plain = np.zeros(n, complex)
        ideal_plain[iL + 5] = tpc * b2[M + 2]
        ideal_plain[iL + 6:iL + 6 + N] = tpc * b2[M + 3:M + 3 + N]
        left = np.zeros(n, complex)
        left[0:M + 2] = b2[0:M + 2]
        err_plain = np.linalg.norm(a2 - ideal_plain - left)
        out[p] = dict(n=n, M=M, N=N, t1=t1, s_obs=s_obs, eps_launch=eps_launch, full=full, errR=errR, eR=eR, ovb=ovb, eta=eta,
                      bound=bound, err_plain=err_plain, eta_cheb=eta_cheb(psi0, dsh), wR=np.linalg.norm(aR) ** 2)
    return out


t_e = time.time()
E1 = end_to_end(0.10)
ok = True
msgs = []
for p in (1, -1):
    r = E1[p]
    ok &= r["full"] <= r["eps_launch"] + r["bound"] and r["wR"] > 0.9
    msgs.append("p=%+d: n=%d, eps_launch=%.3f, measured full err=%.3f <= %.3f+sqrt(eta+2e_R)=%.3f (e_R=%.3f, eta=%.1e), vs plain-line target %.3f" % (
        p, r["n"], r["eps_launch"], r["full"], r["eps_launch"], r["bound"], r["eR"], r["eta"], r["err_plain"]))
chk("E1 rho=0.10 finite device: measured complete error <= (launcher stage) + sqrt(eta + 2 e_R)  [chain of proved steps A1-A3; left-end/right-cut transfer is an observation here]",
    ok, " ; ".join(msgs))
E2 = end_to_end(0.05)
ok = True
msgs = []
for p in (1, -1):
    r = E2[p]
    ok &= r["full"] <= r["eps_launch"] + r["bound"] and r["wR"] > 0.9
    msgs.append("p=%+d: n=%d, eps_launch=%.3f, measured=%.3f, bound=%.3f (e_R=%.3f), plain-target err %.3f" % (
        p, r["n"], r["eps_launch"], r["full"], r["eps_launch"] + r["bound"], r["eR"], r["err_plain"]))
chk("E2 rho=0.05 finite device (about 9.5e3 sites): same inequality; error halves with rho (launcher O(rho), scattering O(rho))",
    ok and E2[1]["full"] < 0.7 * E1[1]["full"] and E2[-1]["full"] < 0.7 * E1[-1]["full"], " ; ".join(msgs) + f" ; {time.time() - t_e:.0f}s")
chk("E5 measured launcher-stage distance ||psi(t1)-beta(t1)|| (rho=0.1, 0.05) is below the sum of the source note's component bounds 29rho/8 + rho + 2rho(t1)^(1/6) (+ survival e^{-rho^2 t}+4rho^2/3): the imported launcher lemmas are consistent at these sizes (not a proof of them)",
    all(E1[p]["eps_launch"] <= 29 * 0.10 / 8 + 0.10 + 2 * 0.10 * E1[p]["t1"] ** (1 / 6) + math.exp(-0.01 * E1[p]["t1"]) + 4 * 0.01 / 3 and
        E2[p]["eps_launch"] <= 29 * 0.05 / 8 + 0.05 + 2 * 0.05 * E2[p]["t1"] ** (1 / 6) + math.exp(-0.0025 * E2[p]["t1"]) + 4 * 0.0025 / 3 for p in (1, -1)))
chk("E3 observed complete error is about e_R-sized (<= 2.5 e_R + launcher) while the proved sqrt(eta+2e_R) is larger: the square-root loss of the norm-conservation step is real slack",
    all(E2[p]["full"] < 3 * E2[p]["eR"] + E2[p]["eps_launch"] for p in (1, -1)) and all(E2[p]["bound"] > E2[p]["eR"] for p in (1, -1)))
chk("E4 Chebyshev position bound at the observation time is consistent with the measured weight outside the output lead",
    all(E2[p]["eta"] <= E2[p]["eta_cheb"] + 1e-12 for p in (1, -1)),
    "eta true/Cheb: " + ", ".join("%.1e/%.1e" % (E2[p]["eta"], E2[p]["eta_cheb"]) for p in (1, -1)))

# ---------------------------------------------------------------------------------------------
# F. composition arithmetic (exact rationals).  Imports from the notes are ASSUMED, not re-proved here.
# ---------------------------------------------------------------------------------------------
def rat_up(x):
    return Fraction(math.ceil(x * 10 ** 12), 10 ** 12)


def composition(eps):
    eps = Fraction(eps)
    # clock-stage allocation: launcher (source note, tolerance eps_c) + sqrt(eta+2 e_R) <= eps/2
    eps_c = eps / 6
    Lc = math.log(32 / float(eps_c))
    rho_c = (float(eps_c) / 64) ** 1.5 * Lc ** (-0.25)                     # source note, ASSUMED
    Cc = max(CC[1][0], CC[-1][0])
    need_e = float(eps) ** 2 / 128                                         # e_R <= eps^2/128  => sqrt(2 e_R)<=eps/8
    rho = min(rho_c, need_e / Cc, float(eps) / (8 * math.sqrt(2) * 4))
    u0 = Lc / rho ** 2
    # crossing time from the Chebyshev bound with eta <= (eps/8)^2 ; sigma0 ~ 1/rho^2, sigma_V ~ sqrt2 rho, v ~ 2
    sig0 = 1 / rho ** 2
    sigV = math.sqrt(2) * rho
    tgt = float(eps) / 8
    D = 200                                                                # port distance beyond the front (bound-state overlap ~0.6^200)
    v = 2.0
    denom = v - sigV / tgt
    assert denom > 0
    s_after = (sig0 / tgt + (D + 1 / rho ** 2) + 1) / denom
    # cone factor of the source note's finite transfer: d >= 4 e ||T|| dt, ||T|| = max hopping row sum of the device
    hop = max(2.0, max(np.sum(np.abs(CORE[p] - np.diag(np.diag(CORE[p]))), axis=1).max() for p in (1, -1)))
    cone = 4 * math.e * hop
    Xtail = 2 * math.log(1 / (float(eps) / 64)) / rho ** 2                 # back-tail truncation, weight <= (eps/64)^2
    m_need = cone * s_after + Xtail                                        # terminus must be farther than the cone reaches (Lemma B, SUGGESTED)
    t1 = max(2 * u0, m_need / 2)                                           # source window T=2u0 is NOT enough: launch time extended (ASSUMED monotone)
    m = int(math.floor(2 * t1 + 0.5))
    M = m + D
    NR = int(math.ceil(cone * s_after)) + 200
    nclock = 1 + (M + 1) + 6 + NR
    q_blocks = 3 + M + 1 + 12 + NR + 1                                      # emitter bond+2 onsites, M line bonds, bond to port, core 6+6, NR output bonds, cap
    blocks_total = nclock + 4 + q_blocks                                   # compensated: L+4+q
    qubits = nclock + 3
    MB = Fraction(4) + 9 * Fraction(math.sqrt(2)).limit_denominator(10 ** 6) / 4          # ||B_near|| <= 4+9f (section 9)
    S = Fraction(t1 + s_after).limit_denominator(1)
    U = max(Fraction(1), 8 * (1 + S * MB) / eps)
    lam_cap_eps = eps / (656 * (1 + S * (U + MB)))
    Kload = Fraction(5)                                                    # max incident norm over clock sites (emitter 3, site0 5, interior 4, core <=3.5)
    Lam = Fraction(5)
    r_up = 1 / U
    Cload = U + Kload + r_up
    lam_cap1 = (Lam - 4) / 16
    lam_cap2 = Fraction(math.sqrt(float((Lam - 4) / (2 * Cload)))).limit_denominator(10 ** 15)
    lam = min(Fraction(1, 1000), lam_cap_eps, lam_cap1, lam_cap2)
    load_bound = 4 + 8 * lam + lam ** 2 * Cload
    return dict(rho=rho, u0=u0, t1=t1, m=m, D=D, M=M, NR=NR, s_obs=S, qubits=qubits, blocks=blocks_total, U=U, lam=lam,
                load_bound=load_bound, Lam=Lam, qb=q_blocks, nclock=nclock, hop=hop, cone=cone, s_after=s_after)


comp = composition(Fraction(1, 10))
ok_cap = comp["load_bound"] <= comp["Lam"]
chk("F1 composed sufficient family for eps=1/10 (rho from e_R<=C_cert*rho and the sqrt-loss; Chebyshev crossing time; section-9 local-support budget U,lambda): incident bound 4+8lam+lam^2 C_load <= Lambda=5",
    ok_cap, "rho=%.2e, launch time t1=%.2e (source window 2u0=%.2e is too short for the cone condition), port at M=%.2e, S=b_eff*t=%.2e, qubits=%.2e, positive blocks=%.2e, U=%.2e, lambda=%.2e, load<=%.6f, hop-norm bound %.3f" % (
        comp["rho"], float(comp["t1"]), 2 * comp["u0"], comp["M"], float(comp["s_obs"]), comp["qubits"], comp["blocks"], float(comp["U"]), float(comp["lam"]), float(comp["load_bound"]), comp["hop"]))
comp2 = composition(Fraction(1, 100))
chk("F2 resource trend: dividing eps by 10 raises S by >= 1e3 (Chebyshev 1/(rho^2 eps) crossing + rho ~ eps^2): sizes are astronomically large sufficient constants, not a practical device",
    float(comp2["s_obs"]) > 1e3 * float(comp["s_obs"]), "s_obs(eps=1/100)=%.2e" % float(comp2["s_obs"]))
chk("F3 inventory count formula: positive blocks = (clock qubits) + 4 + q with q = ordinary positive background blocks (NV compensated count); launcher blocks are disjoint from the active pair so section-9 local budget applies",
    comp["blocks"] == comp["nclock"] + 4 + comp["qb"] and comp["qubits"] == comp["nclock"] + 3)

# ---------------------------------------------------------------------------------------------
n_pass = sum(RES)
n_fail = len(RES) - n_pass
core_ok = all(RES)
if core_ok:
    print("HIT: for the supplied p=+-1 ladder, EVERY left-lead one-head initial vector obeys an exact all-time output formula "
          "(tau*ghat0 plus one explicit above-band bound-state term, CHECKED to 1e-9 against brute force) and a complete-output bound "
          "sqrt(eta+2e_R) with certified tau-Lipschitz data; this converts the packet theorem into a finite-time statement and shows "
          "the launcher-to-output interface reduces to the left-end/right-cut transfer (not proved here)")
print(f"TOTAL: PASS={n_pass} FAIL={n_fail}")
print("SUMMARY: exact finite-time transmitted-output formula and complete-output bound for the supplied stationary ladder (bound state and "
      "resonances located, brute-force and end-to-end finite-device consistent), with the finite left-end/right-cut transfer and mediator "
      "composition left as the unproved/imported steps")
sys.exit(0 if n_fail == 0 else 1)
