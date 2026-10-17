"""Proposed root product-source source review recorder, metadata only."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,ast,difflib,hashlib,json
N=Path(__file__).resolve().parents[1]
D=N/'product_source_mediator_qualified_publication_draft';P=D/'proposal'
PK=P/'.claude/science/physics-loops/toe-product-source-mediator-20261016'
O=N/'root_product_source_qualified_publication_review'
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def rd(p):return json.loads(Path(p).read_text())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
def put(p,v):p.write_text(json.dumps(v,indent=2)+'\n')

parser=argparse.ArgumentParser(description='Source-only proposal: root must supply a pinned completed judgment.')
parser.add_argument('--root-reviewed',action='store_true',required=True)
parser.add_argument('--expectations',type=Path,required=True)
parser.add_argument('--expectations-sha',required=True)
args=parser.parse_args();assert args.root_reviewed
expect_raw=args.expectations.read_bytes();assert hashlib.sha256(expect_raw).hexdigest()==args.expectations_sha
expect=json.loads(expect_raw)
assert expect['kind']=='product_source_review_expectations' and expect['root_completed_actual_read'] is True
assert all(v is not None for v in expect.values()),'Null templates are not actual review inputs'
assert isinstance(expect['review_markdown'],str) and expect['review_markdown'].strip()

assert not O.exists()
assert expect['source_freeze_sha256']=='454a8314303086e43da24a8e447b684308d65037218080b4163d01d800f556eb'
assert pin(D/'FINAL_FREEZE.json')['sha256']=='454a8314303086e43da24a8e447b684308d65037218080b4163d01d800f556eb'
members=rd(D/'FINAL_FREEZE.json')['members'];assert len(members)==166
for r in members:same(D/r['path'],r)
assert {str(p.relative_to(D)) for p in D.rglob('*') if p.is_file()}=={r['path'] for r in members}|{'FINAL_FREEZE.json'}
m=rd(PK/'INPUT_MANIFEST.json')
for r in m['inputs']:same(P/r['path'],r)
note=P/'docs/PRODUCT_SOURCE_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-16.md'
primary=P/'scripts/product_source_mediator_2026_10_16.py'
raw=note.read_bytes();bm=rd(PK/'BODY_MAP.json')
assert raw[:bm['new_wrapper_bytes'][1]]==(D/'packet_text/WRAPPER.md').read_bytes()
assert len(bm['bodies'])==8
for r in bm['bodies']:
 b=raw[r['start_byte_inclusive']:r['end_byte_exclusive']]
 assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
 assert b==(N/r['source']).read_bytes() and raw.count(b)==1
sources=rd(PK/'SOURCE_MANIFEST.json')['sources'];objects=rd(PK/'ARCHIVE_INDEX.json')['objects']
assert len(sources)==71 and len(objects)==49
for r in sources:same(r['original_path'],r);same(P/r['recovery_path'],r)
for r in objects:same(P/r['path'],r)
assert {r['sha256'] for r in sources}=={r['sha256'] for r in objects}
freezes=rd(PK/'FROZEN_SOURCE_CLOSURE.json')['roots'];assert len(freezes)==5
for r in freezes:
 f=rd(N/r['alias']);assert pin(N/r['alias'])['sha256']==r['sha256']
 rows=f[r['key']];assert len(rows)==r['members'] and set(r['selected_members'])=={x['path'] for x in rows}
 for x in rows:same(N/r['folder']/x['path'],x)
acceptances={'product_source_mediator_root_review/ACCEPTANCE.json':'9505e42b907fdb9031f42b02b4609965ef7980af536e9197c4864aba124119f5','product_source_mediator_pauli_root_review/ACCEPTANCE.json':'c79e410fcae41d3a061cf28bc2ffd45d06093a04dbe88e8961523f292a979cfa'}
for p,h in acceptances.items():assert pin(N/p)['sha256']==h
repl={'__MANIFEST_SHA256__':pin(PK/'INPUT_MANIFEST.json')['sha256'],'__AUDIT_INPUT_PATHS__':repr([r['path'] for r in m['inputs']]+[str((PK/'INPUT_MANIFEST.json').relative_to(P))]),'__EXPECTED_BODIES__':repr({r['name']:r['sha256'] for r in bm['bodies']}),'__EXPECTED_FREEZES__':repr({r['alias']:r['sha256'] for r in freezes}),'__EXPECTED_ACCEPTANCES__':repr(acceptances)}
generated=(D/'primary_template.py').read_text()
for k,v in repl.items():generated=generated.replace(k,v)
assert primary.read_text()==generated
def functions(p):
 s=p.read_text();return {x.name:ast.get_source_segment(s,x) for x in ast.walk(ast.parse(s)) if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef))}
reuse=rd(D/'CODE_REUSE_MAP.json');verified=0
for r in reuse['functions']:
 s=functions(D/r['file'])[r['function']];assert hashlib.sha256(s.encode()).hexdigest()==r['source_sha256']
 if r['exact_source_reuse']:
  assert s==functions(N/reuse['baseline']/r['file'])[r['function']];verified+=1
assert verified==21 and len(reuse['functions'])==23
expected_diff=[]
for name in ['build_packet.py','primary_template.py','inspect_packet.py','record_metadata.py','seal_packet.py']:
 old=(D/'machinery_reference'/name).read_text();new=(D/name).read_text()
 expected_diff.extend(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='machinery_reference/'+name,tofile=name))
assert (D/'CODE_FULL_DIFF.patch').read_text()==''.join(expected_diff)
for r in rd(D/'MACHINERY_SOURCE_PINS.json')['sources']:same(r['source'],r);same(D/r['recovery_path'],r)
receipts=[]
historical_deltas=[]
recovery=rd(D/'source_revisions/prepare_input_recovery/RECOVERY.json')
assert recovery['not_a_source_at_launch_capture'] is True and recovery['all_bytes_match_actual_launch_pins'] is True
recovered={r['original']:r for r in recovery['files']};assert len(recovered)==len(recovery['files'])==8
for row in recovered.values():same(D/row['recovered_path'],row)
assert pin(D/'metadata_runs/prepare/INPUT_IDENTITIES_AT_LAUNCH.json')['sha256']==recovery['launch_manifest_sha256']
launch_inputs={x['path']:x for x in rd(D/'metadata_runs/prepare/INPUT_IDENTITIES_AT_LAUNCH.json')}
for path,row in recovered.items():assert {k:row[k] for k in ('bytes','sha256')}=={k:launch_inputs[path][k] for k in ('bytes','sha256')}

for mode in ('prepare','build','inspection','seal'):
 run=D/'metadata_runs'/mode;r=rd(run/'EXECUTION.json');launch=rd(run/'LAUNCH.json')
 assert all(r[k]==v for k,v in launch.items())
 assert r['exit_code']==0 and not r['timed_out'] and r['scientific_programs_run']==0 and r['timeout_seconds']==60
 assert r['started_utc']<=r['finished_utc'] and r['elapsed_seconds']>=0
 for k in ('child_source_at_launch','source_capture','recorder_at_launch','input_identities_at_launch','stdout','stderr'):same(r[k]['path'],r[k])
 same(r['original_source_at_launch']['path'],r['original_source_at_launch'])
 assert r['argv'][1]=='-B' and r['argv'][2]==r['child_source_at_launch']['path'] and r['argv'][3:]==[str(D)] and r['cwd']==str(D)
 assert r['original_source_at_launch']['sha256']==r['child_source_at_launch']['sha256']
 assert r['original_source_at_launch']['path']!=r['child_source_at_launch']['path']
 assert r['inputs_unchanged_after_run'] and (run/'stderr').read_bytes()==b''
 for row in rd(r['input_identities_at_launch']['path']):
  current=pin(Path(row['path']))
  if current!=row:
   assert mode=='prepare' and row['path'] in recovered,'Unrecorded post-run input change'
   old=recovered[row['path']];same(D/old['recovered_path'],row)
   historical_deltas.append({'run':mode,'historical_input_identity':row,'final_input_identity':current,'recovered_original':pin(D/old['recovered_path'])})
  else:same(row['path'],row)
 receipts.append(pin(run/'EXECUTION.json'))
v=rd(D/'VERIFICATION.json');assert v==rd(D/'metadata_runs/inspection/stdout')
mut=v['scoped_metadata_mutants']+v['direct_receipt_predicate_mutants']
assert len(mut)==35 and all(r['rejected'] for r in mut)
assert not v['mathematics_tested_by_this_execution'] and v['historical_scientific_replays']==0
assert v['checked']['body_count']==8
assert historical_deltas==expect['historical_input_deltas'], 'Root must review precise prepare-stage changes and recovered original bytes'
contracts_record=rd(PK/'EXECUTION_CONTRACTS.json');contracts=contracts_record['receipts']
assert len(contracts)==5 and contracts_record['new_scientific_executions']==0 and contracts_record['historical_product_scientific_runs']==0
assert sum(c['schema']=='product_review_metadata' for c in contracts)==3 and sum(c['schema']=='root_review_run' for c in contracts)==2
assert all(c['record']['exit_code']==0 and c['scope']=='metadata only' for c in contracts)
for contract in contracts:
 assert rd(N/contract['alias'])==contract['record']
 for row in contract['files']:same(N/row['alias'],row)
 assert (N/contract['original_alias']).read_bytes()==(N/contract['snapshot_alias']).read_bytes()
 assert hashlib.sha256((N/contract['original_alias']).read_bytes()).hexdigest()==contract['source_sha256']
 assert contract['record']['argv'][contract['argv_source_index']]==str(N/contract['original_alias'])
parent=rd(PK/'PARENT_BINDING.json');assert parent['canonical_binding_complete'] is False and parent['canonical_graph_disposition'] is None
assert len(parent['direct_mathematical_parents'])==1
proposed_parent=parent['direct_mathematical_parents'][0]
assert proposed_parent['note']=='docs/WEAK_MEDIATOR_FIXED_TARGET_BOUNDED_THEOREM_NOTE_2026-10-16.md'
assert proposed_parent['canonical_sha256'] is None and proposed_parent['parent_publication_binding'] is None
assert proposed_parent['physical_Bell_permissions_imported'] is False and parent['product_cannot_be_retroactive_parent_of_weak_mediator'] is True
body_hashes={x['name']:x['sha256'] for x in bm['bodies']}
assert body_hashes['controlling_root_qualification']=='e34377a876885c892d436a2c0fd1c0d32803d332782464c217d004f10eb02ff7'
assert body_hashes['controlling_pauli_qualification']=='1285dde8589a8cb5e923b2cb59028556461d99327a622477812c8cdbe55a58f9'
required=expect['required_canonical_replacements'];assert isinstance(required,list)
assert expect['disposition']=='QUALIFIED_SOURCE_INTEGRATION_APPROVED_CANONICAL_CHECKS_PENDING'
assert expect['proposed_graph_disposition']=='one_new_child_one_direct_parent_edge'
prose=expect['review_markdown']
O.mkdir();(O/'REVIEW.md').write_text(prose)
ev=dict(utc=datetime.now(timezone.utc).isoformat(),exact_freeze_members=166,immutable_bodies=8,source_aliases=71,archive_objects=49,source_freezes=5,exact_function_reuses=21,metadata_mutants=35,receipts=receipts,complete_new_code_and_prose_read=True,complete_metadata_streams_read=True,scientific_executions=0,required_canonical_replacements=required)
ev.update(historical_input_deltas=historical_deltas,historical_receipts=5,historical_successes=5,historical_metadata_failures=0,historical_author_scientific_executions=0,historical_saved_certificate_executions=0,proposed_parent=parent,review_expectations=expect,review_expectation_source=pin(args.expectations),review_expectations_original_utf8=expect_raw.decode('utf-8'))
put(O/'MECHANICAL_EVIDENCE.json',ev)
r=dict(kind='root_qualified_source_publication_review',utc=datetime.now(timezone.utc).isoformat(),root_read_complete=True,disposition='QUALIFIED_SOURCE_INTEGRATION_APPROVED_CANONICAL_CHECKS_PENDING',source_freeze=pin(D/'FINAL_FREEZE.json'),source_note=pin(note),source_validator=pin(primary),source_manifest=pin(PK/'SOURCE_MANIFEST.json'),source_wrapper=pin(D/'packet_text/WRAPPER.md'),review=pin(O/'REVIEW.md'),evidence=pin(O/'MECHANICAL_EVIDENCE.json'),immutable_bodies=8,source_aliases=71,archive_objects=49,metadata_receipts=receipts,scientific_executions=0,actual_canonical_acceptance=None,actual_publication=None,retained_audit=False,required_canonical_replacements=required,proposed_graph_disposition='one_new_child_one_direct_parent_edge',editable_prompt_files_changed=[])
put(O/'REVIEW.json',r);put(O/'FREEZE.json',dict(utc=datetime.now(timezone.utc).isoformat(),members=[dict(pin(O/n),path=n) for n in ('REVIEW.md','MECHANICAL_EVIDENCE.json','REVIEW.json')]))
print(json.dumps(dict(review=pin(O/'REVIEW.json'),freeze=pin(O/'FREEZE.json'),science_executions=0)))
