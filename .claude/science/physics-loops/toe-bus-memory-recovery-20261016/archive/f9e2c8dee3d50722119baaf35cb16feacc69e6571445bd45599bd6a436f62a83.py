#!/usr/bin/env python3
"""Bookkeeping only. These hashes do not decide scientific correctness."""
from pathlib import Path
import hashlib
import json

base = Path(__file__).resolve().parent.parent if Path(__file__).resolve().parent.name.startswith('run_') else Path(__file__).resolve().parent
sha = lambda data: hashlib.sha256(data).hexdigest()

def require_bytes(data, wanted):
    if sha(data) != wanted:
        raise ValueError('Source or stream hash mismatch')

manifest = json.loads((base/'SOURCE_MANIFEST.json').read_text())
checked = []
for name, entry in manifest['sources'].items():
    for field in ('original', 'captured'):
        require_bytes(Path(entry[field]).read_bytes(), entry['sha256'])
    checked.append(name)

run = base/'run_001'
execution = json.loads((run/'EXECUTION.json').read_text())
launch = json.loads((run/'LAUNCH.json').read_text())
assert execution['exit_code'] == 0 and not execution['timed_out']
for path, expected in (
    (run/'executed_source.py', execution['source_at_launch_sha256']),
    (base/'independent_bitstring_check.py', execution['source_at_launch_sha256']),
    (run/'stdout.json', execution['stdout_sha256']),
    (run/'stderr.txt', execution['stderr_sha256']),
    (run/'launcher_at_launch.py', launch['launcher_at_launch_sha256']),
    (base/'ANALYTIC_FINDINGS.md', launch['analytic_findings_sha256'])):
    require_bytes(path.read_bytes(), expected)
assert execution['argv'] == launch['argv']
assert execution['cwd'] == launch['cwd']
tamper_cases = []
for name in ('DERIVATION.md', 'bus_note.md', 'compensated_reservoir.md'):
    entry = manifest['sources'][name]
    altered_in_memory = Path(entry['captured']).read_bytes()+b'\n'
    try:
        require_bytes(altered_in_memory, entry['sha256'])
    except ValueError:
        tamper_cases.append(name)
    else:
        raise AssertionError('Tampered source accepted')
try:
    require_bytes((run/'stdout.json').read_bytes()+b' ', execution['stdout_sha256'])
except ValueError:
    tamper_cases.append('run_001/stdout.json')
else:
    raise AssertionError('Tampered stream accepted')
print(json.dumps({'source_names_checked': checked,
                  'live_originals_match_captures': True,
                  'scientific_execution_record_matches': True,
                  'in_memory_tamper_cases_rejected': tamper_cases,
                  'scientific_status': 'Provenance only; no theorem established by this check.'}, indent=2))
