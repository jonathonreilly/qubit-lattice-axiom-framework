from fractions import Fraction as F
from collections import defaultdict
import json,time

def run(ell):
 nx=5;ny=7;nz=ell+9
 def bit(x,y,z):return 1<<((x*ny+y)*nz+z)
 def cfg(lo,hi):return sum(bit(x,y,z) for x,y in [(2,2),(2,4)] for z in range(lo,hi))
 edges=[]
 for x in range(nx):
  for y in range(ny):
   for z in range(nz):
    for dx,dy,t in [(1,0,0),(0,1,1)]:
     if x+dx<nx and y+dy<ny:edges.append((bit(x,y,z)|bit(x+dx,y+dy,z),t))
 last=sum(bit(x,y,nz-1) for x in range(nx) for y in range(ny));first=last>>(nz-1);mask=((1<<(nx*ny*nz))-1)^last
 def energy(s):return 2*(((s^(s>>1))&mask).bit_count()+(s&last).bit_count()+(s&first).bit_count())
 def amp(s,m,t):return (-1)**((s&m).bit_count()) if t else -1
 def paths(s):
  E=energy(s);cost=[energy(s^m)-E for m,t in edges];assert set(cost)<={4,8}
  signs=[amp(s,m,t) for m,t in edges];B={s:-sum(8//c for c in cost)};A={s:sum(64//(c*c) for c in cost)}
  for i,(m,t) in enumerate(edges):
   for j in range(i+1,len(edges)):
    mm,tt=edges[j];d=s^m^mm
    s1=signs[i]*amp(s^m,mm,tt);s2=signs[j]*amp(s^mm,m,t)
    b=-s1*(8//cost[i])-s2*(8//cost[j]);aa=s1*(64//cost[i]**2)+s2*(64//cost[j]**2)
    if b:B[d]=B.get(d,0)+b
    if aa:A[d]=A.get(d,0)+aa
  return B,A
 a=cfg(3,3+ell);B,A=paths(a);rows=[]
 for lo,hi in [(3,4+ell),(3,5+ell),(4,4+ell),(2,4+ell)]:
  b=cfg(lo,hi);BB,AA=paths(b);sums=defaultdict(int);fold=0
  for s in B.keys()|A.keys():
   delta=8-energy(s)
   if delta:sums[delta]+=B.get(s,0)*BB.get(s,0)
   else:fold+=A.get(s,0)*BB.get(s,0)+B.get(s,0)*AA.get(s,0)
  unf=sum((F(v,64*k) for k,v in sums.items()),F(0));fo=-F(fold,1024)
  row=dict(ell=ell,target=[lo-3,hi-3],coefficient=str(unf+fo),unfolded=str(unf),folded=str(fo));rows.append(row);print(row,flush=True)
 return rows
if __name__=='__main__':
 rows=run(5)
 open(__file__.replace('.py','.json'),'w').write(json.dumps(rows,indent=2)+'\n')
