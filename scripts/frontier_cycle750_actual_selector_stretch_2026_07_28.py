#!/usr/bin/env python3
"""Cycle 750: bounded stretch attempt for an occurrence-derived ACTUAL selector.

The runner asks whether any selector can be composed from the landed Cycle
335 recurrence, Cycle 332 close-verdict, or Cycle 719 enforcement surfaces.
Scientific candidate failures are data, not runner failures: a clean Outcome
B is successful only when every failure has an exhaustive frozen census.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/ACTUAL_SELECTOR_STRETCH_CYCLE750_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py",
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import protected_recurrent_actual_history_selection_cycle335_2026_07_18 as H335
import physical_transition_occurrence_close_tournament_cycle332_2026_07_18 as O332
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


PASS = 0
FAIL = 0
START = monotonic()


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", compact(detail))
    else:
        FAIL += 1
        print("FAIL", label, "::", compact(detail))


# Candidate A: a member is intrinsic only if H335's one-step recurrent
# permutation fixes a marker placed at that physically occupied member.
def recurrent_fixed_member_selector(slots):
    selected = []
    for member, value in enumerate(slots):
        if value != H335.ONE:
            continue
        probe = tuple(
            H335.ONE if index == member else H335.ZERO
            for index in range(len(slots))
        )
        if H335.rotate_right(probe)[member] == H335.ONE:
            selected.append(member)
    return tuple(selected)


# Candidate B: retain every active boundary pair for which the entire landed
# Cycle-332 transition-plus-close verdict is true.
def all_close_verdict_selector(program, alternatives, match, ready):
    closed = O332.protected_closed_flag(H335.ONE)
    return tuple(
        (pre, post)
        for pre, post in alternatives
        if O332.boundary_certificate(
            closed,
            O332.transition_witness(program, pre, post),
            closed,
            match,
            ready,
        )
    )


# Candidate C: retain each one-token station whose orbit realizes the landed
# controller law, returns exactly, restores the token, and has the landed clean
# postimage.  The supplied source-token reference is deliberately not an input.
def enforcement_lineage_selector(
    program,
    before,
    expected,
    bank_count,
    alternatives,
):
    selected = []
    for position in alternatives:
        tokens = tuple(
            int(index == position)
            for index in range(len(program))
        )
        zeros = tuple(value ^ value for value in tokens)
        after, rail_a, rail_b, _trace = K.run_orbit(
            before,
            program,
            token_positions=(position,),
        )
        if after != expected or rail_a != tokens or rail_b != zeros:
            continue
        restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
            after,
            program,
            token_positions=(position,),
            reverse=True,
        )
        banks, links = K.M.unpack_state(after, bank_count)
        dirty = any(
            (
                after[K.R3.X.SOURCE_POINTER],
                any(
                    bank[wire]
                    for bank in banks
                    for wire in (
                        K.A.POINTER,
                        K.A.U_TO_V,
                        K.A.V_TO_U,
                        K.A.DIRECTION_OK,
                        *K.A.FRESH,
                        *K.A.ZERO_WORK,
                        K.A.TOKEN_OK,
                    )
                ),
                any(any(link) for link in links),
            )
        )
        if all(
            (
                restored == before,
                inverse_a == rail_a,
                inverse_b == rail_b,
                not dirty,
            )
        ):
            selected.append(position)
    return tuple(selected)


def actual_identification_adapter(alternatives, selected):
    return tuple(
        (alternative, int(alternative in selected))
        for alternative in alternatives
    )


CANDIDATE_NAMES = (
    "recurrent_fixed_member_selector",
    "all_close_verdict_selector",
    "enforcement_lineage_selector",
)


def header_and_ast_audit() -> dict[str, object]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    assignments = {}
    functions = {}
    imports = {}
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
            for target in targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions[node.name] = node
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports[alias.asname or alias.name] = alias.name

    audit_tuple = assignments.get("AUDIT_INPUT_PATHS")
    declared = assignments.get("DECLARED_INPUT_PATHS")
    literal_tuple = (
        isinstance(audit_tuple, ast.Tuple)
        and len(audit_tuple.elts) == len(AUDIT_INPUT_PATHS)
        and all(isinstance(item, ast.Constant) and isinstance(item.value, str) for item in audit_tuple.elts)
    )
    imported = {
        alias: imports.get(alias)
        for alias in ("H335", "O332", "K")
    }

    candidate_asts = {}
    module_roots = {}
    forbidden_constants = {}
    selector_inputs = {}
    for name in CANDIDATE_NAMES:
        node = functions[name]
        candidate_asts[name] = ast.unparse(node)
        roots = set()
        constants = []
        for child in ast.walk(node):
            if isinstance(child, ast.Attribute):
                root = child
                while isinstance(root, ast.Attribute):
                    root = root.value
                if isinstance(root, ast.Name) and root.id in {"H335", "O332", "K"}:
                    roots.add(root.id)
            if (
                isinstance(child, ast.Constant)
                and type(child.value) is not bool
                and child.value is not None
            ):
                constants.append(child.value)
        module_roots[name] = sorted(roots)
        forbidden_constants[name] = constants
        selector_inputs[name] = [
            argument.arg
            for argument in node.args.args
            if any(token in argument.arg.lower() for token in ("reference", "actual", "selector"))
        ]

    expected_roots = {
        "recurrent_fixed_member_selector": ["H335"],
        "all_close_verdict_selector": ["H335", "O332"],
        "enforcement_lineage_selector": ["K"],
    }
    detail = {
        "pure_literal_audit_tuple": literal_tuple,
        "audit_paths": list(AUDIT_INPUT_PATHS),
        "declared_is_audit_name": isinstance(declared, ast.Name)
        and declared.id == "AUDIT_INPUT_PATHS",
        "timeout": AUDIT_TIMEOUT_SEC,
        "note_path": NOTE_PATH,
        "imports": imported,
        "candidate_module_roots": module_roots,
        "candidate_non_boolean_constants": forbidden_constants,
        "candidate_selector_inputs": selector_inputs,
    }
    check(
        "header, literal input declaration, and exact landed imports are pinned",
        literal_tuple
        and tuple(ast.literal_eval(audit_tuple)) == AUDIT_INPUT_PATHS
        and isinstance(declared, ast.Name)
        and declared.id == "AUDIT_INPUT_PATHS"
        and AUDIT_TIMEOUT_SEC == 900
        and NOTE_PATH
        == "docs/ACTUAL_SELECTOR_STRETCH_CYCLE750_BOUNDED_THEOREM_NOTE_2026-07-28.md"
        and imported
        == {
            "H335": "protected_recurrent_actual_history_selection_cycle335_2026_07_18",
            "O332": "physical_transition_occurrence_close_tournament_cycle332_2026_07_18",
            "K": "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        },
        detail,
    )
    check(
        "no-new-supplier AST audit admits only landed module roots and no selector input or non-Boolean candidate constant",
        module_roots == expected_roots
        and all(not values for values in forbidden_constants.values())
        and all(not values for values in selector_inputs.values()),
        {
            "module_roots": module_roots,
            "non_boolean_constants": forbidden_constants,
            "selector_inputs": selector_inputs,
            "fixture_literal_provenance": {
                "H335": "protected_recurrence_controls initial/history/phase convention",
                "O332": "L=3,6 active rows plus relational_close_controls matcher fixture",
                "K": "held_certificate sizes, directions, genesis, law word, and default source token",
            },
        },
    )
    for name in CANDIDATE_NAMES:
        print("AST", name, "::", compact(candidate_asts[name]))
    return detail


def anchor_certificates() -> dict[str, object]:
    initial = (H335.ONE, H335.ONE, H335.ONE, H335.ZERO)
    ring = [initial]
    for _phase in range(len(initial)):
        ring.append(H335.rotate_right(ring[-1]))
    h_anchor = {
        "period": len(initial),
        "unique_states": len(set(ring[:-1])),
        "recurs": ring[-1] == initial,
    }

    program = O332.compile_transition_program(3)
    active_nonvacuum = program.active_rows[program.nonvacuum[program.active_rows]]
    pre = int(active_nonvacuum[0])
    post = int(program.sidecar.stream_mapping[pre])
    fixture = O332.c329.build_fixture(3)
    match, ready = O332.c329.route_outputs(fixture, "syndrome")
    witness = O332.transition_witness(program, pre, post)
    certificate = O332.boundary_certificate(1, witness, 1, match, ready)
    o_anchor = {
        "L": 3,
        "pair": [pre, post],
        "match_ready": [match, ready],
        "witness": witness,
        "certificate": certificate,
    }

    held = K.held_certificate(2)
    k_anchor = {
        "banks": held["banks"],
        "events": held["events"],
        "logical_failures": held["logical_failures"],
        "fixed_word_failures": held["fixed_word_failures"],
        "inverse_failures": held["inverse_failures"],
        "postimage_failures": held["postimage_failures"],
        "token_return_failures": held["token_return_failures"],
    }
    detail = {"H335": h_anchor, "O332": o_anchor, "K": k_anchor}
    check(
        "anchors: one lawful landed case from H335, O332, and K",
        h_anchor == {"period": 4, "unique_states": 4, "recurs": True}
        and o_anchor["match_ready"] == [1, 1]
        and o_anchor["witness"] == o_anchor["certificate"] == 1
        and not any(
            k_anchor[key]
            for key in (
                "logical_failures",
                "fixed_word_failures",
                "inverse_failures",
                "postimage_failures",
                "token_return_failures",
            )
        ),
        detail,
    )
    return detail


def recurrent_candidate_census() -> dict[str, object]:
    initial = (H335.ONE, H335.ONE, H335.ONE, H335.ZERO)
    history = [initial]
    for _phase in range(len(initial) - 1):
        history.append(H335.rotate_right(history[-1]))

    rows = []
    cyclic_failures = []
    for phase, slots in enumerate(history):
        alternatives = tuple(
            index for index, value in enumerate(slots) if value == H335.ONE
        )
        selected = recurrent_fixed_member_selector(slots)
        reference = (phase,)
        rows.append(
            {
                "fixture": f"ring_L4_phase{phase}",
                "alternative_count": len(alternatives),
                "selected": list(selected),
                "reference": list(reference),
            }
        )
        for shift in range(len(slots)):
            rotated = slots[-shift:] + slots[:-shift] if shift else slots
            observed = recurrent_fixed_member_selector(rotated)
            expected = tuple(sorted((member + shift) % len(slots) for member in selected))
            if observed != expected:
                cyclic_failures.append(
                    {
                        "phase": phase,
                        "shift": shift,
                        "observed": list(observed),
                        "expected": list(expected),
                    }
                )

    tests = {
        "totality": all(len(row["selected"]) == 1 for row in rows),
        "invariance": not cyclic_failures,
        "identification": all(row["selected"] == row["reference"] for row in rows),
    }
    result = {
        "definition": (
            "Among occupied protected triples, select precisely those marker "
            "positions fixed by H335.rotate_right."
        ),
        "fixtures_exhausted": len(rows),
        "alternatives_exhausted": sum(row["alternative_count"] for row in rows),
        "cyclic_symmetry_cases": len(rows) * len(initial),
        "selected_counts": [len(row["selected"]) for row in rows],
        "tests": tests,
        "counterexample": rows[0],
        "symmetry_failures": cyclic_failures[:3],
    }
    check(
        "candidate A recurrent intrinsic-order census is exhaustive and frozen",
        len(rows) == 4
        and result["alternatives_exhausted"] == 12
        and result["cyclic_symmetry_cases"] == 16
        and result["selected_counts"] == [0, 0, 0, 0]
        and tests == {
            "totality": False,
            "invariance": True,
            "identification": False,
        },
        result,
    )
    return result


def close_candidate_census() -> dict[str, object]:
    rows = []
    frame_failures = []
    for length in (3, 6):
        program = O332.compile_transition_program(length)
        fixture = O332.c329.build_fixture(length)
        match, ready = O332.c329.route_outputs(fixture, "syndrome")
        active = tuple(map(int, program.active_rows))
        active_nonvacuum = tuple(
            int(row) for row in program.active_rows if program.nonvacuum[row]
        )
        alternatives = tuple(
            (pre, post)
            for pre in active_nonvacuum
            for post in active
        )
        selected = all_close_verdict_selector(
            program,
            alternatives,
            match,
            ready,
        )
        reference_pre = active_nonvacuum[0]
        reference = (
            (reference_pre, int(program.sidecar.stream_mapping[reference_pre])),
        )
        selected_set = set(selected)
        frames = O332.c314.c311.c235.proper_cubic_frames()
        for frame_index, frame in enumerate(frames):
            mapping, failures = O332.event_frame_mapping(program.sidecar, frame)
            mapped_selected = {
                (int(mapping[pre]), int(mapping[post]))
                for pre, post in selected
            }
            if failures or mapped_selected != selected_set:
                frame_failures.append(
                    {
                        "L": length,
                        "frame": frame_index,
                        "mapping_failures": failures,
                        "symmetric_difference": len(mapped_selected ^ selected_set),
                    }
                )
        rows.append(
            {
                "fixture": f"active_boundary_pairs_L{length}",
                "active_pre_count": len(active_nonvacuum),
                "active_post_count": len(active),
                "alternative_count": len(alternatives),
                "selected_count": len(selected),
                "reference": [list(reference[0])],
                "first_selected": list(selected[0]) if selected else None,
                "frame_cases": len(frames),
            }
        )

    tests = {
        "totality": all(row["selected_count"] == 1 for row in rows),
        "invariance": not frame_failures,
        "identification": all(
            row["selected_count"] == 1
            and row["first_selected"] == row["reference"][0]
            for row in rows
        ),
    }
    result = {
        "definition": (
            "For each complete L=3 or L=6 epoch before a boundary pair is "
            "supplied, select every active nonvacuum (pre,post) pair whose "
            "O332 transition witness and five-input close certificate are true."
        ),
        "fixtures_exhausted": len(rows),
        "alternatives_exhausted": sum(row["alternative_count"] for row in rows),
        "selected_counts": [row["selected_count"] for row in rows],
        "proper_cubic_frame_cases": sum(row["frame_cases"] for row in rows),
        "tests": tests,
        "counterexample": rows[0],
        "symmetry_failures": frame_failures[:3],
    }
    check(
        "candidate B all-close-verdict census is exhaustive and frozen",
        len(rows) == 2
        and all(row["active_pre_count"] == 508 for row in rows)
        and all(row["active_post_count"] == 510 for row in rows)
        and all(row["alternative_count"] == 508 * 510 for row in rows)
        and result["selected_counts"] == [508, 508]
        and result["proper_cubic_frame_cases"] == 48
        and tests == {
            "totality": False,
            "invariance": True,
            "identification": False,
        },
        result,
    )
    return result


def k_epoch_fixtures(bank_count):
    program = K.interleaved_program(bank_count)
    banks, links = K.B.chain_genesis(bank_count)
    state = K.M.pack_state(banks, links)
    rows = []
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        expected = K.A.apply_semantic(
            before,
            K.M.global_allocator_word(bank_count),
        )
        rows.append((event, direction, program, before, expected))
        state = expected
    return tuple(rows)


def cyclic_enforcement_symmetry(bank_count, before, expected) -> dict[str, object]:
    program = K.interleaved_program(bank_count)
    alternatives = tuple(range(len(program)))
    failures = []
    for shift in range(len(program)):
        rotated = program[shift:] + program[:shift]
        selected = enforcement_lineage_selector(
            rotated,
            before,
            expected,
            bank_count,
            alternatives,
        )
        reference = ((len(program) - shift) % len(program),)
        if selected != reference:
            failures.append(
                {
                    "shift": shift,
                    "selected": list(selected),
                    "covariant_reference": list(reference),
                }
            )
    return {"cases": len(program), "failures": failures}


def spatial_symmetry_census(bank_count) -> dict[str, object]:
    _program, track = K.held_physical_program_and_track(bank_count)
    station_sites = track[::2]
    source_site = station_sites[0]
    frames = K.C712.C709.F.base.proper_cubic_frames()
    frame_failures = []
    for frame_index, frame in enumerate(frames):
        moved = tuple(
            tuple(int(value) for value in frame @ site)
            for site in station_sites
        )
        selected_image = tuple(int(value) for value in frame @ source_site)
        if len(set(moved)) != len(station_sites) or selected_image != moved[0]:
            frame_failures.append(frame_index)
    translations = ((3, -2, 1), (-5, 4, 2))
    translation_failures = []
    for shift in translations:
        moved = tuple(
            tuple(site[axis] + shift[axis] for axis in range(3))
            for site in station_sites
        )
        selected_image = tuple(
            source_site[axis] + shift[axis] for axis in range(3)
        )
        if len(set(moved)) != len(station_sites) or selected_image != moved[0]:
            translation_failures.append(shift)
    return {
        "frame_cases": len(frames),
        "frame_failures": frame_failures,
        "translation_cases": len(translations),
        "translation_failures": translation_failures,
    }


def enforcement_candidate_census() -> dict[str, object]:
    rows = []
    cyclic_rows = []
    spatial_rows = []
    q_order_failures = []
    for bank_count in (2, 5, 12):
        fixtures = k_epoch_fixtures(bank_count)
        for event, direction, program, before, expected in fixtures:
            alternatives = tuple(range(len(program)))
            selected = enforcement_lineage_selector(
                program,
                before,
                expected,
                bank_count,
                alternatives,
            )
            rows.append(
                {
                    "fixture": f"banks{bank_count}_event{event}",
                    "banks": bank_count,
                    "event": event,
                    "direction": list(direction),
                    "alternative_count": len(alternatives),
                    "selected": list(selected),
                    "reference": [0],
                }
            )
            if selected:
                reverse_orders = tuple(
                    tuple(reversed(range(len(program))))
                    for _step in range(len(program))
                )
                ordered, rail_a, rail_b, _trace = K.run_orbit(
                    before,
                    program,
                    token_positions=(selected[0],),
                    q_orders=reverse_orders,
                )
                if (
                    ordered != expected
                    or rail_a
                    != tuple(
                        int(index == selected[0])
                        for index in range(len(program))
                    )
                    or any(rail_b)
                ):
                    q_order_failures.append(rows[-1]["fixture"])
        first = fixtures[0]
        cyclic_rows.append(
            {
                "banks": bank_count,
                **cyclic_enforcement_symmetry(
                    bank_count,
                    first[3],
                    first[4],
                ),
            }
        )
        spatial_rows.append(
            {"banks": bank_count, **spatial_symmetry_census(bank_count)}
        )

    cyclic_failures = [
        {"banks": row["banks"], **failure}
        for row in cyclic_rows
        for failure in row["failures"]
    ]
    spatial_failures = [
        {
            "banks": row["banks"],
            "frame_failures": row["frame_failures"],
            "translation_failures": row["translation_failures"],
        }
        for row in spatial_rows
        if row["frame_failures"] or row["translation_failures"]
    ]
    tests = {
        "totality": all(len(row["selected"]) == 1 for row in rows),
        "invariance": not cyclic_failures
        and not spatial_failures
        and not q_order_failures,
        "identification": all(row["selected"] == row["reference"] for row in rows),
    }
    result = {
        "definition": (
            "Across every one-token station, select the stations whose K orbit "
            "equals the derived global allocator law, restores under the landed "
            "inverse, returns the token/rails, and has the landed clean postimage."
        ),
        "fixtures_exhausted": len(rows),
        "alternatives_exhausted": sum(row["alternative_count"] for row in rows),
        "fixture_counts_by_banks": {
            str(size): sum(row["banks"] == size for row in rows)
            for size in (2, 5, 12)
        },
        "selected_count_range": [
            min(len(row["selected"]) for row in rows),
            max(len(row["selected"]) for row in rows),
        ],
        "cyclic_relabel_cases": sum(row["cases"] for row in cyclic_rows),
        "cyclic_relabel_failures": cyclic_failures[:3],
        "proper_cubic_frame_cases": sum(row["frame_cases"] for row in spatial_rows),
        "spatial_translation_cases": sum(
            row["translation_cases"] for row in spatial_rows
        ),
        "spatial_failures": spatial_failures[:3],
        "q_station_order_cases": len(rows),
        "q_station_order_failures": q_order_failures[:3],
        "tests": tests,
        "first_fixture": rows[0],
    }
    expected_fixture_count = 2 * (2 + 5 + 12)
    expected_alternatives = 2 * 2 * len(K.interleaved_program(2))
    expected_alternatives += 2 * 5 * len(K.interleaved_program(5))
    expected_alternatives += 2 * 12 * len(K.interleaved_program(12))
    check(
        "candidate C enforcement-lineage census is exhaustive and frozen",
        len(rows) == expected_fixture_count == 38
        and result["alternatives_exhausted"] == expected_alternatives == 2578
        and result["selected_count_range"] == [1, 1]
        and result["cyclic_relabel_cases"] == 137
        and result["proper_cubic_frame_cases"] == 72
        and result["spatial_translation_cases"] == 6
        and result["q_station_order_cases"] == 38
        and tests
        == {
            "totality": True,
            "invariance": True,
            "identification": True,
        },
        result,
    )
    return result


def failure_entry(result: dict[str, object]) -> dict[str, object]:
    failed = [
        name for name, passed in result["tests"].items() if not passed
    ]
    return {
        "failed_tests": failed,
        "counterexample": result.get("counterexample", result.get("first_fixture")),
    }


def outcome_certificate(
    candidates: dict[str, dict[str, object]],
) -> dict[str, object]:
    passing = [
        name
        for name, result in candidates.items()
        if all(result["tests"].values())
    ]
    failures = {
        name: failure_entry(result)
        for name, result in candidates.items()
        if not all(result["tests"].values())
    }
    conditions_verbatim = [
        "one controller token at source station and zero B/work rails",
        "source boundary and oriented finite program ring",
        "Q-before-R layer order and bounded local macro gate order",
        "clean data-bank/link/route genesis and event predicates",
    ]
    boundary = {
        "fixture_scope_only": True,
        "held_bank_counts": [2, 5, 12],
        "source_boundary_and_orientation_remain_supplied": True,
        "autonomous_genesis_or_enforcement_derived": False,
        "record_typing_derived": False,
        "permanence_derived": False,
        "time_law_derived": False,
        "w3_closed": False,
    }

    if passing:
        outcome = "A"
        enforcement = candidates[passing[0]]
        alternatives = tuple(
            range(enforcement["first_fixture"]["alternative_count"])
        )
        selected = tuple(enforcement["first_fixture"]["selected"])
        adapted = actual_identification_adapter(alternatives, selected)
        adapter_detail = {
            "candidate": passing[0],
            "alternative_count": len(adapted),
            "actual_flag_count": sum(flag for _alternative, flag in adapted),
            "actual_member": [
                alternative for alternative, flag in adapted if flag
            ],
            "agrees_with_supplied_reference": [
                alternative for alternative, flag in adapted if flag
            ]
            == enforcement["first_fixture"]["reference"],
        }
        check(
            "Outcome A identification plus ACTUAL adapter is applied at exact fixture scope",
            adapter_detail["actual_flag_count"] == 1
            and adapter_detail["agrees_with_supplied_reference"],
            {
                "adapter": adapter_detail,
                "conditions_verbatim": conditions_verbatim,
                "boundary": boundary,
            },
        )
        forcing = {
            "actual_selector_stretch_failed": False,
            "failure_census": failures,
            "forcing_class_proposal": None,
            "minimal_missing_content": None,
        }
        statement = (
            "ACTUAL is derivable only on the landed K held fixtures: the unique "
            "enforcement-lineage survivor is identified with the supplied source "
            "token, and ACTUAL=1 exactly for that survivor, subject verbatim to "
            "the listed landed conditions."
        )
    else:
        outcome = "B"
        adapter_detail = None
        forcing = {
            "actual_selector_stretch_failed": True,
            "failure_census": failures,
            "forcing_class_proposal": (
                "suspected-independent (first precise failure; second independent "
                "attempt required by ledger discipline before promotion)"
            ),
            "minimal_missing_content": (
                "For each epoch's physically available alternatives, an objective "
                "occurrence rule fixes the realized member, and ACTUAL=1 exactly "
                "for that member."
            ),
        }
        check(
            "Outcome B freezes every candidate failure and exact forcing-ledger keys",
            len(failures) == len(candidates)
            and all(entry["failed_tests"] for entry in failures.values())
            and forcing["actual_selector_stretch_failed"] is True
            and forcing["forcing_class_proposal"]
            == (
                "suspected-independent (first precise failure; second independent "
                "attempt required by ledger discipline before promotion)"
            )
            and forcing["minimal_missing_content"]
            == (
                "For each epoch's physically available alternatives, an objective "
                "occurrence rule fixes the realized member, and ACTUAL=1 exactly "
                "for that member."
            ),
            forcing,
        )
        statement = (
            "Every landed candidate fails at least one of totality, invariance, "
            "or identification; the precise first-attempt wall is frozen."
        )

    check(
        "honest boundary remains open beyond the exact selector outcome",
        boundary["w3_closed"] is False
        and boundary["fixture_scope_only"] is True
        and boundary["source_boundary_and_orientation_remain_supplied"] is True
        and not boundary["record_typing_derived"]
        and not boundary["permanence_derived"]
        and not boundary["time_law_derived"],
        boundary,
    )
    return {
        "outcome": outcome,
        "passing_candidates": passing,
        "statement": statement,
        "conditions_verbatim": conditions_verbatim if outcome == "A" else [],
        "adapter": adapter_detail,
        "forcing": forcing,
        "boundary": boundary,
    }


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    header = header_and_ast_audit()
    anchors = anchor_certificates()
    candidates = {
        "recurrent_orbit_intrinsic_order": recurrent_candidate_census(),
        "cycle332_all_close_verdicts": close_candidate_census(),
        "enforcement_lineage": enforcement_candidate_census(),
    }
    outcome = outcome_certificate(candidates)
    elapsed = monotonic() - START
    check(
        "bounded runtime and output-ready terminal contract",
        elapsed < AUDIT_TIMEOUT_SEC,
        {
            "runtime_seconds": round(elapsed, 6),
            "timeout_seconds": AUDIT_TIMEOUT_SEC,
            "note_required": False,
            "note_path": NOTE_PATH,
        },
    )
    report = {
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "candidate_results": candidates,
        "certificates": {
            "anchors": anchors,
            "ast_audit": header,
            "no_new_supplier": True,
        },
        "fail": FAIL,
        "outcome": outcome,
        "pass": PASS,
        "runtime_seconds": round(elapsed, 6),
        "w3_closed": False,
    }
    report["report_sha256"] = sha256(
        compact(report).encode("utf-8")
    ).hexdigest()
    print(compact(report))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
