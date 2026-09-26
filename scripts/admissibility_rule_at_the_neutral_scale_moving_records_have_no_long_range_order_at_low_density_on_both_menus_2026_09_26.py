#!/usr/bin/env python3
"""Exact checks: at the neutral scale, moving records have no long-range order below explicit densities on both menus, and
the sphere's threshold falls as beta^-5 (a harvest of probe #9304, confirmed and sharpened by an other-family referee in
#9329). Block 126's law with vacancies as landed: empty weight 1, content weight z times the menu's measure, bond kernel 1
with an empty end and c e^(beta s.s') between contents, on even cubic tori; neutral scales c0 = beta/sinh beta (sphere,
uniform probability measure) and 1/cosh beta (two-valued, counting measure).

A (premises): landed block 126's menus, scales and kernel; the axioms.
B (T1): the sphere average sinh(beta|v|)/(beta|v|); neutrality on both menus; sinh(y)/y increasing; F_(m+1)/F_m =
   (m/(m+1)) beta (coth beta + coth(m beta)) > 1, so the sphere's weight is at most F_6; the two-valued weight is at most
   G(t) = (1+t)^6 + (1-t)^6 for all 28 neighbour counts (Bernstein certificates), and G rises from 2 to 64.
C (T2): occupation w/(1+w) < 1/5 iff w < 1/4; self-avoiding paths on Z^3 (exact counts to n = 5 against 6 5^(n-1)); the
   path sum identity; the rotations fixing only 0; the two-valued region contains z < 1/256 and exceeds 1/320 by 80/G.
D (T3): F_6/beta^5 -> 16/3, so the sphere threshold 1/(4 F_6) ~ 3/(64 beta^5); F_6 -> 1 as beta -> 0; the earlier remark's
   weight exceeds F_6 by a factor ~ 12 beta.
Exact (sympy, fractions). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import re
import sys
import time
from fractions import Fraction as Fr
from math import comb
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_AT_THE_NEUTRAL_SCALE_MOVING_RECORDS_HAVE_NO_LONG_RANGE_ORDER_AT_LOW_DENSITY_ON_BOTH_MENUS_AND_THE_SPHERE_THRESHOLD_FALLS_AS_BETA_TO_MINUS_FIVE_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_WITH_VACANCIES_THE_INFRARED_STIFFNESS_IS_SET_BY_THE_BINDING_SCALE_LONG_RANGE_ORDER_ABOVE_THE_NEUTRAL_SCALE_AND_NO_FULL_BOUND_AT_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_at_the_neutral_scale_moving_records_have_no_long_range_order_at_low_density_on_both_menus_and_the_sphere_threshold_falls_as_beta_to_minus_five_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED_NEEDLES = (
    "`c₀(γ) = γ/sinh γ` (sphere) or `1/cosh γ` (two-valued)",
    "The sphere menu has `s ∈ S²` with the uniform measure",
    "The two-valued menu has `s = ±1` with counting measure.",
    "`B(s, s') = c e^{βs·s'}`",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "sphere_average_forged": "B",
    "occupation_forged": "C",
    "asymptotic_forged": "D",
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
            print(f"PASS: {tag} {msg}", flush=True)
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}", flush=True)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


T0 = time.time()
beta, y, r, th, tt = sp.symbols("beta y r theta t", positive=True)


def F_m(m: int):
    return (beta / sp.sinh(beta)) ** m * sp.sinh(m * beta) / (m * beta)


def bernstein_nonneg(poly_expr, var, deg: int) -> bool:
    """all Bernstein coefficients of poly_expr on [0, 1] in degree deg are >= 0 (a certificate of nonnegativity there)"""
    P = sp.Poly(sp.expand(poly_expr), var)
    a = [P.coeff_monomial(var ** j) for j in range(deg + 1)]
    for i in range(deg + 1):
        b_i = sum(sp.Rational(comb(i, j), comb(deg, j)) * a[j] for j in range(i + 1))
        if b_i < 0:
            return False
    return True


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, landed = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the law with vacancies, its weights and the menus are supplied)")
    needles = list(LANDED_NEEDLES)
    if mut("landed_quote_forged"):
        needles[0] = "`c₀(γ) = γ/cosh γ` (sphere) or `1/cosh γ` (two-valued)"
    checks.check("A3", all(n in landed for n in needles), "landed block 126: c0(gamma) = gamma/sinh gamma (sphere) or 1/cosh gamma (two-valued); the sphere menu with the uniform measure; the two-valued menu with counting measure; B(s, s') = c e^(beta s.s')")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    avg = sp.integrate(sp.exp(beta * r * sp.cos(th)) * sp.sin(th), (th, 0, sp.pi)) / 2
    target = sp.sinh(beta * r) / (beta * r)
    if mut("sphere_average_forged"):
        target = sp.cosh(beta * r) / (beta * r)
    ok1 = sp.simplify((avg - target).rewrite(sp.exp)) == 0
    neutral_s = sp.simplify(beta / sp.sinh(beta) * target.subs(r, 1) - 1) == 0
    neutral_2 = all(sp.simplify((sp.exp(sg * beta) / sp.cosh(beta) - (1 + sg * sp.tanh(beta))).rewrite(sp.exp)) == 0 for sg in (1, -1))
    checks.check("B1", ok1 and neutral_s and neutral_2, "the sphere average <e^(beta s.v)> = sinh(beta|v|)/(beta|v|) (uniform probability measure); at the neutral scales an occupied neighbour weighs 1 on average: (beta/sinh beta) sinh(beta)/beta = 1, and e^(+-beta)/cosh beta = 1 +- tanh beta")
    ser = sp.series(y * sp.cosh(y) - sp.sinh(y), y, 0, 23).removeO()
    ok2 = all(ser.coeff(y, 2 * n) == 0 for n in range(12)) and all(ser.coeff(y, 2 * n + 1) == sp.Rational(2 * n, sp.factorial(2 * n + 1)) for n in range(11))
    checks.check("B2", ok2, "y cosh y - sinh y = sum_(n >= 1) 2n y^(2n+1)/(2n+1)! (coefficients to y^21), so sinh(y)/y increases on y > 0 and x coth x > 1 for x > 0")
    ok3 = sp.simplify(F_m(1) - 1) == 0
    for m in range(1, 6):
        ratio = F_m(m + 1) / F_m(m)
        claim = sp.Rational(m, m + 1) * beta * (sp.coth(beta) + sp.coth(m * beta))
        ok3 = ok3 and sp.simplify((ratio - claim).rewrite(sp.exp)) == 0
    checks.check("B3", ok3, "F_m = c0^m sinh(m beta)/(m beta) has F_1 = 1 and F_(m+1)/F_m = (m/(m+1)) beta (coth beta + coth(m beta)) (m = 1..5), which exceeds 1 by B2; with |v| <= m <= 6 the sphere's conditional weight c0^m sinh(beta|v|)/(beta|v|) is at most F_6(beta)")
    G = (1 + tt) ** 6 + (1 - tt) ** 6
    ok4 = True
    pairs = 0
    for k in range(7):
        for l in range(7 - k):
            S = (1 + tt) ** k * (1 - tt) ** l + (1 - tt) ** k * (1 + tt) ** l
            ok4 = ok4 and bernstein_nonneg(G - S, tt, 6)
            pairs += 1
    ok4 = ok4 and pairs == 28 and G.subs(tt, 0) == 2 and G.subs(tt, 1) == 64 and bernstein_nonneg(sp.diff(G, tt), tt, 5)
    checks.check("B4", ok4, "two-valued: with k neighbours at +1 and l at -1 the conditional weight (1+t)^k (1-t)^l + (1-t)^k (1+t)^l is at most G(t) = (1+t)^6 + (1-t)^6 on [0, 1] for all 28 pairs k + l <= 6 (Bernstein certificates); G rises from G(0) = 2 to G(1) = 64")


# ============================================================================================ family C (T2)
def saw_counts(nmax: int):
    steps = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    counts = [0] * (nmax + 1)

    def extend(path, visited, n):
        counts[n] += 1
        if n == nmax:
            return
        x, y_, z = path[-1]
        for dx, dy, dz in steps:
            nxt = (x + dx, y_ + dy, z + dz)
            if nxt not in visited:
                visited.add(nxt)
                path.append(nxt)
                extend(path, visited, n + 1)
                path.pop()
                visited.remove(nxt)

    extend([(0, 0, 0)], {(0, 0, 0)}, 0)
    return counts


def family_c(checks: Checks) -> None:
    w = sp.Symbol("w", positive=True)
    rho = w / (1 + w)
    edge = sp.Rational(1, 4) if not mut("occupation_forged") else sp.Rational(1, 5)
    ok1 = sp.simplify(sp.diff(rho, w) - 1 / (1 + w) ** 2) == 0 and rho.subs(w, edge) == sp.Rational(1, 5)
    checks.check("C1", ok1, "given the rest, a site is occupied with probability zS/(1 + zS), which increases in S; with S <= S_max and w = z S_max it is at most rho = w/(1 + w), and rho < 1/5 exactly when w < 1/4")
    counts = saw_counts(5)
    ok2 = counts[1:] == [6, 30, 150, 726, 3534] and all(counts[n] <= 6 * 5 ** (n - 1) for n in range(1, 6))
    p = sp.Symbol("p", positive=True)
    ok2 = ok2 and all(sp.expand((1 - 5 * p) * sum(6 * 5 ** (n - 1) * p ** (n + 1) for n in range(1, N + 1)) - 6 * p ** 2 * (1 - (5 * p) ** N)) == 0 for N in range(1, 11))
    checks.check("C2", ok2, "self-avoiding paths on Z^3 from a site: 6, 30, 150, 726, 3534 for n = 1..5, within 6 5^(n-1); the path sum (1 - 5p) sum_(n <= N) 6 5^(n-1) p^(n+1) = 6 p^2 (1 - (5p)^N) (N = 1..10), so the occupied cluster of a site under domination at density rho < 1/5 has expected size at most rho + 6 rho^2/(1 - 5 rho)")
    Rz = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    Rx = sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
    fixed = (Rz - sp.eye(3)).col_join(Rx - sp.eye(3)).nullspace()
    ok3 = fixed == [] and Rz.det() == 1 and Rx.det() == 1 and Rz.T * Rz == sp.eye(3) and Rx.T * Rx == sp.eye(3)
    checks.check("C3", ok3, "cluster decoupling on the sphere: given the occupied set, a common rotation of one cluster's contents keeps every bond weight, so the cluster's conditional mean is fixed by the quarter turns about z and x, whose only common fixed vector is 0; on the two-valued menu a common sign flip does the same")
    G = (1 + tt) ** 6 + (1 - tt) ** 6
    ok4 = bernstein_nonneg(64 - G, tt, 6) and sp.Rational(80, 1) / G.subs(tt, 0) == 40 and sp.Rational(80, 1) / G.subs(tt, 1) == sp.Rational(5, 4) and sp.Rational(64, 1) / G.subs(tt, 0) == 32
    checks.check("C4", ok4, "the two-valued region z < 1/(4 G(tanh beta)) contains z < 1/256 at every beta (G <= 64 on [0, 1]), hence block 153's z < 1/320; it is larger than 1/320 by 80/G: 40 as beta -> 0 and 5/4 as beta -> oo")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    F6 = F_m(6)
    lim_inf = sp.limit((F6 / beta ** 5).rewrite(sp.exp), beta, sp.oo)
    lim_0 = sp.limit(F6.rewrite(sp.exp), beta, 0)
    want = sp.Rational(16, 3) if not mut("asymptotic_forged") else sp.Rational(16, 5)
    thr = sp.limit((beta ** 5 / (4 * F6)).rewrite(sp.exp), beta, sp.oo)
    checks.check("D1", lim_inf == want and lim_0 == 1 and thr == sp.Rational(3, 64), "F_6(beta)/beta^5 -> 16/3 as beta -> oo and F_6 -> 1 as beta -> 0: the sphere threshold z0(beta) = 1/(4 F_6(beta)) tends to 1/4 at small beta and is asymptotic to 3/(64 beta^5)")
    remark = (beta * sp.exp(beta) / sp.sinh(beta)) ** 6
    ratio = sp.limit((remark / (F6 * beta)).rewrite(sp.exp), beta, sp.oo)
    checks.check("D2", ratio == 12, "the earlier remark's weight (beta e^beta/sinh beta)^6 exceeds F_6 by a factor asymptotic to 12 beta; the attempt's region 1/(5 F_6) lies inside 1/(4 F_6)")


# ============================================================================================ family F
FENCES = (
    "This note works within block 126 as landed on main (the law with vacancies, its two menus and its neutral scales) and places block 153 (open PR #9285); it reports densities below which moving records at the neutral scale have no long-range order, on both menus; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at z = 1/256."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Haar", "Bernstein",
                   "Peierls", "Ising", "Heisenberg", "Fröhlich", "Lieb", "Simon", "Israel", "Biskup", "Pisztora", "Deuschel", "Timár", "Harris")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Peierls) —", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p_ for p_ in FORBIDDEN if p_ in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
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
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the sphere average and the two neutral scales",
    "per_site: executed - the conditional weights: F_m's ratios and the 28 two-valued neighbour counts",
    "per_mode: executed - the occupation bound w/(1 + w) and its cutoff w < 1/4",
    "per_block: executed - self-avoiding path counts to n = 5, the path sum, the quarter turns, the regions and the sphere asymptotics",
    "lattice_wide: checked and not executed - the window between low and high density; the sphere at high density; the torus separation lemma",
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
    for p_ in AUDIT_INPUT_PATHS:
        print(f"  {p_}")
    texts = [Path(ROOT, p_).read_text(encoding="utf-8") if Path(ROOT, p_).exists() else "" for p_ in AUDIT_INPUT_PATHS]
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
    print(f"scope: block 126's law with vacancies at the neutral scale: no long-range order for z < 1/(4 F_6(beta)) on the sphere (~ 3/(64 beta^5)) and z < 1/(4 G(tanh beta)) on the two-valued menu (contains z < 1/256); harvest of #9304 (confirmed and sharpened by #9329); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
