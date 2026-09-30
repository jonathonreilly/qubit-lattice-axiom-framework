"""T72 falsifier: is there ONE local instantaneous interaction V = -lam(delta_r0 + kappa*delta_{|r|,1}) (timed) that gives
composite weight W = 1 for every bound state? Scan kappa for W=1 at several lam; if kappa*(lam) varies, W=1 is a tuning per bound state."""
import numpy as np, scipy.sparse as sp, scipy.linalg as la
from t72_stag import h1, pair_band_E
import t72_stag

def two_body_k(N, w, beta, m, e0, lam, timed, periodic, kappa):
    h=h1(N,w,beta,m,e0,periodic); I=sp.identity(N,format='csr',dtype=complex)
    H=sp.kron(h,I)+sp.kron(I,h)
    V=np.zeros(N*N)
    for x in range(N):
        V[x*N+x]=-lam*(w[x] if timed else 1.0)
        for y in ((x+1)%N,(x-1)%N):
            V[x*N+y]+=-lam*kappa*(np.sqrt(w[x]*w[y]) if timed else 1.0)
    return (H+sp.diags(V.astype(complex))).tocsr()

def W_of(lam,kappa,Nring=48,beta=1.0,m=1.0,e0=0.0):
    orig=t72_stag.two_body
    t72_stag.two_body=lambda N,w,b,mm,ee,l,t,periodic=False: two_body_k(N,w,b,mm,ee,l,t,periodic,kappa)
    try:
        M=Nring//2; Qs=[0.0,2*np.pi/M,-2*np.pi/M,4*np.pi/M,-4*np.pi/M]
        d=pair_band_E(Nring,lam,beta,m,e0,Qs,True)
    finally:
        t72_stag.two_body=orig
    E={Q:d[Q][d[Q]>2*e0+0.6*m].min() for Q in Qs}
    E0=E[0.0]; q1=2*np.pi/M; q2=4*np.pi/M
    s1=(E[q1]+E[-q1]-2*E0)/q1**2; s2=(E[q2]+E[-q2]-2*E0)/q2**2
    d2K=4*(4*s1-s2)/3
    return E0*d2K,E0

if __name__=="__main__":
    print("W_pair (timed) for V=-lam(delta_r0 + kappa delta_|r|1); m=beta=1 ring 48")
    print(" lam  kappa    E0      B=2m-E0    W")
    for lam in (0.15,0.3):
        for kappa in (0.0,0.5,1.0,2.0,-0.5,-1.0):
            W,E0=W_of(lam,kappa)
            print(f"{lam:4.2f} {kappa:5.2f} {E0:8.5f} {2-E0:8.5f}  {W:8.5f}")
