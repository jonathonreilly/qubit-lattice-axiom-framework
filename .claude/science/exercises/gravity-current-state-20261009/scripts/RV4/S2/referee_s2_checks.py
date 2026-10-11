"""Independent checks for the RV4/S2 referee report.

This intentionally does not import the worker's s2_* implementation.
It checks the load-bearing Jacobian/counterterm identities directly on
midpoint Brillouin-zone grids and verifies the elementary Fourier claims.
"""

from __future__ import annotations

import itertools
import numpy as np


def grid(d: int, n: int):
    k = 2 * np.pi * (np.arange(n) + 0.5) / n
    return np.meshgrid(*([k] * d), indexing="ij")


def symbol(kind: str, k):
    """Return p_i and dp_i/dk_j for three independent test symbols."""
    d = len(k)
    z = np.zeros_like(k[0])
    s = [np.sin(x) for x in k]
    c = [np.cos(x) for x in k]
    if kind == "sin":
        p = s
        dp = [[c[i] if i == j else z for j in range(d)] for i in range(d)]
        return p, dp

    p_diag = [s[i] * np.prod([c[j] for j in range(d) if j != i], axis=0)
              for i in range(d)]
    dp_diag = []
    for i in range(d):
        row = []
        for j in range(d):
            if i == j:
                row.append(c[i] * np.prod([c[q] for q in range(d) if q != i], axis=0))
            else:
                row.append(-s[i] * s[j]
                           * np.prod([c[q] for q in range(d) if q not in (i, j)], axis=0))
        dp_diag.append(row)
    if kind == "diag":
        return p_diag, dp_diag
    if kind == "mix":
        p_sin, dp_sin = symbol("sin", k)
        p = [0.6 * a + 0.4 * b for a, b in zip(p_sin, p_diag)]
        dp = [[0.6 * dp_sin[i][j] + 0.4 * dp_diag[i][j]
               for j in range(d)] for i in range(d)]
        return p, dp
    raise ValueError(kind)


def velocity(kind: str, channel: str, k):
    p, dp = symbol(kind, k)
    d = len(k)
    z = np.zeros_like(k[0])
    if channel == "E":
        v = [0.5 * p[0], -0.5 * p[1]] + [z] * (d - 2)
        div = 0.5 * (dp[0][0] - dp[1][1])
    elif channel == "T2":
        v = [0.5 * p[1], 0.5 * p[0]] + [z] * (d - 2)
        div = 0.5 * (dp[1][0] + dp[0][1])
    elif channel == "tr":
        v = [0.5 * x for x in p]
        div = 0.5 * sum(dp[i][i] for i in range(d))
    else:
        raise ValueError(channel)
    return v, div


def responses(kind: str, channel: str, d: int, n: int, mass: float):
    k = grid(d, n)
    omega2 = mass * mass + sum(2 * (1 - np.cos(x)) for x in k)
    omega = np.sqrt(omega2)
    grad_omega2 = [2 * np.sin(x) for x in k]
    grad_evac = [x / (4 * omega) for x in grad_omega2]
    v, div = velocity(kind, channel, k)
    directional = sum(g * u for g, u in zip(grad_evac, v))
    mu_flow = -np.mean(directional * div)

    # Adding eps^2 G2 to omega^2 contributes G2/(2 omega) to
    # d^2 [omega(eps)/2] / d eps^2 at eps=0.
    g2 = 0.5 * sum(g * u for g, u in zip(grad_omega2, v)) * div
    mu_counterterm = np.mean(g2 / (2 * omega))
    return mu_flow, mu_counterterm, g2, div, omega / 2


def fft_range(field):
    shape = field.shape
    coeff = np.fft.fftn(field) / field.size
    support = np.argwhere(np.abs(coeff) > 1e-11)
    radius = 0
    for q in support:
        radius = max(radius, *(min(int(x), shape[i] - int(x)) for i, x in enumerate(q)))
    return radius, len(support)


def conformal_mode_rank(d: int, nvec):
    """Rank of a -> traceless sym(n tensor a), represented in all entries."""
    n = np.asarray(nvec, float)
    cols = []
    for j in range(d):
        a = np.zeros(d)
        a[j] = 1
        m = 0.5 * (np.outer(n, a) + np.outer(a, n))
        m -= np.trace(m) * np.eye(d) / d
        cols.append(m.ravel())
    return np.linalg.matrix_rank(np.stack(cols, axis=1), tol=1e-12)


def main():
    for d, n in ((2, 192), (3, 56)):
        for kind in ("sin", "diag", "mix"):
            for channel in ("E", "T2"):
                for mass in (1.0, 0.3):
                    flow, ct, _, _, _ = responses(kind, channel, d, n, mass)
                    print(f"d={d} {kind:4s} {channel:2s} M={mass}: "
                          f"mu_flow={flow:+.12e} mu_G2={ct:+.12e} sum={flow+ct:+.3e}")

    flow, ct, g2_m1, div, evac = responses("sin", "E", 3, 56, 1.0)
    _, _, g2_m03, _, _ = responses("sin", "E", 3, 56, 0.3)
    radius, support = fft_range(g2_m1)
    print(f"G2 mass independence maxdiff={np.max(np.abs(g2_m1-g2_m03)):.3e}; "
          f"Fourier max-norm range={radius}, support_modes={support}")

    ed2 = np.mean(evac * div * div)
    mu_half = 0.5 * (flow - 0.5 * ed2)
    cstar = flow / ed2
    print(f"3D NN half-density mu={mu_half:+.12e}; cstar(M=1)={cstar:.8f}")

    ranks = []
    for d in (2, 3):
        for nv in itertools.product(range(-3, 4), repeat=d):
            if any(nv):
                ranks.append((d, nv, conformal_mode_rank(d, nv)))
    bad = [(d, n, r) for d, n, r in ranks if r != d]
    print(f"conformal nonzero-mode full-rank failures={len(bad)}")

    # E-protected body-diagonal Phi in d=3: Phi=1-prod cos(k_i).
    parity_points = [(0, 0, 0), (np.pi, np.pi, 0),
                     (np.pi, 0, np.pi), (0, np.pi, np.pi)]
    phi_values = [1 - np.prod(np.cos(q)) for q in parity_points]
    print("body-diagonal parity zeros=" + ",".join(f"{x:.1e}" for x in phi_values))

    k = grid(3, 48)
    avg_hessian = [np.mean(np.cos(k[i]) * np.prod([np.cos(k[j]) for j in range(3) if j != i], axis=0))
                   for i in range(3)]
    print("body-diagonal <Hess Phi> diagonal=" + ",".join(f"{x:+.2e}" for x in avg_hessian)
          + " so <Hess Phi-I>=-I")

    for d in (2, 3):
        terms = 4 * 5 if d == 2 else 4 * sum(5 - m for m in range(5))
        moments = 3 * d * 4 + 6
        print(f"count d={d}: coefficients={terms}, slope-free={terms-1}, "
              f"Chebyshev moments={moments}, quadratic conditions={2*moments}")


if __name__ == "__main__":
    main()
