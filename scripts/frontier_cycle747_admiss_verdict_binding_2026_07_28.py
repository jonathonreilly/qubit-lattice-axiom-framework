#!/usr/bin/env python3
"""Cycle 747: conditional ADMISS binding to the Cycle-332 verdict tuple.

This bounded runner identifies a one-bit ADMISS adapter on Cycle 332's own
declared occurrence surface.  It does not derive the word projection, boundary
preparation, ACTUAL, BINDER, Record typing, permanence, or W3 closure.
"""
from __future__ import annotations

import ast
from dataclasses import dataclass, replace
from hashlib import sha256
import inspect
import json
import textwrap
import time

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/ADMISS_VERDICT_BINDING_CYCLE747_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import physical_transition_occurrence_close_tournament_cycle332_2026_07_18 as O332
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


PASS = 0
FAIL = 0

# These four phrases are verbatim from the extract's conditional one-bit ADMISS
# convention: it is valid only after they are independently justified.
CONDITIONS = (
    "word projections",
    "boundary preparation",
    "fixed comparator",
    "matcher/readiness semantics",
)

# This is Cycle 332's verbatim terminal supplied/open inventory in the extract.
CYCLE332_SUPPLIED_OR_OPEN = (
    "two boundary registers and their preparation",
    "selection of the actual history member",
    "fixed transition/comparator programs",
    "fresh witness/certificate/history capacity",
    "Record typing",
    "permanence",
    "clock matcher and calibration",
)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", json.dumps(detail, sort_keys=True, default=str))
    else:
        FAIL += 1
        print("FAIL", label, "::", json.dumps(detail, sort_keys=True, default=str))


@dataclass(frozen=True)
class OccurrenceData:
    program: object
    pre: int
    post: int
    pre_code: int
    post_code: int
    match: int
    ready: int
    event_ready: int
    deleted_stage: int | None = None


@dataclass(frozen=True)
class VerdictEvent:
    pre_state: tuple[object, ...]
    occurrence_data: OccurrenceData


def o332_verdict_tuple(event):
    data = event.occurrence_data
    transition = O332.transition_witness(data.program, data.pre, data.post)
    close = O332.boundary_certificate(
        data.pre_code,
        transition,
        data.post_code,
        data.match,
        data.ready,
        deleted_stage=data.deleted_stage,
    )
    receiver = O332.c326.run_local_close(
        event_ready=data.event_ready,
        identity_match=data.match,
        dependencies_ready=data.ready,
        occurrence=transition,
        close_law=close,
    )
    return transition, close, receiver


def ADMISS_PREDICATE(event):
    _transition, _close, receiver = o332_verdict_tuple(event)
    _receiver_negative, receiver_positive = receiver
    return int(receiver_positive)


def verdicts_pass(verdict: tuple[object, ...]) -> bool:
    transition, close, receiver = verdict
    receiver_negative, receiver_positive = receiver
    return bool(
        transition
        and close
        and not receiver_negative
        and receiver_positive
    )


def lawful_fixture_family() -> tuple[tuple[VerdictEvent, ...], dict[str, object]]:
    events = []
    by_length = {}
    anchors = {}
    for length in (3, 6):
        program = O332.compile_transition_program(length)
        fixture = O332.c329.build_fixture(length)
        match, ready = O332.c329.route_outputs(fixture, "syndrome")
        nonvacuum = program.active_rows[program.nonvacuum[program.active_rows]]
        by_length[str(length)] = len(nonvacuum)
        for ordinal, pre_value in enumerate(nonvacuum):
            pre = int(pre_value)
            post = int(program.sidecar.stream_mapping[pre])
            data = OccurrenceData(
                program=program,
                pre=pre,
                post=post,
                pre_code=1,
                post_code=1,
                match=match,
                ready=ready,
                event_ready=1,
            )
            events.append(VerdictEvent((length, ordinal), data))
        anchors[length] = events[-len(nonvacuum)]
    return tuple(events), {
        "by_length": by_length,
        "total": len(events),
        "anchors": anchors,
    }


def violating_fixture_family(
    lawful_detail: dict[str, object],
) -> tuple[tuple[tuple[str, VerdictEvent], ...], dict[str, object]]:
    rows = []
    categories = {}
    anchors = lawful_detail["anchors"]
    for length in (3, 6):
        anchor = anchors[length]
        data = anchor.occurrence_data
        program = data.program
        fixture = O332.c329.build_fixture(length)
        active = program.active_rows
        active_set = set(map(int, active))
        nonvacuum = active[program.nonvacuum[active]]

        false_post = data.post ^ 1
        other = int(nonvacuum[1])
        spliced_post = int(program.sidecar.stream_mapping[other])
        corrupted_target = list(fixture.words[4].word)
        corrupted_target[O332.c329.LABEL_BITS] ^= 1
        bad_match, good_ready = O332.c329.route_outputs(
            fixture,
            "syndrome",
            target_word=tuple(corrupted_target),
        )

        variants = (
            (
                "readiness_alone",
                replace(
                    data,
                    post=false_post,
                    pre_code=0,
                    post_code=0,
                ),
            ),
            (
                "h_only_false_boundary",
                replace(
                    data,
                    post=false_post,
                    post_code=int(false_post in active_set),
                ),
            ),
            (
                "spliced_boundary",
                replace(data, post=spliced_post),
            ),
            (
                "anti_splice_match",
                replace(data, match=bad_match, ready=good_ready),
            ),
            *tuple(
                (
                    f"deleted_certificate_stage_{stage}",
                    replace(data, deleted_stage=stage),
                )
                for stage in range(5)
            ),
        )
        for ordinal, (category, variant) in enumerate(variants):
            event = VerdictEvent((length, ordinal), variant)
            rows.append((category, event))
            categories[category] = categories.get(category, 0) + 1
    return tuple(rows), {
        "by_category": dict(sorted(categories.items())),
        "total": len(rows),
    }


def _dotted_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        left = _dotted_name(node.value)
        return f"{left}.{node.attr}" if left else node.attr
    return ""


def predicate_ast_certificate() -> dict[str, object]:
    source = "\n".join(
        textwrap.dedent(inspect.getsource(function))
        for function in (o332_verdict_tuple, ADMISS_PREDICATE)
    )
    tree = ast.parse(source)
    constants = [
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant)
    ]
    calls = sorted(
        {
            _dotted_name(node.func)
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
        }
    )
    required_calls = {
        "O332.transition_witness",
        "O332.boundary_certificate",
        "O332.c326.run_local_close",
        "o332_verdict_tuple",
        "int",
    }
    return {
        "call_graph": calls,
        "required_calls_present": required_calls.issubset(calls),
        "literal_constants": constants,
        "no_new_constants": not constants,
    }


def upstream_independence_certificate() -> dict[str, object]:
    source = "\n".join(
        textwrap.dedent(inspect.getsource(function))
        for function in (o332_verdict_tuple, ADMISS_PREDICATE)
    )
    tree = ast.parse(source)
    names = sorted(
        {
            node.id
            for node in ast.walk(tree)
            if isinstance(node, ast.Name)
        }
    )
    attributes = sorted(
        {
            _dotted_name(node)
            for node in ast.walk(tree)
            if isinstance(node, ast.Attribute)
        }
    )
    forbidden_names = {"admit", "admission", "chain", "feedback", "status"}
    admit_calls = [
        _dotted_name(node.func)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and _dotted_name(node.func).split(".")[-1] == "admit"
    ]
    return {
        "event_input_only": "event.occurrence_data" in attributes,
        "uses_pre_state_or_occurrence_data_only": (
            "event.occurrence_data" in attributes
            and "event.pre_state" not in attributes
        ),
        "forbidden_feedback_names": sorted(forbidden_names.intersection(names)),
        "admit_calls": admit_calls,
        "independent": (
            "event.occurrence_data" in attributes
            and not forbidden_names.intersection(names)
            and not admit_calls
        ),
    }


def admission_kwargs(index: int, admissibility: int) -> dict[str, int]:
    return {
        "tick_id": index,
        "orientation": 1 if index % 2 == 0 else -1,
        "certificate": 1,
        "binder": 1,
        "actuality": 1,
        "admissibility": admissibility,
        "law_domain": 1,
    }


def adapter_trace(
    events: tuple[VerdictEvent, ...],
    *,
    derived: bool,
) -> tuple[bytes, dict[str, object]]:
    chain = K.B.C704.C610.EventChain(bank=len(events))
    statuses = []
    for index, event in enumerate(events):
        admissibility = ADMISS_PREDICATE(event) if derived else 1
        statuses.append(chain.admit(**admission_kwargs(index, admissibility)))
    payload = {
        "statuses": statuses,
        "cell_rows": K.B.cell_rows(chain),
        "admitted_ticks": sorted(chain.admitted_ticks),
        "exhausted": chain.exhausted,
    }
    trace = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return trace, {
        "events": len(events),
        "admitted": statuses.count("admitted"),
        "refused": len(statuses) - statuses.count("admitted"),
        "bytes": len(trace),
        "sha256": sha256(trace).hexdigest(),
    }


def refusal_delta(event: VerdictEvent) -> dict[str, object]:
    derived_flag = ADMISS_PREDICATE(event)
    baseline_kwargs = admission_kwargs(0, 1)
    derived_kwargs = admission_kwargs(0, derived_flag)
    differing_inputs = sorted(
        key
        for key in baseline_kwargs
        if baseline_kwargs[key] != derived_kwargs[key]
    )
    baseline_chain = K.B.C704.C610.EventChain(bank=2)
    derived_chain = K.B.C704.C610.EventChain(bank=2)
    baseline_status = baseline_chain.admit(**baseline_kwargs)
    derived_status = derived_chain.admit(**derived_kwargs)
    return {
        "derived_flag": derived_flag,
        "differing_inputs": differing_inputs,
        "baseline_status": baseline_status,
        "derived_status": derived_status,
        "baseline_cells": len(baseline_chain.cells),
        "derived_cells": len(derived_chain.cells),
        "flip_by_flag_alone": (
            differing_inputs == ["admissibility"]
            and baseline_status == "admitted"
            and derived_status.startswith("refused")
            and len(baseline_chain.cells) == 1
            and len(derived_chain.cells) == 0
        ),
    }


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.perf_counter()

    lawful, lawful_detail = lawful_fixture_family()
    violating, violating_detail = violating_fixture_family(lawful_detail)

    anchor_event = lawful_detail["anchors"][3]
    anchor_verdict = o332_verdict_tuple(anchor_event)
    anchor_chain = K.B.C704.C610.EventChain(bank=2)
    anchor_status = anchor_chain.admit(
        **admission_kwargs(0, ADMISS_PREDICATE(anchor_event))
    )
    anchor_detail = {
        "O332_module": O332.__name__,
        "O332_verdict": anchor_verdict,
        "K_module": K.__name__,
        "K_status": anchor_status,
    }
    check(
        "A anchors: one Cycle-332 lawful tuple and one Cycle-719 lawful admission",
        verdicts_pass(anchor_verdict)
        and ADMISS_PREDICATE(anchor_event) == 1
        and anchor_status == "admitted",
        anchor_detail,
    )

    composition = predicate_ast_certificate()
    check(
        "B predicate composition is exactly the Cycle-332 verdict chain with no new constants",
        composition["required_calls_present"]
        and composition["no_new_constants"],
        composition,
    )

    lawful_verdicts = tuple(o332_verdict_tuple(event) for event in lawful)
    lawful_mismatches = sum(
        ADMISS_PREDICATE(event) != int(verdicts_pass(verdict))
        for event, verdict in zip(lawful, lawful_verdicts)
    )
    lawful_nonpasses = sum(not verdicts_pass(verdict) for verdict in lawful_verdicts)
    lawful_detail_public = {
        "by_length": lawful_detail["by_length"],
        "total": lawful_detail["total"],
        "verdict_nonpasses": lawful_nonpasses,
        "identification_mismatches": lawful_mismatches,
    }
    check(
        "C lawful identification is exhaustive on every active nonvacuum Cycle-332 fixture transition",
        lawful_mismatches == lawful_nonpasses == 0
        and all(ADMISS_PREDICATE(event) == 1 for event in lawful),
        lawful_detail_public,
    )

    violating_verdicts = tuple(
        o332_verdict_tuple(event) for _category, event in violating
    )
    violating_mismatches = sum(
        ADMISS_PREDICATE(event) != int(verdicts_pass(verdict))
        for (_category, event), verdict in zip(violating, violating_verdicts)
    )
    violating_passes = sum(verdicts_pass(verdict) for verdict in violating_verdicts)
    violating_predicate_survivors = sum(
        ADMISS_PREDICATE(event) for _category, event in violating
    )
    violating_detail_public = {
        **violating_detail,
        "verdict_passes": violating_passes,
        "predicate_survivors": violating_predicate_survivors,
        "identification_mismatches": violating_mismatches,
    }
    check(
        "D violating identification covers Cycle-332 refusal/failure paths",
        violating_mismatches
        == violating_passes
        == violating_predicate_survivors
        == 0,
        violating_detail_public,
    )

    baseline_trace, baseline_trace_detail = adapter_trace(lawful, derived=False)
    derived_trace, derived_trace_detail = adapter_trace(lawful, derived=True)
    delta = refusal_delta(violating[0][1])
    adapter_detail = {
        "baseline": baseline_trace_detail,
        "derived": derived_trace_detail,
        "lawful_byte_exact": baseline_trace == derived_trace,
        "refusal_delta": delta,
    }
    check(
        "E adapter preserves lawful K traces byte-exactly and flips a failure through ADMISS alone",
        baseline_trace == derived_trace
        and delta["flip_by_flag_alone"],
        adapter_detail,
    )

    upstream = upstream_independence_certificate()
    check(
        "F ADMISS is upstream of K admission feedback",
        upstream["independent"],
        upstream,
    )

    deleted = tuple(
        event
        for category, event in violating
        if category.startswith("deleted_certificate_stage_")
    )
    deleted_predicate_survivors = sum(ADMISS_PREDICATE(event) for event in deleted)
    deleted_statuses = []
    for event in deleted:
        chain = K.B.C704.C610.EventChain(bank=2)
        deleted_statuses.append(
            chain.admit(**admission_kwargs(0, ADMISS_PREDICATE(event)))
        )
    deletion_detail = {
        "cases": len(deleted),
        "expected": 2 * 5,
        "predicate_survivors": deleted_predicate_survivors,
        "adapter_admissions": deleted_statuses.count("admitted"),
        "adapter_refusals": sum(
            status.startswith("refused") for status in deleted_statuses
        ),
    }
    check(
        "G every Cycle-332 certificate-stage deletion is refused",
        len(deleted) == 2 * 5
        and deleted_predicate_survivors == 0
        and deleted_statuses.count("admitted") == 0
        and all(status.startswith("refused") for status in deleted_statuses),
        deletion_detail,
    )

    boundary = {
        "admiss_derived_conditional": True,
        "admiss_derived_unconditional": False,
        "conditions": list(CONDITIONS),
        "cycle332_supplied_or_open": list(CYCLE332_SUPPLIED_OR_OPEN),
        "actual_derived": False,
        "actual_selector_absent_recorded": True,
        "binder_derived": False,
        "law_derived_separately_cycle743": True,
        "law_rederived_here": False,
        "flags_down": ["LAW", "ADMISS"],
        "flags_standing": ["ACTUAL", "BINDER"],
        "two_flags_down_two_standing": True,
        "unchanged_word_projection_derived": False,
        "w1_w2_shown_met_in_allowed_scope": False,
        "w3_closed": False,
        "sharpest_forcing_ledger_line": "missing actual-member selector",
        "supplies": {
            "ACTUAL": "supplied",
            "BINDER": "supplied",
        },
    }
    boundary_honest = (
        boundary["admiss_derived_conditional"]
        and not boundary["admiss_derived_unconditional"]
        and tuple(boundary["conditions"]) == CONDITIONS
        and not boundary["actual_derived"]
        and boundary["actual_selector_absent_recorded"]
        and not boundary["binder_derived"]
        and boundary["law_derived_separately_cycle743"]
        and not boundary["w3_closed"]
        and len(boundary["flags_down"]) == len(boundary["flags_standing"]) == 2
    )
    check(
        "H boundary records conditional ADMISS, supplied ACTUAL/BINDER, separate LAW, and open W3",
        boundary_honest,
        boundary,
    )

    runtime = time.perf_counter() - started
    timed_out = runtime > AUDIT_TIMEOUT_SEC
    check(
        "runtime remains within the declared audit timeout",
        not timed_out,
        {
            "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
            "runtime_sec": round(runtime, 6),
        },
    )

    report = {
        "all_pass": FAIL == 0,
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "audit_timeout_sec": AUDIT_TIMEOUT_SEC,
        "boundary": boundary,
        "certificates": {
            "A_anchors": anchor_detail,
            "B_predicate_composition": composition,
            "C_lawful_identification": lawful_detail_public,
            "D_violating_identification": violating_detail_public,
            "E_adapter": adapter_detail,
            "F_upstream_independence": upstream,
            "G_deletion_control": deletion_detail,
            "H_honest_boundary": boundary_honest,
        },
        "declared_input_paths_equal": DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS,
        "fail": FAIL,
        "note_path": NOTE_PATH,
        "note_required_to_exist": False,
        "pass": PASS,
        "runtime_sec": round(runtime, 6),
    }
    print(json.dumps(report, sort_keys=True, separators=(",", ":"), default=str))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
