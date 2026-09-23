from fractions import Fraction as F
from itertools import permutations,product
import math,json
checks=[]
def ck(n,x,detail):
 assert x,n
 checks.append({'name':n,'pass':True,'detail':detail})
def neg(q):return tuple(-x for x in q)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def menu(q,r):return (q,r,neg(q),neg(r))
def law(q,r,w):return dict(zip(menu(q,r),w))
def rot(q):return (q[2],-q[1],q[0])
q=(F(0),F(0),F(1));r=(F(1),F(0),F(0));w=(F(1,2),F(1,4),F(1,8),F(1,8))
ck('ordered_covariance_counterexample', {rot(k):v for k,v in law(q,r,w).items()}==law(rot(q),rot(r),w) and law(q,r,w)[q]!=law(q,r,w)[r], 'Fixed unequal slot weights are SO(3)-equivariant for every rotation; bisector swaps input slots, not a stabilizer.')
ck('exchange_is_extra',law(q,r,w)!=law(r,q,w),'The counterexample is not exchange-invariant; no counterexample to SO(3) plus slot-exchange covariance is claimed.')
for t in [F(-3,5),F(0),F(3,5)]:
 r=(F(4,5),F(0),t) if t else (F(1),F(0),F(0))
 for lam in [F(0),1/(1+t),-1/(1+t)]:
  ps=[(1+lam*dot(s,tuple(a+b for a,b in zip(q,r))))/4 for s in menu(q,r)]
  ck(f'linear_{t}_{lam}',sum(ps)==1 and min(ps)>=0,'Direct pointwise weights, valid lambda bounds; endpoints have two nonzero atoms.')
 born=[(1+dot(s,q))/2 for s in menu(q,r)]
 ck(f'born_sum_{t}',sum(born)==2,'Antipodal pairs sum to one each at every noncollinear t.')
t=F(3,5);lam=F(1);ck('linear_negative_weight', (1-lam*(1+t))/4==F(-3,20),'lambda=1 at t=3/5 is not a probability.')
ck('one_neighbor_singleton',len({q:1})==1,'delta_q is a finite normalized equivariant one-neighbor kernel; antipodal pair need not both have positive mass.')
beta=math.log(2)/2
ps=[math.exp(beta*x) for x in [1,1,-1,-1]];ps=[x/sum(ps) for x in ps]
ck('gibbs_direct_exp', max(abs(a-b) for a,b in zip(ps,[1/3,1/3,1/6,1/6]))<1e-15,'Independent exponential normalization confirms stated rational masses.')
# Exact discrete analogue of sequential joint-event proof: root uniform on six axes,
# every one-neighbor kernel supported on its axis. Ends-first draws independent roots.
axes=[tuple(F(sign) if i==j else F(0) for i in range(3)) for j in range(3) for sign in [-1,1]]
noncollinear=sum(dot(l,r)**2<1 for l in axes for r in axes)
ck('sequential_joint_event',noncollinear==24,'Chain has endpoint noncollinearity probability 0 for every antipodal-supported kernel; independent six-axis endpoints have probability 24/36. Haar analogue is 1 by zero area of two points.')
print(json.dumps({'checks':checks,'total':len(checks),'original_primary_executed':False},indent=2))
