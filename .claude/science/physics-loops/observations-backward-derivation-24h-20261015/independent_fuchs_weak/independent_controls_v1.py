"""Synthetic-only independent mechanical and compact-window controls.

No raw data, source receipt, author runner or author output is read.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/FUCHS_RELATIVE_MOTION_AND_WEAK_INVERSE_v1.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/FUCHS_WEAK_DEVELOPMENT_PLAN_v1.json",
]
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
from numpy.polynomial.legendre import leggauss
import sympy as s

ROOT=Path(__file__).resolve().parents[5]
EXPECTED=["a9c1fa8fd781175e976be1346a5e92030c388fec8b0b410286ca377650ecef20","851e5314205a6aee01e365328eef23e4cdfe464787299b0ea19d4efcf56db4d7"]
def binding():
    return {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
initial=binding();rows=[];details={}
def ck(name,passed,detail=None):
    rows.append({"name":name,"passed":bool(passed),"detail":detail})
    print(json.dumps({"progress":name,"passed":bool(passed)}),file=sys.stderr,flush=True)
def zero(name,expr):
    residual=s.simplify(expr);ck(name,residual==0,str(residual))
def near(name,actual,expected,rtol=2e-10,atol=1e-11):
    error=float(abs(actual-expected));scale=float(max(abs(actual),abs(expected)))
    ck(name,error<=atol+rtol*scale,{"absolute_error":error,"scale":scale,"rtol":rtol,"atol":atol})
ck("initial_source_binding",list(initial.values())==EXPECTED)

# Eliminate the support using the total momentum equation; no author solve.
mt,mp,om=s.symbols("mt mp om",positive=True)
Z,P,gt,gp,fp,f=s.symbols("Z P gt gp fp f")
D=Z-mt*om**2;Fs=mp*gp+fp
det=D*P-mt*om**2*Z
total_det=D*(P-mt*om**2)-mt**2*om**4
total_num=(P-mt*om**2)*(mt*gt+f)+mt*om**2*(mt*gt+Fs)
target_num=mt*P*gt+mt*om**2*Fs+(P-mt*om**2)*f
zero("total_momentum_determinant",total_det-det)
zero("total_momentum_source_and_internal_force",total_num-target_num)
mat=s.Matrix([[D,-mt*om**2],[-Z,P]])
sol=mat.inv()*s.Matrix([mt*gt+f,Fs-f])
zero("matrix_and_total_momentum_solve",sol[0]-target_num/det)
Hinternal=s.diff(sol[0],f)
zero("internal_calibration_transfer",Hinternal-(P-mt*om**2)/det)
external=mat.inv()*s.Matrix([mt*gt+f,Fs])
zero("external_reaction_calibration_transfer",s.diff(external[0],f)-P/det)
zero("internal_force_equivalent",sol[0].subs(f,0)/Hinternal-mt*(P*gt+om**2*Fs)/(P-mt*om**2))
zero("free_uniform_acceleration_particular",target_num.subs({P:-mp*om**2,gp:gt,fp:0,f:0}))
anti={mt:1,mp:3,om:1,Z:2+s.I/5,P:1}
ck("nonsingular_mechanics_zero_internal_calibration",s.simplify(det.subs(anti))==-1 and s.simplify(Hinternal.subs(anti))==0)
zero("free_support_calibration_reduced_mass",(mt*(P*gt+om**2*mp*gp)/(P-mt*om**2)).subs(P,-mp*om**2)-mt*(gt-gp)/(1+mt/mp))
eps=s.Rational(1,1000);zz=1+s.I*eps;dd=s.I*eps
fixed=1/dd;moving=1/(dd+eps*zz)
rel=float(s.N(s.Abs(moving-fixed)/s.Abs(fixed),20));calibrated=1/(1+eps)
ck("small_mass_ratio_near_pole_response",rel>.5,{"mass_ratio":str(eps),"uncalibrated_relative_change":rel,"internal_calibrated_ratio":str(calibrated)})
details["mechanical_scope"]={"antiresonance_Delta":"-1","antiresonance_internal_force_transfer":"0","source_run_equation4_condition":"Calibration force off; otherwise solving for g_t includes -f/m.","support_ambiguity":"An arbitrary acceleration reconstruction does not solve a separately established support model."}

# Exact demodulation and adjoint, including boundary bilinear forms.
t=s.symbols("t",real=True);Om=s.symbols("Om",positive=True)
gamma,ww=s.symbols("gamma omega0_squared",real=True)
zfun=s.Function("z")(t);wfun=s.Function("w")(t)
qc=zfun*s.exp(s.I*Om*t)
demod=s.diff(qc,t,2)+gamma*s.diff(qc,t)+ww*qc
expected=s.diff(zfun,t,2)+(gamma+2*s.I*Om)*s.diff(zfun,t)+(ww-Om**2+s.I*gamma*Om)*zfun
zero("constant_carrier_exact_demodulation",demod/s.exp(s.I*Om*t)-expected)
phase=s.Function("phase")(t);qvar=zfun*s.exp(s.I*phase)
variable=s.diff(qvar,t,2)+gamma*s.diff(qvar,t)+ww*qvar
vexpected=s.diff(zfun,t,2)+(gamma+2*s.I*s.diff(phase,t))*s.diff(zfun,t)+(ww-s.diff(phase,t)**2+s.I*gamma*s.diff(phase,t)+s.I*s.diff(phase,t,2))*zfun
zero("variable_carrier_extra_derivative",variable/s.exp(s.I*phase)-vexpected)
zero("first_integration_by_parts",wfun*s.diff(zfun,t)+s.diff(wfun,t)*zfun-s.diff(wfun*zfun,t))
zero("second_boundary_bilinear_form",wfun*s.diff(zfun,t,2)-s.diff(wfun,t,2)*zfun-s.diff(wfun*s.diff(zfun,t)-s.diff(wfun,t)*zfun,t))
C,Dm,E,U,b=s.symbols("C D E U b")
a=-gamma/2;nu=(ww-Om**2)/(2*Om)
R=-Dm-s.I*E/(2*Om);B=C+s.I*Dm/Om
integrated=E-(gamma+2*s.I*Om)*Dm+(ww-Om**2+s.I*gamma*Om)*C-2*s.I*Om*b*U
zero("exact_compact_window_identity",integrated-2*s.I*Om*(R-a*B-s.I*nu*C-b*U))
ss=s.symbols("s",real=True)
W=140*ss**3*(1-ss)**3;Wp=s.diff(W,ss);Wpp=s.diff(Wp,ss)
ck("compact_window_boundary_conditions",all(expr.subs(ss,end)==0 for expr in (W,Wp) for end in (0,1)))
zero("compact_window_unit_integral",s.integrate(W,(ss,0,1))-1)

# Exact polynomial manufactured input, then exact finite-row rank/solution.
Omega=s.Integer(5);gam=s.Integer(2);omega2=s.Integer(49)
aval=-1;nval=s.Rational(12,5);bval=(3+2*s.I)/7
z=1+2*s.I+(2-s.I)*t+(1+3*s.I)*t**2+(2+s.I)*t**3/5
def operator(expr):
    return s.diff(expr,t,2)+(gam+2*s.I*Omega)*s.diff(expr,t)+(omega2-Omega**2+s.I*gam*Omega)*expr
u=s.expand(operator(z)/(2*s.I*Omega*bval))
def moment(expr,weight,start):
    return s.expand(s.integrate(s.expand(weight*expr.subs(t,ss+start)),(ss,0,1)))
design=[];rhs=[];moments=[];first_order=[]
for start in range(4):
    cc=moment(z,W,start);ddm=moment(z,Wp,start);ee=moment(z,Wpp,start);uu=moment(u,W,start)
    rr=-ddm-s.I*ee/(2*Omega);bb=cc+s.I*ddm/Omega
    zero(f"manufactured_exact_window_{start}",rr-aval*bb-s.I*nval*cc-bval*uu)
    omitted=s.simplify(-ddm-aval*cc-s.I*nval*cc-bval*uu)
    zero(f"first_order_defect_identity_{start}",omitted-s.I*ee/(2*Omega)-s.I*aval*ddm/Omega)
    first_order.append(str(omitted))
    cols=[bb,s.I*cc,uu,s.I*uu]
    design.extend([[s.re(x).expand() for x in cols],[s.im(x).expand() for x in cols]])
    rhs.extend([s.re(rr).expand(),s.im(rr).expand()])
    moments.append({"start":start,"C":str(cc),"D":str(ddm),"E":str(ee),"U":str(uu)})
AA=s.Matrix(design);yy=s.Matrix(rhs)
rank=AA.rank();ck("manufactured_real_rank_four",rank==4)
solution=(AA.T*AA).inv()*AA.T*yy
target=s.Matrix([aval,nval,s.re(bval),s.im(bval)])
ck("manufactured_unique_exact_coefficients",all(s.simplify(x)==0 for x in solution-target),[str(v) for v in solution])
ck("first_order_is_not_exact",all(s.sympify(x)!=0 for x in first_order),first_order)
bad=yy+s.eye(8)[:,0];fitbad=(AA.T*AA).inv()*AA.T*bad;resbad=bad-AA*fitbad
ck("full_rank_does_not_guarantee_consistency",resbad!=s.zeros(8,1) and AA.T*resbad==s.zeros(4,1))
def singular_values(array):
    array=np.asarray(array,dtype=float);norms=np.linalg.norm(array,axis=0)
    normalized=np.divide(array,norms,out=np.zeros_like(array),where=norms!=0)
    return {"raw":np.linalg.svd(array,compute_uv=False).tolist(),"column_normalized":np.linalg.svd(normalized,compute_uv=False).tolist(),"numeric_rank":int(np.linalg.matrix_rank(array)),"column_norms":norms.tolist()}
details["polynomial_manufactured"]={"z":str(z),"u":str(u),"moments":moments,"rank":rank,"coefficients":[str(x) for x in solution],"first_order_residuals":first_order,"singular_values":singular_values(np.array(AA,dtype=float))}

# Homogeneous amplitudes stay in the observed signal, with unchanged input.
lp=-1-5*s.I+4*s.sqrt(3)*s.I;lm=-1-5*s.I-4*s.sqrt(3)*s.I
for label,ll in (("plus",lp),("minus",lm)):
    zero("homogeneous_characteristic_"+label,ll**2+(gam+2*s.I*Omega)*ll+omega2-Omega**2+s.I*gam*Omega)
nodes,weights=leggauss(64);nodes=(nodes+1)/2;weights=weights/2
wv=s.lambdify(ss,W,"numpy")(nodes);wd=s.lambdify(ss,Wp,"numpy")(nodes);we=s.lambdify(ss,Wpp,"numpy")(nodes)
znum=s.lambdify(t,z,"numpy");unum=s.lambdify(t,u,"numpy")
lpn=complex(s.N(lp));lmn=complex(s.N(lm));bn=complex(bval)
hom=[]
for index,(hp,hm) in enumerate(((0j,0j),(2+1j,-1+2j),(100+30j,-80+20j))):
    errs=[]
    for start in range(4):
        times=start+nodes
        observed=znum(times)+hp*np.exp(lpn*times)+hm*np.exp(lmn*times)
        cc=np.sum(weights*wv*observed);ddm=np.sum(weights*wd*observed);ee=np.sum(weights*we*observed)
        uu=np.sum(weights*wv*unum(times));rr=-ddm-1j*ee/10;bb=cc+1j*ddm/5
        predicted=-bb+1j*float(nval)*cc+bn*uu
        near(f"unsubtracted_homogeneous_window_{index}_{start}",rr,predicted)
        errs.append(float(abs(rr-predicted)))
    hom.append({"amplitude_plus":str(hp),"amplitude_minus":str(hm),"maximum_weak_residual":max(errs)})
details["homogeneous_amplitude_controls"]=hom

# Monochromatic algebra fixes the real rank at two, not four.
sigma=s.Integer(2);ratio=2+s.I
factors=[(1+sigma/Omega)*ratio,s.I*ratio,1,s.I]
factor_matrix=s.Matrix([[s.re(x) for x in factors],[s.im(x) for x in factors]])
ck("monochromatic_exact_rank_two",factor_matrix.rank()==2 and len(factor_matrix.nullspace())==2)
mono=[]
for start in range(4):
    ut=np.exp(2j*(start+nodes));zt=complex(ratio)*ut
    cc=np.sum(weights*wv*zt);ddm=np.sum(weights*wd*zt);ee=np.sum(weights*we*zt);uu=np.sum(weights*wv*ut)
    near(f"monochromatic_first_moment_{start}",ddm,-2j*cc)
    near(f"monochromatic_second_moment_{start}",ee,-4*cc)
    columns=[complex(x)*uu for x in factors]
    mono.extend([[x.real for x in columns],[x.imag for x in columns]])
mono_info=singular_values(mono);ck("monochromatic_numeric_rank_two",mono_info["numeric_rank"]==2)
details["monochromatic_rank"]={"exact_rank":2,"exact_nullspace":[[str(x) for x in v] for v in factor_matrix.nullspace()],"singular_values":mono_info}

# Full-history common filtering versus differential delay and filter state.
delay=s.Rational(1,3)
hz=s.expand((z+z.subs(t,t-delay))/2);hu=s.expand((u+u.subs(t,t-delay))/2)
zero("common_filter_commutes_exactly",operator(hz)-2*s.I*Omega*bval*hu)
ratio1=s.exp(-s.I*s.pi/4);ratio3=s.exp(-3*s.I*s.pi/4)
zero("different_filter_frequency_ratio_separation",s.expand_complex((ratio1-ratio3)*s.conjugate(ratio1-ratio3))-2)
ck("one_b_cannot_absorb_two_delay_ratios",s.simplify(ratio1-ratio3)!=0)
filter_lambda=s.Rational(-5,2)
filter_polynomial=s.simplify(filter_lambda**2+(gam+2*s.I*Omega)*filter_lambda+omega2-Omega**2+s.I*gam*Omega)
state=np.exp(float(filter_lambda)*nodes)
cc=np.sum(weights*wv*state);ddm=np.sum(weights*wd*state);ee=np.sum(weights*we*state)
state_residual=-ddm-1j*ee/10+cc+1j*ddm/5-1j*float(nval)*cc
expected_state=complex(filter_polynomial/(2*s.I*Omega))*cc
near("filter_state_weak_residual",state_residual,expected_state)
ck("compact_window_does_not_remove_filter_state",abs(state_residual)>1e-2,{"residual_real":float(state_residual.real),"residual_imag":float(state_residual.imag),"filter_pole_polynomial":str(filter_polynomial)})
details["filter_scope"]={"common_filter":"Full-history two-tap average","different_filter_test":"Distinct delays give unequal input/output ratios at two frequencies; fixed physical oscillator coefficients held fixed","exception":"Proportional filters may be absorbed into b","instrument_state":"Added exp(-5t/2) is not an oscillator homogeneous mode and has nonzero weak residual"}
final=binding();ck("sources_unchanged",initial==final)
out={"kind":"Independent synthetic mechanical and weak-inverse controls; no empirical or audit status","python":sys.version,"sympy":s.__version__,"numpy":np.__version__,"source_binding":initial,"final_source_binding":final,"summary":{"passed":sum(x["passed"] for x in rows),"failed":sum(not x["passed"] for x in rows)},"checks":rows,"details":details,"raw_trace_access":False,"author_runner_or_results_access":False,"empirical_validation":False}
print(json.dumps(out,indent=2))
assert out["summary"]["failed"]==0
