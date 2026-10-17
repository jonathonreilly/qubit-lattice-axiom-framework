"""Source-integrity only. No scientific runner, simulation or proof is executed."""
from pathlib import Path,PurePosixPath
import hashlib,json
REPO=Path(__file__).resolve().parents[1]
NOTE='docs/INTERACTING_PREPARATION_CONTROL_WORK_BOUNDED_THEOREM_NOTE_2026-10-16.md'
PACKET='.claude/science/physics-loops/toe-interacting-preparation-control-work-20261016'
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
 manifest=json.loads(raw);require(manifest['schema']=='interacting_control_publication_inputs_v1','Input schema')
 rows=manifest['inputs'];paths=[r['path'] for r in rows]
 require(len(paths)==len(set(paths)) and set(AUDIT_INPUT_PATHS)==set(paths)|{PACKET+'/INPUT_MANIFEST.json'},'Exact declared input closure')
 for row in rows:identity(read(row['path']),row)
 note=read(NOTE);header=note.split(b'---',2)[1].decode().splitlines()
 for field in ['claim_type: bounded_theorem','actual_current_surface_status: conditional-support','canonical_parent_binding_complete: false','audit_required_before_effective_retained: true','bare_retained_allowed: false']:
  require(field in header,'Draft scope field '+field)
 maps=json.loads(read(PACKET+'/BODY_MAP.json'))['bodies']
 require({r['name']:r['sha256'] for r in maps}==EXPECTED_BODIES and len(maps)==9,'Nine unchanged body roles')
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
