# numerical search for moving solutions (supporting evidence only)
import pickle, numpy as np, sympy as sp
from scipy.optimize import least_squares
d=pickle.load(open('param.pkl','rb')); params=d['params']
eqs=pickle.load(open('eqs.pkl','rb'))
a0=[p for p in params if d['c0'][(0,0,0)]==p][0]
print("constant-term param",a0)
f=sp.lambdify([params],eqs,'numpy'); J=sp.lambdify([params],sp.Matrix(eqs).jacobian(params),'numpy')
idx=params.index(a0)
rng=np.random.default_rng(0)
best=[]
for t in [None,0.0,0.3,0.6,0.9,-0.5]:
    for trial in range(60):
        x0=rng.normal(size=len(params))*rng.uniform(0.05,0.6)
        if t is None:
            r=least_squares(lambda x:np.array(f(x)),x0,jac=lambda x:np.array(J(x),float),xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=2000)
            x=r.x
        else:
            free=[i for i in range(len(params)) if i!=idx]
            def full(y): x=np.empty(len(params)); x[free]=y; x[idx]=t; return x
            r=least_squares(lambda y:np.array(f(full(y))),x0[free],jac=lambda y:np.array(J(full(y)),float)[:,free],xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=2000)
            x=full(r.x)
        res=np.linalg.norm(f(x)); mov=np.linalg.norm(np.delete(x,idx))
        best.append((res,mov,t))
best.sort(key=lambda z:z[0])
print("smallest residuals (res, norm of non-constant params, fixed a0):")
for b in best[:15]: print(b)
mv=[b for b in best if b[1]>1e-3]
print("best residual among moving candidates:",min(mv)[:2] if mv else None)
