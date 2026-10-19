AUDIT_TIMEOUT_SEC=300
from fractions import Fraction as F
from itertools import product
import json

def coefficient(verts):
 n=len(verts);edges=[(i,(i+1)%n,'X' if verts[i][1]==verts[(i+1)%n][1] else 'Y') for i in range(n)]
 flip=[0]*(1<<n);weights=[F(0)]*(1<<n);weights[0]=F(1)
 for s in range(1,1<<n):
  bit=s&-s;i=bit.bit_length()-1;u,v,_=edges[i];flip[s]=flip[s^bit]^(1<<u)^(1<<v)
  val=F(0)
  for i,(u,v,ax) in enumerate(edges):
   if (s>>i)&1:
    prev=s^(1<<i);sign=-1 if ax=='X' else (-1)**(((flip[prev]>>u)&1)+((flip[prev]>>v)&1))
    val+=sign*weights[prev]
  weights[s]=val/(-4*flip[s].bit_count()) if s!=(1<<n)-1 else val
 return weights[-1]

def expand(corners):
 out=[]
 for (x,y),(u,v) in zip(corners,corners[1:]+corners[:1]):
  dx=(u>x)-(u<x);dy=(v>y)-(v<y)
  while (x,y)!=(u,v):out.append((x,y));x+=dx;y+=dy
 return out
from math import factorial

def halfgamma_ratio(n):
 # Gamma(n+1/2)/sqrtpi
 return F(factorial(2*n),4**n*factorial(n))
def formula(N,m):return (-1)**(m//2+1)*F(1,2**(N-1))*halfgamma_ratio(m//2)*halfgamma_ratio(N-m//2-1)/factorial(N-1)

def square(x,y,z):return [((x,y,z),(x+1,y,z),'X'),((x,y+1,z),(x+1,y+1,z),'X'),((x,y,z),(x,y+1,z),'Y'),((x+1,y,z),(x+1,y+1,z),'Y')]
def coeff(dz,refcols=frozenset()):
 edges=square(0,0,0)+square(1,1,dz);verts=sorted(set(v for e in edges for v in e[:2]));ix={v:i for i,v in enumerate(verts)};edges=[(ix[u],ix[v],ax) for u,v,ax in edges];n=len(edges);full=(1<<n)-1
 refs=sum(1<<i for i,(x,y,z) in enumerate(verts) if (x,y) in refcols)
 vertical=[(i,j) for i,u in enumerate(verts) for j,v in enumerate(verts) if u[:2]==v[:2] and v[2]-u[2]==1]
 flips=[0]*(full+1);psi=[F(0)]*(full+1);energy=[F(0)]*(full+1);psi[0]=F(1)
 for s in range(1,full+1):
  bit=s&-s;e=bit.bit_length()-1;u,v,ax=edges[e];flips[s]=flips[s^bit]^(1<<u)^(1<<v)
  val=F(0)
  for e,(u,v,ax) in enumerate(edges):
   if s>>e&1:
    prev=s^(1<<e);state=refs^flips[prev];sg=-1 if ax=='X' else (-1)**(((state>>u)&1)+((state>>v)&1));val+=sg*psi[prev]
  if flips[s]==0:energy[s]=val
  else:
   t=(s-1)&s
   while t:
    if energy[t]:val-=energy[t]*psi[s^t]
    t=(t-1)&s
   cost=4*(flips[s].bit_count()-sum((flips[s]>>i&1)*(flips[s]>>j&1) for i,j in vertical))
   psi[s]=-val/cost
 return energy[full]

rows=[]
for a in range(1,6):
 for b in range(1,a+1):
  if a+b>7:continue
  verts=expand([(0,0),(a,0),(a,b),(0,b)]);observed=coefficient(verts);pred=formula(len(verts),4)
  assert observed==pred
  rows.append(dict(a=a,b=b,coefficient=str(observed)))
polys=[[(0,0),(2,0),(2,1),(1,1),(1,2),(0,2)],[(0,0),(3,0),(3,1),(1,1),(1,2),(0,2)],[(0,0),(3,0),(3,1),(2,1),(2,2),(1,2),(1,3),(0,3)]]
turns=[]
for p in polys:
 verts=expand(p);obs=coefficient(verts);assert obs==formula(len(verts),len(p));turns.append(dict(N=len(verts),turns=len(p),coefficient=str(obs)))
linked=[]
for dz in range(4):
 obs=coeff(dz);assert coeff(dz,frozenset({(0,0)}))==-obs and coeff(dz,frozenset({(1,1)}))==obs
 linked.append(dict(dz=dz,coefficient=str(obs)))
total=4*(F(1,262144)+coeff(0)+2*coeff(1));axis=8*formula(8,4)
assert total==F(545,5308416) and axis==-F(9,32768)
print(json.dumps(dict(rectangles=rows,nonrectangles=turns,linked=linked,diagonal_interaction=str(total),axis_interaction=str(axis))))
