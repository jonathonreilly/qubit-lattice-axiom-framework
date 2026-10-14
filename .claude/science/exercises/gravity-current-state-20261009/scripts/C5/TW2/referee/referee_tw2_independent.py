"""Independent TW-2 numerical checks.

This intentionally does not import the worker's tw2_conv.py or f3_lib.py.
It reimplements the stated one-loop P=0 Psym formula on a separately built
composite Gauss-Legendre grid, with a chunked z loop to keep RSS small.
"""

from __future__ import annotations

import math
import os
import sys
from dataclasses import dataclass

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "flat"))
from sublum import SymG, SymS  # noqa: E402


BF = 0.909103708
CPH = 2.9435
SLAW = SymS(BF)
GLAW = SymG(CPH)
TET = np.array((-1.0, -1.0, 2.0)) / math.sqrt(3.0)
EG = np.array((1.0, -1.0, 0.0))


@dataclass
class Grid:
    x: np.ndarray
    w: np.ndarray


def independent_grid(order: int, hmax: float = 0.30) -> Grid:
    """Composite GL grid on [0,pi], independently assembled for this audit."""
    anchors = [
        0.0,
        0.00125,
        0.0025,
        0.005,
        0.01,
        0.02,
        0.04,
        0.08,
        0.16,
        0.32,
        BF,
        math.pi - BF,
        CPH,
        math.pi,
    ]
    edges = [anchors[0]]
    for left, right in zip(anchors[:-1], anchors[1:]):
        count = max(1, math.ceil((right - left) / hmax))
        edges.extend(left + (right - left) * j / count for j in range(1, count + 1))
    q, qw = np.polynomial.legendre.leggauss(order)
    nodes, weights = [], []
    for left, right in zip(edges[:-1], edges[1:]):
        nodes.append((right - left) * q / 2 + (right + left) / 2)
        weights.append((right - left) * qw / (2 * math.pi))
    return Grid(np.concatenate(nodes), np.concatenate(weights))


def rk4_flow(k: np.ndarray, rate: float, photon: bool, steps: int = 7) -> np.ndarray:
    """Time-one flow for dy/du = rate*p(y)/2."""
    if rate == 0.0:
        return np.asarray(k, dtype=float)

    def velocity(y: np.ndarray) -> np.ndarray:
        if photon:
            return 0.5 * rate * GLAW.h(y) * GLAW.dh(y)
        return 0.5 * rate * SLAW.s(y) * SLAW.ds(y)

    y = np.asarray(k, dtype=float)
    du = 1.0 / steps
    for _ in range(steps):
        k1 = velocity(y)
        k2 = velocity(y + 0.5 * du * k1)
        k3 = velocity(y + 0.5 * du * k2)
        k4 = velocity(y + du * k3)
        y = y + du * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return y


def mass_value(flowed: tuple[np.ndarray, np.ndarray, np.ndarray], amp: float, symbol: str) -> np.ndarray:
    fx, fy, fz = flowed
    if symbol == "one":
        return amp + 0 * fx + 0 * fy + 0 * fz
    if symbol == "c1c2":
        return amp * np.cos(fx) * np.cos(fy) + 0 * fz
    if symbol == "c1c2_c2k3":
        return amp * np.cos(fx) * np.cos(fy) * np.cos(2 * fz)
    raise ValueError(symbol)


def one_loop_mass(grid: Grid, t: float, strain: np.ndarray, amp: float, symbol: str) -> float:
    """Direct Psym one-loop additive mass in the conventions stated in TW2."""
    x, w = grid.x, grid.w
    n = len(x)
    flowed_nodes = [rk4_flow(x, t * strain[j], photon=False) for j in range(3)]
    photon_d = [GLAW.h(rk4_flow(x, t * strain[j], photon=True)) for j in range(3)]
    xp = np.concatenate(([0.0], x))

    def c_and_m(kx, ky, kz):
        # Inputs are always zero or quadrature nodes, so interpolation is exact
        # at every nonzero argument used below.
        def lookup(j, k):
            table = np.concatenate(([0.0], flowed_nodes[j]))
            return np.sign(k) * np.interp(np.abs(k), xp, table)

        fx, fy, fz = lookup(0, kx), lookup(1, ky), lookup(2, kz)
        return (SLAW.s(fx), SLAW.s(fy), SLAW.s(fz), mass_value((fx, fy, fz), amp, symbol))

    zero = np.zeros(1)
    d0 = tuple(np.asarray(v).reshape(-1)[0] for v in c_and_m(zero, zero, zero))
    ax = c_and_m(x, 0 * x, 0 * x)
    ay = c_and_m(0 * x, x, 0 * x)
    az = c_and_m(0 * x, 0 * x, x)
    mxm = c_and_m(-x, 0 * x, 0 * x)[3]
    mym = c_and_m(0 * x, -x, 0 * x)[3]
    mzm = c_and_m(0 * x, 0 * x, -x)[3]
    pxy = c_and_m(x[:, None], x[None, :], 0 * x[:, None])
    tx = ((ax[3] + mxm) / 2 - d0[3]) / photon_d[0] ** 2
    ty = ((ay[3] + mym) / 2 - d0[3]) / photon_d[1] ** 2
    tz = ((az[3] + mzm) / 2 - d0[3]) / photon_d[2] ** 2

    tadpole = 0.0
    rainbow = 0.0
    chunk = max(1, min(6, 50000 // (n * n)))
    for first in range(0, n, chunk):
        iz = np.arange(first, min(n, first + chunk))
        qx = x[:, None, None]
        qy = x[None, :, None]
        qz = x[iz][None, None, :]
        cq = c_and_m(qx, qy, qz)
        cxz = c_and_m(qx, 0 * qy, qz)
        cyz = c_and_m(0 * qx, qy, qz)
        cx = tuple(v[:, None, None] for v in ax)
        cy = tuple(v[None, :, None] for v in ay)
        cz = tuple(v[iz][None, None, :] for v in az)
        cxy = tuple(v[:, :, None] for v in pxy)
        c0 = tuple(v + 0 * qx + 0 * qy + 0 * qz for v in d0)
        dx = photon_d[0][:, None, None]
        dy = photon_d[1][None, :, None]
        dz = photon_d[2][iz][None, None, :]

        vx = tuple((2 * (cx[a] - c0[a]) + (cxy[a] - cy[a]) + (cxz[a] - cz[a]) + 2 * (cq[a] - cyz[a])) / (6 * dx) for a in range(4))
        vy = tuple((2 * (cy[a] - c0[a]) + (cxy[a] - cx[a]) + (cyz[a] - cz[a]) + 2 * (cq[a] - cxz[a])) / (6 * dy) for a in range(4))
        vz = tuple((2 * (cz[a] - c0[a]) + (cxz[a] - cx[a]) + (cyz[a] - cy[a]) + 2 * (cq[a] - cxy[a])) / (6 * dz) for a in range(4))
        omega = np.sqrt(dx * dx + dy * dy + dz * dz)
        mass = cq[3]
        energy = np.sqrt(cq[0] ** 2 + cq[1] ** 2 + cq[2] ** 2 + mass * mass)
        numerator = mass.copy()
        for vertex in (vx, vy, vz):
            adotc = vertex[0] * cq[0] + vertex[1] * cq[1] + vertex[2] * cq[2]
            numerator += (vertex[0] ** 2 + vertex[1] ** 2 + vertex[2] ** 2 - vertex[3] ** 2) * mass - 2 * vertex[3] * adotc
        weight = w[:, None, None] * w[None, :, None] * w[iz][None, None, :]
        seagull = tx[:, None, None] + ty[None, :, None] + tz[iz][None, None, :]
        tadpole += float(np.sum(weight * seagull / (2 * omega)))
        rainbow += float(np.sum(weight * numerator / (2 * energy * omega * (energy + omega))))
    return tadpole + rainbow


def response(grid: Grid, strain: np.ndarray, amp: float, symbol: str, step: float = 0.003) -> tuple[float, float, float]:
    values = {q: one_loop_mass(grid, q * step, strain, amp, symbol) / amp for q in (0, 1, -1, 2, -2)}
    grad1 = (values[1] - values[-1]) / (2 * step)
    grad2 = (values[2] - values[-2]) / (4 * step)
    hess1 = (values[1] - 2 * values[0] + values[-1]) / step**2
    hess2 = (values[2] - 2 * values[0] + values[-2]) / (2 * step) ** 2
    return values[0], (4 * grad1 - grad2) / 3, (4 * hess1 - hess2) / 3


def size_cross_check(linear_leak: float, hess_eg: float, singlet_hess: float, long_linear_leak: float) -> None:
    me, mmu, mp = 0.000511, 0.10566, 0.9383
    planck = 1.22089e19
    sigma_e = (mmu - me) / 2
    # Nucleon scalar inputs copied as explicit comparator assumptions, not code.
    mu, md, ms, mc, mb, mt = 0.00216, 0.00467, 0.0934, 1.27, 4.18, 172.69
    spi, strange = 0.045, 0.040

    def heavy(mass):
        return (2 / 27) * (mp - spi - strange) / mass

    sigma_pairs = ((mu, mc, 6.6, heavy(mc)), (md, ms, 6.6, strange / ms), (mt, 1500.0, heavy(mt), heavy(1500.0)), (mb, 1500.0, heavy(mb), heavy(1500.0)))
    wn = sum((hi - lo) * (nlo - nhi) / 2 for lo, hi, nlo, nhi in sigma_pairs)
    dln_e = 0.1 * linear_leak * sigma_e / me
    dln_p = 0.4 * linear_leak * wn / mp
    coeff = abs(dln_p - dln_e) / math.sqrt(2)
    slope_range = (1.502e-15, 5.702e-15)
    ratios = tuple(coeff * slope / 3.6e-17 for slope in slope_range)
    hess_ref, mu_ref = 2.42401e-2, 2.424e-21
    mu_rho = (wn / planck) * abs(hess_eg) / (13 * hess_ref) * mu_ref
    dln_e_h = 0.5 * 0.1 * hess_eg * sigma_e / me + 0.5 * 0.1 * singlet_hess
    dln_p_h = 0.5 * 0.4 * hess_eg * wn / mp
    hess_ratios = tuple(abs(dln_p_h - dln_e_h) * rate / 3.6e-17 for rate in (7.670e-30, 1.023e-28))
    electron_only = abs(dln_e) / math.sqrt(2) * slope_range[0] / 3.6e-17
    proton_only = abs(dln_p) / math.sqrt(2) * slope_range[0] / 3.6e-17
    print(f"sizes sigma_e/Mp={sigma_e / planck:.6e} W_N={wn:.6f} GeV")
    print(f"sizes hessian mu_rho={mu_rho:.6e} Earth_ratio={mu_rho / 1.5e-29:.6e} clock_ratios={hess_ratios[0]:.6e},{hess_ratios[1]:.6e}")
    print(f"sizes dln_e/dt={dln_e:+.6f} dln_p/dt={dln_p:+.6f} net={dln_p-dln_e:+.6f}")
    print(f"sizes clock ratios for supplied slope endpoints={ratios[0]:.3f},{ratios[1]:.3f}")
    print(f"sizes component ratios at conservative slope: electron={electron_only:.3f} proton={proton_only:.3f}")
    print(f"sizes long-symbol clock ratios={ratios[0]*long_linear_leak/linear_leak:.3f},{ratios[1]*long_linear_leak/linear_leak:.3f}")


def main() -> None:
    amp = 0.005
    final = None
    final_hess_eg = final_singlet_hess = final_long = None
    orders = tuple(int(value) for value in sys.argv[1:]) or (4, 5, 6)
    for order in orders:
        grid = independent_grid(order)
        a0, ap, app = response(grid, TET, amp, "one")
        b0, bp, bpp = response(grid, TET, amp, "c1c2")
        _, bp_long, bpp_long = response(grid, TET, amp, "c1c2_c2k3")
        _, _, bpp_eg = response(grid, EG, amp, "c1c2")
        final = ap - bp
        final_hess_eg = app - bpp_eg
        final_singlet_hess = app
        final_long = ap - bp_long
        print(
            f"order={order} nodes={len(grid.x)} sumw={grid.w.sum():.16f} "
            f"A'={ap:+.9e} B'={bp:+.9e} leak'={ap-bp:+.9e} "
            f"A''={app:+.9e} B''tet={bpp:+.9e} leak''tet={app-bpp:+.9e} "
            f"B''Eg={bpp_eg:+.9e} leak''Eg={app-bpp_eg:+.9e} "
            f"B'long={bp_long:+.9e} leak'long={ap-bp_long:+.9e} "
            f"B''long={bpp_long:+.9e} leak''long={app-bpp_long:+.9e}"
        )
    assert final is not None and final_hess_eg is not None and final_singlet_hess is not None and final_long is not None
    size_cross_check(final, final_hess_eg, final_singlet_hess, final_long)


if __name__ == "__main__":
    main()
