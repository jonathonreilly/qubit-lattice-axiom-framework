"""Personal exact flat-magnetic controls; no field or flux truncation claim."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import argparse
import hashlib
import json
import time

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh


def graph(side):
    vertices = list(product(range(side), repeat=3))
    left = [v for v in vertices if sum(v) % 2 == 0]
    right = [v for v in vertices if sum(v) % 2 == 1]
    neighbors = {}
    for v in vertices:
        ns = set()
        for axis in range(3):
            for step in (-1, 1):
                w = list(v)
                w[axis] = (w[axis] + step) % side
                ns.add(tuple(w))
        neighbors[v] = sorted(ns)
    pairs = sorted({tuple(sorted((a, c))) for b in right
                    for a, c in combinations(neighbors[b], 2)})
    records = []
    near = defaultdict(set)
    for index, (a, c) in enumerate(pairs):
        assignments = Counter(tuple(sorted((u, v))) for u in neighbors[a]
                              for v in neighbors[c] if u != v)
        vacuum = 2 * sum(m*m for m in assignments.values())
        records.append((a, c, assignments, vacuum))
        for b in set(neighbors[a]) | set(neighbors[c]):
            near[b].add(index)
    return vertices, left, right, neighbors, records, near


def local_delta_row(x, records, near):
    """Q_occ minus its empty-B scalar, with exact integer path weights."""
    x = tuple(sorted(x))
    occupied = set(x)
    row = Counter()
    for index in sorted(near[x[0]] | near[x[1]]):
        _, _, assignments, vacuum = records[index]
        row[x] -= vacuum
        for d, multiplicity in assignments.items():
            if occupied.intersection(d):
                continue
            intermediate = tuple(sorted(x + d))
            for returning in combinations(intermediate, 2):
                reverse = assignments.get(returning, 0)
                if reverse:
                    final = tuple(b for b in intermediate if b not in returning)
                    assert len(final) == 2
                    row[final] += 2*multiplicity*reverse
    return {key: value for key, value in row.items() if value}


def canonical_displacement(x, side):
    d = tuple((b-a) % side for a, b in zip(*x))
    opposite = tuple((-a) % side for a in d)
    return min(d, opposite)


def rational(x):
    return {'numerator': x.numerator, 'denominator': x.denominator,
            'float_diagnostic': float(x)}


def quotient(side):
    vertices, left, right, neighbors, records, near = graph(side)
    origin = right[0]
    displacements = sorted({min(d, tuple((-x) % side for x in d))
                            for d in vertices if sum(d) % 2 == 0 and any(d)})
    indices = {d: i for i, d in enumerate(displacements)}
    weights = [len(right)//2 if d == tuple((-x) % side for x in d)
               else len(right) for d in displacements]
    assert sum(weights) == len(right)*(len(right)-1)//2
    rows = []
    for d in displacements:
        x = (origin, tuple((a+b) % side for a, b in zip(origin, d)))
        local = local_delta_row(x, records, near)
        row = Counter()
        for y, value in local.items():
            row[indices[canonical_displacement(y, side)]] += value
        rows.append({j: value for j, value in sorted(row.items()) if value})
    for i, row in enumerate(rows):
        for j, value in row.items():
            assert i == j or value >= 0
            assert weights[i]*value == weights[j]*rows[j].get(i, 0), (side, i, j)
    # The quotient acts on orbit-constant amplitudes, not normalized orbit kets.
    rr, cc, vv = [], [], []
    for i, row in enumerate(rows):
        for j, value in row.items():
            rr.append(i); cc.append(j)
            vv.append(value*np.sqrt(weights[i]/weights[j]))
    symmetric = csr_matrix((vv, (rr, cc)), shape=(len(rows), len(rows)))
    if len(rows) < 4:
        eigenvalues, eigenvectors = np.linalg.eigh(symmetric.toarray())
        value, vector = eigenvalues[-1], eigenvectors[:, -1]
    else:
        values, vectors = eigsh(symmetric, k=1, which='LA', tol=1e-13,
                                v0=np.sqrt(np.array(weights, dtype=float)))
        value, vector = values[0], vectors[:, 0]
    amplitude = np.abs(vector)/np.sqrt(np.array(weights, dtype=float))
    amplitude /= max(amplitude)
    positive = [max(1, int(round(float(x)*10**12))) for x in amplitude]
    shift = max(0, -min(row.get(i, 0) for i, row in enumerate(rows))) + 1
    ratios = []
    for i, row in enumerate(rows):
        assert row.get(i, 0) + shift > 0
        numerator = sum(a*positive[j] for j, a in row.items()) + shift*positive[i]
        ratios.append(Fraction(numerator, positive[i]))
    low, high = min(ratios)-shift, max(ratios)-shift
    assert float(low)-1e-8 <= value <= float(high)+1e-8
    # Exact row-ratio bounds do not assume eigensolver correctness or optimality.
    gap_low, gap_high = -high/4, -low/4
    vacuum = sum(r[3] for r in records)
    if side >= 6:
        assert vacuum == 321*len(vertices)
    if side == 4:
        assert vacuum == 270*len(vertices)
    # Check the translation reduction on actual translated occupancy rows.
    for d in displacements[::max(1, len(displacements)//5)]:
        expected = rows[indices[d]]
        for base in right[::max(1, len(right)//3)]:
            x = (base, tuple((a+b) % side for a, b in zip(base, d)))
            actual = Counter()
            for y, coefficient in local_delta_row(x, records, near).items():
                actual[indices[canonical_displacement(y, side)]] += coefficient
            assert {j: a for j, a in actual.items() if a} == expected
    return {
        'side': side, 'vertices': len(vertices), 'A_sites': len(left),
        'degree': len(neighbors[left[0]]), 'overlapping_A_pairs': len(records),
        'vacuum_flat_H4': -vacuum, 'occupancy_pair_dimension': len(right)*(len(right)-1)//2,
        'full_one_minus_matter_dimension': len(right)*(len(right)-1)//2*(len(left)+2),
        'translation_orbits': len(rows), 'orbit_weights': weights,
        'canonical_displacements': displacements,
        'delta_Q_rows': [[[j, a] for j, a in row.items()] for row in rows],
        'positive_integer_test_vector': positive, 'nonnegative_shift': shift,
        'exact_delta_Q_Perron_interval': {'lower': rational(low), 'upper': rational(high)},
        'proposed_ground_gap_g2_tau_interval': {'lower': rational(gap_low), 'upper': rational(gap_high)},
        'floating_top_delta_eigenvalue': float(value),
        'floating_eigen_residual': float(np.linalg.norm(symmetric@vector-value*vector)),
        'all_weighted_symmetry_and_translation_checks_exact': True,
    }


def full_colored_cube():
    """Direct S* S construction with every one-minus matter word, degree 3."""
    vertices, left, right, neighbors, records, near = graph(2)
    occupancies = list(combinations(right, 2))
    basis = [(x, m) for x in occupancies for m in sorted(left + list(x))]
    q_full = np.zeros((len(basis), len(basis)), dtype=np.int64)
    q_occ = np.zeros((len(occupancies), len(occupancies)), dtype=np.int64)
    for a, c, assignments, _ in records:
        spin_rows = defaultdict(Counter)
        plain_rows = defaultdict(Counter)
        for col, (x, minus) in enumerate(basis):
            for u in neighbors[a]:
                for v in neighbors[c]:
                    if u == v or u in x or v in x:
                        continue
                    y = tuple(sorted(x+(u, v)))
                    moved = u if minus == a else (v if minus == c else minus)
                    spin_rows[(y, moved)][col] += 1
        for col, x in enumerate(occupancies):
            for d, multiplicity in assignments.items():
                if not set(x).intersection(d):
                    plain_rows[tuple(sorted(x+d))][col] += multiplicity
        for rows, matrix in [(spin_rows, q_full), (plain_rows, q_occ)]:
            for row in rows.values():
                for i, vi in row.items():
                    for j, vj in row.items():
                        matrix[i, j] += 2*vi*vj
    # Integer unnormalized embedding: the same amplitude at each minus position.
    embedding = np.zeros((len(basis), len(occupancies)), dtype=np.int64)
    for i, (x, _) in enumerate(basis):
        embedding[i, occupancies.index(x)] = 1
    assert np.array_equal(q_full@embedding, embedding@q_occ)
    vacuum = sum(r[3] for r in records)
    for i, x in enumerate(occupancies):
        local = local_delta_row(x, records, near)
        for j, y in enumerate(occupancies):
            assert int(q_occ[i, j])-(vacuum if i == j else 0) == local.get(y, 0)
    # Constant row sum and positivity give exact spectral radii, independently
    # of the floating eigenvalue diagnostic.
    full_sums = q_full.sum(axis=1)
    occ_sums = q_occ.sum(axis=1)
    assert min(full_sums) == max(full_sums) == min(occ_sums) == max(occ_sums)
    return {'graph': 'simple degree-three cube', 'full_matter_dimension': len(basis),
            'occupancy_dimension': len(occupancies), 'vacuum_flat_H4': -vacuum,
            'exact_one_pair_flat_H4_bottom': -int(full_sums[0]),
            'exact_flat_H4_ground_difference': vacuum-int(full_sums[0]),
            'integer_intertwining_exact': True,
            'full_positive_Q': q_full.tolist(), 'occupancy_positive_Q': q_occ.tolist(),
            'floating_full_top_eigenvalue': float(np.linalg.eigvalsh(q_full)[-1])}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sides', nargs='+', type=int, default=[2, 4, 6, 8])
    parser.add_argument('--output', default='NATIVE_PAIR_RESULTS.json')
    args = parser.parse_args()
    assert all(side >= 2 and side % 2 == 0 for side in args.sides)
    start = time.perf_counter()
    result = {'status': 'Personal controls for an unsealed ground-spectrum proposal; not independent confirmation.',
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'full_colored_cube': full_colored_cube(), 'quotients': []}
    for side in args.sides:
        row = quotient(side)
        result['quotients'].append(row)
        print(json.dumps({k: row[k] for k in ['side', 'vacuum_flat_H4', 'translation_orbits',
              'proposed_ground_gap_g2_tau_interval', 'floating_eigen_residual']}), flush=True)
    result['elapsed_seconds'] = time.perf_counter()-start
    path = Path(args.output)
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'result': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                      'elapsed_seconds': result['elapsed_seconds']}))


if __name__ == '__main__':
    main()
