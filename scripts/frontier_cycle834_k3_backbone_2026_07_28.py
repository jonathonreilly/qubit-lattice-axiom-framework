#!/usr/bin/env python3
"""Cycle 834: exact k=3 separation backbone and cohort-law probe.

The finite ring has eleven stations.  Geometry below is only cyclic
separation arithmetic.  Dynamics is rebuilt from the landed Cycle-719 core;
the Cycle-801/824/831 science primaries are source anchors only and are
blocklisted from import.

The T=65536 status of the ten unresolved k=3 keys is a landed finite-horizon
status, not a claim that they remain open forever.  The forecast printed here
is pre-registered and conditional on extending the k=2 cohort pattern; it is
not counted as an observed result.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle801_deep_scan_independent_check_2026_07_28.py",
    "scripts/frontier_cycle824_k3_merger_probe_2026_07_28.py",
    "scripts/frontier_cycle831_deep_k2_forecast_tests_2026_07_28.py",
    "scripts/frontier_cycle831_cohorts_independent_check_2026_07_28.py",
)

import ast
from collections import Counter
from hashlib import sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(
    Path(path).stem for path in TEXT_AST_ONLY_PATHS
)


class _BlockedPrimaryFinder(importlib.abc.MetaPathFinder):
    """Fail closed if a source-only science primary is imported."""

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


FIREWALL = _BlockedPrimaryFinder()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_WIDTH_EXPECTED = 5815
WATCHED_COORDINATE_COUNT_EXPECTED = 477
OPEN_HORIZON = 65536
K3_CYCLE_PERIOD = 5952
FUNNEL_LAGS = tuple(range(1, 9))

Key = tuple[int, tuple[int, int, int], int]
CompiledWord = tuple[tuple[int, int, int, int], ...]
State = bytes

K3_REPRESENTATIVES = (
    (0, 2, 4),
    (0, 2, 5),
    (0, 2, 6),
    (0, 2, 7),
    (0, 2, 8),
    (0, 3, 6),
    (0, 3, 7),
)
LANDED_K3_ZERO_KEYS: tuple[Key, ...] = (
    (3, (0, 2, 4), 1),
    (3, (0, 2, 4), 2),
    (3, (0, 2, 5), 1),
    (3, (0, 2, 5), 2),
    (3, (0, 2, 5), 3),
    (3, (0, 2, 6), 1),
    (3, (0, 2, 6), 2),
    (3, (0, 2, 6), 3),
    (3, (0, 2, 7), 1),
    (3, (0, 2, 7), 2),
    (3, (0, 2, 7), 3),
    (3, (0, 2, 8), 1),
    (3, (0, 2, 8), 2),
    (3, (0, 2, 8), 3),
    (3, (0, 3, 6), 2),
    (3, (0, 3, 6), 3),
    (3, (0, 3, 7), 2),
    (3, (0, 3, 7), 3),
)
LANDED_K3_TRANSIENTS: tuple[tuple[Key, int], ...] = (
    ((3, (0, 2, 5), 2), 444),
    ((3, (0, 2, 5), 3), 532),
    ((3, (0, 2, 4), 1), 681),
    ((3, (0, 2, 4), 2), 1385),
)
LANDED_K3_CYCLES: tuple[tuple[Key, int], ...] = (
    ((3, (0, 2, 5), 1), 5952),
    ((3, (0, 2, 6), 1), 5952),
    ((3, (0, 2, 7), 1), 5952),
    ((3, (0, 2, 8), 1), 5952),
)
LANDED_K3_OPEN_THROUGH_65536: tuple[Key, ...] = (
    (3, (0, 2, 6), 2),
    (3, (0, 2, 6), 3),
    (3, (0, 2, 7), 2),
    (3, (0, 2, 7), 3),
    (3, (0, 2, 8), 2),
    (3, (0, 2, 8), 3),
    (3, (0, 3, 6), 2),
    (3, (0, 3, 6), 3),
    (3, (0, 3, 7), 2),
    (3, (0, 3, 7), 3),
)

K2_BACKBONE = (
    (1, 6),
    (1, 7),
    (2, 7),
    (2, 8),
    (3, 8),
    (3, 9),
    (4, 9),
    (4, 10),
    (5, 10),
)
K2_TRANSIENT_COHORTS = (
    {"event": 0, "moment": 14744, "size": 9},
    {"event": 2, "moment": 33195, "size": 9},
    {"event": 1, "moment": 51115, "size": 9},
)
K2_CYCLE_COHORT = {"event": 3, "period": 3, "size": 9}


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def state_sha256(state: State) -> str:
    return sha256(state).hexdigest()


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(sorted(
        (position + shift) % RING_STATIONS for position in positions
    ))


def pairwise_separated(positions: tuple[int, ...]) -> bool:
    occupied = frozenset(positions)
    return all(
        (position + 1) % RING_STATIONS not in occupied
        for position in occupied
    )


def k3_families(
) -> dict[tuple[int, int, int], tuple[tuple[int, int, int], ...]]:
    grouped: dict[
        tuple[int, int, int], set[tuple[int, int, int]]
    ] = {}
    for positions in combinations(range(RING_STATIONS), 3):
        if not pairwise_separated(positions):
            continue
        representative = min(
            rotate_positions(positions, shift)
            for shift in range(RING_STATIONS)
        )
        grouped.setdefault(representative, set()).add(positions)
    return {
        representative: tuple(sorted(alternatives))
        for representative, alternatives in sorted(grouped.items())
    }


def cyclic_forward_gaps(
    positions: tuple[int, int, int],
) -> tuple[int, int, int]:
    first, second, third = positions
    return (
        second - first,
        third - second,
        RING_STATIONS + first - third,
    )


def pairwise_cyclic_separations(
    positions: tuple[int, int, int],
) -> tuple[int, int, int]:
    return tuple(sorted(
        min(
            (right - left) % RING_STATIONS,
            (left - right) % RING_STATIONS,
        )
        for left, right in combinations(positions, 2)
    ))


def separation_class(
    positions: tuple[int, int, int],
) -> str:
    profile = pairwise_cyclic_separations(positions)
    return "PAIRWISE_SEPS_" + "_".join(str(value) for value in profile)


def saturated_run_class(
    positions: tuple[int, int, int],
) -> str:
    gap2_count = cyclic_forward_gaps(positions).count(2)
    return {
        0: "NO_SATURATED_GAP",
        1: "SINGLE_SATURATED_GAP",
        2: "DOUBLE_SATURATED_GAP_RUN",
    }[gap2_count]


def backbone_predicate(key: Key) -> bool:
    """Exact candidate: at least one pair attains allowed minimum 2."""

    return min(pairwise_cyclic_separations(key[1])) == 2


def geometry_certificate() -> dict[str, object]:
    families = k3_families()
    family_rows = tuple({
        "representative": representative,
        "rotation_orbit_size": len(alternatives),
        "forward_gaps": cyclic_forward_gaps(representative),
        "cyclic_gap_multiset":
            tuple(sorted(cyclic_forward_gaps(representative))),
        "pairwise_cyclic_separation_profile":
            pairwise_cyclic_separations(representative),
        "saturated_gap_count":
            cyclic_forward_gaps(representative).count(2),
        "saturated_run_class":
            saturated_run_class(representative),
        "candidate_backbone":
            min(pairwise_cyclic_separations(representative)) == 2,
    } for representative, alternatives in families.items())
    key_rows = tuple({
        "key": key,
        "positions": key[1],
        "event": key[2],
        "forward_gaps": cyclic_forward_gaps(key[1]),
        "pairwise_cyclic_separation_profile":
            pairwise_cyclic_separations(key[1]),
        "separation_class": separation_class(key[1]),
        "saturated_run_class": saturated_run_class(key[1]),
        "candidate_backbone": backbone_predicate(key),
    } for key in LANDED_K3_ZERO_KEYS)
    result = {
        "definitions": {
            "forward_gaps":
                "(p1-p0,p2-p1,11+p0-p2) for sorted positions",
            "pairwise_cyclic_separation":
                "min((b-a) mod 11,(a-b) mod 11) for each pair",
            "saturated_gap":
                "a forward cyclic gap equal to the admitted minimum 2",
            "candidate_backbone":
                "min(pairwise cyclic separation profile) == 2",
        },
        "configuration_count": sum(
            len(alternatives) for alternatives in families.values()
        ),
        "rotation_family_count": len(families),
        "family_rows": family_rows,
        "landed_k3_zero_key_count": len(LANDED_K3_ZERO_KEYS),
        "landed_position_event_rows": key_rows,
        "candidate_classes": (
            "SINGLE_SATURATED_GAP",
            "DOUBLE_SATURATED_GAP_RUN",
        ),
    }
    result["pass"] = (
        tuple(families) == K3_REPRESENTATIVES
        and result["configuration_count"] == 77
        and result["rotation_family_count"] == 7
        and len(LANDED_K3_ZERO_KEYS) == 18
        and len(set(LANDED_K3_ZERO_KEYS)) == 18
        and all(
            key[0] == 3
            and key[1] in families
            and key[2] in range(4)
            for key in LANDED_K3_ZERO_KEYS
        )
        and {
            row["pairwise_cyclic_separation_profile"]
            for row in family_rows
        } == {
            (2, 2, 4),
            (2, 3, 5),
            (2, 4, 5),
            (3, 3, 5),
            (3, 4, 4),
        }
    )
    return result


def class_census(
    geometry: dict[str, object],
) -> dict[str, object]:
    transient_by_key = dict(LANDED_K3_TRANSIENTS)
    cycle_by_key = dict(LANDED_K3_CYCLES)
    open_set = set(LANDED_K3_OPEN_THROUGH_65536)
    categories = {
        key: (
            "TRANSIENT"
            if key in transient_by_key
            else "CYCLE"
            if key in cycle_by_key
            else "OPEN_THROUGH_T65536"
            if key in open_set
            else "UNMAPPED"
        )
        for key in LANDED_K3_ZERO_KEYS
    }
    grouped: dict[str, list[Key]] = {}
    for key in LANDED_K3_ZERO_KEYS:
        grouped.setdefault(separation_class(key[1]), []).append(key)
    rows = []
    for class_name, keys in sorted(grouped.items()):
        counts = Counter(categories[key] for key in keys)
        rows.append({
            "separation_class": class_name,
            "profile": pairwise_cyclic_separations(keys[0][1]),
            "total": len(keys),
            "transient": counts["TRANSIENT"],
            "cycle": counts["CYCLE"],
            "resolved": counts["TRANSIENT"] + counts["CYCLE"],
            "open_through_T65536": counts["OPEN_THROUGH_T65536"],
            "keys_by_status": {
                status: tuple(
                    key for key in keys if categories[key] == status
                )
                for status in (
                    "TRANSIENT",
                    "CYCLE",
                    "OPEN_THROUGH_T65536",
                )
            },
        })
    candidate_keys = tuple(
        key for key in LANDED_K3_ZERO_KEYS if backbone_predicate(key)
    )
    candidate_open = tuple(
        key for key in candidate_keys if key in open_set
    )
    noncandidate_keys = tuple(
        key for key in LANDED_K3_ZERO_KEYS
        if not backbone_predicate(key)
    )
    resolved_set = (
        set(transient_by_key) | set(cycle_by_key)
    )
    expected_open = (
        set(LANDED_K3_ZERO_KEYS) - resolved_set
    )
    result = {
        "landed_resolutions": {
            "transients": LANDED_K3_TRANSIENTS,
            "cycles_entry0": LANDED_K3_CYCLES,
            "other_landed_k3_resolutions": (),
        },
        "class_census": tuple(rows),
        "candidate_backbone": {
            "predicate":
                "minimum pairwise cyclic separation equals 2",
            "keys": candidate_keys,
            "total": len(candidate_keys),
            "transient": sum(
                key in transient_by_key for key in candidate_keys
            ),
            "cycle": sum(key in cycle_by_key for key in candidate_keys),
            "resolved": sum(key in resolved_set for key in candidate_keys),
            "open_through_T65536": candidate_open,
            "open_count": len(candidate_open),
            "contains_all_landed_k3_resolutions":
                resolved_set <= set(candidate_keys),
        },
        "outside_candidate": {
            "keys": noncandidate_keys,
            "resolved": tuple(
                key for key in noncandidate_keys if key in resolved_set
            ),
            "open_through_T65536": tuple(
                key for key in noncandidate_keys if key in open_set
            ),
        },
        "total_census": {
            "keys": len(LANDED_K3_ZERO_KEYS),
            "transient": len(LANDED_K3_TRANSIENTS),
            "cycle": len(LANDED_K3_CYCLES),
            "open_through_T65536":
                len(LANDED_K3_OPEN_THROUGH_65536),
        },
    }
    result["pass"] = (
        bool(geometry["pass"])
        and not any(status == "UNMAPPED" for status in categories.values())
        and len(resolved_set) == 8
        and expected_open == open_set
        and len(candidate_keys) == 14
        and len(candidate_open) == 6
        and resolved_set <= set(candidate_keys)
        and not result["outside_candidate"]["resolved"]
        and sum(row["total"] for row in rows) == 18
        and sum(row["resolved"] for row in rows) == 8
        and sum(row["open_through_T65536"] for row in rows) == 10
    )
    return result


def build_fixtures(
    program: tuple[object, ...],
) -> tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        rows.append((event, direction, before))
        state = K.A.apply_semantic(before, allocator)
    return tuple(rows)


def synchronous_word(
    program: tuple[object, ...],
    token_positions: tuple[int, ...],
) -> tuple[object, ...]:
    positions = tuple(token_positions)
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


def compile_word(word: tuple[object, ...]) -> CompiledWord:
    compiled = []
    for gate in word:
        kind = str(gate.kind)
        wires = tuple(int(wire) for wire in gate.wires)
        if kind == "X" and len(wires) == 1:
            compiled.append((1, wires[0], -1, -1))
        elif kind == "CNOT" and len(wires) == 2:
            compiled.append((2, wires[0], wires[1], -1))
        elif kind == "TOF" and len(wires) == 3:
            compiled.append((3, wires[0], wires[1], wires[2]))
        else:
            raise AssertionError(("unsupported gate", kind, wires))
    return tuple(compiled)


def advance_state(
    state: list[int],
    compiled: CompiledWord,
) -> None:
    for kind, first, second, third in compiled:
        if kind == 1:
            state[first] ^= 1
        elif kind == 2:
            state[second] ^= state[first]
        else:
            state[third] ^= state[first] & state[second]


def one_changed_coordinate(
    left: tuple[int, ...], right: tuple[int, ...]
) -> int:
    changed = tuple(
        index
        for index, (left_bit, right_bit) in enumerate(zip(left, right))
        if left_bit != right_bit
    )
    if len(left) != len(right) or len(changed) != 1:
        raise AssertionError(("coordinate basis", len(changed)))
    return changed[0]


def watched_coordinate_basis() -> dict[str, object]:
    banks0, links0 = K.B.chain_genesis(FIXTURE_BANKS)
    packed = K.M.pack_state(banks0, links0)
    banks, links = K.M.unpack_state(packed, FIXTURE_BANKS)
    indices = {int(K.R3.X.SOURCE_POINTER)}
    watched_registers = (
        K.A.POINTER,
        K.A.U_TO_V,
        K.A.V_TO_U,
        K.A.DIRECTION_OK,
        *K.A.FRESH,
        *K.A.ZERO_WORK,
        K.A.TOKEN_OK,
    )
    for bank_index in range(FIXTURE_BANKS):
        for wire in watched_registers:
            changed_banks = [list(bank) for bank in banks]
            changed_links = [list(link) for link in links]
            changed_banks[bank_index][wire] ^= 1
            changed = K.M.pack_state(
                tuple(tuple(bank) for bank in changed_banks),
                tuple(tuple(link) for link in changed_links),
            )
            indices.add(one_changed_coordinate(packed, changed))
    for link_index, link in enumerate(links):
        for wire in range(len(link)):
            changed_banks = [list(bank) for bank in banks]
            changed_links = [list(item) for item in links]
            changed_links[link_index][wire] ^= 1
            changed = K.M.pack_state(
                tuple(tuple(bank) for bank in changed_banks),
                tuple(tuple(item) for item in changed_links),
            )
            indices.add(one_changed_coordinate(packed, changed))
    result = {
        "indices": tuple(sorted(indices)),
        "state_width": len(packed),
        "watched_coordinate_count": len(indices),
    }
    result["pass"] = (
        result["state_width"] == STATE_WIDTH_EXPECTED
        and result["watched_coordinate_count"]
        == WATCHED_COORDINATE_COUNT_EXPECTED
    )
    return result


def is_clean(
    state: State | list[int],
    watched_indices: tuple[int, ...],
) -> bool:
    return not any(state[index] for index in watched_indices)


def initial_and_compiled(
    key: Key,
    program: tuple[object, ...],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
) -> tuple[tuple[int, ...], CompiledWord]:
    fixture_by_event = {
        event: before for event, _direction, before in fixtures
    }
    word = synchronous_word(program, key[1])
    initial = K.A.apply_semantic(fixture_by_event[key[2]], word)
    return initial, compile_word(word)


def capture_trajectory(
    initial: tuple[int, ...],
    compiled: CompiledWord,
    end_t: int,
) -> tuple[State, ...]:
    state = [int(bit) for bit in initial]
    rows = []
    for horizon_t in range(end_t + 1):
        rows.append(bytes(state))
        if horizon_t < end_t:
            advance_state(state, compiled)
    return tuple(rows)


def equality_groups(
    states: tuple[State, ...],
) -> tuple[tuple[int, ...], ...]:
    groups: dict[State, list[int]] = {}
    for index, state in enumerate(states):
        groups.setdefault(state, []).append(index)
    return tuple(sorted(
        tuple(indices)
        for indices in groups.values()
        if len(indices) >= 2
    ))


def transient_cohort_probe(
    program: tuple[object, ...],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    watched_indices: tuple[int, ...],
) -> dict[str, object]:
    keys = tuple(key for key, _moment in LANDED_K3_TRANSIENTS)
    moments = dict(LANDED_K3_TRANSIENTS)
    trajectories = {}
    for key in keys:
        initial, compiled = initial_and_compiled(key, program, fixtures)
        trajectories[key] = capture_trajectory(
            initial, compiled, moments[key]
        )

    same_time_rows = []
    for left_index, right_index in combinations(range(len(keys)), 2):
        left_key = keys[left_index]
        right_key = keys[right_index]
        shared_stop = min(moments[left_key], moments[right_key])
        exact_times = tuple(
            horizon_t
            for horizon_t in range(shared_stop)
            if trajectories[left_key][horizon_t]
            == trajectories[right_key][horizon_t]
        )
        same_time_rows.append({
            "key_indices": (left_index, right_index),
            "keys": (left_key, right_key),
            "strict_pre_resolution_shared_domain": (0, shared_stop - 1),
            "exact_full_state_coincidence_times": exact_times,
        })

    lag_rows = []
    for lag in FUNNEL_LAGS:
        states = tuple(
            trajectories[key][moments[key] - lag] for key in keys
        )
        lag_rows.append({
            "lag_from_own_resolution": lag,
            "times": tuple(moments[key] - lag for key in keys),
            "exact_equality_groups": equality_groups(states),
            "all_four_exactly_equal": len(set(states)) == 1,
        })

    minus_five = tuple({
        "key": key,
        "time": moments[key] - 5,
        "state_sha256_label_only":
            state_sha256(trajectories[key][moments[key] - 5]),
    } for key in keys)
    identity_rows = tuple({
        "key": key,
        "expected_first_clean": moments[key],
        "clean_times_through_resolution": tuple(
            horizon_t
            for horizon_t, state in enumerate(trajectories[key])
            if is_clean(state, watched_indices)
        ),
    } for key in keys)
    event2_indices = tuple(
        index for index, key in enumerate(keys) if key[2] == 2
    )
    event2_lag_matches = tuple(
        row["lag_from_own_resolution"]
        for row in lag_rows
        if any(
            set(event2_indices) <= set(group)
            for group in row["exact_equality_groups"]
        )
    )
    all_moments = tuple(moments[key] for key in keys)
    result = {
        "key_index": tuple(enumerate(keys)),
        "moments": tuple((key, moments[key]) for key in keys),
        "shared_resolution_moment": len(set(all_moments)) == 1,
        "pairwise_same_time_map": tuple(same_time_rows),
        "any_pairwise_same_time_pre_resolution": any(
            row["exact_full_state_coincidence_times"]
            for row in same_time_rows
        ),
        "time_shift_definition":
            "compare every key at own resolution moment minus d, d=1..8",
        "own_moment_lag_map": tuple(lag_rows),
        "all_four_common_lags": tuple(
            row["lag_from_own_resolution"]
            for row in lag_rows if row["all_four_exactly_equal"]
        ),
        "resolved_event2_pair_common_lags": event2_lag_matches,
        "moment_minus_5": minus_five,
        "moment_minus_5_distinct_state_count":
            len({row["state_sha256_label_only"] for row in minus_five}),
        "identity_rows": identity_rows,
        "synchronized_cohort_observed": False,
        "outcome":
            "NO_K3_TRANSIENT_SYNCHRONIZATION_IN_THE_LANDED_FOUR",
    }
    result["pass"] = (
        len(keys) == 4
        and all_moments == (444, 532, 681, 1385)
        and len(set(all_moments)) == 4
        and len(same_time_rows) == 6
        and not result["any_pairwise_same_time_pre_resolution"]
        and not result["all_four_common_lags"]
        and not event2_lag_matches
        and result["moment_minus_5_distinct_state_count"] == 4
        and all(
            row["clean_times_through_resolution"]
            == (row["expected_first_clean"],)
            for row in identity_rows
        )
    )
    return result


def cycle_cohort_probe(
    program: tuple[object, ...],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    watched_indices: tuple[int, ...],
) -> dict[str, object]:
    keys = tuple(key for key, _period in LANDED_K3_CYCLES)
    initial_and_words = tuple(
        initial_and_compiled(key, program, fixtures) for key in keys
    )
    states = [
        [int(bit) for bit in initial]
        for initial, _compiled in initial_and_words
    ]
    initials = tuple(bytes(state) for state in states)
    return_times: list[list[int]] = [[] for _key in keys]
    nonclean_counts = [0 for _key in keys]
    identical_phase_count = 0
    trace_hashes = [sha256() for _key in keys]
    for horizon_t in range(K3_CYCLE_PERIOD):
        current = tuple(bytes(state) for state in states)
        for lane, state in enumerate(current):
            trace_hashes[lane].update(state)
            nonclean_counts[lane] += not is_clean(
                state, watched_indices
            )
            if horizon_t > 0 and state == initials[lane]:
                return_times[lane].append(horizon_t)
        identical_phase_count += len(set(current)) == 1
        for state, (_initial, compiled) in zip(
            states, initial_and_words
        ):
            advance_state(state, compiled)
    closures = tuple(bytes(state) for state in states)
    trajectory_hashes = tuple(
        hasher.hexdigest() for hasher in trace_hashes
    )
    result = {
        "keys": keys,
        "period": K3_CYCLE_PERIOD,
        "initial_states_exactly_equal": len(set(initials)) == 1,
        "identical_in_phase_count": identical_phase_count,
        "identical_in_phase_every_t0_through_t5951":
            identical_phase_count == K3_CYCLE_PERIOD,
        "earlier_exact_return_times":
            tuple(tuple(rows) for rows in return_times),
        "exact_closure_at_5952": tuple(
            closure == initial
            for closure, initial in zip(closures, initials)
        ),
        "nonclean_phase_counts": tuple(nonclean_counts),
        "trajectory_sha256": trajectory_hashes,
        "all_four_trajectory_sha256_equal":
            len(set(trajectory_hashes)) == 1,
        "outcome":
            "FOUR_PERIOD_5952_CYCLES_IDENTICAL_IN_PHASE",
    }
    result["pass"] = (
        len(keys) == 4
        and result["initial_states_exactly_equal"]
        and result["identical_in_phase_every_t0_through_t5951"]
        and all(not rows for rows in return_times)
        and all(result["exact_closure_at_5952"])
        and all(
            count == K3_CYCLE_PERIOD for count in nonclean_counts
        )
        and result["all_four_trajectory_sha256_equal"]
    )
    return result


def forecast_surface(
    mapping: dict[str, object],
) -> dict[str, object]:
    open_keys = tuple(
        mapping["candidate_backbone"]["open_through_T65536"]
    )
    event_rows = tuple({
        "event": event,
        "open_keys": tuple(
            key for key in open_keys if key[2] == event
        ),
        "count": sum(key[2] == event for key in open_keys),
        "pre_registered_prediction": (
            "the listed keys first resolve at one common horizon with "
            "one common outcome; if transient, their exact full states "
            "at resolution-minus-5 are equal; if cyclic, their minimal "
            "periods agree and their phase relation is reported exactly"
        ),
    } for event in sorted({key[2] for key in open_keys}))
    result = {
        "status": "PRE_REGISTERED_UNTESTED_CONDITIONAL_FORECAST",
        "derivation_scope":
            "conditional extension of the k=2 per-event cohort pattern",
        "standing_prediction_surface": open_keys,
        "per_event_forecasts": event_rows,
        "success_criterion":
            "each three-key event row satisfies its complete prediction",
        "falsifier":
            "within either event row, different first terminal horizons, "
            "different terminal outcomes, a transient minus-5 mismatch, "
            "or a cyclic period mismatch",
        "not_observed_data": True,
        "broad_k3_transient_law_already_supported": False,
    }
    result["pass"] = (
        len(open_keys) == 6
        and tuple(row["event"] for row in event_rows) == (2, 3)
        and all(row["count"] == 3 for row in event_rows)
        and set(open_keys)
        == {
            (3, (0, 2, 6), 2),
            (3, (0, 2, 7), 2),
            (3, (0, 2, 8), 2),
            (3, (0, 2, 6), 3),
            (3, (0, 2, 7), 3),
            (3, (0, 2, 8), 3),
        }
        and result["not_observed_data"]
    )
    return result


def run_science_probe() -> dict[str, object]:
    geometry = geometry_certificate()
    mapping = class_census(geometry)
    program = K.interleaved_program(FIXTURE_BANKS)
    fixtures = build_fixtures(program)
    basis = watched_coordinate_basis()
    transients = transient_cohort_probe(
        program, fixtures, tuple(basis["indices"])
    )
    cycles = cycle_cohort_probe(
        program, fixtures, tuple(basis["indices"])
    )
    forecast = forecast_surface(mapping)
    result = {
        "A_KEY_GEOMETRY": geometry,
        "B_RESOLVED_SET_MAPPING": mapping,
        "C_COHORT_TEST": {
            "transients": transients,
            "cycles": cycles,
            "forecast": forecast,
            "pass":
                transients["pass"]
                and cycles["pass"]
                and forecast["pass"],
        },
        "basis": {
            key: value for key, value in basis.items()
            if key != "indices"
        },
    }
    result["pass"] = (
        geometry["pass"]
        and mapping["pass"]
        and basis["pass"]
        and result["C_COHORT_TEST"]["pass"]
    )
    return result


def run() -> int:
    started = monotonic()
    science = run_science_probe()
    elapsed = monotonic() - started
    report = {
        "cycle": 834,
        "status": "A_TO_C_INCREMENT",
        "checks": {
            "A_KEY_GEOMETRY": science["A_KEY_GEOMETRY"]["pass"],
            "B_RESOLVED_SET_MAPPING":
                science["B_RESOLVED_SET_MAPPING"]["pass"],
            "C_COHORT_TEST": science["C_COHORT_TEST"]["pass"],
        },
        "runtime_seconds": round(elapsed, 6),
        "pass": science["pass"] and elapsed < AUDIT_TIMEOUT_SEC,
    }
    output = "\n".join((
        "CYCLE834_K3_BACKBONE",
        "CERTIFICATE_A=" + compact(science["A_KEY_GEOMETRY"]),
        "CERTIFICATE_B=" + compact(science["B_RESOLVED_SET_MAPPING"]),
        "CERTIFICATE_C=" + compact(science["C_COHORT_TEST"]),
        "REPORT=" + compact(report),
    )) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout limit exceeded")
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        failure = {
            "pass": False,
            "terminal": "CYCLE834_K3_BACKBONE_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
