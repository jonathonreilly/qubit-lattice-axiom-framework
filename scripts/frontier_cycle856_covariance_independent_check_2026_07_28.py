#!/usr/bin/env python3
"""Independent adversarial check of Cycle-856 monitor covariance.

The Cycle-856 source under test is a SHA-pinned, text/AST-only reference.  Its
runtime implementation is import-blocked.  This checker imports only the
landed Cycle-719 computational core and supplies its own Boolean state
evaluator, controller schedule, long-horizon stamp census, group action, and
absolute-record analysis.
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
from typing import Callable, Iterable


AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle856_record_covariance_2026_07_28.py",
)
COMPUTATIONAL_INPUT_PATHS = (AUDIT_INPUT_PATHS[0],)
TEXT_AST_ONLY_PATHS = (AUDIT_INPUT_PATHS[1],)
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "20bce7f6dab9d7755ddefc6e2000d501acb8572dc15f50981b65ba9f6e2a4f2b",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "fc873d0b1947866b238bbe5456ffe89fcd072a21",
}
EXPECTED_BASE_STAMP_SHA256 = {
    "E1": "1901e01751642cf1cd04054ab011fe39b9d384488b07c419e7b9a7e041b7ce52",
    "E2": "bea94bc5b3fb7e4d41cdaa32e565e8f659d40dae17c3c44934bb0ebd0da4181a",
}

FIXTURE_BANKS = 2
MIN_SOURCES = 2
MAX_SOURCES = 5
TRAJECTORY_HORIZON = 51_115
READINGS = ("E1", "E2")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _SourcePrimaryFirewall(importlib.abc.MetaPathFinder):
    """Refuse every attempt to import the Cycle-856 source under test."""

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
            raise ImportError(f"BLOCKLIST forbids source-primary import: {fullname}")
        return None


SOURCE_PRIMARY_FIREWALL = _SourcePrimaryFirewall()
sys.meta_path.insert(0, SOURCE_PRIMARY_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, int, tuple[int, ...]]
State = tuple[int, ...]
Selection = frozenset[Key]


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    prefix = f"blob {len(payload)}\0".encode("ascii")
    return sha1(prefix + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            targets = node.targets
        elif isinstance(node, ast.AnnAssign):
            targets = (node.target,)
        else:
            continue
        if any(isinstance(target, ast.Name) and target.id == name
               for target in targets):
            values.append(node.value)
    if len(values) != 1:
        return None
    try:
        return ast.literal_eval(values[0])
    except (TypeError, ValueError):
        return None


def source_controls() -> dict[str, object]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {path: ast.parse(payload, filename=path)
             for path, payload in payloads.items()}
    self_path = Path(__file__)
    self_tree = ast.parse(self_path.read_bytes(), filename=self_path.name)
    sha_rows = {path: sha256(payload).hexdigest()
                for path, payload in payloads.items()}
    blob_rows = {path: git_blob(payload) for path, payload in payloads.items()}
    imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    source_tree = trees[TEXT_AST_ONLY_PATHS[0]]
    source_function_names = tuple(sorted(
        node.name for node in source_tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ))
    required_source_functions = {
        "base_stamp_census", "monitor_lift", "monitor_stamp_sets",
        "mixed_orbit_report", "intertwining_report",
        "monitor_dependence_report",
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS") == AUDIT_INPUT_PATHS,
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
        "source_primary_AST_top_level_nodes": len(source_tree.body),
        "source_primary_required_functions_present":
            required_source_functions <= set(source_function_names),
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(SOURCE_PRIMARY_FIREWALL.hits),
        "direct_frontier_imports": imports,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and result["source_primary_AST_top_level_nodes"] > 0
        and result["source_primary_required_functions_present"]
        and imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


def separated(positions: tuple[int, ...], stations: int) -> bool:
    occupied = set(positions)
    return all((position + 1) % stations not in occupied for position in occupied)


def rotate_key(key: Key, shift: int, stations: int) -> Key:
    k, event, positions = key
    return k, event, tuple(sorted((position + shift) % stations
                                  for position in positions))


def build_scope() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    stations = len(program)
    skeleton = tuple(sorted(
        (k, event, positions)
        for k in range(MIN_SOURCES, MAX_SOURCES + 1)
        for positions in combinations(range(stations), k)
        if separated(positions, stations)
        for event in range(2 * FIXTURE_BANKS)
    ))
    unseen = set(skeleton)
    orbits = []
    while unseen:
        representative = min(unseen)
        orbit = tuple(sorted({rotate_key(representative, shift, stations)
                              for shift in range(stations)}))
        if not set(orbit) <= set(skeleton):
            raise AssertionError(("orbit closure", representative))
        orbits.append(orbit)
        unseen.difference_update(orbit)
    result = {
        "program": program,
        "stations": stations,
        "census": skeleton,
        "orbits": tuple(sorted(orbits, key=lambda orbit: orbit[0])),
        "per_k": dict(sorted(Counter(key[0] for key in skeleton).items())),
    }
    result["pass"] = (
        stations == 11
        and len(skeleton) == 748
        and len(result["orbits"]) == 68
        and all(len(orbit) == 11 for orbit in result["orbits"])
    )
    return result


def apply_gate(state: list[int], gate: object) -> None:
    """Independent scalar truth-table evaluator for the landed gate alphabet."""

    if gate.kind == "X":
        state[gate.wires[0]] ^= 1
    elif gate.kind == "CNOT":
        control, target = gate.wires
        state[target] ^= state[control]
    elif gate.kind == "TOF":
        first, second, target = gate.wires
        state[target] ^= state[first] & state[second]
    else:
        raise ValueError(("unsupported gate", gate.kind, gate.wires))


def apply_word(initial: State, word: Iterable[object]) -> State:
    state = list(initial)
    for gate in word:
        apply_gate(state, gate)
    return tuple(state)


def controller_orbit(
    initial: State,
    program: tuple[object, ...],
    token_positions: tuple[int, ...],
) -> State:
    """Execute Q-before-R directly, without Cycle-719's orbit evaluator."""

    positions = tuple(token_positions)
    state = initial
    for _chunk in range(len(program)):
        for station in sorted(positions):
            state = apply_word(state, K.mapped_macro(program[station]))
        positions = tuple((position + 1) % len(program) for position in positions)
    if tuple(sorted(positions)) != tuple(sorted(token_positions)):
        raise AssertionError(("controller return", token_positions, positions))
    return state


def derive_event_seeds(program: tuple[object, ...]) -> tuple[tuple[int, State], ...]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        rows.append((event, before))
        state = controller_orbit(before, program, (0,))
    return tuple(rows)


def setup_states(scope: dict[str, object]) -> tuple[State, ...]:
    program = scope["program"]
    census = scope["census"]
    seeds = dict(derive_event_seeds(program))
    states = tuple(
        controller_orbit(seeds[event], program, positions)
        for _k, event, positions in census
    )
    if len({len(state) for state in states}) != 1:
        raise AssertionError("nonuniform state widths")
    return states


def watched_local_wires() -> tuple[int, ...]:
    return (
        K.A.POINTER, K.A.U_TO_V, K.A.V_TO_U, K.A.DIRECTION_OK,
        *K.A.FRESH, *K.A.ZERO_WORK, K.A.TOKEN_OK,
    )


def marker_index(baseline: State, marked: State) -> int:
    differences = tuple(index for index, pair in enumerate(zip(baseline, marked))
                        if pair[0] != pair[1])
    if len(differences) != 1:
        raise AssertionError(("non-coordinate packing marker", differences))
    return differences[0]


def dirty_coordinates() -> tuple[int, ...]:
    """Recover the clean predicate from independent packing-coordinate probes."""

    bank_fixture, link_fixture = K.B.chain_genesis(FIXTURE_BANKS)
    zero_banks = tuple(tuple(0 for _ in bank) for bank in bank_fixture)
    zero_links = tuple(tuple(0 for _ in link) for link in link_fixture)
    baseline = K.M.pack_state(zero_banks, zero_links)
    dirty = {K.R3.X.SOURCE_POINTER}
    for bank_index in range(len(zero_banks)):
        for wire in watched_local_wires():
            banks = [list(bank) for bank in zero_banks]
            banks[bank_index][wire] = 1
            marked = K.M.pack_state(tuple(map(tuple, banks)), zero_links)
            dirty.add(marker_index(baseline, marked))
    for link_index, link in enumerate(zero_links):
        for wire in range(len(link)):
            links = [list(row) for row in zero_links]
            links[link_index][wire] = 1
            marked = K.M.pack_state(zero_banks, tuple(map(tuple, links)))
            dirty.add(marker_index(baseline, marked))
    return tuple(sorted(dirty))


def pack_lanes(states: tuple[State, ...]) -> list[int]:
    return [
        sum(bit << lane for lane, bit in enumerate(column))
        for column in zip(*states)
    ]


def bit_gate_line(gate: object, mask: int) -> str:
    if gate.kind == "X":
        return f" c[{gate.wires[0]}] ^= {mask}"
    if gate.kind == "CNOT":
        control, target = gate.wires
        return f" c[{target}] ^= c[{control}] & {mask}"
    if gate.kind == "TOF":
        first, second, target = gate.wires
        return f" c[{target}] ^= c[{first}] & c[{second}] & {mask}"
    raise ValueError(("unsupported gate", gate.kind, gate.wires))


def compile_chunks(
    program: tuple[object, ...],
    census: tuple[Key, ...],
) -> tuple[tuple[Callable[[list[int]], None], ...], tuple[int, ...]]:
    """Compile independently constructed Q-before-R chunk words.

    Every census lane is duplicated in the upper half of each integer.  The
    duplicate receives the same independently constructed gate masks, making
    every clean boundary and the final full state a simultaneous determinism
    replay of all 748 setups.
    """

    lanes = len(census)
    functions = []
    gate_counts = []
    for chunk in range(len(program)):
        source = ["def apply_chunk(c):"]
        count = 0
        for station, row in enumerate(program):
            base_mask = sum(
                1 << lane
                for lane, (_k, _event, positions) in enumerate(census)
                if (station - chunk) % len(program) in positions
            )
            if not base_mask:
                continue
            doubled_mask = base_mask | (base_mask << lanes)
            for gate in K.mapped_macro(row):
                source.append(bit_gate_line(gate, doubled_mask))
                count += 1
        namespace: dict[str, object] = {}
        exec("\n".join(source), {"__builtins__": {}}, namespace)
        functions.append(namespace["apply_chunk"])
        gate_counts.append(count)
    return tuple(functions), tuple(gate_counts)  # type: ignore[return-value]


def clean_lanes(columns: list[int], dirty: tuple[int, ...], full_mask: int) -> int:
    dirty_mask = 0
    for coordinate in dirty:
        dirty_mask |= columns[coordinate]
    return full_mask & ~dirty_mask


def selected_keys(mask: int, census: tuple[Key, ...]) -> Selection:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(census[bit.bit_length() - 1])
        mask ^= bit
    return frozenset(rows)


def independent_stamp_census(scope: dict[str, object]) -> dict[str, object]:
    started = monotonic()
    census = scope["census"]
    states = setup_states(scope)
    lanes = len(census)
    low_mask = (1 << lanes) - 1
    full_mask = (1 << (2 * lanes)) - 1
    columns = pack_lanes(states + states)
    chunks, gate_counts = compile_chunks(scope["program"], census)
    dirty = dirty_coordinates()
    trace_hash = sha256()
    mismatching_boundaries = 0
    mismatching_lane_observations = 0

    def observe() -> int:
        nonlocal mismatching_boundaries, mismatching_lane_observations
        all_clean = clean_lanes(columns, dirty, full_mask)
        low = all_clean & low_mask
        high = (all_clean >> lanes) & low_mask
        mismatch = low ^ high
        mismatching_boundaries += bool(mismatch)
        mismatching_lane_observations += mismatch.bit_count()
        trace_hash.update(low.to_bytes((lanes + 7) // 8, "little"))
        return low

    initial = observe()
    e1_mask = initial
    e2_mask = initial
    for _orbit in range(TRAJECTORY_HORIZON):
        orbit_end = 0
        for apply_chunk in chunks:
            apply_chunk(columns)
            orbit_end = observe()
            e1_mask |= orbit_end
        e2_mask |= orbit_end

    final_halves_exact = all(
        (column & low_mask) == ((column >> lanes) & low_mask)
        for column in columns
    )
    e1 = selected_keys(e1_mask, census)
    e2 = selected_keys(e2_mask, census)
    setup_catalog_sha = digest(tuple(
        sha256(bytes(state)).hexdigest() for state in states
    ))
    result = {
        "E1": e1,
        "E2": e2,
        "counts": {"E1": len(e1), "E2": len(e2)},
        "selection_sha256": {
            "E1": digest(tuple(sorted(e1))),
            "E2": digest(tuple(sorted(e2))),
        },
        "setup_catalog_sha256": setup_catalog_sha,
        "state_bits": len(states[0]),
        "dirty_coordinate_count": len(dirty),
        "chunk_gate_counts": gate_counts,
        "observed_boundaries": 1 + TRAJECTORY_HORIZON * len(chunks),
        "clean_boundary_trace_sha256": trace_hash.hexdigest(),
        "determinism": {
            "duplicated_setups": lanes,
            "mismatching_boundaries": mismatching_boundaries,
            "mismatching_lane_observations": mismatching_lane_observations,
            "final_full_state_halves_exact": final_halves_exact,
        },
        "runtime_seconds": round(monotonic() - started, 6),
    }
    result["pass"] = (
        result["counts"] == {"E1": 182, "E2": 114}
        and e2 <= e1
        and result["selection_sha256"] == EXPECTED_BASE_STAMP_SHA256
        and setup_catalog_sha
            == "92d2be9fa831eacea635faf96d2e9c456063da7336e45f62beff6f840b9f1287"
        and result["state_bits"] == 5815
        and result["dirty_coordinate_count"] == 477
        and gate_counts == (3106,) * 11
        and result["observed_boundaries"] == 562_266
        and mismatching_boundaries == 0
        and mismatching_lane_observations == 0
        and final_halves_exact
    )
    return result


def range_encode(indices: Iterable[int]) -> str:
    values = sorted(set(indices))
    if not values:
        return ""
    ranges = []
    start = previous = values[0]
    for value in values[1:]:
        if value == previous + 1:
            previous = value
            continue
        ranges.append(str(start) if start == previous else f"{start}-{previous}")
        start = previous = value
    ranges.append(str(start) if start == previous else f"{start}-{previous}")
    return ",".join(ranges)


def mixed_census(scope: dict[str, object], stamps: dict[str, object]) -> dict[str, object]:
    tables = {}
    for reading in READINGS:
        selection = stamps[reading]
        classes = Counter()
        histogram = Counter()
        class_indices: dict[str, list[int]] = defaultdict(list)
        for orbit_index, orbit in enumerate(scope["orbits"]):
            count = sum(key in selection for key in orbit)
            label = (
                "uniform-stamped" if count == scope["stations"] else
                "uniform-silent" if count == 0 else
                "mixed"
            )
            classes[label] += 1
            histogram[count] += 1
            class_indices[label].append(orbit_index)
        tables[reading] = {
            "stamped_setups": len(selection),
            "uniform_stamped_orbits": classes["uniform-stamped"],
            "uniform_silent_orbits": classes["uniform-silent"],
            "mixed_orbits": classes["mixed"],
            "stamped_members_per_orbit": dict(sorted(histogram.items())),
            "orbit_indices_by_class": {
                label: range_encode(indices)
                for label, indices in sorted(class_indices.items())
            },
        }
    result = {
        "orbit_encoding": (
            "orbit indices address the lexicographically sorted 68-orbit "
            "partition of the independently generated 748-setup census"
        ),
        "by_reading": tables,
    }
    result["pass"] = (
        tables["E1"]["stamped_setups"] == 182
        and tables["E1"]["uniform_stamped_orbits"] == 3
        and tables["E1"]["uniform_silent_orbits"] == 12
        and tables["E1"]["mixed_orbits"] == 53
        and tables["E2"]["stamped_setups"] == 114
        and tables["E2"]["uniform_stamped_orbits"] == 0
        and tables["E2"]["uniform_silent_orbits"] == 38
        and tables["E2"]["mixed_orbits"] == 30
        and all(
            row["uniform_stamped_orbits"]
            + row["uniform_silent_orbits"]
            + row["mixed_orbits"] == 68
            for row in tables.values()
        )
    )
    return result


def gate_signature(gate: object) -> tuple[str, tuple[int, ...]]:
    return gate.kind, tuple(gate.wires)


def exact_chunk_manifest(
    program: tuple[object, ...], active: tuple[int, ...]
) -> tuple[tuple[int, tuple[tuple[str, tuple[int, ...]], ...]], ...]:
    return tuple(
        (station, tuple(gate_signature(gate)
                        for gate in K.mapped_macro(program[station])))
        for station in sorted(active)
    )


def phase_lift(scope: dict[str, object]) -> dict[str, object]:
    """Test the lift at exact ordered gate-word/chunk granularity."""

    program = scope["program"]
    census = scope["census"]
    stations = scope["stations"]
    manifest_cache = {
        active: exact_chunk_manifest(program, active)
        for k in range(MIN_SOURCES, MAX_SOURCES + 1)
        for active in combinations(range(stations), k)
    }
    failures = []
    action_failures = []
    chunk_comparisons = 0
    for key in census:
        for monitor in range(stations):
            moved = rotate_key(key, monitor, stations)
            if moved[1] != key[1] and len(failures) < 12:
                failures.append(("event-changed", key, monitor, moved))
            for chunk in range(stations):
                left_active = tuple(sorted(
                    (position + monitor + chunk) % stations
                    for position in key[2]
                ))
                right_active = tuple(sorted(
                    (position + chunk) % stations for position in moved[2]
                ))
                left = manifest_cache[left_active]
                right = manifest_cache[right_active]
                chunk_comparisons += 1
                if left != right and len(failures) < 12:
                    failures.append({
                        "key": key, "monitor": monitor, "chunk": chunk,
                        "left_active": left_active, "right_active": right_active,
                        "left_digest": digest(left), "right_digest": digest(right),
                    })
            for shift in range(stations):
                composed = rotate_key(rotate_key(key, shift, stations),
                                      monitor, stations)
                expected = rotate_key(key, shift + monitor, stations)
                if composed != expected and len(action_failures) < 12:
                    action_failures.append((key, monitor, shift, composed, expected))
    result = {
        "lifted": (
            "the source positions in the initial controller engagement orbit "
            "and in every later 11-chunk H orbit"
        ),
        "not_lifted": (
            "the event seed, clean predicate, 51,115-orbit horizon, or E1/E2 "
            "observation cadence"
        ),
        "honest_granularity": (
            "every chunk's ordered active station list and complete ordered "
            "Cycle-719 mapped-gate word; equal words act on the identical event "
            "seed, so engagement states and all later state boundaries coincide"
        ),
        "exact_gate_word_chunk_comparisons": chunk_comparisons,
        "C11_action_comparisons": len(census) * stations * stations,
        "first_gate_word_failures": tuple(failures),
        "first_action_failures": tuple(action_failures),
    }
    result["pass"] = (
        chunk_comparisons == 90_508
        and not failures
        and not action_failures
    )
    return result


def monitor_selections(
    scope: dict[str, object], stamps: dict[str, object]
) -> dict[str, dict[int, Selection]]:
    return {
        reading: {
            monitor: frozenset(
                key for key in scope["census"]
                if rotate_key(key, monitor, scope["stations"]) in stamps[reading]
            )
            for monitor in range(scope["stations"])
        }
        for reading in READINGS
    }


def intertwining(
    scope: dict[str, object],
    monitor_sets: dict[str, dict[int, Selection]],
    lift: dict[str, object],
) -> dict[str, object]:
    failures = []
    cases = 0
    stations = scope["stations"]
    for reading in READINGS:
        for monitor in range(stations):
            for shift in range(stations):
                moved_monitor = (monitor + shift) % stations
                for key in scope["census"]:
                    left = rotate_key(key, shift, stations) in monitor_sets[reading][monitor]
                    right = key in monitor_sets[reading][moved_monitor]
                    cases += 1
                    if left != right and len(failures) < 20:
                        failures.append({
                            "reading": reading, "key": key,
                            "monitor": monitor, "rotation": shift,
                            "left": left, "right": right,
                        })
    result = {
        "identity": "stamped_m(g.key) == stamped_(g.m)(key)",
        "monitor_action": "g.m = (m + g) mod 11",
        "cases": cases,
        "first_counterexamples": tuple(failures),
        "phase_lift_scope": lift,
        "verdict": (
            "MONITOR_COVARIANT" if lift["pass"] and not failures
            else "PRIMARY_REFUTED_BY_INTERTWINING_COUNTEREXAMPLE"
        ),
        "fixed_monitor_boundary": (
            "breaking occurs only after holding m fixed inside the exact "
            "Cycle-852 phase lift"
        ),
    }
    result["pass"] = lift["pass"] and cases == 181_016 and not failures
    return result


def monitor_table(
    scope: dict[str, object], monitor_sets: dict[str, dict[int, Selection]]
) -> dict[str, object]:
    table = tuple({
        "monitor": monitor,
        "E1": len(monitor_sets["E1"][monitor]),
        "E2": len(monitor_sets["E2"][monitor]),
    } for monitor in range(scope["stations"]))
    witnesses = {}
    failures = []
    for reading in READINGS:
        rows = []
        for left in range(scope["stations"]):
            for right in range(left + 1, scope["stations"]):
                difference = monitor_sets[reading][left] ^ monitor_sets[reading][right]
                if not difference:
                    failures.append((reading, left, right))
                    continue
                key = min(difference)
                rows.append({
                    "monitors": (left, right),
                    "key": key,
                    "membership": (
                        key in monitor_sets[reading][left],
                        key in monitor_sets[reading][right],
                    ),
                })
        witnesses[reading] = tuple(rows)
    unique_memberships = {
        reading: len({digest(tuple(sorted(selection)))
                      for selection in by_monitor.values()})
        for reading, by_monitor in monitor_sets.items()
    }
    result = {
        "table": table,
        "unique_memberships": unique_memberships,
        "pairwise_witness_count": {
            reading: len(rows) for reading, rows in witnesses.items()
        },
        "pairwise_membership_witnesses": witnesses,
        "unseparated_monitor_pairs": tuple(failures),
    }
    result["pass"] = (
        all(row["E1"] == 182 and row["E2"] == 114 for row in table)
        and unique_memberships == {"E1": 11, "E2": 11}
        and result["pairwise_witness_count"] == {"E1": 55, "E2": 55}
        and not failures
    )
    return result


def missing_monitor_certificate(
    census: tuple[Key, ...], by_monitor: dict[int, Selection]
) -> dict[str, object]:
    groups: dict[int, list[int]] = defaultdict(list)
    mapping = []
    absolute = []
    for lane, key in enumerate(census):
        missing = tuple(monitor for monitor in sorted(by_monitor)
                        if key not in by_monitor[monitor])
        if not missing:
            absolute.append(key)
            continue
        witness = missing[0]
        groups[witness].append(lane)
        mapping.append((key, witness))
    return {
        "absolute": frozenset(absolute),
        "nonabsolute_count": len(mapping),
        "witness_encoding": (
            "for each monitor m, comma/range-encoded zero-based census lanes "
            "name setups not stamped at m; each nonabsolute setup occurs once"
        ),
        "first_missing_monitor_by_group": {
            monitor: range_encode(indices)
            for monitor, indices in sorted(groups.items())
        },
        "setup_to_witness_sha256": digest(tuple(mapping)),
    }


def absolute_records(
    scope: dict[str, object], monitor_sets: dict[str, dict[int, Selection]]
) -> dict[str, object]:
    certificates = {
        reading: missing_monitor_certificate(scope["census"], monitor_sets[reading])
        for reading in READINGS
    }
    absolute_e1 = certificates["E1"]["absolute"]
    absolute_e2 = certificates["E2"]["absolute"]
    complete_orbits = tuple(
        orbit for orbit in scope["orbits"] if set(orbit) <= absolute_e1
    )
    orbit_rows = []
    separation_failures = []
    for orbit in complete_orbits:
        gaps = set()
        for key in orbit:
            if key[0] != 2 or len(key[2]) != 2:
                separation_failures.append(("not-k2", key))
                continue
            first, second = key[2]
            gap = (second - first) % scope["stations"]
            gaps.add(tuple(sorted((gap, scope["stations"] - gap))))
        orbit_rows.append({
            "representative": orbit[0],
            "size": len(orbit),
            "event": orbit[0][1],
            "k": orbit[0][0],
            "cyclic_gap_pairs": tuple(sorted(gaps)),
        })
        if gaps != {(5, 6)}:
            separation_failures.append(("separation", orbit[0], tuple(sorted(gaps))))
    monitors_per_absolute = {
        reading: tuple(sorted({
            sum((key in monitor_sets[reading][monitor]) << monitor
                for monitor in range(scope["stations"]))
            for key in certificates[reading]["absolute"]
        }))
        for reading in READINGS
    }
    public_certificates = {
        reading: {
            key: value for key, value in certificate.items() if key != "absolute"
        } | {
            "absolute_count": len(certificate["absolute"]),
            "absolute_keys_sha256": digest(tuple(sorted(certificate["absolute"]))),
        }
        for reading, certificate in certificates.items()
    }
    joint = absolute_e1 & absolute_e2
    result = {
        "by_reading": public_certificates,
        "E1_absolute_orbits": tuple(orbit_rows),
        "E1_absolute_events": tuple(sorted(row["event"] for row in orbit_rows)),
        "E1_absolute_monitor_masks": monitors_per_absolute["E1"],
        "E2_absolute_monitor_masks": monitors_per_absolute["E2"],
        "joint_absolute_count": len(joint),
        "joint_absolute_sha256": digest(tuple(sorted(joint))),
        "first_orbit_identification_failures": tuple(separation_failures[:12]),
    }
    result["pass"] = (
        len(absolute_e1) == 33
        and certificates["E1"]["nonabsolute_count"] == 715
        and monitors_per_absolute["E1"] == ((1 << scope["stations"]) - 1,)
        and len(absolute_e2) == 0
        and certificates["E2"]["nonabsolute_count"] == 748
        and not monitors_per_absolute["E2"]
        and not joint
        and len(complete_orbits) == 3
        and sum(map(len, complete_orbits)) == 33
        and tuple(sorted(row["event"] for row in orbit_rows)) == (0, 1, 2)
        and all(row["size"] == 11 and row["k"] == 2
                and row["cyclic_gap_pairs"] == ((5, 6),)
                for row in orbit_rows)
        and not separation_failures
    )
    return result


def public_stamp_report(stamps: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in stamps.items() if key not in READINGS}


def assemble_output(checks: dict[str, bool], report: dict[str, object]) -> str:
    mixed = report["THE_MIXED_CENSUS"]["by_reading"]
    intertwine = report["THE_INTERTWINING"]
    table = report["THE_MONITOR_TABLE"]
    absolute = report["THE_ABSOLUTE_RECORDS"]
    controls = report["CONTROLS"]
    details = {
        "THE_MIXED_CENSUS": (
            f"E1 setups/classes={mixed['E1']['stamped_setups']}/"
            f"{mixed['E1']['uniform_stamped_orbits']}/"
            f"{mixed['E1']['uniform_silent_orbits']}/"
            f"{mixed['E1']['mixed_orbits']}; E2 setups/classes="
            f"{mixed['E2']['stamped_setups']}/"
            f"{mixed['E2']['uniform_stamped_orbits']}/"
            f"{mixed['E2']['uniform_silent_orbits']}/"
            f"{mixed['E2']['mixed_orbits']}"
        ),
        "THE_INTERTWINING": (
            f"{intertwine['verdict']}; all {intertwine['cases']} cases; "
            f"lifted {intertwine['phase_lift_scope']['lifted']}; granularity: "
            f"{intertwine['phase_lift_scope']['honest_granularity']}"
        ),
        "THE_MONITOR_TABLE": (
            "all monitor sizes E1/E2=182/114; unique memberships=11/11; "
            f"pairwise witnesses={table['pairwise_witness_count']}"
        ),
        "THE_ABSOLUTE_RECORDS": (
            f"E1=33 ({len(absolute['E1_absolute_orbits'])} size-11 k=2 orbits; "
            f"events={absolute['E1_absolute_events']}; gaps 5/6); "
            f"E2=0; joint={absolute['joint_absolute_count']}; exhaustive "
            f"missing-monitor witnesses E1/E2="
            f"{absolute['by_reading']['E1']['nonabsolute_count']}/"
            f"{absolute['by_reading']['E2']['nonabsolute_count']}"
        ),
        "CONTROLS": (
            "SHA/Git-blob pinned literal worktree-relative inputs; source primary "
            "BLOCKLIST text/AST only; duplicated all-setup dynamics and analysis "
            f"replay exact; runtime={report['runtime_seconds']}s; "
            f"stdout={controls['stdout_bytes']} bytes"
        ),
    }
    lines = [
        f"{'PASS' if checks[name] else 'FAIL'} {name} :: {details[name]}"
        for name in (
            "THE_MIXED_CENSUS", "THE_INTERTWINING", "THE_MONITOR_TABLE",
            "THE_ABSOLUTE_RECORDS", "CONTROLS",
        )
    ]
    lines.append("SUMMARY_JSON " + compact(report))
    return "\n".join(lines) + "\n"


def main() -> int:
    started = monotonic()
    controls_pre = source_controls()
    scope = build_scope()
    stamps = independent_stamp_census(scope)
    mixed = mixed_census(scope, stamps)
    lift = phase_lift(scope)
    monitor_sets = monitor_selections(scope, stamps)
    intertwined = intertwining(scope, monitor_sets, lift)
    table = monitor_table(scope, monitor_sets)
    absolute = absolute_records(scope, monitor_sets)

    replay_mixed = mixed_census(scope, stamps)
    replay_lift = phase_lift(scope)
    replay_sets = monitor_selections(scope, stamps)
    replay_intertwined = intertwining(scope, replay_sets, replay_lift)
    replay_table = monitor_table(scope, replay_sets)
    replay_absolute = absolute_records(scope, replay_sets)
    analysis_replay_exact = (
        monitor_sets == replay_sets
        and digest(mixed) == digest(replay_mixed)
        and digest(lift) == digest(replay_lift)
        and digest(intertwined) == digest(replay_intertwined)
        and digest(table) == digest(replay_table)
        and digest(absolute) == digest(replay_absolute)
    )
    controls_post = source_controls()
    elapsed = monotonic() - started
    checks = {
        "THE_MIXED_CENSUS": scope["pass"] and stamps["pass"] and mixed["pass"],
        "THE_INTERTWINING": intertwined["pass"],
        "THE_MONITOR_TABLE": table["pass"],
        "THE_ABSOLUTE_RECORDS": absolute["pass"],
        "CONTROLS": False,
    }
    controls_pass_without_stdout = (
        controls_pre["pass"]
        and controls_post["pass"]
        and controls_pre == controls_post
        and stamps["determinism"]["mismatching_boundaries"] == 0
        and stamps["determinism"]["mismatching_lane_observations"] == 0
        and stamps["determinism"]["final_full_state_halves_exact"]
        and analysis_replay_exact
        and elapsed < AUDIT_TIMEOUT_SEC
        and not SOURCE_PRIMARY_FIREWALL.hits
    )
    report = {
        "checks": checks,
        "THE_MIXED_CENSUS": mixed,
        "THE_INTERTWINING": intertwined,
        "THE_MONITOR_TABLE": table,
        "THE_ABSOLUTE_RECORDS": absolute,
        "CONTROLS": {
            **controls_post,
            "independent_state_recomputation": public_stamp_report(stamps),
            "analysis_replay_exact": analysis_replay_exact,
            "runtime_under_1400s": elapsed < AUDIT_TIMEOUT_SEC,
            "stdout_under_150KB": False,
            "stdout_bytes": 0,
        },
        "runtime_seconds": round(elapsed, 6),
        "pass": False,
    }
    preliminary = assemble_output(checks, report)
    stdout_ok = len(preliminary.encode("utf-8")) < STDOUT_LIMIT_BYTES
    report["CONTROLS"]["stdout_under_150KB"] = stdout_ok
    checks["CONTROLS"] = controls_pass_without_stdout and stdout_ok
    report["pass"] = all(checks.values())
    report["report_sha256"] = digest({
        key: value for key, value in report.items() if key != "report_sha256"
    })
    output = assemble_output(checks, report)
    report["CONTROLS"]["stdout_bytes"] = len(output.encode("utf-8"))
    report["report_sha256"] = digest({
        key: value for key, value in report.items() if key != "report_sha256"
    })
    output = assemble_output(checks, report)
    final_size = len(output.encode("utf-8"))
    if final_size != report["CONTROLS"]["stdout_bytes"]:
        report["CONTROLS"]["stdout_bytes"] = final_size
        report["report_sha256"] = digest({
            key: value for key, value in report.items() if key != "report_sha256"
        })
        output = assemble_output(checks, report)
        final_size = len(output.encode("utf-8"))
    if final_size >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", final_size))
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
