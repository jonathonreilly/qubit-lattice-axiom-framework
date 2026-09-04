"""Continuum heat-kernel coefficients a_1 = R/6 and
a_2 = (1/360)(12 Box R + 5R^2 - 2 Ric^2 + 2 Riem^2),   Gilkey, E=0.
Fully numerical for g = diag(1+eps P_mu cos(k x0))."""
import numpy as np, math
from contR import metric, christoffel

def curv(t, eps, P, k, h=1e-4):
    g = metric(t,eps,P,k); gi = np.linalg.inv(g)
    G = christoffel(t,eps,P,k)
    dG = np.zeros((4,4,4,4))
    dG[0] = (christoffel(t+h,eps,P,k)-christoffel(t-h,eps,P,k))/(2*h)
    Rud = np.zeros((4,4,4,4))       # R^a_{bcd}
    for a in range(4):
     for b in range(4):
      for c in range(4):
       for d in range(4):
        s = dG[c][a,d,b] - dG[d][a,c,b]
        for e in range(4):
            s += G[a][c,e]*G[e][d,b] - G[a][d,e]*G[e][c,b]
        Rud[a,b,c,d] = s
    Rdd = np.einsum('ae,ebcd->abcd', g, Rud)             # R_{abcd}
    Ric = np.einsum('abad->bd', Rud)
    R   = float(np.einsum('bd,bd->', gi, Ric))
    Riem2 = float(np.einsum('abcd,efgh,ae,bf,cg,dh->', Rdd,Rdd,gi,gi,gi,gi))
    Ric2  = float(np.einsum('ab,cd,ac,bd->', Ric,Ric,gi,gi))
    return R, Ric2, Riem2, float(math.sqrt(np.linalg.det(g)))

def integrals(L, eps, P, k, N=1024):
    ts=(np.arange(N)+0.5)*L/N; dt=L/N
    I1=0.0; I2=0.0
    for t in ts:
        R,Ric2,Riem2,sg = curv(t,eps,P,k)
        I1 += (R/6.0)*sg
        I2 += ((5*R*R - 2*Ric2 + 2*Riem2)/360.0)*sg   # Box R integrates to zero
    return I1*dt*L**3, I2*dt*L**3
