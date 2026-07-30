#!/usr/bin/env python3
"""Independent checker for the Cycle 753 fixed-target X/CNOT theorem.

This checker does not import or parse the primary implementation.  It validates
the supplied fixture, reconstructs the landed tree with separate code, checks
the exact arithmetic, exhausts every word through width four, exhausts small
Prüfer families, and then requires the primary to succeed as a subprocess.
"""
from __future__ import annotations

from hashlib import sha256
import heapq
from itertools import product
import json
from math import factorial
from pathlib import Path
import subprocess
import sys
from time import perf_counter


AUDIT_TIMEOUT_SEC = 180
REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    "docs/FIXED_TARGET_X_CNOT_PREPARATION_COUNT_CYCLE753_"
    "BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
META_NOTE_PATH = (
    "docs/GENESIS_TREE_PRUFER_RANK_CYCLE753_META_NOTE_2026-07-28.md"
)
FIXTURE_PATH = "outputs/fixed_target_x_cnot_cycle753_fixture_2026_07_28.json"
PRIMARY_PATH = (
    "scripts/frontier_cycle753_genesis_selection_attempt_2026_07_28.py"
)
PARENT_NOTE_PATH = (
    "docs/GENESIS_WORD_SELF_VERIFICATION_CYCLE732_"
    "BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
PARENT_SOURCE_PATH = (
    "scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py"
)
AUDIT_INPUT_PATHS = (
    "docs/FIXED_TARGET_X_CNOT_PREPARATION_COUNT_CYCLE753_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/GENESIS_TREE_PRUFER_RANK_CYCLE753_META_NOTE_2026-07-28.md",
    "docs/GENESIS_WORD_SELF_VERIFICATION_CYCLE732_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "outputs/fixed_target_x_cnot_cycle753_fixture_2026_07_28.json",
    "scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py",
    "scripts/frontier_cycle753_genesis_selection_attempt_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

EXPECTED_SCHEMA = "cycle753_fixed_target_x_cnot_fixture_v1"
EXPECTED_SUPPORT = (
    6, 40, 109, 110, 111, 112, 113, 114, 116, 117, 118, 119,
    126, 127, 128, 129, 257, 258, 259, 260, 5815, 5949, 5951,
    5953, 5955, 5957, 5969,
)
EXPECTED_CODE = (
    21, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26,
)
EXPECTED_RAW_COUNT = (
    118567477908254066625631346005619254518349824000000000000
)
EXPECTED_CLASS_COUNT = 42277452950578284263485622772148731904
EXPECTED_RANK = 31766083475554533889333676095260538518
STDOUT_LIMIT_BYTES = 150 * 1024

Gate = tuple[str, tuple[int, ...]]
Word = tuple[Gate, ...]

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: object, detail: object = None) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: "
        f"{detail if detail is not None else passed}"
    )
    return passed


def file_sha256(relative: str) -> str:
    return sha256((REPO_ROOT / relative).read_bytes()).hexdigest()


def input_digest(
    replacement: tuple[str, bytes] | None = None,
) -> str:
    digest = sha256()
    for relative in AUDIT_INPUT_PATHS:
        payload = (REPO_ROOT / relative).read_bytes()
        if replacement is not None and replacement[0] == relative:
            payload = replacement[1]
        digest.update(relative.encode())
        digest.update(b"\0")
        digest.update(payload)
        digest.update(b"\0")
    return digest.hexdigest()


def validate_fixture(raw: object) -> dict[str, object]:
    if not isinstance(raw, dict) or set(raw) != {
        "blank_state",
        "landed_word",
        "provenance",
        "register_width",
        "schema",
        "supplied_model",
        "target_support",
    }:
        raise ValueError("fixture top-level schema mismatch")
    expected_model = {
        "alphabet": (
            "X(i) and ordered CNOT(control,target), control != target, "
            "at every register position"
        ),
        "cost": "one unit per X or CNOT",
        "equivalence": "adjacent swaps of semantically commuting gates",
        "landing_rule": (
            "the final bit string must equal the supplied target exactly"
        ),
    }
    if (
        raw["schema"] != EXPECTED_SCHEMA
        or raw["blank_state"] != 0
        or raw["register_width"] != 5979
        or tuple(raw["target_support"]) != EXPECTED_SUPPORT
        or raw["supplied_model"] != expected_model
    ):
        raise ValueError("fixture supplied theorem data mismatch")
    word = raw["landed_word"]
    if not isinstance(word, list) or len(word) != len(EXPECTED_SUPPORT):
        raise ValueError("fixture landed-word length mismatch")
    for record in word:
        if not isinstance(record, dict) or set(record) != {"kind", "wires"}:
            raise ValueError(("invalid gate record", record))
        kind = record["kind"]
        wires = record["wires"]
        if not isinstance(wires, list):
            raise ValueError(("invalid gate wires", record))
        if kind == "X":
            valid = len(wires) == 1
        elif kind == "CNOT":
            valid = len(wires) == 2 and wires[0] != wires[1]
        else:
            valid = False
        if not (
            valid
            and all(
                type(wire) is int and 0 <= wire < raw["register_width"]
                for wire in wires
            )
        ):
            raise ValueError(("gate outside supplied alphabet", record))
    return raw


def plain_word(fixture: dict[str, object]) -> Word:
    return tuple(
        (
            str(record["kind"]),
            tuple(int(wire) for wire in record["wires"]),
        )
        for record in fixture["landed_word"]
    )


def apply_gate(state: int, gate: Gate) -> int:
    kind, wires = gate
    if kind == "X":
        return state ^ (1 << wires[0])
    if kind == "CNOT":
        control, target = wires
        if (state >> control) & 1:
            return state ^ (1 << target)
        return state
    raise ValueError(("gate outside checker alphabet", gate))


def apply_word(state: int, word: Word) -> int:
    for gate in word:
        state = apply_gate(state, gate)
    return state


def gates_commute(left: Gate, right: Gate) -> bool:
    left_kind, left_wires = left
    right_kind, right_wires = right
    if left_kind == right_kind == "X":
        return True
    if left_kind == "X" and right_kind == "CNOT":
        return left_wires[0] != right_wires[0]
    if left_kind == "CNOT" and right_kind == "X":
        return right_wires[0] != left_wires[0]
    if left_kind == right_kind == "CNOT":
        left_control, left_target = left_wires
        right_control, right_target = right_wires
        return (
            left_target != right_control
            and right_target != left_control
        )
    raise ValueError((left, right))


def alphabet(width: int) -> tuple[Gate, ...]:
    return tuple(
        [("X", (wire,)) for wire in range(width)]
        + [
            ("CNOT", (control, target))
            for control in range(width)
            for target in range(width)
            if control != target
        ]
    )


def semantic_commutation_truth(width: int) -> bool:
    gates = alphabet(width)
    for left in gates:
        for right in gates:
            actual = all(
                apply_gate(apply_gate(state, left), right)
                == apply_gate(apply_gate(state, right), left)
                for state in range(1 << width)
            )
            if gates_commute(left, right) != actual:
                return False
    return True


def successful_words(width: int, length: int) -> tuple[Word, ...]:
    gates = alphabet(width)
    target = (1 << width) - 1
    return tuple(
        tuple(gates[index] for index in indices)
        for indices in product(range(len(gates)), repeat=length)
        if apply_word(
            0, tuple(gates[index] for index in indices)
        ) == target
    )


def commutation_component_count(words: tuple[Word, ...]) -> int:
    unseen = set(words)
    components = 0
    while unseen:
        components += 1
        stack = [unseen.pop()]
        while stack:
            word = stack.pop()
            for index in range(len(word) - 1):
                if not gates_commute(word[index], word[index + 1]):
                    continue
                moved = (
                    word[:index]
                    + (word[index + 1], word[index])
                    + word[index + 2:]
                )
                if moved in unseen:
                    unseen.remove(moved)
                    stack.append(moved)
    return components


def exhaustive_small_words() -> dict[int, dict[str, object]]:
    rows: dict[int, dict[str, object]] = {}
    for width in range(1, 5):
        counts = tuple(
            len(successful_words(width, length))
            for length in range(width + 1)
        )
        minimum_words = successful_words(width, width)
        rows[width] = {
            "success_counts_lengths_0_through_width": counts,
            "minimum_word_count": len(minimum_words),
            "commutation_class_count":
                commutation_component_count(minimum_words),
            "expected_minimum_word_count": factorial(width) ** 2,
            "expected_commutation_class_count":
                (width + 1) ** (width - 1),
        }
    return rows


def encode_prufer(
    edges: tuple[tuple[int, int], ...], vertex_count: int
) -> tuple[int, ...]:
    adjacency = [set() for _ in range(vertex_count)]
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    leaves = [
        vertex for vertex, neighbors in enumerate(adjacency)
        if len(neighbors) == 1
    ]
    heapq.heapify(leaves)
    code: list[int] = []
    for _ in range(vertex_count - 2):
        leaf = heapq.heappop(leaves)
        parent = next(iter(adjacency[leaf]))
        code.append(parent)
        adjacency[parent].remove(leaf)
        adjacency[leaf].clear()
        if len(adjacency[parent]) == 1:
            heapq.heappush(leaves, parent)
    return tuple(code)


def decode_prufer(
    code: tuple[int, ...], vertex_count: int
) -> tuple[tuple[int, int], ...]:
    if len(code) != vertex_count - 2:
        raise ValueError("Prüfer length mismatch")
    degree = [1] * vertex_count
    for vertex in code:
        if not 0 <= vertex < vertex_count:
            raise ValueError(("Prüfer digit", vertex))
        degree[vertex] += 1
    leaves = [
        vertex for vertex, value in enumerate(degree) if value == 1
    ]
    heapq.heapify(leaves)
    edges: list[tuple[int, int]] = []
    for parent in code:
        leaf = heapq.heappop(leaves)
        edges.append((min(leaf, parent), max(leaf, parent)))
        degree[leaf] -= 1
        degree[parent] -= 1
        if degree[parent] == 1:
            heapq.heappush(leaves, parent)
    remaining = [vertex for vertex, value in enumerate(degree) if value == 1]
    if len(remaining) != 2:
        raise ValueError(("Prüfer terminal leaves", remaining))
    edges.append((min(remaining), max(remaining)))
    return tuple(sorted(edges))


def exhaustive_small_prufer() -> dict[int, dict[str, int | bool]]:
    rows: dict[int, dict[str, int | bool]] = {}
    for vertex_count in range(2, 7):
        codes = tuple(
            product(range(vertex_count), repeat=vertex_count - 2)
        )
        trees = {decode_prufer(tuple(code), vertex_count) for code in codes}
        roundtrips = all(
            encode_prufer(decode_prufer(tuple(code), vertex_count),
                          vertex_count)
            == tuple(code)
            for code in codes
        )
        rows[vertex_count] = {
            "code_count": len(codes),
            "distinct_tree_count": len(trees),
            "expected": vertex_count ** (vertex_count - 2),
            "roundtrips": roundtrips,
        }
    return rows


def landed_tree(
    fixture: dict[str, object],
) -> dict[str, object]:
    support = tuple(int(wire) for wire in fixture["target_support"])
    label = {wire: index + 1 for index, wire in enumerate(support)}
    target = sum(1 << wire for wire in support)
    state = 0
    prepared: set[int] = set()
    edges: list[tuple[int, int]] = []
    weight_trace = [0]
    for index, gate in enumerate(plain_word(fixture)):
        kind, wires = gate
        if kind == "X":
            parent = 0
            child = wires[0]
        else:
            control, child = wires
            if control not in prepared:
                raise ValueError(("unprepared CNOT control", index, control))
            parent = label[control]
        if child not in label or child in prepared:
            raise ValueError(("invalid landed target step", index, child))
        previous_weight = state.bit_count()
        state = apply_gate(state, gate)
        if state.bit_count() != previous_weight + 1:
            raise ValueError(("nonmonotone landed step", index))
        prepared.add(child)
        edges.append((min(parent, label[child]), max(parent, label[child])))
        weight_trace.append(state.bit_count())
    canonical_edges = tuple(sorted(edges))
    if state != target or tuple(sorted(prepared)) != support:
        raise ValueError("landed word does not prepare supplied target")
    code = encode_prufer(canonical_edges, len(support) + 1)
    rank = 0
    for digit in code:
        rank = rank * (len(support) + 1) + digit
    return {
        "code": code,
        "edges": canonical_edges,
        "final_state": state,
        "rank": rank,
        "target": target,
        "weight_trace": tuple(weight_trace),
    }


def independent_counts(support_size: int) -> dict[str, object]:
    recurrence_factors = tuple(
        (support_size - prepared) * (prepared + 1)
        for prepared in range(support_size)
    )
    recurrence_count = 1
    for factor in recurrence_factors:
        recurrence_count *= factor
    class_product = 1
    for _ in range(support_size - 1):
        class_product *= support_size + 1
    return {
        "minimum_length": support_size,
        "raw_by_recurrence": recurrence_count,
        "raw_by_factorials": factorial(support_size) ** 2,
        "class_by_product": class_product,
        "class_by_power": (support_size + 1) ** (support_size - 1),
        "recurrence_factors": recurrence_factors,
    }


def run_primary() -> dict[str, object]:
    completed = subprocess.run(
        [sys.executable, str(REPO_ROOT / PRIMARY_PATH)],
        cwd=REPO_ROOT,
        capture_output=True,
        check=False,
        text=True,
        timeout=120,
    )
    lines = tuple(line for line in completed.stdout.splitlines() if line)
    if completed.returncode != 0 or not lines:
        raise RuntimeError(
            {
                "primary_returncode": completed.returncode,
                "primary_stdout_tail": lines[-10:],
                "primary_stderr_tail": completed.stderr.splitlines()[-10:],
            }
        )
    report = json.loads(lines[-1])
    if not isinstance(report, dict):
        raise TypeError("primary terminal JSON is not an object")
    return report


def emit_report(report: dict[str, object]) -> int:
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE753_FIXED_TARGET_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE753_FIXED_TARGET_INDEPENDENT_CHECK_FAIL"
    )
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(text.encode())))
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


def main() -> int:
    started = perf_counter()
    report: dict[str, object] = {
        "artifact_kind":
            "independent_conditional_fixed_target_x_cnot_checker",
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "claim_type": "bounded_theorem",
        "scientific_authority": "none",
    }
    try:
        fixture_raw = json.loads((REPO_ROOT / FIXTURE_PATH).read_text())
        fixture = validate_fixture(fixture_raw)
        base_digest = input_digest()
        mutated_fixture = json.loads(json.dumps(fixture))
        mutated_fixture["target_support"][0] = (
            mutated_fixture["target_support"][1]
        )
        mutation_rejected = False
        try:
            validate_fixture(mutated_fixture)
        except ValueError:
            mutation_rejected = True
        mutated_bytes = (
            json.dumps(mutated_fixture, sort_keys=True).encode()
        )
        mutated_digest = input_digest((FIXTURE_PATH, mutated_bytes))
        check(
            "A_literal_complete_input_packet_and_mutation_control",
            len(AUDIT_INPUT_PATHS) == 6
            and len(set(AUDIT_INPUT_PATHS)) == 6
            and all((REPO_ROOT / path).is_file()
                    for path in AUDIT_INPUT_PATHS)
            and base_digest != mutated_digest
            and mutation_rejected,
            {"declared_count": len(AUDIT_INPUT_PATHS)},
        )
        provenance = fixture["provenance"]
        parent_hashes = {
            PARENT_NOTE_PATH: file_sha256(PARENT_NOTE_PATH),
            PARENT_SOURCE_PATH: file_sha256(PARENT_SOURCE_PATH),
        }
        check(
            "B_reviewed_parent_provenance_is_byte_pinned",
            provenance == {
                "reviewed_cycle732_fix_commit":
                    "cbd2f199261fa073c2d7db7a6b34db6fb9792566",
                "source_note": {
                    "path": PARENT_NOTE_PATH,
                    "sha256": parent_hashes[PARENT_NOTE_PATH],
                },
                "source_runner": {
                    "path": PARENT_SOURCE_PATH,
                    "sha256": parent_hashes[PARENT_SOURCE_PATH],
                },
            },
            parent_hashes,
        )

        structure = landed_tree(fixture)
        check(
            "C_landed_word_independently_prepares_exact_target",
            structure["weight_trace"]
            == tuple(range(len(EXPECTED_SUPPORT) + 1))
            and len(structure["edges"]) == len(EXPECTED_SUPPORT),
            {
                "edge_count": len(structure["edges"]),
                "weight_trace": structure["weight_trace"],
            },
        )
        check(
            "D_landed_prufer_coordinate_matches_meta_convention",
            structure["code"] == EXPECTED_CODE
            and structure["rank"] == EXPECTED_RANK,
            {"code": structure["code"], "rank": structure["rank"]},
        )
        all_x = tuple(("X", (wire,)) for wire in EXPECTED_SUPPORT)
        check(
            "E_explicit_nonuniqueness_control",
            apply_word(0, all_x) == structure["target"]
            and all_x != plain_word(fixture),
            {"alternative_length": len(all_x)},
        )

        counts = independent_counts(len(EXPECTED_SUPPORT))
        check(
            "F_exact_raw_count_two_independent_forms",
            counts["raw_by_recurrence"]
            == counts["raw_by_factorials"]
            == EXPECTED_RAW_COUNT,
            counts["raw_by_recurrence"],
        )
        check(
            "G_exact_class_count_two_independent_forms",
            counts["class_by_product"]
            == counts["class_by_power"]
            == EXPECTED_CLASS_COUNT,
            counts["class_by_product"],
        )
        check(
            "H_semantic_commutation_predicate_truth_table",
            semantic_commutation_truth(4),
        )

        small_words = exhaustive_small_words()
        check(
            "I_complete_word_spaces_through_width_four",
            all(
                row["success_counts_lengths_0_through_width"][:-1]
                == (0,) * width
                and row["minimum_word_count"]
                == row["expected_minimum_word_count"]
                and row["commutation_class_count"]
                == row["expected_commutation_class_count"]
                for width, row in small_words.items()
            ),
            small_words,
        )
        small_prufer = exhaustive_small_prufer()
        check(
            "J_complete_prufer_families_through_six_vertices",
            all(
                row["code_count"] == row["distinct_tree_count"]
                == row["expected"]
                and row["roundtrips"] is True
                for row in small_prufer.values()
            ),
            small_prufer,
        )

        primary = run_primary()
        primary_theorem = primary.get("theorem", {})
        boundary = primary.get("claim_boundary", {})
        check(
            "K_primary_subprocess_passes_and_matches_independent_results",
            primary.get("pass") is True
            and primary.get("checks_failed") == 0
            and primary_theorem.get("minimum_length")
            == len(EXPECTED_SUPPORT)
            and primary_theorem.get("raw_minimum_word_count")
            == EXPECTED_RAW_COUNT
            and primary_theorem.get("class_count")
            == EXPECTED_CLASS_COUNT
            and primary.get("landed_coordinate", {}).get("code")
            == list(EXPECTED_CODE)
            and primary.get("landed_coordinate", {}).get("rank")
            == EXPECTED_RANK
            and primary.get("fixture_sha256") == file_sha256(FIXTURE_PATH),
            {
                "primary_terminal": primary.get("terminal"),
                "primary_report_sha256": primary.get("report_sha256"),
            },
        )
        check(
            "L_primary_scope_boundary_is_explicitly_narrow",
            boundary == {
                "analytic_not_exhaustive_search": True,
                "autonomous_selection_claimed": False,
                "axiom_consequence_claimed": False,
                "fixed_target_conditional_theorem": True,
                "physical_minimality_claimed": False,
                "route_independent_no_go_claimed": False,
                "translated_target_family_claimed": False,
            },
            boundary,
        )

        theorem_note = (REPO_ROOT / NOTE_PATH).read_text()
        meta_note = (REPO_ROOT / META_NOTE_PATH).read_text()
        check(
            "M_note_labels_and_boundaries_are_machine_visible",
            "Authority: none" in theorem_note
            and "Claim type: bounded_theorem" in theorem_note
            and "conditional logical-combinatorics statements"
            in theorem_note
            and "not a physical compilation" in theorem_note
            and "Claim type: meta" in meta_note
            and "rank is a coordinate" in meta_note
            and "not a derived physical number" in meta_note,
        )

        runtime = perf_counter() - started
        check(
            "OUTPUT_runtime_under_AUDIT_TIMEOUT",
            runtime < AUDIT_TIMEOUT_SEC,
            round(runtime, 6),
        )
        report.update(
            {
                "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
                "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
                "NOTE_PATH": NOTE_PATH,
                "META_NOTE_PATH": META_NOTE_PATH,
                "FIXTURE_PATH": FIXTURE_PATH,
                "fixture_sha256": file_sha256(FIXTURE_PATH),
                "input_manifest_sha256": base_digest,
                "parent_provenance_sha256": parent_hashes,
                "runtime_seconds": round(runtime, 6),
                "independent_counts": counts,
                "landed_coordinate": {
                    "code": structure["code"],
                    "rank": structure["rank"],
                    "status": "meta coordinate only",
                },
                "small_word_exhaustion": small_words,
                "small_prufer_exhaustion": small_prufer,
                "primary_report_sha256": primary["report_sha256"],
                "claim_boundary": {
                    "fixed_target_conditional_theorem": True,
                    "global_result_is_analytic": True,
                    "translated_target_family_claimed": False,
                    "physical_minimality_claimed": False,
                    "autonomous_selection_claimed": False,
                    "axiom_consequence_claimed": False,
                    "unique_word_or_class_claimed": False,
                    "route_independent_no_go_claimed": False,
                },
            }
        )
    except Exception as error:
        check(
            "UNEXPECTED_checker_exception",
            False,
            {"type": type(error).__name__, "message": str(error)},
        )
        report["error_type"] = type(error).__name__
        report["error"] = str(error)
        report["runtime_seconds"] = round(perf_counter() - started, 6)
    check(
        "OUTPUT_stdout_under_150KB",
        len(json.dumps(report, default=str).encode()) + 8192
        < STDOUT_LIMIT_BYTES,
    )
    return emit_report(report)


if __name__ == "__main__":
    raise SystemExit(main())
