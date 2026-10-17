"""Serialize genuine source/runtime/cap bindings, then run one bounded child."""
from pathlib import Path
import datetime, hashlib, importlib.metadata, importlib.util, json, os
import resource, shutil, subprocess, sys, time

D=Path(__file__).resolve().parent
plan=json.loads((D/'RESOURCE_PLAN.json').read_text())
n=int(sys.argv[1]) if len(sys.argv)>1 else 1
assert 1<=n<=plan['scientific_caps']['maximum_attempts']
run=D/('attempt_%02d'%n); run.mkdir()
executed=run/'check_family.py'; shutil.copyfile(D/'check_family.py',executed)
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def binding(path,kind):
    path=Path(path).resolve(); stat=path.stat(); data=path.read_bytes()
    return {'path':str(path),'kind':kind,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'generation':{'device':stat.st_dev,'inode':stat.st_ino,'size':stat.st_size,'mtime_ns':stat.st_mtime_ns,'ctime_ns':stat.st_ctime_ns}}
runtime=[Path(sys.executable).resolve(),Path(importlib.util.find_spec('sympy').origin),Path(importlib.metadata.distribution('sympy')._path)/'METADATA']
files=[D/'RESOURCE_PLAN.json',D/'SOURCE_MANIFEST.json',D/'check_family.py',Path(__file__),executed]+sorted((D/'inputs').iterdir())
bindings=[binding(p,'source_or_input') for p in files]+[binding(p,'runtime') for p in runtime]
env={key:'1' for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']}
env.update({'PYTHONDONTWRITEBYTECODE':'1','PYTHONHASHSEED':'0'})
command=[str(Path(sys.executable).resolve()),'-B',str(executed)]
record={'serialized_utc':utc(),'command':command,'cwd':str(run),'caps':plan['scientific_caps'],'cpu_soft_hard':[20,20],'wall_timeout_seconds':30,'environment_overrides':env,'bindings':bindings,'runtime_version_metadata':{'python':sys.version,'sympy':importlib.metadata.version('sympy')},'binding_limit':'Interpreter binary, SymPy entry and distribution metadata pinned; not every transitive installed-library byte. Thread requests are recorded, actual thread counts are not measured.'}
pre=run/'PRELAUNCH.json'
with pre.open('x') as stream:
    json.dump(record,stream,indent=2); stream.write('\n'); stream.flush(); os.fsync(stream.fileno())
prehash=hashlib.sha256(pre.read_bytes()).hexdigest()
def limit(): resource.setrlimit(resource.RLIMIT_CPU,(20,20))
before=resource.getrusage(resource.RUSAGE_CHILDREN)
start_utc=utc(); start=time.monotonic(); timeout=False
with (run/'stdout.json').open('wb') as out,(run/'stderr.txt').open('wb') as err:
    try:
        result=subprocess.run(command,cwd=run,env={**os.environ,**env},stdout=out,stderr=err,timeout=30,preexec_fn=limit)
        code=result.returncode
    except subprocess.TimeoutExpired:
        timeout=True; code=None
elapsed=time.monotonic()-start; after=resource.getrusage(resource.RUSAGE_CHILDREN)
post=[]
for row in bindings:
    fresh=binding(row['path'],row['kind'])
    post.append({'path':row['path'],'hash_and_bytes_equal':(fresh['sha256'],fresh['bytes'])==(row['sha256'],row['bytes']),'generation_equal':fresh['generation']==row['generation']})
receipt={'launch_after_prelaunch_fsync_utc':start_utc,'completed_utc':utc(),'prelaunch_sha256':prehash,'exit_code':code,'timed_out':timeout,'wall_seconds':elapsed,'child_user_cpu_seconds':after.ru_utime-before.ru_utime,'child_system_cpu_seconds':after.ru_stime-before.ru_stime,'child_peak_rss_macos_bytes':after.ru_maxrss,'actual_caps':{'cpu_soft_hard_seconds':[20,20],'external_wall_seconds':30,'os_memory_limit':None},'stdout':binding(run/'stdout.json','output'),'stderr':binding(run/'stderr.txt','output'),'postchecks':post}
with (run/'RECEIPT.json').open('x') as stream: json.dump(receipt,stream,indent=2); stream.write('\n')
print(json.dumps({'attempt':n,'exit_code':code,'timed_out':timeout,'wall_seconds':elapsed,'bindings':len(bindings),'all_postchecks_match':all(r['hash_and_bytes_equal'] and r['generation_equal'] for r in post),'stdout_bytes':receipt['stdout']['bytes'],'stderr_bytes':receipt['stderr']['bytes']}))
if code!=0 or timeout or not all(r['hash_and_bytes_equal'] and r['generation_equal'] for r in post): raise SystemExit(1)
