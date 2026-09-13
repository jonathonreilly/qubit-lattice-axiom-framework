"""Find and derive one representation-specific time-sliced weight witness."""
from pathlib import Path
import json,itertools,numpy as np,sympy as sy
from scipy.linalg import expm
P=Path(__file__).resolve().parent
sx=sy.Matrix([[0,1],[1,0]]);sz=sy.diag(1,-1);s2=sy.Matrix([[0,-sy.I],[sy.I,0]]);ii=sy.eye(2)
s=[sy.kronecker_product(ii,x) for x in [sx,s2,sz]]
sb=sy.Rational(4,5);cb=sy.Rational(3,5);mu=sy.Rational(1,5);zeta=sy.Rational(3,5)
on=(2+zeta)*s[2]+mu*sy.kronecker_product(sx,sb*sx+cb*sz)
hops=[(-sb*s[0]-cb*s[2]-sy.I*sy.kronecker_product(sz,cb*sx-sb*sz))/2,(-s[2]-sy.I*s[1])/2]
def h(phases,edges,ncells):
 a=sy.Matrix(sy.kronecker_product(sy.eye(ncells),on))
 for p,(x,y,k) in zip(phases,edges):
  v=hops[k]*sy.I**p
  a[4*x:4*x+4,4*y:4*y+4]+=v;a[4*y:4*y+4,4*x:4*x+4]+=v.adjoint()
 return a
# Try the smallest open edge before the four-cell square.
fixtures=[]
for axis in [0,1]:
 hs=[h([p],[(0,1,axis)],2) for p in [0,1,2]]
 m=np.eye(8,dtype=complex)
 for a in hs:m=expm(-.4*np.array(a,complex))@m
 phase=float(np.angle(np.linalg.slogdet(np.eye(8)+m)[0]))
 fixtures.append((abs(phase),phase,axis,hs))
absphase,phase,axis,hs=max(fixtures,key=lambda x:x[0])
print('one_edge_phases',[(v[1],v[2]) for v in fixtures],flush=True)
if absphase<1e-7:
 edges=[(0,1,0),(0,2,1),(1,3,1),(2,3,0)];rng=np.random.default_rng(12)
 for k in range(100):
  ps=rng.integers(0,4,(3,4)).tolist();hh=[h(p,edges,4) for p in ps];m=np.eye(16,dtype=complex)
  for a in hh:m=expm(-.4*np.array(a,complex))@m
  ph=float(np.angle(np.linalg.slogdet(np.eye(16)+m)[0]))
  if abs(ph)>1e-4:hs=hh;phase=ph;break
 fixture=dict(edges=edges,phase_quarters=ps)
else:fixture=dict(edges=[(0,1,axis)],phase_quarters=[[0],[1],[2]])
print('fixture',fixture,'phase',phase,flush=True)
n=hs[0].rows;order=5;Z=sy.zeros(n)
def mul(a,b):
 return [sum((a[j]*b[k-j] for j in range(k+1)),Z.copy()) for k in range(order+1)]
coeff=[sy.eye(n)]+[Z.copy() for _ in range(order)]
for a in hs:
 powers=[sy.eye(n)]
 for k in range(1,order+1):powers.append(powers[-1]*(-a)/k)
 coeff=mul(powers,coeff)
x=[Z.copy()]+[a/2 for a in coeff[1:]];power=x;logs=[sy.S(0)]*(order+1)
for r in range(1,order+1):
 for k in range(1,order+1):logs[k]+=(-1)**(r+1)*sy.trace(power[k])/r
 if r<order:power=mul(power,x)
logs=[sy.simplify(v) for v in logs]
result=dict(fixture=fixture,parameters=dict(sin_b='4/5',cos_b='3/5',zeta='3/5',mu='1/5',theta='b'),phase_at_step_point4=phase,log_weight_coefficients=[str(v) for v in logs],imag_coefficients=[str(sy.im(v)) for v in logs])
(P/'BLOCK12_EXACT_PHASE_WITNESS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
