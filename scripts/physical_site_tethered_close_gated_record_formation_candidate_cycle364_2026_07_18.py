#!/usr/bin/env python3
"""Cycle 364 Route 1: immediate site-tethered Record-formation candidate.

This runner states and falsifies one downstream hypothesis; it does not derive
the hypothesis from the framework axioms and does not propose axiom language.
On a declared finite basis domain, a fresh physical site and its complete
Cycle-342 30-bit word become one framework-typed site/content Record exactly
when five locally bound predicates hold: complete lawful payload, the explicit
Cycle-361 faithful-close candidate, Cycle-326 predecessor readiness, an
explicit Cycle-362 common-cause/provenance acceptance interface, and fresh
target capacity.  The close bit alone is never called a Record.

The candidate map is immediate and append-only.  It returns one answer for
every declared-domain input, refuses overwrite, preserves prior site/content
Records, commutes on disjoint neighborhoods, and reports overlap classes
without a hidden priority rule.  The tested reference evaluator reads one
target and at most two adjacent predecessors.  Its state domain is explicitly
fixture-aware: every pre-existing Record must remain a lawful typed/permanent
Cycle-342 word.  It is a candidate formation law, not yet a physical gate
compiler or a selected framework law.

Actual law selection, actual-history sampling, Born/statistical weights,
metric time, interval, rate, renewal, and universal full-lattice completion
remain open.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import product
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18 as c342
import physical_autonomous_record_payload_faithful_close_nn_route_cycle361_2026_07_18 as c361
import physical_fixed_global_common_fork_record_lineage_nn_route_cycle362_2026_07_18 as c362


Coord = tuple[int, int, int]
Word = tuple[int, ...]
LENGTHS = (3, 6)
TRAIN_SIZES = (6, 12)
HELD_SIZE = 18
SIZES = TRAIN_SIZES + (HELD_SIZE,)
TRANSLATIONS: tuple[Coord, ...] = ((0, 0, 0), (7, -3, 5))
MAX_PREDECESSORS = 2
LOCAL_RADIUS = 1
RECORD_BITS = c342.RECORD_BITS
AUTHORITY = "none"
AUDIT = "unset"
LAW_NAME = "Cycle-364 immediate site-tethered close-gated formation hypothesis"
CLOSE_SOURCE = "Cycle-361 faithful-close candidate interface"
READINESS_SOURCE = "Cycle-326 fresh/predecessor readiness interface"
PROVENANCE_SOURCE = "Cycle-362 common-fork provenance acceptance interface"
RECORD_TYPE = "conditional framework site/content Record"
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


def bit(value: object) -> bool:
    return value in (0, 1) and not isinstance(value, bool) or isinstance(value, bool)


def valid_coord(coord: object) -> bool:
    return (
        isinstance(coord, tuple)
        and len(coord) == 3
        and all(isinstance(item, int) and not isinstance(item, bool) for item in coord)
    )


def distance(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def translated(coord: Coord, shift: Coord) -> Coord:
    return tuple(a + b for a, b in zip(coord, shift))  # type: ignore[return-value]


@dataclass(frozen=True)
class SiteContentRecord:
    site: Coord
    content: Word
    predecessors: tuple[Coord, ...]
    record_type: str = RECORD_TYPE
    law: str = LAW_NAME
    permanent_under_candidate_law: bool = True


@dataclass(frozen=True)
class FormationState:
    records: tuple[SiteContentRecord, ...] = ()


@dataclass(frozen=True)
class FaithfulCloseInterface:
    site: Coord
    payload: Word
    close_candidate: int
    source: str = CLOSE_SOURCE


@dataclass(frozen=True)
class ReadinessInterface:
    site: Coord
    predecessors: tuple[Coord, ...]
    predecessors_ready: int
    fresh: int
    source: str = READINESS_SOURCE


@dataclass(frozen=True)
class ProvenanceInterface:
    site: Coord
    payload: Word
    predecessors: tuple[Coord, ...]
    accepted: int
    independent_confirmations: int = 1
    source: str = PROVENANCE_SOURCE


@dataclass(frozen=True)
class FormationProposal:
    site: Coord
    payload: Word
    payload_present: Word
    close: FaithfulCloseInterface
    readiness: ReadinessInterface
    provenance: ProvenanceInterface


@dataclass(frozen=True)
class FormationAnswer:
    state: FormationState
    formed: SiteContentRecord | None
    status: str
    conditions: tuple[tuple[str, bool], ...]


@dataclass(frozen=True)
class BatchAnswer:
    state: FormationState
    statuses: tuple[str, ...]
    overlaps: tuple[tuple[int, int, str], ...]


def canonical(records: tuple[SiteContentRecord, ...]) -> tuple[SiteContentRecord, ...]:
    return tuple(sorted(records, key=lambda item: item.site))


def record_map(state: FormationState) -> dict[Coord, SiteContentRecord]:
    return {record.site: record for record in state.records}


def payload_lawful(fixture: c342.c338.RouteFixture, payload: Word) -> bool:
    try:
        record = c342.decode_record_word(payload)
    except (TypeError, ValueError):
        return False
    return (
        record.typed
        and record.permanent
        and c342.cylinder_is_lawful(fixture, record.cylinder)
    )


def validate_record(record: SiteContentRecord) -> None:
    if not isinstance(record, SiteContentRecord):
        raise TypeError("formation state contains a non-Record value")
    if not valid_coord(record.site):
        raise ValueError("Record site is outside the integer cubic domain")
    if (
        not isinstance(record.content, tuple)
        or len(record.content) != RECORD_BITS
        or any(not bit(item) for item in record.content)
    ):
        raise ValueError("Record content is not one binary Cycle-342 word")
    if (
        not isinstance(record.predecessors, tuple)
        or len(record.predecessors) > MAX_PREDECESSORS
        or len(set(record.predecessors)) != len(record.predecessors)
        or record.site in record.predecessors
        or any(not valid_coord(item) for item in record.predecessors)
        or any(distance(record.site, item) > LOCAL_RADIUS for item in record.predecessors)
    ):
        raise ValueError("Record predecessor neighborhood is outside the local domain")
    if (
        record.record_type != RECORD_TYPE
        or record.law != LAW_NAME
        or record.permanent_under_candidate_law is not True
    ):
        raise ValueError("Record typing is not the conditional Cycle-364 type")


def validate_state(
    fixture: c342.c338.RouteFixture,
    state: FormationState,
) -> None:
    if not isinstance(state, FormationState) or not isinstance(state.records, tuple):
        raise TypeError("formation law requires one finite FormationState")
    for record in state.records:
        validate_record(record)
        if not payload_lawful(fixture, record.content):
            raise ValueError(
                "formation state contains an unlawful Cycle-342 Record word"
            )
    if len({record.site for record in state.records}) != len(state.records):
        raise ValueError("formation state contains an occupied-site alias")
    if state.records != canonical(state.records):
        raise ValueError("formation state must use canonical site order")


def validate_proposal(proposal: FormationProposal) -> None:
    if not isinstance(proposal, FormationProposal):
        raise TypeError("formation law requires one FormationProposal")
    if not valid_coord(proposal.site):
        raise ValueError("proposal site is outside the integer cubic domain")
    if (
        not isinstance(proposal.payload, tuple)
        or len(proposal.payload) != RECORD_BITS
        or any(not bit(item) for item in proposal.payload)
    ):
        raise ValueError("proposal payload is not a binary 30-M2 word")
    if (
        not isinstance(proposal.payload_present, tuple)
        or len(proposal.payload_present) != RECORD_BITS
        or any(not bit(item) for item in proposal.payload_present)
    ):
        raise ValueError("payload-presence mask is outside the 30-bit domain")
    if not isinstance(proposal.close, FaithfulCloseInterface):
        raise TypeError("missing explicit Cycle-361 close interface")
    if not isinstance(proposal.readiness, ReadinessInterface):
        raise TypeError("missing explicit Cycle-326 readiness interface")
    if not isinstance(proposal.provenance, ProvenanceInterface):
        raise TypeError("missing explicit Cycle-362 provenance interface")
    if (
        not valid_coord(proposal.close.site)
        or not isinstance(proposal.close.payload, tuple)
        or len(proposal.close.payload) != RECORD_BITS
        or any(not bit(item) for item in proposal.close.payload)
        or not bit(proposal.close.close_candidate)
        or proposal.close.source != CLOSE_SOURCE
    ):
        raise ValueError("Cycle-361 close interface is outside its declared domain")
    predecessors = proposal.readiness.predecessors
    if (
        not valid_coord(proposal.readiness.site)
        or not isinstance(predecessors, tuple)
        or len(predecessors) > MAX_PREDECESSORS
        or len(set(predecessors)) != len(predecessors)
        or proposal.site in predecessors
        or any(not valid_coord(item) for item in predecessors)
        or any(distance(proposal.site, item) > LOCAL_RADIUS for item in predecessors)
        or not bit(proposal.readiness.predecessors_ready)
        or not bit(proposal.readiness.fresh)
        or proposal.readiness.source != READINESS_SOURCE
    ):
        raise ValueError("Cycle-326 readiness interface is outside its local domain")
    if (
        not valid_coord(proposal.provenance.site)
        or not isinstance(proposal.provenance.payload, tuple)
        or len(proposal.provenance.payload) != RECORD_BITS
        or any(not bit(item) for item in proposal.provenance.payload)
        or not isinstance(proposal.provenance.predecessors, tuple)
        or len(proposal.provenance.predecessors) > MAX_PREDECESSORS
        or any(not valid_coord(item) for item in proposal.provenance.predecessors)
        or not bit(proposal.provenance.accepted)
        or not isinstance(proposal.provenance.independent_confirmations, int)
        or isinstance(proposal.provenance.independent_confirmations, bool)
        or not 0 <= proposal.provenance.independent_confirmations <= 3
        or proposal.provenance.source != PROVENANCE_SOURCE
    ):
        raise ValueError("Cycle-362 provenance interface is outside its declared domain")


def condition_table(
    fixture: c342.c338.RouteFixture,
    state: FormationState,
    proposal: FormationProposal,
) -> tuple[tuple[str, bool], ...]:
    existing = record_map(state)
    dependency_ready = set(proposal.readiness.predecessors) <= set(existing)
    complete = all(proposal.payload_present) and payload_lawful(fixture, proposal.payload)
    faithful_close = bool(
        proposal.close.close_candidate
        and proposal.close.site == proposal.site
        and proposal.close.payload == proposal.payload
    )
    predecessors_ready = bool(
        proposal.readiness.predecessors_ready
        and proposal.readiness.site == proposal.site
        and proposal.readiness.predecessors == proposal.provenance.predecessors
        and dependency_ready
    )
    provenance_accepted = bool(
        proposal.provenance.accepted
        and proposal.provenance.site == proposal.site
        and proposal.provenance.payload == proposal.payload
        and proposal.provenance.predecessors == proposal.readiness.predecessors
    )
    fresh_site = bool(proposal.readiness.fresh and proposal.site not in existing)
    return (
        ("complete_payload", bool(complete)),
        ("faithful_close", faithful_close),
        ("predecessor_readiness", predecessors_ready),
        ("provenance_acceptance", provenance_accepted),
        ("fresh_site", fresh_site),
    )


def apply_candidate_law(
    fixture: c342.c338.RouteFixture,
    state: FormationState,
    proposal: FormationProposal,
) -> FormationAnswer:
    """Total Cycle-364 candidate map on its validated finite basis domain."""

    validate_state(fixture, state)
    validate_proposal(proposal)
    conditions = condition_table(fixture, state, proposal)
    failed = tuple(name for name, value in conditions if not value)
    if proposal.site in record_map(state):
        return FormationAnswer(state, None, "overwrite-rejected", conditions)
    if failed:
        return FormationAnswer(state, None, "blocked:" + ",".join(failed), conditions)
    formed = SiteContentRecord(
        proposal.site,
        proposal.payload,
        proposal.readiness.predecessors,
    )
    output = FormationState(canonical(state.records + (formed,)))
    return FormationAnswer(output, formed, "formed", conditions)


def neighborhood(proposal: FormationProposal) -> frozenset[Coord]:
    return frozenset((proposal.site,) + proposal.readiness.predecessors)


def overlap_table(proposals: tuple[FormationProposal, ...]) -> tuple[tuple[int, int, str], ...]:
    rows = []
    for left in range(len(proposals)):
        for right in range(left + 1, len(proposals)):
            a, b = proposals[left], proposals[right]
            if a.site == b.site:
                kind = "same-target-write"
            elif a.site in b.readiness.predecessors or b.site in a.readiness.predecessors:
                kind = "target-predecessor-dependency"
            elif neighborhood(a) & neighborhood(b):
                kind = "shared-read-neighborhood"
            else:
                continue
            rows.append((left, right, kind))
    return tuple(rows)


def apply_atomic_batch(
    fixture: c342.c338.RouteFixture,
    state: FormationState,
    proposals: tuple[FormationProposal, ...],
) -> BatchAnswer:
    validate_state(fixture, state)
    if not isinstance(proposals, tuple):
        raise TypeError("atomic proposals must be a tuple")
    for proposal in proposals:
        validate_proposal(proposal)
    overlaps = overlap_table(proposals)
    conflicted = {
        index
        for left, right, kind in overlaps
        if kind == "same-target-write"
        for index in (left, right)
    }
    answers = []
    additions = []
    for index, proposal in enumerate(proposals):
        if index in conflicted:
            answers.append("overlap-conflict:same-target-write")
            continue
        answer = apply_candidate_law(fixture, state, proposal)
        answers.append(answer.status)
        if answer.formed is not None:
            additions.append(answer.formed)
    output = FormationState(canonical(state.records + tuple(additions)))
    return BatchAnswer(output, tuple(answers), overlaps)


def words(fixture: c342.c338.RouteFixture, count: int) -> tuple[Word, ...]:
    cylinders = c342.make_cylinder_chain(fixture, endpoint=0, count=count)
    records = tuple(c342.form_conditional_record(fixture, item) for item in cylinders)
    if any(not item.typed or not item.permanent for item in records):
        raise RuntimeError("supplied Cycle-342 word fixture failed conditional typing")
    return tuple(c342.record_word(item) for item in records)


def proposal(
    site: Coord,
    payload: Word,
    predecessors: tuple[Coord, ...] = (),
    *,
    complete: int = 1,
    close: int = 1,
    ready: int = 1,
    provenance: int = 1,
    fresh: int = 1,
    confirmations: int = 1,
) -> FormationProposal:
    present = (complete,) * RECORD_BITS
    return FormationProposal(
        site,
        payload,
        present,
        FaithfulCloseInterface(site, payload, close),
        ReadinessInterface(site, predecessors, ready, fresh),
        ProvenanceInterface(
            site,
            payload,
            predecessors,
            provenance,
            confirmations,
        ),
    )


def build_chain(
    fixture: c342.c338.RouteFixture,
    count: int,
) -> tuple[FormationState, tuple[FormationState, ...], tuple[FormationProposal, ...]]:
    payloads = words(fixture, count)
    state = FormationState()
    states = [state]
    proposals = []
    for index, payload in enumerate(payloads):
        site = (index, 0, 0)
        predecessors: tuple[Coord, ...] = () if index == 0 else ((index - 1, 0, 0),)
        item = proposal(site, payload, predecessors)
        answer = apply_candidate_law(fixture, state, item)
        if answer.status != "formed":
            raise RuntimeError(("lawful chain fixture did not form", index, answer))
        proposals.append(item)
        state = answer.state
        states.append(state)
    return state, tuple(states), tuple(proposals)


def truth_table_controls() -> dict[str, object]:
    fixture = c342.c338.build_fixture(3)
    payload = words(fixture, 1)[0]
    target = (0, 0, 0)
    occupied = SiteContentRecord(target, payload, ())
    rows = []
    formation_count = total_failures = nondeterminism = 0
    for is_occupied, gates in product((0, 1), product((0, 1), repeat=5)):
        complete, close, ready, provenance, fresh = gates
        state = FormationState((occupied,)) if is_occupied else FormationState()
        item = proposal(
            target,
            payload,
            complete=complete,
            close=close,
            ready=ready,
            provenance=provenance,
            fresh=fresh,
            confirmations=provenance,
        )
        answer = apply_candidate_law(fixture, state, item)
        repeated = apply_candidate_law(fixture, state, item)
        expected = not is_occupied and all(gates)
        actual = answer.status == "formed"
        formation_count += int(actual)
        nondeterminism += int(answer != repeated)
        total_failures += int(actual != expected)
        total_failures += int(is_occupied and answer.status != "overwrite-rejected")
        rows.append((is_occupied, gates, answer.status, actual))
    detail = {
        "declared_domain_states": len(rows),
        "formed_states": formation_count,
        "truth_table_failures": total_failures,
        "nondeterministic_answers": nondeterminism,
        "condition_order": tuple(name for name, _ in apply_candidate_law(
            fixture, FormationState(), proposal(target, payload)
        ).conditions),
        "occupied_states_answer_overwrite_rejected": 32,
    }
    check(
        "the candidate law gives one deterministic answer on all 64 gate/occupancy states and forms iff all five bound predicates hold",
        len(rows) == 64
        and formation_count == 1
        and total_failures == nondeterminism == 0,
        detail,
    )
    return detail


def append_preservation_and_held_controls() -> dict[str, object]:
    rows = []
    failures = preservation_failures = overwrite_failures = 0
    for length in LENGTHS:
        fixture = c342.c338.build_fixture(length)
        for size in SIZES:
            final, states, proposals = build_chain(fixture, size)
            pair_checks = 0
            for earlier_index, earlier in enumerate(states):
                prior = record_map(earlier)
                for later in states[earlier_index + 1 :]:
                    after = record_map(later)
                    preservation_failures += sum(
                        after.get(site) != record for site, record in prior.items()
                    )
                    pair_checks += len(prior)
            last = proposals[-1]
            overwrite = apply_candidate_law(
                fixture,
                final,
                replace(last, payload=words(fixture, size + 1)[-1]),
            )
            overwrite_failures += int(
                overwrite.status != "overwrite-rejected" or overwrite.state != final
            )
            failures += int(len(final.records) != size)
            rows.append(
                {
                    "L": length,
                    "N": size,
                    "held": length == 6 and size == HELD_SIZE,
                    "formed_records": len(final.records),
                    "later_continuation_preservation_checks": pair_checks,
                    "maximum_predecessors": max(len(item.readiness.predecessors) for item in proposals),
                    "overwrite_rejected": overwrite.status == "overwrite-rejected",
                }
            )
    check(
        "append-only site/content Records preserve every earlier site and word through all later lawful chain continuations at N6/N12/held-N18",
        failures == preservation_failures == overwrite_failures == 0,
        {
            "rows": rows,
            "formation_failures": failures,
            "prior_site_content_residual": preservation_failures,
            "overwrite_failures": overwrite_failures,
        },
    )
    return {"rows": rows, "failures": failures + preservation_failures + overwrite_failures}


def concurrency_and_overlap_controls() -> dict[str, object]:
    fixture = c342.c338.build_fixture(3)
    payloads = words(fixture, 5)
    empty = FormationState()
    left = proposal((0, 0, 0), payloads[0])
    right = proposal((4, 0, 0), payloads[1])
    lr = apply_candidate_law(fixture, apply_candidate_law(fixture, empty, left).state, right)
    rl = apply_candidate_law(fixture, apply_candidate_law(fixture, empty, right).state, left)
    disjoint_batch = apply_atomic_batch(fixture, empty, (left, right))

    same_target_other = proposal((0, 0, 0), payloads[2])
    conflict = apply_atomic_batch(fixture, empty, (left, same_target_other))

    dependent = proposal((1, 0, 0), payloads[3], ((0, 0, 0),))
    dependency_batch = apply_atomic_batch(fixture, empty, (left, dependent))

    root = apply_candidate_law(fixture, empty, left).state
    child_x = proposal((1, 0, 0), payloads[3], ((0, 0, 0),))
    child_y = proposal((0, 1, 0), payloads[4], ((0, 0, 0),))
    xy = apply_candidate_law(fixture, apply_candidate_law(fixture, root, child_x).state, child_y)
    yx = apply_candidate_law(fixture, apply_candidate_law(fixture, root, child_y).state, child_x)
    shared_batch = apply_atomic_batch(fixture, root, (child_x, child_y))

    remote = proposal((9, 0, 0), payloads[2])
    remote_state = apply_candidate_law(fixture, empty, remote).state
    local_without_remote = apply_candidate_law(fixture, empty, left)
    local_with_remote = apply_candidate_law(fixture, remote_state, left)
    remote_map = record_map(local_with_remote.state)

    detail = {
        "disjoint_neighborhoods": not bool(neighborhood(left) & neighborhood(right)),
        "disjoint_sequential_commutes": lr.state == rl.state,
        "disjoint_atomic_matches": disjoint_batch.state == lr.state,
        "same_target_statuses": conflict.statuses,
        "same_target_overlaps": conflict.overlaps,
        "same_target_records": len(conflict.state.records),
        "dependency_overlap": dependency_batch.overlaps,
        "dependency_statuses": dependency_batch.statuses,
        "shared_read_overlap": shared_batch.overlaps,
        "shared_read_sequential_commutes": xy.state == yx.state,
        "shared_read_atomic_matches": shared_batch.state == xy.state,
        "remote_Record_does_not_change_local_conditions": (
            local_without_remote.conditions == local_with_remote.conditions
        ),
        "remote_Record_does_not_change_local_status": (
            local_without_remote.status == local_with_remote.status
        ),
        "remote_Record_preserved_exactly": (
            remote_map.get((9, 0, 0)) == record_map(remote_state).get((9, 0, 0))
        ),
        "priority_rule": None,
    }
    check(
        "disjoint neighborhoods commute while same-target and target/predecessor overlaps are explicit without a priority selector",
        detail["disjoint_neighborhoods"]
        and detail["disjoint_sequential_commutes"]
        and detail["disjoint_atomic_matches"]
        and conflict.statuses == (
            "overlap-conflict:same-target-write",
            "overlap-conflict:same-target-write",
        )
        and conflict.overlaps == ((0, 1, "same-target-write"),)
        and len(conflict.state.records) == 0
        and (0, 1, "target-predecessor-dependency") in dependency_batch.overlaps
        and dependency_batch.statuses[0] == "formed"
        and dependency_batch.statuses[1].startswith("blocked:predecessor_readiness")
        and (0, 1, "shared-read-neighborhood") in shared_batch.overlaps
        and detail["shared_read_sequential_commutes"]
        and detail["shared_read_atomic_matches"]
        and detail["remote_Record_does_not_change_local_conditions"]
        and detail["remote_Record_does_not_change_local_status"]
        and detail["remote_Record_preserved_exactly"]
        and detail["priority_rule"] is None,
        detail,
    )
    return detail


def rotate_payload(
    payload: Word,
    mapping,
) -> Word:
    record = c342.decode_record_word(payload)
    cylinder = record.cylinder
    rotated_cylinder = c342.c338.FutureCylinder(
        endpoint=cylinder.endpoint,
        candidate=cylinder.candidate,
        phase=cylinder.phase,
        future_pre=int(mapping[cylinder.future_pre]),
        future_post=int(mapping[cylinder.future_post]),
    )
    return c342.record_word(
        c342.CylinderRecord(rotated_cylinder, record.typed, record.permanent)
    )


def transform_coord(coord: Coord, frame, shift: Coord) -> Coord:
    return translated(c362.c353.rotated(coord, frame), shift)


def transform_record(record: SiteContentRecord, frame, shift: Coord, mapping) -> SiteContentRecord:
    return replace(
        record,
        site=transform_coord(record.site, frame, shift),
        content=rotate_payload(record.content, mapping),
        predecessors=tuple(transform_coord(item, frame, shift) for item in record.predecessors),
    )


def transform_state(state: FormationState, frame, shift: Coord, mapping) -> FormationState:
    return FormationState(canonical(tuple(
        transform_record(record, frame, shift, mapping) for record in state.records
    )))


def transform_proposal(item: FormationProposal, frame, shift: Coord, mapping) -> FormationProposal:
    site = transform_coord(item.site, frame, shift)
    payload = rotate_payload(item.payload, mapping)
    predecessors = tuple(
        transform_coord(value, frame, shift) for value in item.readiness.predecessors
    )
    return FormationProposal(
        site,
        payload,
        item.payload_present,
        replace(item.close, site=site, payload=payload),
        replace(item.readiness, site=site, predecessors=predecessors),
        replace(item.provenance, site=site, payload=payload, predecessors=predecessors),
    )


def transform_answer(answer: FormationAnswer, frame, shift: Coord, mapping) -> FormationAnswer:
    return FormationAnswer(
        transform_state(answer.state, frame, shift, mapping),
        None if answer.formed is None else transform_record(answer.formed, frame, shift, mapping),
        answer.status,
        answer.conditions,
    )


def covariance_controls() -> dict[str, object]:
    frames = c362.c353.proper_cubic_frames()
    cases = held_cases = mapping_failures = covariance_failures = locality_failures = 0
    for length in LENGTHS:
        fixture = c342.c338.build_fixture(length)
        rotated_fixtures = []
        for frame in frames:
            rotated_fixture, mapping, failures = c342.mapped_fixture(fixture, frame)
            rotated_fixtures.append((frame, rotated_fixture, mapping))
            mapping_failures += failures
        for size in SIZES:
            payloads = words(fixture, size)
            state, _, _ = build_chain(fixture, size - 1)
            target = (size - 1, 0, 0)
            item = proposal(target, payloads[-1], ((size - 2, 0, 0),))
            reference = apply_candidate_law(fixture, state, item)
            for frame, rotated_fixture, mapping in rotated_fixtures:
                for shift in TRANSLATIONS:
                    transformed_state = transform_state(state, frame, shift, mapping)
                    transformed_item = transform_proposal(item, frame, shift, mapping)
                    observed = apply_candidate_law(
                        rotated_fixture,
                        transformed_state,
                        transformed_item,
                    )
                    expected = transform_answer(reference, frame, shift, mapping)
                    covariance_failures += int(observed != expected)
                    locality_failures += int(
                        any(
                            distance(transformed_item.site, predecessor) > LOCAL_RADIUS
                            for predecessor in transformed_item.readiness.predecessors
                        )
                    )
                    cases += 1
                    held_cases += int(length == 6 and size == HELD_SIZE)
    detail = {
        "L_by_N_by_frame_by_translation_cases": cases,
        "proper_cubic_frames": len(frames),
        "translations": TRANSLATIONS,
        "held_L6_N18_cases": held_cases,
        "Cycle342_payload_mapping_failures": mapping_failures,
        "formation_covariance_failures": covariance_failures,
        "local_radius_failures": locality_failures,
    }
    check(
        "site, predecessor, close, provenance, and complete Cycle-342 payload bindings are exact under translations and all 24 proper-cubic frames",
        len(frames) == 24
        and cases == len(LENGTHS) * len(SIZES) * 24 * len(TRANSLATIONS)
        and held_cases == 24 * len(TRANSLATIONS)
        and mapping_failures == covariance_failures == locality_failures == 0,
        detail,
    )
    return detail


def deletion_corruption_splice_and_domain_controls() -> dict[str, object]:
    fixture = c342.c338.build_fixture(3)
    payloads = words(fixture, 3)
    site = (0, 0, 0)
    lawful = proposal(site, payloads[0])
    empty = FormationState()
    deletion_rows = []
    variants = (
        ("complete_payload", proposal(site, payloads[0], complete=0)),
        ("faithful_close", proposal(site, payloads[0], close=0)),
        ("predecessor_readiness", proposal(site, payloads[0], ready=0)),
        ("provenance_acceptance", proposal(site, payloads[0], provenance=0, confirmations=0)),
        ("fresh_site", proposal(site, payloads[0], fresh=0)),
    )
    for name, attacked in variants:
        answer = apply_candidate_law(fixture, empty, attacked)
        deletion_rows.append(
            {
                "deleted": name,
                "formed": answer.formed is not None,
                "state_unchanged": answer.state == empty,
                "condition_visible": dict(answer.conditions)[name] is False,
            }
        )

    corruption_rows = []
    for index in range(RECORD_BITS):
        corrupted = list(lawful.payload)
        corrupted[index] ^= 1
        attacked = replace(lawful, payload=tuple(corrupted))
        answer = apply_candidate_law(fixture, empty, attacked)
        corruption_rows.append(
            (
                index,
                answer.formed is None,
                not dict(answer.conditions)["faithful_close"],
                not dict(answer.conditions)["provenance_acceptance"],
            )
        )

    root_answer = apply_candidate_law(fixture, empty, lawful)
    child = proposal((1, 0, 0), payloads[1], (site,))
    child_lawful = apply_candidate_law(fixture, root_answer.state, child)
    missing_parent = apply_candidate_law(fixture, empty, child)
    corrupted_parent_content = list(root_answer.formed.content)
    corrupted_parent_content[RECORD_BITS - 2] ^= 1
    corrupted_parent = replace(root_answer.formed, content=tuple(corrupted_parent_content))
    corrupted_parent_state = FormationState((corrupted_parent,))
    corrupted_parent_rejections = 0
    try:
        apply_candidate_law(fixture, corrupted_parent_state, child)
    except ValueError:
        corrupted_parent_rejections += 1

    other_site = (4, 0, 0)
    independent = proposal(other_site, payloads[0])
    equal_content_distinct = apply_candidate_law(
        fixture,
        root_answer.state,
        independent,
    )
    close_splice = replace(
        independent,
        close=lawful.close,
    )
    provenance_splice = replace(
        independent,
        provenance=lawful.provenance,
    )
    close_splice_answer = apply_candidate_law(fixture, root_answer.state, close_splice)
    provenance_splice_answer = apply_candidate_law(
        fixture,
        root_answer.state,
        provenance_splice,
    )

    invalid_calls = (
        lambda: apply_candidate_law(fixture, empty, replace(lawful, site=(0, 0))),
        lambda: apply_candidate_law(fixture, empty, replace(lawful, site=(True, 0, 0))),
        lambda: apply_candidate_law(fixture, empty, replace(lawful, payload=lawful.payload[:-1])),
        lambda: apply_candidate_law(fixture, empty, replace(lawful, payload_present=(1,) * 29)),
        lambda: apply_candidate_law(fixture, empty, replace(lawful, payload_present=(2,) + (1,) * 29)),
        lambda: apply_candidate_law(fixture, empty, replace(lawful, close=replace(lawful.close, close_candidate=2))),
        lambda: apply_candidate_law(fixture, empty, replace(lawful, close=replace(lawful.close, source="host-close"))),
        lambda: apply_candidate_law(fixture, empty, replace(lawful, readiness=ReadinessInterface(site, (site,), 1, 1))),
        lambda: apply_candidate_law(fixture, empty, replace(lawful, readiness=ReadinessInterface(site, ((2, 0, 0),), 1, 1))),
        lambda: apply_candidate_law(fixture, empty, replace(lawful, readiness=replace(lawful.readiness, fresh=2))),
        lambda: apply_candidate_law(fixture, empty, replace(lawful, provenance=replace(lawful.provenance, accepted=2))),
        lambda: apply_candidate_law(fixture, empty, replace(lawful, provenance=replace(lawful.provenance, independent_confirmations=4))),
        lambda: apply_candidate_law(fixture, FormationState((SiteContentRecord(site, payloads[0], ()), SiteContentRecord(site, payloads[1], ()))), lawful),
        lambda: apply_atomic_batch(fixture, empty, [lawful]),  # type: ignore[arg-type]
    )
    domain_rejections = 0
    for call in invalid_calls:
        try:
            call()
        except (TypeError, ValueError):
            domain_rejections += 1
    domain_rejections += corrupted_parent_rejections

    formed_leakage = len(root_answer.state.records) - len(empty.records) - 1
    blocked_leakage = (
        int(missing_parent.state != empty)
        + int(close_splice_answer.state != root_answer.state)
        + int(provenance_splice_answer.state != root_answer.state)
    )
    prior_residual = int(
        record_map(child_lawful.state).get(site) != root_answer.formed
        or record_map(equal_content_distinct.state).get(site) != root_answer.formed
    )
    detail = {
        "five_predicate_deletions": deletion_rows,
        "payload_bit_corruptions_tested": len(corruption_rows),
        "payload_corruption_rejections": sum(row[1] for row in corruption_rows),
        "payload_corruption_close_binding_failures": sum(row[2] for row in corruption_rows),
        "payload_corruption_provenance_binding_failures": sum(row[3] for row in corruption_rows),
        "missing_predecessor_status": missing_parent.status,
        "typing_corrupted_predecessor_domain_rejected": corrupted_parent_rejections == 1,
        "equal_content_distinct_site_records": len(equal_content_distinct.state.records),
        "close_splice_status": close_splice_answer.status,
        "provenance_splice_status": provenance_splice_answer.status,
        "lawful_domain_rejections": domain_rejections,
        "attempted_domain_violations": len(invalid_calls) + 1,
        "formed_extra_record_leakage": formed_leakage,
        "blocked_state_leakage": blocked_leakage,
        "prior_site_content_residual": prior_residual,
    }
    check(
        "predicate deletion, all 30 payload-bit corruptions, missing parents, typing-corrupted state, interface splices, aliases, and malformed domains are visible without prior-Record leakage",
        all(
            not row["formed"] and row["state_unchanged"] and row["condition_visible"]
            for row in deletion_rows
        )
        and len(corruption_rows) == RECORD_BITS
        and all(row[1] and row[2] and row[3] for row in corruption_rows)
        and child_lawful.status == "formed"
        and missing_parent.formed is None
        and "predecessor_readiness" in missing_parent.status
        and corrupted_parent_rejections == 1
        and len(equal_content_distinct.state.records) == 2
        and close_splice_answer.formed is None
        and provenance_splice_answer.formed is None
        and domain_rejections == len(invalid_calls) + 1
        and formed_leakage == blocked_leakage == prior_residual == 0,
        detail,
    )
    return detail


def redundancy_threshold_answer(
    fixture: c342.c338.RouteFixture,
    state: FormationState,
    item: FormationProposal,
    threshold: int = 2,
) -> bool:
    answer = apply_candidate_law(fixture, state, item)
    return answer.status == "formed" and item.provenance.independent_confirmations >= threshold


def discriminator_controls() -> dict[str, object]:
    fixture = c342.c338.build_fixture(3)
    payload = words(fixture, 1)[0]
    single = proposal((0, 0, 0), payload, confirmations=1)
    double = proposal((1, 0, 0), payload, confirmations=2)
    immediate_single = apply_candidate_law(fixture, FormationState(), single)
    immediate_double = apply_candidate_law(fixture, FormationState(), double)
    threshold_single = redundancy_threshold_answer(fixture, FormationState(), single)
    threshold_double = redundancy_threshold_answer(fixture, FormationState(), double)
    detail = {
        "discriminator": "one accepted bound provenance witness at a fresh site",
        "independent_confirmations": 1,
        "immediate_candidate_predicts_formation": immediate_single.status == "formed",
        "redundancy_threshold_2_predicts_formation": threshold_single,
        "two_confirmation_common_control": {
            "immediate": immediate_double.status == "formed",
            "threshold_2": threshold_double,
        },
        "law_selected": False,
    }
    check(
        "one accepted provenance interface is a concrete discriminator: the immediate candidate forms while a threshold-two alternative does not",
        immediate_single.status == "formed"
        and not threshold_single
        and immediate_double.status == "formed"
        and threshold_double
        and detail["law_selected"] is False,
        detail,
    )
    return detail


def inventory_and_semantic_controls() -> dict[str, object]:
    inventory = {
        "result": "bounded positive exact candidate Record-formation law on the declared finite domain",
        "hypothesis": LAW_NAME,
        "hypothesis_status": "falsifiable downstream candidate",
        "derived_from_axioms": False,
        "axiom_language_proposed": False,
        "selected_framework_law": False,
        "formed_type": RECORD_TYPE,
        "Record_name_scope": "only the output of this explicitly supplied conditional candidate law",
        "close_bit_alone_is_Record": False,
        "Cycle361_input": "one site/content-bound faithful-close candidate bit for one complete 30-M2 word",
        "Cycle361_physical_circuit_reexecuted": False,
        "Cycle362_input": "one explicit site/content/predecessor-bound Boolean provenance acceptance interface",
        "Cycle362_circuit_silently_spliced": False,
        "Cycle326_input": "one explicit readiness/freshness interface with exact local predecessor-label subset semantics",
        "Cycle326_EventIdentity_or_mode_support_fabricated": False,
        "Cycle342_input": "one supplied lawful typed permanent 30-M2 content word and its L-specific decoder fixture",
        "declared_state_domain": "every existing conditional Record decodes as a lawful typed/permanent Cycle-342 word in the active fixture",
        "state_domain_fixture_aware": True,
        "typing_corruption_is_lawful_blocked_state": False,
        "required_predicates": (
            "complete_payload",
            "faithful_close",
            "predecessor_readiness",
            "provenance_acceptance",
            "fresh_site",
        ),
        "maximum_predecessors": MAX_PREDECESSORS,
        "maximum_site_neighborhood": 1 + MAX_PREDECESSORS,
        "local_radius_L1": LOCAL_RADIUS,
        "state_update": "append exactly one immutable site/content pair or leave the state unchanged",
        "physical_gate_compiler": None,
        "globally_complete_lattice_law": None,
        "consistent_corruption_of_payload_and_all_supplied_interfaces_resolved_upstream": True,
        "actual_law_selection": None,
        "actual_history_sampler": None,
        "Born_weights": None,
        "statistics": None,
        "metric_time": None,
        "interval": None,
        "rate": None,
        "renewal": None,
        "universal_full_lattice_completion": None,
        "no_go": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    text = " ".join(__doc__.split()).lower()
    required_text = (
        "downstream hypothesis",
        "does not derive",
        "close bit alone is never called a record",
        "candidate formation law",
        "actual law selection",
        "born/statistical weights",
        "metric time",
        "renewal",
        "universal full-lattice completion",
        "authority is none",
        "audit is unset",
    )
    check(
        "the inventory keeps every supplied interface and semantic residual explicit with authority none and audit unset",
        all(item in text for item in required_text)
        and RECORD_BITS == 30
        and c361.MATCH_BITS == RECORD_BITS
        and c362.PAYLOAD_LANES == tuple(range(2, RECORD_BITS + 2))
        and inventory["derived_from_axioms"] is False
        and inventory["axiom_language_proposed"] is False
        and inventory["selected_framework_law"] is False
        and inventory["close_bit_alone_is_Record"] is False
        and inventory["Cycle361_physical_circuit_reexecuted"] is False
        and inventory["Cycle362_circuit_silently_spliced"] is False
        and inventory["Cycle326_EventIdentity_or_mode_support_fabricated"] is False
        and inventory["state_domain_fixture_aware"] is True
        and inventory["typing_corruption_is_lawful_blocked_state"] is False
        and inventory["maximum_site_neighborhood"] == 3
        and inventory["physical_gate_compiler"] is None
        and inventory["globally_complete_lattice_law"] is None
        and inventory["actual_law_selection"] is None
        and inventory["actual_history_sampler"] is None
        and inventory["Born_weights"] is inventory["statistics"] is None
        and inventory["metric_time"] is inventory["interval"] is inventory["rate"] is None
        and inventory["renewal"] is inventory["universal_full_lattice_completion"] is None
        and inventory["no_go"] is inventory["axiom_pressure"] is None
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )
    return inventory


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 364 ROUTE 1: IMMEDIATE SITE-TETHERED CLOSE-GATED RECORD-FORMATION CANDIDATE")
    print("authority=none; audit=unset; downstream hypothesis; not axiom language")
    truth = truth_table_controls()
    append = append_preservation_and_held_controls()
    overlap = concurrency_and_overlap_controls()
    covariance = covariance_controls()
    attacks = deletion_corruption_splice_and_domain_controls()
    discriminator = discriminator_controls()
    inventory = inventory_and_semantic_controls()
    check(
        "Route 1 is an exact bounded positive formation-law candidate with a live threshold discriminator, not a selected universal law",
        truth["truth_table_failures"] == 0
        and append["failures"] == 0
        and overlap["priority_rule"] is None
        and covariance["formation_covariance_failures"] == 0
        and attacks["payload_corruption_rejections"] == RECORD_BITS
        and discriminator["immediate_candidate_predicts_formation"]
        and not discriminator["redundancy_threshold_2_predicts_formation"]
        and inventory["selected_framework_law"] is False,
        {
            "disposition": "bounded positive falsifiable downstream candidate",
            "declared_truth_table_states": truth["declared_domain_states"],
            "sizes": SIZES,
            "proper_cubic_frames": covariance["proper_cubic_frames"],
            "Record_law_selected": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_SITE_TETHERED_RECORD_FORMATION_CANDIDATE_OPEN")
        return 1
    print("RESULT PHYSICAL_SITE_TETHERED_RECORD_FORMATION_CANDIDATE_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
