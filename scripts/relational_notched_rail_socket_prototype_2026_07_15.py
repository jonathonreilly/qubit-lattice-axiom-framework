#!/usr/bin/env python3
"""A recurrent notched rail cell that emits H1/R_B01 -> OZ sockets.

A 4x3 cross-section is extended by a two-record tail in phases A/B/C, leaving
one concave notch; D uses the original rectangle so its readout notch has no
extra guard.  The interior launch port still renews the rail.  In each B phase,
the root and guard bordering the notch jointly write one helper.  That helper
and the intervening A context write H1; H1 and the earlier D-phase R_B01 root
match the exact inherited two-parent OZ socket.  Four slices later, the same
rows recur by translation.

This is a local exploratory runner only.  It changes no foundation, registry,
policy, audit state, selected law, or git state.
"""

from __future__ import annotations

from collections import defaultdict, deque

import fragment_safe_role_remap_type_integration_cycle108_2026_07_15 as c108
import self_extending_frame_cage_rail_cycle52_2026_07_14 as c52


Coord = tuple[int, int, int]
YZ = tuple[int, int]
Signature = tuple[tuple[Coord, str], ...]

RECT: frozenset[YZ] = frozenset((y, z) for y in range(4) for z in range(3))
TAIL: frozenset[YZ] = frozenset(((-1, 1), (-1, 2)))
EXTENDED_SHAPE: frozenset[YZ] = RECT | TAIL
ROOT_YZ: YZ = (0, 0)
LOWER_YZ: YZ = (-1, 2)
GUARD_YZ: YZ = (-1, 1)
NOTCH_YZ: YZ = (-1, 0)
PORT_A: YZ = (1, 1)
PORT_B: YZ = (2, 1)
PHASES = ("A", "B", "C", "D")
PERIOD = 4
H0 = "H0"
H1 = "H1"
OZ = "OZ"


PATH_EXTENDED_FORWARD: tuple[YZ, ...] = (
    (1, 1), (1, 2), (0, 2), (-1, 2), (-1, 1), (0, 1), (0, 0),
    (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (2, 1),
)
PATH_EXTENDED_REVERSE = tuple(reversed(PATH_EXTENDED_FORWARD))
SHAPES: dict[str, frozenset[YZ]] = {
    "A": EXTENDED_SHAPE,
    "B": EXTENDED_SHAPE,
    "C": EXTENDED_SHAPE,
    "D": RECT | {LOWER_YZ},
}
PATHS: dict[tuple[str, str], tuple[YZ, ...]] = {
    ("A", "B"): PATH_EXTENDED_FORWARD,
    ("B", "C"): PATH_EXTENDED_REVERSE,
    ("C", "D"): c52.PATH_B,
    ("D", "A"): c52.PATH_A,
}
EXTRA_ORDERS: dict[str, tuple[YZ, ...]] = {
    "A": (LOWER_YZ, GUARD_YZ),
    "B": (),
    "C": (),
    "D": (LOWER_YZ,),
}


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def site(x: int, yz: YZ) -> Coord:
    return (x, yz[0], yz[1])


def mapped_rect_content(phase: str, yz: YZ) -> str:
    abstract = c52.role(phase, yz)
    return c108.ROLE_MAP.get(abstract, abstract)


RECT_CONTENTS = {
    mapped_rect_content(phase, yz)
    for phase in PHASES
    for yz in RECT
}
FULL_ROLES = frozenset(c108.c104.c89.FULL_ROLES)
EXTRA_POOL = tuple(sorted(
    FULL_ROLES - RECT_CONTENTS - {H0, H1, OZ, "R_B01", "BACKSTOP"}
))
if len(EXTRA_POOL) < 8:
    raise RuntimeError(("extra-role-pool", len(EXTRA_POOL)))

CONTENT: dict[tuple[str, YZ], str] = {
    (phase, yz): mapped_rect_content(phase, yz)
    for phase in PHASES
    for yz in RECT
}
TAIL_ROLE_ASSIGNMENT: dict[tuple[str, YZ], str] = {
    ("A", LOWER_YZ): "T_H3",
    ("A", GUARD_YZ): "W3",
    ("B", LOWER_YZ): "AUX",
    ("B", GUARD_YZ): "AUXZ",
    ("C", LOWER_YZ): "COMPLETE",
    ("C", GUARD_YZ): "GU",
    ("D", LOWER_YZ): "GY",
}
CONTENT.update(TAIL_ROLE_ASSIGNMENT)

# Relocate the one existing R_B01 rail value to the D root two slices behind
# the B helper emitter, preserving the exact role multiset.
CONTENT[("D", ROOT_YZ)], CONTENT[("C", (3, 0))] = (
    CONTENT[("C", (3, 0))],
    CONTENT[("D", ROOT_YZ)],
)
HELPER_CONTENT = "JOINT"


def slice_records(x: int, phase: str) -> dict[Coord, str]:
    return {site(x, yz): CONTENT[(phase, yz)] for yz in SHAPES[phase]}


def local_signature(records: dict[Coord, str], target: Coord) -> Signature:
    return tuple(sorted(
        (direction, records[add(target, direction)])
        for direction in c52.DIRECTIONS
        if add(target, direction) in records
    ))


def canonical(signature: Signature) -> Signature:
    return min(c52.rotate_signature(signature, rotation) for rotation in c52.ROTATIONS)


def raw_orbit(signature: Signature, output: str) -> dict[Signature, frozenset[str]]:
    return {
        c52.rotate_signature(signature, rotation): frozenset((output,))
        for rotation in c52.ROTATIONS
    }


def merge_raw(*tables: dict[Signature, frozenset[str]]) -> dict[Signature, frozenset[str]]:
    merged: dict[Signature, set[str]] = defaultdict(set)
    for table in tables:
        for signature, values in table.items():
            merged[signature].update(values)
    return {signature: frozenset(values) for signature, values in merged.items()}


def build_table():
    rows: dict[Signature, str] = {}
    origins: dict[Signature, object] = {}
    for old, new in zip(PHASES, PHASES[1:] + PHASES[:1]):
        records = slice_records(0, old)
        for index, yz in enumerate(PATHS[(old, new)]):
            target = site(1, yz)
            local = local_signature(records, target)
            key = canonical(local)
            output = CONTENT[(new, yz)]
            prior = rows.get(key)
            if prior is not None and prior != output:
                raise RuntimeError(("rail-conflict", old, new, index, prior, output, key))
            rows[key] = output
            origins[key] = ("rail", old, new, index, local)
            records[target] = output
        for extra_index, yz in enumerate(EXTRA_ORDERS[new]):
            target = site(1, yz)
            local = local_signature(records, target)
            key = canonical(local)
            output = CONTENT[(new, yz)]
            prior = rows.get(key)
            if prior is not None and prior != output:
                raise RuntimeError((
                    "extra-conflict", old, new, extra_index, prior, output, key
                ))
            rows[key] = output
            origins[key] = ("extra", old, new, extra_index, local)
            records[target] = output

    q = site(-1, ROOT_YZ)
    blocker = site(0, ROOT_YZ)
    a_guard = site(0, GUARD_YZ)
    root = site(1, ROOT_YZ)
    b_guard = site(1, GUARD_YZ)
    helper = site(1, NOTCH_YZ)
    h1 = site(0, NOTCH_YZ)
    launch = site(-1, NOTCH_YZ)
    exemplar = {
        q: CONTENT[("D", ROOT_YZ)],
        blocker: CONTENT[("A", ROOT_YZ)],
        a_guard: CONTENT[("A", GUARD_YZ)],
        root: CONTENT[("B", ROOT_YZ)],
        b_guard: CONTENT[("B", GUARD_YZ)],
    }
    additions = []
    for label, target, output in (
        ("helper", helper, HELPER_CONTENT),
        ("h1", h1, H1),
        ("oz", launch, OZ),
    ):
        local = local_signature(exemplar, target)
        key = canonical(local)
        prior = rows.get(key)
        if prior is not None and prior != output:
            raise RuntimeError((label, prior, output, local))
        rows[key] = output
        origins[key] = ("socket", label, local)
        additions.append((target, output, local))
        exemplar[target] = output

    raw = merge_raw(*(raw_orbit(signature, output) for signature, output in rows.items()))
    return (
        rows,
        origins,
        raw,
        (q, blocker, a_guard, root, b_guard, helper, h1, launch),
        tuple(additions),
    )


ROWS, ORIGINS, RAW, EXEMPLAR_SOCKET, SOCKET_ADDITIONS = build_table()


def open_candidates(records: dict[Coord, str]) -> frozenset[Coord]:
    return frozenset(
        add(parent, direction)
        for parent in records
        for direction in c52.DIRECTIONS
        if add(parent, direction) not in records
    )


def enabled(records: dict[Coord, str]) -> dict[Coord, frozenset[str]]:
    return {
        target: RAW[local]
        for target in open_candidates(records)
        if (local := local_signature(records, target)) in RAW
    }


def seed_records() -> dict[Coord, str]:
    records = slice_records(-1, "D")
    records[site(-2, PORT_B)] = "BACKSTOP"
    return records


def expected_outputs(last_x: int = 7):
    outputs: dict[Coord, str] = {}
    old = "D"
    for x in range(last_x + 1):
        new = PHASES[x % PERIOD]
        for yz in PATHS[(old, new)]:
            outputs[site(x, yz)] = CONTENT[(new, yz)]
        for yz in EXTRA_ORDERS[new]:
            outputs[site(x, yz)] = CONTENT[(new, yz)]
        old = new

    sockets = []
    for qx in range(-1, last_x + 1, PERIOD):
        ax = qx + 1
        bx = qx + 2
        if bx > last_x:
            continue
        q = site(qx, ROOT_YZ)
        blocker = site(ax, ROOT_YZ)
        a_guard = site(ax, GUARD_YZ)
        root = site(bx, ROOT_YZ)
        b_guard = site(bx, GUARD_YZ)
        helper = site(bx, NOTCH_YZ)
        h1 = site(ax, NOTCH_YZ)
        launch = site(qx, NOTCH_YZ)
        outputs[helper] = HELPER_CONTENT
        outputs[h1] = H1
        outputs[launch] = OZ
        sockets.append((
            q, blocker, a_guard, root, b_guard, helper, h1, launch
        ))
    next_site = site(last_x + 1, PATHS[("D", "A")][0])
    ignored = {next_site: CONTENT[("A", PATHS[("D", "A")][0])]}
    return outputs, tuple(sockets), ignored


def transform_records(
    records: dict[Coord, str],
    rotation: c52.Rotation,
    shift: Coord,
) -> dict[Coord, str]:
    return {
        add(c52.matvec(rotation, position), shift): content
        for position, content in records.items()
    }


def graph(
    rotation: c52.Rotation,
    shift: Coord = (0, 0, 0),
    last_x: int = 7,
    base_records: dict[Coord, str] | None = None,
    include_reached: bool = False,
):
    if last_x % PERIOD != PERIOD - 1:
        raise ValueError(("last_x must end on D", last_x))
    base = transform_records(
        seed_records() if base_records is None else base_records,
        rotation,
        shift,
    )
    expected0, sockets0, ignored0 = expected_outputs(last_x)
    expected = transform_records(expected0, rotation, shift)
    ignored = transform_records(ignored0, rotation, shift)
    ignored_values = {
        target: frozenset((value,)) for target, value in ignored.items()
    }
    sockets = tuple(
        tuple(add(c52.matvec(rotation, item), shift) for item in socket)
        for socket in sockets0
    )
    sites = tuple(sorted(expected))
    index = {position: i for i, position in enumerate(sites)}
    all_mask = (1 << len(sites)) - 1
    queue = deque((0,))
    seen = {0}
    edges = 0
    bad_count = 0
    bad = []
    terminals = []
    while queue:
        mask = queue.popleft()
        records = dict(base)
        records.update({
            position: expected[position]
            for position, i in index.items()
            if mask >> i & 1
        })
        actual = enabled(records)
        wrong = {
            target: values
            for target, values in actual.items()
            if (
                target not in expected
                and ignored.get(target) != next(iter(values))
            )
            or (
                target in expected
                and values != frozenset((expected[target],))
            )
        }
        if wrong:
            bad_count += 1
            if len(bad) < 12:
                details = tuple(
                    (
                        target,
                        values,
                        local_signature(records, target),
                        ORIGINS.get(canonical(local_signature(records, target))),
                    )
                    for target, values in sorted(actual.items())
                    if target in wrong
                )
                bad.append((mask.bit_count(), details))
            continue
        if mask == all_mask:
            if actual != ignored_values:
                bad_count += 1
                if len(bad) < 12:
                    bad.append((mask.bit_count(), "terminal-front", tuple(sorted(actual.items()))))
            else:
                terminals.append(tuple(sorted(actual.items())))
            continue
        futures = [
            target
            for target in actual
            if target in index and not (mask >> index[target] & 1)
        ]
        if not futures:
            bad_count += 1
            if len(bad) < 12:
                bad.append((mask.bit_count(), "dead", tuple(sorted(actual.items()))))
            continue
        for target in futures:
            future = mask | (1 << index[target])
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)
    result = {
        "states": len(seen),
        "edges": edges,
        "bad_count": bad_count,
        "bad": tuple(bad),
        "terminals": tuple(sorted(set(terminals))),
        "expected_count": len(expected),
        "sockets": sockets,
        "ignored": tuple(sorted(ignored.items())),
    }
    if include_reached:
        reached_mask = 0
        for mask in seen:
            reached_mask |= mask
        result["reached"] = tuple(
            position
            for position, i in sorted(index.items())
            if reached_mask >> i & 1
        )
    return result


def controls():
    expected, sockets, _ignored = expected_outputs()
    rail = seed_records()
    rail.update(expected)
    for socket in sockets:
        _q, _blocker, _a_guard, _root, _b_guard, helper, h1, launch = socket
        rail.pop(helper)
        rail.pop(h1)
        rail.pop(launch)
    answers = []
    for socket_index, socket in enumerate(sockets):
        q, blocker, a_guard, root, b_guard, helper, h1, launch = socket
        stages = (
            (
                "helper",
                dict(rail),
                helper,
                (("root", root), ("b_guard", b_guard)),
            ),
            (
                "h1",
                {**rail, helper: HELPER_CONTENT},
                h1,
                (("blocker", blocker), ("a_guard", a_guard), ("helper", helper)),
            ),
            (
                "oz",
                {**rail, helper: HELPER_CONTENT, h1: H1},
                launch,
                (("q", q), ("h1", h1)),
            ),
        )
        for stage, context, target, parents in stages:
            for label, parent in parents:
                deleted = dict(context)
                deleted.pop(parent)
                deleted_actual = enabled(deleted)
                answers.append((
                    socket_index,
                    f"delete_{stage}_{label}",
                    target not in deleted_actual,
                    deleted_actual.get(target),
                ))
                corrupt = dict(context)
                corrupt[parent] = "CORRUPT"
                corrupt_actual = enabled(corrupt)
                answers.append((
                    socket_index,
                    f"corrupt_{stage}_{label}",
                    target not in corrupt_actual,
                    corrupt_actual.get(target),
                ))
    return tuple(answers)


def main() -> None:
    print("SHAPES", {phase: tuple(sorted(shape)) for phase, shape in SHAPES.items()}, "NOTCH", NOTCH_YZ)
    print("PATH_EXTENDED_FORWARD", PATH_EXTENDED_FORWARD)
    print("ROLE_COUNTS", len(set(CONTENT.values())), len(CONTENT), "HELPER", HELPER_CONTENT)
    print("ROLE_CLOSED", set(CONTENT.values()) | {HELPER_CONTENT, H1, OZ} <= FULL_ROLES)
    print("R_B01_SITES", [key for key, value in CONTENT.items() if value == "R_B01"])
    print("ROWS", len(ROWS), "RAW", len(RAW), "CONFLICTS", sum(len(values) != 1 for values in RAW.values()))
    print("SOCKET_EXEMPLAR", EXEMPLAR_SOCKET, SOCKET_ADDITIONS)
    identity = next(
        rotation
        for rotation in c52.ROTATIONS
        if c52.matvec(rotation, (2, 3, 5)) == (2, 3, 5)
    )
    result = graph(identity)
    print("GRAPH", {key: value for key, value in result.items() if key not in {"bad", "sockets"}})
    print("FIRST_BAD", result["bad"][:4])
    print("SOCKETS", result["sockets"])
    longer = graph(identity, last_x=11)
    print("THREE_PERIOD_GRAPH", {
        key: value for key, value in longer.items() if key not in {"bad", "sockets"}
    })
    print("THREE_PERIOD_BAD", longer["bad"][:4])
    initial_q = site(-1, ROOT_YZ)
    next_q = site(3, ROOT_YZ)
    seed = seed_records()
    deleted_seed = dict(seed)
    deleted_seed.pop(initial_q)
    corrupt_seed = dict(seed)
    corrupt_seed[initial_q] = "CORRUPT"
    deleted_result = graph(
        identity,
        base_records=deleted_seed,
        include_reached=True,
    )
    corrupt_result = graph(
        identity,
        base_records=corrupt_seed,
        include_reached=True,
    )
    print("SEED_Q_CONTROLS", {
        "initial_q": initial_q,
        "next_q": next_q,
        "deleted_states": deleted_result["states"],
        "deleted_bad": deleted_result["bad_count"],
        "deleted_next_q_reached": next_q in deleted_result["reached"],
        "corrupt_states": corrupt_result["states"],
        "corrupt_bad": corrupt_result["bad_count"],
        "corrupt_next_q_reached": next_q in corrupt_result["reached"],
    })
    rotated = []
    for index, rotation in enumerate(c52.ROTATIONS):
        item = graph(rotation, (13, -17, 19))
        rotated.append((index, item["bad_count"], len(item["terminals"]), item["states"], item["edges"]))
    print("ROTATED", rotated)
    print("CONTROLS", controls())


if __name__ == "__main__":
    main()
