"""Independent numerical checks for the C4/RL4 referee report.

This deliberately does not import either rl4_A_lemmaU_constants or
rl4_B_endfactor_turnon.  Derivative envelopes are constructed from the real
critical points of the exponential-polynomial derivatives and integrated by
adaptive quadrature, rather than from the worker's running-maximum grids.
"""

from __future__ import annotations

from math import exp, factorial, log, pi, sqrt

import numpy as np
from scipy.integrate import quad

import rl2_core as rc


SQ = sqrt(pi / 24.0)
TAU1 = 0.1
TAU2 = 0.6
THETA = 10.75


def delta_coefficients(c: np.ndarray, order: int) -> np.ndarray:
    """Coefficients of f^(order)=exp(-m) sum d_n m^n/n!."""
    d = np.asarray(c, dtype=float)
    for _ in range(order):
        d = np.r_[d[1:], 0.0] - d
    return d


def value(c: np.ndarray, order: int, m: float) -> float:
    d = delta_coefficients(c, order)
    terms = np.array([m**n / factorial(n) for n in range(len(d))])
    return exp(-m) * float(d @ terms)


def positive_real_roots(c: np.ndarray, order: int) -> np.ndarray:
    """Positive roots of f^(order), using its ordinary-power polynomial."""
    d = delta_coefficients(c, order)
    p = np.array([d[n] / factorial(n) for n in range(len(d))])
    while len(p) > 1 and abs(p[-1]) < 1e-14:
        p = p[:-1]
    roots = np.polynomial.polynomial.polyroots(p)
    out = sorted(r.real for r in roots if abs(r.imag) < 1e-8 and r.real >= 0)
    return np.asarray(out)


class ExactTailEnvelope:
    def __init__(self, c: np.ndarray, order: int):
        self.c = c
        self.order = order
        # Extrema of |f^(order)| occur at the endpoint or roots of the next
        # derivative (zeros do not increase the absolute value).
        self.extrema = positive_real_roots(c, order + 1)

    def __call__(self, m: float) -> float:
        vals = [abs(value(self.c, self.order, m))]
        vals.extend(
            abs(value(self.c, self.order, x))
            for x in self.extrema
            if x >= m
        )
        return max(vals)


def check_operator(index: int, c: np.ndarray) -> dict[str, float]:
    phi1 = ExactTailEnvelope(c, 1)
    phi2 = ExactTailEnvelope(c, 2)

    f0 = value(c, 0, 0.0)
    v2 = pi * TAU2**4 / 24.0
    dh2 = f0 * (exp(f0 * v2) - 1.0)
    h_inf = f0 + dh2
    h0 = value(c, 0, pi * TAU2**4 / 24.0) - dh2

    def hlow(t: float) -> float:
        m = pi * t**4 / 24.0
        f = value(c, 0, m)
        dh = f0 * (exp(f0 * m) - 1.0)
        return max(f - dh, 0.0)

    iw = quad(lambda t: t * hlow(t) ** 2, TAU1, TAU2,
              epsabs=2e-12, epsrel=2e-12, limit=300)[0]
    psi1 = quad(lambda x: phi1(x * x), 0.0, np.inf,
                epsabs=2e-10, epsrel=2e-10, limit=500)[0]
    s2 = quad(lambda x: sqrt(phi2(pi * x * x / 24.0)), 0.0, np.inf,
              epsabs=2e-9, epsrel=2e-9, limit=500)[0]
    psi0 = phi1(0.0)

    c_inv = 4.0 * TAU2**2 * exp(-THETA) / SQ
    arg = SQ * exp(THETA) * TAU2**2 * psi0 / (4.0 * psi1)
    qll = c_inv * psi1 * (1.0 + log(max(1.0, arg)))
    qpl = 4.0 * (TAU2 / TAU1) * exp(-THETA) * psi1 / SQ
    pp_arg = SQ * exp(THETA) * TAU1**2 / 4.0
    qpp = phi1(pp_arg**2)

    a = exp(THETA) * TAU1 / (2.0 * TAU2)
    e2_integrated = s2 / a
    # Use the worker's deliberately weaker point-end lower argument.
    e2_point = sqrt(phi2(pi * (a * TAU1**2) ** 2 / 24.0))
    e2 = max(e2_integrated, e2_point)

    max_c = float(np.max(np.abs(c)))
    worst_log_per_vertex = -np.inf
    worst_g = None
    worst_raw_log = None
    for g in range(3, 1001):
        m = pi * ((g - 2) * TAU1**2 * exp(THETA)) ** 2 / 24.0
        raw_log = (
            g * log(2.0)
            + log(6.0 * max_c)
            - m
            + 5.0 * log(1.0 + m)
            + 2.0 * log(1.0 + h_inf * (pi / 2.0) * TAU2**4)
        )
        if raw_log / g > worst_log_per_vertex:
            worst_log_per_vertex = raw_log / g
            worst_raw_log = raw_log
            worst_g = g
    qg = exp(worst_log_per_vertex) if worst_log_per_vertex > -745 else 0.0

    e_weight = h_inf * (pi / 2.0) * TAU2**2
    omega = pi / 2.0 + h_inf * (pi / 2.0) ** 2 * TAU2**4
    q = max(qll, qpl, qpp, e2, qg)
    k_end = max(1.0, (1.0 + e_weight) ** 2 / (2.0 * omega * h0))
    delta = k_end * 2.0 * omega * q / h0
    clow = (1.0 - 2.0 * delta) * sqrt(pi * iw)

    return {
        "op": index,
        "h_band": dh2,
        "h_inf": h_inf,
        "h0": h0,
        "psi0": psi0,
        "Psi1": psi1,
        "S2": s2,
        "QLL": qll,
        "QPL": qpl,
        "QPP": qpp,
        "E2": e2,
        "qg": qg,
        "qg_worst_g": worst_g,
        "qg_worst_raw_log": worst_raw_log,
        "delta": delta,
        "IW": iw,
        "clow_no_err": clow,
    }


if __name__ == "__main__":
    for i, coefficients in enumerate(rc.OPS):
        result = check_operator(i, coefficients)
        print(" ".join(f"{k}={v}" for k, v in result.items()))
