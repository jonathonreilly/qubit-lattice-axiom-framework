"""Independent exact controls; imports no PR primary or helper."""
from fractions import Fraction as F
from itertools import product
import json,time
from pathlib import Path
import sympy as s
start=time.monotonic();results=[]
def check(name,ok):
 assert ok,name
 results.append(name)
# Independently reconstruct fixed-target cell geometry and every finite binary path.
e=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
for N in range(1,5):
 initial={};targets=[]
 for j in range(1,N+1):
  c=(20*2**j,0,0);targets.append(c)
  initial[add(c,(1,0,0))]=initial[add(c,(2,0,0))]=('trigger',)
  for leaf in range(1,2**(j-1)+1):
   for z in (0,1):initial[add(c,(-3*leaf,3,z))]=('program',j,leaf)
 for bits in product((0,1),repeat=N):
  records=dict(initial);formed=0
  for j,c in enumerate(targets,1):
   leaf=1+sum(b*2**(j-2-k) for k,b in enumerate(bits[:j-1]))
   path=[add(c,(-3*leaf,y,0)) for y in (2,1,0)]+[add(c,(x,0,0)) for x in range(-3*leaf+1,0)]
   for site in path:
    neighbors=[records[add(site,d)] for d in e if add(site,d) in records]
    assert neighbors==[('program',j,leaf)] and site not in records
    records[site]=neighbors[0];formed+=1
   neighbors=[records[add(c,d)] for d in e if add(c,d) in records]
   assert set(neighbors)=={('program',j,leaf),('trigger',)}
   records[c]=('data',j,bits[j-1]);formed+=1
   # Every old program/trigger retains an equal neighbor. Data retains the exact two input neighbors.
   for site,value in records.items():
    ns=[records[add(site,d)] for d in e if add(site,d) in records]
    assert value in ns if value[0]!='data' else set(ns)=={('trigger',),('program',j if site==c else targets.index(site)+1,1+sum(b*2**(targets.index(site)-1-k) for k,b in enumerate(bits[:targets.index(site)]))))}
  assert formed<=3*(2**N-1)+3*N
 check('all_fixed_target_paths_and_permanent_support_N'+str(N),True)
# Program recognition and covariance, independently with explicit rational matrices.
I=s.eye(2);Z=s.diag(1,-1);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]])
P=(I+Z)/2;p=s.Rational(2,5);A=(2+p)*I+P;decoded=(s.trace(A)-5)/2
check('unique_program_probability_and_projector',decoded==p and A-(2+decoded)*I==P)
G=s.Matrix([[1,2],[0,1]]);B=G*A*G.inv();Q=B-(2+p)*I
check('nonunitary_algebra_covariance',s.trace(B)==s.trace(A) and Q*Q==Q and Q==G*P*G.inv())
wrong=(s.trace(A)-5)/4
check('wrong_normalization_rejected',wrong!=p)
# Repeated noncommuting finite history: density recursion vs vector amplitudes.
v=s.Matrix([1,s.I])/s.sqrt(2);rho=v*v.H;axes=(Z,X,Z)
weights={}
for bits in product((0,1),repeat=3):
 sigma=rho;vec=v;ratios=s.Integer(1)
 for axis,bit in zip(axes,bits):
  op=(I+(-1)**bit*axis)/2;den=s.simplify(s.trace(sigma));new=op*sigma*op
  ratios*=s.simplify(s.trace(new)/den) if den else 0
  sigma=new;vec=op*vec
 mass=s.simplify((vec.H*vec)[0]);assert s.simplify(ratios-mass)==0;weights[bits]=mass
check('trace_telescope_independent_amplitudes',sum(weights.values())==1)
# Adaptive tree TV: explicit enumeration, on-code scalar perturbations.
N=5;delta=F(1,32)
def law(shift):
 out={}
 for bits in product((0,1),repeat=N):
  q=F(1)
  for j,b in enumerate(bits):
   p=F(1+sum(bits[:j]),j+3)+shift
   q*=p if b==0 else 1-p
  out[bits]=q
 return out
a,b=law(0),law(delta);tv=sum(abs(a[h]-b[h]) for h in a)/2
check('adaptive_data_TV_bound',sum(a.values())==sum(b.values())==1 and tv<=1-(1-delta)**N<=N*delta)
# Off-code perturbation violates idempotence, so scalar precision is not arbitrary matrix robustness.
off=A+s.diag(s.Rational(1,100),-s.Rational(1,100));offP=off-(2+p)*I
check('off_code_is_not_valid_program',offP*offP!=offP)
print(json.dumps({'status':'pass','checks':results,'count':len(results),'seconds':time.monotonic()-start,'scope':'Independent finite geometry, exact matrix and probability controls only; no primary execution.'},indent=2))
