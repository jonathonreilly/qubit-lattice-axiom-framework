#!/usr/bin/env python3
"""J:derive:plane-memory-loss-2:a2 -- the sphere kernel's chordal Wasserstein sensitivity is 1/3.

Kernel K_V(ds) = (k/(4 pi sinh k)) e^{V.s} dsigma on S^2, k = |V|, A(k) = coth k - 1/k, y = A/k.
Claim (ATTEMPT.md): for |V| <= 3 and every unit d, the chordal Kantorovich-Rubinstein norm of
d.grad_V K_V is <= 1/3, so W_1(K_V, K_V') <= |V - V'|/3 for |V|,|V'| <= 3, and block 27's causal
coupling contracts by beta per level: for every beta < 1 one invariant law and m_t <= beta^t.

Families:
  S  symbolic identities (sympy): moments, monotonicity series, the flows, the energy formula
  R1 small-k region (0, 1/10]: exact rational series bound + crude bounds
  R2 k in [1/10, 3]: interval arithmetic on integers scaled by 2^256 with outward rounding
  N  numerical cross-checks (floats; labelled, not load-bearing)
Every load-bearing claim is exact (sympy / Fraction / outward-rounded integer intervals).
"""
import sys
import time
from fractions import Fraction as F

import sympy as sp

T0 = time.time()
FAILS = []


def ok(tag, cond, msg=""):
    if cond:
        print("ok " + tag + (" " + msg if msg else ""))
    else:
        print("FAIL " + tag + (" " + msg if msg else ""))
        FAILS.append(tag)


k, t, z, u, w = sp.symbols("k t z u w", positive=False, real=True)
kp = sp.symbols("kp", positive=True)
A_ = sp.coth(kp) - 1 / kp                       # A(k)
Ap_ = 1 / kp**2 - 1 / sp.sinh(kp) ** 2          # A'(k)

# ---------------------------------------------------------------- S1 kernel moments
Zw = sp.integrate(sp.exp(kp * w), (w, -1, 1))
m1 = sp.integrate(w * sp.exp(kp * w), (w, -1, 1)) / Zw
m2 = sp.integrate(w**2 * sp.exp(kp * w), (w, -1, 1)) / Zw
ok("S1.mean", sp.simplify((m1 - A_).rewrite(sp.exp)) == 0, "E[w]=coth k-1/k")
ok("S1.second", sp.simplify((m2 - (1 - 2 * A_ / kp)).rewrite(sp.exp)) == 0, "E[w^2]=1-2A/k")
ok("S1.var", sp.simplify((m2 - m1**2 - Ap_).rewrite(sp.exp)) == 0, "Var w = A' = 1/k^2-1/sinh^2 k")
ok("S1.derivA", sp.simplify((sp.diff(A_, kp) - Ap_).rewrite(sp.exp)) == 0, "dA/dk = A'")
# transverse second moment per direction: (1 - E w^2)/2 = A/k
ok("S1.transverse", sp.simplify(((1 - m2) / 2 - A_ / kp).rewrite(sp.exp)) == 0, "E[(s.w)^2]=(1-E[w^2])/2=A/k for w perp V")

# ---------------------------------------------------------------- S2 A'' < 0 (sinh^3 x > x^3 cosh x)
x = sp.symbols("x")
ser = sp.series(sp.sinh(x) ** 3 - x**3 * sp.cosh(x), x, 0, 26).removeO()
good = True
for n in range(0, 26):
    c = ser.coeff(x, n)
    if n % 2 == 1 and n >= 3:
        pred = sp.Rational(3**n - 3 - 4 * n * (n - 1) * (n - 2), 4 * sp.factorial(n))
    else:
        pred = 0
    good &= sp.simplify(c - pred) == 0
ok("S2.series", good, "sinh^3x - x^3 cosh x = sum_{n odd} [(3^n-3)-4n(n-1)(n-2)] x^n/(4 n!) to x^25")
ok("S2.coeffs", all(3**n - 3 - 4 * n * (n - 1) * (n - 2) == 0 for n in (3, 5))
   and all(3**n - 3 - 4 * n * (n - 1) * (n - 2) > 0 for n in range(7, 400, 2))
   and 3**7 > 4 * 7**3, "zero at n=3,5; positive n>=7 (induction 3^n>=4n^3 from n=7)")
# A'' = -2/k^3 + 2 cosh/sinh^3 ; A''<0 <=> k^3 cosh k < sinh^3 k
App = sp.diff(Ap_, kp)
ok("S2.Appform", sp.simplify(App - (-2 / kp**3 + 2 * sp.cosh(kp) / sp.sinh(kp) ** 3)) == 0,
   "A'' = -2/k^3 + 2cosh/sinh^3")

# ---------------------------------------------------------------- S3 ball integrals
C_ = kp / (4 * sp.pi * sp.sinh(kp))
r = sp.symbols("r", positive=True)
ballk = C_ * sp.integrate(r**2 * 4 * sp.pi * sp.sinh(kp * r) / (kp * r), (r, 0, 1))
ok("S3.mass", sp.simplify((ballk - A_ / kp).rewrite(sp.exp)) == 0, "int_B C e^{V.x} dx = A/k")
Iball = (4 * sp.pi / kp) * (sp.cosh(kp) / kp - sp.sinh(kp) / kp**2)   # int_B e^{k z} dx
ok("S3.Iball", sp.simplify((C_ * Iball - A_ / kp).rewrite(sp.exp)) == 0, "int_B e^{kz} = (4pi/k)(cosh/k - sinh/k^2)")
beta1 = C_ * sp.diff(Iball, kp)
ok("S3.beta1", sp.simplify((beta1 - (1 - 3 * A_ / kp) / kp).rewrite(sp.exp)) == 0,
   "int_B z k~ = (1/k)(1-3A/k)")

# ---------------------------------------------------------------- S4 the source flow J_1 (pq-flow)
a_ = 1 - 3 * A_ / kp
fT = sp.exp(kp * t) * (1 - t**2) * (a_ - A_ * t)
I0 = sp.integrate(sp.exp(kp * t) * (1 - t**2), (t, -1, 1))
I1 = sp.integrate(t * sp.exp(kp * t) * (1 - t**2), (t, -1, 1))
ok("S4.I0", sp.simplify((I0 - 4 * A_ * sp.sinh(kp) / kp**2).rewrite(sp.exp)) == 0, "I0 = 4A sinh k/k^2")
ok("S4.I1", sp.simplify((I1 - 4 * a_ * sp.sinh(kp) / kp**2).rewrite(sp.exp)) == 0, "I1 = 4a sinh k/k^2")
ok("S4.N1", sp.simplify((a_ * I0 - A_ * I1).rewrite(sp.exp)) == 0, "N(1) = a I0 - A I1 = 0")
# ODE: with N' = f, q = N e^{-kz}/(1-z^2)^2, p = A/k - z q : 3p + z p' + q' + k(pz+q) = 1
Nf = sp.Function("N")
aS, AS = sp.symbols("a A", real=True)
fz = sp.exp(k * z) * (1 - z**2) * (aS - AS * z)
q = Nf(z) * sp.exp(-k * z) / (1 - z**2) ** 2
p = AS / k - z * q
expr = 3 * p + z * sp.diff(p, z) + sp.diff(q, z) + k * (p * z + q) - 1
expr = expr.subs(sp.Derivative(Nf(z), z), fz)
expr = sp.simplify(expr.subs(aS, 1 - 3 * AS / k))
ok("S4.ode", expr == 0, "div W + k W_z = 1 for W = p x + q zhat")
ok("S4.flux", sp.simplify(p + z * q - AS / k) == 0, "W.s = p + z q = A/k on S^2")
# energy: int over the disk rho<r of |p x + q zhat|^2 2 pi rho = pi r^2[(pz+q)^2 + p^2 r^2/2]
rho, pS, qS = sp.symbols("rho pS qS", real=True)
rr = sp.symbols("rr", positive=True)
disk = sp.integrate((pS**2 * (rho**2 + z**2) + 2 * pS * qS * z + qS**2) * 2 * sp.pi * rho, (rho, 0, rr))
ok("S4.disk", sp.simplify(disk - sp.pi * rr**2 * ((pS * z + qS) ** 2 + pS**2 * rr**2 / 2)) == 0)
br = ((AS / k - z * qS) * z + qS) ** 2 + (AS / k - z * qS) ** 2 * (1 - z**2) / 2
br2 = AS**2 / (2 * k**2) * (1 + z**2) + (AS / k) * z * qS * (1 - z**2) + qS**2 * (1 - z**2) * (1 - z**2 / 2)
ok("S4.bracket", sp.expand(br - br2) == 0, "(pz+q)^2+p^2(1-z^2)/2 = t1,t2,t3 integrands")
# t2: d/dz[z^2 N/2] = z N + z^2 f/2  (so int zN = -1/2 int z^2 f, N(+-1)=0)
ok("S4.t2parts", sp.simplify(sp.diff(z**2 * Nf(z) / 2, z).subs(sp.Derivative(Nf(z), z), fz)
                             - (z * Nf(z) + z**2 * fz / 2)) == 0)
# u-representations of N
fu_left = (sp.exp(k * t) * (1 - t**2) * (aS - AS * t)).subs(t, -1 + (1 + z) * u) * (1 + z)
fu_left2 = (1 + z) ** 2 * sp.exp(k * (-1 + (1 + z) * u)) * u * (2 - (1 + z) * u) * (aS + AS - AS * (1 + z) * u)
ok("S4.uleft", sp.simplify(fu_left - fu_left2) == 0, "N(z)=(1+z)^2 int_0^1 e^{k(-1+(1+z)u)} u(2-(1+z)u)(a+A-A(1+z)u)du")
fu_right = -(sp.exp(k * t) * (1 - t**2) * (aS - AS * t)).subs(t, 1 - (1 - z) * u) * (1 - z)
fu_right2 = (1 - z) ** 2 * sp.exp(k * (1 - (1 - z) * u)) * u * (2 - (1 - z) * u) * (AS - aS - AS * (1 - z) * u)
ok("S4.uright", sp.simplify(fu_right - fu_right2) == 0, "N(z)=(1-z)^2 int_0^1 e^{k(1-(1-z)u)} u(2-(1-z)u)(A-a-A(1-z)u)du")
# omega, phi~ integral forms
Y = sp.symbols("Y", positive=True)
om_int = sp.integrate(2 * u * sp.exp(-Y * (1 - u)), (u, 0, 1))
ph_int = sp.integrate(u * sp.exp(-Y * u), (u, 0, 1))
ok("S4.omega", sp.simplify(om_int - 2 * (Y - 1 + sp.exp(-Y)) / Y**2) == 0)
ok("S4.phi", sp.simplify(ph_int - (1 - (1 + Y) * sp.exp(-Y)) / Y**2) == 0)

# ---------------------------------------------------------------- S5 the directional flow and the energy formula
cS, ApS, e1S = sp.symbols("c Ap e1", real=True)
Aeq = 1 - 2 * AS / k - AS**2          # A' as the variance of w
dJ1 = cS * ((AS / k) * AS - (1 - 3 * AS / k) / k)          # int_B d.J_1 = (A/k)(F.d) - c beta1
ok("S5.dJ1", sp.simplify(dJ1 - (cS / k) * (AS / k - Aeq)) == 0, "int_B d.J_1 = (c/k)(A/k - A')")
E2 = AS / k - 2 * (k * cS) * dJ1 + (k * cS) ** 2 * e1S
ok("S5.E2", sp.simplify(E2 - (AS / k - cS**2 * (2 * (AS / k - Aeq) - k**2 * e1S))) == 0,
   "int |J_d|^2/k~ = A/k - c^2[2(A/k - A') - k^2 e1]")
yS = sp.symbols("y", positive=True)
Bform = 1 / (9 * yS) + yS - 2 * ApS
ok("S5.B", sp.simplify(Bform - ((1 - 3 * yS) ** 2 / (9 * yS) + 2 * (sp.Rational(1, 3) - ApS))) == 0,
   "B = 1/(9y) - 2A' + y = (1-3y)^2/(9y) + 2(1/3 - A')")
ok("S5.target", sp.simplify(yS * (2 * ApS - yS + e1S) - sp.Rational(1, 9) + yS * (Bform - e1S)) == 0,
   "y(2A' - y + k^2 e1) <= 1/9  <=>  k^2 e1 <= B")
# reflection coupling for rotations: cost 2 A (Vhat.n), |V - RV| = 2k (Vhat.n)
print("note S5.refl: mirror coupling cost 2A(Vhat.n) = (A/k)|V-RV| (argument in ATTEMPT step 4)")

# ---------------------------------------------------------------- R1 small k: (0, 1/10]
# E(k) = k^2 - sinh^2 k (1 - k^2/3 + k^4/20) = sum e_n k^{2n};  E >= 0  <=>  1/3 - A' >= k^2/20
def s_(n):
    return F(2 ** (2 * n - 1), sp.factorial(2 * n)) if n >= 1 else F(0)


def e_(n):
    if n == 1:
        return F(1) - s_(1)
    return -(s_(n) - s_(n - 1) / 3 + (s_(n - 2) / 20 if n >= 2 else 0))


serE = sp.series(x**2 - sp.sinh(x) ** 2 * (1 - x**2 / 3 + x**4 / 20), x, 0, 22).removeO()
ok("R1.Eseries", all(sp.Rational(e_(n).numerator, e_(n).denominator) == serE.coeff(x, 2 * n) for n in range(1, 11)))
ok("R1.e123", e_(1) == 0 and e_(2) == 0 and e_(3) == F(1, 60), "e1=e2=0, e3=1/60")
# sum_{m>=2} s_m = sinh^2(1) - 1 <= partial(2..12) + tail, tail <= 2 * s_13
part = sum(s_(m) for m in range(2, 13))
tailS = 2 * s_(13)
Ssum_hi = part + tailS
ok("R1.ssum", Ssum_hi < F(2, 5), "sum_{m>=2} s_m < 2/5")
Tbound = (1 + F(1, 3) + F(1, 20)) * Ssum_hi          # >= sum_{n>=4} |e_n|
ok("R1.E>=0", F(1, 60) - Tbound / 100 > 0, "E(k)/k^6 >= 1/60 - k^2 sum|e_n| > 0 for k<=1/10")
# e < 3125/1024 so e^{1/5} <= 5/4
e_hi = sum(F(1, sp.factorial(n)) for n in range(0, 15)) + F(2, sp.factorial(15))
ok("R1.e", e_hi < F(3125, 1024), "e^{1/5} <= 5/4")
# S <= 2/81 + (1/3)(1/30)/16 + A^2(4 + e^{2k})/4 with A <= 1/30
S1 = F(2, 81) + F(1, 3) * F(1, 30) / 16 + F(1, 900) * (4 + F(5, 4)) / 4
ok("R1.S", S1 < F(1, 10), "t1u+t2u+T3u <= %s < 1/10 <= B/k^2 on (0,1/10]" % str(round(float(S1), 5)))

# ---------------------------------------------------------------- R2 interval arithmetic on [1/10, 3]
P = 256
SC = 1 << P


def fdiv(a, b):
    return a // b


def cdiv(a, b):
    return -((-a) // b)


class IV:
    __slots__ = ("lo", "hi")

    def __init__(s, lo, hi):
        assert lo <= hi
        s.lo, s.hi = lo, hi

    @staticmethod
    def q(v):
        v = F(v)
        return IV(fdiv(v.numerator * SC, v.denominator), cdiv(v.numerator * SC, v.denominator))

    def __add__(s, o):
        o = o if isinstance(o, IV) else IV.q(o)
        return IV(s.lo + o.lo, s.hi + o.hi)

    __radd__ = __add__

    def __neg__(s):
        return IV(-s.hi, -s.lo)

    def __sub__(s, o):
        o = o if isinstance(o, IV) else IV.q(o)
        return IV(s.lo - o.hi, s.hi - o.lo)

    def __rsub__(s, o):
        return (-s) + o

    def __mul__(s, o):
        if not isinstance(o, IV):
            o = F(o)
            if o >= 0:
                return IV(fdiv(s.lo * o.numerator, o.denominator), cdiv(s.hi * o.numerator, o.denominator))
            return -(s * (-o))
        pr = (s.lo * o.lo, s.lo * o.hi, s.hi * o.lo, s.hi * o.hi)
        return IV(fdiv(min(pr), SC), cdiv(max(pr), SC))

    __rmul__ = __mul__

    def recip(s):
        assert s.lo > 0
        return IV(fdiv(SC * SC, s.hi), cdiv(SC * SC, s.lo))

    def __truediv__(s, o):
        if not isinstance(o, IV):
            o = F(o)
            assert o > 0
            return IV(fdiv(s.lo * o.denominator, o.numerator), cdiv(s.hi * o.denominator, o.numerator))
        return s * o.recip()

    def up(s):
        return F(s.hi, SC)

    def dn(s):
        return F(s.lo, SC)


ONE = IV(SC, SC)


def iexp(v):
    v = F(v)
    if v < 0:
        return iexp(-v).recip()
    m = 0
    while v / (1 << m) > F(1, 256):
        m += 1
    tt = IV.q(v / (1 << m))
    term, tot = ONE, ONE
    for n in range(1, 31):
        term = (term * tt) / n
        tot = tot + term
    tot = IV(tot.lo, tot.hi + 1)          # Taylor remainder < 2^-300 < one unit
    for _ in range(m):
        tot = tot * tot
    return tot


def kvals(kk):
    E = iexp(kk)
    E2 = E * E
    den = E2 - ONE
    A = (E2 + ONE) / den - IV.q(F(1) / kk)
    y = A / kk
    a = ONE - 3 * y
    Ap = IV.q(F(1) / (kk * kk)) - (4 * E2) / (den * den)
    piC = (E * kk) / (2 * den)           # pi C = k/(4 sinh k)
    return A, Ap, y, a, piC


def cellcheck(k0, k1, nz):
    A0, Ap0, y0, a0, piC0 = kvals(k0)
    A1, Ap1, y1, a1, piC1 = kvals(k1)
    signs = (y0.up() <= F(1, 3)) and (a0.dn() >= 0) and ((A0 - a1).dn() > 0) and ((A1 - a0).dn() > 0)
    B0 = ((ONE - 3 * y0) * (ONE - 3 * y0)) / (9 * y0) + 2 * (IV.q(F(1, 3)) - Ap0)
    t1u = (y0 * y0 * y0 * (ONE - y0)).up()
    t2u = ((y0 * (A1 - a0)) / 16).up()
    em = iexp(-k0 / nz)
    Em = [ONE]
    for _ in range(2 * nz):
        Em.append(Em[-1] * em)                       # e^{-k0 i/nz}
    ep0 = iexp(k0 / nz)
    eneg = [None] * (2 * nz + 1)
    cur = iexp(-k0)
    for i in range(0, nz + 1):
        eneg[i] = cur                                # e^{k0 z_i}, z_i <= 0
        cur = cur * ep0
    ep1 = iexp(k1 / nz)
    epos = [None] * (2 * nz + 1)
    cur = ONE
    for i in range(nz, 2 * nz + 1):
        epos[i] = cur                                # e^{k1 z_i}, z_i >= 0
        cur = cur * ep1
    emk1 = iexp(-k1 / nz)
    eR = [None] * (2 * nz + 1)
    cur = iexp(3 * k1)
    for j in range(0, 2 * nz + 1):
        eR[j] = cur                                  # e^{k1(2 - z_j)}
        cur = cur * emk1

    def om(i):
        if i == 0:
            return ONE
        Yv = F(k0) * i / nz
        return 2 * (IV.q(Yv) - ONE + Em[i]) / (Yv * Yv)

    def ph(i):
        if i == 0:
            return IV.q(F(1, 2))
        Yv = F(k0) * i / nz
        return (ONE - (ONE + IV.q(Yv)) * Em[i]) / (Yv * Yv)

    aA = a1 + A1
    aA2 = aA * aA
    Am = A1 - a0
    Am2 = Am * Am
    T = F(0)
    for j in range(2 * nz):
        zl = F(-1) + F(j, nz)
        zh = F(-1) + F(j + 1, nz)
        mm = F(0) if zl <= 0 <= zh else min(zl * zl, zh * zh)
        pre = (1 - mm / 2) * (1 - mm) ** 2
        cands = []
        if zh < 1:
            eL = epos[j + 1] if zh >= 0 else eneg[j + 1]
            o = om(j)
            cands.append(((aA2 * eL * o * o) / ((1 - zh) ** 4)).up())
        if zl > -1:
            pp = ph(2 * nz - j - 1)
            cands.append(((4 * Am2 * eR[j] * pp * pp) / ((1 + zl) ** 4)).up())
        T += F(1, nz) * pre * min(cands)
    T3u = piC0.up() * T
    lhs = k1 * k1 * (t1u + t2u + T3u)
    return B0.dn(), lhs, (t1u, t2u, T3u), signs


worst = None
ncell = 0
allok = True
kk = F(1, 10)
while kk < 3:
    k1 = min(F(3), kk + F(1, 100))
    B0, lhs, parts, signs = cellcheck(kk, k1, 100)
    ncell += 1
    if not (lhs <= B0 and signs):
        allok = False
    rr_ = B0 / lhs
    if worst is None or rr_ < worst[0]:
        worst = (rr_, kk, parts)
    kk = k1
ok("R2.cells", allok, "%d k-cells of width 1/100 on [1/10,3] x 200 z-cells of width 1/100: y<=1/3, a>=0, A-a>0, k1^2(t1u+t2u+T3u) <= B(k0)" % ncell)
print("   worst margin B/lhs = %.4f at k in [%s, %s]; t1u,t2u,T3u = %.5f %.5f %.5f"
      % (float(worst[0]), worst[1], worst[1] + F(1, 100), *[float(v) for v in worst[2]]))

# consequences (exact)
ok("C.oneSite", all(float(sp.N(sp.coth(3 * sp.Rational(b, 10)) - 1 / (3 * sp.Rational(b, 10)))) < b / 10
                    for b in range(1, 10)), "spot check (floats; implied by A(k)<k/3): one-site rate A(3b) < b")
print("note C.sharp: block 27 T4 gives W1 >= |F(V)-F(V')| with A(d)/d -> 1/3, so 1/3 is sharp")

# ---------------------------------------------------------------- N numerical cross-checks (floats, not load-bearing)
try:
    import numpy as np
    from scipy.integrate import quad
    from scipy.optimize import linprog
    import scipy.sparse as sps

    def pq_e1(kk):
        A = 1 / np.tanh(kk) - 1 / kk
        C = kk / (4 * np.pi * np.sinh(kk))
        a = 1 - 3 * A / kk
        f = lambda s: np.exp(kk * s) * (1 - s * s) * (a - A * s)
        N = lambda s: quad(f, -1, s, epsabs=1e-14)[0]
        EK = lambda h: 2 * np.pi * C * quad(lambda s: np.exp(kk * s) * h(s), -1, 1)[0]
        y = A / kk
        t1 = y * y * EK(lambda s: 1 - s**4) / 4
        t2 = (y / 4) * EK(lambda s: s * s * (1 - s * s) * (A * s - a))
        t3 = np.pi * C * quad(lambda s: np.exp(-kk * s) * (1 - s * s / 2) * N(s) ** 2 / (1 - s * s) ** 2,
                              -1 + 1e-9, 1 - 1e-9, limit=200)[0]
        return A, 1 / kk**2 - 1 / np.sinh(kk) ** 2, t1 + t2 + t3

    A1n, Ap1n, e1n = pq_e1(1.0)
    cc = 0.6
    E2n = A1n - cc * cc * (2 * (A1n - Ap1n) - e1n)
    bound = np.sqrt(A1n * E2n)
    Nn = 400
    ii = np.arange(Nn) + 0.5
    zz = 1 - 2 * ii / Nn
    rr2 = np.sqrt(1 - zz * zz)
    phs = np.pi * (1 + 5 ** 0.5) * ii
    Spts = np.stack([rr2 * np.cos(phs), rr2 * np.sin(phs), zz], 1)
    uu = np.array([np.sqrt(1 - cc * cc), 0, cc])
    wts = np.exp(1.0 * Spts[:, 2])
    wts /= wts.sum()
    g = wts * (Spts @ uu - (wts * (Spts @ uu)).sum())
    Pp = np.where(g > 0)[0]
    Qq = np.where(g < 0)[0]
    cost = np.linalg.norm(Spts[Pp][:, None, :] - Spts[Qq][None, :, :], axis=2)
    nP, nQ = len(Pp), len(Qq)
    rows = np.concatenate([np.repeat(np.arange(nP), nQ), nP + np.tile(np.arange(nQ), nP)])
    cols = np.concatenate([np.arange(nP * nQ), np.arange(nP * nQ)])
    Aeq = sps.csr_matrix((np.ones(2 * nP * nQ), (rows, cols)), shape=(nP + nQ, nP * nQ))
    bb = np.concatenate([g[Pp], -g[Qq] * g[Pp].sum() / (-g[Qq]).sum()])
    lp = linprog(cost.ravel(), A_eq=Aeq, b_eq=bb, bounds=(0, None), method="highs").fun
    print("N.lp NUMERICAL k=1, d at 53 deg from V: discrete KR norm %.4f (400 pts) vs flow bound %.4f vs A/k %.4f"
          % (lp, bound, A1n))
except Exception as ex:  # numerical block is not load-bearing
    print("N.skip numerical block skipped: " + type(ex).__name__)

print("runtime %.1f s" % (time.time() - T0))
if FAILS:
    print("CHECK FAIL: " + ", ".join(FAILS))
    print("SUMMARY: ROUTE FAILS AT a failed exact check (" + ", ".join(FAILS) + ")")
    sys.exit(1)
HITS = [
    "HIT: for the sphere formation law's kernel K_V (weight e^{V.s}) the chordal Wasserstein "
    "sensitivity to the predecessor sum is at most 1/3: W1(K_V,K_V') <= |V-V'|/3 whenever |V|,|V'| <= 3 "
    "(sharp: block 27's T4 lower bound), proved by an explicit divergence-free flow in the ball, a "
    "Cauchy-Schwarz with weight C e^{V.x} (whose ball integral is exactly A/k), and an outward-rounded "
    "interval check of one scalar inequality on k in [1/10,3] (margin >= 1.73).",
    "HIT: hence block 27's causal coupling contracts by beta per level and, for every beta < 1, the "
    "sphere formation law on the infinite plane has one invariant law, rotation-invariant, and from the "
    "aligned plane m_t <= beta^t -- closing the band [1/sqrt3, 1) left by block 27; beta < 1 is the full "
    "reach of any uniform causal-coupling argument.",
    "HIT: transverse directions exactly: for w perpendicular to V the sensitivity is A(|V|)/|V| "
    "(flow C e^{V.x} w; lower bound by the test function s.w), and for every rotation R, "
    "W1(K_V,K_RV) = (A/k)|V-RV| exactly (mirror coupling above, a linear test function below).",
]
print("SUMMARY: PARTIAL m_t -> 0 on the infinite plane, with m_t <= beta^t and one rotation-invariant "
      "invariant law, for every beta < 1 (was beta < 1/sqrt3); every beta >= 1 open: no uniform "
      "causal-coupling argument passes beta = 1")
print("\n".join(HITS))
