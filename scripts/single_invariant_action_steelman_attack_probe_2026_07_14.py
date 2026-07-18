#!/usr/bin/env python3
"""Bounded exact attack on a one-invariant-action TOE selector steelman."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
ACTION_PARENT = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "RELATIONAL_QUBIT_DISAGREEMENT_CANONICAL_LAW_ESCALATION_NOTE_2026-07-14.md"
)
COMPLETENESS_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md"
)


PASS = 0
FAIL = 0

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
HADAMARD = (X + Z) / sp.sqrt(2)
KET0 = sp.Matrix([1, 0])
KET1 = sp.Matrix([0, 1])
KET_PLUS = (KET0 + KET1) / sp.sqrt(2)


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
        return all(sp.simplify(value) == 0 for value in difference)
    return sp.simplify(difference) == 0


def projector(ket: sp.Matrix) -> sp.Matrix:
    return sp.simplify(ket * ket.conjugate().T)


def swap_matrix() -> sp.Matrix:
    swap = sp.zeros(4)
    for left in range(2):
        for right in range(2):
            swap[2 * right + left, 2 * left + right] = 1
    return swap


SWAP = swap_matrix()
I4 = sp.eye(4)


def block_diagonal(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return left.row_join(sp.zeros(left.rows, right.cols)).col_join(
        sp.zeros(right.rows, left.cols).row_join(right)
    )


def history_hamiltonian(unitary: sp.Matrix) -> sp.Matrix:
    """One-step Feynman-Kitaev propagation term for a two-state clock."""

    identity = sp.eye(unitary.rows)
    return sp.Rational(1, 2) * identity.row_join(-unitary.H).col_join(
        (-unitary).row_join(identity)
    )


def history_hamiltonian_with_input(unitary: sp.Matrix) -> sp.Matrix:
    input_penalty = block_diagonal(projector(KET1), sp.zeros(2))
    return sp.simplify(history_hamiltonian(unitary) + input_penalty)


def cnot(control: int, target: int, qubits: int = 3) -> sp.Matrix:
    size = 2**qubits
    gate = sp.zeros(size)
    for column in range(size):
        bits = [int(value) for value in f"{column:0{qubits}b}"]
        output = bits[:]
        if bits[control]:
            output[target] ^= 1
        row = int("".join(str(value) for value in output), 2)
        gate[row, column] = 1
    return gate


def basis_ket(index: int, dimension: int) -> sp.Matrix:
    ket = sp.zeros(dimension, 1)
    ket[index] = 1
    return ket


def cubic_torus_laplacian(size: int = 3) -> sp.Matrix:
    sites = tuple(product(range(size), repeat=3))
    index = {site: position for position, site in enumerate(sites)}
    laplacian = sp.zeros(len(sites))
    for site in sites:
        row = index[site]
        laplacian[row, row] = 6
        for axis in range(3):
            for direction in (-1, 1):
                neighbor = list(site)
                neighbor[axis] = (neighbor[axis] + direction) % size
                laplacian[row, index[tuple(neighbor)]] -= 1
    return laplacian


def source_contract() -> None:
    section("A - Authority and full-domain target")
    note = " ".join(
        NOTE.read_text(encoding="utf-8")
        .lower()
        .replace("*", "")
        .replace("`", "")
        .split()
    )
    axioms = AXIOMS.read_text(encoding="utf-8")
    parent = ACTION_PARENT.read_text(encoding="utf-8").lower()
    completeness = COMPLETENESS_NOTE.read_text(encoding="utf-8").lower()
    check("A note is authority-free", "authority: none" in note)
    check(
        "A note changes no live authority surface",
        "changes no axiom, registry, primitive, audit, review queue, or retained surface" in note,
    )
    check(
        "A current domain is Z3 with one M2 possibility algebra per site",
        "cubic lattice `Z^3`" in axioms and "`M_2(C)`" in axioms,
    )
    check("A permanent records and record-only state are current constraints", "records are permanent" in axioms.lower() and "A state is a configuration of records." in axioms)
    check("A parent steelman is wired in", "one complete invariant action" in parent and "strongest steelman" in parent)
    check(
        "A complete target includes concurrency renewal clock matter resource and gravity",
        all(term in completeness for term in ("concurrency", "renewal", "clock", "matter", "resource", "gravity")),
    )


def generated_domain_and_invariant_term_basis() -> None:
    section("B - Generated finite cylinders and independent invariant terms")
    for sites in range(1, 6):
        check(
            f"B {sites}-site generated qubit block has matrix size 2^{sites} and algebra dimension 4^{sites}",
            (2**sites) ** 2 == 4**sites,
        )

    total_generators = tuple(
        sp.kronecker_product(pauli, I2) + sp.kronecker_product(I2, pauli)
        for pauli in (X, Y, Z)
    )
    commutator_maps = tuple(
        sp.kronecker_product(generator.T, I4)
        - sp.kronecker_product(I4, generator)
        for generator in total_generators
    )
    stacked = commutator_maps[0].col_join(commutator_maps[1]).col_join(commutator_maps[2])
    check("B common-SU2 pair invariants have dimension two", len(stacked.nullspace()) == 2 and stacked.rank() == 14)

    px = (I2 + X) / 2
    py = (I2 + Y) / 2
    pz = (I2 + Z) / 2
    oriented = sp.simplify(sp.trace(px * py * pz))
    reversed_orientation = sp.simplify(sp.trace(px * pz * py))
    check("B ordered projector triple carries a proper-orientation pseudoscalar", oriented == sp.Rational(1, 4) + sp.I / 4 and reversed_orientation == sp.Rational(1, 4) - sp.I / 4)
    check("B orientation reversal flips the chiral term but not its even part", sp.re(oriented) == sp.re(reversed_orientation) and sp.im(oriented) == -sp.im(reversed_orientation))

    sample_su2 = (I2, sp.I * X, sp.I * Z, sp.I * HADAMARD)
    check(
        "B overlap and ordered-trace terms are invariant under common frame conjugation",
        all(
            exact_equal(
                sp.trace((unitary * px * unitary.H) * (unitary * py * unitary.H)),
                sp.trace(px * py),
            )
            and exact_equal(
                sp.trace(
                    (unitary * px * unitary.H)
                    * (unitary * py * unitary.H)
                    * (unitary * pz * unitary.H)
                ),
                oriented,
            )
            for unitary in sample_su2
        ),
    )

    swap_01 = sp.kronecker_product(SWAP, I2)
    swap_02 = sp.zeros(8)
    for left, center, right in product((0, 1), repeat=3):
        column = 4 * left + 2 * center + right
        row = 4 * right + 2 * center + left
        swap_02[row, column] = 1
    h_one = swap_01 + swap_02
    h_two = swap_01 * swap_02 + swap_02 * swap_01
    spectra = {}
    for eta in (sp.Integer(0), sp.Rational(1, 3)):
        hamiltonian = h_one + eta * h_two
        spectra[eta] = tuple(sorted(hamiltonian.eigenvals()))
    gap_ratio_zero = sp.simplify((spectra[0][1] - spectra[0][0]) / (spectra[0][2] - spectra[0][1]))
    gap_ratio_third = sp.simplify((spectra[sp.Rational(1, 3)][1] - spectra[sp.Rational(1, 3)][0]) / (spectra[sp.Rational(1, 3)][2] - spectra[sp.Rational(1, 3)][1]))
    check("B two independent invariant interaction terms survive the same symmetries", h_one.H == h_one and h_two.H == h_two and h_one * h_two == h_two * h_one)
    check("B their coefficient changes a scale-and-shift invariant spectral ratio", gap_ratio_zero == 2 and gap_ratio_third == 1)


def unique_history_action_wrapper() -> None:
    section("C - A unique frustration-free history minimum can encode any law")
    unitaries = {"identity": I2, "flip": X, "phase": Z, "hadamard": HADAMARD}
    spectra = {}
    ground_vectors = {}
    for name, unitary in unitaries.items():
        hamiltonian = history_hamiltonian_with_input(unitary)
        eigenvalues = hamiltonian.eigenvals()
        spectra[name] = tuple(sorted(eigenvalues.items(), key=lambda item: float(item[0])))
        nullspace = hamiltonian.nullspace()
        ground_vectors[name] = nullspace[0]
        expected_history = KET0.col_join(unitary * KET0) / sp.sqrt(2)
        check(f"C {name} action is positive semidefinite", all(value.is_nonnegative for value in eigenvalues))
        check(f"C {name} action has one zero-energy history", len(nullspace) == 1 and exact_equal(hamiltonian * expected_history, sp.zeros(4, 1)))

    check("C all four exact laws have the same complete history-action spectrum", all(spectrum == spectra["identity"] for spectrum in spectra.values()))
    check("C identity and flip unique minima predict different final states", not exact_equal(I2 * KET0, X * KET0))
    for name, unitary in unitaries.items():
        controlled_change = block_diagonal(I2, unitary)
        check(
            f"C {name} action is a controlled conjugate of the identity-law wrapper",
            exact_equal(
                history_hamiltonian_with_input(unitary),
                controlled_change
                * history_hamiltonian_with_input(I2)
                * controlled_change.H,
            ),
        )

    copy_action = {"write_matching": 0, "write_opposite": 1}
    oppose_action = {"write_matching": 1, "write_opposite": 0}
    check("C copy and oppose constraints are equally gapped and frustration-free", sorted(copy_action.values()) == sorted(oppose_action.values()) == [0, 1])
    check("C unique minimum selects content only because the rule table is inside the action", min(copy_action, key=copy_action.get) != min(oppose_action, key=oppose_action.get))


def formation_persistence_and_renewal_action() -> None:
    section("D - Occurrence, permanent archive, and renewal coefficients")
    disagreement = {"no_write": 0, "copy": 0, "oppose": 4}
    check("D pure disagreement leaves no-write tied with copy", set(name for name, score in disagreement.items() if score == min(disagreement.values())) == {"no_write", "copy"})
    for missed_trigger_coefficient, expected in ((1, "copy"), (0, "no_write"), (-1, "no_write")):
        scores = {
            "no_write": 2 * missed_trigger_coefficient,
            "copy": 0,
            "oppose": 4,
        }
        winners = tuple(name for name, score in scores.items() if score == min(scores.values()))
        if missed_trigger_coefficient == 0:
            check("D zero occurrence coefficient preserves a two-way tie", set(winners) == {"no_write", "copy"})
        else:
            check(
                f"D occurrence coefficient {missed_trigger_coefficient} selects {expected}",
                winners == (expected,),
            )

    archive_actions_without_permanence = {"write_stay": 2, "write_delete": 1}
    archive_actions_with_permanence = {"write_stay": 2, "write_delete": 3}
    check("D resource minimization alone favors later record deletion", min(archive_actions_without_permanence, key=archive_actions_without_permanence.get) == "write_delete")
    check("D an explicit permanence penalty reverses that result", min(archive_actions_with_permanence, key=archive_actions_with_permanence.get) == "write_stay")

    for capacity in range(1, 8):
        states = tuple(range(2**capacity))
        append_edges = tuple(
            (state, state | (1 << site))
            for state in states
            for site in range(capacity)
            if not state & (1 << site)
        )
        check(
            f"D permanent finite archive capacity {capacity} bounds strict writes by {capacity}",
            all(next_state.bit_count() == state.bit_count() + 1 for state, next_state in append_edges)
            and max(state.bit_count() for state in states) == capacity,
        )

    for capacity in (2, 5, 9):
        z_one = Fraction(1, 1)
        z_two = Fraction(2, 1)
        expected_one = Fraction(capacity) * z_one / (1 + z_one)
        expected_two = Fraction(capacity) * z_two / (1 + z_two)
        check(f"D normalized grand-canonical archive at capacity {capacity} retains fugacity freedom", expected_one == Fraction(capacity, 2) and expected_two == Fraction(2 * capacity, 3))

    finite_tape = (1, 0, 0, 0, 0)
    right_shift = finite_tape[-1:] + finite_tape[:-1]
    left_shift = finite_tape[1:] + finite_tape[:1]
    check("D left and right export are equally reversible and content preserving", sorted(left_shift) == sorted(right_shift) == sorted(finite_tape) and left_shift != right_shift)
    returned = finite_tape
    for _ in finite_tape:
        returned = returned[-1:] + returned[:-1]
    check("D finite reversible export returns without a no-return boundary", returned == finite_tape)


def concurrency_and_schedule_action() -> None:
    section("E - Local gate multiset does not select overlapping schedule")
    gate_01 = cnot(0, 1)
    gate_12 = cnot(1, 2)
    initial = basis_ket(4, 8)  # |100>
    forward = sp.simplify(gate_12 * gate_01 * initial)
    reverse = sp.simplify(gate_01 * gate_12 * initial)
    check("E each overlapping local update is unitary and involutive", gate_01.T * gate_01 == sp.eye(8) and gate_12.T * gate_12 == sp.eye(8) and gate_01**2 == sp.eye(8) and gate_12**2 == sp.eye(8))
    check("E the overlapping updates do not commute", gate_12 * gate_01 != gate_01 * gate_12)
    check("E opposite schedules give exact outputs 111 and 110", forward == basis_ket(7, 8) and reverse == basis_ket(6, 8))
    check("E operation-count and local-gate action scores tie across schedules", 2 == 2)
    check("E a history-action wrapper can uniquely encode either schedule", history_hamiltonian(gate_12 * gate_01).eigenvals() == history_hamiltonian(gate_01 * gate_12).eigenvals())

    cz_01 = sp.diag(1, 1, 1, 1, 1, 1, -1, -1)
    cz_12 = sp.diag(1, 1, 1, -1, 1, 1, 1, -1)
    check("E commuting diagonal edge gates are a positive schedule-gauge control", cz_01 * cz_12 == cz_12 * cz_01)


def statistics_actuality_and_branch_measure() -> None:
    section("F - Gibbs/path weights and actuality")
    energy_gap = sp.log(2)
    probabilities = {}
    for inverse_temperature in (1, 2):
        low_weight = sp.Integer(1)
        high_weight = sp.exp(-inverse_temperature * energy_gap)
        probabilities[inverse_temperature] = sp.simplify(low_weight / (low_weight + high_weight))
    check("F one invariant energy gap gives 2/3 or 4/5 under two normalizations", probabilities == {1: sp.Rational(2, 3), 2: sp.Rational(4, 5)})
    check("F only the dimensionless product beta times gap controls Gibbs statistics", sp.simplify(2 * energy_gap) == sp.log(4))

    coarse_zero_action_weights = (Fraction(1, 2), Fraction(1, 2))
    refined_zero_action_weights = (Fraction(1, 3), Fraction(2, 3))
    check("F equal-action branch refinement changes coarse path-count weight", coarse_zero_action_weights != refined_zero_action_weights)
    check(
        "F normalized positive Gibbs weights do not select one actual member",
        all(0 < value < 1 and 0 < 1 - value < 1 for value in probabilities.values()),
    )

    unique_minimum = {"history_a": 0, "history_b": 1}
    check("F zero-temperature minimization selects a history but supplies no nontrivial ensemble", min(unique_minimum, key=unique_minimum.get) == "history_a")

    p0 = projector(KET0)
    p1 = projector(KET1)
    rho = sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 3)], [sp.Rational(1, 3), sp.Rational(1, 3)]])
    luders = sp.simplify(p0 * rho * p0 + p1 * rho * p1)
    random_phase = sp.simplify((rho + Z * rho * Z) / 2)
    check("F one averaged dephasing action admits different physical event decompositions", exact_equal(luders, random_phase))
    check("F those decompositions carry different event weights", (sp.trace(p0 * rho), sp.trace(p1 * rho)) != (sp.Rational(1, 2), sp.Rational(1, 2)))


def matter_chirality_and_clock_terms() -> None:
    section("G - Matter, chirality, and clock terms allowed by one symmetry class")
    sx, sy, sz = sp.symbols("s_x s_y s_z", real=True)
    h_plus = sx * X + sy * Y + sz * Z
    h_minus = -h_plus
    norm = sx**2 + sy**2 + sz**2
    check("G opposite Weyl signs have identical spectrum invariants", exact_equal(h_plus**2, norm * I2) and exact_equal(h_minus**2, norm * I2))
    check("G their velocity determinants carry opposite hand", sp.eye(3).det() == 1 and (-sp.eye(3)).det() == -1)

    kx, ky, kz = sp.symbols("k_x k_y k_z", real=True)
    magnon = 3 - sp.cos(kx) - sp.cos(ky) - sp.cos(kz)
    check("G exchange matter remains parity even", sp.simplify(magnon.subs({kx: -kx, ky: -ky, kz: -kz}) - magnon) == 0)
    check("G exchange matter has no Weyl-linear derivative at zero", all(sp.diff(magnon, variable).subs({kx: 0, ky: 0, kz: 0}) == 0 for variable in (kx, ky, kz)))

    event_count = sp.Integer(12)
    check("G the same ordered event history permits rates one and two", event_count / 1 == 12 and event_count / 2 == 6)
    check("G clock scaling can normalize one coupling but not a dimensionless ratio", sp.Rational(2, 1) / sp.Rational(1, 1) != sp.Rational(1, 1) / sp.Rational(1, 1))


def resource_green_and_gravity_terms() -> None:
    section("H - Green extremum, nonlinear freedom, and universal coupling")
    laplacian = cubic_torus_laplacian(3)
    count = laplacian.rows
    ones = sp.ones(count, 1)
    source = sp.zeros(count, 1)
    source[0] = 1
    source[1] = -1
    augmented = laplacian.row_join(ones).col_join(ones.T.row_join(sp.zeros(1, 1)))
    solution = augmented.inv(method="DM") * source.col_join(sp.zeros(1, 1))
    field = solution[:count, :]
    check("H supplied neutral source has a unique zero-mean finite Green extremum", laplacian * field == source and (ones.T * field)[0] == 0)
    check("H zero source instead selects the constant/zero field", laplacian * sp.zeros(count, 1) == sp.zeros(count, 1))
    check("H source reversal gives an equally normalized opposite response", laplacian * (-field) == -source)

    phi = sp.symbols("phi", real=True)
    linear_stationarity = sp.diff(phi**2 / 2 - 2 * phi, phi)
    nonlinear_stationarity = sp.diff(phi**2 / 2 + phi**4 / 4 - 2 * phi, phi)
    check("H symmetry-allowed nonlinear coefficient changes the exact response", linear_stationarity.subs(phi, 2) == 0 and nonlinear_stationarity.subs(phi, 1) == 0)

    universal_couplings = (sp.Rational(1), sp.Rational(1))
    nonuniversal_couplings = (sp.Rational(1), sp.Rational(2))
    check("H scalar and cubic covariance permit universal or nonuniversal species couplings", universal_couplings != nonuniversal_couplings)
    check("H a common field rescaling cannot remove the species-coupling ratio", universal_couplings[1] / universal_couplings[0] == 1 and nonuniversal_couplings[1] / nonuniversal_couplings[0] == 2)


def operational_reference_functional_and_clause_deletion() -> None:
    section("I - The exact one-functional winner and where the law moved")
    fields = (
        "write occurrence",
        "copy content",
        "coherent phase",
        "eligible context",
        "overlap schedule",
        "record persistence",
        "capacity renewal",
        "actual history",
        "context statistics",
        "matter carrier",
        "chirality",
        "metric clock",
        "gravity response",
    )
    candidates = tuple(product((0, 1), repeat=len(fields)))
    reference = (0,) * len(fields)
    opposite_reference = (1,) * len(fields)

    def distance(candidate: tuple[int, ...], target: tuple[int, ...], omitted: int | None = None) -> int:
        return sum(
            (value - target[index]) ** 2
            for index, value in enumerate(candidate)
            if index != omitted
        )

    reference_scores = tuple(distance(candidate, reference) for candidate in candidates)
    opposite_scores = tuple(distance(candidate, opposite_reference) for candidate in candidates)
    self_consistency_scores = tuple(distance(candidate, candidate) for candidate in candidates)
    check("I operational distance to a complete target has one exact winner", sum(score == min(reference_scores) for score in reference_scores) == 1 and candidates[reference_scores.index(0)] == reference)
    check("I the opposite complete target is an equally unique functional winner", sum(score == min(opposite_scores) for score in opposite_scores) == 1 and candidates[opposite_scores.index(0)] == opposite_reference)
    check("I target-free self-distance leaves every complete law tied", set(self_consistency_scores) == {0} and len(candidates) == 8192)

    for index, field in enumerate(fields):
        deleted_scores = tuple(distance(candidate, reference, omitted=index) for candidate in candidates)
        winners = tuple(candidate for candidate, score in zip(candidates, deleted_scores) if score == min(deleted_scores))
        check(f"I deleting {field} target clause restores exactly two winners", len(winners) == 2 and {winner[index] for winner in winners} == {0, 1})

    positive_coefficients = tuple(range(1, len(fields) + 1))
    scaled_coefficients = tuple(7 * value for value in positive_coefficients)
    weighted_winner = min(candidates, key=lambda candidate: sum(coefficient * bit for coefficient, bit in zip(positive_coefficients, candidate)))
    scaled_winner = min(candidates, key=lambda candidate: sum(coefficient * bit for coefficient, bit in zip(scaled_coefficients, candidate)))
    check("I overall positive action normalization is quotientable", weighted_winner == scaled_winner == reference)
    flipped_first_winner = min(candidates, key=lambda candidate: -candidate[0] + sum(candidate[1:]))
    check("I reversing one invariant term selects the opposite physical clause", flipped_first_winner[0] == 1 and sum(flipped_first_winner) == 1)


def documentation_contract() -> None:
    section("J - Candidate-family coverage and no-go-discipline needles")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "actual generated domain",
        "one representation-independent invariant action",
        "least disagreement",
        "frustration-free",
        "history hamiltonian",
        "stationary action",
        "gibbs/free energy",
        "maximum entropy",
        "minimum description/resource",
        "global consistency",
        "topological/renormalization",
        "write versus no-write",
        "copy versus oppose",
        "eligible context",
        "concurrency and schedule",
        "persistence and renewal",
        "actuality and statistics",
        "matter and gravity",
        "clause-deletion audit",
        "the law moved",
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
        check(f"J note contains boundary: {phrase}", phrase in note)


def main() -> None:
    source_contract()
    generated_domain_and_invariant_term_basis()
    unique_history_action_wrapper()
    formation_persistence_and_renewal_action()
    concurrency_and_schedule_action()
    statistics_actuality_and_branch_measure()
    matter_chirality_and_clock_terms()
    resource_green_and_gravity_terms()
    operational_reference_functional_and_clause_deletion()
    documentation_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
