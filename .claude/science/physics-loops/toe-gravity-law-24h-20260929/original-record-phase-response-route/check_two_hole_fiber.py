"""Sparse exact rows of the physically embedded zero-angle charge fiber.

This does not enumerate the physical field carrier or sample an eigenvalue.
Every row is assembled by a literal inward then outward endpoint operation.
"""
import hashlib
import json
import os
from pathlib import Path
import resource
import time

START_WALL = time.monotonic()
START_CPU = time.process_time()
HERE = Path(__file__).resolve().parent
RUNTIME = Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
DEADLINE = json.loads((RUNTIME / 'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
assert all(os.environ.get(k) == '1' for k in
           ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'))

def guard():
    assert not (RUNTIME / 'STOP_REQUESTED.json').exists(), 'STOP requested'
    assert time.time() < DEADLINE, 'campaign deadline'
    assert time.monotonic() - START_WALL < 90, 'wall price exceeded'

guard()
L = 8
sites = [(x,y,z) for x in range(L) for y in range(L) for z in range(L)]
A = [x for x in sites if sum(x) % 2 == 0]
N = len(A)
origin = (0,0,0)
steps = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

def neighbors(x):
    return [tuple((x[i]+s[i]) % L for i in range(3)) for s in steps]

def row(h,u):
    hrow, qrow = {}, {}
    for filled, remaining in ((h,u),(u,h)):
        for b in neighbors(filled):
            # Inward F*: b's record fills one hole, leaving this B vacant.
            loss = 2 if b in neighbors(remaining) else 0
            for c in neighbors(b):
                if c == remaining:
                    continue  # the remaining A hole cannot hop outward
                out = tuple(sorted((remaining,c)))
                hrow[out] = hrow.get(out,0) + 1
                qrow[out] = qrow.get(out,0) + loss
    return hrow, {x:y for x,y in qrow.items() if y}

trace_q = covariance = trace_hcenter2 = trace_q2 = 0
rows = 0
max_h_sum = max_q_sum = 0
for u in A:
    if u == origin:
        continue
    guard()
    hrow, qrow = row(origin,u)
    own = tuple(sorted((origin,u)))
    assert hrow[own] == 12
    assert qrow.get(own,0) == 4*len(set(neighbors(origin)) & set(neighbors(u)))
    max_h_sum = max(max_h_sum, sum(hrow.values()))
    max_q_sum = max(max_q_sum, sum(qrow.values()))
    for out, value in hrow.items():
        back_h, back_q = row(*out)
        assert back_h.get(own,0) == value
        assert back_q.get(own,0) == qrow.get(out,0)
    trace_q += qrow.get(own,0)
    covariance += sum(v*(hrow.get(out,0)-(12 if out == own else 0)) for out,v in qrow.items())
    trace_hcenter2 += sum((v-(12 if out == own else 0))**2 for out,v in hrow.items())
    trace_q2 += sum(v*v for v in qrow.values())
    rows += 1

# Translation transitivity and unordered pair counting multiply each sum by N/2.
actual = dict(trace_q=trace_q*N//2, covariance=covariance*N//2,
              trace_hcenter2=trace_hcenter2*N//2, trace_q2=trace_q2*N//2)
expected = dict(trace_q=60*N, covariance=432*N,
                trace_hcenter2=54*N*(N-2), trace_q2=912*N)
assert actual == expected, (actual,expected)
assert max_h_sum <= 72 and max_q_sum <= 144
guard()
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 120*1024*1024
result = dict(status='all exact checks satisfied', L=L, N=N, streamed_rows=rows,
              actual=actual, expected=expected, max_h_row_sum=max_h_sum,
              max_q_row_sum=max_q_sum, cpu_seconds=time.process_time()-START_CPU,
              wall_seconds=time.monotonic()-START_WALL, peak_rss_bytes=rss,
              runner_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              scope='Exact reduced physical zero-angle fiber rows; analytic proof supplies embedding and all-volume formulas.')
(HERE/'CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
