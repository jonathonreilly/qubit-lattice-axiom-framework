#!/usr/bin/env python3
"""Cycle 807: close the guard regress over the landed 777/781 grammar.

The four lineage programs are immutable text/AST evidence.  This runner does
not import or execute them.  It independently implements their Boolean wiring
algebra and proves the recursive fanout-closure defeater by structural
induction over the exact typed wrapper grammar extracted below.
"""

from __future__ import annotations

import ast
from collections import deque
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
from time import perf_counter
from typing import Iterable


AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200_000
ENUMERATION_DEPTH = 2
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
GRAMMAR_EQUATIONS = (
    "P ::= LOCK | RAIL(P)",
    "G ::= P | SINGLE(G) | MAJORITY3(G) | REFRESH(G)",
)
DEFEAT_EQUATIONS = (
    "Delta(LOCK)={D}",
    "Delta(RAIL(g))=Delta(g) union {outer_D(i):i in Delta(g)}",
    "Delta(SINGLE(g))=Delta(g) union copy_1(Delta(g))",
    "Delta(MAJORITY3(g))=Delta(g) union copy_1(Delta(g)) "
    "union copy_2(Delta(g)) union copy_3(Delta(g))",
    "Delta(REFRESH(g))=Delta(g) union fresh_copy(Delta(g))",
    "defeat(g)=product_{i in Delta(g)} X(i), after engagement and before "
    "one outer-to-inner boundary sweep",
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
    snapshot: dict[str, dict[str, object]] = {}
    for relative in AUDIT_INPUT_PATHS:
        source = (ROOT / relative).read_bytes()
        snapshot[relative] = {
            "ast_sha256": ast_digest(source),
            "bytes": len(source),
            "sha256": sha256(source).hexdigest(),
        }
    return snapshot


def imported_modules(tree: ast.AST) -> tuple[str, ...]:
    names: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.append(node.module)
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "import_module"
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
        ):
            names.append(node.args[0].value)
    return tuple(names)


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


def node_calls(node: ast.AST) -> tuple[str, ...]:
    return tuple(
        sorted({
            ast.unparse(item.func)
            for item in ast.walk(node)
            if isinstance(item, ast.Call)
        })
    )


def source_firewall_and_provenance() -> dict[str, object]:
    own_source = Path(__file__).read_text(encoding="utf-8")
    own_tree = ast.parse(own_source)
    imports = imported_modules(own_tree)
    literal_paths = assignment_literal(own_tree, "AUDIT_INPUT_PATHS")
    blocked_hits = tuple(sorted(set(imports).intersection(BLOCKLISTED_MODULES)))
    dangerous_calls = tuple(sorted({
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
        relative: ast.parse(
            (ROOT / relative).read_text(encoding="utf-8")
        )
        for relative in AUDIT_INPUT_PATHS
    }
    p777 = AUDIT_INPUT_PATHS[0]
    i777 = AUDIT_INPUT_PATHS[1]
    p781 = AUDIT_INPUT_PATHS[2]
    i781 = AUDIT_INPUT_PATHS[3]
    required_nodes = {
        p777: {
            "RailGuard": (82, 88),
            "build_rail_guard": (280, 297),
        },
        i777: {
            "build_guard": (419, 436),
        },
        p781: {
            "first_write_events": (261, 275),
            "build_guard_events": (278, 295),
            "compile_guard_words": (403, 435),
        },
        i781: {
            "GuardProgram": (823, 832),
            "apply_compiled_word": (843, 854),
            "compile_single_checkpoint": (857, 901),
            "compile_majority_three": (904, 978),
            "fanout_closure": (1314, 1329),
            "adaptive_null_attack": (1332, 1369),
            "regress_theorem_candidate": (1372, 1414),
        },
    }
    observed_nodes: dict[str, dict[str, object]] = {}
    node_ranges_exact = True
    for relative, wanted in required_nodes.items():
        observed_nodes[relative] = {}
        for name, expected_range in wanted.items():
            node = named_node(trees[relative], name)
            observed_range = (node.lineno, node.end_lineno)
            calls = node_calls(node)
            observed_nodes[relative][name] = {
                "calls": calls,
                "line_range": observed_range,
            }
            node_ranges_exact &= observed_range == expected_range

    single = named_node(trees[i781], "compile_single_checkpoint")
    majority = named_node(trees[i781], "compile_majority_three")
    rail = named_node(trees[p777], "build_rail_guard")
    apply_word = named_node(trees[i781], "apply_compiled_word")
    refresh_calls = tuple(
        node
        for node in ast.walk(named_node(trees[i781], "main"))
        if isinstance(node, ast.Call)
        and ast.unparse(node.func) == "compile_single_checkpoint"
        and any(
            keyword.arg == "name"
            and isinstance(keyword.value, ast.Constant)
            and keyword.value.value == "refresh"
            for keyword in node.keywords
        )
    )
    i781_strings = {
        node.value
        for node in ast.walk(trees[i781])
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    p777_strings = {
        node.value
        for node in ast.walk(trees[p777])
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    constructor_shapes = {
        "LOCK": (
            "C745.apply_word"
            in node_calls(named_node(trees[p781], "first_write_events"))
        ),
        "RAIL": (
            {"C745.apply_word", "C745.packet", "C745.persistent"}
            .issubset(node_calls(rail))
            and any(
                "finite recursive Cycle745 composition" in text
                for text in p777_strings
            )
        ),
        "SINGLE": (
            "live_width" in tuple(arg.arg for arg in single.args.args)
            and "K719.A.cn" in node_calls(single)
            and "GuardProgram" in node_calls(single)
        ),
        "MAJORITY3": (
            "live_width" in tuple(arg.arg for arg in majority.args.args)
            and {"K719.A.cn", "K719.A.tof", "GuardProgram"}
            .issubset(node_calls(majority))
        ),
        "REFRESH": (
            len(refresh_calls) == 1
            and refresh_calls[0].lineno == 1489
            and refresh_calls[0].end_lineno == 1505
            and "fresh zero bank at every station boundary" in i781_strings
        ),
        "FINITE_WORD_COMPOSITION": (
            {"X", "CNOT", "TOF"}.issubset(i781_strings)
            and isinstance(apply_word, ast.FunctionDef)
        ),
    }
    citations = {
        "LOCK": f"{p781}:261-275",
        "RAIL": f"{p777}:280-297",
        "RAIL_INDEPENDENT_REBUILD": f"{i777}:419-436",
        "SINGLE_ORIGINAL": f"{p781}:403-435",
        "SINGLE_PARAMETRIC": f"{i781}:857-901",
        "MAJORITY3": f"{i781}:904-978",
        "REFRESH_SCHEDULE": f"{i781}:1489-1505",
        "WORD_SEQUENCING": f"{i781}:843-854",
        "DEFEATER_PATTERN": f"{i781}:1314-1369",
        "REGRESS_SCOPE": f"{i781}:1372-1414",
    }
    return {
        "blocked_import_hits": blocked_hits,
        "constructor_shapes": constructor_shapes,
        "dangerous_execution_calls": dangerous_calls,
        "grammar_citations": citations,
        "imports": imports,
        "literal_AUDIT_INPUT_PATHS": literal_paths,
        "node_ranges_exact": node_ranges_exact,
        "observed_nodes": observed_nodes,
        "ok": (
            literal_paths == AUDIT_INPUT_PATHS
            and all(path_checks.values())
            and not blocked_hits
            and not dangerous_calls
            and node_ranges_exact
            and all(constructor_shapes.values())
        ),
        "path_checks": path_checks,
        "text_AST_only": True,
    }


@dataclass(frozen=True)
class Term:
    kind: str
    child: Term | None = None

    @property
    def depth(self) -> int:
        return 0 if self.child is None else self.child.depth + 1

    @property
    def label(self) -> str:
        if self.child is None:
            return self.kind
        return f"{self.kind}({self.child.label})"


def lock_term() -> Term:
    return Term("LOCK")


def is_persistent(term: Term) -> bool:
    return term.kind == "LOCK" or (
        term.kind == "RAIL"
        and term.child is not None
        and is_persistent(term.child)
    )


def wrap(kind: str, child: Term) -> Term:
    if kind == "RAIL" and not is_persistent(child):
        raise ValueError("RAIL accepts only the persistent sort P")
    if kind not in {"RAIL", "SINGLE", "MAJORITY3", "REFRESH"}:
        raise ValueError(kind)
    return Term(kind, child)


def enumerate_grammar(max_depth: int) -> tuple[Term, ...]:
    exact: dict[int, tuple[Term, ...]] = {0: (lock_term(),)}
    persistent_exact: dict[int, tuple[Term, ...]] = {0: (lock_term(),)}
    for depth in range(1, max_depth + 1):
        persistent_exact[depth] = tuple(
            wrap("RAIL", child) for child in persistent_exact[depth - 1]
        )
        checkpoint_terms = tuple(
            wrap(kind, child)
            for child in exact[depth - 1]
            for kind in ("SINGLE", "MAJORITY3", "REFRESH")
        )
        exact[depth] = (*persistent_exact[depth], *checkpoint_terms)
    return tuple(
        term
        for depth in range(max_depth + 1)
        for term in exact[depth]
    )


@dataclass(frozen=True)
class Gate:
    kind: str
    wires: tuple[int, ...]


@dataclass(frozen=True)
class GuardModel:
    term: Term
    width: int
    code0: tuple[int, ...]
    code1: tuple[int, ...]
    boundary_word: tuple[Gate, ...]
    receipt_indices: tuple[int, ...]
    local_receipt_indices: tuple[int, ...]
    fanout_edges: tuple[tuple[int, int], ...]
    payload_index: int


def cnot(control: int, target: int) -> Gate:
    return Gate("CNOT", (control, target))


def tof(first: int, second: int, target: int) -> Gate:
    return Gate("TOF", (first, second, target))


def x_gate(wire: int) -> Gate:
    return Gate("X", (wire,))


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
            raise ValueError(f"non-landed gate kind {gate.kind}")


def rail_codeword(
    child_word: tuple[int, ...],
    lock_constants: tuple[int, int],
) -> tuple[int, ...]:
    return (
        *child_word,
        *(
            bit
            for child_bit in child_word
            for bit in (child_bit, *lock_constants)
        ),
    )


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
        for left in range(len(quartet_starts))
        for right in range(left + 1, len(quartet_starts))
    )
    pairwise_start = 4 * width
    majority_start = pairwise_start + len(pairs) * width
    correction_start = majority_start + width
    output: list[Gate] = []
    for pair_index, (left, right) in enumerate(pairs):
        pair_output = pairwise_start + pair_index * width
        for index in range(width):
            output.extend((
                cnot(quartet_starts[left] + index, pair_output + index),
                cnot(quartet_starts[right] + index, pair_output + index),
            ))
    first, second, third = copies
    for index in range(width):
        majority = majority_start + index
        output.extend((
            tof(first + index, second + index, majority),
            tof(first + index, third + index, majority),
            tof(second + index, third + index, majority),
        ))
    for target_number, target_start in enumerate(quartet_starts):
        correction = correction_start + target_number * width
        for index in range(width):
            output.extend((
                cnot(target_start + index, correction + index),
                cnot(majority_start + index, correction + index),
                cnot(correction + index, target_start + index),
            ))
    return tuple(output)


def compile_term(
    term: Term,
    lock_constants: tuple[int, int],
) -> GuardModel:
    if term.kind == "LOCK":
        return GuardModel(
            term=term,
            width=3,
            code0=(0, *lock_constants),
            code1=(1, *lock_constants),
            boundary_word=(),
            receipt_indices=(),
            local_receipt_indices=(),
            fanout_edges=(),
            payload_index=0,
        )
    if term.child is None:
        raise ValueError(f"{term.kind} has no child")
    child = compile_term(term.child, lock_constants)
    width = child.width
    if term.kind == "RAIL":
        edges = (
            *child.fanout_edges,
            *((index, width + 3 * index) for index in range(width)),
        )
        return GuardModel(
            term=term,
            width=4 * width,
            code0=rail_codeword(child.code0, lock_constants),
            code1=rail_codeword(child.code1, lock_constants),
            boundary_word=child.boundary_word,
            receipt_indices=child.receipt_indices,
            local_receipt_indices=(),
            fanout_edges=edges,
            payload_index=child.payload_index,
        )
    if term.kind in {"SINGLE", "REFRESH"}:
        local_receipts = tuple(range(2 * width, 3 * width))
        edges = (
            *child.fanout_edges,
            *((index, width + index) for index in range(width)),
        )
        return GuardModel(
            term=term,
            width=3 * width,
            code0=(*child.code0, *child.code0, *(0,) * width),
            code1=(*child.code1, *child.code1, *(0,) * width),
            boundary_word=(*single_boundary(width), *child.boundary_word),
            receipt_indices=(*child.receipt_indices, *local_receipts),
            local_receipt_indices=local_receipts,
            fanout_edges=edges,
            payload_index=child.payload_index,
        )
    if term.kind == "MAJORITY3":
        local_receipts = tuple(range(4 * width, 10 * width))
        edges = (
            *child.fanout_edges,
            *(
                (index, copy + index)
                for index in range(width)
                for copy in (width, 2 * width, 3 * width)
            ),
        )
        return GuardModel(
            term=term,
            width=15 * width,
            code0=(*child.code0, *child.code0, *child.code0, *child.code0,
                   *(0,) * (11 * width)),
            code1=(*child.code1, *child.code1, *child.code1, *child.code1,
                   *(0,) * (11 * width)),
            boundary_word=(*majority_boundary(width), *child.boundary_word),
            receipt_indices=(*child.receipt_indices, *local_receipts),
            local_receipt_indices=local_receipts,
            fanout_edges=edges,
            payload_index=child.payload_index,
        )
    raise ValueError(term.kind)


def fanout_closure(
    seed: int,
    edges: tuple[tuple[int, int], ...],
) -> tuple[int, ...]:
    adjacency: dict[int, list[int]] = {}
    for source, target in edges:
        adjacency.setdefault(source, []).append(target)
    visited = {seed}
    queue = deque((seed,))
    while queue:
        source = queue.popleft()
        for target in adjacency.get(source, ()):
            if target not in visited:
                visited.add(target)
                queue.append(target)
    return tuple(sorted(visited))


@dataclass(frozen=True)
class Defeater:
    mask: tuple[int, ...]
    word: tuple[Gate, ...]
    equation: str
    boundary_schedule: tuple[str, ...]


def boundary_schedule(term: Term) -> tuple[str, ...]:
    if term.kind == "LOCK":
        return ()
    if term.child is None:
        raise ValueError(term.kind)
    if term.kind == "RAIL":
        return boundary_schedule(term.child)
    return (term.kind, *boundary_schedule(term.child))


def defeat(
    term: Term,
    lock_constants: tuple[int, int],
) -> Defeater:
    """The single structural-recursion constructor required by certificate B."""
    if term.kind == "LOCK":
        mask = (1, 0, 0)
        equation = DEFEAT_EQUATIONS[0]
    else:
        if term.child is None:
            raise ValueError(term.kind)
        child_model = compile_term(term.child, lock_constants)
        child_defeater = defeat(term.child, lock_constants)
        child_mask = child_defeater.mask
        width = child_model.width
        if term.kind == "RAIL":
            mask = (
                *child_mask,
                *(
                    bit
                    for changed in child_mask
                    for bit in (changed, 0, 0)
                ),
            )
            equation = DEFEAT_EQUATIONS[1]
        elif term.kind in {"SINGLE", "REFRESH"}:
            mask = (*child_mask, *child_mask, *(0,) * width)
            equation = (
                DEFEAT_EQUATIONS[2]
                if term.kind == "SINGLE"
                else DEFEAT_EQUATIONS[4]
            )
        elif term.kind == "MAJORITY3":
            mask = (
                *child_mask, *child_mask, *child_mask, *child_mask,
                *(0,) * (11 * width),
            )
            equation = DEFEAT_EQUATIONS[3]
        else:
            raise ValueError(term.kind)
    word = tuple(x_gate(index) for index, bit in enumerate(mask) if bit)
    return Defeater(
        mask=mask,
        word=word,
        equation=equation,
        boundary_schedule=boundary_schedule(term),
    )
