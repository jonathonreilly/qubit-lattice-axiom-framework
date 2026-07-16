#!/usr/bin/env python3
"""Cycle 53 bounded direct official-seed-to-rail nucleation obstruction.

The runner exhausts every proper-cubic placement of the exact Cycle-52
A-slice/backstop that is support-safe and radius-one adjacent to the exact
seven-record Cycle-43/47 seed.  In the target-only, exact-signature class no
placement admits more than two parasite-free writes.  A natural best placement
writes BACKSTOP and LAUNCH_A, then reaches an unavoidable rotated two-output
fork.  Auxiliary frame-orbit nucleators remain outside the negative class.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from functools import lru_cache
from itertools import permutations, product
from pathlib import Path

import self_extending_frame_cage_rail_cycle52_2026_07_14 as c52


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "OFFICIAL_SEED_TO_RAIL_NUCLEATION_CYCLE53_NOTE_2026-07-14.md"
CYCLE43 = REVIEW / "STRICT_NN_RECORD_LAW_COMPILER_CYCLE43_NOTE_2026-07-14.md"
CYCLE47 = REVIEW / "SEED_ORBIT_WRITE_ONCE_TRANSDUCER_CYCLE47_NOTE_2026-07-14.md"
CYCLE52 = REVIEW / "SELF_EXTENDING_FRAME_CAGE_RAIL_CYCLE52_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
Rotation = tuple[Coord, Coord, Coord]
Signature = tuple[tuple[Coord, str], ...]

DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0), (-1, 0, 0), (0, 1, 0),
    (0, -1, 0), (0, 0, 1), (0, 0, -1),
)


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def add(a: Coord, b: Coord) -> Coord:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def subtract(a: Coord, b: Coord) -> Coord:
    return tuple(x - y for x, y in zip(a, b))  # type: ignore[return-value]


def dot(a: Coord, b: Coord) -> int:
    return sum(x * y for x, y in zip(a, b))


def cross(a: Coord, b: Coord) -> Coord:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def determinant(matrix: Rotation) -> int:
    return dot(matrix[0], cross(matrix[1], matrix[2]))


def matvec(matrix: Rotation, vector: Coord) -> Coord:
    return tuple(dot(row, vector) for row in matrix)  # type: ignore[return-value]


def proper_cubic_rotations() -> tuple[Rotation, ...]:
    answer: set[Rotation] = set()
    for columns in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for row, column in enumerate(columns):
                values = [0, 0, 0]
                values[column] = signs[row]
                rows.append(tuple(values))
            matrix = tuple(rows)  # type: ignore[assignment]
            if determinant(matrix) == 1:
                answer.add(matrix)
    return tuple(sorted(answer))


ROTATIONS = proper_cubic_rotations()


def seed_records() -> dict[Coord, str]:
    return {
        (0, 0, 0): "Z0",
        (0, 1, 0): "H1",
        (0, 2, 0): "H0",
        (0, 3, 0): "H1",
        (0, 0, 1): "H1",
        (0, 0, 2): "H0",
        (1, 1, 1): "H1",
    }


def official_support() -> frozenset[Coord]:
    seed = seed_records()
    support = set(seed) | {(0, -1, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0)}
    header = tuple(position for position in seed if position != (0, 0, 0))
    for step in (1, 2, 3):
        support.update((x + step, y, z) for x, y, z in header)
    return frozenset(support)


def local_signature(records: dict[Coord, str], target: Coord) -> Signature:
    return tuple(sorted(
        (direction, records[add(target, direction)])
        for direction in DIRECTIONS
        if add(target, direction) in records
    ))


def rotate_signature(signature: Signature, rotation: Rotation) -> Signature:
    return tuple(sorted((matvec(rotation, offset), content) for offset, content in signature))


@lru_cache(maxsize=None)
def canonical_signature(signature: Signature) -> Signature:
    return min(rotate_signature(signature, rotation) for rotation in ROTATIONS)


def open_candidates(records: dict[Coord, str]) -> set[Coord]:
    return {
        add(position, direction)
        for position in records
        for direction in DIRECTIONS
        if add(position, direction) not in records
    }


def signature_classes(records: dict[Coord, str]) -> dict[Signature, list[Coord]]:
    classes: dict[Signature, list[Coord]] = {}
    for target in open_candidates(records):
        key = canonical_signature(local_signature(records, target))
        classes.setdefault(key, []).append(target)
    for targets in classes.values():
        targets.sort()
    return classes


def transform_records(records: dict[Coord, str], rotation: Rotation, shift: Coord) -> dict[Coord, str]:
    return {add(matvec(rotation, position), shift): content for position, content in records.items()}


def motif_placements() -> tuple[dict[Coord, str], ...]:
    seed = seed_records()
    neighbors = open_candidates(seed)
    placements: dict[tuple[tuple[Coord, str], ...], dict[Coord, str]] = {}
    canonical = c52.seed_records()
    for rotation in ROTATIONS:
        moved = transform_records(canonical, rotation, (0, 0, 0))
        for motif_site in moved:
            for neighbor in neighbors:
                shift = subtract(neighbor, motif_site)
                placement = {add(position, shift): content for position, content in moved.items()}
                placements[tuple(sorted(placement.items()))] = placement
    return tuple(placements.values())


def support_safe_placements() -> tuple[dict[Coord, str], ...]:
    seed = seed_records()
    neighbors = open_candidates(seed)
    support = official_support()
    return tuple(
        placement
        for placement in motif_placements()
        if set(placement).isdisjoint(support) and bool(set(placement) & neighbors)
    )


def direct_reachability(placement: dict[Coord, str]) -> tuple[int, int]:
    """Reachability when every append must be one of the thirteen motif roles."""

    items = tuple(placement.items())
    seen = {0}
    stack = [0]
    maximum = 0
    while stack:
        mask = stack.pop()
        maximum = max(maximum, mask.bit_count())
        records = seed_records()
        for index, (position, content) in enumerate(items):
            if mask & (1 << index):
                records[position] = content
        classes = signature_classes(records)
        for index, (target, _content) in enumerate(items):
            if mask & (1 << index):
                continue
            key = canonical_signature(local_signature(records, target))
            if classes.get(key) == [target]:
                future = mask | (1 << index)
                if future not in seen:
                    seen.add(future)
                    stack.append(future)
    return maximum, len(seen)


NATURAL_ROTATION: Rotation = ((-1, 0, 0), (0, 0, 1), (0, 1, 0))
NATURAL_SHIFT: Coord = (-1, 0, 0)


def natural_motif() -> dict[Coord, str]:
    return transform_records(c52.seed_records(), NATURAL_ROTATION, NATURAL_SHIFT)


def orbit_aliases(records: dict[Coord, str], target: Coord) -> list[Coord]:
    key = canonical_signature(local_signature(records, target))
    return signature_classes(records).get(key, [])


@dataclass(frozen=True)
class Rule:
    required: Signature
    output: str


def variants(rule: Rule) -> tuple[Rule, ...]:
    return tuple(Rule(signature, rule.output) for signature in sorted({rotate_signature(rule.required, r) for r in ROTATIONS}))


def rule_outputs(rules: tuple[Rule, ...]) -> dict[Signature, set[str]]:
    outputs: dict[Signature, set[str]] = {}
    for rule in rules:
        outputs.setdefault(rule.required, set()).add(rule.output)
    return outputs


def enabled_for_rule(records: dict[Coord, str], signature_key: Signature, output: str) -> dict[Coord, str]:
    return {
        target: output
        for target in open_candidates(records)
        if canonical_signature(local_signature(records, target)) == signature_key
    }


def one_sided_fork_graph(records: dict[Coord, str], key: Signature, output: str) -> tuple[int, int, set[tuple[tuple[Coord, str], ...]]]:
    state = lambda r: tuple(sorted(r.items()))
    queue = deque((records,))
    seen = {state(records)}
    terminals: set[tuple[tuple[Coord, str], ...]] = set()
    edges = 0
    while queue:
        current = queue.popleft()
        enabled = enabled_for_rule(current, key, output)
        if not enabled:
            terminals.add(state(current))
            continue
        for target, content in enabled.items():
            future = dict(current)
            future[target] = content
            edges += 1
            encoded = state(future)
            if encoded not in seen:
                seen.add(encoded)
                queue.append(future)
    return len(seen), edges, terminals


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def source_contract() -> None:
    section("A - Sources, authority, and exact boundary")
    for path in (NOTE, CYCLE43, CYCLE47, CYCLE52, AXIOMS):
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    check("A note is authority-free", "authority: none" in note)
    check("A note authorizes no foundation or audit edit", "no live foundation or audit edit is authorized" in note)
    check("A note issues no audit verdict", "no audit verdict" in note)
    check("A state remains record-only", "a state is a configuration of records" in axioms)
    check("A records remain permanent", "records are permanent" in axioms)
    check("A exact official seed has seven records", len(seed_records()) == 7)
    check("A exact Cycle-52 nucleation target has thirteen records", len(c52.seed_records()) == 13)
    check("A proper cubic group has 24 elements", len(ROTATIONS) == 24)


def placement_census() -> tuple[dict[Coord, str], ...]:
    section("B - Complete support-safe adjacent placement census")
    placements = motif_placements()
    valid = support_safe_placements()
    support = official_support()
    seed_neighbors = open_candidates(seed_records())
    far_open = ((100, 100, 100), (-100, -100, -100))
    check(
        "B zero-parent signature aliases arbitrary open sites",
        all(local_signature(seed_records(), site) == () for site in far_open)
        and all(site not in support for site in far_open),
    )
    check("B adjacency-generated placement census has 3470 objects", len(placements) == 3470)
    check("B exactly 1468 placements avoid all official support", len(valid) == 1468)
    check("B every retained placement has thirteen distinct sites", all(len(p) == 13 for p in valid))
    check("B every retained placement is disjoint from official support", all(set(p).isdisjoint(support) for p in valid))
    check("B every retained placement has a radius-one seed contact", all(bool(set(p) & seed_neighbors) for p in valid))
    check("B every retained object contains a possible first local target", all(any(target in p for target in seed_neighbors) for p in valid))
    natural = natural_motif()
    check("B natural behind-front placement is in the retained census", tuple(sorted(natural.items())) in {tuple(sorted(p.items())) for p in valid})
    check("B natural placement avoids official support", set(natural).isdisjoint(support))
    return valid


def exhaustive_direct_class(valid: tuple[dict[Coord, str], ...]) -> None:
    section("C - Exhaustive target-only exact-NN construction class")
    depth_histogram: Counter[int] = Counter()
    reachable_total = 0
    for placement in valid:
        depth, states = direct_reachability(placement)
        depth_histogram[depth] += 1
        reachable_total += states
    check("C direct-depth histogram is exact", depth_histogram == Counter({0: 1440, 1: 8, 2: 20}), str(sorted(depth_histogram.items())))
    check("C all placement searches contain exactly 1516 reachable subsets", reachable_total == 1516)
    check("C no support-safe placement completes the thirteen-role motif", depth_histogram[13] == 0)
    check("C no direct placement writes more than two roles", max(depth_histogram) == 2)
    check("C exactly twenty placements attain the two-write maximum", depth_histogram[2] == 20)
    check("C 1440 placements cannot make even one unique exact write", depth_histogram[0] == 1440)


def natural_fork_and_async_graph() -> None:
    section("D - Exact best-prefix fork, conflicts, and asynchronous schedules")
    motif = natural_motif()
    records = seed_records()
    backstop = (0, 1, 1)
    launcher = (-1, 1, 1)
    left = (-1, 1, 0)
    right = (-1, 0, 1)
    check("D natural backstop has the declared role", motif.get(backstop) == "BACKSTOP")
    check("D backstop signature has three H1 parents", [content for _, content in local_signature(records, backstop)] == ["H1", "H1", "H1"])
    check("D backstop is the unique rotated-signature target", orbit_aliases(records, backstop) == [backstop])
    records[backstop] = "BACKSTOP"
    check("D launcher is the unique exact BACKSTOP target", orbit_aliases(records, launcher) == [launcher])
    records[launcher] = "LAUNCH_A"
    check("D fork roles are distinct Cycle-52 contents", motif[left] == "A_0_1" and motif[right] == "A_1_0")
    check("D two desired fork sites have the same rotated signature", canonical_signature(local_signature(records, left)) == canonical_signature(local_signature(records, right)))
    check("D fork orbit has exactly the two desired sites", orbit_aliases(records, left) == sorted((left, right)))

    left_rule = Rule(local_signature(records, left), motif[left])
    right_rule = Rule(local_signature(records, right), motif[right])
    outputs = rule_outputs(tuple(v for rule in (left_rule, right_rule) for v in variants(rule)))
    check("D both desired rules create a mixed-rotation output conflict", any(len(values) == 2 for values in outputs.values()))
    check("D conflict outputs are exactly the two required permanent roles", any(values == {"A_0_1", "A_1_0"} for values in outputs.values()))

    key = canonical_signature(local_signature(records, left))
    states, edges, terminals = one_sided_fork_graph(records, key, motif[left])
    check("D one-sided repair has four reachable asynchronous states", states == 4)
    check("D one-sided repair has four legal schedule edges", edges == 4)
    check("D all schedules join one terminal", len(terminals) == 1)
    terminal = dict(next(iter(terminals)))
    check("D joined terminal permanently writes the wrong role at one site", terminal.get(left) == terminal.get(right) == "A_0_1" and motif[right] == "A_1_0")
    classes = signature_classes(records)
    check("D stalled prefix has no singleton open signature class", all(len(targets) >= 2 for targets in classes.values()))


def supplied_handoff_and_covariance() -> None:
    section("E - Supplied-motif handoff and proper-cubic covariance controls")
    motif = natural_motif()
    combined = seed_records()
    combined.update(motif)
    first = c52.bounded_sequence(1)[0]
    expected_target = add(matvec(NATURAL_ROTATION, first[0]), NATURAL_SHIFT)
    expected = {expected_target: first[1]}
    check("E supplied natural motif exposes exact Cycle-52 frontier", c52.enabled_assignments(combined) == expected)
    check("E original seed causes no extra Cycle-52 target", c52.enabled_assignments(motif) == c52.enabled_assignments(combined))
    check("E handoff target lies beyond the official front", expected_target not in official_support())

    for index, rotation in enumerate(ROTATIONS):
        shift = (11, -7, 5)
        moved_seed = transform_records(seed_records(), rotation, shift)
        moved_motif = transform_records(motif, rotation, shift)
        moved = dict(moved_seed)
        moved.update(moved_motif)
        moved_target = add(matvec(rotation, expected_target), shift)
        check(f"E rotated supplied handoff {index:02d}", c52.enabled_assignments(moved) == {moved_target: first[1]})


def documentation_gate() -> None:
    section("F - Bounded negative, residual, and fresh N1-N8")
    note = normalized(NOTE)
    required = (
        "direct_target_only_exact_nn_nucleator",
        "official_seed_to_rail_nucleation",
        "auxiliary_frame_orbit_nucleator",
        "not a no-go",
        "no live axiom edit",
        "### n1 — alternative route enumeration",
        "### n2 — wall-independence audit",
        "### n3 — hidden-wall scan",
        "### n4 — exact residual matching",
        "### n5 — rhetoric and resolution audit",
        "### n6 — partial-closure paths",
        "### n7 — strongest steelman",
        "### n8 — cross-cycle echo",
        "hostile steelman:",
        "outcome:",
        "no-go-discipline status: pass",
    )
    for phrase in required:
        check(f"F note contains: {phrase}", phrase in note)
    attempted_routes = (
        "zero-parent all-open start | attempted",
        "every support-safe adjacent direct placement | attempted",
        "adaptive-order target-only superset | attempted",
        "two distinct rules at the natural fork | attempted",
        "one-sided common-output repair at the natural fork | attempted",
        "unique single-target auxiliary after the best prefix | attempted",
    )
    check(
        "F N1 names every executed loophole attack",
        all(route in note for route in attempted_routes),
    )
    check("F N1 uses no prior foreclosure", "| ruled out by prior |" not in note)
    check("F N2 audits all ten unordered field pairs", note.count("| no | no |") == 10)
    check("F N2 keeps one nucleation residual", "collapsed residual set: {w_n}" in note)
    check(
        "F N3 states the precise semantic boundary",
        all(
            phrase in note
            for phrase in (
                "asynchronous single-site append rules",
                "fixed scalar cycle-52 output labels",
                "finite 29-site cycle-47 official block",
            )
        ),
    )
    check("F N3 resolves hidden conditions", "unresolved hidden conditions: 0" in note)
    check("F N4 drops mismatched evidence", "drop as negative evidence" in note)
    check("F N5 leaves auxiliary nucleation open", "auxiliary nucleator | not tested / open" in note)
    check("F N6 preserves three closure paths", all(path in note for path in ("symmetric pair", "frame-coded scaffold", "reversible carrier")))
    check("F N7 defeats universal rhetoric", "defeats any universal nucleation no-go" in note)
    check("F N8 carries Cycles 43, 47, 50, 52", all(f"cycle {number}" in note for number in (43, 47, 50, 52)))
    check("F note reports exact runner count", "pass_count_placeholder" not in note)


def main() -> int:
    source_contract()
    valid = placement_census()
    exhaustive_direct_class(valid)
    natural_fork_and_async_graph()
    supplied_handoff_and_covariance()
    documentation_gate()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: DIRECT_TARGET_ONLY_EXACT_NN_NUCLEATOR is rejected across "
        "all support-safe adjacent placements; AUXILIARY_FRAME_ORBIT_NUCLEATOR "
        "remains open inside OFFICIAL_SEED_TO_RAIL_NUCLEATION"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
