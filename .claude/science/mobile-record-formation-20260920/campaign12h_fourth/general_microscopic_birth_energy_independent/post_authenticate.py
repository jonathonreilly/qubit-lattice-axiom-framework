"""Authenticate immutable PRE and released author packet; snapshot exact bytes."""
from pathlib import Path
import json,hashlib,datetime,shutil
here=Path(__file__).resolve().parent
repo=here.parents[4]
author=here.parent/'general_microscopic_birth_energy_author'
hashf=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
pre=json.loads((here/'PRE_SEAL.json').read_text())
assert hashf(here/'PRE_SEAL.json')=='26fd1a7c0a4a5675c357508e6ae70253eebe8ae1d0690743abdcb06ec8c78c5f'
for r in pre['artifacts']:
 p=here/r['path']; assert hashf(p)==r['sha256'] and p.stat().st_size==r['bytes'],r
assert hashf(author/'AUTHOR_SEAL.json')=='0f1219204fbe9b74209d7a0832e311d742a69d6fec0bf481eb28817ba98ecfd9'
s=json.loads((author/'AUTHOR_SEAL.json').read_text()); rows=[]
for r in s['artifacts']:
 p=author/r['path']; assert hashf(p)==r['sha256'] and p.stat().st_size==r['bytes'],r
for r in s['sources']:
 p=repo/r['path']; assert hashf(p)==r['sha256'],(p,r)
for p in [author/'AUTHOR_SEAL.json']+[author/r['path'] for r in s['artifacts']]+[repo/r['path'] for r in s['sources']]:
 name=('author__'+p.name) if p.parent==author else ('source__'+p.parent.name+'__'+p.name)
 dest=here/'post_sources'/name; dest.parent.mkdir(exist_ok=True)
 if dest.exists(): assert hashf(dest)==hashf(p)
 else: shutil.copyfile(p,dest)
 rows.append({'original_path':str(p),'snapshot':str(dest.relative_to(here)),'bytes':dest.stat().st_size,'sha256':hashf(dest)})
o={'comparison_started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'prior_PRE_seal_sha256':hashf(here/'PRE_SEAL.json'),'prior_PRE_artifacts_authenticated':len(pre['artifacts']),'author_seal_sha256':hashf(author/'AUTHOR_SEAL.json'),'author_artifacts_authenticated':len(s['artifacts']),'author_sources_authenticated':len(s['sources']),'rows':rows,'restriction':'No author code imported or executed. Frozen PRE engine may be reused for calculations. Root CHECKPOINT, full_instrument_energy_supply_author and external personal plans remain unread.'}
(here/'POST_SOURCE_BINDINGS.json').write_text(json.dumps(o,indent=2)+'\n')
print(json.dumps({k:v for k,v in o.items() if k!='rows'},indent=2))
for fn in ['LOCAL_LEAKAGE_RESULTS.json','COMPLETE_TWO_CENTER_RESULTS.json']:
 x=json.loads((author/fn).read_text()); print(fn,{k:(len(v) if isinstance(v,(dict,list)) else v) for k,v in x.items()})
