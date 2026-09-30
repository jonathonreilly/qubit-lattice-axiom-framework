#!/usr/bin/env python3
"""Independent sparse rotor words; no author code imported or executed."""
import collections,itertools,json,resource,signal,time
from pathlib import Path
signal.alarm(30)
ROOT=Path(__file__).resolve().parent
steps=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
near=lambda a:[add(a,d) for d in steps]
def charge(q,x):return q.get(x,1 if sum(x)%2==0 else 0)
def state(q,e):return tuple(sorted((x,v) for x,v in q.items() if v!=(1 if sum(x)%2==0 else 0))),tuple(sorted((x,v) for x,v in e.items() if v))
OMEGA=((),())
def step(st,a,b,kind,sigma=0):
 q,e=map(dict,st);qa,qb=charge(q,a),charge(q,b)
 if kind=='out':
  if not qa or qb:return None
  q[a]=0;q[b]=qa;e[a,b]=e.get((a,b),0)-qa
 elif kind=='in':
  if qa or not qb:return None
  q[a]=qb;q[b]=0;e[a,b]=e.get((a,b),0)+qb
 else:
  if qa or qb:return None
  q[a]=sigma;q[b]=-sigma;e[a,b]=e.get((a,b),0)+sigma
 return state(q,e)
def op(v,a,kind,b=None,sigma=0):
 out=collections.Counter()
 for st,amp in v.items():
  for dest in [b] if b is not None else near(a):
   st1=step(st,a,dest,kind,sigma)
   if st1 is not None:out[st1]+=amp
 return {s:a for s,a in out.items() if a}
def physical(v):
 for st in v:
  q,e=map(dict,st); div=collections.Counter()
  for (a,b),v0 in e.items():div[a]+=v0;div[b]-=v0
  for x in set(div)|set(q):assert div[x]==charge(q,x)-(1 if sum(x)%2==0 else 0)
 return len(v)
def cubic(v,a,b,sigma):return {s:-amp for s,amp in op(op(op(v,a,'out'),a,'birth',b,sigma),a,'out').items()}
def birth(v,a,b,sigma):return op(op(v,a,'out'),a,'birth',b,sigma)
t=time.process_time(); a=(0,0,0); normrows=[]; exact_states=0
for b in near(a):
 vs=[cubic({OMEGA:1},a,b,sg) for sg in (1,-1)]
 ns=[sum(v*v for v in r.values()) for r in vs];assert ns==[40,20]
 assert not set(vs[0])&set(vs[1]);normrows.append(ns+[sum(ns)])
 for v in vs:exact_states+=physical(v)
c=(1,1,0);d=(1,0,1);ex=(1,0,0);ey=(0,1,0);ez=(0,0,1);extra=(2,0,1)
v1=birth({OMEGA:1},c,ey,1);v2=birth(v1,d,extra,1);v3=cubic(v2,a,(-1,0,0),1)
counts=[physical(v) for v in [v1,v2,v3]];assert counts==[5,23,100]
s=OMEGA
for aa,bb,kind,sg in [(c,ex,'out',0),(c,ey,'birth',1),(d,ez,'out',0),(d,extra,'birth',1),(a,(0,-1,0),'out',0),(a,(-1,0,0),'birth',1),(a,(0,0,-1),'out',0)]:s=step(s,aa,bb,kind,sg);assert s is not None
assert v3[s]==-2
q,e=map(dict,s);assert charge(q,a)==0 and all(charge(q,b) for b in near(a));assert sum(v!=0 for x,v in q.items() if sum(x)%2)==7
cc=(2,0,0);target=step(step(s,a,ex,'in'),cc,ex,'out');assert target is not None
forward=op(op({s:1},a,'in'),cc,'out');reverse=op(op({s:1},cc,'out'),a,'in');matrix=forward.get(target,0)-reverse.get(target,0);assert matrix==1
q2=dict(target[0]);g2=2*sum(not charge(q2,b) for b in near(cc));assert g2==8
physical({s:1,target:1});maxfield=max(abs(v) for st in v3 for _,v in st[1]);assert maxfield==1
# Geometry independent of charge code: literal periodic star intersections.
geometry=[]
for L in [6,8,10]:
 sites=[x for x in itertools.product(range(L),repeat=3) if sum(x)%2==0]
 N=lambda x:{tuple((a+b)%L for a,b in zip(x,d)) for d in steps}
 n0=N((0,0,0)); overlaps=collections.Counter(len(n0&N(c)) for c in sites if c!=(0,0,0));assert max(overlaps)<=2
 assert all(len(n0&N(tuple((2*d[i])%L for i in range(3))))==1 for d in steps)
 geometry.append({'L':L,'other_star_intersection_histogram':dict(overlaps)})
# Exact conservative arithmetic for Gram/Taylor constants, no sampled evolution.
from fractions import Fraction as Q
for tau in [Q(1,1),Q(1,2),Q(1,13),Q(1,100)]:
 determinant=tau**4/Q(12);trace=tau+tau**3/Q(3);assert determinant/trace>=tau**3/Q(16)
r={'scope':'exact selected original cubic words and periodic star geometry; no simulation of microscopic convergence','cubic_all_six_edges_squared_norms':normrows,'Gauss_checked_cubic_states':exact_states,'composed_word_counts':counts,'dark_word_coefficient':v3[s],'dark_G':0,'selected_H2_element':matrix,'bright_G':g2,'maximum_electric_magnitude':maxfield,'periodic_geometry':geometry,'cpu_seconds':time.process_time()-t,'max_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(ROOT/'RESULTS.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
