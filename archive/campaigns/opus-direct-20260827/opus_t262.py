"""
T262 - does the Seeley-DeWitt STRUCTURE survive dilution?

R181 showed the arena stays connected and diffusive above percolation, and
flagged that the gravity coefficient itself was never recomputed there.  The
foundation of R132/R135 is the expansion

      (4 pi s)^{d/2} K(s) / Vol  =  1 + s a1 + s^2 a2 + ...

Its ZEROTH term is the cheap and decisive test: with D measured independently
from the spectrum (lambda_1 = D khat^2, R181), does

      V(s) = (4 pi D s)^{3/2} K(s) / N   ->  1

on a plateau?  If yes, the diffusive continuum structure the gravity result is
built on survives dilution.  If not, the result is conditional on a complete
lattice -- an assumption the axioms do not make.

D is NOT fitted here; it comes from lambda_1.  So V(s) -> 1 is a genuine
prediction, not a tautology.
"""
import numpy as np, time
L = 16

def build(p, seed=487):
    rng = np.random.default_rng(seed)
    occ = (rng.random((L,L,L)) < p) if p < 1.0 else np.ones((L,L,L), bool)
    sites = np.argwhere(occ); idx=-np.ones((L,L,L),int); idx[occ]=np.arange(len(sites))
    N=len(sites); A=np.zeros((N,N))
    for a,(i,j,k) in enumerate(sites):
        for di,dj,dk in ((1,0,0),(0,1,0),(0,0,1)):
            q=((i+di)%L,(j+dj)%L,(k+dk)%L)
            if occ[q]:
                b=idx[q]; A[a,b]-=1; A[b,a]-=1; A[a,a]+=1; A[b,b]+=1
    return A,N

kh2 = 4*np.sin(np.pi/L)**2
print(f"L={L}, Z^3.  D from lambda_1 (NOT fitted); then V(s) = (4 pi D s)^1.5 K(s)/N")
print("V(s) -> 1 on a plateau  =>  the Seeley-DeWitt structure survives\n")
for p in (1.00, 0.70, 0.50):
    A,N = build(p)
    ev = np.sort(np.maximum(np.linalg.eigvalsh(A),0))
    nz = ev[ev>=1e-9]; D = nz[0]/kh2
    smax = L*L/(4*np.pi*D)
    s = np.geomspace(1.5, min(0.5*smax, 40), 8)
    K = np.array([np.sum(np.exp(-si*ev)) for si in s])
    V = (4*np.pi*D*s)**1.5 * K / N
    print(f"  p={p:4.2f}  N={N:5d}  D={D:.4f}  (window s < {0.5*smax:.0f})")
    print("     s   : " + " ".join(f"{q:8.2f}" for q in s))
    print("     V(s): " + " ".join(f"{q:8.4f}" for q in V))
    mid = V[(s>2)&(s<0.3*smax)]
    if len(mid): print(f"     plateau over the inner window: {mid.min():.4f} .. {mid.max():.4f}")
    print()
