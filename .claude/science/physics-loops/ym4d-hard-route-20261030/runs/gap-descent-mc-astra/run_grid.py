"""Serial GUIDE grid. Run under nice 10 with the already acquired machine lock.
No configurations enter the checkout. Every input and raw slice record is saved.
"""
import datetime as dt
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
SCRATCH=Path(sys.argv[1]).resolve()
HOLDER='gap-descent-mc-astra-16c93871f'
for var in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    if os.environ.get(var)!='1': raise RuntimeError(f'{var} must be 1')
import numpy as np

def cmd_lock(action):
    p=subprocess.run([sys.executable,str(ROOT/'scripts/lab_ops.py'),'numeric-lock',action,'--holder',HOLDER,'--ttl-hours','3'],text=True,capture_output=True,check=True)
    data=json.loads(p.stdout)
    if action=='status' and data.get('lock',{}).get('holder_id')!=HOLDER: raise RuntimeError('machine lock lost')
    return data

def gate():
    cmd_lock('status')
    mem=subprocess.run(['memory_pressure','-Q'],text=True,capture_output=True,check=True)
    m=re.search(r'free percentage:\s*(\d+)',mem.stdout)
    if m is None or int(m[1])<50: raise RuntimeError('50% free memory gate failed: '+mem.stdout)
    peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if (peak if sys.platform=='darwin' else peak*1024)>2e9: raise RuntimeError('2 GB driver RSS gate')
    return int(m[1])

jobs=[]
# Interleave sizes at fixed physics point. Independent hot/cold starts.
for beta in (2.3,2.4,2.5):
    for mult in (1,2,4,8,'face','anchor'):
        for L in (8,12):
            for chain in (0,1):
                face=mult in ('face','anchor')
                jobs.append(dict(L=L,beta=beta,beta_L=0 if face else beta*mult,
                    beta_T=0 if mult=='anchor' else beta,face=face,mult=mult,
                    chain=chain,hot=chain==1,burn=2048,n=2048,stride=4,
                    seed=11020000+len(jobs)*131))

manifest=dict(source='16c93871f140b78f3d5b69de4b5b9de720e2f474',
    source_sha256=hashlib.sha256((HERE/'su2.cpp').read_bytes()).hexdigest(),
    scratch=str(SCRATCH),nice=os.getpriority(os.PRIO_PROCESS,0),
    format='float32: 48*L slice values; 24 Wilson means; 6*L winding slices',
    layout='axis [0,2], APE steps [0,8], plane [01,02,03,12,13,23], shape [P,R], slice',
    jobs=jobs)
(HERE/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
for j in jobs:
    tag=f"L{j['L']}_b{j['beta']:.1f}_{j['mult']}_c{j['chain']}"
    receipt=HERE/(tag+'.json')
    if receipt.exists():
        old=json.loads(receipt.read_text())
        if old.get('complete') and (HERE/(tag+'.npz')).exists(): continue
    free=gate();cmd_lock('refresh')
    prefix=SCRATCH/tag
    args=[str(SCRATCH/'su2'),str(j['L']),str(j['beta_L']),str(j['beta']),str(j['beta_T']),str(int(j['face'])),str(j['seed']),str(int(j['hot'])),str(j['burn']),str(j['n']),str(j['stride']),str(prefix)]
    start=dt.datetime.now(dt.timezone.utc).isoformat();t=time.monotonic()
    print(start,tag,'START',flush=True)
    with (HERE/(tag+'.log')).open('w') as log:
        subprocess.run(args,stdout=log,stderr=subprocess.STDOUT,check=True)
    a=np.fromfile(str(prefix)+'.f32',dtype='<f4').reshape(j['n'],54*j['L']+24)
    payload={'records':a}
    if j['mult']=='anchor':payload['spin']=np.fromfile(str(prefix)+'.spin.f32',dtype='<f4').reshape(j['n'],j['L']//2+1)
    np.savez_compressed(HERE/(tag+'.npz'),**payload)
    (HERE/(tag+'.therm.csv')).write_bytes(Path(str(prefix)+'.therm.csv').read_bytes())
    data=dict(j,complete=True,started=start,seconds=time.monotonic()-t,free_pct=free,
        args=args,raw_sha256=hashlib.sha256(a.tobytes()).hexdigest(),
        archive_sha256=hashlib.sha256((HERE/(tag+'.npz')).read_bytes()).hexdigest())
    receipt.write_text(json.dumps(data,indent=2)+'\n')
    print(tag,'DONE',round(data['seconds'],2),flush=True)
print('GRID COMPLETE',flush=True)
