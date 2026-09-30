#!/usr/bin/env python3
"""Exact checks: the walker sea's energy falls under every uniform shear at fixed volume, and, counted by the member, it forces
the closed lattice to shear - within block 62's framed walk, block 139's staggered mass and blocks 147 and 148 as landed: the sea's
energy per site is -<(|E s|^2 + mu^2)^(1/2)>; at fixed volume its second-order change is negative definite on traceless strains for
every mu >= 0; for unequal lengths at fixed volume it is lower at every size; in block 148's supplied homogeneous action with the
sea as content the lattice has no static or equal-rate state and the sea's force pushes lengths apart (a harvest of probe #9198's
exact part with the supervisor's extensions; not adopted).

B (second order): the pointwise expansion; the cube-averaged moments; the volume constraint and the definiteness bounds; dilations.
C (every size): the convexity identity for the diagonal frame, and the bound that makes it nonnegative.
D (the homogeneous action): the force's monotonicity identity and bound; the member's R_1 and R_2 at zero symbol.
Exact rational and symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_WALKER_SEAS_ENERGY_FALLS_UNDER_EVERY_UNIFORM_SHEAR_AT_FIXED_VOLUME_AND_COUNTED_BY_THE_MEMBER_IT_FORCES_THE_CLOSED_LATTICE_TO_SHEAR_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_walker_seas_energy_falls_under_every_uniform_shear_at_fixed_volume_and_counted_by_the_member_it_forces_the_closed_lattice_to_shear_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "second_order_coefficient_forged": "B",
    "volume_constraint_dropped": "B",
    "hessian_factor_forged": "C",
    "force_derivative_forged": "D",
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


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, the frame, the mass, the member and its homogeneous action are supplied; the memo does not define a time metric)")


S = sp.symbols("s1:4", real=True)
MU = sp.Symbol("mu", nonnegative=True)
T = sp.Symbol("t", positive=True)


def sym_h():
    return sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"h{min(i, j) + 1}{max(i, j) + 1}", real=True))


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    h = sym_h()
    sv = sp.Matrix(S)
    r2 = (sv.T * sv)[0]
    R = sp.sqrt(r2 + MU ** 2)
    E = sp.eye(3) - T * h / 2
    f = -sp.sqrt(sp.expand((sv.T * E.T * E * sv)[0]) + MU ** 2)
    ser = sp.series(f, T, 0, 3).removeO()
    shs = (sv.T * h * sv)[0]
    sh2s = (sv.T * h * h * sv)[0]
    ok1 = sp.simplify(ser.coeff(T, 1) - shs / (2 * R)) == 0 and sp.simplify(ser.coeff(T, 2) - (-sh2s / (8 * R) + shs ** 2 / (8 * R ** 3))) == 0
    checks.check("B1", ok1, "pointwise, -(|(1 - h/2) s|^2 + mu^2)^(1/2) = -R + s.hs/(2R) - s.h^2 s/(8R) + (s.hs)^2/(8R^3) + O(h^3), R = (|s|^2 + mu^2)^(1/2)")
    # the cube's signed permutations: averaging the pointwise second-order term gives the stated moment form
    group = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            group.append((perm, signs))

    def act(expr, g):
        perm, signs = g
        return expr.subs({S[i]: signs[i] * S[perm[i]] for i in range(3)}, simultaneous=True)
    second = -sh2s / (8 * R) + shs ** 2 / (8 * R ** 3)
    avg = sp.expand(sum(act(second, g) for g in group) / len(group))
    Iav = r2 / R                                    # the group average of s_i s_j / R is delta_ij |s|^2/(3R)
    Aav = (S[0] ** 2 * S[1] ** 2 + S[0] ** 2 * S[2] ** 2 + S[1] ** 2 * S[2] ** 2) / (3 * R ** 3)
    Bav = (S[0] ** 4 + S[1] ** 4 + S[2] ** 4) / (3 * R ** 3)
    trh = h.trace()
    trh2 = (h * h).trace()
    diag2 = sum(h[i, i] ** 2 for i in range(3))
    form = -Iav / 24 * trh2 + (Aav * (trh ** 2 + 2 * trh2) + (Bav - 3 * Aav) * diag2) / 8
    ok2 = sp.simplify(avg - sp.expand(form)) == 0
    checks.check("B2", ok2, "averaged over the 48 signed permutations of the axes, the pointwise second-order term is -(I/24) tr h^2 + (1/8)[A((tr h)^2 + 2 tr h^2) + (B - 3A) sum h_ii^2], with I = <|s|^2/R>, A = <s1^2 s2^2/R^3>, B = <s1^4/R^3>")
    # the volume constraint det(1 - h/2) = 1: tr h = -(1/4) tr h_T^2 + O(h^3)
    a, b, c, d, e = sp.symbols("a b c d e", real=True)
    x, y, z = sp.symbols("x y z", real=True)
    hT = sp.Matrix([[a, x, y], [x, b, z], [y, z, -a - b]])
    # h = T h_T + tr(h)/3 1 with tr h = t1 T^2 + O(T^3): det(1 - h/2) = 1 at order T^2 fixes t1
    t1 = sp.Symbol("t1")
    det = sp.expand((sp.eye(3) - (T * hT + t1 * T ** 2 * sp.eye(3) / 3) / 2).det())
    eqs = [det.coeff(T, 1), det.coeff(T, 2)]
    sol = sp.solve([e for e in eqs if e != 0], [t1], dict=True)
    vol_ok = eqs[0] == 0 and len(sol) == 1 and sp.expand(sol[0][t1] + (hT * hT).trace() / 4) == 0
    Ic, Ac, Bc = sp.symbols("I_c A_c B_c", positive=True)
    trT2 = (hT * hT).trace()
    diagT = sum(hT[i, i] ** 2 for i in range(3))
    first = Ic / 6 * (0 if mut("volume_constraint_dropped") else -trT2 / 4)
    coef = sp.Rational(1, 4) if not mut("second_order_coefficient_forged") else sp.Rational(1, 2)
    Q = first - Ic / 24 * trT2 + (Ac * (2 * trT2) + (Bc - 3 * Ac) * diagT) / 8
    Q_stated = (-Ic / 12 + coef * Ac) * trT2 + (Bc - 3 * Ac) / 8 * diagT
    stated_ok = sp.expand(Q - Q_stated) == 0
    # bounds with I >= 3B + 6A: coefficient of sum h_ii^2 and of sum_{i<j} h_ij^2
    cd = sp.expand(Q_stated).coeff(a, 2)          # h_11^2 appears as a^2 and through (-a-b)^2
    Qd = sp.expand(Q_stated.subs({x: 0, y: 0, z: 0}))
    Qo = sp.expand(Q_stated.subs({a: 0, b: 0}))
    diag_coef = sp.expand(Qo.coeff(x, 2)) / 2 if False else None
    off_coef = sp.expand(Qo).coeff(x, 2) / 2      # sum_{i<j} h_ij^2 enters tr h_T^2 twice
    diag_form = -Ic / 12 + Bc / 8 - Ac / 8
    diag_ok = sp.expand(Qd - diag_form * (a ** 2 + b ** 2 + (a + b) ** 2)) == 0
    bound_d = sp.expand((diag_form - (-(Bc + 5 * Ac) / 8)).subs(Ic, 3 * Bc + 6 * Ac)) == 0
    bound_o = sp.expand((2 * off_coef - (-(Ac + Bc) / 2)).subs(Ic, 3 * Bc + 6 * Ac)) == 0
    mono = sp.diff(diag_form, Ic) < 0 and sp.diff(2 * off_coef, Ic) < 0
    checks.check("B3", vol_ok and stated_ok and diag_ok and bound_d and bound_o and mono,
                 "fixed volume det(1 - h/2) = 1 gives tr h = -(1/4) tr h_T^2 + O(h^3); the change is Q = (-I/12 + A/4) tr h_T^2 + ((B - 3A)/8) sum h_ii^2; its diagonal coefficient -I/12 + B/8 - A/8 and off-diagonal one 2(-I/12 + A/4) fall with I and equal -(B + 5A)/8 and -(A + B)/2 at I = 3B + 6A, the least I allowed by |s|^4/R^3 <= |s|^2/R")
    cc = sp.Symbol("c", positive=True)
    dil = sp.simplify((sp.sqrt(sp.expand((sv.T * (cc * sp.eye(3)).T * (cc * sp.eye(3)) * sv)[0])) - cc * sp.sqrt(r2)))
    detg = (cc * sp.eye(3)).det() ** -2
    dil_ok = dil == 0 and sp.simplify(detg ** sp.Rational(-1, 6) - cc) == 0
    C0, Cc, lam = sp.symbols("C0 C_c lam", real=True)
    # no constant plus a multiple of sqrt(det g) matches -I (det g)^(-1/6) = -I c through second order in c = 1 - lam/2
    lhs = sp.series(C0 + Cc * (1 - lam / 2) ** -3, lam, 0, 3).removeO()
    rhs = -Ic * (1 - lam / 2)
    sol2 = sp.solve([sp.expand(lhs - rhs).coeff(lam, k) for k in range(3)], [C0, Cc], dict=True)
    checks.check("B4", dil_ok and not sol2, "a dilation E = c 1 gives -c <|s|> = -I (det g)^(-1/6) at mu = 0, and no constant plus a multiple of (det g)^(1/2) matches it through second order")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    b = sp.symbols("b1:4", positive=True)
    v = sp.symbols("v1:4", real=True)
    lam = sp.symbols("l1:4", real=True)
    s2 = sp.symbols("q1:4", positive=True)
    m2 = sp.Symbol("m2", nonnegative=True)
    f = sp.sqrt(sum(sp.exp(-2 * lam[i]) * s2[i] for i in range(3)) + m2)
    H = sp.hessian(f, lam)
    bb = [sp.exp(-2 * lam[i]) * s2[i] for i in range(3)]
    Ssum = sum(bb) + m2
    factor = 2 if not mut("hessian_factor_forged") else 1
    target = (factor * Ssum * sp.diag(*bb) - sp.Matrix(bb) * sp.Matrix(bb).T) / Ssum ** sp.Rational(3, 2)
    ident = (H - target).applyfunc(sp.simplify) == sp.zeros(3)
    # nonnegativity: 2 S sum b v^2 - (sum b v)^2 = (2S - sum b) sum b v^2 + [sum b sum b v^2 - (sum b v)^2], the bracket a sum of squares
    quad = 2 * (sum(b) + m2) * sum(b[i] * v[i] ** 2 for i in range(3)) - sum(b[i] * v[i] for i in range(3)) ** 2
    sos = sum(b[i] * b[j] * (v[i] - v[j]) ** 2 for i in range(3) for j in range(i + 1, 3))
    split = sp.expand(quad - ((sum(b) + 2 * m2) * sum(b[i] * v[i] ** 2 for i in range(3)) + sos)) == 0
    checks.check("C1", ident and split, "for f = (sum_i e^(-2 lambda_i) s_i^2 + mu^2)^(1/2) the Hessian times S^(3/2) is 2 S diag(b) - b b^T, and v.(2 S diag(b) - b b^T).v = (sum b + 2 mu^2) sum b_i v_i^2 + sum_{i<j} b_i b_j (v_i - v_j)^2 >= 0, strictly along sum v_i = 0 when every b_i > 0: f is strictly convex there, so its zone average, symmetric under permuting the axes, is least at equal lengths")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    dl = sp.Symbol("delta", real=True)
    s1, s2, s3 = sp.symbols("q1:4", positive=True)
    rest = sp.Symbol("rest", nonnegative=True)       # e^(-2c) s3^2 + mu^2
    b1 = sp.exp(-dl) * s1
    b2 = sp.exp(dl) * s2
    f = sp.sqrt(b1 + b2 + rest)
    Dint = (b2 - b1) / f
    dD = sp.diff(Dint, dl)
    power = 2 if not mut("force_derivative_forged") else 1
    stated = ((b1 + b2) * f ** 2 - (b2 - b1) ** 2 / 2) / f ** 3 if power == 2 else ((b1 + b2) * f ** 2 - (b2 - b1) ** 2) / f ** 3
    ident = sp.simplify(dD - stated) == 0
    # the bound: (b1 + b2) f^2 - (b2 - b1)^2/2 >= (b1 + b2) f^2 / 2 > 0, since (b2 - b1)^2 <= (b1 + b2)^2 <= (b1 + b2) f^2
    B1, B2, RR = sp.symbols("B1 B2 RR", nonnegative=True)
    gap = sp.expand(((B1 + B2) * (B1 + B2 + RR) - (B2 - B1) ** 2 / 2) - (B1 + B2) * (B1 + B2 + RR) / 2)
    gap_ok = sp.expand(gap - ((B1 + B2) * RR / 2 + 2 * B1 * B2)) == 0
    odd = sp.simplify(Dint.subs(dl, 0).subs({s1: s2}, simultaneous=True)) == 0
    checks.check("D1", ident and gap_ok and odd, "the force D(delta) = <(e^delta s2^2 - e^-delta s1^2)/f> vanishes at equal lengths by the swap of axes and has dD/ddelta = <[(b1 + b2) f^2 - (b2 - b1)^2/2]/f^3>, whose numerator exceeds half of (b1 + b2) f^2 by (b1 + b2) rest/2 + 2 b1 b2 >= 0: D has the sign of delta, pushing the lengths apart")
    p = sp.symbols("p1:4", real=True)
    h = sym_h()
    pv = sp.Matrix(p)
    p2 = (pv.T * pv)[0]
    R1 = p2 * h.trace() - (pv.T * h * pv)[0]
    R2 = -(p2 / 4) * (h.T * h).trace() + (h * pv).dot(h * pv) / 2 - (pv.T * h * pv)[0] * h.trace() / 2 + (p2 / 4) * h.trace() ** 2
    zero = {p[0]: 0, p[1]: 0, p[2]: 0}
    checks.check("D2", sp.simplify(R1.subs(zero)) == 0 and sp.simplify(R2.subs(zero)) == 0, "block 62's R_1 = p^2 tr h - p^T h p and R_2 vanish at zero symbol: the landed member has no energy for uniform strains")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 62, 139, 147 and 148 as landed on main (the framed walk, the staggered mass, the zero of energy the member sees, and the closed lattice's homogeneous action); it reports how the walker sea's energy responds to a uniform shear, and what that does to the closed lattice if the member counts it; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at mu = 1."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Cauchy", "Schwarz", "Jensen", "Hellmann", "Feynman", "Taylor", "Fourier", "Bloch", "Liouville",
                   "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Green", "Pauli", "Hamilton", "Wigner", "Riemann", "Hilbert", "Schur", "Fermi", "Kasner", "Fierz",
                   "Bessel", "Casimir", "Sakharov")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T3 — at every size, for unequal lengths", "## Theorem T3 — at every size, for unequal lengths (after Jensen)", 1)
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
    "per_element: executed - the pointwise second-order expansion of the lower band's energy under a symmetric frame",
    "per_site: executed - the average over the cube's 48 signed permutations, giving the fourth-moment form",
    "per_mode: executed - the volume constraint and the definiteness bounds on the traceless strain",
    "per_block: executed - the convexity identity for diagonal frames; the force's monotonicity; R_1 and R_2 at zero symbol",
    "lattice_wide: checked and not executed - every uniform frame and every mu >= 0 by proof; T4 within block 148's supplied action",
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
    print("scope: block 62's framed walk with block 139's staggered mass; the sea's energy per site under uniform frames; negative definite second-order change on traceless strains at fixed volume for every mu; lower for unequal lengths at every size; in block 148's supplied action with the sea counted, no static or equal-rate state and a force pushing lengths apart; harvest of #9198 with supervisor extensions, unrefereed; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
