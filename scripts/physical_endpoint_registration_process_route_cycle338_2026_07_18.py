#!/usr/bin/env python3
"""Cycle 338 Route 3: causal-cylinder endpoint registration.

This runner composes three already packaged, separately typed inputs:

* Cycle 333 supplies a unique continuation certificate relative to supplied
  realized-prefix content;
* Cycle 334 supplies a close-gated physical environment endpoint and a lawful
  three-label decoder basis; and
* Cycle 335 supplies reversible recurrence/export patterns and explicit blank
  capacity accounting.

The new route is a finite causal-process decoder.  It stores endpoint label,
realized endpoint content, upstream candidate identity, schedule phase, and
physical pre/post labels in bounded M2 registers.  It registers only a complete
decoded cylinder whose next physical boundary is fixed by the Cycle-314 stream.
It does not select a candidate by direct prefix equality, does not use redundant
pointer voting, and does not use a Born grade or any numerical weight as a
selector.  Its output is conditional registered data, not a Record, permanent
Record, clock tick, probability, or newly selected actual history.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_environment_export_realized_member_bridge_cycle334_2026_07_18 as c334
import physical_relational_actual_history_member_selection_cycle333_2026_07_18 as c333


c287 = c333.c287
c332 = c333.c332
c329 = c333.c329
c314 = c333.c314

TOL = 1.2e-10
LENGTHS = (3, 6)
ENDPOINT_LABELS = c334.BRANCH_LABELS
BOUNDARY_BITS = 10  # The inherited physical boundary alphabet has 1,020 rows.
ENDPOINT_BITS = 3
CONTENT_BITS = 3
CANDIDATE_BITS = 2
PHASE_BITS = 3
PREDICATE_BITS = 3  # close, unique, physical transition
PACKET_BITS = (
    ENDPOINT_BITS
    + CONTENT_BITS
    + CANDIDATE_BITS
    + PHASE_BITS
    + 2 * BOUNDARY_BITS
    + PREDICATE_BITS
)
CYLINDER_BITS = ENDPOINT_BITS + CANDIDATE_BITS + PHASE_BITS + 2 * BOUNDARY_BITS
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
        raise ValueError(("value does not fit declared M2 register", value, width))
    return tuple((value >> index) & 1 for index in range(width))


def xor_word(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    if len(left) != len(right) or any(value not in (0, 1) for value in left + right):
        raise ValueError("XOR words must be equally sized M2 basis words")
    return tuple(a ^ b for a, b in zip(left, right))


@dataclass(frozen=True)
class RouteFixture:
    length: int
    selection: c333.SelectionFixture
    export: c334.CloseExportFixture
    selected_id: int


@dataclass(frozen=True)
class ProcessPacket:
    endpoint: int | None
    content: int | None
    candidate: int | None
    phase: int | None
    pre: int | None
    post: int | None
    close: int
    unique: int
    transition: int


@dataclass(frozen=True)
class FutureCylinder:
    endpoint: int
    candidate: int
    phase: int
    future_pre: int
    future_post: int


@dataclass(frozen=True)
class ProcessArchive:
    incoming: tuple[int, ...]
    slots: tuple[tuple[int, ...], ...]
    exported: tuple[int, ...]
    phase: int


def build_fixture(length: int) -> RouteFixture:
    selection = c333.build_fixture(length)
    upstream = c333.route1_unique(selection, anchor=selection.anchor)
    if upstream.status != "bound" or upstream.selected is None:
        raise RuntimeError("Cycle-333 did not supply its declared unique continuation")
    selected_id = selection.candidates.index(upstream.selected)
    export = c334.close_fixture(length)
    if export.close_certificate != 1:
        raise RuntimeError("Cycle-334 did not supply its declared close certificate")
    return RouteFixture(length, selection, export, selected_id)


def packet_word(packet: ProcessPacket) -> tuple[int, ...]:
    if None in (
        packet.endpoint,
        packet.content,
        packet.candidate,
        packet.phase,
        packet.pre,
        packet.post,
    ):
        raise ValueError("a physical process packet must populate every declared register")
    assert packet.endpoint is not None
    assert packet.content is not None
    assert packet.candidate is not None
    assert packet.phase is not None
    assert packet.pre is not None
    assert packet.post is not None
    for name, value in (
        ("close", packet.close),
        ("unique", packet.unique),
        ("transition", packet.transition),
    ):
        if value not in (0, 1):
            raise ValueError(f"{name} must be one M2")
    word = (
        bits(packet.endpoint, ENDPOINT_BITS)
        + bits(packet.content, CONTENT_BITS)
        + bits(packet.candidate, CANDIDATE_BITS)
        + bits(packet.phase, PHASE_BITS)
        + bits(packet.pre, BOUNDARY_BITS)
        + bits(packet.post, BOUNDARY_BITS)
        + (packet.close, packet.unique, packet.transition)
    )
    if len(word) != PACKET_BITS:
        raise RuntimeError("packet register inventory drifted")
    return word


def cylinder_word(cylinder: FutureCylinder) -> tuple[int, ...]:
    word = (
        bits(cylinder.endpoint, ENDPOINT_BITS)
        + bits(cylinder.candidate, CANDIDATE_BITS)
        + bits(cylinder.phase, PHASE_BITS)
        + bits(cylinder.future_pre, BOUNDARY_BITS)
        + bits(cylinder.future_post, BOUNDARY_BITS)
    )
    if len(word) != CYLINDER_BITS:
        raise RuntimeError("cylinder register inventory drifted")
    return word


def lawful_packet(
    fixture: RouteFixture,
    endpoint: int,
    phase: int,
) -> ProcessPacket:
    if endpoint not in ENDPOINT_LABELS:
        raise ValueError("endpoint is outside the Cycle-334 branch code")
    if not 0 <= phase < fixture.length:
        raise ValueError("phase is outside the declared recurrent window")
    candidate = fixture.selection.candidates[fixture.selected_id]
    transition = c332.transition_witness(
        fixture.selection.program, candidate.pre, candidate.post
    )
    return ProcessPacket(
        endpoint=endpoint,
        content=endpoint,
        candidate=fixture.selected_id,
        phase=phase,
        pre=candidate.pre,
        post=candidate.post,
        close=fixture.export.close_certificate,
        unique=1,
        transition=transition,
    )


def decode_cylinder(
    fixture: RouteFixture,
    packet: ProcessPacket,
) -> FutureCylinder | None:
    """Decode one complete future cylinder or return an unbound interface.

    Candidate identity is checked against the upstream Cycle-333 certificate;
    this function never compares a bank against the realized-prefix anchor.
    Endpoint/content agreement is only one clause of the complete cylinder.
    """

    if None in (
        packet.endpoint,
        packet.content,
        packet.candidate,
        packet.phase,
        packet.pre,
        packet.post,
    ):
        return None
    assert packet.endpoint is not None
    assert packet.content is not None
    assert packet.candidate is not None
    assert packet.phase is not None
    assert packet.pre is not None
    assert packet.post is not None
    if packet.close != 1 or packet.unique != 1 or packet.transition != 1:
        return None
    if packet.endpoint not in ENDPOINT_LABELS or packet.content not in ENDPOINT_LABELS:
        return None
    if packet.endpoint != packet.content:
        return None
    if packet.candidate != fixture.selected_id:
        return None
    if not 0 <= packet.phase < fixture.length:
        return None
    expected = fixture.selection.candidates[packet.candidate]
    if (packet.pre, packet.post) != (expected.pre, expected.post):
        return None
    if c332.transition_witness(
        fixture.selection.program, packet.pre, packet.post
    ) != 1:
        return None
    future_post = int(fixture.selection.program.sidecar.stream_mapping[packet.post])
    if c332.transition_witness(
        fixture.selection.program, packet.post, future_post
    ) != 1:
        return None
    return FutureCylinder(
        endpoint=packet.endpoint,
        candidate=packet.candidate,
        phase=(packet.phase + 1) % fixture.length,
        future_pre=packet.post,
        future_post=future_post,
    )


PROCESS_NODES = frozenset(
    (
        "endpoint_export",
        "realized_content",
        "candidate_certificate",
        "schedule_phase",
        "close_gate",
        "unique_gate",
        "transition_gate",
        "cylinder_decoder",
        "process_commit",
    )
)
PROCESS_EDGES = frozenset(
    (
        ("endpoint_export", "cylinder_decoder"),
        ("realized_content", "cylinder_decoder"),
        ("candidate_certificate", "cylinder_decoder"),
        ("schedule_phase", "cylinder_decoder"),
        ("close_gate", "cylinder_decoder"),
        ("unique_gate", "cylinder_decoder"),
        ("transition_gate", "cylinder_decoder"),
        ("cylinder_decoder", "process_commit"),
    )
)
PROCESS_DAG = c287.Dag(PROCESS_NODES, PROCESS_EDGES)


def execute_schedule(
    fixture: RouteFixture,
    packet: ProcessPacket,
    order: tuple[str, ...],
) -> FutureCylinder | None:
    roots: dict[str, object] = {}
    decoded: FutureCylinder | None = None
    committed: FutureCylinder | None = None
    for node in order:
        if node == "endpoint_export":
            roots[node] = packet.endpoint
        elif node == "realized_content":
            roots[node] = packet.content
        elif node == "candidate_certificate":
            roots[node] = (packet.candidate, packet.pre, packet.post)
        elif node == "schedule_phase":
            roots[node] = packet.phase
        elif node == "close_gate":
            roots[node] = packet.close
        elif node == "unique_gate":
            roots[node] = packet.unique
        elif node == "transition_gate":
            roots[node] = packet.transition
        elif node == "cylinder_decoder":
            if set(roots) != PROCESS_NODES - {"cylinder_decoder", "process_commit"}:
                return None
            decoded = decode_cylinder(fixture, packet)
        elif node == "process_commit":
            committed = decoded
        else:
            raise ValueError(("unknown process node", node))
    return committed


def source_and_register_controls() -> dict[int, RouteFixture]:
    fixtures = {length: build_fixture(length) for length in LENGTHS}
    rows = []
    for length, fixture in fixtures.items():
        endpoint_decodes = []
        for endpoint in ENDPOINT_LABELS:
            packet = lawful_packet(fixture, endpoint, length - 1)
            cylinder = decode_cylinder(fixture, packet)
            endpoint_decodes.append(None if cylinder is None else cylinder.endpoint)
            packet_word(packet)
            if cylinder is not None:
                cylinder_word(cylinder)
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "Cycle333_selected_id": fixture.selected_id,
                "Cycle334_close": fixture.export.close_certificate,
                "Cycle334_false_close": fixture.export.false_close,
                "endpoint_decodes": tuple(endpoint_decodes),
                "packet_M2": PACKET_BITS,
                "cylinder_M2": CYLINDER_BITS,
            }
        )
    check(
        "the Cycle-333 unique certificate and Cycle-334 close/endpoint basis enter one finite M2 process packet at trained and held size",
        all(
            row["Cycle333_selected_id"] == 0
            and row["Cycle334_close"] == 1
            and row["Cycle334_false_close"] == 0
            and row["endpoint_decodes"] == ENDPOINT_LABELS
            and row["packet_M2"] == 34
            and row["cylinder_M2"] == 28
            for row in rows
        ),
        rows,
    )
    return fixtures


def causal_process_controls(fixtures: dict[int, RouteFixture]) -> dict[str, object]:
    schedules = tuple(c287.topological_orders(PROCESS_DAG))
    rows = []
    for length, fixture in fixtures.items():
        for endpoint in ENDPOINT_LABELS:
            packet = lawful_packet(fixture, endpoint, length - 1)
            cylinders = tuple(execute_schedule(fixture, packet, order) for order in schedules)
            encoded = tuple(
                None if cylinder is None else cylinder_word(cylinder)
                for cylinder in cylinders
            )
            rows.append(
                {
                    "L": length,
                    "endpoint": endpoint,
                    "schedules": len(schedules),
                    "decoded_cylinders": len(set(encoded)),
                    "undefined": sum(word is None for word in encoded),
                }
            )
    local = {node: True for node in PROCESS_NODES}
    edge_survivors = 0
    for edge in PROCESS_EDGES:
        for order in schedules[:1]:
            formed = c287.replay_dag(
                PROCESS_DAG, order, local, PROCESS_EDGES - {edge}
            )
            edge_survivors += int("process_commit" in formed)
    check(
        "all causal schedules give one exact decoded future cylinder and every process edge is load bearing",
        len(schedules) == 5040
        and all(
            row["schedules"] == len(schedules)
            and row["decoded_cylinders"] == 1
            and row["undefined"] == 0
            for row in rows
        )
        and edge_survivors == 0,
        {"rows": rows, "load_bearing_edges": len(PROCESS_EDGES), "edge_survivors": edge_survivors},
    )
    return {"schedules": len(schedules), "rows": rows}


def gating_and_attack_controls(fixtures: dict[int, RouteFixture]) -> dict[str, object]:
    rows = []
    for length, fixture in fixtures.items():
        packet = lawful_packet(fixture, 0, 0)
        other = fixture.selection.candidates[1]
        ambiguous_bank = list(fixture.selection.candidates)
        ambiguous_bank[1] = ambiguous_bank[0]
        upstream_ambiguous = c333.route1_unique(
            fixture.selection,
            anchor=fixture.selection.anchor,
            candidates=tuple(ambiguous_bank),
        )
        deleted = {
            field: decode_cylinder(fixture, replace(packet, **{field: None}))
            for field in ("endpoint", "content", "candidate", "phase", "pre", "post")
        }
        clause_attacks = {
            "false_close": decode_cylinder(fixture, replace(packet, close=0)),
            "ambiguity": decode_cylinder(fixture, replace(packet, unique=0)),
            "transition_deleted": decode_cylinder(fixture, replace(packet, transition=0)),
            "endpoint_retarget": decode_cylinder(fixture, replace(packet, endpoint=1)),
            "content_retarget": decode_cylinder(fixture, replace(packet, content=1)),
            "candidate_retarget": decode_cylinder(
                fixture,
                replace(
                    packet,
                    candidate=1,
                    pre=other.pre,
                    post=other.post,
                ),
            ),
            "spliced_post": decode_cylinder(fixture, replace(packet, post=other.post)),
            "phase_overflow": decode_cylinder(fixture, replace(packet, phase=length)),
        }
        counterfactual = decode_cylinder(
            fixture, replace(packet, endpoint=1, content=1)
        )
        endpoint_only_false_positive = decode_cylinder(
            fixture,
            replace(packet, endpoint=1, content=1, post=other.post),
        )
        identity_only_false_positive = decode_cylinder(
            fixture,
            replace(packet, endpoint=1, content=0),
        )
        cylinder = decode_cylinder(fixture, packet)
        assert cylinder is not None
        blank = (0,) * CYLINDER_BITS
        written = xor_word(blank, cylinder_word(cylinder))
        restored = xor_word(written, cylinder_word(cylinder))
        rows.append(
            {
                "L": length,
                "upstream_ambiguity_status": upstream_ambiguous.status,
                "field_deletion_survivors": sum(value is not None for value in deleted.values()),
                "clause_attack_survivors": sum(value is not None for value in clause_attacks.values()),
                "counterfactual_endpoint": None if counterfactual is None else counterfactual.endpoint,
                "counterfactual_changes_cylinder": counterfactual != cylinder,
                "endpoint_only_false_positive": endpoint_only_false_positive,
                "identity_only_false_positive": identity_only_false_positive,
                "inverse_restores_blank": restored == blank,
            }
        )
    malformed_rejections = 0
    malformed_calls = (
        lambda: bits(-1, 3),
        lambda: bits(8, 3),
        lambda: xor_word((0,), (0, 1)),
        lambda: lawful_packet(fixtures[3], 7, 0),
        lambda: lawful_packet(fixtures[3], 0, 3),
        lambda: packet_word(replace(lawful_packet(fixtures[3], 0, 0), close=2)),
    )
    for call in malformed_calls:
        try:
            call()
        except ValueError:
            malformed_rejections += 1
    check(
        "close/unique gating plus ambiguity splice deletion retarget inverse and lawful-domain attacks isolate complete-cylinder registration",
        all(
            row["upstream_ambiguity_status"] == "undefined"
            and row["field_deletion_survivors"] == 0
            and row["clause_attack_survivors"] == 0
            and row["counterfactual_endpoint"] == 1
            and row["counterfactual_changes_cylinder"]
            and row["endpoint_only_false_positive"] is None
            and row["identity_only_false_positive"] is None
            and row["inverse_restores_blank"]
            for row in rows
        )
        and malformed_rejections == len(malformed_calls),
        {"rows": rows, "domain_rejections": malformed_rejections},
    )
    return {"rows": rows, "domain_rejections": malformed_rejections}


def rotate_right(
    words: tuple[tuple[int, ...], ...],
    deleted_swap: int | None = None,
) -> tuple[tuple[int, ...], ...]:
    if len(words) < 2 or deleted_swap not in (None, *range(len(words) - 1)):
        raise ValueError("bounded recurrence needs at least two words and a lawful deletion")
    values = list(words)
    for gate, left in enumerate(reversed(range(len(values) - 1))):
        if gate != deleted_swap:
            values[left], values[left + 1] = values[left + 1], values[left]
    return tuple(values)


def rotate_left(words: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    values = list(words)
    for left in range(len(values) - 1):
        values[left], values[left + 1] = values[left + 1], values[left]
    return tuple(values)


def archive_step(
    archive: ProcessArchive,
    deleted_swap: int | None = None,
) -> ProcessArchive:
    if not archive.slots:
        raise ValueError("archive needs a nonempty bounded window")
    gates = len(archive.slots) + 1
    if deleted_swap not in (None, *range(gates)):
        raise ValueError("deleted swap is outside the archive chain")
    values = [archive.exported, *archive.slots, archive.incoming]
    for gate in range(len(values) - 1):
        if gate != deleted_swap:
            values[gate], values[gate + 1] = values[gate + 1], values[gate]
    return ProcessArchive(
        incoming=values[-1],
        slots=tuple(values[1:-1]),
        exported=values[0],
        phase=(archive.phase + 1) % len(archive.slots),
    )


def archive_inverse(archive: ProcessArchive) -> ProcessArchive:
    values = [archive.exported, *archive.slots, archive.incoming]
    for gate in reversed(range(len(values) - 1)):
        values[gate], values[gate + 1] = values[gate + 1], values[gate]
    return ProcessArchive(
        incoming=values[-1],
        slots=tuple(values[1:-1]),
        exported=values[0],
        phase=(archive.phase - 1) % len(archive.slots),
    )


def recurrence_and_capacity_controls(fixtures: dict[int, RouteFixture]) -> dict[str, object]:
    rows = []
    blank = (0,) * PACKET_BITS
    for length, fixture in fixtures.items():
        words = tuple(packet_word(lawful_packet(fixture, index % 3, index)) for index in range(length))
        ring_initial = words[:-1] + (blank,)
        ring = ring_initial
        ring_history = []
        for _ in range(length):
            ring_history.append(ring)
            ring = rotate_right(ring)
        inverse_ring = ring
        for _ in range(length):
            inverse_ring = rotate_left(inverse_ring)
        initial = ProcessArchive(
            incoming=words[-1],
            slots=words,
            exported=blank,
            phase=0,
        )
        final = archive_step(initial)
        recovered = archive_inverse(final)
        deleted = tuple(archive_step(initial, gate) for gate in range(length + 1))
        initial_nonblank = sum(
            word != blank for word in (initial.incoming, *initial.slots, initial.exported)
        )
        final_nonblank = sum(
            word != blank for word in (final.incoming, *final.slots, final.exported)
        )
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "ring_period": len(set(ring_history)),
                "ring_recurs": ring == ring_initial,
                "ring_inverse": inverse_ring == ring_initial,
                "ring_blank_positions": tuple(row.index(blank) for row in ring_history),
                "archive_inverse": recovered == initial,
                "archive_blank_relocated": final.incoming == blank,
                "archive_oldest_exported": final.exported == words[0],
                "capacity_before": initial_nonblank,
                "capacity_after": final_nonblank,
                "created_blank_capacity": int(final_nonblank != initial_nonblank),
                "swap_deletion_survivors": sum(row == final for row in deleted),
                "maximum_swap_support_M2": 2 * PACKET_BITS,
                "archive_register_M2": (length + 2) * PACKET_BITS + PHASE_BITS,
            }
        )
    check(
        "Cycle-335-style recurrence and export preserve exact packet capacity, relocate rather than create a blank, and remain invertible/deletion-sensitive",
        all(
            row["ring_period"] == row["L"]
            and row["ring_recurs"]
            and row["ring_inverse"]
            and len(set(row["ring_blank_positions"])) == row["L"]
            and row["archive_inverse"]
            and row["archive_blank_relocated"]
            and row["archive_oldest_exported"]
            and row["capacity_before"] == row["capacity_after"] == row["L"] + 1
            and row["created_blank_capacity"] == 0
            and row["swap_deletion_survivors"] == 0
            and row["maximum_swap_support_M2"] == 68
            and row["archive_register_M2"] <= 275
            for row in rows
        ),
        rows,
    )
    return {"rows": rows}


def frame_and_held_controls(fixtures: dict[int, RouteFixture]) -> dict[str, object]:
    cases = mapping_failures = decode_failures = apparatus_failures = 0
    apparatus_rows = []
    for length, fixture in fixtures.items():
        apparatus = c334.physical_apparatus_covariance_control(fixture.export)
        apparatus_rows.append(apparatus)
        apparatus_failures += int(
            apparatus["frames"] != 24
            or apparatus["branch_failures"] != 0
            or apparatus["maximum_export_residual"] >= TOL
        )
        for frame in c314.c311.c235.proper_cubic_frames():
            mapping, failures = c332.event_frame_mapping(
                fixture.selection.program.sidecar, frame
            )
            mapping_failures += failures
            mapped_candidates = tuple(
                c333.Candidate(int(mapping[item.pre]), int(mapping[item.post]))
                for item in fixture.selection.candidates
            )
            support = c329.build_fixture(length, frame)
            match, ready = c329.route_outputs(support, "syndrome")
            mapped_selection = c333.SelectionFixture(
                length=length,
                program=fixture.selection.program,
                anchor=int(mapping[fixture.selection.anchor]),
                candidates=mapped_candidates,
                match=match,
                ready=ready,
            )
            upstream = c333.route1_unique(
                mapped_selection, anchor=mapped_selection.anchor
            )
            if upstream.status != "bound" or upstream.selected is None:
                decode_failures += len(ENDPOINT_LABELS)
                continue
            selected_id = mapped_candidates.index(upstream.selected)
            mapped_fixture = RouteFixture(
                length, mapped_selection, fixture.export, selected_id
            )
            for endpoint in ENDPOINT_LABELS:
                packet = lawful_packet(mapped_fixture, endpoint, length - 1)
                cylinder = decode_cylinder(mapped_fixture, packet)
                decode_failures += int(
                    cylinder is None
                    or cylinder.endpoint != endpoint
                    or cylinder.candidate != selected_id
                )
                cases += 1
    detail = {
        "frame_size_endpoint_cases": cases,
        "proper_cubic_frames_per_size": 24,
        "mapping_failures": mapping_failures,
        "process_decode_failures": decode_failures,
        "physical_apparatus_failures": apparatus_failures,
        "maximum_apparatus_export_residual": max(
            row["maximum_export_residual"] for row in apparatus_rows
        ),
        "held_size": 6,
    }
    check(
        "the endpoint-process decoder and inherited physical apparatus cover every endpoint in all 24 proper-cubic frames at L=3 and held L=6",
        cases == len(LENGTHS) * 24 * len(ENDPOINT_LABELS)
        and mapping_failures == decode_failures == apparatus_failures == 0
        and detail["maximum_apparatus_export_residual"] < TOL,
        detail,
    )
    return detail


def semantic_and_support_controls() -> dict[str, object]:
    detail = {
        "route": "causal complete-cylinder decoder",
        "direct_prefix_equality_used_inside_route": False,
        "redundant_pointer_vote_used": False,
        "Born_grade_defined": False,
        "numerical_weight_used_as_selector": False,
        "actual_member_selected_by_law": False,
        "output_type": "conditional pointwise registered endpoint data",
        "Record_typed": False,
        "permanence_applied": False,
        "clock_or_rate_formed": False,
        "history_genesis_derived": False,
        "packet_M2": PACKET_BITS,
        "cylinder_M2": CYLINDER_BITS,
        "maximum_new_decoder_support_M2": PACKET_BITS + CYLINDER_BITS,
        "maximum_new_swap_support_M2": 2 * PACKET_BITS,
        "held_archive_M2": (6 + 2) * PACKET_BITS + PHASE_BITS,
        "authority": "none",
        "audit": "unset",
    }
    check(
        "the route remains a bounded conditional registration interface with Record/time/Born/actuality firewalls",
        detail["direct_prefix_equality_used_inside_route"] is False
        and detail["redundant_pointer_vote_used"] is False
        and detail["Born_grade_defined"] is False
        and detail["numerical_weight_used_as_selector"] is False
        and detail["actual_member_selected_by_law"] is False
        and detail["Record_typed"] is False
        and detail["permanence_applied"] is False
        and detail["clock_or_rate_formed"] is False
        and detail["maximum_new_decoder_support_M2"] == 62
        and detail["maximum_new_swap_support_M2"] == 68
        and detail["held_archive_M2"] == 275
        and detail["authority"] == "none"
        and detail["audit"] == "unset",
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 338 ROUTE 3: PHYSICAL ENDPOINT PROCESS REGISTRATION")
    print("authority=none; audit=unset")
    fixtures = source_and_register_controls()
    causal = causal_process_controls(fixtures)
    attacks = gating_and_attack_controls(fixtures)
    recurrence = recurrence_and_capacity_controls(fixtures)
    frames = frame_and_held_controls(fixtures)
    semantics = semantic_and_support_controls()
    check(
        "Route 3 joins Cycles 333/334/335 as an exact causal-cylinder endpoint registration without semantic promotion",
        causal["schedules"] == 5040
        and attacks["domain_rejections"] == 6
        and len(recurrence["rows"]) == 2
        and frames["process_decode_failures"] == 0
        and semantics["output_type"] == "conditional pointwise registered endpoint data",
        {
            "route_disposition": "positive bounded conditional",
            "distinctness": "full future cylinder, not direct prefix equality or redundant pointer vote",
            "endpoint_contents": ENDPOINT_LABELS,
            "sizes": LENGTHS,
        },
    )
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_ENDPOINT_REGISTRATION_PROCESS_ROUTE_OPEN")
        return 1
    print("RESULT PHYSICAL_ENDPOINT_REGISTRATION_PROCESS_ROUTE_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
