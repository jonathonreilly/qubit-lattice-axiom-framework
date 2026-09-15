from fractions import Fraction as Q
from itertools import product
from collections import defaultdict
from pathlib import Path
import json,sympy as sy
vectors=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
def kernel(triple):
 vals={1:triple[0],-1:triple[1],0:triple[2]}
 return [[vals[sum(u*v for u,v in zip(a,b))] for b in vectors] for a in vectors]
def causal(config,h,w,phi):
 result=Q(1)
 for i in range(h*w):
  parents=([i-w] if i>=w else [])+([i-1] if i%w else [])
  vals=[]
  for a in range(6):
   v=1
   for p in parents:v*=phi[a][config[p]]
   vals.append(v)
  result*=Q(vals[config[i]],sum(vals))
 return result
phi=kernel((3,1,2));law={x:causal(x,2,3,phi) for x in product(range(6),repeat=6)};assert sum(law.values())==1
# Independently generated causal laws, no rectangle edge/normalizer formula used.
for inds,h,w in [((0,1,3,4),2,2),((1,2,4,5),2,2),((0,1,2),1,3),((3,4,5),1,3)]:
 marg=defaultdict(Q)
 for x,p in law.items():marg[tuple(x[i] for i in inds)]+=p
 assert all(p==causal(x,h,w,phi) for x,p in marg.items())
assert all(p==law[tuple(reversed(x))] for x,p in law.items())
reflect=lambda x:(x[2],x[1],x[0],x[5],x[4],x[3])
tv=sum(abs(p-law[reflect(x)]) for x,p in law.items())/2
assert tv==Q(2764753,79505712)
records=[];n=0
for triple in ((3,1,2),(5,2,4),(2,2,1),(2,2,2)):
 phi=kernel(triple);H=[[sum(phi[a][k]*phi[k][b] for k in range(6)) for b in range(6)] for a in range(6)]
 for seed in range(12):
  x=[(i*i+seed*i+seed)%6 for i in range(9)]
  probabilities=[]
  for a in range(6):x[4]=a;probabilities.append(causal(x,3,3,phi))
  probabilities=[p/sum(probabilities) for p in probabilities]
  pair=[Q(phi[a][x[1]]*phi[a][x[3]]*phi[a][x[5]]*phi[a][x[7]],H[a][x[2]]*H[a][x[6]]) for a in range(6)]
  pair=[p/sum(pair) for p in pair];assert probabilities==pair;n+=1
 for c in range(6):
  vals=[];mirror=[]
  for a in range(6):
   x=[c]*9;x[4]=a;vals.append(causal(x,3,3,phi));mirror.append(causal((x[2],x[1],x[0],x[5],x[4],x[3],x[8],x[7],x[6]),3,3,phi))
  norm=[p/sum(vals) for p in vals];static=[Q(phi[a][c]**4) for a in range(6)];static=[p/sum(static) for p in static]
  assert (norm==static)==(len(set(triple))==1)
  for t in (Q(0),Q(1,3),Q(1,2),Q(1)):
   mixed=[t*p+(1-t)*q for p,q in zip(vals,mirror)];assert [p/sum(mixed) for p in mixed]==norm
  n+=1
 records.append({'triple':triple,'all_center_and_mixed_boundary_checks':'PASS'})
p,q,r=sy.symbols('p q r');A=p*p+q*q+4*r*r;B=2*p*q+4*r*r;C=2*r*(p+q)+2*r*r
assert sy.expand(A-B-(p-q)**2)==0 and sy.expand((A-C).subs(q,p)-2*(p-r)**2)==0
out={'direct_causal_complete_2x3_configurations':len(law),'mirror_TV':str(tv),'direct_causal_marginals':4,'center_boundary_controls':n,'fixtures':records,'symbolic_nonconstant_identities':'PASS'}
Path('/private/tmp/review-drain-20260915/check8039/independent.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
