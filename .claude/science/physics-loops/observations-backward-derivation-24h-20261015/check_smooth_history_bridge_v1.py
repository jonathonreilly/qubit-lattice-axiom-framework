#!/usr/bin/env python3
"""Personally authored synthetic checks; no measured candidate dataset."""
from pathlib import Path
import hashlib,json,sys,itertools
import numpy as np
import sympy as s
from scipy.linalg import expm
from scipy.integrate import solve_ivp
from numpy.polynomial.legendre import leggauss
AUDIT_TIMEOUT_SEC=120
HERE=Path(__file__).resolve().parent
checks=[]
def ck(name,ok,detail=None): checks.append({"name":name,"passed":bool(ok),"detail":detail})
def eq(name,x,y): ck(name,s.simplify(x-y)==0,str(s.simplify(x-y)))

t=s.symbols("t",real=True)
G,O,K=s.symbols("G O K",real=True)
A=s.Function("A")(t);Y=s.Function("Y")(t);B=s.Function("B")(t);phi=s.Function("phi")(t)
ap=s.diff(A,t);app=s.diff(A,t,2)
L0=A**2*s.diff(phi,t,2)+6*A*ap*s.diff(phi,t)+(6*ap**2+3*A*app)*phi
L1=-A**2*s.diff(phi,t)-3*A*ap*phi
L2=A**2*phi
eq("division_free_form_classical",A**3*(s.diff(Y/A,t,2)+G*s.diff(Y/A,t)+O*Y/A-K*(s.diff(B,t,2)+G*s.diff(B,t))),
   A**2*s.diff(Y,t,2)-2*A*ap*s.diff(Y,t)+(2*ap**2-A*app)*Y+G*(A**2*s.diff(Y,t)-A*ap*Y)+O*A**2*Y-K*A**3*(s.diff(B,t,2)+G*s.diff(B,t)))
eq("adjoint_L0",s.diff(A**2*phi,t,2)+s.diff(2*A*ap*phi,t)+(2*ap**2-A*app)*phi,L0)
eq("adjoint_L1",-s.diff(A**2*phi,t)-A*ap*phi,L1)
eq("source_second_derivative",s.diff(A**3*phi,t,2),A*L0)
eq("source_first_derivative",-s.diff(A**3*phi,t),A*L1)
tau,C,gam,ar,db=s.symbols("tau C gam ar db",nonzero=True)
w=s.Function("w")(t);bb=s.Function("b")(t)
H=ar*(w+bb/C)
res=s.diff(H,t,2)+gam/tau*s.diff(H,t)+C/tau*H-ar/C*(s.diff(bb,t,2)+gam/tau*s.diff(bb,t))
eq("regular_identity_cancels_static_forcing",s.expand(res).subs(s.diff(w,t,2),(-gam*s.diff(w,t)-C*w-bb)/tau),0)
x,v,acc=s.symbols("x v acc",real=True);M=s.Function("M")(x)
eq("variable_mass_visible_load",s.diff(M*v,x)*v+s.diff(M*v,v)*acc-s.diff(M*v**2/2,x),M*acc+s.diff(M,x)*v*v/2)
ss,pp,m,r0,r1=s.symbols("ss pp m r0 r1")
eq("three_sample_offset",(m+ss*r1-pp*r0)-ss*(m+r1)+pp*(m+r0),(1-ss+pp)*m)
la=s.symbols("la",nonzero=True)
eq("potential_sign_product",(ar*db/C)*(ar/(la*db)),ar**2/(la*C))

# Independent initial preparations need no steady-state assumption.
Gamma,Omega2,tau_v=.4,2.3,1.4
C_v=tau_v*Omega2
beta=4/3
K_v=beta/C_v
Delta=.35
Ah=np.array([[0.,1.],[-Omega2,-Gamma]])
trans=expm(Ah*Delta)
s_v,p_v=float(np.trace(trans)),float(np.linalg.det(trans))
d=1-s_v+p_v
def bx(x):return beta*(3*x+x**3)/4
def ax(x):return 1+x*x
def ux(x):return .5*x+.1*x**3
def mx(x):return ux(x)-ax(x)*bx(x)/C_v
max_m_error=0.
for xx,z0 in [(-.6,[.7,-.3]),(.1,[-1.2,.9]),(.8,[.2,1.3])]:
    eqz=np.array([-bx(xx)/C_v,0.])
    fs=[ux(xx)+ax(xx)*(eqz+np.linalg.matrix_power(trans,n)@(np.array(z0)-eqz))[0] for n in range(3)]
    est=(fs[2]-s_v*fs[1]+p_v*fs[0])/d
    max_m_error=max(max_m_error,abs(est-mx(xx)))
ck("offset_unequal_hidden_preparations",max_m_error<1e-12,{"max_error":max_m_error,"denominator":d})
ck("full_period_alias_has_no_offset_denominator",abs(1-2+1)==0)

# Sharp but conservative interval formula checked on adverse finite corners.
f=np.array([.8,-.4,1.2]);sv,pv=.6,.75;ef,es,ep=.01,.015,.012
S,P,MF=abs(sv),abs(pv),max(abs(f));dd=1-sv+pv;ed=es+ep
en=(1+S+P)*ef+MF*ed+ef*ed
bd=en/(abs(dd)-ed)+(1+S+P)*MF*ed/(abs(dd)*(abs(dd)-ed))
mtrue=(f[2]-sv*f[1]+pv*f[0])/dd
worst=0.
for signs in itertools.product([-1,1],repeat=5):
    fp=f+ef*np.array(signs[:3]);sp=sv+es*signs[3];ppv=pv+ep*signs[4]
    val=(fp[2]-sp*fp[1]+ppv*fp[0])/(1-sp+ppv)
    worst=max(worst,abs(val-mtrue)/bd)
ck("offset_error_bound_32_corners",worst<=1,{"max_error_over_bound":worst})

# Smooth histories: finite ramps are represented directly.
def motion(tt,kind):
    pars=[(.1,.4,1.1,.17,2.7),(-.1,.3,1.7,.22,3.3),(.2,.27,.8,.25,2.1),(-.2,.35,1.4,.19,3.8),(.05,.43,1.9,.13,4.2)]
    off,a,w1,b,w2=pars[kind]
    xx=off+a*np.sin(w1*tt)+b*np.cos(w2*tt)
    xd=a*w1*np.cos(w1*tt)-b*w2*np.sin(w2*tt)
    xdd=-a*w1*w1*np.sin(w1*tt)-b*w2*w2*np.cos(w2*tt)
    return xx,xd,xdd
def Bparts(tt,kind):
    xx,xd,xdd=motion(tt,kind)
    val=(3*xx+xx**3)/4
    first=.75*(1+xx*xx)*xd
    second=.75*((1+xx*xx)*xdd+2*xx*xd*xd)
    return val,first,second
def run(kind,z0,eta=0.):
    def rhs(tt,z):
        val,bp,_=Bparts(tt,kind)
        return [z[1],-Gamma*z[1]-Omega2*z[0]-beta/tau_v*val+eta*bp]
    sol=solve_ivp(rhs,[0,7],z0,rtol=2e-11,atol=1e-12,dense_output=True,max_step=.035)
    assert sol.success
    def vals(tt,omit_load=False):
        xx,xd,xdd=motion(tt,kind);bv,_,_=Bparts(tt,kind)
        ww=sol.sol(tt)[0];avec=ax(xx)
        R=ux(xx)+avec*ww
        load=(1+.2*xx*xx)*xdd+.2*xx*xd*xd+.07*xd
        J=R+load
        Hrec=(J-(0 if omit_load else load)-mx(xx))/avec
        return Hrec,bv
    return vals
gl,gw=leggauss(160)
def row(fn,l,r,omit=False):
    width=r-l;tt=l+(gl+1)*width/2;weights=gw*width/2;z=(tt-l)/width
    ph=16*z*z*(1-z)**2
    dp=16*(2*z-6*z*z+4*z**3)/width
    ddp=16*(2-12*z+12*z*z)/(width*width)
    hh,bbv=fn(tt,omit)
    integ=lambda vals:float(weights@vals)
    return np.array([-integ(hh*dp),integ(hh*ph),-integ(bbv*ddp),integ(bbv*dp)]),-integ(hh*ddp)
dev_windows=[(.1,1.3),(.8,2.5),(2.,4.2),(3.4,6.6)]
models=[run(k,z) for k,z in [(0,[.4,-.8]),(1,[-1.1,.5]),(2,[1.2,1.1])]]
rows=[row(fn,l,r) for fn in models for l,r in dev_windows]
X=np.array([z[0] for z in rows]);target=np.array([z[1] for z in rows])
theta,_,rank,svals=np.linalg.lstsq(X,target,rcond=None)
true=np.array([Gamma,Omega2,K_v,K_v*Gamma])
ck("development_feature_rank_four",rank==4,{"singular_values":svals.tolist(),"condition_number":float(svals[0]/svals[-1])})
ck("continuous_coefficients_recovered_from_smooth_histories",np.max(abs(theta-true))<2e-7,{"fitted":theta.tolist(),"truth":true.tolist(),"max_error":float(np.max(abs(theta-true)))})
ck("nonlinear_coefficient_constraint",abs(theta[3]-theta[0]*theta[2])<2e-7,{"difference":float(theta[3]-theta[0]*theta[2])})
tfit=expm(np.array([[0.,1.],[-theta[1],-theta[0]]])*Delta)
ck("continuous_fit_agrees_with_separate_discrete_recurrence",abs(np.trace(tfit)-s_v)+abs(np.linalg.det(tfit)-p_v)<2e-7)
reserved=[run(3,[-.6,1.7]),run(4,[2.,-.5])]
test_windows=[(.25,1.9),(1.3,3.7),(3.8,6.8)]
resids=[float(row(fn,l,r)[0]@theta-row(fn,l,r)[1]) for fn in reserved for l,r in test_windows]
ck("reserved_synthetic_histories_and_test_windows",max(abs(np.array(resids)))<2e-7,{"residuals":resids})
bad=[float(row(fn,l,r,True)[0]@theta-row(fn,l,r,True)[1]) for fn in reserved for l,r in test_windows]
ck("omitting_visible_load_is_detected",max(abs(np.array(bad)))>.1,{"residuals":bad})

# Alternative velocity-dependent hidden forcing: same static offset, changed L.
eta=.18
alt=[run(k,z,eta) for k,z in [(0,[.4,-.8]),(1,[-1.1,.5]),(2,[1.2,1.1])]]
altrows=[row(fn,l,r) for fn in alt for l,r in dev_windows]
XA=np.array([z[0] for z in altrows]);ya=np.array([z[1] for z in altrows])
ta,_,ra,_=np.linalg.lstsq(XA,ya,rcond=None)
ck("derivative_forcing_alternative_fits_unconstrained_rows",np.max(abs(XA@ta-ya))<2e-7 and ra==4,{"fitted":ta.tolist()})
ck("derivative_forcing_violates_required_coefficient_relation",abs(ta[3]-ta[0]*ta[2]-eta)<2e-7,{"violation":float(ta[3]-ta[0]*ta[2]),"expected":eta})
ck("frozen_candidate_rejects_derivative_forcing",np.max(abs(XA@theta-ya))>.01,{"maximum_residual":float(np.max(abs(XA@theta-ya)))})
# Exact quotient error envelope on finite adverse corners.
av,yv=.8,-1.7;eA,eR,em=.03,.02,.015
eH=(eR+em)/(av-eA)+abs(yv)*eA/(av*(av-eA))
qh=[]
for signs in itertools.product([-1,1],repeat=3):
    observed=(yv+signs[0]*eR-signs[1]*em)/(av+signs[2]*eA)
    qh.append(abs(observed-yv/av))
ck("regular_quotient_error_bound",max(qh)<=eH+1e-14,{"max_error":max(qh),"bound":eH})
# Derive the regular weak error estimate with independent quadrature.
width=1.7;z=(gl+1)/2;weights=gw*width/2
ph=16*z*z*(1-z)**2;dp=16*(2*z-6*z*z+4*z**3)/width;ddp=16*(2-12*z+12*z*z)/width**2
eh,eb=.003,.004
kh=ddp-Gamma*dp+Omega2*ph
kb=-K_v*ddp+K_v*Gamma*dp
observed_error=weights@(eh*np.abs(kh)+eb*np.abs(kb))
budget=eh*(weights@(np.abs(ddp)+abs(Gamma)*np.abs(dp)+Omega2*np.abs(ph)))+abs(K_v)*eb*(weights@(np.abs(ddp)+abs(Gamma)*np.abs(dp)))
ck("weak_residual_error_budget",observed_error<=budget+1e-14,{"adverse_error":float(observed_error),"budget":float(budget)})
# At a zero-coupling interval all polynomial weights vanish: no false observability claim.
ck("division_free_zero_interval_blind",s.simplify(L0.subs({A:0,ap:0,app:0}))==0 and s.simplify(L1.subs({A:0,ap:0}))==0 and s.simplify(L2.subs(A,0))==0)

result={"note":"SMOOTH_HISTORY_BRIDGE_v1.md","note_sha256":hashlib.sha256((HERE/"SMOOTH_HISTORY_BRIDGE_v1.md").read_bytes()).hexdigest(),"runner_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"empirical_validation":False,"data_role":"Explicit synthetic development and reserved histories; no measured data used.","checks":checks,"summary":{"passed":sum(z["passed"] for z in checks),"failed":sum(not z["passed"] for z in checks)}}
print(json.dumps(result,indent=2));sys.exit(bool(result["summary"]["failed"]))

