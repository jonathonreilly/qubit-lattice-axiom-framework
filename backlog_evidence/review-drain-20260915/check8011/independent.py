from fractions import Fraction as Q
from itertools import product,permutations
from collections import defaultdict
import json,math
vertices=tuple(product(range(2),repeat=2))
N={i:[j for j,v in enumerate(vertices) if sum(abs(a-b) for a,b in zip(vertices[i],v))==1] for i in range(4)}
# Independent orbit implementation: signed-axis vectors and their dot products.
labels=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
def weight(a,b,w):return dict(zip((1,-1,0),w))[sum(x*y for x,y in zip(labels[a],labels[b]))]
def kernel(st,i,w):
 vals=[math.prod(weight(a,st[j],w) for j in N[i] if st[j]>=0) for a in range(6)]
 return [Q(v,sum(vals)) for v in vals]
def advance(law,w,chosen=None):
 out=defaultdict(Q)
 for st,p in law.items():
  available=[i for i in range(4) if st[i]<0] if chosen is None else [chosen]
  for i in available:
   for a,q in enumerate(kernel(st,i,w)):
    v=list(st);v[i]=a;out[tuple(v)]+=p*q/len(available)
 return out
rows=[]
for w in ((3,1,2),(2,2,2)):
 mixed={(-1,)*4:Q(1)};mono=mixed
 for i in range(4):mixed=advance(mixed,w);mono=advance(mono,w,i)
 z=sum(w[:2])+4*w[2]
 for v,p in mono.items():
  # Undirected four-edge product, divided by the only two-parent normalizer.
  two=sum(weight(s,v[1],w)*weight(s,v[2],w) for s in range(6))
  direct=Q(math.prod(weight(v[i],v[j],w) for i in range(4) for j in N[i] if i<j),6*z*z*two)
  assert p==direct
 tv=sum(abs(p-mono[v]) for v,p in mixed.items())/2
 assert sum(mixed.values())==sum(mono.values())==1
 assert tv==(Q(53347,4416984) if w[0]==3 else 0)
 different=sum(p!=mono[v] for v,p in mixed.items());assert different==(720 if w[0]==3 else 0)
 # downset {0,1}; conditional remainder matches direct completion
 marginal=defaultdict(Q)
 for v,p in mono.items():marginal[v[:2]]+=p
 for pair,mass in marginal.items():
  law={pair+(-1,-1):Q(1)}
  for i in (2,3):law=advance(law,w,i)
  assert all(p==mono[v]/mass for v,p in law.items())
 rows.append({'weights':w,'TV':str(tv),'different':different,'downset_conditionals':36})
# Explicit infinite-lattice embedded repair, actual neighbor relation.
def supp(st,x):
 ns=[val for y,val in st.items() if sum(abs(a-b) for a,b in zip(x,y))==1]
 return {ns[0]} if ns and len(set(ns))==1 else set(range(6))
def valid(st):return all(v in supp(st,x) for x,v in st.items())
st={(-1,0,0):0,(1,0,0):1};assert valid(st)
assert all(not valid(dict(st,**{} )|{(0,0,0):a}) for a in range(6))
for x,a in (((2,0,0),1),((0,0,0),0)):
 assert a in supp(st,x);st[x]=a;assert valid(st)
# Race identity exact: integral r_s exp(-sum r*u) du = r_s for normalized weights,
# including zero entries; independent order enumeration establishes factorial event.
for n in range(1,8):
 perms=list(permutations(range(n+1)))
 assert sum(all(p[i]>p[i+1] for i in range(n)) for p in perms)==1
print(json.dumps({'rows':rows,'repair_valid':valid(st),'decreasing_order_counts_verified_through_edges':7},indent=2))
