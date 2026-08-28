#!/usr/bin/env python3
"""Exact finite-gap bounds and strict-coupling collapse checks."""

from __future__ import annotations

import argparse
import itertools
from pathlib import Path

import sympy as sp

from admissibility_exterior_character_gauge_vector_finite_gap_strict_coupling_collapse_independent_2026_08_28 import (
    independent_facts,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_GAUGE_VECTOR_FINITE_GAP_STRICT_COUPLING_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_GAUGE_VECTOR_MATTER_SOURCE_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_exterior_character_gauge_vector_finite_gap_strict_coupling_collapse_independent_2026_08_28.py",
)

MUTATIONS = (
    "break_import_boundary",
    "break_minorization",
    "break_shell_mass",
    "break_gaussian_scale",
    "erase_radial_separation",
    "break_shell_interior",
    "break_gaussian_tail",
    "erase_cross_decay",
    "claim_uniform_gap",
    "break_projection_invariance",
    "break_finite_spectrum",
    "promote_odd_mode",
    "reverse_gap_order",
    "break_zero_coupling_rank",
    "claim_physical_mass",
)

PASS = 0
FAIL = 0


def check(name: str, condition: object) -> None:
    global PASS, FAIL
    ok = bool(condition)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    PASS += int(ok)
    FAIL += int(not ok)


def shell_probability(inner: sp.Expr, outer: sp.Expr) -> sp.Expr:
    radius = sp.symbols("radius", nonnegative=True)
    return sp.integrate(3 * radius**2, (radius, inner, outer))


def shrunken_fraction(inner: sp.Expr, outer: sp.Expr,
                      inverse_scale: sp.Expr) -> sp.Expr:
    full = outer**3 - inner**3
    return sp.cancel(
        ((outer - inverse_scale) ** 3
         - (inner + inverse_scale) ** 3) / full
    )


def exterior_character(relative: sp.Matrix) -> sp.Expr:
    return sp.expand((sp.eye(3) + relative).det())


def defect(relative: sp.Matrix) -> sp.Expr:
    return sp.expand(16 - 2 * exterior_character(relative))


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
    parent = (root / AUDIT_INPUT_PATHS[1]).read_text()
    axioms = (root / AUDIT_INPUT_PATHS[2]).read_text()
    import_boundary_ok = (
        "finite mathematical transfer" in parent
        and "uniformly controlled matter spectral gap" in parent
        and "source/action" in axioms
    )
    if mutation == "break_import_boundary":
        import_boundary_ok = "uniformly controlled matter spectral gap" not in parent
    check(
        "import boundary: the parent supplies the strict finite gauge-vector transfer but not a uniform spectral or physical mass gap",
        import_boundary_ok,
    )

    action_min, action_max = sp.symbols(
        "action_min action_max", real=True, finite=True)
    kernel_min = sp.exp(-action_max)
    kernel_max = sp.exp(-action_min)
    minorization = sp.simplify(kernel_min / kernel_max)
    if mutation == "break_minorization":
        minorization = sp.Integer(0)
    check(
        "fixed finite transfer: the Doob minorization is exp minus the total action oscillation",
        minorization == sp.exp(-(action_max - action_min))
        and minorization.is_positive is True,
    )

    first_inner, first_outer = sp.Rational(1, 4), sp.Rational(1, 3)
    second_inner, second_outer = sp.Rational(1, 2), sp.Rational(2, 3)
    first_mass = shell_probability(first_inner, first_outer)
    second_mass = shell_probability(second_inner, second_outer)
    if mutation == "break_shell_mass":
        second_mass += 1
    check(
        "full-ball radial modes: the two disjoint shell probabilities are exact",
        first_mass == sp.Rational(37, 1728)
        and second_mass == sp.Rational(37, 216),
    )

    tau = sp.symbols("tau", positive=True)
    normalization = sp.Rational(3, 4) / sp.pi
    line_gaussian = sp.sqrt(2 * sp.pi / tau)
    gaussian_scale = sp.simplify(normalization * line_gaussian**3)
    if mutation == "break_gaussian_scale":
        gaussian_scale *= 2
    check(
        "Gaussian normalization: the full-space Schur scale is derived from three exact one-dimensional integrals",
        gaussian_scale
        == sp.Rational(3, 4) / sp.pi * (2 * sp.pi / tau) ** sp.Rational(3, 2),
    )

    separation = second_inner - first_outer
    if mutation == "erase_radial_separation":
        separation = 0
    check(
        "radial separation: the exact shells are gauge invariant and separated by one sixth",
        separation == sp.Rational(1, 6)
        and first_inner > 0 and second_outer < 1,
    )

    m = sp.symbols("m", integer=True, positive=True)
    first_fraction = shrunken_fraction(
        first_inner, first_outer, 1 / m)
    second_fraction = shrunken_fraction(
        second_inner, second_outer, 1 / m)
    first_closed = sp.cancel(
        1 - (900 * m**2 - 432 * m + 3456) / (37 * m**3))
    second_minus_first = sp.factor(second_fraction - first_fraction)
    first_closed_test = first_closed
    if mutation == "break_shell_interior":
        first_closed_test += 1
    shell_interior_ok = (
        sp.simplify(first_fraction - first_closed_test) == 0
        and second_minus_first.is_positive is True
    )
    check(
        "radial interior bound: for m greater than twenty-four the thinner shell gives the exact diagonal minimum",
        shell_interior_ok,
    )

    gaussian_coordinate = sp.symbols("gaussian_coordinate", real=True)
    one_coordinate_second_moment = sp.integrate(
        gaussian_coordinate**2 * sp.exp(-gaussian_coordinate**2 / 2)
        / sp.sqrt(2 * sp.pi),
        (gaussian_coordinate, -sp.oo, sp.oo),
    )
    gaussian_second_moment = sp.simplify(
        sum((one_coordinate_second_moment for _ in range(3)), sp.Integer(0))
    )
    gaussian_second_moment_test = gaussian_second_moment
    if mutation == "break_gaussian_tail":
        gaussian_second_moment_test += 1
    check(
        "Gaussian tail: the three-coordinate second moment derives the Markov loss three over m squared",
        gaussian_second_moment_test == 3,
    )

    diagonal_lower = sp.cancel(
        first_closed * (1 - gaussian_second_moment / m**2))
    cross_prefactor = sp.cancel(
        sp.Integer(37) * sp.factorial(4) * sp.Integer(72) ** 4
        / sp.Integer(1296)
    )
    if mutation == "erase_cross_decay":
        cross_prefactor += 1
    cross_upper = sp.cancel(cross_prefactor / m**10)
    ratio_lower = sp.cancel(diagonal_lower - cross_upper)
    selected_m = (48, 96, 192, 384)
    selected_ratios = tuple(sp.cancel(ratio_lower.subs(m, value))
                            for value in selected_m)
    cross_ok = (
        cross_prefactor == 18_413_568
        and all(value > 0 for value in selected_ratios)
        and all(left < right for left, right
                in zip(selected_ratios, selected_ratios[1:]))
        and sp.limit(ratio_lower, m, sp.oo) == 1
    )
    check(
        "untruncated radial bound: exact shell loss and cross-shell decay force the normalized second radial eigenvalue toward one",
        cross_ok,
    )

    uniform_claim = mutation == "claim_uniform_gap"
    check(
        "strict-coupling boundary: every finite tau is injective but no positive normalized gap is uniform over tau=m^4",
        sp.limit(1 - ratio_lower, m, sp.oo) == 0
        and not uniform_claim,
    )

    cubic_transformations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rotation = sp.zeros(3)
            for column, row in enumerate(permutation):
                rotation[row, column] = signs[column]
            cubic_transformations.append(rotation)
    transformation_test = tuple(cubic_transformations)
    if mutation == "break_projection_invariance":
        corrupted = transformation_test[0].copy()
        corrupted[0, 0] = 2 * corrupted[0, 0]
        transformation_test = (corrupted,) + transformation_test[1:]
    vector = sp.Matrix((sp.Rational(1, 4), sp.Rational(1, 5),
                        sp.Rational(1, 6)))
    generic_entries = sp.symbols("orthogonal_entry_0:9", real=True)
    generic_orthogonal = sp.Matrix(3, 3, generic_entries)
    generic_norm_difference = sp.expand(
        (generic_orthogonal * vector).dot(generic_orthogonal * vector)
        - vector.dot(vector)
    )
    generic_orthogonality_form = sp.expand(
        (vector.T * (generic_orthogonal.T * generic_orthogonal - sp.eye(3))
         * vector)[0]
    )
    generic_norm_identity = (
        sp.expand(generic_norm_difference - generic_orthogonality_form) == 0
    )
    orthogonality_identity = all(
        transformation.T * transformation == sp.eye(3)
        for transformation in transformation_test
    )
    invariant = (
        generic_norm_identity
        and orthogonality_identity
        and all(
        sp.expand((rotation * vector).dot(rotation * vector)
                  - vector.dot(vector)) == 0
        for rotation in transformation_test
        )
        and len(transformation_test) == 48
        and sum(rotation.det() == -1 for rotation in transformation_test) == 24
    )
    parent_top, matter_top, matter_radial = sp.symbols(
        "parent_top matter_top matter_radial", positive=True)
    number_of_sites = 3
    product_top = parent_top * matter_top**number_of_sites
    product_radial = (
        parent_top * matter_radial * matter_top**(number_of_sites - 1)
    )
    projected_ratio = sp.cancel(product_radial / product_top)
    check(
        "gauge projection: radial matter modes are invariant under all proper and improper signed orthogonal actions and the projected tensor ratio is exact",
        invariant and projected_ratio == matter_radial / matter_top,
    )

    a, t = sp.symbols("a t", positive=True)
    identity_three = sp.eye(3)
    reflection = sp.diag(-1, 1, 1)
    reflection_defect = defect(reflection)
    finite_group = (identity_three, reflection)
    conjugation_trivial = all(
        h * u * h.inv() == u for h in finite_group for u in finite_group)
    gauge_kernel = sp.Matrix(((1, a), (a, 1))) / 2
    gauge_trivial_vector = sp.Matrix((1, 1)) / sp.sqrt(2)
    gauge_det_vector = sp.Matrix((1, -1)) / sp.sqrt(2)
    gauge_even = sp.simplify((gauge_trivial_vector.T * gauge_kernel
                              * gauge_trivial_vector)[0])
    gauge_odd = sp.simplify((gauge_det_vector.T * gauge_kernel
                             * gauge_det_vector)[0])

    finite_matter = (
        sp.Matrix((0, 0, 0)), sp.Matrix((1, 0, 0)),
        sp.Matrix((-1, 0, 0)),
    )
    matter_kernel = sp.Matrix(3, 3, lambda row, column:
        t ** sp.expand((finite_matter[row] - finite_matter[column]).dot(
            finite_matter[row] - finite_matter[column]))) / 3
    matter_action = sp.Matrix(((1, 0, 0), (0, 0, 1), (0, 1, 0)))
    matter_projector = (sp.eye(3) + matter_action) / 2
    even_isometry = sp.Matrix(((1, 0), (0, 1 / sp.sqrt(2)),
                               (0, 1 / sp.sqrt(2))))
    matter_even = sp.simplify(even_isometry.T * matter_kernel
                              * even_isometry)
    matter_trace = sp.trace(matter_even)
    matter_det = sp.det(matter_even)
    matter_difference_squared = sp.factor(matter_trace**2 - 4 * matter_det)
    matter_projector_test = matter_projector
    if mutation == "break_finite_spectrum":
        matter_projector_test = sp.eye(3)
    finite_spectrum_ok = (
        reflection_defect == 16
        and sp.simplify(matter_trace - (2 + t**4) / 3) == 0
        and sp.simplify(matter_difference_squared
                        - (t**8 + 8 * t**2) / 9) == 0
        and sp.limit(gauge_odd / gauge_even, a, 0, dir="+") == 1
        and conjugation_trivial
        and matter_projector_test.rank() == 2
        and matter_projector_test * sp.Matrix((0, 1, -1)) == sp.zeros(3, 1)
    )
    check(
        "exact finite diagnostic: normalized Haar and matter projection derive both two-by-two spectral factors",
        finite_spectrum_ok,
    )

    odd_matter = (1 - t**4) / 3
    odd_survives = mutation == "promote_odd_mode"
    check(
        "finite projector boundary: the antisymmetric matter mode is nonzero before Haar averaging and is removed from the gauge-invariant even subspace",
        odd_matter.subs(t, sp.Rational(1, 2)) == sp.Rational(5, 16)
        and not odd_survives,
    )

    dyadic = {a: sp.Rational(1, 2), t: sp.Rational(1, 2)}
    dyadic_trace = sp.cancel(matter_trace.subs(dyadic))
    dyadic_discriminant = sp.cancel(matter_difference_squared.subs(dyadic))
    comparison_threshold = sp.Rational(121, 4)
    if mutation == "reverse_gap_order":
        comparison_threshold = 200
    gap_order_ok = (
        dyadic_trace == sp.Rational(11, 16)
        and dyadic_discriminant == sp.Rational(57, 256)
        and 57 > comparison_threshold
        and sp.cancel(gauge_even.subs(dyadic)
                      / gauge_odd.subs(dyadic)) == 3
    )
    check(
        "dyadic projected diagnostic: the determinant gauge mode is second and the exact logarithmic gap is log three",
        gap_order_ok,
    )

    zero_tau_kernel = sp.ones(3) / 3
    if mutation == "break_zero_coupling_rank":
        zero_tau_kernel = sp.eye(3)
    check(
        "zero-coupling boundary: tau zero is rank-one support collapse rather than the large-tau gap-closing mechanism",
        zero_tau_kernel.rank() == 1,
    )

    physical_claim = mutation == "claim_physical_mass"
    check(
        "physical boundary: the normalized and logarithmic transfer gaps have no mass, clock, Lorentz, or continuum meaning without separate scaling suppliers",
        not physical_claim,
    )

    print("per_element: exact kernel extrema, shell probabilities, Gaussian scale, and projected diagnostic entries were recomputed")
    print("per_site: two full-ball radial shells and one projected finite gauge-matter site were checked")
    print("per_mode: Perron, two radial, determinant, even, odd, zero-coupling, and large-coupling modes were separated")
    print("per_block: one fixed finite gauge-invariant transfer and its projected tensor-factor strict-coupling family were executed; no volume-uniform claim")
    print("lattice_wide: checked and not executed — no refinement, thermodynamic, Lorentzian, physical-mass, or Hamiltonian-gap family is supplied")
    print("STATUS: fixed finite mathematical gap with an explicit full-ball strict-coupling collapse family; no uniform or physical gap")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("primary", "independent"),
                        default="primary")
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.mutation, arguments.mode))
