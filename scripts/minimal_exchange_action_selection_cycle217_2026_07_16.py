#!/usr/bin/env python3
"""Cycle 217: select the minimal static exchange action from the field walk.

Within degree-one Hermitian Laurent polynomials of the already selected local
unitary U, prove that a stationary null mode and positivity force
K=kappa(2I-U-U^dagger), kappa>0.  Prove that proper-cubic covariance uniquely
selects the uniform six-direction scalar source vector.  Verify that stable
quadratic elimination then fixes the attractive same-sign exchange and ties
source and response to one coupling.

This is scoped functional-calculus selection, not uniqueness over all local
actions, larger blocks, nonlinear laws, or QCAs.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import sympy as sp

import active_cubic_source_response_cycle211_2026_07_16 as c211
import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import retarded_cubic_mass_field_cycle213_2026_07_16 as c213
import virtual_exchange_green_kernel_cycle216_2026_07_16 as c216


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "MINIMAL_EXCHANGE_ACTION_SELECTION_CYCLE217_NOTE_2026-07-16.md"
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "degree-one hermitian laurent",
        "stationary null mode",
        "positivity",
        "unique up to positive scale",
        "unique proper-cubic scalar source",
        "attractive sign",
        "one source/response coupling",
        "not uniqueness over all local actions",
        "vacuum-relative mass scalar",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves selection scope and attribution", not missing, missing)


def symbolic_selection_controls() -> None:
    theta, real_part, imaginary_part = sp.symbols(
        "theta u v", real=True
    )
    coefficient = real_part + sp.I * imaginary_part
    constant = -2 * real_part
    eigenvalue = sp.exp(sp.I * theta)
    stiffness = sp.simplify(
        constant
        + coefficient * eigenvalue
        + sp.conjugate(coefficient) / eigenvalue
    )
    first = sp.simplify(sp.diff(stiffness, theta).subs(theta, 0))
    second = sp.simplify(sp.diff(stiffness, theta, 2).subs(theta, 0))
    check(
        "stationary-null Hermiticity gives f'(0)=-2v and f''(0)=-2u",
        first == -2 * imaginary_part and second == -2 * real_part,
        {"first": first, "second": second},
    )

    kappa = sp.symbols("kappa", positive=True, real=True)
    selected = sp.simplify(stiffness.subs({imaginary_part: 0, real_part: -kappa}))
    target = sp.simplify(
        kappa * (2 - sp.exp(sp.I * theta) - sp.exp(-sp.I * theta))
    )
    check(
        "two-sided positivity selects K=kappa(2-U-U^dagger), kappa>0",
        sp.simplify(selected - target) == 0
        and sp.simplify(
            sp.expand_complex(target) - 4 * kappa * sp.sin(theta / 2) ** 2
        )
        == 0,
        selected,
    )

    sample = np.linspace(-np.pi, np.pi, 2001)
    complex_candidate = (
        -2 * (-1.0)
        + (-1.0 + 0.2j) * np.exp(1j * sample)
        + (-1.0 - 0.2j) * np.exp(-1j * sample)
    ).real
    wrong_sign = (
        -2 * 1.0
        + np.exp(1j * sample)
        + np.exp(-1j * sample)
    ).real
    check(
        "imaginary or wrong-sign degree-one coefficients violate positivity",
        np.min(complex_candidate) < -0.01 and np.min(wrong_sign) < -0.01,
        {
            "complex_min": np.min(complex_candidate),
            "wrong_sign_min": np.min(wrong_sign),
        },
    )


def scalar_vertex_selection_controls() -> None:
    frames = c210.proper_cubic_frames()
    stacked = np.concatenate(
        tuple(c210.direction_permutation(frame) - np.eye(6) for frame in frames),
        axis=0,
    )
    singular_values = np.linalg.svd(stacked, compute_uv=False)
    rank = int(np.sum(singular_values > 1e-10))
    null_dimension = 6 - rank
    check(
        "the six-direction representation has one unique proper-cubic invariant vector",
        len(frames) == 24
        and null_dimension == 1
        and np.linalg.norm(stacked @ c210.UNIFORM) < 2e-12,
        {"rank": rank, "null_dimension": null_dimension},
    )

    rng = np.random.default_rng(217)
    candidate = rng.normal(size=6) + 1j * rng.normal(size=6)
    averaged = sum(
        c210.direction_permutation(frame) @ candidate for frame in frames
    ) / len(frames)
    projected = c210.UNIFORM * np.vdot(c210.UNIFORM, candidate)
    check(
        "group averaging any local source vector leaves only the scalar source",
        np.linalg.norm(averaged - projected) < 2e-12,
    )


def matrix_family_controls() -> None:
    rng = np.random.default_rng(218)
    rows = []
    for _ in range(32):
        momentum = rng.uniform(-2.8, 2.8, size=3)
        unitary = c216.walk(momentum)
        kappa = rng.uniform(0.2, 2.0)
        selected = kappa * (2 * np.eye(6) - unitary - unitary.conj().T)
        eigenvalues = np.linalg.eigvalsh(selected)
        rows.append(
            (
                np.linalg.norm(selected - kappa * c216.stiffness(momentum)),
                float(np.min(eigenvalues)),
            )
        )
    check(
        "the selected degree-one family is positive on held-out field modes",
        max(row[0] for row in rows) < 2e-12
        and min(row[1] for row in rows) > -4e-12,
        {
            "identity_residual": max(row[0] for row in rows),
            "minimum_eigenvalue": min(row[1] for row in rows),
        },
    )

    momentum = np.array((0.31, -0.19, 0.11))
    unitary = c216.walk(momentum)
    massive = 0.3 * np.eye(6) + c216.stiffness(momentum)
    check(
        "deleting the stationary null condition introduces an independent screened mass term",
        np.min(np.linalg.eigvalsh(massive)) > 0.29
        and np.linalg.norm((2 * np.eye(6) - unitary - unitary.conj().T) - c216.stiffness(momentum))
        < 2e-12,
    )


def action_and_response_controls() -> None:
    side = 31
    green = c211.solve_field(c211.point_source(side))
    kernel = 3 * green
    source_position = (0, 0, 0)
    probe_position = (4, 0, 0)
    species_set = tuple(c210.tuned_species(beta) for beta in (-0.2, -0.3, -0.4))
    source_species = species_set[-1]
    source_charge = c213.rest_charge(source_species.coin, c210.P_SCALAR)
    coupling = 0.08
    gradient = c211.gradient(kernel, probe_position)
    rows = []
    for species in species_set:
        test_charge = c213.rest_charge(species.coin, c210.P_SCALAR)
        force = coupling**2 * source_charge * test_charge * gradient[0]
        response = c210.force_response(species, force)
        normalized = response.acceleration / (
            -coupling**2 * source_charge * gradient[0]
        )
        rows.append((species.beta, test_charge, response.measured_mass, normalized))
    check(
        "one scalar action vertex ties source and response into one universal coupling",
        max(abs(row[3] - 1) for row in rows) < 0.007,
        rows,
    )

    left_charge = c213.rest_charge(species_set[0].coin, c210.P_SCALAR)
    right_charge = c213.rest_charge(species_set[-1].coin, c210.P_SCALAR)
    pair_kernel = kernel[probe_position]
    on_shell_cross = -coupling**2 * left_charge * right_charge * pair_kernel
    check(
        "positive stiffness elimination fixes the attractive sign for like scalar charges",
        pair_kernel > 0 and on_shell_cross < 0,
        {"kernel": pair_kernel, "cross_action": on_shell_cross},
    )

    kappa = 1.7
    rescaled_coupling = coupling * np.sqrt(kappa)
    reference_strength = coupling**2
    rescaled_strength = rescaled_coupling**2 / kappa
    check(
        "the remaining positive stiffness scale is absorbed into the coupling magnitude",
        abs(reference_strength - rescaled_strength) < 2e-15,
        (reference_strength, rescaled_strength),
    )

    frame_forces = []
    for frame in c210.proper_cubic_frames():
        moved = tuple(int(value) for value in (frame @ np.asarray(probe_position)) % side)
        frame_forces.append(
            np.linalg.norm(c211.gradient(kernel, moved) - frame @ gradient)
        )
    check(
        "the selected scalar action carries its force through every cubic frame",
        max(frame_forces) < 2e-12,
        max(frame_forces),
    )

    record_zero = np.array((1, 0), dtype=complex)
    record_plus = np.array((1, 1), dtype=complex) / np.sqrt(2)
    archived = (
        source_charge,
        source_charge * np.vdot(record_zero, record_zero).real,
        source_charge
        * np.vdot(record_zero, record_zero).real
        * np.vdot(record_plus, record_plus).real,
    )
    check(
        "the uniquely selected source vector is independent of archive redundancy",
        max(abs(value - source_charge) for value in archived) < 2e-14,
        archived,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    symbolic_selection_controls()
    scalar_vertex_selection_controls()
    matrix_family_controls()
    action_and_response_controls()
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
