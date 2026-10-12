"""R13-3 (d): Prony (P-T) leakage at a phase transition with a SPECIFIED transition sector.

Units kappa/3 = 1, u = ln a (site-local: the site's own creation count, d/du = (3/c) d/dt).
Local content: radiation x=4 (R0 a^-4), dust x=3 (M0 a^-3), false vacuum rho_v = V_true + Delta*(1 - s(u)).
Transition sectors (stated, the ingredient missing in R11-3):
  S1 (bag model): latent heat -> radiation (w = 1/3) instantly:   rho_r' = -4 rho_r + Delta s'(u)
  S2 (condensate): latent heat -> a pressureless coherent field (w = 0): rho_m' = -3 rho_m + Delta s'(u)
  s(u) = (1 + tanh((u - u_T)/W))/2. W = width in ln a: global percolation (W ~ H/beta) or a single site's wall
  passage (W ~ H * wall thickness / v_w, tiny).
Exact local energy conservation at fixed site volume holds (the release is local), so m_1 is exact; leakage
enters m_2..m_2N (referee: m_2 = 16 rho_r + 9 rho_m - 4 Delta s').
Prony order N (N atoms from m_1..m_2N). The registered F-law uses rho_hat; H^2 = rho_hat (+ memory, unaffected).
Outputs per (sector, alpha = Delta/rho_r(u_T), W, N):
  eps_peak = max |rho_hat/rho_nc - 1|  (subtraction: the exact non-vacuum density rho_nc = rho_r + rho_m)
  I = int (sqrt(rho_hat/rho_nc) - 1) du = integrated extra e-folds created (homogeneous time-shift)
  neg = whether rho_hat <= 0 or nodes complex anywhere (then H^2 <= 0: a clamp is needed)
Tail rule: eps is a transient; 'decays' means |eps| < 1e-6 at |u - u_T| >= 10 W (checked, printed).
"""
import numpy as np
import sympy as sp

uu = sp.symbols('u', real=True)
MAXK = 7


def make_s(W):
    s = (1 + sp.tanh(uu / W)) / 2
    return [sp.lambdify(uu, sp.diff(s, uu, k), 'numpy') for k in range(MAXK + 1)]


R0, M0 = 30.0, 0.5


def moments(u, Delta, sd, sector):
    """Return rho_nc and m_k = (-d/du)^k rho_tot, k = 1..2N_max (vacuum constant part drops)."""
    # integrate the source exactly: comoving radiation/dust constants
    # rho_X(u) = (X0 + Delta * int_{-inf}^u s'(z) e^{x z} dz) e^{-x u}
    from scipy.integrate import quad
    x = 4 if sector == 'S1' else 3
    src = quad(lambda z: Delta * sd[1](z) * np.exp(x * z), -40, u, epsabs=1e-13, epsrel=1e-12, limit=400)[0]
    r = [R0 * np.exp(-4 * u)]
    m = [M0 * np.exp(-3 * u)]
    if sector == 'S1':
        r[0] += src * np.exp(-4 * u)
    else:
        m[0] += src * np.exp(-3 * u)
    v = [0.0]
    for k in range(1, MAXK + 1):
        if sector == 'S1':
            r.append(-4 * r[-1] + Delta * sd[k](u))
            m.append(-3 * m[-1])
        else:
            r.append(-4 * r[-1])
            m.append(-3 * m[-1] + Delta * sd[k](u))
        v.append(-Delta * sd[k](u))
    tot = [r[k] + m[k] + v[k] for k in range(MAXK + 1)]
    mk = [None] + [(-1) ** k * tot[k] for k in range(1, MAXK + 1)]
    return r[0] + m[0], r[0], mk


def prony(mk, N):
    M = np.array(mk[1:2 * N + 1], dtype=float)
    Hk = np.array([[M[i + j] for j in range(N)] for i in range(N)])
    rhs = -np.array([M[N + i] for i in range(N)])
    try:
        c = np.linalg.solve(Hk, rhs)
    except np.linalg.LinAlgError:
        return np.nan, False
    xs = np.roots(np.concatenate(([1.0], c[::-1])))
    V = np.vander(xs, N, increasing=True).T
    wts = np.linalg.solve(V, M[:N].astype(complex))
    val = np.sum(wts / xs)
    ok = np.isfinite(np.real(val)) and np.real(val) > 0          # H^2 > 0 (no clamp needed at this u)
    return float(np.real(val)), ok


print('# sector  alpha   W      N  eps_peak     I(extra e-folds)  clamp_needed(frac u with rho_hat<=0)  |eps| at u_T+10W   eps(u_T)')
for sector in ('S1', 'S2'):
    for alpha in (0.01, 0.1, 0.5):
        for W in (0.3, 0.15, 0.05, 0.005):
            sd = make_s(W)
            Delta = alpha * R0  # rho_r(u_T = 0) ~ R0 (dust negligible at u = 0: M0 = 0.5)
            us = np.linspace(-12 * W, 12 * W, 481)
            for N in (2, 3):
                eps, nbad = [], 0
                for u in us:
                    rnc, rr, mk = moments(u, Delta, sd, sector)
                    rh, ok = prony(mk, N)
                    nbad += (not ok)
                    eps.append(rh / rnc - 1 if ok else np.nan)
                okall = nbad == 0
                rnc0, _, mk0 = moments(0.0, Delta, sd, sector)
                e0 = prony(mk0, N)[0] / rnc0 - 1
                eps = np.array(eps)
                good = np.isfinite(eps)
                integ = np.trapezoid(np.where(good, np.sqrt(np.clip(1 + eps, 0, None)) - 1, 0.0), us)
                tail = abs(eps[-1]) if np.isfinite(eps[-1]) else np.nan
                print(f'{sector:6s} {alpha:5.2f} {W:6.3f}  {N}  {np.nanmax(np.abs(eps)):.3e}   {integ:+.3e}        '
                      f'{"YES" if not okall else "no ":3s} ({nbad/len(us):.3f})                    {tail:.1e}          {e0:+.4f}')
