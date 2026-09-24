"""Source/evidence bookkeeping and a complete serialized-path audit.

This does not import or execute the scientific control. It reconstructs exact
integer charge and shift data from its certificate to check coverage and
bindings. It is not an independent dynamical simulation.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict
from fractions import Fraction
from datetime import datetime, timezone
import hashlib, json, subprocess

ROOT = Path(__file__).resolve().parent
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def load(name):
    return json.loads((ROOT / name).read_text())

pins = load('SOURCE_PINS.json')
origins = []
for source in pins['sources']:
    path = ROOT / source['frozen_path']
    assert path.stat().st_size == source['bytes']
    assert digest(path) == source['sha256'] == source['expected_sha256']
    if 'commit' in source:
        data = subprocess.check_output(
            ['git', 'show', source['commit'] + ':' + source['path']],
            cwd=source['repository'])
    else:
        data = Path(source['path']).read_bytes()
    assert data == path.read_bytes()
    origins.append(dict(frozen_path=source['frozen_path'], sha256=digest(path),
                        origin_equal=True))
assert len(origins) == 10
print('SOURCE_ORIGINS', json.dumps(origins, sort_keys=True))

# Only the explicitly authorized reports and their seal bytes are reused.
# Do not load prior released author packets through seal-member traversal.
prior_bindings = []
for phase in ['PRE', 'POST']:
    seal = load('sources/readout_' + phase + '_SEAL.json')
    row = next(x for x in seal['members'] if x['path'] == phase + '.md')
    report = ROOT / ('sources/readout_' + phase + '.md')
    assert row['sha256'] == digest(report) and row['bytes'] == report.stat().st_size
    prior_bindings.append(dict(phase=phase, report_sha256=digest(report),
                               seal_sha256=digest(ROOT / ('sources/readout_' + phase + '_SEAL.json')),
                               sealed_report_binding_equal=True,
                               other_old_members_traversed=False))
print('PRIOR_REPORT_BINDINGS', json.dumps(prior_bindings, sort_keys=True))

execution = load('EXECUTION.json')
for field, name in [
    ('script_sha256', 'prepared_probe_control.py'),
    ('stdout_sha256', 'prepared_probe_control.stdout.txt'),
    ('stderr_sha256', 'prepared_probe_control.stderr.txt'),
    ('result_sha256', 'CONTROL_RESULTS.json'),
    ('path_certificate_sha256', 'PATH_CERTIFICATES.json'),
]:
    assert execution[field] == digest(ROOT / name)
assert execution['exit_code'] == 0
assert (ROOT / 'prepared_probe_control.stderr.txt').stat().st_size == 0
lines = (ROOT / 'prepared_probe_control.stdout.txt').read_text().splitlines()
result = load('CONTROL_RESULTS.json')
assert [json.loads(line) for line in lines[:-1]] == result['checks']
assert lines[-1] == 'TOTAL 11 checks completed'
assert result['check_count'] == len(result['checks']) == 11
assert all(x['verified'] for x in result['checks'])
assert result['script_sha256'] == digest(ROOT / 'prepared_probe_control.py')
assert result['path_certificate_sha256'] == digest(ROOT / 'PATH_CERTIFICATES.json')
print('EXECUTION_BINDINGS', json.dumps(execution, sort_keys=True))

certificates = load('PATH_CERTIFICATES.json')
effect_rows = [r for check in result['checks'] if check['name'].startswith('all_prepared_laurent_effects_')
               for r in check['rows']]
assert effect_rows == [{k: v for k, v in row.items() if k != 'paths'} for row in certificates]
assert len(certificates) == result['effect_row_count'] == 48

def sparse_sum(*args):
    out = defaultdict(int)
    for factor, word in args:
        for index, value in word.items():
            out[index] += factor * value
    return {index: value for index, value in out.items() if value}
def word_key(word):
    return tuple(sorted(word.items()))

audited_paths = 0
compact_rows = []
for cert in certificates:
    periods = tuple(cert['periods'])
    vertices = list(product(*(range(n) for n in periods)))
    def wrap(v):
        return tuple(x % n for x, n in zip(v, periods))
    edges = []
    for v in vertices:
        for direction in range(3):
            target = list(v)
            target[direction] += 1
            edges.append((v, wrap(target)))
    edge_ids = {edge: i for i, edge in enumerate(edges)}
    def edge(x, y):
        if (x, y) in edge_ids:
            return {edge_ids[(x, y)]: 1}
        return {edge_ids[(y, x)]: -1}
    def divergence(word):
        div = defaultdict(int)
        for ei, value in word.items():
            x, y = edges[ei]
            div[x] += value
            div[y] -= value
        return {v: value for v, value in div.items() if value}
    A = {v for v in vertices if sum(v) % 2 == 0}
    a, b, c, e, d, r0, rp, rm = map(wrap, [
        (0,0,0), (-1,0,0), (1,0,0), (0,1,0), (1,1,0),
        (0,-1,0), (0,0,1), (0,0,-1)])
    loop = sparse_sum((1, edge(a,c)), (-1, edge(d,c)), (1, edge(d,e)), (-1, edge(a,e)))
    beta = sparse_sum((1, edge(a,rp)), (1, edge(a,rm)), (-1, edge(a,r0)))
    eta_e = sparse_sum((1, beta), (-1, edge(a,e)))
    eta_c = (sparse_sum((1, beta), (1, edge(d,e)), (-1, edge(a,e)), (-1, edge(d,c)))
             if cert['dressing'] == 'loop' else sparse_sum((1, beta), (-1, edge(a,c))))
    expected_signs = {'resolved_plus': [1], 'resolved_minus': [-1], 'coherent': [-1,1]}[cert['channel']]
    assert len(cert['paths']) == cert['path_count'] == 2 * len(expected_signs)
    assert sorted((x['branch'], x['sigma']) for x in cert['paths']) == [
        (branch, sign) for branch in [0,1] for sign in expected_signs]
    matter_keys = []
    for path in cert['paths']:
        branch, sigma = path['branch'], path['sigma']
        occupied, destination, eta = (c, e, eta_c) if branch == 0 else (e, c, eta_e)
        assert tuple(path['destination']) == destination
        assert path['amplitude'] == (1 if branch == 0 else cert['relative_sign'])
        initial_q = {v: 1 for v in A}
        initial_q.update({r0: 1, rp: -1, rm: -1, occupied: 1})
        target = {v: initial_q.get(v,0) - int(v in A) for v in vertices}
        assert divergence(eta) == {v: x for v,x in target.items() if x}
        intermediate_q = dict(initial_q)
        del intermediate_q[a]
        intermediate_q[destination] = 1
        intermediate_E = sparse_sum((1, eta), (-1, edge(a,destination)))
        target = {v: intermediate_q.get(v,0) - int(v in A) for v in vertices}
        assert divergence(intermediate_E) == {v: x for v,x in target.items() if x}
        final_q = dict(intermediate_q)
        final_q[a] = sigma
        final_q[b] = -sigma
        expected_E = sparse_sum((1, intermediate_E), (sigma, edge(a,b)))
        actual_E = dict(path['field_shift'])
        assert actual_E == expected_E
        actual_B = {tuple(v): q for v,q in path['occupied_B']}
        assert actual_B == {v: q for v,q in final_q.items() if v not in A}
        assert {tuple(v) for v in path['A_minus']} == ({a} if sigma == -1 else set())
        target = {v: final_q.get(v,0) - int(v in A) for v in vertices}
        assert divergence(actual_E) == {v: x for v,x in target.items() if x}
        assert len(final_q) == len(A) + 6 and sum(final_q.values()) == len(A)
        matter_keys.append(tuple(sorted(final_q.items())))
        audited_paths += 1
    assert len(set(matter_keys)) == cert['final_matter_word_count'] == len(expected_signs)

    polynomial = defaultdict(Fraction)
    for i, x in enumerate(cert['paths']):
        for j, y in enumerate(cert['paths']):
            if matter_keys[i] != matter_keys[j]:
                continue
            if cert['dephased'] and x['branch'] != y['branch']:
                continue
            word = sparse_sum((1, dict(y['field_shift'])), (-1, dict(x['field_shift'])))
            polynomial[word_key(word)] += Fraction(x['amplitude'] * y['amplitude'], 2)
    polynomial = {key: value for key, value in polynomial.items() if value}
    recorded = {tuple(map(tuple, term['shift'])): Fraction(term['coefficient']) for term in cert['effect']}
    assert polynomial == recorded
    multiplicity = len(expected_signs)
    if cert['dephased']:
        expected = {(): Fraction(multiplicity)}
    elif cert['dressing'] == 'star':
        expected = {(): Fraction(2*multiplicity)} if cert['relative_sign'] == 1 else {}
    else:
        expected = {(): Fraction(multiplicity),
                    word_key(loop): Fraction(cert['relative_sign']*multiplicity,2),
                    word_key({k:-v for k,v in loop.items()}): Fraction(cert['relative_sign']*multiplicity,2)}
    assert recorded == expected
    row = {key: cert[key] for key in ['periods','dressing','relative_sign','channel','dephased','path_count','final_matter_word_count']}
    row['effect_coefficients'] = {('I' if not key else '+loop' if key == word_key(loop) else '-loop'): str(value)
                                  for key,value in recorded.items()}
    row['all_serialized_paths_reconstructed'] = True
    compact_rows.append(row)
    print('COMPLETE_EFFECT_ROW', json.dumps(row, sort_keys=True))

assert audited_paths == 128
direct_rows = [check for check in result['checks'] if check['name'].startswith('direct_physical_output_norms_')]
for check in direct_rows:
    print('DIRECT_OUTPUT_NORMS', json.dumps(check, sort_keys=True))
assert len(direct_rows) == 2

verification = dict(
    created_utc=datetime.now(timezone.utc).isoformat(),
    source_origin_count=len(origins), source_origins=origins,
    prior_report_bindings=prior_bindings, execution_bindings_equal=True,
    stdout_result_checks_equal=True, empty_scientific_stderr=True,
    complete_effect_row_count=len(compact_rows), serialized_paths_reconstructed=audited_paths,
    full_effect_inventory=compact_rows,
    scientific_control_reexecuted_or_imported=False,
    scope='Complete source and execution binding, serialized primitive/Gauss/effect inspection; no new propagation or empirical calculation.',
    verifier_sha256=digest(Path(__file__)),
)
(ROOT/'EVIDENCE_VERIFICATION.json').write_text(json.dumps(verification,indent=2)+'\n')
print('TOTAL verified 10 origins, 2 prior report bindings, all scientific logs/results, 48 effect rows and 128 serialized paths')
