#!/usr/bin/env python3
import hashlib,json,math,platform
from pathlib import Path
import sympy as s
r=s.symbols('r',positive=True);N=s.Function('N')(r);B=s.Function('B')(r)
l=s.log(N);y=1/r-s.diff(l,r)
Gt=(B-1)/r**2+s.diff(B,r)/r
Ga=B*(s.diff(l,r,2)+s.diff(l,r)**2+s.diff(l,r)/r)+s.diff(B,r)/2*(s.diff(l,r)+1/r)
u=(Ga-Gt)/(B*y)
logF_derivative=-s.diff(y,r)/y-2/r-s.diff(l,r)-s.diff(B,r)/(2*B)+1/(B*y*r**2)
checks=[]
def exact(name,v):
 z=s.factor(s.simplify(v));checks.append({'name':name,'pass':z==0,'residual':str(z)})
exact('integration by parts general metric',u-logF_derivative)
p,b=s.symbols('p b',positive=True)
c=(b*p*p-b+1)/(b*(1-p))
exact('power metric exponent',c-(1/(b*(1-p))-1-p))
# Compute circular geodesic frequency from the radial connection directly.
Npow=r**p;Gamma_rtt=b*Npow*s.diff(Npow,r);Gamma_rphph=-b*r
omega_coordinate_squared=-Gamma_rtt/Gamma_rphph
exact('geodesic clock frequency',omega_coordinate_squared-r**(2*p)*p/r**2)
R=r**p;S=r**(-p)/s.sqrt(b);v2=p
exact('radial null slowness',S-1/(R*s.sqrt(b)))
exact('orbital/redshift consistency',s.diff(s.log(R),r)-v2/r)
observable_derivative=s.diff(s.log(S),r)-1/r+s.diff(v2,r)/(1-v2)+R**2*S**2/(r*(1-v2))
exact('observable F reconstruction',observable_derivative-c/r)
# Declared deterministic error examples, not statistical coverage.
bounds=[]
for pv in [0.0,0.2,0.6,0.9]:
 for bv in [0.3,0.7,1.2]:
  for dp in [1e-4,0.002]:
   # C1-clock perturbation p -> p+dp, b fixed, on [1,2].
   ph=pv+dp;n0=1.0;b0=bv;y0=(1-ph)/2
   eN=dp*math.log(2)*2**ph;ey=dp
   E=2*eN/n0+2*ey/y0+0.5*ey/(b0*y0*y0)
   cv=(bv*pv*pv-bv+1)/(bv*(1-pv));ch=(bv*ph*ph-bv+1)/(bv*(1-ph))
   actual=abs((ch-cv)*math.log(2))
   bounds.append({'p':pv,'b':bv,'dp':dp,'log_ratio_error':actual,'deterministic_bound':E,'inside':actual<=E})
# Deliberately omit a measurement factor: the wrong observable inverse must differ.
mutants=[]
for name,v in [('drop_clock_factor',observable_derivative-R**2*S**2/(r*(1-v2))+S**2/(r*(1-v2))),('omit_speed_denominator',s.diff(s.log(S),r)-1/r+R**2*S**2/r),('reciprocal_radar_slowness',-s.diff(s.log(S),r)-1/r+R**2/S**2/(r*(1-v2)))]:
 difference=s.factor((v-c/r).subs({p:s.Rational(1,4),b:s.Rational(1,2)}))
 mutants.append({'name':name,'detected':difference!=0,'residual':str(difference)})
root=Path(__file__).resolve().parent
out={'kind':'synthetic mathematical author controls','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'derivation_sha256':hashlib.sha256((root/'BLOCK01_DERIVATION_v4.md').read_bytes()).hexdigest(),'python':platform.python_version(),'sympy':s.__version__,'exact_checks':checks,'deterministic_bound_examples':bounds,'mutations':mutants,'no_empirical_data':True,'pass':all(x['pass'] for x in checks) and all(x['inside'] for x in bounds) and all(x['detected'] for x in mutants)}
(root/'BLOCK01_OBSERVABLE_CONTROLS_v1.json').write_text(json.dumps(out,indent=2)+'\n')
for z in checks:print(('PASS ' if z['pass'] else 'FAIL ')+z['name']+': '+z['residual'])
print('DETERMINISTIC_BOUND_EXAMPLES',len(bounds),'inside',sum(x['inside'] for x in bounds),'max_error_bound_ratio',max(x['log_ratio_error']/x['deterministic_bound'] for x in bounds))
for x in mutants:print('MUTATION',x)
print('TOTAL: PASS=%d FAIL=%d; BOUND_EXAMPLES=%d; DETECTED_MUTATIONS=%d/%d'%(sum(x['pass'] for x in checks),sum(not x['pass'] for x in checks),len(bounds),sum(x['detected'] for x in mutants),len(mutants)))
raise SystemExit(0 if out['pass'] else 1)
