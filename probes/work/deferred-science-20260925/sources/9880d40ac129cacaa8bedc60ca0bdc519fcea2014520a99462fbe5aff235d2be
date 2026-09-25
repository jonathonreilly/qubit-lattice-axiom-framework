"""Seal this completed blind PRE; never overwrites an existing seal."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json

base=Path(__file__).resolve().parent
seal=base/'PRE_SEAL.json'
assert not seal.exists(),'PRE seal already exists; preserve it'
members=[]
for path in sorted(base.rglob('*')):
    if not path.is_file() or '__pycache__' in path.parts:continue
    if path.name in ('PRE_SEAL.json','SEAL_EXECUTION.json','SEAL_STDERR.txt'):continue
    members.append({'path':str(path.relative_to(base)),'bytes':path.stat().st_size,
                    'sha256':sha256(path.read_bytes()).hexdigest()})
record={'sealed_utc':datetime.now(timezone.utc).isoformat(),
        'scope':'Blind independent PRE completed before any photon-added-energy author release.',
        'note':'PRE.md','member_count':len(members),'members':members,
        'excluded':'Only generated __pycache__, this seal, and its post-seal execution stdout/stderr.',
        'scientific_status':'Conditional independent derivation and bounded controls, no audit authority.',
        'blinding':'No photon-added-energy author source or runner, other active checker packet, or campaign checkpoint was opened.',
        'prior_packets':'Unchanged; prior 23/24 PRE explicitly reused only as pinned known background.',
        'stop_after_seal':True}
seal.write_text(json.dumps(record,indent=2)+'\n')
for member in members:
    path=base/member['path']
    assert sha256(path.read_bytes()).hexdigest()==member['sha256']
    path.chmod(0o444)
seal.chmod(0o444)
print(json.dumps({'sealed_utc':record['sealed_utc'],'members':len(members),
                  'PRE_sha256':sha256((base/'PRE.md').read_bytes()).hexdigest(),
                  'PRE_SEAL_sha256':sha256(seal.read_bytes()).hexdigest(),
                  'SOURCE_PINS_sha256':sha256((base/'SOURCE_PINS.json').read_bytes()).hexdigest(),
                  'every_member_verified_after_sealing':True},indent=2))
