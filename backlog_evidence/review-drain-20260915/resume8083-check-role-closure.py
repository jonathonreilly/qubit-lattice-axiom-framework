import json,gzip,hashlib
from pathlib import Path
r=Path('/private/tmp/review-drain-20260915');repo=r/'resume-author8083';m=json.load(open(repo/'docs/work_history/repo/review_feedback/pr8079-8083-scientific-recovery/manifest.json'));known={(x['original'],x['sha256']) for x in m['rows']};hashes={x['sha256'] for x in m['rows']};bad=[];seen=set()
for x in m['rows']:
 p=repo/x['storage']
 if str(p) in seen:continue
 seen.add(str(p));raw=gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes()
 if hashlib.sha256(raw).hexdigest()!=x['sha256']:bad.append(x['original'])
for p in (repo/'outputs').glob('native_*_2026_09_10_inputs/**/*'):
 if p.is_file():hashes.add(hashlib.sha256(p.read_bytes()).hexdigest())
roles=[]
def walk(x,where):
 if isinstance(x,dict):
  if 'path'in x and 'sha256'in x:roles.append((x['path'],x['sha256'],where))
  for k,v in x.items():
   if k in ('inputs','readiness_inputs'):continue
   if k.endswith('_path')and k[:-5]+'_sha256'in x:roles.append((v,x[k[:-5]+'_sha256'],where+':'+k))
   walk(v,where+'/'+k)
 elif isinstance(x,list):
  for i,v in enumerate(x):walk(v,where+'/'+str(i))
for p in (r/'resume-check8083/.claude').rglob('*BINDING.json'):walk(json.load(open(p)),str(p.relative_to(r)))
missing=[{'original':p,'sha256':s,'role':w} for p,s,w in roles if (p,s)not in known and s not in hashes]
out={'manifest_rows':len(m['rows']),'unique_storage_verified':len(seen),'hash_failures':bad,'explicit_binding_role_occurrences':len(roles),'missing_binding_roles':missing,'boundary':'Read-only exact hashes and direct BINDING roles, excluding inherited umbrella input maps; no scientific recomputation.'};(r/'resume8083-role-closure-check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
