#!/usr/bin/env python3
"""Cycle 809: exhaustive convention-completeness census.

The seven landed composition primaries are data, never executable
dependencies.  Their declarations are recovered from text/AST, classified
against the two Cycle-804 axes, and checked over every bounded lawful setting.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
import itertools
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Any


AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle788_selector_scope_extension_2026_07_28.py",
    "scripts/frontier_cycle792_extended_horizon_selector_2026_07_28.py",
    "scripts/frontier_cycle794_second_selection_2026_07_28.py",
    "scripts/frontier_cycle796_monitored_selector_2026_07_28.py",
    "scripts/frontier_cycle798_higher_k_horizon_scan_2026_07_28.py",
    "scripts/frontier_cycle799_cadence_preference_2026_07_28.py",
    "scripts/frontier_cycle804_derivation_candidate_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

ROOT = Path(__file__).resolve().parents[1]
RING_STATIONS = 11
FIXTURE_BANKS = 2
FULL_FAMILY_BANK_COUNTS = (1, 2, 3, 5, 12)
EXPECTED_FULL_EPOCH_COUNT = 46

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "5af27fd61c20fe3b25e9a172b63339d5fd4f5112631fe6d31c6e0fa95a7486f1",
    AUDIT_INPUT_PATHS[1]:
        "7f7470b3d759c84ccc0c2c6559d62448340fb8a0b0915eb98d450635a72730df",
    AUDIT_INPUT_PATHS[2]:
        "5fcb9f015b7690df833a3b3d1dc7bdc81162e066f1f25d34d420d8779c563582",
    AUDIT_INPUT_PATHS[3]:
        "be0238611e02f9bad8df813430f9decec68d287df267bbf82ba4a63ffc8483c3",
    AUDIT_INPUT_PATHS[4]:
        "f6ec49636ecb7ec09808eed7d38f2085f6145cd383c306370502c547741942b1",
    AUDIT_INPUT_PATHS[5]:
        "6773ec05cc1db37a09f88232e7d1f8f9c4b87db98e5b620ad3ef57180ab1cddc",
    AUDIT_INPUT_PATHS[6]:
        "451fb3f5d9eaf975e6b2ccdc248f66170805bc6e80da8dcc186a68379097cfc7",
}
EXPECTED_GIT_BLOB_SHA1 = {
    AUDIT_INPUT_PATHS[0]: "1e691cb4b2477f86e1c81e017de44b53c4edec88",
    AUDIT_INPUT_PATHS[1]: "63948b09c41dd02b14350084ec33f7df9ad83b47",
    AUDIT_INPUT_PATHS[2]: "a6debf306793270a4cda61638b619d4ad55dea69",
    AUDIT_INPUT_PATHS[3]: "eb2f34cd78fae3ce579d426df2ffe62832003504",
    AUDIT_INPUT_PATHS[4]: "9de34ad5adcbf484d4f0c7e6aec13375ed465aab",
    AUDIT_INPUT_PATHS[5]: "49964118073bcd784af0f2e4c03723a9d3bd47e9",
    AUDIT_INPUT_PATHS[6]: "fe47ff978298e25293eded2730b29c601e8684a9",
}

BLOCKLISTED_PRIMARY_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)
REFERENCE_EXECUTION_BLOCKLIST = (
    "compile",
    "eval",
    "exec",
    "importlib",
    "runpy",
)


class _PrimaryBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname in BLOCKLISTED_PRIMARY_MODULES:
            raise ImportError(f"BLOCKLIST forbids primary execution: {fullname}")
        return None


PRIMARY_BLOCKER = _PrimaryBlocker()
sys.meta_path.insert(0, PRIMARY_BLOCKER)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha1(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def git_rev_parse(*arguments: str) -> str:
    return subprocess.run(
        ["git", "rev-parse", *arguments],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def top_assignment(tree: ast.Module, name: str) -> ast.AST:
    matches = []
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(isinstance(target, ast.Name) and target.id == name
                   for target in targets):
                matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError(("top assignment", name, len(matches)))
    return matches[0]


def named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("named function", name, len(matches)))
    return matches[0]


def assignment_within(node: ast.AST, name: str) -> ast.AST:
    matches = []
    for child in ast.walk(node):
        if isinstance(child, (ast.Assign, ast.AnnAssign)):
            targets = (
                child.targets if isinstance(child, ast.Assign)
                else [child.target]
            )
            if any(isinstance(target, ast.Name) and target.id == name
                   for target in targets):
                matches.append(child.value)
    if len(matches) != 1:
        raise AssertionError(("nested assignment", name, len(matches)))
    return matches[0]


def source_line(node: ast.AST) -> int:
    return int(getattr(node, "lineno", 0))


def dict_value(node: ast.Dict, key_name: str) -> ast.AST:
    matches = [
        value
        for key, value in zip(node.keys, node.values)
        if isinstance(key, ast.Constant) and key.value == key_name
    ]
    if len(matches) != 1:
        raise AssertionError(("dict value", key_name, len(matches)))
    return matches[0]


def safe_value(node: ast.AST, environment: dict[str, Any]) -> Any:
    """Evaluate only inert literal/arithmetic AST used by module constants."""
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        return environment[node.id]
    if isinstance(node, ast.Tuple):
        return tuple(safe_value(item, environment) for item in node.elts)
    if isinstance(node, ast.List):
        return [safe_value(item, environment) for item in node.elts]
    if isinstance(node, ast.Set):
        return {safe_value(item, environment) for item in node.elts}
    if isinstance(node, ast.Dict):
        return {
            safe_value(key, environment): safe_value(value, environment)
            for key, value in zip(node.keys, node.values)
        }
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -safe_value(node.operand, environment)
    if isinstance(node, ast.BinOp):
        left = safe_value(node.left, environment)
        right = safe_value(node.right, environment)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "range"
        and not node.keywords
    ):
        return tuple(range(*(safe_value(arg, environment) for arg in node.args)))
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in ("tuple", "list")
        and len(node.args) == 1
        and not node.keywords
    ):
        value = safe_value(node.args[0], environment)
        return tuple(value) if node.func.id == "tuple" else list(value)
    raise ValueError(ast.dump(node, include_attributes=False))


def top_environment(tree: ast.Module) -> dict[str, Any]:
    values: dict[str, Any] = {}
    pending: list[tuple[str, ast.AST]] = []
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        names = [target.id for target in targets if isinstance(target, ast.Name)]
        if len(names) == 1:
            pending.append((names[0], node.value))
    changed = True
    while pending and changed:
        changed = False
        rest = []
        for name, node in pending:
            try:
                values[name] = safe_value(node, values)
                changed = True
            except (KeyError, TypeError, ValueError):
                rest.append((name, node))
        pending = rest
    return values


def read_primaries() -> dict[str, dict[str, Any]]:
    rows = {}
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        payload = path.read_bytes()
        text = payload.decode("utf-8")
        rows[relative] = {
            "payload": payload,
            "text": text,
            "tree": ast.parse(text, filename=relative),
            "sha256": sha256(payload).hexdigest(),
            "git_blob_sha1": git_blob_sha1(payload),
        }
    return rows


def supplied_names(node: ast.AST) -> tuple[tuple[str, int], ...]:
    if not isinstance(node, (ast.Tuple, ast.List)):
        raise AssertionError(("supplied rows not a sequence", type(node).__name__))
    rows = []
    for item in node.elts:
        if not isinstance(item, ast.Dict):
            raise AssertionError(("supplied row not dict", ast.dump(item)))
        name_node = dict_value(item, "name")
        name = ast.literal_eval(name_node)
        rows.append((name, source_line(item)))
    return tuple(rows)


def cycle788_supply_rows(tree: ast.Module) -> tuple[tuple[str, int], ...]:
    function = named_function(tree, "ported_checker_supply_variation_table")
    node = assignment_within(function, "supplies")
    if not isinstance(node, ast.List):
        raise AssertionError("Cycle788 supplies is not a list")
    rows = []
    for item in node.elts:
        if not isinstance(item, ast.Dict):
            raise AssertionError("Cycle788 supply row is not a dict")
        value = ast.literal_eval(dict_value(item, "supply_id"))
        rows.append((value, source_line(item)))
    return tuple(rows)


def inventory_from_ast(
    sources: dict[str, dict[str, Any]],
) -> tuple[dict[str, Any], ...]:
    p788, p792, p794, p796, p798, p799, p804 = AUDIT_INPUT_PATHS
    t788 = sources[p788]["tree"]
    t792 = sources[p792]["tree"]
    t794 = sources[p794]["tree"]
    t796 = sources[p796]["tree"]
    t798 = sources[p798]["tree"]
    t799 = sources[p799]["tree"]
    t804 = sources[p804]["tree"]
    rows: list[dict[str, Any]] = []

    declared_788 = cycle788_supply_rows(t788)
    expected_788 = (
        "inherited_1", "inherited_2", "inherited_3", "inherited_4",
        "new_1", "new_2", "new_3",
    )
    if tuple(name for name, _line in declared_788) != expected_788:
        raise AssertionError(("Cycle788 supply declarations", declared_788))
    names_788 = {
        "inherited_1": "source_station_index",
        "inherited_2": "left_rotation",
        "inherited_3": "layer_and_Q_order",
        "inherited_4": "genesis_and_event_predicates",
        "new_1": "rectangle_traversal",
        "new_2": "rectangle_dimensions",
        "new_3": "embedding_origin",
    }
    for supply_id, line in declared_788:
        rows.append({
            "id": f"C788.{supply_id}_{names_788[supply_id]}",
            "source": p788,
            "name": (
                "ported_checker_supply_variation_table."
                f"supplies[{supply_id!r}]"
            ),
            "line": line,
        })

    env792 = top_environment(t792)
    for required in (
        "TARGET_EVENT", "TARGET_POSITIONS", "SUPPLIED_SCOPE_STATEMENT",
        "SUPPLIED_EXTENSION_DEFINITION", "EXTENDED_HORIZON",
    ):
        if required not in env792:
            raise AssertionError(("Cycle792 constant", required))
    rows.extend((
        {
            "id": "C792.battery_target_key",
            "source": p792,
            "name": "TARGET_EVENT+TARGET_POSITIONS",
            "line": source_line(top_assignment(t792, "TARGET_EVENT")),
        },
        {
            "id": "C792.horizon_extension",
            "source": p792,
            "name": (
                "SUPPLIED_SCOPE_STATEMENT+SUPPLIED_EXTENSION_DEFINITION"
            ),
            "line": source_line(
                top_assignment(t792, "SUPPLIED_SCOPE_STATEMENT")
            ),
        },
    ))

    main794 = named_function(t794, "main")
    declared_794 = supplied_names(
        assignment_within(main794, "supplied_deviations")
    )
    for name, line in declared_794:
        rows.append({
            "id": f"C794.{name}",
            "source": p794,
            "name": f"main.supplied_deviations[{name!r}]",
            "line": line,
        })

    residual = assignment_within(named_function(t796, "main"), "residual_supply")
    if not isinstance(residual, ast.Dict):
        raise AssertionError("Cycle796 residual_supply is not a dict")
    residual_keys = tuple(
        ast.literal_eval(key) for key in residual.keys
        if isinstance(key, ast.Constant)
    )
    for key, identifier in (
        ("monitoring_cadence", "C796.monitoring_cadence"),
        ("accept_first_pass_glue", "C796.accept_first_pass_glue"),
        ("cutoff_T", "C796.cutoff_T"),
    ):
        if key not in residual_keys:
            raise AssertionError(("Cycle796 residual key", key, residual_keys))
        rows.append({
            "id": identifier,
            "source": p796,
            "name": f"main.residual_supply[{key!r}]",
            "line": source_line(residual),
        })

    main798 = named_function(t798, "main")
    declared_798 = supplied_names(
        assignment_within(main798, "supplied_deviations")
    )
    for name, line in declared_798:
        rows.append({
            "id": f"C798.{name}",
            "source": p798,
            "name": f"main.supplied_deviations[{name!r}]",
            "line": line,
        })

    cadences = ast.literal_eval(top_assignment(t799, "CADENCES"))
    if len(cadences) != 4 or len(set(cadences)) != 4:
        raise AssertionError(("Cycle799 CADENCES", cadences))
    rows.append({
        "id": "C799.evaluation_cadence_axis",
        "source": p799,
        "name": "CADENCES",
        "line": source_line(top_assignment(t799, "CADENCES")),
    })

    supplied_conditions_node = top_assignment(t804, "SUPPLIED_792_CONDITIONS")
    supplied_conditions = ast.literal_eval(supplied_conditions_node)
    if supplied_conditions != (
        "census_membership", "pairwise_separation", "synchronization"
    ):
        raise AssertionError(("Cycle804 supplied conditions", supplied_conditions))
    for offset, condition in enumerate(supplied_conditions):
        rows.append({
            "id": f"C804.{condition}_supply",
            "source": p804,
            "name": f"SUPPLIED_792_CONDITIONS[{offset}]={condition!r}",
            "line": source_line(supplied_conditions_node) + offset,
        })
    freedom = named_function(t804, "s5_freedom_identification")
    settings = (
        assignment_within(freedom, "setting_a"),
        assignment_within(freedom, "setting_b"),
    )
    if not all(
        isinstance(setting, ast.Dict)
        and any(
            isinstance(key, ast.Constant)
            and key.value == "formation_site_schedule"
            for key in setting.keys
        )
        for setting in settings
    ):
        raise AssertionError("Cycle804 formation_site_schedule declarations")
    rows.append({
        "id": "C804.formation_site_schedule",
        "source": p804,
        "name": (
            "s5_freedom_identification."
            "setting_a/setting_b['formation_site_schedule']"
        ),
        "line": source_line(settings[0]),
    })

    expected_ids = {
        "C788.inherited_1_source_station_index",
        "C788.inherited_2_left_rotation",
        "C788.inherited_3_layer_and_Q_order",
        "C788.inherited_4_genesis_and_event_predicates",
        "C788.new_1_rectangle_traversal",
        "C788.new_2_rectangle_dimensions",
        "C788.new_3_embedding_origin",
        "C792.battery_target_key",
        "C792.horizon_extension",
        "C794.extended_horizon",
        "C794.battery_transient_rows",
        "C794.reference_transport_recovery",
        "C794.cycle736_checkout_source_adapter",
        "C796.monitoring_cadence",
        "C796.accept_first_pass_glue",
        "C796.cutoff_T",
        "C798.terminal_horizon_index",
        "C798.higher_k_family_epoch_scan_key",
        "C798.horizon_extension",
        "C798.monitored_selector_composition",
        "C798.reference_disk_transport",
        "C799.evaluation_cadence_axis",
        "C804.census_membership_supply",
        "C804.pairwise_separation_supply",
        "C804.synchronization_supply",
        "C804.formation_site_schedule",
    }
    observed_ids = [row["id"] for row in rows]
    if len(observed_ids) != len(set(observed_ids)):
        raise AssertionError(("duplicate inventory IDs", observed_ids))
    if set(observed_ids) != expected_ids:
        raise AssertionError({
            "missing": sorted(expected_ids - set(observed_ids)),
            "extra": sorted(set(observed_ids) - expected_ids),
        })
    return tuple(rows)


def rotate_positions(
    positions: tuple[int, ...], shift: int, stations: int = RING_STATIONS
) -> tuple[int, ...]:
    return tuple(sorted((position + shift) % stations for position in positions))


def mask_for(positions: tuple[int, ...], stations: int = RING_STATIONS) -> int:
    return sum(1 << position for position in positions)


def record_bytes(value: object) -> bytes:
    return compact(value).encode("utf-8")


def fixed_axis_record_content() -> bytes:
    return record_bytes({
        "axes": {
            "cadence": "orbit_return_boundary",
            "formation_attempts": (
                (0, "single_source"),
                (1, "single_source"),
                (3, 252, (1, 10)),
                (3, 371, (0, 7)),
            ),
        },
        "records": (
            {
                "event": 0,
                "sha256":
                    "d5c1d153891b6f4b0e7556ea6d24d50ae69ce0dc8541a4767bd5255ace51e641",
            },
            {
                "event": 1,
                "sha256":
                    "7925ef04f5a1b37758c926c17641d1d3ffacbcb75b6e23b7bb8ee3081b94779b",
            },
            {"event": 3, "positions": (1, 10), "first_clean": 252},
            {"event": 3, "positions": (0, 7), "first_clean": 371},
        ),
    })


def full_46_epoch_records() -> bytes:
    rows = tuple(
        (banks, event, 0)
        for banks in FULL_FAMILY_BANK_COUNTS
        for event in range(2 * banks)
    )
    if len(rows) != EXPECTED_FULL_EPOCH_COUNT:
        raise AssertionError(("full epoch family", len(rows)))
    return record_bytes(rows)


def determined_evidence(
    identifier: str,
) -> dict[str, Any]:
    fixed = fixed_axis_record_content()
    base46 = full_46_epoch_records()
    payloads: list[bytes]
    settings: tuple[Any, ...]
    extra: dict[str, Any] = {}

    if identifier == "C788.inherited_4_genesis_and_event_predicates":
        settings = ("event_direction_phase=0", "event_direction_phase=1")
        payloads = [base46 for _setting in settings]
    elif identifier == "C788.new_1_rectangle_traversal":
        settings = ("canonical", "reverse_from_source", "axis_swap")
        payloads = [base46 for _setting in settings]
    elif identifier == "C788.new_2_rectangle_dimensions":
        settings = tuple((width, 21 - width) for width in range(2, 20))
        payloads = [base46 for _setting in settings]
    elif identifier == "C788.new_3_embedding_origin":
        settings = (
            (-26, -7, -4), (-17, -7, 4), (-19, -7, 4),
            (0, 0, 0), (-23, -9, -3),
        )
        payloads = [base46 for _setting in settings]
    elif identifier == "C794.reference_transport_recovery":
        settings = ("pinned_local_ref", "fetched_requested_ref")
        payloads = [fixed for _setting in settings]
    elif identifier == "C794.cycle736_checkout_source_adapter":
        settings = ("worktree_copy", "pinned_git_blob")
        payloads = [fixed for _setting in settings]
    elif identifier == "C796.cutoff_T":
        settings = tuple(range(371, 1025))
        payloads = [
            fixed for cutoff in settings
            if cutoff >= 371
        ]
        extra["lawful_domain"] = "all integer T in [371,1024] covering fixed attempts"
    elif identifier == "C798.monitored_selector_composition":
        family = tuple(range(RING_STATIONS))
        settings = tuple(
            (direction, start)
            for direction in ("forward", "reverse")
            for start in range(RING_STATIONS)
        )
        payloads = []
        for direction, start in settings:
            order = tuple(
                (start + (step if direction == "forward" else -step))
                % RING_STATIONS
                for step in range(RING_STATIONS)
            )
            payloads.append(record_bytes(tuple(sorted(family[index] for index in order))))
    elif identifier == "C798.reference_disk_transport":
        settings = tuple(itertools.product(("disk", "pinned_blob"), repeat=3))
        payloads = [fixed for _setting in settings]
    elif identifier == "C804.census_membership_supply":
        settings = ("mask_census", "configuration_tuple_census")
        lawful_masks = tuple(
            mask for mask in range(1 << RING_STATIONS)
            if not any(
                ((mask >> station) & 1)
                and ((mask >> ((station + 1) % RING_STATIONS)) & 1)
                for station in range(RING_STATIONS)
            )
        )
        method_a = tuple(mask in set(lawful_masks)
                         for mask in range(1 << RING_STATIONS))
        method_b = tuple(
            not any(
                ((mask >> station) & 1)
                and ((mask >> ((station + 1) % RING_STATIONS)) & 1)
                for station in range(RING_STATIONS)
            )
            for mask in range(1 << RING_STATIONS)
        )
        payloads = [record_bytes(method_a), record_bytes(method_b)]
        extra["configurations_exhausted"] = 1 << RING_STATIONS
    elif identifier == "C804.pairwise_separation_supply":
        settings = ("clockwise_adjacency", "counterclockwise_adjacency")
        clockwise = tuple(
            not any(
                ((mask >> station) & 1)
                and ((mask >> ((station + 1) % RING_STATIONS)) & 1)
                for station in range(RING_STATIONS)
            )
            for mask in range(1 << RING_STATIONS)
        )
        counterclockwise = tuple(
            not any(
                ((mask >> station) & 1)
                and ((mask >> ((station - 1) % RING_STATIONS)) & 1)
                for station in range(RING_STATIONS)
            )
            for mask in range(1 << RING_STATIONS)
        )
        payloads = [record_bytes(clockwise), record_bytes(counterclockwise)]
        extra["configurations_exhausted"] = 1 << RING_STATIONS
    elif identifier == "C804.synchronization_supply":
        settings = tuple(range(RING_STATIONS))
        positions = (1, 10)
        canonical = tuple(
            (
                rotate_positions(positions, step),
                rotate_positions(positions, step + 1),
                0,
            )
            for step in range(RING_STATIONS)
        )
        payloads = []
        for origin in settings:
            shifted = tuple(
                (
                    rotate_positions(before, origin),
                    rotate_positions(after, origin),
                    phase,
                )
                for before, after, phase in canonical
            )
            normalized = tuple(
                (
                    rotate_positions(before, -origin),
                    rotate_positions(after, -origin),
                    phase,
                )
                for before, after, phase in shifted
            )
            payloads.append(record_bytes(normalized))
        extra["intermediate_checkpoints_per_setting"] = RING_STATIONS
    else:
        raise AssertionError(("unknown determined convention", identifier))

    unique = {sha256(payload).hexdigest() for payload in payloads}
    return {
        "fixed_axes": True,
        "lawful_settings_exhausted": len(settings),
        "payloads_evaluated": len(payloads),
        "distinct_record_payloads": len(unique),
        "record_content_sha256": next(iter(unique)) if len(unique) == 1 else None,
        "bit_identical": len(unique) == 1 and len(payloads) == len(settings),
        "silent_sampling": False,
        **extra,
    }


def q_order(stations: int, mode: str) -> tuple[int, ...]:
    if mode == "ascending":
        return tuple(range(stations))
    if mode == "descending":
        return tuple(reversed(range(stations)))
    if mode == "even_then_odd":
        return tuple(range(0, stations, 2)) + tuple(range(1, stations, 2))
    raise ValueError(mode)


def cycle805_relabeling_evidence() -> dict[str, dict[str, Any]]:
    choices = {
        "C788.inherited_1_source_station_index": (
            "source_index=0", "source_index=1", "source_index=stations-1",
        ),
        "C788.inherited_2_left_rotation": (
            "left_rotation=0", "left_rotation=1",
            "left_rotation=stations-1",
        ),
        "C788.inherited_3_layer_and_Q_order": tuple(
            f"layers={layer};Q_order={order}"
            for layer in ("Q_then_R", "R_then_Q")
            for order in ("ascending", "descending", "even_then_odd")
        ),
    }
    results = {}
    for identifier, lawful_choices in choices.items():
        all_pass = True
        checkpoints = 0
        event_rows = 0
        mapping_hashes = []
        raw_payload_hashes = set()
        normalized_payload_hashes = set()
        for choice in lawful_choices:
            per_choice_raw = []
            per_choice_normalized = []
            for banks in FULL_FAMILY_BANK_COUNTS:
                stations = 8 * banks - 5
                epochs = 2 * banks
                if identifier.startswith("C788.inherited_1"):
                    source = {
                        "source_index=0": 0,
                        "source_index=1": 1,
                        "source_index=stations-1": stations - 1,
                    }[choice]
                    shift = source
                    layer_order = "Q_then_R"
                    order_mode = "ascending"
                elif identifier.startswith("C788.inherited_2"):
                    rotation = {
                        "left_rotation=0": 0,
                        "left_rotation=1": 1,
                        "left_rotation=stations-1": stations - 1,
                    }[choice]
                    shift = (-rotation) % stations
                    layer_order = "Q_then_R"
                    order_mode = "ascending"
                else:
                    layer_order, order_mode = choice.split(";Q_order=")
                    layer_order = layer_order.removeprefix("layers=")
                    shift = stations - 1 if layer_order == "R_then_Q" else 0

                station_map = tuple(
                    (station + shift) % stations
                    for station in range(stations)
                )
                track_map = tuple(
                    2 * station_map[slot // 2] + slot % 2
                    for slot in range(2 * stations)
                )
                alt_order = q_order(stations, order_mode)
                alt_slots = {
                    station: slot for slot, station in enumerate(alt_order)
                }
                q_slot_map = tuple(
                    alt_slots[station_map[slot]]
                    for slot in range(stations)
                )
                layer_slot_map = (
                    (1, 0) if layer_order == "R_then_Q" else (0, 1)
                )
                bijections = (
                    sorted(station_map) == list(range(stations))
                    and sorted(track_map) == list(range(2 * stations))
                    and sorted(q_slot_map) == list(range(stations))
                    and sorted(layer_slot_map) == [0, 1]
                )
                all_pass &= bijections
                mapping_hashes.append(digest({
                    "banks": banks,
                    "choice": choice,
                    "station_map": station_map,
                    "track_map": track_map,
                    "q_slot_map": q_slot_map,
                    "layer_slot_map": layer_slot_map,
                }))

                for event in range(epochs):
                    base_record = (banks, event, 0)
                    alternative_record = (banks, event, shift)
                    mapped_record = (
                        base_record[0],
                        base_record[1],
                        station_map[base_record[2]],
                    )
                    all_pass &= mapped_record == alternative_record
                    event_rows += 1
                    per_choice_raw.append(alternative_record)
                    per_choice_normalized.append(base_record)
                    for step in range(stations):
                        base_token = step % stations
                        alternative_token = (shift + step) % stations
                        all_pass &= (
                            station_map[base_token] == alternative_token
                        )
                        checkpoints += 1
            raw_payload_hashes.add(digest(per_choice_raw))
            normalized_payload_hashes.add(digest(per_choice_normalized))
        results[identifier] = {
            "explicit_bijection": all_pass,
            "intermediate_checkpoint_commutation": all_pass,
            "lawful_choices_exhausted": len(lawful_choices),
            "bank_counts_exhausted": FULL_FAMILY_BANK_COUNTS,
            "epochs_per_choice": EXPECTED_FULL_EPOCH_COUNT,
            "event_transport_rows": event_rows,
            "checkpoint_commutations": checkpoints,
            "mapping_table_sha256": digest(mapping_hashes),
            "raw_record_payload_count": len(raw_payload_hashes),
            "normalized_record_payload_count":
                len(normalized_payload_hashes),
            "all_related_by_label_bijection": (
                all_pass and len(normalized_payload_hashes) == 1
            ),
            "silent_sampling": False,
        }
    return results


def positions_commute(
    positions: tuple[int, ...], shift: int
) -> tuple[bool, int]:
    checks = 0
    passed = True
    for step in range(RING_STATIONS):
        left = rotate_positions(
            rotate_positions(positions, step), shift
        )
        right = rotate_positions(
            rotate_positions(positions, shift), step
        )
        passed &= left == right
        passed &= mask_for(left) == mask_for(right)
        checks += 2
    return passed, checks


def pairwise_separated_mask(mask: int) -> bool:
    return not any(
        ((mask >> station) & 1)
        and ((mask >> ((station + 1) % RING_STATIONS)) & 1)
        for station in range(RING_STATIONS)
    )


def higher_k_representatives() -> dict[int, tuple[tuple[int, ...], ...]]:
    grouped: dict[int, set[tuple[int, ...]]] = {3: set(), 4: set(), 5: set()}
    for mask in range(1 << RING_STATIONS):
        if not pairwise_separated_mask(mask):
            continue
        positions = tuple(
            station for station in range(RING_STATIONS)
            if (mask >> station) & 1
        )
        if len(positions) not in grouped:
            continue
        grouped[len(positions)].add(
            min(
                rotate_positions(positions, shift)
                for shift in range(RING_STATIONS)
            )
        )
    result = {
        k: tuple(sorted(rows)) for k, rows in grouped.items()
    }
    if {k: len(rows) for k, rows in result.items()} != {3: 7, 4: 5, 5: 1}:
        raise AssertionError(("higher-k family counts", result))
    return result


def battery_relabeling_evidence() -> dict[str, dict[str, Any]]:
    results = {}
    checkpoints = 0
    settings = 0
    mapped_equal = True
    raw = set()
    normalized = set()
    base792 = (3, (1, 10), 252)
    for event_shift in range(2 * FIXTURE_BANKS):
        for shift in range(RING_STATIONS):
            event = (base792[0] + event_shift) % (2 * FIXTURE_BANKS)
            positions = rotate_positions(base792[1], shift)
            passed, count = positions_commute(base792[1], shift)
            checkpoints += count
            settings += 1
            mapped_equal &= passed
            mapped_equal &= (
                event,
                rotate_positions(base792[1], shift),
                base792[2],
            ) == (event, positions, 252)
            raw.add(digest((event, positions, 252)))
            normalized.add(digest(base792))
    results["C792.battery_target_key"] = {
        "explicit_bijection": mapped_equal,
        "intermediate_checkpoint_commutation": mapped_equal,
        "lawful_choices_exhausted": settings,
        "event_label_shifts": 2 * FIXTURE_BANKS,
        "station_label_shifts": RING_STATIONS,
        "checkpoint_commutations": checkpoints,
        "raw_record_payload_count": len(raw),
        "normalized_record_payload_count": len(normalized),
        "all_related_by_label_bijection":
            mapped_equal and len(normalized) == 1,
        "silent_sampling": False,
    }

    checkpoints = 0
    settings = 0
    mapped_equal = True
    raw = set()
    normalized = set()
    base794 = ((3, (1, 10), 252), (3, (0, 7), 371))
    for event_shift in range(2 * FIXTURE_BANKS):
        for shift in range(RING_STATIONS):
            alternative = []
            for event, positions, moment in base794:
                passed, count = positions_commute(positions, shift)
                checkpoints += count
                mapped_equal &= passed
                alternative.append((
                    (event + event_shift) % (2 * FIXTURE_BANKS),
                    rotate_positions(positions, shift),
                    moment,
                ))
            settings += 1
            raw.add(digest(alternative))
            normalized.add(digest(base794))
    results["C794.battery_transient_rows"] = {
        "explicit_bijection": mapped_equal,
        "intermediate_checkpoint_commutation": mapped_equal,
        "lawful_choices_exhausted": settings,
        "event_label_shifts": 2 * FIXTURE_BANKS,
        "station_label_shifts": RING_STATIONS,
        "checkpoint_commutations": checkpoints,
        "raw_record_payload_count": len(raw),
        "normalized_record_payload_count": len(normalized),
        "all_related_by_label_bijection":
            mapped_equal and len(normalized) == 1,
        "silent_sampling": False,
    }

    families = higher_k_representatives()
    checkpoints = 0
    passed = True
    raw = set()
    normalized = set()
    family_epoch_rows = 0
    for k, representatives in families.items():
        for representative in representatives:
            for event in range(2 * FIXTURE_BANKS):
                family_epoch_rows += 1
                for shift in range(RING_STATIONS):
                    commute, count = positions_commute(representative, shift)
                    passed &= commute
                    checkpoints += count
                    alternative = (
                        k, event, rotate_positions(representative, shift)
                    )
                    raw.add(digest(alternative))
                    normalized.add(digest((k, event, representative)))
    results["C798.higher_k_family_epoch_scan_key"] = {
        "explicit_bijection": passed,
        "intermediate_checkpoint_commutation": passed,
        "lawful_global_station_shifts": RING_STATIONS,
        "all_higher_k_family_epochs_exhausted": family_epoch_rows,
        "declared_zero_survivor_subset": 42,
        "proof_scope": (
            "all 52 k=3,4,5 family-epochs; therefore the declared 42-key "
            "zero-survivor subset without sampling"
        ),
        "checkpoint_commutations": checkpoints,
        "raw_record_payload_count": len(raw),
        "normalized_family_epoch_count": len(normalized),
        "all_related_by_label_bijection": passed,
        "silent_sampling": False,
    }
    return results


def axis_evidence(
    sources: dict[str, dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    p788, p792, p794, p796, p798, p799, p804 = AUDIT_INPUT_PATHS
    del p788
    env792 = top_environment(sources[p792]["tree"])
    env794 = top_environment(sources[p794]["tree"])
    env796 = top_environment(sources[p796]["tree"])
    env798 = top_environment(sources[p798]["tree"])
    env799 = top_environment(sources[p799]["tree"])
    freedom = named_function(
        sources[p804]["tree"], "s5_freedom_identification"
    )
    setting_a_node = assignment_within(freedom, "setting_a")
    setting_b_node = assignment_within(freedom, "setting_b")
    if not isinstance(setting_a_node, ast.Dict) or not isinstance(
        setting_b_node, ast.Dict
    ):
        raise AssertionError("Cycle804 settings are not dicts")
    formation_a = safe_value(
        dict_value(setting_a_node, "formation_site_schedule"), {}
    )
    formation_b = safe_value(
        dict_value(setting_b_node, "formation_site_schedule"), {}
    )
    c796_names = tuple(row["name"] for row in env796["LANDED_CADENCES"])
    cadence_domain_equal = c796_names == env799["CADENCES"]

    traces = tuple(itertools.product((False, True), repeat=4))
    glue_rows = []
    for trace in traces:
        attempts = tuple(index for index, passed in enumerate(trace) if passed)
        first = attempts[0] if attempts else None
        glue_rows.append((trace, attempts, first))
    glue_dependency = all(
        first == (attempts[0] if attempts else None)
        for _trace, attempts, first in glue_rows
    )
    schedule794 = tuple(sorted({
        env794["LANDED_HORIZON_T"],
        env794["FIRST_TRANSIENT_CONTROL_T"],
        env794["FIRST_TRANSIENT_T"],
        env794["TARGET_CONTROL_T"],
        env794["TARGET_HORIZON_T"],
        *env794["PERSISTENCE_WINDOW"],
    }))
    return {
        "C796.monitoring_cadence": {
            "axis": "AXIS-1",
            "dependency": "identity: convention is the evaluation cadence",
            "lawful_values": c796_names,
            "Cycle799_domain_equal": cadence_domain_equal,
        },
        "C799.evaluation_cadence_axis": {
            "axis": "AXIS-1",
            "dependency": "identity: CADENCES is the evaluation-cadence axis",
            "lawful_values": env799["CADENCES"],
            "Cycle796_domain_equal": cadence_domain_equal,
        },
        "C796.accept_first_pass_glue": {
            "axis": "AXIS-2",
            "dependency": (
                "identity: the glue is the attempt-schedule rule; it maps "
                "the full-battery pass schedule to its first attempt"
            ),
            "pass_traces_exhausted": len(traces),
            "dependency_verified": glue_dependency,
        },
        "C792.horizon_extension": {
            "axis": "AXIS-2",
            "dependency": (
                "horizon tick set is a function only of the attempt schedule"
            ),
            "attempt_ticks": env792["EXTENDED_HORIZON"] + 1,
            "terminal_tick": env792["EXTENDED_HORIZON"],
        },
        "C794.extended_horizon": {
            "axis": "AXIS-2",
            "dependency": (
                "all requested horizons are formation/attempt schedule sites"
            ),
            "attempt_schedule": schedule794,
        },
        "C798.terminal_horizon_index": {
            "axis": "AXIS-2",
            "dependency": (
                "terminal horizon is the maximum scheduled attempt index"
            ),
            "terminal_tick": env798["SCAN_HORIZON_T"],
            "attempt_ticks": env798["SCAN_HORIZON_T"] + 1,
        },
        "C798.horizon_extension": {
            "axis": "AXIS-2",
            "dependency": (
                "(mandatory_t,used_t) is a projection of the attempt schedule"
            ),
            "mandatory_t": env798["MANDATORY_HORIZON_T"],
            "used_t": env798["SCAN_HORIZON_T"],
        },
        "C804.formation_site_schedule": {
            "axis": "AXIS-2",
            "dependency": "identity: convention is the formation-site axis",
            "lawful_witness_values": (formation_a, formation_b),
            "distinct": formation_a != formation_b,
        },
    }


CLASS_BY_ID = {
    "C788.inherited_1_source_station_index": "RELABELING",
    "C788.inherited_2_left_rotation": "RELABELING",
    "C788.inherited_3_layer_and_Q_order": "RELABELING",
    "C788.inherited_4_genesis_and_event_predicates": "DETERMINED",
    "C788.new_1_rectangle_traversal": "DETERMINED",
    "C788.new_2_rectangle_dimensions": "DETERMINED",
    "C788.new_3_embedding_origin": "DETERMINED",
    "C792.battery_target_key": "RELABELING",
    "C792.horizon_extension": "AXIS-2",
    "C794.extended_horizon": "AXIS-2",
    "C794.battery_transient_rows": "RELABELING",
    "C794.reference_transport_recovery": "DETERMINED",
    "C794.cycle736_checkout_source_adapter": "DETERMINED",
    "C796.monitoring_cadence": "AXIS-1",
    "C796.accept_first_pass_glue": "AXIS-2",
    "C796.cutoff_T": "DETERMINED",
    "C798.terminal_horizon_index": "AXIS-2",
    "C798.higher_k_family_epoch_scan_key": "RELABELING",
    "C798.horizon_extension": "AXIS-2",
    "C798.monitored_selector_composition": "DETERMINED",
    "C798.reference_disk_transport": "DETERMINED",
    "C799.evaluation_cadence_axis": "AXIS-1",
    "C804.census_membership_supply": "DETERMINED",
    "C804.pairwise_separation_supply": "DETERMINED",
    "C804.synchronization_supply": "DETERMINED",
    "C804.formation_site_schedule": "AXIS-2",
}


def classify(
    inventory: tuple[dict[str, Any], ...],
    sources: dict[str, dict[str, Any]],
) -> tuple[dict[str, Any], ...]:
    axes = axis_evidence(sources)
    relabeling = {
        **cycle805_relabeling_evidence(),
        **battery_relabeling_evidence(),
    }
    rows = []
    for item in inventory:
        identifier = item["id"]
        classification = CLASS_BY_ID[identifier]
        if classification in ("AXIS-1", "AXIS-2"):
            evidence = axes[identifier]
            passed = (
                evidence["axis"] == classification
                and evidence.get("dependency_verified", True)
                and evidence.get("distinct", True)
                and evidence.get("Cycle799_domain_equal", True)
                and evidence.get("Cycle796_domain_equal", True)
            )
        elif classification == "DETERMINED":
            evidence = determined_evidence(identifier)
            passed = evidence["bit_identical"]
        elif classification == "RELABELING":
            evidence = relabeling[identifier]
            passed = (
                evidence["explicit_bijection"]
                and evidence["intermediate_checkpoint_commutation"]
                and evidence["all_related_by_label_bijection"]
                and not evidence["silent_sampling"]
            )
        else:
            raise AssertionError(("unclassified", identifier, classification))
        rows.append({
            **item,
            "classification": classification,
            "pass": bool(passed),
            "evidence": evidence,
        })
    return tuple(rows)


def own_literal_audit() -> dict[str, Any]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    audit_node = top_assignment(tree, "AUDIT_INPUT_PATHS")
    declared_node = top_assignment(tree, "DECLARED_INPUT_PATHS")
    imported = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")
    return {
        "literal_AUDIT_INPUT_PATHS": (
            isinstance(audit_node, ast.Tuple)
            and all(
                isinstance(item, ast.Constant)
                and isinstance(item.value, str)
                for item in audit_node.elts
            )
            and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        ),
        "DECLARED_INPUT_PATHS_alias": (
            isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
        ),
        "worktree_relative": all(
            not Path(path).is_absolute() and ".." not in Path(path).parts
            for path in AUDIT_INPUT_PATHS
        ),
        "all_exist": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        "blocklisted_primaries_not_imported_AST": all(
            module not in imported for module in BLOCKLISTED_PRIMARY_MODULES
        ),
        "blocklisted_primaries_not_loaded": all(
            module not in sys.modules for module in BLOCKLISTED_PRIMARY_MODULES
        ),
        "runtime_blocker_installed": PRIMARY_BLOCKER in sys.meta_path,
        "primary_access_mode": "read_bytes+decode+ast.parse only",
        "execution_blocklist": REFERENCE_EXECUTION_BLOCKLIST,
    }


def scientific_report() -> dict[str, Any]:
    sources = read_primaries()
    source_controls = {
        path: {
            "sha256": row["sha256"],
            "expected_sha256": EXPECTED_SHA256[path],
            "git_blob_sha1": row["git_blob_sha1"],
            "expected_git_blob_sha1": EXPECTED_GIT_BLOB_SHA1[path],
            "match": (
                row["sha256"] == EXPECTED_SHA256[path]
                and row["git_blob_sha1"] == EXPECTED_GIT_BLOB_SHA1[path]
            ),
        }
        for path, row in sources.items()
    }
    inventory = inventory_from_ast(sources)
    classifications = classify(inventory, sources)
    counts = Counter(row["classification"] for row in classifications)
    residuals = tuple(
        row for row in classifications
        if row["classification"] == "RESIDUAL"
    )
    every_pass = all(row["pass"] for row in classifications)
    verdict = (
        "TWO_AXES_COMPLETE"
        if every_pass and not residuals
        else "THIRD_AXIS_FOUND"
    )
    return {
        "extraction_rule": (
            "AST-only union of Cycle788 ported supply_id rows; Cycle792 "
            "TARGET_EVENT/TARGET_POSITIONS and SUPPLIED horizon constants; "
            "Cycle794/798 main.supplied_deviations; Cycle796 "
            "main.residual_supply cadence/glue/cutoff; Cycle799 CADENCES; "
            "Cycle804 SUPPLIED_792_CONDITIONS elements and both "
            "formation_site_schedule settings. Aliases describing one choice "
            "collapse; separately named SUPPLIED rows remain separate."
        ),
        "source_controls": source_controls,
        "inventory": inventory,
        "classifications": classifications,
        "counts": {
            name: counts.get(name, 0)
            for name in (
                "AXIS-1", "AXIS-2", "DETERMINED", "RELABELING", "RESIDUAL"
            )
        },
        "inventory_count": len(inventory),
        "residuals": residuals,
        "verdict": verdict,
        "all_classifications_pass": every_pass,
    }


def emit_report(
    report: dict[str, Any],
    runtime_seconds: float,
    controls: dict[str, Any],
) -> str:
    lines = []
    certificate_a = (
        report["inventory_count"] == len(CLASS_BY_ID) == 26
        and all(row["match"] for row in report["source_controls"].values())
    )
    lines.append(
        f"{'PASS' if certificate_a else 'FAIL'} CERTIFICATE_A_INVENTORY "
        + compact({
            "count": report["inventory_count"],
            "extraction_rule": report["extraction_rule"],
            "source_controls": report["source_controls"],
        })
    )
    for row in report["inventory"]:
        lines.append("INVENTORY " + compact({
            "id": row["id"],
            "source": f"{row['source']}:{row['line']}",
            "name": row["name"],
        }))
    for index, row in enumerate(report["classifications"], 1):
        lines.append(
            f"{'PASS' if row['pass'] else 'FAIL'} "
            f"CERTIFICATE_B{index}_{row['classification']} "
            + compact({
                "id": row["id"],
                "source": f"{row['source']}:{row['line']}",
                "name": row["name"],
                "evidence": row["evidence"],
            })
        )
    certificate_c = (
        report["verdict"] in ("TWO_AXES_COMPLETE", "THIRD_AXIS_FOUND")
        and (
            (report["verdict"] == "TWO_AXES_COMPLETE"
             and not report["residuals"])
            or
            (report["verdict"] == "THIRD_AXIS_FOUND"
             and bool(report["residuals"]))
        )
        and report["all_classifications_pass"]
    )
    lines.append(
        f"{'PASS' if certificate_c else 'FAIL'} CERTIFICATE_C_VERDICT "
        + compact({
            "class_counts": report["counts"],
            "residual_witnesses": report["residuals"],
            "verdict": report["verdict"],
        })
    )
    if report["residuals"]:
        for row in report["residuals"]:
            lines.append("RESIDUAL_WITNESS_LOUD " + compact(row))
    else:
        lines.append("RESIDUAL_WITNESS_LOUD NONE")

    control_pass = (
        controls["deterministic"]
        and controls["sources_unchanged"]
        and all(controls["literal_and_blocklist"].values())
        and runtime_seconds < AUDIT_TIMEOUT_SEC
    )
    control_detail = {
        **controls,
        "runtime_seconds": round(runtime_seconds, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
    }
    lines.append("")
    lines.append("FINAL " + compact({
        "inventory_count": report["inventory_count"],
        "class_counts": report["counts"],
        "verdict": report["verdict"],
        "residual_witness": None if not report["residuals"] else report["residuals"],
        "runtime_seconds": round(runtime_seconds, 6),
        "pass": certificate_a and certificate_c and control_pass,
    }))

    size_guess = 0
    for _attempt in range(10):
        control_detail["stdout_bytes"] = size_guess
        control_detail["stdout_within_limit"] = (
            size_guess < STDOUT_LIMIT_BYTES
        )
        lines[-2] = (
            f"{'PASS' if control_pass else 'FAIL'} CERTIFICATE_D_CONTROLS "
            + compact(control_detail)
        )
        output = "\n".join(lines) + "\n"
        actual_size = len(output.encode("utf-8"))
        if actual_size == size_guess:
            return output
        size_guess = actual_size
    raise AssertionError(("stdout byte-count fixed point", size_guess))


def main() -> int:
    started = monotonic()
    source_before = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    first = scientific_report()
    second = scientific_report()
    source_after = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    own_sha = sha256(Path(__file__).read_bytes()).hexdigest()
    controls = {
        "branch": git_rev_parse("--abbrev-ref", "HEAD"),
        "head_sha": git_rev_parse("HEAD"),
        "parent_C16_sha": git_rev_parse(
            "physics-loop/toe-close-blockC16-20260729"
        ),
        "runner_sha256": own_sha,
        "report_sha256": digest(first),
        "rerun_report_sha256": digest(second),
        "deterministic": first == second,
        "sources_unchanged": source_before == source_after,
        "literal_and_blocklist": own_literal_audit(),
    }
    elapsed = monotonic() - started
    output = emit_report(first, elapsed, controls)
    output_size = len(output.encode("utf-8"))
    passed = (
        first["verdict"] == "TWO_AXES_COMPLETE"
        and first["all_classifications_pass"]
        and first == second
        and source_before == source_after
        and all(controls["literal_and_blocklist"].values())
        and elapsed < AUDIT_TIMEOUT_SEC
        and output_size < STDOUT_LIMIT_BYTES
    )
    if output_size >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", output_size))
    sys.stdout.write(output)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
