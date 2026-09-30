"""Independent sparse geometry and exact arithmetic controls; no author report/code.
Price: 30 CPU seconds,150MB; one process, BLAS/OMP1. No Hilbert enumeration.
"""
from pathlib import Path
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import hashlib,json,math,resource,time
from fractions import Fraction
from itertools import product
started=time.process_time()
root=Path(__file__).resolve().parent
zero=(0,0,0)
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
norm=lambda a:sum(abs(x) for x in a)
def ball(r):return {x for x in product(range(-r,r+1),repeat=3) if norm(x)<=r}
steps=ball(1)-{zero}
partners={x for x in ball(2) if norm(x)==2}
star=lambda a:{a}|{add(a,s) for s in steps}
active={zero}|partners
pairs={tuple(sorted((a,add(a,d)))) for a in active for d in partners}
assert len(steps)==6 and len(partners)==18 and len(active)==19 and len(pairs)==264
assert all(star(a)|star(c) <= ball(5) for a,c in pairs)
full_support=star(zero).copy()
for a,c in pairs:full_support.update(star(a)|star(c))
assert max(map(norm,full_support))==5
halo=full_support|{add(x,s) for x in full_support for s in steps}
assert max(map(norm,halo))==6 and halo <= ball(6)
assert len(ball(4))==129 and len(ball(6))==377
edges={(add(b,s),b) for b in steps for s in steps}
assert len(edges)==36
# Half-pair center support and commuting-electric one-step enlargement.
center_support=set().union(*(star(zero)|star(c) for c in partners))
center_halo=center_support|{add(x,s) for x in center_support for s in steps}
assert max(map(norm,center_support))==3 and max(map(norm,center_halo))==4
# Exact Schur/current constants, for all actual later local B occupations.
incidence=[2*(5-o)*(6-o)*(o+1) for o in range(6)]
assert incidence==[60,80,72,48,20,0]
assert 2*80*36==5760 and 2*80*264*288==12165120
# Connected sequence product and analytic majorant coefficient controls.
rows=[]
for n in range(1,33):
    count=math.prod(129*(377+129*j) for j in range(n))
    upper=16641**n*math.factorial(n+2)//2
    assert count<=upper
    coefficient=Fraction(n*n*(n+1)*(n+2),2)
    # [z^n] 3z(1+3z)/(1-z)^5, with absent negative index interpreted zero.
    rational=3*math.comb(n+3,4)+(9*math.comb(n+2,4) if n>=2 else 0)
    assert coefficient==rational
    rows.append({'n':n,'connected_count_bound_valid':True,'series_coefficient':int(coefficient)})
K=delta=kappa=Fraction(1)
lambda_local=5184*delta+160*kappa
a=16641*lambda_local
C=241920*kappa*K+12165120*kappa*delta
p0=123744*kappa*delta
T=min(Fraction(1,2*a),p0/(480*C*a))
assert a*T<=Fraction(1,2) and 240*C*a*T<=p0/2
# Controls must detect undercounted support, missing loss and missing polynomial weight.
controls={
    'radius5_current_interaction_picture_is_insufficient':not halo<=ball(5),
    'radius3_generator_interaction_picture_is_insufficient':not center_halo<=ball(3),
    'active_pairs_are_not_only_internal19_choose2':len(pairs)>len(active)*(len(active)-1)//2,
    'loss_doubles_safe_CP_current_allowance':2*80*36!=80*36,
    'quadratic_field_weight_is_not_constant':(4*2+2)*(4*2+3)>(4*1+2)*(4*1+3),
}
assert all(controls.values())
result={'source':'actual cubic geometry and exact integer/rational calculations; no root implementation imported','geometry':{'active_A_centers':len(active),'magnetic_pairs':len(pairs),'electric_edges':len(edges),'current_support_radius':5,'current_D_conjugated_radius':6,'generator_support_radius':3,'generator_D_conjugated_radius':4,'ball4_sites':len(ball(4)),'ball6_sites':len(ball(6)),'actual_current_halo_sites':len(halo)},'later_sector_Gamma_coefficients':incidence,'unit_parameters':{'lambda':str(lambda_local),'a':str(a),'C_star':str(C),'p0':str(p0),'c':str(p0/2),'t0_exact':str(T),'t0_float':float(T)},'coefficient_checks':rows,'controls':controls,'cpu_seconds':time.process_time()-started,'ru_maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
assert result['cpu_seconds']<30 and result['ru_maxrss_bytes']<150*1024**2
(root/'CHECK_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='coefficient_checks'},indent=2))
