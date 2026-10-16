# Exact (rational) setup of covariant walks; complexified: U and V=U^{-1} independent.
import itertools, sympy as sp
from fractions import Fraction
def rotations():
    Rs=[]
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1,-1],repeat=3):
            M=sp.zeros(3,3)
            for i in range(3): M[i,p[i]]=s[i]
            if M.det()==1: Rs.append(M)
    return Rs
# quaternion basis q0=1,q1=i sx,q2=i sy,q3=i sz ; (i s_a)(i s_b) = -(d_ab + i eps s_c) = -d_ab - eps_abc (i s_c)
def qmul(a,b):
    if a==0: return {b:1}
    if b==0: return {a:1}
    if a==b: return {0:-1}
    c=6-a-b
    eps=sp.LeviCivita(a,b,c)
    return {c:-eps}
class Alg:
    """algebra H (x) M_m over Q, basis (a,i,j); conj action from R"""
    def __init__(s,m,Mrep): s.m=m; s.Mrep=Mrep
        # Mrep(R): m x m rational matrix (genuine rep) acting on second factor by conjugation
    def basis(s): return [(a,i,j) for a in range(4) for i in range(s.m) for j in range(s.m)]
    def mul(s,X,Y):
        Z={}
        for (a,i,j),x in X.items():
            for (b,k,l),y in Y.items():
                if j!=k: continue
                for c,cf in qmul(a,b).items():
                    Z[(c,i,l)]=Z.get((c,i,l),0)+cf*x*y
        return Z
    def ad(s,R):
        """matrix of conjugation on basis"""
        B=s.basis(); idx={b:t for t,b in enumerate(B)}
        M=s.Mrep(R); Mi=M.inv()
        A=sp.zeros(len(B),len(B))
        for t,(a,i,j) in enumerate(B):
            # q_a -> sum_c Rq[c,a] q_c, with Rq = 1 (+) R
            qa=[(0,1)] if a==0 else [(c+1,R[c,a-1]) for c in range(3) if R[c,a-1]!=0]
            E=sp.zeros(s.m,s.m); E[i,j]=1; E2=M*E*Mi
            for c,cf in qa:
                for k in range(s.m):
                    for l in range(s.m):
                        if E2[k,l]!=0: A[idx[(c,k,l)],t]+=cf*E2[k,l]
        return A
def perm_rep2(R):
    P=R.applyfunc(abs)  # permutation matrix
    b=sp.Matrix([[1,0],[-1,1],[0,-1]])  # columns e1-e2, e2-e3
    # P*b = b*M
    M=(b.T*b).inv()*b.T*P*b
    assert P*b==b*M
    return M
def equivariant_basis(alg,G,offsets):
    """returns list of basis elements; each element: dict offset->dict basisindex->coef"""
    B=alg.basis(); nb=len(B)
    ads={tuple(R):alg.ad(R) for R in G}
    seen=set(); out=[]
    for n in offsets:
        if n in seen: continue
        orb={}
        nv=sp.Matrix(n)
        stab=[R for R in G if tuple(R*nv)==n]
        for R in G: orb.setdefault(tuple(R*nv),R)
        seen|=set(orb)
        # fixed space of stab
        Mfix=sp.Matrix.vstack(*[ads[tuple(R)]-sp.eye(nb) for R in stab])
        ns=Mfix.nullspace()
        for v in ns:
            el={}
            for m,R in orb.items():
                w=ads[tuple(R)]*v
                el[m]={B[t]:w[t] for t in range(nb) if w[t]!=0}
            out.append(el)
    return out
