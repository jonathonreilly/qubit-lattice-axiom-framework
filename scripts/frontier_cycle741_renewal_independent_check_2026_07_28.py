#!/usr/bin/env python3
"""Independent bounded checker for Cycle 741 physical-bank renewal.

The Cycle 741 primary is parsed as data and is never imported.  All state
evolution below is performed by a small local bit simulator over the public
Cycle 719 gate/program interface.
"""
from __future__ import annotations

import ast
from hashlib import sha256
import json
import sys
from time import perf_counter

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/PHYSICAL_BANK_RENEWAL_CYCLE741_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

PRIMARY_PATH, K_PATH = AUDIT_INPUT_PATHS
STDOUT_LIMIT_BYTES = 150 * 1024
FIXTURE_BANKS = 2
ARCHIVE_SLOTS = 3
CAPACITY_ORBITS = 4
DATA_WIDTH = K.M.R12.TOTAL_WIRES
MATTER_WIRES = tuple(range(K.M.R12.SOURCE_WIDTH))
BANK_WIRES = tuple(
    wire
    for base in K.M.R12.BANK_BASES[:FIXTURE_BANKS]
    for wire in range(base, base + K.A.N)
)
RECORD_WIRES = MATTER_WIRES + BANK_WIRES
RECORD_WIDTH = len(RECORD_WIRES)
ARCHIVE_WIDTH = ARCHIVE_SLOTS * RECORD_WIDTH
FULL_WIDTH = DATA_WIDTH + ARCHIVE_WIDTH
ARCHIVE_SLOT_WIRES = tuple(
    tuple(
        DATA_WIDTH + slot * RECORD_WIDTH + offset
        for offset in range(RECORD_WIDTH)
    )
    for slot in range(ARCHIVE_SLOTS)
)
ZERO_ARCHIVE_SLOT = (0,) * RECORD_WIDTH
GENERATION_DIRECTIONS = (
    ((1, 0), (0, 1), (1, 0), (0, 1)),
    ((0, 1), (1, 0), (0, 1), (1, 0)),
    ((1, 0), (1, 0), (0, 1), (0, 1)),
)

# Frozen byte-delta witnesses independently pinned from the Cycle 719 fixture.
FROZEN_ATTEMPT5_DELTA_FROM_EXHAUSTED = (1, 6, 40, 123, 124, 131)
FROZEN_ATTEMPT5_DELTA_FROM_PREPARED = (123, 124, 131)
FROZEN_EXHAUSTED_SHA256 = (
    "262d1441d82af10723b8b17b13c16a823af6457a92a313da5dea9dcfd8ab74a1"
)
FROZEN_ATTEMPT5_SHA256 = (
    "7cfc03282a47a0fd8b03c2334b8fcbbea1e8cec70a8d670acd202f9360021d1f"
)


def digest_bits(bits: tuple[int, ...]) -> str:
    return sha256(bytes(bits)).hexdigest()


def function_node(tree: ast.AST, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function census", name, len(matches)))
    return matches[0]


def assignment_value(
    body: list[ast.stmt], name: str
) -> ast.expr:
    matches: list[ast.expr] = []
    for node in body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if any(isinstance(target, ast.Name) and target.id == name for target in targets):
            if node.value is None:
                raise AssertionError(("valueless assignment", name))
            matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError(("assignment census", name, len(matches)))
    return matches[0]


def literal_assignment(tree: ast.Module, name: str) -> object:
    return ast.literal_eval(assignment_value(tree.body, name))


def dict_items(node: ast.Dict) -> dict[str, ast.expr]:
    result: dict[str, ast.expr] = {}
    for key, value in zip(node.keys, node.values):
        if not isinstance(key, ast.Constant) or not isinstance(key.value, str):
            continue
        result[key.value] = value
    return result


def local_dict(function: ast.FunctionDef, name: str) -> dict[str, ast.expr]:
    value = assignment_value(function.body, name)
    if not isinstance(value, ast.Dict):
        raise AssertionError(("not a dict", name))
    return dict_items(value)


def subscript_name_key(node: ast.AST, base: str, key: str) -> bool:
    return (
        isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
        and node.value.id == base
        and isinstance(node.slice, ast.Constant)
        and node.slice.value == key
    )


def compared_literal(
    function: ast.FunctionDef, base: str, key: str
) -> object:
    found: list[object] = []
    for node in ast.walk(function):
        if not isinstance(node, ast.Compare) or len(node.ops) != 1:
            continue
        if not isinstance(node.ops[0], (ast.Eq, ast.Is)):
            continue
        if subscript_name_key(node.left, base, key):
            try:
                found.append(ast.literal_eval(node.comparators[0]))
            except (ValueError, TypeError):
                pass
    if len(found) != 1:
        raise AssertionError(("literal comparison", base, key, found))
    return found[0]


def extraction(source: str, tree: ast.Module) -> dict[str, object]:
    audit_paths = literal_assignment(tree, "AUDIT_INPUT_PATHS")
    directions = literal_assignment(tree, "GENERATION_DIRECTIONS")
    fixture_banks = literal_assignment(tree, "FIXTURE_BANKS")
    archive_slots = literal_assignment(tree, "ARCHIVE_SLOTS")
    main_node = function_node(tree, "main")
    boundary = local_dict(main_node, "boundary")
    exact_supplies = ast.literal_eval(
        assignment_value(main_node.body, "exact_supplies")
    )
    dirty_transients = compared_literal(
        main_node, "fifth", "postimage_issues"
    )

    renewal_node = function_node(tree, "renewal_word")
    renewal_text = ast.unparse(renewal_node)
    continuation_node = function_node(tree, "continuation_certificate")
    continuation_assignment = assignment_value(
        continuation_node.body, "continuation_rows"
    )
    if not isinstance(continuation_assignment, ast.Tuple):
        raise AssertionError("continuation_rows is not a literal tuple expression")

    required_boundary = {
        "w4_renewal_achieved",
        "renewal_generations_verified",
        "archive_register_supplied",
        "archive_register_count",
        "archive_capacity_generations",
        "fresh_supplied_blank_inventory_per_renewal",
        "fourth_renewal_or_unbounded_capacity_claimed",
        "scope",
    }
    renewal_shape = (
        "shift_oldest = swap_register_word(" in renewal_text
        and "ARCHIVE_SLOT_WIRES[1], ARCHIVE_SLOT_WIRES[2]" in renewal_text
        and "shift_newer = swap_register_word(" in renewal_text
        and "ARCHIVE_SLOT_WIRES[0], ARCHIVE_SLOT_WIRES[1]" in renewal_text
        and "deposit = swap_register_word(" in renewal_text
        and "RECORD_WIRES, ARCHIVE_SLOT_WIRES[0]" in renewal_text
        and "restore = tuple((K.A.x(wire) for wire in GENESIS_ONE_WIRES))"
        in renewal_text
        and "return shift_oldest + shift_newer + deposit + restore"
        in renewal_text
    )
    expected_dirty = (
        "source_pointer",
        "bank_0.POINTER",
        "bank_0.U_TO_V",
        "bank_0.DIRECTION_OK",
    )
    boundary_literals = {
        key: ast.literal_eval(boundary[key])
        for key in (
            "w4_renewal_achieved",
            "archive_register_supplied",
            "archive_register_count",
            "fresh_supplied_blank_inventory_per_renewal",
            "fourth_renewal_or_unbounded_capacity_claimed",
        )
    }
    archive_supply_declared = any(
        "one initially blank finite 909-M2 archive register" in row
        for row in exact_supplies
    )
    generation_census = tuple(len(row) for row in directions)
    passed = all(
        (
            isinstance(audit_paths, tuple)
            and len(audit_paths) == 2
            and all(isinstance(path, str) for path in audit_paths),
            fixture_banks == 2,
            K.A.BANK_CELLS == 2,
            fixture_banks * K.A.BANK_CELLS == 4,
            generation_census == (4, 4, 4),
            len(directions) == 3,
            len(continuation_assignment.elts) == 3,
            dirty_transients == expected_dirty,
            renewal_shape,
            RECORD_WIDTH == 303,
            ARCHIVE_WIDTH == 909,
            archive_slots == 3,
            archive_supply_declared,
            required_boundary <= set(boundary),
            boundary_literals["w4_renewal_achieved"] is True,
            boundary_literals["archive_register_supplied"] is True,
            boundary_literals["archive_register_count"] == 1,
            boundary_literals[
                "fresh_supplied_blank_inventory_per_renewal"
            ]
            is False,
            boundary_literals[
                "fourth_renewal_or_unbounded_capacity_claimed"
            ]
            is False,
            '"true_exhaustion_horizon_orbits"' in source,
            '"second_orbit"' in source,
            '"fifth_attempt"' in source,
        )
    )
    return {
        "pass": passed,
        "primary_AUDIT_INPUT_PATHS_literal": audit_paths,
        "exhaustion": {
            "orbit_2_lawful_nonclobbering_spec_found": (
                '"second_orbit"' in source
                and '"content_clobbering"' in source
                and "not exhaustion[\"second_orbit\"][\"content_clobbering\"]"
                in source
            ),
            "capacity_packets": fixture_banks * K.A.BANK_CELLS,
            "attempt_5_dirty_transients": dirty_transients,
        },
        "renewal_word": {
            "ast_shape_exact": renewal_shape,
            "semantic_gates": 9 * RECORD_WIDTH + 18,
            "CNOT": 9 * RECORD_WIDTH,
            "X": 18,
        },
        "archive_supply_M2": ARCHIVE_WIDTH,
        "generation_census": {
            "fill_orbits": generation_census,
            "renewals": len(directions),
            "continuations": len(continuation_assignment.elts),
        },
        "boundary_literals": boundary_literals,
    }


def gate_parts(gate: object) -> tuple[str, tuple[int, ...]]:
    if isinstance(gate, tuple) and gate and isinstance(gate[0], str):
        return gate[0], tuple(int(wire) for wire in gate[1:])
    return str(gate.kind), tuple(int(wire) for wire in gate.wires)


def apply_word(
    bits: tuple[int, ...], word: tuple[object, ...]
) -> tuple[int, ...]:
    output = list(bits)
    for gate in word:
        kind, wires = gate_parts(gate)
        if kind == "X" and len(wires) == 1:
            output[wires[0]] ^= 1
        elif kind == "CNOT" and len(wires) == 2:
            output[wires[1]] ^= output[wires[0]]
        elif kind == "TOF" and len(wires) == 3:
            output[wires[2]] ^= output[wires[0]] & output[wires[1]]
        else:
            raise AssertionError(("unsupported semantic gate", kind, wires))
    return tuple(output)


def simulate_orbit(
    data: tuple[int, ...],
    program: tuple[object, ...],
    *,
    reverse: bool = False,
) -> tuple[
    tuple[int, ...],
    tuple[int, ...],
    tuple[int, ...],
    tuple[tuple[tuple[int, ...], tuple[int, ...], int], ...],
]:
    stations = len(program)
    a = [1] + [0] * (stations - 1)
    b = [0] * stations
    output = data
    trace = []
    for _step in range(stations):
        live_before = tuple(index for index, bit in enumerate(a) if bit)
        if not reverse:
            for station in range(stations):
                if a[station]:
                    output = apply_word(
                        output, tuple(K.mapped_macro(program[station]))
                    )
            for station in range(stations):
                a[station], b[station] = b[station], a[station]
            for station in range(stations):
                target = (station + 1) % stations
                b[station], a[target] = a[target], b[station]
        else:
            for station in reversed(range(stations)):
                target = (station + 1) % stations
                b[station], a[target] = a[target], b[station]
            for station in reversed(range(stations)):
                a[station], b[station] = b[station], a[station]
            for station in reversed(range(stations)):
                if a[station]:
                    output = apply_word(
                        output,
                        tuple(reversed(K.mapped_macro(program[station]))),
                    )
        live_after = tuple(index for index, bit in enumerate(a) if bit)
        trace.append((live_before, live_after, sum(b)))
    return output, tuple(a), tuple(b), tuple(trace)


def genesis_state() -> tuple[int, ...]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    return K.M.pack_state(banks, links)


def record_image(data: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(data[wire] for wire in RECORD_WIRES)


def payloads(
    banks: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(bank[wire] for wire in K.A.cell(cell)["payload"])
        for bank in banks
        for cell in range(K.A.BANK_CELLS)
    )


def transient_issues(
    data: tuple[int, ...],
    banks: tuple[tuple[int, ...], ...],
    links: tuple[tuple[int, ...], ...],
) -> tuple[str, ...]:
    issues: list[str] = []
    if data[K.R3.X.SOURCE_POINTER]:
        issues.append("source_pointer")
    named = (
        ("POINTER", (K.A.POINTER,)),
        ("U_TO_V", (K.A.U_TO_V,)),
        ("V_TO_U", (K.A.V_TO_U,)),
        ("DIRECTION_OK", (K.A.DIRECTION_OK,)),
        ("FRESH", K.A.FRESH),
        ("ZERO_WORK", K.A.ZERO_WORK),
        ("TOKEN_OK", (K.A.TOKEN_OK,)),
    )
    for bank_index, bank in enumerate(banks):
        for name, wires in named:
            if any(bank[wire] for wire in wires):
                issues.append(f"bank_{bank_index}.{name}")
    for link_index, link in enumerate(links):
        if any(link):
            issues.append(f"link_{link_index}")
    return tuple(issues)


def controller_word(program: tuple[object, ...]) -> tuple[object, ...]:
    return tuple(
        gate
        for row in program
        for gate in K.mapped_macro(row)
    )


def evaluate_orbit(
    state: tuple[int, ...],
    direction: tuple[int, int],
    event: int,
    coarse: object,
) -> tuple[tuple[int, ...], dict[str, object]]:
    program = K.interleaved_program(FIXTURE_BANKS)
    prepared = K.M.prepare_endpoint(state, direction)
    before_banks, _ = K.M.unpack_state(prepared, FIXTURE_BANKS)
    before_payloads = payloads(before_banks)
    occupied_before = tuple(
        K.A.packet_projection(bank, cell) is not None
        for bank in before_banks
        for cell in range(K.A.BANK_CELLS)
    )
    packet_count_before = K.B.packet_count(before_banks)

    after, a, b, trace = simulate_orbit(prepared, program)
    restored, inverse_a, inverse_b, _ = simulate_orbit(
        after, program, reverse=True
    )
    banks, links = K.M.unpack_state(after, FIXTURE_BANKS)
    after_payloads = payloads(banks)
    decode_ok = False
    chain_exact = False
    try:
        decoded, _order = K.B.decode_local_graph(banks, links)
        status = coarse.admit(
            tick_id=event,
            orientation=1 if direction == (1, 0) else -1,
            certificate=1,
            binder=1,
            actuality=1,
            admissibility=1,
            law_domain=1,
        )
        decode_ok = True
        chain_exact = (
            status == "admitted"
            and K.B.cell_rows(decoded) == K.B.cell_rows(coarse)
        )
    except ValueError:
        pass

    expected_allocator = apply_word(
        prepared, tuple(K.M.global_allocator_word(FIXTURE_BANKS))
    )
    expected_program = apply_word(prepared, controller_word(program))
    invariants = {
        "allocator_word_exact": after == expected_allocator,
        "program_word_exact": after == expected_program,
        "literal_reverse_exact": restored == prepared,
        "inverse_rails_exact": inverse_a == a and inverse_b == b,
        "A0_return": a == (1,) + (0,) * (len(program) - 1),
        "B_return": not any(b),
        "token_trace_one_hot": all(
            len(before_live) == 1
            and len(after_live) == 1
            and b_count == 0
            for before_live, after_live, b_count in trace
        ),
        "postimage_clean": not transient_issues(after, banks, links),
        "decode_and_chain_exact": decode_ok and chain_exact,
        "packet_count_increment": (
            K.B.packet_count(banks) == packet_count_before + 1
        ),
        "prior_payloads_preserved": all(
            not occupied or left == right
            for occupied, left, right in zip(
                occupied_before, before_payloads, after_payloads
            )
        ),
    }
    return after, {
        "all_invariants": all(invariants.values()),
        "invariants": invariants,
        "packet_count_before": packet_count_before,
        "packet_count_after": K.B.packet_count(banks),
        "prepared": prepared,
    }


def fill_generation(
    initial: tuple[int, ...],
    directions: tuple[tuple[int, int], ...],
) -> tuple[tuple[int, ...], tuple[dict[str, object], ...]]:
    state = initial
    coarse = K.B.C704.C610.EventChain(bank=CAPACITY_ORBITS)
    rows = []
    for event, direction in enumerate(directions):
        state, row = evaluate_orbit(state, direction, event, coarse)
        rows.append(row)
    return state, tuple(rows)


def byte_delta(
    before: tuple[int, ...], after: tuple[int, ...]
) -> bytes:
    return bytes(left ^ right for left, right in zip(before, after))


def expected_delta_bytes(changed: tuple[int, ...]) -> bytes:
    changed_set = set(changed)
    return bytes(int(wire in changed_set) for wire in range(DATA_WIDTH))


def exhaustion_recount(
    extracted: dict[str, object],
) -> dict[str, object]:
    state = genesis_state()
    orbit_states = []
    rows = []
    coarse = K.B.C704.C610.EventChain(bank=CAPACITY_ORBITS)
    for event, direction in enumerate(GENERATION_DIRECTIONS[0]):
        state, row = evaluate_orbit(state, direction, event, coarse)
        orbit_states.append(state)
        rows.append(row)

    first_banks, _ = K.M.unpack_state(orbit_states[0], FIXTURE_BANKS)
    second_banks, _ = K.M.unpack_state(orbit_states[1], FIXTURE_BANKS)
    first_occupied = tuple(
        K.A.packet_projection(bank, cell) is not None
        for bank in first_banks
        for cell in range(K.A.BANK_CELLS)
    )
    orbit2_payload_equal = all(
        not occupied or left == right
        for occupied, left, right in zip(
            first_occupied, payloads(first_banks), payloads(second_banks)
        )
    )

    exhausted = orbit_states[-1]
    exhausted_banks, _ = K.M.unpack_state(exhausted, FIXTURE_BANKS)
    prepared = K.M.prepare_endpoint(exhausted, (1, 0))
    prepared_banks, _ = K.M.unpack_state(prepared, FIXTURE_BANKS)
    fifth, a, b, _ = simulate_orbit(
        prepared, K.interleaved_program(FIXTURE_BANKS)
    )
    fifth_banks, fifth_links = K.M.unpack_state(fifth, FIXTURE_BANKS)
    restored, inverse_a, inverse_b, _ = simulate_orbit(
        fifth, K.interleaved_program(FIXTURE_BANKS), reverse=True
    )
    decode_ok = True
    try:
        K.B.decode_local_graph(fifth_banks, fifth_links)
    except ValueError:
        decode_ok = False
    expected_issues = tuple(
        extracted["exhaustion"]["attempt_5_dirty_transients"]
    )
    full_delta_exact = (
        byte_delta(exhausted, fifth)
        == expected_delta_bytes(FROZEN_ATTEMPT5_DELTA_FROM_EXHAUSTED)
    )
    prepared_delta_exact = (
        byte_delta(prepared, fifth)
        == expected_delta_bytes(FROZEN_ATTEMPT5_DELTA_FROM_PREPARED)
    )
    fifth_issues = transient_issues(fifth, fifth_banks, fifth_links)
    payload_byte_equal = (
        bytes().join(map(bytes, payloads(exhausted_banks)))
        == bytes().join(map(bytes, payloads(fifth_banks)))
    )
    program = K.interleaved_program(FIXTURE_BANKS)
    passed = all(
        (
            rows[1]["all_invariants"],
            orbit2_payload_equal,
            all(row["all_invariants"] for row in rows),
            len(rows) == CAPACITY_ORBITS,
            K.B.packet_count(exhausted_banks) == CAPACITY_ORBITS,
            K.B.packet_count(fifth_banks) == CAPACITY_ORBITS,
            payload_byte_equal,
            payloads(exhausted_banks) == payloads(fifth_banks),
            not decode_ok,
            fifth_issues == expected_issues,
            a == (1,) + (0,) * (len(program) - 1),
            not any(b),
            restored == prepared,
            inverse_a == a,
            inverse_b == b,
            full_delta_exact,
            prepared_delta_exact,
            digest_bits(exhausted) == FROZEN_EXHAUSTED_SHA256,
            digest_bits(fifth) == FROZEN_ATTEMPT5_SHA256,
            K.B.source_bank(prepared_banks) in range(FIXTURE_BANKS),
            K.A.declared_append_domain(
                prepared_banks[K.B.source_bank(prepared_banks)]
            )[1]
            == "selected_cell_not_blank",
        )
    )
    return {
        "pass": passed,
        "orbit_2": {
            "lawful": rows[1]["all_invariants"],
            "prior_payload_byte_equal": orbit2_payload_equal,
            "content_clobbering": not orbit2_payload_equal,
        },
        "capacity_packets": K.B.packet_count(exhausted_banks),
        "lawful_orbits": sum(bool(row["all_invariants"]) for row in rows),
        "attempt_5": {
            "lawful": False,
            "packet_count": K.B.packet_count(fifth_banks),
            "payload_byte_equal": payload_byte_equal,
            "dirty_transients": fifth_issues,
            "delta_from_exhausted_byte_exact": full_delta_exact,
            "delta_from_prepared_byte_exact": prepared_delta_exact,
            "state_sha256_exact": digest_bits(fifth)
            == FROZEN_ATTEMPT5_SHA256,
            "literal_reverse_exact": restored == prepared,
        },
    }


def swap_word(
    left_wires: tuple[int, ...],
    right_wires: tuple[int, ...],
) -> tuple[tuple[object, ...], ...]:
    return tuple(
        gate
        for left, right in zip(left_wires, right_wires)
        for gate in (
            ("CNOT", left, right),
            ("CNOT", right, left),
            ("CNOT", left, right),
        )
    )


def independent_renewal_word(
    genesis: tuple[int, ...],
) -> tuple[tuple[object, ...], ...]:
    genesis_one_wires = tuple(
        wire for wire in RECORD_WIRES if genesis[wire]
    )
    return (
        swap_word(ARCHIVE_SLOT_WIRES[1], ARCHIVE_SLOT_WIRES[2])
        + swap_word(ARCHIVE_SLOT_WIRES[0], ARCHIVE_SLOT_WIRES[1])
        + swap_word(RECORD_WIRES, ARCHIVE_SLOT_WIRES[0])
        + tuple(("X", wire) for wire in genesis_one_wires)
    )


def pack_combined(
    data: tuple[int, ...],
    archives: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    return data + tuple(bit for archive in archives for bit in archive)


def split_combined(
    combined: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[tuple[int, ...], ...]]:
    data = combined[:DATA_WIDTH]
    archives = tuple(
        combined[
            DATA_WIDTH + slot * RECORD_WIDTH:
            DATA_WIDTH + (slot + 1) * RECORD_WIDTH
        ]
        for slot in range(ARCHIVE_SLOTS)
    )
    return data, archives


def renewal_word_recount(
    extracted: dict[str, object],
) -> dict[str, object]:
    genesis = genesis_state()
    exhausted, rows = fill_generation(
        genesis, GENERATION_DIRECTIONS[0]
    )
    archives_before = (
        record_image(exhausted),
        record_image(exhausted),
        ZERO_ARCHIVE_SLOT,
    )
    before = pack_combined(exhausted, archives_before)
    word = independent_renewal_word(genesis)
    observed = apply_word(before, word)
    data_after, archives_after = split_combined(observed)
    expected_archives = (
        record_image(exhausted),
        archives_before[0],
        archives_before[1],
    )
    restored = apply_word(observed, tuple(reversed(word)))
    census = {
        kind: sum(gate_parts(gate)[0] == kind for gate in word)
        for kind in ("CNOT", "X", "TOF")
    }
    extracted_census = extracted["renewal_word"]
    scratch_returns = len(before) == len(observed) == FULL_WIDTH
    passed = all(
        (
            all(row["all_invariants"] for row in rows),
            len(word) == 2745 == extracted_census["semantic_gates"],
            census == {"CNOT": 2727, "X": 18, "TOF": 0},
            census["CNOT"] == extracted_census["CNOT"],
            census["X"] == extracted_census["X"],
            bytes(data_after) == bytes(genesis),
            all(
                bytes(left) == bytes(right)
                for left, right in zip(archives_after, expected_archives)
            ),
            restored == before,
            scratch_returns,
            all(
                0 <= wire < FULL_WIDTH
                for gate in word
                for wire in gate_parts(gate)[1]
            ),
        )
    )
    return {
        "pass": passed,
        "semantic_gates": len(word),
        "gate_census": census,
        "pre_state_bits": len(before),
        "post_operating_bit_exact": bytes(data_after) == bytes(genesis),
        "post_archive_bit_exact": archives_after == expected_archives,
        "scratch_registers": 0,
        "scratch_returns": scratch_returns,
        "literal_reverse_exact": restored == before,
    }


def generation_recount() -> dict[str, object]:
    genesis = genesis_state()
    word = independent_renewal_word(genesis)
    data = genesis
    archives = (ZERO_ARCHIVE_SLOT,) * ARCHIVE_SLOTS
    archived_images = []
    fill_rows_by_generation = []
    archive_checks = []
    started_genesis = []
    tail_blank = []
    for directions in GENERATION_DIRECTIONS:
        started_genesis.append(data == genesis)
        exhausted, rows = fill_generation(data, directions)
        fill_rows_by_generation.append(rows)
        image = record_image(exhausted)
        before_archives = archives
        tail_blank.append(before_archives[-1] == ZERO_ARCHIVE_SLOT)
        combined = apply_word(
            pack_combined(exhausted, before_archives), word
        )
        data, archives = split_combined(combined)
        expected_archives = (image,) + before_archives[:-1]
        archive_checks.append(
            tuple(
                bytes(observed) == bytes(expected)
                for observed, expected in zip(archives, expected_archives)
            )
        )
        archived_images.append(image)

    final_archives = archives
    continuation_rows = (
        fill_rows_by_generation[1][0],
        fill_rows_by_generation[2][0],
    )
    coarse = K.B.C704.C610.EventChain(bank=CAPACITY_ORBITS)
    continued, final_continuation = evaluate_orbit(
        data, (0, 1), 0, coarse
    )
    continuation_rows += (final_continuation,)
    continued_banks, _ = K.M.unpack_state(continued, FIXTURE_BANKS)
    fill_counts = tuple(len(rows) for rows in fill_rows_by_generation)
    violations = sum(
        not row["all_invariants"]
        for rows in fill_rows_by_generation
        for row in rows
    )
    expected_final = tuple(reversed(archived_images))
    final_archive_matches = tuple(
        bytes(observed) == bytes(expected)
        for observed, expected in zip(final_archives, expected_final)
    )
    passed = all(
        (
            fill_counts == (4, 4, 4),
            violations == 0,
            all(started_genesis),
            all(tail_blank),
            len(archive_checks) == 3,
            all(all(row) for row in archive_checks),
            len(continuation_rows) == 3,
            all(row["all_invariants"] for row in continuation_rows),
            all(final_archive_matches),
            all(slot != ZERO_ARCHIVE_SLOT for slot in final_archives),
            K.B.packet_count(continued_banks) == 1,
            archives == final_archives,
        )
    )
    return {
        "pass": passed,
        "fill_orbit_census": fill_counts,
        "renewal_census": len(archive_checks),
        "continuation_census": len(continuation_rows),
        "orbit_violations": violations,
        "continuation_violations": sum(
            not row["all_invariants"] for row in continuation_rows
        ),
        "data_started_genesis": tuple(started_genesis),
        "archive_byte_matches_by_generation": tuple(archive_checks),
        "tail_blank_before_each_renewal": tuple(tail_blank),
        "final_archive_newest_first": final_archive_matches,
        "archive_full_after_generation_3": all(
            slot != ZERO_ARCHIVE_SLOT for slot in final_archives
        ),
        "fourth_renewal_claimed": False,
    }


def contains_name(node: ast.AST, name: str) -> bool:
    return any(
        isinstance(child, ast.Name) and child.id == name
        for child in ast.walk(node)
    )


def no_fresh_supply_audit(
    tree: ast.Module,
) -> dict[str, object]:
    renewal_node = function_node(tree, "renewal_word")
    continuation_node = function_node(tree, "continuation_certificate")
    branch_count = sum(
        isinstance(node, (ast.If, ast.IfExp, ast.Match, ast.While))
        for node in ast.walk(renewal_node)
    )
    filtered_comprehensions = sum(
        len(generator.ifs)
        for node in ast.walk(renewal_node)
        if isinstance(
            node,
            (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp),
        )
        for generator in node.generators
    )
    parameters = tuple(
        argument.arg
        for argument in (
            renewal_node.args.posonlyargs
            + renewal_node.args.args
            + renewal_node.args.kwonlyargs
        )
    )
    archive_initializers = [
        node
        for node in continuation_node.body
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        and node.value is not None
        and contains_name(node.value, "ZERO_ARCHIVE_SLOT")
        and any(
            isinstance(target, ast.Name) and target.id == "archives"
            for target in (
                node.targets
                if isinstance(node, ast.Assign)
                else [node.target]
            )
        )
    ]
    generation_loops = [
        node
        for node in continuation_node.body
        if isinstance(node, ast.For)
    ]
    per_renewal_zero_archive_assignments = sum(
        isinstance(node, (ast.Assign, ast.AnnAssign))
        and node.value is not None
        and contains_name(node.value, "ZERO_ARCHIVE_SLOT")
        for loop in generation_loops
        for node in ast.walk(loop)
    )

    genesis = genesis_state()
    word = independent_renewal_word(genesis)
    touched = {
        wire for gate in word for wire in gate_parts(gate)[1]
    }
    declared_operating = set(RECORD_WIRES)
    declared_archive = {
        wire for slot in ARCHIVE_SLOT_WIRES for wire in slot
    }
    undeclared = touched - declared_operating - declared_archive
    nonrecord_operating = (
        touched & set(range(DATA_WIDTH))
    ) - declared_operating
    literal_kinds = tuple(
        sorted({gate_parts(gate)[0] for gate in word})
    )
    passed = all(
        (
            not parameters,
            branch_count == 0,
            filtered_comprehensions == 0,
            len(archive_initializers) == 1,
            len(generation_loops) == 1,
            per_renewal_zero_archive_assignments == 0,
            ARCHIVE_WIDTH == 909,
            len(declared_archive) == 909,
            declared_archive <= touched,
            not undeclared,
            not nonrecord_operating,
            literal_kinds == ("CNOT", "X"),
            len(word) == 2745,
        )
    )
    return {
        "pass": passed,
        "declared_initial_supply": (
            "one finite 909-M2 archive register, blank once"
        ),
        "archive_registers": 1,
        "archive_slots": ARCHIVE_SLOTS,
        "archive_M2": ARCHIVE_WIDTH,
        "initializations_before_generation_loop": len(archive_initializers),
        "blank_archive_assignments_per_renewal": (
            per_renewal_zero_archive_assignments
        ),
        "renewal_runtime_parameters": parameters,
        "renewal_branch_nodes": branch_count,
        "filtered_comprehensions": filtered_comprehensions,
        "scratch_registers": 0,
        "undeclared_operand_wires": tuple(sorted(undeclared)),
        "operating_nonrecord_targets": tuple(
            sorted(nonrecord_operating)
        ),
        "literal_gate_kinds": literal_kinds,
    }


def root_name(node: ast.AST) -> str | None:
    while isinstance(node, (ast.Attribute, ast.Subscript)):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def assignment_targets(node: ast.AST) -> tuple[ast.AST, ...]:
    if isinstance(node, ast.Assign):
        return tuple(node.targets)
    if isinstance(node, ast.AnnAssign):
        return (node.target,)
    if isinstance(node, ast.AugAssign):
        return (node.target,)
    if isinstance(node, ast.NamedExpr):
        return (node.target,)
    if isinstance(node, ast.Delete):
        return tuple(node.targets)
    return ()


def discipline(
    source: str,
    tree: ast.Module,
    k_surface_before: tuple[tuple[str, int], ...],
) -> dict[str, object]:
    allowed_module = (
        "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
    )
    frontier_imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            frontier_imports.extend(
                alias.name
                for alias in node.names
                if alias.name.startswith("frontier_cycle7")
            )
        elif (
            isinstance(node, ast.ImportFrom)
            and node.module
            and node.module.startswith("frontier_cycle7")
        ):
            frontier_imports.append(node.module)
    k_writes = [
        (node.lineno, ast.unparse(target))
        for node in ast.walk(tree)
        for target in assignment_targets(node)
        if root_name(target) == "K"
    ]
    mutator_calls = [
        (node.lineno, ast.unparse(node))
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {"setattr", "delattr"}
        and node.args
        and root_name(node.args[0]) == "K"
    ]
    main_node = function_node(tree, "main")
    boundary = local_dict(main_node, "boundary")
    boundary_checks = {
        "w4_true": ast.literal_eval(
            boundary["w4_renewal_achieved"]
        )
        is True,
        "finite_three_slot_archive": (
            isinstance(
                boundary["archive_capacity_generations"], ast.Name
            )
            and boundary["archive_capacity_generations"].id
            == "ARCHIVE_SLOTS"
            and literal_assignment(tree, "ARCHIVE_SLOTS")
            == ARCHIVE_SLOTS
            and "finite" in ast.literal_eval(boundary["scope"])
            and "three-slot" in ast.literal_eval(boundary["scope"])
        ),
        "three_generations": (
            subscript_name_key(
                boundary["renewal_generations_verified"],
                "continuation",
                "renewal_generations_verified",
            )
            and len(literal_assignment(tree, "GENERATION_DIRECTIONS"))
            == 3
            and any(
                isinstance(node, ast.Compare)
                and subscript_name_key(
                    node.left,
                    "continuation",
                    "renewal_generations_verified",
                )
                and len(node.ops) == 1
                and isinstance(node.ops[0], ast.GtE)
                and len(node.comparators) == 1
                and isinstance(node.comparators[0], ast.Constant)
                and node.comparators[0].value == 3
                for node in ast.walk(main_node)
            )
        ),
        "no_unbounded_claim": ast.literal_eval(
            boundary["fourth_renewal_or_unbounded_capacity_claimed"]
        )
        is False,
    }
    k_surface_after = tuple(
        sorted((name, id(value)) for name, value in vars(K).items())
    )
    passed = all(
        (
            tuple(frontier_imports) == (allowed_module,),
            not k_writes,
            not mutator_calls,
            k_surface_after == k_surface_before,
            all(boundary_checks.values()),
            AUDIT_INPUT_PATHS
            == (
                PRIMARY_PATH,
                K_PATH,
            ),
            AUDIT_TIMEOUT_SEC == 900,
            NOTE_PATH
            == "docs/PHYSICAL_BANK_RENEWAL_CYCLE741_BOUNDED_THEOREM_NOTE_2026-07-28.md",
        )
    )
    return {
        "pass": passed,
        "frontier_cycle7_imports_in_primary": tuple(frontier_imports),
        "allowed_frontier_import": allowed_module,
        "blocklisted_import_count": sum(
            name != allowed_module for name in frontier_imports
        ),
        "K_assignment_writes": tuple(k_writes),
        "K_mutator_calls": tuple(mutator_calls),
        "K_surface_unchanged": k_surface_after == k_surface_before,
        "boundary": boundary_checks,
        "scope": "three generations; one finite archive; no unbounded claim",
    }


def main() -> int:
    started = perf_counter()
    k_surface_before = tuple(
        sorted((name, id(value)) for name, value in vars(K).items())
    )
    with open(PRIMARY_PATH, "r", encoding="utf-8") as handle:
        source = handle.read()
    tree = ast.parse(source, filename=PRIMARY_PATH)

    certificates: dict[str, dict[str, object]] = {}
    errors: dict[str, str] = {}

    try:
        certificates["extraction"] = extraction(source, tree)
    except Exception as error:
        errors["extraction"] = f"{type(error).__name__}: {error}"
        certificates["extraction"] = {"pass": False}

    extracted = certificates["extraction"]
    for name, call in (
        ("exhaustion_recount", lambda: exhaustion_recount(extracted)),
        ("renewal_word_recount", lambda: renewal_word_recount(extracted)),
        ("generation_recount", generation_recount),
        ("no_fresh_supply_audit", lambda: no_fresh_supply_audit(tree)),
        (
            "discipline",
            lambda: discipline(source, tree, k_surface_before),
        ),
    ):
        try:
            certificates[name] = call()
        except Exception as error:
            errors[name] = f"{type(error).__name__}: {error}"
            certificates[name] = {"pass": False}

    elapsed = perf_counter() - started
    certificate_order = (
        "extraction",
        "exhaustion_recount",
        "renewal_word_recount",
        "generation_recount",
        "no_fresh_supply_audit",
        "discipline",
    )
    checks = {
        name: bool(certificates[name].get("pass"))
        for name in certificate_order
    }
    checks["runtime_under_timeout"] = elapsed < AUDIT_TIMEOUT_SEC
    passed_count = sum(checks.values())
    total_count = len(checks)
    report = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "certificates": certificates,
        "checks": checks,
        "checks_passed": passed_count,
        "checks_total": total_count,
        "errors": errors,
        "pass": all(checks.values()),
        "runtime_seconds": round(elapsed, 6),
        "terminal": (
            "CYCLE741_RENEWAL_INDEPENDENT_CHECK_PASS"
            if all(checks.values())
            else "CYCLE741_RENEWAL_INDEPENDENT_CHECK_HONEST_FAIL"
        ),
    }
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    lines = [
        f"{'PASS' if value else 'FAIL'} {name} :: {value}"
        for name, value in checks.items()
    ]
    lines.append(
        json.dumps(report, sort_keys=True, separators=(",", ":"), default=str)
    )
    output = "\n".join(lines) + "\n"
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(
            "FAIL stdout_under_150KB :: False\n"
            + json.dumps(
                {
                    "pass": False,
                    "reason": "stdout bound exceeded",
                    "bytes": len(output.encode()),
                    "terminal": (
                        "CYCLE741_RENEWAL_INDEPENDENT_CHECK_HONEST_FAIL"
                    ),
                },
                sort_keys=True,
            )
            + "\n"
        )
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
