#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,os,subprocess,sys,time
root=Path(__file__).resolve().parent
env=os.environ.copy();env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
start=time.monotonic();started=datetime.datetime.now(datetime.timezone.utc).isoformat()
argv=[sys.executable,str(root/'checks.py')]
with (root/'check_stdout.json').open('wb') as out,(root/'check_stderr.txt').open('wb') as err:
    try:
        run=subprocess.run(argv,cwd=root,env=env,stdout=out,stderr=err,timeout=30)
        code=run.returncode;timed_out=False
    except subprocess.TimeoutExpired:
        code=None;timed_out=True
def identity(p):
    b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
receipt=dict(argv=argv,cwd=str(root),started_utc=started,
             elapsed_seconds=time.monotonic()-start,exit_code=code,timed_out=timed_out,
             resource_caps=dict(cpu_seconds=15,wall_seconds=30,maximum_matrix_dimension=14),
             sources=[identity(root/'checks.py'),identity(Path(__file__))],
             outputs=[identity(root/'check_stdout.json'),identity(root/'check_stderr.txt')])
(root/'EXECUTION.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
sys.exit(0 if code==0 and not timed_out else 1)
