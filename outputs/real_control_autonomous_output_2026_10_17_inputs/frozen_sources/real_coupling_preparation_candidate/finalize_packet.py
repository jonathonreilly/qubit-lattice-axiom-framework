#!/usr/bin/env python3
"""Deterministic identity/freeze bookkeeping only; no scientific replay."""
import ast
import datetime
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def entry(path):
    p = Path(path)
    return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)}


def write(path,obj):
    with Path(path).open('x') as f:
        json.dump(obj,f,indent=2)
        f.write('\n')
        f.flush()
        os.fsync(f.fileno())


sources = json.loads((ROOT/'SOURCE_MAP.json').read_text())['sources']
source_checks = []
for s in sources:
    local, original = ROOT/s['snapshot'],Path(s['original'])
    assert sha(local)==s['sha256']==sha(original),s['snapshot']
    st = original.stat()
    assert (st.st_dev,st.st_ino,st.st_mtime_ns)==(s['device'],s['inode'],s['mtime_ns']),s['snapshot']
    source_checks.append({'snapshot':s['snapshot'],'original':str(original),'sha256':s['sha256'],
                          'original_and_snapshot_unchanged':True})
attempts = []
for name in ('run01','run02'):
    run=ROOT/name
    pre=json.loads((run/'PRELAUNCH.json').read_text())
    receipt=json.loads((run/'RECEIPT.json').read_text())
    assert pre['input_bindings']==receipt['input_bindings_after']
    assert pre['runtime_bindings']==receipt['runtime_bindings_after']
    for b in pre['input_bindings']+pre['runtime_bindings']:
        p=Path(b['path']);st=p.stat()
        assert sha(p)==b['sha256'],str(p)
        assert (st.st_dev,st.st_ino,st.st_mtime_ns)==(b['device'],b['inode'],b['mtime_ns']),str(p)
    assert sha(run/'PRELAUNCH.json')==receipt['prelaunch']['sha256']
    for stream in ('stdout','stderr'):
        assert sha(Path(receipt[stream]['path']))==receipt[stream]['sha256']
    assert pre['captured_utc']<receipt['started_utc']<receipt['completed_utc']
    attempts.append({'name':name,'status':receipt['status'],'exit_code':receipt['exit_code'],
                     'prelaunch_inputs':len(pre['input_bindings']),
                     'runtime_bindings':len(pre['runtime_bindings']),
                     'all_current_bindings_unchanged':True,
                     'wall_seconds':receipt['wall_seconds'],
                     'cpu_seconds':receipt['cpu_user_seconds']+receipt['cpu_system_seconds'],
                     'limits':receipt['limits']})
assert attempts[0]['status']=='failure' and attempts[1]['status']=='ok'
assert 'ModuleNotFoundError' in (ROOT/'run01/stderr.txt').read_text()
assert (ROOT/'run01/stdout.json').read_bytes()==b''
assert (ROOT/'run02/stderr.txt').read_bytes()==b''
payload=json.loads((ROOT/'run02/stdout.json').read_text())
assert len(payload['checks'])==90 and all(c['passed'] is True for c in payload['checks'])
assert sha(ROOT/'check_preparation.py')==sha(ROOT/'run01/executed_source.py')==sha(ROOT/'run02/executed_source.py')
assert sha(ROOT/'CANDIDATE.md')=='57e1cebcee12bf6499564051f91f981fe11814d73d45b9e1168c045e65ab9b8c'
for p in sorted(ROOT.rglob('*.py')):
    ast.parse(p.read_text())
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
check={'checked_utc':now,'operation':'deterministic file/receipt/syntax checks only; no scientific replay',
       'source_pairs':source_checks,'attempts':attempts,'scientific_checks_in_saved_output':90,
       'checker_and_proof_identical_across_attempts':True,
       'scientific_attempts_total':2,'attempts_reaching_science':1,
       'new_science_runs_by_this_finalizer':0,'candidate':entry(ROOT/'CANDIDATE.md'),
       'scope':'Proposed conditional preparation route; no root/private pulse idea read; realifier review remains pending.',
       'writes_confined_to':str(ROOT),'editable_prompt_files_changed':[],
       'repository_Git_PR_checkpoint_axiom_audit_writes':False}
write(ROOT/'FINAL_CHECK.json',check)
members=[entry(p) for p in sorted(ROOT.rglob('*')) if p.is_file()
         and p.name not in ('FILE_MANIFEST.json','FREEZE.json')]
manifest={'created_utc':now,'scope':'All current files in this exclusively owned packet, excluding the manifest/freeze themselves.',
          'members':members}
write(ROOT/'FILE_MANIFEST.json',manifest)
freeze={'frozen_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'status':'frozen proposed conditional theorem and bounded corroboration, not independent/root acceptance',
        'candidate':entry(ROOT/'CANDIDATE.md'),'source_map':entry(ROOT/'SOURCE_MAP.json'),
        'final_check':entry(ROOT/'FINAL_CHECK.json'),'manifest':entry(ROOT/'FILE_MANIFEST.json'),
        'member_count':len(members),'failure_retained':True,
        'private_root_construction_exposure':'none through freeze',
        'scientific_attempt_cap_used':'two child launches: one import failure, one scientific success',
        'next_decision':'Separate review of local preparation, release and realifier-to-resonance interface.',
        'no_further_writes_to_frozen_members_without_separate_record':True}
write(ROOT/'FREEZE.json',freeze)
fd=os.open(ROOT,os.O_RDONLY)
try:
    os.fsync(fd)
finally:
    os.close(fd)
print(json.dumps({'members':len(members),'source_pairs':len(source_checks),'attempts':attempts,
                  'candidate':entry(ROOT/'CANDIDATE.md'),'manifest':entry(ROOT/'FILE_MANIFEST.json'),
                  'freeze':entry(ROOT/'FREEZE.json')},indent=2))
