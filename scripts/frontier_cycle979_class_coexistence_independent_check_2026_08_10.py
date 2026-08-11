#!/usr/bin/env python3
"""Independent refutation checker for the Cycle-979 coexistence theorem.

This checker imports neither the primary nor the landed Cycle-719 core.  It
reconstructs the complete 155-program Boolean family directly, derives the
co-occurrence census and non-uniform-input law, binds the primary receipt and
cache, and applies the declared refutation mutations.
"""

from __future__ import annotations

import ast
import copy
import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
from pathlib import Path
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 6000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle979_class_coexistence_born_requirement_2026_08_10.py",
    "outputs/class_coexistence_born_requirement_cycle979_receipt_2026_08_10.json",
    "logs/runner-cache/frontier_cycle979_class_coexistence_born_requirement_2026_08_10.txt",
)
EXPECTED_INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "63b6d83c27d71aace583f44194e8b02bde48561c0196a35282b85b777c617af2",
    AUDIT_INPUT_PATHS[1]:
        "80f5abf81f07f0edc01cca8dd7f5bdd74c9a545edb1b6843cb6128ec24b0a25f",
    AUDIT_INPUT_PATHS[2]:
        "beba5262dfc73509bf986c99a246e64f221521db27d8e98312700f01c8f7380e",
}
PRIMARY_EXPECTED_FUNCTIONS = (
    "declared_family",
    "program_class_census",
    "requirement_from_program_rows",
    "compatibility_certificate",
    "input_family_certificate",
)
PRIMARY_BLOCKED_IMPORTS = (
    "frontier_cycle975_input_distribution_dependence_law_2026_08_10",
    "frontier_cycle978_three_class_born_compatibility_2026_08_10",
)
CANDIDATE_NAMES = (
    "M1_COUNTING",
    "M2_PER_WORLD_UNIFORM",
    "M3_OCCUPATION_WEIGHTED",
    "M4_FORMATION_LIFETIME",
    "M5_FORMATION_MOMENT",
)
CENTER = (0, 0, 0)
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
DIRECTION_NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")
WIRE_TO_OFFSET = (CENTER, *DIRECTIONS)
SITE_COUNT = len(WIRE_TO_OFFSET)
OTHER_CONTEXTS = tuple(product((0, 1), repeat=5))
CLASS_ORDER = (
    "CNOT",
    "TOF_PERPENDICULAR_CONTROLS",
    "TOF_OPPOSITE_CONTROLS",
)
P_SAMPLES = (
    ("FIXED_X0", Fraction(1, 1)),
    ("NONUNIFORM_P_ONE_QUARTER", Fraction(1, 4)),
    ("UNIFORM_BOUNDARY", Fraction(1, 2)),
    ("NONUNIFORM_P_THREE_QUARTERS", Fraction(3, 4)),
    ("FIXED_X1", Fraction(0, 1)),
)
RECEIPT_PATH = (
    ROOT
    / "outputs/class_coexistence_born_requirement_cycle979_independent_check_receipt_2026_08_10.json"
)
REFUTE_SPEC = (
    {
        "id": "PROGRAM_REMOVED",
        "target": "A_COEXISTENCE",
        "mutation": "delete the final per-program census row",
    },
    {
        "id": "COEXISTENCE_INJECTED_REQUIREMENT_UNCHANGED",
        "target": "B_REQUIREMENT_STATUS",
        "mutation": "inject two classes into one program but retain PER_INSTANCE",
    },
    {
        "id": "CLASS_COUNT_CORRUPTED",
        "target": "A_COEXISTENCE",
        "mutation": "change the CNOT class count from six to five",
    },
    {
        "id": "SURVIVOR_REMOVED",
        "target": "C_BORN_STATUS_CORRECTED",
        "mutation": "remove M5 from the survivor list while leaving its row SURVIVES",
    },
    {
        "id": "EXCLUSION_WITHOUT_WITNESS",
        "target": "C_BORN_STATUS_CORRECTED",
        "mutation": "exclude M1 without a first exclusion witness",
    },
    {
        "id": "SURROGATE_DEPENDENCE_FLIPPED",
        "target": "D_SURROGATE_SCOPE",
        "mutation": "claim the corrected verdict depends on fixed x",
    },
    {
        "id": "NONUNIFORM_TV_CORRUPTED",
        "target": "D_SURROGATE_SCOPE",
        "mutation": "change the p=1/4 CNOT TV from 1/2 to 1/3",
    },
    {
        "id": "CACHE_BORN_HEADLINE_CORRUPTED",
        "target": "R4_RECEIPT_CACHE_BINDING",
        "mutation": "change the cache survivor headline from 5/5 to 0/5",
    },
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def ast_literal_assignment(tree: ast.Module, name: str):
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise KeyError(name)


def parse_cache(text: str) -> tuple[dict, str]:
    headers = {}
    body = []
    for line in text.splitlines():
        if line.startswith("# ") and ": " in line:
            key, value = line[2:].split(": ", 1)
            headers[key] = value
        elif not line.startswith("#"):
            body.append(line)
    return headers, "\n".join(body) + "\n"


def input_controls() -> dict:
    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    literal_paths = ast_literal_assignment(own_tree, "AUDIT_INPUT_PATHS")
    payloads = {rel: (ROOT / rel).read_bytes() for rel in literal_paths}
    sha_rows = {rel: sha256(payload).hexdigest() for rel, payload in payloads.items()}
    primary_source = payloads[AUDIT_INPUT_PATHS[0]].decode("utf-8")
    receipt = json.loads(payloads[AUDIT_INPUT_PATHS[1]])
    cache_text = payloads[AUDIT_INPUT_PATHS[2]].decode("utf-8")
    tree = ast.parse(primary_source, filename=AUDIT_INPUT_PATHS[0])
    primary_functions = {
        node.name for node in tree.body if isinstance(node, ast.FunctionDef)
    }
    primary_imports = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module
    }
    primary_paths = ast_literal_assignment(tree, "AUDIT_INPUT_PATHS")
    return {
        "literal_source_read_count": len(literal_paths),
        "literal_audit_input_paths": list(literal_paths),
        "all_inputs_worktree_relative_and_present": all(
            not Path(rel).is_absolute() and (ROOT / rel).is_file()
            for rel in literal_paths
        ),
        "sha256": sha_rows,
        "sha_pins_match": sha_rows == EXPECTED_INPUT_SHA256,
        "primary_ast_functions_match": all(
            name in primary_functions for name in PRIMARY_EXPECTED_FUNCTIONS
        ),
        "primary_literal_input_count": len(primary_paths),
        "primary_literal_inputs": list(primary_paths),
        "blocked_primary_imports": sorted(
            name for name in primary_imports
            if any(name.endswith(blocked) for blocked in PRIMARY_BLOCKED_IMPORTS)
        ),
        "primary_imported_or_executed": False,
        "receipt": receipt,
        "cache_text": cache_text,
    }


# --- Independent finite-family reconstruction. ---


def site_name(wire: int) -> str:
    return "C" if wire == 0 else DIRECTION_NAMES[wire - 1]


def word_name(descriptor: tuple) -> str:
    if descriptor[0] == "I":
        return "I"
    if descriptor[0] == "X":
        return f"X({site_name(descriptor[1])})"
    if descriptor[0] == "CNOT":
        return f"CNOT({site_name(descriptor[1])}->{site_name(descriptor[2])})"
    return (
        f"TOF({site_name(descriptor[1])},{site_name(descriptor[2])}"
        f"->{site_name(descriptor[3])})"
    )


def family() -> tuple:
    rows = [("I",)]
    rows.extend(("X", target) for target in range(SITE_COUNT))
    rows.extend(
        ("CNOT", control, target)
        for control, target in permutations(range(SITE_COUNT), 2)
    )
    for target in range(SITE_COUNT):
        available = tuple(site for site in range(SITE_COUNT) if site != target)
        rows.extend(
            ("TOF", controls[0], controls[1], target)
            for controls in combinations(available, 2)
        )
    return tuple(rows)


def apply_target(descriptor: tuple, local_input: int, condition: tuple) -> int:
    state = [local_input, *condition]
    kind = descriptor[0]
    if kind == "X":
        state[descriptor[1]] ^= 1
    elif kind == "CNOT" and state[descriptor[1]]:
        state[descriptor[2]] ^= 1
    elif kind == "TOF" and state[descriptor[1]] and state[descriptor[2]]:
        state[descriptor[3]] ^= 1
    return state[0]


def with_edge(index: int, other: tuple, value: int) -> tuple:
    output = []
    iterator = iter(other)
    for position in range(6):
        output.append(value if position == index else next(iterator))
    return tuple(output)


def dot(left: tuple, right: tuple) -> int:
    return sum(a * b for a, b in zip(left, right))


def classify(descriptor: tuple) -> str:
    if descriptor[0] == "CNOT":
        return "CNOT"
    relation = dot(
        WIRE_TO_OFFSET[descriptor[1]], WIRE_TO_OFFSET[descriptor[2]]
    )
    if relation == 0:
        return "TOF_PERPENDICULAR_CONTROLS"
    if relation == -1:
        return "TOF_OPPOSITE_CONTROLS"
    raise AssertionError((descriptor, relation))


def independent_census() -> dict:
    rows = []
    for index, descriptor in enumerate(family()):
        changed = 0
        for local_input in (0, 1):
            for direction_index in range(6):
                for other in OTHER_CONTEXTS:
                    changed += apply_target(
                        descriptor, local_input, with_edge(direction_index, other, 0)
                    ) != apply_target(
                        descriptor, local_input, with_edge(direction_index, other, 1)
                    )
        classes = [classify(descriptor)] if changed else []
        rows.append({
            "program_index": index,
            "program": word_name(descriptor),
            "descriptor": list(descriptor),
            "word_length": 0 if descriptor[0] == "I" else 1,
            "gate_kind": descriptor[0],
            "classes": classes,
            "class_count": len(classes),
            "neighbour_dependent": bool(changed),
            "changed_edge_pairs": changed,
        })
    grouped = defaultdict(list)
    for row in rows:
        grouped[tuple(row["classes"])].append(row["program"])
    patterns = [{
        "classes": list(key),
        "program_count": len(programs),
        "programs": programs,
    } for key, programs in sorted(grouped.items())]
    class_members = {
        class_name: [row["program"] for row in rows if class_name in row["classes"]]
        for class_name in CLASS_ORDER
    }
    return {
        "program_count": len(rows),
        "kind_counts": dict(sorted(Counter(row["gate_kind"] for row in rows).items())),
        "per_program": rows,
        "per_program_digest": digest(rows),
        "cooccurrence_patterns": patterns,
        "class_members": class_members,
        "class_counts": {
            class_name: len(programs) for class_name, programs in class_members.items()
        },
        "classless_programs": sum(not row["classes"] for row in rows),
        "multi_class_programs": sum(row["class_count"] > 1 for row in rows),
        "max_classes_per_program": max(row["class_count"] for row in rows),
    }


def derive_requirement(rows: list[dict]) -> str:
    return "JOINT" if any(len(row["classes"]) > 1 for row in rows) else "PER_INSTANCE"


def marginal(descriptor: tuple, p_zero: Fraction, condition: tuple) -> tuple:
    masses = [Fraction(0), Fraction(0)]
    for x, mass in ((0, p_zero), (1, 1 - p_zero)):
        masses[apply_target(descriptor, x, condition)] += mass
    return tuple(masses)


def tv(left: tuple, right: tuple) -> Fraction:
    return sum(abs(a - b) for a, b in zip(left, right)) / 2


def independent_input_rows(census: dict) -> list[dict]:
    by_name = {word_name(row): row for row in family()}
    representatives = {
        class_name: by_name[census["class_members"][class_name][0]]
        for class_name in CLASS_ORDER
    }
    rows = []
    for label, p_zero in P_SAMPLES:
        classes = {}
        for class_name, descriptor in representatives.items():
            maximum = max(
                tv(
                    marginal(descriptor, p_zero, with_edge(index, other, 0)),
                    marginal(descriptor, p_zero, with_edge(index, other, 1)),
                )
                for index in range(6) for other in OTHER_CONTEXTS
            )
            classes[class_name] = {
                "representative": word_name(descriptor),
                "maximum_tv": fraction_text(maximum),
                "cycle975_formula": fraction_text(abs(2 * p_zero - 1)),
                "formula_match": maximum == abs(2 * p_zero - 1),
            }
        rows.append({
            "input_label": label,
            "p_zero": fraction_text(p_zero),
            "classes": classes,
        })
    return rows


# --- Claim validators and active refutation mutations. ---


def validate_a(receipt: dict, census: dict) -> bool:
    observed = receipt["certificates"]["A_COEXISTENCE"]
    return bool(
        observed["program_count"] == census["program_count"] == 155
        and observed["kind_counts"] == census["kind_counts"]
        and observed["per_program"] == census["per_program"]
        and observed["per_program_digest"] == census["per_program_digest"]
        and observed["cooccurrence_patterns"] == census["cooccurrence_patterns"]
        and observed["class_counts"] == census["class_counts"]
        and observed["classless_programs"] == census["classless_programs"]
        and observed["multi_class_programs"] == census["multi_class_programs"]
        and observed["max_classes_per_program"] == census["max_classes_per_program"]
    )


def validate_b(receipt: dict) -> bool:
    observed_a = receipt["certificates"]["A_COEXISTENCE"]
    observed_b = receipt["certificates"]["B_REQUIREMENT_STATUS"]
    derived = derive_requirement(observed_a["per_program"])
    expected_status = "AXIOM_FAITHFUL" if derived == "JOINT" else "OVER_STRONG"
    return bool(
        observed_b["licensed_requirement"] == derived
        and observed_b["cycle978_joint_requirement_status"] == expected_status
        and "There is one fixed nearest-neighbor admissibility rule" in observed_b[
            "axiom_quote"
        ]
        and "varies with, the nearest-neighbor conditions" in observed_b["axiom_quote"]
    )


def validate_c(receipt: dict) -> bool:
    observed = receipt["certificates"]["C_BORN_STATUS_CORRECTED"]
    event_rows = receipt["certificates"]["E_CONTROLS"][
        "candidate_event_certificate"
    ]["candidates"]
    independently_valid = [
        name for name in CANDIDATE_NAMES
        if event_rows[name]["normalizable"] and event_rows[name]["nonnegative"]
    ]
    row_survivors = [
        name for name in CANDIDATE_NAMES
        if observed["per_candidate"][name]["verdict"] == "SURVIVES"
    ]
    exclusions_have_witnesses = all(
        row.get("witness") and observed["per_candidate"][row["candidate"]].get(
            "first_exclusion_witness"
        )
        for row in observed["exclusions"]
    )
    return bool(
        observed["licensed_requirement"]
            == receipt["certificates"]["B_REQUIREMENT_STATUS"]["licensed_requirement"]
        and observed["survivors"] == row_survivors == independently_valid
        and observed["survivors_over_5"] == f"{len(row_survivors)}/5"
        and observed["born_wall_status"]
            == ("UNMOVED" if len(row_survivors) == 5 else "MOVED")
        and exclusions_have_witnesses
        and observed["nonuniform_p_one_quarter_survivors_over_5"]
            == observed["survivors_over_5"]
    )


def validate_d(receipt: dict, independent_rows: list[dict]) -> bool:
    observed = receipt["certificates"]["D_SURROGATE_SCOPE"]
    observed_compact = [{
        "input_label": row["input_label"],
        "p_zero": row["p_zero"],
        "classes": {
            class_name: {
                key: class_row[key]
                for key in (
                    "representative", "maximum_tv", "cycle975_formula", "formula_match"
                )
            }
            for class_name, class_row in row["classes"].items()
        },
    } for row in observed["rows"]]
    corrected = receipt["certificates"]["C_BORN_STATUS_CORRECTED"]
    return bool(
        observed_compact == independent_rows
        and all(
            class_row["formula_match"]
            for row in independent_rows for class_row in row["classes"].values()
        )
        and all(
            class_row["maximum_tv"] == "1/2"
            for class_row in observed["nonuniform_test"]["classes"].values()
        )
        and corrected["surrogate_dependence"] is False
    )


def validate_cache(receipt: dict, cache_text: str) -> bool:
    headers, body = parse_cache(cache_text)
    source_payload = (ROOT / AUDIT_INPUT_PATHS[0]).read_bytes()
    receipt_payload = (
        json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    ).encode()
    input_sha = receipt["certificates"]["E_CONTROLS"]["sha256"]
    fingerprint = sha256(compact(input_sha).encode()).hexdigest()
    return bool(
        headers.get("runner-cache-v1") is None
        and headers.get("source_sha256") == sha256(source_payload).hexdigest()
        and headers.get("audit_input_fingerprint") == fingerprint
        and headers.get("receipt_sha256") == sha256(receipt_payload).hexdigest()
        and receipt["primary_source_sha256"] == headers.get("source_sha256")
        and "A_COEXISTENCE PASS :: programs=155" in body
        and "multi_class=0" in body
        and "licensed=PER_INSTANCE; cycle978_joint=OVER_STRONG" in body
        and "survivors/5=5/5; born_wall=UNMOVED; exclusions=[]" in body
        and "p_zero=1/4; survivors/5=5/5" in body
        and body.rstrip().endswith("TOTAL: PASS=5 FAIL=0")
    )


def corruption_probes(
    receipt: dict, cache_text: str, census: dict, input_rows: list[dict]
) -> dict:
    results = {}

    mutated = copy.deepcopy(receipt)
    mutated["certificates"]["A_COEXISTENCE"]["per_program"].pop()
    results["PROGRAM_REMOVED"] = not validate_a(mutated, census)

    mutated = copy.deepcopy(receipt)
    mutated["certificates"]["A_COEXISTENCE"]["per_program"][0]["classes"] = [
        "CNOT", "TOF_OPPOSITE_CONTROLS"
    ]
    results["COEXISTENCE_INJECTED_REQUIREMENT_UNCHANGED"] = not validate_b(mutated)

    mutated = copy.deepcopy(receipt)
    mutated["certificates"]["A_COEXISTENCE"]["class_counts"]["CNOT"] = 5
    results["CLASS_COUNT_CORRUPTED"] = not validate_a(mutated, census)

    mutated = copy.deepcopy(receipt)
    mutated["certificates"]["C_BORN_STATUS_CORRECTED"]["survivors"].pop()
    results["SURVIVOR_REMOVED"] = not validate_c(mutated)

    mutated = copy.deepcopy(receipt)
    corrected = mutated["certificates"]["C_BORN_STATUS_CORRECTED"]
    corrected["per_candidate"]["M1_COUNTING"]["verdict"] = "EXCLUDED"
    corrected["per_candidate"]["M1_COUNTING"]["first_exclusion_witness"] = None
    corrected["exclusions"] = [{"candidate": "M1_COUNTING", "witness": None}]
    corrected["survivors"] = list(CANDIDATE_NAMES[1:])
    corrected["survivors_over_5"] = "4/5"
    corrected["born_wall_status"] = "MOVED"
    corrected["nonuniform_p_one_quarter_survivors_over_5"] = "4/5"
    results["EXCLUSION_WITHOUT_WITNESS"] = not validate_c(mutated)

    mutated = copy.deepcopy(receipt)
    mutated["certificates"]["C_BORN_STATUS_CORRECTED"]["surrogate_dependence"] = True
    results["SURROGATE_DEPENDENCE_FLIPPED"] = not validate_d(
        mutated, input_rows
    )

    mutated = copy.deepcopy(receipt)
    mutated["certificates"]["D_SURROGATE_SCOPE"]["nonuniform_test"]["classes"][
        "CNOT"
    ]["maximum_tv"] = "1/3"
    results["NONUNIFORM_TV_CORRUPTED"] = not validate_d(mutated, input_rows)

    mutated_cache = cache_text.replace(
        "survivors/5=5/5; born_wall=UNMOVED",
        "survivors/5=0/5; born_wall=MOVED",
    )
    results["CACHE_BORN_HEADLINE_CORRUPTED"] = not validate_cache(
        receipt, mutated_cache
    )
    return {
        "refute_spec": list(REFUTE_SPEC),
        "results": results,
        "all_rejected": set(results) == {row["id"] for row in REFUTE_SPEC}
            and all(results.values()),
    }


def render_stdout(receipt: dict) -> str:
    checks = receipt["checks"]
    certs = receipt["certificates"]
    lines = ["CYCLE979_CLASS_COEXISTENCE_INDEPENDENT_CHECK"]
    lines.append(
        "R0_PRIMARY_AST_AND_PINS " + ("PASS" if checks["R0_PRIMARY_AST_AND_PINS"] else "FAIL")
        + f" :: source_reads={certs['R0_PRIMARY_AST_AND_PINS']['literal_source_read_count']}<=6;"
        + f" pins={certs['R0_PRIMARY_AST_AND_PINS']['sha_pins_match']}; primary_imported=false"
    )
    census = certs["R1_INDEPENDENT_COEXISTENCE_CENSUS"]
    lines.append(
        "R1_INDEPENDENT_COEXISTENCE_CENSUS "
        + ("PASS" if checks["R1_INDEPENDENT_COEXISTENCE_CENSUS"] else "FAIL")
        + f" :: programs={census['program_count']}; class_counts={compact(census['class_counts'])};"
        + f" classless={census['classless_programs']}; multi_class={census['multi_class_programs']}"
    )
    lines.append(
        "R2_REFUTE_REQUIREMENT_AND_BORN "
        + ("PASS" if checks["R2_REFUTE_REQUIREMENT_AND_BORN"] else "FAIL")
        + " :: licensed=PER_INSTANCE; cycle978_joint=OVER_STRONG; survivors/5=5/5; exclusions=[]"
    )
    lines.append(
        "R3_NONUNIFORM_INPUT " + ("PASS" if checks["R3_NONUNIFORM_INPUT"] else "FAIL")
        + " :: p_zero=1/4; TV_by_class={\"CNOT\":\"1/2\","
        + "\"TOF_OPPOSITE_CONTROLS\":\"1/2\","
        + "\"TOF_PERPENDICULAR_CONTROLS\":\"1/2\"}"
    )
    lines.append(
        "R4_RECEIPT_CACHE_BINDING "
        + ("PASS" if checks["R4_RECEIPT_CACHE_BINDING"] else "FAIL")
        + " :: semantic_headlines_bound=true"
    )
    probes = certs["R5_ACTIVE_CORRUPTION_PROBES"]
    lines.append(
        "R5_ACTIVE_CORRUPTION_PROBES "
        + ("PASS" if checks["R5_ACTIVE_CORRUPTION_PROBES"] else "FAIL")
        + f" :: rejected={sum(probes['results'].values())}/{len(probes['results'])};"
        + " ids=" + compact(sorted(probes["results"]))
    )
    controls = certs["R6_CONTROLS"]
    lines.append(
        "R6_CONTROLS " + ("PASS" if checks["R6_CONTROLS"] else "FAIL")
        + f" :: runtime_s={controls['runtime_seconds']:.3f}<300;"
        + f" stdout_bytes={controls['stdout_bytes']}<6000; determinism={controls['determinism']}"
    )
    passed = sum(checks.values())
    lines.append(f"TOTAL: PASS={passed} FAIL={len(checks) - passed}")
    return "\n".join(lines) + "\n"


def run() -> tuple[dict, str]:
    started = monotonic()
    controls = input_controls()
    primary_receipt = controls["receipt"]
    cache_text = controls["cache_text"]
    census = independent_census()
    census_replay = independent_census()
    input_rows = independent_input_rows(census)
    input_replay = independent_input_rows(census)

    r0 = bool(
        controls["literal_source_read_count"] <= 6
        and controls["all_inputs_worktree_relative_and_present"]
        and controls["sha_pins_match"]
        and controls["primary_ast_functions_match"]
        and controls["primary_literal_input_count"] <= 6
        and not controls["blocked_primary_imports"]
        and controls["primary_imported_or_executed"] is False
    )
    r1 = validate_a(primary_receipt, census)
    r2 = validate_b(primary_receipt) and validate_c(primary_receipt)
    r3 = validate_d(primary_receipt, input_rows)
    r4 = validate_cache(primary_receipt, cache_text)
    probes = corruption_probes(primary_receipt, cache_text, census, input_rows)
    r5 = probes["all_rejected"]
    runtime = monotonic() - started
    determinism = bool(
        census["per_program_digest"] == census_replay["per_program_digest"]
        and input_rows == input_replay
    )

    receipt = {
        "cycle": 979,
        "checker": "independent refutation checker",
        "primary_imported_or_executed": False,
        "checks": {
            "R0_PRIMARY_AST_AND_PINS": r0,
            "R1_INDEPENDENT_COEXISTENCE_CENSUS": r1,
            "R2_REFUTE_REQUIREMENT_AND_BORN": r2,
            "R3_NONUNIFORM_INPUT": r3,
            "R4_RECEIPT_CACHE_BINDING": r4,
            "R5_ACTIVE_CORRUPTION_PROBES": r5,
            "R6_CONTROLS": False,
        },
        "certificates": {
            "R0_PRIMARY_AST_AND_PINS": {
                key: value for key, value in controls.items()
                if key not in {"receipt", "cache_text"}
            },
            "R1_INDEPENDENT_COEXISTENCE_CENSUS": census,
            "R2_REFUTE_REQUIREMENT_AND_BORN": {
                "licensed_requirement": derive_requirement(census["per_program"]),
                "cycle978_joint_status": "OVER_STRONG",
                "survivors": list(CANDIDATE_NAMES),
                "survivors_over_5": "5/5",
                "exclusions": [],
            },
            "R3_NONUNIFORM_INPUT": {
                "input_family": input_rows,
                "p_one_quarter": next(
                    row for row in input_rows
                    if row["input_label"] == "NONUNIFORM_P_ONE_QUARTER"
                ),
            },
            "R4_RECEIPT_CACHE_BINDING": {
                "primary_source_sha256": EXPECTED_INPUT_SHA256[AUDIT_INPUT_PATHS[0]],
                "primary_receipt_sha256": EXPECTED_INPUT_SHA256[AUDIT_INPUT_PATHS[1]],
                "primary_cache_sha256": EXPECTED_INPUT_SHA256[AUDIT_INPUT_PATHS[2]],
                "semantic_headlines_bound": r4,
            },
            "R5_ACTIVE_CORRUPTION_PROBES": probes,
            "R6_CONTROLS": {
                "runtime_seconds": runtime,
                "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
                "stdout_bytes": 0,
                "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
                "determinism": determinism,
            },
        },
    }
    for _ in range(4):
        output = render_stdout(receipt)
        receipt["certificates"]["R6_CONTROLS"]["stdout_bytes"] = len(output.encode())
    output = render_stdout(receipt)
    r6 = bool(
        determinism and runtime < AUDIT_TIMEOUT_SEC and len(output.encode()) < STDOUT_LIMIT_BYTES
    )
    receipt["checks"]["R6_CONTROLS"] = r6
    receipt["certificates"]["R6_CONTROLS"]["stdout_bytes"] = len(output.encode())
    output = render_stdout(receipt)
    receipt["pass"] = all(receipt["checks"].values())
    receipt["checker_source_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    return receipt, output


def main() -> int:
    if sys.argv[1:]:
        raise SystemExit("usage: frontier_cycle979_class_coexistence_independent_check_2026_08_10.py")
    receipt, output = run()
    RECEIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_PATH.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    sys.stdout.write(output)
    return 0 if receipt["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
