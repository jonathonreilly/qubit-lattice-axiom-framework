"""
T265 - R184's control, fixed: the curvature response at the lattice size the
channel actually needs.

R184's control failed (R -> 1.48, not 1) and R increased as s fell, which is the
lattice-artefact regime.  Diagnosis: L = 14 is far too small.  The packet already
records this -- R85: "There is no window at L <= 8 ... which is why the lane
needed L = 32/64."  I ran L = 14 without checking.

Dense diagonalisation cannot reach L = 32 (32768^2).  Stochastic trace estimation
can:  Tr f(Delta) ~ (1/M) sum_j z_j^T f(Delta) z_j  with Chebyshev for f = e^{-s D},
using the SAME probe vectors across all eps values so the eps^2 difference is
correlated and the noise largely cancels.
"""
import numpy as np, time
from scipy.sparse import coo_matrix
from numpy.polynomial.legendre import leggauss
XS, WS = leggauss(24)
def integ(f, lo, hi):
    lo=np.asarray(lo,float); hi=np.asarray(hi,float)
    p=0.5*(lo+hi)[:,None]+0.5*(hi-lo)[:,None]*XS[None,:]
    return 0.5*(hi-lo)*np.sum(WS[None,:]*f(p),axis=1)

def operator(L, p_occ, eps, kappa, seed=577):
    rng=np.random.default_rng(seed)
    occ=(rng.random((L,L,L))<p_occ) if p_occ<1.0 else np.ones((L,L,L),bool)
    t=np.arange(L,dtype=float)
    W=lambda x:(1.0+eps*np.cos(kappa*x))**0.5
    Rho=lambda x:(1.0+eps*np.cos(kappa*x))**1.5
    w0=integ(W,t,t+1.0); wt=integ(W,t-0.5,t+0.5); m=integ(Rho,t-0.5,t+0.5)
    sites=np.argwhere(occ); idx=-np.ones((L,L,L),int); idx[occ]=np.arange(len(sites))
    N=len(sites); M=m[sites[:,0]]
    r,c,v=[],[],[]
    diag=np.zeros(N)
    for ax,(di,dj,dk) in enumerate(((1,0,0),(0,1,0),(0,0,1))):
        nb=((sites[:,0]+di)%L,(sites[:,1]+dj)%L,(sites[:,2]+dk)%L)
        ok=occ[nb]; a=np.arange(N)[ok]; b=idx[nb[0][ok],nb[1][ok],nb[2][ok]]
        ww=(w0 if ax==0 else wt)[sites[a,0]]
        r+= list(a)+list(b); c+= list(b)+list(a); v+= list(-ww)+list(-ww)
        np.add.at(diag,a,ww); np.add.at(diag,b,ww)
    r+=list(range(N)); c+=list(range(N)); v+=list(diag)
    A=coo_matrix((v,(r,c)),shape=(N,N)).tocsr()
    isq=1/np.sqrt(M)
    return A, isq, M.sum(), N

def cheb_trace(A, isq, svals, Z, order=90, lmax=14.0):
    """Tr e^{-s B} on the probe set, B = diag(isq) A diag(isq)"""
    def Bmul(X): return isq[:,None]*(A @ (isq[:,None]*X))
    a, b = 0.0, lmax
    d, e = (b-a)/2, (b+a)/2
    out=[]
    for s in svals:
        k=np.arange(order+1)
        th=np.pi*(k+0.5)/(order+1)
        xk=np.cos(th)
        fk=np.exp(-s*(d*xk+e))
        cj=np.array([ (2.0/(order+1))*np.sum(fk*np.cos(j*th)) for j in range(order+1)])
        cj[0]/=2
        T0=Z.copy(); T1=(Bmul(Z)-e*Z)/d
        acc=cj[0]*T0 + cj[1]*T1
        for j in range(2, order+1):
            T2=2*(Bmul(T1)-e*T1)/d - T0
            acc += cj[j]*T2; T0,T1=T1,T2
        out.append(np.sum(Z*acc)/Z.shape[1])
    return np.array(out)

if __name__=="__main__":
    L=32; kappa=2*np.pi/L; s=np.array([4.0,6.0,9.0,13.0,18.0])
    print(f"L={L}, 3D, kappa={kappa:.4f}, x = s kappa^2 in "
          f"[{s[0]*kappa**2:.2f}, {s[-1]*kappa**2:.2f}]  (R132's window is x <~ 1)")
    print("stochastic trace, correlated probes.  R(s) -> 1 is the control.\n")
    print(f"{'p':>5s} {'N':>6s} {'D':>7s}   {'R(s)':>38s}")
    for p_occ in (1.00, 0.85, 0.70):
        t0=time.time(); h=0.06
        A0,isq0,V0,N = operator(L,p_occ,0.0,kappa)
        rng=np.random.default_rng(99)
        Z=rng.choice([-1.0,1.0], size=(N,24))
        Ks={}; Vs={}
        for ee in (-2,-1,0,1,2):
            A,isq,V,_=operator(L,p_occ,ee*h,kappa)
            Ks[ee]=cheb_trace(A,isq,s,Z); Vs[ee]=V
        K2=0.5*(-Ks[2]+16*Ks[1]-30*Ks[0]+16*Ks[-1]-Ks[-2])/(12*h*h)
        V2=0.5*(-Vs[2]+16*Vs[1]-30*Vs[0]+16*Vs[-1]-Vs[-2])/(12*h*h)
        Kf=cheb_trace(A0,isq0,s,Z)
        D=np.median(((N/Kf)**(2/3))/(4*np.pi*s))
        R=(4*np.pi*D*s)**1.5*K2/V2
        print(f"{p_occ:5.2f} {N:6d} {D:7.4f}   " + " ".join(f"{q:7.4f}" for q in R)
              + f"   [{time.time()-t0:.0f}s]")
