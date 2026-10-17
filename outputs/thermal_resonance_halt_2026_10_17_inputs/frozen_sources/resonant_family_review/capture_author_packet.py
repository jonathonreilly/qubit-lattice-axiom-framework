"""Read-only validation/capture after the independent derivation/run freeze."""
import datetime,hashlib,json,os
from pathlib import Path
ROOT=Path(__file__).resolve().parent
AUTHOR=ROOT.parent/'resonant_family_candidate'
def h(data):return hashlib.sha256(data).hexdigest()
def save(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as out:out.write(data);out.flush();os.fsync(out.fileno())
fr=json.loads((ROOT/'INDEPENDENT_FREEZE.json').read_text())
for x in fr['entries']:
    data=(ROOT/x['path']).read_bytes()
    assert len(data)==x['bytes'] and h(data)==x['sha256'],x['path']
manifest=json.loads((AUTHOR/'FILE_MANIFEST.json').read_text())
for x in manifest['files']:
    data=(AUTHOR/x['path']).read_bytes()
    assert len(data)==x['bytes'] and h(data)==x['sha256'],x['path']
actual={str(p.relative_to(AUTHOR)) for p in AUTHOR.rglob('*') if p.is_file()}
assert actual=={x['path'] for x in manifest['files']}|{'FILE_MANIFEST.json','FREEZE.json'}
entries=[]
for rel in sorted(actual):
    source=AUTHOR/rel;data=source.read_bytes();dst=ROOT/'author_packet'/rel
    save(dst,data)
    entries.append(dict(snapshot=str(dst.relative_to(ROOT)),original=str(source),bytes=len(data),sha256=h(data)))
record=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    independent_freeze_sha256=h((ROOT/'INDEPENDENT_FREEZE.json').read_bytes()),
    independent_frozen_entries_unchanged=len(fr['entries']),
    exposure='Author code/output only accessed after the separate derivation and actual run were frozen.',entries=entries)
save(ROOT/'AUTHOR_CAPTURE_BINDINGS.json',(json.dumps(record,indent=2)+'\n').encode())
print(json.dumps(dict(captured_author_files=len(entries),independent_frozen_entries_unchanged=len(fr['entries']))))
