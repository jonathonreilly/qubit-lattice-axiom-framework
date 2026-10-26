from itertools import product
from functools import lru_cache
import json, math

def bareiss(a):
 a=[r[:] for r in a]; n=len(a);sgn=1;prev=1
 for k in range(n-1):
  if not a[k][k]:
   q=next((q for q in range(k+1,n) if a[q][k]),None)
   if q is None:return 0
   a[k],a[q]=a[q],a[k];sgn=-sgn
  pivot=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    v=a[i][j]*pivot-a[i][k]*a[k][j]
    assert v%prev==0
    a[i][j]=v//prev
  for i in range(k+1,n):a[i][k]=0
  prev=pivot
 return sgn*a[-1][-1]

def cuboid(dim):
 vertices=list(product(*[range(x) for x in dim]));ev=[v for v in vertices if sum(v)%2==0];od=[v for v in vertices if sum(v)%2]; n=len(ev);B=[[0]*n for _ in ev]
 for i,e in enumerate(ev):
  for j,o in enumerate(od):
   if sum(abs(x-y) for x,y in zip(e,o))!=1:continue
   mu=next(k for k in range(3) if e[k]!=o[k]); lower=min(e,o,key=lambda p:p[mu]);phase=(-1)**sum(lower[:mu]);B[i][j]=phase if lower==e else -phase
 # Count perfect matchings independently on the unsigned undirected vertex graph.
 adj=[sum(1<<j for j,w in enumerate(vertices) if sum(abs(x-y) for x,y in zip(v,w))==1) for v in vertices]
 @lru_cache(None)
 def match(mask):
  if not mask:return 1
  # Minimum remaining degree cuts the recursion; no determinant/permutation input.
  ids=[i for i in range(len(vertices)) if mask>>i&1];i=min(ids,key=lambda i:(adj[i]&mask).bit_count());choices=adj[i]&mask;rest=mask^(1<<i);ans=0
  while choices:
   bit=choices&-choices;choices-=bit;ans+=match(rest^bit)
  return ans
 # Signed Leibniz dynamic program, independent determinant algorithm.
 @lru_cache(None)
 def signed(mask):
  i=mask.bit_count()
  if i==n:return 1
  s=0
  for j,v in enumerate(B[i]):
   if v and not mask>>j&1:s+=(-1)**((mask>>(j+1)).bit_count())*v*signed(mask|(1<<j))
  return s
 det=bareiss(B);ds=signed(0);assert det==ds
 return {'dimensions':dim,'sites':len(vertices),'det_exact_bareiss':det,'det_exact_signed_dp':ds,'abs_det':abs(det),'perfect_matchings_unsigned_graph_recursion':match((1<<len(vertices))-1),'defects':[]}
rows=[cuboid(x) for x in [(4,3,2),(2,3,3),(4,3,3)]]
expected=[(1805,1845),(225,229),(101761,117805)]
for row,(det,pm) in zip(rows,expected):
 assert row['abs_det']==det and row['perfect_matchings_unsigned_graph_recursion']==pm
 assert det<pm and row['defects']==[]
from decimal import Decimal, localcontext
with localcontext() as ctx:
 ctx.prec=50
 exponent=-(Decimal(88)*Decimal(10)**38)/Decimal(10).ln()
 # Check the rounded base-ten exponent independently of floating exp underflow.
 assert abs(exponent/(Decimal(10)**39)+Decimal('3.821791440748616'))<Decimal('1e-15')
print(json.dumps({'scope':'finite combinatorics and exponential arithmetic only; no echo-model, search or Higgs-chain validation','kasteleyn':rows,'echo_log10_transmission':str(exponent),'finite_exponential_strictly_positive':'exp(x)>0 for every finite real x; numerical underflow is not exact zero','checks':'three finite determinant/matching inequalities and decimal logarithm conversion passed'},indent=2))
