#!/usr/bin/env python3
import datetime, hashlib, json, os, resource, subprocess, sys, time
from pathlib import Path
p=Path(__file__).resolve().parent
campaign=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
deadline=json.loads((campaign/'DEADLINE.json').read_text())['deadline_epoch']
assert time.time()+30 < deadline
assert not any((campaign/x).exists() for x in ('STOP_REQUESTED','STOP_REQUESTED.json'))
pre=json.loads((p/'CONTROL_PREFLIGHT.json').read_text())
for f,h in pre['source_sha256'].items():
    assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h,(f,'changed before execution')
env=os.environ.copy()
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    env[k]='1'
def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(5,5))
start=time.time(); before=resource.getrusage(resource.RUSAGE_CHILDREN)
with (p/'control.stdout').open('wb') as out,(p/'control.stderr').open('wb') as err:
    proc=subprocess.Popen([sys.executable,str(p/'check_strip_word.py')],cwd=p,env=env,stdout=out,stderr=err,preexec_fn=limits)
    timeout=False
    try:
        code=proc.wait(timeout=30)
    except subprocess.TimeoutExpired:
        timeout=True;proc.kill();code=proc.wait()
end=time.time();after=resource.getrusage(resource.RUSAGE_CHILDREN)
rss=after.ru_maxrss*(1 if sys.platform=='darwin' else 1024)
receipt={'started_at':datetime.datetime.fromtimestamp(start,datetime.timezone.utc).isoformat(),'ended_at':datetime.datetime.fromtimestamp(end,datetime.timezone.utc).isoformat(),'wall_seconds':end-start,'child_cpu_seconds':(after.ru_utime+after.ru_stime)-(before.ru_utime+before.ru_stime),'child_peak_rss_bytes':rss,'exit_code':code,'timed_out':timeout,'rss_postcheck_ok':rss<=100*1024*1024,'cpu_hard_limit':5,'wall_limit':30,'rss_limit':100*1024*1024,'rss_enforcement':'postchecked child rusage, not OS address-space cap','source_sha256':pre['source_sha256'],'stdout_sha256':hashlib.sha256((p/'control.stdout').read_bytes()).hexdigest(),'stderr_sha256':hashlib.sha256((p/'control.stderr').read_bytes()).hexdigest()}
(p/'control-execution.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
raise SystemExit(0 if code==0 and not timeout and receipt['rss_postcheck_ok'] else 1)
