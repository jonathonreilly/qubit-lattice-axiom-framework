"""Bind exact independently accepted PR8175 source and actual versioned captures. No science execution/verdict."""
from pathlib import Path
import hashlib,json,subprocess
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
dp=R/'drain8175-author-unit-draft-v1.json';fp=R/'drain8175-author-final-freeze.json';rp=R/'drain8175-review-final.json'
d=json.loads(dp.read_text());f=json.loads(fp.read_text());v=json.loads(rp.read_text())
assert sha(rp)=='836559a4a8ab8141e1558062cf62b723ccbb7860cbf73290c048c3d8917d00aa'
assert v['verdict']=='PASS' and v['same_session_provenance'] is True and not v['findings']
assert v['reviewer_session']=='/root/review_8175' and v['source_tree']==f['tree']==git('write-tree') and {x['path']:x['sha256'] for x in v['source_paths']}==f['source_paths']
assert not git('diff','--name-only')
for p,h in (f['source_paths']|f['inputs']).items():assert sha(W/p)==h,p
refs=[d['reviewer']['report'],*d['reviewer']['references'],ref(dp),ref(fp)]
for e in f['executions']:
 p=Path(e['receipt']);assert sha(p)==e['sha256'];x=json.loads(p.read_text());assert x['error'] is None;refs += [ref(p),x['adapter'],*x['artifacts']]
refs += [dict(path=p,sha256=h) for p,h in v['immutable_references'].items()]
unique={}
for e in refs:
 p=Path(e['path']);assert p.is_relative_to(R) and sha(p)==e['sha256'],p
 if p.is_relative_to(W):
  rel=p.relative_to(W).as_posix();assert (f['source_paths']|f['inputs']).get(rel)==e['sha256'];continue
 assert str(p) not in unique or unique[str(p)]['sha256']==e['sha256'];unique[str(p)]={'path':str(p),'sha256':e['sha256']}
for row in v['original_dispositions']:
 assert 'final_path' in row and 'final_sha256' in row
 if row['final_path'] is not None:assert f['source_paths'][row['final_path']]==row['final_sha256']
d['source'].update(tree=f['tree'],paths=[dict(path=p,sha256=h) for p,h in sorted(f['source_paths'].items())])
d['reviewer'].update(report=ref(rp),session=v['reviewer_session'],references=list(unique.values()))
for c in d['constituents']:c['dispositions']=dict(ref(rp),json_pointer='/original_dispositions')
for n in d['non_science_notes']:n['review_reference']=ref(rp)
for p in d.get('supporting_proofs',[]):p['review_reference']=ref(rp)
out=R/'drain8175-unit-final.json';assert not out.exists();out.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(ref(out)));print('paths',len(f['source_paths']),'refs',len(unique))
