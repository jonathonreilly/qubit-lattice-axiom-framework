#!/usr/bin/env python3
"""Independent, source-data-only check of the bounded Cycle-729 feed."""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/BORN_SURFACE_FEED_CYCLE729_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "scripts/frontier_cycle722_epoch_fed_endpoint_interval_harness_2026_07_28.py",
)
AUDIT_BLOCKLIST = (
    "frontier_cycle729_born_surface_feed_2026_07_28",
)

import ast
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import inspect
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from time import perf_counter
from typing import Any

import numpy as np

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317
import frontier_cycle722_epoch_fed_endpoint_interval_harness_2026_07_28 as F722


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_DATA_PATH = (
    "scripts/frontier_cycle729_born_surface_feed_2026_07_28.py"
)

EXPECTED_AUDIT_INPUT_PATHS = AUDIT_INPUT_PATHS
EXPECTED_BLOCH_RAW = (48.0, 48.0, 48.0)
EXPECTED_BLOCH_VECTOR = (
    0.5773502691896257,
    0.5773502691896257,
    0.5773502691896257,
)
EXPECTED_COMBINED_STAGE_COUNTS = (200, 164, 180, 144)
EXPECTED_STAGE_TOTAL = 688
EXPECTED_MERGE_FRACTIONS = (
    0.29069767441860467,
    0.23837209302325582,
    0.2616279069767442,
    0.20930232558139536,
)
EXPECTED_PRIMARY_METRICS = {
    "projector": {
        "normalization": 2.220446049250313e-16,
        "minimum_eigenvalue": -8.663816624429912e-18,
        "maximum_eigenvalue": 1.0,
    },
    "merge": {
        "normalization": 3.1463121132764933e-16,
        "minimum_eigenvalue": 0.0,
        "maximum_eigenvalue": 0.5970449817737548,
    },
}
EXPECTED_BINDING_SCHEMA = (
    (
        "2x2x2 epoch legs",
        "len(VARIANTS)",
        "L=3 two-ray logical columns",
        "fixture3.two_ray_encoding.shape[1]",
    ),
    (
        "event rows per leg",
        "min((int(census_summaries[variant]['event_rows']) for variant in VARIANTS))",
        "proper-cubic frame count",
        "frame_count",
    ),
    (
        "distinct tick identities per leg",
        "min((int(census_summaries[variant]['distinct_identities']) for variant in VARIANTS))",
        "proper-cubic frame count",
        "frame_count",
    ),
    (
        "combined event rows",
        "total_event_rows",
        "proper frames x two-ray columns",
        "frame_count * fixture3.two_ray_encoding.shape[1]",
    ),
    (
        "multiplicity of every tick identity",
        "min(identity_multiplicities.values())",
        "pinned fixture lengths L=3,L=6",
        "len((fixture3, fixture6))",
    ),
    (
        "ordered Bloch projection fields",
        "len(BLOCH_FIELD_ORDER)",
        "pointer M2",
        "B317.POINTER_M2",
    ),
    (
        "base-stage coefficient bins",
        "len(BASE_STAGE_ORDER)",
        "maximum merge components",
        "4",
    ),
)
EXPECTED_PROJECTOR_CONVENTION = {
    "census_scalars": (
        "combined one-count in each named Cycle-722 event-table field "
        "over primary then alternate_port"
    ),
    "frame": "Cycle-317 Bloch (x,y,z) order",
    "sign": "positive retained-bit one-counts; no sign flips",
    "normalization": "divide by Euclidean L2 norm exactly once",
    "fitted_parameters": 0,
}
EXPECTED_MERGE_CONVENTION = {
    "projection": (
        "count destination handoffs in the base epoch stages for both "
        "2x2x2 legs, aggregate in declared A,B,C,D order, divide each "
        "integer by their total"
    ),
    "fitted_parameters": 0,
}


def _require(condition: object, message: str) -> None:
    if not bool(condition):
        raise AssertionError(message)


def _json_default(value: object) -> object:
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, Path):
        return str(value)
    raise TypeError(type(value).__name__)


def _table_sha256(table: list[dict[str, object]]) -> str:
    payload = json.dumps(
        table,
        default=_json_default,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    return sha256(payload).hexdigest()


def _assignments(tree: ast.AST) -> dict[str, list[ast.AST]]:
    found: dict[str, list[ast.AST]] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            targets = node.targets
            value = node.value
        elif isinstance(node, ast.AnnAssign):
            targets = (node.target,)
            value = node.value
        else:
            continue
        if value is None:
            continue
        for target in targets:
            if isinstance(target, ast.Name):
                found.setdefault(target.id, []).append(value)
    return found


def _one_assignment(
    assignments: dict[str, list[ast.AST]], name: str
) -> ast.AST:
    nodes = assignments.get(name, [])
    _require(len(nodes) == 1, f"expected one assignment for {name}")
    return nodes[0]


def _literal_assignment(
    assignments: dict[str, list[ast.AST]], name: str
) -> Any:
    return ast.literal_eval(_one_assignment(assignments, name))


def _dict_nodes(node: ast.AST) -> dict[str, ast.AST]:
    _require(isinstance(node, ast.Dict), "expected a dictionary expression")
    result: dict[str, ast.AST] = {}
    for key_node, value_node in zip(node.keys, node.values):
        _require(key_node is not None, "dictionary unpacking is not literal data")
        key = ast.literal_eval(key_node)
        _require(isinstance(key, str), "expected string dictionary key")
        _require(key not in result, f"duplicate dictionary key {key}")
        result[key] = value_node
    return result


def _literal_fields(
    nodes: dict[str, ast.AST], fields: tuple[str, ...]
) -> dict[str, Any]:
    return {field: ast.literal_eval(nodes[field]) for field in fields}


def _same_expression(node: ast.AST, expression: str) -> bool:
    expected = ast.parse(expression, mode="eval").body
    return ast.dump(node, include_attributes=False) == ast.dump(
        expected, include_attributes=False
    )


def _binding_schema(node: ast.AST) -> tuple[tuple[str, str, str, str], ...]:
    _require(isinstance(node, ast.List), "binding_table must be a list")
    rows: list[tuple[str, str, str, str]] = []
    for row_node in node.elts:
        fields = _dict_nodes(row_node)
        _require(
            set(fields)
            == {
                "census_quantity",
                "census_integer",
                "pinned_fixture_quantity",
                "fixture_integer",
            },
            "binding row schema changed",
        )
        rows.append(
            (
                ast.literal_eval(fields["census_quantity"]),
                ast.unparse(fields["census_integer"]),
                ast.literal_eval(fields["pinned_fixture_quantity"]),
                ast.unparse(fields["fixture_integer"]),
            )
        )
    return tuple(rows)


def extraction() -> dict[str, object]:
    primary_path = ROOT / PRIMARY_DATA_PATH
    source_bytes = primary_path.read_bytes()
    tree = ast.parse(source_bytes, filename=str(primary_path))
    assignments = _assignments(tree)

    audit_paths = _literal_assignment(assignments, "AUDIT_INPUT_PATHS")
    b317_pin = _literal_assignment(assignments, "EXPECTED_B317_SHA256")
    variants = _literal_assignment(assignments, "VARIANTS")
    event_fields = _literal_assignment(assignments, "EVENT_FIELDS")
    bloch_field_order = _literal_assignment(assignments, "BLOCH_FIELD_ORDER")
    stage_order = _literal_assignment(assignments, "BASE_STAGE_ORDER")
    splits = _literal_assignment(assignments, "CYCLE317_LITERAL_SPLITS")
    merge_directions = _literal_assignment(
        assignments, "CYCLE317_LITERAL_MERGE_DIRECTIONS"
    )
    forbidden_tokens = _literal_assignment(
        assignments, "FORBIDDEN_CENSUS_RECEIVER_TOKENS"
    )
    frozen = {
        name: _literal_assignment(assignments, name)
        for name in (
            "FROZEN_TABLE_SHA256",
            "FROZEN_BASE_STAGE_HANDOFF_COUNTS",
            "FROZEN_COMBINED_BASE_STAGE_HANDOFF_COUNTS",
            "FROZEN_PORT_INVENTORY",
        )
    }

    projector_feed = _dict_nodes(
        _one_assignment(assignments, "projector_feed")
    )
    projector_convention_nodes = _dict_nodes(projector_feed["convention"])
    projector_convention = _literal_fields(
        projector_convention_nodes,
        (
            "census_scalars",
            "frame",
            "sign",
            "normalization",
            "fitted_parameters",
        ),
    )
    _require(
        _same_expression(
            projector_convention_nodes["field_order"],
            "list(BLOCH_FIELD_ORDER)",
        ),
        "projector field-order binding changed",
    )
    _require(
        _same_expression(
            projector_convention_nodes["raw_counts"],
            "bloch_raw.tolist()",
        ),
        "projector raw-count binding changed",
    )
    _require(
        _same_expression(
            projector_convention_nodes["unit_vector"],
            "bloch_direction.tolist()",
        ),
        "projector vector binding changed",
    )

    merge_feed = _dict_nodes(_one_assignment(assignments, "merge_feed"))
    merge_convention_nodes = _dict_nodes(merge_feed["convention"])
    merge_convention = _literal_fields(
        merge_convention_nodes, ("projection", "fitted_parameters")
    )
    dynamic_merge_bindings = {
        "stage_order": "list(BASE_STAGE_ORDER)",
        "per_variant_counts": (
            "{variant: census_summaries[variant]"
            "['base_stage_destination_handoffs'] for variant in VARIANTS}"
        ),
        "combined_counts": "list(combined_stage_counts)",
        "normalization_total": "stage_total",
        "fraction_tuple": "list(merge_fractions)",
    }
    for field, expression in dynamic_merge_bindings.items():
        _require(
            _same_expression(merge_convention_nodes[field], expression),
            f"merge convention binding changed for {field}",
        )

    no_receiver_nodes = _dict_nodes(
        _one_assignment(assignments, "no_census_weight_receiver")
    )
    no_receiver_literals = _literal_fields(
        no_receiver_nodes,
        ("nonlinear_binary_weight_boundary", "merge_weight_boundary"),
    )
    no_receiver_dynamic = {
        "frozen_port_count": "len(FROZEN_PORT_INVENTORY)",
        "inventory": (
            "{name: list(parameters) for name, parameters "
            "in observed_inventory.items()}"
        ),
        "inventory_matches_extract": (
            "observed_inventory == FROZEN_PORT_INVENTORY"
        ),
        "forbidden_receiver_tokens": (
            "list(FORBIDDEN_CENSUS_RECEIVER_TOKENS)"
        ),
        "receivers_found": "forbidden_receivers",
    }
    for field, expression in no_receiver_dynamic.items():
        _require(
            _same_expression(no_receiver_nodes[field], expression),
            f"no-receiver finding binding changed for {field}",
        )
    weights_finding = ast.literal_eval(
        _one_assignment(assignments, "weights_remain_supplied")
    )
    bindings = _binding_schema(_one_assignment(assignments, "binding_table"))

    observed_b317_sha = sha256(
        (ROOT / AUDIT_INPUT_PATHS[0]).read_bytes()
    ).hexdigest()
    _require(audit_paths == EXPECTED_AUDIT_INPUT_PATHS, "AUDIT tuple changed")
    _require(
        isinstance(audit_paths, tuple)
        and all(isinstance(path, str) for path in audit_paths),
        "AUDIT tuple did not literal-eval to strings",
    )
    _require(
        observed_b317_sha == b317_pin,
        "B317 bytes do not match the primary pin",
    )
    _require(
        Path(B317.__file__).resolve()
        == (ROOT / AUDIT_INPUT_PATHS[0]).resolve(),
        "B317 import did not resolve to the declared input",
    )
    _require(
        Path(F722.__file__).resolve()
        == (ROOT / AUDIT_INPUT_PATHS[1]).resolve(),
        "F722 import did not resolve to the declared input",
    )
    _require(
        projector_convention == EXPECTED_PROJECTOR_CONVENTION,
        "projector convention literal changed",
    )
    _require(
        merge_convention == EXPECTED_MERGE_CONVENTION,
        "merge convention literal changed",
    )
    _require(bindings == EXPECTED_BINDING_SCHEMA, "binding table changed")
    _require(
        tuple(frozen["FROZEN_PORT_INVENTORY"]) and len(
            frozen["FROZEN_PORT_INVENTORY"]
        )
        == 20,
        "frozen port inventory is not the declared 20 signatures",
    )
    _require(
        weights_finding.get("value") is True
        and len(weights_finding.get("required_absent_bridge", ())) == 4,
        "weights-remain-supplied finding changed",
    )

    return {
        "pass": True,
        "tree": tree,
        "assignments": assignments,
        "audit_paths": audit_paths,
        "b317_pin": b317_pin,
        "b317_sha": observed_b317_sha,
        "variants": variants,
        "event_fields": event_fields,
        "bloch_field_order": bloch_field_order,
        "stage_order": stage_order,
        "splits": splits,
        "merge_directions": merge_directions,
        "forbidden_tokens": forbidden_tokens,
        "frozen": frozen,
        "projector_convention": projector_convention,
        "merge_convention": merge_convention,
        "no_receiver_literals": no_receiver_literals,
        "weights_finding": weights_finding,
        "binding_schema": bindings,
        "literal_source_data": True,
        "brief": f"B317 sha256={observed_b317_sha[:16]}…; AST literals bound",
    }


def census_recomputation(extracted: dict[str, object]) -> dict[str, object]:
    variants = tuple(extracted["variants"])
    event_fields = tuple(extracted["event_fields"])
    stage_order = tuple(extracted["stage_order"])
    frozen = extracted["frozen"]

    atlas = F722.EPOCH.P.build_private_atlases()
    primary = F722.EPOCH.build_epoch((2, 2, 2), "primary", atlas)
    alternate = F722.EPOCH.build_epoch(
        (2, 2, 2),
        "alternate_port",
        atlas,
        recurrent_override=primary.recurrent,
    )
    bundles = {"primary": primary, "alternate_port": alternate}
    extensions: dict[str, dict[str, object]] = {}
    summaries: dict[str, dict[str, object]] = {}
    for variant in variants:
        extension = F722.extend_and_walk(bundles[variant])
        extensions[variant] = extension
        table = extension["table"]
        word_stage = {
            word.word_id: slot.stage
            for slot in extension["slots"]
            for word in slot.words
        }
        destination_counts = Counter(
            word_stage[edge[1]] for edge in extension["handoffs"]
        )
        identities = tuple(int(row["tick_identity"]) for row in table)
        summaries[variant] = {
            "event_rows": len(table),
            "distinct_identities": len(set(identities)),
            "identity_minimum": min(identities),
            "identity_maximum": max(identities),
            "event_table_sha256": _table_sha256(table),
            "field_one_counts": {
                field: sum(int(row[field]) for row in table)
                for field in event_fields
            },
            "source_count": len(extension["sources"]),
            "sources_clean": bool(extension["sources_clean"]),
            "E_handoffs": len(extension["e_handoffs"]),
            "base_stage_destination_handoffs": {
                stage: int(destination_counts[stage])
                for stage in stage_order
            },
            "collision_count": int(extension["walk"]["collision_count"]),
            "violation_count": int(extension["walk"]["violation_count"]),
            "lawful": bool(extension["lawful"]),
        }

    for variant in variants:
        summary = summaries[variant]
        _require(summary["event_rows"] == 24, f"{variant} row census")
        _require(
            summary["distinct_identities"] == 24
            and summary["identity_minimum"] == 0
            and summary["identity_maximum"] == 23,
            f"{variant} identity census",
        )
        _require(
            summary["event_table_sha256"]
            == frozen["FROZEN_TABLE_SHA256"][variant],
            f"{variant} table digest",
        )
        _require(
            summary["field_one_counts"]
            == {field: 24 for field in event_fields},
            f"{variant} event-field census",
        )
        _require(
            summary["source_count"] == 5
            and summary["sources_clean"]
            and summary["E_handoffs"] == 120,
            f"{variant} source/handoff census",
        )
        _require(
            summary["base_stage_destination_handoffs"]
            == frozen["FROZEN_BASE_STAGE_HANDOFF_COUNTS"][variant],
            f"{variant} base-stage census",
        )
        _require(
            summary["collision_count"] == 0
            and summary["violation_count"] == 0
            and summary["lawful"],
            f"{variant} lawful census",
        )

    field_order = tuple(extracted["bloch_field_order"])
    combined_field_counts = {
        field: sum(
            int(summaries[variant]["field_one_counts"][field])
            for variant in variants
        )
        for field in event_fields
    }
    bloch_raw = np.asarray(
        tuple(combined_field_counts[field] for field in field_order),
        dtype=float,
    )
    bloch_direction = bloch_raw / np.linalg.norm(bloch_raw)
    combined_stage_counts = tuple(
        sum(
            int(
                summaries[variant]["base_stage_destination_handoffs"][
                    stage
                ]
            )
            for variant in variants
        )
        for stage in stage_order
    )
    stage_total = sum(combined_stage_counts)
    rational_fractions = tuple(
        Fraction(count, stage_total) for count in combined_stage_counts
    )
    merge_fractions = tuple(float(value) for value in rational_fractions)

    _require(tuple(bloch_raw) == EXPECTED_BLOCH_RAW, "Bloch raw census")
    _require(
        tuple(bloch_direction) == EXPECTED_BLOCH_VECTOR,
        "L2-normalized Bloch vector changed",
    )
    _require(
        combined_stage_counts == EXPECTED_COMBINED_STAGE_COUNTS
        and combined_stage_counts
        == tuple(frozen["FROZEN_COMBINED_BASE_STAGE_HANDOFF_COUNTS"]),
        "combined base-stage counts changed",
    )
    _require(stage_total == EXPECTED_STAGE_TOTAL, "stage total changed")
    _require(
        rational_fractions
        == tuple(
            Fraction(count, EXPECTED_STAGE_TOTAL)
            for count in EXPECTED_COMBINED_STAGE_COUNTS
        ),
        "merge fractions fail exact rational reproduction",
    )
    _require(
        merge_fractions == EXPECTED_MERGE_FRACTIONS,
        "merge float fractions changed",
    )
    _require(
        extracted["projector_convention"]["fitted_parameters"] == 0
        and extracted["merge_convention"]["fitted_parameters"] == 0,
        "a fitted parameter entered a projection convention",
    )

    return {
        "pass": True,
        "summaries": summaries,
        "extensions": extensions,
        "bloch_raw": tuple(float(value) for value in bloch_raw),
        "bloch_direction": tuple(float(value) for value in bloch_direction),
        "combined_stage_counts": combined_stage_counts,
        "stage_total": stage_total,
        "rational_fractions": rational_fractions,
        "merge_fractions": merge_fractions,
        "brief": (
            f"raw={tuple(bloch_raw)}; counts={combined_stage_counts}/"
            f"{stage_total}"
        ),
    }


def _menu_metrics(effects: tuple[np.ndarray, ...]) -> dict[str, float]:
    eigenvalues = np.concatenate(
        tuple(
            np.linalg.eigvalsh((effect + effect.conj().T) / 2)
            for effect in effects
        )
    )
    return {
        "normalization": float(
            np.linalg.norm(
                sum(effects, start=np.zeros((2, 2), dtype=complex))
                - np.eye(2, dtype=complex)
            )
        ),
        "minimum_eigenvalue": float(np.min(eigenvalues)),
        "maximum_eigenvalue": float(np.max(eigenvalues)),
    }


def _metric_delta(
    observed: dict[str, float], expected: dict[str, float]
) -> float:
    return max(abs(observed[key] - expected[key]) for key in expected)


def feed_replay(
    extracted: dict[str, object], census: dict[str, object]
) -> dict[str, object]:
    direction = np.asarray(census["bloch_direction"], dtype=float)
    fractions = tuple(float(value) for value in census["merge_fractions"])
    fixture3 = B317.physical_fixture(3)
    fixture6 = B317.physical_fixture(6)

    projector = B317.projector_bloch(direction)
    split_isometry, split_groups = B317.split_projector_isometry(
        projector,
        tuple(extracted["splits"]),
        fixture3.contact,
    )
    split_effects = B317.derived_effects(split_isometry, split_groups)
    split_metrics = _menu_metrics(split_effects)

    literal_projectors = tuple(
        B317.projector_bloch(
            np.asarray(row, dtype=float)
            / np.linalg.norm(np.asarray(row, dtype=float))
        )
        for row in extracted["merge_directions"]
    )
    merge_isometry, merge_groups = B317.merge_isometry(
        tuple(zip(fractions, literal_projectors)),
        fixture3.contact,
    )
    merge_effects = B317.derived_effects(merge_isometry, merge_groups)
    merge_metrics = _menu_metrics(merge_effects)

    split_residual = float(
        np.linalg.norm(
            split_isometry.conj().T @ split_isometry
            - np.eye(2, dtype=complex)
        )
    )
    merge_residual = float(
        np.linalg.norm(
            merge_isometry.conj().T @ merge_isometry
            - np.eye(2, dtype=complex)
        )
    )
    split_delta = _metric_delta(
        split_metrics, EXPECTED_PRIMARY_METRICS["projector"]
    )
    merge_delta = _metric_delta(
        merge_metrics, EXPECTED_PRIMARY_METRICS["merge"]
    )
    machine_tolerance = 8 * np.finfo(float).eps

    for label, metrics in (
        ("projector", split_metrics),
        ("merge", merge_metrics),
    ):
        _require(
            metrics["normalization"] < B317.TOL
            and metrics["minimum_eigenvalue"] > -B317.TOL
            and metrics["maximum_eigenvalue"] < 1 + B317.TOL,
            f"{label} menu rejected by the lawful metric domain",
        )
    _require(np.linalg.norm(direction) == 1.0, "Bloch input is not unit")
    _require(
        len(fractions) == 4
        and all(value >= 0 for value in fractions)
        and abs(sum(fractions) - 1) < 1e-15,
        "merge input is outside its lawful domain",
    )
    _require(
        split_isometry.shape == (16, 2)
        and len(split_effects) == 4
        and split_residual < B317.TOL,
        "projector feed dilation changed",
    )
    _require(
        merge_isometry.shape == (16, 2)
        and len(merge_effects) == 5
        and merge_residual < B317.TOL,
        "merge feed dilation changed",
    )
    _require(
        split_delta <= machine_tolerance
        and merge_delta <= machine_tolerance,
        "primary metric reproduction exceeds machine agreement",
    )

    frame_count = len(B317.c311.c235.proper_cubic_frames())
    variants = tuple(extracted["variants"])
    summaries = census["summaries"]
    identity_multiplicities = Counter(
        int(row["tick_identity"])
        for variant in variants
        for row in census["extensions"][variant]["table"]
    )
    census_integers = (
        len(variants),
        min(int(summaries[v]["event_rows"]) for v in variants),
        min(int(summaries[v]["distinct_identities"]) for v in variants),
        sum(int(summaries[v]["event_rows"]) for v in variants),
        min(identity_multiplicities.values()),
        len(tuple(extracted["bloch_field_order"])),
        len(tuple(extracted["stage_order"])),
    )
    fixture_integers = (
        fixture3.two_ray_encoding.shape[1],
        frame_count,
        frame_count,
        frame_count * fixture3.two_ray_encoding.shape[1],
        len((fixture3, fixture6)),
        B317.POINTER_M2,
        4,
    )
    _require(
        census_integers == fixture_integers
        and census_integers == (2, 24, 24, 48, 2, 3, 4),
        "integer binding table did not independently recompute",
    )
    _require(
        len(identity_multiplicities) == 24
        and max(identity_multiplicities.values()) == 2,
        "identity multiplicity binding changed",
    )

    return {
        "pass": True,
        "split_metrics": split_metrics,
        "merge_metrics": merge_metrics,
        "split_residual": split_residual,
        "merge_residual": merge_residual,
        "split_delta": split_delta,
        "merge_delta": merge_delta,
        "metric_agreement": max(split_delta, merge_delta),
        "binding_integers": census_integers,
        "brief": (
            f"metric_delta={max(split_delta, merge_delta):.3e}; "
            f"bindings={census_integers}"
        ),
    }


def anchor_replay() -> dict[str, object]:
    environment = dict(os.environ)
    environment["PYTHONPATH"] = "scripts"
    completed = subprocess.run(
        [sys.executable, str(ROOT / AUDIT_INPUT_PATHS[0])],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    stdout = completed.stdout.decode("utf-8", errors="replace")
    stderr = completed.stderr.decode("utf-8", errors="replace")
    summaries = re.findall(
        r"^SUMMARY PASS ([0-9]+) FAIL ([0-9]+)$",
        stdout,
        flags=re.MULTILINE,
    )
    pass_lines = len(re.findall(r"^PASS ", stdout, flags=re.MULTILINE))
    fail_lines = len(re.findall(r"^FAIL ", stdout, flags=re.MULTILINE))
    result_lines = re.findall(r"^RESULT (.+)$", stdout, flags=re.MULTILINE)
    _require(completed.returncode == 0, "B317 main returned nonzero")
    _require(summaries == [("15", "0")], "B317 summary is not frozen 15/0")
    _require(pass_lines == 15 and fail_lines == 0, "B317 line census changed")
    _require(
        result_lines
        == ["CYCLE317_PHYSICAL_CONTACT_TERNARY_BORN_BRIDGE_GREEN"],
        "B317 result marker changed",
    )
    _require(not stderr, "B317 emitted stderr")
    _require(
        len(completed.stdout) < 150_000,
        "captured B317 stdout exceeds the bounded policy",
    )
    return {
        "pass": True,
        "pass_count": pass_lines,
        "fail_count": fail_lines,
        "stdout_bytes": len(completed.stdout),
        "brief": f"frozen={pass_lines}/{pass_lines + fail_lines}; stderr=0",
    }


def port_inventory(extracted: dict[str, object]) -> dict[str, object]:
    frozen = {
        name: tuple(parameters)
        for name, parameters in extracted["frozen"][
            "FROZEN_PORT_INVENTORY"
        ].items()
    }
    live_functions = {
        name: function
        for name, function in inspect.getmembers(B317, inspect.isfunction)
        if function.__module__ == B317.__name__
    }
    live = {
        name: tuple(inspect.signature(function).parameters)
        for name, function in sorted(live_functions.items())
    }
    forbidden = {
        name: tuple(
            parameter
            for parameter in parameters
            if any(
                token in parameter.lower()
                for token in extracted["forbidden_tokens"]
            )
        )
        for name, parameters in live.items()
    }
    forbidden = {
        name: parameters
        for name, parameters in forbidden.items()
        if parameters
    }
    _require(len(live) == 20, "live B317 function count is not 20")
    _require(live == frozen, "live signatures differ from frozen inventory")
    _require(not forbidden, "a census-weight receiver is present")
    return {
        "pass": True,
        "count": len(live),
        "receivers": forbidden,
        "brief": "20/20 signatures exact; census receivers=0",
    }


def _attribute_root(node: ast.AST) -> str | None:
    current = node
    while isinstance(current, (ast.Attribute, ast.Subscript)):
        current = current.value
    return current.id if isinstance(current, ast.Name) else None


def discipline(extracted: dict[str, object]) -> dict[str, object]:
    tree = extracted["tree"]
    writes: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and isinstance(
            node.ctx, (ast.Store, ast.Del)
        ):
            root = _attribute_root(node)
            if root in {"B317", "F722"}:
                writes.append(ast.unparse(node))
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in {"setattr", "delattr"}
            and node.args
            and isinstance(node.args[0], ast.Name)
            and node.args[0].id in {"B317", "F722"}
        ):
            writes.append(ast.unparse(node))
    imported_blocklist = tuple(
        name for name in AUDIT_BLOCKLIST if name in sys.modules
    )
    _require(not writes, "primary writes B317/F722 attributes")
    _require(
        extracted["literal_source_data"],
        "findings/conventions were not extracted as source data",
    )
    _require(
        not imported_blocklist,
        "the blocklisted Cycle-729 primary was imported",
    )
    return {
        "pass": True,
        "attribute_writes": tuple(writes),
        "imported_blocklist": imported_blocklist,
        "brief": "primary attribute writes=0; blocklist clean; literals only",
    }


def _run_certificate(
    name: str,
    call: Any,
    *args: object,
) -> dict[str, object]:
    try:
        result = call(*args)
        _require(result.get("pass") is True, f"{name} returned non-PASS")
    except Exception as error:
        result = {
            "pass": False,
            "brief": f"{type(error).__name__}: {error}",
        }
    print(
        ("PASS" if result["pass"] else "FAIL"),
        name,
        "::",
        result["brief"],
    )
    return result


def main() -> int:
    started = perf_counter()
    results: dict[str, dict[str, object]] = {}
    results["extraction"] = _run_certificate("extraction", extraction)

    extracted = results["extraction"] if results["extraction"]["pass"] else {}
    results["census_recomputation"] = _run_certificate(
        "census_recomputation",
        census_recomputation,
        extracted,
    )
    census = (
        results["census_recomputation"]
        if results["census_recomputation"]["pass"]
        else {}
    )
    results["feed_replay"] = _run_certificate(
        "feed_replay",
        feed_replay,
        extracted,
        census,
    )
    results["anchor_replay"] = _run_certificate(
        "anchor_replay", anchor_replay
    )
    results["port_inventory"] = _run_certificate(
        "port_inventory", port_inventory, extracted
    )
    results["discipline"] = _run_certificate(
        "discipline", discipline, extracted
    )

    passed = sum(int(result["pass"]) for result in results.values())
    total = len(results)
    vector = census.get("bloch_direction", "unavailable")
    fractions = census.get("merge_fractions", "unavailable")
    metric_delta = results["feed_replay"].get(
        "metric_agreement", "unavailable"
    )
    runtime = perf_counter() - started
    print(
        f"SUMMARY {passed}/{total} :: vector={vector}; "
        f"fractions={fractions}"
    )
    print(
        f"METRICS agreement={metric_delta}; runtime={runtime:.3f}s; "
        f"stdout_limit=150000"
    )
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
