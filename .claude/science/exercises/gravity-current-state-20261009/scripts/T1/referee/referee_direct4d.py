"""Independent direct-4D check of the T1 continuum coefficients.

This intentionally does not import t1_loop.  It integrates the unexpanded
Euclidean one-loop self energies and takes symmetric external-momentum
differences.  The check is for the Gaussian a2 regulator with twisted mass.
"""

import numpy as np


def grids(nq=150, nx=48, n0=220, qmax=9.0):
    # Spatial radius and polar cosine (the external spatial momentum is x).
    zq, wzq = np.polynomial.legendre.leggauss(nq)
    q = qmax * (zq + 1.0) / 2.0
    wq = wzq * qmax / 2.0
    x, wx = np.polynomial.legendre.leggauss(nx)

    # Direct q0 integral on (-inf,inf), q0 = tan(pi u/2).
    zu, wzu = np.polynomial.legendre.leggauss(n0)
    u = zu
    q0 = np.tan(np.pi * u / 2.0)
    w0 = wzu * (np.pi / 2.0) / np.cos(np.pi * u / 2.0) ** 2
    return q, wq, x, wx, q0, w0


def fields(q, m=0.1, r=1.0):
    g = np.exp(-q * q / 2.0)
    s = q * g
    M = r * (1.0 - g)
    E2 = s * s + M * M + m * m
    w2 = m * m + 2.0 * (1.0 - g)
    return g, s, M, E2, w2


def integrate_a2(p, temporal, m=0.1, r=1.0, n=(150, 48, 220)):
    q, wq, x, wx, q0, w0 = grids(*n)
    q = q[:, None, None]
    x = x[None, :, None]
    q0 = q0[None, None, :]
    measure = (
        (wq[:, None, None] * q[:, :, :1] ** 2)
        * wx[None, :, None]
        * w0[None, None, :]
        / (8.0 * np.pi ** 3)
    )

    g, s, M, E2, w2 = fields(q, m, r)
    den = q0 * q0 + E2

    if temporal:
        # Boson momentum is p-q; second fermion momentum is q+p.
        denb = (p - q0) ** 2 + w2
        i0 = np.sum(measure * q0 * g * g / (den * denb))
        denp = (q0 + p) ** 2 + E2
        num = 4.0 * (M * M - m * m - s * s - q0 * (q0 + p))
        pi = np.sum(measure * g * g * num / (den * denp))
        return i0, pi

    # Boson momentum magnitude |p-q|; second fermion momentum is q+p.
    kmag = np.sqrt(q * q + p * p - 2.0 * q * p * x)
    gp_b, _, _, _, w2p = fields(kmag, m, r)
    ix = np.sum(measure * (s * x) * g * gp_b / (den * (q0 * q0 + w2p)))

    qpmag = np.sqrt(q * q + p * p + 2.0 * q * p * x)
    gp, sp, Mp, E2p, _ = fields(qpmag, m, r)
    # S(q).S(q+p) = g(q) g(q+p) q.(q+p).
    sdot = g * gp * (q * q + q * p * x)
    num = 4.0 * (M * Mp - m * m - sdot - q0 * q0)
    pi = np.sum(measure * g * gp * num / (den * (q0 * q0 + E2p)))
    return ix, pi


def coefficients(h, m=0.1, r=1.0, n=(150, 48, 220)):
    tp, pitp = integrate_a2(+h, True, m, r, n)
    tm, pitm = integrate_a2(-h, True, m, r, n)
    _, pit0 = integrate_a2(0.0, True, m, r, n)
    xp, pixp = integrate_a2(+h, False, m, r, n)
    xm, pixm = integrate_a2(-h, False, m, r, n)
    _, pix0 = integrate_a2(0.0, False, m, r, n)
    A = (tp - tm) / (2.0 * h)
    B = (xp - xm) / (2.0 * h)
    a = (pitp + pitm - 2.0 * pit0) / (2.0 * h * h)
    b = (pixp + pixm - 2.0 * pix0) / (2.0 * h * h)
    k = 16.0 * np.pi**2
    return A, B, a, b, k * ((B - A) - (b - a) / 2.0)


if __name__ == "__main__":
    for h in (0.04, 0.02, 0.01):
        A, B, a, b, delta = coefficients(h)
        print(
            f"h={h:.3f}: 16pi^2 A,B,a,b="
            f"{16*np.pi**2*np.array([A,B,a,b])}; Delta={delta:+.6f}"
        )
