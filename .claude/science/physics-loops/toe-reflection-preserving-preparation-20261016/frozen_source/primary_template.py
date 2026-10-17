"""Source-integrity only. No scientific runner, simulation or proof is executed."""
from pathlib import Path,PurePosixPath
import hashlib,json
REPO=Path(__file__).resolve().parents[1]
NOTE='docs/REFLECTION_PRESERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md'
PACKET='.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016'
AUDIT_TIMEOUT_SEC=60
AUDIT_INPUT_PATHS=__AUDIT_INPUT_PATHS__
MANIFEST_SHA256='__MANIFEST_SHA256__'
EXPECTED_BODIES=__EXPECTED_BODIES__
def require(ok,message):
 if not ok:raise ValueError(message)
def digest(data):return hashlib.sha256(data).hexdigest()
def identity(data,row):require(len(data)==row['bytes'] and digest(data)==row['sha256'],'Byte identity mismatch')
def disk_read(rel):
 p=PurePosixPath(rel);require(not p.is_absolute() and '..' not in p.parts,'Unsafe input path')
 resolved=(REPO/rel).resolve();resolved.relative_to(REPO.resolve());return resolved.read_bytes()
def verify_payload(read):
 raw=read(PACKET+'/INPUT_MANIFEST.json');require(digest(raw)==MANIFEST_SHA256,'Input manifest pin')
 manifest=json.loads(raw);require(manifest['schema']=='reflection_preparation_publication_inputs_v1','Input schema')
 rows=manifest['inputs'];paths=[r['path'] for r in rows]
 require(len(paths)==len(set(paths)) and set(AUDIT_INPUT_PATHS)==set(paths)|{PACKET+'/INPUT_MANIFEST.json'},'Exact declared input closure')
 for row in rows:identity(read(row['path']),row)
 note=read(NOTE);header=note.split(b'---',2)[1].decode().splitlines()
 for field in ['claim_type: bounded_theorem','actual_current_surface_status: conditional-support','canonical_parent_binding_complete: false','audit_required_before_effective_retained: true','bare_retained_allowed: false']:
  require(field in header,'Draft scope field '+field)
 maps=json.loads(read(PACKET+'/BODY_MAP.json'))['bodies']
 require({r['name']:r['sha256'] for r in maps}==EXPECTED_BODIES and len(maps)==3,'Three unchanged body roles')
 for row in maps:
  a,b=row['start_byte_inclusive'],row['end_byte_exclusive']
  require(row['container']==NOTE and isinstance(a,int) and isinstance(b,int) and 0<=a<b<=len(note),'Body interval')
  body=note[a:b];identity(body,row);require(note.count(body)==1,'Unique unchanged body')
 sources=json.loads(read(PACKET+'/SOURCE_MANIFEST.json'))['sources']
 require(len({r['source'] for r in sources})==len(sources),'Unique source aliases')
 archive=json.loads(read(PACKET+'/ARCHIVE_INDEX.json'))['objects']
 require(len({r['sha256'] for r in archive})==len(archive),'Deduplicated archive')
 require({r['sha256'] for r in archive}=={r['sha256'] for r in sources},'Exact archive closure')
 for row in archive:identity(read(row['path']),row)
 recovered={}
 for row in sources:
  raw=read(row['recovery_path']);identity(raw,row);recovered[row['source']]=raw
 def src(alias):require(alias in recovered,'Missing source alias '+alias);return recovered[alias]
 def alias(path):
  require('/renewal_20261015_224023/' in path,'Expected renewal source path')
  return path.split('/renewal_20261015_224023/',1)[1]
 freezes=json.loads(read(PACKET+'/FROZEN_SOURCE_CLOSURE.json'))['roots']
 for f in freezes:
  raw=src(f['folder']+'/FREEZE.json');require(digest(raw)==f['sha256'],'Frozen source pin')
  rows=json.loads(raw)[f['key']];require(len(rows)==f['members'],'Freeze member count')
  for row in rows:
   p=row['path'];key=alias(p) if PurePosixPath(p).is_absolute() else f['folder']+'/'+p
   identity(src(key),row)

 decisions=json.loads(read(PACKET+'/ACCEPTANCE_BINDING.json'))
 require(decisions['source_wrapper_review'] is None,'Source acceptance is not wrapper approval')
 for path,pin,qkey in decisions['qualified_source_decisions']:
  raw=src(path);require(digest(raw)==pin,'Source acceptance identity');accepted=json.loads(raw)
  require(accepted['retained_audit'] is False and accepted['publication'] is None,'Original source acceptance limits')
  identity(src(alias(accepted[qkey]['path'])),accepted[qkey])
 # Verify preserved heterogeneous execution schemas; never import their sources.
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
 state=json.loads(read(PACKET+'/PUBLICATION_STATE.json'))
 require(all(state[k] is None for k in ['source_wrapper_review','source_publication','canonical_integration','current_base_observation','canonical_review','primary_execution','publication_action','retained_audit']),'New source and canonical publication remain unbound')
 require(state['scientific_programs_run_this_draft']==0 and state['scientific_replays']==0,'No scientific execution/replay')
 return dict(note_sha256=digest(note),body_count=len(maps),source_aliases=len(sources),archive_objects=len(archive),science_executions=0)
def verify_actual_binding(read,checked):
 raise ValueError('UNBOUND SOURCE-ONLY PROPOSAL: actual wrapper review, base and canonical execution evidence are pending')
def main():
 checked=verify_payload(disk_read);verify_actual_binding(disk_read,checked)
if __name__=='__main__':main()
