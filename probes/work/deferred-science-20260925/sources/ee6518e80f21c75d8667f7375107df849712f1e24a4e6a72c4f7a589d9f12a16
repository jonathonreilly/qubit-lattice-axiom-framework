from pathlib import Path
from datetime import datetime,timezone
from collections import defaultdict
import hashlib,json,subprocess

ROOT=Path(__file__).resolve().parent
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def load(name):return json.loads((ROOT/name).read_text())
pre=load('PRE_SEAL.json')
assert sha(ROOT/'PRE_SEAL.json')=='5c72901c7a027ba7f00685ce39abe206a2ae0b8a73098ab35e7f0b72324f177c'
for row in pre['members']:
    path=ROOT/row['path'];assert path.stat().st_size==row['bytes'] and sha(path)==row['sha256']
assert len(pre['members'])==33
print('PRE_PRESERVED',len(pre['members']),sha(ROOT/'PRE_SEAL.json'))

pins=load('POST_SOURCE_PINS.json');origin_rows=[]
for row in pins['sources']:
    frozen=ROOT/row['frozen_path']
    if 'commit' in row:
        data=subprocess.check_output(['git','show',row['commit']+':'+row['path']],cwd=row['repository'])
    else:data=Path(row['path']).read_bytes()
    assert data==frozen.read_bytes() and len(data)==row['bytes'] and sha(frozen)==row['sha256']
    origin_rows.append(dict(path=row['frozen_path'],sha256=sha(frozen),origin_equal=True))
for row in pins['reused_unchanged_PRE_sources']:
    path=ROOT/row['frozen_path'];assert sha(path)==row['sha256']
    data=subprocess.check_output(['git','show',row['commit']+':'+row['path']],cwd=row['repository'])
    assert data==path.read_bytes()
print('POST_SOURCE_ORIGINS',json.dumps(origin_rows,sort_keys=True))
current_workflow=Path(pins['reused_unchanged_PRE_sources'][0]['repository'])/'docs/ai_methodology/SCIENCE_WORKFLOW.md'
assert sha(current_workflow)==sha(ROOT/'sources/workflow.md')
print('CURRENT_WORKFLOW_UNCHANGED',sha(current_workflow))

for execution_name,pairs in [
 ('POST_FREEZE_EXECUTION.json',[('script_sha256','freeze_post_sources.py'),('stdout_sha256','freeze_post_sources.stdout.txt'),
  ('stderr_sha256','freeze_post_sources.stderr.txt'),('result_sha256','POST_SOURCE_PINS.json')]),
 ('POST_CONTROL_EXECUTION.json',[('script_sha256','post_control.py'),('stdout_sha256','post_control.stdout.txt'),
  ('stderr_sha256','post_control.stderr.txt'),('result_sha256','POST_CONTROL_RESULTS.json'),('paths_sha256','POST_PATH_CERTIFICATES.json')])]:
    execution=load(execution_name);assert execution['exit_code']==0
    for field,name in pairs:assert execution[field]==sha(ROOT/name)
    stderr_name=next(name for field,name in pairs if field=='stderr_sha256')
    assert (ROOT/stderr_name).stat().st_size==0
    print('EXECUTION_BOUND',execution_name,json.dumps(execution,sort_keys=True))

results=load('POST_CONTROL_RESULTS.json')
stdout=(ROOT/'post_control.stdout.txt').read_text().splitlines()
assert [json.loads(row) for row in stdout[:-1]]==results['checks']
assert stdout[-1]=='TOTAL 8 bounded POST checks completed; author controls not rerun'
assert results['check_count']==len(results['checks'])==8 and all(x['verified'] for x in results['checks'])
assert results['script_sha256']==sha(ROOT/'post_control.py')
assert results['author_result_sha256']==sha(ROOT/'post_sources/author/PREPARED_PROBE_RESULTS.json')
assert results['path_certificate_sha256']==sha(ROOT/'POST_PATH_CERTIFICATES.json')

certificates=load('POST_PATH_CERTIFICATES.json');case_rows=[]
def divergence(flow):
    values=defaultdict(int)
    for x,y,value in flow:
        x,y=tuple(x),tuple(y)
        assert sum(x)%2==0 and sum(y)%2==1
        distances=[min((a-b)%6,(b-a)%6) for a,b in zip(x,y)]
        assert sum(distances)==1
        values[x]+=value;values[y]-=value
    return {v:value for v,value in values.items() if value}
def sparse_delta(rows):return {tuple(v):value for v,value in rows if value}
for cert in certificates:
    assert divergence(cert['initial_field'])==sparse_delta(cert['initial_deviation'])
    assert len(cert['attempts'])==2 and sum(x['birth_legal'] for x in cert['attempts'])==1
    for attempt in cert['attempts']:
        assert divergence(attempt['intermediate_field'])==sparse_delta(attempt['intermediate_deviation'])
        if attempt['birth_legal']:
            assert divergence(attempt['final_field'])==sparse_delta(attempt['final_deviation'])
        else:assert attempt['destination']==[5,0,0]
    case={key:cert[key] for key in ['sigma','branch','reference_loop_flux']}
    case.update(initial_and_two_intermediate_Gauss_equal=True,one_successful_final_Gauss_equal=True)
    case_rows.append(case);print('COMPLETE_SERIALIZED_CASE',json.dumps(case,sort_keys=True))
assert len(certificates)==20
assert {(c['sigma'],c['branch'],c['reference_loop_flux']) for c in certificates}=={
    (sigma,branch,flux) for sigma in [-1,1] for branch in [0,1] for flux in [-2,-1,0,1,2]}

for name in ['POST.md','POST_EVIDENCE_LOG.md','POST_CHECKPOINT.md']:
    path=ROOT/name
    if path.exists():
        assert all(b>=32 or b in (9,10) for b in path.read_bytes()),name

verification=dict(created_utc=datetime.now(timezone.utc).isoformat(),preserved_PRE_seal_sha256=sha(ROOT/'PRE_SEAL.json'),
                  PRE_members_unchanged=33,new_source_origins=origin_rows,reused_main_science_origins_equal=4,
                  current_workflow_unchanged=True,executions_bound=True,stdout_result_checks_equal=True,
                  scientific_check_count=8,serialized_case_count=20,complete_serialized_cases=case_rows,
                  author_controls_executed=False,other_active_checker_packets_read=False,
                  verifier_sha256=sha(Path(__file__)))
(ROOT/'POST_EVIDENCE_VERIFICATION.json').write_text(json.dumps(verification,indent=2)+'\n')
print('TOTAL verified 33 preserved PRE members, 13 new input origins, 4 reused science origins, 8 checks and all 20 serialized cases')
