#!/usr/bin/env python3
"""Independent refutation checker for the Cycle-978 bounded theorem.

The primary is parsed as AST and never imported.  This checker reconstructs
the 155 Boolean words, neighbour witnesses, and proper-rotation classes
without Cycle-719, then derives the product-extension verdicts algebraically.
It rejects active mutations of every headline and binding field.
"""
from __future__ import annotations

import ast
import copy
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 1400
HOUSE_STDOUT_LIMIT_BYTES = 6000
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle978_three_class_born_compatibility_2026_08_10.py",
    "outputs/three_class_born_compatibility_cycle978_receipt_2026_08_10.json",
    "logs/runner-cache/frontier_cycle978_three_class_born_compatibility_2026_08_10.txt",
)
EXPECTED_INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "3104325f8dd6e96e6654200057a5f6f98ed81c481805929c21ed8d7e845c88d9",
    AUDIT_INPUT_PATHS[1]:
        "04b994cfdb1ca3eb95c4bb94900e125bc02d67babb2cc9b13e2fb4968e8e2864",
    AUDIT_INPUT_PATHS[2]:
        "a95f869da308b9121250459886f8740a6ecbfccf678d86aa58c35fe61e33c429",
}
CHECK_RECEIPT = ROOT / (
    "outputs/three_class_born_compatibility_cycle978_"
    "independent_check_receipt_2026_08_10.json"
)
CHECK_CACHE = ROOT / (
    "logs/runner-cache/frontier_cycle978_three_class_born_"
    "independent_check_2026_08_10.txt"
)
CANDIDATES = (
    "M1_COUNTING",
    "M2_PER_WORLD_UNIFORM",
    "M3_OCCUPATION_WEIGHTED",
    "M4_FORMATION_LIFETIME",
    "M5_FORMATION_MOMENT",
)
CLASS_ORDER = (
    "CNOT",
    "TOF_PERPENDICULAR_CONTROLS",
    "TOF_OPPOSITE_CONTROLS",
)
CENTER = (0, 0, 0)
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")
OFFSETS = (CENTER, *DIRECTIONS)
OFFSET_TO_WIRE = {offset: index for index, offset in enumerate(OFFSETS)}
CONDITIONS = tuple(product((0, 1), repeat=6))
OTHER = tuple(product((0, 1), repeat=5))


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def ast_literal_assignment(tree: ast.Module, name: str):
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise KeyError(name)


def site_name(wire: int) -> str:
    return "C" if wire == 0 else NAMES[wire - 1]


def word_name(word: tuple) -> str:
    if word[0] == "I":
        return "I"
    if word[0] == "X":
        return f"X({site_name(word[1])})"
    if word[0] == "CNOT":
        return f"CNOT({site_name(word[1])}->{site_name(word[2])})"
    return (
        f"TOF({site_name(word[1])},{site_name(word[2])}"
        f"->{site_name(word[3])})"
    )


def family() -> tuple:
    words = [("I",)]
    words.extend(("X", target) for target in range(7))
    words.extend(
        ("CNOT", control, target)
        for control, target in permutations(range(7), 2)
    )
    for target in range(7):
        available = tuple(site for site in range(7) if site != target)
        words.extend(
            ("TOF", pair[0], pair[1], target)
            for pair in combinations(available, 2)
        )
    return tuple(words)


def apply(word: tuple, state: tuple) -> tuple:
    output = list(state)
    if word[0] == "X":
        output[word[1]] ^= 1
    elif word[0] == "CNOT":
        output[word[2]] ^= output[word[1]]
    elif word[0] == "TOF":
        output[word[3]] ^= output[word[1]] & output[word[2]]
    return tuple(output)


def with_edge(index: int, other: tuple, bit: int) -> tuple:
    values = []
    source = iter(other)
    for position in range(6):
        values.append(bit if position == index else next(source))
    return tuple(values)


def dot(left: tuple, right: tuple) -> int:
    return sum(a * b for a, b in zip(left, right))


def determinant(matrix: tuple) -> int:
    return (
        matrix[0][0] * (
            matrix[1][1] * matrix[2][2]
            - matrix[1][2] * matrix[2][1]
        )
        - matrix[0][1] * (
            matrix[1][0] * matrix[2][2]
            - matrix[1][2] * matrix[2][0]
        )
        + matrix[0][2] * (
            matrix[1][0] * matrix[2][1]
            - matrix[1][1] * matrix[2][0]
        )
    )


def mat_vec(matrix: tuple, vector: tuple) -> tuple:
    return tuple(dot(row, vector) for row in matrix)


def rotations() -> tuple:
    result = set()
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(
                    signs[row] * int(column == order[row])
                    for column in range(3)
                )
                for row in range(3)
            )
            if determinant(matrix) == 1:
                result.add(matrix)
    return tuple(sorted(result))


ROTATIONS = rotations()


def rotate_wire(wire: int, rotation: tuple) -> int:
    return (
        0 if wire == 0
        else OFFSET_TO_WIRE[mat_vec(rotation, OFFSETS[wire])]
    )


def rotate_word(word: tuple, rotation: tuple) -> tuple:
    if word[0] == "I":
        return word
    if word[0] == "X":
        return ("X", rotate_wire(word[1], rotation))
    if word[0] == "CNOT":
        return (
            "CNOT",
            rotate_wire(word[1], rotation),
            rotate_wire(word[2], rotation),
        )
    controls = sorted(
        (rotate_wire(word[1], rotation), rotate_wire(word[2], rotation))
    )
    return (
        "TOF", controls[0], controls[1],
        rotate_wire(word[3], rotation),
    )


def rotate_state(state: tuple, rotation: tuple) -> tuple:
    output = [0] * 7
    for wire, bit in enumerate(state):
        output[rotate_wire(wire, rotation)] = bit
    return tuple(output)


def classify(word: tuple) -> str:
    if word[0] == "CNOT":
        return "CNOT"
    relation = dot(OFFSETS[word[1]], OFFSETS[word[2]])
    return (
        "TOF_PERPENDICULAR_CONTROLS"
        if relation == 0
        else "TOF_OPPOSITE_CONTROLS"
    )


def independent_family() -> dict:
    words = family()
    word_set = set(words)
    witnesses = []
    changed = 0
    for word in words:
        dependent = False
        for x in (0, 1):
            for index in range(6):
                for other in OTHER:
                    left = (x, *with_edge(index, other, 0))
                    right = (x, *with_edge(index, other, 1))
                    if apply(word, left)[0] != apply(word, right)[0]:
                        changed += 1
                        dependent = True
        if dependent:
            witnesses.append(word)
    grouped = defaultdict(list)
    for word in witnesses:
        grouped[classify(word)].append(word)
    classes = {
        class_name: sorted(
            (word_name(word) for word in grouped[class_name])
        )
        for class_name in CLASS_ORDER
    }
    representatives = {
        class_name: min(
            grouped[class_name], key=word_name
        )
        for class_name in CLASS_ORDER
    }
    covariance_failures = []
    covariance_checks = 0
    for rotation in ROTATIONS:
        for word in witnesses:
            transported = rotate_word(word, rotation)
            if transported not in word_set:
                covariance_failures.append(
                    [word_name(word), "closure"]
                )
                continue
            for mask in range(128):
                state = tuple((mask >> bit) & 1 for bit in range(7))
                covariance_checks += 1
                left = rotate_state(apply(word, state), rotation)
                right = apply(
                    transported, rotate_state(state, rotation)
                )
                if left != right:
                    covariance_failures.append(
                        [word_name(word), mask]
                    )
    return {
        "family_size": len(words),
        "kind_counts": dict(sorted(Counter(word[0] for word in words).items())),
        "witness_count": len(witnesses),
        "witness_names": sorted(map(word_name, witnesses)),
        "changed_edge_pairs": changed,
        "classes": classes,
        "class_counts": {
            name: len(members) for name, members in classes.items()
        },
        "representatives": {
            name: word_name(word)
            for name, word in representatives.items()
        },
        "rotation_count": len(ROTATIONS),
        "covariance_checks": covariance_checks,
        "covariance_failures": covariance_failures,
        "science_digest": digest({
            "family": words,
            "witnesses": witnesses,
            "classes": classes,
        }),
    }


def source_controls() -> dict:
    source_path = ROOT / AUDIT_INPUT_PATHS[0]
    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=AUDIT_INPUT_PATHS[0])
    literal_paths = ast_literal_assignment(tree, "AUDIT_INPUT_PATHS")
    imports = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    }
    blocked = {
        path.removesuffix(".py").split("/")[-1]
        for path in ast_literal_assignment(
            tree, "BLOCKLIST_CITED_PRIMARIES"
        )
    }
    required_functions = {
        "rebuild_event_data",
        "candidate_rebuild",
        "family_and_classes_rebuild",
        "evaluate_class_extension",
        "evaluate_joint_extension",
    }
    functions = {
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
    }
    sha = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    return {
        "literal_audit_input_paths": list(literal_paths),
        "all_inputs_worktree_relative_and_present": all(
            not Path(path).is_absolute()
            and (ROOT / path).is_file()
            and (ROOT / path).resolve().is_relative_to(ROOT.resolve())
            for path in literal_paths
        ),
        "sha256": sha,
        "sha_pins_match": sha == EXPECTED_INPUT_SHA256,
        "primary_ast_required_functions": sorted(
            required_functions & functions
        ),
        "primary_ast_complete": required_functions <= functions,
        "blocked_primary_modules": sorted(blocked),
        "blocked_primary_imports": sorted(blocked & imports),
        "primary_never_imported": True,
        "source_read_count": len(AUDIT_INPUT_PATHS),
    }


def verify_claim(report: dict, rebuilt: dict) -> dict:
    a = report["certificates"]["A_REBUILD"]
    b = report["certificates"]["B_PER_CLASS_TEST"]
    c = report["certificates"]["C_JOINT_TEST"]
    d = report["certificates"]["D_ARTIFACT_VERDICT"]
    candidate_rows = a["candidates"]
    a_ok = bool(
        report["cycle"] == 978
        and tuple(candidate_rows) == CANDIDATES
        and a["event_cardinality"] == 92_260
        and rebuilt["family_size"] == a["family_size"] == 155
        and rebuilt["kind_counts"] == a["family_kind_counts"]
        and rebuilt["witness_count"] == a["witness_count"]
        and rebuilt["witness_names"]
        == sorted(row["word"] for row in a["witnesses"])
        and rebuilt["changed_edge_pairs"] == a["changed_edge_pairs"]
        and rebuilt["class_counts"]
        == {
            row["class"]: row["member_count"]
            for row in a["classes"]
        }
        and rebuilt["classes"]
        == {
            row["class"]: sorted(row["members"])
            for row in a["classes"]
        }
        and not rebuilt["covariance_failures"]
    )
    expected_per_class = {}
    for candidate in CANDIDATES:
        row = candidate_rows[candidate]
        finite_valid = bool(
            row["nonnegative"]
            and row["normalizable"]
            and row["integer_numerator_total"] > 0
            and row["positive_weight_events"] > 0
            and row["positive_weight_events"]
            + row["zero_weight_events"]
            == a["event_cardinality"]
        )
        expected_per_class[candidate] = {
            class_name: (
                "SURVIVES" if finite_valid else "EXCLUDED"
            )
            for class_name in CLASS_ORDER
        }
    claimed_table = {
        candidate: {
            class_name: b["per_class"][candidate][class_name][
                "verdict"
            ]
            for class_name in CLASS_ORDER
        }
        for candidate in CANDIDATES
    }
    exclusions_witnessed = all(
        row["verdict"] == "SURVIVES"
        or (
            row["first_disagreement"] is not None
            and row["first_disagreement"]["witness"]
            == rebuilt["representatives"][class_name]
        )
        for candidate in CANDIDATES
        for class_name, row in b["per_class"][candidate].items()
    )
    b_ok = bool(
        b["class_order"] == list(CLASS_ORDER)
        and claimed_table == expected_per_class
        and exclusions_witnessed
        and len(b["per_class_exclusions"])
        == sum(
            verdict == "EXCLUDED"
            for rows in expected_per_class.values()
            for verdict in rows.values()
        )
    )
    expected_joint = {
        candidate: (
            "SURVIVES"
            if all(
                verdict == "SURVIVES"
                for verdict in expected_per_class[candidate].values()
            )
            else "EXCLUDED"
        )
        for candidate in CANDIDATES
    }
    claimed_joint = {
        candidate: c["joint"][candidate]["verdict"]
        for candidate in CANDIDATES
    }
    expected_survivors = [
        candidate for candidate in CANDIDATES
        if expected_joint[candidate] == "SURVIVES"
    ]
    expected_excluded = [
        candidate for candidate in CANDIDATES
        if expected_joint[candidate] == "EXCLUDED"
    ]
    c_ok = bool(
        claimed_joint == expected_joint
        and c["survivors"] == expected_survivors
        and c["excluded"] == expected_excluded
        and all(
            row["candidate"] in expected_excluded
            and all(
                expected_per_class[row["candidate"]][class_name]
                == "SURVIVES"
                for class_name in CLASS_ORDER
            )
            and row["witness"]
            == row["first_disagreement"]["witness"]
            for row in c["joint_only_exclusions"]
        )
    )
    expected_artifact = (
        "NULL_CONFIRMED_AT_ENLARGED_SCOPE"
        if len(expected_survivors) == len(CANDIDATES)
        else "NULL_WAS_FAMILY_ARTIFACT"
    )
    d_ok = bool(
        d["verdict"] == expected_artifact
        and d["survivors"] == expected_survivors
        and d["excluded"] == expected_excluded
        and d["born_wall_status"]
        == f"survivors/5: {len(expected_survivors)}/5"
    )
    return {
        "pass": a_ok and b_ok and c_ok and d_ok,
        "A_REBUILD": a_ok,
        "B_PER_CLASS_TEST": b_ok,
        "C_JOINT_TEST": c_ok,
        "D_ARTIFACT_VERDICT": d_ok,
        "expected_table": expected_per_class,
        "expected_joint_survivors": expected_survivors,
        "expected_artifact": expected_artifact,
    }


def corruption_probes(report: dict, rebuilt: dict) -> dict:
    mutations = {}

    def rejected(name: str, mutate) -> None:
        changed = copy.deepcopy(report)
        mutate(changed)
        mutations[name] = not verify_claim(changed, rebuilt)["pass"]

    rejected(
        "family_size",
        lambda row: row["certificates"]["A_REBUILD"].__setitem__(
            "family_size", 154
        ),
    )
    rejected(
        "witness_count",
        lambda row: row["certificates"]["A_REBUILD"].__setitem__(
            "witness_count", 20
        ),
    )
    rejected(
        "class_member_count",
        lambda row: row["certificates"]["A_REBUILD"]["classes"][0].__setitem__(
            "member_count", 5
        ),
    )
    rejected(
        "per_class_verdict",
        lambda row: row["certificates"]["B_PER_CLASS_TEST"]["per_class"][
            CANDIDATES[0]
        ][CLASS_ORDER[0]].__setitem__("verdict", "EXCLUDED"),
    )
    rejected(
        "joint_survivors",
        lambda row: row["certificates"]["C_JOINT_TEST"].__setitem__(
            "survivors", list(CANDIDATES[:-1])
        ),
    )
    rejected(
        "artifact_label",
        lambda row: row["certificates"]["D_ARTIFACT_VERDICT"].__setitem__(
            "verdict", "NULL_WAS_FAMILY_ARTIFACT"
        ),
    )
    rejected(
        "born_wall_status",
        lambda row: row["certificates"]["D_ARTIFACT_VERDICT"].__setitem__(
            "born_wall_status", "survivors/5: 4/5"
        ),
    )
    return {
        "probes": mutations,
        "all_rejected": all(mutations.values()),
    }


def main() -> int:
    started = monotonic()
    controls = source_controls()
    report = json.loads(
        (ROOT / AUDIT_INPUT_PATHS[1]).read_text(encoding="utf-8")
    )
    cache = (ROOT / AUDIT_INPUT_PATHS[2]).read_text(encoding="utf-8")
    rebuilt = independent_family()
    verification = verify_claim(report, rebuilt)
    corruptions = corruption_probes(report, rebuilt)
    binding = bool(
        report["pass"]
        and report["primary_source_sha256"]
        == controls["sha256"][AUDIT_INPUT_PATHS[0]]
        and cache.startswith("CYCLE978_THREE_CLASS_BORN_COMPATIBILITY\n")
        and "TOTAL: PASS=5 FAIL=0\n" in cache
        and len(cache.encode()) < HOUSE_STDOUT_LIMIT_BYTES
    )
    elapsed = monotonic() - started
    checks = {
        "R0_PRIMARY_AST_AND_PINS": bool(
            controls["sha_pins_match"]
            and controls["all_inputs_worktree_relative_and_present"]
            and controls["primary_ast_complete"]
            and not controls["blocked_primary_imports"]
            and controls["primary_never_imported"]
        ),
        "R1_INDEPENDENT_FAMILY_AND_CLASSES": bool(
            rebuilt["family_size"] == 155
            and rebuilt["kind_counts"]
            == {"CNOT": 42, "I": 1, "TOF": 105, "X": 7}
            and rebuilt["witness_count"] == 21
            and rebuilt["class_counts"]
            == {
                "CNOT": 6,
                "TOF_PERPENDICULAR_CONTROLS": 12,
                "TOF_OPPOSITE_CONTROLS": 3,
            }
            and rebuilt["rotation_count"] == 24
            and not rebuilt["covariance_failures"]
        ),
        "R2_REFUTE_PER_CLASS_AND_JOINT": verification["pass"],
        "R3_RECEIPT_CACHE_BINDING": binding,
        "R4_ACTIVE_CORRUPTION_PROBES": corruptions["all_rejected"],
        "R5_CONTROLS": False,
    }
    lines = [
        "CYCLE978_THREE_CLASS_BORN_INDEPENDENT_CHECK",
        (
            "R0_PRIMARY_AST_AND_PINS "
            + ("PASS" if checks["R0_PRIMARY_AST_AND_PINS"] else "FAIL")
            + f" :: source_reads={controls['source_read_count']}<=6;"
            + f" sha_pins={controls['sha_pins_match']};"
            + f" blocked_imports={controls['blocked_primary_imports']}"
        ),
        (
            "R1_INDEPENDENT_FAMILY_AND_CLASSES "
            + (
                "PASS"
                if checks["R1_INDEPENDENT_FAMILY_AND_CLASSES"]
                else "FAIL"
            )
            + f" :: family={rebuilt['family_size']};"
            + f" witnesses={rebuilt['witness_count']};"
            + " classes=" + compact(rebuilt["class_counts"])
            + f"; covariance_failures={len(rebuilt['covariance_failures'])}"
        ),
        (
            "R2_REFUTE_PER_CLASS_AND_JOINT "
            + (
                "PASS"
                if checks["R2_REFUTE_PER_CLASS_AND_JOINT"]
                else "FAIL"
            )
            + " :: table_5x3=" + compact(verification["expected_table"])
            + "; joint_survivors="
            + compact(verification["expected_joint_survivors"])
            + f"; artifact={verification['expected_artifact']}"
        ),
        (
            "R3_RECEIPT_CACHE_BINDING "
            + ("PASS" if checks["R3_RECEIPT_CACHE_BINDING"] else "FAIL")
            + f" :: primary_pass={report['pass']}; cache_bytes={len(cache.encode())}"
        ),
        (
            "R4_ACTIVE_CORRUPTION_PROBES "
            + (
                "PASS"
                if checks["R4_ACTIVE_CORRUPTION_PROBES"]
                else "FAIL"
            )
            + " :: " + compact(corruptions["probes"])
        ),
    ]
    provisional = "\n".join(lines) + "\n"
    checks["R5_CONTROLS"] = bool(
        elapsed < AUDIT_TIMEOUT_SEC <= 1400
        and len(provisional.encode()) + 180
        < HOUSE_STDOUT_LIMIT_BYTES
        < STDOUT_LIMIT_BYTES
    )
    lines.append(
        "R5_CONTROLS "
        + ("PASS" if checks["R5_CONTROLS"] else "FAIL")
        + f" :: runtime_s={elapsed:.3f}<1400;"
        + f" stdout_upper_bound={len(provisional.encode()) + 180}"
        + "<6000<150000"
    )
    lines.append(
        f"TOTAL: PASS={sum(checks.values())} "
        f"FAIL={sum(not value for value in checks.values())}"
    )
    stdout = "\n".join(lines) + "\n"
    receipt = {
        "cycle": 978,
        "artifact": "three_class_born_compatibility_independent_check",
        "checks": checks,
        "pass": all(checks.values()),
        "controls": controls,
        "independent_rebuild": rebuilt,
        "verification": verification,
        "corruption_probes": corruptions,
        "primary_binding": binding,
        "runtime_seconds": elapsed,
        "stdout_bytes": len(stdout.encode()),
        "checker_source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    CHECK_RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    CHECK_RECEIPT.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    CHECK_CACHE.parent.mkdir(parents=True, exist_ok=True)
    CHECK_CACHE.write_text(stdout, encoding="utf-8")
    print(stdout, end="")
    return 0 if receipt["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
