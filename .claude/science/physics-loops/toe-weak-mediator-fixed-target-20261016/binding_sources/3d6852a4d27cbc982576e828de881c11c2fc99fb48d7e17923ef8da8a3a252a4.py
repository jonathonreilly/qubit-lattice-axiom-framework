"""Proposed root weak-mediator source review recorder, metadata only."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,ast,difflib,hashlib,json
N=Path(__file__).resolve().parents[1]
D=N/'weak_mediator_qualified_publication_draft';P=D/'proposal'
PK=P/'.claude/science/physics-loops/toe-weak-mediator-fixed-target-20261016'
O=N/'root_weak_mediator_qualified_publication_review'
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
assert expect['kind']=='weak_mediator_source_review_expectations' and expect['root_completed_actual_read'] is True
assert all(v is not None for v in expect.values()),'Null templates are not actual review inputs'
assert isinstance(expect['review_markdown'],str) and expect['review_markdown'].strip()

assert not O.exists()
assert expect['source_freeze_sha256']=='32b3edb257c7695c24242b6ef36680468e31e5d8ee6d1156936fb2b44128fa0f'
assert pin(D/'FINAL_FREEZE.json')['sha256']=='32b3edb257c7695c24242b6ef36680468e31e5d8ee6d1156936fb2b44128fa0f'
members=rd(D/'FINAL_FREEZE.json')['members'];assert len(members)==206
for r in members:same(D/r['path'],r)
assert {str(p.relative_to(D)) for p in D.rglob('*') if p.is_file()}=={r['path'] for r in members}|{'FINAL_FREEZE.json'}
m=rd(PK/'INPUT_MANIFEST.json')
for r in m['inputs']:same(P/r['path'],r)
note=P/'docs/WEAK_MEDIATOR_FIXED_TARGET_BOUNDED_THEOREM_NOTE_2026-10-16.md'
primary=P/'scripts/weak_mediator_fixed_target_2026_10_16.py'
raw=note.read_bytes();bm=rd(PK/'BODY_MAP.json')
assert raw[:bm['new_wrapper_bytes'][1]]==(D/'packet_text/WRAPPER.md').read_bytes()
assert len(bm['bodies'])==12
for r in bm['bodies']:
 b=raw[r['start_byte_inclusive']:r['end_byte_exclusive']]
 assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
 assert b==(N/r['source']).read_bytes() and raw.count(b)==1
sources=rd(PK/'SOURCE_MANIFEST.json')['sources'];objects=rd(PK/'ARCHIVE_INDEX.json')['objects']
assert len(sources)==179 and len(objects)==107
for r in sources:same(r['original_path'],r);same(P/r['recovery_path'],r)
for r in objects:same(P/r['path'],r)
assert {r['sha256'] for r in sources}=={r['sha256'] for r in objects}
freezes=rd(PK/'FROZEN_SOURCE_CLOSURE.json')['roots'];assert len(freezes)==9
for r in freezes:
 f=rd(N/r['alias']);assert pin(N/r['alias'])['sha256']==r['sha256']
 rows=f[r['key']];assert len(rows)==r['members'] and set(r['selected_members'])=={x['path'] for x in rows}
 for x in rows:same(N/r['folder']/x['path'],x)
acceptances={'weak_mediator_root_review/ACCEPTANCE.json':'ba201403a60d1c94751d1550f14d59622c86920ced74ebae21f5f51f5752731b'}
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
editorial_deltas=[]
for mode in ('prepare','build','inspection','seal'):
 run=D/'metadata_runs'/mode;r=rd(run/'EXECUTION.json');launch=rd(run/'LAUNCH.json')
 assert all(r[k]==v for k,v in launch.items())
 assert r['exit_code']==0 and not r['timed_out'] and r['scientific_programs_run']==0 and r['timeout_seconds']==60
 assert r['started_utc']<=r['finished_utc'] and r['elapsed_seconds']>=0
 for k in ('child_source_at_launch','original_source_at_launch','source_capture','recorder_at_launch','input_identities_at_launch','stdout','stderr'):same(r[k]['path'],r[k])
 assert r['argv'][1]=='-B' and r['argv'][2]==r['child_source_at_launch']['path'] and r['argv'][3:]==[str(D)] and r['cwd']==str(D)
 assert r['original_source_at_launch']['sha256']==r['child_source_at_launch']['sha256']
 assert r['original_source_at_launch']['path']!=r['child_source_at_launch']['path']
 assert r['inputs_unchanged_after_run'] and (run/'stderr').read_bytes()==b''
 for row in rd(r['input_identities_at_launch']['path']):
  current=pin(Path(row['path']))
  if current!=row:
   assert Path(row['path']) in {D/'CHECKPOINT.md',D/'BOOKKEEPING_RECOVERY.md'},'Substantive input changed after metadata launch'
   editorial_deltas.append({'run':mode,'historical_input_identity':row,'final_editorial_identity':current})
  else:same(row['path'],row)
 receipts.append(pin(run/'EXECUTION.json'))
v=rd(D/'VERIFICATION.json');assert v==rd(D/'metadata_runs/inspection/stdout')
mut=v['scoped_metadata_mutants']+v['direct_receipt_predicate_mutants']
assert len(mut)==61 and all(r['rejected'] for r in mut)
assert not v['mathematics_tested_by_this_execution'] and v['historical_scientific_replays']==0
assert v['checked']['body_count']==12
assert editorial_deltas==expect['editorial_input_deltas'], 'Root must review exact historical/final editorial differences'
contracts=rd(PK/'EXECUTION_CONTRACTS.json')['receipts'];additional=rd(PK/'ADDITIONAL_EVIDENCE.json')['records']
assert len(contracts)==10 and len(additional)==3
history=[x['record'] for x in contracts+additional]
assert sum(x['exit_code']==0 for x in history)==12 and sum(x['exit_code']==1 for x in history)==1
assert sum(x['schema'].startswith('scientific_') for x in contracts)==2
assert rd(PK/'ADDITIONAL_EVIDENCE.json')['saved_certificate_scientific_executions']==1
required=expect['required_canonical_replacements'];assert isinstance(required,list)
assert expect['disposition']=='QUALIFIED_SOURCE_INTEGRATION_APPROVED_CANONICAL_CHECKS_PENDING'
assert expect['proposed_graph_disposition']=='one_new_root_zero_direct_parent_edges'
prose=expect['review_markdown']
O.mkdir();(O/'REVIEW.md').write_text(prose)
ev=dict(utc=datetime.now(timezone.utc).isoformat(),exact_freeze_members=206,immutable_bodies=12,source_aliases=179,archive_objects=107,source_freezes=9,exact_function_reuses=21,metadata_mutants=61,receipts=receipts,complete_new_code_and_prose_read=True,complete_metadata_streams_read=True,scientific_executions=0,required_canonical_replacements=required)
ev.update(editorial_input_deltas=editorial_deltas,historical_receipts=13,historical_successes=12,historical_metadata_failures=1,historical_author_scientific_executions=2,historical_saved_certificate_executions=1,review_expectations=expect,review_expectation_source=pin(args.expectations),review_expectations_original_utf8=expect_raw.decode('utf-8'))
put(O/'MECHANICAL_EVIDENCE.json',ev)
r=dict(kind='root_qualified_source_publication_review',utc=datetime.now(timezone.utc).isoformat(),root_read_complete=True,disposition='QUALIFIED_SOURCE_INTEGRATION_APPROVED_CANONICAL_CHECKS_PENDING',source_freeze=pin(D/'FINAL_FREEZE.json'),source_note=pin(note),source_validator=pin(primary),source_manifest=pin(PK/'SOURCE_MANIFEST.json'),source_wrapper=pin(D/'packet_text/WRAPPER.md'),review=pin(O/'REVIEW.md'),evidence=pin(O/'MECHANICAL_EVIDENCE.json'),immutable_bodies=12,source_aliases=179,archive_objects=107,metadata_receipts=receipts,scientific_executions=0,actual_canonical_acceptance=None,actual_publication=None,retained_audit=False,required_canonical_replacements=required,proposed_graph_disposition='one_new_root_zero_direct_parent_edges',editable_prompt_files_changed=[])
put(O/'REVIEW.json',r);put(O/'FREEZE.json',dict(utc=datetime.now(timezone.utc).isoformat(),members=[dict(pin(O/n),path=n) for n in ('REVIEW.md','MECHANICAL_EVIDENCE.json','REVIEW.json')]))
print(json.dumps(dict(review=pin(O/'REVIEW.json'),freeze=pin(O/'FREEZE.json'),science_executions=0)))
