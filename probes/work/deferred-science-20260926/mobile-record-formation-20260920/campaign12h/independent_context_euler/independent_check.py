#!/usr/bin/env python3
"""Focused algebra and finite-block controls, without author-source imports."""
from collections import deque
from fractions import Fraction as F
from itertools import product
from math import factorial
from pathlib import Path
import json
import platform

import sympy as sp


CHECKS = []


def check(name, condition, details=None):
    if not condition:
        raise AssertionError((name, details))
    CHECKS.append({"name": name, "passed": True, "details": details})


def zero_matrix(matrix):
    return all(sp.cancel(x) == 0 for x in matrix)


def component(start, edges, vacancy_only=False):
    seen = {start}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        for x, y in edges:
            if state[x] == state[y]:
                continue
            if vacancy_only and not ((state[x] == 0) != (state[y] == 0)):
                continue
            changed = list(state)
            changed[x], changed[y] = changed[y], changed[x]
            changed = tuple(changed)
            if changed not in seen:
                seen.add(changed)
                queue.append(changed)
    return seen


def encode(value):
    if isinstance(value, (F, sp.Basic)):
        return str(value)
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


def main():
    p = sp.Matrix(sp.symbols("p1:7", positive=True))
    u, E, epsilon = sp.symbols("u E epsilon", real=True)
    rho = sum(p)
    p0 = 1 - rho
    one = sp.ones(6, 1)
    S = sp.diag(*[1 / x for x in p]) + sp.ones(6) / p0
    A = u + 2 * E * rho
    B = 2 * E - u - 4 * E * rho
    vectors = ((1, 0, 0), (-1, 0, 0), (0, 1, 0),
               (0, -1, 0), (0, 0, 1), (0, 0, -1))
    identities = []
    for axis in range(3):
        f = sp.Matrix([v[axis] for v in vectors])
        m = (p.T * f)[0]
        J = sp.Matrix([p[a] * (A * f[a] + B * m) for a in range(6)])
        G = A * m
        grad_G = sp.Matrix([sp.diff(G, x) for x in p])
        DJ = J.jacobian(p)
        check(f"flux_potential_axis_{axis}", zero_matrix(S * J - grad_G))
        check(f"entropy_symmetrizer_axis_{axis}", zero_matrix(S * DJ - (S * DJ).T))
        explicit_S_DJ = sp.diag(*[(A * f[a] + B * m) / p[a] for a in range(6)])
        explicit_S_DJ += 2 * E * (f * one.T + one * f.T)
        explicit_S_DJ -= (u + 4 * E * rho) * m / p0 * sp.ones(6)
        check(f"explicit_symmetric_matrix_axis_{axis}", zero_matrix(S * DJ - explicit_S_DJ))
        # Test cancellation with arbitrary spatial derivatives, without a PDE solver.
        dp = sp.Matrix(sp.symbols(f"d{axis}_1:7"))
        # Group coefficients before introducing six arbitrary derivative
        # symbols; expanding the ungrouped rational expression is needlessly
        # expensive and is algebraically the same identity.
        cancellation_matrix = (DJ.T * S - S * DJ).applyfunc(sp.cancel)
        linearized_entropy_coefficient = cancellation_matrix * dp
        check(f"linear_entropy_cancellation_axis_{axis}", zero_matrix(linearized_entropy_coefficient))
        identities.append({"axis": axis, "potential": G, "current": list(J)})

    reaction = epsilon * p0 * one
    reaction_lambda_dot = S * reaction
    for label in range(7):
        eta = sp.zeros(6, 1)
        if label:
            eta[label - 1] = 1
        forward_birth_ratio = -6 * epsilon if label == 0 else epsilon * p0 / p[label - 1]
        time_reference_term = ((eta - p).T * reaction_lambda_dot)[0]
        check(f"exact_birth_reference_cancellation_state_{label}", sp.cancel(forward_birth_ratio - time_reference_term) == 0)

    # The comparison process is an open 2x2x2 block inside the large torus,
    # not a periodic size-two implementation of the four-site context rate.
    sites = tuple(product(range(2), repeat=3))
    index = {x: i for i, x in enumerate(sites)}
    edges = []
    for x in sites:
        for axis in range(3):
            y = list(x)
            y[axis] += 1
            if y[axis] < 2:
                edges.append((index[x], index[tuple(y)]))
    with_vacancies = (0, 0, 1, 2, 3, 4, 5, 6)
    filled = (1, 1, 2, 2, 3, 4, 5, 6)
    first = component(with_vacancies, edges)
    second = component(filled, edges)
    restricted = component(filled, edges, vacancy_only=True)
    check("three_dimensional_block_count_sector_connected_with_vacancies",
          len(first) == factorial(8) // factorial(2),
          {"sites": 8, "edges": len(edges), "reachable_states": len(first)})
    check("three_dimensional_block_count_sector_connected_without_vacancies",
          len(second) == factorial(8) // (factorial(2) ** 2),
          {"reachable_states": len(second)})
    check("vacancy_only_floor_would_not_supply_this_block_lemma",
          len(restricted) == 1 and len(second) == 10080,
          {"vacancy_only_reachable_states": len(restricted), "full_count_sector_states": len(second)})

    # All seven-color sectors of a four-site path, not just one composition.
    path_edges = [(0, 1), (1, 2), (2, 3)]
    remaining = set(product(range(7), repeat=4))
    sectors = []
    while remaining:
        state = min(remaining)
        reached = component(state, path_edges)
        counts = tuple(state.count(a) for a in range(7))
        expected = factorial(4)
        for n in counts:
            expected //= factorial(n)
        assert len(reached) == expected
        assert all(tuple(s.count(a) for a in range(7)) == counts for s in reached)
        remaining.difference_update(reached)
        sectors.append(counts)
    check("all_seven_color_four_site_count_sectors", len(sectors) == 210,
          {"states": 7 ** 4, "connected_sectors": len(sectors)})

    # A forbidden replacement route fails even at a stationary product.
    expected_absolute_single_edge_current = sum(F(1, 49) * abs(int(a == 1) - int(b == 1))
                                                for a in range(7) for b in range(7))
    check("single_edge_absolute_replacement_is_false",
          expected_absolute_single_edge_current == F(12, 49),
          {"parameters": "u=E=0, K=1; all seven probabilities 1/7",
           "mean_current": 0, "mean_absolute_current": expected_absolute_single_edge_current})

    # Finite-population sampling error for one actual four-site current.
    V = ((0, 0, 0),) + vectors
    patterns = tuple(product(range(7), repeat=4))

    def local_current(s):
        l, a, b, r = s
        df = V[a][0] - V[b][0]
        dn = int(a != 0) - int(b != 0)
        h = -df + df * (int(l != 0) + int(r != 0)) + dn * (V[l][0] + V[r][0])
        c = F(4) + F(h, 2)  # u=-1, E=1, K=4
        return c * (int(a == 1) - int(b == 1))

    grand_current = sum(F(1, 7 ** 4) * local_current(s) for s in patterns)
    check("balanced_grand_canonical_current", grand_current == F(5, 49))
    finite_population = []
    for copies in (1, 2, 4, 8):
        population_size = 7 * copies
        canonical_current = F(0)
        for s in patterns:
            counts_left = [copies] * 7
            probability = F(1)
            for k, label in enumerate(s):
                probability *= F(counts_left[label], population_size - k)
                counts_left[label] -= 1
                if probability == 0:
                    break
            canonical_current += probability * local_current(s)
        error = abs(canonical_current - grand_current)
        # Four draws collide with probability at most 6/m in the elementary
        # with/without-replacement coupling; |current| is at most 7 here.
        bound = F(2 * 7 * 6, population_size)
        check(f"canonical_current_sampling_control_m{population_size}", error <= bound)
        finite_population.append({"m": population_size, "canonical_current": canonical_current,
                                  "grand_current": grand_current, "absolute_error": error,
                                  "coupling_error_upper_bound": bound})

    # Exact homogeneous product controls for the two distinct birth scalings.
    t, eps = sp.symbols("t eps", positive=True)
    N = sp.symbols("N", positive=True, integer=True)
    v0 = sp.Rational(1, 2)
    slow_vacancy = v0 * sp.exp(-6 * eps * t)
    fast_vacancy = v0 * sp.exp(-6 * N * eps * t)
    limiting_kl_to_slow_reference = -sp.log(1 - slow_vacancy)
    check("slow_birth_ode", sp.simplify(sp.diff(slow_vacancy, t) + 6 * eps * slow_vacancy) == 0)
    check("fixed_microscopic_birth_ode", sp.simplify(sp.diff(fast_vacancy, t) + 6 * N * eps * fast_vacancy) == 0)
    check("fixed_microscopic_birth_vacancy_limit", sp.limit(fast_vacancy, N, sp.oo) == 0)
    numerical_scaling = []
    for n in (4, 8, 16, 32):
        numerical_scaling.append({"N": n, "slow_vacancy": sp.N(slow_vacancy.subs({eps: sp.Rational(1, 12), t: 1}), 30),
                                  "fast_vacancy": sp.N(fast_vacancy.subs({N: n, eps: sp.Rational(1, 12), t: 1}), 30)})

    result = {"status": "all_focused_checks_passed", "python": platform.python_version(), "sympy": sp.__version__,
              "primary_sources_read": [], "checks": CHECKS, "check_count": len(CHECKS),
              "flux_identities": identities, "canonical_sampling": finite_population,
              "birth_scaling": {"slow_vacancy": slow_vacancy, "fixed_microscopic_vacancy": fast_vacancy,
                                "limiting_relative_entropy_per_site_against_slow_reference": limiting_kl_to_slow_reference,
                                "example_eps_1_over_12_t_1": numerical_scaling},
              "scope": "Exact algebra and finite controls; the general block-replacement and entropy-limit proofs are in REPORT.md, not inferred from these finite checks."}
    output = json.dumps(encode(result), indent=2, sort_keys=True) + "\n"
    Path(__file__).with_name("RESULTS.json").write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
