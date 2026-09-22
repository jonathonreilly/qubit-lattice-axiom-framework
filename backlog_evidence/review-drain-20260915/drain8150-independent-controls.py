from fractions import Fraction as F
from itertools import product,permutations
from collections import defaultdict
import json,time
T=time.monotonic(); checks=0
axis=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
pos=((0,0,0),(1,0,0),(1,1,0),(0,1,0));edges=((0,1),(1,2),(2,3),(3,0));nb={i:[j for j in range(4) if (i,j) in edges or (j,i) in edges] for i in range(4)}
def ck(b):
 global checks
 assert b;checks+=1
def kernel(p,q,r):return [[p if i==j else q if i//2==j//2 else r for j in range(6)]for i in range(6)]
def cond(K,a,rec):
 w=[__import__('math').prod(K[s][b] for b in rec)for s in range(6)];return F(w[a],sum(w))
def measure(K,order,v,adj):
 seen=set();x=F(1)
 for i in order:x*=cond(K,v[i],[v[j]for j in adj[i]if j in seen]);seen.add(i)
 return x
def rate(kind,i,v):
 rec=[j for j in nb[i] if v[j]>=0]
 if kind=='uniform':return 1
 if kind=='seeded':return int(all(a<0 for a in v) or bool(rec))
 if kind=='attracting':return 1+len(rec)
 return 1+int(any(axis[v[j]]==tuple(pos[i][k]-pos[j][k]for k in range(3))for j in rec))
K=kernel(3,1,2); pats=list(product(range(6),repeat=4)); Z=sum(__import__('math').prod(K[v[i]][v[j]] for i,j in edges)for v in pats);static={v:F(__import__('math').prod(K[v[i]][v[j]]for i,j in edges),Z)for v in pats}; results={}
for kind in ('uniform','seeded','attracting','parallel'):
 layer={(-1,)*4:F(1)}
 for depth in range(4):
  nxt=defaultdict(F)
  for v,prob in layer.items():
   rates={i:rate(kind,i,v)for i in range(4)if v[i]<0};total=sum(rates.values());ck(total>0)
   for i,r in rates.items():
    for a in range(6):
     new=list(v);new[i]=a;nxt[tuple(new)]+=prob*F(r,total)*cond(K,a,[v[j]for j in nb[i]if v[j]>=0])
  layer=nxt
 ck(sum(layer.values())==1)
 results[kind]=str(sum(abs(layer[v]-static[v])for v in pats)/2)
expected={'uniform':'262271/15806232','seeded':'30457/2431728','attracting':'591377/39515580','parallel':'2239744469/137703893184'};ck(results==expected)
for p,q,r in ((3,1,2),(1,3,2),(2,2,1),(1,1,3),(1,1,1)):
 K=kernel(p,q,r);z=p+q+4*r;flip=1 if p!=q else 2
 for order in permutations(range(4)):
  base=(0,)*4;w0=measure(K,order,base,nb)/F(p**4,z**4)
  earlier=set();strict=set()
  for i in order:
   rec=set(nb[i])&earlier
   if len(rec)>1:strict|=rec
   earlier.add(i)
  for i in range(4):
   v=list(base);v[i]=flip;pk=F(__import__('math').prod(K[v[a]][v[b]]for a,b in edges),z**4);w1=measure(K,order,v,nb)/pk
   ck(w1>=w0);ck((w1>w0)==(i in strict and len({p,q,r})>1))
 for n in range(2,7):
  same=sum(K[s][0]**n for s in range(6));anti=sum(K[s][1]*K[s][0]**(n-1)for s in range(6));orth=sum(K[s][2]*K[s][0]**(n-1)for s in range(6))
  ck(same-anti==(p-q)*(p**(n-1)-q**(n-1)));ck(same-orth==(p-r)*(p**(n-1)-r**(n-1))+(q-r)*(q**(n-1)-r**(n-1)))
# Fixed outside values cannot be replaced by the constant comparison pattern.
K=kernel(3,1,2);fixed=(1,)*5
norm=[sum(K[s][a]*__import__('math').prod(K[s][b]for b in fixed)for s in range(6))for a in (0,1)]
ck(norm[1]>norm[0]) # opposite sign to an all +x environment; invalid universal monotonic argument
print(json.dumps({'checks':checks,'failures':0,'elapsed_seconds':time.monotonic()-T,'plaquette_total_variations':results,'fixed_minus_x_environment_normalizers':norm,'scope':'Independent merged partial-configuration DP (no original imports), direct sequential-product flip checks on24orders×4sites×5triples, exact normalizer identities; fixed-boundary sign reversal tests proof gap, not a counterexample to arbitrary-env theorem.'},indent=2))
