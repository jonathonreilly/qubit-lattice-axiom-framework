#!/usr/bin/env python3
"""Cycle 852: exhaustive covariant initial-setup selection tournament.

The declared finite census is the four Cycle-719 two-bank event seeds crossed
with every pairwise-separated source placement of size k=2,3,4,5 on its
oriented eleven-station program ring.  Counts and dynamics are rebuilt from
the landed Cycle-719 core.  Cited later primaries are SHA-pinned provenance
surfaces only: a fail-closed import firewall restricts them to text/AST use.

The frame group is the oriented-ring translation group C_11.  Its generator
adds one to every station label and leaves the core event seed fixed.  This is
a declared bounded frame action, not a claim that the supplied source boundary
or ring orientation has been autonomously selected.
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
    "scripts/frontier_cycle796_monitored_selector_2026_07_28.py",
    "scripts/frontier_cycle822_sstar_basin_2026_07_28.py",
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle833_funnel_family_2026_07_28.py",
    "scripts/frontier_cycle836_offbackbone_depth_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "be0238611e02f9bad8df813430f9decec68d287df267bbf82ba4a63ffc8483c3",
    AUDIT_INPUT_PATHS[2]:
        "269d235c4981eaa4b94cfc200a0d472bf9f1ca8b57c2e14880afe754a9d41c56",
    AUDIT_INPUT_PATHS[3]:
        "b14262f6d54dc4f853bda13f321c816b3e762fa37b0b8276a2bec4955c51c481",
    AUDIT_INPUT_PATHS[4]:
        "bd08f5f503e532c724e6ae28915ba2f0b4202360bbe01458924d689e27c79174",
    AUDIT_INPUT_PATHS[5]:
        "b5f59ed04984d8c1956ff82a1f9af165b35ac2dcac99db4b929dbe3d8dc2e0b5",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "eb2f34cd78fae3ce579d426df2ffe62832003504",
    AUDIT_INPUT_PATHS[2]: "56fd26ec1f09e3690aa0e9cacd1447c289fd7ac0",
    AUDIT_INPUT_PATHS[3]: "1afe4941812f83f5e1fd5cc7c04e57231d703e8d",
    AUDIT_INPUT_PATHS[4]: "b3512e0c3e8acdec7bc3f1cfb4e5bf1a236f8fda",
    AUDIT_INPUT_PATHS[5]: "8e4cb3071ac2be62b1de91c900d30d493675b87d",
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a cited text/AST-only primary is imported."""

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
FRAME_GENERATORS = (1, -1)
E2_LANDED_RULE = "record set = first-clean orbit-return selection-event set"
TRAJECTORY_HORIZON = 51_115


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
    parsed_top_levels = {
        path: len(tree.body) for path, tree in trees.items()
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
        "text_AST_parsed_top_level_counts": parsed_top_levels,
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
        and len(AUDIT_INPUT_PATHS) <= 6
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and all(parsed_top_levels.values())
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
    """Build all four event seeds solely through the Cycle-719 core API."""

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


def derive_census() -> tuple[
    tuple[object, ...], tuple[tuple[int, State], ...], tuple[Key, ...]
]:
    program = K.interleaved_program(FIXTURE_BANKS)
    stations = len(program)
    event_seeds = derive_event_seeds(program)
    keys = tuple(
        (k, event, positions)
        for k in range(MIN_SOURCES, MAX_SOURCES + 1)
        for positions in combinations(range(stations), k)
        if pairwise_separated(positions, stations)
        for event, _state in event_seeds
    )
    if len(keys) != len(set(keys)):
        raise AssertionError("duplicate census key")
    return program, event_seeds, tuple(sorted(keys))


def frame_map(key: Key, shift: int, stations: int) -> Key:
    k, event, positions = key
    moved = tuple(sorted((station + shift) % stations for station in positions))
    return k, event, moved


def orbit_of(key: Key, stations: int) -> tuple[Key, ...]:
    return tuple(sorted({
        frame_map(key, shift, stations) for shift in range(stations)
    }))


def partition_orbits(
    census: tuple[Key, ...], stations: int
) -> tuple[tuple[Key, ...], ...]:
    universe = set(census)
    remaining = set(census)
    rows = []
    while remaining:
        representative = min(remaining)
        orbit = orbit_of(representative, stations)
        if not set(orbit) <= universe:
            raise AssertionError(("frame closure", representative, orbit))
        rows.append(orbit)
        remaining.difference_update(orbit)
    return tuple(sorted(rows, key=lambda row: row[0]))


def census_and_orbits() -> dict[str, object]:
    program, event_seeds, census = derive_census()
    stations = len(program)
    orbits = partition_orbits(census, stations)
    per_k = dict(sorted(Counter(key[0] for key in census).items()))
    placement_per_k = {
        k: population // len(event_seeds) for k, population in per_k.items()
    }
    orbit_histogram = dict(sorted(Counter(map(len, orbits)).items()))
    singleton_orbits = tuple(orbit for orbit in orbits if len(orbit) == 1)
    closure_failures = tuple(
        (generator, key, frame_map(key, generator, stations))
        for generator in FRAME_GENERATORS
        for key in census
        if frame_map(key, generator, stations) not in set(census)
    )
    result = {
        "scope": {
            "fixture_banks": FIXTURE_BANKS,
            "ring_stations": stations,
            "event_seeds": len(event_seeds),
            "source_count_window": (MIN_SOURCES, MAX_SOURCES),
            "placement_predicate": "pairwise nonadjacent on oriented C_11",
        },
        "population": len(census),
        "per_k_populations": per_k,
        "per_k_placements_before_four_event_cross": placement_per_k,
        "orbit_count": len(orbits),
        "orbit_size_histogram": orbit_histogram,
        "singleton_orbits": singleton_orbits,
        "census_sha256": digest(census),
        "orbit_partition_sha256": digest(orbits),
        "frame_generators": FRAME_GENERATORS,
        "frame_closure_failures": closure_failures,
        "census": census,
        "orbits": orbits,
        "program": program,
        "event_seeds": event_seeds,
    }
    result["pass"] = (
        stations == 11
        and len(event_seeds) == 4
        and set(per_k) == set(range(MIN_SOURCES, MAX_SOURCES + 1))
        and sum(per_k.values()) == len(census)
        and sum(map(len, orbits)) == len(census)
        and not closure_failures
    )
    return result


def covariance_witness(
    selection: Selection,
    census: tuple[Key, ...],
    stations: int,
) -> dict[str, object]:
    universe = set(census)
    for generator in FRAME_GENERATORS:
        mapped = frozenset(frame_map(key, generator, stations) for key in selection)
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
    return {"covariant": True, "generator": None, "witness": None}


def structural_bound(
    census_report: dict[str, object],
    selections: dict[str, Selection] | None = None,
) -> dict[str, object]:
    census = census_report["census"]
    orbits = census_report["orbits"]
    stations = census_report["scope"]["ring_stations"]
    orbit_by_key = {
        key: frozenset(orbit) for orbit in orbits for key in orbit
    }
    enumerated_subset_failures = []
    # Exhaustively prove the fixed-set lemma orbit-by-orbit: adding or omitting
    # one orbit is the only generator-invariant membership choice.
    for orbit in orbits:
        representative = orbit[0]
        generated = orbit_of(representative, stations)
        if generated != orbit:
            enumerated_subset_failures.append((representative, generated, orbit))
    criterion_rows = {}
    for name, selection in sorted((selections or {}).items()):
        witness = covariance_witness(selection, census, stations)
        union_reconstruction = frozenset(
            key
            for key in selection
            if orbit_by_key[key] <= selection
        )
        criterion_rows[name] = {
            **witness,
            "union_of_orbits": union_reconstruction == selection,
        }
    result = {
        "lemma": (
            "For a G-covariant Boolean selector, membership is constant on "
            "each generated G-orbit; therefore its selection set is a union "
            "of orbits. A unique labeled setup requires an orbit of size one."
        ),
        "proof_method": (
            "enumerate each census orbit under the declared generators and "
            "mechanically compare every tournament selection with its images"
        ),
        "orbit_generation_failures": tuple(enumerated_subset_failures),
        "criterion_covariance": criterion_rows,
        "singleton_orbit_count": len(census_report["singleton_orbits"]),
    }
    result["pass"] = (
        not enumerated_subset_failures
        and all(
            row["covariant"] == row["union_of_orbits"]
            for row in criterion_rows.values()
        )
    )
    return result


def watched_registers() -> tuple[tuple[str, int], ...]:
    """The clean-postimage fields used by the Cycle-719 held predicate."""

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
    """Re-derive packed admissibility coordinates through core pack/unpack.

    No predecessor coordinate table is imported.  Every watched bank/link bit
    is marked in an otherwise-zero core state, packed, and required to change
    exactly one global coordinate.
    """

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


def build_initial_states(
    program: tuple[object, ...],
    event_seeds: tuple[tuple[int, State], ...],
    census: tuple[Key, ...],
) -> tuple[tuple[State, ...], dict[str, object]]:
    seed_by_event = dict(event_seeds)
    word_cache = {
        positions: synchronous_word(program, positions)
        for _k, _event, positions in census
    }
    states = []
    composition_failures = rail_failures = inverse_failures = 0
    for k, event, positions in census:
        before = seed_by_event[event]
        after, rail_a, rail_b, _trace = K.run_orbit(
            before, program, token_positions=positions
        )
        expected_rail = tuple(
            int(station in positions) for station in range(len(program))
        )
        composition_failures += after != K.A.apply_semantic(
            before, word_cache[positions]
        )
        rail_failures += rail_a != expected_rail or any(rail_b)
        restored, inverse_a, inverse_b, _ = K.run_orbit(
            after, program, token_positions=positions, reverse=True
        )
        inverse_failures += (
            restored != before or inverse_a != rail_a or inverse_b != rail_b
        )
        if len(positions) != k:
            raise AssertionError(("key/source mismatch", k, positions))
        states.append(after)
    report = {
        "state_count": len(states),
        "state_bits": len(states[0]),
        "word_gate_counts_by_k": {
            k: tuple(sorted({
                len(word_cache[positions])
                for key_k, _event, positions in census if key_k == k
            }))
            for k in range(MIN_SOURCES, MAX_SOURCES + 1)
        },
        "composition_failures": composition_failures,
        "rail_failures": rail_failures,
        "inverse_failures": inverse_failures,
        "state_catalog_sha256": digest(tuple(
            sha256(bytes(state)).hexdigest() for state in states
        )),
    }
    report["pass"] = (
        report["state_count"] == len(census)
        and report["state_bits"] > 0
        and composition_failures == rail_failures == inverse_failures == 0
    )
    return tuple(states), report


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
    """Compile every H chunk once for the complete bit-sliced census."""

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


def advance(
    columns: list[int], schedule: tuple[tuple[int, int, int, int, int], ...]
) -> None:
    for kind, first, second, third, mask in schedule:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first] & mask
        else:
            columns[third] ^= columns[first] & columns[second] & mask


def compile_fast_schedules(
    schedules: tuple[tuple[tuple[int, int, int, int, int], ...], ...]
) -> tuple[Callable[[list[int]], None], ...]:
    """Compile the fixed exact circuit to direct Python assignments.

    This is a semantics-preserving runtime specialization, not generated
    evidence: the retained tuple schedules remain the audited gate manifest.
    It removes per-gate tuple dispatch so the 65,536-orbit census stays inside
    the declared wall-clock bound.
    """

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


def equality_mask(
    columns: list[int], reference: list[int], candidate_mask: int
) -> int:
    differences = 0
    for left, right in zip(columns, reference):
        differences |= left ^ right
    return candidate_mask & ~differences


def maximum_weight_mask(
    columns: list[int], all_mask: int
) -> tuple[int, int]:
    """Return the exact maximum Hamming weight and every attaining lane."""

    counters: list[int] = []
    for column in columns:
        carry = column & all_mask
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
    candidates = all_mask
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
    columns: list[int], all_mask: int, wire_order: tuple[int, ...]
) -> tuple[int, ...]:
    """Partition exactly by all state bits, retaining only shared states."""

    groups = [all_mask]
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


def trajectory_census(census_report: dict[str, object]) -> dict[str, object]:
    """Scan the full census exactly through the declared finite horizon.

    E1 is monitored after every individual post-engagement H chunk and E2 at
    orbit returns.  Cycle periods are first exact full-state returns observed
    before an E2 clean hit.  Transients are first E2 clean hits.  Unresolved
    lanes remain explicitly unresolved; no extrapolation is made.
    """

    started = monotonic()
    program = census_report["program"]
    event_seeds = census_report["event_seeds"]
    census = census_report["census"]
    states, initial_report = build_initial_states(
        program, event_seeds, census
    )
    # One exact duplicate lane is evolved by the same compiled machinery and
    # compared at every monitored boundary as the determinism replay control.
    simulation_keys = census + (census[0],)
    duplicate_lane = len(census)
    columns = pack_states(states + (states[0],))
    initial_columns = columns.copy()
    schedules = masked_h_schedules(program, simulation_keys)
    fast_schedules = compile_fast_schedules(schedules)
    dirty_indices = dirty_global_indices()
    all_mask = (1 << len(census)) - 1
    simulation_mask = (1 << len(simulation_keys)) - 1
    initial_clean_all = clean_mask(columns, dirty_indices, simulation_mask)
    initial_clean = initial_clean_all & all_mask
    determinism_mismatches = int(
        bool(initial_clean_all & 1)
        != bool(initial_clean_all & (1 << duplicate_lane))
    )
    e1_first: dict[Key, int] = {
        census[lane]: 0 for lane in lane_numbers(initial_clean)
    }
    e2_first: dict[Key, int] = dict(e1_first)
    e1_found_mask = initial_clean
    e2_found_mask = initial_clean
    cycle_period: dict[Key, int] = {}
    unresolved_cycle_mask = all_mask & ~initial_clean

    initial_weight, initial_weight_mask = maximum_weight_mask(columns, all_mask)
    global_max_weight = initial_weight
    global_max_mask = initial_weight_mask

    # A static high-variance order accelerates exact duplicate partitioning;
    # every wire is still visited whenever a candidate group survives.
    wire_order = tuple(sorted(
        range(len(columns)),
        key=lambda wire: (
            abs(2 * columns[wire].bit_count() - len(census)), wire
        ),
    ))
    initial_duplicate_groups = duplicate_groups(columns, all_mask, wire_order)
    initial_group_by_lane = {}
    for group in initial_duplicate_groups:
        members = frozenset(lane_numbers(group))
        for lane in members:
            initial_group_by_lane[lane] = members

    merger_first_moment: dict[tuple[int, ...], int] = {}
    largest_basin_size = 0
    largest_basin_groups: set[tuple[int, ...]] = set()

    for orbit in range(1, TRAJECTORY_HORIZON + 1):
        for step, apply_chunk in enumerate(fast_schedules, 1):
            apply_chunk(columns)
            clean_all = clean_mask(columns, dirty_indices, simulation_mask)
            clean = clean_all & all_mask
            determinism_mismatches += (
                bool(clean_all & 1)
                != bool(clean_all & (1 << duplicate_lane))
            )
            new_e1 = clean & ~e1_found_mask
            absolute_h = (orbit - 1) * len(program) + step
            for lane in lane_numbers(new_e1):
                e1_first[census[lane]] = absolute_h
            e1_found_mask |= new_e1

        orbit_clean_all = clean_mask(columns, dirty_indices, simulation_mask)
        orbit_clean = orbit_clean_all & all_mask
        new_e2 = orbit_clean & ~e2_found_mask
        for lane in lane_numbers(new_e2):
            e2_first[census[lane]] = orbit
        e2_found_mask |= new_e2

        recurrence = equality_mask(
            columns, initial_columns, unresolved_cycle_mask & ~orbit_clean
        )
        primary_recurrence = equality_mask(columns, initial_columns, 1)
        duplicate_recurrence = equality_mask(
            columns, initial_columns, 1 << duplicate_lane
        )
        determinism_mismatches += (
            bool(primary_recurrence) != bool(duplicate_recurrence)
        )
        for lane in lane_numbers(recurrence):
            cycle_period[census[lane]] = orbit
        unresolved_cycle_mask &= ~(orbit_clean | recurrence)

        weight, weight_mask = maximum_weight_mask(columns, all_mask)
        if weight > global_max_weight:
            global_max_weight = weight
            global_max_mask = weight_mask
        elif weight == global_max_weight:
            global_max_mask |= weight_mask

        shared = []
        for group in duplicate_groups(columns, all_mask, wire_order):
            members = tuple(lane_numbers(group))
            member_set = frozenset(members)
            # Exclude identities already present at t=0: a merger requires at
            # least two initially distinct exact states.
            if all(
                initial_group_by_lane.get(lane) == member_set
                for lane in members
            ):
                continue
            shared.append(members)
            merger_first_moment.setdefault(members, orbit)
            size = len(members)
            if size > largest_basin_size:
                largest_basin_size = size
                largest_basin_groups = {members}
            elif size == largest_basin_size:
                largest_basin_groups.add(members)

    deepest_moment = max(merger_first_moment.values(), default=None)
    duplicate_final_exact = all(
        bool(column & 1) == bool(column & (1 << duplicate_lane))
        for column in columns
    )
    deepest_masks = tuple(
        sum(1 << lane for lane in members)
        for members, moment in merger_first_moment.items()
        if moment == deepest_moment
    )
    largest_mask = 0
    for members in largest_basin_groups:
        largest_mask |= sum(1 << lane for lane in members)
    deepest_mask = 0
    for mask in deepest_masks:
        deepest_mask |= mask

    e1_selection = frozenset(e1_first)
    e2_selection = frozenset(e2_first)
    result = {
        "declared_horizon_orbits_inclusive": TRAJECTORY_HORIZON,
        "E1_reading": {
            "cadence": "every post-engagement H-station boundary",
            "coordinate": "absolute_H",
            "first_clean": e1_first,
            "stamped": e1_selection,
            "never_stamped_through_horizon": frozenset(census) - e1_selection,
        },
        "E2_reading": {
            "cadence": "orbit-return boundary",
            "landed_rule_quote": E2_LANDED_RULE,
            "first_clean": e2_first,
            "stamped": e2_selection,
            "never_stamped_through_horizon": frozenset(census) - e2_selection,
        },
        "transient_lengths": dict(e2_first),
        "cycle_periods_before_clean": cycle_period,
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
        "shared_merger_cohort_count": len(merger_first_moment),
        "largest_funnel_basin_size": largest_basin_size,
        "largest_funnel_basin_members": frozenset(
            census[lane] for lane in lane_numbers(largest_mask)
        ),
        "largest_funnel_basin_tie_instances": len(largest_basin_groups),
        "initial_state_duplicate_group_sizes": tuple(sorted(
            Counter(group.bit_count() for group in initial_duplicate_groups).items()
        )),
        "initial_build": initial_report,
        "masked_schedule_gate_counts": tuple(map(len, schedules)),
        "dirty_coordinate_count": len(dirty_indices),
        "determinism_replay": {
            "duplicated_key": census[0],
            "boundary_mismatches": determinism_mismatches,
            "final_full_state_exact": duplicate_final_exact,
        },
        "runtime_seconds": round(monotonic() - started, 6),
    }
    result["trajectory_digest"] = digest({
        "E1": tuple(sorted(e1_first.items())),
        "E2": tuple(sorted(e2_first.items())),
        "cycles": tuple(sorted(cycle_period.items())),
        "maximum_weight": global_max_weight,
        "maximum_weight_attainers": tuple(sorted(result["maximum_weight_attainers"])),
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
        initial_report["pass"]
        and len(e1_first) <= len(census)
        and len(e2_first) <= len(census)
        and e2_selection <= e1_selection
        and not (set(e2_first) & set(cycle_period))
        and (
            len(e2_first) + len(cycle_period)
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
    return frozenset(key for key, value in values.items() if value == target)


def index_runs(indices: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    if not indices:
        return ()
    rows = []
    start = previous = indices[0]
    for index in indices[1:]:
        if index == previous + 1:
            previous = index
            continue
        rows.append((start, previous))
        start = previous = index
    rows.append((start, previous))
    return tuple(rows)


def encoded_selection(
    selection: Selection, census: tuple[Key, ...]
) -> dict[str, object]:
    index = {key: lane for lane, key in enumerate(census)}
    indices = tuple(sorted(index[key] for key in selection))
    return {
        "encoding": (
            "inclusive zero-based runs into A_CENSUS_AND_ORBITS sorted census"
        ),
        "runs": index_runs(indices),
        "key_sha256": digest(tuple(sorted(selection))),
    }


def tournament(
    census_report: dict[str, object], trajectory: dict[str, object]
) -> tuple[dict[str, object], dict[str, Selection]]:
    census = census_report["census"]
    orbits = census_report["orbits"]
    orbit_sizes = {
        key: len(orbit) for orbit in orbits for key in orbit
    }
    e1_first = trajectory["E1_reading"]["first_clean"]
    e2_first = trajectory["E2_reading"]["first_clean"]
    cycle_periods = trajectory["cycle_periods_before_clean"]
    selections: dict[str, Selection] = {
        "maximal_source_count_k": frozenset(
            key for key in census if key[0] == max(row[0] for row in census)
        ),
        "minimal_source_count_k": frozenset(
            key for key in census if key[0] == min(row[0] for row in census)
        ),
        "E2_earliest_record_moment": extremal_selection(e2_first, min),
        "E2_latest_record_moment": extremal_selection(e2_first, max),
        "E1_earliest_first_clean_absolute_H":
            extremal_selection(e1_first, min),
        "E1_latest_first_clean_absolute_H":
            extremal_selection(e1_first, max),
        "E2_stamped": trajectory["E2_reading"]["stamped"],
        "E2_never_stamped_through_horizon":
            trajectory["E2_reading"]["never_stamped_through_horizon"],
        "E1_stamped": trajectory["E1_reading"]["stamped"],
        "E1_never_stamped_through_horizon":
            trajectory["E1_reading"]["never_stamped_through_horizon"],
        "maximal_orbit_size_most_symmetric_placement": frozenset(
            key for key, size in orbit_sizes.items()
            if size == max(orbit_sizes.values())
        ),
        "minimal_orbit_size_least_symmetric_placement": frozenset(
            key for key, size in orbit_sizes.items()
            if size == min(orbit_sizes.values())
        ),
        "longest_transient": extremal_selection(
            trajectory["transient_lengths"], max
        ),
        "shortest_transient": extremal_selection(
            trajectory["transient_lengths"], min
        ),
        "longest_cycle_period": extremal_selection(cycle_periods, max),
        "shortest_cycle_period": extremal_selection(cycle_periods, min),
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
    orbit_sets = {frozenset(orbit) for orbit in orbits}
    stations = census_report["scope"]["ring_stations"]
    rows = {}
    for name, selection in selections.items():
        covariance = covariance_witness(selection, census, stations)
        unique_orbit = selection in orbit_sets
        unique_setup = len(selection) == 1
        rows[name] = {
            "selection_set": encoded_selection(selection, census),
            "size": len(selection),
            "unique_orbit": unique_orbit,
            "unique_setup": unique_setup,
            "singleton_orbit_selection": unique_orbit and unique_setup,
            "covariance": covariance,
            "eligibility": (
                "QUALIFIED" if covariance["covariant"] else "DISQUALIFIED"
            ),
        }
    declared_names = tuple(selections)
    result = {
        "declared_finite_scope": (
            f"all {len(census)} census keys; orbit moments 0.."
            f"{TRAJECTORY_HORIZON}; E1 H boundaries 0.."
            f"{TRAJECTORY_HORIZON * census_report['scope']['ring_stations']}"
        ),
        "no_fitted_parameters": True,
        "ties_are_full_selection_sets": True,
        "E1_E2_owner_fork": (
            "both readings run; neither is designated the rule"
        ),
        "declared_criteria": declared_names,
        "outcome_table": rows,
        "selection_layer_digest": digest(tuple(
            (name, tuple(sorted(selection)))
            for name, selection in selections.items()
        )),
    }
    result["pass"] = (
        len(rows) == 20
        and tuple(rows) == declared_names
        and all(selection <= frozenset(census) for selection in selections.values())
        and all(
            row["size"] == sum(
                stop - start + 1
                for start, stop in row["selection_set"]["runs"]
            )
            for row in rows.values()
        )
        and any(row["eligibility"] == "DISQUALIFIED" for row in rows.values())
        and any(row["eligibility"] == "QUALIFIED" for row in rows.values())
    )
    return result, selections


def verdict(
    census_report: dict[str, object], tournament_report: dict[str, object]
) -> dict[str, object]:
    rows = tournament_report["outcome_table"]
    candidates = tuple(
        name for name, row in rows.items()
        if row["eligibility"] == "QUALIFIED"
        and row["singleton_orbit_selection"]
    )
    singleton_orbits = census_report["singleton_orbits"]
    if candidates:
        tournament_verdict = "SELECTION_CANDIDATE_FOUND"
        proposal_language = (
            "PROPOSAL-ONLY: adoption of any candidate is owner-level"
        )
    else:
        tournament_verdict = "SELECTION_OPEN_AFTER_DECLARED_CRITERIA"
        proposal_language = (
            "No declared criterion supplies an adoption proposal"
        )
    scope_no_go = (
        "NO_COVARIANT_UNIQUE_SETUP_SELECTION_AT_SCOPE"
        if not singleton_orbits else
        "COVARIANT_UNIQUE_SETUP_NOT_EXCLUDED_BY_ORBIT_STRUCTURE"
    )
    result = {
        "tournament_verdict": tournament_verdict,
        "candidate_names": candidates,
        "proposal_language": proposal_language,
        "census_level_verdict": scope_no_go,
        "scope_no_go": (
            "No covariant Boolean criterion whatsoever can select one labeled "
            "setup in this declared census because every frame orbit has size "
            "greater than one. This is a scoped no-go, not a theorem beyond "
            "the Cycle-852 census/frame action."
        ) if not singleton_orbits else None,
        "qualified_criterion_count": sum(
            row["eligibility"] == "QUALIFIED" for row in rows.values()
        ),
        "disqualified_criterion_count": sum(
            row["eligibility"] == "DISQUALIFIED" for row in rows.values()
        ),
    }
    result["pass"] = (
        (tournament_verdict == "SELECTION_CANDIDATE_FOUND") == bool(candidates)
        and (
            scope_no_go == "NO_COVARIANT_UNIQUE_SETUP_SELECTION_AT_SCOPE"
        ) == (not singleton_orbits)
    )
    return result


def public_trajectory(report: dict[str, object]) -> dict[str, object]:
    e1 = report["E1_reading"]
    e2 = report["E2_reading"]
    return {
        "declared_horizon_orbits_inclusive":
            report["declared_horizon_orbits_inclusive"],
        "E1_reading": {
            "cadence": e1["cadence"],
            "coordinate": e1["coordinate"],
            "stamped_count": len(e1["stamped"]),
            "never_stamped_count": len(e1["never_stamped_through_horizon"]),
            "earliest_absolute_H": min(e1["first_clean"].values(), default=None),
            "latest_absolute_H": max(e1["first_clean"].values(), default=None),
        },
        "E2_reading": {
            "cadence": e2["cadence"],
            "landed_rule_quote": e2["landed_rule_quote"],
            "stamped_count": len(e2["stamped"]),
            "never_stamped_count": len(e2["never_stamped_through_horizon"]),
            "earliest_orbit": min(e2["first_clean"].values(), default=None),
            "latest_orbit": max(e2["first_clean"].values(), default=None),
        },
        "transient_count": len(report["transient_lengths"]),
        "cycle_count": len(report["cycle_periods_before_clean"]),
        "unresolved_count": len(report["unresolved_before_clean"]),
        "shortest_cycle_period": min(
            report["cycle_periods_before_clean"].values(), default=None
        ),
        "longest_cycle_period": max(
            report["cycle_periods_before_clean"].values(), default=None
        ),
        "maximum_weight": report["maximum_weight"],
        "maximum_weight_attainer_count":
            len(report["maximum_weight_attainers"]),
        "deepest_shared_merger_moment":
            report["deepest_shared_merger_moment"],
        "deepest_shared_merger_member_count":
            len(report["deepest_shared_merger_members"]),
        "shared_merger_cohort_count": report["shared_merger_cohort_count"],
        "largest_funnel_basin_size": report["largest_funnel_basin_size"],
        "largest_funnel_basin_member_count":
            len(report["largest_funnel_basin_members"]),
        "largest_funnel_basin_tie_instances":
            report["largest_funnel_basin_tie_instances"],
        "initial_state_duplicate_group_sizes":
            report["initial_state_duplicate_group_sizes"],
        "initial_build": report["initial_build"],
        "masked_schedule_gate_counts": report["masked_schedule_gate_counts"],
        "dirty_coordinate_count": report["dirty_coordinate_count"],
        "determinism_replay": report["determinism_replay"],
        "trajectory_digest": report["trajectory_digest"],
        "runtime_seconds": report["runtime_seconds"],
        "pass": report["pass"],
    }


def public_census(report: dict[str, object]) -> dict[str, object]:
    return {
        key: value for key, value in report.items()
        if key not in {"census", "orbits", "program", "event_seeds"}
    }


def main() -> int:
    started = monotonic()
    controls = source_controls()
    census = census_and_orbits()
    trajectory = trajectory_census(census)
    tournament_report, selections = tournament(census, trajectory)
    replay_tournament, replay_selections = tournament(census, trajectory)
    selection_replay_exact = (
        tournament_report["selection_layer_digest"]
        == replay_tournament["selection_layer_digest"]
        and selections == replay_selections
    )
    structural = structural_bound(census, selections)
    final_verdict = verdict(census, tournament_report)
    elapsed = monotonic() - started
    checks = {
        "A_CENSUS_AND_ORBITS": census["pass"],
        "B_STRUCTURAL_BOUND": structural["pass"],
        "C_TOURNAMENT": trajectory["pass"] and tournament_report["pass"],
        "D_VERDICT": final_verdict["pass"],
        "E_CONTROLS": (
            controls["pass"]
            and elapsed < AUDIT_TIMEOUT_SEC
            and not PRIMARY_FIREWALL.hits
            and trajectory["determinism_replay"]["boundary_mismatches"] == 0
            and trajectory["determinism_replay"]["final_full_state_exact"]
            and selection_replay_exact
        ),
    }
    report = {
        "checks": checks,
        "A_CENSUS_AND_ORBITS": public_census(census),
        "B_STRUCTURAL_BOUND": structural,
        "C_TOURNAMENT": {
            **tournament_report,
            "trajectory_census": public_trajectory(trajectory),
        },
        "D_VERDICT": final_verdict,
        "E_CONTROLS": {
            **controls,
            "determinism_replay_exact": selection_replay_exact,
            "runtime_under_1400s": elapsed < AUDIT_TIMEOUT_SEC,
            "stdout_under_150KB": None,
        },
        "runtime_seconds": round(elapsed, 6),
        "pass": all(checks.values()),
    }
    report["report_sha256"] = digest(report)
    findings = (
        "FINDING A_CENSUS_AND_ORBITS :: "
        f"per-k populations={census['per_k_populations']}; "
        f"orbit count={census['orbit_count']}; orbit-size histogram="
        f"{census['orbit_size_histogram']}; complete SINGLETON orbits="
        f"{census['singleton_orbits']}",
        "FINDING B_STRUCTURAL_BOUND :: " + structural["lemma"],
        "FINDING C_TOURNAMENT :: " + compact({
            name: {
                "size": row["size"],
                "unique orbit?": row["unique_orbit"],
                "unique setup?": row["unique_setup"],
                "eligibility": row["eligibility"],
            }
            for name, row in tournament_report["outcome_table"].items()
        }),
        "FINDING D_VERDICT :: "
        f"{final_verdict['tournament_verdict']}; "
        f"{final_verdict['census_level_verdict']}; candidates="
        f"{final_verdict['candidate_names']}",
        "FINDING E_CONTROLS :: SHA-pinned literal worktree-relative inputs; "
        "cited primaries BLOCKLIST text/AST only; exact dynamics duplicate "
        "and selection replay; runtime < 1400s; stdout < 150KB",
    )
    preliminary_lines = tuple(
        f"{'PASS' if passed else 'FAIL'} {name} :: {passed}"
        for name, passed in checks.items()
    ) + findings
    preliminary = "\n".join(preliminary_lines) + "\nSUMMARY_JSON " + compact(report) + "\n"
    stdout_ok = len(preliminary.encode("utf-8")) < STDOUT_LIMIT_BYTES
    report["E_CONTROLS"]["stdout_under_150KB"] = stdout_ok
    checks["E_CONTROLS"] = checks["E_CONTROLS"] and stdout_ok
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
