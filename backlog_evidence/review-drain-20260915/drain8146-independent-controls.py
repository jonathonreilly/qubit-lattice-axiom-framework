from fractions import Fraction as F
from itertools import product
from math import prod
from pathlib import Path
import json,signal,time
import sympy as s
signal.alarm(90)
t0=time.monotonic(); p,q=s.symbols('p q'); menu=range(6)
def weights(a,b,P,Q,R=1): return P if a==b else Q if a//2==b//2 else R
def z(vals,P=p,Q=q,R=1): return s.expand(sum(prod(weights(a,b,P,Q,R) for b in vals) for a in menu))
# Independent fixed-vacuum Mobius criterion: 125 nontrivial cubes suffice for additivity.
zcache={v:z(v) for v in product(menu,repeat=3)}
nums=[]
for v in product(range(1,6),repeat=3):
 n=d=s.Integer(1)
 for mask in range(8):
  vals=tuple(v[i] if mask>>i&1 else 0 for i in range(3))
  if mask.bit_count()%2: n*=zcache[vals]
  else: d*=zcache[vals]
 nums.append(s.expand(n-d))
E1=s.expand(z((0,0,0))*z((0,2,4))**2-z((0,0,2))**3)
E2=s.expand(z((0,0,0))*z((0,1,2))**2-z((0,0,1))*z((0,0,2))**2)
G=s.cancel(E2/(-(p-q)**2))
res=s.factor(s.resultant(E1,G,p))
T=q**3-3*q**2-6*q-1; R=q**3-3*q**2-15*q-19
S=q**6-6*q**5-3*q**4+4*q**3-3*q**2-6*q+31
psi=(-24*q**5+116*q**4+196*q**3+246*q**2+121*q+356)/255
checks={}
for label,sub,mod in [('constant',1,q-1),('equal',q,T),('rho',1,R),('sextic',psi,S)]:
 checks[label]=all(s.rem(n.subs(p,sub).expand(),mod,q)==0 for n in nums)
 assert checks[label]
# On q=1 the two witness common roots give p=1 or rho; mirrors handled independently.
checks['q1_gcd']=str(s.factor(s.gcd(E1.subs(q,1),E2.subs(q,1))))
checks['resultant']=str(res)
checks['positive_root_counts']={str(P):sum(m for (a,b),m in s.Poly(P,q).intervals() if a>=0) for P in [T,R,S]}
# Majority preference counterexample and repaired threshold on a finite rational grid.
def majority(P,Q,R):
 for v in [(0,0,1),(0,0,2)]:
  w=[prod(weights(a,b,P,Q,R) for b in v) for a in menu]
  if not w[0]>max(w[1:]): return False
 return True
tr=(F(3),F(1,100),F(2))
checks['majority_counterexample']={'p_gt_max':tr[0]>max(tr[1:]),'majority':str(tr[0]**2*tr[1]),'orthogonal':str(tr[2]**3),'strict_preference':majority(*tr)}
grid=[F(1,10),F(1,2),F(1),F(2),F(3)]
checks['corrected_threshold_125']=all(majority(P,Q,R)==(P>max(Q,R) and P*P*Q>R**3) for P,Q,R in product(grid,repeat=3))
assert checks['corrected_threshold_125']
# Pair-additive denominators give identical normalized conditionals regardless of opposite-corner grouping.
groups=[[(0,1),(2,3),(4,5)],[(2,4),(0,5),(1,3)]]
def pair(a,b): return 2+(a-b)**2+a+b
def conditional(v,g):
 w=[F(1,prod(pair(a,v[i])*pair(v[i],v[j])*pair(v[j],a) for i,j in g)) for a in range(3)]
 return [a/sum(w) for a in w]
checks['pair_additive_grouping_64']=all(conditional(v,groups[0])==conditional(v,groups[1]) for v in product(range(2),repeat=6))
assert checks['pair_additive_grouping_64']
checks['elapsed_seconds']=time.monotonic()-t0
Path('/private/tmp/review-drain-20260915/drain8146-independent-controls.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
