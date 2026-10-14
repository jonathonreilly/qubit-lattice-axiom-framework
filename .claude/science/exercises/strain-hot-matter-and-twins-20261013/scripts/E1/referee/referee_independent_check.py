#!/usr/bin/env python3
"""Small independent checks for C5/E1.

All arrays are O(N^2) or smaller.  This deliberately uses routes different
from the worker where practical: a dense, explicitly enumerated transfer
matrix; analytic integration over one phi^4 momentum; direct honeycomb BZ
sums; and the closed elliptic-integral form of the large-N O(N) saddle.
"""

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar
from scipy.special import ellipk


K_C = 0.5 * np.arcsinh(1.0)


def dual(k):
    return np.arctanh(np.exp(-2.0 * k))


def eps(q, kx, ky):
    kys = dual(ky)
    c = (np.cosh(2 * kys) * np.cosh(2 * kx)
         - np.sinh(2 * kys) * np.sinh(2 * kx) * np.cos(q))
    return np.arccosh(c)


def ff_vacua(width, kx, ky):
    pref = 0.5 * width * np.log(2 * np.sinh(2 * ky))
    q_ns = (2 * np.arange(width) + 1) * np.pi / width
    q_r = 2 * np.arange(width) * np.pi / width
    e_r = eps(q_r, kx, ky)
    e_r[0] = 2 * (kx - dual(ky))
    return sorted((pref + 0.5 * eps(q_ns, kx, ky).sum(),
                   pref + 0.5 * e_r.sum()), reverse=True)


def dense_tm(width, kx, ky):
    """Explicit 2^L by 2^L row transfer matrix, only used at L=8."""
    states = ((np.arange(1 << width)[:, None] >> np.arange(width)) & 1) * 2 - 1
    bonds = np.sum(states * np.roll(states, -1, axis=1), axis=1)
    vertical = states @ states.T
    tm = np.exp(0.5 * kx * (bonds[:, None] + bonds[None, :]) + ky * vertical)
    return np.linalg.eigvalsh(tm)[-2:][::-1]


def axis_xis(kx, ky):
    return (1 / (2 * (dual(kx) - ky)),
            1 / (2 * (dual(ky) - kx)))


def support_leak(kx, ky):
    """45-degree support-function leak after exact axis-xi rescaling."""
    sx, sy = np.sinh(2 * kx), np.sinh(2 * ky)
    c = np.cosh(2 * kx) * np.cosh(2 * ky)
    xmax = np.arccosh((c - sy) / sx)
    xix, xiy = axis_xis(kx, ky)

    def minus_support(kappa_x):
        arg = np.clip((c - sx * np.cosh(kappa_x)) / sy, 1.0, None)
        kappa_y = np.arccosh(arg)
        return -(kappa_x * xix + kappa_y * xiy) / np.sqrt(2)

    h45 = -minimize_scalar(minus_support, bounds=(-xmax, xmax),
                           method="bounded", options={"xatol": 1e-14}).fun
    return h45 - 1.0, xix, xiy


def phi4_reduced(n):
    """Gauss integration in qx,qy; qz is integrated analytically."""
    x, w = leggauss(n)
    q = np.pi * x
    w = 0.5 * w  # normalized BZ measure dq/(2 pi)
    e = 2 * (1 - np.cos(q))
    qval = 0.0
    i0 = 0.0
    for i in range(n):
        a = e[i] + e + 2.0
        d = a * a - 4.0
        iz1 = 1 / np.sqrt(d)
        iz3 = (2 * a * a + 4) / (2 * d ** 2.5)
        i0 += w[i] * np.sum(w * iz1)
        qval += w[i] * np.sum(w * (e[i] - e) ** 2 * iz3)
    return qval, i0


def continuum_block_coefficient(n):
    """Coefficient C in Q(|q_j|<pi/b) -> C/b, continuum cube."""
    x, w = leggauss(n)
    limit = np.pi
    q = limit * x
    total = 0.0
    for i in range(n):
        a2 = q[i] ** 2 + q ** 2
        iz3 = (limit / (2 * a2 * (a2 + limit**2) ** 2)
               + 3 * limit / (4 * a2**2 * (a2 + limit**2))
               + 3 * np.arctan(limit / np.sqrt(a2)) / (4 * a2**2.5))
        total += w[i] * np.sum(w * (q[i] ** 2 - q ** 2) ** 2 * iz3)
    return total * limit**2 / (2 * np.pi) ** 3


def graphene_inv_uc(n):
    """Direct midpoint sum, independent of the worker's elliptic reduction."""
    theta = (np.arange(n) + 0.5) * 2 * np.pi / n
    z = np.exp(-1j * theta)
    total = 0.0
    for z1 in z:
        total += np.sum(0.5 / np.abs(1 + z1 + z))
    return total / n**2


def logz(kx, ky):
    val = quad(lambda q: eps(q, kx, ky), -np.pi, np.pi,
               epsabs=2e-12, epsrel=2e-12, limit=800)[0] / (2 * np.pi)
    return 0.5 * np.log(2 * np.sinh(2 * ky)) + 0.5 * val


def on_g(mass, jx, jy):
    """Closed anisotropic square-lattice Green function at N=infinity."""
    a = mass * mass + 2 * jx + 2 * jy
    d = a * a - 4 * (jx - jy) ** 2
    return 2 * ellipk(16 * jx * jy / d) / (np.pi * np.sqrt(d))


def on_response(xi, t=0.005):
    m0 = 1 / xi
    target = on_g(m0, 1.0, 1.0)

    def solve(jx, jy):
        return np.exp(brentq(lambda lm: on_g(np.exp(lm), jx, jy) - target,
                             np.log(m0) - 3, np.log(m0) + 3))

    ml = solve(1 + t, 1 - t)
    mv = solve(np.exp(t), np.exp(-t))
    return np.log(ml / m0) / t**2, np.log(mv / m0) / t**2


def main():
    print("[1] Ising exact constants and independent dense transfer matrix")
    ising_gap_coefficient = 2 * np.sqrt(2) * K_C**2
    assert abs(ising_gap_coefficient - 0.549294265424) < 2e-12
    print(f"Kc={K_C:.15f}  2sqrt(2)Kc^2={ising_gap_coefficient:.12f}")
    for kx, ky in ((0.30, 0.25), (0.50, 0.42)):
        vals = dense_tm(8, kx, ky)
        exact = ff_vacua(8, kx, ky)
        assert abs(np.log(vals[0])-exact[0]) < 1e-12
        assert abs(np.log(vals[0]/vals[1])-(exact[0]-exact[1])) < 1e-12
        print(f"L=8 K=({kx:.2f},{ky:.2f}) top-log error="
              f"{abs(np.log(vals[0])-exact[0]):.3e} gap error="
              f"{abs(np.log(vals[0]/vals[1])-(exact[0]-exact[1])):.3e}")

    print("[2] Ising correlation-length/metric leak")
    ratio = (1 + 0.1) / (1 - 0.1)
    kcrit = brentq(lambda ky: np.sinh(2 * ratio * ky) * np.sinh(2 * ky) - 1,
                   0.1, K_C)
    ky = brentq(lambda k: np.sqrt(np.prod(axis_xis(ratio*k, k))) - 100,
                0.1, 0.999999*kcrit)
    leak, xix, xiy = support_leak(ratio * ky, ky)
    assert 0.0208 < leak*xix*xiy < 0.0212
    print(f"xi=({xix:.6f},{xiy:.6f}) h45/haxis-1={leak:.9e} "
          f"coefficient={leak*xix*xiy:.6f}")

    print("[3] phi4 one-loop coefficient by analytic qz integration")
    p200 = phi4_reduced(200)
    p400 = phi4_reduced(400)
    p800 = phi4_reduced(800)
    qext = 2 * p800[0] - p400[0]
    iext = 2 * p800[1] - p400[1]
    c400 = continuum_block_coefficient(400)
    c800 = continuum_block_coefficient(800)
    cext = 2 * c800 - c400
    assert abs(qext - 0.05428576) < 2e-7
    assert abs(iext - 0.25273070) < 2e-7
    assert abs(cext/qext - 0.88279) < 2e-4
    print(f"Q N=200,400,800: {p200[0]:.9f} {p400[0]:.9f} {p800[0]:.9f}")
    print(f"linear extrapolation Q={qext:.8f} I0={iext:.8f}")
    print(f"continuum block C={cext:.8f}; share coefficient C/Q={cext/qext:.5f}")

    print("[4] graphene/Hubbard")
    i2048 = graphene_inv_uc(2048)
    i4096 = graphene_inv_uc(4096)
    iex = 2 * i4096 - i2048
    assert abs(1/iex - 2.231045) < 2e-5
    print(f"direct BZ extrapolation 1/Uc={iex:.8f} Uc={1/iex:.6f}")
    for u in (0.249, 0.26):
        hops = np.array((1 + 2*u, 1 - u, 1 - u))
        gap = 2 * max(0.0, 2*hops.max() - hops.sum())
        print(f"u={u:.3f} triangle gap={gap:.6f}")

    print("[5] Ising free-energy curvature")
    for h in (0.02, 0.01, 0.005):
        d2logz = (logz(K_C*(1+h), K_C*(1-h))
                  + logz(K_C*(1-h), K_C*(1+h)) - 2*logz(K_C, K_C)) / h**2
        assert d2logz > 0
        print(f"h={h:.3f} d2logZ={d2logz:.8f} d2(beta*f)={-d2logz:.8f}")

    print("[6] large-N O(N) response and composite arithmetic")
    for xi in (10.0, 100.0, 1e4):
        lin, vol = on_response(xi)
        assert lin > 0 and abs(vol + 0.25) < 3e-4
        print(f"xi={xi:.0f} dlnm/t2 linear={lin:.6f} volume-preserving={vol:.6f}")
    mpl = 1.22089e19
    strong = 1.0e4
    clock_limit = 1.4e-21
    f6 = 3.68102e-3
    naive = f6 * (strong / mpl) ** 2
    xi_phys = mpl / strong
    kappa = 0.5 * np.log(xi_phys) + 0.35
    on_scaled = 2 * kappa * (strong / mpl) ** 2
    print(f"naive F6 coefficient replacement={naive:.3e}, margin={clock_limit/naive:.3e}")
    print(f"O(N)-linear extrapolation 2*kappa={2*kappa:.3f}, coefficient={on_scaled:.3e}, "
          f"margin={clock_limit/on_scaled:.3e}")


if __name__ == "__main__":
    main()
