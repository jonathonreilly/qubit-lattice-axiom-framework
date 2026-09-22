from fractions import Fraction as F
from itertools import product,combinations
from math import prod
from pathlib import Path
import signal,time,json
signal.alarm(30); t=time.monotonic(); out={}
def phi(a,b,w): return w[0] if a==b else w[1] if a//2==b//2 else w[2]
def z(v,w): return sum(prod(phi(s,a,w) for a in v) for s in range(6))
def ratio(v,w):
 k=len(v); n=d=1
 for mask in range(1<<k):
  val=z([v[i] if mask>>i&1 else 0 for i in range(k)],w)
  if (k-mask.bit_count())%2: d*=val
  else:n*=val
 return F(n,d)
for w in [(3,1,2),(5,2,4)]:
 vals={k:ratio(([1]*k if k%2==0 else [1]*(k-1)+[2]),w) for k in range(2,7)}
 assert all(x!=1 for x in vals.values());out[str(w)]={k:str(v) for k,v in vals.items()}
assert all(ratio([1]*(k-1)+[2],(2,2,2))==1 for k in range(2,7))
# Direct Bernoulli cellular automaton on projected level coordinates: each successor uses self,left,down.
pts=list(product(range(3),repeat=2)); total=0; worst=0
for mask in range(1,1<<len(pts)):
 cur={pts[i] for i in range(len(pts)) if mask>>i&1}; initial=set(cur)
 # Lift initial level to t0=0 as(-j-k,j,k).
 bound=max(-j-k for j,k in cur)+max(j for j,k in cur)+max(k for j,k in cur)+1
 n=0
 while cur:
  possible=cur|{(j+1,k) for j,k in cur}|{(j,k+1) for j,k in cur}
  cur={(j,k) for j,k in possible if sum(v in cur for v in [(j,k),(j-1,k),(j,k-1)])>=2}
  n+=1
  assert n<=bound,(initial,n,bound)
 total+=1;worst=max(worst,n)
out['eroder_nonempty_islands']=total;out['largest_lifetime']=worst
# Exact normalizer closed forms, all 216 predecessor assignments at five p values: maximal defect with >=2 copies.
errors={}
for P in [3,10,30,100,1000]:
 w=(P,1,2); errors[P]=str(max(1-F(prod(phi(0,a,w) for a in v),z(v,w)) for v in product(range(6),repeat=3) if v.count(0)>=2))
assert list(errors.values())==['35/44','21/71','71/971','211/10211','2011/1002011']
out['noise_errors']=errors;out['elapsed_seconds']=time.monotonic()-t
Path('/private/tmp/review-drain-20260915/drain8146-independent-finite-controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
