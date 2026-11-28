#!/usr/bin/env python3
"""Bookkeeping only: inspect saved records; do not import numerical code."""
import ast
import collections
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
LANE = HERE.parents[1]
NOTE = LANE / 'library/gap-descent-n-trend-astra.md'
CUTS = {(10, 12, 32), (14, 18, 44)}
data = json.loads((HERE / 'sweep.json').read_text())
points = data['grid'] + data['bisection']
for point in points:
    assert len(point['values']) == 2
    assert {(v['chars'], v['loops'], v['quadrature']) for v in point['values']} == CUTS
    for v in point['values']:
        stem = f"n{v['n']}_b{v['beta']:.17g}_A{v['chars']}_D{v['loops']}_Q{v['quadrature']}"
        assert json.loads((HERE / (stem + '.json')).read_text()) == v
        assert max(v['residuals']) < 1e-10
        assert v['peak_RSS_bytes'] <= 2_000_000_000
        g = v['per_gap']
        assert max(abs(g[j][i] - g[-1-j][i]) for j in range(len(g)) for i in (0, 1)) <= 1e-9

steps = {}
for n in (4, 5, 6):
    grid = sorted((p for p in data['grid'] if p['n'] == n), key=lambda p: p['beta'])
    assert [p['beta'] for p in grid] == [.5, 1., 1.5, 2., 2.3, 2.4, 2.5, 2.6, 3., 3.5]
    assert all(v['difference'] > 0 for p in grid[:-1] for v in p['values'])
    assert all(v['difference'] < 0 for v in grid[-1]['values'])
    lo, hi, count = 3., 3.5, 0
    while hi - lo > 1e-5:
        mid = (lo + hi) / 2
        found = [p for p in data['bisection'] if p['n'] == n and p['beta'] == mid]
        assert len(found) == 1
        vals = found[0]['values']
        assert vals[0]['difference'] * vals[1]['difference'] > 0
        if vals[0]['difference'] < 0:
            hi = mid
        else:
            lo = mid
        count += 1
    assert next(p['bracket'] for p in data['brackets'] if p['n'] == n) == [lo, hi]
    steps[n] = count

for E in (44, 48):
    d = json.loads((HERE / f'wilson_J4E{E}.json').read_text())
    assert {(x['beta'], x['multiplier']) for x in d['results']} == {(b, m) for b in (2.3, 2.4, 2.5, 2.6) for m in (0, 4, 2, 1)}
    assert len(d['results']) == 16
    assert max(d['peak_RSS_bytes'], d['basis_meta']['peak_RSS_bytes']) <= 2_000_000_000
    assert all(max(x['residuals']) < 1e-9 for x in d['results'])

note = NOTE.read_text()
assert note.startswith('# Repo search\n')
assert sum(line.startswith('RESULT:') for line in note.splitlines()) == 1
assert note.rstrip().splitlines()[-1].startswith('RESULT:')
assert json.loads((HERE / 'numeric_lock_release.json').read_text())['status'] == 'released'
files = [p for p in HERE.rglob('*') if p.is_file() and p.name not in ('artifact_manifest.json', 'record_verification.json')]
assert all(p.suffix in {'.py', '.json', '.log'} for p in files)
assert all(p.stat().st_size < 10_000_000 for p in files)
for p in files:
    if p.suffix == '.py':
        ast.parse(p.read_text(), filename=str(p))
    elif p.suffix == '.json':
        json.loads(p.read_text())
manifest = {str(p.relative_to(LANE)): {'bytes': p.stat().st_size, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(files + [NOTE])}
(HERE / 'artifact_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
record = {'kind': 'saved-record bookkeeping, no proof or new numerical run', 'status': 'passed', 'heat_pairs': len(points), 'bisection_steps_per_n': steps, 'wilson_points': 32, 'file_counts': dict(collections.Counter(p.suffix for p in files)), 'total_bytes': sum(p.stat().st_size for p in files), 'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(), 'branch': subprocess.check_output(['git', 'branch', '--show-current'], text=True).strip()}
assert record['head'] == 'bc343b5d672fd4f07c66ec39247981322f110f18'
(HERE / 'record_verification.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
