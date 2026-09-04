"""
T301 - WHY the anti-Born branch fails to order at M4(C): mechanism, two routes.

T300 finds the anti-Born branch disordered on CP^3. "Disordered" can mean the
ground state is extensively degenerate, or merely that the run never
equilibrated. Two checks that separate them:

(1) EDGE OVERLAP. The anti-Born ground state condition is Tr(rho_x rho_y) = 0 on
    every edge. If <Tr> ~ 0 while the order parameter sits at the 1/sqrt(N)
    floor, the system HAS reached its ground-state manifold and is disordered
    inside it -- degeneracy, not slow dynamics. (Born's ground state is aligned,
    so its <Tr> must go to 1: that is the control.)

(2) ORDERED START. Begin from a perfect Neel state (A=|1>, B=|2>, every edge
    exactly orthogonal, so it IS a ground state) and watch the staggered order
    parameter. If a true ordered phase existed the Neel state would be stable;
    decay to the 1/sqrt(N) floor means the manifold is entropically dominated.

The degeneracy count, for the record: fix sublattice B to |2>. Every A site is
then free in the entire 3-dim orthogonal complement -- a whole CP^2 per site,
so dim(ground manifold) grows like N. Born's is a single CP^3, intensive.
"""
import numpy as np
def sweep(psi,L,d,w,rng,n=4):
    N=L**d
    for _ in range(N):
        pos=tuple(rng.integers(0,L,d))
        nb=[]
        for ax in range(d):
            for s in (1,-1):
                q=list(pos); q[ax]=(q[ax]+s)%L; nb.append(psi[tuple(q)])
        nb=np.array(nb); old=psi[pos]
        new=rng.normal(size=n)+1j*rng.normal(size=n); new/=np.linalg.norm(new)
        to=np.abs(nb@old.conj())**2; tn=np.abs(nb@new.conj())**2
        den=np.prod((1-w)*to+w*(1-to)); num=np.prod((1-w)*tn+w*(1-tn))
        if den<=0: continue
        if num>=den or rng.random()<num/den: psi[pos]=new
    return psi
def measure(psi,L,d,stag,n=4):
    N=L**d
    rho=psi[...,:,None]*psi[...,None,:].conj()-np.eye(n)/n
    U=np.linalg.norm(rho.sum(axis=tuple(range(d))))/N
    S=np.linalg.norm((rho*stag[...,None,None]).sum(axis=tuple(range(d))))/N
    ov=[]
    for ax in range(d):
        ov.append(np.mean(np.abs(np.sum(psi*np.roll(psi,1,axis=ax).conj(),axis=-1))**2))
    return U,S,float(np.mean(ov))
L,d,n=6,4,4; N=L**d; idx=np.indices((L,)*d); stag=(-1.0)**(sum(idx)%2)
print(f"CP^3 on Z^4, L={L}, N={N}, 1/sqrt(N) = {1/np.sqrt(N):.4f}\n")
print("(1) random start, edge overlap <Tr(rho_x rho_y)>")
print("      w     uniform  staggered  <Tr edge>   expected <Tr>")
for w in (0.0,1.0):
    rng=np.random.default_rng(3)
    psi=rng.normal(size=(L,)*d+(n,))+1j*rng.normal(size=(L,)*d+(n,))
    psi/=np.linalg.norm(psi,axis=-1,keepdims=True)
    for i in range(2200): psi=sweep(psi,L,d,w,rng)
    U,S,ov=measure(psi,L,d,stag)
    print(f"    {w:.1f}    {U:.5f}   {S:.5f}   {ov:.5f}     {'1 (aligned)' if w==0 else '0 (orthogonal)'}")
print("\n(2) NEEL start (A=|1>, B=|2>: an exact anti-Born ground state)")
print("     sweeps   uniform  staggered  <Tr edge>")
rng=np.random.default_rng(9)
psi=np.zeros((L,)*d+(n,),dtype=complex)
e1=np.zeros(n,dtype=complex); e1[0]=1; e2=np.zeros(n,dtype=complex); e2[1]=1
psi[stag>0]=e1; psi[stag<0]=e2
for tot in (0,50,200,600,1500):
    while True:
        U,S,ov=measure(psi,L,d,stag); break
    print(f"     {tot:5d}    {U:.5f}   {S:.5f}   {ov:.5f}")
    if tot<1500:
        nxt=(50,200,600,1500)[ (0,50,200,600).index(tot) ]
        for i in range(nxt-tot): psi=sweep(psi,L,d,1.0,rng)
print(f"\n  floor 1/sqrt(N) = {1/np.sqrt(N):.4f}")
