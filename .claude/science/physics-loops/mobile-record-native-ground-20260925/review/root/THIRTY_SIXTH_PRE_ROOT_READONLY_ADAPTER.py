"""Read-only validation of every own serialized Laurent and fixture row."""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import subprocess
HERE = Path(__file__).resolve().parent

def load(name):
    return json.loads((HERE / name).read_text())

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
pins = load('SOURCE_PINS.json')
origins = []
for source in pins['sources']:
    path = HERE / source['frozen_path']
    assert path.stat().st_size == source['bytes']
    assert sha(path) == source['sha256']
    if source['origin'].startswith('git:'):
        raw = subprocess.check_output(['git', 'show', source['revision'] + ':AGENTS.md'], cwd=source['repository'])
    else:
        raw = Path(source['origin']).read_bytes()
    assert raw == path.read_bytes()
    if source.get('exact_git_object'):
        repo = Path(source['origin']).parent.parent
        raw = subprocess.check_output(['git', 'show', source['revision'] + ':docs/' + Path(source['origin']).name], cwd=repo)
        assert raw == path.read_bytes()
    origins.append(dict(path=source['origin'], sha256=source['sha256'], exact=True))
execution_rows = []
for label in ('freeze', 'star', 'dark_fixture'):
    run = load(label + '.execution.json')
    assert run['exit_code'] == 0
    assert sha(Path(run['argv'][1])) == run['script_sha256']
    for stream in ('stdout', 'stderr'):
        path = HERE / (label + '.' + stream + '.txt')
        assert path.stat().st_size == run[stream + '_bytes']
        assert sha(path) == run[stream + '_sha256']
    assert run['stderr_bytes'] == 0
    execution_rows.append(dict(label=label, exit_code=0, elapsed_seconds=run['elapsed_seconds']))
star = load('STAR_LAURENT_ENTRIES.json')
star_result = load('STAR_CONTROL_RESULTS.json')
assert sha(HERE / 'STAR_LAURENT_ENTRIES.json') == star_result['entries_sha256']
assert load('star.stdout.txt') == star_result
words = star['input_words']
vacancy = [w[1:].count(0) for w in words]
tables = {}
for name in ('M', 'Gamma_over_kappa'):
    table = {}
    for i, j, flow, coefficient in star[name]:
        key = (i, j, tuple(flow))
        assert key not in table and coefficient > 0 and (type(coefficient) is int)
        assert vacancy[i] == vacancy[j]
        assert sum(flow) == words[i][0] - words[j][0]
        assert all((-flow[b] == words[i][b + 1] - words[j][b + 1] for b in range(6)))
        table[key] = coefficient
    for (i, j, flow), coefficient in table.items():
        assert table[j, i, tuple((-x for x in flow))] == coefficient
    tables[name] = table
expected = {key: 2 * (vacancy[key[0]] - 1) * coefficient for key, coefficient in tables['M'].items() if 2 * (vacancy[key[0]] - 1) * coefficient}
assert expected == tables['Gamma_over_kappa']
for row in star_result['vacancy_blocks']:
    v = row['v']
    assert row['input_words'] == vacancy.count(v)
    assert row['zero_angle_M_row_sum'] == v * (7 - v)
    assert Fraction(row['certified_affine_upper']) == max(Fraction(7 - 2 * v, 5), 0) * v * (7 - v)
    assert Fraction(row['certified_affine_upper']) <= 6
assert star_result['M_entries'] == len(tables['M']) == len(star['M'])
assert star_result['Gamma_entries'] == len(tables['Gamma_over_kappa'])
fixture = load('DARK_FIXTURE_PATHS.json')
fixture_result = load('DARK_FIXTURE_RESULTS.json')
assert sha(HERE / 'DARK_FIXTURE_PATHS.json') == fixture_result['data_sha256']
assert load('dark_fixture.stdout.txt') == fixture_result
vertices, edges, q0, E0 = (fixture[x] for x in ('vertices', 'edges', 'q0', 'E0'))
A = set(fixture['A'])
assert len(vertices) == 216 and len(edges) == 648
div = [0] * len(vertices)
for (a, b), e in zip(edges, E0):
    assert a in A and b not in A
    distance = sum((min(abs(x - y), 6 - abs(x - y)) for x, y in zip(vertices[a], vertices[b])))
    assert distance == 1
    div[a] += e
    div[b] -= e
assert div == [q0[i] - int(i in A) for i in range(len(vertices))]

def check_row(row, missing_A):
    q = q0.copy()
    for i, x in row['q_changes']:
        assert x != q0[i] and x in (-1, 0, 1)
        q[i] = x
    residual = [q0[i] - q[i] for i in range(len(vertices))]
    for k, e in row['E_changes']:
        assert e != 0 and type(e) is int
        a, b = edges[k]
        residual[a] += e
        residual[b] -= e
    assert not any(residual)
    assert sum(q) == 108
    assert sum((q[a] == 0 for a in A)) == missing_A
    assert row['coefficient'] > 0 and type(row['coefficient']) is int
    return (tuple(q), tuple((tuple(x) for x in row['E_changes'])))
intermediate_rows = 0
norm_S = 0
for pair in fixture['active_pairs']:
    pair_norm = 0
    for row in pair['intermediate']:
        check_row(row, 2)
        intermediate_rows += 1
        pair_norm += row['coefficient'] ** 2
    assert pair_norm == pair['norm_squared']
    norm_S += pair_norm
Qrows = {}
for row in fixture['Q_initial']:
    key = check_row(row, 0)
    assert key not in Qrows
    Qrows[key] = row['coefficient']
assert Qrows[tuple(q0), ()] == norm_S == fixture_result['Q_expectation_initial'] == 4
assert sum((c * c for c in Qrows.values())) == fixture_result['Q_initial_norm_squared'] == 190
assert len(Qrows) == fixture_result['Q_initial_words'] == 115
count_by_channel = Counter()
norm_by_channel = Counter()
for entry in fixture['B_Q_initial']:
    q, changes = check_row(entry['output'], 0)
    a, b, sigma = entry['channel']
    assert q[a] == sigma and q[b] == -sigma
    assert sum((x != 0 for x in q)) == 216
    count_by_channel[tuple(entry['channel'])] += 1
    norm_by_channel[tuple(entry['channel'])] += entry['output']['coefficient'] ** 2
assert sum(count_by_channel.values()) == fixture_result['B_Q_output_words'] == 328
assert len(count_by_channel) == fixture_result['B_Q_nonzero_channels'] == 116
assert sum(norm_by_channel.values()) == fixture_result['B_Q_norm_squared_sum'] == 1240
assert fixture_result['sum_L_h_norm_squared_over_kappa_delta_squared'] == 4 * 1240
electric = sum((E0[k] * (E0[k] - q0[a]) for k, (a, b) in enumerate(edges) if q0[b] == 0))
assert electric == fixture_result['initial_electric_D'] == 2
assert Fraction(5, 108) * (Fraction(1905, 2) - 648) == Fraction(1015, 72)
assert (Fraction(1905, 2) - 648) / 2 == Fraction(609, 4)
result = dict(verification='Own read-only full serialized evidence consistency; no author program imported or executed', source_origins=origins, execution_bindings=execution_rows, Laurent_M_rows_checked=len(star['M']), Laurent_Gamma_rows_checked=len(star['Gamma_over_kappa']), fixture_intermediate_rows_checked=intermediate_rows, fixture_Q_rows_checked=len(Qrows), fixture_B_Q_rows_checked=sum(count_by_channel.values()), exact_operator_identity_and_Gauss_rows_consistent=True, conditional_arithmetic=dict(rate_constant='1015/72', energy_gap_constant='609/4'), domain_limit='Finite paths and full Laurent identities; no field cutoff, full spectrum, independent filling theorem or physics selection claimed.')
print(json.dumps(result, indent=2))
