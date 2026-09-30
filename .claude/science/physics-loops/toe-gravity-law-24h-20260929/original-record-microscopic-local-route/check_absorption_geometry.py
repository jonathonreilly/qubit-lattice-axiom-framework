"""Exact cubic geometry controls for the source-specific one-hole estimate."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
from itertools import product,combinations
from collections import Counter
from fractions import Fraction
import hashlib,json,math,resource,time
t0=time.process_time();here=Path(__file__).resolve().parent
origin=(0,0,0);axes=((1,0,0),(0,1,0),(0,0,1))
dirs=axes+tuple(tuple(-x for x in v) for v in axes)
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
def star(a,L=None):
    result={add(a,d) for d in dirs}
    return result if L is None else {tuple(x%L for x in b) for b in result}
geometry=[]
for L in (6,8,10,None):
    centers=(v for v in product(range(L),repeat=3) if sum(v)%2==0) if L else (v for v in product(range(-4,5),repeat=3) if sum(v)%2==0)
    base=star(origin,L);intersections=Counter()
    for c in centers:
        if c==origin:continue
        overlap=len(base&star(c,L));intersections[overlap]+=1
        assert overlap<=2 and len(base|star(c,L))>=10
    axial=[tuple(2*x for x in d) for d in dirs]
    if L:axial=[tuple(x%L for x in c) for c in axial]
    assert len(set(axial))==6
    assert all(len(base&star(c,L))==1 for c in axial)
    geometry.append({'period':L,'other_center_intersection_counts':dict(sorted(intersections.items())),'axial_centers':axial})
base=star(origin);axial=[tuple(2*x for x in d) for d in dirs]
relevant=set().union(*(star(c) for c in axial))|base
extras=sorted(relevant-base)
# Only the six axial stars matter for this row bound; B outside relevant cannot
# raise their occupation. There are30 possible extras in this smaller union.
hist=Counter();masks=0;rows=0
for n in range(4):
    for selected in combinations(extras,n):
        mask=base|set(selected);masks+=1
        for c in axial:
            occupied=len(mask&star(c));rows+=1
            assert occupied<=1+n<=4
            hist[(6+n,occupied)]+=1
diag=(1,1,0);two_dark=base|star(diag)
assert len(base&star(diag))==2 and len(two_dark)==10
assert base<=two_dark and star(diag)<=two_dark
M=12+18*12+2*18*24
assert M==1092
c0=Fraction(2,M*M+1)
# Exact Gram determinant/trace bound for tau<=1 is analytic. Check its worst
# endpoint tau=1 and a nontrivial rational interior point with exact fractions.
for tau in (Fraction(1),Fraction(1,7)):
    determinant=tau**4/12;trace=tau+tau**3/3
    assert determinant/trace>=tau**3/16
delta=kappa=1.0;c_delta=float(c0)
R0=delta**2*math.sqrt(12)*M*M/2
tau=min(1,math.sqrt(5*c_delta)/(8*R0))
cU=c_delta*tau**3/64;a0=min(.5,kappa*cU/(1+6*kappa*tau)**2)
C0=math.exp(a0/2);gamma=a0/(2*tau)
alpha=.5*math.log1p(gamma/(10*C0*delta*M))
result={'geometry':geometry,'selected_axial_row_local_masks':{'relevant_extra_B_sites':len(extras),'masks':masks,'rows':rows,'occupied_neighbor_histogram':{str(k):v for k,v in sorted(hist.items())},'minimum_bright_G':4},'scope_control':{'ten_occupied_B_mask':sorted(two_dark),'distinct_dark_centers':[origin,diag],'interpretation':'The unique-dark-star proof no longer applies at k=10; this is not a counterexample to every possible higher-sector absorption bound.'},'analytic_constants':{'M':M,'c0_exact':str(c0),'delta':delta,'kappa':kappa,'illustrative_float_tau':tau,'illustrative_float_gamma':gamma,'illustrative_float_alpha':alpha},'cpu_seconds':time.process_time()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact geometry corroboration only. Charge/field injectivity, operator observability, semigroup decay and weighted-domain arguments are proved in FAST_ONE_HOLE_ABSORPTION.md, not inferred from these finite enumerations.'}
assert result['cpu_seconds']<5 and result['peak_rss_bytes']<80*1024**2
(here/'ABSORPTION_GEOMETRY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'masks':masks,'rows':rows,'extra_sites':len(extras),'cpu_seconds':result['cpu_seconds'],'peak_rss_bytes':result['peak_rss_bytes'],'tau':tau,'gamma':gamma},indent=2))
