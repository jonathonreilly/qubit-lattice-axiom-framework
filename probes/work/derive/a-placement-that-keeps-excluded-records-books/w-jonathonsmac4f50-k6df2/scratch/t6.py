import pickle, random, itertools
from fractions import Fraction as Fr
exec(open('t5.py').read().split("random.seed(5)")[0])
def melem(comp,A1,A2,A1p,A2p,d1,d2,d1p,d2p,e1,e2,e1p,e2p,nmax=5):
    C=series(comp,A1,A2,A1p,A2p,d1,d2,d1p,d2p,nmax=nmax)
    u=tens(spinor(A1,e1),spinor(A2,e2)); up=tens(spinor(A1p,e1p),spinor(A2p,e2p))
    out=[]
    for n,cn in enumerate(C):
        tot=(Fr(0),Fr(0))
        for (cp,c),val in cn.items():
            t=gm(gm(cj(up[cp]),val),u[c]); tot=(tot[0]+t[0],tot[1]+t[1])
        out.append(tot)
    return out
random.seed(7)
stats={}
for comp in (0,1):
  for (e1,e2,e1p,e2p,r) in found:
    l2,a,b=r
    d1=(e1[0],e1[1]); d2=(l2*e2[0],l2*e2[1]); d1p=(a*e1p[0],a*e1p[1]); d2p=(b*e2p[0],b*e2p[1])
    for trial in range(4):
        A1=tuple(random.randint(0,1) for _ in range(2)); A2=tuple(random.randint(0,1) for _ in range(2)); A1p=tuple(random.randint(0,1) for _ in range(2))
        A2p=tuple((A1[i]+A2[i]-A1p[i])%2 for i in range(2))
        direct=melem(comp,A1,A2,A1p,A2p,d1,d2,d1p,d2p,e1,e2,e1p,e2p)
        # exchanged incoming: record1 <- (k2,c2), record2 <- (k1,c1)
        exch=melem(comp,A2,A1,A1p,A2p,d2,d1,d1p,d2p,e2,e1,e1p,e2p)
        # NOTE: coin ordering swap: tens(u2,u1) is what melem builds for exchanged input -> correct (state |k2 u2>|k1 u1>) ; antisym amplitude = <q'|O|q> - <q'|O|tau q> with tau q = |k2,u2;k1,u1>
        # but the antisymmetric ket is |k1 u1;k2 u2> - |k2 u2;k1 u1>
        anti=[ (direct[n][0]-exch[n][0], direct[n][1]-exch[n][1]) for n in range(6)]
        o=[n for n in range(6) if anti[n]!=(0,0)]
        stats[(comp,)]=stats.get((comp,),[])+[o[0] if o else None]
        print(comp,"anti nonzero orders",o,"| direct",[n for n in range(6) if direct[n]!=(0,0)])
