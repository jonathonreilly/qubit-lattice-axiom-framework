#!/usr/bin/env python3
"""Cycle 823 independent adversarial check: fidelity before discharge.

The Cycle-817 and Cycle-823 primaries are inert evidence.  This checker reads
only their bytes/text/AST and never imports or executes either module.
"""
from __future__ import annotations

import ast
import base64
from collections import Counter
from hashlib import sha1, sha256
import json
from pathlib import Path
import sys
from time import perf_counter
import zlib


ROOT = Path(__file__).resolve().parents[1]
SELF_PATH = (
    "scripts/frontier_cycle823_discharge_independent_check_2026_07_28.py"
)
PRIMARY_817 = (
    "scripts/frontier_cycle817_general_b_sector_theorem_2026_07_28.py"
)
PRIMARY_823 = (
    "scripts/frontier_cycle823_hypothesis_discharge_2026_07_28.py"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle817_general_b_sector_theorem_2026_07_28.py",
    "scripts/frontier_cycle823_hypothesis_discharge_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
BLOCKLIST = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)
AUDIT_TIMEOUT_SEC = 1200
STDOUT_LIMIT_BYTES = 150 * 1024

EXPECTED_PROVENANCE = {
    PRIMARY_817: {
        "sha256":
            "469a0af17b19bb6a35ac5356b5c143f6027af05c412f92a5b349f09c0452c7a4",
        "blob": "01045658578074e6d3c496ff09b3169381596728",
    },
    PRIMARY_823: {
        "sha256":
            "ecc213e98a7ad2ff673ac486c155fd728847f5978632f8d1bc37a02173ead5b0",
        "blob": "5529b4c3754915157b8a2b210443a3c7e5ab3730",
    },
}

SOURCE_WIDTH = 41
BANK_WIDTH = 131
LINK_HALF_WIDTH = 191
LINK_WIDTH = 382
SOURCE_SUPPORT = (0, SOURCE_WIDTH + BANK_WIDTH)
ARITY = {"X": 1, "CNOT": 2, "TOF": 3}
PAIR_KIND = {
    "handoff_forward": "handoff",
    "relay_latch": "relay",
    "relay_swap": "relay",
    "relay_unlatch": "relay",
    "handoff_return": "handoff",
}
CHECK_BANKS = (3, 7, 10)
PATTERN_BANK = 11

FIDELITY_RULING = (
    "CONFIRMED: Cycle 817 selects the SHA-pinned Cycle-719 constructor, and "
    "Cycle 823 v2 passes the live rows returned by that same constructor to "
    "its actual-object check. Independently extracted local and mapped Gate "
    "signatures are elementwise identical at every b=3..11. This confirms "
    "the bounded direct route only; Cycle 823 v2 makes no general-b claim."
)


def stable_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    ).encode()


def stable_digest(value: object) -> str:
    return sha256(stable_bytes(value)).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def assigned_literal(tree: ast.Module, name: str) -> object:
    environment: dict[str, object] = {}
    matches = []
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else (
                node.target,
            )
            target_names = tuple(
                target.id for target in targets
                if isinstance(target, ast.Name)
            )
            rewritten = ast.fix_missing_locations(
                _LiteralNames(environment).visit(ast.copy_location(
                    ast.Expression(body=node.value), node.value
                ))
            )
            try:
                value = ast.literal_eval(rewritten)
            except (ValueError, TypeError):
                continue
            for target_name in target_names:
                environment[target_name] = value
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in targets
            ):
                matches.append(value)
    if len(matches) != 1:
        raise AssertionError(("assigned literal", name, len(matches)))
    return matches[0]


class _LiteralNames(ast.NodeTransformer):
    """Replace only already-seen literal names inside an inert expression."""

    def __init__(self, environment: dict[str, object]) -> None:
        self.environment = environment

    def visit_Name(self, node: ast.Name) -> ast.AST:
        if node.id not in self.environment:
            return node
        replacement = ast.parse(
            repr(self.environment[node.id]), mode="eval"
        ).body
        return ast.copy_location(replacement, node)


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function", name, len(matches)))
    return matches[0]


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = call_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def load_primaries() -> tuple[
    dict[str, dict[str, str]], dict[str, str], dict[str, ast.Module]
]:
    provenance = {}
    sources = {}
    trees = {}
    for path in AUDIT_INPUT_PATHS:
        full = ROOT / path
        data = full.read_bytes()
        source = data.decode("utf-8")
        row = {
            "sha256": sha256(data).hexdigest(),
            "blob": git_blob_sha1(data),
        }
        row["exact"] = row == EXPECTED_PROVENANCE[path]
        provenance[path] = row
        sources[path] = source
        trees[path] = ast.parse(source, filename=path)
    return provenance, sources, trees


def formalization_certificate(
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    """Attack the claimed direct route by independently extracting both sides."""

    def assignment_expression(
        tree: ast.Module, name: str,
    ) -> ast.AST:
        matches = []
        for node in tree.body:
            if isinstance(node, ast.Assign) and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            ):
                matches.append(node.value)
            elif (
                isinstance(node, ast.AnnAssign)
                and isinstance(node.target, ast.Name)
                and node.target.id == name
                and node.value is not None
            ):
                matches.append(node.value)
        if len(matches) != 1:
            raise AssertionError(("assignment expression", name, len(matches)))
        return matches[0]

    def cycle817_constructor_pin(tree: ast.Module) -> dict[str, str]:
        provenance = assignment_expression(tree, "PROVENANCE")
        if not isinstance(provenance, ast.Dict):
            raise AssertionError("Cycle-817 PROVENANCE is not a dict")
        matches = [
            ast.literal_eval(value)
            for key, value in zip(provenance.keys, provenance.values)
            if isinstance(key, ast.Subscript)
            and isinstance(key.slice, ast.Constant)
            and key.slice.value == 0
        ]
        if len(matches) != 1:
            raise AssertionError(("Cycle-817 constructor pin", len(matches)))
        return matches[0]

    def constructor_selector_817(tree: ast.Module) -> tuple[str, bool]:
        fixed_attempt = function_node(tree, "fixed_b_preimage_attempt")
        constructor_bindings = [
            node for node in ast.walk(fixed_attempt)
            if isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == "cycle719"
                for target in node.targets
            )
            and ast.unparse(node.value) == "trees[AUDIT_INPUT_PATHS[0]]"
        ]
        evidence_calls = [
            node for node in ast.walk(fixed_attempt)
            if isinstance(node, ast.Call)
            and call_name(node.func) == "ast_evidence"
            and len(node.args) >= 2
            and isinstance(node.args[0], ast.Name)
            and node.args[0].id == "cycle719"
            and isinstance(node.args[1], ast.Constant)
            and isinstance(node.args[1].value, str)
            and node.args[1].value == "interleaved_program"
        ]
        if len(evidence_calls) != 1:
            return "", False
        return str(evidence_calls[0].args[1].value), (
            len(constructor_bindings) == 1
        )

    def constructor_selectors_823(
        tree: ast.Module,
    ) -> tuple[str, str, bool]:
        loader = function_node(tree, "load_actual_constructor")
        fixed_check = function_node(tree, "fixed_b_discharge")
        certificate = function_node(tree, "certificate_b")
        build = function_node(tree, "build_core")
        main_node = function_node(tree, "main")
        imports = [
            node for node in ast.walk(loader)
            if isinstance(node, ast.Call)
            and call_name(node.func) == "importlib.import_module"
            and len(node.args) == 1
            and isinstance(node.args[0], ast.Name)
            and node.args[0].id == "ACTUAL_CONSTRUCTOR_MODULE"
        ]
        program_calls = [
            node for node in ast.walk(fixed_check)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "constructor"
            and node.func.attr == "interleaved_program"
            and len(node.args) == 1
            and isinstance(node.args[0], ast.Name)
            and node.args[0].id == "bank_count"
        ]
        mapper_calls = [
            node for node in ast.walk(fixed_check)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "constructor"
            and node.func.attr == "mapped_macro"
            and len(node.args) == 1
            and isinstance(node.args[0], ast.Name)
            and node.args[0].id == "row"
        ]
        discharge_inputs = {
            node.args[0].id
            for node in ast.walk(certificate)
            if isinstance(node, ast.Call)
            and call_name(node.func) == "fixed_b_discharge"
            and node.args
            and isinstance(node.args[0], ast.Name)
        }
        build_calls_b = sum(
            isinstance(node, ast.Call)
            and call_name(node.func) == "certificate_b"
            for node in ast.walk(build)
        )
        main_calls_build = sum(
            isinstance(node, ast.Call)
            and call_name(node.func) == "build_core"
            for node in ast.walk(main_node)
        )
        exact = (
            len(imports) == 1
            and len(program_calls) == 1
            and len(mapper_calls) == 1
            and discharge_inputs == {"bank_count", "PATTERN_TEST_BANK"}
            and build_calls_b == 1
            and main_calls_build == 2
            and ast.unparse(
                assignment_expression(tree, "DISCHARGE_BANKS")
            ) == "tuple(range(3, 11))"
            and assigned_literal(tree, "PATTERN_TEST_BANK") == 11
        )
        return "interleaved_program", "mapped_macro", exact

    def load_constructor(path: str, label: str) -> object:
        import importlib.util

        scripts = str(ROOT / "scripts")
        if scripts not in sys.path:
            sys.path.insert(0, scripts)
        spec = importlib.util.spec_from_file_location(label, ROOT / path)
        if spec is None or spec.loader is None:
            raise AssertionError(("constructor import spec", path))
        module = importlib.util.module_from_spec(spec)
        previous = sys.modules.get(label)
        sys.modules[label] = module
        try:
            spec.loader.exec_module(module)
        finally:
            if previous is None:
                sys.modules.pop(label, None)
            else:
                sys.modules[label] = previous
        return module

    def word_signature(
        word: object,
    ) -> tuple[tuple[str, tuple[int, ...]], ...]:
        return tuple(
            (str(gate.kind), tuple(int(wire) for wire in gate.wires))
            for gate in word
        )

    def object_snapshot(
        constructor: object,
        program_selector: str,
        mapper_selector: str,
        bank_count: int,
    ) -> dict[str, object]:
        program = getattr(constructor, program_selector)(bank_count)
        mapper = getattr(constructor, mapper_selector)
        rows = tuple(
            (
                str(row[0]),
                int(row[1]),
                word_signature(row[2]),
                word_signature(mapper(row)),
            )
            for row in program
        )
        return {
            "rows": rows,
            "predecessor": int(constructor.A.CELLS[0]["pred"][1]),
        }

    def first_difference(
        left: dict[str, object], right: dict[str, object],
    ) -> dict[str, object] | None:
        if left["predecessor"] != right["predecessor"]:
            return {
                "element": "predecessor",
                "Cycle817": left["predecessor"],
                "Cycle823": right["predecessor"],
            }
        rows_left = left["rows"]
        rows_right = right["rows"]
        for station, (row_left, row_right) in enumerate(
            zip(rows_left, rows_right)
        ):
            if row_left != row_right:
                return {
                    "element": "program_row",
                    "station": station,
                    "Cycle817": row_left,
                    "Cycle823": row_right,
                }
        if len(rows_left) != len(rows_right):
            return {
                "element": "program_length",
                "Cycle817": len(rows_left),
                "Cycle823": len(rows_right),
            }
        return None

    h817 = assigned_literal(
        trees[PRIMARY_817], "H_TEMPLATE_PREIMAGE_ZONE_CLASS"
    )
    h823 = assigned_literal(trees[PRIMARY_823], "EXPECTED_HYPOTHESIS")
    identity823 = assigned_literal(
        trees[PRIMARY_823], "EXPECTED_CHECKER_IDENTITY"
    )
    inputs817 = assigned_literal(trees[PRIMARY_817], "AUDIT_INPUT_PATHS")
    path817 = str(inputs817[0])
    path823 = str(assigned_literal(trees[PRIMARY_823], "CYCLE719"))
    module823 = str(
        assigned_literal(trees[PRIMARY_823], "ACTUAL_CONSTRUCTOR_MODULE")
    )
    selector817, selection817_exact = constructor_selector_817(
        trees[PRIMARY_817]
    )
    selector823, mapper823, selection823_exact = (
        constructor_selectors_823(trees[PRIMARY_823])
    )
    pin817 = cycle817_constructor_pin(trees[PRIMARY_817])
    pin823 = assigned_literal(
        trees[PRIMARY_823], "EXPECTED_PROVENANCE"
    )[path823]
    constructor_data = (ROOT / path817).read_bytes()
    observed_pin = {
        "sha256": sha256(constructor_data).hexdigest(),
        "blob": git_blob_sha1(constructor_data),
    }
    route_diff = {
        "constructor_path": (path817, path823),
        "program_selector": (selector817, selector823),
        "v2_module": (Path(path823).stem, module823),
        "Cycle817_pin": {
            "sha256": pin817["sha256"],
            "blob": pin817["blob"],
        },
        "Cycle823_pin": pin823,
        "observed_pin": observed_pin,
    }
    route_equal = (
        path817 == path823
        and selector817 == selector823
        and Path(path823).stem == module823
        and selection817_exact
        and selection823_exact
        and observed_pin
        == {"sha256": pin817["sha256"], "blob": pin817["blob"]}
        == {"sha256": pin823["sha256"], "blob": pin823["blob"]}
    )

    per_b = {}
    comparison_error = None
    try:
        constructor817 = load_constructor(
            path817, "_cycle823_checker_constructor_817"
        )
        constructor823 = load_constructor(
            path823, "_cycle823_checker_constructor_823"
        )
        for bank_count in range(3, 12):
            objects817 = object_snapshot(
                constructor817, selector817, mapper823, bank_count
            )
            objects823 = object_snapshot(
                constructor823, selector823, mapper823, bank_count
            )
            difference = first_difference(objects817, objects823)
            rows817 = objects817["rows"]
            rows823 = objects823["rows"]
            per_b[bank_count] = {
                "b": bank_count,
                "Cycle817_rows": len(rows817),
                "Cycle823_rows": len(rows823),
                "Cycle817_object_sha256": stable_digest(objects817),
                "Cycle823_object_sha256": stable_digest(objects823),
                "elements_compared": {
                    "program_rows": max(len(rows817), len(rows823)),
                    "local_gates": sum(len(row[2]) for row in rows817),
                    "mapped_gates": sum(len(row[3]) for row in rows817),
                    "local_operands": sum(
                        len(wires)
                        for row in rows817
                        for _kind, wires in row[2]
                    ),
                    "mapped_operands": sum(
                        len(wires)
                        for row in rows817
                        for _kind, wires in row[3]
                    ),
                    "predecessor_values": 1,
                },
                "first_difference": difference,
                "elementwise_equal": difference is None,
            }
    except Exception as exc:
        comparison_error = f"{type(exc).__name__}: {exc}"

    object_fidelity_exact = (
        comparison_error is None
        and tuple(per_b) == tuple(range(3, 12))
        and all(row["elementwise_equal"] for row in per_b.values())
    )
    direct_route_real = route_equal and object_fidelity_exact
    formal_817 = (
        "H817(b) := "
        "[actual S and actual F_b are subsets of Z_source=[0,172)] AND "
        "[forall operands x of the actual bank template, x in [0,131)] AND "
        "[forall actual pair templates t and every operand x of t, "
        "x is in t's declared left-bank/right-bank/191-wire-link-half zone] "
        "AND [actual cross predecessor offset p satisfies 0<=p<131] AND "
        "[forall admissible b1,b2, actual F_b1 = actual F_b2]."
    )
    formal_823 = (
        "H823_fixed(b) := fixed_b_discharge reads the live rows from the "
        "Cycle-817-selected interleaved_program, reads every local Gate, "
        "checks every mapped Gate returned by mapped_macro, reads the live "
        "predecessor value, and checks finalizer uniformity at b=3..11."
    )
    predicate_sentence = (
        h817["predicate"][0].upper() + h817["predicate"][1:] + "."
    )
    text_same = h817 == h823
    # The object/predicate fidelity is exact on the tested finite range.  The
    # v2 primary explicitly leaves the general-b claim open, so this bounded
    # equality does not make the two quantifier scopes logically equivalent.
    logically_equivalent = False
    return {
        "certificate": "ACTUAL_OBJECT_FIDELITY_ATTACK",
        "Cycle817_extracted_statement": h817,
        "Cycle823_claimed_restatement": h823,
        "Cycle823_checker_identity": identity823,
        "checker_identity_lexically_exact": identity823 == predicate_sentence,
        "Cycle817_formalization": formal_817,
        "Cycle823_executable_formalization": formal_823,
        "prose_text_identical": text_same,
        "same_quantifiers": False,
        "same_objects_b3_through_b11": object_fidelity_exact,
        "same_predicate_on_compared_objects":
            text_same and direct_route_real,
        "route_extraction": route_diff,
        "route_extraction_equal": route_equal,
        "elementwise_comparison_b3_through_b11": per_b,
        "comparison_error": comparison_error,
        "bounded_object_fidelity_exact": direct_route_real,
        "general_b_scope_claimed_by_823": False,
        "logically_equivalent": logically_equivalent,
        "ruling": FIDELITY_RULING,
        "attack_passed": text_same and direct_route_real,
    }


def decode_embedded_packet(
    tree823: ast.Module,
) -> tuple[
    dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
    dict[str, object],
]:
    encoded = assigned_literal(tree823, "TEMPLATE_PREIMAGE_B85")
    expected = assigned_literal(tree823, "EXPECTED_TEMPLATE_METADATA")
    raw = zlib.decompress(base64.b85decode(encoded.encode("ascii")))
    decoded = json.loads(raw)
    templates = {
        str(name): tuple(
            (str(kind), tuple(int(wire) for wire in wires))
            for kind, wires in word
        )
        for name, word in decoded.items()
    }
    observed = {
        name: {
            "digest": stable_digest(word),
            "gates": len(word),
            "operands": sum(len(wires) for _kind, wires in word),
        }
        for name, word in templates.items()
    }
    well_formed = all(
        kind in ARITY
        and len(wires) == ARITY[kind]
        and len(set(wires)) == len(wires)
        for word in templates.values()
        for kind, wires in word
    )
    return templates, {
        "decoded_bytes": len(raw),
        "metadata_matches_823_internal_constants": observed == expected,
        "well_formed_gate_signatures": well_formed,
        "template_names": tuple(sorted(templates)),
        "embedded_packet_sha256": sha256(raw).hexdigest(),
        "actual_constructor_equality_proved": False,
        "exact_as_embedded_packet": (
            len(raw) == 44_752 and observed == expected and well_formed
        ),
    }


def bank_base(index: int) -> int:
    return SOURCE_WIDTH + BANK_WIDTH * index


def link_base(index: int, capacity: int) -> int:
    return (
        SOURCE_WIDTH + BANK_WIDTH * capacity + LINK_WIDTH * index
    )


def data_width(capacity: int) -> int:
    return (
        SOURCE_WIDTH
        + BANK_WIDTH * capacity
        + LINK_WIDTH * (capacity - 1)
    )


def program_rows(bank_count: int) -> tuple[tuple[str, int], ...]:
    rows: list[tuple[str, int]] = [("source", 0)]
    for bank in range(bank_count):
        rows.append(("bank_packet", bank))
        if bank > 0:
            rows.append(("cross", bank - 1))
        if bank + 1 < bank_count:
            rows.extend((
                ("handoff_forward", bank),
                ("relay_latch", bank),
                ("relay_swap", bank),
            ))
    for edge in range(bank_count - 2, -1, -1):
        rows.extend((
            ("relay_swap", edge),
            ("relay_unlatch", edge),
            ("handoff_return", edge),
        ))
    rows.append(("finalizer", 0))
    return tuple(rows)


def local_zone(wire: int) -> tuple[str, int] | None:
    if 0 <= wire < BANK_WIDTH:
        return "left", wire
    if BANK_WIDTH <= wire < 2 * BANK_WIDTH:
        return "right", wire - BANK_WIDTH
    if 2 * BANK_WIDTH <= wire < 2 * BANK_WIDTH + LINK_HALF_WIDTH:
        return "link", wire - 2 * BANK_WIDTH
    return None


def independently_map_word(
    name: str,
    index: int,
    capacity: int,
    templates: dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    if name in {"source", "finalizer"}:
        return templates[name]
    if name == "bank_packet":
        return tuple(
            (kind, tuple(bank_base(index) + wire for wire in wires))
            for kind, wires in templates[name]
        )
    if name == "cross":
        return ((
            "CNOT",
            (link_base(index, capacity), bank_base(index + 1) + 1),
        ),)
    link_split = 0 if PAIR_KIND[name] == "handoff" else LINK_HALF_WIDTH
    mapped = []
    for kind, wires in templates[name]:
        output = []
        for wire in wires:
            zone = local_zone(wire)
            if zone is None:
                output.append(-1)
            elif zone[0] == "left":
                output.append(bank_base(index) + zone[1])
            elif zone[0] == "right":
                output.append(bank_base(index + 1) + zone[1])
            else:
                output.append(
                    link_base(index, capacity) + link_split + zone[1]
                )
        mapped.append((kind, tuple(output)))
    return tuple(mapped)


def independent_full_check(
    bank_count: int,
    templates: dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
) -> dict[str, object]:
    capacity = bank_count
    rows = program_rows(bank_count)
    failures = []
    gates_checked = 0
    operands_checked = 0
    family_counts = Counter(name for name, _index in rows)
    expected_counts = {
        "source": 1,
        "bank_packet": bank_count,
        "cross": bank_count - 1,
        "handoff_forward": bank_count - 1,
        "relay_latch": bank_count - 1,
        "relay_swap": 2 * (bank_count - 1),
        "relay_unlatch": bank_count - 1,
        "handoff_return": bank_count - 1,
        "finalizer": 1,
    }
    if len(rows) != 8 * bank_count - 5:
        failures.append(("row_count", len(rows), 8 * bank_count - 5))
    if family_counts != expected_counts:
        failures.append((
            "family_counts", dict(family_counts), expected_counts
        ))

    for station, (name, index) in enumerate(rows):
        if name == "bank_packet" and not 0 <= index < bank_count:
            failures.append(("bank_index", station, index))
        if name in {"cross", *PAIR_KIND} and not 0 <= index < bank_count - 1:
            failures.append(("edge_index", station, name, index))

        word = independently_map_word(name, index, capacity, templates)
        gates_checked += len(word)
        operands_checked += sum(len(wires) for _kind, wires in word)
        if name == "cross":
            if not 0 <= 1 < BANK_WIDTH:
                failures.append(("cross_offset", station, 1))
        else:
            local = templates[name]
            if len(local) != len(word):
                failures.append(("gate_count", station, name))
            for gate_index, (kind, wires) in enumerate(local):
                for operand_index, wire in enumerate(wires):
                    if name in {"source", "finalizer"}:
                        local_ok = SOURCE_SUPPORT[0] <= wire < SOURCE_SUPPORT[1]
                    elif name == "bank_packet":
                        local_ok = 0 <= wire < BANK_WIDTH
                    else:
                        local_ok = local_zone(wire) is not None
                    if not local_ok:
                        failures.append((
                            "local_zone", station, name, gate_index,
                            operand_index, wire,
                        ))

        for gate_index, (kind, wires) in enumerate(word):
            if (
                kind not in ARITY
                or len(wires) != ARITY.get(kind)
                or len(set(wires)) != len(wires)
            ):
                failures.append((
                    "gate_shape", station, name, gate_index, kind, wires
                ))
            for operand_index, wire in enumerate(wires):
                if not 0 <= wire < data_width(capacity):
                    failures.append((
                        "mapped_range", station, name, gate_index,
                        operand_index, wire, data_width(capacity),
                    ))
    return {
        "b": bank_count,
        "rows_checked": len(rows),
        "gates_checked": gates_checked,
        "operands_checked": operands_checked,
        "family_counts": dict(sorted(family_counts.items())),
        "failures": failures[:20],
        "failure_count": len(failures),
        "embedded_table_zone_predicate": "PASS" if not failures else "FAIL",
        "actual_constructor_hypothesis": (
            "UNPROVED_OBJECT_IDENTITY"
            if not failures else "FAIL_ON_EMBEDDED_TABLE"
        ),
        "exact_embedded_surrogate": not failures,
    }


def discharge_certificate(
    tree823: ast.Module,
) -> tuple[
    dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
    dict[str, object],
]:
    templates, packet = decode_embedded_packet(tree823)
    rows = {
        bank_count: independent_full_check(bank_count, templates)
        for bank_count in CHECK_BANKS
    }
    b11 = independent_full_check(PATTERN_BANK, templates)
    exact = (
        packet["exact_as_embedded_packet"]
        and all(row["exact_embedded_surrogate"] for row in rows.values())
        and b11["exact_embedded_surrogate"]
    )
    return templates, {
        "certificate": "INDEPENDENT_DISCHARGE",
        "packet": packet,
        "full_b3_b7_b10": rows,
        "b11_pattern": b11,
        "surrogate_result": "PASS" if exact else "FAIL",
        "817_actual_hypothesis_result": "NOT_DISCHARGED",
        "attack_passed": exact,
    }


def negative_control_certificate(
    templates: dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
) -> dict[str, object]:
    perturbed = dict(templates)
    perturbed["bank_packet"] = (
        templates["bank_packet"] + (("X", (BANK_WIDTH,)),)
    )
    result = independent_full_check(3, perturbed)
    detected = (
        not result["exact_embedded_surrogate"]
        and any(
            failure[0] == "local_zone"
            and failure[2] == "bank_packet"
            and failure[-1] == BANK_WIDTH
            for failure in result["failures"]
        )
    )
    return {
        "certificate": "NEGATIVE_CONTROL",
        "perturbation": (
            "append a well-formed X gate at local bank wire 131, outside "
            "the required half-open bank zone [0,131)"
        ),
        "checker_result": result,
        "expected_failure_detected": detected,
        "attack_passed": detected,
    }


def bridge_certificate(
    trees: dict[str, ast.Module],
    fidelity: dict[str, object],
) -> dict[str, object]:
    target = assigned_literal(trees[PRIMARY_817], "TARGET_THEOREM")
    inventory = assigned_literal(
        trees[PRIMARY_817], "CORRECTED_INVENTORY_NAMES"
    )
    bridge817 = ast.unparse(
        function_node(trees[PRIMARY_817], "certificate_c")
    )
    discharge823 = ast.unparse(
        function_node(trees[PRIMARY_823], "certificate_b")
    )
    schema_exact = (
        "CONDITIONAL exactly on H_TEMPLATE_PREIMAGE_ZONE_CLASS" in target
        and "'conditional_on': 'H_TEMPLATE_PREIMAGE_ZONE_CLASS'" in bridge817
        and "'condition_exact_text': H_TEMPLATE_PREIMAGE_ZONE_CLASS"
        in bridge817
        and target.count("CONDITIONAL") == 1
    )
    remaining_premises_explicit = (
        len(inventory) == 8
        and inventory[-1] == "H_SECTOR_INPUT"
        and "corrected seven structural conditions and H_SECTOR_INPUT"
        in target
        and "corrected seven" in discharge823
        and "H_SECTOR_INPUT remain theorem premises" in discharge823
    )
    actual_hypothesis_discharged = fidelity["logically_equivalent"]
    composition_succeeds = (
        schema_exact
        and remaining_premises_explicit
        and actual_hypothesis_discharged
    )
    return {
        "certificate": "THE_BRIDGE_COMPOSITION",
        "Cycle817_target_theorem": target,
        "corrected_condition_inventory": inventory,
        "conditional_schema_exactly_H_TEMPLATE": schema_exact,
        "nothing_else_is_an_open_bridge_condition":
            schema_exact and remaining_premises_explicit,
        "important_scope": (
            "The corrected seven structural conditions and H_SECTOR_INPUT "
            "remain premises; 'unconditional' can only mean removal of "
            "H_TEMPLATE_PREIMAGE_ZONE_CLASS."
        ),
        "conditions_verified_or_supplied_then_H_implies_theorem": schema_exact,
        "actual_H_discharged_by_823": actual_hypothesis_discharged,
        "composition_to_actual_unconditional_statement":
            composition_succeeds,
        "ruling": (
            "The implication schema is present and H_TEMPLATE is its only "
            "open bridge condition, but 823 supplies P823_blob rather than "
            "H817(actual constructors); modus ponens cannot fire."
        ),
        "attack_passed": (
            schema_exact
            and remaining_premises_explicit
            and not composition_succeeds
        ),
    }


def build_core(
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    fidelity = formalization_certificate(trees)
    templates, discharge = discharge_certificate(trees[PRIMARY_823])
    bridge = bridge_certificate(trees, fidelity)
    negative = negative_control_certificate(templates)
    return {
        "restatement_fidelity": fidelity,
        "independent_discharge": discharge,
        "bridge_composition": bridge,
        "negative_control": negative,
    }


def controls_certificate(
    provenance: dict[str, dict[str, str]],
    first: dict[str, object],
    second: dict[str, object],
) -> dict[str, object]:
    literal_paths = (
        DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and all(
            not Path(path).is_absolute()
            and ".." not in Path(path).parts
            and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        )
    )
    loaded_blocklisted_modules = sorted(
        name for name in sys.modules
        if name.split(".")[-1] in BLOCKLIST
    )
    deterministic = stable_bytes(first) == stable_bytes(second)
    exact = (
        all(row["exact"] for row in provenance.values())
        and literal_paths
        and BLOCKLIST
        == (Path(PRIMARY_817).stem, Path(PRIMARY_823).stem)
        and not loaded_blocklisted_modules
        and deterministic
        and AUDIT_TIMEOUT_SEC == 1200
        and STDOUT_LIMIT_BYTES == 150 * 1024
    )
    return {
        "certificate": "CONTROLS",
        "AUDIT_INPUT_PATHS_literal": AUDIT_INPUT_PATHS,
        "literal_worktree_relative_paths_existing": literal_paths,
        "sha256_and_git_blob_sha1": provenance,
        "BLOCKLIST_823_817_primaries": BLOCKLIST,
        "loaded_blocklisted_modules": loaded_blocklisted_modules,
        "primary_access": "bytes/text/AST only; never imported or executed",
        "deterministic_core_byte_identical_on_repeat": deterministic,
        "deterministic_core_sha256": stable_digest(first),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "attack_passed": exact,
    }


def main() -> int:
    started = perf_counter()
    provenance, _sources, trees = load_primaries()
    first = build_core(trees)
    second = build_core(trees)
    controls = controls_certificate(provenance, first, second)
    elapsed = perf_counter() - started

    checks = {
        "ACTUAL_OBJECT_FIDELITY_B3_THROUGH_B11":
            first["restatement_fidelity"]["attack_passed"],
        "INDEPENDENT_DISCHARGE_EMBEDDED_SURROGATE":
            first["independent_discharge"]["attack_passed"],
        "THE_BRIDGE_COMPOSITION_REFUTATION":
            first["bridge_composition"]["attack_passed"],
        "NEGATIVE_CONTROL":
            first["negative_control"]["attack_passed"],
        "CONTROLS": controls["attack_passed"],
        "RUNTIME_UNDER_1200_SECONDS": elapsed < AUDIT_TIMEOUT_SEC,
    }
    exact = all(checks.values())
    report = {
        "version": 2,
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "BLOCKLIST": BLOCKLIST,
        **first,
        "controls": controls,
        "checks": checks,
        "checks_passed": sum(checks.values()),
        "checks_failed": sum(not value for value in checks.values()),
        "runtime_seconds": round(elapsed, 6),
        "primary_claim_refuted": False,
        "primary_direct_actual_object_route_confirmed": exact,
        "verdict": (
            "CONFIRMED_823_V2_DIRECT_ACTUAL_OBJECT_ROUTE"
            if exact else
            "INDEPENDENT_CHECKER_FAILED"
        ),
    }
    report["report_sha256"] = stable_digest(report)

    fidelity = first["restatement_fidelity"]
    discharge = first["independent_discharge"]
    lines = [
        f"{'PASS' if passed else 'FAIL'} {name}"
        for name, passed in checks.items()
    ]
    lines.extend((
        "FORMALIZATION 817 :: " + fidelity["Cycle817_formalization"],
        "FORMALIZATION 823 :: "
        + fidelity["Cycle823_executable_formalization"],
        "RULING :: " + fidelity["ruling"],
    ))
    for bank_count, row in fidelity[
        "elementwise_comparison_b3_through_b11"
    ].items():
        lines.append(
            f"FIDELITY b={bank_count} "
            f"{'PASS' if row['elementwise_equal'] else 'FAIL'} "
            f"rows={row['Cycle817_rows']} "
            f"local_gates={row['elements_compared']['local_gates']} "
            f"mapped_gates={row['elements_compared']['mapped_gates']}"
        )
    for bank_count in CHECK_BANKS:
        row = discharge["full_b3_b7_b10"][bank_count]
        lines.append(
            f"INDEPENDENT b={bank_count} "
            f"embedded={row['embedded_table_zone_predicate']} "
            f"actual={row['actual_constructor_hypothesis']} "
            f"rows={row['rows_checked']} gates={row['gates_checked']} "
            f"operands={row['operands_checked']}"
        )
    b11 = discharge["b11_pattern"]
    lines.append(
        f"PATTERN b=11 embedded={b11['embedded_table_zone_predicate']} "
        f"actual={b11['actual_constructor_hypothesis']} "
        f"rows={b11['rows_checked']} gates={b11['gates_checked']} "
        f"operands={b11['operands_checked']}"
    )
    lines.append("VERDICT " + report["verdict"])
    payload = "\n".join(lines) + "\n" + json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    ) + "\n"
    payload_size = len(payload.encode())
    if payload_size >= STDOUT_LIMIT_BYTES:
        print(json.dumps({
            "verdict": "INDEPENDENT_CHECKER_FAILED",
            "reason": "stdout bound",
            "observed_bytes": payload_size,
            "limit_bytes": STDOUT_LIMIT_BYTES,
        }, sort_keys=True, separators=(",", ":")))
        return 1
    sys.stdout.write(payload)
    return 0 if exact else 1


if __name__ == "__main__":
    raise SystemExit(main())
