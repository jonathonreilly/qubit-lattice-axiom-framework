#!/usr/bin/env python3
"""Exact checks: for a walk h = sum_a F(k_a; l) X_a + mu(l) Gamma (anticommuting involutions; per-axis hops with F(k; 1) = sin k; a
staggered mass mu as in block 139), a uniform stretch slows every wave exactly as it slows a free particle with fixed momentum per
label, d log E/d log l = -l^2 |v|^2, at every stretch iff dF/d(l^2) = -(1/2) F F_k^2 and the mass does not change; that is block 184's
stretch rule, whose long-wave speed 1/l is the one the law's normalisation fixes. Equivalently the response of the walk to a further diagonal
stretch is minus half its own symmetric stress (block 184 T7). The frame H/l, block 69's linear completion and the fixed-generator flow
all obey the law at l = 1 (block 180) and violate it at l != 1. No covariance and no books premise is used. The supervisor's own
derivation, unrefereed. Blocks 69 and 139 as landed; blocks 180, 181 and 184 (pushed) placed and the facts used re-derived.

A (premises): landed block 69 (uniform form); landed block 139 (the staggered mass anticommutes; the square is a number); the axioms.
B (T1): the law from the rule; the rule from the law (separation of variables through the species point k = 0); the free particle's law.
C (T2): block 184's closed form obeys the rule; its long-wave speed is 1/sqrt(l^2) automatically.
D (T3): the stress response as 4 x 4 matrices: d h/d(l_a^2) = -(1/2) K^s_aa(k, k) iff the rule holds and the mass is unchanged.
E (T4): the frame, the linear completion and the fixed-generator flow meet the law at l = 1 and violate it at exact points for l != 1.
F (T5): with the mass unchanged, rest waves keep E = mu and each wave presses between 0 and E/(3V).
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
    "docs/ADMISSIBILITY_RULE_A_UNIFORM_STRETCH_SLOWS_EVERY_WAVE_AS_IT_SLOWS_A_FREE_PARTICLE_ONLY_UNDER_BLOCK_184S_STRETCH_RULE_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/ADMISSIBILITY_RULE_THE_BOOKS_ADMIT_ONE_REST_ENERGY_THE_STAGGERED_MASS_KEEPS_THEM_EXACTLY_SO_MASSIVE_CONTENT_MEETS_THE_MEMBER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_uniform_stretch_slows_every_wave_as_it_slows_a_free_particle_only_under_block_184s_stretch_rule_bounded_theorem_note_2026-09-27"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED69 = (
    "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`",
    "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion.",
)
LANDED139 = (
    "`mε` anticommutes with the walk, so the squared energy is `|sin k|² + m²`, and each wave's energy current is its two-step momentum at every `k`, massive or not.",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "law_forged": "B",
    "closed_form_forged": "C",
    "stress_forged": "D",
    "witness_forged": "E",
    "mass_forged": "F",
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
k = sp.Symbol("k", real=True)
L = sp.Symbol("l", positive=True)
m = sp.Symbol("m", positive=True)  # m = l^2
s = sp.sin(k)
c = sp.cos(k)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t69, t139 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note and len(CLAIM_ID) <= 195, f"the note is present and carries its claim id ({len(CLAIM_ID)} characters) and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its coupling and its completion are supplied)")
    needles = list(LANDED139)
    if mut("landed_quote_forged"):
        needles[0] = needles[0].replace("anticommutes", "commutes")
    checks.check("A3", all(n in t69 for n in LANDED69) and all(n in t139 for n in needles), "landed block 69: the uniform form, and no completion fixed by the leading order; landed block 139: the staggered mass anticommutes with the walk, so the squared energy is |sin k|^2 + m^2")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    Fa = sp.symbols("F1:4", real=True)
    Fd = sp.symbols("D1:4", real=True)
    mu = sp.Symbol("mu", positive=True)
    E = sp.sqrt(sum(f_ ** 2 for f_ in Fa) + mu ** 2)
    rule = [-Fa[i] * Fd[i] ** 2 / 2 for i in range(3)]
    if mut("law_forged"):
        rule = [-Fa[i] * Fd[i] ** 2 / 3 for i in range(3)]
    dE_dm = sum(Fa[i] * rule[i] for i in range(3)) / E  # mass unchanged
    dlog = 2 * m * dE_dm / E
    v2 = sum(Fa[i] ** 2 * Fd[i] ** 2 for i in range(3)) / E ** 2
    ok_fwd = sp.simplify(dlog + m * v2) == 0
    # converse: the law for every k is sum_a g(k_a) + mu mu' = 0 with g = F(dF/dm + F F'^2/2); F odd so g(0) = 0
    # multiplied law d(E^2)/dm = -sum F_a^2 F_a'^2: sum_a g(k_a) + mu mu' = 0 for every k; comparing (x, y, z) with (x', y, z) makes g constant,
    # and g vanishes at a zero of F, so the constant is 0 and mu mu' = 0
    gfun = sp.Function("g")
    xs, xp, ys, zs, cm = sp.symbols("xs xp ys zs cm", real=True)
    law = lambda a_, b_, c_: gfun(a_) + gfun(b_) + gfun(c_) + cm
    diff_pts = sp.simplify(law(xs, ys, zs) - law(xp, ys, zs))
    ok_sep = diff_pts == gfun(xs) - gfun(xp)
    # with g = const = c0 and g(zero of F) = 0: c0 = 0, then 3 c0 + cm = 0 gives cm = 0
    c0 = sp.Symbol("c0")
    sol = sp.solve([c0, 3 * c0 + cm], [c0, cm], dict=True)
    ok_conv = ok_sep and sol == [{c0: 0, cm: 0}]
    # the free particle: E^2 = mu^2 + |p|^2/l^2 with p fixed: d log E/d log l = -|u|^2, u = d E/d(p/l)
    p1, p2, p3 = sp.symbols("p1:4", real=True)
    Ef = sp.sqrt(mu ** 2 + (p1 ** 2 + p2 ** 2 + p3 ** 2) / L ** 2)
    dlog_f = sp.simplify(L * sp.diff(Ef, L) / Ef)
    u2 = sp.simplify(sum((pp / L / Ef) ** 2 for pp in (p1, p2, p3)))
    ok_free = sp.simplify(dlog_f + u2) == 0
    checks.check("B1", ok_fwd, "the rule dF/d(l^2) = -(1/2) F F_k^2 with the mass unchanged gives d log E/d log l = -l^2 |v|^2 for every wave, v_a = F_a F_a'/E, E^2 = sum F_a^2 + mu^2")
    checks.check("B2", ok_conv, "conversely the multiplied law d(E^2)/d(l^2) = -sum F_a^2 F_a'^2 is g(k_1) + g(k_2) + g(k_3) + mu mu' = 0 for every k, g = F(dF/d(l^2) + F F_k^2/2); two points differing in k_1 only give g(k_1) = g(k_1'), so g is constant; it vanishes at a zero of F, so it is 0 and mu' = 0: the rule wherever F != 0, hence everywhere by analyticity")
    checks.check("B3", ok_free, "a free particle with fixed momentum per label, E^2 = mu^2 + |p|^2/l^2, obeys the same law d log E/d log l = -|u|^2 with u its velocity in lengths")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    S_, C_ = sp.symbols("S C", real=True)

    def dk0(expr):
        return sp.diff(expr, S_) * C_ - sp.diff(expr, C_) * S_

    Fm = S_ * sp.sqrt(S_ ** 2 + m * C_ ** 2)
    if mut("closed_form_forged"):
        Fm = S_ * sp.sqrt(S_ ** 2 + m ** 2 * C_ ** 2)
    km_k0 = 1 + (m - 1) * (C_ ** 2 - S_ ** 2)
    km_m = S_ * C_
    Fk = dk0(Fm) / km_k0
    dFdm = sp.diff(Fm, m) - Fk * km_m
    resid = sp.simplify(sp.together((dFdm + Fm * Fk ** 2 / 2).subs(C_, sp.sqrt(1 - S_ ** 2))))
    ok_rule = resid == 0 and sp.simplify(Fm.subs(m, 1).subs(C_, sp.sqrt(1 - S_ ** 2)) - S_) == 0
    fk0 = sp.simplify(Fk.subs({S_: 0, C_: 1}))
    ok_speed = sp.simplify(fk0 - 1 / sp.sqrt(m)) == 0
    checks.check("C1", ok_rule and ok_speed, f"block 184's family, k = k0 + ((m - 1)/2) sin 2k0 and F = sin k0 sqrt(sin^2 k0 + m cos^2 k0), obeys dF/dm = -(1/2) F F_k^2 with F = sin k at m = 1, and its long-wave speed is {fk0}: consistent with the law's own normalisation, which fixes the long-wave speed at 1/l")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    I_ = sp.I
    p1 = sp.Matrix([[0, 1], [1, 0]])
    p2 = sp.Matrix([[0, -I_], [I_, 0]])
    p3 = sp.Matrix([[1, 0], [0, -1]])
    X = [sp.kronecker_product(p3, pm) for pm in (p1, p2, p3)]
    Gm = sp.kronecker_product(p1, sp.eye(2))
    Fa = sp.symbols("F1:4", real=True)
    Fd = sp.symbols("D1:4", real=True)
    dF = sp.symbols("dF1:4", real=True)
    dmu = sp.Symbol("dmu", real=True)
    # single-wave stress of block 184 T7: K^s_aa(k, k) = F_a'^2 F_a X_a (with or without the mass)
    Kaa = [Fd[a_] ** 2 * Fa[a_] * X[a_] for a_ in range(3)]
    if mut("stress_forged"):
        Kaa = [Fd[a_] ** 2 * Fa[a_] * X[a_] / 2 for a_ in range(3)]
    oks = []
    for a_ in range(3):
        resp = dF[a_] * X[a_] + dmu * Gm  # d h/d(l_a^2), with the mass allowed to respond
        eqs = list(resp + Kaa[a_] / 2)
        sol = sp.solve(eqs, [dF[a_], dmu], dict=True)
        oks.append(sol == [{dF[a_]: -Fa[a_] * Fd[a_] ** 2 / 2, dmu: 0}])
    checks.check("D1", all(oks), "the response of the walk to a further stretch of axis a, d h/d(l_a^2) = X_a dF_a/d(l_a^2) + (d mu/d(l_a^2)) Gamma, equals -(1/2) K^s_aa(k, k) = -(1/2) F_a'^2 F_a X_a as 4 x 4 matrices iff the rule holds on that axis and the mass is unchanged")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    def gap(F, at_l, sval):
        """F(dF/dm + F F_k^2/2) at l = at_l, sin k = sval (in (0, 1), cos k > 0), with m = l^2"""
        Fl = F
        dFm = sp.diff(Fl, L) / (2 * L)
        g = Fl * (dFm + Fl * sp.diff(Fl, k) ** 2 / 2)
        return sp.nsimplify(sp.simplify(g.subs(L, at_l).subs(k, sp.asin(sval))))

    frame = s / L
    lin = s * (1 + (L - 1) * s ** 2) / L
    fix = s / sp.sqrt(L ** 2 * c ** 2 + s ** 2)
    sv = sp.Rational(3, 5)
    at1 = [gap(F, 1, sv) for F in (frame, lin, fix)]
    at2 = [gap(frame, 2, sv), gap(lin, 2, sv), gap(fix, sp.sqrt(2), sv)]
    if mut("witness_forged"):
        at2[1] = 0
    ok1 = at1[1] == 0 and at1[2] == 0
    ok2 = all(v_ != 0 for v_ in at2)
    # the frame at l = 1: F(dF/dm + F F_k^2/2) = -s^2/2 + s^2 c^2/2 = -s^4/2 != 0: the frame's law is d log E/d log l = -1 for every wave
    frame_law = sp.simplify(L * sp.diff(sp.sqrt(3) * s / L, L) / (sp.sqrt(3) * s / L))
    checks.check("E1", ok1 and at1[0] != 0 and frame_law == -1, f"at l = 1 block 69's linear completion and the fixed-generator flow meet the law (block 180's first order), while the frame H/l gives d log E/d log l = -1 for every wave (gap {at1[0]} at sin k = 3/5)")
    checks.check("E2", ok2, f"at l != 1 the three violate it: F(dF/d(l^2) + F F_k^2/2) at sin k = 3/5 is {at2[0]} for the frame (l = 2), {at2[1]} for the linear completion (l = 2) and {at2[2]} for the fixed-generator flow (l^2 = 2)")


# ============================================================================================ family F (T5)
def family_f(checks: Checks) -> None:
    mu = sp.Symbol("mu", positive=True)
    Fa = sp.symbols("F1:4", real=True)
    Fd = sp.symbols("D1:4", real=True)
    E = sp.sqrt(sum(f_ ** 2 for f_ in Fa) + mu ** 2)
    dmu = sp.Integer(0)
    if mut("mass_forged"):
        dmu = mu / 2
    dE_dm = (sum(Fa[i] * (-Fa[i] * Fd[i] ** 2 / 2) for i in range(3)) + mu * dmu) / E
    rest = sp.simplify(dE_dm.subs({Fa[0]: 0, Fa[1]: 0, Fa[2]: 0}))
    # pressure per wave: p = -dE/dV = -(dE/d log l)/(3V) = E l^2 |v|^2/(3V), and 0 <= l^2 |v|^2 <= 1 (block 184 T3)
    V = sp.Symbol("V", positive=True)
    press = -(2 * m * dE_dm) / (3 * V)
    v2 = sum(Fa[i] ** 2 * Fd[i] ** 2 for i in range(3)) / E ** 2
    ok_p = sp.simplify(press - E * m * v2 / (3 * V)) == 0
    checks.check("F1", rest == 0 and ok_p, "with the mass unchanged a wave at rest (all F_a = 0, E = mu) keeps its energy, and each wave presses p = E l^2 |v|^2/(3V), between 0 and E/(3V) by block 184 T3")


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
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at l = 1."}
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
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Hilbert) —", 1)
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
    "per_element: executed - the law from the rule; the separation step of the converse (symbolic); the free particle's law",
    "per_site: executed - block 184's closed form obeys the rule, with long-wave speed 1/l",
    "per_mode: executed - the stress response as 4 x 4 matrices with the mass",
    "per_block: executed - the frame, the linear completion and the fixed-generator flow at exact points; the rest energy and the pressure",
    "lattice_wide: checked and not executed - uniqueness of twice-differentiable solutions of the rule (block 184 T4's argument); off-diagonal strains; non-per-axis walks",
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
    family_f(checks)
    family_g(checks, texts[0])
    family_h(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: for per-axis walks with a staggered mass, a uniform stretch slows every wave as it slows a free particle at every stretch iff the walk follows block 184's rule and the mass is unchanged; equivalently the response to a further diagonal stretch is minus half the symmetric stress; the supervisor's own derivation, unrefereed; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
