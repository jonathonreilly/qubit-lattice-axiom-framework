"""Root exact unequal-distance controls; not an empirical test."""
from pathlib import Path
import hashlib
import json
import sympy as s



def controls():
    A, B, r, n = s.symbols('A B r n', positive=True)
    delta = A*A-B*B
    mu = (A*A+B*B-r*r)/(2*A*B)
    p1, p2 = (B*mu-A)/r, (B-A*mu)/r
    gamma = s.factor((mu-p1*p2)/(p1*p2*r))
    U = s.factor(s.diff(gamma, A))
    P = lambda f: s.diff(f,r)+gamma*f
    L = lambda f: U*P(f)-s.diff(U,r)*f
    W = (r*r-delta)**6*(r*r+delta)**4/r**4
    rows = []
    def check(name, expression, nonzero=False):
        q = s.factor(expression)
        passed = bool(q != 0) if nonzero else bool(q == 0)
        rows.append({'name':name,'passed':passed,'residual':str(q)})

    check('radial_product',p1*p2-(delta**2-r**4)/(4*A*B*r*r))
    check('gamma_rational',gamma-(2*r*r*(A*A+B*B)-r**4-delta**2)/(r*(delta**2-r**4)))
    check('fixed_r_angle_derivative',s.diff(mu,A)-(A*A-B*B+r*r)/(2*A*A*B))
    check('lowmode_constant_basis',1/p2-2*B*r/(r*r-delta))
    check('lowmode_dipole_basis',mu/p2-(2*B*B*r/(A*(r*r-delta))-r/A))
    check('time_derivative_extra_basis',s.diff(r/(r*r-delta),A)-2*A*r/(r*r-delta)**2)

    # Direct Cartesian contraction checks; no radial-projection formula supplies
    # the independently differentiated Cartesian covariance.
    x=s.symbols('x0:3'); z=s.symbols('z0:3')
    d2=sum((z[i]-x[i])**2 for i in range(3))
    for k,(aa,bb,cc,ss) in enumerate([(2,3,s.Rational(3,5),s.Rational(4,5)),
                                      (3,2,s.Rational(5,13),s.Rational(12,13)),
                                      (2,2,s.Rational(-3,5),s.Rational(4,5))]):
        nn1=[1,0,0]; nn2=[cc,ss,0]
        at={**{x[i]:aa*nn1[i] for i in range(3)},**{z[i]:bb*nn2[i] for i in range(3)}}
        rr=s.sqrt(aa*aa+bb*bb-2*aa*bb*cc)
        pp1=(bb*cc-aa)/rr; pp2=(bb-aa*cc)/rr
        for degree in [2,4,6,8]:
            f=d2**(degree//2)
            c=sum(nn2[i]*s.diff(f,z[i]) for i in range(3)).subs(at)
            v=sum(nn1[i]*nn2[j]*s.diff(f,x[i],z[j]) for i in range(3) for j in range(3)).subs(at)
            check(f'cartesian_cross_{k}_{degree}',c-pp2*degree*rr**(degree-1))
            check(f'cartesian_auto_{k}_{degree}',v+pp1*pp2*degree*(degree-1)*rr**(degree-2)+(cc-pp1*pp2)*degree*rr**(degree-2))

    # Generic functions establish the differential identities without the
    # geometric formula for gamma or any selected covariance.
    g=s.Function('g')(n,r); rr=s.Function('R')(n,r)
    y=s.Function('y')(n); c=s.Function('c')(n)
    pg=lambda f:s.diff(f,r)+g*f
    t=lambda f:y*s.diff(f,n)+c*f
    kap=y*s.diff(g,n)
    ff=t(pg(rr))-pg(t(rr))
    check('generic_commutator',s.expand(ff-kap*rr))
    check('generic_spatial_constraint',s.expand(kap*pg(ff)-s.diff(kap,r)*ff-kap*kap*pg(rr)))
    check('generic_temporal_constraint',s.expand(kap*t(ff)-y*s.diff(kap,n)*ff-kap*kap*t(rr)))

    polynomials=[]
    for i,f in enumerate([r,r/(r*r-delta),r/(r*r-delta)**2]):
        raw=s.factor(W*L(P(f)))
        poly=s.Poly(raw,r)
        assert all(power[0]%2==0 and power[0]<=12 for power,_ in poly.terms())
        out=raw
        for j in range(7): out=s.expand(r*s.diff(out,r)-2*j*out)
        check(f'lowmode_annihilator_{i}',out)
        polynomials.append({'basis':str(f),'polynomial':str(raw),'degree_r':poly.degree()})

    # A nonzero sensitivity witness in the smooth correlation-function space.
    # This witness is not asserted to be a positive covariance or a full solution.
    response=s.cancel(W*L(P(r**19)))
    for j in range(7): response=s.expand(r*s.diff(response,r)-2*j*response)
    check('operator_not_identically_zero',response.subs({A:2,B:3,r:s.Rational(5,2)}),nonzero=True)
    check('geometry_U_not_identically_zero',U.subs({A:2,B:3,r:s.Rational(5,2)}),nonzero=True)

    # Positive covariance nonvacuity: g(x)=sqrt(2)cos(k.x+theta), with
    # theta uniform and k Gaussian N(0,2*t I), has C(r)=exp(-t*r^2).
    # V=f(N)g, S=s(N)g solves the admitted local law if s'-a0*s=y*f'+c0*f.
    # Shifting the tested c0 by dc changes H by dc*L P R, R=C_r*f1*f2.
    # The leading polynomial coefficient below also follows from U~-4A/r^3,
    # W~r^16 and R''~-8t^3*r^3*exp(-t*r^2).
    rate=s.symbols('rate', positive=True)
    ex=s.exp(-rate*r*r)
    Pe=lambda f:s.diff(f,r)+(gamma-2*rate*r)*f
    Le=lambda f:U*Pe(f)-s.diff(U,r)*f
    base=s.factor(W*Le(Pe(-2*rate*r)))
    gp=s.Poly(base,r)
    check('PSD_gaussian_leading_degree',gp.degree()-16)
    check('PSD_gaussian_leading_coefficient',gp.LC()-32*A*rate**3)
    response_gauss=base
    for j in range(7):
        response_gauss=s.expand(r*s.diff(response_gauss,r)-2*rate*r*r*response_gauss-2*j*response_gauss)
    gfinal=s.Poly(response_gauss,r)
    check('PSD_annihilated_response_degree',gfinal.degree()-30)
    check('PSD_annihilated_response_leading',gfinal.LC()+4096*A*rate**10)
    check('PSD_response_in_chart',response_gauss.subs({A:2,B:3,r:s.Rational(5,2),rate:s.Rational(1,2)}),nonzero=True)

    result={'scope':'Exact conditional geometry and annihilator controls; no empirical test, parameter-identification or PSD sufficiency claim',
            'checks':rows,'annihilator_polynomials':polynomials,
            'expressions':{'gamma':str(gamma),'U':str(U),'W':str(W)},
            'positive_covariance_witness':{'base_polynomial':str(base),'response_polynomial':str(response_gauss),'scope':'A bounded homogeneous isotropic covariance witness for local-law sensitivity, not a full gravitational solution or selected cosmic initial state'},
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    return result
