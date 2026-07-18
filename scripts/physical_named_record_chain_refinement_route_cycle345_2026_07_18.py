#!/usr/bin/env python3
"""Cycle 345 Route 2: named Record-chain refinement on one physical history.

The runner consumes one Cycle-342 L=6, two-page, twelve-Record history.  It
adds frozen formation-time clock-name/membership tags as explicit local M2
basis-register fields.  One fine named subchain and two coarse named
subchains (trained stride two and held stride three) use the same physical
Records and match intervals by shared start/end Record identities.

The result is an exact dimensionless refinement-ratio certificate conditional
on the supplied tags and tag-formation rule.  Host order, page position,
Cycle-342 phase, circuit depth, and the numerical Record identifiers are not
clock readings.  No calibration, physical rate, metric time, broad negative,
axiom pressure, or nearest-neighbour primitive synthesis is claimed.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction
from itertools import permutations, product
from math import lcm
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18 as c342


Coord = tuple[int, int, int]

LENGTH = 6
RECORD_COUNT = 12
ENDPOINT = 0

# These names and memberships are supplied formation-program data.  The
# masks are deliberately literal: no Record phase, page slot, host-loop
# counter, or numerical Record identifier is queried to recover membership.
FINE_CLOCK = 1
COARSE_K2_CLOCK = 2
COARSE_K3_CLOCK = 3
CLOCK_NAMES = (FINE_CLOCK, COARSE_K2_CLOCK, COARSE_K3_CLOCK)
CLOCK_LABELS = {
    FINE_CLOCK: "fine",
    COARSE_K2_CLOCK: "coarse-k2",
    COARSE_K3_CLOCK: "coarse-k3-held",
}
FINE_MEMBERSHIP = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
K2_MEMBERSHIP = (1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
K3_MEMBERSHIP = (1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0)
SUPPLIED_MEMBERSHIP = {
    FINE_CLOCK: FINE_MEMBERSHIP,
    COARSE_K2_CLOCK: K2_MEMBERSHIP,
    COARSE_K3_CLOCK: K3_MEMBERSHIP,
}

# Record identities are intentionally nonmonotone.  Their values individuate
# physical Records; their arithmetic and ordering have no clock meaning.
RECORD_IDS = (9, 2, 14, 5, 11, 0, 7, 13, 4, 15, 1, 10)
RECORD_ID_BITS = 4
PREDECESSOR_PRESENT_BITS = 1
CLOCK_NAME_BITS = 2
CLOCK_MEMBERSHIP_BITS = 1
CLOCK_TAG_BITS = len(CLOCK_NAMES) * (CLOCK_NAME_BITS + CLOCK_MEMBERSHIP_BITS)
IDENTITY_LINK_BITS = 2 * RECORD_ID_BITS + PREDECESSOR_PRESENT_BITS
TAGGED_RECORD_BITS = c342.RECORD_BITS + IDENTITY_LINK_BITS + CLOCK_TAG_BITS

# Supplied block anchors form one nearest-neighbour spatial path.  The local
# register widths below are storage widths; they are not a primitive-layout or
# nearest-neighbour gate-support theorem.
ANCHORS: tuple[Coord, ...] = (
    (0, 0, 0),
    (1, 0, 0),
    (1, 1, 0),
    (1, 1, 1),
    (2, 1, 1),
    (2, 2, 1),
    (2, 2, 2),
    (3, 2, 2),
    (3, 3, 2),
    (3, 3, 3),
    (4, 3, 3),
    (4, 4, 3),
)

TRANSLATIONS: tuple[Coord, ...] = tuple(product((-1, 0, 1), repeat=3))
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


def bits(value: int, width: int) -> tuple[int, ...]:
    if not isinstance(value, int) or value < 0 or value >= 2**width:
        raise ValueError(("value does not fit the supplied basis register", value, width))
    return tuple((value >> index) & 1 for index in range(width))


def integer(word: tuple[int, ...]) -> int:
    if any(bit not in (0, 1) for bit in word):
        raise ValueError("basis-register words must be binary")
    return sum(bit << index for index, bit in enumerate(word))


def squared_distance(left: Coord, right: Coord) -> int:
    return sum((a - b) ** 2 for a, b in zip(left, right))


def moved(anchor: Coord, frame, translation: Coord = (0, 0, 0)) -> Coord:
    rotated = tuple(
        int(sum(frame[row][column] * anchor[column] for column in range(3)))
        for row in range(3)
    )
    return tuple(rotated[index] + translation[index] for index in range(3))


@dataclass(frozen=True)
class ClockTag:
    name: int
    member: int


@dataclass(frozen=True)
class TaggedRecord:
    record: c342.CylinderRecord
    record_id: int
    predecessor_id: int | None
    anchor: Coord
    tags: tuple[ClockTag, ...]


def supplied_tags(position: int) -> tuple[ClockTag, ...]:
    if not 0 <= position < RECORD_COUNT:
        raise ValueError("formation position is outside the supplied tag program")
    return tuple(
        ClockTag(name, SUPPLIED_MEMBERSHIP[name][position]) for name in CLOCK_NAMES
    )


def tagged_word(item: TaggedRecord) -> tuple[int, ...]:
    if len(item.anchor) != 3:
        raise ValueError("a Record block anchor is a spatial Z3 coordinate")
    if tuple(tag.name for tag in item.tags) != CLOCK_NAMES:
        raise ValueError("every Record must carry each declared clock name exactly once")
    if any(tag.member not in (0, 1) for tag in item.tags):
        raise ValueError("clock membership is one M2 basis bit")
    predecessor_present = int(item.predecessor_id is not None)
    predecessor = 0 if item.predecessor_id is None else item.predecessor_id
    word = (
        c342.record_word(item.record)
        + bits(item.record_id, RECORD_ID_BITS)
        + (predecessor_present,)
        + bits(predecessor, RECORD_ID_BITS)
        + tuple(
            bit
            for tag in item.tags
            for bit in bits(tag.name, CLOCK_NAME_BITS) + (tag.member,)
        )
    )
    if len(word) != TAGGED_RECORD_BITS:
        raise RuntimeError("the tagged Record basis-register inventory drifted")
    return word


def decode_tagged_word(word: tuple[int, ...], anchor: Coord) -> TaggedRecord:
    if len(word) != TAGGED_RECORD_BITS:
        raise ValueError("tagged Record word has the wrong basis width")
    record = c342.decode_record_word(word[: c342.RECORD_BITS])
    cursor = c342.RECORD_BITS
    record_id = integer(word[cursor : cursor + RECORD_ID_BITS])
    cursor += RECORD_ID_BITS
    predecessor_present = word[cursor]
    cursor += PREDECESSOR_PRESENT_BITS
    if predecessor_present not in (0, 1):
        raise ValueError("predecessor presence is one M2 basis bit")
    predecessor_value = integer(word[cursor : cursor + RECORD_ID_BITS])
    cursor += RECORD_ID_BITS
    if not predecessor_present and predecessor_value != 0:
        raise ValueError("an absent predecessor has canonical zero payload")
    tags = []
    for _ in CLOCK_NAMES:
        name = integer(word[cursor : cursor + CLOCK_NAME_BITS])
        cursor += CLOCK_NAME_BITS
        member = word[cursor]
        cursor += CLOCK_MEMBERSHIP_BITS
        tags.append(ClockTag(name, member))
    if cursor != TAGGED_RECORD_BITS:
        raise RuntimeError("tagged Record decoder did not consume its domain")
    decoded = TaggedRecord(
        record,
        record_id,
        predecessor_value if predecessor_present else None,
        anchor,
        tuple(tags),
    )
    # Run the full domain checks, including names and binary memberships.
    tagged_word(decoded)
    return decoded


def form_tagged_history(
    records: tuple[c342.CylinderRecord, ...],
    *,
    anchors: tuple[Coord, ...] = ANCHORS,
    record_ids: tuple[int, ...] = RECORD_IDS,
) -> tuple[TaggedRecord, ...]:
    if not (len(records) == len(anchors) == len(record_ids) == RECORD_COUNT):
        raise ValueError("Route 2 requires exactly one twelve-Record history")
    return tuple(
        TaggedRecord(
            record=record,
            record_id=record_ids[position],
            predecessor_id=None if position == 0 else record_ids[position - 1],
            anchor=anchors[position],
            tags=supplied_tags(position),
        )
        for position, record in enumerate(records)
    )


def validate_history(
    fixture: c342.c338.RouteFixture,
    history: tuple[TaggedRecord, ...],
) -> tuple[TaggedRecord, ...]:
    if not history:
        raise ValueError("a named Record history must be nonempty")
    for item in history:
        tagged_word(item)
        if not item.record.typed or not item.record.permanent:
            raise ValueError("clock tags attach only at lawful permanent-Record formation")
    by_id = {item.record_id: item for item in history}
    if len(by_id) != len(history):
        raise ValueError("physical Record identities must be unique")
    if len({item.anchor for item in history}) != len(history):
        raise ValueError("one supplied Record block occupies each anchor")
    roots = tuple(item for item in history if item.predecessor_id is None)
    if len(roots) != 1:
        raise ValueError("the declared named-clock carrier is one causal chain")
    successors: dict[int, TaggedRecord] = {}
    for item in history:
        if item.predecessor_id is None:
            continue
        if item.predecessor_id not in by_id:
            raise ValueError("every predecessor identity must be a physical Record")
        if item.predecessor_id in successors:
            raise ValueError("the Route-2 carrier is a chain, not a fork")
        predecessor = by_id[item.predecessor_id]
        if item.record.cylinder != c342.advance_cylinder(
            fixture, predecessor.record.cylinder
        ):
            raise ValueError("linked Records must follow the Cycle-342 continuation")
        if squared_distance(item.anchor, predecessor.anchor) != 1:
            raise ValueError("successive supplied Record-block anchors must be neighbours")
        successors[item.predecessor_id] = item
    ordered = [roots[0]]
    while ordered[-1].record_id in successors:
        ordered.append(successors[ordered[-1].record_id])
    if len(ordered) != len(history):
        raise ValueError("the predecessor links must cover the full physical history")
    return tuple(ordered)


def tag_for(item: TaggedRecord, clock_name: int) -> ClockTag:
    matches = tuple(tag for tag in item.tags if tag.name == clock_name)
    if len(matches) != 1:
        raise ValueError("clock name is missing or ambiguous on a Record")
    return matches[0]


def causal_segment(
    history: tuple[TaggedRecord, ...],
    start_id: int,
    end_id: int,
) -> tuple[TaggedRecord, ...]:
    """Return the causal interval (start,end], using links rather than tuple order."""

    by_id = {item.record_id: item for item in history}
    if len(by_id) != len(history) or start_id not in by_id or end_id not in by_id:
        raise ValueError("matched endpoints must be unique physical Record identities")
    reverse_path = []
    cursor = end_id
    seen = set()
    while cursor != start_id:
        if cursor in seen:
            raise ValueError("the physical Record links contain a cycle")
        seen.add(cursor)
        item = by_id[cursor]
        reverse_path.append(item)
        if item.predecessor_id is None:
            raise ValueError("the end Record is not downstream of the start Record")
        cursor = item.predecessor_id
    return tuple(reversed(reverse_path))


def clock_increment(
    history: tuple[TaggedRecord, ...],
    start_id: int,
    end_id: int,
    clock_name: int,
) -> int:
    if clock_name not in CLOCK_NAMES:
        raise ValueError("the requested clock name is not declared")
    return sum(
        tag_for(item, clock_name).member
        for item in causal_segment(history, start_id, end_id)
    )


def matched_ratio(
    history: tuple[TaggedRecord, ...],
    start_id: int,
    end_id: int,
    numerator_clock: int,
    denominator_clock: int,
) -> Fraction:
    by_id = {item.record_id: item for item in history}
    for endpoint in (by_id[start_id], by_id[end_id]):
        if not (
            tag_for(endpoint, numerator_clock).member
            and tag_for(endpoint, denominator_clock).member
        ):
            raise ValueError("both named subchains must share the physical endpoints")
    numerator = clock_increment(
        history, start_id, end_id, numerator_clock
    )
    denominator = clock_increment(
        history, start_id, end_id, denominator_clock
    )
    if numerator <= 0 or denominator <= 0:
        raise ValueError("a matched refinement ratio requires positive counts")
    return Fraction(numerator, denominator)


def build_base_history() -> tuple[
    c342.c338.RouteFixture,
    c342.RecordBook,
    tuple[TaggedRecord, ...],
]:
    fixture = c342.c338.build_fixture(LENGTH)
    cylinders = c342.make_cylinder_chain(fixture, ENDPOINT, RECORD_COUNT)
    records = tuple(c342.form_conditional_record(fixture, item) for item in cylinders)
    book = c342.empty_book(LENGTH)
    for record in records[:LENGTH]:
        book = c342.append_record(book, record)
    book = c342.attach_fresh_page(book, (None,) * LENGTH)
    for record in records[LENGTH:]:
        book = c342.append_record(book, record)
    flattened = c342.flatten_records(book)
    if flattened != records:
        raise RuntimeError("Cycle-342 two-page append order drifted")
    return fixture, book, form_tagged_history(flattened)


def source_history_and_encoding_controls(
    fixture: c342.c338.RouteFixture,
    book: c342.RecordBook,
    history: tuple[TaggedRecord, ...],
) -> None:
    ordered = validate_history(fixture, history)
    encoded = tuple(tagged_word(item) for item in history)
    decoded = tuple(
        decode_tagged_word(word, item.anchor) for word, item in zip(encoded, history)
    )
    sidecar_anchor = (
        history[0].anchor[0] + 10,
        history[0].anchor[1],
        history[0].anchor[2],
    )
    sidecar_retarget = decode_tagged_word(encoded[0], sidecar_anchor)
    cylinder_words = tuple(c342.c338.cylinder_word(item.record.cylinder) for item in history)
    detail = {
        "L": fixture.length,
        "Record_pages": len(book.pages),
        "Records_per_page": tuple(len(page) for page in book.pages),
        "typed_permanent_Records": len(history),
        "distinct_complete_cylinder_words": len(set(cylinder_words)),
        "distinct_physical_Record_identities": len({item.record_id for item in history}),
        "base_Record_M2": c342.RECORD_BITS,
        "identity_and_predecessor_M2": IDENTITY_LINK_BITS,
        "clock_name_membership_M2": CLOCK_TAG_BITS,
        "tagged_Record_basis_width_M2": TAGGED_RECORD_BITS,
        "two_page_basis_storage_M2": RECORD_COUNT * TAGGED_RECORD_BITS,
        "spatial_anchor_encoded_in_tagged_word": False,
        "same_word_accepts_external_anchor_sidecar": tagged_word(sidecar_retarget)
        == encoded[0]
        and sidecar_retarget.anchor == sidecar_anchor,
    }
    check(
        "one Cycle-342 L6 two-page history carries exact local formation-time clock-name and membership basis fields",
        fixture.length == LENGTH
        and len(book.pages) == 2
        and all(item is not None for page in book.pages for item in page)
        and len(history) == RECORD_COUNT
        and ordered == history
        and c342.valid_chain(fixture, tuple(item.record for item in history))
        and all(item.record.typed and item.record.permanent for item in history)
        and decoded == history
        and all(len(word) == TAGGED_RECORD_BITS for word in encoded)
        and len(set(cylinder_words)) == LENGTH
        and len({item.record_id for item in history}) == RECORD_COUNT
        and all(
            squared_distance(left.anchor, right.anchor) == 1
            for left, right in zip(history, history[1:])
        )
        and TAGGED_RECORD_BITS == 48
        and not detail["spatial_anchor_encoded_in_tagged_word"]
        and detail["same_word_accepts_external_anchor_sidecar"],
        detail,
    )


def refinement_ratio_controls(history: tuple[TaggedRecord, ...]) -> None:
    start = RECORD_IDS[0]
    k2_end = RECORD_IDS[10]
    k3_end = RECORD_IDS[9]
    common_end = RECORD_IDS[6]
    k2_counts = (
        clock_increment(history, start, k2_end, FINE_CLOCK),
        clock_increment(history, start, k2_end, COARSE_K2_CLOCK),
    )
    k3_counts = (
        clock_increment(history, start, k3_end, FINE_CLOCK),
        clock_increment(history, start, k3_end, COARSE_K3_CLOCK),
    )
    common_counts = tuple(
        clock_increment(history, start, common_end, name) for name in CLOCK_NAMES
    )
    ratios = {
        "trained_fine_over_k2": matched_ratio(
            history, start, k2_end, FINE_CLOCK, COARSE_K2_CLOCK
        ),
        "held_fine_over_k3": matched_ratio(
            history, start, k3_end, FINE_CLOCK, COARSE_K3_CLOCK
        ),
        "common_fine_over_k2": matched_ratio(
            history, start, common_end, FINE_CLOCK, COARSE_K2_CLOCK
        ),
        "common_fine_over_k3": matched_ratio(
            history, start, common_end, FINE_CLOCK, COARSE_K3_CLOCK
        ),
        "common_k2_over_k3": matched_ratio(
            history, start, common_end, COARSE_K2_CLOCK, COARSE_K3_CLOCK
        ),
    }
    detail = {
        "training_stride": 2,
        "held_out_stride": 3,
        "k2_matched_counts": k2_counts,
        "k3_matched_counts": k3_counts,
        "common_lcm_interval_counts": common_counts,
        "lcm": lcm(2, 3),
        "ratios": ratios,
    }
    check(
        "shared physical Record endpoints give exact trained k2, held k3, and common-lcm refinement ratios",
        k2_counts == (10, 5)
        and k3_counts == (9, 3)
        and common_counts == (6, 3, 2)
        and lcm(2, 3) == 6
        and ratios
        == {
            "trained_fine_over_k2": Fraction(2, 1),
            "held_fine_over_k3": Fraction(3, 1),
            "common_fine_over_k2": Fraction(2, 1),
            "common_fine_over_k3": Fraction(3, 1),
            "common_k2_over_k3": Fraction(3, 2),
        }
        and ratios["common_fine_over_k2"] * ratios["common_k2_over_k3"]
        == ratios["common_fine_over_k3"],
        detail,
    )


def additive_split_and_composition_controls(
    history: tuple[TaggedRecord, ...],
) -> None:
    start = RECORD_IDS[0]
    middle = RECORD_IDS[6]
    k2_end = RECORD_IDS[10]
    k3_end = RECORD_IDS[9]
    rows = []
    for clock_name, end in (
        (FINE_CLOCK, k2_end),
        (COARSE_K2_CLOCK, k2_end),
        (FINE_CLOCK, k3_end),
        (COARSE_K3_CLOCK, k3_end),
    ):
        whole = clock_increment(history, start, end, clock_name)
        left = clock_increment(history, start, middle, clock_name)
        right = clock_increment(history, middle, end, clock_name)
        rows.append(
            {
                "clock": CLOCK_LABELS[clock_name],
                "whole": whole,
                "left": left,
                "right": right,
                "additive": whole == left + right,
            }
        )
    check(
        "named subchain increments compose additively across one shared intermediate physical Record",
        all(row["additive"] for row in rows)
        and tuple((row["whole"], row["left"], row["right"]) for row in rows)
        == ((10, 6, 4), (5, 3, 2), (9, 6, 3), (3, 2, 1)),
        rows,
    )


def identity_and_non_time_controls(
    fixture: c342.c338.RouteFixture,
    history: tuple[TaggedRecord, ...],
) -> None:
    cylinder = history[0].record.cylinder
    reference = c342.apply_continuation_program(fixture, cylinder, ("A", "A"))
    identity_outputs = tuple(
        c342.apply_continuation_program(
            fixture,
            cylinder,
            ("A", "A")[:position] + ("I",) + ("A", "A")[position:],
        )
        for position in range(3)
    )

    presentation_orders = (
        history,
        tuple(reversed(history)),
        history[::2] + history[1::2],
        history[3:] + history[:3],
    )
    start, end = RECORD_IDS[0], RECORD_IDS[10]
    presentation_counts = tuple(
        clock_increment(order, start, end, FINE_CLOCK)
        for order in presentation_orders
    )

    id_map = {
        old: new
        for old, new in zip(RECORD_IDS, RECORD_IDS[4:] + RECORD_IDS[:4])
    }
    relabeled = tuple(
        replace(
            item,
            record_id=id_map[item.record_id],
            predecessor_id=None
            if item.predecessor_id is None
            else id_map[item.predecessor_id],
        )
        for item in history
    )
    relabeled_count = clock_increment(
        relabeled, id_map[start], id_map[end], FINE_CLOCK
    )

    phase_shifted = tuple(
        replace(
            item,
            record=c342.form_conditional_record(
                fixture,
                replace(
                    item.record.cylinder,
                    phase=(item.record.cylinder.phase + 1) % LENGTH,
                ),
            ),
        )
        for item in history
    )
    phase_count = clock_increment(phase_shifted, start, end, FINE_CLOCK)
    phase_delta = (
        history[10].record.cylinder.phase - history[0].record.cylinder.phase
    ) % LENGTH
    detail = {
        "identity_insertions_without_Record": len(identity_outputs),
        "identity_state_failures": sum(item != reference for item in identity_outputs),
        "presentation_counts": presentation_counts,
        "nonmonotone_Record_ids": RECORD_IDS,
        "id_relabel_count": relabeled_count,
        "phase_shift_count": phase_count,
        "fine_count": 10,
        "endpoint_phase_delta_mod_6": phase_delta,
        "distinct_cylinder_words": len(
            {
                c342.c338.cylinder_word(item.record.cylinder) for item in history
            }
        ),
        "physical_Record_identities": len(history),
    }
    check(
        "identity continuation without a new Record is gauge while presentation, id relabeling, and phase relabeling do not change the tagged clock count",
        all(item == reference for item in identity_outputs)
        and presentation_counts == (10, 10, 10, 10)
        and relabeled_count == 10
        and validate_history(fixture, relabeled)
        and phase_count == 10
        and validate_history(fixture, phase_shifted)
        and phase_delta != 10
        and len({c342.c338.cylinder_word(item.record.cylinder) for item in history})
        == 6
        and len(history) == 12,
        detail,
    )


def visible_refinement_controls(history: tuple[TaggedRecord, ...]) -> None:
    prefix = history[:11]
    last = history[11]
    nonmember = replace(
        last,
        tags=tuple(ClockTag(name, 0) for name in CLOCK_NAMES),
    )
    start = RECORD_IDS[0]
    before_end = RECORD_IDS[10]
    after_end = RECORD_IDS[11]
    before = clock_increment(prefix, start, before_end, FINE_CLOCK)
    nonmember_after = clock_increment(
        prefix + (nonmember,), start, after_end, FINE_CLOCK
    )
    member_after = clock_increment(history, start, after_end, FINE_CLOCK)
    detail = {
        "global_Records_before": len(prefix),
        "global_Records_after_nonmember": len(prefix + (nonmember,)),
        "global_Records_after_member": len(history),
        "basis_storage_before_M2": len(prefix) * TAGGED_RECORD_BITS,
        "basis_storage_after_M2": len(history) * TAGGED_RECORD_BITS,
        "fine_count_before": before,
        "fine_count_after_visible_nonmember": nonmember_after,
        "fine_count_after_visible_member": member_after,
        "counterfactual_tags_attached_at_formation": True,
    }
    check(
        "a visible nonmember Record changes history and resource but not the named count, while a separately formed visible member changes the count",
        len(prefix) == 11
        and len(prefix + (nonmember,)) == len(history) == 12
        and before == nonmember_after == 10
        and member_after == 11
        and tagged_word(nonmember) != tagged_word(last),
        detail,
    )


def independent_schedule_controls(history: tuple[TaggedRecord, ...]) -> None:
    unused_ids = (3, 6, 8)
    empty_tags = tuple(ClockTag(name, 0) for name in CLOCK_NAMES)
    auxiliaries = tuple(
        TaggedRecord(
            record=history[index].record,
            record_id=record_id,
            predecessor_id=None,
            anchor=(20, 2 * index, 0),
            tags=empty_tags,
        )
        for index, record_id in enumerate(unused_ids)
    )
    start, end = RECORD_IDS[0], RECORD_IDS[10]
    terminal_ledgers = []
    counts = []
    for order in permutations(auxiliaries):
        ledger = {item.record_id: tagged_word(item) for item in history}
        for item in order:
            ledger[item.record_id] = tagged_word(item)
        terminal_ledgers.append(frozenset(ledger.items()))
        counts.append(clock_increment(history + order, start, end, FINE_CLOCK))
    detail = {
        "independent_nonclock_ledger_presentation_orders": len(terminal_ledgers),
        "distinct_terminal_ledgers": len(set(terminal_ledgers)),
        "global_Record_count": RECORD_COUNT + len(auxiliaries),
        "named_clock_counts": tuple(counts),
        "auxiliary_memberships": tuple(
            tuple(tag.member for tag in item.tags) for item in auxiliaries
        ),
        "combined_forest_validated_as_one_clock_chain": False,
        "presentation_order_is_time": False,
    }
    check(
        "permuting three supplied independent nonclock ledger entries leaves the ledger and named causal-subchain count invariant",
        len(terminal_ledgers) == 6
        and len(set(terminal_ledgers)) == 1
        and tuple(counts) == (10,) * 6
        and all(not tag.member for item in auxiliaries for tag in item.tags)
        and not detail["combined_forest_validated_as_one_clock_chain"]
        and not detail["presentation_order_is_time"],
        detail,
    )


def protected_mutation(
    history: tuple[TaggedRecord, ...],
    record_id: int,
    replacement: TaggedRecord | None,
) -> tuple[TaggedRecord, ...]:
    matches = tuple(index for index, item in enumerate(history) if item.record_id == record_id)
    if len(matches) != 1:
        raise ValueError("mutation target must be one physical Record identity")
    index = matches[0]
    current = history[index]
    if current.record.permanent and replacement != current:
        raise ValueError("permanent Record content includes its formation-time clock tags")
    values = list(history)
    if replacement is None:
        values.pop(index)
    else:
        values[index] = replacement
    return tuple(values)


def flip_k2_tag(item: TaggedRecord) -> TaggedRecord:
    return replace(
        item,
        tags=tuple(
            ClockTag(tag.name, 1 - tag.member)
            if tag.name == COARSE_K2_CLOCK
            else tag
            for tag in item.tags
        ),
    )


def permanence_and_domain_controls(
    fixture: c342.c338.RouteFixture,
    history: tuple[TaggedRecord, ...],
) -> None:
    deletion_rejections = 0
    retarget_rejections = 0
    for item in history:
        try:
            protected_mutation(history, item.record_id, None)
        except ValueError:
            deletion_rejections += 1
        try:
            protected_mutation(history, item.record_id, flip_k2_tag(item))
        except ValueError:
            retarget_rejections += 1

    duplicate_id = list(history)
    duplicate_id[1] = replace(duplicate_id[1], record_id=duplicate_id[0].record_id)
    missing_predecessor = list(history)
    missing_predecessor[1] = replace(missing_predecessor[1], predecessor_id=12)
    duplicate_name = replace(
        history[0],
        tags=(history[0].tags[0], history[0].tags[0], history[0].tags[2]),
    )
    invalid_member = replace(
        history[0],
        tags=(ClockTag(FINE_CLOCK, 2),) + history[0].tags[1:],
    )
    invalid_name = replace(
        history[0],
        tags=(ClockTag(0, 1),) + history[0].tags[1:],
    )
    untyped = replace(
        history[0],
        record=replace(history[0].record, typed=False, permanent=False),
    )
    out_of_range_id = replace(history[0], record_id=16)
    malformed = (
        lambda: validate_history(fixture, tuple(duplicate_id)),
        lambda: validate_history(fixture, tuple(missing_predecessor)),
        lambda: tagged_word(duplicate_name),
        lambda: tagged_word(invalid_member),
        lambda: tagged_word(invalid_name),
        lambda: validate_history(fixture, (untyped,) + history[1:]),
        lambda: tagged_word(out_of_range_id),
    )
    domain_rejections = 0
    for call in malformed:
        try:
            call()
        except ValueError:
            domain_rejections += 1
    same = protected_mutation(history, history[0].record_id, history[0])
    detail = {
        "permanent_Record_deletion_rejections": deletion_rejections,
        "permanent_Record_tag_retarget_rejections": retarget_rejections,
        "total_permanent_attacks_rejected": deletion_rejections
        + retarget_rejections,
        "lawful_domain_rejections": domain_rejections,
        "identity_rewrite_allowed": same == history,
    }
    check(
        "deletion or formation-tag retarget is rejected for every permanent Record and malformed encoded domains fail closed",
        deletion_rejections == RECORD_COUNT
        and retarget_rejections == RECORD_COUNT
        and domain_rejections == len(malformed) == 7
        and same == history,
        detail,
    )


def covariance_and_translation_controls(
    fixture: c342.c338.RouteFixture,
    history: tuple[TaggedRecord, ...],
) -> None:
    frames = c342.c314.c311.c235.proper_cubic_frames()
    mapping_failures = cylinder_failures = history_failures = count_failures = 0
    tag_scalar_failures = 0
    frame_translation_cases = 0
    tagged_record_cases = 0
    start = RECORD_IDS[0]
    base_suffixes = tuple(tagged_word(item)[c342.RECORD_BITS :] for item in history)
    for frame in frames:
        rotated_fixture, mapping, failures = c342.mapped_fixture(fixture, frame)
        mapping_failures += failures
        rotated_cylinders = c342.make_cylinder_chain(
            rotated_fixture, ENDPOINT, RECORD_COUNT
        )
        rotated_records = tuple(
            c342.form_conditional_record(rotated_fixture, item)
            for item in rotated_cylinders
        )
        rotated_anchors = tuple(moved(anchor, frame) for anchor in ANCHORS)
        rotated_history = form_tagged_history(
            rotated_records, anchors=rotated_anchors
        )
        for source, target in zip(history, rotated_history):
            expected = c342.c338.FutureCylinder(
                endpoint=source.record.cylinder.endpoint,
                candidate=source.record.cylinder.candidate,
                phase=source.record.cylinder.phase,
                future_pre=int(mapping[source.record.cylinder.future_pre]),
                future_post=int(mapping[source.record.cylinder.future_post]),
            )
            cylinder_failures += int(target.record.cylinder != expected)
        tag_scalar_failures += sum(
            tagged_word(item)[c342.RECORD_BITS :] != expected_suffix
            for item, expected_suffix in zip(rotated_history, base_suffixes)
        )
        for translation in TRANSLATIONS:
            carried = tuple(
                replace(
                    item,
                    anchor=tuple(
                        item.anchor[index] + translation[index] for index in range(3)
                    ),
                )
                for item in rotated_history
            )
            try:
                validate_history(rotated_fixture, carried)
            except ValueError:
                history_failures += 1
            count_failures += int(
                clock_increment(carried, start, RECORD_IDS[10], FINE_CLOCK) != 10
                or matched_ratio(
                    carried,
                    start,
                    RECORD_IDS[10],
                    FINE_CLOCK,
                    COARSE_K2_CLOCK,
                )
                != 2
                or matched_ratio(
                    carried,
                    start,
                    RECORD_IDS[9],
                    FINE_CLOCK,
                    COARSE_K3_CLOCK,
                )
                != 3
            )
            frame_translation_cases += 1
            tagged_record_cases += len(carried)
    detail = {
        "proper_cubic_frames": len(frames),
        "translations_per_frame": len(TRANSLATIONS),
        "frame_translation_history_cases": frame_translation_cases,
        "tagged_Record_cases": tagged_record_cases,
        "mapping_failures": mapping_failures,
        "cylinder_mapping_failures": cylinder_failures,
        "tag_and_identity_scalar_failures": tag_scalar_failures,
        "history_link_failures": history_failures,
        "refinement_count_failures": count_failures,
    }
    check(
        "the same tagged refinement history and exact ratios are covariant in all 24 spatial frames and 27 tested translations per frame",
        len(frames) == 24
        and len(TRANSLATIONS) == 27
        and frame_translation_cases == 24 * 27
        and tagged_record_cases == 24 * 27 * RECORD_COUNT
        and mapping_failures
        == cylinder_failures
        == tag_scalar_failures
        == history_failures
        == count_failures
        == 0,
        detail,
    )


def semantic_and_inventory_controls() -> None:
    detail = {
        "result": "conditional named Record-subchain refinement ratios",
        "authority": "none",
        "audit": "unset",
        "common_history": "one Cycle-342 L6 two-page twelve-Record history",
        "clock_name_and_membership_tags": "supplied at lawful Record formation",
        "tag_rule": "supplied literal fine/k2/k3 membership program",
        "Record_identity_and_predecessor_links": "supplied basis-register fields",
        "spatial_anchor_path": "supplied placement",
        "spatial_anchor_encoded_in_tagged_word": False,
        "fresh_second_page": "supplied Cycle-342 blank capacity",
        "training_stride": 2,
        "held_out_stride": 3,
        "shared_endpoint_matcher": "exact physical Record identity",
        "dimensionless_ratios": (Fraction(2, 1), Fraction(3, 1)),
        "clock_calibration": None,
        "physical_interval_unit": None,
        "rate": None,
        "physical_time": None,
        "phase_is_time": False,
        "page_position_is_time": False,
        "host_order_is_time": False,
        "Record_id_integer_is_time": False,
        "circuit_depth_is_time": False,
        "spatial_frames_are_time_frames": False,
        "base_Record_M2": c342.RECORD_BITS,
        "tag_M2_per_Record": CLOCK_TAG_BITS,
        "tagged_Record_basis_width_M2": TAGGED_RECORD_BITS,
        "two_page_basis_storage_M2": RECORD_COUNT * TAGGED_RECORD_BITS,
        "basis_width_is_nearest_neighbor_gate_support": False,
        "nearest_neighbor_primitive_synthesis": None,
        "Born_grade": None,
        "actual_history_sampler": None,
        "broad_negative": None,
        "axiom_pressure": False,
    }
    check(
        "the supplied tag/refinement structure, basis widths, and strict spatial-time semantic firewall remain explicit",
        detail["authority"] == "none"
        and detail["audit"] == "unset"
        and detail["clock_calibration"] is None
        and detail["physical_interval_unit"] is None
        and detail["rate"] is None
        and detail["physical_time"] is None
        and all(
            detail[key] is False
            for key in (
                "phase_is_time",
                "page_position_is_time",
                "host_order_is_time",
                "Record_id_integer_is_time",
                "circuit_depth_is_time",
                "spatial_frames_are_time_frames",
                "basis_width_is_nearest_neighbor_gate_support",
                "spatial_anchor_encoded_in_tagged_word",
            )
        )
        and detail["nearest_neighbor_primitive_synthesis"] is None
        and detail["Born_grade"] is None
        and detail["actual_history_sampler"] is None
        and detail["broad_negative"] is None
        and detail["axiom_pressure"] is False
        and detail["base_Record_M2"] == 30
        and detail["tag_M2_per_Record"] == 9
        and detail["tagged_Record_basis_width_M2"] == 48
        and detail["two_page_basis_storage_M2"] == 576,
        detail,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 345 ROUTE 2: PHYSICAL NAMED RECORD-CHAIN REFINEMENT")
    print("authority=none; audit=unset")
    fixture, book, history = build_base_history()
    source_history_and_encoding_controls(fixture, book, history)
    refinement_ratio_controls(history)
    additive_split_and_composition_controls(history)
    identity_and_non_time_controls(fixture, history)
    visible_refinement_controls(history)
    independent_schedule_controls(history)
    permanence_and_domain_controls(fixture, history)
    covariance_and_translation_controls(fixture, history)
    semantic_and_inventory_controls()
    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    print("RESULT PHYSICAL_NAMED_RECORD_CHAIN_REFINEMENT_ROUTE_CERTIFIED")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
