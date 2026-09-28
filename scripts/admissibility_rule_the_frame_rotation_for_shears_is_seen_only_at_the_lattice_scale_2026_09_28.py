#!/usr/bin/env python3
"""Exact checks: block 188's frame rotation (pushed; the part of the walk's response to shear that the stress response does not fix,
a k-dependent rotation of the Clifford vector at fixed energy) is observable only at the lattice scale. (T1) For h' = U h U^dag with
U(k) = exp(-i theta(k) n.sigma/2), the energies, the group velocities and the single-wave currents dE/dk are unchanged. (T2) For the
same state carried by U, the density's pair symbol changes by U(k')^dag U(k) - 1 = -(i/2) q.grad(theta) n.sigma + O(q^2): its first
moment moves by the rotation's connection (1/2) grad(theta) <n.sigma>, while the total and every q = 0 value are unchanged. (T3) Every
rotation angle in block 188 T6's table is (1/4) times a product of cosines times a strain component, so its gradient vanishes at all
eight species points and grows linearly away from them (Hessian at k = 0 for (11)/(12): diag(5/4, 1/4, 0)/... per unit strain): the
shift is proportional to the strain and to the distance from the species point, so it vanishes at long wavelength. The supervisor's
own derivation, unrefereed. Block 69 as landed; block 188 (pushed) placed and the table re-derived.

A (premises): landed block 69; the axioms.
B (T1): spectral and single-wave invariance under a k-dependent coin rotation.
C (T2): the pair-symbol change of the density and its first moment.
D (T3): the table's angles re-derived at two entries; gradients zero at all species points; the Hessian at k = 0.
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
    "docs/ADMISSIBILITY_RULE_THE_FRAME_ROTATION_FOR_SHEARS_IS_SEEN_ONLY_AT_THE_LATTICE_SCALE_IT_MOVES_A_WAVES_DENSITY_BY_A_CONNECTION_THAT_VANISHES_AT_THE_SPECIES_POINTS_BOUNDED_THEOREM_NOTE_2026-09-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_frame_rotation_for_shears_is_seen_only_at_the_lattice_scale_it_moves_a_waves_density_by_a_connection_that_vanishes_at_the_species_points_bounded_theorem_note_2026-09-28"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED69 = (
    "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "spectrum_forged": "B",
    "connection_forged": "C",
    "table_forged": "D",
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
I_ = sp.I
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -I_], [I_, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
KS = sp.symbols("k1:4", real=True)


def rot(theta):
    """U = exp(-i theta sigma_z/2)"""
    return sp.Matrix([[sp.exp(-I_ * theta / 2), 0], [0, sp.exp(I_ * theta / 2)]])


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t69 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note and len(CLAIM_ID) <= 195, f"the note is present and carries its claim id ({len(CLAIM_ID)} characters) and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk's frame is supplied)")
    needles = list(LANDED69)
    if mut("landed_quote_forged"):
        needles[0] = needles[0].replace("B_a^j", "B_j^a")
    checks.check("A3", all(n in t69 for n in needles), "landed block 69: the uniform form of the two-step coupling")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    F = sp.Matrix([sp.Function(f"F{i}")(*KS) for i in range(3)])
    th = sp.Function("theta")(*KS)
    h = F[0] * SX + F[1] * SY + F[2] * SZ
    U = rot(th)
    hp = sp.simplify(U * h * U.H.subs(sp.conjugate(th), th))
    # spectrum: h'^2 = h^2 = |F|^2 (U unitary pointwise), so eigenvalues and group velocities agree
    sq = sp.simplify(hp * hp - h * h)
    ok_spec = sq == sp.zeros(2, 2)
    # the rotated Clifford vector: h' = F'.sigma with F' = R_z(theta) F, |F'| = |F|
    Fp = sp.Matrix([sp.simplify((hp * m).trace() / 2) for m in (SX, SY, SZ)])
    ok_rot = sp.simplify(sum(x ** 2 for x in Fp) - sum(x ** 2 for x in F)) == 0
    if mut("spectrum_forged"):
        ok_rot = sp.simplify(sum(x ** 2 for x in Fp) - sum(x ** 2 for x in F) - 1) == 0
    checks.check("B1", ok_spec and ok_rot, "for h' = U h U^dag with U(k) = exp(-i theta(k) sigma_z/2), h'^2 = h^2 = |F|^2 and h' = (R_theta F).sigma with |R_theta F| = |F|: every energy, and so every group velocity dE/dk and every single-wave current (the q = 0 value of the energy current, E dE/dk), is unchanged")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    th = sp.Function("theta")
    q = sp.symbols("q1:4", real=True)
    kp = [KS[i] - q[i] for i in range(3)]
    t = sp.Symbol("t")
    # U(k')^dag U(k) = exp(-i (theta(k) - theta(k')) sigma_z/2); first order in q along q = t qhat
    d = th(*KS) - th(*[KS[i] - t * q[i] for i in range(3)])
    d1 = sp.simplify(sp.diff(d, t).subs(t, 0))
    grad = sum(q[i] * sp.diff(th(*KS), KS[i]) for i in range(3))
    ok_d = sp.simplify(d1 - grad) == 0
    M = sp.Matrix([[sp.exp(-I_ * d / 2), 0], [0, sp.exp(I_ * d / 2)]])
    lin = sp.simplify(sp.diff(M, t).subs(t, 0))
    want = -I_ / 2 * grad * SZ
    if mut("connection_forged"):
        want = -I_ * grad * SZ
    ok_lin = sp.simplify(lin - want) == sp.zeros(2, 2)
    ok_zero = sp.simplify(M.subs(t, 0) - sp.eye(2)) == sp.zeros(2, 2)
    # connection: A = U^dag i dU/dk_j = (1/2) d_j theta sigma_z
    U = rot(th(*KS))
    A = [sp.simplify(U.H.subs(sp.conjugate(th(*KS)), th(*KS)) * I_ * sp.diff(U, KS[j])) for j in range(3)]
    ok_A = all(sp.simplify(A[j] - sp.diff(th(*KS), KS[j]) / 2 * SZ) == sp.zeros(2, 2) for j in range(3))
    checks.check("C1", ok_d and ok_lin and ok_zero and ok_A, "for the same state carried by U, the density's pair symbol is multiplied by U(k')^dag U(k) = 1 - (i/2) q.grad(theta) sigma_z + O(q^2): unchanged at q = 0 (total and every single-wave value), and at first order in q its first moment moves by the connection U^dag i grad U = (1/2) grad(theta) sigma_z, weighted by the wave's polarisation <sigma_z>")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    c = [sp.cos(x) for x in KS]
    C2 = [sp.cos(2 * x) for x in KS]
    table = [(2, -c[0] * c[1] * C2[0]), (1, c[0] * c[2] * C2[0]), (0, -c[1] * c[2] * C2[0]), (2, -c[0] * c[1] * C2[1]), (1, c[0] * c[2] * C2[1]),
             (2, -c[0] * c[1] * C2[2]), (1, c[0] * c[2] * C2[2]), (0, -c[1] * c[2] * C2[1]), (0, -c[1] * c[2] * C2[2])]
    if mut("table_forged"):
        table[0] = (2, -sp.sin(KS[0]) * c[1] * C2[0])
    ok_grad = True
    for _ax, th in table:
        g = [sp.diff(th / 4, x) for x in KS]
        for corner in itertools.product([0, sp.pi], repeat=3):
            sub = dict(zip(KS, corner))
            ok_grad = ok_grad and all(sp.simplify(gi.subs(sub)) == 0 for gi in g)
    H = sp.hessian(table[0][1] / 4, KS).subs({x: 0 for x in KS})
    ok_h = H == sp.diag(sp.Rational(5, 4), sp.Rational(1, 4), 0)
    # re-derive the (11)/(12) entry of block 188's table from the stress-response flows at the free walk
    F = sp.Matrix([sp.sin(x) for x in KS])

    def W(G):
        return (G.T * G)[0]

    def Phi(G, a, b):
        Wg = W(G)
        if a == b:
            return -sp.Rational(1, 4) * sp.diff(G, KS[a]) * sp.diff(Wg, KS[a])
        return -sp.Rational(1, 4) * (sp.diff(G, KS[a]) * sp.diff(Wg, KS[b]) + sp.diff(G, KS[b]) * sp.diff(Wg, KS[a]))

    e = sp.Symbol("e_")
    D1 = sp.diff(Phi(F + e * Phi(F, 0, 1), 0, 0), e).subs(e, 0)
    D2 = sp.diff(Phi(F + e * Phi(F, 0, 0), 0, 1), e).subs(e, 0)
    e3 = sp.Matrix([0, 0, 1])
    ok_t = sp.simplify(sp.expand_trig(D1 - D2 - (table[0][1] / 4) * e3.cross(F))) == sp.zeros(3, 1)
    checks.check("D1", ok_grad and ok_h and ok_t, "every angle of block 188 T6's table ((1/4) times a product of cosines with one doubled, per unit strain; the (11)/(12) entry re-derived here) has zero gradient at all eight species points, and for (11)/(12) the Hessian at k = 0 is diag(5/4, 1/4, 0): the connection, and so the shift, is proportional to the strain and grows linearly away from each species point")


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
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at the species points."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Burgers", "Hopf", "Jacobi", "Ward", "Takahashi", "Wilson", "Kepler", "Bessel", "Liouville", "Paley", "Wiener", "Bloch", "Cauchy", "Berry", "Zak", "Hellmann", "Feynman")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_g(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Berry) —", 1)
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
    "per_element: executed - spectral invariance under a k-dependent coin rotation",
    "per_site: executed - the pair-symbol change of the density at first order in q; the connection",
    "per_mode: executed - the (11)/(12) entry of block 188's table re-derived",
    "per_block: executed - zero gradients of all nine angles at all eight species points; the Hessian at k = 0",
    "lattice_wide: checked and not executed - higher orders in the strain; rotation axes other than a fixed axis; the member's coupling at the pair level",
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
    family_g(checks, texts[0])
    family_h(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: block 188's frame rotation changes no energy, velocity or single-wave current; it moves a wave's density by the rotation's connection (1/2) grad(theta) <sigma>, which is proportional to the strain and vanishes at all species points; the supervisor's own derivation, unrefereed; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
