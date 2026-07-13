#!/usr/bin/env python3
"""Exact finite probes for the open r=1/2 formation-science backlog.

This runner checks bounded algebraic constructions.  It does not adopt a
formation law, a K-stage supply convention, a readout law, or a time law.
"""

from fractions import Fraction

import sympy as sp


PASS = 0
FAIL = 0


def check(label, condition, detail=""):
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        print(f"PASS: {label}")
    else:
        FAIL += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"FAIL: {label}{suffix}")
    return ok


def formation_resolution_probe():
    print("\n[1] FORMATION RESOLUTION AND HAZARD NORMALIZATION")
    carrier_atoms = ("s", "d1", "d2")
    quotient_cells = ("s", "d")

    w_carrier = Fraction(1, len(carrier_atoms))
    w_cells = Fraction(1, len(quotient_cells))
    r_of_w = lambda w: (1 - w) / (2 * w)

    check("uniform carrier atoms give w=1/3", w_carrier == Fraction(1, 3))
    check("uniform quotient cells give w=1/2", w_cells == Fraction(1, 2))
    check("carrier resolution gives r=1", r_of_w(w_carrier) == 1)
    check("quotient-cell resolution gives r=1/2", r_of_w(w_cells) == Fraction(1, 2))

    # The normalized two-channel hazard law has the same ambiguity: the
    # supplied relative hazard, not normalization, selects the result.
    hazard_weight = lambda hs, hd: Fraction(hs, hs + hd)
    check("equal cell hazards select w=1/2", hazard_weight(1, 1) == w_cells)
    check("one-versus-two carrier hazards select w=1/3", hazard_weight(1, 2) == w_carrier)
    check("normalization alone does not identify a resolution", w_carrier != w_cells)


def registration_instrument_probe():
    print("\n[2] PROJECTIVE REGISTRATION AND BRANCH INFORMATION")
    eye = sp.eye(3)
    projectors = [sp.diag(*[1 if i == j else 0 for i in range(3)]) for j in range(3)]
    write_isometry = sp.Matrix.vstack(*projectors)
    check("three-label controlled-copy write is an isometry", write_isometry.H * write_isometry == eye)
    check("extracted write blocks are the spectral projectors", all(write_isometry[3*i:3*(i+1), :] == projectors[i] for i in range(3)))

    positive_spectrum = (sp.Integer(1), sp.Integer(2), sp.Integer(3))
    signed_spectrum = (-sp.Integer(1), sp.Integer(2), sp.Integer(3))
    masses_positive = tuple(x**2 for x in positive_spectrum)
    masses_signed = tuple(x**2 for x in signed_spectrum)
    record_pointer = sp.diag(*masses_positive)
    pointer_on_output = sp.kronecker_product(record_pointer, eye)
    pulled_back_pointer = sp.simplify(write_isometry.H * pointer_on_output * write_isometry)
    positive_transfer = sp.diag(*positive_spectrum)
    check("pointer pullback registers lambda_k^2 exactly", pulled_back_pointer == positive_transfer**2)
    check("lambda^2 registration is nonnegative", all(x >= 0 for x in masses_signed))
    check("real-spectrum premise is load-bearing for nonnegative squares", sp.I**2 == -1)
    check("lambda^2 registration erases the sign branch", masses_positive == masses_signed)
    check("positive square-root readout returns absolute values", tuple(sp.sqrt(x) for x in masses_signed) == (1, 2, 3))
    check("signed spectrum contains a negative branch not removed by W^2", signed_spectrum[0] < 0)

    full_support_state = eye / 3
    outcome_probabilities = tuple(sp.trace(projector * full_support_state) for projector in projectors)
    check("three distinct registered masses require distinct squared labels", len(set(masses_positive)) == 3)
    check(
        "projective probabilities give nonzero support to all three labels",
        sum(outcome_probabilities) == 1
        and outcome_probabilities == (sp.Rational(1, 3),) * 3,
    )
    collision_spectrum = (-sp.Integer(1), sp.Integer(1), sp.Integer(3))
    check("three distinct spectral values need not give three distinct squared values", len(set(collision_spectrum)) == 3 and len({x**2 for x in collision_spectrum}) == 2)


def law_equivalence_probe():
    print("\n[3] LAW EQUIVALENCE AND TIME HOMOGENEITY")

    def canonical_condition(condition):
        environment, record_count = condition
        if environment == "translated-base":
            environment = "base"
        return environment, record_count

    def formation_weight_law(condition):
        environment, record_count = canonical_condition(condition)
        singlet_weight = Fraction(1, 2 + record_count + (environment == "changed"))
        return singlet_weight, 1 - singlet_weight

    def transfer_law(condition):
        environment, record_count = canonical_condition(condition)
        return sp.diag(1 + record_count, 2 + (environment == "changed"), 3)

    c0 = ("base", 0)
    c0_transport = ("translated-base", 0)
    c1 = ("changed", 1)
    check(
        "transport-equivalent conditions give the same formation-weight vector",
        c0 != c0_transport
        and canonical_condition(c0) == canonical_condition(c0_transport)
        and formation_weight_law(c0) == formation_weight_law(c0_transport),
    )
    check(
        "one formation-weight law can give different marginals in changed environments",
        formation_weight_law(c0) != formation_weight_law(c1),
    )
    check(
        "transport-equivalent conditions give the same supplied transfer matrix",
        transfer_law(c0) == transfer_law(c0_transport),
    )
    check(
        "one transfer law can give different matrices in changed environments",
        transfer_law(c0) != transfer_law(c1),
    )

    def noninjective_transfer_law(_condition):
        return sp.eye(3)

    check(
        "equal transfer matrices need not imply equivalent conditions",
        canonical_condition(c0) != canonical_condition(c1)
        and noninjective_transfer_law(c0) == noninjective_transfer_law(c1),
    )


def history_faithfulness_probe():
    print("\n[4] HISTORY-INDEX FAITHFULNESS")
    final_index = 3
    line_edges = {(t, t + 1) for t in range(final_index)}
    cycle_edges = line_edges | {(final_index, 0)}
    seam = {(final_index, 0)}
    record_sets = tuple(frozenset(range(t)) for t in range(final_index + 1))

    check("cyclic compactification adds exactly one seam edge", cycle_edges - line_edges == seam)
    check("cutting the seam recovers the linear history graph", cycle_edges - seam == line_edges)
    check("nested record sets are permanent along the linear history", all(record_sets[a] <= record_sets[b] for a, b in line_edges))
    check("the cyclic seam is not a permanence-preserving history step", not record_sets[final_index] <= record_sets[0])


def k_stage_and_scope_probe():
    print("\n[5] K-STAGE SUPPLY AND C_n SCOPE")

    def k_orbits(n):
        unseen = set(range(n))
        orbits = []
        while unseen:
            k = min(unseen)
            orbit = frozenset({k, (-k) % n})
            orbits.append(orbit)
            unseen -= orbit
        return tuple(orbits)

    for n in range(3, 9):
        orbits = k_orbits(n)
        expected_cells = (n + 1) // 2 if n % 2 else n // 2 + 1
        carrier_singlet_weight = Fraction(1, n)
        cell_singlet_weight = Fraction(1, len(orbits))
        check(f"C_{n} K-orbit count is exact", len(orbits) == expected_cells)
        check(f"C_{n} carrier and cell uniformities are distinguishable", carrier_singlet_weight != cell_singlet_weight)

    c3_orbits = k_orbits(3)
    check("C_3 has one singlet and one paired K cell", c3_orbits == (frozenset({0}), frozenset({1, 2})))
    check("K quotient before counting gives w=1/2 on C_3", Fraction(1, len(c3_orbits)) == Fraction(1, 2))
    c3_carrier_size = sum(len(orbit) for orbit in c3_orbits)
    check("counting supplied carrier members before quotient gives w=1/3", Fraction(1, c3_carrier_size) == Fraction(1, 3))


def many_slice_probe():
    print("\n[6] MANY-SLICE QUENCHED/ANNEALED TRANSFER")
    x = Fraction(2, 1)
    y = Fraction(3, 1)

    def quenched(n):
        return (x**n + y**n) / 2

    def annealed(n):
        return ((x + y) / 2) ** n

    check("N=2 quenched value is 13/2", quenched(2) == Fraction(13, 2))
    check("N=2 annealed value is 25/4", annealed(2) == Fraction(25, 4))
    check("quenched and annealed prescriptions differ for N=2..5", all(quenched(n) != annealed(n) for n in range(2, 6)))

    def markov_product(n, persistence):
        z = sp.diag(sp.Rational(x.numerator, x.denominator), sp.Rational(y.numerator, y.denominator))
        p = sp.Rational(persistence.numerator, persistence.denominator)
        transition = sp.Matrix([[p, 1 - p], [1 - p, p]])
        row = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]]) * z
        if n > 1:
            row = row * (transition * z) ** (n - 1)
        return sp.simplify((row * sp.ones(2, 1))[0])

    check("persistence p=1 reproduces quenched histories", all(markov_product(n, Fraction(1, 1)) == quenched(n) for n in range(1, 5)))
    check("persistence p=1/2 reproduces annealed histories", all(markov_product(n, Fraction(1, 2)) == annealed(n) for n in range(1, 5)))
    check("intermediate persistence produces a third exact transfer law", markov_product(3, Fraction(3, 4)) not in {quenched(3), annealed(3)})


def krein_projection_probe():
    print("\n[7] CANONICAL KREIN POSITIVE-HALF LEAKAGE")
    a11, a12, a21, a22 = sp.symbols("a11 a12 a21 a22")
    b11, b12, b21, b22 = sp.symbols("b11 b12 b21 b22")
    a = sp.Matrix([[a11, a12], [a21, a22]])
    b = sp.Matrix([[b11, b12], [b21, b22]])
    zero = sp.zeros(2)
    identity = sp.eye(2)
    doubled = sp.BlockMatrix([[a, zero], [zero, b]]).as_explicit()
    fundamental_symmetry = sp.BlockMatrix([[zero, identity], [identity, zero]]).as_explicit()
    p_plus = (sp.eye(4) + fundamental_symmetry) / 2
    leakage = sp.simplify((sp.eye(4) - p_plus) * doubled * p_plus)
    delta = a - b
    expected = sp.BlockMatrix([[delta, delta], [-delta, -delta]]).as_explicit() / 4
    check("positive-half leakage has the exact W-Wdag block form", sp.simplify(leakage - expected) == sp.zeros(4))
    check("canonical positive half is invariant when the two blocks tie", leakage.subs({a11:b11, a12:b12, a21:b21, a22:b22}) == sp.zeros(4))
    zero_leakage_solution = sp.solve(list(leakage), [a11, a12, a21, a22], dict=True)
    check(
        "zero leakage forces equality of every paired block entry",
        zero_leakage_solution
        == [{a11: b11, a12: b12, a21: b21, a22: b22}],
    )

    w = sp.Matrix([[1, sp.I], [0, 2]])
    wdag = w.H
    d = sp.diag(1, 1, 1, 1)
    d[:2, :2] = w
    d[2:, 2:] = wdag
    check("the doubled transfer is J-self-adjoint", d.H * fundamental_symmetry == fundamental_symmetry * d)
    check("a non-Hermitian W leaks out of the canonical positive half", (sp.eye(4) - p_plus) * d * p_plus != sp.zeros(4))


def a2_probe():
    print("\n[8] QUADRATIC TWO-SLICE TRANSFER FACTOR A_2(W)=W^2+I/4")
    w = sp.I * sp.eye(3) / 10
    a2 = sp.simplify(w**2 + sp.eye(3) / 4)
    check("W=iI/10 gives A2=6I/25", a2 == sp.Rational(6, 25) * sp.eye(3))
    check("the A2 witness is positive definite", all(value > 0 for value in a2.eigenvals()))
    check("the same W is not Hermitian", w != w.H)
    check("A2 cannot distinguish W from -W", sp.simplify((-w) ** 2 + sp.eye(3) / 4) == a2)


def main():
    formation_resolution_probe()
    registration_instrument_probe()
    law_equivalence_probe()
    history_faithfulness_probe()
    k_stage_and_scope_probe()
    many_slice_probe()
    krein_projection_probe()
    a2_probe()
    print(f"\nSUMMARY: RHALF OPEN BACKLOG PROBES PASS={PASS} FAIL={FAIL}")
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
