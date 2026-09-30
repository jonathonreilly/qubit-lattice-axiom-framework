#!/usr/bin/env python3
"""Exact circle-height inequalities; no H builder and no frozen-file writes."""
from pathlib import Path
import datetime, hashlib, json, resource, time
P=Path(__file__).resolve().parent
R=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (R/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((R/'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
t0,c0=time.monotonic(),time.process_time()
def chi_num(s,L):
    s=(s+5)%L-5
    return s*(L-10) if s<=5 else 5*(L-10)-10*(s-5)
cases=0; tested_sides=[]; point_increments=0; same_move_checks=0
for L in range(28,406,2):
    den=L-10
    values=[chi_num(x,L) for x in range(L)]
    assert min(values)==-5*den and max(values)==5*den
    mins={}
    for d in range(1,5):
        increments=[chi_num(x+d,L)-chi_num(x,L) for x in range(L)]
        point_increments+=L
        assert min(increments)>=-10*d
        mins[d]=min(increments)
        star=sum(chi_num(x+d,L)-chi_num(x,L) for x in [-1,1,0,0,0,0])
        assert star==6*d*den
    for d in range(-2,3):
        assert all(abs(chi_num(x+d,L)-chi_num(x,L))<=2*den for x in range(L))
        same_move_checks+=L
    for k in range(7,L//4+1,2):
        assert 20*(k-6)<=5*den  # sigma*(k-6)<=5/2
        for d in range(1,5):
            lower=6*d*den+(k-6)*mins[d]
            assert 2*lower>=7*d*den
        same_hole=12*den+(k-6)*mins[2]-2*den
        spectral=12*den+(k-6)*mins[2]
        assert same_hole>=5*den and spectral>=7*den
        n=(20*k)//7+1
        assert 7*n>20*k
        cases+=1
    tested_sides.append(L)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'L_range_even':[tested_sides[0],tested_sides[-1]],'side_count':len(tested_sides),'physical_odd_k_side_pairs':cases,'exact_point_increment_checks':point_increments,'same_B_move_checks':same_move_checks,'uniform_minimum_reverse_height_rise':'7/2','same_hole_minimum_rise':5,'spectral_minimum_rise':7,'nilpotency_exponent':'floor(20*k/7)+1','cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(P/'PERIODIC_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
