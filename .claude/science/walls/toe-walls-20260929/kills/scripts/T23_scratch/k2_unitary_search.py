#!/usr/bin/env python3
"""K2: search for UNITARY finite-range (range<=1, period-2 coefficients) operators A with A D' = eps D A, D'=P_g D P_g^T,
i.e. all local unitary lifts of the lattice rotation g that are symmetries of the staggered D (not only monomial ones).
Then report the 8x8 kernel action and how it treats the hw=1 corner triplet."""
import itertools, numpy as np, torch, sys
exec(open('k1_local_intertwiners.py').read().split("gens={")[0])
torch.set_default_dtype(torch.float64)
def run(M,eps,ntry=60,seed=0):
    null=solve(M,eps); mats=mats_from_null(null)
    Bt=torch.tensor(np.array(mats),dtype=torch.complex128)       # (k,N,N)
    Ps=Pg(M); Vt=torch.tensor(V,dtype=torch.complex128); Pt=torch.tensor(Ps,dtype=torch.complex128)
    k=len(mats); out=[]
    g=torch.Generator().manual_seed(seed)
    for t in range(ntry):
        c=(torch.randn(k,generator=g)+1j*torch.randn(k,generator=g)).to(torch.complex128)*0.3
        c.requires_grad_(True)
        opt=torch.optim.LBFGS([c],lr=1,max_iter=400,tolerance_grad=1e-14,tolerance_change=1e-16,line_search_fn='strong_wolfe')
        def closure():
            opt.zero_grad()
            A=torch.einsum('k,kij->ij',c,Bt)
            Id=torch.eye(N,dtype=torch.complex128)
            loss=((A.conj().T@A-Id).abs()**2).sum()
            loss.backward(); return loss
        for _ in range(4): opt.step(closure)
        A=torch.einsum('k,kij->ij',c,Bt).detach()
        err=(A.conj().T@A-torch.eye(N,dtype=torch.complex128)).abs().max().item()
        if err<1e-9:
            K=(Vt.conj().T@A@Pt@Vt).numpy()
            out.append((A.numpy(),K))
    return out
def classify(K):
    """triplet block and leakage"""
    T=K[np.ix_(triplet,triplet)]; rest=[i for i in range(8) if i not in triplet]
    leak=np.linalg.norm(K[np.ix_(rest,triplet)])
    return T,leak
if __name__=="__main__":
    name=sys.argv[1]; eps=int(sys.argv[2])
    G={'E':sp((0,1,2),(1,1,1)),'C4z':sp((1,0,2),(-1,1,1)),'C2d':sp((1,0,2),(-1,-1,-1)),'C3':sp((1,2,0),(1,1,1))}
    res=run(G[name],eps,ntry=int(sys.argv[3]) if len(sys.argv)>3 else 30)
    print(name,eps,"unitary solutions found:",len(res))
    seen=[]
    for A,K in res:
        T,leak=classify(K)
        nz=int((np.abs(K)>1e-6).sum())
        mono=all((np.abs(A[i])>1e-8).sum()==1 for i in range(N))   # monomial?
        rowsupp=max((np.abs(A[i])>1e-8).sum() for i in range(N))
        print(f"  monomial={mono} maxrowsupport={rowsupp} leak(triplet->rest)={leak:.3f} |T|:",np.round(np.abs(T),3).tolist(), "nnz K",nz)
