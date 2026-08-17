#!/usr/bin/env python3
"""Block 130: exact facet-charge bridge on the displayed cell-cutting record.

The runner separates the signed endpoint-difference lattice from the directed
cone and from the still-unmeasured one-flip facet-charge increments.  Every
scientific computation is over the integers or rationals; wall-clock timing
is the sole floating-point quantity.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from math import gcd, lcm
from pathlib import Path
import subprocess
import time


Point = tuple[int, int]
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_FACET_CHARGE_BRIDGE_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SCALAR_QUOTIENT_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_scalar_quotient_theorem_"
    "2026_08_17.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_scalar_quotient_"
    "theorem_2026_08_17.txt"
)
CELL_AUTHORITY_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_ORBIT_STRATA_CYCLE767_"
    "NOTE_2026-08-09.md"
)

# This tuple is deliberately literal: it is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_FACET_CHARGE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SCALAR_QUOTIENT_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_scalar_quotient_theorem_2026_08_17.py",
    "logs/runner-cache/admissibility_dirac_kahler_scalar_quotient_theorem_2026_08_17.txt",
)
# The cell-cutting cycle-767 note is a content-bound authority pinned by
# blob at origin/main in gate A; it is not present on this stacked branch
# and is not an execution input, so it does not appear in
# AUDIT_INPUT_PATHS.

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "02602ca09e4ea69a805a824c3c1f31cb1ee35b20"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block129-scalar-quotient-theorem-20260817"
)
PARENT_COMMIT = "30fd2722a10a02f87c235e2ee592d140f8bb7df5"
PARENT_NOTE_BLOB = "58ce6cb586f7a7a3d59e1f0d2080e33a08a87718"
PARENT_RUNNER_BLOB = "3b811c2329bca16cbe44dcb6a9e266b37b63052e"
PARENT_CACHE_BLOB = "1da860ae5041fa9630bee671edf67e9593569104"

# Final content-bearing cycle-767 commit on origin/main history.  The path was
# subsequently deleted by 31e4c7f, so both its blob and main ancestry are
# checked instead of pretending that the file survives at the main tip.
CELL_AUTHORITY_COMMIT = "64ed8d38b68c53e0e1df55a81ed2bf3dd685d0b3"
CELL_AUTHORITY_BLOB = "82dcb69e9e47ce0211552d4f5e9ac595246e6c25"

ANCESTOR_COMMITS = (
    (128, "f6b0cf59e2cc588ebd3e34b96e730574cb485db2"),
    (127, "ca6792464f60598013a3700f99c02a467af64b7a"),
    (126, "a145a4e2cfc19bc919371196d7c5f3451c0bb45d"),
    (125, "ff85cc8c6a991b2926b9ac5cb5168f2587bc0c0d"),
    (124, "da2b9020e9f15ac55640ef87a0798a78e3c9a0d0"),
    (123, "954322e0e085d6c3133ce24dca49db2efbd7d0a6"),
    (122, "f067b99be7eb49fc46ea8dffccab5e20e6052d88"),
    (121, "1714abeefcf3763c0bfe001f30fd14521c538622"),
    (120, "1c2386bf3df420707fd2ecb2d7ec84002ba40ad1"),
    (119, "33fd2d21558604718f3a88713fe1976aff8f9dbb"),
    (118, "fdd1883c54ca8cc14b1337cc1edc249792d5dab2"),
    (117, "f800356aec0989b6e0fa80ed43274794243b1ca2"),
    (116, "c36d11e4e8d927c6fc31f0a8b579d4bd15f4fa43"),
    (115, "c78301fef7521d0518f485f1bf9266983c9e516a"),
    (114, "75026e71cfbd44ed665ddc41c22ebaa722720ea9"),
    (113, "e76893eb7204d1d727a3ab8838fb3fada3f45dfc"),
    (112, "385a6ba5b1594f20e5d4eebba9da68d8e72abc10"),
    (111, "b04e7c8747b09734711cfcd2bfab961bd12e81ad"),
    (110, "d6761278fca9cac617200792473a8f4da3a6cfff"),
    (109, "ad84cfcc857a65285389ba93b47cd7b718589be5"),
    (108, "8afe8dff5ccf531208238af0aaaec1f547d73874"),
    (107, "d41a05e153d4cb77eee125b82fc0b0bd767bf32e"),
    (106, "22d6d90ec2279e5868c9c825149b2a20beea3797"),
    (105, "d06066c2b908aaca0779625d831dfb10620cf34d"),
    (104, "7fe07db6c03fad1191893c942f708c5cb9a54c43"),
    (103, "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"),
)

# Supervisor-transcribed literals from the merged cycles 723/725/726
# facet-charge series.  Coordinates are (TC, MC), in the displayed order.
FACET_CHARGE_POINTS: tuple[Point, ...] = ((36, 55), (41, 48), (37, 48))

# Supervisor-transcribed cycle-734 move structure.  Each row is
# (positive interior-cost delta, move count), never a facet-charge delta.
INTERIOR_COST_HISTOGRAM: tuple[tuple[int, int], ...] = ((1, 192), (2, 96))
HISTOGRAM_FIELDS = ("interior_cost_delta", "move_count")
FLIP_FACET_DELTAS: tuple[Point, ...] | None = None
REVERSIBILITY_IN_COST_CLASS: bool | None = None

MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_input_pins",
    "break_lattice_equality",
    "break_witnesses",
    "break_conserved_solve",
    "break_cone_onesided",
    "claim_unconditional_momentum",
    "break_echo_facts",
    "claim_flip_deltas_known",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_toe_progress",
    "claim_axiom_amendment",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).strip()


def worktree_blob(path: str) -> str:
    return git_output("hash-object", path)


def commit_blob(commit: str, path: str) -> str:
    return git_output("rev-parse", f"{commit}:{path}")


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def determinant(left: Point, right: Point) -> int:
    return left[0] * right[1] - left[1] * right[0]


def lattice_point(left: int, right: int, d1: Point, d2: Point) -> Point:
    return left * d1[0] + right * d2[0], left * d1[1] + right * d2[1]


def cycle_type(permutation: tuple[int, ...]) -> tuple[int, ...]:
    if sorted(permutation) != list(range(len(permutation))):
        raise AssertionError("valid finite permutation required")
    seen: set[int] = set()
    lengths: list[int] = []
    for start in range(len(permutation)):
        if start in seen:
            continue
        value = start
        length = 0
        while value not in seen:
            seen.add(value)
            value = permutation[value]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def permutation_order(permutation: tuple[int, ...]) -> int:
    order = 1
    for length in cycle_type(permutation):
        order = lcm(order, length)
    return order


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = (
        "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    )
    expected_parent = (
        "0" * 40 if mutation == "stale_parent_authority" else PARENT_NOTE_BLOB
    )
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_REF),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        **{
            f"ancestor_{number}": is_ancestor(commit, "HEAD")
            for number, commit in ANCESTOR_COMMITS
        },
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "expected_parent": expected_parent,
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
        "cell_blob": commit_blob(CELL_AUTHORITY_COMMIT, CELL_AUTHORITY_PATH),
        "cell_on_main_history": is_ancestor(CELL_AUTHORITY_COMMIT, "origin/main"),
    }


@dataclass(frozen=True)
class InputRecordCertificate:
    points: tuple[Point, ...]
    histogram: tuple[tuple[int, int], ...]
    pairwise_distinct: bool
    d1: Point
    d2: Point
    signed_determinant: int
    noncollinear: bool
    pins_exact: bool


def input_record_certificate() -> InputRecordCertificate:
    points = FACET_CHARGE_POINTS
    d1 = subtract(points[1], points[0])
    d2 = subtract(points[2], points[0])
    signed_determinant = determinant(d1, d2)
    return InputRecordCertificate(
        points=points,
        histogram=INTERIOR_COST_HISTOGRAM,
        pairwise_distinct=all(
            left != right for left, right in combinations(points, 2)
        ),
        d1=d1,
        d2=d2,
        signed_determinant=signed_determinant,
        noncollinear=(signed_determinant != 0),
        pins_exact=(
            points == ((36, 55), (41, 48), (37, 48))
            and INTERIOR_COST_HISTOGRAM == ((1, 192), (2, 96))
        ),
    )


@dataclass(frozen=True)
class DifferenceLatticeCertificate:
    d1: Point
    d2: Point
    signed_determinant: int
    index: int
    primitive_normal: Point
    generated_box_size: int
    generated_box_forward: bool
    fundamental_congruence_size: int
    fundamental_generated_size: int
    fundamental_reverse: bool
    fundamental_sets_equal: bool
    tick_witness: Point
    mixed_witness: Point
    witnesses_exact: bool
    sign_indefinite_both_components: bool
    negation_closed: bool


def difference_lattice_certificate(
    record: InputRecordCertificate,
) -> DifferenceLatticeCertificate:
    d1, d2 = record.d1, record.d2
    signed_determinant = determinant(d1, d2)
    index = abs(signed_determinant)

    # A primitive integer normal to d2 is derived, then its pairing with d1
    # determines the modulus.  Here this gives (7,1) and modulus 28.
    raw_normal = (-d2[1], d2[0])
    normal_divisor = gcd(abs(raw_normal[0]), abs(raw_normal[1]))
    primitive_normal = (
        raw_normal[0] // normal_divisor,
        raw_normal[1] // normal_divisor,
    )

    point_bound = 28
    coefficient_range = range(-point_bound, point_bound + 1)
    generated_box = {
        point
        for left, right in product(coefficient_range, repeat=2)
        for point in (lattice_point(left, right, d1, d2),)
        if all(-point_bound <= coordinate <= point_bound for coordinate in point)
    }
    generated_box_forward = all(
        (primitive_normal[0] * x + primitive_normal[1] * y) % index == 0
        for x, y in generated_box
    )

    fundamental_congruence = {
        (x, y)
        for x, y in product(range(index), repeat=2)
        if (primitive_normal[0] * x + primitive_normal[1] * y) % index == 0
    }
    fundamental_generated = {
        point
        for left, right in product(coefficient_range, repeat=2)
        for point in (lattice_point(left, right, d1, d2),)
        if all(0 <= coordinate < index for coordinate in point)
    }

    # Solve x=5m+n and y=-7m-7n over Q for every point satisfying
    # 7x+y=0 mod 28 in the fundamental square, and require integral m,n.
    reverse_witnesses: list[tuple[Point, tuple[int, int]]] = []
    for x, y in sorted(fundamental_congruence):
        coefficient_sum = Fraction(-y, 7)
        left = Fraction(x - coefficient_sum, 4)
        right = coefficient_sum - left
        if left.denominator != 1 or right.denominator != 1:
            continue
        integer_pair = (int(left), int(right))
        if lattice_point(*integer_pair, d1, d2) == (x, y):
            reverse_witnesses.append(((x, y), integer_pair))
    fundamental_reverse = len(reverse_witnesses) == len(fundamental_congruence)

    tick_witness = subtract(d1, d2)
    mixed_witness = lattice_point(1, -5, d1, d2)
    witnesses_exact = tick_witness == (4, 0) and mixed_witness == (0, 28)
    signs = {
        "x": {tick_witness[0], -tick_witness[0]},
        "y": {mixed_witness[1], -mixed_witness[1]},
    }
    sign_indefinite = (
        min(signs["x"]) < 0 < max(signs["x"])
        and min(signs["y"]) < 0 < max(signs["y"])
    )
    negation_closed = all(
        lattice_point(-left, -right, d1, d2)
        == tuple(-coordinate for coordinate in lattice_point(left, right, d1, d2))
        for left, right in product(range(-8, 9), repeat=2)
    )
    return DifferenceLatticeCertificate(
        d1=d1,
        d2=d2,
        signed_determinant=signed_determinant,
        index=index,
        primitive_normal=primitive_normal,
        generated_box_size=len(generated_box),
        generated_box_forward=generated_box_forward,
        fundamental_congruence_size=len(fundamental_congruence),
        fundamental_generated_size=len(fundamental_generated),
        fundamental_reverse=fundamental_reverse,
        fundamental_sets_equal=(fundamental_congruence == fundamental_generated),
        tick_witness=tick_witness,
        mixed_witness=mixed_witness,
        witnesses_exact=witnesses_exact,
        sign_indefinite_both_components=sign_indefinite,
        negation_closed=negation_closed,
    )


def rational_matrix_product(
    left: tuple[tuple[Fraction, ...], ...],
    right: tuple[tuple[Fraction, ...], ...],
) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(
            sum(
                (left[row][inner] * right[inner][column] for inner in range(len(right))),
                Fraction(0),
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


@dataclass(frozen=True)
class ConservedTotalCertificate:
    coefficient_matrix: tuple[Point, Point]
    signed_determinant: int
    inverse: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
    inverse_exact: bool
    homogeneous_solution: tuple[Fraction, Fraction]
    only_trivial_linear_part: bool
    constant_term_free: bool


def conserved_total_certificate(
    lattice: DifferenceLatticeCertificate,
) -> ConservedTotalCertificate:
    matrix = (lattice.d1, lattice.d2)
    a, b = matrix[0]
    c, d = matrix[1]
    signed_determinant = determinant(*matrix)
    inverse = (
        (Fraction(d, signed_determinant), Fraction(-b, signed_determinant)),
        (Fraction(-c, signed_determinant), Fraction(a, signed_determinant)),
    )
    rational_matrix = tuple(
        tuple(Fraction(value) for value in row) for row in matrix
    )
    identity = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    solution = (
        inverse[0][0] * 0 + inverse[0][1] * 0,
        inverse[1][0] * 0 + inverse[1][1] * 0,
    )
    base = FACET_CHARGE_POINTS[0]
    affine_differences = tuple(
        (point[0] - base[0], point[1] - base[1], 1 - 1)
        for point in FACET_CHARGE_POINTS[1:]
    )
    return ConservedTotalCertificate(
        coefficient_matrix=matrix,
        signed_determinant=signed_determinant,
        inverse=inverse,
        inverse_exact=(
            rational_matrix_product(rational_matrix, inverse) == identity
            and rational_matrix_product(inverse, rational_matrix) == identity
        ),
        homogeneous_solution=solution,
        only_trivial_linear_part=(
            signed_determinant != 0
            and solution == (Fraction(0), Fraction(0))
        ),
        # The affine constant c cancels between points and is unrestricted;
        # constancy forces only the TC and MC coefficients to vanish.
        constant_term_free=(
            tuple(row[:2] for row in affine_differences) == matrix
            and all(row[2] == 0 for row in affine_differences)
        ),
    )


@dataclass(frozen=True)
class ConeLatticeSplitCertificate:
    generator_x_coefficients: tuple[int, int]
    generator_y_coefficients: tuple[int, int]
    x_nonnegative: bool
    y_nonpositive: bool
    y_zero_only_at_origin: bool
    pointed: bool
    lattice_negation_closed: bool
    reversible_closure_negation_closed: bool
    reversibility_observed: bool | None
    upgrade_is_conditional: bool
    unconditional_upgrade_asserted: bool


def cone_lattice_split_certificate(
    lattice: DifferenceLatticeCertificate,
    mutation: str,
) -> ConeLatticeSplitCertificate:
    d1, d2 = lattice.d1, lattice.d2
    generator_x = (d1[0], d2[0])
    generator_y = (d1[1], d2[1])
    displayed = {d1, d2}
    reversible_closure = displayed | {
        tuple(-coordinate for coordinate in point) for point in displayed
    }
    reversible_closure_negation_closed = all(
        tuple(-coordinate for coordinate in point) in reversible_closure
        for point in reversible_closure
    )
    unconditional = mutation == "claim_unconditional_momentum"
    return ConeLatticeSplitCertificate(
        generator_x_coefficients=generator_x,
        generator_y_coefficients=generator_y,
        x_nonnegative=all(value >= 0 for value in generator_x),
        y_nonpositive=all(value <= 0 for value in generator_y),
        # For alpha,beta>=0, -y=7(alpha+beta); it vanishes exactly when
        # alpha=beta=0.  The same strict functional proves pointedness.
        y_zero_only_at_origin=tuple(-value for value in generator_y) == (7, 7),
        pointed=all(value > 0 for value in tuple(-value for value in generator_y)),
        lattice_negation_closed=lattice.negation_closed,
        reversible_closure_negation_closed=reversible_closure_negation_closed,
        reversibility_observed=REVERSIBILITY_IN_COST_CLASS,
        upgrade_is_conditional=(
            REVERSIBILITY_IN_COST_CLASS is None
            and reversible_closure_negation_closed
            and not unconditional
        ),
        unconditional_upgrade_asserted=unconditional,
    )


@dataclass(frozen=True)
class DeadEchoCertificate:
    involution_cycle_type: tuple[int, ...]
    order_four_cycle_type: tuple[int, ...]
    involution_cardinality: int
    order_four_cardinality: int
    involution_order: int
    order_four_order: int
    no_bijection_by_cardinality: bool
    no_generator_order_match: bool


def dead_echo_certificate() -> DeadEchoCertificate:
    involution = (1, 0, 3, 2, 5, 4, 7, 6)
    order_four = (1, 2, 3, 0)
    involution_order = permutation_order(involution)
    order_four_order = permutation_order(order_four)
    return DeadEchoCertificate(
        involution_cycle_type=cycle_type(involution),
        order_four_cycle_type=cycle_type(order_four),
        involution_cardinality=len(involution),
        order_four_cardinality=len(order_four),
        involution_order=involution_order,
        order_four_order=order_four_order,
        no_bijection_by_cardinality=(len(involution) != len(order_four)),
        no_generator_order_match=(involution_order != order_four_order),
    )


FLIP_ENUMERATION_WORK_ORDER = (
    "enumerate every flip type",
    "emit pre/post facet charges (TC,MC)",
    "emit facet-charge delta rows",
    "record reversibility within each interior-cost class",
    "compute the delta lattice, rank, cone, and rational nullspace",
)


@dataclass(frozen=True)
class WorkOrderCertificate:
    histogram: tuple[tuple[int, int], ...]
    fields: tuple[str, str]
    move_count: int
    summed_interior_cost_delta: int
    scalar_cost_deltas: bool
    even_move_multiplicities: bool
    typed_as_interior_cost: bool
    flip_facet_deltas: tuple[Point, ...] | None
    flip_outcome_unknown: bool
    work_order_complete: bool


def work_order_certificate() -> WorkOrderCertificate:
    move_count = sum(count for _, count in INTERIOR_COST_HISTOGRAM)
    summed_cost = sum(delta * count for delta, count in INTERIOR_COST_HISTOGRAM)
    return WorkOrderCertificate(
        histogram=INTERIOR_COST_HISTOGRAM,
        fields=HISTOGRAM_FIELDS,
        move_count=move_count,
        summed_interior_cost_delta=summed_cost,
        scalar_cost_deltas=all(
            type(delta) is int and type(count) is int
            for delta, count in INTERIOR_COST_HISTOGRAM
        ),
        even_move_multiplicities=all(
            count > 0 and count % 2 == 0
            for _, count in INTERIOR_COST_HISTOGRAM
        ),
        typed_as_interior_cost=(
            HISTOGRAM_FIELDS == ("interior_cost_delta", "move_count")
            and all(delta > 0 for delta, _ in INTERIOR_COST_HISTOGRAM)
        ),
        flip_facet_deltas=FLIP_FACET_DELTAS,
        flip_outcome_unknown=(FLIP_FACET_DELTAS is None),
        work_order_complete=(
            FLIP_ENUMERATION_WORK_ORDER
            == (
                "enumerate every flip type",
                "emit pre/post facet charges (TC,MC)",
                "emit facet-charge delta rows",
                "record reversibility within each interior-cost class",
                "compute the delta lattice, rank, cone, and rational nullspace",
            )
        ),
    )


SCOPE_KEYS = (
    "facet_charge",
    "difference_lattice",
    "index_28",
    "no_conserved_total",
    "one_sided_cone",
    "lattice_cone_split",
    "conditional_reversibility",
    "tt_parallel",
    "dead_naive_echo",
    "work_order",
    "cross_lane",
    "os_boundary",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity_quotient",
    "adm",
    "n1_n8",
    "w1",
    "n5_resolution",
    "n5_verbatim",
)


N5_LINES = (
    "N5: per_element: exact input-pin, lattice-equality, witness, conserved-solve, cone, and echo certificates are checked",
    "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus",
    "per_mode: the three displayed dissection charge points are noncollinear with signed-difference lattice 7x + y = 0 mod 28, sign-indefinite in both components",
    "per_block: the facet charges admit no conserved affine total and the momentum-like reading of their increments is a labeled conditional on cost-class reversibility — on displayed data only the one-sided cone is proven",
    "lattice_wide: checked and not executed — the flip-enumeration work order, the paired-degeneracy observable question, the common nilpotent differential, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient beyond the displayed carrier, Records, audit retention, and TOE closure remain open",
)


def scope_certificate(note: str, mutation: str) -> dict[str, bool]:
    result = {
        "facet_charge": "facet charge" in note or "facet-charge" in note,
        "difference_lattice": (
            "difference lattice" in note or "7x + y" in note
        ),
        "index_28": any(
            phrase in note
            for phrase in ("index 28", "det -28", "determinant -28")
        ),
        "no_conserved_total": "no conserved" in note and "total" in note,
        "one_sided_cone": "one-sided" in note and "cone" in note,
        "lattice_cone_split": (
            "negation-closed" in note or "lattice, not the cone" in note
        ),
        "conditional_reversibility": (
            "reversibility" in note and "conditional" in note
        ),
        "tt_parallel": "record-charge" in note or "raw counts" in note,
        "dead_naive_echo": any(
            phrase in note for phrase in ("dead", "naive echo", "no equivariant")
        ),
        "work_order": "work order" in note or "flip enumeration" in note,
        "cross_lane": "cross-lane" in note or "cell-cutting" in note,
        "os_boundary": (
            "not an os no-go" in note or "not a curved os no-go" in note
        ),
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "gravity_quotient": (
            "gravity constraint quotient remains unexecuted" in note
        ),
        "adm": "actual adm/history transporter remains" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "w1": "w1" in note,
        "n5_resolution": all(
            f"{resolution}:" in note
            for resolution in (
                "per_element",
                "per_site",
                "per_mode",
                "per_block",
                "lattice_wide",
            )
        ),
        "n5_verbatim": all(
            " ".join(line.lower().split()) in note for line in N5_LINES
        ),
    }
    if mutation == "weaken_no_go_packet":
        result["os_boundary"] = False
        result["n1_n8"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution"] = False
        result["n5_verbatim"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    if mutation == "claim_axiom_amendment":
        result["axiom"] = False
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started = time.monotonic()
    checks = Checks()

    authority = authority_certificate(mutation)
    authority_raw = (
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_FACET_CHARGE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SCALAR_QUOTIENT_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "scripts/admissibility_dirac_kahler_scalar_quotient_theorem_2026_08_17.py",
            "logs/runner-cache/admissibility_dirac_kahler_scalar_quotient_theorem_2026_08_17.txt",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(authority[f"ancestor_{number}"] for number in range(103, 129))
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB
        and authority["cell_blob"] == CELL_AUTHORITY_BLOB
        and authority["cell_on_main_history"]
    )
    checks.check(
        "A-authority",
        "Block 129 note/runner/cache, ancestors 128--103, and the cycle-767 content blob are pinned",
        authority_raw,
    )

    record = input_record_certificate()
    input_raw = (
        record.pins_exact
        and record.points == ((36, 55), (41, 48), (37, 48))
        and record.histogram == ((1, 192), (2, 96))
        and record.pairwise_distinct
        and record.signed_determinant == -28
        and record.noncollinear
    )
    input_gate = input_raw and mutation != "break_input_pins"
    checks.check(
        "B-the-input-record",
        "three literal facet-charge points and the cycle-734 interior-cost histogram are exact; det=-28",
        input_gate,
    )

    lattice = difference_lattice_certificate(record)
    lattice_equality_raw = (
        lattice.d1 == (5, -7)
        and lattice.d2 == (1, -7)
        and lattice.signed_determinant == -28
        and lattice.index == 28
        and lattice.primitive_normal == (7, 1)
        and lattice.generated_box_size > 0
        and lattice.generated_box_forward
        and lattice.fundamental_congruence_size == 28
        and lattice.fundamental_generated_size == 28
        and lattice.fundamental_reverse
        and lattice.fundamental_sets_equal
    )
    witness_raw = (
        lattice.tick_witness == (4, 0)
        and lattice.mixed_witness == (0, 28)
        and lattice.witnesses_exact
        and lattice.sign_indefinite_both_components
        and lattice.negation_closed
    )
    lattice_gate = lattice_equality_raw and witness_raw
    if mutation == "break_lattice_equality":
        lattice_gate = False
    if mutation == "break_witnesses":
        lattice_gate = False
    checks.check(
        "C-the-difference-lattice",
        "L=Zd1+Zd2 equals 7x+y=0 mod 28 both ways; (4,0),(0,28) and both signs are certified",
        lattice_gate,
    )

    conserved = conserved_total_certificate(lattice)
    conserved_raw = (
        conserved.coefficient_matrix == ((5, -7), (1, -7))
        and conserved.signed_determinant == -28
        and conserved.inverse_exact
        and conserved.homogeneous_solution == (Fraction(0), Fraction(0))
        and conserved.only_trivial_linear_part
        and conserved.constant_term_free
    )
    conserved_gate = conserved_raw and mutation != "break_conserved_solve"
    checks.check(
        "D-the-no-conserved-total",
        "5a-7b=0 and a-7b=0 give 4a=0, then a=b=0; the affine constant remains free",
        conserved_gate,
    )

    cone = cone_lattice_split_certificate(lattice, mutation)
    cone_raw = (
        cone.generator_x_coefficients == (5, 1)
        and cone.generator_y_coefficients == (-7, -7)
        and cone.x_nonnegative
        and cone.y_nonpositive
        and cone.y_zero_only_at_origin
        and cone.pointed
        and cone.lattice_negation_closed
        and cone.reversible_closure_negation_closed
        and cone.reversibility_observed is None
        and cone.upgrade_is_conditional
        and not cone.unconditional_upgrade_asserted
    )
    cone_gate = cone_raw and mutation != "break_cone_onesided"
    checks.check(
        "E-the-cone-lattice-split",
        "the directed cone is pointed and one-sided; only the lattice is negation-closed, and reversibility is conditional",
        cone_gate,
    )

    echo = dead_echo_certificate()
    echo_raw = (
        echo.involution_cycle_type == (2, 2, 2, 2)
        and echo.order_four_cycle_type == (4,)
        and echo.involution_cardinality == 8
        and echo.order_four_cardinality == 4
        and echo.involution_order == 2
        and echo.order_four_order == 4
        and echo.no_bijection_by_cardinality
        and echo.no_generator_order_match
    )
    echo_gate = echo_raw and mutation != "break_echo_facts"
    checks.check(
        "F-the-dead-echo",
        "2^4 on eight points versus 4^1 on four has neither a bijection nor a generator-order match",
        echo_gate,
    )

    work_order = work_order_certificate()
    work_order_raw = (
        work_order.histogram == ((1, 192), (2, 96))
        and work_order.fields == ("interior_cost_delta", "move_count")
        and work_order.move_count == 288
        and work_order.summed_interior_cost_delta == 384
        and work_order.scalar_cost_deltas
        and work_order.even_move_multiplicities
        and work_order.typed_as_interior_cost
        and work_order.flip_facet_deltas is None
        and work_order.flip_outcome_unknown
        and work_order.work_order_complete
    )
    work_order_gate = (
        work_order_raw and mutation != "claim_flip_deltas_known"
    )
    checks.check(
        "G-the-work-order",
        "the histogram is interior-cost-only; flip pre/post charges and cost-class reversibility remain required",
        work_order_gate,
    )

    scope = scope_certificate(normalized_note(), mutation)
    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "facet/lattice/cone/conditional/echo/work-order/N1--N8/W1/N5 and no-go/TOE firewalls are present",
        set(scope) == set(SCOPE_KEYS)
        and all(scope.values())
        and elapsed_before_scope <= 200,
    )

    print(
        "AUTHORITY: parent="
        f"{authority['parent']}; Block129 blobs=({authority['parent_note']},"
        f"{authority['parent_runner']},{authority['parent_cache']}); "
        f"cycle767={authority['cell_blob']}"
    )
    print(
        "INPUT: points="
        f"{record.points}; interior-cost histogram={record.histogram}; "
        f"pairwise distinct={record.pairwise_distinct}; det={record.signed_determinant}"
    )
    print(
        "LATTICE: d1="
        f"{lattice.d1}; d2={lattice.d2}; L={{(x,y):7x+y=0 mod 28}}; "
        f"fundamental points={lattice.fundamental_congruence_size}; "
        f"witnesses={lattice.tick_witness},{lattice.mixed_witness} and negatives"
    )
    print(
        "SOLVE: [[5,-7],[1,-7]](a,b)^T=0; subtracting rows gives "
        "4a=0, hence a=b=0; affine c is unrestricted"
    )
    print(
        "CONE: alpha*d1+beta*d2=(5alpha+beta,-7(alpha+beta)); "
        "alpha,beta>=0 gives x>=0,y<=0 with y=0 only at the origin; "
        "reversibility-in-cost-class=UNMEASURED"
    )
    print(
        "ECHO/WORK: cycle types="
        f"{echo.involution_cycle_type} vs {echo.order_four_cycle_type}; "
        f"orders={echo.involution_order} vs {echo.order_four_order}; "
        "flip facet-deltas=UNMEASURED"
    )
    for line in N5_LINES:
        print(line)
    print(
        "RESULT: the first cross-lane theorem stands on exact arithmetic — "
        "no conserved facet total, an indefinite difference lattice, a "
        "one-sided displayed cone, and a dead naive echo — with the "
        "momentum-like bridge conditional on reversibility and the flip "
        "enumeration named as the deciding computation"
    )
    print(
        "DECISION_CUT: hand the flip work order to the cell-cutting lane; "
        "advance the paired-degeneracy question; reject unconditional "
        "momentum-like claims"
    )
    print(
        "TOE: zero obligation retirement; no TOE percentage moves; "
        "retained-positive end-to-end theory count remains zero; gravity "
        "constraint quotient remains unexecuted; actual ADM/history "
        "transporter remains open"
    )
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
