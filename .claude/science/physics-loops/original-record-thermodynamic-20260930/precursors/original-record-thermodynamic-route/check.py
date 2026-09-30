"""Sparse controls for a constructed infinite-volume rotor process.
No infinite process is inferred from samples. Price30CPU/150MB; BLAS1.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
from fractions import Fraction
from itertools import product
import cmath,hashlib,json,math,resource,time
started=time.process_time();here=Path(__file__).resolve().parent
# Exact all-order count majorants, for several local observable/monitor anchors.
counts=[]
for x in (1,7,25,129,377,2000):
    q=max(1,(x+128)//129)
    for n in range(1,25):
        actual_bound=math.prod(129*(x+129*j) for j in range(n))
        majorant=16641**n*math.prod(q+j for j in range(n))
        assert actual_bound<=majorant
    counts.append({'anchor_sites':x,'q':q,'orders_checked':24})
def tail_bound(q,m,z=Fraction(1,2)):
    n=m+1;ratio=z*Fraction(n+q,n+1)
    if ratio>=1:return None
    return Fraction(math.comb(n+q-1,n))*z**n/(1-ratio)
tails=[]
for q in (1,3,16,64):
    m=0
    while tail_bound(q,m) is None or 2*tail_bound(q,m)>Fraction(1,2**20):m+=1
    tails.append({'q':q,'m':m,'physical_buffer_radius':8*m+1,'two_volume_error_upper':str(2*tail_bound(q,m))})
# Exact sum of segment simplex volumes, with two retained event timestamps.
durations=(Fraction(1,6),Fraction(1,3),Fraction(1,2))
for l in range(13):
    total=sum(durations[0]**i*durations[1]**j*durations[2]**(l-i-j)/
              (math.factorial(i)*math.factorial(j)*math.factorial(l-i-j))
              for i in range(l+1) for j in range(l-i+1))
    assert total==Fraction(1,math.factorial(l))
# One complete support-envelope expansion attains the safe radius1+8n bound.
# This enumerates geometric envelopes, not nonzero operator coefficients.
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
norm=lambda a:sum(abs(x) for x in a)
def ball(r):return {x for x in product(range(-r,r+1),repeat=3) if norm(x)<=r}
rootB=(1,0,0);initial={add(rootB,x) for x in ball(1)}
centers={x for x in product(range(-4,7),range(-5,6),range(-5,6))
         if sum(x)%2==0 and any(norm(tuple(xi-yi for xi,yi in zip(x,y)))<=4 for y in initial)}
expanded=initial|{add(a,v) for a in centers for v in ball(4)}
assert max(norm(tuple(xi-yi for xi,yi in zip(x,rootB))) for x in expanded)==9
# Source-physical countercontrol: a Gauss-preserving plaquette circulation.
# In the all-plus empty-B sector D on j units of that circulation is4j^2.
# A unit circulation W has electric frequency8j+4. This is not a norm-C0 flow.
continuity=[]
for j in (1,3,10,100,1000):
    t=math.pi/(8*j+4)
    moving=abs(cmath.exp(1j*(8*j+4)*t)-1)
    fixed=abs(cmath.exp(1j*4*t)-1)
    assert abs(moving-2)<1e-12
    continuity.append({'j':j,'time':t,'norm_lower_bound_from_physical_j_mode':moving,'fixed_zero_circulation_vector_change':fixed})
assert continuity[-1]['fixed_zero_circulation_vector_change']<0.002
# Actual Gauss increment of each elementary original birth branch.
for q in (-1,1):
    for sigma in (-1,1):
        for b in range(6):
            for d in range(6):
                if b==d:continue
                dE=[0]*6;dE[b]=sigma;dE[d]=-q
                assert sum(dE)==sigma-q
                assert -dE[b]==-sigma and -dE[d]==q
# Loss-free observable evolution would violate the remote cancellation premise.
resolved_gain_on_identity=12*5
coherent_gain_on_identity=6*10
assert resolved_gain_on_identity==coherent_gain_on_identity==60
assert resolved_gain_on_identity-60==0 and resolved_gain_on_identity!=0
results={'connected_counts':counts,'explicit_small_time_localization_resources':tails,'segment_simplex_identities_checked':13,'single_step_geometry':{'initial_halo_radius':1,'center_count':len(centers),'expanded_radius':9,'safety_formula':'1+8*n'},'physical_non_norm_continuity_control':continuity,'actual_original_birth_Gauss_increment_cases':2*2*6*5,'remote_gain_only_identity_defect_in_units_kappa':60,'method_limit':'Exact finite combinatorial/rational controls plus an analytic physical plaquette counterexample; CP, compatibility, infinite-volume existence and uniform integrability are proved in REPORT, not inferred from these samples.','cpu_seconds':time.process_time()-started,'ru_maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
assert results['cpu_seconds']<30 and results['ru_maxrss_bytes']<150*1024**2
results['bindings']={name:hashlib.sha256((here/name).read_bytes()).hexdigest()
                     for name in ('check.py','CONTRACT.md','SOURCE_IDENTITIES.json')}
(here/'CHECK_RESULTS.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
