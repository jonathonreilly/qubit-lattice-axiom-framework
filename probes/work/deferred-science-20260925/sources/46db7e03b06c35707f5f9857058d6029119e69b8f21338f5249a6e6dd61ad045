"""Own exact legal-hop/birth and local-support calculation; no parent imports."""
from collections import defaultdict
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def graph(L):
    sites = list(product(range(L), repeat=3))
    index = {v: i for i, v in enumerate(sites)}
    A = [i for i, v in enumerate(sites) if sum(v) % 2 == 0]
    neighbours = {}
    for a in A:
        candidates = set()
        for axis in range(3):
            for sign in (-1, 1):
                x = list(sites[a]); x[axis] = (x[axis] + sign) % L
                candidates.add(index[tuple(x)])
        neighbours[a] = sorted(candidates)
    edges = [(a, b) for a in A for b in neighbours[a]]
    return sites, A, neighbours, edges


def sparse(values):
    return [[i, x] for i, x in enumerate(values) if x]


def divergence(field, edges, n):
    result = [0] * n
    for value, (a, b) in zip(field, edges):
        result[a] += value; result[b] -= value
    return result


def run(L):
    sites, A, neighbours, edges = graph(L)
    n, m = len(sites), len(edges)
    edge_id = {edge: i for i, edge in enumerate(edges)}
    q0 = tuple(int(i in A) for i in range(n))
    e0 = (0,) * m

    def legal_hop(q, field, a, c):
        if q[a] == 0 or q[c] != 0:
            return None
        charge = q[a]
        outq, outfield = list(q), list(field)
        outq[a] = 0; outq[c] = charge
        outfield[edge_id[a, c]] -= charge
        assert divergence(outfield, edges, n) == [x - y for x, y in zip(outq, q0)]
        return tuple(outq), tuple(outfield)

    def legal_birth(q, field, a, b, sign):
        if q[a] != 0 or q[b] != 0:
            return None
        outq, outfield = list(q), list(field)
        outq[a] = sign; outq[b] = -sign
        outfield[edge_id[a, b]] += sign
        assert divergence(outfield, edges, n) == [x - y for x, y in zip(outq, q0)]
        return tuple(outq), tuple(outfield)

    def images(a, b, signs, field):
        output = defaultdict(int)
        for sign in signs:
            for c in neighbours[a]:
                moved = legal_hop(q0, field, a, c)
                if moved is not None:
                    born = legal_birth(*moved, a, b, sign)
                    if born is not None:
                        output[born] += 1
        return dict(output)

    rows = []
    for a, b in edges:
        for sign in (-1, 1):
            for c in neighbours[a]:
                moved = legal_hop(q0, e0, a, c)
                born = legal_birth(*moved, a, b, sign)
                if born is None:
                    assert b == c
                    continue
                q, field = born
                delta = tuple(x - y for x, y in zip(q, q0))
                assert sum(abs(x) for x in q) == len(A) + 2 and sum(delta) == 0
                rows.append({'a': a, 'b': b, 'c': c, 'sign': sign,
                             'delta_q': sparse(delta), 'field': sparse(field)})

    instruments = {}
    for label, channel_signs in [('resolved', [(-1,), (1,)]), ('coherent', [(-1, 1)]), ('plus_only_mutant', [(1,)])]:
        mean = [0] * n
        raw = [[0] * n for _ in range(n)]
        norm = 0
        for a, b in edges:
            for signs in channel_signs:
                for (q, field), amplitude in images(a, b, signs, e0).items():
                    weight = amplitude * amplitude
                    dq = [(i, q[i] - q0[i]) for i in range(n) if q[i] != q0[i]]
                    norm += weight
                    for i, x in dq:
                        mean[i] += weight * x
                        for j, y in dq:
                            raw[i][j] += weight * x * y
        instruments[label] = {'initial_gain_norm': norm, 'mean_slope_in_kappa': mean,
                              'covariance_slope_in_kappa': raw}

    # Two genuinely distinct physical field basis inputs; all selected Gram entries are saved.
    coord_id = {v: i for i, v in enumerate(sites)}
    loop = [coord_id[(0, 0, 0)], coord_id[(1, 0, 0)],
            coord_id[(1, 1, 0)], coord_id[(0, 1, 0)], coord_id[(0, 0, 0)]]
    circulation = [0] * m
    for x, y in zip(loop, loop[1:]):
        if (x, y) in edge_id:
            circulation[edge_id[x, y]] += 7
        else:
            circulation[edge_id[y, x]] -= 7
    assert divergence(circulation, edges, n) == [0] * n
    fields = [e0, tuple(circulation)]
    a, b = coord_id[(0, 0, 0)], coord_id[(1, 0, 0)]
    observed = [a, b, coord_id[(0, 1, 0)], coord_id[(1, 1, 0)]]
    grams = []
    for signs in [(-1,), (1,), (-1, 1)]:
        outputs = [images(a, b, signs, field) for field in fields]
        for operator in [()] + [(x,) for x in observed] + [(x, y) for x in observed for y in observed]:
            matrix = [[0, 0], [0, 0]]
            for r in range(2):
                for c in range(2):
                    for state, amplitude in outputs[c].items():
                        weight = 1
                        for x in operator:
                            weight *= state[0][x] - q0[x]
                        matrix[r][c] += outputs[r].get(state, 0) * amplitude * weight
            grams.append({'signs': list(signs), 'operator_delta_q_sites': list(operator), 'matrix': matrix})

    # Count actual supports after the commuting electric dressing, using site/link atoms.
    dsets = [{a, b, n + i} for i, (a, b) in enumerate(edges)]
    stars = {a: {a, *neighbours[a], *(n + edge_id[a, b] for b in neighbours[a])} for a in A}
    pairs = [(a, c) for i, a in enumerate(A) for c in A[i + 1:] if set(neighbours[a]) & set(neighbours[c])]
    def expand(support):
        return support | set().union(*(d for d in dsets if d & support))
    hsets = [stars[a] | stars[c] for a, c in pairs]
    jsets = [stars[a] for a, b in edges for _ in (-1, 1)]
    support_rows = {}
    for label, sets in [('magnetic', hsets), ('resolved_jump', jsets)]:
        enlarged = [expand(s) for s in sets]
        counts = [sum(atom in s for s in sets) for atom in range(n + m)]
        counts_after = [sum(atom in s for s in enlarged) for atom in range(n + m)]
        support_rows[label] = {'term_count': len(sets), 'max_support_before': max(map(len, sets)),
                               'max_support_after': max(map(len, enlarged)),
                               'incidence_before': counts, 'incidence_after': counts_after}
    return {'L': L, 'sites': sites, 'A': A, 'edges_oriented_A_to_B': edges,
            'primitive_rows': rows, 'instruments': instruments,
            'selected_gram_input_fields': [sparse(field) for field in fields],
            'selected_edge': [a, b], 'selected_grams': grams, 'support_counts': support_rows}


def main():
    data = {'scope': 'Exact new primitive, diagonal-charge compression and support counts; no author code.',
            'tori': [run(4), run(6)],
            'nonnorm_continuity': [{'loop_amplitude_M': M, 'electric_energy_difference_over_K': 8 * M + 4,
                                    'time_in_units_pi_over_K': [1, 8 * M + 4], 'exact_norm_difference': 2}
                                   for M in (1, 10, 100, 1000, 10000)]}
    (HERE / 'PRIMITIVE_RESULTS.json').write_text(json.dumps(data, indent=2) + '\n')
    print(json.dumps({'result': 'PRIMITIVE_RESULTS.json',
                      'tori': [{'L': row['L'], 'primitive_rows': len(row['primitive_rows']),
                                'gram_rows': len(row['selected_grams']),
                                'rates': {k: v['initial_gain_norm'] for k, v in row['instruments'].items()}}
                               for row in data['tori']],
                      'all_primitive_intermediate_and_final_gauss_checks': True}, indent=2))


if __name__ == '__main__':
    main()
