#!/usr/bin/env python3
import datetime,hashlib,json,os,pathlib,resource,signal,subprocess,sys,time
p=pathlib.Path(__file__).resolve().parent
runtime=pathlib.Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
deadline=json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
assert time.time()<deadline and not (runtime/'STOP_REQUESTED.json').exists()
assert not (p/'EXECUTION.json').exists(), 'preserve every prior execution'
expected=json.loads((p/'CONTROL_FREEZE.json').read_text())
for name,h in expected['files'].items():assert hashlib.sha256((p/name).read_bytes()).hexdigest()==h
started=time.monotonic();maxrss=0;reason=None
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',NUMEXPR_NUM_THREADS='1')
def limits():resource.setrlimit(resource.RLIMIT_CPU,(30,31))
with (p/'RESULTS.json').open('w') as out,(p/'STDERR.txt').open('w') as err:
    proc=subprocess.Popen([sys.executable,str(p/'check_readout.py')],stdout=out,stderr=err,env=env,start_new_session=True,preexec_fn=limits)
    while proc.poll() is None:
        rss=subprocess.run(['ps','-o','rss=','-p',str(proc.pid)],capture_output=True,text=True).stdout.strip()
        if rss:maxrss=max(maxrss,int(rss)*1024)
        if time.monotonic()-started>90:reason='wall_cap'
        if maxrss>150*1024**2:reason='rss_cap'
        if time.time()>=deadline:reason='deadline'
        if (runtime/'STOP_REQUESTED.json').exists():reason='STOP_REQUESTED'
        if reason:os.killpg(proc.pid,signal.SIGKILL);break
        time.sleep(.2)
    code=proc.wait()
r={'started_utc':datetime.datetime.fromtimestamp(time.time()-(time.monotonic()-started),datetime.timezone.utc).isoformat(),'exit_code':code,'termination_reason':reason,'wall_seconds':time.monotonic()-started,'sampled_peak_rss_bytes':maxrss,'child_user_cpu_seconds':resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime,'child_system_cpu_seconds':resource.getrusage(resource.RUSAGE_CHILDREN).ru_stime,'deadline_epoch':deadline,'runner_sha256':expected['files']['check_readout.py']}
(p/'EXECUTION.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2));sys.exit(code)
