AUDIT_TIMEOUT_SEC=300
import numpy as np,json
from scipy.integrate import quad
from fractions import Fraction as F
from itertools import product
L=10;gamma=F(12155,33554432);t=2*gamma
U={(4,0):-F(143*L,4194304)/t,(4,1):-F(143*L,8388608)/t,(3,2):F(333355*L,24461180928)/t}
core={(x,y) for x,y in product(range(-4,5),repeat=2) if abs(x)+abs(y)<=4 and sorted((abs(x),abs(y)))!=[0,4]}
outer={}
for x,y in product(range(-5,6),repeat=2):
 a,b=sorted((abs(x),abs(y)),reverse=True)
 if (a,b) in U:outer[x,y]=float(U[a,b])
pts=sorted(core|set(outer));inv=np.diag([0 if r in core else 1/outer[r] for r in pts]);rows=[]
for eps in (1e-2,1e-4,1e-6,1e-8,1e-10,1e-12):
 cache={}
 def green(r):
  x,y=sorted(map(abs,r),reverse=True)
  if (x,y) not in cache:
   def f(k):
    delta=eps+4*np.sin(k/2)**2;A=2+delta;root=np.sqrt(delta*(4+delta));ratio=2/(A+root)
    return np.cos(k*x)*ratio**y/root/np.pi
   cache[x,y]=quad(f,0,np.pi,epsabs=1e-10,epsrel=1e-10,points=[np.sqrt(eps)],limit=200)[0]
  return cache[x,y]
 G=np.array([[green((a[0]-b[0],a[1]-b[1])) for b in pts] for a in pts]);q=np.linalg.solve(inv+G,np.ones(len(pts)));amp=float(q.sum());B=1/amp-np.log(1/eps)/(4*np.pi)
 rows.append(dict(eps=eps,T_over_t=amp,log_ratio=amp*np.log(1/eps)/(4*np.pi),finite_part=B,scale=float(np.exp(4*np.pi*B)),residual=float(np.linalg.norm((inv+G)@q-1))))

cache={}
def potential_kernel(r):
 x,y=sorted(map(abs,r),reverse=True)
 if (x,y) not in cache:
  def f(k):
   delta=4*np.sin(k/2)**2;root=np.sqrt(delta*(4+delta));eta=2*np.arcsinh(np.sin(k/2));angle=x*k
   num=-np.expm1(-y*eta)+2*np.exp(-y*eta)*np.sin(angle/2)**2
   return num/root/np.pi
  cache[x,y]=quad(f,0,np.pi,epsabs=1e-12,epsrel=1e-12)[0]
 return cache[x,y]
C=np.array([[np.log(32)/(4*np.pi)-potential_kernel((a[0]-b[0],a[1]-b[1])) for b in pts] for a in pts]);d=len(pts);aug=np.block([[inv+C,-np.ones((d,1))],[np.ones((1,d)),np.zeros((1,1))]])
sol=np.linalg.solve(aug,np.r_[np.zeros(d),1]);B=sol[-1]
assert abs(potential_kernel((1,0))-.25)<1e-11
assert abs(potential_kernel((1,1))-1/np.pi)<1e-11
assert abs(rows[-1]['finite_part']-B)<1e-9
assert max(r['residual'] for r in rows)<1e-10
for r,u in outer.items():
 missing=sum((r[0]+dx,r[1]+dy) in core for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)))
 assert u>=-8/17*missing-1e-14
augmented_residual=float(np.linalg.norm(aug@sol-np.r_[np.zeros(d),1]))
assert np.isfinite(augmented_residual) and augmented_residual<1e-10, ('augmented residual',augmented_residual)
print(json.dumps(dict(core_size=len(core),potential_sites=len(outer),potentials={str(k):str(v) for k,v in U.items()},rows=rows,finite_matrix_part=float(B),scale=float(np.exp(4*np.pi*B)),augmented_residual=float(np.linalg.norm(aug@sol-np.r_[np.zeros(d),1])),a10=potential_kernel((1,0)),a11=potential_kernel((1,1)),scope='Leading coefficient model Euclidean zero-momentum T; not a fixed-lambda microscopic cross section'),indent=2))
