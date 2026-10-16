#!/usr/local/bin/python3
"""Independent synthetic endpoint/count construction controls; no author imports."""
from pathlib import Path
import hashlib
import json
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
checks = []

def check(name, condition, **detail):
    row = {'name': name, 'passed': bool(condition), **detail}
    checks.append(row)
    if not condition:
        raise AssertionError(row)

def exact_controls():
    H,L,t0,D,s = sp.symbols('H L t0 D s', real=True)
    gamma = [-1,3,-3,1]
    ts = [t0+i*D for i in range(4)]
    es = [t-2*L for t in ts]
    bs = [t-L for t in ts]
    d = lambda t: 1-H*t
    P = lambda t: t-H*t*t/2
    beta = [d(e)*g for e,g in zip(es,gamma)]
    for order in range(3):
        check(f'gamma_polynomial_moment_{order}', sp.expand(sum(g*t**order for g,t in zip(gamma,ts))) == 0)
    check('beta_sum_zero', sp.expand(sum(beta)) == 0)
    check('position_station_column', sum(2*g for g in gamma) == 0)
    check('position_craft_column', sum(-2*g for g in gamma) == 0)
    check('velocity_station_column', sp.expand(sum(g*(P(e)+P(t)) for g,e,t in zip(gamma,es,ts))) == 0)
    check('velocity_craft_column', sp.expand(sum(-2*g*P(b) for g,b in zip(gamma,bs))) == 0)
    check('shared_clock_column', sp.expand(sum(g*(d(e)-d(t)) for g,e,t in zip(gamma,es,ts))) == 0)
    check('constant_chi_moment', sp.expand(sum(g*(d(e)*e-d(t)*t) for g,e,t in zip(gamma,es,ts))) == 0)
    for shift in [0,L,2*L]:
        check('early_force_kernel_'+str(shift), sp.expand(sum(g*(P(t-shift)-P(s)) for g,t in zip(gamma,ts))) == 0)
    dtau = sp.symbols('d_tau0:3', positive=True)
    ell = [-dtau[i]*sum(beta[:i+1]) for i in range(3)]
    recovered = [-ell[0]/dtau[0], ell[0]/dtau[0]-ell[1]/dtau[1], ell[1]/dtau[1]-ell[2]/dtau[2], ell[2]/dtau[2]]
    for i in range(4):
        check('proper_count_endpoint_'+str(i), sp.simplify(recovered[i]-beta[i]) == 0)

    # H=0 common-field norm: exact pair-overlap integration of step densities.
    z=sp.symbols('z',real=True)
    LL=sp.Rational(3,5)
    tt=[sp.Rational(7,5)+i for i in range(4)]
    coeff=[]; knots=[]
    for g,t in zip(gamma,tt):
        coeff += [g*(1+z),g*(z-1),-2*z*g]
        knots += [t-2*LL,t,t-LL-z*LL]
    total=sp.Integer(0)
    pieces=0
    for i in range(12):
        for j in range(i,12):
            gap=sp.Poly(knots[i]-knots[j],z)
            cuts=[sp.Integer(-1),sp.Integer(1)]
            if gap.degree()==1:
                cross=-gap.nth(0)/gap.nth(1)
                if -1<cross<1:
                    cuts.insert(1,cross)
            for lo,hi in zip(cuts[:-1],cuts[1:]):
                mid=(lo+hi)/2
                smaller=knots[i] if (knots[i]-knots[j]).subs(z,mid)<=0 else knots[j]
                expression=sp.Poly((1 if i==j else 2)*coeff[i]*coeff[j]*smaller,z)
                primitive=expression.integrate().as_expr()
                total += primitive.subs(z,hi)-primitive.subs(z,lo)
                pieces += 1
    pi_gram=sp.factor(total/4)
    check('flat_common_field_gram_exact', pi_gram==sp.Rational(329,54), pi_times_gram=str(pi_gram),pair_pieces=pieces)
    # Explicit angle-wise positivity independently follows by sorting the 12 steps.
    kfun=sp.lambdify(z,knots,'numpy'); afun=sp.lambdify(z,coeff,'numpy')
    for zz in [-1,-.7,-.25,0,.2,.75,1]:
        kk=np.asarray(kfun(zz),float); aa=np.asarray(afun(zz),float)
        overlap=float(aa@np.minimum.outer(kk,kk)@aa)
        unique=np.unique(kk)
        interval=sum((right-left)*np.sum(aa[kk>(left+right)/2])**2 for left,right in zip(unique[:-1],unique[1:]))
        check('flat_overlap_sorted_'+str(zz), abs(overlap-interval)<2e-12,overlap=overlap,sorted_intervals=float(interval))
    return str(pi_gram)

L=.6
TIMES=np.array([1.4,2.4,3.4,4.4])
GAMMA=np.array([-1.,3.,-3.,1.])
NUISANCE=np.array([.08,-.035,.09,-.06,.025,-.13])

def field(t,x,kind,H):
    if kind=='trig':
        chi=.2*np.sin(.7*t+.5*x)+.04*t*x+.03*np.cos(.4*t-.8*x)
        ct=.14*np.cos(.7*t+.5*x)+.04*x-.012*np.sin(.4*t-.8*x)
        cx=.1*np.cos(.7*t+.5*x)+.04*t+.024*np.sin(.4*t-.8*x)
    elif kind=='polynomial':
        chi=.12+.05*t*t+.07*t*x+.08*x*x*t
        ct=.1*t+.07*x+.08*x*x
        cx=.07*t+.16*x*t
    elif kind=='constant_chi':
        chi,ct,cx=1.,0.,0.
    elif kind=='constant_h':
        chi=1/(1-H*t); ct=H*chi*chi; cx=0.
    elif kind=='zero':
        chi,ct,cx=0.,0.,0.
    else: raise ValueError(kind)
    return chi,ct,cx

def proper(t,H):
    return -np.log1p(-H*np.asarray(t))/H if H else np.asarray(t)

def weights(s,H):
    P=lambda t:t-H*t*t/2
    F=lambda shift:float(np.sum(GAMMA*(P(TIMES-shift)-P(s))*(s<TIMES-shift)))
    c=float(np.sum(GAMMA*((1-H*(TIMES-2*L))*(s<TIMES-2*L)-(1-H*TIMES)*(s<TIMES))))
    return c,F(2*L)+F(0),-2*F(L)

def kernel(kind,H):
    knots=np.unique(np.r_[0,TIMES,TIMES-L,TIMES-2*L])
    def integrand(s):
        c,ws,wb=weights(s,H)
        return c*field(s,0,kind,H)[0]-ws*field(s,0,kind,H)[2]-wb*field(s,L,kind,H)[2]
    return sum(quad(integrand,lo,hi,epsabs=2e-12,epsrel=2e-12)[0] for lo,hi in zip(knots[:-1],knots[1:]))

def linear_endpoint(kind,H,nuisance):
    def rhs(t,y):
        answer=[]
        for j,x in [(0,0),(3,L)]:
            chi,ct,cx=field(t,x,kind,H)
            answer.extend([y[j+1],-H/(1-H*t)*y[j+1]-(1-H*t)*cx,chi])
        return answer
    sol=solve_ivp(rhs,(0,4.7),nuisance,method='DOP853',rtol=2e-13,atol=2e-14,dense_output=True)
    assert sol.success
    beta=GAMMA*(1-H*(TIMES-2*L))
    phi=[]
    for r in TIMES:
        e=r-2*L; b=r-L
        ye=sol.sol(e); yr=sol.sol(r); yb=sol.sol(b)
        ae=1/(1-H*e); ar=1/(1-H*r)
        phi.append(ye[2]-ae/ar*yr[2]+ae*(ye[0]+yr[0]-2*yb[3]))
    dtau=np.diff(proper(TIMES,H)); ell=-dtau*np.cumsum(beta)[:3]
    return float(beta@phi),float(ell@(np.diff(phi)/dtau))

def nonlinear_endpoint(kind,H,eps,nuisance):
    initial=eps*nuisance.copy();initial[3]+=L
    def rhs(t,y):
        answer=[]
        for j in [0,3]:
            x,v=y[j:j+2];chi,ct,cx=field(t,x,kind,H)
            d=1-H*t; h=d*chi; ht=-H*chi+d*ct; hx=d*cx
            answer.extend([v,-(1-v*v)*(H/d*v+eps*(hx+v*ht)),math.exp(eps*h)/d*math.sqrt(1-v*v)])
        return answer
    sol=solve_ivp(rhs,(0,4.7),initial,method='DOP853',rtol=2e-13,atol=2e-14,dense_output=True)
    assert sol.success
    phases=[]; event_residuals=[]
    for t in TIMES:
        tau=float(proper(t,H))
        r=brentq(lambda r:float(sol.sol(r)[2])-tau,max(0,t-.25),t+.25,xtol=1e-13)
        xs=sol.sol(r)[0]
        b=brentq(lambda b:r-b-float(sol.sol(b)[3]-xs),0,r,xtol=1e-13)
        xb=sol.sol(b)[3]
        e=brentq(lambda e:b-e-float(xb-sol.sol(e)[0]),0,b,xtol=1e-13)
        phases.append(sol.sol(e)[2])
        event_residuals.extend([abs(sol.sol(r)[2]-tau),abs(r-b-(sol.sol(b)[3]-xs)),abs(b-e-(xb-sol.sol(e)[0]))])
    beta=GAMMA*(1-H*(TIMES-2*L));dtau=np.diff(proper(TIMES,H));ell=-dtau*np.cumsum(beta)[:3]
    return float(beta@phases),float(ell@(np.diff(phases)/dtau)),max(event_residuals)

def numerical_controls():
    rows=[]
    for H in [0.,.04,.1]:
        beta=GAMMA*(1-H*(TIMES-2*L));dtau=np.diff(proper(TIMES,H))
        check('proper_spacing_valid_'+str(H),np.all(dtau>0) and (H==0 or np.ptp(dtau)>0),spacings=dtau.tolist())
        cvalue=kernel('constant_chi',H)
        check('constant_chi_numeric_'+str(H),abs(cvalue)<2e-14,value=cvalue)
        if H:
            hvalue=kernel('constant_h',H)
            check('physical_constant_distinguished_'+str(H),abs(hvalue)>1e-7,value=hvalue)
        for kind in ['trig','polynomial']:
            pred=kernel(kind,H)
            l0,c0=linear_endpoint(kind,H,np.zeros(6));ln,cn=linear_endpoint(kind,H,NUISANCE)
            check('linear_ode_vs_kernel_'+str(H)+'_'+kind,max(abs(l0-pred),abs(ln-pred))<2e-10,prediction=pred,no_nuisance=l0,with_nuisance=ln)
            check('linear_three_proper_counts_'+str(H)+'_'+kind,max(abs(c0-l0),abs(cn-ln))<3e-14)
            errors=[];values=[];eventmax=0.;countdiff=0.
            for eps in [.002,.001,.0005]:
                positive=nonlinear_endpoint(kind,H,eps,NUISANCE)
                negative=nonlinear_endpoint(kind,H,-eps,NUISANCE)
                derivative=(positive[0]-negative[0])/(2*eps)
                countderivative=(positive[1]-negative[1])/(2*eps)
                values.append(derivative);errors.append(abs(derivative-pred))
                eventmax=max(eventmax,positive[2],negative[2])
                countdiff=max(countdiff,abs(derivative-countderivative))
            check('nonlinear_fixed_proper_fd_'+str(H)+'_'+kind,errors[-1]<3e-6*max(1,abs(pred)),prediction=pred,steps=[.002,.001,.0005],derivatives=values,errors=errors)
            check('nonlinear_three_proper_counts_'+str(H)+'_'+kind,countdiff<1e-10,maximum_difference=countdiff)
            check('nonlinear_event_roots_'+str(H)+'_'+kind,eventmax<5e-12,maximum_residual=eventmax)
            rows.append({'H':H,'field':kind,'prediction':pred,'errors':errors,'derivatives':values})
    return rows

if __name__=='__main__':
    gram=exact_controls()
    rows=numerical_controls()
    result={'checks_passed':len(checks),'checks':checks,'flat_pi_gram':gram,'nonlinear_comparisons':rows,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'precheck_sha256':hashlib.sha256((HERE/'CURVED_COUNT_PRECHECK_v1.md').read_bytes()).hexdigest(),
        'scope':'Independent exact algebra and synthetic nonlinear proper-count controls. No curved author code exposed. No KG solution or empirical calibration claim.'}
    out=HERE/'INDEPENDENT_CURVED_COUNT_RESULTS_v1.json'
    with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'checks_passed':len(checks),'flat_pi_gram':gram,'maximum_final_fd_error':max(r['errors'][-1] for r in rows),'source_sha256':result['source_sha256']}))
