#!/usr/bin/env python3
"""Cycle 173: one shared signed observable in two Peres--Mermin contexts.

The frozen Cycle-169 signed-membership compiler is rebuilt with a ported
measured-row interface.  One physical signed ZI source forms one splitter and
two disjoint row branches.  Those branches feed independent R1 and C1
membership contexts.  Only the two transported physical membership outputs
feed the final AND terminal.

This is a finite shared-ancestry certificate for one repeated observable.  It
is not a six-context contextuality certificate, probability theorem, Born
rule, or axiom proposal.
"""

from __future__ import annotations

import ast
import hashlib
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import physical_row_native_signed_membership_cycle169_2026_07_16 as c169


Coord = tuple[int, int, int]
Row = tuple[int, int, int, int, int]
Spec = tuple[object, ...]

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "SHARED_ANCESTRY_DUAL_CONTEXT_PERES_MERMIN_CYCLE173_NOTE_2026-07-16.md"
)
CYCLE168_PRIMARY = (
    ROOT / "scripts/peres_mermin_factorized_reference_census_2026_07_16.py"
)
CYCLE168_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PERES_MERMIN_FACTORIZED_REFERENCE_CENSUS_CYCLE168_NOTE_2026-07-16.md"
)
CYCLE169_SCRIPT = (
    ROOT / "scripts/physical_row_native_signed_membership_cycle169_2026_07_16.py"
)
CYCLE169_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ROW_NATIVE_SIGNED_MEMBERSHIP_CYCLE169_NOTE_2026-07-16.md"
)

FROZEN_CYCLE169_SCRIPT_SHA = (
    "f56ee91380ab258dffad4ba7f97c951de4b11fa2413c6258f34aba1277588551"
)
FROZEN_CYCLE169_NOTE_SHA = (
    "a42eb415f6283a34314a97fd8a685ef714bb1c6a302ac622275e361291a26fe8"
)

EX = c169.EX
EY = c169.EY
EZ = c169.EZ
NEG_EX = c169.NEG_EX
NEG_EY = c169.NEG_EY
NEG_EZ = c169.NEG_EZ
FRAME = c169.FRAME
GUIDE = c169.GUIDE
H0 = c169.H0
H1 = c169.H1

ROW_SHIFT: Coord = (0, -4_000, 0)
COLUMN_SHIFT: Coord = (0, 4_000, 0)
SHARED_SPLITTER: Coord = (-3_000, 0, 0)
SHARED_SOURCE: Coord = c169.add(SHARED_SPLITTER, NEG_EX)
AND_TARGET: Coord = (2_000, 0, -2_000)
ROTATION_SHIFT: Coord = (7_001, -7_013, 7_021)

# Cycle-168 named rows:
# R1 = (+ZI,+IZ,+ZZ), C1 = (+ZI,+IX,+ZX).
ZI: Row = (0, 0, 1, 0, 0)
NEG_ZI: Row = (0, 0, 1, 0, 1)
IZ: Row = (0, 0, 0, 1, 0)
ZZ: Row = (0, 0, 1, 1, 0)
IX: Row = (0, 1, 0, 0, 0)
ZX: Row = (0, 1, 1, 0, 0)
NEG_ZX: Row = (0, 1, 1, 0, 1)

ROUTES = {
    "both_accept": ((IZ, ZZ), (IX, ZX), ZI, (1, 1, 1)),
    "both_reject": ((IZ, ZZ), (IX, ZX), NEG_ZI, (0, 0, 0)),
    "row_only": ((IZ, ZZ), (IX, NEG_ZX), ZI, (1, 0, 0)),
}

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


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add(left: Coord, right: Coord) -> Coord:
    return c169.add(left, right)


def sub(left: Coord, right: Coord) -> Coord:
    return c169.sub(left, right)


def scale(factor: int, vector: Coord) -> Coord:
    return c169.scale(factor, vector)


def shifted(site: Coord, delta: Coord) -> Coord:
    return add(site, delta)


def place(
    records: dict[Coord, str],
    site: Coord,
    role: str,
    label: str,
) -> None:
    previous = records.get(site)
    if previous is not None and previous != role:
        raise ValueError(("placement-conflict", label, site, previous, role))
    records[site] = role


def add_expected(
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
    site: Coord,
    role: str,
    parents: frozenset[Coord],
    label: str,
) -> None:
    previous = expected.get(site)
    if previous is not None and previous != role:
        raise ValueError(("expected-conflict", label, site, previous, role))
    previous_parents = dependencies.get(site)
    if previous_parents is not None and previous_parents != parents:
        raise ValueError(
            ("dependency-conflict", label, site, previous_parents, parents)
        )
    expected[site] = role
    dependencies[site] = parents


def path_through(start: Coord, waypoints: tuple[Coord, ...]) -> tuple[Coord, ...]:
    path = [start]
    for waypoint in waypoints:
        c169.line_to(path, waypoint)
    return tuple(path)


@dataclass(frozen=True)
class PortedPlan:
    fixed: dict[Coord, str]
    original_sources: dict[Coord, str]
    expected_specs: dict[Coord, Spec]
    dependencies: dict[Coord, frozenset[Coord]]
    path_groups: tuple[tuple[tuple[Spec, tuple[Coord, ...]], ...], ...]
    open_ports: frozenset[Coord]
    output_site: Coord
    p_input: Coord
    p_leaf_count: int
    compact_regression: tuple[bool, str]


@dataclass(frozen=True)
class ContextInstance:
    label: str
    initial: dict[Coord, str]
    expected: dict[Coord, str]
    dependencies: dict[Coord, frozenset[Coord]]
    output_site: Coord
    output_port: Coord
    p_input: Coord
    source_sites: dict[str, Coord]
    equalities: tuple[int, int, int]
    removable_cage: frozenset[Coord]


@dataclass(frozen=True)
class Apparatus:
    route: str
    initial: dict[Coord, str]
    expected: dict[Coord, str]
    dependencies: dict[Coord, frozenset[Coord]]
    row_output: Coord
    column_output: Coord
    terminal: Coord
    row_branch_first: Coord
    column_branch_first: Coord
    row_branch_guard: Coord
    column_branch_guard: Coord
    source_sites: dict[str, Coord]
    expected_bits: tuple[int, int, int]
    interface_sites: frozenset[Coord]


@lru_cache(maxsize=1)
def ported_plan() -> PortedPlan:
    """Cycle-169 membership with P entering through a 15-leaf row tree."""

    builder = c169.Builder()
    multiplier_shift = (0, -300, 0)
    product_tree = add(c169.cycle164.OUTPUT_PORT, multiplier_shift)

    sockets, final_sites = builder.comparator_sockets()

    g1_center = (-300, 200, -30)
    g2_center = (-300, -200, -30)
    p_tree = (-240, 0, 0)
    g1_tree = (-240, 200, 0)
    g2_tree = (-240, -200, 0)
    p_input = add(p_tree, NEG_EX)

    g1_direct = {
        index: (0, "reference", index)
        for index in range(4)
    }
    g2_direct = {
        index: (1, "reference", index)
        for index in range(4)
    }
    builder.reader(g1_center, "g1", g1_tree, g1_direct)
    builder.reader(g2_center, "g2", g2_tree, g2_direct)

    # Unlike Cycle 169's dense five-face P reader, every P literal is decoded
    # after the one external whole-row input.  This makes a real upstream
    # shared-source fork possible without occupying a reader face with cable
    # furniture.
    p_leaves = tuple(
        ("decode", index, (lane, "candidate", index))
        for lane in range(3)
        for index in range(5)
    )
    builder.comb_tree(p_tree, "p", p_leaves)

    left_source = add(c169.cycle164.LEFT_PATH[0], multiplier_shift)
    left_future = add(c169.cycle164.LEFT_PATH[1], multiplier_shift)
    right_source = add(c169.cycle164.RIGHT_PATH[0], multiplier_shift)
    right_future = add(c169.cycle164.RIGHT_PATH[1], multiplier_shift)
    builder.comb_tree(
        g1_tree,
        "g1",
        (
            ("decode", 4, (0, "reference", 4)),
            ("feed", left_source, left_future, (-700, -350, 300)),
        ),
    )
    builder.comb_tree(
        g2_tree,
        "g2",
        (
            ("decode", 4, (1, "reference", 4)),
            ("feed", right_source, right_future, (-240, -202, -60)),
        ),
    )

    builder.multiplier(multiplier_shift, product_tree)
    product_leaves = tuple(
        ("decode", index, (2, "reference", index))
        for index in range(5)
    )
    builder.comb_tree(product_tree, "prod", product_leaves)

    source_by_destination: dict[tuple[int, str, int], c169.BitSource] = {}
    for source in builder.bit_sources:
        previous = source_by_destination.get(source.destination)
        if previous is not None:
            raise ValueError(
                ("duplicate-bit-destination", source.destination, previous, source)
            )
        source_by_destination[source.destination] = source
    wanted_destinations = {
        (lane, side, index)
        for lane in range(3)
        for side in ("candidate", "reference")
        for index in range(5)
    }
    if set(source_by_destination) != wanted_destinations:
        raise ValueError(
            (
                "bit-destination-census",
                wanted_destinations - set(source_by_destination),
                set(source_by_destination) - wanted_destinations,
            )
        )

    for lane in range(3):
        for index in range(5):
            group: list[tuple[Spec, tuple[Coord, ...]]] = []
            for side in ("candidate", "reference"):
                destination = (lane, side, index)
                endpoint, target, penultimate = sockets[destination]
                source = source_by_destination[destination]
                builder.literal_path(
                    source,
                    endpoint,
                    target,
                    penultimate,
                    ordinal=2 * index + int(side == "reference"),
                    group=group,
                )
            status_item = builder.status_paths.get((lane, index))
            if status_item is not None:
                status_specification, status_path = status_item
                builder.path(status_specification, status_path, group=group)
            builder.path_groups.append(tuple(group))

    a_site = (0, 0, 0)
    b_site = (0, 0, -1)
    e_sites = ((0, 0, 1), (1, 0, 0), (0, -1, -1))
    for lane, (source, endpoint) in enumerate(
        zip(final_sites, e_sites, strict=True)
    ):
        if lane == 1:
            path_list = [source, add(source, NEG_EX), add(source, scale(-2, EX))]
            c169.line_to(path_list, (path_list[-1][0], path_list[-1][1], 50), (2,))
            c169.line_to(path_list, (path_list[-1][0], 0, 50), (1,))
            c169.line_to(path_list, (10, 0, 50), (0,))
            c169.line_to(path_list, (10, 0, 0), (2,))
            c169.line_to(path_list, (2, 0, 0), (0,))
            path_list.append(endpoint)
            path = tuple(path_list)
            direction = NEG_EX
        else:
            direction = tuple(
                0 if a == b else (1 if b > a else -1)
                for a, b in zip(source, endpoint)
            )
            if sum(abs(value) for value in direction) != 1:
                raise ValueError(
                    ("nonaxial-final-path", lane, source, endpoint)
                )
            distance = c169.manhattan(source, endpoint)
            path = tuple(
                add(source, scale(step, direction))
                for step in range(distance + 1)
            )
        consumer = a_site if lane < 2 else b_site
        if add(path[-1], direction) != consumer:
            raise ValueError(
                ("bad-final-status-port", lane, path[-1], consumer)
            )
        builder.path(c169.status_spec(lane, 4), path)

    builder.fixed_record((-1, 0, 0), c169.XOR_ROLE, "xor-a-op")
    builder.fixed_record((0, 1, 0), FRAME, "xor-a-frame")
    builder.fixed_record((0, -1, 0), FRAME, "xor-a-frame")
    builder.expected(
        a_site,
        c169.xor_spec(0),
        frozenset((e_sites[0], e_sites[1])),
    )
    builder.fixed_record((0, 1, -1), c169.XOR_ROLE, "xor-b-op")
    builder.fixed_record((-1, 0, -1), FRAME, "xor-b-frame")
    builder.fixed_record((1, 0, -1), FRAME, "xor-b-frame")
    builder.expected(
        b_site,
        c169.xor_spec(1),
        frozenset((a_site, e_sites[2])),
    )
    final_port = (0, 0, -2)
    builder.open_ports.add(final_port)

    return PortedPlan(
        fixed=dict(builder.fixed),
        original_sources=dict(builder.original_sources),
        expected_specs=dict(builder.expected_specs),
        dependencies=dict(builder.dependencies),
        path_groups=tuple(builder.path_groups),
        open_ports=frozenset(builder.open_ports),
        output_site=b_site,
        p_input=p_input,
        p_leaf_count=len(p_leaves),
        compact_regression=c169.compact_adjacent_regression(),
    )


@lru_cache(maxsize=1)
def ported_scaffold() -> tuple[
    dict[Coord, str],
    frozenset[Coord],
    frozenset[Coord],
]:
    plan = ported_plan()
    records = dict(plan.fixed)
    for site in plan.original_sources:
        place(records, site, c169.ZERO_ROLE, "dummy-original-source")

    dynamic = (
        set(plan.expected_specs)
        | set(plan.open_ports)
        | {plan.p_input}
    )
    protected = frozenset(dynamic | set(plan.original_sources))
    generated_ports: set[Coord] = set()
    for group_index, group in enumerate(plan.path_groups):
        items = tuple(
            (c169.dummy_role(spec), path)
            for spec, path in group
        )
        try:
            records, _outputs, ports = c169.greedy_path_core(
                items,
                constraints=records,
                extra_protected=protected,
            )
        except ValueError as error:
            raise ValueError(
                (
                    "ported-path-group-cage-failure",
                    group_index,
                    tuple(
                        (spec, path[0], path[-1], len(path))
                        for spec, path in group
                    ),
                    error.args,
                )
            ) from error
        generated_ports.update(ports)

    core_dynamic = dynamic
    shell = {
        add(site, direction)
        for site in core_dynamic
        for direction in c169.c53.DIRECTIONS
    }
    core = set(records) | core_dynamic | shell
    cage = {
        add(site, direction)
        for site in core
        for direction in c169.c53.DIRECTIONS
        if add(site, direction) not in core
    }
    added_cage = set()
    for site in cage:
        if site not in records:
            added_cage.add(site)
        place(records, site, FRAME, "ported-global-cage")

    for site in (
        set(plan.expected_specs)
        | set(plan.open_ports)
        | set(plan.original_sources)
        | {plan.p_input}
    ):
        records.pop(site, None)
    return records, frozenset(generated_ports), frozenset(added_cage)


def context_instance(
    label: str,
    generators: tuple[Row, Row],
    measured: Row,
    shift: Coord,
) -> ContextInstance:
    plan = ported_plan()
    scaffold, _ports, removable_cage = ported_scaffold()
    g1, g2 = generators
    context = c169.semantic_context(g1, g2, measured)
    rows, equalities, _prefixes, _xor_a, _xor_b = context

    initial = {
        shifted(site, shift): role
        for site, role in scaffold.items()
    }
    expected = {
        shifted(site, shift): c169.resolve_spec_role(spec, context)
        for site, spec in plan.expected_specs.items()
    }
    dependencies = {
        shifted(site, shift): frozenset(
            shifted(parent, shift)
            for parent in parents
        )
        for site, parents in plan.dependencies.items()
    }
    source_sites = {}
    for site, row_label in plan.original_sources.items():
        moved = shifted(site, shift)
        source_sites[f"{label}.{row_label}"] = moved
        place(
            initial,
            moved,
            c169.joint.pivot.five.ROW_ROLE[rows[row_label]],
            f"{label}-source",
        )
    for site in set(expected) | {
        shifted(site, shift) for site in plan.open_ports
    } | {shifted(plan.p_input, shift)}:
        initial.pop(site, None)

    return ContextInstance(
        label=label,
        initial=initial,
        expected=expected,
        dependencies=dependencies,
        output_site=shifted(plan.output_site, shift),
        output_port=shifted(next(iter(plan.open_ports)), shift),
        p_input=shifted(plan.p_input, shift),
        source_sites=source_sites,
        equalities=equalities,
        removable_cage=frozenset(
            shifted(site, shift) for site in removable_cage
        ),
    )


def branch_paths(
    row_p_input: Coord,
    column_p_input: Coord,
) -> tuple[tuple[Coord, ...], tuple[Coord, ...]]:
    row_first = add(SHARED_SPLITTER, NEG_EY)
    column_first = add(SHARED_SPLITTER, EY)
    row_path = path_through(
        SHARED_SPLITTER,
        (
            row_first,
            (-3_000, -10, 0),
            (-3_000, -10, -1_800),
            (-3_000, row_p_input[1], -1_800),
            (-900, row_p_input[1], -1_800),
            (-900, row_p_input[1], row_p_input[2]),
            (row_p_input[0] - 1, row_p_input[1], row_p_input[2]),
            row_p_input,
        ),
    )
    column_path = path_through(
        SHARED_SPLITTER,
        (
            column_first,
            (-3_000, 10, 0),
            (-3_000, 10, -2_200),
            (-3_000, column_p_input[1], -2_200),
            (-900, column_p_input[1], -2_200),
            (-900, column_p_input[1], column_p_input[2]),
            (
                column_p_input[0] - 1,
                column_p_input[1],
                column_p_input[2],
            ),
            column_p_input,
        ),
    )
    return row_path, column_path


def output_paths(
    row_output: Coord,
    row_port: Coord,
    column_output: Coord,
    column_port: Coord,
) -> tuple[tuple[Coord, ...], tuple[Coord, ...]]:
    left_endpoint = add(AND_TARGET, EZ)
    left_prior = add(left_endpoint, EZ)
    right_endpoint = add(AND_TARGET, NEG_EX)
    right_prior = add(right_endpoint, NEG_EX)
    row_path = path_through(
        row_output,
        (
            row_port,
            (row_port[0], row_port[1], -1_200),
            (1_000, row_port[1], -1_200),
            (1_000, 0, -1_200),
            (2_000, 0, -1_200),
            left_prior,
            left_endpoint,
        ),
    )
    column_path = path_through(
        column_output,
        (
            column_port,
            (column_port[0], column_port[1], -2_500),
            (1_000, column_port[1], -2_500),
            (1_000, 0, -2_500),
            (1_000, 0, -2_000),
            right_prior,
            right_endpoint,
        ),
    )
    return row_path, column_path


def add_path_expected(
    path: tuple[Coord, ...],
    role: str,
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
    label: str,
) -> None:
    for parent, child in zip(path, path[1:]):
        add_expected(
            expected,
            dependencies,
            child,
            role,
            frozenset((parent,)),
            label,
        )


def formation_records(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
    target: Coord,
) -> dict[Coord, str]:
    records = {
        neighbor: initial[neighbor]
        for direction in c169.c53.DIRECTIONS
        if (neighbor := add(target, direction)) in initial
    }
    records.update(
        {
            parent: expected[parent]
            for parent in dependencies[target]
            if parent in expected
        }
    )
    return records


def unique_fixed_guard(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
    target: Coord,
    excluded: frozenset[Coord],
) -> Coord:
    premise = formation_records(initial, expected, dependencies, target)
    candidates = tuple(
        site
        for site in premise
        if site in initial and site not in excluded
    )
    for site in candidates:
        shortened = dict(premise)
        shortened.pop(site)
        actual = c169.UNIFIED_RAW.get(
            c169.c53.local_signature(shortened, target),
            frozenset(),
        )
        if expected[target] not in actual:
            return site
    raise ValueError(("no-unique-fixed-guard", target, candidates))


@lru_cache(maxsize=None)
def apparatus(route: str) -> Apparatus:
    row_generators, column_generators, measured, expected_bits = ROUTES[route]
    row = context_instance("row", row_generators, measured, ROW_SHIFT)
    column = context_instance(
        "column",
        column_generators,
        measured,
        COLUMN_SHIFT,
    )

    initial: dict[Coord, str] = {}
    expected: dict[Coord, str] = {}
    dependencies: dict[Coord, frozenset[Coord]] = {}
    for context in (row, column):
        for site, role in context.initial.items():
            place(initial, site, role, f"{context.label}-initial")
        for site, role in context.expected.items():
            add_expected(
                expected,
                dependencies,
                site,
                role,
                context.dependencies[site],
                f"{context.label}-expected",
            )

    measured_role = c169.joint.pivot.five.ROW_ROLE[measured]
    place(initial, SHARED_SOURCE, measured_role, "shared-observable-source")
    place(initial, add(SHARED_SPLITTER, EZ), GUIDE, "shared-splitter-guide")
    place(initial, add(SHARED_SPLITTER, NEG_EZ), FRAME, "shared-splitter-frame")
    place(initial, add(SHARED_SPLITTER, EX), FRAME, "shared-splitter-frame")
    add_expected(
        expected,
        dependencies,
        SHARED_SPLITTER,
        measured_role,
        frozenset(),
        "shared-splitter",
    )

    row_branch, column_branch = branch_paths(row.p_input, column.p_input)
    row_status_path, column_status_path = output_paths(
        row.output_site,
        row.output_port,
        column.output_site,
        column.output_port,
    )
    interface_paths = (
        (measured_role, row_branch),
        (measured_role, column_branch),
        (c169.bit(expected_bits[0]), row_status_path),
        (c169.bit(expected_bits[1]), column_status_path),
    )

    # The inherited Cycle-169 global cage was built for a terminal source
    # boundary.  Open only cage records in the closed one-neighbor support of
    # the four new interface paths.  Functional reader, cable, comparator, and
    # multiplier furniture is not in removable_cage and therefore cannot be
    # silently carved.
    interface_closed = {
        neighbor
        for _role, path in interface_paths
        for site in path
        for neighbor in (site, *(add(site, d) for d in c169.c53.DIRECTIONS))
    }
    opened_cage = (
        (row.removable_cage | column.removable_cage)
        & interface_closed
    )
    for site in opened_cage:
        initial.pop(site, None)

    protected = frozenset(
        set(expected)
        | set(row.source_sites.values())
        | set(column.source_sites.values())
        | {SHARED_SOURCE}
        | {
            row.p_input,
            column.p_input,
            AND_TARGET,
            add(AND_TARGET, EZ),
            add(AND_TARGET, NEG_EX),
        }
    )
    base_initial_sites = set(initial)
    interface_records, _interface_expected, _ports = c169.greedy_path_core(
        interface_paths,
        constraints=initial,
        extra_protected=protected,
    )
    interface_dynamic = {
        site
        for _role, path in interface_paths
        for site in path
    } | {SHARED_SPLITTER, AND_TARGET}
    for site in interface_dynamic:
        interface_records.pop(site, None)

    for site, role in interface_records.items():
        place(initial, site, role, "interface-furniture")

    add_path_expected(
        row_branch,
        measured_role,
        expected,
        dependencies,
        "row-shared-branch",
    )
    add_path_expected(
        column_branch,
        measured_role,
        expected,
        dependencies,
        "column-shared-branch",
    )
    add_path_expected(
        row_status_path,
        c169.bit(expected_bits[0]),
        expected,
        dependencies,
        "row-context-output",
    )
    add_path_expected(
        column_status_path,
        c169.bit(expected_bits[1]),
        expected,
        dependencies,
        "column-context-output",
    )

    place(initial, add(AND_TARGET, EX), c169.joint.control.bound.spacious.alu.AND_ROLE, "and-op")
    place(initial, add(AND_TARGET, EY), FRAME, "and-frame")
    place(initial, add(AND_TARGET, NEG_EY), FRAME, "and-frame")
    add_expected(
        expected,
        dependencies,
        AND_TARGET,
        c169.bit(expected_bits[2]),
        frozenset((add(AND_TARGET, EZ), add(AND_TARGET, NEG_EX))),
        "and-terminal",
    )

    all_dynamic = set(expected)
    protected_closed = all_dynamic | {
        add(site, direction)
        for site in all_dynamic
        for direction in c169.c53.DIRECTIONS
    }
    new_interface_records = set(interface_records) - base_initial_sites
    external_record_sites = new_interface_records | {
        SHARED_SOURCE,
        add(SHARED_SPLITTER, EZ),
        add(SHARED_SPLITTER, NEG_EZ),
        add(SHARED_SPLITTER, EX),
        add(AND_TARGET, EX),
        add(AND_TARGET, EY),
        add(AND_TARGET, NEG_EY),
    }
    external_core = external_record_sites | interface_dynamic | {
        add(site, direction)
        for site in interface_dynamic
        for direction in c169.c53.DIRECTIONS
    }
    external_cage = {
        add(site, direction)
        for site in external_core
        for direction in c169.c53.DIRECTIONS
        if (
            add(site, direction) not in external_core
            and add(site, direction) not in protected_closed
        )
    }
    for site in external_cage:
        if site not in expected:
            place(initial, site, FRAME, "external-cage")

    for site in expected:
        initial.pop(site, None)

    source_sites = {
        "shared.p": SHARED_SOURCE,
        **row.source_sites,
        **column.source_sites,
    }
    row_first = row_branch[1]
    column_first = column_branch[1]
    row_guard = unique_fixed_guard(
        initial,
        expected,
        dependencies,
        row_first,
        frozenset((SHARED_SPLITTER,)),
    )
    column_guard = unique_fixed_guard(
        initial,
        expected,
        dependencies,
        column_first,
        frozenset((SHARED_SPLITTER,)),
    )

    return Apparatus(
        route=route,
        initial=initial,
        expected=expected,
        dependencies=dependencies,
        row_output=row.output_site,
        column_output=column.output_site,
        terminal=AND_TARGET,
        row_branch_first=row_first,
        column_branch_first=column_first,
        row_branch_guard=row_guard,
        column_branch_guard=column_guard,
        source_sites=source_sites,
        expected_bits=expected_bits,
        interface_sites=frozenset(interface_dynamic),
    )


def enabled(
    records: dict[Coord, str],
    law: dict[c169.c53.Signature, frozenset[str]] = c169.UNIFIED_RAW,
) -> dict[Coord, frozenset[str]]:
    return {
        target: law[signature]
        for target in c169.c53.open_candidates(records)
        if (signature := c169.c53.local_signature(records, target)) in law
    }


@lru_cache(maxsize=None)
def initial_enabled(route: str) -> dict[Coord, frozenset[str]]:
    instance = apparatus(route)
    if route == "both_accept":
        return enabled(instance.initial)

    base = apparatus("both_accept")
    actual = dict(initial_enabled("both_accept"))
    changed = {
        site
        for site in instance.initial
        if instance.initial[site] != base.initial[site]
    }
    if set(instance.initial) != set(base.initial):
        raise ValueError(("route-initial-domain-drift", route))
    affected = {
        add(site, direction)
        for site in changed
        for direction in c169.c53.DIRECTIONS
        if add(site, direction) not in instance.initial
    }
    for candidate in affected:
        signature = c169.c53.local_signature(instance.initial, candidate)
        values = c169.UNIFIED_RAW.get(signature)
        if values is None:
            actual.pop(candidate, None)
        else:
            actual[candidate] = values
    return actual


def children_map(
    dependencies: dict[Coord, frozenset[Coord]],
) -> dict[Coord, tuple[Coord, ...]]:
    children: dict[Coord, list[Coord]] = defaultdict(list)
    for child, parents in dependencies.items():
        for parent in parents:
            children[parent].append(child)
    return {
        parent: tuple(sorted(values))
        for parent, values in children.items()
    }


def descendants(
    dependencies: dict[Coord, frozenset[Coord]],
    starts: set[Coord],
) -> frozenset[Coord]:
    children = children_map(dependencies)
    seen = set(starts)
    queue = deque(starts)
    while queue:
        parent = queue.popleft()
        for child in children.get(parent, ()):
            if child not in seen:
                seen.add(child)
                queue.append(child)
    return frozenset(seen)


def ancestors(
    dependencies: dict[Coord, frozenset[Coord]],
    target: Coord,
) -> frozenset[Coord]:
    seen = set()
    queue = deque((target,))
    while queue:
        child = queue.popleft()
        for parent in dependencies[child]:
            if parent not in seen:
                seen.add(parent)
                queue.append(parent)
    return frozenset(seen)


def schedule(
    dependencies: dict[Coord, frozenset[Coord]],
    order: str,
) -> tuple[Coord, ...]:
    children = children_map(dependencies)
    pending = {
        site: len(parents)
        for site, parents in dependencies.items()
    }
    frontier = {
        site for site, count in pending.items() if count == 0
    }
    result = []
    while frontier:
        target = min(frontier) if order == "min" else max(frontier)
        frontier.remove(target)
        result.append(target)
        for child in children.get(target, ()):
            pending[child] -= 1
            if pending[child] == 0:
                frontier.add(child)
    if len(result) != len(dependencies):
        raise ValueError(("dependency-cycle", len(result), len(dependencies)))
    return tuple(result)


def local_compiled_check(
    instance: Apparatus,
    *,
    rotation=None,
) -> tuple[int, tuple[object, ...]]:
    if rotation is None:
        transform = lambda site: site
        initial = instance.initial
        expected = instance.expected
        dependencies = instance.dependencies
    else:
        transform = lambda site: add(
            c169.c53.matvec(rotation, site),
            ROTATION_SHIFT,
        )
        initial = {
            transform(site): role
            for site, role in instance.initial.items()
        }
        expected = {
            transform(site): role
            for site, role in instance.expected.items()
        }
        dependencies = {
            transform(site): frozenset(transform(parent) for parent in parents)
            for site, parents in instance.dependencies.items()
        }

    failures = []
    checks = 0
    for target, role in expected.items():
        premise = {
            neighbor: initial[neighbor]
            for direction in c169.c53.DIRECTIONS
            if (neighbor := add(target, direction)) in initial
        }
        premise.update(
            {
                parent: expected[parent]
                for parent in dependencies[target]
            }
        )
        signature = c169.c53.local_signature(premise, target)
        actual = c169.UNIFIED_RAW.get(signature, frozenset())
        checks += 1
        if actual != frozenset((role,)):
            failures.append((target, role, actual, dependencies[target]))
            if len(failures) >= 10:
                break
    return checks, tuple(failures)


def dynamic_edge_checks(instance: Apparatus) -> tuple[int, tuple[object, ...]]:
    failures = []
    attempts = 0
    for target, parents in instance.dependencies.items():
        premise = formation_records(
            instance.initial,
            instance.expected,
            instance.dependencies,
            target,
        )
        wanted = instance.expected[target]
        for parent in parents:
            attempts += 1
            trial = dict(premise)
            trial.pop(parent, None)
            actual = c169.UNIFIED_RAW.get(
                c169.c53.local_signature(trial, target),
                frozenset(),
            )
            if wanted in actual:
                failures.append((target, parent, wanted, actual))
                if len(failures) >= 10:
                    return attempts, tuple(failures)
    return attempts, tuple(failures)


def physical_run(
    instance: Apparatus,
    *,
    order: str,
    rotation=None,
) -> tuple[bool, object]:
    if rotation is None:
        initial = dict(instance.initial)
        expected = instance.expected
        dependencies = instance.dependencies
        terminal = instance.terminal
        seeded_actual = dict(initial_enabled(instance.route))
    else:
        def transform(site: Coord) -> Coord:
            return add(c169.c53.matvec(rotation, site), ROTATION_SHIFT)

        initial = {
            transform(site): role
            for site, role in instance.initial.items()
        }
        expected = {
            transform(site): role
            for site, role in instance.expected.items()
        }
        dependencies = {
            transform(site): frozenset(transform(parent) for parent in parents)
            for site, parents in instance.dependencies.items()
        }
        terminal = transform(instance.terminal)
        seeded_actual = {
            transform(site): values
            for site, values in initial_enabled(instance.route).items()
        }

    initial_count = len(initial)
    records = initial
    actual = seeded_actual
    linear = schedule(dependencies, order)
    formed: set[Coord] = set()
    maximum = 0
    work = 0
    children = children_map(dependencies)
    pending = {
        site: len(parents)
        for site, parents in dependencies.items()
    }
    frontier = {
        site for site, count in pending.items() if count == 0
    }
    for target in linear:
        wanted = {
            site: frozenset((expected[site],))
            for site in frontier
        }
        maximum = max(maximum, len(frontier))
        work += len(frontier)
        if actual != wanted:
            return False, (
                "frontier",
                len(formed),
                len(actual),
                len(wanted),
                tuple(sorted(set(actual) - set(wanted)))[:5],
                tuple(sorted(set(wanted) - set(actual)))[:5],
            )
        if target not in frontier:
            return False, ("schedule-frontier", target, len(formed))
        records[target] = expected[target]
        formed.add(target)
        frontier.remove(target)
        for child in children.get(target, ()):
            pending[child] -= 1
            if pending[child] == 0:
                frontier.add(child)
        actual.pop(target, None)
        for direction in c169.c53.DIRECTIONS:
            candidate = add(target, direction)
            if candidate in records:
                actual.pop(candidate, None)
                continue
            signature = c169.c53.local_signature(records, candidate)
            values = c169.UNIFIED_RAW.get(signature)
            if values is None:
                actual.pop(candidate, None)
            else:
                actual[candidate] = values

    return (
        not actual
        and records[terminal] == c169.bit(instance.expected_bits[2]),
        (
            initial_count,
            len(expected),
            work,
            maximum,
            records[terminal],
            tuple(sorted(actual.items())),
        ),
    )


def source_children(instance: Apparatus, source: Coord) -> tuple[Coord, ...]:
    children = []
    for direction in c169.c53.DIRECTIONS:
        target = add(source, direction)
        if target not in instance.expected:
            continue
        premise = formation_records(
            instance.initial,
            instance.expected,
            instance.dependencies,
            target,
        )
        if source in premise:
            children.append(target)
    return tuple(sorted(children))


def source_deletion_checks(
    instance: Apparatus,
) -> tuple[int, tuple[object, ...], dict[str, tuple[bool, bool, bool]]]:
    failures = []
    reach = {}
    attempts = 0
    for label, source in instance.source_sites.items():
        children = source_children(instance, source)
        if not children:
            failures.append((label, "no-source-child", source))
            continue
        killed = descendants(instance.dependencies, set(children))
        reach[label] = (
            instance.row_output in killed,
            instance.column_output in killed,
            instance.terminal in killed,
        )
        for child in children:
            premise = formation_records(
                instance.initial,
                instance.expected,
                instance.dependencies,
                child,
            )
            wanted = instance.expected[child]
            if source not in premise:
                failures.append((label, "source-not-in-premise", child))
                continue
            trial = dict(premise)
            del trial[source]
            actual = c169.UNIFIED_RAW.get(
                c169.c53.local_signature(trial, child),
                frozenset(),
            )
            attempts += 1
            if wanted in actual:
                failures.append((label, "survives", child, wanted, actual))
    return attempts, tuple(failures), reach


def pruned_physical_run(
    instance: Apparatus,
    *,
    removed_initial: Coord,
    cut: Coord,
    wanted_outputs: tuple[bool, bool, bool],
    full_rescan_control: bool = False,
) -> tuple[bool, object]:
    removed = descendants(instance.dependencies, {cut})
    expected = {
        site: role
        for site, role in instance.expected.items()
        if site not in removed
    }
    dependencies = {
        site: parents
        for site, parents in instance.dependencies.items()
        if site not in removed
    }
    if any(not parents <= expected.keys() for parents in dependencies.values()):
        return False, ("uncollapsed-descendant-cut", cut)
    initial = dict(instance.initial)
    initial.pop(removed_initial, None)

    records = initial
    # Removing one initial record can change enablement only at that now-open
    # site and at its six nearest neighbors.  Seed from the already exact full
    # initial frontier, then recompute precisely that complete affected set.
    # This is equivalent to a global open-candidate rescan but avoids repeating
    # a 3.6-million-record scan for every deletion control.
    actual = dict(initial_enabled(instance.route))
    affected = {removed_initial} | {
        add(removed_initial, direction)
        for direction in c169.c53.DIRECTIONS
    }
    for candidate in affected:
        if candidate in records or not any(
            add(candidate, direction) in records
            for direction in c169.c53.DIRECTIONS
        ):
            actual.pop(candidate, None)
            continue
        signature = c169.c53.local_signature(records, candidate)
        values = c169.UNIFIED_RAW.get(signature)
        if values is None:
            actual.pop(candidate, None)
        else:
            actual[candidate] = values
    rescan_equivalent = None
    if full_rescan_control:
        rescanned = enabled(records)
        rescan_equivalent = actual == rescanned
        if not rescan_equivalent:
            return False, (
                "local-reseed-mismatch",
                tuple(sorted(set(actual) - set(rescanned)))[:5],
                tuple(sorted(set(rescanned) - set(actual)))[:5],
            )
    linear = schedule(dependencies, "min")
    children = children_map(dependencies)
    pending = {
        site: len(parents)
        for site, parents in dependencies.items()
    }
    frontier = {
        site for site, count in pending.items() if count == 0
    }
    for step, target in enumerate(linear):
        wanted = {
            site: frozenset((expected[site],))
            for site in frontier
        }
        if actual != wanted:
            return False, (
                "frontier",
                step,
                tuple(sorted(set(actual) - set(wanted)))[:5],
                tuple(sorted(set(wanted) - set(actual)))[:5],
            )
        records[target] = expected[target]
        frontier.remove(target)
        for child in children.get(target, ()):
            pending[child] -= 1
            if pending[child] == 0:
                frontier.add(child)
        actual.pop(target, None)
        for direction in c169.c53.DIRECTIONS:
            candidate = add(target, direction)
            if candidate in records:
                actual.pop(candidate, None)
                continue
            signature = c169.c53.local_signature(records, candidate)
            values = c169.UNIFIED_RAW.get(signature)
            if values is None:
                actual.pop(candidate, None)
            else:
                actual[candidate] = values

    observed = (
        instance.row_output in records,
        instance.column_output in records,
        instance.terminal in records,
    )
    return (
        not actual and observed == wanted_outputs,
        {
            "removed": len(removed),
            "remaining": len(expected),
            "observed": observed,
            "rescan_equivalent": rescan_equivalent,
            "residual": tuple(sorted(actual.items())),
        },
    )


def cycle168_contexts() -> tuple[object, ...]:
    tree = ast.parse(CYCLE168_PRIMARY.read_text(encoding="utf-8"))
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == "PM_CONTEXTS"
                for target in node.targets
            )
        ):
            return ast.literal_eval(node.value)
    raise ValueError("PM_CONTEXTS not found")


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("FROZEN AUTHORITY AND CYCLE-168 REFERENCE")
    check(
        "Cycle-169 frozen script and note hashes match",
        sha256(CYCLE169_SCRIPT) == FROZEN_CYCLE169_SCRIPT_SHA
        and sha256(CYCLE169_NOTE) == FROZEN_CYCLE169_NOTE_SHA,
        (sha256(CYCLE169_SCRIPT), sha256(CYCLE169_NOTE)),
    )
    contexts = cycle168_contexts()
    context_rows = {
        label: tuple(
            c169.tableau.measurement_row(measurement_id, 1)
            for measurement_id in ids
        )
        for label, ids, _sign in contexts
    }
    check(
        "the selected shared source is literal +ZI in Cycle-168 R1 and C1",
        context_rows["R1"] == (ZI, IZ, ZZ)
        and context_rows["C1"] == (ZI, IX, ZX)
        and len(contexts) == 6,
        (context_rows["R1"], context_rows["C1"]),
    )
    cycle168_text = CYCLE168_NOTE.read_text(encoding="utf-8")
    check(
        "the exact Cycle-168 103,680 transcript census remains referenced",
        all(
            phrase in cycle168_text
            for phrase in (
                "attempts                                      103,680",
                "supported                                      38,880",
                "rejected                                       64,800",
                "terminal H1                                     38,880",
            )
        ),
    )

    print("\nPORTED MEMBERSHIP AND COMMON LAW")
    plan = ported_plan()
    scaffold, generated_ports, removable_cage = ported_scaffold()
    check(
        "the ported P interface has 15 physical decoder leaves and no P source",
        "p" not in set(plan.original_sources.values())
        and plan.p_leaf_count == 15
        and plan.p_input not in plan.expected_specs
        and plan.compact_regression[0],
        (
            plan.original_sources,
            plan.p_leaf_count,
        ),
    )
    check(
        "Cycle-169 membership and Cycle-166 unified laws remain conflict-free",
        len(c169.MEMBERSHIP_RAW) == 99_212
        and not c169.MEMBERSHIP_CONFLICTS
        and len(c169.UNIFIED_RAW) == 101_708
        and not c169.UNIFIED_CONFLICTS,
        (
            len(c169.MEMBERSHIP_RAW),
            len(c169.MEMBERSHIP_CONFLICTS),
            len(c169.UNIFIED_RAW),
            len(c169.UNIFIED_CONFLICTS),
            len(scaffold),
            len(generated_ports),
            len(removable_cage),
        ),
    )

    print("\nREPRESENTATIVE ROUTES AND LOCAL COMPILATION")
    instances = {route: apparatus(route) for route in ROUTES}
    route_failures = []
    route_shapes = {}
    for route, instance in instances.items():
        checks, failures = local_compiled_check(instance)
        route_shapes[route] = (
            len(instance.initial),
            len(instance.expected),
            sum(map(len, instance.dependencies.values())),
            checks,
        )
        row_bit = int(instance.expected[instance.row_output] == H1)
        column_bit = int(instance.expected[instance.column_output] == H1)
        terminal_bit = int(instance.expected[instance.terminal] == H1)
        if (
            failures
            or (row_bit, column_bit, terminal_bit) != instance.expected_bits
        ):
            route_failures.append(
                (
                    route,
                    failures[:2],
                    (row_bit, column_bit, terminal_bit),
                    instance.expected_bits,
                )
            )
    check(
        "both-accept, both-reject, and asymmetric routes compile exactly",
        not route_failures,
        {"shapes": route_shapes, "failures": route_failures},
    )
    shared_shapes = {
        (len(value.initial), len(value.expected))
        for value in instances.values()
    }
    check(
        "all three routes use one identical geometry and dependency graph",
        len(shared_shapes) == 1
        and all(
            value.dependencies == instances["both_accept"].dependencies
            for value in instances.values()
        ),
        shared_shapes,
    )

    print("\nFULL PHYSICAL REPRESENTATIVE REPLAYS")
    physical_results = {
        ("both_accept", "min"): physical_run(
            instances["both_accept"], order="min"
        ),
        ("both_reject", "max"): physical_run(
            instances["both_reject"], order="max"
        ),
        ("row_only", "min"): physical_run(
            instances["row_only"], order="min"
        ),
    }
    check(
        "all three representative routes close physically and terminally",
        all(result[0] for result in physical_results.values()),
        physical_results,
    )

    print("\nSHARED SOURCE, FORK, AND SOURCE DELETIONS")
    hard = instances["both_accept"]
    source_attempts, source_failures, source_reach = source_deletion_checks(hard)
    check(
        "all five supplied row sources are load-bearing at their first children",
        source_attempts > 0
        and not source_failures
        and set(source_reach) == set(hard.source_sites),
        (source_attempts, source_failures[:3], source_reach),
    )
    check(
        "shared ZI deletion reaches both contexts while context sources stay local",
        source_reach["shared.p"] == (True, True, True)
        and source_reach["row.g1"] == (True, False, True)
        and source_reach["row.g2"] == (True, False, True)
        and source_reach["column.g1"] == (False, True, True)
        and source_reach["column.g2"] == (False, True, True),
        source_reach,
    )
    row_killed = descendants(hard.dependencies, {hard.row_branch_first})
    column_killed = descendants(hard.dependencies, {hard.column_branch_first})
    check(
        "the two fork branches have disjoint context reach before the AND join",
        hard.row_output in row_killed
        and hard.column_output not in row_killed
        and hard.terminal in row_killed
        and hard.column_output in column_killed
        and hard.row_output not in column_killed
        and hard.terminal in column_killed,
        (
            len(row_killed),
            len(column_killed),
            len(row_killed & column_killed),
        ),
    )
    shared_pruned = pruned_physical_run(
        hard,
        removed_initial=SHARED_SOURCE,
        cut=SHARED_SPLITTER,
        wanted_outputs=(False, False, False),
        full_rescan_control=True,
    )
    row_pruned = pruned_physical_run(
        hard,
        removed_initial=hard.row_branch_guard,
        cut=hard.row_branch_first,
        wanted_outputs=(False, True, False),
    )
    column_pruned = pruned_physical_run(
        hard,
        removed_initial=hard.column_branch_guard,
        cut=hard.column_branch_first,
        wanted_outputs=(True, False, False),
    )
    check(
        "the radius-one source-deletion reseed equals a full global rescan",
        shared_pruned[0]
        and isinstance(shared_pruned[1], dict)
        and shared_pruned[1]["rescan_equivalent"] is True,
        shared_pruned,
    )
    check(
        "physical shared-source deletion kills both context outputs and AND",
        shared_pruned[0]
        and isinstance(shared_pruned[1], dict)
        and shared_pruned[1]["observed"] == (False, False, False),
        shared_pruned,
    )
    check(
        "physical fork deletions kill only their own context output and AND",
        row_pruned[0]
        and column_pruned[0]
        and isinstance(row_pruned[1], dict)
        and isinstance(column_pruned[1], dict)
        and row_pruned[1]["observed"] == (False, True, False)
        and column_pruned[1]["observed"] == (True, False, False),
        {
            "row": row_pruned,
            "column": column_pruned,
            "guards": (hard.row_branch_guard, hard.column_branch_guard),
        },
    )

    print("\nTERMINAL FIREWALL AND EDGE LOAD")
    terminal_parents = hard.dependencies[hard.terminal]
    internal_status_sites = {
        shifted(site, shift)
        for shift in (ROW_SHIFT, COLUMN_SHIFT)
        for site, spec in plan.expected_specs.items()
        if spec[0] in {"status", "xor"}
    }
    left_endpoint = add(AND_TARGET, EZ)
    right_endpoint = add(AND_TARGET, NEG_EX)
    left_ancestors = ancestors(hard.dependencies, left_endpoint)
    right_ancestors = ancestors(hard.dependencies, right_endpoint)
    check(
        "the final checker consumes only two transported context outputs",
        terminal_parents
        == frozenset((left_endpoint, right_endpoint))
        and not (terminal_parents & internal_status_sites)
        and hard.row_output in left_ancestors
        and hard.column_output not in left_ancestors
        and hard.column_output in right_ancestors
        and hard.row_output not in right_ancestors,
        {
            "parents": terminal_parents,
            "left_ancestors": len(left_ancestors),
            "right_ancestors": len(right_ancestors),
        },
    )
    edge_attempts, edge_failures = dynamic_edge_checks(hard)
    check(
        "every declared dynamic edge is load-bearing under the unified law",
        edge_attempts == sum(map(len, hard.dependencies.values()))
        and not edge_failures,
        (edge_attempts, edge_failures[:3]),
    )

    print("\nPROPER-CUBIC COVARIANCE")
    rotation_failures = []
    rotation_checks = 0
    base_sites = set(hard.initial) | set(hard.expected)
    for rotation_index, rotation in enumerate(c169.c53.ROTATIONS):
        transformed = {
            add(c169.c53.matvec(rotation, site), ROTATION_SHIFT)
            for site in base_sites
        }
        checks, failures = local_compiled_check(hard, rotation=rotation)
        rotation_checks += checks
        if len(transformed) != len(base_sites) or failures:
            rotation_failures.append(
                (rotation_index, len(transformed), failures[:2])
            )
    check(
        "all 24 proper-cubic labeled graphs compile by exact isomorphism",
        rotation_checks == 24 * len(hard.expected)
        and not rotation_failures,
        (rotation_checks, rotation_failures[:3]),
    )
    rotated_physical = tuple(
        (
            rotation_index,
            physical_run(
                hard,
                order="min",
                rotation=c169.c53.ROTATIONS[rotation_index],
            ),
        )
        for rotation_index in (1, 5)
    )
    check(
        "two nonidentity rotated hard presentations replay physically",
        all(result[0] for _index, result in rotated_physical),
        rotated_physical,
    )

    print("\nSCOPE")
    note_text = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    normalized = " ".join(note_text.lower().split())
    required_phrases = (
        "one repeated signed observable",
        "not a six-context shared-identity certificate",
        "not a physical contextuality certificate",
        "not a probability or born-rule result",
        "no axiom conclusion follows",
        "### n1",
        "### n2",
        "### n3",
        "### n4",
        "### n5",
        "### n6",
        "### n7",
        "### n8",
    )
    missing = tuple(
        phrase for phrase in required_phrases if phrase not in normalized
    )
    check(
        "the Cycle-173 note carries the exact shared-identity boundary",
        not missing,
        missing,
    )

    print("\nACCOUNTING")
    print("PORTED", len(plan.expected_specs), len(scaffold), len(generated_ports))
    print("ROUTES", route_shapes)
    print("PHYSICAL", physical_results)
    print("SOURCES", source_attempts, source_reach)
    print("EDGES", edge_attempts)
    print("ROTATION_CHECKS", rotation_checks)
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "SHARED_ANCESTRY_DUAL_CONTEXT_PERES_MERMIN_CYCLE173"
        if FAIL == 0
        else "CYCLE173_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
