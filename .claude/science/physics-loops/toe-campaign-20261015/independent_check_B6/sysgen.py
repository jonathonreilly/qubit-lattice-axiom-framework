import sympy as sp, itertools
from exact_setup import *
def walk(eb,syms):
    """U as dict offset -> dict basis -> sympy expr"""
    U={}
    for el,x in zip(eb,syms):
        for n,d in el.items():
            Un=U.setdefault(n,{})
            for b,c in d.items(): Un[b]=Un.get(b,0)+c*x
    return U
def product(alg,U,V):
    W={}
    for n,X in U.items():
        for m,Y in V.items():
            Z=alg.mul(X,Y); p=tuple(a+b for a,b in zip(n,m))
            Wp=W.setdefault(p,{})
            for b,c in Z.items(): Wp[b]=Wp.get(b,0)+c
    return W
def unit_eqs(alg,U,V,both=True):
    eqs=set()
    prods=[product(alg,U,V)]+([product(alg,V,U)] if both else [])
    for W in prods:
        for p,Z in W.items():
            for b,c in Z.items():
                c=sp.expand(c)
                if p==(0,0,0) and b[0]==0 and b[1]==b[2]: c=sp.expand(c-1)
                if c!=0: eqs.add(c)
    return list(eqs)
def to_singular(eqs,vars_,name='I'):
    return 'ideal %s = %s;\n'%(name, ',\n'.join(str(e).replace('**','^') for e in eqs))
