"""Coordinator reproduction of the frozen covariance review, not a new review.

Compare all parsed JSON exactly, excluding only the predeclared created_utc
field in the two independently authored diagnostic programs. Preserve raw data.
Also bind the separate charged stationary-jet author checkpoint for publication.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, sys, tempfile, time

L = Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof')
C = L / 'checks'
def sha(data): return hashlib.sha256(data).hexdigest()
def save(path, data):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(data, indent=2) + '\n')

pins = [
    ('review_soft_fluctuation_receipt.json', '70daa9897a1acd8c2867d592dcc073cbfd517b036ecb475bcaa9a967287cbef8', 'all_review_artifacts'),
    ('charged_stationary_jet_receipt.json', '83ba5129c3b6ca9c6e0d6a4577938531658ddf8fa2a8f21d728831d3edb66b6a', 'owned_artifacts'),
]
records = []
for name, expected, key in pins:
    raw = (C / name).read_bytes()
    assert sha(raw) == expected, name
    packet = json.loads(raw)
    rows = packet[key] + [{'path': str(C/name), 'sha256': expected}]
    if 'report' in packet: rows.append(packet['report'])
    for row in rows:
        p = Path(row['path']); data = p.read_bytes()
        assert sha(data) == row['sha256'], str(p)
        records.append({'path': str(p), 'sha256': sha(data), 'bytes': len(data)})
source = L / 'SOFT_FLUCTUATION_COVARIANCE_ASTRA.md'
source_hash = '327d033b22281f5f727c018ccb9b1d23d8f7d131bd3633602d6655a9b3de2403'
assert sha(source.read_bytes()) == source_hash
save(C/'full_proof_covariance_review_bindings.json', {
    'created_utc': datetime.now(timezone.utc).isoformat(), 'artifacts': records,
    'covariance_source': {'path': str(source), 'sha256': source_hash},
    'scope': 'Frozen covariance review and separate unreviewed charged-jet author packet. No independent charged-jet review is inferred.'})

work = Path(tempfile.mkdtemp(prefix='ym-covariance-review-replay-'))
jobs = [('independent', 'review_soft_fluctuation_independent_02', True),
        ('additional', 'review_soft_fluctuation_additional_02', True),
        ('affected_chart', 'review_soft_fluctuation_chart_affected_01', False)]
def run(job):
    label, stem, timestamp = job
    dest = work / label; dest.mkdir()
    script = C/(stem+'.py'); reference = C/(stem+'.stdout.json')
    shutil.copy2(script, dest/script.name)
    copied_source = dest/source; copied_source.parent.mkdir(parents=True)
    shutil.copy2(source, copied_source)
    assert sha((dest/script.name).read_bytes()) == sha(script.read_bytes())
    started = time.monotonic()
    result = subprocess.run([sys.executable, script.name], cwd=dest, capture_output=True)
    output = C/('full_proof_covariance_review_'+label+'_out.json')
    error = C/('full_proof_covariance_review_'+label+'_err.txt')
    assert not output.exists() and not error.exists()
    output.write_bytes(result.stdout); error.write_bytes(result.stderr)
    actual = json.loads(result.stdout); expected = json.loads(reference.read_bytes())
    if timestamp:
        actual.pop('created_utc'); expected.pop('created_utc')
    receipt = {'label': label, 'command': [sys.executable, script.name],
               'temporary_directory': str(dest), 'exit_code': result.returncode,
               'wall_seconds': time.monotonic()-started,
               'excluded_top_level_fields': ['created_utc'] if timestamp else [],
               'exact_non_time_json_match': actual == expected,
               'source': {'path': str(script), 'sha256': sha(script.read_bytes())},
               'reference': {'path': str(reference), 'sha256': sha(reference.read_bytes())},
               'stdout': {'path': str(output), 'sha256': sha(result.stdout)},
               'stderr': {'path': str(error), 'sha256': sha(result.stderr), 'bytes': len(result.stderr)}}
    save(C/('full_proof_covariance_review_'+label+'_replay.json'), receipt)
    print(json.dumps({'label': label, 'exit_code': result.returncode,
                      'exact_non_time_json_match': actual == expected}), flush=True)
    return receipt
with ThreadPoolExecutor(max_workers=3) as pool:
    runs = list(pool.map(run, jobs))
for row in records: assert sha(Path(row['path']).read_bytes()) == row['sha256'], row['path']
assert sha(source.read_bytes()) == source_hash
ok = all(r['exit_code'] == 0 and not r['stderr']['bytes'] and r['exact_non_time_json_match'] for r in runs)
save(C/'full_proof_covariance_review_replay_summary.json', {
    'created_utc': datetime.now(timezone.utc).isoformat(), 'all_ok': ok,
    'runs': runs, 'frozen_artifact_records': len(records),
    'scope': 'Coordinator reproduction only. Written all-volume mathematics and scientific review remain separately identified; full existence and physical continuum mass gap remain OPEN.'})
assert ok
