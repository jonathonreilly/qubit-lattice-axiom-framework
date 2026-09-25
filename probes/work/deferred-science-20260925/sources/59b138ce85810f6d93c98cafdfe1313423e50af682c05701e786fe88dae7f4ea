#!/usr/bin/env python3
"""Exact checks: one record per site, and no possibility shift among neighbours restores the books - for two records of
block 54's walk under block 78's compression, with any coin term acting on neighbouring records (a general Hermitian matrix on
the pair's two coins, one per axis, its energy anywhere on the bond's line), the defect of the total energy current has entries
that involve none of the term's unknowns and are nonzero, on Z^2 and Z^3 and for either exchange sign (the supervisor's own
derivation; blocks 54 and 78 as landed; blocks 121 and 137 placed; not adopted).

B (T1): Z^2, 32 unknowns, both signs.
C (T2): Z^3, 48 unknowns, both signs.
D (T3): controls; the witness; the placement.
E (T4): the line has nothing to repair.
Exact symbolic and Gaussian-rational arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_NO_POSSIBILITY_SHIFT_AMONG_NEIGHBOURS_RESTORES_THE_BOOKS_NO_NEIGHBOUR_COIN_TERM_KEEPS_TWO_EXCLUDED_RECORDS_ENERGY_CURRENT_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_one_record_per_site_no_possibility_shift_among_neighbours_restores_the_books_no_neighbour_coin_term_keeps_two_excluded_records_energy_current_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "exclusion_lifted_in_2d": "B",
    "third_dimension_witness_forged": "C",
    "control_excluded_forged": "D",
    "line_obstruction_forged": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its exclusion, the currents and their placements, the member and the source link are supplied; the memo does not define a time metric)")


# ============================================================================================ two records with a neighbour coin term, symbolic over Q(i)
PAULI4 = (sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]]))


class NeighbourPair:
    """two records of block 54's walk H = sum_{a < dim} sigma_a S_a on the open Z^dim, (anti)symmetric, with or without
    block 78's exclusion, plus V = sum over neighbouring pairs along axis a of M_a acting on the pair's two coins (the lower
    record first), each M_a = sum_bc c_{a,b,c} sigma_b x sigma_c with its own sixteen real unknowns; V's energy sits at the
    pair's midpoint."""

    def __init__(self, dim, sign, excl, symbolic=True, values=None):
        self.dim, self.sign, self.excl = dim, sign, excl
        self.cs = sp.symbols("c0:%d" % (16 * dim), real=True)
        self.M = []
        for a in range(dim):
            m = sp.zeros(4, 4)
            for b in range(4):
                for c in range(4):
                    sym = self.cs[16 * a + 4 * b + c]
                    coef = sym if symbolic else (values[16 * a + 4 * b + c] if values is not None else 0)
                    m += coef * sp.kronecker_product(PAULI4[b], PAULI4[c])
            self.M.append(m)

    def h1(self, s):
        x, cc = s
        out = []
        for a in range(self.dim):
            for sg in (1, -1):
                y = list(x)
                y[a] -= sg
                y = tuple(y)
                for d in (0, 1):
                    v = PAULI4[a + 1][d, cc]
                    if v != 0:
                        out.append(((y, d), -sp.I * sg * v / 2))
        return out

    def canon(self, s1, s2):
        if s1 == s2:
            return None, None
        if s1 < s2:
            return (s1, s2), 1
        return (s2, s1), self.sign

    @staticmethod
    def vadd(v, key, a):
        nv = sp.expand(v.get(key, 0) + a)
        if nv == 0:
            v.pop(key, None)
        else:
            v[key] = nv

    def proj(self, v):
        if not self.excl:
            return v
        return {key: a for key, a in v.items() if key[0][0] != key[1][0]}

    def axis(self, x, y):
        d = [y[i] - x[i] for i in range(self.dim)]
        if sum(abs(t) for t in d) != 1:
            return None
        return [i for i in range(self.dim) if d[i] != 0][0]

    def vterm(self, v, weight=None):
        out = {}
        for (s1, s2), amp in v.items():
            x1, c1 = s1
            x2, c2 = s2
            ax = self.axis(x1, x2)
            if ax is None:
                continue
            if x1[ax] < x2[ax]:
                lo, hi, clo, chi, flip = x1, x2, c1, c2, False
            else:
                lo, hi, clo, chi, flip = x2, x1, c2, c1, True
            col = 2 * clo + chi
            for row in range(4):
                m = self.M[ax][row, col]
                if m == 0:
                    continue
                key, sg = self.canon((lo, row // 2), (hi, row % 2))
                if not key:
                    continue
                pre = self.sign if flip else 1
                w = 1 if weight is None else weight(lo, hi)
                self.vadd(out, key, amp * m * sg * pre * w)
        return out

    def hop(self, v, weight=None):
        out = {}
        for (s1, s2), a in v.items():
            for t, amp in self.h1(s1):
                key, sg = self.canon(t, s2)
                if key:
                    w = amp if weight is None else amp * weight(t, s1)
                    self.vadd(out, key, a * w * sg)
            for t, amp in self.h1(s2):
                key, sg = self.canon(s1, t)
                if key:
                    w = amp if weight is None else amp * weight(t, s2)
                    self.vadd(out, key, a * w * sg)
        return out

    def add(self, *vs):
        out = {}
        for v in vs:
            for key, a in v.items():
                self.vadd(out, key, a)
        return out

    @staticmethod
    def scale(v, s):
        return {key: sp.expand(a * s) for key, a in v.items()}

    def H2(self, v):
        pv = self.proj(v)
        return self.add(self.proj(self.hop(pv)), self.vterm(pv))

    def D2(self, v, comp):
        pv = self.proj(v)
        a = self.proj(self.hop(pv, lambda t, s: sp.Rational(t[0][comp] + s[0][comp], 2)))
        b = self.vterm(pv, lambda lo, hi: sp.Rational(lo[comp] + hi[comp], 2))
        return self.add(a, b)

    def J(self, v, comp):
        return self.scale(self.add(self.H2(self.D2(v, comp)), self.scale(self.D2(self.H2(v), comp), -1)), sp.I)

    def defect(self, v, comp):
        return self.add(self.H2(self.J(v, comp)), self.scale(self.J(self.H2(v), comp), -1))


def test_pairs(p):
    o = tuple([0] * p.dim)

    def e(*c):
        return tuple(list(c) + [0] * (p.dim - len(c)))
    seconds = [e(1), e(0, 1), e(1, 1), e(2)] if p.dim == 2 else [e(1), e(1, 1), e(2)]
    out = []
    for pos2 in seconds:
        for c1 in (0, 1):
            for c2 in (0, 1):
                key, sg = p.canon((o, c1), (pos2, c2))
                if key:
                    out.append({key: sg})
    return out


def v_free_entries(p):
    """the defect's entries that involve none of the unknowns and are nonzero"""
    free = []
    for v in test_pairs(p):
        for comp in range(p.dim):
            for key, val in p.defect(v, comp).items():
                if not val.free_symbols and val != 0:
                    free.append((key, val))
    return free


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: on Z^2 no neighbour coin term keeps the total energy current of two excluded records."""
    excl = not mut("exclusion_lifted_in_2d")
    counts = []
    for sign in (-1, 1):
        counts.append(len(v_free_entries(NeighbourPair(2, sign, excl))))
    checks.check("B1", all(c > 0 for c in counts),
                 "T1: on Z^2, for two records under one record per site with either exchange sign, and V any neighbour coin term (a general Hermitian 4 x 4 matrix on the two coins of each neighbouring pair, one per axis, 32 real unknowns, its energy at the pair's midpoint), the defect [H2 + V, J] v of the total energy current has entries that involve none of the unknowns and are nonzero (%s and %s such entries over the test pairs and components for the two signs), so no neighbour coin term keeps the current" % (counts[0], counts[1]))


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the same on Z^3."""
    counts = []
    for sign in (-1, 1):
        counts.append(len(v_free_entries(NeighbourPair(3, sign, True))))
    if mut("third_dimension_witness_forged"):
        counts[0] = 0
    checks.check("C1", all(c > 0 for c in counts),
                 "T2: on Z^3 with 48 real unknowns (a general coin matrix per axis), for either exchange sign, the defect again has entries free of every unknown and nonzero (%s and %s entries): no neighbour coin term keeps the current" % (counts[0], counts[1]))


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: controls - free pairs keep it; the witnesses come from exclusion; a term moves most other entries."""
    ok_free = True
    for dim in (2, 3):
        p = NeighbourPair(dim, -1, mut("control_excluded_forged"), symbolic=False)
        for v in test_pairs(p):
            for comp in range(dim):
                ok_free = ok_free and not p.defect(v, comp)
    p0 = NeighbourPair(2, -1, True, symbolic=False)
    vals = [sp.Rational(((7 * i) % 19) - 9, 1 + i % 5) for i in range(32)]
    p1 = NeighbourPair(2, -1, True, symbolic=False, values=vals)
    v = test_pairs(p0)[0]
    d0 = p0.defect(v, 0)
    d1 = p1.defect(v, 0)
    witness = ((((-1, -1), 0), ((0, 0), 1)))
    ok_w = d0.get(witness) == d1.get(witness) == -sp.I / 16
    moved = sum(1 for key in set(d0) | set(d1) if d0.get(key, 0) != d1.get(key, 0))
    tpl = sp.symbols("t", real=True)

    class PlacedPair(NeighbourPair):
        def D2(self, v, comp):
            pv = self.proj(v)
            a = self.proj(self.hop(pv, lambda t, s: sp.Rational(t[0][comp] + s[0][comp], 2)))
            b = self.vterm(pv, lambda lo, hi: sp.Rational(lo[comp] + hi[comp], 2) + (tpl if self.axis(lo, hi) == comp else 0))
            return self.add(a, b)
    pp = PlacedPair(2, -1, True)
    placed_free = 0
    for vv in test_pairs(pp):
        for comp in range(2):
            for key, val in pp.defect(vv, comp).items():
                if not (val.free_symbols - {tpl}) and val != 0:
                    placed_free += 1
    ok_place = placed_free == len(v_free_entries(NeighbourPair(2, -1, True)))
    checks.check("D1", ok_free and ok_w and moved > 0 and ok_place,
                 "T3: without exclusion and without a term the defect vanishes on every test pair on Z^2 and Z^3 (free pairs keep the current, block 137); with exclusion, the pair at (0,0) and (1,0) with both coins up has the defect -i/16 on the state with records at (-1,-1) (up) and (0,0) (down) for no term and for a rational term, while the term moves %d other entries: the witnesses are exclusion's and no neighbour coin term reaches them; with the term's energy anywhere on the bond's line (a free offset t), the same %d entries stay free of every unknown" % (moved, placed_free))


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: on a line there is nothing to repair."""
    p = NeighbourPair(1, -1, True, symbolic=False)
    ok_line = True
    o = (0,)
    for pos2 in ((1,), (2,)):
        for c1 in (0, 1):
            for c2 in (0, 1):
                key, sg = p.canon((o, c1), (pos2, c2))
                if not key:
                    continue
                d = p.defect({key: sg}, 0)
                ok_line = ok_line and not d
    if mut("line_obstruction_forged"):
        ok_line = not ok_line
    checks.check("E1", ok_line,
                 "T4: on the line, two excluded records keep the current with no term (block 137 T2), so the obstruction of T1-T2 belongs to two and three dimensions: there a record must pass around the other's site, and exclusion removes paths that no change of the neighbours' coins restores")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54 and 78 as landed on main (the walk and one record per site), with blocks 121 and 137 placed; it reports whether a coin interaction between neighbouring records can restore the books that exclusion breaks; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "DeWitt", "Hojman", "Kuchar", "Kuchař", "Teitelboim", "Dirac", "Bergmann", "Lorentz", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the defect of the total energy current symbolically in 32 (Z^2) and 48 (Z^3) real unknowns, both exchange signs",
    "per_site: executed - adjacent, diagonal and distance-two test pairs with every coin pair; the witness entry for no term and for a rational term",
    "per_mode: executed - the term's energy anywhere on the bond's line (a symbolic offset); the free and excluded controls",
    "per_block: executed - the line: excluded pairs keep the current with no term",
    "lattice_wide: two records on the open lattice; coin terms on neighbouring pairs only; correlated hops and other placements not treated",
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
    print("scope: one record per site - no coin interaction between neighbouring records restores the energy current of two excluded records on Z^2 or Z^3; supervisor derivation, unrefereed; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
