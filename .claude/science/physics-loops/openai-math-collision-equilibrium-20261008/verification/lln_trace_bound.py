#!/usr/bin/env python3
"""Exact finite certificates for the supplied D3Q27 collision model.

Standard library only; no network, off-repository files, empirical inputs,
ODE integrator, or external theorem re-verification. The companion note proves
positivity, entropy minimization, convergence and the fixed-velocity LLN.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from math import factorial, prod
import sys

AUDIT_TIMEOUT_SEC = 120
PASS = 0
FAIL = 0
Q = Fraction


def check(label, condition, detail):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}: {detail}", flush=True)
    else:
        FAIL += 1
        print(f"FAIL {label}: {detail}", flush=True)


def pair_key(velocities, pair):
    i, j = pair
    return tuple(velocities[i][d] + velocities[j][d] for d in range(3)) + (
        sum(z * z for z in velocities[i] + velocities[j]),
    )


def construct():
    velocities = list(product((-1, 0, 1), repeat=3))
    groups = defaultdict(list)
    for pair in combinations_with_replacement(range(len(velocities)), 2):
        groups[pair_key(velocities, pair)].append(pair)
    reactions = [
        (a, b)
        for key in sorted(groups)
        for a, b in combinations(groups[key], 2)
    ]
    columns = []
    for a, b in reactions:
        nu = [0] * len(velocities)
        for i in a:
            nu[i] -= 1
        for i in b:
            nu[i] += 1
        columns.append(nu)
    invariants = [[1] * 27] + [
        [v[d] for v in velocities] for d in range(3)
    ] + [[sum(z * z for z in v) for v in velocities]]
    return velocities, groups, reactions, columns, invariants


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def modular_pivots(matrix, prime):
    """Independent finite-field elimination, retaining original row indices."""
    a = [[x % prime for x in row] for row in matrix]
    order = list(range(len(a)))
    chosen_rows, chosen_cols = [], []
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        order[rank], order[pivot] = order[pivot], order[rank]
        chosen_rows.append(order[rank])
        chosen_cols.append(col)
        inverse = pow(a[rank][col], -1, prime)
        a[rank] = [(x * inverse) % prime for x in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                factor = a[i][col]
                a[i] = [(x - factor * y) % prime for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return chosen_rows, chosen_cols


def integer_determinant(matrix):
    """Bareiss elimination over integers, independent of modular elimination."""
    a = [list(row) for row in matrix]
    n, previous, sign = len(a), 1, 1
    if n == 0:
        return 1
    for k in range(n - 1):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot_value - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot_value
    return sign * a[-1][-1]


def prime_log(value):
    """Exact coefficients of log(prime) for a positive rational value."""
    out = defaultdict(int)
    for number, sign in ((value.numerator, 1), (value.denominator, -1)):
        p = 2
        while p * p <= number:
            while number % p == 0:
                out[p] += sign
                number //= p
            p += 1
        if number > 1:
            out[number] += sign
    return {p: c for p, c in out.items() if c}


def polynomial_drift(f, reactions, columns, rates):
    out = [Q(0)] * 27
    for ((i, j), (k, l)), nu, rate in zip(reactions, columns, rates):
        flux = rate * (f[i] * f[j] - f[k] * f[l])
        for a in range(27):
            out[a] += nu[a] * flux
    return out


def main():
    velocities, groups, reactions, columns, invariants = construct()
    index = {v: i for i, v in enumerate(velocities)}
    check("network", len(velocities) == 3**3 and sum(map(len, groups.values())) == 27 * 28 // 2,
          f"species={len(velocities)} pair-complexes={sum(map(len, groups.values()))} reversible-pairs={len(reactions)} directed={2 * len(reactions)}")
    directed = set(reactions) | {(b, a) for a, b in reactions}
    check("weak-reversibility", all((b, a) in directed and a != b for a, b in directed),
          "every directed reaction has its explicit one-edge reverse")
    check("four-distinct-species", all(len(set(a + b)) == 4 for a, b in reactions),
          "nontrivial input/output pairs share no species; each stoichiometric column has squared Euclidean norm 4")
    check("five-conservation-identities", all(dot(row, col) == 0 for row in invariants for col in columns),
          f"all {5 * len(columns)} integer row-column contractions vanish")

    # Check every coordinate rectangle used in the analytic separability proof.
    rectangles = 0
    for d, e in combinations(range(3), 2):
        other = next(x for x in range(3) if x not in (d, e))
        for z, x, xp, y, yp in product((-1, 0, 1), repeat=5):
            vs = []
            for u, v in ((x, y), (xp, yp), (x, yp), (xp, y)):
                point = [0, 0, 0]
                point[other], point[d], point[e] = z, u, v
                vs.append(index[tuple(point)])
            left, right = tuple(sorted(vs[:2])), tuple(sorted(vs[2:]))
            assert left == right or (left, right) in directed
            rectangles += 1
    axis_pairs = []
    for d in range(3):
        vp = tuple(int(i == d) for i in range(3))
        vm = tuple(-int(i == d) for i in range(3))
        axis_pairs.append(tuple(sorted((index[vp], index[vm]))))
    check("analytic-invariant-generators", all((axis_pairs[0], axis_pairs[d]) in directed for d in (1, 2)),
          f"{rectangles} coordinate rectangles checked; x/y/z axis-pair exchanges link quadratic coefficients")

    basis_columns = [index[(0, 0, 0)], index[(1, 0, 0)], index[(-1, 0, 0)], index[(0, 1, 0)], index[(0, 0, 1)]]
    invariant_minor = integer_determinant([[row[j] for j in basis_columns] for row in invariants])
    matrix = [[col[i] for col in columns] for i in range(27)]
    pivot_rows, pivot_cols = modular_pivots(matrix, 1000003)
    minor = [[matrix[i][j] for j in pivot_cols] for i in pivot_rows]
    determinant = integer_determinant(minor)
    check("exact-rank-certificate", len(pivot_cols) == 22 and determinant != 0 and invariant_minor != 0,
          f"stoichiometric rank=22; integer 22x22 determinant={determinant}; invariant 5x5 determinant={invariant_minor}")
    print(f"CERTIFICATE row_indices={pivot_rows} column_indices={pivot_cols}")

    raw = [Q(2) ** v[0] * Q(3) ** v[1] * Q(5) ** v[2] * Q(7) ** (-sum(z * z for z in v)) for v in velocities]
    total = sum(raw)
    gibbs = [q / total for q in raw]
    check("rational-gibbs-balance", all(gibbs[i] * gibbs[j] == gibbs[k] * gibbs[l] for (i, j), (k, l) in reactions),
          "q_v proportional to 2^vx 3^vy 5^vz 7^(-|v|^2); all 288 forward/reverse monomials agree exactly")
    rates = [Q(1 + (r % 7), 3) for r in range(len(reactions))]
    check("positive-fixed-rates", all(rate > 0 for rate in rates) and not any(polynomial_drift(gibbs, reactions, columns, rates)),
          "nonuniform rational rates shared by each reversible pair leave the Gibbs state stationary")

    f = [Q(i + 1, 378) for i in range(27)]
    drift = polynomial_drift(f, reactions, columns, rates)
    log_sum = defaultdict(Fraction)
    for fi, di in zip(f, drift):
        for p, coefficient in prime_log(fi).items():
            log_sum[p] += di * coefficient
    positive_terms = 0
    for ((i, j), (k, l)), rate in zip(reactions, rates):
        x, y = f[i] * f[j], f[k] * f[l]
        # log is strictly increasing, so this rational sign check identifies
        # the sign of (x-y) log(x/y) without numerical logarithms.
        assert (x - y) * (x / y - 1) >= 0
        positive_terms += int(x != y)
        for p, coefficient in prime_log(x / y).items():
            log_sum[p] += rate * (x - y) * coefficient
    check("entropy-production-identity", all(value == 0 for value in log_sum.values()) and positive_terms > 0,
          f"exact prime-log coefficients cancel; {positive_terms} strictly dissipative reaction terms at a rational nonstationary state")

    # A non-equilibrium positive state in the same moment class as q.
    epsilon = min(gibbs) / 10
    perturbed = [q + epsilon * c for q, c in zip(gibbs, columns[0])]
    check("positive-compatibility-witness", min(perturbed) > 0 and all(dot(row, perturbed) == dot(row, gibbs) for row in invariants)
          and any(polynomial_drift(perturbed, reactions, columns, rates)),
          "q+epsilon*nu is strictly positive, conserves all five moments, and is not stationary")

    # Exhaust every possible two-particle state and every allowed transition.
    states = []
    for i, j in combinations_with_replacement(range(27), 2):
        n = [0] * 27
        n[i] += 1
        n[j] += 1
        states.append(tuple(n))
    weights = {n: prod(gibbs[i] ** n[i] / factorial(n[i]) for i in range(27)) for n in states}
    transition_count = 0
    for n in states:
        for ((i, j), (k, l)), nu, rate in zip(reactions, columns, rates):
            for sign, source, target in ((1, (i, j), (k, l)), (-1, (k, l), (i, j))):
                u, v = source
                if n[u] * n[v] == 0:
                    continue
                m = tuple(n[a] + sign * nu[a] for a in range(27))
                forward = rate * Q(n[u] * n[v], 2)
                reverse = rate * Q(m[target[0]] * m[target[1]], 2)
                assert m in weights and min(m) >= 0
                assert weights[n] * forward == weights[m] * reverse
                assert all(dot(row, n) == dot(row, m) for row in invariants)
                transition_count += 1
    check("finite-chain-detailed-balance", transition_count == 2 * len(reactions),
          f"all {len(states)} N=2 states and {transition_count} allowed directed transitions; factorial Gibbs weights, rates and invariants checked exactly")

    # Compare the conditional generator against a separate polynomial ODE
    # implementation and retain the normalization of both martingale brackets.
    tested = []
    K = sum(rates)
    for counts in ([i + 1 for i in range(27)], [2 if i % 3 else 0 for i in range(27)], [int(i in (0, 13, 26)) for i in range(27)]):
        N = sum(counts)
        state = [Q(x, N) for x in counts]
        generator_drift = [Q(0)] * 27
        bracket = [[Q(0)] * 27 for _ in range(27)]
        for ((i, j), (k, l)), nu, rate in zip(reactions, columns, rates):
            plus = rate * Q(counts[i] * counts[j], N)
            minus = rate * Q(counts[k] * counts[l], N)
            support = [a for a, x in enumerate(nu) if x]
            for a in support:
                generator_drift[a] += Q(nu[a], N) * (plus - minus)
                for b in support:
                    bracket[a][b] += Q(nu[a] * nu[b], N * N) * (plus + minus)
        ode = polynomial_drift(state, reactions, columns, rates)
        expected = [[sum(rate * nu[a] * nu[b] * (state[i] * state[j] + state[k] * state[l])
                         for ((i, j), (k, l)), nu, rate in zip(reactions, columns, rates)) / N
                     for b in range(27)] for a in range(27)]
        assert generator_drift == ode and bracket == expected
        assert all(sum(row[a] * bracket[a][b] for a in range(27)) == 0 for row in invariants for b in range(27))
        assert sum(bracket[a][a] for a in range(27)) <= K / N
        tested.append(N)
    check("drift-and-noise-normalization", True,
          f"N={tested}: generator drift=F, density bracket=R(f)/N, sqrt(N) bracket=R(f), all five invariant rows annihilate noise")

    # Polynomial certificates used for the LLN constants, in four nonnegative
    # variables: (a+b+c+d)^2 - 4(ab+cd)=(a-b)^2+(c-d)^2+2(a+b)(c+d).
    polynomial = defaultdict(int)
    for i in range(4):
        for j in range(4):
            polynomial[tuple(sorted((i, j)))] += 1
    polynomial[(0, 1)] -= 3
    polynomial[(2, 3)] -= 4
    rhs = defaultdict(int)
    for i, j in ((0, 1), (2, 3)):
        rhs[(i, i)] += 1
        rhs[(j, j)] += 1
        rhs[(i, j)] -= 2
    for i in (0, 1):
        for j in (2, 3):
            rhs[(i, j)] += 2
    check("LLN-constant-certificate", dict(polynomial) == dict(rhs) and all(dot(nu, nu) == 4 for nu in columns),
          "ab+cd<=1/4 on the four-coordinate simplex; trace R<=K and Lipschitz bound ||F(x)-F(y)||_2<=4K||x-y||_2 as proved in note")
    print("ANALYTIC: accepted external persistence + entropy argument proves convergence; finite enumeration does not prove the external theorem.")
    print("ANALYTIC: Doob/Gronwall gives E sup_[0,T] ||fN-f||_2^2 <= 2 exp(8KT) [E||fN(0)-f0||_2^2 + 4KT/N].")
    print("SCOPE: fixed D3Q27, supplied rates, finite particle system; no continuum, native-record, physical-clock or empirical identification.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        FAIL += 1
        print(f"FAIL exception: {type(exc).__name__}: {exc}", flush=True)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}", flush=True)
    sys.exit(1 if FAIL else 0)
