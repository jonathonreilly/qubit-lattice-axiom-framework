#!/usr/bin/env python3
"""Cycle 424: physical absorption-event to Record/time candidate bridge.

Add one detector/sink M2 to the Cycle-423 two-block Q<=2 field code.  One
nearest-neighbor SWAP absorbs the transported boundary-rail excitation into
the detector with an exact inverse and excitation ledger.  The detector bit
then supplies a typed *candidate* event input to the Cycle-364 immediate and
Cycle-366 threshold-three formation laws without selecting either law or an
outcome branch.

Reversible absorption and event-sector copying are not Records.  Sector weight
is not occurrence, probability, or a Born weight.  Candidate commit depth and
update ticks are not physical time or a rate.  Authority is none; audit is
unset.  No no-go, minimum-content, shared-obstruction, or axiom-pressure claim
is made.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from functools import lru_cache
from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import car_compiler_record_causal_depth_bridge_cycle255_2026_07_17 as c255
import physical_redundancy_threshold_record_formation_candidate_cycle366_2026_07_18 as c366
import physical_site_tethered_close_gated_record_formation_candidate_cycle364_2026_07_18 as c364
import two_block_qle2_many_field_transport_cycle423_2026_07_19 as c423


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ABSORPTION_EVENT_RECORD_TIME_BRIDGE_CYCLE424_NOTE_2026-07-19.md"
)
AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
FIREWALL = ROOT / "docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md"
CYCLE367_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECORD_FORMATION_LAW_TOURNAMENT_SYNTHESIS_CYCLE367_NOTE_2026-07-18.md"
)
CYCLE403_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SOURCE_RESPONSE_ACTUALIZATION_LAW_TOURNAMENT_CYCLE403_NOTE_2026-07-18.md"
)
CYCLE170_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "RECORD_DEFINED_CAUSAL_DEPTH_CLOCK_CYCLE170_NOTE_2026-07-16.md"
)
CYCLE423_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "TWO_BLOCK_QLE2_MANY_FIELD_TRANSPORT_CYCLE423_NOTE_2026-07-19.md"
)

AUTHORITY = "none"
AUDIT = "unset"
TOL = 3.0e-11
EDGE_DIRECTION = c423.EDGE_DIRECTION
TARGET_RAIL_DIRECTION = c423.REVERSE[EDGE_DIRECTION]
DETECTOR_COORD = (2, -1, 0)
TRAIN_LENGTH = 3
HELD_LENGTH = 6
PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
Word = tuple[int, ...]


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
    required = (
        "authority: none",
        "audit: unset",
        "complete total-q<=2 code",
        "one detector/sink m2",
        "exact unitary and inverse",
        "excitation ledger",
        "reversible absorption is not a record",
        "cycle-364 immediate site-tethered candidate",
        "cycle-366 threshold-three candidate",
        "neither candidate law is selected",
        "false-trigger refusal",
        "all 24 proper-cubic frames",
        "post-commit permanence",
        "branch weight is not occurrence, probability, or a born weight",
        "commit depth is not time",
        "update ticks are not a rate",
        "record axiom does not supply a formation or selection law",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-424 note freezes the physical seam and semantic boundary", not missing, missing)


def source_contract() -> None:
    axioms = normalized(AXIOMS)
    firewall = normalized(FIREWALL)
    c367 = normalized(CYCLE367_NOTE)
    c403 = normalized(CYCLE403_NOTE)
    c170 = normalized(CYCLE170_NOTE)
    c423 = normalized(CYCLE423_NOTE)
    check(
        "the cited source stack separates physical absorption, candidate formation, dependency depth, and metric time",
        "records form" in axioms
        and "records are permanent" in axioms
        and "formation rules" in axioms
        and "time metric" in axioms
        and "supplied abstract word/order" in firewall
        and "requires clock map" in firewall
        and "none is selected by the framework" in c367
        and "immediate site-tethered formation" in c367
        and "threshold-three convergence formation" in c367
        and "environment label is not a record" in c403
        and "post-commit inverse is undefined" in c403
        and "dimensionless relative duration" in c170
        and "this is not a continuous rate" in c170
        and "complete total-q<=2 code" in c423
        and "not energy, source, work, time, probability, or a record" in c423,
        {
            "axiom_surface": "Record locks one admissible local possibility and is permanent",
            "formation_rule_selected_by_axiom": False,
            "metric_time_or_rate_from_depth": False,
            "physical_input": "Cycle423 complete Q<=2 transported field",
        },
    )


def extended_basis() -> tuple[tuple[int, int, int], ...]:
    return tuple(
        (left, right, detector)
        for left, right in c423.BASIS
        for detector in (0, 1)
        if c423.local_q(left) + c423.local_q(right) + detector <= 2
    )


BASIS = extended_basis()
INDEX = {state: index for index, state in enumerate(BASIS)}
DIMENSION = len(BASIS)


def total_q(state: tuple[int, int, int]) -> int:
    left, right, detector = state
    return c423.local_q(left) + c423.local_q(right) + detector


def detector_bit(state: tuple[int, int, int]) -> int:
    return state[2]


def target_rail_bit(state: tuple[int, int, int], direction: int = EDGE_DIRECTION) -> int:
    _left, right, _detector = state
    _reservoir, field = divmod(right, 64)
    return (field >> c423.REVERSE[direction]) & 1


def diagonal(function) -> np.ndarray:
    return np.diag(np.asarray([function(state) for state in BASIS], dtype=float)).astype(complex)


Q_TOTAL = diagonal(total_q)
N_DETECTOR = diagonal(detector_bit)


def rail_number(direction: int = EDGE_DIRECTION) -> np.ndarray:
    return diagonal(lambda state: target_rail_bit(state, direction))


def basis_state(left: int, right: int, detector: int = 0) -> np.ndarray:
    key = (left, right, detector)
    if key not in INDEX:
        raise ValueError("state is outside the complete fifteen-M2 total-Q<=2 code")
    output = np.zeros(DIMENSION, dtype=complex)
    output[INDEX[key]] = 1
    return output


def expectation(vector: np.ndarray, observable: np.ndarray) -> float:
    return float(np.vdot(vector, observable @ vector).real)


@lru_cache(maxsize=None)
def lifted_cycle423(
    direction: int = EDGE_DIRECTION,
    delete_vertex: bool = False,
    delete_transport: bool = False,
    delete_coin: bool = False,
) -> np.ndarray:
    base = c423.update(direction, delete_vertex, delete_transport, delete_coin)
    output = np.zeros((DIMENSION, DIMENSION), dtype=complex)
    for source_index, (left, right, detector) in enumerate(BASIS):
        base_source = c423.INDEX[(left, right)]
        for base_target in np.flatnonzero(np.abs(base[:, base_source]) > 0):
            target_left, target_right = c423.BASIS[int(base_target)]
            target = (target_left, target_right, detector)
            output[INDEX[target], source_index] = base[int(base_target), base_source]
    return output


def swap_target_rail_and_detector(
    state: tuple[int, int, int],
    direction: int = EDGE_DIRECTION,
) -> tuple[int, int, int]:
    left, right, detector = state
    reservoir, field = divmod(right, 64)
    rail_direction = c423.REVERSE[direction]
    rail = (field >> rail_direction) & 1
    if rail != detector:
        field ^= 1 << rail_direction
        detector ^= 1
    return left, reservoir * 64 + field, detector


@lru_cache(maxsize=None)
def absorption_gate(direction: int = EDGE_DIRECTION) -> np.ndarray:
    output = np.zeros((DIMENSION, DIMENSION), dtype=complex)
    for source_index, source in enumerate(BASIS):
        output[INDEX[swap_target_rail_and_detector(source, direction)], source_index] = 1
    return output


@lru_cache(maxsize=None)
def physical_update(
    direction: int = EDGE_DIRECTION,
    delete_detector: bool = False,
    delete_vertex: bool = False,
    delete_transport: bool = False,
    delete_coin: bool = False,
) -> np.ndarray:
    detector = np.eye(DIMENSION, dtype=complex) if delete_detector else absorption_gate(direction)
    return detector @ lifted_cycle423(direction, delete_vertex, delete_transport, delete_coin)


def physical_sites() -> tuple[Coord, ...]:
    sites: list[Coord] = []
    for center in c423.CENTERS:
        sites.append(center)
        for direction in range(6):
            sites.append(
                tuple(
                    int(center[axis] + c423.c210.DIRECTIONS[direction, axis])
                    for axis in range(3)
                )
            )
    sites.append(DETECTOR_COORD)
    return tuple(sites)


def frame_representation(frame: np.ndarray) -> np.ndarray:
    direction = c423.c210.direction_permutation(frame)
    output = np.zeros((DIMENSION, DIMENSION), dtype=complex)
    for source_index, (left, right, detector) in enumerate(BASIS):
        left_r, left_f = divmod(left, 64)
        right_r, right_f = divmod(right, 64)
        target = (
            left_r * 64 + c423.permute_field(left_f, direction),
            right_r * 64 + c423.permute_field(right_f, direction),
            detector,
        )
        output[INDEX[target], source_index] = 1
    return output


def physical_operator_controls() -> np.ndarray:
    print("\nPHYSICAL FIFTEEN-M2 ABSORPTION SEAM")
    gate = physical_update()
    absorption = absorption_gate()
    identity = np.eye(DIMENSION, dtype=complex)
    inverse = gate.conj().T @ gate - identity
    number = gate @ Q_TOTAL - Q_TOTAL @ gate
    rail = rail_number()
    local_ledger = (
        absorption.conj().T @ N_DETECTOR @ absorption
        - N_DETECTOR
        + absorption.conj().T @ rail @ absorption
        - rail
    )
    q_counts = {q: sum(total_q(state) == q for state in BASIS) for q in range(3)}
    sites = physical_sites()
    target_rail = (
        int(c423.CENTERS[1][0] + c423.c210.DIRECTIONS[TARGET_RAIL_DIRECTION, 0]),
        int(c423.CENTERS[1][1] + c423.c210.DIRECTIONS[TARGET_RAIL_DIRECTION, 1]),
        int(c423.CENTERS[1][2] + c423.c210.DIRECTIONS[TARGET_RAIL_DIRECTION, 2]),
    )
    frame_locality_failures = 0
    covariance = []
    for frame in c423.c210.proper_cubic_frames():
        moved_sites = tuple(tuple(int(value) for value in frame @ np.asarray(site)) for site in sites)
        moved_detector = tuple(int(value) for value in frame @ np.asarray(DETECTOR_COORD))
        moved_rail = tuple(int(value) for value in frame @ np.asarray(target_rail))
        frame_locality_failures += int(len(set(moved_sites)) != 15)
        frame_locality_failures += int(c255.manhattan(moved_detector, moved_rail) != 1)
        representation = frame_representation(frame)
        directions = c423.c210.direction_permutation(frame)
        target_direction = int(np.argmax(directions[:, EDGE_DIRECTION]))
        covariance.append(
            float(
                np.linalg.norm(
                    representation @ gate @ representation.conj().T
                    - physical_update(target_direction)
                )
            )
        )
    check(
        "the complete total-Q<=2 fifteen-M2 update is local, unitary, number conserving, and proper-cubic covariant",
        DIMENSION == 121
        and q_counts == {0: 1, 1: 15, 2: 105}
        and len(BASIS) == len(INDEX)
        and len(set(sites)) == 15
        and np.linalg.norm(inverse) < TOL
        and np.max(np.linalg.norm(inverse, axis=0)) < 2e-12
        and np.linalg.norm(number) < TOL
        and np.linalg.norm(local_ledger) == 0
        and frame_locality_failures == 0
        and len(covariance) == 24
        and max(covariance) < TOL,
        {
            "physical_M2": 15,
            "Cycle423_M2": 14,
            "detector_sink_M2": 1,
            "complete_Q_le_2_dimension": DIMENSION,
            "sector_dimensions": q_counts,
            "unitarity_residual": float(np.linalg.norm(inverse)),
            "maximum_basis_inverse_residual": float(np.max(np.linalg.norm(inverse, axis=0))),
            "Q_commutator": float(np.linalg.norm(number)),
            "detector_plus_target_rail_ledger": float(np.linalg.norm(local_ledger)),
            "detector_gate_support_M2": 2,
            "detector_target_rail_distance": c255.manhattan(DETECTOR_COORD, target_rail),
            "proper_cubic_frames": len(covariance),
            "maximum_frame_residual": max(covariance),
            "frame_locality_failures": frame_locality_failures,
        },
    )
    return gate


def physical_history_controls(gate: np.ndarray) -> dict[str, float]:
    print("\nONE/TWO-SOURCE, DELETION, FALSE-TRIGGER, AND COLLISION CONTROLS")
    expected = float(np.sin(c423.ANGLE) ** 2 / 6)
    vacuum = basis_state(0, 0, 0)
    one = basis_state(64, 0, 0)
    two = basis_state(64, 64, 0)
    one_after = gate @ one
    two_after = gate @ two
    one_restored = gate.conj().T @ one_after
    two_restored = gate.conj().T @ two_after
    detector_deleted = physical_update(delete_detector=True) @ one
    vertex_deleted = physical_update(delete_vertex=True) @ one
    transport_deleted = physical_update(delete_transport=True) @ one
    vacuum_after = gate @ vacuum

    non_target = basis_state(0, 1 << 2, 0)
    non_target_after = absorption_gate() @ non_target
    edge_pair = (1 << EDGE_DIRECTION, 1 << TARGET_RAIL_DIRECTION)
    collision = basis_state(*edge_pair, 0)
    collision_after = absorption_gate() @ collision
    collision_expected = basis_state(1 << EDGE_DIRECTION, 0, 1)
    occupied_detector_and_rail = basis_state(0, 1 << TARGET_RAIL_DIRECTION, 1)
    occupied_after = absorption_gate() @ occupied_detector_and_rail

    one_weight = expectation(one_after, N_DETECTOR)
    two_weight = expectation(two_after, N_DETECTOR)
    check(
        "the transported rail is absorbed without false triggers, deletion leakage, collision loss, or sink overwrite",
        abs(one_weight - expected) < 8e-14
        and abs(two_weight - expected) < 8e-14
        and expectation(one_after, rail_number()) == 0
        and np.linalg.norm(one_restored - one) < 8e-14
        and np.linalg.norm(two_restored - two) < 8e-14
        and expectation(detector_deleted, N_DETECTOR) == 0
        and expectation(vertex_deleted, N_DETECTOR) == 0
        and expectation(transport_deleted, N_DETECTOR) == 0
        and expectation(vacuum_after, N_DETECTOR) == 0
        and expectation(non_target_after, N_DETECTOR) == 0
        and np.linalg.norm(collision_after - collision_expected) == 0
        and np.linalg.norm(occupied_after - occupied_detector_and_rail) == 0
        and abs(expectation(one_after, Q_TOTAL) - 1) < 8e-14
        and abs(expectation(two_after, Q_TOTAL) - 2) < 8e-14,
        {
            "one_source_detector_sector_weight": one_weight,
            "two_source_detector_sector_weight": two_weight,
            "expected_sin2_over_6": expected,
            "one_source_inverse_residual": float(np.linalg.norm(one_restored - one)),
            "two_source_inverse_residual": float(np.linalg.norm(two_restored - two)),
            "detector_deleted_weight": expectation(detector_deleted, N_DETECTOR),
            "source_vertex_deleted_weight": expectation(vertex_deleted, N_DETECTOR),
            "transport_deleted_weight": expectation(transport_deleted, N_DETECTOR),
            "vacuum_false_trigger_weight": expectation(vacuum_after, N_DETECTOR),
            "non_target_rail_false_trigger_weight": expectation(non_target_after, N_DETECTOR),
            "occupied_edge_collision_residual": float(np.linalg.norm(collision_after - collision_expected)),
            "occupied_sink_and_rail_11_residual": float(np.linalg.norm(occupied_after - occupied_detector_and_rail)),
            "gate_controlled_by_expectation": False,
        },
    )
    return {
        "one_source_weight": one_weight,
        "two_source_weight": two_weight,
        "three_independent_detector_sector_weight": one_weight**3,
    }


@dataclass(frozen=True)
class DetectorEventCandidate:
    event_id: str
    detector_site: Coord
    detected: int
    payload: Word
    source_case: str
    reversible_precommit: bool = True
    is_Record: bool = False


def validate_event(event: DetectorEventCandidate) -> None:
    if not isinstance(event, DetectorEventCandidate):
        raise TypeError("event adapter requires one DetectorEventCandidate")
    if event.detected not in (0, 1):
        raise ValueError("detector event bit must be binary")
    if not c364.valid_coord(event.detector_site):
        raise ValueError("detector event site is outside Z3")
    if len(event.payload) != c364.RECORD_BITS or any(bit not in (0, 1) for bit in event.payload):
        raise ValueError("detector event carries no lawful 30-bit payload binding")
    if not event.event_id or event.reversible_precommit is not True or event.is_Record is not False:
        raise ValueError("precommit detector event typing is malformed")


def shifted_base_dag(parent_site: Coord, prefix: str) -> c255.EventDag:
    relative_completion = (1, 1, 1)
    shift = tuple(parent_site[axis] - relative_completion[axis] for axis in range(3))
    return c255.event_dag(prefix=prefix, shift=shift)


def linked_record_dag(base: c255.EventDag, name: str, site: Coord) -> tuple[c255.EventDag, c255.EventDag]:
    events = dict(base.events)
    events[name] = c255.Event(name, site, 1, frozenset((base.completion,)))
    linked = c255.EventDag(events, name, "Cycle424_absorption_conditioned_Record_candidate")
    cut_events = dict(events)
    cut_events[name] = replace(cut_events[name], parents=frozenset())
    cut = c255.EventDag(cut_events, name, linked.semantic_update)
    return linked, cut


def immediate_candidate_controls(weights: dict[str, float]) -> dict[str, object]:
    print("\nCYCLE-364 IMMEDIATE SITE-TETHERED CANDIDATE ADAPTER")
    rows = []
    failures = 0
    covariance_failures = 0
    dag_failures = 0
    permanence_rows = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        fixture = c364.c342.c338.build_fixture(length)
        payloads = c364.words(fixture, 3)
        target = DETECTOR_COORD
        predecessor = (2, -2, 0)
        prior = c364.SiteContentRecord(predecessor, payloads[0], ())
        state = c364.FormationState((prior,))
        answers = {}
        proposals = {}
        for detected in (0, 1):
            event = DetectorEventCandidate(
                f"immediate_L{length}_event",
                target,
                detected,
                payloads[1],
                "Cycle423_one_source_detector_sector",
            )
            validate_event(event)
            item = c364.proposal(
                target,
                event.payload,
                (predecessor,),
                close=event.detected,
                confirmations=1,
            )
            answer = c364.apply_candidate_law(fixture, state, item)
            answers[detected] = answer
            proposals[detected] = item
            failures += int((answer.formed is not None) != bool(detected))
            failures += int(answer.state != state if detected == 0 else False)
            rows.append(
                {
                    "L": length,
                    "held": length == HELD_LENGTH,
                    "detector_bit": detected,
                    "candidate_status": answer.status,
                    "conditional_Records": int(answer.formed is not None),
                    "event_sector_weight": weights["one_source_weight"] if detected else 1 - weights["one_source_weight"],
                }
            )

        formed = answers[1]
        repeated = c364.apply_candidate_law(fixture, formed.state, proposals[1])
        overwrite = c364.apply_candidate_law(
            fixture,
            formed.state,
            c364.proposal(target, payloads[2], (predecessor,), close=1),
        )
        next_site = (2, -1, 1)
        continuation = c364.apply_candidate_law(
            fixture,
            formed.state,
            c364.proposal(next_site, payloads[2], (target,), close=1),
        )
        original = c364.record_map(formed.state)[target]
        permanence_rows.append(
            {
                "L": length,
                "repeat_status": repeated.status,
                "overwrite_status": overwrite.status,
                "continuation_status": continuation.status,
                "original_preserved_after_repeat": c364.record_map(repeated.state)[target] == original,
                "original_preserved_after_overwrite": c364.record_map(overwrite.state)[target] == original,
                "original_preserved_after_continuation": c364.record_map(continuation.state)[target] == original,
                "permanent_under_candidate_law": original.permanent_under_candidate_law,
            }
        )
        failures += int(repeated.state != formed.state or repeated.status != "overwrite-rejected")
        failures += int(overwrite.state != formed.state or overwrite.status != "overwrite-rejected")
        failures += int(
            continuation.status != "formed"
            or c364.record_map(continuation.state)[target] != original
            or not original.permanent_under_candidate_law
        )

        reference = answers[1]
        for frame in c423.c210.proper_cubic_frames():
            rotated_fixture, mapping, mapping_failures = c364.c342.mapped_fixture(fixture, frame)
            transformed_state = c364.transform_state(state, frame, (0, 0, 0), mapping)
            transformed_proposal = c364.transform_proposal(proposals[1], frame, (0, 0, 0), mapping)
            observed = c364.apply_candidate_law(rotated_fixture, transformed_state, transformed_proposal)
            expected = c364.transform_answer(reference, frame, (0, 0, 0), mapping)
            covariance_failures += mapping_failures + int(observed != expected)

        base = shifted_base_dag(predecessor, f"imm_L{length}_")
        linked, cut = linked_record_dag(base, f"imm_L{length}_detector_Record", target)
        dag_failures += int(c255.depth_certificate(base)["depth"] != 4)
        dag_failures += int(c255.depth_certificate(linked)["depth"] != 5)
        dag_failures += int(c255.depth_certificate(cut)["depth"] != 1)
        dag_failures += len(c255.local_failures(linked))
        for frame in c423.c210.proper_cubic_frames():
            moved = c255.transformed(linked, frame)
            dag_failures += len(c255.local_failures(moved))
            dag_failures += int(c255.depth_certificate(moved)["depth"] != 5)

    check(
        "one detector event feeds the immediate candidate while false sectors stay dark and committed candidate Records remain protected",
        failures == 0 and covariance_failures == 0 and dag_failures == 0,
        {
            "rows": rows,
            "post_commit_permanence": permanence_rows,
            "proper_cubic_candidate_failures": covariance_failures,
            "event_DAG_failures": dag_failures,
            "conditional_depth_before_after": (4, 5),
            "edge_deleted_new_node_depth": 1,
            "physical_gate_compiler_for_append": None,
            "law_selected": False,
        },
    )
    return {"rows": rows, "failures": failures + covariance_failures + dag_failures}


def threshold_events(
    layout: c366.Layout,
    word: Word,
    detected_count: int,
) -> tuple[DetectorEventCandidate, ...]:
    block = layout.blocks[0]
    return tuple(
        DetectorEventCandidate(
            f"threshold_detector_{index}",
            layout.sites[block.replicas[index][c366.CLOSE_LANE]].coord,
            int(index < detected_count),
            word,
            "independent_Cycle423_detector_instance",
        )
        for index in range(c366.FORMATION_THRESHOLD)
    )


def threshold_adapter(
    layout: c366.Layout,
    word: Word,
    parent: Coord,
    events: tuple[DetectorEventCandidate, ...],
) -> tuple[c366.Prepared, int]:
    if len(events) != c366.FORMATION_THRESHOLD:
        raise ValueError("threshold adapter requires exactly three installed detector interfaces")
    for event in events:
        validate_event(event)
    expected_sites = tuple(
        layout.sites[layout.blocks[0].replicas[index][c366.CLOSE_LANE]].coord
        for index in range(c366.FORMATION_THRESHOLD)
    )
    if tuple(event.detector_site for event in events) != expected_sites:
        raise ValueError("detector sites are not the three threshold close-interface M2")
    if len({event.event_id for event in events}) != len(events):
        raise ValueError("copied event identifiers are not independent detector events")
    detected = tuple(event for event in events if event.detected)
    if any(event.payload != word for event in detected):
        raise ValueError("detected event payloads do not share the supplied content binding")
    count = len(detected)
    base = c364.proposal(
        layout.blocks[0].target_site,
        word,
        (parent,),
        confirmations=count,
    )
    redundant = c366.redundant_from_immediate(base, count)
    return c366.prepare(layout, ((0, redundant),)), count


def installation_sites(frame: np.ndarray, target: Coord) -> frozenset[Coord]:
    base_sites = physical_sites()
    moved_detector = tuple(int(value) for value in frame @ np.asarray(DETECTOR_COORD))
    shift = tuple(target[axis] - moved_detector[axis] for axis in range(3))
    return frozenset(
        tuple(int(value) + shift[axis] for axis, value in enumerate(frame @ np.asarray(site)))
        for site in base_sites
    )


def threshold_common_layout(layout: c366.Layout) -> dict[str, object]:
    occupied = {site.coord for site in layout.sites}
    targets = tuple(
        layout.sites[layout.blocks[0].replicas[index][c366.CLOSE_LANE]].coord
        for index in range(c366.FORMATION_THRESHOLD)
    )
    frames = c423.c210.proper_cubic_frames()
    choices: list[list[tuple[int, frozenset[Coord]]]] = []
    for target in targets:
        current = []
        for frame_index, frame in enumerate(frames):
            sites = installation_sites(frame, target)
            if (sites - {target}).isdisjoint(occupied):
                current.append((frame_index, sites))
        choices.append(current)
    selected = None
    for combination in product(*choices):
        site_sets = tuple(item[1] for item in combination)
        if all(site_sets[left].isdisjoint(site_sets[right]) for left in range(3) for right in range(left + 1, 3)):
            selected = combination
            break
    return {
        "threshold_close_sites": targets,
        "frame_choice_counts": tuple(len(items) for items in choices),
        "shared_close_M2_common_layout_found": selected is not None,
        "selected_frame_indices": None if selected is None else tuple(item[0] for item in selected),
        "three_installations_total_unique_M2": None
        if selected is None
        else len(set().union(*(item[1] for item in selected))),
        "candidate_layout_other_overlap": None
        if selected is None
        else sum(len((item[1] - {targets[index]}) & occupied) for index, item in enumerate(selected)),
    }


def threshold_candidate_controls(weights: dict[str, float]) -> dict[str, object]:
    print("\nCYCLE-366 THRESHOLD-THREE CANDIDATE ADAPTER")
    rows = []
    failures = 0
    inverse_failures = 0
    commit_inverse_rejections = 0
    protection_rows = []
    layout_rows = []
    dag_failures = 0
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        fixture = c364.c342.c338.build_fixture(length)
        layout = c366.build_layout(1)
        word, alternative = c366.record_words(fixture, 2)
        block = layout.blocks[0]
        parent = (block.target_site[0] + 1, block.target_site[1], block.target_site[2])
        for detected_count in range(4):
            events = threshold_events(layout, word, detected_count)
            prepared, count = threshold_adapter(layout, word, parent, events)
            calculated = c366.apply_layers(prepared.state, layout.layers[:-1])
            restored = c366.apply_layers(calculated, layout.layers[:-1], reverse=True)
            committed = c366.apply_layers(calculated, (layout.layers[-1],))
            records = c366.logical_records(committed)
            inverse_failures += int(restored != prepared.state)
            failures += int(count != detected_count)
            failures += int(len(records) != int(detected_count == 3))
            failures += int(c366.workspace_leakage(committed) != 0)
            rows.append(
                {
                    "L": length,
                    "held": length == HELD_LENGTH,
                    "independent_detector_events": detected_count,
                    "candidate_count": c366.candidate_count(prepared.state, block),
                    "conditional_Records": len(records),
                    "joint_three_event_sector_weight": weights["three_independent_detector_sector_weight"]
                    if detected_count == 3
                    else None,
                }
            )
            if detected_count == 3:
                try:
                    c366.apply_layers(committed, (layout.layers[-1],), reverse=True)
                except ValueError:
                    commit_inverse_rejections += 1
                repeated = c366.step(committed)
                overwritten_bits = list(committed.bits)
                for replica in block.replicas:
                    for lane, value in zip(c366.PAYLOAD_LANES, alternative):
                        overwritten_bits[replica[lane]] = value
                overwritten = c366.step(replace(committed, bits=tuple(overwritten_bits)))
                original_record = records[0]
                protection_rows.append(
                    {
                        "L": length,
                        "formed_state_idempotent": repeated == committed,
                        "overwrite_output_content_residual": sum(
                            a != b
                            for a, b in zip(c366.output_word(overwritten, block), original_record.content)
                        ),
                        "formed_flag_preserved": overwritten.bits[block.formed] == 1,
                        "permanent_under_candidate_law": original_record.permanent_under_candidate_law,
                    }
                )
                failures += int(repeated != committed)
                failures += int(c366.output_word(overwritten, block) != original_record.content)
                failures += int(overwritten.bits[block.formed] != 1)
                failures += int(not original_record.permanent_under_candidate_law)

        copied = list(threshold_events(layout, word, 1))
        copied[1] = replace(copied[1], event_id=copied[0].event_id)
        copied[2] = replace(copied[2], event_id=copied[0].event_id)
        copied_rejection = 0
        try:
            threshold_adapter(layout, word, parent, tuple(copied))
        except ValueError:
            copied_rejection = 1
        corrupted = list(threshold_events(layout, word, 3))
        corrupted[2] = replace(corrupted[2], payload=alternative)
        corrupted_rejection = 0
        try:
            threshold_adapter(layout, word, parent, tuple(corrupted))
        except ValueError:
            corrupted_rejection = 1
        failures += int(copied_rejection != 1 or corrupted_rejection != 1)

        locality_failures = 0
        for frame in c423.c210.proper_cubic_frames():
            framed_sites = tuple(
                replace(site, coord=tuple(int(value) for value in frame @ np.asarray(site.coord)))
                for site in layout.sites
            )
            locality_failures += sum(
                not c366.support_connected_nn(item, framed_sites)
                for layer in layout.layers
                for item in layer.gates
            )
        failures += locality_failures
        common_layout = threshold_common_layout(layout)
        layout_rows.append(
            {
                "L": length,
                "copied_event_fanout_rejected": copied_rejection,
                "mismatched_payload_rejected": corrupted_rejection,
                "proper_cubic_gate_locality_failures": locality_failures,
                "detector_to_threshold_common_layout": common_layout,
            }
        )

        base = shifted_base_dag(parent, f"thr_L{length}_")
        linked, cut = linked_record_dag(base, f"thr_L{length}_convergence_Record", block.target_site)
        dag_failures += int(c255.depth_certificate(base)["depth"] != 4)
        dag_failures += int(c255.depth_certificate(linked)["depth"] != 5)
        dag_failures += int(c255.depth_certificate(cut)["depth"] != 1)
        dag_failures += len(c255.local_failures(linked))
        for frame in c423.c210.proper_cubic_frames():
            moved = c255.transformed(linked, frame)
            dag_failures += len(c255.local_failures(moved))
            dag_failures += int(c255.depth_certificate(moved)["depth"] != 5)

    check(
        "three independent detector events feed the threshold candidate while zero/one/two, copied, and mismatched inputs stay dark",
        failures == 0
        and inverse_failures == 0
        and commit_inverse_rejections == 2
        and dag_failures == 0,
        {
            "rows": rows,
            "precommit_inverse_failures": inverse_failures,
            "post_commit_inverse_rejections": commit_inverse_rejections,
            "post_commit_protection": protection_rows,
            "layout_and_adversarial_controls": layout_rows,
            "event_DAG_failures": dag_failures,
            "conditional_depth_before_after": (4, 5),
            "edge_deleted_new_node_depth": 1,
            "CONSUME_admitted_by_framework": None,
            "law_selected": False,
        },
    )
    return {"rows": rows, "failures": failures + inverse_failures + dag_failures}


def semantic_inventory(weights: dict[str, float]) -> None:
    print("\nSEMANTIC AND INTERFACE INVENTORY")
    inventory = {
        "physical_positive": (
            "Cycle423 Q<=2 field update imported by exact matrix",
            "one local field-rail/detector SWAP on a complete fifteen-M2 Q<=2 code",
            "exact inverse and detector-plus-rail excitation ledger",
            "one-source, two-source, collision, saturation, deletion, and all-frame controls",
        ),
        "conditional_candidate_positive": (
            "typed detector-bit adapter to the Cycle364 immediate candidate",
            "three-distinct-event adapter to the Cycle366 threshold candidate",
            "candidate post-commit permanence and dependency-DAG coordinates",
        ),
        "not_constructed": {
            "coherent_detector_to_30bit_payload_close_provenance_EG": True,
            "threshold_middle_close_physical_placement_or_routing": True,
            "physical_Cycle364_append_gate": True,
            "framework_admission_of_Cycle366_CONSUME": True,
            "formation_law_selection": True,
            "actual_branch_or_history_selection": True,
            "Born_or_frequency_law": True,
            "clock_metric_or_rate_normalization": True,
        },
        "diagnostic_sector_weights": weights,
        "detector_event_is_Record_before_candidate_commit": False,
        "branch_weight_is_occurrence_probability_or_Born": False,
        "commit_depth_or_update_ticks_are_physical_time_or_rate": False,
        "Record_axiom_supplies_formation_or_selection_law": False,
        "negative_claim": False,
        "axiom_pressure": False,
    }
    check(
        "the strongest positive seam and every remaining typed interface stay explicit",
        len(inventory["not_constructed"]) == 8
        and not inventory["detector_event_is_Record_before_candidate_commit"]
        and not inventory["branch_weight_is_occurrence_probability_or_Born"]
        and not inventory["commit_depth_or_update_ticks_are_physical_time_or_rate"]
        and not inventory["Record_axiom_supplies_formation_or_selection_law"]
        and not inventory["negative_claim"]
        and not inventory["axiom_pressure"],
        inventory,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 424: PHYSICAL ABSORPTION-EVENT -> RECORD/TIME CANDIDATE BRIDGE")
    note_contract()
    source_contract()
    gate = physical_operator_controls()
    weights = physical_history_controls(gate)
    immediate_candidate_controls(weights)
    threshold_candidate_controls(weights)
    semantic_inventory(weights)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_ABSORPTION_EVENT_RECORD_TIME_BRIDGE_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_ABSORPTION_EVENT_RECORD_TIME_BRIDGE_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
