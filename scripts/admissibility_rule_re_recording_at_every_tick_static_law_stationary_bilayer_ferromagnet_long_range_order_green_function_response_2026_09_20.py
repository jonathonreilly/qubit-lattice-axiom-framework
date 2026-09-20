#!/usr/bin/env python3
"""Exact checks: re-recording at every tick with the covariant rule.

Scope (conditional on a supplied clause that the axioms memo excludes: a record at every site at every tick).  T1: with the axioms'
nearest-neighbour rule, asynchronous re-recording is reversible for the static law of block 01, and synchronous re-recording on a
bipartite window splits into two alternating chains whose space-time checkerboard has the static law as a stationary law.  T2: with the
site's own previous record added to the past (the symmetric seven-site stencil), the synchronous chain is reversible for
pi(s) = prod_x Z_x(s), pi is one layer of the pair ferromagnet on the doubled graph Gamma, and for even L the map
(x, a) -> (x, a + |x| mod 2) carries Gamma onto the bilayer (Z/L)^3 x K_2, whose bond-plane reflections and layer swap have crossing
edges of the form {u, theta u} and together cross every edge.  T3: the Laplacian of Gamma has the bands E(k) and 14 - E(k); the
infrared bound and the sum rule give <|m_0|^2> >= 1 - (3/(2 beta))(G_L + H_L); the bound is verified exactly on a one-dimensional
two-valued instance; the constants I_0, I_2 are bracketed by exact series.  T4: the linearized law has static response 7/E(k) (the
lattice Green function) and equal-tick covariance (7 sigma^2/2)(1/E + 1/(14 - E)), verified symbolically and exactly on the 3^3 torus.
Exact arithmetic only (integers, Fractions and sympy); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import random
import re
import sys
from fractions import Fraction
from math import comb, factorial
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_RE_RECORDING_AT_EVERY_TICK_STATIC_LAW_STATIONARY_LIGHT_CONE_BILAYER_LONG_RANGE_ORDER_GREEN_FUNCTION_RESPONSE_CONDITIONAL_ON_AN_EXCLUDED_CLAUSE_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_re_recording_at_every_tick_static_law_stationary_light_cone_bilayer_long_range_order_green_function_response_conditional_on_an_excluded_clause_bounded_theorem_note_2026-09-20"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "A site never carries more than one record; records are permanent.",
)

MUTATION_GATE = {
    "async_balance_wrong": "B",
    "checkerboard_wrong": "B",
    "reversibility_wrong": "C",
    "bilayer_map_wrong": "C",
    "spectrum_wrong": "D",
    "infrared_bound_wrong": "D",
    "response_symbol_wrong": "E",
    "claim_transition_injected": "F",
    "claim_classical_name_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: set[str] = set()

    def check(self, tag: str, ok: bool, msg: str) -> None:
        if ok:
            self.passed += 1
            print(f"PASS: {tag} {msg}")
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, block01 = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    norm = normalize_text(axioms)
    checks.check("A2", all(n in norm for n in AXIOM_NEEDLES), "the axioms memo carries the four sentences used, among them the one-record-per-site sentence that the supplied clause contradicts")
    checks.check("A3", BLOCK01_CLAIM_ID in block01 and BLOCK01_FRAGMENT in normalize_text(block01), "block 01 on main carries its claim id and the static law of a product rule")


# ============================================================================================ family B (the axioms' rule, re-recorded)
def weight_six(p, q, r):
    """six-axis weight: values 0..5, the opposite axis of v is v ^ 1"""
    return [[Fraction(p) if a == b else Fraction(q) if a == (b ^ 1) else Fraction(r) for b in range(6)] for a in range(6)]


def static_weight_cycle(W, s):
    n = len(s)
    out = Fraction(1)
    for x in range(n):
        out *= W[s[x]][s[(x + 1) % n]]
    return out


def kernel(W, vals, past):
    """the covariant rule: the law of a new record given the records in its past (any number of them)"""
    w = []
    for a in vals:
        t = Fraction(1)
        for b in past:
            t *= W[a][b]
        w.append(t)
    z = sum(w)
    return [t / z for t in w], z


def family_b(checks: Checks) -> None:
    ok1 = True
    ok2 = True
    ok3 = True
    for (p, q, r) in ((3, 1, 2), (5, 2, 4)):
        W = weight_six(p, q, r)
        vals = range(6)
        configs = list(itertools.product(vals, repeat=4))
        mu = {s: static_weight_cycle(W, s) for s in configs}
        # B1: asynchronous re-recording at one site is in detailed balance with the static law
        for s in configs:
            for x in range(4):
                left, right = s[(x - 1) % 4], s[(x + 1) % 4]
                if mut("async_balance_wrong"):
                    raw = [W[a][left] * W[a][left] * W[a][right] for a in vals]
                    k = [t / sum(raw) for t in raw]
                else:
                    k, _ = kernel(W, vals, (left, right))
                for a in vals:
                    s2 = s[:x] + (a,) + s[x + 1:]
                    if mu[s] * k[a] != mu[s2] * k[s[x]]:
                        ok1 = False
        # B2: on the bipartite cycle the class-0 records are conditionally independent given class 1, with the rule as the conditional
        cls0 = (0, 1) if mut("checkerboard_wrong") else (0, 2)
        cls1 = tuple(x for x in range(4) if x not in cls0)
        marg1 = {}
        for s in configs:
            key = tuple(s[x] for x in cls1)
            marg1[key] = marg1.get(key, 0) + mu[s]
        for s in configs:
            key = tuple(s[x] for x in cls1)
            prod = Fraction(1)
            for x in cls0:
                k, _ = kernel(W, vals, (s[(x - 1) % 4], s[(x + 1) % 4]))
                prod *= k[s[x]]
            if mu[s] != marg1[key] * prod:
                ok2 = False
        # B3: the block update of class 0 given class 1 maps the class-1 marginal to the class-0 marginal (the alternating chain is stationary)
        marg0 = {}
        for s in configs:
            key = tuple(s[x] for x in (0, 2))
            marg0[key] = marg0.get(key, 0) + mu[s]
        m1 = {}
        for s in configs:
            key = (s[1], s[3])
            m1[key] = m1.get(key, 0) + mu[s]
        for e in itertools.product(vals, repeat=2):
            tot = Fraction(0)
            for o, wgt in m1.items():
                k0, _ = kernel(W, vals, (o[1], o[0]))      # site 0: neighbours 3 and 1
                k2, _ = kernel(W, vals, (o[0], o[1]))      # site 2: neighbours 1 and 3
                tot += wgt * k0[e[0]] * k2[e[1]]
            if tot != marg0[e]:
                ok3 = False
    checks.check("B1", ok1, "T1(a): on the four-cycle with the six-axis rule at (3,1,2) and (5,2,4), re-recording one site from its two neighbours is in detailed balance with the static law, for every configuration, site and new value")
    checks.check("B2", ok2, "T1(b): the static law's conditional of one bipartition class given the other is the product of the rule's one-site kernels (every configuration): the synchronous step of a class is a draw from that conditional")
    checks.check("B3", ok3, "T1(b): the synchronous step carries the static law's class-1 marginal to its class-0 marginal, so the space-time checkerboard of the alternating chain has the static law as a stationary law")


# ============================================================================================ family C (the seven-site stencil: reversibility, the doubled graph, the bilayer)
def family_c(checks: Checks) -> None:
    # C1: reversibility on the four-cycle with the site itself in the past, two-valued menu, exhaustive
    ok1 = True
    ok_marg = True
    for (p, q) in ((3, 1), (5, 2)):
        W = [[Fraction(p), Fraction(q)], [Fraction(q), Fraction(p)]]
        vals = range(2)
        configs = list(itertools.product(vals, repeat=4))

        def past(s, x):
            if mut("reversibility_wrong"):
                return (s[(x - 1) % 4], s[x])          # a one-sided past
            return (s[(x - 1) % 4], s[x], s[(x + 1) % 4])

        pi = {}
        for s in configs:
            w = Fraction(1)
            for x in range(4):
                w *= kernel(W, vals, past(s, x))[1]
            pi[s] = w
        for s in configs:
            ks = [kernel(W, vals, past(s, x))[0] for x in range(4)]
            for s2 in configs:
                ks2 = [kernel(W, vals, past(s2, x))[0] for x in range(4)]
                f = pi[s]
                b = pi[s2]
                for x in range(4):
                    f *= ks[x][s2[x]]
                    b *= ks2[x][s[x]]
                if f != b:
                    ok1 = False
        # pi is the layer-0 marginal of the pair law on the doubled graph
        for s0 in configs:
            tot = Fraction(0)
            for s1 in configs:
                w = Fraction(1)
                for x in range(4):
                    for y in ((x - 1) % 4, x, (x + 1) % 4):
                        w *= W[s1[x]][s0[y]]
                tot += w
            if tot != pi[s0] and not mut("reversibility_wrong"):
                ok_marg = False
    checks.check("C1", ok1, "T2: with the site's own record in the past, the synchronous chain on the four-cycle is in detailed balance with pi(s) = prod_x Z_x(s), for all 256 pairs of configurations at two weight pairs")
    checks.check("C2", ok_marg, "T2: pi is the layer-0 marginal of the pair law on the doubled graph, exactly")
    # C3: six-axis menu, random pairs on the four-cycle
    rng = random.Random(36)
    W = weight_six(3, 1, 2)
    vals = range(6)
    ok3 = True
    for _ in range(400):
        s = tuple(rng.randrange(6) for _ in range(4))
        s2 = tuple(rng.randrange(6) for _ in range(4))
        f = Fraction(1)
        b = Fraction(1)
        for x in range(4):
            kx, zx = kernel(W, vals, (s[(x - 1) % 4], s[x], s[(x + 1) % 4]))
            ky, zy = kernel(W, vals, (s2[(x - 1) % 4], s2[x], s2[(x + 1) % 4]))
            f *= zx * kx[s2[x]]
            b *= zy * ky[s[x]]
        if f != b:
            ok3 = False
    checks.check("C3", ok3, "T2: the same detailed balance for the six-axis rule at (3,1,2) on 400 random pairs of configurations")
    # C4: the doubled graph is the bilayer; its reflections
    ok_iso = True
    ok_refl = True
    ok_cover = True
    for L in (4, 6):
        sites = list(itertools.product(range(L), repeat=3))
        steps = [(0, 0, 0)] + [tuple((d if i == j else 0) for i in range(3)) for j in range(3) for d in (1, -1)]
        add = lambda x, e: tuple((x[i] + e[i]) % L for i in range(3))
        gamma = {frozenset({(x, 0), (add(x, e), 1)}) for x in sites for e in steps}
        bil = {frozenset({(x, b), (add(x, e), b)}) for x in sites for b in (0, 1) for e in steps[1:]} | {frozenset({(x, 0), (x, 1)}) for x in sites}
        par = lambda x: sum(x) % 2
        f = (lambda v: v) if mut("bilayer_map_wrong") else (lambda v: (v[0], (v[1] + par(v[0])) % 2))
        image = {frozenset(f(v) for v in e) for e in gamma}
        if image != bil or len(gamma) != 7 * L ** 3:
            ok_iso = False
        if L == 4:
            crossed = set()
            for j in range(3):
                for c in range(L // 2):
                    rho = lambda x: tuple(((2 * c + 1 - x[i]) % L) if i == j else x[i] for i in range(3))
                    theta = lambda v: (rho(v[0]), 1 - v[1])
                    plus = lambda v: ((v[0][j] - c - 1) % L) < L // 2
                    if any(frozenset(theta(v) for v in e) not in gamma for e in gamma):
                        ok_refl = False
                    for e in gamma:
                        u, v = tuple(e)
                        if plus(u) != plus(v):
                            crossed.add(e)
                            if theta(u) != v:
                                ok_refl = False
            cls = lambda v: (v[1] + par(v[0])) % 2
            for e in gamma:
                u, v = tuple(e)
                if cls(u) != cls(v):
                    crossed.add(e)
                    if u[0] != v[0]:
                        ok_refl = False
                elif u[0] == v[0]:
                    ok_refl = False
            if crossed != gamma:
                ok_cover = False
    checks.check("C4", ok_iso, "T2: for L = 4 and 6 the map (x, a) -> (x, a + |x| mod 2) carries the doubled graph (7 L^3 edges) onto the bilayer (Z/L)^3 x K_2 edge for edge")
    checks.check("C5", ok_refl, "T3: on L = 4 every bond-plane reflection composed with the layer swap is an automorphism whose crossing edges are {u, theta u}; the two classes of the bipartition are separated exactly by the vertical edges, each {u, sigma u}")
    checks.check("C6", ok_cover, "T3: every edge of the doubled graph is crossed by one of these reflections")


# ============================================================================================ family D (bands, the infrared bound, the constants)
def exp_lower(x: Fraction, terms: int = 14) -> Fraction:
    return sum(x ** j / factorial(j) for j in range(terms))


def ising_bilayer_cycle(L: int):
    """two-valued records on the doubled graph of the L-cycle, weight 2 per aligned edge pair (e^beta = 2 after a common factor)"""
    edges = [((x, 0), ((x + d) % L, 1)) for x in range(L) for d in (-1, 0, 1)]
    idx = {(x, a): a * L + x for x in range(L) for a in (0, 1)}
    Z = 0
    acc = {}
    for bits in itertools.product((1, -1), repeat=2 * L):
        aligned = sum(1 for u, v in edges if bits[idx[u]] == bits[idx[v]])
        w = 4 ** aligned
        Z += w
        for band in (1, -1):
            d = [bits[idx[(x, 0)]] + band * bits[idx[(x, 1)]] for x in range(L)]
            for n in range(L):
                c = sum(cos_table(L, n * x) * d[x] for x in range(L))
                sn = sum(sin_unit(L, n * x) * d[x] for x in range(L))
                val = Fraction(1, 2) * (c * c + sin_sq_scale(L) * sn * sn)
                acc[(band, n)] = acc.get((band, n), 0) + w * val
    return {k: Fraction(v) / Z for k, v in acc.items()}


def cos_table(L: int, m: int) -> Fraction:
    m %= L
    if L == 4:
        return Fraction((1, 0, -1, 0)[m])
    return (Fraction(1), Fraction(1, 2), Fraction(-1, 2), Fraction(-1), Fraction(-1, 2), Fraction(1, 2))[m]


def sin_unit(L: int, m: int) -> int:
    m %= L
    if L == 4:
        return (0, 1, 0, -1)[m]
    return (0, 1, 1, 0, -1, -1)[m]


def sin_sq_scale(L: int) -> Fraction:
    return Fraction(1) if L == 4 else Fraction(3, 4)


def return_numerators(M: int):
    """b_m = C(2m, m) sum_k C(m, k)^2 C(2k, k): the return probability of the cubic walk after 2m steps is b_m / 36^m"""
    return [comb(2 * m, m) * sum(comb(m, k) ** 2 * comb(2 * k, k) for k in range(m + 1)) for m in range(M + 1)]


def family_d(checks: Checks) -> None:
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    E = 6 - 2 * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3))
    A = 1 + 2 * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3))
    Lap = sp.Matrix([[7, -A], [-A, 7]])
    upper = (12 - E) if mut("spectrum_wrong") else (14 - E)
    ok = sp.simplify(Lap.det() - E * upper) == 0 and sp.simplify(Lap.trace() - (E + upper)) == 0
    shifted = E.subs({k1: k1 + sp.pi, k2: k2 + sp.pi, k3: k3 + sp.pi}, simultaneous=True)
    ok = ok and sp.simplify(14 - E - (shifted + 2)) == 0
    checks.check("D1", ok, "T3: the Laplacian of the doubled graph has symbol [[7, -A], [-A, 7]], A = 1 + 2 sum cos k_j, with the two bands E(k) and 14 - E(k) = E(k + pi) + 2")
    # D2: the infrared bound, exactly, on a small two-valued instance (one component: <|s_band(k)|^2> <= N / (beta lambda)), with beta = log 2 < 6932/10000
    beta_up = Fraction(6932, 10000)
    ok_beta = exp_lower(beta_up) > 2
    ok_ir = True
    worst = Fraction(0)
    for L in (4, 6):
        table = ising_bilayer_cycle(L)
        for (band, n), val in table.items():
            e1 = 2 - 2 * cos_table(L, n)
            lam = e1 if band == 1 else 6 - e1
            if lam == 0:
                continue
            if mut("infrared_bound_wrong"):
                lam = lam * 40
            ratio = val * lam * beta_up / L
            worst = max(worst, ratio)
            if ratio > 1:
                ok_ir = False
    checks.check("D2", ok_beta and ok_ir, f"T3: on the doubled graph of the 4- and 6-cycle with two-valued records at e^beta = 2, every nonzero mode of both bands satisfies the infrared bound exactly (largest ratio to the bound {worst.numerator * 1000 // worst.denominator}/1000; log 2 < 6932/10000 by an exact partial sum)")
    # D3: the constants.  I_0 = (1/6) sum_m b_m/36^m (lower bounds by partial sums); I_2 = (1/8) sum_m (9/16)^m b_m/36^m with a geometric tail
    M = 60
    b = return_numerators(M)
    ok_rec = all(n ** 3 * b[n] == 2 * (2 * n - 1) * (10 * n * n - 10 * n + 3) * b[n - 1] - 36 * (n - 1) * (2 * n - 1) * (2 * n - 3) * b[n - 2] for n in range(2, M + 1))
    part0 = Fraction(1, 6) * sum(Fraction(b[m], 36 ** m) for m in range(M + 1))
    part2 = Fraction(1, 8) * sum(Fraction(9, 16) ** m * Fraction(b[m], 36 ** m) for m in range(M + 1))
    tail2 = Fraction(1, 8) * Fraction(9, 16) ** (M + 1) / (1 - Fraction(9, 16))
    i2_lo, i2_hi = part2, part2 + tail2
    ok_i2 = Fraction(1409314, 10 ** 7) < i2_lo and i2_hi < Fraction(1409316, 10 ** 7)
    ok_i0 = part0 > Fraction(23, 100)
    beta0_hi = Fraction(3, 2) * (Fraction(76, 300) + i2_hi)
    ok_b0 = beta0_hi < Fraction(5914, 10000) and Fraction(3, 2) * (part0 + i2_lo) > Fraction(55, 100)
    checks.check("D3", ok_rec and ok_i2 and ok_i0 and ok_b0, "T3: the closed-walk numbers obey their three-term recursion to m = 60; I_2 lies in (1409314, 1409316)/10^7 by 61 exact terms and a geometric tail; with block 22's bracket 3 I_0 < 76/100 the ordering coupling beta_0 = (3/2)(I_0 + I_2) is below 5914/10000, and above 55/100 by partial sums")
    # D4: the finite-volume sums at L = 4, exactly, and the bound they give
    L = 4
    g = Fraction(0)
    h = Fraction(0)
    for n in itertools.product(range(L), repeat=3):
        e = 6 - 2 * sum(cos_table(L, m) for m in n)
        if any(n):
            g += 1 / e
        h += 1 / (14 - e)
    g /= L ** 3
    h /= L ** 3
    checks.check("D4", g > 0 and h > 0 and g + h < Fraction(1, 2), f"T3: the torus sums at L = 4 are G = {g} and H = {h}; the bound 1 - (3/(2 beta))(G + H) is positive there for beta > {Fraction(3, 2) * (g + h)}")


# ============================================================================================ family E (the linearized law: response and covariance)
def family_e(checks: Checks) -> None:
    k1, k2, k3, s2 = sp.symbols("k1 k2 k3 sigma2", real=True)
    E = 6 - 2 * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3))
    phi7 = (1 + 2 * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3))) / 7
    phi6 = (2 * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3))) / 6
    num = 6 if mut("response_symbol_wrong") else 7
    ok = sp.simplify(1 / (1 - phi7) - num / E) == 0
    ok = ok and sp.simplify(s2 / (1 - phi7 ** 2) - sp.Rational(7, 2) * s2 * (1 / E + 1 / (14 - E))) == 0
    ok = ok and sp.simplify((1 / (1 - phi7)) / (s2 / (1 - phi7 ** 2)) - (1 + phi7) / s2) == 0
    ok6 = sp.simplify(1 / (1 - phi6) - 6 / E) == 0 and sp.simplify(s2 / (1 - phi6 ** 2) - 3 * s2 * (1 / E + 1 / (12 - E))) == 0
    ok6 = ok6 and sp.simplify(phi6.subs({k1: sp.pi, k2: sp.pi, k3: sp.pi}) + 1) == 0 and sp.simplify(phi7.subs({k1: sp.pi, k2: sp.pi, k3: sp.pi}) + sp.Rational(5, 7)) == 0
    checks.check("E1", ok, "T4: for the seven-site stencil phi = 1 - E/7, the static response 1/(1 - phi) is 7/E(k), the equal-tick covariance sigma^2/(1 - phi^2) is (7 sigma^2/2)(1/E + 1/(14 - E)), and response/covariance = (1 + phi)/sigma^2")
    checks.check("E2", ok6, "T4: for the six-site stencil the response is 6/E(k) and the covariance 3 sigma^2 (1/E + 1/(12 - E)), with a second pole at (pi, pi, pi) where phi = -1 (the two alternating chains); with the site in the past phi = -5/7 there")
    # E3: exact propagation on the 3^3 torus: the stationary mean around a persistent source and the stationary covariance
    L = 3
    sites = list(itertools.product(range(L), repeat=3))
    ix = {x: i for i, x in enumerate(sites)}
    N = len(sites)
    P = sp.zeros(N, N)
    for x in sites:
        for e in [(0, 0, 0)] + [tuple((d if i == j else 0) for i in range(3)) for j in range(3) for d in (1, -1)]:
            y = tuple((x[i] + e[i]) % L for i in range(3))
            P[ix[x], ix[y]] += sp.Rational(1, 7)
    cosr = lambda m: sp.Integer(1) if m % 3 == 0 else sp.Rational(-1, 2)
    modes = [n for n in itertools.product(range(L), repeat=3) if any(n)]
    Eval = lambda n: 6 - 2 * sum(cosr(m) for m in n)
    chi = sp.Matrix([sum(cosr(sum(n[i] * x[i] for i in range(3))) * 7 / Eval(n) for n in modes) / N for x in sites])
    src = sp.Matrix([(1 if x == (0, 0, 0) else 0) - sp.Rational(1, N) for x in sites])
    ok3 = (sp.eye(N) - P) * chi == src
    cov = sp.Matrix(N, N, lambda i, j: sum(cosr(sum(n[a] * (sites[i][a] - sites[j][a]) for a in range(3))) / (1 - (1 - Eval(n) / 7) ** 2) for n in modes) / N)
    Q = sp.eye(N) - sp.ones(N, N) / N
    ok3 = ok3 and (P * cov * P.T + Q - cov) == sp.zeros(N, N)
    checks.check("E3", ok3, "T4: on the 3^3 torus, exactly: the mean around a persistent unit source solves (I - P) chi = delta_0 - 1/N with chi the transform of 7/E, and the transform of 1/(1 - phi^2) is the fixed point of Sigma = P Sigma P^T + (I - J/N)")


# ============================================================================================ family F
FENCES = (
    "This note is conditional on a clause that the axioms memo excludes: it supposes a record at every site at every tick, while the memo says that a site never carries more than one record and that records are permanent.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at beta = 59/100."}
CLASSICAL_NAMES = ("Toom", "Berman", "Simon", "Spencer", "Gács", "Mermin", "Wagner", "Bramson", "Gray", "Krylov", "Bogolyubov", "Choquet", "Peierls", "Dobrushin", "Fourier", "Parseval", "Goldstone", "Heisenberg", "Ising", "Glauber", "Watson", "Schwarz", "Cauchy", "Taylor", "Gibbs")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T2", "## Theorem T2 (after Heisenberg)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + nm + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + nm + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — detailed balance of one-site re-recording with the static law; the conditional of one class given the other; the band symbols; the response and covariance symbols",
    "per_site: executed — every configuration of the four-cycle at two weight triples; all 256 pairs for the seven-site stencil; the 3^3 torus propagation of the mean and the covariance, exactly",
    "per_mode: executed — the infrared bound for every nonzero mode of both bands on the doubled 4- and 6-cycle with two-valued records, exactly",
    "per_block: executed — the doubled graph onto the bilayer for L = 4 and 6, edge for edge; every reflection's crossing edges; the cover of all edges",
    "lattice_wide: T1-T4 are proved for every even torus under the supplied clause; the ordering coupling is below 5914/10000 given block 22's bracket; the nonlinear law's memory and its potential around a source are executed in the controls and not claimed; the clause itself contradicts the axioms memo and is not adopted",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


# ============================================================================================ main
def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        ACTIVE_MUTATION = argv[argv.index("--mutation") + 1]
        if ACTIVE_MUTATION not in MUTATION_GATE:
            print(f"unknown mutation {ACTIVE_MUTATION}")
            return 2
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    texts = [Path(ROOT, p).read_text(encoding="utf-8") if Path(ROOT, p).exists() else "" for p in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: re-recording at every tick (a clause the axioms memo excludes) — the static law is stationary for the axioms' rule; the seven-site stencil is one layer of a bilayer pair ferromagnet; the infrared bound and the ordering coupling; the Green-function response; exact")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
