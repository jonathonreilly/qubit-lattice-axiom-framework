"""Independent exact integer/rational controls for the permitted common model.

No parent program is imported. No author packet is opened. This constructs
local hop/return paths, torus incidence, fixed-number Rayleigh counts and
physical integer Gauss flows. It does not diagonalize a truncated rotor.
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import json
import time


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def falling(n, k):
    value = 1
    for i in range(k):
        value *= n-i
    return value


def local_return_count(A, C, occupied):
    count = 0
    for b in A-occupied:
        for d in C-occupied:
            if b == d:
                continue
            output = occupied | {b, d}
            for x in A & output:
                for y in C & output:
                    count += x != y
    return count


def local_formula(r, ua, uc, w):
    ha, hc, t = 6-ua, 6-uc, r-w
    paths = ha*hc-t
    return (paths*((ua+1)*(uc+1)-w)
            + ua*t*(hc-1) + uc*t*(ha-1) + t*(t-1))


def local_certificate(r):
    A = set(range(6))
    C = set(range(r)) | set(range(6, 12-r))
    universe = sorted(A | C)
    common = A & C
    groups = {}
    mutations_rejected = 0
    for bits in product((0, 1), repeat=len(universe)):
        occupied = {v for v, bit in zip(universe, bits) if bit}
        ua, uc, w = len(A & occupied), len(C & occupied), len(common & occupied)
        exact = local_return_count(A, C, occupied)
        formula = local_formula(r, ua, uc, w)
        assert exact == formula
        wrong = (6-ua)*(6-uc)*((ua+1)*(uc+1)-w)
        mutations_rejected += wrong != exact
        key = (ua, uc, w)
        if key not in groups:
            groups[key] = {'r': r, 'ua': ua, 'uc': uc, 'w': w,
                           'return_count': exact, 'occupancy_masks': 0}
        assert groups[key]['return_count'] == exact
        groups[key]['occupancy_masks'] += 1
    paths = [(b, d) for b in A for d in C if b != d]
    union_counts = Counter(len(set(p) | set(q)) for p in paths for q in paths)
    predicted = {2: 36+r*r-2*r,
                 3: 360+32*r-2*r*r,
                 4: (36-r)**2-(36+r*r-2*r)-(360+32*r-2*r*r)}
    assert dict(union_counts) == predicted
    empty = local_return_count(A, C, set())
    assert empty == predicted[2]
    low_ratio = max(F(row['return_count']-empty, row['ua']+row['uc'])
                    for row in groups.values() if row['ua']+row['uc'])
    hole_ratio = max(F(row['return_count'], 12-row['ua']-row['uc'])
                     for row in groups.values() if row['ua']+row['uc'] < 12)
    for row in groups.values():
        row['low_bound_slack'] = str(empty+low_ratio*(row['ua']+row['uc'])-row['return_count'])
        row['hole_bound_slack'] = str(hole_ratio*(12-row['ua']-row['uc'])-row['return_count'])
        assert F(row['low_bound_slack']) >= 0 and F(row['hole_bound_slack']) >= 0
    assert mutations_rejected > 0
    return {'r': r, 'union_size': len(universe), 'masks_checked': 2**len(universe),
            'groups': sorted(groups.values(), key=lambda row: (row['w'], row['ua'], row['uc'])),
            'path_count': len(paths), 'squared_path_union_counts': dict(sorted(union_counts.items())),
            'empty_return_count': empty, 'sharp_local_low_slope': str(low_ratio),
            'sharp_local_hole_slope': str(hole_ratio),
            'low_slope_saturating_groups': [list(key) for key, row in groups.items()
                if row['ua']+row['uc'] and F(row['return_count']-empty, row['ua']+row['uc']) == low_ratio],
            'hole_slope_saturating_groups': [list(key) for key, row in groups.items()
                if row['ua']+row['uc'] < 12 and F(row['return_count'], 12-row['ua']-row['uc']) == hole_ratio],
            'wrong_omitted_common_exclusion_and_exchange_masks_rejected': mutations_rejected}


def rayleigh_union(M, m, certificate):
    return sum(F(value*falling(m, size-2)*falling(M-m, 2), falling(M, size))
               for size, value in certificate['squared_path_union_counts'].items())


def rayleigh_rows(M, m, certificate):
    outside = M-certificate['union_size']
    total = 0
    denominator = choose(M, m)
    normalization = 0
    for row in certificate['groups']:
        inside = row['ua']+row['uc']-row['w']
        multiplicity = row['occupancy_masks']*choose(outside, m-inside)
        total += multiplicity*row['return_count']
        normalization += multiplicity
    assert normalization == denominator
    return F(total, denominator)


def torus(lengths):
    vertices = list(product(*(range(n) for n in lengths)))
    A = [v for v in vertices if sum(v) % 2 == 0]
    B = [v for v in vertices if sum(v) % 2]
    neighbours = {}
    for v in vertices:
        neighbours[v] = set()
        for axis in range(3):
            for sign in (-1, 1):
                w = list(v)
                w[axis] = (w[axis]+sign) % lengths[axis]
                neighbours[v].add(tuple(w))
        assert len(neighbours[v]) == 6
        assert all(sum(w) % 2 != sum(v) % 2 for w in neighbours[v])
    edges = [(a, b) for a in A for b in sorted(neighbours[a])]
    assert len(edges) == 6*len(A)
    return vertices, A, B, neighbours, edges


def geometry_control(lengths, certificates):
    vertices, A, B, neighbours, edges = torus(lengths)
    M = len(A)
    counts = Counter()
    each = {a: Counter() for a in A}
    for a, c in combinations(A, 2):
        r = len(neighbours[a] & neighbours[c])
        if r:
            assert r in (1, 2)
            counts[r] += 1
            each[a][r] += 1
            each[c][r] += 1
    short = sum(n == 4 for n in lengths)
    n1, n2 = 6-2*short, 12+short
    for a in A:
        assert each[a][1] == n1 and each[a][2] == n2
    base = 2*sum(counts[r]*certificates[r]['empty_return_count'] for r in (1, 2))
    assert base == (642-34*short)*M
    zero_field_diagonal = 2*sum(counts[r]*(36-r) for r in (1, 2))
    assert zero_field_diagonal == (618-36*short)*M
    trial = 2*sum(counts[r]*rayleigh_union(M, M//2, certificates[r]) for r in (1, 2))
    low_constant = 12*(n1*F(certificates[1]['sharp_local_low_slope'])
                       + n2*F(certificates[2]['sharp_local_low_slope']))
    hole_constant = 12*(n1*F(certificates[1]['sharp_local_hole_slope'])
                        + n2*F(certificates[2]['sharp_local_hole_slope']))
    assert trial > base and 0 < (trial-base)/(low_constant*M) < 1
    assert 0 < trial/(hole_constant*M) < 1
    return {'lengths': list(lengths), 'M_A_equals_B': M, 'edges': len(edges),
            'length_four_axes': short, 'per_A_r1': n1, 'per_A_r2': n2,
            'unordered_r1_pairs': counts[1], 'unordered_r2_pairs': counts[2],
            'empty_band_maximum_Q0': base,
            'empty_zero_field_diagonal_Q': zero_field_diagonal,
            'half_filled_trial_Q': str(trial),
            'half_filled_trial_gain': str(trial-base),
            'low_occupation_row_constant': str(low_constant),
            'hole_row_constant': str(hole_constant),
            'weak_limit_lower_filling_from_trial': str((trial-base)/(low_constant*M)),
            'weak_limit_upper_filling_from_trial': str(1-trial/(hole_constant*M))}


def physical_graph(lengths):
    vertices, A, B, neighbours, edges = torus(lengths)
    index = {v: i for i, v in enumerate(vertices)}
    edge_index = {frozenset(e): i for i, e in enumerate(edges)}
    parent = {vertices[0]: None}
    order = [vertices[0]]
    for v in order:
        for w in sorted(neighbours[v]):
            if w not in parent:
                parent[w] = v
                order.append(w)
    assert len(order) == len(vertices)
    return vertices, A, B, neighbours, edges, index, edge_index, parent, order


def tree_flow(q, graph):
    vertices, A, B, neighbours, edges, index, edge_index, parent, order = graph
    Aset = set(A)
    demand = {v: q[index[v]]-int(v in Aset) for v in vertices}
    assert sum(demand.values()) == 0
    field = [0]*len(edges)
    for v in reversed(order[1:]):
        u = parent[v]
        e = edge_index[frozenset((v, u))]
        field[e] = demand[v] if edges[e][0] == v else -demand[v]
        demand[u] += demand[v]
    return tuple(field)


def divergence(field, graph):
    vertices, A, B, neighbours, edges, index, edge_index, parent, order = graph
    result = [0]*len(vertices)
    for value, (a, b) in zip(field, edges):
        result[index[a]] += value
        result[index[b]] -= value
    return tuple(result)


def check_gauss(q, field, graph):
    vertices, A, B, neighbours, edges, index, edge_index, parent, order = graph
    aset = set(A)
    assert divergence(field, graph) == tuple(q[index[v]]-int(v in aset) for v in vertices)


def electric_D(q, field, graph):
    vertices, A, B, neighbours, edges, index, edge_index, parent, order = graph
    assert all(q[index[a]] != 0 for a in A)
    terms = [field[e]*(field[e]-q[index[a]]) for e, (a, b) in enumerate(edges)
             if q[index[b]] == 0]
    assert all(value >= 0 for value in terms)
    return sum(terms)


def hop(q, field, a, b, outward, graph):
    vertices, A, B, neighbours, edges, index, edge_index, parent, order = graph
    qa, qb = q[index[a]], q[index[b]]
    source = qa if outward else qb
    assert source in (-1, 1)
    assert (qb == 0) if outward else (qa == 0)
    qnew, enew = list(q), list(field)
    qnew[index[a]], qnew[index[b]] = (0, source) if outward else (source, 0)
    enew[edge_index[frozenset((a, b))]] += -source if outward else source
    qnew, enew = tuple(qnew), tuple(enew)
    check_gauss(qnew, enew, graph)
    assert sum(x != 0 for x in qnew) == sum(x != 0 for x in q)
    return qnew, enew


def cycles(graph):
    vertices, A, B, neighbours, edges, index, edge_index, parent, order = graph
    tree = {edge_index[frozenset((v, parent[v]))] for v in order[1:]}
    non_tree = [e for e in range(len(edges)) if e not in tree]
    basis = []
    for e in non_tree:
        a, b = edges[e]
        field = [0]*len(edges)
        field[e] = 1
        demand = [0]*len(vertices)
        demand[index[a]], demand[index[b]] = -1, 1
        # Solve the opposite endpoint divergence on the spanning tree.
        subtree = dict(zip(vertices, demand))
        for v in reversed(order[1:]):
            u = parent[v]
            f = edge_index[frozenset((v, u))]
            field[f] += subtree[v] if edges[f][0] == v else -subtree[v]
            subtree[u] += subtree[v]
        assert not any(divergence(field, graph))
        assert [field[f] for f in non_tree] == [int(f == e) for f in non_tree]
        basis.append(tuple(field))
    assert len(basis) == len(edges)-len(vertices)+1
    return non_tree, basis


def physical_controls():
    rows = []
    for lengths, c in [((4, 4, 4), (1, 1, 0)), ((6, 6, 6), (2, 0, 0))]:
        graph = physical_graph(lengths)
        vertices, A, B, neighbours, edges, index, edge_index, parent, order = graph
        M = len(A)
        a = (0, 0, 0)
        common = neighbours[a] & neighbours[c]
        non_tree, basis = cycles(graph)
        for axis in range(3):
            winding = [0]*len(edges)
            for coordinate in range(lengths[axis]):
                v, w = [0, 0, 0], [0, 0, 0]
                v[axis] = coordinate
                w[axis] = (coordinate+1) % lengths[axis]
                v, w = tuple(v), tuple(w)
                e = edge_index[frozenset((v, w))]
                winding[e] += 1 if edges[e][0] == v else -1
            assert not any(divergence(winding, graph))
            coordinates = [winding[e] for e in non_tree]
            assert tuple(winding) == tuple(sum(z*v[e] for z, v in zip(coordinates, basis))
                                           for e in range(len(edges)))
        test_cycle = tuple(sum((i % 3-1)*v[e] for i, v in enumerate(basis))
                           for e in range(len(edges)))
        assert not any(divergence(test_cycle, graph))
        for m, rotate in [(0, 0), (2, 0), (M//2, 0), (M//2, M), (M, M)]:
            occupied = A+B[:m]
            negative = set((occupied[rotate:]+occupied[:rotate])[:m//2])
            q = tuple((-1 if v in negative else 1) if v in occupied else 0 for v in vertices)
            field = tree_flow(q, graph)
            field = tuple(x+y for x, y in zip(field, test_cycle))
            check_gauss(q, field, graph)
            D = electric_D(q, field, graph)
            occupied_B = {b for b in B if q[index[b]]}
            direct = 0
            return_outputs = Counter()
            for b in sorted(neighbours[a]-occupied_B):
                q1, e1 = hop(q, field, a, b, True, graph)
                for d in sorted(neighbours[c]-occupied_B-{b}):
                    q2, e2 = hop(q1, e1, c, d, True, graph)
                    output_B = occupied_B | {b, d}
                    for x in sorted(neighbours[a] & output_B):
                        q3, e3 = hop(q2, e2, a, x, False, graph)
                        for y in sorted((neighbours[c] & output_B)-{x}):
                            q4, e4 = hop(q3, e3, c, y, False, graph)
                            direct += 1
                            return_outputs[(q4, e4)] += 1
            expected = local_return_count(neighbours[a], neighbours[c], occupied_B)
            assert direct == expected == sum(return_outputs.values())
            cycle_displacements = [sum(abs(e4[e]-field[e]) for e in non_tree)
                                   for q4, e4 in return_outputs]
            assert max(cycle_displacements, default=0) <= 4
            if m == 0:
                assert electric_D(q, (0,)*len(edges), graph) == 0
                assert return_outputs[(q, field)] == 36-len(common)
            if m == M:
                assert D == 0 and direct == 0 and sum(x*x for x in field) > 0
            rows.append({'lengths': list(lengths), 'M': M, 'm_B': m,
                         'negative_colors': len(negative), 'negative_color_rotation': rotate,
                         'pair_common_neighbours': len(common), 'gated_D': D,
                         'ungated_sum_E_squared': sum(x*x for x in field),
                         'cycle_rank': len(basis), 'physical_return_paths': direct,
                         'unchanged_charge_electric_return_paths': return_outputs[(q, field)],
                         'max_cycle_coordinate_displacement_l1': max(cycle_displacements, default=0),
                         'three_winding_cycles_exactly_reconstructed': True,
                         'distinct_charge_electric_return_words': len(return_outputs),
                         'gauss_checks_exact': True, 'actual_gate_retained': True})
    return rows


def main():
    tick = time.monotonic()
    certificates = {r: local_certificate(r) for r in (1, 2)}
    rows = []
    for M in (32, 48, 108, 256):
        for m in sorted({0, 2, M//4 if (M//4) % 2 == 0 else M//4-1, M//2, M-2, M}):
            for r, certificate in certificates.items():
                first = rayleigh_union(M, m, certificate)
                second = rayleigh_rows(M, m, certificate)
                assert first == second
                rows.append({'M': M, 'm': m, 'r': r, 'ordered_union_rayleigh': str(first),
                             'independent_row_average': str(second), 'difference': '0'})
    geometry = [geometry_control(lengths, certificates) for lengths in
                [(4, 4, 4), (4, 4, 6), (4, 6, 6), (6, 6, 6), (8, 8, 8)]]
    physical = physical_controls()
    data = {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'local_certificates': list(certificates.values()), 'rayleigh_rows': rows,
            'geometry_rows': geometry, 'physical_rows': physical,
            'all_exact_assertions_passed': True,
            'limits': 'Finite local combinatorial certificates and exact physical Gauss/path checks; no rotor truncation, spectral diagonalization, parameter fit, or thermodynamic dynamics test.',
            'elapsed_seconds': time.monotonic()-tick}
    text = json.dumps(data, indent=2, allow_nan=False)+'\n'
    (Path(__file__).parent/'CONTROL_RESULTS.json').write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
