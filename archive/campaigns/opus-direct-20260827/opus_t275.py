"""
T275 - does induced Einstein-Hilbert survive DILUTION?  Curve-collapse test.

The question R182 left open and R184-R187 never reached, asked with the
machinery R188 validated.

No slope is extracted (R188's chord/tangent trap) and no separate D-estimator
is used (R184/R185's was wrong by 3.6-5% even at p=1, where D=1 exactly):
    Rtil(s) = (4 pi s)^{3/2} K2/V2 = D^{-3/2} R_cont(D x),   x = s kappa^2.
D comes from the x->0 intercept of the SAME fit, then the whole diluted curve
must collapse onto the exact continuum function R_cont measured in T266:
    D^{3/2} Rtil(x)  ==  R_cont(D x).

Controls: (i) p=1.00 through the identical stochastic pipeline must reproduce
the exact Bloch answer and return D=1; (ii) disorder realisation AND probe
vectors held fixed across eps so the eps^2 difference is correlated.
"""
import numpy as np, time
from scipy.sparse import coo_matrix, diags
from scipy.sparse.csgraph import connected_components
from numpy.polynomial.legendre import leggauss
XS,WS=leggauss(24)
def integ(f,lo,hi):
    lo=np.asarray(lo,float); hi=np.asarray(hi,float)
    q=0.5*(lo+hi)[:,None]+0.5*(hi-lo)[:,None]*XS[None,:]
    return 0.5*(hi-lo)*np.sum(WS[None,:]*f(q),axis=1)

def build(L,eps,keep):
    kap=2*np.pi/L; t=np.arange(L,dtype=float)
    W  =lambda x:(1.0+eps*np.cos(kap*x))**0.5
    Rho=lambda x:(1.0+eps*np.cos(kap*x))**1.5
    w0=integ(W,t,t+1.0); wt=integ(W,t-0.5,t+0.5); m=integ(Rho,t-0.5,t+0.5)
    i,j,k=np.indices((L,L,L)); flat=lambda a,b,c:((a%L)*L+(b%L))*L+(c%L)
    N=L**3; a=flat(i,j,k).ravel(); x0=i.ravel()
    r,c,v=[],[],[]; dg=np.zeros(N)
    for ax,(di,dj,dk) in enumerate(((1,0,0),(0,1,0),(0,0,1))):
        b=flat(i+di,j+dj,k+dk).ravel(); ww=(w0 if ax==0 else wt)[x0]
        live=keep[a]&keep[b]
        aa,bb,ww=a[live],b[live],ww[live]
        r+=list(aa)+list(bb); c+=list(bb)+list(aa); v+=list(-ww)+list(-ww)
        np.add.at(dg,aa,ww); np.add.at(dg,bb,ww)
    r+=list(range(N)); c+=list(range(N)); v+=list(dg)
    return coo_matrix((v,(r,c)),shape=(N,N)).tocsr(), m[x0]

def giant(L,p,seed):
    N=L**3
    if p>=1.0: return np.ones(N,bool)
    rng=np.random.default_rng(seed); keep=rng.random(N)<p
    A,_=build(L,0.0,keep); idx=np.where(keep)[0]
    nc,lab=connected_components(A[idx][:,idx],directed=False)
    big=np.argmax(np.bincount(lab))
    g=np.zeros(N,bool); g[idx[lab==big]]=True; return g

def cheb_trace(B,svals,Z,lmax):
    """Hutchinson: Tr f(B) ~ mean_z z^T f(B) z  (Rademacher z)."""
    order=int(1.35*max(svals)*lmax/2)+70
    d=e=lmax/2; nz=Z.shape[1]
    kk=np.arange(order+1); th=np.pi*(kk+0.5)/(order+1); xk=np.cos(th)
    C=np.zeros((len(svals),order+1))
    for a,sv in enumerate(svals):
        fk=np.exp(-sv*(d*xk+e))
        C[a]=[(2.0/(order+1))*np.sum(fk*np.cos(q*th)) for q in range(order+1)]
        C[a,0]/=2
    T0=Z.copy(); T1=(B@Z-e*Z)/d
    out=C[:,0]*(np.sum(Z*T0)/nz)+C[:,1]*(np.sum(Z*T1)/nz)
    for q in range(2,order+1):
        T2=2*(B@T1-e*T1)/d-T0
        out+=C[:,q]*(np.sum(Z*T2)/nz); T0,T1=T1,T2
    return out

def Rtil(L,p,xs,seed=11,nz=32,h=0.05):
    kap=2*np.pi/L; s=xs/kap**2
    g=giant(L,p,seed); idx=np.where(g)[0]; n=len(idx)
    rng=np.random.default_rng(101); Z=rng.choice([-1.0,1.0],size=(n,nz))
    Ks={};Vs={}
    for ei in (-2,-1,0,1,2):
        A,m=build(L,ei*h,g)
        As=A[idx][:,idx]; ms=m[idx]
        Dm=diags(1.0/np.sqrt(ms)); B=(Dm@As@Dm).tocsr()
        lmax=float(abs(B).sum(axis=1).max())*1.02      # Gershgorin bound, safe
        Ks[ei]=cheb_trace(B,s,Z,lmax); Vs[ei]=ms.sum()
    d2=lambda D:0.5*(-D[2]+16*D[1]-30*D[0]+16*D[-1]-D[-2])/(12*h*h)
    return (4*np.pi*s)**1.5*d2(Ks)/d2(Vs), n

# exact continuum R_cont(x) from T266 (spline through the measured values)
_xc=np.array([0.0,0.05,0.10,0.20,0.35,0.50])
_rc=np.array([1.0,1.01150,1.02374,1.05038,1.09533,1.14569])
_cf=np.polyfit(_xc,_rc-1.0,3)
R_cont=lambda x: 1.0+np.polyval(_cf,x)

if __name__=="__main__":
    xs=np.array([0.10,0.16,0.24,0.34,0.46])
    print("Rtil(x) = D^{-3/2} R_cont(D x).   D from the x->0 intercept of the same fit.\n")
    for L in (40,56,72):
        print(f"--- L = {L} ---")
        for p in (1.00,0.85,0.70):
            t0=time.time(); R,n=Rtil(L,p,xs)
            # intercept: Rtil = A + B x + C x^2 + E/s ; s = x/kap^2 so E/s ~ (kap^2 E)/x
            kap=2*np.pi/L; s=xs/kap**2
            M=np.vstack([np.ones_like(xs),xs,xs**2,1.0/s]).T
            A=np.linalg.lstsq(M,R,rcond=None)[0][0]
            D=A**(-2.0/3.0)
            coll=D**1.5*R; tgt=R_cont(D*xs)
            print(f"  p={p:.2f}  n={n:7d}  A={A:7.4f}  D={D:7.4f}   "
                  f"collapse D^1.5*Rtil / R_cont(Dx): "
                  +" ".join(f"{c/t:.3f}" for c,t in zip(coll,tgt))+f"   [{time.time()-t0:.0f}s]")
