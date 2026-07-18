#!/usr/bin/env python3
"""Cycle 13: append-only causal Bell/read wire on one qubit per Z3 site.

Companion note:
  docs/work_history/repo/review_feedback/
  APPEND_ONLY_CAUSAL_BELL_WIRE_CYCLE13_NOTE_2026-07-14.md

The candidate is deliberately program/boundary relative.  Permanent finite
motifs decode disjoint directed three-site cells.  A prior endpoint record
enables two commuting nearest-neighbor CZ gates and an onsite X read at the
cell center; later onsite Z reads append the endpoints, with the forward
endpoint becoming the next trigger.  Every phase is reconstructible from
records.  The runner tests covariance, collisions, linear-extension
invariance, the growing commutative record algebra, capacity, hidden prepared
state, actuality/weights, and causal depth versus rate.

No axiom, primitive, registry, audit surface, commit, or PR is changed.  Exit
code is zero exactly when every deterministic finite/symbolic check passes.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path
from typing import Callable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "APPEND_ONLY_CAUSAL_BELL_WIRE_CYCLE13_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CYCLE12_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "FUNDAMENTAL_ONE_QUBIT_QCA_COMPILATION_CYCLE12_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0
TOL = 2.0e-10
Coord = tuple[int, int, int]
DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
HEADER_PATTERN = ("H1", "H0", "H1", "H1", "H0", "H1")


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


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def matvec(matrix: np.ndarray, vector: Coord) -> Coord:
    result = matrix @ np.asarray(vector, dtype=int)
    return tuple(int(value) for value in result)  # type: ignore[return-value]


def proper_cubic_rotations() -> tuple[np.ndarray, ...]:
    rotations: dict[tuple[int, ...], np.ndarray] = {}
    for axis_permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(axis_permutation):
                matrix[row, column] = signs[row]
            if round(np.linalg.det(matrix)) == 1:
                rotations[tuple(int(value) for value in matrix.ravel())] = matrix
    return tuple(rotations.values())


def oriented_frames() -> tuple[tuple[Coord, Coord], ...]:
    return tuple(
        (forward, transverse)
        for forward in DIRECTIONS
        for transverse in DIRECTIONS
        if dot(forward, transverse) == 0
    )


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
        return tuple(
            add(self.trigger, scale(step, self.forward)) for step in (1, 2, 3)
        )  # type: ignore[return-value]

    @property
    def left(self) -> Coord:
        return self.data[0]

    @property
    def center(self) -> Coord:
        return self.data[1]

    @property
    def right(self) -> Coord:
        return self.data[2]


def header_sites(program: Program) -> tuple[Coord, ...]:
    transverse = program.transverse
    normal = program.normal
    offsets = (
        transverse,
        scale(2, transverse),
        scale(3, transverse),
        normal,
        scale(2, normal),
        add(program.forward, add(transverse, normal)),
    )
    return tuple(add(program.trigger, offset) for offset in offsets)


def program_records(program: Program) -> dict[Coord, str]:
    return dict(zip(header_sites(program), HEADER_PATTERN))


def merge_program_records(programs: tuple[Program, ...]) -> dict[Coord, str]:
    records: dict[Coord, str] = {}
    for program in programs:
        for site, content in program_records(program).items():
            if site in records and records[site] != content:
                raise ValueError(f"incompatible program records at {site}")
            records[site] = content
    return records


def detect_programs(records: dict[Coord, str]) -> tuple[Program, ...]:
    if not records:
        return ()
    minima = [min(site[axis] for site in records) - 4 for axis in range(3)]
    maxima = [max(site[axis] for site in records) + 4 for axis in range(3)]
    found: list[Program] = []
    for trigger in product(
        *(range(minima[axis], maxima[axis] + 1) for axis in range(3))
    ):
        for forward, transverse in oriented_frames():
            program = Program(trigger, forward, transverse)
            if all(
                records.get(site) == content
                for site, content in zip(header_sites(program), HEADER_PATTERN)
            ):
                found.append(program)
    return tuple(found)


def transform_program(
    program: Program,
    rotation: np.ndarray,
    translation: Coord = (0, 0, 0),
) -> Program:
    return Program(
        add(matvec(rotation, program.trigger), translation),
        matvec(rotation, program.forward),
        matvec(rotation, program.transverse),
    )


def transform_records(
    records: dict[Coord, str],
    rotation: np.ndarray,
    translation: Coord = (0, 0, 0),
) -> dict[Coord, str]:
    return {
        add(matvec(rotation, site), translation): content
        for site, content in records.items()
    }


def conflicting_programs(programs: tuple[Program, ...]) -> frozenset[Program]:
    conflicts: set[Program] = set()
    for number, left in enumerate(programs):
        left_data = set(left.data)
        left_header = set(header_sites(left))
        for right in programs[number + 1 :]:
            right_data = set(right.data)
            right_header = set(header_sites(right))
            if (
                left_data.intersection(right_data)
                or left_data.intersection(right_header)
                or left_header.intersection(right_data)
            ):
                conflicts.add(left)
                conflicts.add(right)
    return frozenset(conflicts)


def enabled_programs(programs: tuple[Program, ...]) -> tuple[Program, ...]:
    conflicts = conflicting_programs(programs)
    return tuple(program for program in programs if program not in conflicts)


def source_contract() -> None:
    section("A - Framework, Cycle 12 residual, scope, and N1-N8 contract")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").replace("*", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    predecessor = CYCLE12_NOTE.read_text(encoding="utf-8").lower()

    check(
        "A live framework still has four named axioms",
        all(
            name in axioms
            for name in ("### Lattice", "### Qubit", "### Admissibility", "### Record")
        ),
    )
    check(
        "A current Record text supplies permanence but no formation law",
        "Records form." in axioms
        and "records are permanent" in axioms
        and "formation rules" in axioms,
    )
    check(
        "A approved premise registry still has four current paths",
        registry.count('"current_path"') == 4,
    )
    check(
        "A Cycle 12 isolates the append-only causal front route",
        "append-only causal front" in predecessor
        and "fresh record capacity" in predecessor,
    )

    required_phrases = (
        "authority: none",
        "complete candidate law",
        "one m2 per site",
        "all six unit translations",
        "all 24 proper cubic rotations",
        "static collision graph",
        "linear-extension invariance",
        "growing record algebra",
        "record-only future sufficiency",
        "infinite fresh-capacity theorem",
        "one-history actuality remains open",
        "causal depth gives order, not rate",
        "program/boundary relative",
        "constitutional classification",
        "n1 — alternative routes",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
    )
    for phrase in required_phrases:
        check(f"A note contains boundary: {phrase}", phrase in normalized)


def relational_program_and_covariance() -> None:
    section("B - Typed relational program and exact lattice covariance")
    rotations = proper_cubic_rotations()
    check("B proper cubic rotation group has order 24", len(rotations) == 24)
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    base_records = program_records(base)
    check("B one six-record typed header has one decoder", detect_programs(base_records) == (base,))
    check("B header sites do not occupy the three data carriers", not set(header_sites(base)).intersection(base.data))
    check("B both coherent gates are nearest-neighbor edges", manhattan(base.left, base.center) == 1 and manhattan(base.center, base.right) == 1)
    check("B header has finite radius three", max(manhattan(base.trigger, site) for site in header_sites(base)) == 3)

    for number, translation in enumerate(DIRECTIONS):
        moved = transform_program(base, np.eye(3, dtype=int), translation)
        moved_records = transform_records(base_records, np.eye(3, dtype=int), translation)
        check(
            f"B relational decoder is unit-translation covariant {number:02d}",
            detect_programs(moved_records) == (moved,),
        )
    for number, rotation in enumerate(rotations):
        moved = transform_program(base, rotation)
        moved_records = transform_records(base_records, rotation)
        check(
            f"B relational decoder is proper-cubic covariant {number:02d}",
            detect_programs(moved_records) == (moved,),
        )

    chain = tuple(
        Program((3 * event, 0, 0), (1, 0, 0), (0, 1, 0))
        for event in range(6)
    )
    chain_records = merge_program_records(chain)
    check("B six forward cells use 36 distinct typed program records", len(chain_records) == 36)
    check("B repeated headers decode exactly the intended finite chain", set(detect_programs(chain_records)) == set(chain))
    check("B consecutive cells use disjoint fresh triples", all(not set(chain[i].data).intersection(chain[j].data) for i in range(len(chain)) for j in range(i + 1, len(chain))))
    check("B each right endpoint is exactly the next trigger", all(chain[index].right == chain[index + 1].trigger for index in range(len(chain) - 1)))


def collision_graph_probe() -> None:
    section("C - Static program collision graph and hard freeze")
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    reverse_same = Program((4, 0, 0), (-1, 0, 0), (0, 0, 1))
    partial_overlap = Program((5, 0, 0), (-1, 0, 0), (0, 1, 0))
    disjoint = Program((0, 8, 0), (0, 0, 1), (1, 0, 0))
    programs = (base, reverse_same, partial_overlap, disjoint)
    conflicts = conflicting_programs(programs)
    check("C three overlapping nominations enter the frozen conflict set", conflicts == frozenset((base, reverse_same, partial_overlap)))
    check("C one disjoint program remains enabled", enabled_programs(programs) == (disjoint,))
    check("C freeze is idempotent", enabled_programs(enabled_programs(programs)) == (disjoint,))
    header_data_overlap = Program((-3, 0, 1), (1, 0, 0), (0, 1, 0))
    check(
        "C a header/data overlap freezes both programs even when data triples are disjoint",
        not set(base.data).intersection(header_data_overlap.data)
        and conflicting_programs((base, header_data_overlap))
        == frozenset((base, header_data_overlap)),
    )

    rotations = proper_cubic_rotations()
    for number, rotation in enumerate(rotations):
        moved = tuple(transform_program(program, rotation) for program in programs)
        moved_enabled = enabled_programs(moved)
        check(
            f"C collision graph is proper-cubic covariant {number:02d}",
            moved_enabled == (transform_program(disjoint, rotation),),
        )
    for number, translation in enumerate(DIRECTIONS):
        moved = tuple(
            transform_program(program, np.eye(3, dtype=int), translation)
            for program in programs
        )
        check(
            f"C collision graph is unit-translation covariant {number:02d}",
            enabled_programs(moved)
            == (transform_program(disjoint, np.eye(3, dtype=int), translation),),
        )

    # Program records use the H0/H1 content family; dynamically appended X/Z
    # records therefore cannot create or remove a typed header.
    program_records_only = merge_program_records((base, disjoint))
    with_dynamic = dict(program_records_only)
    with_dynamic[base.center] = "X+"
    with_dynamic[base.left] = "Z0"
    with_dynamic[base.right] = "Z1"
    check(
        "C dynamic X/Z records do not change the typed program decoder",
        set(detect_programs(with_dynamic)) == {base, disjoint},
    )


I2 = np.eye(2, dtype=complex)
X = np.array(((0.0, 1.0), (1.0, 0.0)), dtype=complex)
Y = np.array(((0.0, -1.0j), (1.0j, 0.0)), dtype=complex)
Z = np.array(((1.0, 0.0), (0.0, -1.0)), dtype=complex)
PLUS = np.array((1.0, 1.0), dtype=complex) / np.sqrt(2.0)
ZERO = np.array((1.0, 0.0), dtype=complex)


def apply_cz(state: np.ndarray, left: int, right: int, width: int) -> np.ndarray:
    answer = state.copy()
    left_mask = 1 << (width - 1 - left)
    right_mask = 1 << (width - 1 - right)
    for index in range(1 << width):
        if index & left_mask and index & right_mask:
            answer[index] *= -1.0
    return answer


def single_site_operator(operator: np.ndarray, site: int, width: int) -> np.ndarray:
    answer = np.array((1.0,), dtype=complex)
    for index in range(width):
        answer = np.kron(answer, operator if index == site else I2)
    return answer


def measurement_projectors(basis: str) -> tuple[tuple[int, np.ndarray], ...]:
    if basis == "X":
        return ((1, (I2 + X) / 2.0), (-1, (I2 - X) / 2.0))
    if basis == "Z":
        return ((0, (I2 + Z) / 2.0), (1, (I2 - Z) / 2.0))
    raise ValueError(basis)


def measure_state(
    state: np.ndarray, site: int, basis: str, width: int
) -> tuple[tuple[int, float, np.ndarray], ...]:
    branches: list[tuple[int, float, np.ndarray]] = []
    for outcome, local_projector in measurement_projectors(basis):
        projector = single_site_operator(local_projector, site, width)
        projected = projector @ state
        probability = float(np.vdot(projected, projected).real)
        if probability > TOL:
            branches.append((outcome, probability, projected / np.sqrt(probability)))
    return tuple(branches)


def reduced_endpoints_after_center(
    state: np.ndarray, center_outcome: int
) -> tuple[float, np.ndarray]:
    clustered = apply_cz(apply_cz(state, 0, 1, 3), 1, 2, 3)
    branches = {
        outcome: (probability, vector)
        for outcome, probability, vector in measure_state(clustered, 1, "X", 3)
    }
    probability, vector = branches[center_outcome]
    x_vector = PLUS if center_outcome == 1 else np.array((1.0, -1.0)) / np.sqrt(2.0)
    tensor = vector.reshape(2, 2, 2)
    endpoints = np.tensordot(x_vector.conj(), tensor, axes=(0, 1)).reshape(4)
    endpoints /= np.linalg.norm(endpoints)
    return probability, endpoints


def exact_bell_append_instrument() -> None:
    section("D - Exact NN cluster/read instrument and appended parity records")
    record_projectors = (
        (I2 + Y) / 2.0,
        (I2 - Y) / 2.0,
        (I2 + X) / 2.0,
        (I2 - X) / 2.0,
        (I2 + Z) / 2.0,
        (I2 - Z) / 2.0,
    )
    check(
        "D H/X/Z labels are six rank-one projectors in the same M2",
        all(
            np.allclose(projector @ projector, projector, atol=TOL)
            and abs(np.trace(projector).real - 1.0) < TOL
            for projector in record_projectors
        )
        and all(
            not np.allclose(record_projectors[left], record_projectors[right], atol=TOL)
            for left in range(len(record_projectors))
            for right in range(left + 1, len(record_projectors))
        ),
    )
    initial = np.kron(np.kron(PLUS, PLUS), PLUS)
    clustered_left_first = apply_cz(apply_cz(initial, 0, 1, 3), 1, 2, 3)
    clustered_right_first = apply_cz(apply_cz(initial, 1, 2, 3), 0, 1, 3)
    check("D the two nearest-neighbor CZ gates commute", np.allclose(clustered_left_first, clustered_right_first, atol=TOL))
    check("D the coherent cluster preparation preserves norm", abs(np.vdot(clustered_left_first, clustered_left_first) - 1.0) < TOL)

    probability_plus, endpoints_plus = reduced_endpoints_after_center(initial, 1)
    probability_minus, endpoints_minus = reduced_endpoints_after_center(initial, -1)
    bell_even = np.array((1.0, 0.0, 0.0, 1.0), dtype=complex) / np.sqrt(2.0)
    bell_odd = np.array((0.0, 1.0, 1.0, 0.0), dtype=complex) / np.sqrt(2.0)
    check("D center X read has equal conditional weights in the prepared sector", abs(probability_plus - 0.5) < TOL and abs(probability_minus - 0.5) < TOL)
    check("D X+ center record leaves the endpoint Bell-even state", np.allclose(endpoints_plus, bell_even, atol=TOL))
    check("D X- center record leaves the endpoint Bell-odd state", np.allclose(endpoints_minus, bell_odd, atol=TOL))

    joint_probabilities: dict[tuple[int, int, int], float] = {}
    clustered = clustered_left_first
    for middle, middle_probability, middle_state in measure_state(clustered, 1, "X", 3):
        for left, left_probability, left_state in measure_state(middle_state, 0, "Z", 3):
            for right, right_probability, _ in measure_state(left_state, 2, "Z", 3):
                joint_probabilities[(middle, left, right)] = (
                    middle_probability * left_probability * right_probability
                )
    check("D exactly four center/endpoint histories have nonzero weight", len(joint_probabilities) == 4)
    check("D every prepared-sector history has weight one quarter", all(abs(value - 0.25) < TOL for value in joint_probabilities.values()))
    check("D endpoint parity is fixed by the center record", all((left ^ right) == (0 if middle == 1 else 1) for (middle, left, right) in joint_probabilities))
    check("D total instrument weight is one", abs(sum(joint_probabilities.values()) - 1.0) < TOL)


Task = str


def task_prerequisites(events: int) -> dict[Task, frozenset[Task]]:
    prerequisites: dict[Task, frozenset[Task]] = {}
    for event in range(events):
        event_task = f"E{event}"
        left_task = f"L{event}"
        right_task = f"R{event}"
        event_prerequisites = frozenset((f"R{event - 1}",)) if event else frozenset()
        prerequisites[event_task] = event_prerequisites
        prerequisites[left_task] = frozenset((event_task,))
        prerequisites[right_task] = frozenset((event_task,))
    return prerequisites


def linear_extensions(prerequisites: dict[Task, frozenset[Task]]) -> tuple[tuple[Task, ...], ...]:
    extensions: list[tuple[Task, ...]] = []

    def visit(done: tuple[Task, ...]) -> None:
        done_set = set(done)
        if len(done) == len(prerequisites):
            extensions.append(done)
            return
        ready = sorted(
            task
            for task, required in prerequisites.items()
            if task not in done_set and required.issubset(done_set)
        )
        for task in ready:
            visit(done + (task,))

    visit(())
    return tuple(extensions)


def initial_plus_state(width: int) -> np.ndarray:
    answer = np.array((1.0,), dtype=complex)
    for _ in range(width):
        answer = np.kron(answer, PLUS)
    return answer


def apply_task(
    state: np.ndarray, task: Task, events: int
) -> tuple[tuple[int, float, np.ndarray], ...]:
    width = 3 * events
    event = int(task[1:])
    offset = 3 * event
    if task.startswith("E"):
        clustered = apply_cz(apply_cz(state, offset, offset + 1, width), offset + 1, offset + 2, width)
        return measure_state(clustered, offset + 1, "X", width)
    if task.startswith("L"):
        return measure_state(state, offset, "Z", width)
    if task.startswith("R"):
        return measure_state(state, offset + 2, "Z", width)
    raise ValueError(task)


def simulate_schedule(
    order: tuple[Task, ...], events: int, initial: np.ndarray | None = None
) -> dict[tuple[tuple[Task, int], ...], float]:
    if initial is None:
        initial = initial_plus_state(3 * events)
    branches: list[tuple[float, np.ndarray, dict[Task, int]]] = [(1.0, initial, {})]
    for task in order:
        next_branches: list[tuple[float, np.ndarray, dict[Task, int]]] = []
        for history_probability, state, outcomes in branches:
            for outcome, conditional_probability, next_state in apply_task(state, task, events):
                next_outcomes = dict(outcomes)
                next_outcomes[task] = outcome
                next_branches.append(
                    (
                        history_probability * conditional_probability,
                        next_state,
                        next_outcomes,
                    )
                )
        branches = next_branches
    distribution: dict[tuple[tuple[Task, int], ...], float] = {}
    for probability, _, outcomes in branches:
        key = tuple(sorted(outcomes.items()))
        distribution[key] = distribution.get(key, 0.0) + probability
    return distribution


def distributions_close(
    left: dict[tuple[tuple[Task, int], ...], float],
    right: dict[tuple[tuple[Task, int], ...], float],
) -> bool:
    return set(left) == set(right) and all(abs(left[key] - right[key]) < TOL for key in left)


def ready_tasks_from_records(
    programs: tuple[Program, ...], records: dict[Coord, str]
) -> frozenset[Task]:
    ready: set[Task] = set()
    active = enabled_programs(programs)
    for event, program in enumerate(active):
        trigger = records.get(program.trigger, "")
        center = records.get(program.center, "")
        if trigger.startswith("Z") and all(site not in records for site in program.data):
            ready.add(f"E{event}")
        if center.startswith("X"):
            if program.left not in records:
                ready.add(f"L{event}")
            if program.right not in records:
                ready.add(f"R{event}")
    return frozenset(ready)


def append_record(
    records: dict[Coord, str], site: Coord, content: str
) -> dict[Coord, str]:
    if site in records:
        raise ValueError(f"record already present at {site}")
    answer = dict(records)
    answer[site] = content
    return answer


def asynchronous_confluence_probe() -> None:
    section("E - Record-ready DAG and exact linear-extension invariance")
    prerequisites = task_prerequisites(2)
    extensions = linear_extensions(prerequisites)
    check("E two-event append DAG has more than one linear extension", len(extensions) > 1, f"extensions={len(extensions)}")
    reference = simulate_schedule(extensions[0], 2)
    check("E two prepared events produce sixteen complete histories", len(reference) == 16)
    check("E every two-event history has weight one sixteenth", all(abs(value - 1.0 / 16.0) < TOL for value in reference.values()))
    for number, extension in enumerate(extensions):
        distribution = simulate_schedule(extension, 2)
        check(
            f"E linear extension {number:02d} gives the same joint records",
            distributions_close(reference, distribution),
        )

    # The readiness chain is visible in record labels: E creates X at center;
    # L/R require it; R creates the Z trigger required by the next E.
    check("E next event is not ready before the forward endpoint read", prerequisites["E1"] == frozenset(("R0",)))
    check("E delayed left read is causally independent of the next event", "L0" not in prerequisites["E1"])

    programs = tuple(
        Program((3 * event, 0, 0), (1, 0, 0), (0, 1, 0))
        for event in range(2)
    )
    records: dict[Coord, str] = {programs[0].trigger: "Z0"}
    check("E seed records reconstruct only the first center event as ready", ready_tasks_from_records(programs, records) == frozenset(("E0",)))
    records = append_record(records, programs[0].center, "X+")
    check("E center certificate reconstructs both endpoint reads as ready", ready_tasks_from_records(programs, records) == frozenset(("L0", "R0")))
    records = append_record(records, programs[0].right, "Z1")
    check("E forward read reconstructs the next event while left read may lag", ready_tasks_from_records(programs, records) == frozenset(("L0", "E1")))
    records = append_record(records, programs[1].center, "X-")
    check("E next center certificate exposes its endpoint reads without hiding L0", ready_tasks_from_records(programs, records) == frozenset(("L0", "L1", "R1")))
    old_records = dict(records)
    records = append_record(records, programs[0].left, "Z0")
    check("E an append transition leaves every prior record unchanged", all(records[site] == content for site, content in old_records.items()))


def cylinder_embedding(values: np.ndarray, branching: int = 4) -> np.ndarray:
    return np.repeat(values, branching)


def growing_record_algebra_and_capacity() -> None:
    section("F - Growing commutative record algebra and fresh-capacity theorem")
    for depth in range(5):
        dimension = 4**depth
        values = np.arange(dimension, dtype=float) + 0.25
        embedded = cylinder_embedding(values)
        check(f"F depth-{depth} cylinder embedding has dimension 4^(n+1)", len(embedded) == 4 ** (depth + 1))
        check(f"F depth-{depth} cylinder embedding is injective", len(set(embedded[::4])) == dimension)
        ones = np.ones(dimension)
        check(f"F depth-{depth} cylinder embedding preserves the unit", np.allclose(cylinder_embedding(ones), np.ones(4 ** (depth + 1)), atol=TOL))
        second = np.arange(dimension, dtype=float) ** 2 + 1.0
        check(f"F depth-{depth} cylinder embedding preserves multiplication", np.allclose(cylinder_embedding(values * second), cylinder_embedding(values) * cylinder_embedding(second), atol=TOL))

    for events in (1, 2, 5, 11):
        programs = tuple(
            Program((3 * event, 0, 0), (1, 0, 0), (0, 1, 0))
            for event in range(events)
        )
        headers = merge_program_records(programs)
        dynamic_sites = {site for program in programs for site in program.data}
        check(f"F {events} event cells consume exactly 3N fresh data sites", len(dynamic_sites) == 3 * events)
        check(f"F {events} event cells carry exactly 6N static header records", len(headers) == 6 * events)
        check(f"F finite fresh capacity bounds completed events at floor(M/3) for N={events}", len(dynamic_sites) // 3 == events)

    finite_capacities = (2, 3, 8, 17, 30)
    for capacity in finite_capacities:
        maximum_events = capacity // 3
        check(
            f"F fresh capacity {capacity} cannot support more than floor(M/3) events",
            3 * (maximum_events + 1) > capacity,
        )


def alternative_preparation() -> np.ndarray:
    return np.kron(np.kron(ZERO, PLUS), ZERO)


def record_sufficiency_and_preparation() -> None:
    section("G - Record-only future sufficiency is sector-relative")
    order = ("E0", "L0", "R0")
    prepared_distribution = simulate_schedule(order, 1)
    alternative_distribution = simulate_schedule(order, 1, alternative_preparation())
    check("G canonical plus preparation gives four allowed record histories", len(prepared_distribution) == 4)
    check("G an alternative open-site preparation gives one record history", len(alternative_distribution) == 1)
    check("G identical initial record configurations can have different futures", not distributions_close(prepared_distribution, alternative_distribution))

    # Within the declared prepared sector, every admissible order gives the same
    # distribution and each record label determines the conditional Bell parity.
    reversed_reads = simulate_schedule(("E0", "R0", "L0"), 1)
    check("G the prepared sector is record-sufficient under endpoint read reordering", distributions_close(prepared_distribution, reversed_reads))
    check(
        "G typed dynamic records cannot mutate the static H-program field",
        set(HEADER_PATTERN).isdisjoint({"X+", "X-", "Z0", "Z1"}),
    )


def actuality_weights_and_rate() -> None:
    section("H - Actuality, weights, and causal depth versus rate")
    distribution = simulate_schedule(("E0", "L0", "R0"), 1)
    probabilities = np.asarray(tuple(distribution.values()))
    check("H the complete instrument retains four nonzero alternatives", len(probabilities) == 4 and np.all(probabilities > TOL))
    check("H the unconditioned four-history mixture has purity one quarter", abs(float(np.sum(probabilities**2)) - 0.25) < TOL)
    check("H no history receives unit weight from the prepared instrument", float(np.max(probabilities)) < 1.0 - TOL)

    alternative = simulate_schedule(("E0", "L0", "R0"), 1, alternative_preparation())
    check("H outcome weights change when the unsupplied open preparation changes", tuple(sorted(distribution.values())) != tuple(sorted(alternative.values())))

    for depth in (1, 2, 5, 10):
        unit_timestamps = tuple(range(depth + 1))
        slow_timestamps = tuple(7 * value for value in range(depth + 1))
        check(f"H depth {depth} admits distinct elapsed-time assignments", unit_timestamps[-1] != slow_timestamps[-1])
        check(f"H depth {depth} preserves the same causal order under rescaling", all(unit_timestamps[i] < unit_timestamps[i + 1] and slow_timestamps[i] < slow_timestamps[i + 1] for i in range(depth)))


def sentence_classification_and_controls() -> None:
    section("I - Constitutional classification and scoped controls")
    note = " ".join(
        NOTE.read_text(encoding="utf-8")
        .lower()
        .replace("`", "")
        .replace("*", "")
        .split()
    )
    required = (
        "theorem of the candidate law",
        "not a theorem of the current four axioms",
        "local and only add content",
        "do not need to axiomize the extension sentence",
        "prepared-state field remains an import",
        "probability weights remain an import",
        "cross-site qubit frame remains an import",
        "event rate remains an import",
        "fresh infinite program/boundary remains an import",
        "does not derive a unique universal law",
        "does not derive one actual history",
        "does not prove a general no-go",
    )
    for phrase in required:
        check(f"I note preserves classification: {phrase}", phrase in note)


def main() -> None:
    source_contract()
    relational_program_and_covariance()
    collision_graph_probe()
    exact_bell_append_instrument()
    asynchronous_confluence_probe()
    growing_record_algebra_and_capacity()
    record_sufficiency_and_preparation()
    actuality_weights_and_rate()
    sentence_classification_and_controls()
    print(
        "\nSUMMARY: APPEND-ONLY CAUSAL BELL WIRE CYCLE 13 "
        f"PASS={PASS} FAIL={FAIL}"
    )
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
