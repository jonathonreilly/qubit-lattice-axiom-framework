from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
ROOT=Path(__file__).resolve().parent
TARGET=ROOT/'PRE_SEAL.json'
if TARGET.exists(): raise SystemExit('Existing PRE seal preserved; refusing to replace it.')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
pins=json.loads((ROOT/'SOURCE_PINS.json').read_text())
for source in pins['sources']:
    p=ROOT/source['frozen_path']
    assert p.stat().st_size==source['bytes'] and sha(p)==source['sha256'],p
verification=json.loads((ROOT/'EVIDENCE_VERIFICATION.json').read_text())
assert verification['check_count']==33 and all(x['verified'] for x in verification['checks'])
assert (ROOT/'verify_evidence.stderr.txt').stat().st_size==0
assert (ROOT/'verify_evidence.stdout.txt').read_text().endswith('TOTAL 33 evidence checks verified\n')
execution=json.loads((ROOT/'EXECUTION.json').read_text())
assert execution['exit_code']==0
for key,name in [('script_sha256','local_background_control.py'),('result_sha256','CONTROL_RESULTS.json'),('stdout_sha256','local_background_control.stdout.txt'),('stderr_sha256','local_background_control.stderr.txt')]:
    assert execution[key]==sha(ROOT/name),name
members=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file():
        assert p.name!='PRE_SEAL.json'
        members.append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=sha(p)))
seal=dict(phase='blind independent PRE',sealed_at_utc=datetime.now(timezone.utc).isoformat(),
          main_source_commit='0e6ad8285096ed668816f18caaa6fbbfbd9c50e8',
          scope='Full common-rotor local formation-background bound and zero-lag ordered factorial intensity with arbitrary other events.',
          provenance='Root candidate and forbidden active packets unread; inherited model/effort retained; no delegation or author control execution.',
          status='Conditional independent reconstruction, no audit verdict or physical selection.',
          report_sha256=sha(ROOT/'PRE.md'),source_record_count=len(pins['sources']),member_count=len(members),members=members,
          preservation='One-time SHA256 content ledger. All members and seal set read-only. Prior sealed packets remain separate and unchanged.')
with TARGET.open('x') as f: json.dump(seal,f,indent=2);f.write('\n')
for item in members: (ROOT/item['path']).chmod(0o444)
TARGET.chmod(0o444)
for item in members:
    p=ROOT/item['path']; assert sha(p)==item['sha256'] and p.stat().st_size==item['bytes']
print(json.dumps(dict(seal_path=str(TARGET),seal_sha256=sha(TARGET),report_sha256=seal['report_sha256'],member_count=len(members),all_members_reverified=True),indent=2))
