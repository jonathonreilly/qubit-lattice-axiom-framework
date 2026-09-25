#!/usr/bin/env python3
from datetime import datetime,timezone
import hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/'selected-mark-power-personal'
SEAL='b0378a615fdaaca99e563a78e4e1361a19635976e114e2f04f5e5485ceb8a69c'
NOTE='dc34643135d5b31b627420ba6bc325b7d5b5dbf9095e6801d25b26d1dd8c66c6'
PRE='a1cc8dc5b9af73952b55402902076e1b7b28b7bc7bbc2de4834c65dd8297031d'
def sha(data):return hashlib.sha256(data).hexdigest()
assert sha((ROOT/'AUTHOR_SEAL.json').read_bytes())==SEAL
assert sha((ROOT/'ORIGINAL_SELECTED_MARK_ENERGY_POWER_ROOT.md').read_bytes())==NOTE
assert sha((HERE/'PRE_SEAL.json').read_bytes())==PRE
pre=json.loads((HERE/'PRE_SEAL.json').read_text())
for row in pre['members']:
 data=(HERE/row['path']).read_bytes();assert len(data)==row['bytes'] and sha(data)==row['sha256']
seal=json.loads((ROOT/'AUTHOR_SEAL.json').read_text());assert len(seal['files'])==18
sources=[]
for rel,row in [('AUTHOR_SEAL.json',dict(sha256=SEAL,bytes=(ROOT/'AUTHOR_SEAL.json').stat().st_size))]+list(seal['files'].items()):
 assert not Path(rel).is_absolute() and '..' not in Path(rel).parts
 data=(ROOT/rel).read_bytes();assert len(data)==row['bytes'] and sha(data)==row['sha256']
 target=HERE/'post_sources'/'author'/rel;target.parent.mkdir(parents=True,exist_ok=True)
 with target.open('xb') as f:f.write(data)
 sources.append(dict(origin=str(ROOT/rel),frozen_path=str(target.relative_to(HERE)),bytes=len(data),sha256=sha(data),
   role='released root source or author evidence; never executed or imported'))
prior=json.loads((HERE/'SOURCE_PINS.json').read_text())
for row in prior['sources']:
 assert sha(Path(row['origin']).read_bytes())==row['sha256']
result=dict(phase='Released-source POST',created_utc=datetime.now(timezone.utc).isoformat(),
 author_sources=sources,reused_PRE_sources=prior['sources'],PRE_seal_sha256=PRE,PRE_members_unchanged=65,
 author_seal_members=18,author_private_reuse_references_followed=False,
 forbidden_other_packets_read=False,author_code_run_or_imported=False)
with (HERE/'POST_SOURCE_PINS.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result,indent=2))
