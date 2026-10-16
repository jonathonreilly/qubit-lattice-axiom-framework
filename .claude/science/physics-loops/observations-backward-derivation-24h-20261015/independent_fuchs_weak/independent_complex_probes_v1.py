"""Independent synthetic complex-window controls; no author code or raw data."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/FUCHS_RELATIVE_MOTION_AND_WEAK_INVERSE_v2.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/FUCHS_COMPLEX_PROBE_EXTENSION_v1.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/FUCHS_COMPLEX_PROBE_PLAN_v1.json",
]
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
from numpy.polynomial.legendre import leggauss
import sympy as s

ROOT=Path(__file__).resolve().parents[5]
EXPECTED=["87c88650707c10c204a106a86749a9fa42d037ee670e4d1093caa75895538d51","5fbb6ac65f01c4dc16b7cddd8dba6347581f1444b856de239dfe68698a4b73dd","1390d29fc696ebb41030159225d16e9fce5986780e78c4f5beb1ee44bb19feed"]
def binding():
    return {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
initial=binding();checks=[];details={}
def ck(name,passed,detail=None):
    checks.append({"name":name,"passed":bool(passed),"detail":detail})
    print(json.dumps({"progress":name,"passed":bool(passed)}),file=sys.stderr,flush=True)
def zero(name,expr):
    residual=s.simplify(expr);ck(name,residual==0,str(residual))
def near(name,actual,expected,rtol=2e-10,atol=1e-10):
    error=float(abs(actual-expected));scale=float(max(abs(actual),abs(expected)))
    ck(name,error<=atol+rtol*scale,{"absolute_error":error,"scale":scale,"rtol":rtol,"atol":atol})
ck("source_binding",list(initial.values())==EXPECTED)
t,kappa,t0=s.symbols("t kappa t0",real=True)
p=s.Function("p")(t);g=s.exp(-s.I*kappa*(t-t0));w=p*g
zero("first_derivative",s.diff(w,t)-(s.diff(p,t)-s.I*kappa*p)*g)
zero("second_derivative",s.diff(w,t,2)-(s.diff(p,t,2)-2*s.I*kappa*s.diff(p,t)-kappa**2*p)*g)
phase=s.Function("phase")(t);gp=s.exp(-s.I*phase)
zero("variable_phase_second_derivative",s.diff(p*gp,t,2)-(s.diff(p,t,2)-2*s.I*s.diff(phase,t)*s.diff(p,t)-s.diff(phase,t)**2*p-s.I*s.diff(phase,t,2)*p)*gp)
q=s.symbols("q",real=True);W=140*q**3*(1-q)**3;Wp=s.diff(W,q);Wpp=s.diff(Wp,q)
ck("complex_endpoint_conditions",all(expr.subs(q,e)==0 for expr in (W,Wp) for e in (0,1)))
zero("unit_window_mass",s.integrate(W,(q,0,1))-1)
zfun=s.Function("z")(t)
zero("bilinear_first_boundary",w*s.diff(zfun,t)+s.diff(w,t)*zfun-s.diff(w*zfun,t))
zero("bilinear_second_boundary",w*s.diff(zfun,t,2)-s.diff(w,t,2)*zfun-s.diff(w*s.diff(zfun,t)-s.diff(w,t)*zfun,t))

Omega=5;gamma=2;omega2=49;a=-1;nu=12/5;b=(3+2j)/7
z=1+2*s.I+(2-s.I)*t+(1+3*s.I)*t**2+(2+s.I)*t**3/5
op=lambda v:s.diff(v,t,2)+(gamma+2*s.I*Omega)*s.diff(v,t)+(omega2-Omega**2+s.I*gamma*Omega)*v
u=s.expand(op(z)/(2*s.I*Omega*((3+2*s.I)/7)))
znum=s.lambdify(t,z,"numpy");unum=s.lambdify(t,u,"numpy")
nodes,quad=leggauss(64);nodes=(nodes+1)/2;quad=quad/2
pv=s.lambdify(q,W,"numpy")(nodes);pd=s.lambdify(q,Wp,"numpy")(nodes);pdd=s.lambdify(q,Wpp,"numpy")(nodes)
lamplus=-1-5j+4*np.sqrt(3)*1j;lamminus=-1-5j-4*np.sqrt(3)*1j
def weights(k):
    g=np.exp(-1j*k*nodes)
    return (pv*g,(pd-1j*k*pv)*g,(pdd-2j*k*pd-k*k*pv)*g)
def moments(zv,uv,ww,wd,we):
    return (np.dot(quad,ww*zv),np.dot(quad,wd*zv),np.dot(quad,we*zv),np.dot(quad,ww*uv))
def residual(mom):
    c,d,e,uu=mom
    return -d-1j*e/(2*Omega)-a*(c+1j*d/Omega)-1j*nu*c-b*uu
def columns(mom):
    c,d,e,uu=mom
    return np.array([c+1j*d/Omega,1j*c,uu,1j*uu]),-d-1j*e/(2*Omega)
def svd_info(aa):
    norms=np.linalg.norm(aa,axis=0)
    normalized=np.divide(aa,norms,out=np.zeros_like(aa),where=norms!=0)
    raw=np.linalg.svd(aa,compute_uv=False);norm=np.linalg.svd(normalized,compute_uv=False)
    return {"raw":raw.tolist(),"column_normalized":norm.tolist(),"relative_rank_threshold":1e-10,"rank":int(sum(raw>raw[0]*1e-10))}
design=[];rhs=[];wrong_omit=[];wrong_sign=[];wrong_mixed=[];homogeneous=[]
for start in range(4):
    times=start+nodes;zv=znum(times);uv=unum(times)
    zh=zv+(2+1j)*np.exp(lamplus*times)+(-1+2j)*np.exp(lamminus*times)
    for k in (0,2,-1.5):
        ww,wd,we=weights(k);label=f"{start}_{k}"
        mm=moments(zv,uv,ww,wd,we)
        near("bilinear_weak_"+label,residual(mm),0)
        near("consistent_conjugation_"+label,residual(moments(zv,uv,ww.conj(),wd.conj(),we.conj())),0)
        homerr=abs(residual(moments(zh,uv,ww,wd,we)))
        near("unsubtracted_homogeneous_"+label,homerr,0)
        homogeneous.append(float(homerr))
        cols,rr=columns(mm);design.extend([cols.real,cols.imag]);rhs.extend([rr.real,rr.imag])
        if k:
            gg=np.exp(-1j*k*nodes)
            wrong_omit.append(float(abs(residual(moments(zv,uv,ww,pd*gg,pdd*gg)))))
            wrong_sign.append(float(abs(residual(moments(zv,uv,ww,(pd+1j*k*pv)*gg,(pdd+2j*k*pd-k*k*pv)*gg)))))
            c,d,e,uu=mm
            wrong_mixed.append(float(abs(residual((np.dot(quad,ww.conj()*zv),d,e,np.dot(quad,ww.conj()*uv))))))
aa=np.array(design);yy=np.array(rhs);sing=svd_info(aa)
ck("polynomial_rank_four",sing["rank"]==4,sing)
fit=np.linalg.lstsq(aa,yy,rcond=None)[0];target=np.array([a,nu,b.real,b.imag])
for j in range(4):near("coefficient_recovery_"+str(j),fit[j],target[j])
for name,values in (("missing_derivative_terms_detected",wrong_omit),("wrong_derivative_signs_detected",wrong_sign),("mixed_conjugation_detected",wrong_mixed)):
    ck(name,max(values)>1e-5,{"maximum_residual":max(values),"minimum_residual":min(values)})
details["polynomial"]={"singular_values":sing,"recovered_coefficients":fit.tolist(),"maximum_homogeneous_residual":max(homogeneous),"wrong_omit_residuals":wrong_omit,"wrong_sign_residuals":wrong_sign,"wrong_mixed_residuals":wrong_mixed}

# Exact monochromatic factorization applies to every complex compact probe.
sigma=s.Integer(2);A=2+s.I;fac=[(1+sigma/s.Integer(Omega))*A,s.I*A,1,s.I]
factor=s.Matrix([[s.re(x) for x in fac],[s.im(x) for x in fac]])
ck("monochromatic_exact_rank_two",factor.rank()==2 and len(factor.nullspace())==2)
mono=[];mono_moments=[]
for start in range(4):
    ut=np.exp(2j*(start+nodes));zt=(2+1j)*ut
    for k in (0,2,-1.5):
        ww,wd,we=weights(k);c,d,e,uu=moments(zt,ut,ww,wd,we)
        near(f"monochromatic_D_{start}_{k}",d,-2j*c)
        near(f"monochromatic_E_{start}_{k}",e,-4*c)
        if k==2:near(f"matched_probe_U_{start}",uu,np.exp(2j*start))
        cols=np.array([c+1j*d/Omega,1j*c,uu,1j*uu])
        mono.extend([cols.real,cols.imag]);mono_moments.append({"start":start,"kappa":k,"U_real":float(uu.real),"U_imag":float(uu.imag)})
msing=svd_info(np.array(mono));ck("monochromatic_complex_probe_rank_two",msing["rank"]==2,msing)
high=np.exp(40j*nodes)
unmatched=abs(np.dot(quad,pv*high));matched=abs(np.dot(quad,weights(40)[0]*high))
near("high_frequency_matched_probe_norm",matched,1)
ck("matched_probe_can_avoid_cancellation",unmatched<0.01 and matched>0.99,{"unmodulated_norm":float(unmatched),"matched_norm":float(matched),"ratio":float(unmatched/matched)})
details["monochromatic"]={"exact_factor_matrix":str(factor),"exact_nullspace":[[str(x) for x in v] for v in factor.nullspace()],"singular_values":msing,"moments":mono_moments}
final=binding();ck("sources_unchanged",initial==final)
out={"kind":"Independent complex-probe mathematics; entirely synthetic","python":sys.version,"numpy":np.__version__,"sympy":s.__version__,"source_binding":initial,"final_source_binding":final,"summary":{"passed":sum(r["passed"] for r in checks),"failed":sum(not r["passed"] for r in checks)},"checks":checks,"details":details,"raw_trace_access":False,"author_code_or_output_artifacts_read":False,"exposure_note":"Parent supplied progress counts and one quadrature residual after the independent proof/fixture freeze; no author code or output artifacts read.","empirical_validation":False}
print(json.dumps(out,indent=2))
assert not out["summary"]["failed"]
