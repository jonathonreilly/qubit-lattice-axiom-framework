#!/usr/bin/env python3
"""Exact constructed controls; no empirical files or action fitting."""
import json
from pathlib import Path
import sympy as s
AUDIT_TIMEOUT_SEC = 120
# No external scientific or package-local input files are read.

def main():
    checks = {}
    def check(name, expression):
        checks[name] = bool(expression)
    def zero(name, expression):
        check(name, s.simplify(expression) == 0)
    z = s.symbols('z', nonnegative=True)
    h, v0, A0, d0, ell = s.symbols('h v A d ell', real=True)
    k = s.symbols('k', real=True)
    zero('lift_expansion', A0*(h-v0)**2 + k*d0**2 - ell - (A0*h*h-2*A0*v0*h-ell+k*d0*d0+A0*v0*v0))
    d = (z+z*z)/2
    H = 1/(1+2*z)
    v = 1-H/(1+z)
    A = (1+z)**2*s.diff(d,z)**2
    nodes = [s.Rational(1,4),s.Rational(1,2),s.Rational(3,4),s.Integer(1)]
    row = s.Matrix([[A,-2*A*v,-1,d*d]])
    mat = s.Matrix.vstack(*(row.subs(z,x) for x in nodes))
    rhs = s.Matrix([(-A*v*v).subs(z,x) for x in nodes])
    theta = mat.inv()*rhs
    check('rank_four', mat.det()!=0)
    check('recovered_parameters', theta==s.Matrix([1,1,s.Rational(1,4),0]))
    zero('continuum_compatibility', (row*theta)[0]+A*v*v)
    zero('distance_ODE', H*s.diff(2*d,z)-1)
    zero('drift_identity', (1+z)*theta[1]-(1+z)*v-H)
    zero('flat_integral', s.integrate(1/((1+z)*(1-v)),(z,0,z))-2*d)
    # A fifth constructed point is a validation control, not held-out empirical data.
    check('fifth_point', s.simplify((row*theta)[0]+A*v*v).subs(z,s.Rational(5,4))==0)
    check('wrong_scale_rejected', s.simplify((row*s.Matrix([1,1,1,0]))[0]+A*v*v)!=0)
    check('drift_sign_mutation_rejected', s.simplify(A*(1+v)**2-s.Rational(1,4))!=0)
    check('curvature_sign_control', s.expand(A0*(h-v0)**2-ell+k*d0*d0).coeff(k)==d0*d0)
    # Coasting flat background: v=0, d=ln(1+z) admits every H0>0 with L=1/H0.
    coastd=s.log(1+z)
    coastA=s.simplify((1+z)**2*s.diff(coastd,z)**2)
    zero('coasting_family',coastA*h*h-h*h)
    coastmat=s.Matrix([[1,0,-1,s.log(1+x)**2] for x in nodes])
    check('coasting_rank_two',coastmat.rank()==2)
    # Strict flat-integral ratio monotonicity kernel for v(t)>v(s), h>v(t).
    vs,vt=s.symbols('vs vt',real=True)
    zero('ratio_derivative_kernel', -1/(h-vt)+1/(h-vs)-(vs-vt)/((h-vt)*(h-vs)))
    # The following inverse perturbation check uses exact rational arithmetic.
    pert=s.zeros(4); pert[0,0]=s.Rational(1,10**8)
    delta=s.Matrix([s.Rational(1,10**9),0,0,0])
    def norm(m):
        return max(sum(abs(m[i,j]) for j in range(m.cols)) for i in range(m.rows))
    invnorm=norm(mat.inv()); eta=invnorm*norm(pert)
    bound=invnorm*(norm(delta)+norm(pert)*norm(theta))/(1-eta)
    observed=(mat+pert).inv()*(rhs+delta)
    check('inverse_smallness',eta<1)
    check('inverse_bound',norm(observed-theta)<=bound)
    # Clock gain c sends v,H0,H -> c times themselves, L -> L/c, k -> c²k.
    c=s.symbols('c',positive=True)
    zero('clock_gain_symmetry', A0*(c*h-c*v0)**2-(c*c*ell-c*c*k*d0*d0)-c*c*(A0*(h-v0)**2-ell+k*d0*d0))
    # Independent time information: Taylor bound coefficient and exact cubic control.
    t,T,eps,B=s.symbols('t T eps B',positive=True)
    f=t**3
    zero('central_cubic_error',(f.subs(t,t+T)-f.subs(t,t-T))/(2*T)-s.diff(f,t)-T*T)
    Tstar=(3*eps/B)**s.Rational(1,3)
    zero('baseline_optimum',s.diff(eps/T+B*T*T/6,T).subs(T,Tstar))
    # Same matter metric and measured dust density, distinct supplied actions.
    tau=s.symbols('tau',positive=True)
    zet,YY=s.symbols('zet YY',real=True)
    twins=[]
    for exponent,Fexpr,Vexpr in [
    (s.Rational(1,2),6-s.exp(-6*zet)/2,6*s.exp(-2*zet)-s.exp(-8*zet)/16),
    (s.Rational(1,4),42-2*s.exp(-14*zet),s.Rational(63,8)*s.exp(-6*zet)-s.exp(-20*zet)/16)]:
        aa=tau**exponent; zz=exponent*s.log(tau); aE=tau**2/aa
        dot=lambda f: s.simplify(aa*s.diff(f,tau))
        HE=dot(aE)/aE; dz=dot(zz); Y=dz*dz/2
        rho=tau**(4*exponent-6)/8
        FF=Fexpr.subs(zet,zz); VV=Vexpr.subs(zet,zz)
        equations=[3*HE**2-FF*Y-VV-rho,-2*dot(HE)-2*FF*Y-rho,
           dot(rho)+3*HE*rho-dz*rho,
           FF*dot(dz)+3*HE*FF*dz+s.diff(Fexpr,zet).subs(zet,zz)*Y+s.diff(Vexpr,zet).subs(zet,zz)+rho]
        for i,equation in enumerate(equations): zero(f'twin_{exponent}_equation_{i}',equation)
        zero(f'twin_{exponent}_metric',aa*aE-tau**2)
        zero(f'twin_{exponent}_density',rho/aa**4-tau**-6/8)
        check(f'twin_{exponent}_F_positive',bool(FF.subs(tau,s.Rational(1,2))>0))
        check(f'twin_{exponent}_V_positive',bool((VV*tau**(2-2*exponent)).subs(tau,s.Rational(1,2))>0))
        # Both F and tau^(2-2s)V are increasing on [1/2,1].
        check(f'twin_{exponent}_F_monotone',s.diff(FF,tau).is_positive is True)
        check(f'twin_{exponent}_V_scaled_monotone',s.simplify(s.diff(VV*tau**(2-2*exponent),tau)).is_positive is True)
        twins.append({'s':str(exponent),'F_tau':str(s.simplify(FF)),'V_tau':str(s.simplify(VV)), 'q':str(exponent/tau)})
    check('distinct_scalar_histories',twins[0]['q']!=twins[1]['q'])
    couplings=[s.simplify(1/s.sympify(item['F_tau'],locals={'tau':tau}).subs(tau,1)) for item in twins]
    check('canonical_matter_slopes_distinct',couplings[0]!=couplings[1])
    # Rank-three is not nonidentifiability: intersect the nonlinear constraint.
    bb,kk=s.symbols('bb kk')
    poly=s.Poly(s.expand((1+z)**2*h*h-2*z*(1+z)*h-bb+kk*z*z+z*z),z)
    sol=s.solve(poly.all_coeffs(),[h,bb,kk],dict=True)
    check('rank_three_physical_unique',sol==[{bb:0,h:0,kk:-1},{bb:1,h:1,kk:0}])
    # These are kinematic data, not the perturbation data used by the prior kinetic residual.
    zero('twins_same_drift',2-2*s.sqrt(1+z)/(1+z)-(2-2/s.sqrt(1+z)))
    # Exact tensor variable transformation, separate from its geometric-optics use.
    eta,wave=s.symbols('eta wave',real=True)
    btensor=s.Function('btensor')(eta); mu=s.Function('mu')(eta)
    hmode=mu/btensor
    zero('tensor_canonical_mode',s.diff(hmode,eta,2)+2*s.diff(btensor,eta)/btensor*s.diff(hmode,eta)+wave**2*hmode-(s.diff(mu,eta,2)+(wave**2-s.diff(btensor,eta,2)/btensor)*mu)/btensor)
    for exponent in [s.Rational(1,2),s.Rational(1,4)]:
        X=(1+z)**(-exponent/2)
        qz=-(1+z)*2*s.sqrt(1+z)*s.diff(s.log(X),z)
        zero(f'tensor_q_{exponent}',qz-exponent*s.sqrt(1+z))
        aa=tau**exponent; q=exponent/tau; el=(2-exponent)/tau
        RR=aa**2*tau**-6/8
        Frec=s.simplify((-2*(s.diff(el,tau)+q*el)-RR)/q**2)
        Fgiven=s.sympify(twins[0 if exponent==s.Rational(1,2) else 1]['F_tau'],locals={'tau':tau})
        Vgiven=s.sympify(twins[0 if exponent==s.Rational(1,2) else 1]['V_tau'],locals={'tau':tau})
        Yb=aa**2*q*q/2; Qbar=aa**2*(Frec*q*q+RR-3*el*el)
        Erec=s.simplify((s.diff(Qbar,tau)-Frec*s.diff(Yb,tau))/(aa**2*q))
        Egiven=(s.diff(Fgiven,tau)*Yb-s.diff(Vgiven,tau))/(q*aa**2)
        zero(f'tensor_F_recovery_{exponent}',Frec-Fgiven)
        zero(f'tensor_Q_recovery_{exponent}',Qbar-(Fgiven*Yb-Vgiven))
        zero(f'tensor_E_recovery_{exponent}',Erec-Egiven)
    check('tensor_twins_distinct',s.simplify((1+z)**(-s.Rational(1,4))-(1+z)**(-s.Rational(1,8))).subs(z,1)!=0)
    Xsymbol=s.symbols('Xsymbol',positive=True)
    zero('endpoint_compensation_example',(1/Xsymbol)*Xsymbol-1)
    result={'kind':'constructed exact development controls, not empirical validation','checks':checks,
     'passed':sum(checks.values()),'failed':sum(not q for q in checks.values()),
     'determinant':str(mat.det()),'parameters':[str(x) for x in theta],
     'inverse_error_bound':str(bound),'inverse_actual_error':str(norm(observed-theta)), 'twins':twins}
    root=Path(__file__).resolve().parents[1]
    out=root/'outputs/scalar_background_observations/result.json';out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    for name,ok in checks.items(): print(('PASS' if ok else 'FAIL')+': '+name)
    print(f"TOTAL: PASS={result['passed']} FAIL={result['failed']}")
    raise SystemExit(bool(result['failed']))


if __name__ == '__main__':
    main()
