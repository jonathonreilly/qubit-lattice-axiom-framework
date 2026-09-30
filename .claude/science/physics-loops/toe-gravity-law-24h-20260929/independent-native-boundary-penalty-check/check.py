#!/usr/bin/env python3
"""Independent literal rows and occupation counts; no author imports."""
from pathlib import Path
import itertools as it, json, time, resource, signal, os, hashlib
from fractions import Fraction
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
resource.setrlimit(resource.RLIMIT_CPU,(30,31)); signal.alarm(90)
t0=time.monotonic(); c0=time.process_time()
def guard():
    assert not (runtime/'STOP_REQUESTED.json').exists()
    assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
    assert time.monotonic()-t0<90
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=150*1024**2
assert all(os.environ.get(k)=='1' for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'))
guard()
e=[tuple(int(j==i) for j in range(3)) for i in range(3)]
add=lambda x,y:tuple(a+b for a,b in zip(x,y))
mul=lambda s,x:tuple(s*a for a in x)
sub=lambda x,y:add(x,mul(-1,y))
planes=list(it.combinations(range(3),2))
directions=[mul(2,u) for u in e]+[add(e[i],mul(s,e[j])) for i,j in planes for s in (1,-1)]
graph=directions+[mul(-1,d) for d in directions]
edge=lambda x,y:tuple(sorted((x,y)))
def anchor(pair):
    x,y=pair; d=sub(y,x)
    if d in directions:return directions.index(d),x
    return directions.index(mul(-1,d)),y

def rank_mod(rows,n=9,p=101):
    a=[[x%p for x in row] for row in rows]; r=0
    for j in range(n):
        i=next((i for i in range(r,len(a)) if a[i][j]),None)
        if i is None:continue
        a[i],a[r]=a[r],a[i]; z=pow(a[r][j],-1,p); a[r]=[(x*z)%p for x in a[r]]
        for k in range(r+1,len(a)):
            z=a[k][j]
            if z:a[k]=[(x-z*y)%p for x,y in zip(a[k],a[r])]
        r+=1
    return r

def canonical(row):
    out=tuple(sorted((p,c) for p,c in row.items() if c))
    if out and out[0][1]<0:out=tuple((p,-c) for p,c in out)
    return out

boxes=[]
for lengths in ((3,3,3),(4,5,6),(5,5,5)):
    sites=set(it.product(*(range(v) for v in lengths)))
    edges={edge(x,add(x,d)) for x in sites for d in directions if add(x,d) in sites}
    S=[]; old_family_rows=0
    for x in sites:
        pairs=[edge(add(x,u),sub(x,u)) for u in e]
        if all(all(y in sites for y in p) for p in pairs):
            S.append((dict.fromkeys(pairs,1),Fraction(2,3))); old_family_rows+=1
        for i,j in planes:
            words=[(edge(add(x,mul(s,e[i])),add(x,mul(t,e[j]))),s*t) for s,t in it.product((-1,1),repeat=2)]
            full=all(all(y in sites for y in p) for p,c in words)
            if full:old_family_rows+=6
            for (p,c),(q,d) in it.combinations(words,2):
                if all(y in sites for z in (p,q) for y in z):S.append(({p:c,q:-d},Fraction(1,4)))
    constants=[]; incidence={p:Fraction(0) for p in edges}
    for row,w in S:
        z=[0]*9
        for p,c in row.items():z[anchor(p)[0]]+=c
        constants.append(z)
        size=w*sum(c*c for c in row.values())
        for p in row:incidence[p]+=size
    # All actual S rows annihilate the supplied five raw soft directions.
    soft=[[1,-1,0,0,0,0,0,0,0],[1,1,-2,0,0,0,0,0,0]]
    for j in (3,5,7):
        v=[0]*9;v[j]=-1;v[j+1]=1;soft.append(v)
    assert all(sum(a*b for a,b in zip(row,v))==0 for row in constants for v in soft)
    distinct=list({tuple(row) for row in constants});assert rank_mod(distinct)==4
    pin_hist={}
    for y in sites:
        pins={anchor(p)[0] for p in edges if y in p}
        pinrows=[[int(j==i) for j in range(9)] for i in pins]
        rk=rank_mod(distinct+pinrows);pin_hist[rk]=pin_hist.get(rk,0)+1
        if min(lengths)>=4:assert rk==9
    if lengths==(3,3,3):assert pin_hist.get(7,0)==1
    # Independent physical-row enumeration of all 15 and nine gradients.
    grad15={};grad9={}
    def count(target,p,q):
        if p in edges and q in edges:
            key=tuple(sorted((p,q)));target[key]=target.get(key,0)+1
    for x in sites:
        words=[(mul(-1,u),u) for u in e]+[(mul(s,e[i]),mul(t,e[j])) for i,j in planes for s,t in it.product((-1,1),repeat=2)]
        for u,v in words:
            p=edge(add(x,u),add(x,v))
            for step in e:count(grad15,p,edge(add(add(x,u),step),add(add(x,v),step)))
        for d in directions:
            p=edge(x,add(x,d))
            for step in e:count(grad9,p,edge(add(x,step),add(add(x,d),step)))
    assert grad9.keys()==grad15.keys()
    for key,v in grad9.items():
        assert v==1
        typ=anchor(key[0])[0];assert grad15[key]==(1 if typ<3 else 2)
        for p in key:incidence[p]+=2
    maxinc=max(incidence.values());assert maxinc<=15
    boxes.append({'lengths':lengths,'sites':len(sites),'edges':len(edges),'all_complete_individual_S_rows':len(S),'complete_four_word_family_subset_rows':old_family_rows,'pin_rank_histogram':pin_hist,'gradient9_rows':len(grad9),'gradient15_rows_with_multiplicity':sum(grad15.values()),'max_weighted_J_incidence':str(maxinc)})
    guard()

# Full diagonal inequality, not an amplitude-fiber replacement.
L=24
points=[(0,0,0),(0,5,0),(5,5,5),(7,5,5),(5,7,5),(5,5,7),(14,14,14),(16,14,14),(22,20,20),(20,20,20),(10,0,10),(10,2,10)]
inside=lambda x:all(0<=v<L for v in x)
q=[sum(not inside(add(x,d)) for d in graph) for x in points]
nb=[sum(1<<j for j,y in enumerate(points) if sub(y,x) in graph) for x in points]
physedges=[(i,j) for i in range(len(points)) for j in range(i+1,len(points)) if nb[i]>>j&1]
phi=lambda m:(m-1)*(m-2)//2
state_counts=[]
for R in (4,7):
    close={}
    for i,j in physedges:
        close[i,j]=sum(1<<k for k,z in enumerate(points) if k not in (i,j) and min(max(abs(a-b) for a,b in zip(z,points[t])) for t in (i,j))<=R)
    active_boundary=active_near=active_diag=0
    for mask in range(1<<len(points)):
        isolated=near=0
        for i,j in physedges:
            if mask>>i&1 and mask>>j&1:
                if mask&close[i,j]:near+=1
                else:isolated+=1
        bad=mask.bit_count()-2*isolated
        diagonal=sum(min(phi((mask&nb[i]).bit_count()+j) for j in range(q[i]+1)) for i in range(len(points)) if mask>>i&1)
        boundary=sum(q[i]>0 for i in range(len(points)) if mask>>i&1)
        assert bad<=diagonal+boundary+2*near
        active_boundary+=bad>diagonal+2*near
        active_near+=bad>diagonal+boundary
        active_diag+=bad>boundary+2*near
    state_counts.append({'R':R,'occupations':1<<len(points),'boundary_term_necessary_cases':active_boundary,'near_edge_term_necessary_cases':active_near,'diagonal_term_necessary_cases':active_diag})
    assert active_boundary and active_near and active_diag
    guard()

safe_cases=0
for q0 in range(19):
    for m in range(19-q0):
        safe=min(phi(m+j) for j in range(q0+1))
        assert safe==(0 if q0>0 and m<=2 else phi(m))
        for j in range(q0+1):assert 0<=safe<=phi(m+j);safe_cases+=1
boundaries=[]
for ell in (4,5,8):
    sites=set(it.product(range(ell),repeat=3))
    boundary=sum(any(add(x,d) not in sites for d in graph) for x in sites)
    assert boundary==ell**3-(ell-4)**3
    assert Fraction(boundary,ell**3)<=Fraction(12,ell)
    counts=[sum(add(x,d) in sites for x in sites) for d in directions]
    assert counts==[(ell-2)*ell**2]*3+[(ell-1)**2*ell]*6
    boundaries.append({'ell':ell,'boundary_sites':boundary,'axial_mode_norm_squared':counts[0],'triplet_mode_norm_squared':counts[3]})
guard()
result={'scope':'Independent exact finite physical rows and diagonal count checks after author proof/control read; no author imports, spectrum or C_pin computation. Modular full rank is an exact rational lower-rank witness; the five displayed rational soft vectors supply the matching nullspace. The side3 counterfixture is outside the theorem and deliberately retained.','boxes':boxes,'occupation_count_cases':state_counts,'safe_diagonal_cases':safe_cases,'boundary_and_soft_gram':boundaries,'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
