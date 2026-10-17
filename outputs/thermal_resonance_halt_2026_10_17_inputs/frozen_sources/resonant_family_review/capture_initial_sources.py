"""Bookkeeping only. Capture the permitted pre-checker source surface."""
import datetime, hashlib, json, os
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'resonant_family_candidate'
EXPECTED = {
    'CANDIDATE.md': '401e5c2389ef99bd9980898ec118f2476e49dd627d3cf9f32deb812ffc5498f0',
    'FREEZE.json': '8cdf10121e4c42247d4aba730a48413817a62b9ada420adfc6bc70df7df64879',
}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as out:
        out.write(data)
        out.flush()
        os.fsync(out.fileno())

entries = []
for name in ('CANDIDATE.md', 'FREEZE.json', 'SOURCE_MANIFEST.json'):
    src = AUTHOR / name
    data = src.read_bytes()
    if name in EXPECTED:
        assert digest(data) == EXPECTED[name], name
    dst = HERE / 'inputs' / ('author_' + name)
    save(dst, data)
    entries.append(dict(snapshot=str(dst.relative_to(HERE)), original=str(src),
                        sha256=digest(data), bytes=len(data)))

for entry in json.loads((AUTHOR / 'SOURCE_MANIFEST.json').read_text())['entries']:
    src = AUTHOR / entry['snapshot']
    original = Path(entry['original'])
    data = src.read_bytes()
    assert len(data) == entry['bytes'] and digest(data) == entry['sha256']
    assert original.read_bytes() == data, str(original)
    dst = HERE / 'inputs' / Path(entry['snapshot']).name
    save(dst, data)
    entries.append(dict(snapshot=str(dst.relative_to(HERE)), original=str(src),
                        upstream_original=str(original), sha256=digest(data), bytes=len(data),
                        upstream_bytes_equal=True))

record = dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              exposure='Candidate/source manifest/freeze/dependency snapshots only; author scientific code and output not opened.',
              entries=entries)
save(HERE / 'INITIAL_SOURCE_BINDINGS.json', (json.dumps(record, indent=2)+'\n').encode())
print(json.dumps(dict(captured=len(entries), upstream_pairs=21,
                     manifest_sha256=digest((HERE/'INITIAL_SOURCE_BINDINGS.json').read_bytes()))))
