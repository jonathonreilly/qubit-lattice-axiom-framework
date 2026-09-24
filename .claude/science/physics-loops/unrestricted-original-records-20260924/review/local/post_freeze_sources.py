from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
ROOT=Path(__file__).resolve().parent
AUTHOR=ROOT.parent/'local-record-background-personal'
DEST=ROOT/'post_sources/author'
DEST.mkdir(parents=True,exist_ok=True)
def sha(b): return hashlib.sha256(b).hexdigest()
pre=ROOT/'PRE_SEAL.json'
assert sha(pre.read_bytes())=='3acf0388bdfdcad3ee4d5b829eeff1d0a65509c36d732b8ad9b449c415793196'
preseal=json.loads(pre.read_text())
for m in preseal['members']:
    p=ROOT/m['path']; assert sha(p.read_bytes())==m['sha256'] and p.stat().st_size==m['bytes'],m['path']
print('all',preseal['member_count'],'PRE members preserved')
sealpath=AUTHOR/'AUTHOR_CONTROL_SEAL.json'
sealbytes=sealpath.read_bytes()
assert sha(sealbytes)=='455aaba6c0bd18da70176272ed9df914c04f8101bd8e826a81a78495f9af1b18'
seal=json.loads(sealbytes)
assert len(seal['files'])==7
expected=dict(seal['files'])
expected[sealpath.name]=sha(sealbytes)
assert expected['LOCAL_RECORD_BACKGROUND_STABILITY_ROOT.md']=='9f21fae1ea269c0316757d7618d3b50161bd26c4da5759325187c64531220843'
rows=[]
for name,digest in sorted(expected.items()):
    b=(AUTHOR/name).read_bytes(); assert sha(b)==digest,name
    p=DEST/name
    if p.exists(): assert p.read_bytes()==b,name
    else:p.write_bytes(b)
    row=dict(origin=str(AUTHOR/name),frozen_path=str(p.relative_to(ROOT)),bytes=len(b),sha256=digest,
             role='released root argument or author-only finite evidence; no independent author execution')
    rows.append(row);print(json.dumps(row,sort_keys=True))
result=dict(phase='released-source POST',frozen_utc=datetime.now(timezone.utc).isoformat(),
            preserved_PRE_seal_sha256=sha(pre.read_bytes()),preserved_PRE_member_count=preseal['member_count'],
            author_seal_sha256=sha(sealbytes),sources=rows)
(ROOT/'POST_SOURCE_PINS.json').write_text(json.dumps(result,indent=2)+'\n')
print('complete released packet frozen:',len(rows),'files; no other author packet read')
