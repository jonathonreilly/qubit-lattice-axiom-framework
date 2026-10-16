"""Build one self-contained weak-mediator source packet; never replay science."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
D=Path(sys.argv[1]).resolve();N=D.parent
P=D/'proposal';PK='.claude/science/physics-loops/toe-weak-mediator-fixed-target-20261016'
NOTE='docs/WEAK_MEDIATOR_FIXED_TARGET_BOUNDED_THEOREM_NOTE_2026-10-16.md'
SCRIPT='scripts/weak_mediator_fixed_target_2026_10_16.py'
ROOTS={
 'weak_mediator_candidate':('SOURCE_FREEZE.json','551fab5e4c1876dfff3d807ebf837a8c23f3d28724a554049faa8b6ab92d3f9c','files'),
 'weak_mediator_exposed_check':('FINAL_FREEZE.json','ef8dce286398c515be38142b54917e2b82d8ea3363709f78f37e70f11a71511c','files'),
 'weak_mediator_finite_compiler_exposed_check':('FINAL_FREEZE.json','ecf8e0b72ed47c9c112df9d343edb14229c45406c8103201542f30c12fac60f4','files'),
 'weak_mediator_window_reuse_exposed_check':('FINAL_FREEZE.json','0f0edb6a806a238ef2dfaf01f52ca97b2bae1eb73f8871eed05d9ac5a05fe6d7','files'),
 'weak_mediator_structured_coefficients_exposed_check':('FINAL_FREEZE.json','724d308b4222f082dff7d6d4044f1806541d0741e3f57917e6d583e886217a79','files'),
 'weak_mediator_check_proposal':('OUTPUT_FREEZE.json','d26a5fb145c8d772bb037f770b71fd8fc3ac5b85c7c24d75bc26ae40c16ec929','members'),
 'weak_mediator_finite_compiler_proposal':('OUTPUT_FREEZE.json','96b363b56e2b42b11352b8204492c98f0da36be5b98ccb190d476da802054e57','members'),
 'weak_mediator_root_review':('FREEZE.json','44dc1eff1e1107f2253d32cf64cdfb6fcff7307e74ec75debde1d671accac12b','files'),
 'weak_mediator_saved_certificate_check_proposal':('FINAL_FREEZE.json','c7a2385348e6e73f604cac4c91aceab03c2c704462bc5ed1d078f7646e1309e9','files'),
}
EXTRA_DIRS=['runs/weak_mediator_root_acceptance','weak_mediator_saved_certificate_check_execution/runs/check_001']
EXTRA_FILES=['bootstrap/record_weak_mediator_acceptance.py','review_run.py','weak_mediator_saved_certificate_check_GO.json',
 'weak_mediator_candidate/DYADIC_ADDENDUM.md','weak_mediator_candidate/SCALING_ADDENDUM.md',
 'weak_mediator_candidate/FINITE_COMPILER_ADDENDUM.md','weak_mediator_candidate/WINDOW_REUSE_ADDENDUM.md',
 'weak_mediator_candidate/STRUCTURED_COEFFICIENT_ADDENDUM.md']
ACCEPTANCES={'weak_mediator_root_review/ACCEPTANCE.json':'ba201403a60d1c94751d1550f14d59622c86920ced74ebae21f5f51f5752731b'}
BODIES=[
 ('original_proposal','weak_mediator_candidate/PROPOSAL.md'),
 ('dyadic_addendum','weak_mediator_candidate/DYADIC_ADDENDUM.md'),
 ('scaling_addendum','weak_mediator_candidate/SCALING_ADDENDUM.md'),
 ('finite_compiler_addendum','weak_mediator_candidate/FINITE_COMPILER_ADDENDUM.md'),
 ('window_reuse_addendum','weak_mediator_candidate/WINDOW_REUSE_ADDENDUM.md'),
 ('structured_coefficient_addendum','weak_mediator_candidate/STRUCTURED_COEFFICIENT_ADDENDUM.md'),
 ('original_analytic_review','weak_mediator_exposed_check/REVIEW.md'),
 ('dyadic_scaling_analytic_review','weak_mediator_exposed_check/ADDENDUM_REVIEW.md'),
 ('finite_compiler_analytic_review','weak_mediator_finite_compiler_exposed_check/REVIEW.md'),
 ('window_reuse_analytic_review','weak_mediator_window_reuse_exposed_check/REVIEW.md'),
 ('structured_analytic_review','weak_mediator_structured_coefficients_exposed_check/REVIEW.md'),
 ('controlling_root_qualification','weak_mediator_root_review/QUALIFICATION.md'),
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
 rows=read(f)[key];selected=[];member_aliases={}
 assert len({r['path'] for r in rows})==len(rows)
 for row in rows:
  original=row['path'];path=(N/folder/original).resolve();path.relative_to(N/folder)
  b=path.read_bytes();assert ident(b)=={k:row[k] for k in ['bytes','sha256']},str(path)
  alias=str(path.relative_to(N));add(path);selected.append(original);member_aliases[original]=alias
 freeze_rows.append({'folder':folder,'alias':folder+'/'+filename,'sha256':pin,'members':len(rows),
  'key':key,'complete_members':True,'selected_members':selected,'member_aliases':member_aliases,'all_original_members_verified_at_build':True})
for folder in EXTRA_DIRS:
 for p in sorted((N/folder).rglob('*')):
  if p.is_file():add(p,role='actual_terminal_source_receipt_or_full_stream')
for path in EXTRA_FILES:add(N/path,role='actual_original_source_or_go_record')

# Ten distinct original executions: two author science, seven source metadata, one root record.
specs=[
 ('weak_mediator_exposed_check/runs/original_inspection','analytic_metadata','weak_mediator_exposed_check/inspect_original.py','executed_source.py',1),
 ('weak_mediator_exposed_check/runs/addendum_inspection','analytic_metadata','weak_mediator_exposed_check/inspect_addendum.py','executed_source.py',1),
 ('weak_mediator_finite_compiler_exposed_check/runs/metadata_inspection','analytic_metadata','weak_mediator_finite_compiler_exposed_check/inspect_sources.py','executed_source.py',1),
 ('weak_mediator_window_reuse_exposed_check/runs/metadata_inspection','analytic_metadata','weak_mediator_window_reuse_exposed_check/inspect_sources.py','executed_source.py',1),
 ('weak_mediator_structured_coefficients_exposed_check/runs/metadata_inspection','analytic_metadata','weak_mediator_structured_coefficients_exposed_check/inspect_sources.py','executed_source.py',1),
 ('weak_mediator_check_proposal/runs/metadata_001','legacy_metadata','weak_mediator_check_proposal/seal_metadata.py','source_at_launch.py',3),
 ('weak_mediator_finite_compiler_proposal/runs/metadata_001','legacy_metadata','weak_mediator_finite_compiler_proposal/seal_metadata.py','source_at_launch.py',3),
 ('weak_mediator_check_proposal/runs/weak_001','scientific_symbolic','weak_mediator_check_proposal/check_weak_mediator.py','source_at_launch/check_weak_mediator.py',3),
 ('weak_mediator_finite_compiler_proposal/runs/compiler_001','scientific_compiler','weak_mediator_finite_compiler_proposal/compile_coefficients.py','source_at_launch/compile_coefficients.py',3),
 ('runs/weak_mediator_root_acceptance','root_review_run','bootstrap/record_weak_mediator_acceptance.py','executed_source.py',1),
]
contracts=[]
for folder,schema,original,snapshot,index in specs:
 alias=folder+'/EXECUTION.json';r=read(N/alias)
 assert alias in sources and r['exit_code']==0
 source=add(N/original,role='original_source_of_actual_execution')
 captured=add(N/folder/snapshot,role='actual_source_at_launch');assert source==captured
 executed=folder+'/'+snapshot if schema.startswith('scientific_') else original
 assert r['argv'][index]==str(N/executed),(folder,r['argv'])
 files=[]
 for p in sorted((N/folder).rglob('*')):
  if p.is_file() and p.name!='EXECUTION.json':
   a=str(p.relative_to(N));b=add(p);files.append({'alias':a,**ident(b)})
 if schema=='root_review_run':
  b=add(N/'review_run.py');files.append({'alias':'review_run.py',**ident(b)})
  assert ident(b)=={k:r['recorder'][k] for k in ['bytes','sha256']}
 start=r.get('start_utc',r.get('started_at'));end=r.get('end_utc',r.get('completed_at'))
 assert start<end and r['elapsed_seconds']>=0
 contracts.append({'alias':alias,'schema':schema,'record':r,'original_alias':original,
  'snapshot_alias':folder+'/'+snapshot,'executed_alias':executed,'argv_source_index':index,
  'source_sha256':sha(source),'files':files,
  'scope':'single author scientific execution' if schema.startswith('scientific_') else 'metadata only',
  'recorded_cwd':r.get('cwd'),'cwd_missing_in_original_receipt':'cwd' not in r})
for alias,h in ACCEPTANCES.items():assert sha((N/alias).read_bytes())==h
note=(D/'packet_text/WRAPPER.md').read_bytes();wrapper_len=len(note);maps=[]
for name,alias in BODIES:
 raw=(N/alias).read_bytes();assert alias in sources
 note+=('\n\n<!-- Unchanged complete source: '+name+' -->\n\n').encode();start=len(note);note+=raw
 maps.append({'name':name,'source':alias,'container':NOTE,'start_byte_inclusive':start,'end_byte_exclusive':len(note),**ident(raw)})
trailer_start=len(note)
note+=b'\n\nThe new wrapper and final root qualification control the historical status and scope. Source integrity is not proof, native supply, canonical binding or retained status.\n'
put(NOTE,note)
js(PK+'/BODY_MAP.json',{'new_wrapper_bytes':[0,wrapper_len],'trailing_wrapper_bytes':[trailer_start,len(note)],'bodies':maps})
js(PK+'/SOURCE_MANIFEST.json',{'schema':'weak_mediator_source_archive_v1','sources':list(sources.values()),
 'archive_rule':'Complete selected original freeze inventories and bounded actual execution closure; bytes deduplicated. No prior publication archive traversal.'})
js(PK+'/ARCHIVE_INDEX.json',{'objects':list(objects.values()),'recursive_prior_publication_archives':False})
js(PK+'/FROZEN_SOURCE_CLOSURE.json',{'roots':freeze_rows})
js(PK+'/EXECUTION_CONTRACTS.json',{'receipts':contracts,'new_scientific_executions':0,'unique_historical_author_scientific_runs':2})
additional=[]
for folder,expected_exit,purpose in [
 ('weak_mediator_saved_certificate_check_proposal/runs/metadata_001',1,'preserved metadata artifact-path schema failure'),
 ('weak_mediator_saved_certificate_check_proposal/runs/metadata_002',0,'corrected metadata inspection, no science'),
 ('weak_mediator_saved_certificate_check_execution/runs/check_001',0,'separate saved-certificate arithmetic, no compiler or series replay')]:
 alias=folder+'/EXECUTION.json';record=read(N/alias);assert record['exit_code']==expected_exit
 additional.append({'alias':alias,'record':record,'expected_exit_code':expected_exit,'purpose':purpose,
  'files':[{'alias':str(p.relative_to(N)),**ident(add(p))} for p in sorted((N/folder).rglob('*')) if p.is_file() and p.name!='EXECUTION.json']})
js(PK+'/ADDITIONAL_EVIDENCE.json',{'records':additional,'root_acceptance_predates_this_arithmetic_check':True,
 'saved_certificate_scientific_executions':1,'author_programs_replayed':0,'independence':'source-exposed report-derived implementation; same model/shared Python integers; saved endpoint truth remains conditional',
 'checker_receipt_sha256':'73c9f6544f7530f3e8106b6f4f1dc523098e2bf107312bae88644bf8a88358a0',
 'checker_result_sha256':'ea2b9b99c64e6e3eecadde5a9eec34a50a589afb26a0ce40f1e378d0dab3fdb5'})
js(PK+'/PARENT_BINDING.json',{'canonical_binding_complete':False,'direct_mathematical_parents':[],
 'explicit_problem_data':['K=2I+ZZ','W=((9+12i)I+(-16+12i)XX)/25','specified T or T_m=2^(2m+32)',
 'supplied Bell source and four positive XX/YY ports on a square'],
 'self_contained_conditional_root_theorem':True,'canonical_graph_disposition':None,
 'git_ancestry_is_not_mathematical_dependency':True,'other_campaign_theorems_composed':False})
state={k:None for k in ['source_wrapper_review','source_publication_binding','canonical_integration','current_base_observation','canonical_review','staged_review','primary_execution','publication_action','retained_audit']}
state.update(scientific_programs_run_this_draft=0,scientific_replays=0,
 actual_scientific_source_acceptance={'source':'weak_mediator_root_review/ACCEPTANCE.json','sha256':next(iter(ACCEPTANCES.values()))})
js(PK+'/PUBLICATION_STATE.json',state)
js(PK+'/ACTUAL_BINDING.json',{'kind':'unbound_source_only_proposal','source_review':None,'base_observation':None,'canonical_review':None,'canonical_parent_binding':None,'staged_review':None,'publication':None})
for name in ['PR_BODY.md','BINDING_CONTRACT.md','CLAIM_STATUS_CERTIFICATE.md','EVIDENCE_SCOPE.md']:put(PK+'/'+name,(D/'packet_text'/name).read_bytes())
js(PK+'/EXPOSURE.json',{'source_exposed':True,'same_selected_model':True,'blind_independence':False,
 'new_scientific_executions':0,'historical_scientific_replays':0,'historical_author_scientific_runs':2,
 'independent_scientific_replications':0,'actual_author_seconds':[0.2838803748600185,0.131953792180866],
 'separate_saved_certificate_check_runs':1,'saved_certificate_check_seconds':0.07717579184100032,
 'separate_scopes':['finite symbolic algebra','fixed two-scenario rational coefficients'],
 'wall_limit_seconds_each':60,'cpu_quota':None,'ram_quota':None,'retained_audit':False})
inputs=[]
for p in sorted(P.rglob('*')):
 if p.is_file():inputs.append({'path':str(p.relative_to(P)),**ident(p.read_bytes())})
js(PK+'/INPUT_MANIFEST.json',{'schema':'weak_mediator_publication_inputs_v1','inputs':inputs})
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
