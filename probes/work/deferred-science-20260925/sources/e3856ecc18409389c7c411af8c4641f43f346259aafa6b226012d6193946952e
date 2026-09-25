"""Released-source POST correspondence. Reads and prints only; executes no author code."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
from itertools import product, combinations
from math import isfinite
import ast
import json

HERE = Path(__file__).resolve().parent
AUTHOR = HERE / 'post_sources/author47'
STAT_KEYS = ('sha256', 'bytes', 'mode', 'dev', 'ino', 'mtime_ns', 'ctime_ns', 'nlink')


def identity(path):
    stat = path.stat()
    return {'sha256': sha256(path.read_bytes()).hexdigest(), 'bytes': stat.st_size,
            'mode': stat.st_mode, 'dev': stat.st_dev, 'ino': stat.st_ino,
            'mtime_ns': stat.st_mtime_ns, 'ctime_ns': stat.st_ctime_ns, 'nlink': stat.st_nlink}


def load(path):
    return json.loads(path.read_text())


def tuples(value):
    return tuple(tuples(v) for v in value) if isinstance(value, list) else value


def exact_set(serialized):
    values = [tuples(v) for v in serialized]
    assert len(values) == len(set(values)), 'Duplicate stored set entry'
    assert values == sorted(values), 'Stored set order is not canonical'
    return set(values)


def poly_product(p, q):
    result = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            result[i + j] += x * y
    return result


def graph_from_incidence(L):
    sites = list(product(range(L), repeat=3))
    A = [x for x in sites if sum(x) % 2 == 0]
    B = [x for x in sites if sum(x) % 2 == 1]
    adjacent = {}
    for x in sites:
        adjacent[x] = set()
        for axis in range(3):
            for step in (-1, 1):
                y = list(x); y[axis] = (y[axis] + step) % L
                adjacent[x].add(tuple(y))
        assert len(adjacent[x]) == 6
    edges = sorted((a, b) for a in A for b in adjacent[a])
    stars = {a: {('s', *a), *(('s', *b) for b in adjacent[a]),
                 *(('e', *a, *b) for b in adjacent[a])} for a in A}
    # Independently use the defining common-B incidence, not the author's offset table.
    pairs = set()
    for b in B:
        pairs.update(combinations(sorted(adjacent[b]), 2))

    def groups_meeting(atoms):
        answer = {('f', a) for a in A if stars[a] & atoms}
        answer.update(('h', a, c) for a, c in pairs if stars[a] & atoms or stars[c] & atoms)
        return answer

    def support(group):
        return stars[group[1]] if group[0] == 'f' else stars[group[1]] | stars[group[2]]

    return A, edges, stars, pairs, groups_meeting, support


def check_graph(row):
    L = row['L']
    A, edges, stars, pairs, groups_meeting, support = graph_from_incidence(L)
    assert len(pairs) == (15 * L**3 // 4 if L == 4 else 9 * L**3 // 2)
    atom_count = 0; group_count = 0; compact = {}; coefficients = {}
    expected_sites = {'A': {('s', 0, 0, 0)}, 'B': {('s', 1, 0, 0)},
                      'AB': {('s', 0, 0, 0), ('s', 1, 0, 0)}}
    assert set(row['sets']) == set(expected_sites)
    for label, saved in row['sets'].items():
        S = exact_set(saved['S']); assert S == expected_sites[label]
        G = groups_meeting(S)
        X1 = S | set().union(*(support(g) for g in G))
        X2 = set(X1)
        for a, b in edges:
            term = {('s', *a), ('s', *b), ('e', *a, *b)}
            if term & X1:
                X2.update(term)
        G2 = groups_meeting(X2)
        assert X1 == exact_set(saved['X1']) and X2 == exact_set(saved['X2'])
        assert G == exact_set(saved['groups']) and G2 == exact_set(saved['halo_groups'])
        atom_count += len(S) + len(X1) + len(X2)
        group_count += len(G) + len(G2)
        counts = []
        for groups, count_key, strength_key in [(G, 'counts', 'J_coefficients'), (G2, 'halo_counts', 'J_halo_coefficients')]:
            value = {'formation': sum(g[0] == 'f' for g in groups),
                     'magnetic': sum(g[0] == 'h' for g in groups)}
            assert value == saved[count_key]
            strength = [5184 * value['magnetic'], 600 * value['formation']]
            assert strength == saved[strength_key]
            counts.append(value)
        assert len(X1) <= 4651 * len(S) and len(X2) <= 19 * len(X1)
        assert counts[0]['formation'] <= 6 * len(S) and counts[0]['magnetic'] <= 180 * len(S)
        assert all(len(support(g)) <= 25 for g in G | G2)
        assert saved['exhaustive_global_comparison'] == (L <= 8)
        compact[label] = {'X1': len(X1), 'X2': len(X2), 'counts': counts[0], 'halo_counts': counts[1],
                          'J_coefficients': saved['J_coefficients'], 'J_halo_coefficients': saved['J_halo_coefficients']}
    for label, first, second, norm_product in [('AA', 'A', 'A', 4), ('BB', 'B', 'B', 1), ('AB', 'A', 'B', 2)]:
        combined = first if first == second else 'AB'
        p = poly_product(compact[combined]['J_coefficients'], compact[combined]['J_halo_coefficients'])
        q = poly_product(compact[first]['J_coefficients'], compact[second]['J_coefficients'])
        coefficients[label] = [norm_product * (x / 2 + y) for x, y in zip(p, q)]
        assert coefficients[label] == list(map(Fraction, row['M'][label]))
    assert row['M_polynomial_order'] == ['delta_squared', 'delta_kappa', 'kappa_squared']

    # Directly accumulate the entire edge Dirichlet form for the two site tests.
    tests = [{(0, 0, 0): 1}, {(1, 0, 0): 1}]
    means = [0, 0]; covariance = [[0, 0], [0, 0]]
    for a, b in edges:
        gradient = [f.get(b, 0) - f.get(a, 0) for f in tests]
        for i in range(2):
            means[i] += 10 * gradient[i]
            for j in range(2):
                covariance[i][j] += 20 * gradient[i] * gradient[j]
    assert list(map(Fraction, row['means_in_kappa'])) == means == [-60, 60]
    assert [[Fraction(v) for v in r] for r in row['covariance_in_kappa']] == covariance == [[120, -20], [-20, 120]]
    Mab, Mbb = sum(coefficients['AB']), sum(coefficients['BB'])
    interval = min(Fraction(120) / (60 * Mab + 11 * Mbb), Fraction(60) / Mbb)
    illustrative = row['illustrative_delta_kappa_equal_one']
    assert interval == Fraction(illustrative['max_time_for_bound_one_over_sixty'])
    assert illustrative['decimal_time'] == float(interval)
    denominator = 120 - interval * Mbb
    error = interval * (Mab + Mbb / 6) / denominator
    assert denominator > 0 and error <= Fraction(1, 60)
    assert denominator == Fraction(illustrative['denominator']) and error == Fraction(illustrative['ratio_error_bound'])
    return {'L': L, 'global_formation_groups': len(A), 'global_magnetic_pairs': len(pairs),
            'global_electric_terms': len(edges), 'complete_stored_atoms_compared': atom_count,
            'complete_stored_groups_compared': group_count, 'sets': compact,
            'M': {key: list(map(str, values)) for key, values in coefficients.items()},
            'ratio_window': str(interval), 'decimal_window': float(interval),
            'positive_denominator': str(denominator), 'exact_ratio_error': str(error)}


def main():
    pins = load(HERE / 'POST_SOURCE_PINS.json')
    previous = load(HERE / 'POST_PRE_PRESERVATION_BEFORE.json')['files']
    observed = {}
    for row in pins['sources']:
        path = Path(row['origin']); now = identity(path)
        assert all(now[key] == row[key] for key in STAT_KEYS)
        snap = HERE / row['snapshot']
        assert identity(snap)['sha256'] == row['sha256'] and snap.stat().st_size == row['bytes']
        observed[str(path)] = now; observed[str(snap)] = identity(snap)
    for row in previous:
        path = Path(row['path']); now = identity(path)
        assert all(now[key] == row[key] for key in STAT_KEYS)
        observed[str(path)] = now
    assert len(previous) == 41 and len(pins['sources']) == 25
    seal = load(AUTHOR / 'AUTHOR_SEAL.json')
    for member in seal['members']:
        path = AUTHOR / member['path']
        assert identity(path)['sha256'] == member['sha256'] and path.stat().st_size == member['bytes']
    primary_code = AUTHOR / 'local_support_controls.py'
    assert primary_code.read_bytes() == (AUTHOR / 'attempt01/source.py').read_bytes()
    assert (AUTHOR / 'root_readonly_check.py').read_bytes() == (AUTHOR / 'root_readonly_attempt01/source.py').read_bytes()
    assert (AUTHOR / 'WORKING_DERIVATION.md').read_bytes() == (AUTHOR / 'attempt01/WORKING_BEFORE_CONTROL.md').read_bytes()
    execution_bindings = []
    for sub, code in [('attempt01', 'local_support_controls.py'), ('root_readonly_attempt01', 'root_readonly_check.py')]:
        receipt = load(AUTHOR / sub / 'EXECUTION.json')
        output = AUTHOR / sub / 'stdout.json'
        assert receipt['exit_code'] == 0 and receipt['stderr_bytes'] == 0
        assert (AUTHOR / sub / 'stderr.txt').read_bytes() == b''
        assert identity(output)['sha256'] == receipt['stdout_sha256']
        assert identity(AUTHOR / code)['sha256'] == receipt['source_sha256']
        execution_bindings.append({'subpacket': sub, 'source_sha256': receipt['source_sha256'],
                                   'stdout_sha256': receipt['stdout_sha256'],
                                   'elapsed_seconds': receipt['elapsed_seconds'], 'exit_code': receipt['exit_code']})

    # Read author string literals as data; do not execute its prepare_final writer.
    original = (AUTHOR / 'WORKING_DERIVATION.md').read_text()
    reconstructed = original
    state = {}; replacements = []
    for node in ast.parse((AUTHOR / 'prepare_final.py').read_text()).body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            continue
        name = node.targets[0].id
        if name in ('old', 'new'):
            state[name] = ast.literal_eval(node.value)
        elif name == 's' and isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Attribute) and node.value.func.attr == 'replace':
            assert ast.unparse(node.value) == 's.replace(old, new, 1)'
            old, new = state['old'], state['new']
            assert reconstructed.count(old) == 1
            reconstructed = reconstructed.replace(old, new, 1)
            replacements.append({'old_sha256': sha256(old.encode()).hexdigest(), 'new_sha256': sha256(new.encode()).hexdigest(),
                                  'old_bytes': len(old.encode()), 'new_bytes': len(new.encode())})
    note_path = AUTHOR / 'LOCAL_CHARGE_FINITE_TIME_COVARIANCE_ROOT.md'
    assert len(replacements) == 3 and reconstructed == note_path.read_text()
    root_read = load(AUTHOR / 'ROOT_READ_RECEIPT.json')
    assert root_read['note_sha256'] == identity(note_path)['sha256']

    data = load(AUTHOR / 'attempt01/stdout.json')
    assert data['program_sha256'] == identity(primary_code)['sha256']
    assert [g['L'] for g in data['graphs']] == [4, 6, 8, 12, 16, 20]
    assert data['status'] == 'all exact assertions passed' and isfinite(data['elapsed_seconds'])
    graphs = [check_graph(graph) for graph in data['graphs']]
    root_output = load(AUTHOR / 'root_readonly_attempt01/stdout.json')
    assert root_output['observed_files'] == 8 and root_output['byte_and_stat_preservation'] is True
    for own, root in zip(graphs, root_output['graphs']):
        assert own['L'] == root['L'] and own['global_magnetic_pairs'] == root['global_magnetic_pairs']
        assert own['global_electric_terms'] == root['global_electric_terms']
        for label, details in root['local_sets'].items():
            assert {key: own['sets'][label][key] for key in details} == details
        assert own['ratio_window'] == root['exact_bound_window']['max_time_for_bound_one_over_sixty']
    note = note_path.read_text()
    for label, displayed in [('BB', '2373055543296 delta^2+40572057600 delta kappa+170640000 kappa^2'),
                             ('AB', '4371220795392 delta^2+75452083200 delta kappa+319680000 kappa^2')]:
        assert displayed in note
        for graph in graphs[-2:]:
            expected = list(map(int, graph['M'][label]))
            actual = [int(part.split(' ')[0]) for part in displayed.split('+')]
            assert actual == expected
    assert graphs[-1]['ratio_window'] == '5/12223805590224'
    assert graphs[3]['sets']['B']['X2'] == graphs[-1]['sets']['B']['X2'] == 741
    assert graphs[3]['sets']['B']['halo_counts']['magnetic'] == 1710
    assert graphs[-1]['sets']['B']['halo_counts']['magnetic'] == 1713

    # Exact correspondence with the sealed PRE's independently executed primitive matrices.
    pre_data = load(HERE / 'PRIMITIVE_RESULTS.json')
    pre_comparisons = []
    for torus in pre_data['tori']:
        L = torus['L']; coords = list(map(tuple, torus['sites']))
        a, b = coords.index((0, 0, 0)), coords.index((1, 0, 0))
        for instrument in ('resolved', 'coherent'):
            matrix = torus['instruments'][instrument]['covariance_slope_in_kappa']
            assert [[matrix[x][y] for y in (a, b)] for x in (a, b)] == [[120, -20], [-20, 120]]
            assert [torus['instruments'][instrument]['mean_slope_in_kappa'][x] for x in (a, b)] == [-60, 60]
        pre_comparisons.append({'L': L, 'both_original_instruments': 'Exact first coefficients match sealed PRE primitives.'})
    for path, before in observed.items():
        assert identity(Path(path)) == before
    output = {'scope': 'Released-source correspondence and own global common-B incidence reconstruction; no author program or old writer executed.',
              'author47_members': len(seal['members']), 'source_origins': len(pins['sources']),
              'prior_PRE_files_unchanged': len(previous), 'all_observed_sources_and_copies_unchanged': len(observed),
              'working_to_final_literal_replacements': replacements, 'author_execution_bindings': execution_bindings,
              'full_primary_output_sha256': identity(AUTHOR / 'attempt01/stdout.json')['sha256'],
              'author_primary_internal_elapsed_seconds': data['elapsed_seconds'],
              'graphs': graphs, 'sealed_PRE_coefficient_comparisons': pre_comparisons,
              'scientific_proof_assessment': 'Separate POST.md; numerical geometry is not evidence of weak-star measurability or physical selection.'}
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
