"""Source-integrity only. No scientific runner, simulation or proof is executed."""
from pathlib import Path,PurePosixPath
import hashlib,json
REPO=Path(__file__).resolve().parents[1]
NOTE='docs/INHOMOGENEOUS_COMB_LOCAL_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-16.md'
PACKET='.claude/science/physics-loops/toe-inhomogeneous-comb-local-control-20261016'
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
 manifest=json.loads(raw);require(manifest['schema']=='inhomogeneous_comb_publication_inputs_v1','Input schema')
 rows=manifest['inputs'];paths=[r['path'] for r in rows]
 require(len(paths)==len(set(paths)) and set(AUDIT_INPUT_PATHS)==set(paths)|{PACKET+'/INPUT_MANIFEST.json'},'Exact declared input closure')
 for row in rows:identity(read(row['path']),row)
 note=read(NOTE);header=note.split(b'---',2)[1].decode().splitlines()
 for field in ['claim_type: bounded_theorem','actual_current_surface_status: conditional-support','canonical_parent_binding_complete: false','audit_required_before_effective_retained: true','bare_retained_allowed: false']:
  require(field in header,'Draft scope field '+field)
 maps=json.loads(read(PACKET+'/BODY_MAP.json'))['bodies']
 require({r['name']:r['sha256'] for r in maps}==EXPECTED_BODIES and len(maps)==6,'Six unchanged body roles')
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
 for folder,pin in [('inhomogeneous_local_control_root_review','41e4139b7fb4e69fd14ecdd12504bc2e4cd93724f21733b8cab41e5b99967e0c'),('inhomogeneous_uniform_word_root_review','bfb3169ad9f09e65d510378f23379ead74224b37c6cafe9f1a0112da01da36a7')]:
  raw=src(folder+'/QUALIFIED_ACCEPTANCE.json');require(digest(raw)==pin,'Qualified acceptance pin')
  accepted=json.loads(raw);require(accepted['retained_audit'] is False and accepted['publication'] is None,'Historical acceptance limits')
  identity(src(alias(accepted['qualifications']['path'])),accepted['qualifications'])
 for folder in ['inhomogeneous_local_control_root_exposed_check/runs/exact_species_word','inhomogeneous_uniform_word_exposed_check/runs/exact_logical_check']:
  r=json.loads(src(folder+'/EXECUTION.json'));require(r['exit_code']==0 and r['argv'][1]=='-B','Historical exact run/argv')
  for key in ['source','launcher','precheck','stdout','stderr']:identity(src(alias(r[key]['path'])),r[key])
  require(src(folder+'/stderr.txt')==b'','Historical exact-run empty stderr')
 for run in ['unequal_fixed_word_acceptance','uniform_word_acceptance']:
  r=json.loads(src('runs/'+run+'/EXECUTION.json'));require(r['exit_code']==0,'Actual root metadata run')
  for key in ['source_capture','stdout','stderr']:identity(src(alias(r[key]['path'])),r[key])
  require(r['child_source_at_launch']['sha256']==r['source_capture']['sha256'],'Root executed-source linkage')
  identity(src('review_run.py'),r['recorder'])
 for suffix,expected in [('exact_sparse_check',None),('exact_sparse_check_retry',0)]:
  base='local_conserving_sparse_compiler_candidate/runs/'+suffix+'/'
  r=json.loads(src(base+'EXECUTION.json'));require(r['exit_code'] is expected if expected is None else r['exit_code']==expected,'Preserved sparse launch outcome')
  require(digest(src(base+'SOURCE_AT_LAUNCH.py'))==r['source_sha256'],'Sparse executed-source capture')
  require(digest(src(base+'LAUNCHER_AT_LAUNCH.py'))==r['launcher_sha256'],'Sparse original launcher capture')
  for stream in ['stdout','stderr']:require(digest(src(base+stream+'.txt'))==r[stream+'_sha256'],'Sparse complete stream')
 parent=json.loads(read(PACKET+'/PARENT_BINDING.json'))
 require(parent['canonical_binding_complete'] is False and len(parent['direct_mathematical_parents'])==2,'Two source parents; canonical sparse binding pending')
 a,b=parent['direct_mathematical_parents'];identity(src(a['source_alias']),a)
 require(a['sha256']=='6db93809f12315668f720006c6a443301ad682381ce5629c173b1ff1c6d66a7f','Published parent exact source')
 for key in ['derivation','acceptance','qualifications']:require(digest(src(b[key+'_alias']))==b[key+'_sha256'],'Sparse source parent '+key)
 require(b['canonical_path'] is None and b['canonical_claim_id'] is None and b['canonical_publication'] is None,'Unbound sparse canonical identity')
 exposure=json.loads(read(PACKET+'/EXPOSURE.json'))
 require(exposure['new_scientific_executions']==0 and exposure['historical_new_result_executions']==2 and exposure['separate_direct_candidate_accepted'] is False and exposure['blind_independence'] is False,'Honest exposure and scope')
 state=json.loads(read(PACKET+'/PUBLICATION_STATE.json'))
 require(all(state[k] is None for k in ['source_wrapper_review','canonical_integration','current_base_observation','canonical_review','primary_execution','publication_action','retained_audit']),'Unexecuted publication fields')
 require(state['scientific_programs_run_this_draft']==0 and state['scientific_replays']==0,'No draft scientific replay')
 return {'note_sha256':digest(note),'body_count':len(maps),'source_aliases':len(sources),'archive_objects':len(archive),'science_executions':0}
def verify_actual_binding(read,checked):
 # Intentionally fail closed: root must review a separate bound integration version.
 raise ValueError('UNBOUND SOURCE-ONLY PROPOSAL: canonical source/base/parent/review execution evidence is pending')
def main():
 checked=verify_payload(disk_read);verify_actual_binding(disk_read,checked)
if __name__=='__main__':main()
