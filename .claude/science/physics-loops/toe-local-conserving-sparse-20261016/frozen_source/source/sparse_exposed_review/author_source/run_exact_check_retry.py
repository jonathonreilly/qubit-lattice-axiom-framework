"""Bounded single-launch receipt; preserves failures and complete streams."""
from pathlib import Path
import datetime
import hashlib
import json
import resource
import subprocess
import sys
import time

root=Path(__file__).resolve().parent
run=root/'runs'/'exact_sparse_check_retry'
run.mkdir(parents=True,exist_ok=False)
source=(root/'exact_sparse_check.py').read_bytes()
snapshot=run/'SOURCE_AT_LAUNCH.py'
snapshot.write_bytes(source)
launcher=Path(__file__).read_bytes()
(run/'LAUNCHER_AT_LAUNCH.py').write_bytes(launcher)
argv=[sys.executable,str(snapshot)]
record={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'argv':argv,'cwd':str(root),'source_sha256':hashlib.sha256(source).hexdigest(),
        'launcher_sha256':hashlib.sha256(launcher).hexdigest(),
        'wall_seconds_limit':90,'cpu_seconds_limit':60,
        'address_space_bytes_limit':None,
        'retry_reason':'Original launch failed in preexec_fn before scientific source started; retry removes address-space limit, preserves 90s wall/60s CPU bounds. Exact preexec failure cause was not exposed.',
        'stdout':'stdout.txt','stderr':'stderr.txt'}
(run/'EXECUTION.json').write_text(json.dumps(record,indent=2)+'\n')
def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(60,60))
start=time.monotonic()
try:
    result=subprocess.run(argv,cwd=root,capture_output=True,timeout=90,preexec_fn=limits)
    stdout,stderr=result.stdout,result.stderr
    record['exit_code']=result.returncode
except subprocess.TimeoutExpired as exc:
    stdout,stderr=exc.stdout or b'',exc.stderr or b''
    record['exit_code']=None
    record['failure']='Wall timeout'
except Exception as exc:
    stdout,stderr=b'',repr(exc).encode()
    record['exit_code']=None
    record['failure']='Launcher exception'
(run/'stdout.txt').write_bytes(stdout)
(run/'stderr.txt').write_bytes(stderr)
record['elapsed_wall_seconds']=time.monotonic()-start
record['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
record['source_sha256_after']=hashlib.sha256(snapshot.read_bytes()).hexdigest()
record['stdout_sha256']=hashlib.sha256(stdout).hexdigest()
record['stderr_sha256']=hashlib.sha256(stderr).hexdigest()
(run/'EXECUTION.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
print(stdout.decode(errors='replace'))
print(stderr.decode(errors='replace'),file=sys.stderr)
sys.exit(0 if record.get('exit_code')==0 else 1)
