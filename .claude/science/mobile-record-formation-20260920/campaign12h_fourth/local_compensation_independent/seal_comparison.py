#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,datetime
base=Path(__file__).resolve().parent;out=base/'FINAL_SEAL.json';assert not out.exists()
def bind(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def check(r):assert bind(Path(r['path']))=={k:r[k] for k in ['path','bytes','sha256']}
pre=base/'PRE_COMPARISON_SEAL.json';assert bind(pre)['sha256']=='bc1f83597d26466a02d2a1375fea91624b3adb99dcac25f7902262935a9feeb2'
p=json.loads(pre.read_text())
for r in p['sources']+p['artifacts']:check(r)
a=json.loads((base/'COMPARISON_SOURCE_BINDINGS.json').read_text());sources={}
for r in p['sources']+a['author_seals']+a['author_bound_sources_and_evidence']:
 check(r);sources[r['path']]={k:r[k] for k in ['path','bytes','sha256']}
artifacts=[bind(f) for f in sorted(base.iterdir()) if f.is_file() and f!=out]
seal={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'type':'Final bounded post-PRE source comparison','disposition':'No material discrepancy or required new correction. Conditional fixed-graph supplied-model claims only; no formal audit or publication status.','pre_seal':bind(pre),'author_seals':a['author_seals'],'sources':list(sources.values()),'artifacts':artifacts,'read_and_rerun_limits':'Complete new author arguments and controls read, full recorded evidence authenticated, inherited physical builders read only for required definitions. No author runner executed; decisive new controls used independent builders. Scope and distinctions are in COMPARISON.md.','failure_preservation':'PRE unchanged. No failed new execution; countercontrols remain preserved.'}
out.write_text(json.dumps(seal,indent=2)+'\n')
for r in list(sources.values())+artifacts:check(r)
print(json.dumps({'comparison':bind(base/'COMPARISON.md'),'final_seal':bind(out),'sources_verified':len(sources),'artifacts_verified':len(artifacts),'total_verified':len(sources)+len(artifacts)},indent=2))
