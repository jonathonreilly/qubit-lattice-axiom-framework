#!/usr/bin/env python3
"""
Finite supplied-sample rescope of the historical DM/PMNS sole-axiom note.

What this runner proves:
  1. On the explicitly supplied two-point sample set, the exact mean-seed map
     is non-injective: two unequal samples have the same seed pair.
  2. The exact five-coordinate seed-relative encoding distinguishes and
     reconstructs those samples.
  3. Conditional on a separately supplied matrix construction, a
     permutation/rephasing-invariant numerical spectral diagnostic differs
     between the two samples.

What this runner does not prove:
  - that either sample is admitted by the current four framework axioms;
  - that Cl(3) on Z^3 supplies a physical PMNS carrier or source family;
  - a transport law, transport constants, flavor-column selector, eta target,
    or physical eta readout.
"""

from __future__ import annotations

import argparse
import ast
import sys
from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
from pathlib import Path

import numpy as np


SOURCE_PATH = Path(__file__).resolve()

PASS_COUNT = 0
FAIL_COUNT = 0

Q = Fraction
Vector3Q = tuple[Fraction, Fraction, Fraction]
Source5Q = tuple[Fraction, Fraction, Fraction, Fraction, Fraction]


@dataclass(frozen=True)
class SuppliedSample:
    x: Vector3Q
    y: Vector3Q
    delta: Fraction


SAMPLE_A = SuppliedSample(
    x=(Q(115, 100), Q(82, 100), Q(95, 100)),
    y=(Q(41, 100), Q(28, 100), Q(54, 100)),
    delta=Q(63, 100),
)
SAMPLE_B = SuppliedSample(
    x=(Q(105, 100), Q(97, 100), Q(90, 100)),
    y=(Q(60, 100), Q(9, 100), Q(54, 100)),
    delta=Q(63, 100),
)

CYCLE = np.array(
    [
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [1.0, 0.0, 0.0],
    ],
    dtype=complex,
)

FORBIDDEN_PHYSICAL_ETA_NAMES = {
    "ETA_OBS",
    "ETA_NE_CANONICAL",
    "ETA_NE_SEED",
}
FORBIDDEN_PHYSICAL_ETA_NUMBER_LITERALS = {
    "6.12e-10",
    "0.7190825360613422",
    "0.9895125971972334",
}


def check(category: str, name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if bool(condition) else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status} ({category})] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return bool(condition)


def mean3(values: Vector3Q) -> Fraction:
    return sum(values, Q(0, 1)) / 3


def seed_map(sample: SuppliedSample) -> tuple[Fraction, Fraction]:
    return mean3(sample.x), mean3(sample.y)


def source_map(sample: SuppliedSample) -> Source5Q:
    xbar, ybar = seed_map(sample)
    return (
        sample.x[0] - xbar,
        sample.x[1] - xbar,
        sample.y[0] - ybar,
        sample.y[1] - ybar,
        sample.delta,
    )


def reconstruct_from_seed_and_source(
    seed: tuple[Fraction, Fraction], source: Source5Q
) -> SuppliedSample:
    xbar, ybar = seed
    xi1, xi2, eta1, eta2, delta = source
    return SuppliedSample(
        x=(xbar + xi1, xbar + xi2, xbar - xi1 - xi2),
        y=(ybar + eta1, ybar + eta2, ybar - eta1 - eta2),
        delta=delta,
    )


def permute_sample(sample: SuppliedSample, permutation: tuple[int, int, int]) -> SuppliedSample:
    return SuppliedSample(
        x=tuple(sample.x[i] for i in permutation),
        y=tuple(sample.y[i] for i in permutation),
        delta=sample.delta,
    )


def equivalent_by_simultaneous_permutation(a: SuppliedSample, b: SuppliedSample) -> bool:
    return any(permute_sample(a, p) == b for p in permutations(range(3)))


def finite_sample_nonuniqueness_predicate(a: SuppliedSample, b: SuppliedSample) -> bool:
    return (
        a != b
        and seed_map(a) == seed_map(b)
        and source_map(a) != source_map(b)
        and not equivalent_by_simultaneous_permutation(a, b)
    )


def shifted_seed_same_source(sample: SuppliedSample) -> SuppliedSample:
    return SuppliedSample(
        x=tuple(value + Q(1, 10) for value in sample.x),
        y=tuple(value + Q(1, 20) for value in sample.y),
        delta=sample.delta,
    )


def supplied_carrier_matrix(sample: SuppliedSample) -> np.ndarray:
    """
    A supplied numerical construction, not an axiom-derived physical carrier.
    """
    x = np.array([float(value) for value in sample.x], dtype=float)
    y = np.array([float(value) for value in sample.y], dtype=complex)
    y[2] *= np.exp(1j * float(sample.delta))
    return np.diag(x.astype(complex)) + np.diag(y) @ CYCLE


def spectral_signature_from_matrix(carrier: np.ndarray) -> np.ndarray:
    hermitian = carrier @ carrier.conj().T
    eigenvalues = np.linalg.eigvalsh(hermitian)
    trace = float(np.sum(eigenvalues))
    if not np.isfinite(trace) or trace <= 0.0:
        raise ValueError("supplied spectral diagnostic needs positive finite trace")
    return np.asarray(eigenvalues / trace, dtype=float)


def supplied_spectral_signature(sample: SuppliedSample) -> np.ndarray:
    return spectral_signature_from_matrix(supplied_carrier_matrix(sample))


def conditional_numerical_map_predicate(a: SuppliedSample, b: SuppliedSample) -> bool:
    return finite_sample_nonuniqueness_predicate(a, b) and (
        np.linalg.norm(supplied_spectral_signature(a) - supplied_spectral_signature(b))
        > 1.0e-8
    )


def imported_module_roots() -> set[str]:
    tree = ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))
    roots: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".", 1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            roots.add(node.module.split(".", 1)[0])
    return roots


def has_literal_true_load_bearing_check() -> bool:
    tree = ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
            continue
        if node.func.id != "check":
            continue
        condition = node.args[2] if len(node.args) >= 3 else None
        if condition is None:
            condition = next(
                (
                    keyword.value
                    for keyword in node.keywords
                    if keyword.arg == "condition"
                ),
                None,
            )
        if isinstance(condition, ast.Constant) and condition.value is True:
            return True
    return False


def referenced_physical_eta_targets() -> set[str]:
    tree = ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))
    names = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
    hits = {
        name
        for name in names
        if name in FORBIDDEN_PHYSICAL_ETA_NAMES or "best_eta" in name
    }
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Constant)
            and isinstance(node.value, (int, float))
            and repr(float(node.value)) in FORBIDDEN_PHYSICAL_ETA_NUMBER_LITERALS
        ):
            hits.add(repr(node.value))
    return hits


def part0_scope_and_import_firewalls() -> None:
    print("\n" + "=" * 88)
    print("PART 0: IMPORT AND EXECUTABLE FIREWALLS")
    print("=" * 88)

    allowed_import_roots = {
        "__future__",
        "argparse",
        "ast",
        "dataclasses",
        "fractions",
        "itertools",
        "numpy",
        "pathlib",
        "sys",
    }
    imported_roots = imported_module_roots()

    check(
        "B",
        "The repaired runner imports no project-local physics module",
        imported_roots <= allowed_import_roots,
        f"imports={sorted(imported_roots)}",
    )
    check(
        "B",
        "No load-bearing check uses a literal True conclusion",
        not has_literal_true_load_bearing_check(),
    )
    check(
        "B",
        "No former physical eta target name or numeric target is referenced",
        not referenced_physical_eta_targets(),
    )


def part1_exact_finite_sample_seed_map_nonuniqueness() -> None:
    print("\n" + "=" * 88)
    print("PART 1: EXACT FINITE SUPPLIED-SAMPLE SEED-MAP NONUNIQUENESS")
    print("=" * 88)

    seed_a = seed_map(SAMPLE_A)
    seed_b = seed_map(SAMPLE_B)
    source_a = source_map(SAMPLE_A)
    source_b = source_map(SAMPLE_B)

    check(
        "A",
        "Both supplied samples are positive three-coordinate tuples",
        all(value > 0 for value in SAMPLE_A.x + SAMPLE_A.y + SAMPLE_B.x + SAMPLE_B.y),
    )
    check(
        "A",
        "The two supplied samples have exactly equal rational seed pairs",
        seed_a == seed_b == (Q(73, 75), Q(41, 100)),
        f"seed={seed_a}",
    )
    check(
        "A",
        "Their exact five-coordinate seed-relative sources are unequal",
        source_a != source_b,
        f"source_A={source_a}; source_B={source_b}",
    )
    check(
        "A",
        "Seed plus source reconstructs both supplied samples exactly",
        reconstruct_from_seed_and_source(seed_a, source_a) == SAMPLE_A
        and reconstruct_from_seed_and_source(seed_b, source_b) == SAMPLE_B,
    )
    check(
        "A",
        "The witness pair is not a simultaneous coordinate permutation",
        not equivalent_by_simultaneous_permutation(SAMPLE_A, SAMPLE_B),
    )
    check(
        "A",
        "The finite supplied-sample nonuniqueness predicate holds",
        finite_sample_nonuniqueness_predicate(SAMPLE_A, SAMPLE_B),
    )


def part2_hostile_controls() -> None:
    print("\n" + "=" * 88)
    print("PART 2: HOSTILE CONTROLS FOR THE ALGEBRAIC WITNESS")
    print("=" * 88)

    wrong_seed = SuppliedSample(
        x=(SAMPLE_B.x[0] + Q(1, 100), SAMPLE_B.x[1], SAMPLE_B.x[2]),
        y=SAMPLE_B.y,
        delta=SAMPLE_B.delta,
    )
    same_source_wrong_seed = shifted_seed_same_source(SAMPLE_A)
    permuted_a = permute_sample(SAMPLE_A, (1, 2, 0))

    check(
        "A",
        "Wrong-seed control is rejected",
        not finite_sample_nonuniqueness_predicate(SAMPLE_A, wrong_seed),
        f"seeds=({seed_map(SAMPLE_A)},{seed_map(wrong_seed)})",
    )
    check(
        "A",
        "Equal-source duplicate control is rejected",
        not finite_sample_nonuniqueness_predicate(SAMPLE_A, SAMPLE_A),
    )
    check(
        "A",
        "Same-source but shifted-seed control is rejected",
        source_map(same_source_wrong_seed) == source_map(SAMPLE_A)
        and seed_map(same_source_wrong_seed) != seed_map(SAMPLE_A)
        and not finite_sample_nonuniqueness_predicate(SAMPLE_A, same_source_wrong_seed),
    )
    check(
        "A",
        "Pure simultaneous-permutation control is rejected as a relabeling",
        equivalent_by_simultaneous_permutation(SAMPLE_A, permuted_a)
        and not finite_sample_nonuniqueness_predicate(SAMPLE_A, permuted_a),
    )


def part3_conditional_supplied_map_lemma() -> None:
    print("\n" + "=" * 88)
    print("PART 3: CONDITIONAL SUPPLIED NUMERICAL-MAP LEMMA")
    print("=" * 88)

    carrier_a = supplied_carrier_matrix(SAMPLE_A)
    signature_a = spectral_signature_from_matrix(carrier_a)
    signature_b = supplied_spectral_signature(SAMPLE_B)

    permutation = np.array(
        [
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
        ],
        dtype=complex,
    )
    left_rephase = np.diag(np.exp(1j * np.array([0.37, -0.22, 0.91])))
    right_rephase = np.diag(np.exp(1j * np.array([-0.44, 0.19, 0.73])))

    permuted_signature = spectral_signature_from_matrix(
        permutation @ carrier_a @ permutation.conj().T
    )
    rephased_signature = spectral_signature_from_matrix(
        left_rephase @ carrier_a @ right_rephase
    )

    check(
        "D",
        "The supplied spectral diagnostic is finite, ordered, and normalized",
        np.all(np.isfinite(signature_a))
        and np.all(np.diff(signature_a) >= -1.0e-14)
        and abs(float(np.sum(signature_a)) - 1.0) < 1.0e-14,
        f"signature_A={np.round(signature_a, 12)}",
    )
    check(
        "D",
        "The two supplied equal-seed samples have different spectral diagnostics under the supplied map",
        np.linalg.norm(signature_a - signature_b) > 1.0e-8,
        f"distance={np.linalg.norm(signature_a - signature_b):.12f}",
    )
    check(
        "D",
        "Equal-source duplicate gives the same downstream diagnostic",
        np.allclose(signature_a, supplied_spectral_signature(SAMPLE_A), atol=1.0e-14),
    )
    check(
        "D",
        "Basis-permutation control leaves the diagnostic invariant",
        np.allclose(signature_a, permuted_signature, atol=1.0e-14),
    )
    check(
        "D",
        "Left/right rephasing control leaves the diagnostic invariant",
        np.allclose(signature_a, rephased_signature, atol=1.0e-14),
    )
    check(
        "D",
        "The conditional supplied-map nonuniqueness predicate holds",
        conditional_numerical_map_predicate(SAMPLE_A, SAMPLE_B),
        "conditional on the displayed carrier construction only",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--intentional-failure-probe",
        action="store_true",
        help="add one known failing check to verify truthful nonzero exit",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    print("=" * 88)
    print("DM LEPTOGENESIS PMNS SOLE-AXIOM BOUNDARY: FINITE-SAMPLE RESCOPE")
    print("=" * 88)
    print()
    print("Actual current-surface claim:")
    print("  exact nonuniqueness of a mean-seed map on two supplied samples;")
    print("  conditional numerical-map separation under one supplied construction.")
    print("  No axiom-derived active family, transport law, selector, eta target,")
    print("  carrier identification, or physical eta readout is claimed.")

    part0_scope_and_import_firewalls()
    part1_exact_finite_sample_seed_map_nonuniqueness()
    part2_hostile_controls()
    part3_conditional_supplied_map_lemma()

    if args.intentional_failure_probe:
        check(
            "D",
            "Intentional failure probe",
            np.linalg.norm(
                supplied_spectral_signature(SAMPLE_A)
                - supplied_spectral_signature(SAMPLE_A)
            )
            > 1.0,
        )

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Disposition:")
    print("    - support-only demotion from a sole-axiom boundary claim")
    print("    - exact finite supplied-sample seed-map nonuniqueness")
    print("    - conditional supplied numerical-map lemma")
    print("    - active-family admissibility and every physical eta bridge remain open")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
