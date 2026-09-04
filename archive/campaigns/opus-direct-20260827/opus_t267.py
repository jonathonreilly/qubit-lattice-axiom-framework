"""
T267 - the direct diff: d=3 lattice vs exact continuum at IDENTICAL parameters.

R187 localised the ~4/3 to the d=3 lattice operator, but the comparison used
L=32, kappa=2pi/32 for the lattice and L=40, kappa=2pi/40 for the continuum.
This runs both at the SAME L and kappa -- the T202/T203 methodology that worked
in d=4 -- so R_lat/R_cont isolates the operator with nothing else varying.
"""
import numpy as np, time
from scipy.sparse import coo_matrix
from numpy.polynomial.legendre import leggauss
from collections import Counter
XS, WS = leggauss(24)
def integ(f, lo, hi):
    lo=np.asarray(lo,float); hi=np.asarray(hi,float)
    p=0.5*(lo+hi)[:,None]+0.5*(hi-lo)[:,None]*XS[None,:]
    return 0.5*(hi-lo)*np.sum(WS[None,:]*f(p),axis=1)

L, n = 40, 1
kappa = 2*np.pi*n/L
xs = np.array([0.05,0.10,0.20,0.35,0.50]); s = xs/kappa**2
h = 0.05

# ---------------- lattice ----------------
def lat_op(eps):
    t=np.arange(L,dtype=float)
    W=lambda x:(1.0+eps*np.cos(kappa*x))**0.5
    Rho=lambda x:(1.0+eps*np.cos(kappa*x))**1.5
    w0=integ(W,t,t+1.0); wt=integ(W,t-0.5,t+0.5); m=integ(Rho,t-0.5,t+0.5)
    i,j,k=np.indices((L,L,L)); flat=lambda a,b,c:((a%L)*L+(b%L))*L+(c%L)
    N=L**3; M=m[i.ravel()]
    r,c,v=[],[],[]; diag=np.zeros(N)
    a=flat(i,j,k).ravel()
    for ax,(di,dj,dk) in enumerate(((1,0,0),(0,1,0),(0,0,1))):
        b=flat(i+di,j+dj,k+dk).ravel()
        ww=(w0 if ax==0 else wt)[i.ravel()]
        r+=list(a)+list(b); c+=list(b)+list(a); v+=list(-ww)+list(-ww)
        np.add.at(diag,a,ww); np.add.at(diag,b,ww)
    r+=list(range(N)); c+=list(range(N)); v+=list(diag)
    return coo_matrix((v,(r,c)),shape=(N,N)).tocsr(), 1/np.sqrt(M), M.sum(), N

def cheb(A,isq,svals,Z,order=110,lmax=14.0):
    Bmul=lambda X: isq[:,None]*(A@(isq[:,None]*X))
    d,e=(lmax)/2,(lmax)/2; out=[]
    for sv in svals:
        kk=np.arange(order+1); th=np.pi*(kk+0.5)/(order+1); xk=np.cos(th)
        fk=np.exp(-sv*(d*xk+e))
        cj=np.array([(2.0/(order+1))*np.sum(fk*np.cos(q*th)) for q in range(order+1)]); cj[0]/=2
        T0=Z.copy(); T1=(Bmul(Z)-e*Z)/d; acc=cj[0]*T0+cj[1]*T1
        for q in range(2,order+1):
            T2=2*(Bmul(T1)-e*T1)/d-T0; acc+=cj[q]*T2; T0,T1=T1,T2
        out.append(np.sum(Z*acc)/Z.shape[1])
    return np.array(out)

t0=time.time()
A0,isq0,V0,N=lat_op(0.0)
rng=np.random.default_rng(7); Z=rng.choice([-1.0,1.0],size=(N,32))
Ks={};Vs={}
for e in (-2,-1,0,1,2):
    A,isq,V,_=lat_op(e*h); Ks[e]=cheb(A,isq,s,Z); Vs[e]=V
K2=0.5*(-Ks[2]+16*Ks[1]-30*Ks[0]+16*Ks[-1]-Ks[-2])/(12*h*h)
V2=0.5*(-Vs[2]+16*Vs[1]-30*Vs[0]+16*Vs[-1]-Vs[-2])/(12*h*h)
Rlat=(4*np.pi*s)**1.5*K2/V2
print(f"L={L}, kappa={kappa:.5f}, d=3, p=1  [{time.time()-t0:.0f}s]")
print(f"V2 lattice = {V2:.2f}   (3/16)L^3 = {(3/16)*L**3:.2f}")
Rcont=np.array([1.01150,1.02374,1.05038,1.09533,1.14569])   # T266, same L and kappa
tgt=1+(2/9)*xs
print("\n    x      R lattice   R continuum   lat/cont    target")
for i in range(len(xs)):
    print(f"  {xs[i]:5.3f}   {Rlat[i]:9.5f}   {Rcont[i]:11.5f}   {Rlat[i]/Rcont[i]:8.4f}  {tgt[i]:8.5f}")
print(f"\n  mean lat/cont = {np.mean(Rlat/Rcont):.4f}   (4/3 = {4/3:.4f})")
