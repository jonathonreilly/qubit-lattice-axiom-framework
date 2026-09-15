"""One actual execution after a frozen author correction; no review verdict."""
from pathlib import Path
import argparse,json,sys,subprocess,hashlib
p=argparse.ArgumentParser();p.add_argument('pr');p.add_argument('runner');p.add_argument('timeout',type=int);p.add_argument('count',type=int);a=p.parse_args()
r=Path.cwd().parent;freeze=json.load(open(r/f'{a.pr}-author-preexecution.json'))
sys.path.insert(0,'scripts');import runner_cache
result,cache=runner_cache.execute_and_write_cache(a.runner,timeout_sec=a.timeout)
(r/f'{a.pr}-author-final-execution.json').write_text(json.dumps(result,indent=2)+'\n')
assert result['status']=='ok' and result['exit_code']==0 and f'TOTAL: PASS={a.count} FAIL=0' in result['stdout']
assert runner_cache.cache_status(Path(a.runner))=='fresh'
for path,h in freeze.items():
 if Path(path).resolve()!=cache.resolve():assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==h,path
subprocess.run(['git','add',str(cache)],check=True)
for args in [('diff','--check'),('diff','--cached','--check'),('diff','HEAD','--check')]:subprocess.run(['git',*args],check=True)
print('FINAL',subprocess.check_output(['git','write-tree'],text=True).strip(),a.count,'/0',result['elapsed_sec'],flush=True)
