"""Analytic continuum-versus-pole controls; synthetic, not observational data."""
from pathlib import Path
import json,math
from scipy.integrate import quad
rows=[]
for kind in ['gaussian','resolvent']:
 for tau in [4,16,64,256]:
  for atom in [0.,.25]:
   # Resolve the filter peak in y=tau*x. Original unscaled adaptive
   # quadrature missed the narrow x^2*F^2 peak at tau=256.
   if kind=='gaussian':
    F=lambda y:math.exp(-.5*y*y)
    upper=min(tau,12.) # omitted Gaussian tails below 1e-30
   else:
    F=lambda y:1/(1+y*y)
    upper=tau
   a=atom+(1-atom)*quad(F,0,upper,epsabs=1e-12)[0]/tau
   z=atom+(1-atom)*quad(lambda y:F(y)**2,0,upper,epsabs=1e-12)[0]/tau
   var=(1-atom)*quad(lambda y:y*y*F(y)**2,0,upper,epsabs=1e-12)[0]/(tau**3*z)
   assert var>0
   if kind=='gaussian' and atom==0:
    exact=(.5-math.exp(-tau*tau)*tau/(math.sqrt(math.pi)*math.erf(tau)))/tau**2
    assert abs(var/exact-1)<1e-10
   rows.append(dict(filter=kind,tau=tau,atom_weight=atom,source_overlap_squared=a*a/z,std=math.sqrt(var)))
for kind,target in [('gaussian',math.sqrt(math.pi)),('resolvent',math.pi)]:
 row=next(x for x in rows if x['filter']==kind and x['tau']==256 and x['atom_weight']==0)
 assert abs(row['source_overlap_squared']*256/target-1)<.01
 row=next(x for x in rows if x['filter']==kind and x['tau']==256 and x['atom_weight']==.25)
 assert abs(row['source_overlap_squared']-.25)<.02
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Synthetic uniform continuum plus optional central atom; distinguishes shrinking overlap from genuine pole weight; no empirical data', 'rows':rows},indent=2)+'\n')
print('4 overlap asymptotics, 4 analytic Gaussian variances, and 16 positive-width controls passed')
