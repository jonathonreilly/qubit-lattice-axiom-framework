"""One bounded review run with a durable prelaunch byte binding."""
import datetime, hashlib, importlib.metadata, importlib.util, json, os
import resource, subprocess, sys, time
from pathlib import Path

sys.dont_write_bytecode = True
ROOT=Path(__file__).resolve().parent
RUN=ROOT/'run01'
RUN.mkdir(exist_ok=False)

def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def ident(path):
    p=Path(path).resolve()
    data=p.read_bytes(); st=p.stat()
    return dict(path=str(p),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),
                device=st.st_dev,inode=st.st_ino,mtime_ns=st.st_mtime_ns)

def save(path,data):
    if not isinstance(data,bytes): data=(json.dumps(data,indent=2)+'\n').encode()
    with path.open('xb') as out:
        out.write(data);out.flush();os.fsync(out.fileno())

save(RUN/'executed_source.py',(ROOT/'check_independent.py').read_bytes())
static=[ROOT/x for x in ('capture_initial_sources.py','RESOURCE_PLAN.json',
        'INITIAL_SOURCE_BINDINGS.json','INDEPENDENT_DERIVATION.md','check_independent.py','launch_independent.py')]
static+=sorted((ROOT/'inputs').glob('*'))
static+=[RUN/'executed_source.py']
dist=importlib.metadata.distribution('sympy')
metadata=next(dist.locate_file(p) for p in dist.files if str(p).endswith('.dist-info/METADATA'))
runtimes=[Path(sys.executable).resolve(),Path(importlib.util.find_spec('sympy').origin),Path(metadata),
          Path(importlib.util.find_spec('fractions').origin)]
binding= [ident(p) for p in static+runtimes]
plan=json.loads((ROOT/'RESOURCE_PLAN.json').read_text())
environment=os.environ.copy()
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    environment[name]='1'
environment['PYTHONDONTWRITEBYTECODE']='1'
command=[str(Path(sys.executable).resolve()),'-B',str(RUN/'executed_source.py')]
pre=dict(serialization_started_utc=utc(),command=command,cwd=str(RUN),bindings=binding,
         python=sys.version,resource_plan=plan,runtime_binding='Partial file byte identities, not transitive runtime closure.',
         thread_environment={k:environment[k] for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','PYTHONDONTWRITEBYTECODE')})
save(RUN/'PRELAUNCH.json',pre)
pre_fsync_completed=utc()
# Persist the directory entries, too, before any child is launched.
fd=os.open(RUN,os.O_RDONLY)
try: os.fsync(fd)
finally: os.close(fd)
directory_fsync_completed=utc()
pre_identity=ident(RUN/'PRELAUNCH.json')

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(30,30))

before=resource.getrusage(resource.RUSAGE_CHILDREN)
wall_start=time.monotonic()
launch_boundary=utc()
child=subprocess.Popen(command,cwd=RUN,env=environment,stdout=subprocess.PIPE,stderr=subprocess.PIPE,preexec_fn=caps)
timed_out=False
try:
    stdout,stderr=child.communicate(timeout=45)
except subprocess.TimeoutExpired:
    timed_out=True;child.kill();stdout,stderr=child.communicate()
completed=utc(); elapsed=time.monotonic()-wall_start
after=resource.getrusage(resource.RUSAGE_CHILDREN)
save(RUN/'stdout.json',stdout);save(RUN/'stderr.txt',stderr)
unchanged=[dict(path=x['path'],unchanged=ident(x['path'])==x) for x in binding]
receipt=dict(prelaunch=pre_identity,prelaunch_fsync_completed_utc=pre_fsync_completed,
             directory_fsync_completed_utc=directory_fsync_completed,post_fsync_pre_popen_utc=launch_boundary,
             completed_utc=completed,returncode=child.returncode,timeout=timed_out,wall_seconds=elapsed,
             child_user_cpu_seconds=after.ru_utime-before.ru_utime,
             child_system_cpu_seconds=after.ru_stime-before.ru_stime,
             macos_peak_child_rss_bytes=after.ru_maxrss,
             stdout=ident(RUN/'stdout.json'),stderr=ident(RUN/'stderr.txt'),
             resource_caps_actual=dict(cpu_soft=30,cpu_hard=30,external_wall=45,memory='measured only'),
             postlaunch_bindings=unchanged,source_equals_executed=(ROOT/'check_independent.py').read_bytes()==(RUN/'executed_source.py').read_bytes())
save(RUN/'RECEIPT.json',receipt)
print(json.dumps(receipt,indent=2))
if child.returncode or timed_out or not all(x['unchanged'] for x in unchanged):
    raise SystemExit(child.returncode or 1)
