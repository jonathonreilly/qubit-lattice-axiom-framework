#!/usr/bin/env python3
"""Cycle 183: bind the compact five-literal bundle to one consumer patch.

Starting from the Cycle-180 spacing-12 recurrent bundle, this probe adds a
value-neutral binary join tree.  Each generated endpoint launches one status
branch and one literal H0/H1 branch.  The status branches join to one all-five
membership lineage, which gates one ordered five-port literal consumer.

No 32-valued payload is reconstructed.  The probe is evidence for generated
finite-bundle membership under one local law, not particle identity or matter.

This runner has no authority.  It edits no foundation, axiom, primitive,
registry, policy, audit, queue, predecessor, commit, push, or PR surface.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import compact_five_literal_lane_spacing_cycle180_2026_07_16 as c180


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "COMPACT_FIVE_LITERAL_MEMBERSHIP_BIND_CYCLE183_NOTE_2026-07-16.md"
)

c178 = c180.c178
c172 = c180.c172
c171 = c178.c171
c53 = c178.c53
cell = c178.cell

Coord = tuple[int, int, int]
RoleMap = dict[Coord, str]

SPACING = c180.MINIMUM_DISJOINT_SPACING
WORDS = c178.WORDS
H0 = c178.H0
H1 = c178.H1

# Three priced apparatus roles.  MEMBER5 is dynamic and value-neutral.  The
# other two are supplied structural frame roles, never membership records.
MEMBER5 = "MEMBER5"
STATUS_FRAME = "MEMBER5_FRAME"
LITERAL_FRAME = "LITERAL_FRAME"
NEW_ROLES = frozenset((MEMBER5, STATUS_FRAME, LITERAL_FRAME))

OFFSETS = c180.offsets(SPACING)
ENDPOINTS = tuple(
    c172.shift(c172.payload_site(c172.COPY_X[-1]), offset)
    for offset in OFFSETS
)
LANE_Y = tuple(site[1] for site in ENDPOINTS)

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


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def lattice_path(
    start: Coord,
    waypoints: tuple[Coord, ...],
) -> tuple[Coord, ...]:
    """Return a nearest-neighbour path excluding start and including endpoints."""

    current = list(start)
    path = []
    for waypoint in waypoints:
        changed_axes = [
            axis
            for axis in range(3)
            if current[axis] != waypoint[axis]
        ]
        if len(changed_axes) > 1:
            raise ValueError(("non-axis-waypoint", tuple(current), waypoint))
        if not changed_axes:
            continue
        axis = changed_axes[0]
        while current[axis] != waypoint[axis]:
            current[axis] += 1 if waypoint[axis] > current[axis] else -1
            path.append(tuple(current))
    if len(path) != len(set(path)):
        raise ValueError(("path-self-contact", start, waypoints))
    return tuple(path)


NODE_KIND: dict[Coord, str] = {}
NODE_LANE: dict[Coord, int | None] = {}
INTENDED_PARENTS: dict[Coord, frozenset[Coord]] = {}


def place_node(
    site: Coord,
    kind: str,
    lane: int | None,
    parents: frozenset[Coord],
) -> Coord:
    if site in NODE_KIND:
        raise ValueError(("dynamic-overlap", site, NODE_KIND[site], kind))
    if not parents or any(manhattan(site, parent) != 1 for parent in parents):
        raise ValueError(("nonlocal-parent", site, parents))
    NODE_KIND[site] = kind
    NODE_LANE[site] = lane
    INTENDED_PARENTS[site] = parents
    return site


def add_path(
    parent: Coord,
    waypoints: tuple[Coord, ...],
    kind: str,
    lane: int | None,
) -> Coord:
    previous = parent
    for site in lattice_path(parent, waypoints):
        place_node(site, kind, lane, frozenset((previous,)))
        previous = site
    return previous


def add_join(left: Coord, right: Coord, target: Coord) -> Coord:
    return place_node(
        target,
        "status",
        None,
        frozenset((left, right)),
    )


# First binary level: (0,1) and (2,3).
STATUS_LEAVES: list[Coord] = []
status_pair_parents: list[tuple[Coord, Coord]] = []
for pair_index, (left_lane, right_lane, join_y) in enumerate(
    ((0, 1, 9), (2, 3, 33))
):
    pair_ends = []
    for lane, parent_y in ((left_lane, join_y - 1), (right_lane, join_y + 1)):
        y = LANE_Y[lane]
        status_leaf = add(ENDPOINTS[lane], (-1, 0, 0))
        STATUS_LEAVES.append(status_leaf)
        pair_ends.append(
            add_path(
                ENDPOINTS[lane],
                (
                    status_leaf,
                    (-27, y, 0),
                    (-35, y, 0),
                    (-35, parent_y, 0),
                ),
                "status",
                lane,
            )
        )
    status_pair_parents.append(tuple(pair_ends))  # type: ignore[arg-type]

J01 = add_join(*status_pair_parents[0], (-35, 9, 0))
J23 = add_join(*status_pair_parents[1], (-35, 33, 0))

# Second binary level: join the first four lanes.
J01_PARENT = add_path(
    J01,
    ((-50, 9, 0), (-50, 20, 0)),
    "status",
    None,
)
J23_PARENT = add_path(
    J23,
    ((-50, 33, 0), (-50, 22, 0)),
    "status",
    None,
)
J0123 = add_join(J01_PARENT, J23_PARENT, (-50, 21, 0))

# Fifth lane and final all-five join.
J0123_PARENT = add_path(
    J0123,
    ((-65, 21, 0), (-65, 39, 0)),
    "status",
    None,
)
lane = 4
y = LANE_Y[lane]
status_leaf = add(ENDPOINTS[lane], (-1, 0, 0))
STATUS_LEAVES.append(status_leaf)
J4_PARENT = add_path(
    ENDPOINTS[lane],
    (
        status_leaf,
        (-27, y, 0),
        (-65, y, 0),
        (-65, 41, 0),
    ),
    "status",
    lane,
)
JFINAL = add_join(J0123_PARENT, J4_PARENT, (-65, 40, 0))

# One all-five status bus reaches the ordered five-port consumer patch.
STATUS_BUS_END = add_path(
    JFINAL,
    (
        (-81, 40, 0),
        (-81, 3, 0),
        (-81, 3, -20),
        (-81, 51, -20),
    ),
    "status",
    None,
)
STATUS_PARENTS = tuple((-81, y, -20) for y in LANE_Y)

# Five literal paths remain separate until each meets the generated all-five
# status bus inside the final consumer patch.
LITERAL_LEAVES: list[Coord] = []
BIT_PARENTS: list[Coord] = []
for lane, y in enumerate(LANE_Y):
    literal_leaf = add(ENDPOINTS[lane], (0, 1, 0))
    place_node(
        literal_leaf,
        "literal",
        lane,
        frozenset((ENDPOINTS[lane],)),
    )
    LITERAL_LEAVES.append(literal_leaf)
    literal_bridge = add(literal_leaf, (-1, 0, 0))
    place_node(
        literal_bridge,
        "literal",
        lane,
        frozenset((literal_leaf, STATUS_LEAVES[lane])),
    )
    BIT_PARENTS.append(
        add_path(
            literal_bridge,
            (
                (-27, y + 1, -22),
                (-79, y + 1, -22),
                (-79, y, -22),
                (-79, y, -20),
            ),
            "literal",
            lane,
        )
    )

CONSUMER_SITES = tuple((-80, y, -20) for y in LANE_Y)
for lane, (bit_parent, status_parent, consumer) in enumerate(
    zip(BIT_PARENTS, STATUS_PARENTS, CONSUMER_SITES, strict=True)
):
    place_node(
        consumer,
        "consumer",
        lane,
        frozenset((bit_parent, status_parent)),
    )

STATUS_LEAVES = tuple(STATUS_LEAVES)
LITERAL_LEAVES = tuple(LITERAL_LEAVES)
BIT_PARENTS = tuple(BIT_PARENTS)
ADDED_SITES = frozenset(NODE_KIND)
JOIN_SITES = frozenset((J01, J23, J0123, JFINAL))


def node_role(site: Coord, word: tuple[int, ...]) -> str:
    kind = NODE_KIND[site]
    if kind == "status":
        return MEMBER5
    lane = NODE_LANE[site]
    if lane is None:
        raise ValueError(("literal-node-without-lane", site, kind))
    return c178.bit_role(word[lane])


def added_expected(word: tuple[int, ...]) -> RoleMap:
    return {
        site: node_role(site, word)
        for site in NODE_KIND
    }


REFERENCE_WORD = (0, 0, 0, 0, 0)
REFERENCE_SOURCES = c180.source_parts(REFERENCE_WORD, SPACING)
REFERENCE_OUTPUTS = c180.output_parts(REFERENCE_WORD, SPACING)
REFERENCE_INITIAL = c180.merge_disjoint(REFERENCE_SOURCES)
REFERENCE_EXPECTED = c180.merge_disjoint(REFERENCE_OUTPUTS)
REFERENCE_EXITS = c180.merge_disjoint(c180.exit_parts(SPACING))
BASE_OCCUPIED = (
    set(REFERENCE_INITIAL)
    | set(REFERENCE_EXPECTED)
    | set(REFERENCE_EXITS)
)
UNUSED_ENDPOINT_FACES = frozenset(
    add(endpoint, (0, 0, -1))
    for endpoint in ENDPOINTS
)


def adjacent_to_base_expected(site: Coord) -> bool:
    return any(
        add(site, direction) in REFERENCE_EXPECTED
        for direction in c53.DIRECTIONS
    )


def make_scaffold() -> RoleMap:
    scaffold: RoleMap = {}

    def frame(site: Coord, role: str, *, required: bool = False) -> None:
        if site in ADDED_SITES or site in BASE_OCCUPIED:
            if required:
                raise ValueError(("required-frame-overlap", site, role))
            return
        if any(
            manhattan(site, unused_face) <= 1
            for unused_face in UNUSED_ENDPOINT_FACES
        ):
            if required:
                raise ValueError(("required-frame-touches-unused-face", site, role))
            return
        if adjacent_to_base_expected(site):
            if required:
                raise ValueError(("required-frame-touches-base-output", site, role))
            return
        scaffold.setdefault(site, role)

    # Opposite-side markers distinguish the two endpoint-facing leaf rules.
    for leaf in STATUS_LEAVES:
        frame(add(leaf, (-1, 0, 0)), STATUS_FRAME, required=True)
    for leaf in LITERAL_LEAVES:
        frame(add(leaf, (0, 1, 0)), LITERAL_FRAME, required=True)

    # Terminal consumer cage: after each literal is written, all six
    # neighbouring sites are occupied by its two parents or literal frames.
    for consumer in CONSUMER_SITES:
        for direction in c53.DIRECTIONS:
            neighbour = add(consumer, direction)
            if neighbour not in ADDED_SITES:
                frame(neighbour, LITERAL_FRAME, required=True)

    # Cage every remote path/join target.  Near the recurrent endpoint the
    # base-output safety filter leaves only markers that cannot change any
    # Cycle-178 firing signature.
    for site in sorted(ADDED_SITES):
        frame_role = (
            STATUS_FRAME
            if NODE_KIND[site] == "status"
            else LITERAL_FRAME
        )
        for direction in c53.DIRECTIONS:
            neighbour = add(site, direction)
            if neighbour not in ADDED_SITES:
                frame(neighbour, frame_role)
    return scaffold


SCAFFOLD = make_scaffold()


def base_parts(word: tuple[int, ...]):
    source_lanes = c180.source_parts(word, SPACING)
    output_lanes = c180.output_parts(word, SPACING)
    initial = c180.merge_disjoint(source_lanes)
    expected = c180.merge_disjoint(output_lanes)
    exits = c180.merge_disjoint(c180.exit_parts(SPACING))
    return source_lanes, output_lanes, initial, expected, exits


def effective_parents(
    target: Coord,
    base_expected: RoleMap,
) -> frozenset[Coord]:
    parents = set(INTENDED_PARENTS[target])
    parents.update(
        neighbour
        for direction in c53.DIRECTIONS
        if (neighbour := add(target, direction)) in base_expected
    )
    return frozenset(parents)


def compile_table():
    table: dict[c53.Signature, set[str]] = defaultdict(set)
    target_rows: dict[Coord, set[c53.Signature]] = defaultdict(set)
    parent_rows: dict[Coord, set[frozenset[Coord]]] = defaultdict(set)
    for word in WORDS:
        _source_lanes, _output_lanes, initial, base_expected, _exits = base_parts(word)
        initial = {**initial, **SCAFFOLD}
        added = added_expected(word)
        expected = {**base_expected, **added}
        for target in ADDED_SITES:
            parents = effective_parents(target, base_expected)
            premise = {
                neighbour: initial[neighbour]
                for direction in c53.DIRECTIONS
                if (neighbour := add(target, direction)) in initial
            }
            premise.update({
                parent: expected[parent]
                for parent in parents
            })
            signature = c53.canonical_signature(
                c53.local_signature(premise, target)
            )
            output = added[target]
            table[signature].add(output)
            target_rows[target].add(signature)
            parent_rows[target].add(parents)
    return table, target_rows, parent_rows


COMPILED_VALUES, TARGET_ROWS, PARENT_ROWS = compile_table()
COMPILE_CONFLICTS = {
    signature: frozenset(outputs)
    for signature, outputs in COMPILED_VALUES.items()
    if len(outputs) != 1
}
COMPILED_TABLE = {
    signature: next(iter(outputs))
    for signature, outputs in COMPILED_VALUES.items()
    if len(outputs) == 1
}
NEW_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in COMPILED_TABLE.items()
))
NEW_RAW_CONFLICTS = {
    signature: outputs
    for signature, outputs in NEW_RAW.items()
    if len(outputs) != 1
}
FULL_RAW = cell.merge_raw(c178.FULL_RAW, NEW_RAW)
FULL_CONFLICTS = {
    signature: outputs
    for signature, outputs in FULL_RAW.items()
    if len(outputs) != 1
}
BASE_OVERLAP = set(c178.FULL_RAW) & set(NEW_RAW)


def apparatus(word: tuple[int, ...]):
    source_lanes, output_lanes, initial, base_expected, exits = base_parts(word)
    added = added_expected(word)
    overlap = (
        (set(initial) & set(SCAFFOLD))
        | (set(base_expected) & set(SCAFFOLD))
        | (set(exits) & set(SCAFFOLD))
        | (set(base_expected) & set(added))
    )
    if overlap:
        raise ValueError(("apparatus-overlap", tuple(sorted(overlap))[:5]))
    return (
        {**initial, **SCAFFOLD},
        {**base_expected, **added},
        exits,
        source_lanes,
        output_lanes,
        base_expected,
        added,
    )


def transformed(
    records,
    rotation,
    shift: Coord,
):
    return c53.transform_records(records, rotation, shift)


def ownership(output_lanes) -> dict[Coord, int]:
    owners = {}
    for lane, records in enumerate(output_lanes):
        for site in records:
            previous = owners.setdefault(site, lane)
            if previous != lane:
                raise ValueError(("owner-conflict", site, previous, lane))
    return owners


def causal_ancestry(certificate, output_lanes):
    base_owner = ownership(output_lanes)
    ancestry: dict[Coord, frozenset[int]] = {}
    remaining = set(certificate["dependencies"])
    while remaining:
        ready = {
            target
            for target in remaining
            if certificate["dependencies"][target] <= ancestry.keys()
        }
        if not ready:
            raise RuntimeError(("ancestry-cycle", len(remaining)))
        for target in ready:
            if target in base_owner:
                value = frozenset((base_owner[target],))
            else:
                value = frozenset().union(*(
                    ancestry[parent]
                    for parent in certificate["dependencies"][target]
                ))
            ancestry[target] = value
        remaining -= ready
    return ancestry


def intended_added_ancestry() -> dict[Coord, frozenset[int]]:
    roots = {
        endpoint: frozenset((lane,))
        for lane, endpoint in enumerate(ENDPOINTS)
    }
    ancestry = dict(roots)
    remaining = set(ADDED_SITES)
    while remaining:
        ready = {
            target
            for target in remaining
            if INTENDED_PARENTS[target] <= ancestry.keys()
        }
        if not ready:
            raise RuntimeError(("intended-ancestry-cycle", len(remaining)))
        for target in ready:
            ancestry[target] = frozenset().union(*(
                ancestry[parent]
                for parent in INTENDED_PARENTS[target]
            ))
        remaining -= ready
    return {
        target: ancestry[target]
        for target in ADDED_SITES
    }


INTENDED_ANCESTRY = intended_added_ancestry()


def new_enabled(records: RoleMap):
    return {
        target: NEW_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in NEW_RAW
    }


def boundary_closure(
    records: RoleMap,
    wanted: RoleMap,
    *,
    order: str,
):
    records = dict(records)
    formed = set()
    actual = new_enabled(records)
    wrong = []
    maximum = 0
    while actual:
        bad = {
            target: values
            for target, values in actual.items()
            if wanted.get(target) != next(iter(values))
        }
        if bad:
            wrong.append((len(formed), bad))
            break
        maximum = max(maximum, len(actual))
        target = min(actual) if order == "min" else max(actual)
        records[target] = wanted[target]
        formed.add(target)
        c171.refresh_after_append(records, actual, target)
        # refresh_after_append reads c171.FULL_RAW; restrict back to the exact
        # join delta for this frozen-boundary control.
        actual = new_enabled(records)
    return {
        "formed": frozenset(formed),
        "wrong": tuple(wrong),
        "terminal": actual,
        "max_frontier": maximum,
    }


def local_endpoint_deletion_checks(word: tuple[int, ...]):
    _source_lanes, _output_lanes, initial, base_expected, _exits = base_parts(word)
    initial = {**initial, **SCAFFOLD}
    expected = {**base_expected, **added_expected(word)}
    failures = []
    attempts = 0
    for lane, endpoint in enumerate(ENDPOINTS):
        for target in (STATUS_LEAVES[lane], LITERAL_LEAVES[lane]):
            parents = effective_parents(target, base_expected)
            premise = {
                neighbour: initial[neighbour]
                for direction in c53.DIRECTIONS
                if (neighbour := add(target, direction)) in initial
            }
            premise.update({
                parent: expected[parent]
                for parent in parents
            })
            wanted = frozenset((expected[target],))
            baseline = FULL_RAW.get(c53.local_signature(premise, target))
            trial = dict(premise)
            trial.pop(endpoint)
            after = FULL_RAW.get(c53.local_signature(trial, target))
            attempts += 1
            if baseline != wanted or after is not None:
                failures.append(
                    (lane, target, baseline, wanted, after, parents)
                )
    return attempts, tuple(failures)


def boundary_controls(word: tuple[int, ...]):
    _source_lanes, _output_lanes, initial, base_expected, _exits = base_parts(word)
    complete_boundary = {**initial, **base_expected, **SCAFFOLD}
    added = added_expected(word)
    failures = []
    shapes = Counter()
    for lane, endpoint in enumerate(ENDPOINTS):
        expected_reachable = frozenset(
            target
            for target, ancestry in INTENDED_ANCESTRY.items()
            if lane not in ancestry
        )
        for label, replacement in (
            ("absent", None),
            ("wrong-phase", add(endpoint, (0, 0, -1))),
        ):
            records = dict(complete_boundary)
            role = records.pop(endpoint)
            if replacement is not None:
                if replacement in records or replacement in SCAFFOLD:
                    failures.append((lane, label, "replacement-occupied", replacement))
                    continue
                records[replacement] = role
            minimum = boundary_closure(records, added, order="min")
            maximum = boundary_closure(records, added, order="max")
            shapes[(
                label,
                len(minimum["formed"]),
                minimum["max_frontier"],
                maximum["max_frontier"],
            )] += 1
            if (
                minimum["wrong"]
                or maximum["wrong"]
                or minimum["formed"] != expected_reachable
                or maximum["formed"] != expected_reachable
                or JFINAL in minimum["formed"]
                or set(CONSUMER_SITES) & set(minimum["formed"])
            ):
                failures.append(
                    (
                        lane,
                        label,
                        minimum,
                        maximum,
                        len(expected_reachable),
                    )
                )
    return shapes, tuple(failures)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    old_full_raw = c171.FULL_RAW
    c171.FULL_RAW = FULL_RAW
    try:
        print("AUTHORITY, ROLES, AND CANDIDATE PRICE")
        check("Cycle-183 review note exists", NOTE.is_file())
        base_roles = {
            role
            for signature, outputs in c178.FULL_RAW.items()
            for _direction, role in signature
        } | {
            role
            for outputs in c178.FULL_RAW.values()
            for role in outputs
        }
        check(
            "the three apparatus roles are fresh and exactly priced",
            NEW_ROLES.isdisjoint(base_roles)
            and MEMBER5 not in SCAFFOLD.values()
            and set(SCAFFOLD.values()) == {STATUS_FRAME, LITERAL_FRAME},
            (
                NEW_ROLES & base_roles,
                Counter(SCAFFOLD.values()),
            ),
        )
        check(
            "the compiled local delta and merged law are deterministic",
            not COMPILE_CONFLICTS
            and not NEW_RAW_CONFLICTS
            and not FULL_CONFLICTS
            and not BASE_OVERLAP
            and all(len(outputs) == 1 for outputs in FULL_RAW.values()),
            (
                len(COMPILED_TABLE),
                len(NEW_RAW),
                len(FULL_RAW),
                len(COMPILE_CONFLICTS),
                len(NEW_RAW_CONFLICTS),
                len(FULL_CONFLICTS),
                len(BASE_OVERLAP),
            ),
        )
        check(
            "the intended join graph is local and has no unintended adjacent pair",
            all(
                all(manhattan(target, parent) == 1 for parent in parents)
                for target, parents in INTENDED_PARENTS.items()
            )
            and not tuple(
                (left, right)
                for left in ADDED_SITES
                for direction in c53.DIRECTIONS
                if (right := add(left, direction)) in ADDED_SITES
                and left < right
                and left not in INTENDED_PARENTS[right]
                and right not in INTENDED_PARENTS[left]
            ),
            (len(ADDED_SITES), len(SCAFFOLD)),
        )

        print("\nTESTED REPAIR AND EXACT ENDPOINT-SEAM PROFILES")
        seam_profiles = Counter()
        covariance_failures = []
        known_wrong_sites = set()
        for bit in (0, 1):
            word = (bit,) * 5
            role = c178.bit_role(bit)
            _source_lanes, _output_lanes, initial, base_expected, _exits = base_parts(word)
            records = {**initial, **base_expected, **SCAFFOLD}
            added = added_expected(word)
            for lane in range(5):
                records[STATUS_LEAVES[lane]] = added[STATUS_LEAVES[lane]]
                records[LITERAL_LEAVES[lane]] = added[LITERAL_LEAVES[lane]]
            for lane, y in enumerate(LANE_Y):
                inherited_site = (-25, y + 1, -1)
                self_site = (-26, y + 1, -2)
                sterile_site = (-26, y, -2)
                known_wrong_sites.update((inherited_site, self_site))

                inherited_signature = c53.local_signature(records, inherited_site)
                self_signature = c53.local_signature(records, self_site)
                sterile_signature = c53.local_signature(records, sterile_site)
                inherited_base = c178.FULL_RAW.get(inherited_signature)
                inherited_new = NEW_RAW.get(inherited_signature)
                self_base = c178.FULL_RAW.get(self_signature)
                self_new = NEW_RAW.get(self_signature)
                sterile_full = FULL_RAW.get(sterile_signature)
                seam_profiles[(
                    bit,
                    inherited_base,
                    inherited_new,
                    self_base,
                    self_new,
                    sterile_full,
                )] += 1

                expected_inherited = (
                    frozenset((H1,))
                    if bit == 0
                    else None
                )
                for rotation_index, rotation in enumerate(c53.ROTATIONS):
                    rotated_inherited = c53.rotate_signature(
                        inherited_signature,
                        rotation,
                    )
                    rotated_self = c53.rotate_signature(
                        self_signature,
                        rotation,
                    )
                    rotated_sterile = c53.rotate_signature(
                        sterile_signature,
                        rotation,
                    )
                    if c178.FULL_RAW.get(rotated_inherited) != expected_inherited:
                        covariance_failures.append(
                            (
                                "inherited",
                                bit,
                                lane,
                                rotation_index,
                                c178.FULL_RAW.get(rotated_inherited),
                                expected_inherited,
                            )
                        )
                    if NEW_RAW.get(rotated_self) != frozenset((role,)):
                        covariance_failures.append(
                            (
                                "self",
                                bit,
                                lane,
                                rotation_index,
                                NEW_RAW.get(rotated_self),
                                frozenset((role,)),
                            )
                        )
                    if FULL_RAW.get(rotated_sterile) is not None:
                        covariance_failures.append(
                            (
                                "sterile",
                                bit,
                                lane,
                                rotation_index,
                                FULL_RAW.get(rotated_sterile),
                            )
                        )
        expected_profiles = Counter({
            (
                0,
                frozenset((H1,)),
                None,
                None,
                frozenset((H0,)),
                None,
            ): 5,
            (
                1,
                None,
                None,
                None,
                frozenset((H1,)),
                None,
            ): 5,
        })
        check(
            "the unused endpoint-minus-z face is sterile after the first repair",
            all(key[-1] is None for key in seam_profiles)
            and sum(seam_profiles.values()) == 10,
            seam_profiles,
        )
        check(
            "the remaining seam has one inherited H0-only flip and one all-bit self-copy",
            seam_profiles == expected_profiles,
            seam_profiles,
        )
        check(
            "both remaining seam signatures and the repaired face are exact in all 24 orientations",
            not covariance_failures,
            tuple(covariance_failures)[:3],
        )

        print("\nALL-32 FULL-HISTORY FAILURE CENSUS")
        full_history_failures = {}
        unexpected_residuals = []
        for word in WORDS:
            (
                initial,
                expected,
                exits,
                _source_lanes,
                output_lanes,
                base_expected,
                added,
            ) = apparatus(word)
            certificate = c171.causal_certificate(initial, expected, exits)
            if certificate["ok"]:
                unexpected_residuals.append((word, "unexpected-positive"))
                continue
            error = certificate["discovery"].get("error")
            full_history_failures[word] = error
            if (
                not error
                or error[1] != "wrong"
                or not set(error[2])
                or not set(error[2]) <= known_wrong_sites
            ):
                unexpected_residuals.append((word, error))
        check(
            "all 32 words fail first at only the two named endpoint-seam classes",
            len(full_history_failures) == 32
            and not unexpected_residuals,
            (
                Counter(
                    error[0]
                    for error in full_history_failures.values()
                ),
                tuple(unexpected_residuals)[:2],
            ),
        )

        print("\nSURVIVING BOUNDED JOIN-TREE FACTS")
        first_cross_nodes = {
            site
            for site, ancestry in INTENDED_ANCESTRY.items()
            if len(ancestry) > 1
            and all(
                len(INTENDED_ANCESTRY.get(parent, frozenset())) == 1
                for parent in INTENDED_PARENTS[site]
                if parent in INTENDED_ANCESTRY
            )
        }
        check(
            "the intended status tree is value-neutral with all-five final ancestry",
            first_cross_nodes == {J01, J23}
            and INTENDED_ANCESTRY[JFINAL] == frozenset(range(5))
            and all(
                INTENDED_ANCESTRY[site] == frozenset(range(5))
                for site in CONSUMER_SITES
            ),
            (
                first_cross_nodes,
                INTENDED_ANCESTRY[JFINAL],
            ),
        )
        check(
            "no 32-valued payload or supplied MEMBER5 is used by the candidate",
            MEMBER5 not in SCAFFOLD.values()
            and {
                node_role(site, (1, 0, 1, 0, 1))
                for site in ADDED_SITES
                if NODE_KIND[site] in {"literal", "consumer"}
            } <= {H0, H1}
            and {
                node_role(site, (1, 0, 1, 0, 1))
                for site in ADDED_SITES
                if NODE_KIND[site] == "status"
            } == {MEMBER5},
        )

        print("\nENDPOINT EDGE DELETION")
        deletion_attempts = 0
        deletion_failures = []
        for word in WORDS:
            attempts, local_failures = local_endpoint_deletion_checks(word)
            deletion_attempts += attempts
            deletion_failures.extend((word, item) for item in local_failures)
        check(
            "all 320 endpoint-to-leaf edge deletions are exact",
            deletion_attempts == 32 * 5 * 2
            and not deletion_failures,
            (deletion_attempts, tuple(deletion_failures)[:2]),
        )

        print("\nSCOPE AND NO-GO DISCIPLINE")
        note = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
        normalized_note = " ".join(note.split())
        check(
            "the note freezes the narrow obstruction, live routes, and N1-N8 gate",
            "02e981979a" in normalized_note
            and "construction-scoped negative" in normalized_note
            and "custom three-role endpoint branch" in normalized_note
            and "typed literal cable" in normalized_note
            and "not a universal binding no-go" in normalized_note
            and "not particle identity" in normalized_note
            and all(f"N{index}" in normalized_note for index in range(1, 9))
            and "No axiom addition follows" in normalized_note,
        )

        print("\nACCOUNTING")
        print("NEW_ROLES", tuple(sorted(NEW_ROLES)))
        print("SCAFFOLD_RECORDS", len(SCAFFOLD), Counter(SCAFFOLD.values()))
        print("ADDED_DYNAMIC_RECORDS", len(ADDED_SITES))
        print("STATUS_DYNAMIC_RECORDS", sum(kind == "status" for kind in NODE_KIND.values()))
        print("LITERAL_DYNAMIC_RECORDS", sum(kind == "literal" for kind in NODE_KIND.values()))
        print("CONSUMER_RECORDS", len(CONSUMER_SITES))
        print("COMPILED_CANONICAL_ROWS", len(COMPILED_TABLE))
        print("NEW_RAW_ROWS", len(NEW_RAW))
        print("FULL_RAW_ROWS", len(FULL_RAW))
        print("SEAM_PROFILES", seam_profiles)
        print("FULL_HISTORY_FAILURES", len(full_history_failures))
        print(
            "FAILURE_STEPS",
            Counter(error[0] for error in full_history_failures.values()),
        )
        print("J01", J01, "J23", J23, "J0123", J0123, "JFINAL", JFINAL)
        print("CONSUMER_SITES", CONSUMER_SITES)
        print("PASS", PASS, "FAIL", FAIL)
        print(
            "RESULT",
            "CUSTOM_LITERAL_ENDPOINT_SEAM_OBSTRUCTION"
            if FAIL == 0
            else "CYCLE183_OPEN",
        )
        return int(FAIL != 0)
    finally:
        c171.FULL_RAW = old_full_raw


if __name__ == "__main__":
    raise SystemExit(main())
