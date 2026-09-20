#!/usr/bin/env python3
"""Exact checks: records interacting through the odds of unformed sites.

Scope (a supplied reading, not adopted: an unformed site carries its probability distribution over the possibilities, and that
distribution is a condition for its neighbours).  T1, exact summation (an unformed site is one unknown content, summed): across a
straight gap of n bonds two records weigh, against chance, 1 + 3 l1^n + 2 l2^n (equal contents), 1 - 3 l1^n + 2 l2^n (opposite),
1 - l2^n (orthogonal), l1 = (p-q)/(p+q+4r), l2 = (p+q-2r)/(p+q+4r); averaged over contents the weight is exactly 1, and every
arrangement of k records weighs z^k Z: contents interact across empty sites, masses do not.  T2, the self-consistent odds
pi_x(s) ~ prod_y sum_b omega(s,b) pi_y(b): the derivative of the map at the uniform field is K_1 - 1/6 per neighbour, the linearized
field equation is delta_x = sum_y K_1 delta_y with spectrum l_i (6 - E(k)), the uniform field is linearly stable iff 6 |l_i| < 1,
the vector channel is massless on 5p = 7q + 4r (where (3,1,2) sits), and away from it the response to a source is the screened
lattice Green function with m^2 = (1 - 6 l1)/l1.  T3, a proved regime: the map contracts the ratio metric by 1 - kappa per neighbour,
so for 6 (1 - kappa) < 1 the odds exist, are unique for every arrangement of records, and the influence of a record decays
geometrically.  T4, what it carries: the map is covariant under the rotation of all contents, so the first-order source is the
content vector; the content-averaged weight of a site is 1 + 3 l1^2 sum_{y<y'} m_y.m_y' + ..., second order in the leans.  T5, with
'no record' counted among the possibilities: the scalar (mass) channel has first-order strength rho (1-rho)(g-1)/(1+rho(g-1)),
g = c/c_0 the glue, zero at the neutral scale; the vector channel has strength rho g l1/(1+rho(g-1)).
T6, records are boundary values: in the linearized vector channel the field of a set S of agreeing records is u = 1 on S,
u_x = l1 (sum of the six neighbours) off S; its charge on a record, 1 - l1 (sum of u over the neighbours), is 1 - 6 l1 on a record
all of whose neighbours are records, the capacity (total charge) per record falls as the body grows, and u is monotone and subadditive
in S: the source strength of a body is its capacity, not its number of records.
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import random
import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_INTERACTION_THROUGH_THE_ODDS_OF_UNFORMED_SITES_FIELD_EQUATION_MASSLESS_SURFACE_CONTENT_CHARGE_NO_FIRST_ORDER_MASS_CHANNEL_AT_NEUTRAL_SCALE_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_interaction_through_the_odds_of_unformed_sites_field_equation_massless_surface_content_charge_no_first_order_mass_channel_at_neutral_scale_bounded_theorem_note_2026-09-20"
AXIOM_NEEDLES = (
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "A site with no record cannot be read.",
    "No possibility is privileged.",
)

MUTATION_GATE = {
    "gap_formula_wrong": "B",
    "bondwise_average_instead_of_coherent_sum": "B",
    "jacobian_without_normalization": "C",
    "massless_surface_wrong": "C",
    "green_function_mass_wrong": "C",
    "contraction_constant_too_large_kappa": "D",
    "product_bound_dropped_factor": "D",
    "map_not_covariant_injected": "E",
    "second_order_coefficient_wrong": "E",
    "scalar_channel_glue_at_neutral_scale": "E",
    "interior_charge_wrong": "H",
    "capacity_additive_injected": "H",
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


M6 = range(6)
AXIS = {0: (0, 0, 1), 1: (0, 0, -1), 2: (1, 0, 0), 3: (-1, 0, 0), 4: (0, 1, 0), 5: (0, -1, 0)}
INDEX = {v: k for k, v in AXIS.items()}


def omega(p, q, r):
    return [[Fraction(p if a == b else q if a == (b ^ 1) else r) for b in M6] for a in M6]


def k1(p, q, r):
    t = p + q + 4 * r
    return [[v / t for v in row] for row in omega(p, q, r)]


def lam(p, q, r):
    t = Fraction(p + q + 4 * r)
    return Fraction(p - q) / t, Fraction(p + q - 2 * r) / t


def matpow(m, n):
    out = [[Fraction(int(i == j)) for j in M6] for i in M6]
    for _ in range(n):
        out = [[sum(out[i][k] * m[k][j] for k in M6) for j in M6] for i in M6]
    return out


class Dual:
    """a value with its first derivative, exact"""

    def __init__(self, a, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    @staticmethod
    def lift(o):
        return o if isinstance(o, Dual) else Dual(o)

    def __add__(self, o):
        o = Dual.lift(o)
        return Dual(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __mul__(self, o):
        o = Dual.lift(o)
        return Dual(self.a * o.a, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = Dual.lift(o)
        return Dual(self.a / o.a, (self.b * o.a - self.a * o.b) / (o.a * o.a))


def odds_at(om, nbr_fields, normalize=True):
    """the odds of an unformed site from its neighbours' conditions (six weights each; a record is a point mass)"""
    n = []
    for s in M6:
        t = 1
        for f in nbr_fields:
            t = t * sum((om[s][b] * f[b] for b in M6[1:]), om[s][0] * f[0])
        n.append(t)
    tot = sum(n[1:], n[0])
    return ([v / tot for v in n] if normalize else n), tot


def rnd_dist(rng, n=6, spread=12):
    w = [Fraction(rng.randint(1, spread), rng.randint(1, 3)) for _ in range(n)]
    t = sum(w)
    return [v / t for v in w]


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the sentences used")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    ok, avg = True, True
    for (p, q, r) in ((12, 1, 2), (3, 1, 2), (5, 2, 4)):
        k = k1(p, q, r)
        l1, l2 = lam(p, q, r)
        for n in range(1, 7):
            m = matpow(k, n)
            c3 = 2 if mut("gap_formula_wrong") else 3
            ok = ok and 6 * m[0][0] == 1 + c3 * l1 ** n + 2 * l2 ** n and 6 * m[0][1] == 1 - c3 * l1 ** n + 2 * l2 ** n and 6 * m[0][2] == 1 - l2 ** n
            avg = avg and sum(6 * m[0][b] for b in M6) == 6
    checks.check("B1", ok and avg, "T1: an unformed site summed as one unknown content: across a straight gap of n = 1..6 bonds two records weigh, against chance, 1 + 3 l1^n + 2 l2^n (equal), 1 - 3 l1^n + 2 l2^n (opposite), 1 - l2^n (orthogonal) at three triples, and the average over contents is exactly 1")
    # arrangements: on a window every arrangement of records weighs z^k Z once the unformed sites are summed; contents are correlated across an empty site
    om = omega(3, 1, 2)
    bonds = [(0, 1), (1, 2), (2, 3), (3, 0)]
    z_all = sum(_w(om, bonds, cfg) for cfg in product(M6, repeat=4))
    ok2 = True
    for k in range(5):
        for eta in _subsets(4, k):
            tot = Fraction(0)
            for s_eta in product(M6, repeat=k):
                tot += _summed_weight(om, bonds, 4, dict(zip(eta, s_eta)))
            ok2 = ok2 and tot == z_all
    joint = {(a, b): _summed_weight(om, bonds, 4, {0: a, 2: b}, bondwise=mut("bondwise_average_instead_of_coherent_sum")) for a in M6 for b in M6}
    tot = sum(joint.values())
    dependent = any(joint[a, b] / tot != Fraction(1, 36) for a in M6 for b in M6)
    checks.check("B2", ok2 and dependent, "T1: on the plaquette at (3,1,2) every one of the 16 arrangements of records weighs Z once contents are summed (no weight attaches to where the records are: masses do not interact), while the contents of two records across unformed sites are correlated")


def _subsets(n, k):
    from itertools import combinations
    return list(combinations(range(n), k))


def _w(om, bonds, cfg):
    t = Fraction(1)
    for (i, j) in bonds:
        t *= om[cfg[i]][cfg[j]]
    return t


def _summed_weight(om, bonds, n, fixed, bondwise=False):
    """records with the contents in `fixed`; unformed sites summed as one unknown content each (or, bondwise, weighing 1 on each bond)"""
    free = [i for i in range(n) if i not in fixed]
    if bondwise:
        t = Fraction(1)
        for (i, j) in bonds:
            if i in fixed and j in fixed:
                t *= om[fixed[i]][fixed[j]]
        return t
    tot = Fraction(0)
    for vals in product(M6, repeat=len(free)):
        cfg = dict(fixed)
        cfg.update(zip(free, vals))
        tot += _w(om, bonds, cfg)
    return tot


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    rng = random.Random(11)
    p, q, r = 5, 2, 4
    om, k, t = omega(p, q, r), k1(p, q, r), p + q + 4 * r
    fields = [rnd_dist(rng) for _ in range(6)]
    pi, tot = odds_at(om, fields)
    ok = True
    for s in M6:
        pr = Fraction(t, 6) ** 6
        for f in fields:
            pr *= 1 + 6 * sum(k[s][b] * (f[b] - Fraction(1, 6)) for b in M6)
        ok = ok and pr / tot == pi[s]
    checks.check("C1", ok, "T2: the odds of an unformed site factorize exactly as (T/6)^6 prod_y (1 + 6 (K_1 delta_y)(s)) over its six neighbours, delta_y the departure of neighbour y's odds from the uniform ones")
    ok = True
    for b in M6:
        fl = [[Dual(Fraction(1, 6), 1 if (i == 0 and c == b) else 0) for c in M6] for i in range(6)]
        out, _ = odds_at(om, fl, normalize=not mut("jacobian_without_normalization"))
        for s in M6:
            ok = ok and out[s].b == k[s][b] - Fraction(1, 6)
    checks.check("C2", ok, "T2: the exact derivative of the odds map at the uniform field, with respect to one neighbour's odds, is K_1(s,b) - 1/6 (all 36 entries, by exact differentiation): on departures of zero sum, delta_x = sum over neighbours of K_1 delta_y")
    # spectrum on the 4^3 torus: cos-waves times the eigenvectors of K_1
    L = 4
    cosv = (1, 0, -1, 0)
    l1, l2 = lam(p, q, r)
    vec = [Fraction(AXIS[s][2]) for s in M6]
    quad = [Fraction(2 if AXIS[s][2] else -1) for s in M6]
    ok = all(sum(k[s][b] * vec[b] for b in M6) == l1 * vec[s] and sum(k[s][b] * quad[b] for b in M6) == l2 * quad[s] for s in M6)
    for kk in ((0, 0, 0), (1, 0, 0), (2, 2, 0), (2, 2, 2), (1, 2, 1)):
        adj = 2 * sum(cosv[c] for c in kk)
        for x in ((0, 0, 0), (1, 2, 3), (3, 1, 0)):
            wave = lambda y: cosv[sum(kk[i] * y[i] for i in range(3)) % L]
            nb_sum = sum(wave(tuple((x[j] + (d if j == i else 0)) % L for j in range(3))) for i in range(3) for d in (1, -1))
            ok = ok and nb_sum == adj * wave(x)
    checks.check("C3", ok, "T2: K_1 has the vector eigenvalue l1 and the quadrupole eigenvalue l2, and the sum over the six neighbours multiplies a cosine wave by 6 - E(k): the linearized map has the spectrum l_i (6 - E(k)), so the uniform field is linearly stable iff 6 |l_i| < 1")
    surf = lambda p_, q_, r_: (5 * p_ == 16 * r_ - 5 * q_) if mut("massless_surface_wrong") else (5 * p_ == 7 * q_ + 4 * r_)
    ok = surf(3, 1, 2) and 6 * lam(3, 1, 2)[0] == 1 and not surf(5, 2, 4) and not surf(7, 3, 5)
    ok = ok and (1 - 6 * lam(5, 2, 4)[0]) / lam(5, 2, 4)[0] == Fraction(5, 3) and (1 - 6 * lam(7, 3, 5)[0]) / lam(7, 3, 5)[0] == Fraction(3, 2) and 6 * lam(12, 1, 2)[0] > 1
    for (p_, q_, r_) in ((3, 1, 2), (11, 5, 5), (15, 5, 10), (4, 2, 3)):
        ok = ok and ((6 * lam(p_, q_, r_)[0] == 1) == (5 * p_ == 7 * q_ + 4 * r_))
    checks.check("C4", ok, "T2: the vector channel is massless, 6 l1 = 1, exactly on 5p = 7q + 4r; the declared triple (3,1,2) lies on it; (5,2,4) and (7,3,5) are screened with m^2 = (1 - 6 l1)/l1 = 5/3 and 3/2; at (12,1,2) 6 l1 = 22/7 > 1 and the uniform field is unstable")
    sites = list(product(range(L), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    a = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for s in sites:
        for i in range(3):
            for d in (1, -1):
                y = tuple((s[j] + (d if j == i else 0)) % L for j in range(3))
                a[idx[s]][idx[y]] -= l1
    rhs = [Fraction(0)] * n
    rhs[0] = Fraction(1)
    for c in range(n):
        piv = next(i for i in range(c, n) if a[i][c] != 0)
        a[c], a[piv] = a[piv], a[c]
        rhs[c], rhs[piv] = rhs[piv], rhs[c]
        inv = 1 / a[c][c]
        a[c] = [v * inv for v in a[c]]
        rhs[c] *= inv
        for i in range(n):
            if i != c and a[i][c] != 0:
                f = a[i][c]
                a[i] = [vi - f * vc for vi, vc in zip(a[i], a[c])]
                rhs[i] -= f * rhs[c]
    shift = Fraction(1, 7) if mut("green_function_mass_wrong") else 0
    mode = lambda x: sum(Fraction(cosv[sum(kk[i] * x[i] for i in range(3)) % L]) / (1 + shift - l1 * 2 * sum(cosv[c] for c in kk)) for kk in sites) / n
    ok = all(rhs[idx[s]] == mode(s) for s in sites) and rhs[idx[(0, 0, 0)]] > rhs[idx[(1, 0, 0)]] > rhs[idx[(2, 0, 0)]] > 0
    ones_in_kernel = all(1 - 6 * lam(3, 1, 2)[0] == 0 for _ in (0,))
    checks.check("C5", ok and ones_in_kernel, "T2: on the 4^3 torus at (5,2,4) the exact solution of v_x - l1 (sum of the six neighbours) = point source equals the mode sum of 1/(1 - l1 (6 - E(k))) at all 64 sites, positive and decreasing along an axis: the response is the screened lattice Green function with m^2 = (1 - 6 l1)/l1; at (3,1,2) the constant field is in the kernel (no mass term)")


# ============================================================================================ family D (T3)
def ratio_metric(x, y):
    g = [a / b for a, b in zip(x, y)]
    return max(g) / min(g)


def kappa(om, largest=False):
    vals = []
    for s in M6:
        for t in M6:
            if s != t:
                g = [om[s][b] / om[t][b] for b in M6]
                vals.append(min(g) / max(g))
    return max(vals) if largest else min(vals)


def family_d(checks: Checks) -> None:
    rng = random.Random(5)
    ok = True
    tight = Fraction(0)
    for (p, q, r) in ((3, 1, 2), (5, 2, 4), (21, 20, 20), (12, 1, 2)):
        om = omega(p, q, r)
        kp = kappa(om, largest=mut("contraction_constant_too_large_kappa"))
        for _ in range(400):
            x, y = rnd_dist(rng, spread=40), rnd_dist(rng, spread=40)
            r_in = ratio_metric(x, y)
            r_out = ratio_metric([sum(om[s][b] * x[b] for b in M6) for s in M6], [sum(om[s][b] * y[b] for b in M6) for s in M6])
            bound = r_in / ((1 - kp) + kp * r_in)
            ok = ok and r_out <= bound
            tight = max(tight, r_out / bound)
        # adversarial pairs: y concentrated on one content, x = y tilted hard towards the opposite one (the bound's extreme case 1/kappa)
        for (heavy, tilted) in ((1, 0), (0, 1), (2, 0), (0, 2), (3, 2)):
            y = [Fraction(1, 1000)] * 6
            y[heavy] = Fraction(995, 1000)
            x = [v * (10 ** 6 if b == tilted else 1) for b, v in enumerate(y)]
            tx = sum(x)
            x = [v / tx for v in x]
            r_in = ratio_metric(x, y)
            r_out = ratio_metric([sum(om[s][b] * x[b] for b in M6) for s in M6], [sum(om[s][b] * y[b] for b in M6) for s in M6])
            bound = r_in / ((1 - kp) + kp * r_in)
            ok = ok and r_out <= bound
            tight = max(tight, r_out / bound)
    checks.check("D1", ok, f"T3: one neighbour's factor contracts the ratio metric: R(omega x, omega y) <= R/((1 - kappa) + kappa R), kappa the least min/max ratio of two rows of omega, on 1600 exact random pairs and 20 adversarial pairs at four triples (tightest case {tight.numerator * 1000 // tight.denominator}/1000 of the bound); hence log R shrinks by 1 - kappa")
    ok = True
    om = omega(21, 20, 20)
    for case in range(200):
        fa = [rnd_dist(rng) for _ in range(6)]
        fb = [rnd_dist(rng) for _ in range(6)]
        if case % 2:
            fb = [fb[0]] + fa[1:]                                     # only the first neighbour differs
        pa, _ = odds_at(om, fa)
        pb, _ = odds_at(om, fb)
        bound = Fraction(1)
        kp = kappa(om)
        for i, (x, y) in enumerate(zip(fa, fb)):
            if mut("product_bound_dropped_factor") and i == 0:
                continue
            r_in = ratio_metric(x, y)
            bound *= r_in / ((1 - kp) + kp * r_in)
        ok = ok and ratio_metric(pa, pb) <= bound
    kp = kappa(omega(21, 20, 20))
    checks.check("D2", ok and 6 * (1 - kp) < 1 and 6 * (1 - kappa(omega(5, 2, 4))) > 1, f"T3: the odds of a site move by at most the product over its six neighbours of their contracted ratios (200 exact cases, half of them with a single differing neighbour); at (21,20,20) kappa = {kp} and 6 (1 - kappa) = {6 * (1 - kp)} < 1: there the odds exist, are unique for every arrangement of records, and the influence of a record decays geometrically; at (5,2,4) the criterion is silent")


# ============================================================================================ family E (T4, T5)
def rotations():
    rots = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            m = [[signs[i] if perm[i] == j else 0 for j in range(3)] for i in range(3)]
            det = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
            if det == 1:
                rots.append(m)
    return rots


def act(m, a):
    return INDEX[tuple(sum(m[i][j] * AXIS[a][j] for j in range(3)) for i in range(3))]


def odds7_at(om, c, z, nbr_fields):
    """seven outcomes: six contents and 'no record' (index 6)"""
    n = []
    for s in M6:
        t = z
        for f in nbr_fields:
            t = t * (f[6] + c * sum((om[s][b] * f[b] for b in M6[1:]), om[s][0] * f[0]))
        n.append(t)
    e = 1
    for f in nbr_fields:
        e = e * sum(f[1:], f[0])
    n.append(e)
    tot = sum(n[1:], n[0])
    return [v / tot for v in n]


def family_e(checks: Checks) -> None:
    rng = random.Random(3)
    om = omega(5, 2, 4)
    ok = True
    for m in rotations():
        fields = [rnd_dist(rng) for _ in range(5)]
        rec = [Fraction(int(b == 2)) for b in M6]                    # a record of content +x as the sixth neighbour
        base, _ = odds_at(om, fields + [rec])
        rot = lambda f: [f[[a for a in M6 if act(m, a) == b][0]] for b in M6]   # (R f)(b) = f(R^-1 b)
        if mut("map_not_covariant_injected"):
            om_used = [[om[s][b] * (2 if s == 0 else 1) for b in M6] for s in M6]
            base, _ = odds_at(om_used, fields + [rec])
            turned, _ = odds_at(om_used, [rot(f) for f in fields] + [rot(rec)])
        else:
            turned, _ = odds_at(om, [rot(f) for f in fields] + [rot(rec)])
        ok = ok and turned == rot(base)
    checks.check("E1", ok, "T4: the odds map is covariant under the 24 rotations of all contents, records included: the first-order source a record places in the odds is its content vector, odd and of zero mean, and no rotation-invariant (mass) source exists in the six-outcome odds, whose only invariant component is fixed by normalization")
    p, q, r = 5, 2, 4
    l1 = lam(p, q, r)[0]
    leans = [[Fraction(rng.randint(-3, 3), 40) for _ in range(3)] for _ in range(6)]
    def zrel(tt):
        fields = [[Fraction(1, 6) + tt * sum(mv[i] * AXIS[b][i] for i in range(3)) / 2 for b in M6] for mv in leans]
        _, tot = odds_at(omega(p, q, r), fields)
        return tot / (Fraction(p + q + 4 * r, 6) ** 6) / 6
    # exact interpolation of the degree-6 polynomial in tt: second-order coefficient by finite differences at tt = 0, +-1, +-2, +-3
    pts = {t_: zrel(Fraction(t_)) for t_ in range(-3, 4)}
    c1 = (Fraction(3, 4) * (pts[1] - pts[-1]) - Fraction(3, 20) * (pts[2] - pts[-2]) + Fraction(1, 60) * (pts[3] - pts[-3]))
    c2 = (Fraction(-49, 18) * pts[0] + Fraction(3, 2) * (pts[1] + pts[-1]) - Fraction(3, 20) * (pts[2] + pts[-2]) + Fraction(1, 90) * (pts[3] + pts[-3])) / 2
    coef = 2 if mut("second_order_coefficient_wrong") else 3
    want = coef * l1 ** 2 * sum(sum(leans[i][d] * leans[j][d] for d in range(3)) for i in range(6) for j in range(i + 1, 6))
    checks.check("E2", pts[0] == 1 and c1 == 0 and c2 == want, "T4: the content-averaged weight of a site against the void, as a polynomial in the neighbours' leans m_y, has no first-order term and the second-order term 3 l1^2 sum_{y<y'} m_y.m_y' (exact interpolation): what is blind to content enters at second order")
    ok = True
    shown = []
    for (rho, g) in ((Fraction(1, 2), Fraction(1)), (Fraction(3, 10), Fraction(1)), (Fraction(1, 2), Fraction(2)), (Fraction(3, 10), Fraction(3, 2))):
        c0 = Fraction(6, p + q + 4 * r)
        c = g * c0
        z = rho / (6 * (1 - rho) * (1 + rho * (g - 1)) ** 6)
        uni = [rho / 6] * 6 + [1 - rho]
        fixed = odds7_at(omega(p, q, r), c, z, [uni] * 6)
        ok = ok and fixed == uni
        jac = [[None] * 7 for _ in range(7)]
        for b in range(7):
            fl = [[Dual(uni[cc], 1 if (i == 0 and cc == b) else 0) for cc in range(7)] for i in range(6)]
            out = odds7_at(omega(p, q, r), c, z, fl)
            for s in range(7):
                jac[s][b] = out[s].b
        g_used = Fraction(2) if (mut("scalar_channel_glue_at_neutral_scale") and g == 1) else g
        lam_s = rho * (1 - rho) * (g_used - 1) / (1 + rho * (g_used - 1))
        lam_v = rho * g * l1 / (1 + rho * (g - 1))
        u_s = [Fraction(1, 6)] * 6 + [Fraction(-1)]
        u_v = [Fraction(AXIS[a][2], 2) for a in M6] + [Fraction(0)]
        ok = ok and [sum(jac[s][b] * u_s[b] for b in range(7)) for s in range(7)] == [lam_s * v for v in u_s]
        ok = ok and [sum(jac[s][b] * u_v[b] for b in range(7)) for s in range(7)] == [lam_v * v for v in u_v]
        shown.append(f"(rho {rho}, g {g}): scalar {lam_s}, vector {lam_v}")
    checks.check("E3", ok, "T5: with 'no record' among the possibilities the uniform field of density rho is a fixed point for z = rho/(6 (1-rho)(1+rho(g-1))^6), and the exact derivative of the seven-outcome map has the scalar (mass) eigenvalue rho (1-rho)(g-1)/(1+rho(g-1)) and the vector eigenvalue rho g l1/(1+rho(g-1)) per neighbour: " + "; ".join(shown) + ": at the neutral scale g = 1 the mass channel has no first-order strength")


# ============================================================================================ family H (T6)
def equilibrium(L, l, body):
    """u = 1 on the body, u_x = l (sum of the six neighbours) elsewhere; returns u and the charges (1 - l Adj) u on the body"""
    sites = list(product(range(L), repeat=3))
    nb = {s: [tuple((s[j] + (d if j == i else 0)) % L for j in range(3)) for i in range(3) for d in (1, -1)] for s in sites}
    free = [s for s in sites if s not in body]
    fi = {s: i for i, s in enumerate(free)}
    n = len(free)
    a = [[Fraction(0)] * n for _ in range(n)]
    rhs = [Fraction(0)] * n
    for s in free:
        i = fi[s]
        a[i][i] += 1
        for t in nb[s]:
            if t in body:
                rhs[i] += l
            else:
                a[i][fi[t]] -= l
    for c in range(n):
        piv = next(i for i in range(c, n) if a[i][c] != 0)
        a[c], a[piv] = a[piv], a[c]
        rhs[c], rhs[piv] = rhs[piv], rhs[c]
        inv = 1 / a[c][c]
        a[c] = [v * inv for v in a[c]]
        rhs[c] *= inv
        for i in range(n):
            if i != c and a[i][c] != 0:
                f = a[i][c]
                a[i] = [vi - f * vc for vi, vc in zip(a[i], a[c])]
                rhs[i] -= f * rhs[c]
    u = {s: Fraction(1) for s in body}
    u.update({s: rhs[fi[s]] for s in free})
    return u, {s: 1 - l * sum(u[t] for t in nb[s]) for s in body}


def family_h(checks: Checks) -> None:
    L = 5
    ok = True
    shown = []
    for l in (lam(5, 2, 4)[0], Fraction(19, 119)):                     # (5,2,4), and (29/10,1,2) next to the massless surface
        caps = {}
        fields = {}
        for side in (1, 2, 3):
            body = set(product(range(side), repeat=3))
            u, ch = equilibrium(L, l, body)
            caps[side] = sum(ch.values())
            fields[side] = u
            if side == 3:
                inner = ch[(1, 1, 1)]
                want = (1 - 5 * l) if mut("interior_charge_wrong") else (1 - 6 * l)
                ok = ok and inner == want and all(v >= inner for v in ch.values())
        per = [caps[side] / side ** 3 for side in (1, 2, 3)]
        ok = ok and per[0] > per[1] > per[2] and all(fields[2][x] <= fields[3][x] for x in fields[2])
        if mut("capacity_additive_injected"):
            ok = ok and caps[3] == 27 * caps[1]
        shown.append(f"l1 = {l}: capacity per record {', '.join(str(v.numerator * 1000 // v.denominator) for v in per)} thousandths for cubes of 1, 8, 27 records, interior charge {1 - 6 * l}")
    l = lam(5, 2, 4)[0]
    pa, pb = {(0, 0, 0)}, {(2, 0, 0)}
    ua, ca = equilibrium(L, l, pa)
    ub, cb = equilibrium(L, l, pb)
    uab, cab = equilibrium(L, l, pa | pb)
    ok = ok and all(uab[x] <= ua[x] + ub[x] for x in uab) and sum(cab.values()) < sum(ca.values()) + sum(cb.values())
    checks.check("H1", ok, "T6: on the 5^3 torus the field of a body of agreeing records (u = 1 on the body, the linear field equation off it) has the charge 1 - 6 l1 on a record surrounded by records and no smaller charge anywhere, a capacity per record that falls as the body grows, and is monotone and subadditive in the body: " + "; ".join(shown) + ": a record enters as a boundary value, and the source strength of a body is its capacity, not its number of records")


# ============================================================================================ family F
FENCES = (
    "This note works out a supplied reading, in which an unformed site carries its probability distribution and that distribution is a condition for its neighbours; the reading is not in the axioms memo and is not adopted.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Yukawa", "Ornstein", "Zernike", "Goldstone", "Casimir", "Gibbs", "Boltzmann", "Perron", "Frobenius", "Laplace", "Poisson", "Coulomb", "Waals", "Cauchy", "Schwarz", "Bayes", "Bernoulli", "Birkhoff", "Hopf", "Hilbert", "Helmholtz", "Bethe", "Weiss", "Banach", "Lagrange")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Yukawa)", 1)
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
    "per_element: executed — the gap weights for the three relations of two contents at n = 1..6; the 36 entries of the derivative of the odds map; the 24 rotations",
    "per_site: executed — all 16 arrangements of records on the plaquette; the field equation solved exactly at all 64 sites of the 4^3 torus",
    "per_mode: executed — the vector and quadrupole eigenvalues of K_1; cosine waves under the neighbour sum; the mode sum of the screened Green function",
    "per_block: executed — the contraction inequality on 1600 random and 20 adversarial exact pairs and the product bound on 200 exact cases; the seven-outcome derivative at four points (rho, g); the exact field, charges and capacity of cubes of 1, 8 and 27 records on the 5^3 torus at two strengths",
    "lattice_wide: T1 and the symmetry statement hold on every finite window; the linearization, its spectrum and the massless surface are exact on every torus; T3 proves existence, uniqueness and geometric decay for 6 (1 - kappa) < 1 on every graph of degree six; nothing is claimed about the nonlinear field on the massless surface or beyond it",
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
    family_h(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: records interacting through the odds of unformed sites — contents interact across empty sites, masses do not under exact summation; field equation, massless surface, proved screened regime, content as first-order charge, no first-order mass channel at the neutral scale, records as boundary values (capacity, not record count); exact")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
