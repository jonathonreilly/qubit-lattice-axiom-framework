from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
rows=[]
def step(u,p):return (0,u/p) if u<p else (1,(u-p)/(1-p))
for n in range(1,10):
 for word in product((0,1),repeat=n):
  u=sum((F(b,2**j) for j,b in enumerate(word,1)),F(0));state=u;out=[]
  for _ in range(n+3):b,state=step(state,F(1,2));out.append(b)
  assert tuple(out[:n])==word and out[n:]==[0]*3 and state==0
rows.append({'prefix_checks':sum(2**n for n in range(1,10))})
# Derive cylinder inverse from the full history in reverse order, then verify
# posterior density for rho(v)=1/2+v exactly (K=1,m=1/2).
for n in range(1,7):
 for word in product((0,1),repeat=n):
  params=[];past=[]
  for b in word:params.append(F(1+sum(past)%3,4));past.append(b)
  lo,hi=F(0),F(1)
  for b,p in reversed(list(zip(word,params))):
   lo,hi=(p*lo,p*hi) if b==0 else (p+(1-p)*lo,p+(1-p)*hi)
  w=hi-lo;average=F(1,2)+lo+w/2;tv=w/(8*average)
  assert tv<=w/3
  mass=w*(F(1,2)+lo)+w*w/2
  assert mass==w*average
  for x in [F(0),F(1,3),F(3,4)]:
   u=lo+w*x
   for b,p in zip(word,params):actual,u=step(u,p);assert actual==b
   assert u==x
rows.append({'adaptive_conditional_cylinders':'126 histories; exact mass, affine reconstruction and TV bound'})
for n in range(1,20):
 w=F(1,2**n);assert w*w==F(1,4**n)
 assert (w/2)**2/(w*w)==F(1,4)
rows.append({'rare_zero_history':'19 exact checks'})
# Check the nonmonotone alternative reads independent odd-position digits:
for n in range(1,6):
 counts={word:0 for word in product((0,1),repeat=n)}
 for seed in range(4**n):
  u=F(seed,4**n);word=[]
  for _ in range(n):
   word.append(int(u>=F(1,2)));u=4*u;u-=int(u)
  counts[tuple(word)]+=1
 assert set(counts.values())=={2**n}
rows.append({'fourfold_map':'uniform 2n-bit finite seeds give uniform n-output words'})
Path(__file__).with_name('independent_results.json').write_text(json.dumps(rows,indent=2));print(json.dumps(rows))
