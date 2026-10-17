#!/usr/bin/env python3
"""Record the exact bounded local execution and complete stdout/stderr."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time

root=Path(__file__).resolve().parent
script=root/'check.py'
env=os.environ.copy()
env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
argv=[sys.executable,str(script)]
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
clock=time.monotonic()
with (root/'stdout.txt').open('wb') as stdout, (root/'stderr.txt').open('wb') as stderr:
    try:
        proc=subprocess.run(argv,cwd=root,env=env,stdout=stdout,stderr=stderr,timeout=180)
        code=proc.returncode
        timeout=False
    except subprocess.TimeoutExpired:
        code=None
        timeout=True

def identity(path):
    data=path.read_bytes()
    return {'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

receipt={
    'argv':argv,'cwd':str(root),'started_utc':start,
    'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'elapsed_seconds':time.monotonic()-clock,'exit_code':code,'wall_timeout':timeout,
    'limits':{'wall_seconds':180,'child_cpu_seconds':120,'threads':1},
    'sources':{'check':identity(script),'recorder':identity(Path(__file__))},
    'stdout':identity(root/'stdout.txt'),'stderr':identity(root/'stderr.txt'),
}
(root/'EXECUTION.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
sys.exit(0 if code==0 and not timeout else 1)
