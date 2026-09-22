#!/usr/bin/env python3
"""Exact checks: the unsoldered sphere static law with overlap e^{beta t} has finite torus magnetization bounds in dimensions one and two —
the algebraic skeleton of the zero-field lower bound in every dimension, the lattice sums, and the assembly.

Scope.  H1: the generator identities, integration by parts on the sphere for polynomials, the single-bond second-derivative
identity, the quadratic's root and its simplification chain, the bond identity and the bond counts on the 4x4 and 8 tori (the
dimension enters only there).  H2: the sup-norm shell counts 8j and 4L-1 on {-L+1..L}^2, the norm bound |n|^2 <= 2j^2 and
sum_{n != 0} 1/|n|^2 >= 4 H_{L-1} for L <= 12; the dyadic bound H_{2^m} >= 1 + m/2 for m <= 12; the half-angle identity and
sample points; the small-term identities; the line's block of the 2 floor(sqrt L) smallest wavevectors.  H3: Parseval with
symbolic site values on the 4x4 torus, the sphere average 1/3, and the final algebra of the plane and line bounds.  Exact
arithmetic only (Fractions and sympy); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from math import isqrt
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_SPHERE_STATIC_LAW_FINITE_TORUS_MAGNETIZATION_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = 'admissibility_rule_sphere_static_law_finite_torus_magnetization_bounds_bounded_theorem_note_2026-09-15'
PARENT_CLAIM_ID = "possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14"
PARENT_FRAGMENT = "Empty-neighbourhood sphere laws"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "No possibility is privileged.",
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
)

MUTATION_GATE = {
    "shell_count_wrong": "B",
    "dyadic_bound_wrong": "B",
    "line_floor_bound_wrong": "B",
    "cosine_identity_wrong": "C",
    "small_k_term_wrong": "C",
    "final_algebra_wrong": "C",
    "generator_identity_wrong": "D",
    "second_derivative_identity_wrong": "D",
    "root_simplification_wrong": "D",
    "bond_count_wrong": "D",
    "parseval_wrong": "D",
    "claim_order_on_planes_injected": "F",
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


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, parent = texts
    checks.check("A1", all((ROOT / pth).is_file() for pth in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 3,
                 "the three declared inputs exist (this note, the axiom memo, the possibility-covariance note on main)")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the five axiom sentences used are present verbatim in the axiom memo")
    fp = normalize_text(parent)
    checks.check("A3", PARENT_CLAIM_ID in fp and PARENT_FRAGMENT in fp, "the parent's claim id and its empty-neighbourhood sphere-law section are present")
    flat = normalize_text(note)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")


# ============================================================================================ family B
def plane_shells(L: int) -> dict[int, list[int]]:
    rng = range(-L + 1, L + 1)
    shells: dict[int, list[int]] = {}
    for a in rng:
        for b in rng:
            if (a, b) != (0, 0):
                shells.setdefault(max(abs(a), abs(b)), []).append(a * a + b * b)
    return shells


def family_b(checks: Checks) -> None:
    ok = True
    witness = {}
    for L in range(2, 13):
        shells = plane_shells(L)
        full = 8
        if mut("shell_count_wrong"):
            full = 9
        counts = all(len(shells[j]) == full * j for j in range(1, L)) and len(shells[L]) == 4 * L - 1
        norms = all(max(shells[j]) <= 2 * j * j for j in range(1, L + 1))
        total = sum((Fraction(1, q) for j in shells for q in shells[j]), Fraction(0))
        ok = ok and counts and norms and total >= 4 * harmonic(L - 1)
        if L in (2, 12):
            witness[L] = (counts, norms, total >= 4 * harmonic(L - 1))
    checks.check("B1", ok, f"H2(a): on {{-L+1..L}}^2 the sup-norm shell j has 8j points (j < L) and 4L-1 points (j = L), |n|^2 <= 2j^2 on every shell, and sum_{{n != 0}} 1/|n|^2 >= 4 H_(L-1), exactly for L = 2..12 (witness L=2,12: {witness})")
    half = Fraction(1, 2)
    if mut("dyadic_bound_wrong"):
        half = Fraction(2, 3)
    dy = all(harmonic(2 ** m) >= 1 + half * m for m in range(13))
    checks.check("B2", dy, "H2(b): H_(2^m) >= 1 + m/2 for m = 0..12, exactly (each dyadic block contributes at least 1/2)")
    factor = 1
    if mut("line_floor_bound_wrong"):
        factor = 2
    floor_ok = all(4 * isqrt(L) ** 2 >= factor * L for L in range(1, 401))
    count_ok = all(sum(1 for n in range(-L + 1, L + 1) if 1 <= abs(n) <= isqrt(L)) == 2 * isqrt(L) for L in range(2, 401))
    floor_ok = floor_ok and count_ok
    L, beta, n = sp.symbols("L beta n", positive=True)
    per_term = sp.simplify((beta * sp.pi ** 2 + sp.Rational(2, 3)) / L - (beta * sp.pi ** 2 * n ** 2 / L ** 2 + 2 / (3 * L)) - beta * sp.pi ** 2 * (L - n ** 2) / L ** 2) == 0
    checks.check("B3", floor_ok and per_term, "H2(e): 4 floor(sqrt L)^2 >= L for L = 1..400 (so 2 floor(sqrt L) >= sqrt L); exactly 2 floor(sqrt L) wavevectors in the block for L = 2..400; (beta pi^2 + 2/3)/L - [beta pi^2 n^2/L^2 + 2/(3L)] = beta pi^2 (L - n^2)/L^2 >= 0 for n^2 <= L")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    u = sp.symbols("u", real=True)
    target = 4 * sp.sin(u / 2) ** 2
    if mut("cosine_identity_wrong"):
        target = 2 * sp.sin(u / 2) ** 2
    ident = sp.simplify(2 * (1 - sp.cos(u)) - target) == 0
    samples = all(sp.simplify(x ** 2 - 2 * (1 - sp.cos(x))) >= 0 for x in [sp.Rational(i, 10) * sp.pi for i in range(-10, 11)])
    checks.check("C1", ident and samples, "H2(c): 2(1 - cos u) = 4 sin^2(u/2) (so E(k) <= |k|^2 by |sin t| <= |t|); u^2 - 2(1 - cos u) >= 0 at 21 sample points of [-pi, pi]")
    L = sp.symbols("L", positive=True)
    plane = sp.simplify(sp.Rational(4, 3) / (4 * L ** 2) - (sp.pi / L) ** 2 / (3 * sp.pi ** 2)) == 0
    line_val = 2 / (3 * L)
    if mut("small_k_term_wrong"):
        line_val = 1 / (3 * L)
    line = sp.simplify(sp.Rational(4, 3) / (2 * L) - line_val) == 0
    checks.check("C2", plane and line, "H2(d)/(e): 4/(3N) = (pi/L)^2/(3 pi^2) at N = 4L^2 (the plane) and 4/(3N) = 2/(3L) at N = 2L (the line)")
    beta, H, m = sp.symbols("beta H m", positive=True)
    plane_bound = 9 * sp.pi ** 2 * (beta + 1 / (3 * sp.pi ** 2)) / (3 * H)
    plane_target = (3 * sp.pi ** 2 * beta + 1) / H
    if mut("final_algebra_wrong"):
        plane_target = (3 * sp.pi ** 2 * beta + 3) / H
    line_bound = 3 * (beta * sp.pi ** 2 + sp.Rational(2, 3)) / (sp.sqrt(L) / 2)
    line_target = (6 * sp.pi ** 2 * beta + 4) / sp.sqrt(L)
    checks.check("C3", sp.simplify(plane_bound - plane_target) == 0 and sp.simplify(line_bound - line_target) == 0,
                 "H3: 9 pi^2 (beta + 1/(3 pi^2))/(3H) = (3 pi^2 beta + 1)/H (the plane); 3 (beta pi^2 + 2/3)/(sqrt(L)/2) = (6 pi^2 beta + 4)/sqrt(L) (the line)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    sx = sp.Matrix(sp.symbols("x1 x2 x3", real=True)); sy = sp.Matrix(sp.symbols("y1 y2 y3", real=True))
    e2 = sp.Matrix([0, 1, 0])

    def Lgen(v, F):
        w = e2.cross(v)
        return sum(w[i] * sp.diff(F, v[i]) for i in range(3))

    dot = sx.dot(sy)
    g1 = sp.simplify(Lgen(sx, dot) - e2.dot(sx.cross(sy))) == 0 and sp.simplify(Lgen(sy, dot) + e2.dot(sx.cross(sy))) == 0
    g3 = sp.simplify(Lgen(sx, sx[2]) + sx[0]) == 0 and sp.simplify(Lgen(sx, sx[0]) - sx[2]) == 0 and sp.simplify(Lgen(sx, sx[1])) == 0
    if mut("generator_identity_wrong"):
        g3 = sp.simplify(Lgen(sx, sx[2]) - sx[0]) == 0
    checks.check("D1", g1 and g3, "H1(i)/(iv): L_x(s_x.s_y) = e2.(s_x x s_y) = -L_y(s_x.s_y); L s^3 = -s^1, L s^1 = s^3, L s^2 = 0")
    th, ph = sp.symbols("theta phi", real=True)
    svec = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])
    ok_ibp = True
    for F in (sx[0] * sx[2], sx[0] ** 2 * sx[1], sx[2] ** 3):
        LF = Lgen(sx, F).subs({sx[0]: svec[0], sx[1]: svec[1], sx[2]: svec[2]})
        ok_ibp = ok_ibp and sp.simplify(sp.integrate(sp.integrate(LF * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi))) == 0
    cx, cy = sp.symbols("c_x c_y")
    Lc = lambda F: cx * Lgen(sx, F) + cy * Lgen(sy, F)
    Lcbar = lambda F: sp.conjugate(cx) * Lgen(sx, F) + sp.conjugate(cy) * Lgen(sy, F)
    second = -Lc(Lcbar(dot))
    target = (cx - cy) * (sp.conjugate(cx) - sp.conjugate(cy)) * (sx[0] * sy[0] + sx[2] * sy[2])
    if mut("second_derivative_identity_wrong"):
        target = (cx - cy) * (sp.conjugate(cx) - sp.conjugate(cy)) * (sx[0] * sy[0] - sx[2] * sy[2])
    checks.check("D2", ok_ibp and sp.simplify(sp.expand(second - target)) == 0, "H1(i)/(iii): the sphere integral of L F vanishes for three polynomials; -(c_x L_x + c_y L_y)(cbar_x L_x + cbar_y L_y)(s_x.s_y) = |c_x - c_y|^2 (s_x^1 s_y^1 + s_x^3 s_y^3)")
    N, a, M = sp.symbols("N a M", positive=True)
    root = (2 * M ** 2 / 3) / (sp.sqrt(a) + sp.sqrt(a + 4 * M ** 2 / (3 * N)))
    q_ok = sp.simplify(root ** 2 / N + sp.sqrt(a) * root - M ** 2 / 3) == 0
    b = sp.sqrt(a + 4 * M ** 2 / (3 * N))
    factor_target = (b - sp.sqrt(a)) * (3 * b + sp.sqrt(a))
    if mut("root_simplification_wrong"):
        factor_target = (b - sp.sqrt(a)) * (3 * b - sp.sqrt(a))
    s_ok = sp.simplify(4 * b ** 2 - (sp.sqrt(a) + b) ** 2 - factor_target) == 0
    checks.check("D3", q_ok and s_ok, "H1(v)/(vi): the displayed root solves v^2/N + sqrt(a) v - M^2/3 = 0; 4b^2 - (sqrt a + b)^2 = (b - sqrt a)(3b + sqrt a) >= 0 with b = sqrt(a + 4M^2/(3N)), so u >= (M^2/3)^2/(a + 4M^2/(3N))")
    bond_ident = sp.simplify(sp.expand((1 - sp.exp(-sp.I * th)) * (1 - sp.exp(sp.I * th)), complex=True) - 2 * (1 - sp.cos(th))) == 0
    sites2 = list(product(range(4), repeat=2))
    bonds2 = {tuple(sorted((x, ((x[0] + d[0]) % 4, (x[1] + d[1]) % 4)))) for x in sites2 for d in ((1, 0), (0, 1))}
    bonds1 = {tuple(sorted((x, (x + 1) % 8))) for x in range(8)}
    per_dir = 16
    if mut("bond_count_wrong"):
        per_dir = 15
    counts = len(bonds2) == 2 * per_dir and len(bonds1) == 8
    checks.check("D4", bond_ident and counts, "H1(iii): |1 - e^{-i theta}|^2 = 2(1 - cos theta); the 4x4 torus has 2N = 32 bonds (N per direction) and the 8-torus has N = 8: the dimension enters only through the bond count")
    avg = sp.integrate(sp.integrate((sp.sin(th) * sp.cos(ph)) ** 2 * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi)) / (4 * sp.pi)
    sym = {x: sp.Symbol(f"s_{x[0]}{x[1]}", real=True) for x in sites2}
    tot = 0
    for nvec in product(range(4), repeat=2):
        hat = sum(sp.I ** ((nvec[0] * x[0] + nvec[1] * x[1]) % 4) * sym[x] for x in sites2) / sp.Integer(4)
        tot += sp.expand(hat * sp.conjugate(hat))
    target = sum(v ** 2 for v in sym.values())
    if mut("parseval_wrong"):
        target = target * 2
    checks.check("D5", avg == sp.Rational(1, 3) and sp.simplify(sp.expand(tot) - target) == 0, "H3 (the sum rule): the sphere average of (s^1)^2 is 1/3; Parseval sum_k |s^(k)|^2 = sum_x s_x^2 with symbolic site values on the 4x4 torus")


# ============================================================================================ family F
FENCES = ('For a supplied uniform-sphere exponential nearest-neighbour static model in independent dimensions d=1,2,3, on even tori with L>=2: H1 is a finite-volume Fourier lower bound in terms of M_N; H2 supplies explicit lattice sums; H3 gives M_N^4 <= (3 pi^2 beta+1)/H_(L-1) in dimension two and M_N^4 <= (6 pi^2 beta+4)/sqrt(L) in dimension one. These bounds imply vanishing of this torus magnetization-square sequence. No universal state, kernel, gravity or dimension-selection conclusion is retained. This note does not select a physical reading, coupling, rule or dimension and adopts no clause.', 'No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'The standard mathematical imports are stated explicitly; they supply mathematical tools, not physical selection.')
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the plane orders", "derives the classical theorem from the axioms",
)
CLAIM_INJECTIONS = {"claim_order_on_planes_injected": "Hence the plane orders for large beta."}
CLASSICAL_NAMES = ("Mermin", "Wagner", "Hohenberg", "Coleman", "Fröhlich", "Pfister", "McBryan", "Spencer", "Dobrushin", "Shlosman", "Simon", "Peierls", "Toom")  # authors; Bogoliubov, Laplacian, Green function, Parseval name standard objects
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
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem H3"):
            body = body + " (the Mermin–Wagner theorem)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports and the Premises; Bogoliubov, Laplacian, Green function and Parseval name standard objects ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — the generator identities; the single-bond second derivative; the root and its simplification chain; the bond identity",
    "per_site: executed — Parseval with symbolic site values on the 4x4 torus; the sphere average of a component's square",
    "per_mode: executed — the shell counts 8j and 4L-1 and the norm bound on every wavevector shell for L <= 12; the line's block of the 2 floor(sqrt L) smallest wavevectors",
    "per_block: executed — the dyadic blocks of the harmonic sum to m = 12; the bond counts on the 4x4 and 8 tori",
    "lattice_wide: checked and not executed — written conditional model proofs and bounds only; the finite runner does not execute an infinite lattice or physical classification",
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
    print("scope: the unsoldered sphere static law with overlap e^{beta t} on planes and lines — the zero-field lower bound's skeleton in every dimension, the plane's shell sums and the dyadic bound, the line's small-wavevector block, Parseval and the sphere average, the final algebra; exact")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
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
