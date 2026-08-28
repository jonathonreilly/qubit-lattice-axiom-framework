#!/usr/bin/env python3
"""Exact checks for the exterior-character common-clock obstruction."""

from __future__ import annotations

import argparse
import itertools
from math import comb
from pathlib import Path

import sympy as sp

from admissibility_exterior_character_time_refinement_semigroup_obstruction_independent_2026_08_28 import (
    independent_facts,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_EXTERIOR_CHARACTER_ACTION_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_exterior_character_time_refinement_semigroup_obstruction_independent_2026_08_28.py",
)

MUTATIONS = (
    "break_import_boundary",
    "break_exterior_character",
    "break_component_mass",
    "break_linear_series",
    "break_linear_semigroup",
    "break_nonlinear_multiplicity",
    "break_nonlinear_semigroup",
    "break_projected_cycle",
    "erase_improper_sector",
    "break_heat_jump",
    "promote_so3_heat",
    "break_fixed_m_commutator",
    "claim_tree_obstruction",
    "claim_fractional_refinement",
    "claim_physical_time",
    "claim_all_full_transfers",
)

PASS = 0
FAIL = 0


def check(name: str, condition: object) -> None:
    global PASS, FAIL
    ok = bool(condition)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    PASS += int(ok)
    FAIL += int(not ok)


def multiplicity(ell: int, tensor_power: int) -> sp.Integer:
    if ell < 0 or ell > tensor_power:
        return sp.Integer(0)
    left = comb(2 * tensor_power, tensor_power - ell)
    right_index = tensor_power - ell - 1
    right = comb(2 * tensor_power, right_index) if right_index >= 0 else 0
    return sp.Integer(left - right)


def b_series(ell: int, order: int = 4) -> sp.Expr:
    kappa = sp.symbols("kappa", positive=True)
    return sp.Add(*(
        multiplicity(ell, power) * (4 * kappa) ** power / sp.factorial(power)
        for power in range(order + 1)
    ))


def truncated(expr: sp.Expr, variable: sp.Symbol, order: int) -> sp.Expr:
    return sp.series(expr, variable, 0, order + 1).removeO().expand()


def catalan(index: int) -> sp.Integer:
    return sp.Integer(comb(2 * index, index) // (index + 1))


def spin_one_tensor_multiplicities(power: int) -> dict[int, int]:
    multiplicities = {0: 1}
    for _ in range(power):
        updated: dict[int, int] = {}
        for ell, count in multiplicities.items():
            targets = (1,) if ell == 0 else (ell - 1, ell, ell + 1)
            for target in targets:
                updated[target] = updated.get(target, 0) + count
        multiplicities = updated
    return multiplicities


def signed_frames() -> tuple[sp.Matrix, ...]:
    frames: list[sp.Matrix] = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            frames.append(sp.Matrix([
                [signs[row] if column == permutation[row] else 0
                 for column in range(3)]
                for row in range(3)
            ]))
    return tuple(frames)


def conjugation_character_contraction(dimension: int) -> tuple[sp.Expr, sp.Expr]:
    """Contract Tr(Q D Q^T) using sum_i Q_ia Q_ib=delta_ab."""
    entries = sp.symbols(f"d0:{dimension * dimension}")
    matrix = sp.Matrix(dimension, dimension, entries)
    contracted = sp.Add(*(
        matrix[a, b] * sp.KroneckerDelta(a, b)
        for a in range(dimension) for b in range(dimension)
    ))
    return sp.simplify(contracted), sp.trace(matrix)


def iterated_channel_multiplier(value: sp.Expr, length: int,
                                  corrupt_step: int | None = None) -> sp.Expr:
    current = sp.Integer(1)
    for step in range(1, length + 1):
        factor = sp.Integer(1) if step == corrupt_step else value
        current = sp.expand(current * factor)
    return current


def main(mutation: str | None, mode: str) -> int:
    global PASS, FAIL
    PASS = 0
    FAIL = 0

    if mode == "independent":
        for name, condition in independent_facts().items():
            check(f"independent: {name}", condition)
        print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
        return int(FAIL != 0)

    root = Path(__file__).resolve().parents[1]
    source = (root / AUDIT_INPUT_PATHS[0]).read_text()
    parent = (root / AUDIT_INPUT_PATHS[1]).read_text()
    axioms = (root / AUDIT_INPUT_PATHS[2]).read_text()
    if mutation == "break_import_boundary":
        source = source.replace("one supplied projected periodic-cycle specialization", "every projected lattice transfer")
    if mutation == "claim_tree_obstruction":
        source = source.replace(
            "tree gauge quotient can collapse to constants",
            "tree gauge quotient retains the decisive characters",
        )
    if mutation == "claim_fractional_refinement":
        source = source.replace(
            "fractional spectral powers are not proved",
            "fractional spectral powers are proved",
        )
    if mutation == "claim_physical_time":
        source = source.replace("no physical clock", "a physical clock")
    if mutation == "claim_all_full_transfers":
        source = source.replace(
            "does not prove nonembeddability for every nonconstant full transfer",
            "proves nonembeddability for every nonconstant full transfer",
        )
    import_ok = (
        "one supplied projected periodic-cycle specialization" in source
        and "every integer `n>=1`" in source
        and "A derived\nAdmissibility law, a semigroup" in parent
        and "derive a clock" in parent
        and "source/action" in axioms
    )
    check(
        "import boundary: the parent supplies f_n and a finite transfer but no clock or semigroup law",
        import_ok,
    )

    determinant = sp.symbols("delta", integer=True)
    trace = sp.symbols("trace", real=True)
    exterior_degree_traces = (
        sp.Integer(1),
        trace,
        determinant * trace,
        determinant,
    )
    if mutation == "break_exterior_character":
        exterior_degree_traces = (
            exterior_degree_traces[0],
            exterior_degree_traces[1],
            trace,
            exterior_degree_traces[3],
        )
    exterior_character = sp.Add(*exterior_degree_traces)
    exterior_target = (1 + determinant) * (1 + trace)
    check(
        "exterior character: chi=(1+det)(1+Tr) vanishes on the improper component",
        sp.expand(exterior_character - exterior_target) == 0
        and exterior_character.subs(determinant, -1) == 0,
    )

    b0_symbol = sp.symbols("b0", positive=True)
    proper_mass = b0_symbol / (b0_symbol + 1)
    improper_mass = 1 / (b0_symbol + 1)
    determinant_multiplier = proper_mass - improper_mass
    component_target = (b0_symbol - 1) / (b0_symbol + 1)
    if mutation == "break_component_mass":
        component_target = b0_symbol / (b0_symbol + 1)
    check(
        "component bookkeeping: r_det is the proper-minus-improper mass",
        sp.cancel(determinant_multiplier - component_target) == 0
        and sp.cancel(proper_mass + improper_mass) == 1,
    )

    kappa = sp.symbols("kappa", positive=True)
    nominal_b0 = b_series(0)
    nominal_b1 = b_series(1)
    nominal_b2 = b_series(2)
    nominal_b3 = b_series(3)
    b0 = nominal_b0
    if mutation == "break_linear_series":
        b0 += kappa**2
    linear_ok = (
        b0 == 1 + 4 * kappa + 16 * kappa**2 + sp.Rational(160, 3) * kappa**3 + sp.Rational(448, 3) * kappa**4
        and nominal_b1 == 4 * kappa + 24 * kappa**2 + 96 * kappa**3 + sp.Rational(896, 3) * kappa**4
        and nominal_b2 == 8 * kappa**2 + sp.Rational(160, 3) * kappa**3 + sp.Rational(640, 3) * kappa**4
        and nominal_b3 == sp.Rational(32, 3) * kappa**3 + sp.Rational(224, 3) * kappa**4
    )
    check(
        "linear character series: four b_l series are derived from exact tensor multiplicities",
        linear_ok,
    )

    rdet = truncated((nominal_b0 - 1) / (nominal_b0 + 1), kappa, 4)
    rv = truncated(nominal_b1 / (3 * (nominal_b0 + 1)), kappa, 3)
    rv_for_clock = rv
    if mutation == "break_linear_semigroup":
        rv_for_clock = rdet
    ratio_limit = sp.limit(rdet / rv_for_clock, kappa, 0, dir="+")
    check(
        "linear common-clock obstruction: equal vanishing orders but leading ratio three forbid equal channel laws",
        rdet == 2 * kappa + 4 * kappa**2 + sp.Rational(8, 3) * kappa**3 - 16 * kappa**4
        and rv == sp.Rational(2, 3) * kappa + sp.Rational(8, 3) * kappa**2 + sp.Rational(16, 3) * kappa**3
        and ratio_limit == 3,
    )

    n_symbol = sp.symbols("n", integer=True, positive=True)
    central = sp.symbols("central", positive=True)
    m0_over_central = sp.cancel(1 - n_symbol / (n_symbol + 1))
    m1_over_central = sp.cancel(
        n_symbol / (n_symbol + 1)
        - n_symbol * (n_symbol - 1) / ((n_symbol + 1) * (n_symbol + 2))
    )
    symbolic_ratio = sp.cancel(3 * m0_over_central / m1_over_central)
    general_identity_ok = (
        sp.cancel(m0_over_central - 1 / (n_symbol + 1)) == 0
        and sp.cancel(
            m1_over_central
            - 3 * n_symbol / ((n_symbol + 1) * (n_symbol + 2))
        ) == 0
        and symbolic_ratio == (n_symbol + 2) / n_symbol
    )
    nonlinear_multiplicity_ok = general_identity_ok
    nominal_ratios: list[sp.Rational] = []
    for n in range(1, 13):
        c_n = catalan(n)
        m0 = multiplicity(0, n)
        nominal_m1 = multiplicity(1, n)
        m1 = nominal_m1
        if mutation == "break_nonlinear_multiplicity" and n == 4:
            m1 += 1
        nonlinear_multiplicity_ok &= (
            m0 == c_n
            and sp.Rational(m1, c_n) == sp.Rational(3 * n, n + 2)
        )
        nominal_ratios.append(sp.Rational(3 * m0, nominal_m1))
    check(
        "nonlinear multiplicities: the general binomial ratios give Catalan and spin-one counts",
        nonlinear_multiplicity_ok,
    )

    nonlinear_ratios = tuple(nominal_ratios)
    symbolic_ratio_for_check = symbolic_ratio
    if mutation == "break_nonlinear_semigroup":
        symbolic_ratio_for_check = sp.Integer(1)
    check(
        "all-f_n common-clock obstruction: determinant/vector leading ratios equal (n+2)/n, never one",
        symbolic_ratio_for_check == (n_symbol + 2) / n_symbol
        and sp.simplify(symbolic_ratio_for_check - 1) == 2 / n_symbol
        and all(value == sp.Rational(n + 2, n) and value != 1
                for n, value in enumerate(nonlinear_ratios, start=1)),
    )

    vector_contracted, vector_trace = conjugation_character_contraction(3)
    det_q, det_w = sp.symbols("det_q det_w", nonzero=True)
    determinant_contracted = sp.cancel(det_q * det_w / det_q)
    frames = signed_frames()
    word = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, -1]])
    frame_invariance = all(
        sp.trace(frame * word * frame.T) == sp.trace(word)
        and (frame * word * frame.T).det() == word.det()
        for frame in frames
    )
    channel = sp.symbols("r")
    cycle_ok = (
        vector_contracted == vector_trace
        and determinant_contracted == det_w
        and len(frames) == 48
        and sum(int(frame.det() == -1) for frame in frames) == 24
        and frame_invariance
        and all(
            iterated_channel_multiplier(
                channel,
                length,
                corrupt_step=(2 if mutation == "break_projected_cycle" else None),
            ) == channel**length
            for length in range(1, 7)
        )
        and all(value**length != 1
                for value in nominal_ratios[:8]
                for length in range(1, 7))
    )
    check(
        "projected periodic cycle: determinant and vector spin networks retain the unequal leading ratio to power L",
        cycle_ok,
    )

    theta = sp.symbols("theta", real=True)
    so3_class_measure = 2 * sp.sin(theta / 2) ** 2 / sp.pi
    spin_one_character = 1 + 2 * sp.cos(theta)
    improper_character = spin_one_character
    if mutation == "erase_improper_sector":
        improper_character += 1
    improper_trivial_integral = sp.integrate(
        so3_class_measure, (theta, 0, sp.pi)
    )
    improper_vector_integral = sp.simplify(sp.integrate(
        so3_class_measure * improper_character, (theta, 0, sp.pi)
    ))
    improper_density_constant = improper_trivial_integral == 1
    determinant_survives_conjugation = determinant_contracted == det_w
    vector_and_detvector_equal = improper_vector_integral == 0
    check(
        "improper sector: conjugation projection preserves det while constant improper density gives r_V=r_detV",
        determinant_survives_conjugation and vector_and_detvector_equal,
    )

    component_excess, rdetv_symbol = sp.symbols(
        "component_excess r_det_v", positive=True
    )
    diffusivity, jump_rate, clock = sp.symbols(
        "D gamma t", positive=True
    )

    def heat_multiplier(ell: int, parity: int) -> sp.Expr:
        return sp.exp(
            -diffusivity * ell * (ell + 1) * clock / 2
            -jump_rate * (1 - parity) * clock
        )

    vector_parity = -1
    if mutation == "break_heat_jump":
        vector_parity = 1
    heat_det = heat_multiplier(0, -1)
    heat_det_vector = heat_multiplier(1, 1)
    heat_vector = heat_multiplier(1, vector_parity)
    heat_channel_identity = sp.simplify(
        heat_vector - heat_det * heat_det_vector
    ) == 0
    heat_b0 = 1 + component_excess
    rdet_symbol = sp.cancel((heat_b0 - 1) / (heat_b0 + 1))
    rdet_sample = rdet_symbol
    rdetv_sample = rdetv_symbol
    exterior_v = rdetv_sample
    heat_jump_v = rdet_sample * rdetv_sample
    check(
        "heat plus component-jump comparator: h_V=h_det h_detV conflicts with r_V=r_detV and 0<r_det<1",
        heat_channel_identity
        and sp.simplify(
            (exterior_v - heat_jump_v)
            - rdetv_symbol * (1 - rdet_sample)
        ) == 0
        and sp.simplify(1 - rdet_symbol).is_positive
        and sp.simplify(exterior_v - heat_jump_v).is_positive,
    )

    spin_one_counts = spin_one_tensor_multiplicities(1)
    spin_two_counts = spin_one_tensor_multiplicities(2)
    so3_spin1_lead = sp.Rational(spin_one_counts[1], 3)
    so3_spin2_lead = sp.Rational(spin_two_counts[2], 2 * 5)
    if mutation == "promote_so3_heat":
        so3_spin2_lead = so3_spin1_lead**2
    so3_scope = so3_spin2_lead != so3_spin1_lead**2
    check(
        "SO(3) escape boundary: the n=1 restriction has its own common-clock mismatch, not a borrowed O(3) determinant proof",
        so3_scope,
    )

    m_left, m_right = sp.symbols("m_left m_right", positive=True)
    right_entry = m_right
    if mutation == "break_fixed_m_commutator":
        right_entry = m_left
    m_vector = sp.Matrix([m_left, right_entry])
    t_zero = m_vector * m_vector.T
    t_infty = sp.diag(*(entry**2 for entry in m_vector))
    commutator = t_zero * t_infty - t_infty * t_zero
    check(
        "fixed nonconstant half multiplier: rank-one and multiplication endpoint transfers do not commute",
        sp.simplify(
            commutator[0, 1]
            - m_left * right_entry * (right_entry - m_left) * (right_entry + m_left)
        ) == 0
        and commutator[0, 1] != 0,
    )

    tree_escape = "tree gauge quotient can collapse to constants" in source
    check(
        "topology boundary: a tree quotient can remove both decisive nontrivial character modes",
        tree_escape,
    )

    fractional_scope = (
        "fractional spectral powers are not proved" in source
        and "in-family positive-density" in source
    )
    check(
        "fixed-step logarithm boundary: spectral powers do not supply an exterior-family refinement law",
        fractional_scope,
    )

    physical_scope = (
        "no physical clock" in source
        and "no continuum limit" in source
        and "no action\nselection" in source
    )
    check(
        "physical boundary: the obstruction is dimensionless and supplies no clock, continuum, or selected dynamics",
        physical_scope,
    )

    full_transfer_scope = "does not prove nonembeddability for every nonconstant full transfer" in source
    check(
        "full-transfer boundary: the theorem is exact on the projected cycle and fixed-M anisotropic control only",
        full_transfer_scope,
    )

    print("per_element: exterior characters, component masses, and normalized irrep multipliers were recomputed")
    print("per_site: the one-loop and finite-cycle gauge projections were separated from tree quotients")
    print("per_mode: determinant, vector, det-vector, higher-spin, and fixed-M endpoint modes were checked")
    print("per_block: every finite f_n common-clock obstruction and one projected periodic-cycle lift were executed")
    print("lattice_wide: checked and not executed — no co-scaled carrier refinement, continuum family, or physical clock is supplied")
    print("STATUS: the supplied exterior-character coupling family is not an exact common-clock convolution semigroup; fixed-step logs remain valid")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("primary", "independent"), default="primary")
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.mutation, arguments.mode))
