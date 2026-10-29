"""Coordinator byte binding and reproduction of three frozen candidate units.
This does not supply independent review or any continuum theorem.
Original files and failures remain immutable. Only /elapsed_seconds in the
four uniform-minimizer invocations is excluded from output comparison.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, sys, tempfile, time

R = Path.cwd()
L = Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof')
C = L / 'checks'

def sha(b):
    return hashlib.sha256(b).hexdigest()

def dump(p, value):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(value, indent=2) + '\n')

pins = {
    'uniform_soft_minimizer_receipt.json': '4e980541b2bddc77586bfa7f9285ebb4428684268aedaf750b232d9c9b45fe6a',
    'source_sea_manifest.json': '50af7f02d0dea358ad7e7e68badb6b3919b3e6834b0e13b085af806a824141b7',
    'crossover_import_freeze.json': '63ff7f8680d5f36c1e3d5f1021eb839cd4599854a6bc814a440b87356271689f',
}
receipts = {}
for name, h in pins.items():
    raw = (C / name).read_bytes()
    assert sha(raw) == h, name
    receipts[name] = json.loads(raw)
artifacts = receipts['uniform_soft_minimizer_receipt.json']['files']
artifacts += receipts['source_sea_manifest.json']['owned_files']
artifacts += receipts['crossover_import_freeze.json']['artifacts']
artifacts += [{'path': str(C / n), 'sha256': h} for n, h in pins.items()]
inputs = []
for name, keys in [
    ('uniform_soft_minimizer_inputs.json', ['mathematical_sources', 'methodology', 'installed_skills']),
    ('source_sea_read_coverage.json', ['scientific_inputs', 'methodology', 'installed_skills']),
    ('crossover_import_manifest.json', ['local_inputs', 'governance_reads']),
]:
    data = json.loads((C / name).read_text())
    for key in keys:
        inputs += data[key]
verified = []
for rec in artifacts + inputs:
    path = Path(rec['path'])
    revision = rec.get('revision')
    raw = subprocess.check_output(['git', 'show', revision + ':' + str(path)]) if revision else path.read_bytes()
    assert sha(raw) == rec['sha256'], str(path)
    if 'bytes' in rec:
        assert len(raw) == rec['bytes'], str(path)
    verified.append({'path': str(path), 'sha256': sha(raw), 'bytes': len(raw),
                     'via': 'git:' + revision if revision else 'working-files-before-summary-edits'})
unique = {r['path']: {'path': r['path'], 'sha256': r['sha256']} for r in artifacts}
assert all(not Path(p).is_absolute() and Path(p).suffix.lower() != '.pdf' for p in unique)
dump(C / 'full_proof_next_authors_bindings.json', {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'head_before_integration': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
    'receipt_pins': pins, 'verified_records': verified,
    'verified_record_count': len(verified),
    'commit_ready_artifacts': list(unique.values()),
    'commit_ready_artifact_count': len(unique),
    'third_party_documents': 'Excluded; only frozen author inventories are eligible.',
    'scope': 'Byte binding and reproduction; independent reviews remain separately scoped.',
})

jobs = [
    ('uniform_bloch', 'uniform_soft_minimizer_01.py', ['--mode', 'bloch'], 'uniform_soft_minimizer_01_bloch_out.json'),
    ('uniform_periodic', 'uniform_soft_minimizer_01.py', ['--mode', 'periodic'], 'uniform_soft_minimizer_01_periodic_out.json'),
    ('uniform_strip', 'uniform_soft_minimizer_01.py', ['--mode', 'strip'], 'uniform_soft_minimizer_01_strip_out.json'),
    ('uniform_filling', 'uniform_soft_minimizer_02.py', [], 'uniform_soft_minimizer_02_out.json'),
    ('source_sea', 'source_sea_check.py', [], 'source_sea_run_02.json'),
    ('crossover_import', 'crossover_import_exact.py', [], 'crossover_import_attempt01.stdout.json'),
]

def normalize(value, ignore):
    return {k: v for k, v in value.items() if '/' + k not in ignore}

def run(job):
    label, script_name, args, reference_name = job
    script, reference = C / script_name, C / reference_name
    code, expected = script.read_bytes(), reference.read_bytes()
    temporary = Path(tempfile.mkdtemp(prefix='ym-next-authors-replay-'))
    copy = temporary / script_name
    copy.write_bytes(code)
    companions = []
    if label == 'uniform_filling':
        p = C / 'uniform_soft_minimizer_01_periodic_out.json'
        shutil.copyfile(p, temporary / p.name)
        companions.append({'path': str(p), 'sha256': sha(p.read_bytes())})
    command = [sys.executable, str(copy)] + args
    start = datetime.now(timezone.utc).isoformat()
    clock = time.monotonic()
    proc = subprocess.run(command, cwd=R, capture_output=True)
    stem = C / ('full_proof_next_' + label + '_replay')
    out, err = Path(str(stem) + '_out.json'), Path(str(stem) + '_err.txt')
    assert not out.exists() and not err.exists()
    out.write_bytes(proc.stdout)
    err.write_bytes(proc.stderr)
    ignore = {'/elapsed_seconds'} if label.startswith('uniform_') else set()
    match, parse_error = False, None
    try:
        match = normalize(json.loads(proc.stdout), ignore) == normalize(json.loads(expected), ignore)
    except Exception as exc:
        parse_error = repr(exc)
    record = {
        'label': label, 'script': str(script), 'script_sha256': sha(code),
        'reference': str(reference), 'reference_sha256': sha(expected),
        'copied_read_only_companions': companions, 'command': command, 'cwd': str(R),
        'started_utc': start, 'finished_utc': datetime.now(timezone.utc).isoformat(),
        'elapsed_seconds': time.monotonic() - clock, 'exit_code': proc.returncode,
        'stdout': {'path': str(out), 'sha256': sha(proc.stdout)},
        'stderr': {'path': str(err), 'sha256': sha(proc.stderr), 'bytes': len(proc.stderr)},
        'ignored_comparison_fields': sorted(ignore),
        'all_other_output_fields_identical': match, 'parse_error': parse_error,
        'original_script_unchanged': script.read_bytes() == code,
        'reference_unchanged': reference.read_bytes() == expected,
        'scope': 'Coordinator reproduction of author diagnostics, not independent review.',
    }
    dump(Path(str(stem) + '.json'), record)
    print(json.dumps({k: record[k] for k in ['label', 'exit_code', 'all_other_output_fields_identical', 'parse_error']}), flush=True)
    return record

records = []
with ThreadPoolExecutor(max_workers=3) as pool:
    for future in as_completed([pool.submit(run, job) for job in jobs]):
        records.append(future.result())
for rec in unique.values():
    assert sha(Path(rec['path']).read_bytes()) == rec['sha256'], rec['path']
ok = all(r['exit_code'] == 0 and r['stderr']['bytes'] == 0
         and r['all_other_output_fields_identical'] and r['original_script_unchanged']
         and r['reference_unchanged'] for r in records)
dump(C / 'full_proof_next_authors_replay_summary.json', {
    'created_utc': datetime.now(timezone.utc).isoformat(), 'all_ok': ok,
    'runs': sorted(records, key=lambda r: r['label']),
    'all_frozen_author_artifacts_unchanged': True,
    'scope': 'Six diagnostic invocations reproduced; repeated predicates are not independent evidence.',
})
print(json.dumps({'all_ok': ok, 'runs': len(records), 'artifacts': len(unique),
                  'artifact_and_input_bindings': len(verified)}), flush=True)
assert ok
