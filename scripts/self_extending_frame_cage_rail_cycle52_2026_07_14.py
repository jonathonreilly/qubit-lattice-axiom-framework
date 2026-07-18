#!/usr/bin/env python3
"""Cycle 52 autonomous append-only frame/cage rail.

A complete role-coded 4 x 3 slice cages one interior launch record.  Its only
open neighbour starts the next slice.  The other eleven records copy by a
Hamiltonian sweep: each target sees its old-slice role and the preceding new
role, while the alternate common target is already occupied.  Alternating
ports and reverse sweeps renew this finite mechanism indefinitely.  All proper
cubic images are live in the same rule table.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "SELF_EXTENDING_FRAME_CAGE_RAIL_CYCLE52_NOTE_2026-07-14.md"
CYCLE50 = REVIEW / "FRAME_CAGED_LOCAL_MOTIF_CYCLE50_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
Rotation = tuple[Coord, Coord, Coord]
StateKey = tuple[tuple[Coord, str], ...]

DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0), (-1, 0, 0), (0, 1, 0),
    (0, -1, 0), (0, 0, 1), (0, 0, -1),
)
SLICE = tuple(product(range(4), range(3)))
PORT_A = (1, 1)
PORT_B = (2, 1)
PATH_B: tuple[tuple[int, int], ...] = (
    (1, 1), (1, 2), (0, 2), (0, 1), (0, 0), (1, 0),
    (2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (2, 1),
)
PATH_A = tuple(reversed(PATH_B))


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


def site(x: int, yz: tuple[int, int]) -> Coord:
    return (x, yz[0], yz[1])


def neighbors(position: Coord) -> set[Coord]:
    return {add(position, direction) for direction in DIRECTIONS}


def role(phase: str, yz: tuple[int, int]) -> str:
    if phase in {"A", "C"} and yz == PORT_A:
        return f"LAUNCH_{phase}"
    if phase in {"B", "D"} and yz == PORT_B:
        return f"LAUNCH_{phase}"
    return f"{phase}_{yz[0]}_{yz[1]}"


def slice_records(x: int, phase: str) -> dict[Coord, str]:
    return {site(x, yz): role(phase, yz) for yz in SLICE}


def local_signature(records: dict[Coord, str], target: Coord) -> tuple[tuple[Coord, str], ...]:
    return tuple(sorted(
        (direction, records[add(target, direction)])
        for direction in DIRECTIONS
        if add(target, direction) in records
    ))


def rotate_signature(signature: tuple[tuple[Coord, str], ...], rotation: Rotation) -> tuple[tuple[Coord, str], ...]:
    return tuple(sorted((matvec(rotation, offset), content) for offset, content in signature))


@dataclass(frozen=True)
class Rule:
    name: str
    required: tuple[tuple[Coord, str], ...]
    output: str


def variants(rule: Rule) -> tuple[Rule, ...]:
    signatures = {rotate_signature(rule.required, rotation) for rotation in ROTATIONS}
    return tuple(Rule(rule.name, signature, rule.output) for signature in sorted(signatures))


def phase_rules(old_phase: str, new_phase: str, path: tuple[tuple[int, int], ...]) -> tuple[Rule, ...]:
    old = slice_records(0, old_phase)
    records = dict(old)
    rules: list[Rule] = []
    for index, yz in enumerate(path):
        target = site(1, yz)
        signature = local_signature(records, target)
        rules.append(Rule(f"{old_phase}_TO_{new_phase}_{index:02d}", signature, role(new_phase, yz)))
        records[target] = role(new_phase, yz)
    return tuple(rules)


BASE_RULES = (
    phase_rules("A", "B", PATH_B)
    + phase_rules("B", "C", PATH_A)
    + phase_rules("C", "D", PATH_B)
    + phase_rules("D", "A", PATH_A)
)
RULES = tuple(variant for rule in BASE_RULES for variant in variants(rule))
RULE_OUTPUTS: dict[tuple[tuple[Coord, str], ...], frozenset[str]] = {}
_rule_outputs: dict[tuple[tuple[Coord, str], ...], set[str]] = {}
for _rule in RULES:
    _rule_outputs.setdefault(_rule.required, set()).add(_rule.output)
RULE_OUTPUTS = {signature: frozenset(outputs) for signature, outputs in _rule_outputs.items()}
RULE_CONFLICTS = {
    signature: outputs for signature, outputs in RULE_OUTPUTS.items() if len(outputs) != 1
}
RULE_TABLE = {
    signature: next(iter(outputs))
    for signature, outputs in RULE_OUTPUTS.items()
    if len(outputs) == 1
}


def matches(rule: Rule, records: dict[Coord, str], target: Coord) -> bool:
    return target not in records and local_signature(records, target) == rule.required


def enabled_assignments(records: dict[Coord, str]) -> dict[Coord, str]:
    candidates = {
        add(position, direction)
        for position in records
        for direction in DIRECTIONS
        if add(position, direction) not in records
    }
    outputs: dict[Coord, set[str]] = {}
    for target in candidates:
        signature = local_signature(records, target)
        if signature in RULE_CONFLICTS:
            outputs[target] = set(RULE_CONFLICTS[signature])
        elif signature in RULE_TABLE:
            outputs[target] = {RULE_TABLE[signature]}
    conflicts = {target: values for target, values in outputs.items() if len(values) != 1}
    if conflicts:
        raise RuntimeError(f"output conflict: {conflicts}")
    return {target: next(iter(values)) for target, values in outputs.items()}


def append(records: dict[Coord, str], target: Coord, content: str) -> dict[Coord, str]:
    if target in records:
        raise ValueError(f"overwrite at {target}")
    answer = dict(records)
    answer[target] = content
    return answer


def seed_records() -> dict[Coord, str]:
    answer = slice_records(0, "A")
    answer[site(-1, PORT_A)] = "BACKSTOP"
    return answer


def bounded_sequence(layers: int, x0: int = 0) -> tuple[tuple[Coord, str], ...]:
    answer: list[tuple[Coord, str]] = []
    phases = ("A", "B", "C", "D")
    for step in range(1, layers + 1):
        phase = phases[step % 4]
        path = PATH_B if phase in {"B", "D"} else PATH_A
        answer.extend((site(x0 + step, yz), role(phase, yz)) for yz in path)
    return tuple(answer)


def transform_records(records: dict[Coord, str], rotation: Rotation, shift: Coord) -> dict[Coord, str]:
    return {add(matvec(rotation, position), shift): content for position, content in records.items()}


def transform_sequence(sequence: tuple[tuple[Coord, str], ...], rotation: Rotation, shift: Coord) -> tuple[tuple[Coord, str], ...]:
    return tuple((add(matvec(rotation, target), shift), content) for target, content in sequence)


def first_absent(records: dict[Coord, str], sequence: tuple[tuple[Coord, str], ...]) -> tuple[Coord, str] | None:
    return next(((target, content) for target, content in sequence if target not in records), None)


def state_key(records: dict[Coord, str]) -> StateKey:
    return tuple(sorted(records.items()))


def exhaustive_product(
    seed: dict[Coord, str],
    sequences: tuple[tuple[tuple[Coord, str], ...], ...],
    horizon: int,
) -> tuple[int, int, int, int, set[StateKey]]:
    queue = deque((seed,))
    seen = {state_key(seed)}
    terminal: set[StateKey] = set()
    edges = mismatches = deadlocks = 0
    while queue:
        records = queue.popleft()
        fronts = tuple(first_absent(records, sequence) for sequence in sequences)
        expected = {target: content for item in fronts if item is not None for target, content in (item,)}
        enabled = enabled_assignments(records)
        if enabled != expected:
            mismatches += 1
        completed = all(all(target in records for target, _ in sequence[:horizon]) for sequence in sequences)
        if completed:
            terminal.add(state_key(records))
            continue
        legal = {
            target: content
            for target, content in enabled.items()
            if any(target in {t for t, _ in sequence[:horizon]} for sequence in sequences)
        }
        if not legal:
            deadlocks += 1
            continue
        for target, content in legal.items():
            edges += 1
            future = append(records, target, content)
            key = state_key(future)
            if key not in seen:
                seen.add(key)
                queue.append(future)
    return len(seen), edges, mismatches, deadlocks, terminal


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def source_and_table_contract() -> None:
    section("A - Source, authority, and finite table")
    for path in (NOTE, CYCLE50, AXIOMS):
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    check("A note is authority-free", "authority: none" in note)
    check("A note authorizes no foundation or audit edit", "no live foundation or audit edit is authorized" in note)
    check("A note disclaims W_C completion", "not w_c" in note)
    check("A state remains record-only", "a state is a configuration of records" in axioms)
    check("A records remain permanent", "records are permanent" in axioms)
    check("A proper cubic group has 24 elements", len(ROTATIONS) == 24)
    check("A cross-section has twelve role-distinct sites", len(SLICE) == 12 and all(len({role(phase, yz) for yz in SLICE}) == 12 for phase in "ABCD"))
    check("A both Hamiltonian paths cover the slice exactly", set(PATH_A) == set(PATH_B) == set(SLICE) and len(set(PATH_A)) == 12)
    check("A every path step is transverse nearest-neighbour", all(sum(abs(a-b) for a,b in zip(left,right)) == 1 for path in (PATH_A,PATH_B) for left,right in zip(path,path[1:])))
    check("A finite base table has forty-eight phase rules", len(BASE_RULES) == 48)
    two_phase_outputs: dict[tuple[tuple[Coord, str], ...], set[str]] = {}
    for rule in phase_rules("A", "B", PATH_B) + phase_rules("B", "A", PATH_A):
        for variant in variants(rule):
            two_phase_outputs.setdefault(variant.required, set()).add(variant.output)
    check("A two-phase reverse sweep control has a rotated output alias", any(len(values) > 1 for values in two_phase_outputs.values()))
    check("A mixed rotated table is single-valued", not RULE_CONFLICTS)
    check("A indexed rule table retains every unique signature", len(RULE_TABLE) == len(RULE_OUTPUTS))


def cage_and_local_geometry() -> None:
    section("B - Launch cage and cooperative-copy geometry")
    seed = seed_records()
    launch = site(0, PORT_A)
    open_neighbors = {add(launch, direction) for direction in DIRECTIONS if add(launch, direction) not in seed}
    check("B initial launcher has exactly one open neighbour", open_neighbors == {site(1, PORT_A)})
    check("B backstop closes the reverse launch", site(-1, PORT_A) in seed)
    check("B four transverse launcher neighbours are in the complete slice", all((0, PORT_A[0]+dy, PORT_A[1]+dz) in seed for dy,dz in ((1,0),(-1,0),(0,1),(0,-1))))
    check("B first launch rule has one parent", len(BASE_RULES[0].required) == 1)
    check("B every cooperative rule has at least two visible parents", all(len(rule.required) >= 2 for index, rule in enumerate(BASE_RULES) if index % 12))
    transitions = (("A", "B", PATH_B), ("B", "C", PATH_A), ("C", "D", PATH_B), ("D", "A", PATH_A))
    cages_hold = True
    for _old_phase, _new_phase, path in transitions:
        for index in range(1, len(path)):
            target = site(1, path[index])
            old_parent = site(0, path[index])
            new_parent = site(1, path[index - 1])
            alternate = site(0, path[index - 1])
            cages_hold &= neighbors(old_parent) & neighbors(new_parent) == {target, alternate}
    check("B every cooperative pair has one open target and one occupied alternate", cages_hold)
    records = seed
    sequence = bounded_sequence(1)
    unique = True
    for target, content in sequence:
        unique &= enabled_assignments(records) == {target: content}
        records = append(records, target, content)
    next_launch = site(1, PORT_B)
    next_open = {add(next_launch, direction) for direction in DIRECTIONS if add(next_launch, direction) not in records}
    check("B one complete sweep has no parasite", unique)
    check("B renewed launcher is again caged to one forward neighbour", next_open == {site(2, PORT_B)})


def multistep_and_covariance() -> None:
    section("C - Autonomous renewal, permanence, and graph covariance")
    layers = 8
    sequence = bounded_sequence(layers + 1)
    records = seed_records()
    history: list[Coord] = []
    declared = sequence[:12 * layers]
    for index, (target, content) in enumerate(declared):
        enabled = enabled_assignments(records)
        check(f"C write {index:02d} is the unique frontier", enabled == {target: content})
        records = append(records, target, content)
        history.append(target)
    check("C eight complete slices append ninety-six records", len(history) == 96)
    check("C every dynamic target is written once", len(history) == len(set(history)))
    check("C no seed/backstop record is overwritten", len(records) == len(seed_records()) + 96)
    check("C frontier autonomously exposes the ninth slice", enabled_assignments(records) == {sequence[96][0]: sequence[96][1]})
    phases = ("A", "B", "C", "D")
    check("C every completed layer is a full role-coded slice", all(all(records.get(site(x, yz)) == role(phases[x % 4], yz) for yz in SLICE) for x in range(1, 9)))

    replay = bounded_sequence(3)
    for index, rotation in enumerate(ROTATIONS):
        shift = (9, -7, 5)
        moved = transform_records(seed_records(), rotation, shift)
        moved_sequence = transform_sequence(replay, rotation, shift)
        valid = True
        for target, content in moved_sequence:
            if enabled_assignments(moved) != {target: content}:
                valid = False
                break
            moved = append(moved, target, content)
        check(f"C rotated/translated three-slice replay {index:02d}", valid)


def asynchronous_product_graph() -> None:
    section("D - All reachable asynchronous interleavings")
    layers = 2
    horizon = 12 * layers
    extra = 1
    left_shift = (-20, 0, 0)
    right_shift = (20, 0, 0)
    rotation = ROTATIONS[7]
    left_seed = transform_records(seed_records(), ROTATIONS[0], left_shift)
    right_seed = transform_records(seed_records(), rotation, right_shift)
    check("D two motifs have disjoint seed support", set(left_seed).isdisjoint(right_seed))
    combined = dict(left_seed)
    combined.update(right_seed)
    left_sequence = transform_sequence(bounded_sequence(layers + extra), ROTATIONS[0], left_shift)
    right_sequence = transform_sequence(bounded_sequence(layers + extra), rotation, right_shift)
    seen, edges, mismatches, deadlocks, terminals = exhaustive_product(
        combined, (left_sequence, right_sequence), horizon
    )
    expected_states = (horizon + 1) ** 2
    expected_edges = 2 * horizon * (horizon + 1)
    check("D full product graph has exact reachable-state count", seen == expected_states, f"seen={seen}")
    check("D full product graph has exact edge count", edges == expected_edges, f"edges={edges}")
    check("D every reachable enabled set equals the declared fronts", mismatches == 0)
    check("D no reachable nonterminal deadlocks", deadlocks == 0)
    check("D every asynchronous order joins one bounded terminal", len(terminals) == 1)
    terminal = dict(next(iter(terminals)))
    check("D bounded terminal contains both complete two-slice prefixes", all(all(target in terminal for target, _ in sequence[:horizon]) for sequence in (left_sequence, right_sequence)))
    check("D terminal exposes exactly the two next autonomous starts", enabled_assignments(terminal) == {left_sequence[horizon][0]: left_sequence[horizon][1], right_sequence[horizon][0]: right_sequence[horizon][1]})


def documentation_gate() -> None:
    section("E - Bounded result and residual")
    note = normalized(NOTE)
    required = (
        "autonomous_frame_cage_rail_renewal",
        "official_seed_to_rail_nucleation",
        "finite autonomous append-only local motif",
        "all 24 proper-cubic",
        "no pre-laid guide rail",
        "not w_c",
        "support placement",
        "openness reservation",
        "phase distribution",
        "no live axiom edit",
        "no audit verdict",
    )
    for phrase in required:
        check(f"E note contains: {phrase}", phrase in note)
    check("E note reports exact runner count", "pass=169 fail=0" in note)


def main() -> int:
    source_and_table_contract()
    cage_and_local_geometry()
    multistep_and_covariance()
    asynchronous_product_graph()
    documentation_gate()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: AUTONOMOUS_FRAME_CAGE_RAIL_RENEWAL is constructed under "
        "mixed cubic rules; OFFICIAL_SEED_TO_RAIL_NUCLEATION and the larger "
        "W_C openness/phase/support integration remain open"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
