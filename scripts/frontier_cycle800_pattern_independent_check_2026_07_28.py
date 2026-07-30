#!/usr/bin/env python3
"""Independent adversarial checker for the Cycle-800 pattern claim.

Only the landed Cycle-719 controller core is executable science input.  The
Cycle-798 and Cycle-800 primaries are SHA-anchored, AST-parsed text and are
protected by a runtime import firewall.  Configuration families, controller
orbit expansion, gate semantics, inverse chains, selection batteries, and the
6x6 landed-cleanliness matrix are recounted here.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

BLOCKLIST_TEXT_PATHS = (
    "scripts/frontier_cycle798_higher_k_horizon_scan_2026_07_28.py",
    "scripts/frontier_cycle800_pattern_completion_2026_07_28.py",
)

import ast
from hashlib import sha1, sha256
import importlib.abc
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

BLOCKLISTED_MODULES = tuple(
    Path(relative).stem for relative in BLOCKLIST_TEXT_PATHS
)


class _BlocklistFinder(importlib.abc.MetaPathFinder):
    """Fail closed if a text-only primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


IMPORT_FIREWALL = _BlocklistFinder()
sys.meta_path.insert(0, IMPORT_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
WINDOW_OFFSETS = tuple(range(1, 7))
EXCLUSIONS = (
    "synchronous_composition",
    "token_rail_return",
    "literal_inverse",
    "clean_postimage",
)

# (label, k, zero-based event, family member/target, supplied horizon t)
TRANSIENTS = (
    ("K2_T252", 2, 3, (1, 10), 252),
    ("K2_T371", 2, 3, (0, 7), 371),
    ("K3_T444", 3, 2, (0, 2, 5), 444),
    ("K3_T532", 3, 3, (0, 2, 5), 532),
    ("K3_T681", 3, 1, (0, 2, 4), 681),
    ("K3_T1385", 3, 2, (0, 2, 4), 1385),
)
NEW_TEST_LABELS = ("K3_T532", "K3_T681", "K3_T1385")
IDENTITY_LABELS = ("K2_T252", "K2_T371", "K3_T444")

DETERMINISM_SLICE = (
    "K3_T1385",
    2,
    (0, 2, 4),
    (0, 443, 444, 531, 532, 680, 681, 1384, 1385, 1391),
)

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    BLOCKLIST_TEXT_PATHS[0]:
        "f6ec49636ecb7ec09808eed7d38f2085f6145cd383c306370502c547741942b1",
    BLOCKLIST_TEXT_PATHS[1]:
        "5f7f49963fc7a3dec787634a6bf772fb5e406d3bbe667073cf7ea3c636a25e23",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]:
        "c123b8d681c3d76fce08ef13d7673622deac64ad",
    BLOCKLIST_TEXT_PATHS[0]:
        "9de34ad5adcbf484d4f0c7e6aec13375ed465aab",
    BLOCKLIST_TEXT_PATHS[1]:
        "65e92205cbb8e79413f892f6debad37d0511f2a3",
}
EXPECTED_CONFIGURATION_COUNTS = {
    0: 1,
    1: 11,
    2: 44,
    3: 77,
    4: 55,
    5: 11,
}
EXPECTED_FAMILY_COUNTS = {0: 1, 1: 1, 2: 4, 3: 7, 4: 5, 5: 1}

CHECKS: dict[str, bool] = {}
FINDINGS: list[str] = []
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def check(
    label: str,
    condition: bool,
    detail: object,
    finding: str,
) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )
    if not passed:
        FINDINGS.append(finding)
        OUTPUT_LINES.append("REFUTES_PRIMARY FINDING_VERBATIM :: " + finding)
    return passed


def source_controls() -> dict[str, object]:
    self_path = Path(__file__)
    self_tree = ast.parse(
        self_path.read_text(encoding="utf-8"), filename=str(self_path)
    )
    assignments: dict[str, ast.AST] = {}
    direct_imports = []
    for node in self_tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif isinstance(node, ast.Import):
            direct_imports.extend(alias.name for alias in node.names)

    audit_node = assignments["AUDIT_INPUT_PATHS"]
    declared_node = assignments["DECLARED_INPUT_PATHS"]
    literal_inputs = (
        isinstance(audit_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        and isinstance(declared_node, ast.Name)
        and declared_node.id == "AUDIT_INPUT_PATHS"
    )

    rows = {}
    parsed_text_paths = []
    for relative in (*AUDIT_INPUT_PATHS, *BLOCKLIST_TEXT_PATHS):
        path = ROOT / relative
        payload = path.read_bytes() if path.is_file() else b""
        observed_sha = sha256(payload).hexdigest()
        observed_blob = git_blob_sha(payload)
        parsed = False
        if relative in BLOCKLIST_TEXT_PATHS and path.is_file():
            parsed = isinstance(
                ast.parse(payload.decode("utf-8"), filename=relative),
                ast.Module,
            )
            if parsed:
                parsed_text_paths.append(relative)
        rows[relative] = {
            "exists_on_disk": path.is_file(),
            "sha256": observed_sha,
            "expected_sha256": EXPECTED_SHA256[relative],
            "git_blob_sha1": observed_blob,
            "expected_git_blob_sha1": EXPECTED_GIT_BLOBS[relative],
            "anchor_match": (
                path.is_file()
                and observed_sha == EXPECTED_SHA256[relative]
                and observed_blob == EXPECTED_GIT_BLOBS[relative]
            ),
            "execution_mode": (
                "LANDED_IMPORT"
                if relative in AUDIT_INPUT_PATHS
                else "TEXT_ONLY_BLOCKLISTED_AST"
            ),
            "top_level_ast_parsed": (
                parsed if relative in BLOCKLIST_TEXT_PATHS else None
            ),
        }

    science_imports = tuple(
        name for name in direct_imports if name.startswith("frontier_cycle")
    )
    forbidden_dynamic_calls = tuple(
        ast.unparse(node)
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {"exec", "eval", "compile", "__import__"}
    )
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal_tuple": literal_inputs,
        "all_audit_inputs_existing_disk_paths": all(
            (ROOT / relative).is_file() for relative in AUDIT_INPUT_PATHS
        ),
        "direct_science_imports": science_imports,
        "direct_science_imports_exact": science_imports
        == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        ),
        "blocklist_text_paths": BLOCKLIST_TEXT_PATHS,
        "parsed_text_paths": tuple(parsed_text_paths),
        "blocked_runtime_modules": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(IMPORT_FIREWALL.hits),
        "forbidden_dynamic_calls": forbidden_dynamic_calls,
        "rows": rows,
    }
    result["pass"] = (
        literal_inputs
        and result["all_audit_inputs_existing_disk_paths"]
        and result["direct_science_imports_exact"]
        and result["parsed_text_paths"] == BLOCKLIST_TEXT_PATHS
        and not result["blocked_runtime_modules"]
        and not result["firewall_hits"]
        and not forbidden_dynamic_calls
        and all(row["anchor_match"] for row in rows.values())
    )
    return result


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def pairwise_separated(positions: tuple[int, ...]) -> bool:
    occupied = set(positions)
    return all(
        (position + 1) % RING_STATIONS not in occupied
        for position in occupied
    )


def independent_configuration_families() -> tuple[
    dict[int, tuple[tuple[int, ...], ...]],
    dict[int, dict[tuple[int, ...], tuple[tuple[int, ...], ...]]],
]:
    configurations: dict[int, list[tuple[int, ...]]] = {
        k: [] for k in range(6)
    }
    for mask in range(1 << RING_STATIONS):
        positions = tuple(
            station
            for station in range(RING_STATIONS)
            if (mask >> station) & 1
        )
        if pairwise_separated(positions):
            configurations[len(positions)].append(positions)

    frozen_configurations = {
        k: tuple(sorted(rows)) for k, rows in configurations.items()
    }
    families = {}
    for k, rows in frozen_configurations.items():
        grouped: dict[
            tuple[int, ...], set[tuple[int, ...]]
        ] = {}
        for positions in rows:
            representative = (
                min(
                    rotate_positions(positions, shift)
                    for shift in range(RING_STATIONS)
                )
                if positions
                else ()
            )
            grouped.setdefault(representative, set()).add(positions)
        families[k] = {
            representative: tuple(sorted(members))
            for representative, members in sorted(grouped.items())
        }
    return frozen_configurations, families


GateOp = tuple[str, tuple[int, ...]]
ConfigurationKey = tuple[int, tuple[int, ...]]


def bits_to_int(bits: tuple[int, ...]) -> int:
    result = 0
    for wire, value in enumerate(bits):
        result |= int(value) << wire
    return result


def int_to_bits(state: int, width: int) -> tuple[int, ...]:
    return tuple((state >> wire) & 1 for wire in range(width))


def gate_operations(gates: tuple[object, ...]) -> tuple[GateOp, ...]:
    operations = []
    for gate in gates:
        if gate.kind not in {"X", "CNOT", "TOF"}:
            raise AssertionError(("unknown landed gate", gate))
        operations.append((gate.kind, tuple(gate.wires)))
    return tuple(operations)


def independent_apply_word(state: int, operations: tuple[GateOp, ...]) -> int:
    """Independent integer implementation of landed X/CNOT/Toffoli gates."""

    output = state
    for kind, wires in operations:
        if kind == "X":
            output ^= 1 << wires[0]
        elif kind == "CNOT":
            output ^= ((output >> wires[0]) & 1) << wires[1]
        elif kind == "TOF":
            output ^= (
                ((output >> wires[0]) & (output >> wires[1])) & 1
            ) << wires[2]
        else:
            raise AssertionError(("unknown operation", kind, wires))
    return output


def independent_epoch_fixtures() -> tuple[
    tuple[int, tuple[int, int], tuple[object, ...], tuple[int, ...]],
    ...,
]:
    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = gate_operations(
        tuple(K.M.global_allocator_word(FIXTURE_BANKS))
    )
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        rows.append((event, direction, program, before))
        after_int = independent_apply_word(bits_to_int(before), allocator)
        state = int_to_bits(after_int, len(before))
    return tuple(rows)


def synchronous_orbit_word(
    program: tuple[object, ...],
    positions: tuple[int, ...],
) -> tuple[GateOp, ...]:
    """Independently expand all simultaneous Q layers of one closed orbit."""

    live = tuple(positions)
    gates = []
    for _step in range(len(program)):
        occupied = set(live)
        for station, row in enumerate(program):
            if station in occupied:
                gates.extend(K.mapped_macro(row))
        live = tuple(
            (position + 1) % len(program) for position in live
        )
    if tuple(sorted(live)) != tuple(sorted(positions)):
        raise AssertionError(("orbit failed to close", positions, live))
    return gate_operations(tuple(gates))


def expected_forward_trace(
    positions: tuple[int, ...],
    stations: int,
) -> tuple[tuple[tuple[int, ...], tuple[int, ...], int], ...]:
    return tuple(
        (
            tuple(
                sorted(
                    (position + step) % stations
                    for position in positions
                )
            ),
            tuple(
                sorted(
                    (position + step + 1) % stations
                    for position in positions
                )
            ),
            0,
        )
        for step in range(stations)
    )


def landed_residual_support(
    state: int,
    width: int,
) -> tuple[tuple[str, str, int], ...]:
    """Own exact projection of every register watched by Cycle 758."""

    bits = int_to_bits(state, width)
    banks, links = K.M.unpack_state(bits, FIXTURE_BANKS)
    residual = []
    if bits[K.R3.X.SOURCE_POINTER]:
        residual.append(("source", "SOURCE_POINTER", 0))
    registers = (
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
        *tuple(
            (f"FRESH_{index}", wire)
            for index, wire in enumerate(K.A.FRESH)
        ),
        *tuple(
            (f"ZERO_WORK_{index}", wire)
            for index, wire in enumerate(K.A.ZERO_WORK)
        ),
        ("TOKEN_OK", K.A.TOKEN_OK),
    )
    for bank_index, bank in enumerate(banks):
        for register, wire in registers:
            if bank[wire]:
                residual.append(("bank", register, bank_index))
    for link_index, link in enumerate(links):
        for wire, content in enumerate(link):
            if content:
                residual.append(("link", f"WIRE_{wire}", link_index))
    return tuple(residual)


def landed_clean_postimage(state: int, width: int) -> bool:
    return not landed_residual_support(state, width)


def battery_basis(
    families: dict[
        int, dict[tuple[int, ...], tuple[tuple[int, ...], ...]]
    ],
) -> tuple[
    dict[str, tuple[tuple[int, ...], ...]],
    tuple[tuple[int, ...], ...],
]:
    k2_representatives = tuple(families[2])
    k2_battery = tuple(
        sorted(
            set(k2_representatives)
            | {
                next(
                    row[3] for row in TRANSIENTS if row[0] == "K2_T252"
                ),
                next(
                    row[3] for row in TRANSIENTS if row[0] == "K2_T371"
                ),
            }
        )
    )
    batteries = {}
    for label, k, _event, target, _moment in TRANSIENTS:
        batteries[label] = (
            k2_battery if k == 2 else families[k][target]
        )
    return batteries, k2_battery


def snapshot_requests(
    batteries: dict[str, tuple[tuple[int, ...], ...]],
) -> dict[ConfigurationKey, set[int]]:
    requests: dict[ConfigurationKey, set[int]] = {}

    def need(
        event: int,
        positions: tuple[int, ...],
        horizon_t: int,
    ) -> None:
        requests.setdefault((event, positions), set()).add(horizon_t)

    all_moments = tuple(row[4] for row in TRANSIENTS)
    for label, _k, event, target, moment in TRANSIENTS:
        for positions in batteries[label]:
            need(event, positions, moment)
        need(event, target, moment - 1)
        for offset in WINDOW_OFFSETS:
            need(event, target, moment + offset)
        for other_moment in all_moments:
            need(event, target, other_moment)

    _label, event, positions, horizons = DETERMINISM_SLICE
    for horizon_t in horizons:
        need(event, positions, horizon_t)
    return requests


def state_sha(state: int, width: int) -> str:
    payload = state.to_bytes((width + 7) // 8, "little")
    return sha256(payload).hexdigest()


def build_trajectory(
    fixture: tuple[
        int, tuple[int, int], tuple[object, ...], tuple[int, ...]
    ],
    positions: tuple[int, ...],
    requested_horizons: set[int],
) -> dict[str, object]:
    event, direction, program, before = fixture
    width = len(before)
    initial = bits_to_int(before)
    operations = synchronous_orbit_word(program, positions)
    reverse_operations = tuple(reversed(operations))
    tokens = tuple(
        int(station in positions) for station in range(len(program))
    )
    blanks = (0,) * len(program)

    # Directly exercise the landed controller once.  Its Q-layer expansion is
    # data-independent; agreement therefore certifies the cached orbit map.
    direct, rail_a, rail_b, trace = K.run_orbit(
        before, program, token_positions=positions
    )
    expanded_once = independent_apply_word(initial, operations)
    restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
        direct, program, token_positions=positions, reverse=True
    )
    operator_certificate = {
        "direct_controller_equals_independent_orbit_word":
            bits_to_int(direct) == expanded_once,
        "forward_trace_exact":
            trace == expected_forward_trace(positions, len(program)),
        "token_rail_return": rail_a == tokens and rail_b == blanks,
        "direct_literal_inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "gate_count": len(operations),
        "orbit_word_sha256": digest(operations),
    }

    state = initial
    snapshots: dict[int, int] = {}
    max_horizon = max(requested_horizons)
    trace_hash = sha256()
    for horizon_t in range(max_horizon + 1):
        state = independent_apply_word(state, operations)
        if horizon_t in requested_horizons:
            snapshots[horizon_t] = state
            trace_hash.update(horizon_t.to_bytes(4, "little"))
            trace_hash.update(
                bytes.fromhex(state_sha(state, width))
            )

    # One reverse pass checks the exact inverse chain at every cached sample
    # and returns all the way to the event fixture.  This is O(max horizon),
    # rather than separately replaying each overlapping prefix.
    inverse_state = state
    sampled_inverse_matches = {}
    for horizon_t in reversed(range(max_horizon + 1)):
        if horizon_t in requested_horizons:
            sampled_inverse_matches[horizon_t] = (
                inverse_state == snapshots[horizon_t]
            )
        inverse_state = independent_apply_word(
            inverse_state, reverse_operations
        )
    inverse_chain_exact = (
        inverse_state == initial
        and all(sampled_inverse_matches.values())
        and set(sampled_inverse_matches) == requested_horizons
    )

    return {
        "event": event,
        "direction": direction,
        "positions": positions,
        "width": width,
        "requested_horizons": tuple(sorted(requested_horizons)),
        "max_horizon_t": max_horizon,
        "snapshots": snapshots,
        "operator_certificate": operator_certificate,
        "inverse_chain_exact": inverse_chain_exact,
        "snapshot_trace_sha256": trace_hash.hexdigest(),
    }


def evaluate_snapshot(
    trajectory: dict[str, object],
    horizon_t: int,
) -> dict[str, object]:
    state = trajectory["snapshots"][horizon_t]
    operator = trajectory["operator_certificate"]
    conditions = {
        "synchronous_composition": (
            operator[
                "direct_controller_equals_independent_orbit_word"
            ]
            and operator["forward_trace_exact"]
        ),
        "token_rail_return": operator["token_rail_return"],
        "literal_inverse": (
            operator["direct_literal_inverse"]
            and trajectory["inverse_chain_exact"]
        ),
        "clean_postimage": landed_clean_postimage(
            state, trajectory["width"]
        ),
    }
    failed = tuple(
        exclusion
        for exclusion in EXCLUSIONS
        if not conditions[exclusion]
    )
    return {
        "event": trajectory["event"],
        "positions": trajectory["positions"],
        "horizon_t_SUPPLIED": horizon_t,
        "complete_orbits_applied": horizon_t + 1,
        "conditions": conditions,
        "failed_exclusions": failed,
        "selected": not failed,
        "postimage_sha256": state_sha(state, trajectory["width"]),
    }


def exclusion_recount(
    rows: tuple[dict[str, object], ...],
) -> dict[str, dict[str, object]]:
    return {
        exclusion: {
            "pass_count": sum(
                row["conditions"][exclusion] for row in rows
            ),
            "fail_count": sum(
                not row["conditions"][exclusion] for row in rows
            ),
            "passing_positions": tuple(
                row["positions"]
                for row in rows
                if row["conditions"][exclusion]
            ),
            "failing_positions": tuple(
                row["positions"]
                for row in rows
                if not row["conditions"][exclusion]
            ),
        }
        for exclusion in EXCLUSIONS
    }


def recount_selection(
    transient: tuple[
        str, int, int, tuple[int, ...], int
    ],
    batteries: dict[str, tuple[tuple[int, ...], ...]],
    trajectories: dict[ConfigurationKey, dict[str, object]],
) -> dict[str, object]:
    label, k, event, target, moment = transient
    rows = tuple(
        evaluate_snapshot(trajectories[(event, positions)], moment)
        for positions in batteries[label]
    )
    survivors = tuple(
        row["positions"] for row in rows if row["selected"]
    )
    if target not in survivors:
        classification = "STILL_EXCLUDED"
    elif len(survivors) == 1:
        classification = "UNIQUE_SURVIVOR"
    else:
        classification = "TIE"
    veto = evaluate_snapshot(
        trajectories[(event, target)], moment - 1
    )
    window = tuple(
        evaluate_snapshot(
            trajectories[(event, target)], moment + offset
        )
        for offset in WINDOW_OFFSETS
    )
    return {
        "label": label,
        "k": k,
        "event": event,
        "target": target,
        "moment_SUPPLIED": moment,
        "battery_size": len(rows),
        "battery": batteries[label],
        "rows": rows,
        "survivors": survivors,
        "survivor_count": len(survivors),
        "classification": classification,
        "per_exclusion": exclusion_recount(rows),
        "moment_minus_one_veto": veto,
        "window_plus_1_through_6": window,
    }


def expected_exclusion_truth(
    selection: dict[str, object],
    exclusion: str,
) -> bool:
    row = selection["per_exclusion"][exclusion]
    battery_size = selection["battery_size"]
    if exclusion == "clean_postimage":
        return (
            row["pass_count"] == 1
            and row["fail_count"] == battery_size - 1
            and row["passing_positions"] == (selection["target"],)
        )
    return (
        row["pass_count"] == battery_size
        and row["fail_count"] == 0
        and not row["failing_positions"]
    )


def selection_attack_pass(selection: dict[str, object]) -> bool:
    veto = selection["moment_minus_one_veto"]
    window = selection["window_plus_1_through_6"]
    return (
        selection["classification"] == "UNIQUE_SURVIVOR"
        and selection["survivors"] == (selection["target"],)
        and all(
            expected_exclusion_truth(selection, exclusion)
            for exclusion in EXCLUSIONS
        )
        and not veto["selected"]
        and veto["failed_exclusions"] == ("clean_postimage",)
        and tuple(
            row["horizon_t_SUPPLIED"]
            - selection["moment_SUPPLIED"]
            for row in window
        )
        == WINDOW_OFFSETS
        and all(
            not row["selected"]
            and row["failed_exclusions"] == ("clean_postimage",)
            for row in window
        )
    )


def public_selection(selection: dict[str, object]) -> dict[str, object]:
    return {
        "label": selection["label"],
        "k": selection["k"],
        "event": selection["event"],
        "target": selection["target"],
        "moment_SUPPLIED": selection["moment_SUPPLIED"],
        "battery_size": selection["battery_size"],
        "battery": selection["battery"],
        "survivors": selection["survivors"],
        "survivor_count": selection["survivor_count"],
        "classification": selection["classification"],
        "per_exclusion": selection["per_exclusion"],
        "moment_minus_one_veto": selection["moment_minus_one_veto"],
        "window_plus_1_through_6": tuple(
            {
                "horizon_t_SUPPLIED": row["horizon_t_SUPPLIED"],
                "selected": row["selected"],
                "failed_exclusions": row["failed_exclusions"],
                "postimage_sha256": row["postimage_sha256"],
            }
            for row in selection["window_plus_1_through_6"]
        ),
        "battery_rows": tuple(
            {
                "positions": row["positions"],
                "selected": row["selected"],
                "failed_exclusions": row["failed_exclusions"],
                "postimage_sha256": row["postimage_sha256"],
            }
            for row in selection["rows"]
        ),
    }


def recount_simultaneity_matrix(
    trajectories: dict[ConfigurationKey, dict[str, object]],
) -> tuple[tuple[dict[str, object], ...], bool]:
    rows = []
    for row_label, _k, _event, _target, moment in TRANSIENTS:
        cells = []
        for (
            column_label,
            column_k,
            column_event,
            column_target,
            _column_moment,
        ) in TRANSIENTS:
            trajectory = trajectories[(column_event, column_target)]
            state = trajectory["snapshots"][moment]
            residual = landed_residual_support(
                state, trajectory["width"]
            )
            cells.append(
                {
                    "label": column_label,
                    "k": column_k,
                    "event": column_event,
                    "positions": column_target,
                    "clean": not residual,
                    "residual_weight": len(residual),
                }
            )
        rows.append(
            {
                "at_label": row_label,
                "moment_SUPPLIED": moment,
                "cells": tuple(cells),
            }
        )
    matrix = tuple(rows)
    exact_identity = (
        len(matrix) == 6
        and all(len(row["cells"]) == 6 for row in matrix)
        and all(
            cell["clean"] == (cell["label"] == row["at_label"])
            for row in matrix
            for cell in row["cells"]
        )
    )
    return matrix, exact_identity


def declared_slice_payload(
    trajectory: dict[str, object],
    horizons: tuple[int, ...],
) -> dict[str, object]:
    return {
        "event": trajectory["event"],
        "positions": trajectory["positions"],
        "horizons": horizons,
        "state_sha256": tuple(
            (
                horizon_t,
                state_sha(
                    trajectory["snapshots"][horizon_t],
                    trajectory["width"],
                ),
            )
            for horizon_t in horizons
        ),
        "operator_certificate": trajectory["operator_certificate"],
        "inverse_chain_exact": trajectory["inverse_chain_exact"],
    }


def main() -> int:
    started = monotonic()
    controls = source_controls()
    configurations, families = independent_configuration_families()
    batteries, k2_battery = battery_basis(families)
    requests = snapshot_requests(batteries)
    fixtures = independent_epoch_fixtures()
    fixture_by_event = {row[0]: row for row in fixtures}

    trajectories: dict[ConfigurationKey, dict[str, object]] = {}
    batch_timings = []
    for label, _k, event, _target, _moment in TRANSIENTS:
        batch_started = monotonic()
        built = []
        reused = []
        for positions in batteries[label]:
            key = (event, positions)
            if key in trajectories:
                reused.append(positions)
                continue
            trajectories[key] = build_trajectory(
                fixture_by_event[event],
                positions,
                requests[key],
            )
            built.append(positions)
        batch_timings.append(
            {
                "label": label,
                "built_trajectories": len(built),
                "reused_trajectories": len(reused),
                "built_positions": tuple(built),
                "reused_positions": tuple(reused),
                "seconds": round(monotonic() - batch_started, 6),
            }
        )

    missing_keys = tuple(
        sorted(set(requests) - set(trajectories))
    )
    if missing_keys:
        raise AssertionError(("unbuilt requested trajectories", missing_keys))

    selections = {
        row[0]: recount_selection(row, batteries, trajectories)
        for row in TRANSIENTS
    }
    matrix, matrix_exact_identity = recount_simultaneity_matrix(
        trajectories
    )

    OUTPUT_LINES.append(
        "AUDIT_INPUT_PATHS_LITERAL " + repr(AUDIT_INPUT_PATHS)
    )
    OUTPUT_LINES.append("SOURCE_CONTROLS " + compact(controls))
    OUTPUT_LINES.append(
        "CACHE_POLICY "
        + compact(
            {
                "method":
                    "one independently expanded reversible orbit word per "
                    "(event,positions), one forward trajectory, one reverse "
                    "chain, cached snapshots shared across battery/veto/"
                    "window/matrix tests",
                "soundness":
                    "the landed controller is directly exercised for one "
                    "complete orbit on every trajectory; the Q expansion is "
                    "data-independent and both rails close",
                "trajectory_count": len(trajectories),
                "requested_snapshot_count":
                    sum(len(rows) for rows in requests.values()),
            }
        )
    )
    for timing in batch_timings:
        OUTPUT_LINES.append("SELECTION_BATCH_TIMING " + compact(timing))
    OUTPUT_LINES.append(
        "CENSUS "
        + compact(
            {
                "configuration_counts": {
                    k: len(configurations[k]) for k in range(6)
                },
                "family_counts": {
                    k: len(families[k]) for k in range(6)
                },
                "k2_representatives": tuple(families[2]),
                "k2_battery": k2_battery,
            }
        )
    )
    for label, *_rest in TRANSIENTS:
        OUTPUT_LINES.append(
            "SELECTION_RECOUNT "
            + label
            + " "
            + compact(public_selection(selections[label]))
        )

    # Attack 1: all four exclusions receive a complete-family truth table,
    # then veto/uniqueness/window are checked as a separate aggregate.
    for label in NEW_TEST_LABELS:
        selection = selections[label]
        for exclusion in EXCLUSIONS:
            exclusion_label = exclusion.upper()
            check(
                f"CERTIFICATE_1_{label}_{exclusion_label}",
                expected_exclusion_truth(selection, exclusion),
                selection["per_exclusion"][exclusion],
                (
                    f"{label}_EXCLUSION_{exclusion_label}_MISMATCH: the "
                    f"complete battery truth table for {exclusion} does "
                    "not match a unique clean-only survivor."
                ),
            )
        check(
            f"CERTIFICATE_1_{label}_UNIQUE_VETO_CLEAN_WINDOW",
            selection_attack_pass(selection),
            {
                "moment_SUPPLIED": selection["moment_SUPPLIED"],
                "target": selection["target"],
                "classification": selection["classification"],
                "survivors": selection["survivors"],
                "moment_minus_one_selected":
                    selection["moment_minus_one_veto"]["selected"],
                "moment_minus_one_failed_exclusions":
                    selection["moment_minus_one_veto"][
                        "failed_exclusions"
                    ],
                "window": tuple(
                    (
                        row["horizon_t_SUPPLIED"],
                        row["selected"],
                        row["failed_exclusions"],
                    )
                    for row in selection["window_plus_1_through_6"]
                ),
            },
            (
                f"{label}_SELECTION_REFUTED: the target is not the unique "
                "survivor at its supplied moment, lacks the moment-1 veto, "
                "or reappears in the +1..+6 window."
            ),
        )

    # Attack 2: every cell is freshly projected through the landed residual
    # coordinates, including weights on all 30 off-diagonal cells.
    OUTPUT_LINES.append("SIMULTANEITY_MATRIX " + compact(matrix))
    matrix_shape = (
        len(matrix) == len(TRANSIENTS)
        and all(len(row["cells"]) == len(TRANSIENTS) for row in matrix)
    )
    diagonal_clean = all(
        next(
            cell
            for cell in row["cells"]
            if cell["label"] == row["at_label"]
        )["clean"]
        for row in matrix
    )
    off_diagonal_false = all(
        not cell["clean"]
        for row in matrix
        for cell in row["cells"]
        if cell["label"] != row["at_label"]
    )
    check(
        "CERTIFICATE_2_ALL_36_SIMULTANEITY_CELLS",
        (
            matrix_shape
            and diagonal_clean
            and off_diagonal_false
            and matrix_exact_identity
        ),
        {
            "matrix_shape_6x6": matrix_shape,
            "diagonal_clean": diagonal_clean,
            "all_30_off_diagonal_cells_false": off_diagonal_false,
            "boolean_rows": tuple(
                tuple(cell["clean"] for cell in row["cells"])
                for row in matrix
            ),
            "statement": (
                "ONE_AT_A_TIME_ACROSS_STRATA"
                if matrix_exact_identity
                else "SIMULTANEOUS_TRANSIENT_CLEANLINESS_FOUND"
            ),
        },
        (
            "SIMULTANEITY_MATRIX_REFUTED: the independently recounted 6x6 "
            "landed-cleanliness matrix is not clean on exactly its diagonal."
        ),
    )

    # Attack 3: the old 444 selection and both k=2 selections must survive
    # the same stronger uniqueness/veto/no-reappearance test.
    identity_rows = tuple(
        {
            "label": label,
            "moment_SUPPLIED": selections[label]["moment_SUPPLIED"],
            "battery_size": selections[label]["battery_size"],
            "classification": selections[label]["classification"],
            "survivors": selections[label]["survivors"],
            "veto_selected":
                selections[label]["moment_minus_one_veto"]["selected"],
            "window_selected": tuple(
                row["selected"]
                for row in selections[label][
                    "window_plus_1_through_6"
                ]
            ),
        }
        for label in IDENTITY_LABELS
    )
    configuration_counts = {
        k: len(configurations[k]) for k in range(6)
    }
    family_counts = {k: len(families[k]) for k in range(6)}
    identity_pass = (
        configuration_counts == EXPECTED_CONFIGURATION_COUNTS
        and family_counts == EXPECTED_FAMILY_COUNTS
        and tuple(families[2])
        == ((0, 2), (0, 3), (0, 4), (0, 5))
        and k2_battery
        == ((0, 2), (0, 3), (0, 4), (0, 5), (0, 7), (1, 10))
        and all(
            selection_attack_pass(selections[label])
            for label in IDENTITY_LABELS
        )
        and selections["K2_T252"]["battery_size"] == 6
        and selections["K2_T371"]["battery_size"] == 6
        and selections["K3_T444"]["battery_size"] == 11
    )
    check(
        "CERTIFICATE_3_IDENTITY_CONTROLS_T444_T252_T371",
        identity_pass,
        {
            "configuration_counts": configuration_counts,
            "family_counts": family_counts,
            "k2_battery": k2_battery,
            "identity_rows": identity_rows,
        },
        (
            "IDENTITY_CONTROLS_REFUTED: t=444 or the k=2 t=252/t=371 "
            "selection battery failed to reproduce uniquely with its veto "
            "and clean +1..+6 window."
        ),
    )

    all_unique = all(
        selection_attack_pass(selections[label])
        for label, *_rest in TRANSIENTS
    )
    pattern_verdict = (
        "SIX_FOR_SIX_UNIQUE" if all_unique else "DIVERGENT"
    )
    check(
        "CERTIFICATE_3_SIX_FOR_SIX_PATTERN_VERDICT",
        pattern_verdict == "SIX_FOR_SIX_UNIQUE",
        {
            "verdict": pattern_verdict,
            "classifications": tuple(
                (
                    label,
                    selections[label]["classification"],
                    selections[label]["survivors"],
                )
                for label, *_rest in TRANSIENTS
            ),
        },
        (
            "PATTERN_VERDICT_REFUTED: the independent batteries do not "
            "support SIX_FOR_SIX_UNIQUE."
        ),
    )

    # Attack 4: rerun one declared, scattered slice rather than doubling the
    # six heavy batteries.  It includes all three k=3 moments and the longest
    # target/window endpoint.
    _slice_label, slice_event, slice_positions, slice_horizons = (
        DETERMINISM_SLICE
    )
    first_slice = declared_slice_payload(
        trajectories[(slice_event, slice_positions)],
        slice_horizons,
    )
    second_slice_trajectory = build_trajectory(
        fixture_by_event[slice_event],
        slice_positions,
        set(slice_horizons),
    )
    second_slice = declared_slice_payload(
        second_slice_trajectory, slice_horizons
    )
    deterministic = first_slice == second_slice
    first_slice_sha = digest(first_slice)
    second_slice_sha = digest(second_slice)

    elapsed = monotonic() - started
    projected_stdout_bytes = (
        len("\n".join(OUTPUT_LINES).encode("utf-8")) + 24 * 1024
    )
    control_pass = (
        controls["pass"]
        and deterministic
        and first_slice_sha == second_slice_sha
        and elapsed < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < STDOUT_LIMIT_BYTES
    )
    check(
        "CERTIFICATE_4_SHA_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT",
        control_pass,
        {
            "source_controls_pass": controls["pass"],
            "blocked_runtime_modules":
                controls["blocked_runtime_modules"],
            "firewall_hits": controls["firewall_hits"],
            "determinism_slice": DETERMINISM_SLICE,
            "deterministic": deterministic,
            "first_slice_sha256": first_slice_sha,
            "second_slice_sha256": second_slice_sha,
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "projected_stdout_bytes": projected_stdout_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
        (
            "CONTROL_FAILURE: a SHA anchor, text-only import blocklist, "
            "declared-slice determinism check, runtime bound, or stdout "
            "bound failed."
        ),
    )

    passed = all(CHECKS.values()) and not FINDINGS
    OUTPUT_LINES.append("FINDINGS_VERBATIM " + compact(tuple(FINDINGS)))
    terminal = {
        "terminal": (
            "CYCLE800_PATTERN_INDEPENDENT_CHECK_PASS"
            if passed
            else "CYCLE800_PATTERN_INDEPENDENT_CHECK_REFUTES_PRIMARY"
        ),
        "pass": passed,
        "new_recounts": tuple(
            {
                "label": label,
                "moment_SUPPLIED": selections[label]["moment_SUPPLIED"],
                "survivors": selections[label]["survivors"],
                "veto": not selections[label][
                    "moment_minus_one_veto"
                ]["selected"],
                "window_reappearances": tuple(
                    row["horizon_t_SUPPLIED"]
                    for row in selections[label][
                        "window_plus_1_through_6"
                    ]
                    if row["selected"]
                ),
            }
            for label in NEW_TEST_LABELS
        ),
        "simultaneity_statement": (
            "ONE_AT_A_TIME_ACROSS_STRATA"
            if matrix_exact_identity
            else "SIMULTANEOUS_TRANSIENT_CLEANLINESS_FOUND"
        ),
        "pattern_verdict": pattern_verdict,
        "checks": dict(sorted(CHECKS.items())),
        "determinism_sha256": first_slice_sha,
        "runtime_seconds": round(elapsed, 6),
        "findings": tuple(FINDINGS),
    }
    output = (
        "\n".join(OUTPUT_LINES)
        + "\nFINAL "
        + compact(terminal)
        + "\n"
    )
    stdout_bytes = len(output.encode("utf-8"))
    if stdout_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", stdout_bytes, STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
