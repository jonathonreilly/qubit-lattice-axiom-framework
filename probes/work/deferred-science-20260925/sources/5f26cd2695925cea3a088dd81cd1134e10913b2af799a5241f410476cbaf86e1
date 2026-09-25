from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parent
TARGET=ROOT/'POST_SEAL.json'
if TARGET.exists():raise SystemExit('Existing POST seal preserved; refusing replacement.')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
prepath=ROOT/'PRE_SEAL.json'
assert sha(prepath)=='3acf0388bdfdcad3ee4d5b829eeff1d0a65509c36d732b8ad9b449c415793196'
pre=json.loads(prepath.read_text())
excluded={'PRE_SEAL.json'}
for member in pre['members']:
    p=ROOT/member['path'];assert sha(p)==member['sha256'] and p.stat().st_size==member['bytes'],p
    excluded.add(member['path'])
pins=json.loads((ROOT/'POST_SOURCE_PINS.json').read_text())
for item in pins['sources']:
    p=ROOT/item['frozen_path'];assert sha(p)==sha(Path(item['origin']))==item['sha256'],p
for item in json.loads((ROOT/'POST_REFERENCE_PINS.json').read_text())['sources']:
    p=ROOT/item['frozen_path'];assert sha(p)==item['sha256'] and p.stat().st_size==item['bytes'],p
execution=json.loads((ROOT/'POST_CHECK_EXECUTION.json').read_text())
assert execution['exit_code']==0
for key,name in [('script_sha256','post_check_evidence.py'),('stdout_sha256','post_check_evidence.stdout.txt'),('stderr_sha256','post_check_evidence.stderr.txt'),('result_sha256','POST_CHECK_RESULTS.json')]:
    assert execution[key]==sha(ROOT/name),name
result=json.loads((ROOT/'POST_CHECK_RESULTS.json').read_text())
stdout=(ROOT/'post_check_evidence.stdout.txt').read_text().splitlines()
assert [json.loads(s) for s in stdout[:-1]]==result['checks']
assert result['check_count']==34 and all(x['verified'] for x in result['checks'])
assert stdout[-1]=='TOTAL 34 POST correspondence checks verified'
for name in ['post_check_evidence.stderr.txt','post_freeze_sources.stderr.txt','post_freeze_reference.stderr.txt']:
    assert (ROOT/name).stat().st_size==0,name
members=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and str(p.relative_to(ROOT)) not in excluded:
        members.append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=sha(p)))
seal=dict(phase='released-source independent POST',sealed_at_utc=datetime.now(timezone.utc).isoformat(),
          preserved_PRE_seal_sha256=sha(prepath),preserved_PRE_member_count=len(pre['members']),all_PRE_members_unchanged=True,
          author_seal_sha256=pins['author_seal_sha256'],author_note_sha256=sha(ROOT/'post_sources/author/LOCAL_RECORD_BACKGROUND_STABILITY_ROOT.md'),
          scope='Local-background candidate proof, cutoff removal, factorial count scope and complete author-control correspondence; no author execution or unreleased count extension.',
          report_sha256=sha(ROOT/'POST.md'),member_count=len(members),members=members,
          preservation='Separate one-time content-hash ledger; members and seal read-only; all prior PRE files preserved.',
          status='Conditional comparison, no audit verdict or publication action.')
with TARGET.open('x') as f:json.dump(seal,f,indent=2);f.write('\n')
for item in members:(ROOT/item['path']).chmod(0o444)
TARGET.chmod(0o444)
for item in members:assert sha(ROOT/item['path'])==item['sha256']
print(json.dumps(dict(seal_path=str(TARGET),seal_sha256=sha(TARGET),report_sha256=seal['report_sha256'],member_count=len(members),PRE_members_preserved=len(pre['members'])),indent=2))
