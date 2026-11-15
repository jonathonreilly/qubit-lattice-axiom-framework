# B6 (supported couplings exist), B7 (unique min-cost max-entropy coupling), B8 (copy criterion), B11 (Hadamard bound), support factorization.
import numpy as np, itertools
from scipy.optimize import linprog, minimize
from scipy.linalg import expm, block_diag
from functools import reduce
rng=np.random.default_rng(11)
def randU(n):
    q,r=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))); return q*(np.diag(r)/abs(np.diag(r)))
def randrho(n,rank=None):
    a=rng.normal(size=(n,rank or n))+1j*rng.normal(size=(n,rank or n)); r=a@a.conj().T; return r/np.trace(r).real
print("--- B6: random block-sparse unitaries, projectors of rank>1, random (also low-rank) states; LP feasibility of supported coupling")
nfeas=0; ntot=0; nsparse=0
for trial in range(300):
    # resolution of identity: ranks
    ranks=list(rng.integers(1,4,size=rng.integers(3,6))); n=sum(ranks)
    # block-sparse W: direct sum of unitaries over random groupings of basis vectors, then permute outputs within groups only
    perm=rng.permutation(n); cuts=sorted(rng.choice(range(1,n),size=min(2,n-1),replace=False)); groups=np.split(perm,cuts)
    W=np.zeros((n,n),complex)
    for g in groups: W[np.ix_(g,g)]=randU(len(g))
    off=np.cumsum([0]+ranks); Ps=[np.diag([1.0 if off[k]<=i<off[k+1] else 0 for i in range(n)]) for k in range(len(ranks))]
    rho=randrho(n,rank=int(rng.integers(1,n+1)))
    m=len(Ps); p=np.array([np.trace(P@rho).real for P in Ps]); pp=np.array([np.trace(P@W@rho@W.conj().T).real for P in Ps])
    allowed=np.array([[np.abs(Ps[z]@W@Ps[x]).max()>1e-12 for z in range(m)] for x in range(m)])   # [input x, output z]
    if not allowed.all(): nsparse+=1
    # LP: gamma[x,z]>=0, zero where not allowed, marginals p, pp
    Aeq=[];beq=[]
    for x in range(m):
        r=np.zeros((m,m)); r[x,:]=1; Aeq.append(r.ravel()); beq.append(p[x])
    for z in range(m):
        r=np.zeros((m,m)); r[:,z]=1; Aeq.append(r.ravel()); beq.append(pp[z])
    bounds=[(0,None) if allowed[x,z] else (0,0) for x in range(m) for z in range(m)]
    res=linprog(np.zeros(m*m),A_eq=np.array(Aeq),b_eq=np.array(beq),bounds=bounds,method="highs")
    ntot+=1; nfeas+= res.status==0
print(f"feasible {nfeas}/{ntot}; instances with at least one forbidden block: {nsparse}")
# control: replace p' by a wrong output distribution (uniform) -> infeasible often
ninf=0
for trial in range(100):
    n=6; W=block_diag(randU(2),randU(4)); rho=np.diag([0.5,0.5,0,0,0,0]).astype(complex)
    p=rho.diagonal().real; pp=np.ones(6)/6
    allowed=abs(W.T)>1e-12
    Aeq=[];beq=[]
    for x in range(6):
        r=np.zeros((6,6)); r[x,:]=1; Aeq.append(r.ravel()); beq.append(p[x])
    for z in range(6):
        r=np.zeros((6,6)); r[:,z]=1; Aeq.append(r.ravel()); beq.append(pp[z])
    res=linprog(np.zeros(36),A_eq=np.array(Aeq),b_eq=np.array(beq),bounds=[(0,None) if allowed[x,z] else (0,0) for x in range(6) for z in range(6)],method="highs")
    ninf+= res.status!=0
print("control (non-Born output marginal): infeasible in",ninf,"/100")
print("--- B7: uniqueness of min-cost then max-entropy coupling on a small instance (two random starts agree)")
def fermions(n):
    a=np.array([[0,1],[0,0]],complex); Z=np.diag([1,-1]).astype(complex); I=np.eye(2)
    return [reduce(np.kron,[Z]*k+[a]+[I]*(n-k-1)) for k in range(n)]
nm=3; c=fermions(nm); ns=[x.conj().T@x for x in c]
h=sum((c[i+1].conj().T@c[i]+c[i].conj().T@c[i+1]) for i in range(nm-1))   # number conserving even hop "gate"
W=expm(-0.9j*h)
confs=list(itertools.product((0,1),repeat=nm))
def proj(s): return reduce(lambda a,b:a@b,[ns[i] if s[i] else np.eye(2**nm)-ns[i] for i in range(nm)])
Ps=[proj(s) for s in confs]
psi=rng.normal(size=8)+1j*rng.normal(size=8); psi/=np.linalg.norm(psi)
P=reduce(lambda a,b:a@b,[np.eye(8)-2*n for n in ns]); rho=np.outer(psi,psi.conj()); rho=(rho+P@rho@P)/2   # even state
p=np.array([np.trace(Q@rho).real for Q in Ps]); pp=np.array([np.trace(Q@W@rho@W.conj().T).real for Q in Ps])
m=8; allowed=np.array([[abs(Ps[z]@W@Ps[x]).max()>1e-12 for z in range(m)] for x in range(m)])
print("allowed pairs:",int(allowed.sum()),"of 64 (number conservation forbids the rest:",all(sum(confs[x])==sum(confs[z]) for x in range(m) for z in range(m) if allowed[x,z]),")")
cost=np.array([[sum(a!=b for a,b in zip(confs[x],confs[z])) for z in range(m)] for x in range(m)],float)
Aeq=[];beq=[]
for x in range(m):
    r=np.zeros((m,m)); r[x,:]=1; Aeq.append(r.ravel()); beq.append(p[x])
for z in range(m):
    r=np.zeros((m,m)); r[:,z]=1; Aeq.append(r.ravel()); beq.append(pp[z])
bounds=[(0,None) if allowed[x,z] else (0,0) for x in range(m) for z in range(m)]
lp=linprog(cost.ravel(),A_eq=np.array(Aeq),b_eq=np.array(beq),bounds=bounds,method="highs"); cmin=lp.fun
print("min cost:",cmin)
idxs=[k for k,b in enumerate(bounds) if b[1] is None]
A=np.array(Aeq)[:,idxs]; b=np.array(beq); cvec=cost.ravel()[idxs]
def negH(g): g=np.clip(g,1e-300,None); return float((g*np.log(g)).sum())
sols=[]
for st in range(3):
    g0=np.abs(lp.x[idxs]+0.01*rng.random(len(idxs)))
    cons=[{'type':'eq','fun':lambda g:A@g-b},{'type':'eq','fun':lambda g:cvec@g-cmin}]
    r=minimize(negH,g0,constraints=cons,bounds=[(0,1)]*len(idxs),method='SLSQP',options={'maxiter':2000,'ftol':1e-14})
    sols.append(r.x)
print("max difference between optimizers from 3 starts:",max(abs(sols[0]-s).max() for s in sols[1:])," entropies:",[round(-negH(s),8) for s in sols])
print("--- support factorization: two disjoint 'cubes' (2 modes each), blocks of the product gate")
c=fermions(4); ns=[x.conj().T@x for x in c]
def gate(i,j,t): 
    hh=c[j].conj().T@c[i]+c[i].conj().T@c[j]; return expm(-1j*t*hh)
W=gate(0,1,0.7)@gate(2,3,np.pi/2)   # second gate is a full swap up to phase -> has zero blocks
confs=list(itertools.product((0,1),repeat=4))
def proj4(s): return reduce(lambda a,b:a@b,[ns[i] if s[i] else np.eye(16)-ns[i] for i in range(4)])
def blk(Wm,sites,z,x):
    Pz=reduce(lambda a,b:a@b,[ns[i] if z[k] else np.eye(16)-ns[i] for k,i in enumerate(sites)])
    Px=reduce(lambda a,b:a@b,[ns[i] if x[k] else np.eye(16)-ns[i] for k,i in enumerate(sites)])
    return abs(Pz@Wm@Px).max()>1e-12
ok=True
for x in confs:
    for z in confs:
        full=abs(proj4(z)@W@proj4(x)).max()>1e-12
        fact=blk(gate(0,1,0.7),(0,1),z[:2],x[:2]) and blk(gate(2,3,np.pi/2),(2,3),z[2:],x[2:])
        ok&= (full==fact)
print("support of product gate = product of supports:",ok)
print("--- B8: quasi-free states on 4 modes, omega(D_xy) vs formula; criterion")
c=fermions(4); ns=[x.conj().T@x for x in c]
def quasi_free(G):
    # density matrix with omega(c_y^dag c_x)=G_xy, via eigenmodes of G (works also for eigenvalues 0,1)
    lam,U=np.linalg.eigh(G); rho=np.eye(16,dtype=complex)
    for k in range(4):
        a=sum(U[x,k].conj()*c[x] for x in range(4)); nk=a.conj().T@a
        rho=rho@(lam[k]*nk+(1-lam[k])*(np.eye(16)-nk))
    return rho
maxerr=0; maxwick=0
for t in range(200):
    lam=rng.random(4); 
    if t%3==0: lam=np.round(lam)       # projections
    if t%3==1: lam[:2]=np.round(lam[:2])
    U=randU(4)
    if t%5==0: U=block_diag(randU(1),randU(1),randU(2))   # decoupled sites: G_01 = 0 with G_00,G_11 in {0,1} possible
    G=(U*lam)@U.conj().T; rho=quasi_free(G)
    chk=max(abs(np.trace(rho@c[y].conj().T@c[x])-G[x,y]) for x in range(4) for y in range(4)); assert chk<1e-10
    for x,y in itertools.combinations(range(4),2):
        Dv=np.trace(rho@(ns[x]-ns[y])@(ns[x]-ns[y])).real
        f=G[x,x].real*(1-G[y,y].real)+G[y,y].real*(1-G[x,x].real)+2*abs(G[x,y])**2
        maxerr=max(maxerr,abs(Dv-f))
        crit=abs(G[x,y])<1e-9 and ((abs(G[x,x])<1e-9 and abs(G[y,y])<1e-9) or (abs(G[x,x]-1)<1e-9 and abs(G[y,y]-1)<1e-9))
        assert (abs(Dv)<1e-12)==crit,(Dv,G[x,x],G[y,y],G[x,y])
    for F in [(0,1),(0,2,3),(0,1,2,3)]:
        pr=np.trace(rho@reduce(lambda a,b:a@b,[ns[i] for i in F])).real
        GF=G[np.ix_(F,F)]; maxwick=max(maxwick,abs(pr-np.linalg.det(GF).real)); assert pr<=np.prod([G[i,i].real for i in F])+1e-12
print("max |omega(D)-formula|:",maxerr," max |P(all occupied on F)-det G_F|:",maxwick," Hadamard bound held in all cases; criterion equivalence held in all cases")
