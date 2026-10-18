"""NT-2 O22: open 2x2 block slice (3x3 sites, 12 links, 4 plaquettes, no holonomies).
Point kernel (constants dropped): h(Phi) = int_{[-d,d]^4} de prod_{p=1..4} T(Phi_p + e_{p-1} - e_p) (cyclic, e_0 = e_4),
T(x) = (2d - |x|)_+ (sum of a plaquette's two outer links), e_k = the 4 interior links at the centre site.
Smoothed test functions G_i(phi) = prod_p psi(phi_p - c_ip), psi = normalised cubic B-spline of half-width rho
(support [-rho, rho]); quadratic form Q_ij = (h * Psi^{x4})(c_i - c_j), Psi = psi * psi (even), computed as
Tr(W M1 W M2 W M3 W M4), M_p[y, y'] = (T * Psi)(Delta_p + y - y'), Gauss-Legendre nodes y on [-d, d].
T*Psi is a degree-9 piecewise polynomial; tabulated exactly (up to rounding) as a PPoly."""
import numpy as np
from scipy.interpolate import BSpline, PPoly

def make_TPsi(d, rho, wrap_period=None):
    # Psi = psi * psi with psi = cubic B-spline on [-rho, rho] (unit mass) -> Psi = degree-7 B-spline on [-2rho, 2rho]
    tk = np.linspace(-2 * rho, 2 * rho, 9)
    Psi = BSpline.basis_element(tk, extrapolate=False)
    mass = 4 * rho / 8.0  # integral of a B-spline basis element = (t_last - t_first)/(k+1)
    def Psi_f(y):
        v = Psi(y); return np.where(np.isnan(v), 0.0, v) / mass
    gx, gw = np.polynomial.legendre.leggauss(8)
    def TPsi_exact(x):  # int T(x - y) Psi(y) dy, exact piecewise GL (integrand degree <= 8)
        x = np.atleast_1d(x); out = np.zeros_like(x, dtype=float)
        for i, xv in enumerate(x):
            bps = np.unique(np.clip(np.concatenate([tk, xv + np.array([-2 * d, 0.0, 2 * d])]), -2 * rho, 2 * rho))
            tot = 0.0
            for lo, hi in zip(bps[:-1], bps[1:]):
                if hi - lo < 1e-15: continue
                y = 0.5 * (hi - lo) * gx + 0.5 * (hi + lo)
                tot += 0.5 * (hi - lo) * np.dot(gw, np.maximum(2 * d - np.abs(xv - y), 0.0) * Psi_f(y))
            out[i] = tot
        return out
    knots = np.unique(np.concatenate([tk + c for c in (-2 * d, 0.0, 2 * d)]))
    L = 2 * d + 2 * rho
    knots = np.concatenate([[-L - 1.0], knots, [L + 1.0]])
    C = np.zeros((10, len(knots) - 1))
    for k, (lo, hi) in enumerate(zip(knots[:-1], knots[1:])):
        xs = lo + (hi - lo) * (1 - np.cos(np.pi * (np.arange(10) + 0.5) / 10)) / 2
        ys = TPsi_exact(xs)
        c = np.polyfit(xs - lo, ys, 9) if np.abs(ys).max() > 0 else np.zeros(10)
        C[:, k] = c
    pp = PPoly(C, knots, extrapolate=False)
    def f(x):
        v = pp(x); return np.where(np.isnan(v), 0.0, v)
    return f, TPsi_exact

def h_smooth(Delta, f, y, wts):
    """Delta: (4,) centre differences; returns Tr(W M1 W M2 W M3 W M4)."""
    sw = np.sqrt(wts)
    Ms = [sw[:, None] * f(Delta[p] + y[:, None] - y[None, :]) * sw[None, :] for p in range(4)]
    return np.trace(Ms[0] @ Ms[1] @ Ms[2] @ Ms[3])

def qmatrix(C, f, n, d):
    y, wts = np.polynomial.legendre.leggauss(n); y = d * y; wts = d * wts
    k = len(C); Q = np.zeros((k, k)); cache = {}
    for i in range(k):
        for j in range(i, k):
            D = C[i] - C[j]; key = tuple(np.round(D, 12))
            if key not in cache:
                cache[key] = h_smooth(D, f, y, wts)
            Q[i, j] = Q[j, i] = cache[key]
    return Q
