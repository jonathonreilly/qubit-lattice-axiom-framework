"""Record completed root static-edge publication-source review, metadata only."""
from pathlib import Path
from datetime import datetime,timezone
import ast,difflib,hashlib,json
N=Path(__file__).resolve().parents[1]
D=N/'commuting_static_edge_qualified_publication_draft';P=D/'proposal'
PK=P/'.claude/science/physics-loops/toe-commuting-static-edge-fixed-target-20261016'
O=N/'root_commuting_static_edge_qualified_publication_review'
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def rd(p):return json.loads(Path(p).read_text())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
def put(p,v):p.write_text(json.dumps(v,indent=2)+'\n')
assert not O.exists()
assert pin(D/'FINAL_FREEZE.json')['sha256']=='c0f7a24933d585f168b2e724911ef0707126a596daa7495c8db582c4e172fe40'
members=rd(D/'FINAL_FREEZE.json')['members'];assert len(members)==179
for r in members:same(D/r['path'],r)
assert {str(p.relative_to(D)) for p in D.rglob('*') if p.is_file()}=={r['path'] for r in members}|{'FINAL_FREEZE.json'}
m=rd(PK/'INPUT_MANIFEST.json')
for r in m['inputs']:same(P/r['path'],r)
note=P/'docs/COMMUTING_STATIC_EDGE_FIXED_TARGET_BOUNDED_THEOREM_NOTE_2026-10-16.md'
primary=P/'scripts/commuting_static_edge_fixed_target_2026_10_16.py'
raw=note.read_bytes();bm=rd(PK/'BODY_MAP.json')
assert raw[:bm['new_wrapper_bytes'][1]]==(D/'packet_text/WRAPPER.md').read_bytes()
assert len(bm['bodies'])==5
for r in bm['bodies']:
 b=raw[r['start_byte_inclusive']:r['end_byte_exclusive']]
 assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
 assert b==(N/r['source']).read_bytes() and raw.count(b)==1
sources=rd(PK/'SOURCE_MANIFEST.json')['sources'];objects=rd(PK/'ARCHIVE_INDEX.json')['objects']
assert len(sources)==153 and len(objects)==84
for r in sources:same(r['original_path'],r);same(P/r['recovery_path'],r)
for r in objects:same(P/r['path'],r)
assert {r['sha256'] for r in sources}=={r['sha256'] for r in objects}
freezes=rd(PK/'FROZEN_SOURCE_CLOSURE.json')['roots'];assert len(freezes)==5
for r in freezes:
 f=rd(N/r['alias']);assert pin(N/r['alias'])['sha256']==r['sha256']
 rows=f[r['key']];assert len(rows)==r['members'] and set(r['selected_members'])=={x['path'] for x in rows}
 for x in rows:same(N/r['folder']/x['path'],x)
acceptances={'commuting_static_edge_root_review/ACCEPTANCE.json':'f954c36d04380ee49edac71a5dd7cb10e31142d3f3ca03f4da71f5609c04446b'}
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
assert verified==19 and len(reuse['functions'])==23
expected_diff=[]
for name in ['build_packet.py','primary_template.py','inspect_packet.py','record_metadata.py','seal_packet.py']:
 old=(D/'machinery_reference'/name).read_text();new=(D/name).read_text()
 expected_diff.extend(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='machinery_reference/'+name,tofile=name))
assert (D/'CODE_FULL_DIFF.patch').read_text()==''.join(expected_diff)
for r in rd(D/'MACHINERY_SOURCE_PINS.json')['sources']:same(r['source'],r);same(D/r['recovery_path'],r)
receipts=[]
for mode in ('build','inspection','seal'):
 run=D/'metadata_runs'/mode;r=rd(run/'EXECUTION.json');launch=rd(run/'LAUNCH.json')
 assert all(r[k]==v for k,v in launch.items())
 assert r['exit_code']==0 and not r['timed_out'] and r['scientific_programs_run']==0 and r['timeout_seconds']==60
 assert r['started_utc']<=r['finished_utc'] and r['elapsed_seconds']>=0
 for k in ('child_source_at_launch','original_source_at_launch','source_capture','recorder_at_launch','input_identities_at_launch','stdout','stderr'):same(r[k]['path'],r[k])
 assert r['argv'][1]=='-B' and r['argv'][2]==r['child_source_at_launch']['path'] and r['argv'][3:]==[str(D)] and r['cwd']==str(D)
 assert r['original_source_at_launch']['sha256']==r['child_source_at_launch']['sha256']
 assert r['original_source_at_launch']['path']!=r['child_source_at_launch']['path']
 assert r['inputs_unchanged_after_run'] and (run/'stderr').read_bytes()==b''
 for row in rd(r['input_identities_at_launch']['path']):same(row['path'],row)
 receipts.append(pin(run/'EXECUTION.json'))
v=rd(D/'VERIFICATION.json');assert v==rd(D/'metadata_runs/inspection/stdout')
mut=v['scoped_metadata_mutants']+v['direct_receipt_predicate_mutants']
assert len(mut)==40 and all(r['rejected'] for r in mut)
assert not v['mathematics_tested_by_this_execution'] and v['historical_scientific_replays']==0
assert v['checked']['negative_packet_status']=='N1FAIL'
required=[]
prose='''# Root source-publication review: supplied commuting static edge

Qualified source integration is approved at this exact source freeze, with five complete unchanged bodies. Canonical/base/staged reviews and publication remain pending; this is not a retained audit verdict.

Root read all five new publication prose files, the complete new builder, primary template, inspector, recorder, sealer and preparation helper, read guides and recovery disclosure, and all three actual execution receipts with complete streams. The first combined display truncated a builder segment; the complete builder and primary were then read in a bounded call. A guessed previous-recorder filename did not exist; rg located the real source. These are read/discovery limits, not scientific executions. Full module contents include all changed globals and receipt logic. Exact generated-primary literals, complete diff reconstruction, source copies and function reuse were mechanically checked. The large report is fully preserved and hash-bound, not described as manually reread digit by digit or scientifically replayed.

The five mathematical/source bodies were already fully examined for root scientific acceptance f954c36d, controlled by qualifications ef9f0787. Their exact byte intervals remain unchanged. The positive supplied interaction B=(pi-atan(4/3))(I+XX)/T realizes one fixed full-matrix target while literal K=2I+ZZ continues aging. The supplied extra old-edge XX coupling is outside the four onsite rays. All scalar action, incident caps, state-dependent energy and covariance, finite quiet window, and sufficient calibration bounds are retained. The optional external ramp cycle is a separate driven model, not autonomous halt. No mediator or arbitrary-target theorem is composed.

One historical author exact-rational fixture ran0.18528820807114244 seconds, exit0/no timeout, under60 seconds wall limit with no OS CPU/RAM quota. Its60 finite checks and recorded operation/bit counts are distinguished from analytical premises and a separate source-exposed same-model analytical check. There is no second independent scientific execution or blind/model-family check.40 source-wrapper controls concern provenance only. Original failed edits, historical pending language, exact heterogeneous receipt schemas, missing legacy cwd and separately captured original-file launches remain honest.

The narrow static-X determinant invariant is valid for its stated family. Its negative packet remains N1FAIL partial-attempt-with-named-untested-routes; neither the accepted positive construction nor successful packaging changes that disposition. No broader no-go or retained negative authority is conferred. New coupling supply, preparation/installation apparatus, internal timing, physical calibration, exact halt and reuse remain open.

The displayed K,W,T and elementary finite matrix calculation suffice as explicit problem data. The earlier onsite target theorem is context only; Git transport from PR9653 is not a mathematical dependency. Proposed canonical graph disposition is one new mathematical root with zero direct theorem-parent edges, subject to actual graph verification preserving all old graph data. No substantive source correction is required; later binding-status/offset/literal changes must be separately exposed. No physical axiom, editable prompt, model or reasoning setting changed.
'''
O.mkdir();(O/'REVIEW.md').write_text(prose)
ev=dict(utc=datetime.now(timezone.utc).isoformat(),exact_freeze_members=179,immutable_bodies=5,source_aliases=153,archive_objects=84,exact_function_reuses=19,metadata_mutants=40,receipts=receipts,complete_new_code_and_prose_read=True,complete_metadata_streams_read=True,scientific_executions=0,required_canonical_replacements=required)
put(O/'MECHANICAL_EVIDENCE.json',ev)
r=dict(kind='root_qualified_source_publication_review',utc=datetime.now(timezone.utc).isoformat(),root_read_complete=True,disposition='QUALIFIED_SOURCE_INTEGRATION_APPROVED_CANONICAL_CHECKS_PENDING',source_freeze=pin(D/'FINAL_FREEZE.json'),source_note=pin(note),source_validator=pin(primary),source_manifest=pin(PK/'SOURCE_MANIFEST.json'),source_wrapper=pin(D/'packet_text/WRAPPER.md'),review=pin(O/'REVIEW.md'),evidence=pin(O/'MECHANICAL_EVIDENCE.json'),immutable_bodies=5,source_aliases=153,archive_objects=84,metadata_receipts=receipts,scientific_executions=0,actual_canonical_acceptance=None,actual_publication=None,retained_audit=False,required_canonical_replacements=required,proposed_graph_disposition='one_new_root_zero_direct_parent_edges',editable_prompt_files_changed=[])
put(O/'REVIEW.json',r);put(O/'FREEZE.json',dict(utc=datetime.now(timezone.utc).isoformat(),members=[dict(pin(O/n),path=n) for n in ('REVIEW.md','MECHANICAL_EVIDENCE.json','REVIEW.json')]))
print(json.dumps(dict(review=pin(O/'REVIEW.json'),freeze=pin(O/'FREEZE.json'),science_executions=0)))
