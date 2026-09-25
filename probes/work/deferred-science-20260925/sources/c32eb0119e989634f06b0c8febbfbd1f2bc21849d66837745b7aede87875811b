"""Read-only POST46 source/data correspondence; no scientific runner execution.

Reads JSON, text and AST as data. Imports standard library only. No file writes,
subprocesses, dynamic code execution, local imports, network or path discovery.
The separate recorder owns new output files and checks all observed inputs.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import product, combinations
from collections import Counter
import ast
import difflib
import hashlib
import json

D = Path(__file__).resolve().parent
A = D / 'post_author_sources'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def read(p):
    return json.loads(p.read_text())

def identity(p):
    s = p.stat()
    return dict(path=str(p), sha256=sha(p), bytes=s.st_size,
                mtime_ns=s.st_mtime_ns, mode=s.st_mode, inode=s.st_ino)

pins = read(D / 'POST_SOURCE_PINS.json')
baseline = read(D / 'POST_PRESERVATION_BASELINE.json')
for r in baseline['files']:
    assert identity(Path(r['path'])) == r
assert sha(D / 'PRE_SEAL.json') == pins['pre_seal_sha256'] == 'ba242266b82c1768b914a83749b6aa4de64c5fa7992fa7df44f01d4719224410'
pre = read(D / 'PRE_SEAL.json')
for r in pre['members']:
    assert sha(D / r['path']) == r['sha256']
for r in pins['sources']:
    assert sha(Path(r['origin'])) == sha(D / r['snapshot']) == r['sha256']
    assert (D / r['snapshot']).stat().st_size == r['bytes']
for r in pins['reused_pre_origins']:
    assert sha(Path(r['origin'])) == sha(D / r['snapshot']) == r['sha256']
assert sha(A / 'AUTHOR_SEAL.json') == pins['author_seal_sha256'] == '57208448fe5e06b459aaef80b7a044c848954d9ba386d7643baaba20787f604d'
aseal = read(A / 'AUTHOR_SEAL.json')
assert len(aseal['members']) == 15
for r in aseal['members']:
    assert sha(A / r['path']) == r['sha256'] and (A / r['path']).stat().st_size == r['bytes']
assert sha(A / 'CHARGE_CURRENT_AND_INITIAL_COVARIANCE_ROOT.md') == 'b8bec7cc03e7af401aae097445ae24faecd45dcffd8e0273300f16d17d455c1d'

# Read the author primary as syntax only, never importing or evaluating it.
primary = A / 'current_noise_controls.py'
tree = ast.parse(primary.read_text())
imports = sorted({x.name for n in ast.walk(tree) if isinstance(n, ast.Import) for x in n.names}
    | {n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)})
assert imports == ['collections', 'hashlib', 'itertools', 'json', 'pathlib', 'time']
assert primary.read_bytes() == (A / 'attempt01/source.py').read_bytes()
data = read(A / 'attempt01/stdout.json')
receipt = read(A / 'attempt01/EXECUTION.json')
assert data['source_sha256'] == receipt['source_sha256'] == sha(primary)
assert receipt['exit_code'] == 0 and receipt['source_unchanged'] is True
assert sha(A / 'attempt01/stdout.json') == receipt['stdout_sha256']
assert (A / 'attempt01/stderr.txt').read_bytes() == b''
assert sha(A / 'attempt01/stderr.txt') == receipt['stderr_sha256']
rr = read(A / 'ROOT_READONLY_EXECUTION.json')
assert rr['exit_code'] == 0 and rr['all_byte_stat_unchanged'] is True
assert rr['source_sha256'] == sha(A / 'root_readonly_check.py')
assert rr['stdout_sha256'] == sha(A / 'ROOT_READONLY.stdout.json')
assert rr['stderr_sha256'] == sha(A / 'ROOT_READONLY.stderr.txt')
assert (A / 'ROOT_READONLY.stderr.txt').read_bytes() == b''
root_result = read(A / 'ROOT_READONLY.stdout.json')
author_read = read(A / 'ROOT_READ_RECEIPT.json')
assert author_read['author_note_sha256'] == aseal['note_sha256']
assert author_read['primary_result_sha256'] == receipt['stdout_sha256']
assert author_read['readonly_result_sha256'] == rr['stdout_sha256']
assert author_read['failed_scientific_attempts'] == []

def geometry(name):
    if name in ('torus2', 'torus4', 'torus6'):
        period = int(name[-1])
        coords = list(product(range(period), repeat=3))
        aa = {x for x, v in enumerate(coords) if sum(v) % 2 == 0}
        adjacency = []
        for u, v in combinations(range(len(coords)), 2):
            dist = sum(min(abs(x-y), period-abs(x-y)) for x, y in zip(coords[u], coords[v]))
            if dist == 1:
                adjacency.append((u, v) if u in aa else (v, u))
        return coords, aa, sorted(adjacency), period
    if name == 'path7':
        return [(i, 0, 0) for i in range(7)], {0, 2, 4, 6}, sorted(
            (i, i+1) if i % 2 == 0 else (i+1, i) for i in range(6)), None
    assert name == 'K2_3'
    return [(i, 0, 0) for i in range(5)], {0, 1}, list(product((0, 1), (2, 3, 4))), None

def tests(coords, aa, period):
    n = len(coords)
    names = ['constant', 'site0', 'coordinate', 'staggered']
    fs = [[1]*n, [int(i == 0) for i in range(n)],
          [x-2*y+3*z for x, y, z in coords], [1 if i in aa else -1 for i in range(n)]]
    if period == 4:
        names += ['Fourier_re', 'Fourier_im']
        fs += [[(1, 0, -1, 0)[v[0]] for v in coords], [(0, -1, 0, 1)[v[0]] for v in coords]]
    elif period == 6:
        names += ['Fourier_re', 'Fourier_im']
        fs += [[1 if v[0] % 2 == 0 else -1 for v in coords], [0]*n]
    else:
        names += ['index_mod3', 'index_mod5']
        fs += [[i % 3 for i in range(n)], [i % 5 for i in range(n)]]
    return names, fs

groups = data['graph_summaries']
assert [g['graph'] for g in groups] == ['torus2', 'torus4', 'torus6', 'path7', 'K2_3']
assert {r['graph'] for r in data['primitive_rows']} == {g['graph'] for g in groups}
reports = []
stars = {r['degree']: r for r in read(D / 'primitive_attempt01/stdout.json')['star_initial']}
mapped_branches = 0
for g in groups:
    name = g['graph']
    coords, aa, edges, period = geometry(name)
    n = len(coords)
    names, fs = tests(coords, aa, period)
    neighbors = {a: sorted(b for u, b in edges if u == a) for a in aa}
    edge_index = {e: j for j, e in enumerate(edges)}
    degree = {a: len(v) for a, v in neighbors.items()}
    assert g['vertices'] == n and g['A'] == len(aa)
    assert g['edges'] == [list(e) for e in edges]
    assert g['A_degrees'] == [[a, degree[a]] for a in sorted(aa)]
    assert g['test_names'] == names
    mean = [0]*6; cov = [[0]*6 for _ in range(6)]
    electric_drift = [0]*len(edges); charge_drift = [0]*n
    seen = set(); outputs = {}; markcounts = Counter()
    for r in data['primitive_rows']:
        if r['graph'] != name:
            continue
        a, b, c, sign = (r[k] for k in ('a', 'b', 'c', 'sigma'))
        assert a in aa and b in neighbors[a] and c in neighbors[a] and b != c and sign in (-1, 1)
        key = (a, b, c, sign)
        assert key not in seen
        seen.add(key)
        dq = [0]*n; dq[a] = sign-1; dq[b] = -sign; dq[c] = 1
        de = [0]*len(edges); de[edge_index[a, b]] = sign; de[edge_index[a, c]] = -1
        assert r['delta_q'] == [[i, v] for i, v in enumerate(dq) if v]
        assert r['delta_E'] == [[i, v] for i, v in enumerate(de) if v]
        divergence = [0]*n
        for (u, v), shift in zip(edges, de):
            divergence[u] += shift; divergence[v] -= shift
        assert divergence == dq
        q = tuple(int(i in aa)+dq[i] for i in range(n))
        assert all(x in (-1, 0, 1) for x in q)
        assert all(q[a0] != 0 for a0 in aa)
        assert sum(q) == len(aa) and sum(map(abs, q)) == len(aa)+2
        target = outputs.setdefault((a, b), set())
        assert q not in target
        target.add(q); markcounts[a, b] += 1
        values = [sum(x*y for x, y in zip(f, dq)) for f in fs]
        assert values == r['charge_tests']
        for j in range(6):
            mean[j] += values[j]
            for k in range(6):
                cov[j][k] += values[j]*values[k]
        electric_drift = [x+y for x, y in zip(electric_drift, de)]
        charge_drift = [x+y for x, y in zip(charge_drift, dq)]
        # Exact correspondence to the earlier independently written star data.
        sites = [a]+neighbors[a]
        b0 = sites.index(b); c0 = sites.index(c)
        old = [x for x in stars[degree[a]]['branches']
               if (x['mark'], x['hop'], x['sign_at_A']) == (b0, c0, sign)]
        assert len(old) == 1
        assert old[0]['charge_change'] == [dq[x] for x in sites]
        assert old[0]['electric_shift'] == [de[edge_index[a, x]] for x in neighbors[a]]
        mapped_branches += 1
    expected = {(a, b, c, s) for a, near in neighbors.items() for b in near for c in near if b != c for s in (-1, 1)}
    assert seen == expected
    assert len(seen) == g['primitive_rows'] == g['total_first_event_rate_in_kappa']
    assert len(seen) == 2*sum(d*(d-1) for d in degree.values())
    assert g['mark_squared_norms'] == [[a, b, markcounts[a, b], degree[a]-1, 2*(degree[a]-1)] for a, b in edges]
    predicted_mean = [sum(2*(degree[a]-1)*(f[b]-f[a]) for a, b in edges) for f in fs]
    predicted_cov = [[sum(4*(degree[a]-1)*(f[b]-f[a])*(h[b]-h[a]) for a, b in edges) for h in fs] for f in fs]
    assert mean == predicted_mean == g['initial_mean_slope_in_kappa']
    assert cov == predicted_cov == g['initial_covariance_slope_in_kappa']
    currents = [-x for x in electric_drift]
    assert currents == g['formation_current_in_kappa'] == [2*(degree[a]-1) for a, b in edges]
    assert charge_drift == g['initial_charge_drift_in_kappa']
    divcurrent = [0]*n
    for (u, v), j in zip(edges, currents):
        divcurrent[u] += j; divcurrent[v] -= j
    assert charge_drift == [-v for v in divcurrent]
    assert not any(cov[0]) and mean[0] == 0
    assert cov == [list(r) for r in zip(*cov)]
    complex_polarization = dict(
        test='f=test4+i test5; g=test1+i test2',
        mean_f=[mean[4], mean[5]], mean_g=[mean[1], mean[2]],
        hermitian_covariance_fg=[cov[4][1]+cov[5][2], cov[4][2]-cov[5][1]],
        bilinear_covariance_fg=[cov[4][1]-cov[5][2], cov[4][2]+cov[5][1]])
    if period in (4, 6):
        defect = 1 if period == 4 else 2
        exact = dict(allowed_k_in_pi=['1/2' if period == 4 else '1', '0', '0'],
            full_initial_second_moment_slope_in_kappa=80*len(aa)*defect,
            site_normalized_slope_in_kappa=40*defect, defect_sum=defect, imaginary_self_covariance=0)
        assert g['Fourier'] == exact
        assert cov[4][4]+cov[5][5] == exact['full_initial_second_moment_slope_in_kappa']
    else:
        assert g['Fourier'] is None
    reports.append(dict(graph=name, vertices=n, edges=len(edges),
        degree_counts=sorted(Counter(degree.values()).items()), primitive_rows=len(seen),
        test_names=names, mean=mean, covariance=cov,
        formation_current_counts=sorted(Counter(currents).items()),
        charge_drift_counts=sorted(Counter(charge_drift).items()),
        mark_norm_counts=sorted(Counter(tuple(r[2:]) for r in g['mark_squared_norms']).items()),
        Fourier=g['Fourier'], complex_polarization=complex_polarization))

assert mapped_branches == data['primitive_count'] == len(data['primitive_rows']) == 8480
assert data['real_polarized_covariance_entries'] == 180 and data['all_assertions_passed'] is True
expected_root_groups = [dict(graph=r['graph'], primitive_rows=r['primitive_rows'],
    charge_mean=r['mean'], covariance=r['covariance'],
    formation_current_values=[x[0] for x in r['formation_current_counts']],
    charge_drift_values=[x[0] for x in r['charge_drift_counts']], Fourier=r['Fourier']) for r in reports]
assert root_result['groups'] == expected_root_groups
assert root_result['all_complete_primitive_rows_checked'] == 8480
assert root_result['polarized_covariance_entries'] == 180
assert root_result['all_geometry_mark_norm_current_and_charge_arrays_checked'] is True

# Match the common exact L4 Fourier row to the sealed PRE's opposite phase
# convention; self-covariance is unchanged by k -> -k.
fp = read(D / 'fourier_attempt01/stdout.json')
g4 = next(g for g in fp['groups'] if g['L'] == 4)
row4 = next(r for r in g4['Hermitian_covariance_rows'] if r['k_index'] == r['ell_index'] == [3, 0, 0])
assert row4['derivative_over_kappa_polynomial'] == [40, 0]
assert reports[1]['Fourier']['site_normalized_slope_in_kappa'] == 40

# Exact stored PRE off-diagonal-current data supports the analytic wording
# counterexample; this does not rerun that independent control or author code.
primitive_pre = read(D / 'primitive_attempt01/stdout.json')
terms = diagonal = 0
for column in primitive_pre['current_columns']:
    for r in column['magnetic_terms']:
        terms += 1
        assert r['current_without_i_delta'] == [r['h4_coefficient']*s for s in r['shift']]
        if r['q'] == column['q'] and not any(r['shift']):
            diagonal += 1
            assert not any(r['current_without_i_delta'])
minimum = [x for x in primitive_pre['current_columns'] if x['N'] == 2]
assert len(minimum) == 1
assert [x['circulation'] for x in minimum[0]['energies']] == [0, -1000, 1001]
cycle = primitive_pre['coherent_field_magnetic_current']
assert cycle['norm_squared'] == 2
assert cycle['mean_current_numerator_over_delta'] == [[4*x, 0] for x in cycle['cycle']]

old = (A / 'WORKING_DERIVATION.md').read_text()
new = (A / 'CHARGE_CURRENT_AND_INITIAL_COVARIANCE_ROOT.md').read_text()
needle = ('Only for the separately supplied zero-field\n'
          'basis vector does the expectation of that off-diagonal Hamiltonian current\n'
          'vanish.')
assert needle in new
changes = ''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                                      fromfile='WORKING_DERIVATION.md',
                                      tofile='CHARGE_CURRENT_AND_INITIAL_COVARIANCE_ROOT.md'))
for r in baseline['files']:
    assert identity(Path(r['path'])) == r
out = dict(verified_utc=datetime.now(timezone.utc).isoformat(),
    mode='Released-source read-only POST correspondence; no author or PRE scientific code execution/import',
    pre_members_unchanged=31, author_members_verified=15,
    protected_byte_stat_unchanged=len(baseline['files']),
    captured_author_origins_verified=len(pins['sources']), reused_pre_origins_verified=len(pins['reused_pre_origins']),
    transitive_author_origins_not_opened=len(pins['transitive_author_metadata_only']),
    author_primary_imports=imports,
    author_primary=dict(source_sha256=sha(primary), stdout_sha256=receipt['stdout_sha256'],
        exit_code=receipt['exit_code'], elapsed_seconds_external=receipt['elapsed_seconds'],
        elapsed_seconds_internal=data['elapsed_seconds']),
    primitive_rows_checked=8480, exact_pre_star_correspondences=mapped_branches,
    covariance_entries_checked=180, groups=reports,
    shared_L4_normalized_Fourier_covariance=[40, 0],
    stored_PRE_magnetic_terms_checked=terms, stored_PRE_diagonal_magnetic_terms_zero=diagonal,
    minimum_sector_nonzero_circulations_checked=[-1000, 1001],
    retained_PRE_coherent_cycle_current_over_delta=cycle,
    required_repair='Remove only/exclusivity for zero-field basis current expectation; all electric basis states and diagonal mixtures have zero magnetic-current expectation.',
    final_argument_diff=changes,
    limits='Raw stored data is checked mechanically; analytic domain/all-normal-state claims remain proof review. No finite-lag, microscopic derivative, observed spectrum or audit disposition.')
print(json.dumps(out, indent=2, sort_keys=True))
