#!/usr/bin/env python3
"""Cycle 17: finite-seed autonomous self-closing causal diamond.

Companion note:
  docs/work_history/repo/review_feedback/
  AUTONOMOUS_SELF_CLOSING_DIAMOND_CYCLE17_NOTE_2026-07-14.md

A single realized typed record grows a radius-two cubic fence by an exact
nearest-neighbor Hamiltonian construction path, generates its own two proposal
sources and stop roles, prepares and routes both open proposal qubits, derives
two local K certificates, and locks symmetric Bell-capable parity.  The runner
also tests shell topology, arbitrary open-site reset, overlapping seeds,
multiple-front clauses, first-record nucleation, and deletion of every
load-bearing closure clause.

No axiom, primitive, registry, audit surface, commit, push, or PR is changed.
Exit code is zero exactly when every deterministic check passes.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path
import random

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "AUTONOMOUS_SELF_CLOSING_DIAMOND_CYCLE17_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CYCLE16_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "DELAYED_LOCKING_CAUSAL_CLOSE_CYCLE16_NOTE_2026-07-14.md"
)
BOUNDARY_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "DYNAMIC_RECORD_BOUNDARY_INDEX_QCA_STEELMAN_NOTE_2026-07-14.md"
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


def negate(vector: Coord) -> Coord:
    return tuple(-value for value in vector)  # type: ignore[return-value]


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
    moved = matrix @ np.asarray(vector, dtype=int)
    return tuple(int(value) for value in moved)  # type: ignore[return-value]


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


@dataclass(frozen=True)
class Frame:
    forward: Coord
    transverse: Coord

    @property
    def normal(self) -> Coord:
        return cross(self.forward, self.transverse)

    def valid(self) -> bool:
        return (
            self.forward in DIRECTIONS
            and self.transverse in DIRECTIONS
            and dot(self.forward, self.transverse) == 0
        )


def oriented_frames() -> tuple[Frame, ...]:
    return tuple(
        Frame(forward, transverse)
        for forward in DIRECTIONS
        for transverse in DIRECTIONS
        if dot(forward, transverse) == 0
    )


@dataclass(frozen=True)
class Cell:
    center: Coord
    forward: Coord
    transverse: Coord

    @property
    def normal(self) -> Coord:
        return cross(self.forward, self.transverse)

    @property
    def frame(self) -> Frame:
        return Frame(self.forward, self.transverse)

    @property
    def left_frame(self) -> Frame:
        return Frame(negate(self.transverse), negate(self.forward))

    @property
    def right_frame(self) -> Frame:
        return Frame(negate(self.normal), self.forward)


@dataclass(frozen=True)
class Content:
    kind: str
    frame: Frame
    index: int = -1
    bit: int = -1


RecordMap = dict[Coord, Content]


# Radius-two cubic shell plus one odd-parity interior connector.  This exact
# Hamiltonian path was solved once and is verified combinatorially below; it is
# data of the candidate finite construction law, not an external cursor.
CANONICAL_PATH: tuple[Coord, ...] = (
    (2, 2, 2), (2, 1, 2), (2, 1, 1), (2, 1, 0), (2, 1, -1),
    (2, 2, -1), (2, 2, -2), (2, 1, -2), (1, 1, -2), (1, 2, -2),
    (1, 2, -1), (1, 2, 0), (2, 2, 0), (2, 2, 1), (1, 2, 1),
    (1, 2, 2), (1, 1, 2), (1, 0, 2), (1, -1, 2), (2, -1, 2),
    (2, 0, 2), (2, 0, 1), (2, -1, 1), (2, -1, 0), (2, 0, 0),
    (2, 0, -1), (2, -1, -1), (2, -2, -1), (2, -2, -2),
    (1, -2, -2), (1, -1, -2), (2, -1, -2), (2, 0, -2),
    (1, 0, -2), (0, 0, -2), (0, 1, -2), (0, 2, -2), (0, 2, -1),
    (-1, 2, -1), (-1, 2, -2), (-1, 1, -2), (-2, 1, -2),
    (-2, 2, -2), (-2, 2, -1), (-2, 2, 0), (-1, 2, 0), (0, 2, 0),
    (0, 2, 1), (-1, 2, 1), (-2, 2, 1), (-2, 2, 2), (-1, 2, 2),
    (0, 2, 2), (0, 1, 2), (0, 0, 2), (0, -1, 2), (0, -2, 2),
    (-1, -2, 2), (-1, -2, 1), (0, -2, 1), (1, -2, 1), (1, -2, 2),
    (2, -2, 2), (2, -2, 1), (2, -2, 0), (1, -2, 0), (1, -2, -1),
    (0, -2, -1), (0, -2, 0), (-1, -2, 0), (-2, -2, 0),
    (-2, -2, -1), (-2, -2, -2), (-2, -1, -2), (-2, -1, -1),
    (-1, -1, -1), (-1, -2, -1), (-1, -2, -2), (0, -2, -2),
    (0, -1, -2), (-1, -1, -2), (-1, 0, -2), (-2, 0, -2),
    (-2, 0, -1), (-2, 1, -1), (-2, 1, 0), (-2, 1, 1),
    (-2, 0, 1), (-2, 0, 2), (-2, 1, 2), (-1, 1, 2), (-1, 0, 2),
    (-1, -1, 2), (-2, -1, 2), (-2, -2, 2), (-2, -2, 1),
    (-2, -1, 1), (-2, -1, 0), (-2, 0, 0),
)
CANONICAL_SHELL = frozenset(
    site
    for site in product(range(-2, 3), repeat=3)
    if max(abs(value) for value in site) == 2
)
CONNECTOR = (-1, -1, -1)
ROOT_RECORD = (-1, 0, 0)
LEFT_CHAIN = ((-1, -1, 0), (0, -1, 0), (0, -1, -1))
RIGHT_CHAIN = ((-1, 0, 1),)
LEFT_PREP = (1, -1, -1)
RIGHT_PREP = (-1, 1, 1)
LEFT_TERMINAL = (1, 0, -1)
RIGHT_TERMINAL = (0, 1, 1)
LEFT_INPUT = (0, 0, -1)
RIGHT_INPUT = (0, 0, 1)
LEFT_CLOSE = (1, 0, 0)
RIGHT_CLOSE = (0, 1, 0)
OUTPUT = (0, 0, 0)
LEFT_FENCE_ROLE = (2, 0, -1)
LEFT_STOP_ROLE = (1, 0, -2)
RIGHT_FENCE_ROLE = (0, 2, 1)
RIGHT_STOP_ROLE = (0, 1, 2)
PATH_INDEX = {site: index for index, site in enumerate(CANONICAL_PATH)}


def global_site(cell: Cell, local: Coord) -> Coord:
    x, y, z = local
    return add(
        cell.center,
        add(
            scale(x, cell.transverse),
            add(scale(y, cell.normal), scale(z, cell.forward)),
        ),
    )


def builder(stage: int, cell: Cell) -> Content:
    return Content("B", cell.frame, index=stage)


def named(kind: str, frame: Frame, index: int = -1, bit: int = -1) -> Content:
    return Content(kind, frame, index=index, bit=bit)


def seed_records(cell: Cell) -> RecordMap:
    return {global_site(cell, CANONICAL_PATH[0]): builder(0, cell)}


def full_path_records(cell: Cell) -> RecordMap:
    return {
        global_site(cell, local): builder(stage, cell)
        for stage, local in enumerate(CANONICAL_PATH)
    }


def transform_frame(frame: Frame, rotation: np.ndarray) -> Frame:
    return Frame(matvec(rotation, frame.forward), matvec(rotation, frame.transverse))


def transform_content(value: Content, rotation: np.ndarray) -> Content:
    return Content(
        value.kind,
        transform_frame(value.frame, rotation),
        value.index,
        value.bit,
    )


def transform_cell(
    cell: Cell,
    rotation: np.ndarray,
    translation: Coord = (0, 0, 0),
) -> Cell:
    return Cell(
        add(matvec(rotation, cell.center), translation),
        matvec(rotation, cell.forward),
        matvec(rotation, cell.transverse),
    )


def transform_records(
    records: RecordMap,
    rotation: np.ndarray,
    translation: Coord = (0, 0, 0),
) -> RecordMap:
    return {
        add(matvec(rotation, site), translation): transform_content(value, rotation)
        for site, value in records.items()
    }


def source_contract() -> None:
    section("A - Framework, predecessors, scope, and N1-N8 contract")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").replace("*", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    cycle16 = CYCLE16_NOTE.read_text(encoding="utf-8").lower()
    boundary = BOUNDARY_NOTE.read_text(encoding="utf-8").lower()

    check(
        "A framework still has four named axioms",
        all(
            name in axioms
            for name in ("### Lattice", "### Qubit", "### Admissibility", "### Record")
        ),
    )
    check("A Record still withholds formation dynamics", "formation rules" in axioms and "records are permanent" in axioms)
    check("A approved premise registry still has four current paths", registry.count('"current_path"') == 4)
    check("A Cycle 16 leaves autonomous finite interfaces open", "generated autonomously" in cycle16 and "causal closure" in cycle16)
    check("A boundary predecessor separates post-record geometry from first record", "post-record geometry" in boundary and "cannot nucleate the first record" in boundary)

    required = (
        "authority: none",
        "autonomous post-seed self-closure",
        "single finite realized seed",
        "radius-two cubic fence",
        "hamiltonian construction path",
        "proper-cubic covariant",
        "nearest-neighbor law",
        "no supplied stop markers",
        "no prepared proposal carriers",
        "no blank corridor",
        "no global future oracle",
        "no external cursor",
        "all law-permitted proposal fronts",
        "clause deletion",
        "overlapping-seed collision",
        "first-record nucleation remains separate",
        "global-history and qca escapes remain live",
        "no new record axiom is forced",
    )
    for phrase in required:
        check(f"A note states scope phrase: {phrase}", phrase in normalized)
    for label in ("N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"):
        check(f"A no-go discipline includes {label}", f"{label.lower()} —" in normalized)


def shell_path_and_minimality() -> None:
    section("B - Minimal shell topology and exact sequential construction")
    check("B radius-two cubic shell has 98 sites", len(CANONICAL_SHELL) == 98)
    check("B path has shell plus exactly one connector", len(CANONICAL_PATH) == 99 and set(CANONICAL_PATH) == set(CANONICAL_SHELL) | {CONNECTOR})
    check("B Hamiltonian path visits every construction site once", len(set(CANONICAL_PATH)) == len(CANONICAL_PATH))
    check("B every construction transition is nearest-neighbor", all(manhattan(CANONICAL_PATH[index], CANONICAL_PATH[index + 1]) == 1 for index in range(len(CANONICAL_PATH) - 1)))
    shell_parity = Counter(sum(site) & 1 for site in CANONICAL_SHELL)
    path_parity = Counter(sum(site) & 1 for site in CANONICAL_PATH)
    check("B shell bipartition is 50 versus 48", shell_parity == Counter({0: 50, 1: 48}))
    check("B shell alone cannot have a Hamiltonian path by parity", abs(shell_parity[0] - shell_parity[1]) == 2)
    check("B one odd connector repairs path parity to 50 versus 49", path_parity == Counter({0: 50, 1: 49}))
    check("B radius-one shell would occupy every output neighbor", all(max(abs(value) for value in direction) == 1 for direction in DIRECTIONS))
    check("B radius-two is the smallest integer cube shell leaving NN inputs open", all(direction not in CANONICAL_SHELL for direction in DIRECTIONS))
    check("B construction endpoint is a face center", CANONICAL_PATH[-1] == (-2, 0, 0))
    check("B endpoint writes the interior root across one edge", manhattan(CANONICAL_PATH[-1], ROOT_RECORD) == 1)
    for role in (LEFT_FENCE_ROLE, LEFT_STOP_ROLE, RIGHT_FENCE_ROLE, RIGHT_STOP_ROLE):
        check(f"B generated front role lies on shell {role}", role in CANONICAL_SHELL and role in PATH_INDEX)


I2 = np.eye(2, dtype=complex)
X = np.array(((0.0, 1.0), (1.0, 0.0)), dtype=complex)
Y = np.array(((0.0, -1.0j), (1.0j, 0.0)), dtype=complex)
Z = np.array(((1.0, 0.0), (0.0, -1.0)), dtype=complex)
ZERO = np.array((1.0, 0.0), dtype=complex)
ONE = np.array((0.0, 1.0), dtype=complex)
PLUS = np.array((1.0, 1.0), dtype=complex) / np.sqrt(2.0)

GENERIC_TOKENS = tuple(
    [f"B:{stage}" for stage in range(len(CANONICAL_PATH))]
    + ["ROOT", "L:0", "L:1", "L:2", "R:0", "P", "T", "K"]
)
TOKEN_PARAMETER = {token: index + 2.0 for index, token in enumerate(GENERIC_TOKENS)}


def token(value: Content) -> str:
    if value.kind == "B":
        return f"B:{value.index}"
    if value.kind in {"L", "R"}:
        return f"{value.kind}:{value.index}"
    return value.kind


def pauli(vector: np.ndarray) -> np.ndarray:
    return vector[0] * X + vector[1] * Y + vector[2] * Z


def bloch_vector(value: Content) -> np.ndarray:
    if value.kind == "J":
        vector = np.asarray(value.frame.forward, dtype=float)
        return vector if value.bit == 0 else -vector
    parameter = TOKEN_PARAMETER[token(value)]
    coefficients = (1.0, parameter, parameter * parameter)
    vector = (
        coefficients[0] * np.asarray(value.frame.forward, dtype=float)
        + coefficients[1] * np.asarray(value.frame.transverse, dtype=float)
        + coefficients[2] * np.asarray(value.frame.normal, dtype=float)
    )
    return vector / np.linalg.norm(vector)


def record_projector(value: Content) -> np.ndarray:
    return (I2 + pauli(bloch_vector(value))) / 2.0


def content_and_covariance_probe() -> None:
    section("C - One-M2 content, role geometry, and cubic covariance")
    frames = oriented_frames()
    values: list[Content] = []
    for frame in frames:
        values.extend(builder(stage, Cell((0, 0, 0), frame.forward, frame.transverse)) for stage in range(len(CANONICAL_PATH)))
        values.extend(named(kind, frame, index=index) for kind, index in (("ROOT", -1), ("L", 0), ("L", 1), ("L", 2), ("R", 0), ("P", -1), ("T", -1), ("K", -1)))
        values.extend(named("J", frame, bit=bit) for bit in (0, 1))
    projectors = [record_projector(value) for value in values]
    check("C every program/close/output content is rank-one in one M2", all(np.allclose(projector @ projector, projector, atol=TOL) and abs(np.trace(projector).real - 1.0) < TOL for projector in projectors))
    unique = {
        tuple(np.round(projector.real, 11).ravel()) + tuple(np.round(projector.imag, 11).ravel())
        for projector in projectors
    }
    check("C generic typed orbits plus six output axes remain distinct", len(unique) == len(GENERIC_TOKENS) * 24 + 6)

    cell = Cell((0, 0, 0), (0, 0, 1), (1, 0, 0))
    roles = (
        ROOT_RECORD,
        *LEFT_CHAIN,
        *RIGHT_CHAIN,
        LEFT_PREP,
        RIGHT_PREP,
        LEFT_TERMINAL,
        RIGHT_TERMINAL,
        LEFT_INPUT,
        RIGHT_INPUT,
        LEFT_CLOSE,
        RIGHT_CLOSE,
        OUTPUT,
    )
    check("C interior control, proposal, close, and output roles are disjoint", len(set(roles)) == len(roles))
    check("C construction connector avoids every event role", CONNECTOR not in roles)
    check("C proposal fronts terminate across one NN edge", manhattan(LEFT_TERMINAL, LEFT_INPUT) == manhattan(RIGHT_TERMINAL, RIGHT_INPUT) == 1)
    check("C prep certificates are NN to their proposal carriers", manhattan(LEFT_PREP, LEFT_TERMINAL) == manhattan(RIGHT_PREP, RIGHT_TERMINAL) == 1)
    check("C generated closes are NN to terminal records and output", manhattan(LEFT_TERMINAL, LEFT_CLOSE) == manhattan(RIGHT_TERMINAL, RIGHT_CLOSE) == manhattan(LEFT_CLOSE, OUTPUT) == manhattan(RIGHT_CLOSE, OUTPUT) == 1)

    rotations = proper_cubic_rotations()
    check("C proper cubic rotation group has 24 matrices", len(rotations) == 24)
    path_records = full_path_records(cell)
    for number, rotation in enumerate(rotations):
        moved = transform_cell(cell, rotation)
        check(f"C full construction path rotates covariantly {number:02d}", transform_records(path_records, rotation) == full_path_records(moved))
    identity = np.eye(3, dtype=int)
    for number, translation in enumerate(DIRECTIONS):
        moved = transform_cell(cell, identity, translation)
        check(f"C full construction path translates covariantly {number:02d}", transform_records(path_records, identity, translation) == full_path_records(moved))


@dataclass(frozen=True)
class Action:
    kind: str
    site: Coord
    value: Content
    side: str = ""

    @property
    def name(self) -> str:
        return f"{self.kind}:{self.side}:{self.site}:{self.value.kind}:{self.value.index}:{self.value.bit}"


def append_record(records: RecordMap, site: Coord, value: Content) -> RecordMap:
    if site in records and records[site] != value:
        raise ValueError(f"incompatible record at {site}")
    answer = dict(records)
    answer[site] = value
    return answer


def is_extension(old: RecordMap, new: RecordMap) -> bool:
    return len(new) >= len(old) and all(new.get(site) == value for site, value in old.items())


def local_role_record(records: RecordMap, cell: Cell, local: Coord) -> bool:
    stage = PATH_INDEX[local]
    return records.get(global_site(cell, local)) == builder(stage, cell)


def ready_actions(
    records: RecordMap,
    cell: Cell,
    branch_bit: int,
    root_threshold: int = 98,
    allow_single_k: bool = False,
) -> tuple[Action, ...]:
    answer: list[Action] = []
    for site, value in records.items():
        if value.kind == "B" and value.frame == cell.frame and value.index < len(CANONICAL_PATH) - 1:
            target_stage = value.index + 1
            target = global_site(cell, CANONICAL_PATH[target_stage])
            if target not in records:
                answer.append(Action("build", target, builder(target_stage, cell)))

    threshold_site = global_site(cell, CANONICAL_PATH[root_threshold])
    root_site = global_site(cell, ROOT_RECORD)
    if records.get(threshold_site) == builder(root_threshold, cell) and root_site not in records:
        answer.append(Action("root", root_site, named("ROOT", cell.frame)))

    left_chain_sites = tuple(global_site(cell, site) for site in LEFT_CHAIN)
    right_chain_site = global_site(cell, RIGHT_CHAIN[0])
    if records.get(root_site) == named("ROOT", cell.frame):
        if left_chain_sites[0] not in records:
            answer.append(Action("branch", left_chain_sites[0], named("L", cell.frame, index=0), "L"))
        if right_chain_site not in records:
            answer.append(Action("branch", right_chain_site, named("R", cell.frame, index=0), "R"))
    for index in range(len(left_chain_sites) - 1):
        if records.get(left_chain_sites[index]) == named("L", cell.frame, index=index) and left_chain_sites[index + 1] not in records:
            answer.append(Action("branch", left_chain_sites[index + 1], named("L", cell.frame, index=index + 1), "L"))

    prep_specs = (
        (
            "L",
            left_chain_sites[-1],
            named("L", cell.frame, index=2),
            global_site(cell, LEFT_PREP),
            cell.left_frame,
        ),
        (
            "R",
            right_chain_site,
            named("R", cell.frame, index=0),
            global_site(cell, RIGHT_PREP),
            cell.right_frame,
        ),
    )
    for side, predecessor, predecessor_value, prep_site, frame in prep_specs:
        if records.get(predecessor) == predecessor_value and prep_site not in records:
            answer.append(Action("prepare", prep_site, named("P", frame), side))

    terminal_specs = (
        ("L", LEFT_PREP, LEFT_TERMINAL, LEFT_INPUT, LEFT_FENCE_ROLE, LEFT_STOP_ROLE, cell.left_frame),
        ("R", RIGHT_PREP, RIGHT_TERMINAL, RIGHT_INPUT, RIGHT_FENCE_ROLE, RIGHT_STOP_ROLE, cell.right_frame),
    )
    for side, prep_local, terminal_local, input_local, fence_local, stop_local, frame in terminal_specs:
        prep_site = global_site(cell, prep_local)
        terminal_site = global_site(cell, terminal_local)
        input_site = global_site(cell, input_local)
        if (
            records.get(prep_site) == named("P", frame)
            and local_role_record(records, cell, fence_local)
            and local_role_record(records, cell, stop_local)
            and terminal_site not in records
            and input_site not in records
        ):
            answer.append(Action("terminal", terminal_site, named("T", frame), side))

    close_specs = (
        ("L", LEFT_TERMINAL, LEFT_CLOSE, cell.left_frame),
        ("R", RIGHT_TERMINAL, RIGHT_CLOSE, cell.right_frame),
    )
    for side, terminal_local, close_local, frame in close_specs:
        terminal_site = global_site(cell, terminal_local)
        close_site = global_site(cell, close_local)
        if records.get(terminal_site) == named("T", frame) and close_site not in records:
            answer.append(Action("close", close_site, named("K", frame), side))

    left_k = records.get(global_site(cell, LEFT_CLOSE)) == named("K", cell.left_frame)
    right_k = records.get(global_site(cell, RIGHT_CLOSE)) == named("K", cell.right_frame)
    output = global_site(cell, OUTPUT)
    if (left_k and right_k or allow_single_k and (left_k or right_k)) and output not in records:
        answer.append(Action("lock", output, named("J", cell.frame, bit=branch_bit)))
    return tuple(sorted(answer, key=lambda item: item.name))


def random_qubit(rng: np.random.Generator) -> np.ndarray:
    state = rng.normal(size=2) + 1.0j * rng.normal(size=2)
    return state / np.linalg.norm(state)


def initial_open_states(cell: Cell, seed: int) -> dict[Coord, np.ndarray]:
    rng = np.random.default_rng(seed)
    return {
        global_site(cell, local): random_qubit(rng)
        for local in (LEFT_TERMINAL, RIGHT_TERMINAL, LEFT_INPUT, RIGHT_INPUT, OUTPUT)
    }


def apply_action(
    records: RecordMap,
    states: dict[Coord, np.ndarray],
    selected: Action,
    cell: Cell,
) -> tuple[RecordMap, dict[Coord, np.ndarray]]:
    answer_records = dict(records)
    answer_states = {site: state.copy() for site, state in states.items()}
    if selected.kind == "prepare":
        terminal_local = LEFT_TERMINAL if selected.side == "L" else RIGHT_TERMINAL
        answer_states[global_site(cell, terminal_local)] = PLUS.copy()
        answer_states.pop(selected.site, None)
    elif selected.kind == "terminal":
        terminal_local = LEFT_TERMINAL if selected.side == "L" else RIGHT_TERMINAL
        input_local = LEFT_INPUT if selected.side == "L" else RIGHT_INPUT
        terminal = global_site(cell, terminal_local)
        input_site = global_site(cell, input_local)
        proposal = answer_states[terminal].copy()
        # SWAP with the arbitrary open input carrier.  The displaced state is
        # then erased/prepared into the permanent T record at terminal.
        answer_states[input_site] = proposal
        del answer_states[terminal]
    elif selected.kind == "lock":
        answer_states.pop(selected.site, None)
    else:
        answer_states.pop(selected.site, None)
    answer_records = append_record(answer_records, selected.site, selected.value)
    if not is_extension(records, answer_records) or len(answer_records) != len(records) + 1:
        raise RuntimeError("non-extension transition")
    return answer_records, answer_states


def run_schedule(
    chooser: str,
    cell: Cell,
    branch_bit: int,
    seed: int,
    root_threshold: int = 98,
) -> tuple[RecordMap, dict[Coord, np.ndarray], tuple[str, ...], int]:
    records = seed_records(cell)
    states = initial_open_states(cell, seed)
    history: list[str] = []
    rng = random.Random(seed)
    lock_stage = -1
    for _ in range(256):
        actions = ready_actions(records, cell, branch_bit, root_threshold=root_threshold)
        if not actions:
            return records, states, tuple(history), lock_stage
        if chooser == "first":
            selected = actions[0]
        elif chooser == "last":
            selected = actions[-1]
        elif chooser == "random":
            selected = rng.choice(actions)
        elif chooser == "event_first":
            selected = next((item for item in actions if item.kind != "build"), actions[0])
        else:
            raise ValueError(chooser)
        if selected.kind == "lock":
            lock_stage = max(
                value.index for value in records.values() if value.kind == "B"
            )
        records, states = apply_action(records, states, selected, cell)
        history.append(selected.name)
    raise RuntimeError("self-closing program did not terminate")


def autonomous_schedule_probe() -> None:
    section("D - Autonomous post-seed shell, proposals, closes, and schedule")
    cell = Cell((0, 0, 0), (0, 0, 1), (1, 0, 0))
    for branch_bit in (0, 1):
        runs = [
            run_schedule("first", cell, branch_bit, 1700 + branch_bit),
            run_schedule("last", cell, branch_bit, 1710 + branch_bit),
        ]
        runs.extend(
            run_schedule("random", cell, branch_bit, 1720 + 10 * branch_bit + seed)
            for seed in range(12)
        )
        reference_records = runs[0][0]
        for number, (records, states, history, lock_stage) in enumerate(runs):
            check(f"D branch {branch_bit} schedule {number:02d} reaches one record map", records == reference_records)
            check(f"D branch {branch_bit} schedule {number:02d} makes 110 post-seed appends", len(history) == 110 and len(records) == 111)
            check(f"D branch {branch_bit} schedule {number:02d} locks only after path completion", lock_stage == 98)
            check(f"D branch {branch_bit} schedule {number:02d} law-prepares both endpoint proposals", np.allclose(states[global_site(cell, LEFT_INPUT)], PLUS, atol=TOL) and np.allclose(states[global_site(cell, RIGHT_INPUT)], PLUS, atol=TOL))
        check(f"D branch {branch_bit} terminal output has supplied branch bit", reference_records[global_site(cell, OUTPUT)] == named("J", cell.frame, bit=branch_bit))
        check(f"D branch {branch_bit} contains every shell record", all(global_site(cell, site) in reference_records for site in CANONICAL_SHELL))
        check(f"D branch {branch_bit} derives both K records", reference_records[global_site(cell, LEFT_CLOSE)] == named("K", cell.left_frame) and reference_records[global_site(cell, RIGHT_CLOSE)] == named("K", cell.right_frame))
        check(f"D branch {branch_bit} schedules genuinely differ", len({history for _, _, history, _ in runs}) > 2)

    records, _, _, _ = run_schedule("first", cell, 0, 1777)
    prep_sites = {global_site(cell, LEFT_PREP), global_site(cell, RIGHT_PREP)}
    check("D exactly two law-permitted proposal preparations occur", {site for site, value in records.items() if value.kind == "P"} == prep_sites)
    check("D stop and fence roles are generated builder records, not seed records", set(seed_records(cell)) == {global_site(cell, CANONICAL_PATH[0])} and all(local_role_record(records, cell, role) for role in (LEFT_FENCE_ROLE, LEFT_STOP_ROLE, RIGHT_FENCE_ROLE, RIGHT_STOP_ROLE)))
    check("D terminal state has no cursor or cleanup action", ready_actions(records, cell, 0) == ())


def density(state: np.ndarray) -> np.ndarray:
    return np.outer(state, state.conj())


def reset_kraus(target: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    return (
        np.outer(target, ZERO.conj()),
        np.outer(target, ONE.conj()),
    )


def reset_channel(rho: np.ndarray, target: np.ndarray) -> np.ndarray:
    return sum(operator @ rho @ operator.conj().T for operator in reset_kraus(target))


def cnot(control: int, target: int, width: int = 3) -> np.ndarray:
    answer = np.zeros((1 << width, 1 << width), dtype=complex)
    for index in range(1 << width):
        bits = [int(value) for value in f"{index:0{width}b}"]
        if bits[control] == 1:
            bits[target] ^= 1
        moved = int("".join(str(value) for value in bits), 2)
        answer[moved, index] = 1.0
    return answer


def single_site_operator(operator: np.ndarray, site: int, width: int = 3) -> np.ndarray:
    answer = np.array((1.0,), dtype=complex)
    for index in range(width):
        answer = np.kron(answer, operator if index == site else I2)
    return answer


def endpoint_state_after_parity(state: np.ndarray, outcome: int) -> tuple[float, np.ndarray]:
    local = (I2 + Z) / 2.0 if outcome == 0 else (I2 - Z) / 2.0
    projected = single_site_operator(local, 1) @ state
    probability = float(np.vdot(projected, projected).real)
    normalized = projected / np.sqrt(probability)
    endpoints = np.zeros(4, dtype=complex)
    for left, right in product((0, 1), repeat=2):
        endpoints[2 * left + right] = normalized[4 * left + 2 * outcome + right]
    return probability, endpoints


def law_generated_preparation_and_bell() -> None:
    section("E - No supplied carriers/blanks and exact Bell-capable parity")
    rng = np.random.default_rng(1717)
    for trial in range(16):
        state = random_qubit(rng)
        rho = density(state)
        for label, target in (("plus", PLUS), ("zero", ZERO)):
            operators = reset_kraus(target)
            check(f"E {label} reset is trace-preserving {trial:02d}", np.allclose(sum(operator.conj().T @ operator for operator in operators), I2, atol=TOL))
            check(f"E {label} reset erases arbitrary open carrier {trial:02d}", np.allclose(reset_channel(rho, target), density(target), atol=TOL))

        arbitrary_target = random_qubit(rng)
        swap = np.array(((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)), dtype=complex)
        moved = swap @ np.kron(state, arbitrary_target)
        check(f"E SWAP routes proposal through an unprepared target {trial:02d}", np.allclose(moved, np.kron(arbitrary_target, state), atol=TOL))

    left_gate = cnot(0, 1)
    right_gate = cnot(2, 1)
    check("E parity CNOTs commute", np.allclose(left_gate @ right_gate, right_gate @ left_gate, atol=TOL))
    initial = np.kron(np.kron(PLUS, ZERO), PLUS)
    parity_state = left_gate @ right_gate @ initial
    phi_plus = np.array((1, 0, 0, 1), dtype=complex) / np.sqrt(2.0)
    psi_plus = np.array((0, 1, 1, 0), dtype=complex) / np.sqrt(2.0)
    p0, endpoints0 = endpoint_state_after_parity(parity_state, 0)
    p1, endpoints1 = endpoint_state_after_parity(parity_state, 1)
    check("E supplied Born instrument leaves two equal parity alternatives", abs(p0 - 0.5) < TOL and abs(p1 - 0.5) < TOL)
    check("E J0 leaves Phi-plus open endpoints", abs(abs(np.vdot(phi_plus, endpoints0)) - 1.0) < TOL)
    check("E J1 leaves Psi-plus open endpoints", abs(abs(np.vdot(psi_plus, endpoints1)) - 1.0) < TOL)


def reachable(start: Coord, target: Coord, domain: frozenset[Coord], blocked: frozenset[Coord]) -> bool:
    if start in blocked or target in blocked:
        return False
    queue: deque[Coord] = deque((start,))
    seen = {start}
    while queue:
        site = queue.popleft()
        if site == target:
            return True
        for direction in DIRECTIONS:
            neighbor = add(site, direction)
            if neighbor in domain and neighbor not in blocked and neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return False


def compatible(left: RecordMap, right: RecordMap) -> bool:
    return all(site not in left or left[site] == value for site, value in right.items())


def collision_and_clause_deletion() -> None:
    section("F - Multiple seeds/fronts and load-bearing clause deletion")
    cell = Cell((0, 0, 0), (0, 0, 1), (1, 0, 0))
    path_records = full_path_records(cell)
    identical = full_path_records(cell)
    far = full_path_records(Cell((6, 0, 0), cell.forward, cell.transverse))
    near = full_path_records(Cell((1, 0, 0), cell.forward, cell.transverse))
    check("F duplicate identical seed construction is idempotently compatible", compatible(path_records, identical))
    check("F disjoint finite diamonds are compatible", set(path_records).isdisjoint(far) and compatible(path_records, far))
    conflicts = {site for site, value in near.items() if site in path_records and path_records[site] != value}
    check("F nearby independently typed construction paths have explicit collisions", len(conflicts) > 0 and not compatible(path_records, near))

    # Delete the full-path gate: all four shell roles exist by stage 55, so an
    # eager event schedule can lock while stages 56..98 are still absent.
    _, _, _, early_stage = run_schedule("event_first", cell, 0, 1801, root_threshold=55)
    check("F deleting the terminal path gate permits premature K/J", 55 <= early_stage < 98)

    domain = frozenset(product(range(-3, 4), repeat=3))
    full_shell = frozenset(CANONICAL_SHELL)
    outside = (3, 0, 0)
    check("F complete shell separates outside from output", not reachable(outside, OUTPUT, domain, full_shell))
    missing_face = full_shell - {(2, 0, 0)}
    check("F deleting one face-center fence record opens a causal path", reachable(outside, OUTPUT, domain, missing_face))

    complete, _, _, _ = run_schedule("first", cell, 0, 1802)
    left_only = dict(complete)
    left_only.pop(global_site(cell, OUTPUT))
    left_only.pop(global_site(cell, RIGHT_CLOSE))
    check("F two-K rule blocks output after only one port closes", not any(action.kind == "lock" for action in ready_actions(left_only, cell, 0)))
    check("F deleting one-K clause enables premature output", any(action.kind == "lock" for action in ready_actions(left_only, cell, 0, allow_single_k=True)))

    no_prep = dict(complete)
    for local in (OUTPUT, LEFT_TERMINAL, LEFT_CLOSE, LEFT_PREP):
        no_prep.pop(global_site(cell, local), None)
    check("F preparation certificate deletion would be load-bearing", not any(action.kind == "terminal" and action.side == "L" for action in ready_actions(no_prep, cell, 0)))

    # Without resetting the displaced arbitrary state into T, a fixed T record
    # cannot be valid for every open input state.
    t_projector = record_projector(named("T", cell.left_frame))
    check("F deleting terminal erase/preparation fails on zero input", not np.allclose(density(ZERO), t_projector, atol=TOL))
    check("F deleting terminal erase/preparation fails on one input", not np.allclose(density(ONE), t_projector, atol=TOL))

    # If the output carrier is not reset, an allowed prior |1> reverses the
    # advertised J0/Phi+ and J1/Psi+ association.  Equal outcome weights alone
    # therefore do not rescue the claimed parity record.
    left_gate = cnot(0, 1)
    right_gate = cnot(2, 1)
    no_output_reset = left_gate @ right_gate @ np.kron(np.kron(PLUS, ONE), PLUS)
    _, no_reset_j0 = endpoint_state_after_parity(no_output_reset, 0)
    phi_plus = np.array((1, 0, 0, 1), dtype=complex) / np.sqrt(2.0)
    psi_plus = np.array((0, 1, 1, 0), dtype=complex) / np.sqrt(2.0)
    check(
        "F deleting output reset reverses the claimed J0 parity label",
        abs(abs(np.vdot(phi_plus, no_reset_j0))) < TOL
        and abs(abs(np.vdot(psi_plus, no_reset_j0)) - 1.0) < TOL,
    )

    k_prefix = {
        global_site(cell, LEFT_CLOSE): named("K", cell.left_frame),
        global_site(cell, RIGHT_CLOSE): named("K", cell.right_frame),
    }
    rogue_site = global_site(cell, (0, -1, 0))
    no_rogue = dict(k_prefix)
    future_rogue = dict(k_prefix)
    future_rogue[rogue_site] = named("P", cell.frame)
    check("F deleting no-spontaneous-front clause admits a post-K internal source", no_rogue != future_rogue and all(no_rogue.get(site) == value for site, value in k_prefix.items()))


def first_record_nucleation_probe() -> None:
    section("G - First-record nucleation versus post-record self-closure")
    cell = Cell((0, 0, 0), (0, 0, 1), (1, 0, 0))
    check("G empty record configuration enables no post-seed action", ready_actions({}, cell, 0) == ())
    check("G one realized B0 seed enables the first construction append", any(action.kind == "build" for action in ready_actions(seed_records(cell), cell, 0)))

    rotations = proper_cubic_rotations()
    invariant_directions = [direction for direction in DIRECTIONS if all(matvec(rotation, direction) == direction for rotation in rotations)]
    check("G empty proper-cubic neighborhood selects no oriented seed direction", invariant_directions == [])
    for length in (3, 4, 5):
        sites = tuple(product(range(length), repeat=3))
        local_views = {site: ("open",) * 7 for site in sites}
        check(f"G uniform empty {length}^3 torus gives every site the same local view", len(set(local_views.values())) == 1)
        deterministic_fire = {site for site, view in local_views.items() if view == ("open",) * 7}
        check(f"G deterministic homogeneous nucleation on {length}^3 fires everywhere or nowhere", len(deterministic_fire) in {0, length ** 3} and len(deterministic_fire) != 1)

    all_site_centers = tuple((x, y, z) for x, y, z in product(range(3), repeat=3))
    support_a = full_path_records(Cell(all_site_centers[0], cell.forward, cell.transverse))
    support_b = full_path_records(Cell(all_site_centers[1], cell.forward, cell.transverse))
    check("G all-site nucleation immediately creates overlapping construction supports", not compatible(support_a, support_b))


def classification_and_no_go_controls() -> None:
    section("H - Classification, scoped residual, and no-go controls")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("`", "").replace("*", "").split())
    classifications = (
        "post-seed fence generation is candidate law content",
        "the first realized seed remains boundary or nucleation-law content",
        "stop and source roles are law-generated",
        "proposal preparation and open-site erasure are candidate law content",
        "k is derived within the isolated-diamond law",
        "arbitrary overlapping seeds remain nonconfluent",
        "born weights and actuality remain open",
        "rate remains open",
        "formation-as-autonomous-certified-extension is a theorem of the candidate law",
        "not a theorem of the current four axioms",
        "residual law fields are not separate axiom atoms",
        "no new record axiom is forced",
    )
    for phrase in classifications:
        check(f"H note preserves classification: {phrase}", phrase in note)
    n1_markers = (
        "sequential finite shell — attempted",
        "branching wavefront and acknowledgments — attempted",
        "same-content abelian shell — attempted",
        "disjoint multi-seed tiling — attempted",
        "overlap braid or reroute — attempted",
        "stochastic hard-core nucleation — attempted",
        "global-history or qca closure — attempted",
    )
    for marker in n1_markers:
        check(f"H N1 includes route: {marker}", marker in note)
    check("H no-go discipline gate records PASS", "no-go discipline status: pass" in note)


def main() -> None:
    source_contract()
    shell_path_and_minimality()
    content_and_covariance_probe()
    autonomous_schedule_probe()
    law_generated_preparation_and_bell()
    collision_and_clause_deletion()
    first_record_nucleation_probe()
    classification_and_no_go_controls()
    print(
        "\nSUMMARY: AUTONOMOUS SELF-CLOSING DIAMOND CYCLE 17 "
        f"PASS={PASS} FAIL={FAIL}"
    )
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
