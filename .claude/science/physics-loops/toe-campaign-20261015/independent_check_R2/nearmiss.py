# high-precision check that the best near-solution is a strict local minimum of the residual with positive value
import pickle, sympy as sp, mpmath as mp, numpy as np
mp.mp.dps=40
d=pickle.load(open('param.pkl','rb')); params=d['params']
eqs=pickle.load(open('eqs.pkl','rb'))
out=pickle.load(open('num_out.pkl','rb')); x=[mp.mpf(v) for v in out[1][2]]
Phi=sp.expand(sum(e**2 for e in eqs))
g=[sp.diff(Phi,p) for p in params]; H=sp.Matrix(g).jacobian(params)
fP=sp.lambdify([params],Phi,'mpmath'); fg=sp.lambdify([params],g,'mpmath'); fH=sp.lambdify([params],H,'mpmath')
for it in range(30):
    G=mp.matrix(fg(x)); Hm=mp.matrix(fH(x))
    dx=mp.lu_solve(Hm,G); x=[x[i]-dx[i] for i in range(len(x))]
    if mp.norm(dx)<mp.mpf(10)**-30: break
Hm=mp.matrix(fH(x)); ev=mp.eigsy(Hm)[0]
print("iters",it,"Phi=",mp.nstr(fP(x),10),"|grad|=",mp.nstr(mp.norm(mp.matrix(fg(x))),5))
print("Hessian eigenvalues min/max:",mp.nstr(min(ev),5),mp.nstr(max(ev),5))
print("x=",[mp.nstr(v,8) for v in x])
