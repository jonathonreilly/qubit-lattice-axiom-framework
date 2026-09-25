"""Verify unchanged inputs and POST receipts; write a new binding report."""
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import subprocess
HERE = Path(__file__).resolve().parent
sha = lambda raw: hashlib.sha256(raw).hexdigest()
load = lambda name: json.loads((HERE / name).read_text())
pre_raw = (HERE / 'PRE_SEAL.json').read_bytes()
assert sha(pre_raw) == '108fa39b7d3f86f2b9fd825307da6861dd8548bf9295a3415024a72dd19c4f51'
pre = json.loads(pre_raw)
for row in pre['members']:
    raw = (HERE / row['path']).read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
pins = load('POST_SOURCE_PINS.json')
bindings = []
for row in pins['author_sources'] + pins['author_source_origins']:
    frozen = (HERE / row['frozen_path']).read_bytes()
    live = Path(row['origin']).read_bytes()
    assert frozen == live and sha(live) == row['sha256'] and (len(live) == row['bytes'])
    bindings.append(dict(origin=row['origin'], sha256=row['sha256'], bytes=row['bytes']))
for row in pins['procedure_sources']:
    frozen = (HERE / row['frozen_path']).read_bytes()
    _, rev, name = row['origin'].split(':', 2)
    raw = subprocess.check_output(['git', 'show', rev + ':' + name], cwd=HERE.parent / 'campaign-working')
    assert frozen == raw and sha(raw) == row['sha256'] and (len(raw) == row['bytes'])
executions = []
for label in ('post_freeze', 'post_comparison'):
    receipt = load(label + '.execution.json')
    assert receipt['exit_code'] == 0 and receipt['stderr_bytes'] == 0
    assert sha(Path(receipt['argv'][1]).read_bytes()) == receipt['script_sha256']
    for stream in ('stdout', 'stderr'):
        raw = (HERE / (label + '.' + stream + '.txt')).read_bytes()
        assert sha(raw) == receipt[stream + '_sha256'] and len(raw) == receipt[stream + '_bytes']
    executions.append(receipt)
comparison = load('POST_PRIMITIVE_COMPARISON.json')
assert comparison == load('post_comparison.stdout.txt')
author = load('post_sources/author/PRIMITIVE_RATE_ENERGY_RESULTS.json')
assert len(comparison['all_columns']) == len(author['columns']) == 72
for observed, row in zip(comparison['all_columns'], author['columns']):
    assert observed['own_affine_sha256'] == row['complete_affine_columns_sha256']
    assert observed['union_entries'] == len(row['complete_affine_columns'])
    assert observed['Gamma_diagonal'] == row['Gamma_diagonal']
    assert observed['Q_diagonal'] == row['Q_diagonal']
    assert observed['full_payload_equal']
assert sum((row['union_entries'] for row in comparison['all_columns'])) == 43970
phase = comparison['physical_phase_control']
dimension = phase['dimension']
Q, G = (phase['Q_matrix'], phase['Gamma_matrix'])
for row in phase['rows']:
    z = row['integer_complex_amplitudes']
    absolute = [abs(a) + abs(b) for a, b in z]
    norm = sum((a * a + b * b for a, b in z))
    assert norm == row['norm_squared']
    deficits = [[absolute[i] * absolute[j] - z[i][0] * z[j][0] - z[i][1] * z[j][1] for j in range(dimension)] for i in range(dimension)]
    dq = Fraction(sum((Q[i][j] * deficits[i][j] for i in range(dimension) for j in range(dimension))), norm)
    dg = Fraction(sum((G[i][j] * deficits[i][j] for i in range(dimension) for j in range(dimension))), norm)
    assert dq == Fraction(row['Delta_Q']) and dg == Fraction(row['Delta_Gamma'])
    assert 4 * dq - dg == Fraction(row['cube_phase_margin']) >= 0
result = dict(verified_utc=datetime.now(timezone.utc).isoformat(), scope='Source and execution bindings plus complete stored correspondence/phase-row consistency; inputs unchanged, this report newly written', preserved_PRE_seal_sha256=sha(pre_raw), preserved_PRE_members=len(pre['members']), source_bindings=bindings, methodology_revision=pins['procedures_revision'], procedure_bindings=len(pins['procedure_sources']), own_executions=executions, own_reconstructed_columns=72, own_reconstructed_entries=43970, phase_rows_checked=len(phase['rows']), author_code_run_or_imported=False, excluded_other_active_packets_read=False, no_new_scientific_failure=True)
print(json.dumps(result, indent=2))
