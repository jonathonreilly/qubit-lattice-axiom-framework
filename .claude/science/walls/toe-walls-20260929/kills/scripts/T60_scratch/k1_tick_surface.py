"""Kill check K1: which vacuum stress does the June (Euclidean tick surface) formula give vs the fixed-site Hamiltonian sea?
eps(t;m) = -< log( m^2 + sum_mu t_mu^2 sin^2(P_mu/2) ) >_BZ  (June note T1 formula, hop weights t_mu).
Stress-like response  T_mu = t_mu d eps / d t_mu = -2 < t_mu^2 s_mu^2 / (m^2 + sum t^2 s^2) >.
Massless identity: sum_mu T_mu = -2 exactly (overall-scale Jacobian).  Compare hypercubic t0=1 with the continuous-time limit t0 -> large.
"""
import numpy as np
N=40
P=(np.arange(N)+0.5)*2*np.pi/N
s2=np.sin(P/2)**2
S=[None]*4
def T(t,m):
    g=[s2.reshape([-1 if i==j else 1 for i in range(4)]) for j in range(4)]
    tot=m*m+sum(t[j]**2*g[j] for j in range(4))
    return [-2*np.mean(t[j]**2*g[j]/tot) for j in range(4)]
for m in (0.0,0.3,0.7):
    print("m=%.1f"%m)
    for t0 in (1.0,2.0,5.0,20.0):
        Tm=T([t0,1,1,1],m)
        print("  t0=%5.1f  T0=%8.5f  Ti=%8.5f (x3)  sum=%8.5f   T0+2=%8.5f  -3*Ti=%8.5f"%(t0,Tm[0],Tm[1],sum(Tm),Tm[0]+2,-3*Tm[1]))
