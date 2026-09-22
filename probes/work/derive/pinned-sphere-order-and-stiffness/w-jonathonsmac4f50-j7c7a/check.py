"""pinned-sphere-order-and-stiffness, attempt a4 (w-jonathonsmac4f50-j7c7a).

Law with vacancies (block 39): a site is empty or holds a record of content s; bond kernel B(empty, .) = 1, B(s, s') = c exp(beta s.s');
a record weighs z.  Pinned scale c0 = beta/sinh beta (sphere, uniform probability on S^2) or 1/cosh beta (two-valued, s = +-1).
Records' field sigma_x = n_x s_x; sigma^(k) = N^-1/2 sum_x e^{ik.x} sigma_x; E(k) = sum_i 2(1 - cos k_i).
Exact: Fractions, sympy.  The sphere witness is certified with rational interval bounds (no floating point in the decision).
"""
import itertools
import math
from fractions import Fraction as F

import mpmath as mp
import sympy as sp
from sympy.physics.wigner import wigner_3j

RESULTS = []


def want(label, ok, detail=""):
    RESULTS.append((label, bool(ok)))
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + str(detail)) if detail != "" else ""), flush=True)


def psd_minors(M):
    n = M.shape[0]
    return all(M.extract(list(S), list(S)).det() >= 0 for k in range(1, n + 1) for S in itertools.combinations(range(n), k))


# ================================================================== (a) reflection positivity exactly on the floor
ok = True
for q in (3, 20):
    c0 = sp.Rational(2 * q, q * q + 1)                                     # 1/cosh beta, e^beta = q
    for c, expect in ((c0, True), (c0 - sp.Rational(1, 1000), False), (c0 + sp.Rational(1, 1000), True)):
        Bm = sp.Matrix([[1, 1, 1], [1, c * q, c / q], [1, c / q, c * q]])
        ok = ok and psd_minors(Bm) == expect
    ok = ok and sp.Matrix([[1, 1, 1], [1, c0 * q, c0 / q], [1, c0 / q, c0 * q]]).det() == 0
b = sp.Symbol("beta", positive=True); t = sp.Symbol("t", real=True)
ilist = [sp.sinh(b) / b, sp.cosh(b) / b - sp.sinh(b) / b ** 2]
for l in range(1, 5):
    ilist.append(sp.simplify(ilist[l - 1] - (2 * l + 1) / b * ilist[l]))
fh_ok = True
for l in range(5):
    integral = sp.integrate(sp.exp(b * t) * sp.legendre(l, t), (t, -1, 1)) / 2
    fh_ok = fh_ok and sp.simplify((integral - ilist[l]).rewrite(sp.exp)) == 0
    ser = sum((b ** l) * (b ** 2 / 2) ** k / (sp.factorial(k) * sp.factorial2(2 * l + 2 * k + 1)) for k in range(12))
    fh_ok = fh_ok and sp.simplify(sp.series(ilist[l] - ser, b, 0, 2 * 12 + l).removeO()) == 0
want("A1 (a) EXACT: the one-site kernel [[1,1],[1, c exp(beta s.s')]] is positive semidefinite exactly when c >= c0: two-valued - "
     "all principal minors at e^beta = 3, 20 for c = c0 (singular), c0 +- 1/1000; sphere - the Funk-Hecke eigenvalues of exp(beta s.s') "
     "are i_l(beta) = (1/2) int e^{beta t} P_l(t) dt (checked l <= 4 against the recurrence i_{l+1} = i_{l-1} - (2l+1) i_l/beta and "
     "against the positive series beta^l sum (beta^2/2)^k/(k!(2l+2k+1)!!)), all positive, so the Schur complement c exp(beta s.s') - 1 "
     "is PSD iff c i_0 = c sinh(beta)/beta >= 1 (block 39 T5 re-derived)", ok and fh_ok)

# ================================================================== (b) no rotation-symmetric embedding dominates at c0
# embedding: record s -> (s, 0), empty -> (0, h); B = f f' exp(-(beta'/2)|sigma - sigma'|^2) R; R PSD needed for the twist argument.
# Schur on the empty entry: R PSD iff c e^{beta'} exp((beta - beta') s.s') - e^{beta'(1 + h^2)} is a PSD kernel iff c >= e^{beta' h^2} c0(beta - beta').
ok = True
for (q, qp, h2) in ((3, sp.Rational(3, 2), 0), (3, sp.Rational(3, 2), 1), (20, 2, 0), (20, sp.Rational(5, 4), sp.Rational(1, 2))):
    # two-valued: e^beta = q, e^beta' = qp; the remainder's coupling gamma = beta - beta' has e^gamma = q/qp
    c0 = sp.Rational(2 * q, q * q + 1)
    g = sp.Rational(q) / qp
    # R(s, s') = c e^{beta'} e^{gamma s s'} (f = 1), R(empty, s) = e^{(beta'/2)(1 + h^2)}, R(empty, empty) = 1
    # PSD <=> c e^{beta'} e^{gamma ss'} - e^{beta'(1+h^2)} PSD (2x2) <=> c e^{beta'} cosh(gamma) >= e^{beta'(1+h^2)}
    lhs = c0 * qp * (g + 1 / g) / 2
    rhs_sq = qp ** (2 * (1 + h2))                                       # compare squares to stay rational: rhs = qp^(1+h2)
    ok = ok and (lhs ** 2 < rhs_sq)                                     # fails at c0 for beta' > 0
    # and the floor it would need: c >= e^{beta' h^2} / cosh(gamma) > c0
    ok = ok and (qp ** (2 * h2)) * (2 / (g + 1 / g)) ** 2 > c0 ** 2
want("B1 (b) NO-GO FOR THE EMBEDDING FAMILY: embed a record as (s, 0) and the empty state as (0, h) in R^{3+m} (rotation-symmetric; h = 0 "
     "is the twist of blocks 19/36 and of #8616), split B = f f' exp(-(beta'/2)|sigma - sigma'|^2) R; the Schur complement on the empty "
     "entry makes R positive semidefinite iff c >= e^{beta' h^2} c0(beta - beta') [proof in ATTEMPT.md]; since c0 decreases strictly, at "
     "c = c0(beta) only beta' = 0 is allowed - no twist strength survives; checked exactly for the two-valued menu at four (e^beta, "
     "e^beta', h^2)", ok)

# ================================================================== (b) the full-beta infrared bound is FALSE at c0: two-valued, 4-ring
def ring_two(q, z, n=4):
    c = F(2 * q, q * q + 1)
    Z = F(0); num = F(0); occ = F(0)
    for cfg in itertools.product((None, 1, -1), repeat=n):
        w = F(1)
        for x in range(n):
            if cfg[x] is not None: w *= z
            a, bb = cfg[x], cfg[(x + 1) % n]
            if a is not None and bb is not None: w *= c * (q if a == bb else F(1, q))
        Z += w
        sig = [0 if s is None else s for s in cfg]
        m = sum((-1) ** x * sig[x] for x in range(n))
        num += w * m * m
        occ += w * sum(1 for s in cfg if s is not None)
    return num / (n * Z), occ / (n * Z)


def log_lower(q):
    """rational lower bound for log q = 2 atanh((q-1)/(q+1)) from partial sums (all terms positive)."""
    u = F(q - 1, q + 1)
    return 2 * sum(u ** (2 * k + 1) / (2 * k + 1) for k in range(200))


S2, rho2 = ring_two(20, F(1, 2))
LB = 4 * log_lower(20) * S2                                             # E(pi) = 4 on the ring
want("B2 (b) EXACT WITNESS, two-valued: 4-ring (an even 1D torus, where the twist argument would give S(k) <= 1/(beta E(k))), e^beta = 20, "
     "c = c0 = 40/401, z = 1/2, k = pi: S(pi) = <|sigma^(pi)|^2> is the exact rational below, and 4 log(20) S(pi) > 1 with a rational lower "
     "bound on log 20: the full-beta infrared bound fails at the pinned scale", LB > 1,
     f"S(pi) = {S2} = {float(S2):.6f}, rho = {float(rho2):.4f}, 4 beta S(pi) > {float(LB):.4f}")

# ================================================================== (b) the sphere menu: a rigorous certificate on the 4-ring
BETA = 8; Z1 = F(1); LC = 30
K = 160
x16 = F(16)
S_K = sum(x16 ** k / math.factorial(k) for k in range(K + 1))
e16_lo = S_K
e16_hi = S_K + x16 ** (K + 1) / math.factorial(K + 1) * F(K + 2, K + 2 - 16)
coth_lo = (e16_hi + 1) / (e16_hi - 1)                                  # coth 8 = (e^16 + 1)/(e^16 - 1), decreasing in e^16
coth_hi = (e16_lo + 1) / (e16_lo - 1)
aa = [F(1, BETA), F(-1, BETA ** 2)]; bb = [F(0), F(1, BETA)]           # i_l(8) = a_l sinh 8 + b_l cosh 8
for l in range(1, LC + 2):
    aa.append(aa[l - 1] - F(2 * l + 1, BETA) * aa[l])
    bb.append(bb[l - 1] - F(2 * l + 1, BETA) * bb[l])
r_lo, r_hi = [], []
for l in range(LC + 2):
    v1 = BETA * aa[l] + BETA * bb[l] * coth_lo; v2 = BETA * aa[l] + BETA * bb[l] * coth_hi
    lo, hi = min(v1, v2), max(v1, v2)
    r_lo.append(max(lo, F(0))); r_hi.append(min(hi, F(1)))
# tail l > LC+1: r_l <= (8^l/(2l+1)!!) e^{64/(4l+6)} (8/sinh 8) <= (8^l/(2l+1)!!) (5/3)(16/2979)
def dfact(n):
    out = 1
    for k in range(n, 0, -2): out *= k
    return out
e8_lo = sum(F(8) ** k / math.factorial(k) for k in range(60))
e_hi = sum(F(1, math.factorial(k)) for k in range(30)) + F(1, math.factorial(29))
tail_ok = e8_lo > 2980 and e_hi < F(25, 9)             # 8/sinh 8 < 16/2979 and e^{1/2} < 5/3
Tl = lambda l: F(8 ** l, dfact(2 * l + 1)) * F(5, 3) * F(16, 2979)
L0 = LC + 1                                                             # exact sums cover l <= LC; tail from l = LC + 1
tail_term = (2 * L0 + 2) * Tl(L0) ** 4
tail = tail_term * 2                                                    # ratio of successive terms < 1/2 (checked below)
ratio_ok = all((2 * l + 4) * Tl(l + 1) ** 4 <= (2 * l + 2) * Tl(l) ** 4 / 2 for l in range(L0, L0 + 50))
LF_lo = sum((2 * l + 1) * r_lo[l] ** 4 for l in range(LC + 1))
LF_hi = sum((2 * l + 1) * r_hi[l] ** 4 for l in range(LC + 1)) + tail                     # l >= LC+1: (2l+1) r^4 <= (2l+2) T^4
A_lo = sum((l + 1) * (r_lo[l] ** 3 * r_lo[l + 1] + r_lo[l] * r_lo[l + 1] ** 3) for l in range(LC + 1))
A_hi = sum((l + 1) * (r_hi[l] ** 3 * r_hi[l + 1] + r_hi[l] * r_hi[l + 1] ** 3) for l in range(LC + 1)) + tail
O_lo = sum(2 * (l + 1) * r_lo[l] ** 2 * r_lo[l + 1] ** 2 for l in range(LC + 1))
# 4-ring at z = 1: numerator of S(pi): rho - 2 C_adj + C_opp with Z = 15 + LF;  3 S(pi) Z = 7 + LF - 6 r1 - 2 A + 2 r1^2 + O
num_lo = 7 + LF_lo - 6 * r_hi[1] - 2 * A_hi + 2 * r_lo[1] ** 2 + O_lo
V_lo = F(4 * BETA, 3) * num_lo / (15 + LF_hi)
cg_ok = all(wigner_3j(l, 1, l + 1, 0, 0, 0) ** 2 * (2 * l + 1) * (2 * l + 3) == l + 1 for l in range(12))
mp.mp.dps = 40
langevin = lambda x: mp.coth(x) - 1 / x
il = lambda l, x: mp.sqrt(mp.pi / (2 * x)) * mp.besseli(l + mp.mpf(1) / 2, x)
bt = mp.mpf(3)
two_site = sum(2 * (l + 1) * il(l, bt) * il(l + 1, bt) for l in range(120)) / sum((2 * l + 1) * il(l, bt) ** 2 for l in range(120))
lang_ok = abs(two_site - langevin(2 * bt)) < mp.mpf(10) ** -30
want("B3 (b) RIGOROUS WITNESS, SPHERE MENU: 4-ring, beta = 8, c = c0 = 8/sinh 8, z = 1, k = pi. Occupancy patterns: trees weigh 1 per bond "
     "at c0; the full ring weighs sum_l (2l+1) r_l^4 and has <s0.s1> = sum (l+1)(r_l^3 r_{l+1} + r_l r_{l+1}^3)/LF, <s0.s2> = sum 2(l+1) "
     "r_l^2 r_{l+1}^2/LF (r_l = i_l/i_0; the Clebsch-Gordan weight (2l+1)(2l+3)(l 1 l+1; 0 0 0)^2 = l+1 checked exactly for l < 12; the "
     "two-site case reproduces the Langevin function L(2 beta) to 30 digits). With r_l = 8a_l + 8b_l coth 8 (exact rationals a_l, b_l, "
     "l <= 31), rational bounds on e^16 and an explicit tail bound, 4 beta S(pi) > the rational lower bound below > 1",
     V_lo > 1 and tail_ok and ratio_ok and cg_ok and lang_ok, f"4 beta S(pi) > {float(V_lo):.6f}")

# ================================================================== (b) the literal reading: twisting record-record bonds only
q = 3; c0 = sp.Rational(2 * q, q * q + 1); Delta = 2
states = [(u, a) for a in (0, Delta) for u in (None, 1, -1)]


def Kcross(s1, s2):
    (u, a), (v, a2) = s1, s2
    if u is None or v is None: return sp.Integer(1)
    d = (u - v) - (a - a2)                                             # record-record twisted Gaussian: c e^beta e^{-(beta/2) d^2}
    return c0 * q * sp.Rational(1, q ** sp.Rational(d * d, 2)) if (d * d) % 2 == 0 else None


Km = sp.Matrix(6, 6, lambda i, j: Kcross(states[i], states[j]))
x_ = sp.Matrix([-1, 1, sp.Rational(1, 2), -1, sp.Rational(1, 2), 1])       # (empty, +1, -1) at shift 0, then at shift 2
form = (x_.T * Km * x_)[0]
psd_single = psd_minors(Km.extract([0, 1, 2], [0, 1, 2]))
# X3 (#8616): record-only twist's linear term is not E(k) sum sigma psi
sig4 = [1, 1, 0, 1]; psi4 = [1, 0, -1, 0]                               # cos(pi x/2) on the 4-ring
rec_lin = sum((psi4[x] - psi4[(x + 1) % 4]) * (sig4[x] - sig4[(x + 1) % 4]) for x in range(4) if sig4[x] != 0 and sig4[(x + 1) % 4] != 0)
emb_lin = 2 * sum(sig4[x] * psi4[x] for x in range(4))                  # E(pi/2) = 2
want("B4 (b) THE LITERAL READING (only record-record bonds twisted): at c0 its crossing kernel on {empty, +1, -1} x {shift 0, shift 2} "
     "(e^beta = 3) is NOT positive semidefinite - the vector (-1, 1, 1/2, -1, 1/2, 1) on (empty, +1, -1) at shift 0 then shift 2 gives the negative form below - although each "
     "single-shift block is (the twist argument needs all shifts); and even a valid domination would bound the record-bond term, which "
     "for sigma = (+1, +1, empty, +1), k = pi/2 on the 4-ring is 0 while E(k) sum sigma psi = 2 (#8616 X3), not the structure factor",
     form < 0 and psd_single and rec_lin == 0 and emb_lin == 2, f"form = {form} = {float(form):.5f}")

# ================================================================== (c) the constants, conditional on a strength beta'
Sk = {}
for kk in range(4):
    kv = 2 * math.pi * kk / 4
    Z = F(0); num = 0
    c = F(2 * 20, 401)
    tot = F(0)
    for cfg in itertools.product((None, 1, -1), repeat=4):
        wgt = F(1)
        for x in range(4):
            if cfg[x] is not None: wgt *= F(1, 2)
            a, bb2 = cfg[x], cfg[(x + 1) % 4]
            if a is not None and bb2 is not None: wgt *= c * (20 if a == bb2 else F(1, 20))
        Z += wgt
        sig = [0 if s is None else s for s in cfg]
        re = sum(sig[x] * [1, 0, -1, 0][(kk * x) % 4] for x in range(4)); im = sum(sig[x] * [0, 1, 0, -1][(kk * x) % 4] for x in range(4))
        tot += wgt * (re * re + im * im)
    Sk[kk] = tot / (4 * Z)
sumrule = sum(Sk.values()) == 4 * rho2
want("C1 (c) THE CONSTANTS: the sum rule sum_e sum_k <|sigma^e(k)|^2> = N rho holds exactly (|sigma_x|^2 = n_x; checked for the two-valued "
     "4-ring at the B2 point, all four k); IF a twist of strength beta' dominated, M^2 = N^-1 sum_e <|sigma^e(0)|^2> >= rho - (D/beta') "
     "N^-1 sum_{k != 0} 1/E(k) -> rho - 3 G(0)/beta' on Z^3 (D = 3 components, G(0) = 0.2527 in this normalisation of E) and long-range "
     "order would follow for beta' rho > 3 G(0) (G(0) <= sqrt3 pi/8, block 19); by B1 the only strength at c0 is beta' = 0, so this "
     "route gives no bound at the pinned scale", sumrule, f"S(k) = {[str(v) for v in Sk.values()]}")

npass = sum(1 for _, o in RESULTS if o)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
if nfail == 0:
    print("SUMMARY: ROUTE FAILS AT (b): (a) holds exactly on the floor (the kernel [[1,1],[1, c e^{beta s.s'}]] is PSD iff c >= c0), but at "
          "c0 no rotation-symmetric embedding of the empty state admits a twist of any strength beta' > 0 (the remainder is PSD iff "
          "c >= e^{beta' h^2} c0(beta - beta')), and the full-beta infrared bound that (b)-(c) would deliver is FALSE at c0 for both menus: "
          "4 beta S(pi) > 2.12 on the 4-ring for the two-valued menu (exact) and > 1.977 for the sphere menu at beta = 8, z = 1 (rigorous "
          "rational bounds); the literal record-bond twist is not reflection-dominated across shifts and would not bound the structure factor; so (c)-(e) "
          "get no constants from this route at the pinned scale")
    print(f"HIT: at the pinned scale c0 = beta/sinh beta the Gaussian-domination route to long-range order fails for the sphere menu with "
          f"vacancies: on the 4-ring at beta = 8, z = 1, k = pi, 4 beta <|sigma^(k)|^2> > {float(V_lo):.4f} > 1 (rigorous: exact rational "
          f"Bessel coefficients, rational bounds on coth 8, explicit tail), and no embedding of the empty state at (0, h) admits a twist "
          f"of strength beta' > 0 (needs c >= e^(beta' h^2) c0(beta - beta') > c0(beta))")
