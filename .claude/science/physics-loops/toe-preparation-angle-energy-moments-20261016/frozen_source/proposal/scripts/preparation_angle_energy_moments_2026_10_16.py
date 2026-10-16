"""Source-integrity only. No scientific runner, simulation or proof is executed."""
from pathlib import Path,PurePosixPath
import hashlib,json
REPO=Path(__file__).resolve().parents[1]
NOTE='docs/PREPARATION_ANGLE_ENERGY_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-16.md'
PACKET='.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016'
AUDIT_TIMEOUT_SEC=60
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/BINDING_CONTRACT.md', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/BODY_MAP.json', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/EVIDENCE_SCOPE.md', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/EXPOSURE.json', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/FROZEN_SOURCE_CLOSURE.json', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/PARENT_BINDING.json', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/PR_BODY.md', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/04de78019cc4d95d9810d3b0e75c7bcdc92f912b3a12010f741717156d4628de', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/1fa1f822782b7ae7c37d959f1aaef13e694ce355e382bd585f49e1a82ff3322d', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/2960f00e3b45f2c38bd4ccf4a673d5d2f610fecf43a82f40c39e239a33303e51', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/2c12dc8f0e3ab8f607f7681124fe0244c330c264414a2b2bc497adaf42cf1a49', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/2d690b21dd02f31acafaa3d68790afba6d2f248ba0ba1e9710dfdb1eb22177c4', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/3319576ec0caf002d6219cee3a3a0b661f98f29ac56474d4d497a2e89d01ebd9', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/4fab2230a6e338bfb5c0bb227983e5de0346cee87786ce8b9bc9d0d3db1816fc', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/5aba6a6d5e5ac796eabbd463c7156228e701ca00aba6b30b56f9230ba39206ca', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/5ba89f88975389dbc6367e930baa023fc51743d3b0227836d9e33384fa18789a', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/62a5e99ba53e009c3dbc89aec00ddcfd88f305047ea8ce71142f3da9a3f37680', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/66228959ca28222a2fa07a5fce462822ec9e7252e7e88d402ea51c0dc4974486', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/6db93809f12315668f720006c6a443301ad682381ce5629c173b1ff1c6d66a7f', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/74247a4b93e506a1aa44b250e7726c1ef677e38d46d8dfb80b33b0eab5292249', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/76a5ef112dfeea37d65e6c9797aa208d454c57cb69955e90751be18a48748187', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/a57fec5012d5af54b2cec9748b416dd73e6ca071c6db0f04ea2c8bbf6b07ae76', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/ad7611e1d74c5063985a04f4cdbe156e59afcea0a8c2da376e7af25d6d632369', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/b08bce8924387b5faf54911ea7e761a974ec08280dce7c819877257209713359', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/b2161150997749c72ad1e0867a4fcf519ebdbfa07bd526d1faa552eb1f567428', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/b2546340ec39a575f6bc97f37f56cc05cf4d381086d7d6298b6edb4dcde0f2ef', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/bcd78fc50cbafc0564f3ac74803815e3ad96aaeea75d0c37b4842ef6282dd526', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/be6b88899f262bc5961fc5ad1916d69185aad53ca84ce6909269afdc0a82c4be', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/c20291887b2a4dd00244bdc6a0d165ddef7a6f72c63cd808cc037e6a1ad58d13', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/c2ffe7dc8c0792a5590e7d1ee6557cb3b72489ea7c4d855ed96b0afb45756566', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/d32049fc5fe1f8ec166d333ace01e5b1738991e51773eebb5085eeff172ecec4', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/ea1d2bdb8f7a8783dec20dc9945dfb0cd36cf94e74ee6cead60f62fde5a77158', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/f0417ca63a827426d0e70058341a46e4dafc61f1f8d4a975d5ee30c8acda787a', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/f847661ceab121363e9cb8c492836398704a450a53efb896793b8a0b742de896', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/archive/sha256/fd847fb098e1fa15f13a309065e99065128c2be6adaf2a6c336c3a38e5a9aced', 'docs/PREPARATION_ANGLE_ENERGY_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-16.md', '.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016/INPUT_MANIFEST.json']
MANIFEST_SHA256='e92f416e9d5aeaaeacb2e4e86f152a9f6c3de6752a09b45bf65496c3982d8f1b'
EXPECTED_BODIES={'original_proposal': 'fd847fb098e1fa15f13a309065e99065128c2be6adaf2a6c336c3a38e5a9aced', 'exposed_analytical_review': '2c12dc8f0e3ab8f607f7681124fe0244c330c264414a2b2bc497adaf42cf1a49', 'controlling_root_qualifications': '5ba89f88975389dbc6367e930baa023fc51743d3b0227836d9e33384fa18789a'}
EXPECTED_FREEZES={
 'preparation_angle_moment_root_proposal/FREEZE.json':'b2546340ec39a575f6bc97f37f56cc05cf4d381086d7d6298b6edb4dcde0f2ef',
 'preparation_angle_moment_exposed_check/FINAL_FREEZE.json':'be6b88899f262bc5961fc5ad1916d69185aad53ca84ce6909269afdc0a82c4be',
 'preparation_angle_moment_root_review/FREEZE.json':'2960f00e3b45f2c38bd4ccf4a673d5d2f610fecf43a82f40c39e239a33303e51',
}
ROOT_RUNS={
 'preparation_angle_moments_acceptance':(1,'04de78019cc4d95d9810d3b0e75c7bcdc92f912b3a12010f741717156d4628de'),
 'preparation_angle_moments_acceptance_v2':(0,'4fab2230a6e338bfb5c0bb227983e5de0346cee87786ce8b9bc9d0d3db1816fc'),
}
def require(ok,message):
 if not ok:raise ValueError(message)
def digest(data):return hashlib.sha256(data).hexdigest()
def identity(data,row):require(len(data)==row['bytes'] and digest(data)==row['sha256'],'Byte identity mismatch')
def disk_read(rel):
 p=PurePosixPath(rel);require(not p.is_absolute() and '..' not in p.parts,'Unsafe input path')
 resolved=(REPO/rel).resolve();resolved.relative_to(REPO.resolve());return resolved.read_bytes()
def renewal_alias(path):
 marker='/renewal_20261015_224023/'
 require(isinstance(path,str) and path.count(marker)==1,'Expected renewal source path')
 alias=path.split(marker,1)[1];p=PurePosixPath(alias)
 require(not p.is_absolute() and '..' not in p.parts,'Safe historical source alias')
 return alias
def verify_root_record(src,run_name,expected_exit,expected_source):
 prefix='runs/'+run_name+'/'
 r=json.loads(src(prefix+'EXECUTION.json'))
 require(r['exit_code']==expected_exit,'Preserved root metadata exit code')
 require(len(r['argv'])==2 and r['argv'][0]=='python3' and r['argv'][1]==r['child_source_at_launch']['path'],'Exact original root child argv')
 require(renewal_alias(r['source_capture']['path'])==prefix+'executed_source.py','Distinct actual root capture location')
 require(r['source_capture']['path']!=r['child_source_at_launch']['path'],'Root original source and capture are distinct')
 require(r['child_source_at_launch']['sha256']==r['source_capture']['sha256']==expected_source,'Root executed-source hash')
 suffix='_v2' if run_name.endswith('_v2') else ''
 require(renewal_alias(r['child_source_at_launch']['path'])=='bootstrap/accept_preparation_angle_moments'+suffix+'.py','Original root source path')
 for key in ['child_source_at_launch','source_capture','recorder','stdout','stderr']:identity(src(renewal_alias(r[key]['path'])),r[key])
 require(r['child_source_at_launch']['bytes']==r['source_capture']['bytes'],'Root source/capture lengths')
 require(r['start_utc']<r['end_utc'] and r['elapsed_seconds']>=0,'Actual root chronology')
 if expected_exit==1:
  require(src(prefix+'stdout')==b'','Original failed root stdout')
  error=src(prefix+'stderr')
  require(b'FileNotFoundError' in error and b'preparation_angle_moment_exposed_check/FREEZE.json' in error,'Original seal-lookup failure retained')
 else:
  require(src(prefix+'stderr')==b'','Actual successful root stderr')
  output=json.loads(src(prefix+'stdout'))
  require(output['scientific_executions']==0,'Root metadata was not science execution')
  for key in ['acceptance','qualifications','freeze']:identity(src(renewal_alias(output[key]['path'])),output[key])
 return r
def verify_review_record(src):
 folder='preparation_angle_moment_exposed_check/'
 r=json.loads(src(folder+'metadata_runs/source_capture/EXECUTION.json'))
 require(r['exit_code']==0 and r['timed_out'] is False,'Historical exposed-review metadata completion')
 require(len(r['argv'])==4 and r['argv'][1]=='-B' and r['argv'][2]==r['source_at_launch']['path'],'Original review capture argv')
 for key in ['source_original','source_at_launch','recorder_at_launch','stdout','stderr']:identity(src(renewal_alias(r[key]['path'])),r[key])
 require(r['source_original']['sha256']==r['source_at_launch']['sha256'],'Review executed-source linkage')
 require(src(folder+'metadata_runs/source_capture/stderr')==b'','Review metadata stderr')
 result=json.loads(src(folder+'RESULT.json'))
 require(result['scientific_executions']==0 and result['historical_replays']==0 and result['metadata_only'] is True,'Exposed review metadata scope')
 require(result['root_acceptance'] is None and result['canonical_integration'] is None and result['publication'] is None and result['retained_audit'] is False,'Historical reviewer nulls preserved')
 seal=json.loads(src(folder+'SEAL_OPERATION.json'))
 require(seal['process_exit'] is None,'Historical self-recorded seal does not invent process exit')
 return r

def verify_payload(read):
 raw=read(PACKET+'/INPUT_MANIFEST.json');require(digest(raw)==MANIFEST_SHA256,'Input manifest pin')
 manifest=json.loads(raw);require(manifest['schema']=='preparation_angle_moment_publication_inputs_v1','Input schema')
 rows=manifest['inputs'];paths=[r['path'] for r in rows]
 require(len(paths)==len(set(paths)) and set(AUDIT_INPUT_PATHS)==set(paths)|{PACKET+'/INPUT_MANIFEST.json'},'Exact declared input closure')
 for row in rows:identity(read(row['path']),row)
 note=read(NOTE);header=note.split(b'---',2)[1].decode().splitlines()
 for field in ['claim_type: bounded_theorem','actual_current_surface_status: conditional-support','canonical_parent_binding_complete: false','audit_required_before_effective_retained: true','bare_retained_allowed: false']:
  require(field in header,'Draft scope field '+field)
 require(b'Claim type: bounded_theorem.' in note,'Explicit prose claim type')
 maps=json.loads(read(PACKET+'/BODY_MAP.json'))['bodies']
 require({r['name']:r['sha256'] for r in maps}==EXPECTED_BODIES and len(maps)==3,'Three unchanged body roles')
 previous=-1
 for row in maps:
  a,b=row['start_byte_inclusive'],row['end_byte_exclusive']
  require(row['container']==NOTE and isinstance(a,int) and isinstance(b,int) and 0<=a<b<=len(note) and a>previous,'Ordered body interval')
  body=note[a:b];identity(body,row);require(note.count(body)==1,'Unique unchanged body');previous=b
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
 freezes=json.loads(read(PACKET+'/FROZEN_SOURCE_CLOSURE.json'))['roots']
 require({f['alias']:f['sha256'] for f in freezes}==EXPECTED_FREEZES and len(freezes)==3,'Exact bounded source freeze set')
 for f in freezes:
  raw=src(f['alias']);require(digest(raw)==f['sha256'],'Frozen source pin')
  members=json.loads(raw)[f['key']];require(len(members)==f['members'],'Freeze member count')
  for row in members:
   p=row['path'];key=renewal_alias(p) if PurePosixPath(p).is_absolute() else f['folder']+'/'+p
   identity(src(key),row)
 for row in maps:require(note[row['start_byte_inclusive']:row['end_byte_exclusive']]==src(row['source']),'Original body byte recovery')
 accepted=json.loads(src('preparation_angle_moment_root_review/ACCEPTANCE.json'))
 require(digest(src('preparation_angle_moment_root_review/ACCEPTANCE.json'))=='d32049fc5fe1f8ec166d333ace01e5b1738991e51773eebb5085eeff172ecec4','Actual source acceptance pin')
 require(accepted['disposition']=='QUALIFIED_CONDITIONAL_ANALYTICAL_SUPPORT' and accepted['root_read_complete'] is True,'Qualified source decision')
 require(accepted['scientific_executions']==0 and accepted['retained_audit'] is False and accepted['canonical_acceptance'] is None and accepted['publication'] is None,'Source acceptance limits')
 for key in ['candidate','candidate_freeze','exposed_review','review_freeze','controlling_qualifications','prior_failed_metadata_execution']:identity(src(renewal_alias(accepted[key]['path'])),accepted[key])
 require(renewal_alias(accepted['review_freeze']['path']).endswith('/FINAL_FREEZE.json'),'Actual reviewer seal filename')
 for name,(status,pin) in ROOT_RUNS.items():verify_root_record(src,name,status,pin)
 verify_review_record(src)
 parent=json.loads(read(PACKET+'/PARENT_BINDING.json'))
 require(parent['canonical_binding_complete'] is False and len(parent['direct_mathematical_parents'])==1,'Sole source parent; canonical binding pending')
 row=parent['direct_mathematical_parents'][0];identity(src(row['source_alias']),row)
 require(row['sha256']=='6db93809f12315668f720006c6a443301ad682381ce5629c173b1ff1c6d66a7f' and row['canonical_path']=='docs/LOCAL_CONSERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md','Exact direct preparation parent')
 exposure=json.loads(read(PACKET+'/EXPOSURE.json'))
 require(exposure['new_scientific_executions']==0 and exposure['historical_scientific_executions_for_result']==0 and exposure['blind_independence'] is False and exposure['source_exposed'] is True,'Honest exposure and scope')
 state=json.loads(read(PACKET+'/PUBLICATION_STATE.json'))
 require(all(state[k] is None for k in ['source_wrapper_review','source_publication_binding','canonical_integration','current_base_observation','canonical_review','primary_execution','publication_action','retained_audit']),'Unexecuted publication fields')
 require(state['scientific_programs_run_this_draft']==0 and state['scientific_replays']==0,'No draft scientific replay')
 binding=json.loads(read(PACKET+'/ACTUAL_BINDING.json'))
 require(binding['kind']=='unbound_source_only_proposal' and all(binding[k] is None for k in ['source_review','base_observation','canonical_review','canonical_parent_binding','publication']),'Unbound future contract')
 return {'note_sha256':digest(note),'body_count':len(maps),'source_aliases':len(sources),'archive_objects':len(archive),'historical_failed_root_metadata_runs':1,'historical_successful_root_metadata_runs':1,'science_executions':0}
def verify_actual_binding(read,checked):
 # Intentionally fail closed: root must review a separate bound integration version.
 raise ValueError('UNBOUND SOURCE-ONLY PROPOSAL: canonical source/base/parent/review execution evidence is pending')
def main():
 checked=verify_payload(disk_read);verify_actual_binding(disk_read,checked)
if __name__=='__main__':main()
