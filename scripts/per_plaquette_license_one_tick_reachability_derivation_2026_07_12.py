#!/usr/bin/env python3
"""Exact finite certificate for the one-tick link-support derivation block.

The structural bridge remains conditional on the named
``(P-FUND-1TICK)`` packet.  This deterministic runner checks the definitional
reachability identity, its loop-enumeration consequences, the narrowly scoped
covariant-lift counterexample, an explicit locality falsifier, and the paired
note's status/boundary pins.
"""
from __future__ import annotations

import itertools
import re
from pathlib import Path
from typing import Callable, Iterable

Point = tuple[int, int, int]
Link = tuple[Point, Point]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

ROOT = Path(__file__).resolve().parent.parent
NOTE = (
    ROOT
    / "docs"
    / "PER_PLAQUETTE_LICENSE_ONE_TICK_REACHABILITY_DERIVATION_"
    "NARROW_THEOREM_NOTE_2026-07-12.md"
)

DIRS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
E1: Point = (1, 0, 0)
ZERO: Point = (0, 0, 0)

PASS = 0
FAIL = 0

R4_OUTCOME = "named open condition (not a registered premise node)"
R4_DECISIVE = (
    "The accepted sources supply spatial locality and a joint carrier, but "
    "no update law confines each fundamental multi-link term's carrier to "
    "that link's C_1 set."
)

PACKET = """(P-FUND-1TICK) Fundamental one-tick carrier-confinement packet (2026-07-12).
A fundamental multi-link admissibility term is one-tick confined at each
constituent link: the whole term presented at constituent l=(a,b) -- its
entire joint carrier, not merely its availability scalar -- reads only, and is
supported on, tick-t data on l's one-step dependency set C_1({a,b}); in
particular its carrier vertices(L) lie in C_1(l). This is the block's
load-bearing open condition. It is a named conditional packet on this note's
surface only, not an entry in axiom_premise_nodes.json and not a
chain-satisfying premise; the R4 closure attempt above did not derive it."""


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


def bounded_vertices(radius: int) -> set[Point]:
    coordinates = range(-radius, radius + 1)
    return set(itertools.product(coordinates, repeat=3))


def explicit_r_relation(vertices: set[Point]) -> set[tuple[Point, Point]]:
    """Construct R as self-edges plus directed NN edges, without distance."""
    relation: set[tuple[Point, Point]] = set()
    for source in vertices:
        relation.add((source, source))
        for step in DIRS:
            target = add(source, step)
            if target in vertices:
                relation.add((source, target))
    return relation


def c1_from_relation(
    sources: Iterable[Point], relation: set[tuple[Point, Point]]
) -> set[Point]:
    source_set = set(sources)
    return source_set | {
        target for source, target in relation if source in source_set
    }


def closed_loops(length: int) -> list[tuple[Link, ...]]:
    """Use the parent runner's rooted-loop conventions exactly."""
    loops: list[tuple[Link, ...]] = []
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
        interior = points[:-1]
        if len(set(interior)) != len(interior):
            # rooted SIMPLE loops (block-04 convention unification): vacuous
            # at the lengths 4/6 used here; load-bearing at length 8.
            continue
        links = tuple((points[index], points[index + 1]) for index in range(length))
        if len({frozenset(link) for link in links}) == length:
            loops.append(links)
    return loops


def loop_support(loop: tuple[Link, ...]) -> set[Point]:
    return {point for link in loop for point in link}


def derived_reachability_license(
    loop: tuple[Link, ...], relation: set[tuple[Point, Point]]
) -> bool:
    support = loop_support(loop)
    return all(support <= c1_from_relation(link, relation) for link in loop)


def literal_parent_license(loop: tuple[Link, ...]) -> bool:
    support = loop_support(loop)
    return all(
        all(min(distance(point, a), distance(point, b)) <= 1 for point in support)
        for a, b in loop
    )


def is_plaquette(loop: tuple[Link, ...]) -> bool:
    return len(loop_support(loop)) == 4


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
            determinant = permutation_sign(permutation) * signs[0] * signs[1] * signs[2]
            if determinant != 1:
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


def reference_link_action(matrix: Matrix, point: Point) -> Point:
    """Rotate about midpoint e1/2, allowing the undirected endpoint swap."""
    doubled_centered = (2 * point[0] - 1, 2 * point[1], 2 * point[2])
    rotated = mat_vec(matrix, doubled_centered)
    numerators = (rotated[0] + 1, rotated[1], rotated[2])
    if any(value % 2 for value in numerators):
        raise ValueError("reference-link stabilizer did not preserve the lattice")
    return tuple(value // 2 for value in numerators)  # type: ignore[return-value]


def stabilizer_orbits(
    points: set[Point], stabilizer: tuple[Matrix, ...]
) -> set[frozenset[Point]]:
    return {
        frozenset(reference_link_action(matrix, point) for matrix in stabilizer)
        for point in points
    }


def endpoint_transverse_domain(link: Link) -> set[Point]:
    """Endpoints plus the transverse orbit; omit the two axial exterior sites."""
    a, b = link
    axis = sub(b, a)
    domain = {a, b}
    for endpoint in link:
        domain.update(add(endpoint, step) for step in DIRS if dot(step, axis) == 0)
    return domain


def transverse_mutual_containment(loop: tuple[Link, ...]) -> bool:
    support = loop_support(loop)
    return all(support <= endpoint_transverse_domain(link) for link in loop)


def local_update(
    configuration: dict[Point, int],
    vertices: tuple[Point, ...],
    predecessors: dict[Point, tuple[Point, ...]],
    local_function: Callable[[tuple[int, ...]], int],
) -> dict[Point, int]:
    return {
        vertex: local_function(
            tuple(configuration[source] for source in predecessors[vertex])
        )
        for vertex in vertices
    }


def differing_sites(left: dict[Point, int], right: dict[Point, int]) -> set[Point]:
    return {vertex for vertex in left if left[vertex] != right[vertex]}


def block_a(
    vertices: set[Point], relation: set[tuple[Point, Point]]
) -> None:
    section("BLOCK A — Lemma A: explicit-R one-tick identity")
    exact_relation = all(
        ((source, target) in relation) == (distance(source, target) <= 1)
        for source in vertices
        for target in vertices
    )
    check(
        "explicit R contains exactly self plus NN edges in the bounded window",
        exact_relation,
        f"|V|={len(vertices)} |R|={len(relation)}",
    )

    bases: tuple[Point, ...] = ((-1, -1, -1), (0, 0, 0), (1, 1, 1))
    orientations: tuple[Point, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    for base in bases:
        for orientation in orientations:
            endpoint = add(base, orientation)
            computed = c1_from_relation((base, endpoint), relation)
            singleton_union = c1_from_relation((base,), relation) | c1_from_relation(
                (endpoint,), relation
            )
            distance_form = {
                point
                for point in vertices
                if min(distance(point, base), distance(point, endpoint)) <= 1
            }
            check(
                f"Lemma A at base={base}, orientation={orientation}",
                computed == singleton_union == distance_form,
                f"|C_1(link)|={len(computed)}",
            )

    assorted_sources: tuple[tuple[Point, ...], ...] = (
        (),
        (ZERO,),
        ((-1, 0, 0), (1, 0, 0)),
        ((0, -1, 1), (0, 0, 1), (0, 1, 1)),
        ((-1, -1, 0), (1, 1, 0), (0, 0, 1), (0, 0, -1)),
    )
    for index, sources in enumerate(assorted_sources, start=1):
        union = set().union(
            *(c1_from_relation((source,), relation) for source in sources)
        )
        check(
            f"union-additivity spot check {index}",
            c1_from_relation(sources, relation) == union,
            f"|S|={len(sources)}",
        )


def block_b(
    relation: set[tuple[Point, Point]],
) -> tuple[list[tuple[Link, ...]], list[tuple[Link, ...]]]:
    section("BLOCK B — loop consequences under the derived form")
    length4 = closed_loops(4)
    length6 = closed_loops(6)
    derived4 = [derived_reachability_license(loop, relation) for loop in length4]
    derived6 = [derived_reachability_license(loop, relation) for loop in length6]
    literal4 = [literal_parent_license(loop) for loop in length4]
    literal6 = [literal_parent_license(loop) for loop in length6]

    check("rooted length-4 count", len(length4) == 24, f"found={len(length4)}")
    check("all rooted length-4 loops are plaquettes", all(map(is_plaquette, length4)))
    check(
        "all length-4 loops pass the derived C_1 mutual-support form",
        sum(derived4) == 24,
        f"pass={sum(derived4)}/{len(length4)}",
    )
    check(
        "length-4 derived and literal predicates agree loop-by-loop",
        derived4 == literal4,
    )
    check("rooted length-6 count", len(length6) == 264, f"found={len(length6)}")
    check(
        "all length-6 loops fail the derived C_1 mutual-support form",
        sum(derived6) == 0,
        f"pass={sum(derived6)}/{len(length6)}",
    )
    check(
        "length-6 derived and literal predicates agree loop-by-loop",
        derived6 == literal6,
    )
    check(
        "combined derived/literal pass-fail vectors are identical",
        derived4 + derived6 == literal4 + literal6,
        f"vector_length={len(derived4) + len(derived6)}",
    )
    print(
        "  CONSEQUENCE_COUNTS: "
        f"length4={sum(derived4)}/{len(length4)} "
        f"length6={sum(derived6)}/{len(length6)}"
    )
    return length4, length6


def block_c(
    relation: set[tuple[Point, Point]],
    length4: list[tuple[Link, ...]],
    length6: list[tuple[Link, ...]],
) -> None:
    section("BLOCK C — narrowly scoped covariant-lift route pruning")
    rotations = proper_cubic_rotations()
    stabilizer = tuple(
        matrix for matrix in rotations if mat_vec(matrix, E1) in (E1, (-1, 0, 0))
    )
    reference_c1 = c1_from_relation((ZERO, E1), relation)
    endpoints = frozenset((ZERO, E1))
    axial = frozenset(((-1, 0, 0), (2, 0, 0)))
    transverse = frozenset(reference_c1 - endpoints - axial)
    expected_orbits = {endpoints, axial, transverse}
    actual_orbits = stabilizer_orbits(reference_c1, stabilizer)
    endpoint_preserving = sum(mat_vec(matrix, E1) == E1 for matrix in stabilizer)
    endpoint_swapping = sum(mat_vec(matrix, E1) == (-1, 0, 0) for matrix in stabilizer)

    check("proper cubic rotation group has order 24", len(rotations) == 24)
    check(
        "undirected reference-link stabilizer has order 8",
        len(stabilizer) == 8 and endpoint_preserving == endpoint_swapping == 4,
        f"preserve={endpoint_preserving} swap={endpoint_swapping}",
    )
    check(
        "all stabilizer elements preserve C_1({0,e1})",
        all(
            {reference_link_action(matrix, point) for point in reference_c1}
            == reference_c1
            for matrix in stabilizer
        ),
    )
    check(
        "stabilizer orbits are endpoints, axial, and transverse",
        actual_orbits == expected_orbits,
        f"sizes={sorted(map(len, actual_orbits))}",
    )

    smaller_domain = set(endpoints | transverse)
    check(
        "endpoint-plus-transverse domain is a strict covariant subdomain",
        smaller_domain < reference_c1
        and endpoint_transverse_domain((ZERO, E1)) == smaller_domain
        and all(
            {reference_link_action(matrix, point) for point in smaller_domain}
            == smaller_domain
            for matrix in stabilizer
        ),
        f"smaller={len(smaller_domain)} full={len(reference_c1)}",
    )
    transverse4 = [transverse_mutual_containment(loop) for loop in length4]
    transverse6 = [transverse_mutual_containment(loop) for loop in length6]
    check(
        "strict transverse-only lift passes all plaquettes under mutual containment",
        sum(transverse4) == 24,
        f"pass={sum(transverse4)}/{len(length4)}",
    )
    check(
        "minimal-nonempty covariant-lift selector is falsified",
        smaller_domain < reference_c1 and all(transverse4),
        "full C_1 is not selected uniquely by plaquette passage",
    )
    check(
        "transverse-only length-6 behavior is reported",
        sum(transverse6) == 0,
        f"pass={sum(transverse6)}/{len(length6)}",
    )
    print(
        "  BLOCK_C_WITNESS: "
        f"group={len(stabilizer)} orbits=endpoints:{len(endpoints)},"
        f"axial:{len(axial)},transverse:{len(transverse)} "
        f"domain={len(smaller_domain)}/{len(reference_c1)} "
        f"plaquettes={sum(transverse4)}/{len(length4)} "
        f"length6={sum(transverse6)}/{len(length6)}"
    )


def block_d() -> None:
    section("BLOCK D — R-locality falsifier")
    vertices = tuple((coordinate, 0, 0) for coordinate in range(-2, 3))
    vertex_set = set(vertices)
    relation = explicit_r_relation(vertex_set)
    predecessors = {
        vertex: tuple(sorted(source for source, target in relation if target == vertex))
        for vertex in vertices
    }
    check(
        "tiny path R is exactly self plus embedded nearest-neighbor edges",
        all(
            ((source, target) in relation) == (distance(source, target) <= 1)
            for source in vertices
            for target in vertices
        ),
        f"|V|={len(vertices)} |R|={len(relation)}",
    )

    configurations = [
        dict(zip(vertices, bits))
        for bits in itertools.product((0, 1), repeat=len(vertices))
    ]
    local_functions: tuple[tuple[str, Callable[[tuple[int, ...]], int]], ...] = (
        ("OR", lambda values: int(any(values))),
        ("parity", lambda values: sum(values) % 2),
        ("majority", lambda values: int(2 * sum(values) >= len(values))),
    )
    for name, local_function in local_functions:
        violation: tuple[set[Point], set[Point]] | None = None
        for left in configurations:
            left_next = local_update(left, vertices, predecessors, local_function)
            for right in configurations:
                sources = differing_sites(left, right)
                right_next = local_update(right, vertices, predecessors, local_function)
                differences = differing_sites(left_next, right_next)
                if not differences <= c1_from_relation(sources, relation):
                    violation = (sources, differences)
                    break
            if violation is not None:
                break
        check(
            f"C_1-bounded {name} updates respect one-tick confinement exhaustively",
            violation is None,
            f"configuration_pairs={len(configurations) ** 2}",
        )

    source = (-2, 0, 0)
    target = (0, 0, 0)
    left = {vertex: 0 for vertex in vertices}
    right = dict(left)
    right[source] = 1
    local_left = local_update(left, vertices, predecessors, local_functions[1][1])
    local_right = local_update(right, vertices, predecessors, local_functions[1][1])
    local_differences = differing_sites(local_left, local_right)

    def bad_update(configuration: dict[Point, int]) -> dict[Point, int]:
        output = local_update(configuration, vertices, predecessors, local_functions[1][1])
        output[target] = configuration[source]
        return output

    bad_differences = differing_sites(bad_update(left), bad_update(right))
    allowed = c1_from_relation((source,), relation)
    check(
        "counterexample dependency is at graph radius 2 and outside target's R inputs",
        distance(source, target) == 2 and source not in predecessors[target],
    )
    check(
        "C_1-bounded comparison pair stays inside C_1(source)",
        local_differences <= allowed and target not in local_differences,
        f"differences={sorted(local_differences)}",
    )
    check(
        "radius-2 availability changes at the forbidden target after one tick",
        target in bad_differences,
        f"differences={sorted(bad_differences)}",
    )
    check(
        "radius-2 dependency violates one-tick difference confinement",
        not bad_differences <= allowed,
        f"C_1(source)={sorted(allowed)}",
    )
    print(
        "  COUNTEREXAMPLE: "
        f"source={source} target={target} distance={distance(source, target)} "
        f"C_1(source)={sorted(allowed)} bad_differences={sorted(bad_differences)}"
    )


def block_e() -> None:
    section("BLOCK E — note-surface pins")
    exists = NOTE.is_file()
    check("paired theorem note exists", exists, str(NOTE.relative_to(ROOT)))
    note = NOTE.read_text(encoding="utf-8") if exists else ""
    check("note is dated 2026-07-12", "**Date:** 2026-07-12" in note)
    check("note claim type is bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check(
        "conditional status line names the packet",
        "**Status:** bounded theorem conditional on the named `(P-FUND-1TICK)` packet"
        in note,
    )
    check(
        "Lemma A, Lemma B, and Corollary C tags are pinned",
        all(
            tag in note
            for tag in (
                "### Lemma A (definitional identity)",
                "### Lemma B (bridge; conditional closure status)",
                "### Corollary C (the license, derived conditionally)",
            )
        ),
    )
    check(
        "named P-FUND-1TICK packet is fenced verbatim",
        f"```text\n{PACKET}\n```" in note,
    )
    boundary_needles = (
        "## Boundaries",
        "does **not** prove that the fundamental action is per-plaquette",
        "length-4 and length-6 enumeration domains are inherited",
        "does not amend the framework axioms or approved primitives",
        "`theta_bare` is untouched",
        "The parent note is not modified in this block",
    )
    check(
        "all required boundary pins are present",
        all(needle in note for needle in boundary_needles),
    )
    dependency_needles = (
        "[LATTICE_NN_LIGHT_CONE_NOTE.md](LATTICE_NN_LIGHT_CONE_NOTE.md)",
        "[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md)",
        "[QUBIT_LATTICE_JOINT_PRESENTATION_TENSOR_SUBSTRATE_BRIDGE_NOTE_2026-07-09.md]",
        "`PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md`",
        "`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` is context only",
    )
    check(
        "authorized dependencies and context-only surfaces are pinned",
        all(needle in note for needle in dependency_needles),
    )
    check(
        "parent context is not a markdown dependency link",
        "[PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md]"
        not in note,
    )
    check(
        "R4 nonclosure and decisive residual are explicit",
        re.search(r"The R4 closure\s+attempt therefore does not certify", note)
        is not None
        and re.search(
            r"no\s+statement makes a fundamental multi-link availability", note
        )
        is not None,
    )
    check(
        "yaml tail supplies bounded-theorem author hint and one-line scope",
        "claim_type_author_hint: bounded_theorem" in note
        and re.search(r'^claim_scope: "[^\n]+"$', note, flags=re.MULTILINE) is not None,
    )
    check(
        "note avoids bare retained/promoted status vocabulary",
        re.search(r"\b(retained|promoted)\b", note, flags=re.IGNORECASE) is None,
    )


def main() -> int:
    print("=" * 88)
    print("ONE-TICK REACHABILITY DERIVATION OF THE UNIT-NEIGHBORHOOD LINK LICENSE")
    print("=" * 88)
    print(f"R4 OUTCOME: {R4_OUTCOME}")
    print(f"DECISIVE: {R4_DECISIVE}")

    vertices = bounded_vertices(3)
    relation = explicit_r_relation(vertices)
    block_a(vertices, relation)
    length4, length6 = block_b(relation)
    block_c(relation, length4, length6)
    block_d()
    block_e()

    print("\n" + "=" * 88)
    print("SHORT STDOUT SUMMARY")
    print(f"R4 closure outcome: {R4_OUTCOME}")
    print(f"Decisive sentence: {R4_DECISIVE}")
    print("Block C witness counts: group=8, orbits=2/2/8, domain=10/12, plaquettes=24/24, length6=0/264")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
