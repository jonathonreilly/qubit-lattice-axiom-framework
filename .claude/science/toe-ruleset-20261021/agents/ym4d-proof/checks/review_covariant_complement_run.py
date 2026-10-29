#!/usr/bin/env python3
"""Resource-gated one-shot driver; keeps each run under a distinct stem."""
from pathlib import Path
import datetime,hashlib,json,os,re,resource,subprocess,sys,time
base=Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof/checks')
program=Path(sys.argv[1]) if len(sys.argv)>1 else base/'review_covariant_complement_independent.py'
stem=sys.argv[2] if len(sys.argv)>2 else 'review_covariant_complement_independent_01'
now=datetime.datetime.now(datetime.timezone.utc)
lock=json.loads(Path('logs/physics_worker_lock.json').read_text())
memraw=subprocess.check_output(['memory_pressure','-Q'],text=True)
free=float(re.search(r'System-wide memory free percentage:\s*([0-9.]+)%',memraw).group(1))
load=os.getloadavg()[0]
gate={'utc':now.isoformat(),'memory_pressure_raw':memraw,'system_wide_free_percentage':free,'memory_metric':'Darwin memory_pressure -Q native system-wide free percentage, not vm_stat free pages alone','load1':load,'lock':lock,'passes':free>=50 and load<20 and datetime.datetime.fromisoformat(lock['expires_at'])>now and lock['owner']=='ym4d-full-proof','nice':15,'threads':1,'rss_limit_mib':300,'cpu_limit_seconds':90,'wall_limit_seconds':90,'program':str(program),'program_sha256':hashlib.sha256(program.read_bytes()).hexdigest(),'criteria_sha256':hashlib.sha256((base/'review_covariant_complement_criteria.md').read_bytes()).hexdigest()}
(base/(stem+'_gate.json')).write_text(json.dumps(gate,indent=2)+'\n')
if not gate['passes']:
    print(json.dumps(gate));raise SystemExit(2)
env=os.environ.copy()
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:env[key]='1'
env['PYTHONDONTWRITEBYTECODE']='1'
def limits():
    os.nice(15);resource.setrlimit(resource.RLIMIT_CPU,(90,90))
start=time.monotonic();peak=0;reason=None
with (base/(stem+'.stdout.json')).open('x') as out,(base/(stem+'.stderr.txt')).open('x') as err:
    p=subprocess.Popen([sys.executable,str(program)],stdout=out,stderr=err,env=env,preexec_fn=limits)
    while p.poll() is None:
        try:
            rss=int(subprocess.check_output(['ps','-o','rss=','-p',str(p.pid)],text=True,stderr=subprocess.DEVNULL).strip() or 0)
            peak=max(peak,rss)
        except (subprocess.CalledProcessError,ValueError):pass
        if peak>300*1024:reason='RSS over 300 MiB';p.kill()
        if time.monotonic()-start>90:reason='wall over 90 seconds';p.kill()
        time.sleep(.05)
    status=p.wait()
receipt={'exit_code':status,'elapsed_seconds':time.monotonic()-start,'peak_rss_kib':peak,'termination_reason':reason,'program_sha256':gate['program_sha256'],'gate':str(base/(stem+'_gate.json')),'stdout':str(base/(stem+'.stdout.json')),'stderr':str(base/(stem+'.stderr.txt'))}
(base/(stem+'_run.json')).write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
raise SystemExit(status)
