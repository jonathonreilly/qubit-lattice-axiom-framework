#!/usr/bin/env python3
"""Fresh PRE42 exact controls. No imports of previous or author programs.
Read no files; stdout is the complete JSON evidence. All science uses integers
and fractions, including complex numbers represented by pairs of rationals.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
import json


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def scale(a, x):
    return (a * x[0], a * x[1])


def conj(x):
    return (x[0], -x[1])


def mul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def norm2(x):
    return x[0] * x[0] + x[1] * x[1]


def csum(xs):
    out = (0, 0)
    for x in xs:
        out = add(out, x)
    return out


def exact(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, dict):
        return {str(k): exact(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [exact(v) for v in x]
    return x


def graph(name, vertices, aset, edges, coordinates=None, side=None):
    A = tuple(sorted(aset))
    B = tuple(v for v in vertices if v not in aset)
    oriented = tuple(sorted((u, v) if u in aset else (v, u) for u, v in edges))
    assert len(set(oriented)) == len(oriented)
    assert all(a in A and b in B for a, b in oriented)
    neighbors = {a: tuple(b for u, b in oriented if u == a) for a in A}
    return dict(name=name, vertices=tuple(vertices), A=A, B=B, edges=oriented,
                neighbors=neighbors, edge_index={e: i for i, e in enumerate(oriented)},
                coordinates=coordinates, side=side)


def cubic(side):
    coordinates = tuple(product(range(side), repeat=3))
    A = {i for i, x in enumerate(coordinates) if sum(x) % 2 == 0}
    # Unordered-pair metric construction, not the neighbor-list formula tested below.
    edges = []
    for u, v in combinations(range(len(coordinates)), 2):
        distances = [min(abs(x - y), side - abs(x - y))
                     for x, y in zip(coordinates[u], coordinates[v])]
        if sum(distances) == 1:
            edges.append((u, v))
    return graph('cubic_L' + str(side), range(len(coordinates)), A, edges,
                 coordinates, side)


def cycle_flow(g, walk):
    out = [0] * len(g['edges'])
    assert walk[0] == walk[-1]
    for u, v in zip(walk, walk[1:]):
        edge = (u, v) if u in g['A'] else (v, u)
        out[g['edge_index'][edge]] += 1 if u in g['A'] else -1
    return tuple(out)


def fluxes(g):
    zero = (0,) * len(g['edges'])
    if g['name'] == 'star':
        return (zero,)
    if g['name'] == 'irregular':
        c = cycle_flow(g, (0, 2, 1, 3, 0))
        return (zero, c, tuple(-2 * e for e in c))
    ix = {x: i for i, x in enumerate(g['coordinates'])}
    xy = cycle_flow(g, tuple(ix[x] for x in
                            ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 0))))
    if g['side'] == 2:
        other = cycle_flow(g, tuple(ix[x] for x in
                                   ((0, 0, 0), (1, 0, 0), (1, 0, 1), (0, 0, 1), (0, 0, 0))))
    else:
        other = cycle_flow(g, tuple(ix[(x, 0, 0)] for x in range(g['side'])) + (ix[(0, 0, 0)],))
    return (zero, tuple(2 * e for e in xy), tuple(-u + 3 * v for u, v in zip(xy, other)))


def divergence(g, E):
    out = [0] * len(g['vertices'])
    for (a, b), e in zip(g['edges'], E):
        out[a] += e
        out[b] -= e
    return tuple(out)


def check_gauss(g, q, E):
    assert divergence(g, E) == tuple(q[x] - (x in g['A']) for x in g['vertices'])
    assert all(c in (-1, 0, 1) for c in q)


def old_hops(g, q, E, a):
    """Literal F_a primitive; record old target but retain its coherent amplitude."""
    for c in g['neighbors'][a]:
        if q[a] and q[c] == 0:
            q2, E2 = list(q), list(E)
            charge = q[a]
            q2[c], q2[a] = charge, 0
            E2[g['edge_index'][(a, c)]] -= charge
            check_gauss(g, tuple(q2), tuple(E2))
            yield c, tuple(q2), tuple(E2)


def create(g, q, E, a, b, sigma):
    """Literal j_(ab,sigma), including its vacancy tests."""
    if q[a] != 0 or q[b] != 0:
        return None
    q2, E2 = list(q), list(E)
    q2[a], q2[b] = sigma, -sigma
    E2[g['edge_index'][(a, b)]] += sigma
    check_gauss(g, tuple(q2), tuple(E2))
    return tuple(q2), tuple(E2)


def outputs(g, q0, E, a, b, sigma):
    result = []
    for c, q1, E1 in old_hops(g, q0, E, a):
        new = create(g, q1, E1, a, b, sigma)
        if new is not None:
            q, electric = new
            assert c != b
            assert sum(abs(x) for x in q) == len(g['A']) + 2
            assert sum(q) == len(g['A'])
            assert all(q[x] != 0 for x in g['A'])
            relative = tuple(q[x] - q0[x] for x in g['vertices'])
            predicted = [0] * len(q)
            predicted[a], predicted[b], predicted[c] = sigma - 1, -sigma, 1
            assert relative == tuple(predicted)
            assert relative[a] + relative[b] == -1
            assert sum(relative[x] for x in g['neighbors'][a] if x != b) == 1
            assert relative[a] + sum(relative[x] for x in g['neighbors'][a]) == 0
            result.append((c, (q, electric)))
    assert len(result) == len(g['neighbors'][a]) - 1
    assert len({state for _, state in result}) == len(result)
    return result


def charge(q, q0, f):
    return csum(scale(q[x] - q0[x], f[x]) for x in range(len(q)))


def direct_stats(values):
    count = len(values)
    mean = scale(Q(1, count), csum(values))
    second = Q(sum(norm2(v) for v in values), count)
    return mean, second, second - norm2(mean)


def predicted_stats(g, f, sigma):
    M = sum(len(n) * (len(n) - 1) for n in g['neighbors'].values())
    total_s1 = (0, 0)
    second = 0
    for a in g['A']:
        d = len(g['neighbors'][a])
        differences = [add(f[b], scale(-1, f[a])) for b in g['neighbors'][a]]
        s1, s2 = csum(differences), sum(norm2(x) for x in differences)
        total_s1 = add(total_s1, scale(d - 1, s1))
        second += ((d - 1) * s2 if sigma == 0
                   else (d - 1 + sigma) * s2 - sigma * norm2(s1))
    mean = scale(Q(1 if sigma == 0 else 1 - sigma, M), total_s1)
    second = Q(2, M) * second
    return mean, second, second - norm2(mean)


def coherence_row(g, q0, fields):
    a, b = g['edges'][0]
    weights = ((1, 0),) if len(fields) == 1 else ((1, 0), (0, 1), (1, -1))
    vector = defaultdict(lambda: (0, 0))
    for E, amplitude in zip(fields, weights):
        for sigma in (1, -1):
            for _, state in outputs(g, q0, E, a, b, sigma):
                vector[state] = add(vector[state], amplitude)
    Z = sum(norm2(v) for v in vector.values())
    original_diagonal, dephased_diagonal = Counter(), Counter()
    pure_purity, dephased_purity, difference2, cross_blocks = Q(0), Q(0), Q(0), 0
    for s, amp in vector.items():
        original_diagonal[s[0]] += Q(norm2(amp), Z)
        dephased_diagonal[s[0]] += Q(norm2(amp), Z)
        for t, amp2 in vector.items():
            entry = scale(Q(1, Z), mul(amp, conj(amp2)))
            pure_purity += norm2(entry)
            if s[0][a] == t[0][a]:
                dephased_purity += norm2(entry)
            else:
                difference2 += norm2(entry)
                cross_blocks += (norm2(entry) != 0)
    assert original_diagonal == dephased_diagonal
    assert pure_purity == 1 and dephased_purity == Q(1, 2) and difference2 == Q(1, 2)
    return dict(graph=g['name'], field_components=len(fields), original_mark=[a, b],
                coherent_norm2=Z, support=len(vector), offdiagonal_sign_entries=cross_blocks,
                charge_diagonal_equal=True, coherent_purity=pure_purity,
                sign_dephased_purity=dephased_purity, density_difference_HS2=difference2)


def run_graph(g):
    q0 = tuple(int(x in g['A']) for x in g['vertices'])
    fields = fluxes(g)
    assert len(set(fields)) == len(fields)
    M = sum(len(v) * (len(v) - 1) for v in g['neighbors'].values())
    rows, all_zero, checked = [], [], 0
    for field_index, E in enumerate(fields):
        check_gauss(g, q0, E)
        norms = Counter()
        for a, b in g['edges']:
            for sigma in (1, -1):
                out = outputs(g, q0, E, a, b, sigma)
                norms[sigma] += len(out)
                checked += len(out)
                if field_index == 0:
                    all_zero.extend((a, b, c, sigma, state) for c, state in out)
        assert norms[1] == norms[-1] == M
        rows.append(dict(graph=g['name'], field=field_index,
                         input_max_abs_E=max(map(abs, E), default=0),
                         resolved_plus_total_norm2=norms[1],
                         resolved_minus_total_norm2=norms[-1],
                         coherent_edges_total_norm2=norms[1]+norms[-1],
                         actual_output_branches=norms[1]+norms[-1],
                         gauss_and_regional_charge_tests=True))
    gram_checks = 0
    for a, b in g['edges']:
        for signs in ((1,), (-1,), (1, -1)):
            vectors = [Counter(state for sigma in signs
                               for _, state in outputs(g, q0, E, a, b, sigma)) for E in fields]
            for i, vi in enumerate(vectors):
                for j, vj in enumerate(vectors):
                    gram = sum(v * vj.get(k, 0) for k, v in vi.items())
                    expected = len(signs) * (len(g['neighbors'][a]) - 1) if i == j else 0
                    assert gram == expected
                    gram_checks += 1
    actual_histogram = Counter(state[0] for a, b, c, sigma, state in all_zero)
    predicted_histogram = Counter()
    for b, c in product(g['B'], repeat=2):
        if b == c:
            continue
        multiplicity = sum(b in g['neighbors'][a] and c in g['neighbors'][a] for a in g['A'])
        if multiplicity:
            q = list(q0)
            q[b], q[c] = -1, 1
            predicted_histogram[tuple(q)] += multiplicity
    for a in g['A']:
        for b, c in combinations(g['neighbors'][a], 2):
            q = list(q0)
            q[a], q[b], q[c] = -1, 1, 1
            predicted_histogram[tuple(q)] += 2
    assert actual_histogram == predicted_histogram
    merged = Counter(state for *_, state in all_zero)
    wrong_norm = sum(v*v for v in merged.values())
    assert wrong_norm == 3*M and len(all_zero) == 2*M
    summary = dict(graph=g['name'], vertices=len(g['vertices']), A=len(g['A']),
                   B=len(g['B']), edges=len(g['edges']), degrees=[len(g['neighbors'][a]) for a in g['A']],
                   ordered_wedges=M, actual_loss_over_kappa=2*M,
                   input_fields=len(fields), primitive_output_checks=checked,
                   exact_Gram_entries=gram_checks, distinct_charge_patterns=len(actual_histogram),
                   charge_pattern_multiplicities_match=True,
                   invalid_all_label_coherent_norm2=wrong_norm,
                   invalid_all_label_merge_changes_instrument=True)
    fs = {
        'constant': [(1, 0)]*len(q0),
        'point_A': [(int(x == g['A'][0]), 0) for x in g['vertices']],
        'point_B': [(int(x == g['B'][0]), 0) for x in g['vertices']],
        'real_index': [(x-2, 0) for x in g['vertices']],
        'complex_index': [(x % 5-2, x % 3-1) for x in g['vertices']]
    }
    moment_rows = []
    for name, f in fs.items():
        for sigma in (1, -1, 0):
            values = [charge(state[0], q0, f) for a, b, c, sign, state in all_zero
                      if sigma == 0 or sign == sigma]
            actual = direct_stats(values)
            predicted = predicted_stats(g, f, sigma)
            assert actual == predicted
            moment_rows.append(dict(graph=g['name'], test=name, sigma=sigma,
                                    mean=actual[0], second_absolute=actual[1],
                                    variance_absolute=actual[2], branches=len(values), exact=True))
    local_rows = []
    for name in ('real_index', 'complex_index'):
        f = fs[name]
        for a, b in g['edges']:
            db = add(f[b], scale(-1, f[a]))
            remaining = [add(f[c], scale(-1, f[a])) for c in g['neighbors'][a] if c != b]
            average = scale(Q(1, len(remaining)), csum(remaining))
            for sigma in (1, -1, 0):
                values = [charge(s[0], q0, f) for aa, bb, c, sig, s in all_zero
                          if aa == a and bb == b and (sigma == 0 or sigma == sig)]
                actual = direct_stats(values)
                mean = add(average, scale(-sigma, db))
                second = norm2(db) + Q(sum(norm2(v) for v in remaining), len(remaining))
                if sigma:
                    second -= 2*sigma*mul(average, conj(db))[0]
                assert actual == (mean, second, second-norm2(mean))
        local_rows.append(dict(graph=g['name'], test=name, selected_edges=len(g['edges']),
                               exact_selected_mark_moment_comparisons=3*len(g['edges'])))
    return summary, rows, moment_rows, local_rows, coherence_row(g, q0, fields), all_zero


def fourier_rows(g, branches):
    assert g['side'] == 4
    q0 = tuple(int(x in g['A']) for x in g['vertices'])
    powers_i = ((1, 0), (0, 1), (-1, 0), (0, -1))
    a0 = g['A'][0]
    rows = []
    for m in product(range(4), repeat=3):
        f = [powers_i[sum(u*v for u, v in zip(m, x)) % 4] for x in g['coordinates']]
        C = Q(sum(powers_i[t][0] for t in m), 3)
        second = 4*(1-C)
        exceptional = m in ((0,0,0), (2,2,2))
        global_mean = (C-1, 0) if exceptional else (Q(0), Q(0))
        a_character = scale(Q(1, len(g['A'])), csum(f[a] for a in g['A']))
        assert a_character == ((1,0) if exceptional else (0,0))
        results = {}
        for sigma in (1, -1, 0):
            all_values = [charge(state[0], q0, f) for a,b,c,sig,state in branches
                          if sigma == 0 or sigma == sig]
            local_values = [charge(state[0], q0, f) for a,b,c,sig,state in branches
                            if a == a0 and (sigma == 0 or sigma == sig)]
            global_stats, local_stats = direct_stats(all_values), direct_stats(local_values)
            if sigma == 1:
                expected_second, expected_local_mean = Q(12,5)*(1-C*C), (Q(0),Q(0))
            elif sigma == -1:
                expected_second = Q(16,5)*(1-C)+Q(12,5)*(1-C)**2
                expected_local_mean = (2*(C-1),Q(0))
            else:
                expected_second, expected_local_mean = second, (C-1,Q(0))
            expected_global_mean = expected_local_mean if exceptional else (Q(0),Q(0))
            assert global_stats == (expected_global_mean, expected_second,
                                    expected_second-norm2(expected_global_mean))
            assert local_stats == (expected_local_mean, expected_second,
                                   expected_second-norm2(expected_local_mean))
            results[str(sigma)] = dict(global_mean=global_stats[0], second=global_stats[1],
                                       global_variance=global_stats[2],
                                       center_mean=local_stats[0], center_variance=local_stats[2])
        assert results['0']['global_mean'] == global_mean
        assert results['0']['center_variance'] == (1-C)*(3+C)
        rows.append(dict(mode=m, C=C, A_character=a_character, statistics=results, exact=True))
    return rows


def main():
    gs = [graph('star', range(3), {0}, [(0,1),(0,2)]),
          graph('irregular', range(5), {0,1}, [(0,2),(0,3),(1,2),(1,3),(1,4)]),
          cubic(2), cubic(4)]
    report = dict(status='all exact assertions passed', method='fresh integer/Fraction primitives',
                  external_programs_imported=False, graphs=[], primitive_fields=[], moments=[],
                  selected_mark_moments=[], coherent_vs_dephased=[], fourier=[])
    for g in gs:
        summary, primitive, moments, local, coherence, branches = run_graph(g)
        report['graphs'].append(summary)
        report['primitive_fields'].extend(primitive)
        report['moments'].extend(moments)
        report['selected_mark_moments'].extend(local)
        report['coherent_vs_dephased'].append(coherence)
        if g['side'] == 4:
            report['fourier'] = fourier_rows(g, branches)
    report['group_counts'] = {key:len(report[key]) for key in
                              ('graphs','primitive_fields','moments','selected_mark_moments',
                               'coherent_vs_dephased','fourier')}
    print(json.dumps(exact(report), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
