from fractions import Fraction as F
from math import comb
import json

def cycle(w,h):
 pts=[(x,0) for x in range(w+1)]+[(w,y) for y in range(1,h+1)]+[(x,h) for x in range(w-1,-1,-1)]+[(0,y) for y in range(h-1,0,-1)]
 return [(i,(i+1)%len(pts),int(pts[i][0]==pts[(i+1)%len(pts)][0])) for i in range(len(pts))]
def calc(w,h):
 es=cycle(w,h);n=len(es);full=(1<<n)-1;dp=[F(0)]*(full+1);dp[0]=F(1)
 spins=[0]*(full+1)
 for mask in range(1,full+1):
  b=(mask&-mask).bit_length()-1;i,j,y=es[b];spins[mask]=spins[mask^(1<<b)]^(1<<i)^(1<<j)
  for b,(i,j,y) in enumerate(es):
   if mask>>b&1:
    old=mask^(1<<b);state=spins[old];phase=(-1 if not y else (-1 if ((state>>i)^(state>>j))&1 else 1));dp[mask]+=phase*dp[old]
  if mask!=full:dp[mask]/=-4*spins[mask].bit_count()
 return str(dp[full])
rows=[]
for w,h in [(1,1),(2,1),(3,1),(2,2)]:rows.append(dict(w=w,h=h,coefficient=calc(w,h)))
heights=[]
for L in [8,10,12]:
 c=F(9*L,262144);gamma=F(comb(2*L-2,L-1),8**(L-1));v=8*c
 heights.append(dict(L=L,c=str(c),gamma=str(gamma),v=str(v),v_over_two_gamma=str(v/(2*gamma)),parallel_curvature=str(4*gamma*gamma/v)))
print(json.dumps(dict(loops=rows,heights=heights)))
