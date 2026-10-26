import sympy as sp, itertools
from explore import *
lam,mu=sp.symbols('lam mu',real=True)
def bond_axis(a,b):
    d=[b[0][i]-a[0][i] for i in range(len(a[0]))]
    if sum(map(abs,d))!=1: return None
    return [i for i in range(len(d)) if d[i]!=0][0]
def mid(a,b,comp): return sp.Rational(a[0][comp]+b[0][comp],2)
def Vgen(lam,mu,weighted,comp=0):
    # V = mu*(identity on bonds) + lam*(translate bond along its own axis by +-1, coins kept); canonical key keeps (lo,hi) coins
    def F(v):
        o={}
        for (a,b),amp in v.items():
            ax=bond_axis(a,b)
            if ax is None: continue
            m0=mid(a,b,comp)
            targets=[(a,b,mu)]
            for sgn in (1,-1):
                sh=lambda s:((tuple(s[0][i]+(sgn if i==ax else 0) for i in range(len(s[0]))),s[1]))
                targets.append((sh(a),sh(b),lam))
            for (a2,b2,c) in targets:
                if c==0: continue
                m1=mid(a2,b2,comp)
                w=1 if not weighted else (m0+m1)/2
                k=(a2,b2)
                o[k]=sp.expand(o.get(k,0)+c*w*amp)
        return {k:a for k,a in o.items() if a!=0}
    return F
for dim in (2,):
  for sign in (-1,1):
    V=Vgen(lam,mu,False); VD=Vgen(lam,mu,True)
    p=Pair(dim,sign,V,lambda v,comp:VD(v))
    a=((0,)*dim,0);b=((1,)+(0,)*(dim-1),0)
    k,sg=p.canon(a,b)
    d=p.defect({k:sg},0)
    target=(((-1,-1),0),((0,0),1))
    print(sign,sp.factor(d.get(target,0)))
