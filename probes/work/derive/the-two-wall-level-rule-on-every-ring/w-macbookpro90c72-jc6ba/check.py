#!/usr/bin/env python3
"""J:derive:the-two-wall-level-rule-on-every-ring:a2 - checks for ATTEMPT.md (same directory). Exact (sympy) unless labelled.

Block 87 (open PR #8662): one-axis operator h = (1/2i)(tT - T^dag t) on a ring of L sites, (T psi)(x) = psi(x - 1),
t = diag(t_x), t_x = 1 + delta s_x (-1)^x, s_x = +1 on the first half of the ring, -1 on the second. Level rule: the
multiset of E^2 with the two walls is the wall-free one with two copies of delta^2 and of 1 removed and two copies of 0
and of 1 + delta^2 added. Route: h is bipartite with square blocks, so h^2 = J_even (+) J_odd with equal spectra; for
4 | L both walls sit on odd sites, antipodal on the odd ring of M = L/2 sites, where they are diagonal defects +-eta of
the uniform Jacobi matrix J0 = D - C(S + S^dag); the transfer-matrix trace of that ring factorises for every M.
"""
import random
from collections import Counter

import mpmath as mp
import numpy as np
import sympy as sp

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


lam, z, eps = sp.symbols("lambda z epsilon")
E11 = sp.Matrix([[1, 0], [0, 0]])
B = sp.Matrix([[2 * z, -1], [1, 0]])


def U(k):
    return sp.Integer(0) if k == -1 else sp.chebyshevu(k, z)


def bonds(L, ts, tw, flip=None, walls=True):
    """t_x = t_s where s_x (-1)^x = +1 and t_w otherwise; s_x = +1 for x < flip (default L/2), -1 from flip on."""
    flip = L // 2 if flip is None else flip
    return [ts if ((1 if (x < flip or not walls) else -1) * (-1) ** x) == 1 else tw for x in range(L)]


def J_block(t, parity):
    """sublattice block of h^2: diagonal (t_x^2 + t_(x+1)^2)/4, hop -t_(x+1) t_(x+2)/4 between x and x + 2."""
    L = len(t)
    sites = [x for x in range(L) if x % 2 == parity]
    M = len(sites)
    J = sp.zeros(M, M)
    for i, x in enumerate(sites):
        J[i, i] = (t[x] ** 2 + t[(x + 1) % L] ** 2) / 4
        j = (i + 1) % M
        J[i, j] += -t[(x + 1) % L] * t[(x + 2) % L] / 4
        J[j, i] += -t[(x + 1) % L] * t[(x + 2) % L] / 4
    return J


def h_full(t):
    L = len(t)
    H = sp.zeros(L, L)
    for x in range(L):
        H[x, (x - 1) % L] += t[x] / (2 * sp.I)
        H[(x - 1) % L, x] += -t[x] / (2 * sp.I)
    return H


def h87(t):
    """block 87's own axis_operator: (t T - T^T t)/(2i) with T[x, x+1] = 1 (bond x-x+1 carries t_x); h87(t) = -tau h(t) tau^-1."""
    L = len(t)
    Tm = sp.zeros(L, L)
    for x in range(L):
        Tm[x, (x + 1) % L] = 1
    tt = sp.diag(*t)
    return (tt * Tm - Tm.T * tt) / (2 * sp.I)


def cp(J):
    return J.charpoly(lam).as_expr()


def ring_J(M, diag_def, Dv, Cv):
    J = sp.zeros(M, M)
    for i in range(M):
        J[i, i] = Dv + diag_def.get(i, 0)
        J[i, (i + 1) % M] += -Cv
        J[(i + 1) % M, i] += -Cv
    return J


# ------------------------------------------------------------------ A1: sublattice reduction and the rule on rings
red_ok, rule_ok = True, True
for ts, tw, Lmax in ((sp.Rational(13, 10), sp.Rational(7, 10), 40), (sp.Rational(7, 4), sp.Rational(2, 5), 24)):
    D, C, eta = (ts ** 2 + tw ** 2) / 4, ts * tw / 4, (ts ** 2 - tw ** 2) / 4
    for L in range(4, Lmax + 1, 4):
        tW, t0 = bonds(L, ts, tw), bonds(L, ts, tw, walls=False)
        Jo, Je, J0 = J_block(tW, 1), J_block(tW, 0), J_block(t0, 1)
        M = L // 2
        V = sp.zeros(M, M)
        V[(L - 1) // 2, (L - 1) // 2], V[(L // 2 - 1) // 2, (L // 2 - 1) // 2] = eta, -eta
        red_ok &= (Jo - J0 - V) == sp.zeros(M, M) and (L // 2 - 1) % 2 == 1 and (L - 1) // 2 - (L // 2 - 1) // 2 == M // 2
        pw, p0 = cp(Jo), cp(J0)
        red_ok &= sp.expand(cp(Je) - pw) == 0
        if L <= 16 and ts == sp.Rational(13, 10):
            red_ok &= sp.expand(cp(h_full(tW) ** 2) - pw ** 2) == 0 and sp.expand(cp(h87(tW) ** 2) - pw ** 2) == 0
            red_ok &= sp.expand(cp(h87(t0) ** 2) - p0 ** 2) == 0
        rule_ok &= sp.expand(pw * (lam - (ts - tw) ** 2 / 4) * (lam - (ts + tw) ** 2 / 4)
                             - p0 * lam * (lam - (ts ** 2 + tw ** 2) / 2)) == 0
ok("A1", red_ok and rule_ok,
   "exact on every ring L = 4, 8, ..., 40 (t = 1 +- 3/10) and L = 4, ..., 24 (t_s, t_w = 7/4, 2/5): h^2 = J_even (+) "
   "J_odd with equal characteristic polynomials (full h, and block 87's own matrix, to L = 16); both walls on odd sites L-1, L/2-1, antipodal on the "
   "odd ring of M = L/2 sites, J_odd = J0 + eta(P_(L-1) - P_(L/2-1)), eta = (t_s^2 - t_w^2)/4; det(lam - J_walls)"
   "(lam - (t_s-t_w)^2/4)(lam - (t_s+t_w)^2/4) = det(lam - J0) lam (lam - (t_s^2+t_w^2)/2): the level rule")

# ------------------------------------------------------------------ A2: the proof's identities, for every M
pw_ok = all((B ** k).applyfunc(sp.expand) == sp.Matrix([[U(k), -U(k - 1)], [U(k - 1), -U(k - 2)]]).applyfunc(sp.expand)
            for k in range(2, 41)) and all(sp.expand((B ** k).trace() - 2 * sp.chebyshevt(k, z)) == 0 for k in range(1, 41))
tr_ok = True
for M in range(3, 25):
    for r in range(1, M):
        lhs = (B ** (r - 1) * (B + eps * E11) * B ** (M - r - 1) * (B - eps * E11)).trace() - 2
        tr_ok &= sp.expand(lhs - 2 * (sp.chebyshevt(M, z) - 1) + eps ** 2 * U(r - 1) * U(M - r - 1)) == 0
pell_ok = all(sp.expand(sp.chebyshevt(2 * n, z) - 1 - 2 * (z ** 2 - 1) * U(n - 1) ** 2) == 0 for n in range(1, 21))
ts_, tw_ = sp.symbols("t_s t_w", positive=True)
Ds, Cs, es = (ts_ ** 2 + tw_ ** 2) / 4, ts_ * tw_ / 4, (ts_ ** 2 - tw_ ** 2) / 4
zs = (Ds - lam) / (2 * Cs)
lev_ok = (sp.expand(Ds ** 2 - 4 * Cs ** 2 - es ** 2) == 0
          and sp.cancel((4 * (zs ** 2 - 1) - (es / Cs) ** 2) / (lam * (2 * lam - ts_ ** 2 - tw_ ** 2))).free_symbols <= {ts_, tw_}
          and sp.simplify(Ds - 2 * Cs - (ts_ - tw_) ** 2 / 4) == 0 and sp.simplify(Ds + 2 * Cs - (ts_ + tw_) ** 2 / 4) == 0)
mp.mp.dps = 40
wa_ok = True
for n in range(1, 17):
    for zv in (mp.mpf("1.7"), mp.mpf("-0.35"), mp.mpf("0.9")):
        Se = mp.fsum([1 / (zv - mp.cos(2 * mp.pi * j / n)) for j in range(n)])
        So = mp.fsum([1 / (zv - mp.cos((2 * j + 1) * mp.pi / n)) for j in range(n)])
        wa_ok &= abs(Se * So - n ** 2 / (zv ** 2 - 1)) < mp.mpf(10) ** -25 * (1 + abs(Se * So))
ok("A2", pw_ok and tr_ok and pell_ok and lev_ok and wa_ok,
   "identities behind the proof: B = [[2z,-1],[1,0]] has B^k = [[U_k,-U_(k-1)],[U_(k-1),-U_(k-2)]], tr B^k = 2T_k (k to "
   "40); tr(B^(r-1)(B + eps E11)B^(M-r-1)(B - eps E11)) - 2 = 2(T_M - 1) - eps^2 U_(r-1)U_(M-r-1) (symbolic, every "
   "M = 3..24, every r); T_2n - 1 = 2(z^2 - 1)U_(n-1)^2 (n to 20); D^2 - 4C^2 = eta^2, so 4(z^2-1) = (eta/C)^2 is "
   "lam(lam - (t_s^2+t_w^2)/2) = 0, and z = +-1 is lam = (t_s -+ t_w)^2/4 (symbolic); Weinstein-Aronszajn cross-check: "
   "S_per S_anti = n^2/(z^2 - 1) (poles of one sum cancelled by zeros of the other; 40 digits, n to 16)")

# ------------------------------------------------------------------ A3: part (b), any separation, 2n walls, zero modes
d3 = sp.Rational(3, 10)
Dv, Cv = (1 + d3 ** 2) / 2, (1 - d3 ** 2) / 4
zl = (Dv - lam) / (2 * Cv)
sep_ok, surv_ok, zero_ok = True, True, True
for M in (6, 8, 9, 12):
    base = cp(ring_J(M, {}, Dv, Cv))
    for r in range(1, M):
        pw = cp(ring_J(M, {0: d3, r: -d3}, Dv, Cv))
        chi = (sp.chebyshevt(M, zl) - 1) - d3 ** 2 / (2 * Cv ** 2) * U(r - 1).subs(z, zl) * U(M - r - 1).subs(z, zl)
        sep_ok &= sp.expand(pw * (sp.chebyshevt(M, zl) - 1) - base * chi) == 0
        kept = 2 * sum(1 for j in range(1, (M - 1) // 2 + 1) if (2 * r * j) % M == 0)
        surv_ok &= sp.degree(sp.gcd(sp.Poly(pw, lam), sp.Poly(base, lam))) == kept
        zero_ok &= (pw.subs(lam, 0) == 0) == (2 * r == M)
four_ok = True
for M, sites in ((12, (0, 2, 5, 9)), (16, (0, 4, 8, 12)), (10, (0, 1, 3, 7))):
    dd = {s: (-1) ** k * d3 for k, s in enumerate(sites)}
    P = sp.eye(2)
    for k, s in enumerate(sites):
        P = P * (B + (dd[s] / Cv) * E11) * B ** ((sites[(k + 1) % 4] - s - 1) % M)
    four_ok &= sp.expand(cp(ring_J(M, dd, Dv, Cv)) * (sp.chebyshevt(M, zl) - 1)
                         - cp(ring_J(M, {}, Dv, Cv)) * (P.trace() - 2).subs(z, zl) / 2) == 0
rng = random.Random(8763)
gen_ok, crit_ok, ntest, nzero = True, True, 0, 0
s3, w3 = sp.Rational(13, 10), sp.Rational(7, 10)
for L in (6, 8, 10, 12, 14, 16):
    for _ in range(6):
        t = [rng.choice((s3, w3)) for _ in range(L)]
        J = J_block(t, 1)
        M = L // 2
        Delta = sp.eye(2)
        for i in range(M):
            b, bm = J[i, (i + 1) % M], J[(i - 1) % M, i]
            Delta = sp.Matrix([[(lam - J[i, i]) / b, -bm / b], [1, 0]]) * Delta
        pJ = cp(J)
        gen_ok &= sp.expand(pJ - sp.prod([J[i, (i + 1) % M] for i in range(M)]) * (Delta.trace() - 2)) == 0
        H = h_full(t)
        A = H.extract(list(range(0, L, 2)), list(range(1, L, 2)))
        pe, po = sp.prod(t[0::2]), sp.prod(t[1::2])
        crit_ok &= sp.expand(A.det() - (-1) ** M * (po - pe) / (2 * sp.I) ** M) == 0
        crit_ok &= (pJ.subs(lam, 0) == 0) == (pe == po)
        if pe == po:
            nzero += 1
            crit_ok &= sp.diff(pJ, lam).subs(lam, 0) != 0
        ntest += 1
Mf, df = 32, 0.3
Df, Cf = (1 + df ** 2) / 2, (1 - df ** 2) / 4


def sea_sum(defs):
    J = np.zeros((Mf, Mf))
    for i in range(Mf):
        J[i, i] = Df + defs.get(i, 0)
        J[i, (i + 1) % Mf] -= Cf
        J[(i + 1) % Mf, i] -= Cf
    return np.sqrt(np.clip(np.linalg.eigvalsh(J), 0, None)).sum()


rule_e = (1 + df) - np.sqrt(1 + df ** 2)
dev = [sea_sum({}) - sea_sum({0: df, r: -df}) - rule_e for r in range(1, Mf // 2 + 1)]
ratios = [dev[i + 1] / dev[i] for i in range(1, 8)]
att_ok = all(v < 0 for v in dev[:-1]) and all(dev[i] < dev[i + 1] for i in range(len(dev) - 2)) and abs(dev[-1]) < 1e-6
ok("A3", sep_ok and surv_ok and zero_ok and four_ok and gen_ok and crit_ok and nzero > 0 and att_ok,
   "part (b), exact: walls 2r sites apart on one sublattice (odd ring of M = 6, 8, 9, 12, every r): det(lam - J) = "
   "det(lam - J0) [(T_M - 1) - (eta^2/2C^2)U_(r-1)U_(M-r-1)]/(T_M - 1); both band edges always move, a degenerate level "
   "cos(2 pi j/M) keeps both copies iff M | 2rj and loses both otherwise (degree of the common factor), lam = 0 is a "
   "level iff r = M/2; four walls: tr prod_k (B + (d_k/C)E11) B^(m_k) - 2 (M = 10, 12, 16); any bonds "
   f"({ntest} random rings L = 6..16, walls anywhere): det(lam - J_odd) = (prod b_i)(tr prod T_i - 2), det A = (-1)^M "
   f"(prod t_odd - prod t_even)/(2i)^M, zero modes (exactly two) iff prod t_even = prod t_odd ({nzero} such rings); "
   f"float, M = 32, delta = 0.3: the sea's wall-pair energy is (1 + delta) - sqrt(1 + delta^2) only at r = M/2, closer "
   f"pairs cost less ({dev[0]:+.4f} at r = 1, the deficit shrinking by {min(ratios):.2f}-{max(ratios):.2f} per step)")

# ------------------------------------------------------------------ A4: part (c), t = e^(+-delta)
dd_ = sp.Symbol("d", positive=True)
te, tm = sp.exp(dd_), sp.exp(-dd_)
log_ok = all(sp.simplify((a - b).rewrite(sp.exp)) == 0 for a, b in (
    ((te - tm) ** 2 / 4, sp.sinh(dd_) ** 2), ((te + tm) ** 2 / 4, sp.cosh(dd_) ** 2), ((te ** 2 + tm ** 2) / 2, sp.cosh(2 * dd_)),
    (te * tm / 4, sp.Rational(1, 4)), ((te ** 2 - tm ** 2) / 4, sp.sinh(2 * dd_) / 2)))


def e2_float(t):
    L = len(t)
    H = np.zeros((L, L), complex)
    for x in range(L):
        H[x, (x - 1) % L] += t[x] / 2j
        H[(x - 1) % L, x] += -t[x] / 2j
    return list(np.linalg.eigvalsh(H) ** 2)


num_ok, dv = True, 0.37
for L in (8, 12, 16, 20, 24):
    x = np.arange(L)
    s = np.where(x < L // 2, 1, -1)
    lhs = sorted(e2_float(np.exp(dv * s * (-1.0) ** x)) + [np.sinh(dv) ** 2] * 2 + [np.cosh(dv) ** 2] * 2)
    rhs = sorted(e2_float(np.exp(dv * (-1.0) ** x)) + [0.0] * 2 + [np.cosh(2 * dv)] * 2)
    num_ok &= max(abs(a - b) for a, b in zip(lhs, rhs)) < 1e-10
ok("A4", log_ok and num_ok,
   "part (c): t_s, t_w = e^delta, e^-delta give (t_s -+ t_w)^2/4 = sinh^2, cosh^2 delta, (t_s^2 + t_w^2)/2 = cosh 2 delta, "
   "C = 1/4, eta = sinh(2 delta)/2 (symbolic), so levels +-sinh delta, +-cosh delta -> 0, 0, +-sqrt(cosh 2 delta); rings "
   "L = 8..24 at delta = 0.37 agree to 1e-10 (float)")

# ------------------------------------------------------------------ A5: rings with L = 2 mod 4
two_ok, detail = True, ""
for L in (6, 10, 14, 18, 22):
    tW, t0 = bonds(L, s3, w3), bonds(L, s3, w3, walls=False)
    walls = [x for x in range(L) if tW[x] == tW[(x + 1) % L]]
    pw, p0 = cp(J_block(tW, 1)), cp(J_block(t0, 1))
    two_ok &= (p0.subs(lam, 1) != 0 and len(walls) == 2 and all(tW[x] == s3 for x in walls)
               and walls[1] - walls[0] == L // 2 and tW[L // 2:] == tW[:L // 2]
               and pw.subs(lam, 0) == 0 and sp.degree(sp.gcd(sp.Poly(pw, lam), sp.Poly(p0, lam))) == 0)
    if L <= 14:
        two_ok &= sp.expand(cp(h87(tW) ** 2) - pw ** 2) == 0 and sp.expand(cp(h87(t0) ** 2) - p0 ** 2) == 0
    if L == 6:
        r0 = Counter({k: 2 * v for k, v in sp.roots(sp.Poly(p0, lam)).items()})
        rw = Counter({k: 2 * v for k, v in sp.roots(sp.Poly(pw, lam)).items()})
        detail = f"L = 6 loses {dict(r0 - rw)} and gains {dict(rw - r0)}"
ok("A5", two_ok,
   "L = 6, 10, 14, 18, 22 (L = 2 mod 4), exact: the wall-free ring has no level 1 (k = pi is not on the odd sublattice "
   "ring), block 87's s_x gives two strong-strong walls L/2 apart (the bonds have period L/2), zero modes exist "
   f"(prod t_even = prod t_odd) and no squared level of the wall-free ring survives (block 87's matrix to L = 14); {detail}")

print(f"SUMMARY: {'PROVED' if not FAILS else 'PARTIAL (failed: ' + ', '.join(FAILS) + ')'} on every ring whose length "
      "is a multiple of 4 (on L = 2 mod 4 the rule cannot hold: no level 1, block 87's walls are both strong-strong, "
      "every level moves): h^2 = J_even (+) J_odd, isospectral; the walls are defects +-eta at antipodal sites of J_odd; "
      "tr(B^(n-1)(B + eps E11)B^(n-1)(B - eps E11)) - 2 = U_(n-1)^2 (4(z^2 - 1) - eps^2), so only the band edges "
      "z = +-1 move, to lam = 0 and 2D; walls r apart, 2n walls and t = e^(+-delta) follow from the same trace")
if not FAILS:
    print("HIT: on every ring with 4 | L, block 87's one-axis operator with bonds t_s, t_w and two antipodal walls "
          "(strong-strong, weak-weak) has the wall-free squared spectrum with (t_s - t_w)^2/4 and (t_s + t_w)^2/4 "
          "(twice each) replaced by 0 and (t_s^2 + t_w^2)/2 (twice each): delta^2, 1 -> 0, 1 + delta^2 for t = 1 +- delta "
          "and sinh^2, cosh^2 -> 0, cosh 2 delta for t = e^(+-delta); walls r apart on one sublattice give (T_M - 1) - "
          "(eta^2/2C^2) U_(r-1) U_(M-r-1), keeping a degenerate level exactly when M | 2rj; exact zero modes iff the "
          "strong bonds are equally many on the two sublattices (two walls: antipodal)")
