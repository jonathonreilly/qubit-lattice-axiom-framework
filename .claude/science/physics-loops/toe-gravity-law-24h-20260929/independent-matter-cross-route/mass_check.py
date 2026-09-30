#!/usr/bin/env python3
"""Exact full relative-lapse cancellation of staggered-mass commutator terms."""
from position_check import energy,plus,minus,addterm
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;start=time.monotonic()
E={(k,0):v for k,v in energy().items()}
for a in product([-1,1],repeat=3):
    for s in range(2):E[((a,s,a,s,0),1)]=F(-1,8) # epsilon(a)=-1
out=defaultdict(F);paths=0
for ((a,r,b,s,i),power_a),v in E.items():
    for ((c,t,e,u,j),power_b),w in E.items():
        if s!=t or not power_a+power_b:continue
        # E_0 E_d; mass of translated E_0 gets epsilon(d).
        d=minus(b,c);n=i+j+1;z=-v*w*(-1 if n//2%2 else 1)
        factor=-1 if (sum(d)*power_b)%2 else 1
        addterm(out,(d,a,r,plus(e,d),u,n%2,power_a+power_b),z*factor)
        # E_d E_0, independently place the first factor at d.
        d=minus(c,b);factor=-1 if (sum(d)*power_a)%2 else 1
        addterm(out,(d,plus(a,d),r,e,u,n%2,power_a+power_b),-z*factor)
        paths+=2
assert not out
data={'mass_dependent_product_paths':paths,'mass_and_mass_squared_residual_coefficients':len(out),'all_real_staggered_masses':True,'elapsed_s':time.monotonic()-start}
(P/'mass_results.json').write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))
