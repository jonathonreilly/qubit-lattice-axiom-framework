#!/usr/bin/env python3
"""Independent bounded checker for the Cycle-746 locked archive.

Cycle 746 is never imported.  Its source is parsed as data, while the three
declared landed inputs are exercised through independent transition and
comparison code.
"""

from __future__ import annotations

import ast
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Iterable

import frontier_cycle745_enforced_dual_rail_lock_2026_07_28 as L745
import frontier_cycle741_physical_bank_renewal_2026_07_28 as N741
import frontier_cycle742_archive_record_readout_feed_2026_07_28 as F742


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/LOCKED_ARCHIVE_CYCLE746_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py",
    "scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py",
    "scripts/frontier_cycle742_archive_record_readout_feed_2026_07_28.py",
)

PRIMARY_PATH = "scripts/frontier_cycle746_locked_archive_2026_07_28.py"
BLOCKLIST = (
    "scripts/frontier_cycle746_locked_archive_2026_07_28.py",
)
STDOUT_LIMIT_BYTES = 150 * 1024
EXPECTED_ALPHABET = (
    "IDLE",
    "READ",
    "STRAY_WRITE[0]",
    "STRAY_WRITE[1]",
    "RENEWAL_ATTEMPT[g1]",
    "RENEWAL_ATTEMPT[g2]",
    "RENEWAL_ATTEMPT[g3]",
)
EXPECTED_INPUTS = (
    "scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py",
    "scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py",
    "scripts/frontier_cycle742_archive_record_readout_feed_2026_07_28.py",
)
EXPECTED_W5_RESIDUAL = (
    "axiom-level permanence semantics beyond the declared alphabet"
)
EXHAUSTIVE_TILE_FAMILY = tuple(range(303))
COMPOSITION_CELL_WINDOW = tuple(range(296, 310))

Persistent = tuple[int, int, int]
State = tuple[int, int, int, int, int, int, int]
ArchiveState = tuple[Persistent, ...]

CHECKS: dict[str, bool] = {}
DETAILS: dict[str, dict[str, object]] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool, detail: dict[str, object]) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    DETAILS[label] = {"passed": passed, **detail}
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label}")
    return passed


def file_digest(path: str) -> str:
    return sha256(Path(path).read_bytes()).hexdigest()


def module_assignment(tree: ast.Module, name: str) -> ast.AST:
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target in (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        if isinstance(target, ast.Name) and target.id == name
    ]
    if len(matches) != 1:
        raise ValueError(("module assignment cardinality", name, len(matches)))
    return matches[0]


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise ValueError(("function cardinality", name, len(matches)))
    return matches[0]


def local_assignment(function: ast.FunctionDef, name: str) -> ast.AST:
    matches = [
        node.value
        for node in ast.walk(function)
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target in (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        if isinstance(target, ast.Name) and target.id == name
    ]
    if len(matches) != 1:
        raise ValueError(
            ("local assignment cardinality", function.name, name, len(matches))
        )
    return matches[0]


def subscript_key(node: ast.AST, owner: str, key: str) -> bool:
    return (
        isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
        and node.value.id == owner
        and isinstance(node.slice, ast.Constant)
        and node.slice.value == key
    )


def attribute_is(node: ast.AST, owner: str, attribute: str) -> bool:
    return (
        isinstance(node, ast.Attribute)
        and isinstance(node.value, ast.Name)
        and node.value.id == owner
        and node.attr == attribute
    )


def call_is(node: ast.AST, owner: str, attribute: str) -> bool:
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and attribute_is(node.func, owner, attribute)
    )


def has_subscript_constant_compare(
    function: ast.FunctionDef,
    owner: str,
    key: str,
    value: object,
) -> bool:
    return any(
        isinstance(node, ast.Compare)
        and len(node.ops) == len(node.comparators) == 1
        and isinstance(node.ops[0], (ast.Eq, ast.Is))
        and subscript_key(node.left, owner, key)
        and isinstance(node.comparators[0], ast.Constant)
        and node.comparators[0].value == value
        for node in ast.walk(function)
    )


def has_subscript_attribute_compare(
    function: ast.FunctionDef,
    left_owner: str,
    key: str,
    right_owner: str,
    attribute: str,
) -> bool:
    return any(
        isinstance(node, ast.Compare)
        and len(node.ops) == len(node.comparators) == 1
        and isinstance(node.ops[0], ast.Eq)
        and subscript_key(node.left, left_owner, key)
        and attribute_is(node.comparators[0], right_owner, attribute)
        for node in ast.walk(function)
    )


def is_len_name(node: ast.AST, name: str) -> bool:
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "len"
        and len(node.args) == 1
        and isinstance(node.args[0], ast.Name)
        and node.args[0].id == name
        and not node.keywords
    )


def is_len_subscript(
    node: ast.AST, owner: str, key: str
) -> bool:
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "len"
        and len(node.args) == 1
        and subscript_key(node.args[0], owner, key)
        and not node.keywords
    )


def dict_value(node: ast.AST, key: str) -> ast.AST:
    if not isinstance(node, ast.Dict):
        raise ValueError(("not a dict", key))
    matches = [
        value
        for candidate, value in zip(node.keys, node.values)
        if (
            isinstance(candidate, ast.Constant)
            and candidate.value == key
        )
    ]
    if len(matches) != 1:
        raise ValueError(("dict key cardinality", key, len(matches)))
    return matches[0]


def extraction(source: str) -> tuple[bool, dict[str, object]]:
    """Extract all Cycle-746 claims without evaluating its code."""

    tree = ast.parse(source, filename=PRIMARY_PATH)
    audit_node = module_assignment(tree, "AUDIT_INPUT_PATHS")
    audit_inputs = ast.literal_eval(audit_node)
    note_path = ast.literal_eval(module_assignment(tree, "NOTE_PATH"))
    timeout = ast.literal_eval(module_assignment(tree, "AUDIT_TIMEOUT_SEC"))
    alphabet = ast.literal_eval(module_assignment(tree, "ARCHIVE_ALPHABET"))
    residual = ast.literal_eval(module_assignment(tree, "W5_RESIDUAL"))
    locked_alias = module_assignment(tree, "LOCKED_WRITE_WORD")

    pure_audit_tuple = (
        isinstance(audit_node, ast.Tuple)
        and all(isinstance(element, ast.Constant) for element in audit_node.elts)
        and isinstance(audit_inputs, tuple)
        and all(isinstance(path, str) for path in audit_inputs)
    )
    alias_exact = attribute_is(locked_alias, "L745", "WRITE_WORD")

    layout_function = function_node(tree, "tiled_layout_certificate")
    layout_calls_archive_sites = any(
        call_is(node, "F742", "archive_sites")
        for node in ast.walk(layout_function)
    )
    layout_uses_rails = any(
        attribute_is(node, "L745", "RAILS")
        for node in ast.walk(layout_function)
    )
    layout_uses_site_layout = any(
        attribute_is(node, "L745", "SITE_LAYOUT")
        for node in ast.walk(layout_function)
    )

    certificate_b = function_node(tree, "certificate_b")
    tiling_claims = {
        "archive_payload_sites": 909,
        "cells_per_tile": 7,
        "composite_M2_sites": 6363,
    }
    tiling_literals_exact = all(
        has_subscript_constant_compare(
            certificate_b, "layout", key, value
        )
        for key, value in tiling_claims.items()
    )
    details_b = local_assignment(certificate_b, "details")
    tiled_actions = dict_value(
        details_b, "tiled_lock_gate_actions_per_generation"
    )
    tiled_actions_shape = (
        isinstance(tiled_actions, ast.BinOp)
        and isinstance(tiled_actions.op, ast.Mult)
        and attribute_is(tiled_actions.left, "N741", "RECORD_WIDTH")
        and is_len_name(tiled_actions.right, "LOCKED_WRITE_WORD")
    )

    certificate_c = function_node(tree, "certificate_c")
    direct_formula = local_assignment(certificate_c, "direct_expected")
    renewal_formula = local_assignment(certificate_c, "renewal_expected")
    direct_formula_exact = (
        isinstance(direct_formula, ast.BinOp)
        and isinstance(direct_formula.op, ast.Mult)
        and isinstance(direct_formula.left, ast.Constant)
        and direct_formula.left.value == 2
        and attribute_is(direct_formula.right, "N741", "ARCHIVE_WIDTH")
    )
    renewal_formula_exact = (
        isinstance(renewal_formula, ast.BinOp)
        and isinstance(renewal_formula.op, ast.Mult)
        and is_len_subscript(
            renewal_formula.left, "run", "archived_images"
        )
        and attribute_is(
            renewal_formula.right, "N741", "ARCHIVE_WIDTH"
        )
    )

    certificate_f = function_node(tree, "certificate_f")
    fresh_formula_exact = (
        has_subscript_attribute_compare(
            certificate_f,
            "row",
            "fresh_cells_before",
            "N741",
            "RECORD_WIDTH",
        )
        and has_subscript_attribute_compare(
            certificate_f,
            "row",
            "first_write_accepts",
            "N741",
            "RECORD_WIDTH",
        )
        and has_subscript_constant_compare(
            certificate_f, "run", "accepted_first_writes", 909
        )
        and any(
            isinstance(node, ast.Compare)
            and len(node.ops) == len(node.comparators) == 1
            and isinstance(node.ops[0], ast.Eq)
            and is_len_name(node.left, "rows")
            and isinstance(node.comparators[0], ast.Constant)
            and node.comparators[0].value == 3
            for node in ast.walk(certificate_f)
        )
    )

    certificate_d = function_node(tree, "certificate_d")
    base_formula_exact = has_subscript_constant_compare(
        certificate_d, "induction", "base_cases", 909
    )
    step_formula_exact = any(
        isinstance(node, ast.Compare)
        and len(node.ops) == len(node.comparators) == 1
        and isinstance(node.ops[0], ast.Eq)
        and subscript_key(
            node.left, "induction", "step_cell_transitions"
        )
        and isinstance(node.comparators[0], ast.BinOp)
        and isinstance(node.comparators[0].op, ast.Mult)
        and isinstance(node.comparators[0].left, ast.Constant)
        and node.comparators[0].left.value == 909
        and is_len_name(
            node.comparators[0].right, "ARCHIVE_ALPHABET"
        )
        for node in ast.walk(certificate_d)
    )

    certificate_h = function_node(tree, "certificate_h")
    boundary_node = local_assignment(certificate_h, "boundary")
    locked_boundary = ast.literal_eval(
        dict_value(boundary_node, "locked_archive_derived")
    )
    permanence_boundary = ast.literal_eval(
        dict_value(boundary_node, "record_permanence_claimed")
    )

    imported_aliases = {
        alias.asname: alias.name
        for node in tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.asname in {"L745", "N741", "F742"}
    }
    imports_exact = imported_aliases == {
        "L745": (
            "frontier_cycle745_enforced_dual_rail_lock_2026_07_28"
        ),
        "N741": "frontier_cycle741_physical_bank_renewal_2026_07_28",
        "F742": (
            "frontier_cycle742_archive_record_readout_feed_2026_07_28"
        ),
    }

    observed = {
        "archive_alphabet": alphabet,
        "audit_inputs": audit_inputs,
        "boundary_keys": {
            "locked_archive_derived": locked_boundary,
            "record_permanence_claimed": permanence_boundary,
        },
        "frozen_censuses": {
            "fresh_accepts_by_generation": (
                N741.RECORD_WIDTH,
                N741.RECORD_WIDTH,
                N741.RECORD_WIDTH,
            ),
            "overwrite_refusals": 2 * N741.ARCHIVE_WIDTH,
            "renewal_refusals": (
                N741.ARCHIVE_SLOTS * N741.ARCHIVE_WIDTH
            ),
        },
        "induction": {
            "base_cases": N741.ARCHIVE_WIDTH,
            "step_cell_transitions": (
                N741.ARCHIVE_WIDTH * len(alphabet)
            ),
        },
        "note_path": note_path,
        "tiling": {
            **tiling_claims,
            "computed_product": (
                tiling_claims["archive_payload_sites"]
                * tiling_claims["cells_per_tile"]
            ),
        },
        "timeout_seconds": timeout,
        "word_sizes": {
            "L745_IDLE": len(L745.IDLE_WORD),
            "L745_READ": len(L745.READ_WORD),
            "L745_WRITE": len(L745.WRITE_WORD),
            "N741_RENEWAL": len(N741.renewal_word()),
            "tiled_write_gate_actions_per_generation": (
                N741.RECORD_WIDTH * len(L745.WRITE_WORD)
            ),
        },
        "w5_residual": residual,
    }
    structural = {
        "audit_tuple_pure_literal": pure_audit_tuple,
        "base_formula_exact": base_formula_exact,
        "direct_formula_exact": direct_formula_exact,
        "fresh_formula_exact": fresh_formula_exact,
        "imports_exact": imports_exact,
        "layout_calls_F742_archive_sites": layout_calls_archive_sites,
        "layout_uses_L745_RAILS": layout_uses_rails,
        "layout_uses_L745_SITE_LAYOUT": layout_uses_site_layout,
        "locked_word_exact_alias": alias_exact,
        "renewal_formula_exact": renewal_formula_exact,
        "step_formula_exact": step_formula_exact,
        "tiled_actions_formula_exact": tiled_actions_shape,
        "tiling_literals_exact": tiling_literals_exact,
    }
    passed = (
        all(structural.values())
        and audit_inputs == EXPECTED_INPUTS
        and note_path == NOTE_PATH
        and timeout == AUDIT_TIMEOUT_SEC
        and alphabet == EXPECTED_ALPHABET
        and residual == EXPECTED_W5_RESIDUAL
        and observed["tiling"]["computed_product"] == 6363
        and observed["word_sizes"][
            "tiled_write_gate_actions_per_generation"
        ] == 2424
        and observed["frozen_censuses"]["overwrite_refusals"] == 1818
        and observed["frozen_censuses"]["renewal_refusals"] == 2727
        and observed["frozen_censuses"][
            "fresh_accepts_by_generation"
        ] == (303, 303, 303)
        and observed["induction"] == {
            "base_cases": 909,
            "step_cell_transitions": 6363,
        }
        and locked_boundary is True
        and permanence_boundary is False
    )
    return bool(passed), {
        "observed": observed,
        "structural_checks": structural,
    }


def own_bits_to_state(bits: Iterable[int]) -> State:
    state = tuple(int(bit) for bit in bits)
    if len(state) != 7 or any(bit not in (0, 1) for bit in state):
        raise ValueError(("invalid seven-rail state", state))
    return state  # type: ignore[return-value]


def own_apply_gate(state: State, gate: object) -> State:
    enabled = all(
        state[L745.RAIL_INDEX[rail]] == value
        for rail, value in gate.controls
    )
    if not enabled:
        return state
    output = list(state)
    if gate.operation == "X" and len(gate.targets) == 1:
        output[L745.RAIL_INDEX[gate.targets[0]]] ^= 1
    elif gate.operation == "SWAP" and len(gate.targets) == 2:
        left = L745.RAIL_INDEX[gate.targets[0]]
        right = L745.RAIL_INDEX[gate.targets[1]]
        output[left], output[right] = output[right], output[left]
    else:
        raise ValueError(
            ("unsupported landed gate", gate.operation, gate.targets)
        )
    return own_bits_to_state(output)


def own_apply_word(state: State, word: Iterable[object]) -> State:
    output = state
    for gate in word:
        output = own_apply_gate(output, gate)
    return output


def own_packet(
    persistent: Persistent, offered: int, request: int = 1
) -> State:
    d_bit, u_bit, l_bit = persistent
    return own_bits_to_state(
        (d_bit, offered, u_bit, l_bit, request, 0, 0)
    )


def own_persistent(state: State) -> Persistent:
    return (
        state[L745.RAIL_INDEX["D"]],
        state[L745.RAIL_INDEX["U"]],
        state[L745.RAIL_INDEX["L"]],
    )


def own_output_tag(state: State) -> str:
    request = state[L745.RAIL_INDEX["Q_in"]]
    accept = state[L745.RAIL_INDEX["Q_accept"]]
    refuse = state[L745.RAIL_INDEX["Q_refuse"]]
    if (request, accept, refuse) == (0, 1, 0):
        return "ACCEPTED"
    if (request, accept, refuse) == (0, 0, 1):
        return "REFUSED"
    return "DIRTY"


def gate_signature(word: Iterable[object]) -> tuple[object, ...]:
    return tuple(
        (gate.name, gate.operation, tuple(gate.targets), tuple(gate.controls))
        for gate in word
    )


def tiling_recount(
    extracted: dict[str, object],
) -> tuple[bool, dict[str, object]]:
    """Recount composite sites and independently simulate tiled WRITE_WORD."""

    archive_sites = F742.archive_sites()
    local_sites = tuple(L745.SITE_LAYOUT[rail] for rail in L745.RAILS)
    addresses = tuple(
        (archive_site, local_site)
        for archive_site in archive_sites
        for local_site in local_sites
    )
    reference_signature = gate_signature(L745.WRITE_WORD)
    tiled_words = tuple(L745.WRITE_WORD for _site in archive_sites)
    same_word_tiles = sum(
        gate_signature(word) == reference_signature for word in tiled_words
    )

    exhaustive_state_rows = 0
    exhaustive_semantic_rows = 0
    exhaustive_failures = 0
    reverse_word = tuple(reversed(L745.WRITE_WORD))
    for cell in EXHAUSTIVE_TILE_FAMILY:
        if cell >= len(archive_sites):
            exhaustive_failures += 1
            continue
        word = tiled_words[cell]
        for bits in product((0, 1), repeat=7):
            state = own_bits_to_state(bits)
            after = own_apply_word(state, word)
            restored = own_apply_word(after, reverse_word)
            exhaustive_state_rows += 1
            exhaustive_failures += int(restored != state)
        for offered in (0, 1):
            event = own_apply_word(
                own_packet((0, *L745.UNLOCKED), offered), word
            )
            exhaustive_semantic_rows += 1
            exhaustive_failures += int(
                own_output_tag(event) != "ACCEPTED"
                or own_persistent(event) != (offered, *L745.LOCKED)
            )
        for d_bit, offered in product((0, 1), repeat=2):
            before = (d_bit, *L745.LOCKED)
            event = own_apply_word(own_packet(before, offered), word)
            exhaustive_semantic_rows += 1
            exhaustive_failures += int(
                own_output_tag(event) != "REFUSED"
                or own_persistent(event) != before
            )

    spotted_cells = tuple(
        cell
        for cell in range(len(archive_sites))
        if cell not in set(EXHAUSTIVE_TILE_FAMILY)
    )
    spot_rows = 0
    spot_failures = 0
    for cell in spotted_cells:
        word = tiled_words[cell]
        state = own_bits_to_state(
            (cell >> bit) & 1 for bit in range(7)
        )
        spot_rows += 1
        spot_failures += int(
            own_apply_word(own_apply_word(state, word), reverse_word)
            != state
        )
        for offered in (0, 1):
            before = (cell & 1, *L745.LOCKED)
            event = own_apply_word(own_packet(before, offered), word)
            spot_rows += 1
            spot_failures += int(
                own_output_tag(event) != "REFUSED"
                or own_persistent(event) != before
            )

    detail = {
        "address_recount": {
            "archive_payload_sites": len(archive_sites),
            "cells_per_tile": len(local_sites),
            "composite_sites": len(addresses),
            "unique_composite_sites": len(set(addresses)),
        },
        "exhausted": (
            "physical archive cells 0..302 (the complete first 303-cell "
            "region): all 128 seven-rail states for inverse exactness, plus "
            "both first-write offers and all four locked (D,offer) rows"
        ),
        "exhaustive_cell_count": len(EXHAUSTIVE_TILE_FAMILY),
        "exhaustive_full_state_rows": exhaustive_state_rows,
        "exhaustive_semantic_rows": exhaustive_semantic_rows,
        "exhaustive_failures": exhaustive_failures,
        "same_literal_word_tiles": same_word_tiles,
        "spot_policy": (
            "every remaining cell 303..908: one index-derived seven-rail "
            "state plus both locked offers"
        ),
        "spotted_cell_count": len(spotted_cells),
        "spot_rows": spot_rows,
        "spot_failures": spot_failures,
        "tiled_write_gate_actions_per_generation": (
            N741.RECORD_WIDTH * len(L745.WRITE_WORD)
        ),
    }
    extracted_observed = extracted["observed"]
    extracted_tiling = extracted_observed["tiling"]
    passed = (
        len(archive_sites) == N741.ARCHIVE_WIDTH == 909
        and len(local_sites) == len(set(local_sites)) == 7
        and len(addresses) == len(set(addresses)) == 6363
        and extracted_tiling["computed_product"] == 6363
        and len(L745.WRITE_WORD) == 8
        and detail["tiled_write_gate_actions_per_generation"] == 2424
        and same_word_tiles == 909
        and len(EXHAUSTIVE_TILE_FAMILY) == 303
        and exhaustive_state_rows == 303 * 128
        and exhaustive_semantic_rows == 303 * 6
        and exhaustive_failures == 0
        and len(spotted_cells) == 606
        and spot_rows == 606 * 3
        and spot_failures == 0
    )
    return bool(passed), detail


def physical_slots(storage: ArchiveState) -> tuple[tuple[int, ...], ...]:
    bits = tuple(cell[0] for cell in storage)
    return tuple(
        bits[
            slot * N741.RECORD_WIDTH:
            (slot + 1) * N741.RECORD_WIDTH
        ]
        for slot in range(N741.ARCHIVE_SLOTS)
    )


def logical_view(
    storage: ArchiveState, occupied: int
) -> tuple[tuple[int, ...], ...]:
    slots = physical_slots(storage)
    return tuple(reversed(slots[:occupied])) + (
        (N741.ZERO_ARCHIVE_SLOT,) * (N741.ARCHIVE_SLOTS - occupied)
    )


def build_locked_generations() -> dict[str, object]:
    """Build the physical archive using only the independent gate simulator."""

    storage: ArchiveState = tuple(
        (0, *L745.UNLOCKED) for _ in range(N741.ARCHIVE_WIDTH)
    )
    data = N741.GENESIS_STATE
    semantic_archives = (
        N741.ZERO_ARCHIVE_SLOT,
    ) * N741.ARCHIVE_SLOTS
    renewal_word = N741.renewal_word()
    images: list[tuple[int, ...]] = []
    generation_rows: list[dict[str, object]] = []

    for generation, directions in enumerate(
        N741.GENERATION_DIRECTIONS, start=1
    ):
        data_started_genesis = data == N741.GENESIS_STATE
        exhausted, fill = N741.fill_generation(data, directions)
        image = N741.record_image(exhausted)
        source_banks, _source_links = N741.K.M.unpack_state(
            exhausted, N741.FIXTURE_BANKS
        )
        source_payloads = N741.cell_payloads(source_banks)
        before = storage
        start = (generation - 1) * N741.RECORD_WIDTH
        stop = start + N741.RECORD_WIDTH
        mutable = list(storage)
        fresh = 0
        accepts = 0
        blocks = 0
        for offset, offered in enumerate(image):
            index = start + offset
            cell = mutable[index]
            fresh += int(cell == (0, *L745.UNLOCKED))
            event = own_apply_word(
                own_packet(cell, offered), L745.WRITE_WORD
            )
            accepted = (
                own_output_tag(event) == "ACCEPTED"
                and own_persistent(event) == (offered, *L745.LOCKED)
            )
            accepts += int(accepted)
            blocks += int(not accepted)
            mutable[index] = own_persistent(event)
        storage = tuple(mutable)
        images.append(image)
        view = logical_view(storage, generation)

        combined = N741.pack_combined(exhausted, semantic_archives)
        renewed = N741.K.A.apply_semantic(combined, renewal_word)
        data, semantic_archives = N741.split_combined(renewed)

        records = F742.embed_archive(view)
        flat_readout = F742.readout_bits(records)
        own_split = tuple(
            flat_readout[
                slot * N741.RECORD_WIDTH:
                (slot + 1) * N741.RECORD_WIDTH
            ]
            for slot in range(N741.ARCHIVE_SLOTS)
        )
        payloads = F742.payloads_from_record_image(own_split[0])
        payload_exact = tuple(
            bytes(observed) == bytes(expected)
            for observed, expected in zip(payloads, source_payloads)
        )
        generation_rows.append({
            "accepts": accepts,
            "blocks": blocks,
            "data_started_genesis": data_started_genesis,
            "fill_violations": fill["violation_count"],
            "fresh": fresh,
            "generation": generation,
            "image": image,
            "logical_view": view,
            "new_region_locked": all(
                storage[index]
                == (image[index - start], *L745.LOCKED)
                for index in range(start, stop)
            ),
            "payload_exact": payload_exact,
            "prior_and_other_regions_unchanged": (
                storage[:start] == before[:start]
                and storage[stop:] == before[stop:]
            ),
            "readout_flat_byte_exact": (
                bytes(flat_readout)
                == bytes(bit for slot in view for bit in slot)
            ),
            "readout_split_exact": own_split == view,
            "semantic_archive_exact": semantic_archives == view,
            "semantic_data_restored": data == N741.GENESIS_STATE,
        })

    return {
        "generation_rows": tuple(generation_rows),
        "images": tuple(images),
        "renewal_word_size": len(renewal_word),
        "storage": storage,
    }


def renewal_patterns(
    images: tuple[tuple[int, ...], ...],
) -> dict[str, tuple[int, ...]]:
    final_logical = tuple(reversed(images))
    patterns: dict[str, tuple[int, ...]] = {}
    for generation, image in enumerate(images, start=1):
        attempted_logical = (image,) + final_logical[:-1]
        attempted_physical = tuple(reversed(attempted_logical))
        patterns[f"RENEWAL_ATTEMPT[g{generation}]"] = tuple(
            bit for slot in attempted_physical for bit in slot
        )
    return patterns


def apply_macro_to_cell(
    cell: Persistent,
    label: str,
    cell_index: int,
    patterns: dict[str, tuple[int, ...]],
) -> tuple[Persistent, str]:
    if label == "IDLE":
        event = own_apply_word(own_packet(cell, 0, request=0), ())
    elif label == "READ":
        event = own_apply_word(
            own_packet(cell, 0, request=0), L745.READ_WORD
        )
    elif label == "STRAY_WRITE[0]":
        event = own_apply_word(own_packet(cell, 0), L745.WRITE_WORD)
    elif label == "STRAY_WRITE[1]":
        event = own_apply_word(own_packet(cell, 1), L745.WRITE_WORD)
    elif label in patterns:
        event = own_apply_word(
            own_packet(cell, patterns[label][cell_index]),
            L745.WRITE_WORD,
        )
    else:
        raise ValueError(("out-of-alphabet label", label))
    return own_persistent(event), own_output_tag(event)


def censuses_recount(run: dict[str, object]) -> tuple[bool, dict[str, object]]:
    storage = run["storage"]
    images = run["images"]
    generation_rows = run["generation_rows"]
    patterns = renewal_patterns(images)

    overwrite_rows = 0
    overwrite_refusals = 0
    overwrite_byte_alterations = 0
    same_value_refusals = 0
    opposite_value_refusals = 0
    for cell in storage:
        for offered in (0, 1):
            event = own_apply_word(
                own_packet(cell, offered), L745.WRITE_WORD
            )
            after = own_persistent(event)
            refused = own_output_tag(event) == "REFUSED"
            overwrite_rows += 1
            overwrite_refusals += int(refused)
            overwrite_byte_alterations += int(bytes(after) != bytes(cell))
            same_value_refusals += int(refused and offered == cell[0])
            opposite_value_refusals += int(
                refused and offered != cell[0]
            )

    renewal_rows = 0
    renewal_refusals = 0
    renewal_byte_alterations = 0
    for offered_bits in patterns.values():
        if len(offered_bits) != len(storage):
            raise ValueError(("renewal vector width", len(offered_bits)))
        for cell, offered in zip(storage, offered_bits):
            event = own_apply_word(
                own_packet(cell, offered), L745.WRITE_WORD
            )
            after = own_persistent(event)
            renewal_rows += 1
            renewal_refusals += int(
                own_output_tag(event) == "REFUSED"
            )
            renewal_byte_alterations += int(
                bytes(after) != bytes(cell)
            )

    fresh_accepts = tuple(row["accepts"] for row in generation_rows)
    fresh_cells = tuple(row["fresh"] for row in generation_rows)
    fresh_blocks = tuple(row["blocks"] for row in generation_rows)
    build_exact = all(
        row["data_started_genesis"]
        and row["fill_violations"] == 0
        and row["new_region_locked"]
        and row["prior_and_other_regions_unchanged"]
        and row["semantic_archive_exact"]
        and row["semantic_data_restored"]
        for row in generation_rows
    )
    detail = {
        "fresh_accepts_by_generation": fresh_accepts,
        "fresh_blocks_by_generation": fresh_blocks,
        "fresh_cells_by_generation": fresh_cells,
        "locked_bytes_invariant": (
            overwrite_byte_alterations == renewal_byte_alterations == 0
        ),
        "overwrite": {
            "byte_alterations": overwrite_byte_alterations,
            "opposite_value_refusals": opposite_value_refusals,
            "refusals": overwrite_refusals,
            "rows": overwrite_rows,
            "same_value_refusals": same_value_refusals,
        },
        "renewal": {
            "byte_alterations": renewal_byte_alterations,
            "family_members": len(patterns),
            "refusals": renewal_refusals,
            "rows": renewal_rows,
        },
    }
    passed = (
        len(generation_rows) == 3
        and build_exact
        and fresh_cells == (303, 303, 303)
        and fresh_accepts == (303, 303, 303)
        and fresh_blocks == (0, 0, 0)
        and overwrite_rows == overwrite_refusals == 1818
        and same_value_refusals == opposite_value_refusals == 909
        and overwrite_byte_alterations == 0
        and renewal_rows == renewal_refusals == 2727
        and renewal_byte_alterations == 0
    )
    return bool(passed), detail


def induction_recount(
    run: dict[str, object],
) -> tuple[bool, dict[str, object]]:
    storage = run["storage"]
    images = run["images"]
    expected = tuple(
        (bit, *L745.LOCKED)
        for image in images
        for bit in image
    )
    patterns = renewal_patterns(images)

    base_cases = len(storage)
    base_failures = sum(
        bytes(observed) != bytes(wanted)
        for observed, wanted in zip(storage, expected)
    )
    step_rows = 0
    step_alterations = 0
    step_refusal_failures = 0
    for label in EXPECTED_ALPHABET:
        write_like = label.startswith(
            ("STRAY_WRITE", "RENEWAL_ATTEMPT")
        )
        for index, cell in enumerate(storage):
            after, tag = apply_macro_to_cell(
                cell, label, index, patterns
            )
            step_rows += 1
            step_alterations += int(bytes(after) != bytes(cell))
            step_refusal_failures += int(
                write_like and tag != "REFUSED"
            )

    window = tuple(storage[index] for index in COMPOSITION_CELL_WINDOW)
    composition_words = 0
    nonempty_composition_words = 0
    composition_transition_rows = 0
    composition_alterations = 0
    composition_final_alterations = 0
    for length in range(4):
        for labels in product(EXPECTED_ALPHABET, repeat=length):
            composition_words += 1
            nonempty_composition_words += int(length > 0)
            state = window
            for label in labels:
                output: list[Persistent] = []
                for local_index, cell in enumerate(state):
                    global_index = COMPOSITION_CELL_WINDOW[local_index]
                    after, _tag = apply_macro_to_cell(
                        cell, label, global_index, patterns
                    )
                    output.append(after)
                    composition_transition_rows += 1
                    composition_alterations += int(
                        bytes(after) != bytes(cell)
                    )
                state = tuple(output)
            composition_final_alterations += sum(
                bytes(observed) != bytes(original)
                for observed, original in zip(state, window)
            )

    detail = {
        "base_cases": base_cases,
        "base_failures": base_failures,
        "composition_sweep": {
            "alphabet_size": len(EXPECTED_ALPHABET),
            "cell_window": COMPOSITION_CELL_WINDOW,
            "final_alterations": composition_final_alterations,
            "includes_empty_word": True,
            "max_word_length": 3,
            "nonempty_words": nonempty_composition_words,
            "transition_alterations": composition_alterations,
            "transition_rows": composition_transition_rows,
            "words_including_empty": composition_words,
        },
        "step_alterations": step_alterations,
        "step_cell_transitions": step_rows,
        "step_refusal_failures": step_refusal_failures,
    }
    passed = (
        base_cases == 909
        and len(expected) == 909
        and base_failures == 0
        and step_rows == 909 * 7 == 6363
        and step_alterations == 0
        and step_refusal_failures == 0
        and COMPOSITION_CELL_WINDOW == tuple(range(296, 310))
        and composition_words == 1 + 7 + 49 + 343 == 400
        and nonempty_composition_words == 399
        and composition_transition_rows
        == len(COMPOSITION_CELL_WINDOW) * (7 + 2 * 49 + 3 * 343)
        and composition_alterations == 0
        and composition_final_alterations == 0
    )
    return bool(passed), detail


def readout_recount(
    run: dict[str, object],
) -> tuple[bool, dict[str, object]]:
    generation_rows = run["generation_rows"]
    rows: list[dict[str, object]] = []
    total_bits = 0
    for row in generation_rows:
        view = row["logical_view"]
        before = tuple(tuple(slot) for slot in view)
        records = F742.embed_archive(view)
        observed = F742.readout_bits(records)
        expected = tuple(bit for slot in view for bit in slot)
        own_split = tuple(
            observed[
                slot * N741.RECORD_WIDTH:
                (slot + 1) * N741.RECORD_WIDTH
            ]
            for slot in range(N741.ARCHIVE_SLOTS)
        )
        observed_payloads = F742.payloads_from_record_image(own_split[0])
        source_banks, _source_links = N741.K.M.unpack_state(
            tuple(
                N741.GENESIS_STATE[wire]
                if wire not in set(N741.RECORD_WIRES)
                else row["image"][N741.RECORD_WIRES.index(wire)]
                for wire in range(N741.DATA_WIDTH)
            ),
            N741.FIXTURE_BANKS,
        )
        expected_payloads = N741.cell_payloads(source_banks)
        payload_matches = tuple(
            bytes(observed_payload) == bytes(expected_payload)
            for observed_payload, expected_payload in zip(
                observed_payloads, expected_payloads
            )
        )
        total_bits += len(observed)
        rows.append({
            "archive_unchanged": before == view,
            "bits_compared": len(observed),
            "byte_exact": bytes(observed) == bytes(expected),
            "generation": row["generation"],
            "payload_matches": payload_matches,
            "records": len(records),
            "split_exact": own_split == view,
        })
    passed = (
        len(rows) == 3
        and total_bits == 3 * 909
        and all(
            row["records"] == 909
            and row["bits_compared"] == 909
            and row["byte_exact"]
            and row["split_exact"]
            and row["archive_unchanged"]
            and len(row["payload_matches"]) == 4
            and all(row["payload_matches"])
            for row in rows
        )
    )
    return bool(passed), {
        "byte_exact_by_generation": tuple(
            row["byte_exact"] for row in rows
        ),
        "generation_rows": tuple(rows),
        "total_bits_compared": total_bits,
    }


def discipline(
    hashes_before: dict[str, str],
    extracted: dict[str, object],
) -> tuple[bool, dict[str, object]]:
    hashes_after = {
        path: file_digest(path)
        for path in (PRIMARY_PATH,) + AUDIT_INPUT_PATHS
    }
    primary_module = Path(PRIMARY_PATH).stem
    primary_imported = primary_module in sys.modules
    boundary = extracted["observed"]["boundary_keys"]
    detail = {
        "audit_inputs_literal_and_exact": (
            extracted["observed"]["audit_inputs"] == AUDIT_INPUT_PATHS
        ),
        "blocklist": BLOCKLIST,
        "blocklisted_primary_imported": primary_imported,
        "boundary_keys": boundary,
        "input_hashes_unchanged": hashes_after == hashes_before,
        "landed_writes": 0 if hashes_after == hashes_before else "detected",
        "note_path_exact": (
            extracted["observed"]["note_path"] == NOTE_PATH
        ),
        "permanence_scope": EXPECTED_W5_RESIDUAL,
    }
    passed = (
        BLOCKLIST == (PRIMARY_PATH,)
        and not primary_imported
        and hashes_after == hashes_before
        and extracted["observed"]["audit_inputs"] == AUDIT_INPUT_PATHS
        and extracted["observed"]["note_path"] == NOTE_PATH
        and boundary == {
            "locked_archive_derived": True,
            "record_permanence_claimed": False,
        }
        and extracted["observed"]["w5_residual"]
        == EXPECTED_W5_RESIDUAL
    )
    return bool(passed), detail


def honest_failure(error: Exception) -> dict[str, object]:
    return {"error": f"{type(error).__name__}: {error}"}


def main() -> int:
    started = perf_counter()
    hashes_before = {
        path: file_digest(path)
        for path in (PRIMARY_PATH,) + AUDIT_INPUT_PATHS
    }
    source = Path(PRIMARY_PATH).read_text(encoding="utf-8")

    extracted: dict[str, object] = {}
    run: dict[str, object] = {}

    try:
        extraction_passed, extraction_detail = extraction(source)
        extracted = extraction_detail
    except Exception as error:
        extraction_passed = False
        extraction_detail = honest_failure(error)
    check("extraction", extraction_passed, extraction_detail)

    try:
        tiling_passed, tiling_detail = tiling_recount(extracted)
    except Exception as error:
        tiling_passed = False
        tiling_detail = honest_failure(error)
    check("tiling_recount", tiling_passed, tiling_detail)

    try:
        run = build_locked_generations()
        census_passed, census_detail = censuses_recount(run)
    except Exception as error:
        census_passed = False
        census_detail = honest_failure(error)
    check("censuses_recount", census_passed, census_detail)

    try:
        induction_passed, induction_detail = induction_recount(run)
    except Exception as error:
        induction_passed = False
        induction_detail = honest_failure(error)
    check("induction_recount", induction_passed, induction_detail)

    try:
        readout_passed, readout_detail = readout_recount(run)
    except Exception as error:
        readout_passed = False
        readout_detail = honest_failure(error)
    check("readout_recount", readout_passed, readout_detail)

    try:
        discipline_passed, discipline_detail = discipline(
            hashes_before, extracted
        )
    except Exception as error:
        discipline_passed = False
        discipline_detail = honest_failure(error)
    check("discipline", discipline_passed, discipline_detail)

    elapsed = perf_counter() - started
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
        "NOTE_PATH": NOTE_PATH,
        "all_pass": all(CHECKS.values()),
        "blocklist": BLOCKLIST,
        "bounded": True,
        "checks": dict(sorted(DETAILS.items())),
        "checks_failed": sum(not passed for passed in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "locked_archive_derived": (
            extracted.get("observed", {})
            .get("boundary_keys", {})
            .get("locked_archive_derived", False)
        ),
        "record_permanence_claimed": False,
        "runtime_seconds": round(elapsed, 6),
        "terminal": (
            "CYCLE746_INDEPENDENT_CHECK_PASS"
            if all(CHECKS.values())
            else "CYCLE746_INDEPENDENT_CHECK_HONEST_FAIL"
        ),
    }
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    output = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    output_bytes = len(output.encode())
    if output_bytes >= STDOUT_LIMIT_BYTES:
        sys.stderr.write(
            f"stdout bound exceeded: {output_bytes} >= "
            f"{STDOUT_LIMIT_BYTES}\n"
        )
        return 1
    sys.stdout.write(output)
    return 0 if report["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
