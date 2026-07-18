#!/usr/bin/env python3
"""Verify the factorized comparator/XOR logic for commuting signed membership.

The five literal inputs, the commuting product row, and the equality outputs
fed to the XOR component are supplied by the host in this probe.  It is a
component theorem, not yet an end-to-end physical signed-membership apparatus.
"""

from __future__ import annotations

from itertools import product

import cycle48_symplectic_tableau_compression_probe_2026_07_15 as tableau
import physical_joint_stabilizer_update_geometry_probe_2026_07_16 as joint
import total_status_serial_reject_selector_cycle93_2026_07_15 as status


algebra = joint.mult.algebra
alu = joint.control.bound.spacious.alu
c53 = joint.c53
FRAME = joint.FRAME
H0 = status.H0
H1 = status.H1
Coord = tuple[int, int, int]
Row = tuple[int, int, int, int, int]
ROWS = tuple(product((0, 1), repeat=5))
MERGED_RAW = joint.tap.MERGED_RAW
START = (-1, 1, 0)
TARGETS = tuple((index, 1, 0) for index in range(5))
PORT = (5, 1, 0)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def bit(value: int) -> str:
    return H1 if value else H0


def place(records: dict[Coord, str], site: Coord, role: str) -> None:
    prior = records.get(site)
    if prior is not None and prior != role:
        raise ValueError(("placement-conflict", site, prior, role))
    records[site] = role


def lane_apparatus(candidate: Row, reference: Row):
    records: dict[Coord, str] = {START: H1}
    expected: dict[Coord, str] = {}
    dependencies: dict[Coord, frozenset[Coord]] = {}
    equal = True
    for index, (candidate_bit, reference_bit) in enumerate(
        zip(candidate, reference, strict=True)
    ):
        records[(index, 0, 0)] = bit(candidate_bit)
        records[(index, 2, 0)] = bit(reference_bit)
        records[(index, 1, 1)] = H0
        records[(index, 1, -1)] = H1
        equal = equal and candidate_bit == reference_bit
        target = TARGETS[index]
        expected[target] = H1 if equal else H0
        dependencies[target] = (
            frozenset()
            if index == 0
            else frozenset((TARGETS[index - 1],))
        )
    dynamic = set(expected) | {PORT}
    shell = {
        add(site, direction)
        for site in dynamic
        for direction in c53.DIRECTIONS
    }
    core = set(records) | dynamic | shell
    cage = {
        add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if add(site, direction) not in core
    }
    for site in cage:
        place(records, site, FRAME)
    for site in dynamic:
        records.pop(site, None)
    return records, expected, dependencies, equal


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def lane_run(candidate: Row, reference: Row, rotation=None):
    initial, expected, dependencies, equal = lane_apparatus(candidate, reference)
    if rotation is not None:
        shift = (127, -131, 137)

        def moved(site):
            return add(c53.matvec(rotation, site), shift)

        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
        dependencies = {
            moved(site): frozenset(moved(parent) for parent in parents)
            for site, parents in dependencies.items()
        }
    records = dict(initial)
    formed = set()
    actual = enabled(records)
    edges = 0
    maximum = 0
    while len(formed) < len(expected):
        frontier = {
            target: frozenset((expected[target],))
            for target, parents in dependencies.items()
            if target not in formed and parents <= formed
        }
        maximum = max(maximum, len(frontier))
        if actual != frontier:
            return False, (
                len(formed),
                actual,
                frontier,
                len(initial),
                len(expected),
                equal,
            )
        target = min(frontier)
        records[target] = expected[target]
        formed.add(target)
        edges += len(frontier)
        actual.pop(target, None)
        for direction in c53.DIRECTIONS:
            candidate_site = add(target, direction)
            if candidate_site in records:
                actual.pop(candidate_site, None)
                continue
            signature = c53.local_signature(records, candidate_site)
            if signature in MERGED_RAW:
                actual[candidate_site] = MERGED_RAW[signature]
            else:
                actual.pop(candidate_site, None)
    terminal = next(
        site for site in expected
        if not any(site in parents for parents in dependencies.values())
    )
    observed = records[terminal]
    return (
        not actual and observed == (H1 if equal else H0),
        (
            len(expected) + 1,
            edges,
            maximum,
            len(initial),
            len(expected),
            equal,
            observed,
            actual,
        ),
    )


def membership_bits(g1: Row, g2: Row, measured: Row):
    product_row = algebra.multiply_commuting(g1, g2)
    candidates = (g1, g2, product_row)
    equalities = tuple(int(measured == candidate) for candidate in candidates)
    return candidates, equalities, equalities[0] ^ equalities[1] ^ equalities[2]


def factorized_membership_run(g1: Row, g2: Row, measured: Row):
    candidates, equalities, supported = membership_bits(g1, g2, measured)
    lane_results = tuple(
        lane_run(measured, candidate)
        for candidate in candidates
    )
    xor_result = alu.run(
        equalities[0],
        ((0, equalities[1]), (0, equalities[2])),
    )
    return (
        all(ok for ok, _detail in lane_results)
        and xor_result[0]
        and xor_result[1][-1] == supported,
        (equalities, supported, lane_results, xor_result),
    )


def valid_ordered_bases():
    return tuple(
        basis
        for state_id in range(60)
        for basis in tableau.all_bases(state_id)
    )


def commuting_transcripts():
    for g1, g2 in valid_ordered_bases():
        product_row = algebra.multiply_commuting(g1, g2)
        for supported in (g1, g2, product_row):
            yield g1, g2, supported, True
            yield g1, g2, (*supported[:4], supported[4] ^ 1), False


def parent_deletion_failures():
    failures = []
    for signature, output in status.STATUS_TABLE.items():
        for index in range(len(signature)):
            shortened = signature[:index] + signature[index + 1:]
            if output in MERGED_RAW.get(shortened, frozenset()):
                failures.append(("status", signature, index, output))
    for signature, output in alu.CANONICAL_TABLE.items():
        for index in range(len(signature)):
            shortened = signature[:index] + signature[index + 1:]
            if output in MERGED_RAW.get(shortened, frozenset()):
                failures.append(("xor", signature, index, output))
    return tuple(failures)


def main() -> int:
    print(
        "LAW",
        len(MERGED_RAW),
        len(status.STATUS_TABLE),
        len(status.STATUS_RAW),
        len(alu.CANONICAL_TABLE),
        len(alu.ALU_RAW),
        len(set(status.STATUS_RAW) - set(MERGED_RAW)),
        len(set(alu.ALU_RAW) - set(MERGED_RAW)),
    )

    identity_failures = []
    identity_states = identity_edges = 0
    shapes = set()
    for candidate in ROWS:
        for reference in ROWS:
            ok, detail = lane_run(candidate, reference)
            if not ok:
                identity_failures.append((candidate, reference, detail))
            else:
                states, edges, maximum, initial, expected, equal, observed, _actual = detail
                identity_states += states
                identity_edges += edges
                shapes.add((states, edges, maximum, initial, expected, equal, observed))
    print(
        "LANES",
        len(ROWS) ** 2,
        identity_states,
        identity_edges,
        len(identity_failures),
        sorted(shapes),
    )

    rotation_failures = []
    rotation_states = 0
    representative_pairs = tuple(product(ROWS, repeat=2))
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for candidate, reference in representative_pairs:
            ok, detail = lane_run(candidate, reference, rotation)
            if not ok:
                rotation_failures.append((rotation_index, candidate, reference, detail))
            else:
                rotation_states += detail[0]
    print("ROTATIONS", rotation_states, len(rotation_failures))

    algebra_failures = []
    physical_failures = []
    accepts = rejects = 0
    match_counts = [0, 0, 0]
    transcripts = tuple(commuting_transcripts())
    for g1, g2, measured, should_accept in transcripts:
        candidates, equalities, supported = membership_bits(g1, g2, measured)
        if bool(supported) != should_accept:
            algebra_failures.append((g1, g2, measured, equalities, should_accept))
        if should_accept:
            accepts += 1
            match_counts[equalities.index(1)] += 1
        else:
            rejects += 1
        ok, detail = factorized_membership_run(g1, g2, measured)
        if not ok or bool(detail[1]) != should_accept:
            physical_failures.append((g1, g2, measured, should_accept, detail))
    print(
        "DOMAIN",
        len(valid_ordered_bases()),
        len(transcripts),
        accepts,
        rejects,
        tuple(match_counts),
        len(algebra_failures),
        len(physical_failures),
    )

    xor_rotation_failures = []
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for bits in product((0, 1), repeat=3):
            ok, detail = alu.run(
                bits[0],
                ((0, bits[1]), (0, bits[2])),
                rotation,
            )
            if not ok or detail[-1] != (bits[0] ^ bits[1] ^ bits[2]):
                xor_rotation_failures.append((rotation_index, bits, detail))
    deletion_failures = parent_deletion_failures()
    print("XOR_ROTATIONS", len(xor_rotation_failures))
    print("DELETIONS", len(deletion_failures))
    print(
        "ANCESTRY",
        "supplied-five-bit-literals",
        "host-product-enumeration",
        "factorized-xor-inputs",
    )

    result = (
        len(MERGED_RAW) == 97_388
        and not (set(status.STATUS_RAW) - set(MERGED_RAW))
        and not (set(alu.ALU_RAW) - set(MERGED_RAW))
        and identity_states == 6_144
        and identity_edges == 5_120
        and not identity_failures
        and rotation_states == 147_456
        and not rotation_failures
        and len(valid_ordered_bases()) == 360
        and len(transcripts) == 2_160
        and accepts == rejects == 1_080
        and tuple(match_counts) == (360, 360, 360)
        and not algebra_failures
        and not physical_failures
        and not xor_rotation_failures
        and not deletion_failures
    )
    if (
        identity_failures
        or rotation_failures
        or algebra_failures
        or physical_failures
        or xor_rotation_failures
        or deletion_failures
    ):
        print(
            "FAILURE_SAMPLE",
            (
                identity_failures[:2],
                rotation_failures[:2],
                algebra_failures[:2],
                physical_failures[:2],
                xor_rotation_failures[:2],
                deletion_failures[:2],
            ),
        )
    print(
        "RESULT",
        "FACTORIZED_COMMUTING_SIGNED_MEMBERSHIP" if result else "OPEN",
    )
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
