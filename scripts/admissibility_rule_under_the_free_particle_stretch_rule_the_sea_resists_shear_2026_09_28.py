#!/usr/bin/env python3
"""Exact checks: under the free-particle stretch rule (blocks 184, 185, 187; pushed) the filled negative-energy sea's energy per site
RISES at second order under volume-preserving shear, for both shear classes, whereas under block 176's reach-three completions (block
183, pushed) it falls. (T1) For any per-axis completion F = s - lam s c^2 + lam^2 s(1/2 + a s^2 + b s^4) + O(lam^3), the sea's energy
E_sea = -avg_k |F| has second-order term -sum_a lam_a^2 <s_a^2 (1/2 + a s_a^2 + b s_a^4)/|s|> - (1/2)<(sum lam_a^2 s_a^2 c_a^4 -
(sum lam_a s_a^2 c_a^2)^2/|s|^2)/|s|> (block 183 T2 is b = 0, a = -(1 + q2)). (T2) Block 184's rule has a = -4, b = 7/2. (T3) For a
diagonal volume-preserving stretch the second-order energy is exactly 0 on the side-4 torus and positive on sides 6 and 8 under the
rule (4/27 + (34 sqrt 3 + 65 sqrt 6)/864 on side 6 for lam = (1, -1, 0)), negative under the reach-three completions with q2 = -1/2.
(T4) Through block 187's spectrum, the off-diagonal volume-preserving shear g = exp(eps S) raises it too (25/648 + (9 sqrt 6 - 8 sqrt 3)/1728
per eps^2 on side 6), and the diagonal case reproduces T3. The supervisor's own derivation, unrefereed. Blocks 69 and 147 as landed;
blocks 183, 184, 185 and 187 (pushed) placed and the facts used re-derived.

A (premises): landed block 69; landed block 147's sea (filled negative band, energy per site -average E); the axioms.
B (T1): the second-order expansion of |F| for a per-axis completion.
C (T2): block 184's rule at second order in lam = log l: a = -4, b = 7/2 (from the closed form).
D (T3): exact diagonal second-order energies on sides 4, 6, 8 for the rule and for q2 = -1/2.
E (T4): block 187's second-order spectrum along g = exp(eps S); exact off-diagonal and diagonal values on sides 4, 6, 8.
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
    "docs/ADMISSIBILITY_RULE_UNDER_THE_FREE_PARTICLE_STRETCH_RULE_THE_SEA_RESISTS_SHEAR_BOTH_SHEAR_CLASSES_RAISE_ITS_ENERGY_BOUNDED_THEOREM_NOTE_2026-09-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/ADMISSIBILITY_RULE_THE_MEMBERS_ZERO_MODE_TESTS_THE_ZERO_OF_ENERGY_IF_THE_MEMBER_SEES_THE_HALF_FILLED_SEA_A_CLOSED_LATTICE_BOUNCES_OR_CANNOT_MOVE_BOUNDED_THEOREM_NOTE_2026-09-25.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_under_the_free_particle_stretch_rule_the_sea_resists_shear_both_shear_classes_raise_its_energy_bounded_theorem_note_2026-09-28"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED69 = (
    "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`",
)
LANDED147 = (
    "Counting each reduced-zone pair once gives the sea energy per site",
    "`-average_k sqrt(mu²+sum sin²(k)/ell²)`",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "expansion_forged": "B",
    "rule_forged": "C",
    "diag_forged": "D",
    "offdiag_forged": "E",
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
KS = sp.symbols("k1:4", real=True)


def labels(L):
    return [(sp.nsimplify(sp.sin(sp.Rational(2 * j, L) * sp.pi)), sp.nsimplify(sp.cos(sp.Rational(2 * j, L) * sp.pi))) for j in range(L)]


def e2_diag(L, lam, a, b, mu2=0):
    """exact second-order coefficient of E_sea = -avg |F| for the per-axis completion with second-order term s(1/2 + a s^2 + b s^4)"""
    tot = sp.Integer(0)
    for (s1, c1), (s2, c2), (s3, c3) in itertools.product(labels(L), repeat=3):
        s = [s1, s2, s3]
        c = [c1, c2, c3]
        S2 = sum(x ** 2 for x in s) + mu2
        if S2 == 0:
            continue
        S = sp.sqrt(S2)
        t1 = sum(lam[i] ** 2 * s[i] ** 2 * (sp.Rational(1, 2) + a * s[i] ** 2 + b * s[i] ** 4) for i in range(3)) / S
        v2 = sum(lam[i] ** 2 * s[i] ** 2 * c[i] ** 4 for i in range(3))
        sv = sum(lam[i] * s[i] ** 2 * c[i] ** 2 for i in range(3))
        tot += -(t1 + (v2 - sv ** 2 / S2) / (2 * S))
    return sp.nsimplify(sp.radsimp(sp.simplify(tot / L ** 3)))


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t69, t147 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note and len(CLAIM_ID) <= 195, f"the note is present and carries its claim id ({len(CLAIM_ID)} characters) and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its stretch rule and the sea are supplied)")
    needles = list(LANDED147)
    if mut("landed_quote_forged"):
        needles[0] = needles[0].replace("once", "twice")
    checks.check("A3", all(n in t69 for n in LANDED69) and all(n in t147 for n in needles), "landed block 69: the uniform form; landed block 147: the filled sea's energy per site counts each reduced-zone pair once")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    s = sp.symbols("s1:4", positive=True)
    d1 = sp.symbols("d1:4", real=True)
    d2 = sp.symbols("e1:4", real=True)
    t = sp.Symbol("t")
    F = [s[i] + t * d1[i] + t ** 2 * d2[i] for i in range(3)]
    norm = sp.sqrt(sum(f_ ** 2 for f_ in F))
    second = sp.simplify(sp.diff(norm, t, 2).subs(t, 0) / 2)
    S = sp.sqrt(sum(x ** 2 for x in s))
    sd = sum(s[i] * d1[i] for i in range(3))
    want = sum(s[i] * d2[i] for i in range(3)) / S + (sum(x ** 2 for x in d1) - sd ** 2 / S ** 2) / (2 * S)
    if mut("expansion_forged"):
        want = sum(s[i] * d2[i] for i in range(3)) / S + (sum(x ** 2 for x in d1) - sd ** 2 / S ** 2) / S
    ok = sp.simplify(second - want) == 0
    checks.check("B1", ok, "the second-order term of |s + t d1 + t^2 d2| is s.d2/|s| + (|d1|^2 - (s.d1)^2/|s|^2)/(2|s|); with d1_a = -lam_a s_a c_a^2 and d2_a = lam_a^2 s_a(1/2 + a s_a^2 + b s_a^4), E_sea's second-order term is -sum_a lam_a^2 <s_a^2(1/2 + a s_a^2 + b s_a^4)/|s|> - (1/2)<(sum lam_a^2 s_a^2 c_a^4 - (sum lam_a s_a^2 c_a^2)^2/|s|^2)/|s|> (block 183 T2: b = 0, a = -(1 + q2))")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    k, lam = sp.symbols("k lam", real=True)
    s, c = sp.sin(k), sp.cos(k)
    # block 184's rule in tau = (1 - l^2)/2: F = s + tau s c^2 + tau^2 s(3 - 10 s^2 + 7 s^4)/2 + O(tau^3) (block 182 T4(b), 184 T2); with l = e^lam
    tau = (1 - sp.exp(2 * lam)) / 2
    Ft = s + tau * s * c ** 2 + tau ** 2 * s * (3 - 10 * s ** 2 + 7 * s ** 4) / 2
    ser = sp.expand(sp.series(Ft, lam, 0, 3).removeO())
    x = sp.Symbol("x")
    c1 = sp.simplify(ser.coeff(lam, 1) + s * c ** 2)
    c2 = sp.expand(sp.expand_trig(ser.coeff(lam, 2)).subs(c ** 2, 1 - s ** 2))
    want_b = sp.Rational(7, 2)
    if mut("rule_forged"):
        want_b = sp.Rational(5, 2)
    ok2 = sp.simplify(c2 - s * (sp.Rational(1, 2) - 4 * s ** 2 + want_b * s ** 4)) == 0
    checks.check("C1", c1 == 0 and ok2, "block 184's rule at second order in lam = log l: F = s - lam s c^2 + lam^2 s(1/2 - 4 s^2 + (7/2) s^4) + O(lam^3), so a = -4 and b = 7/2 (reach five), outside block 176's reach-three family")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    lam = (1, -1, 0)
    vals = {L: e2_diag(L, lam, -4, sp.Rational(7, 2)) for L in (4, 6, 8)}
    r3 = {L: e2_diag(L, lam, -sp.Rational(1, 2), 0) for L in (4, 6, 8)}
    want6 = sp.Rational(4, 27) + (34 * sp.sqrt(3) + 65 * sp.sqrt(6)) / 864
    if mut("diag_forged"):
        want6 = -want6
    ok = vals[4] == 0 and sp.simplify(vals[6] - want6) == 0 and vals[6] > 0 and vals[8] > 0 and r3[4] == 0 and r3[6] < 0 and r3[8] < 0
    # the quadratic form on traceless diagonal stretches is a multiple of sum lam^2 (the two traceless directions form one class)
    ratio = sp.simplify(e2_diag(6, (1, 1, -2), -4, sp.Rational(7, 2)) / vals[6])
    # the massive sea (block 139's staggered mass: E^2 = |F|^2 + mu^2, the mass unchanged by the rule, block 185 T1)
    m1 = e2_diag(6, lam, -4, sp.Rational(7, 2), sp.Rational(1, 4))
    m2 = e2_diag(6, lam, -4, sp.Rational(7, 2), 1)
    q1 = e2_diag(6, lam, -sp.Rational(1, 2), 0, sp.Rational(1, 4))
    checks.check("D2", m1 > 0 and m2 > 0 and q1 < 0, f"with block 139's staggered mass (mu^2 = 1/4 and 1) the rule's side-6 values stay positive ({m1}, {m2}); the reach-three q2 = -1/2 value at mu^2 = 1/4 stays negative ({q1})")
    checks.check("D1", ok and ratio == 3, f"for lam = (1, -1, 0) the rule's second-order sea energy is 0 on side 4, {vals[6]} on side 6 and {vals[8]} on side 8 (both positive), while block 183's reach-three completions with q2 = -1/2 give {r3[6]} and {r3[8]} (negative); (1, 1, -2) gives three times the side-6 value, as sum lam^2 does")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    p = [sp.sin(2 * x_) for x_ in KS]
    W0 = sum(sp.sin(x_) ** 2 for x_ in KS)

    def w12(S):
        S = sp.Matrix(S)
        P = sp.Matrix(p)
        w1 = -sp.Rational(1, 4) * (P.T * S * P)[0]
        w2 = -sp.Rational(1, 8) * (P.T * S * S * P)[0] - sp.Rational(1, 4) * sum(S[a, b] * p[a] * sp.diff(w1, KS[b]) for a in range(3) for b in range(3))
        return sp.expand(w1), sp.expand(w2)

    def e2_metric(L, S):
        w1, w2 = w12(S)
        f = sp.lambdify(KS, [w1, w2, W0], "sympy")
        tot = sp.Integer(0)
        ks = [sp.Rational(2 * j, L) * sp.pi for j in range(L)]
        for kk in itertools.product(ks, repeat=3):
            a1, a2, a0 = [sp.nsimplify(sp.simplify(v)) for v in f(*kk)]
            if a0 == 0:
                continue
            tot += -(a2 / (2 * sp.sqrt(a0)) - a1 ** 2 / (8 * a0 ** sp.Rational(3, 2)))
        return sp.nsimplify(sp.radsimp(sp.simplify(tot / L ** 3)))

    Sd = [[1, 0, 0], [0, -1, 0], [0, 0, 0]]
    So = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
    od = {L: e2_metric(L, So) for L in (4, 6, 8)}
    dg = {L: e2_metric(L, Sd) for L in (6, 8)}
    want6 = sp.Rational(25, 648) + (9 * sp.sqrt(6) - 8 * sp.sqrt(3)) / 1728
    if mut("offdiag_forged"):
        want6 = -want6
    ok_od = od[4] == 0 and sp.simplify(od[6] - want6) == 0 and od[6] > 0 and od[8] > 0
    # consistency: g = exp(eps diag(1, -1, 0)) is lam = (eps/2, -eps/2, 0), a quarter of T3's lam = (1, -1, 0)
    ok_dg = all(sp.simplify(dg[L] - e2_diag(L, (1, -1, 0), -4, sp.Rational(7, 2)) / 4) == 0 for L in (6, 8))
    checks.check("E1", ok_od and ok_dg, f"through block 187's spectrum along g = exp(eps S) (W = W0 + eps w1 + eps^2 w2 with w1 = -(1/4) p.S.p, w2 = -(1/8) p.S^2.p - (1/4) sum S_ab p_a d_b w1), the off-diagonal shear S = e1 e2 + e2 e1 raises the sea's energy: {od[6]} per eps^2 on side 6, {od[8]} on side 8, 0 on side 4; the diagonal S = diag(1, -1, 0) reproduces a quarter of T3's values exactly")


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
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at q2*."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Burgers", "Hopf", "Jacobi", "Ward", "Takahashi", "Wilson", "Kepler", "Bessel", "Liouville", "Paley", "Wiener", "Bloch", "Cauchy", "Parker", "Friedmann")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_g(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Parker) —", 1)
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
    "per_element: executed - the second-order expansion of |F|; the rule's second-order term",
    "per_site: executed - exact label sums on sides 4, 6, 8 for the diagonal stretch, the rule and q2 = -1/2; the massive sea on side 6",
    "per_mode: executed - block 187's second-order spectrum along exp(eps S) for both shear classes",
    "per_block: executed - the diagonal consistency between the two routes; the (1, 1, -2) ratio",
    "lattice_wide: checked and not executed - the infinite lattice (floating point in scratch, recorded in the note); long shear waves; the massive sea beyond side 6",
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
    family_g(checks, texts[0])
    family_h(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: under the free-particle stretch rule the filled sea's energy rises at second order under volume-preserving shear (both classes; exact on sides 6 and 8, zero on side 4), reversing block 183's reach-three result; the supervisor's own derivation, unrefereed; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
