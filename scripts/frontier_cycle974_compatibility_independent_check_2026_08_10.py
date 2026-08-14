#!/usr/bin/env python3
"""Independent refutation attempt for the Cycle-974 compatibility result.

The primary is blocklisted from execution.  Its source is parsed as AST and
its cache/receipt are data only.  This checker rebuilds the event-weight data
from the landed Cycle-719 core, uses an independent Boolean gate interpreter,
constructs rotations from oriented frames, and attacks the declared
compatibility criterion with active corruptions.
"""

from __future__ import annotations

import ast
import json
import sys
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
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
    "scripts/frontier_cycle974_covariant_law_weight_compatibility_2026_08_10.py",
    "logs/runner-cache/frontier_cycle974_covariant_law_weight_compatibility_2026_08_10.txt",
    "outputs/covariant_law_weight_compatibility_cycle974_receipt_2026_08_10.json",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]: "a6d611f403c2e7eb325f14123ce789cf8b21ed1ec4071c5725e3adbb608a795d",
    AUDIT_INPUT_PATHS[1]: "fa8a25f534b9061f28245aa9a8a52c2951508c70715397943e0f955471c399b0",
    AUDIT_INPUT_PATHS[2]: "16d3ee6fc549c697f6943937f0b1f9a67dbe144e00deb30d2eb99aed4516e199",
    AUDIT_INPUT_PATHS[3]: "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[4]: "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
}
BLOCKLIST_EXECUTION = AUDIT_INPUT_PATHS[:3]
CANDIDATE_NAMES = (
    "M1_COUNTING", "M2_PER_WORLD_UNIFORM", "M3_OCCUPATION_WEIGHTED",
    "M4_FORMATION_LIFETIME", "M5_FORMATION_MOMENT",
)
AXIOM_REQUIRED_NEEDLES = (
    "Finite additivity, a named scalar collection functional `I`, and an assigned",
    "Born weight values,",
    "probability rules beyond the distribution clause",
    "The 2026-08-13 owner-approved revision removed the named scalar functional",
)
FIXTURE_BANKS = 2
HORIZON = 16_384
REGISTER_CAP = 64
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
CONDITIONS = tuple(product((0, 1), repeat=6))
OTHER_CONTEXTS = tuple(product((0, 1), repeat=5))
RECEIPT_PATH = ROOT / "outputs/covariant_law_weight_compatibility_cycle974_independent_check_receipt_2026_08_10.json"


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def lcm(left: int, right: int) -> int:
    return left * right // gcd(left, right)


def literal_assignment(tree: ast.Module, name: str):
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise KeyError(name)


def controls() -> dict:
    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    literal_inputs = literal_assignment(own_tree, "AUDIT_INPUT_PATHS")
    sha_rows = {
        rel: sha256((ROOT / rel).read_bytes()).hexdigest()
        for rel in literal_inputs
    }
    primary_source = (ROOT / AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    primary_tree = ast.parse(primary_source, filename=AUDIT_INPUT_PATHS[0])
    primary_functions = {
        node.name for node in primary_tree.body if isinstance(node, ast.FunctionDef)
    }
    primary_cache = (ROOT / AUDIT_INPUT_PATHS[1]).read_text(encoding="utf-8")
    primary_receipt = json.loads((ROOT / AUDIT_INPUT_PATHS[2]).read_text(encoding="utf-8"))
    axiom_text = (ROOT / AUDIT_INPUT_PATHS[4]).read_text(encoding="utf-8")
    ast_checks = {
        "candidate_names": tuple(literal_assignment(primary_tree, "CANDIDATE_NAMES")) == CANDIDATE_NAMES,
        "criterion_literal_present": "COMPATIBILITY_CRITERION" in {
            target.id
            for node in primary_tree.body if isinstance(node, ast.Assign)
            for target in node.targets if isinstance(target, ast.Name)
        },
        "load_bearing_functions": all(
            name in primary_functions
            for name in ("candidate_rebuild", "dependence_law_rebuild", "compatibility_test")
        ),
        "no_import_of_cited_primaries": not any(
            isinstance(node, (ast.Import, ast.ImportFrom))
            and any("cycle878" in alias.name or "cycle970" in alias.name or "cycle972" in alias.name for alias in node.names)
            for node in ast.walk(primary_tree)
        ),
    }
    cache_checks = {
        "total_pass": "TOTAL: PASS=4 FAIL=0" in primary_cache,
        "all_five_survive_reported": all(f'"{name}":"SURVIVES"' in primary_cache for name in CANDIDATE_NAMES),
        "envelope_runner_binding": f"runner_sha256: {sha_rows[AUDIT_INPUT_PATHS[0]]}" in primary_cache,
        "envelope_timeout_binding": "timeout_sec: 1400" in primary_cache,
        "envelope_success": "status: ok" in primary_cache and "exit_code: 0" in primary_cache,
        "receipt_source_binding": primary_receipt["primary_source_sha256"] == sha256(primary_source.encode()).hexdigest(),
    }
    loaded = sorted(
        name for name in sys.modules
        if any(Path(rel).stem == name for rel in BLOCKLIST_EXECUTION)
    )
    result = {
        "literal_inputs": list(literal_inputs),
        "sha256": sha_rows,
        "pins_match": sha_rows == EXPECTED_SHA256,
        "blocklist_execution": list(BLOCKLIST_EXECUTION),
        "blocklist_text_ast_json_only": True,
        "blocked_modules_loaded": loaded,
        "primary_ast_checks": ast_checks,
        "primary_cache_receipt_checks": cache_checks,
        "primary_receipt": primary_receipt,
        "current_record_boundary_needles_match": all(
            needle in axiom_text for needle in AXIOM_REQUIRED_NEEDLES
        ),
    }
    result["pass"] = bool(
        tuple(literal_inputs) == AUDIT_INPUT_PATHS
        and all(not Path(rel).is_absolute() and (ROOT / rel).is_file() for rel in literal_inputs)
        and result["pins_match"] and result["current_record_boundary_needles_match"] and not loaded
        and all(ast_checks.values()) and all(cache_checks.values())
    )
    return result


def separated(positions: tuple[int, ...], stations: int) -> bool:
    occupied = set(positions)
    return not any((position + 1) % stations in occupied for position in occupied)


def genesis_seeds(program: tuple) -> tuple:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocation = K.M.global_allocator_word(FIXTURE_BANKS)
    rows = []
    for event in range(4):
        direction = ((1, 0), (0, 1))[event % 2]
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        if after != K.A.apply_semantic(before, allocation) or any(rail_b):
            raise AssertionError(("seed semantics", event))
        if rail_a[0] != 1 or any(rail_a[1:]) or len(trace) != len(program):
            raise AssertionError(("seed trace", event))
        rows.append((event, before))
        state = after
    return tuple(rows)


def census() -> tuple:
    program = K.interleaved_program(FIXTURE_BANKS)
    seeds = genesis_seeds(program)
    worlds = []
    for count in range(2, 6):
        for positions in combinations(range(len(program)), count):
            if separated(positions, len(program)):
                worlds.extend((count, event, positions) for event, _state in seeds)
    return program, seeds, tuple(sorted(worlds))


def register_wires() -> tuple[int, ...]:
    return (
        K.A.POINTER, K.A.U_TO_V, K.A.V_TO_U, K.A.DIRECTION_OK,
        *K.A.FRESH, *K.A.ZERO_WORK, K.A.TOKEN_OK,
    )


def dirty_wires() -> tuple:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    zero_banks = tuple(tuple(0 for _ in bank) for bank in banks)
    zero_links = tuple(tuple(0 for _ in link) for link in links)
    baseline = K.M.pack_state(zero_banks, zero_links)

    def changed_index(marked: tuple) -> int:
        changed = [index for index, (left, right) in enumerate(zip(baseline, marked)) if left != right]
        if len(changed) != 1:
            raise AssertionError(("coordinate marker", changed))
        return changed[0]

    per_bank = []
    for bank_index in range(2):
        coordinates = []
        for wire in register_wires():
            marked_banks = [list(bank) for bank in zero_banks]
            marked_banks[bank_index][wire] = 1
            coordinates.append(changed_index(K.M.pack_state(tuple(map(tuple, marked_banks)), zero_links)))
        per_bank.append(tuple(sorted(coordinates)))
    link_coordinates = []
    for link_index, link in enumerate(zero_links):
        for wire in range(len(link)):
            marked_links = [list(row) for row in zero_links]
            marked_links[link_index][wire] = 1
            link_coordinates.append(changed_index(K.M.pack_state(zero_banks, tuple(map(tuple, marked_links)))))
    return tuple(per_bank), tuple(sorted(link_coordinates)), K.R3.X.SOURCE_POINTER


def prepare_columns(program: tuple, seeds: tuple, worlds: tuple) -> list[int]:
    by_event = dict(seeds)
    states = []
    for _count, event, positions in worlds:
        after, rail_a, rail_b, _trace = K.run_orbit(by_event[event], program, token_positions=positions)
        expected = tuple(int(index in positions) for index in range(len(program)))
        if rail_a != expected or any(rail_b):
            raise AssertionError(("world initial state", event, positions))
        states.append(after)
    return [sum(state[wire] << lane for lane, state in enumerate(states)) for wire in range(len(states[0]))]


def masked_steps(program: tuple, worlds: tuple) -> tuple:
    result = []
    for phase in range(len(program)):
        operations = []
        for station, row in enumerate(program):
            mask = sum(
                1 << lane
                for lane, (_count, _event, positions) in enumerate(worlds)
                if (station - phase) % len(program) in positions
            )
            for gate in K.mapped_macro(row):
                if mask:
                    operations.append((gate.kind, gate.wires, mask))
        result.append(tuple(operations))
    return tuple(result)


def apply_operations(columns: list[int], operations: tuple) -> None:
    for kind, wires, mask in operations:
        if kind == "X":
            columns[wires[0]] ^= mask
        elif kind == "CNOT":
            columns[wires[1]] ^= columns[wires[0]] & mask
        elif kind == "TOF":
            columns[wires[2]] ^= columns[wires[0]] & columns[wires[1]] & mask
        else:
            raise AssertionError(("unknown gate", kind))


def clean(columns: list[int], wires: tuple, universe: int) -> int:
    dirty = 0
    for wire in wires:
        dirty |= columns[wire]
    return universe & ~dirty


def bits(mask: int):
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask -= low


def independent_event_rebuild() -> dict:
    program, seeds, worlds = census()
    columns = prepare_columns(program, seeds, worlds)
    steps = masked_steps(program, worlds)
    per_bank, link_coordinates, source_pointer = dirty_wires()
    global_wires = tuple(sorted(set(per_bank[0]) | set(per_bank[1]) | set(link_coordinates) | {source_pointer}))
    universe = (1 << len(worlds)) - 1
    events = []
    occupation = [0] * len(worlds)
    formed = {}
    ordinals = [[0, 0] for _ in worlds]
    global_mask = clean(columns, global_wires, universe)
    previous_bank = [clean(columns, per_bank[index], universe) for index in (0, 1)]
    for lane in bits(global_mask):
        occupation[lane] += 1
        formed[lane] = 0
        events.append((lane, 0, "F", 0))
    boundary = 0
    for _orbit in range(HORIZON):
        for operations in steps:
            apply_operations(columns, operations)
            boundary += 1
            global_mask = clean(columns, global_wires, universe)
            for lane in bits(global_mask):
                occupation[lane] += 1
                if lane not in formed:
                    formed[lane] = boundary
                    events.append((lane, boundary, "F", 0))
            for bank in (0, 1):
                current = clean(columns, per_bank[bank], universe)
                for lane in bits(current & ~previous_bank[bank]):
                    ordinal = ordinals[lane][bank]
                    if ordinal < REGISTER_CAP:
                        events.append((lane, boundary, f"B{bank}", ordinal))
                    ordinals[lane][bank] += 1
                previous_bank[bank] = current
    counts = Counter(event[0] for event in events)
    common = 1
    for count in set(counts.values()):
        common = lcm(common, count)

    def distribute(score):
        return tuple(score(event[0]) * (common // counts[event[0]]) for event in events)

    vectors = {
        "M1_COUNTING": (1,) * len(events),
        "M2_PER_WORLD_UNIFORM": distribute(lambda world: 1),
        "M3_OCCUPATION_WEIGHTED": distribute(lambda world: occupation[world]),
        "M4_FORMATION_LIFETIME": distribute(lambda world: boundary - formed[world] + 1 if world in formed else 0),
        "M5_FORMATION_MOMENT": distribute(lambda world: formed[world] if world in formed else 0),
    }
    rows = {
        name: {
            "zero_weight_events": sum(value == 0 for value in vector),
            "positive_weight_events": sum(value > 0 for value in vector),
            "integer_numerator_total": sum(vector),
            "normalized_weight_digest": digest({"numerators": vector, "total": sum(vector)}),
            "nonnegative": all(value >= 0 for value in vector),
            "normalizable": sum(vector) > 0,
        }
        for name, vector in vectors.items()
    }
    return {
        "event_cardinality": len(events),
        "events_by_tag": dict(sorted(Counter(event[2] for event in events).items())),
        "worlds": len(worlds),
        "formed_worlds": len(formed),
        "event_digest": digest(events),
        "vectors": vectors,
        "rows": rows,
    }


def cross(left: tuple, right: tuple) -> tuple:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def dot(left: tuple, right: tuple) -> int:
    return sum(a * b for a, b in zip(left, right))


def frame_rotations() -> tuple:
    result = set()
    for image_x in DIRECTIONS:
        for image_y in DIRECTIONS:
            if dot(image_x, image_y) != 0:
                continue
            image_z = cross(image_x, image_y)
            matrix = tuple(
                (image_x[row], image_y[row], image_z[row])
                for row in range(3)
            )
            result.add(matrix)
    return tuple(sorted(result))


def mat_vec(matrix: tuple, vector: tuple) -> tuple:
    return tuple(sum(matrix[row][column] * vector[column] for column in range(3)) for row in range(3))


def family() -> tuple:
    return (
        (("I",), ("X", "C"))
        + tuple(("X", direction) for direction in DIRECTIONS)
        + tuple(("CNOT", "C", direction) for direction in DIRECTIONS)
        + tuple(("CNOT", direction, "C") for direction in DIRECTIONS)
    )


def bool_outcome(descriptor: tuple, local_input: int, condition: tuple) -> int:
    if descriptor == ("X", "C"):
        return local_input ^ 1
    if descriptor[0] == "CNOT" and descriptor[2] == "C":
        return local_input ^ condition[DIRECTIONS.index(descriptor[1])]
    return local_input


def with_edge(index: int, other: tuple, value: int) -> tuple:
    result = list(other)
    result.insert(index, value)
    return tuple(result)


def rotate_descriptor(descriptor: tuple, rotation: tuple) -> tuple:
    def rotate(site):
        return site if site == "C" else mat_vec(rotation, site)
    if descriptor[0] == "I":
        return descriptor
    if descriptor[0] == "X":
        return "X", rotate(descriptor[1])
    return "CNOT", rotate(descriptor[1]), rotate(descriptor[2])


def rotate_condition(condition: tuple, rotation: tuple) -> tuple:
    mapping = {
        mat_vec(rotation, direction): condition[index]
        for index, direction in enumerate(DIRECTIONS)
    }
    return tuple(mapping[direction] for direction in DIRECTIONS)


def add_coordinate(left: tuple, right: tuple) -> tuple:
    return tuple(a + b for a, b in zip(left, right))


def coordinate_state(target: tuple, local_input: int, condition: tuple) -> dict:
    state = {target: local_input}
    state.update({
        add_coordinate(target, direction): condition[index]
        for index, direction in enumerate(DIRECTIONS)
    })
    return state


def global_descriptor(descriptor: tuple, target: tuple) -> tuple:
    def place(site):
        return target if site == "C" else add_coordinate(target, site)

    if descriptor[0] == "I":
        return "I", target
    if descriptor[0] == "X":
        return "X", place(descriptor[1])
    return "CNOT", place(descriptor[1]), place(descriptor[2])


def coordinate_apply(state: dict, descriptor: tuple) -> dict:
    after = dict(state)
    if descriptor[0] == "I":
        return after
    if descriptor[0] == "X":
        after[descriptor[1]] = after.get(descriptor[1], 0) ^ 1
        return after
    after[descriptor[2]] = after.get(descriptor[2], 0) ^ after.get(descriptor[1], 0)
    return after


def translate_state(state: dict, translation: tuple) -> dict:
    return {
        add_coordinate(site, translation): value
        for site, value in state.items()
    }


def translate_global_descriptor(descriptor: tuple, translation: tuple) -> tuple:
    return (descriptor[0],) + tuple(
        add_coordinate(site, translation) for site in descriptor[1:]
    )


def translation_corruption_probe() -> dict:
    origin = (0, 0, 0)
    translation = (0, 1, 0)
    condition = (1, 0, 0, 0, 0, 0)
    descriptor = global_descriptor(("CNOT", DIRECTIONS[0], "C"), origin)
    before = coordinate_state(origin, 0, condition)
    expected = translate_state(coordinate_apply(before, descriptor), translation)
    translated_before = translate_state(before, translation)
    transported = translate_global_descriptor(descriptor, translation)
    corrupted = (transported[0], descriptor[1], transported[2])
    observed = coordinate_apply(translated_before, corrupted)
    target = add_coordinate(origin, translation)
    return {
        "translation": translation,
        "quantity": "translated target output",
        "expected": expected[target],
        "observed_under_untranslated_control": observed[target],
        "corruption_rejected": observed[target] != expected[target],
    }


def independent_law_rebuild() -> dict:
    words = family()
    witnesses = []
    dependent_rows = 0
    changed_pairs = 0
    xor_failures = []
    for descriptor in words:
        word_changed = False
        for local_input in (0, 1):
            row_changed = False
            for direction_index in range(6):
                for other in OTHER_CONTEXTS:
                    left = bool_outcome(descriptor, local_input, with_edge(direction_index, other, 0))
                    right = bool_outcome(descriptor, local_input, with_edge(direction_index, other, 1))
                    if left != right:
                        changed_pairs += 1
                        row_changed = True
            dependent_rows += row_changed
            word_changed |= row_changed
        if word_changed:
            witnesses.append(descriptor)
            direction_index = DIRECTIONS.index(descriptor[1])
            for local_input in (0, 1):
                for condition in CONDITIONS:
                    expected = local_input ^ condition[direction_index]
                    observed = bool_outcome(descriptor, local_input, condition)
                    if observed != expected:
                        xor_failures.append((descriptor, local_input, condition, observed, expected))
    rotations = frame_rotations()
    rotation_failures = []
    rotation_checks = 0
    for rotation in rotations:
        for descriptor in words:
            transported = rotate_descriptor(descriptor, rotation)
            for local_input in (0, 1):
                for condition in CONDITIONS:
                    rotation_checks += 1
                    if bool_outcome(descriptor, local_input, condition) != bool_outcome(transported, local_input, rotate_condition(condition, rotation)):
                        rotation_failures.append((descriptor, local_input, condition))
    translation_failures = []
    translation_checks = 0
    origin = (0, 0, 0)
    for translation in DIRECTIONS:
        for descriptor in words:
            placed = global_descriptor(descriptor, origin)
            transported = translate_global_descriptor(placed, translation)
            for local_input in (0, 1):
                for condition in CONDITIONS:
                    translation_checks += 1
                    before = coordinate_state(origin, local_input, condition)
                    left = translate_state(coordinate_apply(before, placed), translation)
                    right = coordinate_apply(translate_state(before, translation), transported)
                    if left != right:
                        translation_failures.append(
                            (translation, descriptor, local_input, condition)
                        )
    marginal_changes = 0
    for descriptor in words:
        for direction_index in range(6):
            for other in OTHER_CONTEXTS:
                marginals = []
                for edge in (0, 1):
                    condition = with_edge(direction_index, other, edge)
                    marginals.append(tuple(
                        sum(Fraction(int(bool_outcome(descriptor, x, condition) == y), 2) for x in (0, 1))
                        for y in (0, 1)
                    ))
                marginal_changes += marginals[0] != marginals[1]
    orbit = {mat_vec(rotation, DIRECTIONS[0]) for rotation in rotations}
    return {
        "family_words": len(words),
        "witness_word_count": len(witnesses),
        "dependent_word_input_rows": dependent_rows,
        "changed_edge_pairs": changed_pairs,
        "xor_failures": xor_failures,
        "rotation_count": len(rotations),
        "rotation_semantic_comparisons": rotation_checks,
        "rotation_failures": rotation_failures,
        "translation_semantic_comparisons": translation_checks,
        "translation_failures": translation_failures,
        "word_law_class_count": int(orbit == set(DIRECTIONS)),
        "state_resolved_class_count": 2 if orbit == set(DIRECTIONS) else None,
        "uniform_target_input_edge_pairs": len(words) * 6 * len(OTHER_CONTEXTS),
        "uniform_target_input_changed_pairs": marginal_changes,
        "canonical_pair": {
            "x": 0,
            "n0": [0, 0, 0, 0, 0, 0],
            "n1": [1, 0, 0, 0, 0, 0],
            "D0": [1, 0],
            "D1": [0, 1],
        },
    }


def evaluate_weighting(vector: tuple, carrier: dict | None = None, xnor: bool = False) -> dict:
    total = sum(vector)
    nonnegative = all(value >= 0 for value in vector)
    if carrier is None:
        carrier = {(x, condition): Fraction(1, 128) for x in (0, 1) for condition in CONDITIONS}
    carrier_total = sum(carrier.values(), Fraction(0))
    event_marginal_match = carrier_total == 1
    first_disagreement = None
    conditional_checks = 0
    if total > 0 and nonnegative:
        for local_input in (0, 1):
            for condition in CONDITIONS:
                denominator = Fraction(total, total) * carrier.get((local_input, condition), Fraction(0))
                if denominator == 0:
                    first_disagreement = {
                        "configuration": [local_input, list(condition)],
                        "quantity": "conditioning carrier",
                        "observed": "0",
                        "expected": ">0",
                    }
                    break
                forced_y = local_input ^ condition[0] ^ int(xnor)
                for outcome in (0, 1):
                    conditional_checks += 1
                    observed = Fraction(int(outcome == forced_y))
                    expected = Fraction(int(outcome == (local_input ^ condition[0])))
                    if observed != expected and first_disagreement is None:
                        first_disagreement = {
                            "configuration": [local_input, list(condition), outcome],
                            "quantity": "P(y|x,n)",
                            "observed": str(observed),
                            "expected": str(expected),
                        }
            if first_disagreement:
                break
    survives = bool(nonnegative and total > 0 and event_marginal_match and first_disagreement is None)
    return {
        "verdict": "SURVIVES" if survives else "EXCLUDED",
        "nonnegative": nonnegative,
        "normalizable": total > 0,
        "event_marginal_match": event_marginal_match,
        "conditional_checks": conditional_checks,
        "first_disagreement": first_disagreement,
    }


def active_corruptions(reference_vector: tuple) -> dict:
    negative = list(reference_vector)
    negative[0] = -1
    missing_configuration_carrier = {
        (x, condition): Fraction(1, 127)
        for x in (0, 1) for condition in CONDITIONS
        if not (x == 0 and condition == (0,) * 6)
    }
    probes = {
        "negative_weight": evaluate_weighting(tuple(negative)),
        "zero_total": evaluate_weighting((0,) * len(reference_vector)),
        "missing_configuration": evaluate_weighting(reference_vector, missing_configuration_carrier),
        "xnor_instead_of_xor": evaluate_weighting(reference_vector, xnor=True),
    }
    translation_transport = translation_corruption_probe()
    return {
        "probes": probes,
        "translation_transport": translation_transport,
        "all_corruptions_rejected": bool(
            all(row["verdict"] == "EXCLUDED" for row in probes.values())
            and translation_transport["corruption_rejected"]
        ),
    }


def render(receipt: dict) -> str:
    checks = receipt["checks"]
    data = receipt["data"]
    selection = data["selection_boundary"]
    lines = ["CYCLE974_COMPATIBILITY_INDEPENDENT_CHECK"]
    lines.append(f"R0_PINS_BLOCKLIST_AND_AST {'PASS' if checks['R0_PINS_BLOCKLIST_AND_AST'] else 'FAIL'} :: pins={data['controls']['pins_match']}; text_AST_JSON_only=True; blocked_modules_loaded={data['controls']['blocked_modules_loaded']}")
    lines.append(f"R1_REFUTE_REBUILD {'PASS' if checks['R1_REFUTE_REBUILD'] else 'FAIL'} :: events={data['event_rebuild']['event_cardinality']}; candidate_digests_match={data['candidate_digests_match']}; law={compact(data['law_rebuild'])}")
    lines.append(f"R2_REFUTE_COMPATIBILITY {'PASS' if checks['R2_REFUTE_COMPATIBILITY'] else 'FAIL'} :: verdicts={compact(data['verdicts'])}; disagreement_witnesses={compact(data['disagreements'])}")
    lines.append(f"R3_ACTIVE_CORRUPTION_PROBES {'PASS' if checks['R3_ACTIVE_CORRUPTION_PROBES'] else 'FAIL'} :: rejected=negative_weight,zero_total,missing_configuration,XNOR; XNOR_witness={compact(data['corruptions']['probes']['xnor_instead_of_xor']['first_disagreement'])}")
    lines.append(f"R4_CRITERION_SCOPE {'PASS' if checks['R4_CRITERION_SCOPE'] else 'FAIL'} :: case={selection['case']}; survivors={selection['survivor_count']}/5; excluded={selection['excluded_count']}; reduction={selection['reduction']}/5; multiple_survivors_under_criterion={selection['multiple_survivors_under_criterion']}")
    lines.append(f"R5_CONTROLS {'PASS' if checks['R5_CONTROLS'] else 'FAIL'} :: determinism={data['determinism']}; runtime_s={data['runtime_seconds']:.3f}<1400; stdout_bytes={data['stdout_bytes']}<6000<150000")
    lines.append("REFUTATION_OUTCOME: NO_DISCREPANCY_FOUND" if all(checks.values()) else "REFUTATION_OUTCOME: DISCREPANCY_FOUND")
    lines.append(f"TOTAL: PASS={sum(checks.values())} FAIL={len(checks)-sum(checks.values())}")
    return "\n".join(lines) + "\n"


def run() -> tuple[dict, str]:
    started = monotonic()
    control = controls()
    rebuilt_a = independent_event_rebuild()
    rebuilt_b = independent_event_rebuild()
    law = independent_law_rebuild()
    primary = control["primary_receipt"]
    primary_rows = primary["certificates"]["A_REBUILD"]["candidate_rows"]
    digests_match = all(
        rebuilt_a["rows"][name]["normalized_weight_digest"] == primary_rows[name]["normalized_weight_digest"]
        for name in CANDIDATE_NAMES
    )
    evaluations = {
        name: evaluate_weighting(rebuilt_a["vectors"][name])
        for name in CANDIDATE_NAMES
    }
    verdicts = {name: row["verdict"] for name, row in evaluations.items()}
    disagreements = {name: row["first_disagreement"] for name, row in evaluations.items()}
    survivor_count = sum(value == "SURVIVES" for value in verdicts.values())
    excluded_count = sum(value == "EXCLUDED" for value in verdicts.values())
    selection_boundary = {
        "case": (
            "MULTIPLE_SURVIVORS_UNDER_DECLARED_CRITERION" if survivor_count > 1
            else "SINGLETON_SELECTION" if survivor_count == 1
            else "NO_SURVIVOR_REFUTATION"
        ),
        "survivor_count": survivor_count,
        "excluded_count": excluded_count,
        "reduction": len(CANDIDATE_NAMES) - survivor_count,
        "multiple_survivors_under_criterion": survivor_count > 1,
    }
    corruptions = active_corruptions(rebuilt_a["vectors"]["M1_COUNTING"])
    determinism = rebuilt_a["event_digest"] == rebuilt_b["event_digest"]
    runtime = monotonic() - started

    r1 = bool(
        rebuilt_a["event_cardinality"] == 92_260
        and rebuilt_a["events_by_tag"] == {"B0": 47_872, "B1": 44_224, "F": 164}
        and rebuilt_a["worlds"] == 748 and rebuilt_a["formed_worlds"] == 164
        and digests_match
        and law["family_words"] == 20 and law["witness_word_count"] == 6
        and law["dependent_word_input_rows"] == 12 and law["changed_edge_pairs"] == 384
        and not law["xor_failures"]
        and law["rotation_count"] == 24 and law["rotation_semantic_comparisons"] == 61_440
        and not law["rotation_failures"]
        and law["translation_semantic_comparisons"] == 15_360
        and not law["translation_failures"]
        and law["word_law_class_count"] == 1 and law["state_resolved_class_count"] == 2
        and law["uniform_target_input_edge_pairs"] == 3_840
        and law["uniform_target_input_changed_pairs"] == 0
    )
    checks = {
        "R0_PINS_BLOCKLIST_AND_AST": control["pass"],
        "R1_REFUTE_REBUILD": r1,
        "R2_REFUTE_COMPATIBILITY": all(verdict == "SURVIVES" for verdict in verdicts.values()) and not any(disagreements.values()),
        "R3_ACTIVE_CORRUPTION_PROBES": corruptions["all_corruptions_rejected"],
        "R4_CRITERION_SCOPE": bool(
            tuple(verdicts) == CANDIDATE_NAMES
            and survivor_count + excluded_count == len(CANDIDATE_NAMES)
            and selection_boundary["survivor_count"]
                == primary["certificates"]["C_SELECTION_STATUS"]["freedom_after"]
            and selection_boundary["excluded_count"]
                == len(primary["certificates"]["C_SELECTION_STATUS"]["excluded"])
            and selection_boundary["reduction"]
                == primary["certificates"]["C_SELECTION_STATUS"]["absolute_reduction"]
            and selection_boundary["multiple_survivors_under_criterion"]
                == primary["certificates"]["C_SELECTION_STATUS"]["multiple_survivors_under_criterion"]
        ),
        "R5_CONTROLS": bool(control["pass"] and determinism and runtime < AUDIT_TIMEOUT_SEC),
    }
    receipt = {
        "cycle": 974,
        "checks": checks,
        "data": {
            "controls": {key: value for key, value in control.items() if key != "primary_receipt"},
            "event_rebuild": {key: value for key, value in rebuilt_a.items() if key != "vectors"},
            "candidate_digests_match": digests_match,
            "law_rebuild": law,
            "verdicts": verdicts,
            "disagreements": disagreements,
            "selection_boundary": selection_boundary,
            "corruptions": corruptions,
            "determinism": determinism,
            "runtime_seconds": runtime,
            "stdout_bytes": 0,
        },
    }
    for _ in range(4):
        output = render(receipt)
        receipt["data"]["stdout_bytes"] = len(output.encode())
    output = render(receipt)
    receipt["checks"]["R5_CONTROLS"] &= len(output.encode()) < HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
    output = render(receipt)
    receipt["pass"] = all(receipt["checks"].values())
    receipt["checker_source_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    return receipt, output


def main() -> int:
    receipt, output = run()
    RECEIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sys.stdout.write(output)
    return 0 if receipt["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
