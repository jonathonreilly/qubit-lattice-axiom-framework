#!/usr/bin/env python3
"""Cycle 177: all-nine/six-context shared-ancestry construction."""

from __future__ import annotations

import ast
import hashlib
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import lru_cache
from itertools import product
from pathlib import Path

import shared_ancestry_dual_context_peres_mermin_cycle173_2026_07_16 as c173


c169 = c173.c169
Coord = c173.Coord
Row = c173.Row
Spec = c173.Spec
EX = c173.EX
EY = c173.EY
EZ = c173.EZ
NEG_EX = c173.NEG_EX
NEG_EY = c173.NEG_EY
NEG_EZ = c173.NEG_EZ
FRAME = c173.FRAME
GUIDE = c173.GUIDE
H0 = c173.H0
H1 = c173.H1

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "ALL_NINE_SIX_CONTEXT_SHARED_ANCESTRY_CYCLE177_NOTE_2026-07-16.md"
)
CYCLE168 = ROOT / "scripts/peres_mermin_factorized_reference_census_2026_07_16.py"
CYCLE173 = (
    ROOT
    / "scripts/shared_ancestry_dual_context_peres_mermin_cycle173_2026_07_16.py"
)
CYCLE173_CHECK = (
    ROOT
    / "scripts/shared_ancestry_dual_context_cycle173_port_contract_check_2026_07_16.py"
)
CYCLE173_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "SHARED_ANCESTRY_DUAL_CONTEXT_PERES_MERMIN_CYCLE173_NOTE_2026-07-16.md"
)
FROZEN = {
    CYCLE173: "92afd28e4cf8b36b98b90b8cf919e13052716a056c64377396da304cb42acc11",
    CYCLE173_CHECK: "d1fcdd953fd9d6dc35e680b28fd7c1fda4eb542b6aae63521cb7f3a5d8d67c55",
    CYCLE173_NOTE: "6c241e3f19dace1c67ed48199c04627d446dff64c01f4dde0c8ae76be37d0cc4",
}

EXPECTED_CONTEXTS = (
    ("R1", (11, 2, 14), 0),
    ("R2", (0, 3, 4), 0),
    ("R3", (12, 6, 9), 0),
    ("C1", (11, 0, 12), 0),
    ("C2", (2, 3, 6), 0),
    ("C3", (14, 4, 9), 1),
)
OBSERVABLE_IDS = tuple(sorted({item for _label, ids, _sign in EXPECTED_CONTEXTS for item in ids}))
OBSERVABLE_INDEX = {measurement_id: index for index, measurement_id in enumerate(OBSERVABLE_IDS)}

CONTEXT_SHIFTS = {
    "R1": (0, -10_000, 0),
    "R2": (0, -6_000, 0),
    "R3": (0, -2_000, 0),
    "C1": (0, 2_000, 0),
    "C2": (0, 6_000, 0),
    "C3": (0, 10_000, 0),
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
    return c173.add(left, right)


def sub(left: Coord, right: Coord) -> Coord:
    return c173.sub(left, right)


def scale(factor: int, vector: Coord) -> Coord:
    return c173.scale(factor, vector)


def shifted(site: Coord, delta: Coord) -> Coord:
    return add(site, delta)


def place(
    records: dict[Coord, str],
    site: Coord,
    role: str,
    label: str,
) -> None:
    c173.place(records, site, role, label)


def add_expected(
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
    site: Coord,
    role: str,
    parents: frozenset[Coord],
    label: str,
) -> None:
    c173.add_expected(expected, dependencies, site, role, parents, label)


@dataclass(frozen=True)
class FullyPortedPlan:
    fixed: dict[Coord, str]
    expected_specs: dict[Coord, Spec]
    dependencies: dict[Coord, frozenset[Coord]]
    path_groups: tuple[tuple[tuple[Spec, tuple[Coord, ...]], ...], ...]
    open_ports: frozenset[Coord]
    output_site: Coord
    row_inputs: dict[str, Coord]
    leaf_counts: dict[str, int]


@dataclass(frozen=True)
class ContextInstance:
    label: str
    initial: dict[Coord, str]
    expected: dict[Coord, str]
    dependencies: dict[Coord, frozenset[Coord]]
    output_site: Coord
    output_port: Coord
    row_inputs: dict[str, Coord]
    removable_cage: frozenset[Coord]
    rows: tuple[Row, Row, Row]
    membership: int


@dataclass(frozen=True)
class Apparatus:
    assignment: tuple[int, ...]
    initial: dict[Coord, str]
    expected: dict[Coord, str]
    dependencies: dict[Coord, frozenset[Coord]]
    source_sites: dict[int, Coord]
    source_splitters: dict[int, Coord]
    branch_first: dict[tuple[int, str], Coord]
    context_outputs: dict[str, Coord]
    context_bits: tuple[int, ...]
    parity_targets: tuple[Coord, ...]
    parity_terminal: Coord
    interface_sites: frozenset[Coord]


class RecordView:
    """Mutable dynamic overlay on one immutable initial-record dictionary."""

    def __init__(
        self,
        base: dict[Coord, str],
        *,
        overrides: dict[Coord, str] | None = None,
        removed: frozenset[Coord] = frozenset(),
    ) -> None:
        self.base = base
        self.overlay = dict(overrides or {})
        self.removed = removed

    def __contains__(self, site: object) -> bool:
        return site in self.overlay or (
            site not in self.removed and site in self.base
        )

    def __getitem__(self, site: Coord) -> str:
        if site in self.overlay:
            return self.overlay[site]
        if site in self.removed:
            raise KeyError(site)
        return self.base[site]

    def __setitem__(self, site: Coord, role: str) -> None:
        self.overlay[site] = role


def contexts_from_cycle168() -> tuple[object, ...]:
    tree = ast.parse(CYCLE168.read_text(encoding="utf-8"))
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


def signed_measurement(measurement_id: int, sign_bit: int) -> Row:
    positive = c169.tableau.measurement_row(measurement_id, 1)
    return (*positive[:4], positive[4] ^ sign_bit)


def path_through(start: Coord, waypoints: tuple[Coord, ...]) -> tuple[Coord, ...]:
    return c173.path_through(start, waypoints)


def add_path_expected(
    path: tuple[Coord, ...],
    role: str,
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
    label: str,
) -> None:
    c173.add_path_expected(path, role, expected, dependencies, label)


def occurrence_map() -> dict[int, tuple[tuple[str, str], ...]]:
    return {
        measurement_id: tuple(
            (label, port_role)
            for label, ids, _sign in EXPECTED_CONTEXTS
            for port_role, candidate in zip(("g1", "g2", "p"), ids, strict=True)
            if candidate == measurement_id
        )
        for measurement_id in OBSERVABLE_IDS
    }


def source_geometry() -> tuple[
    dict[int, Coord],
    dict[int, Coord],
]:
    splitters = {
        measurement_id: (-6_000, 0, 2_000 + 800 * index)
        for index, measurement_id in enumerate(OBSERVABLE_IDS)
    }
    sources = {
        measurement_id: add(splitter, NEG_EX)
        for measurement_id, splitter in splitters.items()
    }
    return sources, splitters


def input_paths() -> tuple[
    dict[tuple[int, str], tuple[Coord, ...]],
    dict[tuple[int, str], Coord],
]:
    plan = fully_ported_plan()
    _sources, splitters = source_geometry()
    paths = {}
    first_sites = {}
    for measurement_id, occurrences in occurrence_map().items():
        splitter = splitters[measurement_id]
        for context_label, port_role in occurrences:
            direction = NEG_EY if context_label.startswith("R") else EY
            target = shifted(
                plan.row_inputs[port_role],
                CONTEXT_SHIFTS[context_label],
            )
            first = add(splitter, direction)
            source_z = splitter[2]
            target_y = target[1]
            path = path_through(
                splitter,
                (
                    first,
                    (splitter[0], -10 if direction == NEG_EY else 10, source_z),
                    (splitter[0], target_y, source_z),
                    (-1_200, target_y, source_z),
                    (-1_200, target_y, target[2]),
                    (target[0] - 1, target_y, target[2]),
                    target,
                ),
            )
            paths[(measurement_id, context_label)] = path
            first_sites[(measurement_id, context_label)] = first
    return paths, first_sites


def parity_geometry() -> tuple[
    tuple[Coord, ...],
    tuple[Coord, ...],
    tuple[tuple[Coord, ...], ...],
]:
    targets = tuple((6_000, 0, -200 * index) for index in range(5))
    context_endpoints = (
        add(targets[0], EZ),
        add(targets[0], EX),
        add(targets[1], EX),
        add(targets[2], EX),
        add(targets[3], EX),
        add(targets[4], EX),
    )
    inter_paths = tuple(
        tuple(
            (targets[index][0], targets[index][1], z)
            for z in range(
                targets[index][2],
                targets[index + 1][2],
                -1,
            )
        )
        for index in range(4)
    )
    if any(path[-1] != add(targets[index + 1], EZ) for index, path in enumerate(inter_paths)):
        raise ValueError(("bad-parity-inter-path", tuple(path[-1] for path in inter_paths)))
    return targets, context_endpoints, inter_paths


def context_output_paths(
    output_sites: dict[str, Coord],
    output_ports: dict[str, Coord],
) -> tuple[tuple[Coord, ...], ...]:
    _targets, endpoints, _inter_paths = parity_geometry()
    paths = []
    for index, (label, endpoint) in enumerate(
        zip((item[0] for item in EXPECTED_CONTEXTS), endpoints, strict=True)
    ):
        output = output_sites[label]
        port = output_ports[label]
        if c169.manhattan(output, port) != 1:
            raise ValueError(("bad-context-output-port", label, output, port))
        terminal_direction = sub(endpoint, parity_geometry()[0][0])
        if index == 0:
            prior = add(endpoint, EZ)
        else:
            prior = add(endpoint, EX)
        channel_z = -3_000 - 600 * index
        channel_x = 8_000 - 200 * index
        path = path_through(
            output,
            (
                port,
                (port[0], port[1], channel_z),
                (channel_x, port[1], channel_z),
                (channel_x, 0, channel_z),
                (channel_x, 0, prior[2]),
                prior,
                endpoint,
            ),
        )
        if index == 0 and add(endpoint, NEG_EZ) != parity_geometry()[0][0]:
            raise ValueError(("bad-first-context-endpoint", endpoint))
        if index > 0:
            target = parity_geometry()[0][index - 1]
            if add(endpoint, NEG_EX) != target:
                raise ValueError(("bad-context-endpoint", index, endpoint, target))
        paths.append(path)
    return tuple(paths)


@lru_cache(maxsize=1)
def fully_ported_plan() -> FullyPortedPlan:
    builder = c169.Builder()
    multiplier_shift = (0, -300, 0)
    product_tree = add(c169.cycle164.OUTPUT_PORT, multiplier_shift)
    sockets, final_sites = builder.comparator_sockets()

    roots = {
        "p": (-240, 0, 0),
        "g1": (-240, 200, 0),
        "g2": (-240, -200, 0),
    }
    row_inputs = {
        label: add(root, NEG_EX)
        for label, root in roots.items()
    }

    p_leaves = tuple(
        ("decode", index, (lane, "candidate", index))
        for lane in range(3)
        for index in range(5)
    )
    builder.comb_tree(roots["p"], "p", p_leaves)

    left_source = add(c169.cycle164.LEFT_PATH[0], multiplier_shift)
    left_future = add(c169.cycle164.LEFT_PATH[1], multiplier_shift)
    right_source = add(c169.cycle164.RIGHT_PATH[0], multiplier_shift)
    right_future = add(c169.cycle164.RIGHT_PATH[1], multiplier_shift)
    g1_leaves = tuple(
        ("decode", index, (0, "reference", index))
        for index in range(5)
    ) + (
        ("feed", left_source, left_future, (-700, -350, 300)),
    )
    g2_leaves = tuple(
        ("decode", index, (1, "reference", index))
        for index in range(5)
    ) + (
        ("feed", right_source, right_future, (-176, -202, -60)),
    )
    builder.comb_tree(roots["g1"], "g1", g1_leaves)
    builder.comb_tree(roots["g2"], "g2", g2_leaves)

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
            c169.line_to(
                path_list,
                (path_list[-1][0], path_list[-1][1], 50),
                (2,),
            )
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
                raise ValueError(("nonaxial-final-path", lane, source, endpoint))
            distance = c169.manhattan(source, endpoint)
            path = tuple(
                add(source, scale(step, direction))
                for step in range(distance + 1)
            )
        consumer = a_site if lane < 2 else b_site
        if add(path[-1], direction) != consumer:
            raise ValueError(("bad-final-status-port", lane, path[-1], consumer))
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

    return FullyPortedPlan(
        fixed=dict(builder.fixed),
        expected_specs=dict(builder.expected_specs),
        dependencies=dict(builder.dependencies),
        path_groups=tuple(builder.path_groups),
        open_ports=frozenset(builder.open_ports),
        output_site=b_site,
        row_inputs=row_inputs,
        leaf_counts={"g1": len(g1_leaves), "g2": len(g2_leaves), "p": len(p_leaves)},
    )


@lru_cache(maxsize=1)
def fully_ported_scaffold() -> tuple[
    dict[Coord, str],
    frozenset[Coord],
    frozenset[Coord],
]:
    plan = fully_ported_plan()
    records = dict(plan.fixed)
    dynamic = set(plan.expected_specs) | set(plan.open_ports) | set(plan.row_inputs.values())
    protected = frozenset(dynamic)
    generated_ports: set[Coord] = set()
    for group_index, group in enumerate(plan.path_groups):
        items = tuple((c169.dummy_role(spec), path) for spec, path in group)
        try:
            records, _outputs, ports = c169.greedy_path_core(
                items,
                constraints=records,
                extra_protected=protected,
            )
        except ValueError as error:
            raise ValueError(
                (
                    "fully-ported-path-group-cage-failure",
                    group_index,
                    tuple((spec, path[0], path[-1], len(path)) for spec, path in group),
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
        place(records, site, FRAME, "fully-ported-global-cage")

    for site in set(plan.expected_specs) | set(plan.open_ports) | set(plan.row_inputs.values()):
        records.pop(site, None)
    return records, frozenset(generated_ports), frozenset(added_cage)


def context_instance(
    label: str,
    rows: tuple[Row, Row, Row],
    shift: Coord,
    *,
    supply_inputs: bool = False,
) -> ContextInstance:
    plan = fully_ported_plan()
    scaffold, _ports, removable_cage = fully_ported_scaffold()
    g1, g2, measured = rows
    semantic = c169.semantic_context(g1, g2, measured)
    _rows, equalities, _prefixes, _xor_a, xor_b = semantic

    initial = {shifted(site, shift): role for site, role in scaffold.items()}
    expected = {
        shifted(site, shift): c169.resolve_spec_role(spec, semantic)
        for site, spec in plan.expected_specs.items()
    }
    dependencies = {
        shifted(site, shift): frozenset(shifted(parent, shift) for parent in parents)
        for site, parents in plan.dependencies.items()
    }
    moved_inputs = {
        row_label: shifted(site, shift)
        for row_label, site in plan.row_inputs.items()
    }
    for site in set(expected) | {
        shifted(site, shift) for site in plan.open_ports
    } | set(moved_inputs.values()):
        initial.pop(site, None)
    if supply_inputs:
        for row_label, row in zip(("g1", "g2", "p"), rows, strict=True):
            place(
                initial,
                moved_inputs[row_label],
                c169.joint.pivot.five.ROW_ROLE[row],
                f"{label}-{row_label}-supplied-input",
            )
    return ContextInstance(
        label=label,
        initial=initial,
        expected=expected,
        dependencies=dependencies,
        output_site=shifted(plan.output_site, shift),
        output_port=shifted(next(iter(plan.open_ports)), shift),
        row_inputs=moved_inputs,
        removable_cage=frozenset(shifted(site, shift) for site in removable_cage),
        rows=rows,
        membership=int(xor_b),
    )


def local_compiled_check(instance: ContextInstance) -> tuple[int, tuple[object, ...]]:
    failures = []
    checks = 0
    for target, role in instance.expected.items():
        premise = {
            neighbor: instance.initial[neighbor]
            for direction in c169.c53.DIRECTIONS
            if (neighbor := add(target, direction)) in instance.initial
        }
        premise.update(
            {
                parent: (
                    instance.expected[parent]
                    if parent in instance.expected
                    else instance.initial[parent]
                )
                for parent in instance.dependencies[target]
            }
        )
        actual = c169.UNIFIED_RAW.get(
            c169.c53.local_signature(premise, target),
            frozenset(),
        )
        checks += 1
        if actual != frozenset((role,)):
            failures.append((target, role, actual, instance.dependencies[target]))
            if len(failures) >= 10:
                break
    return checks, tuple(failures)


@lru_cache(maxsize=None)
def apparatus(assignment: tuple[int, ...]) -> Apparatus:
    if len(assignment) != len(OBSERVABLE_IDS) or any(bit not in (0, 1) for bit in assignment):
        raise ValueError(("bad-assignment", assignment))

    signs = dict(zip(OBSERVABLE_IDS, assignment, strict=True))
    plan = fully_ported_plan()
    scaffold, _ports, removable_cage = fully_ported_scaffold()
    sources, splitters = source_geometry()
    incoming_paths, first_sites = input_paths()
    parity_targets, _context_endpoints, inter_paths = parity_geometry()

    context_rows = {
        label: tuple(signed_measurement(measurement_id, signs[measurement_id]) for measurement_id in ids)
        for label, ids, _unsigned_sign in EXPECTED_CONTEXTS
    }
    semantics = {
        label: c169.semantic_context(*rows)
        for label, rows in context_rows.items()
    }
    context_bits = tuple(
        int(semantics[label][-1])
        for label, _ids, _unsigned_sign in EXPECTED_CONTEXTS
    )
    output_sites = {
        label: shifted(plan.output_site, CONTEXT_SHIFTS[label])
        for label, _ids, _sign in EXPECTED_CONTEXTS
    }
    output_ports = {
        label: shifted(next(iter(plan.open_ports)), CONTEXT_SHIFTS[label])
        for label, _ids, _sign in EXPECTED_CONTEXTS
    }
    outgoing_paths = context_output_paths(output_sites, output_ports)

    input_roles = {
        (measurement_id, context_label): c169.joint.pivot.five.ROW_ROLE[
            signed_measurement(measurement_id, signs[measurement_id])
        ]
        for measurement_id, occurrences in occurrence_map().items()
        for context_label, _port_role in occurrences
    }
    output_roles = tuple(c169.bit(bit) for bit in context_bits)
    cumulative_bits = []
    cumulative = context_bits[0] ^ context_bits[1]
    cumulative_bits.append(cumulative)
    for bit in context_bits[2:]:
        cumulative ^= bit
        cumulative_bits.append(cumulative)
    parity_roles = tuple(c169.bit(bit) for bit in cumulative_bits)

    interface_items = tuple(
        (input_roles[key], incoming_paths[key])
        for key in sorted(incoming_paths)
    ) + tuple(
        (role, path)
        for role, path in zip(output_roles, outgoing_paths, strict=True)
    ) + tuple(
        (parity_roles[index], path)
        for index, path in enumerate(inter_paths)
    )
    interface_dynamic = {
        site
        for _role, path in interface_items
        for site in path
    } | set(splitters.values()) | set(parity_targets)
    interface_closed = interface_dynamic | {
        add(site, direction)
        for site in interface_dynamic
        for direction in c169.c53.DIRECTIONS
    }

    initial: dict[Coord, str] = {}
    expected: dict[Coord, str] = {}
    dependencies: dict[Coord, frozenset[Coord]] = {}

    # Merge each translated context directly from the one local scaffold.  This
    # avoids holding six duplicate million-record dictionaries at once.
    for label, _ids, _unsigned_sign in EXPECTED_CONTEXTS:
        shift = CONTEXT_SHIFTS[label]
        semantic = semantics[label]
        for local_site, role in scaffold.items():
            site = shifted(local_site, shift)
            if local_site in removable_cage and site in interface_closed:
                continue
            place(initial, site, role, f"{label}-scaffold")
        for local_site, spec in plan.expected_specs.items():
            site = shifted(local_site, shift)
            add_expected(
                expected,
                dependencies,
                site,
                c169.resolve_spec_role(spec, semantic),
                frozenset(
                    shifted(parent, shift)
                    for parent in plan.dependencies[local_site]
                ),
                f"{label}-expected",
            )

    source_record_sites = set()
    splitter_fixed_sites = set()
    for measurement_id in OBSERVABLE_IDS:
        role = c169.joint.pivot.five.ROW_ROLE[
            signed_measurement(measurement_id, signs[measurement_id])
        ]
        source = sources[measurement_id]
        splitter = splitters[measurement_id]
        place(initial, source, role, f"source-{measurement_id}")
        source_record_sites.add(source)
        for site, fixed_role in (
            (add(splitter, EZ), GUIDE),
            (add(splitter, NEG_EZ), FRAME),
            (add(splitter, EX), FRAME),
        ):
            place(initial, site, fixed_role, f"splitter-{measurement_id}")
            splitter_fixed_sites.add(site)
        add_expected(
            expected,
            dependencies,
            splitter,
            role,
            frozenset(),
            f"splitter-{measurement_id}",
        )

    xor_fixed_sites = set()
    for index, target in enumerate(parity_targets):
        for site, role in (
            (add(target, NEG_EX), c169.XOR_ROLE),
            (add(target, EY), FRAME),
            (add(target, NEG_EY), FRAME),
        ):
            place(initial, site, role, f"parity-xor-{index}")
            xor_fixed_sites.add(site)

    protected = frozenset(
        set(expected)
        | interface_dynamic
        | source_record_sites
        | splitter_fixed_sites
        | xor_fixed_sites
    )
    # Cable furniture is radius-one local.  Supplying only constraints in the
    # closed support of these routes is therefore exactly equivalent to copying
    # the complete multi-million-record context corpus into the path solver.
    local_constraints = {
        site: initial[site]
        for site in interface_closed
        if site in initial
    }
    interface_records, _interface_expected, _terminal_ports = c169.greedy_path_core(
        interface_items,
        constraints=local_constraints,
        extra_protected=protected,
    )
    for site in interface_dynamic:
        interface_records.pop(site, None)
    new_interface_records = {
        site for site in interface_records
        if site not in initial
    }
    for site, role in interface_records.items():
        place(initial, site, role, "global-interface-furniture")

    for key, path in incoming_paths.items():
        add_path_expected(
            path,
            input_roles[key],
            expected,
            dependencies,
            f"input-{key}",
        )
    for (label, _ids, _unsigned_sign), path, role in zip(
        EXPECTED_CONTEXTS,
        outgoing_paths,
        output_roles,
        strict=True,
    ):
        add_path_expected(
            path,
            role,
            expected,
            dependencies,
            f"output-{label}",
        )

    add_expected(
        expected,
        dependencies,
        parity_targets[0],
        parity_roles[0],
        frozenset((add(parity_targets[0], EZ), add(parity_targets[0], EX))),
        "parity-0",
    )
    for index, path in enumerate(inter_paths):
        add_path_expected(
            path,
            parity_roles[index],
            expected,
            dependencies,
            f"parity-link-{index}",
        )
        next_index = index + 1
        add_expected(
            expected,
            dependencies,
            parity_targets[next_index],
            parity_roles[next_index],
            frozenset(
                (
                    add(parity_targets[next_index], EZ),
                    add(parity_targets[next_index], EX),
                )
            ),
            f"parity-{next_index}",
        )

    all_dynamic = set(expected)
    external_record_sites = (
        new_interface_records
        | source_record_sites
        | splitter_fixed_sites
        | xor_fixed_sites
    )
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
            and add(site, direction) not in all_dynamic
            and not any(
                add(add(site, direction), neighbor_direction) in all_dynamic
                for neighbor_direction in c169.c53.DIRECTIONS
            )
        )
    }
    for site in external_cage:
        if site not in expected:
            place(initial, site, FRAME, "global-external-cage")
    for site in expected:
        initial.pop(site, None)

    return Apparatus(
        assignment=assignment,
        initial=initial,
        expected=expected,
        dependencies=dependencies,
        source_sites=sources,
        source_splitters=splitters,
        branch_first=first_sites,
        context_outputs=output_sites,
        context_bits=context_bits,
        parity_targets=parity_targets,
        parity_terminal=parity_targets[-1],
        interface_sites=frozenset(interface_dynamic),
    )


def formation_records(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
    target: Coord,
) -> dict[Coord, str]:
    return c173.formation_records(initial, expected, dependencies, target)


def global_local_compiled_check(
    instance: Apparatus,
) -> tuple[int, tuple[object, ...]]:
    failures = []
    checks = 0
    for target, role in instance.expected.items():
        premise = formation_records(
            instance.initial,
            instance.expected,
            instance.dependencies,
            target,
        )
        actual = c169.UNIFIED_RAW.get(
            c169.c53.local_signature(premise, target),
            frozenset(),
        )
        checks += 1
        if actual != frozenset((role,)):
            failures.append((target, role, actual, instance.dependencies[target]))
            if len(failures) >= 10:
                break
    return checks, tuple(failures)


def assignment_semantics(
    assignment: tuple[int, ...],
) -> tuple[
    dict[str, object],
    tuple[int, ...],
]:
    signs = dict(zip(OBSERVABLE_IDS, assignment, strict=True))
    semantics = {
        label: c169.semantic_context(
            *tuple(
                signed_measurement(measurement_id, signs[measurement_id])
                for measurement_id in ids
            )
        )
        for label, ids, _unsigned_sign in EXPECTED_CONTEXTS
    }
    bits = tuple(
        int(semantics[label][-1])
        for label, _ids, _unsigned_sign in EXPECTED_CONTEXTS
    )
    return semantics, bits


def fully_ported_semantic_check(
    rows: tuple[Row, Row, Row],
) -> tuple[int, tuple[object, ...], int]:
    plan = fully_ported_plan()
    scaffold, _ports, _removable = fully_ported_scaffold()
    semantic = c169.semantic_context(*rows)
    input_roles = {
        plan.row_inputs[label]: c169.joint.pivot.five.ROW_ROLE[row]
        for label, row in zip(("g1", "g2", "p"), rows, strict=True)
    }
    expected = {
        site: c169.resolve_spec_role(spec, semantic)
        for site, spec in plan.expected_specs.items()
    }
    failures = []
    checks = 0
    for target, role in expected.items():
        premise = {}
        for direction in c169.c53.DIRECTIONS:
            neighbor = add(target, direction)
            if neighbor in scaffold:
                premise[neighbor] = scaffold[neighbor]
            elif neighbor in input_roles:
                premise[neighbor] = input_roles[neighbor]
        premise.update(
            {
                parent: (
                    expected[parent]
                    if parent in expected
                    else input_roles[parent]
                )
                for parent in plan.dependencies[target]
            }
        )
        actual = c169.UNIFIED_RAW.get(
            c169.c53.local_signature(premise, target),
            frozenset(),
        )
        checks += 1
        if actual != frozenset((role,)):
            failures.append((target, role, actual, plan.dependencies[target]))
            if len(failures) >= 10:
                break
    return checks, tuple(failures), int(semantic[-1])


def local_with_roles(
    instance: Apparatus,
    target: Coord,
    *,
    dynamic_roles: dict[Coord, str],
    initial_roles: dict[Coord, str] | None = None,
) -> frozenset[str]:
    overrides = initial_roles or {}
    premise = {}
    for direction in c169.c53.DIRECTIONS:
        neighbor = add(target, direction)
        if neighbor in overrides:
            premise[neighbor] = overrides[neighbor]
        elif neighbor in instance.initial:
            premise[neighbor] = instance.initial[neighbor]
    premise.update(
        {
            parent: dynamic_roles[parent]
            for parent in instance.dependencies[target]
        }
    )
    return c169.UNIFIED_RAW.get(
        c169.c53.local_signature(premise, target),
        frozenset(),
    )


def path_role_check(
    instance: Apparatus,
    path: tuple[Coord, ...],
    role: str,
) -> tuple[int, tuple[object, ...]]:
    failures = []
    checks = 0
    for parent, target in zip(path, path[1:]):
        actual = local_with_roles(
            instance,
            target,
            dynamic_roles={parent: role},
        )
        checks += 1
        if actual != frozenset((role,)):
            failures.append((target, parent, role, actual))
            if len(failures) >= 10:
                break
    return checks, tuple(failures)


def exhaustive_factorized_semantics(
    hard: Apparatus,
) -> tuple[dict[str, object], tuple[object, ...]]:
    failures = []
    histogram: Counter[int] = Counter()
    patterns: Counter[tuple[int, ...]] = Counter()
    context_membership_mismatches = []
    for assignment in product((0, 1), repeat=len(OBSERVABLE_IDS)):
        semantics, bits = assignment_semantics(assignment)
        signs = dict(zip(OBSERVABLE_IDS, assignment, strict=True))
        reference_bits = tuple(
            int(
                (
                    signs[ids[0]]
                    ^ signs[ids[1]]
                    ^ signs[ids[2]]
                )
                == unsigned_sign
            )
            for _label, ids, unsigned_sign in EXPECTED_CONTEXTS
        )
        if bits != reference_bits:
            context_membership_mismatches.append((assignment, bits, reference_bits))
        histogram[sum(bits)] += 1
        patterns[bits] += 1
    if context_membership_mismatches:
        failures.append(("semantic-reference", context_membership_mismatches[:5]))

    context_checks = 0
    for label, ids, unsigned_sign in EXPECTED_CONTEXTS:
        for sign_triple in product((0, 1), repeat=3):
            rows = tuple(
                signed_measurement(measurement_id, sign)
                for measurement_id, sign in zip(ids, sign_triple, strict=True)
            )
            checks, local_failures, membership = fully_ported_semantic_check(rows)
            context_checks += checks
            reference = int(
                (sign_triple[0] ^ sign_triple[1] ^ sign_triple[2])
                == unsigned_sign
            )
            if local_failures or membership != reference:
                failures.append(
                    (
                        "context",
                        label,
                        sign_triple,
                        membership,
                        reference,
                        local_failures[:2],
                    )
                )
                if len(failures) >= 10:
                    break

    incoming, _first = input_paths()
    branch_checks = 0
    for measurement_id, occurrences in occurrence_map().items():
        splitter = hard.source_splitters[measurement_id]
        source = hard.source_sites[measurement_id]
        for sign_bit in (0, 1):
            role = c169.joint.pivot.five.ROW_ROLE[
                signed_measurement(measurement_id, sign_bit)
            ]
            splitter_actual = local_with_roles(
                hard,
                splitter,
                dynamic_roles={},
                initial_roles={source: role},
            )
            branch_checks += 1
            if splitter_actual != frozenset((role,)):
                failures.append(
                    ("splitter-role", measurement_id, sign_bit, splitter_actual)
                )
            for context_label, _port_role in occurrences:
                checks, path_failures = path_role_check(
                    hard,
                    incoming[(measurement_id, context_label)],
                    role,
                )
                branch_checks += checks
                if path_failures:
                    failures.append(
                        (
                            "input-path",
                            measurement_id,
                            context_label,
                            sign_bit,
                            path_failures[:2],
                        )
                    )

    output_sites = hard.context_outputs
    output_ports = {
        label: shifted(next(iter(fully_ported_plan().open_ports)), CONTEXT_SHIFTS[label])
        for label, _ids, _sign in EXPECTED_CONTEXTS
    }
    outgoing = context_output_paths(output_sites, output_ports)
    parity_targets, _endpoints, inter_paths = parity_geometry()
    h_path_checks = 0
    for path in (*outgoing, *inter_paths):
        for role in (H0, H1):
            checks, path_failures = path_role_check(hard, path, role)
            h_path_checks += checks
            if path_failures:
                failures.append(("h-path", path[0], role, path_failures[:2]))

    xor_checks = 0
    for target in parity_targets:
        left = add(target, EZ)
        right = add(target, EX)
        for left_bit, right_bit in product((0, 1), repeat=2):
            wanted = c169.bit(left_bit ^ right_bit)
            actual = local_with_roles(
                hard,
                target,
                dynamic_roles={
                    left: c169.bit(left_bit),
                    right: c169.bit(right_bit),
                },
            )
            xor_checks += 1
            if actual != frozenset((wanted,)):
                failures.append(
                    ("xor", target, left_bit, right_bit, wanted, actual)
                )

    return (
        {
            "assignments": 512,
            "histogram": histogram,
            "patterns": len(patterns),
            "context_checks": context_checks,
            "branch_checks": branch_checks,
            "h_path_checks": h_path_checks,
            "xor_checks": xor_checks,
        },
        tuple(failures[:10]),
    )


REPRESENTATIVE_ASSIGNMENTS = {
    5: (0, 0, 0, 0, 0, 0, 0, 0, 0),
    3: (0, 0, 0, 0, 0, 0, 0, 1, 0),
    1: (0, 0, 0, 0, 1, 0, 1, 0, 0),
}


def resolve_expected(
    assignment: tuple[int, ...],
) -> tuple[dict[Coord, str], tuple[int, ...]]:
    semantics, context_bits = assignment_semantics(assignment)
    signs = dict(zip(OBSERVABLE_IDS, assignment, strict=True))
    plan = fully_ported_plan()
    expected: dict[Coord, str] = {}

    for label, _ids, _unsigned_sign in EXPECTED_CONTEXTS:
        shift = CONTEXT_SHIFTS[label]
        semantic = semantics[label]
        for local_site, spec in plan.expected_specs.items():
            expected[shifted(local_site, shift)] = c169.resolve_spec_role(
                spec,
                semantic,
            )

    incoming, _first = input_paths()
    for measurement_id in OBSERVABLE_IDS:
        role = c169.joint.pivot.five.ROW_ROLE[
            signed_measurement(measurement_id, signs[measurement_id])
        ]
        expected[source_geometry()[1][measurement_id]] = role
        for context_label, _port_role in occurrence_map()[measurement_id]:
            for site in incoming[(measurement_id, context_label)][1:]:
                expected[site] = role

    output_sites = {
        label: shifted(plan.output_site, CONTEXT_SHIFTS[label])
        for label, _ids, _sign in EXPECTED_CONTEXTS
    }
    output_ports = {
        label: shifted(next(iter(plan.open_ports)), CONTEXT_SHIFTS[label])
        for label, _ids, _sign in EXPECTED_CONTEXTS
    }
    outgoing = context_output_paths(output_sites, output_ports)
    for bit, path in zip(context_bits, outgoing, strict=True):
        role = c169.bit(bit)
        for site in path[1:]:
            expected[site] = role

    targets, _endpoints, inter_paths = parity_geometry()
    cumulative = context_bits[0] ^ context_bits[1]
    expected[targets[0]] = c169.bit(cumulative)
    for index, path in enumerate(inter_paths):
        role = c169.bit(cumulative)
        for site in path[1:]:
            expected[site] = role
        cumulative ^= context_bits[index + 2]
        expected[targets[index + 1]] = c169.bit(cumulative)
    return expected, context_bits


@lru_cache(maxsize=2)
def global_schedule(order: str) -> tuple[Coord, ...]:
    return c173.schedule(apparatus(REPRESENTATIVE_ASSIGNMENTS[5]).dependencies, order)


@lru_cache(maxsize=1)
def global_children() -> dict[Coord, tuple[Coord, ...]]:
    return c173.children_map(apparatus(REPRESENTATIVE_ASSIGNMENTS[5]).dependencies)


def role_lookup(
    records: RecordView,
    target: Coord,
    rotation=None,
) -> frozenset[str]:
    signature = c169.c53.local_signature(records, target)
    if rotation is not None:
        signature = c169.c53.rotate_signature(signature, rotation)
    return c169.UNIFIED_RAW.get(signature, frozenset())


def physical_run(
    hard: Apparatus,
    assignment: tuple[int, ...],
    *,
    order: str,
    rotation=None,
) -> tuple[bool, object]:
    expected, context_bits = (
        (hard.expected, hard.context_bits)
        if assignment == hard.assignment
        else resolve_expected(assignment)
    )
    if set(expected) != set(hard.dependencies):
        return False, (
            "expected-domain",
            len(expected),
            len(hard.dependencies),
            tuple(sorted(set(expected) - set(hard.dependencies)))[:3],
            tuple(sorted(set(hard.dependencies) - set(expected)))[:3],
        )
    signs = dict(zip(OBSERVABLE_IDS, assignment, strict=True))
    source_overrides = {
        hard.source_sites[measurement_id]: c169.joint.pivot.five.ROW_ROLE[
            signed_measurement(measurement_id, signs[measurement_id])
        ]
        for measurement_id in OBSERVABLE_IDS
    }
    records = RecordView(hard.initial, overrides=source_overrides)
    actual = {
        splitter: frozenset((expected[splitter],))
        for splitter in hard.source_splitters.values()
    }
    if rotation is not None:
        rotated_roots = {
            splitter: role_lookup(records, splitter, rotation)
            for splitter in hard.source_splitters.values()
        }
        if rotated_roots != actual:
            return False, ("rotated-initial-roots", rotated_roots, actual)

    linear = global_schedule(order)
    children = global_children()
    pending = {
        site: len(parents)
        for site, parents in hard.dependencies.items()
    }
    frontier = {
        site for site, count in pending.items() if count == 0
    }
    work = 0
    maximum = 0
    for step, target in enumerate(linear):
        wanted = {
            site: frozenset((expected[site],))
            for site in frontier
        }
        work += len(frontier)
        maximum = max(maximum, len(frontier))
        if actual != wanted:
            return False, (
                "frontier",
                step,
                len(actual),
                len(wanted),
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
            values = role_lookup(records, candidate, rotation)
            if values:
                actual[candidate] = values
            else:
                actual.pop(candidate, None)

    observed = tuple(
        int(records[hard.context_outputs[label]] == H1)
        for label, _ids, _sign in EXPECTED_CONTEXTS
    )
    return (
        not actual
        and observed == context_bits
        and records[hard.parity_terminal] == H1,
        {
            "assignment": assignment,
            "context_bits": context_bits,
            "formed": len(expected),
            "work": work,
            "maximum": maximum,
            "parity": records[hard.parity_terminal],
            "residual": tuple(sorted(actual.items())),
            "rotation": rotation is not None,
        },
    )


def isolated_context_initial_scan() -> tuple[int, tuple[object, ...]]:
    plan = fully_ported_plan()
    scaffold, _ports, _removable = fully_ported_scaffold()
    rows = (
        signed_measurement(11, 0),
        signed_measurement(2, 0),
        signed_measurement(14, 0),
    )
    records = dict(scaffold)
    for label, row in zip(("g1", "g2", "p"), rows, strict=True):
        records[plan.row_inputs[label]] = c169.joint.pivot.five.ROW_ROLE[row]
    actual = c173.enabled(records)
    roots = {
        add(plan.row_inputs[label], EX): frozenset(
            (c169.joint.pivot.five.ROW_ROLE[row],)
        )
        for label, row in zip(("g1", "g2", "p"), rows, strict=True)
    }
    failures = () if actual == roots else (
        (
            tuple(sorted(set(actual) - set(roots)))[:5],
            tuple(sorted(set(roots) - set(actual)))[:5],
        ),
    )
    return len(actual), failures


def interface_initial_scan(
    hard: Apparatus,
) -> tuple[int, int, tuple[object, ...]]:
    radius_one = set(hard.interface_sites)
    radius_one.update(
        add(site, direction)
        for site in tuple(radius_one)
        for direction in c169.c53.DIRECTIONS
    )
    radius_two = set(radius_one)
    radius_two.update(
        add(site, direction)
        for site in tuple(radius_one)
        for direction in c169.c53.DIRECTIONS
    )
    candidates = {
        site
        for site in radius_two
        if site not in hard.initial
        and any(
            add(site, direction) in hard.initial
            for direction in c169.c53.DIRECTIONS
        )
    }
    records = RecordView(hard.initial)
    actual = {
        site: values
        for site in candidates
        if (values := role_lookup(records, site))
    }
    wanted = {
        splitter: frozenset((hard.expected[splitter],))
        for splitter in hard.source_splitters.values()
    }
    failures = () if actual == wanted else (
        (
            tuple(sorted(set(actual) - set(wanted)))[:5],
            tuple(sorted(set(wanted) - set(actual)))[:5],
        ),
    )
    return len(candidates), len(actual), failures


def source_and_branch_deletion_checks(
    hard: Apparatus,
) -> tuple[dict[str, object], tuple[object, ...], dict[tuple[int, str], Coord]]:
    failures = []
    source_reach = {}
    branch_reach = {}
    guards = {}
    source_attempts = 0
    branch_attempts = 0
    context_output_set = set(hard.context_outputs.values())

    for measurement_id in OBSERVABLE_IDS:
        source = hard.source_sites[measurement_id]
        splitter = hard.source_splitters[measurement_id]
        premise = formation_records(
            hard.initial,
            hard.expected,
            hard.dependencies,
            splitter,
        )
        trial = dict(premise)
        trial.pop(source, None)
        actual = c169.UNIFIED_RAW.get(
            c169.c53.local_signature(trial, splitter),
            frozenset(),
        )
        source_attempts += 1
        if hard.expected[splitter] in actual:
            failures.append(("source-survives", measurement_id, actual))

        killed = c173.descendants(hard.dependencies, {splitter})
        observed_contexts = tuple(
            label
            for label, output in hard.context_outputs.items()
            if output in killed
        )
        wanted_contexts = tuple(
            label for label, _port_role in occurrence_map()[measurement_id]
        )
        source_reach[measurement_id] = (
            observed_contexts,
            hard.parity_terminal in killed,
            len(killed),
        )
        if set(observed_contexts) != set(wanted_contexts) or hard.parity_terminal not in killed:
            failures.append(
                (
                    "source-reach",
                    measurement_id,
                    observed_contexts,
                    wanted_contexts,
                )
            )

        branch_descendants = []
        for context_label, _port_role in occurrence_map()[measurement_id]:
            first = hard.branch_first[(measurement_id, context_label)]
            killed_branch = c173.descendants(hard.dependencies, {first})
            branch_descendants.append(killed_branch)
            observed = tuple(
                label
                for label, output in hard.context_outputs.items()
                if output in killed_branch
            )
            branch_reach[(measurement_id, context_label)] = (
                observed,
                hard.parity_terminal in killed_branch,
                len(killed_branch),
            )
            if observed != (context_label,) or hard.parity_terminal not in killed_branch:
                failures.append(
                    (
                        "branch-reach",
                        measurement_id,
                        context_label,
                        observed,
                    )
                )
            guard = c173.unique_fixed_guard(
                hard.initial,
                hard.expected,
                hard.dependencies,
                first,
                frozenset((splitter,)),
            )
            guards[(measurement_id, context_label)] = guard
            branch_premise = formation_records(
                hard.initial,
                hard.expected,
                hard.dependencies,
                first,
            )
            shortened = dict(branch_premise)
            shortened.pop(guard, None)
            branch_actual = c169.UNIFIED_RAW.get(
                c169.c53.local_signature(shortened, first),
                frozenset(),
            )
            branch_attempts += 1
            if hard.expected[first] in branch_actual:
                failures.append(
                    (
                        "branch-guard-survives",
                        measurement_id,
                        context_label,
                        guard,
                        branch_actual,
                    )
                )
        intersection = branch_descendants[0] & branch_descendants[1]
        if intersection & context_output_set:
            failures.append(
                (
                    "branches-rejoin-before-parity",
                    measurement_id,
                    tuple(sorted(intersection & context_output_set)),
                )
            )

    return (
        {
            "source_attempts": source_attempts,
            "branch_attempts": branch_attempts,
            "source_reach": source_reach,
            "branch_reach": branch_reach,
        },
        tuple(failures[:10]),
        guards,
    )


def dynamic_edge_checks(
    hard: Apparatus,
) -> tuple[int, tuple[object, ...]]:
    failures = []
    attempts = 0
    for target, parents in hard.dependencies.items():
        premise = formation_records(
            hard.initial,
            hard.expected,
            hard.dependencies,
            target,
        )
        wanted = hard.expected[target]
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


def covariance_templates(
    hard: Apparatus,
) -> tuple[dict[str, int], tuple[object, ...]]:
    templates: Counter[tuple[object, str]] = Counter()
    for target, role in hard.expected.items():
        premise = formation_records(
            hard.initial,
            hard.expected,
            hard.dependencies,
            target,
        )
        signature = c169.c53.local_signature(premise, target)
        templates[(signature, role)] += 1

    failures = []
    checks = 0
    for (signature, role), _multiplicity in templates.items():
        for rotation_index, rotation in enumerate(c169.c53.ROTATIONS):
            actual = c169.UNIFIED_RAW.get(
                c169.c53.rotate_signature(signature, rotation),
                frozenset(),
            )
            checks += 1
            if actual != frozenset((role,)):
                failures.append(
                    (rotation_index, signature, role, actual)
                )
                if len(failures) >= 10:
                    break
    direction_failures = []
    direction_set = set(c169.c53.DIRECTIONS)
    for rotation_index, rotation in enumerate(c169.c53.ROTATIONS):
        images = {
            c169.c53.matvec(rotation, direction)
            for direction in c169.c53.DIRECTIONS
        }
        if images != direction_set:
            direction_failures.append((rotation_index, images))
    failures.extend(direction_failures[:10])
    return (
        {
            "templates": len(templates),
            "template_checks": checks,
            "covered_site_checks": 24 * len(hard.expected),
            "rotations": len(c169.c53.ROTATIONS),
        },
        tuple(failures[:10]),
    )


def pruned_physical_run(
    hard: Apparatus,
    *,
    removed_initial: Coord,
    cut: Coord,
    wanted_context_presence: tuple[bool, ...],
) -> tuple[bool, object]:
    removed = c173.descendants(hard.dependencies, {cut})
    expected = {
        site: role
        for site, role in hard.expected.items()
        if site not in removed
    }
    dependencies = {
        site: parents
        for site, parents in hard.dependencies.items()
        if site not in removed
    }
    if any(not parents <= expected.keys() for parents in dependencies.values()):
        return False, ("uncollapsed-descendant-cut", cut)

    records = RecordView(
        hard.initial,
        removed=frozenset((removed_initial,)),
    )
    actual = {
        site: frozenset((expected[site],))
        for site, parents in dependencies.items()
        if not parents
    }
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
        values = role_lookup(records, candidate)
        if values:
            actual[candidate] = values
        else:
            actual.pop(candidate, None)

    linear = c173.schedule(dependencies, "min")
    children = c173.children_map(dependencies)
    pending = {
        site: len(parents)
        for site, parents in dependencies.items()
    }
    frontier = {
        site for site, count in pending.items() if count == 0
    }
    maximum = 0
    work = 0
    for step, target in enumerate(linear):
        wanted = {
            site: frozenset((expected[site],))
            for site in frontier
        }
        work += len(frontier)
        maximum = max(maximum, len(frontier))
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
            values = role_lookup(records, candidate)
            if values:
                actual[candidate] = values
            else:
                actual.pop(candidate, None)

    observed_presence = tuple(
        output in records
        for _label, output in hard.context_outputs.items()
    )
    return (
        not actual
        and observed_presence == wanted_context_presence
        and hard.parity_terminal not in records,
        {
            "removed_dynamic": len(removed),
            "remaining_dynamic": len(expected),
            "observed_context_presence": observed_presence,
            "work": work,
            "maximum": maximum,
            "parity_present": hard.parity_terminal in records,
            "residual": tuple(sorted(actual.items())),
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("FROZEN AUTHORITY")
    observed = {path: sha256(path) for path in FROZEN}
    check(
        "Cycle 173 runner, port contract, and note remain frozen",
        observed == FROZEN,
        {path.name: value for path, value in observed.items()},
    )
    check(
        "Cycle 168 exact six contexts remain selected",
        contexts_from_cycle168() == EXPECTED_CONTEXTS,
        contexts_from_cycle168(),
    )

    print("\nFULLY PORTED SINGLE CONTEXT")
    plan = fully_ported_plan()
    scaffold, ports, removable = fully_ported_scaffold()
    check(
        "g1, g2, and P are all external whole-row ports",
        not plan.fixed.keys() & plan.row_inputs.values()
        and not plan.expected_specs.keys() & plan.row_inputs.values()
        and plan.leaf_counts == {"g1": 6, "g2": 6, "p": 15},
        (plan.row_inputs, plan.leaf_counts),
    )
    check(
        "fully porting both generators adds no raw-law row or conflict",
        len(c169.MEMBERSHIP_RAW) == 99_212
        and not c169.MEMBERSHIP_CONFLICTS
        and len(c169.UNIFIED_RAW) == 101_708
        and not c169.UNIFIED_CONFLICTS,
        (
            len(c169.MEMBERSHIP_RAW),
            len(c169.UNIFIED_RAW),
            len(scaffold),
            len(ports),
            len(removable),
        ),
    )
    representative_rows = (
        signed_measurement(11, 0),
        signed_measurement(2, 0),
        signed_measurement(14, 0),
    )
    representative = context_instance(
        "R1",
        representative_rows,
        (0, 0, 0),
        supply_inputs=True,
    )
    checks, failures = local_compiled_check(representative)
    check(
        "one fully ported R1 context compiles locally",
        not failures and representative.membership == 1,
        (checks, failures, representative.membership),
    )

    print("\nNINE-SOURCE / SIX-CONTEXT COMMON APPARATUS")
    hard = apparatus((0,) * len(OBSERVABLE_IDS))
    global_checks, global_failures = global_local_compiled_check(hard)
    check(
        "nine literal sources feed six physical context terminals",
        len(hard.source_sites) == 9
        and len(hard.branch_first) == 18
        and len(hard.context_outputs) == 6
        and hard.context_bits == (1, 1, 1, 1, 1, 0),
        {
            "sources": len(hard.source_sites),
            "branches": len(hard.branch_first),
            "context_bits": hard.context_bits,
        },
    )
    check(
        "the complete five-of-six representative compiles locally",
        not global_failures
        and hard.expected[hard.parity_terminal] == H1,
        (global_checks, global_failures, hard.expected[hard.parity_terminal]),
    )

    print("\nALL-512 COMMON-GEOMETRY FACTORIZED SEMANTICS")
    semantic_accounting, semantic_failures = exhaustive_factorized_semantics(hard)
    check(
        "all 512 shared-sign assignments close on one factored physical geometry",
        not semantic_failures
        and semantic_accounting["histogram"]
        == Counter({1: 96, 3: 320, 5: 96})
        and semantic_accounting["patterns"] == 32,
        (semantic_accounting, semantic_failures),
    )

    print("\nINITIAL-STATE FIREWALL")
    isolated_enabled, isolated_failures = isolated_context_initial_scan()
    interface_candidates, interface_enabled, interface_failures = interface_initial_scan(hard)
    check(
        "one isolated fully ported context enables only its three comb roots",
        isolated_enabled == 3 and not isolated_failures,
        (isolated_enabled, isolated_failures),
    )
    check(
        "the complete interface neighborhood enables only nine source splitters",
        interface_enabled == 9 and not interface_failures,
        (interface_candidates, interface_enabled, interface_failures),
    )

    print("\nREPRESENTATIVE FULL PHYSICAL REPLAYS")
    physical_results = {
        (5, "min"): physical_run(
            hard,
            REPRESENTATIVE_ASSIGNMENTS[5],
            order="min",
        ),
        (3, "max"): physical_run(
            hard,
            REPRESENTATIVE_ASSIGNMENTS[3],
            order="max",
        ),
        (1, "min"): physical_run(
            hard,
            REPRESENTATIVE_ASSIGNMENTS[1],
            order="min",
        ),
    }
    check(
        "one-, three-, and five-context representatives replay physically",
        all(result[0] for result in physical_results.values()),
        physical_results,
    )

    print("\nSOURCE / BRANCH DELETION REACH")
    deletion_accounting, deletion_failures, branch_guards = (
        source_and_branch_deletion_checks(hard)
    )
    check(
        "all nine sources and eighteen fork guards have exact causal reach",
        not deletion_failures
        and deletion_accounting["source_attempts"] == 9
        and deletion_accounting["branch_attempts"] == 18
        and len(branch_guards) == 18,
        (deletion_accounting, deletion_failures, branch_guards),
    )
    source_cut = pruned_physical_run(
        hard,
        removed_initial=hard.source_sites[11],
        cut=hard.source_splitters[11],
        wanted_context_presence=(False, True, True, False, True, True),
    )
    branch_cut = pruned_physical_run(
        hard,
        removed_initial=branch_guards[(11, "R1")],
        cut=hard.branch_first[(11, "R1")],
        wanted_context_presence=(False, True, True, True, True, True),
    )
    check(
        "representative source and fork cuts replay with exact surviving contexts",
        source_cut[0] and branch_cut[0],
        {"source": source_cut, "branch": branch_cut},
    )

    print("\nDYNAMIC EDGE LOAD")
    edge_attempts, edge_failures = dynamic_edge_checks(hard)
    check(
        "every declared dynamic edge is load-bearing",
        edge_attempts == sum(map(len, hard.dependencies.values()))
        and not edge_failures,
        (edge_attempts, edge_failures),
    )

    print("\nPROPER-CUBIC COVARIANCE")
    covariance_accounting, covariance_failures = covariance_templates(hard)
    check(
        "all 24 proper-cubic images compile by exact local templates",
        not covariance_failures
        and covariance_accounting["covered_site_checks"]
        == 24 * len(hard.expected),
        (covariance_accounting, covariance_failures),
    )
    rotated_physical = physical_run(
        hard,
        REPRESENTATIVE_ASSIGNMENTS[3],
        order="min",
        rotation=c169.c53.ROTATIONS[5],
    )
    check(
        "one nonidentity proper-cubic presentation replays physically",
        rotated_physical[0],
        rotated_physical,
    )

    print("\nSCOPE")
    note_text = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    normalized = " ".join(note_text.lower().split())
    required_phrases = (
        "extensional m2 signed-row role labels",
        "not physical qubit discrimination or copying",
        "not yet a physical contextuality certificate",
        "not a no-classical-memory theorem",
        "not an instrument-equivalence theorem",
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
    missing_scope = tuple(
        phrase for phrase in required_phrases
        if phrase not in normalized
    )
    check(
        "the Cycle-177 note preserves the role-label and operational firewall",
        not missing_scope,
        missing_scope,
    )

    print("\nACCOUNTING")
    print("PLAN", len(plan.expected_specs), len(plan.path_groups), plan.leaf_counts)
    print("SCAFFOLD", len(scaffold), len(ports), len(removable))
    print(
        "GLOBAL",
        len(hard.initial),
        len(hard.expected),
        sum(map(len, hard.dependencies.values())),
        global_checks,
    )
    print("SEMANTICS", semantic_accounting)
    print("PHYSICAL", physical_results)
    print("DELETIONS", deletion_accounting)
    print("PRUNED", source_cut, branch_cut)
    print("EDGES", edge_attempts)
    print("COVARIANCE", covariance_accounting)
    print("ROTATED_PHYSICAL", rotated_physical)
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "CYCLE177_COMMON_APPARATUS_GREEN" if FAIL == 0 else "CYCLE177_OPEN")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
