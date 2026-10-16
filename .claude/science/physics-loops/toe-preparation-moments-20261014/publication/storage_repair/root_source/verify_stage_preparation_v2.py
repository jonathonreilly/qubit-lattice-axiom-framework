import gzip,hashlib,json,shutil,sys
from pathlib import Path
from common import N,W,pin,check_pin,read_json,write_json,run,git_read,stage_exact,now,require_campaign_active
D=N/'publication_integration/preparation';R=D/'storage_repair';c=read_json(N/'preparation_moment_publication_components/INPUTS.json');packet=c['packet'];out=W/packet/'publication/storage_repair';prepared=read_json(R/'PREPARED_SOURCE.json')
require_campaign_active();assert git_read('rev-parse','HEAD').decode().strip()==prepared['base_head']
for name,row in prepared['installed_pins'].items():check_pin(W/name,row)
def copy(source,target):
 target.parent.mkdir(parents=True,exist_ok=True);assert not target.exists();shutil.copyfile(source,target)
for name in ['PREPARED_SOURCE.json','INTEGRITY_CONTROLS.json','CANONICAL_RESULT.json','CANONICAL_EXECUTION.json']:
 copy(R/name,out/'final_records'/name)
for label in ['preparation_storage_repair','preparation_integrity_controls_v2','preparation_canonical_cache_v2']:
 for p in (N/'runs'/label).rglob('*'):
  if p.is_file():copy(p,out/'executions'/label/p.relative_to(N/'runs'/label))
for p in (R/'integrity_runs').rglob('*'):
 if p.is_file():copy(p,out/'integrity_runs'/p.relative_to(R/'integrity_runs'))
for name in ['check_preparation_mutations_v2.py','execute_preparation_cache_v2.py','verify_stage_preparation_v2.py']:
 copy(N/'publication_integration'/name,out/'root_source'/name)
base={name:pin(W/name) for name in prepared['installed_paths']+[c['parent']['repo_path']]};cases=[]
for case in read_json(R/'INTEGRITY_CONTROLS.json')['results']:
 root=R/'integrity_fixtures'/case['case'];changed=[]
 for name in base:
  actual=pin(root/name)
  if actual['sha256']==base[name]['sha256']:continue
  target=out/'mutation_objects'/(actual['sha256']+'.gz')
  if not target.exists():target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(gzip.compress((root/name).read_bytes(),mtime=0))
  changed.append({'path':name,'before':base[name],'after':actual,'stored':pin(target),'codec':'gzip'})
 cases.append({'case':case['case'],'expected_reason':case['expected_reason'],'changed_files':changed})
write_json(out/'FINAL_MUTATION_RECONSTRUCTION.json',{'base':base,'cases':cases,'scope':'Nine integrity controls; no mathematical checks.'})
# Check all original generation members and the complete old executed input tree after relocation.
for filename in ['publication/SOURCE_COMPONENT_RECONSTRUCTION.json','publication/storage_repair/PRE_REPAIR_CANONICAL_MAP.json']:
 for row in read_json(W/packet/filename)['files']:
  raw=(W/row['repository_path']).read_bytes();raw=gzip.decompress(raw) if row.get('codec')=='gzip' else raw
  expected=row.get('source',row);assert len(raw)==expected['bytes'] and hashlib.sha256(raw).hexdigest()==expected['sha256']
for name in ['HANDOFF.md','REVIEW_HISTORY.md']:
 p=W/packet/name;text=p.read_text().replace('eight scratch corruption controls','nine final scratch corruption controls').replace('Eight scratch integrity mutations','Nine final scratch integrity mutations').replace('all eight cases','all nine final cases')
 text+='\nStorage repair: the first staged whitespace check rejected archived patch context and deliberate fragment blank EOF. Exact originals and the failed output are preserved under publication/storage_repair. Explicit .gz representations and a checked decompression/fragment-identity step preserve the unchanged canonical note and all raw proofs. Nine final controls, including corrupt decoded framing, rejected the intended mutations; the fresh canonical envelope succeeded with zero mathematical predicates. Prior executions remain historical evidence.\n'
 p.write_text(text)
paths=sorted(set(prepared['installed_paths'])|{str(p.relative_to(W)) for p in (W/packet/'publication').rglob('*') if p.is_file() and '__pycache__' not in p.parts}|{packet+'/'+x for x in ['HANDOFF.md','TRACE_GATE.md','REVIEW_HISTORY.md']}|{'docs/audit/data/citation_graph_manifest.json','logs/runner-cache/'+Path(c['helper']).stem+'.txt'})
before={name:pin(W/name) for name in paths}
for flag,label in [('--fix','vocabulary_fix'),('--report-only','vocabulary_report')]:run(R,label,['python3','scripts/vocab_lint.py',flag,*paths])
for name,expected in before.items():check_pin(W/name,expected)
python_files=[name for name in paths if name.endswith('.py')];run(R,'python_compile',['python3','-m','py_compile',*python_files])
sys.path.insert(0,str(W/'scripts'));import runner_cache
assert runner_cache.cache_status(c['helper'])=='fresh'
# Note and all graph extractor inputs remain unchanged by the storage-only repair.
graph=read_json(D/'after_graph.json');assert graph['nodes'][c['claim_id']]['note_hash']==pin(W/c['note'])['sha256'];check_pin(W/'docs/audit/data/citation_graph_manifest.json',read_json(D/'GRAPH_VERIFICATION.json')['manifest'])
stage_exact(paths)
status=git_read('status','--porcelain','-z','--untracked-files=all');assert {row[3:].decode() for row in status.split(b'\0') if row}==set(paths)
compat=json.loads(run(R,'focused_compatibility',['python3','docs/audit/scripts/check_changed_audit_evidence.py','--base','HEAD','--include-worktree','--json']))
assert compat['failures']==[] and compat['control_failures']==[] and compat['changed_path_count']==len(paths)
summary={'utc':now().isoformat(),'base':prepared['base_head'],'paths':len(paths),'python_files':len(python_files),'vocabulary_fix_and_report_exit':0,'vocabulary_source_drift':False,'python_compile_exit':0,'canonical_cache_status':'fresh','integrity_cases_rejected':9,'graph_delta':{'nodes':1,'edges':1,'old_complete_nodes_preserved':7114,'old_complete_edges_preserved':16053},'focused_existing_ledger_compatibility':compat,'mathematical_predicates_executed':0,'combined_current_main_validation':'pending separate landing review','independent_retained_audit':'not performed','editable_prompts_changed':[]}
review=W/packet/'REVIEW_HISTORY.md'
with review.open('a') as stream:stream.write('\nActual final focused repository check snapshot:\n\n```json\n'+json.dumps(summary,indent=2)+'\n```\n\nAn empty checked list means no existing scientific claim was audited. This final result append changes only the existing review record; scientific source and canonical inputs remain unchanged.\n')
run(R,'vocabulary_final_review',['python3','scripts/vocab_lint.py','--fix',packet+'/REVIEW_HISTORY.md']);run(R,'vocabulary_final_review_report',['python3','scripts/vocab_lint.py','--report-only',packet+'/REVIEW_HISTORY.md'])
for name,expected in before.items():
 if name!=packet+'/REVIEW_HISTORY.md':check_pin(W/name,expected)
staged=stage_exact(paths)
for name,expected in staged.items():assert hashlib.sha256(git_read('show',':'+name)).hexdigest()==expected['sha256']
assert runner_cache.cache_status(c['helper'])=='fresh'
write_json(R/'STAGED_VERIFICATION.json',dict(summary,staged_pins=staged,review_record=pin(review)));print(summary)
