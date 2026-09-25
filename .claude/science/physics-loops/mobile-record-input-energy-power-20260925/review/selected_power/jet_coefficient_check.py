#!/usr/bin/env python3
"""Second exact implementation: five-input matrix value/first Taylor jet.

No Laurent-state code import. Only counts and first edge-cost moments are
needed. This tests the decisive 67-edge coefficient by a different reduction.
"""
from collections import Counter,defaultdict
from itertools import product
from pathlib import Path
import hashlib,json

HERE=Path(__file__).resolve().parent
a=(0,0,0);d=(1,1,0);h=(2,2,0);c=(1,0,0);e=(0,1,0);b=(-1,0,0)
def neighbors(v):
 for mu in range(3):
  for sign in (-1,1):
   q=list(v);q[mu]+=sign;yield tuple(q)
old=[x for x in neighbors(a) if x!=b]
pre=[{x:1 for x in old if x!=vacant} for vacant in old]
outB={x:1 for x in neighbors(a)}
near={a}|{u for x in neighbors(a) for u in neighbors(x)}
pairs={tuple(sorted((u,v))) for u in near for x in neighbors(u) for v in neighbors(x) if u!=v}
def qa(u):return -1 if u in (d,h) else 1
def image(u,v,Bq):
 out={}
 for x in neighbors(u):
  if x in Bq:continue
  for y in neighbors(v):
   if y in Bq or x==y:continue
   final=dict(Bq);final[x]=qa(u);final[y]=qa(v);key=tuple(sorted(final.items()))
   if key not in out:out[key]=[0,Counter()]
   out[key][0]+=1;out[key][1][u,x]+=qa(u);out[key][1][v,y]+=qa(v)
 return out
H0=[[0]*5 for _ in range(5)];H1=[[Counter() for j in range(5)] for i in range(5)]
h0=0
for u,v in sorted(pairs):
 images=[image(u,v,q) for q in pre]
 for i,j in product(range(5),repeat=2):
  for key,(ni,li) in images[i].items():
   nj,lj=images[j].get(key,(0,{}))
   H0[i][j]-=2*ni*nj
   for link,n in li.items():H1[i][j][link]-=2*n*nj
   for link,n in lj.items():H1[i][j][link]+=2*ni*n
 h0-=2*sum(n*n for n,cost in image(u,v,outB).values())
u0=[0]*5;u0[old.index(e)]=1;u0[old.index(c)]=-1
source_d={old.index(e):(d,c),old.index(c):(d,e)}
t0=sum(H0[i][j]*u0[j] for i,j in product(range(5),repeat=2))
t1=Counter()
for i,j in product(range(5),repeat=2):
 if not u0[j]:continue
 for link,n in H1[i][j].items():t1[link]+=n*u0[j]
 t1[a,old[i]]-=H0[i][j]*u0[j]
 t1[source_d[j]]-=H0[i][j]*u0[j]
ell=Counter({(a,c):1,(d,c):-1,(d,e):1,(a,e):-1})
sumroutes=Counter({(a,e):1,(d,c):1,(a,c):1,(d,e):1})
r4=Counter()
for link in set(ell)|set(t1)|set(sumroutes):r4[link]=2*h0*ell[link]-2*t1[link]-t0*sumroutes[link]
r4={link:n for link,n in r4.items() if n}
artifact=json.loads((HERE/'infinite_RESULTS.json').read_text())
for answer in artifact['answers']:
 expected={(tuple(row['a']),tuple(row['b'])):row['numerator']//row['denominator'] for row in answer['r4']}
 assert all(row['denominator']==1 for row in answer['r4'])
 assert r4==expected
assert H0==[list(row) for row in zip(*H0)]
assert all(H1[i][j]==Counter({link:-n for link,n in H1[j][i].items()}) for i,j in product(range(5),repeat=2))
def serial(f):return [dict(a=u,b=v,value=n) for (u,v),n in sorted(f.items()) if n]
result=dict(scope='Independent exact matrix-jet reduction on the infinite local lift; matches both selected signs.',
   pair_count=len(pairs),vacant_B_word_order=old,H0_local=H0,h0_output_local=h0,t0=t0,
   t1_prime=serial(t1),r4=serial(r4),all_67_r_coefficients_exact=True,
   formula='r4=2 h0 ell - 2 t1_prime - t0(sum of two path costs)',
   source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
with (HERE/'JET_CHECK_RESULTS.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result,indent=2))
