#!/usr/bin/env python3
"""Independent refutation checker for the Cycle-982 true-Z^3 census.

This checker imports and executes neither the primary nor Cycle-719.  It binds
the primary source, receipt, and canonical cache; independently rebuilds the
seven-site graph, Boolean witness set, cubic action, orbit data, separator,
and routing counts; and demands rejection of declared corruptions.
"""

from __future__ import annotations

import ast
import copy
import json
import sys
from hashlib import sha1, sha256
from itertools import combinations, permutations, product
from pathlib import Path
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
CYCLE = 982
AUDIT_TIMEOUT_SEC = 300
HOUSE_STDOUT_LIMIT_BYTES = 6_000
STDOUT_LIMIT_BYTES = 150_000
BASE_ORIGIN_MAIN_COMMIT = "ea0968c71ad46c39c6dacb39f88a18780363b71f"

PRIMARY_PATH = "scripts/frontier_cycle982_z3_adjacency_dependence_classes_2026_08_11.py"
PRIMARY_RECEIPT_PATH = "outputs/z3_adjacency_dependence_classes_cycle982_receipt_2026_08_11.json"
PRIMARY_CACHE_PATH = "logs/runner-cache/frontier_cycle982_z3_adjacency_dependence_classes_2026_08_11.txt"
CHECKER_PATH = (
    "scripts/frontier_cycle982_z3_adjacency_dependence_classes_independent_check_2026_08_11.py"
)
RECEIPT_PATH = (
    "outputs/z3_adjacency_dependence_classes_cycle982_independent_check_receipt_2026_08_11.json"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle982_z3_adjacency_dependence_classes_2026_08_11.py",
    "outputs/z3_adjacency_dependence_classes_cycle982_receipt_2026_08_11.json",
    "logs/runner-cache/frontier_cycle982_z3_adjacency_dependence_classes_2026_08_11.txt",
)
EXPECTED_INPUT_SHA256 = {
    PRIMARY_PATH: "8b5fe04a9f5195bf152b3576cc139f2c61f31782bed829d1188ac8987dfec90c",
    PRIMARY_RECEIPT_PATH: "8a7988828b13903307cc5b34e4a76a9a30b4ba95c4f6278e41d4d20d8483b2b9",
    PRIMARY_CACHE_PATH: "ab17b298793d981da88667e4f5b3b1522392cf29a3e25627e20efec16141ca59",
}
EXPECTED_INPUT_BLOBS = {
    PRIMARY_PATH: "34b10d7d8c6e66cdc12ff08e9b33b2a96946ce99",
    PRIMARY_RECEIPT_PATH: "b8fd98cdf5c9f6d4f67e09e9454cd1e4afd2c516",
    PRIMARY_CACHE_PATH: "2c0785129922347b9792874e546085f21dbc7b11",
}
FORBIDDEN_IMPORT_FRAGMENTS = (
    "frontier_cycle719_two_rail_recurrent_controller_core",
    "frontier_cycle982_z3_adjacency_dependence_classes_2026_08_11",
    "cycle970", "cycle972", "cycle977", "cycle979", "cycle980",
)

CENTER = (0, 0, 0)
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
SITES = (CENTER, *DIRECTIONS)
NAMES = ("C", "+x", "-x", "+y", "-y", "+z", "-z")


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def l1(left: tuple, right: tuple) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def dot(left: tuple, right: tuple) -> int:
    return sum(a * b for a, b in zip(left, right))


def determinant(matrix: tuple) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def rotate(matrix: tuple, vector: tuple) -> tuple:
    return tuple(dot(row, vector) for row in matrix)


def rotations_as_direction_permutations() -> tuple:
    site_to_index = {site: index for index, site in enumerate(SITES)}
    actions = set()
    for axis_order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(signs[row] * int(column == axis_order[row]) for column in range(3))
                for row in range(3)
            )
            if determinant(matrix) != 1:
                continue
            actions.add(tuple(site_to_index[rotate(matrix, site)] for site in SITES))
    return tuple(sorted(actions))


ACTIONS = rotations_as_direction_permutations()


def family() -> tuple:
    return (
        (("I",), ("X", 0))
        + tuple(("CNOT", control, 0) for control in range(1, 7))
        + tuple(("TOF", a, b, 0) for a, b in combinations(range(1, 7), 2))
    )


def output(descriptor: tuple, x: int, neighbours: tuple) -> int:
    if descriptor[0] == "I":
        return x
    if descriptor[0] == "X":
        return x ^ 1
    if descriptor[0] == "CNOT":
        return x ^ neighbours[descriptor[1] - 1]
    return x ^ (
        neighbours[descriptor[1] - 1] & neighbours[descriptor[2] - 1]
    )


def is_witness(descriptor: tuple) -> bool:
    for x in (0, 1):
        for condition in product((0, 1), repeat=6):
            for index in range(6):
                flipped = list(condition)
                flipped[index] ^= 1
                if output(descriptor, x, condition) != output(descriptor, x, tuple(flipped)):
                    return True
    return False


def rotate_descriptor(descriptor: tuple, action: tuple) -> tuple:
    if descriptor[0] in ("I", "X"):
        return descriptor
    wires = tuple(action[wire] for wire in descriptor[1:])
    if descriptor[0] == "TOF":
        return ("TOF", *sorted(wires[:2]), wires[2])
    return (descriptor[0], *wires)


def invariant_j(descriptor: tuple) -> int:
    controls = (descriptor[1],) if descriptor[0] == "CNOT" else descriptor[1:3]
    summed = tuple(sum(SITES[wire][axis] for wire in controls) for axis in range(3))
    return dot(summed, summed)


def descriptor_name(descriptor: tuple) -> str:
    if descriptor[0] == "CNOT":
        return f"CNOT({NAMES[descriptor[1]]}->C)"
    if descriptor[0] == "TOF":
        return f"TOF({NAMES[descriptor[1]]},{NAMES[descriptor[2]]}->C)"
    return "I" if descriptor[0] == "I" else "X(C)"


def independent_expected() -> dict:
    semantic_edges = set(combinations(range(7), 2))
    z3_edges = {
        pair for pair in combinations(range(7), 2) if l1(SITES[pair[0]], SITES[pair[1]]) == 1
    }
    witnesses = tuple(row for row in family() if is_witness(row))
    remaining = set(witnesses)
    orbits = []
    while remaining:
        seed = min(remaining, key=descriptor_name)
        ambient = {rotate_descriptor(seed, action) for action in ACTIONS}
        members = ambient & set(witnesses)
        stabilizer = sum(rotate_descriptor(seed, action) == seed for action in ACTIONS)
        values = sorted({invariant_j(member) for member in members})
        if seed[0] == "CNOT":
            label = "CNOT"
        elif values == [0]:
            label = "TOF_OPPOSITE_CONTROLS"
        elif values == [2]:
            label = "TOF_PERPENDICULAR_CONTROLS"
        else:
            label = "UNCLASSIFIED"
        orbits.append({
            "class_label": label,
            "member_count": len(members),
            "effective_stabilizer_order": stabilizer,
            "J_values": values,
        })
        remaining -= members
    orbits.sort(key=lambda row: row["class_label"])
    # Landed expansion has one X primitive, one CNOT primitive, and a
    # 15-primitive TOF expansion containing 9 one-site and 6 two-site gates.
    # On the star, each TOF uses four distance-1 and two distance-2 pairs:
    # 9 + 4*(2*1-1) + 2*(2*2-1) = 19 routed NN gates.
    return {
        "semantic_edge_count": len(semantic_edges),
        "z3_edge_count": len(z3_edges),
        "relation_classification": (
            "z3_strict_subrelation_of_semantic_wiring"
            if z3_edges < semantic_edges else "unexpected_relation"
        ),
        "family_size": len(family()),
        "witness_count": len(witnesses),
        "witness_names": sorted(descriptor_name(row) for row in witnesses),
        "orbits": orbits,
        "group_order": len(ACTIONS),
        "expanded_primitive_count": 1 + 6 + 15 * 15,
        "routed_nn_gate_count": 1 + 6 + 15 * 19,
        "maximum_route_distance": 2,
        "maximum_touched_sites": 3,
    }


def parse_cache(payload: str) -> dict:
    stdout_marker = "----- stdout -----\n"
    stderr_marker = "\n----- stderr -----\n"
    if stdout_marker not in payload or stderr_marker not in payload:
        return {"valid_envelope": False}
    header, tail = payload.split(stdout_marker, 1)
    stdout, _stderr = tail.split(stderr_marker, 1)
    fields = {}
    for line in header.splitlines()[1:]:
        if ": " in line:
            key, value = line.split(": ", 1)
            fields[key] = value
    return {"valid_envelope": True, "fields": fields, "stdout": stdout}


def selected_primary_view(receipt: dict) -> dict:
    findings = receipt["findings"]
    adjacency = findings["A_ADJACENCY_MAP"]
    census = findings["B_Z3_WITNESS_CENSUS"]
    hosted = census["hosted_census"]
    orbit = None if hosted is None else hosted["orbit_decomposition"]
    return {
        "semantic_edge_count": adjacency["semantic_wiring_edge_count"],
        "z3_edge_count": adjacency["z3_edge_count"],
        "relation_classification": adjacency["relation_classification"],
        "is_quotient_map": adjacency["is_quotient_map"],
        "all_paths_nn": all(
            row["all_steps_z3_nearest_neighbour"]
            for row in adjacency["path_realization"]
        ),
        "family_size": census["family"]["family_size"],
        "hosted": census["route_host"]["all_words_routable"],
        "witness_count": None if hosted is None else hosted["witness_count"],
        "witness_names": [] if hosted is None else sorted(hosted["witness_names"]),
        "orbits": [] if orbit is None else [
            {
                "class_label": row["class_label"],
                "member_count": row["member_count"],
                "effective_stabilizer_order": row["effective_stabilizer_order"],
                "J_values": row["J_values"],
            }
            for row in orbit["orbits"]
        ],
        "group_order": None if orbit is None else orbit["effective_group_order"],
        "expanded_primitive_count": census["route_host"]["expanded_primitive_count"],
        "routed_nn_gate_count": census["route_host"]["routed_nn_gate_count"],
        "maximum_route_distance": census["route_host"]["maximum_route_distance"],
        "maximum_touched_sites": census["route_host"]["maximum_touched_sites"],
        "transfer": findings["C_STRUCTURE_TRANSFER"]["classification"],
        "full_infinite_claimed": findings["D_HONEST_SCOPE"]["full_infinite_z3_instance_claimed"],
        "scope_missing_count": len(findings["D_HONEST_SCOPE"]["not_supplied_by_this_instance"]),
    }


def validate(receipt: dict, cache_payload: str, expected: dict) -> tuple[bool, list[str]]:
    errors = []
    view = selected_primary_view(receipt)
    for key in (
        "semantic_edge_count", "z3_edge_count", "relation_classification",
        "family_size", "witness_count", "witness_names", "orbits", "group_order",
        "expanded_primitive_count", "routed_nn_gate_count",
        "maximum_route_distance", "maximum_touched_sites",
    ):
        if view[key] != expected[key]:
            errors.append(f"mismatch:{key}")
    if view["is_quotient_map"] is not False:
        errors.append("quotient_flag")
    if not view["all_paths_nn"]:
        errors.append("non_nn_path")
    if view["hosted"] is not True:
        errors.append("host_flag")
    if view["transfer"] != "transfers_exactly_on_the_declared_local_family":
        errors.append("transfer")
    if view["full_infinite_claimed"] is not False or view["scope_missing_count"] < 1:
        errors.append("honest_scope")
    if not all(receipt.get("checks", {}).values()) or not receipt.get("pass"):
        errors.append("primary_checks")
    cache = parse_cache(cache_payload)
    if not cache.get("valid_envelope"):
        errors.append("cache_envelope")
    else:
        fields = cache["fields"]
        if fields.get("runner") != PRIMARY_PATH:
            errors.append("cache_runner")
        if fields.get("runner_sha256") != receipt.get("primary_source_sha256"):
            errors.append("cache_source_pin")
        if fields.get("exit_code") != "0" or fields.get("status") != "ok":
            errors.append("cache_status")
        if sha256(cache["stdout"].encode()).hexdigest() != receipt.get("stdout_sha256"):
            errors.append("cache_stdout_pin")
        if "TOTAL: PASS=5 FAIL=0" not in cache["stdout"]:
            errors.append("cache_total")
    return not errors, errors


def mutation_campaign(receipt: dict, cache_payload: str, expected: dict) -> list[dict]:
    mutations = []

    def add(name: str, mutate):
        candidate = copy.deepcopy(receipt)
        candidate_cache = cache_payload
        result = mutate(candidate, candidate_cache)
        if isinstance(result, str):
            candidate_cache = result
        accepted, errors = validate(candidate, candidate_cache, expected)
        mutations.append({"name": name, "rejected": not accepted, "errors": errors})

    add("relation_classification", lambda row, cache: row["findings"]["A_ADJACENCY_MAP"].__setitem__("relation_classification", "relations_equal"))
    add("semantic_edge_count", lambda row, cache: row["findings"]["A_ADJACENCY_MAP"].__setitem__("semantic_wiring_edge_count", 6))
    add("hostability", lambda row, cache: row["findings"]["B_Z3_WITNESS_CENSUS"]["route_host"].__setitem__("all_words_routable", False))
    add("witness_count", lambda row, cache: row["findings"]["B_Z3_WITNESS_CENSUS"]["hosted_census"].__setitem__("witness_count", 20))
    add("orbit_size", lambda row, cache: row["findings"]["B_Z3_WITNESS_CENSUS"]["hosted_census"]["orbit_decomposition"]["orbits"][0].__setitem__("member_count", 5))
    add("stabilizer", lambda row, cache: row["findings"]["B_Z3_WITNESS_CENSUS"]["hosted_census"]["orbit_decomposition"]["orbits"][1].__setitem__("effective_stabilizer_order", 4))
    add("J_separator", lambda row, cache: row["findings"]["B_Z3_WITNESS_CENSUS"]["hosted_census"]["orbit_decomposition"]["orbits"][2].__setitem__("J_values", [0]))
    add("full_infinite_scope", lambda row, cache: row["findings"]["D_HONEST_SCOPE"].__setitem__("full_infinite_z3_instance_claimed", True))
    add("primary_source_pin", lambda row, cache: row.__setitem__("primary_source_sha256", "0" * 64))
    add("cache_headline", lambda row, cache: cache.replace("witnesses=21", "witnesses=20", 1))
    return mutations


def input_controls() -> dict:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    sha_rows = {path: sha256(payload).hexdigest() for path, payload in payloads.items()}
    blob_rows = {path: git_blob(payload) for path, payload in payloads.items()}
    source = (ROOT / CHECKER_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=CHECKER_PATH)
    imports = {
        alias.name for node in ast.walk(tree) if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module
    }
    forbidden = sorted(
        name for name in imports
        if any(fragment in name.lower() for fragment in FORBIDDEN_IMPORT_FRAGMENTS)
    )
    primary_tree = ast.parse(payloads[PRIMARY_PATH], filename=PRIMARY_PATH)
    primary_timeout = None
    for node in primary_tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "AUDIT_TIMEOUT_SEC"
            for target in node.targets
        ):
            primary_timeout = ast.literal_eval(node.value)
    return {
        "literal_audit_input_paths": list(AUDIT_INPUT_PATHS),
        "literal_source_read_count": len(AUDIT_INPUT_PATHS),
        "input_sha256": sha_rows,
        "input_git_blobs": blob_rows,
        "sha_pins_match": sha_rows == EXPECTED_INPUT_SHA256,
        "blob_pins_match": blob_rows == EXPECTED_INPUT_BLOBS,
        "all_inputs_relative_and_present": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "forbidden_imports": forbidden,
        "primary_imported_or_executed": False,
        "cycle719_imported_or_executed": False,
        "prior_cycle_text_or_ast_executed": False,
        "primary_ast_timeout_seconds": primary_timeout,
    }


def render_stdout(receipt: dict) -> str:
    expected = receipt["findings"]["independent_expected"]
    lines = [
        "CYCLE982_Z3_ADJACENCY_DEPENDENCE_CLASSES_INDEPENDENT_CHECK",
        "A_INDEPENDENT_RECONSTRUCTION " + ("PASS" if receipt["checks"]["A_INDEPENDENT_RECONSTRUCTION"] else "FAIL")
        + f" :: semantic_edges={expected['semantic_edge_count']}; z3_edges={expected['z3_edge_count']};"
        + f" witnesses={expected['witness_count']}; orbits={compact(expected['orbits'])}",
        "B_REFUTATION_POWER " + ("PASS" if receipt["checks"]["B_REFUTATION_POWER"] else "FAIL")
        + f" :: rejected={sum(row['rejected'] for row in receipt['findings']['mutations'])}/"
        + f"{len(receipt['findings']['mutations'])}",
        "C_ARTIFACT_BINDING " + ("PASS" if receipt["checks"]["C_ARTIFACT_BINDING"] else "FAIL")
        + f" :: source_receipt_cache_pins={receipt['controls']['sha_pins_match'] and receipt['controls']['blob_pins_match']};"
        + f" clean_validation={receipt['findings']['clean_validation']}",
        "D_PROVENANCE " + ("PASS" if receipt["checks"]["D_PROVENANCE"] else "FAIL")
        + f" :: primary_imported={receipt['controls']['primary_imported_or_executed']};"
        + f" cycle719_imported={receipt['controls']['cycle719_imported_or_executed']};"
        + f" prior_cycles_executed={receipt['controls']['prior_cycle_text_or_ast_executed']}",
        "E_CONTROLS " + ("PASS" if receipt["checks"]["E_CONTROLS"] else "FAIL")
        + f" :: source_reads={receipt['controls']['literal_source_read_count']}<=6;"
        + f" determinism={receipt['controls']['determinism_replay']};"
        + f" runtime_s={receipt['controls']['runtime_seconds']:.3f}<300",
    ]
    passed = sum(receipt["checks"].values())
    lines.append(f"TOTAL: PASS={passed} FAIL={len(receipt['checks']) - passed}")
    return "\n".join(lines) + "\n"


def run_once() -> tuple[dict, str]:
    controls = input_controls()
    primary_receipt = json.loads((ROOT / PRIMARY_RECEIPT_PATH).read_text(encoding="utf-8"))
    primary_cache = (ROOT / PRIMARY_CACHE_PATH).read_text(encoding="utf-8")
    expected = independent_expected()
    clean, clean_errors = validate(primary_receipt, primary_cache, expected)
    mutations = mutation_campaign(primary_receipt, primary_cache, expected)
    findings = {
        "independent_expected": expected,
        "clean_validation": clean,
        "clean_validation_errors": clean_errors,
        "mutations": mutations,
    }
    cache = parse_cache(primary_cache)
    binding = bool(
        controls["sha_pins_match"] and controls["blob_pins_match"]
        and clean and cache.get("valid_envelope")
        and cache.get("fields", {}).get("runner_sha256") == EXPECTED_INPUT_SHA256[PRIMARY_PATH]
    )
    provenance = bool(
        not controls["forbidden_imports"]
        and not controls["primary_imported_or_executed"]
        and not controls["cycle719_imported_or_executed"]
        and not controls["prior_cycle_text_or_ast_executed"]
    )
    checks = {
        "A_INDEPENDENT_RECONSTRUCTION": clean,
        "B_REFUTATION_POWER": bool(mutations) and all(row["rejected"] for row in mutations),
        "C_ARTIFACT_BINDING": binding,
        "D_PROVENANCE": provenance,
        "E_CONTROLS": bool(
            controls["literal_source_read_count"] <= 6
            and controls["all_inputs_relative_and_present"]
            and controls["primary_ast_timeout_seconds"] == 1400
        ),
    }
    return findings, checks


def run() -> tuple[dict, str]:
    started = monotonic()
    first_findings, first_checks = run_once()
    second_findings, second_checks = run_once()
    deterministic = first_findings == second_findings and first_checks == second_checks
    controls = input_controls()
    controls.update({
        "determinism_replay": deterministic,
        "runtime_seconds": monotonic() - started,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "house_stdout_limit_bytes": HOUSE_STDOUT_LIMIT_BYTES,
    })
    checks = dict(first_checks)
    checks["E_CONTROLS"] = bool(
        checks["E_CONTROLS"] and deterministic
        and controls["sha_pins_match"] and controls["blob_pins_match"]
        and controls["runtime_seconds"] < AUDIT_TIMEOUT_SEC
    )
    receipt = {
        "cycle": CYCLE,
        "artifact": "true Z3 adjacency dependence-class independent refutation checker",
        "audit_status_authority": "independent audit lane only",
        "integrity_policy": (
            "checks gate independent reconstruction, artifact binding, and mutation rejection only"
        ),
        "findings": first_findings,
        "science_digest": digest(first_findings["independent_expected"]),
        "controls": controls,
        "checks": checks,
    }
    receipt["checker_source_sha256"] = sha256((ROOT / CHECKER_PATH).read_bytes()).hexdigest()
    for _ in range(3):
        stdout = render_stdout(receipt)
        controls["stdout_bytes"] = len(stdout.encode())
    stdout = render_stdout(receipt)
    if len(stdout.encode()) >= HOUSE_STDOUT_LIMIT_BYTES:
        receipt["checks"]["E_CONTROLS"] = False
        stdout = render_stdout(receipt)
    receipt["pass"] = all(receipt["checks"].values())
    receipt["stdout_sha256"] = sha256(stdout.encode()).hexdigest()
    return receipt, stdout


def main() -> int:
    if sys.argv[1:]:
        raise SystemExit(f"usage: {Path(__file__).name}")
    receipt, stdout = run()
    receipt_path = ROOT / RECEIPT_PATH
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    sys.stdout.write(stdout)
    return 0 if receipt["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
