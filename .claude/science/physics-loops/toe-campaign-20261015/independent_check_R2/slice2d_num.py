import pickle, numpy as np, sympy as sp
from scipy.optimize import least_squares
d=pickle.load(open('slice2d.pkl','rb')); P=d['params']; eqs=d['eqs']
f=sp.lambdify([P],eqs); J=sp.lambdify([P],sp.Matrix(eqs).jacobian(P))
c=P.index(d['c0'][(0,0,0)])
rng=np.random.default_rng(0); out=[]
for t in range(300):
    r=least_squares(lambda x:np.array(f(x)),rng.normal(size=len(P))*rng.uniform(.05,.7),jac=lambda x:np.array(J(x),float),method='lm',xtol=3e-16,ftol=3e-16,gtol=3e-16,max_nfev=20000)
    out.append((np.linalg.norm(f(r.x)),np.linalg.norm(np.delete(r.x,c)),r.x))
out.sort(key=lambda z:z[0])
mv=[o for o in out if o[1]>1e-4]
print("n solutions res<1e-12:",sum(o[0]<1e-12 for o in out),"moving among them:",sum(o[0]<1e-12 and o[1]>1e-4 for o in out))
for o in mv[:6]: print("%.3e %.3f"%o[:2],np.round(o[2],5))
print(P)
