#!/usr/bin/env python3
"""Supervisor control for block 110 (floating point; not part of the exact runner).

Rays of H = c(x)|k| integrated directly in three Cartesian dimensions, for the curvature member's exterior
chi = 1 + a/r, N = 1 - p/r (index chi^3/N) at a fixed first-order turn 4M/b (3a + p = 2M, M = 1) and charge ratios
rho = p/a = 1/2, 1, 3, and for the log-linear completion e^(2A/r) (A = 1). Compared with (i) the exact one-dimensional
quadrature of the half-turn and (ii) the series of the note to fourth order; capture bracketed around the threshold.
"""
import math
import warnings
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq

warnings.filterwarnings("ignore")


def members(rho):
    a = 2.0 / (3.0 + rho)
    p = rho * a
    return a, p


def index_curv(a, p):
    return lambda r: (1 + a / r) ** 3 / (1 - p / r)


def dindex_curv(a, p):
    def dn(r):
        n = (1 + a / r) ** 3 / (1 - p / r)
        return n * (-3 * a / (r * r * (1 + a / r)) - p / (r * r * (1 - p / r)))
    return dn


def index_exp(k, A):
    return lambda r: math.exp(k * A / r)


def dindex_exp(k, A):
    return lambda r: -k * A / (r * r) * math.exp(k * A / r)


def ray_turn(n, dn, b, r_stop, L=2.0e5):
    """Integrate dx/dt = c khat, dk/dt = -|k| grad c with c = 1/n; E = 1 so |k| = n. Returns the turn, or None if captured."""
    x0 = np.array([-L, b, 0.0])
    r0 = np.linalg.norm(x0)
    k0 = np.array([n(r0), 0.0, 0.0])
    J = b * n(r0)

    def rhs(t, y):
        x, k = y[:3], y[3:]
        r = np.linalg.norm(x)
        kn = np.linalg.norm(k)
        c = 1.0 / n(r)
        dc = -dn(r) / n(r) ** 2
        return np.concatenate([c * k / kn, -kn * dc * x / r])

    def hit(t, y):
        return np.linalg.norm(y[:3]) - r_stop
    hit.terminal = True

    def out(t, y):
        return y[0] - L if y[3] > 0 else -1.0
    out.terminal = True
    sol = solve_ivp(rhs, (0, 50 * L), np.concatenate([x0, k0]), method="DOP853", rtol=1e-11, atol=1e-11, events=(hit, out))
    if sol.t_events[0].size:
        return None, J
    kf = sol.y[3:, -1]
    ang = math.atan2(-kf[1], kf[0])
    return ang, J


def quad_turn(n, b, r_lo):
    F = lambda r: r * n(r)
    r0 = brentq(lambda r: F(r) - b, r_lo, 1e6 * b)
    # half-turn = int_{r0}^inf b dr/(r sqrt(F^2 - b^2)); substitute r = r0/(1 - s^2) to soften the endpoint
    def integrand(s):
        if s <= 0:
            s = 1e-300
        r = r0 / (1 - s * s) if s < 1 else float("inf")
        if not math.isfinite(r):
            return 0.0
        drds = 2 * s * r0 / (1 - s * s) ** 2
        val = F(r) ** 2 - b * b
        return b * drds / (r * math.sqrt(max(val, 1e-300)))
    half, _ = quad(integrand, 0, 1, limit=400, epsabs=1e-13, epsrel=1e-13)
    return 2 * half - math.pi


def series_curv(a, p, b):
    c = [2 * (3 * a + p), 1.5 * math.pi * (5 * a * a + 4 * a * p + p * p), (8 / 3) * (42 * a ** 3 + 54 * a * a * p + 27 * a * p * p + 5 * p ** 3),
         (15 * math.pi / 8) * (99 * a ** 4 + 176 * a ** 3 * p + 132 * a * a * p * p + 48 * a * p ** 3 + 7 * p ** 4)]
    return sum(ci / b ** (i + 1) for i, ci in enumerate(c))


def bc_curv(a, p):
    rs = a + p + math.sqrt(a * a + a * p + p * p)
    return (rs + a) ** 3 / (rs * (rs - p)), rs


print("curvature member, M = 1 (3a + p = 2):")
for rho in (0.5, 1.0, 3.0):
    a, p = members(rho)
    n, dn = index_curv(a, p), dindex_curv(a, p)
    bc, rs = bc_curv(a, p)
    rows = []
    for b in (40.0, 12.0, 8.0):
        t_ray, J = ray_turn(n, dn, b, r_stop=max(p, 1e-3) * 1.0001 + 1e-3)
        t_q = quad_turn(n, J, rs)
        rows.append(f"b={b:5.1f}: ray {t_ray:.9f}  quadrature {t_q:.9f}  series(4) {series_curv(a, p, J):.9f}")
    lo, _ = ray_turn(n, dn, bc * (1 - 1e-3), r_stop=(rs + p) / 2)
    hi, _ = ray_turn(n, dn, bc * (1 + 1e-3), r_stop=(rs + p) / 2)
    print(f"  rho = {rho}: a = {a:.6f}, p = {p:.6f}, r* = {rs:.6f}, b_c = {bc:.6f}")
    for row in rows:
        print("    " + row)
    print(f"    b = b_c(1 - 1e-3): {'captured' if lo is None else 'escapes'};  b = b_c(1 + 1e-3): {'captured' if hi is None else 'escapes'}")

print("log-linear completion e^(2A/r), A = 1 (first-order turn 4/b): capture threshold 2e =", round(2 * math.e, 6))
n, dn = index_exp(2.0, 1.0), dindex_exp(2.0, 1.0)
for b in (40.0, 12.0, 8.0):
    t_ray, J = ray_turn(n, dn, b, r_stop=0.2)
    t_q = quad_turn(n, J, 2.0)
    ser = sum(c * (2.0 / J) ** (i + 1) for i, c in enumerate((2, math.pi, 6, 4 * math.pi, 250 / 9, 81 * math.pi / 4)))
    print(f"    b={b:5.1f}: ray {t_ray:.9f}  quadrature {t_q:.9f}  series(6) {ser:.9f}")
lo, _ = ray_turn(n, dn, 2 * math.e * (1 - 1e-3), r_stop=1.0)
hi, _ = ray_turn(n, dn, 2 * math.e * (1 + 1e-3), r_stop=1.0)
print(f"    b = 2e(1 - 1e-3): {'captured' if lo is None else 'escapes'};  b = 2e(1 + 1e-3): {'captured' if hi is None else 'escapes'}")
