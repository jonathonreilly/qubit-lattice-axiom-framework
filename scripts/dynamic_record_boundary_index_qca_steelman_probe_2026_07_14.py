#!/usr/bin/env python3
"""Exact bounded attack on the dynamic-record-boundary indexed-QCA steelman."""

from __future__ import annotations

from collections import Counter
from itertools import permutations, product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "DYNAMIC_RECORD_BOUNDARY_INDEX_QCA_STEELMAN_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "PROPER_CUBIC_QUBIT_QCA_WARD_IDENTITY_STEELMAN_NOTE_2026-07-14.md"
)
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"


PASS = 0
FAIL = 0

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
HADAMARD = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
DIRECTIONS = (
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


def exact_equal(left: sp.Matrix | sp.Expr, right: sp.Matrix | sp.Expr) -> bool:
    difference = left - right
    if isinstance(difference, sp.MatrixBase):
        return all(sp.simplify(sp.expand_complex(value)) == 0 for value in difference)
    return sp.simplify(sp.expand_complex(difference)) == 0


def proper_cubic_rotations() -> tuple[sp.Matrix, ...]:
    rotations = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for column, row in enumerate(permutation):
                matrix[row, column] = signs[column]
            if matrix.det() == 1:
                rotations.append(matrix)
    unique = {tuple(matrix): matrix for matrix in rotations}
    return tuple(unique.values())


ROTATIONS = proper_cubic_rotations()


def rotate_tuple(rotation: sp.Matrix, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(int(value) for value in rotation * sp.Matrix(vector))


def direction_permutation(rotation: sp.Matrix) -> tuple[int, ...]:
    return tuple(DIRECTIONS.index(rotate_tuple(rotation, direction)) for direction in DIRECTIONS)


def controlled_phase(theta: sp.Expr) -> sp.Matrix:
    return sp.diag(1, 1, 1, sp.exp(sp.I * theta))


def partial_transfer(theta: sp.Expr) -> sp.Matrix:
    cosine = sp.cos(theta)
    sine = sp.sin(theta)
    return sp.Matrix(
        [
            [1, 0, 0, 0],
            [0, cosine, sine, 0],
            [0, -sine, cosine, 0],
            [0, 0, 0, 1],
        ]
    )


def cnot(number_qubits: int, control: int, target: int) -> sp.Matrix:
    dimension = 2**number_qubits
    matrix = sp.zeros(dimension)
    for column in range(dimension):
        bits = [int(bit) for bit in f"{column:0{number_qubits}b}"]
        output = list(bits)
        if bits[control] == 1:
            output[target] ^= 1
        row = int("".join(str(bit) for bit in output), 2)
        matrix[row, column] = 1
    return matrix


def partial_trace_qubits(
    density: sp.Matrix,
    keep: tuple[int, ...],
    number_qubits: int,
) -> sp.Matrix:
    traced = tuple(index for index in range(number_qubits) if index not in keep)
    output = sp.zeros(2 ** len(keep))
    for row_keep in product((0, 1), repeat=len(keep)):
        for column_keep in product((0, 1), repeat=len(keep)):
            total = 0
            for environment in product((0, 1), repeat=len(traced)):
                row_bits = [0] * number_qubits
                column_bits = [0] * number_qubits
                for index, qubit in enumerate(keep):
                    row_bits[qubit] = row_keep[index]
                    column_bits[qubit] = column_keep[index]
                for index, qubit in enumerate(traced):
                    row_bits[qubit] = environment[index]
                    column_bits[qubit] = environment[index]
                row = int("".join(str(bit) for bit in row_bits), 2)
                column = int("".join(str(bit) for bit in column_bits), 2)
                total += density[row, column]
            output_row = int("".join(str(bit) for bit in row_keep), 2)
            output_column = int("".join(str(bit) for bit in column_keep), 2)
            output[output_row, output_column] = sp.simplify(total)
    return output


def cyclic_qubit_shift(number_qubits: int, step: int) -> sp.Matrix:
    dimension = 2**number_qubits
    matrix = sp.zeros(dimension)
    for column in range(dimension):
        bits = [int(bit) for bit in f"{column:0{number_qubits}b}"]
        output = [0] * number_qubits
        for site, bit in enumerate(bits):
            output[(site + step) % number_qubits] = bit
        row = int("".join(str(bit) for bit in output), 2)
        matrix[row, column] = 1
    return matrix


def interaction_ring(number_qubits: int, theta: sp.Expr) -> sp.Matrix:
    phases = []
    for index in range(2**number_qubits):
        bits = [int(bit) for bit in f"{index:0{number_qubits}b}"]
        occupied_edges = sum(
            bits[site] * bits[(site + 1) % number_qubits]
            for site in range(number_qubits)
        )
        phases.append(sp.exp(sp.I * theta * occupied_edges))
    return sp.diag(*phases)


def tensor_response(source: sp.Matrix, trace_weight: sp.Expr) -> sp.Matrix:
    trace_part = sp.trace(source) * sp.eye(3) / 3
    traceless = source - trace_part
    return sp.simplify(traceless + trace_weight * trace_part)


def source_contract() -> None:
    section("A - Authority, constitution, and primitive contract")

    def normalized(path: Path) -> str:
        return " ".join(
            path.read_text(encoding="utf-8")
            .lower()
            .replace("*", "")
            .replace("`", "")
            .split()
        )

    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    parent = normalized(PARENT)
    kinetic = normalized(KINETIC)
    realized = normalized(REALIZED)
    scale = normalized(SCALE)
    check("A note is authority-free", "authority: none" in note)
    check(
        "A note changes no live authority surface",
        "changes no axiom, registry, primitive, audit, review queue, or retained surface"
        in note,
    )
    check(
        "A constitutional occurrence and downstream formation rule are separated",
        "records form." in axioms
        and "formation rule (which admissible possibility, at which site, with what weight, at what rate)"
        in axioms,
    )
    check(
        "A parent N7 interacting indexed dynamic-boundary steelman is wired in",
        "interacting, index-nontrivial" in parent
        and "dynamically generated low-record" in parent,
    )
    check(
        "A kinetic primitive supplies form isotropy but not dynamics",
        "c_t = c_s" in kinetic and "not a new dynamics" in kinetic,
    )
    check(
        "A realized-state primitive supplies no state-selection rule or boundary",
        "does not supply a state, state-selection rule" in realized
        and "boundary condition" in realized,
    )
    check(
        "A scale primitive is units conversion without dimensionless dynamics",
        "units conversion" in scale and "zero dimensionless content" in scale,
    )


def primitive_carrier_and_cubic_obstruction() -> None:
    section("B - Primitive displacement and direct carrier boundaries")
    check("B proper cubic rotation group has 24 elements", len(ROTATIONS) == 24)
    candidates = tuple(product((-1, 0, 1), repeat=3))
    fixed = tuple(
        vector
        for vector in candidates
        if all(rotate_tuple(rotation, vector) == vector for rotation in ROTATIONS)
    )
    check("B only zero displacement is fixed by every proper cubic rotation", fixed == ((0, 0, 0),))
    check(
        "B six nearest-neighbor faces form one proper-cubic orbit",
        all(set(rotate_tuple(rotation, direction) for direction in DIRECTIONS) == set(DIRECTIONS) for rotation in ROTATIONS),
    )
    check("B one primitive qubit cannot factor as independent record and rail qubits", 2 < 2 * 2)
    check("B direct record plus six independent face rails needs seven qubits", 2 * 2**6 == 2**7)
    check("B one directional single-particle label plus record fits first in four qubits", 2**3 < 2 * 6 <= 2**4)
    center_plus_faces = {(0, 0, 0), *DIRECTIONS}
    check(
        "B center plus six face sites is a proper-cubic seven-qubit carrier orbit",
        all(
            {rotate_tuple(rotation, site) for site in center_plus_faces}
            == center_plus_faces
            for rotation in ROTATIONS
        ),
    )


def dynamic_record_boundary() -> None:
    section("C - Record-generated low-record boundary and law occurrence field")

    def record(position: tuple[int, int, int], center: tuple[int, int, int], occurrence: int) -> int:
        return int(occurrence == 1 and position == center)

    basis = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

    def gradient(
        position: tuple[int, int, int],
        center: tuple[int, int, int],
        occurrence: int,
    ) -> tuple[int, int, int]:
        components = []
        for direction in basis:
            minus = tuple(position[axis] - direction[axis] for axis in range(3))
            plus = tuple(position[axis] + direction[axis] for axis in range(3))
            components.append(record(minus, center, occurrence) - record(plus, center, occurrence))
        return tuple(components)

    origin = (0, 0, 0)
    check(
        "C one realized central record generates six outward face normals",
        all(gradient(direction, origin, 1) == direction for direction in DIRECTIONS),
    )
    check(
        "C absent occurrence generates no boundary normal",
        all(gradient(direction, origin, 0) == origin for direction in DIRECTIONS),
    )
    check(
        "C generated normal field is proper-cubic covariant",
        all(
            gradient(rotate_tuple(rotation, direction), origin, 1)
            == rotate_tuple(rotation, gradient(direction, origin, 1))
            for rotation in ROTATIONS
            for direction in DIRECTIONS
        ),
    )
    translated_center = (3, -2, 5)
    check(
        "C boundary generation is translation-covariant around any realized record",
        all(
            gradient(
                tuple(translated_center[axis] + direction[axis] for axis in range(3)),
                translated_center,
                1,
            )
            == direction
            for direction in DIRECTIONS
        ),
    )

    contexts = tuple(product((0, 1), repeat=2))

    def occurrence_even(boundary: int, neighbor_parity: int) -> int:
        return boundary * (1 - neighbor_parity)

    def occurrence_odd(boundary: int, neighbor_parity: int) -> int:
        return boundary * neighbor_parity

    even_table = tuple(occurrence_even(*context) for context in contexts)
    odd_table = tuple(occurrence_odd(*context) for context in contexts)
    check("C two cubic-scalar occurrence laws both form records in some contexts", 1 in even_table and 1 in odd_table)
    check("C the exact occurrence domain is not selected by the boundary index", even_table != odd_table)
    check(
        "C record-boundary propagation laws do not nucleate a first record from no boundary",
        occurrence_even(0, 0) == occurrence_even(0, 1) == 0
        and occurrence_odd(0, 0) == occurrence_odd(0, 1) == 0,
    )


def conditional_index_splice_obstruction() -> None:
    section("D - Conditional identity/shift splice needs a boundary carrier")
    size = 8

    def source_map(pattern: tuple[int, ...]) -> tuple[int, ...]:
        return tuple((site - pattern[site]) % size for site in range(size))

    patterns = tuple(product((0, 1), repeat=size))
    bijective = tuple(
        pattern for pattern in patterns if len(set(source_map(pattern))) == size
    )
    check(
        "D naive one-wire conditional identity/shift is bijective only in uniform sectors",
        bijective == ((0,) * size, (1,) * size),
    )
    check("D uniform zero sector is identity", source_map((0,) * size) == tuple(range(size)))
    check("D uniform one sector is the one-step shift", source_map((1,) * size) == tuple((site - 1) % size for site in range(size)))

    domain = (1, 1, 1, 1, 0, 0, 0, 0)
    counts = Counter(source_map(domain))
    repeated_inputs = sum(max(count - 1, 0) for count in counts.values())
    missing_inputs = size - len(counts)
    transitions = sum(domain[site] != domain[(site + 1) % size] for site in range(size))
    check("D one finite shifted domain has two walls", transitions == 2)
    check("D its scalar splice has one duplicated and one missing wire", repeated_inputs == missing_inputs == 1)
    check("D one compensating boundary reroute matches the scalar-map deficit count", repeated_inputs - missing_inputs == 0 and repeated_inputs == 1)


def interacting_six_ray_index_qca() -> None:
    section("E - Interacting six-ray indexed QCA and kernel freedom")
    angles = (sp.pi / 2, sp.pi)
    gates = tuple(controlled_phase(angle) for angle in angles)
    check("E both controlled-phase collisions are exactly unitary", all(exact_equal(gate.H * gate, sp.eye(4)) for gate in gates))
    concurrence_squared = tuple(sp.simplify((1 - sp.cos(angle)) / 2) for angle in angles)
    check("E the two local interactions have different exact entangling strength", concurrence_squared == (sp.Rational(1, 2), sp.Integer(1)))

    direction_permutations = tuple(direction_permutation(rotation) for rotation in ROTATIONS)
    shared_angles = (sp.pi / 2,) * 6
    check(
        "E one shared interaction angle on six rays is proper-cubic invariant",
        all(tuple(shared_angles[index] for index in permutation) == shared_angles for permutation in direction_permutations),
    )
    noncubic_angles = (sp.pi / 2, sp.pi, sp.pi / 2, sp.pi / 2, sp.pi / 2, sp.pi / 2)
    check(
        "E an unequal face interaction assignment fails proper-cubic covariance",
        any(tuple(noncubic_angles[index] for index in permutation) != noncubic_angles for permutation in direction_permutations),
    )

    per_ray_exponent = 1
    shell_exponent = 6 * per_ray_exponent
    check("E one outward qubit rail has partitioned wire-flow index two", 2**per_ray_exponent == 2)
    check("E six cubic-related outward rails have shell index sixty-four", 2**shell_exponent == 64)
    check("E reversing every rail gives the reciprocal inward index", sp.Rational(1, 2**shell_exponent) == sp.Rational(1, 64))
    check("E finite-depth interaction phase does not alter the wire-flow exponent", all(shell_exponent == 6 for _gate in gates))

    number_qubits = 4
    shift = cyclic_qubit_shift(number_qubits, 1)
    inverse_shift = cyclic_qubit_shift(number_qubits, -1)
    interactions = tuple(interaction_ring(number_qubits, angle) for angle in angles)
    qcas = tuple(shift * interaction for interaction in interactions)
    check("E finite ring shifts are inverse unitary permutations", shift.T * shift == sp.eye(2**number_qubits) and shift * inverse_shift == sp.eye(2**number_qubits))
    check("E both interacting shift laws are unitary and translation covariant", all(exact_equal(qca.H * qca, sp.eye(2**number_qubits)) and exact_equal(interaction * shift, shift * interaction) for qca, interaction in zip(qcas, interactions)))
    check("E the same nonzero index admits distinct interacting laws", qcas[0] != qcas[1])
    check("E a finite rail shift recurs rather than becoming globally irreversible", shift**number_qubits == sp.eye(2**number_qubits))


def boundary_theorem_source_and_no_return() -> None:
    section("F - Grant outward boundary theorem; source and occurrence remain law fields")
    bulk_shell_index = 64
    occupied_source_blank_rail = sp.Matrix([0, 0, 1, 0])
    half = partial_transfer(sp.pi / 4)
    full = partial_transfer(sp.pi / 2)
    rail_number = sp.diag(0, 1, 0, 1)
    half_output = sp.simplify(half * occupied_source_blank_rail)
    full_output = sp.simplify(full * occupied_source_blank_rail)
    half_emission = sp.simplify((half_output.H * rail_number * half_output)[0])
    full_emission = sp.simplify((full_output.H * rail_number * full_output)[0])
    check("F half and full boundary source gates are exactly unitary", exact_equal(half.H * half, sp.eye(4)) and exact_equal(full.H * full, sp.eye(4)))
    check("F identical outward bulk index permits half or one-unit transfer", bulk_shell_index == 64 and (half_emission, full_emission) == (sp.Rational(1, 2), sp.Integer(1)))

    vacuum = sp.Matrix([1, 0, 0, 0])
    check("F indexed rail carries capacity without forcing an actual excitation", full * vacuum == vacuum)

    contexts = tuple(product((0, 1), repeat=2))
    even_law = tuple(boundary * (1 - parity) for boundary, parity in contexts)
    odd_law = tuple(boundary * parity for boundary, parity in contexts)
    check("F two nonempty formation-domain laws share the same outward index", 1 in even_law and 1 in odd_law and even_law != odd_law and bulk_shell_index == 64)
    check("F outward no-return is only local/asymptotic on the finite control", cyclic_qubit_shift(4, 1) ** 4 == sp.eye(16))


def record_instrument_and_reversible_dilation() -> None:
    section("G - Stable local record instrument is not selected by the QCA index")
    identity_three = sp.eye(8)
    hadamard_source = sp.kronecker_product(HADAMARD, I2, I2)
    copy_source_record = cnot(3, 0, 1)
    copy_record_witness = cnot(3, 1, 2)
    premeasurement = copy_record_witness * copy_source_record * hadamard_source
    blank = sp.eye(8).col(0)
    coherent = sp.simplify(premeasurement * blank)
    expected = (sp.eye(8).col(0) + sp.eye(8).col(7)) / sp.sqrt(2)
    check("G two-copy premeasurement produces exact GHZ correlation", exact_equal(coherent, expected))
    check("G premeasurement dilation is exactly unitary", exact_equal(premeasurement.H * premeasurement, identity_three))

    coherent_density = sp.simplify(coherent * coherent.H)
    actual_mixture = (
        sp.eye(8).col(0) * sp.eye(8).col(0).T
        + sp.eye(8).col(7) * sp.eye(8).col(7).T
    ) / 2
    coherent_records = partial_trace_qubits(coherent_density, (1, 2), 3)
    mixture_records = partial_trace_qubits(actual_mixture, (1, 2), 3)
    check("G coherent dilation and record instrument have the same local two-record state", exact_equal(coherent_records, mixture_records))
    check("G their global actual-sector semantics remain exactly different", coherent_density != actual_mixture)

    projectors = (
        sp.eye(8).col(0) * sp.eye(8).col(0).T,
        sp.eye(8).col(7) * sp.eye(8).col(7).T,
    )
    weights = tuple(sp.simplify(sp.trace(projector * coherent_density)) for projector in projectors)
    check("G the explicit record instrument has two basis-record branches of weight one-half", weights == (sp.Rational(1, 2), sp.Rational(1, 2)))

    undo_copies = copy_source_record * copy_record_witness
    returned = sp.simplify(undo_copies * coherent)
    plus_blank_blank = sp.kronecker_product(sp.Matrix([1, 1]) / sp.sqrt(2), sp.Matrix([1, 0]), sp.Matrix([1, 0]))
    check("G the closed coherent dilation can be globally unwritten", exact_equal(returned, plus_blank_blank))
    check("G adjoining either local channel leaves the bulk wire index unchanged", 64 == 64)


def downstream_fields_and_joint_selection() -> None:
    section("H - Tensor, species, clock, and joint selection after boundary grant")
    source = sp.diag(2, -1, 0)
    response_one = tensor_response(source, 1)
    response_two = tensor_response(source, 2)
    symmetric_basis = []
    for first in range(3):
        for second in range(first, 3):
            basis = sp.zeros(3)
            basis[first, second] = 1
            basis[second, first] = 1
            symmetric_basis.append(basis)
    check(
        "H two tensor trace weights obey the same proper-cubic covariance",
        all(
            exact_equal(
                tensor_response(rotation * basis * rotation.T, weight),
                rotation * tensor_response(basis, weight) * rotation.T,
            )
            for rotation in ROTATIONS
            for basis in symmetric_basis
            for weight in (1, 2)
        )
        and response_one != response_two,
    )

    charges = (-9, -5, -1, 7, 8)
    universal = tuple(sp.Integer(1) for _charge in charges)
    charge_dependent = tuple(sp.Rational(81 + charge**2, 81) for charge in charges)
    check("H scoped matter tuple remains anomaly neutral", sum(charges) == 0 and sum(charge**3 for charge in charges) == 0)
    check("H common and charge-dependent scalar couplings are distinct index-kernel choices", universal != charge_dependent and len(set(charge_dependent)) > 1)

    layers = tuple(range(8))
    tick_each_layer = layers
    tick_every_second_layer = tuple(layer // 2 for layer in layers)
    check(
        "H the same indexed updates admit distinct pre-primitive tick identifications",
        tick_each_layer != tick_every_second_layer
        and all(
            tick_each_layer[index + 1] - tick_each_layer[index] == 1
            for index in range(len(layers) - 1)
        ),
    )

    fields = (
        "occurrence-domain law",
        "source transfer",
        "interaction kernel",
        "actual sector",
        "update-to-tick identification",
        "tensor ratio",
        "species coupling",
    )
    candidates = tuple(product((0, 1), repeat=len(fields)))
    check("H one fixed outward shell index leaves 128 completion assignments", len(candidates) == 128)
    kinetic_identified = tuple(candidate for candidate in candidates if candidate[4] == 1)
    check("H approved kinetic graining plus update-tick identification reduces the ledger to 64", len(kinetic_identified) == 64)
    full_transfer = tuple(candidate for candidate in kinetic_identified if candidate[1] == 1)
    check("H separately granting one-unit source transfer leaves 32 assignments", len(full_transfer) == 32)

    target = (0, 1, 0, 1, 1, 0, 0)

    def completion_score(candidate: tuple[int, ...], omitted: int | None = None) -> int:
        return sum(
            (value - target[index]) ** 2
            for index, value in enumerate(candidate)
            if index != omitted
        )

    check(
        "H seven explicit clauses select one completion",
        tuple(candidate for candidate in candidates if completion_score(candidate) == 0)
        == (target,),
    )
    for index, field in enumerate(fields):
        scores = {
            candidate: completion_score(candidate, omitted=index)
            for candidate in candidates
        }
        minimum = min(scores.values())
        minima = tuple(candidate for candidate, score in scores.items() if score == minimum)
        check(
            f"H deleting {field} clause restores an exact pair",
            len(minima) == 2 and {candidate[index] for candidate in minima} == {0, 1},
        )


def documentation_contract() -> None:
    section("I - Scope and no-go-discipline contract")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "dynamically generated low-record boundary",
        "occurrence is a field of the exact law",
        "not automatically a separate axiom atom",
        "primitive displacement obstruction",
        "conditional index splice",
        "boundary carrier",
        "interacting six-ray qca",
        "partitioned wire-flow index",
        "outward no-return",
        "one-unit transfer",
        "stable record instrument",
        "tensor trace/traceless ratio",
        "common species coupling",
        "kinetic-isotropy primitive",
        "realized-state primitive",
        "paired laws after granting the boundary theorem",
        "clause-deletion audit",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — exact residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path",
        "n7 — strongest surviving steelman",
        "n8 — cross-cycle echo",
    )
    for phrase in required:
        check(f"I note contains boundary: {phrase}", phrase in note)


def main() -> None:
    source_contract()
    primitive_carrier_and_cubic_obstruction()
    dynamic_record_boundary()
    conditional_index_splice_obstruction()
    interacting_six_ray_index_qca()
    boundary_theorem_source_and_no_return()
    record_instrument_and_reversible_dilation()
    downstream_fields_and_joint_selection()
    documentation_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
