"""Additional boundary and canonical provenance checks."""
AUDIT_TIMEOUT_SEC=120
import numpy as np
import sympy as s
from pathlib import Path
import json,hashlib
rows=[]
def ck(n,c):rows.append({'name':n,'passed':bool(c)})
ROOT=Path(__file__).resolve().parents[3]
frozen=json.loads((Path(__file__).parent/'frozen_sources.json').read_text())
for n,h in frozen.items():ck('hash:'+n,hashlib.sha256((ROOT/n).read_bytes()).hexdigest()==h)
data=json.loads((ROOT/'outputs/ringdown_action_inverse/controls.json').read_text())
for n,h in data['source_hashes'].items():ck('embedded_source:'+n,hashlib.sha256((ROOT/n).read_bytes()).hexdigest()==h)
# Zero gradient and zero second harmonic are permitted if fundamental/pole visible.
for nu,G in [(0.,1.),(.2,0.),(.2,.7)]:
    tau=1.4;Ga=.3;O=2.;la=-Ga/2+1j*np.sqrt(O-Ga*Ga/4);a=2*la+Ga;n=G+nu*la;rho=-n*n/(tau*a);c=.4-.3j;f=n*c;h=0;g=0
    K=abs(a*rho);Q=K*h/abs(f)**2;S=-2*a*rho*g/f**2;r=(S-Q)/(O-la*la)
    ck('zero_gradient:'+str((nu,G)),Q==0 and S==0 and r==0 and abs(rho)>0 and abs(f)>0)
# Semidefinite Rayleigh boundary is admissible and remains so under shift.
for k in [-.7,0,.9]:
    tau=1.2;gamma=.4;nu=.2;d=nu*nu/gamma
    nunew=nu-gamma*k/tau;dnew=d-2*nu*k/tau+gamma*k*k/tau**2
    ck('semidefinite_boundary:'+str(k),abs(dnew*gamma-nunew*nunew)<1e-14 and dnew>=0)
# S and Q genuinely invariant under shifts of clock origin.
la=-.2+1.3j;Ga=.4;O=abs(la)**2;n=.7+.2j;tau=1.1;rho=-n*n/(tau*(2*la+Ga));c=.2+.4j;op=.3;r=.1
f=n*c;h=tau*op*abs(c)**2;g=tau*(op+r*(O-la*la))*c*c/2
S=-2*(2*la+Ga)*rho*g/f**2;Q=abs((2*la+Ga)*rho)*h/abs(f)**2
for shift in [-2.,.5,3.]:
    fs=f*np.exp(la*shift);gs=g*np.exp(2*la*shift);hs=h*np.exp(-Ga*shift)
    ck('clock_origin:'+str(shift),abs(-2*(2*la+Ga)*rho*gs/fs**2-S)<1e-14 and abs(abs((2*la+Ga)*rho)*hs/abs(fs)**2-Q)<1e-14)
# Nonaffine linear response: chain rule with dynamic perturbation symbolic.
jp,jpp,R0,Z,dx=s.symbols('jp jpp R0 Z dx',nonzero=True)
Rnew=(R0+Z*dx)/(jp+jpp*dx)
ck('nonaffine_variation',s.simplify(s.diff(Rnew,dx).subs(dx,0)/jp-(Z/jp**2-R0*jpp/jp**3))==0)
# Exact scope and prediction accounting from actual combined output.
ck('fit_split',all(r['preparation_fit_samples']==60 and r['reserved_prediction_samples']==541 for r in data['inverse_details']['reserved_synthetic_predictions']))
ck('dev_count',data['inverse_details']['grid_points']==61)
ck('no_empirical_claim',data['empirical_validation'] is False and data['data_roles']['independent_empirical_test']=='none')
ck('all_predicates_in_total',len(data['checks'])==194 and all(r['passed'] for r in data['checks']))
result={'summary':{'passed':sum(r['passed'] for r in rows),'failed':sum(not r['passed'] for r in rows)},'checks':rows};print(json.dumps(result,indent=2));assert not result['summary']['failed']
