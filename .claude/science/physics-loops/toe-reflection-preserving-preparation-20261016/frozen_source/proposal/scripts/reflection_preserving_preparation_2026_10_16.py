"""Source-integrity only. No scientific runner, simulation or proof is executed."""
from pathlib import Path,PurePosixPath
import hashlib,json
REPO=Path(__file__).resolve().parents[1]
NOTE='docs/REFLECTION_PRESERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md'
PACKET='.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016'
AUDIT_TIMEOUT_SEC=60
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/ACCEPTANCE_BINDING.json', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/BINDING_CONTRACT.md', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/BODY_MAP.json', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/EXPOSURE.json', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/FROZEN_SOURCE_CLOSURE.json', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/PARENT_BINDING.json', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/PARENT_PUBLICATION_EVIDENCE.json', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/PR_BODY.md', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/009bfbd7dbe5cb8295d26c1898bd911c484af95c024a029e45eb9b6219389956', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/04a27f9a415b269bddd7a38f1e85d99375950313a95cd5bb95c94c8c7297ebf5', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/0c85e9294e4f8c93bc12cde5788e64051916a10612b939b66b280e6d6dddf153', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/131ef659b79ee205e008b4535de6ec5764ce78b9f1444659b13b6b8d0c56f0f8', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/1b3bab5e75e68ee26be2145b21803d556aeb2bb967e68d560b9abbbd5ab523cb', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/1c727dade021ef194f8b017d3304fae9e07689ca32ca8bfad367286212b7f2b5', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/21f090292f0fbd212e9409abcaced9416238dbe762811cda8e1b1fe3a4ba0de4', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/241dbcc2a6f4715df2ef322b4007ad816f954867b1ce47c1d4c61e71517a7388', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/280d0564306f548990b0a342a45676d331997539ff3cd59f7809f8671a281b68', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/2906985b3fc20e92da279462656010f378600d84ffc6346778e1ee6cccf96996', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/2fa9804e93e1daeebf5e666f830bc8230610c712dcb0586b0b5513513d3f4a0c', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/30514c0378008ca91bd11c683b64fb4d578c6667291020dc439d0e41ae9bc3fa', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/3149e0e46fc9a3a264c87282dc25e616222de6078039bfde628d3f8ffc774635', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/3a60172dfe24d5d99faf459e25bc483bcddf6813f6c6efbf6d304d42ff2b3418', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/3f7c8d6234fc0ec1fcf7a9b41959fbe0284d4f03820f32a56acfb147367a0192', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/4474c5cd6f9707e4bf761bf361b67b2e9ea1e9ca2dd2b489c23ab0ecd3aa2438', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/45da91b6224d2fdd569a26e84a712ab0eeba1280bbe0f2362fdd391f9eb24831', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/57321af50a72e48242cd59558edc811795a2001c44dfcd74d466a4c42d60aeff', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/58028fb9788df81db5bafcb45520a997c3891b6e659e5ddeb7b60ca60aed87d0', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/5ba89f88975389dbc6367e930baa023fc51743d3b0227836d9e33384fa18789a', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/632bb16673ca052812ed53817ec1f6115ee23dc89e9516f8910c0860d2c754e0', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/6ce29058d8c30ac399d3c14271331026fc8c150b04c7e55f68e44832d4cbb0ae', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/6db93809f12315668f720006c6a443301ad682381ce5629c173b1ff1c6d66a7f', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/6f6d0f69ae32b84e6c5a01d0aaebbc4eb3e4d7cc81e0adfa53362100952a00f7', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/6fc70e269a55d0f13e63416cb0ce4d1e600d1509c2753ab2db9c2d44a402fde1', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/6ffea8e98853e6b921156b50a64320ffe2370da3ecea7603a4979e970fc3895d', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/7262d9cc214a977cb42e60a274eb5a121c1f6b20a0578d11d40fe653918cd87f', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/78264339d502a05e77b22633decf380e7e095a97dd070c7ae33b208c7490e6f0', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/7a85a100cc613d964ae3d69474a3cfd51ae61123d62c13d183eeea504324df01', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/8388e3d6521cd39a7d7d0c142bd2b63eea3161488132136acdb6dea273f0d76d', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/8a7052c02977aa51fd6daf9b4d485d4ca2504eb92ba623c88ee603a634edb61d', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/97570aecc29faf3dc3aba4228622cd1ea7565b01b7a3bfaae6943e9ba0e45735', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/9e28d4418c7e5711d048424875cbbd45619c16d6429cfcb894fd5907c455a5dd', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/ae215d02125323414a34dd295d7d8036ac43c9a7193559fc61bc731304477370', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/b2161150997749c72ad1e0867a4fcf519ebdbfa07bd526d1faa552eb1f567428', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/c0fc236512c4b57b10a27edcbccc824e83112b9e6c8e195a89ed2511c017d827', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/c351118e54d43eb2ba195b18041dc0af76666b530cd037a07052d6f4965a1b4d', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/cb70b1595b99f441445a78e62370f801725ff056f02369912a1590b92a68d07e', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/d32049fc5fe1f8ec166d333ace01e5b1738991e51773eebb5085eeff172ecec4', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/da73cc0766a3dc37da3d9d76e8f138fd0e0e51f5faaa2da4bb973875857caaed', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/dc4838051396e454d6fdccc6c9d3cd6df8b87a3ffdc7ffcd7d0924e8e44fe9b5', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/dc551736d3aeac18fdf945d21373c4d89a1453929323de0a0d76b5c349d03076', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/ddb52f94cb711d5cdea1271dec89a1e1b22002d055d89676c3f94cec01dc13aa', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/e66487255904aa97e24e27a9643c14a128c9188e2153d56142347b86eea1e724', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/e73667146d03703fd50a68859c6133f93c0f78e81b3c0f1ed61c48ccde09cedf', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/f04cc82e9111e353d0b561b5fb5de145f4d3cd07ccd75c45a627fbb20b1498b5', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/archive/sha256/fd847fb098e1fa15f13a309065e99065128c2be6adaf2a6c336c3a38e5a9aced', 'docs/REFLECTION_PRESERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md', '.claude/science/physics-loops/toe-reflection-preserving-preparation-20261016/INPUT_MANIFEST.json']
MANIFEST_SHA256='abe2beea9806371f92fe866711806d1fbb8bc338ab6d22fb2f8a4e1abd145cdf'
EXPECTED_BODIES={'original_proposal': '9e28d4418c7e5711d048424875cbbd45619c16d6429cfcb894fd5907c455a5dd', 'complete_exposed_review': '7a85a100cc613d964ae3d69474a3cfd51ae61123d62c13d183eeea504324df01', 'current_controlling_qualifications': '4474c5cd6f9707e4bf761bf361b67b2e9ea1e9ca2dd2b489c23ab0ecd3aa2438'}
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
