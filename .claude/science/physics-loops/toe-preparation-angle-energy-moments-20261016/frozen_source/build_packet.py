"""Build a source-only publication proposal; no science code or Git is run."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
D=Path(sys.argv[1]).resolve();N=D.parent;W=N.parent/'correlation_worktree'
P=D/'proposal';PK='.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016'
NOTE='docs/PREPARATION_ANGLE_ENERGY_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-16.md'
SCRIPT='scripts/preparation_angle_energy_moments_2026_10_16.py'
ROOTS={
 'preparation_angle_moment_root_proposal':('FREEZE.json','b2546340ec39a575f6bc97f37f56cc05cf4d381086d7d6298b6edb4dcde0f2ef'),
 'preparation_angle_moment_exposed_check':('FINAL_FREEZE.json','be6b88899f262bc5961fc5ad1916d69185aad53ca84ce6909269afdc0a82c4be'),
 'preparation_angle_moment_root_review':('FREEZE.json','2960f00e3b45f2c38bd4ccf4a673d5d2f610fecf43a82f40c39e239a33303e51'),
}
EXTRA_INPUTS=['review_run.py','bootstrap/accept_preparation_angle_moments.py','bootstrap/accept_preparation_angle_moments_v2.py']
ROOT_RUNS=['preparation_angle_moments_acceptance','preparation_angle_moments_acceptance_v2']
BODIES=[
 ('original_proposal','preparation_angle_moment_root_proposal/PROPOSED_LEMMAS.md'),
 ('exposed_analytical_review','preparation_angle_moment_exposed_check/REVIEW.md'),
 ('controlling_root_qualifications','preparation_angle_moment_root_review/FINAL_QUALIFICATIONS.md'),
]
sha=lambda b:hashlib.sha256(b).hexdigest()
def put(rel,b):
 p=P/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
def js(rel,x):put(rel,(json.dumps(x,indent=2)+'\n').encode())
def ident(b):return {'bytes':len(b),'sha256':sha(b)}
sources={};objects={};freeze_rows=[]
def add(path,alias=None,role='historical_source'):
 b=path.read_bytes();alias=alias or str(path.relative_to(N));h=sha(b)
 r={'source':alias,'original_path':str(path),'role':role,**ident(b),'recovery_path':PK+'/archive/sha256/'+h}
 if alias in sources:assert sources[alias]==r or sources[alias]['sha256']==h
 else:sources[alias]=r
 objects[h]={'path':r['recovery_path'],**ident(b)};put(r['recovery_path'],b)
 return b
assert not P.exists(),'Refuse overwrite of an existing proposal'
for folder,(filename,pin) in ROOTS.items():
 f=N/folder/filename;raw=add(f,role='source_freeze');assert sha(raw)==pin,folder
 freeze=json.loads(raw);key='members';rows=freeze[key]
 for row in rows:
  p=Path(row['path']);p=p if p.is_absolute() else N/folder/p
  p.relative_to(N);b=add(p)
  assert ident(b)=={'bytes':row['bytes'],'sha256':row['sha256']},str(p)
 freeze_rows.append({'folder':folder,'alias':folder+'/'+filename,'key':key,'members':len(rows),'sha256':pin})
for run in ROOT_RUNS:
 for filename in ['EXECUTION.json','executed_source.py','stdout','stderr']:
  add(N/'runs'/run/filename,role='actual_root_metadata_acceptance_evidence')
for rel in EXTRA_INPUTS:add(N/rel,role='original_source_recovery_copy_checked_against_actual_launch_receipt')
parent_name='docs/LOCAL_CONSERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md'
raw=add(W/parent_name,'canonical_parent/'+parent_name,'direct_mathematical_parent')
assert sha(raw)=='6db93809f12315668f720006c6a443301ad682381ce5629c173b1ff1c6d66a7f'
note=(D/'packet_text/WRAPPER.md').read_bytes();wrapper_len=len(note);maps=[]
for name,alias in BODIES:
 raw=(N/alias).read_bytes();note+=('\n\n<!-- Unchanged complete source: '+name+' -->\n\n').encode();start=len(note);note+=raw
 maps.append({'name':name,'source':alias,'container':NOTE,'start_byte_inclusive':start,'end_byte_exclusive':len(note),**ident(raw)})
trailer_start=len(note)
note+=b'\n\nPublication scope remains conditional support under the premises and verification limits above; retained status requires the independent audit path.\n'
put(NOTE,note)
js(PK+'/BODY_MAP.json',{'new_wrapper_bytes':[0,wrapper_len],'trailing_wrapper_bytes':[trailer_start,len(note)],'bodies':maps})
js(PK+'/SOURCE_MANIFEST.json',{'schema':'preparation_angle_moment_source_archive_v1','sources':list(sources.values()),'context_only_paths_not_imported':['interacting_preparation_chronology_candidate','interacting_local_fault_work_candidate']})
js(PK+'/ARCHIVE_INDEX.json',{'objects':list(objects.values()),'recursive_prior_publication_archives':False})
js(PK+'/FROZEN_SOURCE_CLOSURE.json',{'roots':freeze_rows})
parent={'schema':'qualified_source_parents_v1','canonical_binding_complete':False,'direct_mathematical_parents':[
 {'role':'ordered_vacuum_prefix_preparation_only','canonical_path':parent_name,'canonical_claim_id':'local_conserving_preparation_bounded_theorem_note_2026-10-16','source_alias':'canonical_parent/'+parent_name,**ident((W/parent_name).read_bytes())}],
 'excluded_as_mathematical_parents':['interacting_preparation_chronology_candidate','interacting_local_fault_work_candidate','Git ancestry','inhomogeneous comb'],
 'git_ancestry_is_not_mathematical_dependency':True}
js(PK+'/PARENT_BINDING.json',parent)
state={k:None for k in ['source_wrapper_review','source_publication_binding','canonical_integration','current_base_observation','canonical_review','primary_execution','publication_action','retained_audit']}
state.update(scientific_programs_run_this_draft=0,scientific_replays=0)
js(PK+'/PUBLICATION_STATE.json',state)
js(PK+'/ACTUAL_BINDING.json',{'kind':'unbound_source_only_proposal','source_review':None,'base_observation':None,'canonical_review':None,'canonical_parent_binding':None,'publication':None})
for name in ['PR_BODY.md','BINDING_CONTRACT.md','CLAIM_STATUS_CERTIFICATE.md','EVIDENCE_SCOPE.md']:put(PK+'/'+name,(D/'packet_text'/name).read_bytes())
js(PK+'/EXPOSURE.json',{'same_model_source_exposed':True,'source_exposed':True,'prior_preparation_and_integration_exposure':True,'blind_independence':False,'different_model_replication':False,'new_scientific_executions':0,'historical_scientific_executions_for_result':0,'historical_root_metadata_failed_runs':1,'historical_root_metadata_successful_runs':1,'retained_audit':False})
inputs=[]
for p in sorted(P.rglob('*')):
 if p.is_file():inputs.append({'path':str(p.relative_to(P)),**ident(p.read_bytes())})
manifest={'schema':'preparation_angle_moment_publication_inputs_v1','inputs':inputs}
js(PK+'/INPUT_MANIFEST.json',manifest)
msha=sha((P/PK/'INPUT_MANIFEST.json').read_bytes())
template=(D/'primary_template.py').read_text()
generated=template.replace('__MANIFEST_SHA256__',msha).replace('__AUDIT_INPUT_PATHS__',repr([r['path'] for r in inputs]+[PK+'/INPUT_MANIFEST.json'])).replace('__EXPECTED_BODIES__',repr({r['name']:r['sha256'] for r in maps}))
put(SCRIPT,generated.encode())
(D/'BUILD_RESULT.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'note':NOTE,'note_sha256':sha(note),'primary_sha256':sha(generated.encode()),'unchanged_bodies':len(maps),'source_aliases':len(sources),'unique_archive_objects':len(objects),'input_manifest_sha256':msha,'science_executions':0,'canonical_execution':None},indent=2)+'\n')
print((D/'BUILD_RESULT.json').read_text())
