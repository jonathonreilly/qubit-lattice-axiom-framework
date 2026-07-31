#!/usr/bin/env python3
"""Cycle 831: deep k=2 continuation with standing forecasts on the line.

The Cycle-818/819/820/822 primaries are SHA-pinned text/AST-only controls and
are blocked from import.  This runner imports only the landed Cycle-719 core,
rebuilds the complete 176-key family, reproduces the Cycle-819 T=16384
population, and evolves its 151 open keys to the deepest complete admitted
power-of-two boundary.

The landed update is a composition of reversible X/CNOT/TOF gates.  Therefore
any repeated state on a trajectory must first return to its t=0 state: an
invertible map has no positive preperiod.  Exact bit-sliced equality to the
initial state at every moment consequently certifies recurrence and minimal
period without a probabilistic state token.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle818_period_structure_census_2026_07_28.py",
    "scripts/frontier_cycle819_deep_k2_continuation_2026_07_28.py",
    "scripts/frontier_cycle820_shared_moment_mechanism_2026_07_28.py",
    "scripts/frontier_cycle822_basin_independent_check_2026_07_28.py",
)

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "918ae9d1f5b29a4cee437dac8af4bfb27ee0aceee3a7abd0c6bdaaa6fb10d24c",
    AUDIT_INPUT_PATHS[2]:
        "e1c18187a4082fc534b9bd94055258a9aedc05c8dda37bb84f6a0d84592308fe",
    AUDIT_INPUT_PATHS[3]:
        "7344bee5d5f0bcbddcea7b9d83f40a552c90188bf30b4905f2649a49e4bf1649",
    AUDIT_INPUT_PATHS[4]:
        "c2fd23a7bb47caff70e9561fc9da46feef422c053954fa1af925901a1884ed0b",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "9c2657e5fa98c4d2bbb561a0f428cf59fca20973",
    AUDIT_INPUT_PATHS[2]: "c3a071835a61e78a4919decfede8534cbf95e1d9",
    AUDIT_INPUT_PATHS[3]: "6385dfa0dce58e86345483cc521ffa325e0d1cce",
    AUDIT_INPUT_PATHS[4]: "6d48f5d86006a5f6718b5993eaecd5ec69d86112",
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
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


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, tuple[int, int]]
Lane = tuple[Key, str]
MaskedGate = tuple[int, int, int, int, int]

RING_STATIONS = 11
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
BASELINE_HORIZON = 16384
MINIMUM_DEEP_HORIZON = 32768
TARGET_HORIZON = 65536
BOUNDARIES = (BASELINE_HORIZON, MINIMUM_DEEP_HORIZON, TARGET_HORIZON)
BUDGET_DECISION_LIMIT_SEC = 1450
BUDGET_SAFETY_FACTOR = 1.30
BUDGET_RESERVE_SEC = 75.0
DETERMINISM_SLICE_SIZE = 8
SSTAR_ENTRY = 14739
SSTAR_LAG = 5
NINE_SSTAR_KEYS: tuple[Key, ...] = (
    (0, (1, 6)),
    (0, (1, 7)),
    (0, (2, 7)),
    (0, (2, 8)),
    (0, (3, 8)),
    (0, (3, 9)),
    (0, (4, 9)),
    (0, (4, 10)),
    (0, (5, 10)),
)
EXPECTED_CONTROL_TRANSIENTS = {
    (3, (1, 10)): 252,
    (3, (0, 7)): 371,
}
EXPECTED_OLD_CYCLES = {
    (3, (0, 5)): 2,
    (3, (0, 6)): 2,
    (3, (1, 6)): 3,
    (3, (1, 7)): 3,
    (3, (2, 7)): 3,
    (3, (2, 8)): 3,
    (3, (3, 8)): 3,
    (3, (3, 9)): 3,
    (3, (4, 9)): 3,
    (3, (4, 10)): 3,
    (3, (5, 10)): 3,
    (2, (0, 9)): 288,
}
EXPECTED_LATE_CYCLES = {
    (1, (0, 9)): 8928,
    (0, (0, 9)): 8930,
}
EXPECTED_RESOLVED_THROUGH_819 = frozenset(
    set(EXPECTED_CONTROL_TRANSIENTS)
    | set(EXPECTED_OLD_CYCLES)
    | set(EXPECTED_LATE_CYCLES)
    | set(NINE_SSTAR_KEYS)
)
PERIOD_LAW_ROWS = (
    (0, False, 8930),
    (0, True, 8930),
    (1, False, 8928),
    (1, True, 8928),
    (2, False, 288),
    (2, True, 288),
    (3, False, 3),
    (3, True, 2),
)
PERIOD_LAW = {
    (event, contains_zero): period
    for event, contains_zero, period in PERIOD_LAW_ROWS
}
IDENTITY_TRANSIENT_KEY = (3, (1, 10))
IDENTITY_CYCLE_KEY = (2, (0, 9))


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def state_sha256(state: tuple[int, ...]) -> str:
    return sha256(bytes(state)).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_controls() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
        if (ROOT / path).is_file()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=Path(__file__).name,
    )
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    markers = {
        AUDIT_INPUT_PATHS[1]:
            {"candidate_regularities", "verify_cycle_row"},
        AUDIT_INPUT_PATHS[2]:
            {"advance_population", "verify_cycle", "verify_transient"},
        AUDIT_INPUT_PATHS[3]:
            {"exact_equality_partition", "mechanism_candidates"},
        AUDIT_INPUT_PATHS[4]:
            {"catalog_and_predictor", "masked_schedule", "reconstruct_sstar"},
    }
    sha_rows = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    blob_rows = {
        path: git_blob(payload) for path, payload in payloads.items()
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": (
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(
                not Path(path).is_absolute() and (ROOT / path).is_file()
                for path in AUDIT_INPUT_PATHS
            )
        ),
        "sha256": sha_rows,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": blob_rows,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "blocked_AST_markers": tuple(
            (path, tuple(sorted(names))) for path, names in markers.items()
        ),
        "blocked_AST_markers_present": all(
            names <= function_names(trees[path])
            for path, names in markers.items()
        ),
        "direct_frontier_imports": direct_frontier_imports,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS),
        "maximum_named_files": 7,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and result["blocked_AST_markers_present"]
        and direct_frontier_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not result["blocked_loaded"]
        and not result["firewall_hits"]
        and len(AUDIT_INPUT_PATHS) <= 7
    )
    return result


def separated_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if min(
            (pair[1] - pair[0]) % RING_STATIONS,
            (pair[0] - pair[1]) % RING_STATIONS,
        ) > 1
    )


def cyclic_separation(key: Key) -> int:
    left, right = key[1]
    return min(
        (right - left) % RING_STATIONS,
        (left - right) % RING_STATIONS,
    )


def sstar_predicate(key: Key) -> bool:
    return (
        key[0] == 0
        and 0 not in key[1]
        and cyclic_separation(key) == 5
    )


def synchronous_word(
    program: tuple[object, ...],
    positions0: tuple[int, int],
) -> tuple[object, ...]:
    positions = positions0
    word = []
    for _step in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple(
            (position + 1) % len(program) for position in positions
        )
    return tuple(word)


def build_family() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    epochs = []
    epoch_failures = 0
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        epoch_failures += after != K.A.apply_semantic(before, allocator)
        epoch_failures += rail_a != (1,) + (0,) * (len(program) - 1)
        epoch_failures += any(rail_b)
        epoch_failures += len(trace) != len(program)
        epochs.append((event, direction, before))
        state = after

    positions = separated_pairs()
    words = {
        pair: synchronous_word(program, pair) for pair in positions
    }
    states: dict[Key, tuple[int, ...]] = {}
    composition_failures = 0
    rail_failures = 0
    for event, _direction, before in epochs:
        for pair in positions:
            after, rail_a, rail_b, _trace = K.run_orbit(
                before, program, token_positions=pair
            )
            expected_rail = tuple(
                int(station in pair) for station in range(RING_STATIONS)
            )
            composition_failures += (
                after != K.A.apply_semantic(before, words[pair])
            )
            rail_failures += rail_a != expected_rail or any(rail_b)
            states[(event, pair)] = after
    summary = {
        "epochs": len(epochs),
        "positions": len(positions),
        "keys": len(states),
        "state_bits": len(next(iter(states.values()))),
        "allocator_gates": len(allocator),
        "word_gate_counts":
            tuple(sorted({len(word) for word in words.values()})),
        "epoch_failures": epoch_failures,
        "composition_failures": composition_failures,
        "rail_failures": rail_failures,
        "initial_state_sha256": digest(tuple(
            (key, state_sha256(states[key])) for key in sorted(states)
        )),
    }
    summary["pass"] = (
        summary["epochs"] == 4
        and summary["positions"] == 44
        and summary["keys"] == FAMILY_SIZE
        and summary["state_bits"] == 5815
        and summary["allocator_gates"] == 3106
        and summary["word_gate_counts"] == (6212,)
        and summary["epoch_failures"] == 0
        and summary["composition_failures"] == 0
        and summary["rail_failures"] == 0
    )
    return {
        "program": program,
        "positions": positions,
        "words": words,
        "states": states,
        "summary": summary,
    }


def watched_residual_wires() -> tuple[tuple[str, int], ...]:
    bank_named = (
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
        *((f"FRESH_{index}", wire)
          for index, wire in enumerate(K.A.FRESH)),
        *((f"ZERO_WORK_{index}", wire)
          for index, wire in enumerate(K.A.ZERO_WORK)),
        ("TOKEN_OK", K.A.TOKEN_OK),
    )
    rows = [("source.SOURCE_POINTER", K.R3.X.SOURCE_POINTER)]
    for bank_index, base in enumerate(
        K.M.R12.BANK_BASES[:FIXTURE_BANKS]
    ):
        rows.extend(
            (f"bank{bank_index}.{name}", base + wire)
            for name, wire in bank_named
        )
    for link_index, base in enumerate(
        K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]
    ):
        rows.extend(
            (f"link{link_index}.WIRE_{wire}", base + wire)
            for wire in range(K.B.LINK_WIDTH)
        )
    return tuple(rows)


def bit_slice(states: tuple[tuple[int, ...], ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def un_slice(columns: list[int], lane: int) -> tuple[int, ...]:
    return tuple((column >> lane) & 1 for column in columns)


def lane_numbers(mask: int) -> tuple[int, ...]:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def masked_schedule(
    program: tuple[object, ...],
    lanes: tuple[Lane, ...],
) -> tuple[MaskedGate, ...]:
    schedule = []
    for step in range(len(program)):
        for station, row in enumerate(program):
            mask = sum(
                1 << lane
                for lane, (key, _replica) in enumerate(lanes)
                if station in {
                    (key[1][0] + step) % len(program),
                    (key[1][1] + step) % len(program),
                }
            )
            if not mask:
                continue
            for gate in K.mapped_macro(row):
                if gate.kind == "X":
                    schedule.append((0, gate.wires[0], 0, 0, mask))
                elif gate.kind == "CNOT":
                    schedule.append(
                        (1, gate.wires[0], gate.wires[1], 0, mask)
                    )
                elif gate.kind == "TOF":
                    schedule.append(
                        (2, gate.wires[0], gate.wires[1], gate.wires[2], mask)
                    )
                else:
                    raise AssertionError(("non-reversible landed gate", gate))
                if len(set(gate.wires)) != len(gate.wires):
                    raise AssertionError(("repeated landed gate wire", gate))
    return tuple(schedule)


def advance(columns: list[int], schedule: tuple[MaskedGate, ...]) -> None:
    for kind, first, second, third, mask in schedule:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first] & mask
        else:
            columns[third] ^= columns[first] & columns[second] & mask


def nonclean_mask(
    columns: list[int],
    residual_rows: tuple[tuple[str, int], ...],
) -> int:
    result = 0
    for _name, wire in residual_rows:
        result |= columns[wire]
    return result


def equality_to_initial_mask(
    columns: list[int],
    initial_columns: list[int],
    candidates: int,
) -> int:
    matches = candidates
    for current, initial in zip(columns, initial_columns):
        matches &= candidates ^ ((current ^ initial) & candidates)
        if not matches:
            break
    return matches


def equality_to_target_mask(
    columns: list[int],
    target: tuple[int, ...],
    candidates: int,
    wires: tuple[int, ...] | None = None,
) -> int:
    matches = candidates
    selected = range(len(columns)) if wires is None else wires
    for wire in selected:
        matches &= (
            columns[wire]
            if target[wire]
            else candidates ^ (columns[wire] & candidates)
        )
        if not matches:
            break
    return matches


def support_at_lane(
    columns: list[int],
    lane: int,
    residual_rows: tuple[tuple[str, int], ...],
) -> tuple[str, ...]:
    return tuple(
        name for name, wire in residual_rows
        if (columns[wire] >> lane) & 1
    )


def proper_divisors(value: int) -> tuple[int, ...]:
    small = []
    large = []
    candidate = 1
    while candidate * candidate <= value:
        if value % candidate == 0:
            small.append(candidate)
            if candidate * candidate != value:
                large.append(value // candidate)
        candidate += 1
    return tuple(row for row in small + list(reversed(large)) if row < value)


def minimal_sequence_period(
    sequence: tuple[tuple[str, ...], ...],
) -> int:
    for candidate in proper_divisors(len(sequence)) + (len(sequence),):
        if all(
            sequence[index] == sequence[index % candidate]
            for index in range(len(sequence))
        ):
            return candidate
    raise AssertionError("finite sequence has no period")


def boundary_snapshot(
    horizon: int,
    active_mask: int,
    primary_lanes: tuple[Lane, ...],
    columns: list[int],
    residual_rows: tuple[tuple[str, int], ...],
    records: dict[Key, dict[str, object]],
) -> dict[str, object]:
    open_keys = tuple(
        primary_lanes[lane][0] for lane in lane_numbers(active_mask)
    )
    rows = []
    for lane in lane_numbers(active_mask):
        key = primary_lanes[lane][0]
        support = support_at_lane(columns, lane, residual_rows)
        state = un_slice(columns, lane)
        rows.append((key, support, state_sha256(state)))
    transient_count = sum(
        row["outcome"] == "TRANSIENT"
        and int(row["resolution_moment"]) <= horizon
        for row in records.values()
    )
    cycle_count = sum(
        row["outcome"] == "CYCLE"
        and int(row["resolution_moment"]) <= horizon
        for row in records.values()
    )
    result = {
        "horizon": horizon,
        "transient_count": transient_count,
        "cycle_count": cycle_count,
        "open_count": len(open_keys),
        "accounting_total": transient_count + cycle_count + len(open_keys),
        "open_key_sha256": digest(open_keys),
        "landed_boundary_tests_executed": len(rows),
        "landed_boundary_row_sha256": digest(tuple(rows)),
        "open_support_weight_census": dict(sorted(Counter(
            len(row[1]) for row in rows
        ).items())),
        "all_open_landed_nonclean": all(row[1] for row in rows),
        "open_keys": open_keys,
    }
    result["pass"] = (
        result["accounting_total"] == FAMILY_SIZE
        and result["landed_boundary_tests_executed"] == len(open_keys)
        and result["all_open_landed_nonclean"]
    )
    return result


def public_boundary(row: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in row.items() if key != "open_keys"}


def determinism_boundary(
    horizon: int,
    keys: tuple[Key, ...],
    primary_index: dict[Key, int],
    duplicate_index: dict[Key, int],
    columns: list[int],
) -> dict[str, object]:
    rows = []
    for key in keys:
        primary_state = un_slice(columns, primary_index[key])
        duplicate_state = un_slice(columns, duplicate_index[key])
        rows.append({
            "key": key,
            "primary_sha256": state_sha256(primary_state),
            "duplicate_sha256": state_sha256(duplicate_state),
            "exact_tuple_equal": primary_state == duplicate_state,
        })
    return {
        "horizon": horizon,
        "rows": tuple(rows),
        "row_sha256": digest(tuple(rows)),
        "all_exact": all(row["exact_tuple_equal"] for row in rows),
    }


def budget_decision(
    script_started: float,
    phase_seconds: float,
    phase_updates: int,
    start: int,
    candidate: int,
) -> dict[str, object]:
    rate = phase_seconds / phase_updates
    elapsed = monotonic() - script_started
    projected = (
        elapsed
        + BUDGET_SAFETY_FACTOR * rate * (candidate - start)
        + BUDGET_RESERVE_SEC
    )
    return {
        "at_boundary": start,
        "candidate": candidate,
        "measured_phase_seconds": round(phase_seconds, 6),
        "measured_phase_updates": phase_updates,
        "seconds_per_global_update": round(rate, 12),
        "elapsed_at_decision_seconds": round(elapsed, 6),
        "safety_factor": BUDGET_SAFETY_FACTOR,
        "reserve_seconds": BUDGET_RESERVE_SEC,
        "decision_limit_seconds": BUDGET_DECISION_LIMIT_SEC,
        "projected_total_seconds": round(projected, 6),
        "accepted": projected < BUDGET_DECISION_LIMIT_SEC,
    }


def render(
    checks: dict[str, bool],
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    lines = [
        f"{'PASS' if passed else 'FAIL'} {name}"
        for name, passed in checks.items()
    ]
    lines.extend(
        f"CERTIFICATE {name} {compact(value)}"
        for name, value in certificates.items()
    )
    lines.append("SUMMARY_JSON " + compact(report))
    lines.append(str(report["terminal"]))
    return "\n".join(lines) + "\n"


def stable_render(
    checks: dict[str, bool],
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    for _attempt in range(20):
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE831_DEEP_K2_FORECAST_TESTS_PASS"
            if report["pass"]
            else "CYCLE831_DEEP_K2_FORECAST_TESTS_HONEST_FAIL"
        )
        output = render(checks, certificates, report)
        size = len(output.encode())
        controls = certificates["E_CONTROLS"]
        if report["stdout_bytes"] == size and controls["stdout_bytes"] == size:
            return output
        report["stdout_bytes"] = size
        controls["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    script_started = monotonic()
    sources = source_controls()
    family = build_family()
    catalog = tuple(sorted(family["states"]))
    expected_open = tuple(
        key for key in catalog if key not in EXPECTED_RESOLVED_THROUGH_819
    )
    determinism_keys = expected_open[:DETERMINISM_SLICE_SIZE]
    primary_lanes: tuple[Lane, ...] = tuple(
        (key, "primary") for key in catalog
    )
    duplicate_lanes: tuple[Lane, ...] = tuple(
        (key, "determinism_duplicate") for key in determinism_keys
    )
    lanes = primary_lanes + duplicate_lanes
    primary_index = {
        key: lane for lane, (key, _replica) in enumerate(primary_lanes)
    }
    duplicate_index = {
        key: len(primary_lanes) + offset
        for offset, key in enumerate(determinism_keys)
    }
    initial_states = tuple(
        family["states"][key] for key, _replica in lanes
    )
    columns = bit_slice(initial_states)
    initial_columns = columns.copy()
    schedule = masked_schedule(family["program"], lanes)
    residual_rows = watched_residual_wires()
    primary_mask = (1 << len(primary_lanes)) - 1
    baseline_mask = sum(1 << primary_index[key] for key in expected_open)
    duplicate_initial_exact = all(
        initial_states[primary_index[key]]
        == initial_states[duplicate_index[key]]
        for key in determinism_keys
    )
    duplicate_masks_identical = all(
        ((mask >> primary_index[key]) & 1)
        == ((mask >> duplicate_index[key]) & 1)
        for _kind, _first, _second, _third, mask in schedule
        for key in determinism_keys
    )

    one_step = columns.copy()
    advance(one_step, schedule)
    schedule_equivalence = all(
        un_slice(one_step, primary_index[key])
        == K.A.apply_semantic(
            family["states"][key], family["words"][key[1]]
        )
        for key in catalog
    )

    records: dict[Key, dict[str, object]] = {}
    active_mask = primary_mask
    previous_nonclean = nonclean_mask(columns, residual_rows)
    nonclean_prefix_counts = [
        int(bool(previous_nonclean & (1 << lane)))
        for lane in range(len(primary_lanes))
    ]
    initial_inequality_counts = [0] * len(primary_lanes)
    identity_supports = (
        support_at_lane(
            columns, primary_index[IDENTITY_CYCLE_KEY], residual_rows
        ),
    )
    sstar: tuple[int, ...] | None = None
    sstar_reconstruction: dict[str, object] = {}
    sstar_visits: dict[Key, list[int]] = {
        key: [] for key in expected_open
    }
    sstar_visit_hasher = sha256()
    new_resolution_keys: list[Key] = []

    def record_hit(
        key: Key,
        outcome: str,
        moment: int,
        nonclean: int,
    ) -> None:
        lane = primary_index[key]
        state = un_slice(columns, lane)
        verification: dict[str, object]
        if outcome == "TRANSIENT":
            verification = {
                "method":
                    "ONLINE_EXACT_PER_MOMENT_LANDED_SUPPORT_MONITOR",
                "moment": moment,
                "earlier_moments_checked": moment,
                "earlier_nonclean_count":
                    nonclean_prefix_counts[lane],
                "earlier_moments_nonclean":
                    nonclean_prefix_counts[lane] == moment,
                "landed_veto_at_t_minus_1":
                    bool(previous_nonclean & (1 << lane)),
                "event_is_clean": not bool(nonclean & (1 << lane)),
                "observed_state_sha256": state_sha256(state),
            }
            verification["pass"] = (
                verification["earlier_moments_nonclean"]
                and verification["landed_veto_at_t_minus_1"]
                and verification["event_is_clean"]
            )
        else:
            period = moment
            verification = {
                "method":
                    "EXACT_RETURN_TO_T0_EVERY_MOMENT_SCAN_PLUS_REVERSIBILITY",
                "entry": 0,
                "closure": moment,
                "state_period": period,
                "exact_recurrence_to_initial":
                    state == family["states"][key],
                "earlier_return_moments_checked": period - 1,
                "earlier_initial_inequality_count":
                    initial_inequality_counts[lane],
                "every_earlier_return_rejected":
                    initial_inequality_counts[lane] == period - 1,
                "proper_divisors": proper_divisors(period),
                "proper_divisor_returns": (),
                "minimal_period":
                    initial_inequality_counts[lane] == period - 1,
                "cycle_phase_count": period,
                "nonclean_cycle_phase_count":
                    nonclean_prefix_counts[lane],
                "all_cycle_phases_nonclean":
                    nonclean_prefix_counts[lane] == period,
                "reversibility_basis":
                    "each landed lane update is a composition solely of "
                    "distinct-wire X/CNOT/TOF gates",
                "observed_state_sha256": state_sha256(state),
            }
            verification["pass"] = (
                verification["exact_recurrence_to_initial"]
                and verification["every_earlier_return_rejected"]
                and verification["minimal_period"]
                and verification["all_cycle_phases_nonclean"]
            )
        row: dict[str, object] = {
            "key": key,
            "outcome": outcome,
            "resolution_moment": moment,
            "first_clean": moment if outcome == "TRANSIENT" else None,
            "cycle_entry": 0 if outcome == "CYCLE" else None,
            "state_period": moment if outcome == "CYCLE" else None,
            "verification": verification,
        }
        if moment > BASELINE_HORIZON:
            visit_rows = tuple(sstar_visits[key])
            f1 = {
                "predicate_event0_origin_absent_max_separation5":
                    sstar_predicate(key),
                "predicate_expected_false": not sstar_predicate(key),
                "exact_Sstar_visit_count_through_resolution":
                    len(visit_rows),
                "exact_Sstar_visit_moments_through_resolution": visit_rows,
                "resolution_minus_5": moment - SSTAR_LAG,
                "state_at_resolution_minus_5_equals_Sstar":
                    moment - SSTAR_LAG in visit_rows,
                "outcome":
                    "HOLDS_NO_NEW_SSTAR_ENTRANT"
                    if not visit_rows else "FALSIFIED_NEW_SSTAR_ENTRANT",
            }
            f1["pass"] = (
                f1["predicate_expected_false"] and not visit_rows
            )
            row["F1"] = f1
            contains_zero = 0 in key[1]
            if outcome == "CYCLE":
                expected_period = PERIOD_LAW[(key[0], contains_zero)]
                f2 = {
                    "event": key[0],
                    "contains_zero": contains_zero,
                    "expected_period": expected_period,
                    "observed_period": moment,
                    "outcome":
                        "HOLDS_PERIOD_LAW"
                        if moment == expected_period
                        else "FALSIFIED_PERIOD_LAW",
                    "pass": moment == expected_period,
                }
            else:
                f2 = {
                    "event": key[0],
                    "contains_zero": contains_zero,
                    "expected_period": None,
                    "observed_period": None,
                    "outcome": "NOT_APPLICABLE_TRANSIENT",
                    "pass": True,
                }
            row["F2"] = f2
            if outcome == "TRANSIENT":
                same_state_mask = equality_to_target_mask(
                    columns, state, baseline_mask
                )
                row["merger_at_resolution_moment"] = {
                    "moment": moment,
                    "same_state_keys": tuple(
                        primary_lanes[index][0]
                        for index in lane_numbers(same_state_mask)
                    ),
                    "exact_tuple_equality": True,
                    "scan_scope":
                        "all 151 Cycle-819-open primaries at this exact moment",
                }
            else:
                row["merger_at_resolution_moment"] = {
                    "outcome": "NOT_APPLICABLE_CYCLE",
                }
            row["F3"] = {
                "legacy_795_forecast_vector_status": "EXTINCT_EXCLUDED",
                "classification": "PURE_DATA",
                "pass": True,
            }
            new_resolution_keys.append(key)
        records[key] = row

    def scan_sstar(update: int) -> None:
        if sstar is None or update <= BASELINE_HORIZON:
            return
        residual_wires = tuple(wire for _name, wire in residual_rows)
        candidates = equality_to_target_mask(
            columns, sstar, baseline_mask, residual_wires
        )
        matches = equality_to_target_mask(
            columns, sstar, candidates
        ) if candidates else 0
        for lane in lane_numbers(matches):
            key = primary_lanes[lane][0]
            sstar_visits[key].append(update)
            sstar_visit_hasher.update(compact((key, update)).encode())

    def evolve_phase(start: int, stop: int) -> dict[str, object]:
        nonlocal active_mask, previous_nonclean, identity_supports
        phase_started = monotonic()
        start_active = active_mask
        logical_transitions = 0
        phase_resolutions = []
        for update in range(start + 1, stop + 1):
            advance(columns, schedule)
            logical_transitions += active_mask.bit_count()
            nonclean = nonclean_mask(columns, residual_rows)
            if update < EXPECTED_OLD_CYCLES[IDENTITY_CYCLE_KEY]:
                identity_supports += (
                    support_at_lane(
                        columns,
                        primary_index[IDENTITY_CYCLE_KEY],
                        residual_rows,
                    ),
                )
            if update == SSTAR_ENTRY:
                reconstructed = un_slice(
                    columns, primary_index[NINE_SSTAR_KEYS[0]]
                )
                exact_class = equality_to_target_mask(
                    columns, reconstructed, primary_mask
                )
                nonlocal_sstar[0] = reconstructed
                sstar_reconstruction.update({
                    "entry": SSTAR_ENTRY,
                    "state_bits": len(reconstructed),
                    "state_sha256": state_sha256(reconstructed),
                    "exact_population_class": tuple(
                        primary_lanes[lane][0]
                        for lane in lane_numbers(exact_class)
                    ),
                })
            scan_sstar(update)
            clean_hits = active_mask & ~nonclean
            recurrence_hits = equality_to_initial_mask(
                columns,
                initial_columns,
                active_mask & ~clean_hits,
            )
            for lane in lane_numbers(clean_hits):
                key = primary_lanes[lane][0]
                record_hit(key, "TRANSIENT", update, nonclean)
                phase_resolutions.append(key)
            for lane in lane_numbers(recurrence_hits):
                key = primary_lanes[lane][0]
                record_hit(key, "CYCLE", update, nonclean)
                phase_resolutions.append(key)
            active_mask &= ~(clean_hits | recurrence_hits)
            for lane in lane_numbers(active_mask):
                nonclean_prefix_counts[lane] += int(
                    bool(nonclean & (1 << lane))
                )
                initial_inequality_counts[lane] += 1
            previous_nonclean = nonclean
        upper = start_active.bit_count() * (stop - start)
        return {
            "start_horizon": start,
            "end_horizon": stop,
            "active_keys_before": start_active.bit_count(),
            "active_keys_after": active_mask.bit_count(),
            "logical_transitions_executed": logical_transitions,
            "logical_transition_upper_if_no_terminals": upper,
            "logical_transitions_saved_by_terminals":
                upper - logical_transitions,
            "transitions_account":
                logical_transitions + (upper - logical_transitions) == upper,
            "physical_global_updates": stop - start,
            "resolutions_in_phase": len(phase_resolutions),
            "resolved_keys": tuple(phase_resolutions),
            "complete_population": True,
            "seconds": round(monotonic() - phase_started, 6),
        }

    # A one-element cell lets the nested phase function install S* while the
    # scan function keeps a simple nonlocal read through the synchronized name.
    nonlocal_sstar: list[tuple[int, ...] | None] = [None]

    baseline_phase = evolve_phase(0, BASELINE_HORIZON)
    sstar = nonlocal_sstar[0]
    if sstar is None:
        raise AssertionError("S* reconstruction moment not reached")
    baseline_boundary = boundary_snapshot(
        BASELINE_HORIZON,
        active_mask,
        primary_lanes,
        columns,
        residual_rows,
        records,
    )
    boundary_rows = [baseline_boundary]
    determinism_rows = [
        determinism_boundary(
            BASELINE_HORIZON,
            determinism_keys,
            primary_index,
            duplicate_index,
            columns,
        )
    ]
    phases = [baseline_phase]
    decisions = []
    reached = BASELINE_HORIZON

    decision32768 = budget_decision(
        script_started,
        float(baseline_phase["seconds"]),
        BASELINE_HORIZON,
        BASELINE_HORIZON,
        MINIMUM_DEEP_HORIZON,
    )
    decisions.append(decision32768)
    if decision32768["accepted"]:
        phase32768 = evolve_phase(
            BASELINE_HORIZON, MINIMUM_DEEP_HORIZON
        )
        phases.append(phase32768)
        reached = MINIMUM_DEEP_HORIZON
        boundary_rows.append(boundary_snapshot(
            reached,
            active_mask,
            primary_lanes,
            columns,
            residual_rows,
            records,
        ))
        determinism_rows.append(determinism_boundary(
            reached,
            determinism_keys,
            primary_index,
            duplicate_index,
            columns,
        ))
        decision65536 = budget_decision(
            script_started,
            float(phase32768["seconds"]),
            MINIMUM_DEEP_HORIZON - BASELINE_HORIZON,
            MINIMUM_DEEP_HORIZON,
            TARGET_HORIZON,
        )
        decisions.append(decision65536)
        if decision65536["accepted"]:
            phase65536 = evolve_phase(
                MINIMUM_DEEP_HORIZON, TARGET_HORIZON
            )
            phases.append(phase65536)
            reached = TARGET_HORIZON
            boundary_rows.append(boundary_snapshot(
                reached,
                active_mask,
                primary_lanes,
                columns,
                residual_rows,
                records,
            ))
            determinism_rows.append(determinism_boundary(
                reached,
                determinism_keys,
                primary_index,
                duplicate_index,
                columns,
            ))

    baseline_open = tuple(baseline_boundary["open_keys"])
    sstar_reconstruction["expected_class"] = NINE_SSTAR_KEYS
    sstar_reconstruction["pass"] = (
        sstar_reconstruction["state_bits"] == 5815
        and sstar_reconstruction["exact_population_class"]
        == NINE_SSTAR_KEYS
    )
    selected_by_predicate = tuple(
        key for key in catalog if sstar_predicate(key)
    )
    f1_predicate_control = {
        "predicate":
            "event=0 AND origin absent AND max cyclic separation=5",
        "selected_keys": selected_by_predicate,
        "selected_exactly_nine_known_entrants":
            selected_by_predicate == NINE_SSTAR_KEYS,
        "all_151_baseline_open_fail_predicate":
            all(not sstar_predicate(key) for key in baseline_open),
    }
    f1_predicate_control["pass"] = (
        f1_predicate_control["selected_exactly_nine_known_entrants"]
        and f1_predicate_control[
            "all_151_baseline_open_fail_predicate"
        ]
    )

    new_resolutions = tuple(
        records[key] for key in sorted(
            new_resolution_keys,
            key=lambda row: (
                int(records[row]["resolution_moment"]), row
            ),
        )
    )
    new_transients = tuple(
        row for row in new_resolutions
        if row["outcome"] == "TRANSIENT"
    )
    merger_pairs = []
    for left, right in combinations(new_transients, 2):
        left_matches = set(
            left["merger_at_resolution_moment"]["same_state_keys"]
        )
        right_matches = set(
            right["merger_at_resolution_moment"]["same_state_keys"]
        )
        same_moment = (
            left["resolution_moment"] == right["resolution_moment"]
        )
        same_at_left = right["key"] in left_matches
        same_at_right = left["key"] in right_matches
        merger_pairs.append({
            "left": left["key"],
            "right": right["key"],
            "same_resolution_moment": same_moment,
            "exact_same_state_at_left_resolution_moment": same_at_left,
            "exact_same_state_at_right_resolution_moment": same_at_right,
            "shared_moment_and_state":
                same_moment and same_at_left and same_at_right,
        })
    merger_certificate = {
        "definition":
            "Cycle-820-style same-time exact tuple equality, evaluated "
            "online at every new transient resolution moment against all "
            "151 baseline-open keys",
        "new_transient_count": len(new_transients),
        "pair_rows": tuple(merger_pairs),
        "any_new_transients_share_resolution_moment_and_state": any(
            row["shared_moment_and_state"] for row in merger_pairs
        ),
        "any_cross_key_exact_state_match_at_either_tested_moment": any(
            row["exact_same_state_at_left_resolution_moment"]
            or row["exact_same_state_at_right_resolution_moment"]
            for row in merger_pairs
        ),
        "pass": (
            len(merger_pairs)
            == len(new_transients) * (len(new_transients) - 1) // 2
        ),
    }
    cohort_keys = tuple(sorted({
        (
            int(row["resolution_moment"]),
            str(row["outcome"]),
            int(row["key"][0]),
        )
        for row in new_resolutions
    }))
    resolution_cohorts = tuple({
        "resolution_moment": moment,
        "outcome": outcome,
        "event": event,
        "keys": tuple(
            row["key"] for row in new_resolutions
            if row["resolution_moment"] == moment
            and row["outcome"] == outcome
            and row["key"][0] == event
        ),
        "count": sum(
            row["resolution_moment"] == moment
            and row["outcome"] == outcome
            and row["key"][0] == event
            for row in new_resolutions
        ),
        "all_exact_same_state_at_resolution": all(
            set(
                candidate["key"] for candidate in new_resolutions
                if candidate["resolution_moment"] == moment
                and candidate["outcome"] == outcome
                and candidate["key"][0] == event
            ) <= set(row["merger_at_resolution_moment"]["same_state_keys"])
            for row in new_resolutions
            if row["resolution_moment"] == moment
            and row["outcome"] == "TRANSIENT"
            and row["key"][0] == event
        ) if outcome == "TRANSIENT" else None,
    } for moment, outcome, event in cohort_keys)

    identity_transient = records.get(IDENTITY_TRANSIENT_KEY)
    identity_cycle = records.get(IDENTITY_CYCLE_KEY)
    identity_residual_period = minimal_sequence_period(identity_supports)
    identity_pass = (
        identity_transient is not None
        and identity_transient["outcome"] == "TRANSIENT"
        and identity_transient["resolution_moment"] == 252
        and identity_transient["verification"]["pass"]
        and identity_cycle is not None
        and identity_cycle["outcome"] == "CYCLE"
        and identity_cycle["state_period"] == 288
        and identity_cycle["verification"]["pass"]
        and identity_residual_period == 6
    )

    baseline_pass = (
        len(EXPECTED_RESOLVED_THROUGH_819) == 25
        and len(expected_open) == 151
        and baseline_open == expected_open
        and baseline_boundary["transient_count"] == 11
        and baseline_boundary["cycle_count"] == 14
        and baseline_boundary["open_count"] == 151
        and all(
            records[key]["outcome"] == "TRANSIENT"
            and records[key]["resolution_moment"] == moment
            for key, moment in EXPECTED_CONTROL_TRANSIENTS.items()
        )
        and all(
            records[key]["outcome"] == "CYCLE"
            and records[key]["state_period"] == period
            for key, period in {
                **EXPECTED_OLD_CYCLES, **EXPECTED_LATE_CYCLES
            }.items()
        )
        and all(
            records[key]["outcome"] == "TRANSIENT"
            and records[key]["resolution_moment"] == 14744
            for key in NINE_SSTAR_KEYS
        )
    )
    a_pass = (
        sources["pass"]
        and family["summary"]["pass"]
        and schedule_equivalence
        and duplicate_initial_exact
        and duplicate_masks_identical
        and baseline_pass
        and reached >= MINIMUM_DEEP_HORIZON
        and reached in BOUNDARIES
        and all(row["pass"] for row in boundary_rows)
        and all(row["complete_population"] for row in phases)
        and all(row["transitions_account"] for row in phases)
        and all(
            row["verification"]["pass"] for row in new_resolutions
        )
    )
    b_pass = (
        f1_predicate_control["pass"]
        and all(row["F1"]["pass"] for row in new_resolutions)
        and all(row["F2"]["pass"] for row in new_resolutions)
        and all(row["F3"]["pass"] for row in new_resolutions)
        and merger_certificate["pass"]
    )
    null_applies = not new_resolutions
    continuation_phases = tuple(
        row for row in phases if row["start_horizon"] >= BASELINE_HORIZON
    )
    c_pass = (
        not null_applies
        or (
            all(row["resolutions_in_phase"] == 0
                for row in continuation_phases)
            and active_mask.bit_count() == 151
            and sum(
                int(row["logical_transitions_executed"])
                for row in continuation_phases
            )
            == 151 * (reached - BASELINE_HORIZON)
        )
    )
    deterministic = (
        duplicate_initial_exact
        and duplicate_masks_identical
        and all(row["all_exact"] for row in determinism_rows)
    )
    elapsed = monotonic() - script_started
    controls_base = (
        sources["pass"]
        and deterministic
        and not any(
            name in sys.modules for name in BLOCKLISTED_MODULES
        )
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )

    checks = {
        "A_DEEP_CONTINUATION_COMPLETE_BOUNDARIES": a_pass,
        "B_RESOLUTIONS_F1_F2_F3_AND_MERGER_TESTED": b_pass,
        "C_NULL_WITH_TRANSITION_ACCOUNTING_IF_APPLICABLE": c_pass,
        "D_TWO_IDENTITY_RESOLUTIONS_REPRODUCE": identity_pass,
        "E_SHAS_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT": controls_base,
    }
    certificates: dict[str, object] = {
        "A_DEEP_CONTINUATION": {
            "baseline":
                "151 k=2 keys open through complete T=16384, reproduced",
            "family": family["summary"],
            "masked_schedule": {
                "lanes": len(lanes),
                "primary_lanes": len(primary_lanes),
                "determinism_duplicate_lanes": len(duplicate_lanes),
                "instructions_per_global_update": len(schedule),
                "all_lane_one_step_scalar_equivalence":
                    schedule_equivalence,
                "duplicate_initial_states_exact":
                    duplicate_initial_exact,
                "duplicate_lane_masks_identical":
                    duplicate_masks_identical,
                "reversibility_basis": "X/CNOT/TOF only",
            },
            "Sstar_reconstruction": sstar_reconstruction,
            "budget_decisions": tuple(decisions),
            "target_horizon": TARGET_HORIZON,
            "minimum_requested_horizon": MINIMUM_DEEP_HORIZON,
            "horizon_reached": reached,
            "target_reached": reached == TARGET_HORIZON,
            "complete_boundaries": tuple(
                row["horizon"] for row in boundary_rows
            ),
            "boundary_landed_cleanliness":
                tuple(public_boundary(row) for row in boundary_rows),
            "transition_accounting": tuple(phases),
            "final_open_key_sha256":
                boundary_rows[-1]["open_key_sha256"],
        },
        "B_RESOLUTIONS_AND_FORECAST_TESTS": {
            "standing_F1": f1_predicate_control,
            "standing_F2": {
                "law":
                    "state period by (event,zero-membership), Cycle-818 "
                    "strict k=2 table union-refined by Cycle-819 strata",
                "rows_event_contains_zero_expected_period":
                    PERIOD_LAW_ROWS,
            },
            "standing_F3":
                "Cycle-795 forecast-vector class extinct; new resolutions "
                "are pure data and no legacy vector is scored",
            "new_resolution_count": len(new_resolutions),
            "resolution_cohorts": resolution_cohorts,
            "new_resolutions": new_resolutions,
            "Sstar_visit_count_over_151_continuation_trajectories":
                sum(len(rows) for rows in sstar_visits.values()),
            "Sstar_visit_stream_sha256": sstar_visit_hasher.hexdigest(),
            "merger_scan": merger_certificate,
        },
        "C_NULL_BRANCH": {
            "applies": null_applies,
            "statement": (
                f"NO KEY RESOLVED FROM T={BASELINE_HORIZON + 1} THROUGH "
                f"COMPLETE T={reached}; F1/F2/F3 STAY STANDING"
                if null_applies else
                "NULL DOES NOT APPLY; CERTIFICATE B PRINTS EVERY NEW "
                "RESOLUTION AND ITS IMMEDIATE FORECAST TESTS"
            ),
            "continuation_transition_accounting": continuation_phases,
            "forecasts_status":
                "STANDING_UNTESTED_ON_NULL"
                if null_applies else "TESTED_BY_NEW_DATA",
        },
        "D_IDENTITY_CONTROLS": {
            "known_transient": identity_transient,
            "known_cycle": identity_cycle,
            "known_cycle_residual_period": identity_residual_period,
            "statement":
                "first-clean t=252 and exact minimal state-period 288/"
                "residual-period 6 reproduce",
        },
        "E_CONTROLS": {
            **sources,
            "determinism_scope": {
                "declaration":
                    "first eight lexicographic Cycle-819-open keys carried "
                    "as distinct duplicate lanes from t=0 through every "
                    "reached complete boundary",
                "keys": determinism_keys,
                "initial_states_exact": duplicate_initial_exact,
                "identical_lane_masks": duplicate_masks_identical,
                "boundary_rows": tuple(determinism_rows),
                "deterministic": deterministic,
            },
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_bytes": 0,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "blocked_modules_loaded_at_end": tuple(
                name for name in BLOCKLISTED_MODULES
                if name in sys.modules
            ),
            "firewall_hits_at_end": tuple(FIREWALL.hits),
        },
    }
    final_boundary = boundary_rows[-1]
    report = {
        "cycle": 831,
        "horizon_reached": reached,
        "target_horizon": TARGET_HORIZON,
        "new_resolution_count": len(new_resolutions),
        "new_transient_count": len(new_transients),
        "new_cycle_count": sum(
            row["outcome"] == "CYCLE" for row in new_resolutions
        ),
        "F1":
            "HOLDS" if all(row["F1"]["pass"]
                           for row in new_resolutions) else "FALSIFIED",
        "F2": (
            "STANDING_NO_NEW_CYCLE"
            if not any(
                row["outcome"] == "CYCLE" for row in new_resolutions
            )
            else (
                "HOLDS" if all(row["F2"]["pass"]
                               for row in new_resolutions)
                else "FALSIFIED"
            )
        ),
        "merger":
            "YES" if merger_certificate[
                "any_new_transients_share_resolution_moment_and_state"
            ] else "NO",
        "null_applies": null_applies,
        "final_counts": {
            key: final_boundary[key]
            for key in (
                "transient_count", "cycle_count", "open_count",
                "accounting_total",
            )
        },
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE831_DEEP_K2_FORECAST_TESTS_HONEST_FAIL",
    }
    output = stable_render(checks, certificates, report)
    stdout_ok = len(output.encode()) < STDOUT_LIMIT_BYTES
    checks["E_SHAS_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT"] = (
        controls_base and stdout_ok
    )
    output = stable_render(checks, certificates, report)
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "terminal": "CYCLE831_DEEP_K2_FORECAST_TESTS_HONEST_FAIL",
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode()),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "pass": False,
            "terminal": "CYCLE831_DEEP_K2_FORECAST_TESTS_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
