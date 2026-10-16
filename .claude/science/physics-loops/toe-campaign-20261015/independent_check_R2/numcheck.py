# numerical sanity: parametrization gives real u0,u with correct covariance (explicit spin-1/2 lift D(R))
import pickle, numpy as np, sympy as sp, itertools
from scipy.linalg import expm
d=pickle.load(open('param.pkl','rb')); params=d['params']; c0=d['c0']; cu=d['cu']
rng=np.random.default_rng(1)
vals={p:rng.normal() for p in params}
modes=list(c0)
C0=np.array([complex(sp.N(c0[n].subs(vals))) for n in modes])
CU=np.array([[complex(sp.N(cu[n][j].subs(vals))) for j in range(3)] for n in modes])
M=np.array(modes)
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1]);S=[sx,sy,sz]
def V(k):
    ph=np.exp(1j*M@k); u0=C0@ph; u=ph@CU
    return u0,u, u0*np.eye(2)+1j*sum(u[j]*S[j] for j in range(3))
def lift(R):
    w,v=np.linalg.eig(R); i=np.argmin(abs(w-1)); ax=np.real(v[:,i]); ax/=np.linalg.norm(ax)
    th=np.arccos(np.clip((np.trace(R)-1)/2,-1,1))
    for t in (th,-th):
        D=expm(-1j*t/2*sum(ax[j]*S[j] for j in range(3)))
        ok=all(np.allclose(D@S[j]@D.conj().T, sum(R[i,j]*S[i] for i in range(3))) for j in range(3))
        if ok: return D
    raise
G=[]
for p in itertools.permutations(range(3)):
    for s in itertools.product([1,-1],repeat=3):
        Rm=np.zeros((3,3))
        for i in range(3): Rm[i,p[i]]=s[i]
        if np.linalg.det(Rm)>0: G.append(Rm)
err=0;imag=0
for _ in range(20):
    k=rng.uniform(-np.pi,np.pi,3); u0,u,Vk=V(k); imag=max(imag,abs(u0.imag),*abs(u.imag))
    for R in G:
        D=lift(R); err=max(err,np.abs(V(R@k)[2]-D@Vk@D.conj().T).max())
print("max imag part",imag,"max covariance error",err)
