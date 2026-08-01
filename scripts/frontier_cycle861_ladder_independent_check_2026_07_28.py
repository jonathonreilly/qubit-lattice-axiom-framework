#!/usr/bin/env python3
"""Cycle 861 independent adversarial checker for the clean-event ladder.

The Cycle-861 source is SHA-pinned provenance and is parsed as text/AST only.
All dynamics, ladder counts, content comparisons, and cadence probes are
recomputed from the earlier Cycle-719 controller core.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
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
    "scripts/frontier_cycle861_confirmation_ladder_2026_07_28.py",
)
CORE_PATH, SOURCE_PRIMARY_PATH = AUDIT_INPUT_PATHS
SOURCE_PRIMARY_MODULE = Path(SOURCE_PRIMARY_PATH).stem
EXPECTED_SHA256 = {
    CORE_PATH: "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    SOURCE_PRIMARY_PATH: "bf669014fb8f9e01cf73ac386faddda89169bb561cb700ffdda0a3d764319d67",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    SOURCE_PRIMARY_PATH: "d9878691cf07fabdb4852cd7302c016e1a131196",
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _SourcePrimaryBlocker(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname.rsplit(".", 1)[-1] == SOURCE_PRIMARY_MODULE:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST source primary import: {fullname}")
        return None


SOURCE_PRIMARY_BLOCKER = _SourcePrimaryBlocker()
sys.meta_path.insert(0, SOURCE_PRIMARY_BLOCKER)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as CORE


Key = tuple[int, int, tuple[int, ...]]
State = tuple[int, ...]

FIXTURE_BANKS = 2
MIN_SOURCES = 2
MAX_SOURCES = 5
ORBIT_HORIZON = 51_115
EXPECTED_DEPTH_FEATURES = {0: 566, 1: 0, 2: 9, 3: 7, 4: 8}
EXPECTED_POSITIVE = 182
EXPECTED_MAX_DEPTH = 153_348
EXPECTED_PER_K_ZERO_POSITIVE = {
    2: (121, 55),
    3: (234, 74),
    4: (178, 42),
    5: (33, 11),
}
EXPECTED_E2 = 114
EXPECTED_E1_ONLY = 68
EXPECTED_PERIOD496 = 20
EXPECTED_E2_CONTENT_DIFFERENT = 31
TRIO_KEYS: tuple[Key, ...] = (
    (3, 2, (0, 2, 6)),
    (3, 3, (0, 2, 6)),
    (3, 2, (0, 2, 7)),
    (3, 3, (0, 2, 7)),
    (3, 2, (0, 2, 8)),
    (3, 3, (0, 2, 8)),
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def stable_digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def literal_value(tree: ast.Module, name: str) -> object | None:
    found = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            targets = node.targets
        elif isinstance(node, ast.AnnAssign):
            targets = (node.target,)
        else:
            continue
        if any(isinstance(target, ast.Name) and target.id == name for target in targets):
            found.append(node.value)
    if len(found) != 1:
        return None
    try:
        return ast.literal_eval(found[0])
    except (TypeError, ValueError):
        return None


def top_level_functions(tree: ast.Module) -> frozenset[str]:
    return frozenset(
        node.name for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    )


def provenance_controls() -> dict[str, object]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    primary_tree = ast.parse(payloads[SOURCE_PRIMARY_PATH], SOURCE_PRIMARY_PATH)
    self_tree = ast.parse(Path(__file__).read_bytes(), Path(__file__).name)
    shas = {path: sha256(payload).hexdigest() for path, payload in payloads.items()}
    blobs = {path: git_blob(payload) for path, payload in payloads.items()}
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    primary_markers = {
        "scan_ladder", "replay_content", "certificate_a", "certificate_d"
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_value(self_tree, "AUDIT_INPUT_PATHS") == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "sha256": shas,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": blobs,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "source_primary_path": SOURCE_PRIMARY_PATH,
        "source_primary_AST_markers": tuple(sorted(
            primary_markers & top_level_functions(primary_tree)
        )),
        "source_primary_loaded": SOURCE_PRIMARY_MODULE in sys.modules,
        "blocklist_hits": tuple(SOURCE_PRIMARY_BLOCKER.hits),
        "direct_frontier_imports": direct_frontier_imports,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and shas == EXPECTED_SHA256
        and blobs == EXPECTED_GIT_BLOBS
        and result["source_primary_AST_markers"] == tuple(sorted(primary_markers))
        and not result["source_primary_loaded"]
        and not result["blocklist_hits"]
        and direct_frontier_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
    )
    return result


def separated(positions: tuple[int, ...], station_count: int) -> bool:
    occupied = frozenset(positions)
    return not any((position + 1) % station_count in occupied for position in occupied)


def event_seed_states(program: tuple[object, ...]) -> tuple[tuple[int, State], ...]:
    banks, links = CORE.B.chain_genesis(FIXTURE_BANKS)
    state = CORE.M.pack_state(banks, links)
    allocator = CORE.M.global_allocator_word(FIXTURE_BANKS)
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = CORE.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = CORE.run_orbit(before, program)
        if after != CORE.A.apply_semantic(before, allocator):
            raise AssertionError(("event seed semantic mismatch", event))
        if rail_a != (1,) + (0,) * (len(program) - 1) or any(rail_b):
            raise AssertionError(("event seed controller mismatch", event))
        if len(trace) != len(program):
            raise AssertionError(("event seed trace mismatch", event))
        rows.append((event, before))
        state = after
    return tuple(rows)


def rotate_key(key: Key, shift: int, station_count: int) -> Key:
    sources, event, positions = key
    return (
        sources,
        event,
        tuple(sorted((position + shift) % station_count for position in positions)),
    )


def build_scope() -> dict[str, object]:
    program = CORE.interleaved_program(FIXTURE_BANKS)
    station_count = len(program)
    seeds = event_seed_states(program)
    census = tuple(sorted(
        (source_count, event, positions)
        for source_count in range(MIN_SOURCES, MAX_SOURCES + 1)
        for positions in combinations(range(station_count), source_count)
        if separated(positions, station_count)
        for event, _state in seeds
    ))
    remaining = set(census)
    rotation_orbits = []
    while remaining:
        representative = min(remaining)
        orbit = tuple(sorted({
            rotate_key(representative, shift, station_count)
            for shift in range(station_count)
        }))
        if not set(orbit) <= set(census):
            raise AssertionError(("rotation closure", representative))
        rotation_orbits.append(orbit)
        remaining.difference_update(orbit)
    per_k = dict(sorted(Counter(key[0] for key in census).items()))
    return {
        "program": program,
        "station_count": station_count,
        "seeds": seeds,
        "census": census,
        "rotation_orbits": tuple(sorted(rotation_orbits, key=lambda row: row[0])),
        "per_k_population": per_k,
        "pass": (
            station_count == 11
            and len(seeds) == 4
            and len(census) == 748
            and per_k == {2: 176, 3: 308, 4: 220, 5: 44}
            and len(rotation_orbits) == 68
            and all(len(orbit) == station_count for orbit in rotation_orbits)
            and set(TRIO_KEYS) <= set(census)
        ),
    }


def watched_bank_wires() -> tuple[int, ...]:
    return (
        CORE.A.POINTER,
        CORE.A.U_TO_V,
        CORE.A.V_TO_U,
        CORE.A.DIRECTION_OK,
        *CORE.A.FRESH,
        *CORE.A.ZERO_WORK,
        CORE.A.TOKEN_OK,
    )


def dirty_coordinates() -> tuple[int, ...]:
    banks, links = CORE.B.chain_genesis(FIXTURE_BANKS)
    zero_banks = tuple(tuple(0 for _ in bank) for bank in banks)
    zero_links = tuple(tuple(0 for _ in link) for link in links)
    baseline = CORE.M.pack_state(zero_banks, zero_links)
    indices = {CORE.R3.X.SOURCE_POINTER}
    for bank_index in range(len(zero_banks)):
        for wire in watched_bank_wires():
            changed = [list(bank) for bank in zero_banks]
            changed[bank_index][wire] = 1
            packed = CORE.M.pack_state(
                tuple(tuple(bank) for bank in changed), zero_links
            )
            difference = tuple(
                index for index, (left, right) in enumerate(zip(baseline, packed))
                if left != right
            )
            if len(difference) != 1:
                raise AssertionError(("bank packing", bank_index, wire, difference))
            indices.add(difference[0])
    for link_index, link in enumerate(zero_links):
        for wire in range(len(link)):
            changed = [list(row) for row in zero_links]
            changed[link_index][wire] = 1
            packed = CORE.M.pack_state(
                zero_banks, tuple(tuple(row) for row in changed)
            )
            difference = tuple(
                index for index, (left, right) in enumerate(zip(baseline, packed))
                if left != right
            )
            if len(difference) != 1:
                raise AssertionError(("link packing", link_index, wire, difference))
            indices.add(difference[0])
    return tuple(sorted(indices))


def synchronous_word(
    program: tuple[object, ...], positions0: tuple[int, ...]
) -> tuple[object, ...]:
    positions = positions0
    word = []
    for _ in range(len(program)):
        live = frozenset(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(CORE.mapped_macro(row))
        positions = tuple((position + 1) % len(program) for position in positions)
    return tuple(word)


def initial_states(scope: dict[str, object]) -> tuple[tuple[State, ...], int]:
    program = scope["program"]
    census = scope["census"]
    seed_by_event = dict(scope["seeds"])
    word_by_positions = {
        positions: synchronous_word(program, positions)
        for _sources, _event, positions in census
    }
    rows = []
    failures = 0
    for source_count, event, positions in census:
        before = seed_by_event[event]
        after, rail_a, rail_b, _trace = CORE.run_orbit(
            before, program, token_positions=positions
        )
        expected_rail = tuple(
            int(station in positions) for station in range(len(program))
        )
        failures += after != CORE.A.apply_semantic(
            before, word_by_positions[positions]
        )
        failures += rail_a != expected_rail or any(rail_b)
        restored, inverse_a, inverse_b, _trace = CORE.run_orbit(
            after, program, token_positions=positions, reverse=True
        )
        failures += restored != before
        failures += inverse_a != rail_a or inverse_b != rail_b
        failures += len(positions) != source_count
        rows.append(after)
    return tuple(rows), failures


def transpose_states(states: tuple[State, ...]) -> list[int]:
    return [
        sum(bit << lane for lane, bit in enumerate(column))
        for column in zip(*states)
    ]


def gate_tuple(gate: object, mask: int) -> tuple[int, int, int, int, int]:
    if gate.kind == "X":
        return 0, gate.wires[0], 0, 0, mask
    if gate.kind == "CNOT":
        return 1, gate.wires[0], gate.wires[1], 0, mask
    if gate.kind == "TOF":
        return 2, gate.wires[0], gate.wires[1], gate.wires[2], mask
    raise ValueError(("unsupported gate", gate.kind, gate.wires))


def phase_schedules(
    program: tuple[object, ...], keys: tuple[Key, ...]
) -> tuple[tuple[tuple[int, int, int, int, int], ...], ...]:
    rows = []
    station_count = len(program)
    for phase in range(station_count):
        schedule = []
        for station, program_row in enumerate(program):
            lanes = sum(
                1 << lane
                for lane, (_sources, _event, positions) in enumerate(keys)
                if (station - phase) % station_count in positions
            )
            if lanes:
                schedule.extend(
                    gate_tuple(gate, lanes) for gate in CORE.mapped_macro(program_row)
                )
        rows.append(tuple(schedule))
    return tuple(rows)


def compile_phases(
    schedules: tuple[tuple[tuple[int, int, int, int, int], ...], ...]
) -> tuple[Callable[[list[int]], None], ...]:
    compiled = []
    for phase, schedule in enumerate(schedules):
        source = [f"def phase_{phase}(columns):"]
        for kind, control_a, control_b, target, lane_mask in schedule:
            if kind == 0:
                source.append(f" columns[{control_a}] ^= {lane_mask}")
            elif kind == 1:
                source.append(
                    f" columns[{control_b}] ^= columns[{control_a}] & {lane_mask}"
                )
            else:
                source.append(
                    f" columns[{target}] ^= columns[{control_a}] & "
                    f"columns[{control_b}] & {lane_mask}"
                )
        namespace: dict[str, object] = {}
        exec("\n".join(source), {"__builtins__": {}}, namespace)
        compiled.append(namespace[f"phase_{phase}"])
    return tuple(compiled)  # type: ignore[return-value]


def clean_lanes(columns: list[int], dirty: tuple[int, ...], lane_mask: int) -> int:
    contaminated = 0
    for wire in dirty:
        contaminated |= columns[wire]
    return lane_mask & ~contaminated


def equal_to_initial(
    columns: list[int], initial: list[int], candidates: int
) -> int:
    differences = 0
    for current, reference in zip(columns, initial):
        differences |= current ^ reference
    return candidates & ~differences


def lanes(mask: int):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def capture_lane(columns: list[int], lane: int) -> bytes:
    bit = 1 << lane
    return bytes(bool(column & bit) for column in columns)


def lane_matches(columns: list[int], lane: int, reference: bytes) -> bool:
    bit = 1 << lane
    return all(bool(column & bit) == bool(expected)
               for column, expected in zip(columns, reference))


def independent_scan(scope: dict[str, object]) -> dict[str, object]:
    """Single-pass reconstruction of ladder, content, recurrence, and cadences."""

    started = monotonic()
    program = scope["program"]
    census = scope["census"]
    station_count = scope["station_count"]
    states, initial_failures = initial_states(scope)
    duplicate_lane = len(census)
    simulation_states = states + (states[0],)
    simulation_keys = census + (census[0],)
    columns = transpose_states(simulation_states)
    initial_columns = columns.copy()
    dirty = dirty_coordinates()
    schedules = phase_schedules(program, simulation_keys)
    phases = compile_phases(schedules)
    all_real = (1 << len(census)) - 1
    all_simulation = (1 << len(simulation_keys)) - 1

    counts = [0] * len(census)
    first_content: list[bytes | None] = [None] * len(census)
    n1_n2_equal: list[bool | None] = [None] * len(census)
    first_divergence: list[int | None] = [None] * len(census)
    content_comparisons = 0
    ladder_first: dict[Key, int] = {}
    e1_first: dict[Key, int] = {}
    e2_first: dict[Key, int] = {}
    e2_rung: dict[Key, int] = {}
    e2_content_equal_to_set: dict[Key, bool] = {}
    e1_mask = 0
    e2_mask = 0
    every_second_orbit_mask = 0
    every_fourth_orbit_mask = 0
    half_orbit_mask = 0 if station_count % 2 == 0 else None
    cycle_periods: dict[Key, int] = {}
    unresolved_cycle = all_real
    determinism_mismatches = 0
    total_clean_events = 0
    orbit_boundary_clean_events = 0
    event_hasher = sha256()

    def record_h_event(clean: int, absolute_h: int) -> None:
        nonlocal e1_mask, content_comparisons, total_clean_events
        new_e1 = clean & ~e1_mask
        for lane in lanes(new_e1):
            e1_first[census[lane]] = absolute_h
        e1_mask |= clean
        for lane in lanes(clean):
            counts[lane] += 1
            rung = counts[lane]
            total_clean_events += 1
            event_hasher.update(lane.to_bytes(2, "big"))
            event_hasher.update(absolute_h.to_bytes(4, "big"))
            if rung == 1:
                ladder_first[census[lane]] = absolute_h
                first_content[lane] = capture_lane(columns, lane)
                continue
            reference = first_content[lane]
            if reference is None:
                raise AssertionError(("missing rung-1 content", census[lane], rung))
            if rung == 2 or first_divergence[lane] is None:
                same = lane_matches(columns, lane, reference)
                content_comparisons += 1
                if rung == 2:
                    n1_n2_equal[lane] = same
                if not same and first_divergence[lane] is None:
                    first_divergence[lane] = rung

    def record_orbit_boundary(clean: int, absolute_h: int, orbit: int) -> None:
        nonlocal e2_mask, every_second_orbit_mask, every_fourth_orbit_mask
        nonlocal orbit_boundary_clean_events, content_comparisons
        orbit_boundary_clean_events += clean.bit_count()
        new_e2 = clean & ~e2_mask
        for lane in lanes(new_e2):
            key = census[lane]
            e2_first[key] = absolute_h
            e2_rung[key] = counts[lane]
            reference = first_content[lane]
            if reference is None:
                raise AssertionError(("missing E2 baseline", key, orbit))
            if counts[lane] == 1:
                same = True
            else:
                same = lane_matches(columns, lane, reference)
                content_comparisons += 1
            e2_content_equal_to_set[key] = same
        e2_mask |= clean
        if orbit % 2 == 0:
            every_second_orbit_mask |= clean
        if orbit % 4 == 0:
            every_fourth_orbit_mask |= clean

    initial_clean_all = clean_lanes(columns, dirty, all_simulation)
    initial_clean = initial_clean_all & all_real
    determinism_mismatches += (
        bool(initial_clean_all & 1)
        != bool(initial_clean_all & (1 << duplicate_lane))
    )
    record_h_event(initial_clean, 0)
    record_orbit_boundary(initial_clean, 0, 0)
    unresolved_cycle &= ~initial_clean

    for orbit in range(1, ORBIT_HORIZON + 1):
        boundary_clean = 0
        for step, apply_phase in enumerate(phases, 1):
            apply_phase(columns)
            clean_all = clean_lanes(columns, dirty, all_simulation)
            clean = clean_all & all_real
            absolute_h = (orbit - 1) * station_count + step
            determinism_mismatches += (
                bool(clean_all & 1)
                != bool(clean_all & (1 << duplicate_lane))
            )
            record_h_event(clean, absolute_h)
            if half_orbit_mask is not None and step == station_count // 2:
                half_orbit_mask |= clean
            boundary_clean = clean

        record_orbit_boundary(
            boundary_clean, orbit * station_count, orbit
        )
        recurrence = equal_to_initial(
            columns, initial_columns, unresolved_cycle & ~boundary_clean
        )
        for lane in lanes(recurrence):
            cycle_periods[census[lane]] = orbit
        unresolved_cycle &= ~(boundary_clean | recurrence)

    duplicate_final_exact = all(
        bool(column & 1) == bool(column & (1 << duplicate_lane))
        for column in columns
    )
    positive_lanes = tuple(lane for lane, depth in enumerate(counts) if depth)
    result = {
        "depths": tuple(counts),
        "ladder_first": ladder_first,
        "e1_first": e1_first,
        "e2_first": e2_first,
        "e2_rung": e2_rung,
        "e2_content_equal_to_set": e2_content_equal_to_set,
        "n1_n2_equal": tuple(n1_n2_equal),
        "first_divergence": tuple(first_divergence),
        "cycle_periods": cycle_periods,
        "cadence_masks": {
            "every_H_boundary_E1": e1_mask,
            "every_orbit_boundary_E2": e2_mask,
            "every_2nd_orbit": every_second_orbit_mask,
            "every_4th_orbit": every_fourth_orbit_mask,
            "half_orbit_boundary": half_orbit_mask,
        },
        "state_bits": len(columns),
        "dirty_coordinate_count": len(dirty),
        "schedule_gate_counts": tuple(map(len, schedules)),
        "initial_failures": initial_failures,
        "total_clean_events": total_clean_events,
        "orbit_boundary_clean_events": orbit_boundary_clean_events,
        "event_stream_sha256": event_hasher.hexdigest(),
        "content_comparisons": content_comparisons,
        "unresolved_cycle_count": unresolved_cycle.bit_count(),
        "determinism": {
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
        and result["schedule_gate_counts"] == (3106,) * 11
        and ladder_first == e1_first
        and all(n1_n2_equal[lane] is not None for lane in positive_lanes)
        and determinism_mismatches == 0
        and duplicate_final_exact
    )
    return result


def ladder_certificate(
    scope: dict[str, object], scan: dict[str, object]
) -> dict[str, object]:
    census = scope["census"]
    depths = scan["depths"]
    histogram = dict(sorted(Counter(depths).items()))
    per_k_depth_histogram = {
        source_count: dict(sorted(Counter(
            depth for key, depth in zip(census, depths)
            if key[0] == source_count
        ).items()))
        for source_count in range(MIN_SOURCES, MAX_SOURCES + 1)
    }
    per_k_zero_positive = {
        source_count: (
            per_k_depth_histogram[source_count].get(0, 0),
            sum(count for depth, count in per_k_depth_histogram[source_count].items()
                if depth > 0),
        )
        for source_count in range(MIN_SOURCES, MAX_SOURCES + 1)
    }
    claimed_features = {
        depth: histogram.get(depth, 0) for depth in EXPECTED_DEPTH_FEATURES
    }
    result = {
        "census_size": len(census),
        "horizon_orbits_inclusive": ORBIT_HORIZON,
        "horizon_absolute_H_inclusive": ORBIT_HORIZON * scope["station_count"],
        "depth_histogram": histogram,
        "depth_histogram_sha256": stable_digest(histogram),
        "positive_depth_count": sum(depth > 0 for depth in depths),
        "none_at_depth_exactly_1": histogram.get(1, 0) == 0,
        "maximum_depth": max(depths),
        "per_k_depth_histogram": per_k_depth_histogram,
        "per_k_zero_positive": per_k_zero_positive,
        "total_clean_events": scan["total_clean_events"],
        "event_stream_sha256": scan["event_stream_sha256"],
    }
    result["pass"] = (
        scope["pass"]
        and scan["pass"]
        and len(depths) == 748
        and sum(histogram.values()) == 748
        and claimed_features == EXPECTED_DEPTH_FEATURES
        and result["positive_depth_count"] == EXPECTED_POSITIVE
        and result["none_at_depth_exactly_1"]
        and result["maximum_depth"] == EXPECTED_MAX_DEPTH
        and per_k_zero_positive == EXPECTED_PER_K_ZERO_POSITIVE
        and scan["total_clean_events"]
            == sum(depth * count for depth, count in histogram.items())
    )
    return result


def identification_certificate(
    scope: dict[str, object], scan: dict[str, object]
) -> dict[str, object]:
    census = scope["census"]
    depths = scan["depths"]
    depth_by_key = dict(zip(census, depths))
    e1_set = frozenset(scan["e1_first"])
    e2_set = frozenset(scan["e2_first"])
    rung_histogram = dict(sorted(Counter(scan["e2_rung"].values()).items()))
    fixed_rung_matches = tuple(
        rung for rung in range(1, max(depths) + 1)
        if frozenset(
            key for key, depth in zip(census, depths) if depth >= rung
        ) == e2_set
    )
    e1_only = e1_set - e2_set
    period496 = frozenset(
        key for key, period in scan["cycle_periods"].items() if period == 496
    )
    degree_by_key = {
        key: sum(
            rotate_key(key, shift, scope["station_count"]) in e1_set
            for shift in range(scope["station_count"])
        )
        for key in census
    }
    monitor_witnesses = []
    for orbit in scope["rotation_orbits"]:
        depths_in_orbit = Counter(depth_by_key[key] for key in orbit)
        degrees_in_orbit = {degree_by_key[key] for key in orbit}
        if len(degrees_in_orbit) != 1:
            raise AssertionError(("monitor degree not orbit invariant", orbit[0]))
        if len(depths_in_orbit) > 1:
            monitor_witnesses.append({
                "representative": orbit[0],
                "monitor_degree": next(iter(degrees_in_orbit)),
                "depth_histogram": dict(sorted(depths_in_orbit.items())),
            })
    result = {
        "E1_count": len(e1_set),
        "E1_equals_rung1_moment_exact":
            scan["e1_first"] == scan["ladder_first"],
        "E1_moment_sha256": stable_digest(tuple(sorted(scan["e1_first"].items()))),
        "E2_count": len(e2_set),
        "E2_all_first_orbit_boundary_clean_moment_exact": all(
            moment % scope["station_count"] == 0
            for moment in scan["e2_first"].values()
        ),
        "E2_moment_sha256": stable_digest(tuple(sorted(scan["e2_first"].items()))),
        "E2_rung_histogram": rung_histogram,
        "E2_rung_range": (
            min(scan["e2_rung"].values()), max(scan["e2_rung"].values())
        ),
        "fixed_rungs_reproducing_E2": fixed_rung_matches,
        "literal_rung2_count": sum(depth >= 2 for depth in depths),
        "literal_rung2_equals_E2": frozenset(
            key for key, depth in zip(census, depths) if depth >= 2
        ) == e2_set,
        "trio_depths": tuple((key, depth_by_key[key]) for key in TRIO_KEYS),
        "E1_only_count": len(e1_only),
        "E1_only_depth_histogram": dict(sorted(Counter(
            depth_by_key[key] for key in e1_only
        ).items())),
        "E1_only_all_have_confirmations": all(
            depth_by_key[key] >= 2 for key in e1_only
        ),
        "E1_only_confirmations_all_off_orbit_cadence": not (e1_only & e2_set),
        "period496_count": len(period496),
        "period496_never_set": all(depth_by_key[key] == 0 for key in period496),
        "cycle_period_histogram": dict(sorted(Counter(
            scan["cycle_periods"].values()
        ).items())),
        "monitor_degree_does_not_determine_depth": bool(monitor_witnesses),
        "monitor_degree_witness_count": len(monitor_witnesses),
        "monitor_degree_witnesses_first3": tuple(monitor_witnesses[:3]),
    }
    result["pass"] = (
        result["E1_count"] == EXPECTED_POSITIVE
        and result["E1_equals_rung1_moment_exact"]
        and result["E2_count"] == EXPECTED_E2
        and result["E2_all_first_orbit_boundary_clean_moment_exact"]
        and sum(rung_histogram.values()) == EXPECTED_E2
        and result["E2_rung_range"] == (1, 167)
        and not fixed_rung_matches
        and result["literal_rung2_count"] == EXPECTED_POSITIVE
        and not result["literal_rung2_equals_E2"]
        and all(depth == 0 for _key, depth in result["trio_depths"])
        and len(e1_only) == EXPECTED_E1_ONLY
        and result["E1_only_all_have_confirmations"]
        and result["E1_only_confirmations_all_off_orbit_cadence"]
        and len(period496) == EXPECTED_PERIOD496
        and result["period496_never_set"]
        and result["monitor_degree_does_not_determine_depth"]
    )
    return result


def content_identity_certificate(
    scope: dict[str, object], scan: dict[str, object]
) -> dict[str, object]:
    census = scope["census"]
    depths = scan["depths"]
    positive_lanes = tuple(lane for lane, depth in enumerate(depths) if depth > 0)
    rung2_lanes = tuple(lane for lane, depth in enumerate(depths) if depth >= 2)
    equal_keys = tuple(
        census[lane] for lane in rung2_lanes if scan["n1_n2_equal"][lane] is True
    )
    unequal_keys = tuple(
        census[lane] for lane in rung2_lanes if scan["n1_n2_equal"][lane] is False
    )
    divergence_histogram = dict(sorted(Counter(
        scan["first_divergence"][lane]
        for lane in positive_lanes
        if scan["first_divergence"][lane] is not None
    ).items()))
    no_divergence = tuple(
        census[lane] for lane in positive_lanes
        if scan["first_divergence"][lane] is None
    )
    no_divergence_depths = dict(sorted(Counter(
        depths[census.index(key)] for key in no_divergence
    ).items()))
    divergence_manifest = tuple(
        (census[lane], scan["first_divergence"][lane])
        for lane in positive_lanes
    )
    e2_different = tuple(sorted(
        key for key, same in scan["e2_content_equal_to_set"].items() if not same
    ))
    thresholds = {
        "n=1": sum(depth >= 1 for depth in depths),
        "n=2": sum(depth >= 2 for depth in depths),
        "n=3": sum(depth >= 3 for depth in depths),
        f"max={max(depths)}": sum(depth >= max(depths) for depth in depths),
    }
    result = {
        "n1_record_count": len(positive_lanes),
        "n2_record_count": len(rung2_lanes),
        "n1_n2_same_key_set": set(positive_lanes) == set(rung2_lanes),
        "n1_n2_content_equal_keys": len(equal_keys),
        "n1_n2_content_unequal_keys": len(unequal_keys),
        "n1_n2_equal_key_sha256": stable_digest(equal_keys),
        "first_content_divergence_rung_histogram": divergence_histogram,
        "first_content_divergence_manifest_sha256": stable_digest(
            divergence_manifest
        ),
        "no_content_divergence_by_horizon_count": len(no_divergence),
        "no_content_divergence_by_horizon_depth_histogram": no_divergence_depths,
        "first_divergence_rows_account_for_all_positive_keys":
            sum(divergence_histogram.values()) + len(no_divergence)
            == len(positive_lanes),
        "all_observed_first_divergences_after_rung2": all(
            rung >= 3 for rung in divergence_histogram
        ),
        "E2_content_different_from_set_count": len(e2_different),
        "E2_content_different_key_sha256": stable_digest(e2_different),
        "threshold_record_set_sizes": thresholds,
        "content_comparisons": scan["content_comparisons"],
    }
    result["pass"] = (
        len(positive_lanes) == EXPECTED_POSITIVE
        and len(rung2_lanes) == EXPECTED_POSITIVE
        and result["n1_n2_same_key_set"]
        and len(equal_keys) == EXPECTED_POSITIVE
        and not unequal_keys
        and result["first_divergence_rows_account_for_all_positive_keys"]
        and result["all_observed_first_divergences_after_rung2"]
        and len(e2_different) == EXPECTED_E2_CONTENT_DIFFERENT
        and thresholds == {
            "n=1": 182,
            "n=2": 182,
            "n=3": 173,
            f"max={EXPECTED_MAX_DEPTH}": 1,
        }
    )
    return result


def cadence_certificate(
    scope: dict[str, object], scan: dict[str, object]
) -> dict[str, object]:
    census = scope["census"]
    cadence_rows = []
    sets: dict[str, frozenset[Key] | None] = {}
    for cadence, mask in scan["cadence_masks"].items():
        if mask is None:
            sets[cadence] = None
            cadence_rows.append({
                "cadence": cadence,
                "admitted": False,
                "reason": f"odd {scope['station_count']}-chunk orbit has no half boundary",
                "stamped_count": None,
                "key_sha256": None,
            })
            continue
        key_set = frozenset(census[lane] for lane in lanes(mask))
        sets[cadence] = key_set
        cadence_rows.append({
            "cadence": cadence,
            "admitted": True,
            "stamped_count": len(key_set),
            "key_sha256": stable_digest(tuple(sorted(key_set))),
        })
    landed_names = {"every_H_boundary_E1", "every_orbit_boundary_E2"}
    non_landed = {
        name: key_set for name, key_set in sets.items()
        if name not in landed_names and key_set is not None
    }
    size_collisions = tuple(sorted(
        name for name, key_set in non_landed.items()
        if len(key_set) in {EXPECTED_E1_ONLY + EXPECTED_E2, EXPECTED_E2}
    ))
    exact_collisions = tuple(sorted(
        name for name, key_set in non_landed.items()
        if key_set in {
            sets["every_H_boundary_E1"], sets["every_orbit_boundary_E2"]
        }
    ))
    orbit_unique = not size_collisions
    result = {
        "cadence_family": tuple(cadence_rows),
        "non_landed_size_collisions_with_182_or_114": size_collisions,
        "non_landed_exact_set_collisions_with_E1_or_E2": exact_collisions,
        "orbit_boundary_clock_unique_by_landed_census_size": orbit_unique,
        "constructive_reading": (
            "distinct non-landed sizes strengthen the cadence-anchored reading"
            if orbit_unique else
            "a non-landed size coincidence weakens the cadence-anchored reading"
        ),
    }
    result["pass"] = (
        len(sets["every_H_boundary_E1"] or ()) == EXPECTED_POSITIVE
        and len(sets["every_orbit_boundary_E2"] or ()) == EXPECTED_E2
        and sets["half_orbit_boundary"] is None
        and len(cadence_rows) == 5
    )
    return result


def public_scan(scan: dict[str, object]) -> dict[str, object]:
    return {
        key: value for key, value in scan.items()
        if key not in {
            "depths", "ladder_first", "e1_first", "e2_first", "e2_rung",
            "e2_content_equal_to_set", "n1_n2_equal", "first_divergence",
            "cycle_periods", "cadence_masks",
        }
    }


def main() -> int:
    started = monotonic()
    controls_pre = provenance_controls()
    scope = build_scope()
    scan = independent_scan(scope)
    ladder = ladder_certificate(scope, scan)
    identifications = identification_certificate(scope, scan)
    content = content_identity_certificate(scope, scan)
    cadence = cadence_certificate(scope, scan)
    controls_post = provenance_controls()
    elapsed = monotonic() - started

    checks = {
        "THE_LADDER_REPLAY": ladder["pass"],
        "THE_IDENTIFICATIONS": identifications["pass"],
        "THE_N1_N2_CONTENT_IDENTITY": content["pass"],
        "THE_CADENCE_FAMILY_PROBE": cadence["pass"],
        "CONTROLS": (
            controls_pre["pass"]
            and controls_post["pass"]
            and controls_pre == controls_post
            and scan["determinism"]["boundary_mismatches"] == 0
            and scan["determinism"]["final_full_state_exact"]
            and elapsed < AUDIT_TIMEOUT_SEC
            and not SOURCE_PRIMARY_BLOCKER.hits
        ),
    }
    primary_refuted = not all(
        checks[name] for name in (
            "THE_LADDER_REPLAY",
            "THE_IDENTIFICATIONS",
            "THE_N1_N2_CONTENT_IDENTITY",
        )
    )
    cadence_sizes = {
        row["cadence"]: row["stamped_count"]
        for row in cadence["cadence_family"]
    }
    findings = (
        "FINDING THE_LADDER_REPLAY :: independently rebuilt 748 keys through "
        f"orbit {ORBIT_HORIZON}; depth histogram={compact(ladder['depth_histogram'])}; "
        f"depth-1 count={ladder['depth_histogram'].get(1, 0)}; max depth="
        f"{ladder['maximum_depth']}; per-k zero/positive="
        f"{compact(ladder['per_k_zero_positive'])}",
        "FINDING THE_IDENTIFICATIONS :: E1 == rung 1 moment-exact="
        f"{identifications['E1_equals_rung1_moment_exact']} ({identifications['E1_count']}); "
        f"E2 == first orbit-boundary clean moment-exact="
        f"{identifications['E2_all_first_orbit_boundary_clean_moment_exact']} "
        f"({identifications['E2_count']}); E2 rung histogram="
        f"{compact(identifications['E2_rung_histogram'])}, range="
        f"{identifications['E2_rung_range']}, fixed rung matches="
        f"{identifications['fixed_rungs_reproducing_E2']}; six trio depths="
        f"{compact(tuple(depth for _key, depth in identifications['trio_depths']))}; "
        f"68 E1-only all confirmed off cadence="
        f"{identifications['E1_only_all_have_confirmations'] and identifications['E1_only_confirmations_all_off_orbit_cadence']}; "
        f"period-496 count/never-set={identifications['period496_count']}/"
        f"{identifications['period496_never_set']}; monitor degree does not "
        f"determine depth={identifications['monitor_degree_does_not_determine_depth']}",
        "FINDING THE_N1_N2_CONTENT_IDENTITY :: n=1/n=2 record-set sizes="
        f"{content['n1_record_count']}/{content['n2_record_count']}, same keys="
        f"{content['n1_n2_same_key_set']}; per-key content equal="
        f"{content['n1_n2_content_equal_keys']}/{content['n2_record_count']} exact; "
        f"first-divergence rung histogram="
        f"{compact(content['first_content_divergence_rung_histogram'])}; "
        f"none by horizon={content['no_content_divergence_by_horizon_count']} "
        f"with depths={compact(content['no_content_divergence_by_horizon_depth_histogram'])}; "
        f"E2 content differs from set content for "
        f"{content['E2_content_different_from_set_count']} keys; threshold sizes="
        f"{compact(content['threshold_record_set_sizes'])}",
        "FINDING THE_CADENCE_FAMILY_PROBE :: stamped sizes="
        f"{compact(cadence_sizes)}; non-landed size collisions with 182 or 114="
        f"{cadence['non_landed_size_collisions_with_182_or_114']}; exact-set "
        f"collisions={cadence['non_landed_exact_set_collisions_with_E1_or_E2']}; "
        f"orbit-boundary clock unique by landed census size="
        f"{cadence['orbit_boundary_clock_unique_by_landed_census_size']}; "
        f"{cadence['constructive_reading']}",
        "FINDING CONTROLS :: SHA-256 and git-blob pins exact; source primary "
        "BLOCKLIST text/AST only; literal AUDIT_INPUT_PATHS exist worktree-relative; "
        f"determinism mismatches={scan['determinism']['boundary_mismatches']} and "
        f"final exact={scan['determinism']['final_full_state_exact']}; runtime < "
        "1400s; stdout < 150KB",
        "FINDING ADVERSARIAL_DISPOSITION :: "
        + ("PRIMARY_REFUTED by one or more claimed invariants"
           if primary_refuted else
           "PRIMARY_NOT_REFUTED by the independently recomputed claimed invariants"),
    )
    report = {
        "cycle": 861,
        "checker": "independent_adversarial_ladder",
        "checks": checks,
        "THE_LADDER_REPLAY": ladder,
        "THE_IDENTIFICATIONS": identifications,
        "THE_N1_N2_CONTENT_IDENTITY": content,
        "THE_CADENCE_FAMILY_PROBE": cadence,
        "CONTROLS": {
            **controls_post,
            "pre_post_exact": controls_pre == controls_post,
            "determinism": scan["determinism"],
            "scan": public_scan(scan),
            "runtime_under_1400s": elapsed < AUDIT_TIMEOUT_SEC,
            "stdout_under_150KB": None,
        },
        "primary_refuted": primary_refuted,
        "runtime_seconds": round(elapsed, 6),
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
    report["CONTROLS"]["stdout_under_150KB"] = stdout_ok
    checks["CONTROLS"] = checks["CONTROLS"] and stdout_ok
    report["pass"] = all(checks.values())
    report["report_sha256"] = stable_digest({
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
