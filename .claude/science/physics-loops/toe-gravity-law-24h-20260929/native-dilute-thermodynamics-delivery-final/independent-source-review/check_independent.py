"""Independent positive-square column check, not primary implementation reuse.
Read after primary exposure; reconstructs S+mu D+W rather than its attractive H.
Finite exact check only, no thermodynamic or infinite-source execution.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from collections import defaultdict
import json, time
start=time.monotonic()
E=[(1,0,0),(0,1,0),(0,0,1)]
def add(a,b): return tuple(a[i]+b[i] for i in range(3))
def mul(a,k): return tuple(k*x for x in a)
units=[mul(e,k) for e in E for k in [-1,1]]
graph={mul(e,k) for e in E for k in [-2,2]}
for i,j in combinations(range(3),2):
 for s,t in product([-1,1],repeat=2): graph.add(add(mul(E[i],s),mul(E[j],t)))
def shiftword(w,c): return frozenset(add(p,c) for p in w)
ax=[(mul(e,-1),e) for e in E]
pl=[[( (mul(E[i],s),mul(E[j],t)),s*t) for s,t in product([-1,1],repeat=2)] for i,j in combinations(range(3),2)]
# A row is a list of coefficient, two-site word, and a positive rational weight.
srows=[([(1,w) for w in ax],Q(2,3))]
for words in pl:
 for (u,a),(v,b) in combinations(words,2): srows.append(([(a,u),(-b,v)],Q(1,4)))
qrows=[([(1,ax[0]),(-1,ax[1])],Q(1,2)), ([(1,ax[0]),(1,ax[1]),(-2,ax[2])],Q(1,6))]
qrows += [([(c,w) for w,c in words],Q(1,4)) for words in pl]
S=frozenset([(0,0,0),(3,-1,1),(3,1,1),(6,0,0)])
centers={add(p,mul(u,-1)) for p in S for u in units}
gradcenters=centers|{add(c,mul(e,-1)) for c in centers for e in E}
cols=[defaultdict(Q),defaultdict(Q)]
def accumulate(row,weight,col):
 out=defaultdict(Q)
 for c,w in row:
  if w<=S: out[S-w]+=c
 for rem,amp in out.items():
  for c,w in row:
   if not rem&w: col[rem|w]+=weight*c*amp
for c in centers:
 for row,weight in srows: accumulate([(a,shiftword(w,c)) for a,w in row],weight,cols[0])
for c in gradcenters:
 for e in E:
  for row,weight in qrows:
   diff=[(a,shiftword(w,add(c,e))) for a,w in row]+[(-a,shiftword(w,c)) for a,w in row]
   accumulate(diff,weight,cols[1])
D=sum((sum(add(x,d) in S for d in graph)-1)*(sum(add(x,d) in S for d in graph)-2)//2 for x in S)
cols[0][S]+=D
# Independent E1 pair weight in integer units: actual normalized C^2 coefficient
# equals the sum over the three unordered matchings after 2*(1/sqrt2)^2.
def w(p,q):
 d=tuple(q[i]-p[i] for i in range(3))
 return (1 if d in [mul(E[0],2),mul(E[0],-2)] else -1 if d in [mul(E[1],2),mul(E[1],-2)] else 0)
def amp(T):
 p,q,r,s=sorted(T)
 return w(p,q)*w(r,s)+w(p,r)*w(q,s)+w(p,s)*w(q,r)
source=[sum(v*amp(T) for T,v in col.items()) for col in cols]
assert [col[S] for col in cols]==[Q(8,3),Q(4)]
assert source==[Q(0),Q(1,3)]
# Coherent Husimi diagonal for occupation |n,0,...>: Dirichlet parameters
# (n+1,1,1,1,1); E|z0|^4=(n+1)(n+2)/((n+5)(n+6)).
for n in range(2,101):
 lhs=Q((n+1)*(n+2),(n+5)*(n+6))
 rhs=Q(n*(n-1)+4*n+2,(n+5)*(n+6))
 assert lhs==rhs
 p=Q(n*(n-1),(n+5)*(n+6))
 assert n*(n-1)*(1-p)<=27*n
# Scalar variational factors from raw polynomial c*rho^2-nu*rho.
c=Q(7,8);nu=Q(3,11);rho=nu/(2*c)
assert c*rho*rho-nu*rho==-nu*nu/(4*c)
result={'positive_square_column_diagonal':[str(x[S]) for x in cols], 'positive_square_source':[str(x) for x in source], 'Ddiag':D,'sphere_diagonal_cases':99,'wall_seconds':time.monotonic()-start,'scope':'finite independent S+D+W path, diagonal sphere moment and variational factor controls; primary not imported or executed'}
print(json.dumps(result,indent=2))
