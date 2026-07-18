#!/usr/bin/env python3
"""Cycle 171: autonomous signed-row recurrence on the Cycle-144 rail.

One finite completed Cycle-144 boundary is extended by three period-four
recurrent cells.  A signed Pauli-row seed and a finite rear guide head are
placed beside the second completed recurrent socket.  Generated rail records
then carry the guide and the unchanged signed row through three further
socket generations.

This runner has no authority.  It edits no foundation, primitive, registry,
policy, audit, queue, predecessor, commit, push, or PR surface.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path

import physical_r_b01_recurrent_root_bind_cycle144_2026_07_15 as c144
import physical_row_role_fork_cable_probe_2026_07_15 as c162
import physical_joint_stabilizer_update_cycle166_2026_07_16 as c166
import two_recurrent_post_oz_payloads_cycle142_2026_07_15 as c142


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "AUTONOMOUS_SIGNED_ROW_RECURRENT_SIDECAR_CYCLE171_NOTE_2026-07-16.md"
)

b = c144.b
c141 = c142.c141
cell = c141.cell
c53 = c144.c53
Coord = tuple[int, int, int]

ROW_ROLES = tuple(c162.ROW_ROLES)
GUIDE_ROLE = "BACKSTOP"
REAR_STOP_ROLE = "MARK"
PAYLOAD_YZ = (-1, 3)
GUIDE_YZ = (0, 3)
SEED_X = 7
COPY_X = tuple(range(8, 22))
GENERATION_X = (7, 11, 15, 19)

# These are the seven extra fronts visible from the incomplete Cycle-141
# boundary under the later Cycle-162 law.  The completed Cycle-144 boundary
# occupies four targets and changes the local contexts at the other three.
INCOMPLETE_BOUNDARY_FRONTS = {
    (5, 4, 1): "R_A10",
    (3, 2, -2): "H0",
    (-1, 3, -2): "R_C01",
    (-4, 4, 0): "R1",
    (-4, 2, 0): "R1",
    (-4, 3, 1): "R1",
    (-5, 3, 0): "R1",
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


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def shift(site: Coord, dx: int) -> Coord:
    return (site[0] + dx, site[1], site[2])


PAYLOAD_SITE = {
    x: c141.transform_site(cell.site(x, PAYLOAD_YZ))
    for x in range(SEED_X - 1, COPY_X[-1] + 1)
}
GUIDE_SITE = {
    x: c141.transform_site(cell.site(x, GUIDE_YZ))
    for x in range(SEED_X - 1, COPY_X[-1] + 1)
}


def completed_boundary() -> dict[Coord, str]:
    return {**b.FACTOR_SOURCE, **b.FACTOR_OUTPUTS}


def standard_rail_extension() -> dict[Coord, str]:
    """Three translated recurrent cells after the Cycle-144 terminal."""

    outputs: dict[Coord, str] = {}
    old = "B"
    for x, new in zip(range(10, 22), ("C", "D", "A", "B") * 3):
        for yz in cell.PATHS[(old, new)]:
            outputs[cell.site(x, yz)] = cell.CONTENT[(new, yz)]
        for yz in cell.EXTRA_ORDERS[new]:
            outputs[cell.site(x, yz)] = cell.CONTENT[(new, yz)]
        old = new

    for root_x in GENERATION_X[1:]:
        outputs[cell.site(root_x, cell.NOTCH_YZ)] = cell.OZ
        outputs[cell.site(root_x + 1, cell.NOTCH_YZ)] = cell.H1
        outputs[cell.site(root_x + 2, cell.NOTCH_YZ)] = cell.HELPER_CONTENT
        outputs[cell.site(root_x, (-1, 1))] = "R_LB"
        outputs[cell.site(root_x, (-2, 1))] = "R_C22"
        outputs[cell.site(root_x, (-3, 1))] = "J1"
    return outputs


STANDARD_RAIL_EXTENSION = standard_rail_extension()
RAIL_EXTENSION = {
    c141.transform_site(site): value
    for site, value in STANDARD_RAIL_EXTENSION.items()
}


def physical_root_sidecars() -> dict[Coord, str]:
    outputs: dict[Coord, str] = {}
    for dx in (-4, -8, -12):
        for site, value in (*b.SIDECAR_TRUNK, *b.SIDECAR_SHELL):
            outputs[shift(site, dx)] = value
    return outputs


PHYSICAL_ROOT_SIDECARS = physical_root_sidecars()


def source(row_role: str) -> dict[Coord, str]:
    records = completed_boundary()
    records[PAYLOAD_SITE[SEED_X]] = row_role
    records[GUIDE_SITE[SEED_X]] = GUIDE_ROLE
    records[GUIDE_SITE[SEED_X - 1]] = REAR_STOP_ROLE
    return records


def outputs(row_role: str) -> dict[Coord, str]:
    return {
        **RAIL_EXTENSION,
        **PHYSICAL_ROOT_SIDECARS,
        **{GUIDE_SITE[x]: GUIDE_ROLE for x in COPY_X},
        **{PAYLOAD_SITE[x]: row_role for x in COPY_X},
    }


def ignored_fronts() -> dict[Coord, frozenset[str]]:
    next_yz = cell.PATHS[("B", "C")][0]
    return {
        c141.transform_site(cell.site(22, next_yz)):
        frozenset((cell.CONTENT[("C", next_yz)],)),
        (-21, -1, 0): frozenset(("B1",)),
    }


IGNORED = ignored_fronts()


def canonical_sidecar_table(
    row_roles: tuple[str, ...] = ROW_ROLES,
) -> dict[c53.Signature, str]:
    table: dict[c53.Signature, str] = {}
    fixed = {
        **completed_boundary(),
        **RAIL_EXTENSION,
        **PHYSICAL_ROOT_SIDECARS,
    }
    for row_role in row_roles:
        records = {
            **fixed,
            PAYLOAD_SITE[SEED_X]: row_role,
            GUIDE_SITE[SEED_X]: GUIDE_ROLE,
            GUIDE_SITE[SEED_X - 1]: REAR_STOP_ROLE,
        }
        for x in COPY_X:
            guide_local = c53.canonical_signature(
                c53.local_signature(records, GUIDE_SITE[x])
            )
            previous = table.get(guide_local)
            if previous is not None and previous != GUIDE_ROLE:
                raise ValueError(("guide-canonical-conflict", x, previous))
            table[guide_local] = GUIDE_ROLE
            records[GUIDE_SITE[x]] = GUIDE_ROLE

            payload_local = c53.canonical_signature(
                c53.local_signature(records, PAYLOAD_SITE[x])
            )
            previous = table.get(payload_local)
            if previous is not None and previous != row_role:
                raise ValueError(
                    ("payload-canonical-conflict", row_role, x, previous)
                )
            table[payload_local] = row_role
            records[PAYLOAD_SITE[x]] = row_role
    return table


SIDECAR_TABLE = canonical_sidecar_table()
SIDECAR_RAW = cell.merge_raw(*(
    cell.raw_orbit(local, output)
    for local, output in SIDECAR_TABLE.items()
))
BASE_RAW = c166.p.MERGED_RAW
FULL_RAW = cell.merge_raw(BASE_RAW, SIDECAR_RAW)
RAW_CONFLICTS = {
    local: values
    for local, values in FULL_RAW.items()
    if len(values) != 1
}


def stock_enabled(records: dict[Coord, str]) -> dict[Coord, frozenset[str]]:
    return {
        target: FULL_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in FULL_RAW
    }


@dataclass(frozen=True)
class Candidate:
    target: Coord
    output_bit: int | None
    dynamic_mask: int
    values_by_mask: dict[int, frozenset[str]]


def candidate_shell(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
) -> tuple[Coord, ...]:
    occupied = set(initial) | set(expected)
    return tuple(sorted(
        {
            add(site, direction)
            for site in occupied
            for direction in c53.DIRECTIONS
            if add(site, direction) not in initial
        }
        | set(expected)
        | set(IGNORED)
    ))


def preindex_candidates(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
):
    sites = tuple(sorted(expected))
    index = {site: bit for bit, site in enumerate(sites)}
    candidates = []
    for target in candidate_shell(initial, expected):
        fixed: list[tuple[Coord, str]] = []
        dynamic: list[tuple[int, Coord, str]] = []
        for direction in c53.DIRECTIONS:
            neighbour = add(target, direction)
            if neighbour in initial:
                fixed.append((direction, initial[neighbour]))
            elif neighbour in index:
                dynamic.append(
                    (index[neighbour], direction, expected[neighbour])
                )
        values_by_mask: dict[int, frozenset[str]] = {}
        for subset in range(1 << len(dynamic)):
            global_mask = 0
            local = list(fixed)
            for item, (bit, direction, value) in enumerate(dynamic):
                if subset >> item & 1:
                    global_mask |= 1 << bit
                    local.append((direction, value))
            signature = tuple(sorted(local))
            values = FULL_RAW.get(signature)
            if values is not None:
                values_by_mask[global_mask] = values
        if values_by_mask:
            candidates.append(Candidate(
                target=target,
                output_bit=index.get(target),
                dynamic_mask=sum(1 << bit for bit, _d, _v in dynamic),
                values_by_mask=values_by_mask,
            ))
    return sites, index, tuple(candidates)


def preindexed_enabled(
    mask: int,
    candidates: tuple[Candidate, ...],
) -> dict[Coord, frozenset[str]]:
    actual = {}
    for candidate in candidates:
        if (
            candidate.output_bit is not None
            and mask >> candidate.output_bit & 1
        ):
            continue
        values = candidate.values_by_mask.get(mask & candidate.dynamic_mask)
        if values is not None:
            actual[candidate.target] = values
    return actual


def records_at(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    index: dict[Coord, int],
    mask: int,
) -> dict[Coord, str]:
    records = dict(initial)
    records.update({
        site: expected[site]
        for site, bit in index.items()
        if mask >> bit & 1
    })
    return records


def exact_graph(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    *,
    state_limit: int = 5_000_000,
    stock_crosschecks: int = 128,
    check_diamonds: bool = True,
):
    sites, index, candidates = preindex_candidates(initial, expected)
    candidate_by_target = {
        candidate.target: candidate
        for candidate in candidates
    }
    all_mask = (1 << len(sites)) - 1
    queue = deque((0,))
    seen = {0}
    edges = 0
    terminals = 0
    maximum = 0
    bad = []
    mandatory = {site: all_mask for site in sites}
    append_seen = Counter()
    checked = 0
    crosscheck_failures = []
    diamond_pairs = 0
    diamond_failures = []

    while queue:
        mask = queue.popleft()
        actual = preindexed_enabled(mask, candidates)
        if checked < stock_crosschecks:
            stock = stock_enabled(records_at(initial, expected, index, mask))
            checked += 1
            if stock != actual:
                crosscheck_failures.append((mask, stock, actual))
                break

        wrong = {
            target: values
            for target, values in actual.items()
            if (
                target in expected
                and values != frozenset((expected[target],))
            ) or (
                target not in expected
                and IGNORED.get(target) != values
            )
        }
        if wrong:
            bad.append((mask.bit_count(), "wrong", tuple(sorted(wrong.items()))))
            continue
        if mask == all_mask:
            if actual == IGNORED:
                terminals += 1
            else:
                bad.append((mask.bit_count(), "terminal", actual))
            continue

        futures = tuple(sorted(
            target
            for target, values in actual.items()
            if target in index
            and not (mask >> index[target] & 1)
            and values == frozenset((expected[target],))
        ))
        maximum = max(maximum, len(futures))
        if not futures:
            bad.append((mask.bit_count(), "dead", actual))
            continue

        # Check the exact commuting diamond for every co-enabled pair.  Only
        # the opposite target's six-neighbour signature can change after one
        # append, so testing that candidate directly is equivalent to
        # recomputing the complete frontier twice.
        if check_diamonds:
            for left, right in combinations(futures, 2):
                diamond_pairs += 1
                left_candidate = candidate_by_target[left]
                right_candidate = candidate_by_target[right]
                after_left_mask = mask | (1 << index[left])
                after_right_mask = mask | (1 << index[right])
                right_values = right_candidate.values_by_mask.get(
                    after_left_mask & right_candidate.dynamic_mask
                )
                left_values = left_candidate.values_by_mask.get(
                    after_right_mask & left_candidate.dynamic_mask
                )
                if (
                    right_values != frozenset((expected[right],))
                    or left_values != frozenset((expected[left],))
                ):
                    diamond_failures.append(
                        (mask.bit_count(), left, right)
                    )
                    break
        if diamond_failures:
            break

        for target in futures:
            mandatory[target] &= mask
            append_seen[target] += 1
            future = mask | (1 << index[target])
            edges += 1
            if future not in seen:
                if len(seen) >= state_limit:
                    bad.append((mask.bit_count(), "state-limit", state_limit))
                    queue.clear()
                    break
                seen.add(future)
                queue.append(future)

    reached = frozenset(
        site
        for site, count in append_seen.items()
        if count
    )
    return {
        "states": len(seen),
        "edges": edges,
        "terminals": terminals,
        "max_frontier": maximum,
        "bad": tuple(bad),
        "mandatory": mandatory,
        "append_seen": append_seen,
        "reached": reached,
        "index": index,
        "candidates": candidates,
        "stock_crosschecks": checked,
        "crosscheck_failures": tuple(crosscheck_failures),
        "diamond_pairs": diamond_pairs,
        "diamond_failures": tuple(diamond_failures),
    }


def refresh_after_append(
    records: dict[Coord, str],
    actual: dict[Coord, frozenset[str]],
    target: Coord,
) -> None:
    """Update the exact enabled set after one append-only nearest-neighbour write."""

    actual.pop(target, None)
    for direction in c53.DIRECTIONS:
        candidate = add(target, direction)
        if candidate in records:
            actual.pop(candidate, None)
            continue
        signature = c53.local_signature(records, candidate)
        values = FULL_RAW.get(signature)
        if values is None:
            actual.pop(candidate, None)
        else:
            actual[candidate] = values


def split_frontier(
    actual: dict[Coord, frozenset[str]],
    exits: dict[Coord, frozenset[str]],
) -> tuple[dict[Coord, frozenset[str]], dict[Coord, frozenset[str]]]:
    exposed_exits = {
        target: values
        for target, values in actual.items()
        if exits.get(target) == values
    }
    dynamic = {
        target: values
        for target, values in actual.items()
        if target not in exposed_exits
    }
    return dynamic, exposed_exits


def discover_causal_dependencies(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    exits: dict[Coord, frozenset[str]],
    *,
    order: str = "min",
):
    """Discover the direct local parent graph along one exact law replay."""

    records = dict(initial)
    formed: set[Coord] = set()
    dependencies: dict[Coord, frozenset[Coord]] = {}
    actual = stock_enabled(records)
    maximum = 0
    edge_visits = 0
    exit_first_step: dict[Coord, int] = {}

    while len(formed) < len(expected):
        dynamic, exposed_exits = split_frontier(actual, exits)
        for target in exposed_exits:
            exit_first_step.setdefault(target, len(formed))
        declared_values = {
            target: frozenset((expected[target],))
            for target in expected
            if target not in formed
        }
        wrong = {
            target: values
            for target, values in dynamic.items()
            if declared_values.get(target) != values
        }
        if wrong or not dynamic:
            return {
                "ok": False,
                "error": (
                    len(formed),
                    "wrong" if wrong else "dead",
                    wrong if wrong else actual,
                ),
                "error_signatures": {
                    target: c53.local_signature(records, target)
                    for target in wrong
                },
                "dependencies": dependencies,
            }
        maximum = max(maximum, len(dynamic))
        edge_visits += len(dynamic)
        if order == "min":
            target = min(dynamic)
        elif order == "max":
            target = max(dynamic)
        else:
            raise ValueError(("unknown-order", order))
        dependencies[target] = frozenset(
            neighbour
            for direction in c53.DIRECTIONS
            if (
                (neighbour := add(target, direction)) in formed
                and neighbour in expected
            )
        )
        records[target] = expected[target]
        formed.add(target)
        refresh_after_append(records, actual, target)

    return {
        "ok": actual == exits,
        "error": None if actual == exits else ("terminal", actual, exits),
        "dependencies": dependencies,
        "states": len(formed) + 1,
        "edge_visits": edge_visits,
        "max_frontier": maximum,
        "terminal": actual,
        "exit_first_step": exit_first_step,
    }


def causal_replay(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    exits: dict[Coord, frozenset[str]],
    dependencies: dict[Coord, frozenset[Coord]],
    *,
    order: str,
):
    """Replay a declared parent graph and require exact frontier equality."""

    records = dict(initial)
    formed: set[Coord] = set()
    actual = stock_enabled(records)
    maximum = 0
    edge_visits = 0
    exit_first_step: dict[Coord, int] = {}

    while len(formed) < len(expected):
        dynamic, exposed_exits = split_frontier(actual, exits)
        for target in exposed_exits:
            exit_first_step.setdefault(target, len(formed))
        declared = {
            target: frozenset((expected[target],))
            for target, parents in dependencies.items()
            if target not in formed and parents <= formed
        }
        maximum = max(maximum, len(declared))
        edge_visits += len(declared)
        if dynamic != declared:
            mismatched = set(dynamic) ^ set(declared)
            mismatched.update(
                target
                for target in set(dynamic) & set(declared)
                if dynamic[target] != declared[target]
            )
            return {
                "ok": False,
                "error": (
                    len(formed),
                    dynamic,
                    declared,
                    exposed_exits,
                ),
                "error_signatures": {
                    target: c53.local_signature(records, target)
                    for target in mismatched
                },
            }
        if order == "min":
            target = min(declared)
        elif order == "max":
            target = max(declared)
        else:
            raise ValueError(("unknown-order", order))
        records[target] = expected[target]
        formed.add(target)
        refresh_after_append(records, actual, target)

    return {
        "ok": actual == exits,
        "error": None if actual == exits else ("terminal", actual, exits),
        "states": len(formed) + 1,
        "edge_visits": edge_visits,
        "max_frontier": maximum,
        "terminal": actual,
        "exit_first_step": exit_first_step,
    }


def adjacent_unordered_pairs(
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
) -> tuple[tuple[Coord, Coord], ...]:
    unordered = []
    for target in expected:
        for direction in c53.DIRECTIONS:
            neighbour = add(target, direction)
            if target < neighbour and neighbour in expected:
                if (
                    neighbour not in dependencies[target]
                    and target not in dependencies[neighbour]
                ):
                    unordered.append((target, neighbour))
    return tuple(sorted(unordered))


def dynamic_edge_signature_checks(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
):
    signature_failures = []
    deletion_failures = []
    alternate_after_deletion = []
    attempts = 0
    for target, parents in dependencies.items():
        premise = {
            neighbour: initial[neighbour]
            for direction in c53.DIRECTIONS
            if (neighbour := add(target, direction)) in initial
        }
        premise.update({
            parent: expected[parent]
            for parent in parents
        })
        signature = c53.local_signature(premise, target)
        wanted = frozenset((expected[target],))
        if FULL_RAW.get(signature) != wanted:
            signature_failures.append(
                (target, FULL_RAW.get(signature), wanted, parents)
            )
            continue
        for parent in parents:
            trial = dict(premise)
            del trial[parent]
            observed = FULL_RAW.get(c53.local_signature(trial, target))
            attempts += 1
            if observed is not None and expected[target] in observed:
                deletion_failures.append((target, parent, observed))
            elif observed is not None:
                alternate_after_deletion.append((target, parent, observed))
    return {
        "edges": sum(map(len, dependencies.values())),
        "attempts": attempts,
        "signature_failures": tuple(signature_failures),
        "deletion_failures": tuple(deletion_failures),
        "alternate_after_deletion": tuple(alternate_after_deletion),
    }


def causal_depths(
    dependencies: dict[Coord, frozenset[Coord]],
) -> dict[Coord, int]:
    depth: dict[Coord, int] = {}
    remaining = set(dependencies)
    while remaining:
        ready = {
            target
            for target in remaining
            if dependencies[target] <= depth.keys()
        }
        if not ready:
            raise RuntimeError(("causal-cycle", len(remaining)))
        for target in ready:
            depth[target] = 1 + max(
                (depth[parent] for parent in dependencies[target]),
                default=0,
            )
        remaining -= ready
    return depth


def causal_certificate(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    exits: dict[Coord, frozenset[str]],
):
    discovery = discover_causal_dependencies(
        initial, expected, exits, order="min"
    )
    if not discovery["ok"]:
        return {
            "ok": False,
            "discovery": discovery,
        }
    dependencies = discovery["dependencies"]
    minimum = causal_replay(
        initial, expected, exits, dependencies, order="min"
    )
    maximum = causal_replay(
        initial, expected, exits, dependencies, order="max"
    )
    unordered = adjacent_unordered_pairs(expected, dependencies)
    edge_checks = dynamic_edge_signature_checks(
        initial, expected, dependencies
    )
    ok = (
        minimum["ok"]
        and maximum["ok"]
        and not unordered
        and not edge_checks["signature_failures"]
        and not edge_checks["deletion_failures"]
    )
    return {
        "ok": ok,
        "discovery": discovery,
        "dependencies": dependencies,
        "minimum": minimum,
        "maximum": maximum,
        "unordered": unordered,
        "edge_checks": edge_checks,
    }


def oriented_face_geometries() -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
    fixed = {
        **completed_boundary(),
        **RAIL_EXTENSION,
        **PHYSICAL_ROOT_SIDECARS,
    }
    geometries = []
    for payload_y in range(-5, 7):
        for payload_z in range(-5, 7):
            payload_yz = (payload_y, payload_z)
            for delta_y, delta_z in (
                (1, 0), (-1, 0), (0, 1), (0, -1)
            ):
                guide_yz = (
                    payload_y + delta_y,
                    payload_z + delta_z,
                )
                payload = {
                    x: c141.transform_site(cell.site(x, payload_yz))
                    for x in range(6, 22)
                }
                guide = {
                    x: c141.transform_site(cell.site(x, guide_yz))
                    for x in range(6, 22)
                }
                if (
                    any(
                        payload[x] in fixed or guide[x] in fixed
                        for x in range(7, 22)
                    )
                    or guide[6] in fixed
                ):
                    continue
                payload_fixed_counts = tuple(
                    sum(
                        add(payload[x], direction) in fixed
                        for direction in c53.DIRECTIONS
                    )
                    for x in COPY_X
                )
                guide_fixed_counts = tuple(
                    sum(
                        add(guide[x], direction) in fixed
                        for direction in c53.DIRECTIONS
                    )
                    for x in COPY_X
                )
                if (
                    min(payload_fixed_counts) >= 1
                    and min(guide_fixed_counts) >= 1
                ):
                    geometries.append((payload_yz, guide_yz))
    return tuple(geometries)


def initial_role_pair_is_safe(
    payload_yz: tuple[int, int],
    guide_yz: tuple[int, int],
    guide_role: str,
    rear_role: str,
) -> bool:
    payload = c141.transform_site(cell.site(SEED_X, payload_yz))
    guide = c141.transform_site(cell.site(SEED_X, guide_yz))
    rear = c141.transform_site(cell.site(SEED_X - 1, guide_yz))
    boundary = completed_boundary()
    targets = (
        {
            add(site, direction)
            for site in (payload, guide, rear)
            for direction in c53.DIRECTIONS
            if add(site, direction) not in boundary
        }
        | set(b.BIND_IGNORED)
    )
    for row_role in ROW_ROLES:
        records = {
            **boundary,
            payload: row_role,
            guide: guide_role,
            rear: rear_role,
        }
        for target in targets:
            if target in records:
                continue
            observed = BASE_RAW.get(c53.local_signature(records, target))
            if observed != b.BIND_IGNORED.get(target):
                return False
    return True


def existing_role_face_census():
    geometries = oriented_face_geometries()
    survivors = []
    roles = tuple(sorted(cell.FULL_ROLES))
    tested_pairs = 0
    for payload_yz, guide_yz in geometries:
        geometry_survivors = []
        for guide_role in roles:
            for rear_role in roles:
                tested_pairs += 1
                if initial_role_pair_is_safe(
                    payload_yz,
                    guide_yz,
                    guide_role,
                    rear_role,
                ):
                    geometry_survivors.append((guide_role, rear_role))
        if geometry_survivors:
            survivors.append(
                (payload_yz, guide_yz, tuple(geometry_survivors))
            )
    return {
        "geometries": geometries,
        "role_pairs_per_geometry": len(roles) ** 2,
        "tested_pairs": tested_pairs,
        "survivors": tuple(survivors),
    }


def carrier_clean_role_census():
    """Test every existing onsite role as data on the current carrier face.

    Each role gets its own replacement carrier delta.  The candidate is
    merged with Cycle 166 alone, rather than with the 32-role Cycle-171
    table, so this is a genuine alphabet-replacement census and not duplicate
    semantics layered over the current row codebook.
    """

    global FULL_RAW
    original_full_raw = FULL_RAW
    clean = []
    failures = {}
    raw_conflicts = {}
    try:
        for role in sorted(cell.FULL_ROLES):
            try:
                table = canonical_sidecar_table((role,))
            except ValueError as error:
                failures[role] = ("canonical-conflict", error.args)
                continue
            raw = cell.merge_raw(*(
                cell.raw_orbit(local, output)
                for local, output in table.items()
            ))
            candidate_full_raw = cell.merge_raw(BASE_RAW, raw)
            conflicts = {
                local: values
                for local, values in candidate_full_raw.items()
                if len(values) != 1
            }
            if conflicts:
                raw_conflicts[role] = len(conflicts)
                failures[role] = ("base-conflict", len(conflicts))
                continue
            FULL_RAW = candidate_full_raw
            outcome = causal_certificate(
                source(role),
                outputs(role),
                IGNORED,
            )
            if outcome["ok"]:
                clean.append(role)
            elif not outcome["discovery"]["ok"]:
                failures[role] = (
                    "discovery",
                    outcome["discovery"]["error"],
                )
            else:
                replay = (
                    outcome["minimum"]
                    if not outcome["minimum"]["ok"]
                    else outcome["maximum"]
                )
                failures[role] = ("replay", replay["error"])
    finally:
        FULL_RAW = original_full_raw
    return {
        "tested": len(cell.FULL_ROLES),
        "clean": tuple(clean),
        "failures": failures,
        "raw_conflicts": raw_conflicts,
    }


def unary_row_aliases() -> dict[str, frozenset[str]]:
    return {
        role: values
        for role in ROW_ROLES
        if (
            values := BASE_RAW.get((((1, 0, 0), role),))
        ) is not None
    }


def rotate_records(records: dict[Coord, str], rotation, offset: Coord):
    return c53.transform_records(records, rotation, offset)


def rotate_values(values: dict[Coord, frozenset[str]], rotation, offset: Coord):
    return {
        add(c53.matvec(rotation, site), offset): output
        for site, output in values.items()
    }


def direct_payload_deletions() -> tuple[int, tuple]:
    attempts = 0
    failures = []
    fixed = {
        **completed_boundary(),
        **RAIL_EXTENSION,
        **PHYSICAL_ROOT_SIDECARS,
    }
    for row_role in ROW_ROLES:
        records = {
            **fixed,
            PAYLOAD_SITE[SEED_X]: row_role,
            GUIDE_SITE[SEED_X]: GUIDE_ROLE,
            GUIDE_SITE[SEED_X - 1]: REAR_STOP_ROLE,
        }
        for x in COPY_X:
            guide_local = c53.local_signature(records, GUIDE_SITE[x])
            assert FULL_RAW.get(guide_local) == frozenset((GUIDE_ROLE,))
            records[GUIDE_SITE[x]] = GUIDE_ROLE

            target = PAYLOAD_SITE[x]
            payload_local = c53.local_signature(records, target)
            assert FULL_RAW.get(payload_local) == frozenset((row_role,))
            parents = tuple(
                add(target, direction)
                for direction, _value in payload_local
            )
            for parent in parents:
                trial = dict(records)
                del trial[parent]
                attempts += 1
                observed = FULL_RAW.get(
                    c53.local_signature(trial, target),
                    frozenset(),
                )
                if row_role in observed:
                    failures.append((row_role, x, parent, observed))
            records[target] = row_role
    return attempts, tuple(failures)


def generation_ledger(
    dependencies: dict[Coord, frozenset[Coord]],
):
    depth = causal_depths(dependencies)

    ledger = []
    previous = GENERATION_X[0]
    for generation, x in enumerate(GENERATION_X):
        site = PAYLOAD_SITE[x]
        if generation == 0:
            ledger.append({
                "generation": 0,
                "x": x,
                "displacement": 0,
                "block_records": 0,
                "commit_depth": 0,
            })
            continue
        # Each translation-period block has 61 recurrent/socket records,
        # six physical root-sidecar records, and eight row/guide records.
        ledger.append({
            "generation": generation,
            "x": x,
            "displacement": sum(
                abs(a - b)
                for a, b in zip(PAYLOAD_SITE[previous], site)
            ),
            "block_records": 75,
            "commit_depth": depth[site],
        })
        previous = x
    return tuple(ledger), depth


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND SOURCE NORMALIZATION")
    check("Cycle-171 review note exists", NOTE.is_file())
    terminal = completed_boundary()
    check(
        "the completed Cycle-144 boundary has exactly two current-law fronts",
        stock_enabled(terminal) == b.BIND_IGNORED,
        stock_enabled(terminal),
    )
    occupied_legacy = {
        site: terminal.get(site)
        for site in INCOMPLETE_BOUNDARY_FRONTS
        if site in terminal
    }
    quiet_legacy = {
        site
        for site in INCOMPLETE_BOUNDARY_FRONTS
        if site not in terminal and site not in stock_enabled(terminal)
    }
    check(
        "all seven incomplete-boundary fronts are explicitly normalized",
        len(occupied_legacy) == 4
        and len(quiet_legacy) == 3
        and occupied_legacy == {
            (5, 4, 1): "R_A10",
            (3, 2, -2): "H0",
            (-1, 3, -2): "R_C01",
            (-4, 2, 0): "R_C41",
        },
        (occupied_legacy, quiet_legacy),
    )

    print("\nLAW AND GEOMETRY")
    check(
        "all 32 signed row roles are carried with no new onsite role",
        len(ROW_ROLES) == 32
        and {
            GUIDE_ROLE, REAR_STOP_ROLE, *ROW_ROLES
        } <= cell.FULL_ROLES,
    )
    check(
        "four guide plus 128 row locals compile to 3,168 raw rows",
        len(SIDECAR_TABLE) == 132
        and len(SIDECAR_RAW) == 3_168,
        (len(SIDECAR_TABLE), len(SIDECAR_RAW)),
    )
    check(
        "the Cycle-171 delta is disjoint from Cycle 166 and deterministic",
        set(SIDECAR_RAW).isdisjoint(BASE_RAW)
        and not RAW_CONFLICTS
        and len(BASE_RAW) == 100_652
        and len(FULL_RAW) == 103_820,
        (
            len(set(SIDECAR_RAW) & set(BASE_RAW)),
            len(RAW_CONFLICTS),
            len(BASE_RAW),
            len(FULL_RAW),
        ),
    )
    future_sites = tuple(PAYLOAD_SITE[x] for x in GENERATION_X[1:])
    supplied = {
        PAYLOAD_SITE[SEED_X],
        GUIDE_SITE[SEED_X],
        GUIDE_SITE[SEED_X - 1],
    }
    future_closed = {
        site
        for target in future_sites
        for site in (target, *(add(target, d) for d in c53.DIRECTIONS))
    }
    check(
        "no Cycle-171 supplied record lies in a future payload closed NN support",
        supplied.isdisjoint(future_closed),
        supplied & future_closed,
    )
    check(
        "the exact completed boundary is also absent from future payload supports",
        set(terminal).isdisjoint(future_closed),
        set(terminal) & future_closed,
    )

    print("\nREPRESENTATIVE CAUSAL CONFLUENCE CERTIFICATE")
    representative = ROW_ROLES[0]
    representative_source = source(representative)
    representative_outputs = outputs(representative)
    certificate = causal_certificate(
        representative_source,
        representative_outputs,
        IGNORED,
    )
    check(
        "the Cycle-166 union discovers one complete exact causal graph",
        certificate["discovery"]["ok"]
        and len(certificate["dependencies"]) == len(representative_outputs),
        certificate["discovery"].get("error"),
    )
    check(
        "lexicographic min and max equal the declared frontier at every write",
        certificate["minimum"]["ok"]
        and certificate["maximum"]["ok"],
        (
            certificate["minimum"],
            certificate["maximum"],
        ),
    )
    check(
        "zero adjacent unordered dynamic pairs certify all causal schedules",
        not certificate["unordered"],
        certificate["unordered"][:3],
    )
    check(
        "every dynamic edge has its exact signature and is load-bearing",
        not certificate["edge_checks"]["signature_failures"]
        and not certificate["edge_checks"]["deletion_failures"]
        and certificate["edge_checks"]["attempts"]
        == certificate["edge_checks"]["edges"],
        certificate["edge_checks"],
    )
    check(
        "the bounded terminal has exactly the two declared continuation exits",
        certificate["minimum"]["terminal"] == IGNORED
        and certificate["maximum"]["terminal"] == IGNORED,
        (
            certificate["minimum"]["terminal"],
            certificate["maximum"]["terminal"],
        ),
    )

    print("\nANCESTRY, DELETION, AND LEDGER")
    dependencies = certificate["dependencies"]
    direct_parents = {
        target: frozenset(
            set(parents)
            | {
                neighbour
                for direction in c53.DIRECTIONS
                if (
                    (neighbour := add(target, direction))
                    in representative_source
                )
            }
        )
        for target, parents in dependencies.items()
    }
    ancestry_failures = []
    for x in COPY_X:
        required = (
            PAYLOAD_SITE[x - 1],
            GUIDE_SITE[x],
            c141.transform_site(cell.site(x, cell.LOWER_YZ)),
        )
        for parent in required:
            if parent not in direct_parents[PAYLOAD_SITE[x]]:
                ancestry_failures.append((x, parent))
    check(
        "every payload copy has exact prior-row, guide, and phase ancestry",
        not ancestry_failures,
        ancestry_failures,
    )
    ancestor_cache: dict[Coord, frozenset[Coord]] = {}

    def ancestors(target: Coord) -> frozenset[Coord]:
        if target not in ancestor_cache:
            inherited = set(direct_parents[target])
            for parent in dependencies[target]:
                inherited.update(ancestors(parent))
            ancestor_cache[target] = frozenset(inherited)
        return ancestor_cache[target]

    seed_ancestry_failures = tuple(
        x
        for x in GENERATION_X[1:]
        if PAYLOAD_SITE[SEED_X] not in ancestors(PAYLOAD_SITE[x])
    )
    check(
        "G1 through G3 have an unbroken exact ancestry chain to the finite G0 seed",
        not seed_ancestry_failures,
        seed_ancestry_failures,
    )
    deletion_attempts, deletion_failures = direct_payload_deletions()
    check(
        "all direct payload-parent deletions suppress the intended row",
        deletion_attempts == 32 * len(COPY_X) * 3
        and not deletion_failures,
        (deletion_attempts, deletion_failures[:2]),
    )
    ledger, depth = generation_ledger(dependencies)
    check(
        "the three payload generations have period-four displacement and linear cost",
        tuple(item["displacement"] for item in ledger[1:]) == (4, 4, 4)
        and tuple(item["block_records"] for item in ledger[1:]) == (75, 75, 75)
        and all(
            ledger[index_]["commit_depth"]
            < ledger[index_ + 1]["commit_depth"]
            for index_ in range(len(ledger) - 1)
        ),
        ledger,
    )

    print("\nALL VALUES AND COVARIANCE")
    identity_shapes = []
    value_failures = []
    value_failure_details = {}
    for row_role in ROW_ROLES:
        outcome = causal_certificate(
            source(row_role),
            outputs(row_role),
            IGNORED,
        )
        if outcome["ok"]:
            shape = (
                outcome["minimum"]["states"],
                outcome["minimum"]["edge_visits"],
                outcome["minimum"]["max_frontier"],
                outcome["maximum"]["edge_visits"],
                outcome["maximum"]["max_frontier"],
                outcome["edge_checks"]["edges"],
                len(outcome["edge_checks"]["alternate_after_deletion"]),
            )
            identity_shapes.append(shape)
        else:
            value_failures.append(row_role)
            if not outcome["discovery"]["ok"]:
                value_failure_details[row_role] = {
                    "stage": "discovery",
                    "error": outcome["discovery"]["error"],
                    "signatures":
                    outcome["discovery"].get("error_signatures", {}),
                }
            else:
                failed_replay = (
                    outcome["minimum"]
                    if not outcome["minimum"]["ok"]
                    else outcome["maximum"]
                )
                value_failure_details[row_role] = {
                    "stage": "replay",
                    "error": failed_replay["error"],
                    "signatures":
                    failed_replay.get("error_signatures", {}),
                }
    expected_value_failures = {
        "A_0_1",
        "A_0_2",
        "BTG",
        "BTQ",
        "B_0_2",
        "COMP6",
        "DONE",
    }
    check(
        "the common law carries exactly 25 rows and exposes seven type aliases",
        set(value_failures) == expected_value_failures
        and len(identity_shapes) == 25
        and len(set(identity_shapes)) == 1,
        (
            Counter(identity_shapes),
            value_failures,
            value_failure_details,
        ),
    )
    unary_aliases = unary_row_aliases()
    check(
        "three failing row roles are unary instructions in the inherited namespace",
        unary_aliases == {
            "BTQ": frozenset(("TJ",)),
            "COMP6": frozenset(("S7",)),
            "DONE": frozenset(("L1",)),
        },
        unary_aliases,
    )
    face_census = existing_role_face_census()
    check(
        "all 16 oriented faces and 374,544 existing guide/rear pairs are exhausted",
        len(face_census["geometries"]) == 16
        and face_census["role_pairs_per_geometry"] == 23_409
        and face_census["tested_pairs"] == 374_544
        and not face_census["survivors"],
        face_census,
    )
    clean_census = carrier_clean_role_census()
    expected_nonclean_roles = {
        "ALL",
        "A_0_1",
        "A_0_2",
        "BTG",
        "BTQ",
        "B_0_2",
        "COMP6",
        "DONE",
        "GU",
        "J6",
        "L10",
        "L11",
        "L5",
        "L8",
        "L9",
        "LAUNCH_A",
        "M",
        "R_A21",
        "R_A41",
        "R_B01",
        "R_B12",
        "R_B21",
        "R_B31",
        "R_B32",
        "R_B40",
        "R_C12",
        "R_C13",
        "R_C22",
        "R_C41",
        "R_LA",
        "R_LB",
        "R_LC",
        "START",
        "T_H2",
        "W3",
        "W5",
    }
    clean_roles = set(clean_census["clean"])
    check(
        "117 existing roles are carrier-clean, enough for an injective 32-value remap",
        clean_census["tested"] == 153
        and len(clean_roles) == 117
        and set(cell.FULL_ROLES) - clean_roles == expected_nonclean_roles
        and len(clean_roles) >= len(ROW_ROLES),
        (
            len(clean_roles),
            tuple(sorted(set(cell.FULL_ROLES) - clean_roles)),
            clean_census["raw_conflicts"],
        ),
    )

    hard_value = "COMPLETE"
    rotation_shapes = []
    rotation_failures = []
    offset = (401, -409, 419)
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        rotated_source = rotate_records(source(hard_value), rotation, offset)
        rotated_outputs = rotate_records(outputs(hard_value), rotation, offset)
        rotated_ignored = rotate_values(IGNORED, rotation, offset)
        outcome = causal_certificate(
            rotated_source,
            rotated_outputs,
            rotated_ignored,
        )
        if not outcome["ok"]:
            rotation_failures.append((rotation_index, outcome))
            continue
        shape = (
            outcome["minimum"]["states"],
            outcome["minimum"]["edge_visits"],
            outcome["minimum"]["max_frontier"],
            outcome["maximum"]["edge_visits"],
            outcome["maximum"]["max_frontier"],
            outcome["edge_checks"]["edges"],
            len(outcome["edge_checks"]["alternate_after_deletion"]),
        )
        rotation_shapes.append(shape)
    check(
        "one non-aliasing hard row closes in all 24 proper-cubic orientations",
        not rotation_failures
        and len(rotation_shapes) == 24
        and all(shape[0] == 230 and shape[5] == 515 for shape in rotation_shapes),
        (Counter(rotation_shapes), rotation_failures[:1]),
    )
    covariance_failures = []
    covariance_checks = 0
    for local, values in SIDECAR_RAW.items():
        for rotation in c53.ROTATIONS:
            covariance_checks += 1
            if (
                FULL_RAW.get(c53.rotate_signature(local, rotation))
                != values
            ):
                covariance_failures.append((local, rotation))
                break
    check(
        "all 76,032 new raw-row rotations preserve output",
        covariance_checks == 3_168 * 24
        and not covariance_failures,
        covariance_failures[:1],
    )

    print("\nSCOPE")
    note = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    check(
        "review note carries N1-N8 and bounded-carrier scope",
        all(f"### N{index_}" in note for index_ in range(1, 9))
        and "stable record-native information carrier" in note
        and "not an unbounded recurrence theorem" in note
        and "No axiom addition follows" in note,
    )

    print("\nACCOUNTING")
    print("SOURCE_RECORDS", len(representative_source))
    print("VARIABLE_RECORDS", len(representative_outputs))
    print("CANONICAL_ADDITIONS", len(SIDECAR_TABLE))
    print("RAW_ADDITIONS", len(SIDECAR_RAW))
    print("FULL_RAW", len(FULL_RAW))
    print("CARRIER_CLEAN_EXISTING_ROLES", len(clean_roles))
    print(
        "CAUSAL_CERTIFICATE",
        certificate["minimum"]["states"],
        certificate["minimum"]["edge_visits"],
        certificate["minimum"]["max_frontier"],
        certificate["maximum"]["edge_visits"],
        certificate["maximum"]["max_frontier"],
        certificate["edge_checks"]["edges"],
    )
    print("LEDGER", ledger)
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "BOUNDED_CARRIER_TYPE_ALIAS_STOP"
        if FAIL == 0 else "CYCLE171_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
