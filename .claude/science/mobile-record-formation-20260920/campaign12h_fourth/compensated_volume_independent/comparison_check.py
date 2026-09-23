"""Source-bound post-PRE checks; no author scientific-builder imports.

The new decisive reconstruction is an external-plaquette electric phase and
an off-diagonal field Gram check. Finite support overlaps are reassembled
independently for two selected author geometries.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import sympy as sp


BASE = Path(__file__).resolve().parent
ROOT = BASE.parent
AUTHOR = ROOT/'compensated_volume_author'


def bind(path):
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def authenticate():
    seal_path = AUTHOR/'AUTHOR_SEAL.json'
    assert bind(seal_path)['sha256'] == '5da6ab8a81e7f6442a3c63ece190e9119b3c2cdd00c9960465bc01cc963d1f7f'
    seal = json.loads(seal_path.read_text())
    author_rows = seal['sources'] + seal['artifacts']
    for row in author_rows:
        assert bind(Path(row['path'])) == row
    draft_path = AUTHOR/'ANALYTIC_DRAFT_SEAL.json'
    draft = json.loads(draft_path.read_text())
    for row in [draft['artifact']] + draft['sources']:
        assert bind(Path(row['path'])) == row
    pre_path = BASE/'PRE_COMPARISON_SEAL.json'
    assert bind(pre_path)['sha256'] == '6e8bae143d8ee1e0c77c57461c8025143b660709ff89e42c5c072a38d2164d0f'
    pre = json.loads(pre_path.read_text())
    for row in pre['sources'] + pre['artifacts']:
        assert bind(Path(row['path'])) == row
    assert (AUTHOR/'LOCAL_CONTROL.stdout.log').read_bytes() == (AUTHOR/'LOCAL_SUPPORT_BIRTH_RESULTS.json').read_bytes()
    assert (AUTHOR/'LOCAL_CONTROL.stderr.log').read_bytes() == b''
    receipt = json.loads((AUTHOR/'LOCAL_CONTROL_RECEIPT.json').read_text())
    assert receipt['exit_code'] == 0
    assert receipt['runner_sha256'] == bind(AUTHOR/'local_support_and_birth_check.py')['sha256']
    results = json.loads((AUTHOR/'LOCAL_SUPPORT_BIRTH_RESULTS.json').read_text())
    assert results['source_sha256'] == receipt['runner_sha256']
    return {'author_seal': bind(seal_path), 'author_seal_rows_verified': len(author_rows),
            'author_unique_row_paths': len({row['path'] for row in author_rows}),
            'analytic_seal': bind(draft_path), 'analytic_bindings_verified': 1+len(draft['sources']),
            'PRE': bind(pre_path), 'PRE_bindings_verified': len(pre['sources'])+len(pre['artifacts']),
            'author_stdout_equals_results': True, 'author_stderr_empty': True,
            'author_command_receipt_present': True, 'source_rows': author_rows}


def adjacent(x):
    for j in range(len(x)):
        for s in (-1, 1):
            v = list(x)
            v[j] += s
            yield tuple(v)


def make_box(d, low, high):
    vertices = tuple(product(range(low, high), repeat=d))
    present = set(vertices)
    aa = tuple(x for x in vertices if sum(x) % 2 == 0)
    # Bipartite orientations, deliberately different from the author's
    # lexicographic positive-coordinate link convention.
    edges = tuple((a, b) for a in aa for b in adjacent(a) if b in present)
    return vertices, aa, edges


def loop_field(cycle, amplitude, edges):
    index = {e: i for i, e in enumerate(edges)}
    electric = [sp.Integer(0)]*len(edges)
    for x, y in zip(cycle, cycle[1:]+cycle[:1]):
        oriented = (x, y) if sum(x) % 2 == 0 else (y, x)
        electric[index[oriented]] += amplitude if oriented == (x, y) else -amplitude
    return tuple(electric)


def physical(q, electric, vertices, aa, edges):
    div = dict.fromkeys(vertices, sp.Integer(0))
    for value, (a, b) in zip(electric, edges):
        div[a] += value
        div[b] -= value
    return all(sp.expand(div[x]-q[x]+int(x in aa)) == 0 for x in vertices)


def energy(q, electric, edges):
    return sp.expand(sum((1-q[b]**2)*value*(value-q[a])
                         for value, (a, b) in zip(electric, edges)))


def one_path(q0, electric0, a, marked_b, old_b, sigma, edges):
    index = {edge: i for i, edge in enumerate(edges)}
    assert q0[a] and q0[marked_b] == q0[old_b] == 0 and marked_b != old_b
    q = dict(q0)
    old_q = q[a]
    q[a], q[marked_b], q[old_b] = sigma, -sigma, old_q
    electric = list(electric0)
    electric[index[(a, old_b)]] -= old_q
    electric[index[(a, marked_b)]] += sigma
    return q, tuple(electric)


def all_paths(q, electric, a, b, sigma, vertices, edges):
    output = Counter()
    for source, old_b in edges:
        if source != a or old_b == b or q[old_b] or q[b]:
            continue
        qq, ee = one_path(q, electric, a, b, old_b, sigma, edges)
        output[(tuple(qq[x] for x in vertices), ee)] += 1
    return output


def gram(vectors):
    return [[sum(v.get(x, 0)*w.get(x, 0) for x in set(v)|set(w)) for w in vectors]
            for v in vectors]


def external_phase_and_gram():
    vertices, aa, edges = make_box(2, -2, 4)
    q = {x: int(x in aa) for x in vertices}
    a, b, c = (0, 0), (1, 0), (0, 1)
    cycle = ((1, 0), (2, 0), (2, 1), (1, 1))
    m = sp.Symbol('m', integer=True)
    electric = loop_field(cycle, m, edges)
    assert physical(q, electric, vertices, aa, edges)
    assert all(electric[i] == 0 for i, (x, y) in enumerate(edges) if x == a)
    initial_D = energy(q, electric, edges)
    rows = []
    for sigma in (-1, 1):
        qq, ee = one_path(q, electric, a, b, c, sigma, edges)
        assert physical(qq, ee, vertices, aa, edges)
        final_D = energy(qq, ee, edges)
        assert initial_D == 4*m*m and final_D == 2*m*m
        rows.append({'sigma': sigma, 'input_D': str(initial_D), 'output_D': str(final_D),
                     'interaction_picture_phase_exponent_divided_by_iKt': str(sp.expand(final_D-initial_D))})
    input_fields = [loop_field(cycle, n, edges) for n in (-2, 0, 1, 3)]
    plus = [all_paths(q, ee, a, b, 1, vertices, edges) for ee in input_fields]
    minus = [all_paths(q, ee, a, b, -1, vertices, edges) for ee in input_fields]
    coherent = [v+w for v, w in zip(plus, minus)]
    expected = [[3*int(i == j) for j in range(4)] for i in range(4)]
    assert gram(plus) == gram(minus) == expected
    assert gram(coherent) == [[2*x for x in row] for row in expected]
    cross = [[sum(v.get(x, 0)*w.get(x, 0) for x in set(v)|set(w)) for w in minus] for v in plus]
    assert cross == [[0]*4 for _ in range(4)]
    return {'orientation': 'all links A to B', 'external_cycle': cycle,
            'same_original_star_input_data_for_all_m': True, 'phase_rows': rows,
            'tested_normalizable_field_basis_circulations': [-2, 0, 1, 3],
            'resolved_Gram': gram(plus), 'coherent_Gram': gram(coherent),
            'plus_minus_cross_Gram': cross,
            'operator_scope': 'The full initial-sector identity follows analytically from distinct occupied B destinations and unit rotor translations; this matrix tests off-diagonal field inputs.'}


def support_overlap(d, side):
    vertices, aa, edges = make_box(d, 0, side)
    es = {e: {('v', e[0]), ('v', e[1]), ('e', e[0], e[1])} for e in edges}
    stars = {a: {('v', a)} | {cell for e in edges if e[0] == a for cell in es[e]} for a in aa}
    neighborhoods = {a: {b for x, b in edges if x == a} for a in aa}
    pairs = [(a, c) for a, c in combinations(aa, 2) if neighborhoods[a] & neighborhoods[c]]
    originals = [('pair', stars[a] | stars[c]) for a, c in pairs]
    originals += [('birth', stars[a]) for a, b in edges]
    dressed = []
    for kind, support in originals:
        new = set(support)
        for electric_support in es.values():
            if support & electric_support:
                new |= electric_support
        dressed.append(new)
    overlap = max(sum(bool(x & y) for y in dressed) for x in dressed)
    expected = next(row for row in json.loads((AUTHOR/'LOCAL_SUPPORT_BIRTH_RESULTS.json').read_text())['support_geometry']
                    if row['d'] == d and row['side_length'] == side)
    assert overlap == expected['max_actual_term_overlap']
    assert len(pairs) == expected['pair_terms'] and len(edges) == expected['edges']
    return {'d': d, 'side': side, 'pair_terms': len(pairs), 'birth_edge_terms': len(edges),
            'maximum_indexed_term_overlap': overlap, 'agrees_with_author_selected_case': True}


if __name__ == '__main__':
    output = {
        'authentication': authenticate(),
        'new_external_phase_and_Gram_control': external_phase_and_gram(),
        'selected_independent_overlap_reconstructions': [support_overlap(2, 4), support_overlap(3, 4)],
        'fixed_perturbation_time_topology': {
            'proof': 'For fixed terminal A_t=alpha_t(A), V(0,t)A_t-A_t=int_0^t V(0,s) L_I(s) A_t ds. Only terms meeting its uniformly finite support contribute. Thus ||T_t(A)-alpha_t(A)|| <= t ||A|| sum_(Z meeting Xplus) sup_s||ell_Z(s)||cb, uniformly in volume. No global perturbation norm or norm-continuous rotor coefficients are used.',
            'consequence': 'The Wilson-loop norm lower bound is 2-C_W t_m for every fixed bounded local Hamiltonian/birth perturbation, so the obstruction remains.',
            'method': 'analytic reconstruction, not a finite matrix simulation'},
        'F1': {'scope': 'Section 5 final topology paragraph',
               'finding': 'A locally normal representation does not restore norm time continuity on the same full local algebra.',
               'requested_change': 'Separate the possible smaller invariant regular algebra for norm continuity from locally normal representations for strong/weak statewise continuity.'},
        'author_runner_executed': False,
        'new_author_or_prior_scientific_files_changed': False,
    }
    target = BASE/'COMPARISON_RESULTS.json'
    if target.exists():
        raise FileExistsError(target)
    target.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({'status': 'passed',
                      'author_bindings_verified': output['authentication']['author_seal_rows_verified'],
                      'PRE_bindings_verified': output['authentication']['PRE_bindings_verified'],
                      'selected_overlap_counts': [row['maximum_indexed_term_overlap'] for row in output['selected_independent_overlap_reconstructions']],
                      'phase_shift_over_iKt': '-2*m**2',
                      'required_scope_correction': 'F1', 'output': str(target)}, indent=2))
