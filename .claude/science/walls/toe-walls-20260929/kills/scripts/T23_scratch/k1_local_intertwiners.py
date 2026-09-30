#!/usr/bin/env python3
"""Kill check K1: the attack's operator-level claim (F) only enumerates MONOMIAL dressings (site perm x diagonal signs).
Here: solve for ALL finite-range (range<=1, 27 offsets, coefficients period 2) real operators A with A D' = eps D A,
D' = P_g D P_g^T, for g = generators of O. Then ask what the kernel action V^T A P_g V looks like on the hw=1 triplet."""
import itertools, numpy as np, sys
np.set_printoptions(precision=4, suppress=True, linewidth=160)
L=4; N=L**3
pts=list(itertools.product(range(L),repeat=3))
idx=lambda x,y,z:((x%L)*L+(y%L))*L+(z%L)
D=np.zeros((N,N))
for (x,y,z) in pts:
    eta=[1,(-1)**x,(-1)**(x+y)]
    for mu,e in enumerate([(1,0,0),(0,1,0),(0,0,1)]):
        i=idx(x,y,z); D[i,idx(x+e[0],y+e[1],z+e[2])]+=eta[mu]/2; D[i,idx(x-e[0],y-e[1],z-e[2])]-=eta[mu]/2
corners=list(itertools.product([0,1],repeat=3))
V=np.zeros((N,8))
for a,c in enumerate(corners):
    for p in pts: V[idx(*p),a]=(-1)**(c[0]*p[0]+c[1]*p[1]+c[2]*p[2])
V/=np.sqrt(N)
triplet=[corners.index(c) for c in [(1,0,0),(0,1,0),(0,0,1)]]
def Pg(M):
    U=np.zeros((N,N))
    for p in pts:
        q=tuple((M@np.array(p))%L); U[idx(*q),idx(*p)]=1
    return U
offs=[t for t in itertools.product([-1,0,1],repeat=3)]
par=list(itertools.product([0,1],repeat=3))
nun=len(offs)*len(par)
def unknown_index(ti,pi): return ti*len(par)+pi
def basis_matrix(ti,pi):
    B=np.zeros((N,N))
    t=offs[ti]; pr=par[pi]
    for p in pts:
        if (p[0]%2,p[1]%2,p[2]%2)==pr:
            B[idx(*p),idx(p[0]+t[0],p[1]+t[1],p[2]+t[2])]=1
    return B
basis=[basis_matrix(ti,pi) for ti in range(len(offs)) for pi in range(len(par))]
def solve(M,eps):
    Dp=Pg(M)@D@Pg(M).T
    # A Dp - eps D A = 0
    cols=[ (B@Dp - eps*D@B).flatten() for B in basis]
    Amat=np.array(cols).T
    u,s,vt=np.linalg.svd(Amat,full_matrices=False)
    null=vt[np.sum(s>1e-9):]
    return null
def mats_from_null(null):
    return [sum(c*B for c,B in zip(v,basis)) for v in null]
def sp(p,s):
    M=np.zeros((3,3),int)
    for j in range(3): M[p[j],j]=s[j]
    return M
gens={'E':sp((0,1,2),(1,1,1)),'C4z':sp((1,0,2),(-1,1,1)),'C2diag[1,-1,0]':sp((1,0,2),(-1,-1,-1)),'C3':sp((1,2,0),(1,1,1))}
for name,M in gens.items():
    assert round(np.linalg.det(M))==1
    for eps in (1,-1):
        null=solve(M,eps)
        print(f"{name:16s} eps={eps:+d}: dim of space of range<=1 period-2 intertwiners A = {len(null)}")
        if len(null)==0: continue
        Ps=Pg(M)
        Ks=[V.T@(A@Ps)@V for A in mats_from_null(null)]
        # dimension of the span of the 8x8 kernel actions and of the triplet-triplet blocks
        K=np.array([k.flatten() for k in Ks]); r=np.linalg.matrix_rank(K,tol=1e-9)
        Tb=np.array([k[np.ix_(triplet,triplet)].flatten() for k in Ks]); rt=np.linalg.matrix_rank(Tb,tol=1e-9)
        Lk=np.array([np.delete(np.delete(k,triplet,0),triplet,1).flatten() for k in Ks])
        offblk=np.array([np.concatenate([k[np.ix_([i for i in range(8) if i not in triplet],triplet)].flatten()]) for k in Ks])
        print(f"      span of 8x8 kernel actions: rank {r};  triplet block rank {rt};  triplet->outside block rank {np.linalg.matrix_rank(offblk,tol=1e-9)}")
