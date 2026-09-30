from pathlib import Path
import datetime,hashlib,json,os,resource,subprocess,time
p=Path(__file__).resolve().parent
g=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
dead=json.loads((g/'DEADLINE.json').read_text())['deadline_epoch']
assert time.time()<dead
assert not (g/'STOP_REQUESTED').exists() and not (g/'STOP_REQUESTED.json').exists()
env=os.environ.copy()
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):env[k]='1'
def limits():resource.setrlimit(resource.RLIMIT_CPU,(10,10))
start=time.monotonic(); at=datetime.datetime.now(datetime.timezone.utc).isoformat()
proc=subprocess.Popen(['python3',str(p/'check_words.py')],stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env,preexec_fn=limits)
timedout=False
try:out,err=proc.communicate(timeout=45)
except subprocess.TimeoutExpired:
    timedout=True;proc.kill();out,err=proc.communicate()
wall=time.monotonic()-start;u=resource.getrusage(resource.RUSAGE_CHILDREN)
(p/'control.stdout').write_bytes(out);(p/'control.stderr').write_bytes(err)
record={'started_at':at,'exit':proc.returncode,'timed_out':timedout,'wall_seconds':wall,'child_cpu_seconds':u.ru_utime+u.ru_stime,'peak_child_rss_bytes':u.ru_maxrss,'limits':{'CPU_seconds':10,'wall_seconds':45,'RSS_bytes_observed_limit':104857600,'RSS_enforcement':'measured at return; not kernel-enforced'},'code_sha256':hashlib.sha256((p/'check_words.py').read_bytes()).hexdigest(),'plan_sha256':hashlib.sha256((p/'CONTROL_PLAN.md').read_bytes()).hexdigest(),'stdout_sha256':hashlib.sha256(out).hexdigest(),'stderr_sha256':hashlib.sha256(err).hexdigest()}
(p/'control-execution.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
assert proc.returncode==0 and not timedout and u.ru_maxrss<=104857600
