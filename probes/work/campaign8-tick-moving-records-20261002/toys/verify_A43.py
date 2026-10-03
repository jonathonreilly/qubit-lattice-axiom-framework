"""Coordinator check of lane A43: (1) walk nodes/hands; (2) lemma S1 by characters; (3) Neel LSWT speed; (4) parton hop = walk."""
import numpy as np, itertools
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1,-1]).astype(complex); s=[sx,sy,sz]
# (1) walk H = sum sin k_a sigma_a : nodes, hands, slopes
hands=[]
for n in itertools.product([0,1],repeat=3):
    K=np.pi*np.array(n); v=[(-1)**n[a] for a in range(3)]; hands.append(int(np.prod(v)))
    for d in np.random.default_rng(1).normal(size=(20,3)):
        d/=np.linalg.norm(d); q=1e-5*d; H=sum(np.sin(K[a]+q[a])*s[a] for a in range(3))
        assert abs(np.linalg.eigvalsh(H)[1]/1e-5-1)<1e-6
print("(1) walk: 8 nodes, all slopes 1; hands", hands, "sum", sum(hands))
# (2) proper cubic group O (24 signed perms, det +1) and its SU(2) lift
R=[]
for p in itertools.permutations(range(3)):
    for sg in itertools.product([1,-1],repeat=3):
        M=np.zeros((3,3));
        for i in range(3): M[i,p[i]]=sg[i]
        if np.linalg.det(M)>0.5: R.append(M)
assert len(R)==24
def lift(M):  # SU(2) element U with U sigma_a U^dag = sum_b M_ba sigma_b
    best=None
    for c in np.random.default_rng(0).normal(size=(200,2,2))+1j*np.random.default_rng(1).normal(size=(200,2,2)):
        X=sum(sum(M[b,a]*s[b] @ c @ s[a].conj().T for a in range(3)) for b in range(3))+c  # averaging trick
        if np.linalg.norm(X)>1e-6:
            U=X/np.sqrt(np.linalg.det(X)); 
            if all(np.allclose(U@s[a]@U.conj().T, sum(M[b,a]*s[b] for b in range(3))) for a in range(3)): return U
    raise RuntimeError
U=[lift(M) for M in R]
chiT1=np.array([np.trace(M) for M in R])
def mult_T1_in_End(D):  # D: list of matrices (rep or projective rep); End = D (x) D*, genuine
    chiEnd=np.array([abs(np.trace(d))**2 for d in D])
    return np.real(np.sum(chiEnd*chiT1)/24)
# 1-dim reps of O: A1 trivial, A2 = sign of the permutation part
def sgnperm(M): 
    P=np.abs(M); return round(np.linalg.det(P))
A1=[np.eye(1) for M in R]; A2=[np.eye(1)*sgnperm(M) for M in R]
def dsum(X,Y): return [np.block([[x,np.zeros((x.shape[0],y.shape[1]))],[np.zeros((y.shape[0],x.shape[1])),y]]) for x,y in zip(X,Y)]
# E rep: action of S3 (axis permutation) on the plane sum=0
B=np.array([[1,-1,0],[1,1,-2]],float); B[0]/=np.sqrt(2); B[1]/=np.sqrt(6)
E=[B@np.abs(M)@B.T for M in R]
for name,D in [("A1+A1",dsum(A1,A1)),("A1+A2",dsum(A1,A2)),("A2+A2",dsum(A2,A2)),("E",E),("spin-1/2",U)]:
    print("(2)", name, "mult of T1 in End:", round(mult_T1_in_End(D),6))
# (3) Neel LSWT for H = J sum sigma.sigma (Pauli units): omega = 12 J sqrt(1-gamma^2); speed 4 sqrt3 J
J=1.0
for d in [np.array([1,0,0]),np.array([1,1,1])/np.sqrt(3),np.array([1,2,0])/np.sqrt(5)]:
    k=1e-4*d; g=np.mean(np.cos(k)); w=12*J*np.sqrt(1-g**2); print("(3) speed along",np.round(d,3),":",round(w/1e-4,4),"vs 4sqrt3 =",round(4*np.sqrt(3),4))
# (4) parton: hop f_x^dag (i lam sigma_a) f_{x+e_a} + h.c. -> Bloch h(k) = sum_a (i lam sigma_a e^{ik_a} + h.c.) = -2 lam sum sin k_a sigma_a
lam=0.7; k=np.array([0.3,-1.1,2.0])
h=sum(1j*lam*s[a]*np.exp(1j*k[a]) + (1j*lam*s[a]*np.exp(1j*k[a])).conj().T for a in range(3))
print("(4) parton hop equals -2 lam sum sin k sigma:", np.allclose(h, -2*lam*sum(np.sin(k[a])*s[a] for a in range(3))))
