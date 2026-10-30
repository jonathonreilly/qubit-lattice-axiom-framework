import os
os.environ["OMP_NUM_THREADS"]="1"; os.environ["OPENBLAS_NUM_THREADS"]="1"; os.environ["VECLIB_MAXIMUM_THREADS"]="1"
import numpy as np, mpmath as mp
from scipy.sparse.linalg import eigsh
# A. bounded clipped family, 1D chain exact transfer matrix: eps = b clip(phi,K), b=sqrt(c) m, K=C rho sqrt(c)/m
print("A: clipped bounded field, pressure vs c t^2/2; bound on |eps| = C*rho*c")
c=1.0;C=3.0;rho=1.0
for m in [0.2,0.1,0.05]:
    b=np.sqrt(c)*m;K=C*rho*np.sqrt(c)/m
    h=0.15;R=K+8*np.sqrt(1/(2*m));x=np.arange(-R,R+h,h)
    def lam(t):
        v=-0.25*m*m*x*x+0.5*t*b*np.clip(x,-K,K)
        M=np.exp(-0.5*(x[:,None]-x[None,:])**2+v[:,None]+v[None,:])
        return eigsh(M,k=1,which='LA',return_eigenvectors=False)[0]
    l0=lam(0.)
    for t in [0.5,1.0]:
        print(f" m={m} K={K:.0f} sup|eps|={b*K:.2f} t={t} p(t)-p(0)={np.log(lam(t)/l0):.10f} ct^2/2={c*t*t/2:.10f}")
# B. 2D torus, CT1 with additive E = sum_p log(b0(beta-w_p)/b0(beta))
print("B: 2D SU(2) torus Z=sum_j prod_p b_j; ratio |G| exp(-Re E)")
mp.mp.dps=60
def rr(nu,z): return mp.besseli(nu,z)/mp.besseli(1,z)
for tau in [0.5,0.1]:
  for n in [400,4000,40000]:
    beta=mp.mpf(n)/tau; nw=n//4  # 1/4 of plaquettes w, 1/4 conj w, rest 0
    out=[]
    for w in [mp.mpf(1),mp.mpc(0,1),mp.mpc(1,1)/mp.sqrt(2),mp.mpc(-1,1)/mp.sqrt(2),mp.mpf(-1)]:
        num=0;den=0
        for k in range(1,int(6/mp.sqrt(tau))+12):
            nu=k
            r0=mp.log(rr(nu,beta)); r1=mp.log(rr(nu,beta-w)); r2=mp.log(rr(nu,beta-mp.conj(w)))
            num+=mp.exp((n-2*nw)*r0+nw*(r1+r2)); den+=mp.exp(n*r0)
        out.append(float(abs(num/den)))
    print(f" tau={tau} n={n}",["%.5f"%o for o in out], "Theta=%.4f"%float(den))
# C. 4D lattice Casimir: log det'(-Delta) - T^4 f0, neutral; twisted (no zero mode) charged
print("C: 4D log det, fit a + f0 T^4 + kappa ln T")
Ts=[8,12,16,20,24,32]
def logdet(T,th):
    k=2-2*np.cos(2*np.pi*np.arange(T)/T+th/T)
    a=k[:,None]+k[None,:]; s=np.add.outer(a,a).ravel()
    if th==0: s=s[1:]
    return np.log(s).sum()
for th,name in [(0.0,"neutral th=0"),(np.pi,"charged th=pi"),(1.0,"charged th=1")]:
    L=np.array([logdet(T,th) for T in Ts]);X=np.array(Ts,float)
    A=np.c_[X**4,np.log(X),np.ones(len(X)),X**-2.]
    sol=np.linalg.lstsq(A/np.abs(L)[:,None],np.ones(len(X)),rcond=None)[0]
    print(" ",name,"f0=%.8f kappa=%.4f const=%.4f"%(sol[0],sol[1],sol[2]))
