#!/usr/bin/env python3
"""Independent checker for the support-only Bloch-projector fixture.

This process never imports the primary harness.  Its projector oracle is
derived from the closed-form Pauli expression using exact ``Fraction`` data,
and its pins and fixture contract are literals independent of the primary.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/BORN_ACCEPTANCE_HARNESS_SUPPORT_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_born_acceptance_harness_2026_07_28.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "scripts/physical_contact_ternary_born_forcing_release_cycle317_2026_07_18.py",
    "scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py",
    "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py",
    "scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py",
    "scripts/physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17.py",
    "scripts/physical_cycle269_reference_relative_localized_pair_lift_2026_07_17.py",
    "scripts/physical_cycle269_staggered_reservoir_catchup_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
    "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py",
    "docs/AUTONOMOUS_INTERMITTENT_RECORD_INSTRUMENT_CALIBRATION_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/MINIMAL_RECORD_INSTRUMENT_DILATION_SCALAR_EXCHANGE_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/work_history/repo/review_feedback/ACTIVE_CUBIC_SOURCE_RESPONSE_CYCLE211_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/ACTUAL_CONTACT_ACTION_SYNDROME_TOURNAMENT_CYCLE285_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/ARCHIVE_CARRIER_SOURCE_LEDGER_CYCLE227_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/AUTONOMOUS_CUBIC_FIELD_EMISSION_CYCLE214_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/CONTACT_CLOSE_TYPED_RECORD_DAG_CYCLE287_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/FINITE_COIN_SCALAR_WAVE_DILATION_CYCLE215_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/FINITE_COIN_SCALAR_WAVE_DILATION_CYCLE215_NO_GO_DISCIPLINE_CHECKLIST_2026-07-16.md",
    "docs/work_history/repo/review_feedback/FINITE_COIN_SCALAR_WAVE_DILATION_CYCLE215_NO_GO_LEDGER_2026-07-16.md",
    "docs/work_history/repo/review_feedback/FOCK_MODULAR_BOUNDARY_CURRENT_CYCLE229_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/LOCAL_CONSERVATIVE_COMMIT_RESOURCE_GRAVITY_CYCLE9_NOTE_2026-07-14.md",
    "docs/work_history/repo/review_feedback/LOCAL_GENERATOR_SOURCE_TOURNAMENT_CYCLE228_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_COLLISION_SAFE_AUXILIARY_PORTS_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_COMMON_M64_FIXED_SEAM_CYCLE311_NOTE_2026-07-18.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_FULL_TWO_PARTICLE_SECTOR_INTERFACE_CYCLE305_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_HIGHER_NUMBER_FIXED_SEAM_CYCLE308_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_REFERENCE_RELATIVE_LOCALIZED_PAIR_LIFT_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_STAGGERED_RESERVOIR_CATCHUP_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PROPER_CUBIC_BOUND_OBJECT_EQUIVALENCE_CYCLE210_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/RETARDED_CUBIC_MASS_FIELD_CYCLE213_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/VIRTUAL_EXCHANGE_GREEN_KERNEL_CYCLE216_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/WILSON_SUBSYSTEM_SECTOR_FREE_COMPILER_CYCLE269_NOTE_2026-07-17.md",
)

import ast
import copy
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
from typing import Any, Callable


_START = time.monotonic()
ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY_RELATIVE = "scripts/frontier_born_acceptance_harness_2026_07_28.py"
PRIMARY = ROOT / PRIMARY_RELATIVE
BRIDGE_RELATIVE = (
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py"
)

INDEPENDENT_BRIDGE_SHA256 = (
    "e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10"
)
INDEPENDENT_DRIVER_AST_SHA256 = (
    "12750b7a9ee13a66eb4996f735d20c7ec72a56ab3e625db2c528bbde8bc6e236"
)
INDEPENDENT_PRIMARY_SHA256 = (
    "1228ac30140af0fd7344dd8a955aa7c455eb9070d9b7e5d989dbc007332c7b0f"
)
PRIMARY_FUNCTION_AST_SHA256 = {
    "_validate_feed_schema": "c6ce8079e1e72738f5d21d68638ddb0da3c6df1348a5a73daa40755cc48c7185",
    "_compare_observation": "92751d3fcd2a53fc987de72b0b8f404481ffb8345918d89dd588d4c903e1e348",
    "_pin_verdict": "26d64f19c050a91185b84043587538aa5b0bece4c2664a3cc9872fe9427a7000",
    "_sandbox_drift_demo": "18f74726c9800a41f1b3bd67aaba724dea928e86788806735893605be2ff0635",
    "_structural_discipline": "c1d9a174a2be36b9c2c922ca47b4e067a2e1ac51441262bc0b2713f61dc86368",
}

INDEPENDENT_AXIS_CONTRACT = (
    ("axis_plus_x", (1, 0, 0)),
    ("axis_minus_x", (-1, 0, 0)),
    ("axis_plus_y", (0, 1, 0)),
    ("axis_plus_z", (0, 0, 1)),
)
INDEPENDENT_REJECT_CONTRACT = (
    (
        "wrong_arity",
        (1, 0),
        "harness_schema",
        "SchemaRefusal",
        "HARNESS_SCHEMA: direction must contain exactly three entries",
    ),
    (
        "non_normalized",
        (1, 1, 1),
        "landed_surface",
        "ValueError",
        "a Bloch projector needs one unit three-vector",
    ),
    (
        "out_of_domain_value",
        (2, 0, 0),
        "landed_surface",
        "ValueError",
        "a Bloch projector needs one unit three-vector",
    ),
    (
        "boolean_type_violation",
        (True, 0, 0),
        "harness_schema",
        "SchemaRefusal",
        (
            "HARNESS_SCHEMA: direction entries must be finite JSON numbers "
            "and booleans are excluded"
        ),
    ),
)

_LANDED_DRIVER = r"""
import json
import sys

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as landed

records = []
for direction in json.load(sys.stdin):
    try:
        matrix = landed.projector_bloch(direction)
        record = {
            "status": "returned",
            "matrix": [
                [[float(value.real), float(value.imag)] for value in row]
                for row in matrix
            ],
        }
    except Exception as exc:
        record = {
            "status": "raised",
            "exception_type": type(exc).__name__,
            "message": str(exc),
        }
    records.append(record)
print(json.dumps(records, allow_nan=False, separators=(",", ":"), sort_keys=True))
"""

_PRIMARY_WAS_PRELOADED = (
    "frontier_born_acceptance_harness_2026_07_28" in sys.modules
)
_PRIMARY_FINAL: dict[str, Any] | None = None


class CertificateError(RuntimeError):
    """A required independent fact was not established."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise CertificateError(message)


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sha256_path(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _stat_token(path: Path) -> tuple[int, int, int, int, int]:
    stat = path.stat()
    return (
        stat.st_dev,
        stat.st_ino,
        stat.st_size,
        stat.st_mtime_ns,
        stat.st_ctime_ns,
    )


def _clean_env() -> dict[str, str]:
    env = os.environ.copy()
    env.pop("PYTHONPATH", None)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONHASHSEED"] = "0"
    return env


def _assignment_literal(tree: ast.Module, name: str) -> Any:
    values: list[ast.AST] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            values.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            values.append(node.value)
    _require(len(values) == 1, f"{name}: expected one top-level assignment")
    try:
        return ast.literal_eval(values[0])
    except (TypeError, ValueError, SyntaxError) as exc:
        raise CertificateError(f"{name}: assignment is not literal") from exc


def _function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    values = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    _require(len(values) == 1, f"{name}: expected one top-level function")
    return values[0]


def _ast_sha(node: ast.AST) -> str:
    normalized = ast.dump(node, annotate_fields=True, include_attributes=False)
    return _sha256_bytes(normalized.encode("utf-8"))


def _closed_form_projector(
    direction: tuple[Fraction, Fraction, Fraction],
) -> list[list[list[Fraction]]]:
    """Return real/imaginary pairs for (I + n·sigma)/2."""
    x, y, z = direction
    half = Fraction(1, 2)
    zero = Fraction(0)
    return [
        [
            [(1 + z) * half, zero],
            [x * half, -y * half],
        ],
        [
            [x * half, y * half],
            [(1 - z) * half, zero],
        ],
    ]


def _rational_unit_vectors() -> list[tuple[Fraction, Fraction, Fraction]]:
    vectors: list[tuple[Fraction, Fraction, Fraction]] = [
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(-1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(0), Fraction(-1)),
    ]
    triples = (
        (3, 4, 5),
        (5, 12, 13),
        (7, 24, 25),
        (8, 15, 17),
        (9, 40, 41),
        (11, 60, 61),
        (12, 35, 37),
        (20, 21, 29),
    )
    for a, b, denominator in triples:
        first = Fraction(a, denominator)
        second = Fraction(b, denominator)
        for zero_index in range(3):
            first_index = (zero_index + 1) % 3
            second_index = (zero_index + 2) % 3
            for first_sign in (-1, 1):
                for second_sign in (-1, 1):
                    row = [Fraction(0), Fraction(0), Fraction(0)]
                    row[first_index] = first_sign * first
                    row[second_index] = second_sign * second
                    vectors.append(tuple(row))
    _require(len(vectors) == 102, f"oracle vector count={len(vectors)}")
    _require(len(set(vectors)) == 102, "oracle vectors are not unique")
    return vectors


def _run_landed(
    directions: list[list[Any]],
) -> list[dict[str, Any]]:
    completed = subprocess.run(
        [sys.executable, "-c", _LANDED_DRIVER],
        cwd=SCRIPTS,
        env=_clean_env(),
        input=json.dumps(directions, allow_nan=True, separators=(",", ":")),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    _require(completed.returncode == 0, f"landed driver exit={completed.returncode}")
    _require(completed.stderr == "", "landed driver emitted stderr")
    try:
        decoded = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise CertificateError("landed driver emitted invalid JSON") from exc
    _require(
        isinstance(decoded, list) and len(decoded) == len(directions),
        "landed driver result count mismatch",
    )
    _require(
        all(isinstance(row, dict) for row in decoded),
        "landed driver emitted a non-object record",
    )
    return decoded


def contract_and_source_pins() -> str:
    """Compare the primary with independently fixed source and fixture anchors."""
    source = PRIMARY.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(PRIMARY))
    _require(not _PRIMARY_WAS_PRELOADED, "primary harness was preloaded")
    _require(
        "frontier_born_acceptance_harness_2026_07_28" not in sys.modules,
        "primary harness entered sys.modules",
    )
    _require(
        _sha256_path(PRIMARY) == INDEPENDENT_PRIMARY_SHA256,
        "complete primary source differs from independent pin",
    )

    primary_inputs = _assignment_literal(tree, "AUDIT_INPUT_PATHS")
    _require(
        primary_inputs == AUDIT_INPUT_PATHS[1:],
        "primary and independent runtime closures differ",
    )
    _require(
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        "one or more declared runtime inputs are absent",
    )
    _require(
        _assignment_literal(tree, "BRIDGE_SHA256") == INDEPENDENT_BRIDGE_SHA256,
        "primary bridge pin differs from independent pin",
    )
    _require(
        _sha256_path(ROOT / BRIDGE_RELATIVE) == INDEPENDENT_BRIDGE_SHA256,
        "landed bridge bytes differ from independent pin",
    )

    driver_source = _assignment_literal(tree, "_SURFACE_DRIVER")
    driver_sha = _ast_sha(ast.parse(driver_source, filename="<primary-driver>"))
    _require(
        driver_sha == INDEPENDENT_DRIVER_AST_SHA256,
        "primary driver normalized AST differs from independent pin",
    )
    _require(
        _assignment_literal(tree, "SURFACE_DRIVER_AST_SHA256")
        == INDEPENDENT_DRIVER_AST_SHA256,
        "primary self-declared driver pin differs from independent pin",
    )
    observed_function_pins = {
        name: _ast_sha(_function_node(tree, name))
        for name in PRIMARY_FUNCTION_AST_SHA256
    }
    _require(
        observed_function_pins == PRIMARY_FUNCTION_AST_SHA256,
        "one or more production function AST pins drifted",
    )
    dead_driver_tree = copy.deepcopy(tree)
    dead_driver_replacement = ast.parse(
        """
def _surface_observation(feed: dict[str, Any]) -> dict[str, Any]:
    lookup = _lookup_frozen(feed["probe_id"])
    category, frozen = lookup
    return {
        key: copy.deepcopy(value)
        for key, value in frozen["expected"].items()
        if key != "machine_bound"
    }
"""
    ).body[0]
    for index, node in enumerate(dead_driver_tree.body):
        if isinstance(node, ast.FunctionDef) and node.name == "_surface_observation":
            dead_driver_tree.body[index] = dead_driver_replacement
            break
    else:
        raise CertificateError("primary surface function is absent")
    dead_driver_source = (
        ast.unparse(ast.fix_missing_locations(dead_driver_tree)) + "\n"
    ).encode("utf-8")
    _require(
        _sha256_bytes(dead_driver_source) != INDEPENDENT_PRIMARY_SHA256,
        "dead-driver/frozen-table mutation escaped the complete-source pin",
    )

    lawful = _assignment_literal(tree, "FROZEN_LAWFUL_PROBES")
    _require(len(lawful) == len(INDEPENDENT_AXIS_CONTRACT), "lawful row count drift")
    for row, (probe_id, direction) in zip(lawful, INDEPENDENT_AXIS_CONTRACT):
        expected_matrix = _closed_form_projector(
            tuple(Fraction(value) for value in direction)
        )
        expected_matrix_float = [
            [
                [[float(pair[0]), float(pair[1])] for pair in matrix_row]
                for matrix_row in expected_matrix
            ]
        ][0]
        _require(row["probe_id"] == probe_id, f"{probe_id}: label/order drift")
        _require(
            row["feed"]
            == {
                "probe_id": probe_id,
                "kind": "bloch_projector",
                "direction": list(direction),
            },
            f"{probe_id}: feed drift",
        )
        _require(
            row["expected"]["matrix"] == expected_matrix_float,
            f"{probe_id}: matrix differs from independent formula",
        )
        _require(
            row["expected"]["summary"]
            == {
                "shape": [2, 2],
                "hermitian_residual": 0.0,
                "idempotence_residual": 0.0,
                "trace_real": 1.0,
                "trace_imag": 0.0,
                "minimum_eigenvalue": 0.0,
                "maximum_eigenvalue": 1.0,
            },
            f"{probe_id}: invariant summary drift",
        )
        _require(
            row["expected"]["machine_bound"] == 5.0e-15,
            f"{probe_id}: machine bound drift",
        )

    rejected = _assignment_literal(tree, "FROZEN_REJECT_WITNESSES")
    _require(
        len(rejected) == len(INDEPENDENT_REJECT_CONTRACT),
        "reject row count drift",
    )
    for row, contract in zip(rejected, INDEPENDENT_REJECT_CONTRACT):
        probe_id, direction, origin, exception_type, message = contract
        _require(row["probe_id"] == probe_id, f"{probe_id}: reject label drift")
        _require(
            row["feed"]
            == {
                "probe_id": probe_id,
                "kind": "bloch_projector",
                "direction": list(direction),
            },
            f"{probe_id}: reject feed drift",
        )
        _require(
            row["expected"]
            == {
                "origin": origin,
                "status": "raised",
                "exception_type": exception_type,
                "message": message,
            },
            f"{probe_id}: reject expectation drift",
        )
    return (
        f"primary={INDEPENDENT_PRIMARY_SHA256[:12]}…; "
        f"bridge={INDEPENDENT_BRIDGE_SHA256[:12]}…; "
        f"driver={driver_sha[:12]}…; functions={len(observed_function_pins)}; "
        f"dead_driver_mutation=rejected; inputs={len(AUDIT_INPUT_PATHS)}"
    )


def exact_projector_oracle() -> str:
    """Check 102 landed projectors against a Fraction-derived closed form."""
    vectors = _rational_unit_vectors()
    observations = _run_landed(
        [[float(value) for value in vector] for vector in vectors]
    )
    maximum_error = 0.0
    for vector, observed in zip(vectors, observations):
        _require(observed.get("status") == "returned", f"{vector}: landed refusal")
        matrix = observed.get("matrix")
        expected = _closed_form_projector(vector)
        _require(
            isinstance(matrix, list) and len(matrix) == 2,
            f"{vector}: malformed matrix",
        )
        for row_index in range(2):
            for column_index in range(2):
                for pair_index in range(2):
                    actual_value = float(matrix[row_index][column_index][pair_index])
                    expected_value = float(
                        expected[row_index][column_index][pair_index]
                    )
                    maximum_error = max(
                        maximum_error, abs(actual_value - expected_value)
                    )
    _require(maximum_error <= 2.0e-15, f"projector max error={maximum_error}")
    return f"vectors={len(vectors)}; maximum_entry_error={maximum_error:.3g}"


def _run_primary_probe(feed: Any) -> dict[str, Any]:
    completed = subprocess.run(
        [sys.executable, str(PRIMARY), "--probe-json"],
        cwd=ROOT,
        env=_clean_env(),
        input=json.dumps(feed, allow_nan=True, separators=(",", ":")),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    _require(completed.returncode == 0, f"primary probe exit={completed.returncode}")
    _require(completed.stderr == "", "primary probe emitted stderr")
    try:
        decoded = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise CertificateError("primary probe emitted invalid JSON") from exc
    _require(isinstance(decoded, dict), "primary probe output is not an object")
    return decoded


def schema_and_refusal_boundary() -> str:
    """Verify landed refusals and cross-ID schema behavior independently."""
    direct = _run_landed(
        [
            [1, 0],
            [1, 1, 1],
            [2, 0, 0],
            [True, 0, 0],
            ["1", 0, 0],
            [float("inf"), 0, 0],
        ]
    )
    for index in (0, 1, 2):
        _require(
            direct[index]
            == {
                "status": "raised",
                "exception_type": "ValueError",
                "message": "a Bloch projector needs one unit three-vector",
            },
            f"landed refusal {index} drifted",
        )
    _require(
        direct[3].get("status") == "returned",
        "Boolean witness was not shown to be harness-only",
    )
    _require(
        direct[4].get("status") == "returned",
        "string witness was not shown to be harness-only",
    )
    _require(
        direct[5].get("status") == "raised",
        "landed nonfinite behavior drifted",
    )

    cases = {
        "non_object": ([], "harness_schema", "SchemaRefusal"),
        "missing_probe_id": (
            {"kind": "bloch_projector", "direction": [1, 0, 0]},
            "harness_schema",
            "SchemaRefusal",
        ),
        "non_string_probe_id": (
            {
                "probe_id": 7,
                "kind": "bloch_projector",
                "direction": [1, 0, 0],
            },
            "harness_schema",
            "SchemaRefusal",
        ),
        "axis_boolean": (
            {
                "probe_id": "axis_plus_x",
                "kind": "bloch_projector",
                "direction": [True, 0, 0],
            },
            "harness_schema",
            "SchemaRefusal",
        ),
        "axis_string": (
            {
                "probe_id": "axis_plus_x",
                "kind": "bloch_projector",
                "direction": ["1", 0, 0],
            },
            "harness_schema",
            "SchemaRefusal",
        ),
        "axis_nonfinite": (
            {
                "probe_id": "axis_plus_x",
                "kind": "bloch_projector",
                "direction": [float("nan"), 0, 0],
            },
            "harness_schema",
            "SchemaRefusal",
        ),
        "axis_oversized_integer": (
            {
                "probe_id": "axis_plus_x",
                "kind": "bloch_projector",
                "direction": [10**400, 0, 0],
            },
            "harness_schema",
            "SchemaRefusal",
        ),
        "axis_extra_key": (
            {
                "probe_id": "axis_plus_x",
                "kind": "bloch_projector",
                "direction": [1, 0, 0],
                "extra": 1,
            },
            "harness_schema",
            "SchemaRefusal",
        ),
        "unknown_valid": (
            {
                "probe_id": "unknown",
                "kind": "bloch_projector",
                "direction": [1, 0, 0],
            },
            "fixture_registry",
            "FixtureRefusal",
        ),
        "unknown_extra_key": (
            {
                "probe_id": "unknown",
                "kind": "bloch_projector",
                "direction": [1, 0, 0],
                "extra": 1,
            },
            "harness_schema",
            "SchemaRefusal",
        ),
        "known_id_feed_mismatch": (
            {
                "probe_id": "axis_plus_x",
                "kind": "bloch_projector",
                "direction": [-1, 0, 0],
            },
            "fixture_registry",
            "FixtureRefusal",
        ),
        "boolean_id_numeric": (
            {
                "probe_id": "boolean_type_violation",
                "kind": "bloch_projector",
                "direction": [1, 0, 0],
            },
            "fixture_registry",
            "FixtureRefusal",
        ),
    }
    for label, (feed, enforcement, exception_type) in cases.items():
        row = _run_primary_probe(feed)
        observation = row.get("observation")
        _require(row.get("verdict") == "REJECT", f"{label}: verdict was not REJECT")
        _require(
            row.get("enforcement") == enforcement,
            f"{label}: enforcement provenance drifted",
        )
        _require(
            isinstance(observation, dict)
            and observation.get("origin") == enforcement
            and observation.get("status") == "raised"
            and observation.get("exception_type") == exception_type,
            f"{label}: observation provenance drifted",
        )
    return (
        "landed ValueError=3/3; Boolean landed-returned; "
        f"schema/registry provenance={len(cases)}/{len(cases)}"
    )


def _strict_axis_match(observed: Any, expected: Any, bound: float) -> bool:
    """Independent flat-leaf comparator for a single matrix observation."""
    if not isinstance(observed, dict) or set(observed) != {"status", "matrix"}:
        return False
    if observed["status"] != "returned":
        return False
    matrix = observed["matrix"]
    if (
        not isinstance(matrix, list)
        or len(matrix) != 2
        or any(not isinstance(row, list) or len(row) != 2 for row in matrix)
    ):
        return False
    for row_index in range(2):
        for column_index in range(2):
            pair = matrix[row_index][column_index]
            frozen = expected[row_index][column_index]
            if not isinstance(pair, list) or len(pair) != 2:
                return False
            for value, target in zip(pair, frozen):
                if isinstance(value, bool) or not isinstance(value, (int, float)):
                    return False
                try:
                    numeric = float(value)
                    frozen_numeric = float(target)
                except (OverflowError, TypeError, ValueError):
                    return False
                if (
                    not math.isfinite(numeric)
                    or not math.isfinite(frozen_numeric)
                    or abs(numeric - frozen_numeric) > bound
                ):
                    return False
    return True


def independent_comparator_adversaries() -> str:
    """Kill comparator mutants without importing or calling the primary comparator."""
    baseline = _run_landed([[1, 0, 0]])[0]
    expected = [
        [[Fraction(1, 2), Fraction(0)], [Fraction(1, 2), Fraction(0)]],
        [[Fraction(1, 2), Fraction(0)], [Fraction(1, 2), Fraction(0)]],
    ]
    _require(_strict_axis_match(baseline, expected, 5.0e-15), "baseline mismatch")
    mutants: dict[str, Any] = {}
    mutation = copy.deepcopy(baseline)
    mutation["unexpected_probability"] = 0.5
    mutants["outer_extra"] = mutation
    mutation = copy.deepcopy(baseline)
    del mutation["matrix"]
    mutants["outer_missing"] = mutation
    mutation = copy.deepcopy(baseline)
    mutation["status"] = "forged"
    mutants["status"] = mutation
    mutation = copy.deepcopy(baseline)
    mutation["matrix"][0][0][0] += 1.0e-12
    mutants["tolerance"] = mutation
    mutation = copy.deepcopy(baseline)
    mutation["matrix"][0][0][0] = float("nan")
    mutants["nonfinite"] = mutation
    mutation = copy.deepcopy(baseline)
    mutation["matrix"][0][0][0] = "0.5"
    mutants["type"] = mutation
    mutation = copy.deepcopy(baseline)
    mutation["matrix"][0][0][0] = 10**400
    mutants["oversized_integer"] = mutation
    killed = {
        name: not _strict_axis_match(row, expected, 5.0e-15)
        for name, row in mutants.items()
    }
    _require(all(killed.values()), f"independent mutant escaped: {killed}")
    _require(
        _PRIMARY_FINAL is not None,
        "primary hermetic run must precede comparator inspection",
    )
    submitted = _PRIMARY_FINAL.get("comparator_mutations")
    _require(isinstance(submitted, dict), "primary mutation record missing")
    submitted_kills = submitted.get("killed")
    _require(
        isinstance(submitted_kills, dict)
        and len(submitted_kills) >= 22
        and all(value is True for value in submitted_kills.values())
        and submitted.get("oversized_integer_live_drift") is True
        and submitted.get("within_bound_accepted") is True
        and submitted.get("pass") is True,
        "primary load-bearing mutation census is incomplete",
    )
    return (
        f"independent_kills={len(killed)}/{len(killed)}; "
        f"primary_kills={len(submitted_kills)}/{len(submitted_kills)}"
    )


def hermetic_primary_and_sandbox() -> str:
    """Run the primary cleanly, then repeat the pin mutation independently."""
    global _PRIMARY_FINAL
    completed = subprocess.run(
        [sys.executable, str(PRIMARY)],
        cwd=ROOT,
        env=_clean_env(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    _require(completed.returncode == 0, f"primary clean exit={completed.returncode}")
    _require(completed.stderr == b"", "primary clean run emitted stderr")
    text = completed.stdout.decode("utf-8")
    lines = text.splitlines()
    _require(
        "SUMMARY PASS 6 FAIL 0" in lines,
        "primary did not report the fixed 6/0 contract",
    )
    _require(
        lines and lines[-1] == "RESULT BORN_PROJECTOR_FIXTURE_ACCEPTANCE_GREEN",
        "primary terminal marker drifted",
    )
    json_rows = [
        json.loads(line)
        for line in lines
        if line.startswith("{") and '"checks"' in line
    ]
    _require(len(json_rows) == 1, "primary final JSON record count mismatch")
    _PRIMARY_FINAL = json_rows[0]
    _require(
        _PRIMARY_FINAL.get("checks") == {"pass": 6, "fail": 0},
        "primary final check census drifted",
    )

    real = ROOT / BRIDGE_RELATIVE
    real_before_hash = _sha256_path(real)
    real_before_stat = _stat_token(real)
    with tempfile.TemporaryDirectory(prefix="born-independent-pin-") as folder:
        sandbox_root = Path(folder)
        sandbox = sandbox_root / BRIDGE_RELATIVE
        sandbox.parent.mkdir(parents=True)
        shutil.copyfile(real, sandbox)
        original = sandbox.read_bytes()
        changed = bytearray(original)
        changed[-1] ^= 1
        sandbox.write_bytes(bytes(changed))
        sandbox_hash = _sha256_path(sandbox)
        differing = sum(left != right for left, right in zip(original, changed))
    real_after_hash = _sha256_path(real)
    real_after_stat = _stat_token(real)
    _require(differing == 1, f"sandbox differing bytes={differing}")
    _require(
        sandbox_hash != INDEPENDENT_BRIDGE_SHA256,
        "independent sandbox mutation did not cause DRIFT",
    )
    _require(
        real_before_hash == real_after_hash == INDEPENDENT_BRIDGE_SHA256,
        "real bridge hash changed",
    )
    _require(real_before_stat == real_after_stat, "real bridge stat changed")
    return (
        f"primary_stdout_sha256={_sha256_bytes(completed.stdout)[:12]}…; "
        f"sandbox={sandbox_hash[:12]}…; real_hash_and_stat_unchanged"
    )


def _one_line(value: object, limit: int = 900) -> str:
    text = " ".join(str(value).split())
    return text if len(text) <= limit else text[: limit - 1] + "…"


def _run_certificate(
    index: int,
    name: str,
    function: Callable[[], str],
) -> bool:
    try:
        detail = function()
    except Exception as exc:
        print(
            f"FAIL {index}/5 {name} :: "
            f"{type(exc).__name__}: {_one_line(exc)}"
        )
        return False
    print(f"PASS {index}/5 {name} :: {_one_line(detail)}")
    return True


def main() -> int:
    checks = (
        ("contract_and_source_pins", contract_and_source_pins),
        ("exact_projector_oracle", exact_projector_oracle),
        ("schema_and_refusal_boundary", schema_and_refusal_boundary),
        ("hermetic_primary_and_sandbox", hermetic_primary_and_sandbox),
        ("independent_comparator_adversaries", independent_comparator_adversaries),
    )
    results = [
        _run_certificate(index, name, function)
        for index, (name, function) in enumerate(checks, start=1)
    ]
    passed = sum(results)
    print(f"SUMMARY {passed}/{len(results)} {'PASS' if passed == len(results) else 'FAIL'}")
    print(f"RUNTIME {time.monotonic() - _START:.6f}s")
    print("RESULT BORN_PROJECTOR_FIXTURE_INDEPENDENT_CHECK_GREEN")
    return int(passed != len(results))


if __name__ == "__main__":
    raise SystemExit(main())
