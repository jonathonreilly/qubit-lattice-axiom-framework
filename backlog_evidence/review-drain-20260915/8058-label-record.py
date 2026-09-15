from pathlib import Path
import json,subprocess,hashlib
r=Path('/private/tmp/review-drain-20260915');w=r/'author-pool/author-backlog';p=json.loads((r/'review-8058-provisional.json').read_text());v=json.loads((r/'8058-unit-preexecution-v1.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p));git=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip();n='scripts/native_zero_penalty_l4_delayed_splitting_2026_09_08.py';old=subprocess.check_output(['git','-C',str(w),'show','25d6e78e8b848ee2b0b9243617bdb5d04073ccce:'+n],text=True);new=(w/n).read_text();assert new==old.replace('general-torus cut and isolation proofs are analytical, not an exhaustive flux-sector run.','the general-torus cut proof and finite L4 isolation proof are analytical; no exhaustive flux-sector run.')
paths=git('diff','--cached','--name-only').splitlines();p['final_path_sha256']={n:sha(w/n) for n in paths};p['staged_tree']=git('write-tree');p['status']='Affected label correction cold confirmed; initial three successful captures retained, only8052 fresh capture pending';p['late_label_correction']='8052 stdout separated general cut proof from finite L4 isolation. Exact one-string change, no computation change. Initial run completed before finding delivery; source-bound8053/8058 unchanged and reusable.';p['prior_provisional']=ref(r/'review-8058-provisional.json')
for rows in p['constituent_dispositions'].values():
 for x in rows:
  if x['final_path']:x['final_sha256']=sha(w/x['final_path'])
report=r/'review-8058-label-provisional.json';assert not report.exists();report.write_text(json.dumps(p,indent=2)+'\n');rr=ref(report);v['reviewer']['report']=rr;v['reviewer']['references'].append(ref(r/'8052-label-source-freeze.json'));v['source']['tree']=p['staged_tree'];v['source']['paths']=[dict(path=n,sha256=sha(w/n)) for n in paths]
for entries in v['inputs'].values():
 for x in entries:x['sha256']=sha(w/x['path'])
for c in v['constituents']:c['dispositions']=dict(rr,json_pointer=c['dispositions']['json_pointer'])
for n in v['non_science_notes']:n['review_reference']=rr
out=r/'8058-unit-label-preexecution-v1.json';assert not out.exists();out.write_text(json.dumps(v,indent=2)+'\n');print(p['staged_tree'])
