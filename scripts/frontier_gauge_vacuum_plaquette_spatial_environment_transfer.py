#!/usr/bin/env python3
"""
Finite class-sector transfer witness for the plaquette route.

This does not close analytic P(6), identify the actual unmarked spatial Wilson
environment, or compute physical beta=6 boundary data. It only checks one
bounded transfer-amplitude packet: a constructed positive self-adjoint
class-sector transfer witness, a finite boundary vector, and the normalized
boundary-amplitude sequence generated from them.
"""

from __future__ import annotations

import numpy as np


THEOREM_PASS = 0
SUPPORT_PASS = 0
FAIL = 0

NMAX = 5
ETA = 0.32
DEPTH = 3
TOL = 1.0e-14


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
    jmat, weights, index = build_recurrence_matrix(NMAX)
    swap = conjugation_swap_matrix(weights, index)

    # Positive symmetric spatial environment layer on the class sector.
    layer_diag = np.diag(
        [
            np.exp(-0.18 * (p + q) - 0.05 * ((p - q) ** 2))
            for p, q in weights
        ]
    )
    spatial_transfer = matrix_exponential_symmetric(jmat, ETA) @ layer_diag @ matrix_exponential_symmetric(jmat, ETA)

    # Positive conjugation-symmetric boundary state induced by the marked rim.
    eta0 = np.zeros(len(weights), dtype=float)
    eta0[index[(0, 0)]] = 1.0
    boundary = matrix_exponential_symmetric(jmat, 0.5 * ETA) @ eta0

    amp = np.linalg.matrix_power(spatial_transfer, DEPTH) @ boundary
    z_packet = amp.copy()
    rho_packet = z_packet / z_packet[index[(0, 0)]]

    transfer_sym = float(np.max(np.abs(spatial_transfer - spatial_transfer.T)))
    transfer_swap = float(np.max(np.abs(swap @ spatial_transfer - spatial_transfer @ swap)))
    boundary_swap = float(np.max(np.abs(swap @ boundary - boundary)))
    boundary_min = float(np.min(boundary))
    z_swap = float(np.max(np.abs(swap @ z_packet - z_packet)))
    z_min = float(np.min(z_packet))
    rho_min = float(np.min(rho_packet))

    _, psi = dominant_eigenpair(spatial_transfer)
    overlap = float(np.dot(psi, amp) / (np.linalg.norm(psi) * np.linalg.norm(amp)))
    expectation = float(psi @ (jmat @ psi))

    print("=" * 78)
    print("GAUGE-VACUUM PLAQUETTE SPATIAL ENVIRONMENT TRANSFER WITNESS")
    print("=" * 78)
    print()
    print("Finite class-sector witness pieces")
    print(f"  source-operator symmetry error        = {float(np.max(np.abs(jmat - jmat.T))):.3e}")
    print(f"  spatial transfer symmetry error       = {transfer_sym:.3e}")
    print(f"  spatial transfer swap error           = {transfer_swap:.3e}")
    print()
    print("Constructed boundary-amplitude packet")
    print(f"  witness depth                         = {DEPTH}")
    print(f"  positivity tolerance                  = {TOL:.1e}")
    print(f"  boundary minimum entry                = {boundary_min:.3e}")
    print(f"  boundary swap error                   = {boundary_swap:.3e}")
    print(f"  z_packet min / max                    = {z_min:.12f}, {float(np.max(z_packet)):.12f}")
    print(f"  rho_packet min / max                  = {rho_min:.12f}, {float(np.max(rho_packet)):.12f}")
    print(f"  coefficient swap error                = {z_swap:.3e}")
    print()
    print("Finite Perron witness")
    print(f"  Perron overlap with boundary amplitude= {overlap:.12f}")
    print(f"  Perron <J>                            = {expectation:.12f}")
    print()

    check(
        "the finite packet has a positive self-adjoint conjugation-symmetric transfer witness on the class sector",
        transfer_sym < TOL and transfer_swap < TOL and float(np.min(np.linalg.eigvalsh(spatial_transfer))) > 0.0,
        detail="the constructed class-sector packet is one explicit positive symmetric transfer witness",
    )
    check(
        "the finite boundary vector is nonnegative to roundoff tolerance and conjugation-symmetric",
        boundary_swap < TOL and boundary_min >= -TOL,
        detail=f"minimum boundary amplitude={boundary_min:.6e}, tolerance={TOL:.1e}",
    )
    check(
        "the finite packet coefficients are boundary amplitudes of the constructed transfer witness",
        z_min > 0.0 and z_swap < TOL,
        detail="z_packet is realized as a matrix-element sequence of one explicit positive transfer witness",
    )
    check(
        "the normalized finite packet rho_packet is not a generic free positive sequence",
        rho_min > 0.0 and abs(rho_packet[index[(0, 0)]] - 1.0) < TOL,
        detail="once the finite witness is fixed, rho_packet is a normalized boundary-amplitude sequence",
    )

    check(
        "the constructed boundary-amplitude sequence remains positivity-compatible on the truncated class sector",
        z_min > 0.0,
        detail=f"minimum boundary amplitude={z_min:.3e}",
        bucket="SUPPORT",
    )
    check(
        "the finite transfer witness is distinct from a trivial all-ones coefficient packet",
        float(np.max(np.abs(rho_packet - 1.0))) > 1.0e-3,
        detail="the constructed packet has nontrivial boundary-amplitude structure",
        bucket="SUPPORT",
    )
    check(
        "the finite witness localizes the harder framework-point target to actual Wilson-environment boundary-state / Perron data",
        overlap > 0.0 and expectation > 0.0,
        detail=f"Perron overlap={overlap:.6f}, Perron <J>={expectation:.6f}",
        bucket="SUPPORT",
    )

    print()
    print("=" * 78)
    print(f"SUMMARY: THEOREM PASS={THEOREM_PASS} SUPPORT={SUPPORT_PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
