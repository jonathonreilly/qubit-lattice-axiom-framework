#!/usr/bin/env python3
"""Literal pair-row control; no imported model or author-runner functions."""
import collections, fractions, hashlib, itertools, json, pathlib, resource, time
F=fractions.Fraction
start=time.monotonic(); cpu=time.process_time()
axes=((1,0,0),(0,1,0),(0,0,1)); zero=(0,0,0)
def add(x,y,L=None):
    z=tuple(a+b for a,b in zip(x,y)); return tuple(a%L for a in z) if L else z
def mul(s,x): return tuple(s*a for a in x)
def pair(x,y): return tuple(sorted((x,y)))
def words(x,L=None):
    ds=[{pair(add(x,e,L),add(x,mul(-1,e),L)):1} for e in axes]
    planes=[]
    for i,j in itertools.combinations(range(3),2):
        planes.append([{pair(add(x,mul(s,axes[i]),L),add(x,mul(t,axes[j]),L)):s*t} for s,t in itertools.product((-1,1),repeat=2)])
    return ds,planes
def combine(ws,coeffs):
    d=collections.defaultdict(int)
    for w,a in zip(ws,coeffs):
        for e,b in w.items(): d[e]+=a*b
    return {e:a for e,a in d.items() if a}
def qrows(x,L=None):
    ds,ps=words(x,L)
    return [(combine(ds,(1,-1,0)),F(1,2)),(combine(ds,(1,1,-2)),F(1,6))]+[(combine(p,(1,1,1,1)),F(1,4)) for p in ps]
def srows(x,L=None):
    ds,ps=words(x,L)
    return [(combine(ds,(1,1,1)),F(2,3))]+[(combine([p[i],p[j]],(1,-1)),F(1,4)) for p in ps for i,j in itertools.combinations(range(4),2)]
def grows(x,L=None):
    a=qrows(x,L); out=[]
    for e in axes:
        b=qrows(add(x,e,L),L)
        for (u,c),(v,d) in zip(a,b):
            assert c==d and not (set(u)&set(v)), 'adjacent centers share pair'
            out.append((combine([v,u],(1,-1)),c))
    return out
def diag(rows):
    d=collections.defaultdict(F)
    for w,c in rows:
        for e,a in w.items(): d[e]+=c*a*a
    return dict(d)
def edges(L):
    typ={}
    for x in itertools.product(range(L),repeat=3):
        for e in axes:
            for s in (-1,1): typ[pair(x,add(x,mul(2*s,e),L))]='a'
        for i,j in itertools.combinations(range(3),2):
            for s,t in itertools.product((-1,1),repeat=2):typ[pair(x,add(add(x,mul(s,axes[i]),L),mul(t,axes[j]),L))]='p'
    return typ
results={}
for L in (5,6):
    sites=list(itertools.product(range(L),repeat=3)); se=[]; gr=[]; att=[]
    for x in sites:
        se.extend(srows(x,L));gr.extend(grows(x,L))
        att.extend((w,c*(-2 if k<2 else -1)) for k,(w,c) in enumerate(qrows(x,L)))
    sd,gd,ad=map(diag,(se,gr,att)); et=edges(L)
    assert set(sd)==set(gd)==set(ad)==set(et)
    for e,t in et.items():
        assert sd[e]==({'a':F(2,3),'p':F(3,2)}[t])
        assert gd[e]==({'a':F(4),'p':F(3)}[t])
        assert ad[e]==({'a':F(-4,3),'p':F(-1,2)}[t])
    configs=[set(),{sites[0]},{(0,0,0),(2,0,0)},{(0,0,0),(1,1,0)},set(sites)]
    # Fixed arithmetic masks, with no randomness or sampled quantum assumption.
    configs += [{x for j,x in enumerate(sites) if ((j*37+salt*19)%101)<level} for salt in range(5) for level in (3,17,50,90)]
    neighbors={x:set() for x in sites}
    for x,y in et: neighbors[x].add(y);neighbors[y].add(x)
    for cfg in configs:
        m={x:len(neighbors[x]&cfg) for x in cfg}
        V3=sum(v*(v-1)//2 for v in m.values())
        D=sum((v-1)*(v-2)//2 for v in m.values())
        s=sum(c for e,c in sd.items() if set(e)<=cfg)
        a=sum(c for e,c in ad.items() if set(e)<=cfg)
        assert len(cfg)+V3+a==D+s
        # Original literal quadratic lowering row norms on a basis configuration.
        normS=sum(c*sum(z*z for e,z in w.items() if set(e)<=cfg) for w,c in se)
        assert normS==s
    results[f'L{L}']={'sites':len(sites),'positive_S_rows':len(se),'gradient_rows':len(gr),'edges':dict(collections.Counter(et.values())),'configurations':len(configs),'all_weights_exact':True}
# Degree lower bound in both parameter branches, with literal edge-type composition.
degree_checks=0
for tau in (F(1,100),F(1,6),F(1,3),F(5,6),F(1),F(100)):
    mu=F(1); c=min(mu,mu/3+2*tau); wa=2*mu/3+4*tau;wp=3*mu/2+3*tau
    for ma in range(7):
        for mp in range(13):
            m=ma+mp
            assert mu*(m-1)*(m-2)/2+(wa*ma+wp*mp)/2>=c
            degree_checks+=1
    assert min(mu,wa/2)==c
results['degree_checks']=degree_checks
# Infinite-lattice local rows, just the finitely many centers that can cover origin.
centers=list(itertools.product(range(-2,3),repeat=3))
S=[];G=[]
for x in centers:
    S.extend(srows(x));G.extend(grows(x))
def support(w):return set(itertools.chain.from_iterable(w))
def rad(x):return sum(abs(a) for a in x)
incident={e for w,c in S+G for e in w if zero in e}
assert len(incident)==18
for e in incident:
    relevant=[(w,c) for w,c in S+G if e in w]
    assert all(max(map(rad,support(w)))<=3 for w,c in relevant)
    assert sum(c*w.get(e,0)**2 for w,c in S)==({'a':F(2,3),'p':F(3,2)}['a' if max(abs(a-b) for a,b in zip(*e))==2 else 'p'])
# Radius2 is insufficient for complete incident gradient weight; explicit missed row.
missed=[(w,c) for w,c in G if any(zero in e for e in w) and max(map(rad,support(w)))==3]
assert missed
B3={x for x in itertools.product(range(-3,4),repeat=3) if rad(x)<=3}
insideS=[(w,c) for w,c in S if support(w)<=B3]
insideG=[(w,c) for w,c in G if support(w)<=B3]
for e in incident:
    assert diag(insideS)[e]==diag(S)[e]
    assert diag(insideG)[e]==diag(G)[e]
results['local']={'incident_edges':18,'radius3_complete':True,'radius2_missed_gradient_rows':len(missed),'witness':[[[list(a),list(b)],v] for (a,b),v in missed[0][0].items()]}
# Nonzero finite-volume coherent fixture: normalized uniform E1 pair, norm^2=V.
# Its H0 energy vanishes by actual constant Q outputs and local singlet cancellation;
# full dephasing has two particles and one axial edge in every branch.
L=5;psi=collections.defaultdict(int)
for x in itertools.product(range(L),repeat=3):
    ds,_=words(x,L)
    for e,a in combine(ds,(1,-1,0)).items():psi[e]+=a
norm=sum(a*a for a in psi.values());assert norm==2*L**3
for x in itertools.product(range(L),repeat=3):
    for w,c in srows(x,L)+grows(x,L):assert sum(a*psi.get(e,0) for e,a in w.items())==0
assert all(edges(L)[e]=='a' for e in psi)
results['coherent_pair']={'norm_without_sqrt2':norm,'N':2,'H0':0,'dephased_energy_mu':'2/3','dephased_energy_tau':'4','same_occupation_distribution':True}
results['actual_resources']={'cpu_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-start,'maxrss_platform_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
results['runner_sha256']=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
print(json.dumps(results,indent=2,sort_keys=True))
