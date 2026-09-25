"""Exact original rotor jumps and four-hop magnetic columns, with all flux shifts.

Full cube matter words and selected degree-six torus words are checked. Rotor
amplitudes are independent of absolute electric flux, so each affine column
retains every electric-shift word without introducing a field cutoff.
"""
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import time


def graph(side):
    vertices = list(product(range(side), repeat=3))
    index = {v: i for i, v in enumerate(vertices)}
    aa = [i for i, v in enumerate(vertices) if sum(v) % 2 == 0]
    bb = [i for i in range(len(vertices)) if i not in aa]
    adjacency = {}
    for i, v in enumerate(vertices):
        adjacency[i] = sorted({index[tuple((x+(step if axis == j else 0)) % side
                                         for j, x in enumerate(v))]
                               for axis in range(3) for step in (-1, 1)})
    edges = [(a, b) for a in aa for b in adjacency[a]]
    edge_index = {pair: i for i, pair in enumerate(edges)}
    pairs = sorted({tuple(sorted(pair)) for b in bb
                    for pair in combinations(adjacency[b], 2)})
    overlap = [len(set(adjacency[a]) & set(adjacency[c])) for a, c in pairs]
    degree = len(adjacency[bb[0]])
    assert all(len(adjacency[x]) == degree for x in range(len(vertices)))
    assert max(overlap) == 2
    return vertices, aa, bb, adjacency, edges, edge_index, pairs, degree


def tree_flow(q, aa, adjacency, edges, edge_index):
    charge = [v-int(i in aa) for i, v in enumerate(q)]
    assert sum(charge) == 0
    parents, order = {0: None}, [0]
    for u in order:
        for v in adjacency[u]:
            if v not in parents:
                parents[v] = u
                order.append(v)
    electric = [0]*len(edges)
    for v in reversed(order[1:]):
        u = parents[v]
        pair = (v, u) if v in aa else (u, v)
        electric[edge_index[pair]] = charge[v] if v in aa else -charge[v]
        charge[u] += charge[v]
    divergence = [0]*len(q)
    for (a, b), value in zip(edges, electric):
        divergence[a] += value
        divergence[b] -= value
    assert divergence == [v-int(i in aa) for i, v in enumerate(q)]
    return electric


def column_control(side, q, label):
    vertices, aa, bb, adjacency, edges, edge_index, pairs, degree = graph(side)
    electric = tree_flow(q, aa, adjacency, edges, edge_index)
    zero = ((), ())

    def changed(state, updates, edge, shift):
        charges, flux = map(dict, state)
        for site, value in updates.items():
            if value == q[site]:
                charges.pop(site, None)
            else:
                charges[site] = value
        flux[edge] = flux.get(edge, 0)+shift
        if flux[edge] == 0:
            del flux[edge]
        return tuple(sorted(charges.items())), tuple(sorted(flux.items()))

    def f(vector, a, adjoint=False):
        result = Counter()
        for state, weight in vector.items():
            values = dict(state[0])
            qa = values.get(a, q[a])
            for b in adjacency[a]:
                qb = values.get(b, q[b])
                if not adjoint and qa and qb == 0:
                    target = changed(state, {a: 0, b: qa}, edge_index[a, b], -qa)
                elif adjoint and qa == 0 and qb:
                    target = changed(state, {a: qb, b: 0}, edge_index[a, b], qb)
                else:
                    continue
                result[target] += weight
        return result

    def jump(vector, a, b, sign, adjoint=False):
        result = Counter()
        for state, weight in vector.items():
            values = dict(state[0])
            qa, qb = values.get(a, q[a]), values.get(b, q[b])
            if not adjoint and qa == qb == 0:
                target = changed(state, {a: sign, b: -sign}, edge_index[a, b], sign)
            elif adjoint and qa == sign and qb == -sign:
                target = changed(state, {a: 0, b: 0}, edge_index[a, b], -sign)
            else:
                continue
            result[target] += weight
        return result

    def add(target, source, coefficient=1):
        for state, value in source.items():
            target[state] += coefficient*value

    start = Counter({zero: 1})
    outgoing = {a: f(start, a) for a in aa}
    gamma, gamma_coherent, formula = Counter(), Counter(), Counter()
    for a in aa:
        for b in adjacency[a]:
            coherent_output = Counter()
            for sign in (-1, 1):
                output = jump(outgoing[a], a, b, sign)
                add(coherent_output, output)
                add(gamma, f(jump(output, a, b, sign, True), a, True))
            for sign in (-1, 1):
                add(gamma_coherent, f(jump(coherent_output, a, b, sign, True), a, True))
            filtered = Counter({state: value for state, value in outgoing[a].items()
                                if dict(state[0]).get(b, q[b]) == 0})
            add(formula, f(filtered, a, True), 2)
    assert gamma == gamma_coherent == formula
    magnetic = Counter()
    for a, c in pairs:
        out = f(outgoing[a], c)
        add(magnetic, f(f(out, c, True), a, True))
    for state in set(gamma) | set(magnetic):
        assert gamma[state] >= 0 and magnetic[state] >= 0
        assert (degree-1)*gamma[state] <= 8*magnetic[state]
        divergence = [0]*len(q)
        for edge, value in state[1]:
            a, b = edges[edge]
            divergence[a] += value
            divergence[b] -= value
        delta_q = [0]*len(q)
        for site, value in state[0]:
            delta_q[site] = value-q[site]
        assert divergence == delta_q
        assert sum(dict(state[0]).get(a, q[a]) != 0 for a in aa) == len(aa)
        assert sum(dict(state[0]).get(v, q[v]) != 0 for v in range(len(q))) == sum(x != 0 for x in q)
    empty_counts = [sum(q[b] == 0 for b in adjacency[a]) for a in aa]
    exact_diagonal = 2*sum(k*(k-1) for k in empty_counts)
    assert gamma[zero] == exact_diagonal
    m = sum(q[b] != 0 for b in bb)
    assert exact_diagonal >= 4*(degree*(len(bb)-m)-len(aa))
    payload = [[state[0], state[1], gamma[state], magnetic[state]]
               for state in sorted(set(gamma) | set(magnetic))]
    raw = json.dumps(payload, separators=(',', ':')).encode()
    offdiag = [Fraction(gamma[state], magnetic[state])
               for state in gamma if state != zero and gamma[state]]
    return {
        'side': side, 'label': label, 'degree_B': degree, 'A_sites': len(aa),
        'B_occupied': m, 'minus_charges': sum(x == -1 for x in q),
        'initial_charge_word': q, 'one_exact_Gauss_flow': electric,
        'exact_resolved_equals_coherent_equals_formula': True,
        'Gamma_diagonal': exact_diagonal, 'Q_diagonal': magnetic[zero],
        'Gamma_nonzero_entries': sum(v != 0 for v in gamma.values()),
        'Q_nonzero_entries': sum(v != 0 for v in magnetic.values()),
        'maximum_offdiagonal_Gamma_over_Q': str(max(offdiag)) if offdiag else None,
        'entrywise_inequality': '(degree_B-1) Gamma <= 8 Q, kappa=1 and r_max=2',
        'all_output_Gauss_and_number_checks_exact': True,
        'complete_affine_columns_sha256': hashlib.sha256(raw).hexdigest(),
        'complete_affine_columns': payload,
    }


def main():
    tick = time.perf_counter()
    v, aa, bb, *_ = graph(2)
    rows = []
    for m in (0, 2, 4):
        for occupied in combinations(bb, m):
            for minus in combinations(aa+list(occupied), m//2):
                q = [int(i in aa or i in occupied) for i in range(len(v))]
                for i in minus:
                    q[i] = -1
                rows.append(column_control(2, q, f'all_matter_{len(rows)}'))
    assert len(rows) == 65
    v, aa, bb, adjacency, *_ = graph(6)
    index = {x: i for i, x in enumerate(v)}
    sets = [
        ('empty', [], 'B'),
        ('near_pair_minus_B', [index[(1, 0, 0)], index[(0, 1, 0)]], 'B'),
        ('far_pair_minus_A', [index[(1, 0, 0)], index[(4, 3, 0)]], 'A'),
        ('half_occupied_minus_B', bb[:54], 'B'),
        ('half_occupied_minus_A', bb[:54], 'A'),
        ('two_distant_vacancies', [x for x in bb if x not in [index[(1, 0, 0)], index[(4, 3, 0)]]], 'B'),
        ('full_B', bb, 'B'),
    ]
    for label, occupied, signs in sets:
        q = [int(i in aa or i in occupied) for i in range(len(v))]
        for i in (occupied if signs == 'B' else aa)[:len(occupied)//2]:
            q[i] = -1
        rows.append(column_control(6, q, label))
    return {
        'scope': __doc__, 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'cube_complete_matter_words': 65, 'degree_six_selected_words': 7,
        'all_assertions_passed': True, 'columns': rows,
        'limitations': 'Exact primitive affine-column and incidence control. No Hamiltonian diagonalization, weak-coupling threshold, relaxation, microscopic-energy or observational calculation.',
        'elapsed_seconds': time.perf_counter()-tick,
    }


if __name__ == '__main__':
    result = main()
    destination = Path('PRIMITIVE_RATE_ENERGY_RESULTS.json')
    destination.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    summary = {k: v for k, v in result.items() if k != 'columns'}
    summary['rows'] = [{k: v for k, v in row.items()
                        if k not in ['initial_charge_word', 'one_exact_Gauss_flow', 'complete_affine_columns']}
                       for row in result['columns']]
    summary['complete_result_sha256'] = hashlib.sha256(destination.read_bytes()).hexdigest()
    print(json.dumps(summary, indent=2))
