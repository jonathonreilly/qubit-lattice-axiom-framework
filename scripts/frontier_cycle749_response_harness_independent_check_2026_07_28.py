#!/usr/bin/env python3
"""Independent exact-arithmetic check of the Cycle-749 support comparator.

The checker does not import or extract implementation constants from the
primary. It builds its oracle from literal transform data and the committed
fixture, then compares that oracle with a clean SHA-pinned primary subprocess.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = "docs/RESPONSE_COMPARISON_HARNESS_CYCLE749_SUPPORT_NOTE_2026-07-28.md"
PRIMARY_PATH = "scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py"
FIXTURE_PATH = "outputs/response_comparison_harness_cycle749_fixture_2026_07_28.json"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py",
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

from copy import deepcopy
from fractions import Fraction
import ast
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATHS = AUDIT_INPUT_PATHS[2:]
PRIMARY_SHA256 = "480f704ca1b8675e993ba26a07a661dcb54b87f94b72e368c5ae4714e435e21d"
PASS = 0
FAIL = 0

STRICT_UPPER_BOUND = Fraction(3, 10_000_000_000)
DRIFT_UPPER_BOUND = Fraction(1, 1_000_000)
ZERO_OFFSETS = (Fraction(0),) * 7

# These are independent literal oracle inputs, not values extracted from the
# primary source.
ORACLE_TRANSFORMS = {
    "identity": (
        (Fraction(1),) * 3,
        (Fraction(1),) * 4,
        ZERO_OFFSETS,
    ),
    "uniform_sign_reversal": (
        (Fraction(-1),) * 3,
        (Fraction(-1),) * 4,
        ZERO_OFFSETS,
    ),
    "matter_coefficient_perturbation": (
        (Fraction(5_000_000_001, 5_000_000_000), Fraction(1), Fraction(1)),
        (Fraction(1),) * 4,
        ZERO_OFFSETS,
    ),
    "uniform_magnitude_doubling": (
        (Fraction(2),) * 3,
        (Fraction(2),) * 4,
        ZERO_OFFSETS,
    ),
}
ORACLE_LABELS = {
    "identity": "ACCEPT",
    "uniform_sign_reversal": "REJECT",
    "matter_coefficient_perturbation": "DRIFT",
    "uniform_magnitude_doubling": "REJECT",
}


def check(label: str, condition: bool, detail: object = "") -> None:
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


def exact_object(value: object, keys: set[str], label: str) -> dict[str, Any]:
    require(isinstance(value, dict), f"{label} must be an object")
    require(set(value) == keys, f"{label} keys differ")
    return value


def rational(value: object, label: str) -> Fraction:
    require(isinstance(value, str) and value != "", f"{label} must be a string")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError(f"{label} is not rational") from error


def parse_fixture() -> tuple[
    dict[str, Any],
    tuple[tuple[tuple[Fraction, ...], ...], ...],
    tuple[tuple[int, tuple[Fraction, ...]], ...],
    str,
]:
    raw = (ROOT / FIXTURE_PATH).read_bytes()
    payload = exact_object(
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
    require(payload["schema_version"] == 1, "schema version")
    require(
        payload["fixture_kind"] == "conditional_software_regression_fixture",
        "fixture kind",
    )
    thresholds = exact_object(
        payload["thresholds"],
        {"drift_upper_bound", "strict_upper_bound"},
        "thresholds",
    )
    require(
        rational(thresholds["strict_upper_bound"], "strict threshold")
        == STRICT_UPPER_BOUND,
        "strict threshold",
    )
    require(
        rational(thresholds["drift_upper_bound"], "drift threshold")
        == DRIFT_UPPER_BOUND,
        "drift threshold",
    )

    recoil_rows = []
    require(
        isinstance(payload["recoil_rows"], list)
        and len(payload["recoil_rows"]) == 6,
        "recoil row count",
    )
    for index, raw_row in enumerate(payload["recoil_rows"]):
        row = exact_object(
            raw_row,
            {"auxiliary", "direction_index", "matter", "mediator"},
            f"recoil row {index}",
        )
        require(row["direction_index"] == index, f"recoil row {index} index")
        components = []
        for name in ("matter", "mediator", "auxiliary"):
            vector = row[name]
            require(
                isinstance(vector, list) and len(vector) == 3,
                f"recoil row {index} {name}",
            )
            components.append(
                tuple(
                    rational(value, f"recoil row {index} {name}[{axis}]")
                    for axis, value in enumerate(vector)
                )
            )
        recoil_rows.append(tuple(components))

    response_rows = []
    require(
        isinstance(payload["response_rows"], list)
        and len(payload["response_rows"]) == 3,
        "response row count",
    )
    for index, raw_row in enumerate(payload["response_rows"]):
        row = exact_object(raw_row, {"L", "matrix"}, f"response row {index}")
        require(
            isinstance(row["L"], int) and not isinstance(row["L"], bool),
            f"response row {index} L",
        )
        matrix = row["matrix"]
        require(
            isinstance(matrix, list)
            and len(matrix) == 2
            and all(isinstance(matrix_row, list) and len(matrix_row) == 2 for matrix_row in matrix),
            f"response row {index} matrix",
        )
        response_rows.append(
            (
                row["L"],
                tuple(
                    rational(matrix[r][c], f"response row {index}[{r}][{c}]")
                    for r in range(2)
                    for c in range(2)
                ),
            )
        )

    return (
        payload,
        tuple(recoil_rows),
        tuple(response_rows),
        hashlib.sha256(raw).hexdigest(),
    )


def exact_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def oracle_evaluate(
    name: str,
    recoil_rows: tuple[tuple[tuple[Fraction, ...], ...], ...],
    response_rows: tuple[tuple[int, tuple[Fraction, ...]], ...],
    transform: tuple[
        tuple[Fraction, Fraction, Fraction],
        tuple[Fraction, Fraction, Fraction, Fraction],
        tuple[Fraction, ...],
    ],
) -> dict[str, object]:
    recoil_multipliers, response_multipliers, offsets = transform
    recoil_entry_max = Fraction(0)
    balance_max = Fraction(0)
    for expected in recoil_rows:
        actual = tuple(
            tuple(
                recoil_multipliers[component] * value + offsets[component]
                for value in expected[component]
            )
            for component in range(3)
        )
        recoil_entry_max = max(
            recoil_entry_max,
            *(
                abs(actual[component][axis] - expected[component][axis])
                for component in range(3)
                for axis in range(3)
            ),
        )
        balance_max = max(
            balance_max,
            *(
                abs(sum(actual[component][axis] for component in range(3)))
                for axis in range(3)
            ),
        )

    response_entry_max = Fraction(0)
    for _length, expected in response_rows:
        actual = tuple(
            response_multipliers[index] * value + offsets[3 + index]
            for index, value in enumerate(expected)
        )
        response_entry_max = max(
            response_entry_max,
            *(abs(actual[index] - expected[index]) for index in range(4)),
        )

    residuals = {
        "recoil_balance": balance_max,
        "recoil_entries": recoil_entry_max,
        "response_entries": response_entry_max,
    }
    failed = [
        criterion
        for criterion, residual in sorted(residuals.items())
        if residual >= STRICT_UPPER_BOUND
    ]
    largest = max(residuals.values())
    if not failed:
        label = "ACCEPT"
    elif largest <= DRIFT_UPPER_BOUND:
        label = "DRIFT"
    else:
        label = "REJECT"
    return {
        "failed_criteria": failed,
        "label": label,
        "largest_residual": exact_text(largest),
        "residuals": {
            criterion: exact_text(value)
            for criterion, value in sorted(residuals.items())
        },
        "transform": name,
    }


def run_primary() -> dict[str, object]:
    environment = os.environ.copy()
    environment.pop("PYTHONPATH", None)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, str(ROOT / PRIMARY_PATH)],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    json_lines = [
        line for line in completed.stdout.splitlines() if line.startswith("{")
    ]
    certificate: object = json.loads(json_lines[-1]) if json_lines else {}
    return {
        "certificate": certificate,
        "exit_code": completed.returncode,
        "fail_lines": [
            line for line in completed.stdout.splitlines() if line.startswith("FAIL ")
        ],
        "stderr": completed.stderr[-2000:],
    }


def main() -> int:
    started = time.monotonic()
    try:
        payload, recoil_rows, response_rows, fixture_sha = parse_fixture()
    except Exception as error:
        check("A independent fixture parser succeeds", False, repr(error))
        return 1

    provenance = exact_object(
        payload["provenance"],
        {"source_closure_sha256", "source_scope"},
        "provenance",
    )
    expected_source_sha = provenance["source_closure_sha256"]
    actual_source_sha = {
        path: sha256_path(ROOT / path) for path in SOURCE_PATHS
    }
    check(
        "A declared inputs cover primary, fixture, and pinned source closure",
        len(AUDIT_INPUT_PATHS) == 34
        and len(set(AUDIT_INPUT_PATHS)) == len(AUDIT_INPUT_PATHS)
        and isinstance(expected_source_sha, dict)
        and tuple(sorted(expected_source_sha)) == tuple(sorted(SOURCE_PATHS)),
        {"declared_input_count": len(AUDIT_INPUT_PATHS)},
    )
    check(
        "A independent source-hash verification is complete",
        actual_source_sha == expected_source_sha and len(actual_source_sha) == 32,
        {"source_count": len(actual_source_sha)},
    )
    check(
        "A primary source matches the independent literal SHA pin",
        sha256_path(ROOT / PRIMARY_PATH) == PRIMARY_SHA256,
        {"primary_sha256": sha256_path(ROOT / PRIMARY_PATH)},
    )

    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    imported_modules = {
        alias.name
        for node in ast.walk(own_tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    }
    check(
        "A checker does not import the primary module",
        "frontier_cycle749_response_comparison_harness_2026_07_28"
        not in imported_modules,
        {"import_count": len(imported_modules)},
    )

    normalized_rows = all(
        row[1] == row[2]
        and row[0] == tuple(-2 * component for component in row[1])
        and sum(abs(component) for component in row[1]) == 1
        for row in recoil_rows
    )
    check(
        "B independent exact parser recovers normalized coefficient rows",
        normalized_rows
        and len(set(row[1] for row in recoil_rows)) == 6,
        {"row_count": len(recoil_rows)},
    )
    check(
        "B independent exact parser recovers three response tables",
        tuple(length for length, _values in response_rows) == (3, 4, 6),
        {"sizes": [length for length, _values in response_rows]},
    )

    oracle = {
        name: oracle_evaluate(name, recoil_rows, response_rows, transform)
        for name, transform in ORACLE_TRANSFORMS.items()
    }
    oracle_labels = {name: result["label"] for name, result in oracle.items()}
    check(
        "C independent exact oracle reproduces four supplied labels",
        oracle_labels == ORACLE_LABELS,
        oracle_labels,
    )
    check(
        "C independent drift arithmetic is exactly 4e-10",
        oracle["matter_coefficient_perturbation"]["largest_residual"]
        == "1/2500000000",
        oracle["matter_coefficient_perturbation"],
    )

    equality_transform = (
        (
            Fraction(20_000_000_003, 20_000_000_000),
            Fraction(1),
            Fraction(1),
        ),
        (Fraction(1),) * 4,
        ZERO_OFFSETS,
    )
    equality = oracle_evaluate(
        "strict_boundary_equality",
        recoil_rows,
        response_rows,
        equality_transform,
    )
    epsilon = Fraction(1, 10**20)
    just_below_transform = (
        (
            Fraction(1) + (STRICT_UPPER_BOUND - epsilon) / 2,
            Fraction(1),
            Fraction(1),
        ),
        (Fraction(1),) * 4,
        ZERO_OFFSETS,
    )
    just_below = oracle_evaluate(
        "strict_boundary_just_below",
        recoil_rows,
        response_rows,
        just_below_transform,
    )
    at_drift_transform = (
        (
            Fraction(1) + DRIFT_UPPER_BOUND / 2,
            Fraction(1),
            Fraction(1),
        ),
        (Fraction(1),) * 4,
        ZERO_OFFSETS,
    )
    at_drift = oracle_evaluate(
        "drift_boundary_equality",
        recoil_rows,
        response_rows,
        at_drift_transform,
    )
    above_drift_transform = (
        (
            Fraction(1) + (DRIFT_UPPER_BOUND + epsilon) / 2,
            Fraction(1),
            Fraction(1),
        ),
        (Fraction(1),) * 4,
        ZERO_OFFSETS,
    )
    above_drift = oracle_evaluate(
        "drift_boundary_above",
        recoil_rows,
        response_rows,
        above_drift_transform,
    )
    check(
        "D strict-boundary equality is DRIFT while just below is ACCEPT",
        equality["largest_residual"] == "3/10000000000"
        and equality["label"] == "DRIFT"
        and just_below["label"] == "ACCEPT",
        {"at_boundary": equality, "just_below": just_below},
    )
    check(
        "D drift-boundary equality is DRIFT while just above is REJECT",
        at_drift["largest_residual"] == "1/1000000"
        and at_drift["label"] == "DRIFT"
        and above_drift["label"] == "REJECT",
        {"at_boundary": at_drift, "above": above_drift},
    )

    mutated_payload = deepcopy(payload)
    mutated_payload["provenance"]["source_closure_sha256"][SOURCE_PATHS[0]] = "0" * 64
    check(
        "E in-memory provenance mutation is detected",
        mutated_payload["provenance"]["source_closure_sha256"]
        != actual_source_sha,
        {"mutated_path": SOURCE_PATHS[0]},
    )

    primary_run = run_primary()
    certificate = primary_run["certificate"]
    check(
        "F clean primary subprocess exits with no FAIL lines",
        primary_run["exit_code"] == 0
        and not primary_run["fail_lines"]
        and primary_run["stderr"] == "",
        {
            "exit_code": primary_run["exit_code"],
            "fail_lines": primary_run["fail_lines"],
            "stderr": primary_run["stderr"],
        },
    )
    check(
        "F primary certificate has the exact support schema boundary",
        isinstance(certificate, dict)
        and certificate.get("artifact_kind")
        == "conditional_software_regression_comparator"
        and certificate.get("scope")
        == {
            "candidate_interface": "none; transforms fixture outputs only",
            "classification_labels": "local software conventions",
            "scientific_authority": "none",
        }
        and certificate.get("fixture_sha256") == fixture_sha,
        certificate.get("scope") if isinstance(certificate, dict) else certificate,
    )
    check(
        "F primary evaluations match the independent exact oracle",
        isinstance(certificate, dict)
        and certificate.get("evaluations") == oracle,
        {
            "oracle": oracle,
            "primary": certificate.get("evaluations")
            if isinstance(certificate, dict)
            else None,
        },
    )
    check(
        "F primary strict-boundary probe matches the independent oracle",
        isinstance(certificate, dict)
        and certificate.get("strict_boundary_probe") == equality,
        {
            "oracle": equality,
            "primary": certificate.get("strict_boundary_probe")
            if isinstance(certificate, dict)
            else None,
        },
    )

    final_source_sha = {
        path: sha256_path(ROOT / path) for path in SOURCE_PATHS
    }
    check(
        "G fixture, primary, and pinned sources remain stable during execution",
        sha256_path(ROOT / FIXTURE_PATH) == fixture_sha
        and sha256_path(ROOT / PRIMARY_PATH) == PRIMARY_SHA256
        and final_source_sha == expected_source_sha,
        {
            "fixture_stable": sha256_path(ROOT / FIXTURE_PATH) == fixture_sha,
            "primary_stable": sha256_path(ROOT / PRIMARY_PATH) == PRIMARY_SHA256,
            "source_closure_stable": final_source_sha == expected_source_sha,
        },
    )

    output = {
        "artifact_kind": "independent_conditional_software_regression_check",
        "fail": FAIL,
        "fixture_sha256": fixture_sha,
        "note_path": NOTE_PATH,
        "oracle_evaluations": oracle,
        "pass": PASS,
        "primary_sha256": PRIMARY_SHA256,
        "runtime_sec": round(time.monotonic() - started, 6),
        "source_closure_count": len(SOURCE_PATHS),
        "threshold_probes": {
            "drift_above": above_drift,
            "drift_equality": at_drift,
            "strict_below": just_below,
            "strict_equality": equality,
        },
    }
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
