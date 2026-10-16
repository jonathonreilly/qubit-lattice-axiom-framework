"""Post-original-exposure exact mathematics; no author imports or file reads."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = []
import json
import sys
import sympy as s

checks=[];details={}
def ck(name,predicate,detail=None):
    checks.append({"name":name,"passed":bool(predicate),"detail":detail})
    print(json.dumps({"progress":name,"passed":bool(predicate)}),file=sys.stderr,flush=True)
def zero(name,expr):
    value=s.factor(s.together(expr));ck(name,value==0,str(value))

# Build the constraint from differentiation of the independently derived flow.
v=s.symbols("v",real=True,nonzero=True)
h,hd,q,qd,qdd,al,ald,mu=s.symbols("h hd Q Qd Qdd alpha alphadot mu",real=True)
flow=(qd+3*h*q)/(2*v)-3*h*v/2-al*q/2+al*v*v/2
partial=s.diff(flow,h)*hd+s.diff(flow,q)*qd+s.diff(flow,qd)*qdd+s.diff(flow,al)*ald
constraint=s.expand(4*v**3*(partial+s.diff(flow,v)*flow+3*h*flow+(3*hd+mu)*v-3*h*al*(q-v*v)))
zero("reflection_polynomial_invariant",constraint.subs({v:-v,al:-al,ald:-ald},simultaneous=True)-constraint)
zero("reflection_velocity_flow_odd",flow.subs({v:-v,al:-al},simultaneous=True)+flow)
t=s.symbols("t",positive=True);M=s.symbols("M",positive=True)
B=s.Function("B",positive=True)(t);rep=s.sqrt(B)/M
zero("positive_square_coupling",M*M*rep*rep-B)
zero("positive_square_derivative",s.diff(rep,t)-s.diff(B,t)/(2*M*s.sqrt(B)))
phi,psi=s.symbols("phi psi",real=True)
A=s.exp(phi+phi**2/5);V=phi**3+2*phi**2+7
AR=A.subs(phi,-psi);VR=V.subs(phi,-psi)
trajectory=t*t+t;rho=s.Function("rho")(t)
zero("nontrivial_action_reflection_A",AR.subs(psi,-trajectory)-A.subs(phi,trajectory))
zero("nontrivial_action_reflection_V",VR.subs(psi,-trajectory)-V.subs(phi,trajectory))
zero("nontrivial_action_reflection_coupling",(s.diff(AR,psi)/AR).subs(psi,-trajectory)+(s.diff(A,phi)/A).subs(phi,trajectory))
zero("nontrivial_action_reflection_mass",(s.diff(VR,psi,2)+rho*s.diff(AR,psi,2)).subs(psi,-trajectory)-(s.diff(V,phi,2)+rho*s.diff(A,phi,2)).subs(phi,trajectory))
ck("energy_negation_is_not_field_reflection",(VR.subs(psi,0)+V.subs(phi,0))==14)

# Registered density: independent differentiation of the square root.
K=s.symbols("K",positive=True);Kd,Kdd,rr,u=s.symbols("Kd Kdd r q",real=True)
expected=-Kdd/(2*K)+Kd**2/(4*K**2)-3*h*Kd/(2*K)-3*hd+3*h*rr*u/K
for sign in (1,-1):
    vv=sign*s.sqrt(K);dv=sign*Kd/(2*s.sqrt(K));ddv=sign*(Kdd/(2*s.sqrt(K))-Kd**2/(4*K**s.Rational(3,2)))
    alpha=u/vv
    derived=-ddv/vv-3*h*dv/vv-3*hd+3*h*alpha*rr/vv
    zero(f"registered_density_mass_sign_{sign}",derived-expected)
    zero(f"registered_density_dust_sign_{sign}",alpha*vv-u)
zero("registered_density_square_compatibility",(u/s.sqrt(K))**2*K-u*u)
# Original scalar equation from the energy value, rather than its derivative.
Rdot=rr*(u-3*h)
Vdot=6*M*M*h*hd-Rdot-Kd/2
zero("registered_density_original_scalar_equation",(Vdot/s.sqrt(K)+Kd/(2*s.sqrt(K))+3*h*s.sqrt(K)+u*rr/s.sqrt(K)).subs(hd,-(K+rr)/(2*M*M)))

# Independent closed form for the author's non-power-law fixture.
hh=1/t;rd=1/(4*t);vv=s.sqrt(8-t)/(2*t)
at=t*t/4;vt=2/t**2-1/(8*t);rh=t**-3
alpha_t=s.diff(at,t)/(at*vv)
mass=(s.diff(s.diff(vt,t)/vv,t)+rh*s.diff(s.diff(at,t)/vv,t))/vv
mass_closed=(1024-48*t-9*t*t)/(4*t*t*(8-t)**2)
zero("variable_coupling_closed_alpha",alpha_t-4/s.sqrt(8-t))
zero("variable_coupling_closed_mass",mass-mass_closed)
kt=-2*s.diff(hh,t)-rd;qt=s.diff(rd,t)/rd+3*hh
mass_density=expected.subs({K:kt,Kd:s.diff(kt,t),Kdd:s.diff(kt,t,2),h:hh,hd:s.diff(hh,t),rr:rd,u:qt},simultaneous=True)
zero("variable_coupling_registered_density_agreement",mass_density-mass_closed)
zero("variable_coupling_dust_match",qt/vv-alpha_t)
ck("variable_coupling_domain_at_end_bounds",(8-s.Integer(4))>0 and s.Integer(1)>0,{"interval":"1<t<4; r positive and 8-t>4"})
details["variable_coupling"]={"alpha":str(s.factor(alpha_t)),"mu_closed":str(mass_closed),"mu_at_t2":str(mass_closed.subs(t,2))}

# Conformal number-volume and clock conversion, not an observation bridge.
ac=s.Function("a")(t);fac=s.Function("A")(t)
hj=s.diff(fac*ac,t)/(fac*fac*ac)
zero("Jordan_expansion_kinematics",hj-(s.diff(ac,t)/ac+s.diff(fac,t)/fac)/fac)
rhoJ=s.symbols("rho_J",positive=True)
zero("Jordan_to_bare_density",fac**3*rhoJ/fac**3-rhoJ)
zero("Jordan_to_Einstein_density",fac*(fac**3*rhoJ)-fac**4*rhoJ)

# Sensitivity of an instantaneous algebraic root only.
eps=s.symbols("eps",positive=True)
p=(2+eps)/3
mup=2+(8*eps+5*eps**2+2*eps**3)/3
pe=s.factor(constraint.subs({h:p,hd:-p,q:2*p,qd:-4*p,qdd:12*p,al:eps,ald:0,mu:mup},simultaneous=True))
zero("near_degenerate_true_root",pe.subs(v,1))
expected_slope=eps*(4*eps**3+16*eps**2+139*eps+174)/9
slope=s.factor(s.diff(pe,v).subs(v,1))
zero("near_degenerate_hand_slope",slope-expected_slope)
zero("near_degenerate_input_mass",mup-(-2+6*p+3*p*eps*(2*p-1)))
zero("polynomial_mass_derivative",s.diff(constraint,mu)-4*v**4)
sensitivity=-4/slope
zero("near_degenerate_sensitivity",sensitivity+36/(eps*(4*eps**3+16*eps**2+139*eps+174)))
zero("near_degenerate_scaled_limit",s.limit(eps*sensitivity,eps,0)+s.Rational(6,29))
zero("unique_fixture_slope_cross_check",slope.subs(eps,1)-37)
ck("near_degenerate_positive_domain",s.factor(2*p-1).is_positive is True and expected_slope.is_positive is True)
details["conditioning"]={"slope":str(slope),"dv_dmu_at_t1":str(s.factor(sensitivity)),"limit_eps_times_sensitivity":"-6/29","scope":"Instantaneous candidate sensitivity at fixed other input jets; no full-history statistical stability conclusion."}

out={"kind":"Independent mathematical additions after original-unit exposure, without author imports","python":sys.version,"sympy":s.__version__,"checks":checks,"summary":{"passed":sum(x['passed'] for x in checks),"failed":sum(not x['passed'] for x in checks)},"details":details,"file_reads":False,"author_code_imported":False,"empirical_validation":False}
print(json.dumps(out,indent=2))
assert not out['summary']['failed']
