#!/usr/bin/env python3
"""One bounded exact job: local full-carrier identity and sparse packed states.

Priced at <100 MB and <30 s: 64 shell basis states, graph incidence on
L=5,6,7, 24 rotations, and at most54 sparse configurations on1000 qubits.
No source runner import, bosonic approximation, or many-body diagonalization.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, permutations, product
from collections import defaultdict, Counter
from datetime import datetime,timezone
import json,time,resource

OUT=Path(__file__).resolve().parent
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
deadline=json.loads((RUNTIME/'DEADLINE.json').read_text())
assert datetime.now(timezone.utc).timestamp()<deadline['deadline_epoch']
assert not (RUNTIME/'STOP_REQUESTED.json').exists()
START=time.monotonic()
VECTORS=[tuple(s if k==j else 0 for k in range(3)) for j in range(3) for s in [1,-1]]
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(a,c):return tuple(c*x for x in a)
DG=set(scale(v,2) for v in VECTORS)
for i,j in combinations(range(3),2):
    for si,sj in product([-1,1],repeat=2):DG.add(plus(scale(VECTORS[2*i],si),scale(VECTORS[2*j],sj)))
assert len(DG)==18 and (0,0,0) not in DG

# Local bit ordering (+x,-x,+y,-y,+z,-z).
D=[[(1<<(2*j))|(1<<(2*j+1)),1] for j in range(3)]
E1=[D[0],(D[1][0],-1)]
E2=[D[0],D[1],(D[2][0],-2)]
T=[]
for i,j in combinations(range(3),2):
    T.append([((1<<(2*i+a))|(1<<(2*j+b)),(-1)**(a+b)) for a,b in product(range(2),repeat=2)])
WTERMS=[(12,E1),(4,E2)]+[(3,t) for t in T] #12*(2 PE+PT)
ATERMS=[(8,D)]
for t in T:
    for a,b in combinations(range(4),2):ATERMS.append((3,[t[a],(t[b][0],-t[b][1])]))
def qdagq_column(bits,words):
    out=defaultdict(int)
    for rem,c in words:
        if bits&rem!=rem:continue
        middle=bits^rem
        for ins,d in words:
            if middle&ins:continue
            out[middle|ins]+=c*d
    return {k:v for k,v in out.items() if v}
def apply_column(bits,terms):
    out=defaultdict(int)
    for weight,words in terms:
        for target,c in qdagq_column(bits,words).items():out[target]+=weight*c
    return {k:v for k,v in out.items() if v}
for bits in range(64):
    a=apply_column(bits,ATERMS);w=apply_column(bits,WTERMS)
    total=Counter(a);total.update(w)
    actual={k:v for k,v in total.items() if v}
    expected=24*sum(bits&m==m for m,c in D)+12*sum(bits&m==m for t in T for m,c in t)
    assert actual==({bits:expected} if expected else {})

# Exact degree-polynomial certificate; all occupancies of the18-neighbor star.
degree_rows=[]
for m in range(19):
    v3=m*(m-1)//2;cap=max(m-1,0);res=(m-1)*(m-2)//2
    assert 1-m+v3==res and res>=0
    assert 1-m+cap==int(m==0) and v3>=cap
    degree_rows.append([m,v3,cap,res])

rots=[]
for p in permutations(range(3)):
    parity=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    for s in product([-1,1],repeat=3):
        if parity*s[0]*s[1]*s[2]!=1:continue
        def rot(v):
            z=[0]*3
            for i in range(3):z[p[i]]=s[i]*v[i]
            return tuple(z)
        assert {rot(v) for v in DG}==DG
        slot=[VECTORS.index(rot(v)) for v in VECTORS]
        def rb(bits):return sum(1<<slot[i] for i in range(6) if bits>>i&1)
        for bits in range(64):
            assert {rb(a):c for a,c in apply_column(bits,WTERMS).items()}==apply_column(rb(bits),WTERMS)
        rots.append((p,s))
assert len(rots)==24

def geometry(L):
    coords=list(product(range(L),repeat=3));idx={x:i for i,x in enumerate(coords)}
    def site(x):return idx[tuple(t%L for t in x)]
    shell=[[site(plus(x,v)) for v in VECTORS] for x in coords]
    near=[[site(plus(x,d)) for d in DG] for x in coords]
    return coords,shell,near
incidence=[]
for L in [5,6,7]:
    coords,shell,near=geometry(L);opp=Counter();cross=Counter()
    for nodes in shell:
        assert len(set(nodes))==6
        for mask,c in D:opp[tuple(sorted(nodes[i] for i in range(6) if mask>>i&1))]+=1
        for t in T:
            for mask,c in t:cross[tuple(sorted(nodes[i] for i in range(6) if mask>>i&1))]+=1
    assert set(opp).isdisjoint(cross)
    assert set(opp.values())=={1} and set(cross.values())=={2}
    assert len(opp)==3*L**3 and len(cross)==6*L**3
    edges={tuple(sorted((x,y))) for x,ys in enumerate(near) for y in ys}
    assert edges==set(opp)|set(cross)
    assert all(len(set(ys))==18 and x not in ys for x,ys in enumerate(near))
    incidence.append({'L':L,'vertices':L**3,'opposite_edges':len(opp),'cross_edges':len(cross),'near_degree':18})

# Literal global action on an8-particle packed coherent state, L10.
L=10;coords,shell,near=geometry(L);index={x:i for i,x in enumerate(coords)}
centers=[(0,0,0),(5,0,0),(0,5,0),(0,0,5)]
chosen=[E1,E2,E2,E2]
state={0:1}
for x,words in zip(centers,chosen):
    nodes=shell[index[x]];nxt=defaultdict(int)
    for bits,a in state.items():
        for mask,c in words:
            globalmask=sum(1<<nodes[i] for i in range(6) if mask>>i&1)
            assert not bits&globalmask
            nxt[bits|globalmask]+=a*c
    state=dict(nxt)
assert len(state)==54
global_terms=[]
for nodes in shell:
    for weight,words in WTERMS:
        global_terms.append((weight,[(sum(1<<nodes[i] for i in range(6) if mask>>i&1),c) for mask,c in words]))
hout=defaultdict(int);vout=defaultdict(int)
for bits,a in state.items():
    N=bits.bit_count();assert N==8;hout[bits]+=12*N*a
    for weight,words in global_terms:
        for target,c in qdagq_column(bits,words).items():hout[target]-=weight*c*a
    occ=[i for i in range(L**3) if bits>>i&1]
    degrees=[sum(bits>>y&1 for y in near[x]) for x in occ]
    assert degrees==[1]*8
    vout[bits]+=12*sum(m*(m-1)//2 for m in degrees)*a
assert not {k:v for k,v in hout.items() if v}
assert not {k:v for k,v in vout.items() if v}

# Full-shell coherent-product expectation, rational normalized site amplitudes.
product_rows=[]
for u,v in [(F(1),F(0)),(F(4,5),F(3,5)),(F(3,5),F(4,5)),(F(0),F(1))]:
    rho=v*v;psi={bits:u**(6-bits.bit_count())*v**bits.bit_count() for bits in range(64)}
    expectation=F(0)
    for bits,a in psi.items():
        for target,c in apply_column(bits,WTERMS).items():expectation+=psi[target]*c*a/F(12)
    assert expectation==8*rho**3-rho**4
    stabilized=rho-expectation+153*rho**3
    assert stabilized==rho+145*rho**3+rho**4
    product_rows.append({'rho':str(rho),'attraction_per_center':str(expectation),'V3_energy_per_vertex':str(stabilized)})

data={'local_full_carrier_columns':64,'sum_of_squares_terms_per_center':len(ATERMS),'cubic_rotations':24,'neighbor_displacements':sorted(DG),'triple_terms_per_center':153,'degree_certificate_rows':degree_rows,'torus_incidence':incidence,'packed_state':{'L':L,'qubits':L**3,'particles':8,'coherent_configurations':len(state),'norm_squared':sum(v*v for v in state.values()),'H_residual_terms':0,'V3_residual_terms':0},'product_state_checks':product_rows,'elapsed_s':time.monotonic()-START,'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'arithmetic':'integer and fractions.Fraction only'}
(OUT/'results.json').write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))
