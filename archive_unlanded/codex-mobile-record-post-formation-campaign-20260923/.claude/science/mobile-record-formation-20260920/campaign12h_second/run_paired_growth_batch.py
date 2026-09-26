"""Reproducible bounded batch driver, preserving all receipts and failures."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import argparse,hashlib,json,subprocess,time
HERE=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--phase',choices=['pilot','screen'],required=True);p.add_argument('--workers',type=int,default=2);args=p.parse_args()
exe=Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-21-second/paired_record_growth')
out=HERE/('paired_growth_'+args.phase);out.mkdir(exist_ok=True)
if (out/'MANIFEST.json').exists():raise SystemExit('Preserve existing batch; select a new driver/phase explicitly for follow-up.')
sides=[4,8] if args.phase=='pilot' else [4,6,8,12]
seeds=[21092101,21092102] if args.phase=='pilot' else [21092201,21092202,21092203,21092204]
limit=100 if args.phase=='pilot' else 1000
jobs=[]
for N in sides:
 for init in ['empty','jam']:
  for mu,label in [('0','baseline'),('0.06666666666666666667','extended')]:
   for seed in seeds:
    stem=f'N{N}_{init}_{label}_s{seed}';prefix=out/stem
    cmd=[str(exe),str(N),str(seed),'1','1','1',mu,str(limit),str(prefix),init,'40']
    jobs.append({'stem':stem,'command':cmd})
sources={str(x):hashlib.sha256(x.read_bytes()).hexdigest() for x in [exe,HERE/'paired_record_growth.cpp',HERE/'PAIRED_RECORD_GROWTH_SCREEN_PROTOCOL.md',Path(__file__)]}
manifest={'created_utc':datetime.now(timezone.utc).isoformat(),'phase':args.phase,'source_sha256':sources,'workers':args.workers,'jobs':jobs}
(out/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
def run(job):
 start=time.monotonic();r=subprocess.run(job['command'],capture_output=True,text=True)
 (out/(job['stem']+'.stdout')).write_text(r.stdout);(out/(job['stem']+'.stderr')).write_text(r.stderr)
 result={'stem':job['stem'],'returncode':r.returncode,'wall_seconds':time.monotonic()-start}
 (out/(job['stem']+'.receipt.json')).write_text(json.dumps(result,indent=2)+'\n')
 if r.returncode==0:result.update(json.loads((out/(job['stem']+'.json')).read_text()))
 print(json.dumps(result),flush=True);return result
with ThreadPoolExecutor(max_workers=args.workers) as pool:results=list(pool.map(run,jobs))
(out/'BATCH_RESULTS.json').write_text(json.dumps(results,indent=2)+'\n')
assert all(r['returncode']==0 for r in results)
print(json.dumps({'completed':len(results),'phase':args.phase,'all_runs_succeeded':True}),flush=True)
