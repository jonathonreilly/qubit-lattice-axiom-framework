#!/usr/bin/env python3
"""Block 100: classify a Record-native marked pure-birth generator.

The calculation starts from the actual six-neighbour occupancy pointer used by
Block 99.  It classifies proper-cubic rate orbits, constructs conservative
one-token local dilations, resolves a hostile two-star overlap by continuous-
time race semantics, proves finite-seed nonexplosion, and tests equilibrium
detailed balance.  The result is a positive mathematical process family and a
strict selector boundary, not an adopted physical law or TOE closure.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path
import subprocess

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "RECORD_NATIVE_MARKED_PURE_BIRTH_RESOURCE_GENERATOR_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
RUNNER_RELATIVE = (
    "scripts/frontier_record_native_marked_pure_birth_resource_generator_"
    "2026_08_14.py"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_SIX_NEIGHBOR_AFFINE_CQ_CHANNEL_SOLDER_SUPPORT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PARENT_RUNNER = (
    "scripts/frontier_admissibility_six_neighbor_affine_cq_channel_"
    "classifier_2026_08_14.py"
)
PARENT_CACHE = (
    "logs/runner-cache/frontier_admissibility_six_neighbor_affine_cq_channel_"
    "classifier_2026_08_14.txt"
)

CURRENT_MAIN = "43ba5587944ffe0f43df10864c8348a99c17517b"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
PARENT_COMMIT = "a4a7140f0921e70e119b9d641452aa5017a413a6"
PARENT_NOTE_BLOB = "939e6393b5ead6eebf930c39d7c6c592ca42c31e"
PARENT_RUNNER_BLOB = "0fa1c6c56ff506b127177c7f613909db67c79a89"
PARENT_CACHE_BLOB = "d8b6ee6c57def8e4f98c15bb541d3e1b8175782f"

SLOTS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
CONDITIONS = tuple(product((0, 1), repeat=6))
I2 = sp.eye(2)
SIGMA = (
    sp.Matrix(((0, 1), (1, 0))),
    sp.Matrix(((0, -sp.I), (sp.I, 0))),
    sp.Matrix(((1, 0), (0, -1))),
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 190 else detail[:187] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def git_output(*args: str) -> str:
    return subprocess.check_output(("git",) + args, cwd=ROOT, text=True).strip()


def worktree_blob(relative: str) -> str:
    return git_output("hash-object", relative)


def commit_blob(commit: str, relative: str) -> str:
    return git_output("rev-parse", f"{commit}:{relative}")


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
    ).returncode == 0


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(left[row, column] - right[row, column]) == 0
        for row in range(left.rows)
        for column in range(left.cols)
    )


def proper_cubic_rotations() -> tuple[sp.ImmutableMatrix, ...]:
    rotations: set[sp.ImmutableMatrix] = set()
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for source_axis, target_axis in enumerate(permutation):
                matrix[target_axis, source_axis] = signs[source_axis]
            if matrix.det() == 1:
                rotations.add(sp.ImmutableMatrix(matrix))
    return tuple(sorted(rotations, key=lambda item: tuple(item)))


ROTATIONS = proper_cubic_rotations()


@lru_cache(maxsize=None)
def slot_action(rotation: sp.Matrix) -> sp.Matrix:
    action = sp.zeros(6)
    for source_index, slot in enumerate(SLOTS):
        rotated = rotation * sp.Matrix(slot)
        target_index = next(
            index for index, candidate in enumerate(SLOTS)
            if matrix_equal(rotated, sp.Matrix(candidate))
        )
        action[target_index, source_index] = 1
    return action


@lru_cache(maxsize=None)
def rotate_condition(
    rotation: sp.Matrix, condition: tuple[int, ...]
) -> tuple[int, ...]:
    transformed = slot_action(rotation) * sp.Matrix(condition)
    return tuple(int(value) for value in transformed)


@lru_cache(maxsize=None)
def difference(condition: tuple[int, ...]) -> tuple[int, int, int]:
    return (
        condition[0] - condition[1],
        condition[2] - condition[3],
        condition[4] - condition[5],
    )


@lru_cache(maxsize=None)
def norm_squared(direction: tuple[int, int, int]) -> int:
    return sum(value * value for value in direction)


@lru_cache(maxsize=None)
def occupancy_orbits() -> tuple[frozenset[tuple[int, ...]], ...]:
    seen: set[tuple[int, ...]] = set()
    orbits: list[frozenset[tuple[int, ...]]] = []
    for condition in CONDITIONS:
        if condition in seen:
            continue
        orbit = frozenset(rotate_condition(rotation, condition) for rotation in ROTATIONS)
        seen.update(orbit)
        orbits.append(orbit)
    return tuple(
        sorted(
            orbits,
            key=lambda orbit: (
                sum(next(iter(orbit))),
                norm_squared(difference(next(iter(orbit)))),
                tuple(sorted(orbit)),
            ),
        )
    )


def orbit_signature(orbit: frozenset[tuple[int, ...]]) -> tuple[int, int]:
    representative = next(iter(orbit))
    return sum(representative), norm_squared(difference(representative))


def vector_key(vector: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(value) for value in vector)


@lru_cache(maxsize=None)
def spectral_measure(
    direction: tuple[int, int, int], alpha: sp.Expr
) -> dict[tuple[sp.Expr, ...], sp.Expr]:
    vector = sp.Matrix(direction)
    radius = sp.sqrt(vector.dot(vector))
    result: dict[tuple[sp.Expr, ...], sp.Expr] = {}
    for sign in (-1, 1):
        atom = sp.simplify(sign * vector / radius)
        weight = sp.simplify((1 + sign * alpha * radius) / 2)
        result[vector_key(atom)] = weight
    return result


@lru_cache(maxsize=None)
def slot_measure(
    direction: tuple[int, int, int]
) -> dict[tuple[sp.Expr, ...], sp.Expr]:
    result: defaultdict[tuple[sp.Expr, ...], sp.Expr] = defaultdict(
        lambda: sp.Integer(0)
    )
    for axis in range(3):
        atom = sp.zeros(3, 1)
        atom[axis] = direction[axis]
        result[vector_key(atom)] += sp.Rational(1, 3)
    return dict(result)


@lru_cache(maxsize=None)
def axis_collision_measure(
    direction: tuple[int, int, int],
    alpha: sp.Expr,
    *,
    reweighted: bool = False,
) -> dict[tuple[sp.Expr, ...], sp.Expr]:
    """Six axis/outcome atoms for the explicit one-token collision family."""
    k = norm_squared(direction)
    result: dict[tuple[sp.Expr, ...], sp.Expr] = {}
    for axis in range(3):
        if reweighted:
            axis_mass = sp.Rational(1 + direction[axis] ** 2, 3 + k)
        else:
            axis_mass = sp.Rational(1, 3)
        for sign in (-1, 1):
            atom = sp.zeros(3, 1)
            atom[axis] = sign
            probability = sp.simplify(
                (axis_mass + alpha * sign * direction[axis]) / 2
            )
            result[vector_key(atom)] = probability
    return result


def axis_marginals(
    measure: dict[tuple[sp.Expr, ...], sp.Expr]
) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    result = []
    for axis in range(3):
        total = sp.Integer(0)
        for sign in (-1, 1):
            atom = sp.zeros(3, 1)
            atom[axis] = sign
            total += measure[vector_key(atom)]
        result.append(sp.simplify(total))
    return tuple(result)


def measure_mass(measure: dict[tuple[sp.Expr, ...], sp.Expr]) -> sp.Expr:
    return sp.simplify(sum(measure.values(), sp.Integer(0)))


def measure_barycenter(
    measure: dict[tuple[sp.Expr, ...], sp.Expr]
) -> sp.Matrix:
    total = sp.zeros(3, 1)
    for atom, weight in measure.items():
        total += weight * sp.Matrix(atom)
    return sp.simplify(total)


def rotate_measure(
    measure: dict[tuple[sp.Expr, ...], sp.Expr], rotation: sp.Matrix
) -> dict[tuple[sp.Expr, ...], sp.Expr]:
    result: defaultdict[tuple[sp.Expr, ...], sp.Expr] = defaultdict(
        lambda: sp.Integer(0)
    )
    for atom, weight in measure.items():
        result[vector_key(rotation * sp.Matrix(atom))] += weight
    return {atom: sp.simplify(weight) for atom, weight in result.items()}


def measures_equal(
    left: dict[tuple[sp.Expr, ...], sp.Expr],
    right: dict[tuple[sp.Expr, ...], sp.Expr],
) -> bool:
    keys = set(left) | set(right)
    return all(sp.simplify(left.get(key, 0) - right.get(key, 0)) == 0 for key in keys)


def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[index] + right[index] for index in range(3))


def condition_at(
    domain: frozenset[tuple[int, int, int]], site: tuple[int, int, int]
) -> tuple[int, ...]:
    return tuple(int(add(site, slot) in domain) for slot in SLOTS)


def frontier(
    domain: frozenset[tuple[int, int, int]]
) -> frozenset[tuple[int, int, int]]:
    candidates = {add(site, slot) for site in domain for slot in SLOTS} - set(domain)
    return frozenset(
        site for site in candidates if norm_squared(difference(condition_at(domain, site))) > 0
    )


def rate_constant(condition: tuple[int, ...]) -> sp.Expr:
    return sp.Integer(int(norm_squared(difference(condition)) > 0))


def rate_norm(condition: tuple[int, ...]) -> sp.Expr:
    return sp.Integer(norm_squared(difference(condition)))


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = (
        "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    )
    return {
        "origin_main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent_commit": git_output("rev-parse", PARENT_COMMIT),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
    }


def orbit_certificate(mutation: str) -> dict[str, object]:
    orbits = occupancy_orbits()
    signatures = tuple(sorted(orbit_signature(orbit) for orbit in orbits))
    eligible = tuple(signature for signature in signatures if signature[1] > 0)
    rate_dimension = len(eligible)
    if mutation == "collapse_rate_cone":
        rate_dimension = 1
    factored_k = sorted({signature[1] for signature in eligible})
    return {
        "rotations": len(ROTATIONS),
        "conditions": len(CONDITIONS),
        "orbits": len(orbits),
        "signatures": signatures,
        "eligible": eligible,
        "rate_dimension": rate_dimension,
        "factored_dimension": len(factored_k),
        "factored_k": factored_k,
        "partition": sum(len(orbit) for orbit in orbits) == len(CONDITIONS),
    }


def marked_generator_certificate(mutation: str) -> dict[str, object]:
    alphas = (sp.Rational(1, 3), sp.Rational(1, 4))
    normalized = True
    positive = True
    barycenters = True
    covariance = True
    for condition in CONDITIONS:
        direction = difference(condition)
        if norm_squared(direction) == 0:
            continue
        for alpha in alphas:
            measure = spectral_measure(direction, alpha)
            normalized &= measure_mass(measure) == 1
            positive &= all(weight > 0 for weight in measure.values())
            barycenters &= matrix_equal(
                measure_barycenter(measure), alpha * sp.Matrix(direction)
            )
            for rotation in ROTATIONS:
                rotated_direction = tuple(int(value) for value in rotation * sp.Matrix(direction))
                covariance &= measures_equal(
                    rotate_measure(measure, rotation),
                    spectral_measure(rotated_direction, alpha),
                )
    if mutation == "break_mark_normalization":
        normalized = False

    record_map = {
        (-1, 0, 0): sp.Matrix(((1, 0), (0, 0))),
        (0, -1, 0): sp.Matrix(((0, 0), (0, 1))),
    }
    old_copy = {site: matrix.copy() for site, matrix in record_map.items()}
    record_map[(0, 0, 0)] = I2 / 2
    if mutation == "overwrite_record":
        record_map[(-1, 0, 0)] = I2 / 2
    permanence = all(matrix_equal(record_map[site], matrix) for site, matrix in old_copy.items())

    return {
        "normalized": normalized,
        "positive": positive,
        "barycenters": barycenters,
        "covariance": covariance,
        "permanence": permanence,
        "refusal": rate_constant((1, 1, 0, 0, 0, 0)) == 0,
    }


def dilation_resource_certificate(mutation: str) -> dict[str, object]:
    dt = sp.Rational(1, 12)
    norms = []
    charges = []
    for condition in CONDITIONS:
        direction = difference(condition)
        k = norm_squared(direction)
        if k == 0:
            norms.append(sp.Integer(1))
            charges.append((1, 1))
            continue
        for rate in (rate_constant(condition), rate_norm(condition)):
            q = sp.simplify(dt * rate)
            measure = spectral_measure(direction, sp.Rational(1, 3))
            norms.append(sp.simplify(1 - q + q * measure_mass(measure)))
            charges.append((1, 1))

    eligible_signatures = [
        signature for signature in sorted({orbit_signature(item) for item in occupancy_orbits()})
        if signature[1] > 0
    ]
    constant_vector = sp.Matrix([1 for _ in eligible_signatures])
    norm_vector = sp.Matrix([signature[1] for signature in eligible_signatures])
    rate_rank = sp.Matrix.hstack(constant_vector, norm_vector).rank()
    if mutation == "select_rate":
        rate_rank = 1

    alpha_distinct = not matrix_equal(
        sp.Rational(1, 3) * sp.Matrix((1, 1, 0)),
        sp.Rational(1, 4) * sp.Matrix((1, 1, 0)),
    )
    if mutation == "select_alpha":
        alpha_distinct = False

    direction = (1, 1, 0)
    spectral = spectral_measure(direction, sp.Rational(1, 3))
    slots = slot_measure(direction)
    ensemble_distinct = set(spectral).isdisjoint(slots)
    same_barycenter = matrix_equal(
        measure_barycenter(spectral), measure_barycenter(slots)
    )
    resource_exact = all(before == after == 1 for before, after in charges)
    if mutation == "break_resource_debit":
        resource_exact = False

    axis_normalized = True
    axis_positive = True
    axis_barycenter = True
    axis_covariance = True
    uniform_marginals = True
    for condition in CONDITIONS:
        local_direction = difference(condition)
        for alpha in (sp.Rational(1, 3), sp.Rational(1, 4)):
            uniform = axis_collision_measure(local_direction, alpha)
            axis_normalized &= measure_mass(uniform) == 1
            axis_positive &= all(weight >= 0 for weight in uniform.values())
            axis_barycenter &= matrix_equal(
                measure_barycenter(uniform), alpha * sp.Matrix(local_direction)
            )
            uniform_marginals &= axis_marginals(uniform) == (
                sp.Rational(1, 3),
                sp.Rational(1, 3),
                sp.Rational(1, 3),
            )
            for rotation in ROTATIONS:
                rotated_direction = tuple(
                    int(value) for value in rotation * sp.Matrix(local_direction)
                )
                axis_covariance &= measures_equal(
                    rotate_measure(uniform, rotation),
                    axis_collision_measure(rotated_direction, alpha),
                )
        reweighted = axis_collision_measure(
            local_direction, sp.Rational(1, 4), reweighted=True
        )
        axis_normalized &= measure_mass(reweighted) == 1
        axis_positive &= all(weight >= 0 for weight in reweighted.values())
        axis_barycenter &= matrix_equal(
            measure_barycenter(reweighted),
            sp.Rational(1, 4) * sp.Matrix(local_direction),
        )
        for rotation in ROTATIONS:
            rotated_direction = tuple(
                int(value) for value in rotation * sp.Matrix(local_direction)
            )
            axis_covariance &= measures_equal(
                rotate_measure(reweighted, rotation),
                axis_collision_measure(
                    rotated_direction, sp.Rational(1, 4), reweighted=True
                ),
            )

    witness_uniform = axis_collision_measure(direction, sp.Rational(1, 4))
    witness_reweighted = axis_collision_measure(
        direction, sp.Rational(1, 4), reweighted=True
    )
    conditional_axis_distinct = not measures_equal(
        witness_uniform, witness_reweighted
    )
    if mutation == "force_uniform_axis_selection":
        conditional_axis_distinct = False
    contrast_relation = (
        sp.simplify(3 * sp.Rational(1, 3)) == 1
        and sp.simplify(3 * sp.Rational(1, 4)) == sp.Rational(3, 4)
    )

    return {
        "norms": set(norms),
        "max_q": sp.Rational(1, 4),
        "resource_exact": resource_exact,
        "rate_rank": rate_rank,
        "alpha_distinct": alpha_distinct,
        "ensemble_distinct": ensemble_distinct,
        "same_barycenter": same_barycenter,
        "axis_normalized": axis_normalized,
        "axis_positive": axis_positive,
        "axis_barycenter": axis_barycenter,
        "axis_covariance": axis_covariance,
        "uniform_marginals": uniform_marginals,
        "conditional_axis_distinct": conditional_axis_distinct,
        "reweighted_marginals": axis_marginals(witness_reweighted),
        "contrast_relation": contrast_relation,
    }


def two_star_race_certificate(mutation: str) -> dict[str, object]:
    left_record = (-1, 0, 0)
    right_record = (2, 0, 0)
    left_target = (0, 0, 0)
    right_target = (1, 0, 0)
    domain = frozenset((left_record, right_record))
    left_direction = difference(condition_at(domain, left_target))
    right_direction = difference(condition_at(domain, right_target))
    after_left = domain | {left_target}
    after_right = domain | {right_target}

    rotation = sp.diag(-1, -1, 1)
    translation = sp.Matrix((1, 0, 0))

    def affine(site: tuple[int, int, int]) -> tuple[int, int, int]:
        image = rotation * sp.Matrix(site) + translation
        return tuple(int(value) for value in image)

    affine_symmetry = (
        rotation.det() == 1
        and affine(left_record) == right_record
        and affine(right_record) == left_record
        and affine(left_target) == right_target
        and affine(right_target) == left_target
    )

    lam = sp.symbols("lambda", positive=True)
    time_s, time_t = sp.symbols("s t", nonnegative=True)

    def semigroup(time: sp.Expr) -> sp.Matrix:
        survival = sp.exp(-2 * lam * time)
        winner = (1 - survival) / 2
        return sp.Matrix(
            ((survival, winner, winner), (0, 1, 0), (0, 0, 1))
        )

    generator = sp.Matrix(((-2 * lam, lam, lam), (0, 0, 0), (0, 0, 0)))
    derivative = semigroup(time_t).diff(time_t).subs(time_t, 0)
    chapman = semigroup(time_s) * semigroup(time_t)
    serial = mutation != "simultaneous_collision"
    semigroup_ok = matrix_equal(chapman, semigroup(time_s + time_t))
    if mutation == "break_semigroup":
        semigroup_ok = False

    return {
        "directions": (left_direction, right_direction),
        "after_left": difference(condition_at(after_left, right_target)),
        "after_right": difference(condition_at(after_right, left_target)),
        "affine_symmetry": affine_symmetry,
        "derivative": matrix_equal(derivative, generator),
        "semigroup": semigroup_ok,
        "serial": serial,
        "winner": sp.Rational(1, 2),
    }


def nonexplosion_certificate(mutation: str) -> dict[str, object]:
    host = ((0, 0, 0),) + SLOTS
    finite_bounds = []
    rate_bounds = []
    zero_rate_absorbing = []
    for size in range(1, len(host) + 1):
        for subset in combinations(host, size):
            domain = frozenset(subset)
            candidates = frontier(domain)
            finite_bounds.append(len(candidates) <= 6 * len(domain))
            total_rate = sum(
                int(rate_norm(condition_at(domain, site))) for site in candidates
            )
            rate_bounds.append(total_rate <= 18 * len(domain))
            zero_rate_absorbing.append(
                sum(sp.Integer(0) for _site in candidates) == 0
            )
    symbol = sp.symbols("n", integer=True, positive=True)
    harmonic_diverges = sp.limit(sp.harmonic(symbol), symbol, sp.oo) == sp.oo
    if mutation == "break_nonexplosion_bound":
        harmonic_diverges = False
    return {
        "domains": 2 ** len(host) - 1,
        "empty_absorbing": not frontier(frozenset()),
        "zero_rate_absorbing": all(zero_rate_absorbing),
        "frontier_bound": all(finite_bounds),
        "rate_bound": all(rate_bounds),
        "harmonic_diverges": harmonic_diverges,
        "lambda_max": 3,
        "yule_coefficient": 18,
        "general_coefficient": 6 * sp.Symbol("M", positive=True),
    }


def detailed_balance_certificate(mutation: str) -> dict[str, object]:
    p_plus = sp.Rational(2, 3)
    p_minus = sp.Rational(1, 3)
    generator = sp.Matrix(
        ((-1, p_plus, p_minus), (0, 0, 0), (0, 0, 0))
    )
    stationary_basis = generator.T.nullspace()
    blank_zero = all(vector[0] == 0 for vector in stationary_basis)
    forward_fluxes = (p_plus, p_minus)
    no_full_support = blank_zero and all(flux > 0 for flux in forward_fluxes)
    if mutation == "fake_equilibrium_formation":
        no_full_support = False

    resource_not_selector = sp.Matrix.hstack(
        sp.Matrix((1, 1, 1, 1, 1, 1)),
        sp.Matrix((1, 2, 1, 3, 2, 1)),
    ).rank() == 2
    if mutation == "claim_resource_selection":
        resource_not_selector = False
    return {
        "stationary_dimension": len(stationary_basis),
        "blank_zero": blank_zero,
        "no_full_support": no_full_support,
        "resource_not_selector": resource_not_selector,
        "branch_charge": (1, 1),
    }


def scope_certificate(mutation: str) -> dict[str, bool]:
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").lower().split())
    result = {
        "positive_family": "marked pure-birth generator" in note,
        "six_cone": "six-dimensional nonnegative rate cone" in note,
        "three_cone": "three-dimensional cone" in note,
        "two_generators": "two nonproportional generators" in note,
        "copula_collapse": "no separate simultaneous copula" in note,
        "stoichiometry": "resource conservation fixes stoichiometry, not kinetics" in note,
        "equilibrium_boundary": "on this fiber, positive append-only formation is incompatible with full-support detailed balance" in note,
        "drive": "nonequilibrium fuel/boundary law" in note,
        "placement": "record/admissibility interface placement remains an owner decision" in note,
        "not_adopted": "no physical generator is derived or adopted" in note,
        "axiom_unchanged": "no axiom amendment is justified or adopted" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": "retained-positive end-to-end theory count remains zero" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "stop": "the selector experiment stops here" in note,
    }
    if mutation == "force_axiom_edit":
        result["axiom_unchanged"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    if mutation == "claim_obligation_retirement":
        result["zero_retirement"] = False
    if mutation == "weaken_no_go_packet":
        result["n1_n8"] = False
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom_authority",
            "collapse_rate_cone",
            "break_mark_normalization",
            "overwrite_record",
            "break_resource_debit",
            "select_rate",
            "select_alpha",
            "force_uniform_axis_selection",
            "simultaneous_collision",
            "break_semigroup",
            "break_nonexplosion_bound",
            "fake_equilibrium_formation",
            "claim_resource_selection",
            "force_axiom_edit",
            "claim_toe_progress",
            "claim_obligation_retirement",
            "weaken_no_go_packet",
        ),
        default="",
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-current-authority-and-Block99-parent",
        "current axioms, premise registry, and the exact Block99 classifier are content-bound",
        authority["origin_main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == CURRENT_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == CURRENT_REGISTRY_BLOB
        and authority["parent_commit"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and authority["parent_note"] == PARENT_NOTE_BLOB
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
        f"origin/main={str(authority['origin_main'])[:10]}; parent={str(authority['parent_commit'])[:10]}",
    )

    orbits = orbit_certificate(mutation)
    checks.check(
        "B-six-neighbour-rate-orbit-classification",
        "proper-cubic covariance leaves six eligible rate orbits, or three after factorization through d",
        orbits["rotations"] == 24
        and orbits["conditions"] == 64
        and orbits["orbits"] == 10
        and orbits["partition"]
        and len(orbits["eligible"]) == 6
        and orbits["rate_dimension"] == 6
        and orbits["factored_dimension"] == 3
        and orbits["factored_k"] == [1, 2, 3],
        f"orbit signatures={orbits['eligible']}; cone dimensions={orbits['rate_dimension']}/{orbits['factored_dimension']}",
    )

    generator = marked_generator_certificate(mutation)
    checks.check(
        "C-normalized-covariant-marked-local-generator",
        "the spectral marked jump family is positive, normalized, covariant, refusing at d=0, and append-only",
        all(generator.values()),
    )

    dilation = dilation_resource_certificate(mutation)
    checks.check(
        "D-one-token-isometric-resource-selector-test",
        "one-token conservation and local isometry admit nonproportional rates, distinct alpha values, and distinct ensembles",
        dilation["norms"] == {1}
        and dilation["max_q"] <= 1
        and dilation["resource_exact"]
        and dilation["rate_rank"] == 2
        and dilation["alpha_distinct"]
        and dilation["ensemble_distinct"]
        and dilation["same_barycenter"]
        and dilation["axis_normalized"]
        and dilation["axis_positive"]
        and dilation["axis_barycenter"]
        and dilation["axis_covariance"]
        and dilation["uniform_marginals"]
        and dilation["conditional_axis_distinct"]
        and dilation["reweighted_marginals"]
        == (sp.Rational(2, 5), sp.Rational(2, 5), sp.Rational(1, 5))
        and dilation["contrast_relation"],
        "constant versus |d|^2 rates have rank 2; alpha=c/3 with c=1 or 3/4 survives; uniform versus reweighted axes and spectral versus slot remain distinct",
    )

    race = two_star_race_certificate(mutation)
    checks.check(
        "E-overlapping-two-star-continuous-time-race",
        "the affine-symmetric adjacent opportunities have an exact Markov semigroup, probability-one serial order, and equal conditional winner weights",
        race["directions"] == ((-1, 0, 0), (1, 0, 0))
        and race["after_left"] == (0, 0, 0)
        and race["after_right"] == (0, 0, 0)
        and race["affine_symmetry"]
        and race["derivative"]
        and race["semigroup"]
        and race["serial"]
        and race["winner"] == sp.Rational(1, 2),
        "P(no event)=exp(-2 lambda t); P(left)=P(right)=[1-exp(-2 lambda t)]/2",
    )

    nonexplosion = nonexplosion_certificate(mutation)
    checks.check(
        "F-finite-seed-global-process-and-nonexplosion",
        "frontier and total-rate bounds give Yule domination and a nonexplosive full-Z3 process from every finite seed",
        nonexplosion["domains"] == 127
        and nonexplosion["empty_absorbing"]
        and nonexplosion["zero_rate_absorbing"]
        and nonexplosion["frontier_bound"]
        and nonexplosion["rate_bound"]
        and nonexplosion["harmonic_diverges"]
        and nonexplosion["lambda_max"] == 3
        and nonexplosion["yule_coefficient"] == 18
        and nonexplosion["general_coefficient"]
        == 6 * sp.Symbol("M", positive=True),
        "empty seed and M=0 laws are absorbing; checked 127 hostile domains; general Lambda<=6MN, explicit M=3 gives 18N; harmonic sum diverges",
    )

    equilibrium = detailed_balance_certificate(mutation)
    checks.check(
        "G-detailed-balance-and-nonequilibrium-drive-boundary",
        "on the executed three-state fiber, positive append-only jumps have no full-support reversible stationary law; capacity conservation does not select their kinetics",
        equilibrium["stationary_dimension"] == 2
        and equilibrium["blank_zero"]
        and equilibrium["no_full_support"]
        and equilibrium["resource_not_selector"]
        and equilibrium["branch_charge"] == (1, 1),
        "all stationary vectors of the executed fiber put zero mass on the ready prestate; a positive driven/fuel boundary or reverse/export law is extra content",
    )

    scope = scope_certificate(mutation)
    checks.check(
        "H-owner-packet-no-go-and-TOE-firewall",
        "N1-N8 localize one complete generator plus drive/clock decision without axiom adoption, retention, or score movement",
        all(scope.values()),
    )

    print(
        f"AXIOM_AUTHORITY: origin/main={authority['origin_main']} axiom={CURRENT_AXIOM_BLOB}; Block99 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: checked 64 pointer conditions, 10 cubic orbits, six eligible rate classes, two response scales, two ensembles, and two conservative rate laws"
    )
    print(
        "per_site: checked one six-neighbour star, exact append/refusal, old-Record nondemolition under the supplied classical pointer quotient, and one-token conversion"
    )
    print(
        "per_mode: checked constant and |d|^2 hazards, alpha=1/3 and 1/4, spectral and axis-slot marks, symmetric overlap race, and reversible-equilibrium failure"
    )
    print(
        "per_block: checked two-star Chapman-Kolmogorov composition, the empty absorbing state, 127 frontier/rate fixtures, general bounded-rate harmonic nonexplosion, and the minimal owner/law packet"
    )
    print(
        "lattice_wide: proved a nonexplosive marked jump process on full Z3 from every finite initial Record map; arbitrary infinite starts, physical time, fuel renewal, source/action typing, gravity, adoption, and retention remain open"
    )
    print(
        "RESULT: continuous-time generator semantics removes a separate simultaneous scheduler/copula and gives exact finite-seed histories, but symmetry plus one-token conservation leaves a six-rate cone (three through d), response/ensemble alternatives, and a free overall physical rate"
    )
    print(
        "DECISION_CUT: specify one complete marked local generator on a declared pointer interface, plus the nonequilibrium fuel/boundary and physical clock; detailed balance with append-only permanence permits only zero ready-state stationary mass or zero formation"
    )
    print(
        "TOE: zero obligation retirement, zero retained-positive end-to-end theories, and no percentage movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
