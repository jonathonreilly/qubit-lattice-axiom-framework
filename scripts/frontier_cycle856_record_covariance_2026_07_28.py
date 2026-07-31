#!/usr/bin/env python3
"""Cycle 856: exact monitor-covariance test for Cycle-852 records.

Cycle 852 fixes the cut of the eleven-station controller orbit at phase zero.
Here ``stamped_m(key)`` moves that cut to monitor phase ``m``: both the
engagement orbit and every later H chunk begin with the sources advanced by
``m`` stations.  Thus ``m=0`` is exactly the landed Cycle-852 implementation.

The Cycle-852 runner is a SHA-pinned, text/AST-only specification primary.  We
rebuild its needed census, initial states, schedules, clean predicate, horizon,
and E1/E2 cadence directly from the landed Cycle-719 computational core.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Callable


AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle852_selection_tournament_2026_07_28.py",
)
COMPUTATIONAL_INPUT_PATHS = (AUDIT_INPUT_PATHS[0],)
TEXT_AST_ONLY_PATHS = (AUDIT_INPUT_PATHS[1],)
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "fcb1e5ad22e48dc865754bc0a0f5357cdef8e78b477c21f48b74e5971eaa8419",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "d584154f32ead0a03a9661c6f176d52b2a1a77dc",
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if the cited Cycle-852 specification is imported."""

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
E2_LANDED_RULE = "record set = first-clean orbit-return selection-event set"


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


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


def source_controls() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=Path(__file__).name,
    )
    sha_rows = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    blob_rows = {path: git_blob(payload) for path, payload in payloads.items()}
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    landed_tree = trees[AUDIT_INPUT_PATHS[1]]
    landed_literals = {
        name: literal_assignment(landed_tree, name)
        for name in (
            "FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES",
            "TRAJECTORY_HORIZON", "E2_LANDED_RULE",
        )
    }
    expected_literals = {
        "FIXTURE_BANKS": FIXTURE_BANKS,
        "MIN_SOURCES": MIN_SOURCES,
        "MAX_SOURCES": MAX_SOURCES,
        "TRAJECTORY_HORIZON": TRAJECTORY_HORIZON,
        "E2_LANDED_RULE": E2_LANDED_RULE,
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
        "computational_inputs": COMPUTATIONAL_INPUT_PATHS,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "text_AST_parsed_top_level_counts": {
            path: len(tree.body) for path, tree in trees.items()
        },
        "landed_cycle852_literals": landed_literals,
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
        and all(result["text_AST_parsed_top_level_counts"].values())
        and landed_literals == expected_literals
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


def derive_event_seeds(
    program: tuple[object, ...],
) -> tuple[tuple[int, State], ...]:
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
        "per_k_populations": dict(sorted(Counter(k for k, _e, _p in census).items())),
    }
    result["pass"] = (
        stations == 11
        and len(event_seeds) == 4
        and len(census) == 748
        and len(result["orbits"]) == 68
        and all(len(orbit) == 11 for orbit in result["orbits"])
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


def build_initial_states(scope: dict[str, object]) -> tuple[State, ...]:
    program = scope["program"]
    census = scope["census"]
    seed_by_event = dict(scope["event_seeds"])
    word_cache = {
        positions: synchronous_word(program, positions)
        for _k, _event, positions in census
    }
    states = []
    for k, event, positions in census:
        before = seed_by_event[event]
        after, rail_a, rail_b, _trace = K.run_orbit(
            before, program, token_positions=positions
        )
        expected_rail = tuple(
            int(station in positions) for station in range(len(program))
        )
        if after != K.A.apply_semantic(before, word_cache[positions]):
            raise AssertionError(("composition", k, event, positions))
        if rail_a != expected_rail or any(rail_b):
            raise AssertionError(("rail return", k, event, positions))
        states.append(after)
    return tuple(states)


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
    """Compile the exact Cycle-852 H chunks for the bit-sliced census."""

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
    """Specialize the fixed audited tuple schedules to direct assignments."""

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


def clean_mask(
    columns: list[int], dirty_indices: tuple[int, ...], all_mask: int
) -> int:
    dirty = 0
    for wire in dirty_indices:
        dirty |= columns[wire]
    return all_mask & ~dirty


def lane_numbers(mask: int) -> tuple[int, ...]:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def base_stamp_census(scope: dict[str, object]) -> dict[str, object]:
    """Recompute only the landed Cycle-852 E1/E2 stamp predicates.

    The expensive Cycle-852 merger, basin, state-weight, and cycle-period
    tournaments are irrelevant to record covariance and deliberately omitted.
    A duplicate of census lane zero is nevertheless evolved and observed at
    every E1/E2 boundary as an exact determinism replay.
    """

    started = monotonic()
    program = scope["program"]
    census = scope["census"]
    states = build_initial_states(scope)
    simulation_keys = census + (census[0],)
    duplicate_lane = len(census)
    columns = pack_states(states + (states[0],))
    schedules = masked_h_schedules(program, simulation_keys)
    fast_schedules = compile_fast_schedules(schedules)
    dirty_indices = dirty_global_indices()
    all_mask = (1 << len(census)) - 1
    simulation_mask = (1 << len(simulation_keys)) - 1

    initial_clean_all = clean_mask(columns, dirty_indices, simulation_mask)
    e1_found_mask = initial_clean_all & all_mask
    e2_found_mask = e1_found_mask
    determinism_mismatches = int(
        bool(initial_clean_all & 1)
        != bool(initial_clean_all & (1 << duplicate_lane))
    )

    for _orbit in range(1, TRAJECTORY_HORIZON + 1):
        for apply_chunk in fast_schedules:
            apply_chunk(columns)
            clean_all = clean_mask(columns, dirty_indices, simulation_mask)
            e1_found_mask |= clean_all & all_mask
            determinism_mismatches += (
                bool(clean_all & 1)
                != bool(clean_all & (1 << duplicate_lane))
            )
        e2_found_mask |= clean_all & all_mask

    duplicate_final_exact = all(
        bool(column & 1) == bool(column & (1 << duplicate_lane))
        for column in columns
    )
    e1 = frozenset(census[lane] for lane in lane_numbers(e1_found_mask))
    e2 = frozenset(census[lane] for lane in lane_numbers(e2_found_mask))
    state_catalog_sha256 = digest(tuple(
        sha256(bytes(state)).hexdigest() for state in states
    ))
    result = {
        "E1_stamped": e1,
        "E2_stamped": e2,
        "E1_stamped_count": len(e1),
        "E2_stamped_count": len(e2),
        "E1_stamped_sha256": digest(tuple(sorted(e1))),
        "E2_stamped_sha256": digest(tuple(sorted(e2))),
        "state_catalog_sha256": state_catalog_sha256,
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
        len(e1) == 182
        and len(e2) == 114
        and e2 <= e1
        and result["E1_stamped_sha256"]
            == "1901e01751642cf1cd04054ab011fe39b9d384488b07c419e7b9a7e041b7ce52"
        and result["E2_stamped_sha256"]
            == "bea94bc5b3fb7e4d41cdaa32e565e8f659d40dae17c3c44934bb0ebd0da4181a"
        and state_catalog_sha256
            == "92d2be9fa831eacea635faf96d2e9c456063da7336e45f62beff6f840b9f1287"
        and result["state_bits"] == 5815
        and result["dirty_coordinate_count"] == 477
        and result["masked_schedule_gate_counts"] == (3106,) * 11
        and determinism_mismatches == 0
        and duplicate_final_exact
    )
    return result


def monitor_schedule_manifest(
    key: Key, monitor: int, stations: int
) -> tuple[tuple[int, ...], ...]:
    """Program-row indices applied at each chunk of a monitor-rooted orbit."""

    positions = key[2]
    return tuple(
        tuple(sorted(
            (position + monitor + step) % stations
            for position in positions
        ))
        for step in range(stations)
    )


def monitor_lift(scope: dict[str, object]) -> dict[str, object]:
    """Verify the phase lift before using it to transport stamp sets.

    Cycle 852 exposes only phase zero.  Its schedule is completely determined
    by the ordered program rows occupied in each H chunk.  This test compares
    those exact row manifests for every key, monitor phase, and chunk; event
    labels are also required unchanged.  Equality makes the initial orbit and
    every later state boundary identical, not merely the final Boolean stamp.
    """

    census = scope["census"]
    stations = scope["stations"]
    failures = []
    comparisons = 0
    composition_failures = []
    for key in census:
        for monitor in range(stations):
            moved = frame_map(key, monitor, stations)
            left = monitor_schedule_manifest(key, monitor, stations)
            right = monitor_schedule_manifest(moved, 0, stations)
            comparisons += stations
            if left != right and len(failures) < 12:
                failures.append((key, monitor, left, right))
            if moved[1] != key[1] and len(failures) < 12:
                failures.append(("event-label", key, monitor, moved))
            for shift in range(stations):
                composed = frame_map(
                    frame_map(key, shift, stations), monitor, stations
                )
                expected = frame_map(key, monitor + shift, stations)
                if composed != expected and len(composition_failures) < 12:
                    composition_failures.append(
                        (key, monitor, shift, composed, expected)
                    )
    result = {
        "implementation_scope": (
            "Cycle 852 hard-codes monitor phase m=0; Cycle 856 exposes the "
            "honestly supported cyclic cut by advancing the occupied program "
            "rows in both the engagement orbit and later monitoring schedule"
        ),
        "manifest_semantics": (
            "each tuple is the ordered set of SHA-pinned Cycle-719 program "
            "rows whose mapped macros execute at one H boundary"
        ),
        "schedule_chunk_comparisons": comparisons,
        "schedule_manifest_failures": tuple(failures),
        "C11_action_composition_failures": tuple(composition_failures),
    }
    result["pass"] = not failures and not composition_failures
    return result


def monitor_stamp_sets(
    scope: dict[str, object], base: dict[str, object]
) -> dict[str, dict[int, Selection]]:
    census = scope["census"]
    stations = scope["stations"]
    return {
        reading: {
            monitor: frozenset(
                key for key in census
                if frame_map(key, monitor, stations) in base_selection
            )
            for monitor in range(stations)
        }
        for reading, base_selection in (
            ("E1", base["E1_stamped"]),
            ("E2", base["E2_stamped"]),
        )
    }


def mixed_orbit_report(
    scope: dict[str, object], base: dict[str, object]
) -> dict[str, object]:
    stations = scope["stations"]
    readings = {
        "E1": base["E1_stamped"],
        "E2": base["E2_stamped"],
    }
    tables = {}
    offset_rows: dict[int, dict[str, object]] = {}
    for reading, selection in readings.items():
        classes = Counter()
        count_histogram = Counter()
        for orbit_index, orbit in enumerate(scope["orbits"]):
            representative = orbit[0]
            offsets = tuple(
                shift for shift in range(stations)
                if frame_map(representative, shift, stations) in selection
            )
            count = len(offsets)
            orbit_class = (
                "uniformly-stamped" if count == stations else
                "uniformly-silent" if count == 0 else
                "MIXED"
            )
            classes[orbit_class] += 1
            count_histogram[count] += 1
            if orbit_class == "MIXED":
                row = offset_rows.setdefault(orbit_index, {
                    "orbit_index": orbit_index,
                    "representative": representative,
                })
                row[f"{reading}_stamped_offsets"] = offsets
        tables[reading] = {
            "stamped_setup_count": len(selection),
            "uniformly_stamped_orbits": classes["uniformly-stamped"],
            "uniformly_silent_orbits": classes["uniformly-silent"],
            "MIXED_orbits": classes["MIXED"],
            "stamped_members_per_orbit_histogram": dict(sorted(count_histogram.items())),
        }
    rows = []
    for orbit_index in sorted(offset_rows):
        row = offset_rows[orbit_index]
        row.setdefault("E1_stamped_offsets", ())
        row.setdefault("E2_stamped_offsets", ())
        rows.append(row)
    result = {
        "orbit_offset_encoding": (
            "offset g denotes frame_map(representative,g,11); rows are the "
            "union of orbits MIXED under E1 or E2"
        ),
        "by_reading": tables,
        "mixed_orbit_census": tuple(rows),
    }
    result["pass"] = (
        tables["E1"]["stamped_setup_count"] == 182
        and tables["E2"]["stamped_setup_count"] == 114
        and tables["E1"]["uniformly_stamped_orbits"] == 3
        and tables["E1"]["uniformly_silent_orbits"] == 12
        and tables["E1"]["MIXED_orbits"] == 53
        and tables["E2"]["uniformly_stamped_orbits"] == 0
        and tables["E2"]["uniformly_silent_orbits"] == 38
        and tables["E2"]["MIXED_orbits"] == 30
        and all(
            row["uniformly_stamped_orbits"]
            + row["uniformly_silent_orbits"]
            + row["MIXED_orbits"] == 68
            for row in tables.values()
        )
    )
    return result


def intertwining_report(
    scope: dict[str, object],
    monitor_sets: dict[str, dict[int, Selection]],
    lift: dict[str, object],
) -> dict[str, object]:
    census = scope["census"]
    stations = scope["stations"]
    witnesses = []
    comparisons = 0
    for reading, by_monitor in monitor_sets.items():
        for monitor in range(stations):
            for shift in range(stations):
                transformed_monitor = (monitor + shift) % stations
                for key in census:
                    left = frame_map(key, shift, stations) in by_monitor[monitor]
                    right = key in by_monitor[transformed_monitor]
                    comparisons += 1
                    if left != right and len(witnesses) < 20:
                        witnesses.append({
                            "reading": reading,
                            "monitor": monitor,
                            "rotation": shift,
                            "key": key,
                            "left": left,
                            "right": right,
                        })
    holds = lift["pass"] and not witnesses
    result = {
        "identity": "stamped_m(g·key) == stamped_{g·m}(key)",
        "monitor_action": "g·m = (m + g) mod 11",
        "stamp_comparisons": comparisons,
        "schedule_lift": lift,
        "witnesses": tuple(witnesses),
        "verdict": (
            "MONITOR_COVARIANT" if holds else
            "DEEPER_NON_COVARIANCE_IN_CYCLE852_PHASE_LIFT"
        ),
        "interpretation": (
            "fixed-monitor symmetry breaking only; no deeper non-covariance "
            "at the exact Cycle-852 schedule/clean-predicate granularity"
            if holds else
            "the transformed monitor does not restore the declared C_11 action"
        ),
    }
    result["pass"] = holds
    return result


def monitor_dependence_report(
    scope: dict[str, object],
    monitor_sets: dict[str, dict[int, Selection]],
) -> dict[str, object]:
    census = scope["census"]
    table = tuple({
        "monitor": monitor,
        "E1_stamped": len(monitor_sets["E1"][monitor]),
        "E2_stamped": len(monitor_sets["E2"][monitor]),
    } for monitor in range(scope["stations"]))
    absolute = {
        reading: frozenset.intersection(*by_monitor.values())
        for reading, by_monitor in monitor_sets.items()
    }
    absolute_rows = {
        reading: {
            "count": len(selection),
            "keys": tuple(sorted(selection)),
            "key_sha256": digest(tuple(sorted(selection))),
        }
        for reading, selection in absolute.items()
    }
    result = {
        "monitor_table": table,
        "count_dependence": {
            reading: max(map(len, by_monitor.values()))
                - min(map(len, by_monitor.values()))
            for reading, by_monitor in monitor_sets.items()
        },
        "membership_dependence": {
            reading: len({digest(tuple(sorted(selection)))
                          for selection in by_monitor.values()})
            for reading, by_monitor in monitor_sets.items()
        },
        "absolute_records_stamped_under_every_monitor": absolute_rows,
        "absolute_under_both_readings": tuple(sorted(
            absolute["E1"] & absolute["E2"]
        )),
    }
    result["pass"] = (
        all(row["E1_stamped"] == 182 for row in table)
        and all(row["E2_stamped"] == 114 for row in table)
        and result["count_dependence"] == {"E1": 0, "E2": 0}
        and result["membership_dependence"] == {"E1": 11, "E2": 11}
        and absolute_rows["E1"]["count"] == 33
        and absolute_rows["E2"]["count"] == 0
        and not result["absolute_under_both_readings"]
    )
    return result


def public_base(base: dict[str, object]) -> dict[str, object]:
    return {
        key: value for key, value in base.items()
        if key not in {"E1_stamped", "E2_stamped"}
    }


def main() -> int:
    started = monotonic()
    controls_pre = source_controls()
    scope = derive_scope()
    base = base_stamp_census(scope)
    lift = monitor_lift(scope)
    monitor_sets = monitor_stamp_sets(scope, base)
    mixed = mixed_orbit_report(scope, base)
    intertwining = intertwining_report(scope, monitor_sets, lift)
    dependence = monitor_dependence_report(scope, monitor_sets)

    # Pure analysis replay is independent of the simultaneously duplicated
    # exact-dynamics lane used inside base_stamp_census.
    replay_mixed = mixed_orbit_report(scope, base)
    replay_lift = monitor_lift(scope)
    replay_sets = monitor_stamp_sets(scope, base)
    replay_intertwining = intertwining_report(scope, replay_sets, replay_lift)
    replay_dependence = monitor_dependence_report(scope, replay_sets)
    analysis_replay_exact = (
        digest(mixed) == digest(replay_mixed)
        and digest(intertwining) == digest(replay_intertwining)
        and digest(dependence) == digest(replay_dependence)
        and monitor_sets == replay_sets
    )
    controls_post = source_controls()
    elapsed = monotonic() - started
    checks = {
        "A_MIXED_ORBITS": scope["pass"] and base["pass"] and mixed["pass"],
        "B_THE_INTERTWINING_TEST": intertwining["pass"],
        "C_THE_MONITOR_DEPENDENCE_TABLE": dependence["pass"],
        "D_CONTROLS": (
            controls_pre["pass"]
            and controls_post["pass"]
            and controls_pre == controls_post
            and base["determinism_replay"]["boundary_mismatches"] == 0
            and base["determinism_replay"]["final_full_state_exact"]
            and analysis_replay_exact
            and elapsed < AUDIT_TIMEOUT_SEC
            and not PRIMARY_FIREWALL.hits
        ),
    }
    report = {
        "checks": checks,
        "A_MIXED_ORBITS": mixed,
        "B_THE_INTERTWINING_TEST": intertwining,
        "C_THE_MONITOR_DEPENDENCE_TABLE": dependence,
        "D_CONTROLS": {
            **controls_post,
            "base_stamp_recomputation": public_base(base),
            "exact_dynamics_determinism_replay": base["determinism_replay"],
            "analysis_replay_exact": analysis_replay_exact,
            "runtime_under_1400s": elapsed < AUDIT_TIMEOUT_SEC,
            "stdout_under_150KB": None,
        },
        "runtime_seconds": round(elapsed, 6),
        "pass": all(checks.values()),
    }
    findings = (
        "FINDING A_MIXED_ORBITS :: "
        f"E1 stamped=182, orbit classes={compact(mixed['by_reading']['E1'])}; "
        f"E2 stamped=114, orbit classes={compact(mixed['by_reading']['E2'])}",
        "FINDING A_MIXED_ORBITS MIXED_CENSUS :: "
        + compact(mixed["mixed_orbit_census"]),
        "FINDING B_THE_INTERTWINING_TEST :: "
        f"{intertwining['verdict']}; {intertwining['identity']} for all "
        f"{intertwining['stamp_comparisons']} reading/key/monitor/rotation "
        f"cases; {intertwining['interpretation']}; implementation scope: "
        f"{lift['implementation_scope']}",
        "FINDING C_THE_MONITOR_DEPENDENCE_TABLE :: table="
        + compact(dependence["monitor_table"])
        + "; absolute records="
        + compact(dependence["absolute_records_stamped_under_every_monitor"]),
        "FINDING D_CONTROLS :: SHA-pinned literal worktree-relative inputs; "
        "Cycle-852 cited primary BLOCKLIST text/AST only; simultaneous exact-"
        "dynamics duplicate plus analysis replay; runtime < 1400s; stdout < 150KB",
    )
    preliminary_lines = tuple(
        f"{'PASS' if passed else 'FAIL'} {name} :: {passed}"
        for name, passed in checks.items()
    ) + findings
    preliminary = (
        "\n".join(preliminary_lines)
        + "\nSUMMARY_JSON " + compact(report) + "\n"
    )
    stdout_ok = len(preliminary.encode("utf-8")) < STDOUT_LIMIT_BYTES
    report["D_CONTROLS"]["stdout_under_150KB"] = stdout_ok
    checks["D_CONTROLS"] = checks["D_CONTROLS"] and stdout_ok
    report["pass"] = all(checks.values())
    report["report_sha256"] = digest({
        key: value for key, value in report.items() if key != "report_sha256"
    })
    final_lines = tuple(
        f"{'PASS' if passed else 'FAIL'} {name} :: {passed}"
        for name, passed in checks.items()
    ) + findings
    output = "\n".join(final_lines) + "\nSUMMARY_JSON " + compact(report) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
