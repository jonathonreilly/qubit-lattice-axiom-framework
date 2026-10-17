"""Source-integrity only. No scientific runner, simulation or proof is executed."""
from pathlib import Path,PurePosixPath
import hashlib,json
REPO=Path(__file__).resolve().parents[1]
NOTE='docs/POSITIVE_ONSITE_ENDPOINT_CHART_RECURRENCE_BOUNDED_THEOREM_NOTE_2026-10-16.md'
PACKET='.claude/science/physics-loops/toe-positive-onsite-endpoint-chart-recurrence-20261016'
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
 require(r['exit_code']==contract['exit_code'],'Original exit status preserved')
 require(r['argv']==contract['argv'],'Exact original full argv')
 require(r['start_utc']<r['end_utc'] and r['elapsed_seconds']>=0,'Actual execution chronology')
 if contract['schema']=='root_original_and_capture':
  original,capture,recorder='child_source_at_launch','source_capture','recorder'
  require(r['argv'][1]==r[original]['path'],'Root launched original source path')
 else:
  original=contract['original_key'];capture='source_at_launch';recorder='recorder_at_launch'
  require(r['argv'][contract['executed_argv_index']]==r[capture]['path'],'Actually launched captured source path')
  require(r['timed_out'] is False,'Original no-timeout status')
 require(r[original]['path']!=r[capture]['path'],'Original source and executed capture remain distinct')
 require(r[original]['sha256']==r[capture]['sha256']==contract['source_sha256'],'Original/executed source identity')
 require(r[original]['bytes']==r[capture]['bytes'],'Original/executed source length')
 require(renewal_alias(r[original]['path'])==contract['original_alias'],'Original source path identity')
 require(renewal_alias(r[capture]['path'])==contract['capture_alias'],'Actual capture path identity')
 for key in [original,capture,recorder,'stdout','stderr']:identity(src(renewal_alias(r[key]['path'])),r[key])
 for key in ['stdout','stderr']:
  require(r[key]['sha256']==contract[key+'_sha256'],'Complete original '+key+' identity')
 if 'wall_timeout_seconds' in contract:
  require(r['wall_timeout_seconds']==contract['wall_timeout_seconds'],'Actual original wall limit')
 if 'timeout_seconds' in contract:
  require(r['timeout_seconds']==contract['timeout_seconds'],'Actual original wall limit')
 return r
def verify_payload(read):
 raw=read(PACKET+'/INPUT_MANIFEST.json');require(digest(raw)==MANIFEST_SHA256,'Input manifest pin')
 manifest=json.loads(raw);require(manifest['schema']=='endpoint_chart_recurrence_publication_inputs_v1','Input schema')
 rows=manifest['inputs'];paths=[r['path'] for r in rows]
 require(len(paths)==len(set(paths)) and set(AUDIT_INPUT_PATHS)==set(paths)|{PACKET+'/INPUT_MANIFEST.json'},'Exact declared input closure')
 for row in rows:identity(read(row['path']),row)
 note=read(NOTE);header=note.split(b'---',2)[1].decode().splitlines()
 for field in ['claim_type: bounded_theorem','actual_current_surface_status: conditional-support','canonical_parent_binding_complete: false','audit_required_before_effective_retained: true','bare_retained_allowed: false']:
  require(field in header,'Draft scope field '+field)
 require(b'Claim type: bounded_theorem.' in note,'Explicit prose claim type')
 require(b'**Primary runner:** `scripts/positive_onsite_endpoint_chart_recurrence_2026_10_16.py`' in note,'Explicit primary runner label')
 maps=json.loads(read(PACKET+'/BODY_MAP.json'))['bodies']
 require({r['name']:r['sha256'] for r in maps}==EXPECTED_BODIES and len(maps)==9,'Nine unchanged body roles')
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
  members=json.loads(raw)['members'];require(len(members)==f['members'],'Original freeze member count')
  table={r['path']:r for r in members};require(len(table)==len(members),'Unique original freeze members')
  require(set(f['selected_members'])<=set(table),'Selected source membership')
  if f['complete_members']:require(set(f['selected_members'])==set(table),'Complete candidate/root closure')
  for path in f['selected_members']:identity(src(f['folder']+'/'+path),table[path])
 for row in maps:require(note[row['start_byte_inclusive']:row['end_byte_exclusive']]==src(row['source']),'Original body recovery')
 contracts=json.loads(read(PACKET+'/EXECUTION_CONTRACTS.json'))['receipts']
 require(len({r['alias'] for r in contracts})==len(contracts),'Unique original receipt contracts')
 for contract in contracts:verify_receipt(src,contract)
 for alias,sha in EXPECTED_ACCEPTANCES.items():
  raw=src(alias);require(digest(raw)==sha,'Actual root science decision pin')
  decision=json.loads(raw)
  require(decision['root_read_complete'] is True and decision['retained_audit'] is False,'Qualified source decision only')
  require(decision['canonical_binding'] is None and decision['publication'] is None,'Original source decision nulls')
  q=decision['controlling_qualifications'];identity(src(renewal_alias(q['path'])),q)
 parent=json.loads(read(PACKET+'/PARENT_BINDING.json'))
 require(parent['canonical_binding_complete'] is False and parent['direct_mathematical_parents']==[],'No direct canonical mathematical parents; future binding unset')
 exposure=json.loads(read(PACKET+'/EXPOSURE.json'))
 require(exposure['new_scientific_executions']==0 and exposure['blind_independence'] is False and exposure['source_exposed'] is True,'Honest packaging exposure')
 require(exposure['second_ODE_implementation'] is False,'No independent ODE claim')
 state=json.loads(read(PACKET+'/PUBLICATION_STATE.json'))
 require(all(state[k] is None for k in ['source_wrapper_review','source_publication_binding','canonical_integration','current_base_observation','canonical_review','primary_execution','publication_action','retained_audit']),'Unexecuted publication fields')
 require(state['scientific_programs_run_this_draft']==0 and state['scientific_replays']==0,'No packaging science replay')
 binding=json.loads(read(PACKET+'/ACTUAL_BINDING.json'))
 require(binding['kind']=='unbound_source_only_proposal' and all(binding[k] is None for k in ['source_review','base_observation','canonical_review','canonical_parent_binding','publication']),'Unbound future contract')
 return {'note_sha256':digest(note),'body_count':len(maps),'source_aliases':len(sources),'archive_objects':len(archive),'original_receipts':len(contracts),'new_scientific_executions':0}
def verify_actual_binding(read,checked):
 # Intentionally fail closed: root must review a separate bound integration version.
 raise ValueError('UNBOUND SOURCE-ONLY PROPOSAL: canonical source/base/parent/review execution evidence is pending')
def main():
 checked=verify_payload(disk_read);verify_actual_binding(disk_read,checked)
if __name__=='__main__':main()
