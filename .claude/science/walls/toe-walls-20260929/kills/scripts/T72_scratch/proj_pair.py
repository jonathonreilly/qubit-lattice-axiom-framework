# positive-band projected pair (Salpeter-like): contact attraction -lam delta(x1,x2), whole-generator timed => rest at w=1.
import numpy as np, scipy.linalg as la, sys
import indep_pair as ip
def Ep(N,beta,m,lam,A):
    h=ip.h1(N,beta,m,A); ev,U=la.eigh(h); Up=U[:,ev>0]; ep=ev[ev>0]
    n=Up.shape[1]
    # V in product basis: <a b|V|c d> = -lam sum_x conj(Ua[x]) conj(Ub[x]) Uc[x] Ud[x]
    # build tensor
    T=np.einsum('xa,xc->xac',Up.conj(),Up)  # x, a, c
    Vm=-lam*np.einsum('xac,xbd->abcd',T,T)
    H=Vm.reshape(n*n,n*n)+np.diag((ep[:,None]+ep[None,:]).reshape(-1))
    return la.eigvalsh(H).min()
def W(N,beta,m,lam,dA=0.02):
    E0=Ep(N,beta,m,lam,0);a=Ep(N,beta,m,lam,dA);b=Ep(N,beta,m,lam,-dA)
    return E0*(a+b-2*E0)/dA**2/4,E0
N=int(sys.argv[1])
for m,beta in ((1.0,1.0),(0.5,1.0),(0.25,1.0)):
    for lam in (0.1,0.2,0.4):
        w,E0=W(N,beta,m,lam); B=2*m-E0
        print(f"N={N} m={m} beta={beta} lam={lam}: B/2m={B/2/m:.4f} W={w:.5f} coeff (W-1)/(B/2m)={(w-1)/(B/2/m):.2f}",flush=True)
