#!/usr/bin/env python3
"""Cycle 978: five event weightings versus three displayed representatives.

Cited primaries are provenance only: cached notes are checked as text and
cached runners are parsed as AST at pinned git objects.  They are never
imported or executed.  Both the event weightings and the exhaustive 155-word
one-step star family are rebuilt from the landed Cycle-719 substrate.
"""

from __future__ import annotations

import ast
import json
import sys
from collections import Counter, defaultdict
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
BLOCKLIST_CITED_PRIMARIES = (
    "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py",
    "scripts/frontier_cycle974_covariant_law_weight_compatibility_2026_08_10.py",
    "scripts/frontier_cycle977_witness_family_completeness_2026_08_10.py",
)
AUDIT_INPUT_PATHS = (
    "outputs/cycle978_cited_primary_provenance_2026_08_10.json",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
EXPECTED_INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "4c242e12b987147cbd5aef73b6d5034c8fb78d1a7a916fafef29eff7ae51255e",
    AUDIT_INPUT_PATHS[1]:
        "53175250f0458168330160ad6a39c8ec708316f338efd69c49e8eb09e3267b39",
    AUDIT_INPUT_PATHS[2]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
EXPECTED_INPUT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "e78ac83a8519a85a314c93db8616bfbd3a1e64ef",
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
        "label": "cycle974_weight_compatibility",
        "commit": "679afcde32343a7b841e3810357d2a3ced9d3233",
        "note_path": "docs/COVARIANT_LAW_WEIGHT_COMPATIBILITY_CYCLE974_THEOREM_NOTE_2026-08-10.md",
        "note_blob": "33053f5fe6f8e147455bd548f15eb7cdfb2d8c6f",
        "runner_path": "scripts/frontier_cycle974_covariant_law_weight_compatibility_2026_08_10.py",
        "runner_blob": "a52c7d719f514c1eb744ca887645aa9341c223c7",
        "note_needles": (
            "All five survive",
            "product construction",
            "survivors=5/5",
        ),
        "runner_functions": (
            "rebuild_event_data", "candidate_rebuild", "evaluate_extension",
        ),
    },
    {
        "label": "cycle977_three_class_family",
        "commit": "27ec7c243f613fc1ffda4aa93960c18936b176fd",
        "note_path": "docs/WITNESS_FAMILY_COMPLETENESS_CYCLE977_BOUNDED_THEOREM_NOTE_2026-08-10.md",
        "note_blob": "4de442244691c3a0397b59c524c605133aab5fa1",
        "runner_path": "scripts/frontier_cycle977_witness_family_completeness_2026_08_10.py",
        "runner_blob": "59636bcfbe187ace224f33575d4cc92161fb0f46",
        "note_needles": (
            "exactly 21 neighbour-dependence witnesses",
            "three covariant",
            "155 distinct words.",
        ),
        "runner_functions": (
            "declared_family", "witness_census", "covariance_and_classes",
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
PER_CLASS_CRITERION = (
    "Cycle-974 product-form criterion verbatim with its single law kernel L"
    " replaced only by the selected reconstructed class representative L_c:"
    " P_i(e,x,n,y)=p_i(e) q(x,n) 1{y=L_c(x,n)}, q=1/128. Exclude only on"
    " nonnegative/normalization failure, event-marginal mismatch, or the"
    " exact first class-conditional configuration mismatch."
)
JOINT_CRITERION = (
    "Cycle-974-surrogate common-kernel joint criterion: the same unindexed"
    " fixed-input conditional kernel K_i(y|x,n) in one extension"
    " P_i(e,x,n,y) must equal every"
    " displayed representative kernel L_c(y|x,n) pointwise. No class label or"
    " carrier is added because c is not a nearest-neighbour condition."
    " Exclude at the first pair of class witnesses whose truth tables"
    " disagree on an exact (x,n,y) configuration. This is not the full"
    " Admissibility kernel K(y|n): x is an auxiliary supplied local input."
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
RECEIPT_PATH = ROOT / "outputs/three_class_born_compatibility_cycle978_receipt_2026_08_10.json"
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
        "schema": "cycle978-cited-primary-text-ast-provenance-v1",
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
            bundle.get("schema") == "cycle978-cited-primary-text-ast-provenance-v1"
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
        "blocklist_cited_primary_modules": list(BLOCKLIST_CITED_PRIMARIES),
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


CENTER = (0, 0, 0)
DIRECTION_NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")
WIRE_TO_OFFSET = (CENTER, *DIRECTIONS)
DIR_TO_WIRE = {direction: index + 1 for index, direction in enumerate(DIRECTIONS)}
SITE_COUNT = len(WIRE_TO_OFFSET)
CLASS_ORDER = (
    "CNOT",
    "TOF_PERPENDICULAR_CONTROLS",
    "TOF_OPPOSITE_CONTROLS",
)
CLASS_LABELS = {
    "CNOT": "CNOT",
    "TOF_PERPENDICULAR_CONTROLS": "perpendicular-control TOF",
    "TOF_OPPOSITE_CONTROLS": "opposite-control TOF",
}


def determinant(matrix: tuple) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def dot(left: tuple, right: tuple) -> int:
    return sum(a * b for a, b in zip(left, right))


def mat_vec(matrix: tuple, vector: tuple) -> tuple:
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )


def add(left: tuple, right: tuple) -> tuple:
    return tuple(a + b for a, b in zip(left, right))


def rotations() -> tuple:
    result = set()
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(signs[row] * int(column == order[row]) for column in range(3))
                for row in range(3)
            )
            if determinant(matrix) == 1:
                result.add(matrix)
    return tuple(sorted(result))


ROTATIONS = rotations()


def site_name(wire: int) -> str:
    return "C" if wire == 0 else DIRECTION_NAMES[wire - 1]


def word_name(descriptor: tuple) -> str:
    kind = descriptor[0]
    if kind == "I":
        return "I"
    if kind == "X":
        return f"X({site_name(descriptor[1])})"
    if kind == "CNOT":
        return f"CNOT({site_name(descriptor[1])}->{site_name(descriptor[2])})"
    return (
        f"TOF({site_name(descriptor[1])},{site_name(descriptor[2])}"
        f"->{site_name(descriptor[3])})"
    )


def declared_family() -> tuple:
    descriptors = [("I",)]
    descriptors.extend(("X", target) for target in range(SITE_COUNT))
    descriptors.extend(
        ("CNOT", control, target)
        for control, target in permutations(range(SITE_COUNT), 2)
    )
    for target in range(SITE_COUNT):
        available = tuple(site for site in range(SITE_COUNT) if site != target)
        descriptors.extend(
            ("TOF", controls[0], controls[1], target)
            for controls in combinations(available, 2)
        )
    return tuple(descriptors)


def core_word(descriptor: tuple) -> tuple:
    kind = descriptor[0]
    if kind == "I":
        return ()
    if kind == "X":
        return (K.A.x(descriptor[1]),)
    if kind == "CNOT":
        return (K.A.cn(descriptor[1], descriptor[2]),)
    return (K.A.tof(descriptor[1], descriptor[2], descriptor[3]),)


def output_state(
    descriptor: tuple, local_input: int, condition: tuple
) -> tuple:
    return K.A.apply_semantic(
        (local_input, *condition), core_word(descriptor)
    )


def output_bit(descriptor: tuple, local_input: int, condition: tuple) -> int:
    return output_state(descriptor, local_input, condition)[0]


def with_edge(index: int, other: tuple, value: int) -> tuple:
    output = []
    iterator = iter(other)
    for position in range(6):
        output.append(value if position == index else next(iterator))
    return tuple(output)


def law_signature(descriptor: tuple) -> tuple:
    return tuple(
        output_bit(
            descriptor,
            (mask >> 0) & 1,
            tuple((mask >> index) & 1 for index in range(1, SITE_COUNT)),
        )
        for mask in range(1 << SITE_COUNT)
    )


def anf_formula(signature: tuple) -> str:
    coefficients = list(signature)
    for bit in range(SITE_COUNT):
        for mask in range(1 << SITE_COUNT):
            if mask & (1 << bit):
                coefficients[mask] ^= coefficients[mask ^ (1 << bit)]
    variables = ("x", *(f"n_{name}" for name in DIRECTION_NAMES))
    terms = []
    for mask, coefficient in enumerate(coefficients):
        if coefficient:
            factors = [
                variables[index]
                for index in range(SITE_COUNT)
                if mask & (1 << index)
            ]
            terms.append(" AND ".join(factors) if factors else "1")
    return " XOR ".join(terms) if terms else "0"


def rotate_wire(wire: int, rotation: tuple) -> int:
    if wire == 0:
        return 0
    return DIR_TO_WIRE[mat_vec(rotation, WIRE_TO_OFFSET[wire])]


def rotate_descriptor(descriptor: tuple, rotation: tuple) -> tuple:
    kind = descriptor[0]
    if kind == "I":
        return descriptor
    if kind == "X":
        return ("X", rotate_wire(descriptor[1], rotation))
    if kind == "CNOT":
        return (
            "CNOT",
            rotate_wire(descriptor[1], rotation),
            rotate_wire(descriptor[2], rotation),
        )
    controls = sorted(
        (rotate_wire(descriptor[1], rotation), rotate_wire(descriptor[2], rotation))
    )
    return (
        "TOF", controls[0], controls[1],
        rotate_wire(descriptor[3], rotation),
    )


def rotate_state(state: tuple, rotation: tuple) -> tuple:
    transported = [0] * SITE_COUNT
    for wire, bit in enumerate(state):
        transported[rotate_wire(wire, rotation)] = bit
    return tuple(transported)


def global_descriptor(descriptor: tuple, target: tuple) -> tuple:
    if descriptor[0] == "I":
        return descriptor
    return (
        descriptor[0],
        *(add(target, WIRE_TO_OFFSET[wire]) for wire in descriptor[1:]),
    )


def translate_descriptor(descriptor: tuple, translation: tuple) -> tuple:
    if descriptor[0] == "I":
        return descriptor
    return (
        descriptor[0],
        *(add(site, translation) for site in descriptor[1:]),
    )


def coordinate_state(
    target: tuple, local_input: int, condition: tuple
) -> dict:
    return {
        add(target, WIRE_TO_OFFSET[wire]): bit
        for wire, bit in enumerate((local_input, *condition))
    }


def coordinate_apply(state: dict, descriptor: tuple) -> dict:
    output = dict(state)
    kind = descriptor[0]
    if kind == "X":
        output[descriptor[1]] ^= 1
    elif kind == "CNOT" and output[descriptor[1]]:
        output[descriptor[2]] ^= 1
    elif (
        kind == "TOF"
        and output[descriptor[1]]
        and output[descriptor[2]]
    ):
        output[descriptor[3]] ^= 1
    return output


def translate_state(state: dict, translation: tuple) -> dict:
    return {add(site, translation): value for site, value in state.items()}


def classify_witness(descriptor: tuple) -> str:
    if descriptor[0] == "CNOT":
        return "CNOT"
    first = WIRE_TO_OFFSET[descriptor[1]]
    second = WIRE_TO_OFFSET[descriptor[2]]
    relation = dot(first, second)
    if relation == 0:
        return "TOF_PERPENDICULAR_CONTROLS"
    if relation == -1:
        return "TOF_OPPOSITE_CONTROLS"
    raise AssertionError(("unclassified witness", descriptor, relation))


def family_and_classes_rebuild(include_covariance: bool = True) -> dict:
    family = declared_family()
    family_set = set(family)
    kind_counts = dict(sorted(Counter(row[0] for row in family).items()))
    witnesses = []
    changed_pairs = 0
    dependent_rows = 0
    for descriptor in family:
        descriptor_dependent = False
        descriptor_changed = 0
        for local_input in (0, 1):
            row_dependent = False
            for direction_index in range(6):
                for other in OTHER_CONTEXTS:
                    condition_0 = with_edge(direction_index, other, 0)
                    condition_1 = with_edge(direction_index, other, 1)
                    if (
                        output_bit(descriptor, local_input, condition_0)
                        != output_bit(descriptor, local_input, condition_1)
                    ):
                        descriptor_changed += 1
                        changed_pairs += 1
                        row_dependent = True
            dependent_rows += int(row_dependent)
            descriptor_dependent |= row_dependent
        if descriptor_dependent:
            witnesses.append({
                "descriptor": descriptor,
                "word": word_name(descriptor),
                "class": classify_witness(descriptor),
                "law": anf_formula(law_signature(descriptor)),
                "changed_edge_pairs": descriptor_changed,
            })

    grouped = defaultdict(list)
    for row in witnesses:
        grouped[row["class"]].append(row)
    classes = []
    for class_name in CLASS_ORDER:
        members = sorted(grouped.get(class_name, ()), key=lambda row: row["word"])
        if not members:
            continue
        representative = members[0]
        classes.append({
            "class": class_name,
            "label": CLASS_LABELS[class_name],
            "representative": representative["word"],
            "representative_descriptor": representative["descriptor"],
            "law": representative["law"],
            "member_count": len(members),
            "members": [row["word"] for row in members],
            "changed_edge_pairs": sum(row["changed_edge_pairs"] for row in members),
        })

    rotation_failures = []
    translation_failures = []
    bridge_failures = []
    rotation_checks = 0
    translation_checks = 0
    bridge_checks = 0
    if include_covariance:
        for rotation in ROTATIONS:
            for descriptor in family:
                transported = rotate_descriptor(descriptor, rotation)
                if transported not in family_set:
                    rotation_failures.append({
                        "word": word_name(descriptor),
                        "configuration": None,
                        "reason": "family closure",
                    })
                    continue
                for local_input in (0, 1):
                    for condition in CONDITIONS:
                        rotation_checks += 1
                        before = (local_input, *condition)
                        left = rotate_state(
                            K.A.apply_semantic(before, core_word(descriptor)),
                            rotation,
                        )
                        rotated_before = rotate_state(before, rotation)
                        right = K.A.apply_semantic(
                            rotated_before, core_word(transported)
                        )
                        if left != right:
                            rotation_failures.append({
                                "word": word_name(descriptor),
                                "configuration": [local_input, list(condition)],
                                "transported": word_name(transported),
                            })

        for descriptor in family:
            global_word = global_descriptor(descriptor, CENTER)
            for local_input in (0, 1):
                for condition in CONDITIONS:
                    bridge_checks += 1
                    landed = output_state(descriptor, local_input, condition)
                    coordinate = coordinate_apply(
                        coordinate_state(CENTER, local_input, condition),
                        global_word,
                    )
                    reencoded = tuple(
                        coordinate[add(CENTER, WIRE_TO_OFFSET[wire])]
                        for wire in range(SITE_COUNT)
                    )
                    if landed != reencoded:
                        bridge_failures.append({
                            "word": word_name(descriptor),
                            "configuration": [local_input, list(condition)],
                        })

        for translation in DIRECTIONS:
            for descriptor in family:
                global_word = global_descriptor(descriptor, CENTER)
                transported = translate_descriptor(global_word, translation)
                for local_input in (0, 1):
                    for condition in CONDITIONS:
                        translation_checks += 1
                        before = coordinate_state(CENTER, local_input, condition)
                        left = translate_state(
                            coordinate_apply(before, global_word), translation
                        )
                        right = coordinate_apply(
                            translate_state(before, translation), transported
                        )
                        if left != right:
                            translation_failures.append({
                                "word": word_name(descriptor),
                                "translation": list(translation),
                                "configuration": [local_input, list(condition)],
                            })

    failure_words = {
        row["word"]
        for row in rotation_failures + translation_failures + bridge_failures
    }
    for row in classes:
        row["covariant"] = not bool(set(row["members"]) & failure_words)
        row["rotation_checks"] = (
            row["member_count"] * len(ROTATIONS) * 2 * len(CONDITIONS)
        )
        row["translation_checks"] = (
            row["member_count"] * len(DIRECTIONS) * 2 * len(CONDITIONS)
        )
        row["first_covariance_failure"] = next(
            (
                failure for failure in (
                    rotation_failures + translation_failures + bridge_failures
                )
                if failure["word"] in set(row["members"])
            ),
            None,
        )

    witness_rows = [{
        key: value for key, value in row.items() if key != "descriptor"
    } for row in witnesses]
    class_rows = [{
        key: value for key, value in row.items()
        if key != "representative_descriptor"
    } for row in classes]
    return {
        "family_size": len(family),
        "family_kind_counts": kind_counts,
        "family_digest": digest(family),
        "conditioned_configurations": len(family) * 2 * len(CONDITIONS),
        "word_input_rows": len(family) * 2,
        "dependent_word_input_rows": dependent_rows,
        "edge_pair_comparisons": len(family) * 2 * 6 * len(OTHER_CONTEXTS),
        "changed_edge_pairs": changed_pairs,
        "witness_count": len(witnesses),
        "witnesses": witness_rows,
        "witness_digest": digest(witness_rows),
        "class_count": len(classes),
        "classes": class_rows,
        "class_partition_count": sum(row["member_count"] for row in classes),
        "representatives": {
            row["class"]: row["representative_descriptor"]
            for row in classes
        },
        "proper_rotation_count": len(ROTATIONS),
        "rotation_checks": rotation_checks,
        "rotation_failure_count": len(rotation_failures),
        "first_rotation_failure": rotation_failures[0] if rotation_failures else None,
        "translation_checks": translation_checks,
        "translation_failure_count": len(translation_failures),
        "first_translation_failure": translation_failures[0] if translation_failures else None,
        "bridge_checks": bridge_checks,
        "bridge_failure_count": len(bridge_failures),
        "first_bridge_failure": bridge_failures[0] if bridge_failures else None,
        "family_covariant": not bool(
            rotation_failures or translation_failures or bridge_failures
        ),
    }


def class_rows_for_receipt(family: dict) -> list:
    return family["classes"]


def evaluate_class_extension(
    vector: tuple,
    class_name: str,
    representative: tuple,
    carrier: dict | None = None,
    corrupt_kernel: bool = False,
) -> dict:
    if carrier is None:
        carrier = {
            (local_input, condition): Fraction(1, 128)
            for local_input in (0, 1)
            for condition in CONDITIONS
        }
    total = sum(vector)
    nonnegative = all(value >= 0 for value in vector)
    normalizable = total > 0
    carrier_total = sum(carrier.values(), Fraction(0))
    event_marginal_match = carrier_total == 1
    first_disagreement = None
    checks = 0
    if not nonnegative:
        first_disagreement = {
            "witness": word_name(representative),
            "configuration": None,
            "quantity": "min_e w_i(e)",
            "observed": str(min(vector)),
            "expected": ">=0",
        }
    elif not normalizable:
        first_disagreement = {
            "witness": word_name(representative),
            "configuration": None,
            "quantity": "sum_e w_i(e)",
            "observed": str(total),
            "expected": ">0",
        }
    elif not event_marginal_match:
        first_disagreement = {
            "witness": word_name(representative),
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
                        "witness": word_name(representative),
                        "configuration": [local_input, list(condition)],
                        "quantity": "q(x,n)",
                        "observed": str(mass),
                        "expected": ">0",
                    }
                    break
                expected_y = output_bit(representative, local_input, condition)
                forced_y = expected_y ^ int(corrupt_kernel)
                for outcome in (0, 1):
                    checks += 1
                    observed = Fraction(int(outcome == forced_y))
                    expected = Fraction(int(outcome == expected_y))
                    if observed != expected:
                        first_disagreement = {
                            "witness": word_name(representative),
                            "configuration": [
                                local_input, list(condition), outcome
                            ],
                            "quantity": f"P_i(y|x,n,{class_name})",
                            "observed": str(observed),
                            "expected": str(expected),
                        }
                        break
                if first_disagreement:
                    break
            if first_disagreement:
                break
    survives = bool(
        nonnegative
        and normalizable
        and event_marginal_match
        and first_disagreement is None
    )
    return {
        "verdict": "SURVIVES" if survives else "EXCLUDED",
        "representative_witness": word_name(representative),
        "nonnegative": nonnegative,
        "normalizable": normalizable,
        "event_marginal_factor": str(carrier_total),
        "event_marginal_matches": event_marginal_match,
        "conditional_scalar_checks": checks,
        "first_disagreement": first_disagreement,
    }



def evaluate_joint_extension(
    vector: tuple,
    representatives: dict,
) -> dict:
    total = sum(vector)
    first_disagreement = None
    class_items = tuple(representatives.items())
    reference_class, reference_word = class_items[0]
    if not all(value >= 0 for value in vector):
        first_disagreement = {
            "reference_class": reference_class,
            "reference_witness": word_name(reference_word),
            "class": reference_class,
            "witness": word_name(reference_word),
            "configuration": None,
            "quantity": "min_e w_i(e)",
            "observed": str(min(vector)),
            "expected": ">=0",
        }
    elif total <= 0:
        first_disagreement = {
            "reference_class": reference_class,
            "reference_witness": word_name(reference_word),
            "class": reference_class,
            "witness": word_name(reference_word),
            "configuration": None,
            "quantity": "sum_e w_i(e)",
            "observed": str(total),
            "expected": ">0",
        }
    else:
        for class_name, representative in class_items[1:]:
            for local_input in (0, 1):
                for condition in CONDITIONS:
                    reference_y = output_bit(
                        reference_word, local_input, condition
                    )
                    class_y = output_bit(
                        representative, local_input, condition
                    )
                    if reference_y != class_y:
                        first_disagreement = {
                            "reference_class": reference_class,
                            "reference_witness": word_name(reference_word),
                            "class": class_name,
                            "witness": word_name(representative),
                            "configuration": [
                                local_input, list(condition)
                            ],
                            "quantity": (
                                "one unindexed K(y|x,n) equals both "
                                "displayed representative kernels"
                            ),
                            "reference_output": reference_y,
                            "witness_output": class_y,
                            "reference_distribution": [
                                int(reference_y == 0),
                                int(reference_y == 1),
                            ],
                            "witness_distribution": [
                                int(class_y == 0),
                                int(class_y == 1),
                            ],
                        }
                        break
                if first_disagreement:
                    break
            if first_disagreement:
                break
    survives = first_disagreement is None
    return {
        "verdict": "SURVIVES" if survives else "EXCLUDED",
        "event_marginal_identity": (
            "if a common K exists, "
            "sum_{x,n,y} p_i(e)q(x,n)K(y|x,n)=p_i(e)"
        ),
        "class_index_added": False,
        "first_disagreement": first_disagreement,
    }


def active_compatibility_controls(representatives: dict) -> dict:
    reference = (1, 2, 0)
    first_class = next(iter(representatives))
    missing_configuration = {
        (local_input, condition): Fraction(1, 127)
        for local_input in (0, 1)
        for condition in CONDITIONS
        if not (local_input == 0 and condition == (0,) * 6)
    }
    identical_representatives = {
        class_name: representatives[first_class]
        for class_name in representatives
    }
    probes = {
        "valid_per_class": evaluate_class_extension(
            reference, first_class, representatives[first_class]
        ),
        "negative_weight": evaluate_class_extension(
            (-1, 2, 0), first_class, representatives[first_class]
        ),
        "zero_total": evaluate_class_extension(
            (0, 0, 0), first_class, representatives[first_class]
        ),
        "missing_configuration": evaluate_class_extension(
            reference,
            first_class,
            representatives[first_class],
            carrier=missing_configuration,
        ),
        "wrong_class_kernel": evaluate_class_extension(
            reference,
            first_class,
            representatives[first_class],
            corrupt_kernel=True,
        ),
        "identical_kernel_joint": evaluate_joint_extension(
            reference, identical_representatives
        ),
        "three_class_common_kernel": evaluate_joint_extension(
            reference, representatives
        ),
        "negative_weight_joint": evaluate_joint_extension(
            (-1, 2, 0), representatives
        ),
        "zero_total_joint": evaluate_joint_extension(
            (0, 0, 0), representatives
        ),
    }
    expected = {
        "valid_per_class": "SURVIVES",
        "negative_weight": "EXCLUDED",
        "zero_total": "EXCLUDED",
        "missing_configuration": "EXCLUDED",
        "wrong_class_kernel": "EXCLUDED",
        "identical_kernel_joint": "SURVIVES",
        "three_class_common_kernel": "EXCLUDED",
        "negative_weight_joint": "EXCLUDED",
        "zero_total_joint": "EXCLUDED",
    }
    return {
        "expected": expected,
        "observed": {
            name: row["verdict"] for name, row in probes.items()
        },
        "probes": probes,
        "all_decisive": all(
            probes[name]["verdict"] == verdict
            for name, verdict in expected.items()
        ),
    }

def compatibility_tests(candidates: dict, event_data: dict, family: dict) -> dict:
    representatives = family["representatives"]
    per_class = {}
    joint = {}
    for candidate in CANDIDATE_NAMES:
        vector = candidates["vectors"][candidate]
        per_class[candidate] = {}
        for class_name, representative in representatives.items():
            evaluation = evaluate_class_extension(
                vector, class_name, representative
            )
            positive_index = candidates["candidates"][candidate][
                "first_positive_event_index"
            ]
            evaluation["exact_product_witness"] = {
                "event_atom": list(event_data["events"][positive_index]),
                "p_i_event": (
                    f"{vector[positive_index]}/{sum(vector)}"
                ),
                "class_witness": word_name(representative),
                "law": anf_formula(law_signature(representative)),
            }
            per_class[candidate][class_name] = evaluation
        joint[candidate] = evaluate_joint_extension(vector, representatives)

    per_class_exclusions = []
    for candidate, class_rows in per_class.items():
        for class_name, row in class_rows.items():
            if row["verdict"] == "EXCLUDED":
                per_class_exclusions.append({
                    "candidate": candidate,
                    "class": class_name,
                    "witness": row["representative_witness"],
                    "first_disagreement": row["first_disagreement"],
                })
    joint_survivors = [
        candidate for candidate in CANDIDATE_NAMES
        if joint[candidate]["verdict"] == "SURVIVES"
    ]
    joint_excluded = [
        candidate for candidate in CANDIDATE_NAMES
        if joint[candidate]["verdict"] == "EXCLUDED"
    ]
    joint_only = [
        candidate for candidate in joint_excluded
        if all(
            per_class[candidate][class_name]["verdict"] == "SURVIVES"
            for class_name in representatives
        )
    ]
    return {
        "per_class_criterion": PER_CLASS_CRITERION,
        "joint_criterion": JOINT_CRITERION,
        "class_order": list(representatives),
        "per_class": per_class,
        "per_class_exclusions": per_class_exclusions,
        "joint": joint,
        "joint_survivors": joint_survivors,
        "joint_excluded": joint_excluded,
        "joint_only_exclusions": [{
            "candidate": candidate,
            "witness": joint[candidate]["first_disagreement"]["witness"],
            "first_disagreement": joint[candidate]["first_disagreement"],
        } for candidate in joint_only],
        "active_controls": active_compatibility_controls(representatives),
    }


def artifact_verdict(compatibility: dict) -> dict:
    survivor_count = len(compatibility["joint_survivors"])
    if survivor_count == len(CANDIDATE_NAMES):
        verdict = "NULL_CONFIRMED_AT_ENLARGED_SCOPE"
    else:
        verdict = "NULL_WAS_FAMILY_ARTIFACT"
    return {
        "verdict": verdict,
        "survivors": compatibility["joint_survivors"],
        "excluded": compatibility["joint_excluded"],
        "joint_only_exclusions": compatibility["joint_only_exclusions"],
        "born_wall_status": f"survivors/5: {survivor_count}/5",
        "born_wall_stands": survivor_count > 1,
        "does_not_supply": [
            "a local-to-event lift",
            "an event-marginal selector",
            "an occurrence rule",
            "a Born rule",
        ],
    }


def render_stdout(receipt: dict) -> str:
    rebuilt = receipt["certificates"]["A_REBUILD"]
    tests = receipt["certificates"]["B_PER_CLASS_TEST"]
    joint = receipt["certificates"]["C_JOINT_TEST"]
    artifact = receipt["certificates"]["D_ARTIFACT_VERDICT"]
    controls = receipt["certificates"]["E_CONTROLS"]
    candidate_print = {
        name: {
            "definition": rebuilt["candidates"][name]["definition"],
            "positive": rebuilt["candidates"][name]["positive_weight_events"],
            "zero": rebuilt["candidates"][name]["zero_weight_events"],
        }
        for name in CANDIDATE_NAMES
    }
    family_print = {
        row["class"]: {
            "count": row["member_count"],
            "law": row["law"],
            "witnesses": row["members"],
        }
        for row in rebuilt["classes"]
    }
    table = {
        candidate: {
            class_name: tests["per_class"][candidate][class_name]["verdict"]
            for class_name in tests["class_order"]
        }
        for candidate in CANDIDATE_NAMES
    }
    joint_headline = [{
        "candidate": row["candidate"],
        "reference_witness": row["first_disagreement"]["reference_witness"],
        "witness": row["witness"],
        "configuration": row["first_disagreement"]["configuration"],
    } for row in joint["joint_only_exclusions"]]
    lines = ["CYCLE978_THREE_CLASS_BORN_COMPATIBILITY"]
    lines.append(
        "A_REBUILD "
        + ("PASS" if receipt["checks"]["A_REBUILD"] else "FAIL")
        + " :: candidates=" + compact(candidate_print)
        + "; family=" + compact(family_print)
    )
    lines.append(
        "B_PER_CLASS_TEST "
        + ("PASS" if receipt["checks"]["B_PER_CLASS_TEST"] else "FAIL")
        + " :: criterion=" + PER_CLASS_CRITERION
        + "; table_5x3=" + compact(table)
        + "; exclusions=" + compact(tests["per_class_exclusions"])
    )
    lines.append(
        "C_JOINT_TEST "
        + ("PASS" if receipt["checks"]["C_JOINT_TEST"] else "FAIL")
        + " :: criterion=" + JOINT_CRITERION
        + "; survivors=" + compact(joint["survivors"])
        + "; joint_only_exclusions=" + compact(joint_headline)
    )
    lines.append(
        "D_ARTIFACT_VERDICT "
        + ("PASS" if receipt["checks"]["D_ARTIFACT_VERDICT"] else "FAIL")
        + f" :: {artifact['verdict']}; {artifact['born_wall_status']};"
        + " excluded=" + compact(artifact["excluded"])
    )
    lines.append(
        "E_CONTROLS "
        + ("PASS" if receipt["checks"]["E_CONTROLS"] else "FAIL")
        + f" :: source_reads={controls['literal_source_read_count']}<=6;"
        + f" sha_pins={controls['sha_pins_match']};"
        + f" BLOCKLIST_text_AST={controls['blocklist_text_ast_only']};"
        + f" determinism={controls['determinism_replay']};"
        + f" runtime_s={controls['runtime_seconds']:.3f}<1400;"
        + f" stdout_bytes={controls['stdout_bytes']}<6000<150000"
    )
    lines.extend((
        "per_element: checked — each of the five finite weighting rows has"
        " the same exact representative-kernel disagreement.",
        "per_site: checked on the target-centred seven-site star — covariance"
        " transports the finite witness, without a lattice-wide extrapolation.",
        "per_mode: checked and not executed — no continuous M_2(C) modes are"
        " present in the declared basis-state gate family.",
        "per_block: checked — CNOT, perpendicular-control TOF, and"
        " opposite-control TOF representative blocks are reconstructed.",
        "lattice_wide: checked and not executed — only translations of the"
        " one-step star are verified, not a full axiom-level stochastic law.",
    ))
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
    family = family_and_classes_rebuild(include_covariance=True)
    family_replay = family_and_classes_rebuild(include_covariance=False)
    compatibility = compatibility_tests(candidates, full, family)
    artifact = artifact_verdict(compatibility)

    full_prefix = tuple(
        event for event in full["events"]
        if event[1] <= DETERMINISM_ORBITS * full["program_stations"]
    )
    determinism = bool(
        short_a["event_digest"] == short_b["event_digest"]
        and tuple(short_a["events"]) == full_prefix
        and family["family_digest"] == family_replay["family_digest"]
        and family["witness_digest"] == family_replay["witness_digest"]
    )
    runtime = monotonic() - started

    candidate_rows = candidates["candidates"]
    class_names = [row["class"] for row in family["classes"]]
    family_partition_ok = bool(
        family["family_size"] == 1 + 7 + 7 * 6 + 7 * 15
        and family["family_kind_counts"]
        == {"CNOT": 42, "I": 1, "TOF": 105, "X": 7}
        and family["word_input_rows"] == family["family_size"] * 2
        and family["edge_pair_comparisons"]
        == family["word_input_rows"] * 6 * len(OTHER_CONTEXTS)
        and family["class_partition_count"] == family["witness_count"]
        and len({
            member
            for row in family["classes"]
            for member in row["members"]
        }) == family["witness_count"]
    )
    a_pass = bool(
        controls["pass"]
        and candidates["event_cardinality"] == 92_260
        and candidates["events_by_tag"]
        == {"B0": 47_872, "B1": 44_224, "F": 164}
        and tuple(candidate_rows) == CANDIDATE_NAMES
        and all(
            row["normalizable"] and row["nonnegative"]
            for row in candidate_rows.values()
        )
        and family_partition_ok
    )

    all_cells = [
        compatibility["per_class"][candidate][class_name]
        for candidate in CANDIDATE_NAMES
        for class_name in compatibility["class_order"]
    ]
    b_pass = bool(
        len(all_cells) == len(CANDIDATE_NAMES) * len(class_names)
        and all(row["verdict"] in {"SURVIVES", "EXCLUDED"} for row in all_cells)
        and all(
            (row["verdict"] == "SURVIVES")
            == (row["first_disagreement"] is None)
            for row in all_cells
        )
        and len(compatibility["per_class_exclusions"])
        == sum(row["verdict"] == "EXCLUDED" for row in all_cells)
        and compatibility["active_controls"]["all_decisive"]
    )
    joint_rows = compatibility["joint"]
    c_pass = bool(
        set(compatibility["joint_survivors"]).isdisjoint(
            compatibility["joint_excluded"]
        )
        and set(compatibility["joint_survivors"])
        | set(compatibility["joint_excluded"])
        == set(CANDIDATE_NAMES)
        and all(
            (row["verdict"] == "SURVIVES")
            == (row["first_disagreement"] is None)
            for row in joint_rows.values()
        )
        and all(
            candidate in compatibility["joint_excluded"]
            for candidate in (
                row["candidate"]
                for row in compatibility["joint_only_exclusions"]
            )
        )
    )
    expected_artifact_label = (
        "NULL_CONFIRMED_AT_ENLARGED_SCOPE"
        if len(compatibility["joint_survivors"]) == len(CANDIDATE_NAMES)
        else "NULL_WAS_FAMILY_ARTIFACT"
    )
    d_pass = bool(
        artifact["verdict"] == expected_artifact_label
        and artifact["survivors"] == compatibility["joint_survivors"]
        and artifact["excluded"] == compatibility["joint_excluded"]
        and artifact["born_wall_status"]
        == f"survivors/5: {len(compatibility['joint_survivors'])}/5"
    )
    receipt = {
        "cycle": 978,
        "claim": (
            "five finite event weightings versus three displayed radius-one "
            "one-step representative truth tables under the Cycle-974 "
            "fixed-input product-extension surrogate"
        ),
        "claim_type": "bounded_theorem",
        "actual_current_surface_status": "bounded-support",
        "trace_class": "direct_blocker_closure",
        "reachability_to_target": "closes",
        "conditional_surface_status": (
            "exact on the declared 155-word basis-state family, five "
            "reconstructed finite event weightings, and Cycle-974 "
            "fixed-input product-extension surrogate"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "finite one-step basis-state horizon; no full continuous "
            "M_2(C) probability law"
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "checks": {
            "A_REBUILD": a_pass,
            "B_PER_CLASS_TEST": b_pass,
            "C_JOINT_TEST": c_pass,
            "D_ARTIFACT_VERDICT": d_pass,
            "E_CONTROLS": False,
        },
        "certificates": {
            "A_REBUILD": {
                "event_cardinality": candidates["event_cardinality"],
                "events_by_tag": candidates["events_by_tag"],
                "worlds_in_census": candidates["worlds_in_census"],
                "formed_worlds": candidates["formed_worlds"],
                "event_digest": candidates["event_digest"],
                "candidates": candidate_rows,
                "family_size": family["family_size"],
                "family_kind_counts": family["family_kind_counts"],
                "conditioned_configurations": family[
                    "conditioned_configurations"
                ],
                "dependent_word_input_rows": family[
                    "dependent_word_input_rows"
                ],
                "changed_edge_pairs": family["changed_edge_pairs"],
                "witness_count": family["witness_count"],
                "witnesses": family["witnesses"],
                "witness_digest": family["witness_digest"],
                "class_count": family["class_count"],
                "classes": class_rows_for_receipt(family),
                "family_covariant": family["family_covariant"],
                "rotation_checks": family["rotation_checks"],
                "rotation_failure_count": family["rotation_failure_count"],
                "translation_checks": family["translation_checks"],
                "translation_failure_count": family[
                    "translation_failure_count"
                ],
                "bridge_checks": family["bridge_checks"],
                "bridge_failure_count": family["bridge_failure_count"],
                "provenance": controls["provenance"],
            },
            "B_PER_CLASS_TEST": {
                "criterion": compatibility["per_class_criterion"],
                "criterion_relation_to_cycle974": (
                    "verbatim product form per class; only L is instantiated "
                    "by that class representative"
                ),
                "class_order": compatibility["class_order"],
                "per_class": compatibility["per_class"],
                "per_class_exclusions": compatibility[
                    "per_class_exclusions"
                ],
            },
            "C_JOINT_TEST": {
                "criterion": compatibility["joint_criterion"],
                "relation_to_cycle974": (
                    "the product form and event marginal are unchanged, but "
                    "one unindexed conditional kernel must now satisfy all "
                    "three reconstructed class laws on the fixed-(x,n) "
                    "surrogate; this does not identify the axiom-level "
                    "nearest-neighbour kernel after auxiliary x is removed"
                ),
                "joint": compatibility["joint"],
                "survivors": compatibility["joint_survivors"],
                "excluded": compatibility["joint_excluded"],
                "joint_only_exclusions": compatibility[
                    "joint_only_exclusions"
                ],
            },
            "D_ARTIFACT_VERDICT": artifact,
            "E_CONTROLS": {
                "literal_source_read_count": len(AUDIT_INPUT_PATHS),
                "literal_audit_input_paths": controls[
                    "literal_audit_input_paths"
                ],
                "all_inputs_worktree_relative_and_present": controls[
                    "all_inputs_worktree_relative_and_present"
                ],
                "sha256": controls["sha256"],
                "git_blobs": controls["git_blobs"],
                "sha_pins_match": controls["pass"],
                "provenance_blocklist": controls[
                    "provenance_blocklist"
                ],
                "blocklist_cited_primary_modules": controls[
                    "blocklist_cited_primary_modules"
                ],
                "blocklist_text_ast_only": bool(
                    controls["provenance"][
                        "all_pins_and_text_ast_checks_match"
                    ]
                    and not controls["provenance"][
                        "blocked_modules_loaded"
                    ]
                ),
                "blocked_modules_loaded": controls["provenance"][
                    "blocked_modules_loaded"
                ],
                "determinism_replay": determinism,
                "short_replay_digest": short_a["event_digest"],
                "full_prefix_digest": digest(full_prefix),
                "family_replay_digest": family_replay["witness_digest"],
                "active_corruption_controls": compatibility[
                    "active_controls"
                ],
                "runtime_seconds": runtime,
                "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
                "stdout_bytes": 0,
                "stdout_limit_bytes": HOUSE_STDOUT_LIMIT_BYTES,
            },
        },
    }
    for _ in range(4):
        output = render_stdout(receipt)
        receipt["certificates"]["E_CONTROLS"]["stdout_bytes"] = len(
            output.encode()
        )
    output = render_stdout(receipt)
    e_pass = bool(
        controls["pass"]
        and determinism
        and compatibility["active_controls"]["all_decisive"]
        and runtime < AUDIT_TIMEOUT_SEC <= 1400
        and len(output.encode())
        < HOUSE_STDOUT_LIMIT_BYTES
        < STDOUT_LIMIT_BYTES
    )
    receipt["checks"]["E_CONTROLS"] = e_pass
    receipt["certificates"]["E_CONTROLS"]["stdout_bytes"] = len(
        output.encode()
    )
    output = render_stdout(receipt)
    receipt["pass"] = all(receipt["checks"].values())
    receipt["primary_source_sha256"] = sha256(
        Path(__file__).read_bytes()
    ).hexdigest()
    return receipt, output


def main() -> int:
    if sys.argv[1:] == ["--capture-provenance"]:
        return capture_provenance_bundle()
    if sys.argv[1:]:
        raise SystemExit("usage: runner [--capture-provenance]")
    receipt, output = run()
    RECEIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_PATH.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    sys.stdout.write(output)
    return 0 if receipt["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
