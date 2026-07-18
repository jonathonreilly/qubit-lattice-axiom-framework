#!/usr/bin/env python3
"""Cycle 50 finite frame-caged write-once motif micro-probe.

The executable object is intentionally small.  Three role-distinct
orthogonal parents select one target; the same caged signature advances a
HEAD over a finite pre-laid two-guide rail; distinct end guides turn the last
advance into READY.  All 24 proper-cubic rule images are live together.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "FRAME_CAGED_LOCAL_MOTIF_CYCLE50_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
CYCLE47 = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "SEED_ORBIT_WRITE_ONCE_TRANSDUCER_CYCLE47_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
Rotation = tuple[Coord, Coord, Coord]
StateKey = tuple[tuple[Coord, str], ...]

DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
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


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def subtract(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def dot(left: Coord, right: Coord) -> int:
    return sum(a * b for a, b in zip(left, right))


def cross(left: Coord, right: Coord) -> Coord:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def determinant(matrix: Rotation) -> int:
    return dot(matrix[0], cross(matrix[1], matrix[2]))


def matvec(matrix: Rotation, vector: Coord) -> Coord:
    return tuple(dot(row, vector) for row in matrix)  # type: ignore[return-value]


def proper_cubic_rotations() -> tuple[Rotation, ...]:
    rotations: set[Rotation] = set()
    for columns in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows: list[Coord] = []
            for row, column in enumerate(columns):
                values = [0, 0, 0]
                values[column] = signs[row]
                rows.append(tuple(values))  # type: ignore[arg-type]
            matrix = tuple(rows)  # type: ignore[assignment]
            if determinant(matrix) == 1:
                rotations.add(matrix)
    return tuple(sorted(rotations))


ROTATIONS = proper_cubic_rotations()


def neighbors(position: Coord) -> frozenset[Coord]:
    return frozenset(add(position, direction) for direction in DIRECTIONS)


def state_key(records: dict[Coord, str]) -> StateKey:
    return tuple(sorted(records.items()))


def local_signature(
    records: dict[Coord, str], target: Coord
) -> tuple[tuple[Coord, str], ...]:
    return tuple(
        sorted(
            (direction, records[add(target, direction)])
            for direction in DIRECTIONS
            if add(target, direction) in records
        )
    )


def rotate_signature(
    signature: tuple[tuple[Coord, str], ...], rotation: Rotation
) -> tuple[tuple[Coord, str], ...]:
    return tuple(
        sorted((matvec(rotation, offset), content) for offset, content in signature)
    )


@dataclass(frozen=True)
class Rule:
    name: str
    required: tuple[tuple[Coord, str], ...]
    output: str
    exact: bool = True


def variants(rule: Rule) -> tuple[Rule, ...]:
    signatures = {
        rotate_signature(rule.required, rotation) for rotation in ROTATIONS
    }
    return tuple(
        Rule(rule.name, signature, rule.output, rule.exact)
        for signature in sorted(signatures)
    )


INIT = Rule(
    "INIT_FRAME_CAGE",
    (((-1, 0, 0), "A"), ((0, -1, 0), "B"), ((0, 0, -1), "C")),
    "HEAD",
)
STEP = Rule(
    "PROPAGATE_FRAME_CAGE",
    (((-1, 0, 0), "HEAD"), ((0, -1, 0), "GB"), ((0, 0, -1), "GC")),
    "HEAD",
)
HANDSHAKE = Rule(
    "TERMINAL_HANDSHAKE",
    (((-1, 0, 0), "HEAD"), ((0, -1, 0), "EB"), ((0, 0, -1), "EC")),
    "READY",
)
RULES = tuple(
    variant
    for base_rule in (INIT, STEP, HANDSHAKE)
    for variant in variants(base_rule)
)


def matches(rule: Rule, records: dict[Coord, str], target: Coord) -> bool:
    if target in records:
        return False
    signature = local_signature(records, target)
    required = set(rule.required)
    if not required.issubset(signature):
        return False
    return not rule.exact or len(signature) == len(required)


def enabled_assignments(
    records: dict[Coord, str], rules: tuple[Rule, ...] = RULES
) -> dict[Coord, str]:
    candidates = {
        add(position, direction)
        for position in records
        for direction in DIRECTIONS
        if add(position, direction) not in records
    }
    outputs: dict[Coord, set[str]] = {}
    for target in candidates:
        for rule in rules:
            if matches(rule, records, target):
                outputs.setdefault(target, set()).add(rule.output)
    conflicts = {target: values for target, values in outputs.items() if len(values) > 1}
    if conflicts:
        raise RuntimeError(f"output conflict: {conflicts}")
    return {target: next(iter(values)) for target, values in outputs.items()}


def append(records: dict[Coord, str], target: Coord, content: str) -> dict[Coord, str]:
    if target in records:
        raise ValueError(f"overwrite attempted at {target}")
    future = dict(records)
    future[target] = content
    return future


def motif_seed() -> dict[Coord, str]:
    return {
        (-1, 0, 0): "A",
        (0, -1, 0): "B",
        (0, 0, -1): "C",
        (1, -1, 0): "GB",
        (1, 0, -1): "GC",
        (2, -1, 0): "GB",
        (2, 0, -1): "GC",
        (3, -1, 0): "EB",
        (3, 0, -1): "EC",
    }


WRITE_SEQUENCE: tuple[tuple[Coord, str], ...] = (
    ((0, 0, 0), "HEAD"),
    ((1, 0, 0), "HEAD"),
    ((2, 0, 0), "HEAD"),
    ((3, 0, 0), "READY"),
)


def transform_records(
    records: dict[Coord, str], rotation: Rotation, shift: Coord = (0, 0, 0)
) -> dict[Coord, str]:
    return {
        add(matvec(rotation, position), shift): content
        for position, content in records.items()
    }


def transform_sequence(
    sequence: tuple[tuple[Coord, str], ...],
    rotation: Rotation,
    shift: Coord = (0, 0, 0),
) -> tuple[tuple[Coord, str], ...]:
    return tuple(
        (add(matvec(rotation, position), shift), content)
        for position, content in sequence
    )


def expected_frontier(
    records: dict[Coord, str],
    sequences: tuple[tuple[tuple[Coord, str], ...], ...],
) -> dict[Coord, str]:
    expected: dict[Coord, str] = {}
    for sequence in sequences:
        for target, content in sequence:
            if target not in records:
                expected[target] = content
                break
    return expected


def exhaustive_graph(
    seed: dict[Coord, str],
    sequences: tuple[tuple[tuple[Coord, str], ...], ...],
) -> tuple[set[StateKey], set[StateKey], int, int]:
    queue = deque((seed,))
    seen = {state_key(seed)}
    terminal: set[StateKey] = set()
    edges = 0
    frontier_mismatches = 0
    while queue:
        records = queue.popleft()
        enabled = enabled_assignments(records)
        expected = expected_frontier(records, sequences)
        if enabled != expected:
            frontier_mismatches += 1
        if not expected:
            if not enabled:
                terminal.add(state_key(records))
            continue
        if not enabled:
            continue
        for target, content in enabled.items():
            edges += 1
            future = append(records, target, content)
            key = state_key(future)
            if key not in seen:
                seen.add(key)
                queue.append(future)
    return seen, terminal, edges, frontier_mismatches


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def source_and_rule_contract() -> None:
    section("A - Source, authority, and finite rule contract")
    for path in (NOTE, AXIOMS, CYCLE47):
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    check("A note is authority-free", "authority: none" in note)
    check(
        "A note authorizes no foundation edit",
        "no live foundation or audit edit is authorized" in note,
    )
    check("A state remains record-only", "a state is a configuration of records" in axioms)
    check("A records remain permanent", "records are permanent" in axioms)
    check("A proper cubic group has 24 elements", len(ROTATIONS) == 24)
    check("A each three-role signature has a 24-member orbit", all(len(variants(rule)) == 24 for rule in (INIT, STEP, HANDSHAKE)))
    check("A combined table has exactly 72 rotated rules", len(RULES) == 72)
    signature_outputs: dict[tuple[tuple[Coord, str], ...], set[str]] = {}
    for rule in RULES:
        signature_outputs.setdefault(rule.required, set()).add(rule.output)
    check("A rotated rule table has no output conflict", all(len(values) == 1 for values in signature_outputs.values()))


def control_failures_and_cage() -> None:
    section("B - One-parent, two-parent, and unique-cage controls")
    one_rule = variants(Rule("ONE", (((-1, 0, 0), "A"),), "X"))
    one_enabled = enabled_assignments({(0, 0, 0): "A"}, one_rule)
    check("B one-parent orbit enables all six neighboring targets", len(one_enabled) == 6)
    check("B one-parent control cannot choose an orientation", set(one_enabled.values()) == {"X"})

    two_rule = variants(
        Rule("TWO", (((-1, 0, 0), "A"), ((0, -1, 0), "B")), "X")
    )
    two_seed = {(-1, 0, 0): "A", (0, -1, 0): "B"}
    two_enabled = enabled_assignments(two_seed, two_rule)
    expected_two = {(0, 0, 0), (-1, -1, 0)}
    check("B uncaged role-distinct two-parent rule has two targets", set(two_enabled) == expected_two)
    blocked = dict(two_seed)
    blocked[(-1, -1, 0)] = "BLOCK"
    blocked_enabled = enabled_assignments(blocked, two_rule)
    check("B occupying the alternate cages the two-parent target", blocked_enabled == {(0, 0, 0): "X"})

    triple_parents = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
    common = set.intersection(*(set(neighbors(parent)) for parent in triple_parents))
    check("B three orthogonal parents have one common target", common == {(0, 0, 0)})
    stabilizer = [
        rotation
        for rotation in ROTATIONS
        if rotate_signature(INIT.required, rotation) == INIT.required
    ]
    check("B role-distinct triple has trivial proper-cubic stabilizer", len(stabilizer) == 1)
    initial_enabled = enabled_assignments(motif_seed())
    check("B all mixed rotated rules select only the caged origin", initial_enabled == {(0, 0, 0): "HEAD"})


def single_motif_and_covariance() -> None:
    section("C - Frame-preserving propagation, handshake, and covariance")
    records = motif_seed()
    written: list[Coord] = []
    for index, (target, content) in enumerate(WRITE_SEQUENCE):
        enabled = enabled_assignments(records)
        check(f"C step {index} has exactly its declared target", enabled == {target: content})
        check(f"C step {index} target is previously open", target not in records)
        records = append(records, target, content)
        written.append(target)
    check("C terminal READY content is record-visible", records.get((3, 0, 0)) == "READY")
    check("C terminal motif has no enabled cross-fire", not enabled_assignments(records))
    check("C every dynamic site is written once", len(written) == len(set(written)) == 4)
    check("C no seed or guide record is overwritten", len(records) == len(motif_seed()) + 4)

    for index, rotation in enumerate(ROTATIONS):
        shift = (7, -5, 3)
        moved = transform_records(motif_seed(), rotation, shift)
        sequence = transform_sequence(WRITE_SEQUENCE, rotation, shift)
        valid = True
        for target, content in sequence:
            if enabled_assignments(moved) != {target: content}:
                valid = False
                break
            moved = append(moved, target, content)
        valid &= not enabled_assignments(moved)
        check(f"C rotated/translated graph replay {index:02d}", valid)


def asynchronous_mixed_motifs() -> None:
    section("D - Exhaustive mixed-orientation asynchronous graph")
    rotation = ROTATIONS[7]
    left_shift = (-10, 0, 0)
    right_shift = (10, 0, 0)
    left_seed = transform_records(motif_seed(), ROTATIONS[0], left_shift)
    right_seed = transform_records(motif_seed(), rotation, right_shift)
    combined = dict(left_seed)
    check("D two static motifs have disjoint supports", set(combined).isdisjoint(right_seed))
    combined.update(right_seed)
    sequences = (
        transform_sequence(WRITE_SEQUENCE, ROTATIONS[0], left_shift),
        transform_sequence(WRITE_SEQUENCE, rotation, right_shift),
    )
    seen, terminals, edges, mismatches = exhaustive_graph(combined, sequences)
    check("D exhaustive product graph has 25 reachable states", len(seen) == 25)
    check("D exhaustive product graph has 40 directed edges", edges == 40)
    check("D every reachable enabled set equals the declared frontier", mismatches == 0)
    check("D every asynchronous order reaches one terminal state", len(terminals) == 1)
    terminal = dict(next(iter(terminals)))
    ready_targets = {sequence[-1][0] for sequence in sequences}
    check("D terminal has exactly both READY writes", all(terminal.get(target) == "READY" for target in ready_targets))
    dynamic_targets = {target for sequence in sequences for target, _ in sequence}
    check("D no parasitic dynamic target appears", dynamic_targets <= set(terminal) and len(terminal) == len(combined) + 8)


def documentation_gate() -> None:
    section("E - Bounded theorem and N1-N8 documentation gate")
    note = normalized(NOTE)
    required = (
        "frame_caged_local_motif",
        "self_extending_frame_cage_rail",
        "not w_c",
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
        check(f"E note contains: {phrase}", phrase in note)
    check("E N1 has at least five ATTEMPTED routes", note.count("| attempted |") >= 5)
    check("E N1 uses no prior-foreclosure marker", "| ruled out by prior |" not in note)
    check("E N2 collapses to one residual", "collapsed residual set: {w_r}" in note)
    check("E N3 resolves hidden-condition scan", "unresolved hidden conditions: 0" in note)
    check("E N4 drops mismatched evidence", "drop as negative evidence" in note)
    check("E N5 leaves complete W_C open", "complete w_c | not tested / open" in note)
    check("E N6 preserves three positive paths", all(path in note for path in ("cage-builder", "frame-coded", "reversible carrier")))
    check("E N7 defeats impossibility rhetoric", "defeats any impossibility claim" in note)
    check("E N8 carries Cycles 34, 43, and 47", all(f"cycle {number}" in note for number in (34, 43, 47)))


def main() -> int:
    source_and_rule_contract()
    control_failures_and_cage()
    single_motif_and_covariance()
    asynchronous_mixed_motifs()
    documentation_gate()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: a finite pre-laid three-role cage propagates and handshakes "
        "covariantly without aliases; autonomous guide-rail growth remains "
        "SELF_EXTENDING_FRAME_CAGE_RAIL"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
