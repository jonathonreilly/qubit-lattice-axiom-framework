#!/usr/bin/env python3
"""Finite diagonal-affine comparator for a conditional regression fixture.

This support utility transforms already-produced fixture outputs. It has no
source-domain candidate interface and derives no scientific interpretation.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = "docs/RESPONSE_COMPARISON_HARNESS_CYCLE749_SUPPORT_NOTE_2026-07-28.md"
FIXTURE_PATH = "outputs/response_comparison_harness_cycle749_fixture_2026_07_28.json"
AUDIT_INPUT_PATHS = (
    "outputs/response_comparison_harness_cycle749_fixture_2026_07_28.json",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/carried_internal_species_source_field_ledger_repair_2026_07_17.py",
    "scripts/carried_source_recurrent_tagged_block_cycle316_2026_07_18.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/physical_cycle269_coherent_cubic_pair_orbit_2026_07_17.py",
    "scripts/physical_cycle269_coin_stream_contact_common_refinement_cycle304_2026_07_17.py",
    "scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py",
    "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py",
    "scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py",
    "scripts/physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17.py",
    "scripts/physical_cycle269_joint_six_mode_coin_lift_cycle302_2026_07_17.py",
    "scripts/physical_cycle269_local_contact_intertwiner_2026_07_17.py",
    "scripts/physical_cycle269_local_fock_extension_cycle312_2026_07_18.py",
    "scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py",
    "scripts/physical_cycle269_position_growing_recurrent_compiler_cycle307_2026_07_17.py",
    "scripts/physical_cycle269_reference_relative_localized_pair_lift_2026_07_17.py",
    "scripts/physical_cycle269_staggered_reservoir_catchup_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/proper_cubic_recoil_balanced_carried_source_cycle318_2026_07_18.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
    "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATHS = AUDIT_INPUT_PATHS[1:]
PASS = 0
FAIL = 0

Vector = tuple[Fraction, Fraction, Fraction]
RecoilRow = tuple[Vector, Vector, Vector]
Matrix = tuple[
    tuple[Fraction, Fraction],
    tuple[Fraction, Fraction],
]
ResponseRow = tuple[int, Matrix]


def check(label: str, condition: bool, detail: object = "") -> None:
    """Emit the runner's human-readable result format."""
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def require_keys(value: object, expected: set[str], label: str) -> dict[str, Any]:
    require(isinstance(value, dict), f"{label} must be an object")
    require(set(value) == expected, f"{label} keys differ")
    return value


def parse_fraction(value: object, label: str) -> Fraction:
    require(isinstance(value, str) and value != "", f"{label} must be a string")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError(f"{label} is not an exact rational") from error


@dataclass(frozen=True)
class Fixture:
    recoil_rows: tuple[RecoilRow, ...]
    response_rows: tuple[ResponseRow, ...]
    strict_upper_bound: Fraction
    drift_upper_bound: Fraction
    fixture_sha256: str
    source_sha256: dict[str, str]


def parse_vector(value: object, label: str) -> Vector:
    require(isinstance(value, list) and len(value) == 3, f"{label} shape")
    return tuple(
        parse_fraction(component, f"{label}[{index}]")
        for index, component in enumerate(value)
    )  # type: ignore[return-value]


def load_fixture() -> Fixture:
    fixture_file = ROOT / FIXTURE_PATH
    raw = fixture_file.read_bytes()
    data = require_keys(
        json.loads(raw),
        {
            "fixture_kind",
            "normalization_and_supplies",
            "provenance",
            "recoil_rows",
            "response_rows",
            "schema_version",
            "thresholds",
        },
        "fixture",
    )
    require(data["schema_version"] == 1, "fixture schema_version")
    require(
        data["fixture_kind"] == "conditional_software_regression_fixture",
        "fixture kind",
    )
    require_keys(
        data["normalization_and_supplies"],
        {"cycle320", "cycle322", "scientific_authority"},
        "normalization_and_supplies",
    )
    require(
        data["normalization_and_supplies"]["scientific_authority"] == "none",
        "fixture authority",
    )

    provenance = require_keys(
        data["provenance"],
        {"source_closure_sha256", "source_scope"},
        "provenance",
    )
    source_sha256 = provenance["source_closure_sha256"]
    require(isinstance(source_sha256, dict), "source hash map")
    require(
        tuple(sorted(source_sha256)) == tuple(sorted(SOURCE_PATHS)),
        "source closure differs from AUDIT_INPUT_PATHS",
    )
    require(
        all(
            isinstance(digest, str)
            and len(digest) == 64
            and set(digest) <= set("0123456789abcdef")
            for digest in source_sha256.values()
        ),
        "source hash syntax",
    )
    mismatches = {
        path: {
            "expected": source_sha256[path],
            "actual": sha256_path(ROOT / path),
        }
        for path in SOURCE_PATHS
        if not (ROOT / path).is_file()
        or sha256_path(ROOT / path) != source_sha256[path]
    }
    require(not mismatches, f"source closure drift: {mismatches}")

    threshold_data = require_keys(
        data["thresholds"],
        {"drift_upper_bound", "strict_upper_bound"},
        "thresholds",
    )
    strict_upper_bound = parse_fraction(
        threshold_data["strict_upper_bound"], "strict_upper_bound"
    )
    drift_upper_bound = parse_fraction(
        threshold_data["drift_upper_bound"], "drift_upper_bound"
    )
    require(
        Fraction(0) < strict_upper_bound < drift_upper_bound,
        "threshold ordering",
    )

    recoil_data = data["recoil_rows"]
    require(isinstance(recoil_data, list) and len(recoil_data) == 6, "recoil rows")
    recoil_rows: list[RecoilRow] = []
    for index, raw_row in enumerate(recoil_data):
        row = require_keys(
            raw_row,
            {"auxiliary", "direction_index", "matter", "mediator"},
            f"recoil row {index}",
        )
        require(row["direction_index"] == index, f"recoil row {index} index")
        recoil_rows.append(
            (
                parse_vector(row["matter"], f"recoil row {index} matter"),
                parse_vector(row["mediator"], f"recoil row {index} mediator"),
                parse_vector(row["auxiliary"], f"recoil row {index} auxiliary"),
            )
        )

    response_data = data["response_rows"]
    require(
        isinstance(response_data, list) and len(response_data) == 3,
        "response rows",
    )
    response_rows: list[ResponseRow] = []
    for index, raw_row in enumerate(response_data):
        row = require_keys(raw_row, {"L", "matrix"}, f"response row {index}")
        require(
            isinstance(row["L"], int) and not isinstance(row["L"], bool),
            f"response row {index} L",
        )
        raw_matrix = row["matrix"]
        require(
            isinstance(raw_matrix, list)
            and len(raw_matrix) == 2
            and all(isinstance(matrix_row, list) and len(matrix_row) == 2 for matrix_row in raw_matrix),
            f"response row {index} matrix shape",
        )
        matrix: Matrix = tuple(
            tuple(
                parse_fraction(
                    raw_matrix[row_index][column_index],
                    f"response row {index} matrix[{row_index}][{column_index}]",
                )
                for column_index in range(2)
            )
            for row_index in range(2)
        )  # type: ignore[assignment]
        response_rows.append((row["L"], matrix))

    return Fixture(
        recoil_rows=tuple(recoil_rows),
        response_rows=tuple(response_rows),
        strict_upper_bound=strict_upper_bound,
        drift_upper_bound=drift_upper_bound,
        fixture_sha256=hashlib.sha256(raw).hexdigest(),
        source_sha256=dict(source_sha256),
    )


@dataclass(frozen=True)
class DiagonalAffineFixtureTransform:
    """Supplied transform of already-produced fixture output entries."""

    name: str
    recoil_multipliers: tuple[Fraction, Fraction, Fraction]
    response_multipliers: tuple[Fraction, Fraction, Fraction, Fraction]
    offsets: tuple[
        Fraction,
        Fraction,
        Fraction,
        Fraction,
        Fraction,
        Fraction,
        Fraction,
    ]
    role: str


ZERO_OFFSETS = (Fraction(0),) * 7
TRANSFORMS = (
    DiagonalAffineFixtureTransform(
        "identity",
        (Fraction(1),) * 3,
        (Fraction(1),) * 4,
        ZERO_OFFSETS,
        "construction check",
    ),
    DiagonalAffineFixtureTransform(
        "uniform_sign_reversal",
        (Fraction(-1),) * 3,
        (Fraction(-1),) * 4,
        ZERO_OFFSETS,
        "supplied rejection control",
    ),
    DiagonalAffineFixtureTransform(
        "matter_coefficient_perturbation",
        (Fraction(5_000_000_001, 5_000_000_000), Fraction(1), Fraction(1)),
        (Fraction(1),) * 4,
        ZERO_OFFSETS,
        "supplied drift control",
    ),
    DiagonalAffineFixtureTransform(
        "uniform_magnitude_doubling",
        (Fraction(2),) * 3,
        (Fraction(2),) * 4,
        ZERO_OFFSETS,
        "supplied rejection control",
    ),
)
EXPECTED_LABELS = {
    "identity": "ACCEPT",
    "uniform_sign_reversal": "REJECT",
    "matter_coefficient_perturbation": "DRIFT",
    "uniform_magnitude_doubling": "REJECT",
}


def maximum(values: list[Fraction]) -> Fraction:
    return max(values, default=Fraction(0))


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def evaluate_transform(
    transform: DiagonalAffineFixtureTransform,
    fixture: Fixture,
) -> dict[str, object]:
    recoil_entry_residuals: list[Fraction] = []
    balance_residuals: list[Fraction] = []
    for expected_row in fixture.recoil_rows:
        actual_row = tuple(
            tuple(
                transform.recoil_multipliers[component] * value
                + transform.offsets[component]
                for value in expected_row[component]
            )
            for component in range(3)
        )
        recoil_entry_residuals.extend(
            abs(actual_row[component][axis] - expected_row[component][axis])
            for component in range(3)
            for axis in range(3)
        )
        balance_residuals.extend(
            abs(sum(actual_row[component][axis] for component in range(3)))
            for axis in range(3)
        )

    response_entry_residuals: list[Fraction] = []
    for _length, expected_matrix in fixture.response_rows:
        flat = (
            expected_matrix[0][0],
            expected_matrix[0][1],
            expected_matrix[1][0],
            expected_matrix[1][1],
        )
        actual = tuple(
            transform.response_multipliers[index] * value
            + transform.offsets[3 + index]
            for index, value in enumerate(flat)
        )
        response_entry_residuals.extend(
            abs(actual[index] - flat[index]) for index in range(4)
        )

    residuals = {
        "recoil_balance": maximum(balance_residuals),
        "recoil_entries": maximum(recoil_entry_residuals),
        "response_entries": maximum(response_entry_residuals),
    }
    failed = tuple(
        name
        for name, residual in sorted(residuals.items())
        if residual >= fixture.strict_upper_bound
    )
    largest = maximum(list(residuals.values()))
    if not failed:
        label = "ACCEPT"
    elif largest <= fixture.drift_upper_bound:
        label = "DRIFT"
    else:
        label = "REJECT"
    return {
        "failed_criteria": list(failed),
        "label": label,
        "largest_residual": fraction_text(largest),
        "residuals": {
            name: fraction_text(value) for name, value in sorted(residuals.items())
        },
        "transform": transform.name,
    }


def main() -> int:
    started = time.monotonic()
    try:
        fixture = load_fixture()
    except Exception as error:
        check("A fixture schema and pinned source closure load", False, repr(error))
        print(
            json.dumps(
                {
                    "artifact_kind": "conditional_software_regression_comparator",
                    "fail": FAIL,
                    "note_path": NOTE_PATH,
                    "pass": PASS,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 1

    check(
        "A declared inputs cover fixture plus pinned source closure",
        DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and len(AUDIT_INPUT_PATHS) == 33
        and len(set(AUDIT_INPUT_PATHS)) == len(AUDIT_INPUT_PATHS)
        and tuple(sorted(SOURCE_PATHS)) == tuple(sorted(fixture.source_sha256)),
        {"declared_input_count": len(AUDIT_INPUT_PATHS)},
    )
    check(
        "A fixture schema and all pinned source hashes verify",
        len(fixture.source_sha256) == 32,
        {
            "fixture_sha256": fixture.fixture_sha256,
            "source_count": len(fixture.source_sha256),
        },
    )

    normalized_recoil = all(
        row[1] == row[2]
        and row[0] == tuple(-2 * component for component in row[1])
        and sum(abs(component) for component in row[1]) == 1
        for row in fixture.recoil_rows
    )
    check(
        "B fixture contains six normalized coefficient-ledger rows",
        normalized_recoil and len(set(row[1] for row in fixture.recoil_rows)) == 6,
        {"row_count": len(fixture.recoil_rows)},
    )
    check(
        "B fixture contains the declared three finite response tables",
        tuple(length for length, _matrix in fixture.response_rows) == (3, 4, 6)
        and all(
            all(value.denominator > 0 for row in matrix for value in row)
            for _length, matrix in fixture.response_rows
        ),
        {"sizes": [length for length, _matrix in fixture.response_rows]},
    )
    check(
        "B supplied software thresholds are ordered",
        fixture.strict_upper_bound == Fraction(3, 10_000_000_000)
        and fixture.drift_upper_bound == Fraction(1, 1_000_000),
        {
            "accept_requires": "residual < 3e-10",
            "drift_upper_bound": "1e-6",
        },
    )

    evaluations = {
        transform.name: evaluate_transform(transform, fixture)
        for transform in TRANSFORMS
    }
    actual_labels = {
        name: result["label"] for name, result in evaluations.items()
    }
    check(
        "C identity construction row receives ACCEPT",
        actual_labels["identity"] == "ACCEPT",
        evaluations["identity"],
    )
    check(
        "C uniform sign reversal receives REJECT",
        actual_labels["uniform_sign_reversal"] == "REJECT",
        evaluations["uniform_sign_reversal"],
    )
    check(
        "C supplied coefficient perturbation receives DRIFT",
        actual_labels["matter_coefficient_perturbation"] == "DRIFT"
        and evaluations["matter_coefficient_perturbation"]["largest_residual"]
        == "1/2500000000",
        evaluations["matter_coefficient_perturbation"],
    )
    check(
        "C uniform magnitude doubling receives REJECT",
        actual_labels["uniform_magnitude_doubling"] == "REJECT",
        evaluations["uniform_magnitude_doubling"],
    )
    check(
        "C all four supplied software labels match the fixed table",
        actual_labels == EXPECTED_LABELS,
        actual_labels,
    )

    equality_transform = DiagonalAffineFixtureTransform(
        "strict_boundary_equality",
        (
            Fraction(20_000_000_003, 20_000_000_000),
            Fraction(1),
            Fraction(1),
        ),
        (Fraction(1),) * 4,
        ZERO_OFFSETS,
        "strict-boundary regression",
    )
    equality_result = evaluate_transform(equality_transform, fixture)
    check(
        "D residual equal to strict upper bound is not ACCEPT",
        equality_result["largest_residual"] == "3/10000000000"
        and equality_result["label"] == "DRIFT"
        and "recoil_entries" in equality_result["failed_criteria"],
        equality_result,
    )

    current_fixture_sha = sha256_path(ROOT / FIXTURE_PATH)
    current_source_sha = {
        path: sha256_path(ROOT / path) for path in SOURCE_PATHS
    }
    check(
        "E fixture and pinned source bytes remain stable during execution",
        current_fixture_sha == fixture.fixture_sha256
        and current_source_sha == fixture.source_sha256,
        {
            "fixture_stable": current_fixture_sha == fixture.fixture_sha256,
            "source_closure_stable": current_source_sha == fixture.source_sha256,
        },
    )

    certificate = {
        "artifact_kind": "conditional_software_regression_comparator",
        "evaluations": evaluations,
        "expected_labels": EXPECTED_LABELS,
        "fail": FAIL,
        "fixture_path": FIXTURE_PATH,
        "fixture_sha256": fixture.fixture_sha256,
        "note_path": NOTE_PATH,
        "pass": PASS,
        "runtime_sec": round(time.monotonic() - started, 6),
        "scope": {
            "candidate_interface": "none; transforms fixture outputs only",
            "classification_labels": "local software conventions",
            "scientific_authority": "none",
        },
        "source_closure_count": len(fixture.source_sha256),
        "strict_boundary_probe": equality_result,
        "thresholds": {
            "accept_rule": "all residuals strictly below strict_upper_bound",
            "drift_upper_bound": fraction_text(fixture.drift_upper_bound),
            "strict_upper_bound": fraction_text(fixture.strict_upper_bound),
        },
    }
    print(json.dumps(certificate, sort_keys=True, separators=(",", ":")))
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
