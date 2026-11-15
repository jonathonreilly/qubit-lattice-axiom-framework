#!/usr/bin/env python3
"""Run one owned numerical program with preserved resource gates and outputs."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import time

base=Path(__file__).resolve().parent
program=base/sys.argv[1]
tag=sys.argv[2]
assert program.parent==base and program.name.startswith('covariant_complement_')
assert re.fullmatch('[a-zA-Z0-9_]+',tag)
prefix=base/('covariant_complement_'+tag)
lock=json.loads(Path('logs/physics_worker_lock.json').read_text())
mem=subprocess.check_output(['memory_pressure','-Q'],text=True)
pct=int(re.search(r'System-wide memory free percentage: (\d+)%',mem).group(1))
now=datetime.datetime.now(datetime.timezone.utc)
gate=dict(utc=now.isoformat(),lock=lock,memory_output=mem,free_memory_percent=pct,minimum_memory_percent=50,
          load=list(os.getloadavg()),load_limit=os.cpu_count()/2,free_disk_gib=shutil.disk_usage('.').free/2**30,
          memory_limit_mib=300,wall_limit_seconds=90,
          enforcement='RSS watchdog at .25s, CPU soft limit 90s, nice15, library threads1; Darwin rejected direct RSS limits')
gate['passed']=(pct>=50 and gate['load'][0]<=gate['load_limit'] and gate['free_disk_gib']>1 and
                lock['owner']=='ym4d-full-proof' and now<datetime.datetime.fromisoformat(lock['expires_at']))
gatepath=Path(str(prefix)+'_gate.json')
assert not gatepath.exists()
gatepath.write_text(json.dumps(gate,indent=2)+'\n')
print(json.dumps(gate,indent=2),flush=True)
if not gate['passed']: raise SystemExit(75)
env=os.environ.copy()
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'): env[k]='1'
runner='import resource,runpy; resource.setrlimit(resource.RLIMIT_CPU,(90,resource.getrlimit(resource.RLIMIT_CPU)[1])); runpy.run_path('+repr(str(program))+',run_name="__main__")'
t0=time.monotonic(); peak=0; reason=None
with Path(str(prefix)+'_output.txt').open('w') as out,Path(str(prefix)+'_stderr.txt').open('w') as err:
    p=subprocess.Popen(['nice','-n','15',sys.executable,'-c',runner],env=env,stdout=out,stderr=err,start_new_session=True)
    while p.poll() is None:
        rss=subprocess.run(['ps','-o','rss=','-p',str(p.pid)],text=True,capture_output=True).stdout.strip()
        if rss: peak=max(peak,int(rss))
        if peak>300*1024: reason='RSS memory cap'; os.killpg(p.pid,signal.SIGTERM)
        if time.monotonic()-t0>90: reason='wall-time cap'; os.killpg(p.pid,signal.SIGTERM)
        time.sleep(.25)
    rc=p.wait()
run=dict(exit_code=rc,elapsed_seconds=time.monotonic()-t0,peak_rss_kib=peak,termination_reason=reason,
         program=str(program),program_sha256=hashlib.sha256(program.read_bytes()).hexdigest())
Path(str(prefix)+'_run.json').write_text(json.dumps(run,indent=2)+'\n')
print(json.dumps(run,indent=2),flush=True)
raise SystemExit(rc)
