"""Independent analytic-response check for C5/F3.

This script does not import the worker's f3_lib.py.  It differentiates the
unstrained one-loop Psym mass integrand analytically at epsilon=0 for

    delta c = 2 f M,       delta M = -2 f.c,

which is the first variation of H -> exp(i epsilon G_f) H exp(-i epsilon
G_f).  The corner differences, vertices, diagonal seagull, numerator, and
quadrature are reconstructed here.  Three-dimensional arrays are z-slabbed.
"""

from __future__ import annotations

import gc
import os
import sys

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "arch"))
from dirac import D1
from sublum import SymG


ROOT = (0.909103708, 0.555604226)
CPH = 2.9435


def composite_gauss(breaks, order=6, hmax=0.25):
    """Normalized Gauss-Legendre rule on [0, pi], split at symbol edges."""
    points = {0.0, np.pi, 0.0025, 0.005, 0.01, 0.02, 0.04, 0.08, 0.16, 0.32}
    points.update(float(x) for x in breaks if 0.0 < x < np.pi)
    coarse = sorted(points)
    fine = [coarse[0]]
    for left, right in zip(coarse[:-1], coarse[1:]):
        count = max(1, int(np.ceil((right - left) / hmax)))
        fine.extend(left + (right - left) * j / count for j in range(1, count + 1))
    gx, gw = np.polynomial.legendre.leggauss(order)
    nodes, weights = [], []
    for left, right in zip(fine[:-1], fine[1:]):
        nodes.append(0.5 * (right - left) * gx + 0.5 * (right + left))
        weights.append(0.5 * (right - left) * gw / np.pi)
    return np.concatenate(nodes), np.concatenate(weights)


def generator_vector(name, kx, ky, kz):
    sx, sy, sz = np.sin(kx), np.sin(ky), np.sin(kz)
    if name == "G1":
        return sx + 0 * ky + 0 * kz, sy + 0 * kx + 0 * kz, sz + 0 * kx + 0 * ky
    if name == "G2":
        cx, cy, cz = np.cos(kx), np.cos(ky), np.cos(kz)
        return sx * (cy + cz), sy * (cz + cx), sz * (cx + cy)
    raise ValueError(name)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(a, factor):
    return tuple(factor * x for x in a)


def response(name, order=6, hmax=0.25, photon_panels=6, chunk=4):
    fermion = D1(*ROOT)
    photon = SymG(CPH)
    photon_edges = [CPH + j * (np.pi - CPH) / photon_panels for j in range(photon_panels)]
    x, w = composite_gauss([ROOT[0], np.pi - ROOT[0], *photon_edges], order, hmax)
    n = len(x)

    s = fermion.S(x)
    mass1 = fermion.W(x)
    d = photon.h(x)

    def variation(kx, ky, kz):
        """Return (delta c_x, delta c_y, delta c_z, delta M)."""
        kx = kx + 0 * ky + 0 * kz
        ky = ky + 0 * kx + 0 * kz
        kz = kz + 0 * kx + 0 * ky
        c = (fermion.S(kx), fermion.S(ky), fermion.S(kz))
        mass = fermion.W(kx) + fermion.W(ky) + fermion.W(kz)
        f = generator_vector(name, kx, ky, kz)
        dc = tuple(2 * fj * mass for fj in f)
        dm = -2 * sum(fj * cj for fj, cj in zip(f, c))
        return (*dc, dm)

    zero = np.zeros(1)
    v0 = tuple(float(np.ravel(v)[0]) for v in variation(zero, zero, zero))
    vx = variation(x, 0 * x, 0 * x)
    vy = variation(0 * x, x, 0 * x)
    vz = variation(0 * x, 0 * x, x)
    vxy = variation(x[:, None], x[None, :], 0 * x[:, None])

    # The diagonal seagull uses the average of +/- axis points.  Compute the
    # negative side explicitly so parity is not assumed by the checker.
    vx_minus = variation(-x, 0 * x, 0 * x)
    vy_minus = variation(0 * x, -x, 0 * x)
    vz_minus = variation(0 * x, 0 * x, -x)
    dt_x = (0.5 * (vx[3] + vx_minus[3]) - v0[3]) / d**2
    dt_y = (0.5 * (vy[3] + vy_minus[3]) - v0[3]) / d**2
    dt_z = (0.5 * (vz[3] + vz_minus[3]) - v0[3]) / d**2

    tadpole = 0.0
    exchange = 0.0
    max_energy_variation = 0.0
    for start in range(0, n, chunk):
        iz = np.arange(start, min(n, start + chunk))
        X = x[:, None, None]
        Y = x[None, :, None]
        Z = x[iz][None, None, :]

        vq = variation(X, Y, Z)
        vxz = variation(X, 0 * Y, Z)
        vyz = variation(0 * X, Y, Z)

        cx = s[:, None, None]
        cy = s[None, :, None]
        cz = s[iz][None, None, :]
        mass = mass1[:, None, None] + mass1[None, :, None] + mass1[iz][None, None, :]
        energy = np.sqrt(cx**2 + cy**2 + cz**2 + mass**2)

        # Pointwise spectrum invariance is an independent factor/sign check.
        denergy_num = cx * vq[0] + cy * vq[1] + cz * vq[2] + mass * vq[3]
        max_energy_variation = max(max_energy_variation, float(np.max(np.abs(denergy_num))))

        # Linearized Psym vertices from the eight cube corners.  Expand each
        # lower-dimensional corner on its actual coordinate axes explicitly.
        c0 = tuple(np.asarray(v) for v in v0)
        vxe = tuple(v[:, None, None] for v in vx)
        vye = tuple(v[None, :, None] for v in vy)
        vze = tuple(v[iz][None, None, :] for v in vz)
        vxye = tuple(v[:, :, None] for v in vxy)
        dvx = scale(
            add(add(scale(sub(vxe, c0), 2), sub(vxye, vye)), add(sub(vxz, vze), scale(sub(vq, vyz), 2))),
            1.0 / (6 * d[:, None, None]),
        )
        dvy = scale(
            add(add(scale(sub(vye, c0), 2), sub(vxye, vxe)), add(sub(vyz, vze), scale(sub(vq, vxz), 2))),
            1.0 / (6 * d[None, :, None]),
        )
        dvz = scale(
            add(add(scale(sub(vze, c0), 2), sub(vxz, vxe)), add(sub(vyz, vye), scale(sub(vq, vxye), 2))),
            1.0 / (6 * d[iz][None, None, :]),
        )

        omega = np.sqrt(d[:, None, None] ** 2 + d[None, :, None] ** 2 + d[iz][None, None, :] ** 2)
        dnumerator = vq[3].copy()
        c = (cx, cy, cz)
        dc = vq[:3]
        for axis, dv in enumerate((dvx, dvy, dvz)):
            aj = (s / d)[(slice(None), None, None) if axis == 0 else
                         (None, slice(None), None) if axis == 1 else
                         (None, None, iz)]
            bj = (mass1 / d)[(slice(None), None, None) if axis == 0 else
                             (None, slice(None), None) if axis == 1 else
                             (None, None, iz)]
            a_dot_da = aj * dv[axis]
            a_dot_c = aj * c[axis]
            da_dot_c = sum(dv[j] * c[j] for j in range(3))
            a_dot_dc = aj * dc[axis]
            db = dv[3]
            dnumerator += (
                (2 * a_dot_da - 2 * bj * db) * mass
                + (aj**2 - bj**2) * vq[3]
                - 2 * db * a_dot_c
                - 2 * bj * (da_dot_c + a_dot_dc)
            )

        weights = w[:, None, None] * w[None, :, None] * w[iz][None, None, :]
        dtad = dt_x[:, None, None] + dt_y[None, :, None] + dt_z[iz][None, None, :]
        tadpole += float(np.sum(weights * dtad / (2 * omega)))
        exchange += float(np.sum(weights * dnumerator / (2 * energy * omega * (energy + omega))))

    return {
        "nodes": n,
        "tadpole": tadpole,
        "exchange": exchange,
        "total": tadpole + exchange,
        "max_dE_numerator": max_energy_variation,
    }


def main():
    hessian_f1 = 2.4240112e-2
    for name in ("G1", "G2"):
        result = response(name)
        astar = -hessian_f1 / (2 * result["total"])
        print(
            f"{name} nodes={result['nodes']} "
            f"L_tad={result['tadpole']:+.12e} "
            f"L_exchange={result['exchange']:+.12e} "
            f"L_total={result['total']:+.12e} "
            f"a_star={astar:+.12e} "
            f"max|c.dc+M.dM|={result['max_dE_numerator']:.3e}",
            flush=True,
        )
        del result
        gc.collect()


if __name__ == "__main__":
    main()
