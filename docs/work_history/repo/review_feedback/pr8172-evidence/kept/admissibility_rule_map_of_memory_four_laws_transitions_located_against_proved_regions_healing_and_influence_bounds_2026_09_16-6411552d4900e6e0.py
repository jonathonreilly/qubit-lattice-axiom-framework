#!/usr/bin/env python3
"""Exact checks: the map of memory — the proved regions re-computed at (p, 1, 2), the healing bound for the noisy majority automaton,
and the influence bound for the sphere formation law.

Scope.  T1: block 08's criterion 3c < 1 at (p, 1, 2) holds at p = 37/10 and fails at p = 19/5 (c the exact total-variation sensitivity
of the six-axis conditional to one predecessor, maximised over all triples); block 25's condition epsilon(p, 1, 2) <= 7/10^6 holds at
p = 285718 and fails at 285717 (closed forms).  T2: the eroder bound (coordinate maxima never increase; an island with D = M_1 + M_2 + M_3
is empty at level D + 1) executed on random islands; the noise-sensitive region U counted exactly and bounded by 18 (D + 1)^3, with the
polynomial inequality behind the bound checked symbolically.  T3: the influence recursion's solution 2 (sqrt3 beta)^t p_t(x - x_0)
(exact, t <= 6).  Exact arithmetic only (integers, Fractions and sympy); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import random
import re
import sys
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_MAP_OF_MEMORY_WHERE_EACH_OF_THE_FOUR_LAWS_KEEPS_ITS_PLANE_LOCATED_AGAINST_THE_PROVED_REGIONS_WITH_THE_HEALING_AND_INFLUENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_map_of_memory_where_each_of_the_four_laws_keeps_its_plane_located_against_the_proved_regions_with_the_healing_and_influence_bounds_bounded_theorem_note_2026-09-16"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "criterion_bracket_wrong": "B",
    "threshold_p0_wrong": "B",
    "eroder_bound_wrong": "C",
    "region_count_wrong": "C",
    "polynomial_wrong": "C",
    "influence_wrong": "D",
    "claim_reading_injected": "F",
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
    checks.check("A1", CLAIM_ID in note and len(re.findall(r"^claim_id:", note, flags=re.M)) == 1, "the note carries its claim_id once")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the four sentences quoted under Premises")
    checks.check("A3", BLOCK01_CLAIM_ID in block01 and BLOCK01_FRAGMENT in block01.lower(), "block 01's note (on main) carries its claim_id and the rule's product form")
    checks.check("A4", all(Path(ROOT, p).exists() for p in AUDIT_INPUT_PATHS), "all declared inputs exist")


# ============================================================================================ family B
def conditional(p: Fraction, q: Fraction, r: Fraction, a: int, b: int, c: int):
    phi = [[r] * 6 for _ in range(6)]
    for v in range(6):
        phi[v][v] = p
        phi[v][v ^ 1] = q
    w = [phi[v][a] * phi[v][b] * phi[v][c] for v in range(6)]
    Z = sum(w)
    return [x / Z for x in w]


def sensitivity(p: Fraction) -> Fraction:
    worst = Fraction(0)
    for a, b, c in product(range(6), repeat=3):
        k1 = conditional(p, Fraction(1), Fraction(2), a, b, c)
        for a2 in range(6):
            if a2 == a:
                continue
            k2 = conditional(p, Fraction(1), Fraction(2), a2, b, c)
            worst = max(worst, sum((abs(x - y) for x, y in zip(k1, k2)), Fraction(0)) / 2)
    return worst


def deviations(p, q, r):
    p, q, r = Fraction(p), Fraction(q), Fraction(r)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    return d1, d2, d3


def family_b(checks: Checks) -> None:
    lo, hi = Fraction(37, 10), Fraction(19, 5)
    if mut("criterion_bracket_wrong"):
        lo, hi = Fraction(19, 5), Fraction(4)
    c_lo, c_hi = sensitivity(lo), sensitivity(hi)
    checks.check("B1", 3 * c_lo < 1 < 3 * c_hi, f"T1: block 08's criterion at (p, 1, 2): 3c = {3 * c_lo} < 1 at p = 37/10 and 3c = {3 * c_hi} > 1 at p = 19/5 (c the exact total-variation sensitivity to one predecessor, maximised over the 216 triples and the five alternatives)")
    p0 = 285718
    if mut("threshold_p0_wrong"):
        p0 = 285717
    eps0 = Fraction(7, 10 ** 6)
    ok = max(deviations(p0, 1, 2)) <= eps0 < max(deviations(p0 - 1, 1, 2))
    checks.check("B2", ok, "T1: block 25's condition epsilon(p, 1, 2) <= 7/10^6 holds at p = 285718 and fails at 285717 (closed forms of the three deviations)")


# ============================================================================================ family C
def erode(ones):
    cand = set()
    for (a, b) in ones:
        cand |= {(a + 1, b), (a, b + 1), (a, b)}
    new = set()
    for (a, b) in cand:
        preds = [(a - 1, b), (a, b - 1), (a, b)]
        if sum(1 for z in preds if z in ones) >= 2:
            new.add((a, b))
    return new


def region_size(island3):
    M = [max(i[j] for i in island3) for j in range(3)]
    D = sum(M)
    B = 2 * D + 1
    cnt = 0
    for y1 in range(-3 * B - 3, B + 1):
        for y2 in range(-3 * B - 3, B + 1):
            for s in range(1, D + 2):
                y = (y1, y2, s - y1 - y2)
                if y[2] > B:
                    continue
                if any(sum(max(i[j], y[j]) for j in range(3)) <= D + 1 for i in island3):
                    cnt += 1
    return cnt, D


def family_c(checks: Checks) -> None:
    random.seed(28)
    shift = 1
    if mut("eroder_bound_wrong"):
        shift = 0
    ok1 = True
    alive_at_D = 0
    islands = []
    for trial in range(300):
        n = random.randint(1, 10)
        ones = {(random.randint(-4, 4), random.randint(-4, 4)) for _ in range(n)}
        islands.append(ones)
        M1 = max(a for a, b in ones)
        M2 = max(b for a, b in ones)
        M3 = max(-a - b for a, b in ones)
        D = M1 + M2 + M3
        cur = ones
        maxima_ok = True
        for t in range(1, D + shift + 1):
            nxt = erode(cur)
            if nxt:
                maxima_ok = maxima_ok and max(a for a, b in nxt) <= max(a for a, b in cur) and max(b for a, b in nxt) <= max(b for a, b in cur) and max(-a - b for a, b in nxt) <= max(-a - b for a, b in cur)
            if t == D and nxt:
                alive_at_D += 1
            cur = nxt
        ok1 = ok1 and maxima_ok and not cur
    checks.check("C1", ok1 and alive_at_D > 0, f"T2: on 300 random islands the coordinate maxima never increase under the noiseless majority rule and every island is empty at level D + 1, D = M_1 + M_2 + M_3 ({alive_at_D} islands still alive at level D)")
    const = 18
    if mut("region_count_wrong"):
        const = 3
    ok2 = True
    worst = Fraction(0)
    for ones in islands[:120]:
        island3 = [(a, b, -a - b) for a, b in ones]
        cnt, D = region_size(island3)
        ok2 = ok2 and cnt <= const * (D + 1) ** 3
        worst = max(worst, Fraction(cnt, (D + 1) ** 3))
    Dv = sp.symbols("D", nonnegative=True)
    poly_const = 18
    if mut("polynomial_wrong"):
        poly_const = 17
    diff = sp.expand(poly_const * (Dv + 1) ** 3 - (Dv + 1) * (6 * Dv + 5) * (6 * Dv + 4) / 2)
    poly_ok = all(coef >= 0 for coef in sp.Poly(diff, Dv).all_coeffs()) and sp.simplify(diff - (Dv + 1) * (9 * Dv + 8)) == 0
    checks.check("C2", ok2 and poly_ok, f"T2: the noise-sensitive region U of an island (sites of levels 1..D+1 below some level-(D+1) site of the island's forward cone) has at most 18 (D+1)^3 sites on 120 random islands (largest ratio {worst}), and (D+1)(6D+5)(6D+4)/2 <= 18 (D+1)^3 since the difference is (D+1)(9D+8)")


# ============================================================================================ family D
def p_t(t, a, b):
    c = t - a - b
    if min(a, b, c) < 0:
        return Fraction(0)
    return Fraction(factorial(t), factorial(a) * factorial(b) * factorial(c)) / 3 ** t


def family_d(checks: Checks) -> None:
    g = Fraction(2, 7)   # stands for beta/sqrt3; the identity is polynomial in g
    Dt = {(0, 0): Fraction(2)}
    pref = Fraction(2)
    if mut("influence_wrong"):
        pref = Fraction(1)
    ok = True
    for t in range(1, 7):
        new = {}
        for (a, b), v in Dt.items():
            for da, db in ((1, 0), (0, 1), (0, 0)):
                new[(a + da, b + db)] = new.get((a + da, b + db), Fraction(0)) + g * v
        Dt = new
        ok = ok and all(v == pref * (3 * g) ** t * p_t(t, a, b) for (a, b), v in Dt.items()) and sum(Dt.values()) == pref * (3 * g) ** t
    checks.check("D1", ok, "T3: the influence recursion D_{t+1}(x) = (beta/sqrt3) sum_j D_t(x - e_j) from D_0 = 2 at x_0 is solved exactly by 2 (sqrt3 beta)^t p_t(x - x_0), whose sum over the level is 2 (sqrt3 beta)^t (t <= 6, exact)")


# ============================================================================================ family F
FENCES = (
    "This note proves, at `(p, 1, 2)`, the exact brackets of block 08's uniqueness criterion (`3c < 1` at `p = 37/10`, `3c > 1` at `19/5`) and of block 25's condition (`ε ≤ 7/10⁶` from `p = 285718`), the healing bound `P(an island with D = M_1 + M_2 + M_3 survives to level D + 1 in its forward cone) ≤ 18(D + 1)³ ε` for the noisy majority automaton, and the influence bound `2(√3β)^t p_t(x − x_0)` for the sphere formation law; the located strengths at which the four laws keep their planes are executed by simulation and are brackets, not proved values; it does not select a menu, reading, order or coupling as physical, and adopts no clause.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "the physical menu", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "has no ordered phase", "does not order",
)
CLAIM_INJECTIONS = {"claim_reading_injected": "Hence the formation reading is the physical reading."}
CLASSICAL_NAMES = ("Heisenberg", "Potts", "Metropolis", "Toom", "Dobrushin", "Peierls", "Ising", "Binder", "Doeblin", "Kantorovich")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Dobrushin)", 1)
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
            if nm in sec:
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if nm in sections[0]]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — the six-axis conditional's exact sensitivity at two rational couplings; the three deviations' closed forms at 285717 and 285718",
    "per_site: executed — the coordinate maxima and the eroder bound on 300 random islands; the influence recursion's exact solution to t = 6",
    "per_mode: executed — the noise-sensitive region counted exactly on 120 random islands against 18 (D+1)^3; the polynomial inequality symbolically",
    "per_block: executed — the map of memory by simulation in the control and refuter specs (the six-axis formation law at (p,1,2) on 128^2 and 256^2 planes, the six-axis static law on 16^3, 24^3, 32^3, the sphere static law on 16^3, 24^3); brackets, not proved",
    "lattice_wide: T1-T3 proved as stated; the located strengths are executed brackets on finite planes and lattices",
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
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
