#!/usr/bin/env python3
"""Finite support checks for free Dirac CAR positive energy.

This runner verifies only the finite algebra stated in
docs/FREE_DIRAC_CAR_POSITIVE_ENERGY_EQUAL_TIME_ANTICOMMUTATOR_SUPPORT_BOUNDED_NOTE_2026-06-08.md.
It does not select CAR from the framework, prove spacelike microcausality, or
close an OS/Wightman field-construction residual.

The spinor completeness check uses orthonormal Hamiltonian eigenspinors from
numpy.linalg.eigh. A covariant 2E-normalized spin-sum route needs the usual
compensating 1/(2E) field-expansion weight before producing an equal-time
identity.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
NOTE = Path(
    "docs/FREE_DIRAC_CAR_POSITIVE_ENERGY_EQUAL_TIME_ANTICOMMUTATOR_SUPPORT_BOUNDED_NOTE_2026-06-08.md"
)


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name} {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {name} {detail}")


def block(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray) -> np.ndarray:
    return np.block([[a, b], [c, d]])


def main() -> int:
    identity_2 = np.eye(2, dtype=complex)
    zero_2 = np.zeros((2, 2), dtype=complex)
    sigma = [
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    ]

    gamma_0 = block(identity_2, zero_2, zero_2, -identity_2)
    gamma = [block(zero_2, item, -item, zero_2) for item in sigma]

    momentum = np.array([0.4, -0.6, 0.3])
    mass = 0.8
    energy = float(np.sqrt(momentum @ momentum + mass * mass))
    dirac_h = sum(momentum[i] * (gamma_0 @ gamma[i]) for i in range(3)) + mass * gamma_0
    eigvals, eigvecs = np.linalg.eigh(dirac_h)
    u_modes = eigvecs[:, eigvals > 0]
    v_modes = eigvecs[:, eigvals < 0]

    check(
        "MODE_free_massive_dirac_pm_energy",
        np.allclose(np.sort(eigvals), [-energy, -energy, energy, energy])
        and u_modes.shape[1] == 2
        and v_modes.shape[1] == 2,
        f"spectrum +/-E={energy:.3f}; two u modes and two v modes",
    )
    check(
        "spinor_columns_are_orthonormal_eigh_modes",
        np.allclose(eigvecs.conj().T @ eigvecs, np.eye(4), atol=1e-12),
        "eigh returns an orthonormal Hamiltonian eigenbasis",
    )

    one_mode_e = 1.0
    n_a = np.diag([0.0, 1.0, 0.0, 1.0])
    n_b = np.diag([0.0, 0.0, 1.0, 1.0])
    h_car = one_mode_e * n_a + one_mode_e * n_b
    car_eigs = np.linalg.eigvalsh(h_car)
    check(
        "CAR_reordering_is_bounded_below",
        car_eigs.min() >= -1e-12
        and np.allclose(np.sort(car_eigs), [0.0, one_mode_e, one_mode_e, 2.0 * one_mode_e]),
        f"CAR H=E(a^dag a+b^dag b) eigenvalues {np.round(np.sort(car_eigs), 2)}",
    )

    truncation = 8
    h_bose = np.array(
        [
            one_mode_e * n_particle - one_mode_e * n_antiparticle
            for n_particle in range(truncation + 1)
            for n_antiparticle in range(truncation + 1)
        ]
    )
    check(
        "Bose_reordering_is_unbounded_below_trend",
        h_bose.min() <= -one_mode_e * truncation + 1e-9,
        f"Bose H=E(a^dag a-b^dag b) reaches {h_bose.min():.0f} at truncation {truncation}",
    )

    completeness = u_modes @ u_modes.conj().T + v_modes @ v_modes.conj().T
    check(
        "spinor_completeness_gives_equal_time_CAR_matrix",
        np.allclose(completeness, np.eye(4)),
        "orthonormal projectors: sum_s(u u^dag + v v^dag)=I_4",
    )
    pos_projector = u_modes @ u_modes.conj().T
    neg_projector = v_modes @ v_modes.conj().T
    check(
        "positive_negative_energy_projectors_are_orthogonal",
        np.allclose(pos_projector @ neg_projector, np.zeros((4, 4)), atol=1e-12)
        and np.allclose(pos_projector @ pos_projector, pos_projector, atol=1e-12)
        and np.allclose(neg_projector @ neg_projector, neg_projector, atol=1e-12),
        "P_+P_-=0 and P_+^2=P_+, P_-^2=P_-",
    )

    u_2e = np.sqrt(2.0 * energy) * u_modes
    v_2e = np.sqrt(2.0 * energy) * v_modes
    completeness_2e_unweighted = u_2e @ u_2e.conj().T + v_2e @ v_2e.conj().T
    completeness_2e_weighted = completeness_2e_unweighted / (2.0 * energy)
    check(
        "twoE_normalized_spinors_need_field_expansion_weight",
        not np.allclose(completeness_2e_unweighted, np.eye(4))
        and np.allclose(completeness_2e_weighted, np.eye(4)),
        "2E-normalized unweighted sum is 2E I_4; (1/(2E)) weighted sum is I_4",
    )

    bose_sign_matrix = u_modes @ u_modes.conj().T - v_modes @ v_modes.conj().T
    check(
        "Bose_sign_matrix_is_not_equal_time_identity",
        not np.allclose(bose_sign_matrix, np.eye(4)),
        "sum_s(u u^dag - v v^dag) != I_4",
    )

    rapidity = 0.7
    spinor_boost = np.array(
        [
            [np.cosh(rapidity / 2), 0, np.sinh(rapidity / 2), 0],
            [0, np.cosh(rapidity / 2), 0, np.sinh(rapidity / 2)],
            [np.sinh(rapidity / 2), 0, np.cosh(rapidity / 2), 0],
            [0, np.sinh(rapidity / 2), 0, np.cosh(rapidity / 2)],
        ],
        dtype=complex,
    )
    mass_matrix = mass * np.eye(4)
    check(
        "mass_term_scalar_under_supplied_spinor_boost",
        np.allclose(np.linalg.inv(spinor_boost) @ mass_matrix @ spinor_boost, mass_matrix),
        "S^-1(mI)S=mI",
    )

    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    forbidden_closure = [
        "T1 fires",
        "is microcausal",
        "positive-energy and microcausal",
        "keystone's spectrum/causality piece closes",
        "partner chirality now supplied",
        "single remaining residual",
    ]
    check(
        "source_note_keeps_support_boundary",
        NOTE.exists() and all(phrase not in note_text for phrase in forbidden_closure),
        "no submitted closure phrases retained",
    )
    check(
        "source_note_names_open_guardrails",
        "spacelike microcausality is proved" in note_text
        and "partner chirality is physically supplied" in note_text
        and "the framework derives the CAR/spin-statistics selection" in note_text,
        "guardrails keep CAR selection, partner chirality, and spacelike causality open",
    )
    check(
        "source_note_declares_normalization_bridge",
        "normalized" in note_text
        and "projector convention" in note_text
        and "2E" in note_text
        and "1/(2E)" in note_text
        and "not asserted to be `I_4`" in note_text,
        "orthonormal and covariant-spinor normalization routes are separated",
    )

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: finite support only. Given the supplied free Dirac mode algebra, "
        "CAR gives a bounded-below one-mode Hamiltonian and a canonical equal-time "
        "anticommutator matrix; the Bose sign choice is unbounded below. This does "
        "not select CAR, prove spacelike microcausality, or close OS/Wightman field delivery."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
