#!/usr/bin/env python3
"""Additional finite injectivity controls, not a limiting-measure test."""
from pathlib import Path
import hashlib,itertools,json,math
import numpy as np
import sympy as s
here=Path(__file__).resolve().parent
checks=[]
def ck(name,ok,**detail): checks.append(dict(name=name,passed=bool(ok),**detail))
X=np.array(list(itertools.product([-1,1],repeat=7)))
index={tuple(x):i for i,x in enumerate(X)}
plaquettes=[(0,5,2,4),(1,6,3,5)]
loops=np.array([np.prod(X[:,p],axis=1) for p in plaquettes]).T
beta=.4
A=np.exp(-beta/2*np.sum(1-loops,axis=1))
k=np.prod(1+math.tanh(beta)*X[:,None,:]*X[None,:,:],axis=2)/len(X)
T=A[:,None]*k*A[None,:]
eig,vec=np.linalg.eigh(T)
psi=vec[:,-1]*math.sqrt(len(X))
if psi.sum()<0: psi=-psi
u=A*psi
pi=psi*psi/len(X)
Q=k*u[None,:]/(k@u)[:,None]
B=[0,5]
worst=0.
wrong=0.
for i,U in enumerate(X):
 Up=U.copy(); Up[B]*=-1
 j=index[tuple(Up)]
 H=beta*(X[:,B]@(Up[B]-U[B]))
 raw=np.exp(H)*Q[i]
 tilted=raw/raw.sum()
 worst=max(worst,float(np.max(np.abs(tilted-Q[j]))))
 wrong=max(wrong,abs(float(raw.sum())-1))
ck('actual full probability tilt for two changed boundary links',worst<3e-14,error=worst)
ck('mutation: dropping tilt normalizer is detected',wrong>1e-5,max_row_sum_error=wrong)
ck('actual tilted kernel remains stationary under Perron pi',np.max(np.abs(pi@Q-pi))<3e-14)
outside=[i for i in range(7) if i not in B]
pB=sum(bool(set(B)&set(p)) for p in plaquettes)
L=2*beta*pB+4*beta*len(B)
conditional_densities=[]
for z in itertools.product([-1,1],repeat=len(outside)):
 inds=np.where(np.all(X[:,outside]==z,axis=1))[0]
 densities=pi[inds]/pi[inds].sum()*2**len(B)
 conditional_densities.extend(densities)
ck('actual block conditional pi density lower and upper bounds',
   min(conditional_densities)>=math.exp(-L) and max(conditional_densities)<=math.exp(L),
   p_B=pB,b=len(B),minimum=float(min(conditional_densities)),maximum=float(max(conditional_densities)))
r=s.Rational(1,3)
K1=s.Matrix([[1+r,1-r],[1-r,1+r]])/2
for n in (1,2,3):
 K=K1
 for _ in range(n-1): K=s.kronecker_product(K,K1)
 S=np.array(list(itertools.product([-1,1],repeat=n)))
 for support in itertools.chain.from_iterable(itertools.combinations(range(n),j) for j in range(n+1)):
  f=s.Matrix([int(np.prod(x[list(support)])) if support else 1 for x in S])
  lam=r**len(support)
  ck(f'exact character multiplier n={n}, support={support}',K*f==lam*f and lam>0)
 alpha=s.Matrix([s.Rational((-1)**j*(j+1),17) for j in range(2**n)])
 ck(f'exact signed-measure recovery n={n}',K.inv()*(K*alpha)==alpha)
f=s.Matrix([1,-1])
haar=s.ones(2,2)/2
mutated=K1-r*f*f.T/2
ck('zero-coefficient mutation: positive operator is not injective',
   mutated==haar and mutated*f==s.zeros(2,1) and f!=s.zeros(2,1) and mutated.det()==0)
# A genuine finite endpoint witness can coexist with an unrelated zero mode.
extra=s.diag(1,s.Rational(1,2),0)
ck('single positive excited witness is insufficient for full injectivity',
   extra[1,1]>0 and extra*s.Matrix([0,0,1])==s.zeros(3,1))
result=dict(scope='finite supporting controls for the analytic infinite-volume injectivity supplement',
 script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,
 passed=sum(c['passed'] for c in checks),total=len(checks),all_passed=all(c['passed'] for c in checks),
 untested_analytic_steps=['canonical all-boundary-field infinite half-space Gibbs kernels',
 'stationarity and conditional domination after the thermodynamic limit',
 'common full-measure Fubini set for countable exhaustion','finite signed-measure Peter-Weyl uniqueness',
 'L1 martingale convergence'],MG_rows_closed=[],independent_review=False)
(here/'massgap_block_injectivity_results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:result[k] for k in ['passed','total','all_passed']}))
for c in checks:
 if not c['passed']: print(c)
raise SystemExit(0 if result['all_passed'] else 1)
