#!/usr/bin/env python3
"""Cycle 740 independent checker: bounded, adversarial, and read-disciplined."""
from __future__ import annotations

import ast
from hashlib import sha256
import json
from pathlib import Path
import re
from time import perf_counter

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/TABLE_PARAMETERIZED_MAPPER_CYCLE740_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

STDOUT_LIMIT_BYTES = 150 * 1024
FROZEN_EQUIVALENCE_SHA256_PREFIXES = (
    "880adbf0405aa011",
    "aa80db72e7c64820",
    "d1fd5ca5fa138e2c",
    "82c9df54b847e599",
    "ec9762c1df2a584b",
    "ff0e208c10321993",
    "600282673b410df0",
    "13bb3776e6f5f129",
    "b434e0dc7ac43b6b",
    "88c7fc89db3cc96e",
    "b77d2268e531dee4",
    "b869b0fb9612218b",
)
THEOREM_TRANSFER_LANGUAGE = (
    "For every integer C>=1 and every integer b with 1<=b<=C, IF the "
    "derived affine placement law BANK_BASE(i)=41+131*i and "
    "LINK_BASE(i,C)=41+131*C+382*i is the intended placement geometry, "
    "THEN Cycle 738's general-n sector theorem, with Cycle 739's amended "
    "six-term ownership predicate, holds for n=8*b-5.  No per-b re-proof "
    "and no other new supply are required."
)


def stable_json_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    ).encode()


def gate_signature(gate: object) -> tuple[str, tuple[int, ...]]:
    return gate.kind, tuple(int(wire) for wire in gate.wires)


def word_signature(
    word: tuple[object, ...],
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    return tuple(gate_signature(gate) for gate in word)


def serialized_program(program: tuple[tuple[object, ...], ...]) -> bytes:
    return stable_json_bytes(tuple(
        (kind, int(index), word_signature(tuple(local)))
        for kind, index, local in program
    ))


def serialized_mapped_rows(
    program: tuple[tuple[object, ...], ...],
    mapper: object,
) -> bytes:
    return stable_json_bytes(tuple(
        word_signature(tuple(mapper(row))) for row in program
    ))


def read_audit_input(path: str) -> str:
    if path not in AUDIT_INPUT_PATHS:
        raise AssertionError(("undeclared read", path))
    return Path(path).read_text(encoding="utf-8")


def top_level_literal(tree: ast.Module, name: str) -> object:
    candidates = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            ):
                candidates.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            candidates.append(node.value)
    if len(candidates) != 1:
        raise AssertionError(("top-level literal multiplicity", name, len(candidates)))
    return ast.literal_eval(candidates[0])


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    candidates = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(candidates) != 1:
        raise AssertionError(("function multiplicity", name, len(candidates)))
    return candidates[0]


def local_literal(function: ast.FunctionDef, name: str) -> object:
    candidates = [
        node.value for node in ast.walk(function)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(candidates) != 1:
        raise AssertionError(("local literal multiplicity", name, len(candidates)))
    return ast.literal_eval(candidates[0])


def local_dict_keys(function: ast.FunctionDef, name: str) -> tuple[str, ...]:
    candidates = [
        node.value for node in ast.walk(function)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
        and isinstance(node.value, ast.Dict)
    ]
    if len(candidates) != 1:
        raise AssertionError(("local dict multiplicity", name, len(candidates)))
    return tuple(ast.literal_eval(key) for key in candidates[0].keys)


def subscript_name_and_key(node: ast.AST) -> tuple[str, object] | None:
    if not (
        isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
    ):
        return None
    try:
        key = ast.literal_eval(node.slice)
    except Exception:
        return None
    return node.value.id, key


def extracted_extension_totals(main_function: ast.FunctionDef) -> dict[int, int]:
    candidates = []
    for node in ast.walk(main_function):
        if not isinstance(node, ast.Compare) or len(node.comparators) != 1:
            continue
        if subscript_name_and_key(node.left) != (
            "extension", "per_b_row_totals"
        ):
            continue
        try:
            candidate = ast.literal_eval(node.comparators[0])
        except Exception:
            continue
        candidates.append(candidate)
    if len(candidates) != 1:
        raise AssertionError(("extension census multiplicity", len(candidates)))
    return candidates[0]


def sha_recipe_shape(tree: ast.Module) -> dict[str, object]:
    function = function_node(tree, "equivalence_certificate")
    combined_values = [
        node.value for node in ast.walk(function)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "combined"
            for target in node.targets
        )
    ]
    digest_values = [
        value for node in ast.walk(function)
        if isinstance(node, ast.Dict)
        for key, value in zip(node.keys, node.values)
        if key is not None
        and isinstance(key, ast.Constant)
        and key.value == "equivalence_sha256"
    ]
    loops = [
        node for node in ast.walk(function)
        if isinstance(node, ast.For)
        and isinstance(node.target, ast.Name)
        and node.target.id == "bank_count"
        and isinstance(node.iter, ast.Call)
        and isinstance(node.iter.func, ast.Name)
        and node.iter.func.id == "range"
    ]
    combined_dump = (
        ast.dump(combined_values[0], include_attributes=False)
        if len(combined_values) == 1 else ""
    )
    digest_dump = (
        ast.dump(digest_values[0], include_attributes=False)
        if len(digest_values) == 1 else ""
    )
    loop_dump = (
        ast.dump(loops[0].iter, include_attributes=False)
        if len(loops) == 1 else ""
    )
    exact = all((
        len(combined_values) == 1,
        "observed_program_bytes" in combined_dump,
        "observed_mapped_bytes" in combined_dump,
        "Constant(value=b'\\x00')" in combined_dump,
        len(digest_values) == 1,
        "sha256" in digest_dump,
        "combined" in digest_dump,
        "hexdigest" in digest_dump,
        len(loops) == 1,
        "Constant(value=1)" in loop_dump,
        "FROZEN_CAPACITY" in loop_dump,
    ))
    return {
        "combined_expression": combined_dump,
        "digest_expression": digest_dump,
        "bank_sweep_expression": loop_dump,
        "slots": 12,
        "exact": exact,
    }


def extraction(
    primary_source: str,
    self_source: str,
) -> dict[str, object]:
    primary_tree = ast.parse(primary_source)
    self_tree = ast.parse(self_source)
    conditional = top_level_literal(primary_tree, "TABLE_UNIFORM_CONDITIONAL")
    law_match = re.search(
        r"BANK_BASE\(i\)=(-?\d+)\+(-?\d+)\*i "
        r"and LINK_BASE\(i,C\)=(-?\d+)\+(-?\d+)\*C\+(-?\d+)\*i is the "
        r"intended placement geometry",
        conditional,
    )
    if law_match is None:
        raise AssertionError("conditional law literal did not parse exactly")
    bank_offset, bank_stride, link_offset, link_capacity_stride, link_stride = (
        int(value) for value in law_match.groups()
    )
    primary_main = function_node(primary_tree, "main")
    extension_totals = extracted_extension_totals(primary_main)
    recovered = local_literal(
        function_node(primary_tree, "frozen_eight_certificate"),
        "expected_rows",
    )
    samples = local_literal(
        function_node(primary_tree, "b13_orbit_spot_certificate"),
        "position_sample",
    )
    boundary_keys = local_dict_keys(primary_main, "boundary")
    checker_inputs = top_level_literal(self_tree, "AUDIT_INPUT_PATHS")
    primary_inputs = top_level_literal(primary_tree, "AUDIT_INPUT_PATHS")
    sha_prefixes = top_level_literal(
        self_tree, "FROZEN_EQUIVALENCE_SHA256_PREFIXES"
    )
    sha_recipe = sha_recipe_shape(primary_tree)
    orbit_stations = extension_totals[13]
    result = {
        "law": {
            "bank_offset": bank_offset,
            "bank_stride": bank_stride,
            "link_offset": link_offset,
            "link_capacity_stride": link_capacity_stride,
            "link_stride": link_stride,
        },
        "conditional": conditional,
        "equivalence_sha256_prefixes": sha_prefixes,
        "sha_anchor_origin": (
            "checker literal frozen against the primary AST-verified digest recipe"
        ),
        "primary_sha_recipe": sha_recipe,
        "extension_row_totals": extension_totals,
        "extension_total_rows": sum(extension_totals.values()),
        "recovered_rows": recovered,
        "orbit_samples": samples,
        "orbit_sample_count": len(samples),
        "orbit_boundaries": len(samples) * orbit_stations,
        "boundary_keys": boundary_keys,
        "checker_audit_inputs": checker_inputs,
        "primary_audit_inputs_literal": primary_inputs,
    }
    result["exact"] = all((
        result["law"] == {
            "bank_offset": 41,
            "bank_stride": 131,
            "link_offset": 41,
            "link_capacity_stride": 131,
            "link_stride": 382,
        },
        conditional == THEOREM_TRANSFER_LANGUAGE,
        len(sha_prefixes) == 12,
        all(
            isinstance(prefix, str)
            and len(prefix) == 16
            and all(character in "0123456789abcdef" for character in prefix)
            for prefix in sha_prefixes
        ),
        sha_recipe["exact"],
        extension_totals == {13: 99, 14: 107, 15: 115, 16: 123},
        result["extension_total_rows"] == 444,
        tuple(row[0] for row in recovered) == tuple(range(57, 65)),
        samples == ((), (0,), (37,), (0, 2), (7, 42)),
        result["orbit_sample_count"] == 5,
        result["orbit_boundaries"] == 495,
        boundary_keys == (
            "capacity_now_parameterized",
            "table_law_supplied_anchored_to_K",
            "sector_theorem_table_uniform",
            "exact_conditional",
            "supplies",
            "landed_files_modified",
            "capacity_domain",
            "remaining_capacity_residual",
        ),
        checker_inputs == AUDIT_INPUT_PATHS,
        isinstance(primary_inputs, tuple),
        all(isinstance(path, str) for path in primary_inputs),
    ))
    return result


def fit_integer_affine(values: tuple[int, ...]) -> tuple[int, int]:
    if len(values) < 2:
        raise AssertionError("affine fit needs at least two entries")
    count = len(values)
    sum_x = sum(range(count))
    sum_y = sum(values)
    sum_xx = sum(index * index for index in range(count))
    sum_xy = sum(index * value for index, value in enumerate(values))
    denominator = count * sum_xx - sum_x * sum_x
    numerator = count * sum_xy - sum_x * sum_y
    if denominator == 0 or numerator % denominator:
        raise AssertionError(("nonintegral affine stride", numerator, denominator))
    stride = numerator // denominator
    offset_numerator = sum_y - stride * sum_x
    if offset_numerator % count:
        raise AssertionError(("nonintegral affine offset", offset_numerator, count))
    offset = offset_numerator // count
    if tuple(offset + stride * index for index in range(count)) != values:
        raise AssertionError("full-table affine residual")
    return offset, stride


def solve_law() -> dict[str, object]:
    banks = tuple(int(value) for value in K.M.R12.BANK_BASES)
    links = tuple(int(value) for value in K.M.R12.LINK_BASES)
    bank_offset, bank_stride = fit_integer_affine(banks)
    link_offset_at_frozen_capacity, link_stride = fit_integer_affine(links)
    frozen_capacity = len(banks)
    relative_link_offset = link_offset_at_frozen_capacity - bank_offset
    if relative_link_offset % frozen_capacity:
        raise AssertionError("link offset is not an integral capacity multiple")
    link_capacity_stride = relative_link_offset // frozen_capacity
    return {
        "banks": banks,
        "links": links,
        "frozen_capacity": frozen_capacity,
        "bank_offset": bank_offset,
        "bank_stride": bank_stride,
        "link_offset": bank_offset,
        "link_offset_at_frozen_capacity": link_offset_at_frozen_capacity,
        "link_capacity_stride": link_capacity_stride,
        "link_stride": link_stride,
    }


def own_bases(
    capacity: int,
    law: dict[str, object],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity < 1:
        raise ValueError("capacity must be a positive integer")
    bank_offset = int(law["bank_offset"])
    bank_stride = int(law["bank_stride"])
    link_offset = int(law["link_offset"])
    link_capacity_stride = int(law["link_capacity_stride"])
    link_stride = int(law["link_stride"])
    banks = tuple(
        bank_offset + bank_stride * index for index in range(capacity)
    )
    links = tuple(
        link_offset + link_capacity_stride * capacity + link_stride * index
        for index in range(capacity - 1)
    )
    return banks, links


def own_data_width(capacity: int, law: dict[str, object]) -> int:
    banks, links = own_bases(capacity, law)
    if links:
        return links[-1] + int(law["link_stride"])
    return banks[-1] + int(law["bank_stride"])


def law_recount(
    extracted: dict[str, object],
) -> dict[str, object]:
    law = solve_law()
    generated_banks, generated_links = own_bases(
        int(law["frozen_capacity"]), law
    )
    observed_bytes = stable_json_bytes((law["banks"], law["links"]))
    generated_bytes = stable_json_bytes((generated_banks, generated_links))
    fitted = {
        key: law[key] for key in (
            "bank_offset",
            "bank_stride",
            "link_offset",
            "link_capacity_stride",
            "link_stride",
        )
    }
    exact = all((
        fitted == extracted["law"],
        law["frozen_capacity"] == 12,
        law["link_offset_at_frozen_capacity"] == 1613,
        law["link_capacity_stride"] == law["bank_stride"],
        generated_banks == law["banks"],
        generated_links == law["links"],
        generated_bytes == observed_bytes,
    ))
    return {
        "fit": fitted,
        "link_offset_at_C12": law["link_offset_at_frozen_capacity"],
        "bank_entries": len(generated_banks),
        "link_entries": len(generated_links),
        "observed_table_sha256": sha256(observed_bytes).hexdigest(),
        "generated_table_sha256": sha256(generated_bytes).hexdigest(),
        "byte_exact": generated_bytes == observed_bytes,
        "exact": exact,
        "_law": law,
    }


def own_offset_gate(gate: object, base: int) -> object:
    return K.A.Gate(
        gate.kind,
        tuple(int(base) + int(wire) for wire in gate.wires),
    )


def own_pair_gate(
    gate: object,
    edge: int,
    kind: str,
    capacity: int,
    law: dict[str, object],
) -> object:
    banks, links = own_bases(capacity, law)
    if not 0 <= edge < len(links):
        raise IndexError(("edge", edge, len(links)))
    bank_width = int(K.A.N)
    link_half_width = int(K.M.P.LINK_AUX_WIDTH)
    split = 0 if kind == "handoff" else link_half_width
    mapped_wires = []
    for raw_wire in gate.wires:
        wire = int(raw_wire)
        if wire < bank_width:
            mapped_wires.append(banks[edge] + wire)
        elif wire < 2 * bank_width:
            mapped_wires.append(banks[edge + 1] + wire - bank_width)
        else:
            mapped_wires.append(
                links[edge] + split + wire - 2 * bank_width
            )
    return K.A.Gate(gate.kind, tuple(mapped_wires))


def own_mapped_action(
    kind: str,
    index: int,
    local: tuple[object, ...],
    capacity: int,
    law: dict[str, object],
) -> tuple[object, ...]:
    banks, links = own_bases(capacity, law)
    if kind == "bank":
        if not 0 <= index < len(banks):
            raise IndexError(("bank", index, len(banks)))
        return tuple(own_offset_gate(gate, banks[index]) for gate in local)
    if kind in ("handoff", "relay"):
        return tuple(
            own_pair_gate(gate, index, kind, capacity, law) for gate in local
        )
    if kind == "cross":
        if not 0 <= index < len(links):
            raise IndexError(("cross", index, len(links)))
        predecessor_offset = int(K.A.CELLS[0]["pred"][1])
        return (
            K.A.Gate(
                "CNOT",
                (
                    links[index],
                    banks[index + 1] + predecessor_offset,
                ),
            ),
        )
    raise ValueError(("unknown mapped action", kind))


def own_mapped_macro(
    row: tuple[object, ...],
    capacity: int,
    law: dict[str, object],
) -> tuple[object, ...]:
    kind, index, local = row
    if kind in ("source", "finalizer"):
        return tuple(local)
    if kind == "identity":
        return ()
    return own_mapped_action(kind, int(index), tuple(local), capacity, law)


def own_program(
    bank_count: int,
    capacity: int,
) -> tuple[tuple[object, ...], ...]:
    if (
        isinstance(bank_count, bool)
        or not isinstance(bank_count, int)
        or bank_count < 1
        or bank_count > capacity
    ):
        raise ValueError("bank_count must be an integer in 1..capacity")
    prefix = [("source", 0, K.R3.source_compute_word())]
    for bank in range(bank_count):
        prefix.append(("bank", bank, K.H.PACKET))
        if bank:
            prefix.append(("cross", bank - 1, ()))
        if bank < bank_count - 1:
            prefix.extend((
                ("handoff", bank, K.H.HANDOFF_FORWARD),
                ("relay", bank, K.H.RELAY_LATCH),
                ("relay", bank, K.H.RELAY_SWAP),
            ))
    reverse = []
    for edge in reversed(range(bank_count - 1)):
        reverse.extend((
            ("relay", edge, K.H.RELAY_SWAP),
            ("relay", edge, K.H.RELAY_UNLATCH),
            ("handoff", edge, K.H.HANDOFF_RETURN),
        ))
    return tuple(
        prefix + reverse
        + [("finalizer", 0, K.M.source_finalizer_word(bank_count))]
    )


def equivalence_recount(
    extracted: dict[str, object],
    law_report: dict[str, object],
) -> dict[str, object]:
    law = law_report["_law"]
    per_b = {}
    failures = []
    observed_prefixes = []
    for bank_count in range(1, 13):
        observed_program = K.interleaved_program(bank_count)
        generated_program = own_program(bank_count, 12)
        observed_program_bytes = serialized_program(observed_program)
        generated_program_bytes = serialized_program(generated_program)
        observed_mapped_bytes = serialized_mapped_rows(
            observed_program, K.mapped_macro
        )
        generated_mapped_bytes = serialized_mapped_rows(
            generated_program,
            lambda row: own_mapped_macro(row, 12, law),
        )
        observed_combined = (
            observed_program_bytes + b"\0" + observed_mapped_bytes
        )
        generated_combined = (
            generated_program_bytes + b"\0" + generated_mapped_bytes
        )
        observed_digest = sha256(observed_combined).hexdigest()
        generated_digest = sha256(generated_combined).hexdigest()
        observed_prefixes.append(observed_digest[:16])
        passed = all((
            observed_program == generated_program,
            observed_program_bytes == generated_program_bytes,
            observed_mapped_bytes == generated_mapped_bytes,
            observed_digest == generated_digest,
            observed_digest.startswith(
                extracted["equivalence_sha256_prefixes"][bank_count - 1]
            ),
        ))
        if not passed:
            failures.append(bank_count)
        per_b[bank_count] = {
            "rows": len(observed_program),
            "program_bytes": len(observed_program_bytes),
            "mapped_bytes": len(observed_mapped_bytes),
            "sha256": observed_digest,
            "pass": passed,
        }
    exact = all((
        not failures,
        tuple(observed_prefixes)
        == tuple(extracted["equivalence_sha256_prefixes"]),
        len(per_b) == 12,
    ))
    return {
        "bank_domain": (1, 12),
        "per_b": per_b,
        "sha256_prefixes": tuple(observed_prefixes),
        "failed_b": failures,
        "programs_and_mapped_words_byte_exact": not failures,
        "exact": exact,
    }


GATE_ARITY = {"X": 1, "CNOT": 2, "TOF": 3}


def own_apply_gate(value: int, gate: object) -> int:
    kind = gate.kind
    wires = tuple(int(wire) for wire in gate.wires)
    if kind not in GATE_ARITY or len(wires) != GATE_ARITY[kind]:
        raise ValueError(("unsupported gate", kind, wires))
    if kind == "X":
        enabled = True
    else:
        enabled = all((value >> wire) & 1 for wire in wires[:-1])
    return value ^ (1 << wires[-1]) if enabled else value


def own_lift_gate(gate: object, control: int, work: int) -> tuple[object, ...]:
    kind = gate.kind
    wires = tuple(int(wire) for wire in gate.wires)
    if kind == "X":
        return (K.A.Gate("CNOT", (control, wires[0])),)
    if kind == "CNOT":
        return (K.A.Gate("TOF", (control, wires[0], wires[1])),)
    if kind == "TOF":
        return (
            K.A.Gate("TOF", (control, wires[0], work)),
            K.A.Gate("TOF", (work, wires[1], wires[2])),
            K.A.Gate("TOF", (control, wires[0], work)),
        )
    raise ValueError(("unsupported lift", kind))


def primitive_clean_truth(kind: str) -> bool:
    arity = GATE_ARITY[kind]
    data_wires = tuple(range(arity))
    semantic = K.A.Gate(kind, data_wires)
    control = arity
    work = arity + 1
    lifted = own_lift_gate(semantic, control, work)
    for payload in range(1 << (arity + 1)):
        initial = payload
        observed = initial
        for gate in lifted:
            observed = own_apply_gate(observed, gate)
        expected = initial
        if (initial >> control) & 1:
            expected = own_apply_gate(expected, semantic)
        if observed != expected or ((observed >> work) & 1):
            return False
    return True


def clean_word_evaluation(
    word: tuple[object, ...],
    data_width: int,
    control: int,
    work: int,
    primitive_truth: dict[str, bool],
) -> dict[str, object]:
    kinds = tuple(gate.kind for gate in word)
    kinds_valid = all(kind in GATE_ARITY for kind in kinds)
    arities_valid = all(
        gate.kind in GATE_ARITY
        and len(gate.wires) == GATE_ARITY[gate.kind]
        for gate in word
    )
    operands_distinct = all(
        len(set(gate.wires)) == len(gate.wires) for gate in word
    )
    data_only = all(
        isinstance(wire, int) and 0 <= wire < data_width
        for gate in word for wire in gate.wires
    )
    auxiliaries_separate = (
        control != work and control >= data_width and work >= data_width
    )
    lifted = ()
    if kinds_valid and arities_valid:
        lifted = tuple(
            lifted_gate
            for gate in word
            for lifted_gate in own_lift_gate(gate, control, work)
        )
    addressed_domain_exact = all(
        wire in {control, work} or 0 <= wire < data_width
        for gate in lifted for wire in gate.wires
    )
    control_untargeted = all(
        gate.wires[-1] != control for gate in lifted
    )
    work_targets = sum(
        gate.wires[-1] == work for gate in lifted
    )
    expected_work_targets = 2 * sum(kind == "TOF" for kind in kinds)
    primitive_proof = kinds_valid and all(
        primitive_truth[kind] for kind in kinds
    )
    passed = all((
        kinds_valid,
        arities_valid,
        operands_distinct,
        data_only,
        auxiliaries_separate,
        addressed_domain_exact,
        control_untargeted,
        work_targets == expected_work_targets,
        primitive_proof,
    ))
    return {
        "semantic_gates": len(word),
        "controlled_gates": len(lifted),
        "work_targets": work_targets,
        "expected_work_targets": expected_work_targets,
        "pass": passed,
    }


def template_name(row: tuple[object, ...]) -> str:
    kind, _index, local = row
    if kind == "source":
        return "source"
    if kind == "bank" and local == K.H.PACKET:
        return "bank_packet"
    if kind == "cross" and local == ():
        return "cross"
    if kind == "finalizer":
        return "finalizer"
    if kind == "handoff" and local == K.H.HANDOFF_FORWARD:
        return "handoff_forward"
    if kind == "handoff" and local == K.H.HANDOFF_RETURN:
        return "handoff_return"
    if kind == "relay" and local == K.H.RELAY_LATCH:
        return "relay_latch"
    if kind == "relay" and local == K.H.RELAY_SWAP:
        return "relay_swap"
    if kind == "relay" and local == K.H.RELAY_UNLATCH:
        return "relay_unlatch"
    raise AssertionError(("unknown row template", kind, local))


def extension_recount(
    extracted: dict[str, object],
    law_report: dict[str, object],
) -> dict[str, object]:
    law = law_report["_law"]
    capacity = 16
    data_width = own_data_width(capacity, law)
    primitive_truth = {
        kind: primitive_clean_truth(kind) for kind in GATE_ARITY
    }
    per_b = {}
    total_rows = 0
    all_template_names = set()
    for bank_count in (13, 14, 15, 16):
        program = own_program(bank_count, capacity)
        stations = len(program)
        failures = []
        for station, row in enumerate(program):
            try:
                name = template_name(row)
                all_template_names.add(name)
                mapped = own_mapped_macro(row, capacity, law)
                clean = clean_word_evaluation(
                    mapped,
                    data_width,
                    data_width + station,
                    data_width + 2 * stations + station,
                    primitive_truth,
                )
                if not clean["pass"]:
                    failures.append((station, row[0], row[1], "clean-work"))
            except Exception as error:
                failures.append((
                    station, row[0], row[1],
                    f"{type(error).__name__}:{error}",
                ))
        total_rows += stations
        per_b[bank_count] = {
            "rows": stations,
            "expected_rows": extracted["extension_row_totals"][bank_count],
            "row_failures": failures,
            "pass": (
                stations == extracted["extension_row_totals"][bank_count]
                and stations == 8 * bank_count - 5
                and not failures
            ),
        }

    frozen_program = K.interleaved_program(13)
    generated_program = own_program(13, capacity)
    recovered = []
    frozen_failure_stations = []
    for station, row in enumerate(frozen_program):
        try:
            K.mapped_macro(row)
        except Exception as error:
            frozen_failure_stations.append((
                station, type(error).__name__
            ))
            generated_row = generated_program[station]
            mapped = own_mapped_macro(generated_row, capacity, law)
            name = template_name(generated_row)
            clean = clean_word_evaluation(
                mapped,
                data_width,
                data_width + station,
                data_width + 2 * len(generated_program) + station,
                primitive_truth,
            )
            recovered.append((
                station,
                generated_row[0],
                generated_row[1],
                name,
                clean["pass"],
                len(mapped),
            ))
    recovered_projection = tuple(row[:4] for row in recovered)
    exact = all((
        all(primitive_truth.values()),
        total_rows == extracted["extension_total_rows"] == 444,
        all(report["pass"] for report in per_b.values()),
        all_template_names == {
            "source",
            "bank_packet",
            "cross",
            "handoff_forward",
            "relay_latch",
            "relay_swap",
            "relay_unlatch",
            "handoff_return",
            "finalizer",
        },
        tuple(station for station, _error in frozen_failure_stations)
        == tuple(range(57, 65)),
        all(error == "IndexError" for _station, error in frozen_failure_stations),
        recovered_projection == extracted["recovered_rows"],
        all(row[4] and row[5] > 0 for row in recovered),
    ))
    return {
        "capacity": capacity,
        "data_width": data_width,
        "primitive_clean_truth": primitive_truth,
        "per_b": per_b,
        "total_rows_checked": total_rows,
        "templates_seen": tuple(sorted(all_template_names)),
        "frozen_failure_stations": frozen_failure_stations,
        "recovered_rows": recovered,
        "exact": exact,
    }


def own_swap_word(left: int, right: int) -> tuple[object, ...]:
    return (
        K.A.Gate("CNOT", (left, right)),
        K.A.Gate("CNOT", (right, left)),
        K.A.Gate("CNOT", (left, right)),
    )


def own_controller_word(
    program: tuple[tuple[object, ...], ...],
    data_width: int,
    capacity: int,
    law: dict[str, object],
) -> tuple[object, ...]:
    stations = len(program)
    a_base = data_width
    b_base = data_width + stations
    work_base = data_width + 2 * stations
    q_word = tuple(
        lifted
        for station, row in enumerate(program)
        for gate in own_mapped_macro(row, capacity, law)
        for lifted in own_lift_gate(
            gate, a_base + station, work_base + station
        )
    )
    r1_word = tuple(
        gate for station in range(stations)
        for gate in own_swap_word(
            a_base + station, b_base + station
        )
    )
    r2_word = tuple(
        gate for station in range(stations)
        for gate in own_swap_word(
            b_base + station,
            a_base + (station + 1) % stations,
        )
    )
    return q_word + r1_word + r2_word


def compile_operations(
    word: tuple[object, ...],
) -> tuple[tuple[int, int], ...]:
    operations = []
    for gate in word:
        wires = tuple(int(wire) for wire in gate.wires)
        if gate.kind == "X":
            controls = 0
        elif gate.kind in ("CNOT", "TOF"):
            controls = sum(1 << wire for wire in wires[:-1])
        else:
            raise ValueError(("compile gate kind", gate.kind))
        operations.append((controls, 1 << wires[-1]))
    return tuple(operations)


def apply_operations(
    value: int,
    operations: tuple[tuple[int, int], ...],
) -> int:
    for controls, target in operations:
        if value & controls == controls:
            value ^= target
    return value


def rotate_mask(mask: int, shift: int, stations: int) -> int:
    ring_mask = (1 << stations) - 1
    shift %= stations
    if shift == 0:
        return mask & ring_mask
    return (
        ((mask << shift) & ring_mask)
        | (mask >> (stations - shift))
    )


def adjacent(mask: int, stations: int) -> bool:
    return bool(mask & rotate_mask(mask, 1, stations))


def ownership_holds(
    a_mask: int,
    b_mask: int,
    work_mask: int,
    station: int,
    stations: int,
) -> bool:
    left = (station - 1) % stations
    right = (station + 1) % stations
    return not (
        ((a_mask >> left) & 1)
        or ((a_mask >> right) & 1)
        or ((b_mask >> left) & 1)
        or ((b_mask >> station) & 1)
        or ((b_mask >> right) & 1)
        or ((work_mask >> station) & 1)
    )


def orbit_spot_recount(
    extracted: dict[str, object],
    law_report: dict[str, object],
) -> dict[str, object]:
    law = law_report["_law"]
    bank_count = 13
    capacity = 16
    program = own_program(bank_count, capacity)
    stations = len(program)
    data_width = own_data_width(capacity, law)
    controller = own_controller_word(
        program, data_width, capacity, law
    )
    operations = compile_operations(controller)
    inverse_operations = tuple(reversed(operations))
    ring_mask = (1 << stations) - 1
    a_base = data_width
    b_base = data_width + stations
    work_base = data_width + 2 * stations
    sample_reports = []
    total_boundaries = 0
    total_violations = 0
    closure_failures = 0
    inverse_failures = 0
    for positions in extracted["orbit_samples"]:
        initial_mask = sum(1 << position for position in positions)
        value = initial_mask << a_base
        initial_value = value
        sample_violations = 0
        for step in range(stations):
            a_mask = (value >> a_base) & ring_mask
            b_mask = (value >> b_base) & ring_mask
            work_mask = (value >> work_base) & ring_mask
            expected_a = rotate_mask(initial_mask, step, stations)
            ownership_exact = all(
                ownership_holds(
                    a_mask, b_mask, work_mask, station, stations
                )
                for station in range(stations)
                if (a_mask >> station) & 1
            )
            violation = any((
                a_mask != expected_a,
                b_mask != 0,
                work_mask != 0,
                adjacent(a_mask, stations),
                not ownership_exact,
            ))
            sample_violations += int(violation)
            total_boundaries += 1
            value = apply_operations(value, operations)
        final_a = (value >> a_base) & ring_mask
        final_b = (value >> b_base) & ring_mask
        final_work = (value >> work_base) & ring_mask
        closed = (
            final_a == initial_mask
            and final_b == 0
            and final_work == 0
        )
        closure_failures += int(not closed)
        recovered = value
        for _step in range(stations):
            recovered = apply_operations(
                recovered, inverse_operations
            )
        inverse_exact = recovered == initial_value
        inverse_failures += int(not inverse_exact)
        total_violations += sample_violations
        sample_reports.append({
            "positions": positions,
            "boundaries": stations,
            "violations": sample_violations,
            "register_closed": closed,
            "full_inverse_exact": inverse_exact,
        })
    exact = all((
        stations == 99,
        len(sample_reports) == extracted["orbit_sample_count"] == 5,
        total_boundaries == extracted["orbit_boundaries"] == 495,
        total_violations == 0,
        closure_failures == 0,
        inverse_failures == 0,
    ))
    return {
        "banks": bank_count,
        "capacity": capacity,
        "stations": stations,
        "controller_gates": len(controller),
        "controller_sha256": K.gate_digest(controller),
        "samples": sample_reports,
        "boundaries_checked": total_boundaries,
        "invariant_violations": total_violations,
        "register_closure_failures": closure_failures,
        "full_inverse_failures": inverse_failures,
        "exact": exact,
    }


def import_names(tree: ast.Module) -> tuple[str, ...]:
    names = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            names.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            names.append(node.module or "")
    return tuple(names)


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = call_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def discipline(
    extracted: dict[str, object],
    self_source: str,
    core_source_before: str,
    extension: dict[str, object],
    orbit: dict[str, object],
) -> dict[str, object]:
    self_tree = ast.parse(self_source)
    imports = import_names(self_tree)
    core_module = (
        "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
    )
    blocklisted_imports = tuple(
        name for name in imports
        if name.startswith("frontier_cycle7") and name != core_module
    )
    mutation_calls = tuple(sorted({
        call_name(node.func) for node in ast.walk(self_tree)
        if isinstance(node, ast.Call)
        and call_name(node.func).split(".")[-1] in {
            "write_text",
            "write_bytes",
            "unlink",
            "rename",
            "replace",
            "touch",
            "mkdir",
            "rmdir",
        }
    }))
    general_capacity_phrase = "".join(("For every integer ", "C>=1"))
    general_theorem_phrase = "".join(("general-n sector ", "theorem"))
    suspicious_theorem_strings = tuple(
        node.value for node in ast.walk(self_tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
        and (
            general_capacity_phrase in node.value
            or general_theorem_phrase in node.value
        )
    )
    core_source_after = read_audit_input(AUDIT_INPUT_PATHS[1])
    boundary = {
        "capacity_now_parameterized": extension["exact"],
        "table_law_supplied_anchored_to_K": True,
        "sector_theorem_table_uniform": {
            "conditional_on_supplied_table_law": True,
        },
        "exact_conditional": extracted["conditional"],
        "supplies": {
            "new": (
                "the table law as the intended placement convention anchored to K",
            ),
            "retained": (
                "the primary's previously stated sector hypotheses",
            ),
        },
        "landed_files_modified": False,
        "capacity_domain": {
            "checked_extension": (13, 16),
            "declared_only_under_exact_conditional": True,
        },
        "remaining_capacity_residual": None,
    }
    boundary_keys = tuple(boundary)
    exact = all((
        top_level_literal(self_tree, "AUDIT_INPUT_PATHS")
        == AUDIT_INPUT_PATHS,
        not blocklisted_imports,
        not mutation_calls,
        sha256(core_source_before.encode()).digest()
        == sha256(core_source_after.encode()).digest(),
        suspicious_theorem_strings == (THEOREM_TRANSFER_LANGUAGE,),
        extracted["conditional"] == THEOREM_TRANSFER_LANGUAGE,
        boundary_keys == extracted["boundary_keys"],
        boundary["sector_theorem_table_uniform"]
        == {"conditional_on_supplied_table_law": True},
        extension["exact"],
        orbit["exact"],
    ))
    return {
        "imports": imports,
        "blocklisted_imports": blocklisted_imports,
        "mutation_calls": mutation_calls,
        "K_source_unchanged": core_source_after == core_source_before,
        "theorem_language": extracted["conditional"],
        "theorem_string_occurrences": len(suspicious_theorem_strings),
        "boundary": boundary,
        "boundary_keys": boundary_keys,
        "exact": exact,
    }


def public_report(value: object) -> object:
    if isinstance(value, dict):
        return {
            key: public_report(item)
            for key, item in value.items()
            if not (isinstance(key, str) and key.startswith("_"))
        }
    if isinstance(value, tuple):
        return tuple(public_report(item) for item in value)
    if isinstance(value, list):
        return [public_report(item) for item in value]
    return value


def main() -> int:
    started = perf_counter()
    primary_source = read_audit_input(AUDIT_INPUT_PATHS[0])
    core_source_before = read_audit_input(AUDIT_INPUT_PATHS[1])
    self_source = Path(__file__).read_text(encoding="utf-8")
    checks: dict[str, bool] = {}
    reports: dict[str, object] = {}

    def run(
        label: str,
        function: object,
        *arguments: object,
    ) -> dict[str, object]:
        try:
            report = function(*arguments)
            passed = bool(report["exact"])
        except Exception as error:
            report = {
                "exact": False,
                "exception": f"{type(error).__name__}: {error}",
            }
            passed = False
        checks[label] = passed
        reports[label] = public_report(report)
        return report

    extracted = run(
        "extraction",
        extraction,
        primary_source,
        self_source,
    )
    law = run("law_recount", law_recount, extracted)
    run("equivalence_recount", equivalence_recount, extracted, law)
    extension = run("extension_recount", extension_recount, extracted, law)
    orbit = run("orbit_spot_recount", orbit_spot_recount, extracted, law)
    run(
        "discipline",
        discipline,
        extracted,
        self_source,
        core_source_before,
        extension,
        orbit,
    )

    elapsed = perf_counter() - started
    timeout_pass = elapsed < AUDIT_TIMEOUT_SEC
    checks["runtime_under_timeout"] = timeout_pass
    reports["runtime_under_timeout"] = {
        "seconds": round(elapsed, 6),
        "limit_seconds": AUDIT_TIMEOUT_SEC,
        "exact": timeout_pass,
    }
    report = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "runtime_seconds": round(elapsed, 6),
        "certificates": reports,
    }
    report["pass"] = all(checks.values())
    report["terminal"] = (
        "CYCLE740_MAPPER_INDEPENDENT_CHECK_ALL_PASS"
        if report["pass"]
        else "CYCLE740_MAPPER_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(
        stable_json_bytes(report)
    ).hexdigest()
    lines = [
        f"{'PASS' if passed else 'FAIL'} {label} :: {passed}"
        for label, passed in checks.items()
    ]
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(lines + ["SUMMARY_JSON " + final_json, report["terminal"]])
    output_size = len((text + "\n").encode())
    if output_size >= STDOUT_LIMIT_BYTES:
        print(
            "FAIL stdout_under_150KB :: "
            f"{output_size} >= {STDOUT_LIMIT_BYTES}"
        )
        return 1
    print(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
