from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,math
rows=[]
for B in range(1,5):
 for N in range(1,11):
  allowed=0;tv=F(0);qsum=F(0)
  for word in product((-1,1),repeat=N):
   state=0;q=F(1);ok=True
   for x in word:
    if abs(state)==B:
     if x*state>0:q=F(0)
    else:q/=2
    state+=x
    if abs(state)>B:ok=False;q=F(0)
   allowed+=ok;qsum+=q;tv+=abs(q-F(1,2**N))/2
  survival=F(allowed,2**N)
  assert qsum==1 and tv==1-survival
  assert float(survival)<=min(1,math.sqrt(2*B+1)*math.cos(math.pi/(2*B+2))**N)+1e-14
  if B==1:assert survival==F(1,2**(N//2))
 rows.append({'B':B,'enumeration_horizons':'1..10'})
for B in range(1,9):
 states=list(range(-B,B+1));pi={x:F(1,4*B) if abs(x)==B else F(1,2*B) for x in states}
 def choices(x):return [(-1,F(1))] if x==B else [(1,F(1))] if x==-B else [(-1,F(1,2)),(1,F(1,2))]
 stationary={x:F(0) for x in states};lag=F(0)
 for x in states:
  for inc,prob in choices(x):
   stationary[x+inc]+=pi[x]*prob
   for nxt,prob2 in choices(x+inc):lag+=pi[x]*prob*prob2*inc*nxt
 assert stationary==pi and lag==-F(1,2*B)
 rows.append({'stationary_B':B,'lag':str(lag)})
Path(__file__).with_name('independent_results.json').write_text(json.dumps(rows,indent=2));print(json.dumps(rows))
