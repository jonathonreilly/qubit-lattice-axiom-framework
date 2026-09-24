#!/usr/bin/env python3
"""Formation timed by the clock, attempt 2: checks for ATTEMPT.md (worker w-macbookpro9927a-jef4e, claude-opus-5-5).

Block 95 (PR #8860, head f9b34475df) with formation added. Torus T (N_s sites), records with exclusion (W = 1), clock field
log w_z(C) = c lam sum_{r in C} G(z - r) (c = 6 on Z^3 tori, c = 2 on rings; G the zero-mean inverse of the lattice Laplacian),
hops x -> y (empty neighbour) at w_x^a w_y^(1-a) h / (2d), h = 1/2; NEW: an empty site y forms a record at rate z w_y(C)^b; records
are permanent. Block 95's law at fixed count n: pi_n(C) prop exp(c lam (1 - 2a) sum_pairs G).

Exact throughout (fractions, sympy); the rate field is made rational by fixing Q = e^{c lam/D}, D the denominator of G.
"""
from __future__ import annotations

import math
import subprocess
import time
from collections import Counter
from fractions import Fraction as Fr
from itertools import combinations, product

import sympy as sp

OUT: list[str] = []
FAILS: list[str] = []


def check(tag, ok, msg):
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


# ----------------------------------------------------------------------------------------------------------------------
# Green functions

def green_ring(L):
    G = sp.symbols(f"g0:{L}")
    eqs = [sp.Eq(2 * G[d] - G[(d + 1) % L] - G[(d - 1) % L], (1 if d == 0 else 0) - sp.Rational(1, L)) for d in range(L)]
    eqs[-1] = sp.Eq(sum(G), 0)
    sol = sp.solve(eqs, G)
    return [sp.Rational(sol[g]) for g in G]


def green_torus3(L):
    sites = list(product(range(L), repeat=3)); ix = {s: i for i, s in enumerate(sites)}; N = len(sites)
    M = sp.zeros(N, N); rhs = sp.zeros(N, 1)
    for s in sites:
        i = ix[s]; M[i, i] += 6
        for j in range(3):
            for e in (1, -1):
                t = list(s); t[j] = (t[j] + e) % L; M[i, ix[tuple(t)]] -= 1
        rhs[i] = (1 if s == (0, 0, 0) else 0) - sp.Rational(1, N)
    ok = True
    M2 = M.copy(); M2[N - 1, :] = sp.ones(1, N); r2 = rhs.copy(); r2[N - 1] = 0
    g = M2.LUsolve(r2)
    Gd = {s: sp.Rational(g[ix[s]]) for s in sites}
    # the defining identity at every site (including the replaced row)
    for s in sites:
        v = 6 * Gd[s]
        for j in range(3):
            for e in (1, -1):
                t = list(s); t[j] = (t[j] + e) % L; v -= Gd[tuple(t)]
        ok &= v == (1 if s == (0, 0, 0) else 0) - sp.Rational(1, N)
    ok &= sum(Gd.values()) == 0
    return Gd, ok


# ----------------------------------------------------------------------------------------------------------------------
# Family C: at count 2 the total formation rate Lambda depends on the pair's separation for every lam b != 0

def lam2_exponents_ring(G, L, d, D):
    return Counter(int(D * (G[y] + G[(y - d) % L])) for y in range(L) if y not in (0, d))


def lam2_exponents_torus(Gd, L, d, D):
    out = Counter()
    for y in product(range(L), repeat=3):
        if y == (0, 0, 0) or y == d:
            continue
        ymd = tuple((y[i] - d[i]) % L for i in range(3))
        out[int(D * (Gd[y] + Gd[ymd]))] += 1
    return out


def diff_terms(c1, c2):
    keys = sorted(set(c1) | set(c2))
    return [(k, c1.get(k, 0) - c2.get(k, 0)) for k in keys if c1.get(k, 0) != c2.get(k, 0)]


def sign_changes(terms):
    cs = [c for _, c in terms]
    return sum(1 for i in range(len(cs) - 1) if cs[i] * cs[i + 1] < 0)


def ev(terms, q):
    return sum(c * (q ** k if k >= 0 else 1 / q ** (-k)) for k, c in terms)


def family_c():
    t0 = time.time()
    q = sp.symbols("q", positive=True)
    ring_ok, ring_info = True, []
    for L in range(4, 9):
        G = green_ring(L); D = int(sp.ilcm(*[g.q for g in G]))
        seps = list(range(1, L // 2 + 1))
        exs = {d: lam2_exponents_ring(G, L, d, D) for d in seps}
        common = None
        for d in seps[1:]:
            T = diff_terms(exs[seps[0]], exs[d])
            P = sp.Poly(sp.expand(sum(c * q ** (k + 4 * D) for k, c in T)), q)
            roots = {r for r in sp.real_roots(P) if r > 0}
            common = roots if common is None else {r for r in common if P.eval(r) == 0}
        ring_ok &= common == {1}
        ring_info.append(f"{L}")
    tor_ok, tor_info = True, []
    for L, pairs in ((3, [((0, 0, 1), (1, 1, 1)), ((0, 1, 1), (1, 1, 1))]),
                     (4, [((0, 0, 1), (1, 2, 2)), ((0, 1, 2), (1, 2, 2))])):
        Gd, gok = green_torus3(L); D = int(sp.ilcm(*[g.q for g in Gd.values()]))
        tor_ok &= gok
        brackets = []
        for d1, d2 in pairs:
            T = diff_terms(lam2_exponents_torus(Gd, L, d1, D), lam2_exponents_torus(Gd, L, d2, D))
            V = sign_changes(T)
            # derivative in alpha = log q at alpha = 0 (sum k c / D) nonzero: q = 1 is a simple root
            d0 = sum(k * c for k, c in T)
            # locate the one further positive root: scan q = 1 + m/10^6 on a coarse grid of exact rationals
            lo = None
            prev = ev(T, Fr(1000001, 1000000)) > 0
            m = 1
            while m < 10 ** 7:
                cur = ev(T, Fr(1000000 + 2 * m, 1000000)) > 0
                if cur != prev:
                    lo, hi = Fr(1000000 + m, 1000000), Fr(1000000 + 2 * m, 1000000)
                    break
                prev = cur; m *= 2
            # refine by bisection (exact)
            for _ in range(24):
                mid = (lo + hi) / 2
                if (ev(T, mid) > 0) == (ev(T, lo) > 0):
                    lo = mid
                else:
                    hi = mid
            tor_ok &= V == 2 and d0 != 0 and (ev(T, lo) > 0) != (ev(T, hi) > 0) and lo > 1
            brackets.append((lo, hi, V))
        (l1, h1, _), (l2, h2, _) = brackets
        disjoint = h1 < l2 or h2 < l1
        tor_ok &= disjoint
        a1 = [float(D * sp.log(sp.Rational(x))) for x in (l1, h1)]
        a2 = [float(D * sp.log(sp.Rational(x))) for x in (l2, h2)]
        tor_info.append(f"{L}^3: roots at alpha in [{a1[0]:.4f},{a1[1]:.4f}] and [{a2[0]:.4f},{a2[1]:.4f}]")
    check("C1", ring_ok and tor_ok,
          "count 2: the total formation rate Lambda({r,s}) = z sum_(y empty) w_y^b depends on the separation for EVERY lam b "
          f"!= 0: rings L = {','.join(ring_info)} (exact real roots: the only positive q common to all separations is 1); "
          "tori 3^3, 4^3 (G checked at every site): two separation pairs with 2 sign changes each (Laguerre: q = 1 simple, "
          f"exactly one more positive root) whose further roots are separated by exact brackets: {'; '.join(tor_info)} "
          f"({time.time() - t0:.0f} s)")


# ----------------------------------------------------------------------------------------------------------------------
# the ring machinery (exact dynamics)

def ring_setup(L, Q):
    G = green_ring(L); D = int(sp.ilcm(*[g.q for g in G])); Gi = [int(D * g) for g in G]

    def w(x, C):
        return Q ** sum(Gi[(x - r) % L] for r in C)
    return G, D, Gi, w


def pw(v, k):
    return v ** k if k >= 0 else 1 / v ** (-k)


def half_pow(v, num, den):   # v^(num/den) for v a rational power of a perfect square base (a = 1/2 case)
    r = sp.Rational(v) ** sp.Rational(num, den)
    assert r.is_rational
    return Fr(int(r.p), int(r.q))


def rates(C, L, w, a, b):
    C = frozenset(C)
    for x in C:
        for e in (1, -1):
            y = (x + e) % L
            if y in C:
                continue
            if a == Fr(1, 2):
                r = half_pow(w(x, C), 1, 2) * half_pow(w(y, C), 1, 2)
            else:
                r = pw(w(x, C), a) * pw(w(y, C), 1 - a)
            yield (C - {x}) | {y}, r * Fr(1, 4), "hop"
    for y in range(L):
        if y not in C:
            yield C | {y}, pw(w(y, C), b), "form"


def pair_law(L, n, w, a):
    raw = {}
    for C in combinations(range(L), n):
        v = Fr(1)
        for i in range(n):
            for j in range(i + 1, n):
                if a == Fr(1, 2):
                    v *= 1
                else:
                    v *= pw(w(C[i], [C[j]]), 1 - 2 * a)
        raw[frozenset(C)] = v
    Z = sum(raw.values())
    return {k: v / Z for k, v in raw.items()}


def solve(A, bvec):
    n = len(A); M = [row[:] + [bvec[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        inv = 1 / M[c][c]; M[c] = [v * inv for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]; M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [M[r][n] for r in range(n)]


def run(L, Q, a, b, z):
    """exact: for each count n, mean time spent at count n and the law at entry to count n+1"""
    G, D, Gi, w = ring_setup(L, Q)
    nu = {frozenset(): Fr(1)}
    times, laws = [], [nu]
    for n in range(L):
        S = [frozenset(c) for c in combinations(range(L), n)]; ix = {s: i for i, s in enumerate(S)}; m = len(S)
        A = [[Fr(0)] * m for _ in range(m)]; F = {}
        for s in S:
            i = ix[s]
            for t, r, kind in rates(s, L, w, a, b):
                if kind == "hop":
                    A[i][i] += r; A[i][ix[t]] -= r
                else:
                    A[i][i] += z * r; F[(i, t)] = F.get((i, t), 0) + z * r
        x = solve([[A[j][i] for j in range(m)] for i in range(m)], [nu.get(s, Fr(0)) for s in S])
        times.append(sum(x))
        nxt = {}
        for (i, t), r in F.items():
            nxt[t] = nxt.get(t, 0) + x[i] * r
        nu = nxt; laws.append(nu)
    return times, laws, w


def tv(p, q):
    keys = set(p) | set(q)
    return sum(abs(p.get(k, 0) - q.get(k, 0)) for k in keys) / 2


def sep_law(law, L):
    """law of the unordered separation class min(d, L - d) of a two-record configuration"""
    out = Counter()
    for C, v in law.items():
        r, s = sorted(C)
        d = (s - r) % L
        out[min(d, L - d)] += v
    return out


# ----------------------------------------------------------------------------------------------------------------------
# Family B: the characterization at work on the ring of 7 (Q = e^{2 lam/7} = 1/2: records slow clocks)

def family_b():
    L = 7
    Q = Fr(1, 2)
    G, D, Gi, w = ring_setup(L, Q)
    # (1) the creation flux for b = 1 - 2a is prop to pi_n (counts 2, 3), for a = 1, b = 1 it is not
    okflux = True
    for a, b, want in ((1, -1, True), (1, 1, False)):
        for n in (2, 3):
            pin = pair_law(L, n, w, a); pim = pair_law(L, n - 1, w, a)
            ratios = set()
            for C in pin:
                I = sum(pim[C - {x}] * pw(w(x, C - {x}), b) for x in C)
                ratios.add(I / pin[C])
            okflux &= (len(ratios) == 1) == want
    # (2) dynamics, exact entry laws
    z = Fr(1)
    _, lawsA, _ = run(L, Q, 1, -1, z)          # b = 1 - 2a: the reversible creation half (block 39 T4)
    _, lawsB, _ = run(L, Q, 1, 1, z)           # b = 1: block 97's principle read for formation
    pi2 = pair_law(L, 2, w, 1); pi3 = pair_law(L, 3, w, 1)
    tvA2, tvA3 = tv(lawsA[2], pi2), tv(lawsA[3], pi3)
    tvB2 = tv(lawsB[2], pi2)
    sB = sep_law(lawsB[2], L); sP = sep_law(pi2, L)
    wd = [w(d, [0]) for d in range(1, L)]
    okB = all(sB[c] == (wd[c - 1] + wd[L - c - 1]) / sum(wd) for c in range(1, L // 2 + 1))
    okP = all(sP[c] == (pw(wd[c - 1], -1) + pw(wd[L - c - 1], -1)) / sum(pw(v, -1) for v in wd) for c in range(1, L // 2 + 1))
    clsB = [sB[c] for c in range(1, L // 2 + 1)]; clsP = [sP[c] for c in range(1, L // 2 + 1)]
    # (3) the degenerate case a = 1/2, b = 0 keeps the (flat) law at every count (Q = 1/4 keeps w^(1/2) rational)
    Q4 = Fr(1, 4)
    _, lawsC, wC = run(L, Q4, Fr(1, 2), 0, z)
    okC = all(tv(lawsC[n], pair_law(L, n, wC, Fr(1, 2))) == 0 for n in range(1, L + 1))
    check("B1", okflux and tvA2 == 0 and tvA3 > 0 and tvB2 > 0 and okB and okP and okC,
          "ring 7, e^{2 lam/7} = 1/2 (records slow clocks), z = 1, exact: the creation flux sum_x pi_(n-1)(C-x) w_x^b is prop "
          "to block 95's pi_n at counts 2 and 3 for b = 1 - 2a = -1 and not for b = 1; with b = -1 (block 39 T4's creation "
          f"half) the law entering count 2 is pi_2 exactly but entering count 3 it is off by TV {float(tvA3):.4f}; with b = 1 "
          f"(block 97 read for formation) the second record forms at separation d with weight w(d) = 2^(-7G(d)) = "
          f"{', '.join(str(x) for x in wd)} (d = 1..6): classes 1, 2, 3 get {', '.join(str(x) for x in clsB)} against "
          f"pi_2's {', '.join(str(x) for x in clsP)} (weights 1/w): TV {float(tvB2):.4f}; a = 1/2, b = 0 keeps the flat "
          "law at every count (TV 0)")
    return w


# ----------------------------------------------------------------------------------------------------------------------
# Family J: filling and jamming on the ring of 7 (a = b = 1, Q = 1/2)

def family_j():
    L = 7; Q = Fr(1, 2)
    G, D, Gi, w = ring_setup(L, Q)
    zs = [Fr(1, 100), Fr(1, 10), Fr(1), Fr(10), Fr(100)]
    vals, first2 = [], True
    for z in zs:
        times, laws, _ = run(L, Q, 1, 1, z)
        vals.append(z * sum(times))
        first2 &= z * times[0] == Fr(1, 7) and z * times[1] == Fr(1, 13)
    # quasi-static limit: sum_n 1/<Lambda>_(pi_n); no-motion limit: E sum_n 1/Lambda(C_n) over clock-weighted filling
    def Lam(C):
        return sum(w(y, C) for y in range(L) if y not in C)
    qs = sum(1 / sum(p * Lam(C) for C, p in pair_law(L, n, w, 1).items()) for n in range(L))
    memo = {}

    def nm(C):
        if len(C) == L:
            return Fr(0)
        if C in memo:
            return memo[C]
        lam = Lam(C)
        v = 1 / lam + sum(w(y, C) / lam * nm(C | {y}) for y in range(L) if y not in C)
        memo[C] = v
        return v
    nmv = nm(frozenset())
    inc = all(vals[i] < vals[i + 1] for i in range(len(vals) - 1))
    between = qs < vals[0] and vals[-1] < nmv
    check("J1", first2 and inc and between,
          "ring 7, a = b = 1, e^{2 lam/7} = 1/2, exact: z E[time to fill] = "
          + ", ".join(f"{float(v):.5f}" for v in vals) + " at z = 1/100, 1/10, 1, 10, 100 (rational, increasing); limits: "
          f"quasi-static sum_n 1/<Lambda>_pi_n = {float(qs):.5f} < every value < no-motion {float(nmv):.5f}; the first two "
          "stages are z-free (z E[T_1] = 1/7, the next 1/13, since Lambda is constant at counts 0 and 1)")


# ----------------------------------------------------------------------------------------------------------------------
# Family Q: sources

B95 = "f9b34475df1a567d2e1abc2f69b7f259483b728f"
N95 = ("docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH_A_ONE_OVER_R_"
       "POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23.md")
B97 = "f6c81d4a73f6b0547340749e1d1655b2f92a7ef8"
N97 = ("docs/ADMISSIBILITY_RULE_A_RECORD_THAT_CANNOT_READ_THE_FIELD_FROM_ITS_OWN_MOTION_HOPS_ON_ITS_OWN_CLOCK_AND_WITH_KEPT_"
       "BOOKS_RECORDS_ATTRACT_BOUNDED_THEOREM_NOTE_2026-09-23.md")
B39 = "31e5d0300e07357ef4de73c210288fe6615d6f19"
N39 = ("docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE_IS_"
       "A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md")


def family_q():
    def show(h, n):
        return subprocess.run(["git", "show", f"{h}:{n}"], capture_output=True, text=True).stdout
    t95, t97, t39 = show(B95, N95), show(B97, N97), show(B39, N39)
    need = [(t95, "`π(C) ∝ W(C) exp(6 log κ (1 − 2a) Σ_{{r, s} ⊂ C} G(r − s))`"),
            (t95, "`log w_z = 6 log κ Σ_{r∈C} G(z − r)`"),
            (t95, "`w_x^a w_y^(1−a) · h / 6`"),
            (t95, "(one-dimensional law, factor 2 in place of 6)"),
            (t95, "It is held fixed: formation is not included."),
            (t97, "gives `a = 1`"),
            (t39, "so `λ = zZ_x` and no other rate"),
            (t39, "It does not make the growing population a sample of the static ensemble.")]
    bad = [q[:30] for t, q in need if q not in t]
    check("Q", not bad, f"block 95 at {B95[:10]} (T2's pair law, P2's clock law, P3's timing, the ring's factor 2, count held "
          f"fixed), block 97 at {B97[:10]} (a = 1), block 39 at {B39[:10]} (T4: lambda = z Z_x and no other rate; the "
          f"corrigendum: permanence does not give the static ensemble) {bad if bad else ''}")


def main():
    t0 = time.time()
    family_q()
    family_c()
    family_b()
    family_j()
    print("\n".join(OUT))
    print(f"TOTAL: PASS={len(OUT) - len(FAILS)} FAIL={len(FAILS)}  ({time.time() - t0:.0f} s)")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return
    print("SUMMARY: PROVED (b), with exact certificates: with formation at rate z w_y^b at empty sites, records permanent and "
          "block 95's motion (timing a), the law on the occupied set equals block 95's pair law at every count and every "
          "time from the empty lattice iff (i) the creation flux sum_x pi_(n-1)(C-x) w_x(C-x)^b is prop to pi_n (forces "
          "b = 1 - 2a when lam != 0 and G is not constant) and (ii) the total formation rate is the same for all "
          "configurations of each count; (ii) fails at count 2 for every lam b != 0 (first order -2 alpha z (G(0) + G(d)); all "
          "orders on rings 4-8 and on 3^3, 4^3). So for lam != 0 only a = 1/2, b = 0 (flat law) works; block 97's b = 1 with "
          "a = 1 forms the second pair with weight w(d) where the pair law has 1/w(d). PARTIAL exact (a), (c) on the ring of 7: "
          "voids first (formation weight w^b); z E[fill time] rises from the quasi-static to the no-motion value.")
    print("HIT: block 95's clocked gas with formation at rate z w^b at empty sites (records permanent) keeps block 95's pair "
          "law on the occupied set at every count iff lam = 0 or (a = 1/2, b = 0): the creation flux forces b = 1 - 2a and "
          "the count-2 total formation rate varies with the pair's separation for every lam b != 0 (exact on rings 4-8 and "
          "3^3, 4^3); block 97's principle b = 1 with a = 1 forms pairs with weight w(d), the inverse of the pair law 1/w(d)")


if __name__ == "__main__":
    main()
