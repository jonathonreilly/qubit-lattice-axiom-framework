# Build exact equations: all Fourier coefficients of u0^2+|u|^2-1 vanish.
import pickle, sympy as sp, itertools
from collections import defaultdict
d=pickle.load(open('param.pkl','rb')); params=d['params']; c0=d['c0']; cu=d['cu']
F=defaultdict(lambda:0)
modes=list(c0.keys())
for n in modes:
    for m in modes:
        s=tuple(a+b for a,b in zip(n,m))
        F[s]+= c0[n]*c0[m] + sum(cu[n][j]*cu[m][j] for j in range(3))
F[(0,0,0)]-=1
eqs=set()
for s,v in F.items():
    v=sp.expand(v)
    re,im=[sp.expand(x) for x in (sp.re(v),sp.im(v))] if v.has(sp.I) else (v,0)
    for e in (re,im):
        e=sp.expand(e)
        if e!=0:
            # normalize sign/scale
            p=sp.Poly(e,*params); e=sp.expand(e/p.LC())
            eqs.add(e)
eqs=sorted(eqs,key=lambda e:(sp.Poly(e,*params).total_degree(),len(e.args)))
print("n eqs",len(eqs))
pickle.dump(eqs,open('eqs.pkl','wb'))
