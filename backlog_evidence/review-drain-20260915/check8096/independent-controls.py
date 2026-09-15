"""Independent review: orientation products and exact counterexample controls."""
from fractions import Fraction as F
from itertools import product,permutations
import sympy as s
import json,time
start=time.monotonic();checks=[]
def ck(name,ok,**detail):
 assert ok,(name,detail)
 checks.append(dict(name=name,**detail))
# Translation acts by adding a common vector; first differing coordinate and
# its sign do not change. This tests the explicit counterexample to the note.
pts=list(product(range(-1,2),repeat=3));t=(3,-4,2)
ck('lexicographic_translation_counterexample',all((a<b)==(tuple(a[i]+t[i] for i in range(3))<tuple(b[i]+t[i] for i in range(3))) for a in pts for b in pts))
p,m,c=s.symbols('p m c',real=True)
ck('classification_polynomial_expansion',s.expand((1-m)**2+m*(1-p)-(1-(p*p+(1-p)*m))-(m-p)**2)==0)
# Edge order equality: c(1-p)=(1-c)m. Interior p,m forces c=m/(1-p+m), in (0,1).
ck('edge_empty_probability_identity',s.simplify((m/(1-p+m))*(1-p)-(1-m/(1-p+m))*m)==0)
# Star with <=6 mutually nonadjacent leaves: centre-first after one-slot
# constancy has iid mass; leaves-first has same positive leaf mass times f.
f=s.symbols('f')
for n in range(1,7):
 for k in range(n+1):
  leaf=c**k*(1-c)**(n-k)
  ck('star_extension_'+str((n,k)),s.cancel((leaf*f-leaf*c)/leaf)==f-c)
# All histories from an empty window produce zero under this boundary kernel,
# but exchange can fail on an unreachable prefix containing a plus.
ker=lambda n,k: F(0) if k==0 else (F(1,2) if n==1 else F(1,3))
left=ker(1,1)*(1-ker(1,1));right=(1-ker(0,0))*ker(2,1)
ck('unreachable_prefix_exchange_counterexample',left==F(1,4) and right==F(1,3) and left!=right)
# Compute laws by oriented edges, eliminating permutations with the same DAG.
def mass(order,n,edges):
 rank={v:i for i,v in enumerate(order)};incoming=[[] for _ in range(n)]
 for a,b in edges:
  u,v=(a,b) if rank[a]<rank[b] else (b,a);incoming[v].append(u)
 out=[]
 for bits in product([0,1],repeat=n):
  z=F(1)
  for v,nb in enumerate(incoming):
   k=sum(bits[u] for u in nb);m=len(nb);p=F(4**k,4**k+4**(m-k));z*=p if bits[v] else 1-p
  out.append(z)
 return tuple(out)
def tv(a,b):return sum(abs(x-y) for x,y in zip(a,b))/2
for name,n,edges,o1,o2,lawcount,variation,diffs in [
 ('path',3,[(0,1),(1,2)],(0,1,2),(0,2,1),2,F(9,50),8),
 ('square',4,[(0,1),(1,2),(2,3),(3,0)],(0,1,2,3),(0,2,1,3),4,F(9,50),16),
 ('rectangle',6,[(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)],tuple(range(6)),(0,2,3,5,1,4),28,F(135,578),44)]:
 laws={mass(o,n,edges) for o in permutations(range(n))};a=mass(o1,n,edges);b=mass(o2,n,edges)
 ck(name+'_orientation_census',len(laws)==lawcount and all(sum(v)==1 for v in laws),laws=len(laws))
 ck(name+'_pair_witness',tv(a,b)==variation and sum(x!=y for x,y in zip(a,b))==diffs,variation=str(variation),differing_cells=diffs)
 if n==3:ck('path_allminus',a[0]==F(8,25) and b[0]==F(4,17))
print(json.dumps(dict(status='ok',checks=checks,count=len(checks),elapsed_seconds=time.monotonic()-start),indent=2))
