#!/usr/bin/env python3
"""Independent, exact checks of the supplied context-exchange generator.

No repository author source is imported or read.  All fractions are exact;
SymPy is used only for finite matrix characteristic polynomials.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json
import platform

import sympy as sp


V = ((0, 0, 0), (1, 0, 0), (-1, 0, 0),
     (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
INDEX = {v: a for a, v in enumerate(V)}
PATTERNS = tuple(product(range(7), repeat=4))
CHECKS = []


def check(name, condition, detail=None):
    if not condition:
        raise AssertionError((name, detail))
    CHECKS.append({"name": name, "passed": True, "detail": detail})


def coefficients(pattern, i):
    l, a, b, r = pattern
    df = V[a][i] - V[b][i]
    dn = int(a != 0) - int(b != 0)
    outer_n = int(l != 0) + int(r != 0)
    outer_f = V[l][i] + V[r][i]
    return df, df * outer_n + dn * outer_f


def rate(pattern, i, pars, implementation):
    df, context = coefficients(pattern, i)
    h = pars["u"] * df + pars["E"] * context
    if implementation == "linear":
        return pars["K"] + h / 2
    return pars["kappa0"] + max(h, F(0))


def prob_of(pattern, p):
    answer = F(1)
    for a in pattern:
        answer *= p[a]
    return answer


def exact_current(p, pars, implementation, i, derivative=False):
    current = [F(0) for _ in range(7)]
    jac = [[F(0) for _ in range(6)] for _ in range(6)]
    for pattern in PATTERNS:
        _, a, b, _ = pattern
        if a == b:
            continue
        mass_rate = prob_of(pattern, p) * rate(pattern, i, pars, implementation)
        current[a] += mass_rate
        current[b] -= mass_rate
        if derivative:
            counts = Counter(pattern)
            scores = [F(counts[label], 1) / p[label]
                      - F(counts[0], 1) / p[0] for label in range(1, 7)]
            for label, sign in ((a, 1), (b, -1)):
                if label:
                    for column, score in enumerate(scores):
                        jac[label - 1][column] += sign * mass_rate * score
    return current, jac


def formula_current(p, pars, i):
    rho = sum(p[1:])
    m = sum(p[a] * V[a][i] for a in range(1, 7))
    A = pars["u"] + 2 * pars["E"] * rho
    B = 2 * pars["E"] - pars["u"] - 4 * pars["E"] * rho
    occupied = [p[a] * (A * V[a][i] + B * m) for a in range(1, 7)]
    return [-p[0] * (pars["u"] + 4 * pars["E"] * rho) * m] + occupied


def formula_jacobian(rho, pars, i):
    A = pars["u"] + 2 * pars["E"] * rho
    B = 2 * pars["E"] - pars["u"] - 4 * pars["E"] * rho
    return [[A * V[a][i] * int(a == b)
             + rho / 6 * (2 * pars["E"] * V[a][i] + B * V[b][i])
             for b in range(1, 7)] for a in range(1, 7)]


def ring_pattern(state, x):
    return tuple(state[(x + offset) % 4] for offset in (-1, 0, 1, 2))


def ring_forward_check(p, pars, implementation, epsilon):
    exchange = {s: F(0) for s in PATTERNS}
    birth = {s: F(0) for s in PATTERNS}
    for state in PATTERNS:
        mass = prob_of(state, p)
        for x in range(4):
            y = (x + 1) % 4
            changed = list(state)
            changed[x], changed[y] = changed[y], changed[x]
            flux = mass * rate(ring_pattern(state, x), 0, pars, implementation)
            exchange[tuple(changed)] += flux
            exchange[state] -= flux
            if state[x] == 0:
                for a in range(1, 7):
                    changed = list(state)
                    changed[x] = a
                    birth[tuple(changed)] += epsilon * mass
                    birth[state] -= epsilon * mass
    dp = [-6 * epsilon * p[0]] + [epsilon * p[0]] * 6
    max_exchange = F(0)
    max_total = F(0)
    for state in PATTERNS:
        target = prob_of(state, p) * sum(dp[a] / p[a] for a in state)
        max_exchange = max(max_exchange, abs(exchange[state]))
        max_total = max(max_total, abs(exchange[state] + birth[state] - target))
    return {"states": len(PATTERNS), "max_exchange_residual": max_exchange,
            "max_exchange_plus_birth_product_flow_residual": max_total}


def matrix(values):
    return sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row]
                      for row in values])


def encode(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, sp.Basic):
        return str(value)
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


def main():
    tuned = {"u": F(-1), "E": F(1), "K": F(4), "kappa0": F(1)}
    generic = {"u": F(1), "E": F(1), "K": F(4), "kappa0": F(1)}
    biased_pars = {"u": F(3, 7), "E": F(-2, 5), "K": F(3), "kappa0": F(2, 3)}
    implementations = ("linear", "positive_part")
    max_df = 0
    max_context = 0
    positivity = {}
    for pars_name, pars in (("tuned", tuned), ("generic", generic), ("biased", biased_pars)):
        positivity[pars_name] = {}
        for implementation in implementations:
            minimum = min(rate(s, i, pars, implementation)
                          for s in PATTERNS for i in range(3))
            positivity[pars_name][implementation] = minimum
            check(f"strict_positive_{pars_name}_{implementation}", minimum > 0)
    for s in PATTERNS:
        l, a, b, r = s
        for i in range(3):
            df, context = coefficients(s, i)
            max_df = max(max_df, abs(df))
            max_context = max(max_context, abs(context))
            reverse = coefficients((l, b, a, r), i)
            assert reverse == (-df, -context)
            for implementation in implementations:
                difference = rate(s, i, tuned, implementation) - rate((l, b, a, r), i, tuned, implementation)
                assert difference == tuned["u"] * df + tuned["E"] * context
    check("local_coefficient_bounds_and_swap_identity", max_df == 2 and max_context == 4,
          {"patterns": len(PATTERNS), "directions": 3, "max_abs_df": max_df,
           "max_abs_context": max_context})

    rotations_checked = 0
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            transform = [INDEX[tuple(signs[j] * v[perm[j]] for j in range(3))] for v in V]
            for i in range(3):
                j = perm.index(i)
                for s in PATTERNS:
                    transformed = tuple(transform[a] for a in s)
                    if signs[j] == -1:
                        transformed = transformed[::-1]
                    assert coefficients(s, i) == coefficients(transformed, j)
                    rotations_checked += 1
    check("joint_cubic_covariance_all_signed_permutations", True,
          {"group_elements": 48, "pattern_direction_group_cases": rotations_checked})

    for s in PATTERNS:
        sums = [sum(coefficients(ring_pattern(s, x), 0)[j] for x in range(4)) for j in range(2)]
        assert sums == [0, 0]
    check("periodic_line_pointwise_divergence", True, {"ring_size": 4, "states": len(PATTERNS)})
    bad_state = (1, 0, 0, 3)
    missing_cross_divergence = sum((V[ring_pattern(bad_state, x)[1]][0] - V[ring_pattern(bad_state, x)[2]][0])
                                  * (int(ring_pattern(bad_state, x)[0] != 0) + int(ring_pattern(bad_state, x)[3] != 0))
                                  for x in range(4))
    check("deleting_cross_term_breaks_balance", missing_cross_divergence == 1,
          {"state_indices": bad_state, "divergence_of_E_coefficient": missing_cross_divergence})

    p_tuned = [F(1, 2)] + [F(1, 12)] * 6
    p_biased = [F(x, 30) for x in (9, 3, 5, 4, 2, 1, 6)]
    current_records = []
    for case, p, pars in (("tuned_balanced", p_tuned, tuned), ("biased", p_biased, biased_pars)):
        for i in range(3):
            expected = formula_current(p, pars, i)
            for implementation in implementations:
                current, _ = exact_current(p, pars, implementation, i)
                check(f"current_{case}_axis{i}_{implementation}", current == expected and sum(current) == 0)
                current_records.append({"case": case, "axis": i, "implementation": implementation, "current_0_to_6": current})

    direct_jacobians = {}
    for case, pars in (("tuned", tuned), ("generic", generic)):
        direct_jacobians[case] = []
        for i in range(3):
            expected = formula_jacobian(F(1, 2), pars, i)
            for implementation in implementations:
                _, jac = exact_current(p_tuned, pars, implementation, i, derivative=True)
                check(f"direct_product_derivative_{case}_axis{i}_{implementation}", jac == expected)
            direct_jacobians[case].append(matrix(jac))
    check("tuned_derivative_keeps_u_fixed", direct_jacobians["tuned"][0][0, 2] == sp.Rational(1, 6),
          {"d_J_plus_e1_axis1_d_p_plus_e2": direct_jacobians["tuned"][0][0, 2],
           "incorrect_differentiate_along_tuning_value": 0})

    a, g, w1, w2, w3, mu = sp.symbols("a g w1 w2 w3 mu")
    squared_matrix = sp.diag(w1, w2, w3) * (a * sp.eye(3) + g * sp.ones(3))
    proposed = (mu ** 3 - (a + g) * (w1 + w2 + w3) * mu ** 2
                + a * (a + 2 * g) * (w1 * w2 + w1 * w3 + w2 * w3) * mu
                - a ** 2 * (a + 3 * g) * w1 * w2 * w3)
    check("symbolic_squared_speed_characteristic_polynomial",
          sp.expand(squared_matrix.charpoly(mu).as_expr() - proposed) == 0)

    directions = {"axis": (1, 0, 0), "plane_3_4_5": (sp.Rational(3, 5), sp.Rational(4, 5), 0),
                  "space_1_2_2": (sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(2, 3)),
                  "body_diagonal": (1 / sp.sqrt(3),) * 3}
    lam = sp.Symbol("lambda")
    spectra = {}
    for case in direct_jacobians:
        spectra[case] = {}
        for name, direction in directions.items():
            directional = sum((direction[i] * direct_jacobians[case][i] for i in range(3)), sp.zeros(6))
            polynomial = sp.factor(directional.charpoly(lam).as_expr())
            spectra[case][name] = polynomial
            if case == "tuned":
                check(f"isotropic_tuned_spectrum_{name}", sp.expand(polynomial - lam ** 4 * (lam ** 2 - sp.Rational(1, 6))) == 0)
        if case == "generic":
            check("generic_axis_spectrum", sp.expand(spectra[case]["axis"] - lam ** 4 * (lam ** 2 - sp.Rational(25, 6))) == 0)
            check("generic_body_diagonal_spectrum", sp.expand(spectra[case]["body_diagonal"] - (lam ** 2 - sp.Rational(4, 3)) ** 2 * (lam ** 2 - sp.Rational(3, 2))) == 0)
            check("generic_direction_dependence", spectra[case]["axis"] != spectra[case]["body_diagonal"])

    ring_records = {}
    for implementation in implementations:
        residuals = ring_forward_check(p_biased, tuned, implementation, F(2, 7))
        ring_records[implementation] = residuals
        check(f"exact_ring_forward_equation_{implementation}",
              residuals["max_exchange_residual"] == 0 and residuals["max_exchange_plus_birth_product_flow_residual"] == 0)

    full = [F(0)] + [F(1, 6)] * 6
    traffic = {}
    for implementation in implementations:
        traffic[implementation] = sum(prob_of(s, full) * rate(s, 0, tuned, implementation)
                                      for s in PATTERNS if s[1] != s[2])
    check("full_occupancy_exchange_activity", traffic["linear"] == F(5, 6) * tuned["K"]
          and traffic["positive_part"] >= F(5, 6) * tuned["kappa0"], traffic)

    result = {"status": "all_exact_checks_passed", "python": platform.python_version(), "sympy": sp.__version__,
              "source_boundary": "Supplied task specification only; no primary or other repository calculation read or imported.",
              "alphabet": V, "parameters": {"tuned": tuned, "generic": generic, "biased": biased_pars},
              "positivity_minima": positivity, "checks": CHECKS, "check_count": len(CHECKS),
              "currents": current_records,
              "jacobians": {case: [m.tolist() for m in mats] for case, mats in direct_jacobians.items()},
              "directional_characteristic_polynomials": spectra, "ring_forward_equation": ring_records,
              "full_occupancy_unequal_exchange_rate_per_edge": traffic}
    rendered = json.dumps(encode(result), indent=2, sort_keys=True) + "\n"
    Path(__file__).with_name("RESULTS.json").write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
