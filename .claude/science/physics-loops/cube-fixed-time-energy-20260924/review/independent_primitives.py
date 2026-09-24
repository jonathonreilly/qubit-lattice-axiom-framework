"""Independent exact controls from charge hops, with no campaign imports.

This finite calculation checks inherited inputs to the analytic fixed-time
argument. It does not simulate or numerically certify an infinite-time limit.
"""
import hashlib
import itertools
import json
from collections import defaultdict
from pathlib import Path

import sympy as sp

A = (0, 3, 5, 6)
B = (1, 2, 4, 7)
edges = tuple((a, b) for a in A for b in B if (a ^ b).bit_count() == 1)
tree = (1, 2, 3, 4, 6, 9, 11)
chords = tuple(e for e in range(len(edges)) if e not in tree)
zero = (0,) * len(chords)

inc = sp.zeros(8, len(edges))
for e, (a, b) in enumerate(edges):
    inc[a, e] = 1
    inc[b, e] = -1
tree_det = int(inc[:7, list(tree)].det())
assert abs(tree_det) == 1

words = []
for occupied in itertools.combinations(range(8), 6):
    for minus in occupied:
        q = tuple(0 if v not in occupied else -1 if v == minus else 1 for v in range(8))
        words.append(q)
grades = [[q for q in words if sum(q[a] == 0 for a in A) == k] for k in range(3)]
indices = [{q: i for i, q in enumerate(qs)} for qs in grades]
assert list(map(len, grades)) == [36, 96, 36]

def outward(q):
    for e, (a, b) in enumerate(edges):
        if q[a] and not q[b]:
            s = q[a]
            new = list(q)
            new[a], new[b] = 0, s
            exponent = list(zero)
            if e in chords:
                exponent[chords.index(e)] = -s
            yield tuple(new), tuple(exponent)

def difference(x, y):
    return tuple(a - b for a, b in zip(x, y))

G = defaultdict(lambda: defaultdict(int))
# FF* through grade zero: pair all outgoing paths from each grade-zero word.
for q in grades[0]:
    hops = [(indices[1][r], n) for r, n in outward(q)]
    for i, ni in hops:
        for j, nj in hops:
            G[i, j][difference(ni, nj)] += 1
# -F*F through grade two: pair incoming paths to each grade-two word.
incoming = defaultdict(list)
for j, q in enumerate(grades[1]):
    for r, n in outward(q):
        incoming[r].append((j, n))
for hops in incoming.values():
    for i, ni in hops:
        for j, nj in hops:
            G[i, j][difference(nj, ni)] -= 1
G = {ij: {n: c for n, c in poly.items() if c} for ij, poly in G.items()}
G = {ij: poly for ij, poly in G.items() if poly}

dark = []
bright = []
for i, q in enumerate(grades[1]):
    vacancies = tuple(v for v in range(8) if not q[v])
    destination = bright if (vacancies[0] ^ vacancies[1]).bit_count() == 1 else dark
    destination.append(i)
assert (len(bright), len(dark)) == (72, 24)
dark_set = set(dark)
assert not any(i in dark_set and j in dark_set for i, j in G)

def evaluate(first_chord_minus):
    m = sp.zeros(96)
    for (i, j), poly in G.items():
        m[i, j] = sum(c * (-1 if first_chord_minus and n[0] % 2 else 1) for n, c in poly.items())
    assert m == m.T
    return m

witness = evaluate(True)
Q = witness.extract(bright, dark)
gram_det = int((Q.T * Q).det())
assert gram_det > 0
flat = evaluate(False)
Qflat = flat.extract(bright, dark)
rank_flat = Qflat.rank()
assert rank_flat == 23
u = sp.zeros(96, 1)
for i in dark:
    u[i] = 1
assert flat * u == sp.zeros(96, 1)

def clean(state):
    return {key: v for key, v in state.items() if v}

def F(state, inward=False, center=None):
    answer = defaultdict(int)
    for (q, field), amplitude in state.items():
        for e, (a, b) in enumerate(edges):
            if center is not None and a != center:
                continue
            source, target = (b, a) if inward else (a, b)
            if not q[source] or q[target]:
                continue
            sign = q[source]
            newq, newe = list(q), list(field)
            newq[source], newq[target] = 0, sign
            newe[e] += sign if inward else -sign
            answer[(tuple(newq), tuple(newe))] += amplitude
    return clean(answer)

def birth(state, signs):
    answer = defaultdict(int)
    for (q, field), amplitude in state.items():
        if q[0] or q[1]:
            continue
        for sign in signs:
            newq, newe = list(q), list(field)
            newq[0], newq[1] = sign, -sign
            newe[0] += sign
            answer[(tuple(newq), tuple(newe))] += amplitude
    return clean(answer)

def norm_squared(state):
    return sum(v * v for v in state.values())

def gauss_ok(key):
    q, field = key
    return inc * sp.Matrix(field) == sp.Matrix([q[v] - int(v in A) for v in range(8)])

omega = {(tuple(int(v in A) for v in range(8)), (0,) * 12): 1}
mark_results = {}
for label, signs in (('resolved_plus', (1,)), ('resolved_minus', (-1,)), ('coherent', (1, -1))):
    bi = birth(F(omega), signs)
    ri = {key: -amplitude for key, amplitude in F(bi, center=0).items()}
    assert all(gauss_ok(key) for key in (*bi, *ri))
    assert all(sum(field[e] * (field[e] - q[a]) for e, (a, b) in enumerate(edges) if not q[b]) == 0 for q, field in bi)
    assert all(tuple(v for v in range(8) if not q[v]) == (0, 7) for q, field in ri)
    g = defaultdict(int, F(F(ri, inward=True)))
    for key, value in F(F(ri), inward=True).items():
        g[key] -= value
    g = clean(g)
    loss = sum(2 * value * value for (q, field), value in g.items() if any(not q[a] and not q[b] for a, b in edges))
    mark_results[label] = {'b': norm_squared(bi), 'r': norm_squared(ri), 'G_R_norm_squared': norm_squared(g), 'Gamma_G_R_norm_squared': loss, 'B_support': len(bi), 'R_support': len(ri)}
assert [(r['b'], r['r'], r['Gamma_G_R_norm_squared']) for r in mark_results.values()] == [(2, 4, 96), (2, 2, 48), (4, 6, 144)]

# Perturbing the consequential relative sign destroys the dark cancellation.
wrong_diagonal = {}
for i in dark:
    q = grades[1][i]
    wrong_diagonal[i] = sum(1 for _ in outward(q)) + sum(1 for q0 in grades[0] for r, _ in outward(q0) if r == q)
assert all(v == 6 for v in wrong_diagonal.values())

result = {
    'implementation': 'Independent charge-hop and physical-field dictionaries; no imported repo builders or runners.',
    'edge_order': edges,
    'tree_edge_indices': tree,
    'chord_edge_indices': chords,
    'reduced_tree_incidence_determinant': tree_det,
    'charge_grade_dimensions': list(map(len, grades)),
    'bright_dark_dimensions': [len(bright), len(dark)],
    'dark_block_nonzero_Laurent_entries': 0,
    'witness_Gram_determinant': gram_det,
    'flat_Q_rank': rank_flat,
    'flat_dark_constant_vector_annihilated': True,
    'physical_mark_coefficients': mark_results,
    'wrong_relative_sign_dark_diagonal': sorted(set(wrong_diagonal.values())),
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_name('PRIMITIVE_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
print('All exact assertions completed. No infinite-time numerical conclusion is asserted.')
