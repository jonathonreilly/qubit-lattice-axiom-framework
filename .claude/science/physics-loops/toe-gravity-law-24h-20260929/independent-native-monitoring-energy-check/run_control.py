#!/usr/bin/env python3
import datetime,hashlib,json,os,pathlib,resource,signal,subprocess,sys,time
p=pathlib.Path(__file__).resolve().parent;r=pathlib.Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
deadline=json.loads((r/'DEADLINE.json').read_text())['deadline_epoch']
assert time.time()<deadline and not (r/'STOP_REQUESTED.json').exists()
assert not (p/'EXECUTION.json').exists()
freeze=json.loads((p/'CONTROL_FREEZE.json').read_text())
for f,h in freeze['files'].items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h
start=time.monotonic();rssmax=0;reason=None
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',NUMEXPR_NUM_THREADS='1')
def limit():resource.setrlimit(resource.RLIMIT_CPU,(5,6))
with (p/'RESULTS.json').open('w') as out,(p/'STDERR.txt').open('w') as err:
 proc=subprocess.Popen([sys.executable,str(p/'check_monitoring.py')],stdout=out,stderr=err,env=env,start_new_session=True,preexec_fn=limit)
 while proc.poll() is None:
  rss=subprocess.run(['ps','-o','rss=','-p',str(proc.pid)],capture_output=True,text=True).stdout.strip()
  if rss:rssmax=max(rssmax,int(rss)*1024)
  if time.monotonic()-start>30:reason='wall'
  if rssmax>100*1024**2:reason='RSS'
  if time.time()>=deadline:reason='deadline'
  if (r/'STOP_REQUESTED.json').exists():reason='STOP'
  if reason:os.killpg(proc.pid,signal.SIGKILL);break
  time.sleep(.1)
 code=proc.wait()
rec={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':code,'termination_reason':reason,'wall_seconds':time.monotonic()-start,'sampled_peak_rss_bytes':rssmax,'child_user_cpu':resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime,'child_system_cpu':resource.getrusage(resource.RUSAGE_CHILDREN).ru_stime,'runner_sha256':freeze['files']['check_monitoring.py']}
(p/'EXECUTION.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec,indent=2));sys.exit(code)
