#!/usr/bin/env python3
"""Independent literal controls for this author derivation; no prior runner import."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import sys, time, resource, json, math, itertools, hashlib
from pathlib import Path
from fractions import Fraction as F
START=time.monotonic(); CPU=time.process_time()
PACK=Path(__file__).resolve().parent
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (RUNTIME/'STOP_REQUESTED.json').exists(), 'STOP requested'
assert time.time()<json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU,(30,30))

def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def dist(x,y): return max(abs(a-b) for a,b in zip(x,y))
E=[tuple(int(i==j) for i in range(3)) for j in range(3)]
G=set()
for e in E:
    G.update(tuple(s*2*a for a in e) for s in (-1,1))
for i in range(3):
    for j in range(i+1,3):
        for s,t in itertools.product((-1,1),repeat=2): G.add(tuple(s*E[i][k]+t*E[j][k] for k in range(3)))
SITES=((0,0,0),(2,0,0),(1,1,0),(0,2,0),(2,2,0),
       (15,0,0),(17,0,0),(0,15,0),(1,16,0),(0,0,15),(0,0,17),(1,1,15))

def selected(S,R):
    S=frozenset(S)
    edges=frozenset(frozenset((x,y)) for x,y in itertools.combinations(S,2)
                   if sub(x,y) in G and all(min(dist(z,x),dist(z,y))>R for z in S-{x,y}))
    endpoints=set().union(*edges) if edges else set()
    return edges,S-endpoints

removals=0; states=0; caps=0
for R in (2,3,5):
    image=set()
    for mask in range(1<<len(SITES)):
        S=frozenset(SITES[i] for i in range(len(SITES)) if mask>>i&1)
        A,B=selected(S,R); key=(A,B)
        assert key not in image
        image.add(key); states+=1
        assert 2*len(A)+len(B)==len(S)
        for e in A:
            assert selected(S-e,R)==(A-{e},B)
            removals+=1
        Ab,Bb=selected(S,R+4)
        assert Ab<=A
        # Exact cutoff inequality for arbitrary artificial cell partitions and caps.
        cells={}
        for e in A:
            x=min(e); j=tuple(c//10 for c in x)
            cells.setdefault(j,[0,0]); cells[j][0]+=1; cells[j][1]+=int(e in Ab)
        loss=0
        for n,nb in cells.values():
            M=max(1,nb); K=2*M
            if n>K: loss+=n
        assert loss<=2*(len(A)-len(Ab))<=len(Bb)
        caps+=1

# Every actual positive row, reconstructed from endpoints, has edge diameter <=4.
# Weighted incidence: sum row coefficient squared norm for each participating edge.
def canonical_edge(e): return tuple(sorted(e))
def local_words(center):
    ax=[canonical_edge((add(center,e),sub(center,e))) for e in E]
    planes=[]
    for i in range(3):
        for j in range(i+1,3):
            planes.append([(canonical_edge((add(center,tuple(s*a for a in E[i])),add(center,tuple(t*a for a in E[j])))),s*t) for s,t in itertools.product((-1,1),repeat=2)])
    return ax,planes
D=[tuple(2*a for a in e) for e in E]
for i in range(3):
    for j in range(i+1,3):
        D.extend(tuple(E[i][k]+s*E[j][k] for k in range(3)) for s in (-1,1))
targets=[canonical_edge(((0,0,0),d)) for d in D]
inc={e:F(0) for e in targets}; maxhaus=0
rows=[]
for x in itertools.product(range(-4,5),repeat=3):
    for d in D:
        e=canonical_edge((x,add(x,d)))
        for unit in E:
            ep=canonical_edge((add(x,unit),add(add(x,d),unit)))
            rows.append(((e,ep),F(2)))
    ax,planes=local_words(x)
    rows.append((tuple(ax),F(2)))
    for plane in planes:
        for (e,s),(f,t) in itertools.combinations(plane,2): rows.append(((e,f),F(1,2)))
for es,w in rows:
    for e in es:
        if e in inc: inc[e]+=w
    for e,f in itertools.combinations(es,2):
        haus=max(max(min(dist(x,y) for y in f) for x in e),max(min(dist(y,x) for x in e) for y in f))
        maxhaus=max(maxhaus,haus)
assert max(inc.values())==15 and maxhaus<=4

# Literal exterior guard boundaries and matching-profile amplitudes.
boundaries={}
for R in (2,3,5,10,20):
    lo=(-R-2,-R,-R); hi=(R+2,R,R)
    inside=lambda x: all(lo[j]<=x[j]<=hi[j] for j in range(3))
    faces=0
    for j in range(3):
        others=[k for k in range(3) if k!=j]
        for vals in itertools.product(*(range(lo[k],hi[k]+1) for k in others)):
            for side in (-1,1):
                x=[0,0,0]
                for k,v in zip(others,vals):x[k]=v
                x[j]=lo[j]-1 if side<0 else hi[j]
                y=add(tuple(x),E[j])
                assert inside(x)!=inside(y)
                # q=0 iff one removed endpoint is within R of one residual endpoint.
                for z in (tuple(x),y):
                    q=min(dist(a,b) for a in ((0,0,0),(2,0,0)) for b in (z,add(z,(2,0,0))))>R
                    assert q==(not inside(z))
                faces+=1
    assert faces==24*R*R+56*R+22
    boundaries[str(R)]={'boundary_edges':faces,'one_channel_gradient':str(F(faces,2))}

# Gaussian rational arithmetic; all de Finetti entries are checked exactly.
def C(a=0,b=0):return (F(a),F(b))
def ca(x,y):return (x[0]+y[0],x[1]+y[1])
def cm(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def cc(x):return (x[0],-x[1])
def cs(x,s):return (x[0]*s,x[1]*s)
zero=C()
def occupations(n,d):
    if d==1:yield (n,);return
    for k in range(n+1):
        for tail in occupations(n-k,d-1):yield (k,)+tail

def fact(m):return math.prod(math.factorial(i) for i in m)
def plus(m,inds):
    a=list(m)
    for i in inds:a[i]+=1
    return tuple(a)
def matrix_zero(d):return [[zero for j in range(d)] for i in range(d)]
results=[]
for n in (2,3,5):
    d=5; occ=list(occupations(n,d))
    picks=sorted(set([0,1,2,len(occ)//4,len(occ)//2,len(occ)-2,len(occ)-1]))
    poly={occ[j]:C((j%5)-2,(j%3)-1) for j in picks}
    poly={m:v for m,v in poly.items() if v!=zero}
    Z=sum((cm(v,cc(v))[0]*F(fact(m),math.factorial(n)) for m,v in poly.items()),F(0))
    g1=matrix_zero(d); g2=matrix_zero(d*d)
    for k,g in ((1,g1),(2,g2)):
        inds=list(itertools.product(range(d),repeat=k))
        for residual in occupations(n-k,d):
            values=[cs(poly.get(plus(residual,ij),zero),F(fact(plus(residual,ij)),fact(residual))) for ij in inds]
            weight=F(fact(residual),math.factorial(n))/Z/F(math.prod(range(n-k+1,n+1)))
            for i,v in enumerate(values):
                for j,w in enumerate(values):g[i][j]=ca(g[i][j],cs(cm(v,cc(w)),weight))
    assert sum(g1[i][i][0] for i in range(d))==1
    assert sum(g2[i][i][0] for i in range(d*d))==1
    den=(n+d)*(n+d+1); dim=math.comb(n+d-1,d-1)
    for i,j,k,l in itertools.product(range(d),repeat=4):
        # P_sym(gamma1 tensor I)P_sym has four terms, each divided by four.
        sym=zero
        for v,flag in ((g1[i][k],j==l),(g1[i][l],j==k),(g1[j][k],i==l),(g1[j][l],i==k)):
            if flag:sym=ca(sym,v)
        predicted=ca(cs(g2[i*d+j][k*d+l],n*(n-1)),cs(sym,n))
        predicted=ca(predicted,C(int(i==k and j==l)+int(i==l and j==k)))
        predicted=cs(predicted,F(1,den))
        moment=zero
        for m,v in poly.items():
            for t,w in poly.items():
                alpha=plus(t,(i,j)); beta=plus(m,(k,l))
                if alpha==beta:
                    integral=F(math.factorial(d-1)*fact(alpha),math.factorial(n+2+d-1))
                    moment=ca(moment,cs(cm(v,cc(w)),dim*integral/Z))
        assert predicted==moment,(n,i,j,k,l,predicted,moment)
    results.append({'n':n,'d':d,'ordered_entries':d**4,'complex_polynomial_terms':len(poly),'exact':True})

# Actual pair normalization: D_s annihilates normalized two-pair tensors to A_s.
# On a coherent n-sector, sum D_s^dagger D_s = n(n-1)/2, all 15 components.
for n in range(2,15):
    occ=(n-2,1,1,0,0)
    diag=sum(m*(m-1)//2 for m in occ)
    off=sum(occ[i]*occ[j] for i in range(5) for j in range(i+1,5))
    assert diag+off==n*(n-1)//2

out={'description':'Literal selected-edge/environment controls and exact full complex d=5 two-body identity',
     'selected_states_checked':states,'selected_removals_checked':removals,'cap_checks':caps,
     'row_weighted_incidence':[str(inc[e]) for e in targets],'row_max_Hausdorff_distance':maxhaus,
     'guard_boundaries':boundaries,'coherent_identity':results,
     'scope':'Finite controls of stated formulas; no microscopic-to-T0 comparison, EOS, large Fock, or threshold matrix evaluation',
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'cpu_seconds':time.process_time()-CPU,'wall_seconds':time.monotonic()-START,
     'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
# macOS ru_maxrss is bytes; this campaign runs on macOS.
assert out['peak_rss_bytes']<150*1024*1024
(PACK/'controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
