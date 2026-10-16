"""Source-integrity only. No scientific runner, simulation or proof is executed."""
from pathlib import Path,PurePosixPath
import hashlib,json
REPO=Path(__file__).resolve().parents[1]
NOTE='docs/PRODUCT_SOURCE_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-16.md'
PACKET='.claude/science/physics-loops/toe-product-source-mediator-20261016'
AUDIT_TIMEOUT_SEC=60
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/toe-product-source-mediator-20261016/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-product-source-mediator-20261016/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-product-source-mediator-20261016/BINDING_CONTRACT.md', '.claude/science/physics-loops/toe-product-source-mediator-20261016/BODY_MAP.json', '.claude/science/physics-loops/toe-product-source-mediator-20261016/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-product-source-mediator-20261016/EVIDENCE_SCOPE.md', '.claude/science/physics-loops/toe-product-source-mediator-20261016/EXECUTION_CONTRACTS.json', '.claude/science/physics-loops/toe-product-source-mediator-20261016/EXPOSURE.json', '.claude/science/physics-loops/toe-product-source-mediator-20261016/FROZEN_SOURCE_CLOSURE.json', '.claude/science/physics-loops/toe-product-source-mediator-20261016/PARENT_BINDING.json', '.claude/science/physics-loops/toe-product-source-mediator-20261016/PR_BODY.md', '.claude/science/physics-loops/toe-product-source-mediator-20261016/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-product-source-mediator-20261016/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/012fc26792563bdcc5090ff42570826f297ff8fd81533a9902fa8166e6ccfdb4', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/02cfae2b6d31428e00aae7dbbcce3978366ffcd6de217c6ce2bbcc012a15a661', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/052bcf3f2b5577ab5f8d4988f42d25cbb0f52ec6d61999a7a269072f44f14395', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/0c2f97d373ec11c7cc4089330a184ec24e332ccae4c934c2d7dba33c8458137b', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/119b3b977113f1845eca81466b0a33d628f3bbecc61e61f5fd0f7b698cd9a0ca', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/1285dde8589a8cb5e923b2cb59028556461d99327a622477812c8cdbe55a58f9', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/1b8333ee93f9e29c62f85c30e1e4c5f27512a733425948c25c25466fda2cb9f1', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/22e62c1408387329d172d7c3b1e6dc5591fc550b639756db7f92f1e3b159649b', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/22efb1a23713c671d40da0d20f51d12fd8ff0aed3f00e6776d8a80152b139814', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/2ad3573fe74805c1f25be99f18a2eb7e70e405ebff295182557a386a6bbdf517', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/2bb259cbd81c2385f249d4c743ec8dc7e384f4b2919ca180ca908e8d806d93ac', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/353d5c54b12d105c852b7abbe0960c5a85cebb83414890d929dbe6abcd3102f3', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/3a7e1e2b179e85f779c92a7720ee160f235ed398b9b6041a91e53f8ed7313495', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/4335ef2a21127fb0658c9b39de94e127fba95b3ebbaa3a68ef7d2ed4a898e7c0', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/4f2e00d4a1ef4987d4b13e5c8ab74f63bf40436d094a20bd424252e9d0f7f3b4', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/517b3714e8b73bb082ed95b8fab1b5bc07f8c4490f4c2fc8f56816fa0681bf53', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/54190d8be9c64ab8838ef7447454e479ff587e0e372f1e6f034c19a10c1d058b', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/67e7092c3d78dd554dbec8be2c0fac3140761940ccbee64e9c56627c37910cf8', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/740802d4265514aa32479bed90530b40e5a3a954a1aa0c694962964c5cdc4248', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/778c2c98a1077c6a03dd269583138d4161b9403835c73610cb14075a659697d0', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/77e582b092ce7bc967f3d31a443b09891b7cb3c8b33bd88c2438d5034385fd9e', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/7c54639374626757ac9aa4d32a5bf23b317a62e2560d8ed4c4c1651f15babed8', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/85bf5c491574d901c18bf186ae9fb41d113dc5ef578d11e79f90ba532829894d', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/8d166d5c44512350dd0aa193bb94d28d7a9c9534b9d0958d73ed4decb7d2275f', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/8d7c03799d95f281c4a9802bb40d4bdcbc40cac74ee83e5b0b04d1080073e4e6', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/95050f993177cbdcce29d9c73962d57c27e3ec828b542509cf07e94161316e40', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/9505e42b907fdb9031f42b02b4609965ef7980af536e9197c4864aba124119f5', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/96f8fb4656a47c763538ed966499c23fa44c1c3c750d4f2db20d9e123ce2a37b', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/977899e86e3c11c516bb16c8afae406ddfb625208118ebd5ee6db39fa570ba48', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/97b89284b05f95c00065bec70bfd8d38e1bcd366ea49f058384f585f9056e116', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/98823ec54534c9d87922d61f5b8440918e06ca85107b4be09eb6908f263ed716', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/9a0f400c3572f6dbb136ae055db090fa50a3a94fc610a451c3da2d7125e15621', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/9ebe21c87187f6450a56539586de6633465b9d03b318446e58711ae19e0e22a1', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/a40b0fc1be804c2e686b9909facc4369a494dc44223306314365638c280e169b', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/aa1be4b5bef9450cc9e5d6bd94feb440f15ebbb6ac8f38a309dfa5af35de2248', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/ade981d45d1a6deb22c1f4fc72d08d08e031cd7d39171b2aa343ce1e931f3675', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/afe663938b30c750d8a5097b876b3e557212e5e6480fcfa19c466a5483188065', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/b2161150997749c72ad1e0867a4fcf519ebdbfa07bd526d1faa552eb1f567428', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/c0f663eb320fb96172ba94e7a4be221111a38ed4d285a0dde8b587084bdc22dc', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/c5ad25ed30aca28e8f66b3e3cab006e044163756006ffddc68f4f5fd51956432', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/c6ac427900ab13bf671f607b393a94d52f2361b6435ae80f3a959c836458abf6', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/c79e410fcae41d3a061cf28bc2ffd45d06093a04dbe88e8961523f292a979cfa', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/c948f5af8cdf130fbacc9f2f43bb7bc98f92abfae52141718a5300fb4444a04c', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/cfb6f37996afca1bfafcc2a49bf1ad7475b5f8ff0799d3823dd14cf8fbdf3487', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/dcba2ef934e166a2e5c4be7a087a9551184485cd9d2e2b99ff2d215907e6228d', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/de40fdb02b567a0cbb0e43241cb659ac82756bdc6b5ddbf9b80d4f0557918ccf', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/e34377a876885c892d436a2c0fd1c0d32803d332782464c217d004f10eb02ff7', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', '.claude/science/physics-loops/toe-product-source-mediator-20261016/archive/sha256/fb60aa48ee40743326ccb221edfcb3a627a8a66b5ef3178c642175bd2a0195fd', 'docs/PRODUCT_SOURCE_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-16.md', '.claude/science/physics-loops/toe-product-source-mediator-20261016/INPUT_MANIFEST.json']
MANIFEST_SHA256='9e2c64ceb00bca0de4960d15a7b24e2034445ea07acf56ee8f063f4fd7ad6897'
EXPECTED_BODIES={'original_proposal': 'aa1be4b5bef9450cc9e5d6bd94feb440f15ebbb6ac8f38a309dfa5af35de2248', 'finite_compiler_addendum': 'afe663938b30c750d8a5097b876b3e557212e5e6480fcfa19c466a5483188065', 'original_analytic_review': '517b3714e8b73bb082ed95b8fab1b5bc07f8c4490f4c2fc8f56816fa0681bf53', 'finite_compiler_analytic_review': 'c6ac427900ab13bf671f607b393a94d52f2361b6435ae80f3a959c836458abf6', 'controlling_root_qualification': 'e34377a876885c892d436a2c0fd1c0d32803d332782464c217d004f10eb02ff7', 'pauli_realization_addendum': '8d166d5c44512350dd0aa193bb94d28d7a9c9534b9d0958d73ed4decb7d2275f', 'pauli_analytic_review': '4335ef2a21127fb0658c9b39de94e127fba95b3ebbaa3a68ef7d2ed4a898e7c0', 'controlling_pauli_qualification': '1285dde8589a8cb5e923b2cb59028556461d99327a622477812c8cdbe55a58f9'}
EXPECTED_FREEZES={'product_source_mediator_exposed_check/ORIGINAL_FREEZE.json': '97b89284b05f95c00065bec70bfd8d38e1bcd366ea49f058384f585f9056e116', 'product_source_mediator_exposed_check/finite_compiler_addendum/FREEZE.json': 'c0f663eb320fb96172ba94e7a4be221111a38ed4d285a0dde8b587084bdc22dc', 'product_source_mediator_root_review/FREEZE.json': '3a7e1e2b179e85f779c92a7720ee160f235ed398b9b6041a91e53f8ed7313495', 'product_source_mediator_exposed_check/pauli_block_addendum/FREEZE.json': '353d5c54b12d105c852b7abbe0960c5a85cebb83414890d929dbe6abcd3102f3', 'product_source_mediator_pauli_root_review/FREEZE.json': '977899e86e3c11c516bb16c8afae406ddfb625208118ebd5ee6db39fa570ba48'}
EXPECTED_ACCEPTANCES={'product_source_mediator_root_review/ACCEPTANCE.json': '9505e42b907fdb9031f42b02b4609965ef7980af536e9197c4864aba124119f5', 'product_source_mediator_pauli_root_review/ACCEPTANCE.json': 'c79e410fcae41d3a061cf28bc2ffd45d06093a04dbe88e8961523f292a979cfa'}
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
