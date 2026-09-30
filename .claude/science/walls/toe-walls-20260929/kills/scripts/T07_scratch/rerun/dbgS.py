import numpy as np
from common import *
L=24; ring=Ring(L); x=np.arange(L)
side=np.where(x>=12,1.0,-1.0)
SETS=[(0.0,np.pi/4),(0.0,-np.pi/4),(np.pi/2,np.pi/4),(np.pi/2,-np.pi/4)]
def gauss(w,c=12):
    g=np.exp(-(x-c)**2/(2*w**2)); return g/g.sum()
rho0=np.outer(gauss(3.0/np.sqrt(2)),gauss(3.0/np.sqrt(2))); rho0/=rho0.sum()
for s in SETS:
    m=Bell2(L,s[0],s[1],ring)
    R=m.evolve(rho0,np.array([0.,4.,8.]))
    P=m.P(8.0)
    E=lambda r:(r*np.outer(side,side)).sum()
    print(np.round(s,3),'P(B+) rec %.8f  psi %.8f   P(A+) rec %.8f psi %.8f   E_rec %.5f E_psi %.5f'%((R[-1].sum(0)*(side>0)).sum(),(P.sum(0)*(side>0)).sum(),(R[-1].sum(1)*(side>0)).sum(),(P.sum(1)*(side>0)).sum(),E(R[-1]),E(P)))
