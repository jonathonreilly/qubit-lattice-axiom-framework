#!/usr/bin/env python3
"""Bookkeeping only: preserve exact inputs and freeze pre-checker analysis."""
import datetime
import hashlib
import json
import os
from pathlib import Path

R = Path(__file__).resolve().parent
A = R.parent / 'real_coupling_halt_route'

def identity(path):
    b = path.read_bytes()
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def durable_json(path, obj):
    data = (json.dumps(obj, indent=2, sort_keys=True) + '\n').encode()
    with path.open('xb') as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    fd = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)

pins = {
    'ROUTE.md': 'c1cf729c2639d682a66df72b880c529dbabfc1768935ae62d170538973ce2018',
    'FREEZE.json': '16fa2cbf13386826cd6939cc412f66c9224a89eaadd133b2163c5b3130e5829b',
    'SOURCE_MANIFEST.json': '717b918b6b67b736daaddf9f51bde2182ff6013b3a925395744a5881a2b1149a',
}
entries = []
for name, pin in pins.items():
    p = A / name
    d = identity(p)
    if d['sha256'] != pin:
        raise RuntimeError('new-source hash mismatch: ' + str(p))
    dest = R / 'inputs' / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open('xb') as f:
        f.write(p.read_bytes())
    entries.append({'original': str(p), 'snapshot': str(dest.relative_to(R)), **d})

manifest = json.loads((A / 'SOURCE_MANIFEST.json').read_text())
for item in manifest['entries']:
    p = A / item['snapshot']
    d = identity(p)
    if d != {k: item[k] for k in ('bytes', 'sha256')}:
        raise RuntimeError('inherited snapshot mismatch: ' + str(p))
    dest = R / 'inputs' / 'inherited' / Path(item['snapshot']).name
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open('xb') as f:
        f.write(p.read_bytes())
    original = Path(item['original'])
    current = identity(original) if original.is_file() else None
    entries.append({'original': str(p), 'snapshot': str(dest.relative_to(R)),
                    'upstream_original': str(original), 'upstream_current': current,
                    'upstream_matches_snapshot': current == d, **d})

durable_json(R / 'SOURCE_BINDINGS.json', {
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'purpose': 'Read/copy/hash bookkeeping only; not a scientific execution',
    'source_exposure': 'Author argument and frozen inventory read; no author checker, launcher, scalar inputs or outputs read yet',
    'entries': entries,
})
files = []
for p in sorted(R.rglob('*')):
    if p.is_file():
        files.append({'path': str(p.relative_to(R)), **identity(p)})
durable_json(R / 'ANALYTIC_FREEZE.json', {
    'frozen_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'stage': 'Analytic result frozen before author checker/output inspection',
    'scientific_runs': 0,
    'files': files,
})
print(json.dumps({'snapshots': len(entries),
                  'upstream_pairs': sum('upstream_original' in e for e in entries),
                  'upstream_matches': sum(e.get('upstream_matches_snapshot', False) for e in entries),
                  'analytic_files_frozen': len(files),
                  'analysis': identity(R / 'PRECHECK_ANALYSIS.md'),
                  'analytic_freeze': identity(R / 'ANALYTIC_FREEZE.json')}, indent=2))
