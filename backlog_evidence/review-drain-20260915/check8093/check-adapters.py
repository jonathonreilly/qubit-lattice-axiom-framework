from pathlib import Path
from types import SimpleNamespace
import tempfile,hashlib
r=Path('/private/tmp/review-drain-20260915');a=(r/'prepare_candidate_typed.py').read_text();b=(r/'finish_candidate_typed.py').read_text()
prep=a[a.index('non_science_expectations={}'):a.index("record={'base':")]
finish=b[b.index("non_science_expectations=r.get"):b.index('assert len(science)==a.notes')]
passed=[]
with tempfile.TemporaryDirectory(dir=r/'check8093') as td:
 root=Path(td);(root/'note.md').write_text('meta');(root/'review.json').write_text('review')
 digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();h=digest(root/'note.md');rh=digest(root/'review.json')
 def runprep(mode):
  ex={'claim_type':'meta','review':'review.json','sha256':h};u={'procedural_only':True,'source_paths':{'note.md':h},'procedural_review':'review.json','review_evidence_hashes':{'review.json':rh},'non_science_expectations':{'note.md':ex}}
  typ=('meta','meta')
  if mode=='type':typ=('bounded_theorem','bounded_theorem')
  if mode=='hash':ex['sha256']='wrong'
  if mode=='review':ex['review']='absent'
  if mode=='procedural':u['procedural_only']=False
  ns={'collection':{'units':[u]},'root':root,'sha':digest,'graph':SimpleNamespace(extract_claim_type_hint=lambda _:typ)};exec(compile(prep,'actual-prepare-block','exec'),ns)
 def runfinish(mode):
  expected={'claim_type':'meta','review':'review.json','sha256':h};record={'source_owners':{'note.md':'unit'},'review_evidence_hashes':{'review.json':rh},'non_science_expectations':{'note.md':expected}};affected={'m':{'note_path':'note.md','claim_type':'meta','audit_status':'unaudited'},'s':{'note_path':'science.md','claim_type':'bounded_theorem','audit_status':'unaudited'}}
  if mode=='type':affected['m']['claim_type']='bounded_theorem'
  if mode=='status':affected['m']['audit_status']='retained'
  if mode=='duplicate':affected['dup']=dict(affected['m'])
  if mode=='missing':del affected['m']
  if mode=='hash':expected['sha256']='wrong'
  ns={'r':record,'affected':affected,'root':root,'out':root,'digest':digest};exec(compile(finish,'actual-finish-block','exec'),ns);assert set(ns['science'])=={'s'}
 for fn,modes in [(runprep,['good','type','hash','review','procedural']),(runfinish,['good','type','status','duplicate','missing','hash'])]:
  for mode in modes:
   try:fn(mode)
   except AssertionError:
    assert mode!='good';passed.append(fn.__name__+':'+mode+':rejected')
   else:assert mode=='good';passed.append(fn.__name__+':good')
print('\n'.join(passed));print('checks',len(passed))
