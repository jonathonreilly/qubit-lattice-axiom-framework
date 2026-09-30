import numpy as np, scipy.linalg as la
from t72_stag import *

def bound_level(evs, m, e0, Q, beta):
    thr = 2*e0 + 2*np.sqrt(beta**2*np.sin(Q/4)**2 + m**2)   # rough (+,+) edge at K=Q/2: each particle k~K/2=Q/4
    pos = evs[evs>2*e0+0.6*m]
    return pos.min(), thr

def W_pair_band(Nring, lam, beta, m, e0, timed=True):
    M=Nring//2
    Qs=[0.0, 2*np.pi/M, -2*np.pi/M, 4*np.pi/M, -4*np.pi/M]
    d=pair_band_E(Nring,lam,beta,m,e0,Qs,timed)
    E={Q:d[Q][d[Q]>2*e0+0.6*m].min() for Q in Qs}
    E0=E[0.0]
    # K = Q/2  =>  d2E/dK2 = 4 d2E/dQ2 ; Richardson from Q1,Q2
    q1=2*np.pi/M; q2=4*np.pi/M
    s1=(E[q1]+E[-q1]-2*E0)/q1**2; s2=(E[q2]+E[-q2]-2*E0)/q2**2
    d2Q=(4*s1-s2)/3
    d2K=4*d2Q
    return E0*d2K, E0, d2K, d, s1*4, s2*4

if __name__=="__main__":
    # validation of the sector reduction against brute force on the same ring: Q=0 lowest positive eigenvalue
    Nr=24; lam=0.6; b=1.0; m=1.0; e0=0.0
    H=two_body(Nr,np.ones(Nr),b,m,e0,lam,True,periodic=True).toarray()
    evb=la.eigvalsh(H)
    d=pair_band_E(Nr,lam,b,m,e0,[0.0])
    print("validation ring N=24: brute-force lowest positive eig =",evb[evb>0.6].min(), " sector Q=0 lowest =",d[0.0][d[0.0]>0.6].min())
    print("W_pair (timed binding) vs lam; beta=m=1,e0=0; ring N=60")
    print(" lam   E0       B=2m-E0   E''(K)   W_pair    W-1     (s1,s2 = d2E/dK2 at Q1,Q2)")
    for lam in (0.2,0.4,0.6,0.8,1.2):
        Wp,E0,d2,dd,s1,s2=W_pair_band(60,lam,b,m,e0)
        print(f"{lam:4.1f} {E0:8.5f} {2*m-E0:8.5f} {d2:8.5f} {Wp:8.5f} {Wp-1:8.5f}  ({s1:.4f},{s2:.4f})")
