#!/usr/bin/env python3
"""Exact symbolic checks: the unsoldered sphere static law with overlap e^{beta t} — the algebraic skeleton of the infrared bound,
magnetization-square estimates, and the zero-field component bound; Gaussian domination is imported, not executed.

Scope.  G1: the Legendre coefficients of e^{beta t} in Rodrigues form (positive integrand), l <= 4, symbolically in beta.  G2: the
gradient-twist identity; the plane wave as a Laplacian eigenfunction on the 4^3 torus with eigenvalue E(k) = sum 2(1 - cos k_i);
the gradient sum E(k) sum psi^2; the second-order coefficient of the twisted weight.  G3: 1 - cos u >= 2u^2/pi^2 at sample points;
the bound G(0) <= sqrt(3) pi/8; the threshold 3 sqrt(3) pi/8 < 21/10.  G4: the generator identities, integration by parts on the sphere
for polynomials, the single-bond second-derivative identity, the quadratic's root and its limit.  Exact symbolic arithmetic only;
the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from itertools import product
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_SPHERE_STATIC_LAW_ZERO_FIELD_COMPONENT_FOURIER_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_sphere_static_law_zero_field_component_fourier_bounds_bounded_theorem_note_2026-09-15"
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
    "legendre_coefficient_sign_wrong": "B",
    "laplacian_eigenvalue_wrong": "B",
    "gradient_sum_wrong": "B",
    "second_order_coefficient_wrong": "B",
    "cosine_inequality_wrong": "C",
    "green_bound_wrong": "C",
    "threshold_wrong": "C",
    "generator_identity_wrong": "D",
    "integration_by_parts_nonzero_claimed": "D",
    "second_derivative_identity_wrong": "D",
    "quadratic_root_wrong": "D",
    "infrared_bound_direction_reversed": "F",
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
def torus_sites(L: int):
    return list(product(range(L), repeat=3))


def torus_nbrs(x, L: int):
    out = []
    for i in range(3):
        for d in (1, -1):
            y = list(x)
            y[i] = (x[i] + d) % L
            out.append(tuple(y))
    return out


def family_b(checks: Checks) -> None:
    t, beta = sp.symbols("t beta", positive=True)
    ok = True
    for l in range(5):
        direct = sp.integrate(sp.exp(beta * t) * sp.legendre(l, t), (t, -1, 1))
        rod = beta ** l / (2 ** l * sp.factorial(l)) * sp.integrate((1 - t ** 2) ** l * sp.exp(beta * t), (t, -1, 1))
        if mut("legendre_coefficient_sign_wrong"):
            rod = -rod
        ok = ok and sp.simplify(direct - rod) == 0
    checks.check("B1", ok, "G1: int e^{beta t} P_l = (beta^l/(2^l l!)) int (1 - t^2)^l e^{beta t} dt for l <= 4, symbolically in beta (a positive integrand)")
    L = 4
    sites = torus_sites(L)
    ok2 = True
    sums = {}
    for k in ((sp.pi / 2, 0, 0), (sp.pi / 2, sp.pi / 2, 0)):
        E = sum(2 * (1 - sp.cos(ki)) for ki in k)
        if mut("laplacian_eigenvalue_wrong"):
            E = E + 1
        psi = {x: sp.cos(sum(ki * xi for ki, xi in zip(k, x))) for x in sites}
        ok2 = ok2 and all(sp.simplify(sum(psi[x] - psi[y] for y in torus_nbrs(x, L)) - E * psi[x]) == 0 for x in sites)
        bonds = {tuple(sorted((x, y))) for x in sites for y in torus_nbrs(x, L)}
        grad2 = sum((psi[x] - psi[y]) ** 2 for (x, y) in bonds)
        sum2 = sum(psi[x] ** 2 for x in sites)
        target = E * sum2
        if mut("gradient_sum_wrong"):
            target = target * 2
        ok2 = ok2 and sp.simplify(grad2 - target) == 0 and sum2 == len(sites) / sp.Integer(2)
        sums[k] = (E, sum2)
    checks.check("B2", ok2, "G2: on the 4^3 torus the plane wave cos(k.x) is a Laplacian eigenfunction with eigenvalue E(k) = sum 2(1 - cos k_i), and sum over bonds (dpsi)^2 = E(k) sum psi^2 = E(k) N/2, at k = (pi/2,0,0) [E = 2] and (pi/2,pi/2,0) [E = 4]")
    # twist identity and second-order coefficient
    sx = sp.Matrix(sp.symbols("x1 x2 x3", real=True)); sy = sp.Matrix(sp.symbols("y1 y2 y3", real=True))
    phx, phy, lam, X, S2, b = sp.symbols("phi_x phi_y lambda X S2 beta", real=True)
    e = sp.Matrix([1, 0, 0])
    lhs = (sx - sy - (phx - phy) * e).dot(sx - sy - (phx - phy) * e)
    rhs = ((sx - phx * e) - (sy - phy * e)).dot((sx - phx * e) - (sy - phy * e))
    twist_ok = sp.simplify(lhs - rhs) == 0
    expo = sp.exp(b * lam * X - b * lam ** 2 / 2 * S2)
    second = sp.diff(expo, lam, 2).subs(lam, 0)
    target = b ** 2 * X ** 2 - b * S2
    if mut("second_order_coefficient_wrong"):
        target = b ** 2 * X ** 2 + b * S2
    checks.check("B3", twist_ok and sp.simplify(second - target) == 0, "G2: the gradient twist is a site shift; the second lambda-derivative of exp(beta lambda X - beta lambda^2 S2/2) at 0 is beta^2 X^2 - beta S2, the explicitly imported Z(lambda psi) <= Z(0) bound then forces beta^2 <X^2> <= beta S2")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    samples = [sp.Rational(i, 10) * sp.pi for i in range(-10, 11)]
    ok = all(sp.simplify(1 - sp.cos(x) - 2 * x ** 2 / sp.pi ** 2) >= 0 for x in samples)
    if mut("cosine_inequality_wrong"):
        ok = all(sp.simplify(1 - sp.cos(x) - 3 * x ** 2 / sp.pi ** 2) >= 0 for x in samples)
    checks.check("C1", ok, "G3: 1 - cos u >= 2 u^2/pi^2 at 21 sample points of [-pi, pi]")
    r = sp.symbols("r", positive=True)
    ball = sp.integrate(4 * sp.pi * r ** 2 / r ** 2, (r, 0, sp.sqrt(3) * sp.pi))  # int d^3k/|k|^2 over the ball of radius sqrt(3) pi
    bound = sp.pi ** 2 / 4 * ball / (2 * sp.pi) ** 3
    target = sp.sqrt(3) * sp.pi / 8
    if mut("green_bound_wrong"):
        target = sp.sqrt(3) * sp.pi / 4
    c2 = sp.simplify(bound - target) == 0
    thr = 3 * target
    thr_ok = sp.simplify(thr - 3 * sp.sqrt(3) * sp.pi / 8) == 0 and (thr < sp.Rational(21, 10))
    if mut("threshold_wrong"):
        thr_ok = thr < sp.Rational(2, 1)
    checks.check("C2", c2 and thr_ok, "G3: (pi^2/4) (2 pi)^{-3} int_{|k| <= sqrt(3) pi} d^3k/|k|^2 = sqrt(3) pi/8; the threshold 3 sqrt(3) pi/8 is below 21/10")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    sx = sp.Matrix(sp.symbols("x1 x2 x3", real=True)); sy = sp.Matrix(sp.symbols("y1 y2 y3", real=True))
    e2 = sp.Matrix([0, 1, 0])

    def Lgen(v, F):
        w = e2.cross(v)
        return sum(w[i] * sp.diff(F, v[i]) for i in range(3))
    dot = sx.dot(sy)
    g1 = sp.simplify(Lgen(sx, dot) - e2.dot(sx.cross(sy))) == 0
    g2 = sp.simplify(Lgen(sy, dot) + e2.dot(sx.cross(sy))) == 0
    g3 = sp.simplify(Lgen(sx, sx[2]) + sx[0]) == 0 and sp.simplify(Lgen(sx, sx[0]) - sx[2]) == 0 and sp.simplify(Lgen(sx, sx[1])) == 0
    if mut("generator_identity_wrong"):
        g3 = sp.simplify(Lgen(sx, sx[2]) - sx[0]) == 0
    checks.check("D1", g1 and g2 and g3, "G4: L_x(s_x.s_y) = e2.(s_x x s_y), L_y(s_x.s_y) = -e2.(s_x x s_y), L s^3 = -s^1, L s^1 = s^3, L s^2 = 0")
    th, ph = sp.symbols("theta phi", real=True)
    svec = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])
    ok_ibp = True
    for F in (sx[0] * sx[2], sx[0] ** 2 * sx[1], sx[2] ** 3, sx[0] * sx[1] * sx[2]):
        LF = Lgen(sx, F).subs({sx[0]: svec[0], sx[1]: svec[1], sx[2]: svec[2]})
        val = sp.integrate(sp.integrate(LF * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi))
        ok_ibp = ok_ibp and sp.simplify(val) == 0
    if mut("integration_by_parts_nonzero_claimed"):
        ok_ibp = not ok_ibp
    cx, cy = sp.symbols("c_x c_y")
    Lc = lambda F: cx * Lgen(sx, F) + cy * Lgen(sy, F)
    Lcbar = lambda F: sp.conjugate(cx) * Lgen(sx, F) + sp.conjugate(cy) * Lgen(sy, F)
    second = -Lc(Lcbar(dot))
    target = (cx - cy) * (sp.conjugate(cx) - sp.conjugate(cy)) * (sx[0] * sy[0] + sx[2] * sy[2])
    if mut("second_derivative_identity_wrong"):
        target = (cx - cy) * (sp.conjugate(cx) - sp.conjugate(cy)) * (sx[0] * sy[0] - sx[2] * sy[2])
    checks.check("D2", ok_ibp and sp.simplify(sp.expand(second - target)) == 0, "G4: the sphere integral of L F vanishes for four polynomials; -(c_x L_x + c_y L_y)(cbar_x L_x + cbar_y L_y)(s_x.s_y) = |c_x - c_y|^2 (s_x^1 s_y^1 + s_x^3 s_y^3)")
    N, bE, M = sp.symbols("N bE M", positive=True)
    root = (2 * M ** 2 / 3) / (sp.sqrt(bE) + sp.sqrt(bE + 4 * M ** 2 / (3 * N)))
    if mut("quadratic_root_wrong"):
        root = (2 * M ** 2 / 3) / (sp.sqrt(bE) + sp.sqrt(bE + 2 * M ** 2 / (3 * N)))
    q_ok = sp.simplify(root ** 2 / N + sp.sqrt(bE) * root - M ** 2 / 3) == 0
    lim_ok = sp.simplify(sp.limit(root, N, sp.oo) - M ** 2 / (3 * sp.sqrt(bE))) == 0
    checks.check("D3", q_ok and lim_ok, "G4/G5: (2M^2/3)/[sqrt(bE) + sqrt(bE + 4M^2/(3N))] is the positive root of u^2/N + sqrt(bE) u - M^2/3 = 0 and tends to M^2/(3 sqrt(bE)): the lower bound (M^2/3)^2/(beta E)")


# ============================================================================================ family F
FENCES = ('This note gives zero-field component Fourier bounds for the supplied sphere static law using an explicit Gaussian-domination import; it establishes no selected transverse-state correlator, pointwise real-space decay or physical model classification, and adopts no clause.', 'No plane, bridge, Born-weight or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'The uniform sphere measure and exponential interaction are declared model inputs; all load-bearing mathematical imports are explicitly identified.')
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "for every coupling", "selects the", "fires wake condition", "the Bridge weights",
    "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "Goldstone theorem is derived", "washes out", "toward the plane", "the trend",
    "the structure factor is at least 1/(beta E(k))",
)
CLAIM_INJECTIONS = {"infrared_bound_direction_reversed": "Hence the structure factor is at least 1/(beta E(k)) for every k."}
CLASSICAL_NAMES = ("Fröhlich", "Simon", "Spencer", "Israel", "Lieb", "Biskup", "Mermin", "Wagner", "Goldstone", "Peierls", "Toom", "Dobrushin", "Coleman")  # authors; Legendre, Rodrigues and Bogoliubov name standard objects, like Gaussian or Laplacian
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
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem G2"):
            body = body + " (the Fröhlich–Simon–Spencer bound)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports and the Premises' file citation; Legendre, Rodrigues and Bogoliubov name standard objects ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — the Legendre coefficients of e^{beta t} in Rodrigues form for l <= 4; the generator identities; the single-bond second derivative; the quadratic's root and limit",
    "per_site: executed — the plane wave as a Laplacian eigenfunction at every site of the 4^3 torus at two wavevectors",
    "per_mode: executed — the gradient sums E(k) N/2 at two wavevectors; the second-order coefficient of the twisted weight",
    "per_block: executed — integration by parts on the sphere for four polynomials; the Green-function bound and the threshold",
    "lattice_wide: checked and not executed — imported Gaussian domination and written component Fourier/limit proofs; no infinite-lattice execution or transverse-state identification",
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
    print("scope: the unsoldered sphere static law with overlap e^{beta t} — Legendre positivity, the twist and plane-wave identities behind the infrared bound, the Green-function bound and threshold, the generator identities and the quadratic behind the zero-field Bogoliubov bound; exact symbolic")
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
