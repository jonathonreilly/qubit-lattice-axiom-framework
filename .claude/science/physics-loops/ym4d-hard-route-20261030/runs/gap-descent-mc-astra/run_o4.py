"""Run with the grid finished or BOTH its controller and sampler paused.
Keeps the machine numeric lease; verifies and skips completed control archives.
"""
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import sys
import time
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[5]
scratch=Path(sys.argv[1])
holder='gap-descent-mc-astra-16c93871f'
for v in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    if os.environ.get(v)!='1':raise RuntimeError(v+' must be 1')
for beta in (2.3,2.4,2.5):
  for L in (8,12,128):
    for chain in (0,1):
        tag=f'o4_L{L}_b{beta:.1f}_c{chain}'
        receipt=HERE/(tag+'.json');archive=HERE/(tag+'.csv.gz')
        if receipt.exists() and archive.exists():
            old=json.loads(receipt.read_text())
            if hashlib.sha256(archive.read_bytes()).hexdigest()!=old['archive_sha256']:
                raise RuntimeError('archive changed: '+tag)
            if hashlib.sha256((HERE/'o4_control.cpp').read_bytes()).hexdigest()!=old['source_sha256']:
                raise RuntimeError('control source changed: '+tag)
            print(tag,'ALREADY COMPLETE',flush=True)
            continue
        subprocess.run([sys.executable,str(ROOT/'scripts/lab_ops.py'),'numeric-lock','refresh','--holder',holder,'--ttl-hours','3'],check=True)
        pressure=subprocess.run(['memory_pressure','-Q'],capture_output=True,text=True,check=True).stdout
        if int(re.search(r'free percentage:\s*(\d+)',pressure)[1])<50:raise RuntimeError('memory gate')
        path=scratch/(tag+'.csv');seed=22010000+int(beta*10)*101+chain*131+L*1009
        args=[str(scratch/'o4_control'),str(L),str(beta),str(seed),str(chain),'4096','8192',str(path)]
        t=time.monotonic()
        with (HERE/(tag+'.log')).open('w') as f:subprocess.run(args,stdout=f,stderr=subprocess.STDOUT,check=True)
        with gzip.open(HERE/(tag+'.csv.gz'),'wb') as f:f.write(path.read_bytes())
        peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if (peak if sys.platform=='darwin' else peak*1024)>2e9:raise RuntimeError('2 GB RSS stop')
        (HERE/(tag+'.json')).write_text(json.dumps(dict(args=args,seconds=time.monotonic()-t,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),archive_sha256=hashlib.sha256((HERE/(tag+'.csv.gz')).read_bytes()).hexdigest(),source_sha256=hashlib.sha256((HERE/'o4_control.cpp').read_bytes()).hexdigest(),su2_sha256=hashlib.sha256((HERE/'su2.cpp').read_bytes()).hexdigest()),indent=2)+'\n')
        print(tag,'DONE',flush=True)
