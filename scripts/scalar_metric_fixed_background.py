"""Conditional scalar/metric controls; constructed inputs, no file or network I/O."""
AUDIT_TIMEOUT_SEC = 120

def run_checks():
    import hashlib

    import json

    import pathlib

    import sympy as s

    r,tau,mu=s.symbols('r tau mu',positive=True)

    C,Lam=s.symbols('C Lambda',real=True)

    W=s.Function('W')(r,mu)

    checks=[]

    details={}

    def check(name,expr,zero=True):
        out=s.factor(s.simplify(expr))
        checks.append({'name':name,'pass':(out==0)==zero,'expected_zero':zero,'residual':str(out)})

    ang=lambda f:s.diff((1-mu*mu)*s.diff(f,mu),mu)

    lap=lambda f:s.diff(f,r,2)+2*s.diff(f,r)/r+ang(f)/r**2

    fr=s.diff(W,r)-C*W

    gr=lap(W)-Lam*W

    D=Lam-C*C-C/r

    comm=lap(s.diff(W,r))-s.diff(lap(W),r)

    check('general_spherical_commutator',comm-2*s.diff(W,r)/r**2-2*ang(W)/r**3)

    Nr=(r/2)*(lap(fr)-Lam*fr-s.diff(gr,r)+C*gr)-gr+C*fr+s.diff(fr,r)+fr/r

    check('general_local_reconstruction_identity',Nr-D*W)

    check('exceptional_denominator_simple_radial_zero',s.diff(D,r)-C/r**2)

    check('general_compatibility_residual_identity',
          lap(fr)-Lam*fr-s.diff(gr,r)+C*gr-comm)

    check('dropping_spherical_curvature_changes_inverse',C*W/r,False)

    check('wrong_commutator_sign_changes_inverse',r*comm,False)

    a,h,q,b,x,R,kappa,Fbar=s.symbols('a h q b x R kappa Fbar',nonzero=True)

    ell=h-q

    p,p1,p2,lp,w,w1,w2,lw,delta=s.symbols('p p1 p2 lp w w1 w2 lw delta')

    Kres=w2+(3*h-2*q)*w1-lw/a**2+kappa*w+b*R*delta-4*x*p1+2*Fbar*p

    Hres=R*delta-(2*lp/a**2-6*ell*(p1+ell*p)-x*w1+x*x*p-Fbar*w)

    HP=(6*b*ell+4*x)*p1-2*b*lp/a**2+(6*b*ell**2-b*x*x-2*Fbar)*p

    C2=w2+3*ell*w1-lw/a**2+(kappa-b*Fbar)*w-HP

    check('scalar_hamiltonian_source_elimination',(Kres-b*Hres-C2).subs(q,b*x))

    Ct,Ft,G,Lb,ht=s.symbols('Ct Ft G Lb h_tau')

    source=(2*p2+(8*h-6*q)*p1+(4*ht+6*h*h-Ct)*p)/x

    nu=-Lb-Ft/G

    trace=2*p2+8*h*p1+(4*ht+6*h*h)*p-(6*q*p1+Ct*p+G*b*(w1+Lb*w)+Ft*b*w)

    check('trace_to_hidden_scalar_source',(trace+x*(w1-nu*w-source)).subs(G,x/b))

    nudot,sdot,ss=s.symbols('nu_tau S_tau S')

    nus=s.symbols('nu')

    Lambda=a*a*(nudot+nus*nus+3*ell*nus+kappa-b*Fbar)

    gg=a*a*(sdot+(nus+3*ell)*ss-HP)

    eliminated=C2.subs({w1:nus*w+ss,w2:(nudot+nus*nus)*w+nus*ss+sdot})

    check('trace_scalar_to_elliptic_identity',a*a*eliminated+lw-Lambda*w-gg)

    pr,p1r,wr,rz=s.symbols('p_r p1_r w_r Rz')

    redshift=-p-b*w+(x*wr-2*(p1r+ell*pr))/(a*R)

    f=(a*R/x)*(rz+p)+(2/x)*(p1r+ell*pr)

    check('momentum_redshift_to_radial_identity',
          (wr-a*R*b*w/x-f).subs(rz,redshift))

    m=s.Rational(1,5)

    Y=s.factor((8*m*m+12*m+3)/(2*m+3))

    z=m*(m+1)

    k2=s.factor(4*z*(8*z+9)/(3-8*z))

    l=s.Integer(2)

    rad=s.Function('B')(r)

    P=tau**m*rad

    wfield=Y*P

    aa=2*tau

    hh=1/tau

    bb=s.Integer(1)

    xx=1/(2*tau)

    RR=1/(4*tau*tau)

    qq=xx

    ellv=hh-qq

    kv=s.Rational(7,4)/tau**2

    Fb=-1/(2*tau*tau)

    Gv=xx

    Ctv=s.Rational(5,4)/tau**2

    Ftv=s.Rational(3,4)/tau**2

    nuv=-Ftv/Gv

    Cv=s.simplify(aa*RR*bb/xx)

    Lv=s.simplify(aa**2*(s.diff(nuv,tau)+nuv*nuv+3*ellv*nuv+kv-bb*Fb))

    details.update({'C':str(Cv),'Lambda':str(Lv),'nu':str(nuv),'m':str(m),'Y':str(Y),'k2':str(k2)})

    check('witness_C',Cv-1)

    check('witness_Lambda',Lv-15)

    radlap=lambda fn:s.diff(fn,r,2)+2*s.diff(fn,r)/r-l*(l+1)*fn/r**2

    radode=-2*s.diff(rad,r)/r-(k2-l*(l+1)/r**2)*rad

    rules={s.diff(rad,r,2):radode}

    for order in range(3,6):
        rules[s.diff(rad,r,order)]=s.diff(rules[s.diff(rad,r,order-1)],r).subs(rules)

    def reduce_rad(expr):
        for order in range(5,1,-1):expr=expr.subs(s.diff(rad,r,order),rules[s.diff(rad,r,order)])
        return s.factor(s.simplify(expr))

    S=(2*s.diff(P,tau,2)+(8*hh-6*qq)*s.diff(P,tau)+(4*s.diff(hh,tau)+6*hh**2-Ctv)*P)/xx

    HPv=(6*bb*ellv+4*xx)*s.diff(P,tau)-2*bb*radlap(P)/aa**2+(6*bb*ellv**2-bb*xx**2-2*Fb)*P

    gv=reduce_rad(aa**2*(s.diff(S,tau)+(nuv+3*ellv)*S-HPv))

    Vv=(Y-4*m-2)*P

    Rz=-P-wfield+s.diff(Vv,r)

    fv=s.simplify((aa*RR/xx)*(Rz+P)+(2/xx)*s.diff(s.diff(P,tau)+ellv*P,r))

    check('witness_trace_source',s.diff(wfield,tau)-nuv*wfield-S)

    check('witness_elliptic_source',reduce_rad(radlap(wfield)-Lv*wfield-gv))

    check('witness_radial_source',s.diff(wfield,r)-Cv*wfield-fv)

    check('witness_full_matter_euler',s.diff(Vv,tau)*aa+2*Vv+P+wfield)

    Nv=reduce_rad((r/2)*(radlap(fv)-Lv*fv-s.diff(gv,r)+Cv*gv)-gv+Cv*fv+s.diff(fv,r)+fv/r)

    Dv=Lv-Cv*Cv-Cv/r

    check('witness_reconstruction',Nv-Dv*wfield)

    rstar=s.Rational(1,14)

    check('compatible_exceptional_radius_numerator',Nv.subs(r,rstar))

    check('compatible_exceptional_radius_derivative',
          (s.diff(Nv,r)-s.diff(Dv,r)*wfield).subs(r,rstar))

    kr=s.sqrt(k2)*r

    j2=(3/kr**3-1/kr)*s.sin(kr)-3*s.cos(kr)/kr**2

    check('regular_radial_helmholtz_completion',radlap(j2)+k2*j2)

    check('origin_regular_radial_limit',s.limit(j2/r**2,r,0)-k2/15)

    ghost=tau**(-s.Rational(3,2))*s.exp(r)

    check('annular_null_candidate_trace',s.diff(ghost,tau)-nuv*ghost)

    check('annular_null_candidate_radial',s.diff(ghost,r)-Cv*ghost)

    reject=s.factor(radlap(ghost)-Lv*ghost)

    check('annular_null_candidate_rejected_by_field',reject,False)

    details['annular_candidate_failure_ratio']=str(s.factor(reject/ghost))

    return checks, details
