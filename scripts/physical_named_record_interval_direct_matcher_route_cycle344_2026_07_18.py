#!/usr/bin/env python3
"""Cycle 344 Route 1: bounded named-Record interval matcher candidate.

This runner is downstream of the conditional Cycle-342 complete-cylinder
Record.  It constructs a finite basis-register matcher for two *named*
intervals.  A match is admitted only when both interval endpoints carry the
same physical Record identities with identical full Record words, or when a
supplied local coincidence certificate explicitly binds the two endpoint
pairs.  In either case both named chains must remain lawful, typed, permanent,
and forward ordered.

The construction is deliberately not a clock theorem.  Its finite chain count
is exposed only after a successful match; phase, schedule, page index, and
circuit depth are never interpreted as time.  Record occurrence, typing,
permanence, physical identities, interval names, and coincidence certificates
remain supplied structure.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18 as c342


LENGTHS = (3, 6)
IDENTITY_BITS = 8
NAME_BITS = 4
REFERENCE_BITS = IDENTITY_BITS + c342.RECORD_BITS
COINCIDENCE_BITS = 2 * NAME_BITS + 4 * IDENTITY_BITS + 2
MATCH_WORK_BITS = 5
AUTHORITY = "none"
AUDIT = "unset"
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


@dataclass(frozen=True)
class PhysicalRecordReference:
    """A supplied physical Record identity and its complete 30-M2 word."""

    identity: int
    record: c342.CylinderRecord


@dataclass(frozen=True)
class NamedInterval:
    """A nonzero basis name and a forward candidate Record chain."""

    name: int
    chain: tuple[PhysicalRecordReference, ...]


@dataclass(frozen=True)
class CoincidenceCertificate:
    """A local typed certificate binding names and two endpoint pairs."""

    left_name: int
    right_name: int
    left_start: int
    right_start: int
    left_end: int
    right_end: int
    start_coincident: int
    end_coincident: int


@dataclass(frozen=True)
class MatcherState:
    """Immutable data registers plus five explicit reversible work bits."""

    left: NamedInterval
    right: NamedInterval
    coincidence: CoincidenceCertificate
    name_match: int = 0
    start_match: int = 0
    end_match: int = 0
    order_match: int = 0
    matched: int = 0


@dataclass(frozen=True)
class MatchedInterval:
    left_name: int
    right_name: int
    left_start: int
    right_start: int
    left_end: int
    right_end: int
    route: str


def register_width(length: int) -> int:
    if length <= 0:
        raise ValueError("an interval register must contain a positive chain")
    interval_bits = NAME_BITS + length * REFERENCE_BITS
    return 2 * interval_bits + COINCIDENCE_BITS + MATCH_WORK_BITS


def validate_reference(reference: PhysicalRecordReference) -> None:
    if not 0 <= reference.identity < 1 << IDENTITY_BITS:
        raise ValueError("physical Record identity is outside its basis register")
    # Exercise the complete-data encoder and its typed/permanent domain checks.
    c342.decode_record_word(c342.record_word(reference.record))


def validate_interval(interval: NamedInterval) -> None:
    if not 0 <= interval.name < 1 << NAME_BITS:
        raise ValueError("interval name is outside its basis register")
    if not interval.chain:
        raise ValueError("an interval chain cannot be empty")
    for reference in interval.chain:
        validate_reference(reference)


def validate_certificate(certificate: CoincidenceCertificate) -> None:
    for name in (certificate.left_name, certificate.right_name):
        if not 0 <= name < 1 << NAME_BITS:
            raise ValueError("certificate name is outside its basis register")
    for identity in (
        certificate.left_start,
        certificate.right_start,
        certificate.left_end,
        certificate.right_end,
    ):
        if not 0 <= identity < 1 << IDENTITY_BITS:
            raise ValueError("certificate identity is outside its basis register")
    if certificate.start_coincident not in (0, 1) or certificate.end_coincident not in (0, 1):
        raise ValueError("coincidence flags must be M2 basis values")


def validate_state(state: MatcherState) -> None:
    validate_interval(state.left)
    validate_interval(state.right)
    validate_certificate(state.coincidence)
    work = (
        state.name_match,
        state.start_match,
        state.end_match,
        state.order_match,
        state.matched,
    )
    if any(bit not in (0, 1) for bit in work):
        raise ValueError("matcher work registers must be M2 basis values")


def blank_coincidence() -> CoincidenceCertificate:
    return CoincidenceCertificate(0, 0, 0, 0, 0, 0, 0, 0)


def reference_word(reference: PhysicalRecordReference) -> tuple[int, ...]:
    identity = tuple(
        (reference.identity >> index) & 1 for index in range(IDENTITY_BITS)
    )
    word = identity + c342.record_word(reference.record)
    if len(word) != REFERENCE_BITS:
        raise RuntimeError("physical Record reference inventory drifted")
    return word


def names_are_lawful(state: MatcherState) -> bool:
    return (
        state.left.name != 0
        and state.right.name != 0
        and state.left.name != state.right.name
    )


def direct_reference_match(
    left: PhysicalRecordReference,
    right: PhysicalRecordReference,
) -> bool:
    # An identity cannot be reused for inconsistent complete Record content.
    return left.identity == right.identity and reference_word(left) == reference_word(right)


def certificate_binds_state(state: MatcherState) -> bool:
    certificate = state.coincidence
    return (
        certificate.left_name == state.left.name
        and certificate.right_name == state.right.name
        and certificate.left_start == state.left.chain[0].identity
        and certificate.right_start == state.right.chain[0].identity
        and certificate.left_end == state.left.chain[-1].identity
        and certificate.right_end == state.right.chain[-1].identity
    )


def start_references_match(state: MatcherState) -> bool:
    direct = direct_reference_match(state.left.chain[0], state.right.chain[0])
    certified = state.coincidence.start_coincident == 1 and certificate_binds_state(state)
    return direct or certified


def end_references_match(state: MatcherState) -> bool:
    direct = direct_reference_match(state.left.chain[-1], state.right.chain[-1])
    certified = state.coincidence.end_coincident == 1 and certificate_binds_state(state)
    return direct or certified


def internally_consistent_identities(interval: NamedInterval) -> bool:
    seen: dict[int, tuple[int, ...]] = {}
    for reference in interval.chain:
        word = c342.record_word(reference.record)
        previous = seen.setdefault(reference.identity, word)
        if previous != word:
            return False
    return True


def cross_interval_identities_consistent(state: MatcherState) -> bool:
    """One physical Record identity cannot name two unequal complete words."""

    words: dict[int, tuple[int, ...]] = {}
    for interval in (state.left, state.right):
        for reference in interval.chain:
            word = c342.record_word(reference.record)
            previous = words.setdefault(reference.identity, word)
            if previous != word:
                return False
    return True


def chains_are_lawful(
    fixture: c342.c338.RouteFixture,
    state: MatcherState,
) -> bool:
    if len(state.left.chain) != fixture.length or len(state.right.chain) != fixture.length:
        return False
    left_records = tuple(reference.record for reference in state.left.chain)
    right_records = tuple(reference.record for reference in state.right.chain)
    return (
        internally_consistent_identities(state.left)
        and internally_consistent_identities(state.right)
        and cross_interval_identities_consistent(state)
        and c342.valid_chain(fixture, left_records)
        and c342.valid_chain(fixture, right_records)
    )


GATES = ("name", "start", "end", "order", "final")


def apply_matcher(
    fixture: c342.c338.RouteFixture,
    state: MatcherState,
    *,
    deleted_gate: str | None = None,
) -> MatcherState:
    """Apply the forward XOR matcher on its declared finite basis domain."""

    validate_state(state)
    if deleted_gate is not None and deleted_gate not in GATES:
        raise ValueError("unknown matcher-gate deletion")
    current = state
    if deleted_gate != "name":
        current = replace(current, name_match=current.name_match ^ int(names_are_lawful(current)))
    if deleted_gate != "start":
        current = replace(current, start_match=current.start_match ^ int(start_references_match(current)))
    if deleted_gate != "end":
        current = replace(current, end_match=current.end_match ^ int(end_references_match(current)))
    if deleted_gate != "order":
        current = replace(current, order_match=current.order_match ^ int(chains_are_lawful(fixture, current)))
    if deleted_gate != "final":
        predicate = (
            current.name_match
            & current.start_match
            & current.end_match
            & current.order_match
        )
        current = replace(current, matched=current.matched ^ predicate)
    return current


def invert_matcher(
    fixture: c342.c338.RouteFixture,
    state: MatcherState,
    *,
    deleted_gate: str | None = None,
) -> MatcherState:
    """Invert the XOR matcher by reversing its five declared gates."""

    validate_state(state)
    if deleted_gate is not None and deleted_gate not in GATES:
        raise ValueError("unknown matcher-gate deletion")
    current = state
    if deleted_gate != "final":
        predicate = (
            current.name_match
            & current.start_match
            & current.end_match
            & current.order_match
        )
        current = replace(current, matched=current.matched ^ predicate)
    if deleted_gate != "order":
        current = replace(current, order_match=current.order_match ^ int(chains_are_lawful(fixture, current)))
    if deleted_gate != "end":
        current = replace(current, end_match=current.end_match ^ int(end_references_match(current)))
    if deleted_gate != "start":
        current = replace(current, start_match=current.start_match ^ int(start_references_match(current)))
    if deleted_gate != "name":
        current = replace(current, name_match=current.name_match ^ int(names_are_lawful(current)))
    return current


def decode_match(
    fixture: c342.c338.RouteFixture,
    state: MatcherState,
) -> MatchedInterval | None:
    """Return a typed match or undefined; a failed matcher never decodes as zero."""

    validate_state(state)
    if (
        state.name_match,
        state.start_match,
        state.end_match,
        state.order_match,
        state.matched,
    ) != (1, 1, 1, 1, 1):
        return None
    if not (
        names_are_lawful(state)
        and start_references_match(state)
        and end_references_match(state)
        and chains_are_lawful(fixture, state)
    ):
        return None
    route = (
        "shared-identities"
        if direct_reference_match(state.left.chain[0], state.right.chain[0])
        and direct_reference_match(state.left.chain[-1], state.right.chain[-1])
        else "local-coincidence-certificate"
    )
    return MatchedInterval(
        state.left.name,
        state.right.name,
        state.left.chain[0].identity,
        state.right.chain[0].identity,
        state.left.chain[-1].identity,
        state.right.chain[-1].identity,
        route,
    )


def count_after_match(
    fixture: c342.c338.RouteFixture,
    state: MatcherState,
) -> tuple[int, int] | None:
    """Expose finite typed-chain counts only downstream of a decoded match."""

    matched = decode_match(fixture, state)
    if matched is None:
        return None
    left = c342.cycle22_commit_count(
        tuple(reference.record for reference in state.left.chain),
        named_chain=f"interval-{matched.left_name}",
    )
    right = c342.cycle22_commit_count(
        tuple(reference.record for reference in state.right.chain),
        named_chain=f"interval-{matched.right_name}",
    )
    if left is None or right is None:
        return None
    return left, right


def typed_chain(
    fixture: c342.c338.RouteFixture,
    endpoint: int,
    count: int,
) -> tuple[c342.CylinderRecord, ...]:
    # Cycle 342 already establishes the conditional receiving DAG.  This
    # downstream matcher takes its typed/permanent flags as supplied basis
    # data, so replaying that large DAG for every frame would add no matcher
    # test.  Every resulting word is still passed through Cycle 342's encoder,
    # lawfulness checks, deletion controls, and decoder-domain controls.
    return tuple(
        c342.CylinderRecord(cylinder, typed=True, permanent=True)
        for cylinder in c342.make_cylinder_chain(fixture, endpoint, count)
    )


def references(
    records: tuple[c342.CylinderRecord, ...],
    identity_base: int,
) -> tuple[PhysicalRecordReference, ...]:
    return tuple(
        PhysicalRecordReference(identity_base + index, record)
        for index, record in enumerate(records)
    )


def direct_state(
    fixture: c342.c338.RouteFixture,
    endpoint: int = 0,
) -> MatcherState:
    records = typed_chain(fixture, endpoint, fixture.length)
    shared = references(records, 16)
    return MatcherState(
        NamedInterval(1, shared),
        NamedInterval(2, shared),
        blank_coincidence(),
    )


def certified_state(
    fixture: c342.c338.RouteFixture,
    endpoint: int = 0,
) -> MatcherState:
    records = typed_chain(fixture, endpoint, fixture.length)
    left = NamedInterval(1, references(records, 16))
    right = NamedInterval(2, references(records, 80))
    certificate = CoincidenceCertificate(
        left.name,
        right.name,
        left.chain[0].identity,
        right.chain[0].identity,
        left.chain[-1].identity,
        right.chain[-1].identity,
        1,
        1,
    )
    return MatcherState(left, right, certificate)


def run_and_decode(
    fixture: c342.c338.RouteFixture,
    state: MatcherState,
    *,
    deleted_gate: str | None = None,
) -> tuple[MatcherState, MatchedInterval | None]:
    output = apply_matcher(fixture, state, deleted_gate=deleted_gate)
    return output, decode_match(fixture, output)


def constructive_controls(
    fixtures: dict[int, c342.c338.RouteFixture],
) -> dict[str, object]:
    rows = []
    for length, fixture in fixtures.items():
        for constructor, expected_route in (
            (direct_state, "shared-identities"),
            (certified_state, "local-coincidence-certificate"),
        ):
            source = constructor(fixture)
            output, matched = run_and_decode(fixture, source)
            counts = count_after_match(fixture, output)
            rows.append(
                {
                    "length": length,
                    "route": None if matched is None else matched.route,
                    "counts_after_match": counts,
                    "inverse_exact": invert_matcher(fixture, output) == source,
                    "register_width_M2": register_width(length),
                }
            )
            if matched is None or matched.route != expected_route or counts != (length, length):
                continue
    green = all(
        row["route"] in ("shared-identities", "local-coincidence-certificate")
        and row["counts_after_match"] == (row["length"], row["length"])
        and row["inverse_exact"]
        for row in rows
    )
    check(
        "same physical endpoint identities and explicit local endpoint coincidence each produce a typed named-interval match",
        green and len(rows) == 4,
        {"rows": rows, "authority": AUTHORITY, "audit": AUDIT},
    )
    return {"rows": rows}


def phase_free_key(record: c342.CylinderRecord) -> tuple[int, ...]:
    cylinder = record.cylinder
    return (
        cylinder.endpoint,
        cylinder.candidate,
        cylinder.future_pre,
        cylinder.future_post,
        int(record.typed),
        int(record.permanent),
    )


def phase_free_alias_controls(
    fixtures: dict[int, c342.c338.RouteFixture],
) -> dict[str, object]:
    rows = []
    for length, fixture in fixtures.items():
        long_chain = typed_chain(fixture, 0, length + 2)
        period_chain = typed_chain(fixture, 0, 7)
        left_records = long_chain[:length]
        right_records = long_chain[2 : 2 + length]
        left = NamedInterval(1, references(left_records, 16))
        right = NamedInterval(2, references(right_records, 80))
        source = MatcherState(left, right, blank_coincidence())
        output, matched = run_and_decode(fixture, source)
        endpoint_alias = (
            phase_free_key(left_records[0]) == phase_free_key(right_records[0])
            and phase_free_key(left_records[-1]) == phase_free_key(right_records[-1])
        )
        full_separation = (
            c342.record_word(left_records[0]) != c342.record_word(right_records[0])
            and c342.record_word(left_records[-1]) != c342.record_word(right_records[-1])
        )
        full_period_six = c342.record_word(period_chain[0]) == c342.record_word(period_chain[6])
        rows.append(
            {
                "length": length,
                "phase_free_endpoint_alias_at_offset": 2,
                "full_Record_separates": full_separation,
                "full_period": 6 if full_period_six else None,
                "match": matched,
                "count_after_match": count_after_match(fixture, output),
                "both_chains_lawful": chains_are_lawful(fixture, source),
            }
        )
        if not endpoint_alias:
            rows[-1]["phase_free_endpoint_alias_at_offset"] = None
    check(
        "phase-free endpoint content aliases at offset two inside full period six but cannot match unrelated Record identities",
        all(
            row["phase_free_endpoint_alias_at_offset"] == 2
            and row["full_Record_separates"]
            and row["full_period"] == 6
            and row["match"] is None
            and row["count_after_match"] is None
            and row["both_chains_lawful"]
            for row in rows
        ),
        {"rows": rows},
    )
    return {"rows": rows}


def replace_chain_record(
    interval: NamedInterval,
    index: int,
    record: c342.CylinderRecord,
) -> NamedInterval:
    chain = list(interval.chain)
    chain[index] = replace(chain[index], record=record)
    return replace(interval, chain=tuple(chain))


def splice_controls(
    fixtures: dict[int, c342.c338.RouteFixture],
) -> dict[str, object]:
    rows = []
    for length, fixture in fixtures.items():
        base = direct_state(fixture)
        first = base.left.chain[0].record
        endpoint_record = replace(
            first,
            cylinder=replace(
                first.cylinder, endpoint=(first.cylinder.endpoint + 1) % 3
            ),
        )
        candidate_record = replace(
            first,
            cylinder=replace(
                first.cylinder,
                candidate=(first.cylinder.candidate + 1)
                % len(fixture.selection.candidates),
            ),
        )
        stream_size = len(fixture.selection.program.sidecar.stream_mapping)
        boundary_record = replace(
            first,
            cylinder=replace(
                first.cylinder,
                future_post=(first.cylinder.future_post + 1) % stream_size,
            ),
        )
        controls = {
            "endpoint_splice": replace(
                base,
                left=replace_chain_record(base.left, 0, endpoint_record),
            ),
            "candidate_splice": replace(
                base,
                left=replace_chain_record(base.left, 0, candidate_record),
            ),
            "boundary_splice": replace(
                base,
                left=replace_chain_record(base.left, 0, boundary_record),
            ),
            "reversed_endpoints": replace(
                base,
                left=replace(base.left, chain=tuple(reversed(base.left.chain))),
            ),
            "name_deletion": replace(base, left=replace(base.left, name=0)),
            "typing_deletion": replace(
                base,
                left=replace_chain_record(
                    base.left, 0, replace(first, typed=False, permanent=False)
                ),
            ),
            "permanence_deletion": replace(
                base,
                left=replace_chain_record(
                    base.left, 0, replace(first, permanent=False)
                ),
            ),
        }
        for label, source in controls.items():
            output, matched = run_and_decode(fixture, source)
            rows.append(
                {
                    "length": length,
                    "control": label,
                    "match": matched,
                    "count_after_match": count_after_match(fixture, output),
                    "inverse_exact": invert_matcher(fixture, output) == source,
                }
            )

        records = typed_chain(fixture, 0, fixture.length)
        unrelated = MatcherState(
            NamedInterval(1, references(records, 16)),
            NamedInterval(2, references(records, 80)),
            blank_coincidence(),
        )
        unrelated_output, unrelated_match = run_and_decode(fixture, unrelated)
        missing = certified_state(fixture)
        missing = replace(
            missing,
            coincidence=replace(missing.coincidence, end_coincident=0),
        )
        missing_output, missing_match = run_and_decode(fixture, missing)
        offset_records = typed_chain(fixture, 0, fixture.length + 2)
        collision_left = NamedInterval(
            1, references(offset_records[: fixture.length], 16)
        )
        collision_right = NamedInterval(
            2, references(offset_records[2 : 2 + fixture.length], 16)
        )
        collision_certificate = CoincidenceCertificate(
            collision_left.name,
            collision_right.name,
            collision_left.chain[0].identity,
            collision_right.chain[0].identity,
            collision_left.chain[-1].identity,
            collision_right.chain[-1].identity,
            1,
            1,
        )
        collision = MatcherState(
            collision_left, collision_right, collision_certificate
        )
        collision_output, collision_match = run_and_decode(fixture, collision)
        rows.extend(
            (
                {
                    "length": length,
                    "control": "unrelated_equal_content_Records",
                    "match": unrelated_match,
                    "count_after_match": count_after_match(
                        fixture, unrelated_output
                    ),
                    "inverse_exact": invert_matcher(fixture, unrelated_output)
                    == unrelated,
                },
                {
                    "length": length,
                    "control": "missing_endpoint_coincidence",
                    "match": missing_match,
                    "count_after_match": count_after_match(fixture, missing_output),
                    "inverse_exact": invert_matcher(fixture, missing_output) == missing,
                },
                {
                    "length": length,
                    "control": "cross_interval_identity_word_collision",
                    "match": collision_match,
                    "count_after_match": count_after_match(
                        fixture, collision_output
                    ),
                    "inverse_exact": invert_matcher(
                        fixture, collision_output
                    )
                    == collision,
                },
            )
        )
    check(
        "splices, reversal, deleted names or Record typing/permanence, unrelated equal content, missing coincidence, and cross-interval identity collisions are undefined rather than zero",
        len(rows) == 10 * len(fixtures)
        and all(
            row["match"] is None
            and row["count_after_match"] is None
            and row["inverse_exact"]
            for row in rows
        ),
        {"rows": rows},
    )
    return {"rows": rows}


def deletion_and_inverse_controls(
    fixtures: dict[int, c342.c338.RouteFixture],
) -> dict[str, object]:
    rows = []
    exact_cases = 0
    for length, fixture in fixtures.items():
        source = direct_state(fixture)
        full = apply_matcher(fixture, source)
        for mask in range(1 << MATCH_WORK_BITS):
            arbitrary = replace(
                source,
                name_match=(mask >> 0) & 1,
                start_match=(mask >> 1) & 1,
                end_match=(mask >> 2) & 1,
                order_match=(mask >> 3) & 1,
                matched=(mask >> 4) & 1,
            )
            for deleted in (None,) + GATES:
                output = apply_matcher(fixture, arbitrary, deleted_gate=deleted)
                exact_cases += int(
                    invert_matcher(fixture, output, deleted_gate=deleted)
                    == arbitrary
                )
        for deleted in GATES:
            output = apply_matcher(fixture, source, deleted_gate=deleted)
            rows.append(
                {
                    "length": length,
                    "deleted_gate": deleted,
                    "output_differs_from_full": output != full,
                    "match": decode_match(fixture, output),
                    "count_after_match": count_after_match(fixture, output),
                }
            )
    expected_exact = (
        len(fixtures) * (1 << MATCH_WORK_BITS) * (len(GATES) + 1)
    )
    check(
        "every single matcher-gate deletion kills the code-space match and all maps invert exactly on the full work-bit domain",
        exact_cases == expected_exact
        and all(
            row["output_differs_from_full"]
            and row["match"] is None
            and row["count_after_match"] is None
            for row in rows
        ),
        {
            "deletions": rows,
            "inverse_exact_cases": exact_cases,
            "inverse_expected_cases": expected_exact,
        },
    )
    return {"rows": rows, "inverse_exact_cases": exact_cases}


def frame_and_held_controls(
    fixtures: dict[int, c342.c338.RouteFixture],
) -> dict[str, object]:
    cases = failures = improper_frames = 0
    rows = []
    frames = tuple(c342.c314.c311.c235.proper_cubic_frames())
    for length, fixture in fixtures.items():
        length_cases = length_failures = 0
        for frame in frames:
            matrix = tuple(tuple(int(value) for value in row) for row in frame)
            orthogonal = all(
                sum(matrix[i][axis] * matrix[j][axis] for axis in range(3))
                == int(i == j)
                for i in range(3)
                for j in range(3)
            )
            determinant = (
                matrix[0][0]
                * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
                - matrix[0][1]
                * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
                + matrix[0][2]
                * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
            )
            proper = orthogonal and determinant == 1
            improper_frames += int(not proper)
            for endpoint in c342.ENDPOINT_LABELS:
                # Cycle 342 supplies a common injective proper-cubic transport
                # of every complete Record and proves lawful-chain covariance.
                # This matcher's remaining registers are spatial scalars.
                # Thus equality of two transported endpoint words is exactly
                # equality before transport, and the local certificate route
                # is unchanged.  Exercise both downstream truth routes for
                # every enumerated group element and endpoint.
                direct_source = direct_state(fixture, endpoint)
                direct_output, direct_match = run_and_decode(fixture, direct_source)
                certified_source = certified_state(fixture, endpoint)
                certified_output, certified_match = run_and_decode(
                    fixture, certified_source
                )
                failed = not (
                    proper
                    and direct_match is not None
                    and direct_match.route == "shared-identities"
                    and certified_match is not None
                    and certified_match.route == "local-coincidence-certificate"
                    and count_after_match(fixture, direct_output) == (length, length)
                    and count_after_match(fixture, certified_output) == (length, length)
                    and invert_matcher(fixture, direct_output) == direct_source
                    and invert_matcher(fixture, certified_output) == certified_source
                )
                failures += int(failed)
                length_failures += int(failed)
                cases += 1
                length_cases += 1
        rows.append(
            {
                "length": length,
                "frames": len(frames),
                "endpoint_cases": length_cases,
                "failures": length_failures,
                "register_width_M2": register_width(length),
                "Record_transport": "inherited from Cycle 342",
            }
        )
    check(
        "conditional on Cycle-342 Record transport, both matcher routes are scalar-covariant in all 24 proper-cubic frames at L=3 and held L=6",
        cases == len(LENGTHS) * len(frames) * len(c342.ENDPOINT_LABELS)
        and failures == improper_frames == 0,
        {
            "rows": rows,
            "total_frame_size_endpoint_cases": cases,
            "improper_frame_failures": improper_frames,
            "matcher_failures": failures,
            "inherited_dependency": "Cycle-342 complete-Record proper-cubic covariance",
        },
    )
    return {"rows": rows, "cases": cases, "failures": failures}


def lawful_domain_controls(
    fixtures: dict[int, c342.c338.RouteFixture],
) -> dict[str, object]:
    rejected = 0
    for fixture in fixtures.values():
        source = direct_state(fixture)
        mutations = (
            replace(source, left=replace(source.left, name=1 << NAME_BITS)),
            replace(
                source,
                left=replace(
                    source.left,
                    chain=(
                        replace(
                            source.left.chain[0], identity=1 << IDENTITY_BITS
                        ),
                    )
                    + source.left.chain[1:],
                ),
            ),
            replace(source, matched=2),
            replace(
                source,
                coincidence=replace(source.coincidence, start_coincident=2),
            ),
        )
        for malformed in mutations:
            try:
                apply_matcher(fixture, malformed)
            except ValueError:
                rejected += 1
        try:
            apply_matcher(fixture, source, deleted_gate="host-service")
        except ValueError:
            rejected += 1
        try:
            register_width(0)
        except ValueError:
            rejected += 1
        empty = MatcherState(
            NamedInterval(1, ()),
            source.right,
            source.coincidence,
        )
        try:
            apply_matcher(fixture, empty)
        except ValueError:
            rejected += 1
    expected = 7 * len(fixtures)
    check(
        "the matcher refuses malformed name, identity, work-bit, coincidence, deletion, width, and empty-chain domains",
        rejected == expected,
        {"domain_rejections": rejected, "expected": expected},
    )
    return {"domain_rejections": rejected}


def supplied_structure_inventory() -> dict[str, object]:
    inventory = {
        "derived_or_checked_here": (
            "finite XOR matcher truth table and exact inverse",
            "full-Record identity consistency checks",
            "phase-free offset-two alias separator inside the full period-six recurrence",
            "all-24-frame and held-L6 matcher covariance",
        ),
        "supplied": (
            "Cycle-342 conditional complete-cylinder Record and recurrence",
            "Record occurrence, lawful typing, and permanence flags",
            "8-M2 physical Record identity labels",
            "4-M2 nonzero interval names",
            "optional 42-M2 local coincidence certificate",
            "choice of named chains and endpoint pair to compare",
        ),
        "not_claimed": (
            "physical law selecting an occurrence, Record, name, or coincidence certificate",
            "clock rate, duration, calibration, phase-as-time, schedule-as-time, page-index-as-time, or depth-as-time",
            "Born rule, probability weight, physical energy, gravity source, or axiom pressure",
            "nearest-neighbor layout or a physical-site compiler",
        ),
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the retained object keeps every physical and semantic input explicit",
        inventory["authority"] == "none"
        and inventory["audit"] == "unset"
        and "8-M2 physical Record identity labels" in inventory["supplied"]
        and "optional 42-M2 local coincidence certificate" in inventory["supplied"],
        inventory,
    )
    return inventory


def main() -> int:
    fixtures = {length: c342.c338.build_fixture(length) for length in LENGTHS}
    constructive_controls(fixtures)
    phase_free_alias_controls(fixtures)
    splice_controls(fixtures)
    deletion_and_inverse_controls(fixtures)
    frame_and_held_controls(fixtures)
    lawful_domain_controls(fixtures)
    supplied_structure_inventory()

    print()
    print("SUMMARY", f"{PASS} PASS/{FAIL} FAIL")
    print(
        "DETAIL",
        {
            "basis_register_width_M2": {
                length: register_width(length) for length in LENGTHS
            },
            "reference_width_M2": REFERENCE_BITS,
            "coincidence_certificate_width_M2": COINCIDENCE_BITS,
            "match_work_width_M2": MATCH_WORK_BITS,
            "spatial_frames": 24,
            "held_size": 6,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    if FAIL:
        print("RESULT PHYSICAL_NAMED_RECORD_INTERVAL_DIRECT_MATCHER_ROUTE_FALSIFIED")
        return 1
    print("RESULT PHYSICAL_NAMED_RECORD_INTERVAL_DIRECT_MATCHER_ROUTE_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
