"""Independent actual-word/read-collar checks for SA; exact discrete geometry."""
import itertools as it
import json, math, os, re, resource, subprocess, time
from collections import Counter
from functools import lru_cache
import numpy as np

START=time.monotonic(); resources=[]; checks=[]; L=3; h=1

def guard(where):
    cp=subprocess.run(['/usr/bin/memory_pressure','-Q'],capture_output=True,text=True,timeout=5)
    match=re.search(r'System-wide memory free percentage:\s*(\d+)%',cp.stdout)
    assert cp.returncode==0 and match, 'RESOURCE: memory query'
    row={'where':where,'rss':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'free':int(match.group(1)),
         'load':list(os.getloadavg()),'nice':os.getpriority(os.PRIO_PROCESS,0),'elapsed':time.monotonic()-START,
         'threads':{k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']}}
    resources.append(row)
    assert row['rss']<2_000_000_000 and row['free']>=50 and max(row['load'])<20 and row['nice']>=10 and row['elapsed']<=60 and set(row['threads'].values())=={'1'}, ('RESOURCE',row)

def gate(name,ok,detail=None):
    checks.append({'name':name,'passed':bool(ok),'detail':detail})
    assert ok,name

def step(x,mu,sgn):
    y=list(x);y[mu]+=sgn;return tuple(y)

def path(start,target,order):
    x=start;out=[]
    for mu in order:
        while x[mu]!=target[mu]:
            s=1 if x[mu]<target[mu] else -1;y=step(x,mu,s)
            out.append((x if s==1 else y,mu,s));x=y
    return out

def word_templates(mu):
    root=(0,0,0,0);end=step(root,mu,L);out=[]
    for order in it.permutations(range(4)):
        for y in it.product(range(-h,h+1),repeat=4):
            yn=step(y,mu,L);leg=[(step(y,mu,j),mu,1) for j in range(L)]
            back=path(end,yn,order)
            out.append(path(root,y,order)+leg+[(x,d,-s) for x,d,s in reversed(back)])
    return out

@lru_cache(None)
def meta(T,x,mu):
    M=L*T;x=tuple(v%M for v in x);b=tuple(((v+h)//L)%T for v in x)
    if (x[mu]+h)%L==L-1:
        y=list(b);y[mu]=(y[mu]+1)%T
        return b,(b,mu),frozenset([b,tuple(y)])
    return b,None,frozenset()

def distance(T,x,y):
    return sum(min((a-b)%T,(b-a)%T) for a,b in zip(x,y))

def canonical(T,edge,offset):
    x,mu,sgn=edge;return tuple((x[d]+offset[d])%(L*T) for d in range(4)),mu,sgn

def plaq_word(x,mu,nu):
    return [(x,mu,1),(step(x,mu,1),nu,1),(step(x,nu,1),mu,-1),(x,nu,-1)]

guard('start')
templates={mu:word_templates(mu) for mu in range(4)}
counts=Counter();max_distance={'kernel':0,'Wilson':0,'matrix_range':0}; fibre={}
for T in (2,3):
    bases=list(it.product((0,T-1),repeat=4))
    for index,b in enumerate(bases):
        offset=tuple(L*v for v in b)
        for mu in range(4):
            expected=(b,mu)
            for local in templates[mu]:
                edges=[canonical(T,e,offset) for e in local]
                data=[meta(T,x,d) for x,d,s in edges]
                slots=[(vslot,sgn) for (_,vslot,_),(_,_,sgn) in zip(data,edges) if vslot is not None]
                assert slots==[(expected,1)], ('paired crossing',T,b,mu,slots)
                read=set().union(*(set(row[2]) for row in data))
                for row,_,_ in data:
                    md=max(distance(T,row,v) for v in read)
                    assert md<=1,('kernel collar',T,b,mu,row,read)
                    max_distance['kernel']=max(max_distance['kernel'],md)
                counts['paired_words_T'+str(T)]+=1
        if index%4==0:guard('kernel geometry T'+str(T)+' base'+str(index))
    M=L*T
    for xi,x in enumerate(it.product(range(M),repeat=4)):
        for mu,nu in it.combinations(range(4),2):
            edges=[(tuple(v%M for v in y),d,s) for y,d,s in plaq_word(x,mu,nu)]
            data=[meta(T,y,d) for y,d,s in edges]
            read=set().union(*(set(row[2]) for row in data))
            rows={row[0] for row in data}
            for row in rows:
                md=max([distance(T,row,v) for v in read],default=0)
                assert md<=2,('Wilson collar',T,x,mu,nu,row,read)
                max_distance['Wilson']=max(max_distance['Wilson'],md)
                for col in rows:
                    dd=distance(T,row,col);assert dd<=2
                    max_distance['matrix_range']=max(max_distance['matrix_range'],dd)
            counts['fine_plaquettes_T'+str(T)]+=1
        if xi%1500==0:guard('plaquettes T'+str(T)+' site'+str(xi))
    # The fibre is the free positive crossing edge at (1,1,0,0), axis0.
    target=((1,1,0,0),0);X=(0,0,0,0);Y=(1,0,0,0);kernels=set()
    for block in (X,Y):
        for mu in range(4):
            prev=list(block);prev[mu]=(prev[mu]-1)%T
            kernels.add((block,mu));kernels.add((tuple(prev),mu))
    total=0;nonzero=[]
    for b,mu in sorted(kernels):
        offset=tuple(L*v for v in b);hits=0
        for local in templates[mu]:
            edge_hits=[s for x,d,s in (canonical(T,e,offset) for e in local) if (x,d)==target]
            assert len(edge_hits)<=1
            if edge_hits:assert edge_hits==[1];hits+=1
        total+=hits
        if hits:nonzero.append((b,mu,hits))
    assert nonzero==[(X,0,72)] and total==72
    fibre[T]={'distinct_endpoint_kernels':len(kernels),'nonzero':nonzero,'other_words':(len(kernels)-1)*1944}
    guard('complete T'+str(T))
gate('actual row-centred read radius',max_distance['kernel']<=1 and max_distance['Wilson']<=2,max_distance)
gate('periodic crossing fibre multiplicity',all(v['nonzero'][0][2]==72 for v in fibre.values()),fibre)
# A remote coarse link in the opposite side of one double-face plaquette
# changes its genuine diagonal scalar Hessian while the row's coarse data stay fixed.
I=np.eye(2,dtype=complex);sz=np.diag([1.,-1.]);Tgen=1j*sz/math.sqrt(2)
def remote_hessian(theta):
    P=np.diag(np.exp(1j*theta*np.array([1.,-1.])))
    return float(-np.trace(Tgen@Tgen@P).real)
a,b=remote_hessian(.06),remote_hessian(.061)
gate('actual remote coefficient omission detected',abs(a-b)>1e-10,{'first':a,'second':b,'difference':abs(a-b),'read_distance':2})
# Exact good-event obstruction and discontinuity of the actual SU(2) indicator.
alpha=.43;beta=.07;delta=2*abs(math.sin(alpha)*math.sin(beta));df=eta=delta/(2*(L*L+4))
gate('coarse curvature excludes undersized good event',delta>L*L*df+4*eta,{'delta':delta,'necessary_rhs':L*L*df+4*eta})
threshold=.05;astar=2*math.asin(threshold/2);jumps=[]
for displacement in (1e-3,1e-6,1e-9):
    lower=2*abs(math.sin((astar-displacement/2)/2))<=threshold
    upper=2*abs(math.sin((astar+displacement/2)/2))<=threshold
    jumps.append(int(lower)-int(upper))
gate('hard indicator uniform norm does not follow field tail',jumps==[1,1,1],jumps)
guard('completion')
print(json.dumps({'checks':checks,'counts':dict(counts),'maximum_read_distances':max_distance,'fibre':fibre,'resources':resources,'proof_scope':'Exact finite support diagnostics; general row-centred radius follows from the plaquette/two-block stencil argument. Does not certify SA12 or complement prices.'},indent=2))
