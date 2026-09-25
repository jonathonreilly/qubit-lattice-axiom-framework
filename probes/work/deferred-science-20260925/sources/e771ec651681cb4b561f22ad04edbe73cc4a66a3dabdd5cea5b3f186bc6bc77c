#!/usr/bin/env python3
"""Exact checks: forward streaming on the 26 neighbours - an isotropic fourth-rank moment costs diagonal steps, the
shell-linear rules keep an anisotropic capture, every sign-compatible rule has the same diagonal so isotropy is one number
beta = 1/16, and constant-rate forward rules exist that capture isotropically (a harvest block from three Grok-refereed probes
attempts; blocks 44, 51 and 52 as landed supplied; not adopted).

B (T1): the shell-linear forward rules - the isotropy line, the mean step, the capture law.
C (T2): the universal diagonal of sign-compatible rules; beta = 1/16; no pointwise route.
D (T3): the staircase and axes-and-faces rules - forward, sign-compatible, constant total rate.
E (T4): stationarity of the uniform product measure for every rate function, with exchange.
Exact rational and symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_FORWARD_STREAMING_ON_THE_26_NEIGHBOURS_ISOTROPY_OF_THE_SECOND_ORDER_TERM_IS_ONE_NUMBER_AND_CONSTANT_RATE_RULES_CAPTURE_ISOTROPICALLY_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_forward_streaming_on_the_26_neighbours_isotropy_of_the_second_order_term_is_one_number_and_constant_rate_rules_capture_isotropically_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "A site never carries more than one record; records are permanent.",
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "isotropy_line_forged": "B",
    "diagonal_forged": "C",
    "staircase_weight_forged": "D",
    "exchange_dropped": "E",
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


Fr = Fraction


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: one record per site (exchange at an occupied target); each site has a domain of local possibilities (the content, read as the direction of travel); Admissibility is not a dynamics axiom (the streaming clause and its rates are supplied)")


# ============================================================================================ shared objects
HOPS = tuple((x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1) if (x, y, z) != (0, 0, 0))
S2, S3 = sp.sqrt(2), sp.sqrt(3)


def dec(q, n=6):
    """a truncated decimal string of a rational, by integer arithmetic."""
    sign = "-" if q < 0 else ""
    q = abs(q)
    whole = q.numerator // q.denominator
    frac = ((q - whole) * 10 ** n).numerator // ((q - whole) * 10 ** n).denominator
    return f"{sign}{whole}.{str(frac).zfill(n)}"


def zone_moments():
    """sphere moments by the zone lemma: t = s.n is uniform on [-1, 1] and the transverse part is uniform on a circle of radius
    sqrt(1 - t^2); so <|t|^3> = int_0^1 t^3 dt and <x^2 |t|> = int_0^1 t (1 - t^2)/2 dt, <x y |t|> = <x t |t|> = 0 by oddness."""
    t = sp.symbols("t", nonnegative=True)
    return sp.integrate(t ** 3, (t, 0, 1)), sp.integrate(t * (1 - t ** 2) / 2, (t, 0, 1))


def rational_sphere_points():
    """rational points of the unit sphere (inverse stereographic images) and all their images under the 48 signed permutations."""
    base = set()
    for u, v in ((Fr(1, 2), Fr(1, 3)), (Fr(2, 5), Fr(1, 7)), (Fr(3, 4), Fr(2, 3)), (Fr(1, 9), Fr(1, 11)), (Fr(5, 6), Fr(1, 5)), (Fr(1, 4), Fr(1, 4)), (Fr(2, 3), Fr(0)), (Fr(0), Fr(0))):
        den = 1 + u * u + v * v
        base.add((2 * u / den, 2 * v / den, (1 - u * u - v * v) / den))
    base |= {(Fr(1), Fr(0), Fr(0)), (Fr(3, 5), Fr(4, 5), Fr(0)), (Fr(2, 3), Fr(2, 3), Fr(1, 3)), (Fr(1, 3), Fr(2, 3), Fr(2, 3))}
    pts = set()
    for p in base:
        for perm in permutations(range(3)):
            for sg in product((1, -1), repeat=3):
                pts.add(tuple(sg[i] * p[perm[i]] for i in range(3)))
    return sorted(pts)


def staircase(s):
    """the barycentre (staircase) rule: weights on sign-compatible targets, mean s, total 1."""
    order = sorted(range(3), key=lambda m: (-abs(s[m]), m))
    i, j, k = order
    a, b, c = abs(s[i]), abs(s[j]), abs(s[k])
    u = [tuple((1 if s[m] >= 0 else -1) if m == n else 0 for m in range(3)) for n in range(3)]
    add3 = lambda *vs: tuple(sum(v[m] for v in vs) for m in range(3))
    t = Fr(0) if b + c == 0 else (1 - a) / (b + c)
    w = {}
    for d, x in ((u[i], (1 - t) * (a - b) + t * a), (u[j], t * b), (u[k], t * c), (add3(u[i], u[j]), (1 - t) * (b - c)), (add3(u[i], u[j], u[k]), (1 - t) * c)):
        if x != 0:
            w[d] = w.get(d, Fr(0)) + x
    return w, t


def axes_and_faces(s):
    """the maximal-merge rule on axes and face diagonals, scaled to total 1."""
    order = sorted(range(3), key=lambda m: (-abs(s[m]), m))
    i, j, k = order
    a, b, c = abs(s[i]), abs(s[j]), abs(s[k])
    u = [tuple((1 if s[m] >= 0 else -1) if m == n else 0 for m in range(3)) for n in range(3)]
    add3 = lambda *vs: tuple(sum(v[m] for v in vs) for m in range(3))
    if b + c == 0:
        return {u[i]: Fr(1)}
    if a >= b + c:
        z = (b, c, Fr(0))
    else:
        z = ((a + b - c) / 2, (a - b + c) / 2, (-a + b + c) / 2)
    theta = (a + b + c - 1) / sum(z)
    w = {}
    for d, x in ((u[i], a - theta * (z[0] + z[1])), (u[j], b - theta * (z[0] + z[2])), (u[k], c - theta * (z[1] + z[2])), (add3(u[i], u[j]), theta * z[0]), (add3(u[i], u[k]), theta * z[1]), (add3(u[j], u[k]), theta * z[2])):
        if x != 0:
            w[d] = w.get(d, Fr(0)) + x
    return w


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the shell-linear forward rules."""
    along, across = zone_moments()
    lemma = along == sp.Rational(1, 4) and across == sp.Rational(1, 8)
    l1, l2, l3 = sp.symbols("lambda1 lambda2 lambda3", positive=True)
    lam = {1: l1, 2: l2, 3: l3}
    dd = [sp.Matrix(d) for d in HOPS]
    shell = [sum(abs(x) for x in d) for d in HOPS]
    smat = sum((lam[shell[n]] * dd[n] * dd[n].T for n in range(26)), sp.zeros(3, 3))
    ok_s = sp.simplify(smat - (2 * l1 + 8 * l2 + 8 * l3) * sp.eye(3)) == sp.zeros(3, 3)

    def tens(i, j, k, l):
        tot = 0
        for n in range(26):
            d, nd = HOPS[n], shell[n]
            tot += lam[nd] * d[k] * d[l] * (sp.KroneckerDelta(i, j) + sp.Rational(d[i] * d[j], nd))
        return sp.expand(tot / 16)
    obstruction = sp.simplify(tens(0, 0, 0, 0) - tens(0, 0, 1, 1) - 2 * tens(0, 1, 0, 1))
    want = (l1 - l2 - sp.Rational(8, 3) * l3) / 8
    if mut("isotropy_line_forged"):
        want = (l1 - l2 - 3 * l3) / 8
    ok_line = sp.simplify(obstruction - want) == 0
    iso_ok = True
    sub = {l1: l2 + sp.Rational(8, 3) * l3}
    alpha = sp.simplify(tens(0, 0, 1, 1).subs(sub))
    beta = sp.simplify(tens(0, 1, 0, 1).subs(sub))
    for i, j, k, l in product(range(3), repeat=4):
        iso = alpha * sp.KroneckerDelta(i, j) * sp.KroneckerDelta(k, l) + beta * (sp.KroneckerDelta(i, k) * sp.KroneckerDelta(j, l) + sp.KroneckerDelta(i, l) * sp.KroneckerDelta(j, k))
        iso_ok = iso_ok and sp.simplify(tens(i, j, k, l).subs(sub) - iso) == 0
    b51 = [sp.simplify(tens(*ix).subs({l1: 1 / S3, l2: 0, l3: 0})) for ix in ((0, 0, 0, 0), (0, 0, 1, 1), (0, 1, 0, 1))]
    ok_b51 = sp.simplify(b51[0] - 1 / (4 * S3)) == 0 and sp.simplify(b51[1] - 1 / (8 * S3)) == 0 and b51[2] == 0
    kappa = l1 + 2 * S2 * l2 + 4 * l3 / S3
    ok_mean, ok_r = True, True

    def r_closed(s):
        x = [abs(v) for v in s]
        return (l1 * sum(x) + l2 * S2 * (sp.Max(x[0], x[1]) + sp.Max(x[0], x[2]) + sp.Max(x[1], x[2]))
                + l3 / S3 * sum(sp.Abs(s[0] + e1 * s[1] + e2 * s[2]) for e1 in (1, -1) for e2 in (1, -1)))
    for s in ((1, 0, 0), (sp.Rational(3, 5), sp.Rational(4, 5), 0), (sp.Rational(2, 3), sp.Rational(-2, 3), sp.Rational(1, 3)), (sp.Rational(2, 7), sp.Rational(3, 7), sp.Rational(-6, 7)), (1 / S3, 1 / S3, 1 / S3)):
        rates = [lam[shell[n]] * sp.Max(0, sum(s[m] * HOPS[n][m] for m in range(3)) / sp.sqrt(shell[n])) for n in range(26)]
        mean = [sp.simplify(sum(rates[n] * HOPS[n][m] for n in range(26))) for m in range(3)]
        ok_mean = ok_mean and all(sp.simplify(mean[m] - kappa * s[m]) == 0 for m in range(3))
        ok_r = ok_r and sp.simplify(sum(rates) - r_closed(s)) == 0
    diff = sp.simplify(r_closed((1 / S3, 1 / S3, 1 / S3)) - r_closed((1, 0, 0))).subs(l1, l2 + sp.Rational(8, 3) * l3)
    c2, c3 = sp.simplify(sp.expand(diff).coeff(l2)), sp.simplify(sp.expand(diff).coeff(l3))
    ok_cap = sp.simplify(c2 - (S3 + sp.sqrt(6) - 1 - 2 * S2)) == 0 and sp.simplify(c3 - (4 * S3 / 3 - sp.Rational(2, 3))) == 0 and c2 > 0 and c3 > 0
    xs = sp.symbols("x1:4", real=True)
    chi = 1 / sp.sqrt(sum(v ** 2 for v in xs))
    g = [sp.diff(chi, v) for v in xs]
    lap_g = [sp.simplify(sum(sp.diff(gi, v, 2) for v in xs)) for gi in g]
    div_g = sp.simplify(sum(sp.diff(g[m], xs[m]) for m in range(3)))
    ok_inflow = all(e == 0 for e in lap_g) and div_g == 0
    checks.check("B1", lemma and ok_s and ok_line and iso_ok and ok_b51,
                 f"T1(a): <s_i s_j |s.n|> = (delta_ij + n_i n_j)/8 (zone lemma: <|t|^3> = 1/4, <x^2 |t|> = 1/8); for the forward shell rule lambda_|d|^2 (s.d/|d|)_+ on the 26 neighbours the second moment is (2 l1 + 8 l2 + 8 l3) I and the only obstruction to an isotropic fourth-rank moment is T1111 - T1122 - 2 T1212 = (l1 - l2 - (8/3) l3)/8; on that line all 81 components are alpha dd + beta(dd + dd) with alpha = {alpha}, beta = {beta}; block 51's axis clause gives 1/(4 sqrt3), 1/(8 sqrt3), 0")
    checks.check("B2", ok_mean and ok_r and ok_cap and ok_inflow,
                 "T1(b): the mean step is kappa s, kappa = l1 + 2 sqrt2 l2 + 4 l3/sqrt3, at five directions (generic ones included); the total rate r(s) = l1 |s|_1 + l2 sqrt2 sum max(|s_i|,|s_j|) + (l3/sqrt3) sum |s1 +- s2 +- s3| matches the direct sum; on the isotropy line r(body) - r(axis) = (sqrt3 + sqrt6 - 1 - 2 sqrt2) l2 + (4 sqrt3/3 - 2/3) l3, both coefficients positive, so capture stays anisotropic; the potential inflow g = grad(1/r) has lap g = 0 and div g = 0, so the isotropic streaming term vanishes on it")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: sign-compatible rules - the universal diagonal and the one number beta."""
    m111, m112 = zone_moments()
    ok_mom = m111 == sp.Rational(1, 4) and m112 == sp.Rational(1, 8)
    ok_diag, pts = True, rational_sphere_points()
    for s in pts:
        for rule in (staircase(s)[0], axes_and_faces(s)):
            sign_ok = all((d[m] in (0, 1)) if s[m] > 0 else ((d[m] in (0, -1)) if s[m] < 0 else d[m] == 0) for d in rule for m in range(3))
            mm = [sum((w * d[m] * d[m] for d, w in rule.items()), Fr(0)) for m in range(3)]
            forced = [abs(s[m]) + (1 if mut("diagonal_forged") and m == 0 else 0) for m in range(3)]
            ok_diag = ok_diag and sign_ok and mm == forced
    a_, b_ = sp.symbols("a b", positive=True)
    m22 = a_ - (a_ + b_ - 1) / (a_ * b_) * (a_ ** 2 - b_ ** 2)
    ident = sp.simplify((m22 - b_ + (a_ - b_) * (1 - a_) * (1 - b_) / (a_ * b_)).subs(a_, sp.sqrt(1 - b_ ** 2)))
    arc_pts = [(Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(8, 17), Fr(15, 17)), (Fr(7, 25), Fr(24, 25))]
    ok_arc = ident == 0
    for p, q in arc_pts:
        a, b = max(p, q), min(p, q)
        ok_arc = ok_arc and -(a - b) * (1 - a) * (1 - b) / (a * b) < 0
    checks.check("C1", ok_mom and ok_diag,
                 f"T2(a),(b): on the 26 neighbours any rule with mean s has M_mm >= |s_m|, with equality iff it is sign-compatible; both constant-rate rules below have M_mm = |s_m| exactly at all {len(pts)} rational test contents (48 images each), so T1111 = <|s1|^3> = 1/4 and T1122 = <s1^2 |s2|> = 1/8 (exact) for every sign-compatible rule, and the fourth-rank moment is isotropic iff beta = T1212 = <|s1 s2| W12> = 1/16 (axis hops: beta = 0)")
    checks.check("C2", ok_arc,
                 "T2(c): no pointwise route - on the arc s = (a, b, 0), 0 < b < a, a forward rule of total rate 1 has M11 = a and M12 = a + b - 1, and M = alpha I + beta' s s^T would force M22 - b = -(a - b)(1 - a)(1 - b)/(ab) < 0 (identity on the arc, sign at four rational arc points), which is impossible since M22 >= b")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: forward rules with a constant total rate."""
    pts = rational_sphere_points()
    ok, ok_t, forward_only = True, True, True
    for s in pts:
        for rule in (staircase(s)[0], axes_and_faces(s)):
            total = sum(rule.values(), Fr(0))
            mean = [sum((w * d[m] for d, w in rule.items()), Fr(0)) for m in range(3)]
            if mut("staircase_weight_forged") and rule is not None and len(rule) > 2:
                total += Fr(1, 100)
            ok = ok and all(w >= 0 for w in rule.values()) and total == 1 and mean == list(s)
            forward_only = forward_only and all(sum(s[m] * d[m] for m in range(3)) > 0 for d in rule) and len(rule) <= 7
            neg = {tuple(-x for x in d): w for d, w in rule.items()}
            other = staircase(tuple(-x for x in s))[0] if rule == staircase(s)[0] else axes_and_faces(tuple(-x for x in s))
            ok = ok and neg == other
        w, t = staircase(s)
        order = sorted((abs(x) for x in s), reverse=True)
        ok_t = ok_t and 0 <= t <= 1 and t <= order[1] + order[2] + (1 if order[1] + order[2] == 0 else 0)
    ties = [(Fr(2, 3), Fr(2, 3), Fr(1, 3)), (Fr(1, 3), Fr(2, 3), Fr(2, 3)), (Fr(3, 5), Fr(4, 5), Fr(0)), (Fr(9, 11), Fr(6, 11), Fr(2, 11))]
    ok_tie = True
    for s in ties:
        for rule_fn in (lambda v: staircase(v)[0], axes_and_faces):
            base = rule_fn(s)
            for perm in permutations(range(3)):
                ps = tuple(s[perm[m]] for m in range(3))
                img = {tuple(d[perm[m]] for m in range(3)): x for d, x in base.items()}
                ok_tie = ok_tie and rule_fn(ps) == img
    checks.check("D1", ok and forward_only and ok_t,
                 f"T3(a): the staircase rule (1 - t)[(a-b) u_i + (b-c)(u_i+u_j) + c(u_i+u_j+u_k)] + t[a u_i + b u_j + c u_k], t = (1 - a)/(b + c), and the maximal-merge axes-and-faces rule have, at all {len(pts)} rational test contents: weights >= 0, total exactly 1, mean exactly s, every weighted target forward (s.d > 0), at most 7 targets, 0 <= t <= b + c, and a(-s, d) = a(s, -d)")
    checks.check("D2", ok_tie,
                 "T3(b): both rules are covariant under the permutations of the axes, including at ties (a = b, b = c, c = 0), so they are continuous on the sphere and cubic-covariant; with the total rate constant, a capturing site takes content s at rate rho r0 for every s (first order in the density), and the flux form of the far shadow is 1/(4 pi) per unit capture in every direction")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the uniform product measure is stationary for every rate function, with exchange."""
    rng_state = [987654321]

    def rnd(m):
        rng_state[0] = (rng_state[0] * 6364136223846793005 + 1442695040888963407) % (1 << 64)
        return (rng_state[0] >> 33) % m
    side = 3
    sites = [(x, y, z) for x in range(side) for y in range(side) for z in range(side)]

    def mv(x, d):
        return ((x[0] + d[0]) % side, (x[1] + d[1]) % side, (x[2] + d[2]) % side)

    def rates_for(contents):
        table = {}
        for s in contents:
            for d in HOPS:
                key = (s, d)
                partner = (tuple(-x for x in s), tuple(-x for x in d))
                if partner in table:
                    table[key] = table[partner]
                else:
                    table[key] = 1 + rnd(9)
        return table

    def census(n_rec, contents, solid, exchange=True):
        table = rates_for(contents)
        free = [x for x in sites if x not in solid]
        configs = []
        for pos in combinations(free, n_rec):
            for cs in product(contents, repeat=n_rec):
                configs.append(tuple(sorted(zip(pos, cs))))
        index = {c: i for i, c in enumerate(configs)}
        inflow = [0] * len(configs)
        outflow = [0] * len(configs)
        for c in configs:
            occ = dict(c)
            for x, s in c:
                for d in HOPS:
                    rate = table[(s, d)]
                    y = mv(x, d)
                    new = dict(occ)
                    if y in solid:
                        new[x] = tuple(-v for v in s)
                    elif y not in occ:
                        del new[x]
                        new[y] = s
                    elif exchange:
                        new[x], new[y] = occ[y], s
                    else:
                        continue
                    outflow[index[c]] += rate
                    inflow[index[tuple(sorted(new.items()))]] += rate
        bad = sum(1 for i in range(len(configs)) if inflow[i] != outflow[i])
        return len(configs), bad
    six = tuple(tuple((1 if m == n else 0) * sg for m in range(3)) for n in range(3) for sg in (1, -1))
    two = ((1, 0, 0), (-1, 0, 0))
    n1, bad1 = census(2, six, {(1, 1, 1)}, exchange=not mut("exchange_dropped"))
    n3, bad3 = census(3, two, set())
    n4, bad4 = census(2, two, set(), exchange=False)
    checks.check("E1", bad1 == 0 and bad3 == 0 and bad4 > 0,
                 f"T4: on the 3^3 torus with all 26 hop vectors, random positive integer rates with a(-s, d) = a(s, -d), and hop / exchange / reflection with the content reversed at a solid site: every configuration balances ({n1} with a solid site and 2 records of six contents, {n3} with 3 records of two contents), so the uniform product measure is stationary; with exchange suppressed {bad4} of {n4} configurations do not balance")


# ============================================================================================ family F
FENCES = (
    "This note works within the inertial streaming clause of blocks 44, 51 and 52, as landed on main, with the hop set enlarged to the 26 neighbours; it reports when forward streaming, a record moving only along its content, has an isotropic second-order term and an isotropic capture; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Frisch", "Hasslacher", "Pomeau", "Humières", "Lallemand", "Qian", "Archimedes", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Mach", "Eddington", "Soldner", "Dicke", "Riemann", "Regge", "Lame", "Hooke", "Abraham", "Arnowitt", "Deser", "Misner", "Brill", "Lindquist", "Isenberg", "Wilson", "Mathews", "Lichnerowicz", "York", "Hilbert", "Tolman", "Komar", "Friedmann", "Ricci",
                   "Christoffel", "Baierlein", "Wheeler", "Lagrange", "Jacobi", "Brans", "Nordtvedt")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Einstein)", 1)
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
    "per_element: executed - the zone moments <|t|^3> = 1/4 and <x^2 |t|> = 1/8; T for the forward shell rules, all 81 components, symbolic in the three rates",
    "per_site: executed - both constant-rate rules at every rational test content: weights, total, mean, forward, sign-compatible, the universal diagonal, a(-s, d) = a(s, -d)",
    "per_mode: executed - the mean step kappa s and the total rate r(s) at five contents; the potential inflow; the arc identity of the no-pointwise lemma",
    "per_block: executed - stationarity censuses on the 3^3 torus with all 26 hop vectors (11700 and 23400 configurations), and a failing census without exchange",
    "lattice_wide: T1-T4 for every content and every rate function as stated; the values of beta and the isotropic mixture are numerical only; the clause and its hop set are supplied",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


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
    print("scope: forward streaming on the 26 neighbours - shell rules isotropic at fourth rank on l1 = l2 + (8/3) l3 but with anisotropic capture; every sign-compatible rule has M_mm = |s_m|, so isotropy is beta = 1/16; staircase and axes-and-faces rules have constant total rate; stationarity for every rate function with exchange; the isotropy of the mixture numerical; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
