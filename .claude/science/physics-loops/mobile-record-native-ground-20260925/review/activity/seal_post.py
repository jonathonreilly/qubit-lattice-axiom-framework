#!/usr/bin/env python3
"""Seal only the new POST files and bind the preserved immutable PRE."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
sha = lambda raw: hashlib.sha256(raw).hexdigest()
pre_raw = (HERE / 'PRE_SEAL.json').read_bytes()
assert sha(pre_raw) == '108fa39b7d3f86f2b9fd825307da6861dd8548bf9295a3415024a72dd19c4f51'
pre = json.loads(pre_raw)
excluded = {'PRE_SEAL.json'}
for row in pre['members']:
    raw = (HERE / row['path']).read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
    excluded.add(row['path'])
for label in ('post_freeze', 'post_comparison', 'post_bindings'):
    receipt = json.loads((HERE / (label + '.execution.json')).read_text())
    assert receipt['exit_code'] == 0 and receipt['stderr_bytes'] == 0
    assert sha(Path(receipt['argv'][1]).read_bytes()) == receipt['script_sha256']
    for stream in ('stdout', 'stderr'):
        raw = (HERE / (label + '.' + stream + '.txt')).read_bytes()
        assert len(raw) == receipt[stream + '_bytes'] and sha(raw) == receipt[stream + '_sha256']
target = HERE / 'POST_SEAL.json'
assert not target.exists()
members = []
for path in sorted(HERE.rglob('*')):
    if not path.is_file():
        continue
    relative = path.relative_to(HERE).as_posix()
    if relative in excluded:
        continue
    assert not path.is_symlink()
    raw = path.read_bytes()
    members.append(dict(path=relative, bytes=len(raw), sha256=sha(raw)))
seal = dict(
    sealed_utc=datetime.now(timezone.utc).isoformat(),
    phase='Released-source POST comparison; stopped after scoped completion',
    status='Conditional mathematical comparison; no audit verdict or publication action',
    preserved_PRE_seal_sha256=sha(pre_raw), preserved_PRE_members=len(pre['members']),
    author_seal_sha256='24e2131d01c9e47b9d8c684486e726ab753d7cab1962566baee13fbd5fead572',
    author_note_sha256='efd15929c31fb137219efb571b99fd0bc3641410f1ea857339fdde65d9128a81',
    author_programs_executed_or_imported=False,
    model_effort='Inherited unchanged, no delegation',
    member_count=len(members), members=members)
with target.open('x') as out:
    json.dump(seal, out, indent=2)
    out.write('\n')
for row in members:
    path = HERE / row['path']
    raw = path.read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
    path.chmod(0o444)
target.chmod(0o444)
print(json.dumps(dict(seal_path=str(target), seal_sha256=sha(target.read_bytes()),
                      POST_sha256=sha((HERE / 'POST.md').read_bytes()),
                      source_pins_sha256=sha((HERE / 'POST_SOURCE_PINS.json').read_bytes()),
                      member_count=len(members), preserved_PRE_members=len(pre['members'])), indent=2))
