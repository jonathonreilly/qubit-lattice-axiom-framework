#!/usr/bin/env python3
"""Capture actual source-only verification, including the default UNBOUND exit.

Both invocations use the saved executable source. All controlling metadata is
snapshotted before either invocation. No scientific source is imported/run.
"""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
RUN = ROOT / 'runs/metadata_checks'
RUN.mkdir(parents=True, exist_ok=False)

def now():
    return datetime.now(timezone.utc).isoformat()

def info(path):
    raw = path.read_bytes()
    return {'path': str(path), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

def save_receipt(record):
    (RUN / 'EXECUTION.json').write_text(json.dumps(record, indent=2) + '\n')

source = RUN / 'SOURCE_AT_LAUNCH.py'
launcher = RUN / 'LAUNCHER_AT_LAUNCH.py'
shutil.copyfile(ROOT / 'verify_provenance.py', source)
shutil.copyfile(Path(__file__), launcher)
inputs = []
for name in ['SOURCE_MANIFEST.json', 'PROVENANCE.json', 'BODY_RECOVERY_MAP.json',
             'SOURCE_CAPTURE.json', 'EVIDENCE_MAP.json']:
    dest = RUN / 'INPUTS_AT_LAUNCH' / name
    dest.parent.mkdir(exist_ok=True)
    shutil.copyfile(ROOT / name, dest)
    inputs.append({'original': info(ROOT / name), 'snapshot': info(dest)})
record = {'kind': 'actual_metadata_only_verification', 'started_utc': now(),
          'source': info(source), 'launcher': info(launcher), 'inputs_at_launch': inputs,
          'cwd': str(ROOT), 'scientific_executions': 0,
          'limits_per_invocation': {'wall_seconds': 30, 'cpu_seconds': None, 'address_space': None},
          'environment_overrides': {'PYTHONDONTWRITEBYTECODE': '1'}, 'invocations': []}
save_receipt(record)
env = dict(os.environ)
env['PYTHONDONTWRITEBYTECODE'] = '1'
for name, flags, expected in [('strict_default', [], 2), ('explicit_source_only', ['--source-only'], 0)]:
    argv = [sys.executable, '-B', str(source), '--packet-root', str(ROOT)] + flags
    item = {'name': name, 'argv': argv, 'cwd': str(ROOT), 'expected_exit': expected, 'started_utc': now()}
    start = time.monotonic()
    try:
        result = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True, timeout=30)
        stdout, stderr = result.stdout, result.stderr
        item['exit_code'] = result.returncode
    except Exception as exc:
        stdout = getattr(exc, 'stdout', None) or b''
        stderr = (getattr(exc, 'stderr', None) or b'') + repr(exc).encode()
        item['exit_code'] = None
        item['exception'] = repr(exc)
    (RUN / (name + '.stdout.txt')).write_bytes(stdout)
    (RUN / (name + '.stderr.txt')).write_bytes(stderr)
    item.update(finished_utc=now(), elapsed_wall_seconds=time.monotonic() - start,
                stdout=info(RUN / (name + '.stdout.txt')), stderr=info(RUN / (name + '.stderr.txt')))
    record['invocations'].append(item)
    save_receipt(record)
record['inputs_unchanged_after'] = all(info(Path(row['original']['path'])) == row['original'] for row in inputs)
record['executable_source_unchanged_after'] = (ROOT / 'verify_provenance.py').read_bytes() == source.read_bytes()
record['observed_expected_exits'] = all(row['exit_code'] == row['expected_exit'] for row in record['invocations'])
record['finished_utc'] = now()
save_receipt(record)
with (ROOT / 'METADATA_CHECKS.md').open('x') as f:
    f.write('# Actual metadata checks\n\n')
    f.write('Two metadata-only invocations used the captured validator source. The controlling manifest, provenance, body map, evidence map and capture map were saved before launch. No source theorem, circuit propagation, matrix reanalysis or physical simulation was executed.\n\n')
    for item in record['invocations']:
        f.write(f"- `{item['name']}`: actual exit `{item['exit_code']}`, declared expected exit `{item['expected_exit']}`; complete streams in `runs/metadata_checks/{item['name']}.stdout.txt` and `.stderr.txt`.\n")
    f.write('\nDefault exit 2 is the deliberate UNBOUND primary outcome, not a hidden failed launch. An unexpected exit remains recorded and prevents sealing. Before the final seal, these invocations claim exact source/receipt closure only; their `exact_final_inventory_checked` value is false. The sealer subsequently constructs the exhaustive final inventory and performs a read-only final validation. Its final result is returned to the caller without adding an unhashed post-seal file.\n')
print(json.dumps(record, indent=2), flush=True)
sys.exit(0 if record['observed_expected_exits'] and record['inputs_unchanged_after']
         and record['executable_source_unchanged_after'] else 1)
