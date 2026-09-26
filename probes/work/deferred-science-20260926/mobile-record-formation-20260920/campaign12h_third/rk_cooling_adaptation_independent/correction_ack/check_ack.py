from pathlib import Path
from hashlib import sha256
import json
from datetime import datetime, timezone
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]
def load(p): return json.loads(p.read_text())
def identity(p): return {'path':str(p),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
def check(row, replacement=None):
    p=Path(replacement or row['path']); r=identity(p)
    assert (r['bytes'],r['sha256'])==(row['bytes'],row['sha256'])
    return r
receipt_path=BASE/'RK_COOLING_ADAPTATION_F1_REPAIR_RECEIPT.json'
r=load(receipt_path)
for key in ('old_note','new_note','old_author_seal','new_author_seal','diff','independent_final_seal'): check(r[key])
assert r['new_note']['sha256']=='a47a407bd613ac86d0e9e7d359e86185859236ec1a12b88d08fd6f9a2e1a66ab'
assert r['new_author_seal']['sha256']=='de4fae0a513464b2ebcdf00ab954db3fd9c637333e19d73acfd347ea06cc722e'
old=Path(r['old_note']['path']).read_text(); new=Path(r['new_note']['path']).read_text()
before='For nonconstant d(c), the unchanged cooling generator has no pure stationary\nstate. This statement applies to this fixed jump family, even if all its'
after='For nonconstant d(c) and nonzero delta, the unchanged cooling generator has no\npure stationary state. This statement applies to this fixed jump family, even if all its'
assert old.count(before)==new.count(after)==1
assert old.replace(before,after)==new and new.replace(after,before)==old
oa=load(Path(r['old_author_seal']['path'])); na=load(Path(r['new_author_seal']['path']))
oldrows={v['path']:v for v in oa['artifacts']};newrows={v['path']:v for v in na['artifacts']}
assert oldrows.keys()==newrows.keys() and len(oldrows)==20
changed=[k for k in oldrows if oldrows[k]!=newrows[k]]
assert changed==[r['new_note']['path']]
for v in na['artifacts']: check(v)
for v in oa['artifacts']: check(v,r['old_note']['path'] if v['path']==r['new_note']['path'] else None)
fs=load(Path(r['independent_final_seal']['path']))
mapping={r['new_note']['path']:r['old_note']['path'],r['new_author_seal']['path']:r['old_author_seal']['path']}
for v in fs['sources']+fs['artifacts']: check(v,mapping.get(v['path']))
out={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'F1 resolved; narrow statement qualification only','scope':'No unchanged mathematical rerun; no author or earlier independent artifact edited.','before':r['old_note'],'after':r['new_note'],'old_author_seal':r['old_author_seal'],'new_author_seal':r['new_author_seal'],'repair_receipt':identity(receipt_path),'delta':r['diff'],'inverse_exact_recovery':True,'changed_author_artifacts':changed,'unchanged_author_artifacts':19,'historical_independent_final_bindings_authenticated':len(fs['sources'])+len(fs['artifacts']),'prior_final_seal':r['independent_final_seal'],'scientific_conclusion':'The unchanged cooler has no pure stationary state when d(c) is nonconstant AND delta is nonzero. Delta=0 and constant-flippability exceptions remain available.','checker':identity(Path(__file__))}
text=json.dumps(out,indent=2)+'\n';(HERE/'ACK.json').write_text(text);print(text,end='')
