#!/usr/bin/env python3
"""Cycle 333: bounded relational pointwise continuation registration.

The realized-state primitive supplies a pointwise reference but no contingent
content.  This runner tests whether one supplied realized-prefix boundary,
the exact Cycle-314 transition relation, and the Cycle-329/332 close inputs
identify one unique continuation.  The bank-membership flag is not called a
newly selected actual history, Record, clock tick, or Born sample.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import clock_as_commit_count_and_rate_classification_cycle22_2026_07_14 as c22
import cycle189_record_corpus_frequency_bridge_cycle194_2026_07_16 as c194
import spatial_compiler_derived_causal_time_bridge_cycle243_2026_07_17 as c243
import stochastic_record_history_actuality_semantics_cycle27_2026_07_14 as c27
import physical_transition_occurrence_close_tournament_cycle332_2026_07_18 as c332


c329 = c332.c329
c326 = c332.c326
c314 = c332.c314
c287 = c332.c287
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RELATIONAL_ACTUAL_HISTORY_MEMBER_SELECTION_CYCLE333_NOTE_2026-07-18.md"
)
REALIZED = ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
CYCLE30 = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md"
)
CYCLE243 = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "SPATIAL_COMPILER_DERIVED_CAUSAL_TIME_BRIDGE_CYCLE243_NOTE_2026-07-17.md"
)
CYCLE194 = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "CYCLE189_RECORD_CORPUS_FREQUENCY_BRIDGE_CYCLE194_NOTE_2026-07-16.md"
)

TOL = 1.2e-11
N_CANDIDATES = 4
PAIR_LABELS = tuple(combinations(range(N_CANDIDATES), 2))
CANDIDATE_ORDERS = tuple(permutations(range(N_CANDIDATES)))
PAIR_ORDERS = tuple(permutations(PAIR_LABELS))
SOURCE_PATCH_M2 = 45
COMPACT_MATCHER_M2 = 621
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
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-333 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "conditional pointwise registration",
        "supplied realized-prefix content",
        "realized-state primitive supplies the pointwise reference, never the content",
        "invariant relational uniqueness",
        "symmetric local competition",
        "causal-consistency registration",
        "all 24 candidate permutations",
        "all 720 comparator orders",
        "all 24 proper-cubic frames",
        "held l=6",
        "false-event",
        "anti-splice",
        "deletion",
        "leakage",
        "undefined rather than zero actuality",
        "not a newly selected actual history",
        "not a record, clock tick, or born sample",
        "normalized law does not supply contingent member content",
        "no negative, minimum-content, wall, or axiom-pressure claim",
        "no n1–n8 gate is invoked",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the pointwise continuation-registration result and semantic firewalls",
        not missing,
        missing,
    )


@dataclass(frozen=True)
class Candidate:
    pre: int
    post: int


@dataclass(frozen=True)
class SelectionFixture:
    length: int
    program: c332.TransitionProgram
    anchor: int
    candidates: tuple[Candidate, ...]
    match: int
    ready: int


@dataclass(frozen=True)
class SelectionOutcome:
    status: str
    flags: tuple[int, ...] | None
    selected: Candidate | None
    eligibility: tuple[int, ...] | None


def active_set(program: c332.TransitionProgram) -> frozenset[int]:
    return frozenset(map(int, program.active_rows))


def build_fixture(length: int) -> SelectionFixture:
    program = c332.compile_transition_program(length)
    support = c329.build_fixture(length)
    match, ready = c329.route_outputs(support, "syndrome")
    active_nonvacuum = program.active_rows[program.nonvacuum[program.active_rows]]
    pres = tuple(map(int, active_nonvacuum[:N_CANDIDATES]))
    candidates = tuple(
        Candidate(pre, int(program.sidecar.stream_mapping[pre])) for pre in pres
    )
    return SelectionFixture(length, program, pres[0], candidates, match, ready)


def validate_selection_inputs(
    fixture: SelectionFixture,
    anchor: int,
    candidates: tuple[Candidate, ...],
    match: int,
    ready: int,
) -> None:
    if len(candidates) != N_CANDIDATES:
        raise ValueError("Cycle-333 uses exactly four physical candidate pairs")
    if match not in (0, 1) or ready not in (0, 1):
        raise ValueError("match and predecessor readiness are physical bits")
    active = active_set(fixture.program)
    if anchor not in active:
        raise ValueError("the realized-prefix anchor must be on the active event code")
    if any(candidate.pre not in active or candidate.post not in active for candidate in candidates):
        raise ValueError("every candidate boundary must be on the active event code")


def relational_equality(anchor: int, observed: int, witness: int = 0) -> int:
    if witness not in (0, 1):
        raise ValueError("the equality witness is one M2")
    return witness ^ int(anchor == observed)


def equality_full_mapping(ambient: int) -> np.ndarray:
    if ambient <= 0:
        raise ValueError("the physical boundary alphabet must be nonempty")
    pair = np.arange(ambient * ambient, dtype=np.int64)
    anchor = pair // ambient
    observed = pair % ambient
    truth = (anchor == observed).astype(np.int64)
    mapping = np.empty(2 * len(pair), dtype=np.int64)
    mapping[2 * pair] = 2 * pair + truth
    mapping[2 * pair + 1] = 2 * pair + (1 - truth)
    return mapping


def eligibility_bits(
    fixture: SelectionFixture,
    anchor: int,
    candidates: tuple[Candidate, ...],
    *,
    match: int | None = None,
    ready: int | None = None,
    deleted_transition: bool = False,
) -> tuple[int, ...]:
    match = fixture.match if match is None else match
    ready = fixture.ready if ready is None else ready
    validate_selection_inputs(fixture, anchor, candidates, match, ready)
    program = (
        c332.compile_transition_program(fixture.length, deleted=True)
        if deleted_transition
        else fixture.program
    )
    active = active_set(fixture.program)
    bits = []
    for candidate in candidates:
        transition = c332.transition_witness(
            program, candidate.pre, candidate.post
        )
        close = c332.boundary_certificate(
            int(candidate.pre in active),
            transition,
            int(candidate.post in active),
            match,
            ready,
        )
        bits.append(int(candidate.pre == anchor and close == 1))
    return tuple(bits)


def route1_unique(
    fixture: SelectionFixture,
    *,
    anchor: int | None = None,
    candidates: tuple[Candidate, ...] | None = None,
    match: int | None = None,
    ready: int | None = None,
    deleted_transition: bool = False,
    deleted_member_write: bool = False,
) -> SelectionOutcome:
    if anchor is None:
        return SelectionOutcome("undefined", None, None, None)
    candidates = fixture.candidates if candidates is None else candidates
    eligibility = eligibility_bits(
        fixture,
        anchor,
        candidates,
        match=match,
        ready=ready,
        deleted_transition=deleted_transition,
    )
    if sum(eligibility) != 1:
        return SelectionOutcome("undefined", (0,) * len(candidates), None, eligibility)
    if deleted_member_write:
        return SelectionOutcome("deleted", (0,) * len(candidates), None, eligibility)
    flags = eligibility
    selected = candidates[flags.index(1)]
    return SelectionOutcome("bound", flags, selected, eligibility)


def flag_xor_mapping(flags: tuple[int, ...]) -> np.ndarray:
    if len(flags) != N_CANDIDATES or any(bit not in (0, 1) for bit in flags):
        raise ValueError("the member flag word has four binary outputs")
    mask = sum(bit << index for index, bit in enumerate(flags))
    states = np.arange(2**N_CANDIDATES, dtype=np.int64)
    return states ^ mask


def pair_record_mask(left: int, right: int) -> int:
    if left not in (0, 1) or right not in (0, 1):
        raise ValueError("competition scores are binary eligibility bits")
    return int(left >= right) | (int(right >= left) << 1)


def pair_record_mapping(left: int, right: int) -> np.ndarray:
    mask = pair_record_mask(left, right)
    states = np.arange(4, dtype=np.int64)
    return states ^ mask


def route2_competition(
    fixture: SelectionFixture,
    *,
    anchor: int | None = None,
    candidates: tuple[Candidate, ...] | None = None,
    match: int | None = None,
    ready: int | None = None,
    pair_order: tuple[tuple[int, int], ...] = PAIR_LABELS,
    deleted_pair: tuple[int, int] | None = None,
) -> SelectionOutcome:
    if anchor is None:
        return SelectionOutcome("undefined", None, None, None)
    if len(pair_order) != len(PAIR_LABELS) or set(pair_order) != set(PAIR_LABELS):
        raise ValueError("the competition schedule must apply each unordered pair once")
    if deleted_pair is not None and deleted_pair not in PAIR_LABELS:
        raise ValueError("the deleted comparator must be one declared pair")
    candidates = fixture.candidates if candidates is None else candidates
    eligibility = eligibility_bits(
        fixture,
        anchor,
        candidates,
        match=match,
        ready=ready,
    )
    records: dict[tuple[int, int], int] = {}
    for pair in pair_order:
        if pair == deleted_pair:
            continue
        left, right = pair
        records[pair] = pair_record_mask(eligibility[left], eligibility[right])
    winners = []
    for candidate in range(N_CANDIDATES):
        wins = eligibility[candidate] == 1
        for other in range(N_CANDIDATES):
            if other == candidate:
                continue
            pair = (min(candidate, other), max(candidate, other))
            if pair not in records:
                wins = False
                continue
            mask = records[pair]
            candidate_ge = (mask & 1) if candidate < other else ((mask >> 1) & 1)
            other_ge = ((mask >> 1) & 1) if candidate < other else (mask & 1)
            wins = wins and candidate_ge == 1 and other_ge == 0
        winners.append(int(wins))
    flags = tuple(winners)
    if sum(flags) != 1:
        return SelectionOutcome("undefined", (0,) * N_CANDIDATES, None, eligibility)
    selected = candidates[flags.index(1)]
    return SelectionOutcome("bound", flags, selected, eligibility)


MEMBER_NODES = frozenset(
    (
        "realized_prefix",
        "candidate_bank",
        "transition_truth",
        "identity_match",
        "predecessor_ready",
        "relational_unique",
        "member_binding",
    )
)
MEMBER_EDGES = frozenset(
    (
        ("candidate_bank", "transition_truth"),
        ("realized_prefix", "relational_unique"),
        ("candidate_bank", "relational_unique"),
        ("transition_truth", "relational_unique"),
        ("identity_match", "relational_unique"),
        ("predecessor_ready", "relational_unique"),
        ("relational_unique", "member_binding"),
    )
)
MEMBER_DAG = c287.Dag(MEMBER_NODES, MEMBER_EDGES)


def route3_causal(fixture: SelectionFixture) -> dict[str, object]:
    route1 = route1_unique(fixture, anchor=fixture.anchor)
    schedules = tuple(c287.topological_orders(MEMBER_DAG))
    local = {node: True for node in MEMBER_NODES}
    outcomes = tuple(c287.replay_dag(MEMBER_DAG, order, local) for order in schedules)
    edge_rows = []
    for edge in sorted(MEMBER_EDGES):
        formed = c287.replay_dag(
            MEMBER_DAG,
            schedules[0],
            local,
            MEMBER_EDGES - {edge},
        )
        edge_rows.append((edge, "member_binding" in formed))
    false_rows = []
    for node in (
        "realized_prefix",
        "transition_truth",
        "identity_match",
        "predecessor_ready",
        "relational_unique",
    ):
        changed = dict(local)
        changed[node] = False
        formed = c287.replay_dag(MEMBER_DAG, schedules[0], changed)
        false_rows.append((node, "member_binding" in formed))
    return {
        "selection": route1,
        "topological_orders": len(schedules),
        "terminal_sets": len(set(outcomes)),
        "all_nodes_form": all(outcome == MEMBER_NODES for outcome in outcomes),
        "edge_deletion_member_survivors": sum(int(row[1]) for row in edge_rows),
        "predicate_deletion_member_survivors": sum(int(row[1]) for row in false_rows),
    }


def source_and_physical_gate_controls() -> dict[int, SelectionFixture]:
    fixtures = {length: build_fixture(length) for length in (3, 6)}
    rows = []
    equality_mapping = equality_full_mapping(1020)
    equality_identity = np.arange(len(equality_mapping), dtype=np.int64)
    for length, fixture in fixtures.items():
        program = fixture.program
        encoding = program.sidecar.event_encoding
        active = program.active_rows
        nonvacuum = active[program.nonvacuum[active]]
        lawful = tuple(
            c332.transition_witness(
                program,
                int(pre),
                int(program.sidecar.stream_mapping[pre]),
            )
            for pre in nonvacuum
        )
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "event_isometry_residual": float(
                    np.linalg.norm(encoding.conj().T @ encoding - np.eye(encoding.shape[1]))
                ),
                "event_constraint_residual": float(
                    np.linalg.norm(program.sidecar.constraint_signs[:, None] * encoding - encoding)
                ),
                "ambient_rows": len(program.sidecar.stream_mapping),
                "active_rows": len(active),
                "lawful_nonvacuum_transitions": len(nonvacuum),
                "lawful_transition_false_negatives": len(lawful) - sum(lawful),
                "match_ready": (fixture.match, fixture.ready),
            }
        )
    check(
        "the actual Cycle-314 physical transition and Cycle-329 match/readiness inputs survive trained and held size",
        all(
            row["event_isometry_residual"] < TOL
            and row["event_constraint_residual"] < TOL
            and row["ambient_rows"] == 1020
            and row["active_rows"] == 510
            and row["lawful_nonvacuum_transitions"] == 508
            and row["lawful_transition_false_negatives"] == 0
            and row["match_ready"] == (1, 1)
            for row in rows
        ),
        rows,
    )
    check(
        "the physical relational equality gate is an exact bounded involutive permutation on two actual boundary registers and one witness",
        np.array_equal(equality_mapping[equality_mapping], equality_identity),
        {
            "ambient_boundary_rows": 1020,
            "permutation_rows": len(equality_mapping),
            "involution_failures": int(
                np.count_nonzero(equality_mapping[equality_mapping] != equality_identity)
            ),
            "maximum_gate_support_M2": 2 * SOURCE_PATCH_M2 + 1,
        },
    )
    return fixtures


def route1_controls(fixtures: dict[int, SelectionFixture]) -> dict[str, object]:
    rows = []
    order_failures = permutation_failures = involution_failures = 0
    for fixture in fixtures.values():
        expected = fixture.candidates[0]
        base = route1_unique(fixture, anchor=fixture.anchor)
        for order in CANDIDATE_ORDERS:
            bank = tuple(fixture.candidates[index] for index in order)
            output = route1_unique(fixture, anchor=fixture.anchor, candidates=bank)
            order_failures += output.status != "bound" or output.selected != expected
        mapping = flag_xor_mapping(base.flags or (0,) * N_CANDIDATES)
        identity = np.arange(len(mapping), dtype=np.int64)
        permutation_failures += len(mapping) - len(np.unique(mapping))
        involution_failures += int(np.count_nonzero(mapping[mapping] != identity))
        changed = route1_unique(fixture, anchor=fixture.candidates[2].pre)
        deleted_anchor = route1_unique(fixture, anchor=None)
        duplicate_bank = (
            fixture.candidates[0],
            fixture.candidates[0],
            fixture.candidates[2],
            fixture.candidates[3],
        )
        duplicate = route1_unique(
            fixture,
            anchor=fixture.anchor,
            candidates=duplicate_bank,
        )
        rows.append(
            {
                "L": fixture.length,
                "held": fixture.length == 6,
                "base": base,
                "changed_anchor": changed,
                "deleted_anchor": deleted_anchor,
                "duplicate": duplicate,
            }
        )
    detail = {
        "rows": rows,
        "candidate_permutation_tests": len(fixtures) * len(CANDIDATE_ORDERS),
        "candidate_permutation_failures": order_failures,
        "member_mapping_permutation_failures": permutation_failures,
        "member_mapping_involution_failures": involution_failures,
        "conservative_route_support_M2": (
            9 * SOURCE_PATCH_M2 + COMPACT_MATCHER_M2 + 40
        ),
        "host_selection_queries": 0,
    }
    check(
        "route 1 binds the unique relational continuation under all candidate permutations and changes covariantly with supplied prefix content",
        all(
            row["base"].status == "bound"
            and row["base"].selected == fixtures[row["L"]].candidates[0]
            and row["changed_anchor"].status == "bound"
            and row["changed_anchor"].selected == fixtures[row["L"]].candidates[2]
            and row["deleted_anchor"].status == "undefined"
            and row["deleted_anchor"].flags is None
            and row["duplicate"].status == "undefined"
            and row["duplicate"].selected is None
            for row in rows
        )
        and order_failures == permutation_failures == involution_failures == 0
        and detail["host_selection_queries"] == 0,
        detail,
    )
    return detail


def route2_controls(fixtures: dict[int, SelectionFixture]) -> dict[str, object]:
    rows = []
    schedule_failures = candidate_order_failures = pair_gate_failures = 0
    for fixture in fixtures.values():
        expected = fixture.candidates[0]
        for pair_order in PAIR_ORDERS:
            output = route2_competition(
                fixture,
                anchor=fixture.anchor,
                pair_order=pair_order,
            )
            schedule_failures += output.status != "bound" or output.selected != expected
        for order in CANDIDATE_ORDERS:
            bank = tuple(fixture.candidates[index] for index in order)
            output = route2_competition(
                fixture,
                anchor=fixture.anchor,
                candidates=bank,
            )
            candidate_order_failures += output.status != "bound" or output.selected != expected
        eligibility = eligibility_bits(fixture, fixture.anchor, fixture.candidates)
        for left, right in PAIR_LABELS:
            mapping = pair_record_mapping(eligibility[left], eligibility[right])
            identity = np.arange(len(mapping), dtype=np.int64)
            pair_gate_failures += int(np.count_nonzero(mapping[mapping] != identity))
            pair_gate_failures += len(mapping) - len(np.unique(mapping))
        winner_index = fixture.candidates.index(expected)
        winner_pairs = tuple(pair for pair in PAIR_LABELS if winner_index in pair)
        deleted = tuple(
            route2_competition(
                fixture,
                anchor=fixture.anchor,
                deleted_pair=pair,
            )
            for pair in winner_pairs
        )
        duplicate_bank = (
            fixture.candidates[0],
            fixture.candidates[0],
            fixture.candidates[2],
            fixture.candidates[3],
        )
        duplicate = route2_competition(
            fixture,
            anchor=fixture.anchor,
            candidates=duplicate_bank,
        )
        rows.append(
            {
                "L": fixture.length,
                "held": fixture.length == 6,
                "winner_pair_deletions": deleted,
                "duplicate_tie": duplicate,
            }
        )
    detail = {
        "rows": rows,
        "pair_comparator_orders": len(fixtures) * len(PAIR_ORDERS),
        "pair_comparator_order_failures": schedule_failures,
        "candidate_permutation_tests": len(fixtures) * len(CANDIDATE_ORDERS),
        "candidate_permutation_failures": candidate_order_failures,
        "pair_gate_permutation_or_involution_failures": pair_gate_failures,
        "pair_record_M2": 2 * len(PAIR_LABELS),
        "host_selection_queries": 0,
    }
    check(
        "route 2 gives the same unique-or-undefined winner under all 720 local comparator orders with no priority tie break",
        schedule_failures == candidate_order_failures == pair_gate_failures == 0
        and all(
            all(outcome.status == "undefined" for outcome in row["winner_pair_deletions"])
            and row["duplicate_tie"].status == "undefined"
            and row["duplicate_tie"].selected is None
            for row in rows
        )
        and detail["host_selection_queries"] == 0,
        detail,
    )
    return detail


def route3_controls(fixtures: dict[int, SelectionFixture]) -> dict[str, object]:
    rows = {length: route3_causal(fixture) for length, fixture in fixtures.items()}
    check(
        "route 3 registers the same continuation through a schedule-invariant causal-consistency DAG with every dependency load bearing",
        all(
            row["selection"].status == "bound"
            and row["topological_orders"] > 1
            and row["terminal_sets"] == 1
            and row["all_nodes_form"]
            and row["edge_deletion_member_survivors"] == 0
            and row["predicate_deletion_member_survivors"] == 0
            for row in rows.values()
        ),
        rows,
    )
    return rows


def false_event_deletion_and_domain_controls(
    fixtures: dict[int, SelectionFixture],
) -> dict[str, object]:
    rows = []
    for fixture in fixtures.values():
        candidate = fixture.candidates[0]
        other = fixture.candidates[1]
        spliced_bank = list(fixture.candidates)
        spliced_bank[0] = Candidate(candidate.pre, other.post)
        h_only_bank = list(fixture.candidates)
        h_only_bank[0] = Candidate(candidate.pre, candidate.post ^ 1)
        try:
            h_only = route1_unique(
                fixture,
                anchor=fixture.anchor,
                candidates=tuple(h_only_bank),
            )
        except ValueError:
            h_only = SelectionOutcome("rejected", None, None, None)
        support = c329.build_fixture(fixture.length)
        corrupted_target = list(support.words[4].word)
        corrupted_target[c329.LABEL_BITS] ^= 1
        bad_match, good_ready = c329.route_outputs(
            support,
            "syndrome",
            target_word=tuple(corrupted_target),
        )
        good_match, bad_ready = c329.route_outputs(
            support,
            "syndrome",
            closed=(1, 1, 0),
        )
        rows.append(
            {
                "L": fixture.length,
                "spliced": route1_unique(
                    fixture,
                    anchor=fixture.anchor,
                    candidates=tuple(spliced_bank),
                ),
                "h_only": h_only,
                "anti_splice": route1_unique(
                    fixture,
                    anchor=fixture.anchor,
                    match=bad_match,
                    ready=good_ready,
                ),
                "readiness_deleted": route1_unique(
                    fixture,
                    anchor=fixture.anchor,
                    match=good_match,
                    ready=bad_ready,
                ),
                "transition_deleted": route1_unique(
                    fixture,
                    anchor=fixture.anchor,
                    deleted_transition=True,
                ),
                "member_write_deleted": route1_unique(
                    fixture,
                    anchor=fixture.anchor,
                    deleted_member_write=True,
                ),
            }
        )
    rejected = 0
    invalid = (
        lambda: build_fixture(2),
        lambda: build_fixture(7),
        lambda: route1_unique(fixtures[3], anchor=-1),
        lambda: route1_unique(
            fixtures[3],
            anchor=fixtures[3].anchor,
            candidates=fixtures[3].candidates[:3],
        ),
        lambda: route1_unique(fixtures[3], anchor=fixtures[3].anchor, match=2),
        lambda: route2_competition(
            fixtures[3],
            anchor=fixtures[3].anchor,
            pair_order=PAIR_LABELS[:-1],
        ),
        lambda: relational_equality(0, 0, witness=2),
        lambda: equality_full_mapping(0),
    )
    for call in invalid:
        try:
            call()
        except (ValueError, IndexError):
            rejected += 1
    detail = {
        "rows": rows,
        "lawful_domain_rejections": rejected,
        "lawful_domain_attempts": len(invalid),
    }
    check(
        "false-event anti-splice readiness transition member-write and lawful-domain controls suppress or reject binding without assigning zero actuality",
        all(
            row["spliced"].status == "undefined"
            and row["h_only"].status in ("undefined", "rejected")
            and row["anti_splice"].status == "undefined"
            and row["readiness_deleted"].status == "undefined"
            and row["transition_deleted"].status == "undefined"
            and row["member_write_deleted"].status == "deleted"
            for row in rows
        )
        and rejected == len(invalid),
        detail,
    )
    return detail


def held_frame_covariance_controls(fixtures: dict[int, SelectionFixture]) -> dict[str, object]:
    failures = mapping_failures = code_failures = 0
    cases = 0
    for fixture in fixtures.values():
        expected = fixture.candidates[0]
        for frame in c314.c311.c235.proper_cubic_frames():
            mapping, frame_failures = c332.event_frame_mapping(fixture.program.sidecar, frame)
            mapping_failures += frame_failures
            anchor = int(mapping[fixture.anchor])
            candidates = tuple(
                Candidate(int(mapping[item.pre]), int(mapping[item.post]))
                for item in fixture.candidates
            )
            support = c329.build_fixture(fixture.length, frame)
            match, ready = c329.route_outputs(support, "syndrome")
            mapped_expected = Candidate(
                int(mapping[expected.pre]),
                int(mapping[expected.post]),
            )
            active = active_set(fixture.program)
            code_failures += int(
                anchor not in active
                or any(item.pre not in active or item.post not in active for item in candidates)
            )
            for order in CANDIDATE_ORDERS:
                bank = tuple(candidates[index] for index in order)
                first = route1_unique(
                    fixture,
                    anchor=anchor,
                    candidates=bank,
                    match=match,
                    ready=ready,
                )
                second = route2_competition(
                    fixture,
                    anchor=anchor,
                    candidates=bank,
                    match=match,
                    ready=ready,
                )
                failures += int(
                    first.status != "bound"
                    or second.status != "bound"
                    or first.selected != mapped_expected
                    or second.selected != mapped_expected
                )
                cases += 1
    detail = {
        "frame_size_candidate_order_cases": cases,
        "proper_cubic_frames_per_size": 24,
        "mapping_failures": mapping_failures,
        "active_code_failures": code_failures,
        "selection_covariance_failures": failures,
        "held_size": 6,
    }
    check(
        "both pointwise selectors commute with all 24 proper-cubic frames at trained and held size for every candidate ordering",
        cases == 2 * 24 * len(CANDIDATE_ORDERS)
        and mapping_failures == code_failures == failures == 0,
        detail,
    )
    return detail


def far_side_receiving_controls(fixtures: dict[int, SelectionFixture]) -> dict[str, object]:
    realized = normalized(REALIZED)
    cycle30 = normalized(CYCLE30)
    cycle243 = normalized(CYCLE243)
    cycle194 = normalized(CYCLE194)
    symmetric_law = c27.MU
    frozen = c194.frozen_law({0: Fraction(1, 2), 1: Fraction(1, 2)}, 4)
    selected = route1_unique(fixtures[3], anchor=fixtures[3].anchor)
    deleted_anchor = route1_unique(fixtures[3], anchor=None)
    clock_ratio = c243.relative_clock_ratio(1, 1, matched=False)
    detail = {
        "realized_slot_present": "one realized-state reference" in realized,
        "primitive_has_no_selector": "not a state-selection rule" in realized,
        "Cycle30_actuality_interface": "actuality interface" in cycle30,
        "Cycle243_typed_chain": "typed chain of partial maps" in cycle243,
        "Cycle194_member_separate": "actual-history membership remains separate" in cycle194,
        "symmetric_law_normalized": c27.law_normalized(symmetric_law),
        "symmetric_law_swap_invariant": c27.pushforward_history_law(symmetric_law) == symmetric_law,
        "symmetric_history_fixed_points": sum(
            c27.swap_history(history) == history for history in symmetric_law
        ),
        "frozen_law_total": c194.law_total(frozen),
        "frozen_law_members": len(frozen),
        "pointwise_registration": selected.status,
        "deleted_anchor_registration": deleted_anchor.status,
        "record_typed": False,
        "clock_ratio_without_Record_chain_and_matcher": clock_ratio,
        "Born_grade_formed": False,
    }
    check(
        "the bounded continuation registration uses the existing realized-state reference while Record clock and Born receiving contracts remain separately typed",
        all(
            (
                detail["realized_slot_present"],
                detail["primitive_has_no_selector"],
                detail["Cycle30_actuality_interface"],
                detail["Cycle243_typed_chain"],
                detail["Cycle194_member_separate"],
                detail["symmetric_law_normalized"],
                detail["symmetric_law_swap_invariant"],
            )
        )
        and detail["symmetric_history_fixed_points"] == 0
        and detail["frozen_law_total"] == 1
        and detail["frozen_law_members"] == 2
        and detail["pointwise_registration"] == "bound"
        and detail["deleted_anchor_registration"] == "undefined"
        and detail["record_typed"] is False
        and detail["clock_ratio_without_Record_chain_and_matcher"] is None
        and detail["Born_grade_formed"] is False,
        detail,
    )
    return detail


def inventory_controls() -> None:
    text = normalized(NOTE)
    check(
        "the exact supplied and derived inventory keeps the prefix content program capacity typing clock and probability interfaces explicit",
        "supplied-structure inventory" in text
        and "realized-prefix boundary content" in text
        and "fixed equality, transition, close, competition, and dag coefficient tables" in text
        and "candidate boundary registers and fresh work/output m2" in text
        and "record typing is absent" in text
        and "clock matcher and calibration are absent" in text
        and "born grade and normalized member weights are absent" in text
        and "derived continuation-membership flag" in text,
        {
            "boundary_bank_M2": 9 * SOURCE_PATCH_M2,
            "compact_matcher_M2": COMPACT_MATCHER_M2,
            "route1_conservative_total_M2": 9 * SOURCE_PATCH_M2 + COMPACT_MATCHER_M2 + 40,
            "primitive_application": "supplied",
            "host_selection_queries": 0,
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    fixtures = source_and_physical_gate_controls()
    route1 = route1_controls(fixtures)
    route2 = route2_controls(fixtures)
    route3 = route3_controls(fixtures)
    deletions = false_event_deletion_and_domain_controls(fixtures)
    covariance = held_frame_covariance_controls(fixtures)
    far_side = far_side_receiving_controls(fixtures)
    inventory_controls()
    check(
        "Cycle 333 gives three bounded conditional pointwise continuation-registration routes without promoting the output to actual-history selection, Record, clock, or Born selection",
        route1["candidate_permutation_failures"] == 0
        and route2["pair_comparator_order_failures"] == 0
        and all(row["edge_deletion_member_survivors"] == 0 for row in route3.values())
        and deletions["lawful_domain_rejections"] == deletions["lawful_domain_attempts"]
        and covariance["selection_covariance_failures"] == 0
        and far_side["record_typed"] is False
        and "no negative, minimum-content, wall, or axiom-pressure claim" in normalized(NOTE)
        and "no n1–n8 gate is invoked" in normalized(NOTE),
        {
            "invariant_relational_uniqueness": "positive conditional",
            "symmetric_local_competition": "positive conditional",
            "causal_consistency": "positive conditional",
            "actuality_slot": "approved primitive; not a wall",
        },
    )
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE333_POINTWISE_CONTINUATION_REGISTRATION_GREEN" if FAIL == 0 else "CYCLE333_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
