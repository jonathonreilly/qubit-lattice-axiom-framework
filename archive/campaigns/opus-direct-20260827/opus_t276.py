"""
T276 - measure D on the diluted lattice from the lowest nonzero mode.

The T275 intercept route is ill-conditioned (the 1/s artifact is degenerate with
the constant over a narrow x window) -- T274 shows the EXACT computation fails
the same way, so this is a conditioning problem, not dilution.

Independent route: the lowest nonzero eigenvector of B at eps=0 under periodic
BCs is a plane wave at k = 2pi/L, so
    D = lambda_1 * (L/2pi)^2.
At p=1 this has a known exact value, 2(1-cos(2pi/L))(L/2pi)^2 -> 1, giving a
calibration with no fitting at all.

Two soundness checks on each diluted measurement, because low-lying modes on a
disordered lattice can be LOCALISED (Lifshitz tails) rather than plane waves:
  - degeneracy: a k=2pi/L plane wave in 3D is 6-fold degenerate;
  - participation ratio: extended modes have PR = O(1), localised ones ~ 1/n.
"""
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
from opus_t275 import build, giant

print("D from lambda_1 (L/2pi)^2 at eps=0.   p=1 exact: 2(1-cos(2pi/L))(L/2pi)^2\n")
print("   L    p      n        lambda_1     D        exact(p=1)   6 lowest nonzero (/lam1)      PR")
for L in (40,56,72):
    for p in (1.00,0.85,0.70):
        g=giant(L,p,11); idx=np.where(g)[0]; n=len(idx)
        A,m=build(L,0.0,g); As=A[idx][:,idx]; ms=m[idx]
        Dm=diags(1.0/np.sqrt(ms)); B=(Dm@As@Dm).tocsr()
        ev,V=eigsh(B,k=8,sigma=-1e-6,which='LM')
        o=np.argsort(ev); ev=ev[o]; V=V[:,o]
        nz=[i for i in range(len(ev)) if ev[i]>1e-9]
        l1=ev[nz[0]]; D=l1*(L/(2*np.pi))**2
        ex=2*(1-np.cos(2*np.pi/L))*(L/(2*np.pi))**2
        v=V[:,nz[0]]; v=v/np.linalg.norm(v)
        pr=1.0/(n*np.sum(v**4))
        deg=" ".join(f"{ev[i]/l1:.3f}" for i in nz[:6])
        tag=f"  {ex:.5f}" if p>=1.0 else "        -"
        print(f"  {L:3d}  {p:.2f} {n:7d}   {l1:.6e}  {D:7.4f}  {tag}   {deg}   {pr:.3f}")
