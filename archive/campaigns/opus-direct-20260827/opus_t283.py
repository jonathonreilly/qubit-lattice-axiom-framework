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
# ---- corrected analysis (T282 omitted the constant offset a) ----
# The weight is phi(rho,rho') = a + sum lam_a S^a c c'.  For pure states
# Tr(rho rho') = 1/4 + (1/4) c.c', so the Born point is (lam_B, a = 1/4) and
# min phi_Born = min |<z|w>|^2 = 0, attained EXACTLY on orthogonal pairs.
# Test (i) is therefore trivial; the content is test (ii), and the minimum lives
# on the orthogonal set, so that set must be IN the sample.
lam=Vt2[-1][:6].real.copy()
phiB=V@lam
if np.dot(phiB,TR-0.25)<0: lam=-lam
sc=np.dot(V@lam,TR-0.25)/np.dot(V@lam,V@lam); lam=lam*sc
print(f"\nnormalised so V.lam == Tr - 1/4 :  max resid = {np.max(np.abs(V@lam-(TR-0.25))):.2e}")

# build a sample where the minimum actually lives: orthogonal + near-orthogonal
NS=8000; Vs=[]; TRs=[]
for _ in range(NS):
    z=rng.normal(size=n)+1j*rng.normal(size=n); z/=np.linalg.norm(z)
    w=rng.normal(size=n)+1j*rng.normal(size=n)
    w=w-(z.conj()@w)*z; w/=np.linalg.norm(w)                  # exactly orthogonal
    if rng.random()<0.5:                                      # and near-orthogonal
        u=rng.normal(size=n)+1j*rng.normal(size=n); u/=np.linalg.norm(u)
        w=w+0.05*u; w/=np.linalg.norm(w)
    r1=np.outer(z,z.conj()); r2=np.outer(w,w.conj())
    c1,c2=coords(r1),coords(r2)
    Vs.append([c1@S@c2 for S in forms]); TRs.append(np.real(np.trace(r1@r2)))
Vs=np.array(Vs); TRs=np.array(TRs)
Vall=np.vstack([V,Vs]); TRall=np.concatenate([TR,TRs])
a=0.25
print(f"(i) min phi_Born over {len(Vall)} pairs (orthogonal set included) = "
      f"{(a+Vall@lam).min():.3e}   (0 => on the boundary, attained)")

Q,_=np.linalg.qr(np.column_stack([lam,np.eye(6)])[:, :6])
print("\n(ii) perturb lam along each transverse direction at fixed a = 1/4:")
print("     dir    eps=+1e-3        eps=-1e-3       both negative?")
allneg=True
for j in range(1,6):
    t=Q[:,j]; mns=[(a+Vall@(lam+e*t)).min() for e in (1e-3,-1e-3)]
    ok=mns[0]<-1e-12 and mns[1]<-1e-12; allneg&=ok
    print(f"      {j-1}    {mns[0]:+.4e}     {mns[1]:+.4e}     {'YES' if ok else 'NO'}")
print(f"\n  R148's open item: Born point on the boundary of the FULL 6-dim "
      f"positivity region -> {'YES' if allneg else 'NOT ESTABLISHED'}")
print("\n  control: the same perturbation must NOT push it negative if applied")
print("  along the Born direction itself with eps>0 (that only raises the weight):")
for e in (1e-3,-1e-3):
    print(f"    eps={e:+.0e} along lam_Born : min = {(a+Vall@(lam*(1+e))).min():+.4e}")
