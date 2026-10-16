# numeric search on complexified system U V = I (V independent) using exact basis evaluated numerically
import numpy as np, pickle, sys, itertools
from scipy.optimize import least_squares
from exact_setup import Alg, perm_rep2
eb=pickle.load(open(sys.argv[1],'rb')); m=int(sys.argv[2])  # m = second factor size
# build numeric matrices: q basis 2x2 complex
I2=np.eye(2); sx=np.array([[0,1],[1,0]]); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1.,-1])
Q=[I2,1j*sx,1j*sy,1j*sz]
def mat(b):
    a,i,j=b; E=np.zeros((m,m)); E[i,j]=1; return np.kron(Q[a],E)
offs=sorted({n for el in eb for n in el})
d=2*m; L=len(offs); oi={n:t for t,n in enumerate(offs)}
Bm=np.zeros((len(eb),L,d,d),complex)
for t,el in enumerate(eb):
    for n,dd in el.items():
        for b,c in dd.items(): Bm[t,oi[n]]+=float(c)*mat(b)
R=max(max(abs(x) for x in n) for n in offs); M=4*R+1
def grid(c):
    A=np.einsum('t,tnab->nab',c,Bm); G=np.zeros((M,M,M,d,d),complex)
    for n,t in oi.items(): G[n[0]%M,n[1]%M,n[2]%M]=A[t]
    return np.fft.fftn(G,axes=(0,1,2))
nb=len(eb); UNIT=len(sys.argv)>5
def res(x):
    c=x[:nb]+1j*x[nb:2*nb]; e=x[2*nb:3*nb]+1j*x[3*nb:]
    FU=grid(c); FV=np.conj(np.transpose(FU,(0,1,2,4,3))) if UNIT else grid(e)
    P=np.einsum('...ab,...bc->...ac',FU,FV)-np.eye(d); P2=np.einsum('...ab,...bc->...ac',FV,FU)-np.eye(d)
    o=np.concatenate([P.ravel(),P2.ravel()]); return np.concatenate([o.real,o.imag])
rng=np.random.default_rng(int(sys.argv[4]))
const=[t for t,el in enumerate(eb) if (0,0,0) in el]
for tr in range(int(sys.argv[3])):
    x0=rng.normal(size=4*nb)*rng.uniform(0.1,1.5)
    s=least_squares(res,x0,max_nfev=4000,xtol=1e-15,ftol=1e-15,gtol=1e-15)
    c=s.x[:nb]+1j*s.x[nb:2*nb]
    mov=np.linalg.norm([c[t] for t in range(nb) if t not in const])
    print(tr,'res %.2e mov %.3e'%(np.linalg.norm(s.fun),mov),flush=True)
    if np.linalg.norm(s.fun)<1e-9 and mov>1e-4: np.save('cplx_sol_%s_%d.npy'%(sys.argv[1].split('.')[0],tr),s.x)
