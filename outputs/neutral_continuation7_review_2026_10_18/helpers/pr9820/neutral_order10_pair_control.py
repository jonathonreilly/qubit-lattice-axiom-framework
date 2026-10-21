AUDIT_TIMEOUT_SEC=300
from fractions import Fraction as F
from itertools import combinations,product
from collections import Counter,defaultdict
from math import factorial
import json

def graphs(a,b):
 paths=[]
 for ys in combinations(range(a+b),b):
  r=(0,0);es=[]
  for j in range(a+b):
   t=(r[0]+(j not in ys),r[1]+(j in ys));es.append((r,t));r=t
  paths.append(es)
 gs=set()
 for i,p in enumerate(paths):
  for q in paths[i+1:]:
   c=Counter(p+q)
   if any(sum(v for (r,s),v in c.items() if pt in (r,s) and r[0]==s[0])%2!=1 for pt in ((0,0),(a,b))):continue
   gs.add(tuple(sorted(c.items())))
 return sorted(gs)
def components(g):
 # Biconnected components via edge removal for the small cactus graphs here.
 edges=[e for e,n in g if n==1]; groups=[]
 while edges:
  e=edges.pop(0);u,v=e;paths=[(u,[],{u})];cycle=None
  while paths:
   r,es,seen=paths.pop()
   if r==v:cycle=es+[e];break
   for f in edges:
    if r in f:
     t=f[1] if f[0]==r else f[0]
     if t not in seen:paths.append((t,es+[f],seen|{t}))
  assert cycle
  for f in cycle:
   if f in edges:edges.remove(f)
  groups.append(cycle)
 return groups

def coefficient(edges):
 vertices=sorted({v for e in edges for v in e[:2]});ids={v:i for i,v in enumerate(vertices)}
 es=[(ids[u],ids[v],a) for u,v,a in edges];n=len(es);full=(1<<n)-1
 vertical=[(i,j) for i,u in enumerate(vertices) for j,v in enumerate(vertices) if u[:2]==v[:2] and v[2]-u[2]==1]
 flips=[0]*(full+1);psi=[F(0)]*(full+1);energy=[F(0)]*(full+1);psi[0]=F(1)
 for s in range(1,full+1):
  bit=s&-s;k=bit.bit_length()-1;u,v,_=es[k];flips[s]=flips[s^bit]^(1<<u)^(1<<v)
  val=F(0)
  for k,(u,v,a) in enumerate(es):
   if s>>k&1:
    prev=s^(1<<k);sg=-1 if a==0 else (-1)**(((flips[prev]>>u)&1)+((flips[prev]>>v)&1));val+=sg*psi[prev]
  if flips[s]==0:energy[s]=val
  else:
   t=(s-1)&s
   while t:
    if energy[t]:val-=energy[t]*psi[s^t]
    t=(t-1)&s
   cost=4*(flips[s].bit_count()-sum((flips[s]>>i&1)*(flips[s]>>j&1) for i,j in vertical))
   assert cost>0
   psi[s]=-val/cost
 counts=Counter(edges)
 return energy[full]/__import__('functools').reduce(lambda x,y:x*factorial(y),counts.values(),1)
def embed(group,z):return [(u+(z,),v+(z,),0 if u[1]==v[1] else 1) for u,v in group]
rows=[]
for g in graphs(3,2):
 cs=components(g);bridges=[e for e,n in g if n==2];rs=[]
 if len(cs)==1:
  assert not bridges;assignments=[([0],None)]
 elif not bridges:
  assert len(cs)==2;assignments=[([0,z],None) for z in (-1,0,1,2)]
 else:
  assert len(cs)==2 and len(bridges)==1;assignments=[([0,z],w) for w in (-1,0,1,2) for z in (w-1,w,w+1)]
 for zs,w in assignments:
  es=sum([embed(c,z) for c,z in zip(cs,zs)],[])
  if bridges:es+=embed(bridges,w)*2
  c=coefficient(es)
  if (len(cs)==2 and not bridges and zs[1]==2) or w==2:assert c==0
  rs.append(dict(zs=zs,bridge_z=w,c=str(c)))
 rows.append(dict(graph=g,cycle_lengths=[len(c) for c in cs],bridges=bridges,coefficients=rs,total=str(sum(F(r['c']) for r in rs))))
print(json.dumps(dict(rows=rows,total=str(sum(F(r['total']) for r in rows)),pair_contrast=str(4*sum(F(r['total']) for r in rows))),indent=2))
