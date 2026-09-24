#!/usr/bin/env python3
"""Freeze the explicitly released author packet; preserve every PRE member."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

here = Path(__file__).resolve().parent
root = Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth/record-photon-readout-personal')
destination = here / 'post_sources' / 'author'
sha = lambda data: hashlib.sha256(data).hexdigest()
pre_bytes = (here / 'PRE_SEAL.json').read_bytes()
assert sha(pre_bytes) == '65ef5734192d3ca88511a992fad2b1788582ad8acf632c2b2d33e866d121cff6'
pre = json.loads(pre_bytes)
for member in pre['members']:
    assert sha((here / member['path']).read_bytes()) == member['sha256']
seal_bytes = (root / 'AUTHOR_CONTROL_SEAL.json').read_bytes()
assert sha(seal_bytes) == '943b8ae9bf740cd2560bd6b77daf91189e8efee33fd857449378fce62ad2d1a2'
seal = json.loads(seal_bytes)
expected = dict(seal['files'])
assert expected['TWO_FORMATION_RECORDS_READ_A_PHOTON_PACKET_ROOT.md'] == '6710b11cede13fc0cb8c7d9e83fac816d590acef8401bd1e98f432c3252840ce'
expected['AUTHOR_CONTROL_SEAL.json'] = sha(seal_bytes)
destination.mkdir(parents=True, exist_ok=True)
rows = []
for name, digest in sorted(expected.items()):
    source = root / name
    data = source.read_bytes()
    assert sha(data) == digest, name
    frozen = destination / name
    if frozen.exists():
        assert frozen.read_bytes() == data
    else:
        frozen.write_bytes(data)
    frozen.chmod(0o444)
    row = {'origin': str(source), 'frozen_path': str(frozen.relative_to(here)),
           'sha256': digest, 'bytes': len(data), 'lines': len(data.splitlines()),
           'role': 'Released author evidence; not independent numerical reproduction.'}
    rows.append(row)
    print(json.dumps(row, sort_keys=True), flush=True)
out = {'phase': 'released-source POST', 'frozen_at_utc': datetime.now(timezone.utc).isoformat(),
       'preserved_PRE_seal_sha256': sha(pre_bytes), 'preserved_PRE_member_count': len(pre['members']),
       'all_PRE_members_unchanged': True, 'released_author_files': rows,
       'scope': 'Read-only source/evidence comparison; no author control execution, publication edit, audit or delegation.'}
(here / 'POST_SOURCE_PINS.json').write_text(json.dumps(out, indent=2) + '\n')
