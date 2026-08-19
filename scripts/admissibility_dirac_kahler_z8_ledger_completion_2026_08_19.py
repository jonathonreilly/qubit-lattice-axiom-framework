#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_z8_ledger_completion_2026_08_19.py
"""Block 139: exact Z8 ledger-completion bounded theorem.

The committed Block 136 fixture is extended from spatial size six to eight
through its public spatial-fixture seam.  Only the cyclic root field and
projectors are adapted; the committed momentum-block and transfer machinery
is reused.  All scientific comparisons use exact SymPy arithmetic.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re
import subprocess
import sys
import time

import sympy as sp


R = sp.Rational
I = sp.I
SQRT2 = sp.sqrt(2)
_FINAL_LOCATION_ROOT = Path(__file__).resolve().parents[1]
# The cwd fallback keeps this staged scratchpad draft executable before the
# supervisor moves it to scripts/, where the final-location branch is used.
ROOT = (
    _FINAL_LOCATION_ROOT
    if (_FINAL_LOCATION_ROOT / ".git").exists()
    else Path.cwd()
)
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_dirac_kahler_observable_scaling_law_2026_08_18 as b136


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_Z8_LEDGER_COMPLETION_"
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
    "docs/ADMISSIBILITY_DIRAC_KAHLER_Z8_LEDGER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_ZN_CHARGE_KINEMATIC_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_general_zn_charge_kinematic_theorem_2026_08_19.py",
    "logs/runner-cache/admissibility_dirac_kahler_general_zn_charge_kinematic_theorem_2026_08_19.txt",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_OBSERVABLE_SCALING_LAW_BOUNDED_THEOREM_NOTE_2026-08-18.md",
    "scripts/admissibility_dirac_kahler_observable_scaling_law_2026_08_18.py",
    "logs/runner-cache/admissibility_dirac_kahler_observable_scaling_law_2026_08_18.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "29d17653c9c043a74041f070e311f03fce114c0a"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block138-general-zn-theorem-20260819"
)
# Landing supervisor: replace this placeholder with the Block 138 branch tip.
PARENT_COMMIT = "a177384ff4710a8ef1c7f7f244fe2a946df85757"
BLOCK136_COMMIT = "a9e0725db114298d9885e86b34d3c99bfe051444"
BLOCK136_NOTE_BLOB = "5c7e8b724e90320f3ceea332cc3abd4ce5128723"
BLOCK136_RUNNER_BLOB = "f86976787595c0f183ca8ce15456c8f857c2b6a6"
BLOCK136_CACHE_BLOB = "34f29c9a23d97732e864cfc85ba51304d298f8bc"

SPACE_SIZE = 8
TIME_SIZE = b136.TIME_SIZE
Z8_EXTENSION = (I, SQRT2)
Z8_FIELD = sp.QQ.algebraic_field(*Z8_EXTENSION)
PRIMARY_K0_TRACE = R(
    -3962371610825721602827025599106,
    127417091906251505055019140625,
)
SECONDARY_K0_TRACE = R(
    -234369399320455883852546,
    8465566947515869140625,
)
PRIMARY_K0_TRACE_TEXT = (
    "-3962371610825721602827025599106/"
    "127417091906251505055019140625"
)
SECONDARY_K0_TRACE_TEXT = (
    "-234369399320455883852546/"
    "8465566947515869140625"
)

MUTATIONS = (
    "stale_axiom_authority",
    "stale_block138_authority",
    "break_spatial_extension",
    "break_root_projectors",
    "break_rho_completion",
    "break_even_determinants",
    "break_trace_shift_rule",
    "break_class_ledger",
    "break_cross_size_primary",
    "break_cross_size_secondary",
    "break_z8_isospectrality",
    "break_z6_isospectrality",
    "assert_time_shift_intertwiner",
    "weaken_scope_firewalls",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_axiom_authority": "A",
    "stale_block138_authority": "A",
    "break_spatial_extension": "B",
    "break_root_projectors": "B",
    "break_rho_completion": "C",
    "break_even_determinants": "C",
    "break_trace_shift_rule": "D",
    "break_class_ledger": "D",
    "break_cross_size_primary": "E",
    "break_cross_size_secondary": "E",
    "break_z8_isospectrality": "F",
    "break_z6_isospectrality": "F",
    "assert_time_shift_intertwiner": "G",
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
    block138_authority: bool
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
    block138_authority = False
    if parent_ready:
        parent_blobs = tuple(
            commit_blob(PARENT_COMMIT, path)
            for path in (BLOCK138_NOTE, BLOCK138_RUNNER, BLOCK138_CACHE)
        )
        block138_authority = bool(
            git_output("rev-parse", PARENT_REF) == PARENT_COMMIT
            and is_ancestor(PARENT_COMMIT, "HEAD")
            and all(is_hash(value) for value in parent_blobs)
            and parent_blobs
            == tuple(
                worktree_blob(path)
                for path in (BLOCK138_NOTE, BLOCK138_RUNNER, BLOCK138_CACHE)
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
        and b136.AUDIT_TIMEOUT_SEC == AUDIT_TIMEOUT_SEC
    )
    return AuthorityCertificate(
        fixed_authority,
        block138_authority,
        block136_authority,
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
    if isinstance(value, (tuple, list)):
        return all(no_float(item) for item in value)
    if isinstance(value, dict):
        return all(no_float(key) and no_float(item) for key, item in value.items())
    return not sp.sympify(value).has(sp.Float)


def canonical8(value: sp.Expr) -> sp.Expr:
    return Z8_FIELD.to_sympy(Z8_FIELD.from_sympy(sp.expand(value)))


def exact_equal8(left: sp.Expr, right: sp.Expr) -> bool:
    return Z8_FIELD.from_sympy(sp.expand(left - right)) == Z8_FIELD.zero


def matrix_equal8(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        exact_equal8(left[row, column], right[row, column])
        for row in range(left.rows)
        for column in range(left.cols)
    )


def conjugate8(value: sp.Expr) -> sp.Expr:
    return canonical8(sp.conjugate(value))


# omega_8 = exp(+2*pi*i/8), in the committed Block 136 sign convention.
ROOTS8 = (
    sp.S.One,
    SQRT2 * (1 + I) / 2,
    I,
    SQRT2 * (-1 + I) / 2,
    -sp.S.One,
    SQRT2 * (-1 - I) / 2,
    -I,
    SQRT2 * (1 - I) / 2,
)


def root_power8(power: int) -> sp.Expr:
    return ROOTS8[power % SPACE_SIZE]


@lru_cache(maxsize=1)
def projectors8() -> tuple[sp.Matrix, ...]:
    cyclic = b136.shift(SPACE_SIZE)
    return tuple(
        (
            sum(
                (
                    root_power8(-momentum * power) * cyclic**power
                    for power in range(SPACE_SIZE)
                ),
                sp.zeros(SPACE_SIZE),
            )
            / SPACE_SIZE
        ).applyfunc(sp.expand)
        for momentum in range(SPACE_SIZE)
    )


def projectors8_adapter(spatial_size: int) -> tuple[sp.Matrix, ...]:
    if spatial_size != SPACE_SIZE:
        raise ValueError(f"Z8 adapter received spatial size {spatial_size}")
    return projectors8()


@dataclass(frozen=True)
class Z8Solve:
    shear: sp.Rational
    raw: object
    torus_calls: tuple[b136.TorusCall, ...]
    action: sp.Matrix
    blocks: tuple[sp.Matrix, ...]
    transfers: tuple[b136.Transfer, ...]
    momentum_call_count: int
    transfer_call_count: int
    projectors_restored: bool
    field_restored: bool


def build_z8(shear: sp.Rational) -> Z8Solve:
    """Change L_x from six to eight and reuse the committed algorithms."""
    raw, calls = b136.fixture_data_spatial(shear, SPACE_SIZE)
    action = raw.propagator.inv(method="DM").applyfunc(sp.expand)

    committed_projectors = b136.projectors
    momentum_call_count = 0
    try:
        b136.projectors = projectors8_adapter
        block_list = []
        for momentum in range(SPACE_SIZE):
            block_list.append(
                b136.momentum_block(
                    action,
                    momentum,
                    TIME_SIZE,
                    SPACE_SIZE,
                )
            )
            momentum_call_count += 1
        blocks = tuple(block_list)
    finally:
        b136.projectors = committed_projectors
    projectors_restored = b136.projectors is committed_projectors

    committed_extension = b136.ALGEBRAIC_EXTENSION
    committed_field = b136.NUMBER_FIELD
    transfer_call_count = 0
    try:
        b136.ALGEBRAIC_EXTENSION = Z8_EXTENSION
        b136.NUMBER_FIELD = Z8_FIELD
        transfer_list = []
        for block in blocks:
            transfer_list.append(b136.transfer_from_action(block))
            transfer_call_count += 1
        transfers = tuple(transfer_list)
    finally:
        b136.ALGEBRAIC_EXTENSION = committed_extension
        b136.NUMBER_FIELD = committed_field
    field_restored = bool(
        b136.ALGEBRAIC_EXTENSION == committed_extension
        and b136.NUMBER_FIELD is committed_field
    )

    return Z8Solve(
        shear,
        raw,
        calls,
        action,
        blocks,
        transfers,
        momentum_call_count,
        transfer_call_count,
        projectors_restored,
        field_restored,
    )


def fourier_reconstruction_exact(solve: Z8Solve) -> bool:
    projectors = projectors8()
    for time_row in range(TIME_SIZE):
        for time_column in range(TIME_SIZE):
            original = solve.action[
                SPACE_SIZE * time_row : SPACE_SIZE * (time_row + 1),
                SPACE_SIZE * time_column : SPACE_SIZE * (time_column + 1),
            ]
            reconstructed = sum(
                (
                    solve.blocks[momentum][time_row, time_column]
                    * projectors[momentum]
                    for momentum in range(SPACE_SIZE)
                ),
                sp.zeros(SPACE_SIZE),
            )
            if not matrix_equal8(original, reconstructed):
                return False
    return True


def root_projector_certificate() -> bool:
    omega = ROOTS8[1]
    projectors = projectors8()
    cyclic = b136.shift(SPACE_SIZE)
    return bool(
        Z8_EXTENSION == (I, sp.sqrt(2))
        and no_float(ROOTS8)
        and all(exact_equal8(omega**power, ROOTS8[power]) for power in range(8))
        and exact_equal8(omega**8, 1)
        and exact_equal8(omega**4, -1)
        and exact_equal8(omega**2, I)
        and len(projectors) == SPACE_SIZE
        and matrix_equal8(
            sum(projectors, sp.zeros(SPACE_SIZE)),
            sp.eye(SPACE_SIZE),
        )
        and all(projector.rank() == 1 for projector in projectors)
        and all(
            matrix_equal8(
                projectors[left] * projectors[right],
                (
                    projectors[left]
                    if left == right
                    else sp.zeros(SPACE_SIZE)
                ),
            )
            for left in range(SPACE_SIZE)
            for right in range(SPACE_SIZE)
        )
        and all(
            matrix_equal8(
                cyclic * projectors[momentum],
                root_power8(momentum) * projectors[momentum],
            )
            for momentum in range(SPACE_SIZE)
        )
    )


@dataclass(frozen=True)
class SameFamilyCertificate:
    both_committed_shears: bool
    mass_equal_committed_expectation: bool
    shear_profiles_equal_committed_expectations: bool
    only_spatial_input_changed: bool
    root_field_and_projectors_only_adapters: bool
    action_and_momentum_reconstruction_exact: bool
    transfer_machinery_reused: bool
    exact_no_float: bool


def same_family_certificate(
    z8_fixtures: tuple[Z8Solve, ...],
    z6_fixtures: tuple[object, ...],
) -> SameFamilyCertificate:
    shears = (b136.PRIMARY_SHEAR, b136.SECOND_SHEAR)
    calls8 = tuple(item.torus_calls[0] for item in z8_fixtures)
    calls6 = tuple(item.torus_calls[0] for item in z6_fixtures)
    mass_equal = all(
        call8.mass == call6.mass == b136.EXPECTED_MASS
        for call8, call6 in zip(calls8, calls6, strict=True)
    )
    shear_equal = all(
        call8.shear
        == call6.shear
        == b136.expected_shear_profile(shear)
        for shear, call8, call6 in zip(
            shears,
            calls8,
            calls6,
            strict=True,
        )
    )
    only_spatial = all(
        len(z8.torus_calls) == len(z6.torus_calls) == 1
        and call8.half_time == call6.half_time
        and call8.half_time * 2 == TIME_SIZE
        and call8.boundary_sign == call6.boundary_sign == -1
        and call8.spatial_extent == SPACE_SIZE
        and call6.spatial_extent == 6
        and z8.raw.propagator.shape
        == z8.action.shape
        == (TIME_SIZE * SPACE_SIZE, TIME_SIZE * SPACE_SIZE)
        and z6.raw.propagator.shape
        == z6.action.shape
        == (TIME_SIZE * 6, TIME_SIZE * 6)
        for z8, z6, call8, call6 in zip(
            z8_fixtures,
            z6_fixtures,
            calls8,
            calls6,
            strict=True,
        )
    )
    reconstruction = all(
        matrix_equal8(
            z8.action * z8.raw.propagator,
            sp.eye(TIME_SIZE * SPACE_SIZE),
        )
        and matrix_equal8(
            z8.raw.propagator * z8.action,
            sp.eye(TIME_SIZE * SPACE_SIZE),
        )
        and z8.momentum_call_count == SPACE_SIZE
        and len(z8.blocks) == SPACE_SIZE
        and all(block.shape == (TIME_SIZE, TIME_SIZE) for block in z8.blocks)
        and fourier_reconstruction_exact(z8)
        for z8 in z8_fixtures
    )
    transfers_reused = all(
        z8.transfer_call_count == SPACE_SIZE
        and len(z8.transfers) == SPACE_SIZE
        and all(
            transfer.fine_band
            and transfer.construction_valid
            and transfer.characteristic_valid
            and len(transfer.slices) == TIME_SIZE // 2
            and len(transfer.local_transfers) == TIME_SIZE // 2
            and transfer.monodromy.shape == (2, 2)
            for transfer in z8.transfers
        )
        for z8 in z8_fixtures
    )
    exactness = all(
        no_float(z8.raw.propagator)
        and no_float(z8.action)
        and no_float(z8.blocks)
        and no_float(
            tuple(
                transfer.monodromy_trace
                for transfer in z8.transfers
            )
        )
        and no_float(
            tuple(
                transfer.monodromy_determinant
                for transfer in z8.transfers
            )
        )
        and all(
            no_float(transfer.local_transfers)
            and no_float(transfer.monodromy)
            for transfer in z8.transfers
        )
        for z8 in z8_fixtures
    )
    adapters_only = bool(
        root_projector_certificate()
        and b136.ALGEBRAIC_EXTENSION == (I, sp.sqrt(3))
        and Z8_EXTENSION != b136.ALGEBRAIC_EXTENSION
        and all(
            z8.projectors_restored and z8.field_restored
            for z8 in z8_fixtures
        )
    )
    return SameFamilyCertificate(
        tuple(item.shear for item in z8_fixtures)
        == tuple(item.shear for item in z6_fixtures)
        == shears
        and shears[0] != shears[1],
        mass_equal,
        shear_equal,
        only_spatial,
        adapters_only,
        reconstruction,
        transfers_reused,
        exactness,
    )


def equality_classes8(
    values: tuple[sp.Expr, ...],
) -> tuple[tuple[int, ...], ...]:
    classes: list[tuple[int, ...]] = []
    consumed: set[int] = set()
    for index, value in enumerate(values):
        if index in consumed:
            continue
        current = tuple(
            candidate
            for candidate, other in enumerate(values)
            if exact_equal8(value, other)
        )
        classes.append(current)
        consumed.update(current)
    return tuple(classes)


@dataclass(frozen=True)
class Spectrum8:
    traces: tuple[sp.Expr, ...]
    determinants: tuple[sp.Expr, ...]
    trace_classes: tuple[tuple[int, ...], ...]
    determinant_classes: tuple[tuple[int, ...], ...]


def spectrum8(solve: Z8Solve) -> Spectrum8:
    traces = tuple(
        canonical8(transfer.monodromy_trace)
        for transfer in solve.transfers
    )
    determinants = tuple(
        canonical8(transfer.monodromy_determinant)
        for transfer in solve.transfers
    )
    return Spectrum8(
        traces,
        determinants,
        equality_classes8(traces),
        equality_classes8(determinants),
    )


@dataclass(frozen=True)
class LedgerCompletionCertificate:
    both_committed_shears: bool
    zero_four_trace_equal: bool
    zero_four_determinant_equal: bool
    rho_zero_equals_rho_four: bool
    every_even_determinant_one: bool
    exact_no_float: bool


def ledger_completion_certificate(
    spectra: tuple[Spectrum8, ...],
) -> LedgerCompletionCertificate:
    trace_equal = tuple(
        exact_equal8(item.traces[0], item.traces[4])
        for item in spectra
    )
    determinant_equal = tuple(
        exact_equal8(item.determinants[0], item.determinants[4])
        for item in spectra
    )
    rho_equal = tuple(
        trace_ok and determinant_ok
        for trace_ok, determinant_ok in zip(
            trace_equal,
            determinant_equal,
            strict=True,
        )
    )
    even_determinants_one = tuple(
        all(
            exact_equal8(item.determinants[momentum], 1)
            for momentum in (0, 2, 4, 6)
        )
        for item in spectra
    )
    return LedgerCompletionCertificate(
        len(spectra) == 2,
        all(trace_equal),
        all(determinant_equal),
        all(rho_equal),
        all(even_determinants_one),
        no_float(
            tuple(
                value
                for item in spectra
                for value in item.traces + item.determinants
            )
        ),
    )


@dataclass(frozen=True)
class ClassRulesCertificate:
    trace_classes_exact: bool
    determinant_classes_exact: bool
    trace_shift_four_rule: bool
    trace_conjugation_rule: bool
    four_distinct_trace_classes: bool
    both_committed_shears: bool


def class_rules_certificate(
    spectra: tuple[Spectrum8, ...],
) -> ClassRulesCertificate:
    expected_traces = ((0, 4), (1, 5), (2, 6), (3, 7))
    expected_determinants = ((0, 2, 4, 6), (1, 5), (3, 7))
    trace_classes_exact = all(
        item.trace_classes == expected_traces for item in spectra
    )
    determinant_classes_exact = all(
        item.determinant_classes == expected_determinants
        for item in spectra
    )
    shift_rule = all(
        all(
            exact_equal8(
                item.traces[momentum],
                item.traces[(momentum + 4) % SPACE_SIZE],
            )
            for momentum in range(SPACE_SIZE)
        )
        for item in spectra
    )
    conjugation_rule = all(
        all(
            exact_equal8(
                item.traces[(-momentum) % SPACE_SIZE],
                conjugate8(item.traces[momentum]),
            )
            for momentum in range(SPACE_SIZE)
        )
        for item in spectra
    )
    four_distinct = all(
        len(item.trace_classes) == 4
        and all(
            not exact_equal8(
                item.traces[left[0]],
                item.traces[right[0]],
            )
            for left_index, left in enumerate(item.trace_classes)
            for right in item.trace_classes[left_index + 1 :]
        )
        for item in spectra
    )
    return ClassRulesCertificate(
        trace_classes_exact,
        determinant_classes_exact,
        shift_rule,
        conjugation_rule,
        four_distinct,
        len(spectra) == 2,
    )


def exact_equal6(left: sp.Expr, right: sp.Expr) -> bool:
    return (
        b136.field_element(sp.expand(left - right))
        == b136.NUMBER_FIELD.zero
    )


@dataclass(frozen=True)
class CrossSizeCertificate:
    both_committed_shears: bool
    primary_z6_equals_z8: bool
    secondary_z6_equals_z8: bool
    primary_pinned_rational: bool
    secondary_pinned_rational: bool
    displayed_pins_exact: bool
    exact_no_float: bool


def cross_size_certificate(
    z8_spectra: tuple[Spectrum8, ...],
    z6_fixtures: tuple[object, ...],
) -> CrossSizeCertificate:
    pinned = (PRIMARY_K0_TRACE, SECONDARY_K0_TRACE)
    z8_traces = tuple(item.traces[0] for item in z8_spectra)
    z6_traces = tuple(
        item.transfers[0].monodromy_trace
        for item in z6_fixtures
    )
    cross_equal = tuple(
        exact_equal8(z8_trace, z6_trace)
        for z8_trace, z6_trace in zip(
            z8_traces,
            z6_traces,
            strict=True,
        )
    )
    pins_equal = tuple(
        exact_equal8(z8_trace, expected)
        and exact_equal6(z6_trace, expected)
        for z8_trace, z6_trace, expected in zip(
            z8_traces,
            z6_traces,
            pinned,
            strict=True,
        )
    )
    return CrossSizeCertificate(
        tuple(item.shear for item in z6_fixtures)
        == (b136.PRIMARY_SHEAR, b136.SECOND_SHEAR),
        cross_equal[0],
        cross_equal[1],
        pins_equal[0],
        pins_equal[1],
        str(PRIMARY_K0_TRACE) == PRIMARY_K0_TRACE_TEXT
        and str(SECONDARY_K0_TRACE) == SECONDARY_K0_TRACE_TEXT,
        no_float(z8_traces + z6_traces + pinned),
    )


def characteristic_coefficients(
    matrix: sp.Matrix,
) -> tuple[sp.Expr, ...]:
    return tuple(sp.expand(value) for value in matrix.charpoly().all_coeffs())


def coefficients_equal8(
    left: tuple[sp.Expr, ...],
    right: tuple[sp.Expr, ...],
) -> bool:
    return len(left) == len(right) and all(
        exact_equal8(a, b)
        for a, b in zip(left, right, strict=True)
    )


def coefficients_equal6(
    left: tuple[sp.Expr, ...],
    right: tuple[sp.Expr, ...],
) -> bool:
    return len(left) == len(right) and all(
        exact_equal6(a, b)
        for a, b in zip(left, right, strict=True)
    )


@dataclass(frozen=True)
class IsospectralCertificate:
    z8_primary_all_coefficients: bool
    z8_secondary_all_coefficients: bool
    z6_primary_all_coefficients: bool
    z6_secondary_all_coefficients: bool
    monic_degree_eight: bool
    exact_no_float: bool


def isospectral_certificate(
    z8_fixtures: tuple[Z8Solve, ...],
    z6_fixtures: tuple[object, ...],
) -> IsospectralCertificate:
    z8_pairs = tuple(
        (
            characteristic_coefficients(item.blocks[0]),
            characteristic_coefficients(item.blocks[SPACE_SIZE // 2]),
        )
        for item in z8_fixtures
    )
    z6_pairs = tuple(
        (
            characteristic_coefficients(item.blocks[0]),
            characteristic_coefficients(item.blocks[3]),
        )
        for item in z6_fixtures
    )
    z8_equal = tuple(
        coefficients_equal8(left, right) for left, right in z8_pairs
    )
    z6_equal = tuple(
        coefficients_equal6(left, right) for left, right in z6_pairs
    )
    all_pairs = z8_pairs + z6_pairs
    monic_degree_eight = all(
        len(left) == len(right) == TIME_SIZE + 1
        and left[0] == right[0] == 1
        for left, right in all_pairs
    )
    return IsospectralCertificate(
        z8_equal[0],
        z8_equal[1],
        z6_equal[0],
        z6_equal[1],
        monic_degree_eight,
        no_float(all_pairs),
    )


@dataclass(frozen=True)
class RefutedIntertwinerCertificate:
    one_slice_shift_exact: bool
    primary_conjugacy_residual_nonzero: bool
    secondary_conjugacy_residual_nonzero: bool
    exact_no_float: bool


def refuted_intertwiner_certificate(
    z8_fixtures: tuple[Z8Solve, ...],
) -> RefutedIntertwinerCertificate:
    time_shift = b136.shift(TIME_SIZE)
    shift_exact = bool(
        time_shift.shape == (TIME_SIZE, TIME_SIZE)
        and matrix_equal8(time_shift * time_shift.T, sp.eye(TIME_SIZE))
        and time_shift != sp.eye(TIME_SIZE)
        and all(
            time_shift[(column + 1) % TIME_SIZE, column] == 1
            for column in range(TIME_SIZE)
        )
        and sum(time_shift) == TIME_SIZE
    )
    residuals = tuple(
        (
            time_shift * item.blocks[0] * time_shift.T
            - item.blocks[SPACE_SIZE // 2]
        ).applyfunc(sp.expand)
        for item in z8_fixtures
    )
    residual_nonzero = tuple(
        not matrix_equal8(residual, sp.zeros(TIME_SIZE))
        and any(not exact_equal8(entry, 0) for entry in residual)
        for residual in residuals
    )
    return RefutedIntertwinerCertificate(
        shift_exact,
        residual_nonzero[0],
        residual_nonzero[1],
        no_float(residuals),
    )


N5_FENCE = 'N5: per_element: exact Z8 roots and projectors plus the committed Block 136 action and transfer builders are checked in Q(i,sqrt(2))\nper_site: one spatial Z8 extension in the same family; only the extent, root field, and projector set change\nper_mode: at both shears k->k+4 gives exact trace equality and k->8-k gives exact conjugation; the four trace classes remain distinct\nper_block: rho_0=rho_4 gives Sym_2(R)^4, dimension 12, center 4; the N=4 checker finds all characteristic-polynomial coefficients equal for the two real-character momentum blocks\nlattice_wide: exact evidence is N=4,6,8 at shears 5/13 and 3/5; no general-even-N similarity theorem is claimed\nRESULT: the Z8 ledger completes and all three checked sizes occupy the 3m branch; the exact k=0 trace is size-independent on those fixtures\nDECISION_CUT: exhibit the general-even-N isospectral similarity; classify parity-mixing dressing classes; execute the joint-lane program\nTOE: zero obligation retirement; no TOE percentage movement; retained-positive end-to-end theory count remains zero'


SCOPE_KEYS = (
    "same_family_audit",
    "ledger_completion",
    "two_rule_classes",
    "trace_classes",
    "determinant_classes",
    "cross_size_law",
    "primary_pinned_rational",
    "secondary_pinned_rational",
    "isospectrality",
    "refuted_intertwiner",
    "gated_family_upgrade",
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
    compact = note.replace(" ", "")
    shift_rule = bool(
        "k->k+4" in compact
        or "k→k+4" in compact
        or "k↦k+4" in compact
    )
    conjugation_rule = bool(
        "k->8-k" in compact
        or "k→8-k" in compact
        or "k↦8-k" in compact
    )
    return {
        "same_family_audit": (
            "same-family audit" in note
            or "same family audit" in note
        ),
        "ledger_completion": (
            "ledger completion" in note
            and ("rho_0=rho_4" in compact or "ρ_0=ρ_4" in compact)
        ),
        "two_rule_classes": bool(
            shift_rule
            and conjugation_rule
            and (
                "two-rule classes" in note
                or "two rule classes" in note
                or "trace classes" in note
            )
        ),
        "trace_classes": all(
            pair in compact
            for pair in ("(0,4)", "(1,5)", "(2,6)", "(3,7)")
        ),
        "determinant_classes": (
            "(0,2,4,6)" in compact
            and "(1,5)" in compact
            and "(3,7)" in compact
            and (
                "determinant classes" in note
                or "det classes" in note
            )
        ),
        "cross_size_law": (
            (
                "cross-size law" in note
                or "cross size law" in note
            )
            and "z6" in compact
            and "z8" in compact
            and "k=0" in compact
        ),
        "primary_pinned_rational": PRIMARY_K0_TRACE_TEXT in compact,
        "secondary_pinned_rational": SECONDARY_K0_TRACE_TEXT in compact,
        "isospectrality": (
            "isospectral" in note
            and "characteristic polynomial" in note
            and "z6" in compact
            and "z8" in compact
        ),
        "refuted_intertwiner": (
            "refuted intertwiner" in note
            and "one-slice time shift" in note
            and (
                "does not conjugate" in note
                or "not conjugate" in note
                or "nonzero residual" in note
            )
        ),
        "gated_family_upgrade": (
            "per-size checkable fact" in note
            and (
                "gated family upgrade" in note
                or "family upgrade is gated" in note
            )
        ),
        "os_no_go": "not an os no-go" in note,
        "curved_os_no_go": "not a curved os no-go" in note,
        "axiom": "no axiom amendment is justified" in note,
        "firewalls": "firewall" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": bool(
            "no toe percentage moves" in note
            or "no toe percentage movement" in note
        ),
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "gravity_quotient": (
            "gravity constraint quotient remains unexecuted" in note
            or "gravity-constraint quotient is promoted" in note
        ),
        "adm": (
            "actual adm/history transporter remains" in note
            or "actual adm/history transporter" in note
        ),
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
        # Raw substring membership, not normalized membership, makes the
        # printed eight-line fence byte-identical to its note occurrence.
        "n5_verbatim": N5_FENCE in note_text,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started_ns = time.monotonic_ns()

    authority = authority_certificate()
    shears = (b136.PRIMARY_SHEAR, b136.SECOND_SHEAR)
    z8_fixtures = tuple(build_z8(shear) for shear in shears)
    z6_fixtures = tuple(b136.build_z6(shear) for shear in shears)
    spectra = tuple(spectrum8(item) for item in z8_fixtures)
    same_family = same_family_certificate(z8_fixtures, z6_fixtures)
    ledger = ledger_completion_certificate(spectra)
    classes = class_rules_certificate(spectra)
    cross_size = cross_size_certificate(spectra, z6_fixtures)
    isospectral = isospectral_certificate(z8_fixtures, z6_fixtures)
    refuted = refuted_intertwiner_certificate(z8_fixtures)
    scope = scope_certificate(raw_note())

    audit_surface_raw = AUDIT_INPUT_PATHS == (
        "docs/ADMISSIBILITY_DIRAC_KAHLER_Z8_LEDGER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-19.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_ZN_CHARGE_KINEMATIC_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-19.md",
        "scripts/admissibility_dirac_kahler_general_zn_charge_kinematic_theorem_2026_08_19.py",
        "logs/runner-cache/admissibility_dirac_kahler_general_zn_charge_kinematic_theorem_2026_08_19.txt",
        "docs/ADMISSIBILITY_DIRAC_KAHLER_OBSERVABLE_SCALING_LAW_BOUNDED_THEOREM_NOTE_2026-08-18.md",
        "scripts/admissibility_dirac_kahler_observable_scaling_law_2026_08_18.py",
        "logs/runner-cache/admissibility_dirac_kahler_observable_scaling_law_2026_08_18.txt",
    )
    authority_raw = all(
        (
            audit_surface_raw,
            authority.fixed_authority,
            authority.block138_authority,
            authority.block136_authority,
        )
    )
    same_family_raw = all(
        (
            same_family.both_committed_shears,
            same_family.mass_equal_committed_expectation,
            same_family.shear_profiles_equal_committed_expectations,
            same_family.only_spatial_input_changed,
            same_family.root_field_and_projectors_only_adapters,
            same_family.action_and_momentum_reconstruction_exact,
            same_family.transfer_machinery_reused,
            same_family.exact_no_float,
        )
    )
    ledger_raw = all(
        (
            ledger.both_committed_shears,
            ledger.zero_four_trace_equal,
            ledger.zero_four_determinant_equal,
            ledger.rho_zero_equals_rho_four,
            ledger.every_even_determinant_one,
            ledger.exact_no_float,
        )
    )
    classes_raw = all(
        (
            classes.trace_classes_exact,
            classes.determinant_classes_exact,
            classes.trace_shift_four_rule,
            classes.trace_conjugation_rule,
            classes.four_distinct_trace_classes,
            classes.both_committed_shears,
        )
    )
    cross_size_raw = all(
        (
            cross_size.both_committed_shears,
            cross_size.primary_z6_equals_z8,
            cross_size.secondary_z6_equals_z8,
            cross_size.primary_pinned_rational,
            cross_size.secondary_pinned_rational,
            cross_size.displayed_pins_exact,
            cross_size.exact_no_float,
        )
    )
    isospectral_raw = all(
        (
            isospectral.z8_primary_all_coefficients,
            isospectral.z8_secondary_all_coefficients,
            isospectral.z6_primary_all_coefficients,
            isospectral.z6_secondary_all_coefficients,
            isospectral.monic_degree_eight,
            isospectral.exact_no_float,
        )
    )
    refuted_raw = all(
        (
            refuted.one_slice_shift_exact,
            refuted.primary_conjugacy_residual_nonzero,
            refuted.secondary_conjugacy_residual_nonzero,
            refuted.exact_no_float,
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

    # Every certificate and raw gate is captured before a mutation flag can
    # act.  A mutation negates exactly one copied gate value, so no dependent
    # certificate or neighboring gate can cascade.
    raw_gates = {
        "A": authority_raw,
        "B": same_family_raw,
        "C": ledger_raw,
        "D": classes_raw,
        "E": cross_size_raw,
        "F": isospectral_raw,
        "G": refuted_raw,
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
        "main, Block 138 parent artifacts, and committed Block 136 artifacts are content-bound",
        gate_values["A"],
    )
    checks.check(
        "B-same-family",
        "only spatial extent, exact root field, and cyclic projectors change in the exact Z8 rebuild",
        gate_values["B"],
    )
    checks.check(
        "C-ledger-completion",
        "rho_0=rho_4 and every even-momentum determinant is one at both committed shears",
        gate_values["C"],
    )
    checks.check(
        "D-two-rule-classes",
        "the exact trace and determinant classes obey shift-four equality and momentum conjugation",
        gate_values["D"],
    )
    checks.check(
        "E-cross-size-law",
        "the pinned k=0 trace is exactly equal at Z6 and Z8 for both committed shears",
        gate_values["E"],
    )
    checks.check(
        "F-isospectrality",
        "k=0 and k=N/2 blocks have identical characteristic-polynomial coefficients at Z6 and Z8",
        gate_values["F"],
    )
    checks.check(
        "G-refuted-intertwiner",
        "the exact one-slice-shift conjugacy residual is nonzero at both Z8 shears",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the bounded upgrade, negative mechanism, firewalls, pinned rationals, and exact N5 fence are present",
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
