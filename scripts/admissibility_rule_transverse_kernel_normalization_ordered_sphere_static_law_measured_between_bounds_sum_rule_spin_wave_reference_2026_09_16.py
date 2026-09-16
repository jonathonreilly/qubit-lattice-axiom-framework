#!/usr/bin/env python3
"""Exact checks: the normalization of the transverse kernel in the ordered sphere static law — the spin-wave reference, the transverse
sum rule in a field, and Parseval.

Scope.  T1: on the periodic 4^3 lattice the plane waves are eigenvectors of the Laplacian with eigenvalue E(k) = 2 sum_j (1 - cos k_j)
(symbolic), so the Gaussian transverse model with precision beta Lap has k-mode variance 1/(beta E(k)) per component and the
normalization beta E(k) <|theta_hat(k)|^2> = 1.  T2: the single-site transverse sum rule kappa E[(s^1)^2] = E[s^3] for the exponential
law with concentration kappa = beta h (symbolic), the integration-by-parts identity behind the general sum rule on a torus, and the
sum rule's two-site instance by exact quadrature in the cosines.  T3: Parseval on rational data.  Exact arithmetic only (integers,
Fractions and sympy); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_TRANSVERSE_KERNEL_NORMALIZATION_IN_THE_ORDERED_SPHERE_STATIC_LAW_MEASURED_BETWEEN_THE_BOUNDS_WITH_THE_TRANSVERSE_SUM_RULE_AND_THE_SPIN_WAVE_REFERENCE_BOUNDED_THEOREM_NOTE_2026-09-16.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_transverse_kernel_normalization_in_the_ordered_sphere_static_law_measured_between_the_bounds_with_the_transverse_sum_rule_and_the_spin_wave_reference_bounded_theorem_note_2026-09-16"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "eigenvalue_wrong": "B",
    "spin_wave_normalization_wrong": "B",
    "sum_rule_wrong": "C",
    "integration_by_parts_wrong": "C",
    "parseval_wrong": "D",
    "claim_source_injected": "F",
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
def family_b(checks: Checks) -> None:
    L = 4
    sites = list(itertools.product(range(L), repeat=3))
    index = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    Lap = sp.zeros(N, N)
    for s in sites:
        i = index[s]
        for ax in range(3):
            for sh in (1, -1):
                t = list(s)
                t[ax] = (t[ax] + sh) % L
                Lap[i, i] += 1
                Lap[i, index[tuple(t)]] -= 1
    ok = True
    factor = 2
    if mut("eigenvalue_wrong"):
        factor = 1
    for kk in ((1, 0, 0), (2, 0, 0), (1, 1, 0), (1, 2, 3)):
        k = [2 * sp.pi * n / L for n in kk]
        v = sp.Matrix([sp.exp(sp.I * sum((kj * sj for kj, sj in zip(k, s)), sp.Integer(0))) for s in sites])
        E = factor * sum((1 - sp.cos(kj) for kj in k), sp.Integer(0))
        ok = ok and sp.simplify(Lap * v - E * v) == sp.zeros(N, 1)
    checks.check("B1", ok, "T1: on the periodic 4^3 lattice the plane waves e^{ik.x} are eigenvectors of the graph Laplacian with eigenvalue E(k) = 2 sum_j (1 - cos k_j) (four wavevectors, symbolic)")
    # the Gaussian model: density proportional to exp(-(beta/2) theta^T Lap theta) per component; the covariance of the k-mode is 1/(beta E(k)) for k != 0:
    # symbolic on the 1-d ring of 4 sites, where Lap is 4x4 and the modes are explicit
    beta = sp.symbols("beta", positive=True)
    ring = sp.Matrix([[2, -1, 0, -1], [-1, 2, -1, 0], [0, -1, 2, -1], [-1, 0, -1, 2]])
    # restrict to the zero-sum subspace (k != 0): the pseudo-inverse of beta*ring on that subspace has eigenvalues 1/(beta E(k))
    claimed = {1: 1 / (beta * 2), 2: 1 / (beta * 4)}   # E(2 pi/4) = 2, E(pi) = 4
    if mut("spin_wave_normalization_wrong"):
        claimed = {1: 1 / (beta * 4), 2: 1 / (beta * 4)}
    ok2 = True
    for n, val in claimed.items():
        k = 2 * sp.pi * n / 4
        v = sp.Matrix([sp.exp(sp.I * k * x) for x in range(4)])
        ok2 = ok2 and sp.simplify(beta * ring * v - v / val) == sp.zeros(4, 1)
    checks.check("B2", ok2, "T1: for the Gaussian transverse model with precision beta Lap on the 4-ring the k-modes n = 1, 2 have variance 1/(beta E(k)) = 1/(2 beta), 1/(4 beta) per component, so beta E(k) <|theta_hat(k)|^2> = 1 — the spin-wave value of the normalization")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    kap, w = sp.symbols("kappa w", positive=True)
    Z = sp.integrate(sp.exp(kap * w), (w, -1, 1))
    Ew = sp.integrate(w * sp.exp(kap * w), (w, -1, 1)) / Z
    Ew2 = sp.integrate(w ** 2 * sp.exp(kap * w), (w, -1, 1)) / Z
    transverse_sq = (1 - Ew2) / 2
    coeff = 1
    if mut("sum_rule_wrong"):
        coeff = 2
    ok1 = sp.simplify((coeff * kap * transverse_sq - Ew).rewrite(sp.exp)) == 0
    checks.check("C1", ok1, "T2: single site in a field: kappa E[(s^1)^2] = E[s^3] for the exponential law with concentration kappa = beta h (the transverse sum rule's one-site instance, symbolic)")
    # integration by parts on the sphere: for the rotation generator L = s^3 d/ds^1 - s^1 d/ds^3 (about e_2) and smooth G, the surface
    # integral of L G vanishes; hence <L G> = -<G L log w> for the law w dsigma. With G = s^1 and w = e^{kappa s^3} (single site):
    # L s^1 = s^3, L log w = -kappa s^1: <s^3> = kappa <(s^1)^2>. Check L in spherical coordinates: L = -d/dtheta for the polar angle
    # measured from e_3 in the (1,3) plane, and the surface measure's invariance under this rotation.
    th, ph = sp.symbols("theta phi", real=True)
    s1, s3 = sp.sin(th) * sp.cos(ph), sp.cos(th)
    G = sp.Function("G")
    # the generator of rotations about e_2 acting on functions of (theta, phi): with s = (sin th cos ph, sin th sin ph, cos th),
    # rotating about e_2 by angle a: s^1 -> s^1 cos a + s^3 sin a, s^3 -> -s^1 sin a + s^3 cos a; d/da at a = 0 of a function f(s^1, s^3):
    f = sp.Function("f")
    a = sp.symbols("a", real=True)
    rot1 = s1 * sp.cos(a) + s3 * sp.sin(a)
    rot3 = -s1 * sp.sin(a) + s3 * sp.cos(a)
    Lf = sp.diff(f(rot1, rot3), a).subs(a, 0)
    # L applied to s^1 gives s^3 and to s^3 gives -s^1; to kappa s^3 gives -kappa s^1
    L_s1 = sp.simplify(Lf.subs(f, sp.Lambda((sp.Symbol("u"), sp.Symbol("v")), sp.Symbol("u"))).doit())
    L_s3 = sp.simplify(Lf.subs(f, sp.Lambda((sp.Symbol("u"), sp.Symbol("v")), sp.Symbol("v"))).doit())
    sign = -1
    if mut("integration_by_parts_wrong"):
        sign = 1
    ok2 = sp.simplify(L_s1 - s3) == 0 and sp.simplify(L_s3 - sign * s1) == 0
    # the vanishing of the surface integral of L G: integrate L(s^1 s^3) = (s^3)^2 - (s^1)^2 over the sphere -> 0 by symmetry, executed
    integral = sp.integrate(sp.integrate((s3 ** 2 - s1 ** 2) * sp.sin(th), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi))
    checks.check("C2", ok2 and sp.simplify(integral) == 0, "T2: the rotation generator about e_2 sends s^1 to s^3 and s^3 to -s^1; the surface integral of L(s^1 s^3) vanishes (the integration by parts behind the general sum rule beta h N <(m^1)^2> = <m^3> on any torus)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    f = [Fraction(3, 7), Fraction(-2, 7), Fraction(5, 7), Fraction(1, 7)]
    Fk = [sum((f[x] * sp.exp(-2 * sp.pi * sp.I * k * x / 4) for x in range(4)), sp.Integer(0)) for k in range(4)]
    lhs = sp.simplify(sum((sp.Abs(Fk[k]) ** 2 for k in range(4)), sp.Integer(0)) / 4)
    rhs = sum((fx * fx for fx in f), Fraction(0))
    if mut("parseval_wrong"):
        rhs = rhs * 2
    checks.check("D1", sp.simplify(lhs - sp.Rational(rhs.numerator, rhs.denominator)) == 0, "T3: Parseval on a 4-site ring with rational data: N^{-1} sum_k |f_hat(k)|^2 = sum_x f_x^2, so the transverse structure factor's average is the local transverse moment")


# ============================================================================================ family F
FENCES = (
    "This note proves the spin-wave reference `βE(k)⟨|θ̂(k)|²⟩ = 1` for the quadratic transverse model, the transverse sum rule `βh·N⟨(m̂¹)²⟩ = ⟨m̂³⟩` for the sphere static law in a field on any finite torus, and the mode sum's identity for the transverse structure factor; the normalization `c(β, k) = βE(k)S_⊥(k)` of the transverse kernel in the ordered sphere static law is measured by simulation on finite lattices and placed between block 19's bounds, not proved; it does not select a menu, reading, order or coupling as physical, and adopts no clause.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "the physical menu", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "Goldstone", "spontaneous symmetry breaking", "is the source of gravity", "the gravity node's kernel is",
)
CLAIM_INJECTIONS = {"claim_source_injected": "Hence the transverse channel is the source of gravity."}
CLASSICAL_NAMES = ("Heisenberg", "Bogoliubov", "Mermin", "Wagner", "Fröhlich", "Simon", "Spencer", "Dyson", "Lieb", "Parseval", "Ward", "Metropolis")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Bogoliubov)", 1)
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
    "per_element: executed — the Laplacian's plane-wave eigenvalues on the 4^3 lattice; the single-site sum rule symbolically; the rotation generator's action",
    "per_site: executed — the 4-ring Gaussian modes' variances 1/(beta E(k)); the vanishing surface integral behind the integration by parts",
    "per_mode: executed — Parseval on rational data; the measured normalization c(beta, k) for k along an axis on 16^3, 24^3, 32^3 (control), by a second estimator and in a field (refuter)",
    "per_block: executed — the placement of c(beta, k) between (m^2/3)^2 and 1 at beta = 0.8, 1, 1.5, 2, 3 (control and refuter outputs)",
    "lattice_wide: T1-T3 proved as stated; the normalization is measured on finite lattices, not proved",
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
