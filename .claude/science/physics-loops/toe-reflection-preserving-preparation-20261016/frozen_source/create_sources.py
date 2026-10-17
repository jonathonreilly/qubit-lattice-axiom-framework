"""Generate source-only packaging machinery and bounded source map; no science/Git/integration."""
from pathlib import Path
import ast,difflib,hashlib,json
D=Path(__file__).resolve().parent;N=D.parent;W=N.parent/'correlation_worktree';T=N/'interacting_control_qualified_publication_draft'
PK='.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016'
NOTE='docs/REFLECTION_PRESERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md'
SCRIPT='scripts/reflection_preserving_preparation_2026_10_16.py'
assert D.name=='reflection_preparation_qualified_publication_draft' and not (D/'proposal').exists()
def pin(p):
 b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(p):return json.loads(p.read_text())
def dump(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def replace(s,a,b):assert s.count(a)==1,a;return s.replace(a,b)
names=['build_packet.py','primary_template.py','inspect_packet.py','record_metadata.py','seal_packet.py']
R=D/'reference_machinery';R.mkdir(exist_ok=False);old={name:(T/name).read_text() for name in names}
for name in names:(R/name).write_text(old[name])
new={name:text.replace('INTERACTING_PREPARATION_CONTROL_WORK_BOUNDED_THEOREM_NOTE_2026-10-16','REFLECTION_PRESERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16').replace('interacting_preparation_control_work_2026_10_16','reflection_preserving_preparation_2026_10_16').replace('toe-interacting-preparation-control-work-20261016','toe-reflection-preserving-preparation-20261016').replace('interacting_control_source_archive_v1','reflection_preparation_source_archive_v1').replace('interacting_control_publication_inputs_v1','reflection_preparation_publication_inputs_v1') for name,text in old.items()}
new['build_packet.py']=replace(new['build_packet.py'],"js(PK+'/PARENT_PUBLICATION_EVIDENCE.json',dict(publication_alias='publication_integration/inhomogeneous_comb/PUBLICATION.json',attachment_alias='publication_integration/inhomogeneous_comb/ATTACHMENT.json',applies_to='parent_only',this_source_publication=None))","js(PK+'/PARENT_PUBLICATION_EVIDENCE.json',dict(parent_publication_binding=None,this_source_publication=None,scope='Exact parent bytes only; no live publication observation.'))")
a="js(PK+'/EXPOSURE.json',dict(same_model_source_exposed=True,blind_independence=False,different_model_replication=False,shared_parent_authorship=True,new_scientific_executions=0,historical_bridge_floating_executions=1,preparation_scientific_executions=0,fault_work_scientific_executions=0,retained_audit=False))"
new['build_packet.py']=replace(new['build_packet.py'],a,"js(PK+'/EXPOSURE.json',plan['exposure'])")
p=new['primary_template.py'];p=replace(p,"len(maps)==9,'Nine unchanged body roles'","len(maps)==3,'Three unchanged body roles'")
start=p.index(' # Validate heterogeneous original receipt schemas');end=p.index(" state=json.loads(read(PACKET+'/PUBLICATION_STATE.json'))",start)
block=''' # Verify preserved heterogeneous execution schemas; never import their sources.
 def root_receipt(run,output_key=None,output_alias=None):
  folder='runs/'+run+'/'
  r=json.loads(src(folder+'EXECUTION.json'))
  require(r['exit_code']==0 and r['start_utc']<=r['end_utc'],'Successful historical root receipt')
  require(r['argv'][1]==r['child_source_at_launch']['path'],'Actual historical source argv')
  require(r['source_capture']['path']!=r['child_source_at_launch']['path'],'Distinct original and captured source')
  for key in ['child_source_at_launch','source_capture','recorder','stdout','stderr']:identity(src(alias(r[key]['path'])),r[key])
  require(r['source_capture']['sha256']==r['child_source_at_launch']['sha256'],'Historical source-at-launch linkage')
  require(src(alias(r['stderr']['path']))==b'','Historical empty stderr')
  output=json.loads(src(alias(r['stdout']['path'])))
  if output_key:identity(src(output_alias),output[output_key])
  return r,output
 author,fixture=root_receipt('reflection_preparation_author_check')
 require(author['argv']==['python3',author['child_source_at_launch']['path']],'Original author command')
 require(fixture['M']==6 and fixture['scientific_executions']==1 and fixture['independent_validation'] is False,'One historical finite floating fixture')
 # Its chosen endpoint is a recurrence; these recorded floats are not a new phase test.
 require(fixture['lambda_final']>0 and fixture['matched_eta']==0.22,'Original fixture result identity')
 for mode,original,launcher in [('source_capture','capture_sources.py','record_capture.py'),('final_validation','validate_packet.py','seal_review.py')]:
  folder='reflection_preparation_exposed_check/metadata_runs/'+mode+'/'
  r=json.loads(src(folder+'EXECUTION.json'))
  require(r['exit_code']==0 and r['timed_out'] is False and r['wall_timeout_seconds']==60 and r['new_scientific_runs']==0,'Actual reviewer metadata limits')
  require(r['argv'][1]=='-c' and r['argv'][3]==r['source_at_launch']['path'],'Actual reviewer capture command')
  require(alias(r['argv'][4])=='reflection_preparation_exposed_check/'+original,'Actual reviewer original source')
  for key in ['source_at_launch','recorder_at_launch','stdout','stderr']:identity(src(alias(r[key]['path'])),r[key])
  identity(src('reflection_preparation_exposed_check/'+original),r['source_at_launch'])
  identity(src('reflection_preparation_exposed_check/'+launcher),r['recorder_at_launch'])
  require(src(alias(r['stderr']['path']))==b'','Reviewer metadata empty stderr')
 root_receipt('reflection_preparation_acceptance','acceptance','reflection_preparation_root_review/ACCEPTANCE.json')
 root_receipt('reflection_preparation_qualification_clarification','acceptance','reflection_preparation_root_review_v2/ACCEPTANCE.json')
 accepted=json.loads(src('reflection_preparation_root_review_v2/ACCEPTANCE.json'))
 for key in ['supersedes_for_wording_only','original_qualification_preserved','original_acceptance_execution','controlling_qualifications']:identity(src(alias(accepted[key]['path'])),accepted[key])
 old=src('reflection_preparation_root_review/FINAL_QUALIFICATIONS.md')
 corrected=src('reflection_preparation_root_review_v2/FINAL_QUALIFICATIONS.md')
 before=b'M|delta_lambda| and underlying inputs of order epsilon/M^2 can remain necessary sufficient requests for the chosen allocation.'
 after=b'The state allowance M|delta_lambda|=O(epsilon) gives conservative sufficient underlying input requests of order epsilon/M^2 for this allocation; their necessity is not established.'
 require(old.count(before)==1 and old.replace(before,after)==corrected,'Exact sufficient-only editorial correction')
 parent=json.loads(read(PACKET+'/PARENT_BINDING.json'))
 require(parent['canonical_binding_complete'] is False and len(parent['direct_mathematical_parents'])==1,'One exact-source parent; integration unbound')
 row=parent['direct_mathematical_parents'][0];identity(src(row['source_alias']),row)
 require(row['sha256']=='6db93809f12315668f720006c6a443301ad682381ce5629c173b1ff1c6d66a7f','Direct parent source pin')
 exposure=json.loads(read(PACKET+'/EXPOSURE.json'))
 require(exposure['new_scientific_executions']==0 and exposure['historical_author_floating_executions']==1 and exposure['reviewer_scientific_executions']==0 and exposure['blind_independence'] is False,'Exposure and evidence boundaries')
 require(exposure['fixture_tests_final_phase'] is False and exposure['runtime_composition_claimed'] is False,'Phase-test and composition limits')
'''
p=p[:start]+block+p[end:];new['primary_template.py']=p
p=new['inspect_packet.py'];start=p.index('targets={');end=p.index('\nfor name,path in targets.items():',start)
p=p[:start]+'''targets={
 'altered_original_body':NOTE,
 'altered_current_qualification':source['reflection_preparation_root_review_v2/FINAL_QUALIFICATIONS.md']['recovery_path'],
 'missing_original_qualification':source['reflection_preparation_root_review/FINAL_QUALIFICATIONS.md']['recovery_path'],
 'missing_actual_scientific_source':source['runs/reflection_preparation_author_check/executed_source.py']['recovery_path'],
 'missing_author_stdout':source['runs/reflection_preparation_author_check/stdout']['recovery_path'],
 'missing_root_acceptance_source':source['runs/reflection_preparation_acceptance/executed_source.py']['recovery_path'],
 'missing_clarification_source':source['runs/reflection_preparation_qualification_clarification/executed_source.py']['recovery_path'],
 'missing_direct_parent':source['canonical_source/docs/LOCAL_CONSERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md']['recovery_path'],
}'''+p[end:];new['inspect_packet.py']=p
p=new['seal_packet.py'].replace("len(result['scoped_metadata_mutants'])==7","len(result['scoped_metadata_mutants'])==9").replace('scoped_refusals=7','scoped_refusals=9').replace('source_only_interacting_preparation_control_work_publication_draft','source_only_reflection_preserving_preparation_publication_draft')
# Stronger end-of-packaging check preserves fixed authoring inputs; no invented old checkpoint bytes.
p=replace(p,"  assert (folder/'stderr').read_bytes()==b''","  assert (folder/'stderr').read_bytes()==b''\n  for row in json.loads(Path(r['input_identities_at_launch']['path']).read_text()):same(Path(row['path']),row)")
new['seal_packet.py']=p
for name,text in new.items():ast.parse(text);(D/name).write_text(text)
roots={
 'reflection_preparation_root_proposal':'280d0564306f548990b0a342a45676d331997539ff3cd59f7809f8671a281b68',
 'reflection_preparation_exposed_check':'ddb52f94cb711d5cdea1271dec89a1e1b22002d055d89676c3f94cec01dc13aa',
 'reflection_preparation_root_review':'c0fc236512c4b57b10a27edcbccc824e83112b9e6c8e195a89ed2511c017d827',
 'reflection_preparation_root_review_v2':'dc4838051396e454d6fdccc6c9d3cd6df8b87a3ffdc7ffcd7d0924e8e44fe9b5'}
for folder,hash_ in roots.items():assert pin(N/folder/'FREEZE.json')['sha256']==hash_
extra={}
def add(path,alias=None,role='actual_evidence'):
 row=pin(path);key=alias or str(path.relative_to(N));extra[key]=dict(row,alias=key,role=role)
for run in ['reflection_preparation_author_check','reflection_preparation_acceptance','reflection_preparation_qualification_clarification']:
 folder=N/'runs'/run
 for path in folder.iterdir():
  if path.is_file():add(path)
 r=read(folder/'EXECUTION.json')
 for key in ['child_source_at_launch','recorder']:add(Path(r[key]['path']))
parent=W/'docs/LOCAL_CONSERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md';assert pin(parent)['sha256']=='6db93809f12315668f720006c6a443301ad682381ce5629c173b1ff1c6d66a7f'
parent_alias='canonical_source/docs/'+parent.name;add(parent,parent_alias,'direct_canonical_math_parent')
for name in names:add(T/name,role='packaging_machinery_only')
plan=dict(packet=PK,note=NOTE,script=SCRIPT,roots=roots,extra=list(extra.values()),bodies=[['original_proposal','reflection_preparation_root_proposal/PROPOSED_LEMMAS.md'],['complete_exposed_review','reflection_preparation_exposed_check/REVIEW.md'],['current_controlling_qualifications','reflection_preparation_root_review_v2/FINAL_QUALIFICATIONS.md']],parents=[dict(pin(parent),source_alias=parent_alias,canonical_path='docs/'+parent.name)],acceptances=[['reflection_preparation_root_review_v2/ACCEPTANCE.json','e66487255904aa97e24e27a9643c14a128c9188e2153d56142347b86eea1e724','controlling_qualifications']],closure_rule='Four complete bounded freezes plus actual author/acceptance/clarification original and captured sources/recorder/fullstreams, one exact math parent, five machinery sources. No recursive publication archive.',exposure=dict(same_model_source_exposed=True,blind_independence=False,different_model_replication=False,shared_parent_authorship=True,new_scientific_executions=0,historical_author_floating_executions=1,reviewer_scientific_executions=0,fixture_tests_final_phase=False,analytic_M4_nonrecurrence_discriminator=True,runtime_composition_claimed=False,retained_audit=False))
dump(D/'SOURCE_PLAN.json',plan)
def functions(s):
 lines=s.splitlines(True);return {n.name:''.join(lines[n.lineno-1:n.end_lineno]) for n in ast.parse(s).body if isinstance(n,ast.FunctionDef)}
comparisons=[];diffs=D/'machinery_diffs';diffs.mkdir(exist_ok=False)
for name in names:
 a,b=functions(old[name]),functions(new[name]);diff=''.join(difflib.unified_diff(old[name].splitlines(True),new[name].splitlines(True),fromfile='actual_interacting_source/'+name,tofile='proposed_reflection_source/'+name))
 (diffs/(name+'.diff')).write_text(diff)
 comparisons.append(dict(name=name,template=str(T/name),template_sha256=pin(T/name)['sha256'],new_sha256=pin(D/name)['sha256'],unchanged_functions=[k for k in b if k in a and a[k]==b[k]],changed_or_new_functions=[k for k in b if k not in a or a[k]!=b[k]],removed_functions=[k for k in a if k not in b],top_level_code_review_required=old[name]!=new[name],full_source_exact=old[name]==new[name]))
dump(D/'REUSE_AND_READ_MAP.json',dict(exact_function_comparison=comparisons,originals_not_modified=True,archive_reuse='Five exact machinery sources only; no prior publication archive.',new_science_claims=False))
oldq=(N/'reflection_preparation_root_review/FINAL_QUALIFICATIONS.md').read_text();newq=(N/'reflection_preparation_root_review_v2/FINAL_QUALIFICATIONS.md').read_text()
(D/'QUALIFICATION_EVOLUTION.diff').write_text(''.join(difflib.unified_diff(oldq.splitlines(True),newq.splitlines(True),fromfile='original_qualification1c727dad',tofile='current_qualification4474c5cd')))
dump(D/'AUTHORING_EVIDENCE.json',dict(kind='source_authoring_not_scientific_execution',source=pin(Path(__file__)),scope='This deterministic generation script was invoked directly through the tool. No separate prelaunch recorder envelope is claimed for authoring. Actual build/inspection/seal metadata executions use preserved launch sources and full streams.',canonical_changes=False,scientific_executions=0))
print(json.dumps(dict(source_plan=pin(D/'SOURCE_PLAN.json'),machinery_files=names,bodies=3,science_executions=0),indent=2))
