"""T177b - the sector count, with an EXACT spin-l action.

T177's l-action was built by rotating a Fibonacci grid and taking nearest points.
A Fibonacci grid is NOT invariant under the cubic rotations, so that 'permutation'
was an approximation and the action failed the representation test badly
(9.8e-1 at l=4).  Its counts were therefore worthless.

Build the action exactly instead.  Spin-l = HARMONIC POLYNOMIALS of degree l in
three variables (dimension 2l+1), and a rotation acts by f(x) -> f(R^T x), which
is an exact matrix on monomial coefficients.  The harmonic subspace is the kernel
of the Laplacian on degree-l monomials.  No grid, no approximation.

CONTROLS: the action must satisfy A(R)A(S) = A(RS) to machine precision; l=0,1,2
must reproduce R103's 2, 4, 4; and the trivial group must return 24*(2l+1)."""
import numpy as np, itertools
from math import comb
def cubic():
    R=[]
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1,-1],repeat=3):
            M=np.zeros((3,3))
            for i,q in enumerate(p): M[i,q]=s[i]
            if abs(np.linalg.det(M)-1)<1e-9: R.append(M)
    return R
ROT=cubic()
def mons(l): return [(a,b,l-a-b) for a in range(l+1) for b in range(l-a+1)]
def poly_action(R,l):
    """matrix of f(x) -> f(R^T x) on degree-l monomial coefficients"""
    M=mons(l); idx={m:i for i,m in enumerate(M)}
    A=np.zeros((len(M),len(M)))
    for j,m in enumerate(M):
        # (R^T x)^m = prod_k (sum_i R[i,k] x_i)^{m_k}
        coeffs={(0,0,0):1.0}
        for k in range(3):
            for _ in range(m[k]):
                new={}
                for i in range(3):
                    c=R[i,k]
                    if abs(c)<1e-15: continue
                    for e,v in coeffs.items():
                        e2=list(e); e2[i]+=1; e2=tuple(e2)
                        new[e2]=new.get(e2,0.0)+v*c
                coeffs=new
        for e,v in coeffs.items(): A[idx[e],j]+=v
    return A
def harmonic_proj(l):
    """basis of the Laplacian kernel on degree-l monomials"""
    M=mons(l)
    if l<2: return np.eye(len(M))
    Mlow=mons(l-2); idx={m:i for i,m in enumerate(Mlow)}
    L=np.zeros((len(Mlow),len(M)))
    for j,m in enumerate(M):
        for k in range(3):
            if m[k]>=2:
                e=list(m); e[k]-=2
                L[idx[tuple(e)],j]+=m[k]*(m[k]-1)
    U,s,Vt=np.linalg.svd(L)
    ns=Vt[np.sum(s>1e-9):]
    return ns.T
def l_action(l):
    B=harmonic_proj(l)
    Bp=np.linalg.pinv(B)
    return [Bp@poly_action(R,l)@B for R in ROT]
DIRS=[np.array(d,dtype=float) for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
def perm_action(R):
    P=np.zeros((6,6))
    for j,d in enumerate(DIRS):
        i=[k for k,e in enumerate(DIRS) if np.allclose(e,R@d)][0]; P[i,j]=1.0
    return P
def herm_action(R):
    M=np.zeros((4,4)); M[0,0]=1.0; M[1:,1:]=R; return M
IN=[np.kron(perm_action(R),herm_action(R)) for R in ROT]
def eq_dim(gin,gout):
    P=np.zeros((gout[0].shape[0]*gin[0].shape[0],)*2)
    for A,Bm in zip(gin,gout): P+=np.kron(np.linalg.inv(A).T,Bm)
    return int(round(np.trace(P/len(gin)).real))
print("T177b  exact spin-l action on harmonic polynomials")
print(f"   {'l':>3} {'dim':>5} {'rep check':>12} {'covariant maps':>16} {'R103':>7}")
known={0:2,1:4,2:4}
for l in range(0,7):
    A=l_action(l)
    err=0.0
    for i in range(6):
        for j in range(6):
            k=[t for t,X in enumerate(ROT) if np.allclose(X,ROT[i]@ROT[j])][0]
            err=max(err,np.abs(A[i]@A[j]-A[k]).max())
    d=eq_dim(IN,A)
    print(f"   {l:3d} {A[0].shape[0]:5d} {err:12.1e} {d:16d} {str(known.get(l,'')):>7}")
print()
print(f"   CONTROL trivial group at l=3 -> 24*7 = 168 : {eq_dim([np.eye(24)],[np.eye(7)])}")
