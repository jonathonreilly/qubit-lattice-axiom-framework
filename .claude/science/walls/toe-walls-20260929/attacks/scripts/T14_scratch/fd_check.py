"""Independent finite-difference check of the analytic f and t coefficients (small grid, generic eps, detuned tree speeds)."""
import numpy as np
from yukawa_euclid_gap import run
def brute(Nt,Ns,eps,m,mu,c,lam,h):
    tt=2*np.pi*np.arange(Nt)/Nt; ts=2*np.pi*np.arange(Ns)/Ns
    K=np.meshgrid(tt,ts,ts,ts,indexing='ij')
    def s(q):  # q list of 4 arrays (theta,k1,k2,k3)
        return [c*np.sin(q[0])/eps]+[np.sin(q[j]) for j in (1,2,3)]
    def den(q): return m**2+sum(x**2 for x in s(q))
    def D(q): return 1/(mu**2+lam*4*np.sin(q[0]/2)**2/eps**2+sum(4*np.sin(q[j]/2)**2 for j in (1,2,3)))
    meas=1/(eps*Nt*Ns**3)
    def F(nu,P):   # F_nu(P) = int D(k) s_nu(P-k)/den(P-k)
        q=[P[i]-K[i] for i in range(4)]
        return meas*np.sum(D(K)*s(q)[nu]/den(q))
    def T(P):
        q=[K[i]+P[i] for i in range(4)]
        sk=s(K); sq=s(q)
        return 4*meas*np.sum((m**2-sum(a*b for a,b in zip(sk,sq)))/(den(K)*den(q)))
    out={}
    for nu,(scale) in ((0,eps),(1,1.0)):
        e=[0,0,0,0]; e[nu]=h
        Pp=[e[i] for i in range(4)]; Pm=[-e[i] for i in range(4)]
        # physical momentum shift = h/scale
        out['f%d'%nu]=(F(nu,Pp)-F(nu,Pm))/(2*h/scale)
        out['t%d'%nu]=(T(Pp)+T(Pm)-2*T([0,0,0,0]))/(2*(h/scale)**2)
    return out
for (Nt,Ns,eps,m,mu,c,lam) in [(12,12,1.0,0.7,0.6,1.0,1.0),(16,10,0.6,0.8,0.7,1.1,0.85)]:
    a=run(Nt,Ns,eps,m,mu,c,lam)
    b=brute(Nt,Ns,eps,m,mu,c,lam,1e-3)
    print((Nt,Ns,eps,m,mu,c,lam))
    print(' analytic ft,fx,tt,ts:',a['ft'],a['fx'],a['tt'],a['ts'])
    print(' brute    ft,fx,tt,ts:',b['f0'],b['f1'],b['t0'],b['t1'])
