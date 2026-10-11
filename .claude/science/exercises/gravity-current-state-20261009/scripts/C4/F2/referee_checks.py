"""Independent checks for C4/RF/F2.

This does not import any f2_* module.  The fermion momentum derivative is
analytic (rather than the worker's finite difference), while the photon
magnetic coefficient is obtained from a multi-point polynomial intercept
(rather than the worker's two-point Richardson step).
"""

import itertools
import numpy as np


U = 16.0 * np.pi**2


def proper_cubic_rotations():
    out = []
    for p in itertools.permutations(range(3)):
        P = np.zeros((3, 3))
        P[np.arange(3), p] = 1.0
        for signs in itertools.product((-1.0, 1.0), repeat=3):
            R = np.diag(signs) @ P
            if round(np.linalg.det(R)) == 1:
                out.append(R)
    return out


def invariant_matrix_dimension(rotations):
    rows = []
    for R in rotations:
        rows.append(np.kron(R, R) - np.eye(9))
    s = np.linalg.svd(np.vstack(rows), compute_uv=False)
    return int(np.sum(s < 1e-10)), s


def slabs(L):
    k = (np.arange(L) + 0.5) * 2.0 * np.pi / L - np.pi
    ky, kz = np.meshgrid(k, k, indexing="ij")
    return k, ky, kz


def fermion_analytic_derivative(L, m, lam):
    """Continuous-time Z^3 result, with d/dp_x evaluated analytically."""
    k, ky, kz = slabs(L)
    syz2 = np.sin(ky) ** 2 + np.sin(kz) ** 2
    cyz = np.cos(ky / 2.0) ** 2 + np.cos(kz / 2.0) ** 2
    khyz = 4.0 * (np.sin(ky / 2.0) ** 2 + np.sin(kz / 2.0) ** 2)
    a0 = a2 = derivative = 0.0
    for x in k:
        sx, cx = np.sin(x), np.cos(x)
        E = np.sqrt(sx * sx + syz2 + m * m)
        w = np.sqrt(4.0 * np.sin(x / 2.0) ** 2 + khyz + lam * lam)
        c0 = np.cos(x / 2.0) ** 2 + cyz
        a0 += np.sum(-(1.0 - c0) / (2.0 * w * (E + w) ** 2))
        a2 += np.sum(1.0 / (2.0 * w))

        # I(p) numerator is sin(p-x)[cos^2(p-x/2)-1-c_yz].
        b0 = np.cos(x / 2.0) ** 2 - 1.0 - cyz
        n0 = -sx * b0
        dn = cx * b0 - sx * sx
        dE = -sx * cx / E
        g = 1.0 / (2.0 * E * w * (E + w))
        derivative += np.sum(g * (dn - n0 * dE * (1.0 / E + 1.0 / (E + w))))
    norm = float(L**3)
    a0 /= norm
    a2 /= norm
    a1_sun = -derivative / norm
    a1_tad = -0.5 * a2
    return a0, a1_sun, a1_tad, a1_sun + a1_tad - a0


def photon_multipoint(L, m):
    """Continuous-time Z^3 photon result using a five-point k^2 fit."""
    k, qy, qz = slabs(L)
    sy, sz = np.sin(qy), np.sin(qz)
    ks = m * np.array([0.04, 0.06, 0.08, 0.11, 0.15])
    aE = tad = ward = 0.0
    bubbles = np.zeros(len(ks))
    derivative_integral = 0.0
    for qx in k:
        sx, cx = np.sin(qx), np.cos(qx)
        E2 = sx * sx + sy * sy + sz * sz + m * m
        E = np.sqrt(E2)
        transverse = E2 - sx * sx
        aE += 0.5 * np.sum(cx * cx * transverse / E**5)
        tad += 2.0 * np.sum(sy * sy / E)
        ward += np.sum(-2.0 * cx * cx * transverse / E**3 + 2.0 * sx * sx / E)
        derivative_integral += np.sum((cx * cx - sx * sx) / E - sx * sx * cx * cx / E**3)
        for i, ext in enumerate(ks):
            sxp = np.sin(qx + ext)
            Ep = np.sqrt(sxp * sxp + sy * sy + sz * sz + m * m)
            y = sx * sxp - sy * sy + sz * sz + m * m
            bubbles[i] += -4.0 * np.sum(
                np.cos(qy) ** 2 * (E * Ep + y) / (2.0 * E * Ep * (E + Ep))
            )
    norm = float(L**3)
    aE /= norm
    tad /= norm
    ward /= norm
    derivative_integral /= norm
    values = (bubbles / norm + tad) / (4.0 * np.sin(ks / 2.0) ** 2)
    # Fit through quadratic order in lattice external momentum squared.
    x = (2.0 * np.sin(ks / 2.0)) ** 2
    aB = np.polynomial.polynomial.polyfit(x, values, 2)[0]
    per_dirac = U * (aB - aE) / 16.0
    return per_dirac, U * ward, U * derivative_integral


def arithmetic():
    delta = -16.06 - 2.0 * (-0.671)
    alpha = 1.0 / 137.036
    dc = delta * alpha / (4.0 * np.pi)
    me = 0.51099895e6
    energy = 1.4e15
    threshold = 2.0 * me / np.sqrt(2.0 * abs(dc))
    bound = 2.0 * me**2 / energy**2
    mpl = 1.22e19
    mstar = mpl * np.sqrt(16.0 * np.pi**2 * 1e-20)
    hierarchy = (mpl / mstar) ** 4
    return delta, dc, threshold, bound, mstar, hierarchy


if __name__ == "__main__":
    rotations = proper_cubic_rotations()
    dim, singular = invariant_matrix_dimension(rotations)
    print(f"proper cubic rotations={len(rotations)}, invariant 3x3 matrices={dim}")
    print(f"smallest singular values={singular[-3:]}")

    for L, m, lam in ((128, 0.05, 0.05), (192, 0.035, 0.035)):
        a0, sun, tad, dc = fermion_analytic_derivative(L, m, lam)
        print(
            f"fermion L={L} m=lambda={m}: dc={U*dc:+.5f}, "
            f"tad={U*tad:+.5f}, non-tad={U*(sun-a0):+.5f}"
        )

    for L, m in ((160, 0.1), (320, 0.05)):
        dcg, ward, total_derivative = photon_multipoint(L, m)
        print(
            f"photon L={L} m={m}: per-Dirac dc={dcg:+.6f}, "
            f"Ward*16pi^2={ward:+.3e}, derivative check={total_derivative:+.3e}"
        )

    delta, dc, threshold, bound, mstar, hierarchy = arithmetic()
    print(f"Delta(two tastes)={delta:+.3f}; physical split={dc:+.6e}")
    print(f"photon-decay threshold={threshold/1e6:.3f} MeV; LHAASO bound={bound:.3e}")
    print(f"Mstar(assumed 1/16pi^2 law)={mstar:.3e} GeV; fourth-power hierarchy={hierarchy:.3e}")
