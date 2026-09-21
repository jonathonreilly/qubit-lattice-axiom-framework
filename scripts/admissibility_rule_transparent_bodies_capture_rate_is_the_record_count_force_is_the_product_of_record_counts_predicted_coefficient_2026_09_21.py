#!/usr/bin/env python3
"""Exact checks: transparent bodies in the inertial record gas (block 44's clause; supplied, not adopted).

T1: in the uniform product state at density rho, the expected rate at which records step onto one given site is, for the sphere menu,
6 rho <max(0, s.e)>/sqrt 3 with <max(0, s_z)> = 1/4, that is (sqrt 3/2) rho, and for the six-axis menu 6 (rho/6) = rho: the kinetic capture
rate q_1 of one capturing site.  T2: for a body of capturing sites the same expectation is (number of exposed faces) rho/(4 sqrt 3): isolated
sites add (6 faces each), adjacent sites share faces (10 for a pair, 24 for a 2x2x2 cube; 78, 174, 294, 486 for lattice balls of radius 2 to 5).
T3: with block 45's free-streaming force K_0 Q_1 Q_2/r^2, K_0 = sqrt3/(4 pi rho (1 - rho)), two transparent bodies of N_1 and N_2 capturing sites
attract with G N_1 N_2/r^2, G = K_0 q_1^2 = 3 sqrt3 rho/(16 pi (1 - rho)); in rational form (4 pi G)^2 = 27 rho^2/(16 (1 - rho)^2).
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_TRANSPARENT_BODIES_CAPTURE_RATE_IS_THE_RECORD_COUNT_AND_THE_FORCE_IS_THE_PRODUCT_OF_RECORD_COUNTS_OVER_DISTANCE_SQUARED_PREDICTED_COEFFICIENT_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_transparent_bodies_capture_rate_is_the_record_count_and_the_force_is_the_product_of_record_counts_over_distance_squared_predicted_coefficient_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = ("A site never carries more than one record; records are permanent.",)

MUTATION_GATE = {
    "capture_counts_both_hemispheres": "B",
    "six_axis_capture_rate_wrong": "B",
    "faces_count_ignores_shared_faces": "C",
    "ball_face_count_wrong": "C",
    "coefficient_without_blocking": "D",
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


E = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def exposed_faces(body):
    body = set(body)
    return sum(1 for s in body for d in E if tuple(s[i] + d[i] for i in range(3)) not in body)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the sentence used")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    # sphere: <max(0, s_z)> over the uniform sphere = (1/2) integral_0^1 mu d mu = 1/4 (both hemispheres would give 1/2)
    half_moment = Fraction(1, 2) * Fraction(1, 2)
    if mut("capture_counts_both_hemispheres"):
        half_moment = Fraction(1, 2)
    ok = half_moment == Fraction(1, 4)
    shown = []
    for rho in (Fraction(29, 100), Fraction(1, 2)):
        q1_sq = (6 * half_moment * rho) ** 2 / 3                    # q_1 = 6 rho <max(0, s_z)>/sqrt 3
        ok = ok and q1_sq == 3 * rho * rho / 4
        shown.append(f"rho {rho}: q_1^2 = {q1_sq}")
    checks.check("B1", ok, "T1: for the sphere menu <max(0, s_z)> = 1/4 and the expected rate at which records of the uniform product state step onto one site is q_1 = 6 rho (1/4)/sqrt 3 = (sqrt 3/2) rho; in rational form q_1^2 = 3 rho^2/4 (" + "; ".join(shown) + ")")
    # six axes: each of the six neighbours holds, with probability rho/6, a record whose content points at the site
    rho = Fraction(3, 10)
    rate = Fraction(0)
    for k in range(6):                                              # the neighbour at -e_k must hold content k
        for content in range(6):
            if content == k:
                rate += rho / 6
    want = rho / 2 if mut("six_axis_capture_rate_wrong") else rho
    checks.check("B2", rate == want, "T1: for the six-axis menu each of the six neighbours holds a record pointing at the site with probability rho/6, so q_1 = rho")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    single = [(0, 0, 0)]
    far_pair = [(0, 0, 0), (5, 0, 0)]
    near_pair = [(0, 0, 0), (1, 0, 0)]
    cube = list(product(range(2), repeat=3))
    near = 12 if mut("faces_count_ignores_shared_faces") else exposed_faces(near_pair)
    ok = exposed_faces(single) == 6 and exposed_faces(far_pair) == 12 and near == 10 and exposed_faces(cube) == 24
    checks.check("C1", ok, "T2: exposed faces: 6 for a site, 12 for two separate sites, 10 for two adjacent sites, 24 for a 2x2x2 cube: capture rates of separate sites add, sites of a compact body share faces")
    counts = {}
    for big_r in (2, 3, 4, 5):
        ball = [s for s in product(range(-big_r - 1, big_r + 2), repeat=3) if sum(t * t for t in s) <= big_r * big_r]
        counts[big_r] = (len(ball), exposed_faces(ball))
    want = {2: (33, 78), 3: (123, 174), 4: (257, 294), 5: (515, 486 + (1 if mut("ball_face_count_wrong") else 0))}
    checks.check("C2", counts == want, f"T2: lattice balls of radius 2, 3, 4, 5 have {', '.join(str(v[0]) for v in counts.values())} sites and {', '.join(str(v[1]) for v in counts.values())} exposed faces; in the product state a capturing body takes up (exposed faces) rho/(4 sqrt 3) per tick")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    ok = True
    shown = []
    for rho in (Fraction(29, 100), Fraction(1, 10), Fraction(1, 2)):
        block = 1 if mut("coefficient_without_blocking") else (1 - rho)
        k0_sq_16pi2 = Fraction(3) / (rho * block) ** 2             # (4 pi K_0)^2 = 3/(rho (1 - rho))^2
        q1_sq = 3 * rho * rho / 4
        four_pi_g_sq = k0_sq_16pi2 * q1_sq ** 2                     # (4 pi G)^2 with G = K_0 q_1^2
        ok = ok and four_pi_g_sq == Fraction(27) * rho ** 2 / (16 * (1 - rho) ** 2)
        shown.append(f"rho {rho}: (4 pi G)^2 = {four_pi_g_sq}")
    checks.check("D1", ok, "T3: G = K_0 q_1^2 with K_0 = sqrt3/(4 pi rho (1 - rho)) and q_1 = (sqrt 3/2) rho is 3 sqrt3 rho/(16 pi (1 - rho)); in rational form (4 pi G)^2 = 27 rho^2/(16 (1 - rho)^2): " + "; ".join(shown))


# ============================================================================================ family F
FENCES = (
    "This note works within the supplied inertial clause of block 44 and the wind law of block 45; it reports when the capture rate of a body is its number of records and what force follows; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Navier", "Stokes", "Bernoulli", "Bjerknes", "Sage", "Boltzmann", "Gibbs", "Laplace", "Poisson", "Gauss", "Knudsen", "Smoluchowski", "Einstein", "Planck", "Lambert", "Beer")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Knudsen)", 1)
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
    "per_element: executed — the half-sphere first moment 1/4; the six-axis neighbour count",
    "per_site: executed — exposed faces of a site, of separate and adjacent pairs, of a cube and of lattice balls of radius 2 to 5",
    "per_mode: not applicable",
    "per_block: executed — the coefficient (4 pi G)^2 = 27 rho^2/(16 (1 - rho)^2) at three densities",
    "lattice_wide: T1 and T2 are exact expectations in the uniform product state, which neglects the depletion a capturing body causes; T3 combines them with block 45's free-streaming force; the capture rates and the forces of transparent bodies are executed, not proved",
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
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: transparent bodies in the inertial record gas — kinetic capture rate (sqrt 3/2) rho per site, capture by exposed faces, and the coefficient G = 3 sqrt3 rho/(16 pi (1 - rho)) of the force N1 N2/r^2; exact expectations in the product state")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
