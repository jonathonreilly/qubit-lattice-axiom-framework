"""Synthetic exact path-moment and finite-time error controls."""
from pathlib import Path
import hashlib,json,math
from collections import deque
import sympy as s
import numpy as np
P=Path(__file__).resolve().parent;checks=[]
def check(name,ok,**kw):
 assert bool(ok),name
 checks.append({'name':name,'passed':True,**kw})
def stiffness(n,edges):
 K=s.eye(n)
 for i,j,k in edges:
  w=s.zeros(n,1);w[i]=1;w[j]=-1;K+=k*w*w.T
 return K
def moments(K,e,w):
 v=e
 for d in range(K.rows):
  mu=(w.T*v)[0]
  if mu!=0:return d,mu
  v=K*v
 return None,None
rows=[]
for n in range(2,9):
 edges=[(i,i+1,i+1) for i in range(n-1)];K=stiffness(n,edges);e=s.eye(n)[:,0]
 for i,j,k in edges:
  w=s.eye(n)[:,i]-s.eye(n)[:,j];d,mu=moments(K,e,w);assert d==i
  theta=s.Rational(2,3);Kp=K+theta*w*w.T
  v=e;vp=e
  for power in range(2*d+3):
   diff=(e.T*(v-vp))[0]
   if power<2*d+1:assert diff==0
   if power==2*d+1:assert -diff==theta*mu**2
   v=K*v;vp=Kp*vp
  rows.append({'n':n,'edge':[i,j],'d':d,'mu':str(mu),'first_time_power':4*d+3})
check('weighted-chain exact Taylor orders and coefficients',True,cases=len(rows),rows=rows)
# Multiple shortest paths on a square grid; positivity precludes same-end cancellation.
N=9;edges=[]
for r in range(3):
 for c in range(3):
  u=3*r+c
  if r<2:edges.append((u,u+3,1+r+c))
  if c<2:edges.append((u,u+1,2+r+c))
K=stiffness(N,edges);e=s.eye(N)[:,0]
for i,j,k in edges:
 w=s.eye(N)[:,i]-s.eye(N)[:,j];d,mu=moments(K,e,w);assert d==min(i//3+i%3,j//3+j%3)
check('bipartite grid distance matches algebraic access order',True,edges=len(edges))
# Equal-distance triangle symmetry makes the edge invisible to the observed node.
Ktri=stiffness(3,[(0,1,1),(0,2,1),(1,2,2)]);ee=s.eye(3)[:,0];ww=s.Matrix([0,1,-1]);dd,mm=moments(Ktri,ee,ww)
y=s.symbols('y',positive=True)
assert dd is None
check('equal-distance cancellation makes an interior edge invisible',s.simplify(((y*s.eye(3)+Ktri).inv()-(y*s.eye(3)+Ktri+ww*ww.T).inv())[0,0])==0)
K=s.Matrix([[4,-1,0],[-1,5,-1],[0,-1,6]]);O=s.Matrix([[1,0,0],[0,s.Rational(3,5),-s.Rational(4,5)],[0,s.Rational(4,5),s.Rational(3,5)]]);Kp=O*K*O.T
m0=moments(K,ee,ww);m1=moments(Kp,ee,ww);m2=moments(Kp,ee,O*ww)
check('same labeled intervention separates endpoint-equivalent graphs',m0==(1,-1) and m1==(1,s.Rational(1,5)) and m2==m0,leading_coefficient_ratio=str(m0[1]**2/m1[1]**2))
# Evaluate via diagonalization at moderate times where subtraction is well conditioned.
K=np.array([[4,-1,0],[-1,5,-1],[0,-1,6]],float);w=np.array([0,1,-1.]);theta=.7;Kp=K+theta*np.outer(w,w);d=1;mu=-1;M=max(np.linalg.norm(K,2),np.linalg.norm(Kp,2));maxratio=0
for t in np.linspace(.2,2,60):
 def h(mat):
  vals,vec=np.linalg.eigh(mat)
  return np.sum(vec[0,:]**2*np.sin(np.sqrt(vals)*t)/np.sqrt(vals))
 lead=theta*mu**2*t**7/math.factorial(7);actual=h(K)-h(Kp)
 bound=2*M**4*t**9/math.factorial(9)*math.cosh(math.sqrt(M)*t)
 assert abs(actual-lead)<=bound+1e-14;maxratio=max(maxratio,abs(actual-lead)/bound)
check('finite-time remainder against spectral response',True,cases=60,maximum_error_fraction=maxratio)
result={'source_sha256':hashlib.sha256((P/'NETWORK_EVOLUTION_BLOCK10_v1.md').read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'summary':{'passed':len(checks),'failed':0},'empirical_test':False,'scope':'Finite supplied positive spring matrices, exact intervention and ideal impulse/readout. No physical lattice dynamics or hard light cone derived.'}
text=json.dumps(result,indent=2)+'\n';(P/'NETWORK_PATH_ORDER_CONTROLS_v1.json').write_text(text);print(text,end='')
