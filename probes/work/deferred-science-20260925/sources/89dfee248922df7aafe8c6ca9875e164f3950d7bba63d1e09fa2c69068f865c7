from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def verify(name,ok,**info):
    assert ok,(name,info)
    row=dict(name=name,verified=True,**info);checks.append(row)
    print(json.dumps(row,sort_keys=True))
pins=json.loads((ROOT/'SOURCE_PINS.json').read_text())
for item in pins['sources']:
    p=ROOT/item['frozen_path']
    verify('frozen_source_'+p.name,p.stat().st_size==item['bytes'] and sha(p)==item['sha256'])
    if 'commit' in item:
        b=subprocess.check_output(['git','show',item['commit']+':'+item['path']],cwd=item['repository'])
        verify('git_origin_'+p.name,hashlib.sha256(b).hexdigest()==item['sha256'],commit=item['commit'],path=item['path'])
    elif 'path' in item:
        verify('prior_origin_'+p.name,sha(Path(item['path']))==item['sha256'])
old=ROOT.parent/'record-photon-readout-independent'
for name in ['PRE_SEAL.json','POST_SEAL.json']:
    seal=json.loads((old/name).read_text())
    for member in seal['members']:
        p=old/member['path']
        assert p.stat().st_size==member['bytes'] and sha(p)==member['sha256'],member['path']
    verify('unchanged_prior_'+name,len(seal['members'])==seal['member_count'],member_count=seal['member_count'],seal_sha256=sha(old/name))
execution=json.loads((ROOT/'EXECUTION.json').read_text())
result=json.loads((ROOT/'CONTROL_RESULTS.json').read_text())
out=(ROOT/'local_background_control.stdout.txt').read_text().splitlines()
verify('complete_stdout_result_correspondence',[json.loads(x) for x in out[:-1]]==result['checks'] and out[-1]==f"TOTAL {result['check_count']} checks completed")
verify('successful_execution',execution['exit_code']==0 and (ROOT/'local_background_control.stderr.txt').stat().st_size==0)
for key,name in [('script_sha256','local_background_control.py'),('stdout_sha256','local_background_control.stdout.txt'),('stderr_sha256','local_background_control.stderr.txt'),('result_sha256','CONTROL_RESULTS.json')]:
    verify('execution_binding_'+key,execution[key]==sha(ROOT/name))
verify('result_script_binding',result['script_sha256']==sha(ROOT/'local_background_control.py'))
verify('declared_command',execution['command'][1]==str(ROOT/'local_background_control.py') and execution['cwd']==str(ROOT))
verify('all_checks_passed',result['check_count']==10 and len(result['checks'])==10 and all(x['passed'] for x in result['checks']))
verify('source_freeze_completed',(ROOT/'freeze_sources.stderr.txt').stat().st_size==0 and (ROOT/'freeze_sources.stdout.txt').read_text().endswith('all expected source hashes and current workflow identity matched; source pin count 11\n'))
current=ROOT.parent/'campaign-working/docs/ai_methodology/SCIENCE_WORKFLOW.md'
verify('workflow_still_unchanged',sha(current)==pins['current_workflow_sha256'])
payload=dict(verification_scope='Exact sources, preserved old packets, own bounded control execution and full output correspondence; no author computation reproduced.',check_count=len(checks),checks=checks)
(ROOT/'EVIDENCE_VERIFICATION.json').write_text(json.dumps(payload,indent=2)+'\n')
print('TOTAL',len(checks),'evidence checks verified')
