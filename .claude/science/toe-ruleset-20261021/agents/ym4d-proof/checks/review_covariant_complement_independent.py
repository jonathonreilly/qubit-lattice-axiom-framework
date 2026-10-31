#!/usr/bin/env python3
"""Independent finite checks; imports no author checker or generated fixtures."""
import itertools, json, math, os, resource, time
import numpy as np
from scipy.linalg import expm, logm
from scipy.special import roots_legendre, iv

START=time.monotonic()
rng=np.random.default_rng(93471062)
results=[]
def record(name,ok,**details):
    results.append({'name':name,'pass':bool(ok),**details})
def op(a): return float(np.linalg.norm(a,2))
def hs(a): return float(np.linalg.norm(a,'fro'))
def generator(n):
    z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    a=(z-z.conj().T)/2
    a-=np.trace(a)*np.eye(n)/n
    return a/hs(a)
def shift(x,d,s):
    y=list(x); y[d]+=s; return tuple(y)
def canonical(x,d,sign):
    return ((x,d),1) if sign==1 else ((shift(x,d,-1),d),-1)
def word_value(word,links,n):
    z=np.eye(n,dtype=complex)
    for e,sgn in word:
        a=links[e]
        z=z@(a if sgn==1 else a.conj().T)
    return z

def cap_checks(n):
    L=3; h=1; A=3.; root=(0,)*4; I=np.eye(n)
    sites=list(itertools.product(range(-h,h+1),repeat=4))
    edges=[(x,d) for x in sites for d in range(4) if x[d]<h]
    tree=set()
    for x in sites:
        if x==root: continue
        d=max(k for k in range(4) if x[k]!=0)
        y=shift(x,d,-(1 if x[d]>0 else -1))
        tree.add((y,d) if x[d]>0 else (x,d))
    plaquettes=[]
    for x in sites:
        for d,e in itertools.combinations(range(4),2):
            if x[d]<h and x[e]<h:
                plaquettes.append([((x,d),1),((shift(x,d,1),e),1),((shift(x,e,1),d),-1),((x,e),-1)])
    record(f'SU{n}:open-block-counts',len(edges)==216 and len(tree)==80 and len(plaquettes)==216,
           links=len(edges),tree=len(tree),plaquettes=len(plaquettes))
    eps=min(.25,1/(32*A),1/(384*A*A),math.pi/(8*n*A))
    generators={e:(np.zeros((n,n),complex) if e in tree else generator(n)) for e in edges}
    def make_small(alpha): return {e:expm(alpha*a) for e,a in generators.items()}
    def curvature(links): return max(op(I-word_value(p,links,n)) for p in plaquettes)
    low,high=0.,eps
    while curvature(make_small(high)) < eps*(1-1e-7): high*=2
    for _ in range(32):
        mid=(low+high)/2
        if curvature(make_small(mid)) < eps*(1-1e-7): low=mid
        else: high=mid
    W=make_small(low)
    gauges={x:(I.astype(complex) if x==root else expm(5*generator(n))) for x in sites}
    U={(x,d):gauges[x].conj().T@W[(x,d)]@gauges[shift(x,d,1)] for x,d in edges}
    reconstructed={root:I.astype(complex)}
    for x in sorted(sites,key=lambda q:sum(abs(a) for a in q)):
        if x==root:continue
        d=max(k for k in range(4) if x[k]!=0);sgn=1 if x[d]>0 else -1
        p=shift(x,d,-sgn);edge=(p,d) if sgn==1 else (x,d)
        reconstructed[x]=reconstructed[p]@(U[edge] if sgn==1 else U[edge].conj().T)
    Wrec={(x,d):reconstructed[x]@U[(x,d)]@reconstructed[shift(x,d,1)].conj().T for x,d in edges}
    a={e:logm(w) for e,w in Wrec.items()}
    recovery=max(op(Wrec[e]-W[e]) for e in edges)
    tree_error=max(op(Wrec[e]-I) for e in tree)
    record(f'SU{n}:gauge-recovery',recovery<2e-10 and tree_error<2e-10,
           recovery=recovery,tree_error=tree_error,cut=eps,initial_curvature=curvature(U))
    norm_max=max(op(w-I) for w in Wrec.values());log_max=max(op(x) for x in a.values())
    record(f'SU{n}:nonabelian-filling',norm_max<=A*eps+2e-10 and log_max<=2*A*eps+2e-10,
           group_norm=norm_max,group_bound=A*eps,log_norm=log_max,log_bound=2*A*eps)
    contractions=[]
    for t in [.25,.5,.75,.99]:
        Wt={e:expm(t*x) for e,x in a.items()}
        actual=curvature(Wt);bound=eps-eps*(1-t)/4
        contractions.append({'t':t,'actual':actual,'bound':bound})
    record(f'SU{n}:simultaneous-radial-contraction',all(q['actual']<=q['bound']+2e-10 for q in contractions),cases=contractions)
    r=eps/128;t=1-32*r/eps
    centre={(x,d):reconstructed[x].conj().T@expm(t*a[(x,d)])@reconstructed[shift(x,d,1)] for x,d in edges}
    cap={e:expm(.95*r*generator(n))@v for e,v in centre.items()}
    centre_defect=curvature(centre);cap_defect=curvature(cap)
    # Ambient HS chord is <= shortest-group distance; this fixture's distance
    # is evaluated through a small principal logarithm, not a chord surrogate.
    max_distance=max(hs(logm(U[e]@centre[e].conj().T)) for e in edges)
    record(f'SU{n}:original-product-cap',centre_defect<=eps-8*r+2e-10 and cap_defect<=eps-3*r+2e-10 and max_distance<=64*math.sqrt(n)*A*r+2e-10,
           centre_defect=centre_defect,cap_defect=cap_defect,epsilon=eps,r=r,max_distance=max_distance,claimed_distance=64*math.sqrt(n)*A*r)
    mutated={e:expm(.5*logm(v)) for e,v in U.items()}
    mut_curv=curvature(mutated)
    record(f'SU{n}:ungauged-log-mutation',mut_curv>eps+1e-6,curvature=mut_curv,cut=eps)


def incidence_checks():
    L=3;T=2;M=L*T;h=1
    def step(x,d,s):
        y=list(x);y[d]=(y[d]+s)%M;return tuple(y)
    def path(start,delta,order):
        x=start;answer=[]
        for d in order:
            s=1 if delta[d]>=0 else -1
            for _ in range(abs(delta[d])):
                y=step(x,d,s);answer.append(((x,d),1) if s==1 else ((y,d),-1));x=y
        return answer
    def block(x): return tuple(((a+h)//L)%T for a in x)
    all_edges=[(x,d) for x in itertools.product(range(M),repeat=4) for d in range(4)]
    counts={e:{} for e in all_edges}
    crossing_multiplicity_max=0
    labels=list(itertools.product(range(T),repeat=4))
    for X in labels:
        root=tuple(L*a for a in X)
        for d in range(4):
            nextroot=step(root,d,L);label=(X,d)
            for delta in itertools.product(range(-h,h+1),repeat=4):
                y=tuple((a+b)%M for a,b in zip(root,delta))
                for order in itertools.permutations(range(4)):
                    start=path(root,delta,order)
                    line=path(y,tuple(L if k==d else 0 for k in range(4)),[d])
                    end=[(edge,-s) for edge,s in reversed(path(nextroot,delta,order))]
                    occurrences={}
                    for edge,s in start+line+end: occurrences[edge]=occurrences.get(edge,0)+1
                    for edge,k in occurrences.items():
                        counts[edge][label]=counts[edge].get(label,0)+k
                        if block(edge[0])!=block(step(edge[0],edge[1],1)):
                            crossing_multiplicity_max=max(crossing_multiplicity_max,k)
    crossings=[];internal_errors=[]
    for edge,readers in counts.items():
        x,d=edge;X=block(x);Y=block(step(x,d,1))
        if X!=Y:
            crossings.append((edge,readers))
        else:
            for (Z,nu),count in readers.items():
                ZZ=list(Z);ZZ[nu]=(ZZ[nu]+1)%T
                if X not in [Z,tuple(ZZ)]:internal_errors.append([edge,Z,nu])
            if len(readers)>8:internal_errors.append([edge,len(readers)])
    bad=[(e,r) for e,r in crossings if len(r)!=1 or list(r.values())!=[72] or list(r.keys())!=[(block(e[0]),e[1])]]
    record('literal-paired-contours:all-crossing-readers',not bad and crossing_multiplicity_max==1,
           crossing_edges=len(crossings),bad_count=len(bad),occurrences_per_reader=72,words_per_kernel=24*L**4,max_multiplicity=crossing_multiplicity_max,seam_and_direction_coverage='every positive crossing edge, including all periodic block faces')
    record('literal-paired-contours:internal-reader-scope',not internal_errors,
           internal_edges=len(all_edges)-len(crossings),errors=len(internal_errors),max_kernel_readers=max(len(r) for e,r in counts.items() if block(e[0])==block(step(e[0],e[1],1))))
    pcounts={e:0 for e in all_edges}
    for x in itertools.product(range(M),repeat=4):
        for d,e in itertools.combinations(range(4),2):
            word=[(x,d),(step(x,d,1),e),(step(x,e,1),d),(x,e)]
            for edge in set(word):pcounts[edge]+=1
    record('periodic-plaquettes:six-per-link',all(v==6 for v in pcounts.values()),edge_count=len(pcounts),minimum=min(pcounts.values()),maximum=max(pcounts.values()))


def compact_kernel_checks():
    # Unit SU(2) quaternions cover S^3. x0=cos(theta) has Haar density
    # 2/pi sin(theta)^2; the direction x1/cos(theta complement) is uniform.
    z,w=roots_legendre(180);theta=(z+1)*math.pi/2;wtheta=w*math.pi/2
    c,v=roots_legendre(140)
    q0=np.cos(theta)[:,None]+np.zeros((len(theta),len(c)))
    q1=np.sin(theta)[:,None]*c[None,:]
    weights=(2/math.pi)*wtheta[:,None]*np.sin(theta)[:,None]**2*v[None,:]/2
    m=np.array([.62,.27]);dm=np.array([-.11,.39]);vcoarse=np.array([math.cos(.8),math.sin(.8)])
    radius=float(np.linalg.norm(m));dr=float(m@dm/radius)
    unnormalized_gap=[];cases=[]
    for t in [.5,3.,20.]:
        exponent=t*(q0*m[0]+q1*m[1]);density=weights*np.exp(exponent)
        Z=float(density.sum());moment=float((density*(q0*dm[0]+q1*dm[1])).sum()/Z)
        by_integral=t*(float(vcoarse@dm)-moment)
        # For uniform S^3: Z=2 I1(t|M|)/(t|M|), d log Z/d|M|=t I2/I1.
        analytic=t*float(vcoarse@dm)-t*iv(2,t*radius)/iv(1,t*radius)*dr
        bound=2*t*float(np.linalg.norm(dm))
        cases.append({'t':t,'quadrature_derivative':by_integral,'bessel_derivative':float(analytic),'absolute_error':abs(by_integral-analytic),'CC4_bound':bound,'normalizer_derivative':t*moment,'normalizer':Z,'analytic_normalizer':2*float(iv(1,t*radius))/(t*radius)})
        unnormalized_gap.append(abs(t*float(vcoarse@dm)-by_integral))
    record('compact-normalizer:full-Haar-derivative',all(c['absolute_error']<3e-7 and abs(c['quadrature_derivative'])<=c['CC4_bound']+3e-7 for c in cases),cases=cases)
    record('compact-normalizer:omission-mutation',max(unnormalized_gap)>1e-3,derivative_gaps=unnormalized_gap)
    # The SU(2) bi-invariant HS metric is the round S^3 metric scaled by sqrt2.
    # Total volume=2*pi^2*(sqrt2)^3. Lebesgue su(2) unit ball volume=4*pi/3.
    hN=1/(4*math.sqrt(2)*math.pi**2);rH=1.
    cH=hN*(math.sin(rH)/rH)**2*(4*math.pi/3)
    caps=[]
    for r in [.01,.1,.5]:
        theta=r/math.sqrt(2)
        mass=(theta-.5*math.sin(2*theta))/math.pi
        lower=cH*r**3
        caps.append({'HS_radius':r,'actual_mass':mass,'lower_bound':lower,'ratio':mass/lower})
    record('SU2-Haar:cap-volume',all(c['actual_mass']>=c['lower_bound'] for c in caps),cases=caps,cH=cH)
    theta=.1/math.sqrt(2);flat_angle_mass=theta/math.pi;actual=(theta-.5*math.sin(2*theta))/math.pi
    record('SU2-Haar:flat-angle-mutation',flat_angle_mass/actual>2,ratio=flat_angle_mass/actual)

for n in [3,4]:cap_checks(n)
incidence_checks()
compact_kernel_checks()
summary={'scope':'finite falsification only; no uniform theorem or continuum/gap conclusion','seed':93471062,'checks':results,'passed':sum(x['pass'] for x in results),'failed':sum(not x['pass'] for x in results),'elapsed_seconds':time.monotonic()-START,'maxrss_raw':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'thread_environment':{k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']}}
print(json.dumps(summary,indent=2))
raise SystemExit(1 if summary['failed'] else 0)
