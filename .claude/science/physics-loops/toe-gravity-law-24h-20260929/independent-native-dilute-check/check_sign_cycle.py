from fractions import Fraction as F
from itertools import combinations,product
from collections import defaultdict
from pathlib import Path
import json,time,resource
start=time.perf_counter();z=(0,0,0);axes=[tuple(int(i==j) for i in range(3)) for j in range(3)]
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def scale(a,x):return tuple(a*b for b in x)
x=z;y=axes[2]
states=[frozenset((add(c,scale(-1,axes[j])),add(c,axes[j]))) for c,j in [(x,0),(y,0),(x,1),(y,2)]]
assert len(set(states))==4
pairs=[(scale(-1,e),e) for e in axes]
channels=[[(pairs[0],1),(pairs[1],-1)],[(pairs[0],1),(pairs[1],1),(pairs[2],-2)]]
for i,j in combinations(range(3),2):channels.append([((scale(s,axes[i]),scale(t,axes[j])),s*t) for s,t in product((-1,1),repeat=2)])
weights=[F(1,2),F(1,6),F(1,4),F(1,4),F(1,4)]
q=defaultdict(int)
for c in product(range(-3,4),repeat=3):
 for a,channel in enumerate(channels):
  for state,s in enumerate(states):q[(c,a,state)]=sum(coeff for (u,v),coeff in channel if frozenset((add(c,u),add(c,v)))==s)
rows=[]
for i,j in [(0,1),(1,2),(2,3),(3,0)]:
 mu=F(0);tau=F(0)
 for c in product(range(-4,5),repeat=3):
  for a,w in enumerate(weights):
   mu+=(-2 if a<2 else -1)*w*q[(c,a,i)]*q[(c,a,j)]
   for step in axes:
    d=add(c,step);tau+=w*(q[(d,a,i)]-q[(c,a,i)])*(q[(d,a,j)]-q[(c,a,j)])
 rows.append((mu,tau))
assert rows==[(F(0),F(-2,3)),(F(0),F(1,3)),(F(0),F(1,3)),(F(0),F(1,3))]
p=F(1)
for mu,tau in rows:p*=tau
assert p==F(-2,81)
out={'actual_full_two_particle_mu_tau_rows':[[str(a),str(b)] for a,b in rows],'cycle_product_tau4':str(p),'wall_seconds':time.perf_counter()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'author_code_imported':False}
Path(__file__).with_name('sign_cycle.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
