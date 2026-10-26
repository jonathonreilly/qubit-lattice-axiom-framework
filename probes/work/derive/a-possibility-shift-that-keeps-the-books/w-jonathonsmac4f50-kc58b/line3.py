import sympy as sp, itertools
from explore import *
from line import make
U=sp.symbols('U',real=True)
M=U*sp.eye(4)
for sign in (-1,1):
    Vf=make(sign,M,0)
    def VD(v,comp):
        a=Vf(v,lambda x1,x2: sp.Rational(x1[0]+x2[0],2))
        b={k:sp.expand(-U*(k[0][0][0]+k[1][0][0])*amp) for k,amp in v.items()}
        return Pair.add(None,[a,b])
    p=Pair(1,sign,lambda v:Vf(v),VD)
    bad=0
    for pos2 in [(1,),(2,),(3,),(4,)]:
        for c1,c2 in itertools.product((0,1),repeat=2):
            k,sg=p.canon(((0,),c1),(pos2,c2))
            d=p.defect({k:sg},0)
            bad+=bool(d)
    print(sign,'nonzero defects with one-body placement -U X:',bad)
