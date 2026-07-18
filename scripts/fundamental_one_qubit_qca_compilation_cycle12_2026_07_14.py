#!/usr/bin/env python3
"""Cycle 12: fundamental one-qubit QCA compilation probes.

Companion note:
  docs/work_history/repo/review_feedback/
  FUNDAMENTAL_ONE_QUBIT_QCA_COMPILATION_CYCLE12_NOTE_2026-07-14.md

This runner attacks the remaining compilation gap between the exact Cycle 11
22-qubit macrocell construction and the framework's one-M2-per-Z3-site
substrate.  It tests unit translations, every proper cubic rotation,
relational finite program motifs, collision handling, noncommuting schedules,
record-only clock encodings, and the distinction between a fixed interpreter
and its program/boundary inputs.

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
    / "FUNDAMENTAL_ONE_QUBIT_QCA_COMPILATION_CYCLE12_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CYCLE11_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md"
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
HEADER_PATTERN = (1, 0, 1, 1, 0, 1)


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


def canonical_edge(left: Coord, right: Coord) -> tuple[Coord, Coord]:
    return tuple(sorted((left, right)))  # type: ignore[return-value]


def torus_add(coordinate: Coord, shift: Coord, side: int) -> Coord:
    return tuple((value + delta) % side for value, delta in zip(coordinate, shift))  # type: ignore[return-value]


def source_contract() -> None:
    section("A - Framework, predecessor, scope, and N1-N8 contract")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").replace("*", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    predecessor = CYCLE11_NOTE.read_text(encoding="utf-8").lower()

    check(
        "A live framework still has four named axioms",
        all(
            name in axioms
            for name in ("### Lattice", "### Qubit", "### Admissibility", "### Record")
        ),
    )
    check(
        "A fundamental carrier remains one M2 possibility algebra per site",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axioms,
    )
    check(
        "A approved premise registry still has four current paths",
        registry.count('"current_path"') == 4,
    )
    check(
        "A Cycle 11 explicitly leaves fundamental-carrier compilation open",
        "fundamental-carrier mismatch" in predecessor
        and "one-qubit-per-site" in predecessor,
    )

    required_phrases = (
        "authority: none",
        "finite block tiling obstruction",
        "symmetric matching obstruction",
        "relational motif compiler",
        "unit translations",
        "all 24 proper cubic rotations",
        "collision policy",
        "mutable hidden phase",
        "append-only clock front",
        "fixed interpreter does not derive its program",
        "smallest exact obstruction",
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


def parity_blocks(side: int) -> frozenset[frozenset[Coord]]:
    blocks: set[frozenset[Coord]] = set()
    for anchor in product(range(0, side, 2), repeat=3):
        block = frozenset(
            tuple((anchor[axis] + offset[axis]) % side for axis in range(3))
            for offset in product((0, 1), repeat=3)
        )
        blocks.add(block)
    return frozenset(blocks)


def shift_blocks(
    blocks: frozenset[frozenset[Coord]], shift: Coord, side: int
) -> frozenset[frozenset[Coord]]:
    return frozenset(
        frozenset(torus_add(coordinate, shift, side) for coordinate in block)
        for block in blocks
    )


def finite_block_tiling_obstruction() -> None:
    section("B - A finite macrocell tiling is state data, not a unit-translation law")
    side = 4
    blocks = parity_blocks(side)
    sites = frozenset(product(range(side), repeat=3))
    union = frozenset(coordinate for block in blocks for coordinate in block)
    incidence = {
        coordinate: sum(coordinate in block for block in blocks) for coordinate in sites
    }
    check("B 2x2x2 parity blocks cover the finite control torus", union == sites)
    check(
        "B 2x2x2 parity blocks are pairwise disjoint",
        all(count == 1 for count in incidence.values()),
    )
    check("B every parity macrocell carries eight one-qubit sites", all(len(block) == 8 for block in blocks))
    for direction_number, direction in enumerate(DIRECTIONS):
        shifted = shift_blocks(blocks, direction, side)
        check(
            f"B unit translation {direction_number} changes the absolute block partition",
            shifted != blocks,
        )

    # A translation-invariant equivalence relation has the block H of zero as
    # a subgroup.  Z^3 is torsion-free, so no nonzero h can lie in finite H:
    # all integer multiples nh would also have to lie in H.
    for vector in ((1, 0, 0), (1, 2, 0), (-2, 1, 3)):
        multiples = {scale(number, vector) for number in range(-8, 9)}
        check(
            f"B a nonzero candidate block displacement {vector} generates an expanding orbit",
            len(multiples) == 17,
        )


def all_nearest_neighbor_edges(side: int) -> frozenset[tuple[Coord, Coord]]:
    positive = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    return frozenset(
        canonical_edge(coordinate, torus_add(coordinate, direction, side))
        for coordinate in product(range(side), repeat=3)
        for direction in positive
    )


def edge_orbit(side: int) -> frozenset[tuple[Coord, Coord]]:
    rotations = proper_cubic_rotations()
    orbit: set[tuple[Coord, Coord]] = set()
    origin = (0, 0, 0)
    seed_direction = (1, 0, 0)
    for rotation in rotations:
        direction = matvec(rotation, seed_direction)
        for shift in product(range(side), repeat=3):
            orbit.add(canonical_edge(shift, torus_add(shift, direction, side)))
    return frozenset(orbit)


def axis_parity_matching(side: int) -> frozenset[tuple[Coord, Coord]]:
    return frozenset(
        canonical_edge(coordinate, torus_add(coordinate, (1, 0, 0), side))
        for coordinate in product(range(side), repeat=3)
        if coordinate[0] % 2 == 0
    )


def rotate_edges(
    edges: frozenset[tuple[Coord, Coord]], rotation: np.ndarray, side: int
) -> frozenset[tuple[Coord, Coord]]:
    answer: set[tuple[Coord, Coord]] = set()
    for left, right in edges:
        moved_left = tuple(value % side for value in matvec(rotation, left))
        moved_right = tuple(value % side for value in matvec(rotation, right))
        answer.add(canonical_edge(moved_left, moved_right))
    return frozenset(answer)


def matching_obstruction() -> None:
    section("C - A fully symmetric nearest-neighbor edge layer is not a matching")
    side = 4
    rotations = proper_cubic_rotations()
    check("C proper cubic rotation group has order 24", len(rotations) == 24)
    orbit = edge_orbit(side)
    all_edges = all_nearest_neighbor_edges(side)
    check("C one edge orbit under translations and rotations is every NN edge", orbit == all_edges)
    check("C the full edge orbit has exactly 3L^3 undirected edges", len(orbit) == 3 * side**3)
    degrees = {coordinate: 0 for coordinate in product(range(side), repeat=3)}
    for left, right in orbit:
        degrees[left] += 1
        degrees[right] += 1
    check("C the symmetric edge orbit has degree six, not degree one", set(degrees.values()) == {6})

    matching = axis_parity_matching(side)
    matching_degrees = {coordinate: 0 for coordinate in product(range(side), repeat=3)}
    for left, right in matching:
        matching_degrees[left] += 1
        matching_degrees[right] += 1
    check("C an axis/parity layer is a perfect matching", set(matching_degrees.values()) == {1})
    check(
        "C one-site translation changes the axis/parity matching",
        frozenset(
            canonical_edge(
                torus_add(left, (1, 0, 0), side),
                torus_add(right, (1, 0, 0), side),
            )
            for left, right in matching
        )
        != matching,
    )
    axis_changing = next(
        rotation
        for rotation in rotations
        if matvec(rotation, (1, 0, 0)) in ((0, 1, 0), (0, -1, 0))
    )
    check(
        "C an axis-changing cubic rotation changes the axis/parity matching",
        rotate_edges(matching, axis_changing, side) != matching,
    )


@dataclass(frozen=True)
class Program:
    anchor: Coord
    forward: Coord
    transverse: Coord

    @property
    def normal(self) -> Coord:
        return cross(self.forward, self.transverse)

    @property
    def endpoints(self) -> tuple[Coord, Coord]:
        return self.anchor, add(self.anchor, self.forward)


def header_sites(program: Program) -> tuple[Coord, ...]:
    origin = program.anchor
    forward = program.forward
    transverse = program.transverse
    normal = program.normal
    base = add(origin, scale(-3, forward))
    return (
        base,
        add(base, transverse),
        add(base, scale(3, transverse)),
        add(base, normal),
        add(base, scale(2, normal)),
        add(origin, scale(-2, forward)),
    )


def program_records(program: Program) -> dict[Coord, int]:
    return dict(zip(header_sites(program), HEADER_PATTERN))


def detect_programs(records: dict[Coord, int]) -> tuple[Program, ...]:
    if not records:
        return ()
    minima = [min(coordinate[axis] for coordinate in records) - 4 for axis in range(3)]
    maxima = [max(coordinate[axis] for coordinate in records) + 4 for axis in range(3)]
    found: list[Program] = []
    for anchor in product(*(range(minima[axis], maxima[axis] + 1) for axis in range(3))):
        for forward, transverse in oriented_frames():
            program = Program(anchor, forward, transverse)
            if all(
                records.get(site) == bit
                for site, bit in zip(header_sites(program), HEADER_PATTERN)
            ):
                found.append(program)
    return tuple(found)


def transform_program(
    program: Program, rotation: np.ndarray, translation: Coord = (0, 0, 0)
) -> Program:
    return Program(
        add(matvec(rotation, program.anchor), translation),
        matvec(rotation, program.forward),
        matvec(rotation, program.transverse),
    )


def transform_records(
    records: dict[Coord, int], rotation: np.ndarray, translation: Coord = (0, 0, 0)
) -> dict[Coord, int]:
    return {
        add(matvec(rotation, coordinate), translation): bit
        for coordinate, bit in records.items()
    }


def collision_policy(programs: tuple[Program, ...]) -> tuple[Program, ...]:
    endpoint_counts: dict[Coord, int] = {}
    for program in programs:
        for endpoint in program.endpoints:
            endpoint_counts[endpoint] = endpoint_counts.get(endpoint, 0) + 1
    if any(count > 1 for count in endpoint_counts.values()):
        return ()
    return programs


def relational_motif_compiler() -> None:
    section("D - Relational finite motif selects an anchor and oriented edge as state")
    identity = np.eye(3, dtype=int)
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    base_records = program_records(base)
    detected = detect_programs(base_records)
    check("D the asymmetric six-record header has one exact decoder", detected == (base,))
    check("D the decoded target is a fundamental nearest neighbor", sum(value * value for value in base.forward) == 1)
    check("D the header and data pair occupy distinct sites", not set(header_sites(base)).intersection(base.endpoints))

    translations = DIRECTIONS + ((-3, 4, 1), (2, -5, 7))
    for number, translation in enumerate(translations):
        moved_program = transform_program(base, identity, translation)
        moved_records = transform_records(base_records, identity, translation)
        check(
            f"D unit/general translation {number} transports the decoded program",
            detect_programs(moved_records) == (moved_program,),
        )

    rotations = proper_cubic_rotations()
    for number, rotation in enumerate(rotations):
        moved_program = transform_program(base, rotation)
        moved_records = transform_records(base_records, rotation)
        check(
            f"D proper cubic rotation {number:02d} transports the decoded program",
            detect_programs(moved_records) == (moved_program,),
        )

    second = Program((12, 0, 0), (0, 1, 0), (0, 0, 1))
    merged = dict(base_records)
    merged.update(program_records(second))
    two_programs = detect_programs(merged)
    check("D two separated motifs decode as two programs", set(two_programs) == {base, second})
    check("D collision policy retains disjoint fundamental gate pairs", set(collision_policy(two_programs)) == {base, second})

    colliding = Program((1, 0, 0), (-1, 0, 0), (0, 1, 0))
    check("D collision policy freezes two programs sharing a gate endpoint", collision_policy((base, colliding)) == ())
    for number, translation in enumerate(DIRECTIONS):
        translated_pair = tuple(
            transform_program(program, identity, translation)
            for program in (base, colliding)
        )
        check(
            f"D collision freeze is unit-translation covariant {number:02d}",
            collision_policy(translated_pair) == (),
        )
    for number, rotation in enumerate(rotations):
        rotated_pair = tuple(transform_program(program, rotation) for program in (base, colliding))
        check(
            f"D collision freeze is cubic covariant {number:02d}",
            collision_policy(rotated_pair) == (),
        )


def cnot_matrix() -> np.ndarray:
    return np.array(
        ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)),
        dtype=complex,
    )


def embedded_classical_gate(
    gate: callable, width: int
) -> np.ndarray:
    dimension = 1 << width
    matrix = np.zeros((dimension, dimension), dtype=complex)
    for column in range(dimension):
        bits = tuple((column >> (width - 1 - index)) & 1 for index in range(width))
        output = gate(bits)
        row = sum(bit << (width - 1 - index) for index, bit in enumerate(output))
        matrix[row, column] = 1.0
    return matrix


def gate_and_schedule_probe() -> None:
    section("E - One-shot gate succeeds; repetition and noncommuting schedules do not")
    cnot = cnot_matrix()
    check("E fundamental two-site CNOT is unitary", np.allclose(cnot.conj().T @ cnot, np.eye(4), atol=TOL))
    check("E repeated CNOT is the identity", np.allclose(cnot @ cnot, np.eye(4), atol=TOL))

    plus_zero = np.array((1.0, 0.0, 1.0, 0.0), dtype=complex) / np.sqrt(2.0)
    bell_plus = np.array((1.0, 0.0, 0.0, 1.0), dtype=complex) / np.sqrt(2.0)
    check("E one decoded CNOT creates the intended Bell correlation", np.allclose(cnot @ plus_zero, bell_plus, atol=TOL))
    check("E applying the same decoded CNOT again erases that correlation", np.allclose(cnot @ bell_plus, plus_zero, atol=TOL))

    def cnot_01(bits: tuple[int, ...]) -> tuple[int, ...]:
        a, b, c = bits
        return a, b ^ a, c

    def cnot_12(bits: tuple[int, ...]) -> tuple[int, ...]:
        a, b, c = bits
        return a, b, c ^ b

    gate_01 = embedded_classical_gate(cnot_01, 3)
    gate_12 = embedded_classical_gate(cnot_12, 3)
    check("E overlapping CNOT layers do not commute", not np.allclose(gate_12 @ gate_01, gate_01 @ gate_12, atol=TOL))
    input_100 = np.zeros(8, dtype=complex)
    input_100[4] = 1.0
    forward = gate_12 @ gate_01 @ input_100
    reverse = gate_01 @ gate_12 @ input_100
    check("E one layer order maps 100 to 111", abs(forward[7] - 1.0) < TOL)
    check("E the reverse layer order maps 100 to 110", abs(reverse[6] - 1.0) < TOL)

    basis = tuple(product((0, 1), repeat=3))
    cz_01 = np.diag([(-1.0) ** (bits[0] * bits[1]) for bits in basis])
    cz_12 = np.diag([(-1.0) ** (bits[1] * bits[2]) for bits in basis])
    check("E all-edge CZ supplies a commuting symmetric control route", np.allclose(cz_01 @ cz_12, cz_12 @ cz_01, atol=TOL))
    check("E a CZ layer is also an involution", np.allclose(cz_01 @ cz_01, np.eye(8), atol=TOL))

    plus_plus = np.ones(4, dtype=complex) / 2.0
    cz = np.diag((1.0, 1.0, 1.0, -1.0))
    graph_pair = (cz @ plus_plus).reshape(2, 2)
    reduced = graph_pair @ graph_pair.conj().T
    check("E a commuting CZ control can entangle one edge", abs(np.trace(reduced @ reduced).real - 0.5) < TOL)
    check("E repeating the same CZ restores the initial product state", np.allclose(cz @ cz @ plus_plus, plus_plus, atol=TOL))


def record_clock_encodings() -> None:
    section("F - Every exact phase encoding spends one of three distinct resources")
    cursor_before = (1, 0)
    cursor_after = (0, 1)
    check("F a moving one-hot cursor clears its previous site", cursor_before[0] == 1 and cursor_after[0] == 0)
    check("F a reversible phase bit necessarily toggles a previous value", (0 ^ 1, 1 ^ 1) == (1, 0))

    for capacity in (1, 2, 5, 11):
        states = [tuple([1] * tick + [0] * (capacity - tick)) for tick in range(capacity + 1)]
        monotone = all(
            all(old <= new for old, new in zip(states[tick], states[tick + 1]))
            for tick in range(capacity)
        )
        increments = all(
            sum(states[tick + 1]) - sum(states[tick]) == 1
            for tick in range(capacity)
        )
        check(f"F append-only clock of capacity {capacity} preserves old certificates", monotone)
        check(f"F append-only clock of capacity {capacity} supports one fresh tick per site", increments)
        check(f"F append-only clock of capacity {capacity} exhausts after exactly its capacity", len(set(states)) == capacity + 1 and sum(states[-1]) == capacity)

    # A tempting one-shot update maps both stage=0 data=x and stage=1 data=Ux
    # into stage=1 data=Ux, so it is not injective.  Reversibility would need an
    # archive holding the erased predecessor/stage information.
    cnot_basis_image = (0, 1, 3, 2)
    images: list[tuple[int, int]] = []
    for stage in (0, 1):
        for data in range(4):
            output_data = cnot_basis_image[data] if stage == 0 else data
            images.append((1, output_data))
    check("F irreversible one-shot stage write has colliding basis images", len(set(images)) == 4 < len(images))


def fixed_interpreter_probe() -> None:
    section("G - A fixed interpreter leaves program and preparation as inputs")
    identity = np.eye(4, dtype=complex)
    cnot = cnot_matrix()
    interpreter = np.block(
        [[identity, np.zeros((4, 4))], [np.zeros((4, 4)), cnot]]
    )
    check("G controlled interpreter is one fixed unitary", np.allclose(interpreter.conj().T @ interpreter, np.eye(8), atol=TOL))

    plus_zero = np.array((1.0, 0.0, 1.0, 0.0), dtype=complex) / np.sqrt(2.0)
    program_zero = np.concatenate((plus_zero, np.zeros(4, dtype=complex)))
    program_one = np.concatenate((np.zeros(4, dtype=complex), plus_zero))
    out_zero = interpreter @ program_zero
    out_one = interpreter @ program_one
    expected_one = np.concatenate(
        (np.zeros(4, dtype=complex), np.array((1.0, 0.0, 0.0, 1.0)) / np.sqrt(2.0))
    )
    check("G program zero selects the identity branch", np.allclose(out_zero, program_zero, atol=TOL))
    check("G program one selects the Bell-producing branch", np.allclose(out_one, expected_one, atol=TOL))
    check("G the same interpreter admits physically distinct program outcomes", not np.allclose(out_zero, out_one, atol=TOL))


def actuality_and_record_future() -> None:
    section("H - Fundamental compilation does not repair actuality or record sufficiency")
    bell_plus = np.array((1.0, 0.0, 0.0, 1.0), dtype=complex) / np.sqrt(2.0)
    bell_minus = np.array((1.0, 0.0, 0.0, -1.0), dtype=complex) / np.sqrt(2.0)
    equality = np.diag((1.0, 0.0, 0.0, 1.0))
    check("H both Bell equality branches remain nonzero", abs(abs(bell_plus[0]) ** 2 - 0.5) < TOL and abs(abs(bell_plus[3]) ** 2 - 0.5) < TOL)
    check("H opposite Bell phases give the same equality record", abs(np.vdot(bell_plus, equality @ bell_plus) - 1.0) < TOL and abs(np.vdot(bell_minus, equality @ bell_minus) - 1.0) < TOL)

    hadamard = np.array(((1.0, 1.0), (1.0, -1.0)), dtype=complex) / np.sqrt(2.0)
    discriminator = np.kron(hadamard, np.eye(2)) @ cnot_matrix()
    out_plus = discriminator @ bell_plus
    out_minus = discriminator @ bell_minus
    expected_plus = np.array((1.0, 0.0, 0.0, 0.0), dtype=complex)
    expected_minus = np.array((0.0, 0.0, 1.0, 0.0), dtype=complex)
    check("H a Bell recombination distinguishes the two equal-record packets", np.allclose(out_plus, expected_plus, atol=TOL) and np.allclose(out_minus, expected_minus, atol=TOL))


def scoped_obstruction_controls() -> None:
    section("I - Smallest exact obstruction and live escape routes")
    note = " ".join(
        NOTE.read_text(encoding="utf-8")
        .lower()
        .replace("`", "")
        .replace("*", "")
        .split()
    )
    required_controls = (
        "commuting all-edge gates remain open",
        "yang-baxter",
        "relational state tilings remain open",
        "append-only phase tape remains open",
        "intrinsically universal qca remains open",
        "asynchronous confluent rewrite remains open",
        "does not prove a general qca no-go",
        "does not compile the cycle 11 architecture",
        "conditional law clauses remain distinct from framework premises",
    )
    for phrase in required_controls:
        check(f"I note preserves scoped control: {phrase}", phrase in note)


def main() -> None:
    source_contract()
    finite_block_tiling_obstruction()
    matching_obstruction()
    relational_motif_compiler()
    gate_and_schedule_probe()
    record_clock_encodings()
    fixed_interpreter_probe()
    actuality_and_record_future()
    scoped_obstruction_controls()
    print(
        "\nSUMMARY: FUNDAMENTAL ONE-QUBIT QCA COMPILATION CYCLE 12 "
        f"PASS={PASS} FAIL={FAIL}"
    )
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
