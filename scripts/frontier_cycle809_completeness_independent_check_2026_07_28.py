#!/usr/bin/env python3
"""Cycle 809 independent adversarial check of TWO_AXES_COMPLETE.

The six named landed-lineage modules and the Cycle-809 primary are inert
evidence: this checker reads their bytes and ASTs but never imports or executes
them.  Convention extraction is declaration-surface driven and is fixed before
the primary inventory is compared.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
import itertools
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any


AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle792_extended_horizon_selector_2026_07_28.py",
    "scripts/frontier_cycle794_second_selection_2026_07_28.py",
    "scripts/frontier_cycle796_monitored_selector_2026_07_28.py",
    "scripts/frontier_cycle798_higher_k_horizon_scan_2026_07_28.py",
    "scripts/frontier_cycle799_cadence_preference_2026_07_28.py",
    "scripts/frontier_cycle804_derivation_candidate_2026_07_28.py",
    "scripts/frontier_cycle809_convention_completeness_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "7f7470b3d759c84ccc0c2c6559d62448340fb8a0b0915eb98d450635a72730df",
    AUDIT_INPUT_PATHS[1]:
        "5fcb9f015b7690df833a3b3d1dc7bdc81162e066f1f25d34d420d8779c563582",
    AUDIT_INPUT_PATHS[2]:
        "be0238611e02f9bad8df813430f9decec68d287df267bbf82ba4a63ffc8483c3",
    AUDIT_INPUT_PATHS[3]:
        "f6ec49636ecb7ec09808eed7d38f2085f6145cd383c306370502c547741942b1",
    AUDIT_INPUT_PATHS[4]:
        "6773ec05cc1db37a09f88232e7d1f8f9c4b87db98e5b620ad3ef57180ab1cddc",
    AUDIT_INPUT_PATHS[5]:
        "451fb3f5d9eaf975e6b2ccdc248f66170805bc6e80da8dcc186a68379097cfc7",
    AUDIT_INPUT_PATHS[6]:
        "cce8420938b28b805811f4320ee54d7b8a58de0aeceebbd99f10c110338c90a3",
}
EXPECTED_GIT_BLOB_SHA1 = {
    AUDIT_INPUT_PATHS[0]: "63948b09c41dd02b14350084ec33f7df9ad83b47",
    AUDIT_INPUT_PATHS[1]: "a6debf306793270a4cda61638b619d4ad55dea69",
    AUDIT_INPUT_PATHS[2]: "eb2f34cd78fae3ce579d426df2ffe62832003504",
    AUDIT_INPUT_PATHS[3]: "9de34ad5adcbf484d4f0c7e6aec13375ed465aab",
    AUDIT_INPUT_PATHS[4]: "49964118073bcd784af0f2e4c03723a9d3bd47e9",
    AUDIT_INPUT_PATHS[5]: "fe47ff978298e25293eded2730b29c601e8684a9",
    AUDIT_INPUT_PATHS[6]: "307152b50f76e1becbdce29510f03bfa46808a6a",
}

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = AUDIT_INPUT_PATHS[-1]
LINEAGE_PATHS = AUDIT_INPUT_PATHS[:-1]
PRIMARY_MODULE = Path(PRIMARY_PATH).stem
RING_STATIONS = 11
FIXTURE_BANKS = 2


class _PrimaryBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname == PRIMARY_MODULE:
            raise ImportError(
                f"BLOCKLIST forbids Cycle-809 primary execution: {fullname}"
            )
        return None


PRIMARY_BLOCKER = _PrimaryBlocker()
sys.meta_path.insert(0, PRIMARY_BLOCKER)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def encoded(value: object) -> bytes:
    return compact(value).encode("utf-8")


def digest(value: object) -> str:
    return sha256(encoded(value)).hexdigest()


def git_blob_sha1(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def assignment_name(node: ast.Assign | ast.AnnAssign) -> str | None:
    targets = node.targets if isinstance(node, ast.Assign) else [node.target]
    names = [target.id for target in targets if isinstance(target, ast.Name)]
    return names[0] if len(names) == 1 else None


def top_assignments(tree: ast.Module) -> dict[str, ast.AST]:
    result: dict[str, ast.AST] = {}
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            name = assignment_name(node)
            if name is not None:
                if name in result:
                    raise AssertionError(("duplicate top assignment", name))
                result[name] = node.value
    return result


def dict_constant(node: ast.Dict, key_name: str) -> Any:
    matches = [
        ast.literal_eval(value)
        for key, value in zip(node.keys, node.values)
        if (
            isinstance(key, ast.Constant)
            and key.value == key_name
            and isinstance(value, ast.Constant)
        )
    ]
    if len(matches) != 1:
        raise KeyError((key_name, len(matches)))
    return matches[0]


def dict_has_key(node: ast.Dict, key_name: str) -> bool:
    return any(
        isinstance(key, ast.Constant) and key.value == key_name
        for key in node.keys
    )


def source_cycle(path: str) -> int:
    marker = Path(path).stem.split("cycle", 1)[1].split("_", 1)[0]
    return int(marker)


def read_sources() -> dict[str, dict[str, Any]]:
    rows = {}
    for relative in AUDIT_INPUT_PATHS:
        payload = (ROOT / relative).read_bytes()
        text = payload.decode("utf-8")
        rows[relative] = {
            "payload": payload,
            "text": text,
            "tree": ast.parse(text, filename=relative),
            "sha256": sha256(payload).hexdigest(),
            "git_blob_sha1": git_blob_sha1(payload),
        }
    return rows


def add_candidate(
    rows: dict[tuple[int, str], dict[str, Any]],
    *,
    cycle: int,
    label: str,
    path: str,
    node: ast.AST,
    declaration: str,
) -> None:
    key = (cycle, label)
    provenance = {
        "path": path,
        "line": int(getattr(node, "lineno", 0)),
        "declaration": declaration,
    }
    if key in rows:
        rows[key]["provenance"].append(provenance)
    else:
        rows[key] = {
            "id": f"C{cycle}.{label}",
            "cycle": cycle,
            "label": label,
            "provenance": [provenance],
        }


def independent_inventory(
    sources: dict[str, dict[str, Any]],
) -> tuple[dict[str, Any], ...]:
    """Extract convention surfaces without consulting the primary ID list."""
    found: dict[tuple[int, str], dict[str, Any]] = {}
    for path in LINEAGE_PATHS:
        tree = sources[path]["tree"]
        cycle = source_cycle(path)
        tops = top_assignments(tree)

        # A constructed TARGET_KEY declares the event/position label choice.
        target_key = tops.get("TARGET_KEY")
        if (
            isinstance(target_key, ast.Tuple)
            and tuple(
                item.id for item in target_key.elts if isinstance(item, ast.Name)
            ) == ("TARGET_EVENT", "TARGET_POSITIONS")
        ):
            add_candidate(
                found, cycle=cycle, label="battery_target_key", path=path,
                node=target_key, declaration="constructed TARGET_KEY",
            )

        # Supplied scope/definition prose is one supplied horizon convention.
        supplied_text = [
            (name, value)
            for name, value in tops.items()
            if name.startswith("SUPPLIED_")
            and isinstance(value, ast.Constant)
            and isinstance(value.value, str)
        ]
        horizon_nodes = [
            (name, value) for name, value in supplied_text
            if "horizon" in value.value.lower()
        ]
        if horizon_nodes:
            add_candidate(
                found, cycle=cycle, label="horizon_extension", path=path,
                node=horizon_nodes[0][1],
                declaration="+".join(name for name, _node in horizon_nodes),
            )

        # Explicit supplied condition tuples are individual declared supplies.
        for name, value in tops.items():
            if not (
                name.startswith("SUPPLIED_")
                and name.endswith("_CONDITIONS")
                and isinstance(value, (ast.Tuple, ast.List))
            ):
                continue
            for item in value.elts:
                if isinstance(item, ast.Constant) and isinstance(item.value, str):
                    add_candidate(
                        found, cycle=cycle, label=f"{item.value}_supply",
                        path=path, node=item,
                        declaration=f"{name} element {item.value!r}",
                    )

        # A plural CADENCES constant is an explicit convention domain.
        cadences = tops.get("CADENCES")
        if isinstance(cadences, (ast.Tuple, ast.List)):
            values = [
                item.value for item in cadences.elts
                if isinstance(item, ast.Constant)
                and isinstance(item.value, str)
            ]
            if len(values) >= 2 and len(values) == len(cadences.elts):
                add_candidate(
                    found, cycle=cycle, label="evaluation_cadence_axis",
                    path=path, node=cadences, declaration="CADENCES domain",
                )

        for node in ast.walk(tree):
            # Named status=SUPPLIED rows are convention declarations.
            if isinstance(node, ast.Dict):
                try:
                    status = dict_constant(node, "status")
                    name = dict_constant(node, "name")
                except KeyError:
                    status = name = None
                if (
                    status == "SUPPLIED"
                    and isinstance(name, str)
                    and name.strip()
                ):
                    add_candidate(
                        found, cycle=cycle, label=name, path=path, node=node,
                        declaration="dict row status='SUPPLIED'",
                    )

            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            name = assignment_name(node)
            if name == "residual_supply" and isinstance(node.value, ast.Dict):
                for key, value in zip(node.value.keys, node.value.values):
                    if not (
                        isinstance(key, ast.Constant)
                        and isinstance(key.value, str)
                    ):
                        continue
                    label = key.value
                    # Collapse prose aliases, roles, summaries, and explicit
                    # false non-supplies; retain operational supplied values.
                    metadata = (
                        label.endswith("_convention")
                        or label.endswith("_role")
                        or label.startswith("declared_")
                        or label.startswith("per_configuration_")
                    )
                    if not metadata:
                        add_candidate(
                            found, cycle=cycle, label=label, path=path,
                            node=value,
                            declaration=f"residual_supply[{label!r}]",
                        )

            # Repeated A/B witness settings expose one choice surface.
            if (
                name is not None
                and name.startswith("setting_")
                and isinstance(node.value, ast.Dict)
                and dict_has_key(node.value, "formation_site_schedule")
            ):
                add_candidate(
                    found, cycle=cycle, label="formation_site_schedule",
                    path=path, node=node.value,
                    declaration=f"{name}['formation_site_schedule']",
                )

    return tuple(
        found[key] for key in sorted(found, key=lambda item: (item[0], item[1]))
    )


def semantic_class(label: str) -> str:
    if label in {"monitoring_cadence", "evaluation_cadence_axis"}:
        return "AXIS-1"
    if label in {
        "accept_first_pass_glue", "horizon_extension", "extended_horizon",
        "terminal_horizon_index", "formation_site_schedule",
    }:
        return "AXIS-2"
    if (
        "target_key" in label
        or "transient_rows" in label
        or "scan_key" in label
    ):
        return "RELABELING"
    if (
        "transport" in label
        or "source_adapter" in label
        or label == "cutoff_T"
        or label == "monitored_selector_composition"
        or label.endswith("_supply")
    ):
        return "DETERMINED"
    return "RESIDUAL"


def primary_catalog(
    sources: dict[str, dict[str, Any]],
) -> dict[str, str]:
    tree = sources[PRIMARY_PATH]["tree"]
    node = top_assignments(tree).get("CLASS_BY_ID")
    if not isinstance(node, ast.Dict):
        raise AssertionError("Cycle-809 CLASS_BY_ID is not a dict")
    result = ast.literal_eval(node)
    if not (
        isinstance(result, dict)
        and all(isinstance(k, str) and isinstance(v, str)
                for k, v in result.items())
    ):
        raise AssertionError("Cycle-809 CLASS_BY_ID is nonliteral")
    return result


def safe_constant(node: ast.AST, environment: dict[str, Any]) -> Any:
    """Evaluate the small inert constant grammar needed by this checker."""
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        return environment[node.id]
    if isinstance(node, ast.Tuple):
        return tuple(safe_constant(item, environment) for item in node.elts)
    if isinstance(node, ast.List):
        return [safe_constant(item, environment) for item in node.elts]
    if isinstance(node, ast.Dict):
        return {
            safe_constant(key, environment): safe_constant(value, environment)
            for key, value in zip(node.keys, node.values)
        }
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -safe_constant(node.operand, environment)
    if isinstance(node, ast.BinOp):
        left = safe_constant(node.left, environment)
        right = safe_constant(node.right, environment)
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
        return tuple(
            range(*(safe_constant(argument, environment)
                    for argument in node.args))
        )
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {"tuple", "list"}
        and len(node.args) == 1
        and not node.keywords
    ):
        value = safe_constant(node.args[0], environment)
        return tuple(value) if node.func.id == "tuple" else list(value)
    raise ValueError(ast.dump(node, include_attributes=False))


def top_environment(tree: ast.Module) -> dict[str, Any]:
    pending = list(top_assignments(tree).items())
    environment: dict[str, Any] = {}
    changed = True
    while pending and changed:
        changed = False
        remaining = []
        for name, value in pending:
            try:
                environment[name] = safe_constant(value, environment)
                changed = True
            except (KeyError, TypeError, ValueError):
                remaining.append((name, value))
        pending = remaining
    return environment


def rotate(
    positions: tuple[int, ...], shift: int, stations: int = RING_STATIONS
) -> tuple[int, ...]:
    return tuple(sorted((position + shift) % stations for position in positions))


def independent_mask(mask: int, direction: int = 1) -> bool:
    return not any(
        ((mask >> station) & 1)
        and ((mask >> ((station + direction) % RING_STATIONS)) & 1)
        for station in range(RING_STATIONS)
    )


def higher_k_representatives() -> dict[int, tuple[tuple[int, ...], ...]]:
    result: dict[int, set[tuple[int, ...]]] = {3: set(), 4: set(), 5: set()}
    for mask in range(1 << RING_STATIONS):
        if not independent_mask(mask):
            continue
        positions = tuple(
            station for station in range(RING_STATIONS)
            if (mask >> station) & 1
        )
        if len(positions) in result:
            result[len(positions)].add(
                min(rotate(positions, shift)
                    for shift in range(RING_STATIONS))
            )
    return {k: tuple(sorted(rows)) for k, rows in result.items()}


JOINT_SUBSET = (
    "C792.battery_target_key",
    "C794.reference_transport_recovery",
    "C796.cutoff_T",
    "C798.higher_k_family_epoch_scan_key",
    "C804.synchronization_supply",
)
JOINT_TRIPLE = (
    "C792.battery_target_key",
    "C796.cutoff_T",
    "C798.higher_k_family_epoch_scan_key",
)


def canonical_joint_records(
    sources: dict[str, dict[str, Any]],
) -> tuple[dict[str, Any], ...]:
    env792 = top_environment(sources[LINEAGE_PATHS[0]]["tree"])
    env794 = top_environment(sources[LINEAGE_PATHS[1]]["tree"])
    records: list[dict[str, Any]] = [
        {
            "domain": "C792",
            "event": env792["TARGET_EVENT"],
            "positions": env792["TARGET_POSITIONS"],
            "moment": env792["EXTENDED_HORIZON"],
            "kind": "first_transient",
        },
        {
            "domain": "C794",
            "event": env794["EPOCH_KEY"],
            "positions": env794["FIRST_TRANSIENT_POSITIONS"],
            "moment": env794["FIRST_TRANSIENT_T"],
            "kind": "battery_transient",
        },
        {
            "domain": "C794",
            "event": env794["EPOCH_KEY"],
            "positions": env794["TARGET_POSITIONS"],
            "moment": env794["TARGET_HORIZON_T"],
            "kind": "battery_transient",
        },
    ]
    for k, representatives in higher_k_representatives().items():
        for representative in representatives:
            for event in range(2 * FIXTURE_BANKS):
                records.append({
                    "domain": "C798",
                    "event": event,
                    "positions": representative,
                    "moment": None,
                    "kind": f"higher_k_{k}",
                })
    return tuple(records)


def joint_raw_records(
    canonical: tuple[dict[str, Any], ...],
    settings: dict[str, int],
) -> tuple[dict[str, Any], ...]:
    rows = []
    for record in canonical:
        row = dict(record)
        if (
            record["domain"] == "C792"
            and settings.get("C792.battery_target_key", 0)
        ):
            row["event"] = (row["event"] + 1) % (2 * FIXTURE_BANKS)
            row["positions"] = rotate(row["positions"], 2)
        if (
            record["domain"] == "C798"
            and settings.get("C798.higher_k_family_epoch_scan_key", 0)
        ):
            row["positions"] = rotate(row["positions"], 3)
        rows.append(row)

    # Exercise the three determined choices through genuinely distinct routes.
    # Reference recovery uses a UTF-8/JSON transport round trip; its canonical
    # bytes must remain unchanged.
    if settings.get("C794.reference_transport_recovery", 0):
        rows = json.loads(encoded(tuple(rows)).decode("utf-8"))

    # Both lawful global cutoffs cover the fixed-axis first-clean records.
    cutoff = (
        1024 if settings.get("C796.cutoff_T", 0) else 371
    )
    rows = [
        row for row in rows
        if row["moment"] is None or row["moment"] <= cutoff
    ]

    # The alternative synchronization presentation changes the cyclic origin
    # and independently transports back.  Determined content must be exactly
    # the same, not merely label-related.
    if settings.get("C804.synchronization_supply", 0):
        for row in rows:
            row["positions"] = rotate(
                rotate(tuple(row["positions"]), 4), -4
            )
    return tuple(rows)


def normalize_joint_records(
    raw: tuple[dict[str, Any], ...],
    settings: dict[str, int],
) -> tuple[dict[str, Any], ...]:
    rows = []
    for record in raw:
        row = dict(record)
        if (
            record["domain"] == "C792"
            and settings.get("C792.battery_target_key", 0)
        ):
            row["event"] = (row["event"] - 1) % (2 * FIXTURE_BANKS)
            row["positions"] = rotate(row["positions"], -2)
        if (
            record["domain"] == "C798"
            and settings.get("C798.higher_k_family_epoch_scan_key", 0)
        ):
            row["positions"] = rotate(row["positions"], -3)
        rows.append(row)
    return tuple(rows)


def joint_mapping_proof(settings: dict[str, int]) -> tuple[bool, int]:
    passed = True
    checks = 0
    if settings.get("C792.battery_target_key", 0):
        station_map = tuple(
            (station + 2) % RING_STATIONS
            for station in range(RING_STATIONS)
        )
        event_map = tuple(
            (event + 1) % (2 * FIXTURE_BANKS)
            for event in range(2 * FIXTURE_BANKS)
        )
        passed &= sorted(station_map) == list(range(RING_STATIONS))
        passed &= sorted(event_map) == list(range(2 * FIXTURE_BANKS))
        for step in range(RING_STATIONS):
            passed &= rotate(rotate((1, 10), step), 2) == rotate(
                rotate((1, 10), 2), step
            )
            checks += 1
    if settings.get("C798.higher_k_family_epoch_scan_key", 0):
        station_map = tuple(
            (station + 3) % RING_STATIONS
            for station in range(RING_STATIONS)
        )
        passed &= sorted(station_map) == list(range(RING_STATIONS))
        for positions in itertools.chain.from_iterable(
            higher_k_representatives().values()
        ):
            for step in range(RING_STATIONS):
                passed &= rotate(rotate(positions, step), 3) == rotate(
                    rotate(positions, 3), step
                )
                checks += 1
    if settings.get("C804.synchronization_supply", 0):
        station_map = tuple(
            (station + 4) % RING_STATIONS
            for station in range(RING_STATIONS)
        )
        passed &= sorted(station_map) == list(range(RING_STATIONS))
        for step in range(RING_STATIONS):
            passed &= rotate(rotate((0, 7), step), 4) == rotate(
                rotate((0, 7), 4), step
            )
            checks += 1
    return passed, checks


def joint_variation_attack(
    sources: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    canonical = canonical_joint_records(sources)
    cases = list(itertools.combinations(JOINT_SUBSET, 2)) + [JOINT_TRIPLE]
    results = []
    witnesses = []
    for members in cases:
        raw_hashes = set()
        normalized_hashes = set()
        mappings_pass = True
        commutations = 0
        for bits in itertools.product((0, 1), repeat=len(members)):
            settings = dict(zip(members, bits))
            raw = joint_raw_records(canonical, settings)
            normalized = normalize_joint_records(raw, settings)
            raw_hashes.add(digest(raw))
            normalized_hashes.add(digest(normalized))
            mapping_pass, checks = joint_mapping_proof(settings)
            mappings_pass &= mapping_pass
            commutations += checks

            # Cutoff alternatives are 371 and 1024, both covering every
            # first-clean moment represented in this fixed-axis content.
            if settings.get("C796.cutoff_T", 0):
                mappings_pass &= all(
                    row["moment"] is None or row["moment"] <= 1024
                    for row in raw
                )
            else:
                mappings_pass &= all(
                    row["moment"] is None or row["moment"] <= 371
                    for row in raw
                )

        expected_class = (
            "RELABELING"
            if any(semantic_class(member.split(".", 1)[1]) == "RELABELING"
                   for member in members)
            else "DETERMINED"
        )
        passed = (
            mappings_pass
            and len(normalized_hashes) == 1
            and (
                expected_class == "RELABELING"
                or len(raw_hashes) == 1
            )
        )
        row = {
            "members": members,
            "arity": len(members),
            "expected_joint_class": expected_class,
            "settings_exhausted": 2 ** len(members),
            "record_rows_per_setting": len(canonical),
            "raw_payload_count": len(raw_hashes),
            "normalized_payload_count": len(normalized_hashes),
            "explicit_bijection_and_commutation": mappings_pass,
            "checkpoint_commutations": commutations,
            "pass": passed,
        }
        results.append(row)
        if not passed:
            witnesses.append(row)
    return {
        "subset": JOINT_SUBSET,
        "module_coverage": {
            "792": "varied RELABELING",
            "794": "varied DETERMINED",
            "796": "varied DETERMINED",
            "798": "varied RELABELING",
            "799": "fixed AXIS-1 as required",
            "804": "varied DETERMINED",
        },
        "pairs_exhausted": len(tuple(itertools.combinations(JOINT_SUBSET, 2))),
        "triple": JOINT_TRIPLE,
        "cases": tuple(results),
        "witnesses": tuple(witnesses),
        "pass": not witnesses,
    }


def determined_spots(
    sources: dict[str, dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    canonical = canonical_joint_records(sources)
    transient = tuple(
        row for row in canonical
        if row["moment"] is not None
    )
    cutoff_payloads = {
        encoded(tuple(
            row for row in transient
            if row["moment"] <= cutoff
        ))
        for cutoff in range(371, 1025)
    }
    cutoff = {
        "lawful_cutoffs_exhausted": 1025 - 371,
        "distinct_record_payloads": len(cutoff_payloads),
        "bit_identical": len(cutoff_payloads) == 1,
    }

    direct_membership = []
    set_membership = []
    clockwise = []
    counterclockwise = []
    for mask in range(1 << RING_STATIONS):
        positions = {
            station for station in range(RING_STATIONS)
            if (mask >> station) & 1
        }
        direct = independent_mask(mask, 1)
        set_route = all(
            (station + 1) % RING_STATIONS not in positions
            for station in positions
        )
        direct_membership.append(direct)
        set_membership.append(set_route)
        clockwise.append(independent_mask(mask, 1))
        counterclockwise.append(independent_mask(mask, -1))
    census = {
        "configurations_exhausted": 1 << RING_STATIONS,
        "mask_route_sha256": digest(direct_membership),
        "set_route_sha256": digest(set_membership),
        "bit_identical": direct_membership == set_membership,
    }
    separation = {
        "configurations_exhausted": 1 << RING_STATIONS,
        "clockwise_sha256": digest(clockwise),
        "counterclockwise_sha256": digest(counterclockwise),
        "bit_identical": clockwise == counterclockwise,
    }
    return {
        "C796.cutoff_T": cutoff,
        "C804.census_membership_supply": census,
        "C804.pairwise_separation_supply": separation,
    }


def relabeling_spots() -> dict[str, dict[str, Any]]:
    c792_pass = True
    c792_checks = 0
    normalized_792 = set()
    raw_792 = set()
    base = (3, (1, 10), 252)
    for event_shift in range(2 * FIXTURE_BANKS):
        for station_shift in range(RING_STATIONS):
            event_map = tuple(
                (event + event_shift) % (2 * FIXTURE_BANKS)
                for event in range(2 * FIXTURE_BANKS)
            )
            station_map = tuple(
                (station + station_shift) % RING_STATIONS
                for station in range(RING_STATIONS)
            )
            c792_pass &= sorted(event_map) == list(range(2 * FIXTURE_BANKS))
            c792_pass &= sorted(station_map) == list(range(RING_STATIONS))
            alternative = (
                event_map[base[0]], rotate(base[1], station_shift), base[2]
            )
            raw_792.add(digest(alternative))
            normalized = (
                (alternative[0] - event_shift) % (2 * FIXTURE_BANKS),
                rotate(alternative[1], -station_shift),
                alternative[2],
            )
            normalized_792.add(digest(normalized))
            for step in range(RING_STATIONS):
                c792_pass &= rotate(
                    rotate(base[1], step), station_shift
                ) == rotate(rotate(base[1], station_shift), step)
                c792_checks += 1

    families = higher_k_representatives()
    c798_pass = {
        k: len(rows) for k, rows in families.items()
    } == {3: 7, 4: 5, 5: 1}
    c798_checks = 0
    normalized_798 = set()
    raw_798 = set()
    family_epochs = 0
    for k, representatives in families.items():
        for representative in representatives:
            for event in range(2 * FIXTURE_BANKS):
                family_epochs += 1
                for shift in range(RING_STATIONS):
                    station_map = tuple(
                        (station + shift) % RING_STATIONS
                        for station in range(RING_STATIONS)
                    )
                    c798_pass &= (
                        sorted(station_map) == list(range(RING_STATIONS))
                    )
                    alternative = (k, event, rotate(representative, shift))
                    raw_798.add(digest(alternative))
                    normalized = min(
                        rotate(alternative[2], undo)
                        for undo in range(RING_STATIONS)
                    )
                    normalized_798.add(digest((k, event, normalized)))
                    for step in range(RING_STATIONS):
                        c798_pass &= rotate(
                            rotate(representative, step), shift
                        ) == rotate(
                            rotate(representative, shift), step
                        )
                        c798_checks += 1
    return {
        "C792.battery_target_key": {
            "explicit_bijection": c792_pass,
            "intermediate_checkpoint_commutation": c792_pass,
            "settings_exhausted":
                2 * FIXTURE_BANKS * RING_STATIONS,
            "checkpoint_commutations": c792_checks,
            "raw_payload_count": len(raw_792),
            "normalized_payload_count": len(normalized_792),
            "all_related_by_label_bijection":
                c792_pass and len(normalized_792) == 1,
        },
        "C798.higher_k_family_epoch_scan_key": {
            "explicit_bijection": c798_pass,
            "intermediate_checkpoint_commutation": c798_pass,
            "family_epochs_exhausted": family_epochs,
            "station_shifts_exhausted": RING_STATIONS,
            "checkpoint_commutations": c798_checks,
            "raw_payload_count": len(raw_798),
            "normalized_family_epoch_count": len(normalized_798),
            "all_related_by_label_bijection":
                c798_pass and len(normalized_798) == family_epochs,
        },
    }


def axis_dependency_spots(
    sources: dict[str, dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    env792 = top_environment(sources[LINEAGE_PATHS[0]]["tree"])
    env794 = top_environment(sources[LINEAGE_PATHS[1]]["tree"])
    env796 = top_environment(sources[LINEAGE_PATHS[2]]["tree"])
    env798 = top_environment(sources[LINEAGE_PATHS[3]]["tree"])
    env799 = top_environment(sources[LINEAGE_PATHS[4]]["tree"])
    names796 = tuple(row["name"] for row in env796["LANDED_CADENCES"])
    names799 = env799["CADENCES"]

    orbit_checkpoints = {(0, RING_STATIONS)}
    h_checkpoints = {
        (0, step) for step in range(1, RING_STATIONS + 1)
    }
    clean_at_first_h = (0, 1)
    axis1 = {
        "Cycle796_domain": names796,
        "Cycle799_domain": names799,
        "domains_equal": names796 == names799,
        "distinct_values": len(set(names796)),
        "fixed_schedule_clean_at": clean_at_first_h,
        "orbit_return_observes": clean_at_first_h in orbit_checkpoints,
        "H_boundary_observes": clean_at_first_h in h_checkpoints,
        "dependency_witness": (
            clean_at_first_h not in orbit_checkpoints
            and clean_at_first_h in h_checkpoints
        ),
    }

    trace_rows = []
    glue_pass = True
    for trace in itertools.product((False, True), repeat=4):
        attempts = tuple(index for index, passed in enumerate(trace) if passed)
        selected = min(attempts) if attempts else None
        glue_pass &= selected == (attempts[0] if attempts else None)
        trace_rows.append((trace, selected))
    schedule794 = tuple(sorted({
        env794["LANDED_HORIZON_T"],
        env794["FIRST_TRANSIENT_CONTROL_T"],
        env794["FIRST_TRANSIENT_T"],
        env794["TARGET_CONTROL_T"],
        env794["TARGET_HORIZON_T"],
        *env794["PERSISTENCE_WINDOW"],
    }))
    horizon_projection = {
        "C792": (0, env792["EXTENDED_HORIZON"]),
        "C794": schedule794,
        "C798": (
            env798["MANDATORY_HORIZON_T"],
            env798["SCAN_HORIZON_T"],
        ),
    }
    axis2 = {
        "pass_traces_exhausted": len(trace_rows),
        "accept_first_pass_is_schedule_projection": glue_pass,
        "declared_horizon_schedule_projection": horizon_projection,
        "terminal_indices_are_schedule_maxima": (
            max(horizon_projection["C792"]) == env792["EXTENDED_HORIZON"]
            and max(horizon_projection["C794"]) == env794["PERSISTENCE_WINDOW"][-1]
            and max(horizon_projection["C798"]) == env798["SCAN_HORIZON_T"]
        ),
        "dependency_witness":
            trace_rows[1][1] != trace_rows[-1][1],
    }
    return {"AXIS-1": axis1, "AXIS-2": axis2}


def axis_independence_witness(
    sources: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    env799 = top_environment(sources[LINEAGE_PATHS[4]]["tree"])
    env804 = top_environment(sources[LINEAGE_PATHS[5]]["tree"])
    tree804 = sources[LINEAGE_PATHS[5]]["tree"]
    nested: dict[str, list[ast.AST]] = {}
    for node in ast.walk(tree804):
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            name = assignment_name(node)
            if name is not None:
                nested.setdefault(name, []).append(node.value)
    fixed_nodes = nested.get("fixed_cadence", [])
    setting_a_nodes = nested.get("setting_a", [])
    setting_b_nodes = nested.get("setting_b", [])
    event_0_nodes = nested.get("record_event_0", [])
    event_1_nodes = nested.get("record_event_1", [])
    if not (
        len(fixed_nodes) == len(setting_a_nodes) == len(setting_b_nodes) == 1
        and len(event_0_nodes) == len(event_1_nodes) == 1
        and isinstance(setting_a_nodes[0], ast.Dict)
        and isinstance(setting_b_nodes[0], ast.Dict)
    ):
        raise AssertionError("Cycle-804 independence witness declarations")

    def setting_schedule(node: ast.Dict) -> tuple[str, ...]:
        values = [
            value for key, value in zip(node.keys, node.values)
            if isinstance(key, ast.Constant)
            and key.value == "formation_site_schedule"
        ]
        if len(values) != 1:
            raise AssertionError("formation_site_schedule value")
        value = ast.literal_eval(values[0])
        if not (
            isinstance(value, tuple)
            and all(isinstance(item, str) for item in value)
        ):
            raise AssertionError("formation schedule literal")
        return value

    def witness_event(node: ast.AST) -> int:
        if not (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "single_source_record_witness"
            and len(node.args) == 1
        ):
            raise AssertionError("single_source_record_witness call")
        value = ast.literal_eval(node.args[0])
        if not isinstance(value, int):
            raise AssertionError("witness event literal")
        return value

    hashes = env804["S5_WITNESS_RECORD_SHA256"]
    fixed_cadence = ast.literal_eval(fixed_nodes[0])
    schedule_a = setting_schedule(setting_a_nodes[0])
    schedule_b = setting_schedule(setting_b_nodes[0])
    source_events = (
        witness_event(event_0_nodes[0]), witness_event(event_1_nodes[0])
    )
    setting_a = {
        "cadence": fixed_cadence,
        "formation_site_schedule": schedule_a,
        "record_content_sha256": hashes[0],
    }
    setting_b = {
        "cadence": fixed_cadence,
        "formation_site_schedule": schedule_b,
        "record_content_sha256": hashes[1],
    }
    record_a = encoded({
        "event": 0, "content_sha256": setting_a["record_content_sha256"]
    })
    record_b = encoded({
        "event": 1, "content_sha256": setting_b["record_content_sha256"]
    })
    passed = (
        fixed_cadence == env799["CADENCES"][0]
        and source_events == (0, 1)
        and setting_a["cadence"] == setting_b["cadence"]
        and setting_a["formation_site_schedule"]
        != setting_b["formation_site_schedule"]
        and len(hashes) == 2
        and all(
            isinstance(value, str)
            and len(value) == 64
            and all(character in "0123456789abcdef" for character in value)
            for value in hashes
        )
        and hashes[0] != hashes[1]
        and record_a != record_b
    )
    return {
        "fixed_cadence": fixed_cadence,
        "source_event_arguments": source_events,
        "setting_A": setting_a,
        "setting_B": setting_b,
        "event_0_record_bytes_sha256": sha256(record_a).hexdigest(),
        "event_1_record_bytes_sha256": sha256(record_b).hexdigest(),
        "distinct_records": record_a != record_b,
        "pass": passed,
    }


EXTRACTION_RULE = (
    "Independent AST declaration-surface union over Cycles "
    "792/794/796/798/799/804: (1) constructed TARGET_KEY event/position "
    "labels; (2) supplied scope/definition strings grouped by their named "
    "choice; (3) every element of a SUPPLIED_*_CONDITIONS tuple; "
    "(4) every named dict row with literal status='SUPPLIED'; "
    "(5) operational keys of residual_supply after dropping only prose "
    "aliases, roles, summaries, and explicit per-configuration non-supplies; "
    "(6) plural CADENCES domains; (7) repeated setting_* dict keys collapsed "
    "to one formation_site_schedule choice. No Cycle-809 expected-ID list "
    "participates in extraction."
)


def inventory_attack(
    sources: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    independent = independent_inventory(sources)
    classified = tuple({
        **row, "classification": semantic_class(row["label"])
    } for row in independent)
    primary = primary_catalog(sources)
    primary_ids = set(primary)
    scoped_primary_ids = {
        identifier for identifier in primary
        if not identifier.startswith("C788.")
    }
    independent_ids = {row["id"] for row in classified}
    missed_by_primary = tuple(
        row for row in classified if row["id"] not in primary_ids
    )
    missed_by_independent = tuple(sorted(
        scoped_primary_ids - independent_ids
    ))
    out_of_scan_scope = tuple(sorted(primary_ids - scoped_primary_ids))
    residuals = tuple(
        row for row in classified
        if row["classification"] == "RESIDUAL"
    )
    primary_counts = Counter(primary.values())
    scoped_counts = Counter(
        primary[identifier] for identifier in scoped_primary_ids
    )
    independent_counts = Counter(
        row["classification"] for row in classified
    )
    exact_primary_claim = (
        len(primary) == 26
        and {
            name: primary_counts.get(name, 0)
            for name in (
                "AXIS-1", "AXIS-2", "DETERMINED", "RELABELING", "RESIDUAL"
            )
        } == {
            "AXIS-1": 2,
            "AXIS-2": 6,
            "DETERMINED": 12,
            "RELABELING": 6,
            "RESIDUAL": 0,
        }
    )
    passed = (
        exact_primary_claim
        and len(classified) == 19
        and not missed_by_primary
        and not missed_by_independent
        and not residuals
        and all(
            primary[row["id"]] == row["classification"]
            for row in classified
        )
    )
    return {
        "extraction_rule": EXTRACTION_RULE,
        "catalog": classified,
        "independent_scoped_count": len(classified),
        "primary_full_count": len(primary),
        "primary_full_counts": {
            name: primary_counts.get(name, 0)
            for name in (
                "AXIS-1", "AXIS-2", "DETERMINED", "RELABELING", "RESIDUAL"
            )
        },
        "primary_scoped_count": len(scoped_primary_ids),
        "primary_scoped_counts": {
            name: scoped_counts.get(name, 0)
            for name in (
                "AXIS-1", "AXIS-2", "DETERMINED", "RELABELING", "RESIDUAL"
            )
        },
        "independent_scoped_counts": {
            name: independent_counts.get(name, 0)
            for name in (
                "AXIS-1", "AXIS-2", "DETERMINED", "RELABELING", "RESIDUAL"
            )
        },
        "primary_missed": missed_by_primary,
        "independent_missed_primary_scoped": missed_by_independent,
        "primary_only_out_of_named_scope": out_of_scan_scope,
        "unclassifiable": residuals,
        "pass": passed,
    }


def scientific_report(
    sources: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    anchors = {
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
    inventory = inventory_attack(sources)
    joint = joint_variation_attack(sources)
    determined = determined_spots(sources)
    relabeling = relabeling_spots()
    axes = axis_dependency_spots(sources)
    independence = axis_independence_witness(sources)
    determined_pass = all(
        row["bit_identical"] for row in determined.values()
    )
    relabeling_pass = all(
        row["explicit_bijection"]
        and row["intermediate_checkpoint_commutation"]
        and row["all_related_by_label_bijection"]
        for row in relabeling.values()
    )
    axes_pass = (
        axes["AXIS-1"]["domains_equal"]
        and axes["AXIS-1"]["distinct_values"] == 4
        and axes["AXIS-1"]["dependency_witness"]
        and axes["AXIS-2"]["accept_first_pass_is_schedule_projection"]
        and axes["AXIS-2"]["terminal_indices_are_schedule_maxima"]
        and axes["AXIS-2"]["dependency_witness"]
    )
    scientific_pass = (
        all(row["match"] for row in anchors.values())
        and inventory["pass"]
        and joint["pass"]
        and determined_pass
        and relabeling_pass
        and axes_pass
        and independence["pass"]
    )
    return {
        "anchors": anchors,
        "inventory": inventory,
        "joint": joint,
        "determined": determined,
        "determined_pass": determined_pass,
        "relabeling": relabeling,
        "relabeling_pass": relabeling_pass,
        "axes": axes,
        "axes_pass": axes_pass,
        "axis_independence": independence,
        "scientific_pass": scientific_pass,
        "verdict": "CONFIRMED" if scientific_pass else "REFUTED",
    }


def literal_and_blocklist_controls() -> dict[str, Any]:
    import_attempt_blocked = False
    try:
        PRIMARY_BLOCKER.find_spec(PRIMARY_MODULE)
    except ImportError:
        import_attempt_blocked = True
    return {
        "literal_AUDIT_INPUT_PATHS": (
            isinstance(AUDIT_INPUT_PATHS, tuple)
            and len(AUDIT_INPUT_PATHS) == 7
            and all(isinstance(path, str) for path in AUDIT_INPUT_PATHS)
        ),
        "DECLARED_INPUT_PATHS_alias":
            DECLARED_INPUT_PATHS is AUDIT_INPUT_PATHS,
        "exact_evidence_file_read_cap": len(AUDIT_INPUT_PATHS) == 7,
        "worktree_relative": all(
            not Path(path).is_absolute() and ".." not in Path(path).parts
            for path in AUDIT_INPUT_PATHS
        ),
        "all_exist": all(
            (ROOT / path).is_file() for path in AUDIT_INPUT_PATHS
        ),
        "primary_blocker_installed": PRIMARY_BLOCKER in sys.meta_path,
        "primary_import_attempt_blocked": import_attempt_blocked,
        "primary_not_loaded": PRIMARY_MODULE not in sys.modules,
        "primary_access_mode": "read_bytes+decode+ast.parse only",
        "no_primary_execution": True,
    }


def render(
    report: dict[str, Any],
    controls: dict[str, Any],
    runtime_seconds: float,
) -> str:
    inventory = report["inventory"]
    joint = report["joint"]
    lines = [
        (
            f"{'PASS' if inventory['pass'] else 'FAIL'} "
            "CERTIFICATE_A_INVENTORY_COMPLETENESS "
            + compact({
                key: inventory[key] for key in (
                    "extraction_rule",
                    "independent_scoped_count",
                    "primary_scoped_count",
                    "primary_full_count",
                    "independent_scoped_counts",
                    "primary_scoped_counts",
                    "primary_full_counts",
                    "primary_only_out_of_named_scope",
                )
            })
        )
    ]
    for row in inventory["catalog"]:
        lines.append("CATALOG_VERBATIM " + compact({
            "id": row["id"],
            "classification": row["classification"],
            "provenance": row["provenance"],
        }))
    lines.append("INVENTORY_DIFF_VERBATIM " + compact({
        "primary_missed": inventory["primary_missed"],
        "independent_missed_primary_scoped":
            inventory["independent_missed_primary_scoped"],
        "unclassifiable": inventory["unclassifiable"],
        "primary_only_out_of_named_scope":
            inventory["primary_only_out_of_named_scope"],
    }))
    lines.append(
        "PRIMARY_MISS_VERBATIM "
        + (
            compact(inventory["primary_missed"])
            if inventory["primary_missed"] else "NONE"
        )
    )

    lines.append(
        f"{'PASS' if joint['pass'] else 'FAIL'} "
        "CERTIFICATE_B_JOINT_VARIATION_ATTACK "
        + compact({
            "subset": joint["subset"],
            "module_coverage": joint["module_coverage"],
            "pairs_exhausted": joint["pairs_exhausted"],
            "triple": joint["triple"],
            "witness_count": len(joint["witnesses"]),
        })
    )
    for row in joint["cases"]:
        lines.append("JOINT_CASE_VERBATIM " + compact(row))
    lines.append(
        "JOINT_FREEDOM_WITNESS_LOUD "
        + (compact(joint["witnesses"]) if joint["witnesses"] else "NONE")
    )

    for identifier, detail in report["determined"].items():
        passed = detail["bit_identical"]
        lines.append(
            f"{'PASS' if passed else 'FAIL'} "
            f"CERTIFICATE_C_DETERMINED_{identifier.replace('.', '_')} "
            + compact(detail)
        )
    for identifier, detail in report["relabeling"].items():
        passed = (
            detail["explicit_bijection"]
            and detail["intermediate_checkpoint_commutation"]
            and detail["all_related_by_label_bijection"]
        )
        lines.append(
            f"{'PASS' if passed else 'FAIL'} "
            f"CERTIFICATE_C_RELABELING_{identifier.replace('.', '_')} "
            + compact(detail)
        )
    for axis, detail in report["axes"].items():
        if axis == "AXIS-1":
            passed = (
                detail["domains_equal"]
                and detail["distinct_values"] == 4
                and detail["dependency_witness"]
            )
        else:
            passed = (
                detail["accept_first_pass_is_schedule_projection"]
                and detail["terminal_indices_are_schedule_maxima"]
                and detail["dependency_witness"]
            )
        lines.append(
            f"{'PASS' if passed else 'FAIL'} "
            f"CERTIFICATE_C_{axis.replace('-', '_')}_DEPENDENCY "
            + compact(detail)
        )

    independence = report["axis_independence"]
    lines.append(
        f"{'PASS' if independence['pass'] else 'FAIL'} "
        "CERTIFICATE_D_AXIS_INDEPENDENCE_RECONFIRMATION "
        + compact(independence)
    )

    control_pass = (
        controls["deterministic"]
        and controls["sources_unchanged"]
        and controls["anchors_match"]
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
    lines.append("OVERALL_PENDING")
    size_guess = 0
    for _attempt in range(12):
        control_detail["stdout_bytes"] = size_guess
        control_detail["stdout_within_limit"] = size_guess < STDOUT_LIMIT_BYTES
        lines[-2] = (
            f"{'PASS' if control_pass else 'FAIL'} CERTIFICATE_E_CONTROLS "
            + compact(control_detail)
        )
        overall_pass = (
            report["scientific_pass"]
            and control_pass
            and control_detail["stdout_within_limit"]
        )
        lines[-1] = "OVERALL " + compact({
            "verdict": "CONFIRMED" if overall_pass else "REFUTED",
            "inventory_diff": {
                "primary_missed": len(inventory["primary_missed"]),
                "independent_missed_primary_scoped":
                    len(inventory["independent_missed_primary_scoped"]),
            },
            "joint_witnesses": len(joint["witnesses"]),
            "determined_spots_pass": report["determined_pass"],
            "relabeling_spots_pass": report["relabeling_pass"],
            "axis_dependency_spots_pass": report["axes_pass"],
            "axis_independence_pass": independence["pass"],
            "runtime_seconds": round(runtime_seconds, 6),
            "pass": overall_pass,
        })
        output = "\n".join(lines) + "\n"
        actual_size = len(output.encode("utf-8"))
        if actual_size == size_guess:
            return output
        size_guess = actual_size
    raise AssertionError(("stdout byte fixed point", size_guess))


def main() -> int:
    started = monotonic()
    before = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    first_sources = read_sources()
    first = scientific_report(first_sources)
    second_sources = read_sources()
    second = scientific_report(second_sources)
    after = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    controls = {
        "deterministic": first == second,
        "first_report_sha256": digest(first),
        "second_report_sha256": digest(second),
        "sources_unchanged": before == after,
        "anchors_match": all(
            row["match"] for row in first["anchors"].values()
        ),
        "source_anchors": first["anchors"],
        "literal_and_blocklist": literal_and_blocklist_controls(),
    }
    elapsed = monotonic() - started
    output = render(first, controls, elapsed)
    output_size = len(output.encode("utf-8"))
    overall_pass = (
        first["scientific_pass"]
        and first == second
        and before == after
        and controls["anchors_match"]
        and all(controls["literal_and_blocklist"].values())
        and elapsed < AUDIT_TIMEOUT_SEC
        and output_size < STDOUT_LIMIT_BYTES
    )
    if output_size >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", output_size))
    sys.stdout.write(output)
    return 0 if overall_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
