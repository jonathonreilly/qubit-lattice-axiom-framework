"""One-time personal candidate seal; never rerun as a verifier."""
from pathlib import Path
import datetime,hashlib,json
P=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert not (P/'AUTHOR_SEAL.json').exists()
for row in json.loads((P/'SOURCE_PINS.json').read_text())['sources']:
    assert sha(Path(row['path']))==row['sha256']
note=P/'LOCAL_CHARGE_FINITE_TIME_COVARIANCE_ROOT.md'
assert sha(note)=='9a83191276a1a0380158ef88961c1d36b0d82c9cd645210739c999c4568f464a'
assert json.loads((P/'ROOT_READ_RECEIPT.json').read_text())['required_repairs']==[]
members=[]
for p in sorted(P.rglob('*')):
    if not p.is_file():continue
    assert '__pycache__' not in p.parts
    members.append(dict(path=str(p.relative_to(P)),sha256=sha(p),bytes=p.stat().st_size))
j=dict(sealed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='Personal candidate47 before independent disclosure; candidate46 explicitly provisional. No empirical prediction or audit status.',note_sha256=sha(note),members=members)
with (P/'AUTHOR_SEAL.json').open('x') as f:json.dump(j,f,indent=2);f.write('\n')
for row in members:(P/row['path']).chmod(0o444)
(P/'AUTHOR_SEAL.json').chmod(0o444)
print(json.dumps(dict(note_sha256=sha(note),seal_sha256=sha(P/'AUTHOR_SEAL.json'),members=len(members)),indent=2))
