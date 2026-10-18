from fractions import Fraction as F
import json,math

def row(R,L=10):
 idx=lambda x,y,z:((x%R)*R+y%R)*L+z%L
 col=sum(1<<idx(0,0,z) for z in range(L));vac={};charged={}
 for x in range(R):
  for y in range(R):
   for z in range(L):
    i=idx(x,y,z)
    for axis,dx,dy in [('x',1,0),('y',0,1)]:
     j=idx(x+dx,y+dy,z);mask=(1<<i)|(1<<j)
     hv=-1 if axis=='x' else 1
     hc=hv if axis=='x' else (-1)**((col&mask).bit_count())
     vac[mask]=vac.get(mask,F(0))-F(hv,8)
     charged[mask]=charged.get(mask,F(0))-F(hc,8)
 amp=-sum((vac[k]-charged[k])**2 for k in vac)/2
 # Odd-area Q4 rectangles: exact boundary count of four corner plaquettes.
 shapes=[]
 for a in range(1,R//2):
  for b in range(1,R//2):
   if a*b%2==0:continue
   s={(0,0),(a,0),(0,b),(a,b)}
   perimeter=sum((x+dx,y+dy) not in s for x,y in s for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)])
   shapes.append((a,b,perimeter))
 return dict(R=R,L=L,virtual_states=len(vac),amplitude_correction=str(amp),weight_correction=str(2*amp),minimum_shapes=[x for x in shapes if x[2]==8],next_perimeter=min((x[2] for x in shapes if x[2]>8),default=None))
print(json.dumps(dict(rows=[row(R) for R in [4,8,12]],gamma=str(F(math.comb(18,9),8**9))),indent=2))
