#!/usr/bin/env python3
"""Exact connected N4 pair-pulse coefficients, no bosonic replacement.

Price: one local sparse job, <100 MB and <60s anticipated. All matrices
have dimension15; bounded support is derived in REPORT.md.
"""
from pathlib import Path
from itertools import product,combinations,permutations
from collections import defaultdict
from fractions import Fraction as F
from datetime import datetime,timezone
import json,time,resource

OUT=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (runtime/'STOP_REQUESTED.json').exists()
assert datetime.now(timezone.utc).timestamp()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
start=time.monotonic()
zero=(0,0,0)
unit=[tuple(int(i==j) for j in range(3)) for i in range(3)]
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
scale=lambda a,s:tuple(s*x for x in a)
varnames=['u1','u2','v12','v13','v23']
mon=list(combinations(range(5),2))
mon=sorted(mon+[(i,i) for i in range(5)])
mi={x:i for i,x in enumerate(mon)}
Z=(0,)*15
def lin(i):return tuple(int(j==i) for j in range(5))
u=[lin(0),lin(1),(-1,-1,0,0,0)]
v={(0,1):lin(2),(0,2):lin(3),(1,2):lin(4)}
D={}
for i in range(3):
    for s in [-1,1]:D[scale(unit[i],2*s)]=u[i]
for (i,j),w in v.items():
    for s,t in product([-1,1],repeat=2):
        D[add(scale(unit[i],s),scale(unit[j],t))]=tuple(-s*t*a for a in w)
assert len(D)==18
def weight(a,b):return D.get(sub(b,a),(0,)*5)
def mul(a,b):
    z=[0]*15
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:z[mi[tuple(sorted((i,j)))]]+=x*y
    return tuple(z)
def plus(*ps):return tuple(map(sum,zip(*ps))) if ps else Z
def smul(p,c):return tuple(c*x for x in p)
def matchings(S):
    a,b,c,d=S
    return [mul(weight(a,b),weight(c,d)),mul(weight(a,c),weight(b,d)),mul(weight(a,d),weight(b,c))]
def four(S):return plus(*matchings(S))
def matrix():return [[0]*15 for _ in range(15)]
def outer(G,p,q=None,k=1):
    if q is None:q=p
    ip=[(i,x) for i,x in enumerate(p) if x]
    iq=[(i,x) for i,x in enumerate(q) if x]
    for i,x in ip:
        for j,y in iq:G[i][j]+=k*x*y
def matadd(*Gs):return [[sum(G[i][j] for G in Gs) for j in range(15)] for i in range(15)]

types=[]
for i in range(3):types.append((unit[i],scale(unit[i],-1),1))
planes=[]
for i,j in combinations(range(3),2):
    ids=[]
    for s,t in product([-1,1],repeat=2):
        ids.append(len(types));types.append((scale(unit[i],s),scale(unit[j],t),s*t))
    planes.append(ids)
assert len(types)==15

def defects(x,typ):
    aa,bb,sgn=typ;a=add(x,aa);b=add(x,bb)
    candidates=set()
    # Overlap exclusion; include every residual G edge incident to a or b.
    for p in [a,b]:
        for delta in D:candidates.add(tuple(sorted((p,add(p,delta)))))
    # The two crossed perfect matchings are both covered by unordered pairs.
    for da,db in product(D,repeat=2):
        c=add(a,da);d=add(b,db)
        if c!=d:candidates.add(tuple(sorted((c,d))))
    ans={}
    for c,d in candidates:
        if a in (c,d) or b in (c,d):z=smul(mul(weight(a,b),weight(c,d)),-sgn)
        else:z=smul(plus(mul(weight(a,c),weight(b,d)),mul(weight(a,d),weight(b,c))),sgn)
        if any(z):ans[(c,d)]=z
    return ans

d0=[defects(zero,t) for t in types]
G_AE=matrix();G_AT=matrix();G_D=matrix();G_W=matrix()
keys=set().union(*(set(d) for d in d0))
for r in keys:
    ps=[d.get(r,Z) for d in d0]
    outer(G_AE,plus(*ps[:3]),k=8) # 12*(2/3)
    for ids in planes:
        for i,j in combinations(ids,2):outer(G_AT,plus(ps[i],smul(ps[j],-1)),k=3)
for k in range(3):
    d1=[defects(unit[k],t) for t in types]
    keys1=keys|set().union(*(set(d) for d in d1))
    for r in keys1:
        ps=[plus(d1[i].get(r,Z),smul(d0[i].get(r,Z),-1)) for i in range(15)]
        for p in ps[:3]:outer(G_W,p,k=12)
        outer(G_W,plus(*ps[:3]),k=-4)
        for ids in planes:outer(G_W,plus(*(ps[i] for i in ids)),k=3)
for trio in combinations(D,3):outer(G_D,four((zero,)+trio),k=12)
G_mu=matadd(G_AE,G_AT,G_D)

# Adjacent-center defects have residual pairs of opposite lattice parity.
G_W_local=matrix()
for r in keys:
    ps=[d.get(r,Z) for d in d0]
    for p in ps[:3]:outer(G_W_local,p,k=72)
    outer(G_W_local,plus(*ps[:3]),k=-24)
    for ids in planes:outer(G_W_local,plus(*(ps[i] for i in ids)),k=18)
assert G_W_local==G_W

# Number t^4 coefficient = (||C²Omega||²-2||COmega||^4)/(3V).
# Construct its connected numerator K using exclusion stars and 4-cycles.
G_K=matrix()
for delta in D:outer(G_K,mul(D[delta],D[delta]),k=-1) # -2 per undirected edge
for d,e in combinations(D,2):outer(G_K,mul(D[d],D[e]),k=-4)
cycle_sets=set()
for a,c in combinations(D,2):
    for da in D:
        b=add(a,da)
        if b==zero or b in (a,c):continue
        if weight(c,b)!=(0,)*5:cycle_sets.add(tuple(sorted((zero,a,b,c))))
for S in cycle_sets:
    ps=matchings(S)
    for i,j in combinations(range(3),2):
        outer(G_K,ps[i],ps[j]);outer(G_K,ps[j],ps[i])

def evalm(G,z,den=1):
    ms=[z[i]*z[j] for i,j in mon]
    return sum(ms[i].conjugate()*G[i][j]*ms[j] for i in range(15) for j in range(15))/den
def norm(z):return abs(z[0])**2+abs(z[1])**2+abs(z[0]+z[1])**2+2*sum(abs(x)**2 for x in z[2:])
directions={
 'E_real_biaxial':[1,-1,0,0,0],
 'E_real_uniaxial':[1,1,0,0,0],
 'E_complex':[1,1j,0,0,0],
 'T_one':[0,0,1,0,0],
 'T_two_real':[0,0,1,1,0],
 'T_two_phase':[0,0,1,1j,0],
 'T_three_real':[0,0,1,1,1],
 'T_three_phase':[0,0,1,1j,1],
 'mixed_real':[1,-1,1,0,0],
 'mixed_phase':[1,-1,1j,0,0],
}
tests={}
for name,z in directions.items():
    z=list(map(complex,z));s=norm(z)
    tests[name]={'pair_norm_per_site':s,'energy_mu':evalm(G_mu,z,12).real,'energy_tau':evalm(G_W,z,12).real,'number_quartic':evalm(G_K,z,3).real,'normalized_energy_mu':evalm(G_mu,z,12).real/s**2,'normalized_energy_tau':evalm(G_W,z,12).real/s**2}

# Exact covariance under proper signed coordinate permutations, all evaluated
# coefficientwise by substitution on five-variable quadratic monomials.
def parity(p):return -1 if sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2 else 1
def transformed(p,sgn):
    outu=[None]*3;outv={}
    for i in range(3):outu[p[i]]=u[i]
    for (i,j),w in v.items():outv[tuple(sorted((p[i],p[j])))]=tuple(sgn[i]*sgn[j]*x for x in w)
    return [outu[0],outu[1],outv[(0,1)],outv[(0,2)],outv[(1,2)]]
def substitute(G,trans):
    rows=[mul(trans[i],trans[j]) for i,j in mon];out=matrix()
    for i in range(15):
        for j in range(15):
            if G[i][j]:outer(out,rows[i],rows[j],G[i][j])
    return out
rotations=0
for p in permutations(range(3)):
    for sgn in product([-1,1],repeat=3):
        if parity(p)*sgn[0]*sgn[1]*sgn[2]!=1:continue
        tr=transformed(p,sgn)
        for G in [G_mu,G_W,G_K]:assert substitute(G,tr)==G
        rotations+=1
assert rotations==24
for G in [G_mu,G_W,G_K]:assert all(G[i][j]==G[j][i] for i in range(15) for j in range(15))

payload={'coordinates':varnames,'u3':'-u1-u2','monomial_order':[[varnames[i],varnames[j]] for i,j in mon],
 'energy_denominator':12,'energy_mu_matrix_numerator':G_mu,'energy_tau_matrix_numerator':G_W,
 'energy_parts_numerator':{'A_E':G_AE,'A_T':G_AT,'D':G_D},
 'number_quartic_denominator':3,'number_quartic_matrix_numerator':G_K,
 'defect_residual_pair_count':len(keys),'local_defect_counts':[len(d) for d in d0],
 'degree3_stars':816,'rooted_cycle_vertex_sets':len(cycle_sets),'proper_cubic_coefficient_checks':rotations,
 'opposite_parity_defect_identity':True,
 'directions':tests,'elapsed_s':time.monotonic()-start,'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(OUT/'quartic.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps({k:v for k,v in payload.items() if 'matrix' not in k and k!='energy_parts_numerator'},indent=2))
