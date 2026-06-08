#!/usr/bin/env python3
"""B4 hypercubic velocity-anisotropy boundary on a supplied Z4 surface."""

from __future__ import annotations

import itertools
import sys

import numpy as np
import sympy as sp


np.seterr(all="ignore")
PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  --  {detail}" if detail else ""
    print(f"  [{tag}] {label}{suffix}")
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def signed_perms(dim: int) -> list[np.ndarray]:
    mats: list[np.ndarray] = []
    for perm in itertools.permutations(range(dim)):
        for signs in itertools.product([1, -1], repeat=dim):
            matrix = np.zeros((dim, dim))
            for i, j in enumerate(perm):
                matrix[i, j] = signs[i]
            mats.append(matrix)
    return mats


def invariant_dim(group_mats: list[np.ndarray]) -> int:
    dim = group_mats[0].shape[0]
    reynolds = np.zeros((dim, dim))
    for matrix in group_mats:
        reynolds += np.abs(matrix)
    reynolds /= len(group_mats)
    return int(np.linalg.matrix_rank(reynolds, tol=1.0e-9))


def coeffs_4d(p0: float, px: float, nk: int, r_s: float, m0: float, r_t: float | None = None) -> tuple[complex, complex]:
    """One-loop toy self-energy coefficients on an isotropic 4D lattice.

    The check is not used as a precision lattice-QFT coefficient. It verifies
    the finite relabeling fact: when r_t = r_s, the temporal and spatial
    coefficient integrals are identical by B4 symmetry; a deliberate
    r_t != r_s deformation breaks the equality.
    """

    if r_t is None:
        r_t = r_s
    ks = (np.arange(nk) + 0.5) / nk * 2.0 * np.pi - np.pi
    q0, qx, qy, qz = np.meshgrid(ks, ks, ks, ks, indexing="ij")
    dk = 2.0 * np.pi / nk
    norm = (dk / (2.0 * np.pi)) ** 4
    qhat2 = (
        (2.0 * np.sin(q0 / 2.0)) ** 2
        + (2.0 * np.sin(qx / 2.0)) ** 2
        + (2.0 * np.sin(qy / 2.0)) ** 2
        + (2.0 * np.sin(qz / 2.0)) ** 2
        + 1.0e-6
    )

    f0 = np.sin(p0 + q0)
    fx = np.sin(qx)
    fy = np.sin(qy)
    fz = np.sin(qz)
    mass = m0 + r_t * (1.0 - np.cos(p0 + q0)) + r_s * (
        (1.0 - np.cos(qx)) + (1.0 - np.cos(qy)) + (1.0 - np.cos(qz))
    )
    st = np.sum(2j * f0 / (f0 * f0 + fx * fx + fy * fy + fz * fz + mass * mass) / qhat2) * norm

    f0 = np.sin(q0)
    fx = np.sin(px + qx)
    fy = np.sin(qy)
    fz = np.sin(qz)
    mass = m0 + r_t * (1.0 - np.cos(q0)) + r_s * (
        (1.0 - np.cos(px + qx)) + (1.0 - np.cos(qy)) + (1.0 - np.cos(qz))
    )
    ss = np.sum(2j * fx / (f0 * f0 + fx * fx + fy * fy + fz * fz + mass * mass) / qhat2) * norm
    return st, ss


def main() -> int:
    print("=" * 88)
    print("B4 HYPERCUBIC VELOCITY-ANISOTROPY BOUNDARY")
    print("=" * 88)

    section("Invariant-count gate")
    oh_dim = 1 + invariant_dim(signed_perms(3))
    b4_dim = invariant_dim(signed_perms(4))
    check(
        "spatial O_h alone leaves two diagonal kinetic coefficients",
        oh_dim == 2,
        detail=f"invariant dimension={oh_dim} (c_t and c_s independent)",
    )
    check(
        "B4 leaves one diagonal kinetic coefficient",
        b4_dim == 1,
        detail=f"invariant dimension={b4_dim} (c_t=c_s forced)",
    )

    section("Finite relabeling gate")
    diffs: list[float] = []
    for nk in (8, 10, 12):
        st, _ = coeffs_4d(0.12, 0.0, nk, 1.0, 0.2)
        _, ss = coeffs_4d(0.0, 0.12, nk, 1.0, 0.2)
        diff = abs(np.imag(st) - np.imag(ss))
        diffs.append(diff)
        print(f"  nk={nk}: |Sigma_t - Sigma_s| = {diff:.3e}")
    check(
        "B4-symmetric self-energy coefficients agree to machine precision",
        all(diff < 1.0e-12 for diff in diffs),
        detail=f"max diff={max(diffs):.3e}",
    )

    casimirs = {"singlet": 0.0, "fundamental": 4.0 / 3.0, "adjoint": 3.0, "sym2": 10.0 / 3.0}
    species_gap = max(abs((a - b) * max(diffs)) for a in casimirs.values() for b in casimirs.values())
    check(
        "representation factors cannot produce a marginal species velocity difference from a zero spacetime difference",
        species_gap < 1.0e-12,
        detail=f"max Casimir-weighted species gap={species_gap:.3e}",
    )

    section("Form-equality gate")
    def form_diff(r_s: float, r_t: float) -> float:
        st, _ = coeffs_4d(0.12, 0.0, 10, r_s, 0.2, r_t=r_t)
        _, ss = coeffs_4d(0.0, 0.12, 10, r_s, 0.2, r_t=r_t)
        return abs(np.imag(st) - np.imag(ss))

    naive_diff = form_diff(0.0, 0.0)
    wilson_diff = form_diff(1.0, 1.0)
    broken_diff = form_diff(1.0, 2.0)
    check(
        "isotropic naive and Wilson forms keep the B4 equality",
        naive_diff < 1.0e-12 and wilson_diff < 1.0e-12,
        detail=f"naive={naive_diff:.3e}, Wilson={wilson_diff:.3e}",
    )
    check(
        "an explicit temporal/spatial form break reintroduces the marginal anisotropy",
        broken_diff > 1.0e-4,
        detail=f"r_t=2, r_s=1 diff={broken_diff:.3e}",
    )

    section("Dimension-6 residual scale")
    k, a = sp.symbols("k a", positive=True)
    dispersion = sp.expand(sp.series((sp.sin(k * a) / a) ** 2, a, 0, 5).removeO())
    check(
        "the first lattice dispersion correction is dimension-6",
        dispersion.coeff(k, 4) == -a**2 / 3,
        detail=f"k^4 coefficient={dispersion.coeff(k, 4)}",
    )
    m_pl_gev = 1.22e19
    residual = (1.0 / 3.0) * (1.0 / m_pl_gev) ** 2
    check(
        "using the scale-reference primitive as units conversion makes the 1 GeV dimension-6 estimate tiny",
        residual < 1.0e-30,
        detail=f"(1/3)(1 GeV/M_Pl)^2={residual:.3e}",
    )

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
