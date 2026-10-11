"""Independent numerical checks for the D2 referee.

This does not import the worker's helpers.  It evaluates the continuum BW1
integral for the Q4 Cherenkov example, differentiates the implicit pole
equation at the face, and fits the archived ED/residue sequences.
"""

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar


TWOPI = 2.0 * np.pi


def q4(k):
    return (1.0 - np.cos(k)) ** 2


def q4_prime(k):
    return 2.0 * (1.0 - np.cos(k)) * np.sin(k)


def q4_second(k):
    return 2.0 * (np.sin(k) ** 2 + (1.0 - np.cos(k)) * np.cos(k))


def omega(q, c):
    return 2.0 * c * abs(np.sin(q / 2.0))


def threshold_minimizer(c):
    # At K=pi, q=pi-k and P=eps(k)+2c|cos(k/2)|.
    result = minimize_scalar(
        lambda k: q4(k) + 2.0 * c * abs(np.cos(k / 2.0)),
        bounds=(0.0, np.pi),
        method="bounded",
        options={"xatol": 1e-14},
    )
    return result.x, result.fun


def threshold_curvature_comparison(c):
    """One-sided envelope curvature versus the SLAC value with same E and slope."""
    kstar, energy = threshold_minimizer(c)
    slope = abs(q4_prime(kstar))
    matter_curvature = q4_second(kstar)
    phonon_curvature = -0.5 * c * np.cos(kstar / 2.0)
    envelope_curvature = (
        matter_curvature * phonon_curvature /
        (matter_curvature + phonon_curvature)
    )
    slac_curvature = slope / np.pi - slope**2 / energy
    return envelope_curvature, slac_curvature


def quad_split(func, points):
    edges = [0.0] + sorted(points) + [TWOPI]
    return sum(
        quad(func, lo, hi, epsabs=2e-11, epsrel=2e-11, limit=500)[0]
        for lo, hi in zip(edges[:-1], edges[1:])
    )


def continuum_face_pole(c, g2):
    kstar, threshold = threshold_minimizer(c)
    qstars = [np.pi - kstar, np.pi + kstar]

    def pole(q):
        return q4(np.pi - q) + omega(q, c)

    def weight(q):
        return g2 * 2.0 * abs(np.sin(q / 2.0))

    def sigma(lam):
        return quad_split(lambda q: weight(q) / (lam - pole(q)), qstars) / TWOPI

    def equation(lam):
        return lam - q4(np.pi) - sigma(lam)

    # The smallest physical gap below is O(1e-5); 1e-9 is safely above the
    # root and avoids asking quadrature to sample an artificial 1e-13 gap.
    lam = brentq(equation, threshold - 20.0, threshold - 1e-9, xtol=2e-13)

    def moments(q):
        den = lam - pole(q)
        pk = q4_prime(np.pi - q)
        pkk = q4_second(np.pi - q)
        w = weight(q)
        return np.array((w / den**2, w * (pkk / den**2 + 2.0 * pk**2 / den**3)))

    pieces = []
    edges = [0.0] + qstars + [TWOPI]
    for lo, hi in zip(edges[:-1], edges[1:]):
        pieces.append(
            np.array(
                [
                    quad(lambda q, j=j: moments(q)[j], lo, hi,
                         epsabs=2e-10, epsrel=2e-10, limit=500)[0]
                    for j in range(2)
                ]
            )
        )
    J, Ikk = np.sum(pieces, axis=0) / TWOPI
    Z = 1.0 / (1.0 + J)
    epp = (q4_second(np.pi) + Ikk) * Z
    curvature = -epp
    slope = abs(q4_prime(kstar))
    ell = slope / curvature
    return kstar, threshold, threshold - lam, Z, curvature, ell, Z / ell, slope


def log_fit(xs, ys):
    slope, intercept = np.polyfit(np.log(xs), np.log(ys), 1)
    return slope, np.exp(intercept)


def threshold_at(k, c):
    """Global one-phonon threshold using local minimization, not a q lattice."""
    qgrid = np.linspace(-np.pi, np.pi, 129)
    dq = qgrid[1] - qgrid[0]
    objective = lambda q: q4(k - q) + omega(q, c)
    values = np.array([objective(q) for q in qgrid])
    candidates = [values.min(), objective(0.0)]
    for i in np.argsort(values)[:6]:
        result = minimize_scalar(objective, bounds=(qgrid[i] - dq, qgrid[i] + dq),
                                 method="bounded", options={"xatol": 2e-13})
        candidates.append(result.fun)
    return min(candidates)


def independent_threshold_fits():
    k = np.linspace(0.0, np.pi, 1025)
    energy = np.array([threshold_at(x, 1.0) for x in k])
    bandwidth = energy.max() - energy.min()
    for window in (np.pi / 8.0, np.pi / 4.0, np.pi / 2.0):
        select = k >= np.pi - window - 1e-12
        x = k[select] ** 2
        y = energy[select] ** 2
        design = np.vstack((np.ones_like(x), x)).T
        m02, beta = np.linalg.lstsq(design, y, rcond=None)[0]
        fit = np.sqrt(np.clip(m02 + beta * x, 0.0, None))
        deviation = np.max(np.abs(fit - energy[select])) / bandwidth
        chord = (energy[-1] - energy[-2]) / (k[-1] - k[-2])
        slope_ratio = chord / (beta * np.pi / energy[-1])
        print("threshold fit w=%.9g dev=%.7f slope_ratio=%.6f" %
              (window, deviation, slope_ratio))


def report_scalings():
    # g2 is the worker's variable g^2.  A slope two therefore means g^4.
    g2 = np.array([0.03, 0.01, 0.003])
    z_generic = np.array([2.4515e-3, 2.8395e-4, 2.5899e-5])
    print("generic Z vs g2, last three: exponent=%.5f" % log_fit(g2, z_generic)[0])

    n = np.array([8.0, 12.0, 16.0, 20.0, 24.0])
    z03 = np.array([0.7572, 0.7416, 0.7313, 0.7236, 0.7176])
    z10 = np.array([0.5048, 0.4722, 0.4513, 0.4367, 0.4250])
    gamma03 = -log_fit(n, z03)[0]
    gamma10 = -log_fit(n, z10)[0]
    print("ED gamma(g2=.3)=%.5f gamma(g2=1)=%.5f ratio=%.4f" %
          (gamma03, gamma10, gamma10 / gamma03))


if __name__ == "__main__":
    print("# independent continuum Q4 BW1 face calculation")
    print("# c g2 kstar threshold gap Z curvature ell Z/ell threshold_slope")
    weak_g2 = np.array((0.03, 0.01, 0.003))
    for c in (0.4, 1.0):
        face_rows = []
        for g2 in weak_g2:
            vals = continuum_face_pole(c, g2)
            face_rows.append(vals)
            print(("%.1f %.3g " + " ".join(["%.9g"] * 8)) % ((c, g2) + vals))
        z_exponent = log_fit(weak_g2, np.array([row[3] for row in face_rows]))[0]
        ell_exponent = log_fit(weak_g2, np.array([row[5] for row in face_rows]))[0]
        print("Q4 c=%.1f weak exponents vs g2: Z=%.5f ell=%.5f" %
              (c, z_exponent, ell_exponent))
        actual_c2, slac_c2 = threshold_curvature_comparison(c)
        print("Q4 c=%.1f threshold one-side curvature=%.7f matched-SLAC curvature=%.7f" %
              (c, actual_c2, slac_c2))
    independent_threshold_fits()
    report_scalings()
