#!/usr/bin/env python3
"""Exact local occupation-word controls, with no author helper import."""
import itertools, json, os, resource, signal, time
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parent
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def sentinel():
    assert not (RUNTIME/'STOP_REQUESTED.json').exists()
    assert time.time()<json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
sentinel();signal.alarm(180);start=time.time();cpu=time.process_time()
E=[tuple(int(j==i)for j in range(3))for i in range(3)]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
G=sorted([mul(s*2,E[i])for i in range(3)for s in(-1,1)]+[add(mul(s,E[i]),mul(t,E[j]))for i in range(3)for j in range(i+1,3)for s in(-1,1)for t in(-1,1)])
assert len(set(G))==18
def choose_pair(d):
    nz=[i for i,x in enumerate(d)if x]
    if len(nz)==1:
        i=nz[0];sgn=d[i]//2;c=mul(sgn,E[i]);return ('d',i),c,mul(-sgn,E[i]),mul(sgn,E[i]),1
    i,j=nz;s,t=-d[i],d[j];c=mul(d[i],E[i]);return ('v',i,j,s,t),c,mul(s,E[i]),mul(t,E[j]),s*t
def steps(e):return [(i,1 if e[i]>0 else -1)for i in range(3)for _ in range(abs(e[i]))]
def clean(a):return {k:v for k,v in a.items()if v}
def plus(*terms):
    out=defaultdict(int)
    for coeff,a in terms:
        for k,v in a.items():out[k]+=coeff*v
    return clean(out)
def pair_op(endpoints,sites,sign=1):
    bits=[sites.index(p)for p in endpoints];assert bits[0]!=bits[1]
    mask=sum(1<<i for i in bits)
    return {(s^mask,s):sign for s in range(1<<len(sites))if s&mask==mask}
def project_out(a,z,sites,occupied=True):
    bit=1<<sites.index(z)
    return {k:v for k,v in a.items()if bool(k[0]&bit)==occupied}
def gram(a):
    rows=defaultdict(list);out=defaultdict(int)
    for (r,c),v in a.items():rows[r].append((c,v))
    for row in rows.values():
        for i,a in row:
            for j,b in row:out[i,j]+=a*b
    return clean(out)
def dagger(a):return {(c,r):v for (r,c),v in a.items()}
def compose(a,b):
    byrow=defaultdict(list);out=defaultdict(int)
    for (r,c),v in b.items():byrow[r].append((c,v))
    for (r,m),v in a.items():
        for c,w in byrow[m]:out[r,c]+=v*w
    return clean(out)

counts=Counter();pin_checks=0;matrix_checks=0;max_sites=0
for L in (None,5,6,7):
    def tor(p):return p if L is None else tuple(x%L for x in p)
    for d in G:
        typ,c,u,v,sgn=choose_pair(d)
        assert add(c,u)==(0,0,0)and add(c,v)==d
        for e in G:
            if e==d:continue
            path=steps(e);assert len(path)==2
            centers=[c]
            for k,s in path:centers.append(add(centers[-1],mul(s,E[k])))
            if L is None:
                for k,s in path:counts[typ,k]+=1
            z=tor(e);pairs=[(tor(add(cc,u)),tor(add(cc,v)))for cc in centers]
            sites=sorted(set(p for pp in pairs for p in pp));assert z in sites
            max_sites=max(max_sites,len(sites));B=[pair_op(pp,sites,sgn)for pp in pairs]
            A=project_out(B[0],z,sites);assert not project_out(B[2],z,sites)
            D1=plus((1,B[1]),(-1,B[0]));D2=plus((1,B[2]),(-1,B[1]))
            P1=project_out(D1,z,sites);P2=project_out(D2,z,sites)
            assert not plus((1,A),(1,P1),(1,P2))
            triple=[sites.index(tor(x))for x in((0,0,0),d,e)];assert len(set(triple))==3
            mask=sum(1<<i for i in triple)
            assert gram(A)=={(s,s):1 for s in range(1<<len(sites))if s&mask==mask}
            lhs=plus((2,gram(D1)),(2,gram(D2)),(-1,gram(A)))
            rhs=plus((1,gram(plus((1,P1),(-1,P2)))),(2,gram(project_out(D1,z,sites,False))),(2,gram(project_out(D2,z,sites,False))))
            assert lhs==rhs
            pin_checks+=1;matrix_checks+=1
        sentinel()
assert max_sites<=6
for (typ,k),n in counts.items():
    expect=(20 if k==typ[1] else 24)if typ[0]=='d'else(11 if k in typ[1:3]else 12)
    assert n==expect,(typ,k,n,expect)
assert max(counts.values())==24

# All labeled simple graphs through six vertices: a separate integer control
# of the isolated-dimer combinatorics, not a geometric or quantum proxy.
graph_count=0;sharp=False;distant_move_cases=0
for n in range(1,7):
    edges=list(itertools.combinations(range(n),2))
    for mask in range(1<<len(edges)):
        adj=[set()for _ in range(n)]
        for j,(x,y)in enumerate(edges):
            if mask>>j&1:adj[x].add(y);adj[y].add(x)
        deg=list(map(len,adj));iso=deg.count(0)
        dimer_vertices=sum(deg[x]==1 and deg[next(iter(adj[x]))]==1 for x in range(n))
        outside=n-dimer_vertices;triples=sum(m*(m-1)//2 for m in deg)
        assert outside<=iso+3*triples
        assert (outside-n)%2==0
        sharp|=triples>0 and outside==iso+3*triples
        # Fill a new target y=n after removing one end x of an isolated
        # dimer. Allow all target-neighbor sets except its old partner z.
        # This partner must become degree zero, the exact support inclusion
        # used for the distant single-particle coherence estimate.
        for x in range(n):
            if deg[x]!=1:continue
            z=next(iter(adj[x]))
            if deg[z]!=1:continue
            possible=[v for v in range(n)if v not in (x,z)]
            for links in range(1<<len(possible)):
                new_neighbors={v for j,v in enumerate(possible)if links>>j&1}
                after_z=(adj[z]-{x})|({n}if z in new_neighbors else set())
                assert not after_z
                distant_move_cases+=1
        graph_count+=1
    sentinel()
assert sharp

# Literal hard-core pair commutators: identical, one-end overlap, disjoint.
commutators=[]
for e,f in [((0,1),(0,1)),((0,1),(0,2)),((0,1),(2,3))]:
    sites=list(range(4));be=pair_op(e,sites);bf=pair_op(f,sites)
    actual=plus((1,compose(be,dagger(bf))),(-1,compose(dagger(bf),be)))
    if e==f:
        expected={(s,s):1-int(bool(s&1))-int(bool(s&2))for s in range(16)}
        expected=clean(expected)
    elif set(e)&set(f):
        expected={}
        for s in range(16):
            if s&2 and not s&4:expected[s^2^4,s]=1-2*int(bool(s&1))
    else:expected={}
    assert actual==expected
    commutators.append({'e':e,'f':f,'exact_identity':True})

# Actual axial pair-bond action between neighboring centers. The E projector
# is formed from its literal normalized coefficients (rational Gram).
from fractions import Fraction as F
PE=[[F(int(i==j))-F(1,3)for j in range(3)]for i in range(3)]
x=(0,0,0);y=(0,0,1)
vertices=[(x,0),(y,0),(x,1),(y,2)]
physical=[frozenset((add(c,E[i]),add(c,mul(-1,E[i]))))for c,i in vertices]
assert len(set(physical))==4
weights=[]
for j in range(4):
    (c,i),(cc,ii)=vertices[j],vertices[(j+1)%4]
    assert sum(abs(a-b)for a,b in zip(c,cc))==1
    weights.append(-PE[ii][i])
prod=F(1)
for w in weights:prod*=w
assert weights==[F(-2,3),F(1,3),F(1,3),F(1,3)]and prod==F(-2,81)

result={'pin_operator_cases':pin_checks,'full_local_SOS_matrix_identities':matrix_checks,'tori_and_infinite_coordinates':[None,5,6,7],'maximum_local_sites':max_sites,'maximum_local_dimension':2**max_sites,'gradient_multiplicities':[{'type':str(t),'direction':k,'coefficient':n}for(t,k),n in sorted(counts.items())],'maximum_multiplicity':24,'abstract_graph_cases':graph_count,'outside_dimer_bound_sharp':sharp,'literal_commutator_controls':commutators,'axial_four_cycle':{'vertices':vertices,'weights_in_tau_units':list(map(str,weights)),'product_in_tau_fourth_units':str(prod),'scope':'Diagonal occupation-phase sign gauge only; no phase or general positivity exclusion.'},'wall_seconds':round(time.time()-start,3),'cpu_seconds':round(time.process_time()-cpu,3),'peak_rss_native_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'threads':{k:os.environ.get(k)for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']},'scope':'Finite exact controls of the analytic all-state/all-volume argument, not a phase scan.'}
result['distant_single_move_support_cases']=distant_move_cases
(ROOT/'local_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items()if k not in ['gradient_multiplicities','literal_commutator_controls']},indent=2))
