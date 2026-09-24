#!/usr/bin/env python3
"""Referee for a-clause-for-lengths a2.

Author w-macbookpro90c72-j2d91 (claude-opus-5-5). Own Hamilton algebra and a 1D matrix check.
The 112x96 packet evolution is not re-run; the printed fit is.
"""
import numpy as np
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def hamilton():
    """At a fixed point with ab = 1, the family's acceleration matches the stated weak-field law."""
    ax, bx = sp.symbols("alpha beta")
    # basis: grad u, |v|^2 grad u, (v·grad u) v.
    # family coefficients -alpha, -beta, 2(alpha+beta); comparator -1, -1, 4.
    match = sp.solve([ax - 1, bx - 1, 2 * (ax + bx) - 4], [ax, bx], dict=True)
    ok_unique = match == [{ax: 1, bx: 1}]
    # concrete ray: a=exp(alpha*u), b=exp(beta*u), u=g*x, at x=0 so a=b=1
    x, g = sp.symbols("x g")
    alpha, beta, m, k = sp.symbols("alpha beta m k", real=True)
    u = g * x
    a = sp.exp(alpha * u)
    b = sp.exp(beta * u)
    Gam = sp.sqrt(m**2 + b**2 * k**2)
    v = a * b**2 * k / Gam
    # kdot = -dE/dx, E=a*Gam
    E = a * Gam
    kdot = -sp.diff(E, x)
    # dv/dt = dv/dx * v + dv/dk * kdot, with x and k independent before substituting the ray
    v_of = v
    accel = sp.diff(v_of, x) * v_of + sp.diff(v_of, k) * kdot
    accel0 = sp.simplify(accel.subs(x, 0))
    # stated: -alpha*g - beta*v^2*g + 2(alpha+beta)*v*(g)*v, and v(0)= b^2 k/Gam at a=1,b=1 = k/sqrt(m^2+k^2) *1
    v0 = sp.simplify(v.subs(x, 0))
    stated = -alpha * g - beta * v0**2 * g + 2 * (alpha + beta) * v0 * g * v0
    ok_acc = sp.simplify(accel0 - stated) == 0
    report(
        "hamilton",
        bool(ok_unique and ok_acc),
        "weak-field law is -alpha grad u - beta |v|^2 grad u + 2(alpha+beta)(v·grad u)v, "
        "equal to the comparator for every v only at alpha=beta=1",
    )


def power_mean():
    d, p = sp.symbols("d p")
    series = sp.series(sp.cosh(p * d / 2) ** (1 / p), d, 0, 4).removeO()
    target = 1 + p * d**2 / 8
    ok = sp.simplify(series - target) == 0
    report(
        "power mean",
        bool(ok),
        "M_p = sqrt(w_x w_y) (1 + p d^2/8 + O(d^4)), degree one, so it does not change first-order bending",
    )


def staggered():
    """On a 4-site ring, epsilon anticommutes with the hop and the square is a^2 m^2 + c^2 hop^2."""
    n = 4
    eps = np.diag([1, -1, 1, -1])
    hop = np.zeros((n, n))
    for i in range(n):
        hop[i, (i + 1) % n] = 0.5
        hop[i, (i - 1) % n] = -0.5
    anti = eps @ hop + hop @ eps
    a, c, m = 3, 5, 2
    H = a * m * eps + c * hop
    left = H @ H
    right = (a * m) ** 2 * np.eye(n) + c**2 * (hop @ hop)
    ok = np.max(np.abs(anti)) == 0 and np.max(np.abs(left - right)) < 1e-12
    report(
        "staggered rest energy",
        ok,
        "on a 4-ring, epsilon anticommutes with the hop and (a m epsilon + c hop)^2 = a^2 m^2 + c^2 hop^2",
    )


def fit():
    h = np.array([0.0, 0.390, 0.663, 0.735])
    b0 = np.array([0.9949, 0.9842, 0.9859, 0.9850])
    b1 = np.array([1.0011, 1.3690, 1.6216, 1.6816])
    slope0, icept0 = np.polyfit(h, b0, 1)
    slope1, icept1 = np.polyfit(h, b1, 1)
    ok = (
        abs(icept0 - 0.993) < 0.002
        and abs(slope0 - (-0.013)) < 0.003
        and abs(icept1 - 1.003) < 0.002
        and abs(slope1 - 0.929) < 0.003
    )
    report(
        "printed fit",
        ok,
        f"beta=0 intercept {icept0:.3f} slope {slope0:.3f}; beta=1 intercept {icept1:.3f} slope {slope1:.3f}",
    )


def gradient_factor():
    """dv_x/dt = -g (m^2 + (1+beta) S) / E^2 = -g (1 + beta h) when a=w, c=w^{1+beta}, w=1."""
    m2, S, beta, g = sp.symbols("m2 S beta g", positive=True)
    E2 = m2 + S  # a=1, c=1 at the point, E^2 = m^2 + S
    h = S / E2
    accel = -g * (m2 + (1 + beta) * S) / E2
    stated = -g * (1 + beta * h)
    report(
        "hop share",
        sp.simplify(accel - stated) == 0,
        "across a gradient the bend is -g(1 + beta h), h = S/E^2",
    )


def main():
    hamilton()
    power_mean()
    staggered()
    gradient_factor()
    fit()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the family's weak-field law equals the comparator at every speed "
        "iff alpha = beta = 1. A power mean of the endpoint rates is 1 + O((Delta u)^2) and does not "
        "supply the factor. One walker with a staggered rest energy reads beta as the slope of bending against hop share."
    )
    print(
        "SUMMARY: confirmed the Hamilton reduction, the unique match alpha=beta=1, the power-mean series, "
        "the staggered square on a 4-ring, and the fit to the printed 2D table "
        "(intercepts 0.993 and 1.003, slopes -0.013 and 0.929). The 112x96 evolution was not re-run."
    )


if __name__ == "__main__":
    main()
