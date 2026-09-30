# independent check: pair on a ring with uniform Peierls phase A on every hop of both walkers.
# E(A) = E_pair(K=2A) (translation-invariant by 2). W = E0 * d2E/dK2 = E0 * (d2E/dA2)/4
import numpy as np, scipy.linalg as la, sys
def h1(N,beta,m,A):
    H=np.zeros((N,N),complex)
    for x in range(N):
        y=(x+1)%N
        # S = (T - T^dag)/2i style with T psi(x)=psi(x-1): entry <y|S|x> = 1/(2i), <x|S|y> = -1/(2i); gauge phase
        H[y,x]+=beta/(2j)*np.exp(1j*A)
        H[x,y]+=-beta/(2j)*np.exp(-1j*A)
        H[x,x]+=m*(-1)**x
    return H
def Epair(N,beta,m,lam,A,kap=0.0):
    h=h1(N,beta,m,A); I=np.eye(N)
    H=np.kron(h,I)+np.kron(I,h)
    for x in range(N):
        H[x*N+x,x*N+x]+=-lam
        for y in ((x+1)%N,(x-1)%N):
            H[x*N+y,x*N+y]+=-lam*kap
    ev=la.eigvalsh(H)
    return ev[ev>0.6*m].min()
def Wpair(N,beta,m,lam,kap=0.0,dA=0.02):
    E0=Epair(N,beta,m,lam,0,kap)
    Ep=Epair(N,beta,m,lam,dA,kap); Em=Epair(N,beta,m,lam,-dA,kap)
    d2=(Ep+Em-2*E0)/dA**2/4
    return E0*d2,E0,d2
if __name__=="__main__":
    N=int(sys.argv[1]) if len(sys.argv)>1 else 40
    for m,lams in ((1.0,(0.2,0.4)),(0.5,(0.1,0.2,0.4)),(0.25,(0.05,0.1,0.2))):
        for lam in lams:
            W,E0,d2=Wpair(N,1.0,m,lam)
            B=2*m-E0
            print(f"N={N} m={m} lam={lam}: E0={E0:.5f} B={B:.5f} B/2m={B/2/m:.4f} W={W:.5f} (W-1)/(B/2m)={(W-1)/(B/2/m):.2f}",flush=True)
