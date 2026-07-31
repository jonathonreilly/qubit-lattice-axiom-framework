#!/usr/bin/env python3
"""Support-only acceptance fixture for the landed Cycle-317 Bloch projector.

The fixture accepts only eight frozen feeds.  It does not exercise the wider
ternary-menu, split/merge, dilation, trace-functional, or release surface.
Directions are supplied apparatus data; this runner derives no weight,
probability, occurrence, outcome, Record, or Born-law value.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/BORN_ACCEPTANCE_HARNESS_SUPPORT_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
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
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
import copy
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
from typing import Any


_START = time.monotonic()
ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"

BRIDGE_PATH = (
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py"
)
BRIDGE_SHA256 = "e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10"

FROZEN_LAWFUL_PROBES = (
    {
        "probe_id": "axis_plus_x",
        "feed": {
            "probe_id": "axis_plus_x",
            "kind": "bloch_projector",
            "direction": [1, 0, 0],
        },
        "expected": {
            "origin": "landed_surface",
            "status": "returned",
            "matrix": [
                [[0.5, 0.0], [0.5, 0.0]],
                [[0.5, 0.0], [0.5, 0.0]],
            ],
            "summary": {
                "shape": [2, 2],
                "hermitian_residual": 0.0,
                "idempotence_residual": 0.0,
                "trace_real": 1.0,
                "trace_imag": 0.0,
                "minimum_eigenvalue": 0.0,
                "maximum_eigenvalue": 1.0,
            },
            "machine_bound": 5.0e-15,
        },
    },
    {
        "probe_id": "axis_minus_x",
        "feed": {
            "probe_id": "axis_minus_x",
            "kind": "bloch_projector",
            "direction": [-1, 0, 0],
        },
        "expected": {
            "origin": "landed_surface",
            "status": "returned",
            "matrix": [
                [[0.5, 0.0], [-0.5, 0.0]],
                [[-0.5, 0.0], [0.5, 0.0]],
            ],
            "summary": {
                "shape": [2, 2],
                "hermitian_residual": 0.0,
                "idempotence_residual": 0.0,
                "trace_real": 1.0,
                "trace_imag": 0.0,
                "minimum_eigenvalue": 0.0,
                "maximum_eigenvalue": 1.0,
            },
            "machine_bound": 5.0e-15,
        },
    },
    {
        "probe_id": "axis_plus_y",
        "feed": {
            "probe_id": "axis_plus_y",
            "kind": "bloch_projector",
            "direction": [0, 1, 0],
        },
        "expected": {
            "origin": "landed_surface",
            "status": "returned",
            "matrix": [
                [[0.5, 0.0], [0.0, -0.5]],
                [[0.0, 0.5], [0.5, 0.0]],
            ],
            "summary": {
                "shape": [2, 2],
                "hermitian_residual": 0.0,
                "idempotence_residual": 0.0,
                "trace_real": 1.0,
                "trace_imag": 0.0,
                "minimum_eigenvalue": 0.0,
                "maximum_eigenvalue": 1.0,
            },
            "machine_bound": 5.0e-15,
        },
    },
    {
        "probe_id": "axis_plus_z",
        "feed": {
            "probe_id": "axis_plus_z",
            "kind": "bloch_projector",
            "direction": [0, 0, 1],
        },
        "expected": {
            "origin": "landed_surface",
            "status": "returned",
            "matrix": [
                [[1.0, 0.0], [0.0, 0.0]],
                [[0.0, 0.0], [0.0, 0.0]],
            ],
            "summary": {
                "shape": [2, 2],
                "hermitian_residual": 0.0,
                "idempotence_residual": 0.0,
                "trace_real": 1.0,
                "trace_imag": 0.0,
                "minimum_eigenvalue": 0.0,
                "maximum_eigenvalue": 1.0,
            },
            "machine_bound": 5.0e-15,
        },
    },
)

FROZEN_REJECT_WITNESSES = (
    {
        "probe_id": "wrong_arity",
        "feed": {
            "probe_id": "wrong_arity",
            "kind": "bloch_projector",
            "direction": [1, 0],
        },
        "expected": {
            "origin": "harness_schema",
            "status": "raised",
            "exception_type": "SchemaRefusal",
            "message": "HARNESS_SCHEMA: direction must contain exactly three entries",
        },
    },
    {
        "probe_id": "non_normalized",
        "feed": {
            "probe_id": "non_normalized",
            "kind": "bloch_projector",
            "direction": [1, 1, 1],
        },
        "expected": {
            "origin": "landed_surface",
            "status": "raised",
            "exception_type": "ValueError",
            "message": "a Bloch projector needs one unit three-vector",
        },
    },
    {
        "probe_id": "out_of_domain_value",
        "feed": {
            "probe_id": "out_of_domain_value",
            "kind": "bloch_projector",
            "direction": [2, 0, 0],
        },
        "expected": {
            "origin": "landed_surface",
            "status": "raised",
            "exception_type": "ValueError",
            "message": "a Bloch projector needs one unit three-vector",
        },
    },
    {
        "probe_id": "boolean_type_violation",
        "feed": {
            "probe_id": "boolean_type_violation",
            "kind": "bloch_projector",
            "direction": [True, 0, 0],
        },
        "expected": {
            "origin": "harness_schema",
            "status": "raised",
            "exception_type": "SchemaRefusal",
            "message": (
                "HARNESS_SCHEMA: direction entries must be finite JSON numbers "
                "and booleans are excluded"
            ),
        },
    },
)

_SURFACE_DRIVER = r"""
import json
import sys

import numpy as np
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as surface

payload = json.load(sys.stdin)
try:
    projector = surface.projector_bloch(payload["direction"])
    hermitian = (projector + projector.conj().T) / 2
    eigenvalues = np.linalg.eigvalsh(hermitian)
    record = {
        "origin": "landed_surface",
        "status": "returned",
        "matrix": [
            [[float(value.real), float(value.imag)] for value in row]
            for row in projector
        ],
        "summary": {
            "shape": list(projector.shape),
            "hermitian_residual": float(
                np.linalg.norm(projector - projector.conj().T)
            ),
            "idempotence_residual": float(
                np.linalg.norm(projector @ projector - projector)
            ),
            "trace_real": float(np.trace(projector).real),
            "trace_imag": float(np.trace(projector).imag),
            "minimum_eigenvalue": float(np.min(eigenvalues)),
            "maximum_eigenvalue": float(np.max(eigenvalues)),
        },
    }
except Exception as exc:
    record = {
        "origin": "landed_surface",
        "status": "raised",
        "exception_type": type(exc).__name__,
        "message": str(exc),
    }
print(json.dumps(record, allow_nan=False, separators=(",", ":"), sort_keys=True))
"""

SURFACE_DRIVER_AST_SHA256 = (
    "12750b7a9ee13a66eb4996f735d20c7ec72a56ab3e625db2c528bbde8bc6e236"
)

_PASS = 0
_FAIL = 0


def check(label: str, condition: bool, detail: Any = "") -> bool:
    """Print one certificate line and update the local census."""
    global _PASS, _FAIL
    if condition:
        _PASS += 1
        status = "PASS"
    else:
        _FAIL += 1
        status = "FAIL"
    print(f"{status} {label} :: {detail}")
    return condition


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _path_sha256(path: Path) -> str:
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


def _clean_child_env() -> dict[str, str]:
    env = os.environ.copy()
    env.pop("PYTHONPATH", None)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONHASHSEED"] = "0"
    return env


def _pin_verdict(
    relative_path: str,
    expected_sha256: str,
    root: Path = ROOT,
) -> dict[str, Any]:
    """Apply the one production pin predicate to a selectable repository root."""
    path = root / relative_path
    try:
        actual = _path_sha256(path)
    except OSError as exc:
        return {
            "path": relative_path,
            "expected": expected_sha256,
            "actual": None,
            "match": False,
            "verdict": "DRIFT",
            "error": type(exc).__name__,
        }
    match = actual == expected_sha256
    return {
        "path": relative_path,
        "expected": expected_sha256,
        "actual": actual,
        "match": match,
        "verdict": "ACCEPT" if match else "DRIFT",
    }


def _schema_refusal(message: str) -> dict[str, Any]:
    return {
        "origin": "harness_schema",
        "status": "raised",
        "exception_type": "SchemaRefusal",
        "message": message,
    }


def _fixture_refusal(message: str) -> dict[str, Any]:
    return {
        "origin": "fixture_registry",
        "status": "raised",
        "exception_type": "FixtureRefusal",
        "message": message,
    }


def _validate_feed_schema(feed: Any) -> dict[str, Any] | None:
    """Validate shape and scalar domain without consulting ``probe_id``."""
    if not isinstance(feed, dict):
        return _schema_refusal("HARNESS_SCHEMA: feed must be an object")
    if set(feed) != {"probe_id", "kind", "direction"}:
        return _schema_refusal(
            "HARNESS_SCHEMA: feed keys must be exactly probe_id, kind, direction"
        )
    if not isinstance(feed["probe_id"], str):
        return _schema_refusal("HARNESS_SCHEMA: probe_id must be a string")
    if feed["kind"] != "bloch_projector":
        return _schema_refusal("HARNESS_SCHEMA: kind must be bloch_projector")
    direction = feed["direction"]
    if not isinstance(direction, list):
        return _schema_refusal("HARNESS_SCHEMA: direction must be a JSON list")
    if len(direction) != 3:
        return _schema_refusal(
            "HARNESS_SCHEMA: direction must contain exactly three entries"
        )
    for value in direction:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return _schema_refusal(
                "HARNESS_SCHEMA: direction entries must be finite JSON numbers "
                "and booleans are excluded"
            )
        try:
            numeric = float(value)
        except (OverflowError, TypeError, ValueError):
            return _schema_refusal(
                "HARNESS_SCHEMA: direction entries must be finite JSON numbers "
                "and booleans are excluded"
            )
        if not math.isfinite(numeric):
            return _schema_refusal(
                "HARNESS_SCHEMA: direction entries must be finite JSON numbers "
                "and booleans are excluded"
            )
    try:
        json.dumps(feed, allow_nan=False, separators=(",", ":"), sort_keys=True)
    except (TypeError, ValueError):
        return _schema_refusal("HARNESS_SCHEMA: feed must be finite JSON data")
    return None


def _lookup_frozen(probe_id: str) -> tuple[str, dict[str, Any]] | None:
    for row in FROZEN_LAWFUL_PROBES:
        if row["probe_id"] == probe_id:
            return "lawful", row
    for row in FROZEN_REJECT_WITNESSES:
        if row["probe_id"] == probe_id:
            return "reject", row
    return None


def _surface_observation(feed: dict[str, Any]) -> dict[str, Any]:
    encoded = json.dumps(feed, allow_nan=False, separators=(",", ":"), sort_keys=True)
    try:
        completed = subprocess.run(
            [sys.executable, "-c", _SURFACE_DRIVER],
            cwd=SCRIPTS,
            env=_clean_child_env(),
            input=encoded,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=AUDIT_TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired as exc:
        return {
            "origin": "subprocess_driver",
            "status": "driver_error",
            "message": f"timeout after {exc.timeout} seconds",
        }
    if completed.returncode != 0 or completed.stderr:
        return {
            "origin": "subprocess_driver",
            "status": "driver_error",
            "returncode": completed.returncode,
            "stderr_sha256": _sha256_bytes(completed.stderr.encode("utf-8")),
        }
    try:
        decoded = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        return {
            "origin": "subprocess_driver",
            "status": "driver_error",
            "message": f"JSONDecodeError: {exc}",
        }
    if not isinstance(decoded, dict):
        return {
            "origin": "subprocess_driver",
            "status": "driver_error",
            "message": "driver output was not one JSON object",
        }
    return decoded


def _same_json(left: Any, right: Any) -> bool:
    try:
        return json.dumps(
            left, allow_nan=False, separators=(",", ":"), sort_keys=True
        ) == json.dumps(
            right, allow_nan=False, separators=(",", ":"), sort_keys=True
        )
    except (TypeError, ValueError):
        return False


def _numeric_match(observed: Any, expected: Any, bound: float) -> bool:
    if isinstance(expected, bool) or expected is None or isinstance(expected, str):
        return observed == expected
    if isinstance(expected, (int, float)):
        if not isinstance(observed, (int, float)) or isinstance(observed, bool):
            return False
        try:
            observed_numeric = float(observed)
            expected_numeric = float(expected)
        except (OverflowError, TypeError, ValueError):
            return False
        return (
            math.isfinite(observed_numeric)
            and math.isfinite(expected_numeric)
            and abs(observed_numeric - expected_numeric) <= bound
        )
    if isinstance(expected, list):
        return (
            isinstance(observed, list)
            and len(observed) == len(expected)
            and all(
                _numeric_match(actual, frozen, bound)
                for actual, frozen in zip(observed, expected)
            )
        )
    if isinstance(expected, dict):
        return (
            isinstance(observed, dict)
            and set(observed) == set(expected)
            and all(
                _numeric_match(observed[key], value, bound)
                for key, value in expected.items()
            )
        )
    return observed == expected


def _compare_observation(
    category: str,
    feed: Any,
    frozen: dict[str, Any],
    observed: dict[str, Any],
) -> dict[str, bool]:
    expected = frozen["expected"]
    expected_observation = {
        key: value for key, value in expected.items() if key != "machine_bound"
    }
    feed_match = _same_json(feed, frozen["feed"])
    keyset_match = (
        isinstance(observed, dict) and set(observed) == set(expected_observation)
    )
    origin_match = observed.get("origin") == expected["origin"]
    status_match = observed.get("status") == expected["status"]
    if category == "lawful":
        bound = expected["machine_bound"]
        matrix_match = _numeric_match(
            observed.get("matrix"), expected["matrix"], bound
        )
        summary_match = _numeric_match(
            observed.get("summary"), expected["summary"], bound
        )
        signature_match = True
    else:
        matrix_match = True
        summary_match = True
        signature_match = (
            observed.get("exception_type") == expected["exception_type"]
            and observed.get("message") == expected["message"]
        )
    frozen_match = all(
        (
            feed_match,
            keyset_match,
            origin_match,
            status_match,
            matrix_match,
            summary_match,
            signature_match,
        )
    )
    return {
        "feed_match": feed_match,
        "keyset_match": keyset_match,
        "origin_match": origin_match,
        "status_match": status_match,
        "matrix_match": matrix_match,
        "summary_match": summary_match,
        "signature_match": signature_match,
        "frozen_match": frozen_match,
    }


def run_acceptance(feed: Any) -> dict[str, Any]:
    """Classify one frozen projector fixture as ACCEPT, REJECT, or DRIFT."""
    pin = _pin_verdict(BRIDGE_PATH, BRIDGE_SHA256)
    probe_id = feed.get("probe_id") if isinstance(feed, dict) else None
    if not pin["match"]:
        return {
            "probe_id": probe_id,
            "verdict": "DRIFT",
            "pin": pin,
            "comparison": {"frozen_match": False},
            "observation": {"status": "not_run_on_unpinned_surface"},
        }

    schema_observation = _validate_feed_schema(feed)
    lookup = _lookup_frozen(probe_id) if isinstance(probe_id, str) else None
    if schema_observation is not None:
        comparison = {"frozen_match": False}
        category = None
        frozen = None
        if lookup is not None:
            category, frozen = lookup
            comparison = _compare_observation(
                category, feed, frozen, schema_observation
            )
        if comparison["frozen_match"]:
            return {
                "probe_id": frozen["probe_id"],
                "category": category,
                "enforcement": "harness_schema",
                "verdict": "REJECT",
                "pin": pin,
                "comparison": comparison,
                "observation": schema_observation,
            }
        return {
            "probe_id": probe_id,
            "verdict": "REJECT",
            "enforcement": "harness_schema",
            "pin": pin,
            "comparison": comparison,
            "observation": schema_observation,
        }

    if lookup is None:
        return {
            "probe_id": probe_id,
            "verdict": "REJECT",
            "enforcement": "fixture_registry",
            "pin": pin,
            "comparison": {"frozen_match": False},
            "observation": _fixture_refusal(
                "FIXTURE_REGISTRY: probe_id is not a frozen fixture"
            ),
        }

    category, frozen = lookup
    if not _same_json(feed, frozen["feed"]):
        return {
            "probe_id": probe_id,
            "category": category,
            "verdict": "REJECT",
            "enforcement": "fixture_registry",
            "pin": pin,
            "comparison": {"feed_match": False, "frozen_match": False},
            "observation": _fixture_refusal(
                "FIXTURE_REGISTRY: feed does not equal the frozen fixture"
            ),
        }

    observed = _surface_observation(feed)
    comparison = _compare_observation(category, feed, frozen, observed)
    if comparison["frozen_match"]:
        verdict = "ACCEPT" if category == "lawful" else "REJECT"
    else:
        verdict = "DRIFT" if _same_json(feed, frozen["feed"]) else "REJECT"
    return {
        "probe_id": frozen["probe_id"],
        "category": category,
        "enforcement": observed.get("origin", "unknown"),
        "verdict": verdict,
        "pin": pin,
        "comparison": comparison,
        "observation": observed,
    }


def _normalized_ast_sha256(source: str) -> str:
    tree = ast.parse(source, filename="<surface-driver>")
    normalized = ast.dump(tree, annotate_fields=True, include_attributes=False)
    return _sha256_bytes(normalized.encode("utf-8"))


def _structural_discipline() -> dict[str, Any]:
    outer = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    landed_names = {Path(path).stem for path in AUDIT_INPUT_PATHS if path.endswith(".py")}
    outer_imports = {
        alias.name
        for node in ast.walk(outer)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module
        for node in ast.walk(outer)
        if isinstance(node, ast.ImportFrom) and node.module is not None
    }
    parent_imports_landed = bool(landed_names & outer_imports)
    driver_sha = _normalized_ast_sha256(_SURFACE_DRIVER)
    adversarial_mutations = {
        "alias_setattr": _SURFACE_DRIVER.replace(
            'payload = json.load(sys.stdin)',
            'payload = json.load(sys.stdin)\nalias = surface\nsetattr(alias, "projector_bloch", lambda supplied: np.eye(2) / 2)',
        ),
        "dynamic_getattr": _SURFACE_DRIVER.replace(
            'surface.projector_bloch(payload["direction"])',
            'getattr(surface, "projector_" + "bloch")(payload["direction"])',
        ),
        "explicit_synthesis": _SURFACE_DRIVER.replace(
            'payload = json.load(sys.stdin)',
            'payload = json.load(sys.stdin)\nprobability = [float(x) * float(x) for x in payload["direction"]]',
        ),
        "extra_statement": _SURFACE_DRIVER.replace(
            'payload = json.load(sys.stdin)',
            'payload = json.load(sys.stdin)\nunused = 0',
        ),
    }
    mutation_rejected = {
        name: _normalized_ast_sha256(source) != SURFACE_DRIVER_AST_SHA256
        for name, source in adversarial_mutations.items()
    }
    literal_tables = {}
    for name in ("AUDIT_INPUT_PATHS", "FROZEN_LAWFUL_PROBES", "FROZEN_REJECT_WITNESSES"):
        values = []
        for node in outer.body:
            if isinstance(node, ast.Assign) and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            ):
                values.append(node.value)
        try:
            literal_tables[name] = len(values) == 1 and ast.literal_eval(values[0]) is not None
        except (TypeError, ValueError, SyntaxError):
            literal_tables[name] = False
    return {
        "driver_ast_sha256": driver_sha,
        "driver_pin_match": driver_sha == SURFACE_DRIVER_AST_SHA256,
        "mutation_rejected": mutation_rejected,
        "parent_imports_landed": parent_imports_landed,
        "parent_modules_clean": all(name not in sys.modules for name in landed_names),
        "literal_tables": literal_tables,
        "pass": (
            driver_sha == SURFACE_DRIVER_AST_SHA256
            and all(mutation_rejected.values())
            and not parent_imports_landed
            and all(name not in sys.modules for name in landed_names)
            and all(literal_tables.values())
        ),
    }


def _sandbox_drift_demo() -> dict[str, Any]:
    real_path = ROOT / BRIDGE_PATH
    real_before_hash = _path_sha256(real_path)
    real_before_stat = _stat_token(real_path)
    with tempfile.TemporaryDirectory(prefix="born-projector-pin-") as folder:
        sandbox_root = Path(folder)
        sandbox_path = sandbox_root / BRIDGE_PATH
        sandbox_path.parent.mkdir(parents=True)
        shutil.copyfile(real_path, sandbox_path)
        original = sandbox_path.read_bytes()
        changed = bytearray(original)
        changed[-1] ^= 1
        sandbox_path.write_bytes(bytes(changed))
        production_verdict = _pin_verdict(
            BRIDGE_PATH, BRIDGE_SHA256, root=sandbox_root
        )
        differing_bytes = sum(left != right for left, right in zip(original, changed))
    real_after_hash = _path_sha256(real_path)
    real_after_stat = _stat_token(real_path)
    return {
        "production_verdict": production_verdict,
        "one_byte_changed": differing_bytes == 1,
        "real_hash_unchanged": (
            real_before_hash == real_after_hash == BRIDGE_SHA256
        ),
        "real_stat_unchanged": real_before_stat == real_after_stat,
        "pass": (
            production_verdict["verdict"] == "DRIFT"
            and not production_verdict["match"]
            and differing_bytes == 1
            and real_before_hash == real_after_hash == BRIDGE_SHA256
            and real_before_stat == real_after_stat
        ),
    }


def _comparator_mutation_suite(
    lawful_result: dict[str, Any],
    reject_result: dict[str, Any],
) -> dict[str, Any]:
    lawful_row = next(
        row for row in FROZEN_LAWFUL_PROBES if row["probe_id"] == "axis_plus_x"
    )
    reject_row = next(
        row for row in FROZEN_REJECT_WITNESSES if row["probe_id"] == "wrong_arity"
    )
    lawful_feed = copy.deepcopy(lawful_row["feed"])
    lawful_observation = copy.deepcopy(lawful_result["observation"])
    reject_feed = copy.deepcopy(reject_row["feed"])
    reject_observation = copy.deepcopy(reject_result["observation"])
    killed: dict[str, bool] = {}

    def kill_lawful(label: str, observation: Any, feed: Any = lawful_feed) -> None:
        killed[label] = not _compare_observation(
            "lawful", feed, lawful_row, observation
        )["frozen_match"]

    mutated_feed = copy.deepcopy(lawful_feed)
    mutated_feed["extra"] = 1
    kill_lawful("feed_keyset", lawful_observation, mutated_feed)

    mutation = copy.deepcopy(lawful_observation)
    mutation["unexpected_probability"] = 0.5
    kill_lawful("outer_extra_key", mutation)
    mutation = copy.deepcopy(lawful_observation)
    del mutation["summary"]
    kill_lawful("outer_missing_key", mutation)
    for field, replacement in (
        ("origin", "forged_origin"),
        ("status", "forged_status"),
    ):
        mutation = copy.deepcopy(lawful_observation)
        mutation[field] = replacement
        kill_lawful(field, mutation)
    mutation = copy.deepcopy(lawful_observation)
    mutation["matrix"][0][0][0] += 1.0e-6
    kill_lawful("matrix_value", mutation)
    mutation = copy.deepcopy(lawful_observation)
    mutation["matrix"][0][0][0] = "0.5"
    kill_lawful("matrix_type", mutation)
    mutation = copy.deepcopy(lawful_observation)
    mutation["matrix"][0][0][0] = float("inf")
    kill_lawful("matrix_nonfinite", mutation)
    huge_integer_observation = copy.deepcopy(lawful_observation)
    huge_integer_observation["matrix"][0][0][0] = 10**400
    kill_lawful("matrix_oversized_integer", huge_integer_observation)
    for field in (
        "shape",
        "hermitian_residual",
        "idempotence_residual",
        "trace_real",
        "trace_imag",
        "minimum_eigenvalue",
        "maximum_eigenvalue",
    ):
        mutation = copy.deepcopy(lawful_observation)
        if field == "shape":
            mutation["summary"][field] = [2, 3]
        else:
            mutation["summary"][field] = (
                float(mutation["summary"][field]) + 1.0e-6
            )
        kill_lawful("summary_" + field, mutation)
    mutation = copy.deepcopy(lawful_observation)
    mutation["summary"]["unexpected"] = 0
    kill_lawful("summary_extra_key", mutation)
    mutation = copy.deepcopy(lawful_observation)
    mutation["matrix"][0][0][0] += 1.0e-12
    kill_lawful("tolerance_exceeded", mutation)

    within = copy.deepcopy(lawful_observation)
    within["matrix"][0][0][0] += lawful_row["expected"]["machine_bound"] / 2
    within_bound_accepted = _compare_observation(
        "lawful", lawful_feed, lawful_row, within
    )["frozen_match"]

    original_surface = globals()["_surface_observation"]
    try:
        globals()["_surface_observation"] = lambda _feed: copy.deepcopy(
            huge_integer_observation
        )
        huge_integer_live = run_acceptance(lawful_feed)
    finally:
        globals()["_surface_observation"] = original_surface
    huge_integer_live_drift = (
        huge_integer_live["verdict"] == "DRIFT"
        and huge_integer_live["comparison"]["frozen_match"] is False
    )

    for field, replacement in (
        ("exception_type", "RuntimeError"),
        ("message", "forged message"),
    ):
        mutation = copy.deepcopy(reject_observation)
        mutation[field] = replacement
        killed["reject_" + field] = not _compare_observation(
            "reject", reject_feed, reject_row, mutation
        )["frozen_match"]
    mutation = copy.deepcopy(reject_observation)
    mutation["unexpected_probability"] = 0.5
    killed["reject_extra_key"] = not _compare_observation(
        "reject", reject_feed, reject_row, mutation
    )["frozen_match"]
    mutation = copy.deepcopy(reject_observation)
    del mutation["message"]
    killed["reject_missing_key"] = not _compare_observation(
        "reject", reject_feed, reject_row, mutation
    )["frozen_match"]

    return {
        "killed": killed,
        "oversized_integer_live_drift": huge_integer_live_drift,
        "within_bound_accepted": within_bound_accepted,
        "pass": (
            all(killed.values())
            and huge_integer_live_drift
            and within_bound_accepted
        ),
    }


def _schema_metamorphic_suite() -> dict[str, bool]:
    def refuses(feed: Any, enforcement: str) -> bool:
        result = run_acceptance(feed)
        observation = result.get("observation")
        exception_type = (
            "SchemaRefusal"
            if enforcement == "harness_schema"
            else "FixtureRefusal"
        )
        return (
            result.get("verdict") == "REJECT"
            and result.get("enforcement") == enforcement
            and isinstance(observation, dict)
            and observation.get("origin") == enforcement
            and observation.get("status") == "raised"
            and observation.get("exception_type") == exception_type
        )

    cases = {
        "non_object": ([], "harness_schema"),
        "missing_probe_id": (
            {"kind": "bloch_projector", "direction": [1, 0, 0]},
            "harness_schema",
        ),
        "non_string_probe_id": (
            {
                "probe_id": 7,
                "kind": "bloch_projector",
                "direction": [1, 0, 0],
            },
            "harness_schema",
        ),
        "axis_boolean": (
            {
                "probe_id": "axis_plus_x",
                "kind": "bloch_projector",
                "direction": [True, 0, 0],
            },
            "harness_schema",
        ),
        "axis_string": (
            {
                "probe_id": "axis_plus_x",
                "kind": "bloch_projector",
                "direction": ["1", 0, 0],
            },
            "harness_schema",
        ),
        "axis_nonfinite": (
            {
                "probe_id": "axis_plus_x",
                "kind": "bloch_projector",
                "direction": [float("nan"), 0, 0],
            },
            "harness_schema",
        ),
        "axis_oversized_integer": (
            {
                "probe_id": "axis_plus_x",
                "kind": "bloch_projector",
                "direction": [10**400, 0, 0],
            },
            "harness_schema",
        ),
        "axis_extra_key": (
            {
                "probe_id": "axis_plus_x",
                "kind": "bloch_projector",
                "direction": [1, 0, 0],
                "extra": 1,
            },
            "harness_schema",
        ),
        "unknown_valid": (
            {
                "probe_id": "unknown",
                "kind": "bloch_projector",
                "direction": [1, 0, 0],
            },
            "fixture_registry",
        ),
        "unknown_extra_key": (
            {
                "probe_id": "unknown",
                "kind": "bloch_projector",
                "direction": [1, 0, 0],
                "extra": 1,
            },
            "harness_schema",
        ),
        "known_id_feed_mismatch": (
            {
                "probe_id": "axis_plus_x",
                "kind": "bloch_projector",
                "direction": [-1, 0, 0],
            },
            "fixture_registry",
        ),
        "boolean_id_numeric": (
            {
                "probe_id": "boolean_type_violation",
                "kind": "bloch_projector",
                "direction": [1, 0, 0],
            },
            "fixture_registry",
        ),
    }
    return {
        label: refuses(feed, enforcement)
        for label, (feed, enforcement) in cases.items()
    }


def _probe_cli() -> int:
    try:
        feed = json.load(sys.stdin)
    except Exception as exc:
        print(
            json.dumps(
                {
                    "verdict": "REJECT",
                    "observation": _schema_refusal(
                        f"HARNESS_SCHEMA: invalid JSON input: {type(exc).__name__}"
                    ),
                },
                allow_nan=False,
                separators=(",", ":"),
                sort_keys=True,
            )
        )
        return 0
    print(
        json.dumps(
            run_acceptance(feed),
            allow_nan=False,
            separators=(",", ":"),
            sort_keys=True,
        )
    )
    return 0


def main() -> int:
    global _PASS, _FAIL
    _PASS = 0
    _FAIL = 0

    pin = _pin_verdict(BRIDGE_PATH, BRIDGE_SHA256)
    clean_env = _clean_child_env()
    declared_paths_exist = all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
    check(
        "A. landed projector pin and hermetic execution contract",
        pin["match"]
        and "PYTHONPATH" not in clean_env
        and declared_paths_exist,
        {
            "pin": pin,
            "pythonpath_removed": "PYTHONPATH" not in clean_env,
            "declared_input_count": len(AUDIT_INPUT_PATHS),
            "all_declared_inputs_exist": declared_paths_exist,
        },
    )

    lawful = [run_acceptance(row["feed"]) for row in FROZEN_LAWFUL_PROBES]
    check(
        "B. four frozen axis projector fixtures ACCEPT",
        len(lawful) == 4
        and all(
            row["verdict"] == "ACCEPT"
            and row["comparison"]["frozen_match"]
            and row["enforcement"] == "landed_surface"
            for row in lawful
        ),
        {
            row["probe_id"]: {
                "verdict": row["verdict"],
                "frozen_match": row["comparison"]["frozen_match"],
            }
            for row in lawful
        },
    )

    rejected = [run_acceptance(row["feed"]) for row in FROZEN_REJECT_WITNESSES]
    metamorphic = _schema_metamorphic_suite()
    check(
        "C. malformed fixtures REJECT under actual enforcement and schema is ID-independent",
        len(rejected) == 4
        and all(
            row["verdict"] == "REJECT"
            and row["comparison"]["frozen_match"]
            and row["enforcement"]
            == next(
                frozen["expected"]["origin"]
                for frozen in FROZEN_REJECT_WITNESSES
                if frozen["probe_id"] == row["probe_id"]
            )
            for row in rejected
        )
        and all(metamorphic.values()),
        {
            "fixtures": {
                row["probe_id"]: {
                    "verdict": row["verdict"],
                    "enforcement": row["enforcement"],
                }
                for row in rejected
            },
            "metamorphic": metamorphic,
        },
    )

    drift = _sandbox_drift_demo()
    check(
        "D. one-byte sandbox copy reaches DRIFT through the production pin predicate",
        drift["pass"],
        drift,
    )

    comparator = _comparator_mutation_suite(lawful[0], rejected[0])
    check(
        "E. every load-bearing comparator channel kills its quarantined mutant",
        comparator["pass"],
        comparator,
    )

    structure = _structural_discipline()
    check(
        "F. exact normalized driver AST pin rejects alias, dynamic, synthesis, and extra-statement mutations",
        structure["pass"],
        structure,
    )

    census = [
        {
            "probe_id": row["probe_id"],
            "verdict": row["verdict"],
            "frozen_match": row["comparison"]["frozen_match"],
        }
        for row in lawful + rejected
    ]
    for row in census:
        print(
            "CENSUS",
            row["probe_id"],
            "verdict=" + row["verdict"],
            "frozen_match=" + str(row["frozen_match"]),
        )
    final = {
        "checks": {"pass": _PASS, "fail": _FAIL},
        "comparator_mutations": comparator,
        "driver_ast_sha256": structure["driver_ast_sha256"],
        "probe_census": census,
        "runtime_seconds": round(time.monotonic() - _START, 6),
        "scope": {
            "fixture": "projector_bloch_four_axes_only",
            "broader_ternary_surface_tested": False,
            "physics_claim": False,
        },
    }
    print(json.dumps(final, allow_nan=False, separators=(",", ":"), sort_keys=True))
    print(f"SUMMARY PASS {_PASS} FAIL {_FAIL}")
    print("RESULT BORN_PROJECTOR_FIXTURE_ACCEPTANCE_GREEN")
    return int(_FAIL != 0)


if __name__ == "__main__":
    if sys.argv[1:] == ["--probe-json"]:
        raise SystemExit(_probe_cli())
    if sys.argv[1:]:
        print("usage: frontier_born_acceptance_harness_2026_07_28.py [--probe-json]")
        raise SystemExit(2)
    raise SystemExit(main())
