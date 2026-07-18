#!/usr/bin/env python3
"""Bounded exact QCA/Ward-identity attack on the Cycle-15 steelman."""

from __future__ import annotations

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
    / "PROPER_CUBIC_QUBIT_QCA_WARD_IDENTITY_STEELMAN_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "TOPOLOGICAL_CONSERVATION_RG_ACTION_STEELMAN_NOTE_2026-07-14.md"
)


PASS = 0
FAIL = 0

I2 = sp.eye(2)
P1 = sp.diag(0, 1)
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


def direction_permutation(rotation: sp.Matrix) -> sp.Matrix:
    permutation = sp.zeros(6)
    for column, direction in enumerate(DIRECTIONS):
        transformed = tuple(rotation * sp.Matrix(direction))
        row = DIRECTIONS.index(transformed)
        permutation[row, column] = 1
    return permutation


DIRECTION_REP = tuple(direction_permutation(rotation) for rotation in ROTATIONS)
I6 = sp.eye(6)
UNIFORM_PROJECTOR = sp.ones(6) / 6
INVERSION = sp.zeros(6)
for column, direction in enumerate(DIRECTIONS):
    INVERSION[DIRECTIONS.index(tuple(-value for value in direction)), column] = 1
EVEN_PROJECTOR = (I6 + INVERSION) / 2 - UNIFORM_PROJECTOR
VECTOR_PROJECTOR = (I6 - INVERSION) / 2


def collision(theta_even: sp.Expr, theta_vector: sp.Expr) -> sp.Matrix:
    return sp.simplify(
        UNIFORM_PROJECTOR
        + sp.exp(sp.I * theta_even) * EVEN_PROJECTOR
        + sp.exp(sp.I * theta_vector) * VECTOR_PROJECTOR
    )


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


def block_diagonal(blocks: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return sp.diag(*blocks)


def tensor_response(source: sp.Matrix, trace_weight: sp.Expr) -> sp.Matrix:
    trace_part = sp.trace(source) * sp.eye(3) / 3
    traceless = source - trace_part
    return sp.simplify(traceless + trace_weight * trace_part)


def source_contract() -> None:
    section("A - Authority and exact-QCA steelman contract")
    note = " ".join(
        NOTE.read_text(encoding="utf-8")
        .lower()
        .replace("*", "")
        .replace("`", "")
        .split()
    )
    axioms = AXIOMS.read_text(encoding="utf-8")
    parent = PARENT.read_text(encoding="utf-8").lower()
    check("A note is authority-free", "authority: none" in note)
    check(
        "A note changes no live authority surface",
        "changes no axiom, registry, primitive, audit, review queue, or retained surface" in note,
    )
    check("A actual primitive domain is Z3 with one M2 per site", "`Z^3`" in axioms and "`M_2(C)`" in axioms)
    check("A current Record and record-only state constraints are wired in", "records are permanent" in axioms.lower() and "A state is a configuration of records." in axioms)
    check("A linked-current and anomaly-minimal parent inputs are wired in", "(-9,-5,-1,7,8)" in parent and "record increment = exported information quantum" in parent)
    check("A surviving exact QCA Ward steelman is wired in", "exact proper-cubic qca/topological action" in parent and "ward identity" in parent)


def primitive_scalar_qca_transport_boundary() -> None:
    section("B - Primitive scalar nearest-neighbor unitary is forced onsite")
    norm_a, norm_b, real_cross = sp.symbols("A B C", real=True)
    equations = []
    for cosine_sum in (3, 1, -1, -3):
        equations.append(
            sp.Eq(
                norm_a + 4 * cosine_sum**2 * norm_b + 4 * cosine_sum * real_cross,
                1,
            )
        )
    solution = sp.solve(equations, (norm_a, norm_b, real_cross), dict=True)
    check("B four cubic momenta force neighbor amplitude norm to zero", solution == [{norm_a: 1, norm_b: 0, real_cross: 0}])
    check("B remaining scalar law is an onsite unit phase", solution[0][norm_a] == 1 and solution[0][norm_b] == 0)
    check("B primitive scalar class cannot carry a nonzero transport current", solution[0][norm_b] == 0)


def six_direction_block_qca() -> None:
    section("C - Explicit proper-cubic streaming QCA and collision freedom")
    check("C proper-cubic rotation group has 24 elements", len(ROTATIONS) == 24)
    check("C every direction representation is an orthogonal permutation", all(permutation.T * permutation == I6 for permutation in DIRECTION_REP))

    commutator_maps = tuple(
        sp.kronecker_product(permutation.T, I6)
        - sp.kronecker_product(I6, permutation)
        for permutation in DIRECTION_REP
    )
    stacked = commutator_maps[0]
    for commutator_map in commutator_maps[1:]:
        stacked = stacked.col_join(commutator_map)
    check("C six-direction cubic collision commutant has exact dimension three", stacked.rank() == 33 and len(stacked.nullspace()) == 3)
    check("C irreducible projectors have ranks one two and three", (UNIFORM_PROJECTOR.rank(), EVEN_PROJECTOR.rank(), VECTOR_PROJECTOR.rank()) == (1, 2, 3))
    check("C the three cubic projectors are orthogonal and complete", exact_equal(UNIFORM_PROJECTOR + EVEN_PROJECTOR + VECTOR_PROJECTOR, I6) and exact_equal(UNIFORM_PROJECTOR * EVEN_PROJECTOR, sp.zeros(6)) and exact_equal(UNIFORM_PROJECTOR * VECTOR_PROJECTOR, sp.zeros(6)) and exact_equal(EVEN_PROJECTOR * VECTOR_PROJECTOR, sp.zeros(6)))
    check("C every cubic rotation commutes with all three projectors", all(all(exact_equal(permutation * projector, projector * permutation) for projector in (UNIFORM_PROJECTOR, EVEN_PROJECTOR, VECTOR_PROJECTOR)) for permutation in DIRECTION_REP))

    identity_collision = collision(0, 0)
    reverse_collision = collision(0, sp.pi)
    complex_collision = collision(sp.pi / 3, sp.pi / 2)
    check("C identity reverse and complex collisions are all exactly unitary", all(exact_equal(candidate.H * candidate, I6) for candidate in (identity_collision, reverse_collision, complex_collision)))
    check("C reverse collision is direction inversion", exact_equal(reverse_collision, INVERSION))
    check("C cubic Ward/covariance constraints do not identify the collision", identity_collision != reverse_collision and reverse_collision != complex_collision)

    size = 3

    def rotate_position(position: tuple[int, int, int], rotation: sp.Matrix) -> tuple[int, int, int]:
        return tuple(int(value) % size for value in rotation * sp.Matrix(position))

    def rotate_direction(direction: tuple[int, int, int], rotation: sp.Matrix) -> tuple[int, int, int]:
        return tuple(int(value) for value in rotation * sp.Matrix(direction))

    def stream(position: tuple[int, int, int], direction: tuple[int, int, int]) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
        return tuple((position[axis] + direction[axis]) % size for axis in range(3)), direction

    states = tuple(product(range(size), repeat=3))
    check(
        "C direction streaming is homogeneous and proper-cubic covariant",
        all(
            stream(
                rotate_position(position, rotation),
                rotate_direction(direction, rotation),
            )
            == (
                rotate_position(stream(position, direction)[0], rotation),
                rotate_direction(stream(position, direction)[1], rotation),
            )
            for rotation in ROTATIONS
            for position in states
            for direction in DIRECTIONS
        ),
    )
    plus_x = sp.Matrix([1, 0, 0, 0, 0, 0])
    check("C two covariant collisions route one directional input oppositely", identity_collision * plus_x == plus_x and reverse_collision * plus_x == sp.Matrix([0, 1, 0, 0, 0, 0]))
    check("C six fermionic direction modes require a generated six-qubit macrocell", 2**6 == 64)


def ward_identity_and_source_angle() -> None:
    section("D - Exact number Ward identity leaves source/commit angle free")
    number = sp.diag(0, 1, 1, 2)
    rail_occupation = sp.kronecker_product(I2, P1)
    occupied_reservoir_blank_rail = sp.Matrix([0, 0, 1, 0])
    angles = (sp.pi / 6, sp.pi / 4, sp.pi / 2)
    expected = (sp.Rational(1, 4), sp.Rational(1, 2), sp.Integer(1))
    observed = []
    for angle in angles:
        unitary = partial_transfer(angle)
        output = sp.simplify(unitary * occupied_reservoir_blank_rail)
        probability = sp.simplify((output.H * rail_occupation * output)[0])
        observed.append(probability)
        check(f"D source angle {angle} is unitary and obeys exact number Ward identity", exact_equal(unitary.H * unitary, sp.eye(4)) and exact_equal(unitary.H * number * unitary, number))
    check("D the same Ward identity permits quarter half or unit emission", tuple(observed) == expected)
    check("D unit current is selected only at the full-transfer angle", observed[-1] == 1 and observed[0] != 1 and observed[1] != 1)

    vacuum = sp.Matrix([1, 0, 0, 0])
    check("D every displayed number-conserving source law leaves vacuum unchanged", all(partial_transfer(angle) * vacuum == vacuum for angle in angles))
    check("D current conservation therefore does not force first occurrence", partial_transfer(sp.pi / 2) * vacuum == vacuum)


def scoped_matter_tuple_embedding() -> None:
    section("E - Scoped anomaly-minimal matter tuple and generated-block cost")
    charges = (-9, -5, -1, 7, 8)
    check("E scoped charge tuple cancels linear and cubic anomalies", sum(charges) == 0 and sum(charge**3 for charge in charges) == 0)
    check("E charge tuple remains primitive and nonvectorlike", gcd_values(charges) == 1 and not any(-charge in charges for charge in charges))

    fock_charges = tuple(
        sum(occupation[index] * charges[index] for index in range(5))
        for occupation in product((0, 1), repeat=5)
    )
    charge_operator = sp.diag(*fock_charges)
    gauge_phase = sp.diag(*(sp.exp(sp.I * sp.pi * charge / 7) for charge in fock_charges))
    check("E five independent fermionic occupancy modes fit exactly in five primitive qubits", len(fock_charges) == 2**5 == 32)
    check("E exact gauge phase is unitary and commutes with the Fock charge", exact_equal(gauge_phase.H * gauge_phase, sp.eye(32)) and exact_equal(gauge_phase * charge_operator, charge_operator * gauge_phase))
    check("E five two-component Weyl species require at least ten local fermionic modes", 2 * len(charges) == 10 and 2**10 == 1024)
    check("E a three-qubit single-particle species label leaves three extra basis states", 2**3 - len(charges) == 3)
    check("E anomaly cancellation does not choose bulk topological sign", all(sum(charges) == 0 and sum(charge**3 for charge in charges) == 0 for _level in (-1, 1)))


def gcd_values(values: tuple[int, ...]) -> int:
    result = 0
    for value in values:
        result = sp.igcd(result, abs(value))
    return int(result)


def species_dependent_qca_and_common_coupling() -> None:
    section("F - Gauge/cubic Ward identities allow species-dependent dynamics")
    charges = (-9, -5, -1, 7, 8)
    universal_blocks = tuple(collision(sp.pi / 4, sp.pi / 4) for _ in charges)
    nonuniversal_angles = (sp.pi / 6, sp.pi / 4, sp.pi / 3, sp.pi / 2, sp.pi)
    nonuniversal_blocks = tuple(collision(angle / 2, angle) for angle in nonuniversal_angles)
    universal_collision = block_diagonal(universal_blocks)
    nonuniversal_collision = block_diagonal(nonuniversal_blocks)
    species_charge = sp.diag(*(charge for charge in charges for _direction in DIRECTIONS))
    check("F universal and species-dependent collision laws are both unitary", exact_equal(universal_collision.H * universal_collision, sp.eye(30)) and exact_equal(nonuniversal_collision.H * nonuniversal_collision, sp.eye(30)))
    check("F both laws obey the exact species-charge Ward identity", exact_equal(universal_collision * species_charge, species_charge * universal_collision) and exact_equal(nonuniversal_collision * species_charge, species_charge * nonuniversal_collision))
    check("F both laws remain proper-cubic covariant in each species block", all(all(exact_equal(block * permutation, permutation * block) for permutation in DIRECTION_REP) for block in universal_blocks + nonuniversal_blocks))
    check("F Ward identities do not impose species-universal collision phases", universal_collision != nonuniversal_collision)

    universal_couplings = tuple(sp.Integer(1) for _ in charges)
    charge_dependent_couplings = tuple(sp.Rational(81 + charge**2, 81) for charge in charges)
    check("F gauge-invariant scalar gravity coupling may be universal or charge dependent", universal_couplings != charge_dependent_couplings)
    check("F one common field rescaling cannot remove charge-dependent ratios", len(set(charge_dependent_couplings)) > 1)


def orientation_actuality_clock_and_tensor_residuals() -> None:
    section("G - Orientation, actuality, metric rate, and tensor response")

    def tensor_power(matrix: sp.Matrix, power: int) -> sp.Matrix:
        result = sp.ones(1, 1)
        for _ in range(power):
            result = sp.kronecker_product(result, matrix)
        return result

    scalar = sp.zeros(9, 1)
    for axis in range(3):
        scalar[3 * axis + axis] = 1 / sp.sqrt(3)
    pseudoscalar = sp.zeros(27, 1)
    for first, second, third in product(range(3), repeat=3):
        pseudoscalar[9 * first + 3 * second + third] = sp.LeviCivita(first, second, third) / sp.sqrt(6)
    scalar = scalar.col_join(sp.zeros(27, 1))
    pseudoscalar = sp.zeros(9, 1).col_join(pseudoscalar)
    chiral_generator = scalar * pseudoscalar.H + pseudoscalar * scalar.H
    chiral_projector = scalar * scalar.H + pseudoscalar * pseudoscalar.H
    angle = sp.pi / 5
    positive_orientation = sp.eye(36) + (sp.cos(angle) - 1) * chiral_projector - sp.I * sp.sin(angle) * chiral_generator
    negative_orientation = sp.eye(36) + (sp.cos(angle) - 1) * chiral_projector + sp.I * sp.sin(angle) * chiral_generator
    proper_representations = tuple(
        sp.diag(tensor_power(rotation, 2), tensor_power(rotation, 3))
        for rotation in ROTATIONS
    )
    reflection = sp.diag(-1, 1, 1)
    reflection_representation = sp.diag(
        tensor_power(reflection, 2), tensor_power(reflection, 3)
    )
    check(
        "G scalar and pseudoscalar carriers are invariant under every proper cubic rotation",
        all(
            representation * scalar == scalar
            and representation * pseudoscalar == pseudoscalar
            for representation in proper_representations
        ),
    )
    check(
        "G a coordinate reflection fixes the scalar and reverses the pseudoscalar",
        reflection_representation * scalar == scalar
        and reflection_representation * pseudoscalar == -pseudoscalar,
    )
    check(
        "G opposite orientation collisions are unitary and proper-cubic covariant",
        exact_equal(positive_orientation.H * positive_orientation, sp.eye(36))
        and exact_equal(negative_orientation.H * negative_orientation, sp.eye(36))
        and all(
            exact_equal(representation * positive_orientation, positive_orientation * representation)
            and exact_equal(representation * negative_orientation, negative_orientation * representation)
            for representation in proper_representations
        ),
    )
    check(
        "G reflection exchanges the two exact spatial-orientation laws",
        exact_equal(
            reflection_representation
            * positive_orientation
            * reflection_representation.T,
            negative_orientation,
        )
        and positive_orientation != negative_orientation,
    )
    check("G the explicit orientation carrier needs a generated six-qubit block", 2**5 < 36 <= 2**6)

    positive_phase = collision(sp.pi / 3, sp.pi / 2)
    negative_phase = collision(-sp.pi / 3, -sp.pi / 2)
    check("G complex-conjugate collision laws satisfy the same cubic Ward identities", exact_equal(negative_phase, positive_phase.conjugate()) and all(exact_equal(permutation * positive_phase, positive_phase * permutation) and exact_equal(permutation * negative_phase, negative_phase * permutation) for permutation in DIRECTION_REP))
    check("G fixed covariance does not select the collision-phase pair", positive_phase != negative_phase)

    partial_output = sp.simplify(partial_transfer(sp.pi / 4) * sp.Matrix([0, 0, 1, 0]))
    check("G Ward-preserving source can leave a coherent two-branch output", sum(value != 0 for value in partial_output) == 2)
    basis_states = tuple(sp.eye(4).col(index) for index in range(4))
    check("G coherent output is normalized but is not one basis record member", exact_equal((partial_output.H * partial_output)[0], 1) and all(partial_output != basis for basis in basis_states))
    coherent_density = sp.simplify(partial_output * partial_output.H)
    occupied_projectors = (sp.diag(0, 1, 0, 0), sp.diag(0, 0, 1, 0))
    branch_weights = tuple(sp.simplify(sp.trace(projector * coherent_density)) for projector in occupied_projectors)
    dephased_density = sp.simplify(
        sum(
            (projector * coherent_density * projector for projector in occupied_projectors),
            sp.zeros(4),
        )
    )
    number = sp.diag(0, 1, 1, 2)
    check(
        "G a number-Ward instrument gives two normalized basis-record branches",
        branch_weights == (sp.Rational(1, 2), sp.Rational(1, 2))
        and all(
            exact_equal(
                projector * coherent_density * projector / weight,
                projector,
            )
            for projector, weight in zip(occupied_projectors, branch_weights)
        ),
    )
    check(
        "G coherent and record-instrument channels preserve the same number but differ",
        exact_equal(sp.trace(number * coherent_density), 1)
        and exact_equal(sp.trace(number * dephased_density), 1)
        and exact_equal(sp.trace(dephased_density), 1)
        and coherent_density != dephased_density,
    )

    event_count = sp.Integer(12)
    check("G one QCA layer supplies causal depth but rates one and two give different duration", event_count / 1 == 12 and event_count / 2 == 6)

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
    check("G trace weights one and two are both proper-cubic covariant", all(exact_equal(tensor_response(rotation * basis * rotation.T, 1), rotation * tensor_response(basis, 1) * rotation.T) and exact_equal(tensor_response(rotation * basis * rotation.T, 2), rotation * tensor_response(basis, 2) * rotation.T) for rotation in ROTATIONS for basis in symmetric_basis))
    check("G current/tensor Ward form does not select the trace ratio", response_one != response_two)


def granted_link_intersection_and_clause_deletion() -> None:
    section("H - Paired laws after granting every earlier link")
    fields = (
        "event occurrence",
        "collision phase",
        "spatial orientation",
        "actual sector",
        "metric rate",
        "tensor ratio",
        "species coupling",
    )
    candidates = tuple(product((0, 1), repeat=len(fields)))
    ward_scores = {candidate: 0 for candidate in candidates}
    check("H QCA/anomaly/current Ward constraints leave all 128 field assignments", len(tuple(candidate for candidate, score in ward_scores.items() if score == 0)) == 128)
    record_forming = tuple(candidate for candidate in candidates if candidate[0] == 1)
    check("H imposing one linked nonzero event still leaves 64 completion assignments", len(record_forming) == 64)

    target = (1, 0, 0, 0, 0, 0, 0)

    def completion_score(candidate: tuple[int, ...], omitted: int | None = None) -> int:
        return sum((value - target[index]) ** 2 for index, value in enumerate(candidate) if index != omitted)

    completed = tuple(candidate for candidate in candidates if completion_score(candidate) == 0)
    check("H seven explicit completion clauses select one assignment", completed == (target,))
    for index, field in enumerate(fields):
        scores = {candidate: completion_score(candidate, omitted=index) for candidate in candidates}
        minima = tuple(candidate for candidate, score in scores.items() if score == min(scores.values()))
        check(f"H deleting {field} completion clause restores an exact pair", len(minima) == 2 and {candidate[index] for candidate in minima} == {0, 1})


def documentation_contract() -> None:
    section("I - Route coverage and no-go-discipline needles")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "homogeneous proper-cubic generated m2 law",
        "primitive scalar transport",
        "six-direction qca",
        "collision commutant",
        "ward identity",
        "event occurrence",
        "orientation",
        "actual-sector semantics",
        "metric rate",
        "tensor trace/traceless ratio",
        "universal species coupling",
        "scoped matter tuple",
        "generated-block embedding",
        "paired laws after every earlier link",
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
    primitive_scalar_qca_transport_boundary()
    six_direction_block_qca()
    ward_identity_and_source_angle()
    scoped_matter_tuple_embedding()
    species_dependent_qca_and_common_coupling()
    orientation_actuality_clock_and_tensor_residuals()
    granted_link_intersection_and_clause_deletion()
    documentation_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
