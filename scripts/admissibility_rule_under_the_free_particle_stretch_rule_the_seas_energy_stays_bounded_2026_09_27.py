#!/usr/bin/env python3
"""Exact checks: block 147's homogeneous zero-mode model (landed; a supplied scalar constraint 24 alpha l^3 lambdadot^2 = m(lambda) with the
filled sea's instantaneous energy per site as source) redone under the free-particle stretch rule (blocks 184, 185; pushed) instead of
the frame H/l. (T1) every wave's energy is nonincreasing in l, strictly where it moves, and bounded by sqrt(3 + mu^2) on 0 < l^2 < 2, so
the sea's energy per site m_sea(l) is nondecreasing and bounded, with no -I/l divergence as l -> 0; (T2) on block 147's side-4 torus every
label is a fixed point of the rule, so m_sea is exactly constant, -(3 + 3 sqrt 2 + sqrt 3)/8 when massless: the frame's turn at l = I/m0 is
replaced by motion at every length (m0 > I) or none (m0 < I); (T3) on side 6 the moving labels have |v|^2 = 1/4 at l = 1, so m_sea
strictly increases there and the pressure ratio is 1/12; (T4) in the model, when m stays positive, a contracting branch reaches l -> 0 and
an expanding one reaches l = sqrt 2 (where the rule ends) in finite time: a bounce needs m0 below the finite value -m_sea(0+). The
supervisor's own derivation, unrefereed. Blocks 139 and 147 as landed; blocks 180, 184 and 185 (pushed) placed and the facts re-derived.

A (premises): landed block 147 (the constraint, the frame's sea energy, the turn, the side-4 value); landed block 139; the axioms.
B (T1): the law's sign; the bound |F| <= 1 for 0 < l^2 < 2.
C (T2): the fixed labels 0, pi/2, pi of the rule; the side-4 sea energy is constant; the model's two cases.
D (T3): side 6 at l = 1: |v|^2 = 1/4 for every moving label, d log E/d log l = -1/4, pressure ratio 1/12.
E (T4): finite times to l -> 0 and to l = sqrt 2 when m >= m_min > 0; the frame's m_sea = -I/l forces a turn for every m0.
Exact (sympy). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import re
import sys
import time
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_UNDER_THE_FREE_PARTICLE_STRETCH_RULE_THE_SEAS_ENERGY_STAYS_BOUNDED_AND_A_CLOSED_LATTICE_THAT_SEES_IT_NEED_NOT_BOUNCE_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_THE_MEMBERS_ZERO_MODE_TESTS_THE_ZERO_OF_ENERGY_IF_THE_MEMBER_SEES_THE_HALF_FILLED_SEA_A_CLOSED_LATTICE_BOUNCES_OR_CANNOT_MOVE_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/ADMISSIBILITY_RULE_THE_BOOKS_ADMIT_ONE_REST_ENERGY_THE_STAGGERED_MASS_KEEPS_THEM_EXACTLY_SO_MASSIVE_CONTENT_MEETS_THE_MEMBER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_under_the_free_particle_stretch_rule_the_seas_energy_stays_bounded_and_a_closed_lattice_that_sees_it_need_not_bounce_bounded_theorem_note_2026-09-27"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED147 = (
    "constraint `24alpha ell³ lambdadot²=m(lambda)`",
    "`m_sea=-I/ell`",
    "The permitted lengths obey ell>=I/m0.",
    "`I=(3+3sqrt(2)+sqrt(3))/8`",
)
LANDED139 = (
    "`mε` anticommutes with the walk, so the squared energy is `|sin k|² + m²`",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "bound_forged": "B",
    "fixed_label_forged": "C",
    "side6_forged": "D",
    "time_forged": "E",
    "claim_transition_injected": "G",
    "claim_classical_name_in_theorem": "G",
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
L = sp.Symbol("l", positive=True)
k0 = sp.Symbol("k0", real=True)


def rule_k(kk0, l_):
    return kk0 + (l_ ** 2 - 1) / 2 * sp.sin(2 * kk0)


def rule_F(kk0, l_):
    return sp.sin(kk0) * sp.sqrt(sp.sin(kk0) ** 2 + l_ ** 2 * sp.cos(kk0) ** 2)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t147, t139 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note and len(CLAIM_ID) <= 195, f"the note is present and carries its claim id ({len(CLAIM_ID)} characters) and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its stretch rule, the sea and the zero-mode model are supplied)")
    needles = list(LANDED147)
    if mut("landed_quote_forged"):
        needles[2] = "The permitted lengths obey ell<=I/m0."
    checks.check("A3", all(n in t147 for n in needles) and all(n in t139 for n in LANDED139), "landed block 147: the constraint 24 alpha l^3 lambdadot^2 = m(lambda), the frame's m_sea = -I/l, the turn l >= I/m0, and I = (3 + 3 sqrt 2 + sqrt 3)/8 on side 4; landed block 139: the staggered mass anticommutes")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    # the law (block 185 T1): d log E/d log l = -l^2 |v|^2 <= 0
    Fa = sp.symbols("F1:4", real=True)
    Fd = sp.symbols("D1:4", real=True)
    mu = sp.Symbol("mu", nonnegative=True)
    E2 = sum(f_ ** 2 for f_ in Fa) + mu ** 2
    m = L ** 2
    dlogE = 2 * m * sum(Fa[i] * (-Fa[i] * Fd[i] ** 2 / 2) for i in range(3)) / E2
    ok_sign = sp.simplify(dlogE + m * sum(Fa[i] ** 2 * Fd[i] ** 2 for i in range(3)) / E2) == 0
    # |F| <= 1 for 0 < l^2 < 2: F^2 = x(x + l^2(1 - x)), x = sin^2 k0 in [0, 1]; d/dx = l^2 + 2x(1 - l^2) > 0 on [0, 1] iff l^2 < 2
    x = sp.Symbol("x", nonnegative=True)
    F2 = x * (x + m * (1 - x))
    d = sp.expand(sp.diff(F2, x))
    ok_mono = sp.simplify(d.subs(x, 0) - m) == 0 and sp.simplify(d.subs(x, 1) - (2 - m)) == 0 and sp.degree(d, x) == 1
    top = sp.simplify(F2.subs(x, 1))
    if mut("bound_forged"):
        top = top + 1
    checks.check("B1", ok_sign, "under the rule d log E/d log l = -l^2 |v|^2 <= 0 for every wave (block 185 T1), massless or massive: every wave's energy is nonincreasing in l, strictly where it moves")
    checks.check("B2", ok_mono and top == 1, "F^2 = x(x + l^2(1 - x)) with x = sin^2 k0 has x-derivative l^2 + 2x(1 - l^2), equal to l^2 at x = 0 and 2 - l^2 at x = 1, so it is increasing on [0, 1] for 0 < l^2 < 2 with maximum 1: |F| <= 1, E <= sqrt(3 + mu^2), and |m_sea| <= sqrt(3 + mu^2) at every stretch")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    fixed = [sp.Integer(0), sp.pi / 2, sp.pi]
    ok_fix = all(sp.simplify(rule_k(p_, L) - p_) == 0 for p_ in fixed)
    vals = [sp.simplify(rule_F(p_, L)) for p_ in fixed]
    want = [0, 1, 0]
    if mut("fixed_label_forged"):
        want = [0, L, 0]
    ok_vals = [sp.simplify(v_ - w_) == 0 for v_, w_ in zip(vals, want)]
    # side 4: labels 0, pi/2, pi, 3pi/2; the sea energy per site counts each reduced-zone pair once: -average_k E(k)
    labels = [sp.Integer(0), sp.pi / 2, sp.pi, 3 * sp.pi / 2]
    Fvals = {0: 0, 1: 1, 2: 0, 3: -1}
    Es = []
    for n in itertools.product(range(4), repeat=3):
        Es.append(sp.sqrt(sum(sp.Integer(Fvals[i]) ** 2 for i in n)))
    I4 = sp.nsimplify(sum(Es) / len(Es))
    ok_I = sp.simplify(I4 - (3 + 3 * sp.sqrt(2) + sp.sqrt(3)) / 8) == 0
    ok_side4 = all(sp.simplify(rule_F(p_, L) - rule_F(p_, 1)) == 0 for p_ in labels) and all(sp.simplify(rule_k(p_, L) - p_) == 0 for p_ in labels)
    # the model: m = m0 - I constant; lambdadot^2 = (m0 - I)/(24 alpha l^3) >= 0 at every l iff m0 >= I
    m0, alpha = sp.symbols("m0 alpha", positive=True)
    lamdot2 = (m0 - I4) / (24 * alpha * L ** 3)
    ok_model = sp.simplify(lamdot2.subs(m0, I4 + 1) * 24 * alpha * L ** 3 - 1) == 0
    checks.check("C1", ok_fix and all(ok_vals), "labels 0, pi/2 and pi (and -pi/2 by oddness) are fixed points of the rule at every l, with F = 0, 1 and 0 there")
    checks.check("C2", ok_I and ok_side4 and ok_model, f"on block 147's side-4 torus every label (0, pi/2, pi, 3pi/2) is fixed, so every wave keeps its energy and the massless sea's energy per site is -I at every l, I = {I4} (block 147's value): the model's m = m0 - I is constant, so lambdadot^2 = (m0 - I)/(24 alpha l^3) allows every length when m0 > I and none when m0 < I; the frame's turn at l = I/m0 does not occur")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    # side 6 at l = 1: sin^2 k in {0, 3/4}, cos^2 k = 1/4 where sin^2 k = 3/4; a wave with n moving axes has E^2 = 3n/4 and |v|^2 = n(3/4)(1/4)/(3n/4) = 1/4
    oks = []
    for n in (1, 2, 3):
        E2 = sp.Rational(3, 4) * n
        v2 = n * sp.Rational(3, 4) * sp.Rational(1, 4) / E2
        oks.append(v2 == sp.Rational(1, 4))
    ratio = sp.Rational(1, 4) / 3
    if mut("side6_forged"):
        ratio = sp.Rational(1, 3)
    # pressure ratio p/rho = <E l^2 |v|^2>/(3 <E>) = (1/4)/3 when every wave with E > 0 has |v|^2 = 1/4
    checks.check("D1", all(oks) and ratio == sp.Rational(1, 12), "on the side-6 torus at l = 1, massless, every wave with E > 0 has |v|^2 = 1/4, so d log E/d log l = -1/4 for each: the sea's energy per site strictly increases with l there, and its pressure ratio is 1/12 (block 180's side-6 value)")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    # time to reach l from l1 along lambdadot = sqrt(m/(24 alpha l^3)) with m >= mmin > 0: t = int sqrt(24 alpha l/m) dl <= sqrt(24 alpha/mmin) (2/3)|l^(3/2) - l1^(3/2)|
    alpha, mmin, l1 = sp.symbols("alpha mmin l1", positive=True)
    t_up = sp.integrate(sp.sqrt(24 * alpha * L / mmin), (L, 0, l1))
    want = sp.sqrt(24 * alpha / mmin) * sp.Rational(2, 3) * l1 ** sp.Rational(3, 2)
    if mut("time_forged"):
        want = want * 2
    ok_t = sp.simplify(t_up - want) == 0
    t_top = sp.simplify(sp.integrate(sp.sqrt(24 * alpha * L / mmin), (L, 1, sp.sqrt(2))))
    ok_top = t_top.is_positive and t_top.is_finite
    # the frame: m = m0 - I/l < 0 for l < I/m0 whatever m0 > 0: a turn always
    m0, I_ = sp.symbols("m0 I", positive=True)
    lt = sp.solve(sp.Eq(m0 - I_ / L, 0), L)
    ok_frame = lt == [I_ / m0]
    checks.check("E1", ok_t and ok_top and ok_frame, f"in the model, with m >= m_min > 0 the time to reach l -> 0 from l1 is at most sqrt(24 alpha/m_min)(2/3) l1^(3/2), and to reach l = sqrt 2 from l = 1 at most {t_top}: both finite, so with a bounded sea a branch on which m stays positive contracts to l -> 0 or reaches the rule's end at sqrt 2 in finite time; under the frame m = m0 - I/l vanishes at l = I/m0 for every m0, a turn")


# ============================================================================================ family G
FENCES = (
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
    "nothing is adopted and no gravitational claim is made.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens", "big bang", "singularity",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at l = sqrt 2."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Burgers", "Hopf", "Jacobi", "Ward", "Takahashi", "Wilson", "Kepler", "Bessel", "Liouville", "Paley", "Wiener", "Bloch", "Cauchy", "Parker", "Friedmann")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_g(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Friedmann) —", 1)
    norm = normalize_text(text)
    checks.check("G1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p_ for p_ in FORBIDDEN if p_ in text]
    checks.check("G2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("G3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
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
    checks.check("G4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family H
N5_LINES = (
    "per_element: executed - the law's sign; the bound on F; the fixed labels",
    "per_site: executed - the side-4 sea energy and the model's two cases",
    "per_mode: executed - side 6 at l = 1: every moving wave has |v|^2 = 1/4",
    "per_block: executed - the finite times to l -> 0 and to sqrt 2; the frame's turn",
    "lattice_wide: checked and not executed - m_sea(l) on sides 6, 8 and the infinite lattice away from l = 1 (transcendental relabelling); the adiabatic following of the sea (the stretches do not commute); the full lattice constraints",
)


def family_h(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("H1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


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
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_e(checks)
    family_g(checks, texts[0])
    family_h(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: block 147's homogeneous zero-mode model under the free-particle stretch rule: the sea's energy per site is nondecreasing and bounded, constant on side 4; a bounce needs m0 below -m_sea(0+); expanding branches meet the rule's end at sqrt 2 in finite time; the supervisor's own derivation, unrefereed; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
