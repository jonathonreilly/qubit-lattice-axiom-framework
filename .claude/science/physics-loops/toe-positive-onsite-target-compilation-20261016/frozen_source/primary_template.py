"""Source-integrity only. No scientific runner, simulation or proof is executed."""
from pathlib import Path,PurePosixPath
import hashlib,json
REPO=Path(__file__).resolve().parents[1]
NOTE='docs/POSITIVE_ONSITE_TARGET_COMPILATION_BOUNDED_THEOREM_NOTE_2026-10-16.md'
PACKET='.claude/science/physics-loops/toe-positive-onsite-target-compilation-20261016'
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
 require(r['argv']==contract['argv'] and r['cwd']==contract['cwd'],'Exact original full argv and cwd')
 for key,value in contract['temporal_and_limits'].items():require(r[key]==value,'Original chronology, status and limits')
 start=r.get('start_utc',r.get('started_utc'));end=r.get('end_utc',r.get('finished_utc'))
 require(start<end and r['elapsed_seconds']>=0,'Actual execution chronology')
 original,capture=contract['original_key'],contract['capture_key']
 require(r['argv'][contract['executed_argv_index']]==r[contract['executed_key']]['path'],'Actually launched original or captured path')
 require(r[original]['path']!=r[capture]['path'],'Original source and separate snapshot remain distinct')
 require(r[original]['sha256']==r[capture]['sha256']==contract['source_sha256'],'Original and captured source identity')
 require(r[original]['bytes']==r[capture]['bytes'],'Original and captured source length')
 for key,alias in contract['field_aliases'].items():
  require(r[key]==contract['field_pins'][key],'Exact recorded field identity')
  identity(src(alias),r[key])
 return r
def verify_payload(read):
 raw=read(PACKET+'/INPUT_MANIFEST.json');require(digest(raw)==MANIFEST_SHA256,'Input manifest pin')
 manifest=json.loads(raw);require(manifest['schema']=='endpoint_target_compilation_publication_inputs_v1','Input schema')
 rows=manifest['inputs'];paths=[r['path'] for r in rows]
 require(len(paths)==len(set(paths)) and set(AUDIT_INPUT_PATHS)==set(paths)|{PACKET+'/INPUT_MANIFEST.json'},'Exact declared input closure')
 for row in rows:identity(read(row['path']),row)
 note=read(NOTE);header=note.split(b'---',2)[1].decode().splitlines()
 for field in ['claim_type: bounded_theorem','actual_current_surface_status: conditional-support','canonical_parent_binding_complete: false','audit_required_before_effective_retained: true','bare_retained_allowed: false']:
  require(field in header,'Draft scope field '+field)
 require(b'Claim type: bounded_theorem.' in note,'Explicit prose claim type')
 require(b'**Primary runner:** `scripts/positive_onsite_target_compilation_2026_10_16.py`' in note,'Explicit primary runner label')
 maps=json.loads(read(PACKET+'/BODY_MAP.json'))['bodies']
 require({r['name']:r['sha256'] for r in maps}==EXPECTED_BODIES and len(maps)==6,'Six unchanged body roles')
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
 author=json.loads(src('endpoint_target_compilation_candidate/runs/target_001/EXECUTION.json'))
 checker=json.loads(src('endpoint_target_compilation_exposed_check/saved_arithmetic_001/EXECUTION.json'))
 require(author['exit_code']==checker['exit_code']==0 and author['timed_out'] is checker['timed_out'] is False,'Original successful single scientific runs')
 require(author['elapsed_seconds']==461.2228046669625 and author['wall_timeout_seconds']==600,'Actual author process limits')
 require(checker['elapsed_seconds']==10.38794649997726 and checker['wall_timeout_seconds']==180,'Actual checker process limits')
 failed=json.loads(src('runs/endpoint_target_acceptance/EXECUTION.json'));corrected=json.loads(src('runs/endpoint_target_acceptance_correct_schema/EXECUTION.json'))
 require(failed['exit_code']==1 and corrected['exit_code']==0,'Preserved failed root metadata and distinct successful correction')
 require(b"KeyError: 'members'" in src(renewal_alias(failed['stderr']['path'])),'Exact initial schema failure remains')
 successful=json.loads(src(renewal_alias(corrected['stdout']['path'])))
 identity(src('endpoint_target_compilation_root_review/ACCEPTANCE.json'),successful['acceptance'])
 parent=json.loads(read(PACKET+'/PARENT_BINDING.json'))
 require(parent['canonical_binding_complete'] is False and len(parent['direct_mathematical_parents'])==1,'One mathematical parent; canonical binding remains pending')
 parent_row=parent['direct_mathematical_parents'][0]
 require(parent_row['path']=='docs/POSITIVE_ONSITE_ENDPOINT_CHART_RECURRENCE_BOUNDED_THEOREM_NOTE_2026-10-16.md' and parent_row['sha256']=='ab8fd20fb48aae14c9ae22df2b38de97755d717131195d0d4ad25f7236d475a8','Exact sole chart/recurrence parent')
 identity(src(parent_row['source_alias']),parent_row)
 require(parent['intended_graph_delta']=={'new_roots':0,'direct_edges':1},'One parent edge, no new root')
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
