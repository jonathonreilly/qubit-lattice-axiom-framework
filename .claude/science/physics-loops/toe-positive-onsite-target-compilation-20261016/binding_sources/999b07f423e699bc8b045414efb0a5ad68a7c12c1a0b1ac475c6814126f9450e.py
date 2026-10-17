"""Record completed root source-publication review; metadata only."""
from pathlib import Path
from datetime import datetime,timezone
import ast,difflib,hashlib,json
N=Path(__file__).resolve().parents[1]
D=N/'endpoint_target_compilation_qualified_publication_draft';P=D/'proposal'
PK=P/'.claude/science/physics-loops/toe-positive-onsite-target-compilation-20261016'
O=N/'root_endpoint_target_compilation_qualified_publication_review'
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def rd(p):return json.loads(Path(p).read_text())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
def put(p,d):p.write_text(json.dumps(d,indent=2)+'\n')
assert not O.exists()
assert pin(D/'FINAL_FREEZE.json')['sha256']=='d8d497c515fa8f1eebf4f336a55435557cc3c8b60384f4a17a5ce2d40a8c37d7'
f=rd(D/'FINAL_FREEZE.json');members=f['members'];assert len(members)==263
for r in members:same(D/r['path'],r)
assert {str(p.relative_to(D)) for p in D.rglob('*') if p.is_file()}=={r['path'] for r in members}|{'FINAL_FREEZE.json'}
m=rd(PK/'INPUT_MANIFEST.json')
for r in m['inputs']:same(P/r['path'],r)
note=P/'docs/POSITIVE_ONSITE_TARGET_COMPILATION_BOUNDED_THEOREM_NOTE_2026-10-16.md'
primary=P/'scripts/positive_onsite_target_compilation_2026_10_16.py'
raw=note.read_bytes();bm=rd(PK/'BODY_MAP.json')
assert raw[:bm['new_wrapper_bytes'][1]]==(D/'packet_text/WRAPPER.md').read_bytes()
assert len(bm['bodies'])==6
for r in bm['bodies']:
 b=raw[r['start_byte_inclusive']:r['end_byte_exclusive']]
 assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
 assert b==(N/r['source']).read_bytes() and raw.count(b)==1
sources=rd(PK/'SOURCE_MANIFEST.json')['sources'];objects=rd(PK/'ARCHIVE_INDEX.json')['objects']
assert len(sources)==417 and len(objects)==192
for r in sources:
 if 'historical_version_recovered_from' in r:
  same(r['historical_version_recovered_from'],r)
  assert r['source'].startswith('historical_at_launch/'+r['sha256']+'/')
 else:same(r['original_path'],r)
 same(P/r['recovery_path'],r)
for r in objects:same(P/r['path'],r)
assert {r['sha256'] for r in sources}=={r['sha256'] for r in objects}
freezes=rd(PK/'FROZEN_SOURCE_CLOSURE.json')['roots'];assert len(freezes)==3
acceptances={'endpoint_target_compilation_root_review/ACCEPTANCE.json':'949d009ac768e72401c005b5cc7b0161ec93bbfdefdf004dc4b8300e0f140514'}
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
assert verified==20

expected_diff=[]
for name in ['build_packet.py','primary_template.py','inspect_packet.py','record_metadata.py','seal_packet.py']:
 old=(D/'machinery_reference'/name).read_text();new=(D/name).read_text()
 expected_diff.extend(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='machinery_reference/'+name,tofile=name))
assert (D/'CODE_FULL_DIFF.patch').read_text()==''.join(expected_diff)
for row in rd(D/'MACHINERY_SOURCE_PINS.json')['selected_files']:
 same(row['path'],row);same(D/row['recovery'],row)
assert len(reuse['functions'])==23
for row in rd(D/'OBSERVED_PARENT_PUBLICATION.json')['sources']:
 same(row['original_path'],row);same(D/row['copy'],row)
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
assert len(mut)==39 and all(r['rejected'] for r in mut)
assert not v['mathematics_tested_by_this_execution'] and v['historical_scientific_replays']==0
required=[]
prose="# Root source-publication review: complete fixed-target word\n\nQualified source integration is approved at the exact source freeze and six immutable bodies recorded here. Separate canonical/base/staged reviews and publication remain pending; no retained audit verdict is applied.\n\nRoot read all five new publication prose files, the entire builder/primary template/inspector/recorder/sealer, read maps and bookkeeping recovery, and all three actual packaging execution records with complete stdout/stderr. Six scientific bodies were already fully reviewed for acceptance949d and controlling qualifications3982. Their exact byte intervals remain unchanged. The new code's full module contents were read, including heterogeneous launch-schema handling and historical-version recovery. Exact diff/function correspondence and generated-primary literals are checked mechanically; large numeric evidence is preserved rather than claimed manually reread or rerun.\n\nThis single target is W=[(9+12i)I+(-16+12i)XX]/25 for literal K=2I+ZZ and four supplied positive onsite rays. The complete positive-time word, every scalar reserve, actual astronomical T and fixed M,n are retained. One actual461.2228-second author execution and one10.3879-second separately written source-exposed same-model Fraction check establish the stated computed scope. The checker reconstructs phases, coordinate pads,32 inverse updates,768 saved-slot products and41 final powers/residual, not a second local Taylor/ODE, nominal endpoint or recurrence. Trusted runtime and analytic enclosure premises remain explicit. Programmed operator error below2^-40 is distinct from actual physical faults and initial trace discrepancy.\n\nThe sole exact mathematical parent is the combined chart/recurrence noteab8fd20f. Its actual PR9652 publication is a context observation, not approval of this new wrapper. A later actual selected clean base and all canonical decisions require their own receipts. Effective arbitrary-target existence from the parent is not converted into an arbitrary-target compiled word by this fixed example.\n\nAll417 source aliases/192 unique objects, candidate132/checker256/root2 inventories,19 historical receipt contracts and terminal processes are preserved. Actual original launches and executed captures remain distinguished. The original root acceptance schema failure is still exit1, recovered under an explicit captured historical-version alias because its original path later changed. Distinct successful correction is exit0; no science retry occurred. Packaging's later tool-only table-key error is documented honestly without inventing separately captured streams or launch timing.39 packaging controls verify provenance, not science. Source-only nulls stay historical and the default primary intentionally refuses canonical execution.\n\nNo substantive scientific wording correction is required. Canonical binding-status/offset/literal adaptations must be exposed and reviewed separately. Physical controls, clock, precision, waveform and isolation remain supplied. Joint old/reference error includes full-generator/input/timing budgets. Net endpoint old workzero for this commuting W is distinct from absolute control variation and unmodeled microscopic expenditure. Native control supply, installer/controller outputs, practical duration, halt/reset and reuse remain unresolved; no physical realization or retained status is claimed. No editable prompts, physical axioms, model or reasoning settings changed.\n"
O.mkdir();(O/'REVIEW.md').write_text(prose)
ev=dict(utc=datetime.now(timezone.utc).isoformat(),exact_freeze_members=263,immutable_bodies=6,source_aliases=417,archive_objects=192,exact_function_reuses=20,metadata_mutants=39,receipts=receipts,complete_new_code_and_prose_read=True,complete_metadata_streams_read=True,scientific_executions=0,required_canonical_replacements=required)
put(O/'MECHANICAL_EVIDENCE.json',ev)
r=dict(kind='root_qualified_source_publication_review',utc=datetime.now(timezone.utc).isoformat(),root_read_complete=True,disposition='QUALIFIED_SOURCE_INTEGRATION_APPROVED_CANONICAL_CHECKS_PENDING',source_freeze=pin(D/'FINAL_FREEZE.json'),source_note=pin(note),source_validator=pin(primary),source_manifest=pin(PK/'SOURCE_MANIFEST.json'),source_wrapper=pin(D/'packet_text/WRAPPER.md'),review=pin(O/'REVIEW.md'),evidence=pin(O/'MECHANICAL_EVIDENCE.json'),immutable_bodies=6,source_aliases=417,archive_objects=192,metadata_receipts=receipts,scientific_executions=0,actual_canonical_acceptance=None,actual_publication=None,retained_audit=False,required_canonical_replacements=required,editable_prompt_files_changed=[])
put(O/'REVIEW.json',r);put(O/'FREEZE.json',dict(utc=datetime.now(timezone.utc).isoformat(),members=[dict(pin(O/n),path=n) for n in ('REVIEW.md','MECHANICAL_EVIDENCE.json','REVIEW.json')]))
print(json.dumps(dict(review=pin(O/'REVIEW.json'),freeze=pin(O/'FREEZE.json'),science_executions=0)))

