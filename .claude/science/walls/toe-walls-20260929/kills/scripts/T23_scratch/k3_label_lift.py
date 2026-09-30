#!/usr/bin/env python3
"""K3: does a range<=1 UNITARY intertwiner A (A D' = eps D A) exist that acts as the identity on ker D, so that
A P_g is a genuine exact local symmetry of D whose kernel action equals the label-level permutation (transposition of
the hw=1 triplet for C4/C2')?  Uses the same linear space as k1/k2 (complex coefficients).  Also reports the
best achievable residual of the weaker target 'preserves triplet subspace'."""
import itertools, numpy as np, torch, sys
exec(open('k1_local_intertwiners.py').read().split("gens={")[0])
G={'E':sp((0,1,2),(1,1,1)),'C4z':sp((1,0,2),(-1,1,1)),'C2d':sp((1,0,2),(-1,-1,-1)),'C3':sp((1,2,0),(1,1,1))}
def attempt(name,eps,ntry=20,mode='identity',seed=1):
    M=G[name]; null=solve(M,eps); mats=mats_from_null(null)
    Bt=torch.tensor(np.array(mats),dtype=torch.complex128)
    Ps=Pg(M); Vt=torch.tensor(V,dtype=torch.complex128); Pt=torch.tensor(Ps,dtype=torch.complex128)
    Rlab=(Vt.conj().T@Pt@Vt)         # label-level kernel action of pure site permutation
    trip=torch.tensor(triplet); rest=torch.tensor([i for i in range(8) if i not in triplet])
    k=len(mats); best=None; g=torch.Generator().manual_seed(seed)
    for t in range(ntry):
        c=((torch.randn(k,generator=g)+1j*torch.randn(k,generator=g))*0.3).to(torch.complex128).requires_grad_(True)
        opt=torch.optim.LBFGS([c],lr=1,max_iter=500,tolerance_grad=1e-15,tolerance_change=1e-18,line_search_fn='strong_wolfe')
        def closure():
            opt.zero_grad()
            A=torch.einsum('k,kij->ij',c,Bt); Id=torch.eye(N,dtype=torch.complex128)
            loss=((A.conj().T@A-Id).abs()**2).sum()
            Kf=Vt.conj().T@A@Pt@Vt              # kernel action of the lift A P_g
            if mode=='identity':                # A acts trivially on ker D  => kernel action == label permutation
                loss=loss+((Kf-Rlab).abs()**2).sum()
            elif mode=='triplet':               # only require triplet subspace preserved (no leakage)
                loss=loss+((Kf[rest][:,trip]).abs()**2).sum()
            loss.backward(); return loss
        for _ in range(6): opt.step(closure)
        l=closure().item()
        if best is None or l<best[0]:
            best=(l,c.detach().clone())
        if l<1e-18: break
    l,c=best
    A=torch.einsum('k,kij->ij',c,Bt).detach()
    Kf=(Vt.conj().T@A@Pt@Vt).numpy()
    return l,A.numpy(),Kf
if __name__=="__main__":
    name=sys.argv[1]; eps=int(sys.argv[2]); mode=sys.argv[3]; nt=int(sys.argv[4])
    l,A,Kf=attempt(name,eps,ntry=nt,mode=mode)
    T=Kf[np.ix_(triplet,triplet)]
    print(f"{name} eps={eps:+d} mode={mode}: best loss {l:.3e}")
    if l<1e-12:
        print("  lift exists. triplet block |.|:",np.round(np.abs(T),3).tolist())
        print("  monomial?",all((np.abs(A[i])>1e-8).sum()==1 for i in range(N)), " max row support",max((np.abs(A[i])>1e-8).sum() for i in range(N)))
