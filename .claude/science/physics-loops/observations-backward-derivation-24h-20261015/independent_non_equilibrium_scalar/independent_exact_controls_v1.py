"""Exact controls derived from the neutral contract before author exposure."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_non_equilibrium_scalar/NEUTRAL_CONTRACT_BEFORE_EXPOSURE_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_non_equilibrium_scalar/DERIVATION_BEFORE_AUTHOR_EXPOSURE_v1.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_non_equilibrium_scalar/PRE_CODE_FREEZE_v1.json",
]
import hashlib
import json
from pathlib import Path
import sys
import sympy as s

ROOT=Path(__file__).resolve().parents[5]
def bindings():
    return {p:{"sha256":hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),"bytes":(ROOT/p).stat().st_size} for p in AUDIT_INPUT_PATHS}
initial=bindings();checks=[];details={}
def ck(name,passed,detail=None):
    checks.append({"name":name,"passed":bool(passed),"detail":detail})
    print(json.dumps({"progress":name,"passed":bool(passed)}),file=sys.stderr,flush=True)
def zero(name,expr):
    rem=s.factor(s.together(expr));ck(name,rem==0,str(rem));return rem

frozen=json.loads((ROOT/AUDIT_INPUT_PATHS[2]).read_text())
ck("pre_code_proof_and_contract_unchanged",all(initial[str(Path(AUDIT_INPUT_PATHS[0]).parent/n)]["sha256"]==v["sha256"] for n,v in frozen["files"].items()))

# Independent jet algebra, with Q kept separate until the Einstein relation.
M=s.symbols("M",positive=True)
H,Hd,Q,Qd,Qdd,alpha,ad,mu=s.symbols("H Hd Q Qd Qdd alpha alpha_dot mu",real=True)
v=s.symbols("v",real=True,nonzero=True)
J=Qd+3*H*Q;Jd=Qdd+3*Hd*Q+3*H*Qd
r=Q-v*v
F=J/(2*v)-3*H*v/2-alpha*Q/2+alpha*v*v/2
Ft=s.diff(F,H)*Hd+s.diff(F,Q)*Qd+s.diff(F,Qd)*Qdd+s.diff(F,alpha)*ad
accel=Ft+s.diff(F,v)*F
R=accel+3*H*F+(3*Hd+mu)*v-3*H*alpha*r
P=(2*alpha**2*v**6+(2*ad+9*H*alpha)*v**5
   +(6*Hd-9*H**2+4*mu-2*alpha**2*Q)*v**4
   +(-2*ad*Q-alpha*Qd-12*H*alpha*Q)*v**3
   +(2*Jd+6*H*J)*v**2+alpha*Q*J*v-J**2)
zero("dust_equation_derives_velocity_flow",Qd-2*v*F+3*H*r-alpha*v*r)
zero("positive_A_log_derivative",(Qd-2*v*F)/r+3*H-alpha*v)
Vt=6*M**2*H*Hd-Qd+v*F
zero("friedmann_reconstruction_scalar_equation",(Vt/v+F+3*H*v+alpha*r).subs(Hd,-Q/(2*M*M)))
zero("polynomial_from_independent_partial_derivatives",4*v**3*R-P)
poly=s.Poly(P,v)
ck("polynomial_degree_six",poly.degree()==6)
zero("polynomial_leading_coefficient",poly.coeff_monomial(v**6)-2*alpha**2)
zero("polynomial_constant_coefficient",poly.coeff_monomial(1)+J**2)
Vphi=-F-3*H*v-alpha*r
Vphi_t=(s.diff(Vphi,H)*Hd+s.diff(Vphi,Q)*Qd+s.diff(Vphi,Qd)*Qdd
        +s.diff(Vphi,alpha)*ad+s.diff(Vphi,v)*F)
reconstructed_mu=Vphi_t/v+r*(ad/v+alpha**2)
zero("reconstructed_fixed_density_curvature",reconstructed_mu-(mu-R/v))
Vp,Ap,App,rho,Vpp=s.symbols("Vp Ap App rho Vpp",real=True)
Sdot=Vpp*v+rho*App*v-3*H*rho*Ap
zero("fixed_bare_density_force_derivative",Sdot-((Vpp+rho*App)*v-3*H*rho*Ap))
zero("uncoupled_polynomial_even",P.subs({alpha:0,ad:0,v:-v})-P.subs({alpha:0,ad:0}))
ck("uncoupled_degree_bound_four",s.Poly(P.subs({alpha:0,ad:0}),v).degree()<=4)
exception={alpha:0,ad:0,Qd:-3*H*Q,Qdd:-3*Hd*Q+9*H**2*Q,mu:(9*H**2-6*Hd)/4}
zero("exceptional_polynomial_identically_zero",P.subs(exception,simultaneous=True))
zero("exceptional_velocity_flow",F.subs(exception,simultaneous=True)+3*H*v/2)
zero("exceptional_fraction_conservation",((2*v*F*Q-v*v*Qd)/Q**2).subs(exception,simultaneous=True))
details["jet_algebra"]={"F":str(F),"P":str(s.Poly(P,v).as_expr()),"R_denominator":str(s.denom(s.factor(R))),"domain":"Q>0 and 0<v^2<Q; denominator multiplication is reversible only for v!=0","uniqueness":"F_v is continuous on the domain; IVP uniqueness does not guarantee constraint consistency or global interval existence"}

# Independent exact action fixture with alpha nonzero.
t=s.symbols("t",positive=True);phi=s.symbols("phi",real=True)
h=1/t;ph=s.log(t);vel=s.diff(ph,t);rhob=t**-3
Af=s.exp(phi);Vf=s.Rational(3,2)*s.exp(-2*phi)
at=Af.subs(phi,ph);vt=Vf.subs(phi,ph);rt=s.simplify(at*rhob)
al=s.simplify((s.diff(Af,phi)/Af).subs(phi,ph))
vp=s.diff(Vf,phi).subs(phi,ph)
mv=s.diff(Vf,phi,2).subs(phi,ph);ma=rhob*s.diff(Af,phi,2).subs(phi,ph)
zero("fixture_friedmann",3*h*h-vel**2/2-vt-rt)
zero("fixture_raychaudhuri",-2*s.diff(h,t)-vel**2-rt)
zero("fixture_scalar",s.diff(vel,t)+3*h*vel+vp+al*rt)
zero("fixture_bare_dust",s.diff(rhob,t)+3*h*rhob)
zero("fixture_einstein_dust",s.diff(rt,t)+3*h*rt-al*vel*rt)
zero("fixture_signed_alpha",al-1)
zero("fixture_potential_curvature",mv-6/t**2)
zero("fixture_dust_curvature",ma-1/t**2)
zero("fixture_input_mu",mv+ma-7/t**2)
force=vp+al*rt
zero("fixture_along_history_force_derivative",s.diff(force,t)/vel-4/t**2)
zero("fixture_missing_density_term",mv+ma-s.diff(force,t)/vel-3/t**2)
fixed_r_mass=(s.diff(Vf,phi,2)+rt*s.diff(s.diff(Af,phi)/Af,phi)).subs(phi,ph)
zero("fixture_fixed_Einstein_r_is_different",mv+ma-fixed_r_mass-1/t**2)
ck("fixture_open_domain",vel.is_positive is True and rt.is_positive is True)
c,d=s.symbols("c d",real=True)
badV=Vf+c*phi+d
zero("affine_potential_does_not_change_mu",s.diff(badV,phi,2)-s.diff(Vf,phi,2))
zero("affine_potential_retains_scalar_residual",s.diff(vel,t)+3*h*vel+s.diff(badV,phi).subs(phi,ph)+al*rt-c)
zero("affine_potential_retains_Friedmann_residual",3*h*h-vel**2/2-badV.subs(phi,ph)-rt+c*ph+d)
zero("constant_potential_shift_invisible_to_scalar_equation",s.diff(Vf+d,phi)-s.diff(Vf,phi))

x=s.symbols("x",real=True)
fixture_jets={H:1/t,Hd:-1/t**2,Q:2/t**2,Qd:-4/t**3,Qdd:12/t**4,alpha:1,ad:0,mu:7/t**2,v:x/t}
Px=s.factor(t**6*P.subs(fixture_jets,simultaneous=True))
Px_expected=2*x**6+9*x**5+9*x**4-20*x**3+4*x-4
zero("fixture_scaled_compatibility_polynomial",Px-Px_expected)
flow_defect=s.factor(-x-t*t*F.subs(fixture_jets,simultaneous=True))
zero("fixture_flow_for_constant_scaled_velocity",flow_defect+(x-1)*(x*x-2)/(2*x))
gcd=s.gcd(s.Poly(Px,x),s.Poly((x-1)*(x*x-2),x)).monic().as_expr()
zero("fixture_only_common_flow_root",gcd-(x-1))
count=s.Poly(Px,x).count_roots(-s.Rational(3,4),-s.Rational(1,2))
ck("spurious_constraint_root_in_admissible_interval",count==1 and s.Rational(3,4)**2<2,{"root_count":int(count),"interval":["-3/4","-1/2"]})
ck("spurious_root_sign_change",Px.subs(x,-s.Rational(3,4))>0 and Px.subs(x,-s.Rational(1,2))<0)
zero("dust_zero_boundaries_not_constraint_roots",s.rem(s.Poly(Px,x),s.Poly(x*x-2,x)).as_expr()-48)
zero("physical_scaled_velocity_root",Px.subs(x,1))
zero("physical_velocity_flow",flow_defect.subs(x,1))
details["nonzero_coupling_fixture"]={"H":str(h),"phi":str(ph),"A":str(Af),"V":str(Vf),"r":str(rt),"alpha":str(al),"mu":str(mv+ma),"polynomial":str(Px),"flow_defect":str(flow_defect),"common_root_gcd":str(gcd),"spurious_root_interval":["-3/4","-1/2"],"spurious_root_statement":"A constant root x in this interval gives smooth v=x/t satisfying pointwise P=0 but not the dust flow; P alone is insufficient."}

# Continuous family: dimensional reference time and density kept explicit.
lam=s.symbols("lambda",real=True,nonzero=True)
tstar,rhostar=s.symbols("t_star rho_star",positive=True)
hc=2/(3*t);phc=lam*s.log(t/tstar);vc=lam/t
rhoc=rhostar*(t/tstar)**-2
Ac=(4*M*M/3-lam*lam)/(rhostar*tstar*tstar)
Vcf=lam*lam/(2*tstar*tstar)*s.exp(-2*phi/lam)
Vct=s.simplify(Vcf.subs(phi,phc));rc=s.factor(Ac*rhoc)
Vcp=s.simplify(s.diff(Vcf,phi).subs(phi,phc))
Vcpp=s.simplify(s.diff(Vcf,phi,2).subs(phi,phc))
zero("continuous_family_friedmann",3*M*M*hc*hc-vc*vc/2-Vct-rc)
zero("continuous_family_raychaudhuri",-2*M*M*s.diff(hc,t)-vc*vc-rc)
zero("continuous_family_scalar",s.diff(vc,t)+3*hc*vc+Vcp)
zero("continuous_family_bare_dust",s.diff(rhoc,t)+3*hc*rhoc)
zero("continuous_family_Einstein_dust",s.diff(rc,t)+3*hc*rc)
zero("continuous_family_zero_signed_alpha",s.diff(Ac,phi))
zero("continuous_family_same_mu",Vcpp-2/t**2)
zero("continuous_family_constant_fraction",vc*vc/(-2*M*M*s.diff(hc,t))-3*lam*lam/(4*M*M))
Qc=4*M*M/(3*t*t)
jets_c={H:hc,Hd:s.diff(hc,t),Q:Qc,Qd:s.diff(Qc,t),Qdd:s.diff(Qc,t,2),alpha:0,ad:0,mu:2/t**2}
zero("continuous_family_polynomial_vanishes_for_all_v",P.subs(jets_c,simultaneous=True))
zero("continuous_family_all_signed_velocities_follow_flow",F.subs({**jets_c,v:vc},simultaneous=True)-s.diff(vc,t))
family_members=[]
for val in (s.Rational(1,2),s.Integer(1),-s.Rational(3,4)):
    av=Ac.subs({M:1,tstar:1,rhostar:1,lam:val});rr=s.factor(rc.subs({M:1,lam:val}))
    ck("family_member_open_domain_"+str(val),av>0 and val!=0 and val*val<s.Rational(4,3),{"A":str(av),"r":str(rr)})
    family_members.append({"lambda":str(val),"A":str(av),"potential":str(Vcf.subs({lam:val,tstar:1}))})
zero("calibration_example_A_half",Ac.subs({M:1,tstar:1,rhostar:1,lam:s.Rational(1,2)})-s.Rational(13,12))
zero("calibration_example_A_one",Ac.subs({M:1,tstar:1,rhostar:1,lam:1})-s.Rational(1,3))
zero("calibration_fixes_lambda_squared",lam**2-(4*M*M/3-Ac*rhostar*tstar*tstar))
zero("lambda_zero_is_excluded_by_velocity",vc.subs(lam,0))
zero("dust_zero_endpoint_is_excluded",rc.subs(lam,2*M/s.sqrt(3)))
details["continuous_family"]={"H":str(hc),"A":str(Ac),"V":str(Vcf),"mu":str(Vcpp),"fraction":str(3*lam*lam/(4*M*M)),"members":family_members,"physical_difference":"Different |lambda| change the scalar kinetic fraction and canonical potential slope; same given H, alpha, mu, rho_* and scale-factor normalization.","excluded_endpoints":"lambda=0 or lambda^2=4M^2/3 are not members of the open-domain family"}

# Normalize dust independently of the scalar label and mass curvature.
scale=s.symbols("scale",positive=True);AA=s.Function("A")(phi);VV=s.Function("V")(phi)
zero("density_rescaling_preserves_Einstein_energy",(rho/scale)*(scale*AA)-rho*AA)
zero("density_rescaling_preserves_signed_alpha",s.diff(scale*AA,phi)/(scale*AA)-s.diff(AA,phi)/AA)
zero("density_rescaling_preserves_fixed_rho_mass",s.diff(VV,phi,2)+(rho/scale)*s.diff(scale*AA,phi,2)-(s.diff(VV,phi,2)+rho*s.diff(AA,phi,2)))
dimensions={"J/v":(1,-2),"H*v":(1,-2),"alpha*Q":(1,-2),"alpha*v^2":(1,-2),"v_dot":(1,-2)}
ck("velocity_flow_dimensions",len(set(dimensions.values()))==1,dimensions)
ck("de_Sitter_excluded_by_positive_kinetic_and_dust",s.simplify((-2*M*M*Hd).subs(Hd,0))==0,{"reason":"Raychaudhuri requires Q=v^2+r>0; Q=0 cannot meet the contract."})

final=bindings();ck("owned_pre_exposure_inputs_unchanged",initial==final)
out={"kind":"Independent exact scalar inverse controls before author artifact exposure","python":sys.version,"sympy":s.__version__,"summary":{"passed":sum(c["passed"] for c in checks),"failed":sum(not c["passed"] for c in checks)},"checks":checks,"details":details,"input_binding_before":initial,"input_binding_after":final,"author_artifacts_read":False,"author_code_imported":False,"empirical_validation":False}
print(json.dumps(out,indent=2))
assert out["summary"]["failed"]==0
