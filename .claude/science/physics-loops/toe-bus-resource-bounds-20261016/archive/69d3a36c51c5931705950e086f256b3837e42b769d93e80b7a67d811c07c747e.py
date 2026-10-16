from pathlib import Path
import datetime, hashlib, json
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023');P=N/'reachable_bus_resource_candidate';R=N/'reachable_bus_resource_root_review'
def read(p):return json.loads(Path(p).read_text())
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
freeze=read(P/'FREEZE.json')
for row in freeze['members']:
 actual=pin(P/row['path']);assert actual['bytes']==row['bytes'] and actual['sha256']==row['sha256'],row['path']
manifest=read(P/'SOURCE_MANIFEST.json')
for row in manifest['sources']:
 for path in (Path(row['source']),P/row['capture']):
  actual=pin(path);assert actual['bytes']==row['bytes'] and actual['sha256']==row['sha256'],path
assert pin(P/'DERIVATION.md')['sha256']=='ce3ddd3ad376016f391992b30485454378607e6953fddcdeb2ecea702777d875'
assert pin(P/'FREEZE.json')['sha256']=='1eb2a662f00fe01c6d2bcee35c8039d0038001ed9a694980f6a5dbc9325a8996'
proposal=N/'reachable_bus_resource_root_proposal/CONDITIONAL_LEDGER.md'
assert pin(proposal)['sha256']=='fbd9c4471e0869bc260f26d608ca96b653cd3295f89c26a8359355fd1964a8a5'
out=R/'QUALIFIED_ACCEPTANCE.json';assert not out.exists()
record=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='Qualified source accepted; fixed-strong-plant nominal duration and precision requests only, unpublished.',
 candidate=pin(P/'DERIVATION.md'),candidate_freeze=pin(P/'FREEZE.json'),
 independently_frozen_root_derivation=pin(proposal),root_proposal_freeze=pin(proposal.parent/'FREEZE.json'),
 controlling_qualifications=pin(R/'FINAL_QUALIFICATIONS.md'),
 reachable_acceptance=pin(N/'reachable_bus_corrector_root_review/QUALIFIED_ACCEPTANCE.json'),
 full_new_argument_read=True,freeze_members_verified=len(freeze['members']),source_originals_and_captures_verified=len(manifest['sources']),
 scientific_executions=0,historical_science_replayed=0,retained_audit=False,
 resource_power='72q^2+260q+122 for q=d(d-1)/2; fixed plant and fixed graph only.',
 independent_check_limit='Same model; separately frozen root resource derivation and full new argument review. Worker authored the earlier bus; no fresh independent parent revalidation.',
 open_uniformity='Equation36: complete constant package for shrinking bias; old spectral bounds alone insufficient.',editable_prompt_files_changed=[])
out.write_text(json.dumps(record,indent=2)+'\n')
(R/'FREEZE.json').write_text(json.dumps(dict(utc=record['utc'],members=[pin(q) for q in (out,R/'FINAL_QUALIFICATIONS.md',Path(__file__))],scientific_executions=0,retained_audit=False),indent=2)+'\n')
print(json.dumps(dict(acceptance=pin(out),freeze=pin(R/'FREEZE.json'))))
