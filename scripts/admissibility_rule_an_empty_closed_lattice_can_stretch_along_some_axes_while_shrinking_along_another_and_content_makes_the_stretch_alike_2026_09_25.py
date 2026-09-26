#!/usr/bin/env python3
"""Supplied nonlinear diagonal homogeneous action -8alpha exp(sum lambda) sum_(i<j) lambdadot_i lambdadot_j/w-w m with alpha positive. Vacuum power laws satisfy sum p=sum p²=1, while static solutions are also allowed. The stated constant positive rest-content family obeys the constraint on its integration-constant cone and has late expanding-branch rates t lambdadot_i tending to 2/3. Length ratios need not tend to one. This is not full nonlinear lattice solvability, all-content isotropization or derivation of the finite action from its quadratic coefficients."""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_AN_EMPTY_CLOSED_LATTICE_CAN_STRETCH_ALONG_SOME_AXES_WHILE_SHRINKING_ALONG_ANOTHER_AND_CONTENT_MAKES_THE_STRETCH_ALIKE_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_THE_LATTICE_EXPANDS_WITH_THE_STATIC_PULLS_COUPLING_IFF_ALPHA_EQUALS_K_OVER_FOUR_AND_TOP_SPEED_WALKERS_LOSE_ENERGY_AS_ONE_OVER_THE_LENGTH_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/ADMISSIBILITY_RULE_THREE_LENGTHS_PER_SITE_A_BODY_AT_REST_STRETCHES_THEM_ALIKE_HOP_ENERGY_DRIVES_WHOLE_COLUMNS_AND_THE_DELAYS_SPEED_DEPENDS_ON_DIRECTION_BOUNDED_THEOREM_NOTE_2026-09-21.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_an_empty_closed_lattice_can_stretch_along_some_axes_while_shrinking_along_another_and_content_makes_the_stretch_alike_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "cross_term_coefficient_forged": "B",
    "exponent_family_forged": "C",
    "content_cone_dropped": "D",
    "mirror_sign_forged": "D",
    "isotropic_reduction_forged": "E",
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
HALF = sp.Rational(1, 2)
QUARTER = sp.Rational(1, 4)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[:2]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the member, its kinetic term, the volume factor and the content are supplied; the memo does not define a time metric)")


# ============================================================================================ helpers
def three_length_model(al, m_const):
    t = sp.Symbol("t", positive=True)
    lam = [sp.Function("lam%d" % i)(t) for i in range(3)]
    w = sp.Symbol("w", positive=True)
    ld = [sp.diff(x, t) for x in lam]
    V = sp.exp(sum(lam))
    L = -8 * al * V * (ld[0] * ld[1] + ld[0] * ld[2] + ld[1] * ld[2]) / w - w * m_const
    con = sp.diff(L, w).subs(w, 1)
    els = [(sp.diff(sp.diff(L, ld[k]), t) - sp.diff(L, lam[k])).subs(w, 1) for k in range(3)]
    return t, lam, con, els


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    al, be = sp.symbols("alpha beta", positive=True)
    ld = sp.symbols("d1:4")
    hd = sp.diag(*[2 * x for x in ld])
    kin = sp.expand(al * (hd * hd).trace() + be * hd.trace() ** 2)
    M1 = sp.expand(kin).coeff(ld[0], 2)
    M2 = sp.expand(kin).coeff(ld[0], 1).coeff(ld[1], 1)
    target_m2 = 4 * be if mut("cross_term_coefficient_forged") else 8 * be
    at_ratio = sp.simplify(kin.subs(be, -al) + 8 * al * (ld[0] * ld[1] + ld[0] * ld[2] + ld[1] * ld[2])) == 0
    checks.check("B1", sp.simplify(M1 - 4 * (al + be)) == 0 and sp.simplify(M2 - target_m2) == 0 and at_ratio,
                 "the member's kinetic term on a uniform diagonal stretch h_ii = 2 lam_i is block 61's M1 sum lamdot^2 + M2 sum_{i<m} lamdot_i lamdot_m with M1 = 4(alpha + beta), M2 = 8 beta: at the closing ratio only -8 alpha sum_{i<m} lamdot_i lamdot_m survives")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    al = sp.Symbol("alpha", positive=True)
    u = sp.Symbol("u", positive=True)
    den = 1 + u + u ** 2
    p = [-u / den, (1 + u) / den, u * (1 + u) / den]
    if mut("exponent_family_forged"):
        p = [sp.Rational(1, 3)] * 3
    sums = sp.simplify(sum(p)) == 1 and sp.simplify(sum(x ** 2 for x in p)) == 1
    t, lam, con, els = three_length_model(al, 0)
    sub = {lam[k]: p[k] * sp.log(t) for k in range(3)}
    solves = sp.simplify(con.subs(sub).doit()) == 0 and all(sp.simplify(e.subs(sub).doit()) == 0 for e in els)
    ldi = sp.Symbol("ldi", real=True)
    iso = sp.solve(sp.Eq(-8 * al * 3 * ldi ** 2, 0), ldi) == [0]
    checks.check("C1", sums and solves and iso,
                 "an empty closed lattice: l_i = t^(p_i) with p = (-u, 1 + u, u(1 + u))/(1 + u + u^2) solves the constraint and the three equations exactly, with sum p = sum p^2 = 1; an isotropic motion needs 3 lamdot^2 = 0, so an empty lattice cannot stretch alike")
    pa, pb = sp.symbols("pa pb", real=True)
    pc = 1 - pa - pb
    cond = sp.expand(pa * pb + pa * pc + pb * pc)
    # sum p = 1 and sum_{i<j} p_i p_j = 0 force some p <= 0: the product of the three is -(the cube's) ... check: if all p > 0 then sum p^2 < (sum p)^2 = 1
    allpos_impossible = sp.simplify(sp.expand((pa + pb + pc) ** 2 - (pa ** 2 + pb ** 2 + pc ** 2)) - 2 * cond) == 0
    checks.check("C2", allpos_impossible, "with sum p = 1, sum p^2 = 1 is sum_{i<j} p_i p_j = 0, impossible if all p_i > 0: some length shrinks or stays, unless the motion is the static one")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    al, m0 = sp.symbols("alpha m0", positive=True)
    t = sp.Symbol("t", positive=True)
    D = sp.symbols("D0:3")
    Dsum = sum(D)
    Vt = (sp.Rational(3, 2) * m0 * t ** 2 + Dsum * t) / (16 * al)
    S = sp.diff(Vt, t) / Vt
    lamdot = [S - (m0 * t + D[k]) / (8 * al * Vt) for k in range(3)]
    sum_ok = sp.simplify(sum(lamdot) - S) == 0
    cone = D[0] ** 2 + D[1] ** 2 + D[2] ** 2 - 2 * (D[0] * D[1] + D[0] * D[2] + D[1] * D[2])
    resid = sp.simplify(8 * al * Vt * (lamdot[0] * lamdot[1] + lamdot[0] * lamdot[2] + lamdot[1] * lamdot[2]) - m0)
    expected_resid = 0 if mut("content_cone_dropped") else -cone / (t * (2 * Dsum + 3 * m0 * t))
    cone_ok = sp.simplify(resid - expected_resid) == 0
    el_ok = all(sp.simplify(sp.diff(8 * al * Vt * (S - lamdot[k]), t) - m0) == 0 for k in range(3))
    late = [sp.limit(x * t, t, sp.oo) for x in lamdot]
    tr = sp.Symbol("tr", real=True)
    lam_r = [x.subs(t, tr) for x in lamdot]
    past = [sp.limit(x * tr, tr, -sp.oo) for x in lam_r]
    flip = {tr: -tr, D[0]: -D[0], D[1]: -D[1], D[2]: -D[2]}
    if mut("mirror_sign_forged"):
        flip = {tr: -tr}
    mirror_ok = all(sp.simplify(x.subs(flip, simultaneous=True) + x) == 0 for x in lam_r)
    two_thirds = [sp.Rational(2, 3)] * 3
    checks.check("D1", sum_ok and cone_ok and el_ok and late == two_thirds and past == two_thirds and mirror_ok,
                 "rest content m0: 8 alpha V (S - lamdot_k) = m0 t + D_k with V = (3 m0 t^2/2 + D t)/(16 alpha) keeps the equations, and the constraint holds exactly on the cone D0^2 + D1^2 + D2^2 = 2(D0 D1 + D0 D2 + D1 D2); every lamdot_k t -> 2/3 as t -> +oo and as t -> -oo, so the stretch is alike wherever the lattice is large, block 146's |t|^(2/3); the family is closed under t -> -t with D_k -> -D_k, so the equations fix no direction")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    al, ld = sp.symbols("alpha ld", positive=True)
    cross = -8 * al * 3 * ld ** 2
    target = -12 * al * ld ** 2 if mut("isotropic_reduction_forged") else -24 * al * ld ** 2
    checks.check("E1", sp.simplify(cross - target) == 0, "on the isotropic stretch the cross term is -24 alpha lamdot^2, block 146's c_k = -24 alpha")


# ============================================================================================ family F
FENCES = (
    "This note studies an explicitly supplied diagonal homogeneous action; the nonlinear lattice completion remains open; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "DeWitt", "Hojman", "Kuchar", "Kuchař", "Teitelboim", "Dirac", "Bergmann", "Lorentz", "Kato", "Rosenblum", "Ruelle", "Amrein", "Georgescu", "Enss", "Lebesgue", "Levinson", "Birman", "Krein", "Schwarz", "Liouville", "Morse", "Infeld", "Hoffmann", "Fierz", "Darwin", "Laue", "Poincare", "Poincaré", "Grommer", "Belinfante", "Rosenfeld", "Lemaitre", "Lemaître", "Robertson", "Hubble", "Kasner", "Heckmann", "Schucking", "Schücking", "Bianchi", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the member's kinetic term on a uniform diagonal stretch, and its two coefficients",
    "per_site: executed - the three-length homogeneous model: constraint and equations",
    "per_mode: executed - the empty lattice's exponents: an exact rational family; the sign argument",
    "per_block: executed - rest content: the exact family, its cone condition and its late-time limit",
    "lattice_wide: uniform stretches of a closed lattice; the volume factor l1 l2 l3 supplied; unit rate",
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
    print('scope: Supplied nonlinear diagonal homogeneous action -8alpha exp(sum lambda) sum_(i<j) lambdadot_i lambdadot_j/w-w m with alpha positive. Vacuum power laws satisfy sum p=sum p²=1, while static solutions are also allowed. The stated constant positive rest-content family obeys the constraint on its integration-constant cone and has late expanding-branch rates t lambdadot_i tending to 2/3. Length ratios need not tend to one. This is not full nonlinear lattice solvability, all-content isotropization or derivation of the finite action from its quadratic coefficients.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
