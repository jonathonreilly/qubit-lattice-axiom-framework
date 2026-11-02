#!/usr/bin/env python3
"""Different-path author controls for the fixed-reference return continuation.

Exact symbolic finite algebra and one high-precision quadrature comparison.
This is not a computation of the full Yang--Mills Hessian or a continuum proof.
No files are written by the script; stdout is the complete JSON result.
"""
from datetime import datetime, timezone
from itertools import product
from math import comb
import json
import platform
import sys
import time
import traceback

import mpmath as mp
import sympy as sp

started = time.monotonic()
checks = {}
results = {}
errors = {}


def check(name, condition):
    checks[name] = bool(condition)


def zero(expr):
    return sp.cancel(sp.expand(expr)) == 0


def trunc(expr, variables, degree):
    return sp.Add(*[
        coefficient * sp.prod(v ** n for v, n in zip(variables, monomial))
        for monomial, coefficient in sp.Poly(sp.expand(expr), *variables).terms()
        if sum(monomial) <= degree
    ])


def su2_plaquette():
    B, d, sigma, c, p, w = sp.symbols("B d sigma c p w")
    tx = sp.I * sp.Matrix([[0, 1], [1, 0]]) / sp.sqrt(2)
    ty = sp.I * sp.Matrix([[0, -sp.I], [sp.I, 0]]) / sp.sqrt(2)
    degree = 8

    def expt(T, z):
        out = sp.zeros(2)
        for n in range(degree + 1):
            out += z ** n * T ** n / sp.factorial(n)
        return out

    # Actual plaquette with fourth link I; inverse is computed in reverse order.
    P = expt(tx, B) * expt(ty, B) * expt(tx, -d)
    Pinv = expt(tx, d) * expt(ty, -B) * expt(tx, -B)
    action = trunc(sp.trace(2 * sp.eye(2) - P - Pinv) / 2, (B, d), degree)
    increment = sp.expand(action - action.subs(d, 0))
    # Independent quaternion/trigonometric expression for the scalar part.
    closed = 2 * sp.cos(B / sp.sqrt(2)) ** 2 * (1 - sp.cos(d / sp.sqrt(2)))
    closed -= 2 * sp.sin(B / sp.sqrt(2)) * sp.cos(B / sp.sqrt(2)) * sp.sin(d / sp.sqrt(2))
    closed_series = closed.series(B, 0, degree + 1).removeO()
    closed_series = closed_series.series(d, 0, degree + 1).removeO()
    closed_series = trunc(closed_series, (B, d), degree)
    check("su2_generators_hilbert_schmidt_normalized", -sp.trace(tx ** 2) == 1 and -sp.trace(ty ** 2) == 1)
    check("su2_background_generators_noncommute", tx * ty - ty * tx != sp.zeros(2))
    check("su2_matrix_inverse_and_quaternion_series_agree_order8", zero(increment - closed_series))
    check("su2_source_mixed_linear_coefficient_is_minus_one", increment.coeff(B, 1).coeff(d, 1) == -1)
    check("su2_source_quadratic_coefficient_is_one_half", increment.coeff(B, 0).coeff(d, 2) == sp.Rational(1, 2))
    check("su2_source_force_vanishes_at_zero_background", sp.diff(action, d).subs({B: 0, d: 0}) == 0)
    limit_coefficient = sp.expand(increment.subs({B: c * sigma * p, d: sigma * w})).coeff(sigma, 2)
    expected = -c * p * w + w ** 2 / 2
    check("su2_source_scaled_leading_term_contains_background_force", zero(limit_coefficient - expected))
    check("control_dropping_nontrivial_background_linear_term_fails", not zero(limit_coefficient - w ** 2 / 2))
    check("control_reversing_source_link_orientation_fails", not zero(increment - increment.subs(d, -d)))
    # Removing the second, noncommuting background link changes degree four.
    one_axis = 2 * sp.cos(B / sp.sqrt(2)) * (1 - sp.cos(d / sp.sqrt(2)))
    one_axis -= 2 * sp.sin(B / sp.sqrt(2)) * sp.sin(d / sp.sqrt(2))
    one_axis = one_axis.series(B, 0, 5).removeO().series(d, 0, 5).removeO().expand()
    check("control_removing_noncommuting_background_link_fails", increment.coeff(B, 2).coeff(d, 2) != one_axis.coeff(B, 2).coeff(d, 2))
    results["su2"] = {
        "degree": degree,
        "increment_through_degree4": str(trunc(increment, (B, d), 4)),
        "scaled_leading_source_polynomial": str(limit_coefficient),
        "scope": "Actual SU(2) plaquette function; prescribed small link background, not the solved full lattice branch.",
    }


def compositions(total, width):
    if width == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, width - 1):
            yield (first,) + rest


def marked_coefficients():
    comparisons = 0
    strict_b = False
    strict_d = False
    good = True
    for q in range(1, 5):
        for n in range(0, 8):
            independent = [0] * (n + 1)
            for powers in compositions(n, q):
                for r in product(*(range(k + 1) for k in powers)):
                    coefficient = sp.prod(comb(k, j) for k, j in zip(powers, r))
                    independent[sum(r)] += int(coefficient)
            for ell, coefficient in enumerate(independent):
                target = comb(n + q - 1, q - 1) * comb(n, ell)
                good = good and coefficient == target
                comparisons += 1
                if n >= 2 and 0 < ell < n:
                    marked = coefficient * (1 + (n - ell) + ell)
                    strict_b |= marked > coefficient * (1 + ell)
                    strict_d |= marked > coefficient * (1 + n - ell)
    check("all_order_majorant_finite_multiindex_coefficients", good)
    check("control_omitting_background_incidence_mark_fails", strict_b)
    check("control_omitting_fluctuation_incidence_mark_fails", strict_d)

    b, x = sp.symbols("b x", nonnegative=True)
    a, H, q = sp.Rational(1, 2), sp.Integer(1), 3
    f = lambda t: H * (1 - t / a) ** (-q)
    t = sp.symbols("t")
    ft = f(t)
    T3 = f(b + x) - f(b) - x * sp.diff(ft, t).subs(t, b) - x ** 2 * sp.diff(ft, t, 2).subs(t, b) / 2
    point = {b: sp.Rational(1, 20), x: sp.Rational(1, 30)}
    rising3, rising4 = q * (q + 1) * (q + 2), q * (q + 1) * (q + 2) * (q + 3)
    bounds = [
        H * rising3 * 2 ** (q + 3) * x ** 3 / (6 * a ** 3),
        H * rising4 * 2 ** (q + 3) * x ** 3 / (6 * a ** 3),
        H * rising3 * 2 ** (q + 3) * x ** 2 / (2 * a ** 3),
    ]
    actual = [T3, b * sp.diff(T3, b), sp.diff(T3, x)]
    check("explicit_cubic_majorant_bounds_at_rational_control", all((B - A).subs(point) >= 0 for A, B in zip(actual, bounds)))
    fw = lambda t: (1 - t / a) ** (-4) - 1 - 4 * t / a
    Tw = fw(b + x) - fw(b)
    Q = 4 * 5 * 2 ** 6 / a ** 2
    actual_w = [Tw, sp.diff(Tw, b), sp.diff(Tw, x)]
    bounds_w = [Q * (b * x + x ** 2 / 2), Q * x, Q * (b + x)]
    check("explicit_wilson_increment_majorant_at_rational_control", all((B - A).subs(point) >= 0 for A, B in zip(actual_w, bounds_w)))
    results["coefficient_counting"] = {"independent_coefficient_comparisons": comparisons, "q_values": [1, 2, 3, 4], "maximum_total_degree": 7}


def exact_product_insertions():
    j01, j12, j23, h3, j45, h4, h5 = sp.symbols("j01 j12 j23 h3 j45 h4 h5")
    total = pin = pin_insert = pin03 = 0
    for w in product((-1, 1), repeat=6):
        density = (1 + j01 * w[0] * w[1]) * (1 + j12 * w[1] * w[2]) * (1 + j23 * w[2] * w[3]) * (1 + h3 * w[3])
        density *= (1 + j45 * w[4] * w[5]) * (1 + h4 * w[4]) * (1 + h5 * w[5])
        total += density / 64
        if w[0] == 1:
            pin += density / 32
            pin_insert += w[1] * density / 32
        if w[0] == w[3] == 1:
            pin03 += density / 16
    total, pin, pin_insert, pin03 = [sp.expand(v) for v in (total, pin, pin_insert, pin03)]
    # Independent parity/path argument: an unpinned endpoint must have even degree.
    bulk = 1 + j45 * h4 * h5
    path = j01 * j12 * j23
    check("spin_direct_partition_matches_even_degree_formula", zero(total - bulk))
    check("spin_direct_pin_matches_connected_path_formula", zero(pin - (1 + h3 * path) * bulk))
    ratio = sp.cancel(pin / total)
    check("normalized_pin_cancels_disconnected_bulk_exactly", zero(ratio - (1 + h3 * path)))
    check("normalized_pin_has_zero_bulk_source_derivative", sp.diff(ratio, j45) == 0)
    check("control_unnormalized_pin_retains_bulk_factor", not zero(sp.diff(pin, j45)))
    insertion = sp.cancel(pin_insert / total)
    check("anchored_face_insertion_matches_parity_formula", zero(insertion - (j01 + h3 * j12 * j23)))
    check("control_root_only_insertion_misses_remote_attachment", not zero(insertion - j01))
    check("remote_pin_response_requires_complete_connector", ratio.diff(h3, j01, j12, j23) == 1)
    check("control_deleting_connector_kills_remote_response", ratio.subs(j12, 0).diff(h3, j01, j23) == 0)
    conditional = sp.cancel(pin03 / total)
    check("product_event_probability_is_retained", zero(conditional / 4 - (1 + h3) * (1 + path) / 4))
    check("control_dropping_product_event_probability_fails", not zero(conditional - conditional / 4))
    results["product_measure"] = {
        "states_enumerated": 64,
        "partition": str(total),
        "normalized_pin": str(ratio),
        "normalized_face_insertion": str(insertion),
        "product_event_ratio": str(conditional / 4),
    }

    # A positive correlated history can vanish on a tiny complex-source disk.
    # Only two configurations survive the indicator; no 2**512 enumeration.
    m = 512
    z = sp.pi / (2 * m)
    baseline = sp.cos(z) ** m
    retained_history = sp.Integer(2) ** (1 - m) * sp.cos(m * z)
    norm_h = sp.exp(4) * z
    check("correlated_history_control_has_small_CXR_input", float(norm_h.evalf(30)) < 0.25)
    check("correlated_history_baseline_partition_nonzero", baseline.is_positive is True)
    check("correlated_positive_history_numerator_vanishes_exactly", retained_history == 0)
    check("control_replacing_correlated_history_by_one_fails", retained_history != baseline)
    results["history_limitation"] = {
        "sites": m,
        "source": str(z),
        "weighted_interaction_norm_beta4": str(norm_h.evalf(30)),
        "baseline": "cos(pi/1024)^512 > 0",
        "history": "all +1 or all -1; numerator = 2^(-511) cos(pi/2) = 0",
        "scope": "Countercontrol to an arbitrary-history inference, not a no-go for Yang--Mills histories.",
    }


def exact_complex_two_dimensional_flux():
    s, w0, w1 = sp.symbols("s w0 w1")
    sigma, p = sp.Rational(1, 3), sp.Rational(2, 3)
    C0 = sp.Matrix([[2, sp.Rational(1, 5)], [sp.Rational(1, 5), 1]])
    E = sp.Matrix([[sp.I / 10, sp.Rational(1, 20)], [sp.Rational(1, 20), -sp.I / 30]])
    b0 = sp.Matrix([sp.Rational(1, 7), -sp.Rational(1, 9)])
    d = sp.Matrix([sp.Rational(1, 13) + sp.I / 17, -sp.Rational(1, 11)])
    W = sp.Matrix([w0, w1])
    C = C0 + s * E
    a = b0 + s * d + sigma * C * W
    J = sigma ** 2 * C.det()
    density = sp.expand(1 + a[0] + a[1] ** 2 + sp.I * a[0] * a[1] + a[0] ** 2 * a[1])
    pullback = sp.expand(J * density)

    def box_integral(expr):
        return sp.integrate(sp.integrate(expr, (w0, -p, p)), (w1, -p, p))

    direct = sp.expand(box_integral(pullback))
    # In two dimensions J*v = sigma adj(C)(d+sigma E W), which includes every minor.
    Jv = sigma * C.adjugate() * (d + sigma * E * W)
    fluxes = []
    for i, wi in enumerate((w0, w1)):
        other = w1 if i == 0 else w0
        flux_density = sp.expand(density * Jv[i])
        upper = sp.integrate(flux_density.subs(wi, p), (other, -p, p))
        lower = sp.integrate(flux_density.subs(wi, -p), (other, -p, p))
        fluxes.append((sp.expand(upper), sp.expand(lower)))
    oriented = sp.expand(sum(upper + lower for upper, lower in fluxes))
    check("complex_2d_affine_flux_equals_direct_derivative_exactly", zero(sp.diff(direct, s) - oriented))
    wrong_orientation = fluxes[0][0] - fluxes[0][1] + fluxes[1][0] + fluxes[1][1]
    check("control_reversing_one_face_orientation_fails", not zero(sp.diff(direct, s) - wrong_orientation))
    omitted_jacobian = box_integral(sp.expand(J * sp.diff(density, s)))
    check("control_omitting_jacobian_derivative_fails", not zero(sp.diff(direct, s) - omitted_jacobian))
    check("complex_2d_covariance_and_perturbation_noncommute", C0 * E - E * C0 != sp.zeros(2))
    point = sp.Rational(2, 5)
    results["complex_flux"] = {
        "dimension": 2,
        "all_oriented_faces": 4,
        "exact_derivative_at_s_2_over_5": str(sp.expand(sp.diff(direct, s).subs(s, point))),
        "jacobian_omission_error_at_same_s": str(sp.expand((sp.diff(direct, s) - omitted_jacobian).subs(s, point))),
        "scope": "Exact polynomial top-form identity; Gaussian smallness is tested separately.",
    }


def high_precision_gaussian():
    mp.mp.dps = 80
    sigma, p = mp.mpf(1) / 7, mp.mpf(3)
    B = 2 * sigma * p / 5
    eps = mp.mpc(1, 2) / 1000000
    A = 1 + eps
    b1, C1 = B / A, 1 / mp.sqrt(A)
    d, E = b1 - B, C1 - 1
    F = lambda a: (a - B) ** 2 / 2 + eps * a ** 2 / 2
    density = lambda a: mp.exp(-F(a) / sigma ** 2)
    direct = mp.quad(density, [B - sigma * p, B, B + sigma * p])
    ref_U = lambda w: eps * (B * w / sigma + w ** 2 / 2)
    fixed_reference = sigma * mp.exp(-eps * B ** 2 / (2 * sigma ** 2)) * mp.quad(lambda w: mp.exp(-w ** 2 / 2 - ref_U(w)), [-p, 0, p])
    vacuum = eps * B ** 2 / (2 * sigma ** 2 * A)
    primitive = lambda a: sigma * mp.sqrt(mp.pi / (2 * A)) * mp.exp(-vacuum) * mp.erf(mp.sqrt(A) * (a - b1) / (mp.sqrt(2) * sigma))
    bs = lambda s: B + s * d
    Cs = lambda s: 1 + s * E
    affine = lambda s, w: bs(s) + sigma * Cs(s) * w
    integral = lambda s: primitive(affine(s, p)) - primitive(affine(s, -p))
    velocity = lambda s, w: (d / sigma + E * w) / Cs(s)
    flux = lambda s: sigma * Cs(s) * (density(affine(s, p)) * velocity(s, p) - density(affine(s, -p)) * velocity(s, -p))
    rel = lambda x, y: abs(x - y) / max(mp.mpf(1), abs(x), abs(y))
    tolerance = mp.mpf("1e-65")
    check("gaussian_direct_original_quadrature_equals_fixed_reference", rel(direct, fixed_reference) < tolerance)
    check("gaussian_completed_square_erf_equals_original_quadrature", rel(integral(0), direct) < tolerance)
    wrong_linear = sigma * mp.exp(-eps * B ** 2 / (2 * sigma ** 2)) * mp.quad(lambda w: mp.exp(-A * w ** 2 / 2), [-p, 0, p])
    check("control_gaussian_source_linear_omission_fails", abs(wrong_linear - direct) > mp.mpf("1e-18"))
    check("control_gaussian_main_action_omission_fails", abs(direct * mp.exp(vacuum) - direct) > mp.mpf("1e-18"))
    check("control_gaussian_determinant_omission_fails", abs(direct * mp.sqrt(A) - direct) > mp.mpf("1e-18"))
    derivative_errors = []
    for s in (mp.mpf(0), mp.mpf(2) / 7, mp.mpf(1)):
        derivative_errors.append(rel(mp.diff(integral, s), flux(s)))
    check("gaussian_contour_derivative_matches_normalized_face_path", max(derivative_errors) < tolerance)
    log_ratio = mp.log(integral(1) / integral(0))
    integrated_flux = mp.quad(lambda s: flux(s) / integral(s), [0, mp.mpf(1) / 2, 1])
    check("gaussian_log_ratio_equals_integrated_normalized_flux", rel(log_ratio, integrated_flux) < tolerance)
    z_p = mp.erf(p / mp.sqrt(2))
    phi = mp.exp(-p ** 2 / 2) / mp.sqrt(2 * mp.pi)
    Cmax = max(mp.mpf(1), abs(C1))
    # Analytic triangle bounds valid for every real s in [0,1], not a mesh maximum.
    h_bound = mp.exp(4) * (abs(A) * abs(d) * Cmax * p / sigma + abs(A) * abs(E) * (Cmax + abs(C1)) * p ** 2 / 2)
    V_bound = (abs(d) / sigma + abs(E) * p) / (1 - abs(E))
    face_bound = 2 * phi / z_p * mp.exp(4 * h_bound) * V_bound
    check("gaussian_homotopy_uniform_triangle_cluster_bound_small", h_bound < mp.mpf(1) / 4)
    check("gaussian_normalized_log_ratio_obeys_face_bound", abs(log_ratio) <= face_bound)
    # This comparison is at the same B. A B=0 reference would already move at eps=0.
    check("control_zero_background_reference_is_different_at_zero_source", B / sigma != 0)
    results["gaussian"] = {
        "precision_decimal_digits": mp.mp.dps,
        "tolerance": str(tolerance),
        "source": str(eps),
        "same_B_reference": str(B),
        "direct_raw_integral": str(direct),
        "fixed_reference_error": str(rel(direct, fixed_reference)),
        "completed_square_error": str(rel(integral(0), direct)),
        "source_linear_omission_error": str(abs(wrong_linear - direct)),
        "log_ratio": str(log_ratio),
        "normalized_flux_error": str(rel(log_ratio, integrated_flux)),
        "uniform_weighted_h_upper_bound_beta4": str(h_bound),
        "normalized_face_upper_bound": str(face_bound),
        "scope": "One-dimensional Gaussian with nonzero background and complex source; diagnostic of the actual normalization/flux algebra, not a Yang--Mills integration.",
    }


for label, function in [
    ("su2", su2_plaquette),
    ("coefficients", marked_coefficients),
    ("insertions", exact_product_insertions),
    ("flux", exact_complex_two_dimensional_flux),
    ("gaussian", high_precision_gaussian),
]:
    try:
        function()
    except Exception as exc:
        errors[label] = {"type": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc()}
        check(label + "_execution_completed", False)

payload = {
    "recorded_utc": datetime.now(timezone.utc).isoformat(),
    "elapsed_seconds": time.monotonic() - started,
    "python": platform.python_version(),
    "sympy": sp.__version__,
    "mpmath": mp.__version__,
    "checks": checks,
    "check_count": len(checks),
    "all_checks_pass": all(checks.values()) and not errors,
    "results": results,
    "execution_errors": errors,
    "scope": "Author controls only; finite exact algebra and explicitly non-rigorous numerical quadrature. Uniform/all-order claims require the source derivations and fresh review.",
}
print(json.dumps(payload, indent=2, sort_keys=True))
sys.exit(0 if payload["all_checks_pass"] else 1)
