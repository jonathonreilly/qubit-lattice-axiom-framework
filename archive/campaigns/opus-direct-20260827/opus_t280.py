"""
T280 - does D run with scale at p = 0.85?  (R183 showed it runs 2.8x at p=0.70)

If D is scale-dependent there is no single D, the heat trace at moderate s is
governed by a different D than lambda_1 gives, and the collapse test is not
well-posed at that p.  R183 measured this at p=1.00/0.70/0.50 but not 0.85 --
the one density where the curvature measurement might be meaningful.

Method: D_n = lambda_n / khat_n^2 for the lowest transverse-momentum modes.
The p=1 column is NOT flat either -- that is the pure-lattice dispersion
curvature 2(1-cos k)/k^2, a known artifact -- so the DISORDER running is the
p<1 column divided by the p=1 column at the same n.  Reporting the raw column
without that division would read lattice curvature as disorder.
"""
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
from opus_t275 import build, giant

L=40; nmax=10
print(f"L={L}.  D_n = lambda_n/khat_n^2, khat_n = 2 sin(pi n/L) (lattice momentum)")
print("raw D_n, then normalised by the p=1 column (= disorder-induced running)\n")
raw={}
for p in (1.00,0.85,0.70):
    g=giant(L,p,11); idx=np.where(g)[0]
    A,m=build(L,0.0,g); ms=m[idx]
    Dm=diags(1.0/np.sqrt(ms)); B=(Dm@A[idx][:,idx]@Dm).tocsr()
    ev=np.sort(eigsh(B,k=60,sigma=-1e-6,which='LM',return_eigenvectors=False))
    ev=ev[ev>1e-9]
    # modes come in 6-fold plane-wave multiplets; take the multiplet minima
    lev=[];  last=-1
    for v in ev:
        if last<0 or v>last*1.06: lev.append(v); last=v
    D=[]
    for n in range(1,min(nmax,len(lev))+1):
        kh=2*np.sin(np.pi*n/L)
        D.append(lev[n-1]/kh**2)
    raw[p]=np.array(D)
    print(f"  p={p:.2f}  "+" ".join(f"{d:6.3f}" for d in D))
print()
for p in (0.85,0.70):
    n=min(len(raw[p]),len(raw[1.00]))
    r=raw[p][:n]/raw[1.00][:n]
    print(f"  p={p:.2f} / p=1.00 :  "+" ".join(f"{v:6.3f}" for v in r)
          +f"    running = {r.max()/r.min():.2f}x")
