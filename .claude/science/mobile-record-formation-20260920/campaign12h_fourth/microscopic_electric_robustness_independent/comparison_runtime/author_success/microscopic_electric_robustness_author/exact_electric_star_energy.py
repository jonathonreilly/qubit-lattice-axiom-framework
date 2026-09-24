#!/usr/bin/env python3
"""Personal exact star extension across the reviewed electric family."""
from pathlib import Path
import importlib.util,hashlib,json,sys
sys.dont_write_bytecode=True
import sympy as s
HERE=Path(__file__).resolve().parent
source=HERE.parent/'microscopic_birth_energy_author/exact_star_energy.py'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='ce202e534e19254516e7a3437c5c19e8a229334170eda73f65a16ae2f1fa377e'
spec=importlib.util.spec_from_file_location('root_star_for_electric_family',source);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
e,delta,kappa=m.e,m.delta,m.kappa
K,lam=s.symbols('K lambda',nonnegative=True);a=1+3*e**2
E2={N:s.diag(*[sum(x*x for x in m.fields(q)) for q in m.bases[N]]) for N in (1,3)}
assert E2[1]==m.W1 and E2[3]==2*s.eye(12)+m.W3
H1=delta/e**4*m.h1+K*lam*E2[1];H3=delta/e**4*m.h3+K*lam*E2[3]
psi=m.psi_num;rho=psi*psi.T/a
E_initial=s.factor(s.trace(H1*rho));assert s.simplify(E_initial-3*K*lam*e**2/a)==0
rows=[];derivatives={}
for inst in ('resolved','coherent'):
 gain=0;loss=s.zeros(4)
 for b in (1,2,3):
  marks=[(str(c),m.jump(b,c)) for c in (1,-1)] if inst=='resolved' else [('coherent',m.jump(b,1)+m.jump(b,-1))]
  for label,j in marks:
   v=j*m.F1*m.v0;nn=(v.T*v)[0];eta=v*v.T/nn
   mean=s.factor(s.trace(H3*eta));variance=s.factor(s.trace(H3*H3*eta)-mean**2)
   c=s.factor((v.T*m.F3.T*m.F3*v)[0]/nn)
   assert s.simplify(mean-c*delta/e**2-2*K*lam)==0
   assert s.simplify(variance-c*delta**2/e**6*(1+(3-c)*e**2))==0
   gain+=kappa/e**2*s.trace(H3*j*rho*j.T);loss+=j.T*j
   rows.append({'instrument':inst,'edge':[0,b],'mark':label,'c':str(c),'conditional_mean':str(mean),'conditional_variance':str(variance)})
 diss=-kappa/(2*e**2)*s.trace(H1*(loss*rho+rho*loss))
 total=s.factor(gain+diss)
 assert s.simplify(total-18*kappa*delta/(e**2*a)-12*kappa*K*lam/a)==0
 derivatives[inst]={'gain':str(s.factor(gain)),'loss':str(s.factor(diss)),'total':str(total)}
G=s.Matrix([[-s.I*3*delta/e**2,s.I*s.sqrt(3)*delta/e**3],[s.I*s.sqrt(3)*delta/e**3,-s.I*(delta/e**4+K*lam)-2*kappa/e**2]])
z=s.symbols('z');poly=s.expand(e**4*(z*s.eye(2)-G).det())
expected=e**4*z*z+(s.I*delta*a+2*kappa*e**2+s.I*K*lam*e**4)*z+s.I*6*kappa*delta-3*delta*K*lam*e**2
assert s.simplify(poly-expected)==0
zs=-6*kappa+(18*kappa-s.I*(12*kappa**2/delta+3*K*lam))*e**2
assert s.simplify(s.series(poly.subs(z,zs),e,0,4).removeO())==0
# Bounded E2 acts as a scalar on every immediate output, explaining the
# unchanged variance without assuming commutation of H0 and E2 globally.
for b in (1,2,3):
 for c in (1,-1):
  v=m.jump(b,c)*m.F1*m.v0;assert E2[3]*v==2*v
result={'standing':'Personal exact symbolic family calculation; independent review pending','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'initial_common_preparation_energy':str(E_initial),'conditional_outputs':rows,'initial_energy_derivatives':derivatives,'scaled_no_event_characteristic_polynomial':str(poly),'slow_eigenvalue_through_epsilon2':str(zs),'no_event_initial_vector':'(1,sqrt(3)epsilon)/sqrt(1+3epsilon²)','finite_time_formed_energy_coefficient':'3delta/(2epsilon²)+2K lambda','checked_symbolically':True}
(HERE/'EXACT_ELECTRIC_STAR_ENERGY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'initial_energy':str(E_initial),'resolved_energy_derivative':derivatives['resolved'],'slow_eigenvalue':str(zs)},indent=2))
