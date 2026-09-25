"""Read-only independent stored-evidence verifier: no writes, imports or reruns of controls."""
from pathlib import Path
from hashlib import sha256
from collections import defaultdict
from itertools import product
from math import exp, isfinite, sqrt
import json
import subprocess

HERE = Path(__file__).resolve().parent


def read(name):
    return json.loads((HERE / name).read_text())


def observe(path):
    s = path.stat()
    return (sha256(path.read_bytes()).hexdigest(), s.st_size, s.st_mode, s.st_dev,
            s.st_ino, s.st_mtime_ns, s.st_ctime_ns, s.st_nlink)


def matrix(rows):
    out = {(r, c): x for r, c, x in rows}
    assert len(out) == len(rows) and all(out.values())
    return out


def multiply(left, right):
    byrow = defaultdict(list)
    for (r, c), x in right.items():
        byrow[r].append((c, x))
    out = defaultdict(int)
    for (r, k), x in left.items():
        for c, y in byrow[k]:
            out[r, c] += x * y
    return {key: value for key, value in out.items() if value}


def weighted_laplacian(n, A, edges):
    degree = {a: sum(x == a for x, b in edges) for a in A}
    C = [[0] * n for _ in range(n)]
    mu = [0] * n
    for a, b in edges:
        w = 4 * (degree[a] - 1)
        C[a][a] += w; C[b][b] += w
        C[a][b] -= w; C[b][a] -= w
        mu[a] -= w // 2; mu[b] += w // 2
    return C, mu


def check_torus(torus):
    L, sites, A = torus['L'], torus['sites'], torus['A']
    n = len(sites)
    assert sites == [list(x) for x in product(range(L), repeat=3)]
    assert A == [i for i, x in enumerate(sites) if sum(x) % 2 == 0]
    edges = [tuple(e) for e in torus['edges_oriented_A_to_B']]
    expected_edges = [(a, b) for a in A for b in range(n)
                      if sum(min(abs(sites[a][j] - sites[b][j]), L - abs(sites[a][j] - sites[b][j])) for j in range(3)) == 1]
    assert edges == expected_edges
    eid = {edge: i for i, edge in enumerate(edges)}
    neighbours = {a: [b for x, b in edges if x == a] for a in A}
    expected_keys = {(a, b, c, sign) for a, b in edges for c in neighbours[a] if b != c for sign in (-1, 1)}
    actual_keys = set()
    Crows = [[0] * n for _ in range(n)]; murows = [0] * n
    plus = [[0] * n for _ in range(n)]
    for row in torus['primitive_rows']:
        a, b, c, sign = (row[k] for k in ('a', 'b', 'c', 'sign'))
        key = (a, b, c, sign); assert key not in actual_keys; actual_keys.add(key)
        dq = {a: sign - 1, b: -sign, c: 1}; dq = {k: v for k, v in dq.items() if v}
        flux = {eid[a, b]: sign, eid[a, c]: -1}
        assert row['delta_q'] == [[k, dq[k]] for k in sorted(dq)]
        assert row['field'] == [[k, flux[k]] for k in sorted(flux)]
        div = defaultdict(int)
        for edge, val in flux.items():
            x, y = edges[edge]; div[x] += val; div[y] -= val
        assert {k: v for k, v in div.items() if v} == dq
        assert sum(dq.values()) == 0
        for x, vx in dq.items():
            murows[x] += vx
            for y, vy in dq.items():
                Crows[x][y] += vx * vy
                if sign == 1:
                    plus[x][y] += vx * vy
    assert actual_keys == expected_keys
    expected_C, expected_mu = weighted_laplacian(n, A, edges)
    assert Crows == expected_C and murows == expected_mu
    for label in ('resolved', 'coherent'):
        out = torus['instruments'][label]
        assert out['initial_gain_norm'] == len(actual_keys)
        assert out['covariance_slope_in_kappa'] == Crows
        assert out['mean_slope_in_kappa'] == murows
    assert torus['instruments']['plus_only_mutant']['covariance_slope_in_kappa'] == plus
    mutant_differences = sum(plus[i][j] != Crows[i][j] for i in range(n) for j in range(n))
    assert mutant_differences > 0
    assert all(sum(row) == 0 for row in Crows)

    a, b = torus['selected_edge']
    inputs = [dict(row) for row in torus['selected_gram_input_fields']]
    for gram in torus['selected_grams']:
        out = []
        for field in inputs:
            images = defaultdict(int)
            for sign in gram['signs']:
                for c in neighbours[a]:
                    if c == b:
                        continue
                    dq = tuple(sorted((k, v) for k, v in {a: sign - 1, b: -sign, c: 1}.items() if v))
                    flux = defaultdict(int, field); flux[eid[a, b]] += sign; flux[eid[a, c]] -= 1
                    images[dq, tuple(sorted((k, v) for k, v in flux.items() if v))] += 1
            out.append(images)
        values = [[0, 0], [0, 0]]
        for r in range(2):
            for c in range(2):
                for (dq, field), amp in out[c].items():
                    q = dict(dq); value = 1
                    for site in gram['operator_delta_q_sites']:
                        value *= q.get(site, 0)
                    values[r][c] += value * amp * out[r].get((dq, field), 0)
        assert values == gram['matrix']

    atoms = n + len(edges)
    dsets = [{a, b, n + e} for e, (a, b) in enumerate(edges)]
    stars = {a: {a, *neighbours[a], *(n + eid[a, b] for b in neighbours[a])} for a in A}
    pairs = [(a, c) for i, a in enumerate(A) for c in A[i + 1:] if set(neighbours[a]) & set(neighbours[c])]
    support_summary = {}
    for label, sets in [('magnetic', [stars[a] | stars[c] for a, c in pairs]),
                        ('resolved_jump', [stars[a] for a, b in edges for sign in (-1, 1)])]:
        expanded = [support | set().union(*(d for d in dsets if d & support)) for support in sets]
        expected = {'term_count': len(sets), 'max_support_before': max(map(len, sets)),
                    'max_support_after': max(map(len, expanded)),
                    'incidence_before': [sum(i in support for support in sets) for i in range(atoms)],
                    'incidence_after': [sum(i in support for support in expanded) for i in range(atoms)]}
        assert expected == torus['support_counts'][label]
        assert expected['max_support_after'] <= 2 * 13**2
        count_bound = 13 * (6**2 * 5 if label == 'magnetic' else 2 * 6**2)
        assert max(expected['incidence_after']) <= count_bound
        support_summary[label] = {k: (max(v) if isinstance(v, list) else v) for k, v in expected.items()}
    return {'L': L, 'primitive_rows': len(actual_keys), 'complete_covariance_entries_per_instrument': n * n,
            'gram_entries': 4 * len(torus['selected_grams']), 'mutant_different_entries': mutant_differences,
            'diagonal': Crows[0][0], 'nearest_entry': Crows[edges[0][0]][edges[0][1]],
            'support_summary': support_summary}


def check_tree(t):
    words = [tuple(q) for q in t['full_charge_words']]; index = {q: i for i, q in enumerate(words)}
    A = t['A']; edges = [tuple(e) for e in t['edges_A_to_B']]
    assert words == [q for q in product((-1, 0, 1), repeat=6) if sum(q) == 2]
    fields = t['full_fields']
    for q, field in zip(words, fields):
        div = [0] * 6
        for value, (a, b) in zip(field, edges):
            div[a] += value; div[b] -= value
        assert div == [q[v] - int(v in A) for v in range(6)]
    F = {a: {} for a in A}; J = {str(e) + ':' + str(sign): {} for e in range(len(edges)) for sign in (-1, 1)}
    for col, q in enumerate(words):
        for e, (a, b) in enumerate(edges):
            if q[a] and not q[b]:
                r = list(q); r[a] = 0; r[b] = q[a]; r = tuple(r)
                F[a][index[r], col] = 1
            if not q[a] and not q[b]:
                for sign in (-1, 1):
                    r = list(q); r[a] = sign; r[b] = -sign
                    J[str(e) + ':' + str(sign)][index[tuple(r)], col] = 1
    assert all(F[a] == matrix(t['F_columns'][str(a)]) for a in A)
    assert all(J[key] == matrix(t['j_columns'][key]) for key in J)
    keep = t['P_full_indices']; compressed = {i: p for p, i in enumerate(keep)}
    assert keep == [i for i, q in enumerate(words) if all(q[a] for a in A)]
    assert t['P_charge_words'] == [list(words[i]) for i in keep]
    right = {(r, compressed[c]): val for (r, c), val in F[0].items() if c in compressed}
    S = multiply(F[1], right)
    assert S == matrix(t['S_columns'])
    H = {key: -2 * val for key, val in multiply({(c, r): v for (r, c), v in S.items()}, S).items()}
    assert H == matrix(t['H4_columns'])
    B = {}
    for e, (a, b) in enumerate(edges):
        for sign in (-1, 1):
            key = str(e) + ':' + str(sign)
            full = multiply(J[key], F[a])
            B[key] = {(compressed[r], compressed[c]): val for (r, c), val in full.items() if r in compressed and c in compressed}
            assert B[key] == matrix(t['resolved_B_columns'][key])
        added = defaultdict(int, B[str(e) + ':-1'])
        for key, val in B[str(e) + ':1'].items():
            added[key] += val
        assert dict(added) == matrix(t['coherent_B_columns'][str(e)])
    D = []; ungated = []
    for i in keep:
        q, f = words[i], fields[i]
        D.append(sum(f[e] * (f[e] - q[a]) for e, (a, b) in enumerate(edges) if q[b] == 0))
        ungated.append(sum(f[e] * (f[e] - q[a]) for e, (a, b) in enumerate(edges)))
    assert D == t['D']
    gate_mutant_count = sum(a != b for a, b in zip(D, ungated)); assert gate_mutant_count > 0
    N = [sum(abs(x) for x in words[i]) for i in keep]
    assert N == t['number']
    assert all(N[r] == N[c] for r, c in H)
    assert all(N[r] == N[c] + 2 for b in B.values() for r, c in b)
    C, mu = weighted_laplacian(6, A, edges)
    for row in t['derivative_rows']:
        kappa = row['kappa']
        assert abs(row['trace_derivative']) < 2e-14
        assert max(abs(row['mean_slope'][i] - kappa * mu[i]) for i in range(6)) < 2e-14
        assert max(abs(row['covariance_slope'][i][j] - kappa * C[i][j]) for i in range(6) for j in range(6)) < 2e-14
    summaries = []
    for row in t['finite_time_rows']:
        time, kappa, cov = row['t'], row['kappa'], row['covariance']
        assert abs(row['trace_real'] - 1) < 2e-14 and abs(row['trace_imag']) < 2e-14
        assert row['hermiticity_max'] < 2e-14 and row['min_eigenvalue'] > -2e-14
        assert abs(sum(row['mean_charge']) - 2) < 2e-14
        assert max(abs(sum(v)) for v in cov) < 2e-14
        assert max(abs(cov[i][j] - cov[j][i]) for i in range(6) for j in range(6)) < 2e-14
        assert abs(row['number_probabilities']['2'] - exp(-16 * kappa * time)) < 2e-14
        assert abs(sum(row['number_probabilities'].values()) - 1) < 2e-14
        assert row['number_probabilities']['6'] > 0
        rem = max(abs(cov[i][j] - kappa * time * C[i][j]) for i in range(6) for j in range(6)) / time**2
        assert abs(rem - row['max_abs_covariance_remainder_over_t2']) < 1e-7
        pearson = cov[0][2] / sqrt(cov[0][0] * cov[2][2])
        assert abs(pearson - row['pearson_0_2']) < 1e-14
        summaries.append({'instrument': row['instrument'], 'K': row['K'], 't': time,
                          'remainder_over_t2': rem, 'N6_probability': row['number_probabilities']['6'],
                          'pearson': pearson, 'pearson_error_to_negative_inverse_sqrt3': abs(pearson + 1 / sqrt(3))})
    ratios = []
    for label in ('resolved', 'coherent'):
        for K in (0.0, 2.0, 200.0):
            selected = sorted([r for r in summaries if r['instrument'] == label and r['K'] == K and r['t'] < 0.01], key=lambda x: x['t'])
            ratio = 4 * selected[1]['remainder_over_t2'] / selected[0]['remainder_over_t2']
            assert 3.9 < ratio < 4.1
            assert selected[0]['pearson_error_to_negative_inverse_sqrt3'] < selected[1]['pearson_error_to_negative_inverse_sqrt3']
            ratios.append({'instrument': label, 'K': K, 'absolute_remainder_ratio_double_time': ratio})
    assert all(abs(row['trace'] - 1) > .01 for row in t['mutations'])
    assert all(row['N6_probability'] == 0 for row in t['mutations'] if row['mutation'] == 'drop_recycling')
    return {'full_dimension': len(words), 'P_dimension': len(keep), 'all_integer_matrices_reconstructed': True,
            'occupied_B_gate_mutant_different_entries': gate_mutant_count,
            'covariance_slope_in_kappa': C, 'mean_slope_in_kappa': mu,
            'finite_time_rows': summaries, 'small_time_ratios': ratios, 'mutations': t['mutations']}


def leaves(obj):
    if isinstance(obj, dict):
        for val in obj.values():
            yield from leaves(val)
    elif isinstance(obj, list):
        for val in obj:
            yield from leaves(val)
    else:
        yield obj


def main():
    paths = [p for p in HERE.rglob('*') if p.is_file()]
    before = {str(p): observe(p) for p in paths}
    pins = read('SOURCE_PINS.json')
    source_count = 0
    for row in pins['sources']:
        raw = (HERE / row['snapshot']).read_bytes()
        assert sha256(raw).hexdigest() == row['sha256'] and len(raw) == row['bytes']
        if 'origin' in row:
            now = observe(Path(row['origin']))
            assert now == tuple(row[k] for k in ('sha256', 'bytes', 'mode', 'dev', 'ino', 'mtime_ns', 'ctime_ns', 'nlink'))
        if 'git_revision' in row:
            repository = row.get('git_repository', str(HERE.parent / 'campaign-working'))
            original = subprocess.check_output(['git', '-C', repository, 'show', row['git_revision'] + ':' + row['git_path']])
            assert original == raw
        source_count += 1
    for label in ('capture', 'primitive', 'tree'):
        receipt = read(label + '.execution.json')
        assert receipt['exit_code'] == 0
        assert sha256(Path(receipt['command'][2]).read_bytes()).hexdigest() == receipt['source_sha256']
        assert sha256((HERE / 'record_run.py').read_bytes()).hexdigest() == receipt['recorder_sha256']
        for log in receipt['outputs'].values():
            raw = (HERE / log['path']).read_bytes()
            assert sha256(raw).hexdigest() == log['sha256'] and len(raw) == log['bytes']
        assert receipt['outputs']['stderr.txt']['bytes'] == 0
    p = read('PRIMITIVE_RESULTS.json'); t = read('TREE_RESULTS.json')
    floats = [v for v in leaves(t) if isinstance(v, float)]
    assert all(isfinite(v) for v in floats)
    result = {'scope': 'Read-only stored-evidence reconstruction; no writer or numerical evolution executed.',
              'source_origins': source_count, 'tori': [check_torus(row) for row in p['tori']],
              'tree': check_tree(t), 'all_tree_float_leaves_finite': len(floats)}
    for row in p['nonnorm_continuity']:
        assert row['electric_energy_difference_over_K'] == 8 * row['loop_amplitude_M'] + 4
        assert row['time_in_units_pi_over_K'] == [1, row['electric_energy_difference_over_K']]
        assert row['exact_norm_difference'] == 2
    assert {str(path): observe(path) for path in paths} == before
    result['all_observed_input_files_unchanged'] = len(paths)
    result['result_hashes'] = {name: sha256((HERE / name).read_bytes()).hexdigest()
                               for name in ('PRIMITIVE_RESULTS.json', 'TREE_RESULTS.json')}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
