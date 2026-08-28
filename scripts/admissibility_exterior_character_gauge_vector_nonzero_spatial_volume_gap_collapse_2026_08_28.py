#!/usr/bin/env python3
"""Exact checks for nonzero-spatial gauge-vector volume-gap collapse."""

from __future__ import annotations

import argparse
import itertools
from pathlib import Path

import sympy as sp

from admissibility_exterior_character_gauge_vector_nonzero_spatial_volume_gap_collapse_independent_2026_08_28 import (
    independent_facts,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_GAUGE_VECTOR_NONZERO_SPATIAL_VOLUME_GAP_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_GAUGE_VECTOR_FINITE_GAP_STRICT_COUPLING_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_GAUGE_VECTOR_MATTER_SOURCE_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_exterior_character_gauge_vector_nonzero_spatial_volume_gap_collapse_independent_2026_08_28.py",
)

MUTATIONS = (
    "break_import_boundary",
    "break_shell_mass",
    "break_erosion",
    "reverse_erosion_order",
    "break_gaussian_tail",
    "erase_cross_decay",
    "break_geometry_bound",
    "break_action_bound",
    "break_frame_invariance",
    "omit_transporter",
    "hide_negative_sign",
    "promote_wide_source",
    "break_compression_bound",
    "claim_fixed_coupling_volume",
    "promote_quadratic_volume",
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


def shell_probability(inner: sp.Expr, outer: sp.Expr, m: sp.Expr) -> sp.Expr:
    radius = sp.symbols("radius", nonnegative=True)
    return sp.integrate(3 * radius**2,
                        (radius, inner / m, outer / m))


def eroded_fraction(inner: int, outer: int, m: sp.Expr) -> sp.Expr:
    full = sp.Rational(outer**3 - inner**3, 1) / m**3
    lower = sp.Rational(inner, 1) / m + 1 / m**3
    upper = sp.Rational(outer, 1) / m - 1 / m**3
    return sp.cancel((upper**3 - lower**3) / full)


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


def derived_cross_prefactor() -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
    radicand = 2 * (2**3 - 1**3) * (4**3 - 3**3)
    ceiling = sp.ceiling(sp.sqrt(radicand))
    exponential_denominator = sp.Integer(2)**3 * sp.factorial(3)
    prefactor = sp.cancel(ceiling * exponential_denominator / 3)
    return (sp.Integer(radicand), ceiling,
            exponential_denominator, prefactor)


def lower_bound(m_value: int, sites: int) -> sp.Expr:
    m = sp.Integer(m_value)
    v = eroded_fraction(1, 2, m)
    diagonal = (1 - sp.Rational(64 * sites, m_value**2))
    gaussian = 1 - sp.Rational(3, m_value**6)
    _, _, _, cross_prefactor = derived_cross_prefactor()
    eta = cross_prefactor / m**15
    return sp.cancel(diagonal * (v * gaussian) ** sites - eta**sites)


def gap_upper(m_value: int) -> sp.Expr:
    m = sp.Integer(m_value)
    action_loss = sp.Integer(64)
    erosion_loss = sp.Rational(15, 7)
    _, _, _, cross_prefactor = derived_cross_prefactor()
    return sp.cancel(
        (action_loss + erosion_loss) / m
        + 3 / m**5
        + (cross_prefactor / m**15) ** m
    )


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
    spectral_parent = (root / AUDIT_INPUT_PATHS[1]).read_text()
    action_parent = (root / AUDIT_INPUT_PATHS[2]).read_text()
    axioms = (root / AUDIT_INPUT_PATHS[3]).read_text()
    if mutation == "break_import_boundary":
        source = source.replace("N(m)=o(m^2)", "N(m)=O(m^2)")
    if mutation == "claim_fixed_coupling_volume":
        source = source.replace(
            "joint volume/temporal-coupling family",
            "fixed-coupling thermodynamic family",
        )
    import_boundary = (
        "N(m)=o(m^2)" in source
        and "tau=m^12" in source
        and "nonzero hopping" in source
        and "complete projected" in source
        and "complete nonzero spatial action" in spectral_parent
        and "T = M P C M" in action_parent
        and "source/action" in axioms
    )
    check(
        "import boundary: the parents supply the compact shared transfer and leave nonzero spatial matter-connection/volume control open",
        import_boundary,
    )

    m = sp.symbols("m", integer=True, positive=True)
    nominal_first_mass = shell_probability(sp.Integer(1), sp.Integer(2), m)
    nominal_second_mass = shell_probability(sp.Integer(3), sp.Integer(4), m)
    first_mass = nominal_first_mass
    second_mass = nominal_second_mass
    if mutation == "break_shell_mass":
        second_mass = shell_probability(sp.Integer(2), sp.Integer(4), m)
    check(
        "full-ball tubes: the two shrinking radial shell masses are exact",
        first_mass == 7 / m**3 and second_mass == 37 / m**3,
    )

    first_eroded = eroded_fraction(1, 2, m)
    second_eroded = eroded_fraction(3, 4, m)
    first_closed = 1 - (15 * m**4 - 3 * m**2 + 2) / (7 * m**6)
    first_closed_target = first_closed
    if mutation == "break_erosion":
        first_closed_target += 1 / m
    check(
        "radial erosion: the smaller retained fraction has the displayed exact polynomial",
        sp.cancel(first_eroded - first_closed_target) == 0,
    )

    erosion_difference = sp.factor(second_eroded - first_eroded)
    if mutation == "reverse_erosion_order":
        erosion_difference = -erosion_difference
    expected_difference = (
        30 * (m**2 - 1) * (m**2 - 2) / (259 * m**6)
    )
    check(
        "radial erosion ordering: the second shell is less lossy for m greater than two",
        sp.cancel(erosion_difference - expected_difference) == 0,
    )

    nominal_tau = m**12
    tau = nominal_tau
    erosion = m**-3
    gaussian_tail = sp.cancel(3 / (tau * erosion**2))
    if mutation == "break_gaussian_tail":
        tau = m**4
        gaussian_tail = sp.cancel(3 / (tau * erosion**2))
    check(
        "Gaussian retention: the supplied temporal scale and erosion give loss three over m to the sixth",
        gaussian_tail == 3 / m**6,
    )

    gaussian_scale = 3 * sp.sqrt(2 * sp.pi) / (2 * m**18)
    shell_separation = 1 / m
    cross_scale = sp.simplify(
        sp.sqrt(nominal_first_mass * nominal_second_mass) / gaussian_scale
    )
    (cross_radicand, radical_ceiling,
     exponential_denominator, cross_prefactor_bound) = derived_cross_prefactor()
    expected_cross_scale = (
        sp.sqrt(cross_radicand) * m**15 / (3 * sp.sqrt(sp.pi))
    )
    exponential_argument = sp.cancel(nominal_tau * shell_separation**2 / 2)
    cubic_exponential_lower = sp.cancel(
        exponential_argument**3 / sp.factorial(3)
    )
    if mutation == "erase_cross_decay":
        shell_separation = 1 / m**6
        exponential_argument = sp.cancel(nominal_tau * shell_separation**2 / 2)
        cubic_exponential_lower = sp.cancel(
            exponential_argument**3 / sp.factorial(3)
        )
    eta = cross_prefactor_bound / m**15
    cross_ok = (
        sp.simplify(cross_scale - expected_cross_scale) == 0
        and exponential_argument == m**10 / 2
        and cubic_exponential_lower == m**30 / 48
        and 2 * 7 * 37 == cross_radicand
        and sp.Integer(518) < radical_ceiling**2
        and exponential_denominator == 48
        and cross_prefactor_bound == 368
        and sp.limit(eta, m, sp.oo) == 0
    )
    check(
        "cross-shell leakage: exact radical and exponential bounds give eta_m=368/m^15",
        cross_ok,
    )

    a1_max = sp.Integer(7)
    a2_min = sp.Integer(1)
    a3_min = sp.Integer(1)
    nominal_d_max = a1_max / (a2_min * a3_min)
    d_max = nominal_d_max
    hopping_weight = sp.Rational(1, 7) * d_max
    if mutation == "break_geometry_bound":
        a2_min = sp.Rational(1, 2)
        d_max = a1_max / (a2_min * a3_min)
        hopping_weight = sp.Rational(1, 7) * d_max
    check(
        "coframe incidence: the supplied compact diagonal domain bounds lambda_e d_e by one",
        d_max == 7 and hopping_weight == 1,
    )

    sites = sp.symbols("N", integer=True, positive=True)
    source_min = sp.Integer(-1)
    volume_max = sp.Integer(1)
    radius_max = 4 / m
    onsite_coefficient_max = sp.cancel(
        volume_max * (3 - source_min) / 2
    )
    onsite_per_site = sp.cancel(onsite_coefficient_max * radius_max**2)
    hopping_coefficient_max = sp.cancel(
        sp.Rational(1, 7) * nominal_d_max / 2
    )
    hopping_difference_max = 2 * radius_max
    hopping_per_edge = sp.cancel(
        hopping_coefficient_max * hopping_difference_max**2
    )
    onsite_bound = onsite_per_site * sites
    hopping_bound = hopping_per_edge * (sites - 1)
    action_bound = sp.expand(onsite_bound + hopping_bound)
    if mutation == "break_action_bound":
        action_bound += 1 / m
    check(
        "nonzero spatial matter-connection action: every tube history obeys S_matter less than 64 N over m squared",
        onsite_coefficient_max == 2
        and onsite_per_site == 32 / m**2
        and hopping_coefficient_max == sp.Rational(1, 2)
        and hopping_per_edge == 32 / m**2
        and sp.simplify(64 * sites / m**2 - action_bound) == 32 / m**2,
    )

    frames = signed_frames()
    vector = sp.Matrix([sp.Rational(1, 4), sp.Rational(1, 5), sp.Rational(1, 6)])
    if mutation == "break_frame_invariance":
        frames = frames + (sp.diag(2, 1, 1),)
    frame_ok = (
        len(frames) == 48
        and sum(1 for frame in frames if frame.det() == -1) == 24
        and all(sp.expand((frame * vector).dot(frame * vector)
                          - vector.dot(vector)) == 0 for frame in frames)
    )
    check(
        "common projector: all proper and improper signed frames preserve every radial tube",
        frame_ok,
    )

    e1 = sp.Matrix([1, 0, 0])
    endpoint_left = -sp.eye(3)
    endpoint_right = sp.eye(3)
    transporter = sp.eye(3)
    transformed_transporter = endpoint_right * transporter * endpoint_left.inv()
    transformed_left = endpoint_left * e1
    transformed_right = endpoint_right * e1
    covariant_norm = sp.expand(
        (transformed_right - transformed_transporter * transformed_left).dot(
            transformed_right - transformed_transporter * transformed_left
        )
    )
    if mutation == "omit_transporter":
        covariant_norm = sp.expand(
            (transformed_right - transformed_left).dot(
                transformed_right - transformed_left
            )
        )
    check(
        "transporter covariance: the hopping norm survives independent endpoint transformations only with the link",
        covariant_norm == 0,
    )

    negative_hopping = -sp.Rational(1, 2) * sp.Integer(4)
    negative_onsite = sp.Rational(2, 7)
    negative_action = negative_hopping + negative_onsite
    if mutation == "hide_negative_sign":
        negative_action = -negative_hopping + negative_onsite
    check(
        "sign boundary: a negative hopping coefficient gives S_matter=-12/7 and destroys M less than or equal to one",
        negative_action == -sp.Rational(12, 7),
    )

    source_radius = sp.Integer(1)
    onsite_floor = sp.Rational(3 - source_radius, 2)
    if mutation == "promote_wide_source":
        source_radius = sp.Integer(4)
        onsite_floor = sp.Rational(3 - source_radius, 2)
    check(
        "source-domain boundary: r in [-1,1] keeps the onsite quadratic nonnegative",
        onsite_floor == 1,
    )

    selected_m = (128, 256, 512)
    selected_lower = tuple(lower_bound(value, value) for value in selected_m)
    if mutation == "break_compression_bound":
        selected_lower = (-selected_lower[0],) + selected_lower[1:]
    check(
        "projected compression: the connected N=m family has L_m,m greater than seven sixteenths and improves",
        all(value > sp.Rational(7, 16) for value in selected_lower)
        and all(left < right for left, right
                in zip(selected_lower, selected_lower[1:])),
    )

    selected_gap = tuple(gap_upper(value) for value in selected_m)
    volume_scoped = "joint volume/temporal-coupling family" in source
    derived_gap_coefficient = sp.Integer(64) + sp.Rational(15, 7)
    threshold = sp.Integer(128)
    action_threshold = 1 - sp.Rational(64, threshold)
    bernoulli_loss_at_threshold = (
        sp.Rational(15, 7 * threshold) + sp.Rational(3, threshold**5)
    )
    _, _, _, threshold_cross_prefactor = derived_cross_prefactor()
    eta_at_threshold = threshold_cross_prefactor / threshold**15
    all_m_threshold = (
        derived_gap_coefficient == sp.Rational(463, 7)
        and action_threshold >= sp.Rational(1, 2)
        and 1 - bernoulli_loss_at_threshold > sp.Rational(15, 16)
        and eta_at_threshold**threshold < sp.Rational(1, 32)
        and sp.Rational(1, 2) * sp.Rational(15, 16)
        - sp.Rational(1, 32) == sp.Rational(7, 16)
    )
    check(
        "volume-family scope: the exact gap upper bound decreases only on the disclosed joint family",
        volume_scoped
        and all_m_threshold
        and all(sp.Rational(0) < value < sp.Rational(1)
                for value in selected_gap)
        and all(left > right for left, right
                in zip(selected_gap, selected_gap[1:])),
    )

    quadratic_loss_exponent = sp.limit(
        m**2 * (1 - first_closed), m, sp.oo)
    if mutation == "promote_quadratic_volume":
        quadratic_loss_exponent = 0
    check(
        "subquadratic boundary: the present erosion estimate has nonzero loss at N proportional to m squared",
        quadratic_loss_exponent == sp.Rational(15, 7),
    )

    physical_boundary = (
        "no physical mass, time, Hamiltonian, continuum, Lorentz, or gravity"
        in source
    )
    if mutation == "claim_physical_mass":
        physical_boundary = "physical mass gap closes" in source
    check(
        "physical boundary: the mathematical collective-shell gap has no supplied particle or time interpretation",
        physical_boundary,
    )

    print("per_element: exact coframe weights, action signs, shell masses, erosion, Gaussian scale, and cross decay were recomputed")
    print("per_site: full B3 shells, local O(3) covariance, onsite positivity, and nonzero hopping were checked")
    print("per_mode: two projected collective radial tubes, finite strict support, and the quadratic-volume boundary were separated")
    print("per_block: the connected N=m joint volume/temporal-coupling compression was executed; no fixed-coupling thermodynamic theorem")
    print("lattice_wide: checked and not executed — no refinement embeddings, fixed-coupling infinite volume, physical time, or continuum family is supplied")
    print("STATUS: the complete projected transfer with nonzero spatial matter-connection hopping and onsite/source action has an exact joint-family mathematical gap collapse; pure-gauge plaquettes and physical/fixed-coupling limits remain open")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("primary", "independent"),
                        default="primary")
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    raise SystemExit(main(arguments.mutation, arguments.mode))
