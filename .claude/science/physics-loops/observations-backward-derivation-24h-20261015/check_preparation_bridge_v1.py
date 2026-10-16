"""Observed preparation coordinates remove initial-state terms in a supplied class."""
AUDIT_TIMEOUT_SEC = 120
from pathlib import Path
import hashlib, json, sys
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp
ROOT = Path(__file__).resolve().parent
rows=[]; details={}
def check(name, passed, detail=None):
    rows.append(dict(name=name,passed=bool(passed),detail=detail))

# Direct variation with independent jets, before numeric specialization.
x,v,a,w,h,b=s.symbols("x v a w h b", real=True)
names=["tau","C","B","U","M","k","d","nu","gamma"]
F={n:s.Function(n)(x) for n in names}
tau,C,B,U,M,k,d,nu,gamma=[F[n] for n in names]
T=M*v*v/2+k*v*h+tau*h*h/2
V=U+B*w+C*w*w/2
D=d*v*v/2+nu*v*h+gamma*h*h/2
Dt=lambda z:s.diff(z,x)*v+s.diff(z,v)*a+s.diff(z,w)*h+s.diff(z,h)*b
EW=Dt(s.diff(T,h))-s.diff(T,w)+s.diff(V,w)+s.diff(D,h)
EX=Dt(s.diff(T,v))-s.diff(T,x)+s.diff(V,x)+s.diff(D,v)
expectedW=tau*b+(s.diff(tau,x)*v+gamma)*h+C*w+k*a+s.diff(k,x)*v*v+B+nu*v
expectedX=M*a+s.diff(M,x)*v*v/2+k*b-s.diff(tau,x)*h*h/2+s.diff(V,x)+d*v+nu*h
check("full hidden equation from variation",s.simplify(EW-expectedW)==0)
check("full visible equation from variation",s.simplify(EX-expectedX)==0)
zz,zd,zdd,wzero,xi,xid,xidd,eta,etad,etadd=s.symbols("z zd zdd wzero xi xid xidd eta etad etadd",real=True)
clamp={v:0,a:0,w:wzero+zz,h:zd,b:zdd}
def vary(eq):
    return s.expand(sum(s.diff(eq,j)*dj for j,dj in [(x,xi),(v,xid),(a,xidd),(w,eta),(h,etad),(b,etadd)]).subs(clamp))
G=s.diff(B,x)+s.diff(C,x)*wzero
expectedVW=tau*etadd+gamma*etad+C*eta+k*xidd+(nu+s.diff(tau,x)*zd)*xid+(G+s.diff(C,x)*zz+s.diff(gamma,x)*zd+s.diff(tau,x)*zdd)*xi
expectedVX=M*xidd+d*xid+(s.diff(V,x,2).subs(w,wzero+zz)-s.diff(tau,x,2)*zd*zd/2+s.diff(nu,x)*zd+s.diff(k,x)*zdd)*xi+(G+s.diff(C,x)*zz)*eta+(nu-s.diff(tau,x)*zd)*etad+k*etadd
check("nonstationary hidden tangent",s.simplify(vary(EW)-expectedVW)==0)
check("nonstationary visible tangent",s.simplify(vary(EX)-expectedVX)==0)
p,q=s.symbols("p q",real=True)
wr,wp,wq,hr,hp,hq=s.symbols("wr wp wq hr hp hq")
b_eliminated=s.solve(EW,b)[0]
hidden_force=s.expand(EX.subs(b,b_eliminated).subs({w:wr+wp*p+wq*q,h:hr+hp*p+hq*q}))
check("full force degree at most two in arbitrary initial coordinates",s.Poly(hidden_force,p,q).total_degree()<=2)

# The model below is fixed in the plan, not estimated by record synthesis.
tau_expr=1.3*s.exp(.22*x+.05*x*x)
O_expr=3.2+.3*x+.1*x*x
gamma_expr=tau_expr*(.55+.05*s.sin(x))
w0_expr=.2+.35*x+.08*s.sin(1.2*x)
C_expr=tau_expr*O_expr
E_expr=.35*x*x+.04*x**4
models=dict(tau=tau_expr,C=C_expr,B=-C_expr*w0_expr,U=E_expr+C_expr*w0_expr*w0_expr/2,
            M=2.1+.2*s.cos(x),k=.16+.04*x,d=.55+.06*x*x,nu=.12+.02*s.cos(x),gamma=gamma_expr)
keys=[n+str(j) for n in names for j in range(3)]
parfun=s.lambdify(x,[s.diff(models[n],x,j) for n in names for j in range(3)],"numpy")
def pars(xx):return dict(zip(keys,np.asarray(parfun(xx),dtype=float)))
def pole(xx):
    z=pars(xx);ga=z["gamma0"]/z["tau0"];o=z["C0"]/z["tau0"]
    return complex(-ga/2,np.sqrt(o-ga*ga/4))
def drive(t,x0,A,freq):
    co=np.cos(freq*t);si=np.sin(freq*t)
    return x0+A*(1-co)**2,2*A*freq*(1-co)*si,2*A*freq**2*(si*si+(1-co)*co)
def acceleration(z,xd,xdd,ww,wd):
    return (-(z["tau1"]*xd+z["gamma0"])*wd-z["C0"]*ww-z["k0"]*xdd-z["k1"]*xd*xd-z["B0"]-z["nu0"]*xd)/z["tau0"]
def force(z,xd,xdd,ww,wd,wdd):
    return z["M0"]*xdd+.5*z["M1"]*xd*xd+z["k0"]*wdd-.5*z["tau1"]*wd*wd+z["U1"]+z["B1"]*ww+.5*z["C1"]*ww*ww+z["d0"]*xd+z["nu0"]*wd
TS=np.linspace(0,5.2,261)
preps=np.array([.2-.1j,-.1+.23j,.31+.18j,-.25-.27j,.08+.3j,.4-.19j])
reserved=np.array([-.17+.12j,.27-.31j,.05+.08j])
def prefix(x0,c):
    z=pars(x0);la=pole(x0);tt=np.linspace(-3,0,101);w0=-z["B0"]/z["C0"]
    zz=2*np.real(c*np.exp(la*tt));zd=2*np.real(la*c*np.exp(la*tt));zdd=2*np.real(la*la*c*np.exp(la*tt))
    rr=np.array([force(z,0,0,ww,wd,wdd) for ww,wd,wdd in zip(w0+zz,zd,zdd)])
    return tt,rr,la
def fit_prefix(tt,rr,la):
    ga=-2*la.real;om=la.imag
    H=np.column_stack([np.ones_like(tt),np.exp(-ga*tt/2)*np.cos(om*tt),np.exp(-ga*tt/2)*np.sin(om*tt),np.exp(-ga*tt),np.exp(-ga*tt)*np.cos(2*om*tt),np.exp(-ga*tt)*np.sin(2*om*tt)])
    cf=np.linalg.lstsq(H,rr,rcond=None)[0]
    return (cf[1]-1j*cf[2])/2,H,float(np.max(abs(H@cf-rr)))
def simulate(x0,A,freq,c,cubic=0):
    z0=pars(x0);la=pole(x0);y0=[-z0["B0"]/z0["C0"]+2*c.real,2*(la*c).real]
    def fun(t,y):
        xx,xd,xdd=drive(t,x0,A,freq)
        return [y[1],acceleration(pars(xx),xd,xdd,y[0],y[1])]
    sol=solve_ivp(fun,(0,TS[-1]),y0,method="DOP853",t_eval=TS,rtol=2e-11,atol=2e-12)
    assert sol.success,sol.message
    out=[]
    for tt,ww,wd in zip(TS,*sol.y):
        xx,xd,xdd=drive(tt,x0,A,freq);z=pars(xx)
        out.append(force(z,xd,xdd,ww,wd,acceleration(z,xd,xdd,ww,wd))+cubic*xd*(ww+z["B0"]/z["C0"])**3)
    return np.array(out)
def design(ff):
    aa=ff.real;bb=ff.imag
    return np.array([np.ones_like(aa),aa,bb,aa*aa,aa*bb,bb*bb])
E0=np.array([1.,0,0,0,0,0])
def measured_coordinates(x0,cs):return np.array([fit_prefix(*prefix(x0,c))[0] for c in cs])
def synthesize(x0,A,freq,cs):
    ff=measured_coordinates(x0,cs)
    qq=design(ff);weights=np.linalg.solve(qq,E0)
    records=np.array([simulate(x0,A,freq,c) for c in cs])
    return weights@records,ff,weights,records

for xx in np.linspace(-1,1,13):
    z=pars(xx)
    check("positive class at "+str(float(xx)),z["tau0"]>0 and z["M0"]*z["tau0"]-z["k0"]**2>0 and z["d0"]*z["gamma0"]-z["nu0"]**2>0 and pole(xx).imag>0)
histories=[(-.2,.12,.85),(.3,-.09,1.1),(.65,-.14,.7)]
hd=[]
for ih,(x0,amp,freq) in enumerate(histories):
    predicted,ff,weights,records=synthesize(x0,amp,freq,preps)
    truth=simulate(x0,amp,freq,0j)
    err=float(np.max(abs(predicted-truth)))
    check("rest-start force synthesized history"+str(ih),err<2e-8,err)
    check("all six preparations nonzero history"+str(ih),np.min(abs(ff))>1e-3)
    check("moment design certificate history"+str(ih),np.linalg.norm(design(ff)@weights-E0)<1e-10)
    check("signed weights necessary realized history"+str(ih),np.min(weights)<0)
    # Fitted coefficient histories and new prefix coordinates only predict reserves.
    alpha=np.linalg.solve(design(ff).T,records)
    fd=measured_coordinates(x0,reserved)
    held=np.array([simulate(x0,amp,freq,c) for c in reserved])
    held_error=float(np.max(abs(design(fd).T@alpha-held)))
    check("reserved preparation force prediction history"+str(ih),held_error<3e-8,held_error)
    bad=np.array([simulate(x0,amp,freq,c,cubic=.04) for c in preps])
    badalpha=np.linalg.solve(design(ff).T,bad)
    badheld=np.array([simulate(x0,amp,freq,c,cubic=.04) for c in reserved])
    fitted_error=float(np.max(abs(design(ff).T@badalpha-bad)))
    held_bad=float(np.max(abs(design(fd).T@badalpha-badheld)))
    check("six-point cubic alternative interpolates history"+str(ih),fitted_error<1e-10,fitted_error)
    check("reserved prep rejects constructed cubic output history"+str(ih),held_bad>1e-5,held_bad)
    hd.append(dict(role="development" if ih==0 else "reserved synthetic drive",x0=x0,amp=amp,frequency=freq,max_rest_error=err,max_reserved_error=held_error,altered_output_reserved_error=held_bad,weights=weights.tolist(),design_condition=float(np.linalg.cond(design(ff))),prefix_coordinates=[[z.real,z.imag] for z in ff]))
    if ih==0: dev=(ff,weights,records,truth)
details["histories"]=hd

# Exact design limitations and a lower-rank feasible example.
theta=np.arange(6)*2*np.pi/6
circ=np.exp(1j*theta);Qc=design(circ);wc=np.linalg.lstsq(Qc,E0,rcond=None)[0]
check("fixed amplitude has incompatible moment equations",np.linalg.norm(Qc@wc-E0)>.1,float(np.linalg.norm(Qc@wc-E0)))
dual=np.array([-1.,0,0,1,0,1])
check("fixed-amplitude dual polynomial witness",np.max(abs(dual@Qc))<1e-12 and dual@E0==-1)
line=np.array([1.+0j,2.+0j,3.+0j]);wl=np.array([3.,-3.,1.])
check("three collinear amplitudes suffice",np.max(abs(design(line)@wl-E0))<1e-12)
check("quadratic positive-weight contradiction",np.min(abs(circ))>.99)
details["circle_minimum_moment_residual"]=float(np.linalg.norm(Qc@wc-E0))

# General-k tangent response; no reset is used in the synthesized comparison.
def tangent(x0,freq,c,omit=None):
    z=pars(x0);la=pole(x0);w0=-z["B0"]/z["C0"]
    G=z["B1"]+z["C1"]*w0
    def calc(t,y):
        _,xid,xidd=drive(t,0.,1.,freq);xi=drive(t,0.,1.,freq)[0]
        zz=2*(c*np.exp(la*t)).real;zd=2*(la*c*np.exp(la*t)).real;zdd=2*(la*la*c*np.exp(la*t)).real
        inp=z["k0"]*xidd+(z["nu0"]+z["tau1"]*zd)*xid+(G+z["C1"]*zz+z["gamma1"]*zd+z["tau1"]*zdd)*xi
        if omit=="tau_input":inp-=z["tau1"]*zd*xid
        if omit=="gamma_gradient":inp-=z["gamma1"]*zd*xi
        etd=(-z["gamma0"]*y[1]-z["C0"]*y[0]-inp)/z["tau0"]
        vv=z["U2"]+z["B2"]*(w0+zz)+.5*z["C2"]*(w0+zz)**2
        out=z["M0"]*xidd+z["d0"]*xid+(vv-.5*z["tau2"]*zd*zd+z["nu1"]*zd+z["k1"]*zdd)*xi+(G+z["C1"]*zz)*y[0]+(z["nu0"]-z["tau1"]*zd)*y[1]+z["k0"]*etd
        if omit=="kinetic_gradient_output":out-=z["k1"]*zdd*xi
        return etd,out
    sol=solve_ivp(lambda t,y:[y[1],calc(t,y)[0]],(0,TS[-1]),[0.,0.],method="DOP853",t_eval=TS,rtol=2e-11,atol=2e-12)
    assert sol.success
    return np.array([calc(t,y)[1] for t,y in zip(TS,sol.y.T)])
x0=.15;freq=.9;cc=.25-.18j
ex=1e-4
fd=(simulate(x0,ex,freq,cc)-simulate(x0,-ex,freq,cc))/(2*ex)
tv=tangent(x0,freq,cc);rest=tangent(x0,freq,0j)
err=float(np.max(abs(fd-tv)))
check("nonstationary tangent matches direct finite drive derivative",err<2e-6,err)
check("baseline subtraction does not give rest response",np.max(abs(fd-rest))>1e-3,float(np.max(abs(fd-rest))))
for om in ["tau_input","gamma_gradient","kinetic_gradient_output"]:
    er=float(np.max(abs(tangent(x0,freq,cc,om)-fd)))
    check("omission rejected "+om,er>1e-4,er)
central=[]
for eps in [.04,.02,.01,.005]:
    yp,_,_,_=synthesize(x0,eps,freq,preps)
    ym,_,_,_=synthesize(x0,-eps,freq,.9*np.exp(.3j)*preps)
    sy=(yp-ym)/(2*eps)
    er=float(np.max(abs(sy-rest)));central.append(dict(epsilon=eps,max_tangent_error=er))
for i in range(3):
    ratio=central[i]["max_tangent_error"]/central[i+1]["max_tangent_error"]
    check("unmatched-preparation centered convergence"+str(i),2.5<ratio<5.5,ratio)
details["central_difference"]=central
details["nonstationary_tangent_error"]=err

# Simultaneous feature/readout perturbations: no independence assumed.
ff,uw,rr,truezero=dev
rng=np.random.default_rng(20261016)
bounds=[]
for it in range(80):
    ef=2e-6*(1+it/80)
    common=rng.uniform(-1,1,2)
    jitter=rng.uniform(-1,1,(2,6))
    delta=.5*ef*(common[:,None]+jitter)
    fh=ff+delta[0]+1j*delta[1]
    Qh=design(fh);Qtrue=design(ff)
    ea=eb=ef*np.ones(6)
    rad=np.array([np.zeros(6),ea,eb,2*abs(fh.real)*ea+ea*ea,abs(fh.real)*eb+abs(fh.imag)*ea+ea*eb,2*abs(fh.imag)*eb+eb*eb])
    etaq=float(np.linalg.norm(rad))
    AA=1/np.linalg.svd(Qh,compute_uv=False)[-1]
    uh=np.linalg.solve(Qh,E0)
    eu=AA*etaq*np.linalg.norm(uh)/(1-AA*etaq)
    er=2e-7
    obs=rr[:,it*3%len(TS)]+er*np.sign(uh) # deliberately aligned readout error
    pred=float(uh@obs)
    true=float(uw@rr[:,it*3%len(TS)])
    bound=float(er*np.sum(abs(uh))+eu*(np.linalg.norm(obs)+np.sqrt(6)*er))
    ok=AA*etaq<1 and np.linalg.norm(Qtrue-Qh,2)<=etaq+1e-14 and np.linalg.norm(uw-uh)<=eu+1e-12 and abs(pred-true)<=bound+1e-10
    check("correlated error certificate"+str(it),ok)
    bounds.append(dict(actual=abs(pred-true),bound=bound,margin=1-AA*etaq))
details["error_bound_max_ratio"]=max(z["actual"]/z["bound"] for z in bounds)
details["error_margin_min"]=min(z["margin"] for z in bounds)
near=np.exp(1j*theta)*(1+1e-10*np.array([0,1,-1,2,-2,3]))
smin=np.linalg.svd(design(near),compute_uv=False)[-1]
check("near-circle feature-error margin refuses certification",1e-6/smin>=1)
tt,raw,la=prefix(-.2,preps[0]);fit,H,_=fit_prefix(tt,raw,la)
noise=1e-5*np.cos(np.arange(len(tt))*.73)
changed,_,_=fit_prefix(tt,raw+noise,la)
prefix_bound=.5*np.linalg.norm(np.linalg.pinv(H),2)*np.linalg.norm(noise)
check("known-pole prefix fundamental error bound",abs(changed-fit)<=prefix_bound+1e-11)
details["prefix"]={"design_condition":float(np.linalg.cond(H)),"actual_f_error":float(abs(changed-fit)),"bound":float(prefix_bound),"pole_errors_included":False}

result={"summary":{"passed":sum(r["passed"] for r in rows),"failed":sum(not r["passed"] for r in rows)},
        "checks":rows,"details":details,"empirical_validation":False,
        "data_roles":{"development":"First finite drive and six preparations","reserved":"Two additional fixed drives and three additional preparations, declared before computation","empirical":"none"},
        "source_hashes":{n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in ["PREPARATION_BRIDGE_v1.md","PREPARATION_BRIDGE_PLAN_v1.json",Path(__file__).name]},
        "limit":"Class, common histories, observable prefix and calibrated errors remain premises; no certified finite-band inverse or physical reset is derived."}
print(json.dumps(result,indent=2))
sys.exit(bool(result["summary"]["failed"]))
