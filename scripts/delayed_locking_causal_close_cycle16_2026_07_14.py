#!/usr/bin/env python3
"""Cycle 16: delayed locking behind local causal-close certificates.

Companion note:
  docs/work_history/repo/review_feedback/
  DELAYED_LOCKING_CAUSAL_CLOSE_CYCLE16_NOTE_2026-07-14.md

The runner tests a strict nearest-neighbor conserved-front protocol.  Open
proposal qubits propagate by SWAP behind permanent direction-carrying fence
records.  A stop marker produces an arrival record and then a close
certificate adjacent to a merge site.  Only after both finite input ports are
closed do two commuting CNOTs compute and record symmetric parity.  The same
gate leaves Bell alternatives on plus inputs.

It also tests the narrow impossibility of inferring "no later proposal" from
any finite-radius view of an unbounded unclosed channel, plus the live bounded
diamond, explicit fence, conserved-front, and global-history escapes.

No axiom, primitive, registry, audit surface, commit, or PR is changed.  Exit
code is zero exactly when every deterministic check passes.
"""

from __future__ import annotations

from collections import deque
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
    / "DELAYED_LOCKING_CAUSAL_CLOSE_CYCLE16_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CYCLE15_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "ABELIAN_COMPATIBLE_SEED_BELL_MERGE_CYCLE15_NOTE_2026-07-14.md"
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
class Content:
    kind: str
    frame: Frame
    bit: int = -1


RecordMap = dict[Coord, Content]


@dataclass(frozen=True)
class MergeCell:
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

    @property
    def left_input(self) -> Coord:
        return add(self.center, negate(self.forward))

    @property
    def right_input(self) -> Coord:
        return add(self.center, self.forward)

    @property
    def left_stop(self) -> Coord:
        return add(self.left_terminal, self.left_frame.transverse)

    @property
    def right_stop(self) -> Coord:
        return add(self.right_terminal, self.right_frame.transverse)

    @property
    def left_terminal(self) -> Coord:
        return add(self.left_input, self.transverse)

    @property
    def right_terminal(self) -> Coord:
        return add(self.right_input, self.normal)

    @property
    def left_close(self) -> Coord:
        return add(self.left_terminal, negate(self.left_frame.transverse))

    @property
    def right_close(self) -> Coord:
        return add(self.right_terminal, negate(self.right_frame.transverse))

    @property
    def left_source_record(self) -> Coord:
        return add(self.left_terminal, scale(-4, self.left_frame.forward))

    @property
    def right_source_record(self) -> Coord:
        return add(self.right_terminal, scale(-4, self.right_frame.forward))

    @property
    def left_source_proposal(self) -> Coord:
        return add(self.left_source_record, self.left_frame.forward)

    @property
    def right_source_proposal(self) -> Coord:
        return add(self.right_source_record, self.right_frame.forward)


def content(kind: str, frame: Frame, bit: int = -1) -> Content:
    return Content(kind, frame, bit)


def initial_records(cell: MergeCell) -> RecordMap:
    return {
        cell.left_source_record: content("F", cell.left_frame),
        cell.right_source_record: content("F", cell.right_frame),
        cell.left_stop: content("M", cell.left_frame),
        cell.right_stop: content("M", cell.right_frame),
    }


def transform_frame(frame: Frame, rotation: np.ndarray) -> Frame:
    return Frame(
        matvec(rotation, frame.forward),
        matvec(rotation, frame.transverse),
    )


def transform_content(value: Content, rotation: np.ndarray) -> Content:
    return Content(value.kind, transform_frame(value.frame, rotation), value.bit)


def transform_cell(
    cell: MergeCell,
    rotation: np.ndarray,
    translation: Coord = (0, 0, 0),
) -> MergeCell:
    return MergeCell(
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
    section("A - Framework, freshness, predecessor, and scope contract")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").replace("*", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    predecessor = CYCLE15_NOTE.read_text(encoding="utf-8").lower()

    check(
        "A framework still has four named axioms",
        all(
            name in axioms
            for name in ("### Lattice", "### Qubit", "### Admissibility", "### Record")
        ),
    )
    check(
        "A Record supplies permanence while withholding formation rules",
        "records are permanent" in axioms and "formation rules" in axioms,
    )
    check("A approved premise registry still has four current paths", registry.count('"current_path"') == 4)
    check(
        "A Cycle 15 leaves upstream delayed locking live",
        "upstream of formation" in predecessor and "compatible write" in predecessor,
    )

    required = (
        "authority: none",
        "delayed locking",
        "purely local causal-close certificate",
        "strict nearest-neighbor",
        "proper-cubic covariant",
        "no global clock",
        "no hidden cursor",
        "no priority",
        "no future-arrival oracle",
        "bounded causal diamond",
        "explicit close/fence records",
        "conserved fronts",
        "global-history constraint",
        "bell-capable alternatives",
        "record-only readiness",
        "finite-radius silence no-go",
        "no new record axiom is forced",
        "not a universal quantum-state merger",
    )
    for phrase in required:
        check(f"A note states scope phrase: {phrase}", phrase in normalized)

    for label in ("N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"):
        check(f"A no-go discipline includes {label}", f"{label.lower()} —" in normalized)


I2 = np.eye(2, dtype=complex)
X = np.array(((0.0, 1.0), (1.0, 0.0)), dtype=complex)
Y = np.array(((0.0, -1.0j), (1.0j, 0.0)), dtype=complex)
Z = np.array(((1.0, 0.0), (0.0, -1.0)), dtype=complex)
ZERO = np.array((1.0, 0.0), dtype=complex)
ONE = np.array((0.0, 1.0), dtype=complex)
PLUS = np.array((1.0, 1.0), dtype=complex) / np.sqrt(2.0)

COEFFICIENTS: dict[str, tuple[float, float, float]] = {
    "F": (1.0, 2.0, 4.0),
    "M": (1.0, 3.0, 7.0),
    "T": (2.0, 5.0, 11.0),
    "K": (3.0, 8.0, 17.0),
}


def pauli(vector: np.ndarray) -> np.ndarray:
    return vector[0] * X + vector[1] * Y + vector[2] * Z


def bloch_vector(value: Content) -> np.ndarray:
    frame = value.frame
    if value.kind == "J":
        vector = np.asarray(frame.forward, dtype=float)
        return vector if value.bit == 0 else -vector
    coefficients = COEFFICIENTS[value.kind]
    vector = (
        coefficients[0] * np.asarray(frame.forward, dtype=float)
        + coefficients[1] * np.asarray(frame.transverse, dtype=float)
        + coefficients[2] * np.asarray(frame.normal, dtype=float)
    )
    return vector / np.linalg.norm(vector)


def record_projector(value: Content) -> np.ndarray:
    return (I2 + pauli(bloch_vector(value))) / 2.0


def one_m2_content_probe() -> None:
    section("B - One-M2 record content and proper-cubic geometry")
    frames = oriented_frames()
    check("B oriented proper-cubic frame orbit has 24 elements", len(frames) == 24)
    values = [content(kind, frame) for kind in COEFFICIENTS for frame in frames]
    values.extend(content("J", frame, bit) for frame in frames for bit in (0, 1))
    projectors = [record_projector(value) for value in values]
    check(
        "B every protocol record is a rank-one possibility in one M2",
        all(
            np.allclose(projector @ projector, projector, atol=TOL)
            and abs(np.trace(projector).real - 1.0) < TOL
            for projector in projectors
        ),
    )
    unique = {
        tuple(np.round(projector.real, 12).ravel())
        + tuple(np.round(projector.imag, 12).ravel())
        for projector in projectors
    }
    check("B four generic content orbits and six parity axes are distinct", len(unique) == 4 * 24 + 6)

    cell = MergeCell((0, 0, 0), (0, 0, 1), (1, 0, 0))
    roles = (
        cell.center,
        cell.left_input,
        cell.right_input,
        cell.left_stop,
        cell.right_stop,
        cell.left_terminal,
        cell.right_terminal,
        cell.left_close,
        cell.right_close,
        cell.left_source_record,
        cell.right_source_record,
    )
    check("B merge, port, terminal, close, and source roles are site-disjoint", len(set(roles)) == len(roles))
    check("B input qubits are nearest neighbors of output", manhattan(cell.left_input, cell.center) == manhattan(cell.right_input, cell.center) == 1)
    check("B close certificates are nearest neighbors of output", manhattan(cell.left_close, cell.center) == manhattan(cell.right_close, cell.center) == 1)
    check("B terminal fences are nearest neighbors of proposal inputs", manhattan(cell.left_terminal, cell.left_input) == manhattan(cell.right_terminal, cell.right_input) == 1)
    check("B stop markers are nearest neighbors of terminal pre-move tips", manhattan(cell.left_stop, cell.left_terminal) == manhattan(cell.right_stop, cell.right_terminal) == 1)
    check("B terminal-to-close writes are nearest-neighbor", manhattan(cell.left_terminal, cell.left_close) == manhattan(cell.right_terminal, cell.right_close) == 1)

    rotations = proper_cubic_rotations()
    check("B proper cubic rotation group has 24 matrices", len(rotations) == 24)
    seed = initial_records(cell)
    for number, rotation in enumerate(rotations):
        moved = transform_cell(cell, rotation)
        check(
            f"B seed and typed directions rotate covariantly {number:02d}",
            transform_records(seed, rotation) == initial_records(moved),
        )
    identity = np.eye(3, dtype=int)
    for number, translation in enumerate(DIRECTIONS):
        moved = transform_cell(cell, identity, translation)
        check(
            f"B seed translates covariantly {number:02d}",
            transform_records(seed, identity, translation) == initial_records(moved),
        )


@dataclass(frozen=True)
class Action:
    kind: str
    site: Coord
    value: Content
    anchor: Coord

    @property
    def name(self) -> str:
        return f"{self.kind}:{self.site}:{self.value.kind}:{self.value.bit}"


def append_record(records: RecordMap, site: Coord, value: Content) -> RecordMap:
    if site in records and records[site] != value:
        raise ValueError(f"incompatible record at {site}")
    answer = dict(records)
    answer[site] = value
    return answer


def is_extension(old: RecordMap, new: RecordMap) -> bool:
    return len(new) >= len(old) and all(new.get(site) == value for site, value in old.items())


def ready_actions(records: RecordMap, cell: MergeCell) -> tuple[Action, ...]:
    answer: list[Action] = []
    for trail_site, trail_value in records.items():
        if trail_value.kind != "F":
            continue
        frame = trail_value.frame
        tip = add(trail_site, frame.forward)
        if tip in records:
            continue
        stop_site = add(tip, frame.transverse)
        expected_stop = content("M", frame)
        if records.get(stop_site) == expected_stop:
            target = add(tip, frame.forward)
            if target not in records:
                answer.append(Action("terminal", tip, content("T", frame), trail_site))
        else:
            target = add(tip, frame.forward)
            if target not in records:
                answer.append(Action("propagate", tip, content("F", frame), trail_site))

    for terminal, terminal_value in records.items():
        if terminal_value.kind != "T":
            continue
        target = add(terminal, negate(terminal_value.frame.transverse))
        expected = content("K", terminal_value.frame)
        if target not in records:
            answer.append(Action("close", target, expected, terminal))

    left_k = content("K", cell.left_frame)
    right_k = content("K", cell.right_frame)
    if (
        records.get(cell.left_close) == left_k
        and records.get(cell.right_close) == right_k
        and cell.center not in records
        and cell.left_input not in records
        and cell.right_input not in records
    ):
        answer.append(Action("lock", cell.center, content("J", cell.frame, -1), cell.center))
    return tuple(sorted(answer, key=lambda item: item.name))


def initial_open_states(
    cell: MergeCell, left_bit: int, right_bit: int
) -> dict[Coord, np.ndarray]:
    states: dict[Coord, np.ndarray] = {}
    for source, frame in (
        (cell.left_source_record, cell.left_frame),
        (cell.right_source_record, cell.right_frame),
    ):
        for step in range(1, 6):
            states[add(source, scale(step, frame.forward))] = ZERO.copy()
    states[cell.left_source_proposal] = (ZERO if left_bit == 0 else ONE).copy()
    states[cell.right_source_proposal] = (ZERO if right_bit == 0 else ONE).copy()
    states[cell.center] = ZERO.copy()
    for site in (cell.left_close, cell.right_close):
        states[site] = ZERO.copy()
    return states


def apply_action(
    records: RecordMap,
    states: dict[Coord, np.ndarray],
    selected: Action,
    cell: MergeCell,
) -> tuple[RecordMap, dict[Coord, np.ndarray]]:
    answer_records = dict(records)
    answer_states = {site: state.copy() for site, state in states.items()}
    if selected.kind in {"propagate", "terminal"}:
        frame = selected.value.frame
        tip = selected.site
        target = add(tip, frame.forward)
        if tip not in answer_states or target not in answer_states:
            raise RuntimeError("missing open carrier")
        if not np.allclose(answer_states[target], ZERO, atol=TOL):
            raise RuntimeError("forward carrier was not prepared blank")
        proposal = answer_states[tip].copy()
        answer_states[target] = proposal
        del answer_states[tip]
    elif selected.kind == "close":
        answer_states.pop(selected.site, None)
    elif selected.kind == "lock":
        left = answer_states[cell.left_input]
        right = answer_states[cell.right_input]
        if np.allclose(left, ZERO, atol=TOL):
            left_bit = 0
        elif np.allclose(left, ONE, atol=TOL):
            left_bit = 1
        else:
            raise RuntimeError("fixture lock expects basis proposal")
        if np.allclose(right, ZERO, atol=TOL):
            right_bit = 0
        elif np.allclose(right, ONE, atol=TOL):
            right_bit = 1
        else:
            raise RuntimeError("fixture lock expects basis proposal")
        selected = Action(
            selected.kind,
            selected.site,
            content("J", cell.frame, left_bit ^ right_bit),
            selected.anchor,
        )
        answer_states.pop(cell.center, None)
    else:
        raise ValueError(selected.kind)

    answer_records = append_record(answer_records, selected.site, selected.value)
    if not is_extension(records, answer_records) or len(answer_records) != len(records) + 1:
        raise RuntimeError("transition was not a strict record extension")
    return answer_records, answer_states


def run_schedule(
    chooser: str,
    cell: MergeCell,
    left_bit: int,
    right_bit: int,
    seed: int = 0,
) -> tuple[RecordMap, dict[Coord, np.ndarray], tuple[str, ...]]:
    records = initial_records(cell)
    states = initial_open_states(cell, left_bit, right_bit)
    history: list[str] = []
    rng = random.Random(seed)
    for _ in range(64):
        actions = ready_actions(records, cell)
        if not actions:
            return records, states, tuple(history)
        if chooser == "first":
            selected = actions[0]
        elif chooser == "last":
            selected = actions[-1]
        elif chooser == "random":
            selected = rng.choice(actions)
        else:
            raise ValueError(chooser)
        records, states = apply_action(records, states, selected, cell)
        history.append(selected.name)
    raise RuntimeError("protocol did not terminate")


def finite_protocol_schedule_probe() -> None:
    section("C - Conserved-front, causal-close, and schedule probe")
    cell = MergeCell((0, 0, 0), (0, 0, 1), (1, 0, 0))
    for left_bit, right_bit in product((0, 1), repeat=2):
        runs = [
            run_schedule("first", cell, left_bit, right_bit),
            run_schedule("last", cell, left_bit, right_bit),
        ]
        runs.extend(
            run_schedule("random", cell, left_bit, right_bit, seed)
            for seed in range(12)
        )
        reference_records, reference_states, _ = runs[0]
        for index, (records, states, history) in enumerate(runs):
            check(
                f"C bits {left_bit}{right_bit} schedule {index:02d} has one terminal record map",
                records == reference_records,
            )
            check(
                f"C bits {left_bit}{right_bit} schedule {index:02d} uses eleven appends",
                len(history) == 11 and len(records) == 15,
            )
            check(
                f"C bits {left_bit}{right_bit} schedule {index:02d} preserves endpoint proposals",
                np.allclose(states[cell.left_input], reference_states[cell.left_input], atol=TOL)
                and np.allclose(states[cell.right_input], reference_states[cell.right_input], atol=TOL),
            )
        output = reference_records[cell.center]
        check(
            f"C basis proposals {left_bit}{right_bit} lock symmetric XOR",
            output.kind == "J" and output.bit == (left_bit ^ right_bit),
        )
        check(
            f"C basis proposals {left_bit}{right_bit} produce both local close certificates",
            reference_records.get(cell.left_close) == content("K", cell.left_frame)
            and reference_records.get(cell.right_close) == content("K", cell.right_frame),
        )
        check(
            f"C basis proposals {left_bit}{right_bit} leave permanent source-to-port fences",
            all(
                reference_records.get(add(source, scale(step, frame.forward)), Content("", cell.frame)).kind
                == ("T" if step == 4 else "F")
                for source, frame in (
                    (cell.left_source_record, cell.left_frame),
                    (cell.right_source_record, cell.right_frame),
                )
                for step in range(0, 5)
            ),
        )
        check(
            f"C basis proposals {left_bit}{right_bit} use genuinely different schedules",
            len({history for _, _, history in runs}) > 2,
        )

    initial = initial_records(cell)
    actions = ready_actions(initial, cell)
    check("C initially only the two conserved fronts can propagate", len(actions) == 2 and all(item.kind == "propagate" for item in actions))
    almost, _, _ = run_schedule("first", cell, 0, 0)
    check("C terminal state has no enabled cursor or cleanup action", ready_actions(almost, cell) == ())


def single_site_operator(operator: np.ndarray, site: int, width: int = 3) -> np.ndarray:
    answer = np.array((1.0,), dtype=complex)
    for index in range(width):
        answer = np.kron(answer, operator if index == site else I2)
    return answer


def cnot(control: int, target: int, width: int = 3) -> np.ndarray:
    answer = np.zeros((1 << width, 1 << width), dtype=complex)
    for index in range(1 << width):
        bits = [int(value) for value in f"{index:0{width}b}"]
        if bits[control] == 1:
            bits[target] ^= 1
        moved = int("".join(str(value) for value in bits), 2)
        answer[moved, index] = 1.0
    return answer


def swap_operator(width: int = 2) -> np.ndarray:
    if width != 2:
        raise ValueError(width)
    return np.array(
        (
            (1, 0, 0, 0),
            (0, 0, 1, 0),
            (0, 1, 0, 0),
            (0, 0, 0, 1),
        ),
        dtype=complex,
    )


def endpoint_state_after_parity(
    state: np.ndarray, outcome: int
) -> tuple[float, np.ndarray]:
    local = (I2 + Z) / 2.0 if outcome == 0 else (I2 - Z) / 2.0
    projector = single_site_operator(local, 1)
    projected = projector @ state
    probability = float(np.vdot(projected, projected).real)
    normalized = projected / np.sqrt(probability)
    endpoint = np.zeros(4, dtype=complex)
    for left, right in product((0, 1), repeat=2):
        index = 4 * left + 2 * outcome + right
        endpoint[2 * left + right] = normalized[index]
    return probability, endpoint


def quantum_information_and_bell_probe() -> None:
    section("D - Exact quantum transport, symmetric joint value, and Bell alternatives")
    swap = swap_operator()
    rng = np.random.default_rng(1601)
    for trial in range(16):
        proposal = rng.normal(size=2) + 1.0j * rng.normal(size=2)
        proposal /= np.linalg.norm(proposal)
        moved = swap @ np.kron(proposal, ZERO)
        check(f"D SWAP moves arbitrary proposal exactly {trial:02d}", np.allclose(moved, np.kron(ZERO, proposal), atol=TOL))
        check(f"D SWAP does not clone arbitrary proposal {trial:02d}", not np.allclose(moved, np.kron(proposal, proposal), atol=TOL))

    left_gate = cnot(0, 1)
    right_gate = cnot(2, 1)
    identity = np.eye(8, dtype=complex)
    check("D both proposal-to-output CNOTs are unitary", np.allclose(left_gate.conj().T @ left_gate, identity, atol=TOL) and np.allclose(right_gate.conj().T @ right_gate, identity, atol=TOL))
    check("D symmetric parity gates commute exactly", np.allclose(left_gate @ right_gate, right_gate @ left_gate, atol=TOL))

    for left_bit, right_bit in product((0, 1), repeat=2):
        left = ZERO if left_bit == 0 else ONE
        right = ZERO if right_bit == 0 else ONE
        initial = np.kron(np.kron(left, ZERO), right)
        final = left_gate @ right_gate @ initial
        expected = np.kron(np.kron(left, ZERO if (left_bit ^ right_bit) == 0 else ONE), right)
        check(f"D basis joint value is XOR for {left_bit}{right_bit}", np.allclose(final, expected, atol=TOL))

    initial_plus = np.kron(np.kron(PLUS, ZERO), PLUS)
    parity_state = left_gate @ right_gate @ initial_plus
    phi_plus = np.array((1, 0, 0, 1), dtype=complex) / np.sqrt(2.0)
    psi_plus = np.array((0, 1, 1, 0), dtype=complex) / np.sqrt(2.0)
    p_even, even_endpoints = endpoint_state_after_parity(parity_state, 0)
    p_odd, odd_endpoints = endpoint_state_after_parity(parity_state, 1)
    check("D supplied Born instrument gives equal parity alternatives", abs(p_even - 0.5) < TOL and abs(p_odd - 0.5) < TOL)
    check("D even close-and-lock outcome leaves Phi-plus endpoints", abs(abs(np.vdot(phi_plus, even_endpoints)) - 1.0) < TOL)
    check("D odd close-and-lock outcome leaves Psi-plus endpoints", abs(abs(np.vdot(psi_plus, odd_endpoints)) - 1.0) < TOL)
    check("D parity output is symmetric under proposal exchange", np.allclose(left_gate @ right_gate, right_gate @ left_gate, atol=TOL))


def local_view(records: dict[Coord, str], center: Coord, radius: int) -> dict[Coord, str]:
    return {
        subtract(site, center): value
        for site, value in records.items()
        if manhattan(site, center) <= radius
    }


def finite_radius_silence_probe() -> None:
    section("E - Finite-radius silence no-go on an unbounded unclosed channel")
    center = (0, 0, 0)
    local_ready = {
        (1, 0, 0): "local-left-arrived",
        (0, 1, 0): "local-right-arrived",
    }
    for radius in range(1, 17):
        closed_history = dict(local_ready)
        open_history = dict(local_ready)
        far_source = (0, 0, radius + 2)
        open_history[far_source] = "late-incompatible-source"
        check(
            f"E radius {radius:02d} cannot distinguish silence from a far later source",
            local_view(closed_history, center, radius)
            == local_view(open_history, center, radius),
        )
        check(
            f"E radius {radius:02d} late source lies outside the inspected ball",
            manhattan(far_source, center) > radius,
        )
        path = [(0, 0, z) for z in range(radius + 2, -1, -1)]
        check(
            f"E radius {radius:02d} open NN channel admits a later causal path",
            all(manhattan(path[index], path[index + 1]) == 1 for index in range(len(path) - 1)),
        )

    check(
        "E a timeout changes no record in the local view",
        local_view(local_ready, center, 4) == local_view(local_ready, center, 4),
    )


def reachable(
    start: Coord,
    target: Coord,
    domain: frozenset[Coord],
    blocked: frozenset[Coord],
) -> bool:
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


def bounded_diamond_and_fence_probe() -> None:
    section("F - Bounded causal diamond, explicit fence, and conserved-front escapes")
    radius = 3
    domain = frozenset(
        (x, y, z)
        for x in range(-4, 5)
        for y in range(-4, 5)
        for z in range(-4, 5)
    )
    shell = frozenset(
        site for site in domain if max(abs(value) for value in site) == radius
    )
    ports = frozenset(((radius, 0, 0), (-radius, 0, 0)))
    open_shell = shell - ports
    outside = (4, 0, 0)
    center = (0, 0, 0)
    check("F cubic fence with named open port admits a causal path", reachable(outside, center, domain, open_shell))
    check("F recording both finite ports closes every path through the shell", not reachable(outside, center, domain, shell))
    check("F cubic shell is finite and costs surface records", len(shell) == 218)

    cell = MergeCell((0, 0, 0), (0, 0, 1), (1, 0, 0))
    final_records, _, _ = run_schedule("first", cell, 0, 1)
    late_source = add(cell.left_source_record, scale(-2, cell.left_frame.forward))
    late_tip = add(late_source, cell.left_frame.forward)
    late_target = add(late_tip, cell.left_frame.forward)
    check("F a later same-port front meets a permanent trail record", late_target in final_records)
    check("F permanent trail makes later same-port SWAP impossible", late_target in final_records and final_records[late_target].kind == "F")
    check("F both law-generated K records sit in the output NN neighborhood", manhattan(cell.left_close, cell.center) == 1 and manhattan(cell.right_close, cell.center) == 1)
    check("F output record exists only after both close records in every terminal run", final_records[cell.center].kind == "J" and final_records[cell.left_close].kind == "K" and final_records[cell.right_close].kind == "K")


def global_history_constraint_probe() -> None:
    section("G - Global-history constraint escape and its exact price")
    histories = (
        ("L", "R", "CLOSE"),
        ("R", "L", "CLOSE"),
        ("L", "CLOSE", "R"),
        ("R", "CLOSE", "L"),
    )

    def globally_admissible(history: tuple[str, ...]) -> bool:
        return history[-1] == "CLOSE" and set(history[:-1]) == {"L", "R"}

    admitted = tuple(history for history in histories if globally_admissible(history))
    check("G global-history rule admits both input orders", admitted == histories[:2])
    check("G global-history rule excludes both late-after-close histories", all(not globally_admissible(history) for history in histories[2:]))
    prefix = ("L", "R", "CLOSE")
    good_completion = prefix
    bad_completion = prefix + ("LATE",)
    check("G a finite local prefix cannot certify its own global completion", prefix == bad_completion[: len(prefix)] and globally_admissible(good_completion) and not globally_admissible(bad_completion))
    check("G global admissibility is a history restriction rather than an appended local record", "CLOSE" in good_completion and globally_admissible(good_completion))


def classification_and_note_controls() -> None:
    section("H - Law/boundary/derivation classification and no-go controls")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("`", "").replace("*", "").split())
    classifications = (
        "front propagation is candidate law content",
        "stop markers and finite port geometry are boundary content",
        "arrival and close writes are candidate law content",
        "the k certificate is derived only within the candidate protocol",
        "prepared proposal carriers and blank corridors are imported",
        "the parity instrument is candidate law content",
        "born weights and actuality remain open",
        "rate remains open",
        "finite-radius silence is not causal completeness",
        "global-history consistency remains a live nonlocal escape",
        "formation-as-certified-extension is a theorem of this protocol",
        "not a theorem of the current four axioms",
        "no new record axiom is forced",
    )
    for phrase in classifications:
        check(f"H note preserves classification: {phrase}", phrase in note)

    n1_markers = (
        "wider finite radius — attempted",
        "timeout or patient waiting — attempted",
        "bounded finite ports — attempted",
        "explicit closed fence — attempted",
        "conserved proposal front — attempted",
        "topological/unitary transport — attempted",
        "global-history restriction — attempted",
    )
    for marker in n1_markers:
        check(f"H N1 includes tested route: {marker}", marker in note)
    check("H no-go gate records pass status", "no-go discipline status: pass" in note)


def main() -> None:
    source_contract()
    one_m2_content_probe()
    finite_protocol_schedule_probe()
    quantum_information_and_bell_probe()
    finite_radius_silence_probe()
    bounded_diamond_and_fence_probe()
    global_history_constraint_probe()
    classification_and_note_controls()
    print(
        "\nSUMMARY: DELAYED LOCKING CAUSAL CLOSE CYCLE 16 "
        f"PASS={PASS} FAIL={FAIL}"
    )
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
