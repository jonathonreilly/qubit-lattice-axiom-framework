#!/usr/bin/env python3
"""Exact controls for one supplied full-qubit four-particle theorem.

Integrated AUTHOR reuse of frozen physical word, SOS-source and torus-control
implementations, with provenance in the unit pack. No author module is imported
from the campaign. Infinite-volume and convergence results are analytic proofs;
this runner does not numerically evaluate T0 or a thermodynamic limit.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import argparse
import json
import resource
import time
from pathlib import Path
from itertools import product, combinations
from collections import defaultdict, Counter
from fractions import Fraction
import numpy as np
from native_four_particle_normalization_2026_09_30 import run as normalization_control

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    'docs/NATIVE_FOUR_PARTICLE_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-30.md',
    'docs/NATIVE_FOUR_PARTICLE_PERIODIC_BAND_PROOF_2026-09-30.md',
    'docs/NATIVE_FOUR_PARTICLE_THRESHOLD_LIMIT_PROOF_2026-09-30.md',
    'docs/NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md',
    'scripts/native_four_particle_normalization_2026_09_30.py',
    'outputs/native_four_particle_threshold_2026_09_30/compact_trial.json',
)
ROOT=Path(__file__).resolve().parents[1]

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

neighbors=[scale(v,s) for v in unit for s in (-1,1)]
def canonical(S):
 a=min(S)
 return tuple(sorted(sub(x,a) for x in S))

def matching_edges(S):
 a,b,c,d=S
 return [((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))]

def perfect(S):
 return any(sub(b,a) in D and sub(d,c) in D for (a,b),(c,d) in matching_edges(S))

def degrees(S):
 return [sum(sub(y,x) in D for y in S if y!=x) for x in S]

def action12(S):
 """Return coefficients of mu and tau in 12 H|S>, literal sites."""
 out=defaultdict(lambda:[0,0]);S=tuple(S);deg=degrees(S)
 out[S][0]+=12*(len(S)+sum(d*(d-1)//2 for d in deg))
 for a,b in combinations(S,2):
  rem=set(S)-{a,b}
  centers=set(add(a,v) for v in neighbors)&set(add(b,v) for v in neighbors)
  for x in centers:
   da,db=sub(a,x),sub(b,x)
   ia=next(i for i in range(3) if da[i]);ib=next(i for i in range(3) if db[i])
   for shift in [(0,0,0)]+neighbors:
    y=add(x,shift);onsite=shift==(0,0,0)
    candidates=[]
    if ia==ib:
     assert da==scale(db,-1)
     for j in range(3):
      candidates.append((add(y,unit[j]),sub(y,unit[j]),12*(int(ia==j))-4,-2))
    else:
     sg=da[ia]*db[ib]
     for sa,sb in product((-1,1),repeat=2):
      candidates.append((add(y,scale(unit[ia],sa)),add(y,scale(unit[ib],sb)),3*sg*sa*sb,-1))
    for c,d,coef,attract in candidates:
     if c in rem or d in rem:continue
     target=tuple(sorted(rem|{c,d}));assert len(target)==len(S)
     out[target][0]+=coef*attract if onsite else 0
     out[target][1]+=coef*(6 if onsite else -1)
 return {k:tuple(v) for k,v in out.items() if any(v)}


def small_geometry():
    """Finite graph and literal physical-action controls, exact rational values."""
    edges=list(combinations(range(4),2)); nonmatching=0
    for mask in range(64):
        es={edges[i] for i in range(6) if mask>>i&1}
        pm=any(set(tuple(sorted(z)) for z in m)<=es for m in
               [((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))])
        deg=[sum(i in edge for edge in es) for i in range(4)]
        diagonal=sum((d-1)*(d-2)//2 for d in deg)
        assert diagonal>=0
        if not pm:
            assert diagonal>=1
            nonmatching+=1
    assert nonmatching==27
    S=tuple((j,0,0) for j in (0,2,4,6))
    target=tuple(sorted([(0,0,0),(3,-1,1),(3,1,1),(6,0,0)]))
    row=action12(S)
    assert row[target]==action12(target)[S]==(0,4)
    assert not perfect(target)
    for target2 in list(row)[:20]:
        assert action12(target2).get(S,(0,0))==row[target2]
    # Exact adjoint lift: every matching orbit is counted by 2m actual coordinates.
    shapes={((0,0,0),)}; counts=[]
    for count in range(2,5):
        shapes={canonical(S+(add(x,d),)) for S in shapes for x in S for d in D if add(x,d) not in S}
        counts.append(len(shapes))
    assert counts==[9,113,1647]
    for S in shapes:
        pm=[m for m in matching_edges(S) if all(sub(y,x) in D for x,y in m)]
        ordered=[]
        for match in pm:
            for removed,residual in [match,match[::-1]]:
                def forward(edge):
                    x,y=sorted(edge)
                    return x,sub(y,x)
                anchor,e=forward(residual); x,d=forward(removed)
                ordered.append((d,e,sub(x,anchor)))
        assert len(set(ordered))==2*len(pm)
        if pm:
            assert sum((Fraction(1,2*len(pm)) for _ in ordered),Fraction())==1
    core=sorted(S for S in shapes if perfect(S))
    assert len(core)==1487
    return core,{'abstract_graphs':64,'nonmatching_graphs':nonmatching,
                 'connected_counts':counts,'matching_core':len(core),
                 'ordered_adjoint_lifts_checked':len(shapes),'literal_hermiticity_checks':20}


def bare_and_source():
    """Two finite-support expressions: positive-row energy and adjoint row source."""
    d0=[defects(zero,t) for t in types]
    dnear=[[defects(e,t) for t in types] for e in neighbors]
    basekeys=set().union(*(set(d) for d in d0))
    BM=matrix(); BT=matrix()
    for r in basekeys:
        ps=[d.get(r,Z) for d in d0]
        outer(BM,plus(*ps[:3]),k=8)
        for ids in planes:
            for i,j in combinations(ids,2):
                outer(BM,plus(ps[i],smul(ps[j],-1)),k=3)
    for j in range(3):
        dn=dnear[2*j+1]  # neighbors ordered (-unit,+unit)
        for r in basekeys|set().union(*(set(d) for d in dn)):
            ps=[plus(dn[i].get(r,Z),smul(d0[i].get(r,Z),-1)) for i in range(15)]
            for p in ps[:3]:outer(BT,p,k=12)
            outer(BT,plus(*ps[:3]),k=-4)
            for ids in planes:outer(BT,plus(*(ps[i] for i in ids)),k=3)
    FM=defaultdict(lambda:np.zeros(15,dtype=np.int64))
    FT=defaultdict(lambda:np.zeros(15,dtype=np.int64))
    keys=basekeys|set().union(*(set(d) for ds in dnear for d in ds))
    for r in keys:
        ps=np.array([d.get(r,Z) for d in d0],dtype=np.int64)
        lap=6*ps-sum((np.array([d.get(r,Z) for d in ds],dtype=np.int64) for ds in dnear),np.zeros((15,15),dtype=np.int64))
        cm=np.zeros((15,15),dtype=np.int64);ct=cm.copy()
        cm[:3]=8*sum(ps[:3]);ct[:3]=12*lap[:3]-4*sum(lap[:3])
        for ids in planes:
            cm[ids]=3*(4*ps[ids]-sum(ps[ids]));ct[ids]=3*sum(lap[ids])
        for i,(a,b,sg) in enumerate(types):
            if a in r or b in r:continue
            S=canonical((a,b)+r)
            FM[S]+=sg*cm[i]; FT[S]+=sg*ct[i]
    # On matching incoming states the diagonal defect is exactly the degree-three
    # star count: lower-degree isolated contributions have zero incoming amplitude.
    for trio in combinations(D,3):
        S=(zero,)+trio; p=four(S)
        outer(BM,p,k=12)
        FM[canonical(S)]+=12*np.array(p,dtype=np.int64)
    zero15=np.zeros(15,dtype=np.int64)
    keys=sorted(S for S in set(FM)|set(FT) if np.any(FM.get(S,zero15)) or np.any(FT.get(S,zero15)))
    mu=np.array([FM.get(S,zero15) for S in keys]); tau=np.array([FT.get(S,zero15) for S in keys])
    phi=np.array([four(S) for S in keys],dtype=np.int64)
    assert np.array_equal(phi.T@mu,BM)
    assert np.array_equal(phi.T@tau,BT)
    assert len(keys)==29907
    assert sum(perfect(S) for S in keys)==4262
    return keys,mu+tau,np.array(BM,dtype=np.int64)+np.array(BT,dtype=np.int64)


def exact_trial(core,keys,source,B):
    data=json.loads((ROOT/AUDIT_INPUT_PATHS[-1]).read_text())
    assert data['schema']=='native-compact-rational-trial-v1'
    supplied=[tuple(map(tuple,S)) for S in data['core']]
    assert supplied==core
    Xi=np.array(data['numerator'],dtype=np.int64); den=data['denominator']
    assert Xi.shape==(1487,15) and den==65536
    index={S:i for i,S in enumerate(core)}
    fd={S:v for S,v in zip(keys,source)}
    zero15=np.zeros(15,dtype=np.int64)
    FC=np.array([fd.get(S,zero15) for S in core],dtype=np.int64)
    R={S:den*v for S,v in zip(keys,source)}
    AX=np.zeros_like(Xi); core_rows={}; actions=0
    maxx=int(np.max(abs(Xi)))
    # A deliberately loose bound from six removed pairs, two centers, seven
    # shifts, four outputs and coefficients at most72, plus the diagonal.
    row_l1_bound=200000
    assert len(core)*row_l1_bound*maxx+den*int(np.max(abs(source)))<2**60
    for i,S in enumerate(core):
        row=defaultdict(int)
        for target,(mu,tau) in action12(S).items():row[canonical(target)]+=mu+tau
        row={s:v for s,v in row.items() if v}; actions+=len(row)
        # Literal H action applied to the incoming matching polynomial checks every
        # one of the 1487x15 core source coefficients from the separate SOS builder.
        direct=sum((v*np.array(four(s),dtype=np.int64) for s,v in row.items()),np.zeros(15,dtype=np.int64))
        assert np.array_equal(direct,FC[i])
        assert sum(abs(v) for v in row.values())<=row_l1_bound
        for s,v in row.items():
            if s in index:
                core_rows[i,index[s]]=v
                AX[i]+=v*Xi[index[s]]
            if s not in R:R[s]=np.zeros(15,dtype=np.int64)
            R[s]+=v*Xi[i]
    assert all(core_rows.get((j,i))==v for (i,j),v in core_rows.items())
    # Object arithmetic here is deliberate: no unchecked int64 Gram overflow.
    xo=Xi.astype(object); fo=FC.astype(object)
    Qnum=den**2*B.astype(object)+xo.T@AX.astype(object)+den*(fo.T@xo+xo.T@fo)
    assert np.array_equal(Qnum,Qnum.T)
    gram=np.zeros((15,15),dtype=object); residual_rows=0
    batch=[]
    for r in R.values():
        if not np.any(r):continue
        residual_rows+=1;batch.append(r)
        if len(batch)==256:
            ro=np.array(batch,dtype=object);gram+=ro.T@ro;batch=[]
    if batch:
        ro=np.array(batch,dtype=object);gram+=ro.T@ro
    assert residual_rows==35430
    bound=1920*Qnum-gram; bound_den=23040*den**2
    assert np.array_equal(bound,bound.T)
    pe=np.zeros(15,dtype=object);pe[mi[0,0]]=1;pe[mi[0,1]]=-1;pe[mi[1,1]]=1
    physical_factor=Fraction(1,2)  # sqrt2 incoming and raw normalized monomial /2
    E=physical_factor*Fraction(int(pe@bound@pe),bound_den)
    T=physical_factor*Fraction(int(bound[mi[2,2],mi[2,2]]),bound_den)
    assert E==Fraction(5107142386779523,24739011624960)
    assert T==Fraction(358372792045843,1374389534720)
    assert physical_factor*Fraction(int(pe@B@pe),12)==344
    assert physical_factor*Fraction(int(B[mi[2,2],mi[2,2]]),12)==420
    assert E<344 and T<420
    return {'core_action_nonzeros':actions,'compressed_nonzeros':len(core_rows),
            'complete_source_rows':len(keys),'core_source_coefficients_checked':len(core)*15,
            'residual_rows':residual_rows,'raw_monomial_order':mon,
            'raw_upper_denominator':bound_den,
            'raw_upper_numerator':[[str(int(x)) for x in row] for row in bound],
            'residual_gram_numerator':[[str(int(x)) for x in row] for row in gram],
            'normalized_directional_upper':{'E1':str(E),'T12':str(T)},
            'meaning':'Full raw upper form; physical form is 2 P* Q P. Not the actual T0 matrix.'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--family',choices=['all','geometry','normalization','trial'],default='all')
    args=parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU,(90,91))
    start=time.monotonic();cpu=time.process_time()
    results={'scope':'Exact finite controls for the supplied N4 threshold theorem; analytic proof owns convergence.'}
    if args.family in ('all','geometry','trial'):
        core,results['geometry']=small_geometry()
    if args.family in ('all','normalization'):
        results['normalization']=normalization_control()
    if args.family in ('all','trial'):
        keys,source,B=bare_and_source()
        results['trial']=exact_trial(core,keys,source,B)
    results['resources']={'cpu_seconds':time.process_time()-cpu,
        'wall_seconds':time.monotonic()-start,
        'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    assert results['resources']['peak_rss_bytes']<384*1024**2
    print(json.dumps(results,indent=2))
    completed=sum(k in results for k in ('geometry','normalization','trial'))
    print(f"TOTAL: PASS={completed} FAIL=0")

if __name__=='__main__':main()
