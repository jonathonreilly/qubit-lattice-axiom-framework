#!/usr/bin/env python3
"""Compile Cycle 48's finite six-bit decoder into local permanent records.

This is a campaign probe, not an authority-bearing result.  A six-site serial
prefix chain reads literal H0/H1 preparation records.  Every prefix has its
own physical role, so the sixth record is already one of sixty valid state-ID
records or one of four explicit rejects.  The compiled rows are merged with
the Cycle-144 physical-byte/recurrent-root law and screened on every word and
proper-cubic image.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import product

import physical_r_b01_recurrent_root_bind_cycle144_2026_07_15 as bound


c53 = bound.c53
cell = bound.cell
Coord = tuple[int, int, int]
Signature = c53.Signature
Word = tuple[int, int, int, int, int, int]

H0 = "H0"
H1 = "H1"
START_ROLE = "START"
TAG_ROLE = "MARK"
BACKSTOP_ROLE = "BACKSTOP"
CAGE_ROLE = TAG_ROLE

# Exactly 27 roles are kept out of the prefix alphabet.  Besides the decoder
# constants, these are the live Cycle-144 interface roles most likely to occur
# on an exposed frontier.  The remaining 126 roles exactly fit all nonempty
# binary prefixes of length at most six.
RESERVED_ROLES = frozenset({
    H0, H1, START_ROLE, TAG_ROLE, BACKSTOP_ROLE,
    "R_B01", "R_B21", "B1", "J1", "J2", "J3", "J6", "JOINT",
    "OZ", "W3", "A_0_0", "R_A22", "R_A21", "R_A13", "R_C23",
    "B0", "GU", "GY", "R_LB", "R_C22", "ALL", "AUX",
})
PREFIX_ROLES = tuple(sorted(cell.FULL_ROLES - RESERVED_ROLES))
PREFIXES = tuple(
    prefix
    for length in range(1, 7)
    for prefix in product((0, 1), repeat=length)
)
PREFIX_ROLE = dict(zip(PREFIXES, PREFIX_ROLES, strict=True))
ROLE_PREFIX = {role: prefix for prefix, role in PREFIX_ROLE.items()}

DATA = tuple((index, 0, 0) for index in range(6))
CHAIN = tuple((index, 1, 0) for index in range(6))
START = (-1, 1, 0)
SHIFT = (60, 50, 40)
CORE_SITES = frozenset((*DATA, *CHAIN, START))
CAGE_SITES = tuple(sorted({
    c53.add(site, direction)
    for site in CORE_SITES
    for direction in c53.DIRECTIONS
    if c53.add(site, direction) not in CORE_SITES
}))


def bit_role(bit: int) -> str:
    return H1 if bit else H0


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def local_source(word: Word) -> dict[Coord, str]:
    # A solid one-cell quiet shell makes every exterior open site unary.  The
    # only holes are the six serial chain targets.
    records = {site: CAGE_ROLE for site in CAGE_SITES}
    records[START] = START_ROLE
    records.update({site: bit_role(bit) for site, bit in zip(DATA, word)})
    return records


def canonical_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}
    for prefix in PREFIXES:
        index = len(prefix) - 1
        word: Word = tuple(prefix + (0,) * (6 - len(prefix)))  # type: ignore[assignment]
        records = local_source(word)
        records.update({
            CHAIN[prior]: PREFIX_ROLE[prefix[: prior + 1]]
            for prior in range(index)
        })
        local = c53.canonical_signature(c53.local_signature(records, CHAIN[index]))
        output = PREFIX_ROLE[prefix]
        prior = table.get(local)
        if prior is not None and prior != output:
            raise ValueError((prefix, local, prior, output))
        table[local] = output
    return table


CANONICAL_TABLE = canonical_table()
DECODER_RAW = cell.merge_raw(*(
    cell.raw_orbit(local, output)
    for local, output in CANONICAL_TABLE.items()
))
MERGED_RAW = cell.merge_raw(bound.FINAL_RAW, DECODER_RAW)
RAW_CONFLICTS = {
    local: values for local, values in MERGED_RAW.items() if len(values) != 1
}


def local_outputs(word: Word) -> dict[Coord, str]:
    return {
        CHAIN[index]: PREFIX_ROLE[word[: index + 1]]
        for index in range(6)
    }


def transform(records: dict[Coord, str], rotation, shift: Coord = SHIFT):
    return c53.transform_records(records, rotation, shift)


BOUND_TERMINAL = {**bound.b.FACTOR_SOURCE, **bound.b.FACTOR_OUTPUTS}
BOUND_IGNORED = bound.b.BIND_IGNORED


def enabled(records: dict[Coord, str]):
    return {
        target: MERGED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in MERGED_RAW
    }


def exact_instance(word: Word, rotation) -> tuple[bool, object]:
    source = {**BOUND_TERMINAL, **transform(local_source(word), rotation)}
    outputs = transform(local_outputs(word), rotation)
    records = dict(source)
    states = 0
    edges = 0
    for index in range(7):
        actual = enabled(records)
        states += 1
        unexpected = {
            target: values
            for target, values in actual.items()
            if BOUND_IGNORED.get(target) != values
            and outputs.get(target) not in values
        }
        if unexpected:
            return False, ("unexpected", index, tuple(sorted(unexpected.items()))[:8])
        decoder_front = {
            target: values
            for target, values in actual.items()
            if target in outputs and target not in records
        }
        if index == 6:
            if decoder_front:
                return False, ("terminal-front", decoder_front)
            final_site = transform({CHAIN[-1]: "x"}, rotation)
            site = next(iter(final_site))
            expected_prefix = word
            if ROLE_PREFIX.get(records.get(site)) != expected_prefix:
                return False, ("decode", records.get(site), expected_prefix)
            return True, (states, edges)
        expected_site = transform({CHAIN[index]: "x"}, rotation)
        site = next(iter(expected_site))
        expected = frozenset((outputs[site],))
        if decoder_front != {site: expected}:
            return False, ("front", index, decoder_front, site, expected)
        records[site] = outputs[site]
        edges += 1
    raise AssertionError("unreachable")


def standalone_mutation_screen() -> tuple[int, tuple[object, ...]]:
    """Delete or flip every literal input record; no wrong valid ID may form."""
    attempts = 0
    failures: list[object] = []
    identity = c53.ROTATIONS[0]
    for value in range(64):
        word: Word = tuple((value >> shift) & 1 for shift in range(5, -1, -1))  # type: ignore[assignment]
        source = local_source(word)
        for index, site in enumerate(DATA):
            for replacement in (None, bit_role(1 - word[index])):
                attempts += 1
                trial = dict(source)
                if replacement is None:
                    del trial[site]
                else:
                    trial[site] = replacement
                records = {**BOUND_TERMINAL, **transform(trial, identity)}
                intended = transform(local_outputs(word), identity)
                for _step in range(6):
                    actual = enabled(records)
                    new = {
                        target: values for target, values in actual.items()
                        if target not in BOUND_IGNORED and target not in records
                    }
                    if len(new) != 1:
                        break
                    target, values = next(iter(new.items()))
                    if len(values) != 1:
                        break
                    records[target] = next(iter(values))
                final_site = next(iter(transform({CHAIN[-1]: "x"}, identity)))
                final = records.get(final_site)
                if final is not None and ROLE_PREFIX.get(final) == word:
                    failures.append((value, index, replacement, "unchanged-valid-id"))
    return attempts, tuple(failures)


def main() -> int:
    print("ROLE_CENSUS", len(cell.FULL_ROLES), len(RESERVED_ROLES), len(PREFIX_ROLES), len(PREFIXES))
    print("TABLE_CENSUS", len(CANONICAL_TABLE), len(DECODER_RAW), len(MERGED_RAW), len(RAW_CONFLICTS))
    if RAW_CONFLICTS:
        print("RAW_CONFLICT_SAMPLE", tuple(RAW_CONFLICTS.items())[:12])

    failures = []
    states = edges = 0
    valid_roles = set()
    reject_roles = set()
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for value in range(64):
            word: Word = tuple((value >> shift) & 1 for shift in range(5, -1, -1))  # type: ignore[assignment]
            ok, detail = exact_instance(word, rotation)
            if not ok:
                failures.append((rotation_index, value, detail))
            else:
                state_count, edge_count = detail  # type: ignore[misc]
                states += state_count
                edges += edge_count
            final_role = PREFIX_ROLE[word]
            (valid_roles if value < 60 else reject_roles).add(final_role)

    attempts, mutation_failures = standalone_mutation_screen()
    print("INSTANCE_CENSUS", 24 * 64, states, edges, len(failures))
    if failures:
        print("INSTANCE_FAILURE_SAMPLE", failures[:12])
    print("DECODER_CENSUS", len(valid_roles), len(reject_roles), bool(valid_roles & reject_roles))
    print("MUTATION_CENSUS", attempts, len(mutation_failures))
    if mutation_failures:
        print("MUTATION_FAILURE_SAMPLE", mutation_failures[:12])
    result = (
        len(PREFIX_ROLES) == len(PREFIXES) == 126
        and len(CANONICAL_TABLE) == 126
        and not RAW_CONFLICTS
        and not failures
        and len(valid_roles) == 60
        and len(reject_roles) == 4
        and not (valid_roles & reject_roles)
        and not mutation_failures
    )
    print("RESULT", "FINITE_CYCLE48_LOCAL_DECODER" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
