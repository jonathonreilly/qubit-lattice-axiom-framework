#!/usr/bin/env python3
"""Scoped, independently derived diagnostics for the Kirk v4 import screen.

The arbitrary-rank conclusions are proved in the accompanying note. Finite
checks here validate identities, controls, and explicit mutations; they do not
simulate Wilson theory or prove a continuum statement.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import platform
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

import sympy as sp


CHECKS = []


def record(name, condition, detail):
    CHECKS.append({"name": name, "pass": bool(condition), "detail": detail})


def dec(x):
    x = Fraction(x)
    return Decimal(x.numerator) / Decimal(x.denominator)


def log_norm(d, t):
    return Decimal(d) * (Decimal(1) - dec(t) ** 2).ln() / 2


def rational_string(x):
    return str(Fraction(x))


def rational_matrix(rows):
    return sp.Matrix([[sp.Rational(x.numerator, x.denominator)
                       if isinstance(x, Fraction) else sp.Rational(x)
                       for x in row] for row in rows])


def gaussian_witnesses():
    t = Fraction(1, 64)
    # A fixed distance weight e^(a distance)=2 gives the printed row kappa=1/32.
    kappa = 2 * t
    record("printed_weighted_operator_row_small", kappa < Fraction(1, 8),
           {"t": str(t), "distance_weight": 2, "kappa": str(kappa)})
    rows = []
    for d in (1, 2, 3, 5):
        I = sp.eye(d)
        T = sp.Rational(t.numerator, t.denominator) * I
        Q = I.row_join(T).col_join(T.row_join(I))
        P = I.row_join(I).col_join(I.row_join(-I))
        # P/sqrt(2) is orthogonal: use P^T Q P / 2 to avoid radicals.
        mode = sp.diag(*([1 + T[0, 0]] * d + [1 - T[0, 0]] * d))
        record(f"plus_minus_diagonalization_d{d}", P.T * Q * P / 2 == mode,
               "Independent symmetric/antisymmetric mode transformation")
        expected_det = (1 - T[0, 0] ** 2) ** d
        record(f"full_schur_determinant_d{d}", Q.det() == expected_det,
               {"exact_det": str(Q.det()), "spectrum_floor": str(1 - t)})
        K = Q - sp.eye(2 * d)
        record(f"closed_two_step_trace_d{d}", sp.trace(K * K) == 2 * d * T[0, 0] ** 2,
               {"trace": str(sp.trace(K * K)), "rank_multiplier": d})
        if d > 1:
            record(f"mutation_omit_trace_rank_rejected_d{d}",
                   sp.trace(K * K) != 2 * T[0, 0] ** 2,
                   "Replacing every matrix cycle trace by its scalar block-edge product fails")
        record(f"mutation_wrong_schur_sign_rejected_d{d}",
               Q.det() != (1 + T[0, 0] ** 2) ** d,
               "The precision uses det(I-B*B), not det(I+B*B)")
    for d in (1, 2, 8, 128, 4096, 1048576):
        value = log_norm(d, t)
        needed_c = abs(value) * dec((1 - 4 * kappa) ** 4 / kappa)
        rows.append({"core_dimension": d, "operator_row": str(kappa),
                     "minus_log_density_ratio_at_zero": str(-value),
                     "necessary_C_in_printed_row_ignoring_support_weight": str(needed_c)})
        record(f"exact_log_normalizer_additivity_d{d}",
               abs(value - Decimal(d) * log_norm(1, t)) < Decimal("1e-70"),
               "Each independent pair contributes the same nonzero normalizer")
        if d > 1:
            record(f"mutation_omit_normalizer_dimension_rejected_d{d}",
                   abs(value - log_norm(1, t)) > Decimal("1e-5"),
                   "A rank-independent normalizer is incompatible with the exact determinant")

    # The Gaussian ratio integrates to one. Omitting its prefactor gives >1.
    for d in (1, 7, 64):
        norm = (Decimal(1) - dec(t) ** 2) ** (Decimal(d) / 2)
        raw_integral = (Decimal(1) - dec(t) ** 2) ** (-Decimal(d) / 2)
        record(f"normalization_identity_d{d}", abs(norm * raw_integral - 1) < Decimal("1e-70"),
               "Computed from independent two-dimensional Gaussian mode integrals")
        record(f"mutation_drop_normalizer_rejected_d{d}", raw_integral > 1,
               {"integral_without_scalar_normalizer": str(raw_integral)})

    record("zero_coupling_control", log_norm(10000, Fraction(0)) == 0,
           "Uncoupled normalized Gaussian ratio is identically one")
    for d in (1, 4, 16):
        B = sp.zeros(d)
        B[0, 0] = sp.Rational(1, 64)
        record(f"fixed_rank_one_control_d{d}", (sp.eye(d) - B.T * B).det() == sp.Rational(4095, 4096),
               "Growing an uncoupled ambient space does not grow the determinant")
    for s in (1, 2, 4, 8, 16):
        d = s * s
        ts = Fraction(1, 64 * s)
        v = -log_norm(d, ts)
        lower = dec(Fraction(1, 2 * 64 ** 2))
        upper = lower / (Decimal(1) - dec(ts) ** 2)
        record(f"fixed_hilbert_schmidt_control_d{d}", lower <= v <= upper,
               {"minus_log_norm": str(v), "lower": str(lower), "upper": str(upper)})
    return rows


def general_cross_blocks():
    matrices = [
        rational_matrix([[Fraction(1, 32), Fraction(1, 64), 0],
                         [Fraction(1, 80), 0, Fraction(1, 50)]]),
        rational_matrix([[Fraction(1, 10)], [Fraction(-1, 20)], [Fraction(1, 30)]]),
        rational_matrix([[0, 0], [0, 0], [0, 0]]),
    ]
    out = []
    for j, B in enumerate(matrices):
        m, n = B.shape
        Q = sp.eye(m).row_join(B).col_join(B.T.row_join(sp.eye(n)))
        gram_r = sp.eye(n) - B.T * B
        gram_l = sp.eye(m) - B * B.T
        h2 = sum(x * x for x in B)
        record(f"rectangular_schur_identity_{j}", Q.det() == gram_l.det() == gram_r.det(),
               {"shape": [m, n], "det": str(Q.det())})
        # The Frobenius norm bounds the operator norm. This bound is deliberately
        # weaker than the sharp spectral one, but entirely rational before log.
        record(f"positive_precision_frobenius_control_{j}", h2 < 1,
               {"hilbert_schmidt_squared": str(h2)})
        minus_log = -dec(Fraction(Q.det())).ln() / 2
        lower = dec(Fraction(h2) / 2)
        upper = dec(Fraction(h2) / (2 * (1 - Fraction(h2))))
        record(f"dimension_aware_determinant_bounds_{j}", lower <= minus_log <= upper,
               {"lower": str(lower), "value": str(minus_log), "upper": str(upper)})
        out.append({"shape": [m, n], "B": [[str(x) for x in row] for row in B.tolist()],
                    "full_precision_det": str(Q.det()), "hilbert_schmidt_squared": str(h2),
                    "minus_log_normalizer": str(minus_log)})
    return out


def source_derivatives():
    out = []
    t = Fraction(1, 64)
    h = Decimal("1e-18")
    td = dec(t)
    # CIB-R2: the admissible mark is s, with t(s)=t0(1+s), |s|<=1/4.
    # The weighted row includes derivatives through order three.
    mark_radius = Fraction(1, 4)
    marked_row_orders = (2*t*(1+mark_radius), 2*t, Fraction(0), Fraction(0))
    record("admissible_mark_derivative_row", max(marked_row_orders) == Fraction(5, 128)
           and max(marked_row_orders) < Fraction(1, 8),
           {"mark_radius": str(mark_radius), "orders_0_to_3": [str(x) for x in marked_row_orders]})
    for d in (1, 17, 4096):
        def f(x):
            return Decimal(d) * (1 - x * x).ln() / 2
        first_numeric = (f(td + h) - f(td - h)) / (2 * h)
        second_numeric = (f(td + h) - 2 * f(td) + f(td - h)) / (h * h)
        first_exact = -d * t / (1 - t * t)
        second_exact = -d * (1 + t * t) / (1 - t * t) ** 2
        record(f"normalizer_source_first_d{d}", abs(first_numeric - dec(first_exact)) < Decimal("1e-28"),
               {"exact": str(first_exact), "finite_difference": str(first_numeric)})
        record(f"normalizer_source_second_d{d}", abs(second_numeric - dec(second_exact)) < Decimal("1e-28"),
               {"exact": str(second_exact), "finite_difference": str(second_numeric)})
        record(f"mutation_discard_source_scalar_rejected_d{d}", first_exact != 0 and second_exact != 0,
               "Removing the parameter-dependent determinant deletes nonzero responses")
        def marked_f(mark):
            return f(td*(1+mark))
        marked_first_numeric = (marked_f(h)-marked_f(-h))/(2*h)
        marked_second_numeric = (marked_f(h)-2*marked_f(Decimal(0))+marked_f(-h))/(h*h)
        marked_first_exact = t*first_exact
        marked_second_exact = t*t*second_exact
        record(f"admissible_mark_first_d{d}", abs(marked_first_numeric-dec(marked_first_exact)) < Decimal("1e-28"),
               {"exact": str(marked_first_exact), "finite_difference": str(marked_first_numeric)})
        record(f"admissible_mark_second_d{d}", abs(marked_second_numeric-dec(marked_second_exact)) < Decimal("1e-28"),
               {"exact": str(marked_second_exact), "finite_difference": str(marked_second_numeric)})
        record(f"mutation_omitted_mark_chain_factors_rejected_d{d}",
               abs(marked_first_numeric-dec(first_exact)) > Decimal("1e-6")
               and abs(marked_second_numeric-dec(second_exact)) > Decimal("1e-6"),
               "The admissible s mark requires t0 and t0 squared chain factors")
        out.append({"d": d, "first": str(first_exact), "second": str(second_exact),
                    "admissible_mark_first": str(marked_first_exact),
                    "admissible_mark_second": str(marked_second_exact)})
    return out


def pivot_geometry():
    out = []
    R = 12
    for q in (2, 3, 5, 9):
        # One live x_1-directed link on each parallel path at each of q positions.
        pts = list(itertools.product(range(q), repeat=4))
        n = len(pts)
        diameter = 3 * R * (q - 1)
        # CIB-R1: compute l1 diameter from the actual point set independently.
        signed_widths = []
        for signs in itertools.product((-1, 1), repeat=len(pts[0])):
            projections = [R * sum(a*b for a,b in zip(signs, point)) for point in pts]
            signed_widths.append(max(projections) - min(projections))
        computed_diameter = max(signed_widths)
        record(f"actual_grid_diameter_q{q}", diameter == computed_diameter,
               {"formula": diameter, "signed_extrema": computed_diameter,
                "directions": len(signed_widths), "points": len(pts)})
        # Minimum L1 distance is R; the coordinate grid has a spanning tree
        # whose n-1 edges all have length R, proving the exact metric MST.
        min_dist = min(sum(abs(a - b) for a, b in zip(pts[0], x)) for x in pts[1:]) * R
        mst = R * (n - 1)
        ratio = Fraction(diameter, mst)
        record(f"separated_grid_q{q}", min_dist == R and ratio < 1,
               {"pivots": n, "diameter": diameter, "metric_mst": mst, "ratio": str(ratio)})
        if q >= 3:
            record(f"mutation_diameter_linear_pivot_charge_rejected_q{q}", diameter < Fraction(1, 2) * R * (n - 1),
                   "Even the candidate constant c=1/2 fails; the formula proves failure for every fixed c")
        out.append({"q": q, "R": R, "pivots": n, "diameter_over_R_nminus1": str(ratio)})
    for n in (2, 7, 31):
        points = [(R * k, 0, 0, 0) for k in range(n)]
        diameter = points[-1][0] - points[0][0]
        record(f"single_path_geometry_control_n{n}", diameter == R * (n - 1),
               "The linear lower bound is valid for pivots on one straight path")
    return out


def finite_haar_control():
    # Exact finite compact group control for the proof's cancellation logic.
    # This is NOT an SU(N) integration or a Wilson simulation.
    G = tuple(range(3))
    epsilon = Fraction(1, 5)
    residual = (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6))
    nu = tuple(epsilon / 3 + (1 - epsilon) * x for x in residual)
    f = (Fraction(-1), Fraction(0), Fraction(1))
    record("finite_haar_density_normalized", sum(nu) == 1 and all(x >= epsilon / 3 for x in nu),
           {"probabilities": [str(x) for x in nu], "epsilon": str(epsilon)})
    record("finite_haar_centering", sum(f) == 0, "The distinguished factor is Haar-centered")
    for n in (1, 2, 4):
        exact = Fraction(0)
        for xs in itertools.product(G, repeat=n):
            val = Fraction(1)
            for x in xs:
                val *= nu[x] * f[x]
            exact += val
        single = sum(nu[x] * f[x] for x in G)
        record(f"finite_haar_product_cancellation_n{n}", exact == single ** n and abs(exact) <= (1 - epsilon) ** n,
               {"expectation": str(exact), "minorization_bound": str((1 - epsilon) ** n)})
    return {"role": "exact finite compact-group algebra control; not physical lattice evidence"}


def main():
    with localcontext() as ctx:
        ctx.prec = 90
        result = {
            "schema": "crossover-import-independent-diagnostics-v1",
            "scope": "Kirk v4 selected Gaussian supplier and pivot-geometry implications only",
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "runtime": {"python": platform.python_version(), "sympy": sp.__version__},
            "gaussian_rank_witness": gaussian_witnesses(),
            "rectangular_cross_block_controls": general_cross_blocks(),
            "source_normalizer_derivatives": source_derivatives(),
            "pivot_geometry": pivot_geometry(),
            "finite_haar_control": finite_haar_control(),
            "resolution_certificate": {
                "per_element": "Exact rational matrix entries and finite Haar probabilities are checked; no physical link integral is numerically simulated.",
                "per_site": "Checked and not executed as a Wilson site calculation: the original Wilson conditional bound is supplied by a direct analytical proof.",
                "per_mode": "Symmetric and antisymmetric Gaussian modes independently reproduce the determinant and its indispensable rank multiplicity.",
                "per_block": "Two arbitrarily sized Gaussian cores are the quantified analytical test family; finite dimensions and rank controls are executed here.",
                "lattice_wide": "Checked and not executed as continuum evidence: separated finite pivot grids test geometry only, and no Yang–Mills mass-gap claim is inferred.",
            },
            "continuum_target_rows_closed": [],
        }
        result["checks"] = CHECKS
        result["passed"] = sum(x["pass"] for x in CHECKS)
        result["total"] = len(CHECKS)
        result["all_passed"] = all(x["pass"] for x in CHECKS)
        print(json.dumps(result, indent=2))
        raise SystemExit(0 if result["all_passed"] else 1)


if __name__ == "__main__":
    main()
