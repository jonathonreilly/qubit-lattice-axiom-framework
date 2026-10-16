import pickle, numpy as np, sympy as sp
from scipy.optimize import least_squares
d=pickle.load(open('param.pkl','rb')); params=d['params']
eqs=pickle.load(open('eqs.pkl','rb'))
sub={p:0 for p in params[:18]}
e1=[sp.expand(e.subs(sub)) for e in eqs]; e1=[e for e in e1 if e!=0]
P=params[18:]
print(P, len(e1))
for e in e1: print(e)
f=sp.lambdify([P],e1); J=sp.lambdify([P],sp.Matrix(e1).jacobian(P))
rng=np.random.default_rng(2); out=[]
for t in range(200):
    r=least_squares(lambda x:np.array(f(x)),rng.normal(size=7)*0.5,jac=lambda x:np.array(J(x),float),method='lm',xtol=3e-16,ftol=3e-16,gtol=3e-16,max_nfev=20000)
    out.append((np.linalg.norm(f(r.x)),np.linalg.norm(r.x[:-1]),r.x))
out.sort(key=lambda z:z[0])
for o in out[:10]: print("%.3e %.4f"%o[:2],np.round(o[2],5))
