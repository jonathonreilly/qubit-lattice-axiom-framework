#!/usr/bin/env python3
"""J:derive:odds-field-sphere-menu:a1 (worker w-macbookpro90c72-j00d0).

Sphere menu, pair weight exp(beta s.s'); self-consistent odds pi_x(s) ~ prod_y (K1 pi_y)(s) (block 42 T2 read on
the sphere), and block 42 T5's seven-outcome reading ('no record' as a possibility, factor 1 - rho + rho g K1 nu).
  A. Funk-Hecke eigenvalues, their ordering, the massless point (certified interval), the screened side.
  B. The ordered sea: exact Landau coefficients (sympy), the field (spectral quadrature), the sector spectra,
     the turn mode at exactly 1/6, the longitudinal mass and its law near the point.
  C. What a record feeds in: the seven-outcome reading at the neutral scale g = 1 in the ordered sea (mass channel
     strength, the density-lean block, its tricritical point and its massless surface).
  D. Records as boundary values in the massless channel: infinite-lattice capacities from the lattice Green function.
Exact: sympy identities and rational series coefficients. mpmath at 40 digits where stated; float64 spectral
quadrature (N = 64 and 96 Gauss-Legendre nodes, their difference printed as the error).
"""
import math
import sys
import time

import mpmath as mp
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss

T0 = time.time()
FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


mp.mp.dps = 40
HALF = mp.mpf(1) / 2


def lam_mp(beta, l):
    """Funk-Hecke eigenvalue of K1 on angular momentum l: i_l(beta)/i_0(beta)."""
    return mp.besseli(l + HALF, beta) / mp.besseli(HALF, beta)


# ======================= A. the one-neighbour operator =======================
err, err_cf = mp.mpf(0), mp.mpf(0)
for beta in (HALF, mp.mpf(1), mp.mpf(3)):
    Z = mp.sinh(beta) / beta
    lc = [mp.mpf(1), mp.coth(beta) - 1 / beta]
    for l in range(1, 7):
        lc.append(lc[l - 1] - (2 * l + 1) * lc[l] / beta)
    for l in range(0, 7):
        direct = mp.quad(lambda t: mp.exp(beta * t) * mp.legendre(l, t), [-1, 1]) / 2 / Z
        err = max(err, abs(direct - lam_mp(beta, l)))
        err_cf = max(err_cf, abs(lc[l] - lam_mp(beta, l)))
x = sp.symbols("x", positive=True)
s1 = sp.series(sp.coth(x) - 1 / x, x, 0, 9).removeO()
s2 = sp.series(1 - 3 * (sp.coth(x) - 1 / x) / x, x, 0, 9).removeO()
good = (sp.expand(s1 - (x / 3 - x**3 / 45 + 2 * x**5 / 945 - x**7 / 4725)) == 0
        and sp.expand(s2 - (x**2 / 15 - 2 * x**4 / 315 + x**6 / 1575 - 2 * x**8 / 31185)) == 0)
ok("A1", err < mp.mpf(10) ** -30 and err_cf < mp.mpf(10) ** -30 and good,
   f"lambda_l = i_l/i_0 equals the Funk-Hecke integral for l <= 6 at beta = 1/2, 1, 3 (err {mp.nstr(err, 2)}); "
   "lambda_1 = coth b - 1/b and lambda_(l+1) = lambda_(l-1) - (2l+1) lambda_l/b; exact series "
   "lambda_1 = b/3 - b^3/45 + 2b^5/945 - b^7/4725, lambda_2 = b^2/15 - 2b^4/315 + b^6/1575 - 2b^8/31185")

# A2: lambda_l / lambda_(l-1) = E[t] under e^{bt}(1-t^2)^(l-1) on [-1,1], hence 1 > lambda_1 > lambda_2 > ... > 0
good = True
for beta in (mp.mpf(1), mp.mpf(3)):
    for l in range(1, 6):
        num = mp.quad(lambda t: t * mp.exp(beta * t) * (1 - t * t) ** (l - 1), [-1, 1])
        den = mp.quad(lambda t: mp.exp(beta * t) * (1 - t * t) ** (l - 1), [-1, 1])
        r = lam_mp(beta, l) / lam_mp(beta, l - 1)
        good &= abs(r - num / den) < mp.mpf(10) ** -30 and 0 < r < 1
ok("A2", good, "lambda_l/lambda_(l-1) = <t> under e^(bt)(1-t^2)^(l-1) for l <= 5 at b = 1, 3 (to 1e-30): "
   "each ratio lies in (0,1), so 1 > lambda_1 > lambda_2 > ... > 0 for every b > 0")

# A3: the massless point 6 L(b) = 1, certified by interval arithmetic (L increasing: L' = 1/b^2 - 1/sinh^2 b > 0)
IV = mp.iv
IV.dps = 45


def L_iv(b):
    b = IV.mpf(b)
    e = IV.exp(2 * b)
    return (e + 1) / (e - 1) - 1 / b


lo, hi = mp.mpf("0.50855806178558212313"), mp.mpf("0.50855806178558212315")
flo, fhi = 6 * L_iv(lo) - 1, 6 * L_iv(hi) - 1
bc = mp.findroot(lambda b: 6 * (mp.coth(b) - 1 / b) - 1, 0.5)
ok("A3", flo.b < 0 < fhi.a and lo < bc < hi,
   f"beta_c in [{lo}, {hi}] by interval arithmetic (6L-1 < 0 at the left end, > 0 at the right); "
   f"beta_c = {mp.nstr(bc, 22)}")

rows = []
for b in (mp.mpf("0.3"), mp.mpf("0.45"), mp.mpf("0.5")):
    Lb = mp.coth(b) - 1 / b
    m2 = (1 - 6 * Lb) / Lb
    kap = mp.acosh((1 / Lb - 4) / 2)
    rows.append(f"b={mp.nstr(b, 3)}: m^2={mp.nstr(m2, 5)}, 1/m={mp.nstr(1 / mp.sqrt(m2), 4)}, 1/kappa={mp.nstr(1 / kap, 4)}")
ok("A4", True, "screened side (-Lap + m^2) v = source/L, m^2 = (1-6L)/L; axial decay cosh kappa = (1/L - 4)/2: "
   + "; ".join(rows))

# ======================= B. the ordered sea (no vacancies) =======================
t_, a_, l1, l2, l3, rho = sp.symbols("t a lambda1 lambda2 lambda3 rho")
P = [sp.legendre(k, t_) for k in range(6)]


def proj(expr, k):
    """Legendre coefficient of P_k in expr (polynomial in t), exact."""
    return sp.Rational(2 * k + 1, 2) * sp.integrate(sp.expand(expr * P[k]), (t_, -1, 1))


bq, cq = sp.symbols("b c")
u = a_ * P[1] + bq * a_**2 * P[2] + cq * a_**3 * P[3]
wv = a_ * l1 * P[1] + bq * a_**2 * l2 * P[2] + cq * a_**3 * l3 * P[3]


def Nmap(wexpr, order=3):
    """(1+w)^6/<(1+w)^6> - 1 expanded to the given order in a."""
    num = sp.expand(sum(sp.binomial(6, k) * wexpr**k for k in range(order + 1)))
    num = sp.series(num, a_, 0, order + 1).removeO()
    avg = sp.Rational(1, 2) * sp.integrate(num, (t_, -1, 1))
    return sp.expand(sp.series(num / avg, a_, 0, order + 1).removeO() - 1)


Nu = Nmap(wv)
eq2 = sp.expand(proj(Nu, 2).coeff(a_, 2) - bq)
bsol = sp.solve(eq2, bq)[0]
c1 = sp.expand(proj(Nu, 1).subs(bq, bsol))
c3 = sp.simplify(c1.coeff(a_, 3))
good = (sp.simplify(bsol - 10 * l1**2 / (1 - 6 * l2)) == 0 and sp.simplify(c1.coeff(a_, 1) - 6 * l1) == 0
        and sp.simplify(c3 - 6 * l1**3 * (38 * l2 - 3) / (1 - 6 * l2)) == 0)
ok("B1", good, "exact expansion of F = (K1 F)^6/<(K1 F)^6>, F = 1 + a P1 + b a^2 P2 + ...: b = 10 l1^2/(1-6 l2), "
   "a = 6 l1 a + c3 a^3 with c3 = 6 l1^3 (38 l2 - 3)/(1 - 6 l2) (< 0 at beta_c, where l2 = 0.0168 < 3/38); "
   "M = a/3; the reduced longitudinal eigenvalue 6 l1 + 3 c3 a*^2 = 1 - 2(6 l1 - 1)")

LMAX = 70


def plm(m, lmax, t):
    """orthonormal associated Legendre functions on [-1,1] (rows l = 0..lmax; rows below m are zero)."""
    Pm = np.zeros((lmax + 1, len(t)))
    df = 1.0
    for k in range(1, 2 * m, 2):
        df *= k
    Pm[m] = np.sqrt((2 * m + 1) / (2 * math.factorial(2 * m))) * df * (1 - t * t) ** (m / 2)
    if m + 1 <= lmax:
        Pm[m + 1] = np.sqrt(2 * m + 3) * t * Pm[m]
    for l in range(m + 2, lmax + 1):
        a = np.sqrt((4 * l * l - 1) / (l * l - m * m))
        b = np.sqrt(((l - 1) ** 2 - m * m) * (2 * l + 1) / ((l * l - m * m) * (2 * l - 3)))
        Pm[l] = a * t * Pm[l - 1] - b * Pm[l - 2]
    return Pm


class Sea:
    """uniform self-consistent sea at (beta, rho), g = 1: b = 1 - rho + rho K1 F, F = b^6/<b^6>."""

    def __init__(self, beta, rho=1.0, N=96):
        self.beta, self.rho = beta, rho
        self.t, self.w = leggauss(N)
        self.lam = np.array([float(lam_mp(mp.mpf(beta), l)) for l in range(LMAX + 1)])
        self.P = {m: plm(m, LMAX, self.t) for m in (0, 1, 2, 3)}
        self.K = {m: (self.P[m][m:].T * self.lam[m:]) @ self.P[m][m:] for m in (0, 1, 2, 3)}
        G = 1 + 0.3 * self.t
        for it in range(400000):
            b = 1 - rho + rho * G
            F = b ** 6
            F /= 0.5 * np.sum(self.w * F)
            Gn = self.K[0] @ (self.w * F)
            if np.abs(Gn - G).max() < 1e-15:
                G = Gn
                break
            G = Gn
        self.G = G
        self.b = 1 - rho + rho * G
        F = self.b ** 6
        self.F = F / (0.5 * np.sum(self.w * F))
        self.M = 0.5 * np.sum(self.w * self.t * self.F)

    def avgF(self, f):
        return 0.5 * np.sum(self.w * self.F * f)

    def spectrum(self, m):
        """eigenvalues of the per-neighbour operator rho K1(F .)/b on sector m (symmetrized; m = 0 includes 1)."""
        d = np.sqrt(self.rho * self.w * self.F / self.b)
        return np.sort(np.linalg.eigvalsh(d[:, None] * self.K[m] * d[None, :]))[::-1]

    def turn_residual(self):
        """the turn of the lean, eta = F'/F sqrt(1-t^2) = 6 rho sqrt(1-t^2) G'/b, against eigenvalue 1/6."""
        f = self.P[0] @ (self.w * self.F)
        ll = np.arange(LMAX + 1)
        eta = -6 * self.rho * ((self.lam * f * np.sqrt(ll * (ll + 1))) @ self.P[1]) / self.b
        Aeta = self.rho * (self.K[1] @ (self.w * self.F * eta)) / self.b
        return np.abs(Aeta - eta / 6).max() / np.abs(eta).max()


rows, good, dmax = [], True, 0.0
for beta in (0.52, 0.6, 0.8, 1.0, 2.0, 4.0):
    S = Sea(beta)
    S64 = Sea(beta, N=64)
    dmax = max(dmax, abs(S.M - S64.M))
    e0, e1, e2, e3 = S.spectrum(0), S.spectrum(1), S.spectrum(2), S.spectrum(3)
    mu = e0[1]
    mL2 = (1 - 6 * mu) / mu
    res = S.turn_residual()
    good &= abs(e0[0] - 1) < 1e-12 and abs(e1[0] - 1 / 6) < 1e-12 and res < 1e-11
    good &= 6 * mu < 1 and 6 * e1[1] < 1 and 6 * e2[0] < 1 and 6 * e3[0] < 1
    rows.append(f"{beta}: M={S.M:.6f} mL^2={mL2:.4f} 6mu(m=1,2nd)={6 * e1[1]:.3f} 6mu(m=2)={6 * e2[0]:.3f}")
ok("B2", good, "ordered sea F(s.n): per-neighbour spectra by azimuthal number m; m=1 top = 1/6 (to 1e-12) with "
   f"eigenvector the turn of the lean (residual < 1e-11); every other sector below 1/6. N=64 vs 96: {dmax:.0e}. "
   + "; ".join(rows))

rows, good = [], True
for beta in (0.509, 0.51, 0.512):
    S = Sea(beta)
    lm1, lm2 = S.lam[1], S.lam[2]
    eps = 6 * lm1 - 1
    M2L = eps * (1 - 6 * lm2) / (6 * lm1 ** 3 * (3 - 38 * lm2)) / 9
    mu = S.spectrum(0)[1]
    mL2 = (1 - 6 * mu) / mu
    rows.append(f"b={beta}: eps={eps:.2e} M^2/Landau={S.M ** 2 / M2L:.4f} mL^2/(12 eps)={mL2 / (12 * eps):.4f}")
    good &= abs(S.M ** 2 / M2L - 1) < 30 * eps and abs(mL2 / (12 * eps) - 1) < 30 * eps
ok("B3", good, "near the point: M^2 -> (6L-1)(1-6 l2)/(54 l1^3 (3-38 l2)) and mL^2 -> 12(6L-1), twice the "
   "screened side's m^2 ~ 6(1-6L) at equal distance: " + "; ".join(rows))

# ======================= C. the seven-outcome reading at g = 1 =======================
# C1: symbolic: isotropic eigenvalues; density shift; fixed-z cubic; tricritical condition
g, dr, e = sp.symbols("g drho epsilon")
bb = 1 - (rho + dr) + (rho + dr) * g * (1 + e * l1 * t_)
scal = sp.simplify(rho * (1 - rho) * sp.diff(sp.log(bb), dr).subs({dr: 0, e: 0}))
vec = sp.simplify(sp.diff(sp.log(bb), e).subs({dr: 0, e: 0}) / t_)
wr = rho * a_ * l1 * P[1]
avg6 = sp.expand(sp.Rational(1, 2) * sp.integrate(sp.expand((1 + wr) ** 6), (t_, -1, 1)))
c3r = c3.subs({l1: rho * l1, l2: rho * l2})
c3z = c3r + 6 * l1 * rho * (1 - rho) * 5 * rho ** 2 * l1 ** 2
tri = sp.simplify(sp.numer(sp.together(c3z.subs(rho, 1 / (6 * l1)))))
target = 12 * l1 ** 2 + 8 * l1 * l2 - 5 * l1 + 5 * l2
good = (sp.simplify(scal - rho * (1 - rho) * (g - 1) / (1 + rho * (g - 1))) == 0
        and sp.simplify(vec - rho * g * l1 / (1 + rho * (g - 1))) == 0
        and sp.simplify(sp.expand(avg6).coeff(a_, 2) - 5 * rho ** 2 * l1 ** 2) == 0 and sp.expand(avg6).coeff(a_, 1) == 0
        and sp.simplify(tri / target).is_number)
ok("C1", good, "isotropic sea: mass eigenvalue rho(1-rho)(g-1)/(1+rho(g-1)) (zero at g = 1), vector "
   "rho g l1/(1+rho(g-1)); at g = 1 the content map at density rho is the map with every l_k -> rho l_k; "
   "<b^6> = 1 + 5 rho^2 l1^2 a^2 + O(a^3); at fixed fugacity c3 -> c3(rho l) + 30 l1^3 rho^3 (1-rho), which on "
   "6 rho l1 = 1 vanishes iff 12 l1^2 + 8 l1 l2 - 5 l1 + 5 l2 = 0")

L1m = lambda b: mp.coth(b) - 1 / b
L2m = lambda b: 1 - 3 * L1m(b) / b
bt = mp.findroot(lambda b: 12 * L1m(b) ** 2 + 8 * L1m(b) * L2m(b) - 5 * L1m(b) + 5 * L2m(b), 0.95)
rt = 1 / (6 * L1m(bt))
sgn = []
for beta in (0.95, 0.96):
    S0 = Sea(beta)
    rc = 1 / (6 * S0.lam[1])
    S = Sea(beta, rc * 1.001)
    logz = np.log(S.rho / (1 - S.rho)) - np.log(0.5 * np.sum(S.w * S.b ** 6))
    sgn.append(logz - np.log(rc / (1 - rc)))
ok("C2", sgn[0] > 0 > sgn[1] and 0.95 < bt < 0.96,
   f"tricritical point on the ordering line: beta_t = {mp.nstr(bt, 15)}, rho_t = {mp.nstr(rt, 12)}; "
   f"ordered branch at rho = 1.001 rho_c needs log z - log z_c = {sgn[0]:+.1e} at b = 0.95 (continuous), "
   f"{sgn[1]:+.1e} at b = 0.96 (bends back: discontinuous)")


def block(S):
    """per-neighbour linear map on (drho, eta_0) in the ordered sea with vacancies, g = 1."""
    n = len(S.t)
    h = (S.G - 1) / S.b
    Keta = S.rho * (S.K[0] * (S.w * S.F)[None, :]) / S.b[:, None]
    row = 0.5 * (S.w * S.F) @ Keta
    Mx = np.zeros((n + 1, n + 1))
    Mx[1:, 1:] = Keta - np.outer(np.ones(n), row)
    Mx[1:, 0] = h - S.avgF(h)
    Mx[0, 0] = S.rho * (1 - S.rho) * S.avgF(h)
    Mx[0, 1:] = S.rho * (1 - S.rho) * row
    return Mx


rows, good = [], True
for beta, r in [(1.0, 0.9), (2.0, 0.9), (4.0, 0.95)]:
    S = Sea(beta, r)
    Mx = block(S)
    ident = (1 - r) * (1 - 0.5 * np.sum(S.w * S.b ** 5) / (0.5 * np.sum(S.w * S.b ** 6)))
    top = max(np.linalg.eigvals(Mx).real)
    good &= abs(Mx[0, 0] - ident) < 1e-14 and ident > 0 and 6 * top < 1 and S.turn_residual() < 1e-11
    rows.append(f"({beta},{r}): M={S.M:.4f} strength={ident:.3e} 6mu0={6 * top:.3f}")
ok("C3", good, "ordered sea with vacancies at g = 1: the mass channel's own first-order strength is "
   "(1-rho)(1 - <b^5>/<b^6>) > 0 (zero in the isotropic sea); drho enters the m = 0 block through "
   "h = (K1F-1)/b, never m = 1, where the turn stays exactly 1/6; " + "; ".join(rows))

rows, good = [], True
for beta in (1.0, 2.0, 4.0):
    rc = 1 / (6 * Sea(beta).lam[1])
    f = lambda r: 6 * max(np.linalg.eigvals(block(Sea(beta, r))).real) - 1
    a_lo, a_hi = rc * 1.02, 0.999
    good &= f(a_lo) > 0 > f(a_hi)
    for _ in range(40):
        mid = 0.5 * (a_lo + a_hi)
        if f(mid) > 0:
            a_lo = mid
        else:
            a_hi = mid
    S = Sea(beta, a_hi)
    Mx = block(S)
    ev, R = np.linalg.eig(Mx)
    k = int(np.argmax(ev.real))
    r = R[:, k].real / np.linalg.norm(R[:, k].real)
    evl, Lv = np.linalg.eig(Mx.T)
    lft = Lv[:, int(np.argmax(evl.real))].real
    v = Mx[:, 0]
    share = abs((lft @ v) / (lft @ r)) / np.linalg.norm(v)
    good &= share > 0.1 and abs(6 * ev[k].real - 1) < 1e-9
    rows.append(f"b={beta}: rho*={a_hi:.5f} (order from {rc:.4f}), mode share {share:.2f}")
ok("C4", good, "massless surface of the density-lean block (6 mu0 = 1; the uniform ordered sea is unstable below "
   "it); the mass source's coefficient on the massless mode (unit right eigenvector, per unit source): "
   + "; ".join(rows))

# ======================= D. records as boundary values: capacities =======================
mp.mp.dps = 30


def Glat(xv):
    """simple random walk Green function sum_n P^n(0,x) on Z^3: int_0^inf e^-t prod I_(x_i)(t/3) dt."""
    a, b, c = xv
    f = lambda t: mp.besseli(a, t / 3) * mp.besseli(b, t / 3) * mp.besseli(c, t / 3) * mp.exp(-t)
    pts = [mp.mpf(0)] + [mp.mpf(10) ** k for k in range(0, 9)]
    s = mp.fsum(mp.quad(f, [pts[i], pts[i + 1]]) for i in range(len(pts) - 1))
    T = pts[-1]
    Ssum = sum(4 * v * v - 1 for v in xv)
    return s + (mp.mpf(3) / (2 * mp.pi)) ** 1.5 * (2 / mp.sqrt(T) - Ssum / 4 / T ** 1.5)


g0w = (mp.sqrt(6) / (32 * mp.pi ** 3) * mp.gamma(mp.mpf(1) / 24) * mp.gamma(mp.mpf(5) / 24)
       * mp.gamma(mp.mpf(7) / 24) * mp.gamma(mp.mpf(11) / 24))
keys = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 1, 0), (2, 1, 1), (2, 2, 0), (2, 2, 1), (2, 2, 2)]
Gv = {k: Glat(k) for k in keys}
harm = max(abs(6 * Gv[(1, 0, 0)] - Gv[(0, 0, 0)] - Gv[(2, 0, 0)] - 4 * Gv[(1, 1, 0)]),
           abs(6 * Gv[(1, 1, 0)] - 2 * Gv[(1, 0, 0)] - 2 * Gv[(2, 1, 0)] - 2 * Gv[(1, 1, 1)]),
           abs(6 * Gv[(1, 1, 1)] - 3 * Gv[(1, 1, 0)] - 3 * Gv[(2, 1, 1)]))
ok("D1", abs(Gv[(0, 0, 0)] - g0w) < 1e-18 and abs(Gv[(1, 0, 0)] - (g0w - 1)) < 1e-18 and harm < 1e-18,
   f"lattice Green function: G(0) = {mp.nstr(Gv[(0, 0, 0)], 18)} (Watson's Gamma product to 1e-18), "
   f"G(1,0,0) = G(0) - 1, G(1,1,0) = {mp.nstr(Gv[(1, 1, 0)], 15)}, G(1,1,1) = {mp.nstr(Gv[(1, 1, 1)], 15)}; "
   f"harmonic at three sites to {mp.nstr(harm, 1)}")


def Gd(p, q):
    d = tuple(sorted((abs(p[i] - q[i]) for i in range(3)), reverse=True))
    return Gv[d]


def cap(Sset):
    A = mp.matrix([[Gd(p, q) for q in Sset] for p in Sset])
    return mp.fsum(mp.lu_solve(A, mp.matrix([1] * len(Sset))))


bodies = {"1": [(0, 0, 0)], "2 adj": [(0, 0, 0), (1, 0, 0)], "2 at 2": [(0, 0, 0), (2, 0, 0)],
          "2^3": [(i, j, k) for i in range(2) for j in range(2) for k in range(2)],
          "3^3": [(i, j, k) for i in range(3) for j in range(3) for k in range(3)]}
caps = {k: cap(v) for k, v in bodies.items()}
good = (abs(caps["1"] - 1 / g0w) < 1e-18 and caps["2 adj"] < 2 * caps["1"] and caps["2 at 2"] < 2 * caps["1"]
        and caps["2^3"] / 8 < caps["1"] and caps["3^3"] / 27 < caps["2^3"] / 8)
ok("D2", good, "massless channel, records held at lean 1: u = P(walk reaches the body), far field "
   "(3 cap/2 pi)/r; capacities on Z^3 " + ", ".join(f"{k}: {mp.nstr(v, 8)} ({mp.nstr(v / len(bodies[k]), 5)}/record)"
                                                     for k, v in caps.items())
   + f"; one record's r u(r) -> 3/(2 pi G(0)) = {mp.nstr(3 / (2 * mp.pi * g0w), 6)}")

print(f"runtime {time.time() - T0:.0f} s")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS))
    sys.exit(1)
print("SUMMARY: PARTIAL (a)-(d), exact where rational, certified or high precision otherwise; new here: certified "
      "beta_c, the eigenvalue ordering by a moment identity, mL^2 -> 12(6L-1), the seven-outcome reading at g = 1 "
      "in the ordered sea (mass strength, tricritical point, massless density-lean surface), capacities on Z^3; "
      "sector masses checked on a grid of beta, not proved for every beta.")
print("HIT: sphere menu: beta_c in [0.50855806178558212313, 0.50855806178558212315]; beyond it the turn of the "
      "lean is exactly 1/6 per neighbour and mL^2 -> 12(6L-1), twice the screened side. With 'no record' as a "
      "seventh possibility at g = 1 the content map at density rho is the map with l_k -> rho l_k; in the ordered "
      "sea a record's mass gains the first-order strength (1-rho)(1-<b^5>/<b^6>) > 0 and mixes with the "
      "longitudinal lean, never the turn; the ordering line has a tricritical point at "
      "12 l1^2 + 8 l1 l2 - 5 l1 + 5 l2 = 0 (beta_t = 0.957910880617, rho_t = 0.553095169776), beyond which the "
      "ordering is discontinuous and the density-lean block has a massless surface where mass sources a channel "
      "without a mass term.")
