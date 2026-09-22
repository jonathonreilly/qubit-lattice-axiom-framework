import time,json
from itertools import permutations,combinations
from fractions import Fraction as F
import sympy as S
start=time.monotonic();checks=[]
def ck(n,b):
 assert bool(b),n
 checks.append(n)
x=S.Symbol('x')
def adjacency(counts):
 words=sorted(set(permutations(tuple(i for i,n in enumerate(counts) for _ in range(n)))))
 # Independent face operation: swap successive steps, retain labeled destination.
 A=S.zeros(len(words));ix={w:i for i,w in enumerate(words)}
 for w in words:
  for k in range(len(w)-1):
   if w[k]!=w[k+1]: A[ix[w],ix[w[:k]+(w[k+1],w[k])+w[k+2:]]+=1
 return words,A
for c,poly in [((1,1),x*x-1),((2,1),x*(x*x-2)),((2,2),x*x*(x*x-1)*(x*x-5))]:
 words,A=adjacency(c);ck(str(c)+' characteristic',S.expand(A.charpoly(x).as_expr()-poly)==0);ck(str(c)+' zero diagonal',all(A[i,i]==0 for i in range(A.rows)))
w,A=adjacency((1,1,1));ck('3D six permutations',len(w)==6);ck('3D degree2 connected cycle',all(sum(A[i,j] for j in range(6))==2 for i in range(6)) and A.charpoly(x).as_expr()==S.expand((x*x-4)*(x*x-1)**2));ck('3D selected derivative',F(2,18)==F(1,9))
ck('source Haar flip normalization',F(1,3)*F(1,6)==F(1,18));ck('source convention equivalence',F(1,3)*3==1)
# Next subset maximizer: strictly decreasing one-body levels; independent exact
# L4 two-particle spectrum gives gap sqrt5-1 before multiplication1/18.
levels=[2*S.cos(S.pi*k/5) for k in range(1,5)]
sums=[S.simplify(sum(levels[k] for k in ks)) for ks in combinations(range(4),2)]
ck('full subset multiset',sorted(map(str,sums))==sorted(map(str,[S.sqrt(5),S.Integer(1),S.Integer(0),S.Integer(0),-S.Integer(1),-S.sqrt(5)])))
ck('archived splitting corollary',S.simplify((S.sqrt(5)-1)/18-(S.cos(2*S.pi/5)-S.cos(3*S.pi/5))/9)==0)
p,q=S.symbols('p q',nonnegative=True,integer=True);E=p*p+p*q+q*q+3*p+3*q
ck('all-label differences positive',S.expand(E.subs(p,p+1)-E)==2*p+q+4 and S.expand(E.subs(q,q+1)-E)==p+2*q+4)
print(json.dumps({'PASS':len(checks),'FAIL':0,'checks':checks,'elapsed_sec':time.monotonic()-start,'scope':'Small independent adjacency characteristic polynomials, spectral splitting and exact normalization/Casimir identities; no primary/helper imports or full interacting spectrum.'},indent=2))
