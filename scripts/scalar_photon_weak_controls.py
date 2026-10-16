"""Exact primitive-record weak identity and constructed error controls."""
AUDIT_TIMEOUT_SEC = 120
import json
import sympy as s

u,r=s.symbols('u r',real=True)
w=1+u-r; a=1/w; h=s.Integer(-1)
expand=s.expand
T=lambda f:expand(w*s.diff(f,u))
L=lambda f:expand(w*(2*s.diff(f,u)+s.diff(f,r)))
Td=lambda f:expand(-T(f)+h*f)
Ld=lambda f:expand(-L(f)+h*f)
Q=lambda f:expand(r*r*s.diff(f,r)/2)
Qd=lambda f:expand(-s.diff(r*r*f,r)/2)
R=lambda f:expand(s.diff(r*r*s.diff(f,r),r)/2)
lam=expand((u*(1-u)*r*(s.Rational(1,2)-r))**6)
theta=[1+s.Rational(i,10)*u+s.Rational(15-i,20)*r+s.Rational(i%3,30)*u*r for i in range(1,15)]
psi=expand(w*w*(u*u+r**3+u*r)); z=u**3+2*r*r
checks=[]
def check(name,condition):checks.append({'name':name,'pass':bool(condition)})
def integral(f):
    p=s.Poly(s.cancel(f),u,r)
    return sum(c*s.Rational(1,2)**(j+1)/((i+1)*(j+1)) for (i,j),c in p.terms())
def compose(op,f,n):
    for _ in range(n):f=op(f)
    return f
def weights(td=Td,ld=Ld,qd=Qd,wrong_order=False):
    hw=(ld(td(lam)) if wrong_order else td(ld(lam)))+ld((h+theta[1])*lam)+td(theta[0]*lam)+(T(h)+theta[2])*lam
    hx=td(ld(ld(theta[3]*lam)))+td(ld(theta[4]*lam))+td(theta[5]*lam)+ld(ld(theta[6]*lam))+ld(theta[7]*lam)+theta[8]*lam+td(td(theta[9]*lam))
    hb=compose(td,theta[10]*lam,3)+td(td(theta[11]*lam))+td(theta[12]*lam)+theta[13]*lam
    hp=s.cancel(R(hx)+qd(a*hb-2*s.diff(hw,u)))
    return expand(hw),hp
def residual(p,zv):
    X=R(p);B=s.cancel(a*Q(p));W=expand(zv+2*s.diff(Q(p),u))
    aw=L(T(W))+(h+theta[1])*L(W)+theta[0]*T(W)+(T(h)+theta[2])*W
    ax=theta[3]*L(L(T(X)))+theta[4]*L(T(X))+theta[5]*T(X)+theta[6]*L(L(X))+theta[7]*L(X)+theta[8]*X+theta[9]*T(T(X))
    ab=theta[10]*T(T(T(B)))+theta[11]*T(T(B))+theta[12]*T(B)+theta[13]*B
    return expand(aw+ax+ab)

def run_checks():
    checks.clear()
    # Integrate strong and adjoint sides separately on a nonzero witness.
    probe=u**3+r**2+u*r
    for name,op,adj in [('time',T,Td),('characteristic',L,Ld),('path',Q,Qd),('lensing',R,R)]:
        check('adjoint_'+name,integral(lam*op(probe))==integral(adj(lam)*probe))
    for var,ends in [(u,[0,1]),(r,[0,s.Rational(1,2)])]:
        check('vanishing_boundary_traces_'+str(var),all(s.diff(lam,var,j).subs(var,end)==0 for j in range(6) for end in ends))
    hw,hp=weights();strong=integral(lam*residual(psi,z));weak=integral(hw*z+hp*psi)
    check('nonzero_operator_witness',strong!=0)
    check('complete_primitive_identity',strong==weak)
    mutations={}
    for name,kwargs in [('missing_divergence',{'td':lambda f:-T(f),'ld':lambda f:-L(f)}),('wrong_composition_order',{'wrong_order':True}),('path_adjoint_sign',{'qd':lambda f:-Qd(f)})]:
        mw,mp=weights(**kwargs);difference=integral(mw*z+mp*psi)-strong
        check('detected_'+name,difference!=0);mutations[name]=str(difference)

    # w in [1/2,2]. hp*w^2 is polynomial; this supplies a conservative exact
    # L2-duality bound for every pointwise-bounded primitive error on the rectangle.
    weighted_hp=s.cancel(hp*w*w);s.Poly(weighted_hp,u,r)
    normsum=integral(hw*hw)+integral(weighted_hp*weighted_hp)
    epsz=s.Rational(1,10**6);epsp=s.Rational(1,10**6)
    bound_squared=s.Rational(1,2)*(epsz**2+16*epsp**2)*normsum
    noise=[]
    for n in [1,2,4,8]:
        dp=expand(epsp*w*w*(2*u-1)**n*(4*r-1)**n/4)
        dz=expand(epsz*(2*u-1)**n)
        delta=integral(hw*dz+hp*dp)
        direct=integral(lam*residual(dp,dz))
        check('perturbation_identity_'+str(n),delta==direct)
        check('primitive_error_bound_'+str(n),bound_squared-delta*delta>=0)
        noise.append({'degree':n,'weak_error_exact':str(delta),'strong_equals_weak':delta==direct,
            'bound_squared_exact':str(bound_squared),'error_over_bound':str(s.N(abs(delta)/s.sqrt(bound_squared),16)),
            'third_u_derivative_at_upper_corner':str(s.diff(dp,u,3).subs({u:1,r:s.Rational(1,2)}))})
    record={'scope':'Exact operator identity and bounded primitive-error controls; arbitrary coefficient witness is not a scalar solution or empirical data.',
        'passed':sum(c['pass'] for c in checks),'failed':sum(not c['pass'] for c in checks),'checks':checks,
        'strong_residual_exact':str(strong),'weak_residual_exact':str(weak),'mutations':mutations,
        'noise_cases':noise,'bound_scope':'At each fixed smooth candidate and compact test. Finite moment uniqueness, quadrature enclosure, empirical noise and candidate-family-uniform bounds are not established.'}
    return checks, {k:v for k,v in record.items() if k not in {'checks','passed','failed'}}
