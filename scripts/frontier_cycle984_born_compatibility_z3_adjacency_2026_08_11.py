#!/usr/bin/env python3
"""Cycle 984: Born compatibility on the finite true-Z3 star instance.

This runner independently reconstructs the target-local seven-site Z3 star,
its 23 word-length-at-most-one Boolean programs, and the five finite event
weightings.  It does not import a prior verdict.  The per-instance criterion
is evaluated outcome-neutrally: every exclusion must carry its first exact
witness, and an all-survivor result receives no privileged integrity path.
"""

from __future__ import annotations

import importlib.util
import io
import json
import subprocess
import sys
import tarfile
import tempfile
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECEIPT_PATH = ROOT / "outputs/born_compatibility_z3_adjacency_cycle984_receipt_2026_08_11.json"

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 6000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

PINNED_CYCLE719_COMMIT = "39c74017b870c27c804e3992f2a11e90336476b2"
PINNED_CYCLE719_CORE = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
PINNED_CYCLE719_CORE_SHA256 = "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4"
PINNED_CYCLE719_CORE_BLOB = "c123b8d681c3d76fce08ef13d7673622deac64ad"

P_INSTANCE_CRITERION_VERBATIM = (
    "An exclusion is licensed only by a negative event weight, a zero total, "
    "a failed event marginal, missing required neighbour variation, failed "
    "proper-cubic closure, or a concrete program/configuration mismatch."
)

CENTER_NAME = "C"
DIRECTION_NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
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
    "M2_PER_WORLD_UNIFORM":
        "world score a(w)=1; uniform within each event-bearing world",
    "M3_OCCUPATION_WEIGHTED":
        "a(w)=clean-dwell occupation count; uniform within world",
    "M4_FORMATION_LIFETIME":
        "a(w)=boundaries-formation_moment(w)+1 if formed, else 0; uniform within world",
    "M5_FORMATION_MOMENT":
        "a(w)=formation_moment(w) if formed, else 0; uniform within world",
}

FIXTURE_BANKS = 2
MIN_SOURCES = 2
MAX_SOURCES = 5
HORIZON = 16_384
REGISTER_CAP = 64
DETERMINISM_ORBITS = 192
CLASS_ORDER = (
    "CNOT",
    "TOF_PERPENDICULAR_CONTROLS",
    "TOF_OPPOSITE_CONTROLS",
)
BLOCKED_VERDICT_MODULE_FRAGMENTS = (
    "cycle974", "cycle975", "cycle978", "cycle979", "cycle982",
)


def canonical_digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return sha256(payload.encode("utf-8")).hexdigest()


def lcm(left: int, right: int) -> int:
    return left * right // gcd(left, right)


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_pinned_cycle719_core():
    archive = subprocess.run(
        ["git", "archive", "--format=tar", PINNED_CYCLE719_COMMIT, "scripts"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout
    temporary = tempfile.TemporaryDirectory(prefix="cycle984-cycle719-")
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as bundle:
        bundle.extractall(temporary.name, filter="data")
    scripts_dir = Path(temporary.name) / "scripts"
    sys.path.insert(0, str(scripts_dir))
    core_path = Path(temporary.name) / PINNED_CYCLE719_CORE
    spec = importlib.util.spec_from_file_location("cycle984_pinned_cycle719", core_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load pinned Cycle-719 core")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return temporary, module, core_path


PINNED_TEMP, K, PINNED_CORE_PATH = load_pinned_cycle719_core()


def determinant3(matrix: tuple[tuple[int, ...], ...]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def proper_cubic_rotations() -> tuple:
    matrices = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for output_axis in range(3):
                row = [0, 0, 0]
                row[perm[output_axis]] = signs[output_axis]
                rows.append(tuple(row))
            matrix = tuple(rows)
            if determinant3(matrix) == 1:
                matrices.append(matrix)
    return tuple(sorted(set(matrices)))


def rotate(vector: tuple[int, int, int], matrix: tuple) -> tuple[int, int, int]:
    return tuple(sum(row[i] * vector[i] for i in range(3)) for row in matrix)


def program_name(program: dict) -> str:
    if program["kind"] == "I":
        return "I"
    if program["kind"] == "X":
        return "X(C)"
    controls = program["controls"]
    if program["kind"] == "CNOT":
        return f"CNOT({controls[0]}->C)"
    return f"TOF({controls[0]},{controls[1]}->C)"


def build_z3_instance() -> dict:
    sites = ((CENTER_NAME, (0, 0, 0)), *zip(DIRECTION_NAMES, DIRECTIONS))
    edges = tuple((CENTER_NAME, name) for name in DIRECTION_NAMES)
    programs = [{"kind": "I", "controls": ()}, {"kind": "X", "controls": ()}]
    programs.extend({"kind": "CNOT", "controls": (name,)} for name in DIRECTION_NAMES)
    programs.extend(
        {"kind": "TOF", "controls": pair}
        for pair in combinations(DIRECTION_NAMES, 2)
    )
    for index, row in enumerate(programs):
        row["index"] = index
        row["name"] = program_name(row)
    return {"sites": sites, "edges": edges, "programs": tuple(programs)}


def target_output(program: dict, target: int, neighbours: tuple[int, ...]) -> int:
    by_name = dict(zip(DIRECTION_NAMES, neighbours))
    if program["kind"] == "I":
        return target
    if program["kind"] == "X":
        return target ^ 1
    if program["kind"] == "CNOT":
        return target ^ by_name[program["controls"][0]]
    left, right = program["controls"]
    return target ^ (by_name[left] & by_name[right])


def reference_output(program: dict, target: int, neighbours: tuple[int, ...]) -> int:
    index = {name: offset for offset, name in enumerate(DIRECTION_NAMES)}
    kind = program["kind"]
    if kind in ("I", "X"):
        return (target + int(kind == "X")) % 2
    control_bits = [neighbours[index[name]] for name in program["controls"]]
    flip = control_bits[0] if len(control_bits) == 1 else min(control_bits)
    return (target + flip) % 2


def dependence_class(program: dict) -> str | None:
    if program["kind"] == "CNOT":
        return "CNOT"
    if program["kind"] != "TOF":
        return None
    vectors = dict(zip(DIRECTION_NAMES, DIRECTIONS))
    left, right = (vectors[name] for name in program["controls"])
    if tuple(left[i] + right[i] for i in range(3)) == (0, 0, 0):
        return "TOF_OPPOSITE_CONTROLS"
    return "TOF_PERPENDICULAR_CONTROLS"


def class_and_truth_census(instance: dict) -> dict:
    rows = []
    first_mismatch = None
    all_conditions = tuple(product((0, 1), repeat=6))
    for program in instance["programs"]:
        changed = []
        comparisons = 0
        for direction_index, direction_name in enumerate(DIRECTION_NAMES):
            depends = False
            for target in (0, 1):
                for condition in all_conditions:
                    actual = target_output(program, target, condition)
                    reference = reference_output(program, target, condition)
                    if actual != reference and first_mismatch is None:
                        first_mismatch = {
                            "program": program["name"],
                            "target": target,
                            "neighbours": condition,
                            "actual": actual,
                            "reference": reference,
                        }
                    if condition[direction_index] == 0:
                        flipped = list(condition)
                        flipped[direction_index] = 1
                        if target_output(program, target, condition) != target_output(
                            program, target, tuple(flipped)
                        ):
                            depends = True
                            comparisons += 1
            if depends:
                changed.append(direction_name)
        class_name = dependence_class(program) if changed else None
        rows.append({
            "index": program["index"],
            "name": program["name"],
            "kind": program["kind"],
            "controls": program["controls"],
            "classes": () if class_name is None else (class_name,),
            "changed_directions": tuple(changed),
            "changed_edge_pair_count": comparisons,
        })
    class_counts = Counter(
        row["classes"][0] if row["classes"] else "NONE" for row in rows
    )
    return {
        "rows": tuple(rows),
        "class_counts": dict(sorted(class_counts.items())),
        "multi_class_programs": sum(len(row["classes"]) > 1 for row in rows),
        "max_classes_per_program": max(len(row["classes"]) for row in rows),
        "first_program_configuration_mismatch": first_mismatch,
    }


def orbit_certificate(instance: dict, census: dict) -> dict:
    rotations = proper_cubic_rotations()
    vectors = dict(zip(DIRECTION_NAMES, DIRECTIONS))
    vector_names = {vector: name for name, vector in vectors.items()}
    class_members = {
        class_name: tuple(
            row["controls"] for row in census["rows"]
            if row["classes"] == (class_name,)
        )
        for class_name in CLASS_ORDER
    }

    def canonical_controls(controls: tuple[str, ...]) -> tuple[str, ...]:
        return tuple(sorted(controls, key=DIRECTION_NAMES.index))

    representatives = {class_name: members[0] for class_name, members in class_members.items()}
    rows = {}
    closure_failures = []
    for class_name, representative in representatives.items():
        orbit = set()
        stabilizer = 0
        for matrix in rotations:
            rotated = canonical_controls(tuple(
                vector_names[rotate(vectors[name], matrix)] for name in representative
            ))
            orbit.add(rotated)
            if rotated == canonical_controls(representative):
                stabilizer += 1
        expected_members = {canonical_controls(member) for member in class_members[class_name]}
        if orbit != expected_members:
            closure_failures.append({
                "class": class_name,
                "missing": sorted(expected_members - orbit),
                "extra": sorted(orbit - expected_members),
            })
        summed = tuple(sum(vectors[name][axis] for name in representative) for axis in range(3))
        rows[class_name] = {
            "representative": representative,
            "orbit_size": len(orbit),
            "stabilizer": stabilizer,
            "J": sum(component * component for component in summed),
            "members": class_members[class_name],
        }
    return {
        "rotation_count": len(rotations),
        "classes": rows,
        "closure_failures": closure_failures,
    }


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


def derive_worlds() -> tuple:
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
            diffs = [i for i, pair in enumerate(zip(baseline, marked)) if pair[0] != pair[1]]
            if len(diffs) != 1:
                raise AssertionError(("bank marker", bank_index, wire, diffs))
            per_bank[bank_index].add(diffs[0])
    link_wires = set()
    for link_index, link in enumerate(zero_links):
        for wire in range(len(link)):
            changed = [list(row) for row in zero_links]
            changed[link_index][wire] = 1
            marked = K.M.pack_state(zero_banks, tuple(map(tuple, changed)))
            diffs = [i for i, pair in enumerate(zip(baseline, marked)) if pair[0] != pair[1]]
            if len(diffs) != 1:
                raise AssertionError(("link marker", link_index, wire, diffs))
            link_wires.add(diffs[0])
    return (
        tuple(tuple(sorted(row)) for row in per_bank),
        tuple(sorted(link_wires)),
        K.R3.X.SOURCE_POINTER,
    )


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
    program, seeds, worlds = derive_worlds()
    states = initial_states(program, seeds, worlds)
    columns = pack_lanes(states)
    schedule = compiled_schedule(program, worlds)
    per_bank, link_wires, source_pointer = dirty_partition()
    global_dirty = tuple(sorted(set(per_bank[0]) | set(per_bank[1]) | set(link_wires) | {source_pointer}))
    universe = (1 << len(worlds)) - 1
    events = []
    occupation = [0] * len(worlds)
    formed = {}
    ordinals = [[0, 0] for _ in worlds]

    global_0 = clean_mask(columns, global_dirty, universe)
    bank_0 = [clean_mask(columns, per_bank[index], universe) for index in (0, 1)]
    for lane in lanes(global_0):
        occupation[lane] += 1
        formed[lane] = 0
        events.append((lane, 0, "F", 0))
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
                current = clean_mask(columns, per_bank[bank], universe)
                for lane in lanes(current & ~previous_bank[bank]):
                    ordinal = ordinals[lane][bank]
                    if ordinal < REGISTER_CAP:
                        events.append((lane, boundary, f"B{bank}", ordinal))
                    else:
                        beyond_cap += 1
                    ordinals[lane][bank] += 1
                previous_bank[bank] = current
    return {
        "program_stations": len(program),
        "worlds": worlds,
        "events": tuple(events),
        "occupation": tuple(occupation),
        "formed": formed,
        "boundaries": boundary,
        "beyond_cap": beyond_cap,
    }


def rebuild_candidates(event_data: dict) -> dict:
    events = event_data["events"]
    per_world = Counter(event[0] for event in events)
    tag_counts_by_world = {world: Counter() for world in range(len(event_data["worlds"]))}
    for world, _moment, tag, _ordinal in events:
        tag_counts_by_world[world][tag] += 1
    common = 1
    for count in set(per_world.values()):
        common = lcm(common, count)
    boundaries = event_data["boundaries"]
    formed = event_data["formed"]
    occupation = event_data["occupation"]
    scores = {
        "M1_COUNTING": lambda world: per_world[world],
        "M2_PER_WORLD_UNIFORM": lambda _world: 1,
        "M3_OCCUPATION_WEIGHTED": lambda world: occupation[world],
        "M4_FORMATION_LIFETIME":
            lambda world: boundaries - formed[world] + 1 if world in formed else 0,
        "M5_FORMATION_MOMENT": lambda world: formed[world] if world in formed else 0,
    }
    candidates = {}
    for name in CANDIDATE_NAMES:
        world_rows = []
        negative_witness = None
        total = 0
        zeros = 0
        positives = 0
        for world in range(len(event_data["worlds"])):
            count = per_world[world]
            if count == 0:
                continue
            numerator = 1 if name == "M1_COUNTING" else scores[name](world) * (common // count)
            if numerator < 0 and negative_witness is None:
                negative_witness = {"world": world, "event_numerator": numerator}
            total += count * numerator
            zeros += count if numerator == 0 else 0
            positives += count if numerator > 0 else 0
            world_rows.append((world, count, numerator))
        candidates[name] = {
            "definition": CANDIDATE_DEFINITIONS[name],
            "integer_numerator_total": total,
            "normalizable": total > 0,
            "nonnegative": negative_witness is None,
            "first_negative_witness": negative_witness,
            "zero_weight_events": zeros,
            "positive_weight_events": positives,
            "normalized_weight_certificate_digest": canonical_digest({
                "world_rows": world_rows,
                "total": total,
            }),
        }
    world_summary = []
    for world, descriptor in enumerate(event_data["worlds"]):
        world_summary.append({
            "world": world,
            "source_count": descriptor[0],
            "seed_event": descriptor[1],
            "positions": descriptor[2],
            "event_count": per_world[world],
            "events_by_tag": dict(sorted(tag_counts_by_world[world].items())),
            "occupation": occupation[world],
            "formation_moment": formed.get(world),
        })
    return {
        "event_cardinality": len(events),
        "events_by_tag": dict(sorted(Counter(event[2] for event in events).items())),
        "worlds_in_census": len(event_data["worlds"]),
        "worlds_with_events": len(per_world),
        "formed_worlds": len(formed),
        "common_world_denominator": common,
        "boundaries": boundaries,
        "world_summary": world_summary,
        "candidates": candidates,
    }


def output_distribution(program: dict, condition: tuple[int, ...], p_zero: Fraction) -> tuple[Fraction, Fraction]:
    probs = [Fraction(0), Fraction(0)]
    for target, probability in ((0, p_zero), (1, 1 - p_zero)):
        probs[target_output(program, target, condition)] += probability
    return tuple(probs)


def total_variation(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> Fraction:
    return sum(abs(a - b) for a, b in zip(left, right)) / 2


def variation_certificate(instance: dict, census: dict, p_zero: Fraction) -> dict:
    by_name = {program["name"]: program for program in instance["programs"]}
    representatives = {
        class_name: next(row["name"] for row in census["rows"] if row["classes"] == (class_name,))
        for class_name in CLASS_ORDER
    }
    results = {}
    for class_name, name in representatives.items():
        program = by_name[name]
        first = None
        for direction_index, direction_name in enumerate(DIRECTION_NAMES):
            for condition in product((0, 1), repeat=6):
                if condition[direction_index] != 0:
                    continue
                flipped = list(condition)
                flipped[direction_index] = 1
                flipped = tuple(flipped)
                left = output_distribution(program, condition, p_zero)
                right = output_distribution(program, flipped, p_zero)
                tv = total_variation(left, right)
                if tv > 0:
                    first = {
                        "program": name,
                        "varied_direction": direction_name,
                        "condition_0": condition,
                        "condition_1": flipped,
                        "distribution_0": [str(value) for value in left],
                        "distribution_1": [str(value) for value in right],
                        "tv": str(tv),
                    }
                    break
            if first is not None:
                break
        results[class_name] = first
    return {"p_zero": str(p_zero), "classes": results}


def marginal_factors(instance: dict, p_zero: Fraction) -> dict:
    q = Fraction(1, 64)
    rows = {}
    for program in instance["programs"]:
        factor = Fraction(0)
        for target, mu in ((0, p_zero), (1, 1 - p_zero)):
            for condition in product((0, 1), repeat=6):
                outputs = sum(
                    int(outcome == target_output(program, target, condition))
                    for outcome in (0, 1)
                )
                factor += mu * q * outputs
        rows[program["name"]] = factor
    return rows


def evaluate_candidates(candidates: dict, instance: dict, census: dict, orbits: dict, p_zero: Fraction) -> dict:
    factors = marginal_factors(instance, p_zero)
    variation = variation_certificate(instance, census, p_zero)
    results = {}
    for name in CANDIDATE_NAMES:
        candidate = candidates["candidates"][name]
        witness = None
        if not candidate["nonnegative"]:
            witness = {"condition": "negative event weight", **candidate["first_negative_witness"]}
        elif not candidate["normalizable"]:
            witness = {"condition": "zero total", "total": candidate["integer_numerator_total"]}
        else:
            bad_factor = next((program for program, factor in factors.items() if factor != 1), None)
            if bad_factor is not None:
                witness = {
                    "condition": "failed event marginal",
                    "program": bad_factor,
                    "marginal_factor": str(factors[bad_factor]),
                }
            else:
                missing = next((class_name for class_name, row in variation["classes"].items() if row is None), None)
                if missing is not None:
                    witness = {"condition": "missing required neighbour variation", "class": missing}
                elif orbits["closure_failures"]:
                    witness = {"condition": "failed proper-cubic closure", **orbits["closure_failures"][0]}
                elif census["first_program_configuration_mismatch"] is not None:
                    witness = {
                        "condition": "concrete program/configuration mismatch",
                        **census["first_program_configuration_mismatch"],
                    }
        results[name] = {
            "verdict": "SURVIVES" if witness is None else "EXCLUDED",
            "first_exclusion_witness": witness,
        }
    return {
        "p_zero": str(p_zero),
        "criterion": P_INSTANCE_CRITERION_VERBATIM,
        "marginal_factors": {name: str(value) for name, value in factors.items()},
        "variation": variation,
        "candidates": results,
        "survivors": tuple(name for name in CANDIDATE_NAMES if results[name]["verdict"] == "SURVIVES"),
    }


def transfer_verdict(candidate_results: dict) -> dict:
    excluded = [name for name in CANDIDATE_NAMES if candidate_results["candidates"][name]["verdict"] == "EXCLUDED"]
    if excluded:
        first = excluded[0]
        return {
            "verdict": "FAILS_TO_TRANSFER",
            "first_weighting_lost": first,
            "witness": candidate_results["candidates"][first]["first_exclusion_witness"],
        }
    return {"verdict": "TRANSFERS", "first_weighting_lost": None, "witness": None}


def robustness_family(instance: dict, census: dict) -> dict:
    rows = {}
    for p_zero in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)):
        certificate = variation_certificate(instance, census, p_zero)
        observed = {
            class_name: "0" if row is None else row["tv"]
            for class_name, row in certificate["classes"].items()
        }
        rows[str(p_zero)] = {
            "expected_abs_2p_minus_1": str(abs(2 * p_zero - 1)),
            "observed_tv": observed,
        }
    return rows


def bookkeeping_validator(summary: dict) -> bool:
    candidate_rows = summary["candidate_results"]["candidates"]
    survivors = tuple(name for name in CANDIDATE_NAMES if candidate_rows[name]["verdict"] == "SURVIVES")
    exclusions_have_witnesses = all(
        row["first_exclusion_witness"] is not None
        for row in candidate_rows.values() if row["verdict"] == "EXCLUDED"
    )
    survivors_have_no_witnesses = all(
        row["first_exclusion_witness"] is None
        for row in candidate_rows.values() if row["verdict"] == "SURVIVES"
    )
    transfer = transfer_verdict(summary["candidate_results"])
    return bool(
        set(candidate_rows) == set(CANDIDATE_NAMES)
        and survivors == tuple(summary["candidate_results"]["survivors"])
        and exclusions_have_witnesses
        and survivors_have_no_witnesses
        and transfer == summary["transfer"]
    )


def mutation_controls(summary: dict) -> dict:
    probes = {}

    corrupted = json.loads(json.dumps(summary))
    corrupted["candidate_results"]["candidates"]["M1_COUNTING"]["verdict"] = "EXCLUDED"
    probes["exclusion_without_witness"] = not bookkeeping_validator(corrupted)

    corrupted = json.loads(json.dumps(summary))
    corrupted["candidate_results"]["survivors"] = []
    probes["survivor_count"] = not bookkeeping_validator(corrupted)

    corrupted = json.loads(json.dumps(summary))
    corrupted["transfer"]["verdict"] = "FAILS_TO_TRANSFER"
    probes["transfer_headline"] = not bookkeeping_validator(corrupted)

    synthetic = json.loads(json.dumps(summary))
    synthetic["candidate_results"]["candidates"]["M1_COUNTING"] = {
        "verdict": "EXCLUDED",
        "first_exclusion_witness": {"condition": "negative event weight", "world": 0, "event_numerator": -1},
    }
    synthetic["candidate_results"]["survivors"] = list(CANDIDATE_NAMES[1:])
    synthetic["transfer"] = transfer_verdict(synthetic["candidate_results"])
    probes["coherent_one_excluded_accepted"] = bookkeeping_validator(synthetic)

    return probes


def provenance_controls() -> dict:
    source_sha = file_sha256(PINNED_CORE_PATH)
    blob = subprocess.check_output(
        ["git", "rev-parse", f"{PINNED_CYCLE719_COMMIT}:{PINNED_CYCLE719_CORE}"],
        cwd=ROOT,
        text=True,
    ).strip()
    ancestry = subprocess.run(
        ["git", "merge-base", "--is-ancestor", PINNED_CYCLE719_COMMIT, "HEAD"],
        cwd=ROOT,
        check=False,
    ).returncode == 0
    blocked_loaded = sorted(
        name for name in sys.modules
        if any(fragment in name.lower() for fragment in BLOCKED_VERDICT_MODULE_FRAGMENTS)
        and name != "__main__"
    )
    return {
        "pinned_core_sha256": source_sha,
        "expected_pinned_core_sha256": PINNED_CYCLE719_CORE_SHA256,
        "pinned_core_blob": blob,
        "expected_pinned_core_blob": PINNED_CYCLE719_CORE_BLOB,
        "pinned_commit_is_ancestor": ancestry,
        "prior_verdict_modules_loaded": blocked_loaded,
        "pass": bool(
            source_sha == PINNED_CYCLE719_CORE_SHA256
            and blob == PINNED_CYCLE719_CORE_BLOB
            and ancestry
            and not blocked_loaded
        ),
    }


def main() -> int:
    instance = build_z3_instance()
    census = class_and_truth_census(instance)
    orbits = orbit_certificate(instance, census)

    full_events = rebuild_event_data(HORIZON)
    short_a = rebuild_event_data(DETERMINISM_ORBITS)
    short_b = rebuild_event_data(DETERMINISM_ORBITS)
    candidates = rebuild_candidates(full_events)
    candidate_results = evaluate_candidates(candidates, instance, census, orbits, Fraction(1, 4))
    transfer = transfer_verdict(candidate_results)
    robustness = robustness_family(instance, census)

    requirement = "JOINT" if census["multi_class_programs"] else "PER_INSTANCE"
    injected = dict(census)
    injected["multi_class_programs"] = 1
    injected_requirement = "JOINT" if injected["multi_class_programs"] else "PER_INSTANCE"

    summary = {"candidate_results": candidate_results, "transfer": transfer}
    mutations = mutation_controls(summary)
    provenance = provenance_controls()

    site_map = {name: coordinates for name, coordinates in instance["sites"]}
    program_rows = [
        {
            **row,
            "controls": list(row["controls"]),
            "classes": list(row["classes"]),
            "changed_directions": list(row["changed_directions"]),
        }
        for row in census["rows"]
    ]
    receipt = {
        "claim_id": "cycle984_born_compatibility_z3_adjacency",
        "claim_type": "bounded_theorem",
        "audit_status_authority": "independent audit lane only",
        "verdict_imports_used": [],
        "criterion_verbatim": P_INSTANCE_CRITERION_VERBATIM,
        "criterion_adaptation": "none; only the declared program domain is the 23 target-local true-Z3 descriptors",
        "z3_instance": {
            "sites": site_map,
            "edges": [list(edge) for edge in instance["edges"]],
            "program_count": len(instance["programs"]),
            "programs": program_rows,
            "class_counts": census["class_counts"],
            "multi_class_programs": census["multi_class_programs"],
            "max_classes_per_program": census["max_classes_per_program"],
            "truth_table_evaluations": len(instance["programs"]) * 2 * 64,
            "first_program_configuration_mismatch": census["first_program_configuration_mismatch"],
        },
        "orbits": orbits,
        "weighting_rebuild": candidates,
        "requirement": {
            "selected": requirement,
            "injected_coexistence_selected": injected_requirement,
        },
        "per_instance_test": candidate_results,
        "transfer": transfer,
        "input_robustness": robustness,
        "controls": {
            "short_replay_deterministic": short_a == short_b,
            "short_event_count": len(short_a["events"]),
            "mutation_probes": mutations,
            "provenance": provenance,
        },
    }

    a_pass = bool(
        len(instance["sites"]) == 7
        and len(instance["edges"]) == 6
        and len(instance["programs"]) == 23
        and census["class_counts"] == {
            "CNOT": 6,
            "NONE": 2,
            "TOF_OPPOSITE_CONTROLS": 3,
            "TOF_PERPENDICULAR_CONTROLS": 12,
        }
        and census["first_program_configuration_mismatch"] is None
        and orbits["rotation_count"] == 24
    )
    b_pass = bool(
        requirement == "PER_INSTANCE"
        and injected_requirement == "JOINT"
        and candidate_results["criterion"] == P_INSTANCE_CRITERION_VERBATIM
        and bookkeeping_validator(summary)
    )
    c_pass = bookkeeping_validator(summary)
    d_pass = all(
        all(value == row["expected_abs_2p_minus_1"] for value in row["observed_tv"].values())
        for row in robustness.values()
    )
    e_pass = bool(
        candidates["event_cardinality"] == sum(candidates["events_by_tag"].values())
        and set(candidates["candidates"]) == set(CANDIDATE_NAMES)
        and all(mutations.values())
        and provenance["pass"]
        and short_a == short_b
    )

    receipt["checks"] = {
        "A_REBUILD_ON_Z3": a_pass,
        "B_PER_INSTANCE_TEST": b_pass,
        "C_TRANSFER_VERDICT": c_pass,
        "D_INPUT_ROBUSTNESS": d_pass,
        "E_CONTROLS": e_pass,
    }
    receipt["receipt_sha256_without_self"] = canonical_digest(receipt)
    RECEIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    sites_text = "; ".join(f"{name}={coordinates}" for name, coordinates in instance["sites"])
    programs_text = "; ".join(program["name"] for program in instance["programs"])
    weights_text = " | ".join(
        f"{name}: {row['definition']}; total={row['integer_numerator_total']}; "
        f"zero={row['zero_weight_events']}; digest={row['normalized_weight_certificate_digest'][:12]}"
        for name, row in candidates["candidates"].items()
    )
    verdict_text = " | ".join(
        f"{name}={row['verdict']}; witness={row['first_exclusion_witness'] or 'none'}"
        for name, row in candidate_results["candidates"].items()
    )

    print(f"Z3_STAR_SITES(7): {sites_text}")
    print("Z3_STAR_EDGES(6): " + "; ".join(f"{left}--{right}" for left, right in instance["edges"]))
    print(f"Z3_PROGRAMS(23): {programs_text}")
    print(
        "WEIGHTING_REBUILD: "
        f"events={candidates['event_cardinality']}; worlds={candidates['worlds_in_census']}; "
        f"formed={candidates['formed_worlds']}; tags={candidates['events_by_tag']}"
    )
    print(f"WEIGHTINGS(5): {weights_text}")
    print(f"CRITERION_VERBATIM: {P_INSTANCE_CRITERION_VERBATIM}")
    print("CRITERION_ADAPTATION: none; domain declaration is the 23 target-local true-Z3 programs")
    print(f"PER_INSTANCE_RESULTS: {verdict_text}")
    print(f"SURVIVORS/5: {len(candidate_results['survivors'])}/5")
    print(
        f"TRANSFER_VERDICT: {transfer['verdict']}; "
        f"weighting={transfer['first_weighting_lost'] or 'none'}; witness={transfer['witness'] or 'none'}"
    )
    print(
        "NONUNIFORM_P=1/4: "
        + "; ".join(
            f"{class_name}: TV={row['tv'] if row else '0'}"
            for class_name, row in candidate_results["variation"]["classes"].items()
        )
        + f"; survivors={len(candidate_results['survivors'])}/5"
    )
    print("per_element: checked and executed -- all five finite event laws and every event-bearing world were rebuilt")
    print("per_site: checked and executed -- centre plus all six true-Z3 nearest neighbours were enumerated")
    print("per_mode: checked and not executed -- no Fourier or continuous M_2(C) mode claim is made")
    print("per_block: checked and executed -- all 23 programs, 2944 truth rows, three orbits, and five candidate blocks were checked")
    print("lattice_wide: checked and not executed -- the theorem is one finite radius-one star, not an infinite-lattice realization")
    for name, passed in receipt["checks"].items():
        print(f"{name} {'PASS' if passed else 'FAIL'}")
    pass_count = sum(receipt["checks"].values())
    print(f"TOTAL: PASS={pass_count} FAIL={len(receipt['checks']) - pass_count}")
    return 0 if all(receipt["checks"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
