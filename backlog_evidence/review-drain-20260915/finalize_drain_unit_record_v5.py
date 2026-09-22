"""Bind a final independent report to the unchanged source and captured caches.
This is identity-only adaptation; it never infers a scientific verdict.
"""
from pathlib import Path
import argparse,hashlib,json,subprocess
ap=argparse.ArgumentParser();ap.add_argument('unit');ap.add_argument('--worktree',required=True);ap.add_argument('--report',required=True);ap.add_argument('--draft');a=ap.parse_args()
r=Path(__file__).resolve().parent;w=Path(a.worktree);prefix='drain'+a.unit
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
git=lambda *args:subprocess.check_output(['git','-C',str(w),*args],text=True).strip()
draft=Path(a.draft) if a.draft else r/(prefix+'-author-unit-draft-v1.json');freeze=r/(prefix+'-author-final-freeze.json');report=Path(a.report)
d=json.loads(draft.read_text());f=json.loads(freeze.read_text());v=json.loads(report.read_text())
assert git('write-tree')==f['tree'];assert not git('diff','--name-only')
for p,h in f['source_paths'].items():assert sha(w/p)==h,p
for p,h in f['inputs'].items():assert sha(w/p)==h,p
final_sources=v.get('source_hashes',v.get('source_paths',v.get('source',{}).get('paths')))
if isinstance(final_sources,list):final_sources={x['path']:x['sha256'] for x in final_sources}
assert final_sources==f['source_paths'],'Independent final source identity closure missing'
rr=ref(report);refs=[d['reviewer']['report'],*d['reviewer']['references'],ref(draft),ref(freeze),ref(r/(prefix+'-capture.py'))]
refs.extend(ref(Path(e['receipt'])) for e in f['executions'])
# Bind the actually executed capture adapter, including corrected-version scripts.
for e in f['executions']:
 execution=json.loads(Path(e['receipt']).read_text())
 capture=Path(execution['capture_script'])
 assert sha(capture)==execution['capture_script_sha256']
 refs.append(ref(capture))
for q in refs:assert sha(Path(q['path']))==q['sha256']
d['source'].update(tree=f['tree'],paths=[dict(path=p,sha256=h) for p,h in sorted(f['source_paths'].items())])
d['reviewer'].update(report=rr,session=v.get('reviewer_session',v.get('reviewer',d['reviewer']['session'])),references=list({x['path']:x for x in refs}.values()))
disps=v['original_dispositions']
for c in d['constituents']:
 pointer='/original_dispositions'
 if isinstance(disps,dict):
  key=c['id'].removeprefix('PR');assert key in disps;pointer+='/'+key
 c['dispositions']=dict(rr,json_pointer=pointer)
for n in d['non_science_notes']:n['review_reference']=rr
for proof in d.get('supporting_proofs',[]):proof['review_reference']=rr
out=r/(prefix+'-unit-final.json');assert not out.exists();out.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(ref(out)));print('source',len(f['source_paths']),'tree',f['tree'])
