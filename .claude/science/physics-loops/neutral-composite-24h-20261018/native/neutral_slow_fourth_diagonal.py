"""Canonical K4 diagonal when K1|a>=0, joined exact two-step paths."""
from fractions import Fraction as F
from collections import defaultdict
import json,time,sys

def run(ell):
 nx=7;ny=5;nz=ell+6
 def bit(x,y,z):return 1<<((x*ny+y)*nz+z)
 a=sum(bit(x,y,z) for x,y in [(2,2),(4,2)] for z in range(3,3+ell))
 edges=[]
 for x in range(nx):
  for y in range(ny):
   for z in range(nz):
    for dx,dy,t in [(1,0,0),(0,1,1)]:
     if x+dx<nx and y+dy<ny:edges.append((bit(x,y,z)|bit(x+dx,y+dy,z),t))
 last=sum(bit(x,y,nz-1) for x in range(nx) for y in range(ny));first=last>>(nz-1);mask=((1<<(nx*ny*nz))-1)^last
 def energy(s):return 2*(((s^(s>>1))&mask).bit_count()+(s&last).bit_count()+(s&first).bit_count())
 def amp(s,m,t):return (-1)**((s&m).bit_count()) if t else -1
 def diag(s):
  E=energy(s);cost=[energy(s^m)-E for m,t in edges];assert set(cost)<={4,8}
  signs=[amp(s,m,t) for m,t in edges];B={0:-sum(8//c for c in cost)};A={0:sum(64//(c*c) for c in cost)}
  for i,(m,t) in enumerate(edges):
   for j in range(i+1,len(edges)):
    mm,tt=edges[j];d=m^mm
    s1=signs[i]*amp(s^m,mm,tt);s2=signs[j]*amp(s^mm,m,t)
    b=-s1*(8//cost[i])-s2*(8//cost[j]);aa=s1*(64//cost[i]**2)+s2*(64//cost[j]**2)
    if b:B[d]=B.get(d,0)+b
    if aa:A[d]=A.get(d,0)+aa
  # Sum by denominator to retain exact cancellation cheaply.
  sums=defaultdict(int);fold=0
  for d,b in B.items():
   delta=E-energy(s^d)
   if delta:sums[delta]+=b*b
   else:fold+=b*A.get(d,0)
  unfolded=sum((F(v,64*k) for k,v in sums.items()),F(0))
  folded=-F(fold,512)
  return unfolded+folded,dict(unfolded=str(unfolded),folded=str(folded),states=len(B))
 start=time.time();d,details=diag(a);v,vd=diag(0)
 out=dict(ell=ell,edges=len(edges),native=str(d),vacuum=str(v),excess=str(d-v),details=details,vacuum_details=vd,elapsed=time.time()-start)
 print(out,flush=True);return out
if __name__=='__main__':
 rows=[run(ell) for ell in [3,4,5,6,8]]
 open(__file__.replace('.py','.json'),'w').write(json.dumps(rows,indent=2)+'\n')
