"""HIER-3 common RG utilities (own code). MSbar QCD beta function to 4 loops,
Lambda parameter in the standard MSbar convention, piecewise running, and the
two-loop SM gauge system with one-loop top Yukawa (comparator coefficients,
Machacek-Vaughn / Arason et al., quoted from memory)."""
import math
import numpy as np
from scipy.integrate import solve_ivp, quad

Z3 = 1.2020569031595942
LN10 = math.log(10.0)
M_PL = 1.2209e19       # B2 anchor, GeV
V_OBS = 246.22         # GeV (comparator; defines the target ratio only)
M_Z = 91.1876


def betas(nf, loops=2):
    """beta_k for a = alpha/(4 pi), da/dln mu^2 = -sum beta_k a^{k+2}."""
    b0 = 11.0 - 2.0 * nf / 3.0
    b1 = 102.0 - 38.0 * nf / 3.0
    b2 = 2857.0 / 2 - 5033.0 * nf / 18 + 325.0 * nf ** 2 / 54
    b3 = (149753.0 / 6 + 3564.0 * Z3) - (1078361.0 / 162 + 6508.0 * Z3 / 27) * nf \
        + (50065.0 / 162 + 6472.0 * Z3 / 81) * nf ** 2 + 1093.0 * nf ** 3 / 729
    return [b0, b1, b2, b3][:loops]


def beta_a(a, nf, loops):
    """da/dln mu^2 (negative for AF)."""
    bs = betas(nf, loops)
    return -sum(b * a ** (k + 2) for k, b in enumerate(bs))


def lnmu2_over_lambda2(a, nf, loops):
    """Standard MSbar convention: ln(mu^2/Lambda^2) = 1/(b0 a) + (b1/b0^2) ln(b0 a)
    + int_0^a [1/beta(x) + 1/(b0 x^2) - b1/(b0^2 x)] dx.  (1-loop: first term only.)"""
    bs = betas(nf, max(loops, 2))
    b0, b1 = bs[0], bs[1]
    if loops == 1:
        return 1.0 / (b0 * a)
    if loops == 2:
        c = b1 / b0
        # exact closed form for the 2-loop integrand: -(c/b0) ln(1 + c a)
        return 1.0 / (b0 * a) + (b1 / b0 ** 2) * math.log(b0 * a) - (c / b0) * math.log1p(c * a)

    bb = betas(nf, loops) + [0.0] * (4 - loops)
    B2, B3 = bb[2], bb[3]

    def integrand(x):
        # exact rational form of 1/beta + 1/(b0 x^2) - b1/(b0^2 x) (no cancellation)
        P = b0 + b1 * x + B2 * x * x + B3 * x ** 3
        return ((b0 * B2 - b1 * b1) + (b0 * B3 - b1 * B2) * x - b1 * B3 * x * x) / (b0 ** 2 * P)
    val, _ = quad(integrand, 0.0, a, epsabs=1e-14, epsrel=1e-12, limit=200)
    return 1.0 / (b0 * a) + (b1 / b0 ** 2) * math.log(b0 * a) + val


def Lambda(mu, alpha, nf, loops):
    a = alpha / (4 * math.pi)
    return mu * math.exp(-0.5 * lnmu2_over_lambda2(a, nf, loops))


def alpha_from_Lambda(mu, Lam, nf, loops):
    """Invert Lambda(mu, alpha) for alpha (perturbative branch)."""
    from scipy.optimize import brentq
    target = 2.0 * math.log(mu / Lam)
    f = lambda la: lnmu2_over_lambda2(math.exp(la), nf, loops) - target
    lo, hi = math.log(1e-9), math.log(0.2)
    return 4 * math.pi * math.exp(brentq(f, lo, hi, xtol=1e-15))


def run_alpha(alpha0, mu0, mu1, nf, loops, events=None):
    """Integrate alpha from mu0 to mu1 (t = ln mu). Returns alpha(mu1) or None if blown up."""
    def rhs(t, y):
        a = y[0]
        return [2.0 * beta_a(a, nf, loops)]  # da/dln mu = 2 da/dln mu^2
    a0 = alpha0 / (4 * math.pi)
    sol = solve_ivp(rhs, (math.log(mu0), math.log(mu1)), [a0], rtol=1e-12, atol=1e-16,
                    method='DOP853', events=events, dense_output=False)
    if sol.status == 1:
        return None, sol
    return 4 * math.pi * sol.y[0, -1], sol


def mu_where_alpha(alpha0, mu0, nf, loops, alpha_target=1.0):
    """Run downward from mu0 until alpha = alpha_target; return mu (None if never)."""
    at = alpha_target / (4 * math.pi)
    def ev(t, y):
        return y[0] - at
    ev.terminal = True
    ev.direction = 1
    t_lo = math.log(mu0) - 2000.0
    def rhs(t, y):
        return [2.0 * beta_a(y[0], nf, loops)]
    sol = solve_ivp(rhs, (math.log(mu0), t_lo), [alpha0 / (4 * math.pi)], rtol=1e-11,
                    atol=1e-16, method='DOP853', events=ev)
    if sol.t_events[0].size:
        return math.exp(sol.t_events[0][0])
    return None


def piecewise_down(alpha_top, mu_top, segments, loops):
    """segments: list of (mu_lower, nf) applied in order going down from mu_top with
    identity matching. Returns alpha at the last mu_lower."""
    a, mu = alpha_top, mu_top
    for mu_low, nf in segments:
        a, _ = run_alpha(a, mu, mu_low, nf, loops)
        if a is None:
            return None
        mu = mu_low
    return a


# ---------------- two-loop SM gauge system (GUT-normalised g1) -----------------
B1L = np.array([41.0 / 10, -19.0 / 6, -7.0])
B2L = np.array([[199.0 / 50, 27.0 / 10, 44.0 / 5],
                [9.0 / 10, 35.0 / 6, 12.0],
                [11.0 / 10, 9.0 / 2, -26.0]])
DYT = np.array([17.0 / 10, 3.0 / 2, 2.0])
GEN1L = 4.0 / 3
GEN2L = np.array([[19.0 / 15, 3.0 / 5, 44.0 / 15],
                  [1.0 / 5, 49.0 / 3, 4.0],
                  [11.0 / 30, 3.0 / 2, 76.0 / 3]])


def sm_rhs_factory(extra_gens=0.0, two_loop=True):
    b1 = B1L + GEN1L * extra_gens
    b2 = B2L + GEN2L * extra_gens
    k = 1.0 / (16 * math.pi ** 2)

    def rhs(t, y):
        g = y[:3]
        yt = y[3]
        g2 = g * g
        dg = np.empty(3)
        for i in range(3):
            two = (b2[i] @ g2 - DYT[i] * yt * yt) * k if two_loop else 0.0
            dg[i] = k * g[i] ** 3 * (b1[i] + two)
        dyt = k * yt * (4.5 * yt * yt - 8 * g2[2] - 2.25 * g2[1] - 0.85 * g2[0])
        return np.concatenate([dg, [dyt]])
    return rhs


def run_sm(y0, mu0, mu1, extra_gens=0.0, two_loop=True):
    sol = solve_ivp(sm_rhs_factory(extra_gens, two_loop), (math.log(mu0), math.log(mu1)), y0,
                    rtol=1e-11, atol=1e-14, method='DOP853')
    return sol.y[:, -1]
