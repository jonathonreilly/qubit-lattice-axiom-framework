#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,os,resource,subprocess,sys,time
ROOT=Path(__file__).resolve().parent
def identity(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
env=os.environ.copy();env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
argv=[sys.executable,str(ROOT/'check_composition.py')]
start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic()
before=resource.getrusage(resource.RUSAGE_CHILDREN)
with (ROOT/'check.stdout').open('wb') as out,(ROOT/'check.stderr').open('wb') as err:
 try:
  result=subprocess.run(argv,cwd=ROOT,env=env,stdout=out,stderr=err,timeout=90)
  code=result.returncode;timed_out=False
 except subprocess.TimeoutExpired:
  code=None;timed_out=True
after=resource.getrusage(resource.RUSAGE_CHILDREN)
receipt={'argv':argv,'cwd':str(ROOT),'started_utc':start,
 'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t,
 'exit_code':code,'timed_out':timed_out,'cpu_seconds_cap':60,'wall_seconds_cap':90,
 'largest_matrix_dimension':32,'user_cpu_seconds':after.ru_utime-before.ru_utime,
 'system_cpu_seconds':after.ru_stime-before.ru_stime,'peak_rss_bytes_macos':after.ru_maxrss,
 'environment_requests':{k:env[k] for k in ('PYTHONDONTWRITEBYTECODE','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS')},
 'files':[identity(ROOT/n) for n in ('check_composition.py','run_check.py','SOURCE_PINS.json','check.stdout','check.stderr')],
 'generated_evidence':[identity(ROOT/'RESULTS.json')] if (ROOT/'RESULTS.json').exists() else []}
(ROOT/'EXECUTION.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2));sys.exit(0 if code==0 else 1)
