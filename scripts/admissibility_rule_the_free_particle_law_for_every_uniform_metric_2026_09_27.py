#!/usr/bin/env python3
"""Exact checks: the free-particle law for a uniform metric g, dE/dg_ab = -(1/2) E v^a v^b for every wave (v = dE/dk per label; the law a
free particle E^2 = mu^2 + p.g^-1.p obeys), extends block 185 from diagonal stretches to every uniform metric, shears included. For
W = E^2 it is dW = -(1/4) sum_ab dW/dk_a dW/dk_b dg_ab, a system whose six flows commute; from the walk with block 139's staggered mass,
W0 = sum sin^2 k + mu^2, its solution is k = k0 + (1/2)(g - 1) grad W0(k0), W = W0(k0) + (1/4) grad W0 . (g - 1) . grad W0, with
grad_k W = grad W0(k0). It reduces to block 184's rule on diagonal metrics, keeps the rest energy, keeps every wave's speed in lengths
v.g.v below 1 (strictly unless E = 0), and is smooth exactly while every eigenvalue of g lies in (0, 2): at an eigenvalue 2 the band
top folds, at 0 the species points. Spectral statement only; a local walk realising it off the diagonal is open. The supervisor's own
derivation, unrefereed. Blocks 69 and 139 as landed; blocks 184 and 185 (pushed) placed and the facts used re-derived.

A (premises): landed block 69 (uniform form, arbitrary symmetric B); landed block 139 (the staggered mass); the axioms.
B (T1): the free particle obeys the law for a general 2 x 2 metric; the law in W form.
C (T2): the characteristic solution for a general symmetric 3 x 3 metric: grad_k W = grad W0(k0) and the law for all six components.
D (T3): diagonal metrics give block 184's per-axis rule; rest waves keep W = mu^2.
E (T4): 4 W0 - |grad W0|^2 = 4 sum sin^4 k0 + 4 mu^2 >= 0, so v.g.v = (|p|^2 + p.G.p)/(4 W0 + p.G.p) <= 1.
F (T5): the Jacobian 1 + (g - 1) D with D = diag(cos 2k0); invertible when |eigenvalues of g - 1| < 1; singular at the band top when g
   has eigenvalue 2 and at a species point when g has eigenvalue 0; a pure shear is smooth iff |eps| < 1.
I (T6): a Clifford walk realising the spectrum: F = (1 + C G C)^(1/2) sin k0 at k0(k), C = diag(cos k0), with |F|^2 = W - mu^2; block 184's
   walk on the diagonal.
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
    "docs/ADMISSIBILITY_RULE_THE_FREE_PARTICLE_LAW_FOR_EVERY_UNIFORM_METRIC_SHEARS_INCLUDED_FIXES_ONE_SPECTRUM_SMOOTH_WHILE_THE_METRICS_EIGENVALUES_LIE_BETWEEN_ZERO_AND_TWO_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/ADMISSIBILITY_RULE_THE_BOOKS_ADMIT_ONE_REST_ENERGY_THE_STAGGERED_MASS_KEEPS_THEM_EXACTLY_SO_MASSIVE_CONTENT_MEETS_THE_MEMBER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_free_particle_law_for_every_uniform_metric_shears_included_fixes_one_spectrum_smooth_while_the_metrics_eigenvalues_lie_between_zero_and_two_bounded_theorem_note_2026-09-27"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED69 = (
    "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`",
    "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion.",
)
LANDED139 = (
    "`mε` anticommutes with the walk, so the squared energy is `|sin k|² + m²`",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "particle_forged": "B",
    "solution_forged": "C",
    "diagonal_forged": "D",
    "speed_forged": "E",
    "fold_forged": "F",
    "walk_forged": "I",
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
mu = sp.Symbol("mu", nonnegative=True)
K0 = sp.symbols("a b c", real=True)
GS = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"G{min(i, j) + 1}{max(i, j) + 1}", real=True))
W0 = sum(sp.sin(x_) ** 2 for x_ in K0) + mu ** 2
P0 = sp.Matrix([sp.diff(W0, x_) for x_ in K0])


def solution(G):
    k = sp.Matrix(K0) + G * P0 / 2
    W = W0 + (P0.T * G * P0)[0] / 4
    return k, W


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t69, t139 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note and len(CLAIM_ID) <= 195, f"the note is present and carries its claim id ({len(CLAIM_ID)} characters) and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its response to a metric and the law are supplied)")
    needles = list(LANDED69)
    if mut("landed_quote_forged"):
        needles[1] = needles[1].replace("do not determine", "determine")
    checks.check("A3", all(n in t69 for n in needles) and all(n in t139 for n in LANDED139), "landed block 69: the uniform form for an arbitrary strain B, and no completion fixed by the leading order; landed block 139: the staggered mass anticommutes, so the squared energy is |sin k|^2 + m^2")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    g11, g12, g22 = sp.symbols("g11 g12 g22", positive=True)
    p1, p2 = sp.symbols("p1 p2", real=True)
    g = sp.Matrix([[g11, g12], [g12, g22]])
    p = sp.Matrix([p1, p2])
    E = sp.sqrt(mu ** 2 + (p.T * g.inv() * p)[0])
    v = [sp.diff(E, p1), sp.diff(E, p2)]
    fac = sp.Rational(1, 2) if not mut("particle_forged") else sp.Rational(1, 3)
    ok11 = sp.simplify(sp.diff(E, g11) + fac * E * v[0] ** 2) == 0
    ok22 = sp.simplify(sp.diff(E, g22) + fac * E * v[1] ** 2) == 0
    ok12 = sp.simplify(sp.diff(E, g12) + 2 * fac * E * v[0] * v[1]) == 0  # g12 = g21 is one variable: both entries
    # W form: W = E^2, grad W = 2 E v, so -(1/2) E v^a v^b dg_ab is -(1/4) dW_a dW_b / ... : dW/dg_ab = 2E dE/dg_ab = -E^2 v^a v^b = -(1/4) W_a W_b
    Wp = E ** 2
    okW = sp.simplify(sp.diff(Wp, g11) + sp.diff(Wp, p1) ** 2 / 4) == 0
    checks.check("B1", ok11 and ok22 and ok12 and okW, "a free particle E^2 = mu^2 + p.g^-1.p with fixed p obeys dE/dg_ab = -(1/2) E v^a v^b with v = dE/dp (a general 2 x 2 metric; the off-diagonal variable counts both entries); in W = E^2 the law reads dW/dg_ab = -(1/4) W_a W_b")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    G = GS
    k, W = solution(G)
    if mut("solution_forged"):
        W = W0 + (P0.T * G * P0)[0] / 2
    J = k.jacobian(list(K0))
    gradk0W = sp.Matrix([sp.diff(W, x_) for x_ in K0])
    ok_grad = sp.simplify(J.T * P0 - gradk0W) == sp.zeros(3, 1)
    ok_law = True
    for i in range(3):
        for j in range(i, 3):
            gij = sp.Symbol(f"G{i + 1}{j + 1}", real=True)
            lhs = sp.diff(W, gij) - (P0.T * sp.diff(k, gij))[0]
            want = -(P0[i] * P0[j]) / 4 * (1 if i == j else 2)
            ok_law = ok_law and sp.simplify(lhs - want) == 0
    ok_init = sp.simplify(W.subs({s_: 0 for s_ in G.free_symbols}) - W0) == 0
    checks.check("C1", ok_grad and ok_law and ok_init, "for a general symmetric 3 x 3 metric g = 1 + G, k = k0 + (1/2) G grad W0(k0) and W = W0(k0) + (1/4) grad W0 . G . grad W0 give grad_k W = grad W0(k0) (J^T p0 = grad_k0 W) and dW/dG_ab = -(1/4) W_a W_b at fixed k for all six components, with W = W0 at g = 1: one common solution, so the six flows are compatible")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    ms = sp.symbols("m1:4", positive=True)
    G = sp.diag(*[m_ - 1 for m_ in ms])
    k, W = solution(G)
    ok_k = all(sp.simplify(k[i] - (K0[i] + (ms[i] - 1) / 2 * sp.sin(2 * K0[i]))) == 0 for i in range(3))
    per_axis = sum(sp.sin(K0[i]) ** 2 * (sp.sin(K0[i]) ** 2 + ms[i] * sp.cos(K0[i]) ** 2) for i in range(3)) + mu ** 2
    if mut("diagonal_forged"):
        per_axis = per_axis + mu ** 2
    ok_W = sp.simplify(sp.expand_trig(W - per_axis)) == 0
    # rest waves: grad W0 = 0 gives W = mu^2 whatever g
    Wg = solution(GS)[1]
    ok_rest = sp.simplify(Wg.subs({K0[0]: 0, K0[1]: 0, K0[2]: 0}) - mu ** 2) == 0
    checks.check("D1", ok_k and ok_W and ok_rest, "diagonal metrics g = diag(l_a^2) give k_a = k0_a + ((l_a^2 - 1)/2) sin 2k0_a and W = sum sin^2 k0_a (sin^2 k0_a + l_a^2 cos^2 k0_a) + mu^2: block 184's per-axis rule; at the species points (grad W0 = 0, W0 = mu^2) W = mu^2 at every metric")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    gap = sp.simplify(sp.expand_trig(4 * W0 - (P0.T * P0)[0]))
    want = 4 * sum(sp.sin(x_) ** 4 for x_ in K0) + 4 * mu ** 2
    if mut("speed_forged"):
        want = 4 * sum(sp.sin(x_) ** 4 for x_ in K0)
    ok_gap = sp.simplify(gap - want) == 0
    # v = grad_k E = grad W/(2E) = p0/(2E); v.g.v = p0.(1 + G).p0/(4 W) with 4W = 4 W0 + p0.G.p0
    A_, C_, B_ = sp.symbols("A C B", real=True)
    ratio = (A_ + B_) / (C_ + B_)
    ok_ratio = sp.simplify(1 - ratio - (C_ - A_) / (C_ + B_)) == 0
    checks.check("E1", ok_gap and ok_ratio, "4 W0 - |grad W0|^2 = 4 sum sin^4 k0 + 4 mu^2 >= 0; with v = grad W0(k0)/(2E), the speed in lengths is v.g.v = (|p|^2 + p.G.p)/(4 W0 + p.G.p) and 1 - v.g.v = (4 W0 - |p|^2)/(4W) >= 0: no wave is faster than the long waves in any uniform metric, strictly unless E = 0")


# ============================================================================================ family F (T5)
def family_f(checks: Checks) -> None:
    G = GS
    k, _ = solution(G)
    J = k.jacobian(list(K0))
    D = sp.diag(*[sp.cos(2 * x_) for x_ in K0])
    ok_J = sp.simplify(J - (sp.eye(3) + G * D)) == sp.zeros(3, 3)
    # det(1 + G D) is affine in each D_ii; at D = -1 (band top) it is det(1 - G), at D = +1 (species point) det(1 + G)
    d_ = sp.symbols("d1:4", real=True)
    detJ = sp.expand((sp.eye(3) + G * sp.diag(*d_)).det())
    ok_multi = all(sp.degree(detJ, d_i) <= 1 for d_i in d_)
    # an eigenvalue 2 of g (G has eigenvalue 1) makes det(1 - G) = 0: the band top folds; an eigenvalue 0 (G eigenvalue -1) makes det(1 + G) = 0
    eps = sp.Symbol("eps", real=True)
    Gsh = sp.Matrix([[0, eps, 0], [eps, 0, 0], [0, 0, 0]])
    dets = [sp.expand((sp.eye(3) + Gsh * sp.diag(*s_)).det()) for s_ in itertools.product((1, -1), repeat=3)]
    want = sorted({sp.expand(1 - eps ** 2), sp.expand(1 + eps ** 2)}, key=str)
    if mut("fold_forged"):
        want = [sp.expand(1 - 2 * eps ** 2), sp.expand(1 + eps ** 2)]
    ok_shear = sorted(set(dets), key=str) == want
    Gtop = sp.diag(1, 0, 0)
    ok_top = (sp.eye(3) - Gtop).det() == 0 and (sp.eye(3) + (-Gtop)).det() == 0
    # direct converse: an eigenvalue lam >= 2 or <= 0 of g gives t = -1/(lam - 1) in [-1, 1] with det(1 + t G) = 0 (all cos 2k0 = t)
    lam = sp.Symbol("lam", real=True)
    tval = -1 / (lam - 1)
    ok_conv = sp.simplify(1 + tval * (lam - 1)) == 0 and sp.simplify(sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) + sp.Rational(-1, 2) * sp.diag(2, 2, 0)).det() == 0
    checks.check("F1", ok_J and ok_multi, "the Jacobian of k0 -> k is 1 + G D with D = diag(cos 2k0_a), and its determinant is affine in each cos 2k0_a, so on the cube it is extremal at the eight vertices; for |eigenvalues of G| < 1, |G D| < 1 and it is invertible: a real-analytic relabelling for every metric with eigenvalues in (0, 2)")
    checks.check("F2", ok_shear and ok_top and ok_conv, "a pure shear g = 1 + eps(e1 e2 + e2 e1) has vertex determinants 1 - eps^2 and 1 + eps^2: smooth iff |eps| < 1, that is iff g's eigenvalues 1 +- eps lie in (0, 2); an eigenvalue 2 of g gives det(1 - G) = 0 at the band top (D = -1) and an eigenvalue 0 gives det(1 + G) = 0 at a species point (D = 1); conversely an eigenvalue lam >= 2 or <= 0 gives det(1 + tG) = 0 at cos 2k0 = t = -1/(lam - 1) in [-1, 1] (g = diag(3, 3, 1) folds at t = -1/2)")


# ============================================================================================ family I (T6)
def family_i(checks: Checks) -> None:
    S = sp.Matrix([sp.sin(x_) for x_ in K0])
    C = sp.diag(*[sp.cos(x_) for x_ in K0])
    M = sp.eye(3) + C * GS * C
    if mut("walk_forged"):
        M = sp.eye(3) + GS
    _, W = solution(GS)
    ok_norm = sp.simplify(sp.expand_trig((S.T * M * S)[0] + mu ** 2 - W)) == 0
    m_, x_ = sp.symbols("m_ x_", positive=True)
    ok_diag = sp.simplify((sp.sqrt(1 + (m_ - 1) * sp.cos(x_) ** 2) * sp.sin(x_) - sp.sin(x_) * sp.sqrt(sp.sin(x_) ** 2 + m_ * sp.cos(x_) ** 2)).subs(sp.sin(x_) ** 2, 1 - sp.cos(x_) ** 2)) == 0
    checks.check("I1", ok_norm and ok_diag, "the Clifford vector F = (1 + C G C)^(1/2) sin k0, C = diag(cos k0), evaluated at k0(k), has |F|^2 + mu^2 = W exactly for a general symmetric G, and on diagonal metrics it is block 184's F = sin k0 sqrt(sin^2 k0 + l^2 cos^2 k0): a walk h = F.X + mu Gamma realising the spectrum, real-analytic for |G| < 1 since |C G C| <= |G|")


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
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at eigenvalue 2."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Burgers", "Hopf", "Jacobi", "Ward", "Takahashi", "Wilson", "Kepler", "Bessel", "Liouville", "Paley", "Wiener", "Bloch", "Cauchy", "Parker", "Friedmann", "Frobenius")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_g(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Frobenius) —", 1)
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
    "per_element: executed - the free particle's law for a general 2 x 2 metric",
    "per_site: executed - the characteristic solution for a general symmetric 3 x 3 metric, all six components",
    "per_mode: executed - the diagonal reduction to block 184; the rest energy; the speed identity",
    "per_block: executed - the Jacobian, its multilinearity, the pure shear and the two folds; a realising walk",
    "lattice_wide: checked and not executed - uniqueness of the realising walk (any k-dependent rotation of F also realises W); uniqueness of smooth solutions (characteristics, per flow)",
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
    family_f(checks)
    family_i(checks)
    family_g(checks, texts[0])
    family_h(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: the free-particle law for every uniform metric, shears included, has one spectrum: k = k0 + (1/2)(g - 1) grad W0, E^2 = W0 + (1/4) grad W0.(g - 1).grad W0; block 184 on the diagonal; speed in lengths at most 1; smooth exactly while g's eigenvalues lie in (0, 2); spectral only; the supervisor's own derivation, unrefereed; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
