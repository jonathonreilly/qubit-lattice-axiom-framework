#!/usr/bin/env python3
"""Route the four tableau pivot cases with physical selector records."""

from __future__ import annotations

from collections import deque
from itertools import product

import physical_commuting_row_multiplication_probe_2026_07_15 as mult


algebra = mult.algebra
five = mult.five
d = mult.d
c53 = mult.c53
cell = mult.cell
Coord = tuple[int, int, int]
Signature = c53.Signature
FRAME = d.CAGE_ROLE

CASE_SITE = (0, 0, 0)
LANE1 = (0, 0, -1)
LANE2 = (0, -1, 0)
CASE_INPUTS = {"c1": (0, 0, 1), "c2": (-1, 0, 0), "mark": (1, 0, 0), "start": (0, 1, 0)}
LANE_MARKERS = {LANE1: (0, 1, -1), LANE2: (0, -1, 1)}

BRANCHES = {
    "l1_g1": (1, 0, -1),
    "l1_p": (-1, 0, -1),
    "l2_g2": (1, -1, 0),
    "l2_p": (-1, -1, 0),
    "l2_product": (0, -2, 0),
}
BUSES = {
    "l1_g1": (2, 0, -1),
    "l1_p": (-2, 0, -1),
    "l2_g2": (2, -1, 0),
    "l2_p": (-2, -1, 0),
    "l2_product": (0, -3, 0),
}
PORTS = {
    "l1_g1": (1, 1, -1),
    "l1_p": (-1, 1, -1),
    "l2_g2": (1, -1, 1),
    "l2_p": (-1, -1, 1),
    "l2_product": (0, -2, 1),
}
PORT_FRAMES = {
    "l1_g1": (1, 2, -1),
    "l1_p": (-1, 2, -1),
    "l2_g2": (1, -1, 2),
    "l2_p": (-1, -1, 2),
    "l2_product": (0, -2, 2),
}

CASE_ROLES = tuple(d.PREFIX_ROLES[32:36])
CASE_ROLE = {(c1, c2): role for (c1, c2), role in zip(product((0, 1), repeat=2), CASE_ROLES)}
LANE_ROLES = tuple(d.PREFIX_ROLES[41:43])
SELECTOR_ROLES = tuple(d.PREFIX_ROLES[36:41])
SEL_L1_G1, SEL_L1_P, SEL_L2_G2, SEL_L2_P, SEL_L2_PRODUCT = SELECTOR_ROLES
ROUTER_MARKER = d.PREFIX_ROLES[43]

LANE_OUTPUT = {
    (0, 0): (SEL_L1_G1, SEL_L2_G2),
    (0, 1): (SEL_L1_G1, SEL_L2_P),
    (1, 0): (SEL_L1_P, SEL_L2_G2),
    (1, 1): (SEL_L1_P, SEL_L2_PRODUCT),
}
SELECTOR_BRANCH = {
    SEL_L1_G1: "l1_g1",
    SEL_L1_P: "l1_p",
    SEL_L2_G2: "l2_g2",
    SEL_L2_P: "l2_p",
    SEL_L2_PRODUCT: "l2_product",
}
BRANCH_MARK_POS = {
    "l1_g1": (1, -1, -1),
    "l1_p": (-1, -1, -1),
    "l2_g2": (1, -2, 0),
    "l2_p": (-1, -2, 0),
    "l2_product": (-1, -2, 0),
}


def case_local(c1: int, c2: int):
    records = {
        CASE_INPUTS["c1"]: d.H1 if c1 else d.H0,
        CASE_INPUTS["c2"]: d.H1 if c2 else d.H0,
        CASE_INPUTS["mark"]: FRAME,
        CASE_INPUTS["start"]: d.START_ROLE,
    }
    return c53.canonical_signature(c53.local_signature(records, CASE_SITE))


CASE_TABLE = {case_local(c1, c2): CASE_ROLE[(c1, c2)] for c1, c2 in product((0, 1), repeat=2)}


def lane_local(case_role: str, lane: int):
    if lane == 1:
        records = {
            (0, 0, 1): case_role,
            (0, 1, 0): LANE_ROLES[0],
            (0, -1, 0): FRAME,
            (0, 0, -1): FRAME,
        }
    else:
        records = {
            (0, 1, 0): case_role,
            (0, 0, 1): LANE_ROLES[1],
            (0, 0, -1): FRAME,
        }
    return c53.canonical_signature(c53.local_signature(records, (0, 0, 0)))


LANE_TABLE: dict[Signature, str] = {}
for case, case_role in CASE_ROLE.items():
    first, second = LANE_OUTPUT[case]
    for local, output in ((lane_local(case_role, 1), first), (lane_local(case_role, 2), second)):
        prior = LANE_TABLE.get(local)
        if prior is not None and prior != output:
            raise ValueError((case, local, prior, output))
        LANE_TABLE[local] = output


def copy_local(branch: str, selector: str, row_role: str, case: tuple[int, int]):
    target = BRANCHES[branch]
    lane = LANE1 if branch.startswith("l1_") else LANE2
    records = {
        lane: selector,
        BUSES[branch]: row_role,
    }
    for direction in c53.DIRECTIONS:
        site = c53.add(target, direction)
        if site not in {lane, BUSES[branch], PORTS[branch]}:
            if site in BRANCH_MARK_POS.values():
                records[site] = ROUTER_MARKER
            elif site == CASE_INPUTS["c1"]:
                records[site] = d.H1 if case[0] else d.H0
            elif site == CASE_INPUTS["c2"]:
                records[site] = d.H1 if case[1] else d.H0
            elif site == CASE_INPUTS["start"]:
                records[site] = d.START_ROLE
            else:
                records[site] = FRAME
    return c53.canonical_signature(c53.local_signature(records, target))


COPY_TABLE: dict[Signature, str] = {}
for case, selectors in LANE_OUTPUT.items():
    for selector in selectors:
        branch = SELECTOR_BRANCH[selector]
        for row_role in five.ROLE_ROW:
            local = copy_local(branch, selector, row_role, case)
            prior = COPY_TABLE.get(local)
            if prior is not None and prior != row_role:
                raise ValueError((selector, row_role, prior, local))
            COPY_TABLE[local] = row_role


CANONICAL_TABLE = {**CASE_TABLE, **LANE_TABLE, **COPY_TABLE}
ROUTER_RAW = cell.merge_raw(*(
    cell.raw_orbit(local, output)
    for local, output in CANONICAL_TABLE.items()
))
MERGED_RAW = cell.merge_raw(mult.MERGED_RAW, ROUTER_RAW)
RAW_CONFLICTS = {local: values for local, values in MERGED_RAW.items() if len(values) != 1}


TARGETS = {CASE_SITE, LANE1, LANE2, *BRANCHES.values()}


def pivot_rows(g1, g2, measured):
    c1 = algebra.symplectic(g1, measured)
    c2 = algebra.symplectic(g2, measured)
    if not c1 and not c2:
        return (c1, c2), (g1, g2)
    if c1 and c2:
        return (c1, c2), (measured, algebra.multiply_commuting(g2, g1))
    if c1:
        return (c1, c2), (measured, g2)
    return (c1, c2), (g1, measured)


def source(g1, g2, measured):
    case, updated = pivot_rows(g1, g2, measured)
    product_row = algebra.multiply_commuting(g2, g1)
    records: dict[Coord, str] = {
        CASE_INPUTS["c1"]: d.H1 if case[0] else d.H0,
        CASE_INPUTS["c2"]: d.H1 if case[1] else d.H0,
        CASE_INPUTS["mark"]: FRAME,
        CASE_INPUTS["start"]: d.START_ROLE,
        LANE_MARKERS[LANE1]: LANE_ROLES[0],
        LANE_MARKERS[LANE2]: LANE_ROLES[1],
        BUSES["l1_g1"]: five.ROW_ROLE[g1],
        BUSES["l1_p"]: five.ROW_ROLE[measured],
        BUSES["l2_g2"]: five.ROW_ROLE[g2],
        BUSES["l2_p"]: five.ROW_ROLE[measured],
        BUSES["l2_product"]: five.ROW_ROLE[product_row],
        **{site: FRAME for site in PORT_FRAMES.values()},
        **{site: ROUTER_MARKER for site in BRANCH_MARK_POS.values()},
    }
    core = set(records) | TARGETS | set(PORTS.values())
    cage = {
        c53.add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in core
    }
    records.update({site: FRAME for site in cage})
    for target in (*TARGETS, *PORTS.values()):
        records.pop(target, None)
    return records, case, updated


def expected(g1, g2, measured):
    _records, case, updated = source(g1, g2, measured)
    first_selector, second_selector = LANE_OUTPUT[case]
    first_branch = SELECTOR_BRANCH[first_selector]
    second_branch = SELECTOR_BRANCH[second_selector]
    return {
        CASE_SITE: CASE_ROLE[case],
        LANE1: first_selector,
        LANE2: second_selector,
        BRANCHES[first_branch]: five.ROW_ROLE[updated[0]],
        BRANCHES[second_branch]: five.ROW_ROLE[updated[1]],
    }


def enabled(records):
    return {
        target: MERGED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in MERGED_RAW
    }


def graph(g1, g2, measured, rotation=None):
    initial, _case, _updated = source(g1, g2, measured)
    outputs = expected(g1, g2, measured)
    if rotation is not None:
        shift = (103, -107, 109)
        initial = c53.transform_records(initial, rotation, shift)
        outputs = c53.transform_records(outputs, rotation, shift)
    sites = tuple(outputs)
    index = {site: bit for bit, site in enumerate(sites)}
    all_mask = (1 << len(sites)) - 1
    queue = deque((0,))
    seen = {0}
    edges = 0
    terminals = 0
    bad = []
    maximum = 0
    while queue:
        mask = queue.popleft()
        records = dict(initial)
        records.update({site: outputs[site] for site, bit_index in index.items() if mask >> bit_index & 1})
        actual = enabled(records)
        wrong = {
            site: values for site, values in actual.items()
            if site not in outputs or values != frozenset((outputs[site],))
        }
        if wrong:
            bad.append((mask, wrong)); continue
        futures = tuple(site for site in actual if site in index and not (mask >> index[site] & 1))
        maximum = max(maximum, len(futures))
        if mask == all_mask:
            terminals += int(not actual)
            if actual: bad.append((mask, actual))
            continue
        if not futures:
            bad.append((mask, "dead")); continue
        for site in futures:
            edges += 1
            future = mask | 1 << index[site]
            if future not in seen:
                seen.add(future); queue.append(future)
    return len(seen), edges, terminals, maximum, tuple(bad)


def main() -> int:
    print("ROLES", CASE_ROLE, LANE_OUTPUT, SELECTOR_BRANCH)
    print("TABLE", len(CASE_TABLE), len(LANE_TABLE), len(COPY_TABLE), len(CANONICAL_TABLE), len(ROUTER_RAW), len(MERGED_RAW), len(RAW_CONFLICTS))
    if RAW_CONFLICTS:
        print("CONFLICT_SAMPLE", tuple(RAW_CONFLICTS.items())[:20])
    failures = []
    instances = 0
    # All six bases and thirty signed measurements at identity.
    for state_id in range(60):
        for basis in algebra.all_bases(state_id):
            for measurement_id in range(15):
                for outcome_bit in (0, 1):
                    measured = algebra.measurement_row(measurement_id, outcome_bit)
                    result = graph(*basis, measured)
                    instances += 1
                    if result != (10, 13, 1, 2, ()):
                        failures.append((state_id, basis, measurement_id, outcome_bit, result))
    # Full covariance on the canonical stored basis.
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for state_id in range(60):
            basis = algebra.STATE_GENERATORS[state_id]
            for measurement_id in range(15):
                for outcome_bit in (0, 1):
                    measured = algebra.measurement_row(measurement_id, outcome_bit)
                    result = graph(*basis, measured, rotation)
                    instances += 1
                    if result != (10, 13, 1, 2, ()):
                        failures.append((rotation_index, state_id, measurement_id, outcome_bit, result))
    print("GRAPHS", instances, len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])
    result = not RAW_CONFLICTS and not failures
    print("RESULT", "PHYSICAL_FOUR_CASE_PIVOT_ROUTER" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
