#!/usr/bin/env python3
"""Exclusive POST seal, preserving the earlier immutable PRE."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(name):return json.loads((HERE/name).read_text())
seal=HERE/'POST_SEAL.json';assert not seal.exists()
pre=read('PRE_SEAL.json')
assert sha(HERE/'PRE_SEAL.json')=='bed28ea9c81afb7822d0ddeeb552260e3e0547b6f387c9edb8dbd6aec83ee25b'
prior={r['path'] for r in pre['members']}|{'PRE_SEAL.json'}
for r in pre['members']:
    p=HERE/r['path'];assert sha(p)==r['sha256'] and p.stat().st_size==r['bytes']
verification=read('POST_FINAL_VERIFICATION.json')
assert verification==read('post_verify.stdout.txt')
assert verification['all_checks_satisfied'] and verification['POST_sha256']==sha(HERE/'POST.md')
receipt=read('post_verify.execution.json')
assert receipt['exit_code']==0 and receipt['script_sha256']==sha(HERE/'post_verify_evidence.py')
for stream in ('stdout','stderr'):
    p=HERE/('post_verify.'+stream+'.txt')
    assert sha(p)==receipt[stream+'_sha256'] and p.stat().st_size==receipt[stream+'_bytes']
for source in read('POST_SOURCE_PINS.json')['sources']:
    assert sha(HERE/source['frozen_path'])==source['sha256']
    if source.get('role')!='Procedure only':assert sha(Path(source['origin']))==source['sha256']
members=[]
for p in sorted(x for x in HERE.rglob('*') if x.is_file()):
    name=str(p.relative_to(HERE))
    if name in prior:continue
    assert name!='POST_SEAL.json'
    members.append(dict(path=name,bytes=p.stat().st_size,sha256=sha(p)))
data=dict(created_utc=datetime.now(timezone.utc).isoformat(),phase='Released-source POST',
    status='Selective conditional comparison; no audit verdict',
    prior_PRE_seal_sha256=sha(HERE/'PRE_SEAL.json'),unchanged_PRE_member_count=len(pre['members']),
    POST_sha256=sha(HERE/'POST.md'),
    author_primary_sha256='e177784652f4c6fafb344ddc72ac20144ebabb9b063e009a1a8618529f8ef922',
    author_seal_sha256='69a754ada477506f4437705dbb49e8ebe93b3c230185b7376b3b8d6bfb18dc6d',
    author_programs_executed_or_imported=False,author_or_PRE_files_modified=False,
    members=members,preservation='New members and seal made read-only; earlier PRE unchanged')
with seal.open('x') as out:json.dump(data,out,indent=2);out.write('\n')
for r in members:
    p=HERE/r['path'];assert sha(p)==r['sha256'];p.chmod(0o444)
seal.chmod(0o444)
print(json.dumps(dict(seal_path=str(seal),seal_sha256=sha(seal),POST_sha256=sha(HERE/'POST.md'),
    member_count=len(members),all_new_members_reverified=True,
    unchanged_PRE_members=len(pre['members'])),indent=2))
