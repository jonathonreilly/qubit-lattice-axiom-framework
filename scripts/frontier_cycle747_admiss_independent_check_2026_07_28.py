#!/usr/bin/env python3
"""Independent adversarial check of the Cycle-747 conditional ADMISS binding."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/ADMISS_VERDICT_BINDING_CYCLE747_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from dataclasses import dataclass, replace
from hashlib import sha256
import json
from pathlib import Path
import sys
import time


# Imports are permitted only for the two declared audit inputs.  In particular,
# the Cycle-747 primary is parsed as inert text and is never imported.
sys.dont_write_bytecode = True
import physical_transition_occurrence_close_tournament_cycle332_2026_07_18 as O332
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


BLOCKLIST = (
    "scripts/frontier_cycle747_admiss_verdict_binding_2026_07_28.py",
)
PRIMARY_DATA_PATH = BLOCKLIST[0]
EXPECTED_CONDITIONS = (
    "word projections",
    "boundary preparation",
    "fixed comparator",
    "matcher/readiness semantics",
)
SCOPE_LANGUAGE = "two flags derived, two supplied; w3 open"
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", json.dumps(detail, sort_keys=True, default=str))
    else:
        FAIL += 1
        print("FAIL", label, "::", json.dumps(detail, sort_keys=True, default=str))


def _dotted_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = _dotted_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def _function(tree: ast.AST, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one function {name!r}, found {len(matches)}")
    return matches[0]


def _assignment(tree: ast.AST, name: str) -> ast.AST:
    matches = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        if any(isinstance(target, ast.Name) and target.id == name for target in targets):
            matches.append(node.value)
    if len(matches) != 1:
        raise ValueError(f"expected one assignment {name!r}, found {len(matches)}")
    return matches[0]


def _calls(tree: ast.AST) -> set[str]:
    return {
        _dotted_name(node.func)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
    }


def _literal_for_key(mapping: ast.Dict, key: str) -> object:
    for key_node, value_node in zip(mapping.keys, mapping.values):
        if isinstance(key_node, ast.Constant) and key_node.value == key:
            return ast.literal_eval(value_node)
    raise KeyError(key)


def _loop_lengths(function: ast.FunctionDef) -> tuple[int, ...]:
    candidates = []
    for node in ast.walk(function):
        if (
            isinstance(node, ast.For)
            and isinstance(node.target, ast.Name)
            and node.target.id == "length"
        ):
            try:
                value = ast.literal_eval(node.iter)
            except (ValueError, TypeError):
                continue
            if isinstance(value, tuple):
                candidates.append(tuple(int(item) for item in value))
    if candidates != [(3, 6)]:
        raise ValueError(f"unexpected length loops: {candidates!r}")
    return candidates[0]


def _variant_shape(function: ast.FunctionDef) -> tuple[tuple[str, ...], int]:
    variants = _assignment(function, "variants")
    if not isinstance(variants, ast.Tuple):
        raise ValueError("variants is not a literal tuple expression")
    direct = []
    deletion_stages = None
    for element in variants.elts:
        if (
            isinstance(element, ast.Tuple)
            and element.elts
            and isinstance(element.elts[0], ast.Constant)
            and isinstance(element.elts[0].value, str)
        ):
            direct.append(element.elts[0].value)
        elif isinstance(element, ast.Starred):
            range_calls = [
                node
                for node in ast.walk(element.value)
                if isinstance(node, ast.Call)
                and _dotted_name(node.func) == "range"
                and len(node.args) == 1
            ]
            if len(range_calls) != 1:
                raise ValueError("deleted-stage generator does not contain one range")
            deletion_stages = int(ast.literal_eval(range_calls[0].args[0]))
            if "deleted_certificate_stage_" not in ast.unparse(element.value):
                raise ValueError("deleted-stage category format is absent")
        else:
            raise ValueError(f"unexpected variants element: {ast.dump(element)}")
    if deletion_stages is None:
        raise ValueError("deleted-stage variants are absent")
    return tuple(direct), deletion_stages


def extraction(primary_source: str) -> tuple[bool, dict[str, object], ast.Module]:
    """Extract the claim's composition and boundary without executing the primary."""
    tree = ast.parse(primary_source, filename=PRIMARY_DATA_PATH)
    audit_paths = ast.literal_eval(_assignment(tree, "AUDIT_INPUT_PATHS"))
    conditions = ast.literal_eval(_assignment(tree, "CONDITIONS"))

    verdict_function = _function(tree, "o332_verdict_tuple")
    predicate_function = _function(tree, "ADMISS_PREDICATE")
    verdict_calls = _calls(verdict_function)
    predicate_calls = _calls(predicate_function)
    composition_expected = {
        "O332.transition_witness",
        "O332.boundary_certificate",
        "O332.c326.run_local_close",
    }
    predicate_expected = {"o332_verdict_tuple", "int"}
    composition_exact = (
        verdict_calls == composition_expected
        and predicate_calls == predicate_expected
        and not [
            node.value
            for function in (verdict_function, predicate_function)
            for node in ast.walk(function)
            if isinstance(node, ast.Constant)
        ]
        and "return int(receiver_positive)" in ast.unparse(predicate_function)
    )

    lawful_function = _function(tree, "lawful_fixture_family")
    violating_function = _function(tree, "violating_fixture_family")
    lawful_lengths = _loop_lengths(lawful_function)
    violating_lengths = _loop_lengths(violating_function)
    nonvacuum_assign = ast.unparse(_assignment(lawful_function, "nonvacuum"))
    direct_categories, deletion_stages = _variant_shape(violating_function)
    lawful_by_length = {}
    for length in lawful_lengths:
        program = O332.compile_transition_program(length)
        lawful_by_length[str(length)] = len(
            program.active_rows[program.nonvacuum[program.active_rows]]
        )
    lawful_census = sum(lawful_by_length.values())
    violating_census = len(violating_lengths) * (
        len(direct_categories) + deletion_stages
    )
    deletion_census = len(violating_lengths) * deletion_stages
    census_exact = (
        nonvacuum_assign
        == "program.active_rows[program.nonvacuum[program.active_rows]]"
        and direct_categories
        == (
            "readiness_alone",
            "h_only_false_boundary",
            "spliced_boundary",
            "anti_splice_match",
        )
        and (lawful_census, violating_census, deletion_census) == (1016, 18, 10)
    )

    boundary_node = _assignment(_function(tree, "main"), "boundary")
    if not isinstance(boundary_node, ast.Dict):
        raise ValueError("boundary is not a literal-key dictionary")
    boundary = {
        key: _literal_for_key(boundary_node, key)
        for key in (
            "admiss_derived_conditional",
            "admiss_derived_unconditional",
            "actual_derived",
            "actual_selector_absent_recorded",
            "w3_closed",
            "flags_down",
            "flags_standing",
            "supplies",
        )
    }
    boundary_exact = (
        boundary["admiss_derived_conditional"] is True
        and boundary["admiss_derived_unconditional"] is False
        and boundary["actual_derived"] is False
        and boundary["actual_selector_absent_recorded"] is True
        and boundary["w3_closed"] is False
        and boundary["flags_down"] == ["LAW", "ADMISS"]
        and boundary["flags_standing"] == ["ACTUAL", "BINDER"]
        and boundary["supplies"] == {
            "ACTUAL": "supplied",
            "BINDER": "supplied",
        }
    )
    detail = {
        "audit_tuple": audit_paths,
        "boundary": boundary,
        "census": {
            "lawful": lawful_census,
            "lawful_by_length": lawful_by_length,
            "violating": violating_census,
            "deletions": deletion_census,
        },
        "conditions": conditions,
        "predicate_calls": sorted(verdict_calls | predicate_calls),
        "primary_executed": False,
    }
    passed = (
        audit_paths == AUDIT_INPUT_PATHS
        and conditions == EXPECTED_CONDITIONS
        and composition_exact
        and census_exact
        and boundary_exact
    )
    return passed, detail, tree


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
class IndependentEvent:
    pre_state: tuple[object, ...]
    occurrence_data: OccurrenceData


def independent_verdict(event: IndependentEvent) -> tuple[object, ...]:
    """Evaluate the O332 verdict chain without using any Cycle-747 callable."""
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


def independent_admiss(event: IndependentEvent) -> int:
    """The independently implemented one-bit predicate under test."""
    _transition, _close, receiver = independent_verdict(event)
    _receiver_negative, receiver_positive = receiver
    return int(receiver_positive)


FROZEN_VERDICTS = {
    "lawful": (1, 1, (0, 1)),
    "readiness_alone": (0, 0, (1, 0)),
    "h_only_false_boundary": (0, 0, (1, 0)),
    "spliced_boundary": (0, 0, (1, 0)),
    "anti_splice_match": (1, 0, (1, 0)),
    "deleted_certificate_stage": (1, 0, (1, 0)),
}


def _lawful_events() -> tuple[tuple[IndependentEvent, ...], dict[int, IndependentEvent]]:
    events = []
    anchors = {}
    for length in (3, 6):
        program = O332.compile_transition_program(length)
        fixture = O332.c329.build_fixture(length)
        match, ready = O332.c329.route_outputs(fixture, "syndrome")
        nonvacuum = program.active_rows[program.nonvacuum[program.active_rows]]
        length_events = []
        for ordinal, pre_value in enumerate(nonvacuum):
            pre = int(pre_value)
            data = OccurrenceData(
                program=program,
                pre=pre,
                post=int(program.sidecar.stream_mapping[pre]),
                pre_code=1,
                post_code=1,
                match=match,
                ready=ready,
                event_ready=1,
            )
            length_events.append(IndependentEvent((length, ordinal), data))
        anchors[length] = length_events[0]
        events.extend(length_events)
    return tuple(events), anchors


def _violating_events(
    anchors: dict[int, IndependentEvent],
) -> tuple[tuple[str, IndependentEvent], ...]:
    rows = []
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
                replace(data, post=false_post, pre_code=0, post_code=0),
            ),
            (
                "h_only_false_boundary",
                replace(
                    data,
                    post=false_post,
                    post_code=int(false_post in active_set),
                ),
            ),
            ("spliced_boundary", replace(data, post=spliced_post)),
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
        rows.extend(
            (category, IndependentEvent((length, ordinal), variant))
            for ordinal, (category, variant) in enumerate(variants)
        )
    return tuple(rows)


def _frozen_for(category: str) -> tuple[object, ...]:
    if category.startswith("deleted_certificate_stage_"):
        return FROZEN_VERDICTS["deleted_certificate_stage"]
    return FROZEN_VERDICTS[category]


def predicate_recount() -> tuple[
    bool,
    dict[str, object],
    tuple[IndependentEvent, ...],
    tuple[tuple[str, IndependentEvent], ...],
]:
    lawful, anchors = _lawful_events()
    violating = _violating_events(anchors)
    lawful_mismatches = 0
    for event in lawful:
        verdict = independent_verdict(event)
        lawful_mismatches += (
            verdict != FROZEN_VERDICTS["lawful"]
            or independent_admiss(event) != 1
        )
    violating_mismatches = 0
    categories = {}
    deletions = 0
    for category, event in violating:
        verdict = independent_verdict(event)
        expected = _frozen_for(category)
        violating_mismatches += verdict != expected or independent_admiss(event) != 0
        categories[category] = categories.get(category, 0) + 1
        deletions += category.startswith("deleted_certificate_stage_")
    detail = {
        "lawful": len(lawful),
        "lawful_mismatches": lawful_mismatches,
        "violating": len(violating),
        "violating_mismatches": violating_mismatches,
        "deletions": deletions,
        "categories": dict(sorted(categories.items())),
    }
    passed = (
        len(lawful) == 1016
        and len(violating) == 18
        and deletions == 10
        and lawful_mismatches == violating_mismatches == 0
    )
    return passed, detail, lawful, violating


def _admission_kwargs(index: int, admissibility: int) -> dict[str, int]:
    return {
        "tick_id": index,
        "orientation": 1 if index % 2 == 0 else -1,
        "certificate": 1,
        "binder": 1,
        "actuality": 1,
        "admissibility": admissibility,
        "law_domain": 1,
    }


def _adapter_bytes(
    events: tuple[IndependentEvent, ...],
    *,
    derived: bool,
) -> tuple[bytes, int]:
    chain = K.B.C704.C610.EventChain(bank=len(events))
    statuses = []
    for index, event in enumerate(events):
        flag = independent_admiss(event) if derived else 1
        statuses.append(chain.admit(**_admission_kwargs(index, flag)))
    payload = {
        "statuses": statuses,
        "cell_rows": K.B.cell_rows(chain),
        "admitted_ticks": sorted(chain.admitted_ticks),
        "exhausted": chain.exhausted,
    }
    trace = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return trace, statuses.count("admitted")


def adapter_recount(
    lawful: tuple[IndependentEvent, ...],
    violating: tuple[tuple[str, IndependentEvent], ...],
) -> tuple[bool, dict[str, object]]:
    baseline, baseline_admitted = _adapter_bytes(lawful, derived=False)
    derived, derived_admitted = _adapter_bytes(lawful, derived=True)

    failing_event = violating[0][1]
    flag = independent_admiss(failing_event)
    baseline_kwargs = _admission_kwargs(0, 1)
    derived_kwargs = _admission_kwargs(0, flag)
    differing_inputs = sorted(
        key
        for key in baseline_kwargs
        if baseline_kwargs[key] != derived_kwargs[key]
    )
    baseline_chain = K.B.C704.C610.EventChain(bank=2)
    derived_chain = K.B.C704.C610.EventChain(bank=2)
    baseline_status = baseline_chain.admit(**baseline_kwargs)
    derived_status = derived_chain.admit(**derived_kwargs)
    flipped = (
        flag == 0
        and differing_inputs == ["admissibility"]
        and baseline_status == "admitted"
        and derived_status.startswith("refused")
        and len(baseline_chain.cells) == 1
        and len(derived_chain.cells) == 0
    )
    detail = {
        "lawful_byte_equal": baseline == derived,
        "lawful_bytes": len(baseline),
        "lawful_sha256": sha256(baseline).hexdigest(),
        "baseline_admitted": baseline_admitted,
        "derived_admitted": derived_admitted,
        "failure_differing_inputs": differing_inputs,
        "failure_statuses": [baseline_status, derived_status],
        "failure_flipped_by_ADMISS_alone": flipped,
    }
    return (
        baseline == derived
        and baseline_admitted == derived_admitted == len(lawful)
        and flipped,
        detail,
    )


def conditions_audit(o332_source: str) -> tuple[bool, dict[str, object]]:
    tree = ast.parse(o332_source, filename=AUDIT_INPUT_PATHS[0])
    inventory_function = _function(tree, "inventory_controls")
    inventory = ast.literal_eval(_assignment(inventory_function, "inventory"))
    supplied = tuple(inventory["supplied_or_open"])
    calls = _calls(tree)
    docstring = ast.get_docstring(tree) or ""

    word_projection = (
        "c314.build_event_sidecar" in calls
        and "c314.c311.c269.build_code" in calls
        and "sidecar.stream_mapping" in {
            _dotted_name(node)
            for node in ast.walk(tree)
            if isinstance(node, ast.Attribute)
        }
        and "exact Cycle-314 event-flipping stream permutation" in docstring
    )
    boundary_preparation = (
        "two boundary registers and their preparation" in supplied
        and "conditional on supplied boundary" in docstring
    )
    fixed_comparator = "fixed transition/comparator programs" in supplied
    matcher_readiness = (
        "clock matcher and calibration" in supplied
        and "c329.route_outputs" in calls
        and "Cycle-329's physical matcher/readiness outputs" in docstring
    )
    evidence = {
        "word projections": {
            "located": word_projection,
            "source": "compile_transition_program: build_code -> build_event_sidecar -> stream_mapping",
            "status": "imported fixed Cycle-314 convention",
        },
        "boundary preparation": {
            "located": boundary_preparation,
            "source": "supplied_or_open: two boundary registers and their preparation",
        },
        "fixed comparator": {
            "located": fixed_comparator,
            "source": "supplied_or_open: fixed transition/comparator programs",
        },
        "matcher/readiness semantics": {
            "located": matcher_readiness,
            "source": "Cycle-329 route_outputs plus supplied clock matcher/calibration",
        },
    }
    conditional = (
        "conditional on supplied boundary" in docstring
        and all(row["located"] for row in evidence.values())
    )
    detail = {
        "conditions": evidence,
        "conditional_not_absolute": conditional,
        "supplied_or_open_count": len(supplied),
    }
    return conditional, detail


def independence_probe(primary_tree: ast.Module) -> tuple[bool, dict[str, object]]:
    functions = (
        _function(primary_tree, "o332_verdict_tuple"),
        _function(primary_tree, "ADMISS_PREDICATE"),
    )
    combined = ast.Module(body=list(functions), type_ignores=[])
    event_fields = sorted(
        {
            node.attr
            for node in ast.walk(combined)
            if isinstance(node, ast.Attribute)
            and isinstance(node.value, ast.Name)
            and node.value.id == "event"
        }
    )
    calls = _calls(combined)
    names = {
        node.id for node in ast.walk(combined) if isinstance(node, ast.Name)
    }
    forbidden_feedback = sorted(
        {"admit", "admission", "chain", "feedback", "status"}.intersection(names)
    )
    admit_calls = sorted(
        call for call in calls if call.split(".")[-1] == "admit"
    )
    k_references = sorted(name for name in names if name == "K")
    allowed_inputs_only = (
        set(event_fields) <= {"occurrence_data", "pre_state"}
        and "occurrence_data" in event_fields
    )
    independent = (
        allowed_inputs_only
        and not forbidden_feedback
        and not admit_calls
        and not k_references
        and {
            "O332.transition_witness",
            "O332.boundary_certificate",
            "O332.c326.run_local_close",
        }.issubset(calls)
    )
    detail = {
        "allowed_event_fields": ["occurrence_data", "pre_state"],
        "observed_event_fields": event_fields,
        "admit_calls": admit_calls,
        "feedback_names": forbidden_feedback,
        "K_references": k_references,
        "independent": independent,
    }
    return independent, detail


def _input_digests() -> dict[str, str]:
    paths = (PRIMARY_DATA_PATH,) + AUDIT_INPUT_PATHS
    return {
        path: sha256(Path(path).read_bytes()).hexdigest()
        for path in paths
    }


def discipline(
    primary_tree: ast.Module,
    before: dict[str, str],
    after: dict[str, str],
) -> tuple[bool, dict[str, object]]:
    blocked_modules = {Path(path).stem for path in BLOCKLIST}
    loaded_blocked = sorted(blocked_modules.intersection(sys.modules))
    primary_imports = sorted(
        {
            alias.name
            for node in ast.walk(primary_tree)
            if isinstance(node, (ast.Import, ast.ImportFrom))
            for alias in (
                node.names
                if isinstance(node, ast.Import)
                else [ast.alias(name=node.module or "")]
            )
        }
        & blocked_modules
    )
    no_landed_writes = before == after and sys.dont_write_bytecode
    scope = {
        "language": SCOPE_LANGUAGE,
        "derived": ["LAW", "ADMISS"],
        "supplied": ["ACTUAL", "BINDER"],
        "w3_open": True,
    }
    clean = (
        no_landed_writes
        and not loaded_blocked
        and not primary_imports
        and tuple(BLOCKLIST) == (PRIMARY_DATA_PATH,)
        and scope["language"] == "two flags derived, two supplied; w3 open"
        and len(scope["derived"]) == len(scope["supplied"]) == 2
        and scope["w3_open"]
    )
    detail = {
        "blocklist": BLOCKLIST,
        "blocked_modules_loaded": loaded_blocked,
        "input_digests_unchanged": before == after,
        "pycache_writes_disabled": sys.dont_write_bytecode,
        "scope": scope,
    }
    return clean, detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.perf_counter()
    before = _input_digests()
    primary_source = Path(PRIMARY_DATA_PATH).read_text(encoding="utf-8")
    o332_source = Path(AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")

    extracted, extraction_detail, primary_tree = extraction(primary_source)
    check("extraction", extracted, extraction_detail)

    recounted, recount_detail, lawful, violating = predicate_recount()
    check("predicate_recount", recounted, recount_detail)

    adapter_ok, adapter_detail = adapter_recount(lawful, violating)
    check("adapter_recount", adapter_ok, adapter_detail)

    conditions_ok, conditions_detail = conditions_audit(o332_source)
    check("conditions_audit", conditions_ok, conditions_detail)

    independent, independence_detail = independence_probe(primary_tree)
    check("independence_probe", independent, independence_detail)

    after = _input_digests()
    disciplined, discipline_detail = discipline(primary_tree, before, after)
    check("discipline", disciplined, discipline_detail)

    runtime = time.perf_counter() - started
    check(
        "runtime",
        runtime <= AUDIT_TIMEOUT_SEC,
        {
            "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
            "runtime_sec": round(runtime, 6),
        },
    )
    report = {
        "all_pass": FAIL == 0,
        "pass": PASS,
        "fail": FAIL,
        "runtime_sec": round(runtime, 6),
        "recounts": recount_detail,
        "conditions_conditional": conditions_detail["conditional_not_absolute"],
        "independent": independence_detail["independent"],
        "scope": SCOPE_LANGUAGE,
    }
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, separators=(",", ":")))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
