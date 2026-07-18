#!/usr/bin/env python3
"""Cycle 179: five spatial H0/H1 formations feed signed membership.

The measured signed row is never materialized as one 32-valued onsite role.
Instead, ten matching physical witnesses form five separated H0/H1 records.
Each formed bit drives one physical three-branch cable tree whose leaves feed
the existing three candidate sides of the five-literal membership
comparators.

This is a finite record-law orthogonalization of Cycle 176.  It is not yet a
qubit code theorem, tensor-product theorem, instrument theorem, occurrence
law, probability result, or axiom proposal.
"""

from __future__ import annotations

import hashlib
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import lru_cache
from itertools import product
from pathlib import Path

import physical_bare_formation_ported_readout_cycle176_2026_07_16 as c176
import physical_row_native_signed_membership_cycle169_2026_07_16 as c169


Coord = tuple[int, int, int]
Row = tuple[int, int, int, int, int]
Spec = tuple[object, ...]

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FIVE_LANE_FORMATION_MEMBERSHIP_CYCLE179_NOTE_2026-07-16.md"
)
CYCLE169_SCRIPT = (
    ROOT / "scripts/physical_row_native_signed_membership_cycle169_2026_07_16.py"
)
CYCLE169_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ROW_NATIVE_SIGNED_MEMBERSHIP_CYCLE169_NOTE_2026-07-16.md"
)
CYCLE176_SCRIPT = (
    ROOT / "scripts/physical_bare_formation_ported_readout_cycle176_2026_07_16.py"
)
CYCLE176_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_BARE_FORMATION_PORTED_READOUT_CYCLE176_NOTE_2026-07-16.md"
)

FROZEN_CYCLE169_SCRIPT_SHA = (
    "f56ee91380ab258dffad4ba7f97c951de4b11fa2413c6258f34aba1277588551"
)
FROZEN_CYCLE169_NOTE_SHA = (
    "a42eb415f6283a34314a97fd8a685ef714bb1c6a302ac622275e361291a26fe8"
)
FROZEN_CYCLE176_SCRIPT_SHA = (
    "2a89f7667c4363f9d14d6ff1a2780f1f644aea225405321d24d8debab428b514"
)
FROZEN_CYCLE176_NOTE_SHA = (
    "ecbff770eb9f40f3518798e34cf87e34a22bc0c45b8dfc49e32793d769a54042"
)

ORIGIN: Coord = (0, 0, 0)
EX: Coord = c169.EX
EY: Coord = c169.EY
EZ: Coord = c169.EZ
NEG_EX: Coord = c169.NEG_EX
NEG_EY: Coord = c169.NEG_EY
NEG_EZ: Coord = c169.NEG_EZ
FRAME = c169.FRAME
GUIDE = c169.GUIDE
H0 = c169.H0
H1 = c169.H1
AND_ROLE = c169.joint.control.bound.spacious.alu.AND_ROLE

ZI: Row = (0, 0, 1, 0, 0)
NEG_ZI: Row = (0, 0, 1, 0, 1)
IZ: Row = (0, 0, 0, 1, 0)
ZZ: Row = (0, 0, 1, 1, 0)

SOURCE_X = -1_400
SOURCE_Y0 = -2_400
SOURCE_Y_STEP = -420
ROUTE_Z0 = -3_200
ROUTE_Z_BIT_STEP = -360
ROUTE_Z_BRANCH_STEP = -70
ROTATION_SHIFT: Coord = (10_007, -10_009, 10_037)

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


def scale(factor: int, vector: Coord) -> Coord:
    return c169.scale(factor, vector)


def opposite_bit_signature(role: str):
    return c169.c53.canonical_signature(
        c169.c53.local_signature(
            {EZ: role, NEG_EZ: role},
            ORIGIN,
        )
    )


BINARY_INGRESS_TABLE = {
    opposite_bit_signature(role): role
    for role in (H0, H1)
}
BINARY_INGRESS_RAW = c169.cell.merge_raw(*(
    c169.cell.raw_orbit(signature, output)
    for signature, output in BINARY_INGRESS_TABLE.items()
))
MERGED_RAW = c169.cell.merge_raw(c169.UNIFIED_RAW, BINARY_INGRESS_RAW)
RAW_CONFLICTS = {
    signature: outputs
    for signature, outputs in MERGED_RAW.items()
    if len(outputs) != 1
}


def source_site(index: int) -> Coord:
    return (SOURCE_X, SOURCE_Y0 + SOURCE_Y_STEP * index, 0)


def candidate_leaf(lane: int, index: int) -> tuple[Coord, Coord]:
    ordinal = 5 * lane + index
    if ordinal < 14:
        splitter = (-240 + 16 * ordinal, 0, 0)
        return add(splitter, scale(11, EY)), EY
    splitter = (-240 + 16 * 13, 0, 0)
    return add(splitter, scale(11, NEG_EY)), NEG_EY


def path_to_leaf(
    source: Coord,
    branch: int,
    leaf: Coord,
    direction: Coord,
    index: int,
) -> tuple[Coord, ...]:
    first_directions = (EX, EY, NEG_EY)
    first = first_directions[branch]
    path = [
        source,
        add(source, first),
        add(source, scale(2, first)),
    ]
    layer = ROUTE_Z0 + ROUTE_Z_BIT_STEP * index + ROUTE_Z_BRANCH_STEP * branch
    c169.line_to(path, (path[-1][0], path[-1][1], layer), (2,))
    staging = add(leaf, scale(-2, direction))
    ordinal = 3 * index + branch
    portal_x = -1_800 - 40 * ordinal
    if branch == 2 and index == 3:
        near_x = staging[0] - 20
    elif branch == 2 and index == 4:
        near_x = staging[0] + 20
    else:
        near_x = staging[0] - 1
    near_y = (
        staging[1] - 2 - 4 * ordinal
        if direction == EY
        else staging[1] + 2 + 4 * ordinal
    )
    portal_y = near_y + (-1 if direction == EY else 1)
    approach_z = -10 - 4 * ordinal
    c169.line_to(path, (path[-1][0], portal_y, layer), (1,))
    c169.line_to(path, (portal_x, portal_y, layer), (0,))
    c169.line_to(path, (portal_x, portal_y, approach_z), (2,))
    c169.line_to(path, (portal_x, near_y, approach_z), (1,))
    c169.line_to(path, (near_x, near_y, approach_z), (0,))
    c169.line_to(path, (near_x, staging[1], approach_z), (1,))
    c169.line_to(path, (staging[0], staging[1], approach_z), (0,))
    c169.line_to(path, staging, (2,))
    penultimate = add(leaf, scale(-1, direction))
    if c169.manhattan(path[-1], penultimate) != 1:
        raise ValueError(
            ("bad-candidate-leaf-preterminal", index, branch, path[-1], penultimate)
        )
    path.append(penultimate)
    if c169.manhattan(path[-1], leaf) != 1:
        raise ValueError(("bad-candidate-leaf-terminal", index, branch, path[-1], leaf))
    path.append(leaf)
    if c169.cable.terminal_direction(tuple(path)) != direction:
        raise ValueError(
            (
                "wrong-candidate-leaf-direction",
                index,
                branch,
                c169.cable.terminal_direction(tuple(path)),
                direction,
            )
        )
    return tuple(path)


@dataclass(frozen=True)
class FiveLanePlan:
    fixed: dict[Coord, str]
    original_sources: dict[Coord, str]
    expected_specs: dict[Coord, Spec]
    dependencies: dict[Coord, frozenset[Coord]]
    path_groups: tuple[tuple[tuple[Spec, tuple[Coord, ...]], ...], ...]
    open_ports: frozenset[Coord]
    output_site: Coord
    bit_sources: tuple[Coord, ...]
    witnesses: tuple[tuple[Coord, Coord], ...]
    leaves: tuple[tuple[Coord, ...], ...]
    payload_first: Coord


@lru_cache(maxsize=1)
def five_lane_plan() -> FiveLanePlan:
    builder = c169.Builder()
    multiplier_shift = (0, -300, 0)
    product_tree = add(c169.cycle164.OUTPUT_PORT, multiplier_shift)
    sockets, final_sites = builder.comparator_sockets()

    g1_center = (-300, 200, -30)
    g2_center = (-300, -200, -30)
    g1_tree = (-240, 200, 0)
    g2_tree = (-240, -200, 0)
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
    builder.comb_tree(
        product_tree,
        "prod",
        tuple(
            ("decode", index, (2, "reference", index))
            for index in range(5)
        ),
    )

    candidate_sources: dict[
        tuple[int, str, int],
        c169.BitSource,
    ] = {}
    source_sites = []
    witness_sites = []
    all_leaves = []
    for index in range(5):
        source = source_site(index)
        source_sites.append(source)
        witness_sites.append((add(source, EZ), add(source, NEG_EZ)))
        specification = c169.bit_spec("p", index)
        builder.expected(source, specification)
        group: list[tuple[Spec, tuple[Coord, ...]]] = []
        index_leaves = []
        for lane in range(3):
            leaf, direction = candidate_leaf(lane, index)
            index_leaves.append(leaf)
            path = path_to_leaf(source, lane, leaf, direction, index)
            builder.path(specification, path, group=group)
            destination = (lane, "candidate", index)
            candidate_sources[destination] = c169.BitSource(
                leaf,
                direction,
                specification,
                destination,
            )
        builder.path_groups.append(tuple(group))
        all_leaves.append(tuple(index_leaves))

    source_by_destination: dict[
        tuple[int, str, int],
        c169.BitSource,
    ] = {}
    for source in builder.bit_sources:
        previous = source_by_destination.get(source.destination)
        if previous is not None:
            raise ValueError(
                ("duplicate-reference-destination", source.destination)
            )
        source_by_destination[source.destination] = source
    source_by_destination.update(candidate_sources)
    wanted_destinations = {
        (lane, side, index)
        for lane in range(3)
        for side in ("candidate", "reference")
        for index in range(5)
    }
    if set(source_by_destination) != wanted_destinations:
        raise ValueError(
            (
                "five-lane-destination-census",
                wanted_destinations - set(source_by_destination),
                set(source_by_destination) - wanted_destinations,
            )
        )

    payload_first = None
    for lane in range(3):
        for index in range(5):
            group = []
            for side in ("candidate", "reference"):
                destination = (lane, side, index)
                endpoint, target, penultimate = sockets[destination]
                source = source_by_destination[destination]
                before = set(builder.expected_specs)
                builder.literal_path(
                    source,
                    endpoint,
                    target,
                    penultimate,
                    ordinal=2 * index + int(side == "reference"),
                    group=group,
                )
                if lane == 0 and side == "candidate" and index == 0:
                    created = [
                        site
                        for site in builder.expected_specs
                        if site not in before
                    ]
                    payload_first = add(source.site, source.direction)
                    if payload_first not in created:
                        raise ValueError(
                            ("payload-first-not-created", payload_first, created[:3])
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
            path_list = [
                source,
                add(source, NEG_EX),
                add(source, scale(-2, EX)),
            ]
            c169.line_to(
                path_list,
                (path_list[-1][0], path_list[-1][1], 50),
                (2,),
            )
            c169.line_to(
                path_list,
                (path_list[-1][0], 0, 50),
                (1,),
            )
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
    builder.fixed_record(
        (0, 1, -1),
        c169.XOR_ROLE,
        "xor-b-op",
    )
    builder.fixed_record((-1, 0, -1), FRAME, "xor-b-frame")
    builder.fixed_record((1, 0, -1), FRAME, "xor-b-frame")
    builder.expected(
        b_site,
        c169.xor_spec(1),
        frozenset((a_site, e_sites[2])),
    )
    sink = (0, 0, -2)
    builder.fixed_record(add(sink, NEG_EX), H1, "sink-identity-input")
    builder.fixed_record(add(sink, EX), AND_ROLE, "sink-and-operation")
    builder.fixed_record(add(sink, EY), FRAME, "sink-frame")
    builder.fixed_record(add(sink, NEG_EY), FRAME, "sink-frame")
    builder.expected(sink, ("sink",), frozenset((b_site,)))

    if payload_first is None:
        raise ValueError("payload first was not assigned")
    return FiveLanePlan(
        fixed=dict(builder.fixed),
        original_sources=dict(builder.original_sources),
        expected_specs=dict(builder.expected_specs),
        dependencies=dict(builder.dependencies),
        path_groups=tuple(builder.path_groups),
        open_ports=frozenset(builder.open_ports),
        output_site=sink,
        bit_sources=tuple(source_sites),
        witnesses=tuple(witness_sites),
        leaves=tuple(all_leaves),
        payload_first=payload_first,
    )


@lru_cache(maxsize=1)
def structural_scaffold() -> tuple[dict[Coord, str], frozenset[Coord]]:
    plan = five_lane_plan()
    records = dict(plan.fixed)
    for site in plan.original_sources:
        c169.place(records, site, c169.ZERO_ROLE, "dummy-original-source")
    dynamic = set(plan.expected_specs) | set(plan.open_ports)
    protected = frozenset(dynamic | set(plan.original_sources))
    generated_ports: set[Coord] = set()
    for group_index, group in enumerate(plan.path_groups):
        items = tuple(
            (c169.dummy_role(specification), path)
            for specification, path in group
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
                    "five-lane-path-group-cage-failure",
                    group_index,
                    tuple(
                        (specification, path[0], path[-1], len(path))
                        for specification, path in group
                    ),
                    error.args,
                )
            ) from error
        generated_ports.update(ports)

    core_dynamic = set(plan.expected_specs) | set(plan.open_ports)
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
    for site in cage:
        c169.place(records, site, FRAME, "five-lane-global-cage")
    for site in (
        set(plan.expected_specs)
        | set(plan.open_ports)
        | set(plan.original_sources)
    ):
        records.pop(site, None)
    return records, frozenset(generated_ports)


@dataclass(frozen=True)
class FiveLaneInstance:
    measured: Row
    initial: dict[Coord, str]
    expected: dict[Coord, str]
    dependencies: dict[Coord, frozenset[Coord]]
    sources: tuple[Coord, ...]
    witnesses: tuple[tuple[Coord, Coord], ...]
    leaves: tuple[tuple[Coord, ...], ...]
    payload_first: Coord
    payload_guard: Coord
    output: Coord
    expected_output: str


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
    wanted = expected[target]
    for site in sorted(premise):
        if site not in initial or site in excluded:
            continue
        trial = dict(premise)
        trial.pop(site)
        actual = MERGED_RAW.get(
            c169.c53.local_signature(trial, target),
            frozenset(),
        )
        if wanted not in actual:
            return site
    raise ValueError(("no-five-lane-fixed-guard", target, premise))


@lru_cache(maxsize=4)
def instance(measured: Row) -> FiveLaneInstance:
    plan = five_lane_plan()
    scaffold, _ports = structural_scaffold()
    context = c169.semantic_context(IZ, ZZ, measured)
    initial = dict(scaffold)
    expected = {
        site: (
            c169.bit(context[4])
            if specification == ("sink",)
            else c169.resolve_spec_role(specification, context)
        )
        for site, specification in plan.expected_specs.items()
    }
    dependencies = dict(plan.dependencies)
    rows = c169.row_values(IZ, ZZ, measured)
    for site, label in plan.original_sources.items():
        c169.place(
            initial,
            site,
            c169.joint.pivot.five.ROW_ROLE[rows[label]],
            "five-lane-reference-source",
        )
    for index, source in enumerate(plan.bit_sources):
        role = c169.bit(measured[index])
        positive, negative = plan.witnesses[index]
        c169.place(initial, positive, role, "five-lane-positive-witness")
        c169.place(initial, negative, role, "five-lane-negative-witness")
    for site in set(expected) | set(plan.open_ports):
        initial.pop(site, None)
    payload_parent = next(iter(dependencies[plan.payload_first]))
    payload_guard = unique_fixed_guard(
        initial,
        expected,
        dependencies,
        plan.payload_first,
        frozenset((payload_parent,)),
    )
    expected_output = c169.bit(context[4])
    return FiveLaneInstance(
        measured=measured,
        initial=initial,
        expected=expected,
        dependencies=dependencies,
        sources=plan.bit_sources,
        witnesses=plan.witnesses,
        leaves=plan.leaves,
        payload_first=plan.payload_first,
        payload_guard=payload_guard,
        output=plan.output_site,
        expected_output=expected_output,
    )


def local_compiled_check(
    apparatus: FiveLaneInstance,
    *,
    rotation=None,
) -> tuple[int, tuple[object, ...]]:
    checks = 0
    failures = []
    transform = (
        None
        if rotation is None
        else lambda site: add(
            c169.c53.matvec(rotation, site),
            ROTATION_SHIFT,
        )
    )
    for target, wanted in apparatus.expected.items():
        premise = formation_records(
            apparatus.initial,
            apparatus.expected,
            apparatus.dependencies,
            target,
        )
        checked_target = target
        checked_dependencies = apparatus.dependencies[target]
        if transform is not None:
            checked_target = transform(target)
            premise = {
                transform(site): role
                for site, role in premise.items()
            }
            checked_dependencies = frozenset(
                transform(parent)
                for parent in apparatus.dependencies[target]
            )
        actual = MERGED_RAW.get(
            c169.c53.local_signature(premise, checked_target),
            frozenset(),
        )
        checks += 1
        if actual != frozenset((wanted,)):
            failures.append(
                (
                    checked_target,
                    wanted,
                    actual,
                    checked_dependencies,
                )
            )
            if len(failures) >= 10:
                break
    return checks, tuple(failures)


def enabled(
    records: dict[Coord, str],
) -> dict[Coord, frozenset[str]]:
    return {
        target: MERGED_RAW[signature]
        for target in c169.c53.open_candidates(records)
        if (
            signature := c169.c53.local_signature(records, target)
        ) in MERGED_RAW
    }


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


def schedule(
    dependencies: dict[Coord, frozenset[Coord]],
    order: str,
) -> tuple[Coord, ...]:
    children = children_map(dependencies)
    pending = {
        site: len(parents)
        for site, parents in dependencies.items()
    }
    frontier = {site for site, count in pending.items() if count == 0}
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
        raise ValueError(("five-lane-dependency-cycle", len(result), len(dependencies)))
    return tuple(result)


@lru_cache(maxsize=4)
def initial_enabled(measured: Row) -> dict[Coord, frozenset[str]]:
    return enabled(instance(measured).initial)


def dynamic_edge_checks(
    apparatus: FiveLaneInstance,
) -> tuple[int, tuple[object, ...]]:
    attempts = 0
    failures = []
    for target, parents in apparatus.dependencies.items():
        premise = formation_records(
            apparatus.initial,
            apparatus.expected,
            apparatus.dependencies,
            target,
        )
        wanted = apparatus.expected[target]
        for parent in parents:
            attempts += 1
            trial = dict(premise)
            trial.pop(parent)
            actual = MERGED_RAW.get(
                c169.c53.local_signature(trial, target),
                frozenset(),
            )
            if wanted in actual:
                failures.append((target, parent, wanted, actual))
                if len(failures) >= 10:
                    return attempts, tuple(failures)
    return attempts, tuple(failures)


def witness_local_controls(
    apparatus: FiveLaneInstance,
) -> tuple[tuple[int, Coord, frozenset[str]], ...]:
    results = []
    for index, source in enumerate(apparatus.sources):
        premise = formation_records(
            apparatus.initial,
            apparatus.expected,
            apparatus.dependencies,
            source,
        )
        for witness in apparatus.witnesses[index]:
            trial = dict(premise)
            trial.pop(witness)
            actual = MERGED_RAW.get(
                c169.c53.local_signature(trial, source),
                frozenset(),
            )
            results.append((index, witness, actual))
    return tuple(results)


def physical_run(
    apparatus: FiveLaneInstance,
    *,
    order: str,
) -> tuple[bool, object]:
    records = dict(apparatus.initial)
    actual = dict(initial_enabled(apparatus.measured))
    linear = schedule(apparatus.dependencies, order)
    children = children_map(apparatus.dependencies)
    pending = {
        site: len(parents)
        for site, parents in apparatus.dependencies.items()
    }
    frontier = {site for site, count in pending.items() if count == 0}
    work = 0
    maximum = 0
    formed = 0
    for target in linear:
        wanted = {
            site: frozenset((apparatus.expected[site],))
            for site in frontier
        }
        work += len(frontier)
        maximum = max(maximum, len(frontier))
        if actual != wanted:
            return False, (
                "frontier",
                formed,
                tuple(sorted(set(actual) - set(wanted)))[:5],
                tuple(sorted(set(wanted) - set(actual)))[:5],
            )
        records[target] = apparatus.expected[target]
        formed += 1
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
            values = MERGED_RAW.get(signature)
            if values is None:
                actual.pop(candidate, None)
            else:
                actual[candidate] = values
    observed_sources = tuple(records.get(site) for site in apparatus.sources)
    expected_sources = tuple(
        c169.bit(apparatus.measured[index])
        for index in range(5)
    )
    return (
        not actual
        and observed_sources == expected_sources
        and records.get(apparatus.output) == apparatus.expected_output,
        {
            "initial": len(apparatus.initial),
            "dynamic": len(apparatus.expected),
            "work": work,
            "maximum": maximum,
            "sources": observed_sources,
            "output": records.get(apparatus.output),
            "residual": tuple(sorted(actual.items())),
        },
    )


def pruned_physical_run(
    apparatus: FiveLaneInstance,
    *,
    removed_initial: Coord,
    cut: Coord,
    expected_sources: tuple[bool, ...],
    output_expected: bool,
    full_rescan_control: bool = False,
) -> tuple[bool, object]:
    removed = descendants(apparatus.dependencies, {cut})
    expected = {
        site: role
        for site, role in apparatus.expected.items()
        if site not in removed
    }
    dependencies = {
        site: parents
        for site, parents in apparatus.dependencies.items()
        if site not in removed
    }
    if any(not parents <= expected.keys() for parents in dependencies.values()):
        return False, ("uncollapsed-five-lane-cut", cut)

    records = dict(apparatus.initial)
    records.pop(removed_initial, None)
    actual = dict(initial_enabled(apparatus.measured))
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
        values = MERGED_RAW.get(signature)
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
                "five-lane-reseed-mismatch",
                tuple(sorted(set(actual) - set(rescanned)))[:5],
                tuple(sorted(set(rescanned) - set(actual)))[:5],
            )

    linear = schedule(dependencies, "min")
    children = children_map(dependencies)
    pending = {
        site: len(parents)
        for site, parents in dependencies.items()
    }
    frontier = {site for site, count in pending.items() if count == 0}
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
            values = MERGED_RAW.get(signature)
            if values is None:
                actual.pop(candidate, None)
            else:
                actual[candidate] = values

    observed_sources = tuple(source in records for source in apparatus.sources)
    observed_output = apparatus.output in records
    return (
        not actual
        and observed_sources == expected_sources
        and observed_output == output_expected,
        {
            "removed": len(removed),
            "remaining": len(expected),
            "sources": observed_sources,
            "output": observed_output,
            "rescan_equivalent": rescan_equivalent,
            "residual": tuple(sorted(actual.items())),
        },
    )


def causal_certificate(
    apparatus: FiveLaneInstance,
) -> dict[str, object]:
    children = children_map(apparatus.dependencies)
    pending = {
        site: len(parents)
        for site, parents in apparatus.dependencies.items()
    }
    frontier = deque(sorted(site for site, count in pending.items() if count == 0))
    depth: dict[Coord, int] = {}
    profile: Counter[int] = Counter()
    while frontier:
        site = frontier.popleft()
        parents = apparatus.dependencies[site]
        value = (
            1 + max(depth[parent] for parent in parents)
            if parents
            else 1
        )
        depth[site] = value
        profile[value] += 1
        for child in children.get(site, ()):
            pending[child] -= 1
            if pending[child] == 0:
                frontier.append(child)
    if len(depth) != len(apparatus.expected):
        raise ValueError(("five-lane-causal-cycle", len(depth), len(apparatus.expected)))
    source_depths = tuple(depth[site] for site in apparatus.sources)
    leaf_depths = tuple(
        tuple(depth[site] for site in leaves)
        for leaves in apparatus.leaves
    )
    return {
        "depth": max(depth.values()),
        "sources": source_depths,
        "leaves": leaf_depths,
        "payload_first": depth[apparatus.payload_first],
        "output": depth[apparatus.output],
        "edges": sum(map(len, apparatus.dependencies.values())),
        "roots": sum(not parents for parents in apparatus.dependencies.values()),
        "profile_hash": hashlib.sha256(
            ",".join(
                str(profile[index])
                for index in range(1, max(profile) + 1)
            ).encode("utf-8")
        ).hexdigest(),
    }


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND BINARY INGRESS")
    check(
        "Cycle 169 and Cycle 176 frozen hashes match",
        sha256(CYCLE169_SCRIPT) == FROZEN_CYCLE169_SCRIPT_SHA
        and sha256(CYCLE169_NOTE) == FROZEN_CYCLE169_NOTE_SHA
        and sha256(CYCLE176_SCRIPT) == FROZEN_CYCLE176_SCRIPT_SHA
        and sha256(CYCLE176_NOTE) == FROZEN_CYCLE176_NOTE_SHA,
        (
            sha256(CYCLE169_SCRIPT),
            sha256(CYCLE169_NOTE),
            sha256(CYCLE176_SCRIPT),
            sha256(CYCLE176_NOTE),
        ),
    )
    check(
        "two H0/H1 schemas add exactly six conflict-free rows",
        len(BINARY_INGRESS_TABLE) == 2
        and len(BINARY_INGRESS_RAW) == 6
        and not (set(BINARY_INGRESS_RAW) & set(c169.UNIFIED_RAW))
        and len(MERGED_RAW) == 101_714
        and not RAW_CONFLICTS,
        (
            len(BINARY_INGRESS_TABLE),
            len(BINARY_INGRESS_RAW),
            len(MERGED_RAW),
            len(RAW_CONFLICTS),
        ),
    )

    print("\nFIVE-LANE PLAN")
    plan = five_lane_plan()
    scaffold, ports = structural_scaffold()
    check(
        "five separate bit sources feed fifteen candidate leaves",
        len(plan.bit_sources) == 5
        and len(plan.witnesses) == 5
        and all(len(leaves) == 3 for leaves in plan.leaves)
        and len({leaf for leaves in plan.leaves for leaf in leaves}) == 15,
        {
            "sources": plan.bit_sources,
            "leaves": plan.leaves,
            "scaffold": len(scaffold),
            "ports": len(ports),
        },
    )
    check(
        "the plan contains no measured-row role source or row(p) write",
        "p" not in set(plan.original_sources.values())
        and ("row", "p") not in set(plan.expected_specs.values()),
        (
            plan.original_sources,
            tuple(
                item
                for item in plan.expected_specs.items()
                if item[1] == ("row", "p")
            ),
        ),
    )
    neighborhoods = tuple(
        frozenset(
            (source,)
            + tuple(add(source, direction) for direction in c169.c53.DIRECTIONS)
        )
        for source in plan.bit_sources
    )
    check(
        "the five ingress neighborhoods are pairwise disjoint and noncontacting",
        all(
            not (neighborhoods[left] & neighborhoods[right])
            and all(
                c169.manhattan(a, b) > 1
                for a in neighborhoods[left]
                for b in neighborhoods[right]
            )
            for left in range(5)
            for right in range(left + 1, 5)
        ),
        tuple(len(value) for value in neighborhoods),
    )

    print("\nLOCAL CODEWORD CENSUS")
    failures = []
    shapes = set()
    support = Counter()
    for measured in product((0, 1), repeat=5):
        apparatus = instance(measured)
        checks, local_failures = local_compiled_check(apparatus)
        support[apparatus.expected_output] += 1
        shapes.add(
            (
                len(apparatus.initial),
                len(apparatus.expected),
                len(apparatus.dependencies),
            )
        )
        if checks != len(apparatus.expected) or local_failures:
            failures.append((measured, checks, local_failures[:2]))
    check(
        "all 32 finite five-bit codewords compile under one geometry",
        not failures and len(shapes) == 1,
        {"shapes": shapes, "failures": failures[:2]},
    )
    check(
        "exact output support over all 32 codewords is three accepts and twenty-nine rejects",
        support == Counter({H0: 29, H1: 3}),
        support,
    )

    print("\nLOAD-BEARING CAUSAL GRAPH")
    hard = instance(ZI)
    source_neighbors = tuple(
        {
            direction: hard.initial.get(add(source, direction))
            for direction in c169.c53.DIRECTIONS
        }
        for source in hard.sources
    )
    check(
        "each source is bare except for its two matching binary witnesses",
        all(
            neighbors[EZ] == c169.bit(ZI[index])
            and neighbors[NEG_EZ] == c169.bit(ZI[index])
            and all(
                neighbors[direction] is None
                for direction in (EX, NEG_EX, EY, NEG_EY)
            )
            for index, neighbors in enumerate(source_neighbors)
        ),
        source_neighbors,
    )
    witness_controls = witness_local_controls(hard)
    check(
        "all ten individual witness deletions suppress their source locally",
        len(witness_controls) == 10
        and all(not actual for _index, _site, actual in witness_controls),
        witness_controls,
    )
    edge_attempts, edge_failures = dynamic_edge_checks(hard)
    check(
        "every declared dynamic edge is load-bearing",
        edge_attempts == sum(map(len, hard.dependencies.values()))
        and not edge_failures,
        (edge_attempts, edge_failures[:2]),
    )
    causal = causal_certificate(hard)
    check(
        "causal depth orders five formations before leaves, payload, and output",
        causal["sources"] == (1, 1, 1, 1, 1)
        and all(
            all(depth > 1 for depth in lane_depths)
            for lane_depths in causal["leaves"]
        )
        and causal["payload_first"] > min(
            depth
            for lane_depths in causal["leaves"]
            for depth in lane_depths
        )
        and causal["output"] > causal["payload_first"],
        causal,
    )

    print("\nACCEPT AND REJECT PHYSICAL REPLAYS")
    accepted = physical_run(hard, order="min")
    rejected = physical_run(instance(NEG_ZI), order="max")
    check(
        "one accept and one sign-flipped reject close physically and terminally",
        accepted[0]
        and rejected[0]
        and isinstance(accepted[1], dict)
        and isinstance(rejected[1], dict)
        and accepted[1]["output"] == H1
        and rejected[1]["output"] == H0,
        {"accept": accepted, "reject": rejected},
    )

    print("\nTEN WITNESS DELETIONS AND PAYLOAD SEPARATION")
    witness_prunes = []
    for index, source in enumerate(hard.sources):
        for witness_index, witness in enumerate(hard.witnesses[index]):
            expected_sources = tuple(
                lane != index for lane in range(5)
            )
            result = pruned_physical_run(
                hard,
                removed_initial=witness,
                cut=source,
                expected_sources=expected_sources,
                output_expected=False,
                full_rescan_control=index == 0 and witness_index == 0,
            )
            witness_prunes.append((index, witness_index, result))
    check(
        "all ten physical witness deletions remove only their source lane and final output",
        all(result[0] for _index, _witness, result in witness_prunes),
        witness_prunes[:2],
    )
    check(
        "the first witness-deletion reseed equals a full global rescan",
        isinstance(witness_prunes[0][2][1], dict)
        and witness_prunes[0][2][1]["rescan_equivalent"] is True,
        witness_prunes[0],
    )
    payload_parent = next(iter(hard.dependencies[hard.payload_first]))
    payload = pruned_physical_run(
        hard,
        removed_initial=hard.payload_guard,
        cut=hard.payload_first,
        expected_sources=(True, True, True, True, True),
        output_expected=False,
    )
    check(
        "payload-only deletion leaves all five formed sources present",
        payload[0]
        and isinstance(payload[1], dict)
        and payload[1]["sources"] == (True, True, True, True, True)
        and payload[1]["output"] is False,
        {
            "guard": hard.payload_guard,
            "parent": payload_parent,
            "target": hard.payload_first,
            "result": payload,
        },
    )

    print("\nPROPER-CUBIC COVARIANCE")
    rotation_checks = 0
    rotation_failures = []
    for rotation_index, rotation in enumerate(c169.c53.ROTATIONS):
        transformed_directions = {
            c169.c53.matvec(rotation, direction)
            for direction in c169.c53.DIRECTIONS
        }
        checks, local_failures = local_compiled_check(hard, rotation=rotation)
        rotation_checks += checks
        if (
            c169.c53.determinant(rotation) != 1
            or transformed_directions != set(c169.c53.DIRECTIONS)
            or local_failures
        ):
            rotation_failures.append(
                (
                    rotation_index,
                    c169.c53.determinant(rotation),
                    transformed_directions,
                    local_failures[:2],
                )
            )
    check(
        "all 24 proper-cubic images compile by exact isomorphism",
        rotation_checks == 24 * len(hard.expected)
        and not rotation_failures,
        (rotation_checks, rotation_failures[:2]),
    )

    print("\nSCOPE")
    normalized = (
        " ".join(NOTE.read_text(encoding="utf-8").lower().split())
        if NOTE.is_file()
        else ""
    )
    required = (
        "five-lane formation",
        "no reconstructed 32-valued measured-row site",
        "generated finite-composition domain",
        "not a tensor-product theorem",
        "does not choose axiom language",
        "no axiom, primitive, registry, policy, or audit edit follows",
    )
    missing = tuple(phrase for phrase in required if phrase not in normalized)
    check("the note carries the finite-composition boundary", not missing, missing)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "FIVE_LANE_FORMATION_MEMBERSHIP" if FAIL == 0 else "FAIL",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
