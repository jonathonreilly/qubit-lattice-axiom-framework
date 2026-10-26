import pickle, random, itertools
from fractions import Fraction as Fr
from math import factorial
table=pickle.load(open('O16_table.pkl','rb'))
def gm(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def ipow(n):  # i^n
    return [(1,0),(0,1),(-1,0),(0,-1)][n%4]
def series(comp, A1,A2,A1p,A2p, d1,d2,d1p,d2p, nmax=5):
    """C[n][(cp,c)] = coefficient of kappa^n in <k1'k2';c'|O16|k1 k2;c>/vol, corners A (bits), offsets d"""
    C=[dict() for _ in range(nmax+1)]
    for (r,c1,c2,z1,z2,e1,e2,coef) in table[comp]:
        # phase  e^{i k1.r} e^{-i(k1'.z1 + k2'.z2)};  corner sign
        sgn=(-1)**(sum(A1[a]*r[a] for a in range(2)) - sum(A1p[a]*z1[a]+A2p[a]*z2[a] for a in range(2)))
        x=sum(d1[a]*r[a] for a in range(2)) - sum(d1p[a]*z1[a]+d2p[a]*z2[a] for a in range(2))
        key=((e1,e2),(c1,c2))
        for n in range(nmax+1):
            f=gm(ipow(n),(Fr(sgn)*coef[0]*x**n/factorial(n), Fr(sgn)*coef[1]*x**n/factorial(n)))
            cur=C[n].get(key,(Fr(0),Fr(0)))
            C[n][key]=(cur[0]+f[0],cur[1]+f[1])
    return C
def order(C):
    for n,cn in enumerate(C):
        if any(v!=(0,0) for v in cn.values()): return n
    return None
random.seed(1)
def rv(): return Fr(random.randint(-9,9),random.randint(1,5))
res={}
for comp in (0,1):
  for A1 in itertools.product((0,1),repeat=2):
    for A2 in itertools.product((0,1),repeat=2):
      for A1p in itertools.product((0,1),repeat=2):
        A2p=tuple((A1[a]+A2[a]-A1p[a])%2 for a in range(2))
        orders=[]
        for trial in range(3):
            d1=(rv(),rv()); d2=(rv(),rv()); d1p=(rv(),rv()); d2p=(d1[0]+d2[0]-d1p[0], d1[1]+d2[1]-d1p[1])
            C=series(comp,A1,A2,A1p,A2p,d1,d2,d1p,d2p)
            orders.append(order(C))
        res[(comp,A1,A2,A1p,A2p)]=orders
from collections import Counter
print(Counter(tuple(v) for v in res.values()))
mn=Counter(min([o if o is not None else 99 for o in v]) for v in res.values())
print("min order over generic dirs per corner assignment:",mn)
# show which assignments have order 1 or 2
for k,v in list(res.items())[:40]:
    print(k,v)
