import sympy as sp, pickle, numpy as np
from scipy.optimize import least_squares
free, Fs, coeqs = pickle.load(open('q1.pkl','rb'))
f = sp.lambdify([free], coeqs, 'numpy')
J = sp.lambdify([free], sp.Matrix(coeqs).jacobian(free), 'numpy')
rng = np.random.default_rng(0)
sols=[]
for trial in range(400):
    x0 = rng.normal(size=len(free))*rng.uniform(0.05,0.6)
    r = least_squares(lambda x: np.array(f(x),float), x0, jac=lambda x: np.array(J(x),float), xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=2000)
    res = np.linalg.norm(r.fun)
    if res<1e-10: sols.append(r.x)
print('converged', len(sols), 'of 400')
names=[str(v) for v in free]
pickle.dump((names,sols), open('q1_numsols.pkl','wb'))
for x in sols[:40]:
    d = {n: round(v,6) for n,v in zip(names,x) if abs(v)>1e-7}
    print(d)
