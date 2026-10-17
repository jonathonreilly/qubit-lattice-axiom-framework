"""Record root's completed source-wrapper/code review; metadata only, no historical execution."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,sys
N=Path(__file__).resolve().parents[1]
family=sys.argv[1];assert family in ('interacting','angle')
config={
 'interacting':('interacting_control_qualified_publication_draft','FREEZE.json','a82254aa003e3de63109e532adca46c771ec122d910528e9f9ff0f9e2e8996e2','root_interacting_control_qualified_publication_review','INTERACTING_PREPARATION_CONTROL_WORK_BOUNDED_THEOREM_NOTE_2026-10-16.md','interacting_preparation_control_work_2026_10_16.py','toe-interacting-preparation-control-work-20261016',9,219,120,7),
 'angle':('preparation_angle_moment_qualified_publication_draft','FINAL_FREEZE.json','6c55ee7b38717a52a8784d058d996989eecf6b1e3171bf88adacf168a1a007a3','root_preparation_angle_moment_qualified_publication_review','PREPARATION_ANGLE_ENERGY_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-16.md','preparation_angle_energy_moments_2026_10_16.py','toe-preparation-angle-energy-moments-20261016',3,45,32,14)
}[family]
folder,seal,seal_hash,destination,note_name,script_name,packet_name,nb,ns,na,nm=config
D=N/folder;O=N/destination;P=D/'proposal';PK=P/'.claude/science/physics-loops'/packet_name
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(p):return json.loads(Path(p).read_text())
def same(p,row):assert all(pin(p)[k]==row[k] for k in ('bytes','sha256')),str(p)
assert not O.exists()
assert pin(D/seal)['sha256']==seal_hash
frozen=read(D/seal);members=frozen['members']
assert len({r['path'] for r in members})==len(members)
for row in members:same(D/row['path'],row)
actual={str(p.relative_to(D)) for p in D.rglob('*') if p.is_file() and p!=D/seal}
assert actual=={r['path'] for r in members},'Exact source packet membership'
manifest=read(PK/'INPUT_MANIFEST.json')
for row in manifest['inputs']:same(P/row['path'],row)
note=P/'docs'/note_name;raw=note.read_bytes();body_map=read(PK/'BODY_MAP.json')
assert raw[:body_map['new_wrapper_bytes'][1]]==(D/'packet_text/WRAPPER.md').read_bytes()
assert len(body_map['bodies'])==nb
for row in body_map['bodies']:
 body=raw[row['start_byte_inclusive']:row['end_byte_exclusive']]
 assert len(body)==row['bytes'] and hashlib.sha256(body).hexdigest()==row['sha256']
 assert body==(N/row['source']).read_bytes() and raw.count(body)==1
sources=read(PK/'SOURCE_MANIFEST.json')['sources'];archive=read(PK/'ARCHIVE_INDEX.json')['objects']
assert len(sources)==ns and len(archive)==na
assert {r['sha256'] for r in sources}=={r['sha256'] for r in archive}
for row in sources:same(Path(row['original_path']),row);same(P/row['recovery_path'],row)
for row in archive:same(P/row['path'],row)
template=(D/'primary_template.py').read_text()
generated=template.replace('__MANIFEST_SHA256__',pin(PK/'INPUT_MANIFEST.json')['sha256']).replace('__AUDIT_INPUT_PATHS__',repr([r['path'] for r in manifest['inputs']]+[str((PK/'INPUT_MANIFEST.json').relative_to(P))])).replace('__EXPECTED_BODIES__',repr({r['name']:r['sha256'] for r in body_map['bodies']}))
primary=P/'scripts'/script_name;assert primary.read_text()==generated
for name in ('build_packet.py','primary_template.py','inspect_packet.py','record_metadata.py','seal_packet.py'):ast.parse((D/name).read_text())
receipts=[]
for mode in ('build','inspection','seal'):
 run=D/'metadata_runs'/mode;r=read(run/'EXECUTION.json');launch=read(run/'LAUNCH.json')
 assert all(r[k]==v for k,v in launch.items())
 assert r['exit_code']==0 and r['timed_out'] is False and r['scientific_programs_run']==0
 assert r['started_utc']<=r['finished_utc'] and r['elapsed_seconds']>=0
 for key in ('stdout','stderr'):same(r[key]['path'],r[key])
 assert (run/'stderr').read_bytes()==b''
 if family=='interacting' and mode=='seal':
  key='source_and_launcher_at_launch';same(r[key]['path'],r[key]);same(D/'seal_packet.py',r[key])
  assert r['argv'][2]==r[key]['path'] and r['argv'][3:] == ['--validate',str(D)] and r['source_unchanged_after'] is True
 else:
  for key in ('child_source_at_launch','original_source_at_launch','recorder_at_launch','input_identities_at_launch'):same(r[key]['path'],r[key])
  assert r['argv'][2]==r['child_source_at_launch']['path'] and r['argv'][3:]==[str(D)]
  assert r['original_source_at_launch']['sha256']==r['child_source_at_launch']['sha256']
  assert r['original_source_at_launch']['path']!=r['child_source_at_launch']['path'] and r['inputs_unchanged_after_run'] is True
  for row in read(r['input_identities_at_launch']['path']):same(row['path'],row)
 assert r['argv'][1]=='-B' and r['cwd']==str(D)
 receipts.append(pin(run/'EXECUTION.json'))
result=read(D/'VERIFICATION.json');assert result==read(D/'metadata_runs/inspection/stdout')
mutants=result['scoped_metadata_mutants']+result.get('direct_receipt_predicate_mutants',[])
assert len(mutants)==nm and all(m['rejected'] for m in mutants)
assert result['mathematics_tested_by_this_execution'] is False and result['historical_scientific_replays']==0
if family=='interacting':
 specific='''The nine complete scientific bodies reuse the already read, qualified bridge, actual preparation chronology and coherent runtime-fault arguments. Root read all new wrapper and PR prose, binding contract and source-specific primary/build/inspection/recorder/seal code completely. The wrapper correctly preserves the full literal interacting K, forward ramp order, target L_b* V E_p* R_b*, full scalar, independent vacuum and all resource/reference outputs. It makes M=L+2 and sufficiently-large idle intervals controlling corrections without rewriting original bodies. Supplied positive complements on their actual supports and complete control alphabet remain explicit. Runtime charge-based work bounds are not transferred through preparation. Baseline energy, restored-endpoint drive work, absolute work and microscopic apparatus remain distinct. Fixed-q laboratory epsilon^-4 excludes classical synthesis.

The historical bridge is one source-exposed complex128 fixture with uncertified midpoint ramps and an unhelpful small-packet accuracy bound. Preparation and fault-work extensions are analytical only. Root reused exact previous complete argument/review coverage; no numerical program was replayed. Shared authorship/source exposure is not blind independence. Seven observed packaging refusals verify scoped provenance only. The original missing source-at-launch/launcher limitations and failed pin transcription remain intact; actual root records are distinct from publication approval. Direct mathematical parents are preparation6db93809 and combd88f51f5. Actual parent PR9648 publication/attachment is archived separately and its live status can change before integration.
'''
else:
 specific='''The three complete scientific bodies reuse the already read proposal, exposed analytical review and controlling root qualifications. Root read the entire new wrapper, proposed PR, binding/status/evidence prose and primary/build/inspection/recorder/seal code. The restricted deterministic angle-only vacuum trajectory, exact old isolation, all full physical outputs and reference remain explicit. Reverse-hybrid response uses earlier nominal and later actual gates; eta is vector/action and 2eta is unhalved trace. Raw, variance and complete F0 cross moments retain their separate constants and product assumptions. Positive angle increment and positive reserved actual pulse are distinguished from the indefinite additive residual. Generic coupled faults and native suppliers remain outside scope.

The finite lower family keeps its even-L thresholds, constants192/384/768 and separate trace convention. Sufficient total/per-angle allocations are not promoted to universal necessity. Net modeled work does not price absolute work, temporary controls or microscopic drive outputs. Exact carriers and endpoint phase remain supplied and paid. The sole direct mathematical parent is the preparation note6db93809; other interacting and comb results are context or ancestry only. Fourteen observed metadata controls include direct receipt predicates independent of outer hashes. Both original failed and corrected acceptance runs remain immutable with actual source/capture paths and complete streams. Root reused the complete previous mathematical coverage at exact identities; no science computation, fixture replay or formal proof occurred. The review remains same-model, source-exposed and not blind.
'''
prose='''# Root source-publication review

Disposition: qualified source integration approved; actual canonical checks and publication remain pending. This decision applies to this exact source freeze and the new connective prose/metadata machinery, not to an unseen canonical diff. Immutable body identities preserve previous source decisions; archived pending labels remain historical.

'''+specific+'''
Root also inspected the three actual packaging execution schemas and complete stdout; each stderr is empty. The deterministic checks below verify current exact membership, original/recovery bytes, source intervals, template generation and actual launch/source/stream linkage. They do not establish mathematics. Every source-only future binding remains null and the primary's normal entry point refuses. Later phases must supply their own real base/tool/parent observations, canonical and staged review and execution evidence; no Boolean manufactures those phases.

No new source correction is required by this review. No canonical installation, cache, graph, PR, merge, retained audit, physical axiom or editable prompt change is performed by recording it. Native control/vacuum/clock resources, autonomous release/halt and indefinite reuse remain unresolved. The current model and reasoning effort were preserved.
'''
O.mkdir()
(O/'REVIEW.md').write_text(prose)
evidence=dict(utc=datetime.now(timezone.utc).isoformat(),family=family,exact_freeze_members=len(members),immutable_bodies=nb,source_aliases=ns,archive_objects=na,packaging_metadata_mutants=nm,receipts=receipts,code=[pin(D/name) for name in ('build_packet.py','primary_template.py','inspect_packet.py','record_metadata.py','seal_packet.py')],unchanged_body_map=pin(PK/'BODY_MAP.json'),full_stdout_read=True,stderr_empty=True,scientific_executions=0,historical_scientific_replays=0)
(O/'MECHANICAL_EVIDENCE.json').write_text(json.dumps(evidence,indent=2)+'\n')
review=dict(kind='root_qualified_source_publication_review',utc=datetime.now(timezone.utc).isoformat(),root_read_complete=True,disposition='QUALIFIED_SOURCE_INTEGRATION_APPROVED_CANONICAL_CHECKS_PENDING',source_freeze=pin(D/seal),source_note=pin(note),source_validator=pin(primary),source_manifest=pin(PK/'SOURCE_MANIFEST.json'),source_wrapper=pin(D/'packet_text/WRAPPER.md'),review=pin(O/'REVIEW.md'),evidence=pin(O/'MECHANICAL_EVIDENCE.json'),immutable_bodies=nb,source_aliases=ns,archive_objects=na,metadata_receipts=receipts,scientific_executions=0,actual_canonical_acceptance=None,actual_publication=None,retained_audit=False,editable_prompt_files_changed=[])
(O/'REVIEW.json').write_text(json.dumps(review,indent=2)+'\n')
(O/'FREEZE.json').write_text(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),members=[dict(pin(O/name),path=name) for name in ('REVIEW.md','MECHANICAL_EVIDENCE.json','REVIEW.json')]),indent=2)+'\n')
print(json.dumps(dict(review=pin(O/'REVIEW.json'),freeze=pin(O/'FREEZE.json'),evidence=pin(O/'MECHANICAL_EVIDENCE.json'),scientific_executions=0)))
