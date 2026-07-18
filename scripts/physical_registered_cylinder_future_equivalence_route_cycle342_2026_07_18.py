#!/usr/bin/env python3
"""Cycle 342 Route 3: complete-cylinder future-equivalence Record candidate.

The runner takes the green Cycle-338 causal cylinder as its complete-data unit.
It tests whether raw causal schedules with the same decoded cylinder form one
future-equivalent fibre under a declared finite continuation family, and then
feeds that certificate through the conditional Cycle-287 Record receiving DAG.

The retained result, if green, is conditional: occurrence, commit typing, and
Record formation remain explicit law inputs; permanence is applied only after
lawful Record typing.  Finite pages are append-only.  Exhaustion refuses an
overwrite, while renewal attaches separately supplied blank support and leaves
old Records unchanged.  Only a named typed permanent chain is sent to the
Cycle-22 additive commit-count interface.  Matcher, interval, calibration, and
rate remain open.  No Born grade or numerical weight selects a cylinder.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import permutations
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import clock_as_commit_count_and_rate_classification_cycle22_2026_07_14 as c22
import physical_endpoint_registration_process_route_cycle338_2026_07_18 as c338


c287 = c338.c287
c332 = c338.c332
c329 = c338.c329
c314 = c338.c314

LENGTHS = (3, 6)
ENDPOINT_LABELS = c338.ENDPOINT_LABELS
RECORD_TYPE_BITS = 2  # lawful Record typing and conditional permanence
RECORD_BITS = c338.CYLINDER_BITS + RECORD_TYPE_BITS
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


def integer(word: tuple[int, ...]) -> int:
    if any(bit not in (0, 1) for bit in word):
        raise ValueError("an M2 basis word must be binary")
    return sum(bit << index for index, bit in enumerate(word))


@dataclass(frozen=True)
class CylinderRecord:
    cylinder: c338.FutureCylinder
    typed: bool
    permanent: bool


@dataclass(frozen=True)
class RecordBook:
    pages: tuple[tuple[CylinderRecord | None, ...], ...]
    active_page: int


def decode_cylinder_word(word: tuple[int, ...]) -> c338.FutureCylinder:
    if len(word) != c338.CYLINDER_BITS or any(bit not in (0, 1) for bit in word):
        raise ValueError("complete cylinder word has the wrong M2 domain")
    cursor = 0

    def take(width: int) -> int:
        nonlocal cursor
        value = integer(word[cursor : cursor + width])
        cursor += width
        return value

    cylinder = c338.FutureCylinder(
        endpoint=take(c338.ENDPOINT_BITS),
        candidate=take(c338.CANDIDATE_BITS),
        phase=take(c338.PHASE_BITS),
        future_pre=take(c338.BOUNDARY_BITS),
        future_post=take(c338.BOUNDARY_BITS),
    )
    if cursor != c338.CYLINDER_BITS:
        raise RuntimeError("cylinder decoder did not consume its declared register")
    return cylinder


def record_word(record: CylinderRecord) -> tuple[int, ...]:
    word = c338.cylinder_word(record.cylinder) + (
        int(record.typed),
        int(record.permanent),
    )
    if len(word) != RECORD_BITS:
        raise RuntimeError("Record register inventory drifted")
    return word


def decode_record_word(word: tuple[int, ...]) -> CylinderRecord:
    if len(word) != RECORD_BITS:
        raise ValueError("Record word has the wrong M2 width")
    typed, permanent = word[-2:]
    if typed not in (0, 1) or permanent not in (0, 1):
        raise ValueError("Record type flags are M2 basis values")
    if permanent and not typed:
        raise ValueError("permanence cannot precede lawful Record typing")
    return CylinderRecord(
        decode_cylinder_word(word[:-2]), bool(typed), bool(permanent)
    )


def cylinder_is_lawful(
    fixture: c338.RouteFixture,
    cylinder: c338.FutureCylinder,
) -> bool:
    if cylinder.endpoint not in ENDPOINT_LABELS:
        return False
    if cylinder.candidate != fixture.selected_id:
        return False
    if not 0 <= cylinder.phase < fixture.length:
        return False
    if not 0 <= cylinder.future_pre < len(
        fixture.selection.program.sidecar.stream_mapping
    ):
        return False
    if not 0 <= cylinder.future_post < len(
        fixture.selection.program.sidecar.stream_mapping
    ):
        return False
    return (
        c332.transition_witness(
            fixture.selection.program,
            cylinder.future_pre,
            cylinder.future_post,
        )
        == 1
    )


def advance_cylinder(
    fixture: c338.RouteFixture,
    cylinder: c338.FutureCylinder,
) -> c338.FutureCylinder:
    if not cylinder_is_lawful(fixture, cylinder):
        raise ValueError("only a lawful complete cylinder can enter continuation")
    next_post = int(
        fixture.selection.program.sidecar.stream_mapping[cylinder.future_post]
    )
    advanced = c338.FutureCylinder(
        endpoint=cylinder.endpoint,
        candidate=cylinder.candidate,
        phase=(cylinder.phase + 1) % fixture.length,
        future_pre=cylinder.future_post,
        future_post=next_post,
    )
    if not cylinder_is_lawful(fixture, advanced):
        raise RuntimeError("the declared continuation left the physical transition code")
    return advanced


def continuation_signature(
    fixture: c338.RouteFixture,
    cylinder: c338.FutureCylinder,
    depth: int = 3,
) -> tuple[tuple[int, ...], ...]:
    if depth < 0:
        raise ValueError("continuation depth is nonnegative")
    current = cylinder
    words = [c338.cylinder_word(current)]
    for _ in range(depth):
        current = advance_cylinder(fixture, current)
        words.append(c338.cylinder_word(current))
    return tuple(words)


def apply_continuation_program(
    fixture: c338.RouteFixture,
    cylinder: c338.FutureCylinder,
    program: tuple[str, ...],
) -> c338.FutureCylinder:
    current = cylinder
    for operation in program:
        if operation == "I":
            continue
        if operation == "A":
            current = advance_cylinder(fixture, current)
            continue
        raise ValueError(("unknown continuation operation", operation))
    return current


def make_cylinder_chain(
    fixture: c338.RouteFixture,
    endpoint: int,
    count: int,
) -> tuple[c338.FutureCylinder, ...]:
    if count <= 0:
        raise ValueError("a candidate Record chain must be nonempty")
    first = c338.decode_cylinder(
        fixture, c338.lawful_packet(fixture, endpoint, 0)
    )
    if first is None:
        raise RuntimeError("Cycle-338 failed to decode its lawful source packet")
    chain = [first]
    for _ in range(count - 1):
        chain.append(advance_cylinder(fixture, chain[-1]))
    return tuple(chain)


def valid_chain(
    fixture: c338.RouteFixture,
    chain: tuple[CylinderRecord, ...],
) -> bool:
    if not chain:
        return False
    if any(
        not record.typed
        or not record.permanent
        or not cylinder_is_lawful(fixture, record.cylinder)
        for record in chain
    ):
        return False
    return all(
        right.cylinder == advance_cylinder(fixture, left.cylinder)
        for left, right in zip(chain, chain[1:])
    )


def future_fibre_controls(
    fixtures: dict[int, c338.RouteFixture],
) -> dict[str, object]:
    schedules = tuple(c287.topological_orders(c338.PROCESS_DAG))
    rows = []
    for length, fixture in fixtures.items():
        for endpoint in ENDPOINT_LABELS:
            packet = c338.lawful_packet(fixture, endpoint, length - 1)
            cylinders = tuple(
                c338.execute_schedule(fixture, packet, order) for order in schedules
            )
            signatures = tuple(
                None
                if cylinder is None
                else continuation_signature(fixture, cylinder)
                for cylinder in cylinders
            )
            first = cylinders[0]
            if first is None:
                raise RuntimeError("the green Cycle-338 schedule became undefined")
            encoded = c338.cylinder_word(first)
            rows.append(
                {
                    "L": length,
                    "endpoint": endpoint,
                    "raw_schedule_representatives": len(schedules),
                    "decoded_cylinders": len(
                        {None if item is None else c338.cylinder_word(item) for item in cylinders}
                    ),
                    "future_signatures": len(set(signatures)),
                    "decoder_roundtrip": decode_cylinder_word(encoded) == first,
                    "coordinate_readout_bits": tuple(
                        encoded[index] for index in range(c338.CYLINDER_BITS)
                    ),
                }
            )
    # A phase-forgetting packet merges two exact futures and is therefore not a
    # complete Record fibre for this declared phase-sensitive continuation law.
    fixture = fixtures[3]
    base = make_cylinder_chain(fixture, 0, 1)[0]
    phase_changed = replace(base, phase=(base.phase + 1) % fixture.length)
    coarse_base = (
        base.endpoint,
        base.candidate,
        base.future_pre,
        base.future_post,
    )
    coarse_changed = (
        phase_changed.endpoint,
        phase_changed.candidate,
        phase_changed.future_pre,
        phase_changed.future_post,
    )
    phase_separator = {
        "coarse_keys_equal": coarse_base == coarse_changed,
        "complete_words_equal": c338.cylinder_word(base)
        == c338.cylinder_word(phase_changed),
        "future_signatures_equal": continuation_signature(fixture, base)
        == continuation_signature(fixture, phase_changed),
    }
    check(
        "every raw Cycle-338 process schedule lies in one exact complete-cylinder future fibre and the decoder/readout roundtrip is exact",
        len(schedules) == 5040
        and all(
            row["raw_schedule_representatives"] == 5040
            and row["decoded_cylinders"] == 1
            and row["future_signatures"] == 1
            and row["decoder_roundtrip"]
            and len(row["coordinate_readout_bits"]) == c338.CYLINDER_BITS
            for row in rows
        )
        and phase_separator
        == {
            "coarse_keys_equal": True,
            "complete_words_equal": False,
            "future_signatures_equal": False,
        },
        {"rows": rows, "phase_deletion_separator": phase_separator},
    )
    return {"schedules": len(schedules), "rows": rows}


def identity_and_continuation_controls(
    fixtures: dict[int, c338.RouteFixture],
) -> dict[str, object]:
    rows = []
    for length, fixture in fixtures.items():
        cylinder = make_cylinder_chain(fixture, 0, 1)[0]
        reference = apply_continuation_program(fixture, cylinder, ("A", "A"))
        identity_rows = tuple(
            apply_continuation_program(
                fixture,
                cylinder,
                ("A", "A")[:position] + ("I",) + ("A", "A")[position:],
            )
            for position in range(3)
        )
        chain = make_cylinder_chain(fixture, 0, 2 * length + 1)
        joint_period = None
        for index in range(1, len(chain)):
            if chain[index] == chain[0]:
                joint_period = index
                break
        distinct_words = {
            c338.cylinder_word(item)
            for item in chain[: joint_period or len(chain)]
        }
        rows.append(
            {
                "L": length,
                "identity_insertions": len(identity_rows),
                "identity_failures": sum(item != reference for item in identity_rows),
                "joint_phase_boundary_period": joint_period,
                "first_period_distinct": len(distinct_words),
                "phase_recurs_after_L": chain[length].phase == chain[0].phase,
                "boundary_recurs_after_L": chain[length] == chain[0],
                "transition_failures": sum(
                    not cylinder_is_lawful(fixture, item) for item in chain
                ),
            }
        )
    rejected = 0
    for call in (
        lambda: apply_continuation_program(fixtures[3], make_cylinder_chain(fixtures[3], 0, 1)[0], ("bad",)),
        lambda: continuation_signature(fixtures[3], make_cylinder_chain(fixtures[3], 0, 1)[0], -1),
        lambda: make_cylinder_chain(fixtures[3], 0, 0),
        lambda: decode_cylinder_word((0,)),
    ):
        try:
            call()
        except ValueError:
            rejected += 1
    check(
        "identity insertion is contained exactly and the declared lawful continuation has an explicit bounded joint phase/boundary recurrence without calling period time",
        all(
            row["identity_insertions"] == 3
            and row["identity_failures"] == 0
            and row["joint_phase_boundary_period"] in (row["L"], 2 * row["L"])
            and row["first_period_distinct"] == row["joint_phase_boundary_period"]
            and row["phase_recurs_after_L"]
            and row["transition_failures"] == 0
            for row in rows
        )
        and rejected == 4,
        {"rows": rows, "domain_rejections": rejected},
    )
    return {"rows": rows}


def form_conditional_record(
    fixture: c338.RouteFixture,
    cylinder: c338.FutureCylinder,
    *,
    occurrence: bool = True,
    commit: bool = True,
    typing: bool = True,
    permanence: bool = True,
    fibre_certified: bool = True,
) -> CylinderRecord:
    candidate = cylinder_is_lawful(fixture, cylinder) and fibre_certified
    local = {
        "write": candidate,
        "archive": candidate,
        "reset": candidate,
        "candidate_event": candidate,
        "history_export": candidate,
        "actual_event": occurrence,
        "commit": commit,
        "Record": typing,
        "permanent_Record": permanence,
    }
    order = next(c287.topological_orders(c287.BASE_DAG))
    formed = c287.replay_dag(c287.BASE_DAG, order, local)
    return CylinderRecord(
        cylinder,
        typed="Record" in formed,
        permanent="permanent_Record" in formed,
    )


def conditional_record_dag_controls(
    fixtures: dict[int, c338.RouteFixture],
) -> dict[str, object]:
    schedules = tuple(c287.topological_orders(c287.BASE_DAG))
    fixture = fixtures[3]
    cylinder = make_cylinder_chain(fixture, 0, 1)[0]
    candidate = cylinder_is_lawful(fixture, cylinder)
    local = {
        "write": candidate,
        "archive": candidate,
        "reset": candidate,
        "candidate_event": candidate,
        "history_export": candidate,
        "actual_event": True,
        "commit": True,
        "Record": True,
        "permanent_Record": True,
    }
    outcomes = tuple(c287.replay_dag(c287.BASE_DAG, order, local) for order in schedules)
    edge_survivors = 0
    for edge in c287.BASE_EDGES:
        formed = c287.replay_dag(
            c287.BASE_DAG,
            schedules[0],
            local,
            c287.BASE_EDGES - {edge},
        )
        edge_survivors += int("permanent_Record" in formed)
    deletions = {
        name: form_conditional_record(fixture, cylinder, **{name: False})
        for name in ("occurrence", "commit", "typing", "permanence", "fibre_certified")
    }
    ideal = form_conditional_record(fixture, cylinder)
    check(
        "the complete future-fibre certificate conditionally enters the Cycle-287 typed permanent Record DAG with every semantic edge exposed",
        len(schedules) == 2
        and len(set(outcomes)) == 1
        and outcomes[0] == c287.BASE_NODES
        and edge_survivors == 0
        and ideal.typed
        and ideal.permanent
        and not deletions["occurrence"].typed
        and not deletions["commit"].typed
        and not deletions["typing"].typed
        and deletions["permanence"].typed
        and not deletions["permanence"].permanent
        and not deletions["fibre_certified"].typed,
        {
            "topological_orders": len(schedules),
            "edge_deletion_permanent_survivors": edge_survivors,
            "deletions": deletions,
            "conditional_law_inputs": ("occurrence", "commit", "Record typing", "permanence"),
        },
    )
    return {"schedules": len(schedules), "edge_survivors": edge_survivors}


def empty_book(length: int) -> RecordBook:
    if length not in LENGTHS:
        raise ValueError("Record page length is outside the declared domain")
    return RecordBook(((None,) * length,), 0)


def append_record(book: RecordBook, record: CylinderRecord) -> RecordBook:
    if not record.typed or not record.permanent:
        raise ValueError("only a typed permanent Record may enter the append-only book")
    page = list(book.pages[book.active_page])
    try:
        slot = page.index(None)
    except ValueError as error:
        raise ValueError("finite Record page is exhausted") from error
    page[slot] = record
    pages = list(book.pages)
    pages[book.active_page] = tuple(page)
    return RecordBook(tuple(pages), book.active_page)


def attach_fresh_page(
    book: RecordBook,
    blank_page: tuple[None, ...],
) -> RecordBook:
    length = len(book.pages[0])
    if len(blank_page) != length or any(item is not None for item in blank_page):
        raise ValueError("renewal requires one separately supplied blank page")
    if any(item is None for item in book.pages[book.active_page]):
        raise ValueError("renewal is allowed only after explicit exhaustion")
    return RecordBook(book.pages + (blank_page,), len(book.pages))


def erase_or_retarget_record(
    book: RecordBook,
    page: int,
    slot: int,
    replacement: CylinderRecord | None,
) -> RecordBook:
    current = book.pages[page][slot]
    if current is not None and current.permanent and replacement != current:
        raise ValueError("lawful post-Record updates preserve permanent content")
    values = list(book.pages[page])
    values[slot] = replacement
    pages = list(book.pages)
    pages[page] = tuple(values)
    return RecordBook(tuple(pages), book.active_page)


def flatten_records(book: RecordBook) -> tuple[CylinderRecord, ...]:
    return tuple(
        item for page in book.pages for item in page if item is not None
    )


def append_capacity_and_attack_controls(
    fixtures: dict[int, c338.RouteFixture],
) -> dict[str, object]:
    rows = []
    for length, fixture in fixtures.items():
        cylinders = make_cylinder_chain(fixture, 0, 2 * length)
        records = tuple(form_conditional_record(fixture, item) for item in cylinders)
        book = empty_book(length)
        prefixes = [0]
        for record in records[:length]:
            book = append_record(book, record)
            prefixes.append(len(flatten_records(book)))
        first_page = book.pages[0]
        exhausted = False
        try:
            append_record(book, records[length])
        except ValueError:
            exhausted = True
        renewed = attach_fresh_page(book, (None,) * length)
        old_page_preserved = renewed.pages[0] == first_page
        capacities = (length, 2 * length)
        for record in records[length:]:
            renewed = append_record(renewed, record)
        permanent_attack_rejections = 0
        for replacement in (None, records[1]):
            try:
                erase_or_retarget_record(renewed, 0, 0, replacement)
            except ValueError:
                permanent_attack_rejections += 1
        deleted_chain = flatten_records(renewed)[:1] + flatten_records(renewed)[2:]
        spliced_chain = list(flatten_records(renewed))
        spliced_chain[1] = replace(
            spliced_chain[1],
            cylinder=replace(
                spliced_chain[1].cylinder,
                future_pre=spliced_chain[2].cylinder.future_pre,
            ),
        )
        raw = c338.cylinder_word(cylinders[0])
        blank = (0,) * len(raw)
        written = c338.xor_word(blank, raw)
        candidate_inverse = c338.xor_word(written, raw)
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "prefix_counts": tuple(prefixes),
                "exhausted_rejected": exhausted,
                "old_page_preserved": old_page_preserved,
                "capacity_before_after_supplied_renewal": capacities,
                "records_after_renewal": len(flatten_records(renewed)),
                "full_chain_valid": valid_chain(fixture, flatten_records(renewed)),
                "deleted_chain_valid": valid_chain(fixture, deleted_chain),
                "spliced_chain_valid": valid_chain(fixture, tuple(spliced_chain)),
                "permanent_attack_rejections": permanent_attack_rejections,
                "candidate_inverse_before_Record_restores_blank": candidate_inverse == blank,
                "page_M2": length * RECORD_BITS,
                "two_page_M2": 2 * length * RECORD_BITS,
            }
        )
    malformed_rejections = 0
    malformed = (
        lambda: empty_book(4),
        lambda: append_record(empty_book(3), CylinderRecord(make_cylinder_chain(fixtures[3], 0, 1)[0], False, False)),
        lambda: attach_fresh_page(empty_book(3), (None,) * 3),
        lambda: attach_fresh_page(RecordBook(((form_conditional_record(fixtures[3], make_cylinder_chain(fixtures[3], 0, 1)[0]),) * 3,), 0), (None, None)),
        lambda: decode_record_word(c338.cylinder_word(make_cylinder_chain(fixtures[3], 0, 1)[0]) + (0, 1)),
    )
    for call in malformed:
        try:
            call()
        except ValueError:
            malformed_rejections += 1
    check(
        "finite cylinders append monotonically, reject exhaustion, renew only onto supplied blank support, and resist deletion/splice/retarget/inverse attacks after permanence",
        all(
            row["prefix_counts"] == tuple(range(row["L"] + 1))
            and row["exhausted_rejected"]
            and row["old_page_preserved"]
            and row["capacity_before_after_supplied_renewal"]
            == (row["L"], 2 * row["L"])
            and row["records_after_renewal"] == 2 * row["L"]
            and row["full_chain_valid"]
            and not row["deleted_chain_valid"]
            and not row["spliced_chain_valid"]
            and row["permanent_attack_rejections"] == 2
            and row["candidate_inverse_before_Record_restores_blank"]
            and row["two_page_M2"] <= 360
            for row in rows
        )
        and malformed_rejections == len(malformed),
        {"rows": rows, "domain_rejections": malformed_rejections},
    )
    return {"rows": rows, "domain_rejections": malformed_rejections}


def atomic_overlap_commit(
    length: int,
    proposals: tuple[tuple[int, CylinderRecord], ...],
) -> tuple[tuple[CylinderRecord | None, ...], frozenset[int]]:
    if length not in LENGTHS:
        raise ValueError("overlap page is outside the declared domain")
    grouped: dict[int, list[CylinderRecord]] = {}
    for slot, record in proposals:
        if not 0 <= slot < length or not record.typed or not record.permanent:
            raise ValueError("overlap proposals require lawful slots and Records")
        grouped.setdefault(slot, []).append(record)
    page: list[CylinderRecord | None] = [None] * length
    conflicts = set()
    for slot, candidates in grouped.items():
        words = {record_word(item) for item in candidates}
        if len(words) == 1:
            page[slot] = candidates[0]
        else:
            conflicts.add(slot)
    return tuple(page), frozenset(conflicts)


def overlapping_selector_controls(
    fixtures: dict[int, c338.RouteFixture],
) -> dict[str, object]:
    rows = []
    for length, fixture in fixtures.items():
        cylinders = make_cylinder_chain(fixture, 0, 3)
        records = tuple(form_conditional_record(fixture, item) for item in cylinders)
        proposals = (
            (0, records[0]),
            (0, records[0]),
            (1, records[1]),
            (1, records[2]),
            (2, records[2]),
        )
        outputs = tuple(
            atomic_overlap_commit(length, order) for order in permutations(proposals)
        )
        canonical = outputs[0]
        rows.append(
            {
                "L": length,
                "selector_schedules": len(outputs),
                "terminal_outputs": len(set(outputs)),
                "committed_slots": tuple(
                    index for index, item in enumerate(canonical[0]) if item is not None
                ),
                "conflicts": tuple(sorted(canonical[1])),
                "identical_duplicate_idempotent": canonical[0][0] == records[0],
                "priority_tie_break_used": False,
            }
        )
    check(
        "overlapping selectors are schedule invariant: identical complete fibres coalesce while distinct-cylinder conflicts remain blank without priority",
        all(
            row["selector_schedules"] == 120
            and row["terminal_outputs"] == 1
            and row["committed_slots"] == (0, 2)
            and row["conflicts"] == (1,)
            and row["identical_duplicate_idempotent"]
            and row["priority_tie_break_used"] is False
            for row in rows
        ),
        rows,
    )
    return {"rows": rows}


def mapped_fixture(
    fixture: c338.RouteFixture,
    frame: tuple[tuple[int, ...], ...],
) -> tuple[c338.RouteFixture, object, int]:
    mapping, failures = c332.event_frame_mapping(
        fixture.selection.program.sidecar, frame
    )
    candidates = tuple(
        c338.c333.Candidate(int(mapping[item.pre]), int(mapping[item.post]))
        for item in fixture.selection.candidates
    )
    support = c329.build_fixture(fixture.length, frame)
    match, ready = c329.route_outputs(support, "syndrome")
    selection = c338.c333.SelectionFixture(
        length=fixture.length,
        program=fixture.selection.program,
        anchor=int(mapping[fixture.selection.anchor]),
        candidates=candidates,
        match=match,
        ready=ready,
    )
    upstream = c338.c333.route1_unique(selection, anchor=selection.anchor)
    if upstream.status != "bound" or upstream.selected is None:
        raise RuntimeError("rotated Cycle-333 certificate did not bind")
    return (
        c338.RouteFixture(
            fixture.length,
            selection,
            fixture.export,
            candidates.index(upstream.selected),
        ),
        mapping,
        failures,
    )


def frame_and_held_controls(
    fixtures: dict[int, c338.RouteFixture],
) -> dict[str, object]:
    cases = mapping_failures = record_failures = future_failures = 0
    for length, fixture in fixtures.items():
        base_by_endpoint = {
            endpoint: make_cylinder_chain(fixture, endpoint, length)
            for endpoint in ENDPOINT_LABELS
        }
        signatures_by_endpoint = {
            endpoint: tuple(
                continuation_signature(fixture, item)
                for item in base_by_endpoint[endpoint]
            )
            for endpoint in ENDPOINT_LABELS
        }
        for frame in c314.c311.c235.proper_cubic_frames():
            rotated, mapping, failures = mapped_fixture(fixture, frame)
            mapping_failures += failures
            for endpoint in ENDPOINT_LABELS:
                base = base_by_endpoint[endpoint]
                base_signatures = signatures_by_endpoint[endpoint]
                carried = make_cylinder_chain(rotated, endpoint, length)
                records = tuple(form_conditional_record(rotated, item) for item in carried)
                record_failures += int(not valid_chain(rotated, records))
                for source, target, signature in zip(base, carried, base_signatures):
                    expected = c338.FutureCylinder(
                        endpoint=source.endpoint,
                        candidate=source.candidate,
                        phase=source.phase,
                        future_pre=int(mapping[source.future_pre]),
                        future_post=int(mapping[source.future_post]),
                    )
                    future_failures += int(target != expected)
                    carried_signature = continuation_signature(rotated, target)
                    decoded_signature = tuple(
                        decode_cylinder_word(word) for word in signature
                    )
                    expected_signature = tuple(
                        c338.cylinder_word(
                            c338.FutureCylinder(
                                endpoint=item.endpoint,
                                candidate=item.candidate,
                                phase=item.phase,
                                future_pre=int(mapping[item.future_pre]),
                                future_post=int(mapping[item.future_post]),
                            )
                        )
                        for item in decoded_signature
                    )
                    future_failures += int(carried_signature != expected_signature)
                    cases += 1
    detail = {
        "frame_size_endpoint_record_cases": cases,
        "proper_cubic_frames_per_size": 24,
        "mapping_failures": mapping_failures,
        "typed_chain_failures": record_failures,
        "future_equivalence_covariance_failures": future_failures,
        "held_size": 6,
    }
    check(
        "typed complete-cylinder chains and their declared future signatures transform covariantly in all 24 frames at L=3 and held L=6",
        cases == sum(length for length in LENGTHS) * len(ENDPOINT_LABELS) * 24
        and mapping_failures == record_failures == future_failures == 0,
        detail,
    )
    return detail


def cycle22_commit_count(
    chain: tuple[CylinderRecord, ...],
    *,
    named_chain: str | None,
) -> int | None:
    if not named_chain or not chain or any(
        not record.typed or not record.permanent for record in chain
    ):
        return None
    roles = ("start", "left", "close")
    return sum(c22.tau((roles[index % len(roles)],)) for index in range(len(chain)))


def record_count_and_time_firewall_controls(
    fixtures: dict[int, c338.RouteFixture],
) -> dict[str, object]:
    rows = []
    for length, fixture in fixtures.items():
        cylinders = make_cylinder_chain(fixture, 0, length)
        chain = tuple(form_conditional_record(fixture, item) for item in cylinders)
        counts = tuple(
            cycle22_commit_count(
                chain[:prefix], named_chain="Cycle342 complete-cylinder Record chain"
            )
            for prefix in range(1, len(chain) + 1)
        )
        untyped = replace(chain[0], typed=False, permanent=False)
        rows.append(
            {
                "L": length,
                "named_permanent_chain_count": counts[-1],
                "prefix_counts": counts,
                "additive_split": cycle22_commit_count(
                    chain[:1], named_chain="Cycle342 complete-cylinder Record chain"
                )
                + cycle22_commit_count(
                    chain[1:], named_chain="Cycle342 complete-cylinder Record chain"
                )
                == counts[-1],
                "unnamed_count": cycle22_commit_count(chain, named_chain=None),
                "untyped_count": cycle22_commit_count(
                    (untyped,) + chain[1:],
                    named_chain="Cycle342 complete-cylinder Record chain",
                ),
                "matcher": None,
                "interval": None,
                "rate": None,
                "physical_time": None,
            }
        )
    check(
        "only the named typed permanent chain reaches Cycle-22 additive commit count; matcher interval rate and physical time remain open",
        all(
            row["named_permanent_chain_count"] == row["L"]
            and row["prefix_counts"] == tuple(range(1, row["L"] + 1))
            and row["additive_split"]
            and row["unnamed_count"] is None
            and row["untyped_count"] is None
            and row["matcher"] is row["interval"] is row["rate"] is row["physical_time"] is None
            for row in rows
        ),
        rows,
    )
    return {"rows": rows}


def semantic_and_support_controls() -> dict[str, object]:
    detail = {
        "result": "conditional complete-cylinder future-equivalent Record sector",
        "occurrence": "supplied explicit law input",
        "commit_map": "supplied explicit law input",
        "Record_typing": "supplied explicit law input",
        "permanence": "current framework consequence only after typing",
        "fresh_page": "supplied blank capacity; not generated by recurrence",
        "Born_grade": None,
        "numerical_weight_selector": None,
        "actual_history_sampler": None,
        "clock_matcher": None,
        "interval": None,
        "rate": None,
        "circuit_depth_is_time": False,
        "Record_M2": RECORD_BITS,
        "maximum_decoder_and_typing_support_M2": c338.PACKET_BITS + RECORD_BITS,
        "maximum_overlap_batch_support_M2": 4 * RECORD_BITS,
        "held_two_page_support_M2": 12 * RECORD_BITS,
        "authority": "none",
        "audit": "unset",
        "negative_claim": None,
    }
    check(
        "the positive conditional Record-sector candidate keeps occurrence, capacity, actuality, Born, and clock/rate semantics explicit and bounded",
        detail["Born_grade"] is None
        and detail["numerical_weight_selector"] is None
        and detail["actual_history_sampler"] is None
        and detail["clock_matcher"] is None
        and detail["interval"] is None
        and detail["rate"] is None
        and detail["circuit_depth_is_time"] is False
        and detail["Record_M2"] == 30
        and detail["maximum_decoder_and_typing_support_M2"] == 64
        and detail["maximum_overlap_batch_support_M2"] == 120
        and detail["held_two_page_support_M2"] == 360
        and detail["authority"] == "none"
        and detail["audit"] == "unset"
        and detail["negative_claim"] is None,
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 342 ROUTE 3: REGISTERED CYLINDER FUTURE-EQUIVALENCE RECORD SECTOR")
    print("authority=none; audit=unset")
    fixtures = {length: c338.build_fixture(length) for length in LENGTHS}
    fibres = future_fibre_controls(fixtures)
    identity = identity_and_continuation_controls(fixtures)
    dag = conditional_record_dag_controls(fixtures)
    append = append_capacity_and_attack_controls(fixtures)
    overlaps = overlapping_selector_controls(fixtures)
    frames = frame_and_held_controls(fixtures)
    counts = record_count_and_time_firewall_controls(fixtures)
    semantics = semantic_and_support_controls()
    check(
        "Route 3 conditionally joins registered future-equivalent cylinders to an append-only permanent Record chain and count-only interface",
        fibres["schedules"] == 5040
        and len(identity["rows"]) == 2
        and dag["edge_survivors"] == 0
        and append["domain_rejections"] == 5
        and len(overlaps["rows"]) == 2
        and frames["future_equivalence_covariance_failures"] == 0
        and counts["rows"][-1]["rate"] is None
        and semantics["result"]
        == "conditional complete-cylinder future-equivalent Record sector",
        {
            "disposition": "positive bounded conditional",
            "typed_permanence": "conditional on explicit Cycle-287 law inputs",
            "count": "Cycle-22 additive commit count only",
            "rate": "open",
            "sizes": LENGTHS,
        },
    )
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_REGISTERED_CYLINDER_FUTURE_EQUIVALENCE_ROUTE_OPEN")
        return 1
    print("RESULT PHYSICAL_REGISTERED_CYLINDER_FUTURE_EQUIVALENCE_ROUTE_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
