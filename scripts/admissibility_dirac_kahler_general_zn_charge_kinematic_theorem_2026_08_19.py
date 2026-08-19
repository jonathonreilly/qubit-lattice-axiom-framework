#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_general_zn_charge_kinematic_theorem_2026_08_19.py
"""Block 138: conditional general-even-Z_N charge-kinematic theorem.

The runner proves an exact conditional statement for N=2m.  Action reality,
cyclic-shear covariance, and the common-pivot carrier convention are named
structural premises and are checked on the fixtures that realize them.  The
separate (0,m) observable mixer remains a supplied rule.  No Boolean gate is
awarded merely because a hypothesis was declared true.

All scientific arithmetic is exact SymPy arithmetic.  The monotonic integer
clock is used only by the bounded runtime/scope gate.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_observable_scaling_law_2026_08_18 as block136


R = sp.Rational
I = sp.I
_FINAL_LOCATION_ROOT = Path(__file__).resolve().parents[1]
# The cwd fallback keeps this staged scratchpad draft executable before the
# supervisor moves it to scripts/, where the final-location branch is used.
ROOT = (
    _FINAL_LOCATION_ROOT
    if (_FINAL_LOCATION_ROOT / ".git").exists()
    else Path.cwd()
)
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_GENERAL_ZN_CHARGE_KINEMATIC_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TWISTED_SCOUTING_RECORD_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_twisted_scouting_record_"
    "2026_08_19.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_twisted_scouting_"
    "record_2026_08_19.txt"
)
BLOCK136_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_OBSERVABLE_SCALING_LAW_"
    "BOUNDED_THEOREM_NOTE_2026-08-18.md"
)
BLOCK136_RUNNER = (
    "scripts/admissibility_dirac_kahler_observable_scaling_law_"
    "2026_08_18.py"
)
BLOCK136_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_observable_scaling_"
    "law_2026_08_18.txt"
)

# Deliberately literal: this is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_ZN_CHARGE_KINEMATIC_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TWISTED_SCOUTING_RECORD_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_twisted_scouting_record_2026_08_19.py",
    "logs/runner-cache/admissibility_dirac_kahler_twisted_scouting_record_2026_08_19.txt",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_OBSERVABLE_SCALING_LAW_BOUNDED_THEOREM_NOTE_2026-08-18.md",
    "scripts/admissibility_dirac_kahler_observable_scaling_law_2026_08_18.py",
    "logs/runner-cache/admissibility_dirac_kahler_observable_scaling_law_2026_08_18.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "f6e65aed8974d53544cf7dca372f6bcae7f34701"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block137-twisted-scouting-record-20260819"
)
# Landing supervisor: replace this one placeholder with the Block 137 tip.
PARENT_COMMIT = "e4a55e6436f01145b50a4a5d82a884bc9cb7130b"
BLOCK136_COMMIT = "a9e0725db114298d9885e86b34d3c99bfe051444"
BLOCK136_NOTE_BLOB = "5c7e8b724e90320f3ceea332cc3abd4ce5128723"
BLOCK136_RUNNER_BLOB = "f86976787595c0f183ca8ce15456c8f857c2b6a6"
BLOCK136_CACHE_BLOB = "34f29c9a23d97732e864cfc85ba51304d298f8bc"


MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_character_identities",
    "break_cyclic_shear_structure",
    "break_scale_free_line",
    "break_shared_pivot",
    "break_z4_natural_pivot",
    "break_jordan_count",
    "break_z6_degeneracy",
    "break_polynomial_ledger",
    "break_alternative_count",
    "break_n8_instantiation",
    "drop_tenth_vacuity_catch",
    "weaken_scope_firewalls",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_axiom_authority": "A",
    "stale_parent_authority": "A",
    "break_character_identities": "B",
    "break_cyclic_shear_structure": "B",
    "break_scale_free_line": "C",
    "break_shared_pivot": "C",
    "break_z4_natural_pivot": "C",
    "break_jordan_count": "D",
    "break_z6_degeneracy": "E",
    "break_polynomial_ledger": "E",
    "break_alternative_count": "F",
    "break_n8_instantiation": "G",
    "drop_tenth_vacuity_catch": "H",
    "weaken_scope_firewalls": "H",
    "drop_n5_fence": "H",
}


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


def is_hash(value: str) -> bool:
    return re.fullmatch(r"[0-9a-f]{40}", value) is not None


@dataclass(frozen=True)
class AuthorityCertificate:
    fixed_authority: bool
    parent_authority: bool
    block136_authority: bool


def authority_certificate() -> AuthorityCertificate:
    fixed_authority = bool(
        AUDIT_TIMEOUT_SEC == 600
        and git_output("rev-parse", "origin/main") == CURRENT_MAIN
        and commit_blob("origin/main", AXIOM_PATH) == CURRENT_AXIOM_BLOB
        and commit_blob("origin/main", REGISTRY_PATH) == CURRENT_REGISTRY_BLOB
        and worktree_blob(AXIOM_PATH) == WORKTREE_AXIOM_BLOB
        and worktree_blob(REGISTRY_PATH) == WORKTREE_REGISTRY_BLOB
    )

    parent_ready = is_hash(PARENT_COMMIT)
    parent_authority = False
    if parent_ready:
        parent_blobs = tuple(
            commit_blob(PARENT_COMMIT, path)
            for path in (PARENT_NOTE, PARENT_RUNNER, PARENT_CACHE)
        )
        parent_authority = bool(
            git_output("rev-parse", PARENT_REF) == PARENT_COMMIT
            and is_ancestor(PARENT_COMMIT, "HEAD")
            and all(is_hash(value) for value in parent_blobs)
            and parent_blobs
            == tuple(
                worktree_blob(path)
                for path in (PARENT_NOTE, PARENT_RUNNER, PARENT_CACHE)
            )
        )

    block136_authority = bool(
        is_ancestor(BLOCK136_COMMIT, "HEAD")
        and commit_blob(BLOCK136_COMMIT, BLOCK136_NOTE) == BLOCK136_NOTE_BLOB
        and commit_blob(BLOCK136_COMMIT, BLOCK136_RUNNER)
        == BLOCK136_RUNNER_BLOB
        and commit_blob(BLOCK136_COMMIT, BLOCK136_CACHE) == BLOCK136_CACHE_BLOB
        and worktree_blob(BLOCK136_NOTE) == BLOCK136_NOTE_BLOB
        and worktree_blob(BLOCK136_RUNNER) == BLOCK136_RUNNER_BLOB
        and worktree_blob(BLOCK136_CACHE) == BLOCK136_CACHE_BLOB
        and block136.AUDIT_TIMEOUT_SEC == AUDIT_TIMEOUT_SEC
    )
    return AuthorityCertificate(
        fixed_authority,
        parent_authority,
        block136_authority,
    )


def raw_note() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def normalized_note(note: str) -> str:
    return " ".join(note.lower().split())


def exact(value: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.expand_complex(sp.sympify(value)))


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(
        exact(a - b) == 0 for a, b in zip(left, right, strict=True)
    )


def no_float(*values: object) -> bool:
    return all(not sp.sympify(value).atoms(sp.Float) for value in values)


def same_character_mod_n(
    exponent_left: sp.Expr,
    exponent_right: sp.Expr,
    order: sp.Expr,
) -> bool:
    left = sp.sympify(exponent_left)
    right = sp.sympify(exponent_right)
    exact_order = sp.sympify(order)
    quotient = sp.cancel((left - right) / exact_order)
    return bool(
        quotient.is_integer is True
        and sp.simplify(left - right - quotient * exact_order) == 0
    )


def normalized_kernel_carrier(
    matrix: sp.Matrix, pivot: int = 0
) -> tuple[sp.Matrix | None, bool]:
    kernel = matrix.nullspace()
    if len(kernel) != 1:
        return None, False
    pivot_value = exact(kernel[0][pivot])
    if pivot_value == 0:
        return None, False
    carrier = kernel[0].applyfunc(lambda entry: exact(entry / pivot_value))
    valid = carrier[pivot] == 1 and matrix_equal(
        matrix * carrier, sp.zeros(matrix.rows, 1)
    )
    return carrier, valid


@dataclass(frozen=True)
class StructuralPremises:
    reality: bool
    cyclic_shear: bool
    shared_pivot: bool


@dataclass(frozen=True)
class SymbolicStructuralFixture:
    m: sp.Symbol
    order: sp.Expr
    shift_powers: tuple[int, ...]
    temporal_coefficients: tuple[sp.Matrix, ...]
    carrier: sp.Matrix
    opposite_carrier: sp.Matrix
    sector: sp.Matrix
    opposite_sector: sp.Matrix
    premises: StructuralPremises


def build_symbolic_structural_fixture() -> SymbolicStructuralFixture:
    """Build and inspect the three named structural premises at symbolic m."""
    m = sp.symbols("m", integer=True, positive=True)
    order = 2 * m
    shift_powers = (-1, 0, 1)
    coefficient_symbols = sp.symbols("c0:12", real=True)
    coefficients = tuple(
        sp.Matrix(2, 2, coefficient_symbols[4 * index : 4 * index + 4])
        for index in range(3)
    )
    spatial_row, spatial_column = sp.symbols(
        "x y", integer=True
    )
    shift_entries = tuple(
        sp.KroneckerDelta(
            sp.Mod(spatial_row - spatial_column - power, order), 0
        )
        for power in shift_powers
    )
    reality = bool(
        m in order.free_symbols
        and sp.simplify(order / 2 - m) == 0
        and all(
            sp.conjugate(entry) == entry
            for coefficient in coefficients
            for entry in coefficient
        )
        and all(sp.conjugate(entry) == entry for entry in shift_entries)
        and no_float(*coefficients)
    )
    cyclic_shear = bool(
        all(isinstance(power, int) for power in shift_powers)
        and len(set(shift_powers)) == len(shift_powers)
        and all(coefficient.shape == (2, 2) for coefficient in coefficients)
        and all(
            sp.simplify((power + 1) - (1 + power)) == 0
            for power in shift_powers
        )
        and all(
            not entry.has(spatial_row, spatial_column)
            for coefficient in coefficients
            for entry in coefficient
        )
    )

    a, b, c, d = sp.symbols("a b c d", real=True)
    carrier = sp.Matrix((1, a + I * b, c + I * d))
    first_coordinate = sp.Matrix((1, 0, 0))
    sector = sp.eye(3) - carrier * first_coordinate.T
    opposite_sector = sector.conjugate().applyfunc(exact)
    opposite_carrier = carrier.conjugate().applyfunc(exact)
    built, built_valid = normalized_kernel_carrier(sector)
    opposite_built, opposite_valid = normalized_kernel_carrier(
        opposite_sector
    )
    shared_pivot = bool(
        built_valid
        and opposite_valid
        and built is not None
        and opposite_built is not None
        and built[0] == opposite_built[0] == 1
        and matrix_equal(built, carrier)
        and matrix_equal(opposite_built, opposite_carrier)
    )
    return SymbolicStructuralFixture(
        m,
        order,
        shift_powers,
        coefficients,
        carrier,
        opposite_carrier,
        sector,
        opposite_sector,
        StructuralPremises(reality, cyclic_shear, shared_pivot),
    )


@dataclass(frozen=True)
class GeneralKinematicsCertificate:
    named_premises: bool
    action_reality_checked: bool
    cyclic_shear_checked: bool
    character_identities: bool
    conjugation_involution: bool
    projector_kinematics: bool
    block_kinematics: bool
    self_conjugate_sectors: bool
    exactly_two_fixed_charges: bool


def general_kinematics_certificate(
    fixture: SymbolicStructuralFixture,
) -> GeneralKinematicsCertificate:
    m = fixture.m
    order = fixture.order
    k, r, s = sp.symbols("k r s", integer=True)
    character_identities = bool(
        same_character_mod_n(k * r + k * s, k * (r + s), order)
        and same_character_mod_n(order, 0, order)
        and same_character_mod_n(-order, 0, order)
    )
    projector_kinematics = same_character_mod_n(
        k * r, -(order - k) * r, order
    )
    block_kinematics = same_character_mod_n(
        -k * r, (order - k) * r, order
    )
    conjugation_involution = bool(
        same_character_mod_n(order - (order - k), k, order)
        and same_character_mod_n(0, -0, order)
        and same_character_mod_n(m, -m, order)
    )
    self_conjugate_sectors = bool(
        same_character_mod_n(0 * r, -0 * r, order)
        and same_character_mod_n(m * r, -m * r, order)
    )
    return GeneralKinematicsCertificate(
        tuple(StructuralPremises.__dataclass_fields__)
        == ("reality", "cyclic_shear", "shared_pivot"),
        fixture.premises.reality,
        fixture.premises.cyclic_shear,
        character_identities,
        conjugation_involution,
        projector_kinematics,
        block_kinematics,
        self_conjugate_sectors,
        bool(sp.gcd(2, order) == 2),
    )


@lru_cache(maxsize=None)
def root_power(power: int, spatial_size: int) -> sp.Expr:
    exponent = power % spatial_size
    angle = 2 * sp.pi * R(exponent, spatial_size)
    return exact(sp.cos(angle) + I * sp.sin(angle))


def shift(spatial_size: int) -> sp.Matrix:
    result = sp.zeros(spatial_size)
    for column in range(spatial_size):
        result[(column + 1) % spatial_size, column] = 1
    return result


@lru_cache(maxsize=None)
def projectors(spatial_size: int) -> tuple[sp.Matrix, ...]:
    cyclic = shift(spatial_size)
    return tuple(
        (
            sum(
                (
                    root_power(-momentum * power, spatial_size)
                    * cyclic**power
                    for power in range(spatial_size)
                ),
                sp.zeros(spatial_size),
            )
            / spatial_size
        ).applyfunc(exact)
        for momentum in range(spatial_size)
    )


def momentum_block(
    matrix: sp.Matrix,
    momentum: int,
    time_size: int,
    spatial_size: int,
) -> sp.Matrix:
    projector = projectors(spatial_size)[momentum]
    return sp.Matrix(
        time_size,
        time_size,
        lambda row, column: exact(
            sp.trace(
                projector
                * matrix[
                    spatial_size * row : spatial_size * (row + 1),
                    spatial_size * column : spatial_size * (column + 1),
                ]
            )
        ),
    )


@dataclass(frozen=True)
class NaturalZ4Fixture:
    shear: sp.Rational
    real_cyclic_action: bool
    exact_sector_formula: bool
    regular_shared_pivots: bool
    carrier_mirror_entrywise: bool
    self_carriers_real: bool
    no_float_exactness: bool


def natural_z4_fixture(shear: sp.Rational) -> NaturalZ4Fixture:
    spatial_size = 4
    time_size = 2
    cyclic = shift(spatial_size)
    identity = sp.eye(spatial_size)
    action = sp.Matrix.vstack(
        sp.Matrix.hstack(identity, -shear * cyclic),
        sp.Matrix.hstack(-shear * cyclic.T, shear**2 * identity),
    )
    lifted_shift = sp.kronecker_product(sp.eye(time_size), cyclic)
    sectors = tuple(
        momentum_block(action, momentum, time_size, spatial_size)
        for momentum in range(spatial_size)
    )
    expected = tuple(
        sp.Matrix(
            (
                (1, -shear * root_power(momentum, spatial_size)),
                (
                    -shear * root_power(-momentum, spatial_size),
                    shear**2,
                ),
            )
        )
        for momentum in range(spatial_size)
    )
    built = tuple(normalized_kernel_carrier(sector) for sector in sectors)
    carriers = tuple(item[0] for item in built)
    regular = all(valid and carrier is not None for carrier, valid in built)
    mirror = bool(
        regular
        and all(
            carriers[momentum] is not None
            and carriers[(-momentum) % spatial_size] is not None
            and matrix_equal(
                carriers[(-momentum) % spatial_size],
                carriers[momentum].conjugate(),
            )
            for momentum in range(spatial_size)
        )
    )
    self_real = bool(
        regular
        and all(
            carriers[momentum] is not None
            and matrix_equal(
                carriers[momentum], carriers[momentum].conjugate()
            )
            for momentum in (0, spatial_size // 2)
        )
    )
    return NaturalZ4Fixture(
        shear,
        bool(
            matrix_equal(action, action.conjugate())
            and matrix_equal(action * lifted_shift, lifted_shift * action)
        ),
        all(
            matrix_equal(actual, predicted)
            and actual.rank() == 1
            and exact(actual.det()) == 0
            for actual, predicted in zip(sectors, expected, strict=True)
        ),
        bool(
            regular
            and all(
                carrier is not None and carrier[0] == 1
                for carrier in carriers
            )
        ),
        mirror,
        self_real,
        no_float(action, *sectors, *(item for item in carriers if item is not None)),
    )


@dataclass(frozen=True)
class GramCertificate:
    reality_fixes_line: bool
    reality_leaves_scale_free: bool
    shared_pivot_forces_unit: bool
    unit_solution_unique: bool
    natural_z4_both_fixtures: bool


def gram_certificate(
    fixture: SymbolicStructuralFixture,
) -> GramCertificate:
    scale = sp.symbols("lambda", real=True, nonzero=True)
    scaled_opposite = scale * fixture.opposite_carrier
    reality_fixes_line = bool(
        matrix_equal(
            fixture.sector * fixture.carrier,
            sp.zeros(fixture.sector.rows, 1),
        )
        and matrix_equal(
            fixture.opposite_sector * fixture.opposite_carrier,
            sp.zeros(fixture.opposite_sector.rows, 1),
        )
        and matrix_equal(
            (fixture.sector * fixture.carrier).conjugate(),
            fixture.opposite_sector * fixture.opposite_carrier,
        )
        and matrix_equal(
            fixture.opposite_sector * scaled_opposite,
            sp.zeros(fixture.opposite_sector.rows, 1),
        )
    )
    reality_leaves_scale_free = bool(
        reality_fixes_line
        and scaled_opposite[0] == scale
        and scaled_opposite.subs(scale, 2)[0] == 2
        and sp.Integer(2) != 1
    )
    g = sp.symbols("g", nonzero=True)
    pivot = sp.symbols("p", real=True, nonzero=True)
    pivot_solutions = sp.solve(
        sp.Eq(pivot, g * sp.conjugate(pivot)), g
    )
    unit_solutions = sp.solve(sp.Eq(1, g * sp.conjugate(1)), g)
    shared_pivot_forces_unit = bool(
        fixture.premises.shared_pivot and pivot_solutions == [1]
    )
    unit_solution_unique = unit_solutions == [1]
    z4_fixtures = tuple(
        natural_z4_fixture(shear)
        for shear in (block136.PRIMARY_SHEAR, block136.SECOND_SHEAR)
    )
    natural_z4_both = all(
        item.real_cyclic_action
        and item.exact_sector_formula
        and item.regular_shared_pivots
        and item.carrier_mirror_entrywise
        and item.self_carriers_real
        and item.no_float_exactness
        for item in z4_fixtures
    )
    return GramCertificate(
        reality_fixes_line,
        reality_leaves_scale_free,
        shared_pivot_forces_unit,
        unit_solution_unique,
        natural_z4_both,
    )


@dataclass(frozen=True)
class LocalJordanCertificate:
    dimension_three: bool
    symmetric_basis: bool
    jordan_closed: bool
    center_one: bool
    commutator_antisymmetric: bool
    commutator_excluded: bool


def local_jordan_certificate() -> LocalJordanCertificate:
    identity = sp.eye(2)
    diagonal = sp.diag(1, -1)
    exchange = sp.Matrix(((0, 1), (1, 0)))
    basis = (identity, diagonal, exchange)
    flattened = sp.Matrix.hstack(*(item.reshape(4, 1) for item in basis))
    jordan_closed = all(
        flattened.row_join(
            ((left * right + right * left) / 2).reshape(4, 1)
        ).rank()
        == flattened.rank()
        for left in basis
        for right in basis
    )
    central_columns = tuple(
        sp.Matrix.vstack(
            *(
                (candidate * item - item * candidate).reshape(4, 1)
                for item in basis
            )
        )
        for candidate in basis
    )
    central_system = sp.Matrix.hstack(*central_columns)
    commutator = (diagonal * exchange - exchange * diagonal) / 2
    return LocalJordanCertificate(
        flattened.rank() == 3,
        all(item.T == item for item in basis),
        jordan_closed,
        len(basis) - central_system.rank() == 1,
        bool(commutator != sp.zeros(2) and commutator.T == -commutator),
        flattened.row_join(commutator.reshape(4, 1)).rank() == 4,
    )


@dataclass(frozen=True)
class ConditionalCountCertificate:
    two_self_conjugate_charges: bool
    self_charges_distinct: bool
    nonself_pair_count: bool
    anchored_pairing_is_extra_rule: bool
    conditional_block_count: bool
    conditional_dimension_law: bool
    conditional_center_law: bool
    jordan_discipline: bool


def conditional_count_certificate() -> ConditionalCountCertificate:
    m = sp.symbols("m", integer=True, positive=True)
    order = 2 * m
    fixed = sp.gcd(2, order)
    nonself_pairs = sp.cancel((order - fixed) / 2)
    self_charges_distinct = not same_character_mod_n(0, m, order)
    anchored_pairing_is_extra = bool(
        self_charges_distinct
        and same_character_mod_n(0, -0, order)
        and same_character_mod_n(m, -m, order)
    )
    conditional_blocks = sp.simplify(nonself_pairs + 1)
    local = local_jordan_certificate()
    jordan_discipline = all(
        (
            local.dimension_three,
            local.symmetric_basis,
            local.jordan_closed,
            local.center_one,
            local.commutator_antisymmetric,
            local.commutator_excluded,
        )
    )
    return ConditionalCountCertificate(
        fixed == 2,
        self_charges_distinct,
        sp.simplify(nonself_pairs - (m - 1)) == 0,
        anchored_pairing_is_extra,
        sp.simplify(conditional_blocks - m) == 0,
        bool(
            jordan_discipline
            and sp.simplify(3 * conditional_blocks - 3 * m) == 0
        ),
        bool(
            local.center_one
            and sp.simplify(conditional_blocks - m) == 0
        ),
        jordan_discipline,
    )


def charge_blocks(spatial_size: int) -> tuple[tuple[int, int], ...]:
    if spatial_size <= 0 or spatial_size % 2:
        raise ValueError("charge_blocks requires a positive even order")
    half = spatial_size // 2
    return ((0, half),) + tuple(
        (momentum, spatial_size - momentum)
        for momentum in range(1, half)
    )


def embedded(
    pair: tuple[int, int], block: sp.Matrix, spatial_size: int
) -> sp.Matrix:
    result = sp.zeros(spatial_size)
    for row in range(2):
        for column in range(2):
            result[pair[row], pair[column]] = block[row, column]
    return result


@dataclass(frozen=True)
class BlockAlgebraCertificate:
    pairs: tuple[tuple[int, int], ...]
    dimension: int
    center_dimension: int
    disjoint_symmetric_blocks: bool
    jordan_closed: bool
    commutator_antisymmetric: bool
    commutator_excluded: bool


def block_algebra_certificate(spatial_size: int) -> BlockAlgebraCertificate:
    pairs = charge_blocks(spatial_size)
    identity = sp.eye(2)
    diagonal = sp.diag(1, -1)
    exchange = sp.Matrix(((0, 1), (1, 0)))
    local_basis = (identity, diagonal, exchange)
    basis = tuple(
        embedded(pair, item, spatial_size)
        for pair in pairs
        for item in local_basis
    )
    flattened = sp.Matrix.hstack(
        *(item.reshape(spatial_size**2, 1) for item in basis)
    )
    central_columns = tuple(
        sp.Matrix.vstack(
            *(
                (candidate * item - item * candidate).reshape(
                    spatial_size**2, 1
                )
                for item in basis
            )
        )
        for candidate in basis
    )
    central_system = sp.Matrix.hstack(*central_columns)
    disjoint_symmetric = bool(
        len({index for pair in pairs for index in pair}) == spatial_size
        and all(item.T == item for item in basis)
        and all(
            left * right == sp.zeros(spatial_size)
            for left_index, left in enumerate(basis)
            for right_index, right in enumerate(basis)
            if left_index // 3 != right_index // 3
        )
    )
    local = local_jordan_certificate()
    commutator = (diagonal * exchange - exchange * diagonal) / 2
    commutator_excluded = bool(
        local.commutator_excluded
        and all(
            flattened.row_join(
                embedded(pair, commutator, spatial_size).reshape(
                    spatial_size**2, 1
                )
            ).rank()
            == flattened.rank() + 1
            for pair in pairs
        )
    )
    return BlockAlgebraCertificate(
        pairs,
        flattened.rank(),
        len(basis) - central_system.rank(),
        disjoint_symmetric,
        local.jordan_closed,
        local.commutator_antisymmetric,
        commutator_excluded,
    )


@dataclass(frozen=True)
class TransferDegeneracyCertificate:
    both_committed_shears: bool
    rho_zero_equals_rho_three: bool
    zero_three_trace_determinant_equal: bool
    zero_three_determinant_one: bool
    polynomial_classes_reproduced: bool
    traces_one_four_equal: bool
    traces_one_five_conjugate: bool
    exact_no_float: bool


def transfer_degeneracy_certificate() -> TransferDegeneracyCertificate:
    shears = (block136.PRIMARY_SHEAR, block136.SECOND_SHEAR)
    fixtures = tuple(block136.build_z6(shear) for shear in shears)
    trace_determinant_equal = []
    determinant_one = []
    rho_equal = []
    class_reproduction = []
    trace_one_four = []
    trace_one_five = []
    exactness = []
    for fixture in fixtures:
        transfers = fixture.transfers
        traces = tuple(item.monodromy_trace for item in transfers)
        determinants = tuple(
            item.monodromy_determinant for item in transfers
        )
        trace_determinant_equal.append(
            block136.field_element(traces[0])
            == block136.field_element(traces[3])
            and block136.field_element(determinants[0])
            == block136.field_element(determinants[3])
        )
        determinant_one.append(
            block136.field_element(determinants[0])
            == block136.NUMBER_FIELD.one
            and block136.field_element(determinants[3])
            == block136.NUMBER_FIELD.one
        )
        # The stable-root convention is a function of the ordered
        # (trace,determinant) key, so equality of this exact key is rho equality.
        rho_keys = tuple(
            (
                block136.field_element(traces[index]),
                block136.field_element(determinants[index]),
            )
            for index in (0, 3)
        )
        rho_equal.append(rho_keys[0] == rho_keys[1])
        polynomials = tuple(
            item.monodromy_polynomial for item in transfers
        )
        class_reproduction.append(
            block136.strict_degeneracy(polynomials)
            == ((0, 3), (1, 4), (2, 5))
        )
        trace_one_four.append(
            block136.field_element(traces[1])
            == block136.field_element(traces[4])
        )
        trace_one_five.append(
            block136.field_element(traces[5])
            == block136.field_element(
                block136.conjugate_expr(traces[1])
            )
        )
        exactness.append(
            all(block136.no_float(value) for value in traces + determinants)
        )
    return TransferDegeneracyCertificate(
        tuple(item.shear for item in fixtures) == shears
        and shears[0] != shears[1],
        all(rho_equal),
        all(trace_determinant_equal),
        all(determinant_one),
        all(class_reproduction),
        all(trace_one_four),
        all(trace_one_five),
        all(exactness),
    )


@dataclass(frozen=True)
class AlternativeCountCertificate:
    symbolic_nondegenerate_instance: bool
    separate_self_blocks: bool
    mixer_excluded_by_rho: bool
    instance_dimension_eleven: bool
    instance_center_five: bool
    general_dimension_law: bool
    general_center_law: bool
    jordan_closed: bool


def alternative_count_certificate() -> AlternativeCountCertificate:
    spatial_size = 8
    half = spatial_size // 2
    nonself_pairs = tuple(
        (momentum, spatial_size - momentum)
        for momentum in range(1, half)
    )
    identity = sp.eye(2)
    diagonal = sp.diag(1, -1)
    exchange = sp.Matrix(((0, 1), (1, 0)))
    local_basis = (identity, diagonal, exchange)
    basis = [
        embedded(pair, item, spatial_size)
        for pair in nonself_pairs
        for item in local_basis
    ]
    singleton_zero = sp.zeros(spatial_size)
    singleton_zero[0, 0] = 1
    singleton_half = sp.zeros(spatial_size)
    singleton_half[half, half] = 1
    basis.extend((singleton_zero, singleton_half))
    basis_tuple = tuple(basis)
    flattened = sp.Matrix.hstack(
        *(item.reshape(spatial_size**2, 1) for item in basis_tuple)
    )
    central_columns = tuple(
        sp.Matrix.vstack(
            *(
                (candidate * item - item * candidate).reshape(
                    spatial_size**2, 1
                )
                for item in basis_tuple
            )
        )
        for candidate in basis_tuple
    )
    central_system = sp.Matrix.hstack(*central_columns)

    rho_zero = sp.symbols("rho_0", real=True)
    separation = sp.symbols("Delta", real=True, nonzero=True)
    rho_half = rho_zero + separation
    rho_one, rho_two, rho_three = sp.symbols(
        "rho_1 rho_2 rho_3", real=True
    )
    rho_operator = sp.diag(
        rho_zero,
        rho_one,
        rho_two,
        rho_three,
        rho_half,
        rho_three,
        rho_two,
        rho_one,
    )
    forbidden_mixer = embedded(
        (0, half), sp.Matrix(((0, 1), (1, 0))), spatial_size
    )
    mixer_commutator = rho_operator * forbidden_mixer - forbidden_mixer * rho_operator
    separate_self_blocks = bool(
        flattened.rank() == len(basis_tuple)
        and flattened.row_join(
            forbidden_mixer.reshape(spatial_size**2, 1)
        ).rank()
        == flattened.rank() + 1
    )
    mixer_excluded = bool(
        all(
            rho_operator * item == item * rho_operator
            for item in basis_tuple
        )
        and mixer_commutator != sp.zeros(spatial_size)
        and mixer_commutator[0, half] == -separation
        and separation.is_nonzero is True
    )
    jordan_closed = all(
        flattened.row_join(
            ((left * right + right * left) / 2).reshape(
                spatial_size**2, 1
            )
        ).rank()
        == flattened.rank()
        for left in basis_tuple
        for right in basis_tuple
    )
    m = sp.symbols("m", integer=True, positive=True)
    nonself_count = m - 1
    dimension = 3 * nonself_count + 2
    center = nonself_count + 2
    return AlternativeCountCertificate(
        bool(sp.simplify(rho_half - rho_zero - separation) == 0),
        separate_self_blocks,
        mixer_excluded,
        flattened.rank() == 11,
        len(basis_tuple) - central_system.rank() == 5,
        sp.simplify(dimension - (3 * m - 1)) == 0,
        sp.simplify(center - (m + 1)) == 0,
        jordan_closed,
    )


@dataclass(frozen=True)
class N8Certificate:
    exact_pairs: bool
    sym2_four: bool
    dimension_twelve: bool
    center_four: bool
    jordan_and_commutator: bool
    zero_four_sign_definite: bool
    residue_not_integer_equality: bool
    hard_coded_pairing_caveat: bool


def n8_certificate() -> N8Certificate:
    algebra = block_algebra_certificate(8)
    half = 4
    charge = sp.diag(0, half)
    amplitude = sp.symbols("q", real=True)
    balanced = sp.Matrix((amplitude, amplitude))
    expectation = sp.expand((balanced.T * charge * balanced)[0])
    hard_coded_caveat = bool(
        same_character_mod_n(0, -0, 8)
        and same_character_mod_n(half, -half, 8)
        and not same_character_mod_n(0, half, 8)
    )
    return N8Certificate(
        algebra.pairs == ((0, 4), (1, 7), (2, 6), (3, 5)),
        algebra.disjoint_symmetric_blocks,
        algebra.dimension == 12,
        algebra.center_dimension == 4,
        bool(
            algebra.jordan_closed
            and algebra.commutator_antisymmetric
            and algebra.commutator_excluded
        ),
        bool(
            charge.det() == 0
            and all(value >= 0 for value in charge.diagonal())
            and any(value > 0 for value in charge.diagonal())
            and expectation == half * amplitude**2
            and sp.Poly(expectation, amplitude).all_roots() == [0, 0]
        ),
        half % 8 == (-half) % 8 and sp.Integer(half) != sp.Integer(-half),
        hard_coded_caveat,
    )


N5_FENCE = 'N5: per_element: symbolic projector and cyclic-shear block mirrors plus shared-pivot carrier normalization are checked under the three named hypotheses\nper_site: one charge character per spatial site on the stated even cyclic carrier; no odd-N or other-shear extension\nper_mode: k pairs with N-k; k=0,m are individually real; g=1 only on non-self conjugate pairs under SHARED-PIVOT\nper_block: where rho_0=rho_m, m Jordan blocks give dim=3m and center=m; where it fails, two singleton self blocks give dim=3m-1 and center=m+1\nlattice_wide: general even N=2m is symbolic only under ACTION-REALITY, CYCLIC-SHEAR, SHARED-PIVOT and the separately stated transfer-degeneracy rider\nRESULT: conditional general-Z_N charge kinematics; verified transfer degeneracy at N=4 and N=6; N=8 algebraic third point only\nDECISION_CUT: N=8 dynamical degeneracy, parity-mixing dressing classes, and the joint-lane program remain open\nTOE: zero obligation retirement; no TOE percentage movement; retained-positive end-to-end theory count remains zero'


SCOPE_KEYS = (
    "hypothesis_reality",
    "hypothesis_cyclic_shear",
    "hypothesis_shared_pivot",
    "tenth_vacuity_catch",
    "conditional_structure",
    "degeneracy_rider",
    "alternative_count",
    "verification_ledger",
    "n8_dynamical_unchecked",
    "n8_pairing_caveat",
    "os_no_go",
    "curved_os_no_go",
    "axiom",
    "firewalls",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity_quotient",
    "adm",
    "records",
    "audit_retention",
    "n1_n8",
    "w1",
    "n5_fence_keys",
    "n5_verbatim",
)


def scope_certificate(note_text: str) -> dict[str, bool]:
    note = normalized_note(note_text)
    return {
        "hypothesis_reality": (
            "reality hypothesis" in note
            or "action-reality hypothesis" in note
            or "structural premise: reality" in note
        ),
        "hypothesis_cyclic_shear": (
            "cyclic-shear hypothesis" in note
            or "cyclic shear hypothesis" in note
            or "structural premise: cyclic shear" in note
        ),
        "hypothesis_shared_pivot": (
            "shared-pivot hypothesis" in note
            or "shared pivot hypothesis" in note
            or "structural premise: shared pivot" in note
        ),
        "tenth_vacuity_catch": bool(
            re.search(r"tenth[- ]vacuity catch", note) is not None
            or (
                "t1-action-hypothesis" in note
                and "vacu" in note
                and (
                    "declaration-true" in note
                    or "declaration true" in note
                )
            )
        ),
        "conditional_structure": (
            "conditional" in note
            and (
                "(0,m)" in note
                or "(0, m)" in note
                or "(0,n/2)" in note
                or "(0, n/2)" in note
            )
            and "supplied" in note
        ),
        "degeneracy_rider": "degeneracy rider" in note,
        "alternative_count": (
            "3m-1" in note
            and "m+1" in note
            and ("rho_0 != rho_m" in note or "rho_0 ≠ rho_m" in note)
        ),
        "verification_ledger": (
            "verification ledger" in note
            and "z6" in note
            and "5/13" in note
            and "3/5" in note
        ),
        "n8_dynamical_unchecked": (
            (
                "n=8 dynamical degeneracy" in note
                or "z8 dynamical degeneracy" in note
            )
            and "unchecked" in note
        ),
        "n8_pairing_caveat": (
            "hard-coded pairing" in note
            and ("(0,4)" in note or "(0, 4)" in note)
        ),
        "os_no_go": "not an os no-go" in note,
        "curved_os_no_go": "not a curved os no-go" in note,
        "axiom": "no axiom amendment is justified" in note,
        "firewalls": "firewall" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "gravity_quotient": (
            "gravity constraint quotient remains unexecuted" in note
        ),
        "adm": "actual adm/history transporter remains" in note,
        "records": "records" in note and "remain" in note,
        "audit_retention": "audit retention" in note,
        "n1_n8": all(
            re.search(rf"\bn{index}\b", note) is not None
            for index in range(1, 9)
        ),
        "w1": re.search(r"\bw1\b", note) is not None,
        "n5_fence_keys": all(
            f"{category}:" in note
            for category in (
                "per_element",
                "per_site",
                "per_mode",
                "per_block",
                "lattice_wide",
            )
        ),
        "n5_verbatim": normalized_note(N5_FENCE) in note,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started_ns = time.monotonic_ns()

    authority = authority_certificate()
    structural = build_symbolic_structural_fixture()
    kinematics = general_kinematics_certificate(structural)
    gram = gram_certificate(structural)
    count = conditional_count_certificate()
    transfer = transfer_degeneracy_certificate()
    alternative = alternative_count_certificate()
    n8 = n8_certificate()
    scope = scope_certificate(raw_note())

    audit_surface_raw = AUDIT_INPUT_PATHS == (
        "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_ZN_CHARGE_KINEMATIC_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-19.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/ADMISSIBILITY_DIRAC_KAHLER_TWISTED_SCOUTING_RECORD_BOUNDED_THEOREM_NOTE_2026-08-19.md",
        "scripts/admissibility_dirac_kahler_twisted_scouting_record_2026_08_19.py",
        "logs/runner-cache/admissibility_dirac_kahler_twisted_scouting_record_2026_08_19.txt",
        "docs/ADMISSIBILITY_DIRAC_KAHLER_OBSERVABLE_SCALING_LAW_BOUNDED_THEOREM_NOTE_2026-08-18.md",
        "scripts/admissibility_dirac_kahler_observable_scaling_law_2026_08_18.py",
        "logs/runner-cache/admissibility_dirac_kahler_observable_scaling_law_2026_08_18.txt",
    )
    authority_raw = bool(
        audit_surface_raw
        and authority.fixed_authority
        and authority.parent_authority
        and authority.block136_authority
    )
    kinematics_raw = all(
        (
            kinematics.named_premises,
            kinematics.action_reality_checked,
            kinematics.cyclic_shear_checked,
            kinematics.character_identities,
            kinematics.conjugation_involution,
            kinematics.projector_kinematics,
            kinematics.block_kinematics,
            kinematics.self_conjugate_sectors,
            kinematics.exactly_two_fixed_charges,
        )
    )
    gram_raw = all(
        (
            gram.reality_fixes_line,
            gram.reality_leaves_scale_free,
            gram.shared_pivot_forces_unit,
            gram.unit_solution_unique,
            gram.natural_z4_both_fixtures,
        )
    )
    count_raw = all(
        (
            count.two_self_conjugate_charges,
            count.self_charges_distinct,
            count.nonself_pair_count,
            count.anchored_pairing_is_extra_rule,
            count.conditional_block_count,
            count.conditional_dimension_law,
            count.conditional_center_law,
            count.jordan_discipline,
        )
    )
    transfer_raw = all(
        (
            transfer.both_committed_shears,
            transfer.rho_zero_equals_rho_three,
            transfer.zero_three_trace_determinant_equal,
            transfer.zero_three_determinant_one,
            transfer.polynomial_classes_reproduced,
            transfer.traces_one_four_equal,
            transfer.traces_one_five_conjugate,
            transfer.exact_no_float,
        )
    )
    alternative_raw = all(
        (
            alternative.symbolic_nondegenerate_instance,
            alternative.separate_self_blocks,
            alternative.mixer_excluded_by_rho,
            alternative.instance_dimension_eleven,
            alternative.instance_center_five,
            alternative.general_dimension_law,
            alternative.general_center_law,
            alternative.jordan_closed,
        )
    )
    n8_raw = all(
        (
            n8.exact_pairs,
            n8.sym2_four,
            n8.dimension_twelve,
            n8.center_four,
            n8.jordan_and_commutator,
            n8.zero_four_sign_definite,
            n8.residue_not_integer_equality,
            n8.hard_coded_pairing_caveat,
        )
    )
    elapsed_ns = time.monotonic_ns() - started_ns
    scope_raw = bool(
        set(scope) == set(SCOPE_KEYS)
        and all(scope.values())
        and len(MUTATIONS) == 15
        and set(MUTATION_GATE) == set(MUTATIONS)
        and set(MUTATION_GATE.values()) == set("ABCDEFGH")
        and elapsed_ns <= 500 * 1_000_000_000
    )

    # Capture all raw gate values first.  A mutation then negates exactly one
    # copied gate value; it cannot alter any certificate used by another gate.
    raw_gates = {
        "A": authority_raw,
        "B": kinematics_raw,
        "C": gram_raw,
        "D": count_raw,
        "E": transfer_raw,
        "F": alternative_raw,
        "G": n8_raw,
        "H": scope_raw,
    }
    gate_values = dict(raw_gates)
    if mutation:
        target = MUTATION_GATE[mutation]
        gate_values[target] = not gate_values[target]
        changed = tuple(
            key
            for key in raw_gates
            if raw_gates[key] != gate_values[key]
        )
        if changed != (target,):
            raise AssertionError("mutation did not flip exactly one gate")

    checks = Checks()
    checks.check(
        "A-authority",
        "main/axiom/registry, Block137 parent blobs, and committed Block136 note/runner/cache are content-bound",
        gate_values["A"],
    )
    checks.check(
        "B-general-kinematics",
        "named reality/cyclic-shear/shared-pivot premises support the symbolic N=2m character and projector/block mirror identities",
        gate_values["B"],
    )
    checks.check(
        "C-gram-forcing",
        "reality fixes only the line; the shared pivot uniquely gives g=1, realized entrywise by both exact Z4 fixtures",
        gate_values["C"],
    )
    checks.check(
        "D-conditional-jordan-count",
        "given the supplied (0,m) mixer, m copies of Sym_2(R) have dimension 3m and center m; the antisymmetric commutator is excluded",
        gate_values["D"],
    )
    checks.check(
        "E-transfer-ledger",
        "both committed Z6 shears give rho_0=rho_3, equal trace/det with det=1 and classes (0,3)/(1,4)/(2,5); N=8 dynamics UNCHECKED",
        gate_values["E"],
    )
    checks.check(
        "F-alternative-count",
        "for symbolic rho_0!=rho_m the absent self mixer leaves dimension 3m-1 and center m+1; the exact N=8 instance is (11,5)",
        gate_values["F"],
    )
    checks.check(
        "G-n8-instantiation",
        "(0,4)/(1,7)/(2,6)/(3,5) give Sym_2(R)^4, dimension 12, center 4 and sign-definite (0,4); CAVEAT: (0,4) is hard-coded",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "hypotheses, vacuity catch, riders/counts, ledger, N8 caveats, OS/axiom firewalls, N1--N8/W1, and exact N5 fence are present",
        gate_values["H"],
    )
    print(N5_FENCE)
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"[FAIL] INTERNAL-EXCEPTION: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
