#!/usr/bin/env python3
"""Bounded deterministic parameter screen; launches no agents or API calls."""
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,subprocess,sys,time

HERE=Path(__file__).resolve().parent
DEADLINE=datetime(2026,9,21,11,32,19,tzinfo=timezone.utc)
CASES=[(p,e) for p in (1,3,6,12) for e in (.1,.01) if (p,e)!=(3,.01)]

def one(case):
    p,eps=case;code='01' if eps==.1 else '001';name=f'cubic_L8_p{p}_e{code}'
    out=HERE/(name+'.json');log=HERE/(name+'.log')
    if out.exists():raise RuntimeError(f'output already exists: {out}; inspect before resuming')
    remaining=int((DEADLINE-datetime.now(timezone.utc)).total_seconds())
    if remaining<=0:return {'case':name,'status':'deadline_not_started'}
    cmd=[sys.executable,str(HERE/'growing_sim.py'),'--side','8','--dim','3','--p',str(p),'--q','1','--r',str(1 if p==1 else 2),'--epsilon',str(eps),'--reps','128','--seed','20261000','--out',str(out)]
    start=time.monotonic()
    with log.open('w') as stream:
        result=subprocess.run(cmd,stdout=stream,stderr=subprocess.STDOUT,timeout=remaining)
    record={'case':name,'command':cmd,'exit_code':result.returncode,'wall_sec':time.monotonic()-start,'log':str(log),'log_sha256':hashlib.sha256(log.read_bytes()).hexdigest()}
    if result.returncode==0:
        assert out.exists() and out.with_suffix('.npz').exists()
        record['json_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
        record['npz_sha256']=hashlib.sha256(out.with_suffix('.npz').read_bytes()).hexdigest()
    return record

if __name__=='__main__':
    records=[]
    with ThreadPoolExecutor(max_workers=2) as pool:
        for f in as_completed([pool.submit(one,c) for c in CASES]):
            record=f.result();records.append(record)
            print(json.dumps(record),flush=True)
            (HERE/'SCREEN_EXECUTIONS.json').write_text(json.dumps(records,indent=2)+'\n')
    assert all(r.get('exit_code')==0 for r in records)
