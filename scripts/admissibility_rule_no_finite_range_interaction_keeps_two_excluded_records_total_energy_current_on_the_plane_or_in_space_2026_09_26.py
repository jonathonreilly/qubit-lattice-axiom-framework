#!/usr/bin/env python3
"""Exact checks: no finite-range interaction keeps two excluded records' total energy current on the plane or in space -
within block 54's walk and block 78's one record per site, with any bounded hermitian translation-invariant interaction of finite
relative range and any placement in block 143's class, all as landed: a kept current forces the one-body placement current to
vanish; the resolvent identity [g, T(z)] = (h0 - z)[F2, R''(z)](h0 - z) makes the on-shell T-matrix vanish at almost every energy;
the determinant identity makes the perturbation determinant real on the continuum; bounded spectral densities (block 143 T6)
make it identically one; the removed on-site states make it vanish at their energy, a contradiction. The analytic steps are
proved in the note from named standard theorems; this runner checks the algebraic steps and the landed inputs exactly (a harvest
of probe #9251, same model family, line-checked by the supervisor; not adopted).

B (the one-body lemma): the double-commutator identity and the partial trace.
C (the resolvent identity): the operator identity and its shell sandwich, in an exact finite model with [j'', h''] = 0.
D (the determinant): push-through, the determinant product, the determinant identity with Gamma = B B*, and conjugation.
E (block 143's inputs): T1's minor at its rational point and T6's cone tilts, recomputed.
H (the removed states): Delta(z) = det(h'' - z)/det(h0 - z) and Delta(lambda) = 0 when a state is placed at lambda.
Exact rational, Gaussian-rational and symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp
from sympy import QQ_I
from sympy.polys.matrices import DomainMatrix


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_NO_FINITE_RANGE_INTERACTION_KEEPS_TWO_EXCLUDED_RECORDS_TOTAL_ENERGY_CURRENT_ON_THE_PLANE_OR_IN_SPACE_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_no_finite_range_interaction_keeps_two_excluded_records_total_energy_current_on_the_plane_or_in_space_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "double_commutator_factor_forged": "B",
    "shell_factor_dropped": "C",
    "determinant_weight_dropped": "D",
    "cone_tilt_forged": "E",
    "removed_state_restored": "H",
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
I = sp.I
SX, SY, SZ = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])


def dot_sigma(v):
    return v[0] * SX + v[1] * SY + v[2] * SZ


def dm(matrix):
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(QQ_I)


def eye(n):
    return DomainMatrix.eye(n, QQ_I)


def scal(z, n):
    return eye(n) * QQ_I.from_sympy(sp.sympify(z))


def dagger(M):
    return dm(M.to_Matrix().H)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, one record per site, the interaction and the placement are supplied; the memo does not define a time metric)")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    h = sp.symbols("h1:4", real=True)
    f = sp.symbols("f1:4", real=True)
    H, Fm = dot_sigma(h), dot_sigma(f)
    double = sp.expand(H * (H * Fm - Fm * H) - (H * Fm - Fm * H) * H)
    hh = sum(x ** 2 for x in h)
    hf = sum(a * b for a, b in zip(h, f))
    factor = 2 if mut("double_commutator_factor_forged") else 4
    target = dot_sigma([factor * (hh * f[i] - hf * h[i]) for i in range(3)])
    cross = sp.Matrix(h).cross(sp.Matrix(f))
    single = sp.expand(H * Fm - Fm * H)
    perp = [sp.expand(hh * f[i] - hf * h[i] + (sp.Matrix(h).cross(cross))[i]) for i in range(3)]
    ok = (sp.expand(double - target) == sp.zeros(2, 2) and sp.expand(single - 2 * I * dot_sigma(list(cross))) == sp.zeros(2, 2)
          and all(p == 0 for p in perp))
    checks.check("B1", ok, "one record: [h.s,[h.s,f.s]] = 4(|h|^2 f - (h.f)h).s = -4(h x (h x f)).s and [h.s, f.s] = 2i(h x f).s, so the double commutator vanishes iff h x f = 0 iff the single one does")
    X = sp.Matrix(2, 2, sp.symbols("x0:4"))
    Y = sp.Matrix(2, 2, sp.symbols("y0:4"))
    Xt, Yt = X - X.trace() / 2 * sp.eye(2), Y - Y.trace() / 2 * sp.eye(2)
    S = sp.kronecker_product(Xt, sp.eye(2)) + sp.kronecker_product(sp.eye(2), Yt)
    ptr = sp.Matrix(2, 2, lambda i, j: S[2 * i, 2 * j] + S[2 * i + 1, 2 * j + 1])
    checks.check("B2", sp.expand(ptr - 2 * Xt) == sp.zeros(2, 2), "two records: for traceless one-record parts the partial trace of A (x) 1 + 1 (x) B over the second record is 2A, so a vanishing sum forces A = B = 0")


# ============================================================================================ families C, D: an exact finite model
N_MODEL = 6
E0 = [Fr(1, 2), Fr(1, 2), Fr(-3, 4), Fr(5, 3), Fr(-2, 7), Fr(9, 5)]          # a degenerate pair at E = 1/2
GV = [Fr(3, 5), Fr(-4, 5), Fr(1, 3), Fr(2, 9), Fr(-1, 6), Fr(7, 8)]          # g differs on the pair


def model():
    h0 = dm(sp.diag(*[sp.Rational(x.numerator, x.denominator) for x in E0]))
    g = dm(sp.diag(*[sp.Rational(x.numerator, x.denominator) for x in GV]))
    A = dm(sp.Matrix([[1, 0], [2, 1], [0, -1], [1, 3], [-1, 1], [2, -2]]) + I * sp.Matrix([[0, 1], [1, 0], [2, 0], [0, 0], [1, -1], [0, 1]]))
    W = dm(sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 5) + I / 7], [sp.Rational(1, 5) - I / 7, sp.Rational(-1, 2)]]))
    F1 = A * W * dagger(A)
    h2 = h0 + F1
    j2 = h2 * h2 + h2 * QQ_I(3)                    # a function of h'', so [j'', h''] = 0
    F2 = j2 - g
    return h0, g, A, W, F1, h2, j2, F2


def family_c(checks: Checks) -> None:
    h0, g, A, W, F1, h2, j2, F2 = model()
    n = N_MODEL
    commute = h2 * j2 == j2 * h2 and h0 * g == g * h0
    ok = commute
    for z in (sp.Rational(1, 3) + I / 2, sp.Rational(-5, 4) + 2 * I):
        R0, R2 = (h0 - scal(z, n)).inv(), (h2 - scal(z, n)).inv()
        T = F1 - F1 * R2 * F1
        hz = h0 - scal(z, n)
        lhs = g * T - T * g
        rhs = hz * (F2 * R2 - R2 * F2) if mut("shell_factor_dropped") else hz * (F2 * R2 - R2 * F2) * hz
        ok = ok and lhs == rhs and R2 == R0 - R0 * T * R0
    E, eta = sp.Rational(1, 2), sp.Rational(1, 3)
    z = E + I * eta
    R2 = (h2 - scal(z, n)).inv()
    T = (F1 - F1 * R2 * F1).to_Matrix()
    side = (F2 * R2 * F1 - F1 * R2 * F2).to_Matrix()
    a, b = 0, 1
    left = (sp.Rational(GV[b].numerator, GV[b].denominator) - sp.Rational(GV[a].numerator, GV[a].denominator)) * T[b, a]
    right = I * eta * side[b, a]
    ok = ok and sp.expand(left - right) == 0 and sp.expand(left) != 0
    checks.check("C1", ok, "exact finite model (6 states, rank-2 F1, j'' a function of h'', [h0, g] = 0): R'' = R0 - R0 T R0 and [g, T(z)] = (h0 - z)[F2, R''(z)](h0 - z) at two complex z; on an h0-degenerate pair at z = E + i eta, (g_b - g_a) T_ba = i eta (F2 R'' F1 - F1 R'' F2)_ba, nonzero at eta = 1/3")


def family_d(checks: Checks) -> None:
    h0, g, A, W, F1, h2, j2, F2 = model()
    n = N_MODEL
    z = sp.Rational(2, 5) + I * sp.Rational(3, 4)
    R0, R2 = (h0 - scal(z, n)).inv(), (h2 - scal(z, n)).inv()
    Ad = dagger(A)
    Q0, Q2 = Ad * R0 * A, Ad * R2 * A
    T = F1 - F1 * R2 * F1
    push = T == A * W * (eye(2) + Q0 * W).inv() * Ad
    detprod = (eye(2) + W * Q0).det() * (eye(2) - W * Q2).det() == QQ_I(1)
    zb = sp.conjugate(z)
    Q0b = Ad * (h0 - scal(zb, n)).inv() * A
    d_z = QQ_I.to_sympy((eye(2) + W * Q0).det())
    d_zb = QQ_I.to_sympy((eye(2) + W * Q0b).det())
    conj_ok = sp.expand(d_zb - sp.conjugate(d_z)) == 0
    c = sp.Symbol("c")
    Wm = W.to_Matrix()
    Qg = sp.Matrix([[sp.Rational(1, 3) + I / 4, sp.Rational(-2, 5)], [sp.Rational(1, 7), sp.Rational(-1, 2) - I / 3]])
    Bm = sp.Matrix([[1, sp.Rational(1, 2)], [0, 2]]) + I * sp.Matrix([[0, 1], [1, 0]])
    Gam = Bm * Bm.H
    M = (sp.eye(2) + Qg * Wm).inv() if mut("determinant_weight_dropped") else Wm * (sp.eye(2) + Qg * Wm).inv()
    syl = sp.expand((sp.eye(2) + Wm * (Qg - c * Gam)).det() - (sp.eye(2) + Wm * Qg).det() * (sp.eye(2) - c * Bm.H * M * Bm).det()) == 0
    checks.check("D1", push and detprod and conj_ok and syl,
                 "T = A W (1 + Q0 W)^-1 A* with Q0 = A* R0 A; det(1 + W Q0) det(1 - W Q'') = 1; Delta(conj z) = conj Delta(z); and det(1 + W(Q - c Gamma)) = det(1 + W Q) det(1 - c B* M B) for Gamma = B B* and M = W(1 + Q W)^-1, identically in c")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    k1 = [(Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(20, 29), Fr(21, 29))]
    k2 = [(Fr(8, 17), Fr(15, 17)), (Fr(7, 25), Fr(24, 25)), (Fr(9, 41), Fr(40, 41))]
    sin_sum = k1[0][0] * k2[0][1] + k1[0][1] * k2[0][0]
    sin_dif = k1[0][0] * k2[0][1] - k1[0][1] * k2[0][0]
    dg1 = -2 * sin_sum * sin_dif
    e1sq = sum(s * s for s, _ in k1)
    e2sq = sum(s * s for s, _ in k2)
    t1 = 2 * k1[1][0] * k1[1][1]
    t2 = 2 * k2[1][0] * k2[1][1]
    minor_ok = dg1 != 0 and t1 * t1 * e2sq != t2 * t2 * e1sq

    def tilt(tans):
        s2 = [t * t / (1 + t * t) for t in tans]
        c2 = [1 / (1 + t * t) for t in tans]
        return sum((a * b for a, b in zip(s2, c2)), Fr(0)) / sum(s2, Fr(0))
    tp, ts = tilt([Fr(5, 6), Fr(18, 5)]), tilt([Fr(5, 6), Fr(18, 5), Fr(1, 2)])
    want_p = Fr(139761000, 606502321) if not mut("cone_tilt_forged") else Fr(1, 2)
    checks.check("E1", minor_ok and tp == want_p and ts == Fr(2653455542, 8714332815) and tp < 1 and ts < 1,
                 f"block 143's inputs recomputed: T1's minor dg1/dq1 = {dg1} with dE/dq2 nonzero for all four band pairs; T6's cone tilts {tp} (plane) and {ts} (space), both below one")


# ============================================================================================ family H
def family_h(checks: Checks) -> None:
    m = 5
    h0 = dm(sp.Matrix(m, m, lambda i, j: sp.Rational(1, 2) if abs(i - j) == 1 else 0))
    lam = 3
    Pi0 = sp.zeros(m, m)
    Pi0[2, 2] = 1
    if mut("removed_state_restored"):
        h2 = h0
    else:
        P = sp.eye(m) - Pi0
        h2 = dm(P * h0.to_Matrix() * P + lam * Pi0)
    F1 = h2 - h0
    outside = (h0 - scal(lam, m)).det() != QQ_I(0)
    ratio_ok = True
    for z in (sp.Rational(1, 3) + I, sp.Rational(-7, 5) + I / 2, sp.Rational(2, 1) + 3 * I):
        delta = (eye(m) + (h0 - scal(z, m)).inv() * F1).det()
        ratio_ok = ratio_ok and delta * (h0 - scal(z, m)).det() == (h2 - scal(z, m)).det()
    at_lam = (eye(m) + (h0 - scal(lam, m)).inv() * F1).det() == QQ_I(0)
    checks.check("H1", outside and ratio_ok and at_lam,
                 "a removed state placed at lambda = 3, outside the free spectrum of a five-site chain: Delta(z) = det(1 + R0(z) F1) = det(h'' - z)/det(h0 - z) at three complex z, and Delta(lambda) = 0")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54, 78, 121, 137, 140 and 143 as landed on main (the walk, one record per site, the exclusion's compression, the placement class, the two-step momentum and the shell geometry); it proves that no finite-range interaction keeps two excluded records' total energy current on the plane or in space; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Kato", "Rosenblum", "Ruelle", "Amrein", "Georgescu", "Enss", "Lebesgue", "Levinson", "Birman", "Krein",
                   "Schwarz", "Liouville", "Morse", "Fredholm", "Sylvester", "Paley", "Wiener", "Riesz", "Fatou", "Poussin", "Hardy", "Cauchy", "Borel", "Hölder", "Holder",
                   "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Fourier", "Taylor", "Green", "Pauli", "Hamilton", "Wigner", "Bloch", "Schrodinger", "Riemann", "Hilbert")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem", phrase + "\n\n## Theorem", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem — no finite-range interaction keeps the current", "## Theorem — no finite-range interaction keeps the current (after Einstein)", 1)
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
    "per_element: executed - the one-record double-commutator identity and the two-record partial trace (the one-body lemma)",
    "per_site: executed - the resolvent identity and its shell sandwich in an exact six-state model with a kept current",
    "per_mode: executed - push-through, the determinant product, the determinant identity with Gamma = B B*, and conjugation",
    "per_block: executed - block 143's T1 minor and T6 cone tilts recomputed; the removed state's zero of the determinant on a chain",
    "lattice_wide: checked and not executed - the density, boundary-value and H^2 steps on the torus are proved in the note from named theorems",
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
    family_h(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: two records of the walk under one record per site, on the plane or in space, either exchange sign; any bounded hermitian translation-invariant interaction of finite relative range and any placement in block 143 class; the total energy current is not conserved; algebraic steps checked here, analytic steps proved in the note; a harvest of probe 9251 (same family), line-checked by the supervisor, unrefereed; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
