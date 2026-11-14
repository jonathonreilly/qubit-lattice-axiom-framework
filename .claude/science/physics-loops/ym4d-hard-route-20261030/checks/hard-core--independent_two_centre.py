#!/usr/bin/env python3
"""Two centres, (2C) of Text 4.7: a toy that tests the algebra and the logic of the claim, and nothing about the 4D chart.

Claim under test. Let the coordinate origin V^# be strictly local in W, at a radius free of g, and let the Gaussian mean be the
exact minimiser V^*. With b = b^* + b_hat, b^* := position of V^* in the chart at V^#, and b_hat = 2^{-1/2} g P xi_eff, put
s_J := 2^{1/2} P^+ b^* / g and x := xi_eff + s_J. Then b = 2^{-1/2} g P x, at fixed x the field reads W only nearby, and far W
enters only through the centre of the product Gaussian of x. So a sharp cut on x and a sharp function of the field, read together,
are analytic in far W, however large s_J is in noise units, and with no accuracy of V^# in powers of g.

Model. Periodic chain of N sites. W is a real vector w. H(w) := -Delta + m^2 + diag(u0 w^2), V^*(w) := H(w)^{-1} w. V^#(w)_i is the
same solve on a window of radius R about i, with reflecting ends. A^#, the local form, is the same operator with w^2 replaced by its
average over a window of radius 3, so it is deliberately inaccurate. P is a Chebyshev polynomial of degree D in (A^# + m0^2),
approximating (A^# + m0^2)^{-1/2}.

PRE-STATED CRITERIA, written before the first run.

Part A, one chain, N = 128, m = 0.3, m0 = 0.3, u0 = 0.05, w a fixed random vector of sup 1, R = 16, D = 40, g = 1e-3.
PASS-SPLIT   if || A^{-1} - (1/2) P P^T - G_1 G_1^T - G_2 G_2^T || <= 1e-9, with A := H(w), C_1 := (A + m0^2)^{-1}, Delta from P, G_1 :=
             2^{-1/2} C_1^{1/2} (1 - Delta)^{1/2}, G_2 := m0 A^{-1/2} C_1^{1/2}, and ||Delta|| <= 1/2. The form used in P is the wrong one.
PASS-MEAN    if || 2^{-1/2} g P s_J - b^* || <= 1e-9 ||b^*||.
PASS-SIZE    if at g = 1e-3 and at g = 1e-5 the sup of |s_J| exceeds 10 (so above any cut of order p in this toy) and is proportional to
             1 / g within 1 percent: the mean is far from the origin in noise units, and nothing below minds that.
PASS-LOCAL   if at fixed x, moving w_j at distance above R + D + 2 from i changes V_i by at most 1e-13.
CONTROL-LOCAL  the chart centred at V^*, at fixed xi_eff, must change V_i by at least 1e-10 under the same move. Without this PASS-LOCAL
             would show nothing.

Part B, analyticity against a kink. Two noise variables, Phi = 1, a sharp field function e = 1[alpha . x > a_0], alpha = (1, 0.7), a_0 = 0.4,
and a parameter w0 for far W, through the centre s(w0) = (0.3 w0, -0.2 w0).
Gamma_x(w0)  := int over the box |x_i| <= p of rho(x - s(w0)) e(x) dx: the cut in x, W free. Everything about far W is in the density.
Gamma_xi(w0) := int over the box |xi_i| <= p of rho(xi) e(xi + s(w0)) d xi: the cut in the real noise, read at an old polymer.
On w0 in [-1, 1], p = 2.0, Chebyshev fit of degree 24, residual on a grid of 2001 points.
PASS-ANALYTIC if the residual of Gamma_x is at most 1e-9.
CONTROL-KINK  if the residual of Gamma_xi is at least 1e-7. This must hold, or the test has no power and is void.

Part C, the cut against state A at a complex centre. One variable, 60 digits, Phi(x) = exp(0.01 i x - 0.002 x^2), p = 10, p_2 = 80,
s = 1 + i y, y in (0, 1, 5, 10) (the last is p_2 / 8, and above p). G(s) := int_{|x| <= p_2} rho(x - s) Phi(x) dx - int_{|xi| <= p} rho(xi) Phi(xi + s) d xi.
PASS-GOODL if |G(s)| <= 2 exp(-p^2 / 3) sup |Phi(xi + s)| over real xi, for all these y, and at y = 10 the modulus bound exp(y^2 / 2) of the
density exceeds |G| by at least 1e3.

RESULT OF THE FIRST RUN, as registered: PASS-SPLIT (||Delta|| = 0.0365, residual 4e-14), PASS-MEAN, PASS-SIZE (sup |s_J| = 42 at g = 1e-3, 4237 at g = 1e-5),
PASS-LOCAL (9.5e-14, narrowly), CONTROL-LOCAL-OK (2.3e-9), PASS-GOODL (|G| about 1e-23, modulus bound 5e21 at y = 10). **CONTROL-KINK-VOID:** residual of Gamma_xi 7e-16, so Part B had no
power: the line alpha . xi = a_0 - (0.16 w0 sign) only runs over [0.24, 0.56], and it meets a corner of the box only at 0.6 or 3.4. That is an error of my registration, so PASS-ANALYTIC at that run
says nothing. PASS-LOCAL was narrow for a reason that is an error of the toy: the Chebyshev interval read the extreme eigenvalues of the whole form, so P read far w by a rounding-sized amount.
ADDED BEFORE THE SECOND RUN: a_0 = 0.6, so the line runs through the corner (p, -p) of the box at w0 = 0, inside the range; the Chebyshev interval is a fixed one, [0.9 (m^2 + m0^2), 1.1 (4 + m^2 + m0^2 + u0)].
The criteria for Part B are unchanged: PASS-ANALYTIC2 if the residual of Gamma_x is at most 1e-9, CONTROL-KINK2-OK if that of Gamma_xi is at least 1e-7. PASS-LOCAL2: the same move, at most 1e-15.

RESULT OF THE SECOND RUN, as registered: PASS-LOCAL2 (exactly 0), PASS-ANALYTIC2 (6.7e-16), **CONTROL-KINK2-VOID**: residual of Gamma_xi 3.25e-8 against my floor 1e-7, a floor I set without computing. It is 5e7 times the residual of
Gamma_x, so a kink is there, but the registered control did not pass. ADDED BEFORE THE THIRD RUN: p = 1.0, a_0 = 0.3, the same corner, where rho at the corner is larger. Criteria unchanged: PASS-ANALYTIC3 at most 1e-9, CONTROL-KINK3-OK at least 1e-7.

RESULT OF THE THIRD RUN, as registered: PASS-ANALYTIC3 (2.5e-16), CONTROL-KINK3-OK (6.5e-7), with PASS-SPLIT, PASS-MEAN, PASS-SIZE, PASS-LOCAL2, CONTROL-LOCAL-OK, PASS-GOODL unchanged.

The script checks its own RSS against 2 GB. It proves no bound about the 4D chart. It only tests that the two-centre identity, the logic of
where far W enters, and the contour step do what the text says.
"""
import os
import resource
import sys

os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
import numpy as np
from numpy.polynomial import chebyshev as cheb
from scipy import linalg as sla
from scipy import special as ssp
from scipy.integrate import quad
import mpmath as mp

RSS_LIMIT_KB = 2 * 1024 * 1024


def check_rss():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == "darwin":
        rss /= 1024
    if rss > RSS_LIMIT_KB:
        sys.exit("RSS above 2 GB, stopping")


N, M_SQ, M0_SQ, U0 = 128, 0.09, 0.09, 0.05
RADIUS, DEG = 16, 40


def laplacian(n, periodic=True):
    L = np.zeros((n, n))
    for i in range(n):
        L[i, i] = 2.0
        L[i, (i + 1) % n] -= 1.0
        L[(i + 1) % n, i] -= 1.0
    if not periodic:
        L[0, n - 1] = L[n - 1, 0] = 0.0
        L[0, 0] = L[n - 1, n - 1] = 1.0
    return L


def exact_form(w):
    return laplacian(N) + np.diag(M_SQ + U0 * w * w)


def v_star(w):
    return np.linalg.solve(exact_form(w), w)


def v_sharp(w, radius=RADIUS):
    """Solve on a window of radius R about each site, with reflecting ends: the strictly local field."""
    out = np.zeros(N)
    size = 2 * radius + 1
    lap = laplacian(size, periodic=False)
    for i in range(N):
        idx = [(i + d) % N for d in range(-radius, radius + 1)]
        wl = w[idx]
        out[i] = np.linalg.solve(lap + np.diag(M_SQ + U0 * wl * wl), wl)[radius]
    return out


def local_form(w):
    """A^#: the inaccurate local form, w^2 averaged over a window of radius 3."""
    w2 = np.array([np.mean([w[(i + d) % N] ** 2 for d in range(-3, 4)]) for i in range(N)])
    return laplacian(N) + np.diag(M_SQ + U0 * w2)


def cheb_inv_sqrt(a, deg):
    """Chebyshev polynomial of degree deg in a, approximating a^{-1/2}. Strictly banded, of range deg."""
    lo, hi = 0.9 * (M_SQ + M0_SQ), 1.1 * (4.0 + M_SQ + M0_SQ + U0)
    nodes = np.cos(np.pi * (np.arange(deg + 1) + 0.5) / (deg + 1))
    vals = (0.5 * (hi - lo) * nodes + 0.5 * (hi + lo)) ** -0.5
    coef = cheb.chebfit(nodes, vals, deg)
    t = (2.0 * a - (hi + lo) * np.eye(len(a))) / (hi - lo)
    t0, t1 = np.eye(len(a)), t
    out = coef[0] * t0 + coef[1] * t1
    for c in coef[2:]:
        t0, t1 = t1, 2.0 * t @ t1 - t0
        out = out + c * t1
    return out


def sym_fun(a, f):
    e, q = np.linalg.eigh(0.5 * (a + a.T))
    return (q * f(e)) @ q.T


def build_p(w):
    return cheb_inv_sqrt(local_form(w) + M0_SQ * np.eye(N), DEG)


def part_a():
    rng = np.random.default_rng(7)
    w = rng.uniform(-1.0, 1.0, N)
    w = w / np.max(np.abs(w))
    a_star = exact_form(w)
    p_mat = build_p(w)
    c1 = np.linalg.inv(a_star + M0_SQ * np.eye(N))
    c1_half = sym_fun(c1, np.sqrt)
    c1_minus = np.linalg.inv(c1_half)
    delta = c1_minus @ p_mat @ p_mat.T @ c1_minus - np.eye(N)
    delta_norm = np.linalg.norm(delta, 2)
    root = sym_fun(np.eye(N) - delta, lambda e: np.sqrt(np.clip(e, 0.0, None)))
    g1 = c1_half @ root / np.sqrt(2.0)
    a_inv_half = sym_fun(np.linalg.inv(a_star), np.sqrt)
    g2 = np.sqrt(M0_SQ) * a_inv_half @ c1_half
    resid = np.linalg.norm(np.linalg.inv(a_star) - 0.5 * p_mat @ p_mat.T - g1 @ g1.T - g2 @ g2.T, 2)
    print(f"Part A: ||Delta|| = {delta_norm:.4f}, split residual = {resid:.2e}")
    verdict_split = "PASS-SPLIT" if resid <= 1e-9 and delta_norm <= 0.5 else "FAIL-SPLIT"

    vs, vh = v_star(w), v_sharp(w)
    b_star = vs - vh
    print(f"  sup |V^*| = {np.max(np.abs(vs)):.4f}, sup |V^# - V^*| = {np.max(np.abs(b_star)):.3e}")
    p_plus = p_mat.T @ np.linalg.inv(p_mat @ p_mat.T)
    sup_sj = {}
    verdict_mean = "PASS-MEAN"
    for g in (1e-3, 1e-5):
        s_j = np.sqrt(2.0) * p_plus @ b_star / g
        err = np.linalg.norm(p_mat @ s_j * g / np.sqrt(2.0) - b_star)
        if err > 1e-9 * np.linalg.norm(b_star):
            verdict_mean = "FAIL-MEAN"
        sup_sj[g] = np.max(np.abs(s_j))
        print(f"  g = {g:.0e}: sup |s_J| = {sup_sj[g]:.3e}, mean error = {err:.2e}")
    ratio = sup_sj[1e-5] / sup_sj[1e-3] / 100.0
    verdict_size = "PASS-SIZE" if min(sup_sj.values()) > 10.0 and abs(ratio - 1.0) <= 0.01 else "FAIL-SIZE"

    # Locality at fixed x, and the control: the chart centred at V^*.
    g = 1e-3
    x = rng.normal(size=N)
    i, j = 10, (10 + RADIUS + DEG + 5) % N
    w2 = w.copy()
    w2[j] += 0.5
    p2 = build_p(w2)
    field_x = lambda vh_, p_: vh_ + g * p_ @ x / np.sqrt(2.0)
    change_x = abs(field_x(v_sharp(w2), p2)[i] - field_x(v_sharp(w), p_mat)[i])
    field_c = lambda vs_, p_: vs_ + g * p_ @ x / np.sqrt(2.0)
    change_c = abs(field_c(v_star(w2), p2)[i] - field_c(v_star(w), p_mat)[i])
    print(f"  at fixed x, |delta V_i| = {change_x:.3e}; centred at V^*, |delta V_i| = {change_c:.3e}")
    verdict_local = "PASS-LOCAL2" if change_x <= 1e-15 else "FAIL-LOCAL2"
    verdict_ctrl = "CONTROL-LOCAL-OK" if change_c >= 1e-10 else "CONTROL-LOCAL-VOID"
    print(" ", verdict_split, verdict_mean, verdict_size, verdict_local, verdict_ctrl)
    check_rss()


PBOX, A0, ALPHA = 1.0, 0.3, (1.0, 0.7)


def pdf(t):
    return np.exp(-t * t / 2.0) / np.sqrt(2.0 * np.pi)


def cdf(t):
    return 0.5 * ssp.erfc(-t / np.sqrt(2.0))


def gamma_x(w0):
    """Cut on x, field function on x, density centred at s(w0)."""
    s1, s2 = 0.3 * w0, -0.2 * w0
    def inner(x1):
        low = max((A0 - ALPHA[0] * x1) / ALPHA[1], -PBOX)
        if low >= PBOX:
            return 0.0
        return pdf(x1 - s1) * (cdf(PBOX - s2) - cdf(low - s2))
    pts = [(A0 - ALPHA[1] * PBOX) / ALPHA[0], (A0 + ALPHA[1] * PBOX) / ALPHA[0]]
    pts = [q for q in pts if -PBOX < q < PBOX]
    return quad(inner, -PBOX, PBOX, points=pts or None, epsabs=1e-13, epsrel=1e-13, limit=400)[0]


def gamma_xi(w0):
    """Cut on the real noise, field function read at xi + s(w0)."""
    s1, s2 = 0.3 * w0, -0.2 * w0
    shift = A0 - ALPHA[0] * s1 - ALPHA[1] * s2
    def inner(x1):
        low = max((shift - ALPHA[0] * x1) / ALPHA[1], -PBOX)
        if low >= PBOX:
            return 0.0
        return pdf(x1) * (cdf(PBOX) - cdf(low))
    pts = [(shift - ALPHA[1] * PBOX) / ALPHA[0], (shift + ALPHA[1] * PBOX) / ALPHA[0]]
    pts = [q for q in pts if -PBOX < q < PBOX]
    return quad(inner, -PBOX, PBOX, points=pts or None, epsabs=1e-13, epsrel=1e-13, limit=400)[0]


def cheb_residual(f, deg=24, grid=2001):
    nodes = np.cos(np.pi * (np.arange(deg + 1) + 0.5) / (deg + 1))
    coef = cheb.chebfit(nodes, [f(t) for t in nodes], deg)
    pts = np.linspace(-1.0, 1.0, grid)
    return np.max(np.abs(cheb.chebval(pts, coef) - np.array([f(t) for t in pts])))


def part_b():
    # Kink position: a line through a corner of the box. Choose the shift so it occurs inside the range of w0.
    res_x, res_xi = cheb_residual(gamma_x), cheb_residual(gamma_xi)
    print(f"Part B: residual of Gamma_x = {res_x:.2e}, residual of Gamma_xi = {res_xi:.2e}")
    print(" ", "PASS-ANALYTIC3" if res_x <= 1e-9 else "FAIL-ANALYTIC3", "CONTROL-KINK3-OK" if res_xi >= 1e-7 else "CONTROL-KINK3-VOID")
    check_rss()


def part_c():
    mp.mp.dps = 60
    p, p2 = mp.mpf(10), mp.mpf(80)
    rho = lambda z: mp.exp(-z * z / 2) / mp.sqrt(2 * mp.pi)
    Phi = lambda z: mp.exp(0.01j * z - mp.mpf("0.002") * z * z)
    ok = True
    for y in (0, 1, 5, 10):
        s = mp.mpc(1, y)
        mu = mp.quad(lambda t: rho(t - s) * Phi(t), mp.linspace(-p2, p2, 33))
        mu_a = mp.quad(lambda t: rho(t) * Phi(t + s), mp.linspace(-p, p, 17))
        g_val = abs(mu - mu_a)
        sup_phi = max(abs(Phi(t + s)) for t in mp.linspace(-p, p, 401))
        bound = 2 * mp.exp(-p * p / 3) * sup_phi
        mod = mp.exp(mp.mpf(y) * y / 2)
        print(f"Part C: y = {y}: |G| = {mp.nstr(g_val, 5)}, bound = {mp.nstr(bound, 5)}, |mu_A| = {mp.nstr(abs(mu_a), 5)}, modulus bound = {mp.nstr(mod, 5)}")
        ok = ok and g_val <= bound
        if y == 10:
            ok = ok and mod >= 1e3 * g_val
    print(" ", "PASS-GOODL" if ok else "FAIL-GOODL")
    check_rss()


if __name__ == "__main__":
    part_a()
    part_b()
    part_c()
