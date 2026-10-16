from pathlib import Path
import datetime, hashlib, json
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023')
P=N/'bus_preparation_exposed_check'; C=N/'bus_installed_preparation_candidate'; R=N/'bus_preparation_root_review'
def pin(p):
 p=Path(p); b=p.read_bytes(); return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(p):return json.loads(Path(p).read_text())
def verify(row):
 q=Path(row['path']); a=pin(q); assert a['bytes']==row['bytes'] and a['sha256']==row['sha256'],q
for folder in (P,C):
 for row in read(folder/'FREEZE.json')['members']:verify(row)
assert pin(C/'DERIVATION.md')['sha256']=='71e9ec899920fdbb9af3ef56176550bffdfb8d8b77a300d6caa560a90009af29'
assert pin(P/'REVIEW.md')['sha256']=='8b3daec28d23ee89ddaa44c51e219c52978607687ea9458c6bb289fcb9068fc8'
for row in read(P/'SOURCE_MANIFEST.json')['sources'].values():
 for field in ('original','captured'):assert pin(row[field])['sha256']==row['sha256']
for name in ('run_001','run_002_provenance'):
 d=P/name; launch=read(d/'LAUNCH.json'); e=read(d/'EXECUTION.json')
 assert e['exit_code']==0 and not e['timed_out'] and e['argv']==launch['argv'] and e['cwd']==launch['cwd']
 for file,key in [('executed_source.py','source_at_launch_sha256'),('launcher_at_launch.py','launcher_at_launch_sha256')]:assert pin(d/file)['sha256']==launch[key]
 for file,key in [('stdout.json','stdout_sha256'),('stderr.txt','stderr_sha256')]:assert pin(d/file)['sha256']==e[key]
analytic=(P/'ANALYTIC_FINDINGS.md').read_text()
assert analytic[70:] in (P/'REVIEW.md').read_text()
assert pin(P/'ANALYTIC_FINDINGS.md')['sha256']==read(P/'ANALYTIC_FINDINGS_FREEZE.json')['sha256']
assert pin(R/'ANALYTIC_RECONSTRUCTION.md')['sha256']=='cb0fcf69047b0e8ee803e51eaaf1b4d34934463ba1f301b3ad3342226703dba9'
out=R/'QUALIFIED_ACCEPTANCE.json';assert not out.exists()
record=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 status='Accepted conditional driven preparation/release composition with controlling qualifications; unpublished and unaudited.',
 candidate=pin(C/'DERIVATION.md'),candidate_freeze=pin(C/'FREEZE.json'),
 exposed_review=pin(P/'REVIEW.md'),review_freeze=pin(P/'FREEZE.json'),
 root_reconstruction=pin(R/'ANALYTIC_RECONSTRUCTION.md'),root_reconstruction_freeze=pin(R/'ANALYTIC_RECONSTRUCTION_FREEZE.json'),
 controlling_qualifications=pin(R/'FINAL_QUALIFICATIONS.md'),
 actual_scientific_execution=pin(P/'run_001/EXECUTION.json'),actual_provenance_execution=pin(P/'run_002_provenance/EXECUTION.json'),
 source_identity_members_verified=dict(candidate=len(read(C/'FREEZE.json')['members']),review=len(read(P/'FREEZE.json')['members'])),
 full_changed_arguments_read=True,root_new_scientific_executions=0,
 independent_check_limit='Source-exposed, same model; separately authored exact finite algebra and analytic derivation, not full runtime revalidation or retained audit.',
 accepted_refinement='Reviewer general off-code density leakage (N-2)(N+1)/(16N), independently reconstructed algebraically by root.',
 required_clarification='2 nu A_u assumes an additive full operator norm bound. Relative amplitude error requires 2 nu ||Gamma|| A_u.',
 retained_audit=False,editable_prompt_files_changed=[])
out.write_text(json.dumps(record,indent=2)+'\n')
files=[out,R/'FINAL_QUALIFICATIONS.md',R/'ANALYTIC_RECONSTRUCTION.md',R/'ANALYTIC_RECONSTRUCTION_FREEZE.json',Path(__file__)]
(R/'FREEZE.json').write_text(json.dumps(dict(utc=record['utc'],members=[pin(p) for p in files],scientific_executions=0,retained_audit=False),indent=2)+'\n')
print(json.dumps(dict(acceptance=pin(out),freeze=pin(R/'FREEZE.json'))))
