"""Serial repair of one handoff overlap, then matched 16^4 isotropic control.
Runs only after the main grid stops. The duplicated seed is reproduction,
not an independent measurement; the overlapped original remains archived.
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
for v in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    if os.environ.get(v)!='1':raise RuntimeError(v+' must be 1')
import numpy as np

jobs=[dict(L=16,beta=2.5,beta_L=2.5,beta_T=2.5,face=False,mult=1,
    chain=c,hot=bool(c),burn=2048,n=2048,stride=4,seed=31010000+131*c,
    role='matched_volume_isotropic_control') for c in (0,1)]
original=json.loads((HERE/'manifest.json').read_text())
repair=dict(next(j for j in original['jobs'] if j['L']==12 and j['beta']==2.5 and j['mult']==2 and j['chain']==0),
    serial_reproduction=True,role='serial_reproduction_after_pause_handoff')
source_hash=hashlib.sha256((HERE/'su2.cpp').read_bytes()).hexdigest()
(HERE/'extra_manifest.json').write_text(json.dumps(dict(source_sha256=source_hash,
    purpose='Matched published beta=2.5 16^4 control; added after inspecting 8^4/12^4 isotropic controls',
    jobs=jobs,repair_jobs=[repair]),indent=2)+'\n')
for j in [repair]+jobs:
    tag=f"L{j['L']}_b{j['beta']:.1f}_{j['mult']}_c{j['chain']}"
    receipt=HERE/(tag+'.json')
    is_repair=j.get('serial_reproduction',False)
    archived=HERE/'handoff_overlap'
    if is_repair and not (archived/(tag+'.json')).exists():
        archived.mkdir(exist_ok=True);scratch_archive=SCRATCH/'handoff_overlap';scratch_archive.mkdir(exist_ok=True)
        # The completed original is preserved before the serial replacement.
        for suffix in ('.npz','.log','.therm.csv','.json'):
            (HERE/(tag+suffix)).rename(archived/(tag+suffix))
        for suffix in ('.f32','.cfg','.therm.csv'):
            (SCRATCH/(tag+suffix)).rename(scratch_archive/(tag+suffix))
    if receipt.exists():
        old=json.loads(receipt.read_text())
        if old.get('complete') and (not is_repair or old.get('serial_reproduction')) and hashlib.sha256((HERE/(tag+'.npz')).read_bytes()).hexdigest()==old['archive_sha256']:
            print(tag,'ALREADY COMPLETE',flush=True);continue
    status=subprocess.run([sys.executable,str(ROOT/'scripts/lab_ops.py'),'numeric-lock','status'],text=True,capture_output=True,check=True)
    if json.loads(status.stdout).get('lock',{}).get('holder_id')!=HOLDER:raise RuntimeError('numeric lock lost')
    subprocess.run([sys.executable,str(ROOT/'scripts/lab_ops.py'),'numeric-lock','refresh','--holder',HOLDER,'--ttl-hours','3'],check=True)
    pressure=subprocess.run(['memory_pressure','-Q'],capture_output=True,text=True,check=True).stdout
    free=int(re.search(r'free percentage:\s*(\d+)',pressure)[1])
    if free<50:raise RuntimeError('50% free memory gate')
    prefix=SCRATCH/tag
    args=[str(SCRATCH/'su2'),str(j['L']),str(j['beta_L']),str(j['beta']),str(j['beta_T']),'0',str(j['seed']),str(j['chain']),str(j['burn']),str(j['n']),str(j['stride']),str(prefix)]
    started=dt.datetime.now(dt.timezone.utc).isoformat();t=time.monotonic()
    print(started,tag,'START',flush=True)
    with (HERE/(tag+'.log')).open('w') as log:subprocess.run(args,stdout=log,stderr=subprocess.STDOUT,check=True)
    a=np.fromfile(str(prefix)+'.f32',dtype='<f4').reshape(j['n'],54*j['L']+24)
    np.savez_compressed(HERE/(tag+'.npz'),records=a)
    (HERE/(tag+'.therm.csv')).write_bytes(Path(str(prefix)+'.therm.csv').read_bytes())
    peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if (peak if sys.platform=='darwin' else peak*1024)>2e9:raise RuntimeError('2 GB RSS stop')
    raw_hash=hashlib.sha256(a.tobytes()).hexdigest()
    if is_repair:
        old=json.loads((archived/(tag+'.json')).read_text())
        if raw_hash!=old['raw_sha256']:raise RuntimeError('serial reproduction changed raw measurements')
        checks={}
        for suffix in ('.cfg','.therm.csv'):
            a_hash=hashlib.sha256((SCRATCH/(tag+suffix)).read_bytes()).hexdigest()
            b_hash=hashlib.sha256((SCRATCH/'handoff_overlap'/(tag+suffix)).read_bytes()).hexdigest()
            if a_hash!=b_hash:raise RuntimeError('serial reproduction changed '+suffix)
            checks[suffix]=a_hash
        (HERE/'serial_reproduction.json').write_text(json.dumps(dict(tag=tag,
            reason='Controller/sampler handoff race overlapped the original with beta=2.5 control analysis',
            original_receipt='handoff_overlap/'+tag+'.json',same_seed=True,independent_replication=False,
            raw_sha256=raw_hash,other_matching_hashes=checks),indent=2)+'\n')
    receipt.write_text(json.dumps(dict(j,complete=True,started=started,
        seconds=time.monotonic()-t,free_pct=free,nice=os.getpriority(os.PRIO_PROCESS,0),args=args,
        source_sha256=source_hash,raw_sha256=raw_hash,
        archive_sha256=hashlib.sha256((HERE/(tag+'.npz')).read_bytes()).hexdigest()),indent=2)+'\n')
    print(tag,'DONE',flush=True)
