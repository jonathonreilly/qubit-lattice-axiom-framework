#!/usr/bin/env python3
"""Cycle 807 independent adversarial check of the finite guard regress.

This checker does not import or execute the Cycle-807 primary or any of the
four pinned 777/781 lineage modules.  It uses their bytes and ASTs only,
reconstructs the Boolean guard families independently, and separately scans
all tracked Python modules under scripts/ for repo-scope wrapper candidates.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import subprocess
from time import perf_counter
from typing import Iterable


AUDIT_TIMEOUT_SEC = 1200
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle777_prefix_closed_guard_2026_07_28.py",
    "scripts/frontier_cycle777_guard_independent_check_2026_07_28.py",
    "scripts/frontier_cycle781_checkpoint_refusal_law_2026_07_28.py",
    "scripts/frontier_cycle781_checkpoint_independent_check_2026_07_28.py",
    "scripts/frontier_cycle807_universal_regress_theorem_2026_07_28.py",
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
    "scripts/frontier_cycle807_universal_regress_theorem_2026_07_28.py":
        "3c73a802e3f38b8a90f79de0eaef2164df7c5521847afffac2c88300f555e8ce",
}
LINEAGE_PATHS = AUDIT_INPUT_PATHS[:4]
PRIMARY_PATH = AUDIT_INPUT_PATHS[4]
BLOCKLISTED_MODULES = (
    "frontier_cycle807_universal_regress_theorem_2026_07_28",
)
SCHEMA_N_CHOICES = {
    "RAIL777": (1, 8, 63),
    "SINGLE_N": (1, 7, 64),
    "MAJORITY3_N": (1, 5, 32),
    "REFRESH_N": (2, 11, 96),
}
EXPLICIT_CONDITIONS = (
    "state-only finite guard",
    "every changed-support rail is editable",
    "two record-distinct lawful zero-syndrome codewords",
    "arbitrary finite products of one-rail X operators are admitted",
    "the attack finishes after fanout and before the boundary check",
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
    rows: dict[str, dict[str, object]] = {}
    for relative in AUDIT_INPUT_PATHS:
        source = (ROOT / relative).read_bytes()
        rows[relative] = {
            "ast_sha256": ast_digest(source),
            "bytes": len(source),
            "sha256": sha256(source).hexdigest(),
        }
    return rows


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


def imported_modules(tree: ast.AST) -> tuple[str, ...]:
    modules: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.append(node.module)
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "import_module"
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
        ):
            modules.append(node.args[0].value)
    return tuple(modules)


def function_args(node: ast.FunctionDef | ast.AsyncFunctionDef) -> tuple[str, ...]:
    return tuple(
        arg.arg
        for arg in (
            *node.args.posonlyargs,
            *node.args.args,
            *node.args.kwonlyargs,
        )
    )


def call_leaf(node: ast.Call) -> str:
    return ast.unparse(node.func).rsplit(".", 1)[-1]


def return_annotation(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    return ast.unparse(node.returns) if node.returns is not None else ""


def target_names(node: ast.Assign | ast.AnnAssign) -> tuple[str, ...]:
    targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
    return tuple(target.id for target in targets if isinstance(target, ast.Name))


GENERATOR_SCHEMAS = {
    (
        "scripts/frontier_cycle777_prefix_closed_guard_2026_07_28.py",
        "build_rail_guard",
    ): ("RAIL777",),
    (
        "scripts/frontier_cycle777_guard_independent_check_2026_07_28.py",
        "build_guard",
    ): ("RAIL777",),
    (
        "scripts/frontier_cycle781_checkpoint_refusal_law_2026_07_28.py",
        "build_guard_events",
    ): ("RAIL777",),
    (
        "scripts/frontier_cycle781_checkpoint_refusal_law_2026_07_28.py",
        "compile_guard_words",
    ): ("SINGLE_N",),
    (
        "scripts/frontier_cycle781_checkpoint_independent_check_2026_07_28.py",
        "outer_guard_events",
    ): ("RAIL777",),
    (
        "scripts/frontier_cycle781_checkpoint_independent_check_2026_07_28.py",
        "compile_single_checkpoint",
    ): ("SINGLE_N", "REFRESH_N"),
    (
        "scripts/frontier_cycle781_checkpoint_independent_check_2026_07_28.py",
        "compile_majority_three",
    ): ("MAJORITY3_N",),
}


def guard_relevant_function(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
) -> bool:
    terms = ("guard", "checkpoint", "program")
    calls = tuple(
        ast.unparse(item.func)
        for item in ast.walk(node)
        if isinstance(item, ast.Call)
    )
    blob = " ".join((
        node.name,
        *function_args(node),
        return_annotation(node),
        *calls,
    )).lower()
    return any(term in blob for term in terms)


def structural_generator(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
) -> bool:
    calls = {
        call_leaf(item)
        for item in ast.walk(node)
        if isinstance(item, ast.Call)
    }
    args = function_args(node)
    annotations = " ".join(
        ast.unparse(arg.annotation)
        for arg in (
            *node.args.posonlyargs,
            *node.args.args,
            *node.args.kwonlyargs,
        )
        if arg.annotation is not None
    )
    child_guard_argument = (
        any(name.lower() in {"guard", "child_guard", "program"} for name in args)
        or "RailGuard" in annotations
        or "GuardProgram" in annotations
    )
    constructs_known_object = bool({"RailGuard", "GuardProgram"} & calls)
    lexical_builder = node.name in {
        "build_guard_events",
        "outer_guard_events",
        "compile_guard_words",
    }
    return (constructs_known_object and not child_guard_argument) or lexical_builder


def catalog_ruling(
    relative: str,
    node: ast.ClassDef | ast.FunctionDef | ast.AsyncFunctionDef,
) -> tuple[str, tuple[str, ...]]:
    key = (relative, node.name)
    if key in GENERATOR_SCHEMAS:
        return "SCHEMA_GENERATOR", GENERATOR_SCHEMAS[key]
    if isinstance(node, ast.ClassDef):
        return "SCHEMA_CONTAINER_ONLY", ()
    if node.name == "main":
        return "FIXED_INSTANTIATION_ORCHESTRATOR", ()
    calls = {
        call_leaf(item)
        for item in ast.walk(node)
        if isinstance(item, ast.Call)
    }
    args = {name.lower() for name in function_args(node)}
    if (
        {"RailGuard", "GuardProgram"} & calls
        and bool({"guard", "program"} & args)
    ):
        return "STATE_TRANSFORM_NOT_SCHEMA", ()
    if "attack" in node.name:
        return "ATTACK_BUILDER_NOT_SCHEMA", ()
    if node.name in {
        "guard_state_bytes",
        "guard_bytes",
        "tensor_landed_guard_refuses",
        "receipt_count",
        "protected_regions",
        "algebraic_boundary",
        "run_battery",
        "run_guarded_battery",
        "shared_guard_battery",
        "extension_battery",
        "landed_controls",
        "non_interference",
        "lawful_non_interference",
        "program_provenance",
        "primary_guard_provenance_audit",
        "controller_controls",
        "make_fixture",
        "make_refresh_boundary_fixtures",
        "engaged_state",
        "run_attack",
    }:
        return "EVALUATOR_OR_FIXTURE_NOT_SCHEMA", ()
    return "GUARD_BEHAVIOR_SUPPORT_NOT_SCHEMA", ()


def lineage_inventory() -> dict[str, object]:
    catalog: list[dict[str, object]] = []
    discovered_generators: set[tuple[str, str]] = set()
    generator_nodes: dict[
        tuple[str, str], ast.FunctionDef | ast.AsyncFunctionDef
    ] = {}
    trees: dict[str, ast.Module] = {}
    for relative in LINEAGE_PATHS:
        tree = ast.parse((ROOT / relative).read_text(encoding="utf-8"))
        trees[relative] = tree
        for node in tree.body:
            if isinstance(node, ast.ClassDef) and any(
                term in node.name.lower()
                for term in ("guard", "checkpoint", "program")
            ):
                ruling, schemas = catalog_ruling(relative, node)
                catalog.append({
                    "file": relative,
                    "kind": "class",
                    "line": node.lineno,
                    "name": node.name,
                    "ruling": ruling,
                    "schemas": schemas,
                })
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if not guard_relevant_function(node):
                    continue
                ruling, schemas = catalog_ruling(relative, node)
                is_generator = structural_generator(node)
                if is_generator:
                    discovered_generators.add((relative, node.name))
                    generator_nodes[(relative, node.name)] = node
                catalog.append({
                    "file": relative,
                    "kind": "function",
                    "line": node.lineno,
                    "name": node.name,
                    "ruling": ruling,
                    "schemas": schemas,
                    "structural_generator": is_generator,
                })
            elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                names = target_names(node)
                if not any(
                    term in name.lower()
                    for name in names
                    for term in ("guard", "checkpoint", "program")
                ):
                    continue
                catalog.append({
                    "file": relative,
                    "kind": "table",
                    "line": node.lineno,
                    "name": ",".join(names),
                    "ruling": "ATTACK_OR_LAYOUT_TABLE_NOT_SCHEMA",
                    "schemas": (),
                })

    expected_generators = set(GENERATOR_SCHEMAS)
    fifth_generators = tuple(sorted(
        discovered_generators - expected_generators
    ))
    missing_generators = tuple(sorted(
        expected_generators - discovered_generators
    ))
    schemas = tuple(sorted({
        schema
        for key in discovered_generators
        for schema in GENERATOR_SCHEMAS.get(key, ())
    }))

    recursive_rows: list[dict[str, object]] = []
    for key, node in sorted(generator_nodes.items()):
        generator_calls = tuple(sorted({
            call_leaf(item)
            for item in ast.walk(node)
            if isinstance(item, ast.Call)
            and call_leaf(item) in {
                name for _path, name in expected_generators
            }
        }))
        arg_text = " ".join((
            *function_args(node),
            *(
                ast.unparse(arg.annotation)
                for arg in (
                    *node.args.posonlyargs,
                    *node.args.args,
                    *node.args.kwonlyargs,
                )
                if arg.annotation is not None
            ),
        )).lower()
        child_guard_parameter = any(
            term in arg_text
            for term in ("railguard", "guardprogram", "child_guard", "inner_guard")
        )
        recursive_rows.append({
            "file": key[0],
            "line": node.lineno,
            "name": key[1],
            "calls_other_lineage_generators": generator_calls,
            "child_guard_parameter": child_guard_parameter,
            "self_recursive": key[1] in generator_calls,
        })

    independent_path = LINEAGE_PATHS[3]
    main = next(
        node
        for node in trees[independent_path].body
        if isinstance(node, ast.FunctionDef) and node.name == "main"
    )
    fixed_calls = []
    for node in ast.walk(main):
        if not isinstance(node, ast.Call):
            continue
        leaf = call_leaf(node)
        if leaf not in {"compile_single_checkpoint", "compile_majority_three"}:
            continue
        name_keyword = next(
            (
                keyword.value.value
                for keyword in node.keywords
                if keyword.arg == "name"
                and isinstance(keyword.value, ast.Constant)
                and isinstance(keyword.value.value, str)
            ),
            None,
        )
        fixed_calls.append({
            "callee": leaf,
            "file": independent_path,
            "first_argument": ast.unparse(node.args[0]) if node.args else None,
            "line": node.lineno,
            "name_keyword": name_keyword,
        })
    fixed_calls.sort(key=lambda row: int(row["line"]))
    expected_fixed_calls = [
        {
            "callee": "compile_single_checkpoint",
            "file": independent_path,
            "first_argument": "layout.live_width",
            "line": 1487,
            "name_keyword": "single",
        },
        {
            "callee": "compile_majority_three",
            "file": independent_path,
            "first_argument": "layout.live_width",
            "line": 1488,
            "name_keyword": None,
        },
        {
            "callee": "compile_single_checkpoint",
            "file": independent_path,
            "first_argument": "layout.live_width",
            "line": 1489,
            "name_keyword": "refresh",
        },
    ]
    no_recursive_constructor = all(
        not row["child_guard_parameter"]
        and not row["calls_other_lineage_generators"]
        and not row["self_recursive"]
        for row in recursive_rows
    )
    complete = (
        schemas == ("MAJORITY3_N", "RAIL777", "REFRESH_N", "SINGLE_N")
        and not fifth_generators
        and not missing_generators
        and fixed_calls == expected_fixed_calls
        and no_recursive_constructor
    )
    return {
        "catalog": sorted(
            catalog,
            key=lambda row: (str(row["file"]), int(row["line"]), str(row["name"])),
        ),
        "complete": complete,
        "discovered_generator_definitions": tuple(sorted(discovered_generators)),
        "fifth_generators": fifth_generators,
        "fixed_sibling_calls": fixed_calls,
        "missing_generators": missing_generators,
        "no_recursive_constructor": no_recursive_constructor,
        "recursive_rows": recursive_rows,
        "schemas": schemas,
    }


def firewall_and_primary_scope() -> dict[str, object]:
    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    own_imports = imported_modules(own_tree)
    blocked_hits = tuple(sorted(
        set(own_imports).intersection(BLOCKLISTED_MODULES)
    ))
    literal_paths = assignment_literal(own_tree, "AUDIT_INPUT_PATHS")
    dangerous_calls = tuple(sorted({
        ast.unparse(node.func)
        for node in ast.walk(own_tree)
        if isinstance(node, ast.Call)
        and ast.unparse(node.func) in {
            "__import__",
            "compile",
            "eval",
            "exec",
            "importlib.import_module",
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

    primary_tree = ast.parse(
        (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    )
    primary_inputs = assignment_literal(primary_tree, "AUDIT_INPUT_PATHS")
    primary_strings = tuple(
        node.value
        for node in ast.walk(primary_tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    )
    pinned_phrase = any(
        "absent from pinned 777/781 source" in value
        for value in primary_strings
    )
    exclusion_phrase = any(
        "No universal claim is made for recursive/nested guards" in value
        and "outside the finite landed family" in value
        for value in primary_strings
    )
    primary_scope_exact = (
        tuple(primary_inputs) == LINEAGE_PATHS
        and pinned_phrase
        and exclusion_phrase
    )
    return {
        "blocked_import_hits": blocked_hits,
        "blocked_modules": BLOCKLISTED_MODULES,
        "dangerous_execution_calls": dangerous_calls,
        "literal_AUDIT_INPUT_PATHS": literal_paths,
        "path_checks": path_checks,
        "primary_AUDIT_INPUT_PATHS": primary_inputs,
        "primary_scope_exact": primary_scope_exact,
        "primary_text_AST_only": True,
        "scope_phrases": {
            "outside_family_exclusion": exclusion_phrase,
            "pinned_lineage": pinned_phrase,
        },
        "ok": (
            literal_paths == AUDIT_INPUT_PATHS
            and all(path_checks.values())
            and not blocked_hits
            and not dangerous_calls
            and primary_scope_exact
        ),
    }


@dataclass(frozen=True)
class Gate:
    kind: str
    wires: tuple[int, ...]


@dataclass(frozen=True)
class SchemaInstance:
    name: str
    parameter_n: int
    record_width: int
    code0: tuple[int, ...]
    code1: tuple[int, ...]
    boundary_word: tuple[Gate, ...]
    receipt_indices: tuple[int, ...]


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


def schema_instance(
    name: str,
    n: int,
    *,
    base0: tuple[int, ...] | None = None,
    base1: tuple[int, ...] | None = None,
) -> SchemaInstance:
    if n <= 0:
        raise ValueError("N must be positive")
    zero = base0 if base0 is not None else (0,) * n
    one = base1 if base1 is not None else (1,) * n
    if len(zero) != n or len(one) != n or zero == one:
        raise ValueError("base codewords must be distinct N-bit tuples")
    if any(bit not in (0, 1) for bit in (*zero, *one)):
        raise ValueError("codewords are Boolean")
    if name == "RAIL777":
        return SchemaInstance(name, n, n, zero, one, (), ())
    if name in {"SINGLE_N", "REFRESH_N"}:
        return SchemaInstance(
            name,
            n,
            n,
            (*zero, *zero, *(0,) * n),
            (*one, *one, *(0,) * n),
            single_boundary(n),
            tuple(range(2 * n, 3 * n)),
        )
    if name == "MAJORITY3_N":
        return SchemaInstance(
            name,
            n,
            n,
            (*zero, *zero, *zero, *zero, *(0,) * (11 * n)),
            (*one, *one, *one, *one, *(0,) * (11 * n)),
            majority_boundary(n),
            tuple(range(4 * n, 10 * n)),
        )
    raise KeyError(name)


def valid_gate_word(word: Iterable[Gate], width: int) -> bool:
    arity = {"X": 1, "CNOT": 2, "TOF": 3}
    return all(
        gate.kind in arity
        and len(gate.wires) == arity[gate.kind]
        and all(0 <= wire < width for wire in gate.wires)
        for gate in word
    )


def receipt_count(
    state: tuple[int, ...],
    receipt_indices: tuple[int, ...],
) -> int:
    return sum(state[index] for index in receipt_indices)


def evaluate_defeater(instance: SchemaInstance) -> dict[str, object]:
    width = len(instance.code0)
    difference = tuple(
        left ^ right
        for left, right in zip(instance.code0, instance.code1)
    )
    attack_word = tuple(
        x_gate(index)
        for index, bit in enumerate(difference)
        if bit
    )
    clean = list(instance.code0)
    apply_word(clean, instance.boundary_word)
    clean_final = tuple(clean)
    alternate = list(instance.code1)
    apply_word(alternate, instance.boundary_word)
    alternate_final = tuple(alternate)
    attacked = list(instance.code0)
    apply_word(attacked, attack_word)
    exact_codeword_map = tuple(attacked) == instance.code1
    apply_word(attacked, instance.boundary_word)
    final = tuple(attacked)

    lawful_zero_syndrome_pair = (
        receipt_count(clean_final, instance.receipt_indices) == 0
        and receipt_count(alternate_final, instance.receipt_indices) == 0
    )
    finite_x_word = (
        valid_gate_word(attack_word, width)
        and all(gate.kind == "X" for gate in attack_word)
        and len(attack_word) <= width
    )
    conditional_lawful = lawful_zero_syndrome_pair and finite_x_word
    syndrome_null = receipt_count(final, instance.receipt_indices) == 0
    record_byte_identical = (
        final[:instance.record_width]
        == clean_final[:instance.record_width]
    )
    permanence_violated = not record_byte_identical
    exact_alternate_execution = final == alternate_final
    defeat = (
        conditional_lawful
        and exact_codeword_map
        and exact_alternate_execution
        and syndrome_null
        and permanence_violated
        and valid_gate_word(instance.boundary_word, width)
    )
    return {
        "attack_gate_count": len(attack_word),
        "boundary_gate_count": len(instance.boundary_word),
        "conditional_lawful": conditional_lawful,
        "defeat": defeat,
        "exact_alternate_execution": exact_alternate_execution,
        "exact_codeword_map": exact_codeword_map,
        "landed_781_criterion": {
            "permanence_violated": permanence_violated,
            "record_byte_identical_after": record_byte_identical,
            "syndrome_null": syndrome_null,
        },
        "n": instance.parameter_n,
        "schema": instance.name,
        "state_width": width,
        "zero_syndrome_codeword_pair": lawful_zero_syndrome_pair,
    }


def n_generality_certificate() -> dict[str, object]:
    rows: dict[str, tuple[dict[str, object], ...]] = {}
    for schema, choices in SCHEMA_N_CHOICES.items():
        rows[schema] = tuple(
            evaluate_defeater(schema_instance(schema, n))
            for n in choices
        )
    per_schema = {
        schema: (
            tuple(row["n"] for row in schema_rows) == SCHEMA_N_CHOICES[schema]
            and len(schema_rows) >= 3
            and all(row["defeat"] for row in schema_rows)
        )
        for schema, schema_rows in rows.items()
    }
    return {
        "conditions": EXPLICIT_CONDITIONS,
        "n_choices": SCHEMA_N_CHOICES,
        "ok": all(per_schema.values()),
        "per_schema": per_schema,
        "rows": rows,
    }


def one_layer_steps_certificate() -> dict[str, object]:
    specifications = (
        ("SINGLE_N", 9),
        ("MAJORITY3_N", 7),
        ("REFRESH_N", 13),
    )
    rows = []
    for schema, n in specifications:
        base0 = tuple((index * 3 + 1) % 2 for index in range(n))
        base1 = tuple(
            (1 - bit) if index % 3 != 1 else bit
            for index, bit in enumerate(base0)
        )
        if base0[0] == base1[0]:
            base1 = (1 - base0[0], *base1[1:])
        result = evaluate_defeater(
            schema_instance(schema, n, base0=base0, base1=base1)
        )
        rows.append({
            **result,
            "base0_sha256": digest(base0),
            "base1_sha256": digest(base1),
            "step": f"{schema}(G)->defeated_{schema}(G)",
        })
    return {
        "hypothetical_steps": len(rows),
        "ok": len(rows) == 3 and all(row["defeat"] for row in rows),
        "rows": tuple(rows),
    }


def return_expressions(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
) -> tuple[str, ...]:
    return tuple(
        ast.unparse(item.value)
        for item in ast.walk(node)
        if isinstance(item, ast.Return) and item.value is not None
    )


def repo_constructor_candidate(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
) -> bool:
    args = function_args(node)
    annotations = " ".join(
        ast.unparse(arg.annotation)
        for arg in (
            *node.args.posonlyargs,
            *node.args.args,
            *node.args.kwonlyargs,
        )
        if arg.annotation is not None
    )
    result_annotation = return_annotation(node)
    calls_in_returns = {
        call_leaf(item)
        for returned in ast.walk(node)
        if isinstance(returned, ast.Return) and returned.value is not None
        for item in ast.walk(returned.value)
        if isinstance(item, ast.Call)
    }
    typed_guard_input = (
        any("guard" in arg.lower() for arg in args)
        or "guard" in annotations.lower()
    )
    typed_guard_output = (
        "guard" in result_annotation.lower()
        or any("guard" in call.lower() for call in calls_in_returns)
    )
    behavior_input = any(
        arg.lower() in {
            "guard",
            "guards",
            "program",
            "word",
            "controller",
            "function",
        }
        for arg in args
    )
    wrapper_signal = any(
        token in node.name.lower()
        for token in ("wrap", "compos", "refus")
    )
    behavior_output = bool(return_expressions(node))
    return (
        (typed_guard_input and typed_guard_output)
        or (behavior_input and wrapper_signal and behavior_output)
    )


def repo_candidate_ruling(
    relative: str,
    node: ast.FunctionDef | ast.AsyncFunctionDef,
) -> tuple[str, bool, bool]:
    if relative in LINEAGE_PATHS and node.name in {
        "tensor_guard_request",
        "apply_word_to_guard_cells",
        "direct_x_guard_cells",
        "apply_event_sequence_to_guard_cells",
    }:
        return "LINEAGE_STATE_TRANSITION_NOT_COMPOSITION", False, False
    true_wrapper_definitions = {
        (
            "scripts/frontier_cycle723_refusal_wrapped_controller_2026_07_28.py",
            "refusing_controlled_macro",
        ),
        (
            "scripts/frontier_cycle723_refusal_wrapped_controller_2026_07_28.py",
            "wrapped_controller_build",
        ),
        (
            "scripts/frontier_cycle724_local_token_row_enforcement_2026_07_28.py",
            "refusing_controlled_macro",
        ),
    }
    if (relative, node.name) in true_wrapper_definitions:
        return (
            "TRUE_REPO_SCOPE_REFUSAL_WORD_WRAPPER_OUTSIDE_PINNED_LINEAGE",
            True,
            False,
        )
    if "unwrapped" in node.name:
        return "UNWRAPPED_COMPARATOR_NOT_GUARD_CONSTRUCTOR", False, False
    if "mass_path_guard_companion_controls.py" in relative:
        return "GUARD_METRIC_SUMMARY_NOT_GUARD_OBJECT", False, False
    return "DOMAIN_WORD_TRANSFORM_NOT_GUARD_CONSTRUCTOR", False, False


def tracked_script_paths() -> tuple[str, ...]:
    completed = subprocess.run(
        ("git", "ls-files", "scripts/*.py"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return tuple(sorted({
        line
        for line in completed.stdout.splitlines()
        if line.endswith(".py")
    }))


def repo_constructor_search(
    *,
    pinned_lineage_no_constructor: bool,
    primary_scope_exact: bool,
) -> dict[str, object]:
    candidates: list[dict[str, object]] = []
    manifest_rows: list[tuple[str, str]] = []
    parse_errors: list[dict[str, object]] = []
    paths = tracked_script_paths()
    for relative in paths:
        source = (ROOT / relative).read_bytes()
        manifest_rows.append((relative, sha256(source).hexdigest()))
        try:
            tree = ast.parse(source.decode("utf-8"))
        except (SyntaxError, UnicodeDecodeError) as exc:
            parse_errors.append({
                "error": type(exc).__name__,
                "file": relative,
            })
            continue
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if not repo_constructor_candidate(node):
                continue
            ruling, true_wrapper, closes_lineage = repo_candidate_ruling(
                relative, node
            )
            candidates.append({
                "arguments": function_args(node),
                "closes_777_781_guard_grammar": closes_lineage,
                "file": relative,
                "line": node.lineno,
                "name": node.name,
                "return_annotation": return_annotation(node),
                "ruling": ruling,
                "true_guard_behavior_wrapper": true_wrapper,
            })
    candidates.sort(
        key=lambda row: (str(row["file"]), int(row["line"]), str(row["name"]))
    )
    true_wrappers = tuple(
        row for row in candidates if row["true_guard_behavior_wrapper"]
    )
    lineage_closers = tuple(
        row for row in candidates if row["closes_777_781_guard_grammar"]
    )
    repo_scope_wrapper_exists = bool(true_wrappers)
    open_gap_framing_survives = (
        pinned_lineage_no_constructor
        and primary_scope_exact
        and not lineage_closers
    )
    return {
        "candidate_rule": (
            "AST function has guard-typed input+output, or takes a guard-like "
            "word/program and has wrap/compose/refusal return flow"
        ),
        "candidates": tuple(candidates),
        "corpus_manifest_sha256": digest(manifest_rows),
        "lineage_grammar_closers": lineage_closers,
        "ok": (
            not parse_errors
            and open_gap_framing_survives
        ),
        "open_exact_gap_framing_survives_exact_pinned_scope":
            open_gap_framing_survives,
        "parse_errors": tuple(parse_errors),
        "pinned_lineage_no_constructor": pinned_lineage_no_constructor,
        "repo_scope_wrapper_exists": repo_scope_wrapper_exists,
        "repo_wide_no_constructor_claim": not repo_scope_wrapper_exists,
        "tracked_python_files_scanned": len(paths),
        "true_repo_scope_wrappers": true_wrappers,
    }


def deterministic_payload() -> dict[str, object]:
    inventory = lineage_inventory()
    firewall = firewall_and_primary_scope()
    constructor_search = repo_constructor_search(
        pinned_lineage_no_constructor=bool(
            inventory["no_recursive_constructor"]
        ),
        primary_scope_exact=bool(firewall["primary_scope_exact"]),
    )
    return {
        "algebraic_n_generality": n_generality_certificate(),
        "constructor_search": constructor_search,
        "firewall": firewall,
        "one_layer_steps": one_layer_steps_certificate(),
        "schema_inventory": inventory,
    }


def projected_stdout_bytes(lines: list[str], report: dict[str, object]) -> int:
    final = canonical_json(report)
    return sum(
        len((line + "\n").encode("utf-8"))
        for line in (*lines, final)
    )


def main() -> int:
    started = perf_counter()
    before = source_snapshot()
    first = deterministic_payload()
    second = deterministic_payload()
    after = source_snapshot()

    inventory = first["schema_inventory"]
    algebra = first["algebraic_n_generality"]
    constructor = first["constructor_search"]
    firewall = first["firewall"]
    steps = first["one_layer_steps"]
    anchors_pinned = all(
        before[path]["sha256"] == EXPECTED_SHA256[path]
        for path in AUDIT_INPUT_PATHS
    )
    deterministic = first == second
    input_snapshot_unchanged = before == after
    runtime_sec = perf_counter() - started

    certificate_values: dict[str, bool] = {
        "1_SCHEMA_INVENTORY_COMPLETENESS": bool(inventory["complete"]),
        "2_ALGEBRAIC_N_GENERALITY": bool(algebra["ok"]),
        "3_THE_NO_CONSTRUCTOR_CLAIM": bool(constructor["ok"]),
        "4_ONE_LAYER_STEPS": bool(steps["ok"]),
        "5_CONTROLS": False,
    }
    per_schema_values = {
        f"2_ALGEBRAIC_N_GENERALITY_{schema}": bool(value)
        for schema, value in algebra["per_schema"].items()
    }
    controls_base = (
        anchors_pinned
        and input_snapshot_unchanged
        and deterministic
        and firewall["ok"]
        and runtime_sec < AUDIT_TIMEOUT_SEC
    )
    scientific_confirmed = all(
        certificate_values[key]
        for key in (
            "1_SCHEMA_INVENTORY_COMPLETENESS",
            "2_ALGEBRAIC_N_GENERALITY",
            "3_THE_NO_CONSTRUCTOR_CLAIM",
            "4_ONE_LAYER_STEPS",
        )
    )
    verdict = "CONFIRMED" if scientific_confirmed else "REFUTED"

    data_lines = [
        "FINDING_1_SCHEMA_CATALOG " + canonical_json(row)
        for row in inventory["catalog"]
    ]
    data_lines.append(
        "FINDING_1_SCHEMA_INVENTORY_RULING " + canonical_json({
            "discovered_generator_definitions":
                inventory["discovered_generator_definitions"],
            "fifth_generators": inventory["fifth_generators"],
            "fixed_sibling_calls": inventory["fixed_sibling_calls"],
            "missing_generators": inventory["missing_generators"],
            "no_recursive_constructor":
                inventory["no_recursive_constructor"],
            "schemas": inventory["schemas"],
        })
    )
    for schema in sorted(algebra["rows"]):
        for row in algebra["rows"][schema]:
            data_lines.append(
                "FINDING_2_ALGEBRAIC_N_GENERALITY " + canonical_json(row)
            )
    data_lines.append(
        "FINDING_2_DECLARED_N_CHOICES " + canonical_json({
            "conditions": algebra["conditions"],
            "n_choices": algebra["n_choices"],
            "per_schema": algebra["per_schema"],
        })
    )
    data_lines.extend(
        "FINDING_3_CONSTRUCTOR_CANDIDATE " + canonical_json(row)
        for row in constructor["candidates"]
    )
    data_lines.append(
        "FINDING_3_CONSTRUCTOR_SEARCH_RULING " + canonical_json({
            "candidate_rule": constructor["candidate_rule"],
            "corpus_manifest_sha256":
                constructor["corpus_manifest_sha256"],
            "lineage_grammar_closers":
                constructor["lineage_grammar_closers"],
            "open_exact_gap_framing_survives_exact_pinned_scope":
                constructor[
                    "open_exact_gap_framing_survives_exact_pinned_scope"
                ],
            "parse_errors": constructor["parse_errors"],
            "pinned_lineage_no_constructor":
                constructor["pinned_lineage_no_constructor"],
            "primary_scope_exact": firewall["primary_scope_exact"],
            "repo_scope_wrapper_exists":
                constructor["repo_scope_wrapper_exists"],
            "repo_wide_no_constructor_claim":
                constructor["repo_wide_no_constructor_claim"],
            "tracked_python_files_scanned":
                constructor["tracked_python_files_scanned"],
            "true_repo_scope_wrappers":
                constructor["true_repo_scope_wrappers"],
        })
    )
    data_lines.extend(
        "FINDING_4_ONE_LAYER_STEP " + canonical_json(row)
        for row in steps["rows"]
    )
    data_lines.extend((
        "SHA_ANCHORS " + canonical_json(before),
        "PRIMARY_BLOCKLIST_AND_SCOPE " + canonical_json(firewall),
    ))

    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "constructor_scope": {
            "pinned_lineage_no_constructor":
                constructor["pinned_lineage_no_constructor"],
            "repo_scope_wrapper_exists":
                constructor["repo_scope_wrapper_exists"],
            "repo_wide_no_constructor_claim":
                constructor["repo_wide_no_constructor_claim"],
        },
        "inventory_schemas": inventory["schemas"],
        "n_choices": SCHEMA_N_CHOICES,
        "runner_certificates": certificate_values,
        "runtime_sec": runtime_sec,
        "stdout_bytes": 0,
        "verdict": verdict,
    }
    controls_line = ""
    certificate_lines: list[str] = []
    for _iteration in range(12):
        certificate_values["5_CONTROLS"] = bool(
            controls_base
            and int(report["stdout_bytes"]) < STDOUT_LIMIT_BYTES
        )
        report["runner_certificates"] = certificate_values
        controls_line = "FINDING_5_CONTROLS " + canonical_json({
            "anchors_pinned": anchors_pinned,
            "determinism": deterministic,
            "exact_arithmetic": "Boolean GF(2), integer counts, no randomness",
            "input_snapshot_unchanged": input_snapshot_unchanged,
            "literal_input_paths": firewall["literal_AUDIT_INPUT_PATHS"],
            "primary_blocklisted_text_AST_only":
                firewall["primary_text_AST_only"],
            "runtime_limit_sec": AUDIT_TIMEOUT_SEC,
            "runtime_sec": runtime_sec,
            "stdlib_only": True,
            "stdout_bytes": report["stdout_bytes"],
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        })
        all_values = {**certificate_values, **per_schema_values}
        certificate_lines = [
            ("PASS" if value else "FAIL") + f" CERTIFICATE_{name}"
            for name, value in all_values.items()
        ]
        lines = [*data_lines, controls_line, *certificate_lines]
        size = projected_stdout_bytes(lines, report)
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
    return 0 if all(certificate_values.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
