"""
T305 - is it the ALGEBRA enlargement or the LATTICE enlargement that selects
the Born weight?

R193 showed the anti-Born branch fails to order for CP^3 on Z^4.  R142 says Z^4
forces M4(C), but not the converse -- so M4(C) on Z^3 is a coherent intermediate.
If the anti-Born branch already fails there, the selection needs only the ALGEBRA
enlargement, which is a weaker and more interesting requirement than the full
Z^4 + M4(C) package.

Also run n=3 (CP^2) to see whether the mechanism is "n>2" generally or specific
to n=4 -- the degeneracy argument (a whole CP^{n-2} free per site) predicts
"any n>2".

Control that makes the test conclusive: the BORN branch must order in the same
setting. If it does not (Z^3 has 6 neighbours vs Z^4's 8, so t_c is higher and
may exceed the endpoint), the setting is too weakly coupled and the anti-Born
result there says nothing.
"""
import numpy as np
def run(L,d,n,w,sweeps=2200,burn=700,seed=7):
    rng=np.random.default_rng(seed); shape=(L,)*d; N=L**d
    psi=rng.normal(size=shape+(n,))+1j*rng.normal(size=shape+(n,))
    psi/=np.linalg.norm(psi,axis=-1,keepdims=True)
    idx=np.indices(shape); stag=(-1.0)**(sum(idx)%2)
    U=[];S=[]
    for sw in range(sweeps):
        for _ in range(N):
            pos=tuple(rng.integers(0,L,d)); nb=[]
            for ax in range(d):
                for s in (1,-1):
                    q=list(pos); q[ax]=(q[ax]+s)%L; nb.append(psi[tuple(q)])
            nb=np.array(nb); old=psi[pos]
            new=rng.normal(size=n)+1j*rng.normal(size=n); new/=np.linalg.norm(new)
            to=np.abs(nb@old.conj())**2; tn=np.abs(nb@new.conj())**2
            den=np.prod((1-w)*to+w*(1-to)); num=np.prod((1-w)*tn+w*(1-tn))
            if den<=0: continue
            if num>=den or rng.random()<num/den: psi[pos]=new
        if sw>=burn and sw%4==0:
            rho=psi[...,:,None]*psi[...,None,:].conj()-np.eye(n)/n
            U.append(np.linalg.norm(rho.sum(axis=tuple(range(d))))/N)
            S.append(np.linalg.norm((rho*stag[...,None,None]).sum(axis=tuple(range(d))))/N)
    return np.mean(U),np.mean(S)
print("does the ALGEBRA enlargement alone select the Born weight?")
print("w=0 Born, w=1 anti-Born.  Control: the Born row must ORDER, else the")
print("setting is too weakly coupled for the anti-Born row to mean anything.\n")
print("  lattice   n    L     w     uniform   staggered   floor     verdict")
for d,Ls in ((3,(10,14)),(4,(6,))):
    for n in (4,3):
        for L in Ls:
            for w in (0.0,1.0):
                u,s=run(L,d,n,w); fl=1/np.sqrt(L**d); big=max(u,s)
                v="ORDERED" if big>3*fl else "disordered"
                print(f"    Z^{d}    {n}   {L:3d}   {w:.1f}   {u:.5f}   {s:.5f}   {fl:.5f}   {v}"
                      +f"  ({'stag' if s>u else 'unif'})")
