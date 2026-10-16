"""Exact Green identities and a moving-geometry polynomial weak-form fixture."""
import sympy as s


def controls():
    N, r = s.symbols('N r', real=True)
    chi = s.Function('chi')(N)
    f, w = s.Function('f')(N, r), s.Function('w')(N, r)
    K = lambda z: r*s.diff(z, r)
    D = lambda z: s.diff(z, r)/r
    alpha = r*r/(4*chi*chi)
    E = lambda z: alpha*(K(z)+2*z)-z
    Es = lambda z: -alpha*r*s.diff(z, r)-(alpha+1)*z
    Ds = lambda z: -s.diff(z/r, r)
    checks = []
    def add(name, value, **kw):
        checks.append({'name': name, 'passed': bool(value), **kw})
    def zero(z): return s.cancel(s.expand(z)) == 0
    add('E_Green_identity', zero(w*E(f)-f*Es(w)-s.diff(alpha*r*w*f, r)))
    add('D_Green_identity', zero(w*D(f)-f*Ds(w)-s.diff(w*f/r, r)))
    add('K_Green_identity', zero(w*K(f)-f*(-K(w)-w)-s.diff(r*w*f, r)))
    def P(z):
        for shift in [-4, -2, 0, 2]: z=s.expand(K(z)+shift*z)
        return z
    def Ps(z):
        for shift in [-1, 1, 3, 5]: z=s.expand(K(z)+shift*z)
        return z
    # A distinct exact 2D fixture. It is algebraic, not a physical covariance.
    # chi=(1+N)^(-1/2), a=e^N, H=2e^-N(1+N)^(3/2) satisfy chi_N=-1/(aH).
    alpha = (1+N)*r*r/4
    E = lambda z: s.expand(alpha*(K(z)+2*z)-z)
    Es = lambda z: s.expand(-alpha*r*s.diff(z, r)-(alpha+1)*z)
    g = 1/(1+N)
    x, y, m = N*N, (1+N)*(1+N*N), 1+N**3
    h = -1+s.Rational(3,2)/(1+N)
    a0, c0 = (y-x-2)/2, -h*y-m
    w = N**2*(1-N)**2*(r-s.Rational(1,2))**8*(1-r)**8
    SS = 1+N*r**3+N**2*r**8+r**10
    d = N**3+r**5+N*r**2
    U = N*r**4+r**9+N**2
    A, A1 = P(E(E(D(SS)))), P(E(E(D(s.diff(SS,N)))))
    B, B1 = P(E(E(d))), P(E(E(s.diff(d,N))))
    C, C1 = P(E(U)), P(E(s.diff(U,N))-g*(E(U)+U))
    strong = (A1-2*y*B1+y*y*C1)/2-a0*A-(c0-a0*y)*B+c0*y*C
    pw=Ps(w); ls=Es(Es(pw)); qs=Ds(ls); ep=Es(pw)
    kSS=-s.diff(qs,N)/2-a0*qs
    kd=s.diff(y*ls,N)-(c0-a0*y)*ls
    kU=-s.diff(y*y*ep/2,N)-y*y*g*(ep+pw)/2+c0*y*ep
    weak=kSS*SS+kd*d+kU*U
    # Exact integration of polynomial coefficients avoids a symbolic antiderivative heuristic.
    def integrate(poly):
        terms=s.Poly(s.cancel(s.expand(poly*r*r)),N,r).terms()
        return s.simplify(sum(coeff/s.Integer(i+1)*
                   (s.log(2) if j==1 else (1-s.Rational(1,2)**(j-1))/s.Integer(j-1))
                   for (i,j),coeff in terms))
    left, right=integrate(w*strong),integrate(weak)
    add('two_dimensional_weighted_identity', left==right,
        strong_integral=str(left), weak_integral=str(right))
    wrong_g=integrate(y*y*g*(ep+pw)*U/2)
    wrong_y=integrate(s.diff(y,N)*ls*d-s.diff(y*y,N)*ep*U/2)
    add('geometry_correction_is_detected', wrong_g!=0, wrong_residual=str(wrong_g))
    add('coefficient_time_variation_is_detected', wrong_y!=0, wrong_residual=str(wrong_y))
    # Finite-regularity alternative is a fixed rectangle; all endpoint terms vanish here.
    add('fixed_rectangle_boundary_jets', all(
        s.simplify(s.diff(w,r,j).subs(r,b))==0 for b in [s.Rational(1,2),1] for j in range(7))
        and all(s.simplify(s.diff(w,r,j).subs(N,b))==0 for b in [0,1] for j in range(8)))
    return {'checks':checks,'scope':'Exact Green identities and arbitrary polynomial test functions; no empirical inputs or covariance-positivity assertion'}
