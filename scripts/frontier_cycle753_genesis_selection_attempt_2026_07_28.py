#!/usr/bin/env python3
"""Cycle 753: a conditional fixed-target X/CNOT counting theorem.

The fixture supplies one bit target, a full-placement logical X/CNOT alphabet,
unit gate cost, exact landing, and adjacent semantic commutation.  This runner
checks the supplied landed word and evaluates the analytic minimum-word and
tree-class counts.  It does not import or execute the proposal-only Cycle 732
stack, claim a translated target family, or infer physical/axiom selection.
"""
from __future__ import annotations

from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import sys
from time import perf_counter


AUDIT_TIMEOUT_SEC = 120
REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    "docs/FIXED_TARGET_X_CNOT_PREPARATION_COUNT_CYCLE753_"
    "BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
META_NOTE_PATH = (
    "docs/GENESIS_TREE_PRUFER_RANK_CYCLE753_META_NOTE_2026-07-28.md"
)
FIXTURE_PATH = "outputs/fixed_target_x_cnot_cycle753_fixture_2026_07_28.json"
CHECKER_PATH = (
    "scripts/frontier_cycle753_selection_independent_check_2026_07_28.py"
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
    "scripts/frontier_cycle753_selection_independent_check_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

EXPECTED_SCHEMA = "cycle753_fixed_target_x_cnot_fixture_v1"
EXPECTED_SUPPORT = (
    6, 40, 109, 110, 111, 112, 113, 114, 116, 117, 118, 119,
    126, 127, 128, 129, 257, 258, 259, 260, 5815, 5949, 5951,
    5953, 5955, 5957, 5969,
)
EXPECTED_SUPPORT_SIZE = len(EXPECTED_SUPPORT)
EXPECTED_MODEL = {
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
EXPECTED_CODE = (
    21, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26,
)
EXPECTED_RANK = 31766083475554533889333676095260538518
STDOUT_LIMIT_BYTES = 150 * 1024

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool, detail: object = None) -> bool:
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


def declared_input_digest(replacement: tuple[str, bytes] | None = None) -> str:
    digest = sha256()
    for relative in AUDIT_INPUT_PATHS:
        payload = (REPO_ROOT / relative).read_bytes()
        if replacement is not None and relative == replacement[0]:
            payload = replacement[1]
        digest.update(relative.encode())
        digest.update(b"\0")
        digest.update(payload)
        digest.update(b"\0")
    return digest.hexdigest()


def load_fixture() -> dict[str, object]:
    raw = json.loads((REPO_ROOT / FIXTURE_PATH).read_text())
    if set(raw) != {
        "blank_state",
        "landed_word",
        "provenance",
        "register_width",
        "schema",
        "supplied_model",
        "target_support",
    }:
        raise ValueError("fixture top-level schema mismatch")
    if raw["schema"] != EXPECTED_SCHEMA or raw["blank_state"] != 0:
        raise ValueError("fixture identity mismatch")
    width = raw["register_width"]
    support = raw["target_support"]
    if (
        not isinstance(width, int)
        or width <= 0
        or not isinstance(support, list)
        or len(support) != EXPECTED_SUPPORT_SIZE
        or support != sorted(set(support))
        or tuple(support) != EXPECTED_SUPPORT
        or any(not isinstance(wire, int) or not 0 <= wire < width
               for wire in support)
        or raw["supplied_model"] != EXPECTED_MODEL
    ):
        raise ValueError("invalid supplied register/target")
    word = raw["landed_word"]
    if not isinstance(word, list) or len(word) != EXPECTED_SUPPORT_SIZE:
        raise ValueError("invalid supplied landed word")
    for gate in word:
        if not isinstance(gate, dict) or set(gate) != {"kind", "wires"}:
            raise ValueError("invalid gate record")
        kind, wires = gate["kind"], gate["wires"]
        if kind == "X":
            valid = (
                isinstance(wires, list)
                and len(wires) == 1
                and isinstance(wires[0], int)
                and 0 <= wires[0] < width
            )
        elif kind == "CNOT":
            valid = (
                isinstance(wires, list)
                and len(wires) == 2
                and all(isinstance(wire, int) and 0 <= wire < width
                        for wire in wires)
                and wires[0] != wires[1]
            )
        else:
            valid = False
        if not valid:
            raise ValueError(("invalid supplied gate", gate))
    return raw


def apply_gate(state: int, kind: str, wires: tuple[int, ...]) -> int:
    if kind == "X":
        return state ^ (1 << wires[0])
    if kind == "CNOT":
        control, target = wires
        return state ^ (1 << target) if (state >> control) & 1 else state
    raise ValueError(("outside supplied alphabet", kind))


def apply_word(
    state: int, word: tuple[tuple[str, tuple[int, ...]], ...]
) -> int:
    for kind, wires in word:
        state = apply_gate(state, kind, wires)
    return state


def prufer_code(
    edges: tuple[tuple[int, int], ...], vertex_count: int
) -> tuple[int, ...]:
    adjacency = {vertex: set() for vertex in range(vertex_count)}
    for left, right in edges:
        if left == right or left not in adjacency or right not in adjacency:
            raise ValueError(("invalid tree edge", left, right))
        adjacency[left].add(right)
        adjacency[right].add(left)
    if len(edges) != vertex_count - 1:
        raise ValueError("tree edge count mismatch")
    code: list[int] = []
    for _ in range(vertex_count - 2):
        leaves = [vertex for vertex, neighbors in adjacency.items()
                  if len(neighbors) == 1]
        if not leaves:
            raise ValueError("not a tree")
        leaf = min(leaves)
        parent = next(iter(adjacency[leaf]))
        code.append(parent)
        adjacency[parent].remove(leaf)
        adjacency[leaf].clear()
    if sum(bool(neighbors) for neighbors in adjacency.values()) != 2:
        raise ValueError("tree did not reduce to one edge")
    return tuple(code)


def landed_structure(
    fixture: dict[str, object],
) -> dict[str, object]:
    support = tuple(int(wire) for wire in fixture["target_support"])
    labels = {wire: index + 1 for index, wire in enumerate(support)}
    target = sum(1 << wire for wire in support)
    word = tuple(
        (str(gate["kind"]), tuple(int(wire) for wire in gate["wires"]))
        for gate in fixture["landed_word"]
    )
    state = int(fixture["blank_state"])
    prepared: set[int] = set()
    edges: list[tuple[int, int]] = []
    weights = [state.bit_count()]
    failures: list[str] = []
    for index, (kind, wires) in enumerate(word):
        if kind == "X":
            parent, new_wire = 0, wires[0]
        else:
            control, new_wire = wires
            if control not in prepared:
                failures.append(f"gate {index}: unprepared control")
            parent = labels.get(control, -1)
        if new_wire not in labels:
            failures.append(f"gate {index}: target outside supplied support")
        if new_wire in prepared:
            failures.append(f"gate {index}: target prepared twice")
        if parent < 0:
            failures.append(f"gate {index}: invalid parent")
        before = state.bit_count()
        state = apply_gate(state, kind, wires)
        if state.bit_count() != before + 1:
            failures.append(f"gate {index}: not a +1 weight step")
        prepared.add(new_wire)
        if parent >= 0 and new_wire in labels:
            edges.append((parent, labels[new_wire]))
        weights.append(state.bit_count())
    canonical_edges = tuple(
        sorted((min(left, right), max(left, right)) for left, right in edges)
    )
    code = prufer_code(canonical_edges, len(support) + 1)
    rank = 0
    for digit in code:
        rank = rank * (len(support) + 1) + digit
    return {
        "code": code,
        "edges": canonical_edges,
        "failures": tuple(failures),
        "final_state": state,
        "landed_word": word,
        "prepared_support": tuple(sorted(prepared)),
        "rank": rank,
        "target": target,
        "weight_trace": tuple(weights),
    }


def count_theorem(support_size: int) -> dict[str, object]:
    recurrence = tuple(
        (support_size - prepared) * (prepared + 1)
        for prepared in range(support_size)
    )
    raw_by_recurrence = 1
    for factor in recurrence:
        raw_by_recurrence *= factor
    raw_by_factorials = factorial(support_size) ** 2
    class_by_product = 1
    for _ in range(support_size - 1):
        class_by_product *= support_size + 1
    class_by_power = (support_size + 1) ** (support_size - 1)
    return {
        "class_count": class_by_power,
        "class_count_crosscheck": class_by_product,
        "minimum_length": support_size,
        "raw_minimum_word_count": raw_by_factorials,
        "raw_recurrence_factors": recurrence,
        "raw_word_count_crosscheck": raw_by_recurrence,
    }


def emit_report(report: dict[str, object]) -> int:
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE753_FIXED_TARGET_X_CNOT_COUNT_PASS"
        if report["pass"]
        else "CYCLE753_FIXED_TARGET_X_CNOT_COUNT_FAIL"
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
        "artifact_kind": "conditional_fixed_target_x_cnot_counting_theorem",
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "claim_type": "bounded_theorem",
        "scientific_authority": "none",
    }
    try:
        fixture = load_fixture()
        provenance = fixture["provenance"]
        parent_note = provenance["source_note"]
        parent_runner = provenance["source_runner"]
        parent_hashes = {
            PARENT_NOTE_PATH: file_sha256(PARENT_NOTE_PATH),
            PARENT_SOURCE_PATH: file_sha256(PARENT_SOURCE_PATH),
        }
        expected_provenance = {
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
        }
        check(
            "A_fixture_schema_and_fixed_target",
            fixture["schema"] == EXPECTED_SCHEMA
            and len(fixture["target_support"]) == EXPECTED_SUPPORT_SIZE,
            {
                "register_width": fixture["register_width"],
                "support_size": len(fixture["target_support"]),
            },
        )
        check(
            "B_reviewed_parent_provenance_bytes_match",
            provenance == expected_provenance
            and parent_note == expected_provenance["source_note"]
            and parent_runner == expected_provenance["source_runner"],
            parent_hashes,
        )
        base_digest = declared_input_digest()
        mutation_payload = (
            (REPO_ROOT / PARENT_SOURCE_PATH).read_bytes()
            + b"\n# in-memory mutation control\n"
        )
        mutated_digest = declared_input_digest(
            (PARENT_SOURCE_PATH, mutation_payload)
        )
        check(
            "C_complete_literal_input_packet_and_mutation_control",
            len(AUDIT_INPUT_PATHS) == 6
            and len(set(AUDIT_INPUT_PATHS)) == 6
            and all((REPO_ROOT / path).is_file()
                    for path in AUDIT_INPUT_PATHS)
            and base_digest != mutated_digest,
            {"declared_count": len(AUDIT_INPUT_PATHS)},
        )

        structure = landed_structure(fixture)
        support = tuple(int(wire) for wire in fixture["target_support"])
        check(
            "D_landed_word_exactly_prepares_supplied_target",
            not structure["failures"]
            and structure["final_state"] == structure["target"]
            and structure["prepared_support"] == support
            and structure["weight_trace"]
            == tuple(range(EXPECTED_SUPPORT_SIZE + 1)),
            {
                "failures": structure["failures"],
                "weight_trace": structure["weight_trace"],
            },
        )
        check(
            "E_landed_word_is_one_labeled_tree",
            len(structure["edges"]) == EXPECTED_SUPPORT_SIZE
            and len(structure["code"]) == EXPECTED_SUPPORT_SIZE - 1,
            {
                "edge_count": len(structure["edges"]),
                "code_length": len(structure["code"]),
            },
        )

        theorem = count_theorem(EXPECTED_SUPPORT_SIZE)
        check(
            "F_weight_lower_bound_is_27",
            theorem["minimum_length"] == EXPECTED_SUPPORT_SIZE,
            theorem["minimum_length"],
        )
        check(
            "G_raw_minimum_word_count_exact_arithmetic_forms_agree",
            theorem["raw_minimum_word_count"]
            == theorem["raw_word_count_crosscheck"]
            == factorial(EXPECTED_SUPPORT_SIZE) ** 2,
            theorem["raw_minimum_word_count"],
        )
        check(
            "H_commutation_class_count_exact_evaluations_agree",
            theorem["class_count"] == theorem["class_count_crosscheck"]
            == (EXPECTED_SUPPORT_SIZE + 1) ** (EXPECTED_SUPPORT_SIZE - 1),
            theorem["class_count"],
        )
        check(
            "I_landed_coordinate_matches_declared_meta_convention",
            structure["code"] == EXPECTED_CODE
            and structure["rank"] == EXPECTED_RANK
            and 0 <= structure["rank"] < theorem["class_count"],
            {"code": structure["code"], "rank": structure["rank"]},
        )
        all_x_word = tuple(("X", (wire,)) for wire in support)
        check(
            "J_nonuniqueness_control_all_X_is_another_minimum_word",
            apply_word(0, all_x_word) == structure["target"]
            and all_x_word != structure["landed_word"],
            {"all_X_length": len(all_x_word)},
        )
        check(
            "K_scope_excludes_translation_physics_and_axiom_selection",
            fixture["supplied_model"] == EXPECTED_MODEL
            and theorem["class_count"] > 1,
            {
                "translated_target_family_claimed": False,
                "physical_gate_minimality_claimed": False,
                "axiom_selection_claimed": False,
                "unique_class_claimed": False,
            },
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
                "runtime_seconds": round(perf_counter() - started, 6),
                "supplied_scope": {
                    "alphabet": fixture["supplied_model"]["alphabet"],
                    "blank_state": fixture["blank_state"],
                    "cost": fixture["supplied_model"]["cost"],
                    "equivalence": fixture["supplied_model"]["equivalence"],
                    "landing_rule": fixture["supplied_model"]["landing_rule"],
                    "register_width": fixture["register_width"],
                    "target_support": support,
                },
                "theorem": theorem,
                "landed_coordinate": {
                    "code": structure["code"],
                    "rank": structure["rank"],
                    "status": "meta coordinate only",
                },
                "claim_boundary": {
                    "fixed_target_conditional_theorem": True,
                    "analytic_not_exhaustive_search": True,
                    "translated_target_family_claimed": False,
                    "physical_minimality_claimed": False,
                    "autonomous_selection_claimed": False,
                    "axiom_consequence_claimed": False,
                    "route_independent_no_go_claimed": False,
                },
            }
        )
    except Exception as error:
        check(
            "UNEXPECTED_primary_exception",
            False,
            {"type": type(error).__name__, "message": str(error)},
        )
        report["error_type"] = type(error).__name__
        report["error"] = str(error)
        report["runtime_seconds"] = round(perf_counter() - started, 6)
    check(
        "OUTPUT_stdout_under_150KB",
        len(json.dumps(report, default=str).encode()) + 4096
        < STDOUT_LIMIT_BYTES,
    )
    return emit_report(report)


if __name__ == "__main__":
    raise SystemExit(main())
