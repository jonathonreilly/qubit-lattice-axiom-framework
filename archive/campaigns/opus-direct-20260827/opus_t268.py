"""
T268 - is the Chebyshev spectral bound violated?

T200 (d=4, known good) diagonalised EXACTLY. T264/T265 (d=3, gives ~4/3)
introduced stochastic trace + Chebyshev with a hard-coded lmax=14.0.
Chebyshev diverges violently outside its interval, so if lambda_max(B) > lmax
the d=3 numbers are garbage. Check the true bound, then compare
exact-vs-Chebyshev at a small L where both are affordable.
"""
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
from numpy.polynomial.legendre import leggauss
XS, WS = leggauss(24)
def integ(f, lo, hi):
    lo=np.asarray(lo,float); hi=np.asarray(hi,float)
    p=0.5*(lo+hi)[:,None]+0.5*(hi-lo)[:,None]*XS[None,:]
    return 0.5*(hi-lo)*np.sum(WS[None,:]*f(p),axis=1)

def build(L, eps, kappa):
    t=np.arange(L,dtype=float)
    W=lambda x:(1.0+eps*np.cos(kappa*x))**0.5
    Rho=lambda x:(1.0+eps*np.cos(kappa*x))**1.5
    w0=integ(W,t,t+1.0); wt=integ(W,t-0.5,t+0.5); m=integ(Rho,t-0.5,t+0.5)
    i,j,k=np.indices((L,L,L)); flat=lambda a,b,c:((a%L)*L+(b%L))*L+(c%L)
    N=L**3; M=m[i.ravel()]
    r,c,v=[],[],[]; diag=np.zeros(N); a=flat(i,j,k).ravel()
    for ax,(di,dj,dk) in enumerate(((1,0,0),(0,1,0),(0,0,1))):
        b=flat(i+di,j+dj,k+dk).ravel(); ww=(w0 if ax==0 else wt)[i.ravel()]
        r+=list(a)+list(b); c+=list(b)+list(a); v+=list(-ww)+list(-ww)
        np.add.at(diag,a,ww); np.add.at(diag,b,ww)
    r+=list(range(N)); c+=list(range(N)); v+=list(diag)
    A=coo_matrix((v,(r,c)),shape=(N,N)).tocsr()
    isq=1/np.sqrt(M)
    from scipy.sparse import diags
    D=diags(isq); return (D@A@D).tocsr(), M

print("=== (a) true spectral bound of B vs the hard-coded lmax=14.0 ===")
L=16; kappa=2*np.pi/L
for e in (-0.10,-0.05,0.0,0.05,0.10):
    B,_=build(L,e,kappa)
    lm=eigsh(B,k=1,which='LA',return_eigenvectors=False)[0]
    flag = "  <-- EXCEEDS lmax=14" if lm>14.0 else ""
    print(f"  eps={e:+.2f}   lambda_max(B) = {lm:.4f}{flag}")

print("\n=== (b) exact dense trace vs Chebyshev, same operator, L=12 ===")
L=12; kappa=2*np.pi/L
xs=np.array([0.05,0.10,0.20,0.35,0.50]); s=xs/kappa**2; h=0.05
def cheb_tr(B,svals,Z,order=110,lmax=14.0):
    d,e=lmax/2,lmax/2; out=[]
    for sv in svals:
        kk=np.arange(order+1); th=np.pi*(kk+0.5)/(order+1); xk=np.cos(th)
        fk=np.exp(-sv*(d*xk+e))
        cj=np.array([(2.0/(order+1))*np.sum(fk*np.cos(q*th)) for q in range(order+1)]); cj[0]/=2
        T0=Z.copy(); T1=(B@Z-e*Z)/d; acc=cj[0]*T0+cj[1]*T1
        for q in range(2,order+1):
            T2=2*(B@T1-e*T1)/d-T0; acc+=cj[q]*T2; T0,T1=T1,T2
        out.append(np.sum(Z*acc)/Z.shape[1])
    return np.array(out)
N=L**3; rng=np.random.default_rng(3); Z=rng.choice([-1.0,1.0],size=(N,64))
Ke,Kc,Vs={},{},{}
for e in (-2,-1,0,1,2):
    B,M=build(L,e*h,kappa)
    ev=np.linalg.eigvalsh(B.toarray())
    Ke[e]=np.array([np.sum(np.exp(-sv*ev)) for sv in s])
    Kc[e]=cheb_tr(B,s,Z); Vs[e]=M.sum()
d2=lambda D:0.5*(-D[2]+16*D[1]-30*D[0]+16*D[-1]-D[-2])/(12*h*h)
V2=d2(Vs)
Re=(4*np.pi*s)**1.5*d2(Ke)/V2; Rc=(4*np.pi*s)**1.5*d2(Kc)/V2
print(f"  V2 = {V2:.3f}   (3/16)L^3 = {(3/16)*L**3:.3f}")
print("\n    x      R exact    R chebyshev   cheb/exact    1+(2/9)x")
for i in range(len(xs)):
    print(f"  {xs[i]:5.3f}  {Re[i]:9.5f}   {Rc[i]:10.5f}   {Rc[i]/Re[i]:9.5f}  {1+(2/9)*xs[i]:9.5f}")
