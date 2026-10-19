"""Exact recurrence controls for the conditional zone-boundary/crossover operator."""
import json
from pathlib import Path
import sympy as s
from scipy.linalg import eigh
import numpy as np
r=s.symbols('r');k=-(r+1)**2/(4*r);eta=1/(k+1)
M=s.Matrix([[k-s.Rational(3,4),k/r+1/(4*r*r)-1],[s.Rational(1,4)-eta,1/(4*r)-eta*r]])
p=16*r**4+92*r**3+39*r*r-2*r-1
assert s.factor(M.det()+p/(16*r*r*(r-1)))==0
assert s.Poly(p,r).count_roots(-1,0)==2
root=[float(s.re(x)) for x in s.nroots(p) if abs(s.im(x))<1e-12 and -1<float(s.re(x))<0]
thresholds=sorted(float(k.subs(r,x)) for x in root)
rr=s.Rational(1,4);Z=1-rr**2;e=s.Rational(-1,2)+1+s.Rational(1,16)
assert e==s.Rational(9,16) and Z==s.Rational(15,16)
f2=s.Rational(25,16)*Z
curv=s.factor(f2*(s.Rational(656,135)/(1-rr**2)+s.Rational(16,15)*rr**2/(1-rr**2)**2))
assert curv==s.Rational(208,27)
E=s.symbols('E');roots=s.solve(31*E*E+76*E-36,E)
for x in roots:
 ratio=(x+2)/8
 assert abs(float(ratio))<1
 assert s.simplify(x+s.Rational(1,2)-(ratio+1/ratio)/4)==0
rows=[]
for kap,expected in [(0,2),(.1,2),(.3,1),(.7,1),(1.2,0),(2,0)]:
 N=320;H=np.diag(np.r_[.5,np.full(N-1,-.5),-2.])
 for j in range(N-1):H[j,j+1]=H[j+1,j]=kap
 for j in range(N-2):H[j,j+2]=H[j+2,j]=.25
 H[1,N]=H[N,1]=-np.sqrt(2)
 vals=eigh(H,subset_by_index=[N-2,N],eigvals_only=True)
 count=int(sum(vals>2*kap+1e-7));assert count==expected
 rows.append(dict(kappa=kap,top_values=vals.tolist(),finite_count=count,continuum_upper=2*kap))
out=dict(threshold_polynomial=str(p),admissible_r=root,thresholds=thresholds,odd_energy=str(e),odd_boundary_weight=str(Z),odd_source_weight_coefficient=str(4*Z),upper_curvature=str(curv),side_bound_energies=list(map(str,roots)),finite_controls=rows,scope='Exact algebra and conditional halfline proof controls, not native uniform-limit theorem')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(out)
