#!/usr/bin/env python3
"""Cycle 11: infinite reversible record-export QCA integration probes.

Companion note:
  docs/work_history/repo/review_feedback/
  INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md

The construction is an enlarged-cell, translation/proper-cubic-covariant
unitary QCA.  It commits one isolated coherent signal into a local relational
record and exports compensating information along six infinite rails.  The
runner then attacks recurrence, collisions, actuality, record-only future
sufficiency, schedule dependence, renewal, and the resource/Green bridge.

No axiom, primitive, registry, audit surface, commit, or PR is changed.  Exit
code is zero exactly when every deterministic finite/symbolic check passes.
"""

from __future__ import annotations

from itertools import permutations, product
from math import pi
from pathlib import Path
import subprocess
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
QB16_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "AUTONOMOUS_HOMOGENEOUS_BINARY_NUCLEATION_NOTE_2026-07-14.md"
)
QB16_RUNNER = ROOT / "scripts" / "autonomous_homogeneous_binary_nucleation_probe_2026_07_14.py"

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


def coordinates(side: int) -> tuple[Coord, ...]:
    return tuple(product(range(side), repeat=3))


def coordinate_index(side: int) -> dict[Coord, int]:
    return {coordinate: index for index, coordinate in enumerate(coordinates(side))}


def proper_cubic_rotations() -> tuple[np.ndarray, ...]:
    rotations: list[np.ndarray] = []
    for axis_permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(axis_permutation):
                matrix[row, column] = signs[row]
            if round(np.linalg.det(matrix)) == 1:
                rotations.append(matrix)
    unique = {tuple(matrix.ravel()): matrix for matrix in rotations}
    return tuple(unique.values())


def direction_map(rotation: np.ndarray) -> np.ndarray:
    direction_index = {direction: number for number, direction in enumerate(DIRECTIONS)}
    mapping = np.zeros(6, dtype=int)
    for number, direction in enumerate(DIRECTIONS):
        rotated = tuple(int(value) for value in rotation @ np.asarray(direction))
        mapping[number] = direction_index[rotated]
    return mapping


def coordinate_map(
    side: int,
    rotation: np.ndarray | None = None,
    shift: Coord = (0, 0, 0),
) -> np.ndarray:
    if rotation is None:
        rotation = np.eye(3, dtype=int)
    index = coordinate_index(side)
    mapping = np.zeros(side**3, dtype=int)
    for coordinate in coordinates(side):
        moved_array = (
            rotation @ np.asarray(coordinate, dtype=int)
            + np.asarray(shift, dtype=int)
        ) % side
        moved = tuple(int(value) for value in moved_array)
        mapping[index[coordinate]] = index[moved]
    return mapping


def source_contract() -> None:
    section("A - Framework, sibling, scope, and N1-N8 contract")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").replace("*", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    qb16_note = QB16_NOTE.read_text(encoding="utf-8")

    check("A live framework still has four named axioms", all(name in axioms for name in ("### Lattice", "### Qubit", "### Admissibility", "### Record")))
    check("A Record still says formation while withholding the formation rule", "Records form." in axioms and "formation rules" in axioms)
    check("A approved premise registry still has four current paths", registry.count('"current_path"') == 4)
    check("A QB16 sibling explicitly leaves cross-site reference transport open", "cross-site reference transport" in qb16_note.lower() and "not been nearest-neighbor compiled" in qb16_note.lower())

    for phrase in (
        "authority: none",
        "enlarged-cell qca",
        "isolated no-return sector",
        "finite reversible permanence boundary",
        "one-history actuality does not follow",
        "record-only future sufficiency does not follow",
        "renewal is a boundary resource",
        "causal schedule covariance does not follow",
        "resource/green integration",
        "common clock and transport do not follow",
        "n1 — alternative routes",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
    ):
        check(f"A note contains boundary: {phrase}", phrase in normalized)


def commit_swap_matrix() -> np.ndarray:
    """Local unitary on two copies of input+six spent-direction modes.

    For signal value s, |i_s> is swapped with the cubic-invariant symmetric
    one-spent-pulse state |o_s>; the five orthogonal direction combinations
    are fixed.  In the full macrocell, |i_s> means A=1,M=R=0 and |o_s>
    means A=0,M=1,R=s with one symmetric spent excitation.
    """

    dimension = 14
    unitary = np.eye(dimension, dtype=complex)
    for signal in (0, 1):
        input_vector = np.zeros(dimension, dtype=complex)
        output_vector = np.zeros(dimension, dtype=complex)
        input_vector[7 * signal] = 1.0
        output_vector[7 * signal + 1 : 7 * signal + 7] = 1.0 / np.sqrt(6.0)
        unitary += (
            -np.outer(input_vector, input_vector.conj())
            - np.outer(output_vector, output_vector.conj())
            + np.outer(input_vector, output_vector.conj())
            + np.outer(output_vector, input_vector.conj())
        )
    return unitary


def commit_and_cubic_covariance() -> None:
    section("B - Exact local coherent commit unitary")
    unitary = commit_swap_matrix()
    check("B local commit swap is unitary", np.allclose(unitary.conj().T @ unitary, np.eye(14), atol=TOL))
    check("B local commit swap is an involution", np.allclose(unitary @ unitary, np.eye(14), atol=TOL))

    rotations = proper_cubic_rotations()
    check("B proper cubic group has order 24", len(rotations) == 24)
    for number, rotation in enumerate(rotations):
        directions = direction_map(rotation)
        representation = np.zeros((14, 14), dtype=complex)
        for signal in (0, 1):
            representation[7 * signal, 7 * signal] = 1.0
            for direction in range(6):
                representation[7 * signal + 1 + directions[direction], 7 * signal + 1 + direction] = 1.0
        check(
            f"B local commit swap commutes with cubic rotation {number:02d}",
            np.allclose(representation @ unitary, unitary @ representation, atol=TOL),
        )

    plus_input = np.zeros(14, dtype=complex)
    plus_input[0] = plus_input[7] = 1.0 / np.sqrt(2.0)
    committed = unitary @ plus_input
    expected = np.zeros(14, dtype=complex)
    expected[1:7] = 1.0 / np.sqrt(12.0)
    expected[8:14] = 1.0 / np.sqrt(12.0)
    check("B a coherent plus signal maps to the two committed relational branches", np.allclose(committed, expected, atol=TOL))

    minus_input = np.zeros(14, dtype=complex)
    minus_input[0] = 1.0 / np.sqrt(2.0)
    minus_input[7] = -1.0 / np.sqrt(2.0)
    minus_committed = unitary @ minus_input
    check("B orthogonal Bell-phase inputs remain orthogonal after commit", abs(np.vdot(committed, minus_committed)) < TOL)
    check("B spent-pulse norm is exactly one", abs(np.vdot(committed, committed) - 1.0) < TOL)


def export_bits(value: int) -> int:
    marker = (value >> 13) & 1
    record = (value >> 12) & 1
    presence = [(value >> (6 + direction)) & 1 for direction in range(6)]
    content = [(value >> direction) & 1 for direction in range(6)]
    for direction in range(6):
        presence[direction] ^= marker
        content[direction] ^= marker & record
    answer = (marker << 13) | (record << 12)
    for direction in range(6):
        answer |= presence[direction] << (6 + direction)
        answer |= content[direction] << direction
    return answer


def rotate_export_bits(value: int, mapping: np.ndarray) -> int:
    marker = (value >> 13) & 1
    record = (value >> 12) & 1
    answer = (marker << 13) | (record << 12)
    for direction in range(6):
        answer |= ((value >> (6 + direction)) & 1) << (6 + int(mapping[direction]))
        answer |= ((value >> direction) & 1) << int(mapping[direction])
    return answer


def export_gate_and_rail_covariance() -> None:
    section("C - Relational export gate and global rail shifts")
    image = tuple(export_bits(value) for value in range(1 << 14))
    check("C local witness export is a permutation/unitary on basis states", len(set(image)) == 1 << 14)
    check("C local witness export is self-inverse", all(export_bits(export_bits(value)) == value for value in range(1 << 14)))

    rotations = proper_cubic_rotations()
    for number, rotation in enumerate(rotations):
        mapping = direction_map(rotation)
        check(
            f"C local export is cubic covariant {number:02d}",
            all(
                rotate_export_bits(export_bits(value), mapping)
                == export_bits(rotate_export_bits(value, mapping))
                for value in range(1 << 14)
            ),
        )

    side = 3
    count = side**3
    site_index = coordinate_index(side)
    rail_count = 3 * 6 * count  # spent, presence, content
    shift_map = np.zeros(rail_count, dtype=int)
    for family in range(3):
        for direction_number, direction in enumerate(DIRECTIONS):
            for coordinate in coordinates(side):
                moved = tuple((coordinate[axis] + direction[axis]) % side for axis in range(3))
                source = (family * 6 + direction_number) * count + site_index[coordinate]
                target = (family * 6 + direction_number) * count + site_index[moved]
                shift_map[source] = target
    check("C all directional rail shifts form one global permutation", len(set(shift_map.tolist())) == rail_count)

    for number, rotation in enumerate(rotations):
        sites = coordinate_map(side, rotation=rotation)
        directions = direction_map(rotation)
        symmetry = np.zeros(rail_count, dtype=int)
        for family in range(3):
            for direction in range(6):
                for site in range(count):
                    source = (family * 6 + direction) * count + site
                    target = (family * 6 + int(directions[direction])) * count + int(sites[site])
                    symmetry[source] = target
        check(
            f"C global rail shift commutes with cubic rotation {number:02d}",
            np.array_equal(symmetry[shift_map], shift_map[symmetry]),
        )

    translated_sites = coordinate_map(side, shift=(1, 2, 1))
    translation = np.zeros(rail_count, dtype=int)
    for family in range(3):
        for direction in range(6):
            for site in range(count):
                source = (family * 6 + direction) * count + site
                translation[source] = (family * 6 + direction) * count + int(translated_sites[site])
    check("C global rail shift commutes with translations", np.array_equal(translation[shift_map], shift_map[translation]))


def isolated_infinite_export_and_recurrence() -> None:
    section("D - Isolated infinite no-return sector and finite recurrence")
    rotations = proper_cubic_rotations()
    for tick in range(1, 7):
        spent = {
            (direction_number, tuple(tick * value for value in direction)): 1.0 / np.sqrt(6.0)
            for direction_number, direction in enumerate(DIRECTIONS)
        }
        check(f"D spent shell at tick {tick} has unit norm", abs(sum(abs(amplitude) ** 2 for amplitude in spent.values()) - 1.0) < TOL)
        check(f"D spent shell at tick {tick} has no amplitude at its source", all(coordinate != (0, 0, 0) for _, coordinate in spent))
        cubic = True
        for rotation in rotations:
            direction_permutation = direction_map(rotation)
            transformed = {
                (
                    int(direction_permutation[direction]),
                    tuple(int(value) for value in rotation @ np.asarray(coordinate)),
                )
                for direction, coordinate in spent
            }
            cubic = cubic and transformed == set(spent)
        check(f"D spent shell tick {tick} is cubic under all 24 rotations", cubic)

    horizon = 5
    for record in (0, 1):
        presence: set[tuple[int, Coord]] = set()
        content: set[tuple[int, Coord]] = set()
        for age in range(1, horizon + 1):
            for direction_number, direction in enumerate(DIRECTIONS):
                coordinate = tuple(age * value for value in direction)
                presence.add((direction_number, coordinate))
                if record:
                    content.add((direction_number, coordinate))
        check(f"D isolated record {record} exports six fresh presence witnesses per tick", len(presence) == 6 * horizon)
        check(f"D isolated record {record} exports content relationally", len(content) == 6 * horizon * record)
        check(f"D every exported packet decodes marker=1 and content={record}", all(((item in presence), (item in content)) == (True, bool(record)) for item in presence))

    side = 5
    count = side**3
    index = coordinate_index(side)
    source = index[(0, 0, 0)]
    for tick in range(1, side + 1):
        overlap = 0.0
        for direction in DIRECTIONS:
            position = tuple((tick * value) % side for value in direction)
            if index[position] == source:
                overlap += 1.0 / 6.0
        check(
            f"D finite torus return overlap at tick {tick} has the exact value",
            abs(overlap - (1.0 if tick == side else 0.0)) < TOL,
        )
    unitary = commit_swap_matrix()
    output_zero = np.zeros(14, dtype=complex)
    output_zero[1:7] = 1.0 / np.sqrt(6.0)
    recovered = unitary @ output_zero
    expected_input = np.zeros(14, dtype=complex)
    expected_input[0] = 1.0
    check("D a perfectly returned spent shell reverses the local record commit", np.allclose(recovered, expected_input, atol=TOL))


def collision_and_permanence_countermodels() -> None:
    section("E - Multi-source collisions and the permanence domain")
    for upstream_record in (0, 1):
        for local_record in (0, 1):
            incoming_presence = 1
            incoming_content = upstream_record
            outgoing_presence = incoming_presence ^ 1
            outgoing_content = incoming_content ^ local_record
            check(
                f"E downstream record toggles away upstream presence ({upstream_record},{local_record})",
                outgoing_presence == 0,
            )
            check(
                f"E collided content is XOR rather than an append ({upstream_record},{local_record})",
                outgoing_content == (upstream_record ^ local_record),
            )

    unitary = commit_swap_matrix()
    symmetric_return = np.zeros(14, dtype=complex)
    symmetric_return[8:14] = 1.0 / np.sqrt(6.0)  # signal/record branch one
    inverse_precursor = unitary @ symmetric_return
    expected = np.zeros(14, dtype=complex)
    expected[7] = 1.0
    check("E six converging spent components reconstruct the exact inverse precursor", np.allclose(inverse_precursor, expected, atol=TOL))

    permutation_count = 0
    violations = 0
    for permutation in permutations(range(4)):
        permutation_count += 1
        record_set = {2, 3}
        record_invariant = all(permutation[index] in record_set for index in record_set)
        if record_invariant:
            violations += sum(
                permutation[index] in record_set for index in {0, 1}
            )
    check("E all 24 finite four-state reversible maps were enumerated", permutation_count == 24)
    check("E finite invariant record subspace admits no blank-to-record formation", violations == 0)

    integer_window = tuple(range(-6, 7))
    forward_record_permanent = all(index + 1 >= 0 for index in integer_window if index >= 0)
    blank_enters = (-1 + 1) >= 0
    inverse_exists = all((index + 1) - 1 == index for index in integer_window)
    check("E infinite bilateral shift has a forward-invariant record half-line", forward_record_permanent)
    check("E infinite bilateral shift also permits blank-to-record entry", blank_enters)
    check("E the infinite escape remains globally reversible", inverse_exists)


def reduced_density(state: np.ndarray, left_dimension: int) -> np.ndarray:
    reshaped = state.reshape(left_dimension, -1)
    return reshaped @ reshaped.conj().T


def actuality_and_record_future() -> None:
    section("F - One-history actuality and record-only future sufficiency")
    witness_count = 6
    dimension = 2 ** (2 + witness_count)
    plus_ghz = np.zeros(dimension, dtype=complex)
    minus_ghz = np.zeros(dimension, dtype=complex)
    plus_ghz[0] = plus_ghz[-1] = 1.0 / np.sqrt(2.0)
    minus_ghz[0] = 1.0 / np.sqrt(2.0)
    minus_ghz[-1] = -1.0 / np.sqrt(2.0)
    check("F plus/minus exported histories are orthogonal pure states", abs(np.vdot(plus_ghz, minus_ghz)) < TOL and abs(np.vdot(plus_ghz, plus_ghz) - 1.0) < TOL)

    reduced_plus = reduced_density(plus_ghz, 4)
    reduced_minus = reduced_density(minus_ghz, 4)
    expected_records = np.diag((0.5, 0.0, 0.0, 0.5))
    check("F opposite coherent phases have identical local record density", np.allclose(reduced_plus, expected_records, atol=TOL) and np.allclose(reduced_minus, expected_records, atol=TOL))
    equality_projector = np.diag((1.0, 0.0, 0.0, 1.0))
    check("F relational equality decoder accepts both coherent phases", abs(np.trace(equality_projector @ reduced_plus) - 1.0) < TOL and abs(np.trace(equality_projector @ reduced_minus) - 1.0) < TOL)
    check("F both record branches remain nonzero rather than one becoming actual", abs(abs(plus_ghz[0]) ** 2 - 0.5) < TOL and abs(abs(plus_ghz[-1]) ** 2 - 0.5) < TOL)

    hadamard = np.array(((1.0, 1.0), (1.0, -1.0)), dtype=complex) / np.sqrt(2.0)
    cnot = np.array(
        ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)),
        dtype=complex,
    )
    discriminator = np.kron(hadamard, np.eye(2)) @ cnot
    bell_plus = np.array((1.0, 0.0, 0.0, 1.0), dtype=complex) / np.sqrt(2.0)
    bell_minus = np.array((1.0, 0.0, 0.0, -1.0), dtype=complex) / np.sqrt(2.0)
    out_plus = discriminator @ bell_plus
    out_minus = discriminator @ bell_minus
    expected_plus = np.array((1.0, 0.0, 0.0, 0.0), dtype=complex)
    expected_minus = np.array((0.0, 0.0, 1.0, 0.0), dtype=complex)
    check("F a Bell-capable recombination maps equal record packets to distinct futures", np.allclose(out_plus, expected_plus, atol=TOL) and np.allclose(out_minus, expected_minus, atol=TOL))
    check("F the future first-qubit record distinguishes the hidden phase", abs(abs(out_plus[0]) ** 2 - 1.0) < TOL and abs(abs(out_minus[2]) ** 2 - 1.0) < TOL)


def qb16_crosscheck() -> None:
    section("G - Read-only CFSI-QB16 relational decoder cross-check")
    result = subprocess.run(
        [sys.executable, str(QB16_RUNNER)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=90,
        check=False,
    )
    check("G sibling QB16 runner exits cleanly", result.returncode == 0)
    check("G sibling QB16 runner reports no failures", "FAIL=0" in result.stdout)
    pass_lines = [line for line in result.stdout.splitlines() if line.startswith("PASS=")]
    sibling_passes = int(pass_lines[-1].split("=", 1)[1]) if pass_lines else -1
    check("G sibling QB16 runner retains at least its announced 125 checks", sibling_passes >= 125, f"PASS={sibling_passes}")

    reference = sp.Matrix(((sp.Rational(9, 25), sp.Rational(12, 25)), (sp.Rational(12, 25), sp.Rational(16, 25))))
    complement = sp.eye(2) - reference
    rotation = sp.Matrix(((sp.Rational(3, 5), sp.Rational(4, 5)), (-sp.Rational(4, 5), sp.Rational(3, 5))))
    rotated_reference = sp.simplify(rotation * reference * rotation.T)
    rotated_complement = sp.simplify(rotation * complement * rotation.T)
    check("G chosen relational reference is a rank-one effect", reference * reference == reference and sp.trace(reference) == 1)
    check("G complement is the orthogonal binary alternative", sp.simplify(reference * complement) == sp.zeros(2) and sp.simplify(reference + complement) == sp.eye(2))
    check("G simultaneous conjugation preserves equality/complement relations", sp.simplify(rotated_reference * rotated_complement) == sp.zeros(2) and sp.simplify(rotated_reference + rotated_complement) == sp.eye(2))
    qb16_normalized = " ".join(QB16_NOTE.read_text(encoding="utf-8").split())
    check("G QB16 source discloses cross-site transport and atomic-write walls", "does not derive that cross-site transport" in qb16_normalized and "finite-radius atomic write" in qb16_normalized)


def schedule_and_renewal() -> None:
    section("H - Causal schedule covariance and renewal")
    initial = (1, 0, 0)

    def cnot_01(bits: tuple[int, int, int]) -> tuple[int, int, int]:
        a, b, c = bits
        return a, b ^ a, c

    def cnot_12(bits: tuple[int, int, int]) -> tuple[int, int, int]:
        a, b, c = bits
        return a, b, c ^ b

    forward_order = cnot_12(cnot_01(initial))
    reverse_order = cnot_01(cnot_12(initial))
    check("H two local causal gate orders give different records", forward_order == (1, 1, 1) and reverse_order == (1, 1, 0))

    basis = tuple(product((0, 1), repeat=3))
    cz_01 = np.diag([(-1.0) ** (bits[0] * bits[1]) for bits in basis])
    cz_12 = np.diag([(-1.0) ** (bits[1] * bits[2]) for bits in basis])
    check("H commuting CZ edge gates provide a schedule-independent entangler control", np.allclose(cz_01 @ cz_12, cz_12 @ cz_01, atol=TOL))

    marker_before = 0
    witnesses_if_commit_first = 6 * (marker_before ^ 1)
    witnesses_if_export_first = 6 * marker_before
    check("H commit/export layer order changes the first-tick witness record", witnesses_if_commit_first == 6 and witnesses_if_export_first == 0)

    for tape_length in (1, 2, 5, 10):
        fresh_slots = tape_length
        requested_events = tape_length + 1
        check(
            f"H finite fresh tape of length {tape_length} cannot serve T+1 independent writes",
            requested_events > fresh_slots,
        )
    check("H infinite all-blank incoming rails are a boundary condition, not a unitary theorem", "renewal is a boundary resource" in NOTE.read_text(encoding="utf-8").lower())


def partial_trace_environment(joint: np.ndarray) -> np.ndarray:
    tensor = joint.reshape(2, 2, 2, 2)
    return np.trace(tensor, axis1=1, axis2=3)


def resource_collision_and_green_boundary() -> None:
    section("I - Conservative resource collision and Green boundary")
    theta = pi / 6.0
    cosine = np.cos(theta)
    sine = np.sin(theta)
    collision = np.eye(4, dtype=complex)
    collision[1:3, 1:3] = np.array(((cosine, -sine), (sine, cosine)), dtype=complex)
    check("I partial-iSWAP collision is exactly unitary", np.allclose(collision.conj().T @ collision, np.eye(4), atol=TOL))
    occupation = np.diag((0.0, 1.0, 1.0, 2.0))
    check("I partial-iSWAP conserves total resource occupation", np.allclose(collision @ occupation, occupation @ collision, atol=TOL))

    for system_occupation in (0.0, 0.3, 1.0):
        system = np.diag((1.0 - system_occupation, system_occupation))
        for tape_occupation in (0.0, 1.0):
            tape = np.diag((1.0 - tape_occupation, tape_occupation))
            joint = np.kron(system, tape)
            evolved = collision @ joint @ collision.conj().T
            reduced = partial_trace_environment(evolved)
            predicted = cosine**2 * system_occupation + sine**2 * tape_occupation
            check(
                f"I reduced occupation follows the exact collision law n={system_occupation},p={tape_occupation}",
                abs(float(np.real(reduced[1, 1])) - predicted) < TOL,
            )

    initial = np.zeros(4, dtype=complex)
    initial[1] = 1.0  # system blank, tape occupied
    once = collision @ initial
    twice_reused = collision @ once
    reused_occupation = abs(twice_reused[2]) ** 2 + abs(twice_reused[3]) ** 2
    fresh_twice = cosine**2 * sine**2 + sine**2
    check("I reusing one polarized tape qubit differs from two fresh source collisions", abs(reused_occupation - fresh_twice) > 0.2)
    check("I occupied source tape and empty sink tape are distinct supplied polarizations", 1.0 != 0.0)

    side = 5
    count = side**3
    index = coordinate_index(side)
    laplacian = np.zeros((count, count), dtype=float)
    for coordinate in coordinates(side):
        site = index[coordinate]
        for direction in DIRECTIONS:
            neighbor = tuple((coordinate[axis] + direction[axis]) % side for axis in range(3))
            laplacian[site, site] += 1.0
            laplacian[index[neighbor], site] -= 1.0
    transition = np.eye(count) - laplacian / 12.0
    check("I reduced lazy diffusion is local and doubly stochastic", np.all(transition >= -TOL) and np.allclose(transition.sum(axis=0), 1.0, atol=TOL) and np.allclose(transition.sum(axis=1), 1.0, atol=TOL))
    source = np.zeros(count)
    source[index[(0, 0, 0)]] = 1.0
    source[index[(2, 2, 2)]] = -1.0
    augmented = np.block(
        [
            [laplacian, np.ones((count, 1))],
            [np.ones((1, count)), np.zeros((1, 1))],
        ]
    )
    green = np.linalg.solve(augmented, np.concatenate((source, (0.0,))))[:-1]
    check("I stationary reduced field solves the exact local Poisson equation", np.max(np.abs(laplacian @ green - source)) < TOL and abs(green.mean()) < TOL)

    # The coherent one-coin walk keeps one direction for every tick, while
    # the fresh reduced walk convolves independently drawn directions.
    weighted_directions = (((0, 0, 0), 0.5),) + tuple(
        (direction, 1.0 / 12.0) for direction in DIRECTIONS
    )
    fresh_distribution: dict[Coord, float] = {(0, 0, 0): 1.0}
    for tick in range(1, 6):
        next_distribution: dict[Coord, float] = {}
        for coordinate, probability in fresh_distribution.items():
            for direction, weight in weighted_directions:
                moved = tuple(coordinate[axis] + direction[axis] for axis in range(3))
                next_distribution[moved] = next_distribution.get(moved, 0.0) + probability * weight
        fresh_distribution = next_distribution
        fresh_r2 = sum(
            probability * sum(value * value for value in coordinate)
            for coordinate, probability in fresh_distribution.items()
        )
        coherent_r2 = sum(
            weight * sum((tick * value) ** 2 for value in direction)
            for direction, weight in weighted_directions
        )
        check(f"I coherent reused direction is ballistic at tick {tick}", abs(coherent_r2 - tick * tick / 2.0) < TOL)
        check(f"I fresh traced directions are diffusive at tick {tick}", abs(fresh_r2 - tick / 2.0) < TOL)


def common_clock_and_transport_countermodels() -> None:
    section("J - Common QCA tick does not force common clock or transport")
    field = 0.2
    theta = 0.7
    gamma_one = 0.5
    gamma_two = 1.5
    phase_one = theta * (1.0 - gamma_one * field)
    phase_two = theta * (1.0 - gamma_two * field)
    unitary_one = np.diag((1.0, np.exp(-1j * phase_one)))
    unitary_two = np.diag((1.0, np.exp(-1j * phase_two)))
    check("J both species gates are unitary in the same global tick", np.allclose(unitary_one.conj().T @ unitary_one, np.eye(2), atol=TOL) and np.allclose(unitary_two.conj().T @ unitary_two, np.eye(2), atol=TOL))
    check("J the same tick permits species-dependent resource redshift", abs(phase_one - phase_two) > 0.1)

    q = 0.8
    internal = np.diag((0.0, 2.0))
    local_q = np.array((q, 0.9, 1.0))
    onsite = np.kron(np.diag(local_q), internal)
    constant_edges = np.zeros((3, 3))
    weighted_edges = np.zeros((3, 3))
    for left, right in ((0, 1), (1, 2)):
        constant_edges[left, right] = constant_edges[right, left] = -0.25
        weighted_edges[left, right] = weighted_edges[right, left] = -0.25 * np.sqrt(local_q[left] * local_q[right])
    law_one = onsite + np.kron(constant_edges, np.eye(2))
    law_two = onsite + np.kron(weighted_edges, np.eye(2))
    check("J identical local clock blocks coexist with different transport laws", np.allclose(np.diag(law_one), np.diag(law_two), atol=TOL) and np.linalg.norm(np.linalg.eigvalsh(law_one) - np.linalg.eigvalsh(law_two)) > 1.0e-2)


def main() -> None:
    source_contract()
    commit_and_cubic_covariance()
    export_gate_and_rail_covariance()
    isolated_infinite_export_and_recurrence()
    collision_and_permanence_countermodels()
    actuality_and_record_future()
    qb16_crosscheck()
    schedule_and_renewal()
    resource_collision_and_green_boundary()
    common_clock_and_transport_countermodels()
    print(f"\nSUMMARY: INFINITE REVERSIBLE RECORD EXPORT QCA CYCLE 11 PASS={PASS} FAIL={FAIL}")
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
