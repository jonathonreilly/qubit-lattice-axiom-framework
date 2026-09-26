#!/usr/bin/env python3
"""Exact controls for the supplied axis-balanced context generator.

No primary calculation or prior checker is imported.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json
import platform

import sympy as sp


ROOT = Path(__file__).resolve().parent
PROGRESS = (ROOT / "PROGRESS.log").open("w")
V = ((0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0),
     (0, -1, 0), (0, 0, 1), (0, 0, -1))
INDEX = {v: a for a, v in enumerate(V)}
PATTERNS = tuple(product(range(7), repeat=4))
CHECKS = []


def check(name, condition, details=None):
    if not condition:
        raise AssertionError((name, details))
    CHECKS.append({"name": name, "passed": True, "details": details})
    print(name, file=PROGRESS, flush=True)


def coefficients(pattern, i):
    l, a, b, r = pattern
    fl, fa, fb, fr = (V[x][i] for x in pattern)
    df = fa - fb
    dn = int(a != 0) - int(b != 0)
    dq = fa * fa - fb * fb
    cn = df * (int(l != 0) + int(r != 0)) + dn * (fl + fr)
    cq = df * (fl * fl + fr * fr) + dq * (fl + fr)
    return df, cn, cq


def s_value(a, i, pars):
    return pars["A"] * int(a != 0) + pars["B"] * V[a][i] ** 2


def rate(pattern, i, pars, kind):
    df, cn, cq = coefficients(pattern, i)
    h = pars["u"] * df + pars["E"] * (pars["A"] * cn + pars["B"] * cq)
    return pars["K"] + h / 2 if kind == "linear" else pars["kappa0"] + max(h, F(0))


def probability(state, p):
    answer = F(1)
    for a in state:
        answer *= p[a]
    return answer


def input_table(p):
    answer = []
    for pattern in PATTERNS:
        counts = Counter(pattern)
        scores = [F(counts[a], 1) / p[a] - F(counts[0], 1) / p[0] for a in range(1, 7)]
        answer.append((pattern, probability(pattern, p), scores))
    return answer


def direct_current_jacobian(table, pars, i, kind):
    current = [F(0)] * 7
    jac = [[F(0) for _ in range(6)] for _ in range(6)]
    for pattern, mass, scores in table:
        _, a, b, _ = pattern
        if a == b:
            continue
        weight = mass * rate(pattern, i, pars, kind)
        current[a] += weight
        current[b] -= weight
        for label, sign in ((a, 1), (b, -1)):
            if label:
                for column, score in enumerate(scores):
                    jac[label - 1][column] += sign * weight * score
    return current, jac


def analytic_current_jacobian(p, pars, i):
    sigma = sum(p[a] * s_value(a, i, pars) for a in range(7))
    m = sum(p[a] * V[a][i] for a in range(7))
    U = pars["u"] + 2 * pars["E"] * sigma
    Z = pars["u"] + 4 * pars["E"] * sigma
    bracket = [U * V[a][i] + (2 * pars["E"] * s_value(a, i, pars) - Z) * m for a in range(7)]
    current = [p[a] * bracket[a] for a in range(7)]
    jac = [[int(a == b) * bracket[a] + p[a] * (
        2 * pars["E"] * s_value(b, i, pars) * V[a][i]
        - 4 * pars["E"] * s_value(b, i, pars) * m
        + (2 * pars["E"] * s_value(a, i, pars) - Z) * V[b][i])
        for b in range(1, 7)] for a in range(1, 7)]
    return current, jac


def mat(values):
    return sp.Matrix([[sp.Rational(x.numerator, x.denominator) if isinstance(x, F) else x
                       for x in row] for row in values])


def convex_hull(points):
    points = sorted(set(points))
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower, upper = [], []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def ring_pattern(state, x):
    return tuple(state[(x + off) % 4] for off in (-1, 0, 1, 2))


def ring_forward(p, pars, kind, epsilon):
    exchange = {s: F(0) for s in PATTERNS}
    birth = {s: F(0) for s in PATTERNS}
    for state in PATTERNS:
        mass = probability(state, p)
        for x in range(4):
            y = (x + 1) % 4
            changed = list(state)
            changed[x], changed[y] = changed[y], changed[x]
            flow = mass * rate(ring_pattern(state, x), 0, pars, kind)
            exchange[tuple(changed)] += flow
            exchange[state] -= flow
            if state[x] == 0:
                for a in range(1, 7):
                    changed = list(state)
                    changed[x] = a
                    birth[tuple(changed)] += epsilon * mass
                    birth[state] -= epsilon * mass
    dp = [-6 * epsilon * p[0]] + [epsilon * p[0]] * 6
    residual_exchange = max(abs(x) for x in exchange.values())
    residual_flow = max(abs(exchange[s] + birth[s] - probability(s, p) * sum(dp[a] / p[a] for a in s)) for s in PATTERNS)
    return {"exchange": residual_exchange, "exchange_plus_birth_product_flow": residual_flow}


def encode(value):
    if isinstance(value, (F, sp.Basic)):
        return str(value)
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


def main():
    witness = {"u": F(0), "E": F(1, 2), "A": F(2), "B": F(-3), "K": F(3), "kappa0": F(1)}
    generic = {"u": F(1, 3), "E": F(2, 5), "A": F(3, 2), "B": F(-2), "K": F(4), "kappa0": F(1)}
    kinds = ("linear", "positive_part")
    coefficient_points = set()
    for pattern in PATTERNS:
        l, a, b, r = pattern
        for i in range(3):
            coeff = coefficients(pattern, i)
            assert coefficients((l, b, a, r), i) == tuple(-x for x in coeff)
            coefficient_points.add(coeff[1:])
    hull = convex_hull(coefficient_points)
    expected_hull = {(-4, -4), (-2, -4), (4, 0), (4, 4), (2, 4), (-4, 0)}
    check("sharp_context_coefficient_hull", set(hull) == expected_hull, {"vertices": hull})
    check("endpoint_antisymmetry_all_local_states", True, {"patterns": 7 ** 4, "axes": 3})

    covariance_cases = 0
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            transform = [INDEX[tuple(signs[j] * v[perm[j]] for j in range(3))] for v in V]
            for i in range(3):
                j = perm.index(i)
                for pattern in PATTERNS:
                    transformed = tuple(transform[a] for a in pattern)
                    if signs[j] == -1:
                        transformed = transformed[::-1]
                    assert coefficients(pattern, i) == coefficients(transformed, j)
                    covariance_cases += 1
    check("all_48_joint_cubic_transformations", True, {"local_cases": covariance_cases})

    for state in PATTERNS:
        assert all(sum(coefficients(ring_pattern(state, x), 0)[j] for x in range(4)) == 0 for j in range(3))
    check("periodic_line_divergence_each_parameter_coefficient", True, {"states": 7 ** 4})
    rate_ranges = {}
    for name, pars in (("witness", witness), ("generic", generic)):
        rate_ranges[name] = {}
        M = max(4 * abs(pars["A"]), 4 * abs(pars["A"] + pars["B"]), 2 * abs(pars["A"] + 2 * pars["B"]))
        observed = max(abs(pars["A"] * cn + pars["B"] * cq) for cn, cq in coefficient_points)
        check(f"sharp_context_bound_{name}", observed == M)
        for kind in kinds:
            values = [rate(s, 0, pars, kind) for s in PATTERNS]
            rate_ranges[name][kind] = (min(values), max(values))
            check(f"positive_rates_{name}_{kind}", min(values) > 0)
            for s in PATTERNS:
                l, a, b, r = s
                df, cn, cq = coefficients(s, 0)
                expected = pars["u"] * df + pars["E"] * (pars["A"] * cn + pars["B"] * cq)
                assert rate(s, 0, pars, kind) - rate((l, b, a, r), 0, pars, kind) == expected
    check("rate_reverse_difference_for_both_implementations", True)

    cases = [(f"witness_rho_{rho}", [1 - rho] + [rho / 6] * 6, witness, rho)
             for rho in (F(1, 4), F(1, 2), F(3, 4))]
    cases += [("generic_balanced", [F(1, 2)] + [F(1, 12)] * 6, generic, F(1, 2)),
              ("generic_biased", [F(x, 30) for x in (9, 3, 5, 4, 2, 1, 6)], generic, None)]
    transformation = sp.zeros(6)
    for j in range(3):
        transformation[j, 2 * j] = transformation[j, 2 * j + 1] = 1
        transformation[3 + j, 2 * j] = 1
        transformation[3 + j, 2 * j + 1] = -1
    inverse_transformation = transformation.inv()
    jacobians, currents = {}, []
    for name, p, pars, balanced_rho in cases:
        table = input_table(p)
        jacobians[name] = []
        p_sp = [sp.Rational(x.numerator, x.denominator) if isinstance(x, F) else sp.Rational(x) for x in p]
        S = sp.diag(*[1 / x for x in p_sp[1:]]) + sp.ones(6) / p_sp[0]
        for i in range(3):
            wanted_current, wanted_jac = analytic_current_jacobian(p, pars, i)
            for kind in kinds:
                current, jac = direct_current_jacobian(table, pars, i, kind)
                check(f"direct_current_and_six_derivatives_{name}_axis{i}_{kind}",
                      current == wanted_current and sum(current) == 0 and jac == wanted_jac)
                current_matrix = mat(jac)
                assert S * current_matrix == (S * current_matrix).T
            jacobians[name].append(current_matrix)
            currents.append({"case": name, "axis": i, "current_0_to_6": current})
            if balanced_rho is not None:
                rho = sp.Rational(balanced_rho.numerator, balanced_rho.denominator)
                u, E, A, B = [sp.Rational(pars[key].numerator, pars[key].denominator) for key in ("u", "E", "A", "B")]
                alpha = u + 2 * E * rho * (A + 2 * B / 3)
                beta = rho * (2 * E * A - u - 4 * E * rho * (A + B / 3)) / 3
                gamma = 2 * E * A * rho / 3
                direction = sp.zeros(3, 1)
                direction[i] = 1
                D = sp.diag(*direction)
                M = (alpha * sp.eye(3) + beta * sp.ones(3)) * D
                N = D * (alpha * sp.eye(3) + gamma * sp.ones(3))
                expected = sp.zeros(3).row_join(M).col_join(N.row_join(sp.zeros(3)))
                assert transformation * current_matrix * inverse_transformation == expected
    check("nonlinear_entropy_symmetry_at_all_checked_profiles", True)
    check("six_field_block_form_from_direct_derivatives", True)

    # Symbolic identities grouped by moments, avoiding needless large expansions.
    u, E, A, B, rho, sigma, m, fa, fb, sa, sb = sp.symbols("u E A B rho sigma m fa fb sa sb")
    U, Z = u + 2 * E * sigma, u + 4 * E * sigma
    total_current = U * m + (2 * E * sigma - Z * rho) * m
    check("symbolic_total_occupied_current", sp.expand(total_current - (1 - rho) * Z * m) == 0)
    entropy_gradient_component = U * fa + (2 * E * sa - Z) * m + total_current / (1 - rho)
    check("symbolic_flux_potential", sp.cancel(entropy_gradient_component - (U * fa + 2 * E * sa * m)) == 0)
    off_diagonal_S_DJ = (2 * E * sb * fa - 4 * E * sb * m + (2 * E * sa - Z) * fb
                         + (-Z * m + 4 * E * (1 - rho) * sb * m + (1 - rho) * Z * fb) / (1 - rho))
    expected_off_diagonal = 2 * E * (sb * fa + sa * fb) - Z * m / (1 - rho)
    check("symbolic_nonlinear_entropy_symmetry", sp.cancel(off_diagonal_S_DJ - expected_off_diagonal) == 0)
    alpha = u + 2 * E * rho * (A + 2 * B / 3)
    beta = rho * (2 * E * A - u - 4 * E * rho * (A + B / 3)) / 3
    gamma = 2 * E * A * rho / 3
    Q = (1 - rho) * (u + 4 * E * rho * (A + B / 3)) ** 2
    check("symbolic_squared_speed_factor", sp.expand((alpha + 3 * beta) * (alpha + 3 * gamma) - Q) == 0)
    check("all_density_tuning_and_speed",
          sp.simplify(alpha.subs({u: 0, B: -3 * A / 2})) == 0
          and sp.simplify(Q.subs({u: 0, B: -3 * A / 2}) / 3 - 4 * E ** 2 * A ** 2 * rho ** 2 * (1 - rho) / 3) == 0)
    lam, mu, aa, gg, w1, w2, w3 = sp.symbols("lambda mu alpha g w1 w2 w3")
    squared = sp.diag(w1, w2, w3) * (aa ** 2 * sp.eye(3) + gg * sp.ones(3))
    polynomial = (mu ** 3 - (aa ** 2 + gg) * (w1 + w2 + w3) * mu ** 2
                  + aa ** 2 * (aa ** 2 + 2 * gg) * (w1 * w2 + w1 * w3 + w2 * w3) * mu
                  - aa ** 4 * (aa ** 2 + 3 * gg) * w1 * w2 * w3)
    check("general_directional_squared_speed_polynomial", sp.expand(squared.charpoly(mu).as_expr() - polynomial) == 0)
    directions = {"axis": (1, 0, 0), "plane": (sp.Rational(3, 5), sp.Rational(4, 5), 0),
                  "space": (sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(2, 3)),
                  "diagonal": (1 / sp.sqrt(3),) * 3}
    spectra = {}
    for name, p, pars, balanced_rho in cases:
        if balanced_rho is None:
            continue
        spectra[name] = {}
        for direction_name, direction in directions.items():
            directional = sum((direction[i] * jacobians[name][i] for i in range(3)), sp.zeros(6))
            characteristic = sp.factor(directional.charpoly(lam).as_expr())
            spectra[name][direction_name] = characteristic
            if name.startswith("witness"):
                r = sp.Rational(balanced_rho.numerator, balanced_rho.denominator)
                speed_squared = 4 * r ** 2 * (1 - r) / 3
                check(f"witness_full_spectrum_{name}_{direction_name}",
                      sp.expand(characteristic - lam ** 4 * (lam ** 2 - speed_squared)) == 0
                      and directional.rank() == 2 and len(directional.nullspace()) == 4)
        if name == "generic_balanced":
            check("generic_anisotropy_control",
                  sp.expand(spectra[name]["axis"] - lam ** 4 * (lam ** 2 - sp.Rational(41, 150))) == 0
                  and sp.expand(spectra[name]["diagonal"] - (lam ** 2 - sp.Rational(4, 75)) ** 2 * (lam ** 2 - sp.Rational(1, 6))) == 0)

    z = sp.Symbol("z")
    eps = sp.Rational(1, 7)
    frozen_matrix = -sp.I * jacobians["witness_rho_1/2"][0] - eps * sp.ones(6)
    frozen_characteristic = sp.factor(frozen_matrix.charpoly(z).as_expr())
    check("frozen_reaction_spectrum_with_four_extra_modes",
          sp.expand(frozen_characteristic - z ** 4 * (z ** 2 + 6 * eps * z + sp.Rational(1, 6))) == 0)

    p_biased = [F(x, 30) for x in (9, 3, 5, 4, 2, 1, 6)]
    ring = {}
    activity = {}
    p_full = [F(0)] + [F(1, 6)] * 6
    for kind in kinds:
        ring[kind] = ring_forward(p_biased, witness, kind, F(2, 7))
        check(f"exact_ring_product_stationarity_and_birth_flow_{kind}", all(v == 0 for v in ring[kind].values()))
        activity[kind] = sum(probability(s, p_full) * rate(s, 0, witness, kind) for s in PATTERNS if s[1] != s[2])
    check("full_occupancy_activity", activity["linear"] == F(5, 2) and activity["positive_part"] >= F(5, 6), activity)

    result = {"status": "all_exact_checks_passed", "python": platform.python_version(), "sympy": sp.__version__,
              "primary_sources_read": [], "parameters": {"witness": witness, "generic": generic},
              "checks": CHECKS, "check_count": len(CHECKS), "rate_ranges": rate_ranges,
              "coefficient_hull": hull, "currents": currents,
              "jacobians": {name: [m.tolist() for m in matrices] for name, matrices in jacobians.items()},
              "directional_characteristic_polynomials": spectra,
              "frozen_birth_characteristic_polynomial": frozen_characteristic,
              "ring_forward_equation_residuals": ring, "balanced_full_occupancy_activity_per_edge": activity,
              "scope": "Finite and symbolic controls; the all-density classification and Euler applicability are proved in REPORT.md, not inferred from the sampled densities or directions."}
    rendered = json.dumps(encode(result), indent=2, sort_keys=True) + "\n"
    (ROOT / "RESULTS.json").write_text(rendered)
    print(rendered, end="")
    PROGRESS.close()


if __name__ == "__main__":
    main()
