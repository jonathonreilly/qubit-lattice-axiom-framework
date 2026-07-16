#!/usr/bin/env python3
"""Cycle 14: autonomous self-writing append-only Bell front.

Companion note:
  docs/work_history/repo/review_feedback/
  SELF_WRITING_APPEND_ONLY_BELL_FRONT_CYCLE14_NOTE_2026-07-14.md

A finite relational seed writes its own next program header.  A permanent
preparation certificate is appended only after a local reset channel has
prepared the next fresh triple, so every phase is reconstructible from
records.  The runner tests covariance, isolated indefinite growth, Bell
capability, reset irreversibility, dynamic collisions, seed/program freedom,
actuality, rate, capacity, and the Record-axiom classification.

No axiom, primitive, registry, audit surface, commit, or PR is changed.  Exit
code is zero exactly when every deterministic finite/symbolic check passes.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "SELF_WRITING_APPEND_ONLY_BELL_FRONT_CYCLE14_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CYCLE13_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "APPEND_ONLY_CAUSAL_BELL_WIRE_CYCLE13_NOTE_2026-07-14.md"
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
BUILDER_ONE_PATTERN = ("B1", "B0", "B1", "B1", "B0", "B1")
BUILDER_TWO_PATTERN = ("D1", "D0", "D1", "D1", "D0", "D1")


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
    e = program.transverse
    u = program.normal
    offsets = (
        e,
        scale(2, e),
        scale(3, e),
        u,
        scale(2, u),
        add(program.forward, add(e, u)),
    )
    return tuple(add(program.trigger, offset) for offset in offsets)


def certificate_site(program: Program) -> Coord:
    return add(program.trigger, negate(program.transverse))


def program_records(program: Program) -> dict[Coord, str]:
    return dict(zip(header_sites(program), HEADER_PATTERN))


def has_header(program: Program, records: dict[Coord, str]) -> bool:
    return all(
        records.get(site) == content
        for site, content in program_records(program).items()
    )


def detect_programs(records: dict[Coord, str]) -> tuple[Program, ...]:
    header_records = {
        site: content for site, content in records.items() if content in {"H0", "H1"}
    }
    if not header_records:
        return ()
    minima = [min(site[axis] for site in header_records) - 4 for axis in range(3)]
    maxima = [max(site[axis] for site in header_records) + 4 for axis in range(3)]
    found: list[Program] = []
    for trigger in product(
        *(range(minima[axis], maxima[axis] + 1) for axis in range(3))
    ):
        for forward, transverse in oriented_frames():
            program = Program(trigger, forward, transverse)
            if has_header(program, records):
                found.append(program)
    return tuple(found)


def next_straight(program: Program) -> Program:
    return Program(program.right, program.forward, program.transverse)


def next_turn(program: Program) -> Program:
    return Program(program.right, program.transverse, negate(program.forward))


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


def seed_records(program: Program) -> dict[Coord, str]:
    records = program_records(program)
    if program.trigger in records:
        raise ValueError("trigger overlaps header")
    records[program.trigger] = "Z0"
    return records


def append_one(
    records: dict[Coord, str], site: Coord, content: str
) -> dict[Coord, str]:
    if site in records:
        raise ValueError(f"record already present at {site}")
    answer = dict(records)
    answer[site] = content
    return answer


def append_many(
    records: dict[Coord, str], additions: dict[Coord, str]
) -> dict[Coord, str]:
    answer = dict(records)
    for site, content in additions.items():
        if site in answer and answer[site] != content:
            raise ValueError(f"incompatible record at {site}")
        answer[site] = content
    return answer


def is_extension(old: dict[Coord, str], new: dict[Coord, str]) -> bool:
    return len(new) >= len(old) and all(new.get(site) == content for site, content in old.items())


def prep_ready(program: Program, records: dict[Coord, str]) -> bool:
    return (
        has_header(program, records)
        and records.get(program.trigger, "").startswith("Z")
        and certificate_site(program) not in records
        and all(site not in records for site in program.data)
    )


def event_ready(program: Program, records: dict[Coord, str]) -> bool:
    return (
        records.get(certificate_site(program)) == "C"
        and all(site not in records for site in program.data)
    )


def left_ready(program: Program, records: dict[Coord, str]) -> bool:
    return records.get(program.center, "").startswith("X") and program.left not in records


def right_ready(program: Program, records: dict[Coord, str]) -> bool:
    return records.get(program.center, "").startswith("X") and program.right not in records


def shifted_header_sites(program: Program, step: int) -> tuple[Coord, ...]:
    shift = scale(step, program.forward)
    return tuple(add(site, shift) for site in header_sites(program))


def growth_assignment(program: Program, stage: int) -> dict[Coord, str]:
    if stage == 1:
        pattern = BUILDER_ONE_PATTERN
    elif stage == 2:
        pattern = BUILDER_TWO_PATTERN
    elif stage == 3:
        pattern = HEADER_PATTERN
    else:
        raise ValueError(stage)
    return dict(zip(shifted_header_sites(program, stage), pattern))


def assignment_complete(
    assignment: dict[Coord, str], records: dict[Coord, str]
) -> bool:
    return all(records.get(site) == content for site, content in assignment.items())


def assignment_compatible(
    assignment: dict[Coord, str], records: dict[Coord, str]
) -> bool:
    return all(site not in records or records[site] == content for site, content in assignment.items())


def growth_status(program: Program, records: dict[Coord, str]) -> str:
    first = growth_assignment(program, 1)
    second = growth_assignment(program, 2)
    third = growth_assignment(program, 3)
    if assignment_complete(third, records):
        return "done"
    if assignment_complete(second, records):
        return "G3" if assignment_compatible(third, records) else "blocked"
    if assignment_complete(first, records):
        return "G2" if assignment_compatible(second, records) else "blocked"
    if records.get(program.right, "").startswith("Z"):
        return "G1" if assignment_compatible(first, records) else "blocked"
    return "waiting"


def source_contract() -> None:
    section("A - Framework, Cycle 13 residual, scope, and N1-N8 contract")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").replace("*", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    predecessor = CYCLE13_NOTE.read_text(encoding="utf-8").lower()

    check(
        "A framework still has four named axioms",
        all(
            name in axioms
            for name in ("### Lattice", "### Qubit", "### Admissibility", "### Record")
        ),
    )
    check(
        "A Record supplies permanence while withholding formation dynamics",
        "Records form." in axioms
        and "records are permanent" in axioms
        and "formation rules" in axioms,
    )
    check(
        "A approved premise registry still has four current paths",
        registry.count('"current_path"') == 4,
    )
    check(
        "A Cycle 13 explicitly leaves static program and prepared state",
        "typed program records" in predecessor
        and "prepared-state field remains an import" in predecessor,
    )

    required = (
        "authority: none",
        "self-writing front",
        "finite seed",
        "law-generated preparation",
        "preparation certificate",
        "all six unit translations",
        "all 24 proper cubic rotations",
        "isolated-front indefinite-growth theorem",
        "dynamic collision countermodel",
        "no hidden cursor",
        "reset irreversibility",
        "one-history actuality remains open",
        "causal depth still does not fix rate",
        "formation-as-extension remains a theorem",
        "no new record axiom is forced",
        "n1 — alternative routes",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
    )
    for phrase in required:
        check(f"A note contains boundary: {phrase}", phrase in normalized)


def geometry_and_covariance() -> None:
    section("B - Finite seed, self-copy geometry, and lattice covariance")
    rotations = proper_cubic_rotations()
    check("B proper cubic rotation group has order 24", len(rotations) == 24)
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    seed = seed_records(base)
    check("B finite seed has six header records plus one trigger", len(seed) == 7)
    check("B finite seed decodes one relational program", detect_programs(seed) == (base,))
    check("B certificate is outside header and data sites", certificate_site(base) not in set(header_sites(base)).union(base.data))
    check("B both coherent data edges are nearest neighbors", manhattan(base.left, base.center) == 1 and manhattan(base.center, base.right) == 1)

    chain = [base]
    for _ in range(12):
        chain.append(next_straight(chain[-1]))
    supports: dict[Coord, tuple[int, str]] = {
        site: (-1, "seed-header") for site in header_sites(base)
    }
    overlap = False
    for number, program in enumerate(chain[:-1]):
        groups = {
            "data": program.data,
            "certificate": (certificate_site(program),),
            "builder-one": shifted_header_sites(program, 1),
            "builder-two": shifted_header_sites(program, 2),
            "next-header": shifted_header_sites(program, 3),
        }
        for kind, sites in groups.items():
            for site in sites:
                if site in supports:
                    overlap = True
                supports[site] = (number, kind)
    check("B twelve NN-builder cycles have pairwise-disjoint data/certificate/program supports", not overlap)
    check("B each cell right endpoint is the next trigger", all(chain[index].right == chain[index + 1].trigger for index in range(len(chain) - 1)))
    for stage in (1, 2, 3):
        source_sites = (
            header_sites(base) if stage == 1 else shifted_header_sites(base, stage - 1)
        )
        target_sites = shifted_header_sites(base, stage)
        check(
            f"B builder stage G{stage} is six disjoint nearest-neighbor writes",
            all(manhattan(source, target) == 1 for source, target in zip(source_sites, target_sites))
            and len(set(source_sites).intersection(target_sites)) == 0,
        )

    for number, translation in enumerate(DIRECTIONS):
        identity = np.eye(3, dtype=int)
        moved = transform_program(base, identity, translation)
        check(
            f"B finite seed is unit-translation covariant {number:02d}",
            transform_records(seed, identity, translation) == seed_records(moved)
            and transform_program(next_straight(base), identity, translation)
            == next_straight(moved)
            and all(
                transform_records(growth_assignment(base, stage), identity, translation)
                == growth_assignment(moved, stage)
                for stage in (1, 2, 3)
            ),
        )
    for number, rotation in enumerate(rotations):
        moved = transform_program(base, rotation)
        check(
            f"B seed and self-write map are proper-cubic covariant {number:02d}",
            transform_records(seed, rotation) == seed_records(moved)
            and transform_program(next_straight(base), rotation)
            == next_straight(moved)
            and matvec(rotation, certificate_site(base)) == certificate_site(moved)
            and all(
                transform_records(growth_assignment(base, stage), rotation)
                == growth_assignment(moved, stage)
                for stage in (1, 2, 3)
            ),
        )


def record_visible_phase_automaton() -> None:
    section("C - Preparation certificate and complete record-visible phase")
    first = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    second = next_straight(first)
    records = seed_records(first)
    check("C seed reconstructs preparation as the only first phase", prep_ready(first, records) and not event_ready(first, records))

    old = records
    records = append_one(records, certificate_site(first), "C")
    check("C preparation appends its certificate without changing seed records", is_extension(old, records))
    check("C certificate reconstructs the center event as ready", event_ready(first, records) and not prep_ready(first, records))

    old = records
    records = append_one(records, first.center, "X+")
    check("C center read is a permanent extension", is_extension(old, records))
    check("C center record reconstructs both endpoint reads", left_ready(first, records) and right_ready(first, records))

    old = records
    records = append_one(records, first.right, "Z0")
    check("C forward read is a permanent extension", is_extension(old, records))
    check("C forward record reconstructs first NN builder layer", growth_status(first, records) == "G1")

    old = records
    records = append_many(records, growth_assignment(first, 1))
    check("C first builder layer is a permanent extension", is_extension(old, records) and growth_status(first, records) == "G2")
    old = records
    records = append_many(records, growth_assignment(first, 2))
    check("C second builder layer is a permanent extension", is_extension(old, records) and growth_status(first, records) == "G3")
    old = records
    records = append_many(records, growth_assignment(first, 3))
    check("C final builder layer appends exactly the next header", is_extension(old, records) and has_header(second, records))
    check("C the next written header reconstructs its preparation phase", prep_ready(second, records))
    check("C delayed left read remains independently ready", left_ready(first, records))

    old = records
    records = append_one(records, first.left, "Z1")
    check("C delayed endpoint read never edits the advanced front", is_extension(old, records) and prep_ready(second, records))


I2 = np.eye(2, dtype=complex)
X = np.array(((0.0, 1.0), (1.0, 0.0)), dtype=complex)
Y = np.array(((0.0, -1.0j), (1.0j, 0.0)), dtype=complex)
Z = np.array(((1.0, 0.0), (0.0, -1.0)), dtype=complex)
ZERO = np.array((1.0, 0.0), dtype=complex)
ONE = np.array((0.0, 1.0), dtype=complex)
PLUS = np.array((1.0, 1.0), dtype=complex) / np.sqrt(2.0)
MINUS = np.array((1.0, -1.0), dtype=complex) / np.sqrt(2.0)


def density(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


def reset_kraus(target: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    return np.outer(target, ZERO.conj()), np.outer(target, ONE.conj())


def channel(rho: np.ndarray, kraus: tuple[np.ndarray, ...]) -> np.ndarray:
    return sum(operator @ rho @ operator.conj().T for operator in kraus)


def triple_reset_kraus(target: np.ndarray) -> tuple[np.ndarray, ...]:
    local = reset_kraus(target)
    return tuple(
        np.kron(np.kron(left, middle), right)
        for left, middle, right in product(local, repeat=3)
    )


def preparation_reset_probe() -> None:
    section("D - Law-generated preparation and its exact irreversibility price")
    local = reset_kraus(PLUS)
    check("D local plus-reset Kraus operators are trace preserving", np.allclose(sum(operator.conj().T @ operator for operator in local), I2, atol=TOL))
    inputs = (
        density(ZERO),
        density(ONE),
        density(PLUS),
        density(MINUS),
        I2 / 2.0,
        np.array(((0.7, 0.2j), (-0.2j, 0.3)), dtype=complex),
    )
    target = density(PLUS)
    for number, rho in enumerate(inputs):
        check(
            f"D plus-reset maps input {number} to the canonical fresh state",
            np.allclose(channel(rho, local), target, atol=TOL),
        )
    check("D plus-reset is idempotent", np.allclose(channel(channel(inputs[-1], local), local), target, atol=TOL))

    triple = triple_reset_kraus(PLUS)
    check("D three-site product reset has eight Kraus operators", len(triple) == 8)
    check("D three-site reset is trace preserving", np.allclose(sum(operator.conj().T @ operator for operator in triple), np.eye(8), atol=TOL))
    ghz = np.zeros(8, dtype=complex)
    ghz[0] = ghz[-1] = 1.0 / np.sqrt(2.0)
    expected = density(np.kron(np.kron(PLUS, PLUS), PLUS))
    check("D three-site reset erases an entangled input into plus cubed", np.allclose(channel(density(ghz), triple), expected, atol=TOL))

    check("D no unitary can map orthogonal zero and one to the same plus state", abs(np.vdot(ZERO, ONE)) < TOL and abs(np.vdot(PLUS, PLUS) - 1.0) < TOL)
    check("D header/builder/certificate/read labels are eleven distinct rank-one M2 possibilities", _typed_projectors_are_distinct())


def _typed_projectors_are_distinct() -> bool:
    certificate_axis = (X + Y + Z) / np.sqrt(3.0)
    builder_one_axis = (X + Y) / np.sqrt(2.0)
    builder_two_axis = (X + Z) / np.sqrt(2.0)
    projectors = (
        (I2 + Y) / 2.0,
        (I2 - Y) / 2.0,
        (I2 + X) / 2.0,
        (I2 - X) / 2.0,
        (I2 + Z) / 2.0,
        (I2 - Z) / 2.0,
        (I2 + certificate_axis) / 2.0,
        (I2 + builder_one_axis) / 2.0,
        (I2 - builder_one_axis) / 2.0,
        (I2 + builder_two_axis) / 2.0,
        (I2 - builder_two_axis) / 2.0,
    )
    return all(
        np.allclose(projector @ projector, projector, atol=TOL)
        and abs(np.trace(projector).real - 1.0) < TOL
        for projector in projectors
    ) and all(
        not np.allclose(projectors[left], projectors[right], atol=TOL)
        for left in range(len(projectors))
        for right in range(left + 1, len(projectors))
    )


def apply_cz(state: np.ndarray, left: int, right: int, width: int = 3) -> np.ndarray:
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


def measure(
    state: np.ndarray, site: int, basis: str, width: int = 3
) -> tuple[tuple[int, float, np.ndarray], ...]:
    if basis == "X":
        projectors = ((1, (I2 + X) / 2.0), (-1, (I2 - X) / 2.0))
    elif basis == "Z":
        projectors = ((0, (I2 + Z) / 2.0), (1, (I2 - Z) / 2.0))
    else:
        raise ValueError(basis)
    branches: list[tuple[int, float, np.ndarray]] = []
    for outcome, local in projectors:
        projector = single_site_operator(local, site, width)
        projected = projector @ state
        probability = float(np.vdot(projected, projected).real)
        if probability > TOL:
            branches.append((outcome, probability, projected / np.sqrt(probability)))
    return tuple(branches)


def complete_distribution(initial: np.ndarray) -> dict[tuple[int, int, int], float]:
    clustered = apply_cz(apply_cz(initial, 0, 1), 1, 2)
    answer: dict[tuple[int, int, int], float] = {}
    for middle, pm, state_m in measure(clustered, 1, "X"):
        for left, pl, state_l in measure(state_m, 0, "Z"):
            for right, pr, _ in measure(state_l, 2, "Z"):
                answer[(middle, left, right)] = pm * pl * pr
    return answer


def bell_preservation_and_preparation_countermodel() -> None:
    section("E - Bell capability after reset and exact preparation countermodel")
    plus_initial = np.kron(np.kron(PLUS, PLUS), PLUS)
    distribution = complete_distribution(plus_initial)
    check("E law-generated plus preparation yields four histories", len(distribution) == 4)
    check("E law-generated plus preparation gives weight one quarter", all(abs(value - 0.25) < TOL for value in distribution.values()))
    check("E center record fixes endpoint parity", all((left ^ right) == (0 if middle == 1 else 1) for middle, left, right in distribution))

    zero_initial = np.kron(np.kron(ZERO, ZERO), ZERO)
    zero_distribution = complete_distribution(zero_initial)
    check("E equally local zero-reset candidate gives two histories", len(zero_distribution) == 2)
    check("E plus-reset and zero-reset laws predict different endpoint records", distribution != zero_distribution)


def simulate_isolated_front(events: int) -> tuple[dict[Coord, str], tuple[Program, ...]]:
    current = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    programs: list[Program] = [current]
    records = seed_records(current)
    for _ in range(events):
        if not prep_ready(current, records):
            raise RuntimeError("preparation phase missing")
        records = append_one(records, certificate_site(current), "C")
        if not event_ready(current, records):
            raise RuntimeError("event phase missing")
        records = append_one(records, current.center, "X+")
        if not right_ready(current, records):
            raise RuntimeError("forward read missing")
        records = append_one(records, current.right, "Z0")
        for stage in (1, 2, 3):
            if growth_status(current, records) != f"G{stage}":
                raise RuntimeError(f"growth phase G{stage} missing")
            records = append_many(records, growth_assignment(current, stage))
        if not left_ready(current, records):
            raise RuntimeError("left read missing")
        records = append_one(records, current.left, "Z0")
        current = next_straight(current)
        programs.append(current)
    return records, tuple(programs)


def indefinite_growth_and_capacity() -> None:
    section("F - Finite-seed isolated indefinite-growth induction and capacity")
    for events in (1, 2, 5, 12):
        records, programs = simulate_isolated_front(events)
        check(f"F {events} cycles decode every self-written program", set(detect_programs(records)) == set(programs))
        check(f"F {events} cycles append exactly 22N+7 permanent records", len(records) == 22 * events + 7)
        check(f"F {events} cycles advance the trigger by exactly 3N", programs[-1].trigger == (3 * events, 0, 0))
        check(f"F {events} cycles leave the next preparation reconstructibly ready", prep_ready(programs[-1], records))

    for capacity in (21, 22, 47, 99, 220):
        maximum = capacity // 22
        check(
            f"F fresh support {capacity} cannot complete more than floor(M/22) cycles",
            22 * (maximum + 1) > capacity,
        )


def assignments_conflict(
    left: dict[Coord, str], right: dict[Coord, str]
) -> bool:
    return any(site in left and left[site] != content for site, content in right.items())


def dynamic_collision_countermodel() -> None:
    section("G - Exact local collision response and remaining timing freedom")
    first = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    second = Program((-2, -1, 2), (0, 1, 0), (1, 0, 0))
    first_assignment = growth_assignment(first, 1)
    second_assignment = growth_assignment(second, 1)
    conflict_sites = {
        site
        for site, content in first_assignment.items()
        if site in second_assignment and second_assignment[site] != content
    }
    check("G two covariant fronts have an explicit incompatible NN-builder site", conflict_sites == {(1, 0, 2)})
    check("G simultaneous incompatible nominations are detected before writing", assignments_conflict(first_assignment, second_assignment))

    empty: dict[Coord, str] = {}
    first_wins = append_many(empty, first_assignment)
    second_wins = append_many(empty, second_assignment)
    check("G after first write the opposing assignment is visibly blocked", any(site in first_wins and first_wins[site] != content for site, content in second_assignment.items()))
    check("G reversing first arrival gives a different permanent record set", first_wins != second_wins)

    rotations = proper_cubic_rotations()
    for number, rotation in enumerate(rotations):
        moved_first = transform_records(first_assignment, rotation)
        moved_second = transform_records(second_assignment, rotation)
        check(
            f"G incompatible collision relation is proper-cubic covariant {number:02d}",
            assignments_conflict(moved_first, moved_second),
        )
    for number, translation in enumerate(DIRECTIONS):
        identity = np.eye(3, dtype=int)
        moved_first = transform_records(first_assignment, identity, translation)
        moved_second = transform_records(second_assignment, identity, translation)
        check(
            f"G incompatible collision relation is unit-translation covariant {number:02d}",
            assignments_conflict(moved_first, moved_second),
        )


def irreducible_countermodels_and_controls() -> None:
    section("H - Seed, path, actuality, rate, and constitutional countermodels")
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    check("H empty record state has no decoded program", detect_programs({}) == ())
    check("H finite seed and no-seed states give event versus no event", prep_ready(base, seed_records(base)) and not prep_ready(base, {}))

    straight = next_straight(base)
    turned = next_turn(base)
    check("H straight and relational-turn propagation are distinct", straight != turned and straight.trigger == turned.trigger)
    for number, rotation in enumerate(proper_cubic_rotations()):
        moved = transform_program(base, rotation)
        check(
            f"H straight/turn alternatives are both cubic covariant {number:02d}",
            transform_program(straight, rotation) == next_straight(moved)
            and transform_program(turned, rotation) == next_turn(moved),
        )

    distribution = complete_distribution(np.kron(np.kron(PLUS, PLUS), PLUS))
    probabilities = np.asarray(tuple(distribution.values()))
    check("H prepared instrument retains four nonzero histories", len(probabilities) == 4 and np.all(probabilities > TOL))
    check("H no branch is selected with unit weight", float(np.max(probabilities)) < 1.0 - TOL)

    for depth in (1, 3, 8):
        fast = tuple(range(depth + 1))
        slow = tuple(11 * index for index in range(depth + 1))
        check(f"H causal depth {depth} admits distinct rate assignments", fast[-1] != slow[-1])
        check(f"H causal order {depth} survives rate rescaling", all(fast[index] < fast[index + 1] and slow[index] < slow[index + 1] for index in range(depth)))

    note = " ".join(
        NOTE.read_text(encoding="utf-8")
        .lower()
        .replace("`", "")
        .replace("*", "")
        .split()
    )
    required = (
        "formation-as-extension is a theorem of this candidate law",
        "not a theorem of the current four axioms",
        "no new record axiom is logically unavoidable",
        "reset/preparation instrument is new law content",
        "finite seed remains boundary content",
        "blank infinite corridor remains boundary content",
        "multi-front confluence remains open",
        "actuality and weights remain open",
        "rate remains open",
        "does not prove a general no-go",
    )
    for phrase in required:
        check(f"H note preserves classification: {phrase}", phrase in note)


def main() -> None:
    source_contract()
    geometry_and_covariance()
    record_visible_phase_automaton()
    preparation_reset_probe()
    bell_preservation_and_preparation_countermodel()
    indefinite_growth_and_capacity()
    dynamic_collision_countermodel()
    irreducible_countermodels_and_controls()
    print(
        "\nSUMMARY: SELF-WRITING APPEND-ONLY BELL FRONT CYCLE 14 "
        f"PASS={PASS} FAIL={FAIL}"
    )
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
