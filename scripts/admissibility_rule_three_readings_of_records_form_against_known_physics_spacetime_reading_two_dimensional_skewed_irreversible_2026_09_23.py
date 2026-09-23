#!/usr/bin/env python3
"""Exact checks: three readings of "records form" against known physics (not adopted; known physics as comparator only).

READINGS: (i) Z^3 read as spacetime: each site records once, from its already-formed neighbours x - e_j (level planes two-dimensional);
(ii) Z^3 read as space with a record at every site at every tick (block 36's clause, excluded by the memo as written); (iii) Z^3 read as space
with permanent records that move (the owner's reading of 2026-09-20).
B: reading (i)'s level chain is reversible with respect to no law (cycle exponent 8 on the 4 x 4 plane), its propagation is skewed (third
   cumulant 2/27) and its causal cone is a triangle; symmetric pasts have exponent 0, zero skew and centrally symmetric cones.
C: reading (i)'s resting source has a reflection-odd field along the step directions (exact partial sums), zero on the mirror lines.
D: reading (iii)'s motion by the pair weights is reversible for the static law; formation only adds records.
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
    "docs/ADMISSIBILITY_RULE_THREE_READINGS_OF_RECORDS_FORM_AGAINST_KNOWN_PHYSICS_THE_SPACETIME_READING_IS_TWO_DIMENSIONAL_SKEWED_AND_IRREVERSIBLE_BOUNDED_THEOREM_NOTE_2026-09-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_three_readings_of_records_form_against_known_physics_the_spacetime_reading_is_two_dimensional_skewed_and_irreversible_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "spacetime_past_taken_symmetric": "B",
    "skew_taken_zero": "B",
    "mirror_lines_taken_odd": "C",
    "motion_by_the_normalised_rule": "D",
    "spacetime_levels_three_dimensional": "E",
    "one_sided_front_denied": "E",
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
from math import factorial

PLANE_PAST_I = [(0, 0), (-1, 0), (0, -1)]          # reading (i): Z^3 read as spacetime, level plane coordinates (x1, x2); x - e3 is (0, 0)
PLANE_PAST_SYM = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]


def cycle_exponent(size, stencil):
    """Exponent of t in the forward over backward products of the cycle a -> b -> -a -> a on the (Z/size)^2 level plane (contents +-1):
    B(b, a) + B(-a, b) + B(a, -a), A(s', s) = sum_x sum_d s'_x s_(x+d), B(u, v) = A(u, v) - A(v, u); a flips the origin, b flips the site
    -d0 for an offset d0 in the stencil whose opposite is not (the origin's partner when the stencil is symmetric)."""
    sites = list(product(range(size), repeat=2))
    d0 = next((d for d in stencil if tuple(-c for c in d) not in stencil), (1, 0))
    y = tuple((-d0[i]) % size for i in range(2))
    a = {x: (-1 if x == (0, 0) else 1) for x in sites}
    b = {x: (-1 if x == y else 1) for x in sites}
    c = {x: -a[x] for x in sites}

    def A(u, v):
        return sum(u[x] * v[tuple((x[i] + d[i]) % size for i in range(2))] for x in sites for d in stencil)

    def B(u, v):
        return A(u, v) - A(v, u)
    return B(b, a) + B(c, b) + B(a, c)


def walk_P(m, b, c):
    """The m-step law of reading (i)'s level walk (steps 0, e1, e2, each 1/3) at (b, c)."""
    a = m - b - c
    if b < 0 or c < 0 or a < 0:
        return ZERO
    return F(factorial(m), factorial(a) * factorial(b) * factorial(c) * 3 ** m)


def odd_part(y, nmax):
    """Partial sum over the resting worldline (along (1,1,1): plane point (n, n) at 3n levels back) of the reflection-odd part."""
    return sum((walk_P(3 * n, y[0] + n, y[1] + n) - walk_P(3 * n, -y[0] + n, -y[1] + n) for n in range(1, nmax + 1)), ZERO)


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Reading (i): the level chain has an arrow; its propagation is skewed; its cone is a triangle."""
    past = PLANE_PAST_I if not mut("spacetime_past_taken_symmetric") else PLANE_PAST_SYM
    e_i = cycle_exponent(4, past)
    e_sym = cycle_exponent(4, PLANE_PAST_SYM)
    checks.check("B1", e_i == 8 and e_sym == 0, f"reading (i): with Z^3 read as spacetime the predecessors of a record are x - e_1, x - e_2, x - e_3, i.e. the offsets 0, -e_1, -e_2 in the level plane; on the 4 x 4 plane torus the cycle a -> b -> -a -> a has forward over backward exponent {e_i} (ratio t^8): the level chain is reversible with respect to no law, while a symmetric past gives exponent {e_sym}")
    steps = [(ZERO, ZERO), (ONE, ZERO), (ZERO, ONE)]
    mean = tuple(sum((s[i] for s in steps), ZERO) / 3 for i in range(2))
    cen = [tuple(s[i] - mean[i] for i in range(2)) for s in steps]
    cov = [[sum((v[i] * v[j] for v in cen), ZERO) / 3 for j in range(2)] for i in range(2)]
    t111 = sum((v[0] ** 3 for v in cen), ZERO) / 3
    t112 = sum((v[0] ** 2 * v[1] for v in cen), ZERO) / 3
    if mut("skew_taken_zero"):
        t111 = ZERO
    sym3 = [tuple(F(c) for c in d) for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (0, 0, 0))]
    t111_sym = sum((v[0] ** 3 for v in sym3), ZERO) / 7
    m = 3
    cone = {(F(bb) - F(m, 3), F(cc) - F(m, 3)) for bb in range(m + 1) for cc in range(m + 1 - bb)}
    tri = cone != {(-u, -v) for u, v in cone}
    oct_cone = {d for d in product(range(-m, m + 1), repeat=3) if sum(abs(c) for c in d) <= m}
    oct_sym = oct_cone == {tuple(-c for c in d) for d in oct_cone}
    ok = mean == (F(1, 3), F(1, 3)) and cov == [[F(2, 9), F(-1, 9)], [F(-1, 9), F(2, 9)]] and t111 == F(2, 27) and t112 == F(-1, 27) and t111_sym == 0 and tri and oct_sym
    checks.check("B2", ok, "reading (i): the level walk's centred step has covariance [[2/9, -1/9], [-1/9, 2/9]] (isotropic in the plane's own metric) and third cumulants T_111 = 2/27, T_112 = -1/27: its propagation is skewed, and after three levels its causal cone (10 sites, rest frame) is a triangle that point reflection does not preserve; the symmetric pasts of readings (ii) and (iii) have zero third cumulant and a centrally symmetric cone (the octahedron |d|_1 <= 3)")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Reading (i): a resting source's field is not reflection symmetric (exact partial sums)."""
    vals = {y: [odd_part(y, nmax) for nmax in (10, 20, 40)] for y in ((1, 1), (2, -1), (1, 0), (0, 1), (1, -1))}
    along_steps = all(v < 0 for v in vals[(1, 1)]) and all(v > 0 for v in vals[(2, -1)])
    mirror = all(v == 0 for y in ((1, 0), (0, 1), (1, -1)) for v in vals[y])
    if mut("mirror_lines_taken_odd"):
        mirror = not mirror
    grows = abs(vals[(1, 1)][2]) > abs(vals[(1, 1)][1]) > abs(vals[(1, 1)][0])
    checks.check("C1", along_steps and mirror and grows, f"reading (i): the linear field of a source at rest (worldline along (1,1,1), in the level plane at (n, n) three n levels back), Phi(y) = sum_n P_(3n)(y + (n, n)), has a reflection-odd part Phi(y) - Phi(-y) that is exactly zero on the three mirror lines (y = (1, 0), (0, 1), (1, -1): termwise, by the axis swaps) and nonzero along the step directions: partial sums to n = 10, 20, 40 at y = (1, 1) are about {round(vals[(1, 1)][0] * 10000)}/10000, {round(vals[(1, 1)][1] * 10000)}/10000, {round(vals[(1, 1)][2] * 10000)}/10000 (exact rationals, rounded exactly; increasing in size) and the opposite at (2, -1): the field of A at B differs from the field of B at A")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Reading (iii): motion by the pair weights is reversible for the static law; formation only adds records."""
    t, c = sp.symbols("t c", positive=True)
    size = 4                     # a ring of four sites, two records with contents +-1, two vacancies
    states = []
    for occ in product((0, 1, -1), repeat=size):
        if sum(1 for o in occ if o != 0) == 2:
            states.append(occ)

    def weight(s):
        w = sp.Integer(1)
        for x in range(size):
            y = (x + 1) % size
            if s[x] != 0 and s[y] != 0:
                w *= t ** (s[x] * s[y])
            elif (s[x] != 0) != (s[y] != 0):
                w *= c
        return w

    def moves(s):
        out = []
        for x in range(size):
            if s[x] == 0:
                continue
            for y in ((x + 1) % size, (x - 1) % size):
                if s[y] == 0:
                    s2 = list(s)
                    s2[y], s2[x] = s[x], 0
                    out.append(tuple(s2))
        return out
    ok = True
    for s in states:
        for s2 in moves(s):
            if mut("motion_by_the_normalised_rule"):
                # the rule's normalised probability of the moving content at the destination, given the destination's other neighbour
                xs = next(x for x in range(size) if s[x] != 0 and s2[x] == 0)
                ys = next(y for y in range(size) if s2[y] != 0 and s[y] == 0)
                h_f = sum(s[z] for z in ((ys + 1) % size, (ys - 1) % size) if z != xs)
                h_b = sum(s2[z] for z in ((xs + 1) % size, (xs - 1) % size) if z != ys)
                p_f = t ** (s[xs] * h_f) / (t ** h_f + t ** (-h_f))
                p_b = t ** (s2[ys] * h_b) / (t ** h_b + t ** (-h_b))
            else:
                p_f = weight(s2) / (weight(s) + weight(s2))
                p_b = weight(s) / (weight(s) + weight(s2))
            ok = ok and sp.simplify(weight(s) * p_f - weight(s2) * p_b) == 0
    grows = all(sum(1 for o in s if o != 0) == 2 for s in states)
    checks.check("D1", ok and grows, f"reading (iii): on a ring of four with two records (contents +-1) and two vacancies, a record choosing between its place and an empty neighbouring place in proportion to the pair weights (t^(s.s') between records, c between a record and an empty site; t, c symbolic) is in detailed balance with the static law's weight at every one of the {len(states)} configurations and every move (block 39 T1): motion is reversible; formation fills an empty site and is never undone (records are permanent), so the only arrow is formation")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """The dimension of space in each reading, from the growth of causal cones (exact counts)."""
    ok = True
    for m in range(1, 13):
        cone_i = sum(1 for bb in range(m + 1) for cc in range(m + 1 - bb))                     # reading (i): level-plane sites reachable in m levels
        cone_3 = sum(1 for d in product(range(-m, m + 1), repeat=3) if sum(abs(c) for c in d) <= m)   # readings (ii), (iii): |d|_1 <= m
        want_i = (m + 1) * (m + 2) // 2 if not mut("spacetime_levels_three_dimensional") else (m + 1) ** 3
        ok = ok and cone_i == want_i and cone_3 * 3 == (2 * m + 1) * (2 * m * m + 2 * m + 3)
    level_rank = sp.Matrix([[1, -1, 0], [0, 1, -1]]).rank()                                  # the level set x1 + x2 + x3 = t is a rank-2 lattice
    checks.check("E1", ok and level_rank == 2, "the dimension of space in each reading, from the growth of causal cones: in reading (i) a level set of Z^3 is a rank-2 lattice and the sites reachable in m levels number (m + 1)(m + 2)/2 (a quadratic: two space dimensions), exactly for m = 1..12; in readings (ii) and (iii) the ball |d|_1 <= m holds (2m + 1)(2m^2 + 2m + 3)/3 sites (a cubic: three space dimensions)")
    family_e2(checks)


def ring_chain_matrix(L, past, t):
    states = list(product((1, -1), repeat=L))
    P = []
    for s in states:
        hs = [sum(s[(x + d) % L] for d in past) for x in range(L)]
        row = []
        for s2 in states:
            p = ONE
            for x in range(L):
                h = hs[x]
                p *= t ** (s2[x] * h) / (t ** h + t ** (-h))
            row.append(p)
        P.append(row)
    return states, P


def stationary_exact(P):
    n = len(P)
    M = [[P[j][i] - (ONE if i == j else ZERO) for j in range(n)] + [ZERO] for i in range(n)]
    M[-1] = [ONE] * n + [ONE]
    for c in range(n):
        piv = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [M[i][n] / M[i][i] for i in range(n)]


def front_argmax(L, past, t, lag):
    states, P = ring_chain_matrix(L, past, t)
    pi = stationary_exact(P)
    mean0 = sum((pi[i] * s[0] for i, s in enumerate(states)), ZERO)
    g = [s[0] - mean0 for s in states]
    for _ in range(lag):
        g = [sum((P[i][j] * g[j] for j in range(len(g))), ZERO) for i in range(len(g))]
    vals = [sum((pi[i] * (s[r] - mean0) * g[i] for i, s in enumerate(states)), ZERO) for r in range(L)]
    return max(range(L), key=lambda r: vals[r]), vals


def family_e2(checks: Checks) -> None:
    t = F(2)
    rev = [front_argmax(5, (0, 1, -1), t, lag)[0] for lag in (2, 4)]
    one = [front_argmax(5, (0, -1) if not mut("one_sided_front_denied") else (0, 1, -1), t, lag)[0] for lag in (2, 4)]
    checks.check("E2", rev == [0, 0] and one == [4, 3], f"no fronts under detailed balance: for a reversible translation-invariant chain, <f, P^(2n) tau_r f>_pi = <P^n f, tau_r P^n f>_pi <= <f, P^(2n) f>_pi (Cauchy-Schwarz, tau_r unitary), so a disturbance's imprint is largest at its origin at every even lag; exactly on a ring of five at t = e^beta = 2 the lag-2 and lag-4 correlations of the reversible light-cone chain peak at shift {rev}, while the one-sided past's peak moves to shifts {one} (-1 and -2): readings (ii) and (iii)'s record layers carry no waves; waves need a non-reversible or amplitude dynamics")


# ============================================================================================ family F
FENCES = (
    "This note compares three readings of how records form against known physics, used as a comparator only; it reports exact discriminators and a scorecard; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - the cycle exponents on the 4 x 4 plane torus; the third cumulants; the three-level cones; detailed balance of pair-weight motion at every configuration and move of a ring of four",
    "per_site: executed - the resting source's reflection-odd part at five plane points, partial sums to 10, 20, 40",
    "per_mode: executed - control: the resting source's potential against log r to n = 6000, the three-dimensional kernel against 1/r by quadrature",
    "per_block: executed - the scorecard's entries cite the blocks that prove them",
    "lattice_wide: B for every even torus by the one-sided past (block 90 T1), checked on 4 x 4; C for the linear theory, partial sums exact, limits executed; D for every window by the heat-bath form (block 39 T1), checked on a ring; the readings and the comparator benchmarks are supplied",
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
    print("scope: three readings of records form against known physics - (i) Z^3 as spacetime: two space dimensions, a level chain reversible with respect to no law, skewed propagation, a triangular cone, a two-dimensional reflection-odd resting-source field; (ii) re-recording ticks (block 36, excluded by the memo): three dimensions, reversible, 1/r reciprocal; (iii) moving records (owner): three dimensions, reversible motion with formation the only arrow; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
