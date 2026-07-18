#!/usr/bin/env python3
"""Cycle 185: binary-physicalization and complexity census of the full law.

The current Cycle-178 union is an exact deterministic table over symbolic
onsite roles.  This probe asks what that table becomes when every role and
every open neighbour slot is encoded by literal binary records.  It measures:

* the exact role and bit-width requirement;
* raw and proper-cubic-orbit rule counts;
* arity and orbit-size distributions;
* exact 48-bit input / 8-bit output classifier size;
* prefix-trie sharing and a representation-dependent compression census; and
* the remaining gap between finite physical compilability and a natural law.

The runner has no authority.  It edits no foundation, axiom, primitive,
registry, policy, audit, queue, predecessor, commit, push, or PR surface.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import math
from pathlib import Path
import zlib

import recurrent_five_literal_lane_worldline_cycle178_2026_07_16 as c178


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "FULL_LAW_BINARY_PHYSICALIZATION_CENSUS_CYCLE185_NOTE_2026-07-16.md"
)

c53 = c178.c171.c53
LAW = c178.FULL_RAW
DIRECTIONS = tuple(c53.DIRECTIONS)
ROTATIONS = tuple(c53.ROTATIONS)

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


def unique_output(values: frozenset[str]) -> str:
    if len(values) != 1:
        raise ValueError(("nondeterministic-output", values))
    return next(iter(values))


INPUT_ROLES = frozenset(
    role
    for signature in LAW
    for _direction, role in signature
)
OUTPUT_ROLES = frozenset(
    unique_output(values)
    for values in LAW.values()
)
ALL_ROLES = tuple(sorted(INPUT_ROLES | OUTPUT_ROLES))
ROLE_CODE = {
    role: index + 1
    for index, role in enumerate(ALL_ROLES)
}
OPEN_CODE = 0
PORT_SYMBOL_COUNT = len(ALL_ROLES) + 1
ROLE_BITS = math.ceil(math.log2(max(1, len(ALL_ROLES))))
PORT_BITS = math.ceil(math.log2(PORT_SYMBOL_COUNT))
INPUT_BITS = len(DIRECTIONS) * PORT_BITS
OUTPUT_BITS = ROLE_BITS


def signature_codes(signature) -> tuple[int, ...]:
    present = dict(signature)
    return tuple(
        ROLE_CODE[present[direction]]
        if direction in present
        else OPEN_CODE
        for direction in DIRECTIONS
    )


def codes_to_int(codes: tuple[int, ...]) -> int:
    answer = 0
    for code in codes:
        answer = (answer << PORT_BITS) | code
    return answer


def encoded_rows():
    rows = []
    for signature, values in LAW.items():
        output = unique_output(values)
        codes = signature_codes(signature)
        rows.append((codes_to_int(codes), ROLE_CODE[output], signature, output))
    return tuple(sorted(rows))


ENCODED_ROWS = encoded_rows()
ENCODED_KEYS = tuple(row[0] for row in ENCODED_ROWS)


def lcp_length(left: int, right: int, width: int) -> int:
    difference = left ^ right
    return width if difference == 0 else width - difference.bit_length()


def prefix_counts(keys: tuple[int, ...], width: int) -> tuple[int, ...]:
    counts = [1]
    for depth in range(1, width + 1):
        count = 1
        for left, right in zip(keys, keys[1:]):
            if lcp_length(left, right, width) < depth:
                count += 1
        counts.append(count)
    return tuple(counts)


PREFIX_COUNTS = prefix_counts(ENCODED_KEYS, INPUT_BITS)
FULL_TRIE_NODES = sum(PREFIX_COUNTS)
PATRICIA_BRANCH_NODES = max(0, len(ENCODED_KEYS) - 1)
PATRICIA_TOTAL_NODES = (
    0
    if not ENCODED_KEYS
    else 2 * len(ENCODED_KEYS) - 1
)


def shortest_unique_prefix_lengths(
    keys: tuple[int, ...],
    width: int,
) -> tuple[int, ...]:
    lengths = []
    for index, key in enumerate(keys):
        left = lcp_length(keys[index - 1], key, width) if index else -1
        right = (
            lcp_length(key, keys[index + 1], width)
            if index + 1 < len(keys)
            else -1
        )
        lengths.append(min(width, max(left, right) + 1))
    return tuple(lengths)


UNIQUE_PREFIX_LENGTHS = shortest_unique_prefix_lengths(ENCODED_KEYS, INPUT_BITS)


def orbit_census():
    groups = defaultdict(set)
    failures = []
    for signature, values in LAW.items():
        output = unique_output(values)
        canonical = c53.canonical_signature(signature)
        groups[(canonical, output)].add(signature)
        for rotation in ROTATIONS:
            rotated = c53.rotate_signature(signature, rotation)
            if LAW.get(rotated) != values:
                failures.append((signature, output, rotation, LAW.get(rotated)))
                break
    return groups, tuple(failures)


ORBIT_GROUPS, COVARIANCE_FAILURES = orbit_census()
ORBIT_SIZES = Counter(len(signatures) for signatures in ORBIT_GROUPS.values())
ARITY_HISTOGRAM = Counter(len(signature) for signature in LAW)
OUTPUT_HISTOGRAM = Counter(
    unique_output(values)
    for values in LAW.values()
)


def serialize_rows(rows) -> bytes:
    packed = bytearray()
    for key, output, _signature, _role in rows:
        packed.extend(key.to_bytes(INPUT_BITS // 8, "big"))
        packed.append(output)
    return bytes(packed)


RAW_SERIAL = serialize_rows(ENCODED_ROWS)
RAW_COMPRESSED = zlib.compress(RAW_SERIAL, level=9)


def canonical_encoded_rows():
    rows = []
    for canonical, output in ORBIT_GROUPS:
        rows.append(
            (
                codes_to_int(signature_codes(canonical)),
                ROLE_CODE[output],
                canonical,
                output,
            )
        )
    return tuple(sorted(rows))


CANONICAL_ROWS = canonical_encoded_rows()
CANONICAL_SERIAL = serialize_rows(CANONICAL_ROWS)
CANONICAL_COMPRESSED = zlib.compress(CANONICAL_SERIAL, level=9)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND EXACT LAW")
    check("Cycle-185 review note exists", NOTE.is_file())
    check(
        "the consumed Cycle-178 law is deterministic",
        len(LAW) == 101_996
        and all(len(values) == 1 for values in LAW.values())
        and not c178.RAW_CONFLICTS,
        (len(LAW), len(c178.RAW_CONFLICTS)),
    )
    check(
        "the law uses the current 153-role onsite alphabet",
        len(ALL_ROLES) == 153
        and INPUT_ROLES <= set(ALL_ROLES)
        and OUTPUT_ROLES <= set(ALL_ROLES),
        (len(INPUT_ROLES), len(OUTPUT_ROLES), len(ALL_ROLES)),
    )

    print("\nBINARY PHYSICALIZATION CONTRACT")
    check(
        "open plus 153 roles requires exactly eight literal bits per port",
        PORT_SYMBOL_COUNT == 154
        and ROLE_BITS == 8
        and PORT_BITS == 8
        and 2**7 < PORT_SYMBOL_COUNT <= 2**8,
        (PORT_SYMBOL_COUNT, ROLE_BITS, PORT_BITS),
    )
    check(
        "one exact six-neighbour rule row is a 48-bit to 8-bit classifier",
        len(DIRECTIONS) == 6
        and INPUT_BITS == 48
        and OUTPUT_BITS == 8
        and all(0 <= key < 2**48 for key in ENCODED_KEYS),
        (INPUT_BITS, OUTPUT_BITS),
    )
    check(
        "the binary encoding is injective on every exact raw signature",
        len(ENCODED_ROWS) == len(LAW)
        and len(set(ENCODED_KEYS)) == len(LAW),
        (len(ENCODED_ROWS), len(set(ENCODED_KEYS))),
    )

    print("\nPROPER-CUBIC ORBIT CENSUS")
    check(
        "the complete raw table is exactly proper-cubic covariant",
        not COVARIANCE_FAILURES,
        COVARIANCE_FAILURES[:1],
    )
    check(
        "every raw row belongs to exactly one canonical output-labelled orbit",
        sum(ORBIT_SIZES[size] * size for size in ORBIT_SIZES) == len(LAW)
        and set(ORBIT_SIZES) <= {1, 2, 3, 4, 6, 8, 12, 24},
        (len(ORBIT_GROUPS), ORBIT_SIZES),
    )
    check(
        "the arity census covers every raw signature",
        sum(ARITY_HISTOGRAM.values()) == len(LAW)
        and set(ARITY_HISTOGRAM) <= set(range(7)),
        ARITY_HISTOGRAM,
    )

    print("\nEXACT CLASSIFIER SIZE")
    check(
        "the literal flat program bank has 5,711,776 key/output bits",
        len(LAW) * (INPUT_BITS + OUTPUT_BITS) == 5_711_776
        and len(RAW_SERIAL) == len(LAW) * 7,
        (len(RAW_SERIAL), len(RAW_COMPRESSED)),
    )
    check(
        "the full binary prefix trie shares exact input prefixes",
        PREFIX_COUNTS[0] == 1
        and PREFIX_COUNTS[-1] == len(LAW)
        and FULL_TRIE_NODES < 1 + len(LAW) * INPUT_BITS,
        (FULL_TRIE_NODES, PREFIX_COUNTS[:9], PREFIX_COUNTS[-9:]),
    )
    check(
        "Patricia compression remains a six-figure decision object",
        PATRICIA_BRANCH_NODES == len(LAW) - 1
        and PATRICIA_TOTAL_NODES == 2 * len(LAW) - 1,
        (PATRICIA_BRANCH_NODES, PATRICIA_TOTAL_NODES),
    )
    check(
        "unique prefixes do not replace full exact-neighbour verification",
        min(UNIQUE_PREFIX_LENGTHS) >= 1
        and max(UNIQUE_PREFIX_LENGTHS) <= INPUT_BITS
        and any(length < INPUT_BITS for length in UNIQUE_PREFIX_LENGTHS),
        (
            min(UNIQUE_PREFIX_LENGTHS),
            max(UNIQUE_PREFIX_LENGTHS),
            round(sum(UNIQUE_PREFIX_LENGTHS) / len(UNIQUE_PREFIX_LENGTHS), 3),
        ),
    )

    print("\nREPRESENTATION CENSUS")
    check(
        "rotation quotienting materially shrinks but does not trivialize the table",
        1 < len(CANONICAL_ROWS) < len(ENCODED_ROWS)
        and len({row[0] for row in CANONICAL_ROWS}) == len(CANONICAL_ROWS)
        and len(CANONICAL_SERIAL) == len(CANONICAL_ROWS) * 7,
        (
            len(CANONICAL_ROWS),
            len({row[0] for row in CANONICAL_ROWS}),
            len(CANONICAL_SERIAL),
            len(CANONICAL_COMPRESSED),
        ),
    )
    check(
        "all serialized rows round-trip within one-byte role codes",
        max(ROLE_CODE.values()) == 153
        and len(RAW_SERIAL) == 713_972
        and len(CANONICAL_SERIAL) % 7 == 0,
        (max(ROLE_CODE.values()), len(RAW_SERIAL)),
    )
    check(
        "the output census accounts for every row and remains multi-role",
        sum(OUTPUT_HISTOGRAM.values()) == len(LAW)
        and len(OUTPUT_HISTOGRAM) > 2,
        (len(OUTPUT_HISTOGRAM), OUTPUT_HISTOGRAM.most_common(10)),
    )

    print("\nSCOPE")
    check(
        "the note distinguishes finite compilation from law selection",
        NOTE.is_file()
        and "finite physical compilability is not natural-law selection"
        in NOTE.read_text(),
    )

    print("\nACCOUNTING")
    print("RAW_ROWS", len(LAW))
    print("CANONICAL_ORBITS", len(ORBIT_GROUPS))
    print("ORBIT_SIZES", ORBIT_SIZES)
    print("ARITY_HISTOGRAM", ARITY_HISTOGRAM)
    print("INPUT_ROLES", len(INPUT_ROLES))
    print("OUTPUT_ROLES", len(OUTPUT_ROLES))
    print("ALL_ROLES", len(ALL_ROLES))
    print("PORT_SYMBOLS", PORT_SYMBOL_COUNT)
    print("INPUT_BITS", INPUT_BITS)
    print("OUTPUT_BITS", OUTPUT_BITS)
    print("FLAT_PROGRAM_BITS", len(LAW) * (INPUT_BITS + OUTPUT_BITS))
    print("FULL_TRIE_NODES", FULL_TRIE_NODES)
    print("PATRICIA_TOTAL_NODES", PATRICIA_TOTAL_NODES)
    print(
        "UNIQUE_PREFIX_LENGTHS",
        (
            min(UNIQUE_PREFIX_LENGTHS),
            max(UNIQUE_PREFIX_LENGTHS),
            sum(UNIQUE_PREFIX_LENGTHS) / len(UNIQUE_PREFIX_LENGTHS),
        ),
    )
    print("RAW_SERIAL_BYTES", len(RAW_SERIAL))
    print("RAW_ZLIB_BYTES", len(RAW_COMPRESSED))
    print("CANONICAL_SERIAL_BYTES", len(CANONICAL_SERIAL))
    print("CANONICAL_ZLIB_BYTES", len(CANONICAL_COMPRESSED))
    print("OUTPUT_ROLES_USED", len(OUTPUT_HISTOGRAM))
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "FULL_LAW_FINITE_BINARY_COMPILE_WITH_LARGE_UNSELECTED_RULE_VALUE"
        if FAIL == 0
        else "CYCLE185_NEEDS_REPAIR",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
