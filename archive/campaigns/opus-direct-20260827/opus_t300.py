"""
T300 - does the anti-Born branch survive at M4(C)?  The discriminator.

At M2(C) the two positivity endpoints are exchanged by the sublattice flip
v -> -v, i.e. rho -> I - rho, which maps pure states to pure states. Z^3 is
bipartite, so +lambda and -lambda are the SAME theory (T299).

At M4(C) that flip is rho -> I/2 - rho, whose eigenvalues on a pure state are
(-1/2, 1/2, 1/2, 1/2): NOT a state. So the equivalence must fail, and the two
branches are genuinely different theories.

Why that could settle it: the Born ground state is all-aligned -- unique up to a
global rotation, so it orders. The anti-Born ground state needs every edge
ORTHOGONAL; fixing sublattice B to |2>, each A site is free in the whole CP^2
orthogonal to it, an EXTENSIVE degeneracy. If that kills long-range order, then
R169's own criterion (the framework needs a continuum limit at all) selects the
Born weight uniquely at M4(C) -- and the Z^4 + M4(C) proposal would remove an
ambiguity that Z^3 + M2(C) leaves open.

phi = (1-w) Tr(rho rho') + w (1 - Tr(rho rho')):  w=0 Born, w=1 anti-Born.
Both are >= 0 for pure states at any n, since Tr(rho rho') in [0,1].
Controls: measure BOTH uniform and staggered order, so an ordered anti-Born
phase cannot be missed by looking in the wrong channel.
"""
import numpy as np
def run(L,w,n=4,sweeps=2600,burn=800,seed=7,d=4):
    rng=np.random.default_rng(seed)
    shape=(L,)*d; N=L**d
    psi=rng.normal(size=shape+(n,))+1j*rng.normal(size=shape+(n,))
    psi/=np.linalg.norm(psi,axis=-1,keepdims=True)
    idx=np.indices(shape); stag=(-1.0)**(sum(idx)%2)
    def nbrs(pos):
        out=[]
        for ax in range(d):
            for s in (1,-1):
                q=list(pos); q[ax]=(q[ax]+s)%L; out.append(psi[tuple(q)])
        return np.array(out)
    U=[];S=[]
    for sw in range(sweeps):
        for _ in range(N):
            pos=tuple(rng.integers(0,L,d))
            nb=nbrs(pos); old=psi[pos]
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
print("CP^3 (M4(C) pure states) on Z^4.  phi=(1-w)Tr + w(1-Tr):  w=0 Born, w=1 anti-Born")
print("order parameters normalised per site; a DISORDERED phase gives O(1/sqrt(N)).\n")
print("   w      L    uniform    staggered    1/sqrt(N)   verdict")
for w in (0.0,1.0):
    for L in (6,8):
        u,s=run(L,w); nn=1/np.sqrt(L**4)
        big=max(u,s)
        print(f"  {w:.1f}   {L:3d}   {u:.5f}    {s:.5f}     {nn:.5f}    "
              +("ORDERED" if big>3*nn else "disordered")+f"  ({'staggered' if s>u else 'uniform'} channel)")
