# numeric: minimize lambda1^2+lambda2^2 + penalty(neg eig) over b with b2 != 0 (rank<=2 PSD)
import numpy as np, pickle, sympy as sp
from scipy.optimize import minimize
b0,b1,b2=sp.symbols('b0 b1 b2',real=True)
Qf=sp.lambdify((b0,b1,b2),pickle.load(open('Q.pkl','rb')),'numpy')
def obj(b):
    w=np.linalg.eigvalsh(np.array(Qf(*b),float)); return w[0]**2+w[1]**2
rng=np.random.default_rng(0); best=[]
for t in range(3000):
    x0=rng.uniform(-0.8,0.8,3)
    r=minimize(obj,x0,method='Nelder-Mead',options={'xatol':1e-12,'fatol':1e-20,'maxiter':4000})
    best.append((r.fun,abs(r.x[2]),r.x))
best.sort(key=lambda t:t[0])
for f,a,x in best[:3]: print(f,x)
print("min objective with |b2|>0.01:",min(f for f,a,x in best if a>0.01))
# rank-3 surface: fraction of samples in PSD/det=0 region along b1 for fixed b0,b2
