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
env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
argv=[sys.executable,str(root/'certify_interval.py')]
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
clock=time.monotonic()
with (root/'certificate.stdout').open('wb') as out,(root/'certificate.stderr').open('wb') as err:
    try:
        p=subprocess.run(argv,cwd=root,env=env,stdout=out,stderr=err,timeout=90)
        code=p.returncode; timed_out=False
    except subprocess.TimeoutExpired:
        code=None; timed_out=True
def identity(p):
    b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
receipt={'argv':argv,'cwd':str(root),'started_utc':started,
 'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'elapsed_seconds':time.monotonic()-clock,'exit_code':code,'timed_out':timed_out,
 'resource_caps':{'child_cpu_seconds':60,'wall_seconds':90,'largest_executed_matrix_dimension':16,
                  'proposed_square_root_dimension':6,'theorem_matching_dimension':24},
 'environment_requests':{k:env[k] for k in ('PYTHONDONTWRITEBYTECODE','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS')},
 'files':[identity(root/name) for name in ('certify_interval.py','run_certificate.py','SOURCE_MANIFEST.json',
          'certificate.stdout','certificate.stderr')],
 'generated_evidence':[identity(root/name) for name in ('CERTIFICATE.json','POINT_WITNESSES.json') if (root/name).exists()]}
(root/'EXECUTION.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
sys.exit(0 if code==0 and not timed_out else 1)
