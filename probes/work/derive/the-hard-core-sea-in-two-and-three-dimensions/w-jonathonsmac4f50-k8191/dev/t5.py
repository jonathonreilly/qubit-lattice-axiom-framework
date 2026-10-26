import sympy as sp_, time, numpy as np
from lib import *
from tiles import patch
n,b=patch((2,3))
for ferm in (True,False):
    H,_=build_sector(n,b,3,1,ferm)
    A=sp_.Matrix((2*H).toarray().round().astype(int).tolist())
    t=time.time()
    x=sp_.symbols('x')
    cp=A.charpoly(x).as_expr()
    f=sp_.factor_list(cp)
    print("F" if ferm else "B",H.shape,round(time.time()-t,1))
    for fac,m in f[1]:
        roots=sp_.Poly(fac,x).nroots(n=20)
        print("  factor",fac,"mult",m,"min root/2",min(sp_.re(r) for r in roots)/2)
