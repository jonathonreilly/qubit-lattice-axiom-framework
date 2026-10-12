# R13-2 s2: order-k^2 quadratic h-potentials B2(k) = sum_{a<=b} k_a k_b M_ab (M_ab real symmetric 6x6) that annihilate
#  (i)  every symmetric gradient k (x)_s alpha (full linear vector-gauge invariance), or
#  (ii) only transverse ones, alpha = k x beta (flat vector partners).
# Question: does any POSITIVE-SEMIDEFINITE member have a nonzero TT block?  (cutting-plane LP: maximise the minimum
# eigenvalue over sampled directions subject to a unit TT trace; max < 0 => no PSD member with TT != 0.)
import numpy as np, itertools
from scipy.optimize import linprog
from common import *
rng=np.random.default_rng(3)
mons=[(a,b) for a in range(3) for b in range(a,3)]
symb=[]
for i in range(6):
    for j in range(i,6):
        E=np.zeros((6,6)); E[i,j]=E[j,i]=1; symb.append(E)
basis=[(m,E) for m in mons for E in symb]      # 6*21 = 126
def B_of(c,k):
    out=np.zeros((6,6))
    for ci,(m,E) in zip(c,basis):
        if ci!=0: out+=ci*k[m[0]]*k[m[1]]*E
    return out
def Bbasis(k): return [k[m[0]]*k[m[1]]*E for (m,E) in basis]
def cross(k): return np.array([[0,-k[2],k[1]],[k[2],0,-k[0]],[-k[1],k[0],0]])
def nullspace(cond):
    rows=[]
    for t in range(60):
        k=rng.normal(size=3); Bk=Bbasis(k); V=cond(k)
        rows.append(np.array([ (B@V).ravel() for B in Bk]).T)
    A=np.vstack(rows); u,s,vt=np.linalg.svd(A); tol=1e-9*s[0]; r=np.sum(s>tol); return vt[r:].T, s
def cubic_project(N):
    # project the null space onto cubic-covariant members: B(Rk) = D B(k) D^T
    cols=[]
    for v in N.T:
        acc=np.zeros(len(basis))
        # least squares fit of the group average back into the monomial basis
        ks=[rng.normal(size=3) for _ in range(40)]
        target=[]; design=[]
        for k in ks:
            Bavg=sum(D.T@B_of(v,R@k)@D for R,D in zip(G48,D48))/48
            target.append(Bavg.ravel()); design.append(np.array([B.ravel() for B in Bbasis(k)]).T)
        sol=np.linalg.lstsq(np.vstack(design),np.concatenate(target),rcond=None)[0]; cols.append(sol)
    C=np.array(cols).T; u,s,vt=np.linalg.svd(C,full_matrices=False); r=np.sum(s>1e-8*s[0]); return u[:,:r]
def PTT(k):
    A=np.hstack([Vmap(k),Svec(k)[:,None]]); Qo,_=np.linalg.qr(A); return np.eye(6)-Qo@Qo.T
dirs=[d/np.linalg.norm(d) for d in rng.normal(size=(400,3))]
def lp_maxmin(N, restrict=None, iters=60):
    d=N.shape[1]
    Tvec=np.array([np.mean([np.trace(PTT(k)@B_of(N[:,i],k)) for k in dirs[:100]]) for i in range(d)])
    cuts=[]
    for k in dirs[:20]:
        for v in np.eye(6): cuts.append((k,v))
    best=None
    for it in range(iters):
        # variables (c_1..c_d, t): maximise t s.t. v^T B(c,k) v >= t ; Tvec.c = 1 ; |c_i| <= 50
        A=[]; b=[]
        for k,v in cuts:
            row=[ -(v@B_of(N[:,i],k)@v) for i in range(d)]+[1.0]; A.append(row); b.append(0.0)
        res=linprog(c=np.r_[np.zeros(d),-1.0],A_ub=np.array(A),b_ub=np.array(b),A_eq=np.r_[Tvec,0.0][None,:],b_eq=[1.0],
                    bounds=[(-50,50)]*d+[(None,None)],method='highs')
        c=res.x[:d]; t=res.x[d]
        # find worst eigenpair over all directions
        worst=(1e9,None,None)
        for k in dirs:
            B=B_of(N@c,k)
            if restrict is not None: P=restrict(k); B=P@B@P
            w,V=np.linalg.eigh(B)
            if w[0]<worst[0]: worst=(w[0],k,V[:,0])
        cuts.append((worst[1],worst[2])); best=(t,worst[0])
        if worst[0]>=t-1e-9: break
    return best
Ptl=np.eye(6)-np.outer(trv,trv)/3
print("(i) full linear vector-gauge invariance  B2(k) Vmap(k) = 0:")
N1,s=nullspace(lambda k: Vmap(k)); print("   dim (no symmetry imposed) =",N1.shape[1])
C1=cubic_project(N1); print("   dim (cubic-covariant) =",C1.shape[1])
# compare with h:R(h)
k=rng.normal(size=3); BN=-Rmap(k)   # sign as R12-5 s2: B_h = -R  (h:R(h) with their convention)
coef=np.linalg.lstsq(np.array([B_of(C1[:,i],k).ravel() for i in range(C1.shape[1])]).T,BN.ravel(),rcond=None)
print("   h:R(h) lies in the cubic space: residual %.1e"%np.linalg.norm(np.array([B_of(C1[:,i],k).ravel() for i in range(C1.shape[1])]).T@coef[0]-BN.ravel()))
print("   eigenvalues of h:R(h) symbol at random k (normalised by k^2):",np.round(np.linalg.eigvalsh(BN)/(k@k),4))
t,w=lp_maxmin(N1); print("   LP over ALL (non-symmetric) members: max_{TT trace=1} min eig = %.4f (worst sampled %.4f)"%(t,w))
t,w=lp_maxmin(C1); print("   LP over cubic members:            max_{TT trace=1} min eig = %.4f (worst sampled %.4f)"%(t,w))
print("(ii) transverse-only invariance  B2(k) Vmap(k) [k]_x = 0 (flat vector partners), PSD required on traceless h:")
N2,s=nullspace(lambda k: Vmap(k)@cross(k)); print("   dim (no symmetry) =",N2.shape[1])
C2=cubic_project(N2); print("   dim (cubic-covariant) =",C2.shape[1])
t,w=lp_maxmin(C2,restrict=lambda k: Ptl); print("   LP over cubic members, PSD on traceless: max_{TT trace=1} min eig = %.4f (worst %.4f)"%(t,w))
t,w=lp_maxmin(N2,restrict=lambda k: Ptl); print("   LP over all members,   PSD on traceless: max_{TT trace=1} min eig = %.4f (worst %.4f)"%(t,w))
