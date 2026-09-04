"""
T264 - does the CURVATURE RESPONSE survive dilution?

R183 left one item: the induced Einstein-Hilbert coefficient was never computed
on a diluted lattice.  R183 also showed D runs with scale there, so any test must
be D-independent.  It can be:

    (4 pi D s)^{d/2} K_2(s) / Vol_2  =  1 + s (a1/a0) + ...

The SLOPE in s is a1/a0 -- the curvature response relative to the volume -- and
an overall error in D shifts the prefactor, not the slope's ratio to the
intercept.  So compare the ratio  slope/intercept  between complete and diluted
lattices.  If they agree, the curvature response survives dilution.

3D, conformal perturbation g = (1 + eps cos(kappa x0)) delta, weighted graph
Laplacian on the occupied sites, K_2 from a 5-point eps difference.
"""
import numpy as np, time
from numpy.polynomial.legendre import leggauss
XS, WS = leggauss(24)
def integ(f, lo, hi):
    lo=np.asarray(lo,float); hi=np.asarray(hi,float)
    p=0.5*(lo+hi)[:,None]+0.5*(hi-lo)[:,None]*XS[None,:]
    return 0.5*(hi-lo)*np.sum(WS[None,:]*f(p),axis=1)

L = 14
def heat(p_occ, eps, kappa, svals, seed=521):
    rng = np.random.default_rng(seed)
    occ = (rng.random((L,L,L)) < p_occ) if p_occ < 1.0 else np.ones((L,L,L),bool)
    t = np.arange(L, dtype=float)
    W  = lambda x: (1.0+eps*np.cos(kappa*x))**0.5    # sqrt(g) g^{mu mu} in d=3
    Rho= lambda x: (1.0+eps*np.cos(kappa*x))**1.5    # sqrt(g)
    w0 = integ(W, t, t+1.0); wt = integ(W, t-0.5, t+0.5); m = integ(Rho, t-0.5, t+0.5)
    sites=np.argwhere(occ); idx=-np.ones((L,L,L),int); idx[occ]=np.arange(len(sites))
    N=len(sites); A=np.zeros((N,N)); M=np.zeros(N)
    for a,(i,j,k) in enumerate(sites):
        M[a]=m[i]
        for ax,(di,dj,dk) in enumerate(((1,0,0),(0,1,0),(0,0,1))):
            q=((i+di)%L,(j+dj)%L,(k+dk)%L)
            if occ[q]:
                b=idx[q]; ww = w0[i] if ax==0 else wt[i]
                A[a,b]-=ww; A[b,a]-=ww; A[a,a]+=ww; A[b,b]+=ww
    isq=1/np.sqrt(M); B=(isq[:,None]*A)*isq[None,:]
    ev=np.maximum(np.linalg.eigvalsh(0.5*(B+B.T)),0)
    return np.array([np.sum(np.exp(-si*ev)) for si in svals]), M.sum(), N

def resp(p_occ, kappa, svals, h=0.06):
    out={}
    for e in (-2,-1,0,1,2):
        K,V,N = heat(p_occ, e*h, kappa, svals); out[e]=(K,V)
    K2 = 0.5*(-out[2][0]+16*out[1][0]-30*out[0][0]+16*out[-1][0]-out[-2][0])/(12*h*h)
    V2 = 0.5*(-out[2][1]+16*out[1][1]-30*out[0][1]+16*out[-1][1]-out[-2][1])/(12*h*h)
    return K2, V2, out[0][0], N

# n=2 put x = s kappa^2 in [1.2, 3.9]; R132 established the expansion needs
# x <~ 1, so the whole window was outside its range and the p=1 control failed.
kappa = 2*np.pi*1/L
s = np.array([1.5, 2.0, 2.7, 3.6, 4.8])
print(f"L={L}, 3D, conformal perturbation, kappa={kappa:.4f}, "
      f"x = s kappa^2 in [{1.5*kappa**2:.2f}, {4.8*kappa**2:.2f}]")
print("R(s) = (4 pi D s)^1.5 K_2 / Vol_2 ; slope/intercept of R vs s is a1/a0\n")
print(f"{'p':>5s} {'N':>6s} {'D':>7s}  {'R(s) across the window':>40s}  {'slope/icept':>12s}")
for p_occ in (1.00, 0.85, 0.70):
    t0=time.time()
    K2,V2,K0,N = resp(p_occ, kappa, s)
    # D from the flat spectrum's smallest non-zero mode
    Kf,_,_ = heat(p_occ, 0.0, kappa, np.array([1e6]))[0], None, None
    # simpler: get D by matching the flat heat trace at the largest s
    ev_probe = None
    Kflat,Vf,Nf = heat(p_occ, 0.0, kappa, s)
    D = np.median(((Nf/Kflat)**(2/3))/(4*np.pi*s))
    R = (4*np.pi*D*s)**1.5 * K2 / V2
    A_ = np.vstack([np.ones_like(s), s]).T
    c,*_ = np.linalg.lstsq(A_, R, rcond=None)
    print(f"{p_occ:5.2f} {N:6d} {D:7.4f}  " + " ".join(f"{q:7.4f}" for q in R)
          + f"  {c[1]/c[0]:12.5f}   [{time.time()-t0:.0f}s]")
