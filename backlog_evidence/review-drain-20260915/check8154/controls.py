from fractions import Fraction as F
from itertools import product
from collections import Counter
from math import factorial,isqrt,sqrt,cos,pi
import json,time,pathlib
start=time.monotonic();count=0;observations={}
# Direct spectral sums: independent numerical sanity checks, not proof/certified intervals.
for d in [1,2]:
 for L in [2,3,7,13]:
  N=(2*L)**d
  for beta in [F(1,10),F(1),F(4)]:
   v=sum(1/(float(beta)*sum(2-2*cos(pi*n/L)for n in ns)+4/(3*N))for ns in product(range(2*L),repeat=d)if any(ns))/N
   lower=(sum(1/j for j in range(1,L))/(pi*pi*float(beta)+1/3))if d==2 else isqrt(L)/(pi*pi*float(beta)+2/3)
   assert v>=lower;count+=1
# Formal Taylor multiplication: covariance inequality coefficients via convolution, no Sympy integrator.
sinh={n:F(1,factorial(n))for n in range(1,29,2)}
sq={n:sum((a*b for i,a in sinh.items()for j,b in sinh.items()if i+j==n),F(0))for n in range(2,29,2)}
for n in range(4,29,2):assert sq[n-2]-3*sq[n]>=0;count+=1
for n in range(3,29,2):assert F(1,3*factorial(n-2))-F(n-1,factorial(n))>=0;count+=1
# Actual periodized side2 graph: two incidences to every distinct neighbour.
mult=Counter(tuple((int(j==i)*sgn)%2 for j in range(3))for i in range(3)for sgn in [-1,1]);assert len(mult)==3 and set(mult.values())=={2};count+=1
observations['side2_frozen_site_step']={'distinct_neighbours':len(mult),'multiplicity':2,'k0_boundary_coefficient_over_c':2,'claimed_over_c':1}
# Noninteger R shell defect, and exact nearer-endpoint charging on finite graph patches.
assert 2<sqrt(2)+1 and not 2<=sqrt(2);count+=1
chargecases=[]
for R2 in [2,5,10,25,41]:
 m=isqrt(R2)+2;charges=Counter();active=0
 for x in product(range(-m,m+1),repeat=2):
  for i in range(2):
   y=tuple(x[j]+int(j==i)for j in range(2));dx=sum(z*z for z in x);dy=sum(z*z for z in y)
   if min(dx,dy)<R2:
    near=x if dx<=dy else y;charges[near]+=1;active+=1
 assert sum(charges.values())==active and max(charges.values())<=4
 assert all(sum(z*z for z in x)<R2 and max(map(abs,x))<=isqrt(R2)for x in charges);count+=2
 chargecases.append({'radius_squared':R2,'active_bonds':active,'maximum_charge':max(charges.values())})
# Laurent polynomial contour shift: constant coefficient unchanged for general finite powers,
# using rational q=e^a and no trig integration path of primary.
for degree in [2,5,7]:
 poly={0:F(1)}
 for _ in range(degree):
  nxt=Counter()
  for k,v in poly.items():
   for j,c in [(-1,F(2,7)),(0,F(3,5)),(2,F(1,3))]:nxt[k+j]+=v*c
  poly=nxt
 for q in [F(2),F(3,2),F(1,4)]:
  shifted={k:v*q**(-k)for k,v in poly.items()};assert shifted.get(0,0)==poly.get(0,0);count+=1
# A beta-independent faster power satisfies all stated upper exponents (0<kappa<=1).
for R in range(1,25):
 for k in [F(1,2),F(1),F(1,100)]:assert (1+R)**-2 <= (1+R)**(-float(k));count+=1
out={'checks_pass':count,'checks_fail':0,'elapsed_seconds':time.monotonic()-start,'scope':'Independent direct spectral-sum sanity, exact formal coefficient convolution, graph multiplicities/nearer-endpoint charge and Laurent coefficient shift; not primary execution or negative certificate. Reuses prior8153 exact rotation-generator/root controls unchanged.','observations':observations,'nearer_endpoint_charge_cases':chargecases,'bound_inference_counterexample':'(1+R)^-2 is a fixed faster power compatible with every original0<kappa(beta)<=1 upper bound; varying upper exponent does not exclude fixed powers.'}
p=pathlib.Path('/private/tmp/review-drain-20260915/check8154/controls.json');assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
