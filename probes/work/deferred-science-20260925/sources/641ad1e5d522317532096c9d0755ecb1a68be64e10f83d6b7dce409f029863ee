"""One-time POST46 source snapshot writer; no scientific execution or imports.

Only the explicitly released author46 members, existing PRE46 and its six
permitted origins are read. No transitive author source path is followed.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

D = Path(__file__).resolve().parent
A = D.parent / 'native-charge-current-noise-personal'
PRE = 'ba242266b82c1768b914a83749b6aa4de64c5fa7992fa7df44f01d4719224410'
AUTHOR = '57208448fe5e06b459aaef80b7a044c848954d9ba386d7643baaba20787f604d'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def identity(p):
    s = p.stat()
    return dict(path=str(p), sha256=sha(p), bytes=s.st_size,
                mtime_ns=s.st_mtime_ns, mode=s.st_mode, inode=s.st_ino)

assert sha(D / 'PRE_SEAL.json') == PRE
assert sha(A / 'AUTHOR_SEAL.json') == AUTHOR
pre = json.loads((D / 'PRE_SEAL.json').read_text())
author = json.loads((A / 'AUTHOR_SEAL.json').read_text())
assert len(pre['members']) == 31 and len(author['members']) == 15
protected = [D / 'PRE_SEAL.json', A / 'AUTHOR_SEAL.json']
for base, seal in [(D, pre), (A, author)]:
    for row in seal['members']:
        p = base / row['path']
        assert not p.is_symlink() and sha(p) == row['sha256']
        assert p.stat().st_size == row['bytes']
        protected.append(p)
for row in pre['source_origins']:
    p = Path(row['origin'])
    assert sha(p) == row['sha256']
    protected.append(p)
before = [identity(p) for p in protected]
sources = []
for name in ['AUTHOR_SEAL.json'] + [r['path'] for r in author['members']]:
    p = A / name
    out = D / 'post_author_sources' / name
    out.parent.mkdir(parents=True, exist_ok=True)
    raw = p.read_bytes()
    with out.open('xb') as f:
        f.write(raw)
    sources.append(dict(origin=str(p), snapshot=str(out.relative_to(D)),
                        sha256=sha(p), bytes=len(raw)))
pins = dict(captured_utc=datetime.now(timezone.utc).isoformat(),
    phase='Released-source POST46 after immutable PRE46',
    author_seal_sha256=AUTHOR, pre_seal_sha256=PRE,
    sources=sources, reused_pre_origins=pre['source_origins'],
    transitive_author_metadata_only=[r for r in json.loads((A / 'SOURCE_PINS.json').read_text())['sources']
        if 'native-birth-charge-cluster-' in r['origin']],
    scope='Read only the 16 released author46 files and existing PRE46/permitted parents; no author program execution or transitive source reads.')
after = [identity(p) for p in protected]
assert before == after
with (D / 'POST_SOURCE_PINS.json').open('x') as f:
    json.dump(pins, f, indent=2, sort_keys=True); f.write('\n')
with (D / 'POST_PRESERVATION_BASELINE.json').open('x') as f:
    json.dump(dict(at=datetime.now(timezone.utc).isoformat(), files=before,
                   all_byte_stat_unchanged_during_capture=True), f, indent=2, sort_keys=True)
    f.write('\n')
print(json.dumps(dict(captured_author_files=len(sources), protected_files=len(before),
    pre_members_unchanged=31, author_members_unchanged=15,
    source_pins_sha256=sha(D / 'POST_SOURCE_PINS.json'))))
