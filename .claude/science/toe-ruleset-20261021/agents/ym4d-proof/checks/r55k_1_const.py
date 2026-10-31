#!/usr/bin/env python3
# checks/r55k_1_const.py -- REVIEW55_CONST (batch C5), reviewer model claude-opus-5-5.
# Criteria: checks/r55k_1_criteria.md, written BEFORE this file (2026-10-28T22:36:31Z).
# Plain python3 -I. fractions.Fraction + math.isqrt only. Every transcendental value is a rigorous
# rational interval: log by 2*atanh series with explicit tail bound, exp by Taylor with explicit
# remainder bound + repeated squaring, sqrt by integer isqrt. Outward rounding to PB significant bits.
from fractions import Fraction as Fr
from math import isqrt
import sys, time

T0 = time.time()
PB = 300            # relative precision (bits) of outward rounding
JLOG = 75           # atanh series terms (z <= 1/3 -> tail < 3^-151)
NEXP = 40           # Taylor terms for exp on |u| <= 1/8

def _sh(x):
    n, d = abs(x.numerator), x.denominator
    return PB - (n.bit_length() - d.bit_length())
def rd(x):
    x = Fr(x)
    if x == 0: return x
    s = _sh(x); y = x * (Fr(2) ** s)
    return Fr(y.numerator // y.denominator) / (Fr(2) ** s)
def ru(x):
    x = Fr(x)
    if x == 0: return x
    s = _sh(x); y = x * (Fr(2) ** s)
    return Fr(-((-y.numerator) // y.denominator)) / (Fr(2) ** s)

class I:
    __slots__ = ('lo', 'hi')
    def __init__(s, lo, hi=None, raw=False):
        if hi is None: hi = lo
        lo, hi = Fr(lo), Fr(hi)
        assert lo <= hi, (lo, hi)
        if raw: s.lo, s.hi = lo, hi
        else:   s.lo, s.hi = rd(lo), ru(hi)
    @staticmethod
    def c(x):  # exact constant, no rounding
        x = Fr(x); return I(x, x, raw=True)
    def __add__(a, b):
        b = b if isinstance(b, I) else I.c(b); return I(a.lo + b.lo, a.hi + b.hi)
    __radd__ = __add__
    def __neg__(a): return I(-a.hi, -a.lo, raw=True)
    def __sub__(a, b):
        b = b if isinstance(b, I) else I.c(b); return a + (-b)
    def __rsub__(a, b): return I.c(b) - a
    def __mul__(a, b):
        b = b if isinstance(b, I) else I.c(b)
        p = [a.lo * b.lo, a.lo * b.hi, a.hi * b.lo, a.hi * b.hi]
        return I(min(p), max(p))
    __rmul__ = __mul__
    def inv(a):
        assert a.lo > 0 or a.hi < 0, "division by interval containing 0"
        return I(1 / a.hi, 1 / a.lo)
    def __truediv__(a, b):
        b = b if isinstance(b, I) else I.c(b); return a * b.inv()
    def __rtruediv__(a, b): return I.c(b) * a.inv()
    def mid(a): return (a.lo + a.hi) / 2
    def __pow__(a, n):   # [run-2 fix: run 1 aborted in section G on 'I ** int'; nothing else changed]
        assert isinstance(n, int) and n >= 1
        r = a
        for _ in range(n - 1): r = r * a
        return r

def _atanh_lo(z):
    z = Fr(z); z2 = rd(z * z); pw = z; s = Fr(0)
    for j in range(JLOG):
        s = rd(s + rd(pw / (2 * j + 1))); pw = rd(pw * z2)
    return s
def _atanh_hi(z):
    z = Fr(z); z2 = ru(z * z); pw = z; s = Fr(0)
    for j in range(JLOG):
        s = ru(s + ru(pw / (2 * j + 1))); pw = ru(pw * z2)
    # tail: sum_{j>=J} z^{2j+1}/(2j+1) <= z^{2J+1}/((2J+1)(1-z^2)); pw = upper bound of z^{2J+1}
    return ru(s + ru(pw / ((2 * JLOG + 1) * (1 - z2))))
LN2 = I(2 * _atanh_lo(Fr(1, 3)), 2 * _atanh_hi(Fr(1, 3)))

def log_rat(x):
    x = Fr(x); assert x > 0
    n, d = x.numerator, x.denominator
    k = n.bit_length() - d.bit_length()
    y = x / (Fr(2) ** k)
    while y >= 2: y /= 2; k += 1
    while y < 1: y *= 2; k -= 1
    ylo, yhi = max(Fr(1), rd(y)), ru(y)
    zlo, zhi = rd((ylo - 1) / (ylo + 1)), ru((yhi - 1) / (yhi + 1))
    return I(2 * _atanh_lo(max(Fr(0), zlo)), 2 * _atanh_hi(zhi)) + LN2 * k
def LOG(a):
    a = a if isinstance(a, I) else I.c(a)
    return I(log_rat(a.lo).lo, log_rat(a.hi).hi)
LN10 = LOG(10)
def LOG10(a): return LOG(a) / LN10

def _exp_rat(x):
    x = Fr(x)
    if x < 0:
        e = _exp_rat(-x); return (rd(1 / e[1]), ru(1 / e[0]))
    s = 0
    while x / (Fr(2) ** s) > Fr(1, 8): s += 1
    u = x / (Fr(2) ** s)
    lo = hi = Fr(1); tl = th = Fr(1); fact = 1
    for nn in range(1, NEXP + 1):
        tl = rd(tl * u / nn); th = ru(th * u / nn)
        lo = rd(lo + tl); hi = ru(hi + th)
    # remainder <= 2 u^{N+1}/(N+1)!  (u <= 1/8)
    hi = ru(hi + ru(2 * th * u / (NEXP + 1)))
    for _ in range(s): lo = rd(lo * lo); hi = ru(hi * hi)
    return (lo, hi)
def EXP(a):
    a = a if isinstance(a, I) else I.c(a)
    return I(_exp_rat(a.lo)[0], _exp_rat(a.hi)[1], raw=True)
def POW(b, e):
    b = b if isinstance(b, I) else I.c(b)
    e = e if isinstance(e, I) else I.c(e)
    assert b.lo > 0
    return EXP(e * LOG(b))
def _sqrt_rat(x):
    x = Fr(x); assert x >= 0
    n, d = x.numerator, x.denominator; K = PB + 8
    v = isqrt(n * d << (2 * K))
    return (Fr(v, d << K), Fr(v + 1, d << K))
def SQRT(a):
    a = a if isinstance(a, I) else I.c(a)
    return I(_sqrt_rat(a.lo)[0], _sqrt_rat(a.hi)[1])

# ---------------------------------------------------------------- display
def sci(x, sig=7, up=False):
    x = Fr(x)
    if x == 0: return "0"
    neg = x < 0; x = abs(x)
    e = len(str(x.numerator)) - len(str(x.denominator))
    while x >= Fr(10) ** (e + 1): e += 1
    while x < Fr(10) ** e: e -= 1
    m = x / Fr(10) ** e * 10 ** (sig - 1)
    if up != neg: mi = -((-m.numerator) // m.denominator)
    else:         mi = m.numerator // m.denominator
    s = str(mi); s = s[0] + "." + s[1:] if len(s) > 1 else s
    return ("-" if neg else "") + s + "e" + str(e)
def S(a, sig=7):  # interval as [lo, hi]
    return "[%s, %s]" % (sci(a.lo, sig, False), sci(a.hi, sig, True))
def fx(x, k=6, up=False):
    x = Fr(x) * 10 ** k
    v = -((-x.numerator) // x.denominator) if up else x.numerator // x.denominator
    sgn = "-" if v < 0 else ""; v = abs(v); s = str(v).rjust(k + 1, "0")
    return sgn + s[:-k] + "." + s[-k:]
def SF(a, k=6): return "[%s, %s]" % (fx(a.lo, k), fx(a.hi, k, True))

OUT = []
def P(s=""): OUT.append(str(s)); print(s, flush=True)
VERD = []
def verdict(tag, ok, note=""):
    v = {True: "PASS", False: "FAIL", None: "UNDECIDED"}[ok]
    VERD.append((tag, v, note)); P("  >>> %s: %s %s" % (tag, v, note))
def inside(a, lo, hi):   # a subset of [lo, hi) -> True; disjoint -> False; else None
    lo, hi = Fr(lo), Fr(hi)
    if a.lo >= lo and a.hi < hi: return True
    if a.hi < lo or a.lo >= hi: return False
    return None
def le(a, b):  # interval a <= number b
    b = Fr(b)
    if a.hi <= b: return True
    if a.lo > b: return False
    return None
def E(m, e): return Fr(m) * Fr(10) ** e
def AND(*xs):
    if any(x is False for x in xs): return False
    if all(x is True for x in xs): return True
    return None

P("r55k_1_const.py  (REVIEW55_CONST)  PB=%d bits, JLOG=%d, NEXP=%d" % (PB, JLOG, NEXP))
P("sanity: ln2 = %s ; ln10 = %s" % (SF(LN2, 20), SF(LN10, 20)))
chk = LOG10(2) + LOG10(5); P("sanity: log10(2)+log10(5) = %s (must contain 1)" % SF(chk, 20))
assert chk.lo <= 1 <= chk.hi
s2 = SQRT(2); assert s2.lo ** 2 <= 2 <= s2.hi ** 2
ex = EXP(LN2); assert ex.lo <= 2 <= ex.hi
P("sanity: exp(ln2) = %s (must contain 2)" % SF(ex, 20))

# ---------------------------------------------------------------- B(m)
KB = 150
acc = I.c(0)
for k in range(1, KB + 1):
    acc = acc + LOG(2 ** k - 1) / (2 ** k)
tail_hi = (LN2 * (KB + 2) / (2 ** KB)).hi
LOGB1 = I(acc.lo, acc.hi + tail_hi)          # log B(1) = sum_{k>=1} log(2^k-1)/2^k
def Bm(m): return EXP(LOGB1 * m)
B4, B8 = Bm(4), Bm(8)
SQ6 = SQRT(6)

P(); P("=" * 100); P("A. CONST_T"); P("=" * 100)
P("A1  theta = 4/q at q = 5, 6, 7: %s" % [str(Fr(4, q)) for q in (5, 6, 7)])
verdict("A1 (CONST_T l.307-308: theta<=1/2 for every q>4)", all(Fr(4, q) <= Fr(1, 2) for q in (5, 6, 7)),
        "theta = 4/5, 2/3, 4/7 > 1/2; theta<=1/2 iff q>=8 (exact)")
def c_half(q):   # CONST_T c_theta, lambda = 1/(2 theta)
    th = Fr(4, 1) / q
    return (1 - th) * POW(2 * th, th / (1 - th))
def c_quarter(q):
    th = Fr(4, 1) / q
    return (1 - th) * POW(4 * th, th / (1 - th))
c5 = c_half(Fr(5)); P("A2  c_theta(q=5) = %s ; c_theta(q=6) = %s ; c_theta(q=8) = %s [CTRL-1]" %
                      (S(c5), S(c_half(Fr(6))), S(c_half(Fr(8)))))
verdict("A2 (CONST_T: c_theta<=1 for every q>4)", True if c5.hi <= 1 else (False if c5.lo > 1 else None),
        "c_theta(5) > 1")
verdict("CTRL-1 (c_theta(8) <= 1)", le(c_half(Fr(8)), 1))
# bracket for c_theta = 1 :  k(s) = s*log(2s/(1+s)) - log(1+s), s = theta/(1-theta); q = 4(1+s)/s
def ks(s): s = Fr(s); return s * LOG(2 * s / (1 + s)) - LOG(1 + s)
lo_s, hi_s = Fr(3), Fr(4)
assert ks(lo_s).hi < 0 and ks(hi_s).lo > 0
for _ in range(40):
    mid = (lo_s + hi_s) / 2; v = ks(mid)
    if v.hi < 0: lo_s = mid
    elif v.lo > 0: hi_s = mid
    else: break
P("A2b c_theta = 1 at s in [%s, %s] i.e. q in [%s, %s]: c_theta <= 1 iff q >= q_c" %
  (fx(lo_s, 8), fx(hi_s, 8, True), fx(4 * (1 + hi_s) / hi_s, 6), fx(4 * (1 + lo_s) / lo_s, 6, True)))
allok = True
for q in (8, 9, 10, 12, 16, 32, 100, 1000):
    v = c_quarter(Fr(q)); allok = allok and v.hi <= 1
    P("A3  c'_theta(q=%d) = %s" % (q, S(v)))
verdict("A3 (quarter-split constant <= 1 on the grid q>=8)", allok)
base = 36 * 2000 * 486
P("A4  dominant term 1/2*(36*2000*486)^{q/(q-4)}: q=5 -> base^5/2, q=6 -> base^3/2, q=8 -> base^2/2 ; base = %d" % base)
verdict("A4 (CONST_T: q=8 is the worst admissible choice, admissible = q>4)",
        (Fr(base) ** 5 <= Fr(base) ** 2) and (Fr(base) ** 3 <= Fr(base) ** 2),
        "base^5 and base^3 exceed base^2: q=5,6 are worse than q=8")
P("A5  B(4) = %s ; B(8) = %s" % (S(B4, 12), S(B8, 12)))
verdict("A5 (B(4)=43.95, B(8)=1931.5 within 0.05%)",
        inside(B4, Fr(4395, 100) * Fr(9995, 10000), Fr(4395, 100) * Fr(10005, 10000)) and
        inside(B8, Fr(19315, 10) * Fr(9995, 10000), Fr(19315, 10) * Fr(10005, 10000)))
fl8 = SQ6 * Fr(1758, 10) * B8 * Fr(1, 2) * (36 * 486) ** 2
P("A6  sqrt6*175.8*B(8)*1/2*(36*486)^2 = %s" % S(fl8))
verdict("A6 (CONST_T q=8 floor 1.27e14)", inside(fl8, E(1265, 11), E(1275, 11)))
x0 = SQRT(2 * E(1, 13) / (SQ6 * Fr(1758, 10) * B8)) / (36 * 486)
P("A6b C_1C_V at which the dominant term alone reaches 1e13 at q=8: %s (CONST_T: 0.2799)" % S(x0))

P(); P("=" * 100); P("B. STAR_CONST"); P("=" * 100)
Tst = (SQRT(387) - 18) / 4; kap = Fr(7, 8) - Tst
cs_iv = 8 * (9 / Tst + 2) / kap; cg_iv = 8 * 310 / kap + 272
T1 = (SQRT(396) - 18) / 4; csfloor = 8 * (9 / T1 + 2) / (1 - T1)
P("B1  T* = %s ; c_s = %s ; c_g = %s ; floor c_s(delta2=rho=0) = %s" % (S(Tst, 10), S(cs_iv, 13), S(cg_iv, 13), S(csfloor, 10)))
verdict("B1 (c_s 411.92, c_g 5699.63, floor 319.20)",
        AND(inside(cs_iv, Fr(41192, 100), Fr(41193, 100)), inside(cg_iv, Fr(569963, 100), Fr(569964, 100)),
             inside(csfloor, Fr(31919, 100), Fr(31921, 100))))
CS = I.c(Fr("411.9229708842423061")); CG = I.c(Fr("5699.632830341894211"))   # EPSSTAR l.130 / STAR_CONST l.380
P("    printed c_s, c_g inside the enclosures: %s %s" % (cs_iv.lo <= CS.lo <= cs_iv.hi, cg_iv.lo <= CG.lo <= cg_iv.hi))
def CT_star(q, F=Fr(1758, 10), R0=32, cs=CS, cg=CG, mu=3, Nmult=3, acgc=1, bconv="max"):
    q = Fr(q); a = q / (q - 4)
    src = Fr(1, 2) * POW(36 * cs * mu, a)
    vc = Fr(1, 2) * acgc ** 2
    Vinf = cs * POW(R0, -2 + 8 / q)
    cut = 288 * (cg + 18 * Vinf * Nmult)
    Bt = B8 if bconv == "max" else Bm(4 * a)
    return SQ6 * F * Bt * (src + vc + cut)
b11, b12, b100 = CT_star(11), CT_star(12), CT_star(100)
P("B2  STAR_CONST harness (R0=32, A_c g_c=1): C_T(11) = %s ; C_T(12) = %s ; C_T(100) = %s" % (S(b11), S(b12), S(b100)))
verdict("B2 (STAR_CONST 8.3: 9.8e12 / 5.3e12 / 1.4e12)",
        AND(inside(b11, E(975, 10), E(985, 10)), inside(b12, E(525, 10), E(535, 10)), inside(b100, E(135, 10), E(145, 10))))
b12c = CT_star(12, cg=I.c(20))
P("CTRL-3 C_T(12) with c_g -> 20: %s ; ratio to true %s" % (S(b12c), S(b12 / b12c, 6)))
verdict("CTRL-3 (C_1 choice moves C_T(12) by > 1%)", (b12 / b12c).lo > Fr(101, 100))
p1 = Fr("236.9") * CG
P("B3  236.9*c_g = %s ; c_g/20 = %s ; 236.9*c_g/4700 = %s ; 236.9*c_g/4738 = %s" %
  (S(p1, 12), S(CG / 20, 12), S(p1 / 4700, 12), S(p1 / 4738, 12)))
verdict("B3a (EPSSTAR l.218: 236.9*C_1 at C_1=c_g is 1.348e6)", inside(p1, E(13475, 2), E(13485, 2)))
verdict("B3b (x287 is the ratio of the C_1 values)", inside(CG / 20, Fr(2865, 10), Fr(2875, 10)))

P(); P("=" * 100); P("C. EPSSTAR"); P("=" * 100)
N3, N1 = 7 ** 4 * 6, 3 ** 4 * 6
n34 = POW(N3, Fr(3, 4)); r = POW(N3, Fr(1, 4)) / POW(N1, Fr(3, 4))
P("C1  |N_3|^{3/4} = %s (EPSSTAR 1314.21) ; |N_3|^{1/4}/|N_1|^{3/4} = %s (EPSSTAR 0.105889) ; |N_3|^{3/4}|N_1|^{1/4} = %s (EPSSTAR 6171.3)"
  % (S(n34, 10), S(r, 10), S(n34 * POW(N1, Fr(1, 4)), 10)))
verdict("C1a (|N_3|^{3/4} = 1314.21)", inside(n34, Fr("1314.205"), Fr("1314.215")))
verdict("C1b (ratio 0.105889)", inside(r, Fr("0.1058885"), Fr("0.1058895")))
verdict("C1c (ES-1 needs |N_3| < |N_1|^3, exact)", N3 < N1 ** 3, "%d < %d" % (N3, N1 ** 3))
def CS1sq(q, m, cs=CS, cg=CG, s1=4096):
    if q is None: cth, a = I.c(1), Fr(1)
    else:
        q = Fr(q); a = q / (q - 4); cth = c_quarter(q)
    return (1 / (Fr(3, 4) - Fr(1, 4) / m)) * (cth * POW(27 * cs, a) + s1 * cg)
def ACGC(q, m, **kw): return (1 + SQ6) * SQRT(CS1sq(q, m, **kw)) / m
cs1 = SQRT(CS1sq(12, 1))
P("C2  C_S1(12,1) = %s (EPSSTAR 6963.995)" % S(cs1, 10))
a1, a7, a19 = ACGC(12, 1), ACGC(12, 7), ACGC(12, 19615)
P("    A_c g_c bound m=1: %s ; m=7: %s ; m=19615: %s" % (S(a1, 8), S(a7, 8), S(a19, 8)))
verdict("C2 (6963.995 ; 2.402e4 ; 2.871e3 ; 0.99996)",
        AND(inside(cs1, Fr("6963.9945"), Fr("6963.9955")), inside(a1, E(24015, 0), E(24025, 0)),
             inside(a7, E(28705, -1), E(28715, -1)), inside(a19, Fr("0.999955"), Fr("0.999965"))))
def CT_eps(q, F=Fr(1758, 10), R0=64, cs=CS, cg=CG, Ns=3, m=19615, bconv="max", s1=4096, parts=False):
    if q is None: a, Vinf = Fr(1), POW(R0, -2)
    else:
        q = Fr(q); a = q / (q - 4); Vinf = POW(R0, -2 + 8 / q)
    src = Fr(1, 2) * POW(36 * cs * Ns, a)
    ac = ACGC(q, m, cs=cs, cg=cg, s1=s1)
    vc = Fr(1, 2) * ac * ac
    cut = 288 * (cg + 18 * (Ns * cs * Vinf + Fr(1, 36 * m)))
    Bt = B8 if bconv == "max" else Bm(4 * a)
    ct = SQ6 * F * Bt * (src + vc + cut)
    return (ct, src, vc, cut, ac) if parts else ct
c12 = CT_eps(12)
P("C3  C_T(12) EPSSTAR harness = %s" % S(c12, 10))
verdict("C3 (EPSSTAR C_T(12) = 5.288348e12)", inside(c12, Fr("5.2883475e12"), Fr("5.2883485e12")))
eps1 = E(67, -41); H = Fr("5.05e9")
tneed = 2 * eps1 * SQRT(H)
P("C4  t_need = 2*6.7e-40*sqrt(5.05e9) = %s ; t_need/3.01e-35 = %s ; sqrt10 = %s ; t_need/sqrt10 = %s"
  % (S(tneed, 10), S(tneed / E(301, -37), 10), S(SQRT(10), 10), S(tneed / SQRT(10), 10)))
verdict("C4a (EPSSTAR l.525: t_pr >= 3.01e-35)", inside(I.c(E(301, -37)) / tneed, Fr(995, 1000), Fr(1005, 1000)))
q10 = tneed / E(301, -37); s10 = SQRT(10)
verdict("C4b ('exactly sqrt10' as the ratio of printed numbers)", None if (q10.lo <= s10.hi and s10.lo <= q10.hi) else False)
verdict("C4c (slip: t_need/sqrt10 rounds to 3.01e-35)", inside(tneed / SQRT(10), E(3005, -38), E(3015, -38)))
cdc = 1 / SQRT(Fr("3.31e7") * tneed)
P("C5  C_D ceiling = %s (EPSSTAR 3.17e13) ; C_T at 0.9e3/0.5e3: %s / %s" % (S(cdc, 8), S(cdc / 900, 6), S(cdc / 500, 6)))
verdict("C5 (EPSSTAR l.525: C_D <= 3.17e13)", inside(cdc, E(3165, 10), E(3175, 10)))
cfl = CT_eps(12, cs=I.c(Fr("319.19798")))
P("C6  C_T(12) at c_s = 319.19798 with c_g held: %s ; log10(5.288348e12/that) = %s" % (S(cfl, 6), SF(LOG10(c12 / cfl), 4)))
verdict("C6i (EPSSTAR l.608: c_s floor gives C_T >= 4.4e12)", inside(cfl, E(435, 10), E(445, 10)))

P(); P("=" * 100); P("D. F / Stage-1 radius consistency"); P("=" * 100)
def Lam_i(i): return 2 - Fr(2) ** (1 - i)
def sig_i(i): return sum(Fr(j, 2 ** j) for j in range(i))
def istar(Sb, dmin=12):
    i = 0
    while Sb * Fr(2) ** (-i) / Lam_i(i + 1) >= dmin: i += 1
    return i
def logF(R, Sb, i):
    Lm = Lam_i(i)
    return 2 * LOG(R) - Lm * LOG(Sb / Lm) + LN2 * sig_i(i)
def Fmax(alpha, beta, R0, dmin=12, imax=45):
    alpha, beta = Fr(alpha), Fr(beta); best = None; rows = []
    for i in range(1, imax + 1):
        need_lo = dmin * Lam_i(i) * Fr(2) ** (i - 1)          # S >= need_lo  <=> i_* >= i
        need_hi = dmin * Lam_i(i + 1) * Fr(2) ** i             # S >= need_hi  <=> i_* >= i+1
        Rlo = -((-(need_lo + beta) / alpha).numerator // (need_lo + beta) .__truediv__(alpha).denominator) if False else None
        x = (need_lo + beta) / alpha; Rlo = -((-x.numerator) // x.denominator)
        x = (need_hi + beta) / alpha; Rhi = -((-x.numerator) // x.denominator) - 1
        a, b = max(Rlo, R0), Rhi
        if b < a: continue
        for RR in sorted(set([a, b])):
            Sb = alpha * RR - beta; ii = istar(Sb, dmin)
            assert ii == i, (RR, ii, i)
            lf = logF(RR, Sb, i)
            rows.append((RR, i, lf))
            if best is None or lf.lo > best[2].lo: best = (RR, i, lf)
    return best, rows
b1, rows1 = Fmax(Fr(1, 2), 4, 32)
P("D1  CONST_T budget R/2-4, R>=32: max F = %s at R=%d (i*=%d)" % (S(EXP(b1[2]), 8), b1[0], b1[1]))
for RR, i, lf in rows1[:8]: P("      R=%-7d i*=%-2d F=%s" % (RR, i, S(EXP(lf), 6)))
P("      ... asymptote check, last rows: " + "; ".join("R=%d F=%s" % (RR, sci(EXP(lf).lo, 5)) for RR, i, lf in rows1[-2:]))
verdict("D1 (reproduces CONST_T F_max = 175.8 at R = 79) [CTRL-4]", AND(b1[0] == 79, inside(EXP(b1[2]), Fr("175.75"), Fr("175.85"))))
b2, rows2 = Fmax(Fr(1, 4), 3, 64)
F2 = EXP(b2[2])
P("D2  Stage 2 inside B_{3R/4-3} (budget R/4-3), R>=64: max F = %s at R=%d (i*=%d)" % (S(F2, 8), b2[0], b2[1]))
for RR, i, lf in rows2[:6]: P("      R=%-7d i*=%-2d F=%s" % (RR, i, S(EXP(lf), 6)))
verdict("D2 (F = 175.8 is consistent with EPSSTAR's Stage-1 radii)", le(F2, Fr("175.8")))
P("D3  Stage-1 gap R/c-4 (>=12 for R>=16c), Stage-2 budget R(1/2-1/c)-3:")
D3 = {}
for cc in (8, 16, 32, 64, 128):
    bb, rr = Fmax(Fr(1, 2) - Fr(1, cc), 3, 16 * cc)
    D3[cc] = (bb[0], EXP(bb[2]))
    P("      c=%-4d R_0=%-5d max F = %s at R=%d (i*=%d)" % (cc, 16 * cc, S(EXP(bb[2]), 7), bb[0], bb[1]))
ct_d2 = CT_eps(12, F=F2.hi, R0=64)
P("D4  C_T(12) with D2's F (EPSSTAR's own radii, R0=64, m=19615) = %s" % S(ct_d2, 6))
verdict("D4 (C_T(12) <= 1e13 under EPSSTAR's own Stage-1 radii)", le(ct_d2, E(1, 13)))
for cc in (8, 16, 32, 64, 128):
    R0c, Fc = 16 * cc, D3[cc][1]
    s1 = 256 * cc * cc
    m1 = ACGC(12, 1, s1=s1).hi            # A_c g_c bound at m=1 ; any m >= that bound gives A_c g_c <= 1
    mm = int(-((-m1.numerator) // m1.denominator))
    acm = ACGC(12, mm, s1=s1)
    ctc = CT_eps(12, F=Fc.hi, R0=R0c, m=mm, s1=s1)
    P("      c=%-4d R0=%-5d m=%-8d A_c g_c<=%s  C_T(12) = %s ; eps_* factor vs m=19615: %s" %
      (cc, R0c, mm, sci(acm.hi, 4, True), S(ctc, 6), sci(Fr(19615, mm), 4)))

P(); P("=" * 100); P("E. TAUFLAT"); P("=" * 100)
w = SQRT(1 / (Fr("3.31e7") * 53 * Fr("2.75e-15")))
P("E1  C_D window = %s" % SF(w, 7))
verdict("E1 (C_D <= 455.283301)", inside(w, Fr("455.2833"), Fr("455.2834")))
CD9 = 900 * Fr("5.288e12"); cflat, Cp = Fr(1, 640), Fr(53)
thS = 1 / (Fr("3.31e7") * CD9 ** 2)
etaA = cflat * Fr("2.75e-15") ** 2 / Cp ** 2; etaB = cflat * (thS / Cp) ** 2 / Cp ** 2
gap = LOG10(etaA / etaB); sh = LOG10(4 * eps1 ** 2 / etaB)
Hx = 640 * 53 ** 4; tneedx = 2 * eps1 * SQRT(Hx)
P("E2  log10(eta_A/eta_B) = %s ; shortfall log10(4eps^2/eta_B) = %s ; t_need(640*53^4) = %s"
  % (SF(gap, 6), SF(sh, 6), S(tneedx, 8)))
verdict("E2 (52.077 ; 9.707 ; 9.5224e-35)", AND(inside(gap, Fr("52.0765"), Fr("52.0775")), inside(sh, Fr("9.7065"), Fr("9.7075")),
        inside(tneedx, E(95215, -39), E(95225, -39))))
cdx = 1 / SQRT(Fr("3.31e7") * tneedx)
P("    C_D ceiling (640*53^4) = %s ; C_T band /900, /500 = %s , %s" % (S(cdx, 8), S(cdx / 900, 6), S(cdx / 500, 6)))
r080, r578 = LOG10(Fr("5.288e12") / Fr("4.4e12")), LOG10(Fr("5.288e12") / Fr("1.396e12"))
P("E3  log10(5.288/4.4) = %s ; log10(5.288/1.396) = %s" % (SF(r080, 6), SF(r578, 6)))
verdict("E3 (0.080 ; 0.578 as arithmetic)", AND(inside(r080, Fr("0.0795"), Fr("0.0805")), inside(r578, Fr("0.5775"), Fr("0.5785"))))
# E4: rigorous lower bound, option A, P-max
# C_B^tot = 8(2/d2+4) + C_B^s + (O(eps) pieces), C_B^s = 4 + 8(1+||V_s||_inf) >= 12  ->  C_B^tot >= 16/d2 + 44
Ac, Bc, Cc = 54 * 8 * 9, 288 * 8 * 16, 54 * 8 * 2 + 288 * 8 * 44
Pp = SQRT(Ac) + SQRT(Bc)
Pp = Pp * Pp
wst = ((Cc + Pp) - SQRT((Cc + Pp) * Pp)) / Cc
fw = Pp / (wst * (1 - wst)) + Cc / wst
Chat_min = fw + 288 * 272
Fmins = []
for i in range(1, 40):
    Lm, sg = Lam_i(i), sig_i(i)
    v = EXP(LOG(62) * (2 - Lm) + LOG(2 * Lm) * Lm + LN2 * sg)
    Fmins.append((i, v))
Fmin_lb = min(v.lo for i, v in Fmins)
mono = all(Fmins[k][1].lo <= Fmins[k + 1][1].hi for k in range(7, 38))
lb = SQ6 * Fmin_lb * B8 * Chat_min
Lam_inf = Fr(16) * (Fr("4.94") + Fr("3.34"))
need = (cdx / 2 - Fr("46.8")) / (Fr("1.011") * 1 * Lam_inf)
P("E4  Chat_min (all allocations, all q, P-max) >= %s ; F_min (R>=64, any i*) >= %s at i*=%d ; C_T >= %s"
  % (sci(Chat_min.lo, 6), sci(Fmin_lb, 5), min(Fmins, key=lambda t: t[1].lo)[0], sci(lb.lo, 5)))
P("    (2Lam)^Lam*2^sig*64^{2-Lam} by i*: " + ", ".join("%d:%s" % (i, sci(v.lo, 4)) for i, v in Fmins[:10]))
P("    most lenient DESC-eps need (c_N=1, q->inf, C_3=1): C_T <= %s ; margin log10(lb/need) = %s" % (sci(need.hi, 5, True), SF(LOG10(lb / need), 4)))
verdict("E4 (option A dead under P-max for every allocation, q>=8, R0>=64)", (lb.lo > need.hi) if True else None)
lbct = SQ6 * Fmin_lb * B4 * Chat_min
P("    same bound under P-ct (B(4) instead of B(8)): C_T >= %s  (need %s) -> not decisive under P-ct" % (sci(lbct.lo, 4), sci(need.hi, 4, True)))

P(); P("=" * 100); P("F. EPS1_SWEEP / EPS1_EXEC"); P("=" * 100)
def aRS(e): return Fr(e) ** 4 / (4 * 9216 ** 2)
DX = Fr("2.456e-152")
for lab, e in (("6.7e-40", Fr("6.7e-40")), ("8.95e-40", Fr("8.95e-40")), ("9.52e-40", Fr("9.52e-40")), ("1.27e-39", Fr("1.27e-39")), ("1.2687e-39", Fr("1.2687e-39"))):
    P("F1  eps_1=%-10s a_RS = %s ; margin log10(a_RS/100/DX') = %s" % (lab, sci(aRS(e), 7), SF(LOG10(aRS(e) / 100 / DX), 4)))
m67 = LOG10(aRS(eps1) / 100 / DX)
verdict("F1 (a_RS 5.93136e-166 ; margin -15.617)", AND(inside(I.c(aRS(eps1)), E(5931355, -172), E(5931365, -172)), inside(m67, Fr("-15.6175"), Fr("-15.6165"))))
cr = (Fr("1.2687e-39") * Fr("6.7e-40")) / (Fr("8.95e-40") * Fr("9.52e-40"))
crlo = (Fr("1.26865e-39") * Fr("6.65e-40")) / (Fr("8.955e-40") * Fr("9.525e-40"))
crhi = (Fr("1.26875e-39") * Fr("6.75e-40")) / (Fr("8.945e-40") * Fr("9.515e-40"))
P("F2  cross-ratio = %s ; range over the printed rounding intervals = [%s, %s]" % (fx(cr, 6), fx(crlo, 6), fx(crhi, 6, True)))
verdict("F2a ('exactly factorising')", cr == 1, "cross-ratio %s" % fx(cr, 6))
verdict("F2b ('factorising within printed precision')", crlo <= 1 <= crhi)
g0 = Fr("1.57e-76"); ep = Fr("9.38495112638e-45")
rr = (g0 / ep) / (g0 / eps1)
P("F3  (g/eps_1 at proposed)/(g/eps_1 now) at fixed g = %s ; log10 = %s" % (sci(rr, 7), SF(LOG10(rr), 6)))
verdict("F3 (EPS1_SWEEP: 2m*g/eps_1 shrinks as eps_1 falls at fixed g)", rr < 1)
eta12 = Fr("3.52309230578e-88"); bnd = SQRT(eta12 / 4)
rel = (ep - bnd) / bnd
P("F4  sqrt(3.52309230578e-88/4) = %s ; 9.38495112638e-45 relative excess = %s" % (S(bnd, 16), S(rel, 6)))
verdict("F4a (EPS1_SWEEP's 9.38495112638e-45 admissible)", ep <= bnd.lo if ep <= bnd.lo else (False if ep > bnd.hi else None))
verdict("F4b (EPS1_EXEC: excess 2.3406e-13)", inside(rel, E(234055, -18), E(234065, -18)))
verdict("CTRL-2 (9.38495112637e-45 admissible)", Fr("9.38495112637e-45") <= bnd.lo)
Dl = LOG10(eps1 / ep)
P("F5  Delta = %s ; 2D = %s ; 3D = %s ; 4D = %s" % (SF(Dl, 9), SF(2 * Dl, 6), SF(3 * Dl, 6), SF(4 * Dl, 6)))
verdict("F5 (4.853643 ; 9.707 ; 14.561 ; 19.415)", AND(inside(Dl, Fr("4.8536425"), Fr("4.8536435")), inside(2 * Dl, Fr("9.7065"), Fr("9.7075")),
        inside(3 * Dl, Fr("14.5605"), Fr("14.5615")), inside(4 * Dl, Fr("19.4145"), Fr("19.4155"))))
c8 = CT_eps(8)
P("F6  C_T(8) in EPSSTAR's convention = %s ; 2log10(C_T(12)/C_T(8)) = %s ; with 1.27e14: %s" %
  (S(c8, 6), SF(2 * LOG10(c12 / c8), 4), SF(2 * LOG10(Fr("5.288e12") / Fr("1.27e14")), 4)))
verdict("F6 (EPS1_EXEC q=8 row uses the same-convention C_T)", inside(c8, E(126, 12), E(128, 12)))
etaT = 1 / (640 * Fr(53) ** 4 * Fr("3.31e7") ** 2 * CD9 ** 4)
P("F7  eta_flat at C_D = 900*5.288e12 exactly = %s (EPS1_SWEEP 3.52309230578e-88; from t_pr=1.33384e-39: %s)" %
  (sci(etaT, 13), sci(Fr(1, 640) * Fr("1.33384e-39") ** 2 / Fr(53) ** 4, 13)))
verdict("F7 (EPS1_SWEEP's 12-digit eta_flat equals the chain value)", sci(etaT, 12) == sci(Fr("3.52309230578e-88"), 12))

P(); P("=" * 100); P("G. QFIX"); P("=" * 100)
def Lam(q):
    if q is None: return I.c(Lam_inf)
    q = Fr(q); return 4 * POW(2, 2 + 4 / q) * (Fr("4.94") + Fr("3.34") * POW(32, 1 / q))
P("G1  Lambda(8) = %s ; Lambda(12) = %s ; Lambda(inf) = %s" % (SF(Lam(8), 6), SF(Lam(12), 6), SF(Lam(None), 6)))
verdict("G1 (228.333 ; 189.459 ; 132.48)", AND(inside(Lam(8), Fr("228.3325"), Fr("228.3335")), inside(Lam(12), Fr("189.4585"), Fr("189.4595")),
        Lam_inf == Fr("132.48")))
def CD(q, cN=2): return 2 * (Fr("1.011") * cN * Lam(q) * CT_eps(q) + Fr("46.8"))
def cut_of(q, cN=2): return 1 / (Fr("3.31e7") * CD(q, cN) ** 2) / (2 * SQRT(H))
cd11, cd12, cd115 = CD(11), CD(12), CD(Fr(23, 2))
P("G2  C_D(11) = %s (/6.7e15 = %s) ; C_D(12) = %s ; C_D(11.5) = %s" % (S(cd11, 6), S(cd11 / Fr("6.7e15"), 6), S(cd12, 6), S(cd115, 6)))
verdict("G2a (q=11 fails by x1.16)", AND(cd11.lo > Fr("6.7e15"), inside(cd11 / Fr("6.7e15"), Fr("1.155"), Fr("1.165"))))
verdict("G2b (q=12 passes)", le(cd12, Fr("6.7e15")))
verdict("G2c (q=12 is the lowest admissible real q)", False if cd115.hi <= Fr("6.7e15") else (None if cd115.lo <= Fr("6.7e15") else True))
lo_q, hi_q = Fr(11), Fr(23, 2)
for _ in range(30):
    mq = (lo_q + hi_q) / 2; v = CD(mq)
    if v.lo > Fr("6.7e15"): lo_q = mq
    elif v.hi <= Fr("6.7e15"): hi_q = mq
    else: break
P("    real threshold q* (C_D(q*) = 6.7e15, c_N = 2) in [%s, %s]" % (fx(lo_q, 5), fx(hi_q, 5, True)))
def obj(q, cN=2):
    c = cut_of(q, cN)
    e_eff = c if c.hi < eps1 else None
    assert e_eff is not None
    return LOG10(e_eff ** 4 / (4 * 9216 ** 2) / 100 / DX)
o8, oinf, o1000, o100, o12 = obj(8), obj(None), obj(1000), obj(100), obj(12)
P("G3  obj(8) = %s ; obj(12) = %s ; obj(100) = %s ; obj(1000) = %s ; obj(inf) = %s" % (SF(o8, 6), SF(o12, 6), SF(o100, 6), SF(o1000, 6), SF(oinf, 6)))
P("    lever obj(inf)-obj(8) = %s ; obj(inf)-obj(12) = %s ; cutoff-only lever (=lever/4) = %s" % (SF(oinf - o8, 6), SF(oinf - o12, 6), SF((oinf - o8) / 4, 6)))
verdict("G3 (total lever 24.089)", inside(oinf - o8, Fr("24.0885"), Fr("24.0895")))
k1000, k100 = cut_of(1000), cut_of(100)
P("G4  eps_cut(1000) = %s ; eps_cut(100) = %s ; eps_cut(12) = %s" % (S(k1000, 8), S(k100, 8), S(cut_of(12), 8)))
verdict("G4a (3.8235e-43)", inside(k1000, E(38234500, -50), E(38235500, -50)))
verdict("G4b (3.8e-43 admissible at q=1000)", le(I.c(Fr("3.8e-43")), k1000.lo) if True else None)
verdict("G4c (QFIX 3.5e-43 admissible at q=100)", True if Fr("3.5e-43") <= k100.lo else (False if Fr("3.5e-43") > k100.hi else None))
def theta_eps(q, es=Fr("1.12e-37")):
    if q is None: return I.c(es) / (16 * Fr("3.34"))
    q = Fr(q); return es / (16 * Fr("3.34") * POW(32, 1 / q))
th1000 = theta_eps(1000)
tSUP1000 = 1 / (Fr("3.31e7") * CD(1000) ** 2)
cutT = th1000 / (2 * SQRT(H))
esneed = tSUP1000 * 16 * Fr("3.34") * POW(32, Fr(1, 1000))
P("G5  theta_eps(1000) at eps_*=1.12e-37 = %s ; t_SUP(1000) = %s ; cutoff via theta_eps = %s ; eps_* needed = %s"
  % (S(th1000, 7), S(tSUP1000, 7), S(cutT, 7), S(esneed, 7)))
verdict("G5 (Codex 1.4695e-44 ; 2.9141e-36)", AND(inside(cutT, E(146945, -49), E(146955, -49)), inside(esneed, E(29135, -40), E(29145, -40))))
X27 = 27 * CS
P("G6  sign change of d/dq of the A_c g_c bound at q = 16*27*c_s = %s" % S(16 * X27, 12))
for qq in (10 ** 5, 177950, 177951, 10 ** 6, 10 ** 7):
    P("      q=%-9d A_c g_c bound (m=19615) = %s" % (qq, S(ACGC(qq, 19615), 15)))
verdict("G6 (QFIX row 4 'wants q large' for all q)", (ACGC(10 ** 6, 19615).lo < ACGC(10 ** 5, 19615).lo) if False else
        (False if ACGC(10 ** 7, 19615).lo > ACGC(10 ** 6, 19615).hi else None), "bound rises between q=1e6 and 1e7")
for qq in (10 ** 6, 10 ** 12, 10 ** 30, 10 ** 60):
    dct = CT_eps(qq) - CT_eps(None)
    P("      C_T(q) - C_T(inf) at q=1e%d: %s" % (len(str(qq)) - 1, S(dct, 4)))
qx = Fr("1.168e-12") * Fr("3.31e7") * CD(None) ** 2
P("G7  theta_G = theta_SUP(inf) at q = %s ; theta_G = theta_eps(inf; 1.12e-37) at q = %s" % (S(qx, 6), S(Fr("1.168e-12") / theta_eps(None), 6)))
verdict("G7 (QFIX 5.573e26 reproduces as theta_G vs theta_eps at eps_*=1.12e-37)", inside(Fr("1.168e-12") / theta_eps(None), E(55725, 22), E(55735, 22)))
grid = [8, 9, 10, 11, 12, 13, 14, 16, 20, 24, 32, 50, 100, 200, 1000, 10 ** 4, 10 ** 6]
ovals = [(qq, obj(qq)) for qq in grid]
inc = all(ovals[k][1].hi < ovals[k + 1][1].lo for k in range(len(ovals) - 1))
P("G8  obj strictly increasing on QFIX's grid: %s ; obj(1e4)-obj(1000) = %s ; obj(1e6)-obj(1000) = %s" %
  (inc, SF(ovals[-2][1] - o1000, 6), SF(ovals[-1][1] - o1000, 6)))
verdict("G8 ('argmax q = 1000' on QFIX's own grid)", all(o1000.lo >= v.hi for qq, v in ovals))
verdict("CTRL-5 (q=1000 is the argmax of the grid truncated at 1000)", all(o1000.lo >= v.hi for qq, v in ovals if qq < 1000))

P(); P("=" * 100); P("SUMMARY"); P("=" * 100)
for t, v, n in VERD: P("  %-85s %s" % (t, v))
P("runtime %.1f s" % (time.time() - T0))
