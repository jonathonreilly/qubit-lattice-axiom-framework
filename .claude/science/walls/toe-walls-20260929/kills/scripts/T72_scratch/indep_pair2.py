import numpy as np, sys
import indep_pair as ip
import scipy.linalg as la
def Epair(N,beta,m,lam,A,kap=0.0):
    h=ip.h1(N,beta,m,A); I=np.eye(N)
    H=np.kron(h,I)+np.kron(I,h)
    for x in range(N):
        H[x*N+x,x*N+x]+=-lam
        for y in ((x+1)%N,(x-1)%N):
            H[x*N+y,x*N+y]+=-lam*kap
    ev=la.eigvalsh(H)
    return ev[ev>1.2*m].min()   # two-positive branch
def W(N,beta,m,lam,kap=0.0,dA=0.02):
    E0=Epair(N,beta,m,lam,0,kap);Ep=Epair(N,beta,m,lam,dA,kap);Em=Epair(N,beta,m,lam,-dA,kap)
    return E0*(Ep+Em-2*E0)/dA**2/4,E0
N=int(sys.argv[1])
m=1.0
for beta in (1.0,0.5,0.35):
    Wfree=beta**2
    for lam in ([0.2,0.4] if beta==1.0 else [0.05,0.1,0.15]):
        lam2=lam*beta**2 if beta!=1.0 else lam
        w,E0=W(N,beta,m,lam2)
        B=2*m-E0
        print(f"N={N} beta={beta} m={m} lam={lam2:.4f}: B/2m={B/2/m:.5f} W/beta^2={w/Wfree:.5f} coeff (W/beta^2-1)/(B/2m)={(w/Wfree-1)/(B/2/m):.3f}",flush=True)
