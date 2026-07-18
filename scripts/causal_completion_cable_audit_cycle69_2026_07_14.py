#!/usr/bin/env python3
"""Cycle 69: causal audit of the Cycle-67 completion cable.

Cycle 67 deliberately compiled every locally parent-valid subset and then
reported any rotated match outside the intended target/type map.  That static
scan found apparent aliases, but it did not ask whether the local context can
occur in an append-only causal history.  This runner independently recompiles
the table, reproduces all 47 apparently bad conditions (34 target/output
classes), and applies two independent causal infeasibility certificates:

1. a strict-rank mandatory-ancestor induction; and
2. a generous forward closure which ignores exact signatures and therefore
   over-approximates every correct causal history.

It also exhausts the 16-record F/FP/I1/I2/DONE detector and checks the exact
singleton geometry of C_Q through the two endpoint records.  Authority: none.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from pathlib import Path

import completion_barrier_phase_transducer_cycle67_scratch_2026_07_14 as c67
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "CAUSAL_COMPLETION_CABLE_AUDIT_CYCLE69_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature
Condition = tuple[int, int, int, str, Coord]

ROLE_ORDER = tuple(c67.ROLE_SITES)
RANK = {role: rank for rank, role in enumerate(ROLE_ORDER)}
RANK["Z_C"] = RANK["Z_A"]

# Independently restated from the Cycle-67 intended causal prose.  Every
# requirement is a lower bound on the six exact nearest-neighbour contents.
REQUIREMENTS: dict[str, dict[str, int]] = {
    "F": {"R2": 1, "S8": 1},
    "FP": {"F": 2},
    "I1": {"FP": 1, "R2": 2},
    "I2": {"I1": 1, "R1": 2},
    "DONE": {"I2": 3},
    "L1": {"DONE": 1},
    "L2": {"I2": 1, "L1": 1},
    "L3": {"L2": 2, "R1": 1},
    "L4": {"L3": 1, "R2": 1},
    "L5": {"F": 1, "L4": 1},
    "L6": {"L5": 1},
    "L7": {"F": 1, "L6": 1},
    "L8": {"L7": 2},
    "L9": {"L8": 1},
    "L10": {"L9": 1},
    "L11": {"L10": 2},
    "L12": {"H1": 1, "L11": 1},
    "C_Q": {"W6": 1, "Z0": 1, "L12": 1},
    "P0": {"C_Q": 1, "OPEN_B": 1},
    "P1": {"P0": 1, "E": 1, "L8": 1, "L10": 1},
    "P2": {"C_Q": 1, "P1": 1, "J6": 1, "L11": 1},
    "P3": {"P2": 1, "E": 1, "L8": 1, "L10": 1},
    "X_B": {"P3": 1, "OPEN_B": 1},
    "Z_A": {"X_B": 1, "P2": 1, "W6": 1, "Z0": 1},
    "Z_C": {"X_B": 1, "OPEN_C": 1},
}

EXPECTED_BAD_CLASSES = frozenset({
    ((-2, -3, -3), "L10", None),
    ((-2, -2, -4), "L10", None),
    ((-2, -2, -3), "L11", "L9"),
    ((-1, -3, -4), "L8", None),
    ((-1, -3, -3), "L9", "L7"),
    ((-1, -2, -4), "L9", "L7"),
    ((-1, -2, -3), "L10", "L8"),
    ((0, -4, -4), "L6", None),
    ((0, -4, -3), "L7", "L5"),
    ((0, -3, -5), "L6", None),
    ((0, -2, -5), "L7", "L5"),
    ((2, -4, -1), "L7", "L5"),
    ((2, -3, 0), "L9", "L7"),
    ((2, -3, 1), "L10", None),
    ((2, -2, 0), "L10", "L8"),
    ((2, -2, 1), "L11", "L9"),
    ((2, 0, -5), "L7", "L5"),
    ((2, 1, -4), "L9", "L7"),
    ((2, 1, -3), "L10", "L8"),
    ((2, 2, -4), "L10", None),
    ((2, 2, -3), "L11", "L9"),
    ((3, -4, -1), "L6", None),
    ((3, -3, -4), "L2", "DONE"),
    ((3, -3, 0), "L8", None),
    ((3, -2, 0), "L9", "L7"),
    ((3, -2, 1), "L10", None),
    ((3, 0, -5), "L6", None),
    ((3, 1, -4), "L8", None),
    ((3, 1, -3), "L9", "L7"),
    ((3, 2, -3), "L10", None),
    ((4, -3, -1), "L6", None),
    ((4, -2, -1), "L7", "L5"),
    ((4, 0, -4), "L6", None),
    ((4, 0, -3), "L7", "L5"),
})

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def parents_hold(output: str, values: list[str | None]) -> bool:
    count = Counter(value for value in values if value is not None)
    return all(count[label] >= minimum for label, minimum in REQUIREMENTS[output].items())


def compile_conditions(
    base: dict[Coord, str],
    rules: dict[Signature, str],
    allowed: dict[Coord, str],
) -> tuple[Condition, ...]:
    """Independent exact-condition compiler for a finite declared footprint."""

    sites = tuple(sorted(allowed))
    index = {site: bit for bit, site in enumerate(sites)}
    occupied = set(base) | set(allowed)
    candidates = {
        c53.add(site, direction)
        for site in occupied
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in base
    }
    raw_rows = {
        (c53.rotate_signature(signature, rotation), output)
        for signature, output in rules.items()
        for rotation in c53.ROTATIONS
    }
    conditions: set[Condition] = set()
    for target in candidates:
        for signature, output in raw_rows:
            expected = dict(signature)
            present = absent = 0
            viable = True
            for direction in c53.DIRECTIONS:
                neighbour = c53.add(target, direction)
                wanted = expected.get(direction)
                if neighbour in base:
                    if wanted != base[neighbour]:
                        viable = False
                        break
                elif neighbour in allowed:
                    bit = 1 << index[neighbour]
                    if wanted is None:
                        absent |= bit
                    elif wanted == allowed[neighbour]:
                        present |= bit
                    else:
                        viable = False
                        break
                elif wanted is not None:
                    viable = False
                    break
            if not viable:
                continue
            target_bit = 1 << index[target] if target in allowed else 0
            if target_bit:
                absent |= target_bit
            conditions.add((present, absent, target_bit, output, target))
    return tuple(sorted(conditions, key=lambda row: (row[4], row[3], row[0], row[1])))


def mask_sites(mask: int, sites: tuple[Coord, ...]) -> frozenset[Coord]:
    return frozenset(site for bit, site in enumerate(sites) if mask & (1 << bit))


def intended_subset_census() -> tuple[int, int, bool]:
    """Audit every local subset against the independently restated predicates."""

    census = matched = 0
    predicates_agree = True
    for target, output in c67.ALLOWED.items():
        neighbours = tuple(
            c53.add(target, direction)
            for direction in c53.DIRECTIONS
            if c53.add(target, direction) in c67.ALLOWED
        )
        for mask in range(1 << len(neighbours)):
            records = dict(c67.BASE)
            records.update({
                site: c67.ALLOWED[site]
                for bit, site in enumerate(neighbours)
                if mask & (1 << bit)
            })
            values = [records.get(c53.add(target, direction)) for direction in c53.DIRECTIONS]
            ours = parents_hold(output, values)
            theirs = c67.causal_parents_hold(output, values)
            predicates_agree &= ours == theirs
            if not ours:
                continue
            census += 1
            signature = c53.canonical_signature(c53.local_signature(records, target))
            matched += c67.RULES.get(signature) == output
    return census, matched, predicates_agree


def minimal_parent_sets() -> dict[Coord, tuple[frozenset[Coord], ...]]:
    """Find every minimal lower-rank parent set at each intended site."""

    alternatives: dict[Coord, tuple[frozenset[Coord], ...]] = {}
    for role in ROLE_ORDER:
        for target in sorted(c67.ROLE_SITES[role]):
            candidates = tuple(sorted(
                neighbour
                for direction in c53.DIRECTIONS
                if (neighbour := c53.add(target, direction)) in c67.ALLOWED
                and RANK[c67.ALLOWED[neighbour]] < RANK[role]
            ))
            satisfying: list[frozenset[Coord]] = []
            for mask in range(1 << len(candidates)):
                present = frozenset(
                    site for bit, site in enumerate(candidates) if mask & (1 << bit)
                )
                records = dict(c67.BASE)
                records.update({site: c67.ALLOWED[site] for site in present})
                values = [records.get(c53.add(target, direction)) for direction in c53.DIRECTIONS]
                if parents_hold(role, values):
                    satisfying.append(present)
            alternatives[target] = tuple(
                option
                for option in satisfying
                if not any(other < option for other in satisfying)
            )
    return alternatives


def mandatory_ancestors(
    alternatives: dict[Coord, tuple[frozenset[Coord], ...]],
) -> dict[Coord, frozenset[Coord]]:
    """Strict-rank fixed point: ancestors common to every parent alternative."""

    mandatory: dict[Coord, frozenset[Coord]] = {}
    for role in ROLE_ORDER:
        for target in sorted(c67.ROLE_SITES[role]):
            closures: list[frozenset[Coord]] = []
            for option in alternatives[target]:
                closure = set(option)
                for parent in option:
                    closure.update(mandatory[parent])
                closures.append(frozenset(closure))
            mandatory[target] = (
                frozenset.intersection(*closures) if closures else frozenset()
            )
    return mandatory


def overapprox_closure(blocked: frozenset[Coord]) -> frozenset[Coord]:
    """Generate everything causal even if no exact signature row exists.

    This is deliberately more permissive than the Cycle-67 law.  Failure to
    realize a bad condition here is therefore a valid infeasibility witness.
    """

    reached: set[Coord] = set()
    changed = True
    while changed:
        changed = False
        for role in ROLE_ORDER:
            for target in sorted(c67.ROLE_SITES[role]):
                if target in reached or target in blocked:
                    continue
                records = dict(c67.BASE)
                records.update({site: c67.ALLOWED[site] for site in reached})
                values = [records.get(c53.add(target, direction)) for direction in c53.DIRECTIONS]
                if parents_hold(role, values):
                    reached.add(target)
                    changed = True
    return frozenset(reached)


def build_detector() -> tuple[dict[Signature, str], dict[Coord, str]]:
    detector_roles = ("F", "FP", "I1", "I2", "DONE")
    allowed = {
        site: role
        for role in detector_roles
        for site in c67.ROLE_SITES[role]
    }
    rules: dict[Signature, str] = {}
    for target, output in allowed.items():
        neighbours = tuple(
            c53.add(target, direction)
            for direction in c53.DIRECTIONS
            if c53.add(target, direction) in allowed
        )
        for mask in range(1 << len(neighbours)):
            records = dict(c67.BASE)
            records.update({
                site: allowed[site]
                for bit, site in enumerate(neighbours)
                if mask & (1 << bit)
            })
            values = [records.get(c53.add(target, direction)) for direction in c53.DIRECTIONS]
            if not parents_hold(output, values):
                continue
            signature = c53.canonical_signature(c53.local_signature(records, target))
            prior = rules.get(signature)
            if prior is not None and prior != output:
                raise ValueError(f"detector conflict: {prior}/{output}")
            rules[signature] = output
    return rules, allowed


def detector_graph(conditions: tuple[Condition, ...], additions: int) -> tuple[int, int, int, int, int]:
    full = (1 << additions) - 1
    queue = deque((0,))
    seen = {0}
    edges = conflicts = 0
    terminals: list[int] = []
    while queue:
        mask = queue.popleft()
        enabled = [
            condition
            for condition in conditions
            if mask & condition[0] == condition[0] and not mask & condition[1]
        ]
        outputs: dict[int, set[str]] = defaultdict(set)
        for _, _, target_bit, output, _ in enabled:
            outputs[target_bit].add(output)
        conflicts += sum(len(values) > 1 for values in outputs.values())
        if not enabled:
            terminals.append(mask)
        for _, _, target_bit, _, _ in enabled:
            future = mask | target_bit
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)
    return len(seen), edges, len(terminals), terminals.count(full), conflicts


def singleton_endpoint_geometry() -> tuple[int, tuple[tuple[str, Coord, tuple[Coord, ...]], ...]]:
    endpoints = {"C_Q", "P0", "P1", "P2", "P3", "X_B", "Z_A", "Z_C"}
    records = dict(c67.BASE)
    rows: list[tuple[str, Coord, tuple[Coord, ...]]] = []
    for role in ROLE_ORDER:
        if role in endpoints:
            classes = c53.signature_classes(records)
            for target in sorted(c67.ROLE_SITES[role]):
                signature = c53.canonical_signature(c53.local_signature(records, target))
                aliases = tuple(
                    site for site in classes.get(signature, ()) if site not in records
                )
                rows.append((role, target, aliases))
        records.update({site: role for site in c67.ROLE_SITES[role]})
    return sum(aliases == (target,) for _, target, aliases in rows), tuple(rows)


def greedy_complete_schedule(conditions: tuple[Condition, ...]) -> tuple[int, int]:
    sites = tuple(sorted(c67.ALLOWED))
    full = (1 << len(sites)) - 1
    mask = 0
    steps = 0
    bad_enabled = 0
    while mask != full:
        for present, absent, target_bit, output, target in conditions:
            if mask & present == present and not mask & absent:
                if not target_bit or output != c67.ALLOWED.get(target):
                    bad_enabled += 1
        enabled_good = [
            condition
            for condition in conditions
            if condition[2]
            and condition[3] == c67.ALLOWED.get(condition[4])
            and mask & condition[0] == condition[0]
            and not mask & condition[1]
        ]
        if not enabled_good:
            break
        chosen = min(enabled_good, key=lambda row: (RANK[row[3]], row[4]))
        mask |= chosen[2]
        steps += 1
    return steps if mask == full else -steps, bad_enabled


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    check("A01 note exists", NOTE.is_file())
    check("A02 proper cubic group has 24 rotations", len(c53.ROTATIONS) == 24)
    check("A03 independent requirement register covers every role", set(REQUIREMENTS) == set(ROLE_ORDER))
    check("A04 declared role order is strict except the nonadjacent endpoint peers", all(
        RANK[parent] < RANK[role]
        for role, requirements in REQUIREMENTS.items()
        for parent in requirements
        if parent in RANK
    ))

    subset_census, subset_matches, predicates_agree = intended_subset_census()
    check("B01 independent predicates agree on every intended local subset", predicates_agree)
    check("B02 exactly 308 intended parent-valid subsets exist", subset_census == 308, str(subset_census))
    check("B03 all 308 intended subsets have their exact declared row", subset_matches == 308, str(subset_matches))

    conditions = compile_conditions(c67.BASE, c67.RULES, c67.ALLOWED)
    check("C01 independent compiler reproduces Cycle-67 conditions", set(conditions) == set(c67.compile_conditions()))
    good = tuple(
        condition for condition in conditions
        if condition[2] and condition[3] == c67.ALLOWED.get(condition[4])
    )
    bad = tuple(condition for condition in conditions if condition not in good)
    bad_classes = frozenset(
        (target, output, c67.ALLOWED.get(target))
        for _, _, _, output, target in bad
    )
    check("C02 condition census is 355 = 308 intended + 47 apparent bad", (len(conditions), len(good), len(bad)) == (355, 308, 47), f"{len(conditions)}/{len(good)}/{len(bad)}")
    check("C03 exact 34 apparent bad target/output classes reproduced", bad_classes == EXPECTED_BAD_CLASSES, str(len(bad_classes)))
    check("C04 class split is 15 off-footprint + 19 wrong-role", (
        sum(expected is None for _, _, expected in bad_classes),
        sum(expected is not None for _, _, expected in bad_classes),
    ) == (15, 19))
    sites = tuple(sorted(c67.ALLOWED))
    check("C05 every same-target/same-output condition has that target's intended parents", all(
        parents_hold(
            output,
            [
                (
                    c67.ALLOWED[neighbour]
                    if neighbour in mask_sites(present, sites)
                    else c67.BASE.get(neighbour)
                )
                for direction in c53.DIRECTIONS
                for neighbour in (c53.add(target, direction),)
            ],
        )
        for present, _, _, output, target in good
    ))

    alternatives = minimal_parent_sets()
    check("D01 every intended site has a lower-rank causal parent alternative", all(alternatives.values()))
    check("D02 this geometry has one minimal parent set at every site", all(len(options) == 1 for options in alternatives.values()))
    mandatory = mandatory_ancestors(alternatives)
    detector_sites = frozenset(
        site
        for role in ("F", "FP", "I1", "I2", "DONE")
        for site in c67.ROLE_SITES[role]
    )
    done = next(iter(c67.ROLE_SITES["DONE"]))
    check("D03 DONE has all other 15 detector records as mandatory ancestors", mandatory[done] == detector_sites - {done}, str(len(mandatory[done])))

    ancestor_certificates = []
    closure_rejections = []
    for condition in bad:
        present, absent, _, _, _ = condition
        present_sites = mask_sites(present, sites)
        absent_sites = mask_sites(absent, sites)
        witnesses = tuple(sorted(
            (record, ancestor)
            for record in present_sites
            for ancestor in mandatory[record].intersection(absent_sites)
        ))
        ancestor_certificates.append(witnesses)
        closure_rejections.append(not present_sites <= overapprox_closure(absent_sites))
    check("D04 all 47 apparent bad conditions contradict mandatory ancestry", all(ancestor_certificates), str(sum(bool(row) for row in ancestor_certificates)))
    check("D05 independent generous forward closure rejects all 47", all(closure_rejections), str(sum(closure_rejections)))

    detector_rules, detector_allowed = build_detector()
    detector_conditions = compile_conditions(c67.BASE, detector_rules, detector_allowed)
    detector_bad = [
        row for row in detector_conditions
        if not row[2] or row[3] != detector_allowed.get(row[4])
    ]
    check("E01 detector is exactly 6 F / 3 FP / 3 I1 / 3 I2 / 1 DONE", Counter(detector_allowed.values()) == Counter({"F": 6, "FP": 3, "I1": 3, "I2": 3, "DONE": 1}))
    check("E02 detector has 9 canonical rows and 31 compiled conditions", (len(detector_rules), len(detector_conditions)) == (9, 31), f"{len(detector_rules)}/{len(detector_conditions)}")
    check("E03 detector has no static wrong/off-footprint condition", not detector_bad, str(detector_bad))
    graph = detector_graph(detector_conditions, len(detector_allowed))
    check("E04 exact detector graph is 344 states / 1,030 edges", graph[:2] == (344, 1030), str(graph[:2]))
    check("E05 exact detector graph has one complete terminal and no conflict", graph[2:] == (1, 1, 0), str(graph[2:]))

    singleton_count, singleton_rows = singleton_endpoint_geometry()
    check("F01 C_Q and all seven phase/endpoint sites are singleton prefix classes", singleton_count == 8, str(singleton_rows))
    check("F02 endpoint records are nonadjacent commuting peers", c67.c43.manhattan(next(iter(c67.ROLE_SITES["Z_A"])), next(iter(c67.ROLE_SITES["Z_C"]))) == 2)
    pre_relay = set(c67.BASE)
    for role in ROLE_ORDER[: ROLE_ORDER.index("P0")]:
        pre_relay.update(c67.ROLE_SITES[role])
    relay_sites = set().union(*(c67.ROLE_SITES[role] for role in ("P0", "P1", "P2", "P3")))
    check("F03 all four phase relay sites are genuinely fresh before P0", relay_sites.isdisjoint(pre_relay))

    steps, bad_enabled = greedy_complete_schedule(conditions)
    check("G01 an exact declared schedule writes all 91 records", steps == 91, str(steps))
    check("G02 no apparent bad condition is enabled on that schedule", bad_enabled == 0, str(bad_enabled))

    certificate_roles = Counter(
        (c67.ALLOWED[record], c67.ALLOWED[ancestor])
        for witnesses in ancestor_certificates
        for record, ancestor in witnesses
    )
    print(f"\nCONDITIONS={len(conditions)} GOOD={len(good)} APPARENT_BAD={len(bad)} CLASSES={len(bad_classes)}")
    print(f"ANCESTOR_CERTIFICATE_ROLE_PAIRS={dict(sorted(certificate_roles.items()))}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
