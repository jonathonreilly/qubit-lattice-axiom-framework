"""Record completed root source-publication review; metadata only."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json
N=Path(__file__).resolve().parents[1]
D=N/'endpoint_chart_recurrence_qualified_publication_draft';P=D/'proposal'
PK=P/'.claude/science/physics-loops/toe-positive-onsite-endpoint-chart-recurrence-20261016'
O=N/'root_endpoint_chart_recurrence_qualified_publication_review'
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def rd(p):return json.loads(Path(p).read_text())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
def put(p,d):p.write_text(json.dumps(d,indent=2)+'\n')
assert not O.exists()
assert pin(D/'FINAL_FREEZE.json')['sha256']=='996e7619f1bd198225d245a211d48420c8d6ef6ed0ffe10f21743966c59cc326'
f=rd(D/'FINAL_FREEZE.json');members=f['members'];assert len(members)==216
for r in members:same(D/r['path'],r)
assert {str(p.relative_to(D)) for p in D.rglob('*') if p.is_file()}=={r['path'] for r in members}|{'FINAL_FREEZE.json'}
m=rd(PK/'INPUT_MANIFEST.json')
for r in m['inputs']:same(P/r['path'],r)
note=P/'docs/POSITIVE_ONSITE_ENDPOINT_CHART_RECURRENCE_BOUNDED_THEOREM_NOTE_2026-10-16.md'
primary=P/'scripts/positive_onsite_endpoint_chart_recurrence_2026_10_16.py'
raw=note.read_bytes();bm=rd(PK/'BODY_MAP.json')
assert raw[:bm['new_wrapper_bytes'][1]]==(D/'packet_text/WRAPPER.md').read_bytes()
assert len(bm['bodies'])==9
for r in bm['bodies']:
 b=raw[r['start_byte_inclusive']:r['end_byte_exclusive']]
 assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
 assert b==(N/r['source']).read_bytes() and raw.count(b)==1
sources=rd(PK/'SOURCE_MANIFEST.json')['sources'];objects=rd(PK/'ARCHIVE_INDEX.json')['objects']
assert len(sources)==231 and len(objects)==148
for r in sources:same(r['original_path'],r);same(P/r['recovery_path'],r)
for r in objects:same(P/r['path'],r)
assert {r['sha256'] for r in sources}=={r['sha256'] for r in objects}
freezes=rd(PK/'FROZEN_SOURCE_CLOSURE.json')['roots'];assert len(freezes)==7
acceptances={'endpoint_chart_root_review/ACCEPTANCE.json':'112ecd184bf4e0fbb76814c73bffe0fa911b35ba808825e09bb574c790f6faf7','endpoint_recurrence_root_review/ACCEPTANCE.json':'36e72537f8d2546bc15c9baf69dd526fb22d854bafc36d07a020a7225c73465e'}
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
assert verified==16
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
assert len(mut)==27 and all(r['rejected'] for r in mut)
assert not v['mathematics_tested_by_this_execution'] and v['historical_scientific_replays']==0
required=[{'before':'A fixed nonzero calibration floor\ndoes not allow arbitrary final precision.','after':'The stated worst-case error bound does not certify arbitrary final precision at a fixed nonzero calibration error floor.'}]
assert raw.decode().count(required[0]['before'])==1
assert required==rd(N/'endpoint_chart_recurrence_integration_proposal/WRAPPER_REPLACEMENTS.json')[:1]
prose="""# Root source-publication review

Qualified source integration is approved only with the exact canonical wrapper replacement recorded below. Actual integration, base observations, canonical and staged review and publication remain pending. This records no audit verdict.

Root read the complete five new publication prose files, primary template, builder, inspector, metadata recorder and sealer, and all three actual execution records and complete stdout/stderr. Nine original scientific bodies were already read in full for the separate chart and recurrence decisions; their exact identities and controlling qualifications remain unchanged. Current closure, source/recovery identity, function reuse, generated primary literals and launch/stream linkage were mechanically checked. These metadata checks establish no additional mathematics.

The full-U4 chart is conditional on the specified two-qubit K=2I+ZZ, supplied positive onsite X/Y controls, exact tensor/drift interpretation and all original control, clock and isolation hypotheses. Its inverse and analytic enclosure bounds remain source-specific. The explicit recurrence uses the very large stated integer and complete scalar phase, with independent saved-product arithmetic but no second ODE implementation. It improves explicitness, not the existential duration bound. The universal consequence combines the chart with recurrence and effective target access; no executed nontrivial target word belongs to this packet.

The wrapper sentence asserting that a nonzero calibration floor forbids arbitrary final precision is too broad. The canonical wrapper must instead say that the stated worst-case bound does not certify it. Structured cancellation and alternative controls have not been excluded. Original source and all nine bodies stay immutable. Timing and amplitude estimates are sufficient upper-error budgets, not universal necessities.

Both original scientific attempts and separately exposed downstream arithmetic checks preserve source revisions, true launch captures, full streams, resource limits and scope. Packaging ran no science and replayed neither ODE nor recurrence. Same-model source exposure is explicit and is not blind independent replication. The zero direct canonical-parent set reflects a self-contained combined milestone; Git ancestors are not mathematical dependencies. Exact source-only null bindings remain historical; real later phases must provide their own receipts.

Native actuation, vacuum/coherence supply, physical clock and calibration resources, microscopic controller outputs, practical efficiency, autonomous halt and indefinite reuse remain unresolved. No formal retained status, experimental validation or physical realization follows. No editable prompts, physical axioms or model settings changed.
"""
O.mkdir();(O/'REVIEW.md').write_text(prose)
ev=dict(utc=datetime.now(timezone.utc).isoformat(),exact_freeze_members=216,immutable_bodies=9,source_aliases=231,archive_objects=148,exact_function_reuses=16,metadata_mutants=27,receipts=receipts,complete_new_code_and_prose_read=True,complete_metadata_streams_read=True,scientific_executions=0,required_canonical_replacements=required)
put(O/'MECHANICAL_EVIDENCE.json',ev)
r=dict(kind='root_qualified_source_publication_review',utc=datetime.now(timezone.utc).isoformat(),root_read_complete=True,disposition='QUALIFIED_SOURCE_INTEGRATION_APPROVED_CANONICAL_CHECKS_PENDING',source_freeze=pin(D/'FINAL_FREEZE.json'),source_note=pin(note),source_validator=pin(primary),source_manifest=pin(PK/'SOURCE_MANIFEST.json'),source_wrapper=pin(D/'packet_text/WRAPPER.md'),review=pin(O/'REVIEW.md'),evidence=pin(O/'MECHANICAL_EVIDENCE.json'),immutable_bodies=9,source_aliases=231,archive_objects=148,metadata_receipts=receipts,scientific_executions=0,actual_canonical_acceptance=None,actual_publication=None,retained_audit=False,required_canonical_replacements=required,editable_prompt_files_changed=[])
put(O/'REVIEW.json',r);put(O/'FREEZE.json',dict(utc=datetime.now(timezone.utc).isoformat(),members=[dict(pin(O/n),path=n) for n in ('REVIEW.md','MECHANICAL_EVIDENCE.json','REVIEW.json')]))
print(json.dumps(dict(review=pin(O/'REVIEW.json'),freeze=pin(O/'FREEZE.json'),science_executions=0)))

