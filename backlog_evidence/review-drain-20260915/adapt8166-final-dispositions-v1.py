"""Identity-only receipt schema adapter; no review verdict or source mutation."""
from pathlib import Path
import json,hashlib,gzip,copy
r=Path(__file__).resolve().parent;w=r/'review-meta-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:{'path':str(p),'sha256':sha(p)}
report=r/'drain8166-final-review.json';assert sha(report)=='084a5662f8adfa86b5ea4f11a983bdf4e72a710fad21450b4462efef16fc53ab'
failed=r/'drain8166-author-final-cache.json';assert json.loads(failed.read_text())=={'schema_version':1,'mechanical_status':'invalid','error':"'final_path'"}
v=json.loads(report.read_text());handoff=r/'drain8166-author-source-handoff-v1.json';h={e['original_path']:e for e in json.loads(handoff.read_text())['original_dispositions']};freeze=json.loads((r/'drain8166-author-final-freeze.json').read_text());assert v['source_hashes']==freeze['source_paths'];rows=[]
for i,e in enumerate(v['original_dispositions']):
 prior=h[e['original_path']]
 for k in ['original_path','original_mode','original_blob','original_sha256','canonical','disposition']:assert e[k]==prior[k],(i,k)
 recovery=e['recovery'];assert recovery in freeze['source_paths'];raw=gzip.decompress((w/recovery).read_bytes());assert hashlib.sha256(raw).hexdigest()==e['original_sha256'];assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==e['original_blob']
 target=e['canonical'] or recovery;assert target==prior['final_path'];digest=sha(w/target);assert digest==prior['final_sha256']==freeze['source_paths'][target]
 row=dict(e,final_path=target,final_sha256=digest);rows.append(row)
assert len(rows)==len(h)==123
adapter=r/'drain8166-receipt-schema-adapter-v1.json';assert not adapter.exists();adapter.write_text(json.dumps({'role':'Mechanical field adaptation only. Original independent review verdict, scientific dispositions and source bytes are unchanged.','original_final_review':ref(report),'reviewed_source_handoff':ref(handoff),'preserved_failed_cache_preflight':ref(failed),'mapping':'final_path is the independently reviewed canonical field if present, otherwise its exact recovery path; final_sha256 is verified against the frozen source and preexisting handoff.','original_dispositions':rows},indent=2)+'\n')
old=r/'drain8166-unit-final.json';d=json.loads(old.read_text());assert d['reviewer']['report']==ref(report)
for c in d['constituents']:c['dispositions']=dict(ref(adapter),json_pointer='/original_dispositions')
d['reviewer']['references'] += [ref(adapter),ref(old),ref(failed),ref(Path(__file__))]
out=r/'drain8166-unit-final-v2.json';assert not out.exists();out.write_text(json.dumps(d,indent=2)+'\n');print(ref(out));print('123 reviewed dispositions adapted; no source/evidence changed')
