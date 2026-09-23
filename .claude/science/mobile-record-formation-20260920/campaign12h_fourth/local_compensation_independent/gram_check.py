#!/usr/bin/env python3
from collections import defaultdict
from fractions import Fraction
import json
from model import *


def main():
 edges=CUBE_EDGES;A=CUBE_A;q0=tuple(int(v in A) for v in range(8));s0=(q0,(0,)*12)
 first=edges.index((0,1));rows=[]
 for c in [1,None]:
  v=effective_birth(s0,first,c,A,edges)
  denominator=int(sum(abs(a)**2 for a in v.values()));gram=defaultdict(Fraction)
  for edge in range(12):
   for charge in [-1,1]:
    out=apply_paths(v,lambda s:effective_birth(s,edge,charge,A,edges).items())
    for (q,E),amp in out.items():
     for (q2,E2),amp2 in out.items():
      if q!=q2:continue
      assert amp.imag==amp2.imag==0
      gram[tuple(x-y for x,y in zip(E,E2))]+=Fraction(int(amp.real*amp2.real),denominator)
  assert gram[(0,)*12]==8 and len(gram)==3
  flow=next(s for s in gram if any(s));assert gram[flow]==gram[tuple(-x for x in flow)]==1
  assert sum(abs(s) for s in flow)==4
  # Delta_0 and (delta_0 +/- delta_flow)/sqrt(2): independent physical field densities.
  assert gauss(q0,flow,A,edges)
  rows.append({'first_charge':c,'first_norm_squared':denominator,'pulled_back_total_second_loss_over_kappa':[{'shift':s,'coefficient':str(v)} for s,v in sorted(gram.items())],'expectation_on_delta0':8,'expectation_on_equal_plus_pair':9,'expectation_on_equal_minus_pair':7})
 # Normalized shift weight identity on every finite-spin local link value.
 checks=[]
 for S in range(1,8):
  C=S*(S+1)
  for m in range(-S,S+1):
   for sigma in [-1,1]:
    weight=Fraction(C-m*m-sigma*m,C)
    assert 0<=weight<=1
    if abs(m+sigma)>S:assert weight==0
    assert 1-weight==Fraction(m*m+sigma*m,C)>=0
  checks.append({'S':S,'all_local_values_checked':2*(2*S+1)})
 return {'cube_formation_Grams':rows,'finite_spin_local_weight_checks':checks,'interpretation':'Immediate post-first-event hazard is field dependent; this does not determine its later survival law. The explicit two-mark isometry remains valid.'}

if __name__=='__main__':print(json.dumps(main(),indent=2))
