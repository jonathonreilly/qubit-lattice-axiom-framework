"""Personal checks of complete resource sums and live-register signs.

Direct determinant jets provide the derivative comparator. CAR cross-minor
identities are separately checked in the preceding runners. The block Schur
bound is challenged with finite operator blocks; no physical graph sum is
certified here.
"""
import itertools
import json
import math
from pathlib import Path
import numpy as np
from block2_cofactor_cyclic_check import parity, compositions


def jet_product(a, b):
    out = np.zeros_like(a)
    for i in range(len(a)):
        for j in range(len(b)):
            if not (i & j):
                out[i | j] += a[i]*b[j]
    return out


def direct_jet(s, footprints, edges):
    size = 2**len(edges)
    result = np.zeros(size); result[0] = 1.
    pair_index = {tuple(sorted(e)):k for k, e in enumerate(edges)}
    for resource in set().union(*footprints):
        members = [i for i, a in enumerate(footprints) if resource in a]
        det = np.zeros(size)
        for perm in itertools.permutations(members):
            term = np.zeros(size); term[0] = parity(perm)
            for i, j in zip(members, perm):
                factor = np.zeros(size); factor[0] = s[i, j]
                e = pair_index.get(tuple(sorted((i, j))))
                if e is not None and i != j:
                    factor[1 << e] = 1.
                term = jet_product(term, factor)
            det += term
        result = jet_product(result, det)
    return result[-1]


def assigned_live_value(s, footprints, oriented, resources, order, omit_crossing=False):
    pos = {v:i for i, v in enumerate(order)}
    first = [min(pos[r], pos[c]) for r, c in oriented]
    last = [max(pos[r], pos[c]) for r, c in oriented]
    sign = 1
    selected_rows, selected_columns = {}, {}
    for v in order:
        active = [e for e in range(len(oriented)) if first[e] < pos[v] <= last[e]]
        sign *= (-1)**sum(resources[e] in footprints[v] for e in active)
        for e, (r, c) in enumerate(oriented):
            if v in (r, c) and resources[e] not in footprints[v]:
                return 0.
            if r == v:
                key = (v, resources[e])
                if key in selected_rows:
                    return 0.
                selected_rows[key] = True
            if c == v:
                key = (v, resources[e])
                if key in selected_columns:
                    return 0.
                selected_columns[key] = True
        if not omit_crossing:
            for e, f in itertools.combinations(range(len(oriented)), 2):
                if max(first[e], first[f]) != pos[v] or resources[e] != resources[f]:
                    continue
                r, c = oriented[e]; r2, c2 = oriented[f]
                if (pos[r]-pos[r2])*(pos[c]-pos[c2]) < 0:
                    assert max(first[e], first[f]) <= min(last[e], last[f])
                    sign *= -1
    value = float(sign)
    for u in set().union(*footprints):
        members = [v for v in order if u in footprints[v]]
        row = [v for v in members if (v, u) not in selected_rows]
        col = [v for v in members if (v, u) not in selected_columns]
        assert len(row) == len(col)
        value *= np.linalg.det(s[np.ix_(row, col)])
    return value


def register_sum(s, footprints, edges, order, omit_crossing=False):
    universe = sorted(set().union(*footprints))
    value = 0.
    for choices in itertools.product([0, 1], repeat=len(edges)):
        oriented = [e[::-1] if reverse else e for e, reverse in zip(edges, choices)]
        for resources in itertools.product(universe, repeat=len(edges)):
            value += assigned_live_value(s, footprints, oriented, resources, order, omit_crossing)
    return value


def block_schur_challenge(rng):
    results = []
    for a, start, end in [(1,2,1),(2,2,1),(3,1,2),(4,0,2)]:
        rows, cols, dimension = a**end, a**start, 3
        blocks = np.zeros((rows*dimension, cols*dimension))
        for i in range(rows):
            for j in range(cols):
                b = rng.normal(size=(dimension, dimension))+1j*rng.normal(size=(dimension, dimension))
                b = b/np.linalg.norm(b,2)
                # Store real contractions too; complex scalar phases have no norm cost.
                b = b.real
                blocks[i*dimension:(i+1)*dimension,j*dimension:(j+1)*dimension] = b
        actual = np.linalg.norm(blocks,2)
        bound = a**((start+end)/2)
        assert actual <= bound+1e-12
        results.append(dict(footprint_size=a, starts=start, ends=end, norm=float(actual), bound=float(bound)))
    return results


def main():
    rng = np.random.default_rng(515959)
    n = 4
    vectors = rng.normal(size=(n,n)); vectors /= np.linalg.norm(vectors,axis=0)
    s = vectors.T@vectors
    graphs = [[(0,1)],[(0,1),(1,2)],[(0,1),(0,2),(0,3)],
              [(0,1),(1,2),(2,3)],[(0,2),(1,3)]]
    family = [set(),{0},{1},{0,1}]
    max_error = wrong_gap = 0.
    cases = 0
    for sample in range(40):
        footprints = [family[rng.integers(4)] for _ in range(n)]
        for graph in graphs:
            reference = direct_jet(s, footprints, graph)
            for order in [list(range(n)),[1,2,3,0],[3,1,0,2],list(rng.permutation(n))]:
                actual = register_sum(s, footprints, graph, order)
                max_error = max(max_error, abs(actual-reference))
                wrong_gap = max(wrong_gap, abs(register_sum(s, footprints, graph, order, True)-reference))
                cases += 1
    assert max_error < 2e-12
    assert wrong_gap > .1
    configurations = np.array(list(itertools.product(range(4), repeat=n)))
    matrix = rng.normal(size=(4,4)); j = (matrix+matrix.T)/20
    rho = np.linalg.norm(j,2)
    source = np.array([0.,-.4+.1j,.8,1.2-.3j])
    s4 = np.trace(np.diag(abs(source)**4)@j@j)
    phases = np.exp(1j*rng.normal(size=(n,4)))
    epsilon = math.log(2)
    checks = []
    for graph in graphs:
        degrees = [sum(i in edge for edge in graph) for i in range(n)]
        constant = (2*epsilon)**(-len(graph))*math.sqrt(math.prod(math.factorial(d) for d in degrees))
        coefficient = []
        for conf in configurations:
            footprints = [family[a] for a in conf]
            derivative = direct_jet(s, footprints, graph)
            normalized = derivative*math.exp(-(math.log(2)+epsilon)*sum(map(len,footprints)))
            coefficient.append(normalized*np.prod([j[conf[i],conf[(i+1)%n]]*phases[i,conf[i]] for i in range(n)]))
        coefficient = np.array(coefficient)
        values = []
        for powers in compositions(4,n):
            marks = np.prod(source[configurations]**np.array(powers)[None,:],axis=1)
            values.append(abs(coefficient@marks))
        bound = constant*rho**(n-2)*s4
        assert max(values) <= bound+1e-13
        checks.append(dict(edges=graph,degrees=degrees,source_distributions=len(values),
                           maximum_value=float(max(values)),bound=float(bound),ratio=float(max(values)/bound)))
    result = dict(status='finite_author_checks_passed',independent_review=False,
                  live_register_derivative_cases=cases,maximum_identity_error=float(max_error),
                  omitted_matching_sign_gap=float(wrong_gap),
                  block_schur_checks=block_schur_challenge(rng),source_checks=checks,
                  limitations=['generic finite component labels and Gram matrix','shared parity and composition helpers',
                               'complete resource sum for a prescribed derivative graph only',
                               'no all-graph or physical activity-one convergence'])
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
