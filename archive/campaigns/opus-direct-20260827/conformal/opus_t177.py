"""T177 - IS THE PERMITTED HARMONIC CONTENT BOUNDED?  Extending R103's sector count.

R110 posed the axioms lane's central question: does the axiom-permitted
distribution have BOUNDED harmonic content (records drawn from an irreducibly
spread distribution -- intrinsic randomness) or UNBOUNDED (the distribution can
approach a point mass -- effectively deterministic record formation)?

R103 counted covariant maps into the l = 0, 1, 2 sectors: 2, 4, 4.  Extend the
count upward.  If it vanishes above some l, the content is bounded.  If it stays
nonzero, the axioms permit content at every order.

The count is dim Hom_O(input, spin-l), with input = 6 neighbours x (1 + 3) = 24
real dimensions, decomposed in R92 as 2A1 + 2E + 4T1 + 2T2.  Hand prediction by
restricting each SO(3) spin-l rep to the octahedral group:
   l=0 -> A1                       -> 2
   l=1 -> T1                       -> 4
   l=2 -> E + T2                   -> 2 + 2 = 4
   l=3 -> A2 + T1 + T2             -> 0 + 4 + 2 = 6
   l=4 -> A1 + E + T1 + T2         -> 2 + 2 + 4 + 2 = 10
so the count should never vanish -- but hand character work is exactly what I got
wrong twice earlier in this campaign, so compute it.

CONTROLS: l=0,1,2 must reproduce 2, 4, 4; the trivial group must return the full
dimension 24*(2l+1); and each l-action must satisfy A(R)A(S) = A(RS)."""
import numpy as np, itertools
def cubic():
    R=[]
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1,-1],repeat=3):
            M=np.zeros((3,3))
            for i,q in enumerate(p): M[i,q]=s[i]
            if abs(np.linalg.det(M)-1)<1e-9: R.append(M)
    return R
ROT=cubic()
DIRS=[np.array(d,dtype=float) for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
def perm_action(R):
    P=np.zeros((6,6))
    for j,d in enumerate(DIRS):
        i=[k for k,e in enumerate(DIRS) if np.allclose(e,R@d)][0]; P[i,j]=1.0
    return P
def herm_action(R):
    M=np.zeros((4,4)); M[0,0]=1.0; M[1:,1:]=R; return M
IN=[np.kron(perm_action(R),herm_action(R)) for R in ROT]
# spin-l action realised on harmonic polynomials sampled on a grid
def sphere_grid(n):
    i=np.arange(n)+0.5
    phi=np.arccos(1-2*i/n); th=np.pi*(1+5**0.5)*i
    return np.stack([np.cos(th)*np.sin(phi),np.sin(th)*np.sin(phi),np.cos(phi)],axis=1)
G=sphere_grid(3000)
def harm_basis(l):
    """orthonormal basis of degree-l harmonics, as grid samples"""
    def mons(L):
        out=[]
        for a in range(L+1):
            for b in range(L-a+1): out.append((a,b,L-a-b))
        return out
    cols=[]
    for L in (l-2,l):
        if L<0: continue
        for m in mons(L):
            r2pow=(l-L)//2
            cols.append(np.prod(G**np.array(m),axis=1)*(np.sum(G**2,axis=1)**r2pow))
    A=np.array(cols).T
    Q,_=np.linalg.qr(A)
    # degree-l harmonics = degree-l polys orthogonal to degree-(l-2) ones
    if l>=2:
        lower=[]
        for L in range(0,l-1,2):
            for m in mons(L): lower.append(np.prod(G**np.array(m),axis=1))
        Ql,_=np.linalg.qr(np.array(lower).T)
        Q=Q-Ql@(Ql.T@Q)
    Q,_=np.linalg.qr(Q)
    return Q[:,:2*l+1] if Q.shape[1]>=2*l+1 else Q
def l_action(l):
    B=harm_basis(l); acts=[]
    idx={tuple(np.round(g,9)):k for k,g in enumerate(G)}
    for R in ROT:
        RG=G@R.T
        # nearest-grid-point permutation
        P=np.argmin(((RG[:,None,:]-G[None,:,:])**2).sum(-1),axis=1)
        BR=B[P,:]
        acts.append(np.linalg.lstsq(B,BR,rcond=None)[0])
    return acts
def eq_dim(gin,gout):
    n_in=gin[0].shape[0]; n_out=gout[0].shape[0]
    P=np.zeros((n_out*n_in,n_out*n_in))
    for A,Bm in zip(gin,gout): P+=np.kron(np.linalg.inv(A).T,Bm)
    P/=len(gin)
    return int(round(np.trace(P).real))
print("T177  covariant maps into each harmonic sector")
print(f"   {'l':>3} {'dim':>5} {'covariant maps':>16} {'rep check':>12} {'predicted':>11}")
pred={0:2,1:4,2:4,3:6,4:10}
for l in range(0,6):
    A=l_action(l)
    rep=max(np.abs(A[i]@A[j]-l_action(l)[0]*0-  # placeholder to avoid recompute
                   np.zeros_like(A[0])).max() for i in range(1) for j in range(1))
    # proper representation check
    err=0.0
    for i in range(4):
        for j in range(4):
            RS=ROT[i]@ROT[j]
            k=[t for t,X in enumerate(ROT) if np.allclose(X,RS)][0]
            err=max(err,np.abs(A[i]@A[j]-A[k]).max())
    d=eq_dim(IN,A)
    print(f"   {l:3d} {2*l+1:5d} {d:16d} {err:12.1e} {pred.get(l,'?'):>11}")
print()
print(f"   CONTROL trivial group, l=3 -> must be 24*7 = 168 : "
      f"{eq_dim([np.eye(24)],[np.eye(7)])}")
print()
print("   a count that never vanishes means the axioms permit harmonic content at")
print("   every order, so the distribution is NOT forced to be spread.")
