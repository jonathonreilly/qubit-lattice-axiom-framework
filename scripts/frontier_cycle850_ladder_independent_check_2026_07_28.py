#!/usr/bin/env python3
"""Cycle 850 independent adversarial checker: the stratified ladder.

The Cycle-850 and Cycle-849 runners are SHA-pinned source primaries.  This
checker reads them as text/AST only and refuses their import.  Cycle-719 is an
explicit executable core dependency; all population, wavefront, integer-state,
class-split, and mark-search logic below is implemented in this file.
"""
from __future__ import annotations

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle850_stratum_mark_ladder_2026_07_28.py",
    "scripts/frontier_cycle849_scheduling_contrast_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import comb
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_850, PRIMARY_849, CORE_719 = AUDIT_INPUT_PATHS
EXPECTED_SHA256 = {
    PRIMARY_850:
        "6e893336187058cc87ceb068093fed44b28eebee5e93a480f965d399056cdd4c",
    PRIMARY_849:
        "0f1d15c444514f81ac007e2c122b3b47c917bec9a01de8b4e5fef358ef910818",
    CORE_719:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
EXPECTED_GIT_BLOB = {
    PRIMARY_850: "6bb959a5e73c3a06c4703064af0ae0f221f6f6f4",
    PRIMARY_849: "f2e842dbdbc04df27ddd078424a5cd9bc9455af5",
    CORE_719: "c123b8d681c3d76fce08ef13d7673622deac64ad",
}
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
FIXTURE_BANKS = 2
EVENT_COUNT = 4
STRATA = (4, 5)
K3_MARK_BITS = (256, 262)
RUNTIME_LIMIT_SECONDS = 1400
STDOUT_LIMIT_BYTES = 150 * 1024

Key = tuple[int, tuple[int, ...], int]
Gate = tuple[int, int, int, int]


class _SourcePrimaryFirewall(importlib.abc.MetaPathFinder):
    """Turn accidental import/execution of either source primary into failure."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None,
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids source-primary import: {fullname}")
        return None


BLOCKLISTED_MODULES = tuple(sorted((Path(PRIMARY_850).stem, Path(PRIMARY_849).stem)))
FIREWALL = _SourcePrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)
sys.path.insert(0, str(ROOT / "scripts"))

# Authorized executable dependency, intentionally not a source primary.
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values: list[ast.expr] = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == name
                   for target in node.targets):
                values.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            values.append(node.value)
    if len(values) != 1:
        return None
    try:
        return ast.literal_eval(values[0])
    except (TypeError, ValueError):
        return None


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_controls() -> tuple[dict[str, object], tuple[Key, ...]]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {
        path: ast.parse(payload, filename=path) for path, payload in payloads.items()
    }
    self_tree = ast.parse(Path(__file__).read_bytes(), filename=Path(__file__).name)
    rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "worktree_relative": not Path(path).is_absolute(),
        "access": (
            "WORKTREE_TEXT_AST_ONLY_BLOCKLISTED"
            if path in (PRIMARY_850, PRIMARY_849)
            else "AUTHORIZED_EXECUTABLE_CYCLE719_CORE"
        ),
        "sha256": sha256(payloads[path]).hexdigest(),
        "expected_sha256": EXPECTED_SHA256[path],
        "sha256_exact": sha256(payloads[path]).hexdigest() == EXPECTED_SHA256[path],
        "git_blob": git_blob(payloads[path]),
        "expected_git_blob": EXPECTED_GIT_BLOB[path],
        "git_blob_exact": git_blob(payloads[path]) == EXPECTED_GIT_BLOB[path],
    } for path in AUDIT_INPUT_PATHS)
    k3_value = literal_assignment(trees[PRIMARY_849], "K3_OPEN_KEYS")
    if not isinstance(k3_value, tuple):
        raise AssertionError("Cycle-849 K3_OPEN_KEYS is not one literal tuple")
    k3_keys = tuple(k3_value)
    marker_sets = {
        PRIMARY_850: {"stratum_populations", "meeting_structure", "minimal_mark_hunt"},
        PRIMARY_849: {"trio_geometry", "reconstruct_minimal_discriminator"},
        CORE_719: {"interleaved_program", "run_orbit", "held_certificate"},
    }
    markers_exact = all(
        required <= function_names(trees[path])
        for path, required in marker_sets.items()
    )
    literal_paths = literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
    passed = bool(
        literal_paths == AUDIT_INPUT_PATHS
        and all(row["exists"] and row["worktree_relative"] for row in rows)
        and all(row["sha256_exact"] and row["git_blob_exact"] for row in rows)
        and markers_exact
        and len(k3_keys) == 10
        and not any(name in sys.modules for name in BLOCKLISTED_MODULES)
        and not FIREWALL.hits
    )
    return {
        "source_rows": rows,
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal": literal_paths == AUDIT_INPUT_PATHS,
        "all_paths_existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"] for row in rows
        ),
        "source_AST_markers_exact": markers_exact,
        "cycle849_K3_OPEN_KEYS_literal_count": len(k3_keys),
        "blocklisted_modules": BLOCKLISTED_MODULES,
        "blocklisted_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "pass": passed,
    }, k3_keys


def cycle_distance(left: int, right: int, stations: int) -> int:
    clockwise = (right - left) % stations
    return min(clockwise, stations - clockwise)


def independent_placements(stations: int, width: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        placement for placement in combinations(range(stations), width)
        if all(cycle_distance(a, b, stations) > 1
               for a, b in combinations(placement, 2))
    )


def independent_cycle_count(stations: int, width: int) -> int:
    return stations * comb(stations - width - 1, width - 1) // width


def derive_populations(
    program: tuple[object, ...],
) -> tuple[dict[str, object], dict[int, tuple[Key, ...]]]:
    stations = len(program)
    keys_by_k: dict[int, tuple[Key, ...]] = {}
    rows = []
    for width in STRATA:
        placements = independent_placements(stations, width)
        keys = tuple(
            (width, placement, event)
            for placement in placements for event in range(EVENT_COUNT)
        )
        keys_by_k[width] = keys
        rows.append({
            "k": width,
            "position_population": len(placements),
            "independent_cycle_closed_form": independent_cycle_count(stations, width),
            "event_population": EVENT_COUNT,
            "event_key_population": len(keys),
            "placements_sha256": digest(placements),
            "keys_sha256": digest(keys),
        })
    passed = bool(
        stations == 11
        and tuple(row["position_population"] for row in rows) == (55, 11)
        and tuple(row["event_key_population"] for row in rows) == (220, 44)
        and all(row["position_population"] == row["independent_cycle_closed_form"]
                for row in rows)
    )
    return {
        "name": "THE_POPULATIONS",
        "status": "PASS" if passed else "FAIL",
        "finding": (
            "THE_POPULATIONS PASS: Cycle-719 independently yields an 11-station "
            "ring; direct nonadjacent subset enumeration gives k=4: 55 placements/"
            "220 event keys and k=5: 11 placements/44 event keys."
            if passed else
            f"THE_POPULATIONS FAIL: independently derived rows are {rows}."
        ),
        "method": (
            "Use only len(Cycle-719 interleaved_program(2)); enumerate every "
            "nonadjacent cycle subset and cross-check n/k*C(n-k-1,k-1)."
        ),
        "derived_station_count": stations,
        "rows": tuple(rows),
        "pass": passed,
    }, keys_by_k


def wavefront_meet(
    positions: tuple[int, ...], stations: int,
) -> tuple[int, tuple[int, ...]]:
    """Grow one graph ball per source one edge/tick; return first intersection."""

    balls = [{source} for source in positions]
    for tick in range(stations + 1):
        common = set.intersection(*balls)
        if common:
            return tick, tuple(sorted(common))
        balls = [
            ball | {(vertex - 1) % stations for vertex in ball}
                 | {(vertex + 1) % stations for vertex in ball}
            for ball in balls
        ]
    raise AssertionError(("wavefronts did not meet", positions))


def distance_minimax(
    positions: tuple[int, ...], stations: int,
) -> tuple[int, tuple[int, ...]]:
    heights = tuple(
        max(cycle_distance(vertex, source, stations) for source in positions)
        for vertex in range(stations)
    )
    radius = min(heights)
    return radius, tuple(i for i, height in enumerate(heights) if height == radius)


def derive_meets(
    keys_by_k: dict[int, tuple[Key, ...]], stations: int,
) -> tuple[dict[str, object], dict[int, dict[tuple[int, ...], tuple[int, tuple[int, ...]]]]]:
    expected = {
        4: (((3, 1), 11), ((4, 3), 44)),
        5: (((4, 1), 11),),
    }
    lookup: dict[int, dict[tuple[int, ...], tuple[int, tuple[int, ...]]]] = {}
    stratum_rows = []
    all_exact = True
    for width in STRATA:
        placements = tuple(dict.fromkeys(key[1] for key in keys_by_k[width]))
        per_position = []
        signatures: dict[tuple[int, int], int] = {}
        center_counts: dict[int, int] = {}
        lookup[width] = {}
        for placement in placements:
            meet = wavefront_meet(placement, stations)
            minimax = distance_minimax(placement, stations)
            lookup[width][placement] = meet
            signature = (meet[0], len(meet[1]))
            signatures[signature] = signatures.get(signature, 0) + 1
            for center in meet[1]:
                center_counts[center] = center_counts.get(center, 0) + 1
            per_position.append({
                "positions": placement,
                "tick": meet[0],
                "centers": meet[1],
                "center_multiplicity": len(meet[1]),
                "wavefront_equals_distance_minimax": meet == minimax,
            })
        signature_rows = tuple(sorted(signatures.items()))
        row_pass = bool(
            signature_rows == expected[width]
            and all(row["wavefront_equals_distance_minimax"] for row in per_position)
        )
        all_exact &= row_pass
        stratum_rows.append({
            "k": width,
            "meet_tick_center_multiplicity_population": signature_rows,
            "meet_center_support": tuple(sorted(center_counts)),
            "meet_center_occurrence_counts": tuple(sorted(center_counts.items())),
            "position_rows": tuple(per_position),
            "pass": row_pass,
        })
    finding = (
        "THE_MEETS PASS: own simultaneous C11 wavefront growth gives k=4 "
        "exactly 11 tick-3 single-center and 44 tick-4 triple-center meetings; "
        "k=5 gives exactly 11 tick-4 single-center meetings."
        if all_exact else
        f"THE_MEETS FAIL: independently derived strata are {stratum_rows}."
    )
    return {
        "name": "THE_MEETS",
        "status": "PASS" if all_exact else "FAIL",
        "finding": finding,
        "method": (
            "Grow each source ball by explicit neighbor-set expansion and take "
            "the first common intersection; cross-check with a separately "
            "computed distance minimax at every placement."
        ),
        "strata": tuple(stratum_rows),
        "pass": all_exact,
    }, lookup


def compile_word(objects: tuple[object, ...]) -> tuple[Gate, ...]:
    rows = []
    for gate in objects:
        wires = tuple(map(int, gate.wires))
        if len(wires) != len(set(wires)):
            raise AssertionError(("gate repeats a wire", gate.kind, wires))
        if gate.kind == "X" and len(wires) == 1:
            rows.append((0, wires[0], 0, 0))
        elif gate.kind == "CNOT" and len(wires) == 2:
            rows.append((1, wires[0], wires[1], 0))
        elif gate.kind == "TOF" and len(wires) == 3:
            rows.append((2, wires[0], wires[1], wires[2]))
        else:
            raise AssertionError(("unsupported gate", gate.kind, wires))
    return tuple(rows)


def execute(state: int, word: tuple[Gate, ...]) -> int:
    """Independent packed-integer X/CNOT/Toffoli interpreter."""

    for kind, first, second, target in word:
        if kind == 0:
            state ^= 1 << first
        elif kind == 1:
            state ^= ((state >> first) & 1) << second
        elif kind == 2:
            state ^= (((state >> first) & 1) & ((state >> second) & 1)) << target
        else:
            raise AssertionError(("bad compiled gate kind", kind))
    return state


def bits_to_int(bits: bytes) -> int:
    return sum(bit << wire for wire, bit in enumerate(bits))


def int_to_bits(state: int) -> bytes:
    return bytes((state >> wire) & 1 for wire in range(STATE_BITS))


def build_dynamics_context(program: tuple[object, ...]) -> dict[str, object]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    rolling_bits = bytes(K.M.pack_state(banks, links))
    allocator = compile_word(tuple(K.M.global_allocator_word(FIXTURE_BANKS)))
    fixtures = {}
    fixture_rows = []
    for event in range(EVENT_COUNT):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before_bits = bytes(K.M.prepare_endpoint(rolling_bits, direction))
        before = bits_to_int(before_bits)
        fixtures[event] = before
        fixture_rows.append({
            "event": event,
            "direction": direction,
            "packed_sha256": sha256(before.to_bytes(STATE_BYTES, "little")).hexdigest(),
        })
        rolling_bits = int_to_bits(execute(before, allocator))
    macros = tuple(
        compile_word(tuple(K.mapped_macro(row))) for row in program
    )
    passed = bool(
        len(program) == 11
        and len(rolling_bits) == STATE_BITS
        and len(allocator) == 3106
        and tuple(fixtures) == tuple(range(EVENT_COUNT))
        and sum(map(len, macros)) == 3106
    )
    return {
        "fixtures": fixtures,
        "macros": macros,
        "public": {
            "fixture_rows": tuple(fixture_rows),
            "allocator_gate_count": len(allocator),
            "station_macro_gate_counts": tuple(map(len, macros)),
            "station_macro_gate_total": sum(map(len, macros)),
            "pass": passed,
        },
    }


def phase_word(
    macros: tuple[tuple[Gate, ...], ...], positions: tuple[int, ...], phase: int,
) -> tuple[Gate, ...]:
    live = {(source + phase) % len(macros) for source in positions}
    return tuple(
        gate for station, macro in enumerate(macros) if station in live for gate in macro
    )


def orbit_word(
    macros: tuple[tuple[Gate, ...], ...], positions: tuple[int, ...],
) -> tuple[Gate, ...]:
    return tuple(
        gate for phase in range(len(macros))
        for gate in phase_word(macros, positions, phase)
    )


def evolve_keys(
    context: dict[str, object], keys: tuple[Key, ...], stations: int,
    meet_lookup: dict[tuple[int, ...], tuple[int, tuple[int, ...]]] | None = None,
) -> tuple[tuple[int, ...], tuple[dict[str, object], ...]]:
    fixtures = context["fixtures"]
    macros = context["macros"]
    assert isinstance(fixtures, dict)
    assert isinstance(macros, tuple)
    placements = tuple(dict.fromkeys(key[1] for key in keys))
    orbit_cache = {placement: orbit_word(macros, placement) for placement in placements}
    phase_cache: dict[tuple[tuple[int, ...], int], tuple[Gate, ...]] = {}
    states = []
    rows = []
    for key in keys:
        _width, placement, event = key
        meet = (
            meet_lookup[placement]
            if meet_lookup is not None else wavefront_meet(placement, stations)
        )
        state = execute(fixtures[event], orbit_cache[placement])
        for phase in range(meet[0]):
            cache_key = (placement, phase)
            if cache_key not in phase_cache:
                phase_cache[cache_key] = phase_word(macros, placement, phase)
            state = execute(state, phase_cache[cache_key])
        states.append(state)
        rows.append({
            "key": key,
            "class": "ANALOG_TRIO" if placement[1] == 2 else "ANALOG_NONTRIO",
            "meet_tick": meet[0],
            "meet_centers": meet[1],
            "meet_state_sha256": sha256(state.to_bytes(STATE_BYTES, "little")).hexdigest(),
        })
    return tuple(states), tuple(rows)


def class_one_masks(states: tuple[int, ...]) -> tuple[int, ...]:
    """Transpose packed states to one bit-mask per wire and class lane."""

    columns = [0] * STATE_BITS
    for lane, state in enumerate(states):
        if state >> STATE_BITS:
            raise AssertionError(("state exceeds declared width", lane))
        remaining = state
        while remaining:
            low = remaining & -remaining
            wire = low.bit_length() - 1
            columns[wire] |= 1 << lane
            remaining ^= low
    return tuple(columns)


def cross_class_cover_masks(
    positive_one: tuple[int, ...], negative_one: tuple[int, ...],
    positive_count: int, negative_count: int,
) -> tuple[tuple[int, ...], int]:
    """For each wire, mark every cross-class state pair it distinguishes."""

    negative_full = (1 << negative_count) - 1
    covers = []
    for wire in range(STATE_BITS):
        positive_column = positive_one[wire]
        negative_column = negative_one[wire]
        cover = 0
        for lane in range(positive_count):
            block = (
                negative_column
                if not ((positive_column >> lane) & 1)
                else negative_full ^ negative_column
            )
            cover |= block << (lane * negative_count)
        covers.append(cover)
    return tuple(covers), (1 << (positive_count * negative_count)) - 1


def constant_opposite(
    positive_mask: int, positive_full: int,
    negative_mask: int, negative_full: int,
) -> bool:
    return bool(
        positive_mask in (0, positive_full)
        and negative_mask in (0, negative_full)
        and (positive_mask == positive_full) != (negative_mask == negative_full)
    )


def patterns_for_wires(
    states: tuple[int, ...], wires: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    return tuple(sorted({
        tuple((state >> wire) & 1 for wire in wires) for state in states
    }))


def exhaustive_single_pair_search(
    keys: tuple[Key, ...], states: tuple[int, ...], width: int,
) -> dict[str, object]:
    labels = tuple(key[1][1] == 2 for key in keys)
    positive_states = tuple(state for state, label in zip(states, labels) if label)
    negative_states = tuple(state for state, label in zip(states, labels) if not label)
    if not positive_states or not negative_states:
        raise AssertionError(("degenerate class split", width))
    positive_one = class_one_masks(positive_states)
    negative_one = class_one_masks(negative_states)
    covers, cross_full = cross_class_cover_masks(
        positive_one, negative_one, len(positive_states), len(negative_states)
    )
    positive_full = (1 << len(positive_states)) - 1
    negative_full = (1 << len(negative_states)) - 1

    single_tests = 0
    single_survivor_count = 0
    first_single = None
    for wire, cover in enumerate(covers):
        single_tests += 1
        if cover == cross_full:
            single_survivor_count += 1
            if first_single is None:
                first_single = wire

    pair_tests = 0
    pair_survivor_count = 0
    first_pair = None
    inequality_tests = 0
    inequality_survivor_count = 0
    first_inequality = None
    relation_names = ("bit[a] != bit[b]", "bit[a] < bit[b]", "bit[a] > bit[b]")
    for first in range(STATE_BITS - 1):
        cover_first = covers[first]
        positive_first = positive_one[first]
        negative_first = negative_one[first]
        for second in range(first + 1, STATE_BITS):
            pair_tests += 1
            if cover_first | covers[second] == cross_full:
                pair_survivor_count += 1
                if first_pair is None:
                    first_pair = (first, second)

            positive_second = positive_one[second]
            negative_second = negative_one[second]
            relation_masks = (
                (positive_first ^ positive_second,
                 negative_first ^ negative_second),
                ((positive_full ^ positive_first) & positive_second,
                 (negative_full ^ negative_first) & negative_second),
                (positive_first & (positive_full ^ positive_second),
                 negative_first & (negative_full ^ negative_second)),
            )
            for relation, (positive_mask, negative_mask) in zip(
                relation_names, relation_masks
            ):
                inequality_tests += 1
                if constant_opposite(
                    positive_mask, positive_full, negative_mask, negative_full
                ):
                    inequality_survivor_count += 1
                    if first_inequality is None:
                        first_inequality = (relation, first, second)

    total_pairs = comb(STATE_BITS, 2)
    packed_cover_bytes = (len(positive_states) * len(negative_states) + 7) // 8
    completed = bool(
        single_tests == STATE_BITS
        and pair_tests == total_pairs == 16_904_205
        and inequality_tests == 3 * total_pairs
    )
    return {
        "k": width,
        "class_rule": "sorted placement positions[1] == 2 versus complement",
        "analog_trio_key_count": len(positive_states),
        "analog_nontrio_key_count": len(negative_states),
        "cross_class_state_pair_count": len(positive_states) * len(negative_states),
        "single_tests": single_tests,
        "single_family_size": STATE_BITS,
        "single_survivor_count": single_survivor_count,
        "first_single_survivor": first_single,
        "pair_tests": pair_tests,
        "pair_family_size": total_pairs,
        "pair_survivor_count": pair_survivor_count,
        "first_pair_survivor": first_pair,
        "inequality_predicate_forms": relation_names,
        "inequality_tests": inequality_tests,
        "inequality_family_size": 3 * total_pairs,
        "inequality_survivor_count": inequality_survivor_count,
        "first_inequality_survivor": first_inequality,
        "coverage_table_sha256": sha256(b"".join(
            cover.to_bytes(packed_cover_bytes, "little") for cover in covers
        )).hexdigest(),
        "search_complete": completed,
        "pass": completed and not single_survivor_count and not pair_survivor_count,
        "private_positive_states": positive_states,
        "private_negative_states": negative_states,
    }


def no_mark_certificate(
    keys_by_k: dict[int, tuple[Key, ...]],
    states_by_k: dict[int, tuple[int, ...]],
    dynamics_public: dict[str, object],
) -> tuple[dict[str, object], dict[int, dict[str, object]]]:
    private_rows = {
        width: exhaustive_single_pair_search(
            keys_by_k[width], states_by_k[width], width
        ) for width in STRATA
    }
    rows = tuple({
        key: value for key, value in private_rows[width].items()
        if not key.startswith("private_")
    } for width in STRATA)
    passed = bool(
        dynamics_public["pass"]
        and all(row["pass"] for row in rows)
        and all(row["single_tests"] == 5815 for row in rows)
        and all(row["pair_tests"] == 16_904_205 for row in rows)
        and all(row["single_survivor_count"] == 0 for row in rows)
        and all(row["pair_survivor_count"] == 0 for row in rows)
    )
    finding = (
        "THE_NO_MARK_EXHAUSTION PASS: own packed-integer state replay and own "
        "positions[1]==2 split exhaust all 5,815 single bits and all 16,904,205 "
        "unordered bit-pairs at each of k=4 and k=5; both survivor counts are zero."
        if passed else
        f"THE_NO_MARK_EXHAUSTION FAIL: a declared-family survivor or accounting "
        f"mismatch was found: {rows}."
    )
    return {
        "name": "THE_NO_MARK_EXHAUSTION",
        "status": "PASS" if passed else "FAIL",
        "finding": finding,
        "algorithm": (
            "Transpose each class independently, encode for every wire the exact "
            "cross-class state pairs it distinguishes, and exhaustively test whether "
            "one cover or the union of two covers is universal. This does not use the "
            "primary's four-pattern collision implementation."
        ),
        "dynamics": dynamics_public,
        "strata": rows,
        "pass": passed,
    }, private_rows


def constructive_hunt_certificate(
    meet_lookup: dict[int, dict[tuple[int, ...], tuple[int, tuple[int, ...]]]],
    exhaustion_rows: dict[int, dict[str, object]],
) -> dict[str, object]:
    rows = []
    any_found = False
    for width in STRATA:
        row = exhaustion_rows[width]
        positive_states = row["private_positive_states"]
        negative_states = row["private_negative_states"]
        assert isinstance(positive_states, tuple)
        assert isinstance(negative_states, tuple)
        center_support = tuple(sorted({
            center for _tick, centers in meet_lookup[width].values()
            for center in centers
        }))
        wire_pool = tuple(sorted(set(center_support) | set(K3_MARK_BITS)))
        triples = tuple(combinations(wire_pool, 3))
        survivors = []
        for wires in triples:
            positive_patterns = patterns_for_wires(positive_states, wires)
            negative_patterns = patterns_for_wires(negative_states, wires)
            if set(positive_patterns).isdisjoint(negative_patterns):
                survivors.append({
                    "wires": wires,
                    "analog_trio_patterns": positive_patterns,
                    "analog_nontrio_patterns": negative_patterns,
                })
        inequality_found = int(row["inequality_survivor_count"]) > 0
        found = bool(survivors or inequality_found)
        any_found |= found
        rows.append({
            "k": width,
            "meet_center_support": center_support,
            "declared_center_to_wire_embedding": "C11 center c -> state bit[c]",
            "triple_wire_pool": wire_pool,
            "triple_tests": len(triples),
            "triple_family_size": comb(len(wire_pool), 3),
            "triple_survivor_count": len(survivors),
            "first_triple_survivor": survivors[0] if survivors else None,
            "inequality_predicate_forms": row["inequality_predicate_forms"],
            "inequality_tests": row["inequality_tests"],
            "inequality_survivor_count": row["inequality_survivor_count"],
            "first_inequality_survivor": row["first_inequality_survivor"],
            "verdict": "FOUND" if found else "NO_FOUND_MARK_IN_BOUNDED_EXTENSION",
            "pass": not found,
        })
    passed = not any_found
    finding = (
        "THE_CONSTRUCTIVE_HUNT PASS: for each stratum, all 286 bit-triples from "
        "{256,262} union the 11 meet-center probes and all 50,712,615 canonical "
        "pair inequalities (!=, <, >) were exhausted; no separator was found."
        if passed else
        "THE_CONSTRUCTIVE_HUNT FAIL: FOUND a k=4 or k=5 separator in the bounded "
        "triple/inequality extension; this reverses the stratification verdict."
    )
    return {
        "name": "THE_CONSTRUCTIVE_HUNT",
        "status": "PASS" if passed else "FAIL",
        "finding": finding,
        "scope": (
            "Triples use the explicitly declared native embedding of each C11 "
            "meet-center label c as bit[c], union the landed k=3 mark bits 256/262. "
            "Pair inequalities exhaust !=, <, and >; ==, <=, >= are Boolean "
            "complements and therefore have exactly the same separator status."
        ),
        "strata": tuple(rows),
        "found_strata": tuple(row["k"] for row in rows if row["verdict"] == "FOUND"),
        "pass": passed,
    }


def cross_stratum_certificate(
    context: dict[str, object], k3_keys: tuple[Key, ...], stations: int,
) -> dict[str, object]:
    states, dynamics_rows = evolve_keys(context, k3_keys, stations)
    rows = tuple({
        "key": key,
        "class": "TRIO" if key[1][1] == 2 else "NONTRIO",
        "bits_256_262": tuple((state >> wire) & 1 for wire in K3_MARK_BITS),
        "equal": ((state >> K3_MARK_BITS[0]) & 1)
            == ((state >> K3_MARK_BITS[1]) & 1),
    } for key, state in zip(k3_keys, states))
    trio_patterns = tuple(sorted({
        row["bits_256_262"] for row in rows if row["class"] == "TRIO"
    }))
    nontrio_patterns = tuple(sorted({
        row["bits_256_262"] for row in rows if row["class"] == "NONTRIO"
    }))
    passed = bool(
        len(rows) == 10
        and sum(row["class"] == "TRIO" for row in rows) == 6
        and sum(row["class"] == "NONTRIO" for row in rows) == 4
        and trio_patterns == ((0, 0), (1, 1))
        and nontrio_patterns == ((0, 1), (1, 0))
        and all(row["equal"] == (row["class"] == "TRIO") for row in rows)
    )
    return {
        "name": "THE_CROSS_STRATUM_CONSISTENCY",
        "status": "PASS" if passed else "FAIL",
        "finding": (
            "THE_CROSS_STRATUM_CONSISTENCY PASS: under the same wavefront and "
            "integer-state machinery, Cycle-849's ten-key k=3 stratum still has "
            "bit[256] == bit[262] iff TRIO (six TRIO, four NONTRIO)."
            if passed else
            f"THE_CROSS_STRATUM_CONSISTENCY FAIL: the k=3 regression rows are {rows}."
        ),
        "source": "literal K3_OPEN_KEYS parsed from blocklisted Cycle-849 primary",
        "trio_patterns": trio_patterns,
        "nontrio_patterns": nontrio_patterns,
        "rows": rows,
        "meet_state_table_sha256": digest(tuple(
            row["meet_state_sha256"] for row in dynamics_rows
        )),
        "pass": passed,
    }


def science_pass(k3_keys: tuple[Key, ...]) -> tuple[
    dict[str, dict[str, object]], dict[str, object]
]:
    program = tuple(K.interleaved_program(FIXTURE_BANKS))
    populations, keys_by_k = derive_populations(program)
    stations = int(populations["derived_station_count"])
    meets, meet_lookup = derive_meets(keys_by_k, stations)
    context = build_dynamics_context(program)
    states_by_k: dict[int, tuple[int, ...]] = {}
    dynamics_rows = []
    for width in STRATA:
        states, rows = evolve_keys(
            context, keys_by_k[width], stations, meet_lookup[width]
        )
        states_by_k[width] = states
        dynamics_rows.append({
            "k": width,
            "meet_state_count": len(states),
            "analog_trio_key_count": sum(key[1][1] == 2 for key in keys_by_k[width]),
            "analog_nontrio_key_count": sum(key[1][1] != 2 for key in keys_by_k[width]),
            "meet_state_table_sha256": sha256(b"".join(
                state.to_bytes(STATE_BYTES, "little") for state in states
            )).hexdigest(),
        })
    dynamics_public = {
        **context["public"],
        "state_engine": "own packed-integer X/CNOT/Toffoli interpreter",
        "rows": tuple(dynamics_rows),
        "pass": bool(
            context["public"]["pass"]
            and tuple(row["meet_state_count"] for row in dynamics_rows) == (220, 44)
        ),
    }
    exhaustion, private_exhaustion = no_mark_certificate(
        keys_by_k, states_by_k, dynamics_public
    )
    constructive = constructive_hunt_certificate(meet_lookup, private_exhaustion)
    cross = cross_stratum_certificate(context, k3_keys, stations)
    certificates = {
        "THE_POPULATIONS": populations,
        "THE_MEETS": meets,
        "THE_NO_MARK_EXHAUSTION": exhaustion,
        "THE_CONSTRUCTIVE_HUNT": constructive,
        "THE_CROSS_STRATUM_CONSISTENCY": cross,
    }
    private = {
        "keys_by_k": keys_by_k,
        "states_by_k": states_by_k,
        "certificate_digest_sha256": digest(certificates),
    }
    return certificates, private


def render(
    certificates: dict[str, dict[str, object]], summary: dict[str, object],
) -> str:
    lines = [
        f"{'PASS' if certificate['pass'] else 'FAIL'} {name} :: {compact(certificate)}"
        for name, certificate in certificates.items()
    ]
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append(str(summary["terminal"]))
    return "\n".join(lines) + "\n"


def stable_render(
    certificates: dict[str, dict[str, object]], summary: dict[str, object],
    controls_base: bool,
) -> str:
    controls = certificates["CONTROLS"]
    for _attempt in range(20):
        controls["pass"] = bool(
            controls_base and controls["stdout_bytes"] < STDOUT_LIMIT_BYTES
        )
        controls["status"] = "PASS" if controls["pass"] else "FAIL"
        summary["pass"] = bool(
            controls["pass"]
            and all(cert["pass"] for name, cert in certificates.items()
                    if name != "CONTROLS")
        )
        output = render(certificates, summary)
        size = len(output.encode())
        if controls["stdout_bytes"] == size and summary["stdout_bytes"] == size:
            return output
        controls["stdout_bytes"] = size
        summary["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    sources, k3_keys = source_controls()
    first_certificates, first_private = science_pass(k3_keys)
    replay_certificates, replay_private = science_pass(k3_keys)
    deterministic = bool(
        first_certificates == replay_certificates
        and first_private == replay_private
    )
    elapsed = monotonic() - started
    source_end_clean = bool(
        not any(name in sys.modules for name in BLOCKLISTED_MODULES)
        and not FIREWALL.hits
    )
    controls_base = bool(
        sources["pass"] and deterministic and source_end_clean
        and elapsed < RUNTIME_LIMIT_SECONDS
    )
    controls = {
        "name": "CONTROLS",
        "status": "PASS" if controls_base else "FAIL",
        "finding": (
            "CONTROLS PASS: all SHA-256/Git-blob pins are exact; both source "
            "primaries remained blocklisted text/AST-only; AUDIT_INPUT_PATHS is "
            "literal and worktree-relative; a full independent replay is exact; "
            "runtime is under 1400s and stdout is under 150KB."
            if controls_base else
            "CONTROLS FAIL: a SHA/blob, source firewall, literal path, determinism, "
            "runtime, or stdout condition failed."
        ),
        "sources": sources,
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "determinism": {
            "method": "full duplicate population/meet/state/exhaustion/extension/k3 replay",
            "first_digest": first_private["certificate_digest_sha256"],
            "replay_digest": replay_private["certificate_digest_sha256"],
            "full_replay_exact": deterministic,
        },
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": False,
    }
    certificates = {**first_certificates, "CONTROLS": controls}
    science_names = tuple(first_certificates)
    primary_refuted = bool(
        not first_certificates["THE_POPULATIONS"]["pass"]
        or not first_certificates["THE_MEETS"]["pass"]
        or first_certificates["THE_NO_MARK_EXHAUSTION"]["status"] == "FAIL"
        or first_certificates["THE_CONSTRUCTIVE_HUNT"]["found_strata"]
    )
    all_science_pass = all(certificates[name]["pass"] for name in science_names)
    terminal = (
        "CYCLE850_PRIMARY_REFUTED" if primary_refuted else (
            "CYCLE850_LADDER_INDEPENDENT_CHECK_PASS"
            if all_science_pass and controls_base else
            "CYCLE850_LADDER_INDEPENDENT_CHECK_FAIL"
        )
    )
    summary = {
        "cycle": 850,
        "checker": Path(__file__).name,
        "primary_refuted": primary_refuted,
        "declared_family_verdict": (
            "NO_NATIVE_MARK_K4_K5"
            if first_certificates["THE_NO_MARK_EXHAUSTION"]["pass"] else "FOUND"
        ),
        "bounded_extension_verdict": (
            "NO_FOUND_MARK"
            if first_certificates["THE_CONSTRUCTIVE_HUNT"]["pass"] else "FOUND"
        ),
        "stratification_verdict": (
            "LADDER_STRATIFIED" if not primary_refuted else "LADDER_VERDICT_REVERSED"
        ),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": False,
        "terminal": terminal,
    }
    output = stable_render(certificates, summary, controls_base)
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout limit exceeded")
    sys.stdout.write(output)
    return 0 if summary["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "pass": False,
            "exception_type": type(error).__name__,
            "exception": str(error),
            "terminal": "CYCLE850_LADDER_INDEPENDENT_CHECK_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
