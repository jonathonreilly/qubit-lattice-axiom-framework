"""K2 (kill check): re-run of the attacker's IPR analysis with (a) a scan of the IPR cut, (b) the edge-pinning
diagnostic (how many eigenvalues sit exactly at the ideal edges 0 and c), (c) larger L, (d) the density of
extended states in the outer part of the gap.  Reuses only the attacker's walker builder and Wolff sampler."""
import sys, time, numpy as np
from t21_common import *
L=int(sys.argv[1]); nsamp=int(sys.argv[2]); c=float(sys.argv[3]); g=float(sys.argv[4])
N=L**3; nb=neighbours(L); eps=eps_array(L).astype(np.int8); H0=walker_H0(L)
K=np.log(1/g)/4; pb=1-np.exp(-2*K); seed_numba(4242+L); sig=np.ones(N,dtype=np.int8); wolff_steps(sig,nb,pb,500,0)
print(f"L={L} c={c} g={g} samples={nsamp}")
for t in range(nsamp):
    wolff_steps(sig,nb,pb,40,0); s=sig.copy()
    if s.sum()<0: s=-s
    n=(1+eps*s)//2; nfl=int((s==-1).sum())
    d=np.repeat(n.astype(float),2)*c
    t0=time.time(); E,V=np.linalg.eigh(H0+np.diag(d))
    rho=(np.abs(V)**2).reshape(N,2,-1).sum(axis=1); ipr=(rho**2).sum(axis=0)*N
    pin0=int((abs(E)<1e-8).sum()); pinc=int((abs(E-c)<1e-8).sum())
    win=(E>0.1*c)&(E<0.9*c); outer=(E>1e-8)&(E<0.1*c)|((E>0.9*c)&(E<c-1e-8))
    line=f"flipped={nfl:3d} exact-edge states: E=0:{pin0} E=c:{pinc} | in (0.1c,0.9c): {int(win.sum())} states; IPR*N median={np.median(ipr[win]) if win.any() else float('nan'):.1f} min={ipr[win].min() if win.any() else float('nan'):.1f}"
    for cut in (3,5,10,20):
        line+=f" | ext(cut{cut}):{int((win&(ipr<=cut)).sum())}"
    # outer strips: states with 0<E<0.1c or 0.9c<E<c
    line+=f" | strip states(0,0.1c)+(0.9c,c): {int(outer.sum())}, of which IPR*N<=10: {int((outer&(ipr<=10)).sum())}"
    # lowest non-pinned extended state distance from the ideal edge
    ext=(ipr<=10)&(abs(E)>1e-8)&(abs(E-c)>1e-8)&(E>-0.5*c)&(E<1.5*c)
    inside=ext&(E>0)&(E<c)
    dmin=np.min(np.minimum(E[inside],c-E[inside])) if inside.any() else float('nan')
    line+=f" | nearest extended non-pinned state to an edge: {dmin/(c/2):.3f} (c/2 units) ({time.time()-t0:.0f}s)"
    print(line); sys.stdout.flush()
