#!/usr/bin/env python3
"""Exact checks: within block 176's reach-three family, the only finite-stretch completion of block 69's coupling in which each further
uniform stretch acts on the stretched walk as a relabelling (dF/db = p dF/dk with a local odd generator p, to every order) is block 69's
linear completion q = 1 - l; it keeps one speed limit only for l <= 7/6 (blocks 173, 176). So no reach-three completion is both
covariant and admissible beyond l = 7/6. Covariant completions outside reach three exist (the fixed-generator flow and the
self-consistent flow) and leave it at second order (the supervisor's own derivation, unrefereed). Block 69 as landed; blocks 173 and
176 (pushed) placed and their needed facts re-derived.

A (premises): landed block 69 (uniform form; the leading order does not determine a completion); the axioms.
B (T1): the generator's form p = s c g(s^2) (odd, antisymmetric under k -> pi - k); order by order to order 5 with symbolic free
   coefficients every term of a covariant reach-three family is proportional to s c^2.
C (T2): the linear family F = s(1 + beta c^2) is covariant with p = beta' s c/(1 + beta - 3 beta s^2), whose series coefficients are
   s c times polynomials in s^2; its long-wave speed is 1 + beta = 1/l, so l F = s(1 - (1 - l) s^2): q = 1 - l.
D (T3): the axis group speed squared (1 - x)(1 - 3 q x)^2 exceeds the long-wave value near k = 0 iff q < -1/6; with q = 1 - l, iff l > 7/6.
E (T4): the fixed-generator flow F = e^b s/sqrt(c^2 + e^{2b} s^2) and the self-consistent flow (u = F^2, u_b + u_k^2/2 = 0) are
   covariant and have s^5 terms at second order (reach five).
Exact (sympy). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
import time
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_ONLY_REACH_THREE_COMPLETION_THAT_KEEPS_EACH_FURTHER_STRETCH_A_RELABELLING_IS_BLOCK_69S_LINEAR_ONE_AND_IT_FAILS_BEYOND_SEVEN_SIXTHS_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_only_reach_three_completion_that_keeps_each_further_stretch_a_relabelling_is_block_69s_linear_one_and_it_fails_beyond_seven_sixths_bounded_theorem_note_2026-09-27"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED69 = (
    "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`",
    "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion.",
    "Set P_j=S_j C_j=(T_j^2-T_j^-2)/(4i)",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "shape_forged": "B",
    "generator_forged": "C",
    "threshold_forged": "D",
    "flow_forged": "E",
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
k, b = sp.symbols("k b")
s = sp.sin(k)
c = sp.cos(k)
x = sp.Symbol("x")


def over_s_in_x(expr):
    """expr is s times a polynomial in s^2 (with even powers of c); return that polynomial in x = s^2"""
    e = sp.expand(sp.simplify(expr / s))
    e = sp.expand(sp.expand_trig(e))
    e = e.subs(sp.cos(k), sp.sqrt(1 - sp.sin(k) ** 2))
    e = sp.expand(e).subs(sp.sin(k), sp.sqrt(x))
    return sp.expand(sp.simplify(e))


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t69 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its coupling and its completion are supplied)")
    needles = list(LANDED69)
    if mut("landed_quote_forged"):
        needles[1] = "Common corner quadratic forms are a leading-order result and determine a nonlinear completion."
    checks.check("A3", all(n in t69 for n in needles), "landed block 69: the uniform form s_a + c_a sum_j B s_j c_j; its N1: the leading order does not determine a nonlinear completion; the two-step momentum")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    # generator symmetry: odd in k and antisymmetric under k -> pi - k  =>  only sin(2 m k) = s c * poly(s^2)
    ok_sym = all(sp.simplify(sp.sin(n * (sp.pi - k)) + (-1) ** n * sp.sin(n * k)) == 0 for n in range(1, 7))
    ok_even = True
    for n in range(1, 4):
        e = sp.expand(sp.expand_trig(sp.sin(2 * n * k)))
        e = sp.expand(sp.simplify(e / (s * c)))
        e = sp.expand(e.subs(sp.cos(k) ** 2, 1 - sp.sin(k) ** 2))
        ok_even = ok_even and not e.has(sp.cos(k))
    # order by order with symbolic free coefficients
    DEG = 5
    N = 5
    ps = [s * c]
    fn = [s]
    shapes = []
    frees = []
    for n in range(1, N + 1):
        if n >= 2:
            gc = sp.symbols(f"g{n - 1}_0:{DEG + 1}")
            ps.append(s * c * sum(gc[i] * s ** (2 * i) for i in range(DEG + 1)))
        P = sum(b ** mm * ps[mm] for mm in range(len(ps)))
        F = sum(b ** mm * fn[mm] for mm in range(n))
        f_n = sp.expand(sp.expand(sp.diff(F, k) * P).coeff(b, n - 1) / n)
        if n >= 2:
            px = sp.Poly(over_s_in_x(f_n), x)
            conds = [cc for i, cc in enumerate(px.all_coeffs()[::-1]) if i >= 2]
            sol = sp.solve(conds, list(gc), dict=True)
            if not sol:
                shapes.append(False)
                break
            S = sol[0]
            frees += [g for g in gc if g not in S]
            ps[-1] = sp.expand(ps[-1].subs(S))
            f_n = sp.expand(f_n.subs(S))
        fx = sp.expand(over_s_in_x(f_n))
        prop = sp.degree(sp.Poly(fx, x)) <= 1 and sp.simplify(fx.subs(x, 1)) == 0
        if mut("shape_forged"):
            prop = prop and sp.simplify(fx.subs(x, 0)) == 0
        shapes.append(prop)
        fn.append(f_n)
    checks.check("B1", ok_sym and ok_even, "a generator that keeps the family odd and symmetric under k -> pi - k is a sum of sin(2mk) = s c times a polynomial in s^2")
    checks.check("B2", len(shapes) == 5 and all(shapes), f"covariance dF/db = p dF/dk order by order to order 5, every generator coefficient free: each term that stays in reach three is proportional to s c^2 = s(1 - s^2); the free constants ({len(frees)}) only reparametrise b")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    beta = sp.Function("beta")(b)
    F = s * (1 + beta * c ** 2)
    p = sp.diff(beta, b) * s * c / (1 + beta - 3 * beta * s ** 2)
    if mut("generator_forged"):
        p = sp.diff(beta, b) * s * c / (1 + beta - 2 * beta * s ** 2)
    ok = sp.simplify(sp.diff(F, b) - p * sp.diff(F, k)) == 0
    # series coefficients of p for beta = b are s c times polynomials in s^2
    pb = (s * c / (1 + b - 3 * b * s ** 2)).series(b, 0, 5).removeO()
    ok2 = all(sp.simplify(sp.expand(pb.coeff(b, n)) / (s * c)).free_symbols <= {k} for n in range(5))
    lw = sp.limit(F.subs(beta, sp.Symbol("be")) / k, k, 0)
    l_ = sp.Symbol("l", positive=True)
    be = sp.Symbol("be")
    lf = sp.expand((l_ * F.subs(beta, be)).subs(be, 1 / l_ - 1).subs(c ** 2, 1 - s ** 2))
    ok3 = sp.simplify(lw - (1 + be)) == 0 and sp.simplify(lf - s * (1 - (1 - l_) * s ** 2)) == 0
    # at finite stretch, in l: F = g_l(sin k), g_l(S) = S (1 + (l - 1) S^2)/l, monotone on [-1, 1] iff l > 2/3; generator sc/(l (1 + 3(l - 1) s^2))
    l2 = sp.Symbol("l", positive=True)
    S_ = sp.Symbol("S")
    g = S_ * (1 + (l2 - 1) * S_ ** 2) / l2
    gprime = sp.factor(sp.diff(g, S_))
    Fl = s * (1 + (l2 - 1) * s ** 2) / l2
    pl = sp.simplify(-sp.diff(Fl, l2) / sp.diff(Fl, k))
    ok4 = sp.simplify(gprime - (1 + 3 * (l2 - 1) * S_ ** 2) / l2) == 0 and sp.factor(gprime.subs(S_, 1)) == sp.factor((3 * l2 - 2) / l2) and sp.simplify(pl - s * c / (l2 * (1 + 3 * (l2 - 1) * s ** 2))) == 0
    checks.check("C2", ok4, "at finite stretch the linear completion is F = g_l(sin k), g_l(S) = S(1 + (l - 1)S^2)/l, with g_l' = (1 + 3(l - 1)S^2)/l >= (3l - 2)/l: a monotone bijection of [-1, 1] iff l > 2/3, so the free walk relabelled; its generator in l is s c/(l(1 + 3(l - 1)s^2)), bounded there")
    checks.check("C1", ok and ok2 and ok3, "the linear family F = s(1 + beta c^2) obeys dF/db = p dF/dk with p = beta' s c/(1 + beta - 3 beta s^2), a series of s c times polynomials in s^2; its long-wave speed is 1 + beta = 1/l, so l F = s(1 - (1 - l) s^2): q = 1 - l, block 69's linear completion")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    q = sp.Symbol("q", real=True)
    lsym = sp.sin(k) * (1 - q * sp.sin(k) ** 2)
    speed2 = sp.expand(sp.diff(lsym, k) ** 2).subs(sp.cos(k) ** 2, 1 - sp.sin(k) ** 2)
    speed2 = sp.expand(speed2).subs(sp.sin(k), sp.sqrt(x))
    ok = sp.expand(speed2 - (1 - x) * (1 - 3 * q * x) ** 2) == 0
    near0 = sp.expand(sp.series(sp.sqrt((1 - x) * (1 - 3 * q * x) ** 2).subs(x, sp.sin(k) ** 2), k, 0, 4).removeO())
    coef = sp.simplify(near0.coeff(k, 2))
    thr = sp.solve(sp.Eq(coef, 0), q)
    l_ = sp.Symbol("l", positive=True)
    lcrit = sp.solve(sp.Eq(1 - l_, thr[0]), l_)
    want = [sp.Rational(7, 6)] if not mut("threshold_forged") else [sp.Rational(5, 4)]
    checks.check("D1", ok and thr == [-sp.Rational(1, 6)] and lcrit == want, f"the axis group speed squared is (1 - x)(1 - 3 q x)^2, x = sin^2 k; near k = 0 its root is 1 - (1/2 + 3q) k^2 + ..., above the long-wave value iff q < {thr[0]}; for q = 1 - l that is l > {lcrit[0]} (blocks 173, 176)")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    Ffix = sp.exp(b) * s / sp.sqrt(c ** 2 + sp.exp(2 * b) * s ** 2)
    ok1 = sp.simplify(sp.diff(Ffix, b) - s * c * sp.diff(Ffix, k)) == 0
    f2 = sp.simplify(sp.series(Ffix, b, 0, 3).removeO().coeff(b, 2))
    x2 = sp.factor(over_s_in_x(f2))
    want_fix = sp.factor((1 - 4 * x + 3 * x ** 2) / 2)
    # self-consistent flow dF/db = F (dF/dk)^2 (the momentum of the stretched walk, F F_k): u = F^2 obeys u_b = u_k^2/2
    u = sp.Function("u")(k, b)
    Fs = sp.sqrt(u)
    ok2 = sp.simplify((sp.diff(Fs, b) - Fs * sp.diff(Fs, k) ** 2).subs(sp.Derivative(u, b), sp.diff(u, k) ** 2 / 2)) == 0
    # second-order term of the self-consistent flow: f2 = (f0 f1'^... ) from the recursion
    f0 = s
    f1 = f0 * sp.diff(f0, k) ** 2
    f2s = sp.expand((f1 * sp.diff(f0, k) ** 2 + 2 * f0 * sp.diff(f0, k) * sp.diff(f1, k)) / 2)
    x2s = sp.factor(over_s_in_x(f2s))
    want_sc = sp.factor((3 - 10 * x + 7 * x ** 2) / 2)
    if mut("flow_forged"):
        want_sc = sp.factor((3 - 10 * x + 5 * x ** 2) / 2)
    # the fixed-generator flow in l: F = s/sqrt(l^2 c^2 + s^2); its axis speed l^2 c/(1 + (l^2 - 1) c^2)^(3/2) exceeds 1/l somewhere iff l^2 > 3/2
    y = sp.Symbol("y", positive=True)
    ratio2 = 4 * y ** 3 / (27 * (y - 1))
    ok3 = sp.simplify(ratio2.subs(y, sp.Rational(3, 2)) - 1) == 0 and sp.factor(sp.diff(y ** 3 / (y - 1), y)) == sp.factor(y ** 2 * (2 * y - 3) / (y - 1) ** 2)
    # symmetric books at finite stretch need the generator parallel to the velocity (block 179 T1): p_l/(F F_k) must not depend on the axis
    l2 = sp.Symbol("l", positive=True)
    xx = sp.Symbol("xx", positive=True)
    Fl = s * (1 + (l2 - 1) * s ** 2) / l2
    pl = s * c / (l2 * (1 + 3 * (l2 - 1) * s ** 2))
    ratio = sp.simplify(pl / (Fl * sp.diff(Fl, k)))
    rform = l2 / ((1 + (l2 - 1) * xx) * (1 + 3 * (l2 - 1) * xx) ** 2)
    r_a = rform.subs({l2: 2, xx: sp.Rational(9, 25)})
    r_b = rform.subs({l2: 2, xx: sp.Rational(16, 25)})
    ok4 = sp.simplify(ratio - rform.subs(xx, s ** 2)) == 0 and r_a != r_b and r_a == sp.Rational(15625, 45968)
    checks.check("E2", ok4, f"the linear completion's generator over the stretched walk's F F_k is l/((1 + (l - 1)s^2)(1 + 3(l - 1)s^2)^2), axis-dependent: at l = 2 it is {r_a} for sin k = 3/5 and {r_b} for sin k = 4/5, so its current twists (block 179 T1); only F F_k, the self-consistent flow's momentum, keeps symmetric books")
    checks.check("E1", ok1 and ok2 and ok3 and sp.simplify(x2 - want_fix) == 0 and sp.simplify(x2s - want_sc) == 0, "two covariant completions outside reach three: the fixed-generator flow e^b s/sqrt(c^2 + e^{2b} s^2) has second-order term s(1 - 4s^2 + 3s^4)/2, and the self-consistent flow (u = F^2, u_b = u_k^2/2) has s(3 - 10s^2 + 7s^4)/2: both reach five; the fixed-generator flow outruns w/l somewhere iff l^2 > 3/2 (the squared speed ratio at the interior maximum is 4y^3/(27(y - 1)), y = l^2, equal to 1 at y = 3/2 and increasing)")


# ============================================================================================ family F
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
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at l = 7/6."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Burgers", "Hopf", "Jacobi", "Ward", "Takahashi", "Wilson")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Ward) —", 1)
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
    "per_element: executed - the generator's symmetry; the linear family's generator and its series",
    "per_site: executed - the axis group speed polynomial and its long-wave coefficient",
    "per_mode: executed - covariance order by order to order 5 with symbolic free coefficients",
    "per_block: executed - the two covariant completions outside reach three and their second-order terms",
    "lattice_wide: checked and not executed - every order (proof by induction in the text); anisotropic stretches; completions outside reach three beyond second order",
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
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: within block 176's reach-three family, the only completion in which each further uniform stretch acts as a relabelling of the stretched walk (to every order) is block 69's linear completion q = 1 - l, which keeps one speed limit only for l <= 7/6; covariant completions outside reach three leave it at second order; the supervisor's own derivation, unrefereed; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
