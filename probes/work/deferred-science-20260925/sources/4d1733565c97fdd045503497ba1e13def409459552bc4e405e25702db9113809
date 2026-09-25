"""One-time PRE seal. Refuses to overwrite any existing seal."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

ROOT=Path(__file__).resolve().parent
seal_path=ROOT/'PRE_SEAL.json'
assert not seal_path.exists(), 'PRE seal already exists; preserve it'
members=[]
for path in sorted(ROOT.rglob('*')):
    if not path.is_file() or path==seal_path:
        continue
    data=path.read_bytes()
    members.append(dict(path=str(path.relative_to(ROOT)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
seal=dict(phase='blind independent PRE',sealed_at_utc=datetime.now(timezone.utc).isoformat(),
          main_source_commit='0e6ad8285096ed668816f18caaa6fbbfbd9c50e8',
          scope='Exact supplied physical matter/electric preparation and original one-formation rate effect; bounded weak-field and early first-event consequences.',
          provenance='No root candidate, forbidden active packet, author helper, parent runner or delegated agent used. Prior own readout PRE/POST reuse is explicit.',
          status='Conditional independent reconstruction; no audit verdict, retained-grade claim or publication action.',
          preservation='One-time hash ledger; every member and this seal set read-only. Preserve originals for later POST.',
          member_count=len(members),members=members)
with seal_path.open('x') as handle:
    handle.write(json.dumps(seal,indent=2)+'\n')
for row in members:
    path=ROOT/row['path']
    assert path.stat().st_size==row['bytes'] and hashlib.sha256(path.read_bytes()).hexdigest()==row['sha256']
    path.chmod(0o444)
seal_path.chmod(0o444)
print(json.dumps(dict(seal_path=str(seal_path),seal_sha256=hashlib.sha256(seal_path.read_bytes()).hexdigest(),
                     member_count=len(members),all_members_verified=True,
                     PRE_sha256=hashlib.sha256((ROOT/'PRE.md').read_bytes()).hexdigest()),indent=2))
