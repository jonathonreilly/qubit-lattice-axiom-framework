#!/usr/bin/env python3
"""Verify the proper-cubic scalar-even antipodal transition lemma.

Paired note:
    docs/PROPER_CUBIC_SCALAR_EVEN_ANTIPODAL_TRANSITION_LEMMA_NOTE_2026-07-23.md
"""

from __future__ import annotations

import math
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as cycle219
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as cycle210


TOL = 2e-12
TRAIN_BETAS = (-0.4, -0.3, -0.2, 0.0, 0.7)
HELD_BETAS = (-2.4, -0.35, 1.8)
PASS = 0
FAIL = 0

I6 = np.eye(6, dtype=complex)
REVERSE = np.zeros((6, 6), dtype=complex)
REVERSE[np.arange(6), (1, 0, 3, 2, 5, 4)] = 1
SCALAR = np.ones(6, dtype=complex) / math.sqrt(6)
EVEN = np.asarray((0.5, 0.5, -0.5, -0.5, 0.0, 0.0), dtype=complex)
P_SCALAR = np.outer(SCALAR, SCALAR.conj())
P_EVEN = (I6 + REVERSE) / 2 - P_SCALAR
P_VECTOR = (I6 - REVERSE) / 2
PLUS = (SCALAR + EVEN) / math.sqrt(2)
MINUS = (SCALAR - EVEN) / math.sqrt(2)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS: {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {label} :: {detail}")


def common_phase(beta: float) -> complex:
    return complex(np.exp(-1j * np.tan(beta / 2)))


def independent_coin(beta: float, *, even_phase: float = math.pi) -> np.ndarray:
    phase = common_phase(beta)
    return phase * (
        P_SCALAR
        + np.exp(1j * even_phase) * P_EVEN
        + np.exp(1j * beta) * P_VECTOR
    )


def projector_controls() -> None:
    projectors = (P_SCALAR, P_EVEN, P_VECTOR)
    hermitian = max(float(np.linalg.norm(p - p.conj().T)) for p in projectors)
    idempotent = max(float(np.linalg.norm(p @ p - p)) for p in projectors)
    orthogonal = max(
        float(np.linalg.norm(projectors[i] @ projectors[j]))
        for i in range(3)
        for j in range(3)
        if i != j
    )
    resolution = float(np.linalg.norm(sum(projectors) - I6))
    check(
        "reversal projectors form an orthogonal Hermitian resolution",
        max(hermitian, idempotent, orthogonal, resolution) < TOL,
        {
            "hermitian": hermitian,
            "idempotent": idempotent,
            "orthogonal": orthogonal,
            "resolution": resolution,
        },
    )

    vector_residuals = {
        "scalar_norm": abs(float(np.vdot(SCALAR, SCALAR).real) - 1),
        "even_norm": abs(float(np.vdot(EVEN, EVEN).real) - 1),
        "overlap": abs(complex(np.vdot(SCALAR, EVEN))),
        "P_scalar": float(np.linalg.norm(P_SCALAR @ SCALAR - SCALAR)),
        "P_even": float(np.linalg.norm(P_EVEN @ EVEN - EVEN)),
        "P_vector_scalar": float(np.linalg.norm(P_VECTOR @ SCALAR)),
        "P_vector_even": float(np.linalg.norm(P_VECTOR @ EVEN)),
    }
    check(
        "chosen scalar and even vectors obey the exact subspace hypotheses",
        max(vector_residuals.values()) < TOL,
        vector_residuals,
    )

    hadamard = np.asarray(((1, 1), (1, -1)), dtype=complex) / math.sqrt(2)
    abstract_swap = hadamard.conj().T @ np.diag((1, -1)) @ hadamard
    check(
        "independent two-dimensional reduction is the swap matrix",
        np.linalg.norm(abstract_swap - np.asarray(((0, 1), (1, 0)))) < TOL,
        abstract_swap,
    )


def family_controls() -> None:
    rows: list[dict[str, float]] = []
    frame_residuals: list[float] = []
    for beta in TRAIN_BETAS + HELD_BETAS:
        phase = common_phase(beta)
        coin = independent_coin(beta)
        implemented = cycle219.common_species(beta).coin
        basis = np.column_stack((PLUS, MINUS))
        compressed = basis.conj().T @ coin @ basis
        expected_compressed = phase * np.asarray(((0, 1), (1, 0)), dtype=complex)
        row = {
            "beta": beta,
            "implementation": float(np.linalg.norm(coin - implemented)),
            "plus_to_minus": float(np.linalg.norm(coin @ PLUS - phase * MINUS)),
            "minus_to_plus": float(np.linalg.norm(coin @ MINUS - phase * PLUS)),
            "inverse_plus": float(
                np.linalg.norm(coin.conj().T @ PLUS - phase.conjugate() * MINUS)
            ),
            "inverse_minus": float(
                np.linalg.norm(coin.conj().T @ MINUS - phase.conjugate() * PLUS)
            ),
            "square_plus": float(
                np.linalg.norm(coin @ coin @ PLUS - phase**2 * PLUS)
            ),
            "square_minus": float(
                np.linalg.norm(coin @ coin @ MINUS - phase**2 * MINUS)
            ),
            "compressed": float(np.linalg.norm(compressed - expected_compressed)),
            "unitarity": float(np.linalg.norm(coin.conj().T @ coin - I6)),
        }
        rows.append(row)

        for frame in cycle210.proper_cubic_frames():
            representation = cycle210.direction_permutation(frame)
            transported_even = representation @ EVEN
            transported_plus = (SCALAR + transported_even) / math.sqrt(2)
            transported_minus = (SCALAR - transported_even) / math.sqrt(2)
            frame_residuals.extend(
                (
                    float(
                        np.linalg.norm(
                            representation @ coin @ representation.conj().T - coin
                        )
                    ),
                    float(
                        np.linalg.norm(
                            coin @ transported_plus - phase * transported_minus
                        )
                    ),
                    float(
                        np.linalg.norm(
                            coin @ transported_minus - phase * transported_plus
                        )
                    ),
                )
            )

    check(
        "train and held values match the existing supplied coin implementation",
        max(row["implementation"] for row in rows) < TOL,
        rows,
    )
    identity_residual = max(
        max(value for key, value in row.items() if key != "beta") for row in rows
    )
    check(
        "swap, inverse, square, compression, and unitarity identities hold",
        identity_residual < TOL,
        {"maximum_residual": identity_residual},
    )
    check(
        "all 24 proper-cubic frames preserve the transported transition identity",
        max(frame_residuals) < TOL and len(frame_residuals) == 24 * 3 * len(rows),
        {"checks": len(frame_residuals), "maximum_residual": max(frame_residuals)},
    )


def mutation_control() -> None:
    mutation_residuals = []
    for beta in TRAIN_BETAS + HELD_BETAS:
        mutated = independent_coin(beta, even_phase=math.pi + 0.05)
        mutation_residuals.append(
            float(np.linalg.norm(mutated @ PLUS - common_phase(beta) * MINUS))
        )
    check(
        "moving the even-sector phase away from minus one breaks the exact swap",
        min(mutation_residuals) > 0.03,
        {
            "minimum_mutation_residual": min(mutation_residuals),
            "maximum_mutation_residual": max(mutation_residuals),
        },
    )


def main() -> int:
    print("proper-cubic scalar-even antipodal transition lemma runner")
    print(f"train_betas={TRAIN_BETAS}")
    print(f"held_betas={HELD_BETAS}")
    try:
        projector_controls()
        family_controls()
        mutation_control()
    except Exception as exc:
        global FAIL
        FAIL += 1
        print(f"FAIL: runner exception :: {exc!r}")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
