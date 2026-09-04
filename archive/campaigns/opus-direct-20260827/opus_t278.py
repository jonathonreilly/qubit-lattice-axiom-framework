"""
T278 - D by LOBPCG (matrix-free) at every L, and the final collapse.

T277 stored the RAYLEIGH D for the collapse. That is a variational UPPER bound:
exact at p=1 (agrees with the eigensolver to 1.00000) but 12% high at p=0.85
and 35% high at p=0.70, because the true low mode relaxes around the holes.
The eigensolver value is the right one; get it at every L with LOBPCG seeded by
the plane wave (matrix-free, no shift-invert factorisation at L=72).

Then the collapse test with the corrected D, using T277's saved raw Rtil.
"""
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import lobpcg, eigsh
from opus_t275 import build, giant, R_cont

def D_lobpcg(L,p,seed=11):
    g=giant(L,p,seed); idx=np.where(g)[0]; n=len(idx)
    A,m=build(L,0.0,g); As=A[idx][:,idx]; ms=m[idx]
    Dm=diags(1.0/np.sqrt(ms)); B=(Dm@As@Dm).tocsr()
    i,_,_=np.indices((L,L,L)); x0=i.ravel()[idx]
    sq=np.sqrt(ms)
    X=np.column_stack([np.cos(2*np.pi*x0/L)*sq, np.sin(2*np.pi*x0/L)*sq,
                       np.cos(2*np.pi*x0/L+1.0)*sq, np.random.default_rng(5).normal(size=n)])
    Y=sq.reshape(-1,1)/np.linalg.norm(sq)        # deflate the exact zero mode
    X=X-Y@(Y.T@X); X,_=np.linalg.qr(X)
    ev,_=lobpcg(B,X,Y=Y,largest=False,tol=1e-10,maxiter=800)
    return float(np.min(ev))*(L/(2*np.pi))**2, n

print("D by LOBPCG (plane-wave seeded, zero mode deflated)")
print("   L    p      n        D(lobpcg)    D(eigsh)   agree      p=1 exact")
Dd={}
for L in (40,56,72):
    for p in (1.00,0.85,0.70):
        dl,n=D_lobpcg(L,p); Dd[(L,p)]=dl
        if L<=56:
            g=giant(L,p,11); idx=np.where(g)[0]; A,m=build(L,0.0,g)
            Dm=diags(1.0/np.sqrt(m[idx])); B=(Dm@A[idx][:,idx]@Dm).tocsr()
            ev=np.sort(eigsh(B,k=8,sigma=-1e-6,which='LM',return_eigenvectors=False))
            de=float(ev[ev>1e-9][0])*(L/(2*np.pi))**2
            ag=f"{dl/de:.5f}"
        else: de=float('nan'); ag="   -"
        ex=f"{2*(1-np.cos(2*np.pi/L))*(L/(2*np.pi))**2:.5f}" if p>=1.0 else "    -"
        print(f"  {L:3d}  {p:.2f} {n:7d}   {dl:9.5f}  {de:9.5f}   {ag}    {ex}")
np.save("t278_D.npy",np.array([[Dd[(L,p)] for p in (1.00,0.85,0.70)] for L in (40,56,72)]))
