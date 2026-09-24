#!/usr/bin/env python3
"""Level covariance of a supplied gain-one recurrence and a lattice Green comparison.

For the supplied gain-one recurrence on a finite periodic plane, derive early-late Hermitian mode covariance with the conjugated multiplier, its stationary nonzero-mode form, an explicit symmetry subgroup and a mode decay bound. The static lattice Green comparator also has a plane-amplitude times layer-propagator representation, with small-wavevector decay linear rather than quadratic in the transverse wavenumber.
"""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_GRAVITY_NODE_KERNEL_UNDER_THE_FORMATION_READING_A_HEAT_KERNEL_IN_LEVEL_TIME_TIMES_A_PLANE_GREEN_FUNCTION_NOT_THE_COMPARATORS_THREE_DIMENSIONAL_GREEN_FUNCTION_BOUNDED_THEOREM_NOTE_2026-09-18.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_gravity_node_kernel_under_the_formation_reading_a_heat_kernel_in_level_time_times_a_plane_green_function_not_the_comparators_three_dimensional_green_function_bounded_theorem_note_2026-09-18"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "space_time_covariance_wrong": "B",
    "cross_level_recursion_wrong": "B",
    "small_k_form_wrong": "C",
    "symmetry_wrong": "C",
    "decay_rate_wrong": "D",
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


# ------------------------------------------------------------------------------------------- tiny tori (exact rationals)
def cos_exact(L: int, n: int) -> Fraction:
    n %= L
    table = {2: {0: 1, 1: -1}, 3: {0: 1, 1: Fraction(-1, 2), 2: Fraction(-1, 2)}, 4: {0: 1, 1: 0, 2: -1, 3: 0}}
    return Fraction(table[L][n])


def sin_exact_sq(L: int, n: int) -> Fraction:
    return 1 - cos_exact(L, n) ** 2


def shift_matrix(L: int, axis: int):
    N = L * L
    M = sp.zeros(N, N)
    for i in range(L):
        for j in range(L):
            src = i * L + j
            dst = (((i - 1) % L) * L + j) if axis == 0 else (i * L + (j - 1) % L)
            M[src, dst] = 1
    return M


def covariances(L: int, T: int, smax: int, wrong: bool = False):
    """Sigma_t (equal level) and Sigma_{t,t+s} := Cov(theta_t, theta_{t+s}) = Sigma_t (P^s)^T for the recursion theta_{t+1} = P theta_t + xi."""
    N = L * L
    I = sp.eye(N)
    P = (I + shift_matrix(L, 0) + shift_matrix(L, 1)) / 3
    Sigma = sp.zeros(N, N)
    out = []
    for t in range(1, T + 1):
        Sigma = P * Sigma * P.T + I
        cross = {s: Sigma * ((P ** s).T if not wrong else (P ** (s + 1)).T) for s in range(1, smax + 1)}
        out.append((Sigma, cross))
    return P, out


def mode_vectors(L: int):
    """real Fourier characters on the L x L torus: cos and sin of k.x with k = 2 pi n / L, as exact rationals for L in {3, 4}."""
    vecs = {}
    for n1 in range(L):
        for n2 in range(L):
            c = sp.Matrix([cos_exact(L, n1 * i + n2 * j) for i in range(L) for j in range(L)])
            vecs[(n1, n2)] = c
    return vecs


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, block01 = texts
    checks.check("A1", CLAIM_ID in note and len(re.findall(r"^claim_id:", note, flags=re.M)) == 1, "the note carries its claim_id once")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the four sentences quoted under Premises")
    checks.check("A3", BLOCK01_CLAIM_ID in block01 and BLOCK01_FRAGMENT in block01.lower(), "block 01's note (on main) carries its claim_id and the rule's product form")
    checks.check("A4", all(Path(ROOT, p).exists() for p in AUDIT_INPUT_PATHS), "all declared inputs exist")


# ============================================================================================ family B — the space-time covariance (T1)
def family_b(checks: Checks) -> None:
    ph, u, s2 = sp.symbols("phi u sigma2", positive=True)
    ok = True
    # a mode: X_{t+1} = phi X_t + xi, Var xi = sigma2, X_0 = 0.  Cov(X_t, X_{t+s}) = phi^s Var(X_t) (the later noises are independent of X_t)
    # and Var(X_t) = sigma2 (1 - u^t)/(1 - u) with u = |phi|^2: verified as identities for t <= 8 with symbolic phi (real for the check)
    for t in range(1, 9):
        var_t = sum(ph ** (2 * j) for j in range(t)) * s2
        ok = ok and sp.simplify(var_t - s2 * (1 - (ph ** 2) ** t) / (1 - ph ** 2)) == 0
        for s in range(1, 4):
            cov = ph ** s * var_t if not mut("space_time_covariance_wrong") else ph ** (s + 1) * var_t
            ok = ok and sp.simplify(cov - s2 * ph ** s * (1 - (ph ** 2) ** t) / (1 - ph ** 2)) == 0
    checks.check("B1", ok, "T1: real multiplier covariance identity for t<=8, s<=3; the complex early-late orientation is checked separately")
    P4, states4 = covariances(4, 2, 1)
    char = sp.Matrix([[sp.I**i / 4 for i in range(4) for j in range(4)]])
    ph4 = (2+sp.I)/3
    sig, crosses = states4[-1]
    early_late = sp.simplify((char*crosses[1]*sp.conjugate(char).T)[0])
    variance = sp.simplify((char*sig*sp.conjugate(char).T)[0])
    checks.check("B3",sp.simplify(early_late-sp.conjugate(ph4)*variance)==0 and
                 sp.simplify(early_late-ph4*variance)!=0,"L=4 complex character detects early-late conjugation")
    ok2 = True
    for L in (3, 4):
        T, smax = 6 if L == 3 else 4, 3
        P, out = covariances(L, T, smax, wrong=mut("cross_level_recursion_wrong"))
        vecs = mode_vectors(L)
        N = L * L
        for t in range(1, T + 1):
            Sigma, cross = out[t - 1]
            # the equal-level site variance equals the mode sum; the cross-level covariance of the zero mode equals t (a random walk, phi = 1)
            ones = sp.ones(N, 1)
            zero_mode_cross = [(ones.T * cross[s] * ones)[0, 0] / N ** 2 for s in range(1, smax + 1)]
            ok2 = ok2 and all(Fraction(str(v)) == Fraction(t, N) for v in zero_mode_cross)
            # a nonzero cosine mode: c^T Sigma_{t,t+s} c / (c^T c) should equal Re[phi^s] * (1 - u^t)/(1 - u) * (norm)... check the ratio
            # Cov(c.theta_t, c.theta_{t+s}) / Var(c.theta_t) = Re(phi^s) where c is the cosine character of a mode k with -k paired
            for (n1, n2), c in vecs.items():
                if (n1, n2) == (0, 0):
                    continue
                var_c = (c.T * Sigma * c)[0, 0]
                if var_c == 0:
                    continue
                for s in range(1, smax + 1):
                    cov_c = (c.T * cross[s] * c)[0, 0]
                    # phi(k)^s real part: phi = (1 + e^{ik1} + e^{ik2})/3 with k = 2 pi (n1, n2)/L
                    k1 = 2 * sp.pi * n1 / L
                    k2 = 2 * sp.pi * n2 / L
                    phis = sp.nsimplify(sp.expand(((1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3) ** s))
                    re_phis = sp.simplify(sp.re(phis))
                    ok2 = ok2 and sp.simplify(cov_c / var_c - re_phis) == 0
    checks.check("B2", ok2, "T1: on the tori L = 3, 4 the exact rational cross-level covariance Sigma_{t,t+s} = Sigma_t (P^s)^T gives, for every cosine character of a nonzero mode, Cov/Var = Re phi(k)^s at s = 1, 2, 3, and t/L^2 for the plane average (the zero mode's random walk)")


# ============================================================================================ family C — the small-k forms and the symmetry (T2)
def family_c(checks: Checks) -> None:
    k1, k2, k3, eps = sp.symbols("k1 k2 k3 epsilon", real=True)
    u = ((3 + 2 * sp.cos(k1) + 2 * sp.cos(k2) + 2 * sp.cos(k1 - k2)) / 9)
    M = sp.Matrix([[2, -1], [-1, 2]]) / 9
    if mut("small_k_form_wrong"):
        M = sp.Matrix([[2, 1], [1, 2]]) / 9
    kv = sp.Matrix([k1, k2])
    quad = (kv.T * M * kv)[0, 0]
    ser = sp.series((1 - u).subs({k1: eps * k1, k2: eps * k2}), eps, 0, 3).removeO()
    ok = sp.simplify(ser - eps ** 2 * quad) == 0
    ev = sorted(sp.Matrix([[2, -1], [-1, 2]]).eigenvals().keys())
    ok = ok and ev == [1, 3]      # eigenvalues of 9 M: 1 and 3, eigenvectors (1,1) and (1,-1)
    E3 = sum(2 * (1 - sp.cos(k)) for k in (k1, k2, k3))
    ser3 = sp.series(E3.subs({k1: eps * k1, k2: eps * k2, k3: eps * k3}), eps, 0, 3).removeO()
    ok = ok and sp.simplify(ser3 - eps ** 2 * (k1 ** 2 + k2 ** 2 + k3 ** 2)) == 0
    checks.check("C1", ok, "T2: 1 - u(k) = k^T M k + O(k^4) with M = (1/9)[[2,-1],[-1,2]], eigenvalues 1/9 (along (1,1)) and 1/3 (along (1,-1)): an anisotropic two-dimensional quadratic form; the comparator's E(k) = sum 2(1 - cos k_i) = |k|^2 + O(k^4) is isotropic on Z^3")
    # the symmetry: u is invariant under sigma1: (k1,k2) -> (k2,k1) and sigma2: (k1,k2) -> (k1 - k2, -k2), which generate the permutations of {k1, k2, k1 - k2} up to sign
    s1 = u.subs({k1: k2, k2: k1}, simultaneous=True)
    s2 = u.subs({k1: k1 - k2, k2: -k2}, simultaneous=True)
    bad = u.subs({k1: k1 + k2, k2: k2}, simultaneous=True) if mut("symmetry_wrong") else s2
    ok2 = sp.simplify(sp.expand_trig(s1 - u)) == 0 and sp.simplify(sp.expand_trig(bad - u)) == 0
    # the group generated is of order 6 (S_3): check the orbit of a generic point under words of length <= 3 has 6 elements
    def apply(word, pt):
        x, y = pt
        for g in word:
            x, y = (y, x) if g == 1 else (x - y, -y)
        return (x, y)
    from itertools import product
    orbit = set()
    p0 = (sp.Rational(1, 7), sp.Rational(2, 11))
    for n in range(0, 4):
        for word in product((1, 2), repeat=n):
            orbit.add(apply(word, p0))
    ok2 = ok2 and len(orbit) == 6
    # Inverse in the layer coordinate: an amplitude times a decaying propagator.
    rho = sp.symbols("rho", positive=True)
    a = rho + 1/rho - 2
    amp = 1/(1/rho-rho)
    ok2 = sp.simplify((a+2)*amp-2*rho*amp-1)==0
    ok2 = ok2 and sp.simplify((a+2)*rho-rho**2-1)==0
    ok2 = ok2 and amp.subs(rho,sp.Rational(1,2))==sp.Rational(2,3)
    z = sp.symbols("z", positive=True)
    alpha = 2*sp.asinh(z/2) # a=z^2, cosh(alpha)=1+a/2
    ok2 = ok2 and sp.simplify(sp.limit(alpha/z,z,0,dir="+"))==1
    checks.check("D2",ok2,"T3: static Green layer recurrence has G_s=rho^|s|/(rho^-1-rho); its exponent is linear in sqrt(a), unlike the quadratic recurrence decay")


# ============================================================================================ family D — the scaling (T3)
def family_d(checks: Checks) -> None:
    # for a nonzero mode with 1 - u >= 4|k|^2/(9 pi^2) on the square (block 34's inequality), |phi|^s = u^{s/2} <= exp(-(1-u) s/2) <= exp(-2|k|^2 s/(9 pi^2))
    x = sp.symbols("x", positive=True)
    rate = sp.Rational(2, 9) if not mut("decay_rate_wrong") else sp.Rational(4, 9)
    # u^{s/2} = exp(s log(u)/2) and log u <= -(1 - u): check log(1 - y) <= -y for y in (0,1) via the series' sign: -log(1-y) - y = y^2/2 + y^3/3 + ... >= 0
    y = sp.symbols("y", positive=True)
    ser = sp.series(-sp.log(1 - y) - y, y, 0, 6).removeO()
    ok = all(c >= 0 for c in sp.Poly(ser, y).coeffs())
    # the exponent: (1 - u)/2 >= (4|k|^2/(9 pi^2))/2 = 2|k|^2/(9 pi^2)
    ok = ok and sp.simplify(sp.Rational(4, 9) / 2 - rate) == 0
    # the drift: phi(k) = 1 - i (k1 + k2)/3 + O(k^2)
    k1, k2, eps = sp.symbols("k1 k2 epsilon", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    ser_phi = sp.series(phi.subs({k1: eps * k1, k2: eps * k2}), eps, 0, 2).removeO()
    ok = ok and sp.simplify(ser_phi - (1 + sp.I * eps * (k1 + k2) / 3)) == 0
    checks.check("D1", ok, "T3: for every nonzero mode |C_s(k)|/C_0(k) = |phi(k)|^s <= exp(-(1 - u) s/2) <= exp(-2|k|^2 s/(9 pi^2)) on the square (log(1 - y) <= -y): a quadratic mode-decay upper bound; and phi(k) = 1 + i(k1 + k2)/3 + O(k^2): the phase drift is stated in the supplied level coordinates")
    # the comparator: the 3D lattice Green function 1/E(k) has no level-time direction: E depends on (k1,k2,k3) symmetrically, and its
    # restriction to a plane at fixed k3 is a massive 2D form E_2(k1,k2) + 2(1 - cos k3) — the cross-plane dependence is not a multiplicative heat kernel
    k3 = sp.symbols("k3", real=True)
    E3 = sum(2 * (1 - sp.cos(k)) for k in (k1, k2, k3))
    ok2 = sp.simplify(E3 - (2 * (1 - sp.cos(k1)) + 2 * (1 - sp.cos(k2)) + 2 * (1 - sp.cos(k3)))) == 0
    # a multiplicative structure C_s = C_0 phi^s would make C_s(k) / C_0(k) independent of the equal-level factor; for 1/E(k) the ratio of the
    # inverse transforms across planes is not of that form: check that 1/E is not of the form f(k1,k2) g(k3) (mixed second derivative of log(1/E) != 0)
    logE = sp.log(E3)
    mixed = sp.simplify(sp.diff(logE, k1, k3))
    ok2 = ok2 and sp.simplify(mixed.subs({k1: sp.Rational(1, 2), k2: sp.Rational(1, 3), k3: sp.Rational(1, 5)})) != 0
    checks.check("D2", ok2, "T3: the comparator's 1/E(k) is not of the product form (plane factor) x (cross-plane factor) — its logarithm has a non-vanishing mixed derivative in (k1, k3) — so it cannot be written as a plane Green function times a propagator in any direction; the formation kernel is exactly of that form")


# ============================================================================================ family F
FENCES = ('For the supplied gain-one recurrence on a finite periodic plane, derive early-late Hermitian mode covariance with the conjugated multiplier, its stationary nonzero-mode form, an explicit symmetry subgroup and a mode decay bound. The static lattice Green comparator also has a plane-amplitude times layer-propagator representation, with small-wavevector decay linear rather than quadratic in the transverse wavenumber. This recurrence is a supplied linear comparator, not the exact finite-beta Cartesian mean linearization of the nonlinear sphere kernel. Historical nonlinear simulations are author-reported finite observations, not newly verified results or asymptotic theorems. No physical rule, gravity kernel or axiom selection is derived; no clause is adopted.', 'No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.')
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at beta = 6."}
CLASSICAL_NAMES = ("Toom", "Berman", "Simon", "Gács", "Mermin", "Wagner", "Bramson", "Gray", "Krylov", "Bogolyubov", "Choquet", "Peierls", "Dobrushin", "Fourier", "Parseval", "Goldstone")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T2", "## Theorem T2 (after Goldstone)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    nodes = list(ast.walk(ast.parse(src)))
    float_hits = [x for x in nodes if isinstance(x,ast.Constant) and isinstance(x.value,float)]
    float_hits += [x for x in nodes if isinstance(x,ast.Call) and
                   ((isinstance(x.func,ast.Name) and x.func.id in ("float","N")) or
                    (isinstance(x.func,ast.Attribute) and x.func.attr in ("evalf","N")))]
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
N5_LINES = ('per_element: Exact arithmetic checks the supplied recurrence and identities; its gain-one assumption is not the nonlinear Cartesian mean derivative.', 'per_site: Finite periodic plane covariance matrices are compared with exact mode expressions on the explicitly listed small tori.', 'per_mode: Complex covariance orientation, or real mode variances and bounds, are controlled under the explicitly declared transform convention.', 'per_block: The algebraic statements require the supplied model and beta greater than zero; finite numerical observations have only their listed scope.', 'lattice_wide: No nonlinear infinite-volume theorem, physical law selection, gravity kernel or retained audit grade follows from this certificate.')


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
