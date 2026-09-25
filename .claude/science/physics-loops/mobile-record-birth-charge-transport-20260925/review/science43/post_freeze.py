"""New POST43 source freeze; only explicit released seal members are read."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import subprocess

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'native-birth-cluster-transport-personal'
SEAL_HASH = '897ee094e3766f845645260bc7d6f121ed98053d585fd6db04993db81efbeae6'

def hash_bytes(raw):
    return sha256(raw).hexdigest()

def observed(path):
    st = path.stat()
    raw = path.read_bytes()
    return dict(path=str(path), sha256=hash_bytes(raw), bytes=len(raw),
                dev=st.st_dev, ino=st.st_ino, mode=st.st_mode,
                mtime_ns=st.st_mtime_ns, ctime_ns=st.st_ctime_ns, nlink=st.st_nlink)

def write(name, obj):
    with (HERE / name).open('x') as f:
        json.dump(obj, f, indent=2)
        f.write('\n')

pre = json.loads((HERE / 'PRE_SEAL.json').read_text())
before = []
for row in pre['members']:
    seen = observed(HERE / row['path'])
    assert seen['sha256'] == row['sha256'] and seen['bytes'] == row['bytes']
    before.append(seen)
for name in ('PRE_SEAL.json', 'PRE_SEAL_RECEIPT.json'):
    before.append(observed(HERE / name))
write('POST_PRESERVATION_BEFORE.json', {
    'at_utc': datetime.now(timezone.utc).isoformat(), 'files': before,
    'stat_scope': 'Stable identity/mode/size/mtime/ctime/link count; access time excluded because files are read.'})

seal_raw = (AUTHOR / 'AUTHOR_SEAL.json').read_bytes()
assert hash_bytes(seal_raw) == SEAL_HASH
author_seal = json.loads(seal_raw)
assert len(author_seal['members']) == 11
pins = []
for row in [{'path':'AUTHOR_SEAL.json', 'sha256':SEAL_HASH, 'bytes':len(seal_raw)}, *author_seal['members']]:
    relative = Path(row['path'])
    assert not relative.is_absolute() and '..' not in relative.parts
    origin = AUTHOR / relative
    raw = origin.read_bytes()
    assert hash_bytes(raw) == row['sha256'] and len(raw) == row['bytes']
    frozen = HERE / 'post_sources' / 'author' / relative
    frozen.parent.mkdir(parents=True, exist_ok=True)
    with frozen.open('xb') as f:
        f.write(raw)
    pins.append(dict(origin=str(origin), frozen_path=str(frozen.relative_to(HERE)),
                     sha256=row['sha256'], bytes=row['bytes'],
                     role='Released author evidence, not independent execution',
                     observed_origin=observed(origin)))

parent_checks=[]
for row in json.loads((HERE / 'SOURCE_PINS.json').read_text())['sources']:
    frozen=HERE / row['frozen_path']
    raw=frozen.read_bytes()
    assert hash_bytes(raw)==row['sha256']
    if row['origin'].startswith('git:'):
        origin_raw=subprocess.check_output(['git','-C',row['repository'],'show',row['revision']+':AGENTS.md'])
    else:
        origin_raw=Path(row['origin']).read_bytes()
    assert origin_raw==raw
    parent_checks.append(dict(origin=row['origin'], sha256=row['sha256'],
                              frozen_path=row['frozen_path'], exact_current_bytes=True))

result = dict(at_utc=datetime.now(timezone.utc).isoformat(), phase='Released-source POST43',
              author_seal_sha256=SEAL_HASH, author_members=11, author_sources=pins,
              reused_unchanged_parent_and_procedure_pins=parent_checks,
              prior_pre_seal_sha256=hash_bytes((HERE/'PRE_SEAL.json').read_bytes()),
              forbidden_reference_origins_not_followed=True,
              author_programs_imported_or_executed=False,
              old_sealed_writers_executed=False)
write('POST_SOURCE_PINS.json',result)
print(json.dumps(result,indent=2))
