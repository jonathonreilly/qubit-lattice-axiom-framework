#!/usr/bin/env python3
"""Cycle 852 independent adversarial checker: the selection no-go.

The Cycle-852 primary is provenance-only input.  This checker imports only
the landed Cycle-719 controller core, rebuilds the finite setup space from
bit masks, constructs the C_11 action and its orbits, and independently
evolves the complete census with a fresh lane-packed dynamics engine.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Callable, Iterable


AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle852_selection_tournament_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
CORE_PATH = AUDIT_INPUT_PATHS[0]
PRIMARY_PATH = AUDIT_INPUT_PATHS[1]
BLOCKLISTED_MODULES = (Path(PRIMARY_PATH).stem,)
EXPECTED_SHA256 = {
    CORE_PATH: "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    PRIMARY_PATH: "fcb1e5ad22e48dc865754bc0a0f5357cdef8e78b477c21f48b74e5971eaa8419",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    PRIMARY_PATH: "d584154f32ead0a03a9661c6f176d52b2a1a77dc",
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Make executable access to the source primary fail closed."""

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
RING_ORDER = 11
EVENT_PHASES = tuple(range(4))
FRAME_GENERATORS = (1, -1)
TRAJECTORY_HORIZON = 51_115

DECLARED_CRITERIA = (
    "maximal_source_count_k",
    "minimal_source_count_k",
    "E2_earliest_record_moment",
    "E2_latest_record_moment",
    "E1_earliest_first_clean_absolute_H",
    "E1_latest_first_clean_absolute_H",
    "E2_stamped",
    "E2_never_stamped_through_horizon",
    "E1_stamped",
    "E1_never_stamped_through_horizon",
    "maximal_orbit_size_most_symmetric_placement",
    "minimal_orbit_size_least_symmetric_placement",
    "longest_transient",
    "shortest_transient",
    "longest_cycle_period",
    "shortest_cycle_period",
    "trajectory_attains_maximum_weight_state",
    "trajectory_reaches_deepest_shared_merger_state",
    "trajectory_in_largest_funnel_basin",
    "immediate_admissibility_clean_at_t0",
)

EXPECTED_SELECTION_SIZES = {
    "maximal_source_count_k": 44,
    "minimal_source_count_k": 176,
    "E2_earliest_record_moment": 24,
    "E2_latest_record_moment": 9,
    "E1_earliest_first_clean_absolute_H": 24,
    "E1_latest_first_clean_absolute_H": 2,
    "E2_stamped": 114,
    "E2_never_stamped_through_horizon": 634,
    "E1_stamped": 182,
    "E1_never_stamped_through_horizon": 566,
    "maximal_orbit_size_most_symmetric_placement": 748,
    "minimal_orbit_size_least_symmetric_placement": 748,
    "longest_transient": 9,
    "shortest_transient": 24,
    "longest_cycle_period": 1,
    "shortest_cycle_period": 3,
    "trajectory_attains_maximum_weight_state": 2,
    "trajectory_reaches_deepest_shared_merger_state": 5,
    "trajectory_in_largest_funnel_basin": 33,
    "immediate_admissibility_clean_at_t0": 24,
}


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
    matches = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            targets = node.targets
            value = node.value
        elif isinstance(node, ast.AnnAssign):
            targets = (node.target,)
            value = node.value
        else:
            continue
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            matches.append(value)
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def primary_declared_criterion_names(tree: ast.Module) -> tuple[str, ...]:
    """Read names, not values or executable behavior, from the blocked AST."""

    functions = {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    tournament = functions.get("tournament")
    if tournament is None:
        return ()
    for node in ast.walk(tournament):
        if isinstance(node, ast.Assign):
            targets = node.targets
            value = node.value
        elif isinstance(node, ast.AnnAssign):
            targets = (node.target,)
            value = node.value
        else:
            continue
        if not any(
            isinstance(target, ast.Name) and target.id == "selections"
            for target in targets
        ):
            continue
        if not isinstance(value, ast.Dict):
            return ()
        if not all(
            isinstance(key, ast.Constant) and isinstance(key.value, str)
            for key in value.keys
        ):
            return ()
        return tuple(key.value for key in value.keys)
    return ()


def source_controls() -> tuple[dict[str, object], dict[str, str]]:
    payloads = {
        relative: (ROOT / relative).read_bytes()
        for relative in AUDIT_INPUT_PATHS
    }
    before = {
        relative: sha256(payload).hexdigest()
        for relative, payload in payloads.items()
    }
    blobs = {
        relative: git_blob(payload)
        for relative, payload in payloads.items()
    }
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=Path(__file__).name,
    )
    primary_tree = ast.parse(
        payloads[PRIMARY_PATH], filename=PRIMARY_PATH
    )
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    ast_names = primary_declared_criterion_names(primary_tree)
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_AUDIT_INPUT_PATHS": (
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS
        ),
        "existing_worktree_relative": all(
            not Path(relative).is_absolute()
            and ".." not in Path(relative).parts
            and (ROOT / relative).is_file()
            for relative in AUDIT_INPUT_PATHS
        ),
        "sha256": before,
        "git_blobs": blobs,
        "expected_sha256": EXPECTED_SHA256,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "blocked_source_primary": PRIMARY_PATH,
        "primary_access": "read_bytes + ast.parse only",
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(PRIMARY_FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
        "primary_AST_declared_criteria": ast_names,
    }
    result["pass"] = (
        result["literal_AUDIT_INPUT_PATHS"]
        and result["existing_worktree_relative"]
        and before == EXPECTED_SHA256
        and blobs == EXPECTED_GIT_BLOBS
        and ast_names == DECLARED_CRITERIA
        and direct_frontier_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result, before


def positions_from_mask(mask: int) -> tuple[int, ...]:
    return tuple(
        station
        for station in range(RING_ORDER)
        if (mask >> station) & 1
    )


def separated_mask(mask: int) -> bool:
    return not any(
        ((mask >> station) & 1)
        and ((mask >> ((station + 1) % RING_ORDER)) & 1)
        for station in range(RING_ORDER)
    )


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(sorted(
        (station + shift) % RING_ORDER for station in positions
    ))


def frame_map(key: Key, shift: int) -> Key:
    k, event, positions = key
    return k, event, rotate_positions(positions, shift)


def enumerate_placements() -> dict[int, tuple[tuple[int, ...], ...]]:
    rows: dict[int, list[tuple[int, ...]]] = {
        k: [] for k in range(MIN_SOURCES, MAX_SOURCES + 1)
    }
    for mask in range(1 << RING_ORDER):
        k = mask.bit_count()
        if k in rows and separated_mask(mask):
            rows[k].append(positions_from_mask(mask))
    return {k: tuple(sorted(values)) for k, values in rows.items()}


def build_census() -> tuple[
    tuple[object, ...],
    tuple[tuple[int, State], ...],
    dict[int, tuple[tuple[int, ...], ...]],
    tuple[Key, ...],
]:
    program = K.interleaved_program(FIXTURE_BANKS)
    if len(program) != RING_ORDER:
        raise AssertionError(("ring order", len(program)))
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    event_seeds = []
    for event in EVENT_PHASES:
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        if not (
            after == K.A.apply_semantic(before, allocator)
            and rail_a == (1,) + (0,) * (RING_ORDER - 1)
            and not any(rail_b)
            and len(trace) == RING_ORDER
        ):
            raise AssertionError(("event seed", event))
        event_seeds.append((event, before))
        state = after
    placements = enumerate_placements()
    census = tuple(sorted(
        (k, event, positions)
        for k, position_rows in placements.items()
        for positions in position_rows
        for event, _state in event_seeds
    ))
    return program, tuple(event_seeds), placements, census


def generated_orbit(key: Key) -> tuple[Key, ...]:
    seen = set()
    frontier = [key]
    while frontier:
        current = frontier.pop()
        if current in seen:
            continue
        seen.add(current)
        for generator in FRAME_GENERATORS:
            frontier.append(frame_map(current, generator))
    return tuple(sorted(seen))


def partition_orbits(census: tuple[Key, ...]) -> tuple[tuple[Key, ...], ...]:
    universe = set(census)
    remaining = set(census)
    rows = []
    while remaining:
        representative = min(remaining)
        orbit = generated_orbit(representative)
        if not set(orbit) <= universe:
            raise AssertionError(("frame closure", representative))
        rows.append(orbit)
        remaining.difference_update(orbit)
    return tuple(sorted(rows, key=lambda row: row[0]))


def cycle828_scope_counts(
    placements: dict[int, tuple[tuple[int, ...], ...]]
) -> dict[str, object]:
    representatives = {
        k: tuple(sorted({
            min(rotate_positions(positions, shift)
                for shift in range(RING_ORDER))
            for positions in placements[k]
        }))
        for k in range(MIN_SOURCES, MAX_SOURCES + 1)
    }
    per_k = {
        2: len(placements[2]) * len(EVENT_PHASES),
        **{
            k: len(representatives[k]) * len(EVENT_PHASES)
            for k in range(3, MAX_SOURCES + 1)
        },
    }
    result = {
        "event_phase_range": EVENT_PHASES,
        "ring_origin_range_cycle852": tuple(range(RING_ORDER)),
        "cycle828_rule": (
            "all labeled k=2 placements; one rotation-canonical "
            "representative for every k=3,4,5 placement orbit"
        ),
        "rotation_representatives_per_k": {
            k: len(rows) for k, rows in representatives.items()
        },
        "cycle828_per_k": per_k,
        "cycle828_population": sum(per_k.values()),
        "cycle852_per_k": {
            k: len(rows) * len(EVENT_PHASES)
            for k, rows in placements.items()
        },
        "cycle852_population": sum(
            len(rows) * len(EVENT_PHASES)
            for rows in placements.values()
        ),
    }
    result["pass"] = (
        result["rotation_representatives_per_k"]
        == {2: 4, 3: 7, 4: 5, 5: 1}
        and per_k == {2: 176, 3: 28, 4: 20, 5: 4}
        and result["cycle828_population"] == 228
        and result["cycle852_per_k"]
        == {2: 176, 3: 308, 4: 220, 5: 44}
        and result["cycle852_population"] == 748
    )
    return result


def census_certificate(
    census: tuple[Key, ...], orbits: tuple[tuple[Key, ...], ...]
) -> dict[str, object]:
    universe = set(census)
    stabilizer_failures = tuple(
        (key, shift)
        for key in census
        for shift in range(1, RING_ORDER)
        if frame_map(key, shift) == key
    )
    closure_failures = tuple(
        (key, generator)
        for key in census
        for generator in FRAME_GENERATORS
        if frame_map(key, generator) not in universe
    )
    histogram = dict(sorted(Counter(map(len, orbits)).items()))
    per_k = dict(sorted(Counter(key[0] for key in census).items()))
    singletons = tuple(orbit for orbit in orbits if len(orbit) == 1)
    result = {
        "acting_group": (
            "C_11, acting by simultaneous addition mod 11 to every "
            "occupied station; k and event phase are fixed"
        ),
        "population": len(census),
        "per_k": per_k,
        "orbit_count": len(orbits),
        "orbit_histogram": histogram,
        "singleton_orbit_count": len(singletons),
        "closure_failures": closure_failures,
        "nonidentity_stabilizers": stabilizer_failures,
        "constructive_free_action_reason": (
            "Every nonzero element of prime-order C_11 generates C_11. "
            "A fixed occupied subset would therefore be empty or all 11 "
            "stations, but this census has cardinality 2..5; exhaustive "
            "stabilizer enumeration confirms no exception."
        ),
        "census_sha256": digest(census),
        "orbit_partition_sha256": digest(orbits),
    }
    result["pass"] = (
        len(census) == 748
        and per_k == {2: 176, 3: 308, 4: 220, 5: 44}
        and len(orbits) == 68
        and histogram == {11: 68}
        and not singletons
        and not closure_failures
        and not stabilizer_failures
        and sum(map(len, orbits)) == len(census)
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


def derive_dirty_coordinates() -> tuple[int, ...]:
    """Discover clean-postimage coordinates through pack-state probes."""

    banks0, links0 = K.B.chain_genesis(FIXTURE_BANKS)
    zero_banks = tuple(tuple(0 for _bit in bank) for bank in banks0)
    zero_links = tuple(tuple(0 for _bit in link) for link in links0)
    baseline = K.M.pack_state(zero_banks, zero_links)
    indices = {K.R3.X.SOURCE_POINTER}
    for bank_index in range(len(zero_banks)):
        for _name, wire in watched_registers():
            marked_banks = [list(bank) for bank in zero_banks]
            marked_banks[bank_index][wire] = 1
            marked = K.M.pack_state(
                tuple(tuple(bank) for bank in marked_banks), zero_links
            )
            differences = tuple(
                index
                for index, (left, right) in enumerate(zip(baseline, marked))
                if left != right
            )
            if len(differences) != 1:
                raise AssertionError(("bank coordinate probe", differences))
            indices.add(differences[0])
    for link_index, link in enumerate(zero_links):
        for wire in range(len(link)):
            marked_links = [list(row) for row in zero_links]
            marked_links[link_index][wire] = 1
            marked = K.M.pack_state(
                zero_banks, tuple(tuple(row) for row in marked_links)
            )
            differences = tuple(
                index
                for index, (left, right) in enumerate(zip(baseline, marked))
                if left != right
            )
            if len(differences) != 1:
                raise AssertionError(("link coordinate probe", differences))
            indices.add(differences[0])
    return tuple(sorted(indices))


def build_initial_states(
    program: tuple[object, ...],
    event_seeds: tuple[tuple[int, State], ...],
    census: tuple[Key, ...],
) -> tuple[State, ...]:
    seed_by_event = dict(event_seeds)
    states = []
    for k, event, positions in census:
        after, rail_a, rail_b, trace = K.run_orbit(
            seed_by_event[event], program, token_positions=positions
        )
        expected_rail = tuple(
            int(station in positions) for station in range(RING_ORDER)
        )
        if not (
            len(positions) == k
            and rail_a == expected_rail
            and not any(rail_b)
            and len(trace) == RING_ORDER
        ):
            raise AssertionError(("initial state", k, event, positions))
        states.append(after)
    if not states or any(len(state) != len(states[0]) for state in states):
        raise AssertionError("ragged initial state catalog")
    return tuple(states)


def pack_states(states: tuple[State, ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


PackedGate = tuple[int, int, int, int, int]


def packed_gate(gate: object, mask: int) -> PackedGate:
    if gate.kind == "X":
        return 0, gate.wires[0], 0, 0, mask
    if gate.kind == "CNOT":
        return 1, gate.wires[0], gate.wires[1], 0, mask
    if gate.kind == "TOF":
        return 2, gate.wires[0], gate.wires[1], gate.wires[2], mask
    raise ValueError(("unsupported core gate", gate))


def compile_lane_schedules(
    program: tuple[object, ...], simulation_keys: tuple[Key, ...]
) -> tuple[tuple[PackedGate, ...], ...]:
    schedules = []
    for step in range(RING_ORDER):
        operations = []
        for station, row in enumerate(program):
            mask = 0
            for lane, (_k, _event, positions) in enumerate(simulation_keys):
                if (station - step) % RING_ORDER in positions:
                    mask |= 1 << lane
            if mask:
                operations.extend(
                    packed_gate(gate, mask)
                    for gate in K.mapped_macro(row)
                )
        schedules.append(tuple(operations))
    return tuple(schedules)


def advance_interpreted(
    columns: list[int], schedule: tuple[PackedGate, ...]
) -> None:
    for kind, first, second, third, mask in schedule:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first] & mask
        else:
            columns[third] ^= columns[first] & columns[second] & mask


def compile_fast_chunks(
    schedules: tuple[tuple[PackedGate, ...], ...]
) -> tuple[Callable[[list[int]], None], ...]:
    """Specialize exact landed gates; schedules remain the evidence surface."""

    functions = []
    for schedule in schedules:
        lines = ["def apply_chunk(c):"]
        for kind, first, second, third, mask in schedule:
            if kind == 0:
                lines.append(f" c[{first}] ^= {mask}")
            elif kind == 1:
                lines.append(f" c[{second}] ^= c[{first}] & {mask}")
            else:
                lines.append(
                    f" c[{third}] ^= c[{first}] & c[{second}] & {mask}"
                )
        namespace: dict[str, object] = {}
        exec("\n".join(lines), {"__builtins__": {}}, namespace)
        functions.append(namespace["apply_chunk"])
    return tuple(functions)  # type: ignore[return-value]


def clean_mask(
    columns: list[int], dirty_indices: tuple[int, ...], lane_mask: int
) -> int:
    dirty = 0
    for wire in dirty_indices:
        dirty |= columns[wire]
    return lane_mask & ~dirty


def equality_mask(
    columns: list[int], reference: list[int], candidate_mask: int
) -> int:
    """Exact equality with a safe early exit after every candidate differs."""

    differences = 0
    for left, right in zip(columns, reference):
        differences |= left ^ right
        if differences & candidate_mask == candidate_mask:
            return 0
    return candidate_mask & ~differences


def maximum_weight_mask(
    columns: list[int], lane_mask: int
) -> tuple[int, int]:
    counters: list[int] = []
    for column in columns:
        carry = column & lane_mask
        index = 0
        while carry:
            if index == len(counters):
                counters.append(carry)
                break
            carry, counters[index] = (
                counters[index] & carry,
                counters[index] ^ carry,
            )
            index += 1
    candidates = lane_mask
    value = 0
    for bit in reversed(range(len(counters))):
        ones = counters[bit] & candidates
        if ones:
            value |= 1 << bit
            candidates = ones
        else:
            candidates &= ~counters[bit]
    return value, candidates


def lane_numbers(mask: int) -> tuple[int, ...]:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def duplicate_groups(
    columns: list[int], lane_mask: int, wire_order: tuple[int, ...]
) -> tuple[int, ...]:
    groups = [lane_mask]
    for wire in wire_order:
        column = columns[wire]
        next_groups = []
        for group in groups:
            zero = group & ~column
            one = group & column
            if zero.bit_count() > 1:
                next_groups.append(zero)
            if one.bit_count() > 1:
                next_groups.append(one)
        groups = next_groups
        if not groups:
            break
    return tuple(sorted(groups, key=lane_numbers))


def unpack_lane(columns: list[int], lane: int) -> State:
    return tuple((column >> lane) & 1 for column in columns)


def scalar_step(
    state: State,
    program: tuple[object, ...],
    positions: tuple[int, ...],
    step: int,
) -> State:
    output = state
    for station, row in enumerate(program):
        if (station - step) % RING_ORDER in positions:
            output = K.A.apply_semantic(output, K.mapped_macro(row))
    return output


def scalar_shadow_control(
    program: tuple[object, ...],
    event_seeds: tuple[tuple[int, State], ...],
    census: tuple[Key, ...],
    states: tuple[State, ...],
    schedules: tuple[tuple[PackedGate, ...], ...],
) -> dict[str, object]:
    """Cross-check lane packing against direct core semantics for two orbits."""

    selected_lanes = tuple(sorted({
        0, len(census) // 3, 2 * len(census) // 3, len(census) - 1
    }))
    columns = pack_states(states)
    scalar = {lane: states[lane] for lane in selected_lanes}
    mismatches = []
    boundary = 0
    for _orbit in range(2):
        for step, schedule in enumerate(schedules):
            advance_interpreted(columns, schedule)
            boundary += 1
            for lane in selected_lanes:
                scalar[lane] = scalar_step(
                    scalar[lane], program, census[lane][2], step
                )
                if unpack_lane(columns, lane) != scalar[lane]:
                    mismatches.append((boundary, census[lane]))
    inverse_failures = []
    seed_by_event = dict(event_seeds)
    for lane in selected_lanes:
        key = census[lane]
        restored, rail_a, rail_b, _trace = K.run_orbit(
            states[lane], program, token_positions=key[2], reverse=True
        )
        expected_rail = tuple(
            int(station in key[2]) for station in range(RING_ORDER)
        )
        # The initial catalog is one forward multi-token orbit from its seed.
        if not (
            restored == seed_by_event[key[1]]
            and rail_a == expected_rail
            and not any(rail_b)
        ):
            inverse_failures.append(key)
    return {
        "selected_lanes": selected_lanes,
        "boundaries": boundary,
        "full_state_mismatches": tuple(mismatches),
        "inverse_sanity_failures": tuple(inverse_failures),
        "pass": not mismatches and not inverse_failures,
    }


def trajectory_census(
    program: tuple[object, ...],
    event_seeds: tuple[tuple[int, State], ...],
    census: tuple[Key, ...],
) -> dict[str, object]:
    """Exact full-census evolution, independently compiled from core gates."""

    started = monotonic()
    states = build_initial_states(program, event_seeds, census)
    simulation_keys = census + (census[0],)
    duplicate_lane = len(census)
    schedules = compile_lane_schedules(program, simulation_keys)
    fast_chunks = compile_fast_chunks(schedules)
    scalar_shadow = scalar_shadow_control(
        program, event_seeds, census, states, schedules
    )
    columns = pack_states(states + (states[0],))
    initial_columns = columns.copy()
    dirty_indices = derive_dirty_coordinates()
    all_mask = (1 << len(census)) - 1
    simulation_mask = (1 << len(simulation_keys)) - 1

    initial_clean_all = clean_mask(columns, dirty_indices, simulation_mask)
    initial_clean = initial_clean_all & all_mask
    determinism_mismatches = int(
        bool(initial_clean_all & 1)
        != bool(initial_clean_all & (1 << duplicate_lane))
    )
    e1_first = {
        census[lane]: 0 for lane in lane_numbers(initial_clean)
    }
    e2_first = dict(e1_first)
    e1_found_mask = initial_clean
    e2_found_mask = initial_clean
    cycle_periods: dict[Key, int] = {}
    unresolved_cycle_mask = all_mask & ~initial_clean

    global_max_weight, global_max_mask = maximum_weight_mask(
        columns, all_mask
    )
    wire_order = tuple(sorted(
        range(len(columns)),
        key=lambda wire: (
            abs(2 * (columns[wire] & all_mask).bit_count() - len(census)),
            wire,
        ),
    ))
    initial_duplicate_groups = duplicate_groups(
        columns, all_mask, wire_order
    )
    initial_group_by_lane: dict[int, frozenset[int]] = {}
    for group in initial_duplicate_groups:
        members = frozenset(lane_numbers(group))
        for lane in members:
            initial_group_by_lane[lane] = members

    merger_first_moment: dict[tuple[int, ...], int] = {}
    largest_basin_size = 0
    largest_basin_groups: set[tuple[int, ...]] = set()

    for orbit in range(1, TRAJECTORY_HORIZON + 1):
        for step, apply_chunk in enumerate(fast_chunks, 1):
            apply_chunk(columns)
            clean_all = clean_mask(columns, dirty_indices, simulation_mask)
            clean = clean_all & all_mask
            determinism_mismatches += (
                bool(clean_all & 1)
                != bool(clean_all & (1 << duplicate_lane))
            )
            new_e1 = clean & ~e1_found_mask
            absolute_h = (orbit - 1) * RING_ORDER + step
            for lane in lane_numbers(new_e1):
                e1_first[census[lane]] = absolute_h
            e1_found_mask |= new_e1

        orbit_clean_all = clean_mask(
            columns, dirty_indices, simulation_mask
        )
        orbit_clean = orbit_clean_all & all_mask
        new_e2 = orbit_clean & ~e2_found_mask
        for lane in lane_numbers(new_e2):
            e2_first[census[lane]] = orbit
        e2_found_mask |= new_e2

        recurrence = equality_mask(
            columns,
            initial_columns,
            unresolved_cycle_mask & ~orbit_clean,
        )
        primary_recurrence = equality_mask(columns, initial_columns, 1)
        duplicate_recurrence = equality_mask(
            columns, initial_columns, 1 << duplicate_lane
        )
        determinism_mismatches += (
            bool(primary_recurrence) != bool(duplicate_recurrence)
        )
        for lane in lane_numbers(recurrence):
            cycle_periods[census[lane]] = orbit
        unresolved_cycle_mask &= ~(orbit_clean | recurrence)

        weight, weight_mask = maximum_weight_mask(columns, all_mask)
        if weight > global_max_weight:
            global_max_weight = weight
            global_max_mask = weight_mask
        elif weight == global_max_weight:
            global_max_mask |= weight_mask

        for group in duplicate_groups(columns, all_mask, wire_order):
            members = tuple(lane_numbers(group))
            member_set = frozenset(members)
            if all(
                initial_group_by_lane.get(lane) == member_set
                for lane in members
            ):
                continue
            merger_first_moment.setdefault(members, orbit)
            size = len(members)
            if size > largest_basin_size:
                largest_basin_size = size
                largest_basin_groups = {members}
            elif size == largest_basin_size:
                largest_basin_groups.add(members)

        if orbit % 8192 == 0:
            print(
                "PROGRESS independent trajectory"
                f" orbit={orbit}/{TRAJECTORY_HORIZON}"
                f" elapsed={monotonic() - started:.1f}s",
                file=sys.stderr,
                flush=True,
            )

    deepest_moment = max(merger_first_moment.values(), default=None)
    deepest_mask = 0
    for members, first_moment in merger_first_moment.items():
        if first_moment == deepest_moment:
            deepest_mask |= sum(1 << lane for lane in members)
    largest_mask = 0
    for members in largest_basin_groups:
        largest_mask |= sum(1 << lane for lane in members)
    duplicate_final_exact = all(
        bool(column & 1) == bool(column & (1 << duplicate_lane))
        for column in columns
    )
    result = {
        "E1_first": e1_first,
        "E2_first": e2_first,
        "cycle_periods": cycle_periods,
        "unresolved_before_clean": frozenset(
            census[lane] for lane in lane_numbers(unresolved_cycle_mask)
        ),
        "maximum_weight": global_max_weight,
        "maximum_weight_attainers": frozenset(
            census[lane] for lane in lane_numbers(global_max_mask)
        ),
        "deepest_shared_merger_moment": deepest_moment,
        "deepest_shared_merger_members": frozenset(
            census[lane] for lane in lane_numbers(deepest_mask)
        ),
        "largest_funnel_basin_size": largest_basin_size,
        "largest_funnel_basin_members": frozenset(
            census[lane] for lane in lane_numbers(largest_mask)
        ),
        "largest_funnel_basin_tie_instances": len(largest_basin_groups),
        "shared_merger_cohort_count": len(merger_first_moment),
        "initial_duplicate_group_histogram": dict(sorted(Counter(
            group.bit_count() for group in initial_duplicate_groups
        ).items())),
        "dirty_coordinate_count": len(dirty_indices),
        "schedule_gate_counts": tuple(map(len, schedules)),
        "scalar_shadow": scalar_shadow,
        "determinism_duplicate": {
            "key": census[0],
            "boundary_mismatches": determinism_mismatches,
            "final_full_state_exact": duplicate_final_exact,
        },
        "runtime_seconds": round(monotonic() - started, 6),
    }
    result["trajectory_sha256"] = digest({
        "E1": tuple(sorted(e1_first.items())),
        "E2": tuple(sorted(e2_first.items())),
        "periods": tuple(sorted(cycle_periods.items())),
        "max_weight": global_max_weight,
        "max_attainers": tuple(sorted(result["maximum_weight_attainers"])),
        "deepest": (
            deepest_moment,
            tuple(sorted(result["deepest_shared_merger_members"])),
        ),
        "largest": (
            largest_basin_size,
            tuple(sorted(result["largest_funnel_basin_members"])),
        ),
    })
    result["pass"] = (
        scalar_shadow["pass"]
        and len(e1_first) <= len(census)
        and len(e2_first) <= len(census)
        and set(e2_first) <= set(e1_first)
        and not (set(e2_first) & set(cycle_periods))
        and (
            len(e2_first)
            + len(cycle_periods)
            + len(result["unresolved_before_clean"])
            == len(census)
        )
        and global_max_mask != 0
        and determinism_mismatches == 0
        and duplicate_final_exact
    )
    return result


def extremal_selection(
    values: dict[Key, int], choose: Callable[[Iterable[int]], int]
) -> Selection:
    if not values:
        return frozenset()
    target = choose(values.values())
    return frozenset(
        key for key, value in values.items() if value == target
    )


def tournament_selections(
    census: tuple[Key, ...],
    orbits: tuple[tuple[Key, ...], ...],
    trajectory: dict[str, object],
) -> dict[str, Selection]:
    e1_first: dict[Key, int] = trajectory["E1_first"]
    e2_first: dict[Key, int] = trajectory["E2_first"]
    periods: dict[Key, int] = trajectory["cycle_periods"]
    orbit_sizes = {
        key: len(orbit) for orbit in orbits for key in orbit
    }
    result: dict[str, Selection] = {
        "maximal_source_count_k": frozenset(
            key for key in census
            if key[0] == max(row[0] for row in census)
        ),
        "minimal_source_count_k": frozenset(
            key for key in census
            if key[0] == min(row[0] for row in census)
        ),
        "E2_earliest_record_moment": extremal_selection(e2_first, min),
        "E2_latest_record_moment": extremal_selection(e2_first, max),
        "E1_earliest_first_clean_absolute_H":
            extremal_selection(e1_first, min),
        "E1_latest_first_clean_absolute_H":
            extremal_selection(e1_first, max),
        "E2_stamped": frozenset(e2_first),
        "E2_never_stamped_through_horizon":
            frozenset(census) - frozenset(e2_first),
        "E1_stamped": frozenset(e1_first),
        "E1_never_stamped_through_horizon":
            frozenset(census) - frozenset(e1_first),
        "maximal_orbit_size_most_symmetric_placement": frozenset(
            key for key, size in orbit_sizes.items()
            if size == max(orbit_sizes.values())
        ),
        "minimal_orbit_size_least_symmetric_placement": frozenset(
            key for key, size in orbit_sizes.items()
            if size == min(orbit_sizes.values())
        ),
        "longest_transient": extremal_selection(e2_first, max),
        "shortest_transient": extremal_selection(e2_first, min),
        "longest_cycle_period": extremal_selection(periods, max),
        "shortest_cycle_period": extremal_selection(periods, min),
        "trajectory_attains_maximum_weight_state":
            trajectory["maximum_weight_attainers"],
        "trajectory_reaches_deepest_shared_merger_state":
            trajectory["deepest_shared_merger_members"],
        "trajectory_in_largest_funnel_basin":
            trajectory["largest_funnel_basin_members"],
        "immediate_admissibility_clean_at_t0": frozenset(
            key for key, moment in e1_first.items() if moment == 0
        ),
    }
    if tuple(result) != DECLARED_CRITERIA:
        raise AssertionError(("criterion order", tuple(result)))
    return result


def covariance_witness(
    selection: Selection, census: tuple[Key, ...]
) -> dict[str, object]:
    universe = set(census)
    for generator in FRAME_GENERATORS:
        mapped = frozenset(frame_map(key, generator) for key in selection)
        if mapped != selection:
            lost = tuple(sorted(selection - mapped))
            gained = tuple(sorted(mapped - selection))
            return {
                "covariant": False,
                "generator": generator,
                "selected_key": lost[0] if lost else None,
                "mapped_key": gained[0] if gained else None,
                "mapped_inside_census": mapped <= universe,
            }
    return {
        "covariant": True,
        "generator": None,
        "selected_key": None,
        "mapped_key": None,
        "mapped_inside_census": True,
    }


def period_status(key: Key, trajectory: dict[str, object]) -> object:
    periods: dict[Key, int] = trajectory["cycle_periods"]
    e2_first: dict[Key, int] = trajectory["E2_first"]
    if key in periods:
        return ("period_before_clean", periods[key])
    if key in e2_first:
        return ("clean_before_recurrence", e2_first[key])
    return ("unresolved_through_horizon", TRAJECTORY_HORIZON)


def size1_autopsy(
    census: tuple[Key, ...],
    orbits: tuple[tuple[Key, ...], ...],
    trajectory: dict[str, object],
    selections: dict[str, Selection],
) -> dict[str, object]:
    longest = selections["longest_cycle_period"]
    witness = covariance_witness(longest, census)
    if len(longest) != 1 or witness["covariant"]:
        selected_key = None
        mapped_key = None
    else:
        selected_key = witness["selected_key"]
        mapped_key = witness["mapped_key"]
    period_profiles = tuple(
        tuple(period_status(key, trajectory) for key in orbit)
        for orbit in orbits
    )
    nonconstant_orbits = sum(
        len(set(profile)) > 1 for profile in period_profiles
    )
    periods: dict[Key, int] = trajectory["cycle_periods"]
    result = {
        "period_count": len(periods),
        "period_range": (
            min(periods.values(), default=None),
            max(periods.values(), default=None),
        ),
        "longest_period_selection_size": len(longest),
        "longest_period_key": selected_key,
        "longest_period_value": (
            periods.get(selected_key) if selected_key is not None else None
        ),
        "frame_witness": witness,
        "mapped_key_period_status": (
            period_status(mapped_key, trajectory)
            if mapped_key is not None else None
        ),
        "period_status_nonconstant_orbit_count": nonconstant_orbits,
        "period_is_constant_on_every_frame_orbit": nonconstant_orbits == 0,
        "resolution": (
            "No contradiction: argmax period is a singleton only because "
            "the period observable is not C_11-invariant.  The fixed "
            "source/program origin is not co-rotated, so the singleton "
            "selection is not an orbit union."
        ),
    }
    result["pass"] = (
        len(longest) == 1
        and bool(periods)
        and not witness["covariant"]
        and witness["mapped_inside_census"]
        and selected_key in periods
        and mapped_key not in longest
        and nonconstant_orbits > 0
    )
    return result


def tournament_certificate(
    census: tuple[Key, ...],
    orbits: tuple[tuple[Key, ...], ...],
    selections: dict[str, Selection],
) -> tuple[dict[str, object], dict[str, dict[str, object]]]:
    orbit_sets = {frozenset(orbit) for orbit in orbits}
    orbit_by_key = {
        key: frozenset(orbit) for orbit in orbits for key in orbit
    }
    rows: dict[str, dict[str, object]] = {}
    for name, selection in selections.items():
        covariance = covariance_witness(selection, census)
        union_of_orbits = all(
            orbit_by_key[key] <= selection for key in selection
        )
        rows[name] = {
            "size": len(selection),
            "selection_sha256": digest(tuple(sorted(selection))),
            "covariance": covariance,
            "union_of_orbits": union_of_orbits,
            "unique_orbit": selection in orbit_sets,
            "unique_setup": len(selection) == 1,
            "eligibility": (
                "QUALIFIED" if covariance["covariant"] else "DISQUALIFIED"
            ),
        }
    observed_sizes = {name: row["size"] for name, row in rows.items()}
    unique_orbit_names = tuple(
        name for name, row in rows.items() if row["unique_orbit"]
    )
    candidates = tuple(
        name for name, row in rows.items()
        if row["covariance"]["covariant"] and row["unique_setup"]
    )
    qualified = tuple(
        name for name, row in rows.items()
        if row["covariance"]["covariant"]
    )
    result = {
        "declared_criterion_count": len(DECLARED_CRITERIA),
        "observed_sizes": observed_sizes,
        "expected_sizes": EXPECTED_SELECTION_SIZES,
        "qualified_criteria": qualified,
        "unique_orbit_criteria": unique_orbit_names,
        "covariant_unique_setup_candidates": candidates,
        "selection_layer_sha256": digest(tuple(
            (name, tuple(sorted(selection)))
            for name, selection in selections.items()
        )),
        "conclusion": (
            "SELECTION_OPEN_AFTER_DECLARED_CRITERIA; "
            "NO_COVARIANT_UNIQUE_SETUP_SELECTION_AT_SCOPE"
        ),
    }
    result["pass"] = (
        tuple(selections) == DECLARED_CRITERIA
        and observed_sizes == EXPECTED_SELECTION_SIZES
        and all(selection <= frozenset(census)
                for selection in selections.values())
        and all(
            row["covariance"]["covariant"] == row["union_of_orbits"]
            for row in rows.values()
        )
        and qualified == (
            "maximal_source_count_k",
            "minimal_source_count_k",
            "maximal_orbit_size_most_symmetric_placement",
            "minimal_orbit_size_least_symmetric_placement",
        )
        and not unique_orbit_names
        and not candidates
    )
    return result, rows


def multiples_audit(
    rows: dict[str, dict[str, object]]
) -> dict[str, object]:
    nonmultiples = {
        name: {
            "size": row["size"],
            "verified_non_covariance_witness": row["covariance"],
            "broken_symmetry": (
                "origin-anchored dynamics: the frame action rotates token "
                "placements only, while the nonuniform program macros, "
                "source station, event seed, and monitoring phase remain fixed"
            ),
        }
        for name, row in rows.items()
        if row["size"] % RING_ORDER
    }
    result = {
        "group_orbit_divisor": RING_ORDER,
        "nonmultiple_criteria": nonmultiples,
        "nonmultiple_count": len(nonmultiples),
        "corrected_reported_sizes": (),
    }
    result["pass"] = (
        bool(nonmultiples)
        and all(
            not row["verified_non_covariance_witness"]["covariant"]
            and row["verified_non_covariance_witness"]["mapped_inside_census"]
            for row in nonmultiples.values()
        )
        and all(
            rows[name]["size"] == EXPECTED_SELECTION_SIZES[name]
            for name in nonmultiples
        )
        and not result["corrected_reported_sizes"]
    )
    return result


def no_go_discipline_summary(
    census: dict[str, object],
    autopsy: dict[str, object],
    multiples: dict[str, object],
    tournament: dict[str, object],
    scope: dict[str, object],
) -> dict[str, object]:
    """N1-N8 gate, kept concise because the checker is the evidence packet."""

    routes = (
        ("singleton search", census["singleton_orbit_count"] == 0),
        ("nontrivial-stabilizer search", not census["nonidentity_stabilizers"]),
        ("covariant singleton-period steelman", autopsy["pass"]),
        ("all nonmultiple-size covariance attacks", multiples["pass"]),
        ("declared tournament unique-orbit replay", tournament["pass"]),
        ("Cycle-828 reduced-scope apparent-representative attack", scope["pass"]),
    )
    result = {
        "N1_alternative_routes": routes,
        "N2_wall_independence": (
            "one structural wall only: no singleton orbit; vacuous pair table"
        ),
        "N3_hidden_wall_scan": (
            "bounded C_11 action, fixed oriented ring/source origin, k=2..5, "
            "four event phases, and 51115-orbit diagnostic horizon are explicit"
        ),
        "N4_residual_matching": (
            "no external no-go witness is used; every attack targets unique "
            "labeled setup selection in this exact census/action"
        ),
        "N5_rhetoric_resolution": (
            "claim is restricted to labeled setups at this finite scope, not "
            "unique orbit selection or any larger physical theory"
        ),
        "N6_partial_closure": (
            "choosing a frame origin or a non-covariant criterion can select "
            "a label, but changes the covariance requirement; unique-orbit "
            "selection was separately tested and not found"
        ),
        "N7_steelman": (
            "Strongest reversal was the singleton argmax-period set; exact "
            "orbit transport shows period is origin-anchored and the set is "
            "not covariant"
        ),
        "N8_cross_cycle_echo": (
            "Cycle 828's 228 keys suppress higher-k origin copies by canonical "
            "rotation representatives; restoring origins yields 748, not a "
            "singleton at the Cycle-852 scope"
        ),
    }
    result["pass"] = (
        len(routes) >= 5
        and all(passed for _name, passed in routes)
        and census["pass"]
        and autopsy["pass"]
        and multiples["pass"]
        and tournament["pass"]
        and scope["pass"]
    )
    return result


def public_trajectory(trajectory: dict[str, object]) -> dict[str, object]:
    e1_first: dict[Key, int] = trajectory["E1_first"]
    e2_first: dict[Key, int] = trajectory["E2_first"]
    periods: dict[Key, int] = trajectory["cycle_periods"]
    return {
        "horizon_orbits_inclusive": TRAJECTORY_HORIZON,
        "E1_stamped_count": len(e1_first),
        "E1_never_count": 748 - len(e1_first),
        "E1_moment_range": (
            min(e1_first.values(), default=None),
            max(e1_first.values(), default=None),
        ),
        "E2_stamped_count": len(e2_first),
        "E2_never_count": 748 - len(e2_first),
        "E2_moment_range": (
            min(e2_first.values(), default=None),
            max(e2_first.values(), default=None),
        ),
        "period_count": len(periods),
        "period_range": (
            min(periods.values(), default=None),
            max(periods.values(), default=None),
        ),
        "unresolved_count": len(trajectory["unresolved_before_clean"]),
        "maximum_weight": trajectory["maximum_weight"],
        "maximum_weight_attainer_count":
            len(trajectory["maximum_weight_attainers"]),
        "deepest_shared_merger_moment":
            trajectory["deepest_shared_merger_moment"],
        "deepest_shared_merger_member_count":
            len(trajectory["deepest_shared_merger_members"]),
        "shared_merger_cohort_count":
            trajectory["shared_merger_cohort_count"],
        "largest_funnel_basin_size":
            trajectory["largest_funnel_basin_size"],
        "largest_funnel_basin_member_count":
            len(trajectory["largest_funnel_basin_members"]),
        "largest_funnel_basin_tie_instances":
            trajectory["largest_funnel_basin_tie_instances"],
        "initial_duplicate_group_histogram":
            trajectory["initial_duplicate_group_histogram"],
        "dirty_coordinate_count": trajectory["dirty_coordinate_count"],
        "schedule_gate_counts": trajectory["schedule_gate_counts"],
        "scalar_shadow": trajectory["scalar_shadow"],
        "determinism_duplicate": trajectory["determinism_duplicate"],
        "trajectory_sha256": trajectory["trajectory_sha256"],
        "runtime_seconds": trajectory["runtime_seconds"],
        "pass": trajectory["pass"],
    }


def render(
    checks: dict[str, bool],
    findings: tuple[str, ...],
    report: dict[str, object],
) -> str:
    lines = tuple(
        f"{'PASS' if passed else 'FAIL'} {name} :: {passed}"
        for name, passed in checks.items()
    ) + findings
    return "\n".join(lines) + "\nSUMMARY_JSON " + compact(report) + "\n"


def main() -> int:
    started = monotonic()
    source_control, sources_before = source_controls()
    program, event_seeds, placements, census = build_census()
    orbits = partition_orbits(census)
    census_report = census_certificate(census, orbits)
    scope_report = cycle828_scope_counts(placements)
    trajectory = trajectory_census(program, event_seeds, census)
    selections = tournament_selections(census, orbits, trajectory)
    tournament_report, criterion_rows = tournament_certificate(
        census, orbits, selections
    )
    autopsy = size1_autopsy(census, orbits, trajectory, selections)
    multiples = multiples_audit(criterion_rows)
    no_go_gate = no_go_discipline_summary(
        census_report, autopsy, multiples, tournament_report, scope_report
    )
    sources_after = {
        relative: sha256((ROOT / relative).read_bytes()).hexdigest()
        for relative in AUDIT_INPUT_PATHS
    }
    elapsed = monotonic() - started
    controls = {
        **source_control,
        "sources_unchanged": sources_before == sources_after,
        "determinism": trajectory["determinism_duplicate"],
        "independent_scalar_shadow": trajectory["scalar_shadow"],
        "no_go_discipline_N1_N8": no_go_gate,
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_under_1400s": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_bytes": None,
        "stdout_under_150KB": None,
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(PRIMARY_FIREWALL.hits),
    }
    controls["pass"] = (
        source_control["pass"]
        and controls["sources_unchanged"]
        and trajectory["scalar_shadow"]["pass"]
        and trajectory["determinism_duplicate"]["boundary_mismatches"] == 0
        and trajectory["determinism_duplicate"]["final_full_state_exact"]
        and no_go_gate["pass"]
        and controls["runtime_under_1400s"]
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
    )

    checks = {
        "THE_CENSUS": census_report["pass"],
        "THE_SIZE1_AUTOPSY": trajectory["pass"] and autopsy["pass"],
        "THE_MULTIPLES_AUDIT": multiples["pass"],
        "THE_TOURNAMENT_REPLAY": tournament_report["pass"],
        "THE_SCOPE_RECONCILIATION": scope_report["pass"],
        "CONTROLS": controls["pass"],
    }
    public_rows = {
        name: {
            "size": row["size"],
            "selection_sha256": row["selection_sha256"],
            "covariance": row["covariance"],
            "union_of_orbits": row["union_of_orbits"],
            "unique_orbit": row["unique_orbit"],
            "unique_setup": row["unique_setup"],
            "eligibility": row["eligibility"],
        }
        for name, row in criterion_rows.items()
    }
    report = {
        "checks": checks,
        "THE_CENSUS": census_report,
        "THE_SIZE1_AUTOPSY": autopsy,
        "THE_MULTIPLES_AUDIT": multiples,
        "THE_TOURNAMENT_REPLAY": {
            **tournament_report,
            "criteria": public_rows,
            "trajectory": public_trajectory(trajectory),
        },
        "THE_SCOPE_RECONCILIATION": scope_report,
        "CONTROLS": controls,
        "pass": all(checks.values()),
    }
    findings = (
        "FINDING THE_CENSUS :: acting group=C_11 simultaneous station-label "
        f"translations; population={census_report['population']}; "
        f"orbits={census_report['orbit_count']}; histogram="
        f"{census_report['orbit_histogram']}; singleton orbits="
        f"{census_report['singleton_orbit_count']}; action free because a "
        "nonzero shift generates prime-order C_11 while every occupied set "
        "has size 2..5",
        "FINDING THE_SIZE1_AUTOPSY :: "
        f"longest-period size={autopsy['longest_period_selection_size']}; "
        f"key={autopsy['longest_period_key']}; period="
        f"{autopsy['longest_period_value']}; +1 image="
        f"{autopsy['frame_witness']['mapped_key']}; image status="
        f"{autopsy['mapped_key_period_status']}; period orbit-constant="
        f"{autopsy['period_is_constant_on_every_frame_orbit']}; "
        "DISQUALIFIED non-covariant, so no singleton-orbit contradiction",
        "FINDING THE_MULTIPLES_AUDIT :: every non-multiple of 11 has an "
        "exact +1/-1 frame witness; no reported size corrected; broken "
        "symmetry is the fixed program/source origin and monitoring phase; "
        f"rows={compact({name: row['size'] for name, row in multiples['nonmultiple_criteria'].items()})}",
        "FINDING THE_TOURNAMENT_REPLAY :: sizes="
        f"{compact(tournament_report['observed_sizes'])}; unique-orbit "
        f"criteria={tournament_report['unique_orbit_criteria']}; covariant "
        "unique-setup candidates="
        f"{tournament_report['covariant_unique_setup_candidates']}; "
        f"{tournament_report['conclusion']}",
        "FINDING THE_SCOPE_RECONCILIATION :: Cycle-828 228 = all k2 "
        "labels 176 + canonical higher-k rotation representatives "
        "28+20+4; Cycle-852 restores origins 0..10 for every higher-k "
        "representative, giving 176+308+220+44=748; both use event phases "
        "0..3 and the same C_11 Cycle-719 ring",
        "FINDING CONTROLS :: SHA/Git-blob pinned literal worktree-relative "
        "inputs; Cycle-852 primary BLOCKLIST text/AST only; duplicate-lane "
        "determinism plus direct scalar shadow; N1-N8 gate; runtime <1400s; "
        "stdout <150KB",
    )

    preliminary = render(checks, findings, report)
    stdout_bytes = len(preliminary.encode("utf-8"))
    controls["stdout_bytes"] = stdout_bytes
    controls["stdout_under_150KB"] = stdout_bytes < STDOUT_LIMIT_BYTES
    controls["pass"] = controls["pass"] and controls["stdout_under_150KB"]
    checks["CONTROLS"] = controls["pass"]
    report["pass"] = all(checks.values())
    report["report_sha256"] = digest({
        key: value for key, value in report.items()
        if key != "report_sha256"
    })
    output = render(checks, findings, report)
    controls["stdout_bytes"] = len(output.encode("utf-8"))
    controls["stdout_under_150KB"] = (
        controls["stdout_bytes"] < STDOUT_LIMIT_BYTES
    )
    checks["CONTROLS"] = controls["pass"] and controls["stdout_under_150KB"]
    report["pass"] = all(checks.values())
    report["report_sha256"] = digest({
        key: value for key, value in report.items()
        if key != "report_sha256"
    })
    output = render(checks, findings, report)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
