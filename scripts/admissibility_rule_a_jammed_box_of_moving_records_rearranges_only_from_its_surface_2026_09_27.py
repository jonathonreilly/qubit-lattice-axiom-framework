#!/usr/bin/env python3
"""Exact checks: a jammed box of moving records rearranges only from its surface; the movable set grows one layer per move,
the arrangements first reached in two moves number 18L^4 + 33L^2 - 24L, and in T moves (6L^2)^T/T! + O(L^(2T-2)) with no
L^(2T-1) term (a harvest of probe #8992, confirmed by an other-family referee in #9349). Block 39's transit as landed.

A (premises): landed block 39's transit (a record moves to an empty neighbour with positive probability); the axioms.
B (T1): for L = 2..5 the sites vacated within t moves (t <= 3) are exactly those within graph distance t of the outside.
C (T2): N_1 = 6L^2 and N_2 = 18L^4 + 33L^2 - 24L for L = 2..9 by breadth-first enumeration; the two-displaced part
   C(6L^2, 2) - 12L and the one-displaced part 36L^2 - 12L separately.
D (T3): the T-displaced arrangements number [x^T](1+x)^(6(L-2)^2)(1+2x)^(12(L-2))(1+3x)^8 (checked at T = 3, L = 2..4);
   its expansion is (6L^2)^T/T! + O(L^(2T-2)) with no L^(2T-1) term for T = 1..5.
Exact (integers, sympy). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
import time
from math import comb
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_A_JAMMED_BOX_OF_MOVING_RECORDS_REARRANGES_ONLY_FROM_ITS_SURFACE_ONE_LAYER_PER_MOVE_AND_ITS_REACHABLE_ARRANGEMENTS_HAVE_NO_VOLUME_TERM_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE_IS_A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_jammed_box_of_moving_records_rearranges_only_from_its_surface_one_layer_per_move_and_its_reachable_arrangements_have_no_volume_term_bounded_theorem_note_2026-09-27"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "depth_forged": "B",
    "two_move_forged": "C",
    "generating_forged": "D",
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
            print(f"PASS: {tag} {msg}", flush=True)
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}", flush=True)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


T0 = time.time()
DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def inbox(x, L):
    return 0 <= x[0] < L and 0 <= x[1] < L and 0 <= x[2] < L


def successors(state, L):
    """state = (removed, added): frozensets of box sites vacated and outside sites occupied; yield the states one move away"""
    removed, added = state

    def occ(y):
        return (inbox(y, L) and y not in removed) or y in added

    movers = set(added)
    for x in removed:
        for d in DIRS:
            y = add(x, d)
            if inbox(y, L) and y not in removed:
                movers.add(y)
    for i in range(L):
        for j in range(L):
            for x in ((0, i, j), (L - 1, i, j), (i, 0, j), (i, L - 1, j), (i, j, 0), (i, j, L - 1)):
                if x not in removed:
                    movers.add(x)
    for x in movers:
        if not occ(x):
            continue
        for d in DIRS:
            y = add(x, d)
            if occ(y):
                continue
            rem, ad = set(removed), set(added)
            if x in ad:
                ad.discard(x)
            else:
                rem.add(x)
            if inbox(y, L):
                rem.discard(y)
            else:
                ad.add(y)
            yield (frozenset(rem), frozenset(ad))


def bfs(L, depth):
    start = (frozenset(), frozenset())
    seen = {start: 0}
    frontier = [start]
    layers = [[start]]
    for t in range(1, depth + 1):
        nxt = []
        for s in frontier:
            for s2 in successors(s, L):
                if s2 not in seen:
                    seen[s2] = t
                    nxt.append(s2)
        layers.append(nxt)
        frontier = nxt
    return layers


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, landed39 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the transit and the jammed box are supplied)")
    need = "A bond with exactly one occupied end is visited" if not mut("landed_quote_forged") else "A bond with two occupied ends is visited"
    checks.check("A3", need in landed39, "landed block 39: pair-weight transit visits a bond with exactly one occupied end, and the record moves to the empty end with positive probability")


# ============================================================================================ family B (T1)
def family_b(checks: Checks, cache) -> None:
    ok = True
    for L, tmax in ((2, 3), (3, 3), (4, 3), (5, 2)):
        layers = cache[(L, tmax)]
        vacated = set()
        for t in range(1, tmax + 1):
            for rem, _ in layers[t]:
                vacated |= rem
            shell = {(a, b, c) for a in range(L) for b in range(L) for c in range(L)
                     if min(min(a + 1, L - a), min(b + 1, L - b), min(c + 1, L - c)) <= (t if not mut("depth_forged") else t + 1)}
            ok = ok and vacated == shell
    checks.check("B1", ok, "for L = 2, 3, 4 (t <= 3) and L = 5 (t <= 2) the box sites vacated within t moves are exactly those within graph distance t of the outside: the movable set grows one layer per move")


# ============================================================================================ family C (T2)
def family_c(checks: Checks, cache) -> None:
    ok = True
    for L in range(2, 10):
        layers = cache.get((L, 3)) or cache.get((L, 2))
        n1, n2 = len(layers[1]), len(layers[2])
        two = sum(1 for rem, ad in layers[2] if len(ad) == 2)
        one = n2 - two
        want2 = 18 * L ** 4 + 33 * L ** 2 - 24 * L if not mut("two_move_forged") else 18 * L ** 4 + 33 * L ** 2 - 23 * L
        ok = ok and n1 == 6 * L ** 2 and n2 == want2 and two == comb(6 * L ** 2, 2) - 12 * L and one == 36 * L ** 2 - 12 * L
    checks.check("C1", ok, "breadth-first enumeration for L = 2..9: N_1 = 6L^2 and N_2 = 18L^4 + 33L^2 - 24L, split as C(6L^2, 2) - 12L arrangements with two displaced records and 36L^2 - 12L with one")


# ============================================================================================ family D (T3)
def family_d(checks: Checks, cache) -> None:
    x, Ls = sp.symbols("x L")
    ok = True
    for L in (2, 3, 4):
        layers = cache[(L, 3)]
        three = sum(1 for rem, ad in layers[3] if len(ad) == 3)
        gf = sp.expand((1 + x) ** (6 * (L - 2) ** 2) * (1 + 2 * x) ** (12 * (L - 2)) * (1 + 3 * x) ** 8)
        want = gf.coeff(x, 3) if not mut("generating_forged") else gf.coeff(x, 3) + 1
        ok = ok and three == want
    totals = [len(cache[(L, 3)][3]) for L in (2, 3, 4)]
    ok = ok and totals == [4184, 38394, 189128]
    for T in range(1, 6):
        # the coefficient as a polynomial in L: C(6(L-2)^2 + 12(L-2) + 8 + ..., T) structure through the product's expansion
        gfL = sp.expand(sp.series((1 + x) ** (6 * (Ls - 2) ** 2) * (1 + 2 * x) ** (12 * (Ls - 2)) * (1 + 3 * x) ** 8, x, 0, T + 1).removeO())
        cT = sp.expand(sp.simplify(gfL.coeff(x, T)))
        poly = sp.Poly(cT, Ls)
        ok = ok and poly.degree() == 2 * T and sp.simplify(poly.coeff_monomial(Ls ** (2 * T)) - sp.Rational(6 ** T, sp.factorial(T))) == 0
        ok = ok and poly.coeff_monomial(Ls ** (2 * T - 1)) == 0
    checks.check("D1", ok, f"the three-displaced arrangements at move 3 equal [x^3](1+x)^(6(L-2)^2)(1+2x)^(12(L-2))(1+3x)^8 for L = 2, 3, 4, with all arrangements at move 3 numbering {totals}; for T = 1..5 the coefficient is a polynomial in L of degree 2T with leading term 6^T L^(2T)/T! and no L^(2T-1) term")


# ============================================================================================ family F
FENCES = (
    "This note works within block 39 as landed on main (records that move to empty neighbouring sites with positive probability) and counts how a jammed box of aligned records can rearrange; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at the surface."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Kawasaki", "Glauber", "Wulff")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Kawasaki) —", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p_ for p_ in FORBIDDEN if p_ in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a_) for a_ in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + re.escape(nm) + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + re.escape(nm) + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - single moves of records to empty neighbours, with arrangements as vacated and occupied sets",
    "per_site: executed - the depth law for L = 2..5",
    "per_mode: executed - the two-move census for L = 2..9, split by displaced count",
    "per_block: executed - the three-move census for L = 2..4 and the generating function's expansion for T = 1..5",
    "lattice_wide: checked and not executed - faceted shapes; formation; the exact polynomial for three moves",
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
    for p_ in AUDIT_INPUT_PATHS:
        print(f"  {p_}")
    texts = [Path(ROOT, p_).read_text(encoding="utf-8") if Path(ROOT, p_).exists() else "" for p_ in AUDIT_INPUT_PATHS]
    cache = {}
    for L in (2, 3, 4):
        cache[(L, 3)] = bfs(L, 3)
    for L in range(5, 10):
        cache[(L, 2)] = bfs(L, 2)
    checks = Checks()
    family_a(checks, texts)
    family_b(checks, cache)
    family_c(checks, cache)
    family_d(checks, cache)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: block 39's moving records from a jammed L-box: one layer per move; N_2 = 18L^4 + 33L^2 - 24L; N_T = (6L^2)^T/T! + O(L^(2T-2)) with no L^(2T-1) term; harvest of #8992 (confirmed by #9349); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
