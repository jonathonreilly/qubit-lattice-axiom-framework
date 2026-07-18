#!/usr/bin/env python3
"""Independent recurrence, confluence, and compact-law checks for the notched cell.

This runner deliberately treats the all-subsets compiler as a conservative
screen rather than silently equating every local subset with a lawful history.
Every wrong-valued static fingerprint must receive a causal impossibility
certificate, and every reachable asynchronous history is still enumerated.

The file is campaign-local.  It selects no law and edits no foundation,
registry, policy, audit, or git state.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from functools import reduce
from itertools import combinations

import relational_notched_rail_socket_prototype_2026_07_15 as cell


Coord = tuple[int, int, int]
ValueSet = frozenset[str]


@dataclass(frozen=True, order=True)
class Condition:
    target: Coord
    present: tuple[Coord, ...]
    neighbourhood: tuple[Coord, ...]
    values: tuple[str, ...]


def shift(position: Coord, delta: Coord) -> Coord:
    return tuple(a + b for a, b in zip(position, delta))  # type: ignore[return-value]


def translated(records: dict[Coord, str], dx: int) -> dict[Coord, str]:
    return {shift(site, (dx, 0, 0)): value for site, value in records.items()}


def independent_enabled(
    records: dict[Coord, str],
    raw: dict[cell.Signature, ValueSet] = cell.RAW,
) -> dict[Coord, ValueSet]:
    candidates = {
        shift(parent, direction)
        for parent in records
        for direction in cell.c52.DIRECTIONS
        if shift(parent, direction) not in records
    }
    answer = {}
    for target in candidates:
        local = tuple(sorted(
            (direction, records[shift(target, direction)])
            for direction in cell.c52.DIRECTIONS
            if shift(target, direction) in records
        ))
        if local in raw:
            answer[target] = raw[local]
    return answer


def static_screen(periods: int) -> tuple[
    dict[Coord, str],
    tuple[Condition, ...],
    tuple[Condition, ...],
    tuple[Coord, ...],
]:
    """Enumerate every local subset, without assuming global reachability."""

    last_x = 4 * periods - 1
    outputs, _sockets, ignored0 = cell.expected_outputs(last_x=last_x)
    source = cell.seed_records()
    complete = {**source, **outputs}
    candidates = set(outputs) | set(ignored0)
    for parent in complete:
        for direction in cell.c52.DIRECTIONS:
            target = shift(parent, direction)
            if target not in source:
                candidates.add(target)

    conditions = []
    wrong = []
    unexpected = set()
    for target in sorted(candidates):
        fixed = {
            shift(target, direction): source[shift(target, direction)]
            for direction in cell.c52.DIRECTIONS
            if shift(target, direction) in source
        }
        variable = tuple(sorted(
            shift(target, direction)
            for direction in cell.c52.DIRECTIONS
            if shift(target, direction) in outputs
        ))
        for mask in range(1 << len(variable)):
            present = tuple(
                site for index, site in enumerate(variable) if mask >> index & 1
            )
            records = dict(fixed)
            records.update({site: outputs[site] for site in present})
            local = tuple(sorted(
                (direction, records[shift(target, direction)])
                for direction in cell.c52.DIRECTIONS
                if shift(target, direction) in records
            ))
            if local not in cell.RAW:
                continue
            condition = Condition(
                target,
                present,
                variable,
                tuple(sorted(cell.RAW[local])),
            )
            conditions.append(condition)
            if target not in outputs and target not in ignored0:
                unexpected.add(target)
            elif (
                target in outputs
                and cell.RAW[local] != frozenset((outputs[target],))
            ):
                wrong.append(condition)
    return (
        outputs,
        tuple(sorted(conditions)),
        tuple(sorted(wrong)),
        tuple(sorted(unexpected)),
    )


def period_blocks(periods: int) -> tuple[dict[Coord, str], ...]:
    first, _sockets, _ignored = cell.expected_outputs(last_x=3)
    return tuple(translated(first, cell.PERIOD * index) for index in range(periods))


def period_index(blocks: tuple[dict[Coord, str], ...]) -> dict[Coord, int]:
    answer = {}
    for index, block in enumerate(blocks):
        for site in block:
            if site in answer:
                raise RuntimeError(("period-overlap", site, answer[site], index))
            answer[site] = index
    return answer


def graph(periods: int, *, diamonds: bool = False):
    """Enumerate reachable states without calling the prototype graph routine."""

    last_x = 4 * periods - 1
    outputs, _sockets, ignored0 = cell.expected_outputs(last_x=last_x)
    ignored = {site: frozenset((value,)) for site, value in ignored0.items()}
    source = cell.seed_records()
    sites = tuple(sorted(outputs))
    index = {site: bit for bit, site in enumerate(sites)}
    all_mask = (1 << len(sites)) - 1
    blocks = period_blocks(periods)
    owner = period_index(blocks)
    block_masks = tuple(sum(1 << index[site] for site in block) for block in blocks)

    queue = deque((0,))
    seen = {0}
    edges = 0
    terminals = 0
    bad = []
    max_frontier = 0
    mandatory_before = {site: all_mask for site in sites}
    append_seen = Counter()
    mixed_states = 0
    mixed_frontiers = 0
    cross_period_diamonds = 0
    diamond_pairs = 0
    diamond_failures = []

    while queue:
        mask = queue.popleft()
        records = dict(source)
        records.update({
            site: outputs[site]
            for site, bit in index.items()
            if mask >> bit & 1
        })
        actual = independent_enabled(records)
        wrong = {
            target: values
            for target, values in actual.items()
            if (
                target in outputs
                and values != frozenset((outputs[target],))
            ) or (
                target not in outputs
                and ignored.get(target) != values
            )
        }
        if wrong:
            bad.append((mask.bit_count(), tuple(sorted(wrong.items()))))
            continue

        if any(
            mask & block_masks[n]
            and mask & block_masks[n - 1] != block_masks[n - 1]
            for n in range(1, periods)
        ):
            mixed_states += 1

        if mask == all_mask:
            if actual == ignored:
                terminals += 1
            else:
                bad.append((mask.bit_count(), "terminal-front", actual))
            continue

        futures = tuple(sorted(
            target
            for target, values in actual.items()
            if target in index
            and not (mask >> index[target] & 1)
            and values == frozenset((outputs[target],))
        ))
        max_frontier = max(max_frontier, len(futures))
        if not futures:
            bad.append((mask.bit_count(), "dead", actual))
            continue
        if len({owner[target] for target in futures}) > 1:
            mixed_frontiers += 1

        if diamonds:
            for left, right in combinations(futures, 2):
                diamond_pairs += 1
                if owner[left] != owner[right]:
                    cross_period_diamonds += 1
                after_left = independent_enabled({**records, left: outputs[left]})
                after_right = independent_enabled({**records, right: outputs[right]})
                if (
                    after_left.get(right) != frozenset((outputs[right],))
                    or after_right.get(left) != frozenset((outputs[left],))
                ):
                    diamond_failures.append((mask.bit_count(), left, right))

        for target in futures:
            mandatory_before[target] &= mask
            append_seen[target] += 1
            future = mask | (1 << index[target])
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)

    return {
        "periods": periods,
        "outputs": outputs,
        "sites": sites,
        "index": index,
        "states": len(seen),
        "edges": edges,
        "terminals": terminals,
        "bad": tuple(bad),
        "max_frontier": max_frontier,
        "mandatory_before": mandatory_before,
        "append_seen": append_seen,
        "mixed_states": mixed_states,
        "mixed_frontiers": mixed_frontiers,
        "diamond_pairs": diamond_pairs,
        "cross_period_diamonds": cross_period_diamonds,
        "diamond_failures": tuple(diamond_failures),
    }


def causal_certificates(result, wrong: tuple[Condition, ...]):
    index = result["index"]
    mandatory = result["mandatory_before"]
    certificates = []
    unresolved = []
    for condition in wrong:
        absent = set(condition.neighbourhood) - set(condition.present)
        reasons = []
        for present in condition.present:
            if present not in index:
                continue
            must = mandatory[present]
            if (
                condition.target in index
                and must >> index[condition.target] & 1
            ):
                reasons.append(("target-before-present", condition.target, present))
            for missing in absent:
                if missing in index and must >> index[missing] & 1:
                    reasons.append(("absent-before-present", missing, present))
        if reasons:
            certificates.append((condition, tuple(sorted(set(reasons)))))
        else:
            unresolved.append(condition)
    return tuple(certificates), tuple(unresolved)


def normalize_condition(condition: Condition, period: int) -> Condition:
    delta = (-cell.PERIOD * period, 0, 0)
    return Condition(
        shift(condition.target, delta),
        tuple(shift(site, delta) for site in condition.present),
        tuple(shift(site, delta) for site in condition.neighbourhood),
        condition.values,
    )


def corruption_controls() -> tuple[int, tuple[object, ...], int, tuple[object, ...]]:
    outputs, sockets, _ignored = cell.expected_outputs()
    complete = cell.seed_records()
    complete.update(outputs)
    for socket in sockets:
        for target in socket[5:]:
            complete.pop(target)

    direct_attempts = 0
    false_positive = []
    for socket_index, socket in enumerate(sockets):
        q, blocker, a_guard, root, b_guard, helper, h1, launch = socket
        stages = (
            ("helper", dict(complete), helper, cell.HELPER_CONTENT,
             (("root", root), ("b_guard", b_guard))),
            ("h1", {**complete, helper: cell.HELPER_CONTENT}, h1, cell.H1,
             (("blocker", blocker), ("a_guard", a_guard), ("helper", helper))),
            ("oz", {**complete, helper: cell.HELPER_CONTENT, h1: cell.H1},
             launch, cell.OZ, (("q", q), ("h1", h1))),
        )
        for stage, context, target, expected, parents in stages:
            for label, parent in parents:
                alternatives = (None, *sorted(cell.FULL_ROLES - {context[parent]}))
                for alternate in alternatives:
                    trial = dict(context)
                    if alternate is None:
                        del trial[parent]
                    else:
                        trial[parent] = alternate
                    direct_attempts += 1
                    if expected in independent_enabled(trial).get(target, frozenset()):
                        false_positive.append((
                            socket_index, stage, label, alternate, target
                        ))

    identity = next(
        rotation
        for rotation in cell.c52.ROTATIONS
        if cell.c52.matvec(rotation, (2, 3, 5)) == (2, 3, 5)
    )
    initial_q = cell.site(-1, cell.ROOT_YZ)
    next_q = cell.site(3, cell.ROOT_YZ)
    seed = cell.seed_records()
    recurrence_attempts = 0
    recurrence_failures = []
    for alternate in (None, *sorted(cell.FULL_ROLES - {seed[initial_q]})):
        trial = dict(seed)
        if alternate is None:
            del trial[initial_q]
        else:
            trial[initial_q] = alternate
        outcome = cell.graph(
            identity,
            last_x=3,
            base_records=trial,
            include_reached=True,
        )
        recurrence_attempts += 1
        if next_q in outcome["reached"]:
            recurrence_failures.append((alternate, outcome["states"]))
    return (
        direct_attempts,
        tuple(false_positive),
        recurrence_attempts,
        tuple(recurrence_failures),
    )


def main() -> int:
    checks = []

    def check(label: str, condition: bool, detail: object = "") -> None:
        checks.append((label, bool(condition), detail))
        print(("PASS" if condition else "FAIL"), label, "::", detail)

    print("GRAMMAR")
    output_roles = frozenset(cell.ROWS.values())
    input_roles = frozenset(value for signature in cell.ROWS for _d, value in signature)
    check("58 fixed canonical rows", len(cell.ROWS) == 58, len(cell.ROWS))
    check("1320 proper-cubic raw rows", len(cell.RAW) == 1320, len(cell.RAW))
    check("raw table is single-valued", all(len(v) == 1 for v in cell.RAW.values()))
    check("one canonical output role per row", len(output_roles) == 58, len(output_roles))
    check("closed 153-role alphabet", input_roles | output_roles <= cell.FULL_ROLES)
    check(
        "strict nearest-neighbour signatures",
        all(direction in cell.c52.DIRECTIONS for signature in cell.ROWS for direction, _v in signature),
    )

    print("\nRECURRENCE")
    blocks = period_blocks(5)
    expected5, sockets5, _ignored5 = cell.expected_outputs(last_x=19)
    union = {}
    for block in blocks:
        overlap = set(union) & set(block)
        check("period block has no output overlap", not overlap, tuple(sorted(overlap))[:2])
        union.update(block)
    check("five periods are exact translations", union == expected5, (len(union), len(expected5)))
    check("58 records per period", all(len(block) == 58 for block in blocks))
    check("one socket per period", len(sockets5) == 5, len(sockets5))
    check(
        "socket coordinates recur by period translation",
        all(
            tuple(shift(site, (4 * n, 0, 0)) for site in sockets5[0]) == sockets5[n]
            for n in range(5)
        ),
    )

    rail_only = cell.seed_records()
    rail_only.update({
        site: value
        for site, value in expected5.items()
        if value not in {cell.HELPER_CONTENT, cell.H1, cell.OZ}
        or site not in {item for socket in sockets5 for item in socket[5:]}
    })
    signatures = []
    for socket in sockets5:
        helper, h1, launch = socket[5:]
        staged = dict(rail_only)
        local_helper = cell.local_signature(staged, helper)
        staged[helper] = cell.HELPER_CONTENT
        local_h1 = cell.local_signature(staged, h1)
        staged[h1] = cell.H1
        local_oz = cell.local_signature(staged, launch)
        signatures.append((local_helper, local_h1, local_oz))
    check("all five sockets have identical oriented signatures", len(set(signatures)) == 1)
    c129_launch = (((0, 0, 1), cell.H1), ((0, 1, 0), "R_B01"))
    check(
        "OZ socket exactly matches Cycle-129 canonical launch",
        cell.canonical(signatures[0][2]) == cell.canonical(c129_launch),
        cell.canonical(signatures[0][2]),
    )

    print("\nSTATIC SCREEN AND CAUSAL FIREWALL")
    screen_counts = []
    screens = {}
    for periods in range(1, 6):
        outputs, conditions, wrong, unexpected = static_screen(periods)
        screens[periods] = (outputs, conditions, wrong, unexpected)
        screen_counts.append((periods, len(outputs), len(conditions), len(wrong), len(unexpected)))
    check(
        "static screen has no unexpected target through five periods",
        all(not item[3] for item in screens.values()),
        screen_counts,
    )
    check(
        "static condition accounting is affine",
        all(len(screens[n][1]) == 114 * n - 23 for n in range(1, 6)),
        tuple((n, len(screens[n][1])) for n in range(1, 6)),
    )
    check(
        "wrong-valued warning accounting is affine",
        all(len(screens[n][2]) == 56 * n - 24 for n in range(1, 6)),
        tuple((n, len(screens[n][2])) for n in range(1, 6)),
    )
    wrong4 = screens[4][2]
    by_period = tuple(sum(4 * n <= item.target[0] <= 4 * n + 3 for item in wrong4) for n in range(4))
    check("wrong-warning boundary/interior split", by_period == (41, 56, 56, 47), by_period)
    interior1 = {
        normalize_condition(item, 1) for item in wrong4 if 4 <= item.target[0] <= 7
    }
    interior2 = {
        normalize_condition(item, 2) for item in wrong4 if 8 <= item.target[0] <= 11
    }
    check("interior warning corpus is translation invariant", interior1 == interior2, len(interior1))

    print("\nASYNCHRONOUS HISTORY AND CONFLUENCE")
    graph4 = graph(4)
    check("four-period exhaustive graph is clean", not graph4["bad"], graph4["bad"][:2])
    check(
        "four-period exhaustive census",
        (graph4["states"], graph4["edges"], graph4["terminals"])
        == (18_856, 73_037, 1),
        (graph4["states"], graph4["edges"], graph4["terminals"]),
    )
    check("successive cells genuinely interleave", graph4["mixed_states"] > 0, graph4["mixed_states"])
    check("mixed-cell frontiers occur", graph4["mixed_frontiers"] > 0, graph4["mixed_frontiers"])
    certificates, unresolved = causal_certificates(graph4, wrong4)
    check(
        "every static wrong warning has a causal contradiction",
        len(certificates) == len(wrong4) and not unresolved,
        (len(certificates), len(unresolved)),
    )

    graph3 = graph(3, diamonds=True)
    check("three-period independent graph is clean", not graph3["bad"])
    check(
        "every co-enabled action pair commutes",
        graph3["diamond_pairs"] > 0 and not graph3["diamond_failures"],
        (graph3["diamond_pairs"], len(graph3["diamond_failures"])),
    )
    check(
        "cross-period action pairs commute",
        graph3["cross_period_diamonds"] > 0 and not graph3["diamond_failures"],
        graph3["cross_period_diamonds"],
    )

    print("\nCOVARIANCE AND CORRUPTION")
    rotated = []
    for rotation in cell.c52.ROTATIONS:
        outcome = cell.graph(rotation, (13, -17, 19))
        rotated.append((
            outcome["states"], outcome["edges"], outcome["bad_count"],
            len(outcome["terminals"]),
        ))
    check(
        "all 24 proper-cubic coimages have the same exact graph",
        len(rotated) == 24 and set(rotated) == {(1096, 2701, 0, 1)},
        Counter(rotated),
    )
    direct_attempts, false_positive, recurrence_attempts, recurrence_failures = corruption_controls()
    check(
        "all direct parent perturbations suppress the intended value",
        direct_attempts == 2142 and not false_positive,
        (direct_attempts, false_positive[:2]),
    )
    check(
        "all seed-q perturbations suppress the descendant q",
        recurrence_attempts == 153 and not recurrence_failures,
        (recurrence_attempts, recurrence_failures[:2]),
    )

    failed = tuple(label for label, passed, _detail in checks if not passed)
    print("\nACCOUNTING")
    print("CANONICAL_ROWS", len(cell.ROWS))
    print("RAW_ROWS", len(cell.RAW))
    print("ROLE_ALPHABET_USED", len(input_roles | output_roles), "OF", len(cell.FULL_ROLES))
    print("PERIOD_RECORDS", 58, "FORMULA", "58*N")
    print("STATIC_CONDITIONS", "114*N-23")
    print("STATIC_WRONG_WARNINGS", "56*N-24", "ALL_CAUSALLY_DISCHARGED_AT_N=4")
    print("PASS", len(checks) - len(failed), "FAIL", len(failed))
    print("FAILED", failed)
    print(
        "RESULT",
        "RELATIONAL_TWO_CELL_RECURRENCE_AND_COMPACT_LAW_GATE_PASS"
        if not failed
        else "FAIL",
    )
    return int(bool(failed))


if __name__ == "__main__":
    raise SystemExit(main())
