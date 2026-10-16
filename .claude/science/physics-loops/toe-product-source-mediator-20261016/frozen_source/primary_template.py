"""Source-integrity only. No scientific runner, simulation or proof is executed."""
from pathlib import Path,PurePosixPath
import hashlib,json
REPO=Path(__file__).resolve().parents[1]
NOTE='docs/PRODUCT_SOURCE_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-16.md'
PACKET='.claude/science/physics-loops/toe-product-source-mediator-20261016'
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
 require(r==contract['record'],'Exact original receipt including actual absent fields')
 start=r.get('start_utc',r.get('started_at'));end=r.get('end_utc',r.get('finished_at'))
 require(isinstance(start,str) and isinstance(end,str) and start<end and r['elapsed_seconds']>=0 and r['exit_code']==0,'Actual successful chronology')
 require(renewal_alias(r['argv'][contract['argv_source_index']])==contract['original_alias']==contract['executed_alias'],'Original source was actually launched, not its separate capture')
 require(r.get('cwd')==contract['recorded_cwd'] and ('cwd' not in r)==contract['cwd_missing_in_original_receipt'],'Literal historical cwd')
 original=src(contract['original_alias']);snapshot=src(contract['snapshot_alias'])
 require(original==snapshot and digest(original)==contract['source_sha256'],'Original and separately captured source bytes')
 for row in contract['files']:identity(src(row['alias']),row)
 folder=contract['alias'].rsplit('/',1)[0]
 if contract['schema']=='product_review_metadata':
  require(r['argv'][1]=='-B' and r['timeout_seconds']==30 and r['timed_out'] is False,'Actual bounded metadata launch')
  require(r['scientific_executions']==0 and r['source_unchanged_during_run'] is True,'Metadata only and unchanged source')
  require(digest(snapshot)==r['source_sha256'],'Original recorded source hash')
  require(digest(src(folder+'/launcher_source.py'))==r['launcher_sha256'],'Actual launcher copy')
  require('stdout' not in r and 'stderr' not in r and contract['stream_hashes_added_by_archive_not_original_receipt'] is True,'Do not invent original stream-hash fields')
  require(src(folder+'/stderr')==b'','Complete original empty stderr')
 elif contract['schema']=='root_review_run':
  for field in ['child_source_at_launch','source_capture','recorder','stdout','stderr']:
   identity(src(renewal_alias(r[field]['path'])),r[field])
  require(r['argv'][1]==r['child_source_at_launch']['path'],'Root original-source argv')
  require('timeout_seconds' not in r and 'timed_out' not in r,'No invented root metadata timeout')
 else:raise ValueError('Unexpected receipt schema')
 return r
def verify_payload(read):
 raw=read(PACKET+'/INPUT_MANIFEST.json');require(digest(raw)==MANIFEST_SHA256,'Input manifest pin')
 manifest=json.loads(raw);require(manifest['schema']=='product_source_mediator_publication_inputs_v1','Input schema')
 rows=manifest['inputs'];paths=[r['path'] for r in rows]
 require(len(paths)==len(set(paths)) and set(AUDIT_INPUT_PATHS)==set(paths)|{PACKET+'/INPUT_MANIFEST.json'},'Exact declared input closure')
 for row in rows:identity(read(row['path']),row)
 note=read(NOTE);header=note.split(b'---',2)[1].decode().splitlines()
 for field in ['claim_type: bounded_theorem','actual_current_surface_status: conditional-support','source_science_acceptance_complete: true','canonical_parent_binding_complete: false','audit_required_before_effective_retained: true','bare_retained_allowed: false']:
  require(field in header,'Draft scope field '+field)
 require(b'Claim type: bounded_theorem.' in note,'Explicit prose claim type')
 require(b'**Primary runner:** `scripts/product_source_mediator_2026_10_16.py`' in note,'Explicit provenance-primary label')
 maps=json.loads(read(PACKET+'/BODY_MAP.json'))['bodies']
 require({r['name']:r['sha256'] for r in maps}==EXPECTED_BODIES and len(maps)==len(EXPECTED_BODIES),'Exact unchanged body roles')
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
   require(f['member_aliases'][path]==alias and alias.startswith(f['folder']+'/'),'Literal source members within root')
   identity(src(alias),table[path])
 for row in maps:require(note[row['start_byte_inclusive']:row['end_byte_exclusive']]==src(row['source']),'Original body recovery')
 contracts=json.loads(read(PACKET+'/EXECUTION_CONTRACTS.json'))['receipts']
 require(len({r['alias'] for r in contracts})==len(contracts),'Unique original execution records')
 require(sum(c['schema']=='product_review_metadata' for c in contracts)==3 and sum(c['schema']=='root_review_run' for c in contracts)==2,'Three original review metadata runs and two root decision runs')
 for contract in contracts:verify_receipt(src,contract)
 for alias,h in EXPECTED_ACCEPTANCES.items():
  raw=src(alias);require(digest(raw)==h,'Actual root decision pin');decision=json.loads(raw)
  expected_status='QUALIFIED_CONDITIONAL_ADDENDUM_ACCEPTED_PUBLICATION_PENDING' if alias.startswith('product_source_mediator_pauli_root_review/') else 'QUALIFIED_CONDITIONAL_SOURCE_ACCEPTED_PUBLICATION_PENDING'
  require(decision['status']==expected_status,'Actual qualified source/addendum status')
  require(decision['retained_audit'] is False and decision['scientific_executions']==0,'Analytical source acceptance, no audit or science execution')
  require(decision['publication'] is None and decision['canonical_integration'] is None,'No canonical/publication invention')
  require(decision.get('source_exposed_checks',decision.get('source_exposed')) is True and decision['blind_review'] is False,'Actual exposure')
  identity(src(renewal_alias(decision['qualification']['path'])),decision['qualification'])
  for row in decision.get('sources',[]):identity(src(renewal_alias(row['path'])),row)
  for key in ['source','review','review_freeze','metadata_execution','prior_acceptance']:
   if key in decision:identity(src(renewal_alias(decision[key]['path'])),decision[key])
  for review in decision.get('analytic_reviews',[]):
   for key in ['freeze','review','execution','stdout','stderr','separate_source_capture']:
    identity(src(renewal_alias(review[key]['path'])),review[key])
   require(review['scientific_executions']==0,'No scientific execution invented from a review')
   require(renewal_alias(review['actual_original_launched']) in recovered,'Recorded original launched source retained')
 for folder in ['runs/product_source_root_acceptance','runs/product_pauli_root_acceptance']:
  root_receipt=json.loads(src(folder+'/EXECUTION.json'))
  root_output=json.loads(src(renewal_alias(root_receipt['stdout']['path'])))
  for key in ['acceptance','qualification','freeze']:identity(src(renewal_alias(root_output[key]['path'])),root_output[key])
  require(root_output['scientific_executions']==0,'Root decision recording scope')
 parent=json.loads(read(PACKET+'/PARENT_BINDING.json'))
 require(parent['canonical_binding_complete'] is False and parent['canonical_graph_disposition'] is None,'Parent canonical/graph binding remains pending')
 require(len(parent['direct_mathematical_parents'])==1,'One mathematical parent')
 p=parent['direct_mathematical_parents'][0]
 require(p['note']=='docs/WEAK_MEDIATOR_FIXED_TARGET_BOUNDED_THEOREM_NOTE_2026-10-16.md' and p['canonical_sha256'] is None and p['parent_publication_binding'] is None,'Exact proposed parent name; no guessed finalized pin')
 require(p['physical_Bell_permissions_imported'] is False and parent['product_cannot_be_retroactive_parent_of_weak_mediator'] is True,'Only mathematical machinery composes')
 for alias in p['source_aliases']:src(alias)
 exposure=json.loads(read(PACKET+'/EXPOSURE.json'))
 require(exposure['source_exposed'] is True and exposure['blind_independence'] is False,'Honest source exposure')
 require(all(exposure[k]==0 for k in ['new_scientific_executions','historical_scientific_replays','historical_product_scientific_runs','coefficient_lists_emitted','scientific_replications']),'No product science run or coefficient list')
 state=json.loads(read(PACKET+'/PUBLICATION_STATE.json'))
 require(all(state[k] is None for k in ['source_wrapper_review','source_publication_binding','canonical_integration','current_base_observation','canonical_review','staged_review','primary_execution','publication_action','retained_audit']),'Unexecuted publication fields')
 require(state['actual_scientific_source_acceptances']==EXPECTED_ACCEPTANCES,'Actual source decisions separate from future approvals')
 require(state['scientific_programs_run_this_draft']==0 and state['scientific_replays']==0,'No packaging science replay')
 binding=json.loads(read(PACKET+'/ACTUAL_BINDING.json'))
 require(binding['kind']=='unbound_source_only_proposal' and all(binding[k] is None for k in ['source_review','base_observation','canonical_review','canonical_parent_binding','staged_review','publication']),'Unbound future contract')
 return {'note_sha256':digest(note),'body_count':len(maps),'source_aliases':len(sources),'archive_objects':len(archive),'original_metadata_receipts':len(contracts),'new_scientific_executions':0}
def verify_actual_binding(read,checked):
 # Intentionally fail closed: root must review a separate bound integration version.
 raise ValueError('UNBOUND SOURCE-ONLY PROPOSAL: canonical source/base/parent/review execution evidence is pending')
def main():
 checked=verify_payload(disk_read);verify_actual_binding(disk_read,checked)
if __name__=='__main__':main()
