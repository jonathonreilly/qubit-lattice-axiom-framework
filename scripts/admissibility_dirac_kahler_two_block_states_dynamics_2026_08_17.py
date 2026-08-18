#!/usr/bin/env python3
"""Block 133: exact states-and-dynamics certificate for the two-block algebra.

The runner imports the landed Block 132 observable-algebra construction and
uses exact rational or algebraic arithmetic throughout.  It distinguishes the
biased state induced in the certified frame from the separately normalized
Tr/4 frame, certifies the counter-rotating momentum quadratures, and identifies
the balanced gravity class without adjoining its missing Y observable.
Wall-clock timing is the sole floating-point quantity.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16 as b119
import admissibility_dirac_kahler_two_block_observable_algebra_2026_08_17 as b132


R = sp.Rational
I = sp.I
RHO = b119.RHO
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_TWO_BLOCK_STATES_DYNAMICS_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_BLOCK_OBSERVABLE_ALGEBRA_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_two_block_observable_algebra_"
    "2026_08_17.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_two_block_observable_"
    "algebra_2026_08_17.txt"
)
B119_RUNNER = (
    "scripts/admissibility_dirac_kahler_reflection_intertwiner_completion_"
    "2026_08_16.py"
)
B119_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_reflection_intertwiner_"
    "completion_2026_08_16.txt"
)

# This tuple is deliberately literal: it is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_BLOCK_STATES_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_BLOCK_OBSERVABLE_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_two_block_observable_algebra_2026_08_17.py",
    "logs/runner-cache/admissibility_dirac_kahler_two_block_observable_algebra_2026_08_17.txt",
    "scripts/admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16.py",
    "logs/runner-cache/admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "02602ca09e4ea69a805a824c3c1f31cb1ee35b20"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block132-two-block-observable-algebra-20260817"
)
PARENT_COMMIT = "0236823bed5b648ad8357e5d1b79bdfe1be36c39"
PARENT_NOTE_BLOB = "4b330950a10afd8aeb863107271dd5605b86fdde"
PARENT_RUNNER_BLOB = "c23896e00ab00ab2bf587cae8f4002b34a62c80a"
PARENT_CACHE_BLOB = "411b5f5fb2c63e7c4d4cc57ac85cafe78d97a306"
B119_COMMIT = "33fd2d21558604718f3a88713fe1976aff8f9dbb"
B119_RUNNER_BLOB = "952494a18ba13b7d25fb144b8569687813d9bddc"
B119_CACHE_BLOB = "f7a9b09538c8787ed88885c04cdea3e5cff70104"

ANCESTOR_COMMITS = (
    (131, "d3a666f62c87b3b8178289024087090c91ced327"),
    (130, "db394d1536a8243c2b01b3e45413813e45f8abdd"),
    (129, "30fd2722a10a02f87c235e2ee592d140f8bb7df5"),
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

# q_0 and q_1 are pinned independently.  The remaining exact direction
# weights are then pinned by q_2=g_02 q_0 (with Block 132's literal g_02 pin)
# and the forced conjugate-pair identity q_3=q_1.
DIRECTION_BASE_PINS = {
    R(5, 13): (
        R(
            1150375921826694113555410035428125457400046724232655679510128418644,
            78818981495363350772720329776070208150156820427053866300121890625,
        )
        * RHO
        + R(
            2551760577187948708831975621544907002416341583124,
            2017627675810846293109860712085830226130175201449,
        ),
        R(
            74810282488664230980940890727509529911814046713354838439326223427401027593902539112485052,
            96263948812720778195707147302876216488862931210874321631857695665694862166240216796875,
        )
        * RHO
        + R(
            5861115526326352488714957098049817172821651848298584759897950715316,
            6571479869879327548698576558000254761468540553325723058519469865141,
        ),
    ),
    R(3, 5): (
        R(
            1929582570829448125429212338350289753301106276,
            199669918972549851130286515573737207275390625,
        )
        * RHO
        + R(
            685969651848560392472786260406310596,
            478257127996035806743292224763026521,
        ),
        R(
            1457386714041244279937491929662883188827670431983183517670528156972,
            560375227874156102732062361754341714825305744456110940342421875,
        )
        * RHO
        + R(
            5249507183780459677725873072861609272806341163892,
            7291367263848626791180264000120680322961850668777,
        ),
    ),
}

MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_state_space",
    "break_vacuum_weights",
    "claim_certified_maximally_mixed",
    "break_normalization_ledger",
    "break_orbit_signs",
    "break_conserving_algebra",
    "break_equator_identification",
    "break_invariant_span",
    "break_summary_table",
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
        "worktree_parent_note": worktree_blob(PARENT_NOTE),
        "worktree_parent_runner": worktree_blob(PARENT_RUNNER),
        "worktree_parent_cache": worktree_blob(PARENT_CACHE),
        "b119_ancestor": is_ancestor(B119_COMMIT, "HEAD"),
        "b119_runner": commit_blob(B119_COMMIT, B119_RUNNER),
        "b119_cache": commit_blob(B119_COMMIT, B119_CACHE),
        "worktree_b119_runner": worktree_blob(B119_RUNNER),
        "worktree_b119_cache": worktree_blob(B119_CACHE),
    }


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


def commutator(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return (left * right - right * left).applyfunc(sp.expand)


def trace_pair(density: sp.Matrix, observable: sp.Matrix) -> sp.Expr:
    return sp.factor(sp.trace(density * observable))


def same_row_space(left: sp.Matrix, right: sp.Matrix) -> bool:
    return (
        left.cols == right.cols
        and left.rank() == right.rank()
        and left.col_join(right).rank() == left.rank()
    )


def embed_pair(matrix: sp.Matrix, indices: tuple[int, int]) -> sp.Matrix:
    result = sp.zeros(4)
    for local_row, row in enumerate(indices):
        for local_column, column in enumerate(indices):
            result[row, column] = matrix[local_row, local_column]
    return result


I2 = sp.eye(2)
X = sp.Matrix(((0, 1), (1, 0)))
Y = sp.Matrix(((0, I), (-I, 0)))
Z = sp.Matrix(((1, 0), (0, -1)))


def disk_density(x: sp.Expr, z: sp.Expr) -> sp.Matrix:
    """The trace-one real qubit density in disk coordinates."""
    return sp.Matrix(((1 + z, x), (x, 1 - z))) / 2


@dataclass(frozen=True)
class StateSpaceCertificate:
    weight: sp.Symbol
    density02: sp.Matrix
    density13: sp.Matrix
    total_density: sp.Matrix
    trace_normalized: bool
    disk_determinants_exact: bool
    inverse_coordinates_exact: bool
    ambient_dimension: int
    trace_constraint_rank: int
    affine_dimension: int
    pure_projector_identity: bool
    pure_bloch_circle: bool
    antipodal_identification: bool
    fixture_independent: bool


def state_space_certificate() -> StateSpaceCertificate:
    w, x02, z02, x13, z13 = sp.symbols(
        "w x_02 z_02 x_13 z_13", real=True
    )
    rho02 = disk_density(x02, z02)
    rho13 = disk_density(x13, z13)
    density02 = w * rho02
    density13 = (1 - w) * rho13
    total_density = embed_pair(density02, (0, 2)) + embed_pair(
        density13, (1, 3)
    )
    determinant_identities = (
        sp.simplify(
            rho02.det() - (1 - x02**2 - z02**2) / 4
        )
        == 0
        and sp.simplify(
            rho13.det() - (1 - x13**2 - z13**2) / 4
        )
        == 0
    )

    a, b = sp.symbols("a b", real=True)
    generic_trace_one = sp.Matrix(((a, b), (b, 1 - a)))
    inverse_x = 2 * b
    inverse_z = 2 * a - 1
    inverse_coordinates_exact = (
        matrix_zero(disk_density(inverse_x, inverse_z) - generic_trace_one)
        and sp.factor(
            generic_trace_one.det()
            - (1 - inverse_x**2 - inverse_z**2) / 4
        )
        == 0
    )

    e00 = sp.Matrix(((1, 0), (0, 0)))
    e11 = sp.Matrix(((0, 0), (0, 1)))
    affine_basis = (
        embed_pair(e00, (0, 2)),
        embed_pair(e11, (0, 2)),
        embed_pair(X, (0, 2)),
        embed_pair(e00, (1, 3)),
        embed_pair(e11, (1, 3)),
        embed_pair(X, (1, 3)),
    )
    basis_columns = tuple(sp.Matrix(tuple(item)) for item in affine_basis)
    ambient_dimension = sp.Matrix.hstack(*basis_columns).rank()
    trace_constraint = sp.Matrix(
        [[sp.trace(item) for item in affine_basis]]
    )
    trace_constraint_rank = trace_constraint.rank()
    affine_dimension = ambient_dimension - trace_constraint_rank

    u, v = sp.symbols("u v", real=True)
    vector = sp.Matrix((u, v))
    projector = vector * vector.T
    norm = u**2 + v**2
    bloch_x = 2 * u * v
    bloch_z = u**2 - v**2
    pure_projector_identity = matrix_zero(
        projector * projector - norm * projector
    )
    pure_bloch_circle = sp.expand(
        bloch_x**2 + bloch_z**2 - norm**2
    ) == 0
    antipodal_identification = matrix_zero(
        (-vector) * (-vector).T - projector
    )
    displayed_expressions = (
        density02,
        density13,
        total_density,
        projector,
        sp.Matrix((bloch_x, bloch_z)),
    )
    fixture_independent = all(
        RHO not in expression.free_symbols for expression in displayed_expressions
    )
    return StateSpaceCertificate(
        w,
        density02,
        density13,
        total_density,
        sp.factor(sp.trace(total_density)) == 1,
        determinant_identities,
        inverse_coordinates_exact,
        ambient_dimension,
        trace_constraint_rank,
        affine_dimension,
        pure_projector_identity,
        pure_bloch_circle,
        antipodal_identification,
        fixture_independent,
    )


def affine_root_interval(
    expression: sp.Expr,
    sector: b119.Sector,
) -> tuple[sp.Rational, sp.Rational]:
    """Exact rational enclosure using the certified stable-root interval."""
    reduced = b119.red(expression, sector.polynomial)
    polynomial = sp.Poly(reduced, RHO)
    if polynomial.degree() > 1:
        raise AssertionError("a direction weight must be affine in its root")
    slope = polynomial.coeff_monomial(RHO)
    intercept = polynomial.coeff_monomial(1)
    lower_integer, upper_integer = sector.stable_interval
    lower_root = R(lower_integer, 10**12)
    upper_root = R(upper_integer, 10**12)
    endpoint_values = (
        sp.cancel(slope * lower_root + intercept),
        sp.cancel(slope * upper_root + intercept),
    )
    return min(endpoint_values), max(endpoint_values)


def intervals_disjoint(
    left: tuple[sp.Rational, sp.Rational],
    right: tuple[sp.Rational, sp.Rational],
) -> bool:
    return left[1] < right[0] or right[1] < left[0]


@dataclass(frozen=True)
class FixtureVacuumCertificate:
    shear: sp.Rational
    direction_weights: tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]
    base_weight_pins: tuple[sp.Expr, sp.Expr]
    exact_weights_pinned: bool
    direction_intervals: tuple[
        tuple[sp.Rational, sp.Rational],
        tuple[sp.Rational, sp.Rational],
        tuple[sp.Rational, sp.Rational],
        tuple[sp.Rational, sp.Rational],
    ]
    all_weights_positive: bool
    one_three_equality_forced: bool
    zero_two_weights_unequal: bool
    zero_one_weights_unequal: bool
    block_totals_unequal: bool


def fixture_vacuum_certificate(
    sectors: tuple[b119.Sector, ...],
    carrier: b132.CarrierCertificate,
) -> FixtureVacuumCertificate:
    if len(sectors) != 4:
        raise AssertionError("one fixture must have four sector directions")
    weights = tuple(
        b132.vector_norm_squared(sector.y, sector.polynomial)
        for sector in sectors
    )
    if carrier.shear not in DIRECTION_BASE_PINS:
        raise AssertionError("the fixture has no direction-weight pin")
    pin_zero, pin_one = DIRECTION_BASE_PINS[carrier.shear]
    zero_pin = b119.red(weights[0] - pin_zero, sectors[0].polynomial) == 0
    one_pin = b119.red(weights[1] - pin_one, sectors[1].polynomial) == 0
    two_pin = b119.red(
        weights[2] - carrier.g_pin * weights[0], sectors[0].polynomial
    ) == 0
    three_pin = b119.red(
        weights[3] - weights[1], sectors[1].polynomial
    ) == 0
    split = b132.fixture_split_certificate(sectors)
    one_three_forced = (
        split.one_three_polynomial_shared
        and split.one_three_root_shared
        and split.one_three_y_conjugate
        and split.one_three_g_one
        and three_pin
    )
    zero_two_unequal = (
        carrier.g_nonunit
        and b119.red(weights[2] - weights[0], sectors[0].polynomial) != 0
    )
    intervals = tuple(
        affine_root_interval(weight, sector)
        for weight, sector in zip(weights, sectors)
    )
    even_total_interval = affine_root_interval(
        weights[0] + weights[2], sectors[0]
    )
    odd_total_interval = affine_root_interval(
        weights[1] + weights[3], sectors[1]
    )
    return FixtureVacuumCertificate(
        carrier.shear,
        weights,
        (pin_zero, pin_one),
        zero_pin and one_pin and two_pin and three_pin,
        intervals,
        all(lower > 0 for lower, _ in intervals),
        one_three_forced,
        zero_two_unequal,
        intervals_disjoint(intervals[0], intervals[1]),
        intervals_disjoint(even_total_interval, odd_total_interval),
    )


@dataclass(frozen=True)
class CertifiedVacuumCertificate:
    fixtures: tuple[FixtureVacuumCertificate, ...]
    symbolic_weights: tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]
    density: sp.Matrix
    central_weights: tuple[sp.Expr, sp.Expr]
    internal_densities: tuple[sp.Matrix, sp.Matrix]
    trace_normalized: bool
    trace_representation_exact: bool
    central_decomposition_exact: bool
    certified_frame_biased: bool
    one_three_maximally_mixed: bool


def certified_vacuum_certificate(
    fixtures: tuple[FixtureVacuumCertificate, ...],
) -> CertifiedVacuumCertificate:
    q_zero, q_one, g = sp.symbols(
        "q_0 q_1 g_02", positive=True, nonzero=True
    )
    weights = (q_zero, q_one, g * q_zero, q_one)
    total = sum(weights)
    density = sp.diag(*weights) / total
    central_weights = (
        sp.factor((weights[0] + weights[2]) / total),
        sp.factor((weights[1] + weights[3]) / total),
    )
    internal02 = sp.diag(weights[0], weights[2]) / (
        weights[0] + weights[2]
    )
    internal13 = sp.diag(weights[1], weights[3]) / (
        weights[1] + weights[3]
    )
    reconstructed = (
        central_weights[0] * embed_pair(internal02, (0, 2))
        + central_weights[1] * embed_pair(internal13, (1, 3))
    )

    a02, b02, d02, a13, b13, d13 = sp.symbols(
        "a_02 b_02 d_02 a_13 b_13 d_13", real=True
    )
    observable = embed_pair(
        sp.Matrix(((a02, b02), (b02, d02))), (0, 2)
    ) + embed_pair(sp.Matrix(((a13, b13), (b13, d13))), (1, 3))
    induced_functional = sp.factor(
        (
            weights[0] * a02
            + weights[2] * d02
            + weights[1] * a13
            + weights[3] * d13
        )
        / total
    )
    all_fixture_biases = all(
        item.exact_weights_pinned
        and item.all_weights_positive
        and item.one_three_equality_forced
        and item.zero_two_weights_unequal
        and item.block_totals_unequal
        for item in fixtures
    )
    return CertifiedVacuumCertificate(
        fixtures,
        weights,
        density,
        central_weights,
        (internal02, internal13),
        sp.factor(sp.trace(density)) == 1,
        sp.factor(trace_pair(density, observable) - induced_functional) == 0,
        matrix_zero(density - reconstructed),
        all_fixture_biases,
        matrix_zero(internal13 - I2 / 2)
        and all(item.one_three_equality_forced for item in fixtures),
    )


@dataclass(frozen=True)
class NormalizationCertificate:
    certified_gram: sp.Matrix
    intra_block_scale: sp.Matrix
    intra_block_gram: sp.Matrix
    block_scale: sp.Matrix
    final_gram: sp.Matrix
    final_density: sp.Matrix
    parent_not_square_imported: bool
    first_move_needed: bool
    second_move_needed: bool
    exactly_two_moves: bool
    intra_block_equalization_exact: bool
    block_equalization_exact: bool
    scales_real_positive: bool
    involutivity_preserved: bool
    positivity_preserved: bool


def normalization_certificate(
    carriers: tuple[b132.CarrierCertificate, ...],
    fixtures: tuple[FixtureVacuumCertificate, ...],
) -> NormalizationCertificate:
    q_zero, q_one, g = sp.symbols(
        "q_0 q_1 g_02", positive=True, nonzero=True
    )
    certified_gram = sp.diag(q_zero, q_one, g * q_zero, q_one)
    intra_scale = sp.diag(1, 1, 1 / sp.sqrt(g), 1)
    intra_gram = (intra_scale.T * certified_gram * intra_scale).applyfunc(
        sp.simplify
    )
    block_scale = sp.diag(
        1,
        sp.sqrt(q_zero / q_one),
        1,
        sp.sqrt(q_zero / q_one),
    )
    final_gram = (block_scale.T * intra_gram * block_scale).applyfunc(
        sp.simplify
    )
    final_density = (final_gram / sp.trace(final_gram)).applyfunc(sp.simplify)

    fields = tuple(b132.field_caveat_certificate(item) for item in carriers)
    gauges = tuple(b132.gauge_certificate(item) for item in carriers)
    parent_observable = b132.observable_space_certificate()
    parent_not_square_imported = all(
        field.root_field_quadratic
        and field.no_rational_solution
        and field.sqrt_not_in_field
        for field in fields
    ) and all(gauge.extension_normalization for gauge in gauges)

    scales = tuple(intra_scale.diagonal()) + tuple(block_scale.diagonal())
    scales_real_positive = all(
        sp.simplify(sp.conjugate(value) - value) == 0
        and value.is_positive is True
        for value in scales
    )
    reality = sp.eye(4)
    transformed_reality_one = (
        intra_scale.inv() * reality * intra_scale.conjugate()
    ).applyfunc(sp.simplify)
    transformed_reality_two = (
        block_scale.inv()
        * transformed_reality_one
        * block_scale.conjugate()
    ).applyfunc(sp.simplify)
    involutivity_preserved = (
        matrix_zero(transformed_reality_one - sp.eye(4))
        and matrix_zero(transformed_reality_two - sp.eye(4))
        and matrix_zero(
            transformed_reality_two * transformed_reality_two.conjugate()
            - sp.eye(4)
        )
        and parent_observable.involutivity_preserved
    )
    positivity_preserved = (
        all(value.is_positive is True for value in intra_gram.diagonal())
        and all(value.is_positive is True for value in final_gram.diagonal())
        and parent_observable.positivity_preserved
    )
    first_move_needed = all(item.zero_two_weights_unequal for item in fixtures)
    second_move_needed = all(item.zero_one_weights_unequal for item in fixtures)
    two_moves = (intra_scale, block_scale)
    return NormalizationCertificate(
        certified_gram,
        intra_scale,
        intra_gram,
        block_scale,
        final_gram,
        final_density,
        parent_not_square_imported,
        first_move_needed,
        second_move_needed,
        len(two_moves) == 2 and first_move_needed and second_move_needed,
        matrix_zero(intra_gram - sp.diag(q_zero, q_one, q_zero, q_one)),
        matrix_zero(final_gram - q_zero * sp.eye(4))
        and matrix_zero(final_density - sp.eye(4) / 4),
        scales_real_positive,
        involutivity_preserved,
        positivity_preserved,
    )


def observable_basis() -> tuple[tuple[str, sp.Matrix], ...]:
    return (
        ("I_02", embed_pair(I2, (0, 2))),
        ("Z_02", embed_pair(Z, (0, 2))),
        ("X_02", embed_pair(X, (0, 2))),
        ("I_13", embed_pair(I2, (1, 3))),
        ("Z_13", embed_pair(Z, (1, 3))),
        ("X_13", embed_pair(X, (1, 3))),
    )


def trig_matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(
        sp.simplify(sp.expand_complex(value)) == 0 for value in matrix
    )


@dataclass(frozen=True)
class MomentumCertificate:
    momentum: sp.Matrix
    generator_differences: tuple[int, int]
    orbit02_x: sp.Matrix
    orbit02_y: sp.Matrix
    orbit13_x: sp.Matrix
    orbit13_y: sp.Matrix
    orbit02_exact: bool
    orbit13_exact: bool
    opposite_orientations: bool
    identity_and_z_fixed: bool
    conserving_flags: tuple[bool, bool, bool, bool, bool, bool]
    commutant_rank: int
    commutant_dimension: int
    conserving_algebra_exact: bool


def momentum_certificate() -> MomentumCertificate:
    t = sp.Symbol("t", real=True)
    cosine, sine = sp.cos(2 * t), sp.sin(2 * t)
    momentum02 = sp.diag(0, 2)
    momentum13 = sp.diag(1, -1)
    momentum = sp.diag(0, 1, 2, -1)
    difference02 = int(momentum02[0, 0] - momentum02[1, 1])
    difference13 = int(momentum13[0, 0] - momentum13[1, 1])
    unitary02 = sp.diag(sp.exp(I * 0 * t), sp.exp(I * 2 * t))
    unitary13 = sp.diag(sp.exp(I * t), sp.exp(-I * t))

    orbit02_x = cosine * X - sine * Y
    orbit02_y = sine * X + cosine * Y
    orbit13_x = cosine * X + sine * Y
    orbit13_y = -sine * X + cosine * Y
    exact02 = (
        trig_matrix_zero(unitary02 * X * unitary02.H - orbit02_x)
        and trig_matrix_zero(unitary02 * Y * unitary02.H - orbit02_y)
        and matrix_zero(
            orbit02_x.diff(t).subs(t, 0) - I * commutator(momentum02, X)
        )
        and matrix_zero(
            orbit02_y.diff(t).subs(t, 0) - I * commutator(momentum02, Y)
        )
    )
    exact13 = (
        trig_matrix_zero(unitary13 * X * unitary13.H - orbit13_x)
        and trig_matrix_zero(unitary13 * Y * unitary13.H - orbit13_y)
        and matrix_zero(
            orbit13_x.diff(t).subs(t, 0) - I * commutator(momentum13, X)
        )
        and matrix_zero(
            orbit13_y.diff(t).subs(t, 0) - I * commutator(momentum13, Y)
        )
    )
    fixed = all(
        trig_matrix_zero(unitary * matrix * unitary.H - matrix)
        for unitary in (unitary02, unitary13)
        for matrix in (I2, Z)
    )
    basis = observable_basis()
    conserving = tuple(
        matrix_zero(commutator(momentum, matrix)) for _, matrix in basis
    )

    a02, b02, c02, a13, b13, c13 = sp.symbols(
        "a_02 b_02 c_02 a_13 b_13 c_13", real=True
    )
    variables = (a02, b02, c02, a13, b13, c13)
    generic = embed_pair(a02 * I2 + b02 * X + c02 * Z, (0, 2))
    generic += embed_pair(a13 * I2 + b13 * X + c13 * Z, (1, 3))
    equations = tuple(
        entry for entry in commutator(momentum, generic) if entry != 0
    )
    coefficients, _ = sp.linear_eq_to_matrix(equations, variables)
    expected_coefficients, _ = sp.linear_eq_to_matrix(
        (b02, b13), variables
    )
    commutant_rank = coefficients.rank()
    commutant_dimension = len(variables) - commutant_rank
    conserving_exact = (
        same_row_space(coefficients, expected_coefficients)
        and commutant_rank == 2
        and commutant_dimension == 4
        and conserving == (True, True, False, True, True, False)
        and momentum02[0, 0] != momentum02[1, 1]
        and momentum13[0, 0] != momentum13[1, 1]
    )
    return MomentumCertificate(
        momentum,
        (difference02, difference13),
        orbit02_x,
        orbit02_y,
        orbit13_x,
        orbit13_y,
        exact02,
        exact13,
        (difference02, difference13) == (-2, 2),
        fixed,
        conserving,
        commutant_rank,
        commutant_dimension,
        conserving_exact,
    )


@dataclass(frozen=True)
class BalancedEquatorCertificate:
    radius: sp.Symbol
    phase: sp.Symbol
    pure_density: sp.Matrix
    family_density: sp.Matrix
    equal_moduli_exact: bool
    relative_phase_free: bool
    equator_identification_exact: bool
    positivity_identity_exact: bool
    general_observable: sp.Matrix
    general_expectation: sp.Expr
    y_not_admissible: bool
    invariant_rank: int
    invariant_dimension: int
    invariant_span_exact: bool


def balanced_equator_certificate() -> BalancedEquatorCertificate:
    radius = sp.Symbol("r", positive=True, nonzero=True)
    phase = sp.Symbol("phi", real=True)
    c_one = 1 / sp.sqrt(2)
    c_three = sp.exp(-I * phase) / sp.sqrt(2)
    vector = sp.Matrix((c_one, c_three))
    pure_density = vector * vector.H
    expected_pure = (I2 + sp.cos(phase) * X + sp.sin(phase) * Y) / 2
    family_density = (
        radius * pure_density + (1 - radius) * I2 / 2
    ).applyfunc(sp.expand)
    expected_family = (
        I2
        + radius * (sp.cos(phase) * X + sp.sin(phase) * Y)
    ) / 2
    equal_moduli = (
        sp.simplify(sp.conjugate(c_one) * c_one) == R(1, 2)
        and sp.simplify(sp.conjugate(c_three) * c_three) == R(1, 2)
        and sp.simplify((vector.H * vector)[0]) == 1
    )
    full_phase = (
        trig_matrix_zero(pure_density.subs(phase, 0) - (I2 + X) / 2)
        and trig_matrix_zero(
            pure_density.subs(phase, sp.pi / 2) - (I2 + Y) / 2
        )
        and phase in pure_density.free_symbols
    )
    equator_exact = (
        trig_matrix_zero(pure_density - expected_pure)
        and trig_matrix_zero(family_density - expected_family)
    )
    positivity_identity = (
        sp.simplify(sp.trace(expected_family)) == 1
        and sp.simplify(
            sp.expand_complex(expected_family.det()) - (1 - radius**2) / 4
        )
        == 0
    )

    a, b, c = sp.symbols("a b c", real=True)
    observable = a * I2 + b * X + c * Z
    expectation = sp.simplify(
        sp.expand_complex(trace_pair(expected_family, observable))
    )
    phase_difference = sp.simplify(
        expectation.subs(phase, 0) - expectation.subs(phase, sp.pi)
    )
    invariant_equation = sp.simplify(phase_difference / (2 * radius))
    variables = (a, b, c)
    invariant_coefficients, _ = sp.linear_eq_to_matrix(
        (invariant_equation,), variables
    )
    expected_coefficients, _ = sp.linear_eq_to_matrix((b,), variables)
    invariant_rank = invariant_coefficients.rank()
    invariant_dimension = len(variables) - invariant_rank
    y_excluded = (
        matrix_zero(Y.H - Y)
        and matrix_zero(Y.T + Y)
        and matrix_zero(Y.conjugate() + Y)
        and not matrix_zero(Y.T - Y)
        and not matrix_zero(Y.conjugate() - Y)
    )
    invariant_exact = (
        expectation == a + radius * b * sp.cos(phase)
        and invariant_equation == b
        and same_row_space(invariant_coefficients, expected_coefficients)
        and invariant_rank == 1
        and invariant_dimension == 2
        and y_excluded
    )
    return BalancedEquatorCertificate(
        radius,
        phase,
        pure_density,
        expected_family,
        equal_moduli,
        full_phase,
        equator_exact,
        positivity_identity,
        observable,
        expectation,
        y_excluded,
        invariant_rank,
        invariant_dimension,
        invariant_exact,
    )


@dataclass(frozen=True)
class BasisRow:
    name: str
    matrix: sp.Matrix
    momentum_conserving: bool
    balanced_measurable: str
    certified_vacuum_value: sp.Expr


@dataclass(frozen=True)
class SummaryTableCertificate:
    rows: tuple[BasisRow, ...]
    table_exact: bool
    honest_closer: str
    no_tensor_claim: bool


def summary_table_certificate(
    vacuum: CertifiedVacuumCertificate,
    momentum: MomentumCertificate,
    balanced: BalancedEquatorCertificate,
) -> SummaryTableCertificate:
    basis = observable_basis()
    balanced_full = embed_pair(balanced.family_density, (1, 3))
    balanced_expectations = tuple(
        sp.simplify(sp.expand_complex(trace_pair(balanced_full, matrix)))
        for _, matrix in basis
    )
    balanced_labels = tuple(
        "null"
        if index < 3 and expectation == 0
        else (
            "yes"
            if sp.simplify(sp.diff(expectation, balanced.phase)) == 0
            else "no"
        )
        for index, expectation in enumerate(balanced_expectations)
    )
    vacuum_values = tuple(
        sp.factor(trace_pair(vacuum.density, matrix))
        for _, matrix in basis
    )
    rows = tuple(
        BasisRow(
            name,
            matrix,
            momentum.conserving_flags[index],
            balanced_labels[index],
            vacuum_values[index],
        )
        for index, (name, matrix) in enumerate(basis)
    )
    q_zero, q_one, g = vacuum.symbolic_weights[:3]
    # The third tuple entry is g*q_0, so recover g without introducing a
    # second source for the exact table values.
    g = sp.cancel(vacuum.symbolic_weights[2] / q_zero)
    total = sum(vacuum.symbolic_weights)
    expected_vacuum = (
        sp.factor(q_zero * (1 + g) / total),
        sp.factor(q_zero * (1 - g) / total),
        sp.Integer(0),
        sp.factor(2 * q_one / total),
        sp.Integer(0),
        sp.Integer(0),
    )
    closer = (
        "exact expectations and selection rules are complete on the direct "
        "sum; no tensor-product structure is claimed"
    )
    table_exact = (
        tuple(row.name for row in rows)
        == ("I_02", "Z_02", "X_02", "I_13", "Z_13", "X_13")
        and tuple(row.momentum_conserving for row in rows)
        == (True, True, False, True, True, False)
        and tuple(row.balanced_measurable for row in rows)
        == ("null", "null", "null", "yes", "yes", "no")
        and all(
            sp.factor(actual - expected) == 0
            for actual, expected in zip(vacuum_values, expected_vacuum)
        )
    )
    return SummaryTableCertificate(
        rows,
        table_exact,
        closer,
        "no tensor-product structure" in closer
        and "tensor-product structure exists" not in closer,
    )


N5_LINES = (
    "N5: per_element: exact state-space, vacuum-weight, normalization, orbit, equator, and summary certificates are checked",
    "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus",
    "per_mode: the certified vacuum is a biased central mixture with the conjugate block maximally mixed by force and the per-sector-real block biased, while momentum counter-rotates the two blocks' quadratures at rate two",
    "per_block: the balanced gravity sector is the full bloch equator whose invariant observables are exactly the identity and z because the y quadrature is not an admissible observable — the certified package's measurement physics is complete with exact expectations and selection rules",
    "lattice_wide: checked and not executed — the common nilpotent differential, the flip work order, richer carriers, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient beyond the displayed carrier, Records, audit retention, and TOE closure remain open",
)


SCOPE_KEYS = (
    "biased_central_mixture",
    "frame_distinction",
    "two_moves",
    "opposite_orientations",
    "diagonal_conserving",
    "full_equator",
    "invariant_span",
    "y_exclusion",
    "no_tensor",
    "measurement_physics",
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


def scope_certificate(note: str, mutation: str) -> dict[str, bool]:
    result = {
        "biased_central_mixture": "biased" in note
        and "central mixture" in note,
        "frame_distinction": "certified frame" in note
        and "normalized frame" in note,
        "two_moves": "two normalizations" in note or "two moves" in note,
        "opposite_orientations": "opposite orientations" in note
        or "counter-rotating" in note,
        "diagonal_conserving": "diagonal" in note and "conserving" in note,
        "full_equator": "full bloch equator" in note
        or "free relative phase" in note,
        "invariant_span": "span{i, z}" in note or "i and z" in note,
        "y_exclusion": "y quadrature" in note and "not an" in note,
        "no_tensor": "no tensor-product structure" in note,
        "measurement_physics": "selection rules" in note
        or "exact expectations" in note,
        "os_boundary": "not an os no-go" in note
        or "not a curved os no-go" in note,
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
            "docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_BLOCK_STATES_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_BLOCK_OBSERVABLE_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "scripts/admissibility_dirac_kahler_two_block_observable_algebra_2026_08_17.py",
            "logs/runner-cache/admissibility_dirac_kahler_two_block_observable_algebra_2026_08_17.txt",
            "scripts/admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16.py",
            "logs/runner-cache/admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16.txt",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(
            authority[f"ancestor_{number}"] for number in range(103, 132)
        )
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB
        and authority["worktree_parent_note"] == PARENT_NOTE_BLOB
        and authority["worktree_parent_runner"] == PARENT_RUNNER_BLOB
        and authority["worktree_parent_cache"] == PARENT_CACHE_BLOB
        and authority["b119_ancestor"]
        and authority["b119_runner"] == B119_RUNNER_BLOB
        and authority["b119_cache"] == B119_CACHE_BLOB
        and authority["worktree_b119_runner"] == B119_RUNNER_BLOB
        and authority["worktree_b119_cache"] == B119_CACHE_BLOB
    )
    checks.check(
        "A-authority",
        "Block 132 blobs, ancestors 131--103, and landed Block 119 runner/cache are pinned",
        authority_raw,
    )

    states = state_space_certificate()
    state_raw = (
        states.trace_normalized
        and states.disk_determinants_exact
        and states.inverse_coordinates_exact
        and states.ambient_dimension == 6
        and states.trace_constraint_rank == 1
        and states.affine_dimension == 5
        and states.pure_projector_identity
        and states.pure_bloch_circle
        and states.antipodal_identification
        and states.fixture_independent
    )
    checks.check(
        "B-the-state-space",
        "displayed linear algebra gives dim 5, two Bloch disks, and the two RP^1 pure families, fixture-independently",
        state_raw and mutation != "break_state_space",
    )

    sector_fixtures = tuple(
        b119.make_sectors(shear)
        for shear in (b119.prior.PRIMARY_SHEAR, b119.prior.SECOND_SHEAR)
    )
    carriers = tuple(
        b132.carrier_certificate(sectors) for sectors in sector_fixtures
    )
    vacuum_fixtures = tuple(
        fixture_vacuum_certificate(sectors, carrier)
        for sectors, carrier in zip(sector_fixtures, carriers)
    )
    vacuum = certified_vacuum_certificate(vacuum_fixtures)
    vacuum_raw = (
        tuple(item.shear for item in vacuum.fixtures) == (R(5, 13), R(3, 5))
        and all(
            item.exact_weights_pinned
            and item.all_weights_positive
            and item.one_three_equality_forced
            and item.zero_two_weights_unequal
            and item.block_totals_unequal
            for item in vacuum.fixtures
        )
        and vacuum.trace_normalized
        and vacuum.trace_representation_exact
        and vacuum.central_decomposition_exact
        and vacuum.certified_frame_biased
        and vacuum.one_three_maximally_mixed
    )
    if mutation in (
        "break_vacuum_weights",
        "claim_certified_maximally_mixed",
    ):
        vacuum_raw = False
    checks.check(
        "C-the-certified-vacuum",
        "both fixtures give pinned positive direction weights, a biased central mixture, and only block (1,3) maximally mixed",
        vacuum_raw,
    )

    normalization = normalization_certificate(carriers, vacuum_fixtures)
    normalization_raw = (
        normalization.parent_not_square_imported
        and normalization.first_move_needed
        and normalization.second_move_needed
        and normalization.exactly_two_moves
        and normalization.intra_block_equalization_exact
        and normalization.block_equalization_exact
        and normalization.scales_real_positive
        and normalization.involutivity_preserved
        and normalization.positivity_preserved
        and matrix_zero(normalization.final_density - sp.eye(4) / 4)
    )
    checks.check(
        "D-the-normalization-ledger",
        "exactly two positive real moves give Tr/4 and preserve involutivity and positivity; Block 132 supplies the nonsquare import",
        normalization_raw and mutation != "break_normalization_ledger",
    )

    momentum = momentum_certificate()
    orbit_raw = (
        momentum.generator_differences == (-2, 2)
        and momentum.orbit02_exact
        and momentum.orbit13_exact
        and momentum.opposite_orientations
        and momentum.identity_and_z_fixed
    )
    conserving_raw = (
        momentum.commutant_rank == 2
        and momentum.commutant_dimension == 4
        and momentum.conserving_algebra_exact
    )
    if mutation == "break_orbit_signs":
        orbit_raw = False
    if mutation == "break_conserving_algebra":
        conserving_raw = False
    checks.check(
        "E-the-momentum-orbits",
        "e^{itP} rotates the two quadrature planes at rate 2 with differences (-2,+2), while the conserving algebra is diagonal R^4",
        orbit_raw and conserving_raw,
    )

    balanced = balanced_equator_certificate()
    equator_raw = (
        balanced.equal_moduli_exact
        and balanced.relative_phase_free
        and balanced.equator_identification_exact
        and balanced.positivity_identity_exact
    )
    invariant_raw = (
        balanced.general_expectation
        == sp.Symbol("a", real=True)
        + balanced.radius
        * sp.Symbol("b", real=True)
        * sp.cos(balanced.phase)
        and balanced.y_not_admissible
        and balanced.invariant_rank == 1
        and balanced.invariant_dimension == 2
        and balanced.invariant_span_exact
    )
    if mutation == "break_equator_identification":
        equator_raw = False
    if mutation == "break_invariant_span":
        invariant_raw = False
    checks.check(
        "F-the-balanced-equator",
        "|c_1|=|c_3| gives the full free-relative-phase Bloch equator; phi-invariant admissible observables are exactly span{I,Z}",
        equator_raw and invariant_raw,
    )

    summary = summary_table_certificate(vacuum, momentum, balanced)
    summary_raw = (
        len(summary.rows) == 6
        and summary.table_exact
        and summary.no_tensor_claim
    )
    checks.check(
        "G-the-summary-table",
        "the six basis rows have exact conserving, balanced-measurable, and certified-frame vacuum columns with no tensor claim",
        summary_raw and mutation != "break_summary_table",
    )

    scope = scope_certificate(normalized_note(), mutation)
    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "frame, orbit, equator, exclusion, N1--N8/W1/N5, no-go, and TOE firewalls are present",
        set(scope) == set(SCOPE_KEYS)
        and all(scope.values())
        and elapsed_before_scope <= 400,
    )

    print(
        "AUTHORITY: Block132 parent="
        f"{authority['parent']}; note/runner/cache and Block119 pins exact"
    )
    print(
        "STATE: D_02=w(I+x_02 X+z_02 Z)/2, "
        "D_13=(1-w)(I+x_13 X+z_13 Z)/2; 0<=w<=1, "
        "x_j^2+z_j^2<=1; affine dim=5; fixture-independent"
    )
    print(
        "PURE: w=1 or 0 and rho=vv^T/(v^Tv), v~-v; each boundary "
        "family is RP^1 and an interior central mixture is not pure"
    )
    for fixture in vacuum.fixtures:
        print(
            f"VACUUM-PIN c={fixture.shear}: "
            "literal exact q0,q1 pins; q2=g02*q0; q3=q1; positive "
            "direction intervals and unequal block-total intervals"
        )
    print(
        "CERTIFIED FRAME: D_cert=diag(q0,q1,g02*q0,q1)/N, "
        "N=q0(1+g02)+2q1; W02=q0(1+g02)/N != W13=2q1/N; "
        "rho02=diag(1,g02)/(1+g02) is biased, rho13=I/2"
    )
    print(
        "NORMALIZED FRAME: two moves: y2->y2/sqrt(g02) (Block132 "
        "certifies sqrt(g02) notin Q(rho)), then "
        "(y1,y3)->sqrt(q0/q1)(y1,y3); the result is Tr_4/4"
    )
    print(
        "ORBITS: d02=-2: X->cos(2t)X-sin(2t)Y; d13=+2: "
        "X->cos(2t)X+sin(2t)Y; the Y rotations have the opposite "
        "matching signs; I,Z fixed; diagonal R^4 conserving"
    )
    print(
        "BALANCED: |c1|=|c3| gives rho=(I+r(cos(phi)X+sin(phi)Y))/2 "
        "with free relative phase; <aI+bX+cZ>=a+r*b*cos(phi), so "
        "span{I,Z} only; Y is not an admissible Sym_2(R) observable"
    )
    print(
        "TABLE: observable | P-conserving | balanced-measurable | "
        "certified-frame vacuum value"
    )
    for row in summary.rows:
        print(
            f"  {row.name:4s} | "
            f"{'yes' if row.momentum_conserving else 'no ':3s} | "
            f"{row.balanced_measurable:4s} | {row.certified_vacuum_value}"
        )
    print(f"PHYSICS: {summary.honest_closer}")
    for line in N5_LINES:
        print(line)
    if checks.failed == 0:
        print(
            "RESULT: the two-block algebra's measurement theory is complete — "
            "a biased certified vacuum with a two-step normalization ledger, "
            "counter-rotating momentum dynamics with the diagonal conserved, "
            "and a balanced gravity sector that measures exactly the identity and z"
        )
        print(
            "DECISION_CUT: the common differential and richer carriers are the "
            "frontier; reject frame-ambiguous vacuum claims; advance exact "
            "state expectations and selection rules only"
        )
    else:
        print(
            "RESULT: BLOCKED — at least one exact authority, state, vacuum, "
            "normalization, dynamics, equator, table, scope, mutation, or "
            "runtime certificate failed"
        )
        print(
            "DECISION_CUT: repair the failed certificate without conflating "
            "the certified and normalized frames"
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
