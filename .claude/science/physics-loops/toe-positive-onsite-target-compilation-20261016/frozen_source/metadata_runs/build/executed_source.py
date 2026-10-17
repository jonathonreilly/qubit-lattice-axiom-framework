"""Build one source-only fixed-target packet; never execute historical science."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
D=Path(sys.argv[1]).resolve();N=D.parent
P=D/'proposal';PK='.claude/science/physics-loops/toe-positive-onsite-target-compilation-20261016'
NOTE='docs/POSITIVE_ONSITE_TARGET_COMPILATION_BOUNDED_THEOREM_NOTE_2026-10-16.md'
SCRIPT='scripts/positive_onsite_target_compilation_2026_10_16.py'
ROOTS={
 'endpoint_target_compilation_candidate':('FREEZE.json','0f61e1040c491541eb24e4f94396d805c1b6a251202485c276570af1491d31fc','members'),
 'endpoint_target_compilation_exposed_check':('FINAL_FREEZE.json','857c60addbcd5882635a5b2178ec6014b65e40e364f35a01e62d1e04499d1722','files'),
 'endpoint_target_compilation_root_review':('FREEZE.json','2a1abb6395600909f76649cfe68ed1010012ef2d1273a6018cbd92aa9c1c391c','members'),
}
ROOT_RUNS=['endpoint_target_acceptance','endpoint_target_acceptance_correct_schema']
ACCEPTANCES={'endpoint_target_compilation_root_review/ACCEPTANCE.json':'949d009ac768e72401c005b5cc7b0161ec93bbfdefdf004dc4b8300e0f140514'}
PARENT_NOTE='docs/POSITIVE_ONSITE_ENDPOINT_CHART_RECURRENCE_BOUNDED_THEOREM_NOTE_2026-10-16.md'
PARENT_SHA='ab8fd20fb48aae14c9ae22df2b38de97755d717131195d0d4ad25f7236d475a8'
BODIES=[
 ('original_target_derivation','endpoint_target_compilation_candidate/DERIVATION.md'),
 ('pre_program_analytic_review','endpoint_target_compilation_exposed_check/REVIEW.md'),
 ('complete_prelaunch_source_review','endpoint_target_compilation_exposed_check/program_exposed/REVIEW.md'),
 ('completed_saved_arithmetic_review','endpoint_target_compilation_exposed_check/ARITHMETIC_REVIEW.md'),
 ('saved_arithmetic_coverage','endpoint_target_compilation_exposed_check/ARITHMETIC_SOURCE_COVERAGE.md'),
 ('controlling_root_qualifications','endpoint_target_compilation_root_review/FINAL_QUALIFICATIONS.md'),
]
sha=lambda b:hashlib.sha256(b).hexdigest()
def put(rel,b):
 p=P/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
def js(rel,x):put(rel,(json.dumps(x,indent=2)+'\n').encode())
def ident(b):return {'bytes':len(b),'sha256':sha(b)}
def read(p):return json.loads(p.read_text())
sources={};objects={};freeze_rows=[]
def add(path,alias=None,role='historical_source',captured_bytes=None,recovered_from=None):
 path=path.resolve();b=path.read_bytes() if captured_bytes is None else captured_bytes;alias=alias or str(path.relative_to(N));h=sha(b)
 r={'source':alias,'original_path':str(path),'role':role,**ident(b),'recovery_path':PK+'/archive/sha256/'+h}
 if recovered_from is not None:r['historical_version_recovered_from']=str(recovered_from)
 if alias in sources:assert sources[alias]['sha256']==h
 else:sources[alias]=r
 objects[h]={'path':r['recovery_path'],**ident(b)}
 if not (P/r['recovery_path']).exists():put(r['recovery_path'],b)
 return b
assert not P.exists(),'Refuse overwrite of an existing proposal'
for folder,(filename,pin,key) in ROOTS.items():
 f=N/folder/filename;raw=add(f,role='source_freeze');assert sha(raw)==pin
 rows=read(f)[key];selected=[]
 assert len({r['path'] for r in rows})==len(rows)
 for row in rows:
  rel=row['path'];path=N/folder/rel;path.resolve().relative_to(N)
  b=path.read_bytes();assert ident(b)=={'bytes':row['bytes'],'sha256':row['sha256']},str(path)
  add(path);selected.append(rel)
 for terminal in ['runs/final_freeze','closure_metadata_run']:
  for p in sorted((N/folder/terminal).glob('*')):
   if p.is_file():add(p,role='original_terminal_freeze_evidence')
 freeze_rows.append({'folder':folder,'alias':folder+'/'+filename,'sha256':pin,'members':len(rows),
  'key':key,'complete_members':True,'selected_members':selected,'all_original_members_verified_at_build':True})
for name in ROOT_RUNS:
 for p in sorted((N/'runs'/name).iterdir()):
  if p.is_file():add(p,role='actual_root_metadata_or_heuristic_evidence')

# Preserve literal launch paths and separately captured versions; no source is executed.
contracts=[];processed=set()
while True:
 pending=[alias for alias in sources if alias.endswith('/EXECUTION.json') and alias not in processed]
 if not pending:break
 for alias in pending:
  processed.add(alias);r=read(Path(sources[alias]['original_path']))
  if 'child_source_at_launch' in r:
   original,capture,recorder='child_source_at_launch','source_capture','recorder'
  else:
   original='original_source' if 'original_source' in r else 'source_original'
   capture='source_at_launch';recorder='recorder_at_launch' if 'recorder_at_launch' in r else 'launcher_at_launch'
  source_raw=Path(r[capture]['path']).read_bytes();assert ident(source_raw)=={k:r[original][k] for k in ['bytes','sha256']}
  original_path=Path(r[original]['path']);original_alias=str(original_path.relative_to(N))
  if original_path.read_bytes()!=source_raw:
   original_alias='historical_at_launch/'+r[original]['sha256']+'/'+original_alias
   add(original_path,alias=original_alias,role='preserved_superseded_original_source',captured_bytes=source_raw,recovered_from=r[capture]['path'])
  else:add(original_path,role='actual_original_launch_source')
  for field in [capture,recorder,'stdout','stderr','checker_source_freeze','original_input_binding','input_binding_at_launch']:
   if field not in r:continue
   raw=add(Path(r[field]['path']),role='actual_capture_binding_or_full_stream')
   assert ident(raw)=={k:r[field][k] for k in ['bytes','sha256']}
  index=2 if r['argv'][1]=='-B' else 1
  executed=original if r['argv'][index]==r[original]['path'] else capture
  assert r['argv'][index]==r[executed]['path'] and r[original]['path']!=r[capture]['path']
  fields=[original,capture,recorder,'stdout','stderr']
  aliases={field:(original_alias if field==original else str(Path(r[field]['path']).relative_to(N))) for field in fields}
  for field in ['checker_source_freeze','original_input_binding','input_binding_at_launch']:
   if field in r:fields.append(field);aliases[field]=str(Path(r[field]['path']).relative_to(N))
  temporal={k:r[k] for k in ['start_utc','end_utc','started_utc','finished_utc','elapsed_seconds','timed_out','wall_timeout_seconds','timeout_seconds','cpu_ram_limits','source_unchanged','source_unchanged_during_run'] if k in r}
  contract={'alias':alias,'original_key':original,'capture_key':capture,'recorder_key':recorder,
   'executed_key':executed,'executed_argv_index':index,'argv':r['argv'],'cwd':r['cwd'],
   'exit_code':r['exit_code'],'temporal_and_limits':temporal,'source_sha256':r[original]['sha256'],
   'field_aliases':aliases,'field_pins':{field:r[field] for field in fields},
   'execution_scope':'Original path launched with separate preserved snapshot' if executed==original else 'Captured copy actually launched'}
  contracts.append(contract)
parent_raw=add(N.parent/'correlation_worktree'/PARENT_NOTE,alias='canonical_parent/'+PARENT_NOTE,role='sole_direct_mathematical_parent_exact_source')
assert sha(parent_raw)==PARENT_SHA
for alias,h in ACCEPTANCES.items():assert sha((N/alias).read_bytes())==h
note=(D/'packet_text/WRAPPER.md').read_bytes();wrapper_len=len(note);maps=[]
for name,alias in BODIES:
 raw=(N/alias).read_bytes();assert alias in sources
 note+=('\n\n<!-- Unchanged complete source: '+name+' -->\n\n').encode();start=len(note);note+=raw
 maps.append({'name':name,'source':alias,'container':NOTE,'start_byte_inclusive':start,'end_byte_exclusive':len(note),**ident(raw)})
trailer_start=len(note)
note+=b'\n\nPublication scope remains conditional support under the premises and verification limits above; retained status requires the independent audit path.\n'
put(NOTE,note)
js(PK+'/BODY_MAP.json',{'new_wrapper_bytes':[0,wrapper_len],'trailing_wrapper_bytes':[trailer_start,len(note)],'bodies':maps})
js(PK+'/SOURCE_MANIFEST.json',{'schema':'endpoint_target_compilation_source_archive_v1','sources':list(sources.values()),
 'archive_rule':'Complete candidate132/checker256/root inventories, terminal metadata and exact execution version aliases; shared bytes deduplicated once, no prior publication archive traversal.'})
js(PK+'/ARCHIVE_INDEX.json',{'objects':list(objects.values()),'recursive_prior_publication_archives':False})
js(PK+'/FROZEN_SOURCE_CLOSURE.json',{'roots':freeze_rows})
js(PK+'/EXECUTION_CONTRACTS.json',{'receipts':contracts,'new_scientific_executions':0})
js(PK+'/PARENT_BINDING.json',{'canonical_binding_complete':False,'direct_mathematical_parents':[
 {'path':PARENT_NOTE,'source_alias':'canonical_parent/'+PARENT_NOTE,**ident(parent_raw)}],
 'intended_graph_delta':{'new_roots':0,'direct_edges':1},'git_ancestry_is_not_mathematical_dependency':True})
state={k:None for k in ['source_wrapper_review','source_publication_binding','canonical_integration','current_base_observation','canonical_review','primary_execution','publication_action','retained_audit']}
state.update(scientific_programs_run_this_draft=0,scientific_replays=0)
js(PK+'/PUBLICATION_STATE.json',state)
js(PK+'/ACTUAL_BINDING.json',{'kind':'unbound_source_only_proposal','source_review':None,'base_observation':None,'canonical_review':None,'canonical_parent_binding':None,'publication':None})
for name in ['PR_BODY.md','BINDING_CONTRACT.md','CLAIM_STATUS_CERTIFICATE.md','EVIDENCE_SCOPE.md']:put(PK+'/'+name,(D/'packet_text'/name).read_bytes())
js(PK+'/EXPOSURE.json',{'source_exposed':True,'same_selected_model':True,'blind_independence':False,
 'second_ODE_implementation':False,'new_scientific_executions':0,'historical_scientific_replays':0,
 'historical_author_target_commands':1,'historical_separate_saved_evidence_checks':1,
 'author_elapsed_seconds':461.2228046669625,'checker_elapsed_seconds':10.38794649997726,
 'checker_recomputed_local_ODE_slots':False,'new_scientific_attempts':0,'retained_audit':False})
inputs=[]
for p in sorted(P.rglob('*')):
 if p.is_file():inputs.append({'path':str(p.relative_to(P)),**ident(p.read_bytes())})
js(PK+'/INPUT_MANIFEST.json',{'schema':'endpoint_target_compilation_publication_inputs_v1','inputs':inputs})
msha=sha((P/PK/'INPUT_MANIFEST.json').read_bytes())
replacements={'__MANIFEST_SHA256__':msha,'__AUDIT_INPUT_PATHS__':repr([r['path'] for r in inputs]+[PK+'/INPUT_MANIFEST.json']),
 '__EXPECTED_BODIES__':repr({r['name']:r['sha256'] for r in maps}),
 '__EXPECTED_FREEZES__':repr({r['alias']:r['sha256'] for r in freeze_rows}),
 '__EXPECTED_ACCEPTANCES__':repr(ACCEPTANCES)}
generated=(D/'primary_template.py').read_text()
for key,value in replacements.items():generated=generated.replace(key,value)
put(SCRIPT,generated.encode())
result={'utc':datetime.now(timezone.utc).isoformat(),'note':NOTE,'note_sha256':sha(note),'primary_sha256':sha(generated.encode()),
 'unchanged_bodies':len(maps),'source_aliases':len(sources),'unique_archive_objects':len(objects),
 'source_receipts':len(contracts),'input_manifest_sha256':msha,'science_executions':0,'canonical_execution':None}
(D/'BUILD_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
