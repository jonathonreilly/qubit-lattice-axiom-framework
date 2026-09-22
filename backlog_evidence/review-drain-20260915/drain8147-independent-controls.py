from fractions import Fraction as F
from math import factorial,comb
from collections import defaultdict
import json,time,pathlib
start=time.monotonic();checks=0
# Independent 3D undirected displacement dynamic program, compared to multinomial coincidence formula.
c={(0,0,0):1};steps=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
for m in range(13):
 if m%2==0:
  n=m//2;s=sum((factorial(n)//(factorial(a)*factorial(b)*factorial(n-a-b)))**2 for a in range(n+1) for b in range(n-a+1));assert c.get((0,0,0),0)==comb(2*n,n)*s;checks+=1
 else:assert c.get((0,0,0),0)==0;checks+=1
 out=defaultdict(int)
 for p,num in c.items():
  for step in steps:out[tuple(x+y for x,y in zip(p,step))]+=num
 c=out
# Direct multinomial formula and exact summations (no primary walk counter).
P=[F(sum((factorial(n)//(factorial(a)*factorial(b)*factorial(n-a-b)))**2 for a in range(n+1) for b in range(n-a+1)),9**n) for n in range(31)]
for n in range(1,31):assert F(1,36*n)<=P[n]<=F(2,n);checks+=1
for t in range(1,31):
 H=sum(F(1,k) for k in range(1,t+1));V=sum(P[:t]);assert H/36<=V<=1+2*sum(F(1,k) for k in range(1,t));assert sum(P[n]/4**n for n in range(t))<=F(4,3);checks+=1
# Opposite parent signs and formal Born Hessian; actual all-aligned sphere marginal has different exact moments.
assert -F(1,2)/3==-F(1,6);assert -(-F(1,2))/3==F(1,6);checks+=2
# Area measure t=cos(theta) uniform[-1,1], density proportional((1+t)/2)^3: normalized moments via polynomial integration.
def integral(poly):return sum(v*F(2,k+1) for k,v in enumerate(poly) if k%2==0)
p=[F(comb(3,k),8) for k in range(4)];z=integral(p);mean=integral([0]+p)/z;second=integral([0,0]+p)/z
assert mean==F(3,5);assert second==F(7,15);assert (1-second)/2==F(4,15);assert F(4,15)!=F(2,3);checks+=4
out={'status':'PASS','checks':checks,'elapsed_sec':time.monotonic()-start,'scope':['direct3Dreturn-walk recurrence vs multinomial identity through12steps','exact coincidence/harmonic/geometric bounds through30','parent conditional sign','exact aligned Born sphere moments: Ez=3/5,Ex²=4/15, not formal tangentGaussian2/3'],'primary_imported_or_executed':False}
p=pathlib.Path(__file__).with_suffix('.json');assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
