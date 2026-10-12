# R13-2 s5: semiclassical check of the sign-free model of s4 (q-basis, DeWitt lam=0, energetic G via xi, energetic S,
# compact N-type potential).  Find the classical static minimum of V(theta) = ks sum(1-cos S theta) + kB/2 sin.B_N.sin,
# then the harmonic frequencies about it (Lagrangian kinetic from beta_t (theta_dot + G^T xi)^2 + mu xi^2, xi integrated out).
# Lemma P predicts: at a true minimum (PSD Hessian), gapless TT implies gapless partners.  We count the soft modes.
import numpy as np, sys
from scipy.optimize import minimize
from common import *
import s4_hmc as S4
def build(L):
    kk=2*np.pi*np.fft.fftfreq(L)
    T=np.diag([1,1,1,1/np.sqrt(2),1/np.sqrt(2),1/np.sqrt(2)])
    offs=[np.zeros(3)]*3+[np.array([.5,.5,0]),np.array([0,.5,.5]),np.array([.5,0,.5])]
    M=np.zeros((L,L,L,6,6),complex)
    for i,a in enumerate(kk):
        for j,b in enumerate(kk):
            for l,c in enumerate(kk):
                k=np.array([a,b,c]); q=2*np.sin(k/2); P=np.diag([np.exp(-1j*k@o) for o in offs]); M[i,j,l]=P.conj().T@T@(-Rmap(q))@T@P
    return M
R=lambda f,s,ax: np.roll(f,s,axis=ax)
def Sop(q):
    out=np.zeros(q.shape[:-1])
    for j in range(3):
        for i in range(3):
            if i!=j: out+=R(q[...,j],-1,i)+R(q[...,j],1,i)-2*q[...,j]
    for a,(i,j) in zip((3,4,5),((0,1),(1,2),(0,2))):
        f=q[...,a]; out-= f-R(f,1,i)-R(f,1,j)+R(R(f,1,i),1,j)
    return out
def ST(s):
    out=np.zeros(s.shape+(6,))
    for j in range(3):
        for i in range(3):
            if i!=j: out[...,j]+=R(s,1,i)+R(s,-1,i)-2*s
    for a,(i,j) in zip((3,4,5),((0,1),(1,2),(0,2))):
        out[...,a]-= s-R(s,-1,i)-R(s,-1,j)+R(R(s,-1,i),-1,j)
    return out
def GT(xi):
    out=np.empty(xi.shape[:-1]+(6,))
    for j in range(3): out[...,j]=R(xi[...,j],1,j)-xi[...,j]
    for a,(i,j) in zip((3,4,5),((0,1),(1,2),(0,2))):
        out[...,a]=xi[...,j]-R(xi[...,j],-1,i)+xi[...,i]-R(xi[...,i],-1,j)
    return out
def run(L,kB,ks,beta_t,mu,starts=6,seed=0):
    rng=np.random.default_rng(seed); M=build(L); sh=(L,L,L,6)
    def BV(s):
        f=np.fft.fftn(s,axes=(0,1,2)); return np.fft.ifftn(np.einsum('xyzab,xyzb->xyza',M,f),axes=(0,1,2)).real
    def V(x):
        th=x.reshape(sh); s=np.sin(th); return ks*np.sum(1-np.cos(Sop(th)))+0.5*kB*np.sum(s*BV(s))
    def dV(x):
        th=x.reshape(sh); return (ks*ST(np.sin(Sop(th)))+kB*np.cos(th)*BV(np.sin(th))).ravel()
    best=None
    for st in range(starts):
        x0=rng.uniform(0,2*np.pi,np.prod(sh)) if st>0 else rng.normal(size=np.prod(sh))*0.05
        r=minimize(V,x0,jac=dV,method='L-BFGS-B',options={'maxiter':20000,'gtol':1e-10})
        if best is None or r.fun<best.fun: best=r
        print(f"   L={L} start {st}: V_min/site = {r.fun/L**3:+.5f}  |grad|={np.linalg.norm(dV(r.x)):.1e}"); sys.stdout.flush()
    x=best.x; th=x.reshape(sh); s=np.sin(th)
    # dominant Fourier content of the condensate
    F=np.abs(np.fft.fftn(s,axes=(0,1,2)))**2; tot=F.sum(axis=(-1))
    top=np.argsort(tot.ravel())[::-1][:3]; kk=[np.unravel_index(t,tot.shape) for t in top]
    print(f"   best V_min/site={best.fun/L**3:+.5f}; |sin| mean={np.mean(np.abs(s)):.3f}; dominant k (units 2pi/L): {kk} weights {np.round(tot.ravel()[top]/tot.sum(),3)}")
    # Hessian of V by finite differences of dV
    n=x.size; Hs=np.zeros((n,n)); h=1e-6
    for i in range(n):
        e=np.zeros(n); e[i]=h; Hs[:,i]=(dV(x+e)-dV(x-e))/(2*h)
    Hs=0.5*(Hs+Hs.T); ev=np.linalg.eigvalsh(Hs)
    # Lagrangian kinetic: beta_t (thd + GT xi)^2 + mu xi^2, minimise over xi -> K_L = beta_t*(I - beta_t*GT (beta_t G GT + mu)^{-1} G)
    nx=L**3*3; Gt=np.zeros((n,nx))
    for i in range(nx):
        e=np.zeros(nx); e[i]=1; Gt[:,i]=GT(e.reshape((L,L,L,3))).ravel()
    A=beta_t*Gt.T@Gt+mu*np.eye(nx); KL=beta_t*(np.eye(n)-beta_t*Gt@np.linalg.solve(A,Gt.T))
    # frequencies: KL thdd = -Hs theta  (Lagrangian KL/1 * thdot^2 normalisation: L = thd.KL.thd - V  -> omega^2 = eig(KL^{-1} Hs)/? )
    # action form beta_t(...)^2 is Euclidean 'K/2 thd^2' with K=2*KL ; potential V ~ (1/2) th.Hs.th  => omega^2 = eig(Hs, 2KL)
    import scipy.linalg as sl
    w2=sl.eigh(Hs,2*KL,eigvals_only=True)
    print(f"   Hessian eigs: min {ev.min():+.2e} (PSD at a minimum); #near-zero(|eig|<1e-6)={np.sum(np.abs(ev)<1e-6)} of {n}")
    w=np.sqrt(np.maximum(w2,0)); print(f"   lowest 24 harmonic frequencies: {np.round(np.sort(w)[:24],4)}")
    return np.sort(w)
if __name__=="__main__":
    kB,ks,bt,mu=[float(v) for v in sys.argv[1:5]]
    for L in [int(v) for v in sys.argv[5].split(',')]:
        print(f"== kB={kB} ks={ks} beta_t={bt} mu={mu} L={L}"); run(L,kB,ks,bt,mu)
