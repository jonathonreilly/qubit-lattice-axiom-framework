"""Preserve the root's analytic judgment after exact source-identity verification."""
from pathlib import Path
import datetime,hashlib,json
O=Path(__file__).resolve().parent;N=O.parent;D=N/'shrinking_bias_resource_candidate';R=N/'shrinking_bias_resource_exposed_check'
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):
 b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=sha(b))
def read(p):return json.loads(p.read_text())
def write(p,obj):
 assert not p.exists(),str(p);p.write_text(json.dumps(obj,indent=2)+'\n')
def verify_folder(path,expected,key,count):
 assert sha((path/'FREEZE.json').read_bytes())==expected
 rows=read(path/'FREEZE.json')[key];assert len(rows)==count
 for x in rows:
  p=Path(x['path']);p=p if p.is_absolute() else path/p;b=p.read_bytes()
  assert len(b)==x['bytes'] and sha(b)==x['sha256'] and not p.is_symlink()
 assert {str(p.relative_to(path)) for p in path.rglob('*') if p.is_file()}=={x['path'] for x in rows}|{'FREEZE.json'}
def main():
 verify_folder(D,'8b96d1e0790c864a1caefe4a7035740e9c0835ebb943d4f0700d7c1f00aa43e2','members',33)
 verify_folder(R,'f62e621034d56367ebbadadd47048d4bfec90beb4161e8eaa69e4a001859da98','files',9)
 for folder,manifest,count in [(D,'SOURCE_MANIFEST.json',23),(R,'SOURCE_IDENTITIES.json',3)]:
  rows=read(folder/manifest)['sources'];assert len(rows)==count
  for row in rows:
   b=Path(row['source']).read_bytes();assert b==(folder/row['capture']).read_bytes()
   assert len(b)==row['bytes'] and sha(b)==row['sha256']
 assert pin(D/'DERIVATION.md')['sha256']=='2bfb24cce9760be23d750b3b2a190b3110bc0326c035488aae004d1de7849a74'
 assert read(R/'CHECKPOINT.json')['scientific_executions']==read(D/'FREEZE.json')['scientific_executions']==0
 result=dict(accepted_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='qualified conditional source acceptance; unpublished; not retained audit',
  controlling_qualifications=pin(O/'FINAL_QUALIFICATIONS.md'),candidate=pin(D/'DERIVATION.md'),candidate_freeze=pin(D/'FREEZE.json'),
  exposed_review=pin(R/'REVIEW.md'),review_freeze=pin(R/'FREEZE.json'),source_manifest=pin(D/'SOURCE_MANIFEST.json'),
  root_pre_result_sketch=pin(N/'shrinking_bias_resource_root_proposal/PRE_RESULT_SKETCH.md'),root_sketch_freeze=pin(N/'shrinking_bias_resource_root_proposal/FREEZE.json'),
  initial_source_verification=pin(O/'SOURCE_VERIFICATION.json'),
  claim='Uniform nominal runtime and numerical precision requests on the supplied admissible shrinking-bias domain; fixed-plant equation36 discharged conditionally.',
  runtime_exponent='P=2+4p+2*kappa*v; d=2 gives1078',
  source_checks=dict(candidate_members=33,author_sources=23,review_members=9,review_sources=3),
  scientific_executions=0,historical_scientific_replays=0,
  independence='Root unshared pre-result sketch; same-model author continuation; source-exposed same-model focused polynomial-basis derivative proof and precision recomputation. Not full parent validation or retained audit.',
  unresolved=['supplied admissible attenuable bias and physical access','native purity/phase/calibration/isolation','chronological preparation composition','physical energy identification','arbitrary oracle wall time','autonomous halt and reuse'],editable_prompt_files_changed=[])
 write(O/'QUALIFIED_ACCEPTANCE.json',result)
 write(O/'FREEZE.json',dict(frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),files=[pin(p) for p in sorted(O.iterdir()) if p.is_file()]))
 print(json.dumps(dict(acceptance=pin(O/'QUALIFIED_ACCEPTANCE.json'),freeze=pin(O/'FREEZE.json'),review=pin(R/'REVIEW.md'),candidate_members=33,review_members=9,scientific_executions=0)))
if __name__=='__main__':main()
