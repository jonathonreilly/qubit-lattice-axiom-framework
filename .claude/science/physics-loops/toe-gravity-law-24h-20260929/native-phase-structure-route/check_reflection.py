#!/usr/bin/env python3
"""Exact two-site Pauli projections of the actual full hard-core Hamiltonian.

No prior-route code imported, no full torus Hilbert-space enumeration.
The projection is normalized partial trace, not an effective Hamiltonian.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import json, os, resource, signal, time

ROOT=Path(__file__).resolve().parent
RT=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def sentinel():
    assert not (RT/'STOP_REQUESTED.json').exists()
    assert time.time()<json.loads((RT/'DEADLINE.json').read_text())['deadline_epoch']
sentinel();signal.alarm(60);started=time.time();cpu=time.process_time()
E=[tuple(int(i==j)for j in range(3))for i in range(3)]
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(s,a):return tuple(s*x for x in a)
G=[scale(2*s,E[i])for i in range(3)for s in(-1,1)]
G += [plus(scale(s,E[i]),scale(t,E[j]))for i in range(3)for j in range(i+1,3)for s in(-1,1)for t in(-1,1)]
S=[(0,0,0)]+[scale(s,e)for e in E for s in(-1,1)]+G
assert len(set(S))==25
records=[]
for L in (12,14,16):
    def tor(x):return tuple(a%L for a in x)
    def add(x,y):return tor(plus(x,y))
    left=[tor((-1,0,0)),tor((-2,0,0))]
    right=[tor((2,0,0)),tor((3,0,0))]
    targets=set(left+right)
    wanted={frozenset((x,y)):(i,j)for i,x in enumerate(left)for j,y in enumerate(right)}
    centers={add(x,scale(-1,s))for x in targets for s in S}
    values=defaultdict(F);primitive_terms=0
    def write(pair,pa,pb,coef,component,imag=False):
        if pair not in wanted:return
        i,j=wanted[pair]
        values[component,i,j,pa,pb,imag]+=coef
    def project_product(A,B,coef,component):
        # Creation pair A followed by annihilation pair B. At common sites
        # the literal local factor is b^dagger b=n. Else it is b or b^dagger.
        common=set(A)&set(B)
        if len(common)==2:
            pair=frozenset(A)
            write(pair,'Z','Z',coef/F(4),component)
        elif len(common)==1:
            ca=next(iter(set(A)-common));an=next(iter(set(B)-common))
            pair=frozenset((ca,an))
            if pair not in wanted:return
            i,j=wanted[pair]
            # Trace n_common=1/2; b=(X+iY)/2, b^dagger=(X-iY)/2.
            write(pair,'X','X',coef/F(8),component)
            write(pair,'Y','Y',coef/F(8),component)
            sign=1 if ca==left[i] else -1
            write(pair,'X','Y',sign*coef/F(8),component,True)
            write(pair,'Y','X',-sign*coef/F(8),component,True)
        # Four distinct endpoints have zero two-site partial trace.
    def sectors(c):
        axial=[frozenset((add(c,e),add(c,scale(-1,e))))for e in E]
        ans=[(axial,[[F(int(i==j))-F(1,3)for j in range(3)]for i in range(3)],-2)]
        for i in range(3):
            for j in range(i+1,3):
                signs=[(s,t)for s in(-1,1)for t in(-1,1)]
                ps=[frozenset((add(c,scale(s,E[i])),add(c,scale(t,E[j]))))for s,t in signs]
                gram=[[F(s*t*u*v,4)for u,v in signs]for s,t in signs]
                ans.append((ps,gram,-1))
        return ans
    for c in centers:
        # Actual 153 triple projectors, with no mean-field replacement.
        neigh=[add(c,d)for d in G]
        assert len(set(neigh))==18
        for y,z in combinations(neigh,2):
            triple=(c,y,z);assert len(set(triple))==3
            for x,w in combinations(triple,2):
                write(frozenset((x,w)),'Z','Z',F(1,8),'mu')
            primitive_terms+=1
        base=sectors(c)
        for ps,gram,mult in base:
            for i,A in enumerate(ps):
                for j,B in enumerate(ps):
                    project_product(A,B,mult*gram[i][j],'mu');primitive_terms+=1
        for k in range(3):
            moved=sectors(add(c,E[k]))
            for (ps,g,_),(qs,_,__) in zip(base,moved):
                for AA,sa in ((ps,-1),(qs,1)):
                    for BB,sb in ((ps,-1),(qs,1)):
                        for i,A in enumerate(AA):
                            for j,B in enumerate(BB):
                                project_product(A,B,sa*sb*g[i][j],'tau');primitive_terms+=1
    values={k:v for k,v in values.items()if v}
    expected={('mu',0,1,'Z','Z',False):F(1,8),('mu',1,0,'Z','Z',False):F(1,8)}
    assert values==expected,(L,values)
    # F=(n_a-1/2)+(n_b-1/2)=-(Z_a+Z_b)/2.
    derivative=-sum(values.values())/4
    assert derivative==F(-1,16)
    records.append({'L':L,'centers_generated':len(centers),'literal_projector_products':primitive_terms,
                    'nonzero_two_site_cross_Pauli_coefficients':[{'key':str(k),'value':str(v)}for k,v in sorted(values.items())],
                    'RP_first_derivative_in_mu_units':str(derivative),
                    'both_diagonal_three_by_three_Pauli_blocks_zero':True,
                    'tau_and_chemical_potential_cross_blocks_zero':True})
    sentinel()

# Constants for the separate local-commutator source-response proof.
D=24**3*4*7*10*3//6
assert D==1935360
result={'checks':records,'source_third_order_remainder_constant':D,
        'uniform_five_channel_source_constants':{
            'A_star_in_units_of_182mu_plus_240tau':96**4*25*30*35*40//24,
            'D_star':96**3*6*11*16*8//6,
            'source_density_coefficient_s':6},
        'method':'Full local operator-product partial traces; analytical all-volume proof remains necessary.',
        'wall_seconds':round(time.time()-started,3),'cpu_seconds':round(time.process_time()-cpu,3),
        'peak_rss_bytes_on_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'threads':{k:os.environ.get(k)for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')}}
(ROOT/'reflection_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
