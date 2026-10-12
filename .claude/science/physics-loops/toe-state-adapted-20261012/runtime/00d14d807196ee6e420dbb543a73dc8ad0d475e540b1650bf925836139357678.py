#!/usr/bin/env python3
"""Run already-frozen sentinel fixtures; never run original scientific code."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

E = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


p = argparse.ArgumentParser()
p.add_argument('--seal-sha256', required=True)
args = p.parse_args()
seal_path = E / 'INTEGRITY_EXECUTION_SEAL.json'
if digest(seal_path) != args.seal_sha256:
    raise SystemExit('Integrity execution seal anchor mismatch')
seal = json.loads(seal_path.read_text())
for rel, expected in seal['files'].items():
    if digest(E / rel) != expected:
        raise SystemExit('Integrity input mismatch: ' + rel)

results_dir = E / 'integrity_01' / 'results'
results_dir.mkdir(exist_ok=False)
records = []
for name in ['valid', 'tampered_checker', 'exit_only_survivor']:
    fixture = E / 'integrity_01' / 'fixtures' / name
    outdir = results_dir / name
    outdir.mkdir()
    command = [sys.executable, '-u', str(fixture / 'execute_checks.py')]
    record = {'fixture': name, 'command': command, 'cwd': str(fixture),
              'start_utc': utc(), 'timeout_seconds': 20, 'process_group': True,
              'expected_execution_seal_sha256': args.seal_sha256,
              'source_hashes_before': {rel: digest(E / rel) for rel in seal['files']}}
    (outdir / 'OUTER_START.json').write_text(json.dumps(record, indent=2) + '\n')
    started = time.monotonic()
    with (outdir / 'INNER.stdout').open('wb') as out, (outdir / 'INNER.stderr').open('wb') as err:
        child = subprocess.Popen(command, cwd=fixture, stdout=out, stderr=err,
                                 start_new_session=True)
        try:
            record['returncode'] = child.wait(timeout=20)
            record['timed_out'] = False
        except subprocess.TimeoutExpired:
            record['timed_out'] = True
            os.killpg(child.pid, signal.SIGTERM)
            try:
                record['returncode'] = child.wait(timeout=2)
            except subprocess.TimeoutExpired:
                os.killpg(child.pid, signal.SIGKILL)
                record['returncode'] = child.wait(timeout=2)
        out.flush()
        err.flush()
        os.fsync(out.fileno())
        os.fsync(err.fileno())
    record.update(end_utc=utc(), elapsed_seconds=time.monotonic() - started,
                  source_hashes_after={rel: digest(E / rel) for rel in seal['files']},
                  stdout_sha256=digest(outdir / 'INNER.stdout'),
                  stderr_sha256=digest(outdir / 'INNER.stderr'))
    record['sources_unchanged'] = record['source_hashes_before'] == record['source_hashes_after']
    record['launch_markers'] = sorted(x.name for x in fixture.glob('*.launched'))
    record['attempt_exists'] = (fixture / 'attempt_01').exists()
    complete_path = fixture / 'attempt_01' / 'COMPLETE.json'
    record['complete'] = json.loads(complete_path.read_text()) if complete_path.exists() else None
    (outdir / 'OUTER_END.json').write_text(json.dumps(record, indent=2) + '\n')
    (outdir / 'OUTER.stdout').write_text(json.dumps(record, indent=2) + '\n')
    (outdir / 'OUTER.stderr').write_text('')
    records.append(record)

# Save complete records before deriving or displaying a result.
(results_dir / 'COMPLETE.json').write_text(json.dumps({'completed_utc': utc(), 'records': records}, indent=2) + '\n')
valid, tampered, survivor = records
markers = ['check_fock.launched', 'check_strong_limit.launched']
checks = {
    'exact_driver_sha256_in_all_fixtures': all(digest(E / 'integrity_01' / 'fixtures' / name / 'execute_checks.py') == 'e73d595995f41edf3ca14e218c1010d865081d8136ebec953960dd2475cc8051' for name in ['valid', 'tampered_checker', 'exit_only_survivor']),
    'all_input_hashes_unchanged': all(x['sources_unchanged'] for x in records),
    'no_timeout': all(not x['timed_out'] for x in records),
    'valid_fixture_launches_both': valid['returncode'] == 0 and valid['launch_markers'] == markers and [x['returncode'] for x in valid['complete']['records']] == [0, 0],
    'tamper_rejected_before_launch': tampered['returncode'] != 0 and tampered['launch_markers'] == [] and not tampered['attempt_exists'] and (results_dir / 'tampered_checker' / 'INNER.stderr').read_text() == 'Pre-execution source mismatch: check_fock.py\n',
    'exit_only_survivor_preserved': survivor['returncode'] == 0 and survivor['launch_markers'] == markers and [x['returncode'] for x in survivor['complete']['records']] == [7, 0],
}
result = {'checked_utc': utc(), 'checks': checks,
          'all_expected_behaviors_observed': all(checks.values()),
          'exit_only_survivor': 'Driver exit 0 coexists with first child exit 7. Inspect child statuses and raw records; driver status alone is insufficient.',
          'original_scientific_checks_rerun': False}
(results_dir / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
sys.exit(0 if all(checks.values()) else 1)
