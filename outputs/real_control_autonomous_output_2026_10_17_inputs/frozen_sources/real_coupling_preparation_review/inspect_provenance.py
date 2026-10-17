#!/usr/bin/env python3
"""Bookkeeping only; no imports/replays of any scientific checker."""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path

R=Path(__file__).resolve().parent
A=R.parent/'real_coupling_preparation_candidate'
def identity(p,generation=False):
    p=Path(p);b=p.read_bytes()
    d={'bytes':len(b),'sha256':sha256(b).hexdigest()}
    if generation:
        s=p.stat();d.update(path=str(p.resolve()),device=s.st_dev,inode=s.st_ino,mtime_ns=s.st_mtime_ns)
    return d
def save(path,obj):
    with path.open('x') as f:
        json.dump(obj,f,indent=2,sort_keys=True);f.write('\n');f.flush();os.fsync(f.fileno())
af=json.loads((R/'ANALYTIC_FREEZE.json').read_text())
for e in af['files']:
    assert identity(R/e['path'])=={k:e[k] for k in ('bytes','sha256')},e['path']
fr=json.loads((A/'FREEZE.json').read_text())
assert identity(A/'FREEZE.json')['sha256']=='41ce93b77d46c1dbecdde6f674201ca8b6e20026ae10231fe9b925fb69468e49'
for key in ('candidate','source_map','final_check','manifest'):
    e=fr[key];assert identity(A/e['path'])=={k:e[k] for k in ('bytes','sha256')}
manifest=json.loads((A/'FILE_MANIFEST.json').read_text())
members=manifest['members']
assert len(members)==fr['member_count']
expected={e['path'] for e in members}|{'FILE_MANIFEST.json','FREEZE.json'}
assert expected=={str(p.relative_to(A)) for p in A.rglob('*') if p.is_file()}
inventory=[]
for name in sorted(expected):
    src=A/name;d=identity(src)
    if name not in ('FILE_MANIFEST.json','FREEZE.json'):
        e=next(x for x in members if x['path']==name)
        assert d=={k:e[k] for k in ('bytes','sha256')}
    dest=R/'author_packet'/name;dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open('xb') as f:f.write(src.read_bytes())
    inventory.append({'source':str(src),'snapshot':str(dest.relative_to(R)),**d})

pairs=[]
for e in json.loads((A/'SOURCE_MAP.json').read_text())['sources']:
    d=identity(Path(e['original']),True)
    assert {k:d[k] for k in ('bytes','sha256')}==identity(A/e['snapshot'])
    assert all(d[k]==e[k] for k in ('bytes','sha256','device','inode','mtime_ns'))
    pairs.append({'snapshot':e['snapshot'],'current_original':d,'unchanged':True})

attempts=[]
for name in ('run01','run02'):
    run=A/name;pre=json.loads((run/'PRELAUNCH.json').read_text());rec=json.loads((run/'RECEIPT.json').read_text())
    assert pre['input_bindings']==rec['input_bindings_after']
    assert pre['runtime_bindings']==rec['runtime_bindings_after']
    bindings=[]
    for e in pre['input_bindings']+pre['runtime_bindings']:
        actual=identity(Path(e['path']),True)
        assert actual==e
        bindings.append({'identity':actual,'matches_pre_and_post':True})
    assert identity(run/'PRELAUNCH.json',True)==rec['prelaunch']
    for stream in ('stdout','stderr'):
        assert identity(Path(rec[stream]['path']),True)==rec[stream]
    assert datetime.fromisoformat(pre['captured_utc'])<datetime.fromisoformat(rec['started_utc'])<datetime.fromisoformat(rec['completed_utc'])
    assert rec['limits']=={'cpu_soft_hard_seconds':[20,20],'external_wall_seconds':30,'memory_cap':None}
    assert rec['all_bound_files_unchanged'] and not rec['timed_out']
    attempts.append({'run':name,'prelaunch':identity(run/'PRELAUNCH.json'),
        'receipt':identity(run/'RECEIPT.json'),'input_count':len(pre['input_bindings']),
        'runtime_count':len(pre['runtime_bindings']),'bindings_current':bindings,
        'captured_utc':pre['captured_utc'],'started_utc':rec['started_utc'],'completed_utc':rec['completed_utc'],
        'exit_code':rec['exit_code'],'status':rec['status'],
        'wall_seconds':rec['wall_seconds'],'cpu_user_seconds':rec['cpu_user_seconds'],
        'cpu_system_seconds':rec['cpu_system_seconds'],'rss_bytes':rec['child_maxrss_native_units'],
        'limits':rec['limits']})
assert attempts[0]['exit_code']==1 and attempts[1]['exit_code']==0
assert (A/'run01/stdout.json').read_bytes()==b''
assert b'ModuleNotFoundError' in (A/'run01/stderr.txt').read_bytes()
assert (A/'run02/stderr.txt').read_bytes()==b''
assert identity(A/'check_preparation.py')==identity(A/'run01/executed_source.py')==identity(A/'run02/executed_source.py')
out=json.loads((A/'run02/stdout.json').read_text())
assert identity(A/'check_preparation.py')['sha256']==out['executed_source_sha256']
assert all(e['passed'] is True for e in out['checks'])
for name in ('run01','run02'):
    pre=json.loads((A/name/'PRELAUNCH.json').read_text())
    cp=next(e for e in pre['input_bindings'] if e['path']==str(A/'CANDIDATE.md'))
    assert identity(A/'CANDIDATE.md',True)==cp
retry_ns=(A/'RETRY_AMENDMENT.md').stat().st_mtime_ns
retry_utc=datetime.fromtimestamp(retry_ns/10**9,timezone.utc).isoformat()
assert datetime.fromisoformat(attempts[0]['completed_utc'])<datetime.fromisoformat(retry_utc)<datetime.fromisoformat(attempts[1]['captured_utc'])
assert datetime.fromisoformat(attempts[1]['completed_utc'])<datetime.fromisoformat(fr['frozen_utc'])<datetime.fromisoformat(af['frozen_utc'])
result={'checked_utc':datetime.now(timezone.utc).isoformat(),
    'operation':'copy/hash/generation/record consistency only; no scientific execution or author replay',
    'review_scientific_runs':0,'analytical_entries_unchanged':len(af['files']),
    'author_inventory':inventory,'source_pairs':pairs,'attempts':attempts,
    'retry_amendment_mtime_utc':retry_utc,'author_freeze_utc':fr['frozen_utc'],
    'review_analysis_freeze_utc':af['frozen_utc'],
    'candidate_and_checker_identical_across_attempts':True,
    'saved_check_count':len(out['checks']),'check_count_is_not_independent_proof':True,
    'checker_scope_finding':'Last ramp_error_and_complete_trace_ceiling first clause is a non-discriminating endpoint comparison, not a check of the Duhamel ramp theorem. Independent analytic proof and earlier supported Gram checks provide that support.',
    'private_root_idea_accessed':False,'realifier_dependency_status':'provisional; no root qualification inferred'}
save(R/'PROVENANCE.json',result)
summary={'author_members_verified':len(members),'author_total_files_copied':len(inventory),
    'source_pairs_verified':len(pairs),'review_analytic_entries_unchanged':len(af['files']),
    'attempt_bindings':[{'run':e['run'],'inputs':e['input_count'],'runtimes':e['runtime_count']} for e in attempts],
    'review_scientific_runs':0,'provenance':identity(R/'PROVENANCE.json')}
save(R/'PROVENANCE_SUMMARY.json',summary)
print(json.dumps(summary,indent=2))
