#!/usr/bin/env python3
"""Selective post-seal source/receipt comparison, not an author-suite replay."""
from pathlib import Path
import datetime, hashlib, importlib.util, json, sys
import sympy as sp
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
RAW = HERE.parent

def identity(p):
    b = p.read_bytes()
    return {"path": str(p), "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}

def module(name, p):
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def load(p):
    return json.loads(p.read_text())

def frozen_preseal():
    seal = load(HERE / 'PRE_COMPARISON_SEAL.json')
    for row in seal['artifacts']:
        assert identity(Path(row['path'])) == row
    return identity(HERE / 'PRE_COMPARISON_SEAL.json')

def full_generator_clock(own, n, edges, beta, svalue):
    """Assemble one transient growing chain, rather than recursive stage kernels."""
    layers = [own.old.matchings(n, edges, j) for j in range(n // 2 + 1)]
    states = sum(layers[:-1], [])
    full = layers[-1]
    where = {M: i for i, M in enumerate(states)}
    terminal = {M: i for i, M in enumerate(full)}
    Q = sp.zeros(len(states))
    A = sp.zeros(len(states), len(full))
    adj = own.old.neighbors(n, edges)
    for M, i in where.items():
        for _, T in own.old.actions(n, adj, M):
            Q[i, i] += 1
            Q[i, where[T]] -= 1
        occupied = {x for e in M for x in e}
        for e in edges:
            if not occupied.intersection(e):
                T = own.canon((*M, e))
                Q[i, i] += beta
                if T in terminal:
                    A[i, terminal[T]] += beta
                else:
                    Q[i, where[T]] -= beta
    empty = where[()]
    assert Q * sp.ones(len(states), 1) == A * sp.ones(len(full), 1)
    mean = Q.inv() * sp.ones(len(states), 1)
    transform = (Q + beta * svalue * sp.eye(len(states))).inv() * A
    return sp.factor(beta * mean[empty]), sp.factor(sum(transform[empty, :]))

def main():
    preseal = frozen_preseal()
    own = module('sealed_all_stage_independent', HERE / 'independent_check.py')
    author = module('postseal_author_all_stage', RAW / 'geometric_all_stage_check.py')
    result = load(RAW / 'geometric_all_stage_checks/RESULTS.json')
    source_rows = []
    for name, digest in result['sources_sha256'].items():
        row = identity(RAW / name)
        assert row['sha256'] == digest
        source_rows.append(row)
    groups = {r['group']: r for r in result['rows']}
    assert set(groups) == {'connectivity', 'counting', 'clock', 'comparison'}
    for name, row in groups.items():
        assert row['pass'] is True
        assert {k: v for k, v in row.items() if k != 'group'} == load(
            RAW / 'geometric_all_stage_checks' / (name + '.json'))
    conn = groups['connectivity']
    assert conn['graphs'] == len(conn['rows']) == 42
    assert conn['marked_paths'] == sum(r['replayed'] for r in conn['rows']) == 8330
    for row in conn['rows']:
        n = row['vertices']; edges = set(map(tuple, row['edges']))
        counts = [len(own.old.matchings(n, edges, j)) for j in range(n // 2 + 1)]
        assert counts == row['cardinality_counts']
        assert row['replayed'] == sum(counts[:-1]) and counts[-1] > 0
    counting = groups['counting']
    assert counting['graphs'] == sum(r['graphs'] for r in counting['rows']) == 24333
    assert counting['injective_triples'] == sum(r['injective_triples'] for r in counting['rows']) == 2291317
    prelim = load(RAW / 'geometric_corridor_transport_checks/RESULTS.json')
    assert prelim['source_sha256'] == identity(RAW / 'geometric_corridor_transport_check.py')['sha256']
    assert prelim['graphs'] == len(prelim['rows']) == 842
    assert prelim['parent_pairs'] == sum(sum(r['ordered_parent_pairs_by_cardinality'].values()) for r in prelim['rows']) == 115062
    for row in prelim['rows']:
        assert row['longest_route'] <= row['route_bound'] == row['vertices'] - 2
        assert row['largest_reference_multiplicity'] <= 2 * (row['edges'] + row['edges'] ** 2)
    log = (RAW / 'GEOMETRIC_ALL_STAGE_RUN.log').read_text().splitlines()
    assert log[-1] == 'PASS: four complete all-stage control groups'
    assert (RAW / 'GEOMETRIC_ALL_STAGE_RUN.stderr').read_bytes() == b''
    events = [json.loads(x) for x in log[:-1]]
    assert [x['group'] for x in events if x.get('passed')] == list(groups)
    assert [{k: v for k, v in x.items() if k != 'group'} for x in events if x['group'] == 'counting_progress'] == counting['rows']

    # Independent matrix and immutable-record replay comparison on selected cases.
    matrix_rows = []
    cases = [('path4', 4, {(0, 1), (1, 2), (2, 3)}),
             ('cycle4', 4, {(0, 1), (1, 2), (2, 3), (0, 3)}),
             ('odd_barbell', 6, {(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5), (2, 3)})]
    for name, n, edges in cases:
        layers, Ls, As = author.matrices(n, edges)
        replayed = 0
        for j, layer in enumerate(layers[:-1]):
            independently_ordered = [own.canon(M) for M in layer]
            assert set(independently_ordered) == set(own.old.matchings(n, edges, j))
            L, _ = own.graph_laplacian(n, edges, independently_ordered)
            A = sp.Matrix([[int(set(M) < set(T)) for T in layers[j + 1]] for M in layer])
            assert L == Ls[j] and A == As[j]
            for M in layer:
                target, ops = author.align_to_reference(n, edges, M, layers[-1][0])
                state = own.Marked(n, own.old.neighbors(n, edges), own.canon(M))
                before = state.labels.copy()
                for op in ops:
                    state.slide(op)
                assert state.M == own.canon(target)
                for a, b, c in reversed(ops):
                    state.slide((c, b, a))
                assert state.M == own.canon(M) and state.labels == before
                replayed += 1
        matrix_rows.append({'graph': name, 'layers_exactly_compared': len(Ls), 'author_paths_independently_replayed': replayed})
    edges = {(x, x + 1) for x in range(9)}
    T = frozenset({(0, 1), (8, 9)})
    ops = author.c.transport(10, edges, T, (0, 1), (8, 9))
    state = own.Marked(10, own.old.neighbors(10, edges), ((8, 9),))
    for op in ops:
        state.slide(op)
    assert len(ops) == 8 and state.M == ((0, 1),)

    clock_cases = {
        'cycle4': (4, {(0, 1), (1, 2), (2, 3), (0, 3)}),
        'paw4': (4, {(0, 1), (1, 2), (0, 2), (2, 3)}),
        'cycle6': (6, {(x, (x + 1) % 6) if x < (x + 1) % 6 else ((x + 1) % 6, x) for x in range(6)}),
        'irregular6': (6, {(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 2), (1, 4), (2, 5)})}
    exact_clock_rows = []
    for row in groups['clock']['rows']:
        n, edges = clock_cases[row['graph']]
        beta = sp.Rational(row['beta'])
        mean, transform = full_generator_clock(own, n, edges, beta, sp.Rational(7, 5))
        assert mean == sp.Rational(row['scaled_exact_mean'])
        assert transform == sp.Rational(row['exact_laplace'])
        exact_clock_rows.append({'graph': row['graph'], 'beta': row['beta'], 'complete_generator_mean_and_transform_equal': True})
    assert len(exact_clock_rows) == 12
    assert frozen_preseal() == preseal
    output = {
        'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'precomparison_seal': preseal,
        'source_bindings': source_rows,
        'authentication': {'all_four_group_files_equal_combined_result': True,
                           'author_connectivity_graph_inventories_reconstructed': 42,
                           'author_marked_paths_receipt_count_only': 8330,
                           'author_exhaustive_injections_receipt_count_only': 2291317,
                           'preliminary_corridor_graphs_receipt_count_only': 842,
                           'preliminary_ordered_paths_receipt_count_only': 115062,
                           'run_log_agrees_and_stderr_empty': True},
        'selective_independent_recomputations': {'matrix_and_marked_route_cases': matrix_rows,
                                               'path10_empty_corridor_length': len(ops),
                                               'complete_transient_generator_clock_rows': exact_clock_rows},
        'coverage_limit': 'Author exhaustive suites were not rerun. Authenticated stored counts are distinct from the selective independent recomputations and pre-seal proof/controls.',
        'failed_attempts': []}
    (HERE / 'AUTHOR_COMPARISON_RESULTS.json').write_text(json.dumps(output, indent=2) + '\n')
    print('Authenticated all author source/result/log bindings; 42 inventories, selected matrices/routes, and 12 exact full-generator clock rows agree.')

if __name__ == '__main__':
    main()
