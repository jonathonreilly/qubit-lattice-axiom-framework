#!/usr/bin/env python3
"""Predeclared bounded local simulations; no agent or API delegation."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
OUT = HERE / 'volume_followup'
DEADLINE = datetime(2026, 9, 21, 11, 32, 19, tzinfo=timezone.utc)
CASES = [(side, p, eps, rho) for side in (6, 12, 16)
         for p in (3, 12) for eps in (.1, .01) for rho in (.25, .05)]


def one(case):
    side, p, eps, rho = case
    name = f'L{side}_p{p}_eps{eps}_rho{rho}'
    path = OUT / (name + '.json')
    if path.exists():
        raise RuntimeError(f'Inspect existing result before resuming: {path}')
    remaining = int((DEADLINE - datetime.now(timezone.utc)).total_seconds())
    if remaining <= 0:
        return {'case': name, 'status': 'deadline_not_started'}
    cmd = [sys.executable, str(HERE / 'growing_sim.py'), '--side', str(side),
           '--dim', '3', '--p', str(p), '--q', '1', '--r', '2', '--epsilon',
           str(eps), '--rho0', str(rho), '--reps', '512', '--seed', '20272000',
           '--out', str(path)]
    began = time.monotonic()
    with path.with_suffix('.log').open('w') as stream:
        try:
            done = subprocess.run(cmd, stdout=stream, stderr=subprocess.STDOUT,
                                  timeout=remaining)
            status = {'exit_code': done.returncode}
        except subprocess.TimeoutExpired:
            status = {'status': 'campaign_deadline_timeout'}
    record = {'case': name, 'command': cmd, 'wall_seconds': time.monotonic()-began,
              **status}
    for file in (path, path.with_suffix('.log'), path.with_suffix('.npz')):
        if file.exists():
            record[file.suffix + '_sha256'] = hashlib.sha256(file.read_bytes()).hexdigest()
    return record


if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    results = []
    with ThreadPoolExecutor(max_workers=2) as pool:
        for future in as_completed([pool.submit(one, case) for case in CASES]):
            row = future.result()
            results.append(row)
            (OUT / 'EXECUTIONS.json').write_text(json.dumps(results, indent=2)+'\n')
            print(json.dumps(row), flush=True)
    assert all(row.get('exit_code') == 0 for row in results)
