#!/usr/bin/env python3
# sr2_55_1 — SRC2_55 elementary constants (exact rational arithmetic only; no floats in any verdict).
# Criteria: sr2_55_1_criteria.md (written first). Writes nothing; prints to stdout.
from fractions import Fraction as Fr
from math import comb, factorial
import random

results = []
def gate(name, ok, detail=""):
    results.append(("gate", name, bool(ok)))
    print(f"{name}: {'PASS' if ok else 'FAIL'} {detail}")
def control(name, fired, detail=""):
    results.append(("control", name, bool(fired)))
    print(f"{name}: {'FIRED' if fired else 'DID NOT FIRE'} {detail}")

def ceil_fr(q):
    q = Fr(q)
    return -((-q.numerator) // q.denominator)

# ---------- rigorous exponential enclosures ----------
def P(x, N):
    x = Fr(x); s = Fr(0); t = Fr(1)
    for k in range(N + 1):
        if k > 0:
            t = t * x / k
        s += t
    return s

def EU(x):
    """rational upper bound for e^{-x}, x >= 0 (1/P_N(x) <= ... valid for every N since P_N(x) <= e^x)."""
    x = Fr(x)
    if x < 0:
        raise ValueError
    N = 30 if x > 130 else max(30, min(400, ceil_fr(3 * x)))
    return 1 / P(x, N)

def EL(x):
    """rational lower bound for e^{-x}, x >= 0; returns 0 (trivially valid) for large x."""
    x = Fr(x)
    if x < 0:
        raise ValueError
    if x >= 40:
        return Fr(0)
    N = 80
    tail = x ** (N + 1) / (factorial(N + 1) * (1 - x / (N + 2)))
    return 1 / (P(x, N) + tail)

# sanity of the enclosures (not a gate of the file's claims, but a guard on the tool): EL(x) <= EU(x) on samples
assert all(EL(Fr(k, 7)) <= EU(Fr(k, 7)) for k in range(0, 200))

# ---------- G1: Bell numbers ----------
B = [1]
for n in range(0, 80):
    B.append(sum(comb(n, k) * B[k] for k in range(n + 1)))
g1 = all(B[n] <= factorial(n) for n in range(1, 81))
gate("G1 Bell B_n <= n! (n=1..80)", g1, f"B_10={B[10]}, 10!={factorial(10)}")
c1 = any(B[n] > factorial(n - 1) for n in range(1, 81))
first = next(n for n in range(1, 81) if B[n] > factorial(n - 1))
control("C1 false bound B_n <= (n-1)!", c1, f"first failure n={first}: B={B[first]} > {factorial(first-1)}")

# ---------- G2: Proposition NF ----------
prod1 = Fr(1); prod2 = Fr(1)
ok_a = True; ok_b = True
c2 = False; c2b = False
for K in range(1, 401):
    prod1 *= (1 + Fr(1, K))
    prod2 *= (1 + Fr(1, K * K))
    if prod1 != K + 1:
        ok_a = False
    if not (prod2 < 4):
        ok_b = False
    if prod1 > 4:
        c2 = True
    if not (prod2 < 3):
        c2b = True
gate("G2a prod_{i<=K}(1+1/i) = K+1 (K=1..400)", ok_a, f"K=400 value {prod1}")
gate("G2b prod_{i<=K}(1+1/i^2) < 4 (K=1..400)", ok_b, f"K=400 value in ({Fr(prod2.numerator*1000//prod2.denominator,1000)}, +1/1000)")
control("C2 false 'prod(1+1/i) <= 4 for all K<=400'", c2)
control("C2b false 'prod(1+1/i^2) < 3 for all K<=400'", c2b)

# ---------- G3: Lemma SSUM ----------
def S_upper(d, L, tau):
    d = Fr(d); L = Fr(L); tau = Fr(tau)
    Jlow = 10
    s = Fr(0)
    for j in range(-Jlow, 0):
        x = tau * L ** j
        s += x ** 4 * EU(d * x / 2)
    # j >= 0 up to J where x_{J+1} >= 200/d
    j = 0
    while True:
        x = tau * L ** j
        if x >= 200 / d and x >= 16 / d:
            break
        s += x ** 4 * EU(d * x / 2)
        j += 1
    x1 = tau * L ** j          # x_{J+1}: first term NOT summed explicitly
    M = x1 ** 4 * EU(d * x1 / 4)
    tail_high = M * EU(d * x1 / 4) / (1 - EU(d * x1 * (L - 1) / 4))
    tail_low = tau ** 4 * L ** (-4 * (Jlow + 1)) / (1 - L ** (-4))
    return s + tail_high + tail_low

def S_lower(d, L, tau):
    d = Fr(d); L = Fr(L); tau = Fr(tau)
    s = Fr(0)
    for j in range(-10, 12):
        x = tau * L ** j
        s += x ** 4 * EL(d * x / 2)
    return s

def Shat_lower(d, L):
    d = Fr(d); L = Fr(L)
    first = L ** 4 / (L ** 4 - 1)
    second = (16 / d) ** 4 * EL(4) * EL(d / 4) / (1 - EL(d * (L - 1) / 4))
    return first + second

params = [(Fr(1, 10), 3), (Fr(1, 2), 3), (Fr(1), 3), (Fr(2), 3), (Fr(1), 5), (Fr(4), 7)]
taus = [Fr(1), Fr(5, 4), Fr(3, 2), Fr(2), Fr(5, 2), Fr(29, 10)]
g3 = True; c3 = False; worst = None
for (d, L) in params:
    sh = Shat_lower(d, L)
    tl = [t for t in taus if t < L] + ([Fr(4)] if L == 5 else []) + ([Fr(6)] if L == 7 else [])
    for tau in tl:
        su = S_upper(d, L, tau)
        if not (su <= sh):
            g3 = False
            print(f"   G3 violation at d={d}, L={L}, tau={tau}")
        ratio = su / sh
        if worst is None or ratio > worst[0]:
            worst = (ratio, d, L, tau)
        if S_lower(d, L, tau) > Fr(L) ** 4 / (Fr(L) ** 4 - 1):
            c3 = True
gate("G3 S^+(tau) <= Shat^-(d,L) on all samples", g3,
     f"max S^+/Shat^- = {Fr(worst[0].numerator*10**6//worst[0].denominator, 10**6)} at d={worst[1]}, L={worst[2]}, tau={worst[3]}")
control("C3 wrong bound L^4/(L^4-1) exceeded by a rigorous S^-", c3)

# ---------- G4: Proposition HOM ----------
class C:
    __slots__ = ("re", "im")
    def __init__(self, re, im=0):
        self.re = Fr(re); self.im = Fr(im)
    def __add__(s, o):
        o = o if isinstance(o, C) else C(o); return C(s.re + o.re, s.im + o.im)
    __radd__ = __add__
    def __sub__(s, o):
        o = o if isinstance(o, C) else C(o); return C(s.re - o.re, s.im - o.im)
    def __rsub__(s, o):
        return C(o) - s
    def __mul__(s, o):
        o = o if isinstance(o, C) else C(o)
        return C(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)
    __rmul__ = __mul__
    def inv(s):
        n = s.re * s.re + s.im * s.im
        return C(s.re / n, -s.im / n)
    def __truediv__(s, o):
        o = o if isinstance(o, C) else C(o); return s * o.inv()
    def __eq__(s, o):
        o = o if isinstance(o, C) else C(o); return s.re == o.re and s.im == o.im
    def abs2(s):
        return s.re * s.re + s.im * s.im

rng = random.Random(55021)
def rq(lo=-20, hi=20, den=17):
    return Fr(rng.randint(lo, hi), rng.randint(1, den))
ok_a = True; n_a = 0
while n_a < 100:
    u = C(rq(), rq()); e = C(rq(-5, 5, 9), rq(-5, 5, 9))
    if u.abs2() == 0 or e.abs2() == 0 or e == C(1) or e == C(-1):
        continue
    cs = [u * (1 + e), u * (1 + e), u * (1 - e), u * (1 - e)]
    if any(c.abs2() == 0 for c in cs):
        continue
    ssum = C(0)
    for c in cs:
        ssum = ssum + c.inv()
    lhs = ssum.inv()
    rhs = u * (1 - e * e) / 4
    if not (lhs == rhs):
        ok_a = False
    n_a += 1
ok_b = True
for _ in range(50):
    cs = [Fr(rng.randint(1, 50), rng.randint(1, 13)) for _ in range(4)]
    Phi = Fr(rng.randint(-30, 30), rng.randint(1, 7))
    S = sum(1 / c for c in cs)
    F = [Phi / (c * S) for c in cs]
    E = sum(c * f * f for c, f in zip(cs, F)) / 2
    if sum(F) != Phi or E != Phi * Phi / (2 * S):
        ok_b = False
    for _ in range(20):
        dd = [Fr(rng.randint(-9, 9), rng.randint(1, 5)) for _ in range(3)]
        dd.append(-sum(dd))
        if all(x == 0 for x in dd):
            continue
        Ed = sum(c * (f + x) ** 2 for c, f, x in zip(cs, F, dd)) / 2
        if not (Ed > E):
            ok_b = False
u, e, Cb = Fr(1000), Fr(1, 4), Fr(1000)
ok_c = (u / 4) * e * e > Cb / u
gate("G4a harmonic identity (Sum 1/c)^-1 = (u/4)(1-eps^2), 100 complex samples", ok_a)
gate("G4b Lagrange minimiser exact and strictly below 1000 feasible perturbations", ok_b)
gate("G4c size: (u/4)eps^2 > C_b/u at u=1000, eps=1/4, C_b=1000", ok_c, f"{(u/4)*e*e} > {Cb/u}")
ceff = (Fr(1) / 4) * (1 - Fr(1, 16))
control("C4 'c_eff = u/4' at u=1, eps=1/4", ceff != Fr(1, 4), f"c_eff={ceff}")

# ---------- G5: OS-chain arithmetic ----------
ok5 = True
for alpha in (Fr(1, 10), Fr(1, 2), Fr(9, 10)):
    b, p, r, qX = Fr(1), 2 + alpha, Fr(1), Fr(4)
    pX, rX, bX = p + 4, r + 6, b + Fr(5, 2) * r + 8
    s_ext = max(ceil_fr(rX + pX + 7), qX + 6)
    beta_ext = bX + 7 * rX + 1
    s_br = max(ceil_fr(p + r + 17), qX + 6)
    beta_br = b + Fr(19, 2) * r + 51
    if not (pX == 6 + alpha and rX == 7 and bX == Fr(23, 2) and s_ext == 21 and s_br == 21
            and beta_ext == Fr(123, 2) and beta_br == Fr(123, 2)):
        ok5 = False
gate("G5 p_X=6+alpha, r_X=7, b_X=23/2, s=21, beta=123/2 (both routes)", ok5)
def g5_pred(b, r, alpha, qX=Fr(4)):
    p = 2 + alpha
    pX, rX, bX = p + 4, r + 6, b + Fr(5, 2) * r + 8
    return (max(ceil_fr(rX + pX + 7), qX + 6) == 21 and bX + 7 * rX + 1 == Fr(123, 2)
            and max(ceil_fr(p + r + 17), qX + 6) == 21 and b + Fr(19, 2) * r + 51 == Fr(123, 2))
s_c = max(ceil_fr(2 + Fr(1, 2) + 1 + 17), 10); b_c = 1 + Fr(19, 2) + 51
control("C5 (pre-registered, weak) claims s=20 and beta=61 rejected", (s_c != 20) and (b_c != 61), f"computed s={s_c}, beta={b_c}")
c5b = not g5_pred(Fr(0), Fr(0), Fr(1, 2))
print(f"C5b (informational, not pre-registered): G5 predicate with wrong (b,r)=(0,0) {'FAILS as it should' if c5b else 'PASSES (bad)'}")

# ---------- G6: Lemma SC (ii) on 2D tents ----------
lam = Fr(1, 2); zeta = Fr(3, 2)
tents = [((Fr(0), Fr(0)), Fr(1, 2)), ((Fr(2), Fr(0)), Fr(1, 2)), ((Fr(0), Fr(2)), Fr(3, 4))]
def box(c, w):
    return (c[0] - w, c[0] + w, c[1] - w, c[1] + w)
def box_dist2(b1, b2):
    gx = max(Fr(0), b2[0] - b1[1], b1[0] - b2[1]); gy = max(Fr(0), b2[2] - b1[3], b1[2] - b2[3])
    return gx * gx + gy * gy
for i in range(3):
    assert tents[i][1] >= lam
    for j in range(i + 1, 3):
        assert box_dist2(box(*tents[i]), box(*tents[j])) >= lam * lam
def f(i, x):
    (c, w) = tents[i]
    m = max(abs(x[0] - c[0]), abs(x[1] - c[1]))
    return max(Fr(0), 1 - m / w)
def zsample():
    while True:
        a, b, cden = rng.randint(-8, 8), rng.randint(-8, 8), rng.randint(1, 9)
        if a * a + b * b <= cden * cden:
            return C(zeta * Fr(a, cden), zeta * Fr(b, cden))
zsets = [[C(zeta), C(-zeta), C(0, zeta)]] + [[zsample() for _ in range(3)] for _ in range(9)]
def eta(z, x):
    return sum((z[i] * f(i, x) for i in range(3)), C(0))
def rpt(inside):
    if inside:
        i = rng.randint(0, 2); (c, w) = tents[i]
        return (c[0] + Fr(rng.randint(-16, 16), 16) * w, c[1] + Fr(rng.randint(-16, 16), 16) * w)
    return (Fr(rng.randint(-64, 192), 64), Fr(rng.randint(-64, 192), 64))
ok6 = True; c6 = False; npairs = 0
for z in zsets:
    pairs = [((Fr(0), Fr(0)), (Fr(2), Fr(0)))] + [(rpt(k % 2 == 0), rpt(k % 3 == 0)) for k in range(199)]
    for (x, y) in pairs:
        dx2 = (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
        lhs = (eta(z, x) - eta(z, y)).abs2()
        mn = min(Fr(1), dx2 / (lam * lam))
        if not (lhs <= 4 * zeta * zeta * mn):
            ok6 = False
        if lhs > zeta * zeta * mn:
            c6 = True
        npairs += 1
gate(f"G6 |eta(x)-eta(y)|^2 <= 4 zeta^2 min(1,|x-y|^2/lam^2) on {npairs} pairs", ok6)
control("C6 bound without the factor 2 fails somewhere", c6)

# ---------- verdict ----------
gates_ok = all(ok for (kind, _, ok) in results if kind == "gate")
controls_ok = all(ok for (kind, _, ok) in results if kind == "control")
print(f"gates: {sum(1 for r in results if r[0]=='gate' and r[2])}/{sum(1 for r in results if r[0]=='gate')} pass; "
      f"controls: {sum(1 for r in results if r[0]=='control' and r[2])}/{sum(1 for r in results if r[0]=='control')} fired")
print("VERDICT: PASS" if (gates_ok and controls_ok) else "VERDICT: FAIL")
