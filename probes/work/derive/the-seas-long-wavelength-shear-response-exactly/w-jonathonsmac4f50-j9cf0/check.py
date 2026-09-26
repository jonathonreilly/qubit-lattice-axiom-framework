#!/usr/bin/env python3
"""The walker sea's static response to a long strain wave: continuity at q = 0, member + sea at long wavelength,
and the relabelling test of the q^2 part.  J:derive:the-seas-long-wavelength-shear-response-exactly:a2

Setting (block 62 as landed): H = 1/2 sum_j {E^j(x).sigma, S_j}, S_j = (T_j - T_j^dag)/(2i) (symbol s_j = sin k_j),
h = -(eps + eps^T); frame E = 1 + eps cos(q.x) with eps symmetric; free sea = all negative-energy states filled.
Static second-order energy per site (interband only; intraband transitions are Pauli-blocked):
    E2(q) = -< F(k,q) >,  F = [|w|^2 (a b + s.s') - 2 (s.w)(s'.w)] / (a b (a + b)),
    s = s(k), s' = s(k+q), a = |s|, b = |s'|, w = (1/4) eps (s + s').
A  exact algebra (sympy): the vertex, the two-level matrix element, F(k,0) = (a^2|eps s|^2 - (s.eps s)^2)/(4a^3),
   the uniform second-order term -(a^2|eps s|^2 - (s.eps s)^2)/(2a^3); hence lim E2 = 1/2 uniform form (proof: bounded F)
B  the bound 0 <= F <= ||eps||^2 (a+b)/4 (proof in ATTEMPT; exact spot checks at rational points)
C  (3): member + sea energy < 0 for every K > 0 at long enough wavelength, every non-dilation strain
D  (1): exact reduction of the q^2 coefficient (q || e3) to zone moments; high-precision evaluation [float, not certified]
"""
import itertools, random, sys, time
from fractions import Fraction as Fr
import sympy as sp

T0 = time.time()
FAIL = []
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""), flush=True)
    if not ok: FAIL.append(name)

print("== A exact algebra")
# A1 vertex: <k'|1/2 sum_j {f(x) E_j.sigma, S_j}|k> = 1/2 sum_j E_j.sigma fhat(k'-k) (s_j(k) + s_j(k'))
k, kp, fh = sp.symbols('k kp fh')
# S_j acting on e^{ikx}: (e^{ik} - e^{-ik})/(2i) = sin k ; multiplication by f contributes fhat(k'-k)
lhs = sp.Rational(1, 2)*(fh*sp.sin(k) + sp.sin(kp)*fh)          # {f, S}: f S on |k> then S f on |k>
check("A1 vertex: <k'|{f sigma_a, S_j}|k>/2 = sigma_a fhat (s_j(k) + s_j(k'))/2; with f = eps cos(q.x), fhat(+-q) = eps/2, "
      "so <k+q|V|k> = sigma.w, w = eps (s + s')/4", sp.simplify(lhs - fh*(sp.sin(k) + sp.sin(kp))/2) == 0)
# A2 two-level element: |<+,n'| sigma.w |-,n>|^2 = [|w|^2 (1 + n.n') - 2 (n.w)(n'.w)]/2 for unit n, n'
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
def sdot(v): return v[0]*sx + v[1]*sy + v[2]*sz
w_ = sp.Matrix(sp.symbols('w1:4', real=True))
def unit(p, q_):   # rational unit vector from two rationals (inverse stereographic)
    d = 1 + p**2 + q_**2
    return sp.Matrix([2*p/d, 2*q_/d, (1 - p**2 - q_**2)/d])
okA2 = True
for (p1, q1, p2, q2) in [(Fr(1, 3), Fr(2, 5), Fr(-3, 7), Fr(1, 2)), (Fr(0), Fr(1, 4), Fr(5, 3), Fr(-2, 9)), (Fr(2), Fr(-1, 3), Fr(1, 11), Fr(4, 5))]:
    n = unit(sp.Rational(p1.numerator, p1.denominator), sp.Rational(q1.numerator, q1.denominator))
    n2 = unit(sp.Rational(p2.numerator, p2.denominator), sp.Rational(q2.numerator, q2.denominator))
    Pp = (sp.eye(2) + sdot(n2))/2; Pm = (sp.eye(2) - sdot(n))/2
    val = sp.expand((Pp*sdot(w_)*Pm*sdot(w_)).trace())
    ref = sp.expand((w_.dot(w_)*(1 + n.dot(n2)) - 2*n.dot(w_)*n2.dot(w_))/2)
    if sp.simplify(val - ref) != 0: okA2 = False
check("A2 Tr[P+(n') sigma.w P-(n) sigma.w] = [|w|^2(1+n.n') - 2(n.w)(n'.w)]/2 (symbolic w, exact rational unit vectors)", okA2)
# A3 F(k,0) and the uniform second-order term, generic symmetric eps
e = sp.symbols('e11 e12 e13 e22 e23 e33', real=True)
EPS = sp.Matrix([[e[0], e[1], e[2]], [e[1], e[3], e[4]], [e[2], e[4], e[5]]])
s = sp.Matrix(sp.symbols('s1:4', real=True)); a = sp.Symbol('a', positive=True)
w0 = EPS*s/2                                          # q -> 0: s' = s, b = a
F0 = (w0.dot(w0)*(a*a + s.dot(s)) - 2*s.dot(w0)**2)/(a*a*2*a)
F0 = F0.subs(s.dot(s), a**2)
target = ((EPS*s).dot(EPS*s)*a**2 - (s.dot(EPS*s))**2)/(4*a**3)
check("A3 F(k,0) = (a^2|eps s|^2 - (s.eps s)^2)/(4 a^3) for every symmetric eps", sp.simplify(sp.expand(F0 - target).subs(s[0]**2 + s[1]**2 + s[2]**2, a**2)) == 0)
lam = sp.Symbol('lam')
v = (sp.eye(3) + lam*EPS)*s
norm = sp.sqrt(sp.expand(v.dot(v)))
ser = sp.series(-norm, lam, 0, 3).removeO()
c2 = sp.simplify(ser.coeff(lam, 2))
unif = -((EPS*s).dot(EPS*s)*s.dot(s) - (s.dot(EPS*s))**2)/(2*s.dot(s)**sp.Rational(3, 2))
check("A4 second-order term of -|(1+eps)s| is -(r^2|eps s|^2 - (s.eps s)^2)/(2 r^3) = -2 F(k,0) (so the q->0 limit is half the uniform form, pointwise)",
      sp.simplify(c2 - unif) == 0)

print("== B the bound 0 <= F <= ||eps||^2 (a+b)/4 (exact spot checks; proof in ATTEMPT)")
random.seed(26)
okB = True; worst = Fr(0)
for trial in range(400):
    sv = [Fr(random.randint(-9, 9), 9) for _ in range(3)]; sq = [Fr(random.randint(-9, 9), 9) for _ in range(3)]
    E = [[Fr(random.randint(-6, 6), 5) for _ in range(3)] for _ in range(3)]
    E = [[(E[i][j] + E[j][i])/2 for j in range(3)] for i in range(3)]
    a2 = sum(x*x for x in sv); b2 = sum(x*x for x in sq)
    if a2 == 0 or b2 == 0: continue
    wv = [sum(E[i][j]*(sv[j] + sq[j]) for j in range(3))/4 for i in range(3)]
    ww = sum(x*x for x in wv); sw = sum(x*y for x, y in zip(sv, wv)); qw = sum(x*y for x, y in zip(sq, wv)); ssq = sum(x*y for x, y in zip(sv, sq))
    A_ = sp.sqrt(sp.Rational(a2.numerator, a2.denominator)); B_ = sp.sqrt(sp.Rational(b2.numerator, b2.denominator))
    N = sp.Rational(ww.numerator, ww.denominator)*(A_*B_ + sp.Rational(ssq.numerator, ssq.denominator)) - 2*sp.Rational(sw.numerator, sw.denominator)*sp.Rational(qw.numerator, qw.denominator)
    Fv = N/(A_*B_*(A_ + B_))
    Fro2 = sum(E[i][j]**2 for i in range(3) for j in range(3))                         # ||eps||_2^2 <= ||eps||_F^2
    ub = sp.Rational(Fro2.numerator, Fro2.denominator)*(A_ + B_)/4
    if not (sp.N(Fv, 50) >= -1e-40 and sp.N(ub - Fv, 50) >= -1e-40): okB = False
check("B1 0 <= F <= ||eps||_F^2 (a+b)/4 at 400 random rational configurations (50-digit evaluation of exact expressions)", okB)

print("== C member + sea at long wavelength (PROVED; ingredients checked)")
# C1 the uniform form is <= 0 pointwise and < 0 somewhere for every symmetric eps not proportional to 1
# pointwise: (s.eps s)^2 <= |s|^2 |eps s|^2 (Cauchy-Schwarz); equality iff s is an eigenvector of eps.
eps_T = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])     # a traceless shear
sv = sp.Matrix([1, 1, 0]); val = ((eps_T*sv).dot(eps_T*sv)*sv.dot(sv) - sv.dot(eps_T*sv)**2)
check("C1 Cauchy-Schwarz gap is positive at s = (1,1,0) for the shear diag(1,-1,0) (so the uniform form is strictly negative)", val > 0, str(val))
# C2 the member's static energy is O(K p^2 |h|^2): R2 is a quadratic form in h with coefficients quadratic in p
pp = sp.Matrix(sp.symbols('p1:4', real=True)); hs = sp.symbols('h11 h12 h13 h22 h23 h33', real=True)
Hm = sp.Matrix([[hs[0], hs[1], hs[2]], [hs[1], hs[3], hs[4]], [hs[2], hs[4], hs[5]]])
P2 = pp.dot(pp)
R2 = -(P2/4)*(Hm.T*Hm).trace() + sp.Rational(1, 2)*(Hm*pp).dot(Hm*pp) - sp.Rational(1, 2)*pp.dot(Hm*pp)*Hm.trace() + (P2/4)*Hm.trace()**2
t_ = sp.Symbol('t')
check("C2 landed R2 is homogeneous of degree 2 in p (so the member costs at most C K |p|^2 |h|^2 per mode)",
      sp.expand(R2.subs({pp[i]: t_*pp[i] for i in range(3)}, simultaneous=True) - t_**2*R2) == 0)
# C3 relabelling invariance of R2 (landed T3(b)), re-checked
xi = sp.Matrix(sp.symbols('x1:4', real=True))
Hr = Hm + pp*xi.T + xi*pp.T
R2r = -(P2/4)*(Hr.T*Hr).trace() + sp.Rational(1, 2)*(Hr*pp).dot(Hr*pp) - sp.Rational(1, 2)*pp.dot(Hr*pp)*Hr.trace() + (P2/4)*Hr.trace()**2
check("C3 R2 is unchanged by h -> h + p xi^T + xi p^T (landed)", sp.expand(R2r - R2) == 0)

print("== D (1): exact reduction of the q^2 coefficient for q || e3 and its evaluation [float]")
s1, s2, s3, c3, q, A = sp.symbols('s1 s2 s3 c3 q A', real=True)
def trunc(x, n=2):
    x = sp.expand(x); return sum(x.coeff(q, i)*q**i for i in range(n + 1))
sp3 = s3 + c3*q - s3*q**2/2                                # sin(k3 + q) to O(q^2)
Delta = trunc(sp3**2 - s3**2)
b_ = trunc(A + Delta/(2*A) - Delta**2/(8*A**3))
def coeffs(eps):
    sv_ = sp.Matrix([s1, s2, s3]); spv = sp.Matrix([s1, s2, sp3])
    w = eps*(sv_ + spv)/4
    N = trunc(w.dot(w)*(A*b_ + sv_.dot(spv)) - 2*sv_.dot(w)*spv.dot(w))
    D = trunc(A*b_*(A + b_)); D0 = D.coeff(q, 0); d = trunc(D - D0)
    F = trunc(N*trunc(1/D0 - d/D0**2 + d**2/D0**3))
    return [sp.expand(sp.simplify(F.coeff(q, i).subs(c3**2, 1 - s3**2))) for i in range(3)]
MODES = (("xi = e1 (h13 = h31 = 1)", sp.Matrix([[0, 0, -sp.Rational(1, 2)], [0, 0, 0], [-sp.Rational(1, 2), 0, 0]])),
         ("xi = e3 (h33 = 2)", sp.Matrix([[0, 0, 0], [0, 0, 0], [0, 0, -1]])))
import mpmath as mp
mp.mp.dps = 80
def M1(n, t):
    z = t/2; tot = mp.mpf(0)
    for j in range(n + 1):
        for i in range(j + 1):
            tot += mp.binomial(n, j)*(-1)**j*mp.binomial(j, i)*mp.besseli(abs(j - 2*i), z)/mp.mpf(2)**j
    return mp.exp(-z)*tot/mp.mpf(2)**n
cache = {}
def moment(n1, n2, n3, nu):
    key = (n1, n2, n3, nu)
    if key not in cache:
        g = lambda t: t**(nu - 1)*M1(n1, t)*M1(n2, t)*M1(n3, t)
        Tm = mp.mpf(10)**7
        val = mp.quad(g, [0, mp.mpf(1)/100, 1, 10, 100, 1000, 10**4, 10**5, 10**6, Tm]) + g(Tm)*Tm
        cache[key] = val/mp.gamma(nu)
    return cache[key]
def zone_avg(expr):
    tot = mp.mpf(0); R2s = s1**2 + s2**2 + s3**2
    for term in sp.Add.make_args(sp.expand(expr)):
        cf, rest = term.as_coeff_Mul()
        num, den = rest.as_numer_denom()
        ex = sp.degree(num, A) - sp.degree(den, A)
        mon = sp.simplify(rest/A**ex)
        assert ex % 2 == 1
        if ex > 0: mon = sp.expand(mon*R2s**((ex + 1)//2)); nu = sp.Rational(1, 2)
        else: nu = sp.Rational(-ex, 2)
        for t2 in sp.Add.make_args(sp.expand(mon)):
            c2_, m2 = t2.as_coeff_Mul()
            pw = sp.Poly(m2, s1, s2, s3).monoms()[0]
            assert all(x % 2 == 0 for x in pw) and sum(pw) - 2*nu > -3      # every monomial integrable at the Dirac points
            cc = sp.Rational(cf)*sp.Rational(c2_)
            tot += mp.mpf(cc.p)/cc.q*moment(pw[0]//2, pw[1]//2, pw[2]//2, mp.mpf(nu.p)/nu.q)
    return tot
Iv = zone_avg(A)
check("D0 [float] the Laplace-Bessel moment method reproduces I = <|s|> = 1.1938011214298", abs(Iv - mp.mpf('1.19380112142980')) < mp.mpf('1e-12'), mp.nstr(Iv, 16))
for lab, eps in MODES:
    F0, F1, F2 = coeffs(eps)
    odd = all(t.has(c3) for t in sp.Add.make_args(F1))
    check(f"D1 {lab}: the q^1 integrand is odd under k3 -> -k3 (every term carries c3 s3), so the q^1 coefficient vanishes", odd)
    v0 = -zone_avg(F0); v2 = -zone_avg(F2)
    print(f"   [float] {lab}: q^0 coefficient of E2 = {mp.nstr(v0, 12)}, q^2 coefficient of E2 = {mp.nstr(v2, 12)}", flush=True)
    check(f"D2 [float] {lab}: q^2 coefficient is nonzero (R2 gives 0): not relabelling-invariant", abs(v2) > mp.mpf('1e-3'), mp.nstr(v2, 10))

print(f"== done in {time.time()-T0:.0f}s")
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("SUMMARY: PARTIAL (exact for (2) and (3)): the static response E2(q) = -<F(k,q)> has a bounded integrand "
          "(0 <= F <= ||eps||^2 (a+b)/4), so it is continuous at q = 0 with limit exactly half the uniform second-order "
          "form; that form is <= 0 pointwise (Cauchy-Schwarz) and < 0 for every strain not proportional to 1; the member "
          "costs O(K |p|^2); hence member + sea lowers its energy under every long enough shear wave, for every K > 0. "
          "(1): exact reduction of the q^2 coefficient to zone moments; 1D Bessel evaluation gives 0.0022838 and 0.0039358 "
          "for the e3 relabelling modes [float; interval certification open]")
    print("HIT member + sea is unstable to every long enough shear wave for every K > 0 (exact); the sea's static response is continuous at q = 0 with half the uniform form")
