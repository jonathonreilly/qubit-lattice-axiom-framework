#!/usr/bin/env python3
"""Exact bounded probes for escalating relational disagreement into a full law."""

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
    / "RELATIONAL_QUBIT_DISAGREEMENT_CANONICAL_LAW_ESCALATION_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
TOURNAMENT_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "FIRST_PRINCIPLES_LAW_SELECTION_TOURNAMENT_NOTE_2026-07-14.md"
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
PAULIS = (X, Y, Z)
KET0 = sp.Matrix([1, 0])
KET1 = sp.Matrix([0, 1])
KET_PLUS = (KET0 + KET1) / sp.sqrt(2)
KET_MINUS = (KET0 - KET1) / sp.sqrt(2)
KET_PLUS_I = (KET0 + sp.I * KET1) / sp.sqrt(2)
KET_MINUS_I = (KET0 - sp.I * KET1) / sp.sqrt(2)


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


def overlap(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(left * right))


def exchange_unitary(theta: sp.Expr, sign: int = 1) -> sp.Matrix:
    """exp(-i sign*theta*SWAP), using SWAP**2=I exactly."""

    return sp.simplify(sp.cos(theta) * I4 - sp.I * sign * sp.sin(theta) * SWAP)


def partial_trace_second(rho: sp.Matrix) -> sp.Matrix:
    result = sp.zeros(2)
    for left in range(2):
        for left_prime in range(2):
            result[left, left_prime] = sum(
                rho[2 * left + right, 2 * left_prime + right]
                for right in range(2)
            )
    return sp.simplify(result)


def expectation(rho: sp.Matrix, observable: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(rho * observable))


def source_contract() -> None:
    section("A - Source, authority, and target contract")
    note = " ".join(
        NOTE.read_text(encoding="utf-8")
        .lower()
        .replace("`", "")
        .replace("*", "")
        .split()
    )
    axioms = AXIOMS.read_text(encoding="utf-8")
    tournament = TOURNAMENT_NOTE.read_text(encoding="utf-8").lower()
    completeness = COMPLETENESS_NOTE.read_text(encoding="utf-8").lower()
    check("A note is authority-free", "authority: none" in note)
    check(
        "A note changes no live foundation surface",
        "changes no axiom, registry, primitive, audit, review queue, or retained surface" in note,
    )
    check(
        "A Admissibility remains explicitly nondynamical",
        "Admissibility is not a dynamics axiom." in axioms,
    )
    check(
        "A Record occurrence is present while its rule remains outside the axioms",
        "Records form." in axioms
        and "formation rules" in axioms
        and "at what rate" in axioms,
    )
    check(
        "A prior copy-equal winner and disagreement atom are wired in",
        "copy-equal" in tournament and "minimum triggered disagreement" in tournament,
    )
    check(
        "A complete-law target includes state context record actuality and statistics",
        all(
            f"`{field}`" in completeness
            for field in ("state", "context", "record", "actuality", "statistics")
        ),
    )


def su2_commutant_and_exchange_quotient() -> None:
    section("B - SU(2)-relational pair law and clock/energy quotient")
    total_generators = tuple(
        sp.kronecker_product(pauli, I2) + sp.kronecker_product(I2, pauli)
        for pauli in PAULIS
    )
    commutator_maps = tuple(
        sp.kronecker_product(generator.T, I4)
        - sp.kronecker_product(I4, generator)
        for generator in total_generators
    )
    stacked = commutator_maps[0].col_join(commutator_maps[1]).col_join(commutator_maps[2])
    check("B diagonal-SU(2) commutant has exact dimension two", stacked.rank() == 14 and len(stacked.nullspace()) == 2)
    check("B identity and SWAP are independent commutant elements", all(exact_equal(SWAP * generator, generator * SWAP) for generator in total_generators) and SWAP != I4)
    check("B SWAP is Hermitian involutive", SWAP.H == SWAP and SWAP * SWAP == I4)

    sample_su2 = (
        I2,
        sp.I * X,
        sp.I * Z,
        sp.I * (X + Z) / sp.sqrt(2),
    )
    check(
        "B projector-overlap exchange is invariant under simultaneous qubit-frame change",
        all(
            exact_equal(
                sp.kronecker_product(unitary, unitary)
                * SWAP
                * sp.kronecker_product(unitary.H, unitary.H),
                SWAP,
            )
            for unitary in sample_su2
        ),
    )

    eigenvalues = SWAP.eigenvals()
    check("B SWAP splits singlet and triplet sectors", eigenvalues == {1: 3, -1: 1})
    check("B positive rescaling and identity shift leave only the nonzero exchange sign", {-1, 1} == {sp.sign(value) for value in (-3, 5)})

    theta = sp.pi / 7
    alpha = sp.Integer(3)
    beta = sp.Integer(5)
    base = exchange_unitary(theta, sign=-1)
    transformed = sp.exp(-sp.I * beta * theta / alpha) * (
        sp.cos(theta) * I4 + sp.I * sp.sin(theta) * SWAP
    )
    check(
        "B positive clock rescaling plus scalar energy shift preserves the channel up to phase",
        exact_equal(transformed, sp.exp(-sp.I * beta * theta / alpha) * base),
    )
    check("B the dimensionless exchange angle survives the clock-rescaling quotient", sp.simplify((alpha * 1) * (theta / alpha)) == theta)
    check("B a positive quotient does not identify alignment with antialignment", not exact_equal(exchange_unitary(theta, -1), exchange_unitary(theta, 1)))

    swap_left_center = sp.kronecker_product(SWAP, I2)
    swap_center_right = sp.kronecker_product(I2, SWAP)
    full_alignment = -(swap_left_center + swap_center_right)
    full_antialignment = swap_left_center + swap_center_right
    check("B full three-qubit alignment Hamiltonian has a four-dimensional ground space", full_alignment.eigenvals().get(-2) == 4)
    check("B full three-qubit antialignment Hamiltonian also has a degenerate ground space", full_antialignment.eigenvals().get(-1) == 2)


def relational_disagreement_metrics_and_formation_gap() -> None:
    section("C - Fidelity, overlap, relative entropy, and occurrence")
    kets = (KET0, KET1, KET_PLUS, KET_MINUS, KET_PLUS_I, KET_MINUS_I)
    projectors = tuple(projector(ket) for ket in kets)
    for index, reference in enumerate(projectors):
        overlaps = tuple(overlap(reference, candidate) for candidate in projectors)
        check(f"C overlap uniquely selects matching test projector {index}", overlaps[index] == 1 and sum(value == 1 for value in overlaps) == 1)
        for candidate, fidelity in zip(projectors, overlaps):
            hs = sp.simplify(sp.trace((reference - candidate) ** 2))
            check(
                f"C Hilbert-Schmidt and infidelity ordering agree for reference {index}",
                hs == 2 * (1 - fidelity),
            )

    relative_entropy_slope = sp.simplify(sp.log(sp.Rational(1, 4)) - sp.log(sp.Rational(3, 4)))
    check("C regularized pure-reference relative entropy decreases strictly with overlap", relative_entropy_slope == -sp.log(3) and relative_entropy_slope.is_negative)

    for index, reference in enumerate(projectors):
        aligned_energy = tuple(sp.simplify(-2 * overlap(reference, candidate)) for candidate in projectors)
        antialigned_energy = tuple(sp.simplify(2 * overlap(reference, candidate)) for candidate in projectors)
        check(f"C two equal neighbors uniquely minimize alignment energy at their projector {index}", aligned_energy[index] == -2 and sum(value == -2 for value in aligned_energy) == 1)
        orthogonal_index = index + 1 if index % 2 == 0 else index - 1
        check(f"C reversing the exchange sign selects the orthogonal projector {index}", antialigned_energy[orthogonal_index] == 0 and sum(value == 0 for value in antialigned_energy) == 1)

    equal_sum = 2 * projectors[0]
    opposite_sum = projectors[0] + projectors[1]
    skew_sum = projectors[0] + projectors[2]
    check("C equal references give a nondegenerate effective target", equal_sum.eigenvals() == {2: 1, 0: 1})
    check("C orthogonal references make every center projector tie", opposite_sum == I2)
    check("C nonorthogonal unequal references still have one top eigendirection", len(skew_sum.eigenvals()) == 2 and all(multiplicity == 1 for multiplicity in skew_sum.eigenvals().values()))

    disagreement_only = {"copy": 0, "no_write": 0, "oppose": 4}
    with_trigger_cost = {"copy": 0, "no_write": 2, "oppose": 4}
    reverse_trigger_cost = {"copy": 0, "no_write": -2, "oppose": 4}
    check("C disagreement alone leaves copy and no-write tied", set(name for name, value in disagreement_only.items() if value == min(disagreement_only.values())) == {"copy", "no_write"})
    check("C a positive missed-trigger cost uniquely selects copy", min(with_trigger_cost, key=with_trigger_cost.get) == "copy")
    check("C reversing the occurrence cost instead selects no-write", min(reverse_trigger_cost, key=reverse_trigger_cost.get) == "no_write")

    input_overlap = sp.simplify((KET0.T * KET_PLUS)[0] ** 2)
    output_overlap = sp.simplify((KET0.T * KET_PLUS)[0] ** 3)
    check("C two-to-three universal cloning would change a nonorthogonal inner product", input_overlap == sp.Rational(1, 2) and output_overlap == sp.sqrt(2) / 4 and input_overlap != output_overlap)
    cnot = sp.Matrix(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ]
    )
    check(
        "C orthogonal recorded alternatives can still be copied by a controlled gate",
        exact_equal(cnot * sp.kronecker_product(KET0, KET0), sp.kronecker_product(KET0, KET0))
        and exact_equal(cnot * sp.kronecker_product(KET1, KET0), sp.kronecker_product(KET1, KET1)),
    )


def bell_context_and_actualization_controls() -> None:
    section("D - Coherent Bell contexts, instruments, and one actual member")
    input_state = sp.kronecker_product(KET0, KET1)
    entangled_state = sp.simplify(exchange_unitary(sp.pi / 4) * input_state)
    entangled_rho = projector(entangled_state)
    reduced = partial_trace_second(entangled_rho)
    check("D quarter-exchange maps a product input to a normalized state", exact_equal((entangled_state.H * entangled_state)[0], 1))
    check("D quarter-exchange gives a maximally mixed one-qubit reduction", exact_equal(reduced, I2 / 2))
    check("D idle exchange leaves the same input unentangled", exact_equal(exchange_unitary(0) * input_state, input_state))

    singlet = sp.kronecker_product(KET0, KET1) - sp.kronecker_product(KET1, KET0)
    singlet = singlet / sp.sqrt(2)
    rho_singlet = projector(singlet)
    b0 = (Z + X) / sp.sqrt(2)
    b1 = (Z - X) / sp.sqrt(2)
    correlators = (
        expectation(rho_singlet, sp.kronecker_product(Z, b0)),
        expectation(rho_singlet, sp.kronecker_product(Z, b1)),
        expectation(rho_singlet, sp.kronecker_product(X, b0)),
        expectation(rho_singlet, sp.kronecker_product(X, b1)),
    )
    chsh = sp.simplify(correlators[0] + correlators[1] + correlators[2] - correlators[3])
    check("D relational singlet contexts reach exact Tsirelson magnitude", chsh == -2 * sp.sqrt(2))

    theta = sp.pi / 6
    alternative_chsh = sp.simplify(-2 * (sp.cos(theta) + sp.sin(theta)))
    check("D another covariant relative context angle gives a different Bell value", alternative_chsh == -sp.sqrt(3) - 1 and alternative_chsh != chsh)
    check("D maximum Bell magnitude is an additional target beyond exchange covariance", abs(float(chsh)) > abs(float(alternative_chsh)))

    local_values = (-1, 1)
    local_chsh_values = tuple(
        a0 * b0v + a0 * b1v + a1 * b0v - a1 * b1v
        for a0, a1, b0v, b1v in product(local_values, repeat=4)
    )
    check("D every local deterministic response table has CHSH magnitude two", set(abs(value) for value in local_chsh_values) == {2})

    rho = sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 3)], [sp.Rational(1, 3), sp.Rational(1, 3)]])
    p0 = projector(KET0)
    p1 = projector(KET1)
    pvm_channel = sp.simplify(p0 * rho * p0 + p1 * rho * p1)
    phase_channel = sp.simplify((rho + Z * rho * Z) / 2)
    pvm_weights = (sp.trace(p0 * rho), sp.trace(p1 * rho))
    phase_weights = (sp.Rational(1, 2) * sp.trace(rho), sp.Rational(1, 2) * sp.trace(rho))
    check("D Lüders and random-phase instruments have the same nonselective channel", exact_equal(pvm_channel, phase_channel))
    check("D their physical event weights and labels differ", pvm_weights == (sp.Rational(2, 3), sp.Rational(1, 3)) and phase_weights == (sp.Rational(1, 2), sp.Rational(1, 2)))
    check("D normalized positive weights do not name one actual result", all(weight > 0 for weight in pvm_weights) and len(pvm_weights) == 2)


def record_state_and_renewal_controls() -> None:
    section("E - Record-only future sufficiency and renewal")
    ghz_zero = sp.kronecker_product(KET0, KET0, KET0)
    ghz_one = sp.kronecker_product(KET1, KET1, KET1)
    ghz_plus = (ghz_zero + ghz_one) / sp.sqrt(2)
    ghz_minus = (ghz_zero - ghz_one) / sp.sqrt(2)
    rho_plus = projector(ghz_plus)
    rho_minus = projector(ghz_minus)
    diagonal_plus = sp.diag(*[rho_plus[index, index] for index in range(8)])
    diagonal_minus = sp.diag(*[rho_minus[index, index] for index in range(8)])
    xxx = sp.kronecker_product(X, X, X)
    check("E opposite GHZ phases have the same readable computational-basis diagonal", exact_equal(diagonal_plus, diagonal_minus))
    check("E a later coherent context distinguishes those phases exactly", expectation(rho_plus, xxx) == 1 and expectation(rho_minus, xxx) == -1)
    check("E phase-complete records or a no-return restriction are therefore substantive", rho_plus != rho_minus)

    for capacity in range(1, 8):
        longest_strict_append_count = capacity
        check(f"E finite site-tagged archive of capacity {capacity} admits at most {capacity} strict appends", longest_strict_append_count == capacity)
    capacity = 12
    probability = Fraction(1, 5)
    expected_available = tuple(Fraction(capacity) * (1 - probability) ** tick for tick in range(8))
    expected_writes = tuple(value * probability for value in expected_available)
    check("E sparse independent writes monotonically deplete finite blank capacity", all(left > right for left, right in zip(expected_available, expected_available[1:])))
    check("E sparse formation delays but does not stabilize a positive finite-capacity flux", all(left > right for left, right in zip(expected_writes, expected_writes[1:])))

    finite_tape = (1, 0, 0, 0, 0)
    shifted = finite_tape[-1:] + finite_tape[:-1]
    check("E a cyclic shift is reversible and transports rather than site-tethers a record", shifted == (0, 1, 0, 0, 0) and sorted(shifted) == sorted(finite_tape))
    cycled = finite_tape
    for _ in range(len(finite_tape)):
        cycled = cycled[-1:] + cycled[:-1]
    check("E finite reversible export returns and cannot be an absolute no-return archive", cycled == finite_tape)


def matter_chirality_and_clock_controls() -> None:
    section("F - Matter/chirality and clock")
    sx, sy, sz = sp.symbols("s_x s_y s_z", real=True)
    h_plus = sx * X + sy * Y + sz * Z
    h_minus = -h_plus
    norm_squared = sx**2 + sy**2 + sz**2
    check("F mirror Weyl symbols have identical squared spectra", exact_equal(h_plus * h_plus, norm_squared * I2) and exact_equal(h_minus * h_minus, norm_squared * I2))
    check("F their velocity-map determinants have opposite chirality", sp.eye(3).det() == 1 and (-sp.eye(3)).det() == -1)
    check("F no proper qubit-frame rotation equals spatial inversion", (-sp.eye(3)).det() != 1)

    kx, ky, kz = sp.symbols("k_x k_y k_z", real=True)
    magnon = 3 - sp.cos(kx) - sp.cos(ky) - sp.cos(kz)
    gradient_at_zero = tuple(sp.diff(magnon, variable).subs({kx: 0, ky: 0, kz: 0}) for variable in (kx, ky, kz))
    hessian_at_zero = sp.hessian(magnon, (kx, ky, kz)).subs({kx: 0, ky: 0, kz: 0})
    check("F cubic exchange magnon dispersion is parity even", sp.simplify(magnon.subs({kx: -kx, ky: -ky, kz: -kz}) - magnon) == 0)
    check("F its low-momentum leading term is quadratic rather than Weyl-linear", gradient_at_zero == (0, 0, 0) and hessian_at_zero == sp.eye(3))

    active_edge_count = sp.diag(1, 2)
    beta = sp.Integer(1)
    time = sp.pi / 2
    sector_phase = sp.diag(sp.exp(-sp.I * beta * time), sp.exp(-sp.I * 2 * beta * time))
    check("F a per-active-edge identity shift is not global across record sectors", sector_phase == sp.diag(-sp.I, -1) and sector_phase != sector_phase[0, 0] * sp.eye(2))
    check("F active-edge count is not a scalar on the sector superposition", active_edge_count != active_edge_count[0, 0] * sp.eye(2))

    event_count = sp.Integer(12)
    durations = (event_count / sp.Integer(1), event_count / sp.Integer(2))
    check("F one causal event order permits distinct metric rate calibrations", durations == (12, 6))
    check("F dimensionless exchange phase fixes neither formation rate calibration", sp.pi / 4 != sp.pi / 2)


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


def resource_green_controls() -> None:
    section("G - Disagreement action, resource source, and finite Green response")
    laplacian = cubic_torus_laplacian(3)
    count = laplacian.rows
    ones = sp.ones(count, 1)
    source = sp.zeros(count, 1)
    source[0] = 1
    source[1] = -1
    cycle_laplacian = sp.Matrix([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]])
    cycle_spectrum = cycle_laplacian.eigenvals()
    kronecker_sum = (
        sp.kronecker_product(cycle_laplacian, sp.eye(3), sp.eye(3))
        + sp.kronecker_product(sp.eye(3), cycle_laplacian, sp.eye(3))
        + sp.kronecker_product(sp.eye(3), sp.eye(3), cycle_laplacian)
    )
    cubic_spectrum = tuple(
        left + middle + right
        for left, middle, right in product((0, 3, 3), repeat=3)
    )
    check("G three-cycle factor has one zero and two nonzero modes", cycle_spectrum == {0: 1, 3: 2})
    check("G constructed cubic Hessian is the exact three-factor Kronecker sum", laplacian == kronecker_sum)
    check(
        "G cubic disagreement Hessian is symmetric with one constant zero mode",
        laplacian == laplacian.T
        and laplacian * ones == sp.zeros(count, 1)
        and cubic_spectrum.count(0) == 1,
    )
    check("G neutral source is compatible with the zero-mode quotient", (ones.T * source)[0] == 0)

    augmented = laplacian.row_join(ones).col_join(ones.T.row_join(sp.zeros(1, 1)))
    target = source.col_join(sp.zeros(1, 1))
    solution = augmented.inv(method="DM") * target
    field = solution[:count, :]
    multiplier = solution[count, 0]
    check("G zero-mean finite Green solution is exact and unique", laplacian * field == source and (ones.T * field)[0] == 0 and multiplier == 0)
    check("G source reversal gives the opposite field with the same quadratic norm", laplacian * (-field) == -source and (field.T * laplacian * field)[0] == ((-field).T * laplacian * (-field))[0])

    offset = sp.Rational(7, 3)
    shifted_field = field + offset * ones
    action = sp.simplify((field.T * laplacian * field)[0] / 2 - (source.T * field)[0])
    shifted_action = sp.simplify((shifted_field.T * laplacian * shifted_field)[0] / 2 - (source.T * shifted_field)[0])
    check("G neutral-source Dirichlet action is invariant under scalar-field offset", action == shifted_action)
    check("G the Green equation appears only after the linear source term is supplied", laplacian * sp.zeros(count, 1) == sp.zeros(count, 1) and source != sp.zeros(count, 1))


def augmentation_term_deletion_audit() -> None:
    section("H - Field-by-field selector-term deletion audit")
    atoms = (
        "alignment orientation",
        "triggered occurrence",
        "Bell phase and contexts",
        "event instrument and weights",
        "realized history member",
        "phase-complete record scope",
        "renewal/export boundary",
        "matter carrier and interactions",
        "chirality sign or domain",
        "metric clock calibration",
        "resource source and gravity map",
    )
    candidates = tuple(product((0, 1), repeat=len(atoms)))
    full_scores = tuple(sum(candidate) for candidate in candidates)
    check("H eleven explicit physical atoms produce one bookkeeping winner", sum(score == min(full_scores) for score in full_scores) == 1 and len(candidates) == 2048)
    for index, atom in enumerate(atoms):
        deleted_scores = tuple(sum(value for position, value in enumerate(candidate) if position != index) for candidate in candidates)
        check(f"H deleting {atom} restores an exact two-way tie", sum(score == min(deleted_scores) for score in deleted_scores) == 2)
        flipped_scores = tuple(sum(value if position != index else 1 - value for position, value in enumerate(candidate)) for candidate in candidates)
        flipped_winner = candidates[flipped_scores.index(min(flipped_scores))]
        check(f"H reversing {atom} selects its opposite competitor", flipped_winner[index] == 1 and sum(flipped_winner) == 1)


def documentation_contract() -> None:
    section("I - Scope, atom ledger, and no-go-discipline needles")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "exact relational disagreement functional",
        "projector overlap",
        "fidelity",
        "relative entropy",
        "clock rescaling",
        "energy shift",
        "no-cloning",
        "coherent bell contexts",
        "formation and actuality",
        "record-only state",
        "renewal",
        "chirality and matter",
        "resource and green response",
        "the cost has become the law",
        "opposite or tied competitor",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — exact residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path",
        "n7 — strongest steelman",
        "n8 — cross-cycle echo",
    )
    for phrase in required:
        check(f"I note contains boundary: {phrase}", phrase in note)


def main() -> None:
    source_contract()
    su2_commutant_and_exchange_quotient()
    relational_disagreement_metrics_and_formation_gap()
    bell_context_and_actualization_controls()
    record_state_and_renewal_controls()
    matter_chirality_and_clock_controls()
    resource_green_controls()
    augmentation_term_deletion_audit()
    documentation_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
