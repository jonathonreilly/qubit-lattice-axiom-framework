#!/usr/bin/env python3
"""A typed H0/H1 copy cable with straight and covariant turn cells."""

from __future__ import annotations

from collections import deque
import sys

import physical_row_role_literal_fanout_probe_2026_07_15 as fanout


sys.setrecursionlimit(max(sys.getrecursionlimit(), 10_000))


d = fanout.d
c53 = fanout.c53
cell = fanout.cell
Coord = tuple[int, int, int]
Signature = c53.Signature
FRAME = d.CAGE_ROLE
GUIDE_ROLE = d.PREFIX_ROLES[49]
ORIGIN = (0, 0, 0)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def neg(vector: Coord) -> Coord:
    return tuple(-value for value in vector)  # type: ignore[return-value]


def dot(left: Coord, right: Coord) -> int:
    return sum(a * b for a, b in zip(left, right))


def cross(left: Coord, right: Coord) -> Coord:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def straight_guide(back: Coord) -> Coord:
    return next(direction for direction in c53.DIRECTIONS if dot(back, direction) == 0)


def segment_records(
    target: Coord,
    previous: Coord,
    future: Coord,
    value: str,
    guide_override: Coord | None = None,
):
    back = sub(previous, target)
    forward = sub(future, target)
    if back not in c53.DIRECTIONS or forward not in c53.DIRECTIONS:
        raise ValueError((target, previous, future, "nonlocal"))
    if forward == back:
        raise ValueError((target, previous, future, "u-turn"))
    if forward == neg(back):
        guide = straight_guide(back) if guide_override is None else guide_override
        if guide not in c53.DIRECTIONS or dot(back, guide) != 0:
            raise ValueError((back, guide, "invalid-straight-guide"))
        kind = "straight"
    elif dot(back, forward) == 0:
        guide = cross(back, forward)
        kind = "turn"
    else:
        raise ValueError((target, previous, future, "invalid-angle"))
    records = {previous: value, add(target, guide): GUIDE_ROLE}
    for direction in c53.DIRECTIONS:
        site = add(target, direction)
        if site not in {previous, future, add(target, guide)}:
            records[site] = FRAME
    return kind, records


def canonical_local(value: str, kind: str) -> Signature:
    target = ORIGIN
    previous = (0, 0, 1)
    future = (0, 0, -1) if kind == "straight" else (1, 0, 0)
    observed_kind, records = segment_records(target, previous, future, value)
    if observed_kind != kind:
        raise AssertionError((observed_kind, kind))
    return c53.canonical_signature(c53.local_signature(records, target))


CANONICAL_TABLE = {
    canonical_local(value, kind): value
    for value in (d.H0, d.H1)
    for kind in ("straight", "turn")
}
CABLE_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in CANONICAL_TABLE.items()
))
MERGED_RAW = cell.merge_raw(fanout.MERGED_RAW, CABLE_RAW)
RAW_CONFLICTS = {
    signature: values for signature, values in MERGED_RAW.items() if len(values) != 1
}


PATHS: dict[str, tuple[Coord, ...]] = {
    "straight": ((0, 0, 0), (0, 0, -1), (0, 0, -2), (0, 0, -3), (0, 0, -4)),
    "one_turn": ((0, 0, 0), (0, 0, -1), (0, 0, -2), (1, 0, -2), (2, 0, -2)),
    "two_turn": ((0, 0, 0), (0, 0, -1), (1, 0, -1), (1, 1, -1), (1, 2, -1)),
    "three_axis": ((0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0), (2, 1, 1), (2, 1, 2)),
}


def terminal_direction(path: tuple[Coord, ...]) -> Coord:
    return sub(path[-1], path[-2])


def multi_path_core(
    items: tuple[tuple[str, tuple[Coord, ...]], ...],
    constraints: dict[Coord, str] | None = None,
    extra_protected: set[Coord] | frozenset[Coord] = frozenset(),
):
    records: dict[Coord, str] = dict(constraints or {})
    expected: dict[Coord, str] = {}
    terminal_ports: set[Coord] = set()
    for value, path in items:
        prior_source = records.get(path[0])
        if prior_source is not None and prior_source != value:
            raise ValueError((path[0], prior_source, value, "source-conflict"))
        records[path[0]] = value
        for site in path[1:]:
            prior = expected.get(site)
            if prior is not None and prior != value:
                raise ValueError((site, prior, value, "path-output-conflict"))
            expected[site] = value
        terminal_ports.add(add(path[-1], terminal_direction(path)))

    segment_options = []
    segment_labels = []
    protected = set(expected) | terminal_ports | set(extra_protected)
    for value, path in items:
        terminal_port = add(path[-1], terminal_direction(path))
        for index, target in enumerate(path[1:], 1):
            previous = path[index - 1]
            future = path[index + 1] if index + 1 < len(path) else terminal_port
            back = sub(previous, target)
            forward = sub(future, target)
            guides = (
                tuple(direction for direction in c53.DIRECTIONS if dot(back, direction) == 0)
                if forward == neg(back)
                else (None,)
            )
            options = []
            for guide in guides:
                _kind, local_records = segment_records(
                    target, previous, future, value, guide_override=guide
                )
                guards = {
                    site: role
                    for site, role in local_records.items()
                    if site != previous
                }
                if not (set(guards) & protected):
                    options.append(guards)
            segment_options.append(options)
            segment_labels.append((path[0], index, target, previous, future))

    fixed_empty = tuple(
        (segment_labels[index], len(segment_options[index]))
        for index in range(len(segment_options))
        if not any(
            all(
                site not in records or records[site] == role
                for site, role in option.items()
            )
            for option in segment_options[index]
        )
    )
    if fixed_empty:
        raise ValueError(("no-guide-option-against-fixed-records", fixed_empty))

    def compatible(option: dict[Coord, str], placed: dict[Coord, str]) -> bool:
        return all(site not in placed or placed[site] == role for site, role in option.items())

    def choose(remaining: frozenset[int], placed: dict[Coord, str]):
        if not remaining:
            return placed
        domains = {
            index: tuple(
                option for option in segment_options[index]
                if compatible(option, placed)
            )
            for index in remaining
        }
        if any(not domain for domain in domains.values()):
            return None
        index = min(remaining, key=lambda item: (len(domains[item]), item))
        rest = remaining - {index}
        for option in domains[index]:
            trial = {**placed, **option}
            # Forward checking prevents a poor guide choice from launching a
            # global exponential search along an otherwise local cable.
            if all(
                any(compatible(candidate, trial) for candidate in segment_options[future])
                for future in rest
            ):
                result = choose(rest, trial)
                if result is not None:
                    return result
        return None

    chosen = choose(frozenset(range(len(segment_options))), dict(records))
    if chosen is None:
        raise ValueError((
            "no-compatible-guide-assignment",
            tuple(segment_labels),
        ))
    return chosen, expected, frozenset(terminal_ports)


def path_core(
    value: str,
    path: tuple[Coord, ...],
    constraints: dict[Coord, str] | None = None,
    extra_protected: set[Coord] | frozenset[Coord] = frozenset(),
):
    records, expected, terminal_ports = multi_path_core(
        ((value, path),),
        constraints=constraints,
        extra_protected=extra_protected,
    )
    return records, expected, next(iter(terminal_ports))


def apparatus(value: str, path: tuple[Coord, ...]):
    records, expected, terminal_port = path_core(value, path)

    def place(site: Coord, role: str) -> None:
        prior = records.get(site)
        if prior is not None and prior != role:
            raise ValueError((site, prior, role, path))
        records[site] = role

    core = set(records) | set(path) | {terminal_port}
    cage = {
        add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if add(site, direction) not in core
    }
    for site in cage:
        place(site, FRAME)
    for target in path[1:]:
        records.pop(target, None)
    records.pop(terminal_port, None)
    return records, expected, terminal_port


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def graph(value: str, path: tuple[Coord, ...], rotation=None):
    initial, expected, terminal_port = apparatus(value, path)
    if rotation is not None:
        shift = (167, -173, 179)
        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
        terminal_port = next(iter(c53.transform_records({terminal_port: "x"}, rotation, shift)))
    records = dict(initial)
    states = 1
    edges = 0
    bad = []
    for step, (target, output) in enumerate(expected.items()):
        actual = enabled(records)
        wanted = {target: frozenset((output,))}
        if actual != wanted:
            bad.append((step, actual, wanted))
            break
        records[target] = output
        states += 1
        edges += 1
    else:
        if actual := enabled(records):
            bad.append(("terminal", actual))
        if terminal_port in records:
            bad.append(("port-filled", terminal_port, records[terminal_port]))
    return states, edges, tuple(bad), len(initial)


def main() -> int:
    print("ROLE", GUIDE_ROLE)
    print("TABLE", len(CANONICAL_TABLE), len(CABLE_RAW), len(MERGED_RAW), len(RAW_CONFLICTS))
    if RAW_CONFLICTS:
        print("CONFLICT_SAMPLE", tuple(RAW_CONFLICTS.items())[:20])
    failures = []
    sizes = {}
    instances = 0
    for name, path in PATHS.items():
        for value in (d.H0, d.H1):
            for rotation_index, rotation in enumerate(c53.ROTATIONS):
                result = graph(value, path, rotation)
                instances += 1
                sizes.setdefault(name, set()).add(result[3])
                if result[:3] != (len(path), len(path) - 1, ()):
                    failures.append((name, value, rotation_index, result))
    print("PATHS", instances, {name: sorted(values) for name, values in sizes.items()}, len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])
    result = not RAW_CONFLICTS and not failures
    print("RESULT", "PHYSICAL_LITERAL_BIT_CABLE" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
