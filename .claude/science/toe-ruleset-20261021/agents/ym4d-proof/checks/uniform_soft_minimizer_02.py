#!/usr/bin/env python3
"""Exact plaquette boundary certificates; separate from the sparse minimizer code."""
from collections import Counter
from itertools import permutations,product
from pathlib import Path
import json, math, time

L=3; D=4; checks=[];details={};start=time.time()
def check(name,ok,**kw):checks.append(dict(name=name,passed=bool(ok),**kw))
def clean(c):return {k:v for k,v in c.items() if v}
def combine(a,b,scale=1):
    out=Counter(a)
    for key,val in b.items():out[key]+=scale*val
    return out
def endpoint_word(y,order):
    return [(mu,1 if y[mu]>0 else -1) for mu in order for _ in range(abs(y[mu]))]
def edge_chain(word):
    x=[0]*D;out=Counter()
    for mu,sgn in word:
        if sgn<0:x[mu]-=1
        out[(tuple(x),mu)]+=sgn
        if sgn>0:x[mu]+=1
    return out

def filling(word):
    word=list(word);surf=Counter()
    for end in range(len(word)-1,0,-1):
        for i in range(end):
            a,sa=word[i];b,sb=word[i+1]
            if a<=b:continue
            x=[0]*D
            for mu,s in word[:i]:x[mu]+=s
            if sa<0:x[a]-=1
            if sb<0:x[b]-=1
            surf[(tuple(x),b,a)]+=-sa*sb
            word[i],word[i+1]=word[i+1],word[i]
    return surf

def boundary(surf):
    out=Counter()
    for (x,mu,nu),coef in surf.items():
        xm=list(x);xm[mu]+=1;xn=list(x);xn[nu]+=1
        for key,s in [((x,mu),1),((tuple(xm),nu),1),((tuple(xn),mu),-1),((x,nu),-1)]:out[key]+=coef*s
    return out

for mu in range(D):
    surfaces=[];chains=[];sum_s=Counter();sum_c=Counter();maxarea=0;maxradius=0;mutation_done=False
    straight=edge_chain([(mu,1)]*L)
    for y in product(range(-L//2+1,L//2+1),repeat=D):
        for order in permutations(range(D)):
            leg=endpoint_word(y,order)
            word=leg+[(mu,1)]*L+[(nu,-s) for nu,s in reversed(leg)]
            chain=edge_chain(word);surface=filling(word)
            assert clean(boundary(surface))==clean(combine(chain,straight,-1))
            area=sum(abs(v) for v in surface.values());maxarea=max(maxarea,area)
            maxradius=max(maxradius,max((max(abs(z) for z in x) for (x,a,b),v in surface.items() if v),default=0))
            if area and not mutation_done:
                bad=Counter(surface);key=next(k for k,v in bad.items() if v);bad[key]=0
                check(f'deleted_plaquette_rejected_mu{mu}',clean(boundary(bad))!=clean(combine(chain,straight,-1)));mutation_done=True
            surfaces.append(surface);chains.append(chain);sum_s=combine(sum_s,surface);sum_c=combine(sum_c,chain)
    count=len(surfaces);maxspread=0
    for surface,chain in zip(surfaces,chains):
        spread=Counter({k:count*v for k,v in surface.items()});spread=combine(spread,sum_s,-1)
        rhs=Counter({k:count*v for k,v in chain.items()});rhs=combine(rhs,sum_c,-1)
        assert clean(boundary(spread))==clean(rhs)
        maxspread=max(maxspread,sum(abs(v) for v in spread.values())/count)
    check(f'all_boundaries_mu{mu}',count==24*L**4,individual_count=count,spread_count=count)
    check(f'area_bounds_mu{mu}',maxarea<=25*L**2 and maxspread<=50*L**2,individual_max=maxarea,spread_max=maxspread)
    details[f'orientation_{mu}']=dict(contours=count,max_surface_l1=maxarea,max_spread_l1=maxspread,max_coordinate_radius=maxradius)

base=Path(__file__).resolve().parent
prior=json.loads((base/'uniform_soft_minimizer_01_periodic_out.json').read_text())
row=next(c for c in prior['checks'] if c['name']=='curvature_column_cell_count')
wrong=row['count_bound']/L**4
check('actual_missing_density_bound_rejected',row['column_max']>wrong*(1+1e-10),actual_column=row['column_max'],mutated_bound=wrong)
for a in [.001,.03,.4,2.]:
    c=1/math.tanh(a/2)
    for r in [1,3,9,81,59049]:
        finer=1/math.tanh(a/(2*r))
        check(f'coth_density_a{a}_r{r}',finer<=r*c*(1+1e-14),ratio=finer/(r*c))
    for t in [.0,.1,.3,.5,.9]:
        shifted=(math.exp(-a*t)+math.exp(-a*(1-t)))/(-math.expm1(-a))
        check(f'shifted_row_a{a}_t{t}',shifted<=c*(1+1e-14),ratio=shifted/c)
out=dict(scope='Exact d=4 L=3 path fillings and disclosed post-run density mutation; finite support for the general proof',checks=checks,passed=sum(c['passed'] for c in checks),total=len(checks),details=details,elapsed_seconds=time.time()-start)
print(json.dumps(out,indent=2));raise SystemExit(0 if all(c['passed'] for c in checks) else 1)
