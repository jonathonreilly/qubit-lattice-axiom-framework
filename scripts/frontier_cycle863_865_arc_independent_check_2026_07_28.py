#!/usr/bin/env python3
"""Finite Cycle-719 controller clean-predicate census for Cycles 863--865.

The runner independently constructs a 748-configuration ring-11 corpus and
replays the landed Cycle-719 controller through a declared finite horizon.  It
reports controller-internal clean-predicate and synchronization tables only.
Controller boundaries, clean predicates, and orbit indices are supplied
program instrumentation; this runner does not identify them with framework
Record formation, physical time, duration, rate, or an intrinsic clock.
"""
from __future__ import annotations

import ast
from bisect import bisect_left
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic


AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
EXPECTED_INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, int, tuple[int, ...]]
State = tuple[int, ...]

BANKS = 2
MIN_SOURCES = 2
MAX_SOURCES = 5
HORIZON = 51_115
GLOBAL_STORE_CAP = 4096
BANK_STORE_CAP = 512


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def source_controls() -> dict[str, object]:
    """Verify the one external repository input without branch-local pins."""

    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    for path, payload in payloads.items():
        ast.parse(payload, filename=path)

    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"), filename=__file__)
    declared_literal = None
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        ):
            declared_literal = ast.literal_eval(node.value)

    sha_rows = {path: sha256(payload).hexdigest() for path, payload in payloads.items()}
    expected_origin = (ROOT / AUDIT_INPUT_PATHS[0]).resolve()
    module_origin = Path(K.__file__).resolve()
    result = {
        "certificate": "SOURCE_CONTROLS",
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "literal_declaration": declared_literal == AUDIT_INPUT_PATHS,
        "worktree_relative_inputs": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "input_sha256": sha_rows,
        "expected_input_sha256": EXPECTED_INPUT_SHA256,
        "imported_module_origin": str(module_origin.relative_to(ROOT)),
        "branch_name_required": False,
    }
    result["pass"] = bool(
        result["literal_declaration"]
        and result["worktree_relative_inputs"]
        and sha_rows == EXPECTED_INPUT_SHA256
        and module_origin == expected_origin
    )
    return result


def separated_on_ring(positions: tuple[int, ...], stations: int) -> bool:
    occupied = set(positions)
    return all((position + 1) % stations not in occupied for position in occupied)


def event_seed_states(program) -> tuple[tuple[int, State], ...]:
    banks, links = K.B.chain_genesis(BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(BANKS)
    rows = []
    for event_index in range(2 * BANKS):
        direction = (1, 0) if event_index % 2 == 0 else (0, 1)
        prepared = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(prepared, program)
        expected_rail = (1,) + (0,) * (len(program) - 1)
        if after != K.A.apply_semantic(prepared, allocator):
            raise AssertionError(("seed allocator", event_index))
        if rail_a != expected_rail or any(rail_b) or len(trace) != len(program):
            raise AssertionError(("seed rails", event_index))
        rows.append((event_index, prepared))
        state = after
    return tuple(rows)


def independent_census():
    program = K.interleaved_program(BANKS)
    stations = len(program)
    seeds = event_seed_states(program)
    keys = []
    for source_count in range(MIN_SOURCES, MAX_SOURCES + 1):
        for positions in combinations(range(stations), source_count):
            if not separated_on_ring(positions, stations):
                continue
            for event_index, _state in seeds:
                keys.append((source_count, event_index, positions))
    return program, seeds, tuple(sorted(keys))


def watched_bank_wires() -> tuple[int, ...]:
    return (
        K.A.POINTER,
        K.A.U_TO_V,
        K.A.V_TO_U,
        K.A.DIRECTION_OK,
        *K.A.FRESH,
        *K.A.ZERO_WORK,
        K.A.TOKEN_OK,
    )


def assemble_clean_predicates():
    """Discover packed coordinates for the supplied program predicates."""

    banks0, links0 = K.B.chain_genesis(BANKS)
    zero_banks = tuple(tuple(0 for _ in bank) for bank in banks0)
    zero_links = tuple(tuple(0 for _ in link) for link in links0)
    baseline = K.M.pack_state(zero_banks, zero_links)

    bank_coordinates: list[set[int]] = [set() for _ in zero_banks]
    for bank_index in range(len(zero_banks)):
        for wire in watched_bank_wires():
            changed = [list(bank) for bank in zero_banks]
            changed[bank_index][wire] = 1
            marked = K.M.pack_state(tuple(tuple(bank) for bank in changed), zero_links)
            delta = [
                index
                for index, pair in enumerate(zip(baseline, marked))
                if pair[0] != pair[1]
            ]
            if len(delta) != 1:
                raise AssertionError(("bank coordinate", bank_index, wire, delta))
            bank_coordinates[bank_index].add(delta[0])

    link_coordinates: set[int] = set()
    for link_index, link in enumerate(zero_links):
        for wire in range(len(link)):
            changed = [list(row) for row in zero_links]
            changed[link_index][wire] = 1
            marked = K.M.pack_state(zero_banks, tuple(tuple(row) for row in changed))
            delta = [
                index
                for index, pair in enumerate(zip(baseline, marked))
                if pair[0] != pair[1]
            ]
            if len(delta) != 1:
                raise AssertionError(("link coordinate", link_index, wire, delta))
            link_coordinates.add(delta[0])

    banks = tuple(tuple(sorted(row)) for row in bank_coordinates)
    global_coordinates = tuple(
        sorted(
            set(banks[0])
            | set(banks[1])
            | link_coordinates
            | {K.R3.X.SOURCE_POINTER}
        )
    )
    return {
        "bank": banks,
        "links": tuple(sorted(link_coordinates)),
        "source_pointer": K.R3.X.SOURCE_POINTER,
        "global": global_coordinates,
    }


def initial_states(program, seeds, census):
    seed_map = dict(seeds)
    states = []
    failures = 0
    for _count, event_index, positions in census:
        after, rail_a, rail_b, _trace = K.run_orbit(
            seed_map[event_index], program, token_positions=positions
        )
        expected = tuple(int(station in positions) for station in range(len(program)))
        failures += int(rail_a != expected or any(rail_b))
        states.append(after)
    return tuple(states), failures


def transpose_states(states: tuple[State, ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def compiled_schedules(program, census):
    """Compile exact bit-sliced steps directly from every active station."""

    schedules = []
    stations = len(program)
    for step in range(stations):
        encoded = []
        for station, row in enumerate(program):
            mask = sum(
                1 << lane
                for lane, (_count, _event, positions) in enumerate(census)
                if (station - step) % stations in positions
            )
            if not mask:
                continue
            for gate in K.mapped_macro(row):
                if gate.kind == "X":
                    encoded.append((0, gate.wires[0], 0, 0, mask))
                elif gate.kind == "CNOT":
                    encoded.append((1, gate.wires[0], gate.wires[1], 0, mask))
                elif gate.kind == "TOF":
                    encoded.append((2, gate.wires[0], gate.wires[1], gate.wires[2], mask))
                else:
                    raise AssertionError(("unknown gate", gate))
        source = ["def advance(columns):"]
        for kind, left, right, target, mask in encoded:
            if kind == 0:
                source.append(f" columns[{left}] ^= {mask}")
            elif kind == 1:
                source.append(f" columns[{right}] ^= columns[{left}] & {mask}")
            else:
                source.append(
                    f" columns[{target}] ^= columns[{left}] & columns[{right}] & {mask}"
                )
        namespace: dict[str, object] = {}
        exec("\n".join(source), {"__builtins__": {}}, namespace)
        schedules.append(namespace["advance"])
    return tuple(schedules)


def clean_mask(columns: list[int], coordinates: tuple[int, ...], universe: int) -> int:
    dirty = 0
    for coordinate in coordinates:
        dirty |= columns[coordinate]
    return universe & ~dirty


def set_bits(mask: int):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def append_masked(stores, mask: int, boundary: int, cap: int) -> None:
    for lane in set_bits(mask):
        if len(stores[lane]) < cap:
            stores[lane].append(boundary)


def independent_replay(program, seeds, census, predicates):
    """Exact bit-sliced replay with a duplicated-lane determinism control."""

    started = monotonic()
    states, init_failures = initial_states(program, seeds, census)
    lane_count = len(census)
    duplicate_lane = lane_count
    simulated_census = census + (census[0],)
    columns = transpose_states(states + (states[0],))
    schedules = compiled_schedules(program, simulated_census)
    universe_all = (1 << (lane_count + 1)) - 1
    universe_primary = (1 << lane_count) - 1
    duplicate_bit = 1 << duplicate_lane
    stations = len(program)

    stores = {
        "global": [[] for _ in census],
        "bank0": [[] for _ in census],
        "bank1": [[] for _ in census],
        "sync": [[] for _ in census],
    }
    totals = Counter()
    sync_on_orbit_boundary = 0
    first_global_clean_boundary: dict[Key, int] = {}
    first_orbit_end_global_clean: dict[Key, int] = {}
    duplicate_mismatches = 0

    def observe(boundary: int):
        nonlocal duplicate_mismatches, sync_on_orbit_boundary
        global_all = clean_mask(columns, predicates["global"], universe_all)
        bank0_all = clean_mask(columns, predicates["bank"][0], universe_all)
        bank1_all = clean_mask(columns, predicates["bank"][1], universe_all)
        duplicate_mismatches += int(
            bool(global_all & 1) != bool(global_all & duplicate_bit)
        )
        duplicate_mismatches += int(
            bool(bank0_all & 1) != bool(bank0_all & duplicate_bit)
        )
        duplicate_mismatches += int(
            bool(bank1_all & 1) != bool(bank1_all & duplicate_bit)
        )
        masks = {
            "global": global_all & universe_primary,
            "bank0": bank0_all & universe_primary,
            "bank1": bank1_all & universe_primary,
            "sync": bank0_all & bank1_all & universe_primary,
        }
        for kind, mask in masks.items():
            totals[kind] += mask.bit_count()
            append_masked(
                stores[kind],
                mask,
                boundary,
                GLOBAL_STORE_CAP if kind in {"global", "sync"} else BANK_STORE_CAP,
            )
        if boundary % stations == 0:
            sync_on_orbit_boundary += masks["sync"].bit_count()
        for lane in set_bits(masks["global"]):
            first_global_clean_boundary.setdefault(census[lane], boundary)
        return masks["global"]

    last_global = observe(0)
    for lane in set_bits(last_global):
        first_orbit_end_global_clean.setdefault(census[lane], 0)

    for orbit in range(1, HORIZON + 1):
        for step, advance in enumerate(schedules, 1):
            advance(columns)
            boundary = (orbit - 1) * stations + step
            last_global = observe(boundary)
        for lane in set_bits(last_global):
            first_orbit_end_global_clean.setdefault(census[lane], orbit)

    return {
        "stations": stations,
        "stores": stores,
        "totals": dict(totals),
        "sync_on_orbit_boundary": sync_on_orbit_boundary,
        "first_global_clean_boundary": first_global_clean_boundary,
        "first_orbit_end_global_clean": first_orbit_end_global_clean,
        "init_failures": init_failures,
        "duplicate_mismatches": duplicate_mismatches,
        "final_columns_digest": digest(columns),
        "runtime_seconds": round(monotonic() - started, 3),
    }


def replay_certificate(rep, census) -> dict[str, object]:
    stations = rep["stations"]
    first_global = rep["first_global_clean_boundary"]
    first_orbit_end = rep["first_orbit_end_global_clean"]
    first_sync_matches = 0
    orbit_end_with_sync = 0
    sync_only_configurations = 0
    for lane, key in enumerate(census):
        syncs = rep["stores"]["sync"][lane]
        if key in first_orbit_end and syncs:
            orbit_end_with_sync += 1
            first_sync_matches += int(syncs[0] == first_orbit_end[key] * stations)
        elif key not in first_orbit_end and syncs:
            sync_only_configurations += 1

    stored_syncs = [
        boundary for lane in rep["stores"]["sync"] for boundary in lane
    ]
    stored_sync_total = len(stored_syncs)
    stored_sync_on = sum(boundary % stations == 0 for boundary in stored_syncs)
    stored_sync_fraction = stored_sync_on / stored_sync_total
    result = {
        "certificate": "FINITE_REPLAY_TABLE",
        "census_configurations": len(census),
        "horizon_orbits": HORIZON,
        "controller_stations": stations,
        "configurations_with_global_clean_observation": len(first_global),
        "configurations_with_orbit_end_global_clean_observation": len(first_orbit_end),
        "configurations_without_global_clean_observation_within_horizon": (
            len(census) - len(first_global)
        ),
        "uncapped_predicate_event_totals": rep["totals"],
        "stored_sync_events_with_per_configuration_cap_4096": stored_sync_total,
        "stored_sync_on_orbit_boundary": stored_sync_on,
        "stored_sync_off_orbit_boundary": stored_sync_total - stored_sync_on,
        "stored_sync_on_orbit_boundary_fraction": round(stored_sync_fraction, 9),
        "stored_sync_on_orbit_boundary_percent": round(100 * stored_sync_fraction, 2),
        "first_sync_equals_first_orbit_end_global_clean": (
            f"{first_sync_matches}/{orbit_end_with_sync}"
        ),
        "sync_observed_without_orbit_end_global_clean": sync_only_configurations,
        "initialization_failures": rep["init_failures"],
        "deterministic_duplicate_mismatches": rep["duplicate_mismatches"],
        "final_columns_digest": rep["final_columns_digest"],
        "interpretation_boundary": (
            "finite controller-predicate table only; no framework Record or "
            "physical-time identification"
        ),
    }
    result["pass"] = bool(
        len(census) == 748
        and len(first_global) == 182
        and len(first_orbit_end) == 114
        and len(census) - len(first_global) == 566
        and rep["totals"] == {
            "bank0": 14_667_058,
            "bank1": 58_508_289,
            "global": 2_505_173,
            "sync": 6_821_527,
        }
        and stored_sync_total == 559_606
        and stored_sync_on == 79_267
        and stored_sync_total - stored_sync_on == 480_339
        and round(100 * stored_sync_fraction, 2) == 14.16
        and first_sync_matches == 25
        and orbit_end_with_sync == 114
        and sync_only_configurations == 624
        and rep["init_failures"] == 0
        and rep["duplicate_mismatches"] == 0
        and rep["final_columns_digest"]
        == "33fd167eaa0843246eb7446d8eb0203263f9d6153e76712c001534148853bf37"
    )
    return result


def cohort_certificate(rep, census) -> dict[str, object]:
    """Tabulate event-count rungs at first orbit-end clean observations."""

    stations = rep["stations"]
    first_orbit_end = rep["first_orbit_end_global_clean"]
    first_global = rep["first_global_clean_boundary"]
    event_count_rung: dict[Key, int] = {}
    censored = 0
    for lane, key in enumerate(census):
        if key not in first_orbit_end:
            continue
        boundary = first_orbit_end[key] * stations
        events = rep["stores"]["global"][lane]
        index = bisect_left(events, boundary)
        if index < len(events) and events[index] == boundary:
            event_count_rung[key] = index + 1
        else:
            censored += 1

    cohorts: dict[int, list[tuple[Key, int]]] = defaultdict(list)
    for key, rung in event_count_rung.items():
        cohorts[first_orbit_end[key]].append((key, rung))
    spread_histogram = Counter(
        max(rung for _key, rung in members)
        - min(rung for _key, rung in members)
        for members in cohorts.values()
    )
    multi_member = sum(len(members) > 1 for members in cohorts.values())

    rows = []
    for orbit, members in sorted(cohorts.items()):
        if len(members) < 2:
            continue
        base = min(rung for _key, rung in members)
        for key, rung in members:
            rows.append(
                {
                    "orbit": orbit,
                    "key": key,
                    "offset": rung - base,
                    "first_global_clean_boundary": first_global[key],
                }
            )

    by_first_boundary: dict[int, list[int]] = defaultdict(list)
    for row in rows:
        by_first_boundary[row["first_global_clean_boundary"]].append(row["offset"])
    violating_groups = {
        boundary: sorted(set(offsets))
        for boundary, offsets in by_first_boundary.items()
        if len(set(offsets)) != 1
    }
    collision_instances = sum(len(offsets) - 1 for offsets in by_first_boundary.values())
    offset_histogram = dict(sorted(Counter(row["offset"] for row in rows).items()))

    result = {
        "certificate": "FINITE_COHORT_TABLE",
        "event_count_rungs": len(event_count_rung),
        "rung_censored": censored,
        "orbit_index_cohorts": len(cohorts),
        "multi_member_cohorts": multi_member,
        "within_cohort_rung_spread_histogram": dict(sorted(spread_histogram.items())),
        "multi_member_rows": len(rows),
        "within_cohort_offset_histogram": offset_histogram,
        "first_clean_boundary_groups": len(by_first_boundary),
        "repeated_first_clean_boundary_instances": collision_instances,
        "groups_with_multiple_offsets": violating_groups,
        "interpretation_boundary": (
            "an exact finite table equality, not a universal predictor or physical law"
        ),
    }
    result["pass"] = bool(
        len(event_count_rung) == 114
        and censored == 0
        and len(cohorts) == 44
        and multi_member == 15
        and dict(sorted(spread_histogram.items())) == {0: 30, 1: 4, 2: 4, 4: 5, 5: 1}
        and len(rows) == 85
        and offset_histogram == {0: 41, 1: 15, 2: 13, 3: 9, 4: 6, 5: 1}
        and len(by_first_boundary) == 50
        and collision_instances == 35
        and not violating_groups
    )
    return result


def emit(payloads, started: float) -> int:
    checks = {payload["certificate"]: payload["pass"] for payload in payloads}
    summary = {
        "artifact": "cycles_863_865_finite_controller_clean_event_census",
        "checks": checks,
        "runtime_seconds": round(monotonic() - started, 3),
        "pass": all(checks.values()),
        "scope": "finite supplied controller corpus; no physical-time or Record-formation claim",
    }
    lines = ["CYCLE863_865_FINITE_CONTROLLER_CLEAN_EVENT_CENSUS"]
    for payload in payloads:
        status = "PASS" if payload["pass"] else "FAIL"
        lines.append(f"CERTIFICATE {payload['certificate']} {status} {compact(payload)}")
    lines.extend(
        (
            "N5_QUANTIFIER per_element: not_claimed",
            "N5_QUANTIFIER per_site: not_claimed",
            "N5_QUANTIFIER per_mode: not_claimed",
            "N5_QUANTIFIER per_block: one_declared_finite_controller_corpus",
            "N5_QUANTIFIER lattice_wide: not_claimed",
            "SUMMARY_JSON " + compact(summary),
            "CYCLE863_865_FINITE_CONTROLLER_CLEAN_EVENT_CENSUS_"
            + ("PASS" if summary["pass"] else "HONEST_FAIL"),
        )
    )
    output = "\n".join(lines) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if summary["pass"] else 1


def main() -> int:
    started = monotonic()
    controls = source_controls()
    if not controls["pass"]:
        return emit((controls,), started)

    program, seeds, census = independent_census()
    predicates = assemble_clean_predicates()
    replay = independent_replay(program, seeds, census, predicates)
    finite_replay = replay_certificate(replay, census)
    cohorts = cohort_certificate(replay, census)
    controls.update(
        {
            "controller_stations": len(program),
            "event_seed_count": len(seeds),
            "predicate_sizes": {
                "bank0": len(predicates["bank"][0]),
                "bank1": len(predicates["bank"][1]),
                "links": len(predicates["links"]),
                "global": len(predicates["global"]),
            },
            "runtime_below_declared_timeout": (
                monotonic() - started < AUDIT_TIMEOUT_SEC
            ),
        }
    )
    controls["pass"] = bool(
        controls["pass"]
        and controls["controller_stations"] == 11
        and controls["event_seed_count"] == 4
        and controls["runtime_below_declared_timeout"]
    )
    return emit((finite_replay, cohorts, controls), started)


if __name__ == "__main__":
    raise SystemExit(main())
