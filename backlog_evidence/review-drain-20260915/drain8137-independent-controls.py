from fractions import Fraction as F
from itertools import product,permutations
import json,time
from pathlib import Path
t=time.monotonic();checks=[]
def check(n,c):assert c,n;checks.append(n)
def mm(A,B):return [[sum(x*y for x,y in zip(row,col))for col in zip(*B)]for row in A]
P=[[F(1,3)]*3 for _ in range(3)];u=[1,-1,0];v=[1,1,-2];K=[[P[i][j]+F(1,12)*u[i]*v[j]for j in range(3)]for i in range(3)]
check('radial_nilpotent_strictly_positive_markov',all(min(row)>0 and sum(row)==1 for row in K));check('radial_nonconstant_Haar_square',K!=P and mm(K,K)==P);check('radial_not_reversible',K[0][1]!=K[1][0])
# Binary bit-flip symmetric rule: fair for <=2 recorded neighbours; probability
# 1/2 + sum(spins)/12 for exactly3. Cubic-invariant, strictly interior.
def law(edges,order):
 out={}
 for vals in product([-1,1],repeat=len(order)):
  assignment=dict(zip(sorted(order),vals));seen=set();p=F(1)
  for site in order:
   ns=[assignment[x]for x in seen if frozenset([site,x])in edges];q=F(1,2)+(F(sum(ns),12)if len(ns)>=3 else 0);p*=q if assignment[site]==1 else 1-q;seen.add(site)
  out[vals]=p
 return out
path={frozenset([0,1]),frozenset([1,2])};laws=[law(path,o)for o in permutations(range(3))];check('delayed_variation_all_path3_orders_iid',all(x==laws[0]for x in laws)and set(laws[0].values())=={F(1,8)})
star={frozenset([0,i])for i in range(1,4)};a=law(star,[0,1,2,3]);b=law(star,[1,2,3,0]);check('delayed_variation_star4_distinguishes',a!=b);check('star4_probability_normalization',sum(a.values())==sum(b.values())==1)
# Independently integrate polynomial moments using exact monomial antiderivatives.
def integ(c):return sum(x/F(i+1)for i,x in enumerate(c)if i%2==0)
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
b=F(3,5);g=F(2,7);density=[1-g/2,b,3*g/2];p2=[F(-1,2),0,F(3,2)]
check('zonal_normalization',integ(density)==1);check('zonal_dipole_by_antiderivative',integ(mul([0,1],density))==b/3);check('zonal_quadrupole_by_antiderivative',integ(mul(p2,density))==g/5)
# Great circle conditional second moment: z lies in plane perpendicular to q,
# when q dot z=0. Average of squared two coordinates on circle is1/2.
check('equator_four_angles_second_moment',sum(F(x*x)for x in [1,0,-1,0])/4==F(1,2));check('haar_second_moment_by_integral',integ([0,0,1])==F(1,3))
out=dict(status='PASS',checks=checks,count=len(checks),elapsed_seconds=time.monotonic()-t,radial_counterexample=[[str(x)for x in row]for row in K],scope='Independent exact counterexamples and moment integrations; no primary runner import or execution',continuous_null_variation='On S2 set K0=K1=Haar; Km=Haar except when at least two recorded directions coincide, then delta at their common direction (for m=2). SO3-covariant and nonconstant pointwise; coincidence is Haar^2-null. By induction every finite sequential product remains iid Haar. Thus pointwise variation is insufficient.')
p=Path('/private/tmp/review-drain-20260915/drain8137-independent-controls.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
