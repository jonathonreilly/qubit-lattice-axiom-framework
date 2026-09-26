"""Execute the declared independent-seed formation diagnostics; retain all receipts."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
from itertools import product
import argparse,datetime,hashlib,json,subprocess,time
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['pilot','screen']);parser.add_argument('executable',type=Path);args=parser.parse_args();exe=args.executable.resolve()
 if args.mode=='pilot':cases=list(product([4,6,8],[1],[21092301,21092302]));check_every='1'
 else:cases=list(product([4,8,12,16,24,32],[.1,1,10],range(21092401,21092409)));check_every='0'
 out=HERE/f'geometric_growth_{args.mode}';out.mkdir(exist_ok=False)
 source=HERE/'geometric_partner_growth.cpp';protocol=HERE/'GEOMETRIC_PARTNER_FORMATION_SCREEN_PROTOCOL.md'
 manifest={'mode':args.mode,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':sha(source),'binary_sha256':sha(exe),'protocol_sha256':sha(protocol),'wrapper_sha256':sha(Path(__file__)),'cases':cases,'workers':2,'geometry_only':True,'nu':0,'event_cap':10000000}
 (out/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
 def run(case):
  N,beta,seed=case;name=f'N{N}_b{beta}_s{seed}';prefix=out/name;cmd=[str(exe),str(N),str(seed),str(beta),'1','10000000',str(prefix),check_every]
  started=time.monotonic();proc=subprocess.run(cmd,text=True,capture_output=True);wall=time.monotonic()-started
  Path(str(prefix)+'.stdout').write_text(proc.stdout);Path(str(prefix)+'.stderr').write_text(proc.stderr)
  files=[Path(str(prefix)+suffix) for suffix in ['.csv','.json','.state.txt','.stdout','.stderr']]
  receipt={'case':case,'command':cmd,'exit_code':proc.returncode,'wall_seconds':wall,'files':{p.name:sha(p) for p in files if p.exists()}}
  Path(str(prefix)+'.receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
  if proc.returncode:raise RuntimeError(f'{name}: {proc.stderr}')
  data=json.loads(Path(str(prefix)+'.json').read_text());return {'name':name,'N':N,'beta':beta,'seed':seed,'wall_seconds':wall,**{k:data[k] for k in ['full','time','events','slide_events','site_reuses','max_site_births','winding']}}
 results=[];failures=[]
 with ThreadPoolExecutor(max_workers=2) as pool:
  futures={pool.submit(run,case):case for case in cases}
  for future in as_completed(futures):
   try:row=future.result();results.append(row);print(json.dumps(row),flush=True)
   except Exception as error:failures.append({'case':futures[future],'error':str(error)});print(json.dumps(failures[-1]),flush=True)
 assert sha(source)==manifest['source_sha256'] and sha(exe)==manifest['binary_sha256']
 result={'manifest':manifest,'results':sorted(results,key=lambda r:(r['N'],r['beta'],r['seed'])),'failures':failures,'all_processes_succeeded':not failures,'all_completed':not failures and all(r['full'] for r in results)}
 (out/'SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'runs':len(results),'failures':len(failures),'all_full':result['all_completed'],'total_process_seconds':sum(r['wall_seconds'] for r in results)}),flush=True)
 if failures:raise SystemExit(1)
if __name__=='__main__':main()
