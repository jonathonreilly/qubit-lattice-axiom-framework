import sympy as sp, pickle, sys
from exact_setup import *; from sysgen import *
eb=pickle.load(open('q2_basis.pkl','rb'))
alg=Alg(2,perm_rep2)
u=sp.symbols('u1:20'); v=sp.symbols('v1:20')
U=walk(eb,u); Vw=walk(eb,v)
# V has offsets negated? V = U^{-1}; its support also in box (box symmetric); same equivariant space
eqs=unit_eqs(alg,U,Vw)
print(len(eqs))
const=[i for i,el in enumerate(eb) if (0,0,0) in el]
print('constant-term basis idx',const, [eb[i][(0,0,0)] for i in const])
s='LIB "modstd.lib";\noption(redSB);\nring r=0,(%s),dp;\n'%(','.join(map(str,u+v)))
s+=to_singular(eqs,u+v)
s+='int t=timer; ideal J=modStd(I); "time",timer-t; "dim",dim(J); J;\n quit;\n'
open('q2_full.sing','w').write(s)
