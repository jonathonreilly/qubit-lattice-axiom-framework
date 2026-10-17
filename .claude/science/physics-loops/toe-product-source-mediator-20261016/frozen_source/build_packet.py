"""Build product-source provenance metadata; never execute scientific code."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
D=Path(sys.argv[1]).resolve();N=D.parent
P=D/'proposal';PK='.claude/science/physics-loops/toe-product-source-mediator-20261016'
NOTE='docs/PRODUCT_SOURCE_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-16.md'
SCRIPT='scripts/product_source_mediator_2026_10_16.py'
ROOTS={
 'product_source_mediator_exposed_check':('ORIGINAL_FREEZE.json','97b89284b05f95c00065bec70bfd8d38e1bcd366ea49f058384f585f9056e116','members'),
 'product_source_mediator_exposed_check/finite_compiler_addendum':('FREEZE.json','c0f663eb320fb96172ba94e7a4be221111a38ed4d285a0dde8b587084bdc22dc','members'),
 'product_source_mediator_root_review':('FREEZE.json','3a7e1e2b179e85f779c92a7720ee160f235ed398b9b6041a91e53f8ed7313495','files'),
 'product_source_mediator_exposed_check/pauli_block_addendum':('FREEZE.json','353d5c54b12d105c852b7abbe0960c5a85cebb83414890d929dbe6abcd3102f3','members'),
 'product_source_mediator_pauli_root_review':('FREEZE.json','977899e86e3c11c516bb16c8afae406ddfb625208118ebd5ee6db39fa570ba48','files'),
}
EXTRA_DIRS=['runs/product_source_root_acceptance','runs/product_pauli_root_acceptance']
EXTRA_FILES=['bootstrap/record_product_source_acceptance.py','review_run.py',
 'product_source_mediator_candidate/PROPOSAL.md','product_source_mediator_candidate/FINITE_COMPILER_ADDENDUM.md',
 'weak_mediator_candidate/PROPOSAL.md','weak_mediator_candidate/FINITE_COMPILER_ADDENDUM.md',
 'bootstrap/record_product_pauli_acceptance.py','product_source_mediator_candidate/PAULI_BLOCK_ADDENDUM.md']
ACCEPTANCES={
 'product_source_mediator_root_review/ACCEPTANCE.json':'9505e42b907fdb9031f42b02b4609965ef7980af536e9197c4864aba124119f5',
 'product_source_mediator_pauli_root_review/ACCEPTANCE.json':'c79e410fcae41d3a061cf28bc2ffd45d06093a04dbe88e8961523f292a979cfa',
}
BODIES=[
 ('original_proposal','product_source_mediator_candidate/PROPOSAL.md'),
 ('finite_compiler_addendum','product_source_mediator_candidate/FINITE_COMPILER_ADDENDUM.md'),
 ('original_analytic_review','product_source_mediator_exposed_check/REVIEW.md'),
 ('finite_compiler_analytic_review','product_source_mediator_exposed_check/finite_compiler_addendum/REVIEW.md'),
 ('controlling_root_qualification','product_source_mediator_root_review/QUALIFICATION.md'),
 ('pauli_realization_addendum','product_source_mediator_candidate/PAULI_BLOCK_ADDENDUM.md'),
 ('pauli_analytic_review','product_source_mediator_exposed_check/pauli_block_addendum/REVIEW.md'),
 ('controlling_pauli_qualification','product_source_mediator_pauli_root_review/QUALIFICATION.md'),
]
BODY_PINS={
 'original_proposal':'aa1be4b5bef9450cc9e5d6bd94feb440f15ebbb6ac8f38a309dfa5af35de2248',
 'finite_compiler_addendum':'afe663938b30c750d8a5097b876b3e557212e5e6480fcfa19c466a5483188065',
 'original_analytic_review':'517b3714e8b73bb082ed95b8fab1b5bc07f8c4490f4c2fc8f56816fa0681bf53',
 'finite_compiler_analytic_review':'c6ac427900ab13bf671f607b393a94d52f2361b6435ae80f3a959c836458abf6',
 'controlling_root_qualification':'e34377a876885c892d436a2c0fd1c0d32803d332782464c217d004f10eb02ff7',
 'pauli_realization_addendum':'8d166d5c44512350dd0aa193bb94d28d7a9c9534b9d0958d73ed4decb7d2275f',
 'pauli_analytic_review':'4335ef2a21127fb0658c9b39de94e127fba95b3ebbaa3a68ef7d2ed4a898e7c0',
 'controlling_pauli_qualification':'1285dde8589a8cb5e923b2cb59028556461d99327a622477812c8cdbe55a58f9',
}
sha=lambda b:hashlib.sha256(b).hexdigest()
def put(rel,b):
 p=P/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
def js(rel,x):put(rel,(json.dumps(x,indent=2)+'\n').encode())
def ident(b):return {'bytes':len(b),'sha256':sha(b)}
def read(p):return json.loads(p.read_text())
sources={};objects={};freeze_rows=[]
def add(path,alias=None,role='historical_source'):
 path=path.resolve();path.relative_to(N);b=path.read_bytes();alias=alias or str(path.relative_to(N));h=sha(b)
 r={'source':alias,'original_path':str(path),'role':role,**ident(b),'recovery_path':PK+'/archive/sha256/'+h}
 if alias in sources:assert sources[alias]['sha256']==h
 else:sources[alias]=r
 objects[h]={'path':r['recovery_path'],**ident(b)}
 if not (P/r['recovery_path']).exists():put(r['recovery_path'],b)
 return b
assert not P.exists(),'Refuse overwrite of an existing proposal'
for folder,(filename,pin,key) in ROOTS.items():
 f=N/folder/filename;raw=add(f,role='source_freeze');assert sha(raw)==pin
 rows=read(f)[key];selected=[];member_aliases={}
 assert len({r['path'] for r in rows})==len(rows)
 for row in rows:
  original=row['path'];path=(N/folder/original).resolve();path.relative_to(N/folder)
  b=path.read_bytes();assert ident(b)=={k:row[k] for k in ['bytes','sha256']},str(path)
  alias=str(path.relative_to(N));add(path);selected.append(original);member_aliases[original]=alias
 freeze_rows.append({'folder':folder,'alias':folder+'/'+filename,'sha256':pin,'members':len(rows),
  'key':key,'complete_members':True,'selected_members':selected,'member_aliases':member_aliases,'all_original_members_verified_at_build':True})
for folder in EXTRA_DIRS:
 for p in sorted((N/folder).rglob('*')):
  if p.is_file():add(p,role='actual_terminal_source_receipt_or_full_stream')
for path in EXTRA_FILES:add(N/path,role='actual_original_source_or_mathematical_parent_source')
specs=[
 ('product_source_mediator_exposed_check/metadata','product_review_metadata','product_source_mediator_exposed_check/inspect_sources.py','executed_source.py',2),
 ('product_source_mediator_exposed_check/finite_compiler_addendum/metadata','product_review_metadata','product_source_mediator_exposed_check/finite_compiler_addendum/inspect_sources.py','executed_source.py',2),
 ('runs/product_source_root_acceptance','root_review_run','bootstrap/record_product_source_acceptance.py','executed_source.py',1),
 ('product_source_mediator_exposed_check/pauli_block_addendum/metadata','product_review_metadata','product_source_mediator_exposed_check/pauli_block_addendum/inspect_sources.py','executed_source.py',2),
 ('runs/product_pauli_root_acceptance','root_review_run','bootstrap/record_product_pauli_acceptance.py','executed_source.py',1),
]
contracts=[]
for folder,schema,original,snapshot,index in specs:
 alias=folder+'/EXECUTION.json';r=read(N/alias);assert r['exit_code']==0
 source=add(N/original,role='original_source_of_actual_metadata_execution')
 captured=add(N/folder/snapshot,role='separate_source_at_launch');assert source==captured
 assert r['argv'][index]==str(N/original),'Original source, not capture, was actually launched'
 files=[]
 for p in sorted((N/folder).rglob('*')):
  if p.is_file() and p.name!='EXECUTION.json':
   a=str(p.relative_to(N));b=add(p);files.append({'alias':a,**ident(b)})
 if schema=='root_review_run':
  b=add(N/'review_run.py');files.append({'alias':'review_run.py',**ident(b)})
  assert ident(b)=={k:r['recorder'][k] for k in ['bytes','sha256']}
 start=r.get('start_utc',r.get('started_at'));end=r.get('end_utc',r.get('finished_at'))
 assert start<end and r['elapsed_seconds']>=0
 contracts.append({'alias':alias,'schema':schema,'record':r,'original_alias':original,
  'snapshot_alias':folder+'/'+snapshot,'executed_alias':original,'argv_source_index':index,
  'source_sha256':sha(source),'files':files,'scope':'metadata only',
  'recorded_cwd':r.get('cwd'),'cwd_missing_in_original_receipt':'cwd' not in r,
  'stream_hashes_added_by_archive_not_original_receipt':schema=='product_review_metadata'})
for alias,h in ACCEPTANCES.items():assert sha((N/alias).read_bytes())==h
note=(D/'packet_text/WRAPPER.md').read_bytes();wrapper_len=len(note);maps=[]
for name,alias in BODIES:
 raw=(N/alias).read_bytes();assert alias in sources and sha(raw)==BODY_PINS[name]
 note+=('\n\n<!-- Unchanged complete source: '+name+' -->\n\n').encode();start=len(note);note+=raw
 maps.append({'name':name,'source':alias,'container':NOTE,'start_byte_inclusive':start,'end_byte_exclusive':len(note),**ident(raw)})
trailer_start=len(note)
note+=b'\n\nThe new wrapper and root qualifications control historical status. Source integrity is not proof, native supply, canonical binding or retained status.\n'
put(NOTE,note)
js(PK+'/BODY_MAP.json',{'new_wrapper_bytes':[0,wrapper_len],'trailing_wrapper_bytes':[trailer_start,len(note)],'bodies':maps})
js(PK+'/SOURCE_MANIFEST.json',{'schema':'product_source_mediator_source_archive_v1','sources':list(sources.values()),
 'archive_rule':'Complete selected original review/decision freeze inventories and bounded actual metadata closure; no prior publication archive traversal.'})
js(PK+'/ARCHIVE_INDEX.json',{'objects':list(objects.values()),'recursive_prior_publication_archives':False})
js(PK+'/FROZEN_SOURCE_CLOSURE.json',{'roots':freeze_rows})
js(PK+'/EXECUTION_CONTRACTS.json',{'receipts':contracts,'new_scientific_executions':0,'historical_product_scientific_runs':0})
js(PK+'/PARENT_BINDING.json',{'canonical_binding_complete':False,'direct_mathematical_parents':[{
 'note':'docs/WEAK_MEDIATOR_FIXED_TARGET_BOUNDED_THEOREM_NOTE_2026-10-16.md','canonical_sha256':None,
 'role':'exact finite-dimensional corrector/residual and equality-safe three-atan interval machinery only',
 'source_aliases':['weak_mediator_candidate/PROPOSAL.md','weak_mediator_candidate/FINITE_COMPILER_ADDENDUM.md'],
 'physical_Bell_permissions_imported':False,'parent_publication_binding':None}],
 'canonical_graph_disposition':None,'git_ancestry_is_not_mathematical_dependency':True,
 'other_campaign_theorems_composed':False,'product_cannot_be_retroactive_parent_of_weak_mediator':True})
state={k:None for k in ['source_wrapper_review','source_publication_binding','canonical_integration','current_base_observation','canonical_review','staged_review','primary_execution','publication_action','retained_audit']}
state.update(scientific_programs_run_this_draft=0,scientific_replays=0,
 actual_scientific_source_acceptances=ACCEPTANCES)
js(PK+'/PUBLICATION_STATE.json',state)
js(PK+'/ACTUAL_BINDING.json',{'kind':'unbound_source_only_proposal','source_review':None,'base_observation':None,'canonical_review':None,'canonical_parent_binding':None,'staged_review':None,'publication':None})
for name in ['PR_BODY.md','BINDING_CONTRACT.md','CLAIM_STATUS_CERTIFICATE.md','EVIDENCE_SCOPE.md']:put(PK+'/'+name,(D/'packet_text'/name).read_bytes())
js(PK+'/EXPOSURE.json',{'source_exposed':True,'same_selected_model':True,'blind_independence':False,
 'new_scientific_executions':0,'historical_scientific_replays':0,'historical_product_scientific_runs':0,
 'coefficient_lists_emitted':0,'scientific_replications':0,'analytical_review_metadata_runs':3,
 'root_science_acceptance_recording_runs':2,'retained_audit':False})
inputs=[]
for p in sorted(P.rglob('*')):
 if p.is_file():inputs.append({'path':str(p.relative_to(P)),**ident(p.read_bytes())})
js(PK+'/INPUT_MANIFEST.json',{'schema':'product_source_mediator_publication_inputs_v1','inputs':inputs})
msha=sha((P/PK/'INPUT_MANIFEST.json').read_bytes())
replacements={'__MANIFEST_SHA256__':msha,'__AUDIT_INPUT_PATHS__':repr([r['path'] for r in inputs]+[PK+'/INPUT_MANIFEST.json']),
 '__EXPECTED_BODIES__':repr({r['name']:r['sha256'] for r in maps}),
 '__EXPECTED_FREEZES__':repr({r['alias']:r['sha256'] for r in freeze_rows}),
 '__EXPECTED_ACCEPTANCES__':repr(ACCEPTANCES)}
generated=(D/'primary_template.py').read_text()
for key,value in replacements.items():generated=generated.replace(key,value)
put(SCRIPT,generated.encode())
result={'utc':datetime.now(timezone.utc).isoformat(),'note':NOTE,'note_sha256':sha(note),'primary_sha256':sha(generated.encode()),
 'unchanged_bodies':len(maps),'source_aliases':len(sources),'unique_archive_objects':len(objects),
 'source_receipts':len(contracts),'input_manifest_sha256':msha,'science_executions':0,'canonical_execution':None}
(D/'BUILD_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
