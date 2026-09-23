#!/usr/bin/env python3
"""Exact point arithmetic, recentered finite-island controls and a supplied directed recurrence. No simulation or model-coupling execution."""

from __future__ import annotations

import hashlib, json
import random
import re
import sys
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_MEMORY_MB = 768
AUDIT_INPUT_PATHS = (
    "docs/SIX_AXIS_POINT_SENSITIVITIES_FINITE_ISLAND_HEALING_AND_DIRECTED_RECURRENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
EXPECTED_INPUT_SHA256 = {'docs/SIX_AXIS_POINT_SENSITIVITIES_FINITE_ISLAND_HEALING_AND_DIRECTED_RECURRENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md': 'db64c52383eb094eee873e1f99a7e14643f6f8486c8fb14cc9e9aaf5c7bcf86b', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md': 'cc7e8423b3bb35f7f2cf4699d498556b98fbc55229eb8a5d9f52e1ba00a63f97'}
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "six_axis_point_sensitivities_finite_island_healing_and_directed_recurrence_bounds_bounded_theorem_note_2026-09-16"
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
    "translation_origin_wrong": "C",
    "third_coordinate_wrong": "C",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.results = []
        self.passed = 0
        self.failed = 0
        self.failed_families: set[str] = set()

    def check(self, tag: str, ok: bool, msg: str) -> None:
        self.results.append(dict(tag=tag,passed=bool(ok),detail=msg))
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
    checks.check("A3", BLOCK01_CLAIM_ID in block01 and BLOCK01_FRAGMENT in block01.lower(), "the finite-window product-rule note carries its claim_id and the rule's product form")
    checks.check("A4", all(Path(ROOT, p).exists() and hashlib.sha256(Path(ROOT,p).read_bytes()).hexdigest()==EXPECTED_INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS), "all three declared source/parent pins match")


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
    checks.check("B1", 3 * c_lo == Fraction(406962630,413162167) and 3 * c_hi == Fraction(871815,862244) and 3 * c_lo < 1 < 3 * c_hi, f"Exact point evaluations at (p, 1, 2): 3c = {3 * c_lo} < 1 at p = 37/10 and 3c = {3 * c_hi} > 1 at p = 19/5 (c the exact total-variation sensitivity to one predecessor, maximised over the 216 triples and the five alternatives)")
    p0 = 285718
    if mut("threshold_p0_wrong"):
        p0 = 285717
    eps0 = Fraction(7, 10 ** 6)
    ok = max(deviations(p0, 1, 2)) <= eps0 < max(deviations(p0 - 1, 1, 2))
    checks.check("B2", ok, "The maximum of the three deviations is <=7/10^6 at p=285718 and >7/10^6 at p=285717; two integer evaluations only")

    checks.check("B3", 3*sensitivity(Fraction(1,10))==Fraction(87,52), "Exact p=1/10 value 3c=87/52; no half-line conclusion")

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
    assert island3 and all(sum(i)==0 for i in island3)
    if not mut("translation_origin_wrong"):
        origin=min(island3)
        island3=[tuple(i[j]-origin[j] for j in range(3)) for i in island3]
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
                maxima_ok = maxima_ok and max(a for a, b in nxt) <= max(a for a, b in cur) and max(b for a, b in nxt) <= max(b for a, b in cur) and max((2 if mut("third_coordinate_wrong") else 1)*t-a-b for a,b in nxt) <= max((2 if mut("third_coordinate_wrong") else 1)*(t-1)-a-b for a,b in cur)
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

    examples=[[(0,0,0)],[(0,0,0),(1,0,-1),(0,1,-1)]]
    translations=[(0,0,0),(100,-100,0),(-73,19,54)]
    checks.check("C3", all(region_size([tuple(i[j]+v[j] for j in range(3)) for i in I])[0]==expected for I,expected in zip(examples,[3,76]) for v in translations), "Singleton and triangle region counts 3 and 76 under three level-zero translations")

# ============================================================================================ family D
def p_t(t, a, b):
    c = t - a - b
    if min(a, b, c) < 0:
        return Fraction(0)
    return Fraction(factorial(t), factorial(a) * factorial(b) * factorial(c)) / 3 ** t


def family_d(checks: Checks) -> None:
    g = Fraction(2, 7)   # explicitly supplied recurrence coefficient; the identity is polynomial in g
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
    checks.check("D1", ok, "Equality majorant E_{t+1}=g sum_j E_t(x-e_j), E0=2 delta, gives 2(3g)^t p_t and total 2(3g)^t through t=6; no sphere coupling tested")


# Five truthful resolution lines; printing them is not an additional mathematical check.
N5_LINES = (
    "per_element: executed — exact six-axis sensitivities at three rational points and deviations at two integers",
    "per_site: executed — 300 seeded finite islands with true third coordinate and recurrence majorant through six steps",
    "per_mode: executed — 120 recentered region counts, polynomial inequality and translated singleton/triangle cases",
    "per_block: checked and not executed — historical finite simulation protocols and all raw outputs preserved; primary performs no simulation",
    "lattice_wide: checked and not executed — full general eroder, finite noise bound and supplied recurrence proofs; no asymptotic threshold or model-coupling inference",
)
def family_g(checks):
    for line in N5_LINES:
        print(line)


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
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    output=ROOT/"logs"/"runner-cache"/(Path(__file__).stem+("--"+ACTIVE_MUTATION if ACTIVE_MUTATION else "")+".json")
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(dict(checks=checks.results,passed=checks.passed,failed=checks.failed,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=EXPECTED_INPUT_SHA256,mutation=ACTIVE_MUTATION),indent=2)+"\n")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
