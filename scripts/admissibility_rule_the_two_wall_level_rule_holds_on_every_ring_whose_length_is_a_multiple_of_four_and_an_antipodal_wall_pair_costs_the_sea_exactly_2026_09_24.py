#!/usr/bin/env python3
"""Exact checks: block 87's two-wall level rule holds on every ring whose length is a multiple of four, for any strong and
weak bonds - two walls remove the band-edge levels and add 0 and the mean square of the bonds - so an antipodal wall pair
costs the sea exactly max(t_s, t_w) - sqrt((t_s^2 + t_w^2)/2); walls at any separation follow a Chebyshev formula; exact
zero modes occur iff the even and odd bond products agree; on rings of length 2 mod 4 the rule cannot hold (a harvest block
from a Grok-refereed probes attempt; block 87 as landed; not adopted).

B (T1): the two sublattice blocks, and the walls as two opposite diagonal defects.
C (T2): the ring lemma and the Chebyshev form.
D (T3): the four-level rule on every ring with 4 | L, and the wall pair's cost.
E (T4): exact zero modes, and the failure on rings of length 2 mod 4.
Exact arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_THE_TWO_WALL_LEVEL_RULE_HOLDS_ON_EVERY_RING_WHOSE_LENGTH_IS_A_MULTIPLE_OF_FOUR_AND_AN_ANTIPODAL_WALL_PAIR_COSTS_THE_SEA_EXACTLY_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_DEFECTS_OF_THE_ALTERNATION_ARE_SEPARABLE_WALLS_CARRY_SHEETS_OF_LOWER_MASS_LINES_LOWER_STILL_AND_THREE_CROSSING_WALLS_BIND_EXACT_ZERO_MODES_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/ADMISSIBILITY_RULE_WHAT_A_WALL_IN_THE_ALTERNATION_COSTS_THE_SEA_CHARGES_IT_BY_AN_EXACT_LEVEL_RULE_BLOCK_59S_COLLINEAR_COUPLING_REWARDS_IT_DOMAINS_IFF_ALPHA_LARGE_BOUNDED_THEOREM_NOTE_2026-09-22.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_two_wall_level_rule_holds_on_every_ring_whose_length_is_a_multiple_of_four_and_an_antipodal_wall_pair_costs_the_sea_exactly_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "wall_defect_forged": "B",
    "chebyshev_forged": "C",
    "level_rule_forged": "D",
    "zero_mode_forged": "E",
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
    note, axioms = texts[:2]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged (the alternation and its walls are supplied patterns of bond rates); Admissibility is not a dynamics axiom (the hop, the bond rates and the sea are supplied)")


# ============================================================================================ block 87's one-axis operator with two walls
LAM, ZZ, EPS = sp.symbols("lambda z epsilon")


def wall_bonds(ll, ts, tw):
    """bonds t_x, x = 0..L-1, alternating strong/weak with block 87's two walls: t_x = ts where s_x (-1)^x = +1, else tw,
    s_x = +1 for x < L/2 and -1 otherwise."""
    out = []
    for x in range(ll):
        s = 1 if x < ll // 2 else -1
        out.append(ts if s * (-1) ** x == 1 else tw)
    return out


def sub_block(bonds, parity):
    """one sublattice block of h^2 for block 87's h, read off h^2 directly (parity 0: even sites, 1: odd sites)."""
    hh = h_matrix(bonds)
    sq = (hh * hh).applyfunc(sp.expand)
    sites = list(range(parity, len(bonds), 2))
    return sq.extract(sites, sites)


def h_matrix(bonds):
    """block 87's h = (1/2i)(t T - T^T t), T[x, x+1] = 1, bond x -> x+1 carries t_x."""
    ll = len(bonds)
    mat = sp.zeros(ll, ll)
    for x in range(ll):
        y = (x + 1) % ll
        mat[x, y] += bonds[x] / (2 * sp.I)
        mat[y, x] += -bonds[x] / (2 * sp.I)
    return mat


def chebyshev_uv(n):
    tt = [sp.Integer(1), ZZ]
    uu = [sp.Integer(1), 2 * ZZ]
    for k in range(2, n + 1):
        tt.append(sp.expand(2 * ZZ * tt[-1] - tt[-2]))
        uu.append(sp.expand(2 * ZZ * uu[-1] - uu[-2]))
    return tt, uu


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the two sublattice chains are partners, and for 4 | L the walls are two opposite diagonal defects."""
    ok = True
    for ll in (4, 8, 12, 16):
        bonds = wall_bonds(ll, 1 + sp.Rational(3, 10), 1 - sp.Rational(3, 10))
        hh = h_matrix(bonds)
        sq = (hh * hh).applyfunc(sp.expand)
        evens, odds = list(range(0, ll, 2)), list(range(1, ll, 2))
        cross = all(sq[i, j] == 0 for i in evens for j in odds)
        je = sq.extract(evens, evens)
        jo = sq.extract(odds, odds)
        ok = ok and cross and sp.expand(je.charpoly(LAM).as_expr() - jo.charpoly(LAM).as_expr()) == 0
    ts, tw = sp.symbols("t_s t_w", positive=True)
    for ll in (8, 12, 16, 20, 24):
        bonds = wall_bonds(ll, ts, tw)
        je = sub_block(bonds, 0)
        m = ll // 2
        dd, cc, eta = (ts ** 2 + tw ** 2) / 4, ts * tw / 4, (ts ** 2 - tw ** 2) / 4
        want = sp.zeros(m, m)
        for i in range(m):
            want[i, i] = dd
            want[i, (i + 1) % m] += -cc
            want[(i + 1) % m, i] += -cc
        want[0, 0] += eta
        want[m // 2, m // 2] -= eta
        if mut("wall_defect_forged"):
            want[0, 0] += eta
        ok = ok and (je - want).applyfunc(sp.expand).is_zero_matrix
    checks.check("B1", ok,
                 "T1: on rings L = 4..16, h^2 of block 87's operator h = (1/2i)(t T - T^T t) splits into two sublattice blocks with equal characteristic polynomials (A A^dagger and A^dagger A); for 4 | L and symbolic strong and weak bonds (L = 8..24), the even block with block 87's two walls (at sites 0 and L/2) is the wall-free chain D - C(S + S^-1), D = (t_s^2 + t_w^2)/4, C = t_s t_w/4, plus +eta at the strong-strong wall and -eta at the weak-weak wall, eta = (t_s^2 - t_w^2)/4, the walls M/2 apart")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the ring lemma and the Chebyshev form of two opposite defects."""
    ok_lemma = True
    seed = 11
    for m in (3, 4, 5, 6, 7):
        a = []
        b = []
        for i in range(m):
            seed = (seed * 1103515245 + 12345) % 2147483648
            a.append(sp.Rational((seed >> 16) % 7 - 3, 2))
            seed = (seed * 1103515245 + 12345) % 2147483648
            b.append(sp.Rational((seed >> 16) % 5 + 1, 3))
        jm = sp.zeros(m, m)
        for i in range(m):
            jm[i, i] = a[i]
            jm[i, (i + 1) % m] += b[i]
            jm[(i + 1) % m, i] += b[i]
        prod = sp.eye(2)
        for i in range(m):
            ti = sp.Matrix([[(LAM - a[i]) / b[i], -b[(i - 1) % m] / b[i]], [1, 0]])
            prod = ti * prod
        lhs = jm.charpoly(LAM).as_expr()
        rhs = sp.prod(b) * (prod.trace() - 2)
        ok_lemma = ok_lemma and sp.expand(lhs - rhs) == 0
    tt, uu = chebyshev_uv(26)
    bm = sp.Matrix([[2 * ZZ, -1], [1, 0]])
    ok_pow = True
    pw = sp.eye(2)
    for k in range(1, 13):
        pw = (pw * bm).applyfunc(sp.expand)
        ok_pow = ok_pow and sp.expand(pw[0, 0] - uu[k]) == 0 and sp.expand(pw.trace() - 2 * tt[k]) == 0
    ok_two = True
    e11 = sp.Matrix([[1, 0], [0, 0]])
    for mm in range(3, 13):
        for r in range(1, mm):
            prod = (bm + EPS * e11) * bm ** (r - 1) * (bm - EPS * e11) * bm ** (mm - r - 1)
            val = sp.expand(prod.trace() - 2)
            want = sp.expand(2 * (tt[mm] - 1) - EPS ** 2 * uu[r - 1] * uu[mm - r - 1])
            if mut("chebyshev_forged"):
                want = sp.expand(2 * (tt[mm] - 1) - EPS ** 2 * uu[r] * uu[mm - r - 1])
            ok_two = ok_two and sp.expand(val - want) == 0
    checks.check("C1", ok_lemma and ok_pow and ok_two,
                 "T2: on rings of 3-7 sites with random rational diagonals and hops, det(lambda - J) = (prod b_i)(tr(T_(M-1) ... T_0) - 2) exactly; B = [[2z, -1], [1, 0]] has (B^k)_11 = U_k and tr B^k = 2 T_k (k <= 12); and two opposite diagonal defects +-eta = +-eps C, r sublattice sites apart on a ring of M (2r original-lattice sites), give 2(T_M - 1) - eps^2 U_(r-1) U_(M-r-1), symbolically for every M = 3..12 and every r")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the four-level rule on every ring with 4 | L, and the wall pair's cost to the sea."""
    ok = True
    for ts, tw in ((1 + sp.Rational(3, 10), 1 - sp.Rational(3, 10)), (sp.Rational(7, 4), sp.Rational(2, 5))):
        for ll in (4, 8, 12, 16, 20, 24):
            jw = sub_block(wall_bonds(ll, ts, tw), 0)
            j0 = sub_block([ts if x % 2 == 0 else tw for x in range(ll)], 0)
            lhs = sp.expand(jw.charpoly(LAM).as_expr() * (LAM - (ts - tw) ** 2 / 4) * (LAM - (ts + tw) ** 2 / 4))
            rhs = sp.expand(j0.charpoly(LAM).as_expr() * LAM * (LAM - (ts ** 2 + tw ** 2) / 2))
            if mut("level_rule_forged"):
                rhs = sp.expand(j0.charpoly(LAM).as_expr() * LAM * (LAM - (ts ** 2 + tw ** 2) / 4))
            ok = ok and lhs == rhs
    ts, tw, dl = sp.symbols("t_s t_w delta", positive=True)
    dd, cc, eta = (ts ** 2 + tw ** 2) / 4, ts * tw / 4, (ts ** 2 - tw ** 2) / 4
    ok_edges = sp.expand(dd ** 2 - 4 * cc ** 2 - eta ** 2) == 0 and sp.expand(dd - 2 * cc - (ts - tw) ** 2 / 4) == 0 and sp.expand(dd + 2 * cc - (ts + tw) ** 2 / 4) == 0
    logs = {ts: sp.exp(dl), tw: sp.exp(-dl)}
    ok_log = (sp.simplify(((ts - tw) ** 2 / 4).subs(logs) - sp.sinh(dl) ** 2) == 0 and sp.simplify(((ts + tw) ** 2 / 4).subs(logs) - sp.cosh(dl) ** 2) == 0
              and sp.simplify(((ts ** 2 + tw ** 2) / 2).subs(logs) - sp.cosh(2 * dl)) == 0)
    cost = (ts + tw) / 2 + (ts - tw) / 2 - sp.sqrt((ts ** 2 + tw ** 2) / 2)
    ok_cost = sp.simplify(cost.subs({ts: 1 + dl, tw: 1 - dl}) - ((1 + dl) - sp.sqrt(1 + dl ** 2))) == 0 and sp.simplify((ts ** 2 - ((ts ** 2 + tw ** 2) / 2)) - (ts ** 2 - tw ** 2) / 2) == 0
    checks.check("D1", ok and ok_edges and ok_log and ok_cost,
                 "T3: for every ring L = 4, 8, ..., 24 at (t_s, t_w) = (13/10, 7/10) and (7/4, 2/5), det(lambda - J_walls)(lambda - (t_s - t_w)^2/4)(lambda - (t_s + t_w)^2/4) = det(lambda - J_0) lambda (lambda - (t_s^2 + t_w^2)/2) exactly: two walls remove the band-edge levels and add 0 and (t_s^2 + t_w^2)/2, each twice in h^2; D^2 - 4C^2 = eta^2 symbolically; for t = e^(+-delta) the rule for magnitudes is abs(sinh), cosh -> 0, sqrt(cosh 2 delta); so an antipodal wall pair raises the sea's energy by exactly max(t_s, t_w) - sqrt((t_s^2 + t_w^2)/2) > 0, block 87's (1 + delta) - sqrt(1 + delta^2) at t = 1 +- delta, on every ring with 4 | L")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: exact zero modes iff the even and odd bond products agree; the rule fails when L = 2 mod 4."""
    ok_det = True
    seed = 5
    for ll in (6, 8, 10, 12):
        bonds = []
        for x in range(ll):
            seed = (seed * 1103515245 + 12345) % 2147483648
            bonds.append(sp.Rational((seed >> 16) % 4 + 1, 2))
        hh = h_matrix(bonds)
        evens, odds = list(range(0, ll, 2)), list(range(1, ll, 2))
        amat = hh.extract(evens, odds)
        m = ll // 2
        want = (sp.prod([bonds[x] for x in evens]) - sp.prod([bonds[x] for x in odds])) / (2 * sp.I) ** m
        if mut("zero_mode_forged"):
            want = (sp.prod([bonds[x] for x in evens]) + sp.prod([bonds[x] for x in odds])) / (2 * sp.I) ** m
        ok_det = ok_det and sp.simplify(amat.det() - want) == 0
    ts, tw = sp.Rational(13, 10), sp.Rational(7, 10)
    ok_anti = True
    for ll in (8, 12, 16):
        bonds = wall_bonds(ll, ts, tw)
        odd_p = sp.prod([bonds[x] for x in range(1, ll, 2)])
        even_p = sp.prod([bonds[x] for x in range(0, ll, 2)])
        ok_anti = ok_anti and odd_p == even_p and sub_block(bonds, 0).det() == 0
    ok_fail = True
    for ll in (6, 10):
        jw = sub_block(wall_bonds(ll, ts, tw), 0)
        j0 = sub_block([ts if x % 2 == 0 else tw for x in range(ll)], 0)
        g = sp.gcd(jw.charpoly(LAM).as_expr(), j0.charpoly(LAM).as_expr())
        edge_absent = sp.expand(j0.charpoly(LAM).as_expr().subs(LAM, (ts + tw) ** 2 / 4)) != 0
        ok_fail = ok_fail and sp.degree(g, LAM) == 0 and edge_absent
    checks.check("E1", ok_det and ok_anti and ok_fail,
                 "T4: for random rational bonds on rings of 6-12 sites the sublattice block has det A = (prod_even t - prod_odd t)/(2i)^M, so exact zero modes exist iff the two bond products agree, and then exactly two; block 87's antipodal walls on rings L = 8, 12, 16 balance them (a zero level of J_odd); on rings L = 6, 10 (L = 2 mod 4) no level of the wall-free ring survives the walls and (t_s + t_w)^2/4 is not a wall-free level, so the four-level rule cannot hold there")


# ============================================================================================ family F
FENCES = (
    "This note works within block 87 as landed on main (the one-axis hop with alternating bond rates and two walls, and the sea's energy as the sum of negative levels); it reports the exact change of the levels on every ring whose length is a multiple of four, and the wall pair's cost to the sea; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Chebyshev", "Sylvester", "Weinstein", "Aronszajn", "Peierls", "Jackiw", "Rebbi", "Su", "Schrieffer", "Heeger", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the sublattice blocks of h^2 and the walls as diagonal defects, symbolically in the two bonds, on rings L = 8..24",
    "per_site: executed - the ring determinant lemma on random rational rings of 3-7 sites; the powers of the transfer matrix",
    "per_mode: executed - the Chebyshev form of two opposite defects for every M = 3..12 and every separation",
    "per_block: executed - the four-level identity on rings L = 4..24 at two bond pairs; the determinant of the sublattice block; the rings of length 2 mod 4",
    "lattice_wide: T1-T3 for every ring with 4 | L by proof, checked through L = 24; T4 zero-mode criterion on even rings; the all-level-movement counterexamples are only the stated L=6,10 fixtures; one axis; the alternation, the walls and the sea supplied",
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
    print('scope: Two-wall transfer rule with small-ring exceptions and restricted failure examples. Supplied model only; no audit verdict.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
