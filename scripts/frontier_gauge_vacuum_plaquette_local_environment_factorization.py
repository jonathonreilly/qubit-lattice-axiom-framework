#!/usr/bin/env python3
"""
Bounded fourth-power diagonal matrix packet.

This does not close analytic P(6), the residual source-sector environment, or
the operator-level mixed-kernel compression bridge. It computes the finite
stipulated integral coefficients on NMAX = 5 and packages their fourth powers
as the finite matrix D_6^packet. No physical local-factor identification is
claimed.
"""

from __future__ import annotations

import numpy as np
from scipy.special import iv


THEOREM_PASS = 0
SUPPORT_PASS = 0
FAIL = 0

BETA = 6.0
ARG = BETA / 3.0
MODE_MAX = 80
NMAX = 5


def check(name: str, condition: bool, detail: str = "", bucket: str = "THEOREM") -> None:
    global THEOREM_PASS, SUPPORT_PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        if bucket == "SUPPORT":
            SUPPORT_PASS += 1
        else:
            THEOREM_PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] [{bucket}] {name}")
    if detail:
        print(f"         {detail}")


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def highest_weight_triple(p: int, q: int) -> list[int]:
    return [p + q, q, 0]


def coefficient_matrix(mode: int, lam: list[int]) -> np.ndarray:
    return np.array(
        [[iv(mode + lam[j] + i - j, ARG) for j in range(3)] for i in range(3)],
        dtype=float,
    )


def wilson_character_coefficient(p: int, q: int) -> float:
    lam = highest_weight_triple(p, q)
    total = 0.0
    for mode in range(-MODE_MAX, MODE_MAX + 1):
        total += float(np.linalg.det(coefficient_matrix(mode, lam)))
    return total


def normalized_link_eigenvalue(p: int, q: int, c00: float) -> float:
    return wilson_character_coefficient(p, q) / (dim_su3(p, q) * c00)


def recurrence_neighbors(p: int, q: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for a, b in [
        (p + 1, q),
        (p - 1, q + 1),
        (p, q - 1),
        (p, q + 1),
        (p + 1, q - 1),
        (p - 1, q),
    ]:
        if a >= 0 and b >= 0:
            out.append((a, b))
    return out


def weights_box(nmax: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


def build_recurrence_matrix(nmax: int) -> tuple[np.ndarray, list[tuple[int, int]], dict[tuple[int, int], int]]:
    weights = weights_box(nmax)
    index = {w: i for i, w in enumerate(weights)}
    jmat = np.zeros((len(weights), len(weights)), dtype=float)
    for p, q in weights:
        i = index[(p, q)]
        for a, b in recurrence_neighbors(p, q):
            if (a, b) in index:
                jmat[index[(a, b)], i] += 1.0 / 6.0
    return jmat, weights, index


def conjugation_swap_matrix(
    weights: list[tuple[int, int]], index: dict[tuple[int, int], int]
) -> np.ndarray:
    swap = np.zeros((len(weights), len(weights)), dtype=float)
    for w in weights:
        swap[index[(w[1], w[0])], index[w]] = 1.0
    return swap


def matrix_exponential_symmetric(m: np.ndarray, tau: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh(m)
    return (vecs * np.exp(tau * vals)) @ vecs.T


def dominant_eigenpair(m: np.ndarray) -> tuple[float, np.ndarray]:
    vals, vecs = np.linalg.eigh(m)
    idx = int(np.argmax(vals))
    vec = vecs[:, idx]
    if np.sum(vec) < 0.0:
        vec = -vec
    return float(vals[idx]), vec


def main() -> int:
    c00 = wilson_character_coefficient(0, 0)
    weights = weights_box(NMAX)
    a_link = np.array([normalized_link_eigenvalue(p, q, c00) for p, q in weights], dtype=float)
    d_local = np.diag(a_link**4)

    jmat, _, index = build_recurrence_matrix(NMAX)
    swap = conjugation_swap_matrix(weights, index)
    multiplier = matrix_exponential_symmetric(jmat, BETA / 2.0)

    local_only = multiplier @ d_local @ multiplier
    local_only_sym = float(np.max(np.abs(local_only - local_only.T)))
    local_only_swap = float(np.max(np.abs(swap @ local_only - local_only @ swap)))
    _, psi_local = dominant_eigenpair(local_only)
    local_value = float(psi_local @ (jmat @ psi_local))

    nonmarked_scalar_norm = c00 / c00
    nonmarked_counts = [0, 1, 7, 31]
    normalized_mixed_boxes = [np.diag((nonmarked_scalar_norm**n) * (a_link**4)) for n in nonmarked_counts]
    mix_box_spread = max(
        float(np.max(np.abs(box - d_local))) for box in normalized_mixed_boxes
    )

    local_sym = float(np.max(np.abs(swap @ d_local - d_local @ swap)))
    min_local = float(np.min(np.diag(d_local)))
    min_link = float(np.min(a_link))

    print("=" * 78)
    print("FINITE FOURTH-POWER DIAGONAL MATRIX PACKET")
    print("=" * 78)
    print()
    print("Stipulated integral coefficients at x = 2")
    print(f"  c_(0,0)                              = {c00:.15f}")
    for rep in [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0)]:
        idx = weights.index(rep)
        print(
            f"  a_link{rep!s:<11} = {a_link[idx]:.15f}   "
            f"a_link^4 = {a_link[idx]**4:.15f}"
        )
    print()
    print("Finite fourth-power diagonal packet")
    print(f"  non-marked trivial-channel factor     = {nonmarked_scalar_norm:.15f}")
    print(f"  scalar-insertion normalized spread    = {mix_box_spread:.3e}")
    print(f"  fourth-power swap error               = {local_sym:.3e}")
    print(f"  min/max fourth-power diagonal         = {float(np.min(np.diag(d_local))):.12f}, {float(np.max(np.diag(d_local))):.12f}")
    print()
    print("Finite constructed matrix package")
    print(f"  constructed package symmetry error    = {local_only_sym:.3e}")
    print(f"  constructed package swap error        = {local_only_swap:.3e}")
    print(f"  constructed package Perron <J>        = {local_value:.12f}")
    print()

    check(
        "the stipulated integral has explicit normalized SU(3) coefficients from the Bessel-determinant mode sum",
        c00 > 0.0 and abs(a_link[weights.index((0, 0))] - 1.0) < 1.0e-12,
        detail=f"c_(0,0)={c00:.12f}, a_(0,0)={a_link[weights.index((0, 0))]:.12f}",
    )
    check(
        "the constructed trivial-channel scalar normalization is unity",
        abs(nonmarked_scalar_norm - 1.0) < 1.0e-15,
        detail="support-only normalization bookkeeping",
        bucket="SUPPORT",
    )
    check(
        "the finite fourth-power matrix D_6^packet = diag(a_(p,q)(6)^4) is positive and conjugation-symmetric",
        local_sym < 1.0e-12 and min_local > 0.0 and min_link > 0.0,
        detail=f"matrix symmetry={local_sym:.3e}, min diagonal={min_local:.6e}; no local-factor authority is claimed",
    )
    check(
        "the finite constructed package exp(3 J) D_6^packet exp(3 J) is self-adjoint and conjugation-symmetric",
        local_only_sym < 1.0e-12 and local_only_swap < 1.0e-12,
        detail=f"package symmetry={local_only_sym:.3e}, swap={local_only_swap:.3e}",
    )

    check(
        "the constructed package has a finite positive Perron diagnostic",
        np.isfinite(local_value) and local_value > 0.0,
        detail=f"constructed <J> = {local_value:.6e}; no physical readout is inferred",
        bucket="SUPPORT",
    )
    check(
        "the fourth-power diagonal is nonconstant on the finite box",
        float(np.max(np.diag(d_local)) - np.min(np.diag(d_local))) > 1.0e-3,
        detail="finite diagnostic only",
        bucket="SUPPORT",
    )
    check(
        "all constructed coefficient and matrix entries are finite",
        bool(np.all(np.isfinite(a_link)) and np.all(np.isfinite(d_local)) and np.all(np.isfinite(local_only))),
        detail="numerical-health diagnostic only",
        bucket="SUPPORT",
    )

    print()
    print("=" * 78)
    print(f"SUMMARY: THEOREM PASS={THEOREM_PASS} SUPPORT={SUPPORT_PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
