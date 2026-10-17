#!/usr/bin/env python3
"""Post-analysis bookkeeping only. Never runs/imports the author checker."""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path

R = Path(__file__).resolve().parent
A = R.parent / 'real_coupling_halt_route'

def identity(p, generation=False):
    b = p.read_bytes()
    d = {'bytes': len(b), 'sha256': sha256(b).hexdigest()}
    if generation:
        s = p.stat()
        d.update(device=s.st_dev, inode=s.st_ino, mtime_ns=s.st_mtime_ns)
    return d

def save(p, obj):
    with p.open('x') as f:
        json.dump(obj, f, indent=2, sort_keys=True)
        f.write('\n')
        f.flush()
        os.fsync(f.fileno())

af = json.loads((R / 'ANALYTIC_FREEZE.json').read_text())
analysis_entries = []
for e in af['files']:
    d = identity(R / e['path'])
    if d != {k: e[k] for k in ('bytes', 'sha256')}:
        raise RuntimeError('analysis freeze changed: ' + e['path'])
    analysis_entries.append({'path': e['path'], 'unchanged': True})

freeze_identity = identity(A / 'FREEZE.json')
assert freeze_identity['sha256'] == '16fa2cbf13386826cd6939cc412f66c9224a89eaadd133b2163c5b3130e5829b'
freeze = json.loads((A / 'FREEZE.json').read_text())
inventory = []
expected = {e['path'] for e in freeze['files']} | {'FREEZE.json'}
actual = {str(p.relative_to(A)) for p in A.rglob('*') if p.is_file()}
assert actual == expected
for e in freeze['files'] + [{'path': 'FREEZE.json', **freeze_identity}]:
    src = A / e['path']
    d = identity(src)
    assert d == {k: e[k] for k in ('bytes', 'sha256')}
    dest = R / 'author_packet' / e['path']
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open('xb') as f:
        f.write(src.read_bytes())
    inventory.append({'source': str(src), 'snapshot': str(dest.relative_to(R)), **d})

pre = json.loads((A / 'run01/PRELAUNCH.json').read_text())
receipt = json.loads((A / 'run01/RECEIPT.json').read_text())
output = json.loads((A / 'run01/stdout.json').read_text())
manifest = json.loads((A / 'SOURCE_MANIFEST.json').read_text())
after = {e['label']: e for e in receipt['bindings_after']}
bindings = []
for e in pre['bindings']:
    p = Path(e['path'])
    if not p.is_absolute():
        p = A / p
    d = identity(p, True)
    assert d == e['identity'] == after[e['label']]['identity']
    assert after[e['label']]['unchanged']
    bindings.append({'label': e['label'], 'path': str(p), 'identity': d,
                     'matches_prelaunch_and_receipt': True})

pairs = []
for e in manifest['entries']:
    d = identity(Path(e['original']))
    s = identity(A / e['snapshot'])
    assert d == s == {k: e[k] for k in ('bytes', 'sha256')}
    pairs.append({'original': e['original'], 'snapshot': e['snapshot'], **d,
                  'unchanged': True})

assert identity(A / 'check_route.py') == identity(A / 'run01/executed_source.py')
assert identity(A / 'check_route.py')['sha256'] == output['source_sha256']
assert identity(A / 'run01/PRELAUNCH.json', True) == receipt['prelaunch_identity']
assert identity(A / 'run01/PRELAUNCH.json')['sha256'] == output['prelaunch_sha256']
assert identity(A / 'run01/stdout.json', True) == receipt['stdout']
assert identity(A / 'run01/stderr.txt', True) == receipt['stderr']
assert receipt['returncode'] == 0 and not receipt['timed_out']
assert receipt['status'] == output['status'] == 'completed'
assert receipt['prelaunch_unchanged'] and receipt['all_bindings_unchanged']
assert receipt['all_original_source_contents_unchanged']
assert all(e['result'].get('satisfied', True) for e in output['records'])

chronology = {
    'author_prelaunch_created': pre['created_before_subprocess_utc'],
    'author_prelaunch_fsync_completed': receipt['prelaunch_fsync_completed_utc'],
    'author_subprocess_created_after': receipt['subprocess_created_after_utc'],
    'author_finished': receipt['finished_utc'],
    'author_freeze': freeze['frozen_utc'],
    'review_analysis_freeze': af['frozen_utc'],
    'post_exposure_bookkeeping': datetime.now(timezone.utc).isoformat(),
}
dates = [datetime.fromisoformat(x) for x in chronology.values()]
assert dates == sorted(dates)
result = {
    'purpose': 'Provenance, bytes and record consistency only; no new scientific execution',
    'review_scientific_runs': 0,
    'author_checker_replayed_or_imported': False,
    'chronology': chronology,
    'analysis_entries': analysis_entries,
    'author_inventory': inventory,
    'author_bindings_current': bindings,
    'original_snapshot_pairs_current': pairs,
    'author_dimensions_record': next(x['result'] for x in output['records'] if x['test'] == 'actual_dimensions'),
    'author_record_count': len(output['records']),
    'scientific_inference_from_record_count': False,
    'author_costs': {k: receipt[k] for k in ('wrapper_wall_seconds', 'child_user_cpu_seconds',
        'child_system_cpu_seconds', 'child_peak_rss_raw', 'child_peak_rss_units',
        'cpu_soft_hard_seconds', 'external_wall_seconds', 'thread_count_measured')},
    'non_scientific_review_read_failure': 'First attempted check_realification.py, which does not exist; cat returned No such file or directory. Correct check_route.py subsequently read completely. No scientific run failed or was attempted.',
    'read_scope_limit': 'Raw 74301-byte lexical repository search copied and hashed, not claimed read in full; all new mathematics, checker, launcher, prelaunch, receipt and stdout read completely.',
}
save(R / 'PROVENANCE.json', result)
summary = {'author_inventory_files': len(inventory), 'author_frozen_entries': len(freeze['files']),
           'analysis_files_unchanged': len(analysis_entries),
           'actual_current_prelaunch_bindings': len(bindings),
           'runtime_bindings': sum(e['label'].startswith('runtime:') for e in bindings),
           'original_snapshot_pairs': len(pairs), 'review_scientific_runs': 0,
           'author_returncode': receipt['returncode'],
           'provenance': identity(R / 'PROVENANCE.json')}
save(R / 'PROVENANCE_SUMMARY.json', summary)
print(json.dumps(summary, indent=2))
