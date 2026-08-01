#!/usr/bin/env python3
"""Cycle 861: exact confirmation-ladder identification audit.

The owner-supplied N6 model sets a record possibility at its first clean
post-engagement H boundary, confirms it at every later clean H-boundary
revisit, and locks the record at a chosen rung.  This runner reconstructs the
complete Cycle-852 census and horizon directly from the Cycle-719 core.  The
Cycle-852/856/860 primaries, plus the historical Cycle-849 trio-mark source,
are SHA-pinned text/AST provenance only and are never imported.

This is a model-layer audit.  It changes no axiom surface and treats the lock
threshold as a dial unless the computed threshold structure forces one.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Callable


AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle852_selection_tournament_2026_07_28.py",
    "scripts/frontier_cycle856_record_covariance_2026_07_28.py",
    "scripts/frontier_cycle860_readout_discriminator_2026_07_28.py",
)
CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
HISTORICAL_AST_PROVENANCE = (
    "655dd678aa",
    "scripts/frontier_cycle849_scheduling_contrast_2026_07_28.py",
    "0f1d15c444514f81ac007e2c122b3b47c917bec9a01de8b4e5fef358ef910818",
    "f2e842dbdbc04df27ddd078424a5cd9bc9455af5",
)
BLOCKLISTED_MODULES = tuple(sorted({
    *(Path(path).stem for path in TEXT_AST_ONLY_PATHS),
    Path(HISTORICAL_AST_PROVENANCE[1]).stem,
}))
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "fcb1e5ad22e48dc865754bc0a0f5357cdef8e78b477c21f48b74e5971eaa8419",
    AUDIT_INPUT_PATHS[2]:
        "20bce7f6dab9d7755ddefc6e2000d501acb8572dc15f50981b65ba9f6e2a4f2b",
    AUDIT_INPUT_PATHS[3]:
        "28a62fb0bc83ec7a46c18901158693344a84cc1eff8c0c9537b40d9004d8b926",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "d584154f32ead0a03a9661c6f176d52b2a1a77dc",
    AUDIT_INPUT_PATHS[2]: "fc873d0b1947866b238bbe5456ffe89fcd072a21",
    AUDIT_INPUT_PATHS[3]: "b48450fbe70f152bfeaab561a12591a2ec7d48c0",
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if any cited text/AST-only primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids primary import: {fullname}")
        return None


PRIMARY_FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, PRIMARY_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, int, tuple[int, ...]]
State = tuple[int, ...]
Selection = frozenset[Key]

FIXTURE_BANKS = 2
MIN_SOURCES = 2
MAX_SOURCES = 5
TRAJECTORY_HORIZON = 51_115
LANDED_E1_STAMPED = 182
LANDED_E2_STAMPED = 114
E2_LANDED_RULE = "record set = first-clean orbit-return selection-event set"
K3_TRIOS: tuple[Key, ...] = (
    (3, 2, (0, 2, 6)),
    (3, 3, (0, 2, 6)),
    (3, 2, (0, 2, 7)),
    (3, 3, (0, 2, 7)),
    (3, 2, (0, 2, 8)),
    (3, 3, (0, 2, 8)),
)
K3_MARK_WIRES = (256, 262)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target in (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        if isinstance(target, ast.Name) and target.id == name
    ]
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def function_names(tree: ast.Module) -> frozenset[str]:
    return frozenset(
        node.name for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    )


def historical_payload() -> bytes:
    commit, path, _expected_sha, _expected_blob = HISTORICAL_AST_PROVENANCE
    return subprocess.run(
        ("git", "show", f"{commit}:{path}"),
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    ).stdout


def source_controls() -> dict[str, object]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=Path(__file__).name,
    )
    historical = historical_payload()
    historical_tree = ast.parse(
        historical, filename=HISTORICAL_AST_PROVENANCE[1]
    )
    sha_rows = {
        path: sha256(payload).hexdigest() for path, payload in payloads.items()
    }
    blob_rows = {path: git_blob(payload) for path, payload in payloads.items()}
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    primary_markers = {
        AUDIT_INPUT_PATHS[1]: {
            "derive_census", "dirty_global_indices", "trajectory_census",
        },
        AUDIT_INPUT_PATHS[2]: {
            "monitor_stamp_sets", "monitor_dependence_report",
        },
        AUDIT_INPUT_PATHS[3]: {"lane_snapshot_sha", "stamp_scan"},
    }
    marker_exact = all(
        markers <= function_names(trees[path])
        for path, markers in primary_markers.items()
    )
    historical_keys = literal_assignment(historical_tree, "K3_OPEN_KEYS")
    expected_historical_trios = tuple(
        (k, event, positions)
        for k, positions, event in (historical_keys or ())
        if positions[1] == 2
    )
    historical_facts = {
        "sha256": sha256(historical).hexdigest(),
        "git_blob": git_blob(historical),
        "K3_OPEN_KEYS": historical_keys,
        "EXPECTED_K3_NATIVE_WIRES": literal_assignment(
            historical_tree, "EXPECTED_K3_NATIVE_WIRES"
        ),
        "certificate_markers": tuple(sorted(
            {"certificate_b_mark", "certificate_c_contrast"}
            & function_names(historical_tree)
        )),
        "trio_mapping_exact": expected_historical_trios == K3_TRIOS,
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "sha256": sha_rows,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": blob_rows,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "historical_text_AST_only": {
            "commit": HISTORICAL_AST_PROVENANCE[0],
            "path": HISTORICAL_AST_PROVENANCE[1],
            **historical_facts,
        },
        "parsed_top_level_counts": {
            **{path: len(tree.body) for path, tree in trees.items()},
            f"{HISTORICAL_AST_PROVENANCE[0]}:{HISTORICAL_AST_PROVENANCE[1]}":
                len(historical_tree.body),
        },
        "AST_semantic_markers_exact": marker_exact,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(PRIMARY_FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and all(result["parsed_top_level_counts"].values())
        and marker_exact
        and historical_facts["sha256"] == HISTORICAL_AST_PROVENANCE[2]
        and historical_facts["git_blob"] == HISTORICAL_AST_PROVENANCE[3]
        and historical_facts["EXPECTED_K3_NATIVE_WIRES"] == K3_MARK_WIRES
        and historical_facts["certificate_markers"]
            == ("certificate_b_mark", "certificate_c_contrast")
        and historical_facts["trio_mapping_exact"]
        and direct_frontier_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


def pairwise_separated(positions: tuple[int, ...], stations: int) -> bool:
    occupied = set(positions)
    return all(
        (station + 1) % stations not in occupied for station in occupied
    )


def derive_event_seeds(program: tuple[object, ...]) -> tuple[tuple[int, State], ...]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        if not (
            after == K.A.apply_semantic(before, allocator)
            and rail_a == (1,) + (0,) * (len(program) - 1)
            and not any(rail_b)
            and len(trace) == len(program)
        ):
            raise AssertionError(("Cycle-719 event seed", event))
        rows.append((event, before))
        state = after
    return tuple(rows)


def frame_map(key: Key, shift: int, stations: int) -> Key:
    k, event, positions = key
    moved = tuple(sorted((station + shift) % stations for station in positions))
    return k, event, moved


def derive_scope() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    stations = len(program)
    event_seeds = derive_event_seeds(program)
    census = tuple(sorted(
        (k, event, positions)
        for k in range(MIN_SOURCES, MAX_SOURCES + 1)
        for positions in combinations(range(stations), k)
        if pairwise_separated(positions, stations)
        for event, _state in event_seeds
    ))
    remaining = set(census)
    orbits = []
    while remaining:
        representative = min(remaining)
        orbit = tuple(sorted({
            frame_map(representative, shift, stations)
            for shift in range(stations)
        }))
        if not set(orbit) <= set(census):
            raise AssertionError(("frame closure", representative))
        orbits.append(orbit)
        remaining.difference_update(orbit)
    result = {
        "program": program,
        "event_seeds": event_seeds,
        "census": census,
        "orbits": tuple(sorted(orbits, key=lambda row: row[0])),
        "stations": stations,
        "population": len(census),
        "per_k_populations": dict(sorted(Counter(key[0] for key in census).items())),
    }
    result["pass"] = (
        stations == 11
        and len(event_seeds) == 4
        and len(census) == 748
        and len(result["orbits"]) == 68
        and all(len(orbit) == 11 for orbit in result["orbits"])
        and set(K3_TRIOS) <= set(census)
    )
    return result


def watched_registers() -> tuple[tuple[str, int], ...]:
    return (
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


def dirty_global_indices() -> tuple[int, ...]:
    banks0, links0 = K.B.chain_genesis(FIXTURE_BANKS)
    zero_banks = tuple(tuple(0 for _bit in bank) for bank in banks0)
    zero_links = tuple(tuple(0 for _bit in link) for link in links0)
    baseline = K.M.pack_state(zero_banks, zero_links)
    indices = {K.R3.X.SOURCE_POINTER}
    for bank_index, _bank in enumerate(zero_banks):
        for _name, wire in watched_registers():
            changed = [list(bank) for bank in zero_banks]
            changed[bank_index][wire] = 1
            marked = K.M.pack_state(
                tuple(tuple(bank) for bank in changed), zero_links
            )
            differences = tuple(
                index
                for index, (left, right) in enumerate(zip(baseline, marked))
                if left != right
            )
            if len(differences) != 1:
                raise AssertionError(("packed bank marker", differences))
            indices.add(differences[0])
    for link_index, link in enumerate(zero_links):
        for wire in range(len(link)):
            changed = [list(row) for row in zero_links]
            changed[link_index][wire] = 1
            marked = K.M.pack_state(
                zero_banks, tuple(tuple(row) for row in changed)
            )
            differences = tuple(
                index
                for index, (left, right) in enumerate(zip(baseline, marked))
                if left != right
            )
            if len(differences) != 1:
                raise AssertionError(("packed link marker", differences))
            indices.add(differences[0])
    return tuple(sorted(indices))


def synchronous_word(
    program: tuple[object, ...], positions0: tuple[int, ...]
) -> tuple[object, ...]:
    positions = tuple(positions0)
    word = []
    for _step in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple(
            (station + 1) % len(program) for station in positions
        )
    return tuple(word)


def build_initial_states(scope: dict[str, object]) -> tuple[tuple[State, ...], int]:
    program = scope["program"]
    census = scope["census"]
    seed_by_event = dict(scope["event_seeds"])
    word_cache = {
        positions: synchronous_word(program, positions)
        for _k, _event, positions in census
    }
    states = []
    failures = 0
    for k, event, positions in census:
        before = seed_by_event[event]
        after, rail_a, rail_b, _trace = K.run_orbit(
            before, program, token_positions=positions
        )
        expected_rail = tuple(
            int(station in positions) for station in range(len(program))
        )
        failures += after != K.A.apply_semantic(before, word_cache[positions])
        failures += rail_a != expected_rail or any(rail_b)
        restored, inverse_a, inverse_b, _ = K.run_orbit(
            after, program, token_positions=positions, reverse=True
        )
        failures += (
            restored != before or inverse_a != rail_a or inverse_b != rail_b
        )
        if len(positions) != k:
            raise AssertionError(("key/source mismatch", k, positions))
        states.append(after)
    return tuple(states), failures


def pack_states(states: tuple[State, ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def compile_masked_gate(gate: object, mask: int) -> tuple[int, int, int, int, int]:
    if gate.kind == "X":
        return (0, gate.wires[0], 0, 0, mask)
    if gate.kind == "CNOT":
        return (1, gate.wires[0], gate.wires[1], 0, mask)
    if gate.kind == "TOF":
        return (2, gate.wires[0], gate.wires[1], gate.wires[2], mask)
    raise ValueError(("unsupported landed gate", gate))


def masked_h_schedules(
    program: tuple[object, ...], census: tuple[Key, ...]
) -> tuple[tuple[tuple[int, int, int, int, int], ...], ...]:
    stations = len(program)
    rows = []
    for step in range(stations):
        schedule = []
        for station, program_row in enumerate(program):
            mask = sum(
                1 << lane
                for lane, (_k, _event, positions) in enumerate(census)
                if (station - step) % stations in positions
            )
            if not mask:
                continue
            schedule.extend(
                compile_masked_gate(gate, mask)
                for gate in K.mapped_macro(program_row)
            )
        rows.append(tuple(schedule))
    return tuple(rows)


def compile_fast_schedules(
    schedules: tuple[tuple[tuple[int, int, int, int, int], ...], ...]
) -> tuple[Callable[[list[int]], None], ...]:
    functions = []
    for schedule in schedules:
        source = ["def apply_chunk(c):"]
        for kind, first, second, third, mask in schedule:
            if kind == 0:
                source.append(f" c[{first}] ^= {mask}")
            elif kind == 1:
                source.append(f" c[{second}] ^= c[{first}] & {mask}")
            else:
                source.append(
                    f" c[{third}] ^= c[{first}] & c[{second}] & {mask}"
                )
        namespace: dict[str, object] = {}
        exec("\n".join(source), {"__builtins__": {}}, namespace)
        functions.append(namespace["apply_chunk"])
    return tuple(functions)  # type: ignore[return-value]


def clean_mask(columns: list[int], dirty_indices: tuple[int, ...], all_mask: int) -> int:
    dirty = 0
    for wire in dirty_indices:
        dirty |= columns[wire]
    return all_mask & ~dirty


def equality_mask(
    columns: list[int], reference: list[int], candidate_mask: int
) -> int:
    differences = 0
    for left, right in zip(columns, reference):
        differences |= left ^ right
    return candidate_mask & ~differences


def lane_numbers(mask: int) -> tuple[int, ...]:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def update_sequence_hash(hasher: object, lane: int, absolute_h: int) -> None:
    hasher.update(lane.to_bytes(2, "big"))
    hasher.update(absolute_h.to_bytes(4, "big"))
    hasher.update(bytes((int(absolute_h % 11 == 0),)))


def scan_ladder(scope: dict[str, object]) -> dict[str, object]:
    """Record every clean H-boundary event and the landed E1/E2 censuses."""

    started = monotonic()
    program = scope["program"]
    census = scope["census"]
    states, initial_failures = build_initial_states(scope)
    simulation_keys = census + (census[0],)
    duplicate_lane = len(census)
    columns = pack_states(states + (states[0],))
    initial_columns = columns.copy()
    schedules = masked_h_schedules(program, simulation_keys)
    fast_schedules = compile_fast_schedules(schedules)
    dirty_indices = dirty_global_indices()
    all_mask = (1 << len(census)) - 1
    simulation_mask = (1 << len(simulation_keys)) - 1
    sequences: list[list[int]] = [[] for _key in census]
    sequence_hasher = sha256()
    e1_first: dict[Key, int] = {}
    e2_first_h: dict[Key, int] = {}
    cycle_periods: dict[Key, int] = {}

    initial_clean_all = clean_mask(columns, dirty_indices, simulation_mask)
    initial_clean = initial_clean_all & all_mask
    determinism_mismatches = int(
        bool(initial_clean_all & 1)
        != bool(initial_clean_all & (1 << duplicate_lane))
    )
    for lane in lane_numbers(initial_clean):
        sequences[lane].append(0)
        update_sequence_hash(sequence_hasher, lane, 0)
        e1_first[census[lane]] = 0
        e2_first_h[census[lane]] = 0
    e1_found = initial_clean
    e2_found = initial_clean
    unresolved_cycle_mask = all_mask & ~initial_clean
    stations = len(program)

    for orbit in range(1, TRAJECTORY_HORIZON + 1):
        orbit_clean = 0
        for step, apply_chunk in enumerate(fast_schedules, 1):
            apply_chunk(columns)
            clean_all = clean_mask(columns, dirty_indices, simulation_mask)
            clean = clean_all & all_mask
            absolute_h = (orbit - 1) * stations + step
            for lane in lane_numbers(clean):
                sequences[lane].append(absolute_h)
                update_sequence_hash(sequence_hasher, lane, absolute_h)
            determinism_mismatches += (
                bool(clean_all & 1)
                != bool(clean_all & (1 << duplicate_lane))
            )
            new_e1 = clean & ~e1_found
            for lane in lane_numbers(new_e1):
                e1_first[census[lane]] = absolute_h
            e1_found |= new_e1
            orbit_clean = clean

        new_e2 = orbit_clean & ~e2_found
        for lane in lane_numbers(new_e2):
            e2_first_h[census[lane]] = orbit * stations
        e2_found |= new_e2

        recurrence = equality_mask(
            columns, initial_columns, unresolved_cycle_mask & ~orbit_clean
        )
        for lane in lane_numbers(recurrence):
            cycle_periods[census[lane]] = orbit
        unresolved_cycle_mask &= ~(orbit_clean | recurrence)

    duplicate_final_exact = all(
        bool(column & 1) == bool(column & (1 << duplicate_lane))
        for column in columns
    )
    frozen_sequences = tuple(tuple(row) for row in sequences)
    depths = tuple(map(len, frozen_sequences))
    annotated_manifest_sha = digest(tuple(
        (
            key,
            tuple((moment, moment % stations == 0) for moment in row),
        )
        for key, row in zip(census, frozen_sequences)
    ))
    result = {
        "sequences": frozen_sequences,
        "depths": depths,
        "e1_first": e1_first,
        "e2_first_h": e2_first_h,
        "cycle_periods": cycle_periods,
        "unresolved_before_orbit_clean": frozenset(
            census[lane] for lane in lane_numbers(unresolved_cycle_mask)
        ),
        "sequence_event_count": sum(depths),
        "orbit_boundary_event_count": sum(
            moment % stations == 0
            for row in frozen_sequences for moment in row
        ),
        "annotated_sequence_manifest_sha256": annotated_manifest_sha,
        "stream_sequence_sha256": sequence_hasher.hexdigest(),
        "initial_build_failures": initial_failures,
        "state_bits": len(states[0]),
        "dirty_coordinate_count": len(dirty_indices),
        "masked_schedule_gate_counts": tuple(map(len, schedules)),
        "determinism_replay": {
            "duplicated_key": census[0],
            "boundary_mismatches": determinism_mismatches,
            "final_full_state_exact": duplicate_final_exact,
        },
        "runtime_seconds": round(monotonic() - started, 6),
    }
    result["pass"] = (
        initial_failures == 0
        and result["state_bits"] == 5815
        and result["dirty_coordinate_count"] == 477
        and result["masked_schedule_gate_counts"] == (3106,) * 11
        and all(
            all(left < right for left, right in zip(row, row[1:]))
            for row in frozen_sequences
        )
        and all(
            (not row) or e1_first[key] == row[0]
            for key, row in zip(census, frozen_sequences)
        )
        and all(
            moment in frozen_sequences[census.index(key)]
            and moment % stations == 0
            for key, moment in e2_first_h.items()
        )
        and determinism_mismatches == 0
        and duplicate_final_exact
    )
    return result


def lane_snapshot_sha(columns: list[int], lane: int) -> str:
    bit = 1 << lane
    return sha256(
        bytes(int(bool(column & bit)) for column in columns)
    ).hexdigest()


def replay_content(
    scope: dict[str, object], expected_depths: tuple[int, ...], max_depth: int
) -> dict[str, object]:
    """Replay the event stream and snapshot only candidate threshold rungs."""

    started = monotonic()
    program = scope["program"]
    census = scope["census"]
    states, initial_failures = build_initial_states(scope)
    simulation_keys = census + (census[0],)
    duplicate_lane = len(census)
    columns = pack_states(states + (states[0],))
    schedules = masked_h_schedules(program, simulation_keys)
    fast_schedules = compile_fast_schedules(schedules)
    dirty_indices = dirty_global_indices()
    all_mask = (1 << len(census)) - 1
    simulation_mask = (1 << len(simulation_keys)) - 1
    target_rungs = tuple(sorted({1, 2, 3, max_depth}))
    content_by_rung: dict[int, dict[Key, str]] = {
        rung: {} for rung in target_rungs
    }
    counts = [0] * len(census)
    sequence_hasher = sha256()
    trio_mark_bits: dict[Key, tuple[int, int]] = {}

    def observe(clean: int, absolute_h: int) -> None:
        for lane in lane_numbers(clean):
            counts[lane] += 1
            rung = counts[lane]
            update_sequence_hash(sequence_hasher, lane, absolute_h)
            if rung in content_by_rung:
                content_by_rung[rung][census[lane]] = lane_snapshot_sha(
                    columns, lane
                )
            if rung == 1 and census[lane] in K3_TRIOS:
                bit = 1 << lane
                trio_mark_bits[census[lane]] = tuple(
                    int(bool(columns[wire] & bit)) for wire in K3_MARK_WIRES
                )

    initial_clean_all = clean_mask(columns, dirty_indices, simulation_mask)
    observe(initial_clean_all & all_mask, 0)
    determinism_mismatches = int(
        bool(initial_clean_all & 1)
        != bool(initial_clean_all & (1 << duplicate_lane))
    )
    stations = len(program)
    for orbit in range(1, TRAJECTORY_HORIZON + 1):
        for step, apply_chunk in enumerate(fast_schedules, 1):
            apply_chunk(columns)
            clean_all = clean_mask(columns, dirty_indices, simulation_mask)
            observe(
                clean_all & all_mask,
                (orbit - 1) * stations + step,
            )
            determinism_mismatches += (
                bool(clean_all & 1)
                != bool(clean_all & (1 << duplicate_lane))
            )

    duplicate_final_exact = all(
        bool(column & 1) == bool(column & (1 << duplicate_lane))
        for column in columns
    )
    result = {
        "target_rungs": target_rungs,
        "content_by_rung": content_by_rung,
        "trio_mark_bits_at_set": trio_mark_bits,
        "depths": tuple(counts),
        "stream_sequence_sha256": sequence_hasher.hexdigest(),
        "initial_build_failures": initial_failures,
        "determinism_replay": {
            "duplicated_key": census[0],
            "boundary_mismatches": determinism_mismatches,
            "final_full_state_exact": duplicate_final_exact,
            "depth_vector_exact": tuple(counts) == expected_depths,
        },
        "runtime_seconds": round(monotonic() - started, 6),
    }
    result["pass"] = (
        initial_failures == 0
        and tuple(counts) == expected_depths
        and all(
            len(content_by_rung[rung])
            == sum(depth >= rung for depth in expected_depths)
            for rung in target_rungs
        )
        and determinism_mismatches == 0
        and duplicate_final_exact
    )
    return result


def certificate_a(scope: dict[str, object], scan: dict[str, object]) -> dict[str, object]:
    census = scope["census"]
    depths = scan["depths"]
    histogram = dict(sorted(Counter(depths).items()))
    per_k = {
        k: dict(sorted(Counter(
            depth for key, depth in zip(census, depths) if key[0] == k
        ).items()))
        for k in range(MIN_SOURCES, MAX_SOURCES + 1)
    }
    result = {
        "certificate": "A_LADDER_CENSUS",
        "census_size": len(census),
        "horizon_orbits_inclusive": TRAJECTORY_HORIZON,
        "horizon_absolute_H_inclusive": TRAJECTORY_HORIZON * scope["stations"],
        "sequence_definition": (
            "for every sorted Cycle-852 key, all clean post-engagement H "
            "boundaries in increasing absolute-H order; each event is "
            "annotated orbit_boundary iff absolute_H mod 11 == 0"
        ),
        "full_per_key_sequence_rows_computed": len(scan["sequences"]),
        "full_annotated_sequence_manifest_sha256":
            scan["annotated_sequence_manifest_sha256"],
        "total_clean_events": scan["sequence_event_count"],
        "orbit_boundary_clean_events": scan["orbit_boundary_event_count"],
        "maximum_depth_reached": max(depths),
        "depth_histogram": histogram,
        "per_k_depth_breakdown": per_k,
        "stage_semantics": (
            "depth 0 never set; depth 1 set only; depth d is set plus d-1 "
            "clean-revisit confirmations"
        ),
    }
    result["pass"] = (
        scope["pass"]
        and scan["pass"]
        and len(depths) == 748
        and sum(histogram.values()) == 748
        and all(sum(rows.values()) == scope["per_k_populations"][k]
                for k, rows in per_k.items())
        and scan["sequence_event_count"] == sum(
            depth * count for depth, count in histogram.items()
        )
    )
    return result


def certificate_b(scope: dict[str, object], scan: dict[str, object]) -> dict[str, object]:
    census = scope["census"]
    stations = scope["stations"]
    sequences = scan["sequences"]
    depths = scan["depths"]
    stage1_moments = {
        key: row[0] for key, row in zip(census, sequences) if row
    }
    first_orbit_clean = {
        key: next(moment for moment in row if moment % stations == 0)
        for key, row in zip(census, sequences)
        if any(moment % stations == 0 for moment in row)
    }
    e2_rungs = {
        key: sequences[census.index(key)].index(moment) + 1
        for key, moment in first_orbit_clean.items()
    }
    rung_histogram = dict(sorted(Counter(e2_rungs.values()).items()))
    e1_set = frozenset(stage1_moments)
    e2_set = frozenset(first_orbit_clean)
    stage2_set = frozenset(
        key for key, depth in zip(census, depths) if depth >= 2
    )
    fixed_rung_matches = tuple(
        rung for rung in range(1, max(depths) + 1)
        if frozenset(
            key for key, depth in zip(census, depths) if depth >= rung
        ) == e2_set
    )
    result = {
        "certificate": "B_STAGE_IDENTIFICATION",
        "stage1_count": len(stage1_moments),
        "landed_E1_count": len(scan["e1_first"]),
        "stage1_equals_E1_moment_exact": stage1_moments == scan["e1_first"],
        "stage1_moment_sha256": digest(tuple(sorted(stage1_moments.items()))),
        "stage1_key_sha256": digest(tuple(sorted(e1_set))),
        "first_orbit_boundary_clean_count": len(first_orbit_clean),
        "landed_E2_count": len(scan["e2_first_h"]),
        "first_orbit_clean_equals_E2_moment_exact":
            first_orbit_clean == scan["e2_first_h"],
        "E2_moment_sha256": digest(tuple(sorted(first_orbit_clean.items()))),
        "E2_key_sha256": digest(tuple(sorted(e2_set))),
        "literal_stage2_count": len(stage2_set),
        "literal_stage2_equals_E2": stage2_set == e2_set,
        "E2_landed_rung_histogram": rung_histogram,
        "fixed_per_H_rungs_reproducing_E2": fixed_rung_matches,
        "exact_relation": (
            "E1 is exactly per-H rung 1. E2 is exactly the first clean event "
            "whose H boundary is an orbit boundary; its per-H rung is key-"
            "dependent and is given by E2_landed_rung_histogram."
        ),
    }
    result["pass"] = (
        result["stage1_equals_E1_moment_exact"]
        and len(e1_set) == LANDED_E1_STAMPED
        and result["stage1_key_sha256"]
            == "1901e01751642cf1cd04054ab011fe39b9d384488b07c419e7b9a7e041b7ce52"
        and result["first_orbit_clean_equals_E2_moment_exact"]
        and len(e2_set) == LANDED_E2_STAMPED
        and result["E2_key_sha256"]
            == "bea94bc5b3fb7e4d41cdaa32e565e8f659d40dae17c3c44934bb0ebd0da4181a"
        and set(e2_rungs) == e2_set
        and sum(rung_histogram.values()) == LANDED_E2_STAMPED
    )
    return result


def certificate_c(
    scope: dict[str, object],
    scan: dict[str, object],
    content: dict[str, object],
) -> dict[str, object]:
    census = scope["census"]
    depths_by_key = dict(zip(census, scan["depths"]))
    e1_set = frozenset(scan["e1_first"])
    e2_set = frozenset(scan["e2_first_h"])
    e1_only = e1_set - e2_set
    cycle_keys = frozenset(scan["cycle_periods"])
    trio_rows = tuple({
        "key": key,
        "set_absolute_H": scan["e1_first"].get(key),
        "depth": depths_by_key[key],
        "confirmations": max(0, depths_by_key[key] - 1),
        "mark_bits_256_262": content["trio_mark_bits_at_set"].get(key),
        "Cycle849_D3_mark_true":
            len(set(content["trio_mark_bits_at_set"].get(key, (0, 1)))) == 1,
    } for key in K3_TRIOS)

    orbit_rows = []
    absolute_orbits = []
    mixed_orbits = []
    for orbit in scope["orbits"]:
        stamped_count = sum(key in e1_set for key in orbit)
        if stamped_count == len(orbit):
            absolute_orbits.append(orbit)
        elif stamped_count:
            mixed_orbits.append(orbit)
    probe_orbits = tuple(absolute_orbits) + tuple(mixed_orbits[:3])
    correlation = Counter()
    for orbit in probe_orbits:
        degree = sum(orbit[0] in {
            key for key in census
            if frame_map(key, monitor, scope["stations"]) in e1_set
        } for monitor in range(scope["stations"]))
        depth_hist = Counter(depths_by_key[key] for key in orbit)
        for key in orbit:
            direct_degree = sum(
                frame_map(key, monitor, scope["stations"]) in e1_set
                for monitor in range(scope["stations"])
            )
            if direct_degree != degree:
                raise AssertionError(("monitor degree varies in orbit", orbit[0]))
            correlation[(direct_degree, depths_by_key[key])] += 1
        orbit_rows.append({
            "class": "absolute-record" if orbit in absolute_orbits else "mixed",
            "representative": orbit[0],
            "stamped_under_m_monitors_degree": degree,
            "ladder_depth_histogram": dict(sorted(depth_hist.items())),
        })
    depths_by_degree: dict[int, set[int]] = defaultdict(set)
    for (degree, depth), count in correlation.items():
        if count:
            depths_by_degree[degree].add(depth)
    relation = (
        "monitor degree does not determine ladder depth on the probe"
        if any(len(values) > 1 for values in depths_by_degree.values()) else
        "monitor degree determines ladder depth on the probe"
    )
    result = {
        "certificate": "C_TIER_REINTERPRETATION",
        "Cycle849_k3_trios": trio_rows,
        "k3_trios_set_but_unconfirmed": all(
            row["depth"] == 1 and row["Cycle849_D3_mark_true"]
            for row in trio_rows
        ),
        "E1_only_count": len(e1_only),
        "E1_only_set_never_confirmed": all(
            depths_by_key[key] == 1 for key in e1_only
        ),
        "zero_record_cycle_count": len(cycle_keys),
        "zero_record_cycles_never_set": all(
            depths_by_key[key] == 0 for key in cycle_keys
        ),
        "monitor_probe_policy": (
            "all three lexicographically ordered E1 absolute-record orbits "
            "plus the first three lexicographically ordered E1 mixed orbits"
        ),
        "absolute_record_orbit_count": len(absolute_orbits),
        "mixed_orbit_count": len(mixed_orbits),
        "monitor_probe_orbits": tuple(orbit_rows),
        "monitor_degree_ladder_depth_correlation": tuple(
            {"monitor_degree": degree, "ladder_depth": depth, "keys": count}
            for (degree, depth), count in sorted(correlation.items())
        ),
        "monitor_degree_relation": relation,
    }
    result["pass"] = (
        result["k3_trios_set_but_unconfirmed"]
        and len(e1_only) == 68
        and result["E1_only_set_never_confirmed"]
        and len(cycle_keys) == 20
        and result["zero_record_cycles_never_set"]
        and len(absolute_orbits) == 3
        and len(mixed_orbits) == 53
        and len(probe_orbits) == 6
        and sum(correlation.values()) == 66
        and all(row["stamped_under_m_monitors_degree"] == 11
                for row in orbit_rows[:3])
        and all(0 < row["stamped_under_m_monitors_degree"] < 11
                for row in orbit_rows[3:])
    )
    return result


def certificate_d(
    scope: dict[str, object],
    scan: dict[str, object],
    content: dict[str, object],
    cert_b: dict[str, object],
) -> dict[str, object]:
    census = scope["census"]
    depths = scan["depths"]
    max_depth = max(depths)
    candidates = (
        ("n=1", 1),
        ("n=2", 2),
        ("n=3", 3),
        (f"max_reached={max_depth}", max_depth),
    )
    record_sets = {
        label: frozenset(
            key for key, depth in zip(census, depths) if depth >= rung
        )
        for label, rung in candidates
    }
    threshold_rows = tuple({
        "threshold": label,
        "rung": rung,
        "record_count": len(record_sets[label]),
        "record_key_sha256": digest(tuple(sorted(record_sets[label]))),
        "reproduces_E1": record_sets[label] == frozenset(scan["e1_first"]),
        "reproduces_E2": record_sets[label] == frozenset(scan["e2_first_h"]),
        "distinct_content_classes_at_lock": len(set(
            content["content_by_rung"][rung].values()
        )),
    } for label, rung in candidates)
    pair_rows = []
    for left_index, (left_label, left_rung) in enumerate(candidates):
        for right_label, right_rung in candidates[left_index + 1:]:
            left_set = record_sets[left_label]
            right_set = record_sets[right_label]
            shared = left_set & right_set
            same = sum(
                content["content_by_rung"][left_rung][key]
                == content["content_by_rung"][right_rung][key]
                for key in shared
            )
            different = len(shared) - same
            left_only = len(left_set - right_set)
            right_only = len(right_set - left_set)
            pair_rows.append({
                "threshold_pair": (left_label, right_label),
                "left_only_records": left_only,
                "right_only_records": right_only,
                "shared_content_equal": same,
                "shared_content_different": different,
                "content_equal_across_rungs": different == 0,
                "readout_additivity_distinguishes": bool(
                    left_only or right_only or different
                ),
            })
    result = {
        "certificate": "D_THRESHOLD_STRUCTURE",
        "threshold_table": threshold_rows,
        "fixed_per_H_rungs_reproducing_E2":
            cert_b["fixed_per_H_rungs_reproducing_E2"],
        "E2_reproducing_rung_definition":
            "first clean event at an orbit-return H boundary",
        "content_snapshot_comparisons": tuple(pair_rows),
        "readout_statement": (
            "For each pair, a lower-only record permits a content-determined "
            "additive witness supported on that content; a shared history "
            "with different lock snapshots permits a value separating those "
            "contents. Counts are reported without choosing a value function."
        ),
        "actual_current_surface_status": "open",
        "model_layer": "N6 record-production-model slot",
        "axiom_surface_touched": False,
        "threshold_forced": False,
        "threshold_disposition": (
            "The landed dynamics distinguishes candidate dials but supplies "
            "no normative rule selecting one; threshold remains an owner dial."
        ),
    }
    result["pass"] = (
        record_sets["n=1"] == frozenset(scan["e1_first"])
        and all(
            len(content["content_by_rung"][rung])
            == len(record_sets[label])
            for label, rung in candidates
        )
        and all(
            record_sets[right_label] <= record_sets[left_label]
            for left_index, (left_label, left_rung) in enumerate(candidates)
            for right_label, right_rung in candidates[left_index + 1:]
            if left_rung <= right_rung
        )
        and not result["axiom_surface_touched"]
        and not result["threshold_forced"]
    )
    return result


def public_scan(scan: dict[str, object]) -> dict[str, object]:
    return {
        key: value for key, value in scan.items()
        if key not in {
            "sequences", "depths", "e1_first", "e2_first_h",
            "cycle_periods", "unresolved_before_orbit_clean",
        }
    }


def public_content(content: dict[str, object]) -> dict[str, object]:
    return {
        "target_rungs": content["target_rungs"],
        "content_counts_by_rung": {
            rung: len(rows)
            for rung, rows in content["content_by_rung"].items()
        },
        "content_digests_by_rung": {
            rung: digest(tuple(sorted(rows.items())))
            for rung, rows in content["content_by_rung"].items()
        },
        "trio_mark_bits_at_set": content["trio_mark_bits_at_set"],
        "stream_sequence_sha256": content["stream_sequence_sha256"],
        "initial_build_failures": content["initial_build_failures"],
        "determinism_replay": content["determinism_replay"],
        "runtime_seconds": content["runtime_seconds"],
        "pass": content["pass"],
    }


def main() -> int:
    started = monotonic()
    controls_pre = source_controls()
    scope = derive_scope()
    scan = scan_ladder(scope)
    cert_a = certificate_a(scope, scan)
    cert_b = certificate_b(scope, scan)
    content = replay_content(scope, scan["depths"], cert_a["maximum_depth_reached"])
    cert_c = certificate_c(scope, scan, content)
    cert_d = certificate_d(scope, scan, content, cert_b)
    controls_post = source_controls()
    elapsed = monotonic() - started
    replay_exact = (
        scan["stream_sequence_sha256"] == content["stream_sequence_sha256"]
        and scan["depths"] == content["depths"]
    )
    checks = {
        "A_LADDER_CENSUS": cert_a["pass"],
        "B_STAGE_IDENTIFICATION": cert_b["pass"],
        "C_TIER_REINTERPRETATION": cert_c["pass"],
        "D_THRESHOLD_STRUCTURE": cert_d["pass"],
        "E_CONTROLS": (
            controls_pre["pass"]
            and controls_post["pass"]
            and controls_pre == controls_post
            and replay_exact
            and scan["determinism_replay"]["boundary_mismatches"] == 0
            and scan["determinism_replay"]["final_full_state_exact"]
            and content["determinism_replay"]["boundary_mismatches"] == 0
            and content["determinism_replay"]["final_full_state_exact"]
            and elapsed < AUDIT_TIMEOUT_SEC
            and not PRIMARY_FIREWALL.hits
        ),
    }
    threshold_counts = {
        row["threshold"]: row["record_count"]
        for row in cert_d["threshold_table"]
    }
    findings = (
        "FINDING A_LADDER_CENSUS :: full 748-key ordered clean-event "
        f"sequences through orbit {TRAJECTORY_HORIZON} computed with orbit-"
        f"boundary annotations; depth histogram={compact(cert_a['depth_histogram'])}; "
        f"per-k={compact(cert_a['per_k_depth_breakdown'])}; manifest_sha256="
        f"{cert_a['full_annotated_sequence_manifest_sha256']}",
        "FINDING B_STAGE_IDENTIFICATION :: stage-1 moments == E1 exactly "
        f"({cert_b['stage1_count']}, moment-exact); first orbit-boundary clean "
        f"== E2 exactly ({cert_b['first_orbit_boundary_clean_count']}, moment-"
        f"exact); literal per-H stage-2 == E2 is "
        f"{cert_b['literal_stage2_equals_E2']}; E2 rung histogram="
        f"{compact(cert_b['E2_landed_rung_histogram'])}; fixed per-H rungs "
        f"reproducing E2={cert_b['fixed_per_H_rungs_reproducing_E2']}",
        "FINDING C_TIER_REINTERPRETATION :: six k=3 trios are set-only with "
        f"Cycle-849 D3 marks at set={cert_c['k3_trios_set_but_unconfirmed']}; "
        f"68 E1-only are set-never-confirmed="
        f"{cert_c['E1_only_set_never_confirmed']}; 20 zero-record cycles are "
        f"never-set={cert_c['zero_record_cycles_never_set']}; monitor-degree/"
        f"depth correlation={compact(cert_c['monitor_degree_ladder_depth_correlation'])}; "
        f"relation={cert_c['monitor_degree_relation']}",
        "FINDING D_THRESHOLD_STRUCTURE :: induced record counts="
        f"{compact(threshold_counts)}; fixed E2 rung="
        f"{cert_d['fixed_per_H_rungs_reproducing_E2']}; E2 instead uses first "
        "orbit-boundary clean; content-snapshot comparison="
        f"{compact(cert_d['content_snapshot_comparisons'])}; threshold remains "
        "a model-layer dial; no axiom surface touched",
        "FINDING E_CONTROLS :: SHA-pinned literal worktree-relative "
        "AUDIT_INPUT_PATHS exist; Cycle-852/856/860 and historical Cycle-849 "
        "cited primaries BLOCKLIST text/AST only; complete dynamics replay "
        "exact; runtime < 1400s; stdout < 150KB",
    )
    report = {
        "cycle": 861,
        "checks": checks,
        "A_LADDER_CENSUS": cert_a,
        "B_STAGE_IDENTIFICATION": cert_b,
        "C_TIER_REINTERPRETATION": cert_c,
        "D_THRESHOLD_STRUCTURE": cert_d,
        "E_CONTROLS": {
            **controls_post,
            "scan": public_scan(scan),
            "content_replay": public_content(content),
            "complete_dynamics_replay_exact": replay_exact,
            "runtime_under_1400s": elapsed < AUDIT_TIMEOUT_SEC,
            "stdout_under_150KB": None,
        },
        "runtime_seconds": round(elapsed, 6),
        "actual_current_surface_status": "open",
        "pass": all(checks.values()),
    }
    preliminary_lines = tuple(
        f"CERTIFICATE {name} {'PASS' if passed else 'FAIL'} :: {passed}"
        for name, passed in checks.items()
    ) + findings
    preliminary = (
        "\n".join(preliminary_lines)
        + "\nSUMMARY_JSON " + compact(report) + "\n"
    )
    stdout_ok = len(preliminary.encode("utf-8")) < STDOUT_LIMIT_BYTES
    report["E_CONTROLS"]["stdout_under_150KB"] = stdout_ok
    checks["E_CONTROLS"] = checks["E_CONTROLS"] and stdout_ok
    report["pass"] = all(checks.values())
    report["report_sha256"] = digest({
        key: value for key, value in report.items() if key != "report_sha256"
    })
    final_lines = tuple(
        f"CERTIFICATE {name} {'PASS' if passed else 'FAIL'} :: {passed}"
        for name, passed in checks.items()
    ) + findings
    output = "\n".join(final_lines) + "\nSUMMARY_JSON " + compact(report) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
