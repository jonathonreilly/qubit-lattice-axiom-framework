import gzip,hashlib,json,shutil
from pathlib import Path
from common import N,W,pin,check_pin,read_json,write_json,now,require_campaign_active
D=N/'publication_integration/preparation';P=N/'preparation_moment_publication_components';c=read_json(P/'INPUTS.json');packet=W/c['packet'];out=packet/'publication';assert not out.exists();require_campaign_active()
prepared=read_json(D/'PREPARED_SOURCE.json')
for name,expected in prepared['installed_pins'].items():check_pin(W/name,expected)
def copy(source,target):
 source=Path(source);target=Path(target);assert not target.exists();target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
 return {'source':pin(source),'repository_path':str(target.relative_to(W))}
rows=[]
f=read_json(P/'FINAL_FREEZE.json')
for item in f['members']+[dict(pin(P/'FINAL_FREEZE.json'),path='FINAL_FREEZE.json')]:
 source=P/item['path'];check_pin(source,item)
 if item['path'].startswith('payload/'):
  relative=item['path'][8:];target=W/relative
  if target.read_bytes()!=source.read_bytes():target=out/'generation/original_payload'/relative
  else:
   rows.append({'source':pin(source),'repository_path':relative});continue
 else:target=out/'generation'/item['path']
 rows.append(copy(source,target))
write_json(out/'SOURCE_COMPONENT_RECONSTRUCTION.json',{'scope':'Exact all-member reconstruction of frozen components; payload entries reuse unchanged current repository bytes or preserve original changed metadata/helper. No raw proof copies added.','freeze':pin(P/'FINAL_FREEZE.json'),'files':rows})
for source in sorted((N/'preparation_wrapper_check').rglob('*')):
 if source.is_file():copy(source,out/'wrapper_check'/source.relative_to(N/'preparation_wrapper_check'))
for name in ['common.py','accept_preparation_components.py','prepare_preparation.py','check_preparation_mutations.py','run_identity_fixture.py','execute_preparation_cache.py','check_preparation_graph.py','package_preparation_review.py']:
 copy(N/'publication_integration'/name,out/'root_source'/name)
copy(N/'run.py',out/'root_source/campaign_recorder.py')
for name in ['COMPONENT_ROOT_ACCEPTANCE.json','PREPARE_DRIVER_REVIEW.json','PREPARED_SOURCE.json','INTEGRITY_CONTROLS.json','CANONICAL_RESULT.json','CANONICAL_EXECUTION.json','BASE_GRAPH_BINDING.json','GRAPH_VERIFICATION.json','BASE_GRAPH_BINDING_FAILED_SCHEMA.json']:
 copy(D/name,out/'root_records'/name)
for name in ['preparation_components_source_check','preparation_component_root_acceptance','preparation_fresh_fetch','preparation_install_bound_source','preparation_integrity_controls','preparation_canonical_cache','preparation_graph_before','preparation_graph_after','preparation_graph_verification']:
 for p in (N/'runs'/name).rglob('*'):
  if p.is_file():copy(p,out/'executions'/name/p.relative_to(N/'runs'/name))
for group in ['actual_parent_pr','prepare_origin_main','prepare_origin_ai_execution','integrity_runs','write_graph_manifest']:
 for p in (D/group).rglob('*'):
  if p.is_file():copy(p,out/'executions'/group/p.relative_to(D/group))
mutations=[];parent=c['parent']['repo_path'];base={name:pin(W/name) for name in prepared['installed_paths']+[parent]}
for case in read_json(D/'INTEGRITY_CONTROLS.json')['results']:
 root=D/'integrity_fixtures'/case['case'];changes=[]
 for name in base:
  actual=pin(root/name)
  if actual['sha256']==base[name]['sha256']:continue
  key=actual['sha256'];target=out/'integrity_mutations/objects'/(key+'.gz')
  if not target.exists():target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(gzip.compress((root/name).read_bytes(),mtime=0))
  changes.append({'path':name,'before':base[name],'after':actual,'stored':pin(target),'codec':'gzip'})
 mutations.append({'case':case['case'],'expected_reason':case['expected_reason'],'changed_files':changes})
write_json(out/'integrity_mutations/RECONSTRUCTION.json',{'scope':'Each complete scratch case is the pinned canonical input tree plus these exact replaced bytes. Only integrity failures are tested.','base_files':base,'cases':mutations})
for row in rows:check_pin(W/row['repository_path'],row['source'])
for name,expected in prepared['installed_pins'].items():check_pin(W/name,expected)
write_json(D/'PUBLICATION_EVIDENCE_PACKAGE.json',{'utc':now().isoformat(),'component_reconstruction_members':len(rows),'files':{str(p.relative_to(W)):pin(p) for p in out.rglob('*') if p.is_file()},'current_proof_bytes_changed':False})
print({'publication_files':sum(p.is_file() for p in out.rglob('*')),'frozen_source_members':len(rows),'record':pin(D/'PUBLICATION_EVIDENCE_PACKAGE.json')})
