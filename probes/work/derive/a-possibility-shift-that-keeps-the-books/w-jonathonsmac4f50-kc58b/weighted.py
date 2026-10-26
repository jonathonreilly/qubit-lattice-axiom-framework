import sympy as sp, itertools, random
from explore import *
from explore2 import basis, randherm
def run(dim,sign,lo,hi,dens,seed,off=0):
    B=basis(dim,lo,hi)
    col,idx=randherm(B,dens,seed)
    t=sp.symbols('t')
    def midc(k,comp): return sp.Rational(k[0][0][comp]+k[1][0][comp],2)
    def V(v,weighted=False,comp=0):
        o={}
        for k,a in v.items():
            if k in idx:
                for i,m in col(k):
                    kk=B[i]
                    w=1 if not weighted else (midc(k,comp)+midc(kk,comp))/2+off
                    o[kk]=sp.expand(o.get(kk,0)+t*m*w*a)
        return {k:a for k,a in o.items() if a!=0}
    p=Pair(dim,sign,lambda v:V(v),lambda v,comp:V(v,True,comp))
    a=((0,)*dim,0);b=((1,)+(0,)*(dim-1),0)
    k,sg=p.canon(a,b)
    d=p.defect({k:sg},0)
    target=(((-1,-1)+(0,)*(dim-2),0),((0,)*dim,1))
    return sp.expand(d.get(target,0))
print(run(2,-1,-2,2,0.1,5))
print(run(2,1,-2,2,0.1,6,off=sp.Rational(1,3)))
