#!/usr/bin/env python3
"""Exact independent controls for the terminal-correlation argument.

No primary campaign files are imported. Writes RESULTS.json beside this file.
The infinite-volume result is proved in REPORT.md, not inferred from this suite.
"""
from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import ceil, e
from pathlib import Path
import json
import platform

HERE = Path(__file__).resolve().parent
PREVIOUS = HERE.parent / 'independent_local_activity'


def menu(uniform=False):
    return [[F(1) if uniform else F(3, 2) if a == b else F(1, 2) if (a ^ 1) == b else F(1)
             for b in range(6)] for a in range(6)]


def graph_model(n, edges, W):
    states = list(product(range(-1, 6), repeat=n))
    neighbors = [{y if x == i else x for x, y in edges if i in (x, y)} for i in range(n)]
    weights = {}
    for s in states:
        weight = F(1)
        for x, y in edges:
            if s[x] != -1 and s[y] != -1:
                weight *= W[s[x]][s[y]]
        weights[s] = weight
    births, hops, local_births = {}, {}, {}
    for s in states:
        b, h = {}, {}
        bx = [F(0)]*n
        for x in range(n):
            if s[x] != -1:
                continue
            for a in range(6):
                rate = F(1)
                for y in neighbors[x]:
                    if s[y] != -1:
                        rate *= W[a][s[y]]
                target = list(s)
                target[x] = a
                b[tuple(target)] = rate
                bx[x] += rate
        for x, y in edges:
            if (s[x] == -1) == (s[y] == -1):
                continue
            target = list(s)
            target[x], target[y] = target[y], target[x]
            target = tuple(target)
            h[target] = weights[target]/(weights[s]+weights[target])
        births[s], hops[s], local_births[s] = b, h, bx
    return states, neighbors, births, hops, local_births


def solve(matrix, rhs):
    n = len(matrix)
    augmented = [list(matrix[i])+list(rhs[i]) for i in range(n)]
    outputs = len(rhs[0])
    for col in range(n):
        pivot = next(i for i in range(col, n) if augmented[i][col])
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        denominator = augmented[col][col]
        augmented[col] = [v/denominator for v in augmented[col]]
        for row in range(n):
            if row == col or not augmented[row][col]:
                continue
            multiplier = augmented[row][col]
            augmented[row] = [a-multiplier*b for a, b in zip(augmented[row], augmented[col])]
    return [row[n:n+outputs] for row in augmented]


def terminal_values(n, edges, W, epsilon, kappa):
    states, neighbors, births, hops, local_births = graph_model(n, edges, W)
    chi = (1, -1, 0, 0, 0, 0)
    values = {}
    for s in states:
        if -1 not in s:
            a, b = F(chi[s[0]]), F(chi[s[-1]])
            values[s] = [a, b, a*b]
    largest = 0
    for number in reversed(range(n)):
        groups = defaultdict(list)
        for s in states:
            content = tuple(sorted(a for a in s if a != -1))
            if len(content) == number:
                groups[content].append(s)
        for content, group in groups.items():
            index = {s: i for i, s in enumerate(group)}
            largest = max(largest, len(group))
            matrix = [[F(0) for _ in group] for _ in group]
            rhs = [[F(0)]*3 for _ in group]
            for i, s in enumerate(group):
                matrix[i][i] = epsilon*sum(births[s].values())+kappa*sum(hops[s].values())
                for t, rate in hops[s].items():
                    matrix[i][index[t]] -= kappa*rate
                for t, rate in births[s].items():
                    for j in range(3):
                        rhs[i][j] += epsilon*rate*values[t][j]
            answer = solve(matrix, rhs)
            for s, v in zip(group, answer):
                values[s] = v
    # Check each harmonic equation against the actual independent transitions.
    for s in states:
        if -1 not in s:
            continue
        for j in range(3):
            residual = sum(epsilon*r*(values[t][j]-values[s][j]) for t, r in births[s].items())
            residual += sum(kappa*r*(values[t][j]-values[s][j]) for t, r in hops[s].items())
            assert residual == 0
    return values, {'states': len(states), 'maximum_linear_system': largest}


def absorb_checks():
    edges = [(0, 1), (1, 2)]
    records = []
    for uniform, epsilon, kappa in [(False, F(1), F(0)), (False, F(1), F(1)),
                                    (False, F(1), F(10)), (False, F(1, 7), F(1, 7)),
                                    (True, F(1), F(1))]:
        values, metadata = terminal_values(3, edges, menu(uniform), epsilon, kappa)
        means = values[(-1, -1, -1)]
        covariance = means[2]-means[0]*means[1]
        assert means[0] == means[1] == 0
        if uniform:
            assert covariance == 0
            # Homogeneous product initial law: vacancy 2/3, +e1 record 1/3.
            # For W=1 the terminal product marginal has E chi=1/3.
            expected = [F(0)]*3
            for s in product([-1, 0], repeat=3):
                p = F(1)
                for a in s:
                    p *= F(2, 3) if a == -1 else F(1, 3)
                for j in range(3):
                    expected[j] += p*values[s][j]
            assert expected == [F(1, 3), F(1, 3), F(1, 9)]
        else:
            assert covariance > 0
        records.append({'uniform_W': uniform, 'epsilon': str(epsilon), 'kappa': str(kappa),
                        'empty_start_endpoint_covariance': str(covariance),
                        'covariance_decimal': float(covariance), **metadata})
    assert records[1]['empty_start_endpoint_covariance'] == records[3]['empty_start_endpoint_covariance']
    return records


def vacancy_exponential_drift():
    epsilon, kappa = F(1, 7), F(2, 3)
    W = menu()
    checks = 0
    strictest_gap = None
    for n, edges in [(3, [(0, 1), (1, 2)]), (4, [(0, 1), (1, 2), (2, 3), (0, 3)])]:
        states, neighbors, births, hops, bx = graph_model(n, edges, W)
        z = 2
        alpha = 6*epsilon*F(1, 2)**z
        exponential_increment = alpha/(2*z*kappa)  # e^delta - 1
        for s in states:
            for x in range(n):
                if s[x] != -1:
                    continue
                hop_rate = kappa*sum(rate for target, rate in hops[s].items() if target[x] != -1)
                killing_rate = epsilon*bx[s][x]
                drift = hop_rate*exponential_increment-killing_rate
                assert drift <= -alpha/2
                gap = -alpha/2-drift
                strictest_gap = gap if strictest_gap is None else min(strictest_gap, gap)
                checks += 1
    return {'vacancy_label_drift_checks': checks, 'minimum_margin': str(strictest_gap),
            'epsilon': str(epsilon), 'kappa': str(kappa)}


def dependence_constants():
    # Actual acceptance at 0 reads content at distance two along 0--1--2.
    equal = F(3, 2)/(1+F(3, 2))
    antipodal = F(1, 2)/(1+F(1, 2))
    assert equal == F(3, 5) and antipodal == F(1, 3) and equal != antipodal
    for distance in range(1, 1001):
        radius = (distance-1)//2
        depth = radius//2+1
        assert 2*radius < distance and depth == ceil(distance/4)
    epsilon, kappa, d = F(1), F(1), 1
    z = 2*d
    alpha, beta = 6*epsilon*F(1, 2)**z, 6*epsilon*F(3, 2)**z
    A = (z+1)*(beta+2*z*kappa)
    Q = 1+2*z*kappa/alpha
    return {'distance_two_hop_acceptances': [str(equal), str(antipodal)],
            'radius_depth_integer_checks': 1000,
            'example': {'d': d, 'epsilon': str(epsilon), 'kappa': str(kappa),
                        'alpha': str(alpha), 'beta': str(beta), 'A': str(A),
                        'empty_start_Q': str(Q),
                        'exponential_length_upper_bound_8eA_over_alpha': float(8*e*A/alpha)}}


def correlated_initial_counterexample():
    states, neighbors, births, hops, bx = graph_model(2, [(0, 1)], menu())
    plus, minus = (0, 0), (1, 1)
    assert not births[plus] and not hops[plus]
    assert not births[minus] and not hops[minus]
    marginal = F(1, 2)*1+F(1, 2)*(-1)
    product_moment = F(1, 2)*1+F(1, 2)*1
    assert marginal == 0 and product_moment-marginal*marginal == 1
    return {'law': 'probability 1/2 all +e1, probability 1/2 all -e1',
            'initial_and_final_vacancy_density': 0,
            'successful_event_count': 0, 'connected_correlation_at_every_distance': 1}


def main():
    seal = json.loads((PREVIOUS/'SEAL.json').read_text())
    assert sha256((PREVIOUS/'SEAL.json').read_bytes()).hexdigest() == 'e5a93c93d7a74d69713108035d53e78692bf6cd7bd2c4f87ca41bf281dfa0eb4'
    for name, expected in seal['artifacts_sha256'].items():
        assert sha256((PREVIOUS/name).read_bytes()).hexdigest() == expected
    output = {'prior_local_activity_evidence_reverified': True,
              'exact_terminal_absorption_controls': absorb_checks(),
              'vacancy_exponential_drift': vacancy_exponential_drift(),
              'dependence_constants': dependence_constants(),
              'nonproduct_counterexample': correlated_initial_counterexample(),
              'python': platform.python_version(), 'all_checks_passed': True}
    text = json.dumps(output, indent=2)+'\n'
    (HERE/'RESULTS.json').write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
