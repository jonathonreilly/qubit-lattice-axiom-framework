# GUIDE: Q_8, one sheet, two slice sites: exact 5x5 class-function model of Lemma KIN.
import numpy as np
# classes: {1},{-1},{+-i},{+-j},{+-k}; sizes 1,1,2,2,2; x = 1,-1,0,0,0
sz=np.array([1,1,2,2,2.0]); x=np.array([1,-1,0,0,0.0])
chars=np.array([[1,1,1,1,1],[1,1,1,-1,-1],[1,1,-1,1,-1],[1,1,-1,-1,1],[2,-2,0,0,0.0]])  # triv, s_i, s_j, s_k, tau
dim=np.array([1,1,1,1,2.0])
def lam(b):
    if np.isinf(b): return np.ones(5)
    w=np.exp(b*(x-1)); Z=(sz*w).sum()
    return (chars*(sz*w)).sum(1)/Z/dim
def gap(bM,bL):
    kap=lam(bM)**2*lam(bL)**2
    V=chars*np.sqrt(sz/8.0)            # orthonormal characters in the basis of normalized class indicators
    K=(V.T*kap)@V
    E=np.diag(np.exp(0.5*bM*(x-1)))    # shift by a constant: ratios unchanged
    T=E@K@E
    ev=np.sort(np.linalg.eigvalsh((T+T.T)/2))[::-1]
    return np.log(ev[0]/ev[1])
def lead(bL):
    l=lam(bL); K00=(1+3*l[1]**2+4*l[4]**2)/8; Kss=(3+l[1]**2)/4
    return np.log(K00)-np.log(Kss)
print("check vs first script: bM=2.4 face %.6f, bL=5 %.6f, bL=10 %.6f"%(gap(2.4,np.inf),gap(2.4,5),gap(2.4,10)))
for bM in (2.4,4,6,8,12):
    out=[]
    for bL in (3,4,5,6,8,10):
        out.append("bL=%g: d=%.3e lead=%.3e -8e^-bL=%.3e"%(bL,gap(bM,bL)-gap(bM,np.inf),lead(bL),-8*np.exp(-bL)))
    print("bM=%g face=%.5f | "%(bM,gap(bM,np.inf))+" ; ".join(out))
# where does the dip start/end at bM=2.4, and the smallest bM with a dip
for bM in (1.0,1.5,1.8,2.0,2.2,2.4,3.0):
    g=np.array([gap(bM,b) for b in np.linspace(0.2,30,3000)]); f=gap(bM,np.inf)
    print("bM=%.1f  min(gap-face)=%.4e at bL=%.2f"%(bM,(g-f).min(),np.linspace(0.2,30,3000)[(g-f).argmin()]))
