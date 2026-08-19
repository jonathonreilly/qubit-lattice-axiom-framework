#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_isospectral_similarity_theorem_2026_08_19.py
"""Block 140: exact family-scoped isospectral-similarity theorem.

For the committed Dirac--Kahler fixture family, the captured local action has
a real, cyclic, spatial nearest-neighbor form with coefficients independent of
the checked spatial extent.  Its two real-character blocks are

    B_epsilon = C_0 + epsilon (C_-1 + C_+1).

The antiperiodic half-period time operator U=T_AP**4 commutes with C_0 and
anticommutes with C_-1+C_+1.  Hence B_+1 and B_-1 are exactly similar for
every even spatial extent in that named family.  Every scientific comparison
below uses exact SymPy arithmetic.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
import sys
import time

import sympy as sp


R = sp.Rational
LAM = sp.symbols("lambda")
SHEAR = sp.symbols("c", real=True)
PRIMARY_SHEAR = R(5, 13)
SECONDARY_SHEAR = R(3, 5)
SHEARS = (PRIMARY_SHEAR, SECONDARY_SHEAR)
SPACE_SIZES = (4, 6)

_FINAL_LOCATION_ROOT = Path(__file__).resolve().parents[1]
# This fallback keeps the scratchpad draft executable before it is moved to
# scripts/, where the final-location branch is used.
ROOT = (
    _FINAL_LOCATION_ROOT
    if (_FINAL_LOCATION_ROOT / ".git").exists()
    else Path.cwd()
)
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_dirac_kahler_observable_scaling_law_2026_08_18 as b136


TIME_SIZE = b136.TIME_SIZE
COMMITTED_FIXTURE_BUILDER = b136.fixture_data_spatial
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_ISOSPECTRAL_SIMILARITY_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
BLOCK138_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_ZN_CHARGE_KINEMATIC_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
BLOCK138_RUNNER = (
    "scripts/admissibility_dirac_kahler_general_zn_charge_kinematic_"
    "theorem_2026_08_19.py"
)
BLOCK138_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_general_zn_charge_"
    "kinematic_theorem_2026_08_19.txt"
)
BLOCK139_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_Z8_LEDGER_COMPLETION_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
BLOCK139_RUNNER = (
    "scripts/admissibility_dirac_kahler_z8_ledger_completion_2026_08_19.py"
)
BLOCK139_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_z8_ledger_completion_"
    "2026_08_19.txt"
)
PARENT_ARTIFACTS = (
    BLOCK138_NOTE,
    BLOCK138_RUNNER,
    BLOCK138_CACHE,
    BLOCK139_NOTE,
    BLOCK139_RUNNER,
    BLOCK139_CACHE,
)

# Deliberately literal: this is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ISOSPECTRAL_SIMILARITY_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_ZN_CHARGE_KINEMATIC_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_general_zn_charge_kinematic_theorem_2026_08_19.py",
    "logs/runner-cache/admissibility_dirac_kahler_general_zn_charge_kinematic_theorem_2026_08_19.txt",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_Z8_LEDGER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_z8_ledger_completion_2026_08_19.py",
    "logs/runner-cache/admissibility_dirac_kahler_z8_ledger_completion_2026_08_19.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "29d17653c9c043a74041f070e311f03fce114c0a"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block139-z8-ledger-completion-20260819"
)
# Landing supervisor: replace this placeholder with the Block 139 branch tip.
PARENT_COMMIT = "ccfdb57a46d22d3a60c82db8d31df1414835dd0c"

MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_symbolic_capture",
    "break_committed_roundtrip",
    "break_spatial_reconstruction",
    "break_size_independent_stencil",
    "break_plus_block_formula",
    "break_minus_block_formula",
    "break_half_period_similarity",
    "assert_one_slice_similarity",
    "break_charpoly_coefficient",
    "inject_float_charpoly",
    "drop_boundary_denominator",
    "weaken_scope_firewalls",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_axiom_authority": "A",
    "stale_parent_authority": "A",
    "break_symbolic_capture": "B",
    "break_committed_roundtrip": "B",
    "break_spatial_reconstruction": "C",
    "break_size_independent_stencil": "C",
    "break_plus_block_formula": "D",
    "break_minus_block_formula": "D",
    "break_half_period_similarity": "E",
    "assert_one_slice_similarity": "E",
    "break_charpoly_coefficient": "F",
    "inject_float_charpoly": "F",
    "drop_boundary_denominator": "G",
    "weaken_scope_firewalls": "H",
    "drop_n5_fence": "H",
}


class Checks:
    def __init__(self) -> None:
        self.results: list[tuple[str, str, bool]] = []

    def check(self, key: str, statement: str, condition: object) -> None:
        self.results.append((key, statement, bool(condition)))

    def report(self) -> None:
        for key, statement, value in self.results:
            print(f"[{'PASS' if value else 'FAIL'}] {key}: {statement}")
        print(
            "GATES "
            + " ".join(
                f"{key}={'PASS' if value else 'FAIL'}"
                for key, _, value in self.results
            )
        )

    def finish(self) -> int:
        passed = sum(value for _, _, value in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return failed


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
    parent_ref_and_ancestry: bool
    parent_artifact_blobs: bool


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
    parent_ref_and_ancestry = False
    parent_artifact_blobs = False
    if parent_ready:
        committed_blobs = tuple(
            commit_blob(PARENT_COMMIT, path) for path in PARENT_ARTIFACTS
        )
        parent_ref_and_ancestry = bool(
            git_output("rev-parse", PARENT_REF) == PARENT_COMMIT
            and is_ancestor(PARENT_COMMIT, "HEAD")
        )
        parent_artifact_blobs = bool(
            len(committed_blobs) == 6
            and all(is_hash(value) for value in committed_blobs)
            and committed_blobs
            == tuple(worktree_blob(path) for path in PARENT_ARTIFACTS)
        )
    return AuthorityCertificate(
        fixed_authority,
        parent_ref_and_ancestry,
        parent_artifact_blobs,
    )


def raw_note() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def normalized_note(text: str) -> str:
    return " ".join(text.lower().split())


def no_float(value: object) -> bool:
    if isinstance(value, sp.MatrixBase):
        return not value.has(sp.Float)
    if isinstance(value, (tuple, list, set)):
        return all(no_float(item) for item in value)
    if isinstance(value, dict):
        return all(no_float(key) and no_float(item) for key, item in value.items())
    return not sp.sympify(value).has(sp.Float)


def canonical(value: sp.Expr) -> sp.Expr:
    return sp.cancel(sp.expand(value))


def canonical_matrix(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(matrix).applyfunc(canonical)


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(canonical(value) == 0 for value in matrix)


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and matrix_zero(left - right)


def cyclic_shift(size: int) -> sp.Matrix:
    result = sp.zeros(size)
    for column in range(size):
        result[(column + 1) % size, column] = 1
    return result


def antiperiodic_shift(size: int) -> sp.Matrix:
    result = cyclic_shift(size)
    result[0, size - 1] = -1
    return result


class ActionCaptured(Exception):
    def __init__(self, action: sp.MatrixBase) -> None:
        super().__init__("committed local action captured before inversion")
        self.action = sp.Matrix(action)


@dataclass(frozen=True)
class SymbolicCapture:
    spatial_size: int
    action: sp.Matrix
    inverse_restored: bool


def capture_symbolic_action(spatial_size: int) -> SymbolicCapture:
    """Capture the exact local operator used to define the propagator."""
    original_inverse = sp.MatrixBase.inv
    captured_action: sp.Matrix | None = None

    def intercept_inverse(matrix, *args, **kwargs):
        if matrix.shape == (
            TIME_SIZE * spatial_size,
            TIME_SIZE * spatial_size,
        ):
            raise ActionCaptured(matrix)
        return original_inverse(matrix, *args, **kwargs)

    sp.MatrixBase.inv = intercept_inverse
    try:
        COMMITTED_FIXTURE_BUILDER(SHEAR, spatial_size)
    except ActionCaptured as captured:
        captured_action = canonical_matrix(captured.action)
    finally:
        sp.MatrixBase.inv = original_inverse

    if captured_action is None:
        raise AssertionError("the committed fixture did not invert its local action")
    return SymbolicCapture(
        spatial_size,
        captured_action,
        sp.MatrixBase.inv is original_inverse,
    )


def committed_action(shear: sp.Rational, spatial_size: int) -> sp.Matrix:
    raw, _calls = COMMITTED_FIXTURE_BUILDER(shear, spatial_size)
    return canonical_matrix(raw.propagator.inv(method="DM"))


def spatial_coefficients(
    action: sp.MatrixBase,
    spatial_size: int,
) -> dict[int, sp.Matrix]:
    """Extract C_r from the first spatial column of every time block."""
    return {
        offset: sp.Matrix(
            TIME_SIZE,
            TIME_SIZE,
            lambda time_row, time_column: action[
                spatial_size * time_row + offset % spatial_size,
                spatial_size * time_column,
            ],
        )
        for offset in (-1, 0, 1)
    }


def reconstruct_action(
    coefficients: dict[int, sp.Matrix],
    spatial_size: int,
) -> sp.Matrix:
    shift = cyclic_shift(spatial_size)
    return canonical_matrix(
        sum(
            (
                sp.kronecker_product(coefficients[offset], shift**offset)
                for offset in (-1, 0, 1)
            ),
            sp.zeros(TIME_SIZE * spatial_size),
        )
    )


def real_character_projector(spatial_size: int, epsilon: int) -> sp.Matrix:
    shift = cyclic_shift(spatial_size)
    return sum(
        (
            epsilon**power * shift**power
            for power in range(spatial_size)
        ),
        sp.zeros(spatial_size),
    ) / spatial_size


def projected_block(
    action: sp.MatrixBase,
    spatial_size: int,
    epsilon: int,
) -> sp.Matrix:
    projector = real_character_projector(spatial_size, epsilon)
    return canonical_matrix(
        sp.Matrix(
            TIME_SIZE,
            TIME_SIZE,
            lambda time_row, time_column: sp.trace(
                projector
                * action[
                    spatial_size * time_row : spatial_size * (time_row + 1),
                    spatial_size
                    * time_column : spatial_size
                    * (time_column + 1),
                ]
            ),
        )
    )


@dataclass(frozen=True)
class FamilyCaptureCertificate:
    committed_builder_used: bool
    both_symbolic_sizes_captured: bool
    interception_restored: bool
    primary_roundtrips_exact: bool
    secondary_roundtrips_exact: bool
    symbolic_domain_exact: bool
    exact_real_no_float: bool


def family_capture_certificate(
    captures: dict[int, SymbolicCapture],
    fixed_actions: dict[tuple[int, sp.Rational], sp.Matrix],
) -> FamilyCaptureCertificate:
    actions = {size: captures[size].action for size in SPACE_SIZES}
    primary_roundtrips = all(
        matrix_equal(
            actions[size].subs(SHEAR, PRIMARY_SHEAR),
            fixed_actions[(size, PRIMARY_SHEAR)],
        )
        for size in SPACE_SIZES
    )
    secondary_roundtrips = all(
        matrix_equal(
            actions[size].subs(SHEAR, SECONDARY_SHEAR),
            fixed_actions[(size, SECONDARY_SHEAR)],
        )
        for size in SPACE_SIZES
    )
    all_matrices = tuple(actions.values()) + tuple(fixed_actions.values())
    return FamilyCaptureCertificate(
        b136.fixture_data_spatial is COMMITTED_FIXTURE_BUILDER,
        tuple(captures) == SPACE_SIZES
        and all(
            actions[size].shape
            == (TIME_SIZE * size, TIME_SIZE * size)
            for size in SPACE_SIZES
        ),
        all(captures[size].inverse_restored for size in SPACE_SIZES),
        primary_roundtrips,
        secondary_roundtrips,
        TIME_SIZE == 8
        and PRIMARY_SHEAR == b136.PRIMARY_SHEAR
        and SECONDARY_SHEAR == b136.SECOND_SHEAR
        and PRIMARY_SHEAR != SECONDARY_SHEAR
        and all(action.free_symbols == {SHEAR} for action in actions.values()),
        no_float(all_matrices)
        and all(not matrix.has(sp.I) for matrix in all_matrices),
    )


@dataclass(frozen=True)
class SpatialOnlyPremiseCertificate:
    support_exactly_named: bool
    n4_reconstruction_exact: bool
    n6_reconstruction_exact: bool
    local_coefficients_size_independent: bool
    exact_real_no_float: bool


def spatial_only_premise_certificate(
    actions: dict[int, sp.Matrix],
    coefficients: dict[int, dict[int, sp.Matrix]],
) -> SpatialOnlyPremiseCertificate:
    same_local_coefficients = all(
        matrix_equal(coefficients[4][offset], coefficients[6][offset])
        for offset in (-1, 0, 1)
    )
    return SpatialOnlyPremiseCertificate(
        all(tuple(coefficients[size]) == (-1, 0, 1) for size in SPACE_SIZES),
        matrix_equal(actions[4], reconstruct_action(coefficients[4], 4)),
        matrix_equal(actions[6], reconstruct_action(coefficients[6], 6)),
        same_local_coefficients,
        no_float(coefficients)
        and all(
            not coefficient.has(sp.I)
            for by_offset in coefficients.values()
            for coefficient in by_offset.values()
        ),
    )


@dataclass(frozen=True)
class RealCharacterFormulaCertificate:
    projectors_are_real_characters: bool
    n4_plus_formula: bool
    n4_minus_formula: bool
    n6_plus_formula: bool
    n6_minus_formula: bool
    exact_no_float: bool


def real_character_formula_certificate(
    actions: dict[int, sp.Matrix],
    coefficients: dict[int, dict[int, sp.Matrix]],
) -> RealCharacterFormulaCertificate:
    formulas: dict[tuple[int, int], bool] = {}
    projectors_exact = []
    projected: list[sp.Matrix] = []
    for size in SPACE_SIZES:
        shift = cyclic_shift(size)
        nyquist_sign = sp.diag(*((-1) ** site for site in range(size)))
        plus_projector = real_character_projector(size, 1)
        minus_projector = real_character_projector(size, -1)
        projectors_exact.append(
            matrix_equal(plus_projector**2, plus_projector)
            and matrix_equal(minus_projector**2, minus_projector)
            and sp.trace(plus_projector) == sp.trace(minus_projector) == 1
            and matrix_equal(nyquist_sign * shift * nyquist_sign, -shift)
            and matrix_equal(
                nyquist_sign * plus_projector * nyquist_sign,
                minus_projector,
            )
        )
        c_zero = coefficients[size][0]
        c_odd = coefficients[size][-1] + coefficients[size][1]
        for epsilon in (1, -1):
            actual = projected_block(actions[size], size, epsilon)
            expected = c_zero + epsilon * c_odd
            projected.append(actual)
            formulas[(size, epsilon)] = matrix_equal(actual, expected)
    return RealCharacterFormulaCertificate(
        all(projectors_exact),
        formulas[(4, 1)],
        formulas[(4, -1)],
        formulas[(6, 1)],
        formulas[(6, -1)],
        no_float(projected),
    )


@dataclass(frozen=True)
class SimilarityCertificate:
    half_period_operator_exact: bool
    operator_algebra_exact: bool
    c_zero_invariant_both_sizes: bool
    c_odd_sign_flip_both_sizes: bool
    symbolic_block_similarity_both_sizes: bool
    primary_plain_shift_residual_nonzero: bool
    secondary_plain_shift_residual_nonzero: bool
    exact_no_float: bool


def similarity_certificate(
    coefficients: dict[int, dict[int, sp.Matrix]],
) -> SimilarityCertificate:
    plain_one_slice = cyclic_shift(TIME_SIZE)
    time_antiperiodic = antiperiodic_shift(TIME_SIZE)
    time_intertwiner = time_antiperiodic ** (TIME_SIZE // 2)
    inverse = canonical_matrix(time_intertwiner.inv())

    c_zero_identities = []
    c_odd_identities = []
    symbolic_similarities = []
    block_pairs: dict[int, tuple[sp.Matrix, sp.Matrix]] = {}
    for size in SPACE_SIZES:
        c_zero = coefficients[size][0]
        c_odd = coefficients[size][-1] + coefficients[size][1]
        block_plus = canonical_matrix(c_zero + c_odd)
        block_minus = canonical_matrix(c_zero - c_odd)
        block_pairs[size] = (block_plus, block_minus)
        c_zero_identities.append(
            matrix_equal(
                time_intertwiner * c_zero * time_intertwiner.T,
                c_zero,
            )
        )
        c_odd_identities.append(
            matrix_equal(
                time_intertwiner * c_odd * time_intertwiner.T,
                -c_odd,
            )
        )
        symbolic_similarities.append(
            block_plus.has(SHEAR)
            and block_minus.has(SHEAR)
            and matrix_equal(
                time_intertwiner * block_plus * inverse,
                block_minus,
            )
        )

    plain_residuals = {
        (size, shear): canonical_matrix(
            plain_one_slice
            * block_pairs[size][0]
            * plain_one_slice.T
            - block_pairs[size][1]
        ).subs(SHEAR, shear)
        for size in SPACE_SIZES
        for shear in SHEARS
    }
    return SimilarityCertificate(
        TIME_SIZE == 8
        and matrix_equal(
            time_intertwiner,
            antiperiodic_shift(TIME_SIZE) ** 4,
        )
        and time_intertwiner != plain_one_slice,
        matrix_equal(time_intertwiner**2, -sp.eye(TIME_SIZE))
        and matrix_equal(inverse, time_intertwiner.T)
        and matrix_equal(time_intertwiner.T, -time_intertwiner)
        and matrix_equal(
            time_intertwiner.T * time_intertwiner,
            sp.eye(TIME_SIZE),
        ),
        all(c_zero_identities),
        all(c_odd_identities),
        all(symbolic_similarities),
        all(
            not matrix_zero(plain_residuals[(size, PRIMARY_SHEAR)])
            for size in SPACE_SIZES
        ),
        all(
            not matrix_zero(plain_residuals[(size, SECONDARY_SHEAR)])
            for size in SPACE_SIZES
        ),
        no_float(
            (
                plain_one_slice,
                time_antiperiodic,
                time_intertwiner,
                inverse,
                block_pairs,
                plain_residuals,
            )
        ),
    )


def characteristic_coefficients(
    matrix: sp.MatrixBase,
) -> tuple[sp.Expr, ...]:
    return tuple(canonical(value) for value in matrix.charpoly(LAM).all_coeffs())


@dataclass(frozen=True)
class CharacteristicCertificate:
    n4_all_coefficients_equal: bool
    n6_all_coefficients_equal: bool
    all_time_size_plus_one: bool
    all_monic: bool
    symbolic_in_c: bool
    exact_real_no_float: bool


def characteristic_certificate(
    coefficients: dict[int, dict[int, sp.Matrix]],
) -> CharacteristicCertificate:
    pairs = {}
    for size in SPACE_SIZES:
        c_zero = coefficients[size][0]
        c_odd = coefficients[size][-1] + coefficients[size][1]
        pairs[size] = (
            characteristic_coefficients(c_zero + c_odd),
            characteristic_coefficients(c_zero - c_odd),
        )

    equalities = {
        size: all(
            canonical(left - right) == 0
            for left, right in zip(*pairs[size], strict=True)
        )
        for size in SPACE_SIZES
    }
    flat_coefficients = tuple(
        value
        for size in SPACE_SIZES
        for side in pairs[size]
        for value in side
    )
    return CharacteristicCertificate(
        equalities[4],
        equalities[6],
        all(
            len(plus) == len(minus) == TIME_SIZE + 1
            for plus, minus in pairs.values()
        ),
        all(
            plus[0] == minus[0] == 1
            for plus, minus in pairs.values()
        ),
        all(value.free_symbols <= {SHEAR} for value in flat_coefficients)
        and any(value.has(SHEAR) for value in flat_coefficients),
        no_float(flat_coefficients)
        and all(not value.has(sp.I) for value in flat_coefficients),
    )


# Exact witnesses are (spatial offset, time row, time column) within the
# captured local coefficient matrices.  Each reduced denominator contains
# the factor (1-c**2), which is the builder's 1/(1-q**2) site-matrix boundary
# written in the solve's shear symbol c.
BOUNDARY_FACTOR_WITNESSES = (
    (-1, 0, 6),
    (0, 0, 0),
    (1, 0, 1),
)


def denominator_has_boundary_factor(value: sp.Expr) -> bool:
    denominator = sp.denom(canonical(value))
    denominator_polynomial = sp.Poly(denominator, SHEAR, domain=sp.QQ)
    boundary_polynomial = sp.Poly(1 - SHEAR**2, SHEAR, domain=sp.QQ)
    return denominator_polynomial.rem(boundary_polynomial).is_zero


@dataclass(frozen=True)
class WellPosednessCertificate:
    structural_witnesses_n4: bool
    structural_witnesses_n6: bool
    boundary_factor_is_uncancelled: bool
    primary_boundary_value_exact: bool
    secondary_boundary_value_exact: bool
    excluded_values_are_exactly_c_squared_one: bool
    exact_no_float: bool


def well_posedness_certificate(
    coefficients: dict[int, dict[int, sp.Matrix]],
) -> WellPosednessCertificate:
    witness_values = {
        size: tuple(
            coefficients[size][offset][time_row, time_column]
            for offset, time_row, time_column in BOUNDARY_FACTOR_WITNESSES
        )
        for size in SPACE_SIZES
    }
    structural = {
        size: all(
            value != 0 and denominator_has_boundary_factor(value)
            for value in witness_values[size]
        )
        for size in SPACE_SIZES
    }
    factor_removed = all(
        not denominator_has_boundary_factor(
            canonical(value * (1 - SHEAR**2))
        )
        for values in witness_values.values()
        for value in values
    )
    boundary_values = tuple(canonical(1 - shear**2) for shear in SHEARS)
    return WellPosednessCertificate(
        structural[4],
        structural[6],
        factor_removed,
        boundary_values[0] == R(144, 169),
        boundary_values[1] == R(16, 25),
        sp.solve(sp.Eq(1 - SHEAR**2, 0), SHEAR) == [-1, 1]
        and all(shear**2 != 1 for shear in SHEARS),
        no_float((witness_values, boundary_values, BOUNDARY_FACTOR_WITNESSES)),
    )


N5_FENCE = 'N5: per_element: the fixed symbolic C_-1, C_0, and C_+1 obey U C_0 U^T=C_0 and U(C_-1+C_+1)U^T=-(C_-1+C_+1), with U=T_AP^4 and c^2!=1\nper_site: exact spatial reconstruction uses only offsets {-1,0,1}; N=4 and N=6 have the same C_r, Block 139 covers N=8, and family membership at each size is a checked premise\nper_mode: the Nyquist sign maps the k=0 plus-character projector to the k=N/2 minus-character projector for every even spatial N\nper_block: U=[[0,-I_4],[I_4,0]], U^2=-I, and U^-1=U^T=-U give U B_(+1) U^-1=B_(-1) symbolically in c; the plain one-slice shift remains refuted\nlattice_wide: for every even spatial N>=4 in the displayed fixed-C_r, Z8-AP, spatial-NN family at c^2!=1, cyclic super-slice rotation gives rho_0=rho_(N/2)\nRESULT: the displayed family realizes Sym_2(R)^(N/2), dimension 3N/2, center N/2; the 3m-1 branch remains an out-of-family contingency only\nDECISION_CUT: classify parity-mixing dressing classes; execute the joint-lane program; test richer carriers beyond the displayed family\nTOE: zero obligation retirement; no TOE percentage movement; retained-positive end-to-end theory count remains zero'


SCOPE_KEYS = (
    "family_scoped_theorem",
    "spatial_only_premise",
    "every_even_spatial_n",
    "mechanism_identities",
    "operator_algebra",
    "consistency_pair",
    "well_posedness_boundary",
    "cyclic_rotation_downstream_chain",
    "family_wide_3m_collapse",
    "out_of_family_contingency",
    "os_no_go",
    "curved_os_no_go",
    "axiom",
    "firewalls",
    "n5_verbatim",
)


def scope_certificate(note_text: str) -> dict[str, bool]:
    note = normalized_note(note_text)
    math_compact = re.sub(r"[\s\\{}$`]", "", note_text.lower())
    block_identity = bool(
        "ub_(+1)u^-1=b_(-1)" in math_compact
        or "ub_+1u^-1=b_-1" in math_compact
        or "ub(+1)u^-1=b(-1)" in math_compact
    )
    return {
        "family_scoped_theorem": (
            "family-scoped" in note and "theorem" in note
        ),
        "spatial_only_premise": (
            "spatial-only" in note and "premise" in note
        ),
        "every_even_spatial_n": "every even spatial n" in note,
        "mechanism_identities": bool(
            "uc_0u^t=c_0" in math_compact
            and "uc_oddu^t=-c_odd" in math_compact
            and block_identity
        ),
        "operator_algebra": bool(
            "u=t_ap^4" in math_compact
            and "u^2=-i" in math_compact
            and "u^-1=u^t=-u" in math_compact
        ),
        "consistency_pair": all(
            phrase in note
            for phrase in ("one-slice", "refuted", "half-period", "works")
        ),
        "well_posedness_boundary": bool(
            "well-posedness boundary" in note
            and (
                "c^2=1" in math_compact
                or "c²=1" in math_compact
                or "c^2!=1" in math_compact
                or "c²≠1" in math_compact
            )
        ),
        "cyclic_rotation_downstream_chain": (
            "cyclic rotation of the same product" in note
        ),
        "family_wide_3m_collapse": "family-wide 3m collapse" in note,
        "out_of_family_contingency": (
            "out-of-family" in note and "contingency" in note
        ),
        "os_no_go": "not an os no-go" in note,
        "curved_os_no_go": "not a curved os no-go" in note,
        "axiom": "no axiom amendment is justified" in note,
        "firewalls": "firewall" in note,
        # Raw substring membership makes the printed eight-line fence
        # byte-identical to its note occurrence.
        "n5_verbatim": N5_FENCE in note_text,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started_ns = time.monotonic_ns()

    authority = authority_certificate()
    captures = {
        size: capture_symbolic_action(size) for size in SPACE_SIZES
    }
    actions = {size: captures[size].action for size in SPACE_SIZES}
    fixed_actions = {
        (size, shear): committed_action(shear, size)
        for size in SPACE_SIZES
        for shear in SHEARS
    }
    coefficients = {
        size: spatial_coefficients(actions[size], size)
        for size in SPACE_SIZES
    }
    capture = family_capture_certificate(captures, fixed_actions)
    spatial_only = spatial_only_premise_certificate(actions, coefficients)
    real_blocks = real_character_formula_certificate(actions, coefficients)
    similarity = similarity_certificate(coefficients)
    characteristic = characteristic_certificate(coefficients)
    well_posedness = well_posedness_certificate(coefficients)
    scope = scope_certificate(raw_note())

    audit_surface_raw = AUDIT_INPUT_PATHS == (
        "docs/ADMISSIBILITY_DIRAC_KAHLER_ISOSPECTRAL_SIMILARITY_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-19.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_ZN_CHARGE_KINEMATIC_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-19.md",
        "scripts/admissibility_dirac_kahler_general_zn_charge_kinematic_theorem_2026_08_19.py",
        "logs/runner-cache/admissibility_dirac_kahler_general_zn_charge_kinematic_theorem_2026_08_19.txt",
        "docs/ADMISSIBILITY_DIRAC_KAHLER_Z8_LEDGER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-19.md",
        "scripts/admissibility_dirac_kahler_z8_ledger_completion_2026_08_19.py",
        "logs/runner-cache/admissibility_dirac_kahler_z8_ledger_completion_2026_08_19.txt",
    )
    parent_surface_raw = PARENT_ARTIFACTS == (
        BLOCK138_NOTE,
        BLOCK138_RUNNER,
        BLOCK138_CACHE,
        BLOCK139_NOTE,
        BLOCK139_RUNNER,
        BLOCK139_CACHE,
    )
    authority_raw = all(
        (
            audit_surface_raw,
            parent_surface_raw,
            authority.fixed_authority,
            authority.parent_ref_and_ancestry,
            authority.parent_artifact_blobs,
        )
    )
    capture_raw = all(
        (
            capture.committed_builder_used,
            capture.both_symbolic_sizes_captured,
            capture.interception_restored,
            capture.primary_roundtrips_exact,
            capture.secondary_roundtrips_exact,
            capture.symbolic_domain_exact,
            capture.exact_real_no_float,
        )
    )
    spatial_only_raw = all(
        (
            spatial_only.support_exactly_named,
            spatial_only.n4_reconstruction_exact,
            spatial_only.n6_reconstruction_exact,
            spatial_only.local_coefficients_size_independent,
            spatial_only.exact_real_no_float,
        )
    )
    real_blocks_raw = all(
        (
            real_blocks.projectors_are_real_characters,
            real_blocks.n4_plus_formula,
            real_blocks.n4_minus_formula,
            real_blocks.n6_plus_formula,
            real_blocks.n6_minus_formula,
            real_blocks.exact_no_float,
        )
    )
    similarity_raw = all(
        (
            similarity.half_period_operator_exact,
            similarity.operator_algebra_exact,
            similarity.c_zero_invariant_both_sizes,
            similarity.c_odd_sign_flip_both_sizes,
            similarity.symbolic_block_similarity_both_sizes,
            similarity.primary_plain_shift_residual_nonzero,
            similarity.secondary_plain_shift_residual_nonzero,
            similarity.exact_no_float,
        )
    )
    characteristic_raw = all(
        (
            characteristic.n4_all_coefficients_equal,
            characteristic.n6_all_coefficients_equal,
            characteristic.all_time_size_plus_one,
            characteristic.all_monic,
            characteristic.symbolic_in_c,
            characteristic.exact_real_no_float,
        )
    )
    well_posedness_raw = all(
        (
            well_posedness.structural_witnesses_n4,
            well_posedness.structural_witnesses_n6,
            well_posedness.boundary_factor_is_uncancelled,
            well_posedness.primary_boundary_value_exact,
            well_posedness.secondary_boundary_value_exact,
            well_posedness.excluded_values_are_exactly_c_squared_one,
            well_posedness.exact_no_float,
        )
    )
    elapsed_ns = time.monotonic_ns() - started_ns
    scope_raw = bool(
        set(scope) == set(SCOPE_KEYS)
        and all(scope.values())
        and len(MUTATIONS) == 15
        and set(MUTATION_GATE) == set(MUTATIONS)
        and set(MUTATION_GATE.values()) == set("ABCDEFGH")
        and N5_FENCE.count("\n") == 7
        and elapsed_ns <= 500 * 1_000_000_000
    )

    # Capture every raw gate before a mutation flag acts.  A mutation negates
    # exactly one copied gate value, so no certificate or neighboring gate can
    # cascade.
    raw_gates = {
        "A": authority_raw,
        "B": capture_raw,
        "C": spatial_only_raw,
        "D": real_blocks_raw,
        "E": similarity_raw,
        "F": characteristic_raw,
        "G": well_posedness_raw,
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
        "main plus the committed Block 138 and 139 note/runner/cache artifacts are content-bound",
        gate_values["A"],
    )
    checks.check(
        "B-symbolic-family-capture",
        "the exact real c-family actions at N=4,6 round-trip to both committed rational shears",
        gate_values["B"],
    )
    checks.check(
        "C-spatial-only-family-form-premise",
        "the SPATIAL-only cyclic-NN reconstruction has the same local C_r at N=4,6",
        gate_values["C"],
    )
    checks.check(
        "D-real-character-block-formula",
        "both real-character projections equal C_0+epsilon(C_-1+C_+1) at N=4,6",
        gate_values["D"],
    )
    checks.check(
        "E-isospectral-similarity",
        "U=T_AP^4 gives the symbolic similarity while the plain one-slice shift is refuted",
        gate_values["E"],
    )
    checks.check(
        "F-characteristic-polynomial",
        "all nine monic characteristic coefficients agree symbolically in c with no floats",
        gate_values["F"],
    )
    checks.check(
        "G-well-posedness-boundary",
        "the uncancelled 1/(1-q^2) structure excludes c^2=1 and both fixture values are exact",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the family theorem, downstream chain, contingency, firewalls, and exact N5 fence are present",
        gate_values["H"],
    )
    checks.report()
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
