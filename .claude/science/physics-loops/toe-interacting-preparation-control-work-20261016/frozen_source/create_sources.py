"""Generate source-only packet machinery. No scientific program is imported."""
from pathlib import Path
import hashlib,json,difflib,ast
D=Path(__file__).resolve().parent;N=D.parent;W=N.parent/'correlation_worktree';OLD=N/'inhomogeneous_comb_qualified_publication_draft'
sha=lambda b:hashlib.sha256(b).hexdigest()
def write(name,s):
 p=D/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
def dump(name,v):write(name,json.dumps(v,indent=2)+'\n')
PK='.claude/science/physics-loops/toe-interacting-preparation-control-work-20261016'
NOTE='docs/INTERACTING_PREPARATION_CONTROL_WORK_BOUNDED_THEOREM_NOTE_2026-10-16.md';SCRIPT='scripts/interacting_preparation_control_work_2026_10_16.py'
roots={
'interacting_ramp_bridge_root_proposal':'6020f7ad4f5382dd63cb6732952c9ae8c0dcd37583963cddb94a585a5f56405a',
'interacting_ramp_bridge_exposed_check':'83bf3031df5ff937a51f51a1a9739af292ae9c4c6b08ecdb11f173774dbc791d',
'interacting_ramp_bridge_root_review':'ff9e1f34a51caf2026397296b5eab01aac3e4303e78d68dc7e6aedc687fc77a4',
'interacting_preparation_chronology_candidate':'4fbed25fe83d4ea4f0550848493755496e03c932dc549e745c1189e799ba9b2f',
'interacting_preparation_chronology_exposed_check':'6fd82d9be7d1c8a70fb56968fd9a71c52694b61c8b71f02a0315e3a43a93ddcb',
'interacting_preparation_chronology_root_review':'e90518e3bc1f397ad71807bd387f3542f13c1fb2b1baae9c50dcf7afb87d0af3',
'interacting_local_fault_work_candidate':'7951d1048a2d6a9f882f672de5f6ce036dc87adc927e88d540329a97e648ee37',
'interacting_local_fault_work_exposed_check':'906cf5f7164e8595ec9b9a0c89c104a507dfcbfecd74581a0c946ae75fb2eb34',
'interacting_local_fault_work_root_review':'746b566fa8a9a658b0e00bca39a1a9e79e9dc7fad4271dd831645b82fc69ad88'}
bodies=[]
for tag,orig,filename in [('bridge','interacting_ramp_bridge_root_proposal','PROPOSED_LEMMAS.md'),('preparation','interacting_preparation_chronology_candidate','DERIVATION.md'),('fault_work','interacting_local_fault_work_candidate','DERIVATION.md')]:
 stem={'bridge':'interacting_ramp_bridge','preparation':'interacting_preparation_chronology','fault_work':'interacting_local_fault_work'}[tag]
 bodies += [(tag+'_original',orig+'/'+filename),(tag+'_exposed_review',stem+'_exposed_check/REVIEW.md'),(tag+'_controlling_qualifications',stem+'_root_review/FINAL_QUALIFICATIONS.md')]
parents=[]
for name,h,cid in [('LOCAL_CONSERVING_PREPARATION','6db93809f12315668f720006c6a443301ad682381ce5629c173b1ff1c6d66a7f','local_conserving_preparation'),('INHOMOGENEOUS_COMB_LOCAL_CONTROL','d88f51f5d90abca373a312d20580c3fe9dd3e999d1965ec70bd26466fe1670c5','inhomogeneous_comb_local_control')]:
 rel='docs/'+name+'_BOUNDED_THEOREM_NOTE_2026-10-16.md';b=(W/rel).read_bytes();assert sha(b)==h
 parents.append(dict(canonical_path=rel,canonical_claim_id=cid+'_bounded_theorem_note_2026-10-16',source_alias='canonical_parent/'+rel,bytes=len(b),sha256=h))
extra=[]
def extra_path(p,role,alias=None):
 b=p.read_bytes();extra.append(dict(path=str(p),alias=alias or str(p.relative_to(N)),role=role,bytes=len(b),sha256=sha(b)))
for p in parents:extra_path(W/p['canonical_path'],'direct_mathematical_parent',p['source_alias'])
for run in ['interacting_ramp_acceptance','interacting_preparation_acceptance','interacting_fault_work_acceptance']:
 for p in sorted((N/'runs'/run).iterdir()):
  if p.is_file():extra_path(p,'actual_source_acceptance_metadata_evidence')
extra_path(N/'review_run.py','current_exact_recovery_copy_of_root_recorder_not_launch_capture')
for name in ['PUBLICATION.json','ATTACHMENT.json']:
 extra_path(N/'publication_integration/inhomogeneous_comb'/name,'actual_parent_publication_not_this_draft_approval')
for name in ['build_packet.py','primary_template.py','inspect_packet.py','record_metadata.py','seal_packet.py']:
 extra_path(OLD/name,'packaging_template_only_no_scientific_dependency')
for rel in ['docs/ai_methodology/SCIENCE_WORKFLOW.md','docs/ai_methodology/skills/ai-physics-lane-builder/SKILL.md','docs/ai_methodology/skills/workhorse/SKILL.md','docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md','docs/WRITING_VOICE_GUIDE_2026-04-25.md']:
 extra_path(W/rel,'methodology_snapshot_no_science_premise','authority/'+rel)
accept=[('interacting_ramp_bridge_root_review/QUALIFIED_ACCEPTANCE.json','857b4ce85a3f1a826e4dfd0c4342df5845e4991e60d3c5f85b1d30e3b98d93fa','qualifications'),('interacting_preparation_chronology_root_review/ACCEPTANCE.json','0cbc3e8b6020894222319c43ae4f1deda6f75be8a020b886982dd445e669d6e8','controlling_qualifications'),('interacting_local_fault_work_root_review/ACCEPTANCE.json','10a4832688c81c227c74f29de239964a5d7d268000a4d7bf1babf6f8b441c4c8','controlling_qualifications')]
dump('SOURCE_PLAN.json',dict(packet=PK,note=NOTE,script=SCRIPT,roots=roots,bodies=bodies,extra=extra,parents=parents,acceptances=accept,closure_rule='Exactly each of nine specified freeze member sets plus explicit extras; no recursive traversal of captured parent freeze references or prior publication archives.'))
# Reuse the established byte/address helpers; source selection and result metadata are new.
oldbuild=(OLD/'build_packet.py').read_text();helpers=oldbuild[oldbuild.index('sha=lambda'):oldbuild.index("assert not P.exists()")]
build='''"""Build only the scoped source publication proposal; no science, Git or canonical writes."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
D=Path(sys.argv[1]).resolve();N=D.parent;P=D/'proposal'
plan=json.loads((D/'SOURCE_PLAN.json').read_text());PK=plan['packet'];NOTE=plan['note'];SCRIPT=plan['script']
'''+helpers+'''
assert not P.exists(),'Refuse overwrite of existing proposal'
for folder,pin in plan['roots'].items():
 raw=add(N/folder/'FREEZE.json',role='source_freeze');assert sha(raw)==pin,folder
 frozen=json.loads(raw);key='members' if 'members' in frozen else 'files';rows=frozen[key]
 for row in rows:
  p=Path(row['path']);p=p if p.is_absolute() else N/folder/p;p.relative_to(N)
  raw=add(p);assert ident(raw)=={'bytes':row['bytes'],'sha256':row['sha256']},str(p)
 freeze_rows.append(dict(folder=folder,key=key,members=len(rows),sha256=pin))
for row in plan['extra']:
 raw=add(Path(row['path']),row['alias'],row['role']);assert ident(raw)=={'bytes':row['bytes'],'sha256':row['sha256']}
note=(D/'packet_text/WRAPPER.md').read_bytes();wrapper_len=len(note);maps=[]
for name,alias in plan['bodies']:
 raw=(N/alias).read_bytes();note+=('\\n\\n<!-- Unchanged complete source: '+name+' -->\\n\\n').encode();start=len(note);note+=raw
 maps.append(dict(name=name,source=alias,container=NOTE,start_byte_inclusive=start,end_byte_exclusive=len(note),**ident(raw)))
put(NOTE,note)
js(PK+'/BODY_MAP.json',dict(new_wrapper_bytes=[0,wrapper_len],bodies=maps))
js(PK+'/SOURCE_MANIFEST.json',dict(schema='interacting_control_source_archive_v1',sources=list(sources.values())))
js(PK+'/ARCHIVE_INDEX.json',dict(objects=list(objects.values())))
js(PK+'/FROZEN_SOURCE_CLOSURE.json',dict(roots=freeze_rows,closure_rule=plan['closure_rule']))
js(PK+'/PARENT_BINDING.json',dict(canonical_binding_complete=False,direct_mathematical_parents=plan['parents'],git_ancestry_is_not_mathematical_dependency=True))
js(PK+'/ACCEPTANCE_BINDING.json',dict(qualified_source_decisions=plan['acceptances'],source_wrapper_review=None))
js(PK+'/PARENT_PUBLICATION_EVIDENCE.json',dict(publication_alias='publication_integration/inhomogeneous_comb/PUBLICATION.json',attachment_alias='publication_integration/inhomogeneous_comb/ATTACHMENT.json',applies_to='parent_only',this_source_publication=None))
state={k:None for k in ['source_wrapper_review','source_publication','canonical_integration','current_base_observation','canonical_review','primary_execution','publication_action','retained_audit']};state.update(scientific_programs_run_this_draft=0,scientific_replays=0)
js(PK+'/PUBLICATION_STATE.json',state)
js(PK+'/ACTUAL_BINDING.json',dict(kind='unbound_source_only_proposal',source_review=None,base_observation=None,canonical_review=None,canonical_parent_binding=None))
for name in ['PR_BODY.md','BINDING_CONTRACT.md']:put(PK+'/'+name,(D/'packet_text'/name).read_bytes())
js(PK+'/EXPOSURE.json',dict(same_model_source_exposed=True,blind_independence=False,different_model_replication=False,shared_parent_authorship=True,new_scientific_executions=0,historical_bridge_floating_executions=1,preparation_scientific_executions=0,fault_work_scientific_executions=0,retained_audit=False))
inputs=[dict(path=str(p.relative_to(P)),**ident(p.read_bytes())) for p in sorted(P.rglob('*')) if p.is_file()]
js(PK+'/INPUT_MANIFEST.json',dict(schema='interacting_control_publication_inputs_v1',inputs=inputs))
msha=sha((P/PK/'INPUT_MANIFEST.json').read_bytes());template=(D/'primary_template.py').read_text()
generated=template.replace('__MANIFEST_SHA256__',msha).replace('__AUDIT_INPUT_PATHS__',repr([r['path'] for r in inputs]+[PK+'/INPUT_MANIFEST.json'])).replace('__EXPECTED_BODIES__',repr({r['name']:r['sha256'] for r in maps}))
put(SCRIPT,generated.encode())
result=dict(utc=datetime.now(timezone.utc).isoformat(),note=NOTE,note_sha256=sha(note),unchanged_bodies=len(maps),source_aliases=len(sources),unique_archive_objects=len(objects),freeze_member_counts=[r['members'] for r in freeze_rows],input_manifest_sha256=msha,scientific_executions=0,canonical_execution=None)
(D/'BUILD_RESULT.json').write_text(json.dumps(result,indent=2)+'\\n');print(json.dumps(result,indent=2))
'''
write('build_packet.py',build)
oldprimary=(OLD/'primary_template.py').read_text();primary=oldprimary[:oldprimary.index(" for folder,pin in [('inhomogeneous_local_control_root_review'")]
primary=primary.replace('INHOMOGENEOUS_COMB_LOCAL_CONTROL','INTERACTING_PREPARATION_CONTROL_WORK').replace('toe-inhomogeneous-comb-local-control','toe-interacting-preparation-control-work').replace('inhomogeneous_comb_publication_inputs_v1','interacting_control_publication_inputs_v1').replace('len(maps)==6','len(maps)==9').replace('Six unchanged body roles','Nine unchanged body roles')
primary+='''
 decisions=json.loads(read(PACKET+'/ACCEPTANCE_BINDING.json'))
 require(decisions['source_wrapper_review'] is None,'Source acceptance is not wrapper approval')
 for path,pin,qkey in decisions['qualified_source_decisions']:
  raw=src(path);require(digest(raw)==pin,'Source acceptance identity');accepted=json.loads(raw)
  require(accepted['retained_audit'] is False and accepted['publication'] is None,'Original source acceptance limits')
  identity(src(alias(accepted[qkey]['path'])),accepted[qkey])
 # Validate heterogeneous original receipt schemas without rewriting them.
 base='interacting_ramp_bridge_exposed_check/runs/ramp_interface/'
 r=json.loads(src(base+'EXECUTION.json'));require(r['exit_code']==0 and r['argv'][1]=='-B','Historical floating bridge execution')
 for key in ['source','launcher','precheck','stdout','stderr']:identity(src(alias(r[key]['path'])),r[key])
 require(json.loads(src(base+'stdout.txt'))==json.loads(src(base+'output/RESULT.json')),'Bridge recorded result equality')
 for folder in ['interacting_preparation_chronology_candidate/runs/source_capture/','interacting_local_fault_work_exposed_check/runs/source_integrity/']:
  r=json.loads(src(folder+'EXECUTION.json'));require(r['exit_code']==0 and r['argv'][1]=='-B','Actual metadata child argv')
  require(digest(src(folder+'executed_source.py'))==r['source_sha256'],'Original metadata source capture')
  require(digest(src(folder+'executed_launcher.py'))==r['launcher_sha256'],'Original metadata launcher capture')
  for key,row in r['streams'].items():identity(src(folder+key),row)
 folder='interacting_preparation_chronology_exposed_check/runs/source_capture/'
 r=json.loads(src(folder+'EXECUTION.json'));require(r['exit_code']==0 and r['child_argv'][1]=='-B','Preparation review metadata')
 for key in ['source','launcher']:identity(src(alias(r[key]['path'])),r[key])
 for row in r['streams'].values():identity(src(alias(row['path'])),row)
 folder='interacting_preparation_chronology_exposed_check/runs/final_validation/'
 r=json.loads(src(folder+'EXECUTION.json'));require(r['exit_code']==0,'Preparation final metadata validation')
 identity(src(alias(r['source_and_launcher']['path'])),r['source_and_launcher'])
 for row in r['streams'].values():identity(src(alias(row['path'])),row)
 # This original candidate has streams/source, but no actual execution envelope.
 # Do not synthesize an argv, exit code or source-at-launch assertion for it.
 failed=src('interacting_local_fault_work_candidate/METADATA_CHECK.stderr.txt')
 require(b'AssertionError' in failed,'Preserved failed metadata pin attempt')
 require(src('interacting_local_fault_work_candidate/METADATA_CHECK_2.stderr.txt')==b'','Corrected metadata stream retained')
 for run in ['interacting_ramp_acceptance','interacting_preparation_acceptance','interacting_fault_work_acceptance']:
  r=json.loads(src('runs/'+run+'/EXECUTION.json'));require(r['exit_code']==0,'Actual root source acceptance metadata')
  for key in ['source_capture','stdout','stderr']:identity(src(alias(r[key]['path'])),r[key])
  require(r['source_capture']['sha256']==r['child_source_at_launch']['sha256'],'Root source-at-launch linkage')
  identity(src('review_run.py'),r['recorder'])
 parent=json.loads(read(PACKET+'/PARENT_BINDING.json'))
 require(parent['canonical_binding_complete'] is False and len(parent['direct_mathematical_parents'])==2,'Two exact-source parents; integration unbound')
 pins=['6db93809f12315668f720006c6a443301ad682381ce5629c173b1ff1c6d66a7f','d88f51f5d90abca373a312d20580c3fe9dd3e999d1965ec70bd26466fe1670c5']
 for row,pin in zip(parent['direct_mathematical_parents'],pins):identity(src(row['source_alias']),row);require(row['sha256']==pin,'Direct parent source pin')
 pub=json.loads(src('publication_integration/inhomogeneous_comb/PUBLICATION.json'))
 attach=json.loads(src('publication_integration/inhomogeneous_comb/ATTACHMENT.json'))
 require(pub['number']==9648 and pub['isDraft'] is False and pub['state']=='OPEN' and pub['source_note']['sha256']==pins[1],'Actual recorded parent publication')
 require(attach['arguments']['url']==pub['url'] and attach['actual_result']['isError'] is False,'Actual parent attachment envelope')
 exposure=json.loads(read(PACKET+'/EXPOSURE.json'))
 require(exposure['new_scientific_executions']==0 and exposure['historical_bridge_floating_executions']==1 and exposure['preparation_scientific_executions']==0 and exposure['fault_work_scientific_executions']==0 and exposure['blind_independence'] is False,'Exposure and evidence boundaries')
 state=json.loads(read(PACKET+'/PUBLICATION_STATE.json'))
 require(all(state[k] is None for k in ['source_wrapper_review','source_publication','canonical_integration','current_base_observation','canonical_review','primary_execution','publication_action','retained_audit']),'New source and canonical publication remain unbound')
 require(state['scientific_programs_run_this_draft']==0 and state['scientific_replays']==0,'No scientific execution/replay')
 return dict(note_sha256=digest(note),body_count=len(maps),source_aliases=len(sources),archive_objects=len(archive),science_executions=0)
def verify_actual_binding(read,checked):
 raise ValueError('UNBOUND SOURCE-ONLY PROPOSAL: actual wrapper review, base and canonical execution evidence are pending')
def main():
 checked=verify_payload(disk_read);verify_actual_binding(disk_read,checked)
if __name__=='__main__':main()
'''
write('primary_template.py',primary)
inspect=(OLD/'inspect_packet.py').read_text().replace('INHOMOGENEOUS_COMB_LOCAL_CONTROL','INTERACTING_PREPARATION_CONTROL_WORK').replace('inhomogeneous_comb_local_control','interacting_preparation_control_work').replace('toe-inhomogeneous-comb-local-control','toe-interacting-preparation-control-work')
a=inspect.index('targets={');b=inspect.index('\nfor name,path in targets.items():')
inspect=inspect[:a]+'''targets={
 'altered_original_body':NOTE,
 'altered_fault_qualification':source['interacting_local_fault_work_root_review/FINAL_QUALIFICATIONS.md']['recovery_path'],
 'missing_actual_scientific_source':source['interacting_ramp_bridge_exposed_check/runs/ramp_interface/SOURCE_AT_LAUNCH.py']['recovery_path'],
 'missing_preserved_failed_metadata':source['interacting_local_fault_work_candidate/METADATA_CHECK.stderr.txt']['recovery_path'],
 'missing_root_actual_acceptance_source':source['runs/interacting_preparation_acceptance/executed_source.py']['recovery_path'],
 'missing_parent_attachment':source['publication_integration/inhomogeneous_comb/ATTACHMENT.json']['recovery_path'],
}'''+inspect[b:]
write('inspect_packet.py',inspect)
record=(OLD/'record_metadata.py').read_text();a=record.index("if mode=='build':");b=record.index('inputs=[pin(p)',a)
record=record[:a]+'''if mode=='build':
 plan=json.loads((D/'SOURCE_PLAN.json').read_text())
 for folder in plan['roots']:
  f=N/folder/'FREEZE.json';input_paths.add(f);v=json.loads(f.read_text())
  for row in v.get('members',v.get('files',[])):
   p=Path(row['path']);input_paths.add(p if p.is_absolute() else N/folder/p)
 input_paths.update(Path(row['path']) for row in plan['extra'])
'''+record[b:]
record=record.replace("'kind':'publication_packaging_metadata_only','argv':argv", "'kind':'publication_packaging_metadata_only','launcher_orig_argv':list(sys.orig_argv),'argv':argv")
write('record_metadata.py',record)
# Exact function-level reuse plus complete source diffs; no claim unchanged where adaptation occurred.
reuse=[]
for name in ['build_packet.py','primary_template.py','inspect_packet.py','record_metadata.py']:
 old=(OLD/name).read_text();new=(D/name).read_text()
 def funcs(s):
  return {n.name:ast.get_source_segment(s,n) for n in ast.parse(s).body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
 of,nf=funcs(old),funcs(new)
 reuse.append(dict(name=name,template=str(OLD/name),template_sha256=sha(old.encode()),new_sha256=sha(new.encode()),unchanged_functions=[k for k in nf if k in of and nf[k]==of[k]],changed_or_new_functions=[k for k in nf if k not in of or nf[k]!=of[k]],removed_functions=sorted(set(of)-set(nf)),top_level_code_review_required=True))
 write('machinery_diffs/'+name+'.diff',''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=str(OLD/name),tofile=str(D/name))))
dump('REUSE_AND_READ_MAP.json',dict(exact_function_comparison=reuse,originals_not_modified=True,archive_reuse='Only five source machinery files; no prior publication archive copied.',seal='New local-only seal; prior Git-show methodology stage intentionally omitted.'))
print(json.dumps(dict(created='source plan and four metadata programs',sources=len(extra),body_count=len(bodies),science_executions=0)))
