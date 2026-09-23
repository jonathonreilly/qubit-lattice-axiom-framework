"""Exact periodic Gauss-compatible dark words; all arithmetic is integral."""
from pathlib import Path
from itertools import product, combinations
from collections import defaultdict
from fractions import Fraction
import json

HERE = Path(__file__).resolve().parent
L = 12

def build(d):
    vertices = list(product(range(L), repeat=d))
    A = [x for x in vertices if sum(x) % 2 == 0]
    B = [x for x in vertices if sum(x) % 2 == 1]
    aset, bset = set(A), set(B)
    neighbors = {}
    for x in vertices:
        nb = []
        for axis in range(d):
            for step in (-1, 1):
                y = list(x)
                y[axis] = (y[axis] + step) % L
                nb.append(tuple(y))
        neighbors[x] = sorted(nb)
    edges = [(a, b) for a in A for b in neighbors[a]]
    E = {e: 0 for e in edges}
    q = {x: int(x in aset) for x in vertices}
    routes = []
    for transverse in product(range(L), repeat=d-1):
        parity = (1 - sum(transverse)) % 2
        chain = [(parity + 2*j, *transverse) for j in range(6)]
        indices = [(1, 2), (4, 5)] if not any(transverse) else [(0, 1), (2, 3), (4, 5)]
        for j, k in indices:
            left, right = chain[j], chain[k]
            a = ((left[0] + right[0]) // 2, *transverse)
            assert a in aset and left in neighbors[a] and right in neighbors[a]
            assert q[a] == 1 and q[left] == q[right] == 0
            # The specified legal old-plus hop and sigma=+ birth route.
            q[left] = 1
            q[right] = -1
            E[(a, left)] = -1
            E[(a, right)] = 1
            routes.append((a, left, right))
    holes = [x for x in B if not q[x]]
    expected_holes = [(1, *([0]*(d-1))), (7, *([0]*(d-1)))]
    assert holes == expected_holes
    def check_gauss(field):
        div = {x: 0 for x in vertices}
        for (a, b), value in field.items():
            div[a] += value
            div[b] -= value
        assert all(div[x] == q[x] - int(x in aset) for x in vertices)
    check_gauss(E)
    distances = [sum(min(abs(x-y), L-abs(x-y)) for x,y in zip(u,v))
                 for u,v in combinations(holes, 2)]
    assert min(distances) == 6
    # Distinct periodic images of the same hole are at distance at least L;
    # these two species and their images have distance at least 6.
    empty_nb = {a: [b for b in neighbors[a] if not q[b]] for a in A}
    assert max(map(len, empty_nb.values())) == 1
    resolved_birth_paths = sum(2*len(empty)*(len(empty)-1) for empty in empty_nb.values())
    assert resolved_birth_paths == 0
    pair_set = set()
    for b in B:
        for a,c in combinations(neighbors[b], 2):
            pair_set.add(tuple(sorted((a,c))))
    double_hop_paths = 0
    for a,c in pair_set:
        double_hop_paths += sum(b != e for b in empty_nb[a] for e in empty_nb[c])
    assert double_hop_paths == 0
    # Therefore every S_ac is zero on the word, not just its expectation.
    D = sum((1-int(q[b] != 0))*field*(field-q[a]) for (a,b),field in E.items())
    assert D == 0
    assert sum(q.values()) == len(A)
    assert sum(value != 0 for value in q.values()) == len(vertices)-2
    assert max(map(abs, E.values())) == 1
    result = dict(dimension=d, period=L, vertices=len(vertices), edges=len(edges),
                  A_count=len(A), B_count=len(B), holes=holes,
                  minimum_periodic_hole_distance=6,
                  max_empty_neighbors_at_A=1,
                  overlapping_A_pairs=len(pair_set),
                  resolved_birth_paths=resolved_birth_paths,
                  overlapping_pair_double_hop_paths=double_hop_paths,
                  all_Gauss_constraints=True, total_charge=sum(q.values()),
                  record_number=sum(value != 0 for value in q.values()), D=D,
                  max_absolute_field=1,
                  B_occupation_density=str(Fraction(len(B)-2,len(B))),
                  record_density_per_vertex=str(Fraction(len(vertices)-2,len(vertices))),
                  vacancy_density_per_vertex=str(Fraction(2,len(vertices))),
                  even_translation_average_terms=len(vertices)//2,
                  specified_legal_routes_from_empty_B=len(routes),
                  route_scope='Basis-word route support only; no assertion about full evolved output or a likely history.',
                  occupied_B_charges=[[list(b),q[b]] for b in B if q[b]],
                  nonzero_fields=[[list(a),list(b),v] for (a,b),v in E.items() if v])
    if d == 2:
        a, hole, c, b = (0,0), (1,0), (1,1), (0,1)
        loop = {(a,hole):1, (c,hole):-1, (c,b):1, (a,b):-1}
        shifted = dict(E)
        for edge,value in loop.items(): shifted[edge] += value
        check_gauss(shifted)
        shifted_D = sum((1-int(q[v] != 0))*field*(field-q[u])
                        for (u,v),field in shifted.items())
        assert shifted_D == 2
        result['dark_oscillation_countercontrol'] = dict(
            base_D=0, shifted_D=2,
            added_physical_plaquette_circulation=[[list(u),list(v),w] for (u,v),w in loop.items()],
            both_words_annihilated_by_all_births_and_pair_terms=True,
            relative_angular_frequency='2 K',
            scope='Finite torus two-word superposition; formation-free does not imply state convergence.')
    return result

results = [build(d) for d in (2,3)]
(HERE / 'PERIODIC_DARK_RESULTS.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps([{k:r[k] for k in ['dimension','vertices','edges','holes',
    'overlapping_A_pairs','resolved_birth_paths','overlapping_pair_double_hop_paths',
    'all_Gauss_constraints','D','max_absolute_field','record_density_per_vertex',
    'vacancy_density_per_vertex']} for r in results], indent=2))
