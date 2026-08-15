#!/usr/bin/env python3
"""Block 107: exact ADM-seam two-history Gram obstruction packet.

The flat antiperiodic reflection torus reproduces the calibrated Block 104
Gram exactly.  The transfer-derived shear channel, its two forced flat seam
anchors, the raw two-history Gram defects, and the exhaustion of a cell-local
plus nearest-neighbor dressing ansatz are then checked over exact rationals.
This is a bounded seam-mechanism result, not a curved OS no-go or completion
of the actual ADM/history transporter.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_LOCAL_DUAL_PATCH_DESCENT_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_local_dual_patch_descent_"
    "2026_08_15.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_local_dual_patch_descent_"
    "2026_08_15.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_LOCAL_DUAL_PATCH_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "scripts/admissibility_dirac_kahler_local_dual_patch_descent_2026_08_15.py",
    "logs/runner-cache/admissibility_dirac_kahler_local_dual_patch_descent_2026_08_15.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "9714c638b6be7c730e35552a2497b71107b9d8cd"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_COMMIT = "22d6d90ec2279e5868c9c825149b2a20beea3797"
PARENT_NOTE_BLOB = "a08c8d5381e5bfac52f23d28fa6ffd05adf81697"
PARENT_RUNNER_BLOB = "2d82838197b6ee0324fec40cc4a5823e09a2468f"
PARENT_CACHE_BLOB = "d845d15e140d33a60d34bbebf462870be45c9c8b"
ANCESTOR_105 = "d06066c2b908aaca0779625d831dfb10620cf34d"
ANCESTOR_104 = "7fe07db6c03fad1191893c942f708c5cb9a54c43"
ANCESTOR_103 = "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"


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
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
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


I = sp.I
LX = 4
OFFSETS = ((0, 0), (0, 1), (1, 0), (1, 1))


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    if left.shape != right.shape:
        return False
    return all(sp.expand(entry) == 0 for entry in left - right)


def matrix_simplify_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    if left.shape != right.shape:
        return False
    return all(sp.simplify(entry) == 0 for entry in left - right)


def parity(integer: int) -> sp.Integer:
    return sp.Integer(1 if integer % 2 == 0 else -1)


def max_abs_entry(matrix: sp.Matrix) -> sp.Expr:
    values = [sp.simplify(sp.Abs(entry)) for entry in matrix]
    return max(values, default=sp.Integer(0))


def h_site(shear: sp.Expr, volume: sp.Expr) -> sp.Matrix:
    metric = sp.Matrix([[1, shear], [shear, 1]])
    return sp.diag(volume, volume * metric.inv(), 1 / volume)


def flat_chain(mass: sp.Expr, eigenvalue: sp.Expr, half: int) -> sp.Matrix:
    # Sites t=-half,...,half-1 are mapped to index t+half.
    size = 2 * half
    operator = sp.zeros(size, size)
    for time in range(-half, half):
        index = time + half
        operator[index, index] = mass + I * parity(time) * eigenvalue
        if time + 1 < half:
            operator[index, index + 1] = sp.Rational(1, 2)
        if time - 1 >= -half:
            operator[index, index - 1] = -sp.Rational(1, 2)
    return operator


def torus_objects(
    mass: sp.Expr,
    field_c: dict[int, sp.Expr],
    volume: sp.Expr,
    half_time: int,
    boundary_sign: int,
    spatial_extent: int = LX,
) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix, object]:
    """Build the exact Z_(2*half_time) x Z_spatial_extent overlap objects."""
    size = 2 * half_time * spatial_extent

    def site_index(time: int, space: int) -> int:
        return ((time + half_time) % (2 * half_time)) * spatial_extent + (
            space % spatial_extent
        )

    def temporal_hop_sign(target_time_raw: int) -> sp.Integer:
        return sp.Integer(
            boundary_sign
            if target_time_raw >= half_time or target_time_raw < -half_time
            else 1
        )

    staggered = sp.zeros(size, size)
    for time in range(-half_time, half_time):
        for space in range(spatial_extent):
            index = site_index(time, space)
            staggered[index, index] += mass
            staggered[index, site_index(time + 1, space)] += (
                sp.Rational(1, 2) * temporal_hop_sign(time + 1)
            )
            staggered[index, site_index(time - 1, space)] += (
                -sp.Rational(1, 2) * temporal_hop_sign(time - 1)
            )
            staggered[index, site_index(time, space + 1)] += (
                parity(time) * sp.Rational(1, 2)
            )
            staggered[index, site_index(time, space - 1)] += (
                -parity(time) * sp.Rational(1, 2)
            )

    degrees = {
        site_index(time, space): (time % 2) + (space % 2)
        for time in range(-half_time, half_time)
        for space in range(spatial_extent)
    }
    kernel = staggered - mass * sp.eye(size)
    raising_kernel = sp.zeros(size, size)
    for row in range(size):
        for column in range(size):
            if kernel[row, column] != 0 and degrees[row] == degrees[column] + 1:
                raising_kernel[row, column] = kernel[row, column]
    differential = -I * raising_kernel

    hodge = sp.zeros(size, size)
    for anchor_time in range(-half_time, half_time):
        for anchor_space in range(spatial_extent):
            block = h_site(field_c[anchor_time], volume)
            for row_offset, (row_time, row_space) in enumerate(OFFSETS):
                for column_offset, (column_time, column_space) in enumerate(OFFSETS):
                    if block[row_offset, column_offset] == 0:
                        continue
                    hodge[
                        site_index(anchor_time + row_time, anchor_space + row_space),
                        site_index(anchor_time + column_time, anchor_space + column_space),
                    ] += block[row_offset, column_offset] / 4

    operator = mass * hodge + I * (
        hodge * differential + differential.H * hodge
    )
    reflection = sp.zeros(size, size)
    for time in range(-half_time, half_time):
        for space in range(spatial_extent):
            reflection[
                site_index(-1 - time, space), site_index(time, space)
            ] = 1
    return operator, staggered, hodge, differential, reflection, site_index


def torus_objects_mixed(
    mass: sp.Expr,
    half_time: int,
    boundary_sign: int,
    shear: sp.Expr,
    spatial_extent: int = LX,
) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix, object]:
    """Upper anchors use H(c), lower anchors its P4 reflection image."""
    size = 2 * half_time * spatial_extent

    def site_index(time: int, space: int) -> int:
        return ((time + half_time) % (2 * half_time)) * spatial_extent + (
            space % spatial_extent
        )

    def temporal_hop_sign(target_time_raw: int) -> sp.Integer:
        return sp.Integer(
            boundary_sign
            if target_time_raw >= half_time or target_time_raw < -half_time
            else 1
        )

    staggered = sp.zeros(size, size)
    for time in range(-half_time, half_time):
        for space in range(spatial_extent):
            index = site_index(time, space)
            staggered[index, index] += mass
            staggered[index, site_index(time + 1, space)] += (
                sp.Rational(1, 2) * temporal_hop_sign(time + 1)
            )
            staggered[index, site_index(time - 1, space)] += (
                -sp.Rational(1, 2) * temporal_hop_sign(time - 1)
            )
            staggered[index, site_index(time, space + 1)] += (
                parity(time) * sp.Rational(1, 2)
            )
            staggered[index, site_index(time, space - 1)] += (
                -parity(time) * sp.Rational(1, 2)
            )

    degrees = {
        site_index(time, space): (time % 2) + (space % 2)
        for time in range(-half_time, half_time)
        for space in range(spatial_extent)
    }
    kernel = staggered - mass * sp.eye(size)
    raising_kernel = sp.zeros(size, size)
    for row in range(size):
        for column in range(size):
            if kernel[row, column] != 0 and degrees[row] == degrees[column] + 1:
                raising_kernel[row, column] = kernel[row, column]
    differential = -I * raising_kernel

    shear_square = 1 - shear**2
    hodge_upper = sp.Matrix(
        [
            [1, 0, 0, 0],
            [0, 1 / shear_square, -shear / shear_square, 0],
            [0, -shear / shear_square, 1 / shear_square, 0],
            [0, 0, 0, 1],
        ]
    )
    offset_time_flip = sp.Matrix(
        [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
    )
    hodge_lower = offset_time_flip * hodge_upper * offset_time_flip
    hodge_flat = sp.eye(4)
    hodge = sp.zeros(size, size)
    for anchor_time in range(-half_time, half_time):
        if anchor_time in (-1, half_time - 1):
            block = hodge_flat
        elif anchor_time >= 0:
            block = hodge_upper
        else:
            block = hodge_lower
        for anchor_space in range(spatial_extent):
            for row_offset, (row_time, row_space) in enumerate(OFFSETS):
                for column_offset, (column_time, column_space) in enumerate(OFFSETS):
                    if block[row_offset, column_offset] == 0:
                        continue
                    hodge[
                        site_index(anchor_time + row_time, anchor_space + row_space),
                        site_index(anchor_time + column_time, anchor_space + column_space),
                    ] += block[row_offset, column_offset] / 4

    operator = mass * hodge + I * (
        hodge * differential + differential.H * hodge
    )
    reflection = sp.zeros(size, size)
    for time in range(-half_time, half_time):
        for space in range(spatial_extent):
            reflection[
                site_index(-1 - time, space), site_index(time, space)
            ] = 1
    return operator, staggered, hodge, differential, reflection, site_index


def history_gram(
    propagator: sp.Matrix, site_index, spatial_extent: int = LX
) -> sp.Matrix:
    positive = [
        site_index(time, space)
        for time in (0, 1)
        for space in range(spatial_extent)
    ]
    reflected = [
        site_index(-1 - time, space)
        for time in (0, 1)
        for space in range(spatial_extent)
    ]
    return sp.Matrix(
        len(positive),
        len(positive),
        lambda row, column: sp.conjugate(
            propagator[positive[row], reflected[column]]
        ),
    )


def gram_and_diag(
    operator: sp.Matrix, site_index, spatial_extent: int = LX
) -> tuple[sp.Matrix, sp.Expr, tuple[sp.Expr, ...]]:
    propagator = operator.inv()
    gram = history_gram(propagator, site_index, spatial_extent)
    defect = max_abs_entry(gram - gram.H)
    leading_minors = tuple(
        sp.factor(gram[:size, :size].det())
        for size in range(1, gram.rows + 1)
    )
    return gram, defect, leading_minors


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
        "parent": git_output("rev-parse", PARENT_COMMIT),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        "ancestor_105": is_ancestor(ANCESTOR_105, "HEAD"),
        "ancestor_104": is_ancestor(ANCESTOR_104, "HEAD"),
        "ancestor_103": is_ancestor(ANCESTOR_103, "HEAD"),
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "expected_parent": expected_parent,
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
    }


def flat_profile(half_time: int) -> dict[int, sp.Integer]:
    return {
        time: sp.Integer(0) for time in range(-half_time, half_time)
    }


def constant_profile(
    half_time: int, shear: sp.Expr
) -> dict[int, sp.Expr]:
    return {time: shear for time in range(-half_time, half_time)}


def step_profile(half_time: int, shear: sp.Expr) -> dict[int, sp.Expr]:
    return {
        time: (
            sp.Integer(0)
            if time in (-1, half_time - 1)
            else (shear if time >= 0 else -shear)
        )
        for time in range(-half_time, half_time)
    }


def raw_step_profile(
    half_time: int, shear: sp.Rational
) -> dict[int, sp.Expr]:
    """Sign-rule profile WITHOUT zeroing the straddling anchors."""
    return {
        time: (shear if time >= 0 else -shear)
        for time in range(-half_time, half_time)
    }


PERIODIC_WITNESS = sp.Matrix((24, 1, 24, 1, -37, -1, -37, -1))
PERIODIC_WITNESS_VALUE = sp.Rational(-713858800, 1216449)


def flat_torus_foundation(mutation: str) -> dict[str, object]:
    mass = sp.Rational(9, 20)
    half_time = 4
    flat = flat_profile(half_time)
    operator, staggered, hodge, _, reflection, site_index = torus_objects(
        mass, flat, sp.Integer(1), half_time, -1
    )
    if mutation == "break_flat_normalization":
        # Changing the overlap analysis weight from 1/2 to 1 scales H_ov
        # and its linear action by four.
        hodge = 4 * hodge
        operator = 4 * operator
    gram, gram_defect, leading_minors = gram_and_diag(operator, site_index)

    periodic_operator, _, _, _, _, periodic_index = torus_objects(
        mass, flat, sp.Integer(1), half_time, 1
    )
    periodic_gram = history_gram(periodic_operator.inv(), periodic_index)
    witness_value = sp.factor(
        (PERIODIC_WITNESS.H * periodic_gram * PERIODIC_WITNESS)[0]
    )
    witness_asserted = mutation != "claim_periodic_positive"
    return {
        "hodge_identity": matrix_equal(hodge, sp.eye(2 * half_time * LX)),
        "same_action": matrix_equal(operator, staggered),
        "reflection_defect": max_abs_entry(
            reflection * operator.H * reflection - operator
        ),
        "gram": gram,
        "gram_defect": gram_defect,
        "leading_minors": leading_minors,
        "minors_positive": all(bool(minor > 0) for minor in leading_minors),
        "periodic_witness_value": witness_value,
        "periodic_witness_pinned": witness_value == PERIODIC_WITNESS_VALUE,
        "periodic_witness_negative": bool(witness_value < 0),
        "periodic_witness_asserted": witness_asserted,
    }


def complex_abs_square(value: sp.Expr) -> sp.Expr:
    return sp.factor(sp.expand(value * sp.conjugate(value)))


def calibrated_chain_gram(
    mass: sp.Expr, eigenvalue: sp.Expr, half: int
) -> sp.Matrix:
    propagator = flat_chain(mass, eigenvalue, half).inv()
    offset = half
    raw = sp.Matrix(
        2,
        2,
        lambda row, column: propagator[
            offset + row, offset - 1 - column
        ],
    )
    return raw.C


def flat_chain_calibration(mutation: str) -> dict[str, object]:
    mass = sp.Rational(9, 20)
    radius = sp.Rational(3, 4)
    target_z = (
        sp.Rational(1, 2)
        if mutation == "break_calibration_target"
        else sp.Rational(1, 4)
    )
    entrywise_improvement = True
    limiting_accuracy = True
    maximum_half24_error = sp.Integer(0)
    for eigenvalue in (sp.Rational(3, 5), -sp.Rational(3, 5)):
        channel = (mass + I * eigenvalue) / radius
        target = sp.simplify(
            (2 * target_z / (1 + target_z))
            * sp.Matrix(
                [
                    [1, sp.sqrt(target_z) * channel],
                    [sp.sqrt(target_z) * sp.conjugate(channel), target_z],
                ]
            )
        )
        gram8 = calibrated_chain_gram(mass, eigenvalue, 8)
        gram16 = calibrated_chain_gram(mass, eigenvalue, 16)
        gram24 = calibrated_chain_gram(mass, eigenvalue, 24)
        for error8, error16, error24 in zip(
            gram8 - target, gram16 - target, gram24 - target, strict=True
        ):
            entrywise_improvement &= bool(
                complex_abs_square(error16) < complex_abs_square(error8)
            )
            limiting_accuracy &= bool(
                complex_abs_square(error24) < sp.Rational(1, 10**18)
            )
            maximum_half24_error = max(
                maximum_half24_error, sp.simplify(sp.Abs(error24))
            )
    return {
        "target_z": target_z,
        "entrywise_improvement": entrywise_improvement,
        "limiting_accuracy": limiting_accuracy,
        "maximum_half24_error": maximum_half24_error,
    }


def reflection_channel_theorem(mutation: str) -> dict[str, object]:
    shear, volume = sp.symbols("q v", real=True, nonzero=True)
    shear_square = 1 - shear**2
    offset_time_flip = (
        sp.eye(4)
        if mutation == "break_channel_identity"
        else sp.Matrix(
            [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
        )
    )
    reflected = offset_time_flip * h_site(-shear, volume) * offset_time_flip
    expected = sp.Matrix(
        [
            [volume / shear_square, 0, 0, shear * volume / shear_square],
            [0, 1 / volume, 0, 0],
            [0, 0, volume, 0],
            [shear * volume / shear_square, 0, 0, volume / shear_square],
        ]
    )

    half_time = 4
    fixture_shear = sp.Rational(5, 13)
    _, _, hodge, _, reflection, _ = torus_objects(
        sp.Rational(9, 20),
        constant_profile(half_time, fixture_shear),
        sp.Integer(1),
        half_time,
        -1,
    )
    hodge_defect = max_abs_entry(reflection * hodge.C * reflection - hodge)
    expected_defect = (
        sp.Integer(0)
        if mutation == "mislabel_channel_value"
        else sp.Rational(65, 576)
    )
    return {
        "symbolic_matrix": matrix_simplify_equal(reflected, expected),
        "degree_changing_entry": sp.simplify(
            reflected[0, 3] - shear * volume / shear_square
        )
        == 0,
        "old_channel_zero": sp.simplify(reflected[1, 2]) == 0,
        "hodge_defect": hodge_defect,
        "expected_hodge_defect": expected_defect,
        "fixture_identity": sp.Rational(5, 13)
        * sp.Rational(169, 144)
        / 4
        == sp.Rational(65, 576),
    }


def canonical_time(time: int, half_time: int) -> int:
    return ((time + half_time) % (2 * half_time)) - half_time


def theta_anchor(time: int, half_time: int) -> int:
    return canonical_time(-2 - time, half_time)


def derived_seam_data(mutation: str) -> dict[str, object]:
    half_time = 4
    anchors = range(-half_time, half_time)
    fixed_points = {
        time for time in anchors if theta_anchor(time, half_time) == time
    }
    expected_fixed_points = (
        {0} if mutation == "drop_seam_constraint" else {-1, half_time - 1}
    )
    fixed_values = sp.symbols("c_fixed_0:2", real=True)
    forced_zero = all(
        sp.solve(sp.Eq(value, -value), value) == [sp.Integer(0)]
        for value in fixed_values
    )
    profile = step_profile(half_time, sp.Rational(5, 13))
    zero_anchors = {time for time, value in profile.items() if value == 0}
    antisymmetric = all(
        profile[theta_anchor(time, half_time)] == -profile[time]
        for time in anchors
    )
    return {
        "fixed_points": fixed_points,
        "expected_fixed_points": expected_fixed_points,
        "forced_zero": forced_zero,
        "zero_anchors": zero_anchors,
        "antisymmetric": antisymmetric,
    }


def two_history_gram_walls(mutation: str) -> dict[str, object]:
    mass = sp.Rational(9, 20)
    shear = sp.Rational(5, 13)
    volume = sp.Integer(1)
    half_time = 4

    constant_operator, _, constant_hodge, _, constant_reflection, constant_index = (
        torus_objects(
            mass,
            constant_profile(half_time, shear),
            volume,
            half_time,
            -1,
        )
    )
    step_operator, _, step_hodge, _, step_reflection, step_index = torus_objects(
        mass,
        step_profile(half_time, shear),
        volume,
        half_time,
        -1,
    )
    mixed_operator, _, mixed_hodge, mixed_differential, mixed_reflection, mixed_index = (
        torus_objects_mixed(mass, half_time, -1, shear)
    )

    raw_operator, _, _, _, _, raw_index = torus_objects(
        mass,
        raw_step_profile(half_time, shear),
        volume,
        half_time,
        -1,
    )
    constant_propagator = constant_operator.inv()
    step_propagator = step_operator.inv()
    mixed_propagator = mixed_operator.inv()
    constant_gram = history_gram(constant_propagator, constant_index)
    step_gram = history_gram(step_propagator, step_index)
    gh_step_gram = history_gram(step_propagator * step_hodge, step_index)
    mixed_gram = history_gram(mixed_propagator, mixed_index)
    raw_gram = history_gram(raw_operator.inv(), raw_index)

    constant_defect = sp.factor(max_abs_entry(constant_gram - constant_gram.H))
    step_defect = sp.factor(max_abs_entry(step_gram - step_gram.H))
    gh_step_defect = sp.factor(max_abs_entry(gh_step_gram - gh_step_gram.H))
    mixed_defect = sp.factor(max_abs_entry(mixed_gram - mixed_gram.H))
    raw_defect = sp.factor(max_abs_entry(raw_gram - raw_gram.H))

    ordering = constant_defect > step_defect > 0
    if mutation == "invert_defect_ordering":
        ordering = constant_defect < step_defect
    constant_claim = (
        constant_defect == 0
        if mutation == "claim_const_history_hermitian"
        else constant_defect != 0
    )
    step_claim = (
        step_defect == 0
        if mutation == "claim_step_gram_hermitian"
        else step_defect != 0
    )
    return {
        "constant_defect": constant_defect,
        "step_defect": step_defect,
        "gh_step_defect": gh_step_defect,
        "mixed_defect": mixed_defect,
        "ordering": ordering,
        "constant_claim": constant_claim,
        "step_claim": step_claim,
        "gh_improves": gh_step_defect < step_defect and gh_step_defect != 0,
        "raw_defect": raw_defect,
        "raw_tension": (
            raw_defect == 0
            if mutation == "claim_raw_seam_hermitian"
            else raw_defect != 0 and raw_defect < step_defect
        ),
        "mixed_hodge_covariance": max_abs_entry(
            mixed_reflection * mixed_hodge.C * mixed_reflection - mixed_hodge
        ),
        "mixed_differential_defect": max_abs_entry(
            mixed_reflection * mixed_differential * mixed_reflection
            + mixed_differential.H
        ),
        "step_gram": step_gram,
        "step_operator": step_operator,
        "step_reflection": step_reflection,
        "constant_hodge": constant_hodge,
        "constant_reflection": constant_reflection,
    }


def diagonal_dressing_candidates(half_time: int) -> dict[str, sp.Matrix]:
    size = 2 * half_time * LX

    def diagonal(function) -> sp.Matrix:
        return sp.diag(
            *(
                function((index // LX) - half_time, index % LX)
                for index in range(size)
            )
        )

    grade_phase = diagonal(
        lambda time, space: I ** ((time % 2) + (space % 2))
    )
    space_parity = diagonal(lambda _time, space: parity(space))
    time_parity = diagonal(lambda time, _space: parity(time))
    product_parity = diagonal(lambda time, space: parity(time + space))
    identity = sp.eye(size)
    return {
        "1": identity,
        "Gx": space_parity,
        "Gt": time_parity,
        "Gp": product_parity,
        "i^deg": grade_phase,
        "Gx i^deg": space_parity * grade_phase,
        "Gt i^deg": time_parity * grade_phase,
        "Gp i^deg": product_parity * grade_phase,
    }


def covariance_dressing_hits(
    operator: sp.Matrix, reflection: sp.Matrix, half_time: int
) -> set[tuple[str, str]]:
    operations = (
        ("H", operator.H),
        ("C", operator.C),
        ("T", operator.T),
        ("id", operator),
    )
    hits: set[tuple[str, str]] = set()
    for name, dressing in diagonal_dressing_candidates(half_time).items():
        for operation_name, transformed in operations:
            if matrix_equal(
                reflection * dressing * transformed * dressing.H * reflection,
                operator,
            ):
                hits.add((name, operation_name))
    return hits


def calibrated_covariance_hits(
    raw_hits: set[tuple[str, str]]
) -> set[tuple[str, str]]:
    # Gate C fixes the undressed conjugate-history convention, so the real-flat
    # algebraic aliases 1.T, Gp.C, and Gp.id are recorded but not new calibrated
    # reflection dressings.
    return {hit for hit in raw_hits if hit == ("1", "H")}




DRESSING_CERTIFICATE_PARAMS = (
    sp.Integer(507968644026955530085904130509337010540515817873788319311345515383612296029720079811810132653552),
    sp.Integer(41532452335260334034957746615889889690141434198992020757127483010426721818108364308425298585240),
    sp.Integer(41385182270195709174736265631465163934297334634942112413026201220858061429793417133170586290840),
    sp.Integer(-99516981857048688256249971796779510257767571680017059012842643361723281883552835866630003281646),
    sp.Integer(1833417318393208695828568805895558222747355122178331594308500486778470789047226029468070931680),
    sp.Integer(49534066411967129048632336601892334125920831929632587776519163897056228339957906900848719808600),
    sp.Integer(583767067596676525810620669726200150411964788957764188321891010476389121880969423915023775555800),
    sp.Integer(-46762561091094320816555106519491637698970558945336688478301137068354391186814368133036915388440),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(-92960679527218549712063123648860240924804580124293876596738494826013816450206947628786021433420),
    sp.Integer(-6569810041034990666397887436556810085064577129273936941551768108135948329034687859174023071605),
    sp.Integer(133516288783768367469283644911877346264106372353413436532524148686263056273769626431868334990822),
    sp.Integer(26742410356895126745535006571044757690289091385775689900022386467043627087667933340911979773690),
    sp.Integer(1141840098923108606599239406887185095350960538229366092543131324331321934064787023154467642900),
    sp.Integer(-10543458475696290351592926717261960542828614152490703288304052005311823243958105442678533563450),
    sp.Integer(-7927787670195359755557189516226228108576859033834767431124876154442883641974756457673417862700),
    sp.Integer(11674104500194566881743916578595078230869856330134760975432605685370682360799228233700344384600),
    sp.Integer(12777217829042196308049921249039261245126781699759011073564588287232440929641832936058662863900),
    sp.Integer(51641136209626860803571044139848886376972040538507485453284935047479173999665019715384101841455),
    sp.Integer(-1513412767693811407321557218629570743956855060170988787741252444125600093131000377482643574200),
    sp.Integer(-40650934460081410399681180537301940677600066415371305320275889098941410910127407570312503495600),
    sp.Integer(13715642233382803381407015868476235218978164944954642113991959874450106937210517757938581639300),
    sp.Integer(-439377900298203311803032740892456022439086952952867712570041032165496801231580754753025553800),
    sp.Integer(13626139327766502706780472161998142325518350936019798691061025590120098329552232789377780137600),
    sp.Integer(11486206220758586577073108998021921327342797813304905942803233155684437982813237631969526051500),
)

def stage_h_local_dressing_rank(gram: sp.Matrix, mutation: str) -> dict[str, object]:
    # Literal Stage-H ansatz: four complex 2x2 blocks multiplying the cell-local,
    # staggered, symmetric-neighbor, and antisymmetric-neighbor spatial matrices.
    spatial_shift = sp.zeros(4, 4)
    for space in range(4):
        spatial_shift[(space + 1) % 4, space] = 1
    spatial_factors = [
        sp.eye(4),
        sp.diag(*(parity(space) for space in range(4))),
        spatial_shift + spatial_shift.T,
        spatial_shift - spatial_shift.T,
    ]
    parameters = sp.symbols("p0:32", real=True)
    dressing = sp.zeros(8, 8)
    parameter_offset = 0
    for factor_index in range(4):
        block = sp.Matrix(
            2,
            2,
            lambda row, column: parameters[
                parameter_offset + 2 * (2 * row + column)
            ]
            + I
            * parameters[
                parameter_offset + 2 * (2 * row + column) + 1
            ],
        )
        parameter_offset += 8
        dressing += sp.Matrix(
            8,
            8,
            lambda row, column: block[row // 4, column // 4]
            * spatial_factors[factor_index][row % 4, column % 4],
        )

    condition = sp.expand(dressing * gram - gram.H * dressing.H)
    equations: list[sp.Expr] = []
    for entry in condition:
        entry = sp.expand(entry)
        equations.append(sp.re(entry))
        equations.append(sp.im(entry))
    coefficients, right_hand_side = sp.linear_eq_to_matrix(equations, parameters)
    coefficient_rank = coefficients.rank()
    pinned = list(DRESSING_CERTIFICATE_PARAMS)
    if mutation == "break_pd_certificate":
        pinned[0] = pinned[0] + 1
    substitution = {parameters[i]: pinned[i] for i in range(32)}
    pinned_dressing = dressing.subs(substitution)
    dressed = sp.expand(pinned_dressing * gram)
    certificate_equation = matrix_equal(
        sp.expand(pinned_dressing * gram - gram.H * pinned_dressing.H),
        sp.zeros(8),
    )
    certificate_invertible = sp.expand(pinned_dressing.det()) != 0
    if certificate_equation:
        certificate_minors = [
            sp.nsimplify(sp.det(dressed[:size, :size])) for size in range(1, 9)
        ]
        certificate_positive = all(minor > 0 for minor in certificate_minors)
    else:
        # A corrupted pin leaves a non-Hermitian dressed Gram; positivity
        # is then undefined and the certificate fails closed.
        certificate_positive = False
    return {
        "parameter_count": len(parameters),
        "equation_count": len(equations),
        "coefficient_rank": coefficient_rank,
        "homogeneous": matrix_equal(
            right_hand_side, sp.zeros(len(equations), 1)
        ),
        "nullity": len(parameters) - coefficient_rank,
        "certificate_equation": certificate_equation,
        "certificate_invertible": certificate_invertible,
        "certificate_positive": certificate_positive,
    }


EXPECTED_FLAT_RAW_HITS = {
    ("1", "H"),
    ("1", "T"),
    ("Gp", "C"),
    ("Gp", "id"),
}


def local_dressing_exhaustion(
    mutation: str, walls: dict[str, object]
) -> dict[str, object]:
    half_time = 4
    mass = sp.Rational(9, 20)
    flat_operator, _, _, _, flat_reflection, _ = torus_objects(
        mass,
        flat_profile(half_time),
        sp.Integer(1),
        half_time,
        -1,
    )
    flat_raw_hits = covariance_dressing_hits(
        flat_operator, flat_reflection, half_time
    )
    step_raw_hits = covariance_dressing_hits(
        walls["step_operator"], walls["step_reflection"], half_time
    )
    flat_hits = calibrated_covariance_hits(flat_raw_hits)
    step_hits = calibrated_covariance_hits(step_raw_hits)
    expected_flat_hits = (
        set()
        if mutation == "claim_flat_needs_dressing"
        else {("1", "H")}
    )
    stage_h = stage_h_local_dressing_rank(walls["step_gram"], mutation)
    expected_rank = 32 if mutation == "claim_dressing_space_trivial" else 24
    return {
        "flat_raw_hits": flat_raw_hits,
        "step_raw_hits": step_raw_hits,
        "flat_raw_complete": flat_raw_hits == EXPECTED_FLAT_RAW_HITS,
        "flat_hits": flat_hits,
        "step_hits": step_hits,
        "expected_flat_hits": expected_flat_hits,
        "stage_h": stage_h,
        "expected_rank": expected_rank,
    }


SCOPE_KEYS = (
    "transfer_reflection",
    "degree_channel",
    "antiperiodic",
    "curved_boundary",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity",
    "adm",
    "n1_n8",
    "walls",
    "n5_resolution",
)


def scope_certificate(mutation: str) -> dict[str, bool]:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return {key: False for key in SCOPE_KEYS}
    note = " ".join(raw_note.lower().split())
    result = {
        "transfer_reflection": "transfer-derived reflection" in note,
        "degree_channel": "a02" in note or "degree-changing channel" in note,
        "antiperiodic": "antiperiodic" in note,
        "curved_boundary": "not a curved os no-go" in note,
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": "retained-positive end-to-end theory count remains zero"
        in note,
        "gravity": "gravity constraint quotient remains unexecuted" in note,
        "adm": "actual adm/history transporter remains" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "walls": "w1" in note and "w2" in note,
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
    }
    if mutation == "weaken_no_go_packet":
        result["n1_n8"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution"] = False
    if mutation == "claim_adm_link_derived":
        result["adm"] = False
    if mutation == "claim_curved_os_closed":
        result["curved_boundary"] = False
    if mutation == "claim_axiom_amendment":
        result["axiom"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    if mutation == "claim_obligation_retirement":
        result["zero_retirement"] = False
    return result


MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "claim_periodic_positive",
    "break_flat_normalization",
    "break_calibration_target",
    "break_channel_identity",
    "mislabel_channel_value",
    "drop_seam_constraint",
    "claim_const_history_hermitian",
    "claim_step_gram_hermitian",
    "claim_raw_seam_hermitian",
    "invert_defect_ordering",
    "claim_dressing_space_trivial",
    "break_pd_certificate",
    "claim_flat_needs_dressing",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_adm_link_derived",
    "claim_curved_os_closed",
    "claim_axiom_amendment",
    "claim_toe_progress",
    "claim_obligation_retirement",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-current-authority-and-Block106-parent",
        "current axioms, registries, ancestry, and the Block106 parent triple are content-bound",
        authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and authority["ancestor_105"]
        and authority["ancestor_104"]
        and authority["ancestor_103"]
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
        f"registry origin/main={authority['registry']}; worktree={authority['worktree_registry']}",
    )

    foundation = flat_torus_foundation(mutation)
    checks.check(
        "B-flat-torus-foundation",
        "the normalized flat antiperiodic torus has the exact positive Gram and a periodic counterexample",
        foundation["hodge_identity"]
        and foundation["same_action"]
        and foundation["reflection_defect"] == 0
        and foundation["gram_defect"] == 0
        and foundation["minors_positive"]
        and foundation["periodic_witness_asserted"]
        and foundation["periodic_witness_pinned"]
        and foundation["periodic_witness_negative"],
        f"eight leading minors positive; periodic w^H K w={foundation['periodic_witness_value']}",
    )

    calibration = flat_chain_calibration(mutation)
    checks.check(
        "C-flat-chain-calibration",
        "both spatial eigenlines converge entrywise to the exact Block104 z=1/4 Gram",
        calibration["target_z"] == sp.Rational(1, 4)
        and calibration["entrywise_improvement"]
        and calibration["limiting_accuracy"],
        f"max half-24 exact error={calibration['maximum_half24_error']}; bound=1/10^9",
    )

    channel = reflection_channel_theorem(mutation)
    checks.check(
        "D-reflection-channel-theorem",
        "offset time reflection sends the shear into the degree-changing channel with exact defect 65/576",
        channel["symbolic_matrix"]
        and channel["degree_changing_entry"]
        and channel["old_channel_zero"]
        and channel["hodge_defect"] == channel["expected_hodge_defect"]
        and channel["fixture_identity"],
        f"max |P conj(H_ov) P-H_ov|={channel['hodge_defect']}",
    )

    seam = derived_seam_data(mutation)
    checks.check(
        "E-derived-seam-data",
        "theta_anchor has two fixed anchors whose reflection-antisymmetric shear is forced exactly flat",
        seam["fixed_points"] == seam["expected_fixed_points"]
        and seam["forced_zero"]
        and seam["zero_anchors"] == {-1, 3}
        and seam["antisymmetric"],
        f"fixed points={sorted(seam['fixed_points'])}; zero anchors={sorted(seam['zero_anchors'])}",
    )

    walls = two_history_gram_walls(mutation)
    checks.check(
        "F-two-history-gram-walls",
        "constant, raw-seam, two-seam, GH-step, and A02 histories have the exact ordered non-Hermiticity walls",
        walls["ordering"]
        and walls["constant_claim"]
        and walls["step_claim"]
        and walls["gh_improves"]
        and walls["raw_tension"]
        and walls["mixed_hodge_covariance"] == 0
        and walls["mixed_differential_defect"] == sp.Rational(1, 2)
        and walls["mixed_defect"] != 0,
        "all defects are computed from exact rational matrices",
    )
    print(
        "GRAM_DEFECTS_EXACT: "
        f"const={walls['constant_defect']} step={walls['step_defect']} "
        f"GH-step={walls['gh_step_defect']} A02={walls['mixed_defect']} "
        f"raw-seam={walls['raw_defect']}"
    )
    print(
        "GRAM_DEFECTS_DISPLAY: "
        f"const={sp.N(walls['constant_defect'], 8)} "
        f"step={sp.N(walls['step_defect'], 8)} "
        f"GH-step={sp.N(walls['gh_step_defect'], 8)} "
        f"A02={sp.N(walls['mixed_defect'], 8)}"
    )

    exhaustion = local_dressing_exhaustion(mutation, walls)
    stage_h = exhaustion["stage_h"]
    checks.check(
        "G-local-dressing-space-and-certificate",
        "the diagonal class is empty on the seam while the local GL solve has an eight-dimensional space with a displayed exact positive-definite dressing",
        exhaustion["flat_raw_complete"]
        and exhaustion["flat_hits"] == exhaustion["expected_flat_hits"]
        and exhaustion["step_raw_hits"] == set()
        and exhaustion["step_hits"] == set()
        and stage_h["parameter_count"] == 32
        and stage_h["equation_count"] == 128
        and stage_h["homogeneous"]
        and stage_h["coefficient_rank"] == exhaustion["expected_rank"]
        and stage_h["nullity"] == 32 - exhaustion["expected_rank"]
        and stage_h["certificate_equation"]
        and stage_h["certificate_invertible"]
        and stage_h["certificate_positive"],
        f"rank={stage_h['coefficient_rank']} nullity={stage_h['nullity']}; pinned dressing: equation/invertible/PD all exact",
    )

    checks.check(
        "H-positivity-structure",
        "flat antiperiodic positivity is exact; the step claim stops at certified non-Hermiticity",
        foundation["gram_defect"] == 0
        and foundation["minors_positive"]
        and walls["step_defect"] != 0,
        "no PSD or non-PSD assertion is made for the step-profile symmetrized Gram",
    )

    scope = scope_certificate(mutation)
    checks.check(
        "I-scope",
        "the bounded note preserves the N1--N8, W1/W2, N5, ADM, gravity, audit, and TOE walls",
        all(scope.values()),
        "note scope is guarded against absence; no curved-OS or transporter completion is inferred",
    )

    print(
        f"AXIOM_AUTHORITY: origin/main={authority['main']} axiom={CURRENT_AXIOM_BLOB} registry={CURRENT_REGISTRY_BLOB}; Block106 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: exact calibration, reflection channel, seam constraint, Gram-defect, and local dressing-space identities are checked"
    )
    print(
        "per_site: one Grassmann mode is retained per fine site on the antiperiodic reflection torus"
    )
    print(
        "per_mode: both spatial eigenline signs are calibrated exactly against the Block 104 Gram"
    )
    print(
        "per_block: the straddling anchors are exactly flat and the shear channel reflects into the degree-changing channel"
    )
    print(
        "lattice_wide: checked and not executed — the transfer-derived seam transporter, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open"
    )
    print(
        "RESULT: framework calibration and seam-channel identities are exact; the raw two-history pairing has a certified non-Hermiticity obstruction while the displayed eight-dimensional local dressing space contains an exact positive-definite repair candidate"
    )
    print(
        "DECISION_CUT: advance the involution admissibility and transfer-derived selection of the displayed local dressing space; reject undressed and diagonal-class seam pairings"
    )
    print(
        "TOE: zero obligation retirement, retained-positive end-to-end theory count remains zero, and no TOE percentage moves"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
