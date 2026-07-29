#!/usr/bin/env python3
"""Cycle 743 independent checker: derive and audit LAW without importing 743."""

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/LAW_FLAG_DERIVED_CYCLE743_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle730_charge_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
)

import ast
from hashlib import sha256
import json
import os
import sys
from time import perf_counter

sys.dont_write_bytecode = True

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle730_charge_row_enforcement_2026_07_28 as E730
import frontier_cycle731_token_count_certificate_2026_07_28 as C731


PRIMARY_PATH = (
    "scripts/frontier_cycle743_law_flag_derived_2026_07_28.py"
)
IMPORT_BLOCKLIST = (
    "frontier_cycle743_law_flag_derived_2026_07_28",
)
STDOUT_LIMIT_BYTES = 150 * 1024
SCOPE_STATEMENT_VERBATIM = (
    "This changes LAW's supply status AT THE HELD FIXTURE SCOPE only "
    "after this exact identification; it does NOT derive ADMISS; "
    "ACTUAL/BINDER remain supplied constants; W3 is NOT closed "
    "(three flags remain; the composed occurrence route is the named "
    "next mechanism)."
)
REMAINING_SCOPE_VERBATIM = "three flags remain supplied; w3 open"

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []
WRITE_ATTEMPTS: list[tuple[object, ...]] = []


def _audit_write_attempts(event: str, args: tuple[object, ...]) -> None:
    if event != "open" or len(args) < 3:
        return
    mode = args[1]
    flags = args[2]
    mode_writes = isinstance(mode, str) and any(
        marker in mode for marker in ("w", "a", "x", "+")
    )
    write_mask = (
        os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND
    )
    flag_writes = isinstance(flags, int) and bool(flags & write_mask)
    if mode_writes or flag_writes:
        WRITE_ATTEMPTS.append(tuple(args[:3]))


sys.addaudithook(_audit_write_attempts)


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label}")
    return passed


INDEPENDENT_LAW_SOURCE = '''
def INDEPENDENT_LAW(event_state):
    program = event_state["program"]
    a = event_state["A"]
    b = event_state["B"]
    refs = event_state["refs"]
    h = event_state["h"]
    stations = len(program)
    component_rows = []
    for _step in range(stations):
        active_stations = tuple(
            station
            for station, occupied in enumerate(a)
            if occupied and K.mapped_macro(program[station])
        )
        charge_row_nullity = all(
            (
                a[station]
                ^ b[station]
                ^ refs[station]
                ^ refs[(station + 1) % stations]
                ^ (h if station == 0 else 0)
            ) == 0
            for station in active_stations
        )
        count_sector_membership = sum(a) == C731.EXPECTED_COUNT
        parity_sector_membership = (sum(a) + sum(b)) % 2 == h
        component_rows.append(
            charge_row_nullity
            and count_sector_membership
            and parity_sector_membership
        )
        a = tuple(
            a[(station - 1) % stations] for station in range(stations)
        )
        b = tuple(
            b[(station + 1) % stations] for station in range(stations)
        )
    return int(all(component_rows))
'''.strip()

INDEPENDENT_LAW_AST = ast.parse(INDEPENDENT_LAW_SOURCE)
_LAW_NAMESPACE = {"K": K, "C731": C731}
exec(
    compile(INDEPENDENT_LAW_AST, "<cycle743-independent-law>", "exec"),
    _LAW_NAMESPACE,
)
INDEPENDENT_LAW = _LAW_NAMESPACE["INDEPENDENT_LAW"]


def _read_primary_ast() -> tuple[str, ast.Module]:
    with open(PRIMARY_PATH, "r", encoding="utf-8") as handle:
        source = handle.read()
    return source, ast.parse(source, filename=PRIMARY_PATH)


def _assignment(
    body: list[ast.stmt], name: str
) -> ast.expr:
    for node in body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            )
        ):
            return node.value
    raise AssertionError(("assignment absent", name))


def _function(tree: ast.Module, name: str) -> ast.FunctionDef:
    rows = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(rows) != 1:
        raise AssertionError(("function census", name, len(rows)))
    return rows[0]


def _static_string(node: ast.expr) -> str:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if (
        isinstance(node, ast.Call)
        and not node.args
        and not node.keywords
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "strip"
        and isinstance(node.func.value, ast.Constant)
        and isinstance(node.func.value.value, str)
    ):
        return node.func.value.value.strip()
    raise AssertionError(("not a static string literal", ast.dump(node)))


def _check_conditions(main_node: ast.FunctionDef) -> dict[str, ast.expr]:
    conditions: dict[str, ast.expr] = {}
    for node in ast.walk(main_node):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "check"
            and len(node.args) >= 2
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
        ):
            conditions[node.args[0].value] = node.args[1]
    return conditions


def _compact(node: ast.AST) -> str:
    return "".join(ast.unparse(node).split())


def _return_dict(
    tree: ast.Module, function_name: str
) -> dict[str, ast.expr]:
    function_node = _function(tree, function_name)
    returns = [
        node.value
        for node in ast.walk(function_node)
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    ]
    if len(returns) != 1:
        raise AssertionError(("return dict census", function_name, len(returns)))
    output: dict[str, ast.expr] = {}
    for key, value in zip(returns[0].keys, returns[0].values):
        if (
            isinstance(key, ast.Constant)
            and isinstance(key.value, str)
            and value is not None
        ):
            output[key.value] = value
    return output


def extraction() -> dict[str, object]:
    source, tree = _read_primary_ast()
    audit_node = _assignment(tree.body, "AUDIT_INPUT_PATHS")
    audit_paths = ast.literal_eval(audit_node)
    note_path = ast.literal_eval(_assignment(tree.body, "NOTE_PATH"))
    timeout = ast.literal_eval(_assignment(tree.body, "AUDIT_TIMEOUT_SEC"))
    predicate_source = _static_string(
        _assignment(tree.body, "LAW_PREDICATE_SOURCE")
    )
    predicate_tree = ast.parse(predicate_source)
    predicate_text = _compact(predicate_tree)
    predicate_calls = {
        ast.unparse(node.func)
        for node in ast.walk(predicate_tree)
        if isinstance(node, ast.Call)
    }
    composition_fragments = (
        "charge_row_nullity=all(",
        "notE730.charge_row_value(a,b,refs,h,station)",
        "count_sector_membership=sum(a)==C731.EXPECTED_COUNT",
        "parity_sector_membership=E730.F728.token_parity("
        "E730.tuple_to_mask(a),E730.tuple_to_mask(b))==h",
        "charge_row_nullityandcount_sector_membershipand"
        "parity_sector_membership",
        "a,b=E730.rotate_forward(a,b)",
        "returnint(all(component_rows))",
    )

    main_node = _function(tree, "main")
    conditions = _check_conditions(main_node)
    lawful_condition = _compact(conditions["C_identification_lawful"])
    violating_condition = _compact(
        conditions["D_identification_violating"]
    )
    equivalence_condition = _compact(
        conditions["E_adapter_equivalence"]
    )
    refusal_condition = _compact(conditions["F_adapter_refusal"])

    lawful_fragments = (
        "lawful['orbit_events']==lawful['expected_orbit_events']==4",
        "lawful['q_time_enforcement_events']=="
        "lawful['expected_q_time_enforcement_events']==44",
        "lawful['q_time_component_failures']==0",
        "lawful['predicate_actual_mismatches']==0",
    )
    violating_fragments = (
        "violating['E730_charge_family']['states']=="
        "violating['E730_charge_family']['expected_states']==183",
        "violating['E730_charge_family']['actual_unrefused_states']==0",
        "==341",
        "violating['C731_count_family']['states']=="
        "violating['C731_count_family']['expected_states']==55",
        "violating['C731_count_family']['predicate_refused_states']==55",
        "violating['total_states']==238",
        "violating['total_predicate_actual_mismatches']==0",
        "violating['landed_literal_oracle_failures']==0",
    )
    equivalence_fragments = (
        "adapter_equivalence['events']==4",
        "adapter_equivalence['constant_law_flags']==(1,1,1,1)",
        "adapter_equivalence['derived_law_flags']==(1,1,1,1)",
        "adapter_equivalence['byte_exact_trace_equal']",
    )
    refusal_fragments = (
        "adapter_refusal['derived_law_domain']==0",
        "adapter_refusal['constant_law_domain']==1",
        "adapter_refusal['constant_status']=='admitted'",
        "str(adapter_refusal['derived_status']).startswith('refused')",
        "adapter_refusal['derived_chain_rows']==()",
        "adapter_refusal['K_controller_output_and_trace_equal']",
        "adapter_refusal['only_admit_argument_changed']=='law_domain'",
    )

    refusal_function = _function(tree, "adapter_refusal_certificate")
    common_arguments = ast.literal_eval(
        _assignment(refusal_function.body, "common_arguments")
    )
    admit_calls = [
        node
        for node in ast.walk(refusal_function)
        if isinstance(node, ast.Call)
        and ast.unparse(node.func)
        in ("constant_chain.admit", "derived_chain.admit")
    ]
    admit_law_domains = {
        ast.unparse(call.func): ast.unparse(
            next(keyword.value for keyword in call.keywords
                 if keyword.arg == "law_domain")
        )
        for call in admit_calls
    }
    admit_share_common = all(
        any(
            keyword.arg is None
            and isinstance(keyword.value, ast.Name)
            and keyword.value.id == "common_arguments"
            for keyword in call.keywords
        )
        for call in admit_calls
    )
    refusal_return = _return_dict(tree, "adapter_refusal_certificate")
    behavioral_delta = ast.literal_eval(
        refusal_return["behavioral_delta"]
    )
    only_argument = ast.literal_eval(
        refusal_return["only_admit_argument_changed"]
    )

    boundary_node = _assignment(main_node.body, "boundary")
    boundary = ast.literal_eval(boundary_node)
    boundary_exact = (
        boundary["law_flag_derived_at_fixture_scope"] is True
        and boundary["admiss_derived"] is False
        and boundary["actual_derived"] is False
        and boundary["binder_derived"] is False
        and boundary["w3_closed"] is False
        and boundary["scope_statement"] == SCOPE_STATEMENT_VERBATIM
    )
    pure_audit_tuple = (
        isinstance(audit_node, ast.Tuple)
        and all(
            isinstance(element, ast.Constant)
            and isinstance(element.value, str)
            for element in audit_node.elts
        )
    )
    passed = all(
        (
            timeout == AUDIT_TIMEOUT_SEC,
            note_path == NOTE_PATH,
            pure_audit_tuple,
            audit_paths == AUDIT_INPUT_PATHS,
            all(fragment in predicate_text for fragment in composition_fragments),
            {
                "E730.charge_row_value",
                "E730.rotate_forward",
                "E730.tuple_to_mask",
                "E730.F728.token_parity",
            }
            <= predicate_calls,
            all(fragment in lawful_condition for fragment in lawful_fragments),
            all(
                fragment in violating_condition
                for fragment in violating_fragments
            ),
            all(
                fragment in equivalence_condition
                for fragment in equivalence_fragments
            ),
            all(
                fragment in refusal_condition
                for fragment in refusal_fragments
            ),
            common_arguments
            == {
                "tick_id": 0,
                "orientation": 1,
                "certificate": 1,
                "binder": 1,
                "actuality": 1,
                "admissibility": 1,
            },
            admit_share_common,
            admit_law_domains
            == {
                "constant_chain.admit": "1",
                "derived_chain.admit": "derived_flag",
            },
            only_argument == "law_domain",
            "law_domain=1 admits" in behavioral_delta,
            "law_domain=0 refuses" in behavioral_delta,
            boundary_exact,
            "frontier_cycle743_law_flag_derived_2026_07_28" not in source[
                : source.find("import frontier_cycle719")
            ],
        )
    )
    return {
        "pass": passed,
        "audit_tuple_literal": pure_audit_tuple,
        "predicate_composition_extracted": all(
            fragment in predicate_text for fragment in composition_fragments
        ),
        "lawful_orbit_events": 4,
        "lawful_q_time_rows": 44,
        "charge_violators": 183,
        "count_violators": 55,
        "declared_mismatches": 0,
        "adapter_delta_argument": only_argument,
        "boundary_keys": {
            key: boundary[key]
            for key in (
                "law_flag_derived_at_fixture_scope",
                "admiss_derived",
                "actual_derived",
                "binder_derived",
                "w3_closed",
            )
        },
    }


def _bits_to_int(bits: tuple[int, ...]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(bits))


def _rotate(
    a: tuple[int, ...], b: tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    stations = len(a)
    return (
        tuple(a[(station - 1) % stations] for station in range(stations)),
        tuple(b[(station + 1) % stations] for station in range(stations)),
    )


def _reference_from_q(
    q_mask: int, h: int, stations: int
) -> tuple[int, ...]:
    current = 0
    refs = 0
    closure = 0
    for station in range(stations):
        refs |= current << station
        following = (
            current
            ^ ((q_mask >> station) & 1)
            ^ (h if station == 0 else 0)
        )
        if station == stations - 1:
            closure = following
        else:
            current = following
    if closure:
        raise AssertionError(("reference obstruction", q_mask, h, stations))
    return tuple((refs >> station) & 1 for station in range(stations))


def _lawful_refs(stations: int) -> tuple[tuple[int, ...], int]:
    h = stations & 1
    refs = _reference_from_q((1 << stations) - 1, h, stations)
    return refs, h


def _event_state(
    program: tuple[object, ...],
    data: tuple[int, ...],
    a_positions: tuple[int, ...],
    refs: tuple[int, ...],
    h: int,
) -> dict[str, object]:
    stations = len(program)
    return {
        "program": program,
        "data": data,
        "A": tuple(
            int(station in a_positions) for station in range(stations)
        ),
        "B": (0,) * stations,
        "refs": refs,
        "h": h,
    }


def _component_rows(state: dict[str, object]) -> tuple[bool, ...]:
    program = state["program"]
    a = state["A"]
    b = state["B"]
    refs = state["refs"]
    h = int(state["h"])
    stations = len(program)
    rows = []
    for _step in range(stations):
        charge_null = True
        for station, occupied in enumerate(a):
            if not occupied or not K.mapped_macro(program[station]):
                continue
            charge_null = charge_null and not (
                a[station]
                ^ b[station]
                ^ refs[station]
                ^ refs[(station + 1) % stations]
                ^ (h if station == 0 else 0)
            )
        a_mask = _bits_to_int(a)
        b_mask = _bits_to_int(b)
        count_member = a_mask.bit_count() == C731.EXPECTED_COUNT
        parity_member = (
            (a_mask.bit_count() + b_mask.bit_count()) & 1
        ) == h
        rows.append(charge_null and count_member and parity_member)
        a, b = _rotate(a, b)
    return tuple(rows)


def _charge_events(
    program: tuple[object, ...],
    refs: tuple[int, ...],
    h: int,
) -> tuple[tuple[int, int], ...]:
    stations = len(program)
    a = (1,) + (0,) * (stations - 1)
    b = (0,) * stations
    events = []
    for step in range(stations):
        for station, occupied in enumerate(a):
            if (
                occupied
                and K.mapped_macro(program[station])
                and (
                    a[station]
                    ^ b[station]
                    ^ refs[station]
                    ^ refs[(station + 1) % stations]
                    ^ (h if station == 0 else 0)
                )
            ):
                events.append((step, station))
        a, b = _rotate(a, b)
    return tuple(events)


def _charge_cases(
    program: tuple[object, ...],
) -> tuple[dict[str, object], ...]:
    stations = len(program)
    baseline_refs, baseline_h = _lawful_refs(stations)
    rows = []
    for station, program_row in enumerate(program):
        if not K.mapped_macro(program_row):
            continue
        for kind, flipped_ref in (
            ("flip_ref_s", station),
            ("flip_ref_s_plus_1", (station + 1) % stations),
        ):
            refs = list(baseline_refs)
            refs[flipped_ref] ^= 1
            rows.append(
                {
                    "station": station,
                    "kind": kind,
                    "flipped_ref": flipped_ref,
                    "refs": tuple(refs),
                    "h": baseline_h,
                }
            )
    if K.mapped_macro(program[0]):
        rows.append(
            {
                "station": 0,
                "kind": "flip_h",
                "flipped_ref": None,
                "refs": baseline_refs,
                "h": baseline_h ^ 1,
            }
        )
    return tuple(rows)


def predicate_recount() -> dict[str, object]:
    program = K.interleaved_program(2)
    stations = len(program)
    refs, h = _lawful_refs(stations)
    declared_refs, declared_h = E730.lawful_reference_rails(stations)
    word, layout, _blocks, _metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, C731.EXPECTED_COUNT
        )
    )

    banks, links = K.B.chain_genesis(2)
    physical_state = K.M.pack_state(banks, links)
    lawful_events = []
    q_time_rows = 0
    q_time_failures = 0
    lawful_mismatches = 0
    for event in range(4):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(physical_state, direction)
        state = _event_state(program, before, (0,), refs, h)
        predicate = INDEPENDENT_LAW(state)
        components = _component_rows(state)
        q_time_rows += len(components)
        q_time_failures += sum(not row for row in components)

        source = C731.controller_full_input(
            _bits_to_int(before), layout, a=(0,), refs=refs, h=h
        )
        observed = C731.literal_apply(
            (source,), word, layout["full_width"], stations
        )[0]
        rows = C731.controller_rows(observed, layout)
        after, a, b, _trace = K.run_orbit(before, program)
        actual_unrefused = (
            rows["data"] == _bits_to_int(after)
            and rows["A"] == a
            and rows["B"] == b
            and not any(rows["work"])
            and rows["refs"] == refs
            and rows["h"] == h
            and C731.all_auxiliary_clean(rows)
        )
        mismatch = predicate != int(actual_unrefused)
        lawful_mismatches += mismatch
        lawful_events.append(
            (event, predicate, bool(actual_unrefused), bool(mismatch))
        )
        physical_state = after

    charge_program = E730.R719.PROGRAM
    own_charge_cases = _charge_cases(charge_program)
    declared_charge_cases = E730.charge_violation_cases(charge_program)
    case_identity_match = own_charge_cases == declared_charge_cases
    charge_predicate_mismatches = 0
    own_charge_refusals = 0
    for case in own_charge_cases:
        state = _event_state(
            charge_program,
            (),
            (0,),
            case["refs"],
            int(case["h"]),
        )
        predicate = INDEPENDENT_LAW(state)
        events = _charge_events(
            charge_program, case["refs"], int(case["h"])
        )
        own_charge_refusals += len(events)
        charge_predicate_mismatches += predicate != 0 or not events

    charge_oracle = E730.charge_violation_census_certificate()
    charge_oracle_failures = sum(
        int(charge_oracle[key])
        for key in (
            "literal_prediction_mismatches",
            "host_prediction_mismatches",
            "refusal_event_mismatches",
            "target_station_refusal_mismatches",
            "rail_and_reference_return_failures",
            "syndrome_scratch_return_failures",
        )
    )

    placements = tuple(
        (left, right)
        for left in range(stations)
        for right in range(left + 1, stations)
    )
    initial_banks, initial_links = K.B.chain_genesis(2)
    initial = K.M.prepare_endpoint(
        K.M.pack_state(initial_banks, initial_links), (1, 0)
    )
    initial_value = _bits_to_int(initial)
    count_sources = []
    count_refs = []
    count_case_identity_match = True
    for placement in placements:
        a_mask = sum(1 << station for station in placement)
        case_refs = _reference_from_q(a_mask, 0, stations)
        count_refs.append(case_refs)
        count_case_identity_match = (
            count_case_identity_match
            and case_refs == C731.canonical_refs(a_mask, 0, 0, stations)
        )
        count_sources.append(
            C731.controller_full_input(
                initial_value,
                layout,
                a=placement,
                refs=case_refs,
                h=0,
            )
        )
    count_observed = C731.literal_apply(
        tuple(count_sources), word, layout["full_width"], 1
    )
    count_mismatches = 0
    count_literal_refusals = 0
    for placement, case_refs, observed in zip(
        placements, count_refs, count_observed
    ):
        state = _event_state(program, initial, placement, case_refs, 0)
        predicate = INDEPENDENT_LAW(state)
        rows = C731.controller_rows(observed, layout)
        a_before = tuple(
            int(station in placement) for station in range(stations)
        )
        expected_a, expected_b = _rotate(
            a_before, (0,) * stations
        )
        actual_refused = (
            rows["data"] == initial_value
            and rows["A"] == expected_a
            and rows["B"] == expected_b
            and not any(rows["work"])
            and rows["refs"] == case_refs
            and rows["h"] == 0
            and C731.all_auxiliary_clean(rows)
        )
        count_literal_refusals += actual_refused
        actual_unrefused = not actual_refused
        count_mismatches += predicate != int(actual_unrefused)

    passed = all(
        (
            E730.F728.marked_station(stations) == 0,
            refs == declared_refs,
            h == declared_h,
            len(lawful_events) == 4,
            q_time_rows == 44,
            q_time_failures == 0,
            lawful_mismatches == 0,
            all(
                predicate == 1 and actual and not mismatch
                for _event, predicate, actual, mismatch in lawful_events
            ),
            case_identity_match,
            len(own_charge_cases) == 183,
            charge_predicate_mismatches == 0,
            own_charge_refusals == 341,
            charge_oracle["census_size"] == 183,
            charge_oracle["observed_refusals"] == 341,
            charge_oracle_failures == 0,
            count_case_identity_match,
            len(placements) == 55,
            count_literal_refusals == 55,
            count_mismatches == 0,
        )
    )
    return {
        "pass": passed,
        "lawful_orbit_events": len(lawful_events),
        "lawful_q_time_rows": q_time_rows,
        "lawful_mismatches": lawful_mismatches,
        "charge_states": len(own_charge_cases),
        "charge_refusal_events": own_charge_refusals,
        "charge_mismatches": charge_predicate_mismatches,
        "count_states": len(placements),
        "count_literal_refusals": count_literal_refusals,
        "count_mismatches": count_mismatches,
        "total_states_recounted": (
            len(lawful_events) + len(own_charge_cases) + len(placements)
        ),
    }


def _canonical_trace_bytes(rows: list[dict[str, object]]) -> bytes:
    return json.dumps(
        rows, sort_keys=True, separators=(",", ":"), default=str
    ).encode()


def _run_adapter(derived: bool) -> dict[str, object]:
    program = K.interleaved_program(2)
    refs, h = _lawful_refs(len(program))
    banks, links = K.B.chain_genesis(2)
    physical_state = K.M.pack_state(banks, links)
    chain = K.B.C704.C610.EventChain(bank=4)
    trace_rows = []
    flags = []
    for event in range(4):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(physical_state, direction)
        state = _event_state(program, before, (0,), refs, h)
        law_flag = INDEPENDENT_LAW(state) if derived else 1
        after, a, b, controller_trace = K.run_orbit(before, program)
        banks, links = K.M.unpack_state(after, 2)
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
        flags.append(law_flag)
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
    payload = _canonical_trace_bytes(trace_rows)
    return {
        "trace_bytes": payload,
        "trace_sha256": sha256(payload).hexdigest(),
        "flags": tuple(flags),
        "events": len(trace_rows),
    }


def adapter_recount() -> dict[str, object]:
    constant = _run_adapter(False)
    derived = _run_adapter(True)

    program = K.interleaved_program(2)
    refs, h = _lawful_refs(len(program))
    hostile_refs = list(refs)
    hostile_refs[0] ^= 1
    hostile_refs = tuple(hostile_refs)
    banks, links = K.B.chain_genesis(2)
    before = K.M.prepare_endpoint(
        K.M.pack_state(banks, links), (1, 0)
    )
    hostile_state = _event_state(
        program, before, (0,), hostile_refs, h
    )
    hostile_flag = INDEPENDENT_LAW(hostile_state)
    hostile_components = _component_rows(hostile_state)

    word, layout, _blocks, _metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, C731.EXPECTED_COUNT
        )
    )
    initial_data = _bits_to_int(before)
    source = C731.controller_full_input(
        initial_data,
        layout,
        a=(0,),
        refs=hostile_refs,
        h=h,
    )
    observed = C731.literal_apply(
        (source,), word, layout["full_width"], 1
    )[0]
    rows = C731.controller_rows(observed, layout)
    unwrapped = K.A.apply_semantic(
        before, K.mapped_macro(program[0])
    )
    cascade_refused = (
        rows["data"] == initial_data
        and C731.all_auxiliary_clean(rows)
        and unwrapped != before
    )

    after_constant, a_constant, b_constant, trace_constant = K.run_orbit(
        before, program
    )
    after_derived, a_derived, b_derived, trace_derived = K.run_orbit(
        before, program
    )
    constant_chain = K.B.C704.C610.EventChain(bank=4)
    derived_chain = K.B.C704.C610.EventChain(bank=4)
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
        **common_arguments, law_domain=hostile_flag
    )
    controller_equal = (
        after_constant == after_derived
        and a_constant == a_derived
        and b_constant == b_derived
        and trace_constant == trace_derived
    )
    byte_equal = constant["trace_bytes"] == derived["trace_bytes"]
    passed = all(
        (
            constant["events"] == derived["events"] == 4,
            constant["flags"] == (1, 1, 1, 1),
            derived["flags"] == (1, 1, 1, 1),
            byte_equal,
            constant["trace_sha256"] == derived["trace_sha256"],
            hostile_flag == 0,
            not all(hostile_components),
            cascade_refused,
            constant_status == "admitted",
            str(derived_status).startswith("refused"),
            K.B.cell_rows(constant_chain) != (),
            K.B.cell_rows(derived_chain) == (),
            controller_equal,
        )
    )
    return {
        "pass": passed,
        "lawful_events": constant["events"],
        "lawful_trace_byte_equal": byte_equal,
        "lawful_trace_sha256": constant["trace_sha256"],
        "hostile_derived_law_domain": hostile_flag,
        "hostile_constant_status": constant_status,
        "hostile_derived_status": derived_status,
        "hostile_cascade_refused": cascade_refused,
        "only_admit_argument_changed": "law_domain",
        "controller_output_and_trace_equal": controller_equal,
    }


def _predicate_input_probe(source: str, function_name: str) -> dict[str, object]:
    tree = ast.parse(source)
    function_node = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == function_name
    )
    arguments = tuple(argument.arg for argument in function_node.args.args)
    keys = set()
    for node in ast.walk(function_node):
        if (
            isinstance(node, ast.Subscript)
            and isinstance(node.value, ast.Name)
            and node.value.id == "event_state"
            and isinstance(node.slice, ast.Constant)
            and isinstance(node.slice.value, str)
        ):
            keys.add(node.slice.value)
    call_leaves = {
        (
            node.func.attr
            if isinstance(node.func, ast.Attribute)
            else node.func.id
            if isinstance(node.func, ast.Name)
            else ast.unparse(node.func)
        )
        for node in ast.walk(function_node)
        if isinstance(node, ast.Call)
    }
    identifiers = {
        node.id for node in ast.walk(function_node) if isinstance(node, ast.Name)
    }
    identifiers |= {
        node.attr
        for node in ast.walk(function_node)
        if isinstance(node, ast.Attribute)
    }
    forbidden = {
        "admit",
        "accept",
        "accepted",
        "acceptance",
        "status",
        "law_domain",
        "certificate",
        "binder",
        "actuality",
        "admissibility",
    }
    return {
        "arguments": arguments,
        "event_state_keys": tuple(sorted(keys)),
        "acceptance_calls": tuple(sorted(call_leaves & forbidden)),
        "supplied_flag_identifiers": tuple(sorted(identifiers & forbidden)),
        "pass": (
            arguments == ("event_state",)
            and keys == {"program", "A", "B", "refs", "h"}
            and not (call_leaves & forbidden)
            and not (identifiers & forbidden)
        ),
    }


def independence_probe() -> dict[str, object]:
    _source, primary_tree = _read_primary_ast()
    primary_predicate_source = _static_string(
        _assignment(primary_tree.body, "LAW_PREDICATE_SOURCE")
    )
    primary = _predicate_input_probe(
        primary_predicate_source, "LAW_PREDICATE"
    )
    independent = _predicate_input_probe(
        INDEPENDENT_LAW_SOURCE, "INDEPENDENT_LAW"
    )
    passed = (
        primary["pass"]
        and independent["pass"]
        and "admit" not in primary_predicate_source
        and "law_domain" not in primary_predicate_source
        and "admit" not in INDEPENDENT_LAW_SOURCE
        and "law_domain" not in INDEPENDENT_LAW_SOURCE
    )
    return {
        "pass": passed,
        "primary_dynamic_inputs": primary["event_state_keys"],
        "independent_dynamic_inputs": independent["event_state_keys"],
        "acceptance_call_feedback": (),
        "supplied_flag_inputs": (),
        "genuinely_upstream_of_admit": passed,
    }


def discipline() -> dict[str, object]:
    loaded_files = tuple(
        str(getattr(module, "__file__", ""))
        for module in sys.modules.values()
        if getattr(module, "__file__", None)
    )
    blocklist_clean = (
        all(name not in sys.modules for name in IMPORT_BLOCKLIST)
        and all(
            not path.endswith(
                "frontier_cycle743_law_flag_derived_2026_07_28.py"
            )
            for path in loaded_files
        )
    )
    scope_exact = (
        SCOPE_STATEMENT_VERBATIM
        == (
            "This changes LAW's supply status AT THE HELD FIXTURE SCOPE only "
            "after this exact identification; it does NOT derive ADMISS; "
            "ACTUAL/BINDER remain supplied constants; W3 is NOT closed "
            "(three flags remain; the composed occurrence route is the named "
            "next mechanism)."
        )
        and REMAINING_SCOPE_VERBATIM
        == "three flags remain supplied; w3 open"
    )
    passed = all(
        (
            not WRITE_ATTEMPTS,
            blocklist_clean,
            scope_exact,
            AUDIT_INPUT_PATHS
            == (
                "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
                "scripts/frontier_cycle730_charge_row_enforcement_2026_07_28.py",
                "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
            ),
            NOTE_PATH
            == "docs/LAW_FLAG_DERIVED_CYCLE743_BOUNDED_THEOREM_NOTE_2026-07-28.md",
            sys.dont_write_bytecode,
        )
    )
    return {
        "pass": passed,
        "landed_write_attempts": len(WRITE_ATTEMPTS),
        "import_blocklist": IMPORT_BLOCKLIST,
        "blocklist_clean": blocklist_clean,
        "scope_statement": SCOPE_STATEMENT_VERBATIM,
        "remaining_scope": REMAINING_SCOPE_VERBATIM,
        "w3_closed": False,
    }


def main() -> int:
    started = perf_counter()
    results: dict[str, object] = {}
    certificates = (
        ("A_extraction", extraction),
        ("B_predicate_recount", predicate_recount),
        ("C_adapter_recount", adapter_recount),
        ("D_independence_probe", independence_probe),
        ("E_discipline", discipline),
    )
    for label, certificate in certificates:
        try:
            result = certificate()
            results[label] = result
            check(label, bool(result["pass"]))
        except Exception as error:
            results[label] = {
                "pass": False,
                "error_type": type(error).__name__,
                "error": str(error)[:1000],
            }
            check(label, False)

    elapsed = perf_counter() - started
    report = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not passed for passed in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(elapsed, 6),
        "certificates": results,
        "terminal": (
            "CYCLE743_LAW_FLAG_INDEPENDENT_CHECK_PASS"
            if all(CHECKS.values())
            else "CYCLE743_LAW_FLAG_INDEPENDENT_CHECK_HONEST_FAIL"
        ),
    }
    payload = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    projected = (
        "\n".join(OUTPUT_LINES)
        + "\n"
        + "PASS OUTPUT_stdout_under_150KB\n"
        + payload
        + "\n"
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(projected.encode()) < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(
        not passed for passed in CHECKS.values()
    )
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE743_LAW_FLAG_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE743_LAW_FLAG_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        text = (
            "FAIL OUTPUT_stdout_under_150KB\n"
            '{"pass":false,"terminal":'
            '"CYCLE743_LAW_FLAG_INDEPENDENT_CHECK_HONEST_FAIL"}\n'
        )
        sys.stdout.write(text)
        return 1
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
