"""Build one supplied-static-edge source packet; never execute historical science."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
D=Path(sys.argv[1]).resolve();N=D.parent
P=D/'proposal';PK='.claude/science/physics-loops/toe-commuting-static-edge-fixed-target-20261016'
NOTE='docs/COMMUTING_STATIC_EDGE_FIXED_TARGET_BOUNDED_THEOREM_NOTE_2026-10-16.md'
SCRIPT='scripts/commuting_static_edge_fixed_target_2026_10_16.py'
ROOTS={
 'endpoint_finite_quantum_actuator_candidate':('FREEZE.json','0677ed775ee782608fa5bccdf6e3e24891f1cf2833394196ec240b309a5ad0b2','members'),
 'commuting_target_static_edge_exposed_check':('FREEZE.json','66f573eeada95e368ae1ac464cf2ebdb5f20abd951804e48554662f67b2789ce','files'),
 'commuting_target_static_edge_exposed_check/author_cross_review':('FREEZE.json','25c099e61df3fda1322ed2ed856e0c16773c0f139aebc45887a7560382996a67','members'),
 'commuting_static_edge_check_proposal':('PRELAUNCH_FREEZE.json','68be4520b91aff3614ff436dad0c16bc550170dd6e36e623af85b9325a540b67','members'),
 'commuting_static_edge_root_review':('FREEZE.json','151c7b3c3e3cd9ad88670fb5606f8bde54f1b0d22b32b33ea874d22e966d4b58','members'),
}
EXTRA_DIRS=['endpoint_finite_quantum_actuator_candidate/runs/metadata_001',
 'commuting_target_static_edge_exposed_check/metadata_run',
 'commuting_static_edge_check_proposal/runs/metadata_001',
 'commuting_static_edge_check_proposal/runs/edge_001','runs/static_edge_root_acceptance']
EXTRA_FILES=['commuting_static_edge_check_proposal/ROOT_GO.md',
 'bootstrap/record_commuting_static_edge_acceptance.py','review_run.py']
ACCEPTANCES={'commuting_static_edge_root_review/ACCEPTANCE.json':'f954c36d04380ee49edac71a5dd7cb10e31142d3f3ca03f4da71f5609c04446b'}
BODIES=[
 ('original_author_derivation','endpoint_finite_quantum_actuator_candidate/DERIVATION.md'),
 ('initial_pre_author_analysis','commuting_target_static_edge_exposed_check/ANALYSIS.md'),
 ('complete_exposed_cross_review','commuting_target_static_edge_exposed_check/author_cross_review/REVIEW.md'),
 ('preserved_N1_FAIL_checklist','commuting_target_static_edge_exposed_check/author_cross_review/NO_GO_DISCIPLINE_CHECKLIST.md'),
 ('controlling_root_qualifications','commuting_static_edge_root_review/FINAL_QUALIFICATIONS.md'),
]
sha=lambda b:hashlib.sha256(b).hexdigest()
def put(rel,b):
 p=P/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
def js(rel,x):put(rel,(json.dumps(x,indent=2)+'\n').encode())
def ident(b):return {'bytes':len(b),'sha256':sha(b)}
def read(p):return json.loads(p.read_text())
sources={};objects={};freeze_rows=[]
def add(path,alias=None,role='historical_source'):
 path=path.resolve();path.relative_to(N);b=path.read_bytes();alias=alias or str(path.relative_to(N));h=sha(b)
 r={'source':alias,'original_path':str(path),'role':role,**ident(b),'recovery_path':PK+'/archive/sha256/'+h}
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
  rel=row['path'];path=N/folder/rel;path.resolve().relative_to(N/folder)
  b=path.read_bytes();assert ident(b)=={k:row[k] for k in ['bytes','sha256']},str(path)
  add(path);selected.append(rel)
 freeze_rows.append({'folder':folder,'alias':folder+'/'+filename,'sha256':pin,'members':len(rows),
  'key':key,'complete_members':True,'selected_members':selected,'all_original_members_verified_at_build':True})
for folder in EXTRA_DIRS:
 for p in sorted((N/folder).rglob('*')):
  if p.is_file():add(p,role='actual_terminal_source_receipt_or_full_stream')
for path in EXTRA_FILES:add(N/path,role='actual_original_source_or_go_record')

# Six actual executions, not duplicate aliases from copied inventories.
specs=[
 ('endpoint_finite_quantum_actuator_candidate/runs/metadata_001','legacy_metadata',
  'endpoint_finite_quantum_actuator_candidate/seal_metadata.py','source_at_launch.py',1),
 ('commuting_target_static_edge_exposed_check/metadata_run','initial_metadata',
  'commuting_target_static_edge_exposed_check/freeze_metadata.py','source_at_launch.py',2),
 ('commuting_target_static_edge_exposed_check/author_cross_review/metadata_run','captured_metadata',
  'commuting_target_static_edge_exposed_check/author_cross_review/capture_metadata.py','source_at_launch.py',2),
 ('commuting_static_edge_check_proposal/runs/metadata_001','legacy_metadata',
  'commuting_static_edge_check_proposal/seal_metadata.py','source_at_launch.py',1),
 ('commuting_static_edge_check_proposal/runs/edge_001','scientific_edge',
  'commuting_static_edge_check_proposal/check_static_edge.py','source_at_launch/check_static_edge.py',3),
 ('runs/static_edge_root_acceptance','root_review_run',
  'bootstrap/record_commuting_static_edge_acceptance.py','executed_source.py',1),
]
contracts=[]
for folder,schema,original,snapshot,index in specs:
 alias=folder+'/EXECUTION.json';r=read(N/alias)
 assert alias in sources and r['exit_code']==0
 source=add(N/original,role='original_source_of_actual_execution')
 captured=add(N/folder/snapshot,role='actual_source_at_launch')
 assert source==captured
 executed=folder+'/'+snapshot if schema in {'captured_metadata','scientific_edge'} else original
 assert r['argv'][index]==str(N/executed)
 files=[]
 for p in sorted((N/folder).rglob('*')):
  if p.is_file() and p.name!='EXECUTION.json':
   a=str(p.relative_to(N));b=add(p);files.append({'alias':a,**ident(b)})
 if schema=='root_review_run':
  b=add(N/'review_run.py');files.append({'alias':'review_run.py',**ident(b)})
  assert ident(b)=={k:r['recorder'][k] for k in ['bytes','sha256']}
 start=r['start_utc'];end=r['end_utc'];assert start<end and r['elapsed_seconds']>=0
 contracts.append({'alias':alias,'schema':schema,'record':r,'original_alias':original,
  'snapshot_alias':folder+'/'+snapshot,'executed_alias':executed,'argv_source_index':index,
  'source_sha256':sha(source),'files':files,
  'scope':'single author scientific fixture' if schema=='scientific_edge' else 'metadata only',
  'recorded_cwd':r.get('cwd'),'cwd_missing_in_original_receipt':'cwd' not in r})
for alias,h in ACCEPTANCES.items():assert sha((N/alias).read_bytes())==h
note=(D/'packet_text/WRAPPER.md').read_bytes();wrapper_len=len(note);maps=[]
for name,alias in BODIES:
 raw=(N/alias).read_bytes();assert alias in sources
 note+=('\n\n<!-- Unchanged complete source: '+name+' -->\n\n').encode();start=len(note);note+=raw
 maps.append({'name':name,'source':alias,'container':NOTE,'start_byte_inclusive':start,'end_byte_exclusive':len(note),**ident(raw)})
trailer_start=len(note)
note+=b'\n\nThe controlling wrapper and root qualifications govern scope. Negative material remains N1FAIL partial-attempt; no retained status or new publication approval is conferred.\n'
put(NOTE,note)
js(PK+'/BODY_MAP.json',{'new_wrapper_bytes':[0,wrapper_len],'trailing_wrapper_bytes':[trailer_start,len(note)],'bodies':maps})
js(PK+'/SOURCE_MANIFEST.json',{'schema':'commuting_static_edge_source_archive_v1','sources':list(sources.values()),
 'archive_rule':'Complete selected original freeze inventories and bounded actual execution closure; bytes deduplicated. No prior publication archive traversal.'})
js(PK+'/ARCHIVE_INDEX.json',{'objects':list(objects.values()),'recursive_prior_publication_archives':False})
js(PK+'/FROZEN_SOURCE_CLOSURE.json',{'roots':freeze_rows})
js(PK+'/EXECUTION_CONTRACTS.json',{'receipts':contracts,'new_scientific_executions':0,'unique_historical_scientific_runs':1})
js(PK+'/PARENT_BINDING.json',{'canonical_binding_complete':False,'direct_mathematical_parents':[],
 'explicit_problem_data':['K=2I+ZZ','fixed W','fixed T','w=24','supplied calibrated positive XX edge'],
 'prior_target_theorem_is_context_only':True,'canonical_graph_disposition':None,
 'git_ancestry_is_not_mathematical_dependency':True,'mediator_proposal_composed':False})
state={k:None for k in ['source_wrapper_review','source_publication_binding','canonical_integration','current_base_observation','canonical_review','staged_review','primary_execution','publication_action','retained_audit']}
state.update(scientific_programs_run_this_draft=0,scientific_replays=0,
 actual_scientific_source_acceptance={'source':'commuting_static_edge_root_review/ACCEPTANCE.json','sha256':next(iter(ACCEPTANCES.values()))})
js(PK+'/PUBLICATION_STATE.json',state)
js(PK+'/ACTUAL_BINDING.json',{'kind':'unbound_source_only_proposal','source_review':None,'base_observation':None,'canonical_review':None,'canonical_parent_binding':None,'staged_review':None,'publication':None})
js(PK+'/NO_GO_STATUS.json',{'packet_status':'FAIL','N1':'FAIL','disposition':'partial-attempt-with-named-untested-routes',
 'narrow_invariant_validity_separate':True,'positive_theorem_separate':True,'new_retained_negative_authority':False})
for name in ['PR_BODY.md','BINDING_CONTRACT.md','CLAIM_STATUS_CERTIFICATE.md','EVIDENCE_SCOPE.md']:put(PK+'/'+name,(D/'packet_text'/name).read_bytes())
# Keep the exact checklist linkable as a sidecar as well as an immutable body.
put(PK+'/NO_GO_DISCIPLINE_CHECKLIST.md',(N/BODIES[3][1]).read_bytes())
for name in ['APPROACH_REGISTRY.md','NO_GO_LEDGER.md']:
 put(PK+'/'+name,(N/'commuting_target_static_edge_exposed_check/author_cross_review'/name).read_bytes())
skill_rel='sources/current_main/docs/ai_methodology/skills/no-go-discipline/SKILL.md'
put(PK+'/'+skill_rel,(N/'commuting_target_static_edge_exposed_check/author_cross_review'/skill_rel).read_bytes())
js(PK+'/EXPOSURE.json',{'source_exposed':True,'same_selected_model':True,'blind_independence':False,
 'new_scientific_executions':0,'historical_scientific_replays':0,'historical_author_scientific_runs':1,
 'independent_scientific_replications':0,'actual_author_seconds':0.18528820807114244,
 'wall_limit_seconds':60,'cpu_quota':None,'ram_quota':None,'retained_audit':False})
inputs=[]
for p in sorted(P.rglob('*')):
 if p.is_file():inputs.append({'path':str(p.relative_to(P)),**ident(p.read_bytes())})
js(PK+'/INPUT_MANIFEST.json',{'schema':'commuting_static_edge_publication_inputs_v1','inputs':inputs})
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
