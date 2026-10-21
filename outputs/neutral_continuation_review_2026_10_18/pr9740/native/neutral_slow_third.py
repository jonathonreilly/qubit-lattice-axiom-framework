"""Canonical third-order native matrix elements, exact rational local paths."""
from fractions import Fraction as F
import json,time

def kernel(ell,r,s,target_ell=None):
 target_ell=ell if target_ell is None else target_ell
 nx=8;ny=7;nz=max(ell,target_ell)+6
 def bit(x,y,z):return 1<<((x*ny+y)*nz+z)
 def cfg(pair,length):return sum(bit(x+2,y+2,z+3) for x,y in [(0,0),pair] for z in range(length))
 a=cfg(r,ell);b=cfg(s,target_ell);diff=a^b
 edges=[]
 for x in range(nx):
  for y in range(ny):
   for z in range(nz):
    for dx,dy,axis in [(1,0,'x'),(0,1,'y')]:
     if x+dx<nx and y+dy<ny:edges.append((bit(x,y,z)|bit(x+dx,y+dy,z),axis))
 lookup=dict(edges);mask=(1<<(nx*ny*nz))-1
 # Outside longitudinal neighbors are fixed up. Each column has explicit top/bottom bits.
 zlast=sum(bit(x,y,nz-1) for x in range(nx) for y in range(ny))
 def energy(state):return 2*((state ^ (state>>1)) & (mask ^ zlast)).bit_count()+2*(state & zlast).bit_count()+2*(state & (zlast>>(nz-1))).bit_count()
 def amp(state,m,t):return -1 if t=='x' else (-1)**((state&m).bit_count())
 total=F(0);unfold=F(0);fold=F(0);paths=0
 for m1,t1 in edges:
  st1=a^m1;e1=energy(st1);q1=8-e1
  for m2,t2 in edges:
   m3=diff^m1^m2
   if m3 not in lookup:continue
   st2=st1^m2;e2=energy(st2);q2=8-e2
   coeff=F(1,q1*q2) if q1 and q2 else -F(1,2*q1*q1) if q1 else -F(1,2*q2*q2) if q2 else F(0)
   value=amp(a,m1,t1)*amp(st1,m2,t2)*amp(st2,m3,lookup[m3])*coeff
   total+=value;paths+=1
   if q1 and q2:unfold+=value
   else:fold+=value
 assert energy(a)==energy(b)==8
 return dict(ell=ell,r=r,s=s,target_ell=target_ell,coefficient=str(total),unfolded=str(unfold),folded=str(fold),paths=paths,edges=len(edges))
if __name__=='__main__':
 rows=[kernel(ell,r,s,L) for ell,r,s,L in [(3,(2,0),(1,0),3),(3,(2,0),(3,0),3),(3,(2,0),(2,1),3),(3,(0,2),(0,1),3),(3,(2,0),(1,0),2),(3,(2,0),(1,0),1),(4,(2,0),(1,0),4),(4,(2,0),(3,0),4),(3,(2,0),(2,0),4)]]
 out=dict(rows=rows,scope='Exact canonical K3 local matrix elements, H0 energy8; supplied uniform reference')
 print(json.dumps(out,indent=2));open(__file__.replace('.py','.json'),'w').write(json.dumps(out,indent=2)+'\n')
