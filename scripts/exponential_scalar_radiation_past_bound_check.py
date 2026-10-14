"""Direct exact and quadrature controls; no observational calibration or fit."""
import argparse,json,math,pathlib,tempfile
import sympy as S
from scipy.integrate import quad

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    'docs/EXPONENTIAL_SCALAR_RADIATION_PAST_BOUND_BOUNDED_THEOREM_NOTE_2026-10-14.md',
    'docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md',
]

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args();tmp=tempfile.TemporaryDirectory(prefix='radiation-past-bound-') if args.output is None else None;out=pathlib.Path(args.output) if args.output else pathlib.Path(tmp.name)/'results';out.mkdir(parents=True,exist_ok=False)
 rows=[]
 def ck(name,condition,details=None):rows.append({'name':name,'ok':bool(condition),'details':details})
 def zero(name,e):
  v=S.simplify(e);ck(name,v==0,str(v))
 k=S.symbols('k',positive=True);ak=(1-k)*(1+3*k)/4;s=(1+k)/(k*(1-3*k));E=S.symbols('E',positive=True);F=1+s*E;J=1+(1-3*ak)*s*E
 C=(1+s)*E/F;Cmax=(1+s)/s;bu=S.sqrt(ak)/F;Kuu=J/F**2
 zero('action.coupling_norm',bu**2/Kuu-ak/J)
 zero('action.strict_domain_margin',1-3*ak-(1-3*k)**2/4)
 zero('action.conformal_upper_gap',Cmax-C-(1+s)/(s*F))
 # The full action at phi=0 has zero gradient and vanishing conformal trace source for radiation.
 u,x,y,nu=S.symbols('u x y nu',real=True);alpha=S.sqrt(ak);Eu=S.exp(2*alpha*u);Fu=1+s*Eu
 U=S.Rational(3,2)+3*s*(Eu-1)**2/(2*Fu**2)+k*x*x*S.exp(-(1-k)*u/alpha)/2+k*y*y*S.exp(-(1+k)*u/alpha)/3+nu*(1+s)*u*u/(2*Fu**2)
 origin={u:0,x:0,y:0}
 zero('action.vacuum_value',U.subs(origin)-S.Rational(3,2))
 for z in [u,x,y]:zero('action.stationary_'+str(z),S.diff(U,z).subs(origin))
 zero('action.vacuum_conformal',C.subs(E,1)-1)
 A,HE,c,rj=S.symbols('A HE c rj',positive=True);HJ=(HE+c)/A
 density_power=4
 rhoE=A**density_power*rj
 rhoEdot=density_power*c*rhoE+A**density_power*(-4*HJ*rj)*A
 zero('radiation.conformal_conservation',rhoEdot+4*HE*rhoE)
 aE=S.symbols('aE',positive=True)
 zero('radiation.charge_conformal',rhoE*aE**4-rj*(A*aE)**4)
 zero('radiation.trace',rj-3*(rj/3))
 X,D,h,Q,r0,a0=S.symbols('X D h Q r0 a0',positive=True)
 clock_factor=S.Rational(1,2)
 T=clock_factor*S.asinh(h*X/D)/h
 zero('comparison.clock_derivative',S.diff(T,X)-1/(2*S.sqrt(h*h*X*X+D*D)))
 zero('comparison.saturation_derivative',S.diff(T,X)*2*S.sqrt(h*h*X*X+D*D)-1)
 Tstar=S.simplify(T.subs({X:a0*a0,D:a0*a0*S.sqrt(r0/(3*Q))}))
 zero('comparison.scale_normalization_cancel',Tstar-S.asinh(h*S.sqrt(3*Q/r0))/(2*h))
 zero('comparison.physical_density',Tstar.subs(r0,A**4*rj)-S.asinh(h*S.sqrt(3*Q/rj)/(A*A))/(2*h))
 z=S.symbols('z',positive=True)
 zero('comparison.coarse_integrand_gap',1-S.diff(S.asinh(z),z)-(1-1/S.sqrt(1+z*z)))
 t=S.symbols('t',positive=True);Xexact=D*S.sinh(2*h*t)/h;Hexact=h*S.coth(2*h*t)
 zero('saturation.definition_H',S.diff(Xexact,t)/(2*Xexact)-Hexact)
 zero('saturation.friedmann',Hexact**2-h*h-D*D/Xexact**2)
 zero('saturation.raychaudhuri',S.diff(Hexact,t)+2*D*D/Xexact**2)
 Kcurve=12*((S.diff(Hexact,t)+Hexact**2)**2+Hexact**4)
 zero('saturation.kretschmann',S.trigsimp(Kcurve-24*h**4*(1+1/S.sinh(2*h*t)**4)))
 zero('saturation.ricci_scalar_constant',6*(S.diff(Hexact,t)+2*Hexact**2)-12*h*h)
 zero('vacuum.kretschmann_finite',12*(h**4+h**4)-24*h**4)
 # Distinct dimensionful synthetic values; these are comparison functions, not scalar orbits.
 samples=[]
 for hv in [.4,1.7]:
  for dens in [.07,1.2]:
   q=2.3;x0=1.6**2;dd=x0*math.sqrt(dens/(3*q));bound=math.asinh(hv*math.sqrt(3*q/dens))/(2*hv)
   for stiff in [0.,.03,2.]:
    integrand=lambda xx: 1/(2*math.sqrt(hv*hv*xx*xx+dd*dd+(stiff/xx if xx else 0))) if xx else (1/(2*dd) if stiff==0 else 0)
    val,err=quad(integrand,0,x0,epsabs=1e-11,epsrel=1e-11)
    row={'Hv':hv,'Q':q,'rhoE0':dens,'X0':x0,'extra_positive_stiff':stiff,'duration':val,'quad_error_estimate':err,'comparison_bound':bound};samples.append(row)
    ck('quadrature.comparison',val<=bound+2e-11,row)
    if stiff==0:ck('quadrature.saturating_age',abs(val-bound)<2e-11,row)
    else:ck('quadrature.strict_positive_extra',val<bound,row)
   coarse=.5*math.sqrt(3*q/dens)
   ck('quadrature.positive_vacuum_sharpens',bound<coarse,{'bound':bound,'coarse':coarse})
 # Nonuniform limits and the exact-radiation singularity: test established formulas, not fit data.
 for kval in [.001,.11,.32]:
  coeff=(1-kval)*(1+3*kval)/4;sk=(1+kval)/(kval*(1-3*kval));eta=1-math.sqrt(3*coeff)
  ck('clock.positive_margin',eta>0,{'k':kval,'eta':eta})
  ck('physical.loose_vacuum_Cmax',math.sqrt((1+sk)/sk)>1)
 vals=[math.asinh(math.sqrt(3/r))/(2) for r in [1.,.01,.0001]]
 ck('vacuum_limit.duration_grows',vals[0]<vals[1]<vals[2],vals)
 ks=[24*(1+1/math.sinh(2*t0)**4) for t0 in [.5,.1,.01]]
 ck('radiation_endpoint.K_diverges',ks[0]<ks[1]<ks[2],ks)
 result={'scope':'Exact algebra plus positive comparison-function quadrature. No full rolling orbit, empirical fit or initial-state selection.','checks':rows,'passed':sum(r['ok'] for r in rows),'failed':sum(not r['ok'] for r in rows),'comparison_samples':samples}
 (out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));raise SystemExit(bool(result['failed']))
if __name__=='__main__':main()
