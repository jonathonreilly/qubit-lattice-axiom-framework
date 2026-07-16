#!/usr/bin/env python3
"""Cycle 169: row-native commuting signed membership.

Three original signed-row records are the only variable supplied inputs.  The
apparatus physically derives the commuting product, fans row ancestry before
literal decoding, compares the measured row with g1/g2/g1*g2, and XORs the
three mutually-exclusive equality records.  No literal input, product row, or
equality bit is supplied by the host.

The complete membership apparatus needs the Cycle-165 law, the generic
Cycle-166 row splitter, the Cycle-167 sign decoder, and 288 direct/fold
comparator rows: 99,212 raw rows.  The 101,708-row number is reserved for the
union with the full Cycle-166 update law.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import lru_cache
from itertools import product
from pathlib import Path
import sys
import time

import cycle48_symplectic_tableau_compression_probe_2026_07_15 as tableau
import physical_downstream_signed_row_decoder_probe_2026_07_16 as signed
import physical_joint_stabilizer_update_geometry_probe_2026_07_16 as joint


tap = signed.tap
ported = signed.ported
cycle164 = tap.prior
algebra = joint.mult.algebra
c53 = joint.c53
cell = joint.cell
cable = joint.cable
FRAME = joint.FRAME
GUIDE = joint.GUIDE
H0 = ported.d.H0
H1 = ported.d.H1
XOR_ROLE = joint.control.bound.spacious.alu.XOR_ROLE
Coord = tuple[int, int, int]
Row = tuple[int, int, int, int, int]
Spec = tuple[object, ...]
ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "PHYSICAL_ROW_NATIVE_SIGNED_MEMBERSHIP_CYCLE169_NOTE_2026-07-16.md"
)

ROWS = tuple(product((0, 1), repeat=5))
ZERO = (0, 0, 0, 0, 0)
ZERO_ROLE = joint.pivot.five.ROW_ROLE[ZERO]
INDEX_ROLES = ported.terminal.INDEX_ROLES

BASE_MEMBERSHIP_RAW = cell.merge_raw(
    tap.MERGED_RAW,
    joint.SPLITTER_RAW,
    signed.SIGN_RAW,
)
BASE_MEMBERSHIP_CONFLICTS = {
    signature: outputs
    for signature, outputs in BASE_MEMBERSHIP_RAW.items()
    if len(outputs) != 1
}

EX = (1, 0, 0)
EY = (0, 1, 0)
EZ = (0, 0, 1)
NEG_EX = (-1, 0, 0)
NEG_EY = (0, -1, 0)
NEG_EZ = (0, 0, -1)


def comparator_signature(
    candidate: int,
    reference: int,
    prior: int | None,
):
    records = {
        EY: H1 if candidate else H0,
        NEG_EY: H1 if reference else H0,
        EZ: GUIDE,
        NEG_EZ: FRAME,
    }
    if prior is None:
        records[NEG_EX] = FRAME
    else:
        records[NEG_EX] = H1 if prior else H0
    return c53.canonical_signature(c53.local_signature(records, (0, 0, 0)))


DIRECT_COMPARATOR_TABLE = {
    comparator_signature(candidate, reference, None): (
        H1 if candidate == reference else H0
    )
    for candidate, reference in product((0, 1), repeat=2)
}
FOLD_COMPARATOR_TABLE = {
    comparator_signature(candidate, reference, prior): (
        H1 if prior and candidate == reference else H0
    )
    for candidate, reference, prior in product((0, 1), repeat=3)
}
COMPARATOR_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for table in (DIRECT_COMPARATOR_TABLE, FOLD_COMPARATOR_TABLE)
    for signature, output in table.items()
))
MEMBERSHIP_RAW = cell.merge_raw(BASE_MEMBERSHIP_RAW, COMPARATOR_RAW)
MEMBERSHIP_CONFLICTS = {
    signature: outputs
    for signature, outputs in MEMBERSHIP_RAW.items()
    if len(outputs) != 1
}
UNIFIED_RAW = cell.merge_raw(
    joint.MERGED_RAW,
    signed.SIGN_RAW,
    COMPARATOR_RAW,
)
UNIFIED_CONFLICTS = {
    signature: outputs
    for signature, outputs in UNIFIED_RAW.items()
    if len(outputs) != 1
}


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def scale(factor: int, vector: Coord) -> Coord:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


def neg(vector: Coord) -> Coord:
    return scale(-1, vector)


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def moved(site: Coord, rotation, shift: Coord) -> Coord:
    return add(c53.matvec(rotation, site), shift)


def line_to(path: list[Coord], target: Coord, axes=(0, 1, 2)) -> None:
    current = list(path[-1])
    for axis in axes:
        while current[axis] != target[axis]:
            current[axis] += 1 if target[axis] > current[axis] else -1
            point = tuple(current)  # type: ignore[assignment]
            if point in path:
                raise ValueError(("path-self-contact", point, target, tuple(path)))
            path.append(point)


def place(records: dict[Coord, str], site: Coord, role: str, label: str = "") -> None:
    previous = records.get(site)
    if previous is not None and previous != role:
        raise ValueError(("placement-conflict", label, site, previous, role))
    records[site] = role


def bit(value: int) -> str:
    return H1 if value else H0


def row_spec(label: str) -> Spec:
    return ("row", label)


def bit_spec(label: str, index: int) -> Spec:
    return ("bit", label, index)


def status_spec(lane: int, index: int) -> Spec:
    return ("status", lane, index)


def xor_spec(index: int) -> Spec:
    return ("xor", index)


def dummy_role(spec: Spec) -> str:
    return ZERO_ROLE if spec[0] == "row" else H0


@dataclass(frozen=True)
class BitSource:
    site: Coord
    direction: Coord
    spec: Spec
    destination: tuple[int, str, int]


@dataclass
class Blueprint:
    fixed: dict[Coord, str]
    original_sources: dict[Coord, str]
    expected_specs: dict[Coord, Spec]
    dependencies: dict[Coord, frozenset[Coord]]
    path_groups: list[tuple[tuple[Spec, tuple[Coord, ...]], ...]]
    open_ports: set[Coord]
    output_site: Coord
    compact_regression: tuple[bool, str]


class Builder:
    def __init__(self) -> None:
        self.fixed: dict[Coord, str] = {}
        self.original_sources: dict[Coord, str] = {}
        self.expected_specs: dict[Coord, Spec] = {}
        self.dependencies: dict[Coord, frozenset[Coord]] = {}
        self.path_groups: list[tuple[tuple[Spec, tuple[Coord, ...]], ...]] = []
        self.open_ports: set[Coord] = set()
        self.bit_sources: list[BitSource] = []
        self.status_paths: dict[
            tuple[int, int],
            tuple[Spec, tuple[Coord, ...]],
        ] = {}

    def fixed_record(self, site: Coord, role: str, label: str) -> None:
        place(self.fixed, site, role, label)

    def original_source(self, site: Coord, label: str) -> None:
        previous = self.original_sources.get(site)
        if previous is not None and previous != label:
            raise ValueError(("source-conflict", site, previous, label))
        if site in self.fixed:
            raise ValueError(("source-fixed-conflict", site, self.fixed[site], label))
        self.original_sources[site] = label

    def expected(
        self,
        site: Coord,
        spec: Spec,
        parents: frozenset[Coord] = frozenset(),
    ) -> None:
        previous = self.expected_specs.get(site)
        if previous is not None and previous != spec:
            raise ValueError(("expected-conflict", site, previous, spec))
        prior_parents = self.dependencies.get(site)
        if prior_parents is not None and prior_parents != parents:
            raise ValueError(("dependency-conflict", site, prior_parents, parents))
        self.expected_specs[site] = spec
        self.dependencies[site] = parents

    def path(
        self,
        spec: Spec,
        path: tuple[Coord, ...],
        *,
        group: list[tuple[Spec, tuple[Coord, ...]]] | None = None,
    ) -> None:
        if len(path) < 2:
            raise ValueError(("short-path", path))
        if any(manhattan(left, right) != 1 for left, right in zip(path, path[1:])):
            raise ValueError(("nonlocal-path", path))
        for previous, target in zip(path, path[1:]):
            self.expected(target, spec, frozenset((previous,)))
        item = (spec, path)
        if group is None:
            self.path_groups.append((item,))
        else:
            group.append(item)

    def reader(
        self,
        center: Coord,
        label: str,
        tree_root: Coord,
        direct_destinations: dict[int, tuple[int, str, int]],
    ) -> None:
        self.original_source(center, label)
        for direction, index_role in zip(
            ported.TARGETS,
            ported.INDEX_ROLES,
            strict=True,
        ):
            self.fixed_record(add(center, add(direction, EZ)), index_role, "reader-index")
        self.fixed_record(add(center, NEG_EZ), FRAME, "reader-backstop")

        for index, direction in enumerate(ported.TARGETS):
            target = add(center, direction)
            port = add(center, scale(2, direction))
            index_site = add(target, EZ)
            for neighbor_direction in c53.DIRECTIONS:
                site = add(target, neighbor_direction)
                if site not in {center, port, index_site}:
                    self.fixed_record(site, FRAME, "reader-frame")
            spec = bit_spec(label, index)
            self.expected(target, spec)
            self.bit_sources.append(
                BitSource(target, direction, spec, direct_destinations[index])
            )

        tap_site = add(center, EZ)
        self.expected(tap_site, row_spec(label))
        root_input = add(tree_root, NEG_EX)
        path = [
            tap_site,
            add(center, scale(2, EZ)),
            add(center, scale(3, EZ)),
            add(center, scale(4, EZ)),
        ]
        line_to(path, (tree_root[0] - 2, center[1], path[-1][2]), (0,))
        line_to(path, (tree_root[0] - 2, tree_root[1], path[-1][2]), (1,))
        line_to(path, (tree_root[0] - 2, tree_root[1], tree_root[2]), (2,))
        if path[-1] != add(tree_root, scale(-2, EX)):
            raise ValueError(("bad-reader-trunk-preterminal", center, tree_root, path[-1]))
        path.append(root_input)
        if add(root_input, EX) != tree_root:
            raise ValueError(("bad-reader-trunk-port", center, tree_root, root_input))
        self.path(row_spec(label), tuple(path))

    def splitter_fixed(self, site: Coord) -> None:
        # Proper-cubic image of Cycle 166:
        # input -x; outputs +/-y; GUIDE +z; FRAME -z,+x.
        self.fixed_record(add(site, EZ), GUIDE, "splitter-guide")
        self.fixed_record(add(site, NEG_EZ), FRAME, "splitter-frame")
        self.fixed_record(add(site, EX), FRAME, "splitter-forward-frame")

    def decoder_leaf(
        self,
        row_label: str,
        index: int,
        splitter: Coord,
        direction: Coord,
        destination: tuple[int, str, int],
        *,
        group: list[tuple[Spec, tuple[Coord, ...]]],
    ) -> None:
        endpoint = add(splitter, scale(10, direction))
        decoder = add(splitter, scale(11, direction))
        path = tuple(
            add(splitter, scale(distance, direction))
            for distance in range(11)
        )
        self.path(row_spec(row_label), path, group=group)
        if add(endpoint, direction) != decoder:
            raise ValueError(("bad-leaf-port", splitter, endpoint, decoder))

        # Proper-cubic ported-reader image: row parent behind, bit port ahead,
        # typed index +z, and FRAME at +/-x and -z.
        self.fixed_record(add(decoder, EZ), INDEX_ROLES[index], "leaf-index")
        self.fixed_record(add(decoder, EX), FRAME, "leaf-frame")
        self.fixed_record(add(decoder, NEG_EX), FRAME, "leaf-frame")
        self.fixed_record(add(decoder, NEG_EZ), FRAME, "leaf-frame")
        spec = bit_spec(row_label, index)
        self.expected(decoder, spec, frozenset((endpoint,)))
        self.bit_sources.append(
            BitSource(decoder, direction, spec, destination)
        )

    def routed_row_leaf(
        self,
        row_label: str,
        splitter: Coord,
        direction: Coord,
        endpoint: Coord,
        future: Coord,
        channel: Coord,
        *,
        group: list[tuple[Spec, tuple[Coord, ...]]],
    ) -> None:
        final_direction = sub(future, endpoint)
        if final_direction not in c53.DIRECTIONS:
            raise ValueError(("bad-row-feed-future", endpoint, future))
        penultimate = sub(endpoint, final_direction)
        perpendicular = EX if final_direction not in {EX, NEG_EX} else EZ
        prepenultimate = sub(penultimate, perpendicular)
        path = [
            splitter,
            add(splitter, direction),
            add(splitter, scale(2, direction)),
        ]
        line_to(path, channel, (2, 0, 1))
        line_to(path, (prepenultimate[0], path[-1][1], path[-1][2]), (0,))
        line_to(path, (prepenultimate[0], prepenultimate[1], path[-1][2]), (1,))
        line_to(path, prepenultimate, (2,))
        if manhattan(path[-1], penultimate) != 1:
            raise ValueError(("bad-row-feed-preterminal", path[-1], penultimate))
        path.append(penultimate)
        if manhattan(path[-1], endpoint) != 1:
            raise ValueError(("bad-row-feed-terminal", path[-1], endpoint))
        path.append(endpoint)
        if add(endpoint, final_direction) != future:
            raise ValueError(("bad-row-feed-port", endpoint, future))
        self.path(row_spec(row_label), tuple(path), group=group)

    def comb_tree(
        self,
        root: Coord,
        row_label: str,
        leaves: tuple[tuple[object, ...], ...],
    ) -> None:
        count = len(leaves)
        if count < 2:
            raise ValueError(("tree-too-small", row_label, count))
        splitters = tuple(add(root, (16 * index, 0, 0)) for index in range(count - 1))
        leaf_index = 0
        for index, splitter in enumerate(splitters):
            self.splitter_fixed(splitter)
            input_site = add(splitter, NEG_EX)
            self.expected(
                splitter,
                row_spec(row_label),
                frozenset((input_site,)),
            )
            group: list[tuple[Spec, tuple[Coord, ...]]] = []

            positive = leaves[leaf_index]
            leaf_index += 1
            if positive[0] != "decode":
                raise ValueError(("positive-leaf-must-decode", positive))
            _kind, bit_index, destination = positive
            self.decoder_leaf(
                row_label,
                int(bit_index),
                splitter,
                EY,
                destination,  # type: ignore[arg-type]
                group=group,
            )

            if index + 1 < len(splitters):
                next_splitter = splitters[index + 1]
                path = [
                    splitter,
                    add(splitter, NEG_EY),
                    add(splitter, scale(-2, EY)),
                ]
                line_to(path, add(path[-1], scale(-4, EZ)), (2,))
                line_to(
                    path,
                    (next_splitter[0] - 2, path[-1][1], path[-1][2]),
                    (0,),
                )
                line_to(
                    path,
                    (next_splitter[0] - 2, next_splitter[1], path[-1][2]),
                    (1,),
                )
                line_to(
                    path,
                    (next_splitter[0] - 2, next_splitter[1], next_splitter[2]),
                    (2,),
                )
                path.append(add(next_splitter, NEG_EX))
                if add(path[-1], EX) != next_splitter:
                    raise ValueError(("bad-comb-port", splitter, next_splitter, path[-1]))
                self.path(row_spec(row_label), tuple(path), group=group)
            else:
                negative = leaves[leaf_index]
                leaf_index += 1
                if negative[0] == "decode":
                    _kind, bit_index, destination = negative
                    self.decoder_leaf(
                        row_label,
                        int(bit_index),
                        splitter,
                        NEG_EY,
                        destination,  # type: ignore[arg-type]
                        group=group,
                    )
                elif negative[0] == "feed":
                    (
                        _kind,
                        endpoint,
                        future,
                        channel,
                    ) = negative
                    self.routed_row_leaf(
                        row_label,
                        splitter,
                        NEG_EY,
                        endpoint,  # type: ignore[arg-type]
                        future,  # type: ignore[arg-type]
                        channel,  # type: ignore[arg-type]
                        group=group,
                    )
                else:
                    raise ValueError(("unknown-leaf", negative))
            self.path_groups.append(tuple(group))
        if leaf_index != count:
            raise ValueError(("leaf-count", row_label, leaf_index, count))

    def multiplier(self, shift: Coord, product_tree: Coord) -> None:
        for site in cycle164.m.FRAMES:
            self.fixed_record(add(site, shift), cycle164.m.FRAME_ROLE, "multiplier-frame")
        self.fixed_record(
            add(cycle164.m.PORT_FRAME, shift),
            cycle164.m.FRAME_ROLE,
            "multiplier-port-frame",
        )

        left_path = tuple(add(site, shift) for site in cycle164.LEFT_PATH)
        right_path = tuple(add(site, shift) for site in cycle164.RIGHT_PATH)
        output_path = tuple(add(site, shift) for site in cycle164.OUTPUT_PATH)
        group: list[tuple[Spec, tuple[Coord, ...]]] = []
        self.path(row_spec("g1"), left_path, group=group)
        self.path(row_spec("g2"), right_path, group=group)
        target = add(cycle164.m.TARGET, shift)
        left = add(cycle164.m.LEFT, shift)
        right = add(cycle164.m.RIGHT, shift)
        self.expected(target, row_spec("prod"), frozenset((left, right)))
        self.path(row_spec("prod"), output_path, group=group)
        self.path_groups.append(tuple(group))
        output_port = add(cycle164.OUTPUT_PORT, shift)
        if output_port != product_tree:
            raise ValueError(("product-tree-port", output_port, product_tree))

    def comparator_sockets(self):
        rotations = (
            (
                ((0, 0, 1), (0, 1, 0), (-1, 0, 0)),
                (0, 0, 100),
            ),
            (
                ((-1, 0, 0), (0, 1, 0), (0, 0, -1)),
                (100, 300, 0),
            ),
            (
                ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
                (0, -100, -1),
            ),
        )
        sockets: dict[tuple[int, str, int], tuple[Coord, Coord, Coord]] = {}
        final_sites = []
        for lane, (rotation, shift) in enumerate(rotations):
            def transform(site: Coord) -> Coord:
                return moved(site, rotation, shift)

            previous_endpoint: Coord | None = None
            for index in range(5):
                target = transform((10 * index, 0, 0))
                candidate = transform((10 * index, -1, 0))
                reference = transform((10 * index, 1, 0))
                self.fixed_record(
                    transform((10 * index, 0, 1)),
                    GUIDE,
                    "comparator-guide",
                )
                self.fixed_record(
                    transform((10 * index, 0, -1)),
                    FRAME,
                    "comparator-frame",
                )
                parents = {candidate, reference}
                if previous_endpoint is None:
                    self.fixed_record(
                        transform((-1, 0, 0)),
                        FRAME,
                        "direct-comparator-backstop",
                    )
                else:
                    parents.add(previous_endpoint)
                self.expected(target, status_spec(lane, index), frozenset(parents))
                sockets[(lane, "candidate", index)] = (candidate, target, transform((10 * index, -2, 0)))
                sockets[(lane, "reference", index)] = (reference, target, transform((10 * index, 2, 0)))
                if index < 4:
                    next_target = transform((10 * (index + 1), 0, 0))
                    direction = sub(next_target, target)
                    unit = tuple(value // 10 for value in direction)  # type: ignore[assignment]
                    path = tuple(
                        add(target, scale(distance, unit))
                        for distance in range(10)
                    )
                    if add(path[-1], unit) != next_target:
                        raise ValueError(("status-port", lane, index, path[-1], next_target))
                    self.status_paths[(lane, index)] = (
                        status_spec(lane, index),
                        path,
                    )
                    previous_endpoint = path[-1]
                else:
                    final_sites.append(target)
        return sockets, tuple(final_sites)

    def literal_path(
        self,
        source: BitSource,
        endpoint: Coord,
        target: Coord,
        penultimate: Coord,
        ordinal: int,
        *,
        group: list[tuple[Spec, tuple[Coord, ...]]],
    ) -> None:
        terminal_direction = sub(target, endpoint)
        if terminal_direction not in c53.DIRECTIONS:
            raise ValueError(("literal-target-not-local", endpoint, target))
        if add(endpoint, terminal_direction) != target:
            raise ValueError(("literal-bad-port", endpoint, target))
        if sub(endpoint, penultimate) != terminal_direction:
            raise ValueError(("literal-bad-penultimate", penultimate, endpoint, target))

        lane, side, literal_index = source.destination
        if lane == 0:
            perpendicular = NEG_EX if side == "candidate" else EX
        elif lane == 1:
            perpendicular = (0, 0, 0)
        else:
            perpendicular = NEG_EX if side == "candidate" else EX
        prepenultimate = (
            sub(penultimate, terminal_direction)
            if lane == 1
            else add(penultimate, perpendicular)
        )

        side_sign = -1 if side == "candidate" else 1
        height = 400 + 200 * lane + 8 * ordinal
        lane_channels = (
            (
                side_sign * (500 + 4 * ordinal),
                200 + 4 * ordinal,
                height,
            ),
            (
                -800 - 4 * ordinal,
                side_sign * (1000 + 4 * ordinal),
                side_sign * height,
            ),
            (
                side_sign * (500 + 4 * ordinal),
                -1500 - 4 * ordinal,
                height,
            ),
        )
        channel = lane_channels[lane]
        path = [
            source.site,
            add(source.site, source.direction),
            add(source.site, scale(2, source.direction)),
        ]
        # One tangential escape cell clears the reader's whole-row trunk.
        # Every (lane, side, index) then owns a distinct height and side
        # corridor before its short, lane-oriented terminal ray.
        if source.direction == EX:
            escape = add(path[-1], scale(4, EY))
        elif source.direction == NEG_EX:
            escape = add(path[-1], scale(-4, EY))
        else:
            escape = add(path[-1], EX)
        line_to(path, escape)
        if source.direction in {EY, NEG_EY}:
            line_to(
                path,
                add(path[-1], scale(6 + ordinal, source.direction)),
            )
        line_to(path, (path[-1][0], path[-1][1], channel[2]), (2,))
        line_to(path, (channel[0], path[-1][1], channel[2]), (0,))
        line_to(path, channel, (1,))
        if lane == 1:
            approach = sub(
                prepenultimate,
                scale(8 + 8 * literal_index, terminal_direction),
            )
            terminal_height = channel[2] + side_sign * (
                100 + 10 * literal_index
            )
            line_to(path, (channel[0], channel[1], terminal_height), (2,))
            line_to(path, (channel[0], approach[1], terminal_height), (1,))
            line_to(path, (approach[0], approach[1], terminal_height), (0,))
            line_to(path, approach, (2,))
            line_to(path, prepenultimate, (1,))
        else:
            line_to(path, (channel[0], channel[1], prepenultimate[2]), (2,))
            line_to(path, (channel[0], prepenultimate[1], prepenultimate[2]), (1,))
            line_to(path, prepenultimate, (0,))
        if manhattan(path[-1], penultimate) != 1:
            raise ValueError(("literal-preterminal", source, path[-1], penultimate))
        path.append(penultimate)
        if manhattan(path[-1], endpoint) != 1:
            raise ValueError(("literal-terminal", source, path[-1], endpoint))
        path.append(endpoint)
        self.path(source.spec, tuple(path), group=group)


def compact_adjacent_regression() -> tuple[bool, str]:
    # Two neighboring compact-lane bit endpoints each need the other endpoint's
    # face as cable furniture.  The retained cable grammar must reject this.
    items = (
        (H0, ((0, -2, 0), (0, -1, 0))),
        (H1, ((1, -2, 0), (1, -1, 0))),
    )
    protected = frozenset(
        {
            (0, -2, 0),
            (0, -1, 0),
            (0, 0, 0),
            (1, -2, 0),
            (1, -1, 0),
            (1, 0, 0),
        }
    )
    try:
        cable.multi_path_core(items, extra_protected=protected)
    except ValueError as error:
        return True, str(error).split("(", 1)[0]
    return False, "compact adjacent cable endpoints unexpectedly composed"


def greedy_path_core(
    items: tuple[tuple[str, tuple[Coord, ...]], ...],
    *,
    constraints: dict[Coord, str],
    extra_protected: frozenset[Coord],
):
    """Exact retained cable furniture without the generic exponential CSP.

    These Cycle-169 routes live in disjoint slabs.  Exact backtracking is
    therefore factored by shared-furniture components, avoiding the generic
    solver's repeated global-domain rebuild over thousands of independent
    straight cells.
    """
    records = dict(constraints)
    expected: dict[Coord, str] = {}
    terminal_ports: set[Coord] = set()
    for value, path in items:
        prior_source = records.get(path[0])
        if prior_source is not None and prior_source != value:
            raise ValueError(("source-conflict", path[0], prior_source, value))
        records[path[0]] = value
        for site in path[1:]:
            prior = expected.get(site)
            if prior is not None and prior != value:
                raise ValueError(("path-output-conflict", site, prior, value))
            expected[site] = value
        terminal_ports.add(add(path[-1], cable.terminal_direction(path)))

    protected = set(expected) | terminal_ports | set(extra_protected)
    segments: list[tuple[tuple[Coord, int, Coord, Coord, Coord], tuple[dict[Coord, str], ...]]] = []
    for value, path in items:
        terminal_port = add(path[-1], cable.terminal_direction(path))
        for index, target in enumerate(path[1:], 1):
            previous = path[index - 1]
            future = path[index + 1] if index + 1 < len(path) else terminal_port
            back = sub(previous, target)
            forward = sub(future, target)
            guides = (
                tuple(
                    direction
                    for direction in c53.DIRECTIONS
                    if cable.dot(back, direction) == 0
                )
                if forward == cable.neg(back)
                else (None,)
            )
            options = []
            for guide in guides:
                _kind, local_records = cable.segment_records(
                    target,
                    previous,
                    future,
                    value,
                    guide_override=guide,
                )
                guards = {
                    site: role
                    for site, role in local_records.items()
                    if site != previous
                }
                if not (set(guards) & protected):
                    options.append(guards)
            if not options:
                raise ValueError(("no-protected-guide-option", path[0], index, target))
            segments.append(((path[0], index, target, previous, future), tuple(options)))

    def compatible(option: dict[Coord, str], placed: dict[Coord, str]) -> bool:
        return all(
            site not in placed or placed[site] == role
            for site, role in option.items()
        )

    parents = list(range(len(segments)))

    def find(index: int) -> int:
        while parents[index] != index:
            parents[index] = parents[parents[index]]
            index = parents[index]
        return index

    def union(left: int, right: int) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root != right_root:
            parents[right_root] = left_root

    occupants: dict[Coord, list[int]] = defaultdict(list)
    for index, (_label, options) in enumerate(segments):
        sites = set().union(*(set(option) for option in options))
        for site in sites:
            occupants[site].append(index)
    for indices in occupants.values():
        for index in indices[1:]:
            union(indices[0], index)

    components: dict[int, list[int]] = defaultdict(list)
    for index in range(len(segments)):
        components[find(index)].append(index)

    def solve_component(
        remaining: frozenset[int],
        placed: dict[Coord, str],
    ) -> dict[Coord, str] | None:
        if not remaining:
            return placed
        domains = {
            index: tuple(
                option
                for option in segments[index][1]
                if compatible(option, placed)
            )
            for index in remaining
        }
        if any(not domain for domain in domains.values()):
            return None
        index = min(remaining, key=lambda item: (len(domains[item]), item))
        rest = remaining - {index}
        for option in domains[index]:
            result = solve_component(rest, {**placed, **option})
            if result is not None:
                return result
        return None

    for component in components.values():
        relevant_sites = set().union(*(
            set(option)
            for index in component
            for option in segments[index][1]
        ))
        base = {
            site: records[site]
            for site in relevant_sites
            if site in records
        }
        chosen = solve_component(frozenset(component), base)
        if chosen is None:
            raise ValueError((
                "no-compatible-guide-component",
                tuple(segments[index][0] for index in component),
            ))
        records.update(chosen)
    return records, expected, frozenset(terminal_ports)


@lru_cache(maxsize=1)
def blueprint() -> Blueprint:
    builder = Builder()
    multiplier_shift = (0, -300, 0)
    product_tree = add(cycle164.OUTPUT_PORT, multiplier_shift)

    sockets, final_sites = builder.comparator_sockets()

    p_center = (-300, 0, -30)
    g1_center = (-300, 200, -30)
    g2_center = (-300, -200, -30)
    p_tree = (-240, 0, 0)
    g1_tree = (-240, 200, 0)
    g2_tree = (-240, -200, 0)

    p_direct = {
        index: (0, "candidate", index)
        for index in range(4)
    }
    g1_direct = {
        index: (0, "reference", index)
        for index in range(4)
    }
    g2_direct = {
        index: (1, "reference", index)
        for index in range(4)
    }
    builder.reader(p_center, "p", p_tree, p_direct)
    builder.reader(g1_center, "g1", g1_tree, g1_direct)
    builder.reader(g2_center, "g2", g2_tree, g2_direct)

    p_leaves: list[tuple[object, ...]] = [
        ("decode", 4, (0, "candidate", 4)),
    ]
    p_leaves.extend(
        ("decode", index, (1, "candidate", index))
        for index in range(5)
    )
    p_leaves.extend(
        ("decode", index, (2, "candidate", index))
        for index in range(5)
    )
    builder.comb_tree(p_tree, "p", tuple(p_leaves))

    left_source = add(cycle164.LEFT_PATH[0], multiplier_shift)
    left_future = add(cycle164.LEFT_PATH[1], multiplier_shift)
    right_source = add(cycle164.RIGHT_PATH[0], multiplier_shift)
    right_future = add(cycle164.RIGHT_PATH[1], multiplier_shift)
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

    source_by_destination: dict[tuple[int, str, int], BitSource] = {}
    for source in builder.bit_sources:
        previous = source_by_destination.get(source.destination)
        if previous is not None:
            raise ValueError(("duplicate-bit-destination", source.destination, previous, source))
        source_by_destination[source.destination] = source
    wanted_destinations = {
        (lane, side, index)
        for lane in range(3)
        for side in ("candidate", "reference")
        for index in range(5)
    }
    if set(source_by_destination) != wanted_destinations:
        raise ValueError((
            "bit-destination-census",
            wanted_destinations - set(source_by_destination),
            set(source_by_destination) - wanted_destinations,
        ))

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
                builder.path(
                    status_specification,
                    status_path,
                    group=group,
                )
            builder.path_groups.append(tuple(group))

    # Final status transport into two independently oriented XOR stages.
    a_site = (0, 0, 0)
    b_site = (0, 0, -1)
    e_sites = ((0, 0, 1), (1, 0, 0), (0, -1, -1))
    for lane, (source, endpoint) in enumerate(zip(final_sites, e_sites, strict=True)):
        if lane == 1:
            path_list = [source, add(source, NEG_EX), add(source, scale(-2, EX))]
            line_to(path_list, (path_list[-1][0], path_list[-1][1], 50), (2,))
            line_to(path_list, (path_list[-1][0], 0, 50), (1,))
            line_to(path_list, (10, 0, 50), (0,))
            line_to(path_list, (10, 0, 0), (2,))
            line_to(path_list, (2, 0, 0), (0,))
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
            distance = manhattan(source, endpoint)
            path = tuple(
                add(source, scale(step, direction))
                for step in range(distance + 1)
            )
        consumer = a_site if lane < 2 else b_site
        if add(path[-1], direction) != consumer:
            raise ValueError(("bad-final-status-port", lane, path[-1], consumer))
        builder.path(status_spec(lane, 4), path)

    builder.fixed_record((-1, 0, 0), XOR_ROLE, "xor-a-op")
    builder.fixed_record((0, 1, 0), FRAME, "xor-a-frame")
    builder.fixed_record((0, -1, 0), FRAME, "xor-a-frame")
    builder.expected(a_site, xor_spec(0), frozenset((e_sites[0], e_sites[1])))
    builder.fixed_record((0, 1, -1), XOR_ROLE, "xor-b-op")
    builder.fixed_record((-1, 0, -1), FRAME, "xor-b-frame")
    builder.fixed_record((1, 0, -1), FRAME, "xor-b-frame")
    builder.expected(b_site, xor_spec(1), frozenset((a_site, e_sites[2])))
    final_port = (0, 0, -2)
    builder.open_ports.add(final_port)

    return Blueprint(
        fixed=builder.fixed,
        original_sources=builder.original_sources,
        expected_specs=builder.expected_specs,
        dependencies=builder.dependencies,
        path_groups=builder.path_groups,
        open_ports=builder.open_ports,
        output_site=b_site,
        compact_regression=compact_adjacent_regression(),
    )


@lru_cache(maxsize=1)
def structural_scaffold():
    plan = blueprint()
    records = dict(plan.fixed)
    for site in plan.original_sources:
        place(records, site, ZERO_ROLE, "dummy-original-source")

    dynamic = set(plan.expected_specs) | set(plan.open_ports)
    protected = frozenset(dynamic | set(plan.original_sources))
    all_generated_ports: set[Coord] = set()
    for group_index, group in enumerate(plan.path_groups):
        items = tuple(
            (dummy_role(spec), path)
            for spec, path in group
        )
        try:
            records, _outputs, ports = greedy_path_core(
                items,
                constraints=records,
                extra_protected=protected,
            )
        except ValueError as error:
            raise ValueError((
                "path-group-cage-failure",
                group_index,
                tuple((spec, path[0], path[-1], len(path)) for spec, path in group),
                error.args,
            )) from error
        all_generated_ports.update(ports)
        for _spec, path in group:
            wanted = add(path[-1], cable.terminal_direction(path))
            if wanted not in ports:
                raise ValueError(("missing-path-port", group_index, path[-1], wanted, ports))

    # Keep all consumer sites and the final output port genuinely empty.
    core_dynamic = set(plan.expected_specs) | set(plan.open_ports)
    shell = {
        add(site, direction)
        for site in core_dynamic
        for direction in c53.DIRECTIONS
    }
    core = set(records) | core_dynamic | shell
    cage = {
        add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if add(site, direction) not in core
    }
    for site in cage:
        place(records, site, FRAME, "global-cage")

    for site in set(plan.expected_specs) | set(plan.open_ports) | set(plan.original_sources):
        records.pop(site, None)
    return records, frozenset(all_generated_ports)


def row_values(g1: Row, g2: Row, measured: Row):
    if algebra.symplectic(g1, g2):
        raise ValueError(("noncommuting-generators", g1, g2))
    if not any(g1[:4]) or not any(g2[:4]) or g1[:4] == g2[:4]:
        raise ValueError(("invalid-independent-basis", g1, g2))
    product_row = algebra.multiply_commuting(g1, g2)
    return {
        "g1": g1,
        "g2": g2,
        "p": measured,
        "prod": product_row,
    }


def semantic_context(g1: Row, g2: Row, measured: Row):
    rows = row_values(g1, g2, measured)
    candidates = (rows["g1"], rows["g2"], rows["prod"])
    equalities = tuple(int(measured == candidate) for candidate in candidates)
    prefixes = []
    for candidate in candidates:
        equal = True
        local = []
        for left, right in zip(measured, candidate, strict=True):
            equal = equal and left == right
            local.append(int(equal))
        prefixes.append(tuple(local))
    xor_a = equalities[0] ^ equalities[1]
    xor_b = xor_a ^ equalities[2]
    return rows, equalities, tuple(prefixes), xor_a, xor_b


def resolve_spec_role(spec: Spec, context) -> str:
    rows, _equalities, prefixes, xor_a, xor_b = context
    kind = spec[0]
    if kind == "row":
        return joint.pivot.five.ROW_ROLE[rows[str(spec[1])]]
    if kind == "bit":
        return bit(rows[str(spec[1])][int(spec[2])])
    if kind == "status":
        return bit(prefixes[int(spec[1])][int(spec[2])])
    if kind == "xor":
        return bit(xor_a if int(spec[1]) == 0 else xor_b)
    raise ValueError(("unknown-spec", spec))


def resolve_specs(
    g1: Row,
    g2: Row,
    measured: Row,
) -> tuple[dict[Coord, str], dict[str, Row], tuple[int, int, int]]:
    plan = blueprint()
    context = semantic_context(g1, g2, measured)
    rows, equalities, _prefixes, _xor_a, _xor_b = context

    expected = {
        site: resolve_spec_role(spec, context)
        for site, spec in plan.expected_specs.items()
    }
    return expected, rows, equalities


@lru_cache(maxsize=None)
def apparatus(g1: Row, g2: Row, measured: Row):
    plan = blueprint()
    scaffold, generated_ports = structural_scaffold()
    initial = dict(scaffold)
    expected, rows, equalities = resolve_specs(g1, g2, measured)
    for site, label in plan.original_sources.items():
        place(
            initial,
            site,
            joint.pivot.five.ROW_ROLE[rows[label]],
            "original-row-source",
        )
    for site in set(expected) | set(plan.open_ports):
        initial.pop(site, None)
    return (
        initial,
        expected,
        plan.dependencies,
        plan.output_site,
        rows,
        equalities,
        generated_ports,
    )


def enabled(records, law=MEMBERSHIP_RAW):
    return {
        target: law[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in law
    }


def transformed_prepared(prepared, rotation):
    (
        initial,
        expected,
        dependencies,
        output_site,
        rows,
        equalities,
        generated_ports,
    ) = prepared
    shift = (3001, -3011, 3019)
    return (
        c53.transform_records(initial, rotation, shift),
        c53.transform_records(expected, rotation, shift),
        {
            moved(site, rotation, shift): frozenset(
                moved(parent, rotation, shift)
                for parent in parents
            )
            for site, parents in dependencies.items()
        },
        moved(output_site, rotation, shift),
        rows,
        equalities,
        frozenset(
            moved(site, rotation, shift)
            for site in generated_ports
        ),
    )


def schedule_seams(dependencies: dict[Coord, frozenset[Coord]]) -> tuple[tuple[Coord, Coord], ...]:
    sites = set(dependencies)
    seams = set()
    for site in sites:
        for direction in c53.DIRECTIONS:
            neighbor = add(site, direction)
            if (
                neighbor in sites
                and site < neighbor
                and neighbor not in dependencies[site]
                and site not in dependencies[neighbor]
            ):
                seams.add((site, neighbor))
    return tuple(sorted(seams))


def route_occupancy_preflight(plan: Blueprint):
    owners: dict[Coord, list[tuple[int, Spec, Coord, Coord]]] = defaultdict(list)
    boxes = []
    for group_index, group in enumerate(plan.path_groups):
        points = [site for _spec, path in group for site in path]
        lower = tuple(min(site[axis] for site in points) for axis in range(3))
        upper = tuple(max(site[axis] for site in points) for axis in range(3))
        boxes.append((
            group_index,
            tuple(spec for spec, _path in group),
            lower,
            upper,
            len(set(points)),
        ))
        for spec, path in group:
            label = (group_index, spec, path[0], path[-1])
            for site in path[1:]:
                owners[site].append(label)
    collisions = tuple(
        (site, tuple(labels))
        for site, labels in owners.items()
        if len(labels) != 1
    )
    fixed_hits = tuple(sorted(set(owners) & set(plan.fixed)))
    source_hits = tuple(sorted(set(owners) & set(plan.original_sources)))
    return tuple(boxes), collisions, fixed_hits, source_hits


def initial_role_firewall(g1: Row, g2: Row, measured: Row):
    plan = blueprint()
    initial, expected, _dependencies, _output, _rows, _eq, _ports = apparatus(
        g1, g2, measured
    )
    expected_sites = set(expected)
    payload_leaks = tuple(sorted(expected_sites & set(initial)))
    port_leaks = tuple(sorted(plan.open_ports & set(initial)))
    row_roles = set(joint.pivot.five.ROLE_ROW)
    supplied_row_sites = {
        site
        for site, role in initial.items()
        if role in row_roles
    }
    wanted_sources = set(plan.original_sources)
    source_role_failures = tuple(sorted(supplied_row_sites ^ wanted_sources))
    kind_counts = Counter(
        spec[0]
        for site, spec in plan.expected_specs.items()
        if site in initial
    )
    h_controls = []
    for site, role in sorted(plan.fixed.items()):
        if role not in {H0, H1}:
            continue
        consumers = tuple(
            sorted(
                (
                    neighbor,
                    plan.expected_specs[neighbor],
                )
                for direction in c53.DIRECTIONS
                if (
                    (neighbor := add(site, direction))
                    in plan.expected_specs
                    and plan.expected_specs[neighbor][0] == "status"
                )
            )
        )
        category = "unclassified-fixed-h"
        if len(consumers) == 1:
            target, _spec = consumers[0]
            opposite = sub(target, sub(site, target))
            opposite_role = plan.fixed.get(opposite)
            if {role, opposite_role} == {H0, H1}:
                category = "comparator-operator-rail"
            elif role == H1:
                category = "comparator-true-seed"
        h_controls.append((site, role, category, consumers))
    h_category_counts = Counter(item[2] for item in h_controls)
    return {
        "payload_leaks": payload_leaks,
        "port_leaks": port_leaks,
        "source_role_failures": source_role_failures,
        "supplied_sources": tuple(sorted(plan.original_sources.items())),
        "leaked_kinds": tuple(sorted(kind_counts.items())),
        "fixed_h_controls": tuple(h_controls),
        "h_category_counts": tuple(sorted(h_category_counts.items())),
        "strict_no_supplied_intermediate": not h_controls,
    }


def initial_crossfire(g1: Row, g2: Row, measured: Row):
    initial, expected, dependencies, _output, _rows, _eq, _ports = apparatus(
        g1, g2, measured
    )
    actual = enabled(initial)
    wanted = {
        target: frozenset((expected[target],))
        for target, parents in dependencies.items()
        if not parents
    }
    return (
        actual == wanted,
        len(actual),
        len(wanted),
        tuple(sorted(set(actual) - set(wanted)))[:5],
        tuple(sorted(set(wanted) - set(actual)))[:5],
    )


@lru_cache(maxsize=1)
def compiled_local_templates():
    plan = blueprint()
    scaffold, _ports = structural_scaffold()
    templates: Counter[tuple[Spec, tuple[object, ...]]] = Counter()
    unexpected = []
    for site, output_specification in plan.expected_specs.items():
        descriptors = []
        for direction in c53.DIRECTIONS:
            neighbor = add(site, direction)
            if neighbor in scaffold:
                descriptors.append(("constant", scaffold[neighbor]))
            elif neighbor in plan.original_sources:
                descriptors.append(("source", plan.original_sources[neighbor]))
            elif (
                neighbor in plan.expected_specs
                and neighbor in plan.dependencies[site]
            ):
                descriptors.append(("spec", plan.expected_specs[neighbor]))
            elif (
                neighbor in plan.expected_specs
                and site in plan.dependencies[neighbor]
            ):
                descriptors.append(None)
            elif neighbor in plan.expected_specs:
                descriptors.append(("unexpected-dynamic", plan.expected_specs[neighbor]))
                unexpected.append((site, neighbor))
            else:
                descriptors.append(None)
        templates[(output_specification, tuple(descriptors))] += 1
    return templates, tuple(unexpected)


def template_local_check(g1: Row, g2: Row, measured: Row):
    templates, unexpected = compiled_local_templates()
    context = semantic_context(g1, g2, measured)
    rows, equalities, _prefixes, _xor_a, _xor_b = context
    failures = []
    for (output_specification, descriptors), multiplicity in templates.items():
        local_records = {}
        for direction, descriptor in zip(c53.DIRECTIONS, descriptors, strict=True):
            if descriptor is None:
                continue
            descriptor_kind = descriptor[0]
            if descriptor_kind == "constant":
                role = descriptor[1]
            elif descriptor_kind == "source":
                role = joint.pivot.five.ROW_ROLE[rows[str(descriptor[1])]]
            elif descriptor_kind == "spec":
                role = resolve_spec_role(descriptor[1], context)
            else:
                failures.append((
                    "unexpected-dynamic",
                    descriptor,
                    multiplicity,
                ))
                continue
            local_records[direction] = role
        wanted = resolve_spec_role(output_specification, context)
        signature = c53.local_signature(local_records, (0, 0, 0))
        actual = MEMBERSHIP_RAW.get(signature, frozenset())
        if actual != frozenset((wanted,)):
            failures.append((
                output_specification,
                wanted,
                actual,
                signature,
                multiplicity,
            ))
            if len(failures) >= 5:
                break
    supported = equalities[0] ^ equalities[1] ^ equalities[2]
    return (
        not unexpected and not failures,
        tuple(failures),
        len(templates),
        sum(templates.values()),
        equalities,
        supported,
    )


def proper_cubic_equivalence_check():
    plan = blueprint()
    failures = []
    base_sites = (
        set(plan.fixed)
        | set(plan.original_sources)
        | set(plan.expected_specs)
        | set(plan.open_ports)
    )
    comparator_checks = 0
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        direction_image = {
            c53.matvec(rotation, direction)
            for direction in c53.DIRECTIONS
        }
        if direction_image != set(c53.DIRECTIONS):
            failures.append(("directions", rotation_index, direction_image))
        transformed_sites = {
            c53.matvec(rotation, site)
            for site in base_sites
        }
        if len(transformed_sites) != len(base_sites):
            failures.append((
                "site-injectivity",
                rotation_index,
                len(base_sites),
                len(transformed_sites),
            ))
        for table in (DIRECT_COMPARATOR_TABLE, FOLD_COMPARATOR_TABLE):
            for signature, output in table.items():
                comparator_checks += 1
                rotated = c53.rotate_signature(signature, rotation)
                if MEMBERSHIP_RAW.get(rotated, frozenset()) != frozenset((output,)):
                    failures.append((
                        "comparator-law",
                        rotation_index,
                        signature,
                        output,
                        MEMBERSHIP_RAW.get(rotated, frozenset()),
                    ))
    return (
        len(c53.ROTATIONS),
        comparator_checks,
        len(base_sites),
        tuple(failures),
    )


def local_compiled_check(g1: Row, g2: Row, measured: Row, rotation=None):
    prepared = apparatus(g1, g2, measured)
    if rotation is not None:
        prepared = transformed_prepared(prepared, rotation)
    initial, expected, dependencies, output_site, _rows, equalities, _ports = prepared
    failures = []
    for site, output in expected.items():
        local_records = {
            neighbor: initial[neighbor]
            for direction in c53.DIRECTIONS
            if (neighbor := add(site, direction)) in initial
        }
        for parent in dependencies[site]:
            if manhattan(parent, site) == 1:
                local_records[parent] = expected[parent]
        signature = c53.local_signature(local_records, site)
        actual = MEMBERSHIP_RAW.get(signature, frozenset())
        if actual != frozenset((output,)):
            failures.append((site, output, actual, signature, dependencies[site]))
            if len(failures) >= 5:
                break
    supported = equalities[0] ^ equalities[1] ^ equalities[2]
    if expected[output_site] != bit(supported):
        failures.append(("wrong-output", equalities, expected[output_site], supported))
    return not failures, tuple(failures)


def deterministic_run(
    g1: Row,
    g2: Row,
    measured: Row,
    *,
    order: str = "min",
    rotation=None,
    law=MEMBERSHIP_RAW,
):
    prepared = apparatus(g1, g2, measured)
    if rotation is not None:
        prepared = transformed_prepared(prepared, rotation)
    initial, expected, dependencies, output_site, _rows, equalities, _ports = prepared
    records = dict(initial)
    formed: set[Coord] = set()
    actual = enabled(records, law)
    children: dict[Coord, list[Coord]] = defaultdict(list)
    remaining_parents = {
        target: len(parents)
        for target, parents in dependencies.items()
    }
    for child, parents in dependencies.items():
        for parent in parents:
            children[parent].append(child)
    frontier = {
        target
        for target, count in remaining_parents.items()
        if count == 0
    }
    maximum = edges = 0
    while len(formed) < len(expected):
        wanted = {
            target: frozenset((expected[target],))
            for target in frontier
        }
        maximum = max(maximum, len(frontier))
        if actual != wanted:
            return False, (
                "frontier",
                len(formed),
                len(actual),
                len(frontier),
                tuple(sorted(set(actual) - frontier))[:5],
                tuple(sorted(frontier - set(actual)))[:5],
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
        frontier.remove(target)
        for child in children.get(target, ()):
            remaining_parents[child] -= 1
            if remaining_parents[child] == 0:
                frontier.add(child)
        actual.pop(target, None)
        for direction in c53.DIRECTIONS:
            candidate = add(target, direction)
            if candidate in records:
                actual.pop(candidate, None)
                continue
            signature = c53.local_signature(records, candidate)
            if signature in law:
                actual[candidate] = law[signature]
            else:
                actual.pop(candidate, None)
    supported = equalities[0] ^ equalities[1] ^ equalities[2]
    return (
        not actual and records[output_site] == bit(supported),
        (
            len(expected) + 1,
            edges,
            maximum,
            len(initial),
            len(expected),
            equalities,
            supported,
            records[output_site],
            tuple(sorted(actual.items())),
        ),
    )


def formation_records(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
    child: Coord,
):
    records = {
        neighbor: initial[neighbor]
        for direction in c53.DIRECTIONS
        if (neighbor := add(child, direction)) in initial
    }
    for parent in dependencies[child]:
        if manhattan(parent, child) == 1:
            records[parent] = expected[parent]
    return records


def deletion_controls(g1: Row, g2: Row, measured: Row):
    plan = blueprint()
    initial, expected, dependencies, output_site, _rows, _eq, _ports = apparatus(
        g1, g2, measured
    )
    controls = []
    # Every direct dynamic parent and each original variable row source.
    for child, parents in dependencies.items():
        records = formation_records(initial, expected, dependencies, child)
        wanted = expected[child]
        for parent in parents:
            if manhattan(parent, child) != 1:
                continue
            controls.append(("dynamic", parent, child, records, wanted))

    for source_site in plan.original_sources:
        for direction in c53.DIRECTIONS:
            child = add(source_site, direction)
            if child in expected:
                records = formation_records(initial, expected, dependencies, child)
                if source_site in initial and source_site in records:
                    controls.append(("original-source", source_site, child, records, expected[child]))

    # The new direct/fold comparator uses no fixed H record.  Delete every
    # fixed GUIDE/FRAME guard adjacent to a status target as a separate
    # structural-ancestry control.
    for child, specification in plan.expected_specs.items():
        if specification[0] != "status":
            continue
        records = formation_records(initial, expected, dependencies, child)
        for direction in c53.DIRECTIONS:
            parent = add(child, direction)
            if parent in plan.fixed and plan.fixed[parent] in {GUIDE, FRAME}:
                controls.append((
                    "comparator-structural",
                    parent,
                    child,
                    records,
                    expected[child],
                ))

    failures = []
    for label, parent, child, records, wanted in controls:
        local = c53.local_signature(records, child)
        if MEMBERSHIP_RAW.get(local, frozenset()) != frozenset((wanted,)):
            failures.append((label, "baseline", parent, child, wanted, MEMBERSHIP_RAW.get(local)))
            continue
        shortened = dict(records)
        shortened.pop(parent, None)
        actual = MEMBERSHIP_RAW.get(c53.local_signature(shortened, child), frozenset())
        if wanted in actual:
            failures.append((label, "survives", parent, child, wanted, actual))
    return len(controls), tuple(failures), output_site


def valid_ordered_bases():
    return tuple(
        basis
        for state_id in range(60)
        for basis in tableau.all_bases(state_id)
    )


def transcripts():
    for g1, g2 in valid_ordered_bases():
        product_row = algebra.multiply_commuting(g1, g2)
        for supported in (g1, g2, product_row):
            yield g1, g2, supported, True
            yield g1, g2, (*supported[:4], supported[4] ^ 1), False


def main() -> int:
    started = time.time()
    plan = blueprint()
    scaffold, generated_ports = structural_scaffold()
    route_boxes, route_collisions, route_fixed_hits, route_source_hits = (
        route_occupancy_preflight(plan)
    )
    print(
        "LAW",
        len(tap.MERGED_RAW),
        len(joint.SPLITTER_RAW),
        len(signed.SIGN_RAW),
        len(COMPARATOR_RAW),
        len(MEMBERSHIP_RAW),
        len(MEMBERSHIP_CONFLICTS),
        len(joint.MERGED_RAW),
        len(UNIFIED_RAW),
        len(UNIFIED_CONFLICTS),
    )
    print(
        "GEOMETRY",
        len(plan.original_sources),
        len(plan.expected_specs),
        len(scaffold),
        len(plan.path_groups),
        len(generated_ports),
        len(schedule_seams(plan.dependencies)),
    )
    print(
        "ROUTE_PREFLIGHT",
        len(route_boxes),
        len(route_collisions),
        len(route_fixed_hits),
        len(route_source_hits),
    )
    print("COMPACT_REGRESSION", plan.compact_regression)

    domain_failures = []
    accepts = rejects = 0
    match_counts = [0, 0, 0]
    all_transcripts = tuple(transcripts())
    for g1, g2, measured, should_accept in all_transcripts:
        (
            ok,
            detail,
            _template_count,
            _covered_sites,
            equalities,
            supported,
        ) = template_local_check(g1, g2, measured)
        observed = bool(supported)
        if should_accept:
            accepts += 1
            match_counts[equalities.index(1)] += 1
        else:
            rejects += 1
        if not ok or observed != should_accept:
            domain_failures.append((g1, g2, measured, should_accept, detail, equalities))
    print(
        "DOMAIN",
        len(valid_ordered_bases()),
        len(all_transcripts),
        accepts,
        rejects,
        tuple(match_counts),
        len(domain_failures),
    )

    hard = next(
        (g1, g2, measured)
        for g1, g2, measured, should_accept in all_transcripts
        if should_accept
        and measured == algebra.multiply_commuting(g1, g2)
        and measured[4] == 1
    )
    firewall = initial_role_firewall(*hard)
    crossfire = initial_crossfire(*hard)
    print(
        "FIREWALL",
        len(firewall["payload_leaks"]),
        len(firewall["port_leaks"]),
        len(firewall["source_role_failures"]),
        firewall["h_category_counts"],
        firewall["strict_no_supplied_intermediate"],
    )
    print("INITIAL_CROSSFIRE", crossfire)
    covariance = proper_cubic_equivalence_check()
    print("COVARIANCE", covariance[:3], len(covariance[3]))

    min_result = deterministic_run(*hard, order="min")
    max_result = deterministic_run(*hard, order="max")
    print("MIN", min_result)
    print("MAX", max_result)
    physical_rotation_results = tuple(
        (
            rotation_index,
            deterministic_run(
                *hard,
                order="min",
                rotation=c53.ROTATIONS[rotation_index],
            ),
        )
        for rotation_index in range(6)
    )
    print("PHYSICAL_ROTATIONS", physical_rotation_results)

    deletion_count, deletion_failures, output_site = deletion_controls(*hard)
    print("DELETIONS", deletion_count, len(deletion_failures), output_site)
    if (
        domain_failures
        or covariance[3]
        or not min_result[0]
        or not max_result[0]
        or any(not result[0] for _index, result in physical_rotation_results)
        or deletion_failures
    ):
        print(
            "FAILURE_SAMPLE",
            (
                domain_failures[:1],
                covariance[3][:1],
                min_result if not min_result[0] else (),
                max_result if not max_result[0] else (),
                tuple(
                    item
                    for item in physical_rotation_results
                    if not item[1][0]
                )[:1],
                deletion_failures[:3],
            ),
        )

    result = (
        NOTE.is_file()
        and len(tap.MERGED_RAW) == 97_388
        and len(joint.SPLITTER_RAW) == 768
        and len(signed.SIGN_RAW) == 768
        and len(COMPARATOR_RAW) == 288
        and len(MEMBERSHIP_RAW) == 99_212
        and not MEMBERSHIP_CONFLICTS
        and len(UNIFIED_RAW) == 101_708
        and not UNIFIED_CONFLICTS
        and plan.compact_regression[0]
        and len(plan.original_sources) == 3
        and not route_collisions
        and not route_fixed_hits
        and not route_source_hits
        and not schedule_seams(plan.dependencies)
        and not firewall["payload_leaks"]
        and not firewall["port_leaks"]
        and not firewall["source_role_failures"]
        and firewall["strict_no_supplied_intermediate"]
        and crossfire[0]
        and len(valid_ordered_bases()) == 360
        and len(all_transcripts) == 2_160
        and accepts == rejects == 1_080
        and tuple(match_counts) == (360, 360, 360)
        and not domain_failures
        and not covariance[3]
        and min_result[0]
        and max_result[0]
        and all(result[0] for _index, result in physical_rotation_results)
        and deletion_count > 0
        and not deletion_failures
    )
    print("SECONDS", round(time.time() - started, 3))
    print("RESULT", "PHYSICAL_ROW_NATIVE_SIGNED_MEMBERSHIP" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    sys.setrecursionlimit(max(sys.getrecursionlimit(), 100_000))
    raise SystemExit(main())
