#!/usr/bin/env python3
"""Positive grand-canonical nearest-neighbor conditionals: sharp total-variation influence, an explicit uniqueness criterion, reflection identities and finite arithmetic without a coexistence claim."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_WHERE_MOVING_RECORDS_CANNOT_CLUMP_A_SHARP_ONE_SITE_BOUND_GIVES_UNIQUENESS_BELOW_A_RATIO_SPREAD_OF_49_OVER_25_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE_IS_A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md')
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
    note, axioms = texts[:2]
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
    """Exact checks for the scoped companion statements."""
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
    checks.check("B1", good and tv2 == Fr(1, 5), 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
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
    checks.check("C1", good and spread312 and content_only, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
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
    checks.check("D1", good and crossing == [], 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
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
    checks.check("E1", patterns and bounds_ok and cert, 'Scoped exact check E1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


def family_scope(checks):
    c=Fr(1,10)
    small=Rmax(c,Fr(9),Fr(8),Fr(8))
    Om=sp.Matrix(6,6,lambda i,j: 3 if i==j else (1 if i//2==j//2 else 2))
    vec=sp.Matrix([1,-1,0,0,0,0])
    checks.check("D9", small<LIM and (Om-sp.ones(6))*vec==2*vec and Rmax(Fr(1,100),Fr(3),Fr(1),Fr(2))>=9, 'Scoped exact check D9: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family F
FENCES = ('This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.', 'No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.')
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
    nodes = list(ast.walk(ast.parse(src)))
    float_hits = [n for n in nodes if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    float_hits += [n for n in nodes if isinstance(n, ast.Call) and ((isinstance(n.func, ast.Name) and n.func.id in ('float', 'N')) or (isinstance(n.func, ast.Attribute) and n.func.attr in ('evalf', 'N')))]
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
    "per_element: exact matrix or algebraic elements in the specified fixtures",
    "per_site: site identities in the explicitly stated finite fixtures",
    "per_mode: only the modes or finite spectral invariants actually checked below",
    "per_block: the stated finite operator and state comparisons",
    "lattice_wide: general conclusions rely on the scoped written proofs; historical simulations are deferred",
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
    family_scope(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print('scope: Positive grand-canonical nearest-neighbor conditionals: sharp total-variation influence, an explicit uniqueness criterion, reflection identities and finite arithmetic without a coexistence claim.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
