#!/usr/bin/env python3
"""Cycle 974: covariant neighbour law versus five event weightings.

The cited Cycle-878/970/972 primaries are provenance only: their notes are
read as text and their runners are parsed as AST at pinned git objects.  They
are never imported or executed.  The event data are rebuilt from the landed
Cycle-719 substrate, and the radius-one XOR law is independently enumerated
on that same landed substrate.
"""

from __future__ import annotations

import ast
import json
import sys
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K  # noqa: E402


AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
HOUSE_STDOUT_LIMIT_BYTES = 6000
AUDIT_INPUT_PATHS = (
    "outputs/cycle974_cited_primary_provenance_2026_08_10.json",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
EXPECTED_INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "978302583fc5e58b883f1970c73a335fc4d9366984773875ea2b6dd969ad538c",
    AUDIT_INPUT_PATHS[1]:
        "53175250f0458168330160ad6a39c8ec708316f338efd69c49e8eb09e3267b39",
    AUDIT_INPUT_PATHS[2]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
EXPECTED_INPUT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "d2b4197f3417ec85e0fcb148db89146b742fafe3",
    AUDIT_INPUT_PATHS[1]: "2f5fdd26898f62c17fcabc846761f7785c2eadb1",
    AUDIT_INPUT_PATHS[2]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
}

PROVENANCE = (
    {
        "label": "cycle878_event_weightings",
        "commit": "f655c945318231538ad7a5cc8956dc384115f8ea",
        "note_path": "docs/EVENT_SPACE_GROUNDWORK_CYCLE878_SUPPORT_NOTE_2026-07-28.md",
        "note_blob": "17c07f4d6d3dc07c81828827f25ab575dc7b722d",
        "runner_path": "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py",
        "runner_blob": "769f65e51ea2e896af750e92592a421464c3c0e1",
        "note_needles": (
            "92,260 realized record-write events",
            "Five record-native weightings are FINITE-MEASURE CANDIDATES",
            "a derived lift of that local law through Record",
        ),
        "runner_functions": ("derive_census", "composed_scan", "build_candidates"),
    },
    {
        "label": "cycle970_inter_site_gate",
        "commit": "6fd0de0a288d212a4a6ce3fdd4dc9019f30dbbad",
        "note_path": "docs/INTER_SITE_GATE_CYCLE970_BOUNDED_THEOREM_NOTE_2026-08-09.md",
        "note_blob": "f7b788d8076e7864bc5dbcbb33cb9e49554e494a",
        "runner_path": "scripts/frontier_cycle970_inter_site_gate_2026_08_09.py",
        "runner_blob": "4670bcb9d83cfc039f1336398c6a4aa4af014f7c",
        "note_needles": (
            "same supplied local state `x=0`",
            "D(y | n=0):              [1,0]",
            "uniform marginal remains 0/10",
        ),
        "runner_functions": ("point_distribution", "minimal_gate_attempt"),
    },
    {
        "label": "cycle972_covariant_dependence_law",
        "commit": "3826925e019c0e1966a9b85110a397db2c61d33f",
        "note_path": "docs/COVARIANT_DEPENDENCE_LAW_CYCLE972_BOUNDED_THEOREM_NOTE_2026-08-09.md",
        "note_blob": "e328562ec0ff3b80acef65c490bb5903cc3e8438",
        "runner_path": "scripts/frontier_cycle972_covariant_dependence_law_2026_08_09.py",
        "runner_blob": "ab497ae52f74bc8e8c6cc6eb5888bfaf9f119f15",
        "note_needles": (
            "y = x XOR n_d",
            "61,440",
            "3,840",
        ),
        "runner_functions": (
            "state_resolved_census", "uniform_target_input_census",
            "covariance_and_orbits",
        ),
    },
)

CANDIDATE_NAMES = (
    "M1_COUNTING",
    "M2_PER_WORLD_UNIFORM",
    "M3_OCCUPATION_WEIGHTED",
    "M4_FORMATION_LIFETIME",
    "M5_FORMATION_MOMENT",
)
CANDIDATE_DEFINITIONS = {
    "M1_COUNTING": "w(e)=1",
    "M2_PER_WORLD_UNIFORM": "world score a(w)=1; uniform within each event-bearing world",
    "M3_OCCUPATION_WEIGHTED": "a(w)=clean-dwell occupation count; uniform within world",
    "M4_FORMATION_LIFETIME": "a(w)=boundaries-formation_moment(w)+1 if formed, else 0; uniform within world",
    "M5_FORMATION_MOMENT": "a(w)=formation_moment(w) if formed, else 0; uniform within world",
}
COMPATIBILITY_CRITERION = (
    "existential joint-extension criterion: a normalized event weighting p_i"
    " survives iff there exists P_i(e,x,n,y) with event marginal p_i and"
    " conditional P_i(y|x,n)=1{y=x XOR n_d} on every fixed-input radius-one"
    " configuration; mechanically use P_i=p_i(e)*q(x,n)*1{y=x XOR n_d},"
    " q=1/128.  Exclude only on nonnegative/normalization failure, event-"
    "marginal mismatch, or a first conditional configuration mismatch."
)

FIXTURE_BANKS = 2
MIN_SOURCES = 2
MAX_SOURCES = 5
HORIZON = 16_384
REGISTER_CAP = 64
DETERMINISM_ORBITS = 192
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
CONDITIONS = tuple(product((0, 1), repeat=6))
OTHER_CONTEXTS = tuple(product((0, 1), repeat=5))
RECEIPT_PATH = ROOT / "outputs/covariant_law_weight_compatibility_cycle974_receipt_2026_08_10.json"
PROVENANCE_BUNDLE_PATH = ROOT / AUDIT_INPUT_PATHS[0]


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode()
    return __import__("hashlib").sha1(header + payload).hexdigest()


def lcm(left: int, right: int) -> int:
    return left * right // gcd(left, right)


def ast_literal_assignment(tree: ast.Module, name: str):
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise KeyError(name)


def capture_provenance_bundle() -> int:
    """One-shot maintainer action; normal certification never needs git objects."""
    import subprocess

    entries = []
    for item in PROVENANCE:
        note_ref_blob = subprocess.check_output(
            ["git", "rev-parse", f'{item["commit"]}:{item["note_path"]}'],
            text=True,
        ).strip()
        runner_ref_blob = subprocess.check_output(
            ["git", "rev-parse", f'{item["commit"]}:{item["runner_path"]}'],
            text=True,
        ).strip()
        if note_ref_blob != item["note_blob"] or runner_ref_blob != item["runner_blob"]:
            raise AssertionError((item["label"], note_ref_blob, runner_ref_blob))
        entries.append({
            "label": item["label"],
            "commit": item["commit"],
            "note_path": item["note_path"],
            "note_blob": item["note_blob"],
            "runner_path": item["runner_path"],
            "runner_blob": item["runner_blob"],
            "note_text": subprocess.check_output(
                ["git", "cat-file", "-p", item["note_blob"]], text=True
            ),
            "runner_source": subprocess.check_output(
                ["git", "cat-file", "-p", item["runner_blob"]], text=True
            ),
        })
    payload = {
        "schema": "cycle974-cited-primary-text-ast-provenance-v1",
        "capture_rule": "commit:path resolved to the declared blob before payload capture",
        "entries": entries,
    }
    PROVENANCE_BUNDLE_PATH.parent.mkdir(parents=True, exist_ok=True)
    PROVENANCE_BUNDLE_PATH.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(PROVENANCE_BUNDLE_PATH.relative_to(ROOT))
    return 0


def provenance_controls() -> dict:
    bundle = json.loads(PROVENANCE_BUNDLE_PATH.read_text(encoding="utf-8"))
    by_label = {entry["label"]: entry for entry in bundle["entries"]}
    rows = []
    for item in PROVENANCE:
        entry = by_label[item["label"]]
        note = entry["note_text"].encode("utf-8")
        runner = entry["runner_source"].encode("utf-8")
        note_blob = git_blob(note)
        runner_blob = git_blob(runner)
        note_text = entry["note_text"]
        tree = ast.parse(entry["runner_source"], filename=item["runner_path"])
        functions = {
            node.name for node in tree.body if isinstance(node, ast.FunctionDef)
        }
        row = {
            "label": item["label"],
            "commit": item["commit"],
            "note_path": item["note_path"],
            "note_blob": note_blob,
            "runner_path": item["runner_path"],
            "runner_blob": runner_blob,
            "note_text_needles_match": all(
                needle in note_text for needle in item["note_needles"]
            ),
            "runner_ast_functions_match": all(
                name in functions for name in item["runner_functions"]
            ),
            "text_ast_only": True,
        }
        if item["label"] == "cycle878_event_weightings":
            row["ast_candidate_names"] = list(
                ast_literal_assignment(tree, "CANDIDATE_NAMES")
            )
            row["candidate_names_match"] = tuple(row["ast_candidate_names"]) == CANDIDATE_NAMES
        row["pass"] = bool(
            entry["commit"] == item["commit"]
            and entry["note_path"] == item["note_path"]
            and entry["runner_path"] == item["runner_path"]
            and entry["note_blob"] == item["note_blob"] == note_blob
            and entry["runner_blob"] == item["runner_blob"] == runner_blob
            and row["note_text_needles_match"]
            and row["runner_ast_functions_match"]
            and row.get("candidate_names_match", True)
        )
        rows.append(row)
    return {
        "bundle_schema": bundle.get("schema"),
        "bundle_entry_count": len(bundle["entries"]),
        "rows": rows,
        "all_pins_and_text_ast_checks_match": bool(
            bundle.get("schema") == "cycle974-cited-primary-text-ast-provenance-v1"
            and len(bundle["entries"]) == len(PROVENANCE)
            and set(by_label) == {item["label"] for item in PROVENANCE}
            and all(row["pass"] for row in rows)
        ),
        "blocked_modules_loaded": sorted(
            name for name in sys.modules
            if any(item["runner_path"].removesuffix(".py").endswith(name) for item in PROVENANCE)
        ),
    }


def input_controls() -> dict:
    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    literal_paths = ast_literal_assignment(own_tree, "AUDIT_INPUT_PATHS")
    sha_rows = {}
    blob_rows = {}
    for rel in AUDIT_INPUT_PATHS:
        payload = (ROOT / rel).read_bytes()
        sha_rows[rel] = sha256(payload).hexdigest()
        blob_rows[rel] = git_blob(payload)
    provenance = provenance_controls()
    result = {
        "literal_audit_input_paths": list(literal_paths),
        "all_inputs_worktree_relative_and_present": all(
            not Path(rel).is_absolute() and (ROOT / rel).is_file()
            for rel in literal_paths
        ),
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "provenance_blocklist": [
            entry
            for item in PROVENANCE
            for entry in (
                f'{item["commit"]}:{item["note_path"]} (text)',
                f'{item["commit"]}:{item["runner_path"]} (AST)',
            )
        ],
        "provenance": provenance,
    }
    result["pass"] = bool(
        tuple(literal_paths) == AUDIT_INPUT_PATHS
        and result["all_inputs_worktree_relative_and_present"]
        and sha_rows == EXPECTED_INPUT_SHA256
        and blob_rows == EXPECTED_INPUT_BLOBS
        and provenance["all_pins_and_text_ast_checks_match"]
        and not provenance["blocked_modules_loaded"]
    )
    return result


def pairwise_separated(positions: tuple[int, ...], stations: int) -> bool:
    occupied = set(positions)
    return all((station + 1) % stations not in occupied for station in occupied)


def derive_event_seeds(program: tuple) -> tuple:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        if after != K.A.apply_semantic(before, allocator):
            raise AssertionError(("allocator semantic mismatch", event))
        if rail_a != (1,) + (0,) * (len(program) - 1) or any(rail_b):
            raise AssertionError(("allocator rail mismatch", event))
        if len(trace) != len(program):
            raise AssertionError(("allocator trace mismatch", event))
        rows.append((event, before))
        state = after
    return tuple(rows)


def derive_census() -> tuple:
    program = K.interleaved_program(FIXTURE_BANKS)
    stations = len(program)
    seeds = derive_event_seeds(program)
    worlds = tuple(sorted(
        (count, event, positions)
        for count in range(MIN_SOURCES, MAX_SOURCES + 1)
        for positions in combinations(range(stations), count)
        if pairwise_separated(positions, stations)
        for event, _state in seeds
    ))
    return program, seeds, worlds


def watched_registers() -> tuple:
    return (
        ("POINTER", K.A.POINTER), ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U), ("DIRECTION_OK", K.A.DIRECTION_OK),
        *((f"FRESH_{i}", wire) for i, wire in enumerate(K.A.FRESH)),
        *((f"ZERO_WORK_{i}", wire) for i, wire in enumerate(K.A.ZERO_WORK)),
        ("TOKEN_OK", K.A.TOKEN_OK),
    )


def dirty_partition() -> tuple:
    banks0, links0 = K.B.chain_genesis(FIXTURE_BANKS)
    zero_banks = tuple(tuple(0 for _ in bank) for bank in banks0)
    zero_links = tuple(tuple(0 for _ in link) for link in links0)
    baseline = K.M.pack_state(zero_banks, zero_links)
    per_bank = [set() for _ in zero_banks]
    for bank_index in range(len(zero_banks)):
        for _name, wire in watched_registers():
            changed = [list(bank) for bank in zero_banks]
            changed[bank_index][wire] = 1
            marked = K.M.pack_state(tuple(map(tuple, changed)), zero_links)
            diffs = [index for index, pair in enumerate(zip(baseline, marked)) if pair[0] != pair[1]]
            if len(diffs) != 1:
                raise AssertionError(("bank marker", bank_index, wire, diffs))
            per_bank[bank_index].add(diffs[0])
    link_wires = set()
    for link_index, link in enumerate(zero_links):
        for wire in range(len(link)):
            changed = [list(row) for row in zero_links]
            changed[link_index][wire] = 1
            marked = K.M.pack_state(zero_banks, tuple(map(tuple, changed)))
            diffs = [index for index, pair in enumerate(zip(baseline, marked)) if pair[0] != pair[1]]
            if len(diffs) != 1:
                raise AssertionError(("link marker", link_index, wire, diffs))
            link_wires.add(diffs[0])
    return tuple(tuple(sorted(row)) for row in per_bank), tuple(sorted(link_wires)), K.R3.X.SOURCE_POINTER


def initial_states(program: tuple, seeds: tuple, worlds: tuple) -> tuple:
    by_event = dict(seeds)
    states = []
    for _count, event, positions in worlds:
        after, rail_a, rail_b, _trace = K.run_orbit(
            by_event[event], program, token_positions=positions
        )
        expected = tuple(int(station in positions) for station in range(len(program)))
        if rail_a != expected or any(rail_b):
            raise AssertionError(("initial state rail", event, positions))
        states.append(after)
    return tuple(states)


def pack_lanes(states: tuple) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def compile_masked_gate(gate: object, mask: int) -> tuple:
    if gate.kind == "X":
        return 0, gate.wires[0], 0, 0, mask
    if gate.kind == "CNOT":
        return 1, gate.wires[0], gate.wires[1], 0, mask
    if gate.kind == "TOF":
        return 2, gate.wires[0], gate.wires[1], gate.wires[2], mask
    raise ValueError(gate)


def compiled_schedule(program: tuple, worlds: tuple) -> tuple:
    schedules = []
    stations = len(program)
    for step in range(stations):
        schedule = []
        for station, row in enumerate(program):
            mask = sum(
                1 << lane
                for lane, (_count, _event, positions) in enumerate(worlds)
                if (station - step) % stations in positions
            )
            if mask:
                schedule.extend(compile_masked_gate(gate, mask) for gate in K.mapped_macro(row))
        source = ["def apply(columns):"]
        for kind, left, right, third, mask in schedule:
            if kind == 0:
                source.append(f" columns[{left}] ^= {mask}")
            elif kind == 1:
                source.append(f" columns[{right}] ^= columns[{left}] & {mask}")
            else:
                source.append(f" columns[{third}] ^= columns[{left}] & columns[{right}] & {mask}")
        namespace = {}
        exec("\n".join(source), {"__builtins__": {}}, namespace)
        schedules.append(namespace["apply"])
    return tuple(schedules)


def clean_mask(columns: list[int], dirty: tuple[int, ...], universe: int) -> int:
    combined = 0
    for wire in dirty:
        combined |= columns[wire]
    return universe & ~combined


def lanes(mask: int):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def rebuild_event_data(orbits: int) -> dict:
    program, seeds, worlds = derive_census()
    states = initial_states(program, seeds, worlds)
    columns = pack_lanes(states)
    schedule = compiled_schedule(program, worlds)
    per_bank, link_wires, source_pointer = dirty_partition()
    global_dirty = tuple(sorted(set(per_bank[0]) | set(per_bank[1]) | set(link_wires) | {source_pointer}))
    bank_dirty = tuple(tuple(sorted(row)) for row in per_bank)
    universe = (1 << len(worlds)) - 1
    events = []
    occupation = [0] * len(worlds)
    formed = {}
    ordinals = [[0, 0] for _ in worlds]

    global_0 = clean_mask(columns, global_dirty, universe)
    bank_0 = [clean_mask(columns, bank_dirty[index], universe) for index in (0, 1)]
    for lane in lanes(global_0):
        occupation[lane] += 1
        formed[lane] = 0
        events.append((lane, 0, "F", 0))
    for bank in (0, 1):
        for lane in lanes(bank_0[bank]):
            pass
    previous_bank = bank_0
    boundary = 0
    beyond_cap = 0
    for _orbit in range(1, orbits + 1):
        for apply_chunk in schedule:
            apply_chunk(columns)
            boundary += 1
            globally_clean = clean_mask(columns, global_dirty, universe)
            for lane in lanes(globally_clean):
                occupation[lane] += 1
                if lane not in formed:
                    formed[lane] = boundary
                    events.append((lane, boundary, "F", 0))
            for bank in (0, 1):
                current = clean_mask(columns, bank_dirty[bank], universe)
                for lane in lanes(current & ~previous_bank[bank]):
                    ordinal = ordinals[lane][bank]
                    if ordinal < REGISTER_CAP:
                        events.append((lane, boundary, f"B{bank}", ordinal))
                    else:
                        beyond_cap += 1
                    ordinals[lane][bank] += 1
                previous_bank[bank] = current
    atoms = [(world, tag, ordinal) for world, _moment, tag, ordinal in events]
    return {
        "program_stations": len(program),
        "worlds": worlds,
        "events": tuple(events),
        "event_digest": digest(events),
        "event_atoms_are_singletons": len(atoms) == len(set(atoms)),
        "occupation": tuple(occupation),
        "formed": formed,
        "boundaries": boundary,
        "beyond_cap": beyond_cap,
        "initial_global_clean_lanes": global_0.bit_count(),
    }


def candidate_rebuild(event_data: dict) -> dict:
    events = event_data["events"]
    per_world = Counter(event[0] for event in events)
    supported = tuple(sorted(per_world))
    common = 1
    for count in set(per_world.values()):
        common = lcm(common, count)

    def world_weighted(score):
        return tuple(
            score(event[0]) * (common // per_world[event[0]])
            for event in events
        )

    boundaries = event_data["boundaries"]
    formed = event_data["formed"]
    occupation = event_data["occupation"]
    vectors = {
        "M1_COUNTING": (1,) * len(events),
        "M2_PER_WORLD_UNIFORM": world_weighted(lambda world: 1),
        "M3_OCCUPATION_WEIGHTED": world_weighted(lambda world: occupation[world]),
        "M4_FORMATION_LIFETIME": world_weighted(
            lambda world: boundaries - formed[world] + 1 if world in formed else 0
        ),
        "M5_FORMATION_MOMENT": world_weighted(
            lambda world: formed[world] if world in formed else 0
        ),
    }
    rows = {}
    for name in CANDIDATE_NAMES:
        vector = vectors[name]
        total = sum(vector)
        rows[name] = {
            "definition": CANDIDATE_DEFINITIONS[name],
            "integer_numerator_total": total,
            "common_within_world_denominator": 1 if name == "M1_COUNTING" else common,
            "normalizable": total > 0,
            "nonnegative": all(value >= 0 for value in vector),
            "zero_weight_events": sum(value == 0 for value in vector),
            "positive_weight_events": sum(value > 0 for value in vector),
            "normalized_weight_digest": digest({
                "numerators": vector,
                "total": total,
            }),
            "first_positive_event_index": next(index for index, value in enumerate(vector) if value > 0),
        }
    return {
        "event_cardinality": len(events),
        "events_by_tag": dict(sorted(Counter(event[2] for event in events).items())),
        "worlds_in_census": len(event_data["worlds"]),
        "worlds_with_events": len(supported),
        "formed_worlds": len(formed),
        "per_world_event_count_range": [min(per_world.values()), max(per_world.values())],
        "common_within_world_denominator": common,
        "event_atom_singletons": event_data["event_atoms_are_singletons"],
        "event_digest": event_data["event_digest"],
        "candidates": rows,
        "vectors": vectors,
    }


def determinant(matrix: tuple) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat_vec(matrix: tuple, vector: tuple) -> tuple:
    return tuple(sum(matrix[row][column] * vector[column] for column in range(3)) for row in range(3))


def add(left: tuple, right: tuple) -> tuple:
    return tuple(a + b for a, b in zip(left, right))


def rotations() -> tuple:
    result = set()
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(tuple(signs[row] * int(column == order[row]) for column in range(3)) for row in range(3))
            if determinant(matrix) == 1:
                result.add(matrix)
    return tuple(sorted(result))


def declared_family() -> tuple:
    words = [("I",), ("X", "C")]
    words.extend(("X", direction) for direction in DIRECTIONS)
    words.extend(("CNOT", "C", direction) for direction in DIRECTIONS)
    words.extend(("CNOT", direction, "C") for direction in DIRECTIONS)
    return tuple(words)


def wire(site: object) -> int:
    return 0 if site == "C" else DIRECTIONS.index(site) + 1


def core_word(descriptor: tuple) -> tuple:
    if descriptor[0] == "I":
        return ()
    if descriptor[0] == "X":
        return (K.A.x(wire(descriptor[1])),)
    return (K.A.cn(wire(descriptor[1]), wire(descriptor[2])),)


def point_distribution(descriptor: tuple, local_input: int, condition: tuple) -> tuple:
    after = K.A.apply_semantic((local_input, *condition), core_word(descriptor))
    return int(after[0] == 0), int(after[0] == 1)


def with_edge(index: int, other: tuple, value: int) -> tuple:
    output = []
    iterator = iter(other)
    for position in range(6):
        output.append(value if position == index else next(iterator))
    return tuple(output)


def rotate_site(site: object, rotation: tuple):
    return site if site == "C" else mat_vec(rotation, site)


def rotate_descriptor(descriptor: tuple, rotation: tuple) -> tuple:
    if descriptor[0] == "I":
        return descriptor
    if descriptor[0] == "X":
        return "X", rotate_site(descriptor[1], rotation)
    return "CNOT", rotate_site(descriptor[1], rotation), rotate_site(descriptor[2], rotation)


def rotate_condition(condition: tuple, rotation: tuple) -> tuple:
    transported = {
        mat_vec(rotation, direction): condition[index]
        for index, direction in enumerate(DIRECTIONS)
    }
    return tuple(transported[direction] for direction in DIRECTIONS)


def global_descriptor(descriptor: tuple, target: tuple) -> tuple:
    def global_site(site):
        return target if site == "C" else add(target, site)
    if descriptor[0] == "I":
        return descriptor
    if descriptor[0] == "X":
        return "X", global_site(descriptor[1])
    return "CNOT", global_site(descriptor[1]), global_site(descriptor[2])


def coordinate_state(target: tuple, local_input: int, condition: tuple) -> dict:
    state = {target: local_input}
    state.update({add(target, direction): condition[index] for index, direction in enumerate(DIRECTIONS)})
    return state


def coordinate_apply(state: dict, descriptor: tuple) -> dict:
    output = dict(state)
    if descriptor[0] == "X":
        output[descriptor[1]] ^= 1
    elif descriptor[0] == "CNOT":
        output[descriptor[2]] ^= output[descriptor[1]]
    return output


def translate_state(state: dict, translation: tuple) -> dict:
    return {add(site, translation): value for site, value in state.items()}


def translate_descriptor(descriptor: tuple, translation: tuple) -> tuple:
    if descriptor[0] == "I":
        return descriptor
    if descriptor[0] == "X":
        return "X", add(descriptor[1], translation)
    return "CNOT", add(descriptor[1], translation), add(descriptor[2], translation)


def dependence_law_rebuild() -> dict:
    family = declared_family()
    witness_words = []
    dependent_rows = 0
    changed_pairs = 0
    xor_failures = []
    for descriptor in family:
        descriptor_dependent = False
        for local_input in (0, 1):
            row_dependent = False
            for direction_index, direction in enumerate(DIRECTIONS):
                direction_dependent = False
                for other in OTHER_CONTEXTS:
                    condition_0 = with_edge(direction_index, other, 0)
                    condition_1 = with_edge(direction_index, other, 1)
                    if point_distribution(descriptor, local_input, condition_0) != point_distribution(descriptor, local_input, condition_1):
                        changed_pairs += 1
                        direction_dependent = True
                row_dependent |= direction_dependent
            dependent_rows += int(row_dependent)
            descriptor_dependent |= row_dependent
        if descriptor_dependent:
            witness_words.append(descriptor)
            incoming = descriptor[1]
            direction_index = DIRECTIONS.index(incoming)
            for local_input in (0, 1):
                for condition in CONDITIONS:
                    observed = point_distribution(descriptor, local_input, condition)
                    expected_y = local_input ^ condition[direction_index]
                    expected = (int(expected_y == 0), int(expected_y == 1))
                    if observed != expected:
                        xor_failures.append((descriptor, local_input, condition, observed, expected))

    rotation_rows = rotations()
    rotation_failures = []
    rotation_checks = 0
    for rotation in rotation_rows:
        for descriptor in family:
            transported = rotate_descriptor(descriptor, rotation)
            for local_input in (0, 1):
                for condition in CONDITIONS:
                    rotation_checks += 1
                    if point_distribution(descriptor, local_input, condition) != point_distribution(transported, local_input, rotate_condition(condition, rotation)):
                        rotation_failures.append((descriptor, local_input, condition))

    translation_failures = []
    translation_checks = 0
    target = (0, 0, 0)
    for translation in DIRECTIONS:
        for descriptor in family:
            local_global = global_descriptor(descriptor, target)
            transported_word = translate_descriptor(local_global, translation)
            for local_input in (0, 1):
                for condition in CONDITIONS:
                    translation_checks += 1
                    before = coordinate_state(target, local_input, condition)
                    left = translate_state(coordinate_apply(before, local_global), translation)
                    right = coordinate_apply(translate_state(before, translation), transported_word)
                    if left != right:
                        translation_failures.append((descriptor, translation, local_input, condition))

    marginal_changed_pairs = 0
    for descriptor in family:
        for direction_index in range(6):
            for other in OTHER_CONTEXTS:
                distributions = []
                for edge_value in (0, 1):
                    condition = with_edge(direction_index, other, edge_value)
                    distributions.append(tuple(
                        sum(Fraction(point_distribution(descriptor, x, condition)[y], 2) for x in (0, 1))
                        for y in (0, 1)
                    ))
                marginal_changed_pairs += distributions[0] != distributions[1]

    direction_orbit = {mat_vec(rotation, DIRECTIONS[0]) for rotation in rotation_rows}
    canonical_0 = (0,) * 6
    canonical_1 = (1, 0, 0, 0, 0, 0)
    return {
        "family_words": len(family),
        "neighbour_conditions": len(CONDITIONS),
        "witness_word_count": len(witness_words),
        "dependent_word_input_rows": dependent_rows,
        "changed_edge_pairs": changed_pairs,
        "xor_truth_table_comparisons": len(witness_words) * 2 * len(CONDITIONS),
        "xor_failures": xor_failures,
        "law": "y=x XOR n_d",
        "rotation_count": len(rotation_rows),
        "rotation_semantic_comparisons": rotation_checks,
        "rotation_failures": rotation_failures,
        "translation_semantic_comparisons": translation_checks,
        "translation_failures": translation_failures,
        "word_law_class_count": int(len(direction_orbit) == len(DIRECTIONS)),
        "state_resolved_class_count": 2 if len(direction_orbit) == len(DIRECTIONS) else None,
        "uniform_target_input_edge_pairs": len(family) * 6 * len(OTHER_CONTEXTS),
        "uniform_target_input_changed_pairs": marginal_changed_pairs,
        "canonical_pair": {
            "fixed_target_input": 0,
            "condition_n_d_0": list(canonical_0),
            "condition_n_d_1": list(canonical_1),
            "distribution_n_d_0": list(point_distribution(("CNOT", DIRECTIONS[0], "C"), 0, canonical_0)),
            "distribution_n_d_1": list(point_distribution(("CNOT", DIRECTIONS[0], "C"), 0, canonical_1)),
        },
    }


def evaluate_extension(
    vector: tuple,
    carrier: dict | None = None,
    use_xnor_kernel: bool = False,
) -> dict:
    """Mechanically test the declared product extension, including its failures."""
    if carrier is None:
        carrier = {
            (local_input, condition): Fraction(1, 128)
            for local_input in (0, 1) for condition in CONDITIONS
        }
    total = sum(vector)
    nonnegative = all(value >= 0 for value in vector)
    normalizable = total > 0
    carrier_total = sum(carrier.values(), Fraction(0))
    event_marginal_match = carrier_total == 1
    first_disagreement = None
    conditional_checks = 0
    if not nonnegative:
        first_disagreement = {
            "configuration": None,
            "quantity": "min_e w_i(e)",
            "observed": str(min(vector)),
            "expected": ">=0",
        }
    elif not normalizable:
        first_disagreement = {
            "configuration": None,
            "quantity": "sum_e w_i(e)",
            "observed": str(total),
            "expected": ">0",
        }
    elif not event_marginal_match:
        first_disagreement = {
            "configuration": None,
            "quantity": "sum_{x,n} q(x,n)",
            "observed": str(carrier_total),
            "expected": "1",
        }
    else:
        for local_input in (0, 1):
            for condition in CONDITIONS:
                mass = carrier.get((local_input, condition), Fraction(0))
                if mass <= 0:
                    first_disagreement = {
                        "configuration": [local_input, list(condition)],
                        "quantity": "q(x,n)",
                        "observed": str(mass),
                        "expected": ">0",
                    }
                    break
                forced_y = local_input ^ condition[0] ^ int(use_xnor_kernel)
                for outcome in (0, 1):
                    conditional_checks += 1
                    numerator = mass if outcome == forced_y else Fraction(0)
                    observed = numerator / mass
                    expected = Fraction(int(outcome == (local_input ^ condition[0])))
                    if observed != expected:
                        first_disagreement = {
                            "configuration": [local_input, list(condition), outcome],
                            "quantity": "P_i(y|x,n)",
                            "observed": str(observed),
                            "expected": str(expected),
                        }
                        break
                if first_disagreement:
                    break
            if first_disagreement:
                break
    survives = bool(
        nonnegative and normalizable and event_marginal_match
        and first_disagreement is None
    )
    return {
        "verdict": "SURVIVES" if survives else "EXCLUDED",
        "nonnegative": nonnegative,
        "normalizable": normalizable,
        "event_marginal_factor": str(carrier_total),
        "event_marginal_matches": event_marginal_match,
        "conditional_scalar_checks": conditional_checks,
        "first_disagreement": first_disagreement,
    }


def active_compatibility_controls() -> dict:
    reference = (1, 2, 0)
    missing_configuration_carrier = {
        (local_input, condition): Fraction(1, 127)
        for local_input in (0, 1) for condition in CONDITIONS
        if not (local_input == 0 and condition == (0,) * 6)
    }
    probes = {
        "valid_xor": evaluate_extension(reference),
        "negative_weight": evaluate_extension((-1, 2, 0)),
        "zero_total": evaluate_extension((0, 0, 0)),
        "missing_configuration": evaluate_extension(
            reference, carrier=missing_configuration_carrier
        ),
        "xnor_instead_of_xor": evaluate_extension(reference, use_xnor_kernel=True),
    }
    expected = {
        "valid_xor": "SURVIVES",
        "negative_weight": "EXCLUDED",
        "zero_total": "EXCLUDED",
        "missing_configuration": "EXCLUDED",
        "xnor_instead_of_xor": "EXCLUDED",
    }
    return {
        "expected_verdicts": expected,
        "probes": probes,
        "all_controls_decisive": all(
            probes[name]["verdict"] == verdict for name, verdict in expected.items()
        ),
    }


def compatibility_test(candidates: dict, event_data: dict, law: dict) -> dict:
    rows = {}
    vectors = candidates["vectors"]
    events = event_data["events"]
    q = Fraction(1, 2 * len(CONDITIONS))
    for name in CANDIDATE_NAMES:
        vector = vectors[name]
        total = sum(vector)
        evaluation = evaluate_extension(vector)
        positive_index = candidates["candidates"][name]["first_positive_event_index"]
        atom_numerator = vector[positive_index]
        rows[name] = {
            **evaluation,
            "event_marginal_identity": "sum_{x,n,y} P_i(e,x,n,y)=p_i(e)",
            "conditional_identity": "P_i(y|x,n)=1{y=x XOR n_d}",
            "exact_extension_witness": {
                "event_atom": list(events[positive_index]),
                "p_i_event": f"{atom_numerator}/{total}",
                "canonical_configuration_pair": law["canonical_pair"],
                "joint_mass_at_forced_outcome_per_configuration": str(Fraction(atom_numerator, total) * q),
            },
        }
    survivors = tuple(name for name in CANDIDATE_NAMES if rows[name]["verdict"] == "SURVIVES")
    excluded = tuple(name for name in CANDIDATE_NAMES if rows[name]["verdict"] == "EXCLUDED")
    return {
        "criterion": COMPATIBILITY_CRITERION,
        "auxiliary_conditioning_carrier": "q(x,n)=1/128; arbitrary strictly positive q gives the same conditional kernel and event marginal",
        "rows": rows,
        "survivors": survivors,
        "excluded": excluded,
        "survivor_count": len(survivors),
        "excluded_count": len(excluded),
        "active_controls": active_compatibility_controls(),
    }


def selection_status(compatibility: dict) -> dict:
    survivor_count = compatibility["survivor_count"]
    excluded_count = compatibility["excluded_count"]
    status = {
        "survivors": compatibility["survivors"],
        "excluded": compatibility["excluded"],
        "freedom_before": len(CANDIDATE_NAMES),
        "freedom_after": survivor_count,
        "absolute_reduction": len(CANDIDATE_NAMES) - survivor_count,
        "fractional_reduction": str(Fraction(len(CANDIDATE_NAMES) - survivor_count, len(CANDIDATE_NAMES))),
        "born_wall_stands": survivor_count > 1,
        "does_not_supply": (
            "a local-to-event lift", "an event-marginal selector",
            "an occurrence rule", "a Born rule",
        ),
    }
    if survivor_count > 1:
        status.update({
            "case": "RESIDUAL_FREEDOM",
            "selected_weighting": None,
            "selection_premises": (),
            "refutation_target": None,
        })
    elif survivor_count == 1:
        status.update({
            "case": "SINGLETON_SELECTION",
            "selected_weighting": compatibility["survivors"][0],
            "selection_premises": (
                "the five reconstructed finite event weightings are exhaustive candidates",
                "the existential joint-extension criterion",
                "strictly positive normalized q(x,n)",
                "the certified XOR conditional on every radius-one configuration",
            ),
            "refutation_target": None,
        })
    else:
        status.update({
            "case": "NO_SURVIVOR_REFUTATION",
            "selected_weighting": None,
            "selection_premises": (),
            "refutation_target": "the declared compatibility criterion or a landed input row",
        })
    status["partition_count"] = survivor_count + excluded_count
    return status


def render_stdout(receipt: dict) -> str:
    candidates = receipt["certificates"]["A_REBUILD"]["candidate_rows"]
    compatibility = receipt["certificates"]["B_COMPATIBILITY_TEST"]
    selection = receipt["certificates"]["C_SELECTION_STATUS"]
    lines = ["CYCLE974_COVARIANT_LAW_WEIGHT_COMPATIBILITY"]
    lines.append(
        "A_REBUILD " + ("PASS" if receipt["checks"]["A_REBUILD"] else "FAIL")
        + f" :: events={receipt['certificates']['A_REBUILD']['event_cardinality']};"
        + " candidates=" + compact({name: {
            "definition": candidates[name]["definition"],
            "zeros": candidates[name]["zero_weight_events"],
            "positive": candidates[name]["positive_weight_events"],
        } for name in CANDIDATE_NAMES})
        + "; dependence=" + compact(receipt["certificates"]["A_REBUILD"]["dependence_law"])
    )
    lines.append(
        "B_COMPATIBILITY_TEST " + ("PASS" if receipt["checks"]["B_COMPATIBILITY_TEST"] else "FAIL")
        + " :: criterion=" + COMPATIBILITY_CRITERION
        + "; verdicts=" + compact({name: compatibility["rows"][name]["verdict"] for name in CANDIDATE_NAMES})
        + "; witness_pair=" + compact(receipt["certificates"]["A_REBUILD"]["dependence_law"]["canonical_pair"])
    )
    lines.append(
        "C_SELECTION_STATUS " + ("PASS" if receipt["checks"]["C_SELECTION_STATUS"] else "FAIL")
        + f" :: case={selection['case']}; five_to={selection['freedom_after']};"
        + f" excluded={compatibility['excluded_count']};"
        + f" reduction={selection['absolute_reduction']}/5"
        + f" ({20 * selection['absolute_reduction']}%);"
        + f" wall_stands={selection['born_wall_stands']};"
        + f" selected={selection['selected_weighting']};"
        + f" refutation_target={selection['refutation_target']}"
    )
    controls = receipt["certificates"]["D_CONTROLS"]
    lines.append(
        "D_CONTROLS " + ("PASS" if receipt["checks"]["D_CONTROLS"] else "FAIL")
        + f" :: sha_pins={controls['sha_pins_match']}; BLOCKLIST_text_AST_only={controls['blocklist_text_ast_only']};"
        + f" determinism={controls['determinism_replay']}; runtime_s={controls['runtime_seconds']:.3f}<1400;"
        + f" stdout_bytes={controls['stdout_bytes']}<6000<150000"
    )
    passed = sum(receipt["checks"].values())
    failed = len(receipt["checks"]) - passed
    lines.append(f"TOTAL: PASS={passed} FAIL={failed}")
    return "\n".join(lines) + "\n"


def run() -> tuple[dict, str]:
    started = monotonic()
    controls = input_controls()
    full = rebuild_event_data(HORIZON)
    short_a = rebuild_event_data(DETERMINISM_ORBITS)
    short_b = rebuild_event_data(DETERMINISM_ORBITS)
    candidates = candidate_rebuild(full)
    law = dependence_law_rebuild()
    compatibility = compatibility_test(candidates, full, law)
    selection = selection_status(compatibility)
    full_prefix = tuple(
        event for event in full["events"]
        if event[1] <= DETERMINISM_ORBITS * full["program_stations"]
    )
    determinism_replay = bool(
        short_a["event_digest"] == short_b["event_digest"]
        and tuple(short_a["events"]) == full_prefix
    )
    runtime = monotonic() - started

    a_pass = bool(
        controls["pass"]
        and candidates["event_cardinality"] == 92_260
        and candidates["events_by_tag"] == {"B0": 47_872, "B1": 44_224, "F": 164}
        and candidates["worlds_in_census"] == 748
        and candidates["formed_worlds"] == 164
        and candidates["event_atom_singletons"]
        and tuple(candidates["candidates"]) == CANDIDATE_NAMES
        and all(row["normalizable"] and row["nonnegative"] for row in candidates["candidates"].values())
        and law["family_words"] == 20
        and law["witness_word_count"] == 6
        and law["dependent_word_input_rows"] == 12
        and law["changed_edge_pairs"] == 384
        and law["xor_truth_table_comparisons"] == 768
        and not law["xor_failures"]
        and law["rotation_semantic_comparisons"] == 61_440
        and not law["rotation_failures"]
        and law["translation_semantic_comparisons"] == 15_360
        and not law["translation_failures"]
        and law["word_law_class_count"] == 1
        and law["state_resolved_class_count"] == 2
        and law["uniform_target_input_edge_pairs"] == 3_840
        and law["uniform_target_input_changed_pairs"] == 0
    )
    b_pass = bool(
        compatibility["active_controls"]["all_controls_decisive"]
        and tuple(compatibility["rows"]) == CANDIDATE_NAMES
        and set(compatibility["survivors"]).isdisjoint(compatibility["excluded"])
        and set(compatibility["survivors"]) | set(compatibility["excluded"]) == set(CANDIDATE_NAMES)
        and all(
            all(
                row[key] == evaluate_extension(candidates["vectors"][name])[key]
                for key in (
                    "verdict", "nonnegative", "normalizable",
                    "event_marginal_factor", "event_marginal_matches",
                    "conditional_scalar_checks", "first_disagreement",
                )
            )
            for name, row in compatibility["rows"].items()
        )
    )
    c_pass = bool(
        selection["partition_count"] == len(CANDIDATE_NAMES)
        and selection["freedom_before"] == len(CANDIDATE_NAMES)
        and selection["freedom_after"] == compatibility["survivor_count"]
        and selection["absolute_reduction"] == len(CANDIDATE_NAMES) - compatibility["survivor_count"]
        and selection["fractional_reduction"] == str(Fraction(selection["absolute_reduction"], len(CANDIDATE_NAMES)))
        and (
            (
                selection["case"] == "RESIDUAL_FREEDOM"
                and selection["freedom_after"] > 1
                and selection["born_wall_stands"]
                and selection["selected_weighting"] is None
                and selection["refutation_target"] is None
            )
            or (
                selection["case"] == "SINGLETON_SELECTION"
                and selection["freedom_after"] == 1
                and not selection["born_wall_stands"]
                and selection["selected_weighting"] == compatibility["survivors"][0]
                and bool(selection["selection_premises"])
                and selection["refutation_target"] is None
            )
            or (
                selection["case"] == "NO_SURVIVOR_REFUTATION"
                and selection["freedom_after"] == 0
                and not selection["born_wall_stands"]
                and selection["selected_weighting"] is None
                and bool(selection["refutation_target"])
            )
        )
    )
    d_pass = bool(
        controls["pass"] and determinism_replay and runtime < AUDIT_TIMEOUT_SEC
    )
    receipt = {
        "cycle": 974,
        "claim": "covariant nearest-neighbour XOR law compatibility with the five finite event weightings",
        "checks": {
            "A_REBUILD": a_pass,
            "B_COMPATIBILITY_TEST": b_pass,
            "C_SELECTION_STATUS": c_pass,
            "D_CONTROLS": d_pass,
        },
        "certificates": {
            "A_REBUILD": {
                "event_cardinality": candidates["event_cardinality"],
                "events_by_tag": candidates["events_by_tag"],
                "worlds_in_census": candidates["worlds_in_census"],
                "formed_worlds": candidates["formed_worlds"],
                "per_world_event_count_range": candidates["per_world_event_count_range"],
                "event_digest": candidates["event_digest"],
                "candidate_rows": candidates["candidates"],
                "dependence_law": law,
                "provenance": controls["provenance"],
            },
            "B_COMPATIBILITY_TEST": compatibility,
            "C_SELECTION_STATUS": selection,
            "D_CONTROLS": {
                "literal_audit_input_paths": controls["literal_audit_input_paths"],
                "sha256": controls["sha256"],
                "git_blobs": controls["git_blobs"],
                "sha_pins_match": controls["sha256"] == EXPECTED_INPUT_SHA256 and controls["git_blobs"] == EXPECTED_INPUT_BLOBS,
                "provenance_blocklist": controls["provenance_blocklist"],
                "blocklist_text_ast_only": controls["provenance"]["all_pins_and_text_ast_checks_match"],
                "blocked_modules_loaded": controls["provenance"]["blocked_modules_loaded"],
                "determinism_replay": determinism_replay,
                "short_replay_digest": short_a["event_digest"],
                "full_prefix_digest": digest(full_prefix),
                "runtime_seconds": runtime,
                "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
                "stdout_bytes": 0,
                "stdout_limit_bytes": HOUSE_STDOUT_LIMIT_BYTES,
            },
        },
    }
    for _ in range(4):
        output = render_stdout(receipt)
        receipt["certificates"]["D_CONTROLS"]["stdout_bytes"] = len(output.encode())
    output = render_stdout(receipt)
    stdout_ok = len(output.encode()) < HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
    receipt["checks"]["D_CONTROLS"] &= stdout_ok
    receipt["certificates"]["D_CONTROLS"]["stdout_bytes"] = len(output.encode())
    output = render_stdout(receipt)
    receipt["pass"] = all(receipt["checks"].values())
    receipt["primary_source_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    return receipt, output


def main() -> int:
    if sys.argv[1:] == ["--capture-provenance"]:
        return capture_provenance_bundle()
    if sys.argv[1:]:
        raise SystemExit("usage: runner [--capture-provenance]")
    receipt, output = run()
    RECEIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sys.stdout.write(output)
    return 0 if receipt["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
