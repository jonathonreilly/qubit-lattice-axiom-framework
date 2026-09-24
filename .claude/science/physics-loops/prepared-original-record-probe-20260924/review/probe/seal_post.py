"""One-time POST seal; all PRE members remain byte-for-byte preserved."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

ROOT=Path(__file__).resolve().parent
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
pre_path=ROOT/'PRE_SEAL.json';pre=json.loads(pre_path.read_text())
assert sha(pre_path)=='5c72901c7a027ba7f00685ce39abe206a2ae0b8a73098ab35e7f0b72324f177c'
for row in pre['members']:
    path=ROOT/row['path'];assert path.stat().st_size==row['bytes'] and sha(path)==row['sha256']
old={row['path'] for row in pre['members']}|{'PRE_SEAL.json'}
seal_path=ROOT/'POST_SEAL.json'
assert not seal_path.exists(),'POST seal exists; preserve it'
members=[]
for path in sorted(ROOT.rglob('*')):
    if not path.is_file() or path==seal_path:continue
    relative=str(path.relative_to(ROOT))
    if relative in old:continue
    members.append(dict(path=relative,bytes=path.stat().st_size,sha256=sha(path)))
seal=dict(phase='released-source POST comparison',sealed_at_utc=datetime.now(timezone.utc).isoformat(),
          preserved_PRE_seal_sha256=sha(pre_path),preserved_PRE_member_count=len(pre['members']),all_PRE_members_unchanged=True,
          author_note_sha256=sha(ROOT/'post_sources/author/PREPARED_MATTER_INTERFERENCE_PROBE_ROOT.md'),
          author_seal_sha256=sha(ROOT/'post_sources/author/AUTHOR_SEAL.json'),
          scope='Actual root preparation, full count and ordered moment proof comparison, own narrow primitive/Gauss control and author evidence correspondence; no author rerun or audit verdict.',
          member_count=len(members),members=members,
          preservation='One-time content-hash ledger. All POST members and this seal set read-only; PRE originals unchanged.')
with seal_path.open('x') as handle:handle.write(json.dumps(seal,indent=2)+'\n')
for row in members:
    path=ROOT/row['path'];assert path.stat().st_size==row['bytes'] and sha(path)==row['sha256'];path.chmod(0o444)
seal_path.chmod(0o444)
print(json.dumps(dict(POST_seal_path=str(seal_path),POST_seal_sha256=sha(seal_path),POST_sha256=sha(ROOT/'POST.md'),
                     POST_member_count=len(members),PRE_members_unchanged=len(pre['members']),all_POST_members_verified=True),indent=2))
