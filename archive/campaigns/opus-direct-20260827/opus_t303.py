"""
T282 - R148's own open scope item: is the Born point on the boundary of the
FULL six-dimensional positivity region at M4(C)?

R148 verified the Born form is the unique member of R147's six-parameter family
constant (=vanishing) on orthogonal pairs, and that WITHIN the isotropic line
the vanishing point is the positivity boundary. It explicitly left open:
"Whether it lies on the boundary of the full six-dimensional positivity region
is not checked here."

Setup (R147/T230): the covariance group is the lattice's proper rotations
lifted to spin (hyperoctahedral in 4 dims), NOT SU(4) -- which is why the
invariant symmetric forms number six, not one.

The weight for parameters (lam, a) is  phi(rho,rho') = a + sum_ab lam_a S^a c c'.
Positivity region P = { (lam,a) : phi >= 0 on all pure pairs }.  A point is on
the BOUNDARY iff inf_pairs phi = 0 -- i.e. the weight is non-negative and
actually attains zero.  So the test is:
    (i)  min over pure pairs of phi_Born  == 0   (attained, not just >= 0)
    (ii) every neighbourhood of the Born point contains a lam with min < 0
Test (ii) directly: perturb the Born direction by each of the 5 transverse
basis directions, both signs, and check the minimum goes negative.
"""
import numpy as np, itertools
n=4
def gens(n):
    B=[]
    for i in range(n):
        for j in range(i+1,n):
            E=np.zeros((n,n),dtype=complex); E[i,j]=1; E[j,i]=1; B.append(E/np.sqrt(2))
            F=np.zeros((n,n),dtype=complex); F[i,j]=-1j; F[j,i]=1j; B.append(F/np.sqrt(2))
    for k in range(1,n):
        d=np.zeros(n); d[:k]=1; d[k]=-k
        B.append(np.diag(d).astype(complex)/np.sqrt(k*k+k))
    return B
T=gens(n); m=len(T)
def hyperoct(d):
    out=[]
    for perm in itertools.permutations(range(d)):
        for sg in itertools.product([1,-1],repeat=d):
            R=np.zeros((d,d))
            for i,p in enumerate(perm): R[i,p]=sg[i]
            if abs(np.linalg.det(R)-1)<1e-12: out.append(R)
    return out
I2=np.eye(2,dtype=complex)
SX=np.array([[0,1],[1,0]],dtype=complex); SY=np.array([[0,-1j],[1j,0]],dtype=complex)
SZ=np.array([[1,0],[0,-1]],dtype=complex)
GAM=[np.kron(SX,I2),np.kron(SY,I2),np.kron(SZ,SX),np.kron(SZ,SY)]
def spin_U(R):
    rows=[]
    for mu in range(4):
        tgt=sum(R[nu,mu]*GAM[nu] for nu in range(4))
        rows.append(np.kron(np.eye(4),GAM[mu].T)-np.kron(tgt,np.eye(4)))
    A=np.vstack(rows); _,sv,Vt=np.linalg.svd(A,full_matrices=False)
    return Vt[-1].conj().reshape(4,4)
Os=[]
for R in hyperoct(4):
    U=spin_U(R); Ui=np.linalg.inv(U); O=np.zeros((m,m))
    for j,Bj in enumerate(T):
        X=U@Bj@Ui
        for i,Bi in enumerate(T): O[i,j]=np.real(np.trace(Bi.conj().T@X))
    Os.append(O)
idx=[(i,j) for i in range(m) for j in range(i,m)]
rows=[]
for O in Os:
    for a,(i,j) in enumerate(idx):
        r=np.zeros(len(idx))
        for b,(k,l) in enumerate(idx):
            r[b]+=O[k,i]*O[l,j]+(O[l,i]*O[k,j] if k!=l else 0.0)
        r[a]-=1.0; rows.append(r)
A=np.array(rows); _,sv,Vt=np.linalg.svd(A,full_matrices=False)
K=int(np.sum(sv<=max(A.shape)*np.finfo(float).eps*sv.max()))
forms=[]
for t in range(K):
    v=Vt[len(Vt)-K+t]; S=np.zeros((m,m))
    for b,(k,l) in enumerate(idx):
        S[k,l]+=v[b]
        if k!=l: S[l,k]+=v[b]
    forms.append(S)
print(f"invariant symmetric forms: {len(forms)} (expect 6)")

rng=np.random.default_rng(3)
def coords(r): return np.array([np.real(np.trace(t.conj().T@r)) for t in T])
NP=20000
C1=np.zeros((NP,m)); C2=np.zeros((NP,m)); TR=np.zeros(NP)
for i in range(NP):
    z=rng.normal(size=n)+1j*rng.normal(size=n); z/=np.linalg.norm(z)
    w=rng.normal(size=n)+1j*rng.normal(size=n); w/=np.linalg.norm(w)
    r1=np.outer(z,z.conj()); r2=np.outer(w,w.conj())
    C1[i]=coords(r1); C2[i]=coords(r2); TR[i]=np.real(np.trace(r1@r2))
# value of each basis form on every pair
V=np.array([[C1[i]@S@C2[i] for S in forms] for i in range(NP)])   # (NP, 6)

# the Born direction: the one constant on orthogonal pairs (R148)
ortho=[]
for _ in range(600):
    z=rng.normal(size=n)+1j*rng.normal(size=n); z/=np.linalg.norm(z)
    w=rng.normal(size=n)+1j*rng.normal(size=n); w-= (z.conj()@w)*z; w/=np.linalg.norm(w)
    r1=np.outer(z,z.conj()); r2=np.outer(w,w.conj())
    c1,c2=coords(r1),coords(r2)
    ortho.append([c1@S@c2 for S in forms])
Vo=np.array(ortho); Aug=np.hstack([Vo,-np.ones((len(Vo),1))])
_,s2,Vt2=np.linalg.svd(Aug,full_matrices=False)
kk=int(np.sum(s2<=max(Aug.shape)*np.finfo(float).eps*s2.max()))
lam=Vt2[-1][:6].real.copy(); mu=Vt2[-1][6].real
print(f"dim{{constant on orthogonal pairs}} = {kk} (expect 1)")
# ---- T303: how many VERTICES does the 6-dim positivity region have? ----
# T284/T298 scanned only the radial line through the Born direction, plus
# transverse balls around it. That found two apexes. But the region is
# 6-dimensional and could have vertices OFF that line -- each of which would be
# another canonically distinguished candidate rule, and R193 tested only two.
#
# Find them by linear programming: maximise many random linear functionals
# c.lambda over { lambda : a + V lambda >= 0 }. Every optimum is on the boundary;
# vertices recur across objectives, faces do not. Cluster the optima.
import numpy as np
from scipy.optimize import linprog
lam=Vt2[-1][:6].real.copy()
if np.dot(V@lam,TR-0.25)<0: lam=-lam
lam=lam*(np.dot(V@lam,TR-0.25)/np.dot(V@lam,V@lam))     # V.lam == Tr - 1/4
rng2=np.random.default_rng(17)
rows=[]
for _ in range(12000):
    z=rng2.normal(size=n)+1j*rng2.normal(size=n); z/=np.linalg.norm(z)
    r=rng2.random()
    if r<0.35: w=rng2.normal(size=n)+1j*rng2.normal(size=n); w=w-(z.conj()@w)*z
    elif r<0.70: w=z+0.03*(rng2.normal(size=n)+1j*rng2.normal(size=n))
    else: w=rng2.normal(size=n)+1j*rng2.normal(size=n)
    w/=np.linalg.norm(w)
    r1=np.outer(z,z.conj()); r2=np.outer(w,w.conj())
    c1,c2=coords(r1),coords(r2)
    rows.append([c1@S@c2 for S in forms])
Vc=np.vstack([V,np.array(rows)]); a=0.25
print(f"\nLP over {Vc.shape[0]} pure-pair constraints, a = 1/4 fixed.")
opt=[]
for t in range(400):
    obj=rng2.normal(size=6); obj/=np.linalg.norm(obj)
    r=linprog(-obj, A_ub=-Vc, b_ub=np.full(Vc.shape[0],a), bounds=[(-50,50)]*6, method="highs")
    if r.status==0: opt.append(r.x)
opt=np.array(opt); print(f"  {len(opt)}/400 LPs solved")
# cluster
keep=[]
for x in opt:
    if not any(np.linalg.norm(x-y)<1e-4 for y in keep): keep.append(x)
print(f"  distinct optima (tol 1e-4): {len(keep)}")
# how many are VERTICES: at a vertex all 6 directions exit immediately
def is_vertex(x,eps=1e-4):
    Q,_=np.linalg.qr(np.column_stack([x if np.linalg.norm(x)>1e-9 else np.eye(6)[0],np.eye(6)])[:, :6])
    dirs=[Q[:,j] for j in range(6)]
    return all((a+Vc@(x+s*eps*u)).min()<-1e-12 for u in dirs for s in (1,-1))
verts=[x for x in keep if is_vertex(x)]
print(f"  of which VERTICES (every direction exits): {len(verts)}")
if verts:
    print("\n  vertex   |lam|    overlap with Born direction   phi on orthogonal pairs")
    ub=lam/np.linalg.norm(lam)
    orth=np.abs(np.array([r for r in rows])) # placeholder
    for i,x in enumerate(verts[:12]):
        ov=float(x@ub/np.linalg.norm(x))
        # value of phi on exactly-orthogonal pairs: use the first 35% of rows
        print(f"    {i}     {np.linalg.norm(x):7.4f}      {ov:+.6f}")
    print(f"\n  Born direction itself: |lam| = {np.linalg.norm(lam):.4f}, overlap +1.000000")
    print(f"  anti-Born (-1/3 lam):  |lam| = {np.linalg.norm(lam)/3:.4f}, overlap -1.000000")
