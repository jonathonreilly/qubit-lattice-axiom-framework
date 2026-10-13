"""R17-11 forks: can a unimodular-type receiver (Lambda(x) fed by the exchange, R5-3 route 1) absorb Q = div(W h) instead of E?
Unimodular Bianchi needs kappa*Q_nu = d_nu Lambda: Q must be closed (dQ = 0, a gradient) -- cf. R4-4 Lemma K.
Check (sympy, spherical metric as r1711_lemmaV_general, W = const): Q_t, Q_r (lower) and dQ_{tr} = d_t Q_r - d_r Q_t.
FRW control: Q = -3 H W dt is closed, but then Lambda(t) = Lambda0 + kappa*int 3 H W dt drifts by 3 kappa W per e-fold.
"""
import sympy as sp
t, r = sp.symbols('t r', real=True)
N = sp.Function('N')(t, r); A = sp.Function('A')(t, r); B = sp.Function('B')(t, r)
W = sp.symbols('W', positive=True)
theta = sp.diff(sp.log(A*B**2), t)/N
# lower components: n_nu = (-N, 0, 0, 0); a_nu = (0, d_r ln N, 0, 0); Q_nu = W (a_nu + theta n_nu)
Qt = W*theta*(-N)
Qr = W*sp.diff(sp.log(N), r)
curl = sp.simplify(sp.diff(Qr, t) - sp.diff(Qt, r))
print("Q_t =", sp.simplify(Qt), ";  Q_r =", sp.simplify(Qr))
print("dQ_tr = d_t Q_r - d_r Q_t =", curl)
# generic numeric test
sub = {N: 1 + sp.Rational(1, 10)*r**2*t, A: t**sp.Rational(2, 3)*(1 + r**2/10), B: r*t**sp.Rational(2, 3)}
c2 = sp.simplify(sp.diff(Qr.subs(sub), t) - sp.diff(Qt.subs(sub), r))
print("dQ_tr on a sample inhomogeneous lapse/metric (W=1):", sp.simplify(c2.subs(W, 1)), " at t=1,r=1:", sp.N(c2.subs({W: 1, t: 1, r: 1})))
# FRW: N=1, A=a(t), B=r a(t)
a = sp.Function('a')(t)
cF = sp.simplify(sp.diff(Qr.subs({N: 1, A: a, B: r*a}).doit(), t) - sp.diff(Qt.subs({N: 1, A: a, B: r*a}).doit(), r))
print("FRW control dQ_tr =", cF, "; Q_t =", sp.simplify(Qt.subs({N: 1, A: a, B: r*a}).doit()), "-> Lambda' = kappa*Q_t-type drift 3 H W per unit time")
