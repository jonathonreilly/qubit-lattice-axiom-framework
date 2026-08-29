#!/usr/bin/env python3
"""Exact certificate for the Block243 q=4 O10 temporal cup bridge.

The raw cup C: V^3 -> V_p x V_A x V^3 is normalized to Chat=C/sqrt(3).
For the supplied even four-strand central multiplier R4, this runner computes

    Delta4 = Chat^T R_(pDEF) (I-P_C) R_(ADEF) Chat

directly on the 3^5 carrier and proves the closed spin-sector formulas.  This
is a multiplicativity-defect lemma, not the complete q=4 response and not the
physical conditional-Haar projector Q.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import product
from pathlib import Path

import numpy as np
import sympy as sp


AUDIT_TIMEOUT_SEC = 180
ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_O10_TEMPORAL_CUP_BRIDGE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_O10_CUP_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
MUTATIONS = (
    "multiply_separate_compressions",
    "claim_positive_bridge",
    "identify_cup_projector_with_physical_q",
    "drop_spin_three",
    "claim_complete_q4_response",
    "axiom_edit",
)

GENERATORS = (
    np.array(((0, 0, 0), (0, 0, -1), (0, 1, 0)), dtype=np.int64),
    np.array(((0, 0, 1), (0, 0, 0), (-1, 0, 0)), dtype=np.int64),
    np.array(((0, -1, 0), (1, 0, 0), (0, 0, 0)), dtype=np.int64),
)
IDENTITY3 = np.eye(3, dtype=np.int64)


def _kron_all(factors: tuple[np.ndarray, ...]) -> np.ndarray:
    result = np.array([[1]], dtype=np.int64)
    for factor in factors:
        result = np.kron(result, factor)
    return result


@lru_cache(None)
def _embedded_generators(power: int) -> dict[tuple[int, int], np.ndarray]:
    return {
        (axis, position): _kron_all(tuple(
            generator if slot == position else IDENTITY3
            for slot in range(power)
        ))
        for axis, generator in enumerate(GENERATORS)
        for position in range(power)
    }


def _casimir(power: int, positions: tuple[int, ...]) -> sp.SparseMatrix:
    dimension = 3**power
    embedded = _embedded_generators(power)
    result = np.zeros((dimension, dimension), dtype=np.int64)
    for axis in range(3):
        total = sum(
            (embedded[axis, position] for position in positions),
            np.zeros_like(result),
        )
        result -= total @ total
    return sp.SparseMatrix(result)


def _flat(indices: tuple[int, ...]) -> int:
    result = 0
    for index in indices:
        result = 3 * result + index
    return result


@lru_cache(None)
def _cup() -> sp.SparseMatrix:
    entries: dict[tuple[int, int], int] = {}
    for d, e, f in product(range(3), repeat=3):
        for p in range(3):
            entries[(_flat((p, p, d, e, f)), _flat((d, e, f)))] = 1
    return sp.SparseMatrix(243, 27, entries)


def _apply_polynomial(
    operator: sp.SparseMatrix,
    matrix: sp.MatrixBase,
    coefficients: tuple[sp.Expr, ...],
) -> sp.MatrixBase:
    result = sp.zeros(matrix.rows, matrix.cols)
    for coefficient in reversed(coefficients):
        result = operator * result + coefficient * matrix
    return result


@lru_cache(None)
def exact_bridge_data() -> dict[str, object]:
    t, u, v, w = sp.symbols("t u v w")
    x = sp.symbols("x")
    weights = (sp.Integer(1), t, u, v, w)
    polynomial = sp.interpolate(
        [(spin * (spin + 1), weights[spin]) for spin in range(5)], x
    ).expand()
    coefficients = tuple(polynomial.coeff(x, degree) for degree in range(5))

    cup = _cup()
    cup_projector = cup * cup.T / 3
    casimir_a = _casimir(5, (1, 2, 3, 4))
    casimir_p = _casimir(5, (0, 2, 3, 4))
    r_a_cup = _apply_polynomial(casimir_a, cup, coefficients)
    complement = r_a_cup - cup * (cup.T * r_a_cup) / 3
    delta = sp.simplify(
        cup.T * _apply_polynomial(casimir_p, complement, coefficients) / 3
    )

    casimir3 = sp.Matrix(_casimir(3, (0, 1, 2)))
    identity27 = sp.eye(27)
    projectors: dict[int, sp.Matrix] = {}
    for spin in range(4):
        eigenvalue = spin * (spin + 1)
        projector = identity27
        for other in range(4):
            if other == spin:
                continue
            other_eigenvalue = other * (other + 1)
            projector = (
                projector
                * (casimir3 - other_eigenvalue * identity27)
                / (eigenvalue - other_eigenvalue)
            )
        projectors[spin] = projector

    formulas = {
        0: sp.Integer(0),
        1: (9*t**2 + 30*t*u - 48*t - 35*u**2 + 40*u + 4) / 162,
        2: -(3*t**2 + 50*t*u - 56*t*v - 25*u**2 + 28*v**2) / 150,
        3: -(80*u**2 + 560*u*v - 720*u*w - 343*v**2
             + 126*v*w + 297*w**2) / 1764,
    }
    direct_scalars = {
        spin: sp.factor(sp.trace(projectors[spin] * delta) / sp.trace(projectors[spin]))
        for spin in range(4)
    }
    central_residuals = {
        spin: sp.simplify(
            projectors[spin] * delta - direct_scalars[spin] * projectors[spin]
        )
        for spin in range(4)
    }
    return {
        "symbols": (t, u, v, w),
        "polynomial": polynomial,
        "cup": cup,
        "cup_projector": cup_projector,
        "delta": delta,
        "casimir3": casimir3,
        "formulas": formulas,
        "direct_scalars": direct_scalars,
        "central_residuals": central_residuals,
    }


def exact_checks(mutation: str | None = None):
    data = exact_bridge_data()
    t, u, v, w = data["symbols"]
    cup = data["cup"]
    cup_projector = data["cup_projector"]
    delta = data["delta"]
    formulas = dict(data["formulas"])
    if mutation == "multiply_separate_compressions":
        formulas[1] = sp.Integer(0)
    if mutation == "drop_spin_three":
        formulas[3] = sp.Integer(0)

    sample = {t: sp.Rational(3, 10), u: sp.Rational(2, 5),
              v: sp.Rational(1, 2), w: sp.Rational(3, 5)}
    sample_expected = (
        sp.Integer(0), sp.Rational(49, 1800),
        -sp.Rational(29, 5000), -sp.Rational(1097, 176400),
    )
    sample_actual = tuple(sp.factor(data["direct_scalars"][spin].subs(sample))
                          for spin in range(4))
    identity = {t: 1, u: 1, v: 1, w: 1}
    identity_gradients = tuple(
        sp.diff(data["formulas"][spin], variable).subs(identity)
        for spin in range(4) for variable in (t, u, v, w)
    )
    note = (ROOT / AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8").lower()
    scope_ok = (
        "actual_current_surface_status: conditional-support" in note
        and "proposal_allowed: false" in note
        and "physical `q=" in note
        and "not positive" in note
    )
    if mutation in (
        "claim_positive_bridge",
        "identify_cup_projector_with_physical_q",
        "claim_complete_q4_response",
    ):
        scope_ok = False
    axiom_ok = mutation != "axiom_edit"

    checks = (
        ("the raw cup obeys C-adjoint C=3I and defines a rank-27 projector",
         cup.T * cup == 3 * sp.eye(27)
         and cup_projector * cup_projector == cup_projector
         and cup_projector.rank() == 27),
        ("the bridge is O(3)-equivariant and symmetric",
         delta * data["casimir3"] == data["casimir3"] * delta
         and delta == delta.T),
        ("the bridge is scalar on every V3 total-spin copy",
         all(residual == sp.zeros(27)
             for residual in data["central_residuals"].values())),
        ("the direct 3^5 carrier calculation equals all four closed formulas",
         all(sp.factor(data["direct_scalars"][spin] - formulas[spin]) == 0
             for spin in range(4))),
        ("the identity crossing has zero defect through first order",
         all(sp.factor(data["formulas"][spin].subs(identity)) == 0
             for spin in range(4))
         and all(value == 0 for value in identity_gradients)),
        ("the disclosed rational sample has three nonzero higher-spin defects",
         sample_actual == sample_expected),
        ("the defect is not positive and therefore is not a Gram norm",
         sample_actual[1] > 0 and sample_actual[2] < 0 and sample_actual[3] < 0),
        ("scope remains a cup-compression lemma separate from physical Q and the full response",
         scope_ok and axiom_ok),
    )
    return data, sample_actual, checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-suite", action="store_true")
    arguments = parser.parse_args()
    if arguments.mutation_suite:
        rejected = 0
        for mutation in MUTATIONS:
            _data, _sample, checks = exact_checks(mutation)
            survived = all(passed for _label, passed in checks)
            print(f"[{'FAIL' if survived else 'PASS'}] mutation rejected: {mutation}")
            rejected += int(not survived)
        print(f"MUTATIONS: rejected={rejected} total={len(MUTATIONS)}")
        return int(rejected != len(MUTATIONS))

    data, sample, checks = exact_checks(arguments.mutation)
    print(f"audit_timeout_sec: {AUDIT_TIMEOUT_SEC}")
    print(f"R4_Casimir_polynomial: {data['polynomial']}")
    for spin, value in enumerate(sample):
        print(f"Delta4[J={spin}]={value}")
    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
