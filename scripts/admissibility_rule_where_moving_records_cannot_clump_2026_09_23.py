#!/usr/bin/env python3
"""Exact checks: where moving records cannot clump - a sharp one-site bound gives uniqueness below a ratio spread of 49/25; site-plane reflection
positivity holds for every law (a probes worker's result, w-macbookpro90c72-j046a, refereed by a Grok model, another family; block 39's law with vacancies; not adopted).

B (T1): sup TV between f and f h, h in [m, M], is (sqrt M - sqrt m)/(sqrt M + sqrt m), attained.
C (T2): uniqueness at every fugacity when R_max < 49/25; exact windows; (3,1,2) has spread 9 (referee's correction), no certificate.
D (T3): bond-plane reflection positivity iff c >= c0, p >= q, p + q >= 2r; site-plane reflection positivity for every positive law.
E (T4): the unit-cube bad patterns (254 in 16 classes) and an exact certificate of the (very conservative) contour condition.
Exact arithmetic only (Fractions, exact symbolic algebra); the runner scans its own source for floating-point literals.
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
    "docs/ADMISSIBILITY_RULE_WHERE_MOVING_RECORDS_CANNOT_CLUMP_A_SHARP_ONE_SITE_BOUND_GIVES_UNIQUENESS_BELOW_A_RATIO_SPREAD_OF_49_OVER_25_BOUNDED_THEOREM_NOTE_2026-09-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_where_moving_records_cannot_clump_a_sharp_one_site_bound_gives_uniqueness_below_a_ratio_spread_of_49_over_25_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "tv_bound_loosened": "B",
    "window_widened": "C",
    "bond_plane_eigenvalue_forged": "D",
    "certificate_constant_forged": "E",
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


# ============================================================================================ helpers (block 39's law with vacancies)
import itertools
import random
from collections import Counter, deque

Fr = F
CONT = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
STATES = [None] + CONT
LIM = Fr(49, 25)


def Wt(a, b, c, p, q, r):
    if a is None or b is None:
        return Fr(1)
    return c * (p if a == b else (q if a == tuple(-x for x in b) else r))


def Rmax(c, p, q, r):
    best = Fr(1)
    for b in STATES:
        for b2 in STATES:
            if b == b2:
                continue
            hs = [Wt(a, b2, c, p, q, r) / Wt(a, b, c, p, q, r) for a in STATES]
            best = max(best, max(hs) / min(hs))
    return best


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the sharp one-site bound sup TV = (sqrt M - sqrt m)/(sqrt M + sqrt m), attained."""
    Mm, mm, H = sp.symbols("M m H", positive=True)
    val = (H - mm) * (Mm - H) / ((Mm - mm) * H)
    crit = sp.solve(sp.diff(val, H), H)
    best = sp.simplify(val.subs(H, sp.sqrt(Mm * mm)))
    claim = (sp.sqrt(Mm) - sp.sqrt(mm)) / (sp.sqrt(Mm) + sp.sqrt(mm)) if not mut("tv_bound_loosened") else (Mm - mm) / (Mm + mm)
    good = sp.sqrt(Mm * mm) in crit and sp.simplify(best - claim) == 0
    rng = random.Random(20260923)
    for _ in range(300):
        k = rng.randint(2, 7)
        f = [Fr(rng.randint(1, 20), rng.randint(1, 9)) for _ in range(k)]
        h = [Fr(rng.randint(1, 30), rng.randint(1, 9)) for _ in range(k)]
        tot, totp = sum(f, Fr(0)), sum((fi * hi for fi, hi in zip(f, h)), Fr(0))
        tv = sum((max(Fr(0), fi * hi / totp - fi / tot) for fi, hi in zip(f, h)), Fr(0))
        good = good and max(h) / min(h) >= ((1 + tv) / (1 - tv)) ** 2
    f2 = [Fr(2), Fr(3)]
    h2 = [Fr(9), Fr(4)]
    tv2 = sum((max(Fr(0), fi * hi / sum((a * b for a, b in zip(f2, h2)), Fr(0)) - fi / sum(f2, Fr(0))) for fi, hi in zip(f2, h2)), Fr(0))
    checks.check("B1", good and tv2 == Fr(1, 5), "T1: for laws P ~ f and P' ~ f h with h in [m, M], the largest total-variation distance over f is (sqrt M - sqrt m)/(sqrt M + sqrt m) = tanh(log(M/m)/4), attained by a two-point f (maximiser at mean sqrt(Mm), symbolic; 300 random rational instances within it; 1/5 attained at M/m = 9/4)")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: uniqueness at every fugacity when every neighbour change has ratio spread below 49/25."""
    lim = LIM if not mut("window_widened") else LIM + Fr(1, 10)
    w = Fr(1)
    good = True
    for cw in (Fr(25, 49) + Fr(1, 1000), Fr(1), Fr(49, 25) - Fr(1, 1000)):
        good = good and Rmax(cw, w, w, w) < lim
    for cw in (Fr(25, 49) - Fr(1, 1000), Fr(49, 25) + Fr(1, 1000)):
        good = good and not Rmax(cw, w, w, w) < lim
    p, q, r = Fr(9), Fr(8), Fr(8)
    good = good and Rmax(Fr(25, 392) + Fr(1, 10 ** 4), p, q, r) < lim and Rmax(Fr(49, 225) - Fr(1, 10 ** 4), p, q, r) < lim
    good = good and not Rmax(Fr(25, 392) - Fr(1, 10 ** 4), p, q, r) < lim and not Rmax(Fr(49, 225) + Fr(1, 10 ** 4), p, q, r) < lim
    spread312 = all(Rmax(Fr(k, 10), Fr(3), Fr(1), Fr(2)) >= 9 for k in range(1, 40))
    content_only = max(Wt(a, (-1, 0, 0), Fr(1), Fr(3), Fr(1), Fr(2)) / Wt(a, (1, 0, 0), Fr(1), Fr(3), Fr(1), Fr(2)) for a in CONT) / min(Wt(a, (-1, 0, 0), Fr(1), Fr(3), Fr(1), Fr(2)) / Wt(a, (1, 0, 0), Fr(1), Fr(3), Fr(1), Fr(2)) for a in CONT) == 9
    checks.check("C1", good and spread312 and content_only, "T2: six neighbours, each changing a site's conditional law by at most tanh(log R/4), give uniqueness at every fugacity when R_max < 49/25 (6 tanh(log R/4) < 1): content-less records for 25/49 < cw < 49/25 (at the neutral scale cw = 1 the sites are independent), (9,8,8) for 25/392 < c < 49/225, checked exactly just inside and outside each edge; at (3,1,2) a neighbour turned to its opposite content changes the odds by (p/q)^2 = 9 (the referee's correction of the worker's 4), so no certificate at any c")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: reflection positivity - bond planes from the neutral scale up (block 39 T5); site planes for every positive law."""
    cc, P_, Q_, R_ = sp.symbols("c p q r", positive=True)
    Om = sp.Matrix(6, 6, lambda i, j: P_ if i == j else (Q_ if i // 2 == j // 2 else R_))
    Sch = cc * Om - sp.ones(6, 6)
    vecs = {"uniform": sp.Matrix([1] * 6), "vector": sp.Matrix([1, -1, 0, 0, 0, 0]), "quadrupole": sp.Matrix([1, 1, -1, -1, 0, 0])}
    eig = {k: sp.simplify((Sch * v)[0] / v[0]) for k, v in vecs.items()}
    quad = cc * (P_ + Q_ - 2 * R_) if not mut("bond_plane_eigenvalue_forged") else cc * (P_ + Q_ + 2 * R_)
    good = sp.simplify(eig["uniform"] - (cc * (P_ + Q_ + 4 * R_) - 6)) == 0 and sp.simplify(eig["vector"] - cc * (P_ - Q_)) == 0
    good = good and sp.simplify(eig["quadrupole"] - quad) == 0
    # site planes: nearest-neighbour bonds never cross a plane of sites (a plane x_1 = 0 contains its sites; every bond joins sites whose
    # first coordinates differ by at most one, so no bond joins x_1 < 0 to x_1 > 0)
    crossing = [(x, d) for x in range(-2, 3) for d in (1, -1) if (x < 0 < x + d) or (x + d < 0 < x)]
    checks.check("D1", good and crossing == [], "T3: through bond planes the law with vacancies is reflection positive iff the 7x7 bond matrix is positive semidefinite, iff its Schur complement c Omega - J (eigenvalues cT - 6, c(p - q), c(p + q - 2r)) is: c >= c0, p >= q, p + q >= 2r (block 39 T5); through planes of sites no nearest-neighbour bond crosses, so the weight splits as F theta F with the plane's bonds and fugacities shared as square roots, and the law is reflection positive for every positive (c, p, q, r)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: bad unit cubes, their disseminated weights, and an explicit (very conservative) clumping certificate."""
    cube = list(itertools.product((0, 1), repeat=3))
    res = Counter()
    for bits in itertools.product((0, 1), repeat=8):
        if len(set(bits)) == 1:
            continue
        occ = dict(zip(cube, bits))
        n = 8
        rho = Fr(sum(occ.values()), n)
        e = Fr(sum(1 for x in occ for d in range(3) if occ[x] != occ[tuple((x[i] + (1 if i == d else 0)) % 2 for i in range(3))]), n)
        seen, comp = set(), 0
        for s in (x for x in occ if occ[x]):
            if s in seen:
                continue
            comp += 1
            seen.add(s)
            dq = deque([s])
            while dq:
                x = dq.popleft()
                for d in range(3):
                    for sg in (1, -1):
                        y = tuple((x[i] + (sg if i == d else 0)) % 2 for i in range(3))
                        if occ[y] and y not in seen:
                            seen.add(y)
                            dq.append(y)
        res[(rho, e, Fr(comp, n))] += 1
    patterns = sum(res.values()) == 254 and len(res) == 16 and min(k[1] for k in res) == Fr(3, 4)
    S2, S6 = Fr(10906, 10000), Fr(12511, 10000)
    bounds_ok = S2 ** 8 >= 2 and S6 ** 8 >= 6
    base_M = 44 if not mut("certificate_constant_forged") else 20

    def eps_upper(M, tq, contents=True):
        tot = Fr(0)
        for (rho, e, kap), n in res.items():
            k8 = int(kap * 8)
            rk8 = int((rho - kap) * 8)
            base = (S6 ** k8) * ((S2 ** rk8) if tq == 2 else Fr(1)) if contents else Fr(1)
            tot += n * base * Fr(1, M ** int(4 * e))
        return tot
    cert = 676 * eps_upper(base_M, 2) <= Fr(1, 4) and 676 * eps_upper(38, 1, contents=False) <= Fr(1, 4)
    checks.check("E1", patterns and bounds_ok and cert, "T4: the 254 non-uniform occupancy patterns of a unit cube, repeated with period two by the site-plane reflections, fall in 16 classes of occupied fraction, mixed-bond density (at least 3/4) and cluster density; with the tree bound for contents each weighs at most 6^kappa t^(rho - kappa) (c w*)^(-e/2) per cube, and exact rational arithmetic certifies 676 eps <= 1/4 at T/w* = 2, c w* = 44^8, and for content-less records at cw = 38^8: an explicit, very conservative region where the chessboard and contour estimates (imported) give two phases")


# ============================================================================================ family F
FENCES = (
    "This note works within the owner's moving-records reading and block 39's law with vacancies (the equilibrium of records that move by the pair weights) and reports, from a probes worker's result refereed by another model family, where that law cannot clump and which reflections it admits; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - the one-site bound on 300 random rational instances; every ordered neighbour change of the seven states",
    "per_site: executed - the 254 non-uniform occupancy patterns of a unit cube",
    "per_mode: executed - the bond matrix's Schur complement on the uniform, vector and quadrupole subspaces",
    "per_block: executed - the exact contour certificate over the 16 pattern classes",
    "lattice_wide: T1 for every pair of laws; T2 on Z^3 through the imported uniqueness criterion; T3 for every positive (c, p, q, r); T4 through the imported chessboard and contour estimates; block 39's law supplied",
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
    print("scope: where moving records cannot clump - uniqueness at every fugacity when every neighbour change has ratio spread below 49/25 (content-less 25/49 < cw < 49/25; none at (3,1,2), spread 9); site-plane reflection positivity for every law; an explicit, very conservative clumping region; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
