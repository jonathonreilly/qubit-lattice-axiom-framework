import pickle, numpy as np, sympy as sp
from scipy.optimize import least_squares
d=pickle.load(open('param.pkl','rb')); params=d['params']
eqs=pickle.load(open('eqs.pkl','rb'))
f=sp.lambdify([params],eqs,'numpy'); J=sp.lambdify([params],sp.Matrix(eqs).jacobian(params),'numpy')
rng=np.random.default_rng(5)
out=[]
for trial in range(40):
    x0=rng.normal(size=len(params))*rng.uniform(0.05,0.6)
    r=least_squares(lambda x:np.array(f(x)),x0,jac=lambda x:np.array(J(x),float),method='lm',xtol=3e-16,ftol=3e-16,gtol=3e-16,max_nfev=50000)
    x=r.x; res=np.linalg.norm(f(x)); mov=np.linalg.norm(x[:-1])
    out.append((res,mov,x))
out.sort(key=lambda z:z[0])
for res,mov,x in out[:8]:
    print("%.3e %.4f"%(res,mov), np.round(x,4))
pickle.dump(out,open('num_out.pkl','wb'))
