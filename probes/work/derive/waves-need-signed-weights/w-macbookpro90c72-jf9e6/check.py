#!/usr/bin/env python3
"""J:derive:waves-need-signed-weights:a4 -- exact checks (sympy / Fraction).

Depth rigidity, the self-inversive ladder, the J<=3 classification (deltoid =
discriminant), and the cone identities for the signed nearest-neighbour rules.
"""
from fractions import Fraction as F
import sympy as sp

BAD = []
def ok(m): print("ok " + m)
def bad(m): BAD.append(m); print("BAD " + m)

lam, nu = sp.symbols('lam nu')
x, y = sp.symbols('x y', real=True)


# ---------------------------------------------------------------- S0
# (a) nonnegative weights, ONE branch: the theorem and its exception.
# theta_{t+1} = sum_{j<J} W_j * theta_{t-j}, W_j >= 0 finite, gain sum_j Wh_j(0) = 1.
# Step 1 of ATTEMPT.md proves: if one branch has |lam(k)| = 1 on a nonempty open
# set, every level with mass is a single site, W_j = g_j delta_{(j+1)v}, common v.
# Checked here: that family's symbol is transport times a k-FREE recursion, so the
# branch lam = e^{-ikv} is unimodular at every k; and an instance one step outside
# the family has no unimodular branch away from k = 0.
kk, mu = sp.Symbol('kk', real=True), sp.Symbol('mu')
vv = sp.Symbol('vv', positive=True)
for J in (2, 3, 4):
    gs = sp.symbols('g0:%d' % J, nonnegative=True)
    chi = lam**J - sum(gs[j]*sp.exp(-sp.I*kk*(j + 1)*vv)*lam**(J - 1 - j)
                       for j in range(J))
    red = sp.powsimp(sp.expand(chi.subs(lam, mu*sp.exp(-sp.I*kk*vv))
                               * sp.exp(sp.I*J*kk*vv)), force=True)
    tgt = mu**J - sum(gs[j]*mu**(J - 1 - j) for j in range(J))
    (ok if sp.simplify(sp.expand(red - tgt)) == 0 else bad)(
        "S0 J=%d chi(mu e^{-ikv}) = e^{-iJkv} (mu^J - sum_j g_j mu^{J-1-j}): k-free"
        % J)

# not vacuous: J=3, g = (1/2, 0, 1/2), v = 1 -- theta_{t+1}(x) =
# (theta_t(x-1) + theta_{t-2}(x-3))/2, three levels, two of them carrying mass.
P3 = mu**3 - sp.Rational(1, 2)*mu**2 - sp.Rational(1, 2)
QQ = mu**2 + mu/2 + sp.Rational(1, 2)
(ok if sp.expand(P3 - (mu - 1)*QQ) == 0 else bad)(
    "S0 instance g=(1/2,0,1/2): mu^3 - mu^2/2 - 1/2 = (mu - 1)(mu^2 + mu/2 + 1/2)")
(ok if sp.discriminant(QQ, mu) == sp.Rational(-7, 4)
    and QQ.coeff(mu, 0) == sp.Rational(1, 2) else bad)(
    "S0 instance: transport branch |lam| = 1 at every k; the other two are a "
    "conjugate pair (disc = -7/4 < 0) of modulus 1/sqrt(2) < 1")


def rev_conj(P):
    """lam^d conj(P(1/conj lam)): roots 1/conj(root). Res(P, P*) != 0 => no |lam| = 1."""
    cs = sp.Poly(P, lam).all_coeffs()
    return sum(sp.conjugate(cs[i])*lam**i for i in range(len(cs)))


# one step outside the family: W_0 = W_1 = delta_1/2 (needs y_1 = 2 y_0 = 2, has 1).
for kv, lab, want in ((sp.pi/3, 'pi/3', 1), (sp.pi/2, 'pi/2', 1),
                      (sp.pi, 'pi', 1), (0, '0', 0)):
    ee = sp.expand(sp.cos(kv) - sp.I*sp.sin(kv))
    PP = sp.expand(lam**2 - ee/2*lam - ee/2)
    R = sp.simplify(sp.expand(sp.resultant(PP, sp.expand(rev_conj(PP)), lam)))
    (ok if (R != 0) == bool(want) else bad)(
        "S0 W_0 = W_1 = delta_1/2 at k = %s: Res(P, P*) = %s" % (lab, R))


# ---------------------------------------------------------------- S1
# A real FIR symbol is unimodular only if it is one signed site.
def autocorr(w):
    ac = {}
    for p, wp in w.items():
        for q, wq in w.items():
            ac[p - q] = ac.get(p - q, 0) + wp * wq
    return {m: v for m, v in ac.items() if v != 0}

S1 = [("one signed site", {3: F(-1)}),
      ("NN average", {-1: F(1, 2), 1: F(1, 2)}),
      ("three sites", {0: F(1, 2), 2: F(1, 3), 5: F(1, 6)}),
      ("signed pair, unit l2 norm", {0: F(3, 5), 1: F(-4, 5)})]
for name, w in S1:
    ac, sup = autocorr(w), sorted(w)
    mstar = sup[-1] - sup[0]
    uni = (ac == {0: F(1)})
    if len(w) == 1:
        good = uni and abs(w[sup[0]]) == 1
    else:
        good = (not uni) and ac.get(mstar, F(0)) == w[sup[-1]] * w[sup[0]] != 0
    (ok if good else bad)("S1 %s: |W|^2==1 is %s, extreme-lag %d coeff %s"
                          % (name, uni, mstar, ac.get(mstar, 0)))


# ---------------------------------------------------------------- S2
# All branches unimodular  =>  a_j = -a_{J-1} conj(a_{J-2-j}).
for J in (2, 3, 4):
    ph = sp.symbols('p0:%d' % J, real=True)
    P = sp.expand(sp.prod([lam - sp.exp(sp.I * p) for p in ph]))
    c = [sp.expand(P.coeff(lam, m)) for m in range(J + 1)]
    a = [-c[J - 1 - j] for j in range(J)]
    resid = [sp.simplify(sp.expand(a[j] + a[J - 1] * sp.conjugate(a[J - 2 - j])))
             for j in range(J - 1)]
    (ok if all(r == 0 for r in resid) else bad)(
        "S2 J=%d ladder a_j = -a_{J-1} conj(a_{J-2-j}) (%d relations)" % (J, J - 1))

# the J=2 instance: a_1 = -1 forces W_0 symmetric (a_0 real)
a0 = sp.Symbol('a0')
(ok if sp.simplify(a0 - (-(-1) * sp.conjugate(a0))) == sp.simplify(a0 - sp.conjugate(a0))
 else bad)("S2 J=2 with a_1=-1 reduces to a_0 = conj(a_0): W_0 symmetric")


# ---------------------------------------------------------------- S3
# disc of the canonical self-inversive cubic = the deltoid polynomial.
b = x + sp.I * y
CUB = nu**3 - b * nu**2 + sp.conjugate(b) * nu - 1
D = sp.expand(sp.discriminant(CUB, nu))
DELT = sp.expand((x**2 + y**2)**2 + 18 * (x**2 + y**2) - 8 * x * (x**2 - 3 * y**2) - 27)
(ok if sp.simplify(D - DELT) == 0 else bad)(
    "S3 disc(nu^3-b nu^2+conj(b) nu-1) = (|b|^2)^2+18|b|^2-8Re(b^3)-27 (real, = deltoid)")
(ok if sp.factor(D.subs(y, 0)) == sp.factor((x + 1) * (x - 3)**3) else bad)(
    "S3 real section: disc = (b+1)(b-3)^3, so disc<=0 iff b in [-1,3]")
cusps = [sp.simplify(D.subs({x: sp.re(3 * sp.exp(2 * sp.pi * sp.I * j / 3)),
                             y: sp.im(3 * sp.exp(2 * sp.pi * sp.I * j / 3))}))
         for j in range(3)]
(ok if all(cu == 0 for cu in cusps) else bad)(
    "S3 the three cusps 3, 3w, 3w^2 lie on disc=0 (w = exp(2 pi i/3))")


# ---------------------------------------------------------------- S4
# disc sign against exact unimodular / off-circle root triples.
def disc_of(bv):
    return sp.expand(sp.simplify(sp.discriminant(
        nu**3 - bv * nu**2 + sp.conjugate(bv) * nu - 1, nu)))

u1, u2 = sp.Rational(3, 5) + sp.Rational(4, 5) * sp.I, sp.Rational(5, 13) + sp.Rational(12, 13) * sp.I
u3 = sp.simplify(1 / (u1 * u2))
prod_on = sp.simplify(u1 * u2 * u3)
b_on = sp.simplify(u1 + u2 + u3)
d_on = sp.nsimplify(disc_of(b_on))
(ok if prod_on == 1 and sp.simplify(sp.Abs(u3) - 1) == 0 and d_on < 0 else bad)(
    "S4 unimodular triple (3+4i)/5,(5+12i)/13,conj(product): b=%s, disc=%s<0"
    % (sp.nsimplify(b_on), d_on))

d_off = disc_of(sp.Integer(10))
roots_off = sp.roots(sp.Poly(nu**3 - 10 * nu**2 + 10 * nu - 1, nu))
mods = sorted(sp.simplify(sp.Abs(r)) for r in roots_off)
(ok if d_off == 3773 and d_off > 0 and sp.simplify(mods[0] - 1) != 0 else bad)(
    "S4 b=10: disc=%s>0 and the roots (9+-sqrt77)/2, 1 are not all unimodular" % d_off)

# Both directions of "all roots unimodular <=> disc <= 0", symbolic in the
# parameters (not instances).  The self-inversive root multiset is closed under
# nu -> 1/conj(nu); in odd degree at least one root is fixed, i.e. unimodular.
# (i) all three on the circle, product 1 (so th_3 = -th_1-th_2):
t1, t2 = sp.symbols('t1 t2', real=True)
th3 = [t1, t2, -t1 - t2]
b_un = sum(sp.exp(sp.I * t) for t in th3)
D_un = sp.discriminant(nu**3 - b_un * nu**2 + sp.conjugate(b_un) * nu - 1, nu)
R_un = -64 * sp.prod([sp.sin((th3[i] - th3[j]) / 2)**2
                      for i in range(3) for j in range(i + 1, 3)])
(ok if sp.simplify(sp.expand((D_un - R_un).rewrite(sp.exp))) == 0 else bad)(
    "S4 on the circle: disc = -64 prod_{i<j} sin^2((th_i-th_j)/2) <= 0, identically in "
    "(th_1,th_2) -- so every unimodular triple has disc <= 0, with equality iff repeated")
# (ii) off the circle the triple is e^{-2id}, rho e^{id}, e^{id}/rho (the pair is
#      swapped by the involution, the fixed root is forced by the product):
rho_s = sp.Symbol('rho', positive=True)
dl = sp.Symbol('dl', real=True)
ei = sp.exp(sp.I * dl)
b_off = ei**-2 + rho_s * ei + ei / rho_s
D_off = sp.discriminant(nu**3 - b_off * nu**2 + sp.conjugate(b_off) * nu - 1, nu)
R_off = (rho_s - 1 / rho_s)**2 * (2 * sp.cos(3 * dl) - rho_s - 1 / rho_s)**2
(ok if sp.simplify(sp.expand((D_off - R_off).rewrite(sp.exp))) == 0 else bad)(
    "S4 off the circle: disc = (rho-1/rho)^2 (2cos 3d - (rho+1/rho))^2 identically in "
    "(rho,d); rho+1/rho > 2 >= 2cos 3d and rho != 1/rho, so disc > 0 strictly")
# the same on an exact instance: rho=2, e^{2id} = (3-4i)/5, i.e. ed = (2-i)/sqrt5.
ed = (2 - sp.I) / sp.sqrt(5)
rho = sp.Integer(2)
b_gen = sp.expand(ed**-2 + rho * ed + ed / rho)
lhs = sp.radsimp(sp.expand(disc_of(b_gen)))
rhs = sp.radsimp(sp.expand((rho - 1 / rho)**2 * (ed**3 + ed**-3 - rho - 1 / rho)**2))
(ok if sp.simplify(lhs - rhs) == 0 and sp.simplify(sp.im(lhs)) == 0
 and sp.simplify(lhs) > 0 else bad)(
    "S4 instance rho=2, ed=(2-i)/sqrt5: 2cos 3d = 4 sqrt5/25 and disc = %s > 0"
    % sp.nsimplify(lhs))


# ---------------------------------------------------------------- S5
# The J=3 gain-one rule theta_{t+1} = P(theta_t + theta_{t-1}) - theta_{t-2}.
Ph = sp.Symbol('Phat', real=True)
CH = sp.expand(lam**3 - Ph * lam**2 - Ph * lam + 1)
FAC = sp.expand((lam + 1) * (lam**2 - (1 + Ph) * lam + 1))
(ok if sp.expand(CH - FAC) == 0 else bad)(
    "S5 lam^3-P lam^2-P lam+1 = (lam+1)(lam^2-(1+P)lam+1): a blinking branch lam=-1 at every k")
# the pair: |1+Phat| <= 2 gives e^{+-i w}, |1+Phat| > 2 gives sigma*rho, sigma/rho.
w = sp.Symbol('w', real=True)
sg, rr = sp.Symbol('sigma'), sp.Symbol('rr', positive=True)
QU = (lam**2 - (1 + Ph) * lam + 1).subs(Ph, 2 * sp.cos(w) - 1)
QR = (lam**2 - (1 + Ph) * lam + 1).subs(Ph, sg * (rr + 1 / rr) - 1)
(ok if sp.simplify(sp.expand((QU - (lam - sp.exp(sp.I * w)) * (lam - sp.exp(-sp.I * w)))
                             .rewrite(sp.exp))) == 0
 and sp.simplify(sp.expand(QR.subs(sg, 1) - (lam - rr) * (lam - 1 / rr))) == 0
 and sp.simplify(sp.expand(QR.subs(sg, -1) - (lam + rr) * (lam + 1 / rr))) == 0 else bad)(
    "S5 pair unimodular iff |1+Phat| <= 2 iff Phat in [-3,1]: 1+Phat=2cos w factors as "
    "(lam-e^{iw})(lam-e^{-iw}), 1+Phat=+-(rr+1/rr) as (lam-+rr)(lam-+1/rr), |rr|>1 "
    "(asymmetric window; the J=2 window is [-1,1])")
# the blinking mode exactly, on a ring of 7 with an arbitrary rational profile
N = 7
f = [F(k * k + 1, 3 * k + 5) for k in range(N)]
def Pav(v): return [(v[(i - 1) % N] + v[(i + 1) % N]) / 2 for i in range(N)]
th = {-2: [(+1) * z for z in f], -1: [(-1) * z for z in f], 0: [(+1) * z for z in f]}
good = True
for t in range(0, 6):
    nxt = [Pav(th[t])[i] + Pav(th[t - 1])[i] - th[t - 2][i] for i in range(N)]
    if nxt != [-z for z in th[t]]:
        good = False
    th[t + 1] = nxt
(ok if good else bad)("S5 (-1)^t f(x) is an exact solution for every profile f (6 ticks, ring 7)")
# losslessness on the ring: every mode has |1+Phat| <= 2
N6 = 6
ph6 = [sp.cos(2 * sp.pi * j / N6) for j in range(N6)]
(ok if all(sp.simplify(sp.Abs(1 + p) - 2) <= 0 for p in ph6) else bad)(
    "S5 ring of 6: all 3*6 branches unimodular (Phat in {1,1/2,-1/2,-1})")


# ---------------------------------------------------------------- S6
# Cone identities.  J=2: cos w = Phat.  J=3: cos w = (1+Phat)/2.  Phat = (1/d) sum cos k_j.
for d in (1, 2, 3, 4):
    cs = sp.symbols('c0:%d' % d, real=True)
    S = sum(cs)
    num = sum(1 - c**2 for c in cs)
    pairs = sum((cs[i] - cs[j])**2 for i in range(d) for j in range(i + 1, d))
    # J = 2 (massless):  |grad w|^2 = num / (d^2 - S^2)
    lhs2 = sp.together(sp.Rational(1, d) - num / (d**2 - S**2))
    rhs2 = sp.together(pairs / (d * (d**2 - S**2)))
    e2 = sp.simplify(sp.expand(sp.numer(sp.together(lhs2 - rhs2))))
    # J = 3 (gain one): |grad w|^2 = num / (4 d^2 - (d+S)^2)
    lhs3 = sp.together(sp.Rational(1, 2 * d) - num / (4 * d**2 - (d + S)**2))
    rhs3 = sp.together(((d - S)**2 + 2 * pairs) / (2 * d * (4 * d**2 - (d + S)**2)))
    e3 = sp.simplify(sp.expand(sp.numer(sp.together(lhs3 - rhs3))))
    (ok if e2 == 0 and e3 == 0 else bad)(
        "S6 d=%d: 1/d - |grad w|^2 = sum_{i<j}(c_i-c_j)^2 / (d(d^2-S^2));  "
        "1/2d - |grad w|^2 = [(d-S)^2 + 2 sum_{i<j}(c_i-c_j)^2] / (2d(4d^2-(d+S)^2))" % d)

# the long-wavelength limit fills the sphere: |grad w| -> 1/sqrt(d), 1/sqrt(2d) along every ray
eps = sp.Symbol('eps', positive=True)
for d in (2, 3):
    ns = sp.symbols('n0:%d' % d, positive=True)
    cs = [sp.cos(eps * n) for n in ns]
    S, num = sum(cs), sum(1 - c**2 for c in cs)
    l2 = sp.limit(num / (d**2 - S**2), eps, 0)
    l3 = sp.limit(num / (4 * d**2 - (d + S)**2), eps, 0)
    (ok if sp.simplify(l2 - sp.Rational(1, d)) == 0
     and sp.simplify(l3 - sp.Rational(1, 2 * d)) == 0 else bad)(
        "S6 d=%d: along every ray k=eps*n, |grad w|^2 -> 1/%d (J=2) and 1/%d (J=3)"
        % (d, d, 2 * d))


# ---------------------------------------------------------------- S7
# No isotropic spectrum: a witness pair |k| equal, omega different (d=2, J=2, a=1).
h = sp.pi / 12
kA, kB = (0 * h, 5 * h), (3 * h, 4 * h)
cA = sp.simplify((sp.cos(kA[0]) + sp.cos(kA[1])) / 2)
cB = sp.simplify((sp.cos(kB[0]) + sp.cos(kB[1])) / 2)
(ok if sp.simplify(kA[0]**2 + kA[1]**2 - kB[0]**2 - kB[1]**2) == 0
 and sp.simplify(sp.nsimplify(cA - cB)) != 0 else bad)(
    "S7 |k| equal at (0,5)h and (3,4)h, h=pi/12, but cos w differs: %s vs %s"
    % (sp.nsimplify(cA), sp.nsimplify(cB)))


# ---------------------------------------------------------------- S8
# Jensen bound on the branch-modulus product for a spread deepest level.
for name, w in [("NN average", {-1: F(1, 2), 1: F(1, 2)}),
                ("three sites", {0: F(1, 2), 2: F(1, 3), 5: F(1, 6)})]:
    n2 = sum(v * v for v in w.values())
    (ok if sum(w.values()) == 1 and n2 < 1 else bad)(
        "S8 %s: gain one, ||w||_2^2 = %s < 1, so mean log|prod branches| <= %s/2 log %s"
        % (name, n2, 1, n2))


# ---------------------------------------------------------------- S9
# (c) bridge: a unitary rule on AMPLITUDES gives each component a signed scalar
# recursion, and the deepest coefficient is +-det U(k), of modulus 1 -- so S1
# (complex form) forces det U(k) to be one lattice shift times a unit constant.
u11, u12, u21, u22 = sp.symbols('u11 u12 u21 u22')
U = sp.Matrix([[u11, u12], [u21, u22]])
(ok if sp.expand(U*U - (u11 + u22)*U + (u11*u22 - u12*u21)*sp.eye(2)) == sp.zeros(2, 2)
 else bad)("S9 Cayley-Hamilton: psi_{t+2} = (tr U) psi_{t+1} - (det U) psi_t, each component")

th, k2 = sp.symbols('th k2', real=True)
cc, sq = sp.cos(th), sp.sin(th)
Uk = sp.Matrix([[cc*sp.exp(-sp.I*k2), sq], [-sq, cc*sp.exp(sp.I*k2)]])
(ok if sp.simplify(Uk.H*Uk - sp.eye(2)) == sp.zeros(2, 2)
    and sp.simplify(sp.det(Uk) - 1) == 0
    and sp.simplify(sp.trace(Uk) - 2*cc*sp.cos(k2)) == 0 else bad)(
    "S9 the 1+1 coin symbol is unitary with det = 1, tr = 2 c cos k: "
    "lam^2 - 2 c cos k lam + 1, i.e. exactly the two-level signed rule")


def autocorr_c(w):
    ac = {}
    for p, wp in w.items():
        for q, wq in w.items():
            ac[p - q] = sp.expand(ac.get(p - q, 0) + wp*sp.conjugate(wq))
    return {m: v for m, v in ac.items() if sp.simplify(v) != 0}


acc = autocorr_c({0: sp.Rational(3, 5), 1: sp.Rational(4, 5)*sp.I})
(ok if sp.simplify(acc[0] - 1) == 0 and sp.simplify(acc[1] - sp.Rational(12, 25)*sp.I) == 0
 else bad)("S9 complex form of S1: {3/5, 4i/5} has l2 norm 1 but extreme lag "
           "12i/25 != 0, so |What| is not 1: unit norm alone is not enough")


# ---------------------------------------------------------------- summary
print()
if BAD:
    print("SUMMARY: ROUTE FAILS AT " + BAD[0])
else:
    print("SUMMARY: PARTIAL - (a) one branch, nonnegative weights: |lam| = 1 on an open "
          "set forces rigid transport, every level with mass one site W_j = g_j "
          "delta_{(j+1)v} (S0); (b) signed: W_{J-1} = +-delta_{y0} and the ladder "
          "W_j = -eps S_{y0} reflect(W_{J-2-j}), J <= 3 lossless iff disc <= 0, the "
          "gain-one J=3 rule blinks at lam = -1, window [-3,1] (S1-S5); (c) det U(k) is "
          "one shift; the signed NN cones are round at 1/sqrt(d), 1/sqrt(2d) (S6-S9).")
    print("HIT: a nonnegative gain-one formation law over finitely many levels has no "
          "branch with |lam(k)| = 1 on a nonempty open set unless every level carrying "
          "mass is a single site W_j = g_j delta_{(j+1)v} sharing one v: rigid transport "
          "at v averaged over delays.")
    print("HIT: dropping nonnegativity, a real J-level rule with all J branches unimodular "
          "on an open set has W_{J-1} = +-delta_{y0} and W_j = -eps S_{y0} "
          "reflect(W_{J-2-j}); for J = 3 lossless is exactly disc <= 0 for "
          "disc = |b|^4 + 18|b|^2 - 8 Re(b^3) - 27, real section (b+1)(b-3)^3.")
    print("HIT: any finite-range unitary rule on n-component amplitudes has "
          "det U(k) = c e^{-i k.y0} with |c| = 1: each component obeys a depth-n signed "
          "recursion whose deepest weight is +-det U, of modulus 1.")
    print("HIT: the massless signed nearest-neighbour rule on Z^d has velocity set closing "
          "to exactly the ball of radius 1/sqrt(d) (1/sqrt(2d) for the gain-one "
          "three-level rule), via 1/d - |grad w|^2 = sum_{i<j}(cos k_i - cos k_j)^2 / "
          "(d (d^2 - S^2)), S = sum_j cos k_j: the cone is round though the spectrum is "
          "not a function of |k|.")
import sys
sys.exit(1 if BAD else 0)
