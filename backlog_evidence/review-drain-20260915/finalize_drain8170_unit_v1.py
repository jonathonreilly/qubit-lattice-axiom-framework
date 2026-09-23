"""Bind exact independently accepted PR8170 source and actual versioned captures. No science execution/verdict."""
from pathlib import Path
import hashlib,json,subprocess
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
dp=R/'drain8170-author-unit-draft-v1.json';fp=R/'drain8170-author-final-freeze.json';rp=R/'drain8170-final-review.json'
d=json.loads(dp.read_text());f=json.loads(fp.read_text());v=json.loads(rp.read_text())
assert sha(rp)=='04172d3763aa51bfae72fe23d73917f284eb61eeb5572c757948e6226f2fc8e9'
assert v['decision']=='SCIENCE_EVIDENCE_ACCEPTED' and not v['blockers'] and v['same_original_session']
assert v['reviewer_session']=='/root/review_8170' and v['tree']==f['tree']==git('write-tree') and v['source_hashes']==f['source_paths']
assert not git('diff','--name-only')
for p,h in (f['source_paths']|f['inputs']).items():assert sha(W/p)==h,p
refs=[d['reviewer']['report'],*d['reviewer']['references'],ref(dp),ref(fp)]
for e in f['executions']:
 p=Path(e['receipt']);assert sha(p)==e['sha256'];x=json.loads(p.read_text());assert x['error'] is None;refs += [ref(p),x['adapter'],*x['artifacts']]
refs += v['references']
unique={}
for e in refs:
 p=Path(e['path']);assert p.is_relative_to(R) and sha(p)==e['sha256'],p
 assert str(p) not in unique or unique[str(p)]['sha256']==e['sha256'];unique[str(p)]={'path':str(p),'sha256':e['sha256']}
for row in v['original_dispositions']:
 assert 'final_path' in row and 'final_sha256' in row
 if row['final_path'] is not None:assert f['source_paths'][row['final_path']]==row['final_sha256']
d['source'].update(tree=f['tree'],paths=[dict(path=p,sha256=h) for p,h in sorted(f['source_paths'].items())])
d['reviewer'].update(report=ref(rp),session=v['reviewer_session'],references=list(unique.values()))
for c in d['constituents']:c['dispositions']=dict(ref(rp),json_pointer='/original_dispositions')
for n in d['non_science_notes']:n['review_reference']=ref(rp)
for p in d.get('supporting_proofs',[]):p['review_reference']=ref(rp)
out=R/'drain8170-unit-final.json';assert not out.exists();out.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(ref(out)));print('paths',len(f['source_paths']),'refs',len(unique))
