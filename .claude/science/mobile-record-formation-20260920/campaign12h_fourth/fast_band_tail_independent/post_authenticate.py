from pathlib import Path
import hashlib,json,datetime,difflib
HERE=Path(__file__).resolve().parent;BASE=HERE.parent;REPO=HERE.parents[4]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
pre=json.loads((HERE/'PRE_SEAL.json').read_text())
assert sha(HERE/'PRE_SEAL.json')=='070337f415cd81ddafa7178790863a2ecc542bcb23d6a142b681e10f4cec853e'
for r in pre['artifacts']:assert sha(HERE/r['path'])==r['sha256'] and (HERE/r['path']).stat().st_size==r['bytes']
author=BASE/'fast_band_tail_author';assert sha(author/'AUTHOR_SEAL.json')=='646d5a33082c0d44a8af5a25a22b61da9b8ca89275651f80458c2a9c7f7f02e6'
s=json.loads((author/'AUTHOR_SEAL.json').read_text());bindings=[]
def snapshot(p,relative):
 out=HERE/'post_sources'/relative;out.parent.mkdir(parents=True,exist_ok=True);assert not out.exists();out.write_bytes(p.read_bytes());bindings.append({'path':str(p),'snapshot':str(out.relative_to(HERE)),'bytes':out.stat().st_size,'sha256':sha(out)})
snapshot(author/'AUTHOR_SEAL.json','author/AUTHOR_SEAL.json')
for r in s['artifacts']:
 p=author/r['path'];assert sha(p)==r['sha256'] and p.stat().st_size==r['bytes'];snapshot(p,'author/'+r['path'])
for r in s['sources']:
 p=REPO/r['path'];assert sha(p)==r['sha256'];snapshot(p,'bound_sources/'+p.parent.name+'__'+p.name)
dep=BASE/'fast_band_energy_independent';assert sha(dep/'FINAL_SEAL.json')=='5824c37555272e57a1b5b0b1214bcb5441a86dd9362f18bb157bbeec960a4ef5'
ds=json.loads((dep/'FINAL_SEAL.json').read_text());dr=next(r for r in ds['artifacts'] if r['path']=='COMPARISON.md');assert sha(dep/'COMPARISON.md')==dr['sha256']
for n in ('COMPARISON.md','FINAL_SEAL.json'):snapshot(dep/n,'compact_dependency/'+n)
result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'PRE_artifacts_authenticated':len(pre['artifacts']),'PRE_seal_sha256':sha(HERE/'PRE_SEAL.json'),'author_artifacts_authenticated':len(s['artifacts']),'author_bound_sources_authenticated':len(s['sources']),'author_seal_sha256':sha(author/'AUTHOR_SEAL.json'),'compact_dependency_scope':'Only released complete comparison report and final seal were read/authenticated here. Root separately reports full review/authentication of all 80; this packet does not claim to repeat that work.','compact_dependency_artifacts_in_its_seal':len(ds['artifacts']),'compact_dependency_seal_sha256':sha(dep/'FINAL_SEAL.json'),'bindings':bindings,'restriction':'No author code imported or executed; only own frozen PRE engine may be reused. No external personal plan, current CHECKPOINT, or other current peer material read.'}
(HERE/'POST_SOURCE_BINDINGS.json').write_text(json.dumps(result,indent=2)+'\n')
old=(author/'initial_integer_power_attempt/exact_tail_control.py').read_text().splitlines(True);new=(author/'exact_tail_control.py').read_text().splitlines(True)
(HERE/'AUTHOR_INTEGER_FIX.diff').write_text(''.join(difflib.unified_diff(old,new,fromfile='initial_integer_power_attempt/exact_tail_control.py',tofile='exact_tail_control.py')))
print(json.dumps({k:v for k,v in result.items() if k!='bindings'},indent=2))
x=json.loads((author/'EXACT_TAIL_RESULTS.json').read_text());print('certificate fields',{k:len(v) if isinstance(v,(list,dict)) else v for k,v in x.items()})
