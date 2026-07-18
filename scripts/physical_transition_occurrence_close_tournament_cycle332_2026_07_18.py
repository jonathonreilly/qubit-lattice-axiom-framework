#!/usr/bin/env python3
"""Cycle 332: transition-sensitive occurrence/close predicate tournament.

The runner starts from the exact Cycle-314 event-flipping stream permutation
and Cycle-329's physical matcher/readiness outputs.  It tests a reversible
two-boundary transition witness, a relational close certificate, and protected
prior-candidate inputs.  A witness remains conditional on supplied boundary
registers; a candidate is not promoted to Record or permanence.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import contact_close_typed_record_dag_cycle287_2026_07_17 as c287
import physical_support_matcher_predecessor_controls_cycle329_2026_07_18 as c329


c326 = c329.c326
c314 = c329.c314
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_TRANSITION_OCCURRENCE_CLOSE_TOURNAMENT_CYCLE332_NOTE_2026-07-18.md"
)
TOL = 1.2e-11
SOURCE_PATCH_M2 = 45
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-332 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "transition-sensitive reversible occurrence witness",
        "relational two-boundary close certificate",
        "protected-history predecessor route",
        "actual cycle-314 event transition",
        "cycle-329 matcher and readiness",
        "readiness alone cannot close",
        "false event",
        "anti-splice",
        "deletion",
        "held l=6",
        "all 24 proper-cubic frames",
        "two boundary registers remain supplied",
        "occurrence witness is not a selected actual member",
        "commit candidate is not a record",
        "forward nonreturn is not permanence",
        "reversibility and capacity",
        "broad gate status: fail / do not ship",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the three occurrence/close routes and semantic firewall",
        not missing,
        missing,
    )


@dataclass(frozen=True)
class TransitionProgram:
    length: int
    sidecar: object
    active_rows: np.ndarray
    nonvacuum: np.ndarray
    truth: np.ndarray


def compile_transition_program(length: int, deleted: bool = False) -> TransitionProgram:
    if length not in (3, 6):
        raise ValueError("Cycle-332 transition program is declared only at L=3 and L=6")
    sidecar = c314.build_event_sidecar(c314.c311.c269.build_code(length))
    ambient = len(sidecar.stream_mapping)
    active = np.flatnonzero(np.linalg.norm(sidecar.event_encoding, axis=1) > TOL)
    physical_numbers = sidecar.numbers[np.arange(ambient) // 2]
    nonvacuum = physical_numbers > 0
    truth = np.zeros(ambient * ambient, dtype=np.uint8)
    if not deleted:
        source = np.arange(ambient)[nonvacuum]
        truth[source * ambient + sidecar.stream_mapping[source]] = 1
    return TransitionProgram(length, sidecar, active, nonvacuum, truth)


def transition_full_mapping(program: TransitionProgram) -> np.ndarray:
    pair = np.arange(len(program.truth), dtype=np.int32)
    full = np.empty(2 * len(pair), dtype=np.int32)
    full[2 * pair] = 2 * pair + program.truth
    full[2 * pair + 1] = 2 * pair + (1 - program.truth)
    return full


def transition_witness(
    program: TransitionProgram,
    pre: int,
    post: int,
    witness: int = 0,
) -> int:
    ambient = len(program.sidecar.stream_mapping)
    if not 0 <= pre < ambient or not 0 <= post < ambient or witness not in (0, 1):
        raise ValueError("transition boundary labels and witness are outside the declared domain")
    pair = pre * ambient + post
    return int(witness ^ int(program.truth[pair]))


def transition_program_controls() -> dict[int, TransitionProgram]:
    programs = {}
    rows = []
    for length in (3, 6):
        program = compile_transition_program(length)
        programs[length] = program
        sidecar = program.sidecar
        ambient = len(sidecar.stream_mapping)
        active = program.active_rows
        active_set = set(map(int, active))
        active_nonvac = active[program.nonvacuum[active]]
        active_vacuum = active[~program.nonvacuum[active]]
        mapped = sidecar.stream_mapping[active]
        code_preserved = all(int(row) in active_set for row in mapped)
        lawful_truth = np.asarray(
            [transition_witness(program, int(pre), int(sidecar.stream_mapping[pre])) for pre in active]
        )
        expected = program.nonvacuum[active].astype(int)
        active_truth = program.truth[
            (active[:, None] * ambient + active[None, :]).reshape(-1)
        ]
        h_only = tuple(
            transition_witness(
                program,
                int(pre),
                int(sidecar.stream_mapping[pre]) ^ 1,
            )
            for pre in active_nonvac
        )
        rolled = np.roll(active_nonvac, 1)
        spliced = tuple(
            transition_witness(
                program,
                int(pre),
                int(sidecar.stream_mapping[other]),
            )
            for pre, other in zip(active_nonvac, rolled)
        )
        deleted = compile_transition_program(length, deleted=True)
        deletion_survivors = sum(
            transition_witness(deleted, int(pre), int(sidecar.stream_mapping[pre]))
            for pre in active_nonvac
        )
        full_mapping = transition_full_mapping(program)
        identity = np.arange(len(full_mapping), dtype=np.int32)
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "ambient_rows": ambient,
                "active_code_rows": len(active),
                "nonvacuum_transitions": len(active_nonvac),
                "vacuum_boundaries": len(active_vacuum),
                "code_preserved": code_preserved,
                "truth_false_negatives": int(np.count_nonzero(lawful_truth != expected)),
                "active_pair_false_positives": int(active_truth.sum() - len(active_nonvac)),
                "h_only_false_events": sum(h_only),
                "spliced_boundary_false_events": sum(spliced),
                "deleted_transition_survivors": deletion_survivors,
                "permutation_failures": len(full_mapping) - len(np.unique(full_mapping)),
                "involution_failures": int(np.count_nonzero(full_mapping[full_mapping] != identity)),
                "two_boundary_plus_witness_support_M2": 2 * SOURCE_PATCH_M2 + 1,
            }
        )
    check(
        "route 1 compiles the actual Cycle-314 stream transition into a reversible two-boundary occurrence witness with exact false-event controls",
        all(
            row["ambient_rows"] == 1020
            and row["active_code_rows"] == 510
            and row["nonvacuum_transitions"] == 508
            and row["vacuum_boundaries"] == 2
            and row["code_preserved"]
            and row["truth_false_negatives"] == 0
            and row["active_pair_false_positives"] == 0
            and row["h_only_false_events"] == 0
            and row["spliced_boundary_false_events"] == 0
            and row["deleted_transition_survivors"] == 0
            and row["permutation_failures"] == 0
            and row["involution_failures"] == 0
            and row["two_boundary_plus_witness_support_M2"] == 91
            for row in rows
        ),
        rows,
    )
    return programs


BOUNDARY_NODES = frozenset(
    (
        "pre_boundary",
        "transition_witness",
        "post_boundary",
        "identity_match",
        "predecessor_ready",
        "close_certificate",
    )
)
BOUNDARY_EDGES = frozenset(
    (
        ("pre_boundary", "transition_witness"),
        ("transition_witness", "post_boundary"),
        ("post_boundary", "close_certificate"),
        ("identity_match", "close_certificate"),
        ("predecessor_ready", "close_certificate"),
    )
)
BOUNDARY_DAG = c287.Dag(BOUNDARY_NODES, BOUNDARY_EDGES)


def boundary_certificate(
    pre_code: int,
    transition: int,
    post_code: int,
    match: int,
    ready: int,
    *,
    deleted_stage: int | None = None,
) -> int:
    return c329.causal_certificate(
        (pre_code, transition, post_code, match, ready),
        (1, 1, 1, 1, 1),
        deleted_stage=deleted_stage,
    )[0]


def relational_close_controls(programs: dict[int, TransitionProgram]) -> dict[str, object]:
    rows = []
    deletion_survivors = false_event_survivors = anti_splice_survivors = 0
    for length, program in programs.items():
        fixture = c329.build_fixture(length)
        match, ready = c329.route_outputs(fixture, "syndrome")
        active = program.active_rows
        pre = int(active[program.nonvacuum[active]][0])
        post = int(program.sidecar.stream_mapping[pre])
        witness = transition_witness(program, pre, post)
        certificate = boundary_certificate(1, witness, 1, match, ready)
        readiness_alone = boundary_certificate(0, 0, 0, match, ready)
        h_only_post = post ^ 1
        h_only = boundary_certificate(
            1,
            transition_witness(program, pre, h_only_post),
            int(h_only_post in set(map(int, active))),
            match,
            ready,
        )
        other = int(active[program.nonvacuum[active]][1])
        spliced_post = int(program.sidecar.stream_mapping[other])
        spliced = boundary_certificate(
            1,
            transition_witness(program, pre, spliced_post),
            1,
            match,
            ready,
        )
        corrupted_target = list(fixture.words[4].word)
        corrupted_target[c329.LABEL_BITS] ^= 1
        bad_match, good_ready = c329.route_outputs(
            fixture,
            "syndrome",
            target_word=tuple(corrupted_target),
        )
        anti_splice = boundary_certificate(1, witness, 1, bad_match, good_ready)
        deleted = tuple(
            boundary_certificate(1, witness, 1, match, ready, deleted_stage=stage)
            for stage in range(5)
        )
        deletion_survivors += sum(deleted)
        false_event_survivors += readiness_alone + h_only + spliced
        anti_splice_survivors += anti_splice
        receiver = c326.run_local_close(
            event_ready=1,
            identity_match=match,
            dependencies_ready=ready,
            occurrence=witness,
            close_law=certificate,
        )
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "match_ready": (match, ready),
                "transition_witness": witness,
                "close_certificate": certificate,
                "receiver": receiver,
                "readiness_alone": readiness_alone,
                "h_only": h_only,
                "spliced_boundary": spliced,
                "anti_splice": anti_splice,
                "deleted_stages": deleted,
            }
        )

    schedules = tuple(c287.topological_orders(BOUNDARY_DAG))
    local = {node: True for node in BOUNDARY_NODES}
    outcomes = tuple(c287.replay_dag(BOUNDARY_DAG, order, local) for order in schedules)
    edge_deletions = tuple(
        "close_certificate"
        in c287.replay_dag(
            BOUNDARY_DAG,
            schedules[0],
            local,
            BOUNDARY_EDGES - {edge},
        )
        for edge in sorted(BOUNDARY_EDGES)
    )
    readiness_local = {node: node == "predecessor_ready" for node in BOUNDARY_NODES}
    readiness_outcome = c287.replay_dag(BOUNDARY_DAG, schedules[0], readiness_local)
    detail = {
        "rows": rows,
        "topological_orders": len(schedules),
        "terminal_sets": len(set(outcomes)),
        "edge_deletion_close_survivors": sum(edge_deletions),
        "readiness_only_DAG_close": "close_certificate" in readiness_outcome,
        "certificate_stage_deletion_survivors": deletion_survivors,
        "false_event_survivors": false_event_survivors,
        "anti_splice_survivors": anti_splice_survivors,
        "conservative_source_matcher_certificate_receiver_M2": (
            2 * SOURCE_PATCH_M2 + 621 + 1 + 6 + 2
        ),
    }
    check(
        "route 2 forms a relational two-boundary close certificate that readiness alone, false boundaries, anti-splicing, and deletions cannot produce",
        all(
            row["match_ready"] == (1, 1)
            and row["transition_witness"] == row["close_certificate"] == 1
            and row["receiver"] == (0, 1)
            and row["readiness_alone"] == row["h_only"] == row["spliced_boundary"] == 0
            and row["anti_splice"] == 0
            and row["deleted_stages"] == (0,) * 5
            for row in rows
        )
        and len(schedules) > 1
        and len(set(outcomes)) == 1
        and outcomes[0] == BOUNDARY_NODES
        and not any(edge_deletions)
        and "close_certificate" not in readiness_outcome
        and deletion_survivors == false_event_survivors == anti_splice_survivors == 0
        and detail["conservative_source_matcher_certificate_receiver_M2"] == 720,
        detail,
    )
    return detail


def protect_candidate(
    candidate: int,
    *,
    delete_fanout: int | None = None,
) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    if candidate not in (0, 1) or delete_fanout not in (None, 0, 1):
        raise ValueError("protected candidate uses one bit and two optional fanout gates")
    state = [candidate, 0, 0]
    for gate, target in enumerate((1, 2)):
        if gate != delete_fanout and state[0]:
            state[target] ^= 1
    protected = tuple(state)
    for target in (2, 1):
        if state[0]:
            state[target] ^= 1
    return protected, tuple(state)


def protected_closed_flag(triple: tuple[int, int, int]) -> int:
    return c329.equality_circuit(triple, (1, 1, 1))[0]


def protected_history_controls(programs: dict[int, TransitionProgram]) -> dict[str, object]:
    rows = []
    corruption_survivors = splice_survivors = deletion_survivors = 0
    prior_candidate = c326.run_local_close(
        event_ready=1,
        identity_match=1,
        dependencies_ready=1,
        occurrence=1,
        close_law=1,
    )[1]
    protected = tuple(protect_candidate(prior_candidate)[0] for _ in range(3))
    recovered = tuple(protect_candidate(prior_candidate)[1] for _ in range(3))
    flags = tuple(protected_closed_flag(triple) for triple in protected)
    for length, program in programs.items():
        fixture = c329.build_fixture(length)
        match, ready = c329.route_outputs(fixture, "direct", closed=flags)
        pre = int(program.active_rows[program.nonvacuum[program.active_rows]][0])
        post = int(program.sidecar.stream_mapping[pre])
        witness = transition_witness(program, pre, post)
        close = boundary_certificate(1, witness, 1, match, ready)
        receiver = c326.run_local_close(
            event_ready=1,
            identity_match=match,
            dependencies_ready=ready,
            occurrence=witness,
            close_law=close,
        )
        corrupted_rows = []
        for predecessor in range(3):
            for replica in range(3):
                mutated = [list(row) for row in protected]
                mutated[predecessor][replica] = 0
                corrupted_flags = tuple(
                    protected_closed_flag(tuple(row)) for row in mutated
                )
                output = c329.route_outputs(fixture, "direct", closed=corrupted_flags)
                corrupted_rows.append((predecessor, replica, output))
                corruption_survivors += output[1]
        fanout_rows = []
        for predecessor in range(3):
            for deleted_gate in (0, 1):
                triples = list(protected)
                triples[predecessor] = protect_candidate(
                    prior_candidate,
                    delete_fanout=deleted_gate,
                )[0]
                deleted_flags = tuple(protected_closed_flag(row) for row in triples)
                output = c329.route_outputs(fixture, "direct", closed=deleted_flags)
                fanout_rows.append((predecessor, deleted_gate, output))
                deletion_survivors += output[1]
        predecessor_words = tuple(
            fixture.words[index].word for index in fixture.predecessors
        )
        spliced_words = list(predecessor_words)
        spliced_words[0] = fixture.words[3].word
        spliced = c329.route_outputs(
            fixture,
            "direct",
            predecessor_words=tuple(spliced_words),
            closed=flags,
        )
        splice_survivors += spliced[1]
        false_boundary = int(program.sidecar.stream_mapping[pre]) ^ 1
        false_witness = transition_witness(program, pre, false_boundary)
        false_receiver = c326.run_local_close(
            event_ready=1,
            identity_match=match,
            dependencies_ready=ready,
            occurrence=false_witness,
            close_law=close,
        )
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "prior_candidate": prior_candidate,
                "protected": protected,
                "protected_flags": flags,
                "inverse_recovered": recovered,
                "match_ready": (match, ready),
                "current_transition": witness,
                "receiver": receiver,
                "single_replica_faults": corrupted_rows,
                "fanout_deletions": fanout_rows,
                "identity_splice": spliced,
                "false_boundary_receiver": false_receiver,
            }
        )
    detail = {
        "rows": rows,
        "single_replica_readiness_survivors": corruption_survivors,
        "fanout_deletion_readiness_survivors": deletion_survivors,
        "identity_splice_readiness_survivors": splice_survivors,
        "fresh_replica_capacity_M2": 6,
        "protected_history_M2": 9,
        "conservative_source_matcher_history_receiver_M2": (
            2 * SOURCE_PATCH_M2 + 1089 + 9 + 6 + 1 + 1 + 2
        ),
    }
    check(
        "route 3 derives predecessor-closed flags from identity-checked protected prior candidates while exposing reversibility and finite capacity",
        all(
            row["prior_candidate"] == 1
            and row["protected"] == ((1, 1, 1),) * 3
            and row["protected_flags"] == (1, 1, 1)
            and row["inverse_recovered"] == ((1, 0, 0),) * 3
            and row["match_ready"] == (1, 1)
            and row["current_transition"] == 1
            and row["receiver"] == (0, 1)
            and all(output == (1, 0) for _pred, _replica, output in row["single_replica_faults"])
            and all(output == (1, 0) for _pred, _gate, output in row["fanout_deletions"])
            and row["identity_splice"] == (1, 0)
            and row["false_boundary_receiver"] == (1, 0)
            for row in rows
        )
        and corruption_survivors == deletion_survivors == splice_survivors == 0
        and detail["fresh_replica_capacity_M2"] == 6
        and detail["conservative_source_matcher_history_receiver_M2"] == 1198,
        detail,
    )
    return detail


def event_frame_mapping(sidecar, frame: np.ndarray) -> tuple[np.ndarray, int]:
    reducer = c314.c311.c305.StabilizerReducer(sidecar.encoder.code)
    old, failures = c314.c311.flagged_frame_representation(
        sidecar.encoder,
        sidecar.basis,
        {},
        frame,
        reducer,
    )
    mapping, _phases, mapping_failures = c314.c311.signed_mapping(old)
    role_mapping = np.concatenate(
        (mapping, mapping + c314.c311.FLAGGED_MICRO_DIMENSION)
    )
    event_mapping = np.empty(2 * len(sidecar.base_encoding), dtype=int)
    for row in range(len(sidecar.base_encoding)):
        for h in (0, 1):
            event_mapping[2 * row + h] = 2 * role_mapping[row] + h
    return event_mapping, failures + mapping_failures


def held_frame_and_domain_controls(programs: dict[int, TransitionProgram]) -> None:
    frame_rows = []
    for length, program in programs.items():
        for frame in c314.c311.c235.proper_cubic_frames():
            mapping, failures = event_frame_mapping(program.sidecar, frame)
            stream_failures = int(
                np.count_nonzero(
                    mapping[program.sidecar.stream_mapping]
                    != program.sidecar.stream_mapping[mapping]
                )
            )
            h_failures = int(np.count_nonzero(mapping % 2 != np.arange(len(mapping)) % 2))
            fixture = c329.build_fixture(length, frame)
            match_ready = c329.route_outputs(fixture, "syndrome")
            frame_rows.append(
                (length, failures, stream_failures, h_failures, fixture.covariance_failures, match_ready)
            )
    rejected = 0
    invalid = (
        lambda: compile_transition_program(2),
        lambda: compile_transition_program(7),
        lambda: transition_witness(programs[3], -1, 0),
        lambda: transition_witness(programs[3], 0, 1020),
        lambda: transition_witness(programs[3], 0, 0, 2),
        lambda: protect_candidate(2),
        lambda: protect_candidate(1, delete_fanout=2),
        lambda: boundary_certificate(1, 1, 1, 1, 1, deleted_stage=5),
    )
    for call in invalid:
        try:
            call()
        except (ValueError, IndexError):
            rejected += 1
    check(
        "the transition, matcher, and readiness controls hold at L=6 and in every proper-cubic frame with lawful-domain rejection",
        len(frame_rows) == 48
        and all(
            failures == stream == h == covariance == 0 and match_ready == (1, 1)
            for _length, failures, stream, h, covariance, match_ready in frame_rows
        )
        and rejected == len(invalid),
        {
            "frame_size_cases": len(frame_rows),
            "frame_failures": sum(sum(row[1:5]) for row in frame_rows),
            "lawful_domain_rejections": rejected,
            "attempted": len(invalid),
        },
    )


def inventory_controls() -> None:
    inventory = {
        "derived": (
            "conditional Cycle-314 stream-transition witness",
            "two-boundary close certificate",
            "identity-checked predecessor readiness from protected candidates",
        ),
        "supplied_or_open": (
            "two boundary registers and their preparation",
            "selection of the actual history member",
            "fixed transition/comparator programs",
            "fresh witness/certificate/history capacity",
            "Record typing",
            "permanence",
            "clock matcher and calibration",
        ),
    }
    text = normalized(NOTE)
    check(
        "the supplied boundary, selection, capacity, typing, permanence, clock, and calibration inventory remains explicit",
        "two boundary registers remain supplied" in text
        and "occurrence witness is not a selected actual member" in text
        and "commit candidate is not a record" in text
        and "forward nonreturn is not permanence" in text,
        inventory,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    programs = transition_program_controls()
    relational = relational_close_controls(programs)
    protected = protected_history_controls(programs)
    held_frame_and_domain_controls(programs)
    inventory_controls()
    check(
        "Cycle 332 closes three bounded transition-sensitive routes without promoting a witness or candidate to selected Record history",
        relational["false_event_survivors"] == 0
        and protected["single_replica_readiness_survivors"] == 0
        and "broad gate status: fail / do not ship" in normalized(NOTE)
        and "no axiom pressure" in normalized(NOTE),
        {
            "transition_witness": "positive conditional on two boundaries",
            "relational_close": "positive",
            "protected_history": "positive but reversible",
        },
    )
    print("DATA relational", relational)
    print("DATA protected", protected)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE332_TRANSITION_OCCURRENCE_CLOSE_GREEN"
        if FAIL == 0
        else "CYCLE332_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
