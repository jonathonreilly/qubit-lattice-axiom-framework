#!/usr/bin/env python3
"""The sea's response to a slow uniform stretch -- worker w-macbookpro9927a-jad41.

Families (see ATTEMPT.md for the steps they check):
  P  operator identity for the cranking inertia: sympy spin trace, and an exact
     Gaussian-rational check on the periodic 4^3 lattice (128 states).
  M  the three cubic parts, O_h invariance, the 3-dimensional invariant space,
     positivity on traceless stretches, the dilation part.
  H  hopping coefficients of D(mu) in exact rationals; a large-mu lower bound.
  L  the Laplace/series representation: series identities, ratio monotonicity,
     factorisation of the averages.
  R  interval arithmetic (mpmath.iv): D(0), c/a, b/a, and D(mu) > 0 on
     mu^2 in [0, 16].
  K  the member's form alpha[tr(hdot^2) - (tr hdot)^2] against a positive response.
Everything except family R is exact (fractions / sympy). Family R is interval
arithmetic with outward rounding (ASSUMED A1 in ATTEMPT.md).
"""
import sys
from fractions import Fraction as Fr
from itertools import permutations, product

import sympy as sp
from mpmath import iv, mpf

FAILS = []


def ok(tag, cond, msg=""):
    if not cond:
        FAILS.append(tag)
    print(f"{tag} {'ok' if cond else 'FAIL'} {msg}".rstrip())


# ---------------------------------------------------------------- family P
s1, s2, s3, b1, b2, b3, mu = sp.symbols('s1 s2 s3 b1 b2 b3 mu', real=True)
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]),
       sp.Matrix([[1, 0], [0, -1]])]
sv, bv = sp.Matrix([s1, s2, s3]), sp.Matrix([b1, b2, b3])
sdot = lambda v: sum((v[a] * sig[a] for a in range(3)), sp.zeros(2))
X, A = sdot(bv), sdot(sv)
C = A * X
E2 = s1**2 + s2**2 + s3**2 + mu**2
lhs = sp.expand((E2 * X * X - C * C + mu**2 * X * X).trace())
cr = sv.cross(bv)
rhs = sp.expand(4 * (cr.dot(cr) + mu**2 * bv.dot(bv)))
ok("P1", sp.simplify(lhs - rhs) == 0,
   "Tr_spin[E^2X^2-(AX)^2+mu^2X^2] = 4(|s x b|^2+mu^2|b|^2)")

# exact lattice check, L = 4 (sin k in {0,1,0,-1}); Gaussian rationals as pairs
L = 4
sites = list(product(range(L), repeat=3))
sidx = {x: i for i, x in enumerate(sites)}
ZERO = (Fr(0), Fr(0))


def gm(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def mat_add(*terms):
    out = {}
    for coef, M in terms:
        for r, row in M.items():
            orow = out.setdefault(r, {})
            for c, v in row.items():
                w = gm(coef, v)
                o = orow.get(c, ZERO)
                orow[c] = (o[0] + w[0], o[1] + w[1])
    return {r: {c: v for c, v in row.items() if v != ZERO}
            for r, row in out.items() if any(v != ZERO for v in row.values())}


def mat_mul(M, N):
    out = {}
    for r, row in M.items():
        acc = {}
        for k, v in row.items():
            for c, w in N.get(k, {}).items():
                p = gm(v, w)
                o = acc.get(c, ZERO)
                acc[c] = (o[0] + p[0], o[1] + p[1])
        acc = {c: v for c, v in acc.items() if v != ZERO}
        if acc:
            out[r] = acc
    return out


def trace(M):
    t = ZERO
    for r, row in M.items():
        v = row.get(r, ZERO)
        t = (t[0] + v[0], t[1] + v[1])
    return t


PAULI = [{(0, 1): (Fr(1), Fr(0)), (1, 0): (Fr(1), Fr(0))},
         {(0, 1): (Fr(0), Fr(-1)), (1, 0): (Fr(0), Fr(1))},
         {(0, 0): (Fr(1), Fr(0)), (1, 1): (Fr(-1), Fr(0))}]


def spin_site(spin, site):  # spin (x) site operator; index = 2*site + spin
    out = {}
    for (a, b), u in spin.items():
        for r, row in site.items():
            for c, v in row.items():
                out.setdefault(2 * r + a, {})[2 * c + b] = gm(u, v)
    return out


ONE_SPIN = {(0, 0): (Fr(1), Fr(0)), (1, 1): (Fr(1), Fr(0))}
S_site = []
for a in range(3):
    M = {}
    for x in sites:
        xp = list(x); xp[a] = (xp[a] + 1) % L
        xm = list(x); xm[a] = (xm[a] - 1) % L
        M.setdefault(sidx[x], {})[sidx[tuple(xp)]] = (Fr(0), Fr(-1, 2))
        M[sidx[x]][sidx[tuple(xm)]] = (Fr(0), Fr(1, 2))
    S_site.append(M)
Gam = {sidx[x]: {sidx[x]: (Fr((-1) ** sum(x)), Fr(0))} for x in sites}
IDN = {i: {i: (Fr(1), Fr(0))} for i in range(2 * len(sites))}
SS = [spin_site(PAULI[a], S_site[a]) for a in range(3)]
Ssq = mat_add(*[((Fr(1), Fr(0)), spin_site(ONE_SPIN, mat_mul(S_site[a], S_site[a])))
                for a in range(3)])
GAM = spin_site(ONE_SPIN, Gam)
H0 = mat_add(*[((Fr(1), Fr(0)), SS[a]) for a in range(3)])
modes = {'T2': [[0, 1, 0], [1, 0, 0], [0, 0, 0]], 'E': [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
         'A1': [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
         'gen': [[Fr(1, 3), 2, -1], [2, Fr(-5, 7), Fr(1, 2)], [-1, Fr(1, 2), 3]]}
sin4 = [0, 1, 0, -1]
p_ok = True
for m_val in (Fr(0), Fr(1), Fr(2, 3)):
    H = mat_add(((Fr(1), Fr(0)), H0), ((m_val, Fr(0)), GAM))
    E2op = mat_add(((Fr(1), Fr(0)), Ssq), ((m_val**2, Fr(0)), IDN))
    p_ok &= mat_add(((Fr(1), Fr(0)), mat_mul(H, H)), ((Fr(-1), Fr(0)), E2op)) == {}
    for name, dh in modes.items():
        dh = [[Fr(v) for v in row] for row in dh]
        Xop = {}
        for a_ in range(3):
            for i_ in range(3):
                if dh[a_][i_]:
                    Xop = mat_add(((Fr(1), Fr(0)), Xop),
                                  ((-dh[a_][i_] / 2, Fr(0)),
                                   spin_site(PAULI[a_], S_site[i_])))
        HX = mat_mul(H, Xop)
        tr = mat_add(((Fr(1), Fr(0)), mat_mul(E2op, mat_mul(Xop, Xop))),
                     ((Fr(-1), Fr(0)), mat_mul(HX, HX)))
        lat = trace(tr)
        mom = Fr(0)
        for k in product(range(L), repeat=3):
            s = [Fr(sin4[q]) for q in k]
            b = [-sum(dh[a_][i_] * s[i_] for i_ in range(3)) / 2 for a_ in range(3)]
            cx = [s[1] * b[2] - s[2] * b[1], s[2] * b[0] - s[0] * b[2], s[0] * b[1] - s[1] * b[0]]
            mom += 4 * (sum(v * v for v in cx) + m_val**2 * sum(v * v for v in b))
        p_ok &= (lat == (mom, Fr(0)))
ok("P2", p_ok, "4^3 torus, mu in {0,1,2/3}, 4 stretches: H^2=S^2+mu^2 and "
   "Tr(E^2X^2-(HX)^2) = 4 sum_k(|s x b|^2+mu^2|b|^2), exactly")

# ---------------------------------------------------------------- family M
x1, x2, x3 = sp.symbols('x1 x2 x3', nonnegative=True)
SUBS = {s1**2: x1, s2**2: x2, s3**2: x3}


def mode_parts(dh):
    v = sp.Matrix(dh) * sv
    c = sv.cross(v)
    return sp.expand(c.dot(c)), sp.expand(v.dot(v))


def to_x(e):
    e = sp.expand(e)
    return sp.expand(e.subs({s1: sp.sqrt(x1), s2: sp.sqrt(x2), s3: sp.sqrt(x3)}))


cT, nT = mode_parts(modes['T2'])
cE, nE = mode_parts(modes['E'])
cA, nA = mode_parts(modes['A1'])
w = 2 * x1 * x2 - sp.Rational(1, 2) * (x1 - x2)**2
ok("M1", to_x(nE - nT) == 0 and sp.expand(to_x(cE - cT) - 2 * w) == 0 and cA == 0
   and to_x(nA) == x1 + x2 + x3,
   "|dh s|^2 equal for E,T2; |s x Es|^2-|s x Ts|^2 = 2w; dilation: s x s = 0")

hs = sp.symbols('h11 h22 h33 h12 h13 h23')
Hm = sp.Matrix([[hs[0], hs[3], hs[4]], [hs[3], hs[1], hs[5]], [hs[4], hs[5], hs[2]]])
signed = []
for perm in permutations(range(3)):
    for sg in product((1, -1), repeat=3):
        P = sp.zeros(3)
        for i in range(3):
            P[i, perm[i]] = sg[i]
        signed.append(P)
integrand = lambda Hmat, svec: (lambda v: (svec.cross(v)).dot(svec.cross(v))
                                + mu**2 * v.dot(v))(Hmat * svec)
base = sp.expand(integrand(Hm, sv))
inv_ok = all(sp.expand(integrand(P * Hm * P.T, P * sv) - base) == 0 for P in signed)
monos = [hs[i] * hs[j] for i in range(6) for j in range(i, 6)]
cs = sp.symbols('q0:%d' % len(monos))
q = sum(c * m for c, m in zip(cs, monos))
eqs = []
for P in signed:
    Hp = P * Hm * P.T
    sub = {hs[0]: Hp[0, 0], hs[1]: Hp[1, 1], hs[2]: Hp[2, 2], hs[3]: Hp[0, 1],
           hs[4]: Hp[0, 2], hs[5]: Hp[1, 2]}
    diff = sp.Poly(sp.expand(q.xreplace(sub) - q), *hs)
    eqs += list(diff.coeffs())
sol = sp.linsolve(eqs, cs)
(solv,) = sol
dim = len(set().union(*[sp.sympify(e).free_symbols for e in solv]) & set(cs))
trh2 = sp.expand((Hm * Hm).trace()); trh = Hm.trace(); diag2 = sum(hs[i]**2 for i in range(3))
indep = sp.Matrix([[sp.Poly(f, *hs).coeff_monomial(m) for m in monos]
                   for f in (trh2, sp.expand(trh**2), diag2)]).rank() == 3
ok("M2", inv_ok and dim == 3 and indep,
   "integrand O_h-invariant (48 signed perms); invariant quadratic forms on Sym(3): "
   "dim 3 = span{tr h^2, (tr h)^2, sum h_ii^2}")

lam = sp.symbols('lam')
null_sol = sp.solve([c for c in sp.Poly(sp.expand((sv.cross(Hm * sv))[0]), s1, s2, s3).coeffs()]
                    + [c for c in sp.Poly(sp.expand((sv.cross(Hm * sv))[1]), s1, s2, s3).coeffs()]
                    + [c for c in sp.Poly(sp.expand((sv.cross(Hm * sv))[2]), s1, s2, s3).coeffs()],
                    hs, dict=True)
ok("M3", len(null_sol) == 1 and all(null_sol[0].get(hs[i], hs[i]) == 0 for i in (3, 4, 5))
   and null_sol[0].get(hs[0], hs[0]) == null_sol[0].get(hs[1], hs[1]) == hs[2],
   "s x (dh s) = 0 for all s iff dh = lam*1: positive on every traceless stretch")

QA, QE, QT = sp.symbols('QA QE QT')
a_, b_, c_ = QT / 2, (QA - sp.Rational(3, 2) * QE) / 9, (QE - QT) / 2
form = lambda Hmat: a_ * (Hmat * Hmat).trace() + b_ * Hmat.trace()**2 + c_ * sum(Hmat[i, i]**2 for i in range(3))
fit_ok = (sp.simplify(form(sp.Matrix(modes['T2'])) - QT) == 0
          and sp.simplify(form(sp.Matrix(modes['E'])) - QE) == 0
          and sp.simplify(form(sp.Matrix(modes['A1'])) - QA) == 0)
ok("M4", fit_ok, "Q = a tr h^2 + b (tr h)^2 + c sum h_ii^2 with a=Q_T/2, c=(Q_E-Q_T)/2, "
   "b=(Q_A-3Q_E/2)/9; at mu=0 Q_A=0 so b/a = -(1+c/a)/3")

# ---------------------------------------------------------------- family H
def avg_poly(poly):  # <x^n> = C(2n,n)/4^n, independent axes
    P = sp.Poly(sp.expand(poly), x1, x2, x3)
    tot = sp.Integer(0)
    for mon, co in P.terms():
        t = co
        for n in mon:
            t *= sp.binomial(2 * n, n) / sp.Integer(4)**n
        tot += t
    return sp.nsimplify(tot)


kk = sp.symbols('k', real=True)
mom_ok = all(sp.integrate(sp.sin(kk)**(2 * n), (kk, 0, 2 * sp.pi)) / (2 * sp.pi)
             == sp.binomial(2 * n, n) / sp.Integer(4)**n for n in range(0, 7))
S = x1 + x2 + x3
Dco = [2 * sp.binomial(sp.Rational(-5, 2), n) * avg_poly(w * S**n) for n in range(5)]
want = [sp.Rational(3, 4), sp.Rational(-65, 16), sp.Rational(8155, 512),
        sp.Rational(-113085, 2048), sp.Rational(11823735, 65536)]
ok("H1", mom_ok and Dco == want and Dco[1] / Dco[0] == sp.Rational(-65, 12),
   "D = <2w/E^5> = 3/4 mu^-5 - 65/16 mu^-7 + 8155/512 mu^-9 - 113085/2048 mu^-11 "
   "+ 11823735/65536 mu^-13 + ...")
dEh = sp.simplify(to_x(cE - cT) / 16 / (2 * w))   # b = -dh s/2: |b|^2 terms carry 1/4
dEe = sp.simplify(to_x(cE - cT) / 4 / (2 * w))    # b = de s
ok("H2", dEh == sp.Rational(1, 16) and dEe == sp.Rational(1, 4),
   "m_E - m_T = <w/(8E^5)> = D/16 per unit dh; = <w/(2E^5)> = D/4 per unit frame "
   "displacement de (dh = -2de); a common factor for all three parts")
wplus = 3 * x1 * x2 + sp.Rational(1, 2) * (x1**2 + x2**2)
Wp = avg_poly(wplus * S**2)
nu0 = sp.Integer(16)
lb = sp.Rational(3, 8) - sp.Rational(65, 32) / nu0 - sp.Rational(35, 8) * Wp / nu0**2
ok("H3", avg_poly(w) == sp.Rational(3, 8) and avg_poly(w * S) == sp.Rational(13, 16) and lb > 0,
   f"D >= 2mu^-5[3/8 - (65/32)/mu^2 - (35/8)W+/mu^4], W+ = {Wp}; = {lb} > 0 at mu^2 = 16")

# ---------------------------------------------------------------- family L
t, z = sp.symbols('t z', nonnegative=True)
N = 14
xm = [sp.binomial(2 * n, n) / sp.Integer(4)**n for n in range(N + 3)]
fser = [sum((-t)**n / sp.factorial(n) * xm[p + n] for n in range(N)) for p in range(3)]
M_ = N // 2 + 2
S0 = sum(z**(2 * m) / (4**m * sp.factorial(m)**2) for m in range(M_))
S1 = sum(z**(2 * m + 1) / (2 * 4**m * sp.factorial(m) * sp.factorial(m + 1)) for m in range(M_))
S2 = sum(z**(2 * m) * (2 * m + 2) * (2 * m + 1) / (sp.factorial(m + 1)**2 * 4**(m + 1)) for m in range(M_))
ez = sum((-z)**n / sp.factorial(n) for n in range(N + 2))
cl = [ez * S0, ez * (S0 - S1) / 2, ez * (S0 - 2 * S1 + S2) / 4]
ser_ok = all(sp.expand(sp.series(cl[p].subs(z, t / 2) - fser[p], t, 0, N - 1).removeO()) == 0
             for p in range(3))
mm = sp.symbols('m', nonnegative=True, integer=True)
rho = [1 / (4 * (mm + 1)**2), 1 / (4 * (mm + 1) * (mm + 2)),
       (2 * mm + 3) / (2 * (mm + 2) * (2 * mm + 2) * (2 * mm + 1))]
terms = [1 / (4**mm * sp.factorial(mm)**2), 1 / (2 * 4**mm * sp.factorial(mm) * sp.factorial(mm + 1)),
         (2 * mm + 2) * (2 * mm + 1) / (sp.factorial(mm + 1)**2 * 4**(mm + 1))]
ratio_ok = all(sp.simplify(sp.combsimp(terms[j].subs(mm, mm + 1) / terms[j]) - rho[j]) == 0
               for j in range(3))
mono_ok = True
for r_ in rho:
    num, den = sp.fraction(sp.together(r_ - r_.subs(mm, mm + 1)))
    mono_ok &= all(c > 0 for c in sp.Poly(sp.expand(num), mm).coeffs()) and \
        all(c > 0 for c in sp.Poly(sp.expand(den), mm).coeffs())
ok("L1", ser_ok and ratio_ok and mono_ok,
   "f_p(t)=<x^p e^{-tx}>: f0=e^-z S0, f1=e^-z(S0-S1)/2, f2=e^-z(S0-2S1+S2)/4, z=t/2 "
   "(to t^12); term ratios z^2 rho_m with rho_m decreasing")
F0, F1, F2 = sp.symbols('F0 F1 F2')


def lap(poly):  # <poly(x) e^{-t(x1+x2+x3)}> for independent axes
    P = sp.Poly(sp.expand(poly), x1, x2, x3)
    return sp.expand(sum(co * sp.Mul(*[[F0, F1, F2][e] for e in mon]) for mon, co in P.terms()))


ok("L2", lap(w) == 3 * F1**2 * F0 - F2 * F0**2 and lap(to_x(cT)) == 2 * F2 * F0**2
   and lap(to_x(cE)) == 6 * F1**2 * F0,
   "<w e^-tS> = 3f1^2f0 - f2f0^2 =: A - B; at mu=0 Q_E ~ 2A, Q_T ~ 2B (same factor)")

# ---------------------------------------------------------------- family R
iv.prec = 110
EPS = mpf(2)**-90


def ivq(x):
    return iv.mpf(x.numerator) / x.denominator


def series3(tt):
    zz_ = tt / 2
    zz = zz_ * zz_
    if zz_.b == 0:
        return iv.mpf(1), iv.mpf(1) / 2, iv.mpf(3) / 8

    def ssum(first, ratio):
        acc, term, m = iv.mpf(0), first, 0
        while True:
            acc += term
            r = ratio(m)
            nxt = term * r
            if r.b < 0.5 and nxt.b <= acc.a * EPS:
                return acc + iv.mpf([0, (nxt / (1 - r)).b])
            term, m = nxt, m + 1
    Z0 = ssum(iv.mpf(1), lambda m: zz / (4 * (m + 1)**2))
    Z1 = ssum(zz_ / 2, lambda m: zz / (4 * (m + 1) * (m + 2)))
    Z2 = ssum(iv.mpf(1) / 2, lambda m: zz * (2 * m + 3) / (2 * (m + 2) * (2 * m + 2) * (2 * m + 1)))
    e = iv.exp(-zz_)
    return e * Z0, e * (Z0 - Z1) / 2, e * (Z0 - 2 * Z1 + Z2) / 4


def AB(tt):
    f0, f1, f2 = series3(tt)
    return 3 * f1 * f1 * f0, f2 * f0 * f0


grid = [Fr(i, 256) for i in range(257)]
while grid[-1] < 400:
    xg = grid[-1] * Fr(65, 64)
    grid.append(Fr(-((-xg * 256) // 1), 256))
T = grid[-1]
n = len(grid) - 1
tv = [ivq(g) for g in grid]
vals = [AB(g) for g in tv]
W, LAM, CB, CV = [], [], [], []
for i in range(n):
    lo, hi = tv[i], tv[i + 1]
    w52 = (hi * hi * iv.sqrt(hi) - lo * lo * iv.sqrt(lo)) * 2 / 5
    w72 = (hi**3 * iv.sqrt(hi) - lo**3 * iv.sqrt(lo)) * 2 / 7
    cen = w72 / w52
    W.append(w52); LAM.append((cen - lo) / (hi - lo))
    CB.append(iv.mpf(cen.b)); CV.append(AB(iv.mpf(cen.b)))
PI, SQ2 = iv.pi, iv.sqrt(2)
SQPI, Ti = iv.sqrt(PI), ivq(T)
eT = iv.exp(-Ti / 2)
Gh = {0: SQPI, 1: SQPI / 2, 2: 3 * SQPI / 4}
kap = {p: Gh[p] / PI * (1 + (2 * p + 1) * (SQ2 - 1) / Ti)
       + (iv.mpf(1) / 2 if p == 0 else SQ2 / PI) * eT * Ti**p * iv.sqrt(Ti) for p in (0, 1, 2)}
lmb = {p: Gh[p] / PI * (1 - iv.mpf(2)**p * SQ2 * eT) for p in (0, 1, 2)}
tail = [iv.mpf([(3 * lmb[1]**2 * lmb[0] / Ti).a, (3 * kap[1]**2 * kap[0] / Ti).b]),
        iv.mpf([(lmb[2] * lmb[0]**2 / Ti).a, (kap[2] * kap[0]**2 / Ti).b])]


def low_int(j, nu):
    acc = iv.mpf(0)
    for i in range(n):
        F = CV[i][j] if nu is None else CV[i][j] * iv.exp(-CB[i] * nu)
        acc += W[i] * F
    return acc.a + (tail[j].a if nu is None else 0)


def up_int(j, nu):
    acc = iv.mpf(0)
    ex = None if nu is None else [iv.exp(-g * nu) for g in tv]
    for i in range(n):
        Fa, Fb = vals[i][j], vals[i + 1][j]
        if ex:
            Fa, Fb = Fa * ex[i], Fb * ex[i + 1]
        acc += W[i] * (Fa + LAM[i] * (Fb - Fa))
    tl = tail[j].b if nu is None else (tail[j] * iv.exp(-Ti * nu)).b
    return (acc + tl).b


lA, uA, lB, uB = low_int(0, None), up_int(0, None), low_int(1, None), up_int(1, None)
G52 = 3 * SQPI / 4
Dlo, Dhi = (2 * (iv.mpf(lA) - uB) / G52).a, (2 * (iv.mpf(uA) - lB) / G52).b
ok("R1", Dlo > 0, f"D(0) in [{float(Dlo):.5f}, {float(Dhi):.5f}] (quoted 0.124): "
   f"{n} cells to t={float(T):.1f}, Jensen/chord brackets, two-sided tails")
rlo, rhi = (iv.mpf(lA) / uB).a, (iv.mpf(uA) / lB).b
ca_lo, ca_hi, ba_lo, ba_hi = (rlo - 1).a, (rhi - 1).b, (-rhi / 3).a, (-rlo / 3).b
ok("R2", rlo > 1 and ba_lo > iv.mpf(-93) / 200,
   f"mu=0: Q_E/Q_T in [{float(rlo):.5f}, {float(rhi):.5f}]; c/a in [{float(ca_lo):.4f}, "
   f"{float(ca_hi):.4f}]; b/a in [{float(ba_lo):.4f}, {float(ba_hi):.4f}] (> -0.465)")
cells, nu_lo, step, worst = 0, Fr(0), Fr(1, 64), None
while nu_lo < 16:
    nu_hi = min(nu_lo + step, Fr(16))
    marg = low_int(0, ivq(nu_hi)) - up_int(1, None if nu_lo == 0 else ivq(nu_lo))
    if marg > 0:
        cells += 1
        worst = marg if worst is None or marg < worst else worst
        nu_lo, step = nu_hi, step * Fr(5, 4)
    else:
        step /= 2
        if step < Fr(1, 2**14):
            break
ok("R3", nu_lo >= 16, f"D(mu) > 0 on {cells} cells covering mu^2 in [0,16] (least lower "
   f"margin {float(worst.a):.2e}); with H3, D(mu) > 0 for every mu >= 0")

# ---------------------------------------------------------------- family K
al, be, ld = sp.symbols('alpha beta lamdot', real=True)
Kf = lambda Hd: al * (Hd * Hd).trace() + be * Hd.trace()**2
ck = sp.expand(Kf(2 * ld * sp.eye(3)) / ld**2)
kT = sp.expand(Kf(sp.Matrix(modes['T2'])))
ok("K1", ck == 12 * al + 36 * be and ck.subs(be, -al) == -24 * al and kT.subs(be, -al) == 2 * al,
   "member on h=2lam*1: (12a+36b)lamdot^2 = -24a lamdot^2 at b=-a; on unit shear T2: +2a")
ok("K2", sp.expand(ck.subs(be, -al) * kT.subs(be, -al)) == -48 * al**2,
   "the two values have opposite signs for every alpha != 0: the member's form is "
   "indefinite; a PSD form (or any positive sum of them) takes no negative value")

print(f"checks: {'all passed' if not FAILS else 'FAILED ' + ' '.join(FAILS)}")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
    sys.exit(1)
print("SUMMARY: PROVED (family R by interval arithmetic, ASSUMED A1) cranking inertia of the "
      "half-filled staggered sea: exact per-mode formula, PSD, dilation part zero iff mu=0, "
      "exact hopping coefficients of D, D(mu)>0 for every mu, and no PSD response equals "
      "the member's indefinite form")
print("HIT: For H = sigma.(e s) + mu(-1)^(x1+x2+x3), e = (1+h)^(-1/2), the half-filled sea's "
      "cranking inertia per site is m(dh) = <(|s x dh s|^2 + mu^2|dh s|^2)/(16E^5)>, "
      "E^2 = |s|^2+mu^2: positive semidefinite, positive on every traceless stretch, dilation "
      "part <mu^2|s|^2/(16E^5)>, zero exactly at mu = 0. m_E - m_T = D/16 per unit dh (D/4 per "
      "unit frame displacement) with D = <2w/E^5> = 3/4 mu^-5 - 65/16 mu^-7 + 8155/512 mu^-9 "
      "- ...; interval arithmetic gives D(0) in [0.1238, 0.1241] and D(mu) > 0 for every mu, "
      "so the sea's inertia always carries a positive cubic-only term. At mu = 0, "
      "b/a = -(1+c/a)/3 with c/a in [0.3935, 0.3944], b/a in [-0.4648, -0.4645] (quoted "
      "-0.47). The member's alpha[tr hdot^2 - (tr hdot)^2] is -24 alpha lamdot^2 on the "
      "dilation and +2 alpha on a unit shear, so no positive semidefinite response equals it.")
