#!/usr/local/bin/python3
"""Author controls for the supplied de Sitter scalar/count reconstruction."""
from pathlib import Path
import hashlib
import json
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from numpy.polynomial.legendre import leggauss

HERE=Path(__file__).resolve().parent
checks=[]
L=.6
times=np.array([1.4,2.4,3.4,4.4])
gamma=np.array([-1.,3.,-3.,1.])


def check(name,condition,**evidence):
    checks.append({'name':name,'passed':bool(condition),**evidence})
    if not condition:
        raise AssertionError(name+': '+repr(evidence))


def weights(s,H):
    s=np.asarray(s)
    P=lambda t:t-H*t*t/2
    F=lambda a:np.sum(gamma[:,None]*(P(times[:,None]-a)-P(s))*(s<times[:,None]-a),axis=0)
    ws,wb=F(2*L)+F(0),-2*F(L)
    cs=np.sum(gamma[:,None]*((1-H*(times[:,None]-2*L))*(s<times[:,None]-2*L)
                          -(1-H*times[:,None])*(s<times[:,None])),axis=0)
    return cs,ws,wb


def exact_gram():
    z,t,H=sp.symbols('z t H',real=True)
    length=sp.Rational(3,5)
    ts=[sp.Rational(7,5)+j for j in range(4)]
    gs=[-1,3,-3,1]
    # Each event is an affine time q and its affine-in-time Heaviside coefficient.
    events=[]
    for ti,gi in zip(ts,gs):
        events.extend([
            (ti-2*length,gi*(1-H*(ti-2*length)+z*(1-H*t))),
            (ti,gi*(-(1-H*ti)+z*(1-H*t))),
            (ti-length-length*z,-2*gi*z*(1-H*(t+length*z)))])
    cuts={sp.Rational(-1),sp.Rational(1)}
    for i,(qi,_) in enumerate(events):
        for qj,_ in events[i+1:]:
            diff=sp.Poly(qi-qj,z)
            if diff.degree()==1:
                root=-diff.nth(0)/diff.nth(1)
                if -1<root<1:
                    cuts.add(root)
    cuts=sorted(cuts)
    total=0
    for za,zb in zip(cuts[:-1],cuts[1:]):
        mid=(za+zb)/2
        qs=sorted(set(q for q,_ in events),key=lambda q:float(q.subs(z,mid)))
        interval_total=0
        for qa,qb in zip(qs[:-1],qs[1:]):
            tm=(qa.subs(z,mid)+qb.subs(z,mid))/2
            ht=sp.expand(sum(expr for q,expr in events if q.subs(z,mid)>tm))
            poly=sp.Poly(ht*ht,t)
            primitive=sum(value*t**(power[0]+1)/(power[0]+1) for power,value in poly.terms())
            interval_total+=sp.expand(primitive.subs(t,qb)-primitive.subs(t,qa))
        zp=sp.Poly(sp.expand(interval_total),z)
        total+=sum(value*(zb**(power[0]+1)-za**(power[0]+1))/(power[0]+1)
                   for power,value in zp.terms())
    gram=sp.factor(total/(4*sp.pi))
    return gram,H,cuts


def numerical_gram(H,order=120):
    # Independent direct time-interval integration of transformed weights.
    zn,zw=leggauss(order)
    total=0.
    for z,wz in zip(zn,zw):
        edges=sorted(set([*(times-2*L),*times,*(times-L-L*z)]))
        for a,b in zip(edges[:-1],edges[1:]):
            gn,gw=leggauss(3)
            tau=a+(b-a)*(gn+1)/2
            fp=lambda s,shift: -(1-H*s)*np.sum(gamma[:,None]*(s<times[:,None]-shift),axis=0)
            c,_,_=weights(tau,H)
            wsp=fp(tau,2*L)+fp(tau,0)
            wbp=-2*fp(tau+L*z,L)
            hh=c-z*wsp-z*wbp
            total+=wz*np.sum(gw*hh*hh)*(b-a)/2
    return total/(4*np.pi)


def mode_and_observation(H,B,k,z,initial=True):
    mu=np.sqrt(B-2)*H
    omega=np.hypot(k,mu)
    y0=np.zeros(7,dtype=complex)
    y0[:2]=[1,1j*omega]
    if initial:
        y0[2:]=[.31,-.27,.12,.19,-.23]
    bodyphase=np.exp(-1j*k*z*L)
    def rhs(t,y):
        a=1/(1-H*t); hh=H*a
        f,fp,eta,xs,vs,xb,vb=y
        return np.array([fp,-(k*k+mu*mu*a*a)*f,f,vs,-hh*vs+1j*k*z*f/a,
                         vb,-hh*vb+1j*k*z*bodyphase*f/a])
    sol=solve_ivp(rhs,[0,times[-1]],y0,method='DOP853',rtol=2e-11,atol=2e-12,dense_output=True)
    if not sol.success:
        raise AssertionError(sol.message)
    phase=[]
    for ti in times:
        emit,bounce=ti-2*L,ti-L
        ye,yb,yr=sol.sol(emit),sol.sol(bounce),sol.sol(ti)
        ae=1/(1-H*emit); ar=1/(1-H*ti)
        phase.append(ye[2]-ae/ar*yr[2]+ae*(ye[3]+yr[3]-2*yb[5]))
    beta=(1-H*(times-2*L))*gamma
    direct=np.dot(beta,phase)
    gn,gw=leggauss(36)
    edges=sorted(set([*(times-2*L),*times,*(times-L)]))
    weighted=0j
    for a,b in zip(edges[:-1],edges[1:]):
        t=a+(b-a)*(gn+1)/2
        cs,ws,wb=weights(t,H)
        f=sol.sol(t)[0]
        weighted+=np.sum(gw*f*(cs+1j*k*z*(ws+bodyphase*wb)))*(b-a)/2
    return direct,weighted,sol


def run():
    t,H,B=sp.symbols('t H B',positive=True)
    a=1/(1-H*t); hh=sp.diff(a,t)/a
    h=sp.Function('h')(t); chi=sp.Function('chi')(t)
    transformed=sp.expand(a*(sp.diff(chi/a,t,2)+2*hh*sp.diff(chi/a,t)+a*a*B*H*H*chi/a))
    expected=sp.diff(chi,t,2)+(B-2)*H*H/(1-H*t)**2*chi
    check('conformal_field_equation',sp.simplify(transformed-expected)==0)
    c,w,u=sp.symbols('c w u',real=True)
    # Time derivative contribution is the nontrivial part of the weight change.
    lhs=c*chi/a-(1-u*u)*w*u*sp.diff(chi/a,t)
    rhs=(c+(1-u*u)*hh*w*u)*chi/a-(1-u*u)*w*u*sp.diff(chi,t)/a
    check('moving_clock_force_weight_transform',sp.simplify(lhs-rhs)==0)
    p,q=sp.symbols('p q',real=True)
    energy=(p-H*q)**2+B*H*H*q*q
    expected=p*p-2*H*p*q+(B+1)*H*H*q*q
    check('physical_initial_energy_cross_term',sp.expand(energy-expected)==0)
    rng=np.random.default_rng(17)
    ratios=[]
    for b in [12.001,16.,50.,1000.]:
        r=1/np.sqrt(b-2)
        lam=np.linalg.eigvalsh([[1.,-r],[-r,1+3*r*r]])
        formula=np.array([1+1.5*r*r-np.sqrt(r*r+2.25*r**4),1+1.5*r*r+np.sqrt(r*r+2.25*r**4)])
        check('physical_energy_eigenvalues_B_'+str(b),np.max(abs(lam-formula))<1e-14 and lam[0]>0,eigenvalues=lam.tolist())
        for _ in range(20):
            f=rng.normal(size=3); n=f@f
            physical=f[0]**2-2*r*f[0]*f[1]+(1+3*r*r)*f[1]**2+f[2]**2
            ratios.append(physical/n)
            assert lam[0]-1e-13 <= physical/n <= lam[1]+1e-13
    check('energy_norm_random_controls',True,sampled_cases=len(ratios),range=[min(ratios),max(ratios)])

    length,t0,step=sp.symbols('L t0 step',positive=True)
    tt=[t0+i*step for i in range(4)]
    gam=[-1,3,-3,1]
    P=lambda s:s-H*s*s/2
    beta=[(1-H*(x-2*length))*g for x,g in zip(tt,gam)]
    conditions={
        'endpoint_sum':sum(beta),
        'initial_position':sum(gam),
        'station_initial_velocity':sum(g*(P(x-2*length)+P(x)) for x,g in zip(tt,gam)),
        'spacecraft_initial_velocity':sum(-2*g*P(x-length) for x,g in zip(tt,gam)),
        'initial_clock':sum(g*2*H*length for g in gam),
        'comparison_constant':sum(g*((1-H*(x-2*length))*(x-2*length)-(1-H*x)*x) for x,g in zip(tt,gam))}
    for name,expr in conditions.items():
        check('exact_curved_contrast_'+name,sp.simplify(expr)==0)
    gram,Hsym,cuts=exact_gram()
    check('curved_gram_flat_limit',sp.simplify(gram.subs(Hsym,0)-sp.Rational(329,54)/sp.pi)==0,expression=str(gram),angular_cuts=[str(x) for x in cuts])
    numerical=[]
    for hv in [0.,.01,.05,.15]:
        value=float(gram.subs(Hsym,hv))
        # Split angular integral at all exact event-order break points.
        # Current numerical_gram samples globally, so retain its finite diagnostic error.
        numeric=numerical_gram(hv,240)
        numerical.append([hv,value,numeric,abs(value-numeric)])
    check('curved_gram_direct_piecewise_control',max(x[3] for x in numerical)<4e-4,comparisons=numerical,classification='finite angular quadrature diagnostic, exact polynomial is proof supplier')

    maxcount=0.;maxinitial=0.;modeboundratios=[]
    for hv in [.005,.05,.12]:
        bv=16.;mu=np.sqrt(bv-2)*hv;T=times[-1]
        S=mu*mu*hv*T*T/(1-hv*T);R=np.exp(S/mu)
        for kv,zv in [(.03,-.7),(.4,.2),(2.,.8),(8.,-1.)]:
            direct,weighted,sol=mode_and_observation(hv,bv,kv,zv,True)
            direct0,_,_=mode_and_observation(hv,bv,kv,zv,False)
            maxcount=max(maxcount,abs(direct-weighted))
            maxinitial=max(maxinitial,abs(direct-direct0))
            grid=np.linspace(0,T,301);f,fp=sol.sol(grid)[:2];omega=np.hypot(kv,mu)
            e=np.exp(1j*omega*grid)
            ratio_f=np.max(abs(f-e))/(R*S/omega)
            ratio_p=np.max(abs(fp-1j*omega*e))/(R*S)
            modeboundratios.extend([float(ratio_f),float(ratio_p)])
    check('curved_original_ode_vs_derived_count',maxcount<3e-9,maximum_error=float(maxcount))
    check('curved_initial_orbit_clock_cancellation',maxinitial<3e-9,maximum_error=float(maxinitial))
    check('potential_mode_difference_enclosure',max(modeboundratios)<=1+1e-8,maximum_ratio=max(modeboundratios))
    # Explicit count conversion at actual proper-time labels.
    hv=.05
    tau=-np.log(1-hv*times)/hv
    beta=(1-hv*(times-2*L))*gamma
    phase=np.array([.4,-.2,.8,.1])
    count=np.diff(phase)/np.diff(tau)
    coeff=-np.diff(tau)*np.cumsum(beta)[:-1]
    check('proper_count_endpoint_conversion',abs(coeff@count-beta@phase)<2e-15,
          proper_intervals=np.diff(tau).tolist(),count_coefficients=coeff.tolist())
    result={'status':'working mathematical controls; no empirical validation','checks':checks,'checks_passed':len(checks),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'working_note_sha256':hashlib.sha256((HERE/'CURVED_COUNT_WORKING_v1.md').read_bytes()).hexdigest(),
            'exact_massless_curved_count_gram':str(gram),'exact_gram_coefficients':[str(x) for x in sp.Poly(gram,Hsym).all_coeffs()],
            'curved_count_numeric_gram':numerical,'mode_comparison_maximum_ratio':max(modeboundratios),
            'limits':['Fixed vacuum/action and homogeneous linear scalar perturbation only.','No actual measured H,B,Q, residual, error or energy budget.','Potential operator high-frequency proof needs independent check.']}
    (HERE/'CURVED_COUNT_RESULTS_v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'checks_passed':len(checks),'exact_gram':str(gram),'source_sha256':result['source_sha256'],
                      'maximum_count_error':maxcount,'maximum_initial_leakage':maxinitial}))


if __name__=='__main__':
    run()
