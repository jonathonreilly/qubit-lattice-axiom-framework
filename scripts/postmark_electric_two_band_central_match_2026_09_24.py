#!/usr/bin/env python3
"""Two-band crossing normal forms and the finite-support central expansion.

All results are conditional on the supplied six-site finite-spin hop map.
The calculations concern frozen 15-cell symbols and coefficientwise operator
limits; they do not imply a global spectral gap or a fixed-time propagator
limit.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ['docs/FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/POSTMARK_ELECTRIC_CORE_AND_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/POSTMARK_ELECTRIC_MOVING_INDEX_CELL_SYMBOL_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/POSTMARK_ELECTRIC_TWO_BAND_CENTRAL_MATCH_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'scripts/core_derivation.py']
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUTPUT_DIR = ROOT / "outputs" / "postmark_moving_index_2026_09_24"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise ImportError(filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


physical_model = load("physical_model", "core_derivation.py")

POS_LEFT = (0, 1, 0, 1, 1, 1, 2, 1, 2, 2, 2, 3, 2, 3, 3)
POS_RIGHT = (0, 0, 0, 1, 0, 1, 1, 1, 2, 1, 2, 2, 2, 3, 2)
NEG_LEFT = (-1, -2, -1, -2, -2, -2, -3, -2, -3, -3, -3, -4, -3, -4, -4)
NEG_RIGHT = (-1, -1, -1, -2, -1, -2, -2, -2, -3, -2, -3, -3, -3, -4, -3)

SIDES = {
    "+": (POS_LEFT, POS_RIGHT, -3),
    "-": (NEG_LEFT, NEG_RIGHT, +3),
}


def alpha(offset: int, u):
    return u**2 - u * (2 * offset + 1)


def cell_coefficients(side: str, u):
    left, right, wrap = SIDES[side]
    offdiag = [(alpha(left[r], u) + alpha(right[r], u)) / 2
               for r in range(15)]
    previous_right = [right[(r - 1) % 15] for r in range(15)]
    previous_right[0] = right[14] + wrap
    diagonal = [alpha(left[r], u) + alpha(previous_right[r], u)
                for r in range(15)]
    return diagonal, offdiag


def band_matrix_element(diagonal, offdiag, theta, ell, ell_prime):
    q = (theta + 2 * sp.pi * ell) / 15
    q_prime = (theta + 2 * sp.pi * ell_prime) / 15
    total = sum(
        sp.exp(sp.I * (q_prime - q) * r)
        * (diagonal[r] - offdiag[r]
           * (sp.exp(sp.I * q_prime) + sp.exp(-sp.I * q)))
        for r in range(15)
    ) / 15
    return sp.simplify(sp.expand_complex(total))


def projected_crossing(side: str, theta, ell: int, ell_prime: int):
    u = sp.symbols("u", real=True)
    diagonal, offdiag = cell_coefficients(side, u)
    matrix = sp.Matrix([
        [band_matrix_element(diagonal, offdiag, theta, ell, ell),
         band_matrix_element(diagonal, offdiag, theta, ell, ell_prime)],
        [band_matrix_element(diagonal, offdiag, theta, ell_prime, ell),
         band_matrix_element(diagonal, offdiag, theta, ell_prime, ell_prime)],
    ]).applyfunc(sp.simplify)
    return u, matrix


def f(m):
    return m * (m + 1)


def global_edge_labels(n: int):
    """Exact imported hop labels on edge n -> n+1, including n=-1 -> 0."""
    if n >= 0:
        k, r = divmod(n, 15)
        left, right = POS_LEFT, POS_RIGHT
        cell_index = k
    else:
        cell_index = -(n // 15)
        r = n + 15 * cell_index
        left, right = NEG_LEFT, NEG_RIGHT
    return 3 * cell_index + left[r], 3 * cell_index + right[r]


def verify_signed_label_reflection():
    """Prove that both signed label tables define one Casimir family."""
    k = sp.symbols("k", integer=True)
    residue_rows = []
    for r in range(15):
        if NEG_LEFT[r] != -POS_LEFT[r] - 1:
            raise ArithmeticError(("left signed-label reflection", r))
        if NEG_RIGHT[r] != -POS_RIGHT[r] - 1:
            raise ArithmeticError(("right signed-label reflection", r))
        for negative, positive, name in (
            (NEG_LEFT[r], POS_LEFT[r], "left"),
            (NEG_RIGHT[r], POS_RIGHT[r], "right"),
        ):
            actual = 3*(-k) + negative
            signed_reference = 3*k + positive
            if sp.simplify(f(actual) - f(signed_reference)) != 0:
                raise ArithmeticError(("exact Casimir reflection", name, r))
        residue_rows.append({
            "residue": r,
            "L_minus_equals_minus_L_plus_minus_1": True,
            "R_minus_equals_minus_R_plus_minus_1": True,
            "factors_equal_for_symbolic_signed_cell_index": True,
        })

    checked_edges = 0
    for n in range(-1000, 1001):
        signed_k, r = divmod(n, 15)
        actual = global_edge_labels(n)
        reference = (3*signed_k + POS_LEFT[r],
                     3*signed_k + POS_RIGHT[r])
        if tuple(f(m) for m in actual) != tuple(f(m) for m in reference):
            raise ArithmeticError(("global signed-cell edge factors", n,
                                   actual, reference))
        checked_edges += 1
    if global_edge_labels(-1) != (-1, 0):
        raise ArithmeticError(("actual n=-1 edge labels", global_edge_labels(-1)))
    return {
        "residue_identities": residue_rows,
        "exact_identity": "f(-m-1)=f(m), f(m)=m(m+1)",
        "signed_cell_rule": "for n=15k+r, both edge factors use f(3k+L_r^+) and f(3k+R_r^+) for every integer k",
        "finite_edge_crosscheck_n_minus1000_to1000": checked_edges,
        "actual_labels_on_edge_minus1_to0": list(global_edge_labels(-1)),
        "scope": "exact coefficient identity throughout the path; it removes a sign-induced coefficient defect at the origin and makes no propagator claim",
    }


def central_q_at_site(n: int):
    """Diagonal and right-link coefficients of Q on the finite-support core."""
    m_left, m_right = global_edge_labels(n)
    _, m_right_previous = global_edge_labels(n - 1)
    return (-f(m_left) - f(m_right_previous),
            sp.Rational(1, 2) * (f(m_left) + f(m_right)))


def central_q_cell(side: str, k):
    """Frozen cell coefficients of Q=S^2(N_S-N_inf)+o(1), side by side."""
    left, right, wrap = SIDES[side]
    m_left = [3 * k + a for a in left]
    m_right = [3 * k + a for a in right]
    previous_right = [m_right[(r - 1) % 15] for r in range(15)]
    previous_right[0] = 3 * k + right[14] + wrap
    diagonal = [-f(m_left[r]) - f(previous_right[r]) for r in range(15)]
    positive_hopping = [sp.Rational(1, 2) * (f(m_left[r]) + f(m_right[r]))
                        for r in range(15)]
    return diagonal, positive_hopping


def direct_bloch_projection(diagonal, hopping, theta, ell: int, ell_prime: int):
    """Explicit 15x15 construction in the stated v_q[r]=exp(i*q*r) basis."""
    matrix = sp.zeros(15, 15)
    for r in range(15):
        matrix[r, r] = diagonal[r]
    for r in range(14):
        matrix[r, r + 1] = matrix[r + 1, r] = hopping[r]
    matrix[14, 0] = hopping[14] * sp.exp(sp.I*theta)
    matrix[0, 14] = hopping[14] * sp.exp(-sp.I*theta)
    q = (theta + 2*sp.pi*ell)/15
    q_prime = (theta + 2*sp.pi*ell_prime)/15
    vectors = [
        sp.Matrix([sp.exp(sp.I*q*r)/sp.sqrt(15) for r in range(15)]),
        sp.Matrix([sp.exp(sp.I*q_prime*r)/sp.sqrt(15) for r in range(15)]),
    ]
    return sp.Matrix([
        [(vectors[i].conjugate().T*matrix*vectors[j])[0] for j in range(2)]
        for i in range(2)
    ]).applyfunc(lambda x: sp.simplify(sp.expand_complex(x)))


def central_projected_matrix(side: str, theta, ell: int, ell_prime: int, k):
    diagonal, positive_hopping = central_q_cell(side, k)
    # The existing symbol helper uses H_{r,r+1}=-offdiag.  Q has the
    # positive hopping shown above, hence the sign reversal here.
    negative_offdiag = [-x for x in positive_hopping]
    return sp.Matrix([
        [band_matrix_element(diagonal, negative_offdiag, theta, ell, ell),
         band_matrix_element(diagonal, negative_offdiag, theta, ell, ell_prime)],
        [band_matrix_element(diagonal, negative_offdiag, theta, ell_prime, ell),
         band_matrix_element(diagonal, negative_offdiag, theta, ell_prime, ell_prime)],
    ]).applyfunc(sp.simplify)


def expected_central_matrices(k):
    sqrt3 = sp.sqrt(3)
    return {
        ("+", "theta=0"): sp.Matrix([
            [-27*k**2 - 33*k - sp.Rational(62, 5),
             (6*k + 4 + 6*sqrt3*sp.I*(k + 1)) / 5],
            [(6*k + 4 - 6*sqrt3*sp.I*(k + 1)) / 5,
             -27*k**2 - 33*k - sp.Rational(62, 5)],
        ]),
        ("-", "theta=0"): sp.Matrix([
            [-27*k**2 + 33*k - sp.Rational(62, 5),
             (4 - 6*k - 6*sqrt3*sp.I*(k - 1)) / 5],
            [(4 - 6*k + 6*sqrt3*sp.I*(k - 1)) / 5,
             -27*k**2 + 33*k - sp.Rational(62, 5)],
        ]),
        ("+", "theta=pi"): sp.Matrix([
            [-9*k**2 - sp.Rational(51, 5)*k - sp.Rational(58, 15),
             (18*k + 8 - sqrt3*sp.I*(6*k + 2)) / 15],
            [(18*k + 8 + sqrt3*sp.I*(6*k + 2)) / 15,
             -9*k**2 - sp.Rational(51, 5)*k - sp.Rational(58, 15)],
        ]),
        ("-", "theta=pi"): sp.Matrix([
            [-9*k**2 + sp.Rational(51, 5)*k - sp.Rational(58, 15),
             (8 - 18*k - sqrt3*sp.I*(2 - 6*k)) / 15],
            [(8 - 18*k + sqrt3*sp.I*(2 - 6*k)) / 15,
             -9*k**2 + sp.Rational(51, 5)*k - sp.Rational(58, 15)],
        ]),
    }


def verify_principal_projected_derivatives():
    theta = sp.symbols("theta", real=True)
    cases = ((sp.Integer(0), 5, 10, 1),
             (sp.pi, 12, 2, -1))
    rows = []
    for theta0, ell, ell_prime, sigma in cases:
        matrix = sp.zeros(15, 15)
        for r in range(15):
            matrix[r, r] = 2
        for r in range(14):
            matrix[r, r + 1] = matrix[r + 1, r] = -1
        matrix[0, 14] = -sp.exp(-sp.I * theta)
        matrix[14, 0] = -sp.exp(sp.I * theta)
        qs = ((theta0 + 2*sp.pi*ell)/15,
              (theta0 + 2*sp.pi*ell_prime)/15)
        vectors = [sp.Matrix([sp.exp(sp.I*q*r)/sp.sqrt(15)
                              for r in range(15)]) for q in qs]
        compressed = sp.Matrix([
            [(vectors[a].conjugate().T * matrix * vectors[b])[0]
             for b in range(2)] for a in range(2)
        ])
        derivative = compressed.diff(theta).subs(theta, theta0)
        derivative = derivative.applyfunc(lambda x: sp.simplify(sp.expand_complex(x)))
        target = sp.diag(sigma*sp.sqrt(3)/15, -sigma*sp.sqrt(3)/15)
        if any(sp.simplify(derivative[i, j]-target[i, j]) != 0
               for i in range(2) for j in range(2)):
            raise ArithmeticError((theta0, derivative, target))
        rows.append({
            "boundary": "theta=0" if theta0 == 0 else "theta=pi",
            "bands": [ell, ell_prime],
            "fixed_basis_projected_derivative_of_N0_over_w":
                [[str(derivative[i, j]) for j in range(2)] for i in range(2)],
        })
    return rows


def verify_crossing_normal_forms():
    u, delta, h = sp.symbols("u delta h", real=True)
    sqrt3 = sp.sqrt(3)
    cases = (
        ("+", "theta=0", sp.Integer(0), 5, 10,
         sqrt3 * (1-u**2) / 15,
         u * (3*u - 11), 2*u*(1+sp.I*sqrt3)/5),
        ("-", "theta=0", sp.Integer(0), 5, 10,
         sqrt3 * (1-u**2) / 15,
         u * (3*u + 11), 2*u*(-1-sp.I*sqrt3)/5),
        ("+", "theta=pi", sp.pi, 12, 2,
         -sqrt3 * (1-u**2) / 15,
         u * (5*u - 17) / 5, 2*u*(3-sp.I*sqrt3)/15),
        ("-", "theta=pi", sp.pi, 12, 2,
         -sqrt3 * (1-u**2) / 15,
         u * (5*u + 17) / 5, -2*u*(3-sp.I*sqrt3)/15),
    )
    rows = []
    for side, label, theta, ell, ell_prime, slope, scalar, coupling in cases:
        expected = sp.Matrix([[scalar, coupling], [sp.conjugate(coupling), scalar]])
        actual = projected_crossing(side, theta, ell, ell_prime)[1]
        if any(sp.simplify(actual[i, j] - expected[i, j]) != 0
               for i in range(2) for j in range(2)):
            raise ArithmeticError((side, label, actual, expected))
        diagonal, offdiag = cell_coefficients(side, u)
        direct = direct_bloch_projection(diagonal, [-x for x in offdiag],
                                         theta, ell, ell_prime)
        if any(sp.simplify(actual[i, j]-direct[i, j]) != 0
               for i in range(2) for j in range(2)):
            raise ArithmeticError((side, label, "explicit 15x15 N1 projection", actual, direct))
        nu = lambda band, th: 2*(1-u**2)*(1-sp.cos((th+2*sp.pi*band)/15))
        slope0 = sp.simplify(sp.diff(nu(ell, sp.symbols("th")), sp.symbols("th"))
                             .subs(sp.symbols("th"), theta))
        slope1 = sp.simplify(sp.diff(nu(ell_prime, sp.symbols("th")), sp.symbols("th"))
                             .subs(sp.symbols("th"), theta))
        if sp.simplify(slope0 - slope) != 0 or sp.simplify(slope1 + slope) != 0:
            raise ArithmeticError((side, label, slope0, slope1, slope))
        # 2x2 local normal form in the unperturbed crossing basis.
        normal = sp.Matrix([[slope*delta + h*scalar, h*coupling],
                            [h*sp.conjugate(coupling), -slope*delta + h*scalar]])
        rows.append({
            "side": "positive" if side == "+" else "negative",
            "boundary": label,
            "bands": [ell, ell_prime],
            "principal_eigenvalue": "3*(1-u^2)" if label == "theta=0" else "1-u^2",
            "detuning_slope_first_band": str(slope),
            "common_subprincipal_shift": str(scalar),
            "subprincipal_coupling": str(coupling),
            "first_order_normal_form_matrix": [[str(normal[i, j]) for j in range(2)]
                                                 for i in range(2)],
            "leading_gap_for_delta_theta_O_1_over_S":
                str(sp.sqrt(4*slope**2*delta**2 + 4*h**2*sp.Abs(coupling)**2)),
        })
    return {"crossings": rows,
            "independent_explicit_15x15_matrix_projections": "all four N1 projections match exactly in the stated exp(+i*q*r) Bloch basis",
            "fixed_basis_principal_derivative_check":
                verify_principal_projected_derivatives()}


def verify_central_crossing_projections():
    k = sp.symbols("k", real=True)
    cases = (("+", "theta=0", sp.Integer(0), 5, 10),
             ("-", "theta=0", sp.Integer(0), 5, 10),
             ("+", "theta=pi", sp.pi, 12, 2),
             ("-", "theta=pi", sp.pi, 12, 2))
    expected = expected_central_matrices(k)
    rows = []
    for side, label, theta, ell, ell_prime in cases:
        actual = central_projected_matrix(side, theta, ell, ell_prime, k)
        target = expected[(side, label)]
        if any(sp.simplify(actual[i, j] - target[i, j]) != 0
               for i in range(2) for j in range(2)):
            raise ArithmeticError((side, label, actual, target))
        diagonal, hopping = central_q_cell(side, k)
        direct = direct_bloch_projection(diagonal, hopping, theta, ell, ell_prime)
        if any(sp.simplify(actual[i, j]-direct[i, j]) != 0
               for i in range(2) for j in range(2)):
            raise ArithmeticError((side, label, "explicit 15x15 Q projection", actual, direct))
        off = sp.simplify(actual[0, 1])
        magnitude = sp.simplify(sp.sqrt(sp.expand_complex(off*sp.conjugate(off))))
        predicted = {
            ("+", "theta=0"): sp.Rational(2, 5)*sp.sqrt(36*k**2+66*k+31),
            ("-", "theta=0"): sp.Rational(2, 5)*sp.sqrt(36*k**2-66*k+31),
            ("+", "theta=pi"): sp.Rational(2, 15)*sp.sqrt(108*k**2+90*k+19),
            ("-", "theta=pi"): sp.Rational(2, 15)*sp.sqrt(108*k**2-90*k+19),
        }[(side, label)]
        if sp.simplify(magnitude**2 - predicted**2) != 0:
            raise ArithmeticError((side, label, magnitude, predicted))
        outer_linear = {
            "theta=0": sp.Rational(12, 5)*k,
            "theta=pi": 4*sp.sqrt(3)*k/5,
        }[label]
        constant = {
            ("+", "theta=0"): sp.Rational(11, 5),
            ("-", "theta=0"): -sp.Rational(11, 5),
            ("+", "theta=pi"): sp.sqrt(3)/3,
            ("-", "theta=pi"): -sp.sqrt(3)/3,
        }[(side, label)]
        if sp.simplify(sp.limit(magnitude-outer_linear, k, sp.oo)-constant) != 0:
            raise ArithmeticError((side, label, "central/outer matching", magnitude))
        rows.append({
            "side": "positive" if side == "+" else "negative",
            "boundary": label,
            "bands": [ell, ell_prime],
            "projected_Q_matrix": [[str(actual[i, j]) for j in range(2)]
                                   for i in range(2)],
            "Q_coupling_magnitude": str(predicted),
            "central_frozen_cell_gap_coefficient": str(2*predicted),
            "outer_linear_Q_coupling_as_k_large": str(outer_linear),
            "constant_inner_correction_after_outer_linear_term": str(constant),
            "physical_cell_index_domain": "k>=1" if side == "+" else "K>=1",
            "scope": "coefficient projection of a side-frozen cell; not the spectrum of the full central interface operator",
        })
    return {"crossings": rows,
            "independent_explicit_15x15_matrix_projections": "all four central Q projections match exactly in the stated exp(+i*q*r) Bloch basis"}


def verify_scalar_central_match():
    h, k, a = sp.symbols("h k a", real=True)
    u = 3*k*h
    exact = 1 - h**2*(3*k+a)*(3*k+a+1)/(1+h)
    alpha = u**2-u*(2*a+1)
    outer_to_second_order = 1-u**2+h*alpha-h**2*(u-a)*(u-a-1)
    difference = sp.series(exact-outer_to_second_order, h, 0, 3).removeO()
    if sp.simplify(difference) != 0:
        raise ArithmeticError(("exact-to-outer central scalar match", difference))
    return {
        "exact_finite_spin_factor": "1 - h^2*(3k+a)*(3k+a+1)/(1+h), h=1/S",
        "outer_expansion_through_h2": "(1-u^2)+h*(u^2-u*(2a+1))-h^2*(u-a)*(u-a-1)",
        "central_substitution": "u=3kh with fixed k",
        "difference_through_h2": str(difference),
        "conclusion": "the finite-offset h^2 term contributes at order one to C*(N_S-N_inf) when u=3k/S and k is fixed",
    }


def verify_core_coefficient_limit():
    rows = []
    max_errors = {}
    nodes = physical_model.walk_nodes(61)
    for spin in (64, 128, 256, 512):
        max_diag = 0.0
        max_off = 0.0
        for n in range(-60, 61):
            state = nodes[n]
            h2_row = physical_model.finite_spin_h2(state, spin)
            # The independent physical-state routine returns H_2; M_S=-H_2.
            m_diag = -h2_row.get(state, 0.0)
            m_off = -h2_row.get(nodes[n + 1], 0.0)
            q_diag, q_hop = central_q_at_site(n)
            max_diag = max(max_diag, abs(spin**2*(m_diag-2)-float(q_diag)))
            # Staggering changes M_S's positive path link into N_S's negative link.
            max_off = max(max_off, abs(spin**2*(1-m_off)-float(q_hop)))
        if max_diag > 400 / spin or max_off > 200 / spin:
            raise ArithmeticError((spin, "independent physical-state core comparison",
                                   max_diag, max_off))
        max_errors[str(spin)] = {"diagonal": max_diag, "offdiagonal": max_off}
        rows.append({"S": spin, "max_abs_error_on_n_-60_to_60": max_errors[str(spin)]})
    return {
        "spins": rows,
        "source": "independent enumeration of physical charge/electric states and all ordered two-hop paths in scripts/core_derivation.py, compared with the signed-label formula in this runner",
        "coefficientwise_theorem": "For every f in c00(Z), S^2*(N_S-N_inf)f -> Qf in l2, where Q is the tridiagonal operator with diagonal d_n and offdiagonal c_n defined in the accompanying note.",
        "uniform_growing_window_bound": "For edge labels in cells |k|<=K_S=o(sqrt(S)), the diagonal coefficient error is O((K_S+1)^2/S) and the offdiagonal error is O((K_S+1)^2/S+(K_S+1)^4/S^2), uniformly. This follows by writing A=f(m_L), B=f(m_R)=O((K_S+1)^2), using S^2/C=S/(S+1), and Taylor expanding sqrt((1-A/C)(1-B/C)) for A/C,B/C=o(1).",
        "generator_core_identity": "(G_S+C*N_inf)f = N_S^2*f - C*(N_S-N_inf)f -> (N_inf^2-Q)f for each f in c00(Z).",
        "role": "finite-spin corroboration of the exact coefficientwise formula; not a uniform operator-norm estimate",
    }


def verify_actual_interface():
    values = {str(n): [str(central_q_at_site(n)[0]), str(central_q_at_site(n)[1])]
              for n in range(-3, 4)}
    plus_diag, _ = central_q_cell("+", sp.Integer(0))
    actual_zero_diag, _ = central_q_at_site(0)
    plus_previous_edge = central_q_cell("+", sp.Integer(-1))[1][14]
    actual_crossing_edge = central_q_at_site(-1)[1]
    if (sp.simplify(plus_diag[0]-actual_zero_diag) != 0
            or sp.simplify(plus_previous_edge-actual_crossing_edge) != 0):
        raise ArithmeticError("the Casimir-reflected labels fail to match across the central seam")
    if sp.simplify(f(-1)-f(0)) != 0:
        raise ArithmeticError("R_m=C-m(m+1) is not invariant under m -> -m-1 at the seam")
    return {
        "actual_core_coefficients_n_minus3_to3": values,
        "actual_negative_edge_labels_at_n_minus1": list(global_edge_labels(-1)),
        "positive_extrapolated_edge_labels_at_n_minus1": [
            str(3*(-1)+POS_LEFT[14]),
            str(3*(-1)+POS_RIGHT[14]),
        ],
        "casimir_identity": "m(m+1)=(-m-1)(-m)",
        "central_diagonal_match_at_n0": str(sp.simplify(plus_diag[0]-actual_zero_diag)),
        "central_link_match_at_n_minus1": str(sp.simplify(plus_previous_edge-actual_crossing_edge)),
        "scope": "the Casimir factors match across n=-1/0 despite different signed labels; this local check supplies no fixed-time propagation estimate",
    }


def main():
    result = {
        "claim_status": "conditional local two-band normal form and finite-support central coefficient theorem; no global propagator asymptotic",
        "upstream_model_source_note": "docs/FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md",
        "historical_upstream_model_source_sha256": "d235b264783de82bd563d17c217c0b3bc22718638223106215ae43edfd7dbb23",
        "historical_upstream_model_source_revision": "c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6",
        "historical_source_pr_status": "PR #8831 is CLOSED without merge; its conditional source is present in the cited canonical main note",
        "historical_main_revision_searched": "c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6",
        "read_inventory": {
            "scientific_inputs": [
                "the supplied six-site path and signed hop labels in the cited source notes",
                "the physical charge/electric state and legal-hop enumeration in scripts/core_derivation.py",
                "the exact signed 15-residue cell construction stated in the cited notes",
            ],
            "package_integrity_reads": [
                "scripts/runner_cache.py binds this runner SHA-256 and the declared input fingerprints; no external data files are read at execution time",
            ],
        },
        "operator": "N_S=J M_S J, N_inf=2I-shift-shift*, G_S=N_S^2-C N_S, C=S(S+1)",
        "outer_two_band_crossings": verify_crossing_normal_forms(),
        "one_global_signed_label_family": verify_signed_label_reflection(),
        "central_projected_cell_coefficients": verify_central_crossing_projections(),
        "scalar_outer_to_inner_match": verify_scalar_central_match(),
        "coefficientwise_core_limit_check": verify_core_coefficient_limit(),
        "actual_center_interface": verify_actual_interface(),
        "scope_limit": "The 2x2 matrices are projections of frozen-cell symbols; the fixed-support Q limit is an unbounded polynomial Jacobi operator on c00. Neither gives a global finite-spin gap, scattering matrix, statewise tail bound, or fixed-time readout limit.",
    }
    target = OUTPUT_DIR / "TWO_BAND_MATCH_RESULTS.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    print("TOTAL: PASS=6 FAIL=0 (executed identity/finite-control families; no asymptotic certification)")


if __name__ == "__main__":
    main()
