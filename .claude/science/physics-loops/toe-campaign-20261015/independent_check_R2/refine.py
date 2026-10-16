import pickle, numpy as np, sympy as sp
from scipy.optimize import least_squares
d=pickle.load(open('param.pkl','rb')); params=d['params']
eqs=pickle.load(open('eqs.pkl','rb'))
f=sp.lambdify([params],eqs,'numpy'); J=sp.lambdify([params],sp.Matrix(eqs).jacobian(params),'numpy')
out=pickle.load(open('num_out.pkl','rb'))
x=out[1][2]
for it in range(10):
    r=least_squares(lambda x:np.array(f(x)),x,jac=lambda x:np.array(J(x),float),method='lm',xtol=3e-16,ftol=3e-16,gtol=3e-16,max_nfev=100000)
    x=r.x; Jx=np.array(J(x),float); sv=np.linalg.svd(Jx,compute_uv=False)
    print(it,r.nfev,"res %.3e"%np.linalg.norm(f(x)),"min sv %.2e"%sv[-1], np.round(x[:18],5))
