#!/usr/bin/env python3
"""Exclusive immutable PRE manifest; no scientific computation."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
seal=HERE/'PRE_SEAL.json'
assert not seal.exists()
bindings=json.loads((HERE/'FINAL_BINDINGS.json').read_text())
assert bindings['all_checks_satisfied']
assert sha(HERE/'PRE.md')==bindings['final_PRE_sha256']
receipt=json.loads((HERE/'final_bindings.execution.json').read_text())
assert receipt['exit_code']==0
assert receipt['script_sha256']==sha(HERE/'finalize_bindings.py')
for stream in ('stdout','stderr'):
    p=HERE/('final_bindings.'+stream+'.txt')
    assert sha(p)==receipt[stream+'_sha256'] and p.stat().st_size==receipt[stream+'_bytes']
assert json.loads((HERE/'final_bindings.stdout.txt').read_text())==bindings
sources=json.loads((HERE/'SOURCE_PINS.json').read_text())
for row in sources['sources']:
    assert sha(Path(row['origin']))==sha(HERE/row['frozen_path'])==row['sha256']
members=[]
for path in sorted(p for p in HERE.rglob('*') if p.is_file()):
    assert path.name!='PRE_SEAL.json'
    members.append(dict(path=str(path.relative_to(HERE)),bytes=path.stat().st_size,sha256=sha(path)))
data=dict(created_utc=datetime.now(timezone.utc).isoformat(),
 phase='blind independent PRE, before author disclosure',
 authority='conditional reconstruction and own bounded controls; no audit verdict',
 source_revision=sources['source_revision'],scientific_parent_count=2,
 author_source_access=False,author_program_execution=False,delegation=False,
 PRE_sha256=sha(HERE/'PRE.md'),members=members,
 preservation='All listed members and this seal are made read-only. Later work must use separate files.')
with seal.open('x') as out:json.dump(data,out,indent=2);out.write('\n')
for row in members:
    path=HERE/row['path'];assert sha(path)==row['sha256'];path.chmod(0o444)
seal.chmod(0o444)
print(json.dumps(dict(seal_path=str(seal),seal_sha256=sha(seal),
 PRE_sha256=sha(HERE/'PRE.md'),member_count=len(members),all_members_reverified=True),indent=2))
