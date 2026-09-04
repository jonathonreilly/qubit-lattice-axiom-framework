"""
T269 - EXACT d=3 Bloch diagonalisation, convergence at FIXED x.

The metric depends only on x0, so (q_y,q_z) are good quantum numbers: the
operator block-diagonalises into L^2 matrices of size LxL. This is the exact
method that made the d=4 code known-good (T200) -- no Chebyshev, no stochastic
noise, no spectral-bound assumption.

Test: R_cont(x) is L-independent (the continuum problem has the single scale
kappa, so it depends on s*kappa^2 alone). So at FIXED x, R_lat -> R_cont as
L grows is a pure finite-lattice convergence statement.
"""
import numpy as np, time
from numpy.polynomial.legendre import leggauss
XS, WS = leggauss(24)
def integ(f, lo, hi):
    lo=np.asarray(lo,float); hi=np.asarray(hi,float)
    p=0.5*(lo+hi)[:,None]+0.5*(hi-lo)[:,None]*XS[None,:]
    return 0.5*(hi-lo)*np.sum(WS[None,:]*f(p),axis=1)

def heat3(L, eps, svals):
    """exact Tr e^{-s B} in d=3 by Bloch decomposition over (qy,qz)."""
    kappa=2*np.pi/L; t=np.arange(L,dtype=float)
    W  =lambda x:(1.0+eps*np.cos(kappa*x))**0.5    # f^{d/2-1}, d=3
    Rho=lambda x:(1.0+eps*np.cos(kappa*x))**1.5    # f^{d/2},   d=3
    w=integ(W,t,t+1.0); v=integ(W,t-0.5,t+0.5); m=integ(Rho,t-0.5,t+0.5)
    idx=np.arange(L); isq=1.0/np.sqrt(m)
    K0=np.zeros((L,L))
    K0[idx,idx]=w+np.roll(w,1)
    jp=(idx+1)%L
    K0[idx,jp]-=w; K0[jp,idx]-=w
    q=2*np.pi*np.arange(L)/L; c2=2*(1-np.cos(q))
    tot=np.zeros(len(svals))
    for a in range(L):
        for b in range(L):
            Q=c2[a]+c2[b]
            K=K0.copy(); K[idx,idx]+=Q*v
            B=K*isq[:,None]*isq[None,:]
            ev=np.linalg.eigvalsh(B)
            tot+=np.array([np.sum(np.exp(-sv*ev)) for sv in svals])
    return tot, m.sum()*L*L

def R_of(L, xs, h=0.05):
    kappa=2*np.pi/L; s=xs/kappa**2
    Ks={};Vs={}
    for e in (-2,-1,0,1,2):
        Ks[e],Vs[e]=heat3(L,e*h,s)
    d2=lambda D:0.5*(-D[2]+16*D[1]-30*D[0]+16*D[-1]-D[-2])/(12*h*h)
    return (4*np.pi*s)**1.5*d2(Ks)/d2(Vs), d2(Vs)

# continuum reference (T266): depends on x alone
Rcont={0.20:1.05038, 0.35:1.09533}
xs=np.array([0.20,0.35])
print("exact Bloch, d=3.   R_cont(0.20)=1.05038   R_cont(0.35)=1.09533")
print("\n   L      s(x=.20)  s(x=.35)   R(0.20)    R(0.35)    ratio.20  ratio.35")
for L in (16,24,32,40,56,72):
    t0=time.time(); R,V2=R_of(L,xs); kap=2*np.pi/L
    print(f"  {L:3d}   {0.20/kap**2:8.2f} {0.35/kap**2:8.2f}   "
          f"{R[0]:8.5f}  {R[1]:8.5f}   {R[0]/Rcont[0.20]:8.4f} {R[1]/Rcont[0.35]:8.4f}   [{time.time()-t0:.0f}s]")
