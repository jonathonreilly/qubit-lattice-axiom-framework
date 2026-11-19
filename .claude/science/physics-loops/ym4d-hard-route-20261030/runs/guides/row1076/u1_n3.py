# GUIDE: compact U(1), one sheet, three slice sites (two cuts): Lemma KIN's operator in the Fourier basis.
import numpy as np
M=10                                    # modes m1,m2 in [-M,M]
ms=np.arange(-M,M+1); L=len(ms)
Ng=64; t=(np.arange(Ng))*2*np.pi/Ng
def lam(b,n):
    n=np.abs(n)
    if np.isinf(b): return np.ones_like(n,dtype=float)
    tt=(np.arange(4000)+0.5)*2*np.pi/4000; w=np.exp(b*(np.cos(tt)-1))
    tab=np.array([(np.cos(k*tt)*w).sum() for k in range(0,4*M+2)]); tab/=tab[0]
    return tab[n]
# multiplication by e^{(bM/2) cos q}: matrix in Fourier basis
def Emat(bM):
    c=np.array([(np.exp(0.5*bM*(np.cos(t)-1))*np.cos(k*t)).sum()/Ng for k in range(0,2*M+1)])
    return np.array([[c[abs(a-b)] for b in ms] for a in ms])
def gap(bM,bL):
    E1=Emat(bM); E=np.kron(E1,E1)
    m1,m2=np.meshgrid(ms,ms,indexing='ij'); n1=-m1; n2=m1-m2; n3=m2
    kap=lam(bM,n1)*lam(bM,n2)*lam(bM,n3)*lam(bL,n2+n3)**2*lam(bL,n3)**2
    T=E@np.diag(kap.ravel())@E
    ev=np.sort(np.linalg.eigvalsh((T+T.T)/2))[::-1]
    return np.log(ev[0]/ev[1])
for bM in (1.0,2.4,4.0):
    f=gap(bM,np.inf); grid=[0.5,1,2.4,4,6,10,20,50,200]
    g=[gap(bM,b) for b in grid]
    print("U(1) n=3 bM=%.1f face=%.6f  "%(bM,f)+"  ".join("bL=%g:%+.2e"%(b,v-f) for b,v in zip(grid,g)))
