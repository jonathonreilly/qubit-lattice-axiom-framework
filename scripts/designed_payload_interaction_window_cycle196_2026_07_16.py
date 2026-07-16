#!/usr/bin/env python3
"""Cycle 196: first designed interaction of two compact literal bundles.

One retained H0/H1 egress from each of the two Cycle-192 bundles is routed
into a disjoint local window.  Two retained literal cables meet at one
retained XOR row, preserving both incoming record lineages and appending one
joint H0/H1 record with load-bearing ancestry from both bundles.

This is an authority-free bounded classical interaction construction.  It
edits no foundation, axiom, primitive, registry, policy, audit, queue,
predecessor, commit, push, or PR surface.
"""

from __future__ import annotations

import hashlib
from collections import Counter, deque
from itertools import product
from pathlib import Path

import bare_metal_literal_egress_bind_cycle190_2026_07_16 as c190
import binary_xor_and_record_alu_probe_2026_07_15 as alu
import compact_binary_bundle_transparent_contact_cycle192_2026_07_16 as c192
import physical_literal_bit_cable_probe_2026_07_15 as cable
import recurrent_five_literal_lane_worldline_cycle178_2026_07_16 as c178


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "DESIGNED_PAYLOAD_INTERACTION_WINDOW_CYCLE196_NOTE_2026-07-16.md"
)
CYCLE190_SCRIPT = (
    ROOT / "scripts/bare_metal_literal_egress_bind_cycle190_2026_07_16.py"
)
CYCLE190_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "BARE_METAL_LITERAL_EGRESS_BIND_CYCLE190_NOTE_2026-07-16.md"
)
CYCLE192_SCRIPT = (
    ROOT / "scripts/compact_binary_bundle_transparent_contact_cycle192_2026_07_16.py"
)
CYCLE192_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "COMPACT_BINARY_BUNDLE_TRANSPARENT_CONTACT_CYCLE192_NOTE_2026-07-16.md"
)

FROZEN_CYCLE190_SCRIPT_SHA = (
    "77bafcc6e51759e8a9ad561d2a193e58fdf0699e15c74a8d792f33f999a6d76c"
)
FROZEN_CYCLE190_NOTE_SHA = (
    "37efc07d3fe8ef7d12826d78e752c7368d0164d332f6cc30ee2320eb297d6c85"
)
FROZEN_CYCLE192_SCRIPT_SHA = (
    "349d7fd7fefb1898596bf7fd30b077eff05168d2a9c6cfad51791618eca41b46"
)
FROZEN_CYCLE192_NOTE_SHA = (
    "866820bab8f7db29fb9bbd8939b5b341d39c43d64f797ffd13d1eb7b3e08ed6b"
)

Coord = tuple[int, int, int]
SELECTED_LANE = 2
XOR_GATE: Coord = (-100, 27, -25)
ROTATION_SHIFT: Coord = (30_011, -30_013, 30_029)

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
    return tuple(
        a + b for a, b in zip(left, right, strict=True)
    )  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(
        a - b for a, b in zip(left, right, strict=True)
    )  # type: ignore[return-value]


def scale(factor: int, vector: Coord) -> Coord:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


def shifted(records, offset: Coord):
    return {
        add(site, offset): value
        for site, value in records.items()
    }


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


def line_to(
    path: list[Coord],
    target: Coord,
    axes: tuple[int, ...] = (0, 1, 2),
) -> None:
    current = list(path[-1])
    for axis in axes:
        while current[axis] != target[axis]:
            current[axis] += 1 if target[axis] > current[axis] else -1
            point = tuple(current)  # type: ignore[assignment]
            if point in path:
                raise ValueError(("path-self-contact", point, target))
            path.append(point)


def bit(value: int) -> str:
    return c178.H1 if value else c178.H0


def xor_gate_geometry(center: Coord):
    """Cycle-169 orientation: two inputs, XOR role, two frame records."""

    first = add(center, (0, 0, 1))
    second = add(center, (1, 0, 0))
    fixed = {
        add(center, (-1, 0, 0)): alu.XOR_ROLE,
        add(center, (0, 1, 0)): alu.FRAME_ROLE,
        add(center, (0, -1, 0)): alu.FRAME_ROLE,
    }
    return first, second, fixed


def prefix_join_graph(
    initial: dict[Coord, str],
    paths: tuple[tuple[Coord, ...], tuple[Coord, ...]],
    center: Coord,
    values: tuple[int, int],
    law,
):
    """Exhaust every reachable two-prefix state and the final XOR append."""

    expected_paths = tuple(
        {
            site: bit(value)
            for site in path[1:]
        }
        for value, path in zip(values, paths, strict=True)
    )
    expected_output = bit(values[0] ^ values[1])

    def enabled(records):
        return {
            target: law[signature]
            for target in c178.c53.open_candidates(records)
            if (
                signature := c178.c53.local_signature(records, target)
            ) in law
        }

    queue = deque(((0, 0, False),))
    seen = {(0, 0, False)}
    edges = 0
    maximum = 0
    terminals = 0
    bad = []
    history_counts = {(0, 0, False): 1}
    path_lengths = tuple(len(path) - 1 for path in paths)

    while queue:
        left_count, right_count, joined = queue.popleft()
        records = dict(initial)
        for path, count, value in zip(
            paths,
            (left_count, right_count),
            values,
            strict=True,
        ):
            records.update({
                site: bit(value)
                for site in path[1 : count + 1]
            })
        if joined:
            records[center] = expected_output

        actual = enabled(records)
        wanted = {}
        if left_count < path_lengths[0]:
            target = paths[0][left_count + 1]
            wanted[target] = frozenset((expected_paths[0][target],))
        if right_count < path_lengths[1]:
            target = paths[1][right_count + 1]
            wanted[target] = frozenset((expected_paths[1][target],))
        if (
            left_count == path_lengths[0]
            and right_count == path_lengths[1]
            and not joined
        ):
            wanted[center] = frozenset((expected_output,))

        if actual != wanted:
            bad.append(((left_count, right_count, joined), actual, wanted))
            continue
        maximum = max(maximum, len(wanted))
        if joined:
            terminals += 1
            continue

        successors = []
        if left_count < path_lengths[0]:
            successors.append((left_count + 1, right_count, False))
        if right_count < path_lengths[1]:
            successors.append((left_count, right_count + 1, False))
        if not successors:
            successors.append((left_count, right_count, True))
        for successor in successors:
            edges += 1
            history_counts[successor] = (
                history_counts.get(successor, 0)
                + history_counts[(left_count, right_count, joined)]
            )
            if successor not in seen:
                seen.add(successor)
                queue.append(successor)

    terminal_state = (path_lengths[0], path_lengths[1], True)
    return {
        "states": len(seen),
        "edges": edges,
        "terminals": terminals,
        "maximum": maximum,
        "histories": history_counts.get(terminal_state, 0),
        "bad": tuple(bad),
        "path_lengths": path_lengths,
    }


def canonical_xor_subset():
    return {
        signature: output
        for signature, output in alu.CANONICAL_TABLE.items()
        if alu.XOR_ROLE in {
            role for _direction, role in signature
        }
    }


def raw_subset(table):
    return cable.cell.merge_raw(*(
        cable.cell.raw_orbit(signature, output)
        for signature, output in table.items()
    ))


def selected_word(value: int) -> tuple[int, int, int, int, int]:
    return tuple(
        value if lane == SELECTED_LANE else 0
        for lane in range(5)
    )  # type: ignore[return-value]


def merge_records(*parts: dict[Coord, str]) -> dict[Coord, str]:
    merged: dict[Coord, str] = {}
    for part in parts:
        for site, role in part.items():
            place(merged, site, role, "merge")
    return merged


def pair_base(left_value: int, right_value: int):
    left_word = selected_word(left_value)
    right_word = selected_word(right_value)
    (
        left_sources,
        left_outputs,
        left_initial,
        left_expected,
        left_exits,
    ) = c190.base_parts(left_word)
    (
        right_sources,
        right_outputs,
        right_initial,
        right_expected,
        right_exits,
    ) = c190.base_parts(right_word)
    offset = c192.CONTACT_OFFSET
    return {
        "left_word": left_word,
        "right_word": right_word,
        "left_sources": left_sources,
        "right_sources": tuple(
            shifted(part, offset) for part in right_sources
        ),
        "left_outputs": left_outputs,
        "right_outputs": tuple(
            shifted(part, offset) for part in right_outputs
        ),
        "initial": merge_records(
            left_initial,
            shifted(right_initial, offset),
        ),
        "expected": merge_records(
            left_expected,
            shifted(right_expected, offset),
        ),
        "exits": {
            **left_exits,
            **shifted(right_exits, offset),
        },
    }


LEFT_ENDPOINT = c190.ENDPOINTS[SELECTED_LANE]
LEFT_TERMINAL = c190.TERMINAL_BITS[SELECTED_LANE]
RIGHT_ENDPOINT = add(LEFT_ENDPOINT, c192.CONTACT_OFFSET)
RIGHT_TERMINAL = add(LEFT_TERMINAL, c192.CONTACT_OFFSET)

LEFT_STEM = c190.STEM_PATHS[SELECTED_LANE]
RIGHT_STEM = tuple(
    add(site, c192.CONTACT_OFFSET) for site in LEFT_STEM
)
LEFT_IDENTITY = c190.STATUS_CABLE_PATHS[SELECTED_LANE]
RIGHT_IDENTITY = tuple(
    add(site, c192.CONTACT_OFFSET) for site in LEFT_IDENTITY
)


def interaction_paths():
    first_input, second_input, _fixed = xor_gate_geometry(XOR_GATE)

    left = [LEFT_TERMINAL]
    line_to(left, (-46, 27, -12), (2,))
    line_to(left, (-100, 27, -12), (0,))
    line_to(left, first_input, (2,))

    right = [RIGHT_TERMINAL]
    line_to(right, (-46, 27, 6), (2,))
    line_to(right, (-46, 29, 6), (1,))
    line_to(right, (-90, 29, 6), (0,))
    line_to(right, (-90, 29, -25), (2,))
    line_to(right, (-90, 27, -25), (1,))
    line_to(right, second_input, (0,))

    if sub(XOR_GATE, left[-1]) != sub(left[-1], left[-2]):
        raise ValueError(("left-gate-direction", left[-2:], XOR_GATE))
    if sub(XOR_GATE, right[-1]) != sub(right[-1], right[-2]):
        raise ValueError(("right-gate-direction", right[-2:], XOR_GATE))
    if set(left).intersection(right):
        raise ValueError(("interaction-path-overlap", set(left) & set(right)))
    return tuple(left), tuple(right)


LEFT_INTERACTION, RIGHT_INTERACTION = interaction_paths()

PATH_SIDES = (
    (0, LEFT_STEM),
    (0, LEFT_IDENTITY),
    (0, LEFT_INTERACTION),
    (1, RIGHT_STEM),
    (1, RIGHT_IDENTITY),
    (1, RIGHT_INTERACTION),
)

EXTENSION_PATH_SITES = frozenset(
    site
    for _side, path in PATH_SIDES
    for site in path[1:]
)
EXTENSION_DYNAMIC = (
    EXTENSION_PATH_SITES
    | {LEFT_TERMINAL, RIGHT_TERMINAL, XOR_GATE}
)

EXTENSION_PARENTS: dict[Coord, frozenset[Coord]] = {}
for _side, path in PATH_SIDES:
    for previous, target in zip(path[:-1], path[1:], strict=True):
        wanted = frozenset((previous,))
        prior = EXTENSION_PARENTS.setdefault(target, wanted)
        if prior != wanted:
            raise ValueError(("path-parent-conflict", target, prior, wanted))
EXTENSION_PARENTS[LEFT_TERMINAL] = frozenset((LEFT_STEM[-1],))
EXTENSION_PARENTS[RIGHT_TERMINAL] = frozenset((RIGHT_STEM[-1],))
EXTENSION_PARENTS[XOR_GATE] = frozenset((
    LEFT_INTERACTION[-1],
    RIGHT_INTERACTION[-1],
))

LEFT_IDENTITY_EXIT = add(
    LEFT_IDENTITY[-1],
    sub(LEFT_IDENTITY[-1], LEFT_IDENTITY[-2]),
)
RIGHT_IDENTITY_EXIT = add(
    RIGHT_IDENTITY[-1],
    sub(RIGHT_IDENTITY[-1], RIGHT_IDENTITY[-2]),
)
IDENTITY_EXITS = (LEFT_IDENTITY_EXIT, RIGHT_IDENTITY_EXIT)


def selected_caps() -> dict[Coord, str]:
    records = {}
    for endpoint, terminal in (
        (LEFT_ENDPOINT, LEFT_TERMINAL),
        (RIGHT_ENDPOINT, RIGHT_TERMINAL),
    ):
        records[add(endpoint, (0, 1, 0))] = c190.EGRESS_CAP
        records[add(endpoint, (0, 0, -1))] = c190.EGRESS_CAP
        records[add(terminal, (0, 1, 0))] = c190.EGRESS_CAP
    return records


SELECTED_CAPS = selected_caps()


def build_interaction_scaffold():
    reference = pair_base(0, 0)
    _first, _second, gate_fixed = xor_gate_geometry(XOR_GATE)
    constraints = merge_records(
        reference["initial"],
        reference["expected"],
        SELECTED_CAPS,
        gate_fixed,
    )
    path_items = tuple(
        (c178.H0, path)
        for _side, path in PATH_SIDES
    )
    records, cable_expected, terminal_ports = cable.multi_path_core(
        path_items,
        constraints=constraints,
        extra_protected=(
            EXTENSION_DYNAMIC
            | set(reference["exits"])
            | set(IDENTITY_EXITS)
            | {XOR_GATE}
        ),
    )
    wanted_ports = {
        LEFT_TERMINAL,
        RIGHT_TERMINAL,
        LEFT_IDENTITY_EXIT,
        RIGHT_IDENTITY_EXIT,
        XOR_GATE,
    }
    if set(cable_expected) != set(EXTENSION_PATH_SITES):
        raise ValueError((
            "cable-dynamic-mismatch",
            len(set(cable_expected) ^ set(EXTENSION_PATH_SITES)),
        ))
    if set(terminal_ports) != wanted_ports:
        raise ValueError(("terminal-port-mismatch", terminal_ports, wanted_ports))

    base_sites = set(reference["initial"]) | set(reference["expected"])
    scaffold = {
        site: role
        for site, role in records.items()
        if site not in base_sites
        and site not in EXTENSION_DYNAMIC
        and site not in terminal_ports
    }

    # The cable grammar fixes every direct formation neighbourhood.  A second
    # shell of retained FRAME records closes the exposed furniture and the
    # three fixed XOR parents without changing any declared local signature.
    protected = (
        set(reference["initial"])
        | set(reference["expected"])
        | set(reference["exits"])
        | set(EXTENSION_DYNAMIC)
        | set(terminal_ports)
    )
    dynamic_shell = {
        add(site, direction)
        for site in EXTENSION_DYNAMIC
        for direction in c178.c53.DIRECTIONS
    }
    core = (
        set(scaffold)
        | set(EXTENSION_DYNAMIC)
        | set(terminal_ports)
        | dynamic_shell
    )
    cage = {
        add(site, direction)
        for site in core
        for direction in c178.c53.DIRECTIONS
        if add(site, direction) not in core
        and add(site, direction) not in protected
        and add(site, direction)[0] <= -28
    }
    for site in cage:
        place(scaffold, site, cable.FRAME, "interaction-cage")
    for site in EXTENSION_DYNAMIC | set(terminal_ports):
        scaffold.pop(site, None)
    return scaffold, frozenset(terminal_ports), frozenset(cage)


INTERACTION_SCAFFOLD, OBSERVED_PORTS, INTERACTION_CAGE = (
    build_interaction_scaffold()
)


def extension_expected(left_value: int, right_value: int):
    expected = {}
    for side, path in PATH_SIDES:
        value = left_value if side == 0 else right_value
        for site in path[1:]:
            place(expected, site, bit(value), "extension-path")
    place(expected, LEFT_TERMINAL, bit(left_value), "left-terminal")
    place(expected, RIGHT_TERMINAL, bit(right_value), "right-terminal")
    place(
        expected,
        XOR_GATE,
        bit(left_value ^ right_value),
        "xor-output",
    )
    return expected


def interaction_apparatus(left_value: int, right_value: int):
    base = pair_base(left_value, right_value)
    extension = extension_expected(left_value, right_value)
    initial = merge_records(base["initial"], INTERACTION_SCAFFOLD)
    expected = merge_records(base["expected"], extension)
    # The outer retained FRAME shell makes the two identity continuations
    # terminal records.  Only the twenty inherited recurrent exits remain
    # enabled after the joint XOR write.
    exits = dict(base["exits"])
    overlap = set(initial) & set(expected)
    if overlap:
        raise ValueError(("initial-expected-overlap", tuple(sorted(overlap))[:5]))
    return initial, expected, exits, base, extension


def local_formation_premise(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    target: Coord,
):
    premise = {
        neighbor: initial[neighbor]
        for direction in c178.c53.DIRECTIONS
        if (neighbor := add(target, direction)) in initial
    }
    premise.update({
        parent: expected[parent]
        for parent in EXTENSION_PARENTS[target]
    })
    return premise


def certificate_premise(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
    target: Coord,
):
    premise = {
        neighbor: initial[neighbor]
        for direction in c178.c53.DIRECTIONS
        if (neighbor := add(target, direction)) in initial
    }
    premise.update({
        parent: expected[parent]
        for parent in dependencies[target]
    })
    return premise


def lineage_ancestry(certificate, base):
    owners = {}
    for side, parts in enumerate((
        base["left_outputs"],
        base["right_outputs"],
    )):
        for lane, records in enumerate(parts):
            for site in records:
                owners[site] = frozenset(((side, lane),))

    ancestry: dict[Coord, frozenset[tuple[int, int]]] = {}
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
            if target in owners:
                ancestry[target] = owners[target]
            else:
                ancestry[target] = frozenset().union(*(
                    ancestry[parent]
                    for parent in certificate["dependencies"][target]
                ))
        remaining -= ready
    return ancestry


def variable_initial_sites():
    initials = {
        pair: interaction_apparatus(*pair)[0]
        for pair in product((0, 1), repeat=2)
    }
    sites = set().union(*(set(records) for records in initials.values()))
    variable = {
        site
        for site in sites
        if len({records.get(site) for records in initials.values()}) > 1
    }
    lane_offset = c190.OFFSETS[SELECTED_LANE]
    left_seed = add(
        c190.c172.payload_site(c190.c172.SEED_X),
        lane_offset,
    )
    right_seed = add(left_seed, c192.CONTACT_OFFSET)
    return variable, (left_seed, right_seed)


def deletion_controls(certificates):
    attempts = []
    failures = []
    lane_offset = c190.OFFSETS[SELECTED_LANE]
    left_seed = add(
        c190.c172.payload_site(c190.c172.SEED_X),
        lane_offset,
    )
    left_first = add(
        c190.c172.payload_site(c190.c172.COPY_X[0]),
        lane_offset,
    )
    right_seed = add(left_seed, c192.CONTACT_OFFSET)
    right_first = add(left_first, c192.CONTACT_OFFSET)

    for pair, certificate in certificates.items():
        initial, expected, _exits, _base, _extension = (
            interaction_apparatus(*pair)
        )
        dependencies = certificate["dependencies"]
        controls = (
            ("source-left", left_first, left_seed),
            ("source-right", right_first, right_seed),
            ("egress-left", LEFT_STEM[1], LEFT_ENDPOINT),
            ("egress-right", RIGHT_STEM[1], RIGHT_ENDPOINT),
            ("terminal-left", LEFT_TERMINAL, LEFT_STEM[-1]),
            ("terminal-right", RIGHT_TERMINAL, RIGHT_STEM[-1]),
            ("joint-left", XOR_GATE, LEFT_INTERACTION[-1]),
            ("joint-right", XOR_GATE, RIGHT_INTERACTION[-1]),
        )
        for label, target, parent in controls:
            premise = certificate_premise(
                initial,
                expected,
                dependencies,
                target,
            )
            baseline = c190.FULL_RAW.get(
                c178.c53.local_signature(premise, target)
            )
            trial = dict(premise)
            trial.pop(parent)
            observed = c190.FULL_RAW.get(
                c178.c53.local_signature(trial, target)
            )
            wanted = frozenset((expected[target],))
            attempts.append((pair, label, target, parent, baseline, observed))
            if baseline != wanted or (
                observed is not None and expected[target] in observed
            ):
                failures.append(attempts[-1])
    return tuple(attempts), tuple(failures)


def flip_controls():
    extensions = {
        pair: extension_expected(*pair)
        for pair in product((0, 1), repeat=2)
    }
    left_sites = {
        site
        for side, path in PATH_SIDES
        if side == 0
        for site in path[1:]
    } | {LEFT_TERMINAL}
    right_sites = {
        site
        for side, path in PATH_SIDES
        if side == 1
        for site in path[1:]
    } | {RIGHT_TERMINAL}
    failures = []
    attempts = 0
    for fixed_right in (0, 1):
        before = extensions[(0, fixed_right)]
        after = extensions[(1, fixed_right)]
        attempts += 1
        if not (
            all(before[site] != after[site] for site in left_sites)
            and all(before[site] == after[site] for site in right_sites)
            and before[XOR_GATE] != after[XOR_GATE]
        ):
            failures.append(("left", fixed_right))
    for fixed_left in (0, 1):
        before = extensions[(fixed_left, 0)]
        after = extensions[(fixed_left, 1)]
        attempts += 1
        if not (
            all(before[site] != after[site] for site in right_sites)
            and all(before[site] == after[site] for site in left_sites)
            and before[XOR_GATE] != after[XOR_GATE]
        ):
            failures.append(("right", fixed_left))
    return attempts, tuple(failures)


def transform_site(site: Coord, rotation):
    return add(c178.c53.matvec(rotation, site), ROTATION_SHIFT)


def covariance_census():
    checks = 0
    local_failures = []
    terminal_failures = []
    for rotation_index, rotation in enumerate(c178.c53.ROTATIONS):
        for pair in product((0, 1), repeat=2):
            initial, expected, exits, _base, _extension = (
                interaction_apparatus(*pair)
            )
            for target in EXTENSION_DYNAMIC:
                premise = local_formation_premise(initial, expected, target)
                rotated_premise = {
                    transform_site(site, rotation): role
                    for site, role in premise.items()
                }
                rotated_target = transform_site(target, rotation)
                observed = c190.FULL_RAW.get(
                    c178.c53.local_signature(
                        rotated_premise,
                        rotated_target,
                    )
                )
                checks += 1
                if observed != frozenset((expected[target],)):
                    local_failures.append((
                        rotation_index,
                        pair,
                        target,
                        expected[target],
                        observed,
                    ))
                    break

            # A proper rotation of the complete terminal corpus must expose
            # exactly the proper rotation of the twenty inherited exits.
            final_records = {**initial, **expected}
            rotated_final = {
                transform_site(site, rotation): role
                for site, role in final_records.items()
            }
            rotated_exits = {
                transform_site(site, rotation): roles
                for site, roles in exits.items()
            }
            observed_exits = {
                target: c190.FULL_RAW[signature]
                for target in c178.c53.open_candidates(rotated_final)
                if (
                    signature := c178.c53.local_signature(
                        rotated_final,
                        target,
                    )
                ) in c190.FULL_RAW
            }
            if observed_exits != rotated_exits:
                terminal_failures.append((
                    rotation_index,
                    pair,
                    len(observed_exits),
                    len(rotated_exits),
                    tuple(sorted(set(observed_exits) ^ set(rotated_exits)))[:3],
                ))
    return checks, tuple(local_failures), tuple(terminal_failures)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    old_full_raw = c190.c171.FULL_RAW
    c190.c171.FULL_RAW = c190.FULL_RAW
    try:
        print("AUTHORITY AND FROZEN PREDECESSORS")
        check(
            "Cycles 190 and 192 frozen hashes match",
            sha256(CYCLE190_SCRIPT) == FROZEN_CYCLE190_SCRIPT_SHA
            and sha256(CYCLE190_NOTE) == FROZEN_CYCLE190_NOTE_SHA
            and sha256(CYCLE192_SCRIPT) == FROZEN_CYCLE192_SCRIPT_SHA
            and sha256(CYCLE192_NOTE) == FROZEN_CYCLE192_NOTE_SHA,
            (
                sha256(CYCLE190_SCRIPT),
                sha256(CYCLE190_NOTE),
                sha256(CYCLE192_SCRIPT),
                sha256(CYCLE192_NOTE),
            ),
        )

        print("\nRETAINED INTERACTION ATOMS AND PRICE")
        xor_table = canonical_xor_subset()
        xor_raw = raw_subset(xor_table)
        check(
            "the retained law contains the exact four-case XOR family",
            len(xor_table) == 4
            and len(xor_raw) == 96
            and all(
                c190.FULL_RAW.get(row) == values
                for row, values in xor_raw.items()
            ),
            (len(xor_table), len(xor_raw)),
        )
        check(
            "the retained literal cable family is present literally",
            len(cable.CANONICAL_TABLE) == 4
            and len(cable.CABLE_RAW) == 96
            and all(
                c190.FULL_RAW.get(row) == values
                for row, values in cable.CABLE_RAW.items()
            ),
            (len(cable.CANONICAL_TABLE), len(cable.CABLE_RAW)),
        )
        check(
            "the interaction adds zero rows and zero onsite roles",
            len(c190.COMPILED_TABLE) == 16
            and len(c190.NEW_RAW) == 342
            and len(c190.FULL_RAW) == 102_338
            and not c190.FULL_CONFLICTS
            and c190.MEMBER5 not in INTERACTION_SCAFFOLD.values()
            and set(extension_expected(0, 1).values()) <= {c178.H0, c178.H1},
            {
                "interaction_canonical_rows": 0,
                "interaction_raw_rows": 0,
                "interaction_roles": 0,
                "cycle190_full_raw": len(c190.FULL_RAW),
                "scaffold_roles": Counter(INTERACTION_SCAFFOLD.values()),
            },
        )

        print("\nDESIGNED GEOMETRY")
        pair_support = pair_base(0, 0)
        route_intersections = (
            set(LEFT_INTERACTION) & set(RIGHT_INTERACTION)
        )
        check(
            "two selected endpoint forks route to one disjoint local window",
            LEFT_STEM[0] == LEFT_ENDPOINT
            and RIGHT_STEM[0] == RIGHT_ENDPOINT
            and LEFT_IDENTITY[0] == LEFT_TERMINAL
            and RIGHT_IDENTITY[0] == RIGHT_TERMINAL
            and LEFT_INTERACTION[0] == LEFT_TERMINAL
            and RIGHT_INTERACTION[0] == RIGHT_TERMINAL
            and not route_intersections
            and set(INTERACTION_SCAFFOLD).isdisjoint(EXTENSION_DYNAMIC)
            and set(pair_support["initial"]).isdisjoint(
                set(pair_support["expected"])
            ),
            {
                "left_endpoint": LEFT_ENDPOINT,
                "right_endpoint": RIGHT_ENDPOINT,
                "left_terminal": LEFT_TERMINAL,
                "right_terminal": RIGHT_TERMINAL,
                "gate": XOR_GATE,
                "dynamic": len(EXTENSION_DYNAMIC),
                "scaffold": len(INTERACTION_SCAFFOLD),
                "cage": len(INTERACTION_CAGE),
            },
        )
        check(
            "the joint record has exactly the two routed literal parents",
            EXTENSION_PARENTS[XOR_GATE]
            == frozenset((
                LEFT_INTERACTION[-1],
                RIGHT_INTERACTION[-1],
            ))
            and all(
                sum(abs(value) for value in sub(parent, XOR_GATE)) == 1
                for parent in EXTENSION_PARENTS[XOR_GATE]
            ),
            EXTENSION_PARENTS[XOR_GATE],
        )

        print("\nFOUR INPUTS AND FULL-HISTORY CONFLUENCE")
        certificates = {}
        shapes = Counter()
        certificate_failures = []
        truth_table = {}
        for pair in product((0, 1), repeat=2):
            initial, expected, exits, base, _extension = (
                interaction_apparatus(*pair)
            )
            certificate = c190.c171.causal_certificate(
                initial,
                expected,
                exits,
            )
            certificates[pair] = certificate
            truth_table[pair] = expected[XOR_GATE]
            if not certificate["ok"]:
                certificate_failures.append((
                    pair,
                    certificate.get("discovery", {}).get("error"),
                    certificate.get("minimum", {}).get("error"),
                    certificate.get("maximum", {}).get("error"),
                ))
                continue
            shapes[(
                certificate["minimum"]["states"],
                certificate["edge_checks"]["edges"],
                certificate["minimum"]["max_frontier"],
                certificate["maximum"]["max_frontier"],
                len(certificate["unordered"]),
                len(certificate["minimum"]["terminal"]),
            )] += 1
        check(
            "H0/H0, H0/H1, H1/H0, and H1/H1 all close exactly",
            not certificate_failures
            and shapes == Counter({(3_256, 7_126, 31, 31, 0, 20): 4}),
            (shapes, certificate_failures),
        )
        check(
            "the appended joint record is exact XOR",
            truth_table == {
                (0, 0): c178.H0,
                (0, 1): c178.H1,
                (1, 0): c178.H1,
                (1, 1): c178.H0,
            },
            truth_table,
        )
        check(
            "determinism plus zero adjacent unordered pairs proves every history confluent",
            all(
                certificate["minimum"]["ok"]
                and certificate["maximum"]["ok"]
                and not certificate["unordered"]
                and not certificate["edge_checks"]["signature_failures"]
                and not certificate["edge_checks"]["deletion_failures"]
                for certificate in certificates.values()
            ),
            {
                pair: (
                    certificate["minimum"]["max_frontier"],
                    certificate["maximum"]["max_frontier"],
                    len(certificate["unordered"]),
                )
                for pair, certificate in certificates.items()
            },
        )

        print("\nLITERAL LINEAGES, ANCESTRY, AND INPUT FIREWALL")
        ancestry_failures = []
        for pair, certificate in certificates.items():
            _initial, expected, _exits, base, _extension = (
                interaction_apparatus(*pair)
            )
            ancestry = lineage_ancestry(certificate, base)
            wanted_joint = frozenset(((0, SELECTED_LANE), (1, SELECTED_LANE)))
            if (
                ancestry[XOR_GATE] != wanted_joint
                or ancestry[LEFT_IDENTITY[-1]]
                != frozenset(((0, SELECTED_LANE),))
                or ancestry[RIGHT_IDENTITY[-1]]
                != frozenset(((1, SELECTED_LANE),))
                or expected[LEFT_IDENTITY[-1]] != bit(pair[0])
                or expected[RIGHT_IDENTITY[-1]] != bit(pair[1])
            ):
                ancestry_failures.append((
                    pair,
                    ancestry[XOR_GATE],
                    ancestry[LEFT_IDENTITY[-1]],
                    ancestry[RIGHT_IDENTITY[-1]],
                ))
        check(
            "both literal continuations survive and the joint ancestry is exactly two-lane",
            not ancestry_failures,
            ancestry_failures,
        )
        variable, wanted_variable = variable_initial_sites()
        check(
            "only the two original selected seeds vary across the four preparations",
            variable == set(wanted_variable)
            and all(
                c190.MEMBER5 not in interaction_apparatus(*pair)[0].values()
                for pair in product((0, 1), repeat=2)
            ),
            (variable, wanted_variable),
        )
        check(
            "no four-valued or 32-valued payload role is reconstructed",
            all(
                set(extension_expected(*pair).values()) <= {c178.H0, c178.H1}
                for pair in product((0, 1), repeat=2)
            )
            and not (
                set().union(*(
                    set(extension_expected(*pair).values())
                    for pair in product((0, 1), repeat=2)
                ))
                & set(c178.c175.NEW_ROW_ROLES)
            ),
            set().union(*(
                set(extension_expected(*pair).values())
                for pair in product((0, 1), repeat=2)
            )),
        )

        print("\nDELETION AND FLIP CONTROLS")
        deletion_attempts, deletion_failures = deletion_controls(certificates)
        check(
            "all source, egress, terminal, and joint-parent deletions are load-bearing",
            len(deletion_attempts) == 32 and not deletion_failures,
            (len(deletion_attempts), deletion_failures[:2]),
        )
        flip_attempts, flip_failures = flip_controls()
        check(
            "all four one-input flips change only that lineage and the XOR record",
            flip_attempts == 4 and not flip_failures,
            (flip_attempts, flip_failures),
        )

        print("\nALL-24 PROPER-CUBIC COVARIANCE")
        rotation_checks, rotation_failures, terminal_failures = covariance_census()
        check(
            "all four inputs are locally exact in all 24 proper-cubic images",
            rotation_checks == 24 * 4 * len(EXTENSION_DYNAMIC)
            and not rotation_failures
            and all(
                c178.c53.determinant(rotation) == 1
                for rotation in c178.c53.ROTATIONS
            ),
            (rotation_checks, rotation_failures[:1]),
        )
        check(
            "all 96 rotated terminal corpora expose exactly the inherited exits",
            not terminal_failures,
            terminal_failures[:2],
        )

        print("\nPREDECESSOR COEXISTENCE")
        transparent = c192.pair_bundle(c192.ZERO, c192.ONE)
        transparent_certificate = c190.c171.causal_certificate(
            transparent["initial"],
            transparent["expected"],
            transparent["exits"],
        )
        check(
            "the untouched Cycle-192 transparent pair retains its exact certificate",
            transparent_certificate["ok"]
            and transparent_certificate["minimum"]["states"] == 3_041
            and transparent_certificate["edge_checks"]["edges"] == 6_910
            and len(transparent_certificate["minimum"]["terminal"]) == 20,
            (
                transparent_certificate.get("ok"),
                transparent_certificate.get("minimum", {}).get("states"),
                transparent_certificate.get("edge_checks", {}).get("edges"),
            ),
        )
        predecessor = c190.apparatus((1, 0, 1, 0, 1))
        predecessor_certificate = c190.c171.causal_certificate(
            predecessor[0],
            predecessor[1],
            predecessor[2],
        )
        check(
            "the frozen Cycle-190 five-lane consumer remains exact under the same law",
            predecessor_certificate["ok"]
            and predecessor_certificate["minimum"]["states"] == 2_289
            and predecessor_certificate["edge_checks"]["edges"] == 4_232,
            (
                predecessor_certificate.get("ok"),
                predecessor_certificate.get("minimum", {}).get("states"),
                predecessor_certificate.get("edge_checks", {}).get("edges"),
            ),
        )

        print("\nSCOPE")
        normalized = (
            " ".join(NOTE.read_text(encoding="utf-8").lower().split())
            if NOTE.is_file()
            else ""
        )
        required = (
            "classical physical interaction prerequisite",
            "not quantum scattering",
            "zero new rows and zero new roles",
            "no supplied value-dependent intermediate",
            "inherited cycle-178 rotated-schedule boundary",
            "no axiom addition follows",
            "no foundation, axiom, primitive, registry, policy, or audit edit",
        )
        missing = tuple(phrase for phrase in required if phrase not in normalized)
        check(
            "the note states the exact positive scope and inherited boundary",
            not missing,
            missing,
        )

        print("\nACCOUNTING")
        print("SELECTED_LANE", SELECTED_LANE)
        print("ENDPOINTS", LEFT_ENDPOINT, RIGHT_ENDPOINT)
        print("TERMINALS", LEFT_TERMINAL, RIGHT_TERMINAL)
        print("IDENTITY_ENDPOINTS", LEFT_IDENTITY[-1], RIGHT_IDENTITY[-1])
        print("INTERACTION_INPUTS", LEFT_INTERACTION[-1], RIGHT_INTERACTION[-1])
        print("XOR_GATE", XOR_GATE)
        print("INTERACTION_SCAFFOLD", len(INTERACTION_SCAFFOLD))
        print("INTERACTION_DYNAMIC", len(EXTENSION_DYNAMIC))
        print("FULL_RAW_ROWS", len(c190.FULL_RAW))
        print("FOUR_CASE_SHAPES", shapes)
        print("ROTATION_CHECKS", rotation_checks)
        print("DELETION_CONTROLS", len(deletion_attempts))
        print("FLIP_CONTROLS", flip_attempts)
        print("PASS", PASS, "FAIL", FAIL)
        print(
            "RESULT",
            "DESIGNED_PAYLOAD_XOR_INTERACTION_WINDOW"
            if FAIL == 0
            else "CYCLE196_NEEDS_REPAIR",
        )
        return 0 if FAIL == 0 else 1
    finally:
        c190.c171.FULL_RAW = old_full_raw


if __name__ == "__main__":
    raise SystemExit(main())
