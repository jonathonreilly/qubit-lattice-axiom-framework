#!/usr/bin/env python3
"""Exact finite component factors and scoped marginalization diagnostics.
No universal graph-based converse is tested or claimed.

Scope.  Q3(a)-(c): the spectral decomposition of the six-axis product rule phi with explicit eigenvectors; the entry differences of
phi^2 and the constancy criterion p = q = r; the path powers phi^{k+2}, k <= 3.  Q2: the factor of a pendant path of two and of
three unrecorded sites, symbolically in (p, q, r), for all six values of the attachment record.  Q3(e): the sphere factors and the
series positivity of z cosh z - sinh z.  Q4: the abstract square-plus-site diagnostics at three triples, the cube witness, the pendant forest,
and Q1's average identity, all as exact rationals.  E: the two unrecorded corners of a plaquette (entrywise square of phi^2).
Exact arithmetic only (integers, Fractions and sympy); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_FINITE_UNRECORDED_COMPONENT_FACTORIZATION_AND_ATTACHMENT_FACTORS_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_finite_unrecorded_component_factorization_and_attachment_factors_bounded_theorem_note_2026-09-15"
PARENT_CLAIM_ID = "possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14"
PARENT_FRAGMENT = "Empty-neighbourhood sphere laws"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "No possibility is privileged.",
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "A site with no record cannot be read.",
    "A state is a configuration of records.",
)

MUTATION_GATE = {
    "spectral_decomposition_wrong": "B",
    "constancy_criterion_wrong": "B",
    "path_eigenvalue_wrong": "B",
    "one_attachment_nonconstant_claimed": "B",
    "sphere_one_attachment_wrong": "C",
    "sphere_series_sign_wrong": "C",
    "plaquette_tv_wrong": "D",
    "cube_tv_wrong": "D",
    "forest_tv_nonzero_claimed": "D",
    "average_identity_wrong": "D",
    "hadamard_component_constant_claimed": "E",
    "claim_reading_selected_injected": "F",
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
        self.failed_families: list[str] = []

    def check(self, label: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        if not ok:
            self.failed_families.append(label[0])
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize_text(text: str) -> str:
    return " ".join(text.split())


MENU = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def relation(v, w) -> str:
    if v == w:
        return "same"
    if tuple(-c for c in v) == w:
        return "anti"
    return "orth"


def phi_of(v, w, p, q, r):
    return {"same": p, "anti": q, "orth": r}[relation(v, w)]


def phi_matrix(p, q, r):
    return sp.Matrix(6, 6, lambda i, j: phi_of(MENU[i], MENU[j], p, q, r))


def sector_basis():
    odd = [sp.Matrix([1 if k == 2 * i else (-1 if k == 2 * i + 1 else 0) for k in range(6)]) for i in range(3)]
    even = [sp.Matrix([1, 1, -1, -1, 0, 0]), sp.Matrix([0, 0, 1, 1, -1, -1])]
    const = sp.Matrix([1] * 6)
    return const, odd, even


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, parent, block01 = texts
    checks.check("A1", all((ROOT / pth).is_file() for pth in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 4,
                 "the four declared inputs exist (this note, the axiom memo, the possibility-covariance note, block 01's note on main)")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the seven axiom sentences used are present verbatim in the axiom memo")
    fp, f1 = normalize_text(parent), normalize_text(block01)
    checks.check("A3", PARENT_CLAIM_ID in fp and PARENT_FRAGMENT in fp and BLOCK01_CLAIM_ID in f1 and BLOCK01_FRAGMENT in f1,
                 "the parents' claim ids and their sections (the sphere laws; the static law of a product rule) are present")
    flat = normalize_text(note)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    p, q, r = sp.symbols("p q r", positive=True)
    Phi = phi_matrix(p, q, r)
    const, odd, even = sector_basis()
    lam_odd = p - q
    if mut("spectral_decomposition_wrong"):
        lam_odd = p + q
    ok1 = sp.simplify(Phi * const - (p + q + 4 * r) * const) == sp.zeros(6, 1)
    ok1 = ok1 and all(sp.simplify(Phi * f - lam_odd * f) == sp.zeros(6, 1) for f in odd)
    ok1 = ok1 and all(sp.simplify(Phi * g - (p + q - 2 * r) * g) == sp.zeros(6, 1) for g in even)
    checks.check("B1", ok1, "Q3(a): phi has eigenvalue Z1 = p + q + 4r on constants, p - q on the three odd vectors delta_{e_i} - delta_{-e_i}, and p + q - 2r on the two even zero-sum vectors")
    Phi2 = Phi * Phi
    d_same = sp.factor(sp.expand(Phi2[0, 0] - Phi2[0, 2]))
    d_anti = sp.factor(sp.expand(Phi2[0, 1] - Phi2[0, 2]))
    target_same = (p - r) ** 2 + (q - r) ** 2
    if mut("constancy_criterion_wrong"):
        target_same = (p - r) ** 2 - (q - r) ** 2
    ok2 = sp.simplify(d_same - target_same) == 0 and sp.simplify(d_anti - 2 * (p - r) * (q - r)) == 0
    sol = sp.solve([sp.expand(Phi2[0, 0] - Phi2[0, 2]), sp.expand(Phi2[0, 1] - Phi2[0, 2])], [p, q], dict=True)
    ok2 = ok2 and sol == [{p: r, q: r}]
    checks.check("B2", ok2, "Q3(b): phi^2_same - phi^2_orth = (p - r)^2 + (q - r)^2 and phi^2_anti - phi^2_orth = 2 (p - r)(q - r); both vanish iff p = q = r")
    ok3 = True
    for k in range(1, 4):
        Pk = Phi ** (k + 2)
        exp_odd = (p - q) ** (k + 2)
        if mut("path_eigenvalue_wrong"):
            exp_odd = (p - q) ** (k + 1)
        ok3 = ok3 and all(sp.simplify(Pk * f - exp_odd * f) == sp.zeros(6, 1) for f in odd)
        ok3 = ok3 and all(sp.simplify(Pk * g - (p + q - 2 * r) ** (k + 2) * g) == sp.zeros(6, 1) for g in even)
    checks.check("B3", ok3, "Q3(c): a bridging path of k internal bonds contributes phi^{k+2}, with nontrivial eigenvalues (p - q)^{k+2} and (p + q - 2r)^{k+2}, k <= 3")

    def pendant_factor(length: int, vb):
        total = 0
        for u in product(range(6), repeat=length):
            w = phi_of(vb, MENU[u[0]], p, q, r)
            for i in range(length - 1):
                w = w * phi_of(MENU[u[i]], MENU[u[i + 1]], p, q, r)
            total = total + w
        return sp.expand(total)

    ok4 = True
    for length in (2, 3):
        vals = [pendant_factor(length, vb) for vb in MENU]
        same = all(sp.simplify(vals[0] - v) == 0 for v in vals[1:])
        if mut("one_attachment_nonconstant_claimed"):
            same = not same
        ok4 = ok4 and same
    checks.check("B4", ok4, "Q2: the factor of a pendant path of two and of three unrecorded sites is the same polynomial in (p, q, r) for all six values of the attachment record")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    b, t, w, z = sp.symbols("beta t w z", positive=True)
    one = 2 * sp.pi * sp.integrate(sp.exp(b * t), (t, -1, 1))
    target = 4 * sp.pi * sp.sinh(b) / b
    if mut("sphere_one_attachment_wrong"):
        target = 4 * sp.pi * sp.cosh(b) / b
    checks.check("C1", sp.simplify(sp.expand((one - target).rewrite(sp.exp))) == 0, "Q3(e): the one-attachment sphere factor 2 pi int_{-1}^{1} e^{beta t} dt = 4 pi sinh(beta)/beta")
    two = 2 * sp.pi * sp.integrate(sp.exp(b * w * t), (t, -1, 1))
    two_ok = sp.simplify(sp.expand((two - 4 * sp.pi * sp.sinh(b * w) / (b * w)).rewrite(sp.exp))) == 0
    n = sp.symbols("n", positive=True, integer=True)
    coeff = 1 / sp.factorial(2 * n) - 1 / sp.factorial(2 * n + 1)
    closed = sp.simplify(coeff - 2 * n / sp.factorial(2 * n + 1)) == 0
    series = sp.series(z * sp.cosh(z) - sp.sinh(z), z, 0, 24).removeO()
    sign = 1
    if mut("sphere_series_sign_wrong"):
        sign = -1
    pos = all(sign * series.coeff(z, 2 * m + 1) > 0 for m in range(1, 11)) and series.coeff(z, 1) == 0
    checks.check("C2", two_ok and closed and pos, "Q3(e): the two-attachment factor 4 pi sinh(beta w)/(beta w) with w = |v_x + v_y|; z cosh z - sinh z = sum_{n>=1} 2n z^{2n+1}/(2n+1)! has positive coefficients (n <= 10), so sinh z/z increases")


# ============================================================================================ family D
def law(bonds, sites, pqr):
    Z = 0
    wts = {}
    for u in product(range(6), repeat=len(sites)):
        rec = {s: MENU[k] for s, k in zip(sites, u)}
        w = 1
        for a, c in bonds:
            w *= phi_of(rec[a], rec[c], *pqr)
        wts[u] = w
        Z += w
    return {k: Fraction(v, Z) for k, v in wts.items()}


def marginal(lawd, sites, keep):
    idx = [sites.index(s) for s in keep]
    out: dict = {}
    for u, w in lawd.items():
        key = tuple(u[i] for i in idx)
        out[key] = out.get(key, Fraction(0)) + w
    return out


def tv(a, b) -> Fraction:
    keys = set(a) | set(b)
    return sum((abs(a.get(k, Fraction(0)) - b.get(k, Fraction(0))) for k in keys), Fraction(0)) / 2


W4 = ["c0", "c1", "c2", "c3"]
W4B = [("c0", "c1"), ("c1", "c2"), ("c2", "c3"), ("c3", "c0")]


def family_d(checks: Checks) -> None:
    expected = {(3, 1, 2): Fraction(78621, 4563820), (5, 2, 4): Fraction(675203620, 64463986907), (2, 1, 2): Fraction(221667, 30063356)}
    if mut("plaquette_tv_wrong"):
        expected[(3, 1, 2)] = Fraction(78621, 4563821)
    ok1 = True
    for pqr, ex in expected.items():
        R1 = law(W4B, W4, pqr)
        R2 = marginal(law(W4B + [("c0", "x"), ("c1", "x")], W4 + ["x"], pqr), W4 + ["x"], W4)
        d = tv(R1, R2)
        ok1 = ok1 and d == ex and d > 0
    checks.check("D1", ok1, "Q4(a): the abstract square-plus-vertex graph with a triangle (not a cubic-lattice fixture): TV(R1, R2) = 78621/4563820, 675203620/64463986907, 221667/30063356 at (3,1,2), (5,2,4), (2,1,2), exactly")
    pqr = (3, 1, 2)
    R1 = law(W4B, W4, pqr)
    # cube: bottom face c0..c3 recorded, top face t0..t3 unrecorded, with the vertical bonds; the top-face factor summed per bottom configuration
    top_configs = list(product(range(6), repeat=4))
    top_weight = {}
    for tcfg in top_configs:
        w = 1
        for i in range(4):
            w *= phi_of(MENU[tcfg[i]], MENU[tcfg[(i + 1) % 4]], *pqr)
        top_weight[tcfg] = w
    num = {}
    Z = 0
    for bcfg in top_configs:
        wb = 1
        for i in range(4):
            wb *= phi_of(MENU[bcfg[i]], MENU[bcfg[(i + 1) % 4]], *pqr)
        f = 0
        for tcfg, wt in top_weight.items():
            wv = wt
            for i in range(4):
                wv *= phi_of(MENU[bcfg[i]], MENU[tcfg[i]], *pqr)
            f += wv
        num[bcfg] = wb * f
        Z += wb * f
    R2c = {k: Fraction(v, Z) for k, v in num.items()}
    ex_cube = Fraction(9778807, 1312253264)
    if mut("cube_tv_wrong"):
        ex_cube = Fraction(9778807, 1312253265)
    checks.check("D2", tv(R1, R2c) == ex_cube, "Q4(b): the cube with its top face unrecorded (a four-cycle touching all four recorded sites): TV(R1, R2) = 9778807/1312253264 at (3,1,2), exactly")
    pend = [("c0", "p1"), ("p1", "p2"), ("c2", "p3")]
    sites = W4 + ["p1", "p2", "p3"]
    R1f = law(W4B, W4, (2, 1, 2))
    R2f = marginal(law(W4B + pend, sites, (2, 1, 2)), sites, W4)
    d = tv(R1f, R2f)
    cond = d == 0
    if mut("forest_tv_nonzero_claimed"):
        cond = d > 0
    checks.check("D3", cond, "Q4(c)/Q2: the plaquette with a pendant path of two sites off one corner and a pendant site off the opposite corner: TV(R1, R2) = 0 exactly at (2,1,2)")
    joint = law(W4B + [("c0", "x"), ("c1", "x")], W4 + ["x"], (3, 1, 2))
    R2 = marginal(joint, W4 + ["x"], W4)
    mix: dict = {}
    for xval in range(6):
        block = {k[:4]: v for k, v in joint.items() if k[4] == xval}
        mass = sum(block.values(), Fraction(0))
        weight = mass
        if mut("average_identity_wrong"):
            weight = Fraction(xval + 1, 21)  # a non-uniform reweighting of the exterior records (the true marginal is uniform by Q2's symmetry)
        for k, v in block.items():
            mix[k] = mix.get(k, Fraction(0)) + weight * (v / mass)
    checks.check("D4", all(mix.get(k, Fraction(0)) == R2[k] for k in R2), "Q1: on the abstract square-plus-vertex diagnostic, mu_W^R2 equals the average of the exterior-records laws mu_W^R3(.|omega) weighted by the exterior's marginal law, exactly")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    p, q, r = sp.symbols("p q r", positive=True)
    Phi = phi_matrix(p, q, r)
    Phi2 = Phi * Phi
    H = sp.Matrix(6, 6, lambda i, j: Phi2[i, j] ** 2)  # two single-site components on the same pair: the entrywise square
    const, odd, even = sector_basis()
    lam_odd = sp.simplify((odd[0].T * H * odd[0])[0, 0] / (odd[0].T * odd[0])[0, 0])
    lam_even = sp.simplify((even[0].T * H * even[0])[0, 0] / (even[0].T * even[0])[0, 0])
    both_zero_generic = sp.simplify(lam_odd.subs({p: 3, q: 1, r: 2})) == 0 and sp.simplify(lam_even.subs({p: 3, q: 1, r: 2})) == 0
    at_constant = sp.simplify(lam_odd.subs({p: 1, q: 1, r: 1})) == 0 and sp.simplify(lam_even.subs({p: 1, q: 1, r: 1})) == 0
    covariant = all(sp.simplify(H * f - lam_odd * f) == sp.zeros(6, 1) for f in odd) and all(sp.simplify(H * g - lam_even * g) == sp.zeros(6, 1) for g in even)
    cond = covariant and at_constant and not both_zero_generic
    if mut("hadamard_component_constant_claimed"):
        cond = covariant and both_zero_generic
    checks.check("E1", cond, "Q3(d): the two unrecorded corners of a plaquette contribute the entrywise square of phi^2, a covariant matrix with sector eigenvalues that vanish at p = q = r and not at (3,1,2)")


# ============================================================================================ family F
FENCES = ('This note proves finite component factorization, conditional averaging, at-most-one-attachment constancy, scoped bridge and path factors, and named finite graph witnesses for supplied positive static models; it does not prove a universal graph-based equivalence or select a physical reading.', 'No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'The mathematical imports and supplied probability conventions are explicit; they do not establish a physical interpretation.')

FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the axioms select", "adopt the", "the correct reading",
)
CLAIM_INJECTIONS = {"claim_reading_selected_injected": "Hence the axioms select the free-window reading."}
CLASSICAL_NAMES = ("Schur", "Dobrushin", "Peierls", "Toom", "Mermin", "Wagner", "Fröhlich", "Spencer", "Kolmogorov")  # authors; Markov, Gibbs, Hadamard name standard objects
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text + "\n" + phrase
    flat = normalize_text(text)
    checks.check("F1", all(f in flat for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [ph for ph in FORBIDDEN if ph.lower() in flat.lower()]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    source_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    scan = [ln for ln in source_lines if SCAN_MARKER not in ln]
    float_literal = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])")
    conversion = "flo" + "at("  # float-scan-marker-line
    evalf = "eva" + "lf("  # float-scan-marker-line
    numeric = "N" + "("  # float-scan-marker-line
    bad = [ln for ln in scan if float_literal.search(ln) or conversion in ln or evalf in ln or numeric in ln]
    checks.check("F3", not bad and len(scan) > 150, f"runner source: no floating-point literal or conversion call ({len(bad)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for i, sec in enumerate(sections):
        title = sec.splitlines()[0].strip() if i > 0 else "(front matter)"
        body = sec
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem Q3"):
            body = body + " (Schur's lemma)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports and the Premises; Markov, Gibbs and Hadamard name standard objects ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — the spectral decomposition of phi with explicit eigenvectors; the entry differences of phi^2; the path powers k <= 3; the sphere integrals and the series",
    "per_site: executed — the pendant paths of two and three unrecorded sites, symbolically for all six attachment records",
    "per_mode: executed — the two unrecorded corners' entrywise square of phi^2 and its sector eigenvalues",
    "per_block: executed — the abstract square-plus-site diagnostics at three triples; the cube with its top face unrecorded; the pendant forest; the average identity",
    "lattice_wide: component factorization and at-most-one-attachment sufficiency are proved analytically; general attachment-only converse deferred; finite diagnostics do not prove it",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5 and all(len(l) >= 40 for l in N5_LINES), "the five N5 resolution lines are printed")


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
    checks = Checks()
    texts = [(ROOT / pth).read_text(encoding="utf-8") if (ROOT / pth).is_file() else "" for pth in AUDIT_INPUT_PATHS]
    print("AUDIT_INPUT_PATHS:")
    for pth in AUDIT_INPUT_PATHS:
        print(f"  {pth}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: unrecorded sites — the free-window versus integrated-exterior readings of the static law; the spectral algebra of the six-axis rule, the pendant and bridging factors, the sphere factors, abstract-graph diagnostics and genuine cube witnesses; exact")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        observed = "".join(sorted(set(checks.failed_families))) or "none"
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {observed}")
    failed = checks.finish()
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
