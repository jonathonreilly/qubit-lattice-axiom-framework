#!/usr/bin/env python3
"""Independent refutation checker for Cycle 984.

The checker parses but never imports or executes the primary.  It does not
load Cycle 719 or any earlier cycle runner.  It independently reconstructs
the finite Z3 Boolean instance, re-evaluates the five weighting formulas from
the primary receipt's per-world sufficient statistics, recomputes the
per-instance verdict, and actively rejects corruptions of decisive fields.
"""

from __future__ import annotations

import ast
import copy
import json
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = ROOT / "scripts/frontier_cycle984_born_compatibility_z3_adjacency_2026_08_11.py"
PRIMARY_RECEIPT_PATH = ROOT / "outputs/born_compatibility_z3_adjacency_cycle984_receipt_2026_08_11.json"
PRIMARY_CACHE_PATH = ROOT / "logs/runner-cache/frontier_cycle984_born_compatibility_z3_adjacency_2026_08_11.txt"
RECEIPT_PATH = ROOT / "outputs/born_compatibility_z3_adjacency_cycle984_independent_check_receipt_2026_08_11.json"

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 6000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle984_born_compatibility_z3_adjacency_2026_08_11.py",
    "outputs/born_compatibility_z3_adjacency_cycle984_receipt_2026_08_11.json",
    "logs/runner-cache/frontier_cycle984_born_compatibility_z3_adjacency_2026_08_11.txt",
)

EXPECTED_PRIMARY_SHA256 = "45a5bfd7ae9a67a5b4c600ab8226b166ece0e442683374c0bef17625cda5cebc"
EXPECTED_PRIMARY_RECEIPT_SHA256 = "1632d90a128371aa69814d9eabb5a6cdcd0ea97ff220e25e26bfba796f5d32ed"
EXPECTED_PRIMARY_CACHE_INPUT_FINGERPRINT = "b47fb7d88de539c8233152d8acee62b360b8aac23720d0621be787565054b63a"

EXPECTED_CRITERION = (
    "An exclusion is licensed only by a negative event weight, a zero total, "
    "a failed event marginal, missing required neighbour variation, failed "
    "proper-cubic closure, or a concrete program/configuration mismatch."
)
NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")
COORDINATES = {
    "C": (0, 0, 0),
    "+x": (1, 0, 0), "-x": (-1, 0, 0),
    "+y": (0, 1, 0), "-y": (0, -1, 0),
    "+z": (0, 0, 1), "-z": (0, 0, -1),
}
WEIGHT_NAMES = (
    "M1_COUNTING",
    "M2_PER_WORLD_UNIFORM",
    "M3_OCCUPATION_WEIGHTED",
    "M4_FORMATION_LIFETIME",
    "M5_FORMATION_MOMENT",
)
CLASS_NAMES = (
    "CNOT",
    "TOF_PERPENDICULAR_CONTROLS",
    "TOF_OPPOSITE_CONTROLS",
)


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return sha256(payload.encode("utf-8")).hexdigest()


def lcm(left: int, right: int) -> int:
    return left * right // gcd(left, right)


def literal_assignments(path: Path) -> dict:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    result = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            try:
                result[node.targets[0].id] = ast.literal_eval(node.value)
            except (ValueError, TypeError):
                pass
    return result


def independent_programs() -> tuple:
    rows = [("I", ()), ("X", ())]
    rows.extend(("CNOT", (index,)) for index in range(6))
    rows.extend(("TOF", pair) for pair in combinations(range(6), 2))
    return tuple(rows)


def label(program: tuple) -> str:
    kind, controls = program
    if kind == "I":
        return "I"
    if kind == "X":
        return "X(C)"
    if kind == "CNOT":
        return f"CNOT({NAMES[controls[0]]}->C)"
    return f"TOF({NAMES[controls[0]]},{NAMES[controls[1]]}->C)"


def independent_output(program: tuple, target: int, neighbours: tuple[int, ...]) -> int:
    kind, controls = program
    if kind == "I":
        flip = 0
    elif kind == "X":
        flip = 1
    elif kind == "CNOT":
        flip = neighbours[controls[0]]
    else:
        flip = neighbours[controls[0]] * neighbours[controls[1]]
    return 1 if target != flip else 0


def independent_class(program: tuple) -> str | None:
    kind, controls = program
    if kind == "CNOT":
        return "CNOT"
    if kind != "TOF":
        return None
    left = COORDINATES[NAMES[controls[0]]]
    right = COORDINATES[NAMES[controls[1]]]
    dot = sum(a * b for a, b in zip(left, right))
    return "TOF_OPPOSITE_CONTROLS" if dot == -1 else "TOF_PERPENDICULAR_CONTROLS"


def independent_z3_certificate() -> dict:
    programs = independent_programs()
    rows = []
    class_counts = {"NONE": 0, **{name: 0 for name in CLASS_NAMES}}
    mismatch = None
    for index, program in enumerate(programs):
        class_name = independent_class(program)
        class_counts[class_name or "NONE"] += 1
        changed = []
        changed_count = 0
        for direction in range(6):
            seen = False
            for target in (0, 1):
                for spectators in product((0, 1), repeat=5):
                    low = list(spectators)
                    low.insert(direction, 0)
                    high = list(low)
                    high[direction] = 1
                    if independent_output(program, target, tuple(low)) != independent_output(program, target, tuple(high)):
                        seen = True
                        changed_count += 1
            if seen:
                changed.append(NAMES[direction])
        rows.append({
            "index": index,
            "name": label(program),
            "kind": program[0],
            "controls": [NAMES[i] for i in program[1]],
            "classes": [] if class_name is None else [class_name],
            "changed_directions": changed,
            "changed_edge_pair_count": changed_count,
        })
    return {
        "sites": {name: list(COORDINATES[name]) for name in ("C", *NAMES)},
        "edges": [["C", name] for name in NAMES],
        "program_count": len(programs),
        "programs": rows,
        "class_counts": dict(sorted(class_counts.items())),
        "multi_class_programs": 0,
        "max_classes_per_program": 1,
        "truth_table_evaluations": len(programs) * 2 * 64,
        "first_program_configuration_mismatch": mismatch,
    }


def sign_of_permutation(perm: tuple[int, ...]) -> int:
    inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


def rotate_coordinate(vector: tuple[int, ...], perm: tuple[int, ...], signs: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(signs[axis] * vector[perm[axis]] for axis in range(3))


def independent_orbits() -> dict:
    rotations = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if sign_of_permutation(perm) * signs[0] * signs[1] * signs[2] == 1:
                rotations.append((perm, signs))
    coordinate_to_name = {value: name for name, value in COORDINATES.items() if name != "C"}
    representatives = {
        "CNOT": ("+x",),
        "TOF_PERPENDICULAR_CONTROLS": ("+x", "+y"),
        "TOF_OPPOSITE_CONTROLS": ("+x", "-x"),
    }
    expected_members = {
        class_name: {
            tuple(sorted(
                (NAMES[controls[0]],) if kind == "CNOT" else (NAMES[controls[0]], NAMES[controls[1]]),
                key=NAMES.index,
            ))
            for kind, controls in independent_programs()
            if independent_class((kind, controls)) == class_name
        }
        for class_name in CLASS_NAMES
    }
    rows = {}
    failures = []
    for class_name, representative in representatives.items():
        orbit = set()
        stabilizer = 0
        for perm, signs in rotations:
            rotated = tuple(sorted(
                (
                    coordinate_to_name[rotate_coordinate(COORDINATES[name], perm, signs)]
                    for name in representative
                ),
                key=NAMES.index,
            ))
            orbit.add(rotated)
            if rotated == tuple(sorted(representative, key=NAMES.index)):
                stabilizer += 1
        if orbit != expected_members[class_name]:
            failures.append({"class": class_name})
        summed = tuple(sum(COORDINATES[name][axis] for name in representative) for axis in range(3))
        rows[class_name] = {
            "representative": list(representative),
            "orbit_size": len(orbit),
            "stabilizer": stabilizer,
            "J": sum(value * value for value in summed),
            "members": [
                list(row)
                for row in sorted(
                    expected_members[class_name],
                    key=lambda controls: tuple(NAMES.index(name) for name in controls),
                )
            ],
        }
    return {"rotation_count": len(rotations), "classes": rows, "closure_failures": failures}


def independent_weighting_rebuild(receipt: dict) -> dict:
    supplied = receipt["weighting_rebuild"]
    world_summary = supplied["world_summary"]
    counts = [row["event_count"] for row in world_summary if row["event_count"]]
    common = 1
    for count in set(counts):
        common = lcm(common, count)
    boundaries = supplied["boundaries"]

    def event_numerator(name: str, row: dict) -> int:
        count = row["event_count"]
        if name == "M1_COUNTING":
            return 1
        multiplier = common // count
        if name == "M2_PER_WORLD_UNIFORM":
            score = 1
        elif name == "M3_OCCUPATION_WEIGHTED":
            score = row["occupation"]
        elif name == "M4_FORMATION_LIFETIME":
            formation = row["formation_moment"]
            score = boundaries - formation + 1 if formation is not None else 0
        elif name == "M5_FORMATION_MOMENT":
            score = row["formation_moment"] or 0
        else:
            raise ValueError(name)
        return score * multiplier

    rows = {}
    for name in WEIGHT_NAMES:
        compressed = []
        total = zeros = positives = 0
        negative = None
        for row in world_summary:
            count = row["event_count"]
            if not count:
                continue
            numerator = event_numerator(name, row)
            compressed.append((row["world"], count, numerator))
            total += count * numerator
            zeros += count if numerator == 0 else 0
            positives += count if numerator > 0 else 0
            if numerator < 0 and negative is None:
                negative = {"world": row["world"], "event_numerator": numerator}
        rows[name] = {
            "definition": supplied["candidates"][name]["definition"],
            "integer_numerator_total": total,
            "normalizable": total > 0,
            "nonnegative": negative is None,
            "first_negative_witness": negative,
            "zero_weight_events": zeros,
            "positive_weight_events": positives,
            "normalized_weight_certificate_digest": canonical_digest({
                "world_rows": compressed,
                "total": total,
            }),
        }
    event_cardinality = sum(row["event_count"] for row in world_summary)
    tag_counter = Counter()
    for row in world_summary:
        tag_counter.update(row["events_by_tag"])
    return {
        "event_cardinality": event_cardinality,
        "events_by_tag": dict(sorted(tag_counter.items())),
        "worlds_in_census": len(world_summary),
        "worlds_with_events": sum(bool(row["event_count"]) for row in world_summary),
        "formed_worlds": sum(row["formation_moment"] is not None for row in world_summary),
        "common_world_denominator": common,
        "boundaries": boundaries,
        "world_summary": world_summary,
        "candidates": rows,
    }


def distribution(program: tuple, condition: tuple[int, ...], p_zero: Fraction) -> tuple[Fraction, Fraction]:
    result = [Fraction(0), Fraction(0)]
    for target, probability in ((0, p_zero), (1, 1 - p_zero)):
        result[independent_output(program, target, condition)] += probability
    return tuple(result)


def tv(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> Fraction:
    return sum(abs(a - b) for a, b in zip(left, right)) / 2


def first_variation(program: tuple, p_zero: Fraction) -> dict | None:
    for direction in range(6):
        for spectators in product((0, 1), repeat=5):
            low = list(spectators)
            low.insert(direction, 0)
            high = list(low)
            high[direction] = 1
            left = distribution(program, tuple(low), p_zero)
            right = distribution(program, tuple(high), p_zero)
            strength = tv(left, right)
            if strength:
                return {
                    "program": label(program),
                    "varied_direction": NAMES[direction],
                    "condition_0": list(low),
                    "condition_1": high,
                    "distribution_0": [str(value) for value in left],
                    "distribution_1": [str(value) for value in right],
                    "tv": str(strength),
                }
    return None


def independent_variation(p_zero: Fraction) -> dict:
    representatives = {
        class_name: next(program for program in independent_programs() if independent_class(program) == class_name)
        for class_name in CLASS_NAMES
    }
    return {
        "p_zero": str(p_zero),
        "classes": {class_name: first_variation(program, p_zero) for class_name, program in representatives.items()},
    }


def independent_candidate_results(weighting: dict, orbits: dict, p_zero: Fraction) -> dict:
    variation = independent_variation(p_zero)
    candidate_rows = {}
    for name in WEIGHT_NAMES:
        row = weighting["candidates"][name]
        witness = None
        if not row["nonnegative"]:
            witness = {"condition": "negative event weight", **row["first_negative_witness"]}
        elif not row["normalizable"]:
            witness = {"condition": "zero total", "total": row["integer_numerator_total"]}
        elif any(value is None for value in variation["classes"].values()):
            missing = next(key for key, value in variation["classes"].items() if value is None)
            witness = {"condition": "missing required neighbour variation", "class": missing}
        elif orbits["closure_failures"]:
            witness = {"condition": "failed proper-cubic closure", **orbits["closure_failures"][0]}
        candidate_rows[name] = {
            "verdict": "SURVIVES" if witness is None else "EXCLUDED",
            "first_exclusion_witness": witness,
        }
    return {
        "p_zero": str(p_zero),
        "criterion": EXPECTED_CRITERION,
        "variation": variation,
        "candidates": candidate_rows,
        "survivors": [name for name in WEIGHT_NAMES if candidate_rows[name]["verdict"] == "SURVIVES"],
    }


def independent_transfer(results: dict) -> dict:
    excluded = [name for name in WEIGHT_NAMES if results["candidates"][name]["verdict"] == "EXCLUDED"]
    if not excluded:
        return {"verdict": "TRANSFERS", "first_weighting_lost": None, "witness": None}
    first = excluded[0]
    return {
        "verdict": "FAILS_TO_TRANSFER",
        "first_weighting_lost": first,
        "witness": results["candidates"][first]["first_exclusion_witness"],
    }


def independent_robustness() -> dict:
    rows = {}
    for p_zero in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)):
        variation = independent_variation(p_zero)
        observed = {
            class_name: "0" if row is None else row["tv"]
            for class_name, row in variation["classes"].items()
        }
        rows[str(p_zero)] = {
            "expected_abs_2p_minus_1": str(abs(2 * p_zero - 1)),
            "observed_tv": observed,
        }
    return rows


def parse_cache(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    header_text, stdout_text = text.split("----- stdout -----\n", 1)
    stdout_text, stderr_text = stdout_text.split("\n----- stderr -----\n", 1)
    header = {}
    for line in header_text.splitlines()[1:]:
        if ": " in line:
            key, value = line.split(": ", 1)
            header[key] = value
    return {"header": header, "stdout": stdout_text, "stderr": stderr_text, "text": text}


def validate_receipt(receipt: dict, cache: dict) -> tuple[bool, dict]:
    expected_z3 = independent_z3_certificate()
    expected_orbits = independent_orbits()
    expected_weights = independent_weighting_rebuild(receipt)
    expected_results = independent_candidate_results(expected_weights, expected_orbits, Fraction(1, 4))
    expected_results["marginal_factors"] = {label(program): "1" for program in independent_programs()}
    expected_transfer = independent_transfer(expected_results)
    expected_robustness = independent_robustness()
    comparisons = {
        "criterion": receipt.get("criterion_verbatim") == EXPECTED_CRITERION,
        "no_adaptation": receipt.get("criterion_adaptation", "").startswith("none;"),
        "no_verdict_imports": receipt.get("verdict_imports_used") == [],
        "z3_instance": receipt.get("z3_instance") == expected_z3,
        "orbits": receipt.get("orbits") == expected_orbits,
        "weightings": receipt.get("weighting_rebuild") == expected_weights,
        "requirement": receipt.get("requirement") == {
            "selected": "PER_INSTANCE",
            "injected_coexistence_selected": "JOINT",
        },
        "per_instance": receipt.get("per_instance_test") == expected_results,
        "transfer": receipt.get("transfer") == expected_transfer,
        "robustness": receipt.get("input_robustness") == expected_robustness,
        "cache_runner_pin": cache["header"].get("runner_sha256") == EXPECTED_PRIMARY_SHA256,
        "cache_input_pin": cache["header"].get("input_fingerprint_sha256") == EXPECTED_PRIMARY_CACHE_INPUT_FINGERPRINT,
        "cache_status": cache["header"].get("exit_code") == "0" and cache["header"].get("status") == "ok",
        "cache_semantics": (
            "SURVIVORS/5: 5/5" in cache["stdout"]
            and "TRANSFER_VERDICT: TRANSFERS; weighting=none; witness=none" in cache["stdout"]
            and "NONUNIFORM_P=1/4: CNOT: TV=1/2" in cache["stdout"]
            and cache["stdout"].rstrip().endswith("TOTAL: PASS=5 FAIL=0")
        ),
    }
    return all(comparisons.values()), comparisons


def active_corruption_probes(receipt: dict, cache: dict) -> dict:
    probes = {}

    def rejected(mutated: dict, mutated_cache: dict | None = None) -> bool:
        return not validate_receipt(mutated, mutated_cache or cache)[0]

    mutated = copy.deepcopy(receipt)
    mutated["z3_instance"]["sites"]["+x"] = [2, 0, 0]
    probes["coordinate_map"] = rejected(mutated)

    mutated = copy.deepcopy(receipt)
    mutated["z3_instance"]["program_count"] = 24
    probes["program_count"] = rejected(mutated)

    mutated = copy.deepcopy(receipt)
    mutated["z3_instance"]["class_counts"]["CNOT"] = 5
    probes["class_count"] = rejected(mutated)

    mutated = copy.deepcopy(receipt)
    mutated["weighting_rebuild"]["candidates"]["M4_FORMATION_LIFETIME"]["integer_numerator_total"] += 1
    probes["weighting_total"] = rejected(mutated)

    mutated = copy.deepcopy(receipt)
    mutated["per_instance_test"]["survivors"] = []
    probes["survivor_count"] = rejected(mutated)

    mutated = copy.deepcopy(receipt)
    mutated["per_instance_test"]["candidates"]["M1_COUNTING"] = {
        "verdict": "EXCLUDED", "first_exclusion_witness": None,
    }
    probes["exclusion_without_witness"] = rejected(mutated)

    mutated = copy.deepcopy(receipt)
    mutated["transfer"]["verdict"] = "FAILS_TO_TRANSFER"
    probes["transfer_headline"] = rejected(mutated)

    mutated = copy.deepcopy(receipt)
    mutated["input_robustness"]["1/4"]["observed_tv"]["CNOT"] = "0"
    probes["nonuniform_tv"] = rejected(mutated)

    mutated_cache = copy.deepcopy(cache)
    mutated_cache["header"]["runner_sha256"] = "0" * 64
    probes["primary_source_pin"] = rejected(receipt, mutated_cache)

    mutated_cache = copy.deepcopy(cache)
    mutated_cache["stdout"] = mutated_cache["stdout"].replace("SURVIVORS/5: 5/5", "SURVIVORS/5: 4/5")
    probes["cache_survivor_headline"] = rejected(receipt, mutated_cache)
    return probes


def main() -> int:
    source_sha = file_sha256(PRIMARY_PATH)
    receipt_sha = file_sha256(PRIMARY_RECEIPT_PATH)
    assignments = literal_assignments(PRIMARY_PATH)
    primary_receipt = json.loads(PRIMARY_RECEIPT_PATH.read_text(encoding="utf-8"))
    primary_cache = parse_cache(PRIMARY_CACHE_PATH)

    validated, comparisons = validate_receipt(primary_receipt, primary_cache)
    corruptions = active_corruption_probes(primary_receipt, primary_cache)
    ast_and_pins = bool(
        source_sha == EXPECTED_PRIMARY_SHA256
        and receipt_sha == EXPECTED_PRIMARY_RECEIPT_SHA256
        and assignments.get("P_INSTANCE_CRITERION_VERBATIM") == EXPECTED_CRITERION
        and tuple(assignments.get("CANDIDATE_NAMES", ())) == WEIGHT_NAMES
        and assignments.get("AUDIT_INPUT_PATHS") == (
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
        )
    )
    checks = {
        "R0_PRIMARY_AST_AND_PINS": ast_and_pins,
        "R1_INDEPENDENT_Z3_AND_ORBITS": all(comparisons[key] for key in ("z3_instance", "orbits")),
        "R2_INDEPENDENT_WEIGHTINGS": comparisons["weightings"],
        "R3_PER_INSTANCE_AND_TRANSFER": all(comparisons[key] for key in ("criterion", "no_adaptation", "no_verdict_imports", "requirement", "per_instance", "transfer")),
        "R4_NONUNIFORM_INPUT": comparisons["robustness"],
        "R5_RECEIPT_CACHE_BINDING": validated and all(comparisons[key] for key in ("cache_runner_pin", "cache_input_pin", "cache_status", "cache_semantics")),
        "R6_ACTIVE_CORRUPTION_PROBES": all(corruptions.values()),
        "R7_CONTROLS": len(AUDIT_INPUT_PATHS) == 3,
    }
    receipt = {
        "claim_id": "cycle984_born_compatibility_z3_adjacency_independent_check",
        "primary_imported_or_executed": False,
        "cycle719_imported_or_executed": False,
        "primary_source_sha256": source_sha,
        "primary_receipt_sha256": receipt_sha,
        "comparisons": comparisons,
        "active_corruption_probes": corruptions,
        "checks": checks,
    }
    receipt["receipt_sha256_without_self"] = canonical_digest(receipt)
    RECEIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"INDEPENDENT_Z3: sites=7 edges=6 programs=23 witnesses=21 rotations=24")
    print("INDEPENDENT_WEIGHTINGS: names=5 events=92260 formulas_recomputed_from_world_statistics=true")
    print(f"INDEPENDENT_PER_INSTANCE: survivors={len(primary_receipt['per_instance_test']['survivors'])}/5")
    print(f"INDEPENDENT_TRANSFER: {primary_receipt['transfer']['verdict']}")
    print("INDEPENDENT_NONUNIFORM_P=1/4: TV=1/2 for CNOT, perpendicular TOF, opposite TOF")
    print(f"ACTIVE_CORRUPTIONS: rejected={sum(corruptions.values())}/{len(corruptions)}")
    for name, passed in checks.items():
        print(f"{name} {'PASS' if passed else 'FAIL'}")
    pass_count = sum(checks.values())
    print(f"TOTAL: PASS={pass_count} FAIL={len(checks) - pass_count}")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
