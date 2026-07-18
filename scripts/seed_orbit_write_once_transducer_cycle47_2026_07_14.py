#!/usr/bin/env python3
"""Cycle 47 rejected write-once seed-orbit transducer candidate.

This runner keeps the attempted scalar-label rule table only long enough to
execute its exact counterexample.  It proves rotated-rule parasitic writes, a
legal non-goal deadlock, the old search helper's dead-end masking, and the
one-parent openness-launch ambiguity.  Passing this runner certifies the
bounded rejection and corrected acceptance contract, not a working W_C.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import permutations, product
import inspect
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "SEED_ORBIT_WRITE_ONCE_TRANSDUCER_CYCLE47_NOTE_2026-07-14.md"
CYCLE41 = REVIEW / "COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md"
CYCLE43 = REVIEW / "STRICT_NN_RECORD_LAW_COMPILER_CYCLE43_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
Rotation = tuple[Coord, Coord, Coord]

DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
HEADER_PATTERN = ("H1", "H0", "H1", "H1", "H0", "H1")
BUILDER_ONE_PATTERN = ("B1", "B0", "B1", "B1", "B0", "B1")
BUILDER_TWO_PATTERN = ("D1", "D0", "D1", "D1", "D0", "D1")

# Cross-section coordinates are (e,u).  The two interior ports alternate.
SLICE: tuple[tuple[int, int], ...] = tuple(product(range(4), range(3)))
PORT_A = (1, 1)
PORT_B = (2, 1)
PATH_P: tuple[tuple[int, int], ...] = (
    (1, 1),
    (1, 2),
    (0, 2),
    (0, 1),
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 0),
    (3, 1),
    (3, 2),
    (2, 2),
    (2, 1),
)
PATH_Q = tuple(reversed(PATH_P))


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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def subtract(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def scale(factor: int, vector: Coord) -> Coord:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


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


@dataclass(frozen=True)
class Program:
    trigger: Coord
    forward: Coord
    transverse: Coord

    @property
    def normal(self) -> Coord:
        return cross(self.forward, self.transverse)

    @property
    def data(self) -> tuple[Coord, Coord, Coord]:
        return tuple(add(self.trigger, scale(step, self.forward)) for step in (1, 2, 3))  # type: ignore[return-value]


def header_sites(program: Program) -> tuple[Coord, ...]:
    d, e, u = program.forward, program.transverse, program.normal
    offsets = (e, scale(2, e), scale(3, e), u, scale(2, u), add(d, add(e, u)))
    return tuple(add(program.trigger, offset) for offset in offsets)


def seed_records(program: Program) -> dict[Coord, str]:
    records = dict(zip(header_sites(program), HEADER_PATTERN))
    records[program.trigger] = "Z0"
    return records


def certificate_site(program: Program) -> Coord:
    return add(program.trigger, scale(-1, program.transverse))


def shifted_header_sites(program: Program, step: int) -> tuple[Coord, ...]:
    return tuple(add(site, scale(step, program.forward)) for site in header_sites(program))


def official_block_support(program: Program) -> frozenset[Coord]:
    support = set(seed_records(program)) | set(program.data) | {certificate_site(program)}
    for stage in (1, 2, 3):
        support.update(shifted_header_sites(program, stage))
    return frozenset(support)


def site(x: int, yz: tuple[int, int]) -> Coord:
    return (x, yz[0], yz[1])


def local_signature(records: dict[Coord, str], target: Coord) -> tuple[tuple[Coord, str], ...]:
    return tuple(
        sorted(
            (direction, records[add(target, direction)])
            for direction in DIRECTIONS
            if add(target, direction) in records
        )
    )


def rotate_signature(signature: tuple[tuple[Coord, str], ...], rotation: Rotation) -> tuple[tuple[Coord, str], ...]:
    return tuple(sorted((matvec(rotation, offset), content) for offset, content in signature))


@dataclass(frozen=True)
class Rule:
    name: str
    required: tuple[tuple[Coord, str], ...]
    output: str
    exact: bool = False


def rule_variants(rule: Rule) -> tuple[Rule, ...]:
    variants = {
        (rotate_signature(rule.required, rotation), rule.output, rule.exact)
        for rotation in ROTATIONS
    }
    return tuple(Rule(rule.name, required, output, exact) for required, output, exact in sorted(variants))


def matches(rule: Rule, records: dict[Coord, str], target: Coord) -> bool:
    if target in records:
        return False
    signature = local_signature(records, target)
    required = set(rule.required)
    if not required.issubset(signature):
        return False
    return not rule.exact or len(signature) == len(required)


def relative_required(target: Coord, parents: tuple[tuple[Coord, str], ...]) -> tuple[tuple[Coord, str], ...]:
    return tuple(sorted((subtract(parent, target), content) for parent, content in parents))


def initial_slice_contents() -> dict[tuple[int, int], str]:
    return {
        (0, 0): "Z0",
        (1, 0): "H1",
        (2, 0): "H0",
        (3, 0): "H1",
        (0, 1): "H1",
        (0, 2): "H0",
        (1, 1): "DONE_A",
        (1, 2): "I1",
        (2, 1): "I1",
        (2, 2): "I2",
        (3, 1): "I3",
        (3, 2): "I4",
    }


def phase_contents(path: tuple[tuple[int, int], ...], prefix: str, final: str) -> dict[tuple[int, int], str]:
    answer = {position: f"{prefix}{index}" for index, position in enumerate(path[:-1])}
    answer[path[-1]] = final
    return answer


P_CONTENT = phase_contents(PATH_P, "P", "DONE_B")
Q_CONTENT = phase_contents(PATH_Q, "Q", "DONE_A")


def make_rules() -> tuple[Rule, ...]:
    rules: list[Rule] = []
    j = site(0, PORT_A)
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    seed = seed_records(base)

    rules.append(
        Rule(
            "BOOT_DONE_A",
            relative_required(j, tuple((parent, seed[parent]) for parent in ((1, 1, 1), (0, 0, 1), (0, 1, 0)))),
            "DONE_A",
            exact=True,
        )
    )
    rules.append(
        Rule(
            "BOOT_I1",
            relative_required(site(0, (1, 2)), ((j, "DONE_A"), (site(0, (0, 2)), "H0"))),
            "I1",
            exact=True,
        )
    )
    rules.append(
        Rule(
            "BOOT_I2",
            relative_required(site(0, (2, 2)), ((site(0, (1, 2)), "I1"), (site(0, (2, 1)), "I1"))),
            "I2",
            exact=True,
        )
    )
    rules.append(
        Rule(
            "BOOT_I3",
            relative_required(site(0, (3, 1)), ((site(0, (2, 1)), "I1"), (site(0, (3, 0)), "H1"))),
            "I3",
            exact=True,
        )
    )
    rules.append(
        Rule(
            "BOOT_I4",
            relative_required(site(0, (3, 2)), ((site(0, (2, 2)), "I2"), (site(0, (3, 1)), "I3"))),
            "I4",
            exact=True,
        )
    )

    # A single DONE port has five occupied neighbours; its only open neighbor
    # receives the first tile of the next slice.
    rules.append(Rule("P_SEED", (((1, 0, 0), "DONE_A"),), "P0", exact=True))
    rules.append(Rule("Q_SEED", (((1, 0, 0), "DONE_B"),), "Q0", exact=True))

    initial = initial_slice_contents()
    for index in range(1, len(PATH_P)):
        target = site(-1, PATH_P[index])
        previous = site(-1, PATH_P[index - 1])
        old_parent = site(0, PATH_P[index])
        output = P_CONTENT[PATH_P[index]]
        rules.append(
            Rule(
                f"P_INITIAL_{index:02d}",
                relative_required(target, ((previous, P_CONTENT[PATH_P[index - 1]]), (old_parent, initial[PATH_P[index]]))),
                output,
            )
        )

    # Recurrent P slice reads the prior Q slice.
    for index in range(1, len(PATH_P)):
        target = site(-1, PATH_P[index])
        previous = site(-1, PATH_P[index - 1])
        old_parent = site(0, PATH_P[index])
        output = P_CONTENT[PATH_P[index]]
        rules.append(
            Rule(
                f"P_RENEW_{index:02d}",
                relative_required(target, ((previous, P_CONTENT[PATH_P[index - 1]]), (old_parent, Q_CONTENT[PATH_P[index]]))),
                output,
            )
        )

    # Q is the reverse Hamiltonian pass over a P slice.
    for index in range(1, len(PATH_Q)):
        target = site(-1, PATH_Q[index])
        previous = site(-1, PATH_Q[index - 1])
        old_parent = site(0, PATH_Q[index])
        output = Q_CONTENT[PATH_Q[index]]
        rules.append(
            Rule(
                f"Q_RENEW_{index:02d}",
                relative_required(target, ((previous, Q_CONTENT[PATH_Q[index - 1]]), (old_parent, P_CONTENT[PATH_Q[index]]))),
                output,
            )
        )

    expanded = tuple(variant for rule in rules for variant in rule_variants(rule))
    return expanded


RULES = make_rules()


def enabled_assignments(records: dict[Coord, str]) -> dict[Coord, str]:
    candidates = {
        add(recorded, direction)
        for recorded in records
        for direction in DIRECTIONS
        if add(recorded, direction) not in records
    }
    enabled: dict[Coord, set[str]] = {}
    for target in candidates:
        for rule in RULES:
            if matches(rule, records, target):
                enabled.setdefault(target, set()).add(rule.output)
    conflicts = {target: outputs for target, outputs in enabled.items() if len(outputs) != 1}
    if conflicts:
        raise RuntimeError(f"transition conflict: {conflicts}")
    return {target: next(iter(outputs)) for target, outputs in enabled.items()}


def apply(records: dict[Coord, str], target: Coord, content: str) -> dict[Coord, str]:
    if target in records:
        raise ValueError(f"record overwrite at {target}")
    answer = dict(records)
    answer[target] = content
    return answer


def state_key(records: dict[Coord, str]) -> tuple[tuple[Coord, str], ...]:
    return tuple(sorted(records.items()))


def first_slice_goal(records: dict[Coord, str]) -> bool:
    return records.get(site(-1, PORT_B)) == "DONE_B"


def exhaustive_first_slice(seed: dict[Coord, str], max_states: int = 10000) -> tuple[set[tuple[tuple[Coord, str], ...]], int]:
    queue = deque((seed,))
    seen = {state_key(seed)}
    goals: set[tuple[tuple[Coord, str], ...]] = set()
    transitions = 0
    while queue:
        records = queue.popleft()
        if first_slice_goal(records):
            goals.add(state_key(records))
            continue
        enabled = enabled_assignments(records)
        for target, content in enabled.items():
            transitions += 1
            future = apply(records, target, content)
            key = state_key(future)
            if key not in seen:
                seen.add(key)
                queue.append(future)
        if len(seen) > max_states:
            raise RuntimeError("first-slice state exploration exceeded bound")
    return goals, transitions


def exhaustive_diagnostics(
    seed: dict[Coord, str], max_states: int = 50000
) -> tuple[
    set[tuple[tuple[Coord, str], ...]],
    set[tuple[tuple[Coord, str], ...]],
    int,
]:
    """Repeat the old search while retaining its omitted non-goal dead ends."""

    queue = deque((seed,))
    seen = {state_key(seed)}
    goals: set[tuple[tuple[Coord, str], ...]] = set()
    dead_ends: set[tuple[tuple[Coord, str], ...]] = set()
    transitions = 0
    while queue:
        records = queue.popleft()
        if first_slice_goal(records):
            goals.add(state_key(records))
            continue
        enabled = enabled_assignments(records)
        if not enabled:
            dead_ends.add(state_key(records))
            continue
        for target, content in enabled.items():
            transitions += 1
            future = apply(records, target, content)
            key = state_key(future)
            if key not in seen:
                seen.add(key)
                queue.append(future)
        if len(seen) > max_states:
            raise RuntimeError("diagnostic state exploration exceeded bound")
    return goals, dead_ends, transitions


def deterministic_run(seed: dict[Coord, str], completed_slices: int) -> tuple[dict[Coord, str], tuple[tuple[Coord, str], ...]]:
    records = dict(seed)
    history: list[tuple[Coord, str]] = []
    done_count = 0
    last_done_sites: set[Coord] = set()
    for _ in range(10000):
        current_done = {
            position
            for position, content in records.items()
            if content in {"DONE_A", "DONE_B"} and position[0] < 0
        }
        if len(current_done) >= completed_slices:
            return records, tuple(history)
        enabled = enabled_assignments(records)
        if not enabled:
            return records, tuple(history)
        target = sorted(enabled)[0]
        content = enabled[target]
        records = apply(records, target, content)
        history.append((target, content))
        last_done_sites = current_done
        done_count = len(last_done_sites)
    raise RuntimeError(f"deterministic run did not finish: {done_count}")


def transform_records(records: dict[Coord, str], rotation: Rotation, shift: Coord = (0, 0, 0)) -> dict[Coord, str]:
    return {add(matvec(rotation, position), shift): content for position, content in records.items()}


def source_contract() -> None:
    section("A - Source, authority, and exact target boundary")
    for path in (NOTE, CYCLE41, CYCLE43, AXIOMS):
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    check("A note is authority-free", "authority: none" in note)
    check("A note authorizes no foundation edit", "no live foundation or audit edit is authorized" in note)
    check("A state remains record-only", "a state is a configuration of records" in axioms)
    check("A Record remains one-per-site and permanent", "site never carries more than one record" in axioms and "records are permanent" in axioms)
    check("A Cycle 47 keeps the exact Cycle-41 target", "event_readiness_local_causal_domain" in note)
    check(
        "A Cycle 47 names the corrected residual transducer",
        "frame_retaining_open_quartet_phase_transducer" in note,
    )


def geometry_and_rule_table() -> None:
    section("B - Bootstrap geometry and finite covariant transition table")
    check("B proper cubic rotation group has 24 elements", len(ROTATIONS) == 24)
    check("B cross-section has twelve sites", len(SLICE) == 12)
    check("B Hamiltonian phase visits every cross-section site once", len(PATH_P) == len(set(PATH_P)) == 12 and set(PATH_P) == set(SLICE))
    check("B alternating ports are distinct interior sites", PORT_A != PORT_B and all(0 < y < 3 and 0 < z < 2 for y, z in (PORT_A, PORT_B)))
    check("B every Hamiltonian step is nearest-neighbor", all(sum(abs(a - b) for a, b in zip(left, right)) == 1 for left, right in zip(PATH_P, PATH_P[1:])))
    check("B transition table is finite", 100 < len(RULES) < 5000, f"rotated_rules={len(RULES)}")

    # Covariant-orbit consistency: one exact local signature never requests
    # two different record contents.
    outputs: dict[tuple[bool, tuple[tuple[Coord, str], ...]], set[str]] = {}
    for rule in RULES:
        outputs.setdefault((rule.exact, rule.required), set()).add(rule.output)
    check(
        "B rejected table contains a rotated-signature output conflict",
        any(len(values) > 1 for values in outputs.values()),
    )

    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    seed = seed_records(base)
    bootstrap_new = {site(0, yz) for yz in SLICE} - set(seed)
    check("B bootstrap needs exactly six safe certificate sites", len(bootstrap_new) == 6)
    check("B bootstrap certificate sites avoid official support", bootstrap_new.isdisjoint(official_block_support(base)))


def rotation_equivalent(
    left: tuple[tuple[Coord, str], ...],
    right: tuple[tuple[Coord, str], ...],
) -> bool:
    return any(rotate_signature(left, rotation) == right for rotation in ROTATIONS)


def rejected_candidate_counterexample() -> None:
    section("C - Executable rejection of the scalar-label candidate")
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    seed = seed_records(base)

    # The two I1 arms are scalar-identical.  Hence the intended first P turn
    # and the terminal-blocking turn have proper-cubic-equivalent signatures.
    p_alias_state = {
        (-1, 1, 1): "P0",
        (0, 1, 2): "I1",
        (0, 2, 1): "I1",
    }
    intended_p1 = local_signature(p_alias_state, (-1, 1, 2))
    parasitic_p1 = local_signature(p_alias_state, (-1, 2, 1))
    check("C intended P1 signature has two parents", len(intended_p1) == 2)
    check("C parasitic P1 signature has two parents", len(parasitic_p1) == 2)
    check(
        "C intended and terminal-blocking P1 signatures are proper-cubic aliases",
        rotation_equivalent(intended_p1, parasitic_p1),
    )

    i3_alias_state = {
        (0, 1, 2): "I1",
        (0, 2, 1): "I1",
        (0, 3, 0): "H1",
        (1, 1, 1): "H1",
    }
    intended_i3 = local_signature(i3_alias_state, (0, 3, 1))
    parasitic_i3_a = local_signature(i3_alias_state, (1, 1, 2))
    parasitic_i3_b = local_signature(i3_alias_state, (1, 2, 1))
    check("C intended I3 signature has two parents", len(intended_i3) == 2)
    check(
        "C first parasitic I3 signature is a proper-cubic alias",
        rotation_equivalent(intended_i3, parasitic_i3_a),
    )
    check(
        "C second parasitic I3 signature is a proper-cubic alias",
        rotation_equivalent(intended_i3, parasitic_i3_b),
    )

    dead, history = deterministic_run(seed, 1)
    check("C sorted legal schedule performs exactly twenty writes", len(history) == 20)
    check("C dead schedule contains exactly twenty-seven records", len(dead) == 27)
    check("C sorted schedule does not complete the first slice", not first_slice_goal(dead))
    check("C sorted schedule is a non-goal deadlock", not enabled_assignments(dead))
    check("C parasitic P1 occupies the intended terminal", dead.get((-1, 2, 1)) == "P1")
    check("C first parasitic I3 is permanent", dead.get((1, 1, 2)) == "I3")
    check("C second parasitic I3 is permanent", dead.get((1, 2, 1)) == "I3")
    check("C parasitic I4 is disabled rather than repairing the dead state", (1, 2, 2) not in dead)

    old_source = inspect.getsource(exhaustive_first_slice)
    check("C concrete dead state is a non-goal terminal state", not first_slice_goal(dead) and not enabled_assignments(dead))
    check("C old exhaustive helper has no dead-end collection", "dead_ends" not in old_source)
    check("C old exhaustive helper returns goals and transition count only", "return goals, transitions" in old_source)
    check("C corrected diagnostic API includes an explicit dead-end set", "dead_ends.add" in inspect.getsource(exhaustive_diagnostics))


def one_parent_openness_alias() -> None:
    section("D - One-parent openness sidecar ambiguity")
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    seed = seed_records(base)
    targets = {
        "a": (1, 0, 0),
        "q": (0, -1, 0),
        "back": (-1, 0, 0),
        "down": (0, 0, -1),
    }
    signatures = {name: local_signature(seed, target) for name, target in targets.items()}
    check("D four Z0-adjacent targets are initially open", all(target not in seed for target in targets.values()))
    check("D each launch target sees exactly one Z0 parent", all(signature == ((subtract((0, 0, 0), targets[name]), "Z0"),) for name, signature in signatures.items()))
    reference = signatures["down"]
    check("D all four one-parent signatures are rotation-equivalent", all(rotation_equivalent(reference, signature) for signature in signatures.values()))
    official = {certificate_site(base), *base.data}
    check("D ambiguous launch set intersects future official support", {targets["a"], targets["q"]} <= official)
    check("D exact matching cannot distinguish the four one-parent launches", all(len(signature) == 1 for signature in signatures.values()))


def confluence_and_renewal() -> tuple[dict[Coord, str], tuple[tuple[Coord, str], ...]]:
    section("C - Exhaustive write-once confluence and indefinite slice renewal")
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    seed = seed_records(base)
    goals, transitions = exhaustive_first_slice(seed)
    check("C exhaustive asynchronous search reaches a first-slice goal", bool(goals), f"transitions={transitions}")
    check("C every asynchronous order has one identical first-slice state", len(goals) == 1, f"goals={len(goals)}")
    goal = dict(next(iter(goals)))
    expected_slice = {site(-1, yz): content for yz, content in P_CONTENT.items()}
    check("C first completed P slice has the exact twelve-tile dictionary", all(goal.get(position) == content for position, content in expected_slice.items()))
    check("C bootstrap closes the complete 4x3 initial address slice", all(site(0, yz) in goal for yz in SLICE))

    records, history = deterministic_run(seed, 10)
    check("C ten renewed slices complete", sum(content in {"DONE_A", "DONE_B"} and position[0] < 0 for position, content in records.items()) == 10)
    check("C every transition appends one previously absent record", len(history) == len(set(position for position, _ in history)))
    check("C renewal consumes exactly twelve new records per slice plus six bootstrap records", len(records) == len(seed) + 6 + 12 * 10)
    check("C alternating DONE ports advance one NN layer per slice", all(records.get(site(-layer, PORT_B if layer % 2 else PORT_A)) == ("DONE_B" if layer % 2 else "DONE_A") for layer in range(1, 11)))
    check("C all transducer records stay on or behind the seed plane", all(position[0] <= 0 for position, _ in history))
    check("C no transducer record touches official block support", set(position for position, _ in history).isdisjoint(official_block_support(base)))
    return records, history


def covariance_replay(history: tuple[tuple[Coord, str], ...]) -> None:
    section("D - Translation and proper-cubic covariance replay")
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    seed = seed_records(base)
    for index, rotation in enumerate(ROTATIONS):
        shift = (11, -7, 5)
        records = transform_records(seed, rotation, shift)
        valid = True
        for target, content in history:
            moved_target = add(matvec(rotation, target), shift)
            enabled = enabled_assignments(records)
            if enabled.get(moved_target) != content:
                valid = False
                break
            records = apply(records, moved_target, content)
        check(f"D rotated/translated history {index:02d} remains executable", valid)


def positive_and_negative_probe_controls() -> None:
    section("E - Positive seed probes and the remaining open-quartet case")
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    seed = seed_records(base)
    complete, _ = deterministic_run(seed, 1)
    check("E exact seed produces the first DONE_B certificate", first_slice_goal(complete))

    for index, removed in enumerate(sorted(seed)):
        defective = dict(seed)
        defective.pop(removed)
        result, _ = deterministic_run(defective, 1)
        check(f"E deleting positive seed fact {index:02d} blocks DONE_B", not first_slice_goal(result))

    probes = (certificate_site(base),) + base.data
    unchanged = True
    for probe in probes:
        occupied = dict(seed)
        occupied[probe] = "BLOCK"
        result, _ = deterministic_run(occupied, 1)
        unchanged &= first_slice_goal(result)
    check("E present implementation does not inspect q,a,b,c openness", unchanged)
    check("E remaining case has exactly four open probes", len(probes) == len(set(probes)) == 4)
    check("E open probes are all official future sites", set(probes) <= official_block_support(base))
    check("E no probe can itself hold a provisional certificate", all(probe not in complete or probe in seed for probe in probes))


def documentation_gate() -> None:
    section("E - Bounded rejection, acceptance contract, and N1-N8")
    note = normalized(NOTE)
    required = (
        "current construction is rejected",
        "frame_retaining_open_quartet_phase_transducer",
        "not a no-go against a completed w_c",
        "no live axiom edit",
        "single-front",
        "frame_retention",
        "caged_targets",
        "open_q/a/b/c",
        "reservation",
        "phase_distribution",
        "merge_finalization",
        "confluence",
        "support_avoidance",
        "renewal_rebinding",
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
    check("E N1 uses no prior foreclosure marker", "| ruled out by prior |" not in note)
    check("E N2 collapses to one transducer", "collapsed residual set: {w_c}" in note)
    check("E N3 resolves hidden-condition scan", "unresolved hidden conditions: 0" in note)
    check("E N4 drops mismatched prior evidence", "drop as negative evidence" in note)
    check("E N5 leaves the full transducer open", "complete w_c | not tested / open" in note)
    check("E N6 keeps three positive closure paths", all(route in note for route in ("sidecar probe loop", "delayed official write", "reversible carrier probe")))
    check("E N7 demotes any impossibility claim", "defeats any impossibility claim" in note)
    check("E N8 carries forward Cycle 14, 34, 43", all(f"cycle {number}" in note for number in (14, 34, 43)))


def main() -> int:
    source_contract()
    geometry_and_rule_table()
    rejected_candidate_counterexample()
    one_parent_openness_alias()
    documentation_gate()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: the displayed scalar-label table is rejected by rotated "
        "cross-fire and a legal deadlock; frame-coded/caged constructions "
        "remain open under FRAME_RETAINING_OPEN_QUARTET_PHASE_TRANSDUCER"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
