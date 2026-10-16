from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json
local=[]
for table in product((0,1),repeat=4):
 A0,A1,B0,B1=table
 wins=[((A0,A1)[x]^(B0,B1)[y])==x*y for x,y in product((0,1),repeat=2)]
 assert sum(wins)<=3;local.append(wins)
for px,py in product([F(1,4),F(1,2),F(3,4)],repeat=2):
 weights=[(px if x else 1-px)*(py if y else 1-py) for x,y in product((0,1),repeat=2)]
 assert max(sum(w*b for w,b in zip(weights,win)) for win in local)==1-min(weights)
# Exact tail from exposed rational tau, using recurrence rather than floats.
tau=F(108,10000000);q=1-(F(1,2)-tau)**2;N=245;k=196
pmf=(1-q)**N;tail=F(0)
for j in range(N+1):
 if j>=k:tail+=pmf
 if j<N:pmf=pmf*F(N-j,j+1)*q/(1-q)
assert tail==sum(F(comb(N,j))*q**j*(1-q)**(N-j) for j in range(k,N+1))
# Verify all continuations for a small adversarial adaptive win process.
Nsmall=7;kmin=5;qsmall=F(3,4)
dist={():F(1)}
for t in range(Nsmall):
 nxt={}
 for history,prob in dist.items():
  actual=qsmall if sum(history)%2==0 else F(1,3)
  nxt[history+(1,)]=prob*actual;nxt[history+(0,)]=prob*(1-actual)
 dist=nxt
actualtail=sum(prob for h,prob in dist.items() if sum(h)>=kmin)
bound=sum(F(comb(Nsmall,j))*qsmall**j*(1-qsmall)**(Nsmall-j) for j in range(kmin,Nsmall+1));assert actualtail<=bound
result={'local_tables':len(local),'biased_product_cases':9,'exposed_binomial_tail':float(tail),'q':str(q),'adaptive_tail':str(actualtail),'binomial_bound':str(bound),'tau_domain_counterexample':{'tau':'3/4','constant_settings_win':'1','incorrect_formula_q':'15/16'}}
Path(__file__).with_name('independent_results.json').write_text(json.dumps(result,indent=2));print(json.dumps(result))
