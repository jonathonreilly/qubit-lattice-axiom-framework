"""Root controls of support, electric-phase scope, and local birth counting.

Exact combinatorics and integer/polynomial field algebra only. These are not a
numerical infinite-volume convergence proof or an independent reconstruction.
"""
from pathlib import Path
from collections import defaultdict
from itertools import product, combinations
import hashlib, json, time
import sympy as sp

D = Path(__file__).resolve().parent


def graph(d, length, offset=0):
    vertices = tuple(product(range(offset, offset+length), repeat=d))
    vs = set(vertices)
    edges = []
    neighbors = defaultdict(list)
    for a in vertices:
        for i in range(d):
            b = tuple(x+int(j == i) for j, x in enumerate(a))
            if b in vs:
                edges.append((a, b))
                neighbors[a].append(b)
                neighbors[b].append(a)
    return vertices, tuple(edges), neighbors


def A(a):
    return sum(a) % 2 == 0


def edge(a, b):
    return tuple(sorted((a, b)))


def vertex_cell(a):
    return ('v', a)


def edge_cell(e):
    return ('e', e[0], e[1])


def electric_support(e):
    return {vertex_cell(e[0]), edge_cell(e), vertex_cell(e[1])}


def star(a, neighbors):
    return {vertex_cell(a)} | {vertex_cell(b) for b in neighbors[a]} | {
        edge_cell(edge(a, b)) for b in neighbors[a]}


def support_controls(d, length):
    vertices, edges, neighbors = graph(d, length)
    ds = [electric_support(e) for e in edges]
    by_cell = defaultdict(list)
    for i, support in enumerate(ds):
        for x in support:
            by_cell[x].append(i)
    pairs = set()
    for b in vertices:
        if not A(b):
            pairs.update(tuple(sorted(p)) for p in combinations(neighbors[b], 2))
    original = [('pair', star(a, neighbors) | star(c, neighbors)) for a, c in sorted(pairs)]
    original += [('birth', star(a if A(a) else b, neighbors)) for a, b in edges]
    dressed = []
    rows = []
    for kind, support in original:
        # Exactly one union over electric terms touching the original support.
        touching = {i for x in support for i in by_cell[x]}
        extended = support | set().union(*(ds[i] for i in touching))
        points = [x[1] for x in extended if x[0] == 'v']
        # Every edge's endpoints are in these supports. On a rectangular
        # incidence graph their diameter is attained by vertex cells.
        diameter = max(2*sum(abs(x-y) for x, y in zip(a, b)) for a in points for b in points)
        assert diameter <= (12 if kind == 'pair' else 8)
        assert all(vertex_cell(x[1]) in extended and vertex_cell(x[2]) in extended
                   for x in extended if x[0] == 'e')
        dressed.append(extended)
        rows.append((kind, len(support), len(extended), diameter))
    by_cell2 = defaultdict(set)
    for i, support in enumerate(dressed):
        for x in support:
            by_cell2[x].add(i)
    overlaps = [len(set().union(*(by_cell2[x] for x in support))) for support in dressed]
    z = 2*d
    bound = z*z*sum(z**k for k in range(17))
    assert max(overlaps) <= bound
    return {'d': d, 'side_length': length, 'vertices': len(vertices), 'edges': len(edges),
            'pair_terms': len(pairs), 'birth_edge_terms': len(edges),
            'max_actual_term_overlap': max(overlaps), 'proved_coarse_overlap_bound': bound,
            'support_rows': {kind: {'maximum_original_cells': max(r[1] for r in rows if r[0] == kind),
                                   'maximum_dressed_cells': max(r[2] for r in rows if r[0] == kind),
                                   'maximum_dressed_incidence_diameter': max(r[3] for r in rows if r[0] == kind)}
                             for kind in ['pair', 'birth']}}


def circulation(cycle, amplitude):
    fields = defaultdict(lambda: sp.Integer(0))
    for a, b in zip(cycle, cycle[1:]+cycle[:1]):
        fields[edge(a, b)] += amplitude if a < b else -amplitude
    return dict(fields)


def div(fields):
    result = defaultdict(lambda: sp.Integer(0))
    for (a, b), value in fields.items():
        result[a] += value
        result[b] -= value
    return {a: sp.expand(v) for a, v in result.items() if sp.expand(v) != 0}


def electric_D(q, fields, edges):
    result = sp.Integer(0)
    for e in edges:
        a, b = e if A(e[0]) else (e[1], e[0])
        if q[b] != 0:
            continue
        E = fields.get(e, 0)
        k = -q[a] if a < b else q[a]
        result += E*(E+k)
    return sp.expand(result)


def mark(q, fields, a, b, c, sigma):
    assert A(a) and q[a] and not q[b] and not q[c] and b != c
    outq = dict(q)
    old = q[a]
    outq[a], outq[b], outq[c] = sigma, -sigma, old
    outE = defaultdict(lambda: sp.Integer(0), fields)
    outE[edge(a, c)] += -old if a < c else old
    outE[edge(a, b)] += sigma if a < b else -sigma
    charge_change = {x: outq[x]-q[x] for x in q if outq[x] != q[x]}
    delta_fields = {e: sp.expand(outE.get(e, 0)-fields.get(e, 0)) for e in set(outE)|set(fields)}
    assert div(delta_fields) == charge_change
    return outq, dict(outE)


def phase_countercontrols():
    vertices, edges, neighbors = graph(2, 6, -2)
    q = {a: int(A(a)) for a in vertices}
    n = sp.Symbol('n', integer=True)
    # A plaquette entirely outside the old A-star links, but meeting its B
    # neighbor. It gives gauge-compatible inputs indistinguishable on that
    # old star and different electric phases for the same birth path.
    a, b, c = (0, 0), (1, 0), (0, 1)
    external_cycle = [(1, 0), (2, 0), (2, 1), (1, 1)]
    fields = circulation(external_cycle, n)
    assert div(fields) == {}
    assert all(edge_cell(e) not in star(a, neighbors) for e in fields)
    outq, outE = mark(q, fields, a, b, c, 1)
    initial = electric_D(q, fields, edges)
    final = electric_D(outq, outE, edges)
    assert initial == 4*n*n and final == 2*n*n
    delta = sp.expand(final-initial)
    assert delta == -2*n*n
    dressed = star(a, neighbors).copy()
    for e in edges:
        if electric_support(e) & star(a, neighbors):
            dressed |= electric_support(e)
    relevant = [e for e in fields if b in e]
    assert all(edge_cell(e) in dressed for e in relevant)
    # The free norm-continuity obstruction is a bounded gauge-invariant W.
    loop = [(0, 0), (1, 0), (1, 1), (0, 1)]
    fn = circulation(loop, n)
    fn1 = circulation(loop, n+1)
    before = electric_D(q, fn, edges)
    after = electric_D(q, fn1, edges)
    difference = sp.expand(after-before)
    assert before == 4*n*n and difference == 8*n+4
    return {'one_shell_enlargement_is_needed': {'initial_D': str(initial), 'after_same_birth_D': str(final),
               'birth_electric_phase_difference': str(delta),
               'external_cycle': external_cycle, 'original_star_inputs_identical': True,
               'all_original_and_output_words_Gauss_compatible': True,
               'changed_external_D_edges_are_in_one_dressed_shell': True},
            'norm_time_continuity_counterexample': {'plaquette_D': str(before),
               'plaquette_translation_energy_difference_over_K': str(difference),
               'times': 'pi/[K(8n+4)], n->infinity',
               'exact_norm_difference_at_these_times': 2,
               'scope': 'State maximizing the norm changes with n; each fixed normal-state expectation remains continuous.'}}


def initial_rates(d):
    vertices, edges, neighbors = graph(d, 6, -2)
    q = {a: int(A(a)) for a in vertices}
    target = (1,)+(0,)*(d-1)
    z = 2*d
    assert len(neighbors[target]) == z
    b_created = 0
    b_transferred = 0
    channels = []
    for a in neighbors[target]:
        assert A(a) and len(neighbors[a]) == z
        for b in neighbors[a]:
            v = {}
            for sigma in [-1, 1]:
                outputs = []
                for c in neighbors[a]:
                    if c == b:
                        continue
                    outq, outE = mark(q, {}, a, b, c, sigma)
                    fingerprint = (tuple(sorted((x, outq[x]-q[x]) for x in q if outq[x] != q[x])),
                                   tuple(sorted((e, E) for e, E in outE.items() if E)))
                    outputs.append(fingerprint)
                    if b == target:
                        b_created += 1
                    elif c == target:
                        b_transferred += 1
                assert len(outputs) == len(set(outputs)) == z-1
                v[sigma] = set(outputs)
            assert not v[-1] & v[1]
            channels.append({'a': a, 'b': b, 'resolved_Gram': z-1, 'coherent_Gram': 2*(z-1)})
    assert b_created == b_transferred == 2*z*(z-1)
    return {'d': d, 'z': z, 'local_B_site': target,
            'rate_into_B_by_newborn_without_kappa': b_created,
            'rate_into_B_by_old_record_transfer_without_kappa': b_transferred,
            'local_B_occupation_initial_derivative_without_kappa': b_created+b_transferred,
            'record_density_per_vertex_initial_derivative_without_kappa': (b_created+b_transferred)//2,
            'single_edge_initial_count_rate_without_kappa': 2*(z-1),
            'resolved_and_coherent_agree_at_initial_instant': True,
            'physical_channels_checked': channels}


def main():
    started = time.monotonic()
    supports = [support_controls(d, length) for d, length in [(2,4),(2,6),(2,8),(3,4),(3,6)]]
    phases = phase_countercontrols()
    rates = [initial_rates(d) for d in [2,3]]
    out = {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'support_geometry': supports, 'electric_phase_controls': phases,
           'local_initial_formation': rates, 'elapsed_seconds': time.monotonic()-started,
           'scope': 'Exact finite geometry and physical polynomial/rate controls. No evolution fit, thermodynamic numerical proof, source derivation or volume-uniform microscopic bound.'}
    p = D/'LOCAL_SUPPORT_BIRTH_RESULTS.json'
    assert not p.exists()
    p.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2), flush=True)


if __name__ == '__main__':
    main()
