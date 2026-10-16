import sympy as sp, pickle, numpy as np, sys
from scipy.optimize import least_squares
free, Fs, coeqs = pickle.load(open('q1.pkl','rb'))
names=[str(v) for v in free]; i0 = names.index('x0_0')
sub = [e.subs(free[i0],0) for e in coeqs]; fr = [v for v in free if v!=free[i0]]
f = sp.lambdify([fr], sub, 'numpy'); J = sp.lambdify([fr], sp.Matrix(sub).jacobian(fr), 'numpy')
rng = np.random.default_rng(int(sys.argv[1]))
sols=[]
for trial in range(int(sys.argv[2])):
    x0 = rng.normal(size=len(fr))*rng.uniform(0.1,0.7)
    r = least_squares(lambda x: np.array(f(x),float), x0, jac=lambda x: np.array(J(x),float), xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=3000)
    if np.linalg.norm(r.fun)<1e-10: sols.append(r.x)
print('found', len(sols))
frn=[str(v) for v in fr]
for x in sols:
    print({n: round(float(v),6) for n,v in zip(frn,x) if abs(v)>1e-6})
pickle.dump((frn,sols), open(f'q1_r0zero_{sys.argv[1]}.pkl','wb'))
