import sympy as sp, itertools
from explore import *
from line import make
U,tt=sp.symbols('U tt',real=True)
def defects(M,sign,toff,dimline=True):
    Vf=make(sign,M,toff)
    p=Pair(1,sign,lambda v:Vf(v),lambda v,comp:Vf(v,lambda x1,x2: sp.Rational(x1[0]+x2[0],2)+toff))
    res={}
    for pos2 in [(1,),(2,),(3,),(4,)]:
        for c1,c2 in itertools.product((0,1),repeat=2):
            k,sg=p.canon(((0,),c1),(pos2,c2))
            d=p.defect({k:sg},0)
            if d: res[(pos2,c1,c2)]=d
    return res
for sign in (-1,1):
    M=U*sp.eye(4)
    r=defects(M,sign,0)
    print(sign,'U*1, tt=0: nonzero defects',len(r))
    r=defects(M,sign,tt)
    print(sign,'U*1, tt free: nonzero defects',len(r), list(r.items())[:1])
