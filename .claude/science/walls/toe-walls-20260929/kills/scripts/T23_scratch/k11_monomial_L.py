#!/usr/bin/env python3
"""K11: robustness of the attack's block F (monomial dressed symmetries) to lattice size.  Repeat the (g,t) enumeration at L=6
(t over all L^3 translations) and count proper / improper dressed symmetries that preserve the hw=1 triplet and their triplet action."""
import itertools, sys, numpy as np
from collections import Counter
L=int(sys.argv[1]); N=L**3
pts=list(itertools.product(range(L),repeat=3)); idx=lambda x,y,z:((x%L)*L+(y%L))*L+(z%L)
D=np.zeros((N,N))
for (x,y,z) in pts:
    eta=[1,(-1)**x,(-1)**(x+y)]
    for mu,e in enumerate([(1,0,0),(0,1,0),(0,0,1)]):
        i=idx(x,y,z); D[i,idx(x+e[0],y+e[1],z+e[2])]+=eta[mu]/2; D[i,idx(x-e[0],y-e[1],z-e[2])]-=eta[mu]/2
corners=list(itertools.product([0,1],repeat=3)); V=np.zeros((N,8))
for a,c in enumerate(corners):
    for p in pts: V[idx(*p),a]=(-1)**(c[0]*p[0]+c[1]*p[1]+c[2]*p[2])
V/=np.sqrt(N); triplet=[corners.index(c) for c in [(1,0,0),(0,1,0),(0,0,1)]]
G=[]
for p in itertools.permutations(range(3)):
    for s in itertools.product([1,-1],repeat=3):
        M=np.zeros((3,3),int)
        for j in range(3): M[p[j],j]=s[j]
        G.append((p,s,M))
nz=[np.nonzero(D[i])[0] for i in range(N)]
def dress(perm_index):     # U = site permutation given as array q[p]: U e_p = e_q[p]
    # Dg = U D U^T ; want diagonal signs s with S Dg S = eps D
    Dg=np.zeros_like(D)
    Dg[np.ix_(perm_index,perm_index)]=D     # (U D U^T)[q(i),q(j)] = D[i,j]
    for eps in (1,-1):
        s=np.zeros(N,int); s[0]=1; stack=[0]; ok=True
        while stack and ok:
            i=stack.pop()
            for j in nz[i]:
                if abs(Dg[i,j])<1e-12: ok=False;break
                sj=int(round(eps*D[i,j]/Dg[i,j]))*s[i]
                if s[j]==0: s[j]=sj; stack.append(j)
                elif s[j]!=sj: ok=False;break
        if ok and (s!=0).all() and np.allclose((s[:,None]*Dg*s[None,:]),eps*D): return eps,s
    return None
cnt=Counter(); acts=Counter(); ndress=0
for (p,sg,M) in G:
    prop=round(np.linalg.det(M))==1
    for t in itertools.product(range(L),repeat=3):
        q=np.array([idx(*tuple((M@np.array(pp)+np.array(t))%L)) for pp in pts])
        r=dress(q)
        if r is None: continue
        eps,s=r; ndress+=1
        # kernel action: (S U) V ; U e_p = e_q[p]
        UV=np.zeros_like(V); UV[q,:]=V
        R8=V.T@(s[:,None]*UV)
        if np.linalg.norm(R8.T@R8-np.eye(8))>1e-8: continue
        rest=[i for i in range(8) if i not in triplet]
        pres=np.linalg.norm(R8[np.ix_(rest,triplet)])<1e-9
        cnt[(prop,eps,pres)]+=1
        if pres:
            T=R8[np.ix_(triplet,triplet)]; perm=tuple(int(np.argmax(np.abs(T[:,j]))) for j in range(3))
            acts[(prop,perm)]+=1
print(f"L={L}: dressed (g,t) found: {ndress} of {48*L**3}")
print(" by (proper, eps, triplet-preserved):",dict(cnt))
print(" triplet-preserving actions by (proper, permutation of the three corners):",dict(acts))
