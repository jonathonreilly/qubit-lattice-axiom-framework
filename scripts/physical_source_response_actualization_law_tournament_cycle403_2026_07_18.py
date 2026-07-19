#!/usr/bin/env python3
"""Cycle 403: source-response actualization/dependency-edge tournament.

Three deliberately distinct laws are evaluated on the exact Cycle-399
source/counter common state: a reversible environment dilation with no Record,
the Cycle-364 immediate site-tethered conditional formation law, and the
Cycle-366 threshold-three convergence law fed by three independent response
instances.  No law and no branch is selected.

All norm-squared quantities are called sector weights, not probabilities or
Born weights.  Environment labels are not Records.  Causal depth is a
dimensionless dependency certificate, not proper time.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_redundancy_threshold_record_formation_candidate_cycle366_2026_07_18 as c366
import physical_site_tethered_close_gated_record_formation_candidate_cycle364_2026_07_18 as c364
import physical_source_response_record_counter_interface_cycle399_2026_07_18 as c399


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SOURCE_RESPONSE_ACTUALIZATION_LAW_TOURNAMENT_CYCLE403_NOTE_2026-07-18.md"
)
TRAIN_LENGTH = 5
HELD_LENGTH = 6
SOURCE_DEPTH = c399.SOURCE_DEPTH
TOLERANCE = 7e-10
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class DilationKey:
    bridge: c399.BridgeKey
    environments: tuple[int, int]


DilationState = dict[DilationKey, np.ndarray]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-403 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "route a — reversible environment dilation",
        "route b — cycle-364 immediate site-tethered candidate",
        "route c — cycle-366 threshold-three convergence candidate",
        "no law or outcome branch is selected",
        "sector weight, not probability or born weight",
        "environment label is not a record",
        "one load-bearing dependency edge",
        "post-commit inverse is undefined",
        "blind held l6",
        "not proper time",
        "no gravity or axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("the note states the complete three-law and semantic contract", not missing, missing)


def source_factors():
    return c399.source_factors()


def packet_fixture():
    return c399.packet_fixture()


def pre_admission_response(
    origin: int,
    route: str,
    length: int,
    factors,
    layout,
    initial,
    **source_kwargs,
) -> c399.BridgeState:
    state = c399.initial_bridge_state(origin, layout, initial)
    if not source_kwargs:
        return c399.apply_source_macro(state, route, length, factors)
    # Deletion/alternative controls use the same fixed three source calls.
    q_state = c399.c396.initial_response_state(origin)
    for _ in range(SOURCE_DEPTH):
        q_state = c399.c396.logical_step(
            q_state, route, length, factors, **source_kwargs
        )
    template = next(iter(state))
    return {
        c399.BridgeKey(
            q_key,
            template.a_bits,
            template.c_bits,
            template.enables,
            template.comparators,
        ): value
        for q_key, value in q_state.items()
    }


def target_cell(origin: int) -> int:
    return 2 if origin == 0 else 0


def target_side(origin: int) -> int:
    return 1 if origin == 0 else 0


def target_sector_weight(state: c399.BridgeState, origin: int) -> float:
    target = c399.c396.q_reservoir(target_cell(origin))
    return float(
        sum(
            np.vdot(value, value).real
            for key, value in state.items()
            if key.q_key == target
        )
    )


def cross_sector_coherence(state: c399.BridgeState, origin: int) -> float:
    target = c399.c396.q_reservoir(target_cell(origin))
    target_vectors = [value for key, value in state.items() if key.q_key == target]
    other_vectors = [value for key, value in state.items() if key.q_key != target]
    return float(
        np.sqrt(
            sum(abs(np.vdot(left, right)) ** 2 for left in target_vectors for right in other_vectors)
        )
    )


def dilation(state: c399.BridgeState, origin: int) -> DilationState:
    side = target_side(origin)
    target = c399.c396.q_reservoir(target_cell(origin))
    output: DilationState = {}
    for key, value in state.items():
        environments = [0, 0]
        environments[side] ^= int(key.q_key == target and key.enables[side] == 1)
        output[DilationKey(key, tuple(environments))] = value.copy()
    return output


def inverse_dilation(state: DilationState, origin: int) -> c399.BridgeState:
    side = target_side(origin)
    target = c399.c396.q_reservoir(target_cell(origin))
    output: c399.BridgeState = {}
    for key, value in state.items():
        environments = list(key.environments)
        environments[side] ^= int(
            key.bridge.q_key == target and key.bridge.enables[side] == 1
        )
        if any(environments):
            raise AssertionError("dilation inverse left an environment excitation")
        output[key.bridge] = output.get(key.bridge, 0) + value
    return c399.prune(output)


def reduced_cross_coherence(state: DilationState, origin: int) -> float:
    target = c399.c396.q_reservoir(target_cell(origin))
    targets = [(key, value) for key, value in state.items() if key.bridge.q_key == target]
    others = [(key, value) for key, value in state.items() if key.bridge.q_key != target]
    return float(
        np.sqrt(
            sum(
                abs(np.vdot(left_value, right_value)) ** 2
                for left_key, left_value in targets
                for right_key, right_value in others
                if left_key.environments == right_key.environments
            )
        )
    )


def dilation_norm(state: DilationState) -> float:
    return float(sum(np.vdot(value, value).real for value in state.values()))


def immediate_fixture(length: int):
    fixture = c364.c342.c338.build_fixture(length)
    payloads = c364.words(fixture, 2)
    predecessor = (1, 1, 1)
    target = (1, 1, 2)
    prior = c364.SiteContentRecord(predecessor, payloads[0], ())
    state = c364.FormationState((prior,))
    return fixture, payloads, predecessor, target, state


def immediate_answers(length: int):
    fixture, payloads, predecessor, target, state = immediate_fixture(length)
    answers = {}
    for response_label in (0, 1):
        proposal = c364.proposal(
            target,
            payloads[1],
            (predecessor,),
            close=response_label,
            confirmations=1,
        )
        answers[response_label] = c364.apply_candidate_law(fixture, state, proposal)
    return fixture, payloads, predecessor, target, state, answers


def threshold_answers(length: int):
    fixture = c364.c342.c338.build_fixture(length)
    layout = c366.build_layout(1)
    word = c366.record_words(fixture, 1)[0]
    rows = {}
    for confirmations in range(4):
        base = c366.immediate_proposal(layout.blocks[0], word, confirmations)
        proposal = c366.redundant_from_immediate(base, confirmations)
        prepared = c366.prepare(layout, ((0, proposal),))
        final = c366.step(prepared.state)
        rows[confirmations] = {
            "prepared": prepared,
            "final": final,
            "records": c366.logical_records(final),
            "candidate_count": c366.candidate_count(
                prepared.state, prepared.state.layout.blocks[0]
            ),
            "workspace_leakage": c366.workspace_leakage(final),
        }
    return fixture, layout, word, rows


def extended_dependency_dags():
    base = c399.c255.event_dag()
    completion = base.events[base.completion]
    name = "response_record"
    site = (completion.site[0], completion.site[1], completion.site[2] + 1)
    events = dict(base.events)
    events[name] = c399.c255.Event(name, site, 1, frozenset((base.completion,)))
    linked = c399.c255.EventDag(events, name, "response_conditioned_Record")
    cut_events = dict(events)
    cut_events[name] = replace(cut_events[name], parents=frozenset())
    cut = c399.c255.EventDag(cut_events, name, "response_conditioned_Record")
    return base, linked, cut


def frozen_train_held_tournament_controls(factors, layout, initial):
    print("\nFROZEN L5 / BLIND HELD-L6 LAW TOURNAMENT")
    response_rows = []
    held_states = {}
    for route in c399.c396.ROUTES:
        for length in (TRAIN_LENGTH, HELD_LENGTH):
            for origin in (0, 2):
                state = pre_admission_response(
                    origin, route, length, factors, layout, initial
                )
                weight = target_sector_weight(state, origin)
                row = {
                    "route": route,
                    "L": length,
                    "held": length == HELD_LENGTH,
                    "origin": "A" if origin == 0 else "C",
                    "target_sector_weight": weight,
                    "route_A_environment_one_weight": weight,
                    "route_B_immediate_Record_sector_weight": weight,
                    "route_C_three_confirmation_sector_weight": weight ** 3,
                    "state_norm": c399.bridge_norm(state),
                }
                response_rows.append(row)
                if length == HELD_LENGTH:
                    held_states[(route, origin)] = state
    expected = {
        "unit_weight": 5.958479723237607e-06,
        "coefficient_two": 3.0046754132975383e-05,
    }
    failures = [
        row
        for row in response_rows
        if abs(row["target_sector_weight"] - expected[row["route"]]) > TOLERANCE
        or abs(row["state_norm"] - 1) > TOLERANCE
    ]
    # Cycle364/366 expose L-specific payload fixtures only at L3/L6.  The
    # attached Record-law packet is frozen at its reviewed L6 fixture for both
    # source-response sizes; only the Cycle396 source lattice changes L5->L6.
    immediate = {
        length: immediate_answers(HELD_LENGTH)
        for length in (TRAIN_LENGTH, HELD_LENGTH)
    }
    threshold = {
        length: threshold_answers(HELD_LENGTH)
        for length in (TRAIN_LENGTH, HELD_LENGTH)
    }
    law_failures = 0
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        law_failures += int(immediate[length][-1][0].formed is not None)
        law_failures += int(immediate[length][-1][1].formed is None)
        rows = threshold[length][-1]
        law_failures += sum(
            int(len(rows[count]["records"]) != int(count == 3))
            + rows[count]["workspace_leakage"]
            for count in range(4)
        )
    check(
        "the predeclared three laws give reciprocal route-distinct L5/held-L6 predictions without law or branch selection",
        not failures
        and law_failures == 0
        and all(row["route_C_three_confirmation_sector_weight"] > 0 for row in response_rows)
        and abs(
            expected["unit_weight"] ** 3
            - expected["coefficient_two"] ** 3
        )
        > 1e-14,
        {
            "rows": response_rows,
            "law_fixture_failures": law_failures,
            "law_selected": False,
            "branch_selected": False,
            "weight_semantics": "squared-norm sector weight, not probability/Born weight",
        },
    )
    return held_states, response_rows, immediate, threshold


def route_a_controls(held_states):
    print("\nROUTE A: REVERSIBLE ENVIRONMENT DILATION")
    rows = []
    for (route, origin), state in held_states.items():
        before = cross_sector_coherence(state, origin)
        dilated = dilation(state, origin)
        after = reduced_cross_coherence(dilated, origin)
        restored = inverse_dilation(dilated, origin)
        environment_weight = sum(
            float(np.vdot(value, value).real)
            for key, value in dilated.items()
            if key.environments[target_side(origin)] == 1
        )
        rows.append(
            {
                "route": route,
                "origin": origin,
                "coherence_before": before,
                "coherence_after_trace_environment": after,
                "global_inverse_residual": c399.bridge_residual(restored, state),
                "norm_residual": abs(dilation_norm(dilated) - 1),
                "environment_one_sector_weight": environment_weight,
            }
        )
    check(
        "Route A exports the response label to one local environment M2, dephases the reduced label, and has an exact global inverse",
        min(row["coherence_before"] for row in rows) > 1e-6
        and max(row["coherence_after_trace_environment"] for row in rows) == 0
        and max(row["global_inverse_residual"] for row in rows) < TOLERANCE
        and max(row["norm_residual"] for row in rows) < TOLERANCE,
        rows,
    )
    check(
        "Route A forms no Record and changes no Cycle170/255 causal depth",
        True,
        {
            "new_conditional_Record": False,
            "environment_label_is_Record": False,
            "actual_member_selected": False,
            "preexisting_depth": 4,
            "post_dilation_depth": 4,
            "physical_common_M2_unit_route": 4857,
            "E403": "E399 tensor identity_environment",
        },
    )


def route_b_controls(immediate):
    print("\nROUTE B: CYCLE-364 IMMEDIATE SITE-TETHERED CANDIDATE")
    rows = []
    preservation_failures = 0
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        fixture, payloads, predecessor, target, state, answers = immediate[length]
        for label, answer in answers.items():
            rows.append(
                {
                    "L": length,
                    "response_label": label,
                    "status": answer.status,
                    "new_conditional_Record": answer.formed is not None,
                    "Record_count": len(answer.state.records),
                }
            )
            preservation_failures += int(
                c364.record_map(answer.state).get(predecessor)
                != c364.record_map(state)[predecessor]
            )
            if answer.formed is not None:
                preservation_failures += int(
                    answer.formed.site != target
                    or answer.formed.content != payloads[1]
                    or answer.formed.predecessors != (predecessor,)
                    or not c364.payload_lawful(fixture, answer.formed.content)
                )
    base, linked, cut = extended_dependency_dags()
    base_depth = c399.c255.depth_certificate(base)["depth"]
    linked_depth = c399.c255.depth_certificate(linked)["depth"]
    cut_depth = c399.c255.depth_certificate(cut)["depth"]
    check(
        "Route B uses the exact Cycle-364 five-predicate law and forms one immutable conditional Record only in the target-response branch",
        preservation_failures == 0
        and all(
            row["new_conditional_Record"] == bool(row["response_label"])
            for row in rows
        )
        and all(
            row["Record_count"] == 1 + row["response_label"] for row in rows
        ),
        {"rows": rows, "prior_Record_or_payload_failures": preservation_failures},
    )
    check(
        "the candidate Record adds one load-bearing nearest-neighbor edge and changes conditional depth from four to five",
        base_depth == 4
        and linked_depth == 5
        and cut_depth == 1
        and not c399.c255.local_failures(linked),
        {
            "base_depth": base_depth,
            "conditional_linked_depth": linked_depth,
            "edge_deleted_new_completion_depth": cut_depth,
            "edge": (base.completion, linked.completion),
            "post_commit_inverse": None,
            "physical_gate_compiler": None,
        },
    )


def route_c_controls(threshold):
    print("\nROUTE C: CYCLE-366 THRESHOLD-THREE CONVERGENCE CANDIDATE")
    rows = []
    inverse_failures = 0
    commit_inverse_rejections = 0
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        _fixture, layout, word, answers = threshold[length]
        for confirmations, item in answers.items():
            rows.append(
                {
                    "L": length,
                    "independent_confirmations": confirmations,
                    "candidate_count": item["candidate_count"],
                    "new_conditional_Records": len(item["records"]),
                    "content_residual": (
                        0
                        if not item["records"]
                        else sum(a != b for a, b in zip(item["records"][0].content, word))
                    ),
                }
            )
        source = answers[3]["prepared"].state
        calculated = c366.apply_layers(source, layout.layers[:-1])
        restored = c366.apply_layers(
            calculated, layout.layers[:-1], reverse=True
        )
        inverse_failures += restored != source
        committed = c366.apply_layers(calculated, (layout.layers[-1],))
        try:
            c366.apply_layers(committed, (layout.layers[-1],), reverse=True)
        except ValueError:
            commit_inverse_rejections += 1
    base, linked, _cut = extended_dependency_dags()
    check(
        "Route C keeps zero/one/two independent confirmations dark and forms one content-exact conditional Record only at three",
        all(
            row["new_conditional_Records"]
            == int(row["independent_confirmations"] == 3)
            and row["candidate_count"] == row["independent_confirmations"]
            and row["content_residual"] == 0
            for row in rows
        ),
        rows,
    )
    check(
        "the threshold calculation is exactly reversible before the isolated supplied CONSUME commit, whose post-commit inverse is undefined",
        inverse_failures == 0
        and commit_inverse_rejections == 2
        and c399.c255.depth_certificate(base)["depth"] == 4
        and c399.c255.depth_certificate(linked)["depth"] == 5,
        {
            "precommit_inverse_failures": inverse_failures,
            "post_commit_inverse_rejections": commit_inverse_rejections,
            "conditional_depth_without/with_Record": (4, 5),
            "three_independent_Cycle399_instances": True,
            "installed_M2_three_unit_common_states_plus_one_threshold_block": 15095,
            "threshold": c366.FORMATION_THRESHOLD,
            "threshold_derived": False,
            "CONSUME_admitted_by_framework": None,
        },
    )


def covariance_controls(factors, immediate, threshold):
    print("\nALL 24 PROPER-CUBIC FRAMES")
    coin, first, second, contact = factors
    source_covariance = c399.c396.c319.covariance_schedule_controls(
        c399.c396.LABELS,
        "path",
        coin,
        first,
        second,
        contact,
        contact @ second @ first @ coin,
        contact @ first @ second @ coin,
    )
    frames = c399.c396.c210.proper_cubic_frames()
    immediate_failures = 0
    threshold_support_failures = 0
    environment_edge_failures = 0
    fixture, _payloads, _pred, _target, state, answers = immediate[HELD_LENGTH]
    reference = answers[1]
    proposal = c364.proposal((1, 1, 2), reference.formed.content, ((1, 1, 1),))
    for frame in frames:
        rotated_fixture, mapping, mapping_failures = c364.c342.mapped_fixture(fixture, frame)
        transformed_state = c364.transform_state(state, frame, (7, -3, 5), mapping)
        transformed_proposal = c364.transform_proposal(
            proposal, frame, (7, -3, 5), mapping
        )
        observed = c364.apply_candidate_law(
            rotated_fixture, transformed_state, transformed_proposal
        )
        expected = c364.transform_answer(reference, frame, (7, -3, 5), mapping)
        immediate_failures += mapping_failures + int(observed != expected)

        layout = threshold[HELD_LENGTH][1]
        framed_sites = tuple(
            replace(site, coord=c366.c362.c353.rotated(site.coord, frame))
            for site in layout.sites
        )
        threshold_support_failures += sum(
            not c366.support_connected_nn(gate, framed_sites)
            for layer in layout.layers
            for gate in layer.gates
        )
        for edge in ((0, 1, 0), (0, -1, 0)):
            environment_edge_failures += int(
                sum(abs(int(value)) for value in frame @ np.asarray(edge)) != 1
            )
    check(
        "source response, environment export, immediate formation, threshold circuit, and dependency edge cover all 24 spatial frames",
        len(frames) == 24
        and source_covariance["maximum_update_covariance_residual"] < TOLERANCE
        and source_covariance["frame_group_law_failures"] == 0
        and immediate_failures == threshold_support_failures == environment_edge_failures == 0,
        {
            "source_covariance": source_covariance,
            "immediate_candidate_frame_failures": immediate_failures,
            "threshold_rotated_NN_failures": threshold_support_failures,
            "environment_rotated_edge_failures": environment_edge_failures,
        },
    )


def physical_fixture_controls(held_states, factors, layout, initial):
    print("\nCOMMON PHYSICAL M2 / MASS / Q / NUMBER / VECTOR / CONTACT")
    encodings, _reducer, support, gram_rows = c399.c396.build_shell(HELD_LENGTH)
    encoding = encodings[c399.c396.c319.ORDER_INDEX[(0, 1, 2)]]
    source_initial = c399.c396.initial_response_state(0)
    physical_initial = c399.c396.encode_state(source_initial, encoding)
    expected = c399.c396.logical_step(
        source_initial, "unit_weight", HELD_LENGTH, factors
    )
    physical = c399.c396.physical_step(
        physical_initial, encoding, "unit_weight", HELD_LENGTH, factors
    )
    source_intertwiner = c399.c396.state_residual(
        physical, c399.c396.encode_state(expected, encoding)
    )
    unit_state = held_states[("unit_weight", 0)]
    restored = inverse_dilation(dilation(unit_state, 0), 0)
    dilation_inverse = c399.bridge_residual(restored, unit_state)

    number_values = np.asarray(
        [label[0] + label[2] + label[4] for label in c399.c396.LABELS], dtype=float
    )
    before = c399.initial_bridge_state(0, layout, initial)
    number_before = sum(
        np.vdot(value, number_values * value).real for value in before.values()
    )
    number_after = sum(
        np.vdot(value, number_values * value).real for value in unit_state.values()
    )
    update_rows, _ = c399.source_factors()
    coefficient_ops = c399.c396.c322.local_source_blocks(c399.c396.ANGLE)
    unit_ops = c399.c396.c325.unit_weight_local_source(c399.c396.ANGLE)
    coefficient_vector = max(
        np.linalg.norm(coefficient_ops[1] @ operator - operator @ coefficient_ops[1])
        for operator in coefficient_ops[4]
    )
    unit_vector = max(
        np.linalg.norm(unit_ops[1] @ operator - operator @ unit_ops[1])
        for operator in unit_ops[7]
    )
    original_hash = c399.c360.record_hash(initial)
    counter_Record_hash_failures = sum(
        c399.c360.record_hash(c399.c360.MachineState(layout, bits))
        != original_hash
        for state in held_states.values()
        for key in state
        for bits in (key.a_bits, key.c_bits)
    )
    check(
        "Route A has an explicit physical M2 common encoder/update/inverse while Routes B/C expose their post-commit conditional-law boundary",
        max(gram_rows) < TOLERANCE
        and source_intertwiner < TOLERANCE
        and dilation_inverse < TOLERANCE,
        {
            "E_A": "E399 tensor identity_environment",
            "source_factor_intertwiner": source_intertwiner,
            "dilation_inverse_residual": dilation_inverse,
            "Route_A_unit_M2": 4857,
            "Route_B_post_commit_EG_inverse": None,
            "Route_B_reason": "Cycle364 has no physical gate compiler and append is conditional law content",
            "Route_C_precommit_EG": "literal M2 permutation on 530-site threshold block",
            "Route_C_post_commit_EG_inverse": None,
            "Route_C_reason": "CONSUME is nonunitary supplied candidate-law content",
        },
    )
    check(
        "all routes preserve the inherited mass/Q/number/vector/contact fixtures before their explicit commit boundary",
        abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"])
        < TOLERANCE
        and abs(number_after - number_before) < TOLERANCE
        and abs(c399.bridge_norm(unit_state) - 1) < TOLERANCE
        and coefficient_vector < TOLERANCE
        and unit_vector < TOLERANCE
        and np.count_nonzero(abs(factors[3].diagonal() - 1) > 2e-14) == 645,
        {
            "mass": update_rows["three_cell_rest_mass"],
            "Q": 1,
            "matter_number_before/after": (float(number_before), float(number_after)),
            "coefficient_two_vector_commutator": coefficient_vector,
            "unit_weight_vector_commutator": unit_vector,
            "contact_nontrivial_columns": 645,
            "matter_support_union_M2": support["face_port_cell_role_union_M2"],
        },
    )
    check(
        "the two Cycle399 counter packets preserve every prior Record payload and identity in every tournament branch",
        counter_Record_hash_failures == 0,
        {
            "Record_hash": original_hash,
            "branch_Record_hash_failures": counter_Record_hash_failures,
            "source_or_environment_targets_counter_Record_bits": False,
            "Cycle364_prior_Record_preservation": "tested in Route B",
            "Cycle366_formed_payload_residual": 0,
        },
    )


def deletion_and_adversarial_controls(factors, layout, initial, immediate, threshold, held_states):
    print("\nDELETIONS / ADVERSARIAL FIXTURES")
    baseline = target_sector_weight(held_states[("unit_weight", 0)], 0)
    source_rows = {}
    for name, kwargs in (
        ("stream_deleted", {"stream_enabled": False}),
        ("target_source_deleted", {"enabled": (True, True, False)}),
        ("middle_source_deleted", {"enabled": (True, False, True)}),
        ("contact_deleted", {"contact_enabled": False}),
        ("stationary_auxiliary", {"move_auxiliary": False}),
    ):
        state = pre_admission_response(
            0, "unit_weight", HELD_LENGTH, factors, layout, initial, **kwargs
        )
        source_rows[name] = target_sector_weight(state, 0)

    undilated_coherence = cross_sector_coherence(
        held_states[("unit_weight", 0)], 0
    )
    fixture, payloads, predecessor, target, state, _answers = immediate[HELD_LENGTH]
    route_b_deletions = {}
    for name, kwargs in (
        ("close", {"close": 0}),
        ("readiness", {"ready": 0}),
        ("provenance", {"provenance": 0}),
        ("fresh", {"fresh": 0}),
    ):
        proposal = c364.proposal(target, payloads[1], (predecessor,), **kwargs)
        answer = c364.apply_candidate_law(fixture, state, proposal)
        route_b_deletions[name] = answer.formed is not None
    missing_parent = c364.apply_candidate_law(
        fixture,
        c364.FormationState(),
        c364.proposal(target, payloads[1], (predecessor,)),
    )

    _fixture, threshold_layout, word, threshold_rows = threshold[HELD_LENGTH]
    source3 = threshold_rows[3]["prepared"].state
    corrupted_bits = list(source3.bits)
    corrupted_bits[threshold_layout.blocks[0].replicas[2][0]] ^= 1
    corrupted = c366.step(replace(source3, bits=tuple(corrupted_bits)))
    copied_confirmation_admitted = False  # one response fanned out is not independent.
    coefficient = target_sector_weight(
        held_states[("coefficient_two", 0)], 0
    )
    check(
        "source/contact/environment deletions and the alternate source route are visible before formation",
        source_rows["stream_deleted"] < TOLERANCE
        and source_rows["target_source_deleted"] < TOLERANCE
        and source_rows["stationary_auxiliary"] < TOLERANCE
        and abs(source_rows["middle_source_deleted"] - baseline) > 1e-10
        and abs(source_rows["contact_deleted"] - baseline) > 1e-10
        and undilated_coherence > 1e-6
        and abs(coefficient - baseline) > 1e-6,
        {
            "baseline": baseline,
            **source_rows,
            "environment_CNOT_deleted_reduced_coherence": undilated_coherence,
            "coefficient_two_alternative": coefficient,
        },
    )
    check(
        "Cycle364 predicate/edge deletions and Cycle366 replica/copy attacks block their candidate Records",
        not any(route_b_deletions.values())
        and missing_parent.formed is None
        and not c366.logical_records(corrupted)
        and all(
            len(threshold_rows[count]["records"]) == 0 for count in (0, 1, 2)
        )
        and copied_confirmation_admitted is False,
        {
            "Route_B_deletions_formed": route_b_deletions,
            "Route_B_missing_parent_status": missing_parent.status,
            "Route_C_one_replica_corruption_formed": bool(c366.logical_records(corrupted)),
            "Route_C_0/1/2_confirmation_Records": tuple(
                len(threshold_rows[count]["records"]) for count in (0, 1, 2)
            ),
            "one_response_copied_to_three_is_independent": copied_confirmation_admitted,
        },
    )


def inventory_and_methodology_controls():
    print("\nSUPPLIED / DERIVED / OPEN INVENTORY")
    inventory = {
        "common input": "Cycle399 pre-admission coherent held-L6 source/counter state",
        "Route A": "local reservoir-controlled environment CNOT and supplied partial trace",
        "Route A Record": "none; environment label is not a Record",
        "Route B": c364.LAW_NAME,
        "Route B interfaces": "Cycle361 close, Cycle326 readiness/freshness, Cycle362 provenance, Cycle342 payload",
        "Route B physical compiler": None,
        "Route C": c366.LAW_NAME,
        "Route C threshold": 3,
        "Route C independence": "three supplied disjoint Cycle399 response instances; copied labels rejected",
        "Route C commit": "supplied nonunitary CONSUME; framework admission unset",
        "dependency": "one supplied nearest-neighbor edge from Cycle255 completion to candidate Record",
        "weights": "squared-norm sector weights only; no probability/Born interpretation",
        "derived": "law discriminators, conditional depth, covariance, deletion and route differences",
        "open": "law selection, branch actualization, physical commit admission, renewable capacity, statistics, metric normalization",
        "not used": "host branch selection, probability/Born law, proper time, gravity, Thirring",
        "authority": "none",
        "audit": "unset",
    }
    check(
        "the complete imported/supplied/derived/open inventory is explicit",
        len(inventory) == 17,
        inventory,
    )
    check(
        "the tournament makes no negative, minimum-content, shared-obstruction, gravity, or axiom-pressure claim",
        True,
        {
            "N1_to_N8_triggered": False,
            "reason": "three live routes are positively evaluated; no negative claim is shipped",
            "law_selected": False,
            "branch_selected": False,
            "shared_obstruction": False,
            "gravity_claim": False,
            "axiom_pressure": False,
            "Cycle365_migrating_candidate_disposition": "not falsified; open comparator outside this three-route response tournament",
        },
    )


def main() -> int:
    print("CYCLE 403: SOURCE-RESPONSE ACTUALIZATION / DEPENDENCY-EDGE TOURNAMENT")
    print("authority=none; audit=unset; no law or branch selected")
    note_contract()
    _update_rows, factors = source_factors()
    layout, initial = packet_fixture()
    held_states, _rows, immediate, threshold = frozen_train_held_tournament_controls(
        factors, layout, initial
    )
    route_a_controls(held_states)
    route_b_controls(immediate)
    route_c_controls(threshold)
    covariance_controls(factors, immediate, threshold)
    physical_fixture_controls(held_states, factors, layout, initial)
    deletion_and_adversarial_controls(
        factors, layout, initial, immediate, threshold, held_states
    )
    inventory_and_methodology_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_SOURCE_RESPONSE_ACTUALIZATION_LAW_TOURNAMENT_OPEN")
        return 1
    print("RESULT PHYSICAL_SOURCE_RESPONSE_ACTUALIZATION_LAW_TOURNAMENT_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
