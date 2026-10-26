import pickle, random, itertools
from fractions import Fraction as Fr
exec(open('t3.py').read().split("random.seed(1)")[0])
found=pickle.load(open('onshell_points.pkl','rb'))
def spinor(A,d):
    # leading-order + band spinor of h(A+delta) = sum eps_a delta_a sigma_a  (unnormalised (1,w)), d unit vector
    ex=(-1)**A[0]; ey=(-1)**A[1]
    w=(Fr(ex)*d[0], Fr(ey)*d[1])   # w = ex dx + i ey dy
    return [(Fr(1),Fr(0)), w]
def tens(u,v):  # index c=(c1,c2)
    out={}
    for c1 in range(2):
        for c2 in range(2):
            out[(c1,c2)]=gm(u[c1],v[c2])
    return out
def cj(z): return (z[0],-z[1])
random.seed(5)
for comp in (0,1):
  for (e1,e2,e1p,e2p,r) in found[:6]:
    l2,a,b=r
    d1=(e1[0],e1[1]); d2=(l2*e2[0],l2*e2[1]); d1p=(a*e1p[0],a*e1p[1]); d2p=(b*e2p[0],b*e2p[1])
    for trial in range(3):
        A1=tuple(random.randint(0,1) for _ in range(2)); A2=tuple(random.randint(0,1) for _ in range(2)); A1p=tuple(random.randint(0,1) for _ in range(2))
        A2p=tuple((A1[i]+A2[i]-A1p[i])%2 for i in range(2))
        C=series(comp,A1,A2,A1p,A2p,d1,d2,d1p,d2p,nmax=5)
        u=tens(spinor(A1,e1),spinor(A2,e2)); up=tens(spinor(A1p,e1p),spinor(A2p,e2p))
        ords=[]
        for n,cn in enumerate(C):
            tot=(Fr(0),Fr(0))
            for (cp,c),val in cn.items():
                t=gm(gm(cj(up[cp]),val),u[c]); tot=(tot[0]+t[0],tot[1]+t[1])
            ords.append(tot!=(0,0))
        print(comp,A1,A2,A1p,A2p,"nonzero orders:",[n for n,x in enumerate(ords) if x])
