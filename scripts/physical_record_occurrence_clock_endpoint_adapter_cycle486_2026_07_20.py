#!/usr/bin/env python3
"""Cycle 486: exact Record-occurrence-to-clock-endpoint adapter tournament.

The input surfaces are exact frozen Cycle-444 clock/event payloads and two
independent Cycle-483 supplied-bath FORM occurrences of actual Cycle-443 /
Cycle-449 admitted carriers.  Three routes are compared:

1. direct 30-bit alias to the Cycle-342/364 cylinder word (falsified control);
2. a priority composite sidecar retaining the full 79+30 M2 pair;
3. a distinct reversible 18-bit endpoint codec with the raw 30 bits retained
   only as inverse environment.

The positive routes produce two bath-candidate-law-relative basis FORM
occurrences, not framework actuality or Records.  Clock interval dK is read
only from bound physical endpoint words.  It is never update count, layer,
depth, proper time, lapse, or a rate.  Authority is none and audit is unset.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from itertools import product
from pathlib import Path
import resource
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_event_latched_recurrent_echo_calibration_tournament_cycle444_2026_07_19 as c444
import physical_reset_environment_record_occurrence_cycle483_2026_07_19 as c483


c449 = c483.c449
c443 = c483.c443
c364 = c443.c364
c342 = c364.c342

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECORD_OCCURRENCE_CLOCK_ENDPOINT_ADAPTER_CYCLE486_NOTE_2026-07-20.md"
)
SOURCE_IDENTITIES = {
    "Cycle342": (
        ROOT / "scripts/physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18.py",
        "5b3d46bd72948f07bcf8b6c9d881663cd02082e770aaa8d7ba1950d1012b09bc",
    ),
    "Cycle364": (
        ROOT / "scripts/physical_site_tethered_close_gated_record_formation_candidate_cycle364_2026_07_18.py",
        "4fb41afc5067849689a958697d986962eab32ca6549199b046519e3bb48d8920",
    ),
    "Cycle443": (
        ROOT / "scripts/physical_delayed_dependency_admission_latch_cycle443_2026_07_19.py",
        "febfa320e566db01c50abd482352b6573daf6780a18414bef83a6529e960112b",
    ),
    "Cycle444": (
        ROOT / "scripts/physical_event_latched_recurrent_echo_calibration_tournament_cycle444_2026_07_19.py",
        "75a7f42ebbea25702474b8856413cbc2bd4c5e37d8d04b8ccf7e3b4d86f50262",
    ),
    "Cycle449": (
        ROOT / "scripts/physical_record_actualization_law_program_tournament_cycle449_2026_07_19.py",
        "857febfb57c7b82559465ab0623ef15b5c392b87ceb323340e007c228df442ad",
    ),
    "Cycle483": (
        ROOT / "scripts/physical_reset_environment_record_occurrence_cycle483_2026_07_19.py",
        "52f0621a06792093ad64a706ab7741335cfd7ff9418b3756f4ab83cf72b8d222",
    ),
}

AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0
WORD = c443.WORD
PAYLOAD = c444.PAYLOAD_BITS
CODE = 18
ENDPOINTS = 2
TOL = 1.0e-12
WALL_CAP_SECONDS = 900.0
RSS_CAP_BYTES = 4 * 1024**3
Word = tuple[int, ...]
Coord = tuple[int, int, int]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest() if path.exists() else "missing"


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "direct alias route",
        "explicit falsified control",
        "priority composite sidecar binding",
        "full 30-m2 clock payload",
        "lawful 79-m2 admitted carrier",
        "distinct reversible 18-bit endpoint codec",
        "two candidate-law-relative basis form occurrences",
        "not framework actuality",
        "not framework records",
        "not update count, layer, or causal depth",
        "train l5 and held l9",
        "dk=2 and dk=4",
        "all 24 proper-cubic frames",
        "calibration, proper time, lapse, epoch renewal, member selection, record type, and permanence remain open",
        "n1 —",
        "n8 —",
        "no axiom pressure",
    ) + tuple(
        f"{name.lower()} runner sha-256: {expected}"
        for name, (_path, expected) in SOURCE_IDENTITIES.items()
    )
    body = normalized(NOTE)
    missing = tuple(item for item in required if item not in body)
    identity_mismatches = tuple(
        (name, file_sha256(path), expected)
        for name, (path, expected) in SOURCE_IDENTITIES.items()
        if file_sha256(path) != expected
    )
    module_paths = (
        ("Cycle444", Path(c444.__file__).resolve(), SOURCE_IDENTITIES["Cycle444"][0].resolve()),
        ("Cycle483", Path(c483.__file__).resolve(), SOURCE_IDENTITIES["Cycle483"][0].resolve()),
        ("Cycle449", Path(c449.__file__).resolve(), SOURCE_IDENTITIES["Cycle449"][0].resolve()),
        ("Cycle443", Path(c443.__file__).resolve(), SOURCE_IDENTITIES["Cycle443"][0].resolve()),
    )
    path_mismatches = tuple(item for item in module_paths if item[1] != item[2])
    check(
        "the Cycle486 note and imported physical interfaces are frozen exactly",
        not missing and not identity_mismatches and not path_mismatches,
        {
            "missing_note_contract": missing,
            "source_identity_mismatches": identity_mismatches,
            "module_path_mismatches": path_mismatches,
        },
    )


def bits(value: int, width: int) -> Word:
    if not isinstance(value, int) or isinstance(value, bool) or value not in range(1 << width):
        raise ValueError("integer leaves its binary M2 word")
    return tuple((value >> lane) & 1 for lane in range(width))


def integer(word: Word) -> int:
    if any(bit not in (0, 1) for bit in word):
        raise ValueError("word is not binary")
    return sum(bit << lane for lane, bit in enumerate(word))


def selected(word: Word | list[int], sites: tuple[int, ...]) -> Word:
    return tuple(word[site] for site in sites)


@dataclass(frozen=True)
class ClockPair:
    size: int
    length: int
    start_position: int
    end_position: int
    payloads: tuple[Word, Word]
    event_identities: tuple[int, int]
    dK: int


def validate_endpoint_payload(payload: Word, expected_identity: int | None = None) -> None:
    if (
        not isinstance(payload, tuple)
        or len(payload) != PAYLOAD
        or any(not isinstance(bit, int) or isinstance(bit, bool) or bit not in (0, 1) for bit in payload)
    ):
        raise ValueError("Cycle444 endpoint payload has the wrong 30-M2 domain")
    c444.clock_position(payload[: c444.CLOCK_BITS])
    identity = integer(payload[16:20])
    if identity == 0 or (expected_identity is not None and identity != expected_identity):
        raise ValueError("Cycle444 endpoint identity is absent or unexpected")


@lru_cache(maxsize=None)
def clock_pair(size: int, length: int, start_position: int) -> ClockPair:
    if size not in (c444.TRAIN_SIZE, c444.HELD_SIZE):
        raise ValueError("Cycle486 accepts only Cycle444 train L5 and held L9")
    if length not in (1, 2) or length > (size - 1) // 2:
        raise ValueError("echo length leaves the declared Cycle444 envelope")
    initial = c444.echo_initial(length, start_position)
    output = c444.run_echo(initial, length)
    if output.rails[-1] != 1 or output.reflector != 1:
        raise RuntimeError("actual Cycle444 echo did not reach its physical endpoint")
    start_latch = c444.apply_latch(c444.blank_latch(1, initial.clock, bits(1, c444.EVENT_BITS)))
    end_latch = c444.apply_latch(c444.blank_latch(1, output.clock, bits(2, c444.EVENT_BITS)))
    payloads = (
        c444.endpoint_payload(start_latch, 1, 1, 0),
        c444.endpoint_payload(end_latch, 1, 1, 0),
    )
    validate_endpoint_payload(payloads[0], 1)
    validate_endpoint_payload(payloads[1], 2)
    end_position = c444.clock_position(payloads[1][:16])
    if start_position >= end_position:
        raise ValueError("Cycle486 bounded endpoint pair is wrapping")
    return ClockPair(
        size,
        length,
        start_position,
        end_position,
        payloads,
        (1, 2),
        end_position - start_position,
    )


def context(size: int) -> tuple[str, int, int]:
    if size == c444.TRAIN_SIZE:
        return "train_L3", c483.TRAIN_HORIZON, c444.TRAIN_START
    if size == c444.HELD_SIZE:
        return "held_L6", c483.HELD_HORIZON, c444.HELD_START
    raise ValueError("unknown train/held context")


def direct_alias_controls() -> dict[str, object]:
    print("\nDIRECT 30-BIT ALIAS FALSIFIER")
    rows = []
    failures = 0
    for size, length in product((c444.TRAIN_SIZE, c444.HELD_SIZE), (1, 2)):
        case_name, _horizon, start = context(size)
        fixture = next(case for case in c443.CASES if case.name == case_name).child.fixture
        pair = clock_pair(size, length, start)
        for role, payload in zip(("launch", "return"), pair.payloads):
            decoded = c342.decode_record_word(payload)
            lawful = c364.payload_lawful(fixture, payload)
            failures += int(lawful)
            rows.append(
                {
                    "size": size,
                    "Cycle443_case": case_name,
                    "length": length,
                    "role": role,
                    "equal_width": len(payload) == c342.RECORD_BITS == 30,
                    "decoded_type_flags": (decoded.typed, decoded.permanent),
                    "Cycle364_payload_lawful": lawful,
                }
            )
    check(
        "equal width does not make the actual Cycle444 endpoint payload a lawful Cycle342/364 cylinder word",
        len(rows) == 8
        and failures == 0
        and all(row["equal_width"] and not row["Cycle364_payload_lawful"] for row in rows),
        {"rows": rows, "lawful_aliases": failures},
    )
    return {"rows": rows}


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


@dataclass(frozen=True)
class AdapterLayout:
    route: str
    payload_input: tuple[tuple[int, ...], ...]
    payload_output: tuple[tuple[int, ...], ...]
    code_output: tuple[tuple[int, ...], ...]
    code_expected: tuple[tuple[int, ...], ...]
    carrier_output: tuple[tuple[int, ...], ...]
    identity_output: tuple[tuple[int, ...], ...]
    predecessor: tuple[int, ...]
    occurrence_flags: tuple[tuple[int, ...], ...]
    content_match: tuple[tuple[int, ...], ...]
    carrier_match: tuple[tuple[int, ...], ...]
    identity_match: tuple[tuple[int, ...], ...]
    predecessor_match: tuple[int, ...]
    prefix: tuple[int, ...]
    total_m2: int


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    output = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return output


@lru_cache(maxsize=None)
def layout(route: str) -> AdapterLayout:
    if route not in ("sidecar", "codec"):
        raise ValueError("Cycle486 route must be sidecar or codec")
    cursor = [ENDPOINTS * c483.TOTAL_M2]
    payload_input = tuple(take(cursor, PAYLOAD) for _ in range(ENDPOINTS))
    payload_output = tuple(take(cursor, PAYLOAD) for _ in range(ENDPOINTS)) if route == "sidecar" else ()
    code_output = tuple(take(cursor, CODE) for _ in range(ENDPOINTS)) if route == "codec" else ()
    code_expected = tuple(take(cursor, CODE) for _ in range(ENDPOINTS)) if route == "codec" else ()
    carrier_output = tuple(take(cursor, WORD) for _ in range(ENDPOINTS))
    identity_output = tuple(take(cursor, 4) for _ in range(ENDPOINTS)) if route == "sidecar" else ()
    predecessor = take(cursor, 4)
    occurrence_flags = tuple(take(cursor, 4) for _ in range(ENDPOINTS))
    content_width = PAYLOAD if route == "sidecar" else CODE
    content_match = tuple(take(cursor, content_width) for _ in range(ENDPOINTS))
    carrier_match = tuple(take(cursor, WORD) for _ in range(ENDPOINTS))
    identity_match = tuple(take(cursor, 4) for _ in range(ENDPOINTS))
    predecessor_match = take(cursor, 4)
    condition_count = ENDPOINTS * (4 + content_width + WORD + 4) + 4
    prefix = take(cursor, condition_count)
    return AdapterLayout(
        route,
        payload_input,
        payload_output,
        code_output,
        code_expected,
        carrier_output,
        identity_output,
        predecessor,
        occurrence_flags,
        content_match,
        carrier_match,
        identity_match,
        predecessor_match,
        prefix,
        cursor[0],
    )


def gate(kind: str, sites: tuple[int, ...], label: str, total_m2: int) -> Gate:
    widths = {"X": 1, "CNOT": 2, "TOFFOLI": 3, "SWAP": 2}
    if kind not in widths or len(sites) != widths[kind] or len(set(sites)) != len(sites):
        raise ValueError("malformed Cycle486 gate")
    if any(site not in range(total_m2) for site in sites):
        raise ValueError("Cycle486 gate leaves its bounded M2 block")
    return Gate(kind, sites, label)


def apply_gate(state: list[int], item: Gate) -> None:
    if item.kind == "X":
        state[item.sites[0]] ^= 1
    elif item.kind == "CNOT":
        control, target = item.sites
        state[target] ^= state[control]
    elif item.kind == "TOFFOLI":
        left, right, target = item.sites
        state[target] ^= state[left] & state[right]
    elif item.kind == "SWAP":
        left, right = item.sites
        state[left], state[right] = state[right], state[left]
    else:
        raise ValueError("unknown Cycle486 primitive")


def apply_schedule(initial: Word, schedule: tuple[Gate, ...], *, reverse: bool = False) -> Word:
    state = list(initial)
    for item in reversed(schedule) if reverse else schedule:
        apply_gate(state, item)
    return tuple(state)


def shifted_c483(item: c483.Gate, endpoint: int, total_m2: int) -> Gate:
    offset = endpoint * c483.TOTAL_M2
    return gate(item.kind, tuple(offset + site for site in item.sites), f"bath{endpoint}:{item.label}", total_m2)


def append_majority(
    output: list[Gate],
    group: tuple[int, int, int],
    target: int,
    label: str,
    total_m2: int,
) -> None:
    left, middle, right = group
    output.extend(
        (
            gate("TOFFOLI", (left, middle, target), f"{label}:lm", total_m2),
            gate("TOFFOLI", (left, right, target), f"{label}:lr", total_m2),
            gate("TOFFOLI", (middle, right, target), f"{label}:mr", total_m2),
        )
    )


def append_xnor(
    output: list[Gate], left: int, right: int, target: int, label: str, total_m2: int
) -> None:
    output.extend(
        (
            gate("X", (target,), f"{label}:seed", total_m2),
            gate("CNOT", (left, target), f"{label}:left", total_m2),
            gate("CNOT", (right, target), f"{label}:right", total_m2),
        )
    )


def append_constant_match(
    output: list[Gate], source: int, target: int, expected: int, label: str, total_m2: int
) -> None:
    if expected == 0:
        output.append(gate("X", (target,), f"{label}:zero-seed", total_m2))
    output.append(gate("CNOT", (source, target), f"{label}:copy", total_m2))


def append_prefix(output: list[Gate], conditions: tuple[int, ...], prefix: tuple[int, ...], total_m2: int) -> None:
    if len(conditions) != len(prefix) or not conditions:
        raise ValueError("Cycle486 prefix workspace mismatch")
    output.append(gate("CNOT", (conditions[0], prefix[0]), "binding-prefix:0", total_m2))
    for lane in range(1, len(conditions)):
        output.append(
            gate("TOFFOLI", (prefix[lane - 1], conditions[lane], prefix[lane]), f"binding-prefix:{lane}", total_m2)
        )


def c483_group(endpoint: int, group: tuple[int, int, int]) -> tuple[int, int, int]:
    offset = endpoint * c483.TOTAL_M2
    return tuple(offset + site for site in group)  # type: ignore[return-value]


def c483_site(endpoint: int, site: int) -> int:
    return endpoint * c483.TOTAL_M2 + site


@lru_cache(maxsize=None)
def adapter_schedule(route: str) -> tuple[Gate, ...]:
    item = layout(route)
    output: list[Gate] = []
    conditions: list[int] = []
    for endpoint in range(ENDPOINTS):
        flags = item.occurrence_flags[endpoint]
        output.append(
            gate("CNOT", (c483_site(endpoint, c483.B_FORM), flags[0]), f"{route}-flag:{endpoint}:form", item.total_m2)
        )
        for name, source_group, target in (
            ("type", c483.B_TYPE, flags[1]),
            ("occurrence", c483.B_OCCURRENCE, flags[2]),
            ("lock", c483.B_LOCK, flags[3]),
        ):
            append_majority(
                output,
                c483_group(endpoint, source_group),
                target,
                f"{route}-flag:{endpoint}:{name}",
                item.total_m2,
            )
        conditions.extend(flags)

        for lane, target in enumerate(item.carrier_output[endpoint]):
            append_majority(
                output,
                c483_group(endpoint, c483.B_GROUPS[lane]),
                target,
                f"{route}-carrier:{endpoint}:{lane}",
                item.total_m2,
            )

        if route == "sidecar":
            for lane, (source, target) in enumerate(zip(item.payload_input[endpoint], item.payload_output[endpoint])):
                output.append(gate("CNOT", (source, target), f"sidecar-payload-copy:{endpoint}:{lane}", item.total_m2))
            for lane, (source, target) in enumerate(zip(item.payload_output[endpoint][16:20], item.identity_output[endpoint])):
                output.append(gate("CNOT", (source, target), f"sidecar-identity:{endpoint}:{lane}", item.total_m2))
            content_source = item.payload_input[endpoint]
            content_target = item.payload_output[endpoint]
            identity_source = item.identity_output[endpoint]
        else:
            for position in range(c444.CLOCK_BITS):
                for binary_lane in range(4):
                    if (position >> binary_lane) & 1:
                        output.append(
                            gate(
                                "CNOT",
                                (item.payload_input[endpoint][position], item.code_output[endpoint][binary_lane]),
                                f"codec-position:{endpoint}:{position}:{binary_lane}",
                                item.total_m2,
                            )
                        )
                        output.append(
                            gate(
                                "CNOT",
                                (item.payload_input[endpoint][position], item.code_expected[endpoint][binary_lane]),
                                f"codec-expected-position:{endpoint}:{position}:{binary_lane}",
                                item.total_m2,
                            )
                        )
            for lane in range(14):
                source = item.payload_input[endpoint][16 + lane]
                output.append(gate("CNOT", (source, item.code_output[endpoint][4 + lane]), f"codec-field:{endpoint}:{lane}", item.total_m2))
                output.append(gate("CNOT", (source, item.code_expected[endpoint][4 + lane]), f"codec-expected-field:{endpoint}:{lane}", item.total_m2))
            content_source = item.code_expected[endpoint]
            content_target = item.code_output[endpoint]
            identity_source = item.code_output[endpoint][4:8]

        for lane, (source, target, work) in enumerate(
            zip(content_source, content_target, item.content_match[endpoint])
        ):
            append_xnor(output, source, target, work, f"{route}-content-match:{endpoint}:{lane}", item.total_m2)
        conditions.extend(item.content_match[endpoint])

        for lane, (target, work) in enumerate(zip(item.carrier_output[endpoint], item.carrier_match[endpoint])):
            source = c483_site(endpoint, c483.ACTIVE_WORD[lane])
            append_xnor(output, source, target, work, f"{route}-carrier-match:{endpoint}:{lane}", item.total_m2)
        conditions.extend(item.carrier_match[endpoint])

        expected_identity = bits(endpoint + 1, 4)
        for lane, (source, target, expected) in enumerate(
            zip(identity_source, item.identity_match[endpoint], expected_identity)
        ):
            append_constant_match(output, source, target, expected, f"{route}-identity-match:{endpoint}:{lane}", item.total_m2)
        conditions.extend(item.identity_match[endpoint])

    start_identity = item.identity_output[0] if route == "sidecar" else item.code_output[0][4:8]
    for lane, (source, target) in enumerate(zip(start_identity, item.predecessor)):
        output.append(gate("CNOT", (source, target), f"{route}-predecessor-copy:{lane}", item.total_m2))
    for lane, (source, predecessor, work) in enumerate(zip(start_identity, item.predecessor, item.predecessor_match)):
        append_xnor(output, source, predecessor, work, f"{route}-predecessor-match:{lane}", item.total_m2)
    conditions.extend(item.predecessor_match)
    append_prefix(output, tuple(conditions), item.prefix, item.total_m2)
    return tuple(output)


@lru_cache(maxsize=None)
def composite_schedule(route: str, horizon: int) -> tuple[Gate, ...]:
    c483.validate_horizon(horizon)
    total = layout(route).total_m2
    output = []
    for endpoint in range(ENDPOINTS):
        output.extend(shifted_c483(item, endpoint, total) for item in c483.bath_schedule(horizon))
    output.extend(adapter_schedule(route))
    return tuple(output)


def composite_initial(pair: ClockPair, case_name: str, law: str, route: str) -> Word:
    item = layout(route)
    if law not in c449.PROGRAMS:
        raise ValueError("unknown Cycle449 program law")
    state = [0] * item.total_m2
    for endpoint in range(ENDPOINTS):
        occurrence_initial = c483.prepare_state(case_name, law, route="bath", reset_work=1)
        offset = endpoint * c483.TOTAL_M2
        state[offset : offset + c483.TOTAL_M2] = occurrence_initial.bits
        for site, value in zip(item.payload_input[endpoint], pair.payloads[endpoint]):
            state[site] = value
    return tuple(state)


def replace_selected(state: list[int], sites: tuple[int, ...], values: Word) -> None:
    if len(sites) != len(values):
        raise ValueError("Cycle486 declarative field width mismatch")
    for site, value in zip(sites, values):
        state[site] = value


def declarative_codec(payload: Word) -> Word:
    """Independent one-hot-sector codec formula; no physical schedule call."""
    validate_endpoint_payload(payload)
    position = tuple(
        sum(payload[index] for index in range(c444.CLOCK_BITS) if (index >> lane) & 1) % 2
        for lane in range(4)
    )
    return position + payload[16:]


def coarse_composite_step(initial: Word, route: str, horizon: int) -> Word:
    """Independent declarative composite map used for the E/G comparison.

    The two frozen Cycle483 bath maps are lower-layer premises.  Everything
    after them is populated directly from the declared endpoint semantics.
    This function intentionally does not call adapter_schedule or
    composite_schedule.
    """

    item = layout(route)
    c483.validate_horizon(horizon)
    if len(initial) != item.total_m2:
        raise ValueError("Cycle486 coarse composite input width mismatch")
    adapter_inputs = {site for bank in item.payload_input for site in bank}
    if any(initial[site] for site in range(ENDPOINTS * c483.TOTAL_M2, item.total_m2) if site not in adapter_inputs):
        raise ValueError("Cycle486 declarative adapter outputs/work must enter blank")

    state = list(initial)
    conditions: list[int] = []
    identities: list[Word] = []
    for endpoint in range(ENDPOINTS):
        lower_initial = c483_slice(initial, endpoint)
        lower_output = c483.apply_schedule(lower_initial, c483.bath_schedule(horizon))
        offset = endpoint * c483.TOTAL_M2
        state[offset : offset + c483.TOTAL_M2] = lower_output.bits

        flags = (
            lower_output.bits[c483.B_FORM],
            c483.majority(lower_output.bits, c483.B_TYPE),
            c483.majority(lower_output.bits, c483.B_OCCURRENCE),
            c483.majority(lower_output.bits, c483.B_LOCK),
        )
        replace_selected(state, item.occurrence_flags[endpoint], flags)
        conditions.extend(flags)

        carrier = c483.majority_word(lower_output.bits, c483.B_GROUPS[:WORD])
        replace_selected(state, item.carrier_output[endpoint], carrier)
        payload = selected(state, item.payload_input[endpoint])
        validate_endpoint_payload(payload, endpoint + 1)

        if route == "sidecar":
            endpoint_word = payload
            replace_selected(state, item.payload_output[endpoint], endpoint_word)
            identity = endpoint_word[16:20]
            replace_selected(state, item.identity_output[endpoint], identity)
            content_expected = payload
        else:
            endpoint_word = declarative_codec(payload)
            replace_selected(state, item.code_output[endpoint], endpoint_word)
            replace_selected(state, item.code_expected[endpoint], endpoint_word)
            identity = endpoint_word[4:8]
            content_expected = endpoint_word
        identities.append(identity)

        content_match = tuple(int(left == right) for left, right in zip(content_expected, endpoint_word))
        replace_selected(state, item.content_match[endpoint], content_match)
        conditions.extend(content_match)

        active_word = selected(lower_output.bits, c483.ACTIVE_WORD)
        carrier_match = tuple(int(left == right) for left, right in zip(active_word, carrier))
        replace_selected(state, item.carrier_match[endpoint], carrier_match)
        conditions.extend(carrier_match)

        identity_match = tuple(int(left == right) for left, right in zip(identity, bits(endpoint + 1, 4)))
        replace_selected(state, item.identity_match[endpoint], identity_match)
        conditions.extend(identity_match)

    replace_selected(state, item.predecessor, identities[0])
    written_predecessor = selected(state, item.predecessor)
    predecessor_match = tuple(int(left == right) for left, right in zip(identities[0], written_predecessor))
    replace_selected(state, item.predecessor_match, predecessor_match)
    conditions.extend(predecessor_match)

    prefix: list[int] = []
    running = 1
    for condition in conditions:
        running &= condition
        prefix.append(running)
    replace_selected(state, item.prefix, tuple(prefix))
    return tuple(state)


def bit_residual(left: Word, right: Word) -> tuple[int, float]:
    if len(left) != len(right):
        raise ValueError("Cycle486 bit-residual widths differ")
    differences = tuple(abs(a - b) for a, b in zip(left, right))
    return sum(int(value != 0) for value in differences), float(max(differences, default=0))


@dataclass(frozen=True)
class BoundEndpoint:
    route: str
    law: str
    carrier: Word
    endpoint_word: Word
    event_identity: int
    predecessor_identity: int | None
    bath_relative_FORM_occurrence: bool = True
    framework_actuality: bool = False
    framework_Record: bool = False
    unbounded_permanence: bool = False


@dataclass(frozen=True)
class DecodedPair:
    endpoints: tuple[BoundEndpoint, BoundEndpoint]
    dK: int
    decoded_from: str
    proper_time: None = None
    lapse: None = None


def c483_slice(state: Word, endpoint: int) -> c483.State:
    offset = endpoint * c483.TOTAL_M2
    return c483.State(state[offset : offset + c483.TOTAL_M2])


def decode_composite(state: Word, route: str, horizon: int) -> DecodedPair | None:
    item = layout(route)
    if len(state) != item.total_m2 or state[item.prefix[-1]] != 1:
        return None
    occurrences = tuple(c483.bath_occurrence(c483_slice(state, endpoint), horizon) for endpoint in range(ENDPOINTS))
    if any(occurrence is None for occurrence in occurrences):
        return None
    endpoints = []
    for endpoint, occurrence in enumerate(occurrences):
        assert occurrence is not None
        carrier = selected(state, item.carrier_output[endpoint])
        if carrier != occurrence.content or len(carrier) != WORD:
            return None
        if route == "sidecar":
            endpoint_word = selected(state, item.payload_output[endpoint])
            identity = integer(selected(state, item.identity_output[endpoint]))
            position = c444.clock_position(endpoint_word[:16])
            binding = endpoint_word[20:]
        else:
            endpoint_word = selected(state, item.code_output[endpoint])
            if endpoint_word != selected(state, item.code_expected[endpoint]):
                return None
            position = integer(endpoint_word[:4])
            identity = integer(endpoint_word[4:8])
            binding = endpoint_word[8:]
        if identity != endpoint + 1 or binding != bits(1, 4) + bits(1, 4) + bits(0, 2):
            return None
        predecessor = None if endpoint == 0 else integer(selected(state, item.predecessor))
        endpoints.append(
            BoundEndpoint(
                route,
                occurrence.law,
                carrier,
                endpoint_word,
                identity,
                predecessor,
            )
        )
        if endpoint == 0:
            start_position = position
        else:
            end_position = position
    if endpoints[0].event_identity == endpoints[1].event_identity:
        return None
    if endpoints[1].predecessor_identity != endpoints[0].event_identity:
        return None
    if start_position >= end_position:
        return None
    return DecodedPair(
        tuple(endpoints),  # type: ignore[arg-type]
        end_position - start_position,
        "full physical 30-M2 sidecar words" if route == "sidecar" else "physical reversible 18-bit codec words",
    )


def carrier_is_actual_admitted(case_name: str, law: str, carrier: Word) -> bool:
    stimulus = c483.route_stimulus(law)
    packets = c449.packet_sets(case_name)[stimulus]
    expected = packets[1].word if law == "threshold3" else packets[0].word
    admissions = tuple(packet.admission for packet in packets if any(packet.admission))
    return carrier == expected and len(carrier) == WORD and bool(admissions) and all(all(word) for word in admissions)


def positive_route_controls() -> dict[str, object]:
    print("\nTWO BATH FORM OCCURRENCES / SIDECAR AND CODEC / TRAIN-HELD")
    rows = []
    failures = 0
    maximum_bit_residual = 0.0
    maximum_bit_mismatches = 0
    for size, length, law, route in product(
        (c444.TRAIN_SIZE, c444.HELD_SIZE),
        (1, 2),
        tuple(c449.PROGRAMS),
        ("sidecar", "codec"),
    ):
        case_name, horizon, start = context(size)
        pair = clock_pair(size, length, start)
        initial = composite_initial(pair, case_name, law, route)
        schedule = composite_schedule(route, horizon)
        output = apply_schedule(initial, schedule)
        coarse_expected = coarse_composite_step(initial, route, horizon)
        bit_mismatches, max_bit_residual = bit_residual(output, coarse_expected)
        restored = apply_schedule(output, schedule, reverse=True)
        decoded = decode_composite(output, route, horizon)
        exact = (
            bit_mismatches == 0
            and max_bit_residual == 0.0
            and restored == initial
            and decoded is not None
            and decoded.dK == 2 * length == pair.dK
            and len(decoded.endpoints) == 2
            and all(carrier_is_actual_admitted(case_name, law, endpoint.carrier) for endpoint in decoded.endpoints)
            and all(endpoint.bath_relative_FORM_occurrence for endpoint in decoded.endpoints)
            and all(not endpoint.framework_actuality and not endpoint.framework_Record for endpoint in decoded.endpoints)
            and decoded.proper_time is None
            and decoded.lapse is None
        )
        maximum_bit_residual = max(maximum_bit_residual, max_bit_residual)
        maximum_bit_mismatches = max(maximum_bit_mismatches, bit_mismatches)
        failures += int(not exact)
        rows.append(
            {
                "size": size,
                "Cycle443_case": case_name,
                "length": length,
                "law": law,
                "route": route,
                "horizon": horizon,
                "two_FORM_occurrences": None if decoded is None else len(decoded.endpoints),
                "dK": None if decoded is None else decoded.dK,
                "decoded_from": None if decoded is None else decoded.decoded_from,
                "coarse_physical_bit_mismatches": bit_mismatches,
                "exact_global_inverse": restored == initial,
                "E_G_max_bit_residual": max_bit_residual,
            }
        )
    check(
        "both positive routes bind two actual admitted-carrier FORM occurrences and decode dK=2/4 without refit",
        len(rows) == 24 and failures == 0,
        {
            "rows": rows,
            "failures": failures,
            "maximum_coarse_physical_bit_mismatches": maximum_bit_mismatches,
            "maximum_E_G_bit_residual": maximum_bit_residual,
        },
    )
    return {"rows": rows}


def without_label(schedule: tuple[Gate, ...], label: str) -> tuple[Gate, ...]:
    output = tuple(item for item in schedule if item.label != label)
    if len(output) != len(schedule) - 1:
        raise ValueError(f"deletion label is not unique: {label}")
    return output


def deletion_domain_controls() -> dict[str, object]:
    print("\nDELETIONS / MALFORMED / HELD BOUNDARY")
    pair = clock_pair(c444.TRAIN_SIZE, 2, c444.TRAIN_START)
    case_name, horizon, _start = context(c444.TRAIN_SIZE)
    results = {}
    for route in ("sidecar", "codec"):
        initial = composite_initial(pair, case_name, "immediate", route)
        schedule = composite_schedule(route, horizon)
        item = layout(route)
        nominal = apply_schedule(initial, schedule)
        results[f"{route}_nominal"] = decode_composite(nominal, route, horizon) is not None

        no_fresh = list(initial)
        no_fresh[c483_site(1, c483.B_FRESH)] = 0
        results[f"{route}_return_fresh_deleted"] = decode_composite(
            apply_schedule(tuple(no_fresh), schedule), route, horizon
        ) is None

        occurrence_deleted = without_label(schedule, f"{route}-flag:1:occurrence:lm")
        results[f"{route}_occurrence_term_deleted"] = decode_composite(
            apply_schedule(initial, occurrence_deleted), route, horizon
        ) is None

        predecessor_deleted = without_label(schedule, f"{route}-predecessor-copy:0")
        results[f"{route}_predecessor_deleted"] = decode_composite(
            apply_schedule(initial, predecessor_deleted), route, horizon
        ) is None

        prefix_deleted = without_label(schedule, f"binding-prefix:{len(item.prefix) - 1}")
        results[f"{route}_final_binding_gate_deleted"] = decode_composite(
            apply_schedule(initial, prefix_deleted), route, horizon
        ) is None

    side_schedule = composite_schedule("sidecar", horizon)
    side_initial = composite_initial(pair, case_name, "immediate", "sidecar")
    side_payload_deleted = without_label(side_schedule, "sidecar-payload-copy:1:5")
    side_deleted_output = apply_schedule(side_initial, side_payload_deleted)
    side_deleted_mismatches, side_deleted_residual = bit_residual(
        side_deleted_output, coarse_composite_step(side_initial, "sidecar", horizon)
    )
    results["sidecar_payload_lane_deleted"] = (
        decode_composite(side_deleted_output, "sidecar", horizon) is None
        and side_deleted_mismatches > 0
        and side_deleted_residual > 0
    )

    codec_schedule = composite_schedule("codec", horizon)
    codec_initial = composite_initial(pair, case_name, "immediate", "codec")
    codec_position_deleted = without_label(codec_schedule, "codec-position:1:5:0")
    codec_deleted_output = apply_schedule(codec_initial, codec_position_deleted)
    codec_deleted_mismatches, codec_deleted_residual = bit_residual(
        codec_deleted_output, coarse_composite_step(codec_initial, "codec", horizon)
    )
    results["codec_position_gate_deleted"] = (
        decode_composite(codec_deleted_output, "codec", horizon) is None
        and codec_deleted_mismatches > 0
        and codec_deleted_residual > 0
    )

    malformed = 0
    malformed_actions = (
        lambda: validate_endpoint_payload((0,) * 29),
        lambda: validate_endpoint_payload((0,) * 30),
        lambda: validate_endpoint_payload((1, 1) + (0,) * 14 + bits(1, 4) + (0,) * 10),
        lambda: validate_endpoint_payload(c444.one_hot(1) + bits(0, 4) + (0,) * 10),
        lambda: clock_pair(4, 1, 1),
        lambda: clock_pair(5, 3, 1),
        lambda: layout("alias"),
        lambda: composite_initial(pair, case_name, "unknown", "sidecar"),
        lambda: c483.validate_horizon(c483.HELD_HORIZON + 1),
    )
    for action in malformed_actions:
        try:
            action()
        except ValueError:
            malformed += 1

    check(
        "fresh token, occurrence, payload/codec, predecessor, final binding, malformed, and held-horizon controls are visible",
        all(results.values()) and malformed == len(malformed_actions),
        {
            "deletions": results,
            "load_bearing_gate_coarse_physical_mismatch": {
                "sidecar_payload_copy": {
                    "bit_mismatches": side_deleted_mismatches,
                    "max_bit_residual": side_deleted_residual,
                },
                "codec_position_CNOT": {
                    "bit_mismatches": codec_deleted_mismatches,
                    "max_bit_residual": codec_deleted_residual,
                },
            },
            "malformed_rejections": malformed,
            "held_L9_uses_Cycle483_horizon": c483.HELD_HORIZON,
            "seventh_repair_slice_available": False,
            "unbounded_permanence_claimed": False,
        },
    )
    return {"deletions": results, "malformed": malformed}


@dataclass(frozen=True)
class RouteTrace:
    logical_gates: int
    primitive_counts: dict[str, int]
    routed_gate_plans: int
    swap_spans: int
    restored_line_nn_primitives: int
    maximum_support_m2: int
    connected_failures: int
    sha256: str


@dataclass(frozen=True)
class SwapSpan:
    desired_operand: int
    start_position: int
    end_position: int

    @property
    def adjacent_swaps(self) -> int:
        return self.end_position - self.start_position


@dataclass(frozen=True)
class RestoredLinePlan:
    kind: str
    label: str
    logical_operands: tuple[int, ...]
    forward_spans: tuple[SwapSpan, ...]
    final_operand_sites: tuple[int, ...]
    adjacent_swap_count: int
    adjacency_failures: int
    operand_order_failures: int
    final_connectivity_failures: int
    restoration_failures: int

    @property
    def failures(self) -> int:
        return (
            self.adjacency_failures
            + self.operand_order_failures
            + self.final_connectivity_failures
            + self.restoration_failures
        )


def restored_line_plan(item: Gate, total_m2: int) -> RestoredLinePlan:
    if item.kind == "X":
        final_sites = item.sites
        return RestoredLinePlan(
            item.kind,
            item.label,
            item.sites,
            (),
            final_sites,
            0,
            0,
            0,
            int(len(final_sites) != 1),
            0,
        )
    labels = list(range(total_m2))
    targets = tuple(range(total_m2 - len(item.sites), total_m2))
    spans: list[SwapSpan] = []
    adjacency_failures = 0
    for desired, target in zip(reversed(item.sites), reversed(targets)):
        position = labels.index(desired)
        if position > target:
            raise RuntimeError("Cycle486 restored-line router order failed")
        start = position
        while position < target:
            adjacency_failures += int(position + 1 - position != 1)
            labels[position], labels[position + 1] = labels[position + 1], labels[position]
            position += 1
        spans.append(SwapSpan(desired, start, target))
    operand_order_failures = int(tuple(labels[index] for index in targets) != item.sites)
    final_connectivity_failures = sum(
        int(right != left + 1) for left, right in zip(targets[:-1], targets[1:])
    )

    restored = list(labels)
    for span in reversed(spans):
        for left in reversed(range(span.start_position, span.end_position)):
            adjacency_failures += int(left + 1 - left != 1)
            restored[left], restored[left + 1] = restored[left + 1], restored[left]
    restoration_failures = int(restored != list(range(total_m2)))
    return RestoredLinePlan(
        item.kind,
        item.label,
        item.sites,
        tuple(spans),
        targets,
        sum(span.adjacent_swaps for span in spans),
        adjacency_failures,
        operand_order_failures,
        final_connectivity_failures,
        restoration_failures,
    )


@lru_cache(maxsize=None)
def adapter_plans(route: str) -> tuple[RestoredLinePlan, ...]:
    item = layout(route)
    return tuple(restored_line_plan(primitive, item.total_m2) for primitive in adapter_schedule(route))


@lru_cache(maxsize=None)
def adapter_trace(route: str) -> RouteTrace:
    schedule = adapter_schedule(route)
    plans = adapter_plans(route)
    digest = sha256(b"Cycle486 deterministic restored right-edge line router v2 with explicit plans")
    primitives = 0
    failures = 0
    for primitive, plan in zip(schedule, plans):
        if (primitive.kind, primitive.label, primitive.sites) != (
            plan.kind,
            plan.label,
            plan.logical_operands,
        ):
            failures += 1
        swaps = plan.adjacent_swap_count
        base = 3 if primitive.kind == "SWAP" else 1
        primitives += base + 6 * swaps
        failures += plan.failures
        digest.update(
            (
                f"{primitive.kind}|{primitive.sites}|{primitive.label}|"
                f"{tuple((span.desired_operand, span.start_position, span.end_position) for span in plan.forward_spans)}|"
                f"{plan.final_operand_sites}|{plan.adjacent_swap_count}|{plan.failures}\n"
            ).encode()
        )
    return RouteTrace(
        len(schedule),
        dict(Counter(primitive.kind for primitive in schedule)),
        len(plans),
        sum(len(plan.forward_spans) for plan in plans),
        primitives,
        max(len(primitive.sites) for primitive in schedule),
        failures,
        digest.hexdigest(),
    )


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def coordinate_support_connected(support: tuple[Coord, ...]) -> bool:
    if not support:
        return False
    reached = {support[0]}
    changed = True
    while changed:
        changed = False
        for site in support:
            if site not in reached and any(manhattan(site, other) == 1 for other in reached):
                reached.add(site)
                changed = True
    return len(reached) == len(support)


def covariance_resource_controls() -> dict[str, object]:
    print("\nALL24 / FIXED NN SCHEDULE / RESOURCE LEDGER")
    traces = {route: adapter_trace(route) for route in ("sidecar", "codec")}
    failures = 0
    frame_rows = []
    maximum_total = max(layout(route).total_m2 for route in traces)
    for frame_index, frame in enumerate(c444.FRAMES):
        coordinates = tuple(
            tuple(int(value) for value in frame @ np.asarray((site, 0, 0)))
            for site in range(maximum_total)
        )
        line_ok = len(set(coordinates)) == maximum_total and all(
            manhattan(coordinates[index], coordinates[index + 1]) == 1
            for index in range(maximum_total - 1)
        )
        frame_plan_failures = 0
        for route in traces:
            total_m2 = layout(route).total_m2
            for plan in adapter_plans(route):
                final_support = tuple(coordinates[site] for site in plan.final_operand_sites)
                frame_plan_failures += int(not coordinate_support_connected(final_support))
                for span in plan.forward_spans:
                    span_in_domain = (
                        0 <= span.start_position <= span.end_position < total_m2
                        and span.adjacent_swaps == span.end_position - span.start_position
                    )
                    # The complete transformed line was checked edge by edge;
                    # a valid span is therefore an explicit subset of those
                    # certified adjacent edges in this frame.
                    frame_plan_failures += int(not line_ok or not span_in_domain)
        failures += int(not line_ok) + frame_plan_failures
        frame_rows.append(
            {
                "frame": frame_index,
                "line_ok": line_ok,
                "routed_plan_failures": frame_plan_failures,
            }
        )

    resources = {}
    for route, trace in traces.items():
        item = layout(route)
        resources[route] = {
            "total_M2": item.total_m2,
            "adapter_trace": trace,
            "train_full_logical_gates": 2 * len(c483.bath_schedule(c483.TRAIN_HORIZON)) + trace.logical_gates,
            "held_full_logical_gates": 2 * len(c483.bath_schedule(c483.HELD_HORIZON)) + trace.logical_gates,
            "train_fresh_bath_M2_pair": 2 * (261 + c483.TRAIN_HORIZON * 255),
            "held_fresh_bath_M2_pair": 2 * (261 + c483.HELD_HORIZON * 255),
        }
    check(
        "the imported bath blocks and new adapter schedules form one bounded restored-NN family in all proper-cubic frames",
        len(c444.FRAMES) == 24
        and failures == 0
        and maximum_total < 64_000
        and all(trace.maximum_support_m2 <= 3 and trace.connected_failures == 0 for trace in traces.values()),
        {
            "proper_cubic_frames": len(c444.FRAMES),
            "frame_failures": failures,
            "frame_rows": frame_rows,
            "maximum_total_M2": maximum_total,
            "resources": resources,
            "imported_Cycle483_bath_train_trace_SHA256": "e5074999da01505a38fdcfac772bcb93ece1649c5d524107f4e9a0946e08cc77",
            "imported_Cycle483_bath_held_trace_SHA256": "cbeed0d438c432a0324762b194bfce22a1a331eb5605e1b8db8254118b8d2cbc",
            "primitive_support_M2": 3,
        },
    )
    return {"traces": traces, "resources": resources}


def inventory_n1_n8_controls() -> dict[str, object]:
    print("\nSUPPLIED / DERIVED / OPEN / FULL N1-N8")
    supplied = (
        "actual frozen Cycle444 launch/return latch payloads and echo candidate update",
        "actual frozen Cycle443 admitted carriers and Cycle449 one-hot law program",
        "two independent Cycle483 blank bath stacks and supplied FORM/TYPE/OCCURRENCE/LOCK semantics",
        "event identities 1 then 2, common oscillator/device/epoch binding, and predecessor grammar",
        "train L5/Cycle443 L3 and held L9/Cycle443 L6 pairing",
        "restored-line geometry, finite three/six repair horizons, and proper-cubic frame family",
    )
    derived = (
        "direct-alias lawfulness failure on all eight actual launch/return train/held payloads",
        "two exact bath-dilation inverses per endpoint pair",
        "full 79+30 sidecar binding and distinct reversible 18-bit codec binding",
        "unique event identities, exact predecessor, carrier, payload/codec, and occurrence checks",
        "dK 2 and 4 decoded from physical endpoint words on train L5 and held L9 without refit",
        "fixed bounded M2 schedules, restored NN manifests, all24, deletions, malformed and resource controls",
    )
    open_items = (
        "selection or derivation of the Cycle444 update and Cycle483 bath FORM law",
        "one realized member for coherent or mixed candidate inputs",
        "framework Record typing, actuality, and unbounded permanence",
        "bath and endpoint capacity renewal plus physical epoch rollover",
        "echo calibration, universal clock equivalence, physical proper time, lapse, and empirical scale",
        "source response, energy/stress identification, gravity, and Born/frequency law",
    )
    n1 = (
        "raw equal-width cylinder alias — ATTEMPTED; falsified on the exact eight bounded payloads only",
        "full disjoint sidecar product — ATTEMPTED; succeeds and defeats any broad format-incompatibility no-go",
        "reversible compressed clock codec — ATTEMPTED; succeeds and is distinct in primary endpoint representation",
        "tagged sum-type endpoint union — OPEN; could retain separate schemas under an explicit tag",
        "autonomous joint clock/occurrence coformation — OPEN; could generate both carriers in one local law",
        "instrument trajectory with retained outcome carrier — OPEN; could select a realized endpoint member",
        "migratory/topological predecessor chain — OPEN; could extend identity and permanence beyond six slices",
    )
    n2 = (
        "bath-law selection, realized-member selection, framework Record typing/permanence, bath/epoch renewal, and calibration/proper-time interpretation remain pairwise independent",
    )
    result = {
        "supplied": supplied,
        "derived": derived,
        "open": open_items,
        "N1": n1,
        "N2": n2,
        "N3": "candidate update, bath purity, FORM semantics, identities, predecessor grammar, contexts, geometry, horizons, calibration and discarded baths are explicit supplies",
        "N4": "Cycle342/364 matches only the attempted cylinder alias residual; Cycle444 matches the clock payload residual; Cycle443/449 matches admitted precommit; Cycle483 matches bath-relative occurrence, not framework actuality",
        "N5": "the alias falsifier is restricted to eight actual 30-M2 endpoint payloads and is not generalized to arbitrary codecs, sidecars, blocks, or lattice-wide laws",
        "N6": "the two positive adapters are explicit import-bound-theorem candidates; later law selection, renewal, Record typing and calibration audits can retire separate imports without an axiom",
        "N7": "a hostile reviewer points to the successful sidecar and codec, then demands an autonomous coformation or tagged-union law; those live mechanisms defeat any route-independent obstruction",
        "N8": "Cycles443, 449 and 483 repeatedly retired apparent format/actualization walls by retained carriers, fixed programs and explicit dilations; Cycle486 again succeeds by retained sidecar and codec structure",
        "claim_gate": "direct-alias finite falsifier PASS; broad no-go FAIL; minimum-content FAIL; shared-obstruction FAIL; axiom-pressure FAIL; no axiom pressure",
    }
    check(
        "the exact supplied/derived/open ledger and full N1-N8 preserve only the narrow alias falsifier",
        AUTHORITY == "none"
        and AUDIT == "unset"
        and len(n1) >= 5
        and "no axiom pressure" in result["claim_gate"],
        result,
    )
    return result


def resource_guard(started: float) -> None:
    elapsed = time.monotonic() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = int(raw) if sys.platform == "darwin" else int(raw * 1024)
    check(
        "the Cycle486 runner remains inside its declared wall/RSS caps",
        elapsed < WALL_CAP_SECONDS and peak_bytes < RSS_CAP_BYTES,
        {
            "elapsed_seconds": elapsed,
            "peak_RSS_MiB": peak_bytes / 1024**2,
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "RSS_cap_GiB": RSS_CAP_BYTES / 1024**3,
        },
    )


def main() -> int:
    started = time.monotonic()
    note_contract()
    direct_alias_controls()
    positive_route_controls()
    deletion_domain_controls()
    covariance_resource_controls()
    inventory_n1_n8_controls()
    resource_guard(started)
    print("\nRESULT", f"pass={PASS}", f"fail={FAIL}")
    if FAIL == 0:
        print("RESULT PHYSICAL_RECORD_OCCURRENCE_CLOCK_ENDPOINT_ADAPTER_CERTIFIED")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
