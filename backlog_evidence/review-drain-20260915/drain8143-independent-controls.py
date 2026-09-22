from fractions import Fraction as F
from itertools import product
import json,time,pathlib
start=time.monotonic();checks=0
# Independent graph induction control: content types only; no primary import or target-mask filtering.
dirs=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def near(z):return [tuple(a+b for a,b in zip(z,d)) for d in dirs]
for L in range(1,9):
 state={(-1,0,0):'carrier'}
 for j in range(L):state[(3*j,-1,0)]='program';state[(3*j+2,1,0)]='marker'
 targets={(x,0,0) for x in range(3*L)};core=set(state)|targets
 guards={v for z in core for v in near(z)}-core
 state.update({z:'zero' for z in guards})
 for stage in range(3*L+1):
  frontier={v for z in state for v in near(z)}-state.keys();active=[]
  for z in frontier:
   types=sorted(state[v] for v in near(z) if v in state and state[v]!='zero')
   if types in [['carrier','program'],['outcome'],['marker','outcome']]:active.append(z)
  assert set(active)==({(stage,0,0)} if stage<3*L else set());checks+=1
  if stage<3*L:state[(stage,0,0)]='carrier' if stage%3==2 else 'outcome'
# Independent rank-one amplitudes vs full 2x2 sandwich products, real rational normalized spinors.
vecs=[(F(1),F(0)),(F(3,5),F(4,5)),(F(5,13),F(12,13))]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def outer(v):return [[x*y for y in v] for x in v]
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
for labels in product([0,1],repeat=3):
 vs=[v if l==0 else (-v[1],v[0]) for v,l in zip(vecs,labels)]
 rho=outer((F(8,17),F(15,17)));sigma=rho
 mass=dot((F(8,17),F(15,17)),vs[0])**2
 for a,b in zip(vs,vs[1:]):mass*=dot(a,b)**2
 for v in vs:sigma=mul(mul(outer(v),sigma),outer(v))
 assert mass==sigma[0][0]+sigma[1][1];checks+=1
# Exact denominator minima and bounded activation identity.
for s in [F(i,17) for i in range(301)]:
 assert s+(s-1)**2== (s-F(1,2))**2+F(3,4)
 assert 0<=s/(s+(s-1)**2)<=1;checks+=1
out={'status':'PASS','checks':checks,'elapsed_sec':time.monotonic()-start,'scope':['whole finite frontier typed-geometry independent implementation L1..8','eight rational rank-one histories via amplitudes versus sandwiches','denominator and bounded activation identities'],'primary_imported_or_executed':False}
p=pathlib.Path(__file__).with_suffix('.json');assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
