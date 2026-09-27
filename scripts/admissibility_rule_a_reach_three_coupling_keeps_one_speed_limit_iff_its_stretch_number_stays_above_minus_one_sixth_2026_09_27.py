#!/usr/bin/env python3
"""Exact checks: every reach-three coupling of the stretched lengths at uniform stretch has one number q (l s = sin k (1 - q sin^2 k));
it keeps the long-wave speed w/l as the fastest, and keeps every ray's bending within the long-wave ratio, exactly when
q >= -1/6 (within q <= 2/3); block 69's linear completion q = 1 - l breaks this beyond l = 7/6, and the smooth completion
q = (1 - l)/sqrt(1 + 36(l - 1)^2), which agrees with block 69 at first order in the strain, never does (the supervisor's own
derivation, unrefereed). Blocks 59, 60 and 69 as landed; block 173 (pushed) placed.

A (premises): landed block 69 T4's uniform-strain symbol and its open completion; the axioms.
B (T1): odd symbols of reach at most three are span{sin k, sin k cos^2 k} = span{sin k, sin 3k}; with long-wave speed w/l they are
   l s = sin k (1 - q sin^2 k); the frame is q = 0, block 69's linear completion 1 + b = 1/l is q = 1 - l.
C (T2): the axis group speed squared is (1 - x)(1 - 3qx)^2, x = sin^2 k, and 1 - speed^2 = x S(x, q) with S >= 0 on [0, 1] x
   [-1/6, 2/3]; near k = 0 the speed is 1 - (1/2 + 3q) k^2 + O(k^4), above 1 iff q < -1/6; in every direction |grad|s|| <= max|s_a'|.
D (T3): A_a = l^2 (s'^2 + s s'') = 1 - x P(x, q) with P >= 0 on the same box; A_a = 1 - (2 + 12q) k^2 + O(k^4); rho_a =
   1 + l q' x/(1 - qx); with A <= 1 and 0 <= rho <= 1 the bending ratio A[1 + rho(R - 1)] is at most R.
E (T4): the completion q(l) = (1 - l)/sqrt(1 + 36(l - 1)^2): q = 1 - l + O((l - 1)^3), -1/6 < q < 1/6, q' = -(1 + 36(l - 1)^2)^(-3/2),
   and 1 - q + l q' >= 0 for all l > 0.
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
    "docs/ADMISSIBILITY_RULE_A_REACH_THREE_COUPLING_KEEPS_ONE_SPEED_LIMIT_IFF_ITS_STRETCH_NUMBER_STAYS_ABOVE_MINUS_ONE_SIXTH_AND_A_SMOOTH_COMPLETION_OF_BLOCK_69_DOES_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_reach_three_coupling_keeps_one_speed_limit_iff_its_stretch_number_stays_above_minus_one_sixth_and_a_smooth_completion_of_block_69_does_bounded_theorem_note_2026-09-27"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED69 = (
    "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`",
    "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion.",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "family_forged": "B",
    "speed_threshold_forged": "C",
    "bending_poly_forged": "D",
    "completion_forged": "E",
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
k = sp.Symbol("k", real=True)
q, x, l = sp.symbols("q x l", real=True)


def ls_of(qv):
    return sp.sin(k) * (1 - qv * sp.sin(k) ** 2)


def in_x(expr):
    """rewrite a polynomial in sin k, cos k with even powers of cos k into x = sin^2 k"""
    e = sp.expand(sp.simplify(expr))
    e = e.subs(sp.cos(k) ** 2, 1 - sp.sin(k) ** 2)
    e = sp.expand(e).subs(sp.sin(k), sp.sqrt(x))
    return sp.expand(e)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t69 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its coupling to the lengths and its completion are supplied)")
    needles = list(LANDED69)
    if mut("landed_quote_forged"):
        needles[1] = "Common corner quadratic forms are a leading-order result and determine a nonlinear completion."
    checks.check("A3", all(n in t69 for n in needles), "landed block 69 T4: the uniform-strain symbol s_a + c_a sum_j B s_j c_j; its N1: the leading order does not determine a nonlinear completion")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    ok = sp.simplify(sp.sin(3 * k) - sp.sin(k) * (4 * sp.cos(k) ** 2 - 1)) == 0
    p_, q_ = sp.symbols("p q_", real=True)
    gen = sp.sin(k) * (p_ + q_ * sp.cos(k) ** 2)
    slope = sp.diff(gen, k).subs(k, 0)
    ok = ok and sp.simplify(slope - (p_ + q_)) == 0
    ok = ok and sp.simplify(gen.subs(p_, 1 - q_) - ls_of(q_)) == 0
    b = sp.Symbol("b")
    block69 = sp.sin(k) + sp.cos(k) * b * sp.sin(k) * sp.cos(k)
    lin = sp.simplify(l * block69.subs(b, 1 / l - 1))
    want = 1 - l if not mut("family_forged") else l - 1
    ok = ok and sp.simplify(lin - ls_of(want)) == 0
    checks.check("B1", ok, "odd symbols of reach at most three along an axis are span{sin k, sin k cos^2 k} = span{sin k, sin 3k}; with slope 1/l at k = 0 (long-wave speed w/l) they are l s = sin k (1 - q sin^2 k); the frame is q = 0 and block 69's linear completion 1 + b = 1/l is q = 1 - l")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    d1 = sp.diff(ls_of(q), k)
    speed2 = in_x(d1 ** 2)
    ok = sp.expand(speed2 - (1 - x) * (1 - 3 * q * x) ** 2) == 0
    S = 9 * q ** 2 * x ** 2 - 9 * q ** 2 * x - 6 * q * x + 6 * q + 1
    ok = ok and sp.expand(1 - speed2 - x * S) == 0
    # S >= 0 on x in [0, 1], q in [-1/6, 2/3]: S(0) = 6q + 1 >= 0, S(1) = 1, and the vertex x* = 1/2 + 1/(3q) lies outside [0, 1]
    ok = ok and sp.expand(S.subs(x, 0) - (6 * q + 1)) == 0 and sp.expand(S.subs(x, 1)) == 1
    xv = sp.solve(sp.diff(S, x), x)
    ok = ok and len(xv) == 1 and sp.simplify(xv[0] - (sp.Rational(1, 2) + 1 / (3 * q))) == 0
    ok = ok and (sp.Rational(1, 2) + 1 / (3 * sp.Rational(2, 3))) >= 1 and (sp.Rational(1, 2) + 1 / (3 * (-sp.Rational(1, 6)))) <= 0
    ser = sp.series(d1, k, 0, 4).removeO()
    thr = -sp.Rational(1, 6) if not mut("speed_threshold_forged") else -sp.Rational(1, 4)
    ok = ok and sp.simplify(ser.coeff(k, 2) + (sp.Rational(1, 2) + 3 * q)) == 0 and sp.solve(sp.Eq(sp.Rational(1, 2) + 3 * q, 0), q) == [thr]
    s1, s2, s3, d1_, d2_, d3_ = sp.symbols("s1 s2 s3 d1 d2 d3", real=True)
    grad2 = ((s1 * d1_) ** 2 + (s2 * d2_) ** 2 + (s3 * d3_) ** 2) / (s1 ** 2 + s2 ** 2 + s3 ** 2)
    M = sp.Symbol("M", positive=True)
    bound = sp.simplify(M ** 2 - grad2.subs({d1_: M, d2_: M, d3_: M}))
    ok = ok and bound == 0
    checks.check("C1", ok, "the axis group speed in units of w/l squared is (1 - x)(1 - 3qx)^2, x = sin^2 k, and 1 - speed^2 = x S(x, q) with S(0) = 6q + 1, S(1) = 1 and its vertex 1/2 + 1/(3q) outside [0, 1] for q in [-1/6, 2/3], so no axis wave outruns w/l there; near k = 0 the speed is 1 - (1/2 + 3q) k^2, above 1 iff q < -1/6; in any direction |grad |s||^2 = sum (s_a s_a')^2/|s|^2 <= max s_a'^2")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    f = ls_of(q)
    A = in_x(sp.diff(f, k) ** 2 + f * sp.diff(f, k, 2))
    P = 18 * q ** 2 * x ** 2 - 15 * q ** 2 * x - 16 * q * x + 12 * q + 2
    if mut("bending_poly_forged"):
        P = P + x
    ok = sp.expand(A - (1 - x * P)) == 0
    ok = ok and sp.expand(P.subs(x, 0) - (12 * q + 2)) == 0 and sp.expand(P.subs(x, 1) - (3 * q ** 2 - 4 * q + 2)) == 0
    ok = ok and sp.discriminant(3 * q ** 2 - 4 * q + 2, q) < 0
    xv = sp.solve(sp.diff(P, x), x)
    ok = ok and len(xv) == 1 and sp.simplify(xv[0] - (sp.Rational(5, 12) + 4 / (9 * q))) == 0
    ok = ok and (sp.Rational(5, 12) + 4 / (9 * sp.Rational(2, 3))) >= 1 and (sp.Rational(5, 12) + 4 / (9 * (-sp.Rational(1, 6)))) <= 0
    ser = sp.series(sp.diff(f, k) ** 2 + f * sp.diff(f, k, 2), k, 0, 3).removeO()
    ok = ok and sp.simplify(ser.coeff(k, 0) - 1) == 0 and sp.simplify(ser.coeff(k, 2) + (2 + 12 * q)) == 0
    qf = sp.Function("qf")
    s_l = sp.sin(k) * (1 - qf(l) * sp.sin(k) ** 2) / l
    rho = sp.simplify(-l * sp.diff(sp.log(s_l), l))
    ok = ok and sp.simplify(rho - (1 + l * sp.diff(qf(l), l) * sp.sin(k) ** 2 / (1 - qf(l) * sp.sin(k) ** 2))) == 0
    Av, rv, R = sp.symbols("A_v rho_v R", real=True)
    ok = ok and sp.simplify(R - Av * (1 + rv * (R - 1)) - ((1 - Av) * (1 + rv * (R - 1)) + (1 - rv) * (R - 1))) == 0
    checks.check("D1", ok, "A_a = l^2 (s'^2 + s s'') = 1 - x P(x, q), P(0) = 12q + 2, P(1) = 3q^2 - 4q + 2 > 0, vertex 5/12 + 4/(9q) outside [0, 1] for q in [-1/6, 2/3], so A_a <= 1 there; A_a = 1 - (2 + 12q) k^2 + O(k^4); rho_a = 1 + l q' x/(1 - qx); and R - A[1 + rho(R - 1)] = (1 - A)(1 + rho(R - 1)) + (1 - rho)(R - 1) >= 0 whenever A <= 1, 0 <= rho <= 1, R >= 1")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    v = sp.Symbol("v", real=True)                           # v = l - 1
    qv = -v / sp.sqrt(1 + 36 * v ** 2)
    if mut("completion_forged"):
        qv = -v / sp.sqrt(1 + 16 * v ** 2)
    ser = sp.series(qv, v, 0, 4).removeO()
    ok = sp.expand(ser - (-v + 18 * v ** 3)) == 0
    ok = ok and sp.limit(qv, v, sp.oo) == -sp.Rational(1, 6) and sp.limit(qv, v, -1) == 1 / sp.sqrt(37)
    dq = sp.simplify(sp.diff(qv, v))
    ok = ok and sp.simplify(dq + (1 + 36 * v ** 2) ** (-sp.Rational(3, 2))) == 0
    # 1 - q + l q' >= 0 for l = 1 + v > 0: with w = sqrt(1 + 36 v^2) >= 1 it reads w^2 (w + v) >= 1 + v
    w = sp.Symbol("w", positive=True)
    expr = 1 - qv + (1 + v) * dq
    lhs = sp.simplify(expr * w ** 3).subs(sp.sqrt(1 + 36 * v ** 2), w)
    ok = ok and sp.simplify(sp.expand(sp.simplify((1 - qv + (1 + v) * dq) * (1 + 36 * v ** 2) ** sp.Rational(3, 2))) - ((1 + 36 * v ** 2) * (sp.sqrt(1 + 36 * v ** 2) + v) - (1 + v))) == 0
    checks.check("E1", ok, "the completion q = (1 - l)/sqrt(1 + 36 (l - 1)^2): q = (1 - l) + 18 (l - 1)^3 + ..., agreeing with block 69 at first order; q -> -1/6 as l -> oo and q < 1/sqrt(37) on l > 0, so q stays in (-1/6, 1/6); q' = -(1 + 36(l - 1)^2)^(-3/2) < 0; and (1 - q + l q') w^3 = w^2 (w + v) - (1 + v) with w = sqrt(1 + 36 v^2) >= 1, v = l - 1, which is >= 0 for l > 0, so 0 <= rho_a <= 1")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 59, 60 and 69 as landed on main (the local ray comparison, the one-body field and the reach-three coupling at uniform strain) and places block 173 (a pushed branch); it reports which completions of the reach-three coupling keep one speed limit; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at q = -1/6."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Chebyshev) —", 1)
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
    "per_element: executed - the reach-three family and its one number q",
    "per_site: executed - speed and bending polynomials in x = sin^2 k on the box [0, 1] x [-1/6, 2/3]",
    "per_mode: executed - the long-wave expansions and the threshold q = -1/6",
    "per_block: executed - the smooth completion's series, bounds, slope and the rho inequality",
    "lattice_wide: checked and not executed - completions outside the reach-three family; sub-principal terms; the dynamics that would fix the completion",
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
    print(f"scope: the reach-three family l s = sin k (1 - q sin^2 k): no wave outruns w/l and no ray bends more than R times the fall iff q >= -1/6 (within q <= 2/3, with 0 <= rho <= 1); block 69's linear completion q = 1 - l fails beyond l = 7/6; the completion q = (1 - l)/sqrt(1 + 36(l - 1)^2) agrees at first order and never fails; the supervisor's own derivation, unrefereed; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
