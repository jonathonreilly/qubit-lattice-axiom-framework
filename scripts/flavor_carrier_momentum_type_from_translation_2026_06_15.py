#!/usr/bin/env python3
"""Flavor carrier type split: translation symmetry forces momentum type.

This runner proves only the finite framework-native carrier-type statement:
on the periodic 2x2x2 representative with three commuting translation
unitaries, the joint spectral/BZ basis is explicit, local position-diagonal
observables are generation-blind on the character states, and separating the
three hw=1 corner labels requires momentum-block projectors.

It does not claim that the physical generation locus is forced to be hw=1.
That remains the separate staggered/KS chirality-gate bridge.
"""

from __future__ import annotations

import itertools

import numpy as np


PASS = 0
FAIL = 0


def check(label: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")
    return cond


def translation_matrix(axis: int, sites: list[tuple[int, int, int]]) -> np.ndarray:
    index = {site: i for i, site in enumerate(sites)}
    T = np.zeros((len(sites), len(sites)), dtype=float)
    for site in sites:
        shifted = list(site)
        shifted[axis] = (shifted[axis] + 1) % 2
        T[index[tuple(shifted)], index[site]] = 1.0
    return T


def character_vector(k: tuple[int, int, int], sites: list[tuple[int, int, int]]) -> np.ndarray:
    vals = []
    for n in sites:
        phase = (-1) ** sum(ki * ni for ki, ni in zip(k, n))
        vals.append(phase / np.sqrt(len(sites)))
    return np.array(vals, dtype=float)


def main() -> int:
    sites = list(itertools.product([0, 1], repeat=3))
    T = [translation_matrix(axis, sites) for axis in range(3)]
    I = np.eye(len(sites))

    print("Flavor carrier type split: finite translation/BZ carrier type")

    check(
        "A1 translations are commuting unitaries on the periodic 2x2x2 cell",
        all(np.allclose(Ti.T @ Ti, I) for Ti in T)
        and all(np.allclose(T[i] @ T[j], T[j] @ T[i]) for i in range(3) for j in range(3)),
    )

    corners = list(itertools.product([0, 1], repeat=3))
    psi = {k: character_vector(k, sites) for k in corners}
    U = np.column_stack([psi[k] for k in corners])
    check(
        "A2 Z2^3 character vectors form an orthonormal joint spectral basis",
        np.allclose(U.T @ U, I),
        detail=f"basis_size={U.shape[1]}",
    )

    eigen_ok = True
    for k in corners:
        for axis, Ti in enumerate(T):
            eigen_ok = eigen_ok and np.allclose(Ti @ psi[k], ((-1) ** k[axis]) * psi[k])
    check(
        "A3 each BZ corner is a simultaneous translation eigencharacter",
        eigen_ok,
    )

    projectors = {k: np.outer(psi[k], psi[k]) for k in corners}
    check(
        "A4 momentum projectors are orthogonal idempotents resolving identity",
        all(np.allclose(P @ P, P) for P in projectors.values())
        and all(np.allclose(projectors[k1] @ projectors[k2], np.zeros_like(I))
                for k1 in corners for k2 in corners if k1 != k2)
        and np.allclose(sum(projectors.values()), I),
    )

    hw1 = sorted(k for k in corners if sum(k) == 1)

    def rotate(k: tuple[int, int, int]) -> tuple[int, int, int]:
        return (k[2], k[0], k[1])

    orbit = [hw1[0]]
    while rotate(orbit[-1]) not in orbit:
        orbit.append(rotate(orbit[-1]))
    check(
        "A5 hw=1 contains three corners and C3[111] permutes them transitively",
        len(hw1) == 3 and sorted(orbit) == hw1,
        detail=f"hw1={hw1}, orbit={orbit}",
    )

    P_site0 = np.zeros((8, 8))
    P_site0[0, 0] = 1.0
    local_exps = [float(psi[k].T @ P_site0 @ psi[k]) for k in hw1]
    check(
        "A6 a single-site local projector is generation-blind on hw=1 characters",
        np.allclose(local_exps, [1 / 8] * 3),
        detail=f"<P_site0>={np.round(local_exps, 6).tolist()}",
    )

    abs_profiles = [np.abs(psi[k]) ** 2 for k in hw1]
    check(
        "A7 all position probability profiles are identical across hw=1 characters",
        all(np.allclose(abs_profiles[0], profile) for profile in abs_profiles[1:]),
        detail=f"profile={np.round(abs_profiles[0], 6).tolist()}",
    )

    weights = np.array([0.0, 1.0, 3.0, 4.0, 8.0, 9.0, 11.0, 15.0])
    O_diag = np.diag(weights)
    diag_exps = [float(psi[k].T @ O_diag @ psi[k]) for k in hw1]
    check(
        "A8 every diagonal position observable has the same expectation on hw=1 characters",
        np.allclose(diag_exps, [float(np.mean(weights))] * 3),
        detail=f"diag_expectations={np.round(diag_exps, 6).tolist()}",
    )

    Pk0 = projectors[hw1[0]]
    momentum_exps = [float(psi[k].T @ Pk0 @ psi[k]) for k in hw1]
    check(
        "A9 a momentum-block projector separates the three hw=1 labels",
        np.allclose(momentum_exps, [1.0, 0.0, 0.0]),
        detail=f"<P_k0>={np.round(momentum_exps, 6).tolist()}",
    )

    eps_sum = sum((-1) ** (n[0] + n[1] + n[2]) for n in sites)
    check(
        "A10 extensive position Gamma5 sum vanishes on the full periodic cell",
        eps_sum == 0,
        detail=f"sum_x epsilon(x)={eps_sum}",
    )

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
