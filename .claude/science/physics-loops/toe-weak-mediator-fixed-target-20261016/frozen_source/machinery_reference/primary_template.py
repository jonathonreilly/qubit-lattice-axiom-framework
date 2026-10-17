"""Source-integrity only. No scientific runner, simulation or proof is executed."""
from pathlib import Path,PurePosixPath
import hashlib,json
REPO=Path(__file__).resolve().parents[1]
NOTE='docs/COMMUTING_STATIC_EDGE_FIXED_TARGET_BOUNDED_THEOREM_NOTE_2026-10-16.md'
PACKET='.claude/science/physics-loops/toe-commuting-static-edge-fixed-target-20261016'
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
 require(r==contract['record'],'Exact heterogeneous original receipt, including all recorded limits')
 require(r['exit_code']==0 and r['start_utc']<r['end_utc'] and r['elapsed_seconds']>=0,'Actual successful chronology')
 require(r.get('timeout',r.get('timed_out',False)) is False,'Original timeout state')
 require(renewal_alias(r['argv'][contract['argv_source_index']])==contract['executed_alias'],'Actually launched source path and argv position')
 require(r.get('cwd')==contract['recorded_cwd'] and ('cwd' not in r)==contract['cwd_missing_in_original_receipt'],'Do not fabricate absent historical cwd')
 original=src(contract['original_alias']);snapshot=src(contract['snapshot_alias'])
 require(original==snapshot and digest(original)==contract['source_sha256'],'Actual original and separately captured source bytes')
 for row in contract['files']:identity(src(row['alias']),row)
 folder=contract['alias'].rsplit('/',1)[0];schema=contract['schema']
 if schema=='legacy_metadata':
  require(digest(snapshot)==r['source_sha256'],'Legacy source hash field')
  for name in ['stdout','stderr']:require(digest(src(folder+'/'+name+'.txt'))==r[name+'_sha256'],'Legacy full stream hash')
 elif schema in {'initial_metadata','captured_metadata'}:
  for field in ['source_at_launch','recorder_at_launch','stdout','stderr']:
   identity(src(renewal_alias(r[field]['path'])),r[field])
  require(r['source_unchanged_during_run'] is True,'Metadata source unchanged during actual run')
 elif schema=='scientific_edge':
  require(r['scientific_launches']==1 and r['prelaunch_verified'] is True and r['source_unchanged'] is True,'Exactly one actual author fixture')
  require(r['argv'][1:3]==['-I','-B'] and r['argv'][5]==r['executed_inputs']['path'],'Captured isolated source and input argv')
  require(r['wall_limit_seconds']==60 and r['cpu_quota'] is None and r['ram_quota'] is None,'Actual wall limit; no CPU/RAM quota')
  for field in ['original_source','executed_source','executed_inputs','go_record']:
   identity(src(renewal_alias(r[field]['path'])),r[field])
  identity(src(folder+'/recorder_at_launch.py'),r['recorder_source'])
  for row in r['artifacts']:identity(src(folder+'/'+row['path']),row)
  for name in ['stdout','stderr']:identity(src(folder+'/'+name+'.txt'),r[name])
 elif schema=='root_review_run':
  for field in ['child_source_at_launch','source_capture','recorder','stdout','stderr']:
   identity(src(renewal_alias(r[field]['path'])),r[field])
  require(r['argv'][1]==r['child_source_at_launch']['path'],'Root actually launched original with separate capture')
 else:raise ValueError('Unexpected receipt schema')
 return r
def verify_payload(read):
 raw=read(PACKET+'/INPUT_MANIFEST.json');require(digest(raw)==MANIFEST_SHA256,'Input manifest pin')
 manifest=json.loads(raw);require(manifest['schema']=='commuting_static_edge_publication_inputs_v1','Input schema')
 rows=manifest['inputs'];paths=[r['path'] for r in rows]
 require(len(paths)==len(set(paths)) and set(AUDIT_INPUT_PATHS)==set(paths)|{PACKET+'/INPUT_MANIFEST.json'},'Exact declared input closure')
 for row in rows:identity(read(row['path']),row)
 note=read(NOTE);header=note.split(b'---',2)[1].decode().splitlines()
 for field in ['claim_type: bounded_theorem','actual_current_surface_status: conditional-support','source_science_acceptance_complete: true','canonical_parent_binding_complete: false','audit_required_before_effective_retained: true','bare_retained_allowed: false']:
  require(field in header,'Draft scope field '+field)
 require(b'Claim type: bounded_theorem.' in note,'Explicit prose claim type')
 require(b'**Primary runner:** `scripts/commuting_static_edge_fixed_target_2026_10_16.py`' in note,'Explicit primary runner label')
 maps=json.loads(read(PACKET+'/BODY_MAP.json'))['bodies']
 require({r['name']:r['sha256'] for r in maps}==EXPECTED_BODIES and len(maps)==5,'Five unchanged body roles')
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
  for path in f['selected_members']:identity(src(f['folder']+'/'+path),table[path])
 for row in maps:require(note[row['start_byte_inclusive']:row['end_byte_exclusive']]==src(row['source']),'Original body recovery')
 require(read(PACKET+'/NO_GO_DISCIPLINE_CHECKLIST.md')==src('commuting_target_static_edge_exposed_check/author_cross_review/NO_GO_DISCIPLINE_CHECKLIST.md'),'Complete unchanged negative sidecar')
 contracts=json.loads(read(PACKET+'/EXECUTION_CONTRACTS.json'))['receipts']
 require(len(contracts)==6 and len({r['alias'] for r in contracts})==6,'Six unique historical execution contracts')
 for contract in contracts:verify_receipt(src,contract)
 require(sum(c['schema']=='scientific_edge' for c in contracts)==1,'One historical scientific execution, no duplicate alias counting')
 acceptance_alias='commuting_static_edge_root_review/ACCEPTANCE.json'
 require(EXPECTED_ACCEPTANCES=={acceptance_alias:'f954c36d04380ee49edac71a5dd7cb10e31142d3f3ca03f4da71f5609c04446b'},'Exact actual positive disposition')
 decision_raw=src(acceptance_alias);require(digest(decision_raw)==EXPECTED_ACCEPTANCES[acceptance_alias],'Actual root science decision pin')
 decision=json.loads(decision_raw)
 require(decision['root_complete_argument_and_checker_source_read'] is True and decision['retained_audit'] is False,'Qualified source decision only')
 require(decision['actual_publication'] is None and decision['independent_scientific_executions']==0,'No publication or independent fixture invented')
 require(decision['disposition']=='accept_conditional_positive_supplied_edge_for_regular_review; preserve_negative_N1_FAIL_partial_attempt','Positive/negative dispositions kept separate')
 for field in ['qualifications','actual_scientific_execution','actual_report']:
  identity(src(renewal_alias(decision[field]['path'])),decision[field])
 root_receipt=json.loads(src('runs/static_edge_root_acceptance/EXECUTION.json'))
 actual_root_output=json.loads(src(renewal_alias(root_receipt['stdout']['path'])))
 identity(decision_raw,actual_root_output['acceptance'])
 identity(src('commuting_static_edge_root_review/FREEZE.json'),actual_root_output['freeze'])
 fixture=json.loads(src('commuting_static_edge_check_proposal/runs/edge_001/EXECUTION.json'))
 require(fixture['elapsed_seconds']==0.18528820807114244,'Preserve actual author elapsed time')
 report=json.loads(src('commuting_static_edge_check_proposal/runs/edge_001/output/REPORT.json'))
 require(report['source_sha256']==fixture['executed_source']['sha256'] and report['input_sha256']==fixture['executed_inputs']['sha256'],'Report actual source/input bindings')
 require(len(report['checks'])==60 and all(r['holds'] for r in report['checks']),'Recorded assertions only, no arithmetic replay')
 require(report['arithmetic_statistics']=={'maximum_integer_bits':16241,'rational_operations':38343,'integer_operations':115492},'Actual whole-run statistics')
 require(report['computed']['coefficient_stage_arithmetic_statistics']['rational_operations']==127,'Coefficient count is not whole-run count')
 require(len(report['analytic_premises_not_computed'])==7,'Analytic-premise boundary preserved')
 parent=json.loads(read(PACKET+'/PARENT_BINDING.json'))
 require(parent['canonical_binding_complete'] is False and parent['direct_mathematical_parents']==[] and parent['canonical_graph_disposition'] is None,'No invented dependency or graph disposition')
 require(parent['prior_target_theorem_is_context_only'] is True and parent['mediator_proposal_composed'] is False,'No unrequested theorem composition')
 negative=json.loads(read(PACKET+'/NO_GO_STATUS.json'))
 require(negative['packet_status']==negative['N1']=='FAIL' and negative['disposition']=='partial-attempt-with-named-untested-routes','Negative packet remains N1FAIL partial')
 exposure=json.loads(read(PACKET+'/EXPOSURE.json'))
 require(exposure['new_scientific_executions']==0 and exposure['blind_independence'] is False and exposure['source_exposed'] is True,'Honest packaging exposure')
 require(exposure['historical_author_scientific_runs']==1 and exposure['independent_scientific_replications']==0,'Single author fixture only')
 state=json.loads(read(PACKET+'/PUBLICATION_STATE.json'))
 require(all(state[k] is None for k in ['source_wrapper_review','source_publication_binding','canonical_integration','current_base_observation','canonical_review','staged_review','primary_execution','publication_action','retained_audit']),'Unexecuted publication fields')
 require(state['actual_scientific_source_acceptance']=={'source':acceptance_alias,'sha256':EXPECTED_ACCEPTANCES[acceptance_alias]},'Actual science acceptance distinguished from future approvals')
 require(state['scientific_programs_run_this_draft']==0 and state['scientific_replays']==0,'No packaging science replay')
 binding=json.loads(read(PACKET+'/ACTUAL_BINDING.json'))
 require(binding['kind']=='unbound_source_only_proposal' and all(binding[k] is None for k in ['source_review','base_observation','canonical_review','canonical_parent_binding','staged_review','publication']),'Unbound future contract')
 return {'note_sha256':digest(note),'body_count':len(maps),'source_aliases':len(sources),'archive_objects':len(archive),'original_receipts':len(contracts),'new_scientific_executions':0,'negative_packet_status':'N1FAIL'}
def verify_actual_binding(read,checked):
 # Intentionally fail closed: root must review a separate bound integration version.
 raise ValueError('UNBOUND SOURCE-ONLY PROPOSAL: canonical source/base/parent/review execution evidence is pending')
def main():
 checked=verify_payload(disk_read);verify_actual_binding(disk_read,checked)
if __name__=='__main__':main()
