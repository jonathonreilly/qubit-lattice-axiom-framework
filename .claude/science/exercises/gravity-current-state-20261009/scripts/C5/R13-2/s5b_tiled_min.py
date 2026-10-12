# R13-2 s5b: as s5, but the minimum is found on a 2^3 cell (many starts) and tiled to L=4,6,8, then re-minimised;
# harmonic frequencies about the tiled (period-2) condensate.
import numpy as np, sys, scipy.linalg as sl
from scipy.optimize import minimize
import s5_classical_min as S5
kB,ks,bt,mu=[float(v) for v in sys.argv[1:5]]
rng=np.random.default_rng(1)
def setup(L):
    M=S5.build(L); sh=(L,L,L,6)
    def BV(s):
        f=np.fft.fftn(s,axes=(0,1,2)); return np.fft.ifftn(np.einsum('xyzab,xyzb->xyza',M,f),axes=(0,1,2)).real
    V=lambda x: ks*np.sum(1-np.cos(S5.Sop(x.reshape(sh))))+0.5*kB*np.sum(np.sin(x.reshape(sh))*BV(np.sin(x.reshape(sh))))
    dV=lambda x: (ks*S5.ST(np.sin(S5.Sop(x.reshape(sh))))+kB*np.cos(x.reshape(sh))*BV(np.sin(x.reshape(sh)))).ravel()
    return V,dV,sh
V2,dV2,sh2=setup(2); best=None
for st in range(200):
    r=minimize(V2,rng.uniform(0,2*np.pi,48),jac=dV2,method='L-BFGS-B',options={'maxiter':5000,'gtol':1e-12})
    if best is None or r.fun<best.fun: best=r
print(f"2^3 cell: best V/site={best.fun/8:+.5f}")
cell=best.x.reshape(sh2)
for L in (4,6,8):
    V,dV,sh=setup(L); x0=np.tile(cell,(L//2,L//2,L//2,1)).ravel()
    r=minimize(V,x0,jac=dV,method='L-BFGS-B',options={'maxiter':20000,'gtol':1e-12})
    x=r.x; n=x.size
    Hs=np.zeros((n,n)); h=1e-6
    for i in range(n):
        e=np.zeros(n); e[i]=h; Hs[:,i]=(dV(x+e)-dV(x-e))/(2*h)
    Hs=0.5*(Hs+Hs.T); ev=np.linalg.eigvalsh(Hs)
    nx=L**3*3; Gt=np.zeros((n,nx))
    for i in range(nx):
        e=np.zeros(nx); e[i]=1; Gt[:,i]=S5.GT(e.reshape((L,L,L,3))).ravel()
    A=bt*Gt.T@Gt+mu*np.eye(nx); KL=bt*(np.eye(n)-bt*Gt@np.linalg.solve(A,Gt.T))
    w=np.sqrt(np.maximum(sl.eigh(Hs,2*KL,eigvals_only=True),0))
    print(f"L={L}: V/site tiled={V(x0)/L**3:+.5f} reminimised={r.fun/L**3:+.5f} |grad|={np.linalg.norm(dV(x)):.1e}; Hessian min eig {ev.min():+.3e}; lowest 8 omega {np.round(np.sort(w)[:8],4)}; #omega<0.1: {np.sum(w<0.1)}")
    sys.stdout.flush()
