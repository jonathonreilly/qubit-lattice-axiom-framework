"""Replay selected original marked paths for arbitrarily sized finite B islands.
This checks source accessibility, not a probability bound or a projected process.
"""
from collections import defaultdict
from itertools import product
from pathlib import Path
import hashlib
import json
import resource
import time

HERE = Path(__file__).resolve().parent
RUNTIME = Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (RUNTIME / 'STOP_REQUESTED.json').exists()
assert time.time() < json.loads((RUNTIME / 'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU, (10, 11))
start = time.process_time()
rows = []
for R in (5, 7, 19):
    M = (R+6)//4
    q, E, divergence = {}, {}, defaultdict(int)
    default = lambda v: 1-sum(v)%2
    charge = lambda v: q.get(v, default(v))
    births = 0
    def move(a, b, birth=False):
        assert sum(a)%2 == 0 and sum(b)%2 == 1
        assert sum(abs(x-y) for x, y in zip(a,b)) == 1
        if birth:
            assert charge(a) == charge(b) == 0
            q[a], q[b], step = 1, -1, 1
        else:
            assert charge(a) == 1 and charge(b) == 0
            q[a], q[b], step = 0, 1, -1
        assert (a,b) not in E  # every shift is exactly zero to +/-one
        E[a,b] = step
        divergence[a] += step
        divergence[b] -= step
        assert divergence[a]+default(a)-charge(a) == 0
        assert divergence[b]+default(b)-charge(b) == 0
    for y,z in product(range(-R,R+1), repeat=2):
        if (y,z) == (0,0):
            lines = [list(range(-4*M+1,0,2)), list(range(3,4*M+2,2))]
        else:
            p = (1-y-z)%2
            lines = [list(range(-4*M+p,4*M+p,2))]
        for line in lines:
            assert len(line)%2 == 0
            for x,x2 in zip(line[::2],line[1::2]):
                a,b,c = (x+1,y,z),(x,y,z),(x2,y,z)
                move(a,b)
                move(a,c,True)
                births += 1
    move((0,0,0),(1,0,0))
    assert all(divergence[v]+default(v)-charge(v) == 0 for v in set(q)|set(divergence))
    B = {v for v,c in q.items() if sum(v)%2 and c}
    assert len(B) == 4*M*(2*R+1)**2+1 == 2*births+1
    assert [v for v,c in q.items() if sum(v)%2 == 0 and c == 0] == [(0,0,0)]
    wanted = {v for v in product(range(-R,R+1),repeat=3) if sum(v)%2}
    assert wanted <= B
    assert max(map(abs,E.values())) == 1
    rows.append({'R':R,'M':M,'actual_marks':births,'B_occupants':len(B),
                 'required_cube_B_sites':len(wanted),'all_required_B_filled':True,
                 'single_A_hole':(0,0,0),'gauss_exact':True,
                 'all_selected_hop_and_birth_weights_one_for_every_integer_S_ge1':True})
result = {'selected_paths':rows,'cpu_seconds':time.process_time()-start,
          'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
assert result['peak_rss_bytes'] < 150*1024**2
(HERE/'SOURCE_ISLAND_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
