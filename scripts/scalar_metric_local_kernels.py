"""Attributed local-kernel and geometry controls; no observational input."""
AUDIT_TIMEOUT_SEC = 120
import sympy as s


def run_checks():
    checks=[]

    def ck(name,expr,zero=True):
        value=s.factor(s.simplify(expr))
        checks.append({'name':name,'pass':(value==0)==zero,
                       'expected_zero':zero,'residual':str(value)})

    X,Y,Z,r,mu,t=s.symbols('X Y Z r mu tau',real=True,positive=True)

    c0,c1,c2,c3,c4=s.symbols('c0 c1 c2 c3 c4',real=True)

    chi=c0+c1*X+c2*Y+c3*Z+c4*(X**2+Y**2+Z**2)

    lapxyz=lambda f:sum(s.diff(f,z,2) for z in (X,Y,Z))

    for i,v in enumerate((X,Y,Z)):
        for j,w in enumerate((X,Y,Z)):
            if j>=i:ck(f'traceless Hessian kernel component {i}{j}',
                        s.diff(chi,v,w)-(lapxyz(chi)/3 if i==j else 0))

    h,q,x,xp,R,G=s.symbols('h q x xp R G',nonzero=True)

    C=R/G

    transport=2*q-3*h

    Fbar=-xp-(3*h-2*q)*x

    coefficient=-(transport-xp/x-C)-Fbar/x

    ck('Hamiltonian hidden velocity coefficient',coefficient-(6*h-4*q+2*xp/x+C))

    lam,Q,ss0,ss1,ss2=s.symbols('lambda Q s0 s1 s2',nonzero=True)

    ang=lambda f:s.diff((1-mu**2)*s.diff(f,mu),mu)

    lap=lambda f:s.diff(f,r,2)+2*s.diff(f,r)/r+ang(f)/r**2

    source=ss2*r*r+ss1*mu*r+ss0

    part=-ss2*r*r/lam-(2*ss2/lam**2+ss1*mu/lam)*r-(2*ss2/lam**3+ss1*mu/lam**2+ss0/lam)

    ck('polynomial-source radial particular solution',s.diff(part,r)-lam*part-source)

    At,ft,af=s.symbols('At f angular_f')

    e=s.exp(lam*r)*(At*r*r*ft+2*lam*r*ft+af)

    five=s.expand(s.diff(e,r,5)/s.exp(lam*r))

    pol=s.Poly(five,r)

    ck('fifth derivative leading exponential coefficient',pol.coeff_monomial(r*r)-lam**5*At*ft)

    ck('fifth derivative removes resonant spectral exception',
       pol.coeff_monomial(r)-10*pol.coeff_monomial(r*r)/lam-2*lam**6*ft)

    tt0,tt1,tt2=s.symbols('t0 t1 t2')

    T=tt0+tt1*mu*r+tt2*r*r

    polpart=s.expand(r*r*(lap(part)+Q*part-T))

    ck('polynomial forcing killed by five radial derivatives',s.diff(polpart,r,5))

    ck('forbidden inverse-square radial coefficient',polpart.coeff(r,0)-2*ss1*mu/lam**2)

    ck('forbidden inverse-radius coefficient',polpart.coeff(r,1)+4*ss2/lam**2)

    ck('surviving velocity potential is spatially constant',
       s.diff(part.subs({ss1:0,ss2:0}),r))

    cc,Lambda=s.symbols('C Lambda',nonzero=True)

    W=s.Function('W')(r,mu)

    f=s.diff(W,r)-cc*W

    g=lap(W)-Lambda*W

    D=Lambda-cc*cc-cc/r

    N=(r/2)*(lap(f)-Lambda*f-s.diff(g,r)+cc*g)-g+cc*f+s.diff(f,r)+f/r

    candidate=r*r*(s.diff(N,r)-cc*N-D*f)/cc

    ck('root reconstruction avoids exceptional D denominator',candidate-W)

    a=2*t

    h=1/t

    b=s.Integer(1)

    x=1/(2*t)

    q=b*x

    ell=h-q

    R=1/(4*t*t)

    Fbar=-1/(2*t*t)

    kappa=s.Rational(7,4)/t**2

    zvel=t**(-s.Rational(1,2))*s.exp(Z+s.sqrt(14)*X)

    w=zvel/(2*t)

    J=w

    P=s.Integer(0)

    delta=5*w

    ck('planar mode momentum',2*(s.diff(P,t)+ell*P)-x*w+R*zvel)

    ck('planar mode Hamiltonian',R*delta-(2*lapxyz(P)/a**2-6*ell*(s.diff(P,t)+ell*P)-x*s.diff(w,t)+x*x*P-Fbar*w))

    ck('planar mode Euler',s.diff(zvel,t)+P+J)

    ck('planar mode bare continuity',s.diff(delta,t)-3*s.diff(P,t)+lapxyz(zvel)/a**2)

    ck('planar mode uneliminated scalar',s.diff(w,t,2)+(3*h-2*q)*s.diff(w,t)-lapxyz(w)/a**2+kappa*w+b*R*delta-4*x*s.diff(P,t)+2*Fbar*P)

    ck('planar mode spatial pressure trace',2*s.diff(P,t,2)+2*(q+4*ell)*s.diff(P,t)+(4*s.diff(ell,t)+4*q*ell+6*ell**2+x*x)*P-x*s.diff(w,t)+(Fbar-b*R)*w)

    ck('planar mode corrected planar redshift zero',-J+s.diff(zvel,Z)/a)

    radial=(X*s.diff(zvel,X)+Y*s.diff(zvel,Y)+Z*s.diff(zvel,Z))/s.sqrt(X*X+Y*Y+Z*Z)

    ck('planar mode fails actual spherical radial redshift',(-J+radial/a).subs({X:1,Y:1,Z:1}),False)
    return checks, {"scope": "Post-independent root integration; full-action planar witness and local spherical uniqueness"}
