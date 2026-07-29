#!/usr/bin/env python3
"""Cycle 753 independent adversarial selection/minimality checker.

The Cycle-753 primary is parsed as inert source text and is blocklisted from
import.  All semantic checks and recounts below are independent
implementations over the two declared predecessor modules.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/GENESIS_SELECTION_ATTEMPT_CYCLE753_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from collections import defaultdict
from hashlib import sha256
from itertools import permutations, product
import json
from math import comb, factorial
from pathlib import Path
import sys
from time import perf_counter


STARTED = perf_counter()
PRIMARY_PATH = (
    "scripts/frontier_cycle753_genesis_selection_attempt_2026_07_28.py"
)
BLOCKLIST = (
    "frontier_cycle753_genesis_selection_attempt_2026_07_28",
)
STDOUT_LIMIT_BYTES = 150 * 1024
BRUTE_FORCE_OPERATION_BUDGET = 50_000_000
EXPECTED_BOUND = 27
EXPECTED_RING_STATIONS = 11
EXPECTED_OUTCOME = "B_MULTIPLE_MINIMAL_CLASSES"
EXPECTED_STATUS = (
    "correct and minimum-length, but one of N inequivalent minimum classes"
)
CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []

IMPORT_ERROR: Exception | None = None
try:
    import frontier_cycle732_genesis_word_self_verification_2026_07_28 as G732
    import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
except Exception as error:  # Emit an honest bounded failure, not a traceback.
    IMPORT_ERROR = error
    G732 = None  # type: ignore[assignment]
    K = None  # type: ignore[assignment]


def check(label: str, condition: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def emit_report(report: dict[str, object]) -> int:
    report["AUDIT_INPUT_PATHS"] = AUDIT_INPUT_PATHS
    report["NOTE_PATH"] = NOTE_PATH
    report["audit_timeout_seconds"] = AUDIT_TIMEOUT_SEC
    report["blocklist"] = BLOCKLIST
    report["runtime_seconds"] = round(perf_counter() - STARTED, 6)
    preliminary = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(preliminary.encode())
        + len("\n".join(OUTPUT_LINES).encode())
        + 4096
        < STDOUT_LIMIT_BYTES,
    )
    check(
        "OUTPUT_runtime_under_AUDIT_TIMEOUT",
        float(report["runtime_seconds"]) < AUDIT_TIMEOUT_SEC,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE753_SELECTION_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE753_SELECTION_INDEPENDENT_CHECK_HONEST_FAIL"
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


def module_assignment(tree: ast.AST, name: str) -> ast.AST:
    for node in getattr(tree, "body", ()):
        if isinstance(node, ast.Assign):
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            ):
                return node.value
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            return node.value
    raise KeyError(("module assignment", name))


def function_node(tree: ast.AST, name: str) -> ast.FunctionDef:
    for node in getattr(tree, "body", ()):
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise KeyError(("function", name))


def local_assignment(scope: ast.AST, name: str) -> ast.AST:
    for node in ast.walk(scope):
        if isinstance(node, ast.Assign):
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            ):
                return node.value
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            return node.value
    raise KeyError(("local assignment", name))


def dict_nodes(node: ast.AST) -> dict[str, ast.AST]:
    if not isinstance(node, ast.Dict):
        raise TypeError(("expected dict", type(node).__name__))
    output: dict[str, ast.AST] = {}
    for key, value in zip(node.keys, node.values):
        literal_key = ast.literal_eval(key)
        if not isinstance(literal_key, str):
            raise TypeError(("non-string dict key", literal_key))
        output[literal_key] = value
    return output


def check_condition(scope: ast.AST, label: str) -> ast.AST:
    for node in ast.walk(scope):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "check"
            and len(node.args) >= 2
        ):
            try:
                candidate = ast.literal_eval(node.args[0])
            except (ValueError, TypeError):
                continue
            if candidate == label:
                return node.args[1]
    raise KeyError(("check", label))


def safe_arithmetic(node: ast.AST, names: dict[str, object]) -> object:
    """Evaluate only a small arithmetic/literal AST vocabulary."""

    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        if node.id not in names:
            raise ValueError(("unknown safe name", node.id))
        return names[node.id]
    if isinstance(node, ast.Tuple):
        return tuple(safe_arithmetic(item, names) for item in node.elts)
    if isinstance(node, ast.List):
        return [safe_arithmetic(item, names) for item in node.elts]
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -int(safe_arithmetic(node.operand, names))
    if isinstance(node, ast.BinOp):
        left = safe_arithmetic(node.left, names)
        right = safe_arithmetic(node.right, names)
        operations = {
            ast.Add: lambda: left + right,  # type: ignore[operator]
            ast.Sub: lambda: left - right,  # type: ignore[operator]
            ast.Mult: lambda: left * right,  # type: ignore[operator]
            ast.FloorDiv: lambda: left // right,  # type: ignore[operator]
            ast.Pow: lambda: left ** right,  # type: ignore[operator]
        }
        for kind, operation in operations.items():
            if isinstance(node.op, kind):
                return operation()
        raise ValueError(("unsafe binary operator", type(node.op).__name__))
    if isinstance(node, ast.Compare) and len(node.ops) == len(node.comparators) == 1:
        left = safe_arithmetic(node.left, names)
        right = safe_arithmetic(node.comparators[0], names)
        if isinstance(node.ops[0], ast.Eq):
            return left == right
        if isinstance(node.ops[0], ast.NotEq):
            return left != right
        if isinstance(node.ops[0], ast.Lt):
            return left < right  # type: ignore[operator]
        if isinstance(node.ops[0], ast.LtE):
            return left <= right  # type: ignore[operator]
        raise ValueError(("unsafe comparison", type(node.ops[0]).__name__))
    if isinstance(node, ast.IfExp):
        branch = node.body if safe_arithmetic(node.test, names) else node.orelse
        return safe_arithmetic(branch, names)
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {"factorial", "comb"}
    ):
        arguments = tuple(
            int(safe_arithmetic(argument, names)) for argument in node.args
        )
        return (
            factorial(*arguments)
            if node.func.id == "factorial"
            else comb(*arguments)
        )
    if isinstance(node, ast.JoinedStr):
        pieces: list[str] = []
        for item in node.values:
            if isinstance(item, ast.Constant) and isinstance(item.value, str):
                pieces.append(item.value)
            elif isinstance(item, ast.FormattedValue):
                pieces.append(str(safe_arithmetic(item.value, names)))
            else:
                raise ValueError(("unsafe f-string item", ast.dump(item)))
        return "".join(pieces)
    raise ValueError(("unsafe AST", type(node).__name__, ast.unparse(node)))


def extraction() -> dict[str, object]:
    """AST-only extraction of every Cycle-753 completeness claim."""

    source = Path(PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_PATH)
    primary_audit_node = module_assignment(tree, "AUDIT_INPUT_PATHS")
    primary_audit = ast.literal_eval(primary_audit_node)
    search_limit = ast.literal_eval(module_assignment(tree, "SEARCH_LIMIT"))
    ring_stations = ast.literal_eval(
        module_assignment(tree, "RING_STATIONS")
    )
    main_node = function_node(tree, "main")

    alphabet_nodes = dict_nodes(local_assignment(main_node, "alphabet"))
    safe_nodes = dict_nodes(local_assignment(main_node, "safe_pruning"))
    expected_safe_keys = (
        "rule_1_weight_lower_bound",
        "rule_1_machine_premises",
        "rule_2_minimum_monotonicity",
        "rule_2_landed_machine_check",
        "rule_3_translation",
        "rule_3_machine_check",
        "rule_4_commutation",
        "rule_4_complete_quotient",
    )
    justification_keys = (
        "rule_1_weight_lower_bound",
        "rule_2_minimum_monotonicity",
        "rule_3_translation",
        "rule_4_commutation",
        "rule_4_complete_quotient",
    )
    justifications = {
        key: ast.literal_eval(safe_nodes[key]) for key in justification_keys
    }

    exact_node = function_node(tree, "exact_census")
    census_dict: dict[str, ast.AST] | None = None
    for node in ast.walk(exact_node):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "append"
            and node.args
            and isinstance(node.args[0], ast.Dict)
        ):
            candidate = dict_nodes(node.args[0])
            if "lawful_goal_words" in candidate:
                census_dict = candidate
                break
    if census_dict is None:
        raise AssertionError("exact_census row dictionary absent")
    goal_words_node = local_assignment(exact_node, "goal_words")
    goal_classes_node = local_assignment(exact_node, "goal_classes")

    arithmetic_names: dict[str, object] = {
        "target_weight": search_limit,
        "RING_STATIONS": ring_stations,
    }
    per_target_node = local_assignment(main_node, "per_target_raw_words")
    per_target = int(safe_arithmetic(per_target_node, arithmetic_names))
    arithmetic_names["per_target_raw_words"] = per_target
    orbit_node = local_assignment(main_node, "orbit_raw_words")
    orbit_raw = int(safe_arithmetic(orbit_node, arithmetic_names))
    arithmetic_names["orbit_raw_words"] = orbit_raw
    class_node = local_assignment(main_node, "class_count")
    class_count = int(safe_arithmetic(class_node, arithmetic_names))
    arithmetic_names["class_count"] = class_count

    primary_goal_words: list[int] = []
    primary_goal_classes: list[int] = []
    for length in range(search_limit + 1):
        census_names = {
            "length": length,
            "targets": ring_stations,
            "support_size": search_limit,
        }
        primary_goal_words.append(
            int(
                safe_arithmetic(
                    goal_words_node, census_names
                )
            )
        )
        primary_goal_classes.append(
            int(
                safe_arithmetic(
                    goal_classes_node, census_names
                )
            )
        )

    census_assertion = ast.unparse(
        check_condition(
            main_node, "C_exhaustive_census_each_length_through_L27"
        )
    )
    boundary_nodes = dict_nodes(local_assignment(main_node, "boundary"))
    outcome = safe_arithmetic(
        local_assignment(main_node, "outcome"), arithmetic_names
    )
    arithmetic_names["outcome"] = outcome
    status = safe_arithmetic(
        boundary_nodes["Cycle732_word_status"], arithmetic_names
    )
    bound = safe_arithmetic(boundary_nodes["bound_L"], {
        **arithmetic_names,
        "SEARCH_LIMIT": search_limit,
    })
    minimum_proved = safe_arithmetic(
        boundary_nodes["minimum_proved"], arithmetic_names
    )
    selection_derived = safe_arithmetic(
        boundary_nodes["selection_derived_as_minimality"],
        arithmetic_names,
    )
    selection_narrowed = safe_arithmetic(
        boundary_nodes["selection_narrowed_to_frozen_census"],
        arithmetic_names,
    )
    remaining_tuple = safe_arithmetic(
        boundary_nodes["W1_remaining_supplies"], {
            **arithmetic_names,
            "remaining_supplies": safe_arithmetic(
                local_assignment(main_node, "remaining_supplies"),
                arithmetic_names,
            ),
        }
    )
    minimal_sentence = safe_arithmetic(
        local_assignment(main_node, "minimal_content_sentence"),
        arithmetic_names,
    )

    full_census_nodes = dict_nodes(
        local_assignment(main_node, "full_minimal_census")
    )
    rank_statement = safe_arithmetic(
        full_census_nodes["representation"], arithmetic_names
    )
    report_nodes = dict_nodes(local_assignment(main_node, "report"))
    search_space_nodes = dict_nodes(report_nodes["search_space"])

    literal_contract = (
        isinstance(primary_audit, tuple)
        and all(isinstance(path, str) for path in primary_audit)
        and ast.dump(primary_audit_node)
        == ast.dump(
            ast.parse(repr(primary_audit), mode="eval").body
        )
    )
    extracted_ok = (
        literal_contract
        and search_limit == EXPECTED_BOUND
        and ring_stations == EXPECTED_RING_STATIONS
        and tuple(safe_nodes) == expected_safe_keys
        and tuple(alphabet_nodes)
        == (
            "full_width",
            "X_placements",
            "CNOT_ordered_distinct_placements",
            "size",
            "gate_kinds",
        )
        and tuple(search_space_nodes)
        == (
            "initial_state",
            "alphabet",
            "lawful_target_definition",
            "lawful_target_count",
            "lawful_target_weights",
            "landed_target",
            "landed_target_sha256",
        )
        and all(primary_goal_words[length] == 0 for length in range(27))
        and primary_goal_words[27] == orbit_raw
        and all(primary_goal_classes[length] == 0 for length in range(27))
        and primary_goal_classes[27] == class_count
        and "census[:-1]" in census_assertion
        and "lawful_goal_words" in census_assertion
        and "lawful_goal_classes" in census_assertion
        and "== 0" in census_assertion
        and outcome == EXPECTED_OUTCOME
        and bound == EXPECTED_BOUND
        and minimum_proved is True
        and status == EXPECTED_STATUS
        and selection_derived is False
        and selection_narrowed is True
        and isinstance(remaining_tuple, tuple)
        and remaining_tuple[-1]
        == f"one residual minimal-class rank in [0,{class_count - 1}]"
    )
    return {
        "pass": extracted_ok,
        "primary_source_sha256": sha256(source.encode()).hexdigest(),
        "primary_AUDIT_INPUT_PATHS_literal": literal_contract,
        "primary_AUDIT_INPUT_PATHS": primary_audit,
        "search_limit": search_limit,
        "ring_stations": ring_stations,
        "search_space_keys": tuple(search_space_nodes),
        "alphabet_definition": {
            key: ast.unparse(value)
            for key, value in alphabet_nodes.items()
        },
        "pruning_keys": tuple(safe_nodes),
        "stated_safety_justifications": justifications,
        "census_formulae": {
            "unpruned_alphabet_words":
                ast.unparse(census_dict["unpruned_alphabet_words"]),
            "target_tagged_viable_prefix_words":
                ast.unparse(
                    census_dict["target_tagged_viable_prefix_words"]
                ),
            "translation_quotiented_commutation_prefix_classes":
                ast.unparse(
                    census_dict[
                        "translation_quotiented_commutation_prefix_classes"
                    ]
                ),
            "lawful_goal_words": ast.unparse(goal_words_node),
            "lawful_goal_classes": ast.unparse(goal_classes_node),
        },
        "census_assertion": census_assertion,
        "stated_zero_lawful_lengths": tuple(
            length for length, count in enumerate(primary_goal_words)
            if count == 0
        ),
        "stated_length_27_raw_count": primary_goal_words[27],
        "stated_length_27_minimal_class_count":
            primary_goal_classes[27],
        "per_target_raw_formula": ast.unparse(per_target_node),
        "orbit_raw_formula": ast.unparse(orbit_node),
        "class_formula": ast.unparse(class_node),
        "outcome": outcome,
        "bound_L": bound,
        "Cycle732_word_status": status,
        "selection_derived_as_minimality": selection_derived,
        "selection_narrowed_to_frozen_census": selection_narrowed,
        "minimal_content_sentence": minimal_sentence,
        "prufer_rank_census_statement": rank_statement,
        "remaining_prufer_rank_convention": remaining_tuple[-1],
    }


def bits_to_int(bits: tuple[int, ...]) -> int:
    return sum(int(bit) << wire for wire, bit in enumerate(bits))


def int_to_bits(value: int, width: int) -> tuple[int, ...]:
    return tuple((value >> wire) & 1 for wire in range(width))


def apply_gate(state: int, kind: str, wires: tuple[int, ...]) -> int:
    if kind == "X":
        return state ^ (1 << wires[0])
    if kind == "CNOT":
        control, target = wires
        return (
            state ^ (1 << target)
            if (state >> control) & 1
            else state
        )
    raise ValueError(("outside X/CNOT alphabet", kind, wires))


def apply_word(state: int, word: tuple[object, ...]) -> int:
    for gate in word:
        state = apply_gate(state, gate.kind, tuple(gate.wires))
    return state


def translation_wire_map(
    layout: dict[str, int], shift: int
) -> tuple[int, ...]:
    """Independent station-block rotation on the actual Cycle-732 layout."""

    stations = int(layout["stations"])
    mapping = list(range(int(layout["full_width"])))
    for name in (
        "a_base",
        "b_base",
        "work_base",
        "syndrome_base",
        "ref_base",
        "charge_base",
    ):
        base = int(layout[name])
        for station in range(stations):
            mapping[base + station] = (
                base + (station + shift) % stations
            )
    block_rows = (
        (
            "scratch_base",
            (
                int(layout["or_scratch_base"])
                - int(layout["scratch_base"])
            )
            // stations,
        ),
        (
            "or_scratch_base",
            (int(layout["ref_base"]) - int(layout["or_scratch_base"]))
            // stations,
        ),
    )
    for name, block_width in block_rows:
        base = int(layout[name])
        for station in range(stations):
            moved = (station + shift) % stations
            for slot in range(block_width):
                mapping[base + station * block_width + slot] = (
                    base + moved * block_width + slot
                )
    return tuple(mapping)


def translate_value(value: int, mapping: tuple[int, ...]) -> int:
    output = 0
    while value:
        low = value & -value
        wire = low.bit_length() - 1
        output |= 1 << mapping[wire]
        value ^= low
    return output


def translate_word(
    word: tuple[object, ...], mapping: tuple[int, ...]
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    return tuple(
        (gate.kind, tuple(mapping[wire] for wire in gate.wires))
        for gate in word
    )


def apply_plain_word(
    state: int, word: tuple[tuple[str, tuple[int, ...]], ...]
) -> int:
    for kind, wires in word:
        state = apply_gate(state, kind, wires)
    return state


def gate_pair_commutes(
    left: tuple[str, tuple[int, ...]],
    right: tuple[str, tuple[int, ...]],
) -> bool:
    left_kind, left_wires = left
    right_kind, right_wires = right
    if left_kind == right_kind == "X":
        return True
    if left_kind == "X" and right_kind == "CNOT":
        return left_wires[0] != right_wires[0]
    if left_kind == "CNOT" and right_kind == "X":
        return right_wires[0] != left_wires[0]
    if left_kind == right_kind == "CNOT":
        a, b = left_wires
        c, d = right_wires
        return b != c and d != a
    raise ValueError((left, right))


def k_semantics_and_commutation_truth() -> dict[str, object]:
    width = 4
    gates = tuple(
        [("X", (wire,)) for wire in range(width)]
        + [
            ("CNOT", (control, target))
            for control in range(width)
            for target in range(width)
            if control != target
        ]
    )
    semantic_mismatches = 0
    for kind, wires in gates:
        gate = (
            K.A.x(wires[0])
            if kind == "X"
            else K.A.cn(wires[0], wires[1])
        )
        for state in range(1 << width):
            observed = bits_to_int(
                tuple(K.A.apply_semantic(int_to_bits(state, width), (gate,)))
            )
            semantic_mismatches += observed != apply_gate(
                state, kind, wires
            )

    commutation_mismatches = 0
    commuting_pairs = 0
    noncommuting_pairs = 0
    for left in gates:
        for right in gates:
            semantic_commutes = all(
                apply_plain_word(state, (left, right))
                == apply_plain_word(state, (right, left))
                for state in range(1 << width)
            )
            predicted = gate_pair_commutes(left, right)
            commutation_mismatches += semantic_commutes != predicted
            commuting_pairs += semantic_commutes
            noncommuting_pairs += not semantic_commutes
    return {
        "test_width": width,
        "single_gate_truth_rows": len(gates) * (1 << width),
        "single_gate_semantic_mismatches": semantic_mismatches,
        "ordered_gate_pairs": len(gates) ** 2,
        "commuting_pairs": commuting_pairs,
        "noncommuting_pairs": noncommuting_pairs,
        "commutation_iff_mismatches": commutation_mismatches,
        "pass":
            semantic_mismatches == 0
            and commutation_mismatches == 0
            and noncommuting_pairs > 0,
    }


def weight_and_monotonicity_counterexample_search(
    maximum_width: int = 4,
) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    delta_failures = 0
    nonmonotone_goal_words = 0
    total_goal_words = 0
    for width in range(1, maximum_width + 1):
        gates = tuple(
            [("X", (wire,)) for wire in range(width)]
            + [
                ("CNOT", (control, target))
                for control in range(width)
                for target in range(width)
                if control != target
            ]
        )
        for state in range(1 << width):
            for kind, wires in gates:
                delta = (
                    apply_gate(state, kind, wires).bit_count()
                    - state.bit_count()
                )
                delta_failures += delta not in (-1, 0, 1)

        target = (1 << width) - 1
        width_goal_words = 0
        width_bad_words = 0
        for word_indices in product(range(len(gates)), repeat=width):
            state = 0
            trace = [0]
            for index in word_indices:
                kind, wires = gates[index]
                state = apply_gate(state, kind, wires)
                trace.append(state.bit_count())
            if state == target:
                width_goal_words += 1
                if trace != list(range(width + 1)):
                    width_bad_words += 1
        expected = factorial(width) ** 2
        rows.append(
            {
                "width_and_length": width,
                "alphabet_size": len(gates),
                "unpruned_words": len(gates) ** width,
                "goal_words": width_goal_words,
                "expected_monotone_words": expected,
                "nonmonotone_goal_words": width_bad_words,
            }
        )
        total_goal_words += width_goal_words
        nonmonotone_goal_words += width_bad_words
    return {
        "maximum_width": maximum_width,
        "rows": tuple(rows),
        "weight_delta_failures": delta_failures,
        "total_goal_words": total_goal_words,
        "nonmonotone_goal_words": nonmonotone_goal_words,
        "pass":
            delta_failures == 0
            and nonmonotone_goal_words == 0
            and all(
                row["goal_words"] == row["expected_monotone_words"]
                for row in rows
            ),
    }


def monotone_words(
    support_size: int,
) -> tuple[tuple[tuple[int, int], ...], ...]:
    """All monotone words; parent 0 denotes X, other parents denote CNOT."""

    words: list[tuple[tuple[int, int], ...]] = []
    vertices = tuple(range(1, support_size + 1))
    for order in permutations(vertices):
        parent_options = tuple(
            (0,) + order[:step] for step in range(support_size)
        )
        for parents in product(*parent_options):
            words.append(tuple(zip(parents, order)))
    return tuple(words)


def abstract_gate(
    edge: tuple[int, int]
) -> tuple[str, tuple[int, ...]]:
    parent, child = edge
    return (
        ("X", (child,))
        if parent == 0
        else ("CNOT", (parent, child))
    )


def tree_key(
    word: tuple[tuple[int, int], ...]
) -> tuple[tuple[int, int], ...]:
    return tuple(
        sorted((min(parent, child), max(parent, child))
               for parent, child in word)
    )


def prufer_code_from_tree(
    edges: tuple[tuple[int, int], ...], vertices: int
) -> tuple[int, ...]:
    adjacency = {vertex: set() for vertex in range(vertices)}
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    code: list[int] = []
    for _ in range(vertices - 2):
        leaf = min(
            vertex
            for vertex, neighbors in adjacency.items()
            if len(neighbors) == 1
        )
        neighbor = next(iter(adjacency[leaf]))
        code.append(neighbor)
        adjacency[neighbor].remove(leaf)
        del adjacency[leaf]
    return tuple(code)


class DisjointSet:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root == right_root:
            return
        if self.rank[left_root] < self.rank[right_root]:
            left_root, right_root = right_root, left_root
        self.parent[right_root] = left_root
        if self.rank[left_root] == self.rank[right_root]:
            self.rank[left_root] += 1


def commutation_quotient_counterexample_search(
    support_size: int = 5,
) -> dict[str, object]:
    words = monotone_words(support_size)
    indices = {word: index for index, word in enumerate(words)}
    dsu = DisjointSet(len(words))
    unsafe_swap_failures = 0
    for index, word in enumerate(words):
        for position in range(len(word) - 1):
            left = abstract_gate(word[position])
            right = abstract_gate(word[position + 1])
            if not gate_pair_commutes(left, right):
                continue
            swapped = (
                word[:position]
                + (word[position + 1], word[position])
                + word[position + 2:]
            )
            other = indices.get(swapped)
            if other is None:
                unsafe_swap_failures += 1
            else:
                dsu.union(index, other)

    component_trees: dict[int, set[tuple[tuple[int, int], ...]]] = (
        defaultdict(set)
    )
    tree_sizes: dict[tuple[tuple[int, int], ...], int] = defaultdict(int)
    for index, word in enumerate(words):
        component_trees[dsu.find(index)].add(tree_key(word))
        tree_sizes[tree_key(word)] += 1
    tree_keys = tuple(tree_sizes)
    codes = tuple(
        prufer_code_from_tree(key, support_size + 1)
        for key in tree_keys
    )
    expected_raw = factorial(support_size) ** 2
    expected_classes = (support_size + 1) ** (support_size - 1)
    return {
        "support_size": support_size,
        "raw_words_enumerated": len(words),
        "expected_raw_words": expected_raw,
        "commutation_components": len(component_trees),
        "rooted_tree_keys": len(tree_keys),
        "expected_prufer_classes": expected_classes,
        "unsafe_commuting_swaps": unsafe_swap_failures,
        "components_with_multiple_trees": sum(
            len(keys) != 1 for keys in component_trees.values()
        ),
        "minimum_class_size": min(tree_sizes.values()),
        "maximum_class_size": max(tree_sizes.values()),
        "class_sizes_sum": sum(tree_sizes.values()),
        "distinct_prufer_codes": len(set(codes)),
        "prufer_code_length_failures": sum(
            len(code) != support_size - 1 for code in codes
        ),
        "prufer_digit_failures": sum(
            not all(0 <= digit <= support_size for digit in code)
            for code in codes
        ),
        "pass":
            len(words) == expected_raw
            and len(component_trees) == expected_classes
            and len(tree_keys) == expected_classes
            and unsafe_swap_failures == 0
            and all(len(keys) == 1 for keys in component_trees.values())
            and sum(tree_sizes.values()) == expected_raw
            and len(set(codes)) == expected_classes
            and all(len(code) == support_size - 1 for code in codes)
            and all(
                all(0 <= digit <= support_size for digit in code)
                for code in codes
            ),
    }


def translation_certificate(
    fixture: dict[str, object], word: tuple[object, ...]
) -> dict[str, object]:
    layout = fixture["layout"]
    target = int(fixture["target"])
    width = int(layout["full_width"])
    stations = int(layout["stations"])
    mappings = tuple(
        translation_wire_map(layout, shift)
        for shift in range(stations)
    )
    targets = tuple(
        translate_value(target, mapping) for mapping in mappings
    )
    permutation_failures = sum(
        tuple(sorted(mapping)) != tuple(range(width))
        for mapping in mappings
    )
    identity_failures = sum(
        mappings[0][wire] != wire for wire in range(width)
    )
    composition_failures = 0
    for left in range(stations):
        for right in range(stations):
            combined = (left + right) % stations
            composition_failures += any(
                mappings[left][mappings[right][wire]]
                != mappings[combined][wire]
                for wire in range(width)
            )
    equivariance_failures = 0
    for mapping, translated_target in zip(mappings, targets):
        moved_word = translate_word(word, mapping)
        equivariance_failures += (
            apply_plain_word(0, moved_word) != translated_target
        )
    a_base = int(layout["a_base"])
    a_rows = tuple(
        tuple(
            (translated >> (a_base + station)) & 1
            for station in range(stations)
        )
        for translated in targets
    )
    return {
        "stations": stations,
        "full_width": width,
        "mapping_permutation_failures": permutation_failures,
        "identity_failures": identity_failures,
        "group_composition_failures": composition_failures,
        "target_orbit_size": len(set(targets)),
        "target_weights": tuple(value.bit_count() for value in targets),
        "unique_A_marker_each_target": all(sum(row) == 1 for row in a_rows),
        "A_marker_rows": a_rows,
        "translated_word_equivariance_failures": equivariance_failures,
        "pass":
            stations == EXPECTED_RING_STATIONS
            and permutation_failures == 0
            and identity_failures == 0
            and composition_failures == 0
            and len(set(targets)) == stations
            and all(value.bit_count() == target.bit_count() for value in targets)
            and all(sum(row) == 1 for row in a_rows)
            and equivariance_failures == 0,
    }


def brute_force_unpruned_window(
    width: int, lawful_targets: tuple[int, ...]
) -> dict[str, object]:
    """Literal full-alphabet word-tree enumeration with no safety pruning."""

    alphabet_size = width ** 2
    maximum_length = 0
    while (
        alphabet_size ** (maximum_length + 1)
        <= BRUTE_FORCE_OPERATION_BUDGET
    ):
        maximum_length += 1
    if maximum_length != 1:
        raise AssertionError(
            ("unexpected brute-force window", width, maximum_length)
        )

    target_set = set(lawful_targets)
    goals = [int(0 in target_set)]
    examined = 0
    length_one_goals = 0
    for wire in range(width):
        output = apply_gate(0, "X", (wire,))
        length_one_goals += output in target_set
        examined += 1
    for control in range(width):
        for target in range(width):
            if control == target:
                continue
            output = apply_gate(0, "CNOT", (control, target))
            length_one_goals += output in target_set
            examined += 1
    goals.append(length_one_goals)
    return {
        "operation_budget": BRUTE_FORCE_OPERATION_BUDGET,
        "alphabet_size": alphabet_size,
        "largest_feasible_L_small": maximum_length,
        "next_depth_word_count": alphabet_size ** (maximum_length + 1),
        "word_counts_by_length": (1, examined),
        "lawful_goal_counts_by_length": tuple(goals),
        "expected_word_counts_by_length": (1, alphabet_size),
        "pass":
            examined == alphabet_size
            and tuple(goals) == (0, 0)
            and alphabet_size <= BRUTE_FORCE_OPERATION_BUDGET
            and alphabet_size ** 2 > BRUTE_FORCE_OPERATION_BUDGET,
    }


def independent_pruned_recount(
    support_size: int, translations: int
) -> dict[str, object]:
    """Independent recurrence; no Cycle-753 census helper is executed."""

    prefix_per_target = 1
    rows: list[dict[str, int]] = []
    for length in range(support_size + 1):
        if length:
            prefix_per_target *= (
                support_size - length + 1
            ) * length
        rows.append(
            {
                "length": length,
                "target_tagged_viable_prefix_words":
                    translations * prefix_per_target,
                "lawful_goal_words": 0,
                "lawful_goal_classes": 0,
            }
        )
    per_target_raw = prefix_per_target
    orbit_raw = translations * per_target_raw
    class_count = 1
    for _ in range(support_size - 1):
        class_count *= support_size + 1
    rows[-1]["lawful_goal_words"] = orbit_raw
    rows[-1]["lawful_goal_classes"] = class_count

    permutation_orders = 1
    parent_choices = 1
    for step in range(support_size):
        permutation_orders *= support_size - step
        parent_choices *= step + 1
    return {
        "rows": tuple(rows),
        "zero_lawful_lengths": tuple(
            row["length"] for row in rows[:-1]
            if row["lawful_goal_words"] == 0
            and row["lawful_goal_classes"] == 0
        ),
        "preparation_orders": permutation_orders,
        "parent_choice_sequences": parent_choices,
        "raw_minimal_words_per_exact_target": per_target_raw,
        "translation_group_order": translations,
        "translation_action_free": True,
        "raw_minimal_words_across_translation_orbit": orbit_raw,
        "commutation_classes_via_prufer": class_count,
        "prufer_alphabet_size": support_size + 1,
        "prufer_code_length": support_size - 1,
        "rank_interval": (0, class_count - 1),
        "pass":
            tuple(row["length"] for row in rows)
            == tuple(range(support_size + 1))
            and tuple(
                row["lawful_goal_words"] for row in rows[:-1]
            )
            == (0,) * support_size
            and tuple(
                row["lawful_goal_classes"] for row in rows[:-1]
            )
            == (0,) * support_size
            and permutation_orders == factorial(support_size)
            and parent_choices == factorial(support_size)
            and per_target_raw
            == permutation_orders * parent_choices
            and orbit_raw == translations * per_target_raw
            and class_count
            == (support_size + 1) ** (support_size - 1),
    }


def landed_anchor(
    fixture: dict[str, object],
    word: tuple[object, ...],
    class_count: int,
) -> dict[str, object]:
    target = int(fixture["target"])
    width = int(fixture["layout"]["full_width"])
    support = tuple(
        wire for wire in range(width) if (target >> wire) & 1
    )
    labels = {wire: index + 1 for index, wire in enumerate(support)}
    prepared: set[int] = set()
    edges: list[tuple[int, int]] = []
    weight_trace = [0]
    subset_failures = 0
    structure_failures = 0
    state = 0
    for gate in word:
        kind = gate.kind
        wires = tuple(gate.wires)
        before_weight = state.bit_count()
        if kind == "X" and len(wires) == 1:
            wire = wires[0]
            parent = 0
        elif kind == "CNOT" and len(wires) == 2:
            control, wire = wires
            if control not in prepared:
                structure_failures += 1
            parent = labels.get(control, -1)
        else:
            structure_failures += 1
            continue
        if wire not in labels or wire in prepared or parent < 0:
            structure_failures += 1
        else:
            edges.append((parent, labels[wire]))
        prepared.add(wire)
        state = apply_gate(state, kind, wires)
        weight_trace.append(state.bit_count())
        subset_failures += bool(state & ~target)
        structure_failures += state.bit_count() != before_weight + 1

    canonical_edges = tuple(
        sorted((min(left, right), max(left, right))
               for left, right in edges)
    )
    code = (
        prufer_code_from_tree(canonical_edges, len(support) + 1)
        if len(canonical_edges) == len(support)
        else ()
    )
    rank = 0
    for digit in code:
        rank = rank * (len(support) + 1) + digit
    k_observed = bits_to_int(
        tuple(K.A.apply_semantic((0,) * width, word))
    )
    return {
        "length": len(word),
        "support_size": len(support),
        "alphabet": tuple(sorted(set(gate.kind for gate in word))),
        "own_zero_landing": state == target,
        "K_zero_landing": k_observed == target,
        "prepared_support_exact": prepared == set(support),
        "rooted_tree_edges": len(canonical_edges),
        "structure_failures": structure_failures,
        "target_subset_failures": subset_failures,
        "weight_trace": tuple(weight_trace),
        "prufer_code": code,
        "prufer_code_sha256": sha256(
            json.dumps(code, separators=(",", ":")).encode()
        ).hexdigest(),
        "prufer_rank": rank,
        "rank_interval": (0, class_count - 1),
        "pass":
            len(word) == len(support) == EXPECTED_BOUND
            and set(gate.kind for gate in word) <= {"X", "CNOT"}
            and state == k_observed == target
            and prepared == set(support)
            and len(canonical_edges) == len(support)
            and structure_failures == 0
            and subset_failures == 0
            and weight_trace == list(range(len(support) + 1))
            and len(code) == len(support) - 1
            and all(0 <= digit <= len(support) for digit in code)
            and 0 <= rank < class_count,
    }


def pruning_safety_reproof(
    fixture: dict[str, object], word: tuple[object, ...]
) -> dict[str, object]:
    semantics = k_semantics_and_commutation_truth()
    monotonicity = weight_and_monotonicity_counterexample_search()
    translation = translation_certificate(fixture, word)
    quotient = commutation_quotient_counterexample_search()
    rule_verdicts = {
        "rule_1_weight_lower_bound":
            semantics["single_gate_semantic_mismatches"] == 0
            and monotonicity["weight_delta_failures"] == 0,
        "rule_2_minimum_monotonicity": monotonicity["pass"],
        "rule_3_translation": translation["pass"],
        "rule_4_commutation_and_prufer_quotient":
            semantics["commutation_iff_mismatches"] == 0
            and quotient["pass"],
    }
    return {
        "rule_verdicts": rule_verdicts,
        "rule_1_and_rule_4_actual_K_truth": semantics,
        "rule_1_and_rule_2_unpruned_counterexample_search":
            monotonicity,
        "rule_3_actual_register_translation": translation,
        "rule_4_small_exact_quotient_search": quotient,
        "independent_arguments": {
            "rule_1": (
                "X and active CNOT toggle one bit; inactive CNOT toggles "
                "none. Thus each gate raises Hamming weight by at most one."
            ),
            "rule_2": (
                "A weight-27 endpoint after 27 gates saturates all 27 "
                "per-gate upper bounds. Every step therefore adds a target "
                "bit; any neutral, decreasing, repeated, inactive-control, "
                "or outside-support step would force a later gain above one."
            ),
            "rule_3": (
                "The independently rebuilt block map is a C11 permutation "
                "action, preserves X/CNOT semantics, and has a free target "
                "orbit certified by the unique rotating A marker."
            ),
            "rule_4": (
                "The truth-table commutation iff is exact. A minimum word "
                "chooses one parent among root plus earlier vertices for "
                "each new target, hence a rooted tree; commuting swaps are "
                "exactly swaps of incomparable preparation events. Prüfer "
                "codes biject those trees with length-26 base-28 words."
            ),
        },
        "pass": all(rule_verdicts.values()),
    }


def main() -> int:
    if IMPORT_ERROR is not None:
        check("INPUT_G732_and_K_imported", False)
        return emit_report(
            {
                "bounded": True,
                "import_error_type": type(IMPORT_ERROR).__name__,
                "import_error": str(IMPORT_ERROR),
                "honest_boundary": (
                    "The declared predecessors did not import; no "
                    "minimality or selection conclusion was emitted."
                ),
            }
        )

    report: dict[str, object] = {"bounded": True}
    try:
        blocklist_clean = all(
            module not in sys.modules for module in BLOCKLIST
        )
        check("DISCIPLINE_Cycle753_primary_blocklisted", blocklist_clean)
        check(
            "INPUT_AUDIT_tuple_exact_and_literal",
            AUDIT_INPUT_PATHS
            == (
                "scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py",
                "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
            ),
        )

        extracted = extraction()
        report["extraction"] = extracted
        check("A_extraction_AST_only_complete", extracted["pass"])
        check(
            "DISCIPLINE_primary_still_not_imported_after_extraction",
            all(module not in sys.modules for module in BLOCKLIST),
        )

        fixture = G732.declared_fixture()
        layout = fixture["layout"]
        target = int(fixture["target"])
        word = G732.genesis_word(len(fixture["program"]), layout)
        support_size = target.bit_count()

        pruning = pruning_safety_reproof(fixture, word)
        report["pruning_safety_reproof"] = pruning
        check("B_pruning_safety_independently_reproved", pruning["pass"])

        translation = pruning["rule_3_actual_register_translation"]
        target_orbit = tuple(
            translate_value(
                target, translation_wire_map(layout, shift)
            )
            for shift in range(int(layout["stations"]))
        )
        brute = brute_force_unpruned_window(
            int(layout["full_width"]), target_orbit
        )
        report["unpruned_brute_force_window"] = brute

        recount = independent_pruned_recount(
            support_size, int(layout["stations"])
        )
        report["minimality_recount"] = recount
        brute_matches_pruned = (
            brute["lawful_goal_counts_by_length"]
            == tuple(
                row["lawful_goal_words"]
                for row in recount["rows"][
                    : int(brute["largest_feasible_L_small"]) + 1
                ]
            )
        )
        check(
            "B_unpruned_full_register_window_matches_pruned_census",
            brute["pass"] and brute_matches_pruned,
        )
        check(
            "C_minimality_recount_zero_0_26_and_exact_L27",
            recount["pass"]
            and recount["zero_lawful_lengths"] == tuple(range(27))
            and recount["raw_minimal_words_across_translation_orbit"]
            == extracted["stated_length_27_raw_count"]
            and recount["commutation_classes_via_prufer"]
            == extracted["stated_length_27_minimal_class_count"],
        )

        anchor = landed_anchor(
            fixture,
            word,
            int(recount["commutation_classes_via_prufer"]),
        )
        report["anchor"] = anchor
        check("D_G732_landed_word_in_minimal_class_family", anchor["pass"])

        expected_residual = (
            "one residual minimal-class rank in "
            f"[0,{int(recount['commutation_classes_via_prufer']) - 1}]"
        )
        discipline = {
            "blocklist_clean": all(
                module not in sys.modules for module in BLOCKLIST
            ),
            "outcome_verbatim":
                extracted["outcome"] == EXPECTED_OUTCOME,
            "status_verbatim":
                extracted["Cycle732_word_status"] == EXPECTED_STATUS,
            "minimality_derived":
                recount["zero_lawful_lengths"] == tuple(range(27))
                and anchor["pass"],
            "selection_not_eliminated":
                int(recount["commutation_classes_via_prufer"]) > 1,
            "selection_narrowed_not_derived":
                extracted["selection_derived_as_minimality"] is False
                and extracted["selection_narrowed_to_frozen_census"]
                is True,
            "prufer_rank_remaining_convention_verbatim":
                extracted["remaining_prufer_rank_convention"]
                == expected_residual,
            "primary_never_imported":
                all(module not in sys.modules for module in BLOCKLIST),
        }
        discipline["pass"] = all(discipline.values())
        report["discipline"] = discipline
        check(
            "E_outcome_and_remaining_convention_discipline",
            discipline["pass"],
        )
        report["honest_boundary"] = {
            "bound_L": EXPECTED_BOUND,
            "outcome": EXPECTED_OUTCOME,
            "minimum_length_derived": True,
            "selection_eliminated": False,
            "selection_narrowed_to_class_rank_interval": True,
            "remaining_convention": expected_residual,
        }
    except Exception as error:
        check("UNEXPECTED_checker_exception", False)
        report["exception_type"] = type(error).__name__
        report["exception"] = str(error)
        report["honest_boundary"] = (
            "The independent checker raised a caught exception; no clean "
            "minimality or selection verdict was emitted."
        )
    return emit_report(report)


if __name__ == "__main__":
    raise SystemExit(main())
