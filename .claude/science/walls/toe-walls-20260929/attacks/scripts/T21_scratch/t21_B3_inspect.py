import sys
import numpy as np
sys.path.insert(0, '.')
from t21_common import *
L=8; N=L**3; nb=neighbours(L); eps=eps_array(L).astype(np.int8); H0=walker_H0(L)
g=0.25; K=np.log(1/g)/4; pb=1-np.exp(-2*K); seed_numba(77)
sig=np.ones(N,dtype=np.int8); wolff_steps(sig,nb,pb,500,0)
for trial in range(3):
    wolff_steps(sig,nb,pb,40,0); s=sig.copy()
    if s.sum()<0: s=-s
    n=(1+eps*s)//2
    flipped=np.where(s==-1)[0]
    print("trial",trial,"flipped sites:",len(flipped),"on even sublattice (vacancies of occupied):",int((eps[flipped]==1).sum()),"odd (interstitials):",int((eps[flipped]==-1).sum()))
    for c in (2.0,):
        d=np.repeat(n.astype(float),2)*c
        E,V=np.linalg.eigh(H0+np.diag(d))
        rho=(np.abs(V)**2).reshape(N,2,-1).sum(axis=1); ipr=(rho**2).sum(axis=0)*N
        # print eigenvalues within [-0.6, c+0.6] with IPR
        idx=np.where((E>-0.5)&(E<c+0.5))[0]
        # lower-band top region and upper-band bottom region and in-gap
        print(" c=%.1f states with E in [-0.5,c+0.5]:"%c)
        print("   E:", np.round(E[idx],4))
        print("   IPR*N:", np.round(ipr[idx],1))
        # ideal edges
        print("   exact ideal edges 0 and c; count of eigenvalues within 1e-8 of 0:",int((abs(E)<1e-8).sum())," of c:",int((abs(E-c)<1e-8).sum()))
