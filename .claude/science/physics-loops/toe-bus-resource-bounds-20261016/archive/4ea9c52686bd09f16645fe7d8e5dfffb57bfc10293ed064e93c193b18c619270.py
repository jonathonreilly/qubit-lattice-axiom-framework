from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
O=Path(__file__).resolve().parent;N=O.parent;Q=N/'bus_bounded_slew_preparation_exposed_check';A=N/'bus_bounded_slew_preparation_root_proposal'
def read(p):return json.loads(Path(p).read_text())
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
assert pin(Q/'FREEZE.json')['sha256']=='6794345fce3b8f11bb990512de09c1f40893f290d00d8e0032005ed783757525'
f=read(Q/'FREEZE.json')
for r in f['files']:same(Q/r['path'],r)
for r in read(Q/'SOURCE_MANIFEST.json')['sources']:
 same(r['path'],r);same(Q/r['capture'],r)
r=read(Q/'run_001/EXECUTION.json');l=read(Q/'run_001/LAUNCH.json')
assert all(r[k]==v for k,v in l.items()) and r['exit_code']==0 and not r['timed_out']
assert r['start_utc']<=r['end_utc'] and r['elapsed_seconds']>0
for k in ['source_at_launch','source_capture','launcher_at_launch','launcher_capture','source_inputs','stdout','stderr']:same(r[k]['path'],r[k])
assert Path(r['stderr']['path']).read_bytes()==b''
assert read(r['stdout']['path'])==read(Q/'CHECK_RESULT.json')
assert r['argv'][1]=='-B' and r['argv'][2]==r['source_capture']['path']
assert pin(A/'PROPOSED_LEMMAS.md')['sha256']=='6e09476675188bc8053e2b3b00095db3eb5e1ebf59c816c923da0675a33edc44'
assert pin(Q/'REVIEW.md')['sha256']=='a1b9ef4621b2a4a420d86f30c16449273d0a0a4bc46f22d078a4b2884cbda1d1'
record=dict(utc=datetime.now(timezone.utc).isoformat(),kind='root_qualified_source_acceptance',disposition='Accepted conditional preparation with fixed per-site modeled strength/slew and explicitly evolved retained memory; not the earlier literal-Q comparator.',root_read_complete=True,proposal=pin(A/'PROPOSED_LEMMAS.md'),proposal_freeze=pin(A/'FREEZE.json'),review=pin(Q/'REVIEW.md'),review_freeze=pin(Q/'FREEZE.json'),controlling_qualifications=pin(O/'FINAL_QUALIFICATIONS.md'),parent_acceptance=pin(N/'bus_preparation_root_review/QUALIFIED_ACCEPTANCE.json'),parent_qualifications=pin(N/'bus_preparation_root_review/FINAL_QUALIFICATIONS.md'),review_execution=pin(Q/'run_001/EXECUTION.json'),source_manifest=pin(Q/'SOURCE_MANIFEST.json'),frozen_members_verified=len(f['files']),original_and_captured_sources_verified=6,verification_limits='One exposed same-model analytical review with separately written floating-point xi=0 discriminator; no blind replication, positive-xi physical simulation, derivative measurement, new root scientific execution or retained audit. Polynomial composition and native suppliers remain open.',accepted_refinements=['Noncircular uniform beta_bar before xi for optional moment tolerances.','Reference-valued moment operators retaining E conjugated by U_E.','Order-one literal-memory discrepancy despite equal ordinary moments.'],root_scientific_programs_run=0,retained_audit=False,editable_prompt_files_changed=[])
out=O/'QUALIFIED_ACCEPTANCE.json';assert not out.exists();out.write_text(json.dumps(record,indent=2)+'\n')
freeze=O/'FREEZE.json';assert not freeze.exists();freeze.write_text(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),files=[pin(out),pin(O/'FINAL_QUALIFICATIONS.md')],independent_retained_audit=False),indent=2)+'\n')
print(json.dumps(dict(acceptance=pin(out),freeze=pin(freeze))))

