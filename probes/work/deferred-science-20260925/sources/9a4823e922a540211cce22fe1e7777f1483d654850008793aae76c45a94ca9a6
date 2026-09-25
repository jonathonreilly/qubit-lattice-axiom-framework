#!/usr/bin/env python3
"""One-time POST source-snapshot writer, limited to released seal members."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
base=Path(__file__).resolve().parent
author=base.parent/'native-birth-charge-cluster-personal'
seal_path=author/'AUTHOR_SEAL.json'
raw=seal_path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='061b603af09865b1f8673d2332816849f799f504dbadfe54b205e53be9077186'
seal=json.loads(raw)
preseal=base/'PRE_SEAL.json'
assert hashlib.sha256(preseal.read_bytes()).hexdigest()=='61b5a0edaffee445ba80cfd7eb7e25cb60dea3e6aede4b449df2fc2e3dbc7cca'
pre=json.loads(preseal.read_text())
for row in pre['members']:
    assert hashlib.sha256((base/row['path']).read_bytes()).hexdigest()==row['sha256']
root=base/'post_sources'
root.mkdir(exist_ok=False)
rows=[]
for row in seal['members']+[dict(path='AUTHOR_SEAL.json',sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw))]:
    origin=author/row['path']
    data=origin.read_bytes()
    assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256']
    snapshot=root/row['path']
    snapshot.parent.mkdir(parents=True,exist_ok=True)
    snapshot.write_bytes(data)
    snapshot.chmod(0o444)
    rows.append(dict(origin=str(origin),snapshot=str(snapshot.relative_to(base)),sha256=row['sha256'],bytes=len(data)))
manifest=dict(captured_utc=datetime.now(timezone.utc).isoformat(),phase='POST42 released sources',
              scope='Author42 seal and ten expressly released members only; no author program execution/import',
              pre_seal_sha256=hashlib.sha256(preseal.read_bytes()).hexdigest(),
              pre_members_verified=len(pre['members']),sources=rows)
(base/'POST_SOURCE_PINS.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
print(json.dumps(dict(pre_members_unchanged=len(pre['members']),released_origins=len(rows)),indent=2))
