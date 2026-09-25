#!/usr/bin/env python3
"""One-time POST42 seal writer. Leaves every PRE member and seal untouched."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json
base=Path(__file__).resolve().parent
target=base/'POST_SEAL.json'
assert not target.exists()
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
pre=json.loads((base/'PRE_SEAL.json').read_text())
pre_sha=digest(base/'PRE_SEAL.json')
assert pre_sha=='61b5a0edaffee445ba80cfd7eb7e25cb60dea3e6aede4b449df2fc2e3dbc7cca'
old=set(row['path'] for row in pre['members'])|{'PRE_SEAL.json'}
pre_before={str(base/name):(base/name).stat() for name in old}
for row in pre['members']:
    assert digest(base/row['path'])==row['sha256']
pins=json.loads((base/'POST_SOURCE_PINS.json').read_text())
for row in pins['sources']:
    assert digest(Path(row['origin']))==digest(base/row['snapshot'])==row['sha256']
receipt=json.loads((base/'post_verification_attempt01/EXECUTION.json').read_text())
assert receipt['exit_code']==0 and receipt['observed_unchanged']
assert receipt['observed_before']==receipt['observed_after']
for name,row in receipt['observed_after'].items():
    p=Path(name)
    assert digest(p)==row['sha256'] and p.stat().st_size==row['size']
    assert p.stat().st_mtime_ns==row['mtime_ns'] and p.stat().st_mode==row['mode']
assert digest(base/'post_verification_attempt01/stdout.json')==receipt['stdout_sha256']
assert digest(base/'post_verification_attempt01/stderr.txt')==receipt['stderr_sha256']
assert (base/'post_verification_attempt01/stderr.txt').read_bytes()==b''
new=[p for p in sorted(base.rglob('*')) if p.is_file() and str(p.relative_to(base)) not in old]
assert all(not p.is_symlink() for p in new)
members=[dict(path=str(p.relative_to(base)),sha256=digest(p),bytes=p.stat().st_size) for p in new]
seal=dict(sealed_utc=datetime.now(timezone.utc).isoformat(),phase='POST42 released-source comparison',
          report='POST.md',report_sha256=digest(base/'POST.md'),
          pre_seal_sha256=pre_sha,preserved_PRE_members=pre['members'],
          source_origins=pins['sources'],members=members,member_count=len(members),
          readonly_verifier='post_verify_readonly.py',verification_report='post_verification_attempt01/stdout.json',
          author_program_execution_or_import=False,additional_agents=False,
          publication_or_audit_mutations=False,
          scope='Complete released candidate42; no new blind derivation; unchanged PRE attribution retained')
with target.open('x') as out:
    out.write(json.dumps(seal,indent=2,sort_keys=True)+'\n')
for p in new+[target]:
    p.chmod(0o444)
for row in pre['members']:
    assert digest(base/row['path'])==row['sha256']
assert digest(base/'PRE_SEAL.json')==pre_sha
for name,stat in pre_before.items():
    now=Path(name).stat()
    assert now.st_size==stat.st_size and now.st_mtime_ns==stat.st_mtime_ns and now.st_mode==stat.st_mode
for row in members:
    assert digest(base/row['path'])==row['sha256']
print(json.dumps(dict(POST_sha256=seal['report_sha256'],POST_SEAL_sha256=digest(target),
                     POST_members=len(members),PRE_members_preserved=len(pre['members']),
                     released_origins=len(pins['sources']),all_members_reverified=True),indent=2,sort_keys=True))
