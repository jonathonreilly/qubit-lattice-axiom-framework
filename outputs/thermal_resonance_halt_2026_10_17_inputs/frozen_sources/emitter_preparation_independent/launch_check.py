"""Capture and fsync actual science inputs before one bounded child execution."""
from pathlib import Path
import hashlib,importlib.metadata,importlib.util,json,os,platform,resource,shutil,subprocess,sys,time
from datetime import datetime,timezone
D=Path(__file__).resolve().parent
plan=json.loads((D/'RESOURCE_PLAN.json').read_text());caps=plan['scientific_caps']
old=sorted(D.glob('attempt_*'));assert len(old)<caps['maximum_attempts']
A=D/('attempt_'+str(len(old)+1).zfill(2));A.mkdir()
executed=A/'check_preparation.py';shutil.copyfile(D/'check_preparation.py',executed)
def binding(p):
 p=Path(p).resolve();raw=p.read_bytes();s=p.stat()
 return {'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'generation':{'device':s.st_dev,'inode':s.st_ino,'mtime_ns':s.st_mtime_ns,'ctime_ns':s.st_ctime_ns}}
def save(path,obj):
 with path.open('x') as f:f.write(json.dumps(obj,indent=2)+'\n');f.flush();os.fsync(f.fileno())
runtime=[Path(sys.executable),Path(importlib.util.find_spec('sympy').origin)]
dist=importlib.metadata.distribution('sympy')
runtime += [Path(dist.locate_file(x)) for x in dist.files if str(x).endswith('.dist-info/METADATA')]
paths=[D/'RESOURCE_PLAN.json',D/'SOURCE_MAP.json',D/'check_preparation.py',Path(__file__),executed]+sorted((D/'inputs').glob('*'))+runtime
rows=[binding(p) for p in paths]
env=dict(os.environ);env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
pre={'utc':datetime.now(timezone.utc).isoformat(),'argv':[sys.executable,str(executed)],'cwd':str(A),'caps':caps,'bindings':rows,'runtime_version':platform.python_version(),'thread_requests':'1; requests only, not measured thread counts'}
save(A/'PRELAUNCH.json',pre)
def limits():resource.setrlimit(resource.RLIMIT_CPU,tuple(caps['cpu_soft_hard_seconds']))
start=time.monotonic();before=resource.getrusage(resource.RUSAGE_CHILDREN);timeout=False
with (A/'stdout.json').open('wb') as out,(A/'stderr.txt').open('wb') as err:
 p=subprocess.Popen(pre['argv'],cwd=A,env=env,stdout=out,stderr=err,preexec_fn=limits)
 try:code=p.wait(timeout=caps['external_wall_seconds'])
 except subprocess.TimeoutExpired:timeout=True;p.kill();code=p.wait()
after=resource.getrusage(resource.RUSAGE_CHILDREN);post=[binding(r['path']) for r in rows]
receipt={'finished_utc':datetime.now(timezone.utc).isoformat(),'exit_code':code,'timed_out':timeout,'wall_seconds':time.monotonic()-start,'user_cpu_seconds':after.ru_utime-before.ru_utime,'system_cpu_seconds':after.ru_stime-before.ru_stime,'child_peak_rss_native_units':after.ru_maxrss,'platform':platform.platform(),'caps':caps,'prelaunch':binding(A/'PRELAUNCH.json'),'stdout':binding(A/'stdout.json'),'stderr':binding(A/'stderr.txt'),'all_bound_bytes_and_generations_unchanged':rows==post,'after_bindings':post}
save(A/'RECEIPT.json',receipt)
print(json.dumps({k:receipt[k] for k in ['exit_code','timed_out','wall_seconds','user_cpu_seconds','system_cpu_seconds','all_bound_bytes_and_generations_unchanged']},indent=2))
sys.exit(0 if code==0 and not timeout and rows==post else 1)
