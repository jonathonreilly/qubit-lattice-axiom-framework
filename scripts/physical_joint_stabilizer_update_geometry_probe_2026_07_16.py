#!/usr/bin/env python3
"""Compose the retained physical stabilizer-update atoms in one geometry."""

from __future__ import annotations

from collections import defaultdict
from functools import lru_cache

import physical_row_reader_payload_tap_probe_2026_07_16 as tap
import physical_three_row_spacious_isolated_pivot_probe_2026_07_15 as control


mux = tap.prior.prior
transport = mux.transport
pivot = control.pivot
mult = mux.pivot.mult
cable = mux.cable
cell = mux.cell
c53 = mux.c53
FRAME = mux.FRAME
GUIDE = mux.GUIDE
Coord = tuple[int, int, int]
Signature = c53.Signature


MULTIPLIER_SHIFT = (0, 600, 100)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def moved(site: Coord, rotation, shift: Coord) -> Coord:
    return add(c53.matvec(rotation, site), shift)


def transform_records(records: dict[Coord, str], rotation, shift: Coord):
    return {
        moved(site, rotation, shift): role
        for site, role in records.items()
    }


def place(records: dict[Coord, str], site: Coord, role: str, label: str = "") -> None:
    previous = records.get(site)
    if previous is not None and previous != role:
        raise ValueError(("placement-conflict", label, site, previous, role))
    records[site] = role


def line_to(path: list[Coord], target: Coord, axes=(0, 1, 2)) -> None:
    current = list(path[-1])
    for axis in axes:
        while current[axis] != target[axis]:
            current[axis] += 1 if target[axis] > current[axis] else -1
            point = tuple(current)  # type: ignore[assignment]
            if point in path:
                raise ValueError(("path-self-contact", point, target))
            path.append(point)


# A tap has only one open face after it forms.  This generic relational splitter
# converts that single derived row into a row record with two open transverse
# output faces.  It adds no onsite role and is shared by all 32 physical rows.
SPLITTER_INPUT = (0, 0, -1)
SPLITTER_OUTPUTS = ((1, 0, 0), (-1, 0, 0))
SPLITTER_FIXED = {
    (0, 1, 0): GUIDE,
    (0, -1, 0): FRAME,
    (0, 0, 1): FRAME,
}


def splitter_local(row_role: str) -> Signature:
    records = {SPLITTER_INPUT: row_role, **SPLITTER_FIXED}
    return c53.canonical_signature(c53.local_signature(records, (0, 0, 0)))


SPLITTER_TABLE = {
    splitter_local(row_role): row_role
    for row_role in mux.ROW_ROLES
}
SPLITTER_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in SPLITTER_TABLE.items()
))
MERGED_RAW = cell.merge_raw(tap.MERGED_RAW, SPLITTER_RAW)
RAW_CONFLICTS = {
    signature: outputs
    for signature, outputs in MERGED_RAW.items()
    if len(outputs) != 1
}


INTEGRATED_CASE_DIRECTION = (0, -1, 0)
INTEGRATED_BRANCHES = (
    (
        (1, 0, 0),
        (2, 0, 0),
        {
            (1, 1, 0): pivot.ROUTER_MARKER,
            (1, -1, 0): FRAME,
            (1, 0, -1): FRAME,
        },
    ),
    (
        (-1, 0, 0),
        (-2, 0, 0),
        {
            (-1, 1, 0): GUIDE,
            (-1, -1, 0): FRAME,
            (-1, 0, -1): FRAME,
        },
    ),
    (
        (0, 1, 0),
        (0, 2, 0),
        {
            (1, 1, 0): pivot.ROUTER_MARKER,
            (-1, 1, 0): GUIDE,
            (0, 1, -1): FRAME,
        },
    ),
)


@lru_cache(maxsize=None)
def integrated_local(count: int):
    if count not in (2, 3):
        raise ValueError(count)
    zero_role = pivot.five.ROW_ROLE[(0, 0, 0, 0, 0)]
    fixed = {
        (0, 0, 1): GUIDE,
        (0, 0, -1): FRAME if count == 2 else pivot.ROUTER_MARKER,
    }
    for _target, _bus, guards in INTEGRATED_BRANCHES[:count]:
        for site, role in guards.items():
            place(fixed, site, role, "integrated-local-guard")
    case_path = tuple((0, -depth, 0) for depth in range(8, 0, -1))
    output_paths = tuple(
        (
            target,
            add(target, (0, 0, 1)),
            add(target, (0, 0, 2)),
            add(target, (0, 0, 3)),
        )
        for target, _bus, _guards in INTEGRATED_BRANCHES[:count]
    )
    items = (
        (pivot.CASE_ROLE[(0, 0)], case_path),
        *((zero_role, path) for path in output_paths),
    )
    dynamic = {
        (0, 0, 0),
        *(site for _value, path in items for site in path),
        *(bus for _target, bus, _guards in INTEGRATED_BRANCHES[:count]),
    }
    chosen, _outputs, ports = cable.multi_path_core(
        items,
        constraints=fixed,
        extra_protected=frozenset(dynamic),
    )
    wanted_ports = {
        (0, 0, 0),
        *(add(path[-1], cable.terminal_direction(path)) for path in output_paths),
    }
    if set(ports) != wanted_ports:
        raise ValueError(("wrong-integrated-local-ports", count, ports, wanted_ports))
    structural = {
        site: role
        for site, role in chosen.items()
        if site not in dynamic
    }
    return structural, case_path, output_paths


def integrated_selector_local(case_role: str, count: int) -> Signature:
    structural, _case_path, _output_paths = integrated_local(count)
    records = {
        **structural,
        INTEGRATED_CASE_DIRECTION: case_role,
    }
    return c53.canonical_signature(c53.local_signature(records, (0, 0, 0)))


INTEGRATED_SELECTOR_TABLE = {}
for case, case_role in pivot.CASE_ROLE.items():
    for lane_index, count in enumerate((2, 3)):
        signature = integrated_selector_local(case_role, count)
        output = pivot.LANE_OUTPUT[case][lane_index]
        previous = INTEGRATED_SELECTOR_TABLE.get(signature)
        if previous is not None and previous != output:
            raise ValueError(("integrated-selector-conflict", case, previous, output))
        INTEGRATED_SELECTOR_TABLE[signature] = output


def integrated_gate_local(
    selector: str,
    row_role: str,
    branch_index: int,
    count: int,
) -> Signature:
    structural, _case_path, _output_paths = integrated_local(count)
    target, bus, _guards = INTEGRATED_BRANCHES[branch_index]
    records = {
        **structural,
        (0, 0, 0): selector,
        bus: row_role,
    }
    return c53.canonical_signature(c53.local_signature(records, target))


INTEGRATED_GATE_TABLE = {}
for selector, branch_index, count in (
    (pivot.SEL_L1_G1, 0, 2),
    (pivot.SEL_L1_P, 1, 2),
    (pivot.SEL_L2_G2, 0, 3),
    (pivot.SEL_L2_P, 1, 3),
    (pivot.SEL_L2_PRODUCT, 2, 3),
):
    for row_role in mux.ROW_ROLES:
        signature = integrated_gate_local(
            selector,
            row_role,
            branch_index,
            count,
        )
        previous = INTEGRATED_GATE_TABLE.get(signature)
        if previous is not None and previous != row_role:
            raise ValueError(("integrated-gate-conflict", selector, previous, row_role))
        INTEGRATED_GATE_TABLE[signature] = row_role


INTEGRATED_SELECTOR_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in INTEGRATED_SELECTOR_TABLE.items()
))
INTEGRATED_GATE_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in INTEGRATED_GATE_TABLE.items()
))
MERGED_RAW = cell.merge_raw(
    tap.MERGED_RAW,
    SPLITTER_RAW,
    INTEGRATED_SELECTOR_RAW,
    INTEGRATED_GATE_RAW,
)
RAW_CONFLICTS = {
    signature: outputs
    for signature, outputs in MERGED_RAW.items()
    if len(outputs) != 1
}


def source_sites():
    centers = (
        *control.bound.GENERATOR_CENTERS,
        control.bound.MEASURED_CENTER,
    )
    taps = tuple(add(center, tap.TAP) for center in centers)
    splitters = tuple(add(site, (0, 0, 10)) for site in taps)
    trunks = tuple(
        tuple(add(site, (0, 0, depth)) for depth in range(10))
        for site in taps
    )
    return centers, taps, splitters, trunks


SOURCE_CENTERS, TAP_SITES, SPLITTER_SITES, TAP_TRUNK_PATHS = source_sites()


def mux_geometry():
    lane1 = (-160, 800, 0)
    lane2 = (160, 800, 0)
    result = {}
    for label, selector, count in (
        ("lane1", lane1, 2),
        ("lane2", lane2, 3),
    ):
        _structural, _case_tail, local_stems = integrated_local(count)
        targets = tuple(
            add(selector, target)
            for target, _bus, _guards in INTEGRATED_BRANCHES[:count]
        )
        buses = tuple(
            add(selector, bus)
            for _target, bus, _guards in INTEGRATED_BRANCHES[:count]
        )
        stems = tuple(
            tuple(add(selector, site) for site in path)
            for path in local_stems
        )
        if label == "lane1":
            common = add(selector, (0, 70, 0))
            terminals = (
                add(common, (1, 0, 0)),
                add(common, (-1, 0, 0)),
            )
            preterminals = tuple(add(site, (0, -1, 0)) for site in terminals)
            paths = []
            first = list(stems[0])
            first.extend(
                add(targets[0], (0, 0, depth))
                for depth in range(4, 11)
            )
            line_to(first, (-100, 800, 10), (0,))
            line_to(first, (-100, 800, -80), (2,))
            line_to(first, (-100, 868, -80), (1,))
            line_to(first, (-159, 868, -80), (0,))
            line_to(first, (-159, 850, -80), (1,))
            line_to(first, (-159, 850, 0), (2,))
            line_to(first, preterminals[0], (1,))
            paths.append(tuple(first))
            second = list(stems[1])
            second.extend(
                add(targets[1], (0, 0, depth))
                for depth in range(4, 16)
            )
            line_to(second, (-220, 800, 15), (0,))
            line_to(second, (-220, 800, -100), (2,))
            line_to(second, (-220, 868, -100), (1,))
            line_to(second, (-161, 868, -100), (0,))
            line_to(second, (-161, 840, -100), (1,))
            line_to(second, (-161, 840, 0), (2,))
            line_to(second, preterminals[1], (1,))
            paths.append(tuple(second))
        else:
            common = add(selector, (0, 0, 80))
            terminals = (
                add(common, (1, 0, 0)),
                add(common, (-1, 0, 0)),
                add(common, (0, 0, 1)),
            )
            preterminals = (
                add(terminals[0], (0, -1, 0)),
                add(terminals[1], (0, -1, 0)),
                add(terminals[2], (0, 1, 0)),
            )
            paths = []
            first = list(stems[0])
            first.extend(
                add(targets[0], (0, 0, depth))
                for depth in range(4, 11)
            )
            line_to(first, (220, 800, 10), (0,))
            line_to(first, (220, 740, 10), (1,))
            line_to(first, (220, 740, 80), (2,))
            line_to(first, (220, 798, 80), (1,))
            line_to(first, (161, 798, 80), (0,))
            first.append(preterminals[0])
            paths.append(tuple(first))
            second = list(stems[1])
            second.extend(
                add(targets[1], (0, 0, depth))
                for depth in range(4, 16)
            )
            line_to(second, (100, 800, 15), (0,))
            line_to(second, (100, 860, 15), (1,))
            line_to(second, (100, 860, 80), (2,))
            line_to(second, (100, 798, 80), (1,))
            line_to(second, (159, 798, 80), (0,))
            second.append(preterminals[1])
            paths.append(tuple(second))
            third = list(stems[2])
            third.extend(
                add(targets[2], (0, 0, depth))
                for depth in range(4, 21)
            )
            line_to(third, (240, 801, 20), (0,))
            line_to(third, (240, 700, 20), (1,))
            line_to(third, (240, 700, 81), (2,))
            line_to(third, (240, 802, 81), (1,))
            line_to(third, (160, 802, 81), (0,))
            third.append(preterminals[2])
            paths.append(tuple(third))
        result[label] = {
            "selector": selector,
            "count": count,
            "targets": targets,
            "buses": buses,
            "voids": (
                (add(selector, (0, 1, 0)),)
                if count == 2
                else ()
            ),
            "common": common,
            "terminals": terminals,
            "preterminals": preterminals,
            "paths": tuple(paths),
            "join_guide": add(common, (0, 1, 0)),
            "join_frame": add(common, (0, -1, 0)),
        }
    return result


MUX = mux_geometry()


def joint_case_paths():
    case_site = add(pivot.CASE_SITE, control.CONTROLLER_SHIFT)
    paths = []
    first = [case_site, add(pivot.LANE1, control.CONTROLLER_SHIFT)]
    line_to(first, (first[-1][0], first[-1][1], -200), (2,))
    line_to(first, (-160, first[-1][1], -200), (0,))
    line_to(first, (-160, 790, -200), (1,))
    line_to(first, (-160, 790, 0), (2,))
    line_to(first, (-160, 792, 0), (1,))
    first.extend((-160, y, 0) for y in range(793, 800))
    paths.append(tuple(first))

    second = [case_site, add(pivot.LANE2, control.CONTROLLER_SHIFT)]
    line_to(second, (0, 350, 0), (1,))
    line_to(second, (20, 350, 0), (0,))
    line_to(second, (20, 350, 200), (2,))
    line_to(second, (160, 350, 200), (0,))
    line_to(second, (160, 790, 200), (1,))
    line_to(second, (160, 790, 0), (2,))
    line_to(second, (160, 792, 0), (1,))
    second.extend((160, y, 0) for y in range(793, 800))
    paths.append(tuple(second))

    terminals = tuple(
        add(path[-1], cable.terminal_direction(path))
        for path in paths
    )
    wanted = (MUX["lane1"]["selector"], MUX["lane2"]["selector"])
    if terminals != wanted:
        raise ValueError(("wrong-joint-case-terminals", terminals, wanted))
    return tuple(paths)


JOINT_CASE_PATHS = joint_case_paths()


def branch_path(start: Coord, first: Coord, waypoints, bus: Coord) -> tuple[Coord, ...]:
    path = [start, first]
    for target, axes in waypoints:
        line_to(path, target, axes)
    if path[-1] == bus:
        raise ValueError(("bus-entered-before-terminal", bus))
    path.append(bus)
    return tuple(path)


def payload_paths():
    g1_split, g2_split, p_split = SPLITTER_SITES
    lane1_buses = MUX["lane1"]["buses"]
    lane2_buses = MUX["lane2"]["buses"]
    left = add(mult.LEFT, MULTIPLIER_SHIFT)
    right = add(mult.RIGHT, MULTIPLIER_SHIFT)

    g1_mux = branch_path(
        g1_split,
        add(g1_split, (-1, 0, 0)),
        (
            ((-300, 0, 182), (0,)),
            ((-300, 0, 300), (2,)),
            ((-300, 500, 300), (1,)),
            ((-157, 500, 300), (0,)),
            ((-157, 780, 300), (1,)),
            ((-157, 780, 0), (2,)),
            ((-157, 800, 0), (1,)),
        ),
        lane1_buses[0],
    )
    g1_mult = branch_path(
        g1_split,
        add(g1_split, (1, 0, 0)),
        (
            ((-180, 0, 182), (0,)),
            ((-180, 0, 420), (2,)),
            ((-180, 600, 420), (1,)),
            ((0, 600, 420), (0,)),
            ((0, 600, 102), (2,)),
        ),
        left,
    )
    g2_mux = branch_path(
        g2_split,
        add(g2_split, (1, 0, 0)),
        (
            ((300, 0, 182), (0,)),
            ((300, 0, 340), (2,)),
            ((300, 480, 340), (1,)),
            ((163, 480, 340), (0,)),
            ((163, 780, 340), (1,)),
            ((163, 780, 0), (2,)),
            ((163, 800, 0), (1,)),
        ),
        lane2_buses[0],
    )
    g2_mult = branch_path(
        g2_split,
        add(g2_split, (-1, 0, 0)),
        (
            ((160, -60, 191), (0, 1)),
            ((160, -60, -300), (2,)),
            ((160, 600, -300), (1,)),
            ((0, 600, -300), (0,)),
            ((0, 600, 98), (2,)),
        ),
        right,
    )
    p_lane1 = branch_path(
        p_split,
        add(p_split, (-1, 0, 0)),
        (
            ((-1, 0, -100), (2,)),
            ((-320, 0, -100), (0,)),
            ((-320, 0, -400), (2,)),
            ((-320, 260, -400), (1,)),
            ((-163, 260, -400), (0,)),
            ((-163, 760, -400), (1,)),
            ((-163, 760, 0), (2,)),
            ((-163, 800, 0), (1,)),
        ),
        lane1_buses[1],
    )
    p_lane2 = branch_path(
        p_split,
        add(p_split, (1, 0, 0)),
        (
            ((1, 0, -100), (2,)),
            ((320, 0, -100), (0,)),
            ((320, 0, -360), (2,)),
            ((320, 250, -360), (1,)),
            ((157, 250, -360), (0,)),
            ((157, 760, -360), (1,)),
            ((157, 760, 0), (2,)),
            ((157, 800, 0), (1,)),
        ),
        lane2_buses[1],
    )
    return {
        "g1_mux": g1_mux,
        "g1_mult": g1_mult,
        "g2_mux": g2_mux,
        "g2_mult": g2_mult,
        "p_lane1": p_lane1,
        "p_lane2": p_lane2,
    }


PAYLOAD_PATHS = payload_paths()


def product_path() -> tuple[Coord, ...]:
    target = add(mult.TARGET, MULTIPLIER_SHIFT)
    bus = MUX["lane2"]["buses"][2]
    path = [target, add(target, (0, -1, 0)), add(target, (1, -1, 0))]
    line_to(path, (300, 599, 100), (0,))
    line_to(path, (300, 599, -150), (2,))
    line_to(path, (300, 803, -150), (1,))
    line_to(path, (160, 803, -150), (0,))
    line_to(path, (160, 803, 0), (2,))
    path.append(bus)
    return tuple(path)


PRODUCT_PATH = product_path()


CASE_REPRESENTATIVES = {
    (0, 0): (
        (0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0),
        (0, 0, 1, 1, 0),
    ),
    (0, 1): (
        (0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0),
        (0, 1, 0, 0, 0),
    ),
    (1, 0): (
        (0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0),
        (1, 0, 0, 0, 0),
    ),
    (1, 1): (
        (0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0),
        (1, 1, 0, 0, 0),
    ),
}


def base_uncaged(g1, g2, measured):
    records, expected, dependencies, results, _ports = (
        control.bound.uncaged_apparatus(g1, g2, measured)
    )
    case = pivot.pivot_rows(g1, g2, measured)[0]
    lane_outputs = pivot.LANE_OUTPUT[case]
    place(
        records,
        add(pivot.CASE_INPUTS["mark"], control.CONTROLLER_SHIFT),
        FRAME,
        "controller-case-mark",
    )
    place(
        records,
        add(pivot.CASE_INPUTS["start"], control.CONTROLLER_SHIFT),
        control.d.START_ROLE,
        "controller-case-start",
    )
    return records, expected, dependencies, results, case, lane_outputs


def add_splitters(records, expected, dependencies, rows):
    for center, tap_site, splitter, trunk, row in zip(
        SOURCE_CENTERS,
        TAP_SITES,
        SPLITTER_SITES,
        TAP_TRUNK_PATHS,
        rows,
        strict=True,
    ):
        row_role = pivot.five.ROW_ROLE[row]
        records.pop(tap_site, None)
        expected[tap_site] = row_role
        dependencies[tap_site] = frozenset()
        for previous, target in zip(trunk, trunk[1:]):
            expected[target] = row_role
            dependencies[target] = frozenset((previous,))
        expected[splitter] = row_role
        dependencies[splitter] = frozenset((trunk[-1],))
        local_shift = splitter
        for local_site, role in SPLITTER_FIXED.items():
            place(records, add(local_shift, local_site), role, "splitter-fixed")
        # SPLITTER_INPUT is occupied by the derived tap rather than fixed data.
        if add(splitter, SPLITTER_INPUT) != trunk[-1]:
            raise ValueError(("wrong-splitter-input", center, trunk[-1], splitter))


def add_terminal_fixed(
    records: dict[Coord, str],
    common: Coord,
    terminal: Coord,
    preterminal: Coord,
    label: str,
):
    rx = sub(common, terminal)
    rz = sub(preterminal, terminal)
    ry = cable.cross(rz, rx)

    def terminal_moved(vector: Coord) -> Coord:
        return tuple(
            vector[0] * rx[index]
            + vector[1] * ry[index]
            + vector[2] * rz[index]
            for index in range(3)
        )  # type: ignore[return-value]

    for local_direction, role in mux.TERMINAL_PATTERN.items():
        place(
            records,
            add(terminal, terminal_moved(local_direction)),
            role,
            f"{label}-terminal",
        )


def add_output_fixed(records, label: str):
    geometry = MUX[label]
    place(records, geometry["join_guide"], GUIDE, f"{label}-join")
    place(records, geometry["join_frame"], FRAME, f"{label}-join")
    for terminal, preterminal in zip(
        geometry["terminals"],
        geometry["preterminals"],
        strict=True,
    ):
        add_terminal_fixed(
            records,
            geometry["common"],
            terminal,
            preterminal,
            label,
        )


def add_integrated_fixed(records, label: str):
    geometry = MUX[label]
    structural, _case_tail, _output_stems = integrated_local(geometry["count"])
    for site, role in structural.items():
        place(
            records,
            add(geometry["selector"], site),
            role,
            f"{label}-integrated",
        )


def add_mux_expected(
    expected,
    dependencies,
    label: str,
    selector: str,
    candidate_roles,
):
    geometry = MUX[label]
    index = mux.SELECTOR_INDEX[selector]
    selected = candidate_roles[index]
    path = geometry["paths"][index]
    terminal = geometry["terminals"][index]
    common = geometry["common"]
    expected[path[0]] = selected
    dependencies[path[0]] = frozenset((
        geometry["selector"],
        geometry["buses"][index],
    ))
    for previous, target in zip(path, path[1:]):
        expected[target] = selected
        dependencies[target] = frozenset((previous,))
    expected[terminal] = selected
    dependencies[terminal] = frozenset((path[-1],))
    expected[common] = selected
    dependencies[common] = frozenset((terminal,))
    return selected


def grouped_routing_scaffold(items, fixed, protected):
    item_by_path = {path: (value, path) for value, path in items}
    bundle_paths = (
        (
            TAP_TRUNK_PATHS[0],
            PAYLOAD_PATHS["g1_mux"],
            PAYLOAD_PATHS["g1_mult"],
        ),
        (
            TAP_TRUNK_PATHS[1],
            PAYLOAD_PATHS["g2_mux"],
            PAYLOAD_PATHS["g2_mult"],
        ),
        (
            TAP_TRUNK_PATHS[2],
            PAYLOAD_PATHS["p_lane1"],
            PAYLOAD_PATHS["p_lane2"],
        ),
    )
    bundled = {path for group in bundle_paths for path in group}
    bundles = [
        tuple(item_by_path[path] for path in group)
        for group in bundle_paths
    ]
    by_source = defaultdict(list)
    for item in items:
        if item[1] in bundled:
            continue
        by_source[item[1][0]].append(item)
    groups = sorted(
        (*bundles, *(tuple(group) for group in by_source.values())),
        key=lambda group: (sum(len(path) for _value, path in group), group[0][1][0]),
    )
    placed = dict(fixed)
    terminal_ports = set()
    all_path_sites = {site for _value, path in items for site in path}
    protected = frozenset(set(protected) | all_path_sites)
    sources = {path[0] for _value, path in items}
    for group in groups:
        placed, _outputs, ports = cable.multi_path_core(
            group,
            constraints=placed,
            extra_protected=protected,
        )
        terminal_ports.update(ports)
    scaffold = {
        site: role
        for site, role in placed.items()
        if site not in fixed and site not in sources
    }
    return scaffold, frozenset(terminal_ports)


@lru_cache(maxsize=1)
def structural_scaffold():
    zero = (0, 0, 0, 0, 0)
    records, expected, dependencies, _results, _case, lane_outputs = base_uncaged(
        zero, zero, zero
    )
    add_splitters(records, expected, dependencies, (zero, zero, zero))
    zero_role = pivot.five.ROW_ROLE[zero]
    product_role = zero_role
    add_integrated_fixed(records, "lane1")
    add_integrated_fixed(records, "lane2")
    add_output_fixed(records, "lane1")
    add_output_fixed(records, "lane2")
    for site in mult.FRAMES:
        place(records, add(site, MULTIPLIER_SHIFT), mult.FRAME_ROLE, "multiplier")
    place(
        records,
        add(mult.PORT_FRAME, MULTIPLIER_SHIFT),
        mult.FRAME_ROLE,
        "multiplier-port",
    )

    case = pivot.pivot_rows(zero, zero, zero)[0]
    case_role = pivot.CASE_ROLE[case]
    selector_items = control.path_items(zero, zero, zero)[:2]
    items = (
        *selector_items,
        *((zero_role, path) for path in TAP_TRUNK_PATHS),
        *((case_role, path) for path in JOINT_CASE_PATHS),
        (zero_role, PAYLOAD_PATHS["g1_mux"]),
        (zero_role, PAYLOAD_PATHS["g1_mult"]),
        (zero_role, PAYLOAD_PATHS["g2_mux"]),
        (zero_role, PAYLOAD_PATHS["g2_mult"]),
        (zero_role, PAYLOAD_PATHS["p_lane1"]),
        (zero_role, PAYLOAD_PATHS["p_lane2"]),
        (product_role, PRODUCT_PATH),
        *((zero_role, path) for path in MUX["lane1"]["paths"]),
        *((zero_role, path) for path in MUX["lane2"]["paths"]),
    )
    dynamic = set(expected)
    dynamic.update(site for _value, path in items for site in path)
    dynamic.update({
        MUX["lane1"]["selector"],
        MUX["lane2"]["selector"],
        add(pivot.CASE_SITE, control.CONTROLLER_SHIFT),
        *MUX["lane1"]["buses"],
        *MUX["lane2"]["buses"],
        *MUX["lane1"]["targets"],
        *MUX["lane2"]["targets"],
        *MUX["lane1"]["voids"],
        *MUX["lane2"]["voids"],
        MUX["lane1"]["common"],
        MUX["lane2"]["common"],
        *MUX["lane1"]["terminals"],
        *MUX["lane2"]["terminals"],
        add(mult.TARGET, MULTIPLIER_SHIFT),
    })
    scaffold, ports = grouped_routing_scaffold(
        items,
        records,
        frozenset(dynamic),
    )
    required_ports = {
        *MUX["lane1"]["targets"],
        *MUX["lane2"]["targets"],
        MUX["lane1"]["selector"],
        MUX["lane2"]["selector"],
        add(pivot.CASE_SITE, control.CONTROLLER_SHIFT),
        *MUX["lane1"]["terminals"],
        *MUX["lane2"]["terminals"],
        add(mult.TARGET, MULTIPLIER_SHIFT),
    }
    if not required_ports <= set(ports):
        raise ValueError(("missing-joint-ports", required_ports - set(ports), ports))
    return scaffold, ports


@lru_cache(maxsize=None)
def apparatus(g1, g2, measured):
    if mult.algebra.symplectic(g1, g2):
        raise ValueError(("noncommuting-generators", g1, g2))
    records, expected, dependencies, results, case, lane_outputs = base_uncaged(
        g1, g2, measured
    )
    rows = (g1, g2, measured)
    add_splitters(records, expected, dependencies, rows)
    g1_role, g2_role, p_role = (
        pivot.five.ROW_ROLE[row] for row in rows
    )
    product_row = mult.algebra.multiply_commuting(g1, g2)
    product_role = pivot.five.ROW_ROLE[product_row]

    add_integrated_fixed(records, "lane1")
    add_integrated_fixed(records, "lane2")
    add_output_fixed(records, "lane1")
    add_output_fixed(records, "lane2")
    for site in mult.FRAMES:
        place(records, add(site, MULTIPLIER_SHIFT), mult.FRAME_ROLE, "multiplier")
    place(
        records,
        add(mult.PORT_FRAME, MULTIPLIER_SHIFT),
        mult.FRAME_ROLE,
        "multiplier-port",
    )
    scaffold, ports = structural_scaffold()
    for site, role in scaffold.items():
        place(records, site, role, "joint-routing")

    for value, path in control.path_items(g1, g2, measured)[:2]:
        for target in path[1:]:
            previous = expected.get(target)
            if previous is not None and previous != value:
                raise ValueError(("selector-input-overlap", target, previous, value))
            expected[target] = value
        for previous, target in zip(path, path[1:]):
            dependencies[target] = frozenset((previous,))

    case_site = add(pivot.CASE_SITE, control.CONTROLLER_SHIFT)
    case_role = pivot.CASE_ROLE[case]
    c_inputs = frozenset((
        add(pivot.CASE_INPUTS["c1"], control.CONTROLLER_SHIFT),
        add(pivot.CASE_INPUTS["c2"], control.CONTROLLER_SHIFT),
    ))
    expected[case_site] = case_role
    dependencies[case_site] = c_inputs
    for path in JOINT_CASE_PATHS:
        for target in path[1:]:
            previous = expected.get(target)
            if previous is not None and previous != case_role:
                raise ValueError(("case-path-overlap", target, previous, case_role))
            expected[target] = case_role
        for previous, target in zip(path, path[1:]):
            dependencies[target] = frozenset((previous,))
    for label, selector in zip(("lane1", "lane2"), lane_outputs, strict=True):
        site = MUX[label]["selector"]
        expected[site] = selector
        dependencies[site] = frozenset((JOINT_CASE_PATHS[0 if label == "lane1" else 1][-1],))

    path_values = {
        "g1_mux": g1_role,
        "g1_mult": g1_role,
        "g2_mux": g2_role,
        "g2_mult": g2_role,
        "p_lane1": p_role,
        "p_lane2": p_role,
    }
    for label, path in PAYLOAD_PATHS.items():
        value = path_values[label]
        for target in path[1:]:
            previous = expected.get(target)
            if previous is not None and previous != value:
                raise ValueError(("payload-overlap", label, target, previous, value))
            expected[target] = value
        for previous, target in zip(path, path[1:]):
            dependencies[target] = frozenset((previous,))

    target = add(mult.TARGET, MULTIPLIER_SHIFT)
    left = add(mult.LEFT, MULTIPLIER_SHIFT)
    right = add(mult.RIGHT, MULTIPLIER_SHIFT)
    expected[target] = product_role
    dependencies[target] = frozenset((left, right))
    for previous, output in zip(PRODUCT_PATH, PRODUCT_PATH[1:]):
        expected[output] = product_role
        dependencies[output] = frozenset((previous,))

    lane1_selected = add_mux_expected(
        expected,
        dependencies,
        "lane1",
        lane_outputs[0],
        (g1_role, p_role),
    )
    lane2_selected = add_mux_expected(
        expected,
        dependencies,
        "lane2",
        lane_outputs[1],
        (g2_role, p_role, product_role),
    )

    open_sites = {
        *MUX["lane1"]["targets"],
        *MUX["lane2"]["targets"],
        *(site for path in MUX["lane1"]["paths"] for site in path),
        *(site for path in MUX["lane2"]["paths"] for site in path),
        MUX["lane1"]["common"],
        MUX["lane2"]["common"],
        *MUX["lane1"]["terminals"],
        *MUX["lane2"]["terminals"],
        *MUX["lane1"]["voids"],
        *MUX["lane2"]["voids"],
    }
    dynamic_sites = set(expected) | open_sites
    interface_shell = {
        add(site, direction)
        for site in dynamic_sites
        for direction in c53.DIRECTIONS
    }
    core = set(records) | dynamic_sites | interface_shell
    cage = {
        add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if add(site, direction) not in core
    }
    for site in cage:
        place(records, site, FRAME, "final-cage")
    for site in set(expected) | open_sites:
        records.pop(site, None)
    return (
        records,
        expected,
        dependencies,
        results,
        case,
        lane_outputs,
        (lane1_selected, lane2_selected),
        product_role,
        ports,
    )


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def transformed_prepared(prepared, rotation):
    (
        initial,
        expected,
        dependencies,
        results,
        case,
        lane_outputs,
        selected,
        product_role,
        ports,
    ) = prepared
    shift = (1201, -1213, 1217)

    def moved(site):
        return add(c53.matvec(rotation, site), shift)

    return (
        c53.transform_records(initial, rotation, shift),
        c53.transform_records(expected, rotation, shift),
        {
            moved(site): frozenset(moved(parent) for parent in parents)
            for site, parents in dependencies.items()
        },
        results,
        case,
        lane_outputs,
        selected,
        product_role,
        frozenset(moved(site) for site in ports),
    ), tuple(
        moved(MUX[label]["common"])
        for label in ("lane1", "lane2")
    )


def schedule_seams(g1, g2, measured):
    _initial, expected, dependencies, *_rest = apparatus(g1, g2, measured)
    seams = set()
    for site in expected:
        for direction in c53.DIRECTIONS:
            neighbor = add(site, direction)
            if (
                neighbor in expected
                and site < neighbor
                and neighbor not in dependencies[site]
                and site not in dependencies[neighbor]
            ):
                seams.add((site, neighbor))
    return tuple(sorted(seams))


def deterministic_run(
    g1,
    g2,
    measured,
    limit: int | None = None,
    rotation=None,
    order: str = "min",
):
    prepared = apparatus(g1, g2, measured)
    output_sites = tuple(
        MUX[label]["common"]
        for label in ("lane1", "lane2")
    )
    if rotation is not None:
        prepared, output_sites = transformed_prepared(prepared, rotation)
    (
        initial,
        expected,
        dependencies,
        results,
        case,
        lane_outputs,
        selected,
        product_role,
        ports,
    ) = prepared
    records = dict(initial)
    formed = set()
    actual = enabled(records)
    maximum = 0
    edges = 0
    while len(formed) < len(expected):
        frontier = {
            target: frozenset((expected[target],))
            for target, parents in dependencies.items()
            if target not in formed and parents <= formed
        }
        maximum = max(maximum, len(frontier))
        if actual != frontier:
            missing = set(frontier) - set(actual)
            unexpected = set(actual) - set(frontier)
            neighborhoods = {
                target: {
                    direction: records.get(add(target, direction))
                    for direction in c53.DIRECTIONS
                }
                for target in missing | unexpected
            }
            return False, (
                len(formed),
                actual,
                frontier,
                neighborhoods,
                len(initial),
                len(expected),
                results,
                case,
                selected,
                product_role,
            )
        if order == "min":
            target = min(frontier)
        elif order == "max":
            target = max(frontier)
        else:
            raise ValueError(("unknown-order", order))
        records[target] = expected[target]
        formed.add(target)
        edges += len(frontier)
        actual.pop(target, None)
        for direction in c53.DIRECTIONS:
            candidate = add(target, direction)
            if candidate in records:
                actual.pop(candidate, None)
                continue
            signature = c53.local_signature(records, candidate)
            if signature in MERGED_RAW:
                actual[candidate] = MERGED_RAW[signature]
            else:
                actual.pop(candidate, None)
        if limit is not None and len(formed) >= limit:
            break
    outputs = (
        records.get(output_sites[0]),
        records.get(output_sites[1]),
    )
    complete = len(formed) == len(expected)
    return (
        complete and not actual and outputs == selected,
        (
            len(formed) + 1,
            edges,
            maximum,
            len(initial),
            len(expected),
            results,
            case,
            lane_outputs,
            selected,
            outputs,
            product_role,
            actual,
            len(ports),
        ),
    )


def deletion_control_pairs(g1, g2, measured):
    prepared = apparatus(g1, g2, measured)
    (
        _initial,
        _expected,
        _dependencies,
        _results,
        _case,
        lane_outputs,
        _selected,
        _product_role,
        _ports,
    ) = prepared
    pairs = []
    for index, label in enumerate(("g1", "g2", "p")):
        pairs.append((f"{label}-source-to-tap", TAP_SITES[index], SOURCE_CENTERS[index]))
        pairs.append((
            f"{label}-trunk-to-splitter",
            SPLITTER_SITES[index],
            TAP_TRUNK_PATHS[index][-1],
        ))
    case_site = add(pivot.CASE_SITE, control.CONTROLLER_SHIFT)
    pairs.extend((
        (
            "case-c1-parent",
            case_site,
            add(pivot.CASE_INPUTS["c1"], control.CONTROLLER_SHIFT),
        ),
        (
            "case-c2-parent",
            case_site,
            add(pivot.CASE_INPUTS["c2"], control.CONTROLLER_SHIFT),
        ),
    ))
    multiplier_target = add(mult.TARGET, MULTIPLIER_SHIFT)
    pairs.extend((
        (
            "multiplier-left-parent",
            multiplier_target,
            add(mult.LEFT, MULTIPLIER_SHIFT),
        ),
        (
            "multiplier-right-parent",
            multiplier_target,
            add(mult.RIGHT, MULTIPLIER_SHIFT),
        ),
    ))
    for lane_index, label in enumerate(("lane1", "lane2")):
        geometry = MUX[label]
        selector = lane_outputs[lane_index]
        selected_index = mux.SELECTOR_INDEX[selector]
        target = geometry["targets"][selected_index]
        terminal = geometry["terminals"][selected_index]
        path = geometry["paths"][selected_index]
        pairs.extend((
            (
                f"{label}-case-parent",
                geometry["selector"],
                JOINT_CASE_PATHS[lane_index][-1],
            ),
            (
                f"{label}-selector-parent",
                target,
                geometry["selector"],
            ),
            (
                f"{label}-bus-parent",
                target,
                geometry["buses"][selected_index],
            ),
            (
                f"{label}-terminal-parent",
                terminal,
                path[-1],
            ),
            (
                f"{label}-common-parent",
                geometry["common"],
                terminal,
            ),
        ))
    return tuple(pairs)


def parent_deletion_checks(g1, g2, measured):
    prepared = apparatus(g1, g2, measured)
    initial, expected, dependencies, *_rest = prepared
    pending = {
        label: (target, parent)
        for label, target, parent in deletion_control_pairs(g1, g2, measured)
    }
    results = {}
    records = dict(initial)
    formed = set()
    actual = enabled(records)
    while len(formed) < len(expected):
        frontier = {
            target: frozenset((expected[target],))
            for target, parents in dependencies.items()
            if target not in formed and parents <= formed
        }
        if actual != frontier:
            return results, ("frontier-mismatch", len(formed), actual, frontier)
        for label, (target, parent) in tuple(pending.items()):
            if target not in actual:
                continue
            parent_role = records.pop(parent, None)
            if parent_role is None:
                results[label] = False
            else:
                signature = c53.local_signature(records, target)
                results[label] = signature not in MERGED_RAW
                records[parent] = parent_role
            del pending[label]
        target = min(frontier)
        records[target] = expected[target]
        formed.add(target)
        actual.pop(target, None)
        for direction in c53.DIRECTIONS:
            candidate = add(target, direction)
            if candidate in records:
                actual.pop(candidate, None)
                continue
            signature = c53.local_signature(records, candidate)
            if signature in MERGED_RAW:
                actual[candidate] = MERGED_RAW[signature]
            else:
                actual.pop(candidate, None)
    if pending:
        return results, ("unreached-controls", pending)
    return results, None


def main() -> int:
    print(
        "LAW",
        {
            "base_raw": len(tap.MERGED_RAW),
            "splitter": (len(SPLITTER_TABLE), len(SPLITTER_RAW)),
            "selector": (
                len(INTEGRATED_SELECTOR_TABLE),
                len(INTEGRATED_SELECTOR_RAW),
            ),
            "gate": (len(INTEGRATED_GATE_TABLE), len(INTEGRATED_GATE_RAW)),
            "gate_base_overlap": len(
                set(INTEGRATED_GATE_RAW) & set(tap.MERGED_RAW)
            ),
            "merged_raw": len(MERGED_RAW),
            "conflicts": len(RAW_CONFLICTS),
        },
    )
    print(
        "PATHS",
        {label: len(path) for label, path in PAYLOAD_PATHS.items()},
        len(PRODUCT_PATH),
    )
    print(
        "MUX",
        {
            label: (
                geometry["selector"],
                geometry["buses"],
                geometry["common"],
                tuple(map(len, geometry["paths"])),
            )
            for label, geometry in MUX.items()
        },
    )
    case_results = {}
    try:
        for case, rows in CASE_REPRESENTATIVES.items():
            case_results[case] = deterministic_run(*rows)
            print("CASE", case, case_results[case])
        reverse_results = {
            case: deterministic_run(*rows, order="max")
            for case, rows in CASE_REPRESENTATIVES.items()
        }
        seams = {
            case: schedule_seams(*rows)
            for case, rows in CASE_REPRESENTATIVES.items()
        }
        deletion_results = {}
        deletion_errors = {}
        for case, rows in CASE_REPRESENTATIVES.items():
            case_deletions, case_error = parent_deletion_checks(*rows)
            deletion_results[case] = case_deletions
            deletion_errors[case] = case_error
    except ValueError as error:
        print("LAYOUT_FAILURE", str(error)[:20_000])
        print("RESULT", "OPEN")
        return 1
    print("REVERSE", reverse_results)
    print("SCHEDULE_SEAMS", {case: len(value) for case, value in seams.items()})
    print("DELETIONS", deletion_results, deletion_errors)
    result = (
        len(SPLITTER_TABLE) == 32
        and len(SPLITTER_RAW) == 768
        and len(INTEGRATED_SELECTOR_TABLE) == 8
        and len(INTEGRATED_SELECTOR_RAW) == 192
        and len(INTEGRATED_GATE_TABLE) == 160
        and len(INTEGRATED_GATE_RAW) == 3_840
        and len(set(INTEGRATED_GATE_RAW) & set(tap.MERGED_RAW)) == 1_536
        and len(MERGED_RAW) == 100_652
        and not RAW_CONFLICTS
        and all(len(outputs) == 1 for outputs in MERGED_RAW.values())
        and all(ok for ok, _detail in case_results.values())
        and all(ok for ok, _detail in reverse_results.values())
        and all(not value for value in seams.values())
        and all(error is None for error in deletion_errors.values())
        and all(len(values) == 20 for values in deletion_results.values())
        and all(
            passed
            for values in deletion_results.values()
            for passed in values.values()
        )
    )
    print("RESULT", "PHYSICAL_JOINT_STABILIZER_UPDATE" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
