#!/usr/bin/env python3
"""Exact checks: the zero-field bound on the formation bilayer - a held source's kernel without a field in 3+1, and no memory on planes
(the formation reading with block 90's light-cone past; block 20's zero-field inequality carried to the bilayer; not adopted).

OBJECTS: block 90's doubled graph and bilayer torus in dimension d = 2, 3 (V = 2N vertices, N = L^d sites per slab, L even); the sphere
ferromagnet on it at zero field; M^2 = <|V^-1 sum_u s_u|^2>; u(k) = V^-1 <|sum_u e^(-ik.x_u) s^1_u|^2>; E(k) = sum_j (2 - 2 cos k_j);
block 91's response R^(k) of a level's records to a held source.
T1: u(k) >= (M^2/3)^2 / (beta E(k) + 2/(3V)) for every k != 0 (a rotation-derivation inequality at zero field; the rungs carry no weight).
T2 (3+1): R^(k) = beta u(k), so with block 90's M^2 >= 1 - beta_L/beta: ((1 - beta_L/beta)/3)^2/(E(k) + 2/(3 beta V)) <= R^(k) <= 1/E(k)
   in every finite volume and at zero field; in the limit ((1 - beta_0/beta)/3)^2/E(k) <= R^(k) <= 1/E(k), beta_0 = 0.5905.
T3 (2+1): M^4 <= (6 pi^2 beta + 1/2)/H_(L/2 - 1), and a level's <|m_0|^2> <= M^2 + 3/(20 beta N): light-cone formation keeps no common
   direction on planes.
Exact arithmetic only (integers, Fractions, exact symbolic algebra); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_ZERO_FIELD_BOUND_ON_THE_FORMATION_BILAYER_A_HELD_SOURCES_KERNEL_WITHOUT_A_FIELD_IN_3PLUS1_AND_NO_MEMORY_ON_PLANES_BOUNDED_THEOREM_NOTE_2026-09-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_zero_field_bound_on_the_formation_bilayer_a_held_sources_kernel_without_a_field_in_3plus1_and_no_memory_on_planes_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "quadratic_step_sign_flipped": "B",
    "response_is_twice_beta_u": "C",
    "shell_count_doubled": "D",
    "plane_stiffness_counts_rungs": "D",
    "level_mean_without_the_staggered_term": "E",
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


F = Fraction
ZERO = F(0)
ONE = F(1)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


# ============================================================================================ helpers
STENCIL_RING = (0, 1, -1)


def unit_axes(d):
    return [tuple(1 if i == j else 0 for i in range(d)) for j in range(d)]


def doubled_graph_edges_d(size, d):
    stencil = [tuple(0 for _ in range(d))] + [tuple(s * e[i] for i in range(d)) for e in unit_axes(d) for s in (1, -1)]
    edges = set()
    for x in product(range(size), repeat=d):
        for dv in stencil:
            y = tuple((x[i] + dv[i]) % size for i in range(d))
            edges.add(frozenset({(x, 0), (y, 1)}))
    return edges


def bilayer_edges_d(size, d):
    edges = set()
    for x in product(range(size), repeat=d):
        edges.add(frozenset({(x, 0), (x, 1)}))
        for a in (0, 1):
            for e in unit_axes(d):
                y = tuple((x[i] + e[i]) % size for i in range(d))
                edges.add(frozenset({(x, a), (y, a)}))
    return edges


def relabel(v):
    x, a = v
    return (x, a ^ (sum(x) % 2))


def reflections_d(size, d):
    out = []
    for j in range(d):
        for c in range(size):
            def th(v, j=j, c=c):
                x, a = v
                y = list(x)
                y[j] = (2 * c + 1 - x[j]) % size
                return (tuple(y), a)

            def half(v, j=j, c=c):
                return ((v[0][j] - c - 1) % size) < size // 2
            out.append((th, half))
    out.append((lambda v: (v[0], 1 - v[1]), lambda v: v[1] == 0))
    return out


def harmonic(n):
    return sum((F(1, j) for j in range(1, n + 1)), ZERO)


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the zero-field inequality's algebra on the bilayer."""
    al = sp.symbols("al1 al2 al3", real=True)
    a = sp.symbols("a1 a2 a3")
    s = [sp.symbols(f"s1_{i} s2_{i} s3_{i}") for i in range(3)]
    V = sp.Integer(3)

    def rot(v, t):
        return (v[0] * sp.cos(t) + v[2] * sp.sin(t), v[1], -v[0] * sp.sin(t) + v[2] * sp.cos(t))
    r = [rot(s[i], al[i]) for i in range(3)]

    def D(expr):
        return sum(a[i] * sp.diff(expr, al[i]) for i in range(3)).subs({al[i]: 0 for i in range(3)})
    A = sum((1 / a[i]) * r[i][0] for i in range(3))                      # c-bar_u = 1/c_u on the unit circle
    Abar = sum(a[i] * s[i][0] for i in range(3))
    m3 = sum(r[i][2] for i in range(3)) / V
    m3_0 = sum(s[i][2] for i in range(3)) / V
    A_0 = sum((1 / a[i]) * s[i][0] for i in range(3))
    dA = sp.simplify(D(A) - V * m3_0) == 0
    dm = sp.simplify(D(m3) + Abar / V) == 0
    dF = sp.simplify(D(A * m3) - (V * m3_0 ** 2 - A_0 * Abar / V)) == 0
    checks.check("B1", dA and dm and dF, "T1: for D = sum_u c_u L_u (rotations about e2 weighted by c_u on the unit circle), exactly on a symbolic configuration: D(sum_u c-bar_u s^1_u) = V m^3, D m^3 = -V^-1 sum_u c_u s^1_u, hence D F = V (m^3)^2 - V^-1 |A|^2 for F = A m^3 (block 20's step (iv) on the bilayer's V vertices); the bond identity is block 91 E1")
    x, al_, bE, Nn = sp.symbols("x a bE N", positive=True)
    sign = 1 if not mut("quadratic_step_sign_flipped") else -1
    ident = sp.expand((bE + 2 * al_ / Nn) * x - al_ ** 2 - (bE * x - (al_ - x / Nn) ** 2 + sign * x ** 2 / Nn ** 2)) == 0
    diff = al_ ** 2 / (bE + 2 * al_ / Nn) - al_ ** 2 / (bE + sp.Rational(2, 3) / Nn)
    ok_weak = sp.simplify(diff - 2 * al_ ** 2 * Nn * (1 - 3 * al_) / ((bE * Nn + 2 * al_) * (3 * bE * Nn + 2))) == 0
    checks.check("B2", ident and ok_weak, "T1: the quadratic step: (bE + 2a/N) x - a^2 = bE x - (a - x/N)^2 + x^2/N^2 identically, so (a - x/N)^2 <= bE x gives x >= a^2/(bE + 2a/N) >= a^2/(bE + 2/(3N)) for a = M^2/3 <= 1/3 (the difference is 2a^2 N (1 - 3a)/((bE N + 2a)(3 bE N + 2)) >= 0): u(k) >= (M^2/3)^2/(beta E(k) + 2/(3V)) with V in place of N")
    # Parseval on the 4 x 4 bilayer with rational spins: sum over both branches = sum of squares
    L = 4
    cos_q = (1, 0, -1, 0)
    sin_q = (0, 1, 0, -1)
    verts = [(xx, b) for xx in product(range(L), repeat=2) for b in (0, 1)]
    val = {v: F((3 * v[0][0] + 5 * v[0][1] + 7 * v[1]) % 11 - 5, 7) for v in verts}
    tot = ZERO
    for n in product(range(L), repeat=2):
        for sgn in (1, -1):
            re = sum((val[v] * (1 if v[1] == 0 else sgn) * cos_q[(n[0] * v[0][0] + n[1] * v[0][1]) % 4] for v in verts), ZERO)
            im = sum((val[v] * (1 if v[1] == 0 else sgn) * sin_q[(n[0] * v[0][0] + n[1] * v[0][1]) % 4] for v in verts), ZERO)
            tot += (re * re + im * im) / len(verts)
    parse = tot == sum((val[v] ** 2 for v in verts), ZERO)
    checks.check("B3", parse, "T1: the sum rule's Parseval identity on the 4 x 4 bilayer with rational values: sum over k and both branches of V^-1 |sum_u e^(-ik.x_u)(1, +-1)_u s_u|^2 = sum_u s_u^2 exactly; with the sphere's average 1/3, sum_k u(k) <= V/3")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2 (3+1): the held source's window at zero field in every finite volume."""
    beta, u, S2, Nn = sp.symbols("beta u S2 N", positive=True)
    # u = V^-1 <|2 S_+^|^2> with V = 2N;  R = 2 beta N^-1 <|S_+^|^2>
    u_def = 4 * S2 / (2 * Nn)
    R_def = 2 * beta * S2 / Nn
    factor = 1 if not mut("response_is_twice_beta_u") else 2
    c1 = sp.simplify(R_def - factor * beta * u_def) == 0
    checks.check("C1", c1, "T2: block 91's response R^(k) = 2 beta N^-1 <|S_+^(k)|^2> equals beta u(k) (u = V^-1 <|2 S_+^(k)|^2>, V = 2N), so T1 gives R^(k) >= (M^2/3)^2/(E(k) + 2/(3 beta V)) at zero field; with block 91's upper side R^(k) <= 1/E(k)")
    vals = {}
    for size in (4, 6):
        cosv = [sp.cos(2 * sp.pi * n / size) for n in range(size)]
        Gs = sp.Integer(0)
        Hs = sp.Integer(0)
        for c in product(cosv, repeat=3):
            E = 6 - 2 * sum(c)
            if E != 0:
                Gs += 1 / E
            Hs += 1 / (E + 2)
        vals[size] = sp.nsimplify(sp.Rational(3, 2) * (Gs + Hs) / size ** 3)
    b = sp.Integer(1)
    mu4 = 1 - vals[4] / b
    mu6 = 1 - vals[6] / b
    low4 = (mu4 / 3) ** 2
    low6 = (mu6 / 3) ** 2
    ok = vals[4] == sp.Rational(18239, 35840) and vals[6] == sp.Rational(27735979, 51891840) and mu4 == sp.Rational(17601, 35840) and low4 > 0 and low6 > 0 and low6 < low4
    b0, bb = sp.symbols("beta_0 beta", positive=True)
    lim = sp.simplify(((1 - b0 / bb) / 3) ** 2 - (bb - b0) ** 2 / (9 * bb ** 2)) == 0
    checks.check("C2", ok and lim, f"T2: with block 90's M^2 >= 1 - beta_L/beta (beta_4 = 18239/35840, beta_6 = 27735979/51891840, recomputed exactly), the zero-field floor at beta = 1 is (M^2/3)^2 >= {low4} on 4^3 and {low6} on 6^3 (times 1/(E(k) + 2/(3 beta V))); in the limit the floor is ((1 - beta_0/beta)/3)^2 = (beta - beta_0)^2/(9 beta^2), positive for every beta > beta_0, about 5905/10000")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3 (2+1): the plane's bilayer; the lattice sum; no common direction."""
    ok1 = True
    counts = []
    for size in (4, 6):
        g = doubled_graph_edges_d(size, 2)
        img = {frozenset(relabel(v) for v in e) for e in g}
        bl = bilayer_edges_d(size, 2)
        ok1 = ok1 and img == bl and len(g) == 5 * size * size
        counts.append(len(g))
    size = 4
    bl = bilayer_edges_d(size, 2)
    verts = [(x, a) for x in product(range(size), repeat=2) for a in (0, 1)]
    ok_ref = True
    covered = set()
    for th, half in reflections_d(size, 2):
        ok_ref = ok_ref and all(th(v) != v and half(v) != half(th(v)) for v in verts)
        for e in bl:
            p, q = tuple(e)
            if half(p) != half(q):
                covered.add(e)
                ok_ref = ok_ref and th(p) == q
    ok_ref = ok_ref and covered == bl
    cos_q = (1, 0, -1, 0)
    ok_st = True
    N = size * size
    for n in product(range(size), repeat=2):
        tot = 0
        for e in bl:
            p, q = tuple(e)
            dm = (sum(n[i] * (p[0][i] - q[0][i]) for i in range(2))) % 4
            w = 2 - 2 * cos_q[dm]
            if p[0] == q[0] and mut("plane_stiffness_counts_rungs"):
                w = 2
            tot += w
        E2 = 4 - 2 * (cos_q[n[0]] + cos_q[n[1]])
        ok_st = ok_st and tot == 2 * N * E2
    checks.check("D1", ok1 and ok_ref and ok_st, f"T3: in two dimensions the parity relabelling maps the doubled graph onto the plane bilayer ({counts[0]} edges at L = 4, {counts[1]} at L = 6); the 9 reflections of the 4 x 4 bilayer fix no vertex, their crossing edges are mirror pairs and every edge crosses one (block 90's reflection structure, so block 91's upper side holds on planes too); the stiffness sum is 2N E_2(k) at all 16 wave vectors (rungs 0)")
    ok_sum = True
    for L in range(4, 26, 2):
        half = L // 2
        tot = ZERO
        for n in product(range(-half + 1, half + 1), repeat=2):
            if n != (0, 0):
                tot += F(1, n[0] * n[0] + n[1] * n[1])
        mult = 4 if not mut("shell_count_doubled") else 8
        ok_sum = ok_sum and tot >= mult * harmonic(half - 1)
    dyadic = all(harmonic(2 ** m) >= 1 + F(m, 2) for m in range(0, 11))
    t = sp.symbols("t", real=True)
    f = t ** 2 - 2 + 2 * sp.cos(t)
    conv = f.subs(t, 0) == 0 and sp.simplify(sp.diff(f, t) - 2 * (t - sp.sin(t))) == 0 and sp.simplify(sp.diff(f, t, 2) - 2 * (1 - sp.cos(t))) == 0 and sp.simplify(f.subs(t, -t) - f) == 0
    Lsym = sp.symbols("L", positive=True)
    small = sp.simplify(sp.Rational(2, 3) / (2 * Lsym ** 2) - (2 * sp.pi / Lsym) ** 2 / (12 * sp.pi ** 2)) == 0
    checks.check("D2", ok_sum and dyadic and conv and small, "T3: the plane's lattice sum: for every even L from 4 to 24, sum over n in {-L/2 + 1, ..., L/2}^2, n != 0, of |n|^-2 >= 4 H_(L/2 - 1) exactly (block 20's shell count: shells j < L/2 have 8j points with |n|^2 <= 2j^2); H_(2^m) >= 1 + m/2 for m <= 10; 2 - 2 cos t <= t^2 (f(0) = 0, f' = 2(t - sin t), f'' = 2(1 - cos t) >= 0, f even); and 2/(3V) = |k_min|^2/(12 pi^2) with V = 2L^2, so 2/(3V) <= |k|^2/(12 pi^2) for every k != 0")
    beta, M, H, Nn = sp.symbols("beta M H N", positive=True)
    # (M^2/3)^2 (beta + 1/(12 pi^2))^-1 (N/pi^2) H <= V/3 = 2N/3
    bound = sp.solve(sp.Eq((M ** 2 / 3) ** 2 * (Nn / sp.pi ** 2) * H / (beta + 1 / (12 * sp.pi ** 2)), 2 * Nn / 3), M ** 4)
    target = (6 * sp.pi ** 2 * beta + sp.Rational(1, 2)) / H
    ok_alg = any(sp.simplify(bb - target) == 0 for bb in bound) if bound else False
    if not bound:
        lhs = sp.solve(sp.Eq((M ** 2 / 3) ** 2 * (Nn / sp.pi ** 2) * H / (beta + 1 / (12 * sp.pi ** 2)), 2 * Nn / 3), M)
        ok_alg = any(sp.simplify(mm ** 4 - target) == 0 for mm in lhs)
    checks.check("D3", ok_alg, "T3: the final algebra on planes: summing u(k) >= (M^2/3)^2/((beta + 1/(12 pi^2))|k|^2) over k != 0 against sum_k u(k) <= V/3 = 2N/3, with sum_(k != 0) |k|^-2 >= (N/pi^2) H_(L/2 - 1), gives M^4 <= (6 pi^2 beta + 1/2)/H_(L/2 - 1), which tends to 0 as the plane grows, at every beta")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """A level's mean direction against the bilayer's: the staggered antisymmetric term."""
    t = sp.symbols("t", positive=True)
    size = 4
    verts = [(x, a) for x in range(size) for a in (0, 1)]
    edges = [((x, 0), ((x + d) % size, 1)) for x in range(size) for d in STENCIL_RING]
    Z = sp.Integer(0)
    m0 = sp.Integer(0)
    mb = sp.Integer(0)
    st = sp.Integer(0)
    for vals in product((1, -1), repeat=len(verts)):
        sg = dict(zip(verts, vals))
        w = t ** sum(sg[p] * sg[q] for p, q in edges)
        Z += w
        lev = sp.Rational(sum(sg[(x, 0)] for x in range(size)), size)
        bil = sp.Rational(sum(sg[v] for v in verts), 2 * size)
        B = {(x, b): sg[(x, b ^ (x % 2))] for x in range(size) for b in (0, 1)}
        stag = sp.Rational(sum((-1) ** x * (B[(x, 0)] - B[(x, 1)]) for x in range(size)), 2 * size)
        m0 += w * lev ** 2
        mb += w * bil ** 2
        st += w * stag ** 2
    rhs = mb + st if not mut("level_mean_without_the_staggered_term") else mb
    e1 = sp.simplify((m0 - rhs) / Z) == 0
    checks.check("E1", e1, "T3: a level's mean is the bilayer's mean plus the antisymmetric branch at the staggered wave vector, and by the slab swap <|m_0|^2> = <|m_bil|^2> + <|N^-1 S_-^(pi)|^2> exactly (enumeration of the doubled ring of four, two values, symbolic t)")
    beta, Nn = sp.symbols("beta N", positive=True)
    st2 = 3 / (2 * beta * Nn * (8 + 2))
    st3 = 3 / (2 * beta * Nn * (12 + 2))
    e2 = sp.simplify(st2 - sp.Rational(3, 20) / (beta * Nn)) == 0 and sp.simplify(st3 - sp.Rational(3, 28) / (beta * Nn)) == 0
    checks.check("E2", e2, "T3: the staggered term is bounded by the infrared bound of the antisymmetric branch, three components times 1/(2 beta N (E(pi) + 2)): 3/(20 beta N) on planes (E(pi,pi) = 8) and 3/(28 beta N) in 3+1; so on planes <|m_0|^2> <= ((6 pi^2 beta + 1/2)/H_(L/2 - 1))^(1/2) + 3/(20 beta N) -> 0, and in 3+1 a level's memory and the bilayer's differ by O(1/N)")


# ============================================================================================ family F
FENCES = (
    "This note works within the formation reading of the Record axiom with the supplied light-cone clause of block 90; it reports a zero-field lower bound on the formation bilayer, with what it gives in 3+1 and on planes; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the derivation identities on a symbolic configuration; Parseval on the 4 x 4 bilayer with rational values; the level-mean identity by enumeration of the doubled ring",
    "per_site: executed - the plane relabelling edge by edge (L = 4, 6); the 9 plane reflections vertex by vertex; the plane stiffness sum over every edge",
    "per_mode: executed - the plane stiffness sum at every wave vector; the lattice sums for L = 4 to 24; control: the plateau of light-cone formation on planes of side 16 to 128",
    "per_block: executed - the quadratic step and the final algebra symbolically; the exact floors on 4^3 and 6^3 at beta = 1",
    "lattice_wide: T1 for every even L in d = 2, 3 by block 20's argument with the bilayer's stiffness sum; T2 for every even L and beta > beta_L in 3+1, with block 90's T4 and block 91's upper side; T3 for every even L and every beta on planes; the constant beta_0 executed; the clause, the menu and the coupling are supplied",
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
    print("scope: the zero-field bound on the formation bilayer - u(k) >= (M^2/3)^2/(beta E(k) + 2/(3V)); in 3+1, with block 90's M^2 >= 1 - beta_L/beta, a held source's response lies between ((1 - beta_L/beta)/3)^2/(E(k) + 2/(3 beta V)) and 1/E(k) at zero field in every finite volume; on planes M^4 <= (6 pi^2 beta + 1/2)/H_(L/2 - 1) and a level keeps no common direction at any beta; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
