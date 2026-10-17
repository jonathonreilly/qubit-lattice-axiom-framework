#!/usr/bin/env python3
from pathlib import Path
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time

root=Path(__file__).resolve().parent
env=os.environ.copy()
env['PYTHONDONTWRITEBYTECODE']='1'
argv=[sys.executable,str(root/'column_norm_check.py')]
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
clock=time.monotonic()
with (root/'check_stdout.txt').open('wb') as out, (root/'check_stderr.txt').open('wb') as err:
    try:
        p=subprocess.run(argv,cwd=root,env=env,stdout=out,stderr=err,timeout=30)
        code=p.returncode
        timed_out=False
    except subprocess.TimeoutExpired:
        code=None
        timed_out=True
def identity(p):
    b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
receipt={'argv':argv,'cwd':str(root),'started_utc':start,
    'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'elapsed_seconds':time.monotonic()-clock,'exit_code':code,'timed_out':timed_out,
    'resource_caps':{'child_cpu_seconds':10,'wall_seconds':30,'maximum_matrix_dimension':2},
    'sources':[identity(root/'column_norm_check.py'),identity(Path(__file__))],
    'stdout':identity(root/'check_stdout.txt'),'stderr':identity(root/'check_stderr.txt')}
(root/'CHECK_EXECUTION.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
sys.exit(0 if code==0 and not timed_out else 1)
