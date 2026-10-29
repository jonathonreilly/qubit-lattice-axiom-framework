"""Independent matrix-product geometry; no imports from author/predecessor code."""
import itertools as it
import json
import math
import numpy as np
from scipy.linalg import expm, logm

I=np.eye(2,dtype=complex)
pauli=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],dtype=complex)
basis=1j*pauli/math.sqrt(2)
rng=np.random.default_rng(929107)
checks=[]; controls=[]; details={}
def check(name,condition,**data):
    checks.append(dict(name=name,passed=bool(condition),**data))
def control(name,condition,**data):
    controls.append(dict(name=name,rejected=bool(condition),**data))
def norm(a):return float(np.linalg.norm(a,2))
def su2(v):return expm(np.einsum('a,aij->ij',np.asarray(v),basis))
def randgroup():
    q=rng.normal(size=4);q/=np.linalg.norm(q)
    return q[0]*I+1j*np.einsum('a,aij->ij',q[1:],pauli)

def setup(T,L=3):
    n=T*L;h=L//2
    sites=list(it.product(range(n),repeat=4)); coarse=list(it.product(range(T),repeat=4))
    def split(x):
        return tuple(((int(t)+h)//L)%T for t in x),tuple((int(t)+h)%L-h for t in x)
    def plus(x,mu,step=1):
        y=list(x);y[mu]+=step;return tuple(y)
    def ekey(x,mu):return (tuple(int(t)%n for t in x),mu)
    def edge(U,x,mu,sgn=1):
        return U[ekey(x,mu)] if sgn==1 else U[ekey(plus(x,mu,-1),mu)].conj().T
    def steps(x,target,order):
        x=tuple(x);out=[]
        for mu in order:
            while x[mu]!=target[mu]:
                sg=1 if target[mu]>x[mu] else -1;out.append((x,mu,sg));x=plus(x,mu,sg)
        assert x==tuple(target)
        return out
    def path(U,word):
        out=I.copy()
        for x,mu,sg in word:out=out@edge(U,x,mu,sg)
        return out
    def contour(X,mu,off,order):
        root=tuple(L*t for t in X);end=plus(root,mu,L)
        y=tuple(root[j]+off[j] for j in range(4));z=plus(y,mu,L)
        return steps(root,y,order)+steps(y,z,[mu])+steps(z,end,tuple(reversed(order)))
    def plaq(U,x,mu,nu):
        return edge(U,x,mu)@edge(U,plus(x,mu),nu)@edge(U,plus(x,nu),mu,-1 if False else 1).conj().T@edge(U,x,nu).conj().T
    def lift(V):
        out={}
        for x in sites:
            X,r=split(x)
            for mu in range(4):out[(x,mu)]=V[(X,mu)] if r[mu]==h else I
        return out
    return locals()

for T in [2,3]:
    env=setup(T);sites=env['sites'];coarse=env['coarse'];n=env['n'];h=env['h'];split=env['split'];plus=env['plus'];edge=env['edge'];contour=env['contour'];path=env['path'];plaq=env['plaq'];lift=env['lift']
    V={(X,mu):randgroup() for X in coarse for mu in range(4)};U=lift(V)
    fine_error=0.;counts={};flat_count=0;nonflat=0
    for x in sites:
        X,r=split(x)
        for mu,nu in it.combinations(range(4),2):
            actual=plaq(U,x,mu,nu)
            if r[mu]==h and r[nu]==h:
                Xm=tuple(t%T for t in plus(X,mu));Xn=tuple(t%T for t in plus(X,nu))
                expect=V[(X,mu)]@V[(Xm,nu)]@V[(Xn,mu)].conj().T@V[(X,nu)].conj().T
                key=(X,mu,nu);counts[key]=counts.get(key,0)+1;nonflat+=1
            else:expect=I;flat_count+=1
            fine_error=max(fine_error,norm(actual-expect))
    check(f'T{T} all fine plaquettes equal exact face formula',fine_error<2e-11,max_error=fine_error,total=flat_count+nonflat)
    check(f'T{T} each coarse plaquette has L squared copies',set(counts.values())=={9},multiplicities=sorted(set(counts.values())),coarse_count=len(counts))
    chosen=[]
    for mu in range(4):
        chosen.append(((0,0,0,0),mu));X=[0]*4;X[mu]=T-1;chosen.append((tuple(X),mu))
    cerror=0;number=0;pairing_error=0
    for X,mu in chosen:
        for off in it.product(range(-h,h+1),repeat=4):
            for order in it.permutations(range(4)):
                actual=path(U,contour(X,mu,off,order));cerror=max(cerror,norm(actual-V[(X,mu)]));number+=1
    check(f'T{T} actual centered paired contours including all wrap directions',cerror<2e-11,max_error=cerror,contours=number)
    brick_err=0;trivial_err=0;brick_plaquettes=0;brick_edges=0;seam_witness=0
    for X,mu in chosen:
        root=tuple(3*t for t in X)
        ranges=[range(root[j]-h,root[j]+h+1+(3 if j==mu else 0)) for j in range(4)]
        lo=tuple(r.start for r in ranges);hi=tuple(r.stop-1 for r in ranges)
        def g(x):return I if x[mu]<=root[mu]+h else V[(X,mu)]
        for x in it.product(*ranges):
            for nu in range(4):
                y=plus(x,nu)
                if y[nu]<=hi[nu]:
                    trivial_err=max(trivial_err,norm(g(x)@edge(U,x,nu)@g(y).conj().T-I));brick_edges+=1
            for nu,lam in it.combinations(range(4),2):
                if x[nu]<hi[nu] and x[lam]<hi[lam]:
                    brick_err=max(brick_err,norm(plaq(U,x,nu,lam)-I));brick_plaquettes+=1
        if T==2:
            x=list(root);x[mu]=hi[mu];x=tuple(x);y=list(x);y[mu]=lo[mu];y=tuple(y)
            seam_witness=max(seam_witness,norm(g(x)@edge(U,x,mu)@g(y).conj().T-I))
    check(f'T{T} lifted brick flat plaquettes',brick_err<2e-11,max_error=brick_err,plaquettes=brick_plaquettes)
    check(f'T{T} lifted brick gauge trivialization',trivial_err<2e-11,max_error=trivial_err,edges=brick_edges)
    if T==2:control('induced torus far seam incorrectly trivialized with brick gauge',seam_witness>.1,defect=seam_witness)
    angles=[.9,-.7,.4,1.1];F={(X,mu):su2([0,0,angles[mu]]) for X in coarse for mu in range(4)};UF=lift(F)
    flaterr=max(norm(plaq(UF,x,mu,nu)-I) for x in sites for mu,nu in it.combinations(range(4),2))
    hol=max(norm(np.linalg.matrix_power(F[((0,0,0,0),mu)],T)-I) for mu in range(4))
    check(f'T{T} arbitrary large flat holonomy survives the lift',flaterr<2e-11 and hol>.5,curvature=flaterr,holonomy_defect=hol)
    control(f'T{T} replacing coarse holonomies by I changes actual contours',max(norm(F[((0,0,0,0),mu)]-I) for mu in range(4))>.5)

# A complete T=2 relative-chart stress test including a random pinned gauge.
env=setup(2);sites=env['sites'];coarse=env['coarse'];plus=env['plus'];split=env['split'];edge=env['edge'];plaq=env['plaq'];lift=env['lift'];path=env['path'];steps=env['steps'];n=env['n']
V={(X,mu):su2(1e-8*rng.normal(size=3))@su2([0,0,[.8,-.6,.7,.3][mu]]) for X in coarse for mu in range(4)}
U0=lift(V);U={k:su2(1e-9*rng.normal(size=3))@v for k,v in U0.items()}
pg={x:randgroup() for x in sites}
for X in coarse:pg[tuple(3*t for t in X)]=I
Ug={}
for (x,mu),val in U.items():
    y=tuple(t%n for t in plus(x,mu));Ug[(x,mu)]=pg[x]@val@pg[y].conj().T
# Reconstruct tree gauge from oriented tree recursion rather than stored gauge.
g={}
for X in coarse:
    root=tuple(3*t for t in X);g[root]=I
    offs=sorted(it.product([-1,0,1],repeat=4),key=lambda r:sum(abs(t) for t in r))
    for r in offs:
        if not any(r):continue
        j=max(j for j in range(4) if r[j]);sg=1 if r[j]>0 else -1
        rp=list(r);rp[j]-=sg
        parent=tuple(root[k]+rp[k] for k in range(4));child=tuple(root[k]+r[k] for k in range(4))
        gp=g[tuple(t%n for t in parent)]
        g[tuple(t%n for t in child)]=gp@edge(Ug,parent,j,sg)
W={}
for (x,mu),val in Ug.items():
    y=tuple(t%n for t in plus(x,mu));W[(x,mu)]=g[x]@val@g[y].conj().T
maxfine=max(norm(plaq(Ug,x,mu,nu)-I) for x in sites for mu,nu in it.combinations(range(4),2))
eta=0;deltaV=0
for X in coarse:
    root=tuple(3*t for t in X)
    for mu in range(4):eta=max(eta,norm(path(Ug,steps(root,plus(root,mu,3),[mu]))-V[(X,mu)]))
    for mu,nu in it.combinations(range(4),2):
        Xm=tuple(t%2 for t in plus(X,mu));Xn=tuple(t%2 for t in plus(X,nu))
        vp=V[(X,mu)]@V[(Xm,nu)]@V[(Xn,mu)].conj().T@V[(X,nu)].conj().T
        deltaV=max(deltaV,norm(vp-I))
maxrel=0;maxlog=0;maxtrace=0;maxint=0;maxtree=0
for (x,mu),val in W.items():
    X,r=split(x);rel=val@U0[(x,mu)].conj().T;z=logm(rel)
    maxrel=max(maxrel,norm(rel-I));maxlog=max(maxlog,float(np.linalg.norm(z)));maxtrace=max(maxtrace,float(abs(np.trace(z))))
    if r[mu]<1:maxint=max(maxint,norm(val-I))
    y=tuple(t%n for t in plus(x,mu));_,ry=split(y)
    # Test every parent-child tree edge by the child rule.
    for s in [r,ry]:
        if any(s):
            j=max(j for j in range(4) if s[j])
            if j==mu:
                if (s is r and r[mu]<0) or (s is ry and ry[mu]>0):maxtree=max(maxtree,norm(val-I))
check('pinned tree recursion reaches tree identity',maxtree<2e-11,max_error=maxtree)
check('strong-good nonabelian relative-link estimate',maxint<=270*maxfine+2e-11 and maxrel<=270*maxfine+eta+2e-11,relative=maxrel,internal=maxint,bound=270*maxfine+eta)
check('strong-good coarse curvature inequality',deltaV<=9*maxfine+4*eta+2e-11,coarse=deltaV,fine=maxfine,mismatch=eta)
check('relative principal chart includes tested large-holonomy sector',maxtrace<2e-11 and maxlog<2*math.sqrt(2)*(270*maxfine+eta),max_log_HS=maxlog,max_trace=maxtrace)
# The old interior-only cut does not constrain double-face curvature.
Ubad=lift({(X,mu):randgroup() for X in coarse for mu in range(4)})
interior=0;allp=0
for x in sites:
    X,r=split(x)
    for mu,nu in it.combinations(range(4),2):
        d=norm(plaq(Ubad,x,mu,nu)-I);allp=max(allp,d)
        if r[mu]<1 and r[nu]<1:interior=max(interior,d)
control('interior-only cut substituted for all-fine-good',interior<2e-11 and allp>.5,interior=interior,all_plaquettes=allp)
# A nontraceless SU(3) matrix principal logarithm is excluded.
center=np.exp(2j*math.pi/3)*np.eye(3);centerlog=logm(center)
control('principal matrix logarithm without traceless radius guard',abs(np.trace(centerlog))>6 and np.linalg.norm(centerlog)>math.pi/math.sqrt(3),log_norm=float(np.linalg.norm(centerlog)),trace_im=float(np.trace(centerlog).imag))
result={'implementation':'independent centered matrix products, tree recursion and coarse lifts','checks':checks,'controls':controls,'passed':sum(x['passed'] for x in checks),'total':len(checks),'controls_rejected':sum(x['rejected'] for x in controls),'controls_total':len(controls),'limits':'Finite L=3 T=2,3 diagnostics; theorem quantifiers require the analytic proof. No author code imported.'}
print(json.dumps(result,indent=2,allow_nan=False))
assert result['passed']==result['total'] and result['controls_rejected']==result['controls_total']
