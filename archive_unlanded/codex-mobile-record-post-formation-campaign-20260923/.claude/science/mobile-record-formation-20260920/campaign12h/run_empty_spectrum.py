#!/usr/bin/env python3
"""Execute the declared finite empty-start spectrum screen locally."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
OUT = HERE/'empty_spectrum'
DEADLINE = datetime(2026,9,21,11,32,19,tzinfo=timezone.utc)
CASES = [(side,p,mobility,eps,128) for side in (8,16) for p in (3,12)
         for mobility,eps in ((0.,.1),(1.,.1),(1.,.01))]
CASES.append((8,1,1.,.1,512))


def one(case):
    side,p,mobility,eps,reps = case
    name = f'L{side}_p{p}_mobility{mobility}_eps{eps}'
    out = OUT/(name+'.json')
    if out.exists() or out.with_suffix('.npz').exists():
        raise RuntimeError(f'Inspect existing evidence before resuming {out}')
    remaining = int((DEADLINE-datetime.now(timezone.utc)).total_seconds())
    if remaining <= 0:
        return {'case':name,'status':'deadline_not_started'}
    cmd = [sys.executable,str(HERE/'growing_spectrum.py'),'--side',str(side),
           '--p',str(p),'--r',str(1 if p == 1 else 2),'--epsilon',str(eps),
           '--mobility',str(mobility),'--reps',str(reps),'--seed','20284000',
           '--out',str(out)]
    began = time.monotonic()
    with out.with_suffix('.log').open('w') as stream:
        try:
            done = subprocess.run(cmd,stdout=stream,stderr=subprocess.STDOUT,timeout=remaining)
            status = {'exit_code':done.returncode}
        except subprocess.TimeoutExpired:
            status = {'status':'campaign_deadline_timeout'}
    record = {'case':name,'command':cmd,'wall_seconds':time.monotonic()-began,**status}
    for path in (out,out.with_suffix('.log'),out.with_suffix('.npz')):
        if path.exists():
            record[path.suffix+'_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
    return record


if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    results = []
    with ThreadPoolExecutor(max_workers=2) as pool:
        for future in as_completed([pool.submit(one,case) for case in CASES]):
            row = future.result(); results.append(row)
            (OUT/'EXECUTIONS.json').write_text(json.dumps(results,indent=2)+'\n')
            print(json.dumps(row),flush=True)
    assert all(row.get('exit_code') == 0 for row in results)
