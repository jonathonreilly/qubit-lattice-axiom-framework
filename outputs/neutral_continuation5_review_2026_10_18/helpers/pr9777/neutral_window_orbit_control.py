"""Exact bit-state orbit/control checks, not full Hilbert-space diagonalization."""
from collections import defaultdict

def run_checks():
 nx=ny=4;nz=8;V=nx*ny*nz
 def index(x,y,z):return (x*ny+y)*nz+z
 cols=[sum(1<<index(x,y,z) for z in range(nz)) for x in range(nx) for y in range(ny)]
 xplanes=[sum(cols[x*ny+y] for y in range(ny)) for x in range(nx)]
 yplanes=[sum(cols[x*ny+y] for x in range(nx)) for y in range(ny)]
 low=sum(1<<index(x,y,0) for x in range(nx) for y in range(ny));full=(1<<V)-1
 def shift(s,k):
  return ((s<<k)&full&~sum(low<<j for j in range(k))) | ((s>>(nz-k))&sum(low<<j for j in range(k)))
 def walls(s):return (s^shift(s,1)).bit_count()
 def C(s):return V-2*(s^shift(s,2)).bit_count()
 bonds=[(1<<index(x,y,z)|1<<index((x+1)%nx,y,z),'x') for x in range(nx) for y in range(ny) for z in range(nz)]
 bonds += [(1<<index(x,y,z)|1<<index(x,(y+1)%ny,z),'y') for x in range(nx) for y in range(ny) for z in range(nz)]
 def K(s):
  d=defaultdict(int)
  for mask,a in bonds:
   t=s^mask
   if walls(t)==4:d[t]+= -1 if a=='x' else (-1)**((s&mask).bit_count())
  return {t:c for t,c in d.items() if c}
 seeds=[(1<<index(0,0,2))|(1<<index(1,0,2)),(1<<index(0,0,2))|(1<<index(0,1,2)),(1<<index(0,0,2))|(1<<index(2,2,2))]
 seedK=[K(s) for s in seeds];seen=set();checks=0
 for rb in range(1<<(nx-1)):
  xm=0
  for x in range(1,nx):
   if rb>>(x-1)&1:xm^=xplanes[x]
  for cb in range(1<<ny):
   ym=0
   for y in range(ny):
    if cb>>y&1:ym^=yplanes[y]
   flip=xm^ym
   def phase(s):return (-1)**((s&ym).bit_count())
   support=set()
   for s,ks in zip(seeds,seedK):
    assert walls(s^flip)==4 and C(s^flip)==C(s)
    left={t:phase(s)*v for t,v in K(s^flip).items()}
    right={t^flip:phase(t)*v for t,v in ks.items()}
    assert left==right
    support.add(s^flip);support.update(t^flip for t in ks);checks+=1
   assert not support&seen
   seen.update(support)
 return dict(physical_qubits=V,backgrounds=2**(nx+ny-1),seed_and_symmetry_checks=checks,disjoint_seed_residual_configurations=len(seen),scope='Exact physical-bit N4 K1/plane/source covariance and disjoint short-interval background supports; not128-qubit diagonalization or a finite-lambda full-H spectral test')
if __name__=='__main__':
 import json
 print(json.dumps(run_checks(),indent=2))
