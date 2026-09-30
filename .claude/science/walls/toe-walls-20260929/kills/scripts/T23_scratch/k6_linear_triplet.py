#!/usr/bin/env python3
"""K6: exact linear-algebra version. For each generator g, S_g = {range<=1, period-2 real/complex A : A D' = eps D A}.
Triplet preservation of the lift A P_g is LINEAR in A (rest<-triplet block of V^T A P_g V = 0).  Compute dim S_g and the
dim of the triplet-preserving subspace; then the rank of the triplet->triplet block map on that subspace."""
import numpy as np
exec(open('k1_local_intertwiners.py').read().split("gens={")[0])
G={'E':sp((0,1,2),(1,1,1)),'C4z':sp((1,0,2),(-1,1,1)),'C2d':sp((1,0,2),(-1,-1,-1)),'C3':sp((1,2,0),(1,1,1)),'C2z':sp((0,1,2),(-1,-1,1))}
rest=[i for i in range(8) if i not in triplet]
for name,M in G.items():
    for eps in (1,-1):
        null=solve(M,eps); mats=mats_from_null(null)
        Ps=Pg(M)
        Ks=[V.T@(A@Ps)@V for A in mats]
        # linear map c -> leakage block
        Lk=np.array([k[np.ix_(rest,triplet)].flatten() for k in Ks]).T     # (15, k)
        u,s,vt=np.linalg.svd(Lk,full_matrices=True)
        r=int((s>1e-9).sum()); sub=vt[r:]                                   # basis of triplet-preserving subspace
        dim=len(sub)
        if dim==0:
            print(f"{name:4s} eps={eps:+d}: dim S_g={len(null)}, triplet-preserving subspace dim = 0"); continue
        Tb=np.array([sum(c*Ks[i][np.ix_(triplet,triplet)] for i,c in enumerate(v)).flatten() for v in sub])
        rt=np.linalg.matrix_rank(Tb,tol=1e-9)
        # do any of these blocks contain a permutation-type (transposition) pattern? look at the span of triplet blocks
        print(f"{name:4s} eps={eps:+d}: dim S_g={len(null)}, triplet-preserving subspace dim = {dim}, span of 3x3 triplet blocks has rank {rt}")
        # which 3x3 patterns appear: check whether span contains elementary matrix e_ij for i!=j
        span=Tb.reshape(dim,3,3)
        def in_span(Mx):
            A=Tb.T; x,res,rk,sv=np.linalg.lstsq(A,Mx.flatten(),rcond=None); return np.linalg.norm(A@x-Mx.flatten())<1e-8
        offdiag=[(i,j) for i in range(3) for j in range(3) if i!=j]
        print("     off-diagonal elementary matrices in span:",[(i,j) for (i,j) in offdiag if in_span(np.eye(3)[:,[j]]@np.eye(3)[[i],:])])
        print("     diagonal-only span? ", all(np.abs(span[:,i,j]).max()<1e-9 for (i,j) in offdiag))
