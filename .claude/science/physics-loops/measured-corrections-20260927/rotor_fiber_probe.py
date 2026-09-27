"""Exploratory finite-epsilon rotor fiber only; omits physical electric scaling."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import itertools,json
import sympy as s
import numpy as np
x,c,z=s.symbols('x c z',real=True)
b=8*(1+c)
poly=s.expand((z-4*x)*(1-z)*((1-z)*(2-z)-4*x)+4*x*((1-z)*(2-z)-4*x)+x*x*b)
series=s.Integer(0);coefficients={}
for k in range(1,6):
    a=s.Symbol(f'a{k}'); trial=series+a*x**k
    eq=s.expand(poly.subs(z,trial)).coeff(x,k)
    val=s.factor(s.solve(eq,a)[0]);coefficients[k]=str(val);series+=val*x**k
print('Schur polynomial:',poly)
print('Low-band lambda coefficients in x=epsilon^2:',coefficients)
states=list(itertools.combinations(range(4),2));lookup={v:i for i,v in enumerate(states)}
rows=[]
for phi in (.0,.7,1.8,3.0):
 for eps in (.1,.05,.025):
    h=np.diag([sum(a not in st for a in (0,2)) for st in states]).astype(complex)
    h[lookup[(0,2)],lookup[(0,2)]]+=4*eps**2
    for i,st in enumerate(states):
      for a,bb in ((0,1),(0,3),(2,1),(2,3)):
        if a in st and bb not in st:
          target=tuple(sorted((set(st)-{a})|{bb}));j=lookup[target]
          value=-eps*np.exp(1j*phi*(a==0 and bb==3))
          h[j,i]+=value;h[i,j]+=value.conjugate()
    ev=np.linalg.eigvalsh(h); exact=float(ev[0])
    estimate=float(series.subs({x:eps**2,c:np.cos(phi)}))
    polynomial=float(poly.subs({z:exact,x:eps**2,c:np.cos(phi)}))
    rows.append(dict(phi=phi,epsilon=eps,band=exact,series=estimate,error=abs(exact-estimate),schur_residual=polynomial))
print(json.dumps(rows,indent=2))
print('Exploratory diagnostic only: no joint finite-spin/electric derivation or empirical prediction.')
