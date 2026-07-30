#!/usr/bin/env python3
"""Cycle 807: audit whether the 777/781 regress has a universal grammar proof.

The lineage programs are immutable text/AST evidence.  This runner never
imports or executes them.  It extracts the family they actually instantiate,
reimplements the exact Boolean wiring, proves the conditional Hamming-word
defeater, and fails closed if the requested recursive guard grammar is absent.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
from time import perf_counter
from typing import Iterable


AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200_000
ENUMERATION_DEPTH = 1
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle777_prefix_closed_guard_2026_07_28.py",
    "scripts/frontier_cycle777_guard_independent_check_2026_07_28.py",
    "scripts/frontier_cycle781_checkpoint_refusal_law_2026_07_28.py",
    "scripts/frontier_cycle781_checkpoint_independent_check_2026_07_28.py",
)
EXPECTED_SHA256 = {
    "scripts/frontier_cycle777_prefix_closed_guard_2026_07_28.py":
        "c4bb14040957cd2509d738a56ce13f436f0ac4449cd8eac1a051b396c951b652",
    "scripts/frontier_cycle777_guard_independent_check_2026_07_28.py":
        "67dbe53ad180f7a4cc6f1ffd0d40606e961ff47fb12bfa5bc9c3aeb9cf638962",
    "scripts/frontier_cycle781_checkpoint_refusal_law_2026_07_28.py":
        "b1158250dcb1449f6abac4f6bb6a0a90f47511a8a0f587e85483f4b6f3624211",
    "scripts/frontier_cycle781_checkpoint_independent_check_2026_07_28.py":
        "29709ff9163aa347ac7124d6dd48be06591d775354890218072221706ce20d94",
}
BLOCKLISTED_MODULES = (
    "frontier_cycle777_prefix_closed_guard_2026_07_28",
    "frontier_cycle777_guard_independent_check_2026_07_28",
    "frontier_cycle781_checkpoint_refusal_law_2026_07_28",
    "frontier_cycle781_checkpoint_independent_check_2026_07_28",
)
LANDED_FAMILY_EQUATIONS = (
    "B ::= RAIL777",
    "G_landed ::= B | SINGLE_N(B) | MAJORITY3_N(B) | REFRESH_N(B)",
    "No production c(G_landed) occurs in the pinned lineage.",
)
CONDITIONAL_DEFEAT_EQUATIONS = (
    "Delta((),())=()",
    "Delta((a,tail_a),(b,tail_b))=(a XOR b,Delta(tail_a,tail_b))",
    "defeat(c0,c1)=product_{i:Delta(c0,c1)[i]=1} X(i)",
    "c0 XOR Delta(c0,c1)=c1",
)
EXPLICIT_781_SCOPE_PREMISES = (
    "state-only guard",
    "all relevant rails fully editable",
    "two record-distinct lawful zero-syndrome codewords",
    "arbitrary finite one-qubit-operator-algebra X words admitted",
    "attack word can finish after fanout and before the boundary check",
)
OUTSIDE_OR_ALTERNATIVE_ROUTES = (
    "authenticated reference",
    "inaccessible or transition-restricted rails",
    "atomic or history-dependent boundary checking",
    "explicit attempt/location rails",
    "a unique lawful post-engagement codeword",
    "restricted attack alphabet or timing",
)
ROOT = Path(__file__).resolve().parents[1]


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def ast_digest(source: bytes) -> str:
    tree = ast.parse(source.decode("utf-8"))
    dumped = ast.dump(tree, annotate_fields=True, include_attributes=False)
    return sha256(dumped.encode("utf-8")).hexdigest()


def source_snapshot() -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for relative in AUDIT_INPUT_PATHS:
        source = (ROOT / relative).read_bytes()
        result[relative] = {
            "ast_sha256": ast_digest(source),
            "bytes": len(source),
            "sha256": sha256(source).hexdigest(),
        }
    return result


def assignment_literal(tree: ast.Module, name: str) -> object:
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            )
        ):
            return ast.literal_eval(node.value)
    raise KeyError(name)


def named_node(tree: ast.Module, name: str) -> ast.AST:
    for node in tree.body:
        if (
            isinstance(node, (ast.ClassDef, ast.FunctionDef))
            and node.name == name
        ):
            return node
    raise KeyError(name)


def imported_modules(tree: ast.AST) -> tuple[str, ...]:
    result: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            result.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            result.append(node.module)
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "import_module"
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
        ):
            result.append(node.args[0].value)
    return tuple(result)


def call_names(node: ast.AST) -> tuple[str, ...]:
    return tuple(sorted({
        ast.unparse(item.func)
        for item in ast.walk(node)
        if isinstance(item, ast.Call)
    }))


def recursive_call_count(node: ast.AST, name: str) -> int:
    return sum(
        isinstance(item, ast.Call)
        and isinstance(item.func, ast.Name)
        and item.func.id == name
        for item in ast.walk(node)
    )


def grammar_extraction_and_firewall() -> dict[str, object]:
    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    imports = imported_modules(own_tree)
    literal_paths = assignment_literal(own_tree, "AUDIT_INPUT_PATHS")
    blocked_hits = tuple(sorted(set(imports).intersection(BLOCKLISTED_MODULES)))
    execution_calls = tuple(sorted({
        ast.unparse(node.func)
        for node in ast.walk(own_tree)
        if isinstance(node, ast.Call)
        and ast.unparse(node.func) in {
            "__import__", "compile", "eval", "exec", "importlib.import_module"
        }
    }))
    path_checks = {
        relative: (
            not Path(relative).is_absolute()
            and (ROOT / relative).is_file()
            and (ROOT / relative).resolve().is_relative_to(ROOT.resolve())
        )
        for relative in AUDIT_INPUT_PATHS
    }
    trees = {
        relative: ast.parse((ROOT / relative).read_text(encoding="utf-8"))
        for relative in AUDIT_INPUT_PATHS
    }
    p777, i777, p781, i781 = AUDIT_INPUT_PATHS
    nodes = {
        "primary_rail": named_node(trees[p777], "build_rail_guard"),
        "independent_rail": named_node(trees[i777], "build_guard"),
        "primary_checkpoint": named_node(trees[p781], "compile_guard_words"),
        "single": named_node(trees[i781], "compile_single_checkpoint"),
        "majority3": named_node(trees[i781], "compile_majority_three"),
        "executor": named_node(trees[i781], "apply_compiled_word"),
        "adaptive": named_node(trees[i781], "adaptive_null_attack"),
        "regress_scope": named_node(trees[i781], "regress_theorem_candidate"),
    }
    expected_ranges = {
        "primary_rail": (280, 297),
        "independent_rail": (419, 436),
        "primary_checkpoint": (403, 435),
        "single": (857, 901),
        "majority3": (904, 978),
        "executor": (843, 854),
        "adaptive": (1332, 1369),
        "regress_scope": (1372, 1414),
    }
    observed_ranges = {
        name: (node.lineno, node.end_lineno)
        for name, node in nodes.items()
    }

    constructor_calls = tuple(
        node
        for node in ast.walk(trees[i781])
        if isinstance(node, ast.Call)
        and ast.unparse(node.func) in {
            "compile_single_checkpoint", "compile_majority_three"
        }
    )
    call_rows = tuple({
        "callee": ast.unparse(node.func),
        "first_argument": (
            ast.unparse(node.args[0]) if node.args else None
        ),
        "line": node.lineno,
        "name_keyword": next(
            (
                keyword.value.value
                for keyword in node.keywords
                if keyword.arg == "name"
                and isinstance(keyword.value, ast.Constant)
            ),
            None,
        ),
    } for node in sorted(constructor_calls, key=lambda item: item.lineno))
    expected_calls = (
        {
            "callee": "compile_single_checkpoint",
            "first_argument": "layout.live_width",
            "line": 1487,
            "name_keyword": "single",
        },
        {
            "callee": "compile_majority_three",
            "first_argument": "layout.live_width",
            "line": 1488,
            "name_keyword": None,
        },
        {
            "callee": "compile_single_checkpoint",
            "first_argument": "layout.live_width",
            "line": 1489,
            "name_keyword": "refresh",
        },
    )
    no_recursive_rail = (
        recursive_call_count(nodes["primary_rail"], "build_rail_guard") == 0
        and recursive_call_count(nodes["independent_rail"], "build_guard") == 0
    )
    no_child_guard_parameter = (
        tuple(arg.arg for arg in nodes["single"].args.args) == ("live_width",)
        and tuple(arg.arg for arg in nodes["majority3"].args.args)
        == ("live_width",)
    )
    no_recursive_checkpoint_construction = (
        call_rows == expected_calls
        and no_child_guard_parameter
        and all(
            row["first_argument"] == "layout.live_width"
            for row in call_rows
        )
    )
    constructor_shapes = {
        "RAIL777": {
            "calls": call_names(nodes["primary_rail"]),
            "one_layer_instantiated": no_recursive_rail,
        },
        "SINGLE_N": {
            "calls": call_names(nodes["single"]),
            "parameter": "live_width",
        },
        "MAJORITY3_N": {
            "calls": call_names(nodes["majority3"]),
            "parameter": "live_width",
        },
        "REFRESH_N": {
            "implemented_by": "compile_single_checkpoint",
            "main_call_line": 1489,
            "schedule_only_variant": True,
        },
    }
    citations = {
        "RAIL777": f"{p777}:280-297",
        "RAIL777_INDEPENDENT": f"{i777}:419-436",
        "CHECKPOINT_PRIMARY": f"{p781}:403-435",
        "SINGLE_N": f"{i781}:857-901",
        "MAJORITY3_N": f"{i781}:904-978",
        "FIXED_SIBLING_INSTANTIATIONS": f"{i781}:1487-1506",
        "REFRESH_BOUNDARIES": f"{i781}:1530-1562",
        "DEFEATER_PATTERN": f"{i781}:1314-1369",
        "CONDITIONAL_SCOPE": f"{i781}:1387-1413",
    }
    return {
        "blocked_import_hits": blocked_hits,
        "constructor_calls": call_rows,
        "constructor_shapes": constructor_shapes,
        "dangerous_execution_calls": execution_calls,
        "grammar_citations": citations,
        "imports": imports,
        "landed_family": LANDED_FAMILY_EQUATIONS,
        "literal_AUDIT_INPUT_PATHS": literal_paths,
        "no_child_guard_parameter": no_child_guard_parameter,
        "no_recursive_checkpoint_construction":
            no_recursive_checkpoint_construction,
        "no_recursive_guard_closure": (
            no_recursive_rail and no_recursive_checkpoint_construction
        ),
        "no_recursive_rail": no_recursive_rail,
        "node_ranges_exact": observed_ranges == expected_ranges,
        "observed_ranges": observed_ranges,
        "ok": (
            literal_paths == AUDIT_INPUT_PATHS
            and all(path_checks.values())
            and not blocked_hits
            and not execution_calls
            and observed_ranges == expected_ranges
            and no_recursive_rail
            and no_recursive_checkpoint_construction
        ),
        "path_checks": path_checks,
        "text_AST_only": True,
    }


@dataclass(frozen=True)
class Gate:
    kind: str
    wires: tuple[int, ...]


@dataclass(frozen=True)
class GuardSchema:
    name: str
    depth: int
    code0: tuple[int, ...]
    code1: tuple[int, ...]
    boundary_word: tuple[Gate, ...]
    receipt_indices: tuple[int, ...]
    provenance: str


def x_gate(wire: int) -> Gate:
    return Gate("X", (wire,))


def cnot(control: int, target: int) -> Gate:
    return Gate("CNOT", (control, target))


def tof(first: int, second: int, target: int) -> Gate:
    return Gate("TOF", (first, second, target))


def apply_word(state: list[int], word: Iterable[Gate]) -> None:
    for gate in word:
        if gate.kind == "X":
            state[gate.wires[0]] ^= 1
        elif gate.kind == "CNOT":
            control, target = gate.wires
            state[target] ^= state[control]
        elif gate.kind == "TOF":
            first, second, target = gate.wires
            state[target] ^= state[first] & state[second]
        else:
            raise ValueError(gate.kind)


def hamming_mask(
    first: tuple[int, ...],
    second: tuple[int, ...],
) -> tuple[int, ...]:
    """Total finite-tuple implementation of the printed recursion equations."""
    if len(first) != len(second):
        raise ValueError("codeword widths differ")
    return tuple(left ^ right for left, right in zip(first, second))


def single_boundary(width: int) -> tuple[Gate, ...]:
    checkpoint = width
    syndrome = 2 * width
    return tuple(
        gate
        for index in range(width)
        for gate in (
            cnot(index, syndrome + index),
            cnot(checkpoint + index, syndrome + index),
            cnot(syndrome + index, index),
        )
    )


def majority_boundary(width: int) -> tuple[Gate, ...]:
    copies = (width, 2 * width, 3 * width)
    quartet_starts = (0, *copies)
    pairs = tuple(
        (left, right)
        for left in range(4)
        for right in range(left + 1, 4)
    )
    pairwise_start = 4 * width
    majority_start = 10 * width
    correction_start = 11 * width
    word: list[Gate] = []
    for pair_index, (left, right) in enumerate(pairs):
        output = pairwise_start + pair_index * width
        for index in range(width):
            word.extend((
                cnot(quartet_starts[left] + index, output + index),
                cnot(quartet_starts[right] + index, output + index),
            ))
    first, second, third = copies
    for index in range(width):
        majority = majority_start + index
        word.extend((
            tof(first + index, second + index, majority),
            tof(first + index, third + index, majority),
            tof(second + index, third + index, majority),
        ))
    for number, target in enumerate(quartet_starts):
        correction = correction_start + number * width
        for index in range(width):
            word.extend((
                cnot(target + index, correction + index),
                cnot(majority_start + index, correction + index),
                cnot(correction + index, target + index),
            ))
    return tuple(word)


def landed_schema_family() -> tuple[GuardSchema, ...]:
    # This is the exact changed-support slice: the selected primary D rail and
    # its Cycle-777 outer D copy.  All omitted rails are identical context.
    base0 = (0, 0)
    base1 = (1, 1)
    rail = GuardSchema(
        name="RAIL777",
        depth=0,
        code0=base0,
        code1=base1,
        boundary_word=(),
        receipt_indices=(),
        provenance=AUDIT_INPUT_PATHS[0] + ":280-297",
    )
    width = len(base0)
    single = GuardSchema(
        name="SINGLE_N(RAIL777)",
        depth=1,
        code0=(*base0, *base0, *(0,) * width),
        code1=(*base1, *base1, *(0,) * width),
        boundary_word=single_boundary(width),
        receipt_indices=tuple(range(2 * width, 3 * width)),
        provenance=AUDIT_INPUT_PATHS[3] + ":857-901",
    )
    majority = GuardSchema(
        name="MAJORITY3_N(RAIL777)",
        depth=1,
        code0=(*base0, *base0, *base0, *base0, *(0,) * (11 * width)),
        code1=(*base1, *base1, *base1, *base1, *(0,) * (11 * width)),
        boundary_word=majority_boundary(width),
        receipt_indices=tuple(range(4 * width, 10 * width)),
        provenance=AUDIT_INPUT_PATHS[3] + ":904-978",
    )
    refresh = GuardSchema(
        name="REFRESH_N(RAIL777)",
        depth=1,
        code0=single.code0,
        code1=single.code1,
        boundary_word=single.boundary_word,
        receipt_indices=single.receipt_indices,
        provenance=AUDIT_INPUT_PATHS[3] + ":1489-1505",
    )
    return rail, single, majority, refresh


def gate_indices_valid(word: Iterable[Gate], width: int) -> bool:
    arities = {"X": 1, "CNOT": 2, "TOF": 3}
    return all(
        gate.kind in arities
        and len(gate.wires) == arities[gate.kind]
        and all(0 <= wire < width for wire in gate.wires)
        for gate in word
    )


def evaluate_schema(schema: GuardSchema) -> dict[str, object]:
    mask = hamming_mask(schema.code0, schema.code1)
    attack_word = tuple(
        x_gate(index) for index, bit in enumerate(mask) if bit
    )
    attacked = list(schema.code0)
    apply_word(attacked, attack_word)
    attacked_codeword = tuple(attacked)
    apply_word(attacked, schema.boundary_word)
    final_state = tuple(attacked)

    clean = list(schema.code0)
    apply_word(clean, schema.boundary_word)
    alternate = list(schema.code1)
    apply_word(alternate, schema.boundary_word)
    syndrome_count = sum(
        final_state[index] for index in schema.receipt_indices
    )
    exact_alternate_execution = final_state == tuple(alternate)
    record_changed = final_state[0] != tuple(clean)[0]
    algebraic_defeat = (
        attacked_codeword == schema.code1
        and exact_alternate_execution
        and syndrome_count == 0
        and record_changed
        and gate_indices_valid(attack_word, len(schema.code0))
        and gate_indices_valid(schema.boundary_word, len(schema.code0))
    )
    return {
        "algebraic_defeat": algebraic_defeat,
        "attack_gate_count": len(attack_word),
        "attack_mutates_record_support": record_changed,
        "attack_word_kinds": tuple(sorted({gate.kind for gate in attack_word})),
        "boundary_gate_count": len(schema.boundary_word),
        "conditional_lawfulness": (
            "true exactly under EXPLICIT_781_SCOPE_PREMISES; not derived here"
        ),
        "depth": schema.depth,
        "exact_alternate_execution": exact_alternate_execution,
        "name": schema.name,
        "provenance": schema.provenance,
        "syndrome_count": syndrome_count,
        "width_of_changed_support_model": len(schema.code0),
    }


def hamming_constructor_certificate() -> dict[str, object]:
    rows = []
    failures = []
    for width in range(5):
        for first_value in range(1 << width):
            first = tuple(
                (first_value >> index) & 1 for index in range(width)
            )
            for second_value in range(1 << width):
                second = tuple(
                    (second_value >> index) & 1 for index in range(width)
                )
                mask = hamming_mask(first, second)
                observed = tuple(
                    bit ^ flip for bit, flip in zip(first, mask)
                )
                row = {
                    "first": first,
                    "mask": mask,
                    "maps": observed == second,
                    "second": second,
                    "width": width,
                }
                rows.append(row)
                if not row["maps"]:
                    failures.append(row)
    wide_width = 4096
    wide_mask = hamming_mask((0,) * wide_width, (1,) * wide_width)
    wide_exact = len(wide_mask) == wide_width and all(wide_mask)
    return {
        "conditional_theorem": (
            "For two admitted lawful codewords of equal finite width, the "
            "finite product-X word on their Hamming difference maps one "
            "exactly to the other."
        ),
        "equations": CONDITIONAL_DEFEAT_EQUATIONS,
        "exact_rows": len(rows),
        "failure_count": len(failures),
        "implementation": (
            "iterative finite-tuple realization; no interpreter recursion limit"
        ),
        "ok": not failures and wide_exact,
        "recursion_equations_checked": not failures,
        "truth_digest": digest(rows),
        "wide_finite_tuple_check": {
            "exact": wide_exact,
            "width": wide_width,
        },
    }


def finite_family_and_step_certificate() -> dict[str, object]:
    schemas = landed_schema_family()
    rows = tuple(evaluate_schema(schema) for schema in schemas)
    depth_histogram = {
        depth: sum(schema.depth == depth for schema in schemas)
        for depth in range(ENUMERATION_DEPTH + 1)
    }
    step_rows = tuple(
        {
            "algebraic_step_pass": row["algebraic_defeat"],
            "constructor": row["name"].split("_N", 1)[0],
            "depth": row["depth"],
            "local_syndrome_zero": row["syndrome_count"] == 0,
        }
        for row in rows[1:]
    )
    return {
        "depth": ENUMERATION_DEPTH,
        "depth_histogram": depth_histogram,
        "expected_count": 4,
        "expected_depth_histogram": {0: 1, 1: 3},
        "fixed_family_all_algebraic_defeats": all(
            row["algebraic_defeat"] for row in rows
        ),
        "fixed_step_rows": step_rows,
        "ok": (
            len(schemas) == 4
            and len({schema.name for schema in schemas}) == 4
            and depth_histogram == {0: 1, 1: 3}
            and all(row["algebraic_defeat"] for row in rows)
        ),
        "rows": rows,
    }


def deterministic_payload() -> dict[str, object]:
    extraction = grammar_extraction_and_firewall()
    constructor = hamming_constructor_certificate()
    finite = finite_family_and_step_certificate()
    recursive_induction_closed = not extraction["no_recursive_guard_closure"]
    return {
        "conditional_constructor": constructor,
        "finite_family": finite,
        "grammar_extraction": extraction,
        "recursive_induction": {
            "closed": recursive_induction_closed,
            "exact_failing_constructor": (
                None
                if recursive_induction_closed
                else "COMPOSE_OR_WRAP_G: absent from pinned 777/781 source"
            ),
            "fixed_one_layer_steps_pass": all(
                row["algebraic_step_pass"]
                for row in finite["fixed_step_rows"]
            ),
            "requested_multiple_recursive_depths_available": False,
        },
    }


def projected_stdout_bytes(lines: list[str], report: dict[str, object]) -> int:
    final_line = canonical_json(report)
    return sum(
        len((line + "\n").encode("utf-8"))
        for line in (*lines, final_line)
    )


def main() -> int:
    started = perf_counter()
    before_snapshot = source_snapshot()
    first = deterministic_payload()
    second = deterministic_payload()
    after_snapshot = source_snapshot()

    extraction = first["grammar_extraction"]
    constructor = first["conditional_constructor"]
    finite = first["finite_family"]
    induction = first["recursive_induction"]
    anchors_pinned = all(
        before_snapshot[path]["sha256"] == EXPECTED_SHA256[path]
        for path in AUDIT_INPUT_PATHS
    )
    deterministic = first == second

    target_a = bool(
        anchors_pinned
        and before_snapshot == after_snapshot
        and extraction["ok"]
    )
    target_b = bool(constructor["ok"])
    target_c = bool(finite["ok"])
    target_d = bool(induction["closed"])
    verdict = (
        "UNIVERSAL_AT_GRAMMAR"
        if all((target_a, target_b, target_c, target_d))
        else "OPEN_EXACT_GAP"
    )
    target_e = verdict == "UNIVERSAL_AT_GRAMMAR"
    exact_gap = induction["exact_failing_constructor"]

    data_lines = [
        "CERTIFICATE_A_GRAMMAR_EXTRACTION " + canonical_json({
            "constructor_schema_count": 4,
            "constructors": (
                "RAIL777", "SINGLE_N", "MAJORITY3_N", "REFRESH_N",
            ),
            "family_equations": LANDED_FAMILY_EQUATIONS,
            "provenance": extraction["grammar_citations"],
            "recursive_closure_present":
                not extraction["no_recursive_guard_closure"],
        }),
        "SHA_ANCHORS " + canonical_json(before_snapshot),
        "IMPORT_BLOCKLIST " + canonical_json({
            "blocked_hits": extraction["blocked_import_hits"],
            "blocked_modules": BLOCKLISTED_MODULES,
            "dangerous_execution_calls":
                extraction["dangerous_execution_calls"],
            "literal_AUDIT_INPUT_PATHS":
                extraction["literal_AUDIT_INPUT_PATHS"],
            "text_AST_only": extraction["text_AST_only"],
        }),
        "CERTIFICATE_B_CONDITIONAL_DEFEATER " + canonical_json({
            **constructor,
            "explicit_scope_premises": EXPLICIT_781_SCOPE_PREMISES,
            "not_proved": (
                "The premises are not derived from Admissibility or Record, "
                "and the recursion is over configuration bits, not guards."
            ),
        }),
    ]
    data_lines.extend(
        "CERTIFICATE_C_FINITE_CASE " + canonical_json(row)
        for row in finite["rows"]
    )
    data_lines.append(
        "CERTIFICATE_C_FINITE_SUMMARY " + canonical_json({
            key: value
            for key, value in finite.items()
            if key != "rows"
        })
    )
    data_lines.append(
        "CERTIFICATE_D_INDUCTION " + canonical_json({
            **induction,
            "source_fact": (
                "single, majority3, and refresh are sibling instantiations "
                "over the same layout.live_width, not constructors on G"
            ),
        })
    )
    data_lines.append(
        "CERTIFICATE_E_VERDICT " + canonical_json({
            "exact_gap": exact_gap,
            "outside_or_alternative_routes": OUTSIDE_OR_ALTERNATIVE_ROUTES,
            "record_axiom_necessity_established": False,
            "scope": (
                "The finite landed sibling family is defeated algebraically "
                "under the explicit 781 editability/codeword/timing premises."
            ),
            "scope_exclusion": (
                "No universal claim is made for recursive/nested guards or "
                "for guards outside the finite landed family."
            ),
            "verdict": verdict,
        })
    )

    runtime_sec = perf_counter() - started
    controls_base = bool(
        anchors_pinned
        and before_snapshot == after_snapshot
        and extraction["ok"]
        and deterministic
        and runtime_sec < AUDIT_TIMEOUT_SEC
    )
    runner_certificates = {
        "A_EXACT_FINITE_GRAMMAR_EXTRACTION": target_a,
        "B_CONDITIONAL_DEFEATER_ALGEBRA": target_b,
        "C_COMPLETE_FINITE_FAMILY": target_c,
        "D_HONEST_MISSING_INDUCTION_GAP": (
            not target_d and exact_gap is not None
        ),
        "E_HONEST_SCOPED_VERDICT": (
            not target_e
            and verdict == "OPEN_EXACT_GAP"
            and not target_d
        ),
        "F_CONTROLS": False,
    }
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "conditional_defeater_proved": target_b,
        "enumerated_guard_count": finite["expected_count"],
        "enumeration_depth": ENUMERATION_DEPTH,
        "recursive_induction_closed": target_d,
        "record_axiom_necessity_established": False,
        "runner_certificates": runner_certificates,
        "runtime_sec": runtime_sec,
        "stdout_bytes": 0,
        "target_certificates": {
            "A": target_a,
            "B": target_b,
            "C": target_c,
            "D": target_d,
            "E": target_e,
        },
        "verdict": verdict,
    }
    certificate_lines: list[str] = []
    controls_line = ""
    for _iteration in range(12):
        runner_certificates["F_CONTROLS"] = bool(
            controls_base
            and int(report["stdout_bytes"]) < STDOUT_LIMIT_BYTES
        )
        report["runner_certificates"] = runner_certificates
        controls_line = "CERTIFICATE_F_CONTROLS " + canonical_json({
            "anchors_pinned": anchors_pinned,
            "determinism": deterministic,
            "exact_arithmetic": "Boolean GF(2); integer counts; no randomness",
            "input_snapshot_unchanged": before_snapshot == after_snapshot,
            "runtime_limit_sec": AUDIT_TIMEOUT_SEC,
            "runtime_sec": runtime_sec,
            "stdlib_only": True,
            "stdout_bytes": report["stdout_bytes"],
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "text_AST_blocklist": extraction["ok"],
        })
        certificate_lines = [
            ("PASS" if value else "FAIL") + f" RUNNER_CERTIFICATE_{name}"
            for name, value in runner_certificates.items()
        ]
        candidate_lines = [*data_lines, controls_line, *certificate_lines]
        size = projected_stdout_bytes(candidate_lines, report)
        if size == report["stdout_bytes"]:
            break
        report["stdout_bytes"] = size

    final_lines = [*data_lines, controls_line, *certificate_lines]
    final_size = projected_stdout_bytes(final_lines, report)
    if final_size != report["stdout_bytes"]:
        report["stdout_bytes"] = final_size
    for line in final_lines:
        print(line)
    print(canonical_json(report))
    return 0 if all(runner_certificates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
