#!/usr/bin/env python3
"""Freeze the completed PRE payload once; do not mutate previous seals."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
target = HERE / 'PRE_SEAL.json'
assert not target.exists()
sha = lambda raw: hashlib.sha256(raw).hexdigest()
for label in ('freeze', 'star', 'dark_fixture', 'verification'):
    receipt = json.loads((HERE / (label + '.execution.json')).read_text())
    assert receipt['exit_code'] == 0
    assert sha(Path(receipt['argv'][1]).read_bytes()) == receipt['script_sha256']
    for stream in ('stdout', 'stderr'):
        raw = (HERE / (label + '.' + stream + '.txt')).read_bytes()
        assert len(raw) == receipt[stream + '_bytes']
        assert sha(raw) == receipt[stream + '_sha256']
    assert receipt['stderr_bytes'] == 0
members = []
for path in sorted(HERE.rglob('*')):
    if not path.is_file():
        continue
    assert not path.is_symlink()
    raw = path.read_bytes()
    members.append(dict(path=path.relative_to(HERE).as_posix(),
                        bytes=len(raw), sha256=sha(raw)))
seal = dict(
    created_utc=datetime.now(timezone.utc).isoformat(),
    phase='Blind independent PRE, stopped before incompatibility author access',
    source_revision='60c5f194d940a7bbaf1cdd545296e31d74a02f1a',
    status='Conditional mathematical reconstruction; no audit verdict',
    model_effort='Inherited unchanged; no delegation',
    author_incompatibility_packet_read=False,
    provisional_dependency='Only the explicitly released filling note and seal were read; its half-occupancy trial is a conditional import',
    independent_controls='Own all-color Laurent star enumeration and physical integer-Gauss cubic fixture; own read-only evidence consistency verifier',
    member_count=len(members), members=members)
with target.open('x') as out:
    json.dump(seal, out, indent=2)
    out.write('\n')
for member in members:
    path = HERE / member['path']
    assert path.stat().st_size == member['bytes'] and sha(path.read_bytes()) == member['sha256']
    path.chmod(0o444)
target.chmod(0o444)
print(json.dumps(dict(seal=str(target), seal_sha256=sha(target.read_bytes()),
                      member_count=len(members),
                      PRE_sha256=sha((HERE / 'PRE.md').read_bytes()),
                      source_pins_sha256=sha((HERE / 'SOURCE_PINS.json').read_bytes())),
                 indent=2))
