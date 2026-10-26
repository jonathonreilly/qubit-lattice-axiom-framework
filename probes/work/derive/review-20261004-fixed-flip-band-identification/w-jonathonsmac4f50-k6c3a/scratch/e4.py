import sys; sys.path.insert(0,'scratch')
from e2 import *
from e3 import shear_data
import random
mp.mp.dps=40
ZETA={'i':mp.mpf(1)/20,'ii':mp.mpf(1)/500}
EPS0={'i':mp.mpf(1)/62500,'ii':mp.mpf(1)/2250000}
def gap(nd,d,zeta,eps):
    X=zeta**3+abs(d['m'])*zeta**2+abs(d['lam'])*eps+abs(d['a1'])*eps*zeta
    Y=zeta**3+abs(d['b1'])*eps*zeta
    amps={'x':2,'y':2,'z':2*nd.J,'odd':2*nd.kap}
    ent=[[mp.mpf(0)]*4 for _ in range(4)]
    for a,b,n,kd in TERMS:
        phi=abs(n[0]-n[1])*X+abs(n[0]+n[1])*Y+abs(n[2])*zeta
        dl=amps[kd]*phi+(2*eps if kd=='odd' else 0)
        ent[a][b]+=dl; ent[b][a]+=dl
    Hd=max(sum(r) for r in ent)
    U=nd.T[:,2:4]
    Uf2=sum(abs(U[i,j])**2 for i in range(4) for j in range(2))
    A,B,C=nd.blocks(nd.H0)
    dC0=abs(C[0,0]*C[1,1]-C[0,1]*C[1,0]); Cn=sum(abs(C[i,j]) for i in range(2) for j in range(2))
    return dC0/Cn, Uf2*Hd
if __name__=='__main__':
  for w in ('i','ii'):
    for sg in (1,-1):
        nd=Node(w,sg); d=shear_data(nd)
        sig=EPS0[w]
        lo,hi=gap(nd,d,ZETA[w],EPS0[w])
        print(w,sg,'min|lambda(C0)| lower',mp.nstr(lo,6),' ||dC|| bound',mp.nstr(hi,6),' ratio',mp.nstr(lo/hi,6))
