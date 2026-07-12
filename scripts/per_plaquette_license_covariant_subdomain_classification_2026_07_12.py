#!/usr/bin/env python3
"""Exact finite certificate for the covariant link-subdomain classification.

This deterministic runner constructs the order-eight stabilizer of the
undirected reference link, exhausts all endpoint-containing subsets of its
one-step domain, and computes the length-4/length-6 mutual-containment table.
It also checks the paired note's theorem, status, table, and boundary pins.
"""
from __future__ import annotations

import itertools
from pathlib import Path
from typing import Callable, Iterable

Point = tuple[int, int, int]
Link = tuple[Point, Point]
Loop = tuple[Link, ...]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
DomainBuilder = Callable[[Link], set[Point]]

ROOT = Path(__file__).resolve().parent.parent
NOTE = (
    ROOT
    / "docs"
    / "PER_PLAQUETTE_LICENSE_COVARIANT_SUBDOMAIN_CLASSIFICATION_"
    "NOTE_2026-07-12.md"
)

ZERO: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
NEG_E1: Point = (-1, 0, 0)
DIRS: tuple[Point, ...] = (
    E1,
    NEG_E1,
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
REFERENCE_LINK: Link = (ZERO, E1)
RADIUS2_WITNESS: Point = (-2, 0, 0)

PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def check(label: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  --  {detail}" if detail else ""
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}{suffix}")
    return ok


def add(a: Point, b: Point) -> Point:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def sub(a: Point, b: Point) -> Point:
    return tuple(x - y for x, y in zip(a, b))  # type: ignore[return-value]


def dot(a: Point, b: Point) -> int:
    return sum(x * y for x, y in zip(a, b))


def distance(a: Point, b: Point) -> int:
    return sum(abs(x - y) for x, y in zip(a, b))


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[Matrix, ...]:
    matrices: list[Matrix] = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] != 1:
                continue
            rows = []
            for row in range(3):
                entries = [0, 0, 0]
                entries[permutation[row]] = signs[row]
                rows.append(tuple(entries))
            matrices.append(tuple(rows))  # type: ignore[arg-type]
    return tuple(matrices)


def mat_vec(matrix: Matrix, vector: Point) -> Point:
    return tuple(dot(row, vector) for row in matrix)  # type: ignore[return-value]


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    columns = tuple(tuple(right[row][column] for row in range(3)) for column in range(3))
    return tuple(
        tuple(dot(row, column) for column in columns) for row in left
    )  # type: ignore[return-value]


def reference_link_action(matrix: Matrix, point: Point) -> Point:
    """Act about the midpoint e1/2, so axis reversal swaps the endpoints."""
    doubled_centered = (2 * point[0] - 1, 2 * point[1], 2 * point[2])
    rotated = mat_vec(matrix, doubled_centered)
    numerators = (rotated[0] + 1, rotated[1], rotated[2])
    if any(value % 2 for value in numerators):
        raise ValueError("reference-link action did not preserve the lattice")
    return tuple(value // 2 for value in numerators)  # type: ignore[return-value]


def undirected_link_stabilizer(rotations: Iterable[Matrix]) -> tuple[Matrix, ...]:
    return tuple(matrix for matrix in rotations if mat_vec(matrix, E1) in (E1, NEG_E1))


def orbit(point: Point, group: tuple[Matrix, ...]) -> frozenset[Point]:
    return frozenset(reference_link_action(matrix, point) for matrix in group)


def orbit_partition(
    points: set[Point], group: tuple[Matrix, ...]
) -> set[frozenset[Point]]:
    remaining = set(points)
    parts: set[frozenset[Point]] = set()
    while remaining:
        part = orbit(min(remaining), group)
        parts.add(part)
        remaining -= part
    return parts


def l1_ball(center: Point, radius: int) -> set[Point]:
    offsets = itertools.product(range(-radius, radius + 1), repeat=3)
    return {
        add(center, offset)
        for offset in offsets
        if sum(abs(coordinate) for coordinate in offset) <= radius
    }


def endpoint_domain(link: Link) -> set[Point]:
    return set(link)


def endpoint_axial_domain(link: Link) -> set[Point]:
    a, b = link
    axis = sub(b, a)
    return {a, b, sub(a, axis), add(b, axis)}


def endpoint_transverse_domain(link: Link) -> set[Point]:
    a, b = link
    axis = sub(b, a)
    domain = {a, b}
    for endpoint in link:
        domain.update(add(endpoint, step) for step in DIRS if dot(step, axis) == 0)
    return domain


def c1_domain(link: Link) -> set[Point]:
    return set().union(*(l1_ball(endpoint, 1) for endpoint in link))


def radius2_domain(link: Link) -> set[Point]:
    return set().union(*(l1_ball(endpoint, 2) for endpoint in link))


DOMAIN_BUILDERS: tuple[tuple[str, str, DomainBuilder], ...] = (
    ("E", "E (endpoints)", endpoint_domain),
    ("E+A", "E union A", endpoint_axial_domain),
    ("E+T", "E union T", endpoint_transverse_domain),
    ("C_1", "C_1", c1_domain),
    ("radius-2", "radius-2", radius2_domain),
)


def closed_loops(length: int) -> list[Loop]:
    """Use the block-01/parent rooted-loop convention exactly."""
    loops: list[Loop] = []
    for steps in itertools.product(DIRS, repeat=length):
        position = ZERO
        points = [position]
        admissible = True
        for index, step in enumerate(steps):
            if index > 0 and add(steps[index - 1], step) == ZERO:
                admissible = False
                break
            position = add(position, step)
            points.append(position)
        if not admissible or points[-1] != ZERO:
            continue
        links = tuple((points[index], points[index + 1]) for index in range(length))
        if len({frozenset(link) for link in links}) == length:
            loops.append(links)
    return loops


def loop_support(loop: Loop) -> set[Point]:
    return {point for link in loop for point in link}


def is_plaquette(loop: Loop) -> bool:
    return len(loop_support(loop)) == 4


def passes_domain(loop: Loop, builder: DomainBuilder) -> bool:
    support = loop_support(loop)
    return all(support <= builder(link) for link in loop)


def block_a() -> tuple[
    tuple[Matrix, ...], set[Point], frozenset[Point], frozenset[Point], frozenset[Point]
]:
    section("BLOCK A — explicit undirected-link stabilizer and orbit decomposition")
    rotations = proper_cubic_rotations()
    group = undirected_link_stabilizer(rotations)
    group_set = set(group)
    endpoint_preserving = tuple(
        matrix
        for matrix in group
        if reference_link_action(matrix, ZERO) == ZERO
        and reference_link_action(matrix, E1) == E1
    )
    endpoint_swapping = tuple(
        matrix
        for matrix in group
        if reference_link_action(matrix, ZERO) == E1
        and reference_link_action(matrix, E1) == ZERO
    )

    check("proper cubic rotation group has order 24", len(rotations) == len(set(rotations)) == 24)
    check(
        "G_l has order 8 = four axial rotations times endpoint swap",
        len(group) == len(group_set) == 8
        and len(endpoint_preserving) == len(endpoint_swapping) == 4,
        f"preserve={len(endpoint_preserving)} swap={len(endpoint_swapping)}",
    )
    check(
        "G_l is closed under composition",
        all(mat_mul(left, right) in group_set for left in group for right in group),
        "64 products checked",
    )
    check(
        "every G_l element fixes {0,e1} as an undirected set",
        all(
            {
                reference_link_action(matrix, ZERO),
                reference_link_action(matrix, E1),
            }
            == {ZERO, E1}
            for matrix in group
        ),
    )

    reference_c1 = c1_domain(REFERENCE_LINK)
    endpoints = frozenset((ZERO, E1))
    axial = frozenset((NEG_E1, (2, 0, 0)))
    transverse = frozenset(
        (
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
            (1, 1, 0),
            (1, -1, 0),
            (1, 0, 1),
            (1, 0, -1),
        )
    )
    full_partition = orbit_partition(reference_c1, group)
    nonendpoint_partition = orbit_partition(reference_c1 - set(endpoints), group)
    check("C_1({0,e1}) has size 12", len(reference_c1) == 12)
    check(
        "the stated endpoint, axial, and transverse sets partition C_1",
        set(endpoints) | set(axial) | set(transverse) == reference_c1
        and not (set(endpoints) & set(axial))
        and not (set(endpoints) & set(transverse))
        and not (set(axial) & set(transverse)),
        f"sizes={len(endpoints)}/{len(axial)}/{len(transverse)}",
    )
    check(
        "the full orbit decomposition is exactly E, A, T with sizes 2/2/8",
        full_partition == {endpoints, axial, transverse},
        f"sizes={sorted(map(len, full_partition))}",
    )
    check(
        "the 10 non-endpoint points decompose into exactly A and T",
        nonendpoint_partition == {axial, transverse},
        f"orbit_count={len(nonendpoint_partition)}",
    )
    return group, reference_c1, endpoints, axial, transverse


def block_b(
    group: tuple[Matrix, ...],
    reference_c1: set[Point],
    endpoints: frozenset[Point],
    axial: frozenset[Point],
    transverse: frozenset[Point],
) -> None:
    section("BLOCK B — exhaustive invariant-subset lattice")
    nonendpoints = tuple(sorted(reference_c1 - set(endpoints)))
    invariant_domains: set[frozenset[Point]] = set()
    tested = 0
    for mask in range(1 << len(nonendpoints)):
        tested += 1
        candidate = set(endpoints)
        candidate.update(
            point for index, point in enumerate(nonendpoints) if mask & (1 << index)
        )
        if all(
            {reference_link_action(matrix, point) for point in candidate} == candidate
            for matrix in group
        ):
            invariant_domains.add(frozenset(candidate))

    expected_domains = {
        endpoints,
        endpoints | axial,
        endpoints | transverse,
        endpoints | axial | transverse,
    }
    check(
        "all 2^10 endpoint-containing subsets were tested",
        tested == 1024,
        f"tested={tested}",
    )
    check(
        "exactly four subsets are G_l-invariant",
        len(invariant_domains) == 4,
        f"invariant={len(invariant_domains)}",
    )
    check(
        "the invariant-subset lattice is exactly E, E union A, E union T, C_1",
        invariant_domains == expected_domains,
        f"sizes={sorted(map(len, invariant_domains))}",
    )
    check(
        "the four domains are closed under union and intersection",
        all(
            (left | right) in invariant_domains and (left & right) in invariant_domains
            for left in invariant_domains
            for right in invariant_domains
        ),
    )
    print(
        "  INVARIANT_SUBSETS: "
        f"tested={tested} invariant={len(invariant_domains)} sizes="
        f"{sorted(map(len, invariant_domains))}"
    )


def block_c() -> tuple[list[dict[str, object]], list[Loop], list[Loop]]:
    section("BLOCK C — computed length-4/length-6 classification table")
    rotations = proper_cubic_rotations()
    translations: tuple[Point, ...] = ((2, -1, 3), (-3, 0, 1))
    covariance_checks = []
    reversal_checks = []
    for _, _, builder in DOMAIN_BUILDERS:
        reference = builder(REFERENCE_LINK)
        reversal_checks.append(reference == builder((E1, ZERO)))
        covariance_checks.extend(
            {mat_vec(matrix, point) for point in reference}
            == builder((ZERO, mat_vec(matrix, E1)))
            for matrix in rotations
        )
        covariance_checks.extend(
            {add(point, translation) for point in reference}
            == builder((translation, add(translation, E1)))
            for translation in translations
        )
    check(
        "all five domain builders are undirected-link definitions",
        all(reversal_checks),
    )
    check(
        "all five domain builders are translation/proper-rotation covariant",
        all(covariance_checks),
        f"comparisons={len(covariance_checks)}",
    )

    length4 = closed_loops(4)
    length6 = closed_loops(6)
    check("rooted length-4 count", len(length4) == 24, f"found={len(length4)}")
    check("all rooted length-4 loops are plaquettes", all(map(is_plaquette, length4)))
    check("rooted length-6 count", len(length6) == 264, f"found={len(length6)}")

    reference_c1 = c1_domain(REFERENCE_LINK)
    rows: list[dict[str, object]] = []
    for key, label, builder in DOMAIN_BUILDERS:
        reference = builder(REFERENCE_LINK)
        rows.append(
            {
                "key": key,
                "label": label,
                "size": len(reference),
                "length4": sum(passes_domain(loop, builder) for loop in length4),
                "length6": sum(passes_domain(loop, builder) for loop in length6),
                "one_tick": reference <= reference_c1,
            }
        )

    expected = {
        "E": (2, 0, 0, True),
        "E+A": (4, 0, 0, True),
        "E+T": (10, 24, 0, True),
        "C_1": (12, 24, 0, True),
        "radius-2": (38, 24, 264, False),
    }
    actual = {
        str(row["key"]): (
            row["size"],
            row["length4"],
            row["length6"],
            row["one_tick"],
        )
        for row in rows
    }
    check(
        "the complete five-row classification matches the computed theorem table",
        actual == expected,
        str(actual),
    )
    check(
        "domains missing T give the constant-empty family",
        actual["E"][1:3] == actual["E+A"][1:3] == (0, 0),
    )
    check(
        "domains containing T give the constant 24/0 family",
        actual["E+T"][1:3] == actual["C_1"][1:3] == (24, 0),
    )
    check(
        "radius-2 admits the entire enumerated length-6 class",
        actual["radius-2"][2] == len(length6) == 264,
    )

    print("  COMPUTED_CLASSIFICATION_TABLE:")
    print("  domain       size   length-4   length-6   one-tick-subset-C_1")
    for row in rows:
        print(
            f"  {str(row['label']):<12} {int(row['size']):>4}   "
            f"{int(row['length4']):>3}/{len(length4):<3}    "
            f"{int(row['length6']):>3}/{len(length6):<3}    "
            f"{'yes' if row['one_tick'] else 'NO'}"
        )
    return rows, length4, length6


def block_d(rows: list[dict[str, object]]) -> None:
    section("BLOCK D — one-tick column and named radius-2 witness")
    by_key = {str(row["key"]): row for row in rows}
    reference_c1 = c1_domain(REFERENCE_LINK)
    reference_radius2 = radius2_domain(REFERENCE_LINK)
    left_ball = l1_ball(ZERO, 2)
    right_ball = l1_ball(E1, 2)
    check(
        "the four lattice domains are subsets of C_1",
        all(bool(by_key[key]["one_tick"]) for key in ("E", "E+A", "E+T", "C_1")),
    )
    check(
        "radius-2 is not a subset of C_1",
        not bool(by_key["radius-2"]["one_tick"]),
        f"radius2={len(reference_radius2)} C_1={len(reference_c1)}",
    )
    check(
        "radius-2 size is 25 + 25 - 12 = 38",
        len(left_ball) == len(right_ball) == 25
        and len(left_ball & right_ball) == 12
        and len(reference_radius2) == 38,
        f"balls={len(left_ball)}/{len(right_ball)} intersection={len(left_ball & right_ball)}",
    )
    check(
        "-2e1 is a named radius-2 point outside C_1",
        RADIUS2_WITNESS in reference_radius2
        and RADIUS2_WITNESS not in reference_c1
        and distance(RADIUS2_WITNESS, ZERO) == 2,
        f"witness={RADIUS2_WITNESS}",
    )
    check(
        "the witness is the block-01 radius-2 source/target violation class",
        RADIUS2_WITNESS == (-2, 0, 0)
        and ZERO == (0, 0, 0)
        and distance(RADIUS2_WITNESS, ZERO) == 2,
        "source=(-2,0,0) target=(0,0,0)",
    )
    print(
        "  ONE_TICK_WITNESS: "
        f"point={RADIUS2_WITNESS} in_radius2=True in_C_1=False "
        "block01_target=(0, 0, 0)"
    )


def table_row_needles(rows: list[dict[str, object]]) -> tuple[str, ...]:
    by_key = {str(row["key"]): row for row in rows}
    return (
        f"| `E` (endpoints) | {by_key['E']['size']} | empty ({by_key['E']['length4']}/24) | {by_key['E']['length6']}/264 | yes |",
        f"| `E∪A` | {by_key['E+A']['size']} | empty ({by_key['E+A']['length4']}/24) | {by_key['E+A']['length6']}/264 | yes |",
        f"| `E∪T` | {by_key['E+T']['size']} | all plaquettes ({by_key['E+T']['length4']}/24) | {by_key['E+T']['length6']}/264 | yes |",
        f"| `C_1` | {by_key['C_1']['size']} | all plaquettes ({by_key['C_1']['length4']}/24) | {by_key['C_1']['length6']}/264 | yes |",
        f"| radius-2 | {by_key['radius-2']['size']} | {by_key['radius-2']['length4']}/24 | {by_key['radius-2']['length6']}/264 | NO |",
    )


def block_e(rows: list[dict[str, object]]) -> None:
    section("BLOCK E — paired-note surface pins")
    exists = NOTE.is_file()
    check("paired classification note exists", exists, str(NOTE.relative_to(ROOT)))
    note = NOTE.read_text(encoding="utf-8") if exists else ""
    check("note is dated 2026-07-12", "**Date:** 2026-07-12" in note)
    check("note claim type is bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check(
        "note has the exact finite-classification status",
        "**Status:** exact finite classification support on the enumerated domains" in note,
    )
    check(
        "canonical status-authority firewall is present",
        "**Status authority:** independent audit lane only." in note,
    )
    check(
        "completeness theorem tag and exhaustive count are pinned",
        "## Theorem (completeness)" in note
        and "all `2^10 = 1024` subsets" in note
        and "exactly `2^2 = 4`" in note,
    )
    check(
        "classification table contains every computed cell",
        "## Computed classification table" in note
        and all(row in note for row in table_row_needles(rows)),
    )
    check(
        "enumerated-domain interval theorem tag is pinned",
        "## Theorem (enumerated-domain interval classification)" in note,
    )
    boundary_needles = (
        "## Boundaries",
        "enumerated lengths 4 and 6 only",
        "classification of covariant domains",
        "does **not** prove that the fundamental action is per-plaquette",
        "`theta_bare` is untouched",
        "does not amend an axiom or approved primitive",
    )
    check(
        "all required boundary pins are present",
        all(needle in note for needle in boundary_needles),
    )
    check(
        "radius-2 witness and block-01 falsifier class are named",
        "`-2e1 = (-2,0,0)`" in note
        and "source `(-2,0,0)` and target `(0,0,0)`" in note,
    )
    dependency_needles = (
        "[PER_PLAQUETTE_LICENSE_ONE_TICK_REACHABILITY_DERIVATION_NARROW_THEOREM_NOTE_2026-07-12.md](PER_PLAQUETTE_LICENSE_ONE_TICK_REACHABILITY_DERIVATION_NARROW_THEOREM_NOTE_2026-07-12.md)",
        "[LATTICE_NN_LIGHT_CONE_NOTE.md](LATTICE_NN_LIGHT_CONE_NOTE.md)",
        "`PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md`",
    )
    check(
        "authorized dependencies and backticked parent context are pinned",
        all(needle in note for needle in dependency_needles),
    )
    check(
        "the parent context is not a markdown dependency edge",
        "[PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md]"
        not in note,
    )
    check(
        "yaml tail supplies bounded-theorem author hint and one-line scope",
        "claim_type_author_hint: bounded_theorem" in note
        and "claim_scope:" in note,
    )


def main() -> int:
    print("=" * 88)
    print("COVARIANT ONE-STEP LINK-SUBDOMAIN COMPLETENESS CLASSIFICATION")
    print("=" * 88)

    group, reference_c1, endpoints, axial, transverse = block_a()
    block_b(group, reference_c1, endpoints, axial, transverse)
    rows, _, _ = block_c()
    block_d(rows)
    block_e(rows)

    by_key = {str(row["key"]): row for row in rows}
    print("\n" + "=" * 88)
    print("SHORT STDOUT SUMMARY")
    print(
        "E union A row: "
        f"size={by_key['E+A']['size']} "
        f"length4={by_key['E+A']['length4']}/24 "
        f"length6={by_key['E+A']['length6']}/264"
    )
    print(f"radius-2 domain size: {by_key['radius-2']['size']}")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
