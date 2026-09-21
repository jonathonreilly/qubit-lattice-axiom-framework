#!/usr/bin/env python3
"""Separate exact controls for the tagged proof and clock-budget scope.

No primary runner is imported. Transition rates below use local edge-factor
cancellation and explicitly track a distinguished immutable record.
"""
from collections import defaultdict, deque
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import platform

import sympy as sp

HERE = Path(__file__).resolve().parent


def tagged_model(n, edges, W, epsilon, kappa):
    neighbors = [set() for _ in range(n)]
    for x, y in edges:
        neighbors[x].add(y)
        neighbors[y].add(x)
    states = []
    for tag in range(n):
        others = [x for x in range(n) if x != tag]
        for values in product(range(-1, 6), repeat=n-1):
            state = [0]*n  # distinguished record has content zero
            for x, value in zip(others, values):
                state[x] = value
            states.append((tuple(state), tag))
    transitions = {}
    for key in states:
        state, tag = key
        rows = []
        for x in range(n):
            if state[x] != -1:
                continue
            for content in range(6):
                rate = epsilon
                for y in neighbors[x]:
                    if state[y] != -1:
                        rate *= W[content][state[y]]
                target = list(state)
                target[x] = content
                rows.append(((tuple(target), tag), rate, False))
        for x, y in edges:
            if (state[x] == -1) == (state[y] == -1):
                continue
            source, destination = (y, x) if state[x] == -1 else (x, y)
            content = state[source]
            old_factor = F(1)
            new_factor = F(1)
            for z in neighbors[source]-{destination}:
                if state[z] != -1:
                    old_factor *= W[content][state[z]]
            for z in neighbors[destination]-{source}:
                if state[z] != -1:
                    new_factor *= W[content][state[z]]
            rate = kappa*new_factor/(old_factor+new_factor)
            target = list(state)
            target[source], target[destination] = target[destination], target[source]
            is_tag = source == tag
            rows.append(((tuple(target), destination if is_tag else tag), rate, is_tag))
        transitions[key] = rows
    return states, transitions


def ordered_groups(states):
    groups = defaultdict(list)
    for key in states:
        state, tag = key
        others = tuple(sorted(content for x, content in enumerate(state)
                              if x != tag and content != -1))
        if -1 in state:
            groups[others].append(key)
    return sorted(groups.values(), key=lambda group: sum(a != -1 for a in group[0][0]), reverse=True)


def exact_tag_mean(states, transitions):
    values = {key: sp.Integer(0) for key in states if -1 not in key[0]}
    for group in ordered_groups(states):
        index = {key: i for i, key in enumerate(group)}
        matrix = sp.zeros(len(group))
        rhs = sp.zeros(len(group), 1)
        for key, i in index.items():
            for target, rate, is_tag in transitions[key]:
                matrix[i, i] += rate
                if target in index:
                    matrix[i, index[target]] -= rate
                else:
                    rhs[i] += rate*values[target]
                if is_tag:
                    rhs[i] += rate
        answer = matrix.inv()*rhs
        for key, i in index.items():
            values[key] = answer[i]
    for key in states:
        residual = sum(rate*(values[target]-values[key]+int(is_tag))
                       for target, rate, is_tag in transitions[key])
        assert residual == 0
        assert values[key] >= 0
    return values


def exact_tag_tails(states, transitions, count):
    previous = {key: sp.Integer(1) for key in states}
    tails = []
    for m in range(1, count+1):
        current = {key: sp.Integer(0) for key in states if -1 not in key[0]}
        for group in ordered_groups(states):
            index = {key: i for i, key in enumerate(group)}
            matrix = sp.zeros(len(group))
            rhs = sp.zeros(len(group), 1)
            for key, i in index.items():
                for target, rate, is_tag in transitions[key]:
                    matrix[i, i] += rate
                    if is_tag:
                        rhs[i] += rate*previous[target]
                    elif target in index:
                        matrix[i, index[target]] -= rate
                    else:
                        rhs[i] += rate*current[target]
            answer = matrix.inv()*rhs
            for key, i in index.items():
                current[key] = answer[i]
        assert all(0 <= current[key] <= previous[key] <= 1 for key in states)
        tails.append(current)
        previous = current
    return tails


def tagged_checks():
    epsilon, kappa = F(2, 3), F(5, 7)
    flat = [[F(1) for _ in range(6)] for _ in range(6)]
    two, rates = tagged_model(2, [(0, 1)], flat, epsilon, kappa)
    mean = exact_tag_mean(two, rates)
    tails = exact_tag_tails(two, rates, 6)
    q = kappa/(12*epsilon+kappa)
    for tag in [0, 1]:
        state = [-1, -1]
        state[tag] = 0
        key = (tuple(state), tag)
        assert mean[key] == kappa/(12*epsilon)
        for m in range(1, 7):
            assert tails[m-1][key] == q**m

    # Six contents, nonconstant symmetric weights, no row-sum condition.
    weights = [[F(3+(a+b) % 4, 4) for b in range(6)] for a in range(6)]
    states, rates = tagged_model(3, [(0, 1), (1, 2)], weights, epsilon, kappa)
    means = exact_tag_mean(states, rates)
    tails = exact_tag_tails(states, rates, 4)
    z = 2
    lam = z*kappa
    ell = min(F(1), min(x for row in weights for x in row))
    alpha = 6*epsilon*ell**z
    gamma = alpha/2
    A = 1+4*lam/alpha
    c = sp.Rational(lam)*(sp.E-1)+sp.Rational(gamma)
    integrated_bound = sp.Rational(lam/gamma)+sp.Rational(lam*A)*(3/sp.Rational(gamma)+2*c/sp.Rational(gamma)**2)
    for key in states:
        tag_intensity = sum(rate for _, rate, is_tag in rates[key] if is_tag)
        assert tag_intensity <= lam
        assert means[key] <= integrated_bound
    chosen = [((-1, 0, -1), 1), ((0, -1, 1), 0), ((0, 2, -1), 0)]
    examples = []
    for key in chosen:
        examples.append({'state': key[0], 'tag_position': key[1],
                         'mean_lifetime_hops_exact': str(means[key]),
                         'mean_lifetime_hops': float(means[key]),
                         'tail_probabilities_m1_to_m4': [str(tail[key]) for tail in tails]})
    return {'two_site_geometric_ratio': str(q), 'two_site_mean': str(kappa/(12*epsilon)),
            'two_site_exact_tail_thresholds': 6,
            'interacting_path_total_states': len(states),
            'interacting_path_transient_states': sum(-1 in key[0] for key in states),
            'maximum_exact_mean': str(max(means.values())),
            'uniform_tag_mean_bound': float(integrated_bound),
            'scope': 'Finite induced path control for local rates and tagged counts; not a proof of the infinite tagged estimate.',
            'examples': examples}


def geometry_and_tail_algebra():
    counts = []
    for d in [1, 2, 3]:
        for integer_travel_budget in range(5):
            radius = integer_travel_budget+1
            ball = sum(sum(abs(x) for x in point) <= radius
                       for point in product(range(-radius, radius+1), repeat=d))
            box = (2*integer_travel_budget+3)**d
            assert ball <= box
            counts.append({'dimension': d, 'travel_budget': integer_travel_budget,
                           'candidate_destination_count': ball, 'box_bound': box})
    t, T, gamma, c = sp.symbols('t T gamma c', positive=True)
    checks = 0
    for d in [1, 2, 3]:
        # Differentiate an explicit proposed tail integral rather than
        # integrate the same polynomial twice.
        primitive = sp.exp(-gamma*T)*sum(
            sp.binomial(d,k)*3**(d-k)*(2*c)**k*sp.factorial(k)
            *sum((gamma*T)**i/sp.factorial(i) for i in range(k+1))/gamma**(k+1)
            for k in range(d+1))
        assert sp.simplify(sp.diff(primitive,T)+(2*c*T+3)**d*sp.exp(-gamma*T)) == 0
        assert sp.limit(primitive,T,sp.oo) == 0
        checks += 1
    return {'candidate_ball_counts': counts, 'tail_antiderivative_checks': checks}


def time_varying_budget():
    # Uniformly random vacancy on a three-cycle: a TI initial law with v0=1/3.
    # epsilon(t)=a for t<1, zero afterwards. There is at most one birth.
    a, kappa = sp.symbols('a kappa', positive=True)
    Q = sp.Matrix([[-kappa, kappa/2, kappa/2],
                   [kappa/2, -kappa, kappa/2],
                   [kappa/2, kappa/2, -kappa]])
    one = sp.ones(3,1)
    killed = Q-6*a*sp.eye(3)
    assert Q*one == sp.zeros(3,1)
    assert killed*one == -6*a*one
    survival_at_switch = sp.exp(-6*a)
    vacancy_limit = survival_at_switch/3
    mean_births_per_site = (1-survival_at_switch)/3
    assert sp.simplify(mean_births_per_site+vacancy_limit-sp.Rational(1,3)) == 0
    # Conditional on no birth by t=1, motion after the cutoff is a finite
    # irreducible chain on permutations of two permanent tags and one vacancy.
    states = list(product(range(3),repeat=3))
    states = [s for s in states if set(s)=={0,1,2}]  # 0 vacancy, 1/2 tags
    seen = {states[0]}
    todo = deque(seen)
    while todo:
        s = todo.popleft()
        vacant = s.index(0)
        for x in range(3):
            if x == vacant:
                continue
            target = list(s)
            target[vacant],target[x] = target[x],target[vacant]
            target = tuple(target)
            if target not in seen:
                seen.add(target);todo.append(target)
    assert set(states) == seen
    return {'clock': 'epsilon(t)=a on [0,1), zero thereafter; fixed kappa>0',
            'initial_vacancy_density': '1/3',
            'limiting_vacancy_density': str(vacancy_limit),
            'mean_births_per_site': str(mean_births_per_site),
            'probability_of_persistent_vacancy_motion': str(survival_at_switch),
            'irreducible_two_tag_vacancy_configurations': len(seen)}


def degree_counterexample():
    # Simple two-vertex periodic quotient, one undirected edge.
    # Exact reward calculation for departures from vertex 0, empty start.
    epsilon, kappa = sp.Integer(1), sp.Integer(1)
    b,h = 6*epsilon,kappa/2
    matrix = sp.Matrix([[2*b,-b,-b],[0,b+h,-h],[0,-h,b+h]])
    reward = sp.Matrix([0,h,0])  # empty, record at 0, record at 1
    answer = matrix.inv()*reward
    actual = answer[0]
    actual_degree_formula = kappa/(12*epsilon)*(1-sp.Rational(1,2))
    z_bound_formula = 2*kappa/(12*epsilon)*(1-sp.Rational(1,2))
    assert actual == actual_degree_formula == sp.Rational(1,24)
    assert z_bound_formula == sp.Rational(1,12) != actual
    return {'actual_degree': 1, 'degree_bound_z_2d': 2,
            'exact_expected_departures_per_site': str(actual),
            'formula_using_degree_bound_as_exact_degree': str(z_bound_formula),
            'scope': 'Only a finding if simple side-two tori are included; all upper bounds remain valid.'}


def thin_torus_limit_counterexample():
    # W=1, empty start: independent uniform terminal contents at distinct sites.
    # A growing 3-by-L torus still identifies 0 and 3*e1 for every L.
    chi = [1,-1,0,0,0,0]
    mean = sum(F(value,6) for value in chi)
    aliased_covariance = sum(F(value*value,6) for value in chi)-mean*mean
    distinct_covariance = sum(F(x*y,36) for x in chi for y in chi)-mean*mean
    assert (0 % 3,0) == (3 % 3,0)
    assert aliased_covariance == F(1,3)
    assert distinct_covariance == 0
    return {'growing_tori': '3-by-L as L tends to infinity',
            'fixed_Z2_observation_sites': [[0,0],[3,0]],
            'torus_quotient_covariance': str(aliased_covariance),
            'Z2_covariance': str(distinct_covariance),
            'scope': 'Volume growth alone does not give the stated Z^d local limit; all periods must diverge.'}


def main():
    result = {'tagged_controls': tagged_checks(),
              'geometry_and_tail_algebra': geometry_and_tail_algebra(),
              'time_varying_budget': time_varying_budget(),
              'torus_degree_scope_counterexample': degree_counterexample(),
              'thin_torus_limit_counterexample': thin_torus_limit_counterexample(),
              'versions': {'python': platform.python_version(),'sympy':sp.__version__},
              'all_checks_passed': True}
    text = json.dumps(result,indent=2)+'\n'
    (HERE/'INDEPENDENT_RESULTS.json').write_text(text)
    print(text,end='')


if __name__ == '__main__':
    main()
