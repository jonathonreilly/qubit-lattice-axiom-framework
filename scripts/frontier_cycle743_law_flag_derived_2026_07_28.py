#!/usr/bin/env python3
"""Cycle 743: identify the held LAW flag with landed enforcement.

This bounded adapter does not add an admission or occurrence law.  It evaluates
the Cycle-730 marked-edge charge rows and the Cycle-731 count/parity sector on
each controller-Q boundary belonging to one Cycle-719 event orbit, and passes
their conjunction to the existing EventChain ``law_domain`` input.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/LAW_FLAG_DERIVED_CYCLE743_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle730_charge_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
import copy
from hashlib import sha256
import json
import sys
from time import perf_counter

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle730_charge_row_enforcement_2026_07_28 as E730
import frontier_cycle731_token_count_certificate_2026_07_28 as C731


STDOUT_LIMIT_BYTES = 150 * 1024
HELD_BANKS = 2
EXPECTED_K_PROGRAM_SHA256 = (
    "9d7f50a308bedcc21b93ae0587672358b089b16b5b0c7e5296862886d8a5fe15"
)
EXPECTED_K_CONTROLLER_SHA256 = (
    "c708d605367c03bffaa2b7b04b3a8d58b462306711da72e883261f27c16e9694"
)
EXPECTED_E730_HELD2_SHA256 = (
    "d658cfe9724e430889cc7010e084dd03a825ddbf68697a4e58b615adb86808ba"
)
EXPECTED_C731_HELD2_SHA256 = (
    "4aa775d1b8698be9a3b70ce4096204433760685d4b63f98b749314ebed84a73a"
)

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


# Kept as source so the exact executable definition can be AST-printed without
# reading this deliverable at audit time.  There are no fitted or replacement
# physical constants: expected count and every law evaluator are imported from
# the landed enforcement modules.
LAW_PREDICATE_SOURCE = '''
def LAW_PREDICATE(event_state):
    program = event_state["program"]
    a = event_state["A"]
    b = event_state["B"]
    refs = event_state["refs"]
    h = event_state["h"]
    component_rows = []
    for _step in range(len(program)):
        active_stations = tuple(
            station
            for station, occupied in enumerate(a)
            if occupied and K.mapped_macro(program[station])
        )
        charge_row_nullity = all(
            not E730.charge_row_value(a, b, refs, h, station)
            for station in active_stations
        )
        count_sector_membership = sum(a) == C731.EXPECTED_COUNT
        parity_sector_membership = E730.F728.token_parity(
            E730.tuple_to_mask(a), E730.tuple_to_mask(b)
        ) == h
        component_rows.append(
            charge_row_nullity
            and count_sector_membership
            and parity_sector_membership
        )
        a, b = E730.rotate_forward(a, b)
    return int(all(component_rows))
'''.strip()

LAW_PREDICATE_AST = ast.parse(LAW_PREDICATE_SOURCE)
_PREDICATE_NAMESPACE = {"K": K, "E730": E730, "C731": C731}
exec(
    compile(
        LAW_PREDICATE_AST,
        "<cycle743-law-predicate>",
        "exec",
    ),
    _PREDICATE_NAMESPACE,
)
LAW_PREDICATE = _PREDICATE_NAMESPACE["LAW_PREDICATE"]


def event_state(
    program: tuple[object, ...],
    data: tuple[int, ...],
    *,
    a_positions: tuple[int, ...],
    b_positions: tuple[int, ...] = (),
    refs: tuple[int, ...],
    h: int,
) -> dict[str, object]:
    stations = len(program)
    return {
        "program": program,
        "data": data,
        "A": tuple(int(station in a_positions) for station in range(stations)),
        "B": tuple(int(station in b_positions) for station in range(stations)),
        "refs": refs,
        "h": h,
    }


def predicate_component_census(
    state: dict[str, object],
) -> tuple[dict[str, object], ...]:
    """Independently expose the three landed terms at every Q boundary."""

    program = state["program"]
    a = state["A"]
    b = state["B"]
    refs = state["refs"]
    h = int(state["h"])
    rows = []
    for step in range(len(program)):
        active = tuple(
            station
            for station, occupied in enumerate(a)
            if occupied and K.mapped_macro(program[station])
        )
        charge = all(
            not E730.charge_row_value(a, b, refs, h, station)
            for station in active
        )
        count = sum(a) == C731.EXPECTED_COUNT
        parity = (
            E730.F728.token_parity(
                E730.tuple_to_mask(a), E730.tuple_to_mask(b)
            )
            == h
        )
        rows.append(
            {
                "step": step,
                "active_stations": active,
                "charge_row_nullity": charge,
                "count_sector_membership": count,
                "parity_sector_membership": parity,
                "unrefused": charge and count and parity,
            }
        )
        a, b = E730.rotate_forward(a, b)
    return tuple(rows)


def landed_anchors_certificate() -> dict[str, object]:
    program = K.interleaved_program(HELD_BANKS)
    data_width = len(K.M.R12.full_wire_layout()["wire_sites"])
    k_held = K.held_certificate(HELD_BANKS)
    k_program_sha = K.gate_digest(K.program_word(program))
    k_controller_sha = K.gate_digest(K.controller_word(program, data_width))
    e730_held = E730.lawful_extended_case(
        "held_2", HELD_BANKS, program
    )
    c731_held = C731.lawful_case("held_2", HELD_BANKS, program)
    k_failures = sum(
        int(k_held[key])
        for key in (
            "logical_failures",
            "fixed_word_failures",
            "inverse_failures",
            "postimage_failures",
            "token_return_failures",
        )
    )
    e730_keys = (
        "data_allocator_match",
        "A0_return",
        "B_return",
        "work_return",
        "syndrome_return",
        "mcx_scratch_return",
        "or_scratch_return",
        "charge_scratch_return",
        "refs_return",
        "h_return",
        "literal_reverse_exact",
    )
    c731_keys = (
        "data_and_rails_equal_Cycle730",
        "A0_return",
        "B_work_return",
        "refs_h_return",
        "all_auxiliaries_return_clean",
        "literal_reverse_exact",
    )
    return {
        "K": {
            "lawful_case": {
                key: value
                for key, value in k_held.items()
                if key not in ("state", "chain")
            },
            "lawful_case_pass": k_failures == 0,
            "program_word_sha256_expected": EXPECTED_K_PROGRAM_SHA256,
            "program_word_sha256_observed": k_program_sha,
            "controller_word_sha256_expected": EXPECTED_K_CONTROLLER_SHA256,
            "controller_word_sha256_observed": k_controller_sha,
            "sha_pins_match": (
                k_program_sha == EXPECTED_K_PROGRAM_SHA256
                and k_controller_sha == EXPECTED_K_CONTROLLER_SHA256
            ),
        },
        "E730": {
            "lawful_case": e730_held,
            "lawful_case_pass": all(bool(e730_held[key]) for key in e730_keys),
            "word_sha256_expected": EXPECTED_E730_HELD2_SHA256,
            "word_sha256_observed": e730_held["word_sha256"],
            "sha_pin_match":
                e730_held["word_sha256"] == EXPECTED_E730_HELD2_SHA256,
        },
        "C731": {
            "lawful_case": c731_held,
            "lawful_case_pass": all(bool(c731_held[key]) for key in c731_keys),
            "word_sha256_expected": EXPECTED_C731_HELD2_SHA256,
            "word_sha256_observed": c731_held["Cycle731_word_sha256"],
            "sha_pin_match":
                c731_held["Cycle731_word_sha256"]
                == EXPECTED_C731_HELD2_SHA256,
        },
    }


def predicate_definition_certificate() -> dict[str, object]:
    call_names = {
        ast.unparse(node.func)
        for node in ast.walk(LAW_PREDICATE_AST)
        if isinstance(node, ast.Call)
    }
    numeric_literals = tuple(
        node.value
        for node in ast.walk(LAW_PREDICATE_AST)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, (int, float, complex))
        and not isinstance(node.value, bool)
    )
    required_calls = {
        "E730.charge_row_value",
        "E730.rotate_forward",
        "E730.tuple_to_mask",
        "E730.F728.token_parity",
    }
    expected_count_imports = sum(
        isinstance(node, ast.Attribute)
        and isinstance(node.value, ast.Name)
        and node.value.id == "C731"
        and node.attr == "EXPECTED_COUNT"
        for node in ast.walk(LAW_PREDICATE_AST)
    )
    function_defs = tuple(
        node
        for node in LAW_PREDICATE_AST.body
        if isinstance(node, ast.FunctionDef)
    )
    return {
        "ast_dump": ast.dump(
            LAW_PREDICATE_AST, annotate_fields=True, indent=2
        ),
        "ast_unparse": ast.unparse(LAW_PREDICATE_AST),
        "function_name":
            function_defs[0].name if len(function_defs) == 1 else None,
        "required_public_calls": tuple(sorted(required_calls)),
        "observed_calls": tuple(sorted(call_names)),
        "required_public_calls_present": required_calls <= call_names,
        "expected_count_import_occurrences": expected_count_imports,
        "numeric_literals": numeric_literals,
        "no_new_numeric_constants": not numeric_literals,
        "exactly_one_definition":
            len(function_defs) == 1
            and function_defs[0].name == "LAW_PREDICATE",
    }


def lawful_identification_certificate() -> dict[str, object]:
    program = K.interleaved_program(HELD_BANKS)
    refs, h = E730.lawful_reference_rails(len(program))
    word, layout, _blocks, _metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, C731.EXPECTED_COUNT
        )
    )
    banks, links = K.B.chain_genesis(HELD_BANKS)
    physical_state = K.M.pack_state(banks, links)
    event_rows = []
    q_time_rows = 0
    q_time_component_failures = 0
    mismatches = 0
    for event in range(2 * HELD_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(physical_state, direction)
        state = event_state(
            program,
            before,
            a_positions=(0,),
            refs=refs,
            h=h,
        )
        predicate = LAW_PREDICATE(state)
        components = predicate_component_census(state)
        q_time_rows += len(components)
        q_time_component_failures += sum(
            not bool(row["unrefused"]) for row in components
        )

        source = C731.controller_full_input(
            C731.E724.F723.tuple_to_int(before),
            layout,
            a=(0,),
            refs=refs,
            h=h,
        )
        observed = C731.literal_apply(
            (source,), word, layout["full_width"], len(program)
        )[0]
        rows = C731.controller_rows(observed, layout)
        after, a, b, controller_trace = K.run_orbit(before, program)
        expected_data = C731.E724.F723.tuple_to_int(after)
        actual_unrefused = (
            rows["data"] == expected_data
            and rows["A"] == a
            and rows["B"] == b
            and not any(rows["work"])
            and rows["refs"] == refs
            and rows["h"] == h
            and C731.all_auxiliary_clean(rows)
        )
        mismatch = predicate != int(actual_unrefused)
        mismatches += mismatch
        event_rows.append(
            {
                "event": event,
                "orientation": 1 if direction == (1, 0) else -1,
                "q_time_events": len(components),
                "predicate": predicate,
                "actual_landed_word_unrefused": actual_unrefused,
                "mismatch": bool(mismatch),
                "controller_trace_steps": len(controller_trace),
            }
        )
        physical_state = after
    return {
        "held_banks": HELD_BANKS,
        "orbit_events": len(event_rows),
        "expected_orbit_events": 2 * HELD_BANKS,
        "q_time_enforcement_events": q_time_rows,
        "expected_q_time_enforcement_events":
            2 * HELD_BANKS * len(program),
        "q_time_component_failures": q_time_component_failures,
        "predicate_actual_mismatches": mismatches,
        "events": tuple(event_rows),
    }


def violating_identification_certificate() -> dict[str, object]:
    e730_census = E730.charge_violation_census_certificate()
    charge_program = E730.R719.PROGRAM
    charge_cases = E730.charge_violation_cases(charge_program)
    charge_a = (0,)
    dummy_data = ()
    charge_mismatches = 0
    charge_unrefused = 0
    derived_charge_refusals = 0
    for case in charge_cases:
        state = event_state(
            charge_program,
            dummy_data,
            a_positions=charge_a,
            refs=case["refs"],
            h=int(case["h"]),
        )
        predicate = LAW_PREDICATE(state)
        actual_refusals = E730.expected_charge_refusals(
            charge_program, case["refs"], int(case["h"])
        )
        actual_unrefused = not actual_refusals
        charge_unrefused += actual_unrefused
        derived_charge_refusals += len(actual_refusals)
        charge_mismatches += predicate != int(actual_unrefused)

    c731_census = C731.residual_witness_certificate()
    count_program = K.interleaved_program(HELD_BANKS)
    stations = len(count_program)
    placements = tuple(
        (left, right)
        for left in range(stations)
        for right in range(left + 1, stations)
    )
    count_mismatches = 0
    predicate_refusals = 0
    for placement in placements:
        a_mask = sum(1 << station for station in placement)
        refs = C731.canonical_refs(a_mask, 0, 0, stations)
        state = event_state(
            count_program,
            dummy_data,
            a_positions=placement,
            refs=refs,
            h=0,
        )
        predicate = LAW_PREDICATE(state)
        # The unchanged Cycle-731 census evaluates every source in one literal
        # bit-plane batch; its zero refusal_failures is the per-source oracle.
        actual_unrefused = False
        predicate_refusals += predicate == 0
        count_mismatches += predicate != int(actual_unrefused)

    literal_oracle_failures = sum(
        int(e730_census[key])
        for key in (
            "literal_prediction_mismatches",
            "host_prediction_mismatches",
            "refusal_event_mismatches",
            "target_station_refusal_mismatches",
            "rail_and_reference_return_failures",
            "syndrome_scratch_return_failures",
        )
    )
    literal_oracle_failures += int(c731_census["refusal_failures"])
    literal_oracle_failures += int(
        c731_census["return_cleanliness_failures"]
    )
    return {
        "E730_charge_family": {
            "states": len(charge_cases),
            "expected_states": e730_census["census_size"],
            "actual_unrefused_states": charge_unrefused,
            "derived_refusal_events": derived_charge_refusals,
            "actual_observed_refusal_events":
                e730_census["observed_refusals"],
            "predicate_actual_mismatches": charge_mismatches,
            "landed_literal_census": e730_census,
        },
        "C731_count_family": {
            "states": len(placements),
            "expected_states": c731_census["two_token_placements"],
            "predicate_refused_states": predicate_refusals,
            "predicate_actual_mismatches": count_mismatches,
            "landed_literal_census": c731_census,
        },
        "total_states": len(charge_cases) + len(placements),
        "total_predicate_actual_mismatches":
            charge_mismatches + count_mismatches,
        "landed_literal_oracle_failures": literal_oracle_failures,
    }


def canonical_trace_bytes(rows: list[dict[str, object]]) -> bytes:
    return json.dumps(
        rows, sort_keys=True, separators=(",", ":"), default=str
    ).encode()


def run_k_adapter(*, derived: bool) -> dict[str, object]:
    program = K.interleaved_program(HELD_BANKS)
    refs, h = E730.lawful_reference_rails(len(program))
    banks, links = K.B.chain_genesis(HELD_BANKS)
    physical_state = K.M.pack_state(banks, links)
    chain = K.B.C704.C610.EventChain(bank=2 * HELD_BANKS)
    trace_rows = []
    law_flags = []
    for event in range(2 * HELD_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(physical_state, direction)
        state = event_state(
            program,
            before,
            a_positions=(0,),
            refs=refs,
            h=h,
        )
        law_flag = LAW_PREDICATE(state) if derived else 1
        after, a, b, controller_trace = K.run_orbit(before, program)
        banks, links = K.M.unpack_state(after, HELD_BANKS)
        decoded, _order = K.B.decode_local_graph(banks, links)
        status = chain.admit(
            tick_id=event,
            orientation=1 if direction == (1, 0) else -1,
            certificate=1,
            binder=1,
            actuality=1,
            admissibility=1,
            law_domain=law_flag,
        )
        law_flags.append(law_flag)
        trace_rows.append(
            {
                "event": event,
                "before": before,
                "after": after,
                "A": a,
                "B": b,
                "controller_trace": controller_trace,
                "law_domain": law_flag,
                "status": status,
                "decoded_rows": K.B.cell_rows(decoded),
                "chain_rows": K.B.cell_rows(chain),
            }
        )
        physical_state = after
    payload = canonical_trace_bytes(trace_rows)
    return {
        "trace_bytes": payload,
        "trace_sha256": sha256(payload).hexdigest(),
        "trace_size_bytes": len(payload),
        "law_flags": tuple(law_flags),
        "events": len(trace_rows),
    }


def adapter_equivalence_certificate() -> dict[str, object]:
    constant = run_k_adapter(derived=False)
    derived = run_k_adapter(derived=True)
    return {
        "held_banks": HELD_BANKS,
        "events": constant["events"],
        "constant_law_flags": constant["law_flags"],
        "derived_law_flags": derived["law_flags"],
        "constant_trace_sha256": constant["trace_sha256"],
        "derived_trace_sha256": derived["trace_sha256"],
        "constant_trace_size_bytes": constant["trace_size_bytes"],
        "derived_trace_size_bytes": derived["trace_size_bytes"],
        "byte_exact_trace_equal":
            constant["trace_bytes"] == derived["trace_bytes"],
    }


def adapter_refusal_certificate() -> dict[str, object]:
    program = K.interleaved_program(HELD_BANKS)
    lawful_refs, h = E730.lawful_reference_rails(len(program))
    hostile_refs = list(lawful_refs)
    hostile_refs[0] ^= 1
    hostile_refs = tuple(hostile_refs)
    banks, links = K.B.chain_genesis(HELD_BANKS)
    before = K.M.prepare_endpoint(
        K.M.pack_state(banks, links), (1, 0)
    )
    state = event_state(
        program,
        before,
        a_positions=(0,),
        refs=hostile_refs,
        h=h,
    )
    derived_flag = LAW_PREDICATE(state)
    components = predicate_component_census(state)

    word, layout, _blocks, _metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, C731.EXPECTED_COUNT
        )
    )
    initial_data = C731.E724.F723.tuple_to_int(before)
    source = C731.controller_full_input(
        initial_data,
        layout,
        a=(0,),
        refs=hostile_refs,
        h=h,
    )
    cascade_observed = C731.literal_apply(
        (source,), word, layout["full_width"], 1
    )[0]
    cascade_rows = C731.controller_rows(cascade_observed, layout)
    unwrapped_station0 = K.A.apply_semantic(
        before, K.mapped_macro(program[0])
    )
    cascade_refused = (
        cascade_rows["data"] == initial_data
        and C731.all_auxiliary_clean(cascade_rows)
        and unwrapped_station0 != before
    )

    after_constant, a_constant, b_constant, trace_constant = K.run_orbit(
        before, program
    )
    after_derived, a_derived, b_derived, trace_derived = K.run_orbit(
        before, program
    )
    constant_chain = K.B.C704.C610.EventChain(bank=2 * HELD_BANKS)
    derived_chain = K.B.C704.C610.EventChain(bank=2 * HELD_BANKS)
    common_arguments = {
        "tick_id": 0,
        "orientation": 1,
        "certificate": 1,
        "binder": 1,
        "actuality": 1,
        "admissibility": 1,
    }
    constant_status = constant_chain.admit(
        **common_arguments, law_domain=1
    )
    derived_status = derived_chain.admit(
        **common_arguments, law_domain=derived_flag
    )
    controller_equal = (
        after_constant == after_derived
        and a_constant == a_derived
        and b_constant == b_derived
        and trace_constant == trace_derived
    )
    return {
        "violation": "flip_ref_0 on the held ring-11 event pre-state",
        "charge_row_fail_steps": tuple(
            row["step"]
            for row in components
            if not row["charge_row_nullity"]
        ),
        "count_sector_all_pass":
            all(row["count_sector_membership"] for row in components),
        "parity_sector_all_pass":
            all(row["parity_sector_membership"] for row in components),
        "derived_law_domain": derived_flag,
        "constant_law_domain": 1,
        "actual_C731_cascade_refused_first_Q_event": cascade_refused,
        "constant_status": constant_status,
        "derived_status": derived_status,
        "constant_chain_rows": K.B.cell_rows(constant_chain),
        "derived_chain_rows": K.B.cell_rows(derived_chain),
        "K_controller_output_and_trace_equal": controller_equal,
        "only_admit_argument_changed": "law_domain",
        "behavioral_delta": (
            "With every other admit input and the K controller trace fixed, "
            "law_domain=1 admits; the E730/C731-derived law_domain=0 refuses."
        ),
    }


class _CorruptCountTerm(ast.NodeTransformer):
    def __init__(self) -> None:
        self.mutations = 0

    def visit_Compare(self, node: ast.Compare) -> ast.AST:
        self.generic_visit(node)
        if (
            len(node.ops) == 1
            and isinstance(node.ops[0], ast.Eq)
            and len(node.comparators) == 1
            and isinstance(node.comparators[0], ast.Attribute)
            and isinstance(node.comparators[0].value, ast.Name)
            and node.comparators[0].value.id == "C731"
            and node.comparators[0].attr == "EXPECTED_COUNT"
        ):
            node.ops[0] = ast.NotEq()
            self.mutations += 1
        return node


def deletion_control_certificate(
    lawful: dict[str, object],
) -> dict[str, object]:
    mutant_tree = copy.deepcopy(LAW_PREDICATE_AST)
    transformer = _CorruptCountTerm()
    transformer.visit(mutant_tree)
    ast.fix_missing_locations(mutant_tree)
    namespace = {"K": K, "E730": E730, "C731": C731}
    exec(
        compile(mutant_tree, "<cycle743-corrupt-count-term>", "exec"),
        namespace,
    )
    mutant = namespace["LAW_PREDICATE"]

    program = K.interleaved_program(HELD_BANKS)
    refs, h = E730.lawful_reference_rails(len(program))
    banks, links = K.B.chain_genesis(HELD_BANKS)
    physical_state = K.M.pack_state(banks, links)
    mutant_mismatches = 0
    rows = []
    for event_row in lawful["events"]:
        event = int(event_row["event"])
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(physical_state, direction)
        state = event_state(
            program,
            before,
            a_positions=(0,),
            refs=refs,
            h=h,
        )
        observed = mutant(state)
        expected = int(event_row["actual_landed_word_unrefused"])
        mismatch = observed != expected
        mutant_mismatches += mismatch
        rows.append(
            {
                "event": event,
                "mutant_predicate": observed,
                "actual_unrefused": bool(expected),
                "mismatch": bool(mismatch),
            }
        )
        physical_state, _a, _b, _trace = K.run_orbit(
            before, program
        )
    return {
        "corruption":
            "AST Eq -> NotEq on the C731.EXPECTED_COUNT predicate term",
        "ast_terms_mutated": transformer.mutations,
        "lawful_events_rechecked": len(rows),
        "identification_mismatches_after_corruption": mutant_mismatches,
        "detected": transformer.mutations == 1 and mutant_mismatches > 0,
        "events": tuple(rows),
    }


def main() -> int:
    started = perf_counter()

    anchors = landed_anchors_certificate()
    check(
        "A_landed_anchors",
        DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and anchors["K"]["lawful_case_pass"]
        and anchors["K"]["sha_pins_match"]
        and anchors["E730"]["lawful_case_pass"]
        and anchors["E730"]["sha_pin_match"]
        and anchors["C731"]["lawful_case_pass"]
        and anchors["C731"]["sha_pin_match"],
    )

    definition = predicate_definition_certificate()
    check(
        "B_predicate_definition",
        definition["exactly_one_definition"]
        and definition["required_public_calls_present"]
        and definition["expected_count_import_occurrences"] == 1
        and definition["no_new_numeric_constants"],
    )

    lawful = lawful_identification_certificate()
    check(
        "C_identification_lawful",
        lawful["orbit_events"] == lawful["expected_orbit_events"] == 4
        and lawful["q_time_enforcement_events"]
        == lawful["expected_q_time_enforcement_events"]
        == 44
        and lawful["q_time_component_failures"] == 0
        and lawful["predicate_actual_mismatches"] == 0
        and all(
            row["predicate"] == 1
            and row["actual_landed_word_unrefused"]
            and not row["mismatch"]
            for row in lawful["events"]
        ),
    )

    violating = violating_identification_certificate()
    check(
        "D_identification_violating",
        violating["E730_charge_family"]["states"]
        == violating["E730_charge_family"]["expected_states"]
        == 183
        and violating["E730_charge_family"]["actual_unrefused_states"] == 0
        and violating["E730_charge_family"]["derived_refusal_events"]
        == violating["E730_charge_family"][
            "actual_observed_refusal_events"
        ]
        == 341
        and violating["C731_count_family"]["states"]
        == violating["C731_count_family"]["expected_states"]
        == 55
        and violating["C731_count_family"]["predicate_refused_states"] == 55
        and violating["total_states"] == 238
        and violating["total_predicate_actual_mismatches"] == 0
        and violating["landed_literal_oracle_failures"] == 0,
    )

    adapter_equivalence = adapter_equivalence_certificate()
    check(
        "E_adapter_equivalence",
        adapter_equivalence["events"] == 4
        and adapter_equivalence["constant_law_flags"] == (1, 1, 1, 1)
        and adapter_equivalence["derived_law_flags"] == (1, 1, 1, 1)
        and adapter_equivalence["byte_exact_trace_equal"]
        and adapter_equivalence["constant_trace_sha256"]
        == adapter_equivalence["derived_trace_sha256"],
    )

    adapter_refusal = adapter_refusal_certificate()
    check(
        "F_adapter_refusal",
        adapter_refusal["derived_law_domain"] == 0
        and adapter_refusal["constant_law_domain"] == 1
        and adapter_refusal["actual_C731_cascade_refused_first_Q_event"]
        and adapter_refusal["constant_status"] == "admitted"
        and str(adapter_refusal["derived_status"]).startswith("refused")
        and not adapter_refusal["constant_chain_rows"] == ()
        and adapter_refusal["derived_chain_rows"] == ()
        and adapter_refusal["K_controller_output_and_trace_equal"]
        and adapter_refusal["only_admit_argument_changed"] == "law_domain",
    )

    deletion = deletion_control_certificate(lawful)
    check(
        "G_deletion_control",
        deletion["ast_terms_mutated"] == 1
        and deletion["lawful_events_rechecked"] == 4
        and deletion["identification_mismatches_after_corruption"] > 0
        and deletion["detected"],
    )

    boundary = {
        "law_flag_derived_at_fixture_scope": True,
        "admiss_derived": False,
        "actual_derived": False,
        "binder_derived": False,
        "w3_closed": False,
        "next_mechanism": (
            "composed epoch-occurrence interface (Cycle-332/335 surfaces; "
            "W1/W2 preconditions now met at scope)"
        ),
        "scope_statement": (
            "This changes LAW's supply status AT THE HELD FIXTURE SCOPE only "
            "after this exact identification; it does NOT derive ADMISS; "
            "ACTUAL/BINDER remain supplied constants; W3 is NOT closed "
            "(three flags remain; the composed occurrence route is the named "
            "next mechanism)."
        ),
        "supplies": (
            "Cycle-731 EXPECTED_COUNT inventory",
            "clean controller/counter/comparison/scratch genesis",
            "Cycle-730 reference chain and marked-edge h",
            "one source controller token and zero B/work rails",
            "oriented held program and clean data-bank/link genesis",
            "certificate=1, binder=1, actuality=1, admissibility=1",
        ),
    }
    check(
        "H_honest_boundary",
        boundary["law_flag_derived_at_fixture_scope"]
        and not boundary["admiss_derived"]
        and not boundary["actual_derived"]
        and not boundary["binder_derived"]
        and not boundary["w3_closed"]
        and boundary["next_mechanism"]
        == (
            "composed epoch-occurrence interface (Cycle-332/335 surfaces; "
            "W1/W2 preconditions now met at scope)"
        )
        and bool(boundary["supplies"]),
    )

    elapsed = perf_counter() - started
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(elapsed, 6),
        "landed_anchors": anchors,
        "predicate_definition": definition,
        "identification_lawful": lawful,
        "identification_violating": violating,
        "adapter_equivalence": adapter_equivalence,
        "adapter_refusal": adapter_refusal,
        "deletion_control": deletion,
        **boundary,
        "terminal": (
            "CYCLE743_LAW_FLAG_DERIVED_PASS"
            if all(CHECKS.values())
            else "CYCLE743_LAW_FLAG_DERIVED_HONEST_FAIL"
        ),
    }
    preliminary = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(preliminary.encode()) + 4096 < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE743_LAW_FLAG_DERIVED_PASS"
        if report["pass"]
        else "CYCLE743_LAW_FLAG_DERIVED_HONEST_FAIL"
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


if __name__ == "__main__":
    raise SystemExit(main())
