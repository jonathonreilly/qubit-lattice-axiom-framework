#!/usr/bin/env python3
"""Exact bounded checks for RECOVERY_CLUSTER_ASTRA.md; standard library only.

This does not certify Yang--Mills premises or any limiting statement.
Polynomial keys are (t degree, z0 degree, z1 degree, z2 degree, z3 degree).
"""
from fractions import Fraction as F
from itertools import product, permutations
from collections import defaultdict
import hashlib
import json
from pathlib import Path

ZERO = (0, 0, 0, 0, 0)
ONE = {ZERO: F(1)}


def add(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, F(0)) + v
        if out[k] == 0:
            del out[k]
    return out


def scale(p, a):
    return {k: v * a for k, v in p.items() if v * a}


def mul(p, q, cap=None):
    out = defaultdict(F)
    for k, v in p.items():
        for l, w in q.items():
            kl = tuple(x + y for x, y in zip(k, l))
            if cap is None or kl[0] <= cap:
                out[kl] += v * w
    return {k: v for k, v in out.items() if v}


def formal_log(p, cap):
    x = add(p, scale(ONE, -1))
    assert x.get(ZERO, 0) == 0
    out, power = {}, ONE
    for n in range(1, cap + 1):
        power = mul(power, x, cap)
        out = add(out, scale(power, F((-1) ** (n + 1), n)))
    return out


def connected(support):
    # Fixed path 0--1--2--3; singleton and nonempty interval are connected.
    return bool(support) and max(support) - min(support) + 1 == len(support)


def overlap_connected(indices, atoms):
    todo = set(indices)
    seen = {todo.pop()}
    while todo:
        nxt = {j for j in todo if any(atoms[i]['support'] & atoms[j]['support']
                                      for i in seen)}
        if not nxt:
            return False
        seen.update(nxt)
        todo.difference_update(nxt)
    return True


atoms = []
for x in range(4):
    key = [1, 0, 0, 0, 0]
    key[1 + x] = 1
    atoms.append(dict(support=frozenset([x]), parity=1 << x,
                      coefficient=F(1, 101 + x), key=tuple(key)))
for j, (x, y) in enumerate([(0, 1), (1, 2), (2, 3), (0, 3)]):
    atoms.append(dict(support=frozenset(range(x, y + 1)),
                      parity=(1 << x) ^ (1 << y),
                      coefficient=F(1, 105 + j), key=(1, 0, 0, 0, 0)))


def direct_partition(flip_long=False):
    # Implementation 1: sum products over all actual spin configurations.
    out = {}
    for spins in product([-1, 1], repeat=4):
        p = ONE
        for i, atom in enumerate(atoms):
            sign = 1
            for x in range(4):
                if atom['parity'] & (1 << x):
                    sign *= spins[x]
            if flip_long and i == 7:
                sign *= -1
            p = mul(p, add(ONE, {atom['key']: sign * atom['coefficient']}))
        out = add(out, scale(p, F(1, 16)))
    return out


def connected_activities():
    # Implementation 2: character parity, with no spin configurations.
    activities = {}
    collections = 0
    surviving = 0
    for mask in range(1, 1 << len(atoms)):
        ids = [i for i in range(len(atoms)) if mask & (1 << i)]
        if not overlap_connected(ids, atoms):
            continue
        collections += 1
        parity, coeff = 0, F(1)
        key = ZERO
        support = frozenset()
        for i in ids:
            atom = atoms[i]
            parity ^= atom['parity']
            coeff *= atom['coefficient']
            key = tuple(x + y for x, y in zip(key, atom['key']))
            support |= atom['support']
        if parity:
            continue
        surviving += 1
        activities[support] = add(activities.get(support, {}), {key: coeff})
    return activities, collections, surviving


def gas_partition(activities):
    # Enumerate mutually disjoint polymers, independent of interaction labels.
    states = {frozenset(): ONE}
    for support, activity in sorted(activities.items(), key=lambda p: tuple(p[0])):
        out = dict(states)
        for used, p in states.items():
            if not used & support:
                target = used | support
                out[target] = add(out.get(target, {}), mul(p, activity))
        states = out
    total = {}
    for p in states.values():
        total = add(total, p)
    return total


def log_activities_to_six(activities):
    # Minimum degree is three: only 1- and 2-polymer clusters enter t^6.
    assert all(k[0] >= 3 for p in activities.values() for k in p)
    out = {s: {k: v for k, v in p.items() if k[0] <= 6}
           for s, p in activities.items()}
    for s, p in activities.items():
        for t, q in activities.items():
            if s & t:
                u = s | t
                out[u] = add(out.get(u, {}), scale(mul(p, q, 6), F(-1, 2)))
    return out


def inverse(matrix):
    n = len(matrix)
    a = [row[:] + [F(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for c in range(n):
        pivot = next(i for i in range(c, n) if a[i][c])
        a[c], a[pivot] = a[pivot], a[c]
        v = a[c][c]
        a[c] = [x / v for x in a[c]]
        for i in range(n):
            if i != c:
                v = a[i][c]
                a[i] = [x - v * y for x, y in zip(a[i], a[c])]
    return [row[n:] for row in a]


def determinant_polynomial(matrix):
    n = len(matrix)
    out = {}
    for perm in permutations(range(n)):
        sign = (-1) ** sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = ONE
        for i in range(n):
            term = mul(term, matrix[i][perm[i]])
        out = add(out, scale(term, sign))
    return out


checks = {}
direct = direct_partition()
activities, collections, surviving = connected_activities()
gas = gas_partition(activities)
checks['direct_partition_equals_connected_gas'] = direct == gas
direct_log = formal_log(direct, 6)
local_logs = log_activities_to_six(activities)
cluster_log = {}
for p in local_logs.values():
    cluster_log = add(cluster_log, p)
checks['direct_log_equals_connected_log_to_degree_6'] = direct_log == cluster_log
checks['all_log_supports_connected'] = all(connected(s) for s in local_logs)
checks['all_log_source_dependencies_inside_support'] = all(
    all(k[1 + x] == 0 or x in s for x in range(4))
    for s, p in local_logs.items() for k in p)
probe_key = (3, 1, 0, 0, 1)
probe_expected = F(1, 101 * 104 * 108)
checks['long_jump_source_coefficient'] = direct_log.get(probe_key) == probe_expected
flipped_log = formal_log(direct_partition(flip_long=True), 6)
checks['sign_corruption_detected'] = (
    flipped_log != direct_log and flipped_log.get(probe_key) == -probe_expected)

# Uniform operator example: use 729 as the proved strict upper bound on e^6.
eps = F(1, 16384)
upper_atom = 729 * eps
max_row = max_col = max_incidence = F(0)
graph_count = 0
for n in range(1, 9):
    for mask in range(1 << n):
        vertices = {i for i in range(n) if mask & (1 << i)}
        terms = [(i, j, frozenset([i, j]), upper_atom)
                 for i in vertices for j in vertices if abs(i - j) == 1]
        for v in vertices:
            max_row = max(max_row, sum((w for x, y, s, w in terms if x == v), F(0)))
            max_col = max(max_col, sum((w for x, y, s, w in terms if y == v), F(0)))
            max_incidence = max(max_incidence, sum((w for x, y, s, w in terms if v in s), F(0)))
        graph_count += 1
checks['finite_operator_majorants'] = (
    max_row == max_col == F(729, 8192) and max_incidence == F(729, 4096)
    and max_row < F(1, 8) and max_incidence < F(1, 4))
checks['analytic_example_rational_margins'] = (
    F(27) + F(8, 7) - 1 < 28
    and F(27) + F(1, 8) * F(8, 7) ** 2 < 28
    and F(27, 1024) * (F(4, 3) + F(1, 4) * F(16, 9)) == F(3, 64)
    and F(3, 64) < F(1, 4))

# Full determinant at zero interaction: independent permutation and inverse paths.
k0 = [[F(1), -eps / 2, F(0)],
      [-eps / 2, F(1), -eps / 2],
      [F(0), -eps / 2, F(1)]]
kp = [[F(0), -eps / 2, F(0)],
      [-eps / 2, F(0), F(0)],
      [F(0), F(0), F(0)]]
tk = (1, 0, 0, 0, 0)
kpoly = [[add({ZERO: k0[i][j]} if k0[i][j] else {},
               {tk: kp[i][j]} if kp[i][j] else {}) for j in range(3)] for i in range(3)]
det = determinant_polynomial(kpoly)
det_derivative = -det[tk] / (2 * det[ZERO])
kinv = inverse(k0)
trace_derivative = -sum((kinv[i][j] * kp[j][i] for i in range(3)
                         for j in range(3)), F(0)) / 2
checks['full_logdet_two_exact_paths'] = (
    det_derivative == trace_derivative == F(1, 1073741822))
checks['dropped_determinant_detected_at_H_zero'] = det_derivative != 0

# Old locality controls: explicit dependence data, not semantic code inference.
def valid_label(support, w_reads, z_reads):
    return connected(support) and set(w_reads) <= support and set(z_reads) <= support

checks['remote_parameter_wrong_label_detected'] = not valid_label({0}, {0}, {0, 3})
checks['remote_parameter_connector_label_valid'] = valid_label({0, 1, 2, 3}, {0}, {0, 3})
checks['long_jump_endpoint_only_label_detected'] = not valid_label({0, 3}, {0, 3}, {0, 3})
checks['long_jump_connector_label_valid'] = valid_label({0, 1, 2, 3}, {0, 3}, {0, 3})
remote = {(1, 1, 0, 0, 1): F(-1)}
remote_exp, power = ONE, ONE
factorial = 1
for n in range(1, 7):
    power = mul(power, remote, 6)
    factorial *= n
    remote_exp = add(remote_exp, scale(power, F(1, factorial)))
checks['remote_log_coefficient_reproduced'] = formal_log(remote_exp, 6) == remote

report = {
    'scope': 'Exact finite algebraic checks; no Yang--Mills or limiting certificate.',
    'arithmetic': 'Python standard-library Fraction, no floating-point calculations.',
    'checks': checks,
    'all_checks_pass': all(checks.values()),
    'spin_check': {
        'spin_configurations': 16,
        'interaction_factors': 8,
        'nonempty_factor_subsets': 255,
        'overlap_connected_subsets': collections,
        'nonzero_connected_subsets_after_parity': surviving,
        'gas_supports': len(activities),
        'partition_nonzero_monomials': len(direct),
        'log_nonzero_monomials_through_t6': len(direct_log),
        'maximum_polymer_count_in_log_check': 2,
        'long_source_log_coefficient_t3': str(direct_log.get(probe_key)),
        'sign_corruption_coefficient_t3': str(flipped_log.get(probe_key))},
    'operator_check': {
        'induced_path_graphs_checked': graph_count,
        'path_vertex_counts': [1, 8],
        'weighted_entry_upper': str(upper_atom),
        'maximum_row': str(max_row), 'maximum_column': str(max_col),
        'maximum_support_incidence': str(max_incidence),
        'h_local_proved_upper': '3/64',
        'universal_scope_from_proof': 'maximum degree two; finite scan is not the proof'},
    'normalizer_check': {
        'nonlinear_interaction_H': 0,
        'logdet_derivative_from_permutation_determinant': str(det_derivative),
        'logdet_derivative_from_gauss_jordan_inverse_trace': str(trace_derivative),
        'incorrect_omitted_factor_prediction': '0'},
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
print(json.dumps(report, indent=2, sort_keys=True))
if not report['all_checks_pass']:
    raise SystemExit(1)
