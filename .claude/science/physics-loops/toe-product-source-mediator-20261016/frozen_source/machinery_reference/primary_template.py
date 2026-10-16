"""Source-integrity only. No scientific runner, simulation or proof is executed."""
from pathlib import Path,PurePosixPath
import hashlib,json
REPO=Path(__file__).resolve().parents[1]
NOTE='docs/WEAK_MEDIATOR_FIXED_TARGET_BOUNDED_THEOREM_NOTE_2026-10-16.md'
PACKET='.claude/science/physics-loops/toe-weak-mediator-fixed-target-20261016'
AUDIT_TIMEOUT_SEC=60
AUDIT_INPUT_PATHS=__AUDIT_INPUT_PATHS__
MANIFEST_SHA256='__MANIFEST_SHA256__'
EXPECTED_BODIES=__EXPECTED_BODIES__
EXPECTED_FREEZES=__EXPECTED_FREEZES__
EXPECTED_ACCEPTANCES=__EXPECTED_ACCEPTANCES__
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
def verify_receipt(src,contract):
 r=json.loads(src(contract['alias']))
 require(r==contract['record'],'Exact heterogeneous original receipt, including recorded limits')
 start=r.get('start_utc',r.get('started_at'));end=r.get('end_utc',r.get('completed_at'))
 require(isinstance(start,str) and isinstance(end,str) and r['exit_code']==0 and start<end and r['elapsed_seconds']>=0,'Actual successful chronology')
 require(r.get('timeout',r.get('timed_out',False)) is False,'Original timeout state')
 require(renewal_alias(r['argv'][contract['argv_source_index']])==contract['executed_alias'],'Actually launched source path and argv position')
 require(r.get('cwd')==contract['recorded_cwd'] and ('cwd' not in r)==contract['cwd_missing_in_original_receipt'],'Do not invent absent historical cwd')
 original=src(contract['original_alias']);snapshot=src(contract['snapshot_alias'])
 require(original==snapshot and digest(original)==contract['source_sha256'],'Actual original and separately captured source bytes')
 for row in contract['files']:identity(src(row['alias']),row)
 folder=contract['alias'].rsplit('/',1)[0];schema=contract['schema']
 if schema=='legacy_metadata':
  require(digest(snapshot)==r['source_sha256'],'Legacy source hash field')
  for name in ['stdout','stderr']:require(digest(src(folder+'/'+name+'.txt'))==r[name+'_sha256'],'Legacy full stream hash')
 elif schema=='analytic_metadata':
  for field in ['child_source_at_launch','source_capture','recorder_source','stdout','stderr']:
   identity(src(renewal_alias(r[field]['path'])),r[field])
  require(r['child_source_unchanged'] is True,'Analytic metadata source unchanged')
  require(r.get('captured_source_matches',r.get('source_capture_bytes_match')) is True,'Captured source equality')
 elif schema in {'scientific_symbolic','scientific_compiler'}:
  require(r['scientific_launches']==1 and r['prelaunch_verified'] is True and r['source_unchanged'] is True,'One actual author execution per program')
  require(r['argv'][1:3]==['-I','-B'],'Isolated captured source launch')
  if schema=='scientific_symbolic':require(r['argv'][4:6]==['--inputs',r['executed_inputs']['path']],'Symbolic input supplied by argv')
  else:require(r['argv'][4]=='--output' and r['executed_inputs']['path'].endswith('/source_at_launch/PARAMETERS.json'),'Compiler fixed sibling parameters, not an invented argv input')
  require(r['wall_limit_seconds']==60 and r['cpu_quota'] is None and r['ram_quota'] is None,'Actual wall limit; no CPU/RAM quota')
  for field in ['original_source','executed_source','executed_inputs','go_record']:
   identity(src(renewal_alias(r[field]['path'])),r[field])
  identity(src(folder+'/PRELAUNCH_FREEZE_at_launch.json'),r['prelaunch_freeze'])
  for row in r['artifacts']:identity(src(folder+'/'+row['path']),row)
  recorder_row=next(x for x in r['artifacts'] if x['path']=='recorder_at_launch.py')
  identity(src(folder+'/recorder_at_launch.py'),recorder_row)
  require(r['executed_source_after']=={k:r['executed_source'][k] for k in ['bytes','sha256']},'Actual unchanged source after execution')
 elif schema=='root_review_run':
  for field in ['child_source_at_launch','source_capture','recorder','stdout','stderr']:
   identity(src(renewal_alias(r[field]['path'])),r[field])
  require(r['argv'][1]==r['child_source_at_launch']['path'],'Root actually launched original with separate capture')
 else:raise ValueError('Unexpected receipt schema')
 return r
def verify_payload(read):
 raw=read(PACKET+'/INPUT_MANIFEST.json');require(digest(raw)==MANIFEST_SHA256,'Input manifest pin')
 manifest=json.loads(raw);require(manifest['schema']=='weak_mediator_publication_inputs_v1','Input schema')
 rows=manifest['inputs'];paths=[r['path'] for r in rows]
 require(len(paths)==len(set(paths)) and set(AUDIT_INPUT_PATHS)==set(paths)|{PACKET+'/INPUT_MANIFEST.json'},'Exact declared input closure')
 for row in rows:identity(read(row['path']),row)
 note=read(NOTE);header=note.split(b'---',2)[1].decode().splitlines()
 for field in ['claim_type: bounded_theorem','actual_current_surface_status: conditional-support','source_science_acceptance_complete: true','canonical_parent_binding_complete: false','audit_required_before_effective_retained: true','bare_retained_allowed: false']:
  require(field in header,'Draft scope field '+field)
 require(b'Claim type: bounded_theorem.' in note,'Explicit prose claim type')
 require(b'**Primary runner:** `scripts/weak_mediator_fixed_target_2026_10_16.py`' in note,'Explicit primary runner label')
 maps=json.loads(read(PACKET+'/BODY_MAP.json'))['bodies']
 require({r['name']:r['sha256'] for r in maps}==EXPECTED_BODIES and len(maps)==12,'Twelve unchanged body roles')
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
 roots=json.loads(read(PACKET+'/FROZEN_SOURCE_CLOSURE.json'))['roots']
 require({f['alias']:f['sha256'] for f in roots}==EXPECTED_FREEZES,'Exact bounded frozen source roots')
 for f in roots:
  raw=src(f['alias']);require(digest(raw)==f['sha256'],'Actual frozen source identity')
  members=json.loads(raw)[f['key']];require(len(members)==f['members'],'Original freeze member count')
  table={r['path']:r for r in members};require(len(table)==len(members),'Unique original freeze members')
  require(set(f['selected_members'])==set(table) and f['complete_members'] is True,'Complete selected original inventories')
  for path in f['selected_members']:
   alias=renewal_alias(path) if path.startswith('/') else f['folder']+'/'+path
   require(f['member_aliases'][path]==alias and alias.startswith(f['folder']+'/'),'Literal original freeze paths normalized within root')
   identity(src(alias),table[path])
 for row in maps:require(note[row['start_byte_inclusive']:row['end_byte_exclusive']]==src(row['source']),'Original body recovery')
 contracts=json.loads(read(PACKET+'/EXECUTION_CONTRACTS.json'))['receipts']
 require(len(contracts)==10 and len({r['alias'] for r in contracts})==10,'Ten unique historical execution contracts')
 for contract in contracts:verify_receipt(src,contract)
 require(sum(c['schema'].startswith('scientific_') for c in contracts)==2,'Two distinct author scientific executions')
 additional=json.loads(read(PACKET+'/ADDITIONAL_EVIDENCE.json'))
 require(len(additional['records'])==3 and additional['root_acceptance_predates_this_arithmetic_check'] is True,'Separate additive evidence chronology')
 for item in additional['records']:
  r=json.loads(src(item['alias']));require(r==item['record'] and r['exit_code']==item['expected_exit_code'],'Preserve exact success and failure records')
  for row in item['files']:identity(src(row['alias']),row)
  if 'source_capture' in r:identity(src(renewal_alias(r['source_capture']['path'])),r['source_capture'])
  if 'scope' in r:
   require(r['started_at']<r['completed_at'] and r['source_unchanged'] is True,'Actual saved-check metadata chronology')
   identity(src(renewal_alias(r['source_capture']['path'])),r['child_source_at_launch'])
   for field in ['recorder_source','stdout','stderr']:identity(src(renewal_alias(r[field]['path'])),r[field])
   require(r['argv'][3]==r['child_source_at_launch']['path'],'Original metadata argv, failed source recovered from capture')
  else:
   require(digest(src(item['alias']))==additional['checker_receipt_sha256']=='73c9f6544f7530f3e8106b6f4f1dc523098e2bf107312bae88644bf8a88358a0','Actual separate checker receipt')
   require(r['scientific_launches']==r['maximum_attempts']==1 and r['timeout'] is False and r['error'] is None,'One completed saved-certificate check')
   require(r['launch_started_at']<r['launch_completed_at'] and r['elapsed_seconds']==0.07717579184100032,'Actual separate checker elapsed time')
   require(r['wall_limit_seconds']==60 and r['cpu_quota'] is None and r['ram_quota'] is None,'Checker actual limits')
   for field in ['original_source_at_launch','executed_source_at_launch','recorder_capture','recorder_source','report_capture','parameters_capture','root_go','root_go_capture','proposal_freeze']:
    identity(src(renewal_alias(r[field]['path'])),r[field])
   require(r['argv'][3]==r['executed_source_at_launch']['path'] and r['argv'][5]==r['report_capture']['path'] and r['argv'][7]==r['parameters_capture']['path'],'Checker captured argv')
   for row in r['artifacts']:identity(src(renewal_alias(row['path'])),row)
   result_raw=src('weak_mediator_saved_certificate_check_execution/runs/check_001/output/RESULT.json')
   require(digest(result_raw)==additional['checker_result_sha256']=='ea2b9b99c64e6e3eecadde5a9eec34a50a589afb26a0ce40f1e378d0dab3fdb5','Exact additive result')
   result=json.loads(result_raw)
   require(result['check_count']==429 and len(result['checks'])==429 and len(result['scenarios'])==2 and result['error'] is None,'Recorded arithmetic-check result only')
   require(result['author_compiler_imported_or_reexecuted'] is False and result['series_reconstructed'] is False,'Separate conditional endpoint check scope')
 acceptance_alias='weak_mediator_root_review/ACCEPTANCE.json'
 require(EXPECTED_ACCEPTANCES=={acceptance_alias:'ba201403a60d1c94751d1550f14d59622c86920ced74ebae21f5f51f5752731b'},'Exact actual root disposition')
 decision_raw=src(acceptance_alias);require(digest(decision_raw)==EXPECTED_ACCEPTANCES[acceptance_alias],'Actual root science decision pin')
 decision=json.loads(decision_raw)
 require(decision['status']=='QUALIFIED_CONDITIONAL_SOURCE_ACCEPTED_PUBLICATION_PENDING' and decision['retained_audit'] is False,'Qualified source decision only')
 require(decision['publication'] is None and decision['canonical_integration'] is None,'No publication or canonical binding invented')
 require(decision['source_exposed_checks'] is True and decision['blind_review'] is False,'Actual source exposure')
 identity(src(renewal_alias(decision['qualification']['path'])),decision['qualification'])
 root_receipt=json.loads(src('runs/weak_mediator_root_acceptance/EXECUTION.json'))
 root_output=json.loads(src(renewal_alias(root_receipt['stdout']['path'])))
 for key in ['acceptance','qualification','freeze']:identity(src(renewal_alias(root_output[key]['path'])),root_output[key])
 require(root_output['scientific_replays']==0,'Root acceptance metadata did not replay science')
 for row in decision['sources']:identity(src(renewal_alias(row['path'])),row)
 for row in decision['analytic_reviews']:
  for key in ['freeze','review','addendum_review']:
   if key in row:identity(src(renewal_alias(row[key]['path'])),row[key])
 for row in decision['actual_scientific_executions']:
  for key in ['receipt','output_freeze','report']:identity(src(renewal_alias(row[key]['path'])),row[key])
  r=json.loads(src(renewal_alias(row['receipt']['path'])));report=json.loads(src(renewal_alias(row['report']['path'])))
  require(r['elapsed_seconds']==row['elapsed_seconds'],'Actual author duration')
  require(report['source_sha256']==r['executed_source']['sha256'],'Report actual source binding')
  require(len(report['checks'])==row['checks'] and all(x['holds'] for x in report['checks']),'Recorded author assertions; no arithmetic replay')
 parent=json.loads(read(PACKET+'/PARENT_BINDING.json'))
 require(parent['canonical_binding_complete'] is False and parent['direct_mathematical_parents']==[] and parent['canonical_graph_disposition'] is None,'No invented dependency or graph disposition')
 require(parent['self_contained_conditional_root_theorem'] is True and parent['other_campaign_theorems_composed'] is False,'No other theorem composition')
 exposure=json.loads(read(PACKET+'/EXPOSURE.json'))
 require(exposure['new_scientific_executions']==0 and exposure['blind_independence'] is False and exposure['source_exposed'] is True,'Honest packaging exposure')
 require(exposure['historical_author_scientific_runs']==2 and exposure['independent_scientific_replications']==0,'Two author programs only')
 state=json.loads(read(PACKET+'/PUBLICATION_STATE.json'))
 require(all(state[k] is None for k in ['source_wrapper_review','source_publication_binding','canonical_integration','current_base_observation','canonical_review','staged_review','primary_execution','publication_action','retained_audit']),'Unexecuted publication fields')
 require(state['actual_scientific_source_acceptance']=={'source':acceptance_alias,'sha256':EXPECTED_ACCEPTANCES[acceptance_alias]},'Actual science acceptance distinguished from future approvals')
 require(state['scientific_programs_run_this_draft']==0 and state['scientific_replays']==0,'No packaging science replay')
 binding=json.loads(read(PACKET+'/ACTUAL_BINDING.json'))
 require(binding['kind']=='unbound_source_only_proposal' and all(binding[k] is None for k in ['source_review','base_observation','canonical_review','canonical_parent_binding','staged_review','publication']),'Unbound future contract')
 return {'note_sha256':digest(note),'body_count':len(maps),'source_aliases':len(sources),'archive_objects':len(archive),'original_receipts':len(contracts),'new_scientific_executions':0}
def verify_actual_binding(read,checked):
 # Intentionally fail closed: root must review a separate bound integration version.
 raise ValueError('UNBOUND SOURCE-ONLY PROPOSAL: canonical source/base/parent/review execution evidence is pending')
def main():
 checked=verify_payload(disk_read);verify_actual_binding(disk_read,checked)
if __name__=='__main__':main()
