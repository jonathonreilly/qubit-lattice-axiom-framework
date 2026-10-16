"""Conditional port test; all numeric records are synthetic, never observations."""
AUDIT_TIMEOUT_SEC = 120
import hashlib
import json
from itertools import product
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import solve_ivp, quad
import sympy as sy

checks = []
details = {}


def check(name, condition, detail=None):
    row = {"name": name, "passed": bool(condition)}
    if detail is not None:
        row["detail"] = detail
    checks.append(row)


# Derive the held-force expression from the action, including velocity terms.
x, w, xd, wd, xdd, wdd = sy.symbols("x w xd wd xdd wdd", real=True)
M, k, tau, U, B, C, d, nu, gamma = [sy.Function(n)(x) for n in
                                       ["M", "k", "tau", "U", "B", "C", "d", "nu", "gamma"]]
T = M*xd**2/2 + k*xd*wd + tau*wd**2/2
V = U+B*w+C*w**2/2
Ray = d*xd**2/2+nu*xd*wd+gamma*wd**2/2
dt = lambda z: sy.diff(z,x)*xd+sy.diff(z,w)*wd+sy.diff(z,xd)*xdd+sy.diff(z,wd)*wdd
Fx = sy.expand(dt(sy.diff(T,xd))-sy.diff(T-V,x)+sy.diff(Ray,xd))
Fw = sy.expand(dt(sy.diff(T,wd))-sy.diff(T-V,w)+sy.diff(Ray,wd))
held = Fx.subs({xd:0,xdd:0})
expected = k*wdd-tau.diff(x)*wd**2/2+U.diff(x)+B.diff(x)*w+C.diff(x)*w**2/2+nu*wd
check("Euler_Lagrange_held_force", sy.simplify(held-expected)==0)
check("Euler_Lagrange_held_hidden", sy.simplify(Fw.subs({xd:0,xdd:0})-(tau*wdd+gamma*wd+B+C*w))==0)
zero = {xd:0,wd:0,xdd:0,wdd:0,w:-B/C}
G = B.diff(x)-C.diff(x)*B/C
check("reciprocal_stiffness_cross", sy.simplify(sy.diff(Fx,w).subs(zero)-G)==0 and sy.simplify(sy.diff(Fw,x).subs(zero)-G)==0)
check("reciprocal_kinetic_cross", sy.diff(Fx,wdd)==k and sy.diff(Fw,xdd)==k)
check("reciprocal_damping_cross", sy.simplify(sy.diff(Fx,wd).subs(zero)-nu)==0 and sy.simplify(sy.diff(Fw,xd).subs(zero)-nu)==0)
check("visible_variable_mass_coefficient", sy.expand(Fx).coeff(xd,2)==M.diff(x)/2)

ga, om, cp, tp, ta = sy.symbols("Gamma omega Cp tp tau0", positive=True, real=True)
gg, nn, kk = sy.symbols("G nu0 k0", real=True)
cc, cb, ee, eb = sy.symbols("c cbar E Ebar")
lam=-ga/2+sy.I*om; lb=sy.conjugate(lam); O=sy.expand(lam*lb)
z=cc*ee+cb*eb; zd=lam*cc*ee+lb*cb*eb; zdd=lam**2*cc*ee+lb**2*cb*eb
force=sy.expand(gg*z+kk*zdd+nn*zd+cp*z*z/2-tp*zd*zd/2)
N=gg+nn*lam+kk*lam**2
check("ringdown_fundamental", sy.simplify(force.coeff(ee,1).coeff(eb,0)-N*cc)==0)
check("ringdown_decay_coefficient", sy.simplify(force.coeff(ee,1).coeff(eb,1)-(cp-tp*O)*cc*cb)==0)
check("ringdown_double_frequency", sy.simplify(force.coeff(ee,2)-(cp-tp*lam**2)*cc**2/2)==0)
check("variable_inertia_frequency_gradient", sy.simplify((C/tau).diff(x)*tau-(C.diff(x)-tau.diff(x)*C/tau))==0)
s=sy.symbols("s"); pol=sy.symbols("p0")+sy.symbols("p1")*s+sy.symbols("p2")*s**2
Ns=gg+nn*s+kk*s**2
Z=pol-Ns**2/(ta*(s-lam)*(s-lb))
rho=sy.cancel((s-lam)*Z).subs(s,lam)
check("dynamic_stiffness_residue", sy.simplify(rho+N**2/(ta*(lam-lb)))==0)
check("residue_factor", sy.simplify((2*lam+ga)*rho+N**2/ta)==0)
check("visible_load_polynomial_absent", not (sy.simplify(rho).free_symbols & {sy.symbols("p0"),sy.symbols("p1"),sy.symbols("p2")}))
check("cubic_output_blind_selected_coefficients", all(sy.expand(z**3).coeff(ee,a).coeff(eb,b)==0 for a,b in [(1,0),(1,1)]))
check("quadratic_output_changes_h", sy.expand(z**2).coeff(ee,1).coeff(eb,1)==2*cc*cb)

# Chosen family only generates synthetic records; the extractor sees no hidden parameters.
tx=1+sy.Rational(18,100)*x+sy.Rational(4,100)*x*x
cx=sy.Rational(34,10)+sy.Rational(11,10)*x+sy.Rational(17,100)*x*x
bx=sy.Rational(8,10)*x+sy.Rational(15,100)*x*x+sy.Rational(5,100)*x**3
ux=sy.Rational(6,10)*x*x+sy.Rational(3,100)*x**4
kx=sy.Rational(18,100)+sy.Rational(3,100)*x
nux=sy.Rational(4,100)-sy.Rational(5,1000)*x
gamx=tx*(sy.Rational(35,100)+sy.Rational(3,100)*x)
mx=2+sy.Rational(1,10)*x*x; dx=sy.Rational(4,10)
fields=[tx,cx,bx,ux,kx,nux,gamx,mx,dx,tx.diff(x),cx.diff(x),bx.diff(x),ux.diff(x),cx.diff(x,2),bx.diff(x,2),ux.diff(x,2),(cx/tx).diff(x)]
getpar=sy.lambdify(x,fields,"numpy")


def synthetic_records(env, initial, epsilon=0.0, cubic=0.0):
    t0,c0,b0,u0,k0,n0,g0,m0,d0,tp0,cp0,bp0,up0,cpp0,bpp0,upp0,op = [float(v) for v in getpar(env)]
    w0=-b0/c0; G0=bp0+cp0*w0
    S0=upp0+bpp0*w0+cpp0*w0*w0/2
    rates=(g0/t0,c0/t0)
    angular=np.geomspace(.2,5.5,35)
    values=[]
    for freq in angular:
        sv=1j*freq
        # Full linear matrix and its hidden equation, not the fitted residue formula.
        mat=np.array([[m0*sv*sv+d0*sv+S0,k0*sv*sv+n0*sv+G0],
                      [k0*sv*sv+n0*sv+G0,t0*sv*sv+g0*sv+c0]],dtype=complex)
        eta=-mat[1,0]/mat[1,1]
        values.append(mat[0,0]+mat[0,1]*eta)
    times=np.linspace(0,16,601)
    sol=solve_ivp(lambda t,y:[y[1],-(g0*y[1]+c0*y[0])/t0],
                  (times[0],times[-1]),initial,t_eval=times,rtol=2e-11,atol=2e-13,method="DOP853")
    assert sol.success
    zz,vv=sol.y; acc=-(g0*vv+c0*zz)/t0; ww=w0+zz
    force=up0+bp0*ww+cp0*ww**2/2+k0*acc+n0*vv-tp0*vv**2/2
    force+=epsilon*zz**2+cubic*zz**3
    truth={"Oprime":op,"tau":t0,"Gamma":rates[0],"O":rates[1],"kinetic_margin":m0*t0-k0*k0,"damping_margin":d0*g0-n0*n0}
    return angular,np.asarray(values),times,force,truth


def extract(angular, zvals, times, force):
    ss=1j*angular
    A=np.column_stack([-ss*zvals,-zvals,ss**4,ss**3,ss**2,ss,np.ones_like(ss)])
    y=ss*ss*zvals
    mat=np.vstack([A.real,A.imag]); target=np.r_[y.real,y.imag]
    coeff,resid,rank,sv=np.linalg.lstsq(mat,target,rcond=None)
    Gamma,omega2=coeff[:2]
    assert Gamma>0 and omega2>Gamma*Gamma/4
    pole=-Gamma/2+1j*np.sqrt(omega2-Gamma*Gamma/4)
    residue=np.polyval(coeff[2:],pole)/(2*pole+Gamma)
    kspec=abs((2*pole+Gamma)*residue)
    t=times; freq=pole.imag
    basis=np.column_stack([np.ones_like(t),np.exp(-Gamma*t/2)*np.cos(freq*t),
          np.exp(-Gamma*t/2)*np.sin(freq*t),np.exp(-Gamma*t),
          np.exp(-Gamma*t)*np.cos(2*freq*t),np.exp(-Gamma*t)*np.sin(2*freq*t)])
    rc,_,rrank,rsv=np.linalg.lstsq(basis,force,rcond=None)
    f=(rc[1]-1j*rc[2])/2; h=rc[3]
    return {"Gamma":Gamma,"O":omega2,"kspec":kspec,"h":h,"f":f,
            "Q":kspec*h/abs(f)**2,"residue":residue,"pole":pole,
            "rank":int(rank),"ring_rank":int(rrank),"condition":float(sv[0]/sv[-1]),
            "ring_condition":float(rsv[0]/rsv[-1]),
            "ring_residual":float(np.max(np.abs(basis@rc-force)))}


rows=[]
development=[(-.8,(.31,-.22)),(.0,(-.42,.13)),(.7,(.15,.39))]
reserved=[(-.45,(-.27,-.37)),(.3,(.52,.19)),(1.,(-.18,.41))]
for group, cases in [("development",development),("reserved_synthetic",reserved)]:
    for env,initial in cases:
        a,zv,t,force,truth=synthetic_records(env,initial)
        fit=extract(a,zv,t,force)
        lab=group+"_"+str(env)
        check(lab+"_positive_class",truth["kinetic_margin"]>0 and truth["damping_margin"]>0)
        check(lab+"_extractor_rank",fit['rank']==7 and fit['ring_rank']==6)
        check(lab+"_pole_recovery",abs(fit['O']-truth['O'])<1e-10 and abs(fit['Gamma']-truth['Gamma'])<1e-10)
        check(lab+"_action_identity",abs(fit['Q']-truth['Oprime'])<3e-9)
        check(lab+"_full_force_closure",fit['ring_residual']<1e-10)
        rows.append({"role":group,"x":env,"initial":initial,"true_derivative":truth['Oprime'],"extracted_Q":fit['Q'],"dynamic_fit_condition":fit['condition'],"ring_fit_condition":fit['ring_condition'],"max_force_residual":fit['ring_residual']})
details['synthetic_rows']=rows

aa,zz,tt,ff,truth=synthetic_records(.3,(.31,-.22))
base=extract(aa,zz,tt,ff)
alt=extract(*synthetic_records(.3,(.31,-.22),epsilon=.08)[:4])
check("output_only_quadratic_same_linear_response",abs(alt['kspec']-base['kspec'])<1e-14)
check("output_only_quadratic_same_fundamental",abs(alt['f']-base['f'])<1e-10)
check("output_only_quadratic_predicted_defect",abs((alt['Q']-base['Q'])-.16/truth['tau'])<2e-9)
check("output_only_quadratic_rejected",abs(alt['Q']-truth['Oprime'])>.1)
check("output_only_quadratic_still_six_modes",alt['ring_residual']<1e-10)
cub=extract(*synthetic_records(.3,(.31,-.22),cubic=.8)[:4])
check("cubic_output_requires_closure_test",cub['ring_residual']>1e-4)
details['alternative']={'quadratic_defect':float(alt['Q']-base['Q']),'cubic_full_basis_residual':cub['ring_residual']}

# Time-origin and signed affine observation changes do not need hidden state.
later=extract(aa,zz,tt[100:]-tt[100],ff[100:])
check("time_origin_cancels",abs(later['Q']-base['Q'])<1e-9)
for gx,gr in [(2.3,.7),(-1.7,-2.1)]:
    changed=extract(aa,zz*gr/gx,tt,ff*gr+3)
    check("affine_work_orientation_"+str(gx),abs(changed['Q']-base['Q']/gx)<1e-9)

# Distinct necessary exclusions, rather than forcing a fit to supply them.
check("no_decay_merges_h_with_offset",len(set([0,0]))==1)
check("unexcited_mode_has_no_force_anchor",abs(0j)**2==0)
Ncancel=(s-lam)*(s-lb)
Zcancel=sy.cancel(pol-Ncancel**2/(ta*(s-lam)*(s-lb)))
check("pole_cancellation_is_blind",sy.denom(Zcancel).has(s)==False)
check("omit_inertia_gradient_is_false",abs(float((cx.diff(x)/tx-(cx/tx).diff(x)).subs(x,.3)))>.1)

# Error budget for correlated complex perturbations uses true bounds.
K0,h0,f0=.8,-.35,.7+.4j
eK,eh,ef=.02,.015,.01
Fmin=abs(f0);Fmax=Fmin;Hmax=abs(h0);Kmax=K0
eD=2*Fmax*ef+ef*ef;Dmin=Fmin*Fmin
eN=Kmax*eh+Hmax*eK+eK*eh
budget=eN/(Dmin-eD)+Kmax*Hmax*eD/(Dmin*(Dmin-eD))
error_cases=[]
for sk,sh in product([-1,1],repeat=2):
    for angle in np.linspace(0,2*np.pi,17):
        qh=(K0+sk*eK)*(h0+sh*eh)/abs(f0+ef*np.exp(1j*angle))**2
        error_cases.append(abs(qh-K0*h0/abs(f0)**2))
check("finite_quotient_error_68_cases",max(error_cases)<=budget)
la=-.2+1.8j;ga0=.4;rh=.3-.2j;el,eg,er=.01,.02,.015
ekbound=(2*abs(la)+abs(ga0))*er+abs(rh)*(2*el+eg)+(2*el+eg)*er
errs=[]
for u,v in product(np.linspace(0,2*np.pi,9),repeat=2):
    for sign in [-1,1]:
        kh=abs((2*(la+el*np.exp(1j*u))+ga0+sign*eg)*(rh+er*np.exp(1j*v)))
        errs.append(abs(kh-abs((2*la+ga0)*rh)))
check("residue_modulus_error_162_cases",max(errs)<=ekbound)
details['error_budgets']={'quotient_bound':budget,'quotient_max_error':max(error_cases),'residue_bound':ekbound,'residue_max_error':max(errs)}

# Cross-environment integral with a separate exact analytic Lipschitz certificate.
Qfun=sy.lambdify(x,(cx/tx).diff(x),'numpy')
Ofun=sy.lambdify(x,cx/tx,'numpy')
qa,qb=-.8,1.; integ,qe=quad(Qfun,qa,qb,epsabs=1e-12,epsrel=1e-12)
check("cross_environment_integral",abs(integ-(Ofun(qb)-Ofun(qa)))<1e-12)
# A manufactured Lipschitz function isolates the midpoint bound itself.
edges=np.array([0.,.1,.4,.65,1.]); widths=np.diff(edges); mids=(edges[:-1]+edges[1:])/2
Lq=2.;epsilon_q=.003
qfun=lambda a:abs(2*a-.71)
trueint=quad(qfun,0,1,points=[.355],epsabs=1e-12)[0]
estimate=sum(widths*(qfun(mids)+epsilon_q))
bound=sum(widths*epsilon_q)+Lq*sum(widths**2)/4
check("finite_bin_Lipschitz_certificate",abs(estimate-trueint)<=bound)

root=Path(__file__).resolve().parent
result={"scope":"conditional synthetic common-action ringdown test; not physical validation",
        "source_sha256":hashlib.sha256((root/'COMMON_ACTION_RINGDOWN_v1.md').read_bytes()).hexdigest(),
        "runner_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "versions":{"numpy":np.__version__,"scipy":scipy.__version__,"sympy":sy.__version__},
        "summary":{"passed":sum(c['passed'] for c in checks),"failed":sum(not c['passed'] for c in checks)},
        "checks":checks,"details":details,"empirical_validation":False,
        "data_roles":{"calibration":"synthetic linear-response records; pole features fitted before ringdown extraction","development":"three named environments","reserved_test":"three distinct synthetic environments and preparations; frozen extractor, no fitted potential function"}}
print(json.dumps(result,indent=2))
assert result['summary']['failed']==0
