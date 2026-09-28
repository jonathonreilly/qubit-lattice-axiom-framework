#!/usr/bin/env python3
"""Exact checks: if the member sees the filled sea (block 147's reading), the sea's second-order energy under uniform volume-preserving
strain enters the member's landed quadratic action (block 135) as a potential for its uniform traceless modes, which have no curvature
term. (T1) With L = [alpha tr(hdot^2) + beta (tr hdot)^2]/wbar + K wbar(u R1 + R2) - e u + (1/2) Theta.h and h = eps S (S traceless,
uniform), R1 = R2 = 0 and tr hdot = 0, so L = (alpha/wbar) tr(S^2) epsdot^2 - E2 eps^2 and omega^2 = wbar E2/(alpha tr S^2); at
alpha = K/4, omega^2 = 4 wbar E2/(K tr S^2). (T2) Under the free-particle rule E2 > 0 for both shear classes (block 190): the uniform
shear modes acquire a real gap. (T3) Under block 62's frame (H/l per axis) the second-order sea energy is -<sum lam_a^2 s_a^2/|s| -
(sum lam_a s_a^2)^2/(2|s|^3)>, negative for every nonzero stretch by the inequality (sum lam s^2)^2 <= (sum lam^2 s^2)(sum s^2): the modes
grow. (T4) Under block 183's reach-three completions with q2 = -1/2 they grow too. (T5) A vacuum whose energy depends on the volume
only, rho sqrt(det g), gives no second-order energy when det g = 1: no gap. The supervisor's own derivation, unrefereed. Blocks 69,
135, 147 and 150 as landed; blocks 183, 187 and 190 (pushed) placed and the facts used re-derived.

A (premises): landed block 135's quadratic action; landed block 147's sea; landed block 150 T4 (the sea's inertia); the axioms.
B (T1): the uniform traceless mode's equation and frequency.
C (T2): E2 under the free-particle rule through block 187's spectrum (both classes; exact on sides 6, 8).
D (T3): the frame's second-order formula and its sign; an exact side-6 value.
E (T4): block 183's reach-three completion with q2 = -1/2 on sides 6, 8.
F (T5): det exp(eps S) = 1 for traceless S.
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
    "docs/ADMISSIBILITY_RULE_IF_THE_MEMBER_SEES_THE_SEA_ITS_UNIFORM_SHEAR_MODES_ACQUIRE_A_GAP_UNDER_THE_FREE_PARTICLE_RULE_AND_GROW_UNDER_THE_FRAME_BOUNDED_THEOREM_NOTE_2026-09-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_ONE_LIGHT_CONE_EXACTLY_ON_THE_LATTICE_THE_TWO_STEP_CONTENT_MEETS_THE_MEMBERS_IDENTITY_FOR_EVERY_STATE_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/ADMISSIBILITY_RULE_THE_MEMBERS_ZERO_MODE_TESTS_THE_ZERO_OF_ENERGY_IF_THE_MEMBER_SEES_THE_HALF_FILLED_SEA_A_CLOSED_LATTICE_BOUNCES_OR_CANNOT_MOVE_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/ADMISSIBILITY_RULE_EVERY_CLOCK_PROFILE_A_RELABELLING_FORCES_THE_WHOLE_MOMENTUM_CONSTRAINT_AND_NO_POSITIVE_INERTIA_CAN_BE_ADDED_TO_THE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-25.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_if_the_member_sees_the_sea_its_uniform_shear_modes_acquire_a_gap_under_the_free_particle_rule_and_grow_under_the_frame_bounded_theorem_note_2026-09-28"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED135 = (
    "`L = [α tr(ḣ²) + β(tr ḣ)²]/w̄ + Kw̄(uR₁ + R₂) − e_uu + ½ΣΘ_ijh_ij`",
)
LANDED147 = (
    "Counting each reduced-zone pair once gives the sea energy per site",
)
LANDED150 = (
    "**T4: the sea's inertia is such an addition.**",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "frequency_forged": "B",
    "rule_sign_forged": "C",
    "frame_forged": "D",
    "reach3_forged": "E",
    "volume_forged": "F",
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


def e2_diag(L, lam, a, b):
    tot = sp.Integer(0)
    for (s1, c1), (s2, c2), (s3, c3) in itertools.product(labels(L), repeat=3):
        s = [s1, s2, s3]
        c = [c1, c2, c3]
        S2 = sum(x ** 2 for x in s)
        if S2 == 0:
            continue
        S = sp.sqrt(S2)
        t1 = sum(lam[i] ** 2 * s[i] ** 2 * (sp.Rational(1, 2) + a * s[i] ** 2 + b * s[i] ** 4) for i in range(3)) / S
        v2 = sum(lam[i] ** 2 * s[i] ** 2 * c[i] ** 4 for i in range(3))
        sv = sum(lam[i] * s[i] ** 2 * c[i] ** 2 for i in range(3))
        tot += -(t1 + (v2 - sv ** 2 / S2) / (2 * S))
    return sp.nsimplify(sp.radsimp(sp.simplify(tot / L ** 3)))


def e2_metric(L, S):
    p = [sp.sin(2 * x_) for x_ in KS]
    W0 = sum(sp.sin(x_) ** 2 for x_ in KS)
    Sm = sp.Matrix(S)
    P = sp.Matrix(p)
    w1 = sp.expand(-sp.Rational(1, 4) * (P.T * Sm * P)[0])
    w2 = sp.expand(-sp.Rational(1, 8) * (P.T * Sm * Sm * P)[0] - sp.Rational(1, 4) * sum(Sm[a, b] * p[a] * sp.diff(w1, KS[b]) for a in range(3) for b in range(3)))
    f = sp.lambdify(KS, [w1, w2, W0], "sympy")
    tot = sp.Integer(0)
    ks = [sp.Rational(2 * j, L) * sp.pi for j in range(L)]
    for kk in itertools.product(ks, repeat=3):
        a1, a2, a0 = [sp.nsimplify(sp.simplify(v)) for v in f(*kk)]
        if a0 == 0:
            continue
        tot += -(a2 / (2 * sp.sqrt(a0)) - a1 ** 2 / (8 * a0 ** sp.Rational(3, 2)))
    return sp.nsimplify(sp.radsimp(sp.simplify(tot / L ** 3)))


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t135, t147, t150 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note and len(CLAIM_ID) <= 195, f"the note is present and carries its claim id ({len(CLAIM_ID)} characters) and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the member, the sea's reading and the stretch rule are supplied)")
    needles = list(LANDED135)
    if mut("landed_quote_forged"):
        needles[0] = needles[0].replace("½ΣΘ_ijh_ij", "ΣΘ_ijh_ij")
    checks.check("A3", all(n in t135 for n in needles) and all(n in t147 for n in LANDED147) and all(n in t150 for n in LANDED150), "landed block 135: the member's quadratic action L = [alpha tr(hdot^2) + beta (tr hdot)^2]/wbar + K wbar(u R1 + R2) - e u + (1/2) Theta.h; landed block 147: the sea's energy per site; landed block 150 T4: the sea's inertia")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    alpha, wbar, E2, K, trS2, t = sp.symbols("alpha wbar E2 K trS2 t", positive=True)
    eps = sp.Function("eps")(t)
    Lag = alpha / wbar * trS2 * sp.diff(eps, t) ** 2 - E2 * eps ** 2
    el = sp.simplify(sp.diff(sp.diff(Lag, sp.diff(eps, t)), t) - sp.diff(Lag, eps))
    om2 = sp.Symbol("om2")
    trial = el.subs(sp.Derivative(eps, (t, 2)), -om2 * eps)
    sol = sp.solve(sp.Eq(trial, 0), om2)
    want = wbar * E2 / (alpha * trS2)
    if mut("frequency_forged"):
        want = wbar * E2 / (2 * alpha * trS2)
    # R1 = p^2 tr h - p.h.p and R2 (curvature, quadratic in p) vanish at p = 0; tr hdot = 0 for traceless S
    p = sp.symbols("p1:4")
    S = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
    R1 = (sum(x ** 2 for x in p) * S.trace() - (sp.Matrix(p).T * S * sp.Matrix(p))[0])
    ok_r = R1.subs({x: 0 for x in p}) == 0 and S.trace() == 0 and (S * S).trace() == 2
    ok = sol == [want] and ok_r and sp.simplify(want.subs(alpha, K / 4) - 4 * wbar * E2 / (K * trS2)) == 0
    checks.check("B1", ok, "for a uniform traceless strain h = eps S the curvature terms and tr hdot vanish, so L = (alpha/wbar) tr(S^2) epsdot^2 - E2 eps^2 and omega^2 = wbar E2/(alpha tr S^2); at alpha = K/4 (one light cone) omega^2 = 4 wbar E2/(K tr S^2), with tr S^2 = 2 for both shear classes")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    Sd = [[1, 0, 0], [0, -1, 0], [0, 0, 0]]
    So = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
    vals = {(name, L): e2_metric(L, S) for name, S in (("diag", Sd), ("off", So)) for L in (6, 8)}
    if mut("rule_sign_forged"):
        vals[("off", 6)] = -vals[("off", 6)]
    ok = all(v > 0 for v in vals.values())
    checks.check("C1", ok, f"under the free-particle rule (block 187's spectrum along g = exp(eps S)) E2 > 0 for both shear classes on sides 6 and 8 (diagonal {vals[('diag', 6)]}, off-diagonal {vals[('off', 6)]} on side 6): a real gap, omega^2 = 2 wbar E2/K at alpha = K/4")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    s = sp.symbols("s1:4", positive=True)
    lam = sp.symbols("m1:4", real=True)
    t = sp.Symbol("t")
    f = sp.sqrt(sum(s[i] ** 2 * sp.exp(-2 * t * lam[i]) for i in range(3)))
    second = sp.simplify(sp.diff(f, t, 2).subs(t, 0) / 2)
    S = sp.sqrt(sum(x ** 2 for x in s))
    A_ = sum(lam[i] ** 2 * s[i] ** 2 for i in range(3))
    B_ = sum(lam[i] * s[i] ** 2 for i in range(3))
    want = A_ / S - B_ ** 2 / (2 * S ** 3)
    if mut("frame_forged"):
        want = A_ / S - B_ ** 2 / S ** 3
    ok_form = sp.simplify(second - want) == 0
    # (sum lam s^2)^2 <= (sum lam^2 s^2)(sum s^2): the bracket is at least A/(2|S|) > 0, so the sea's second-order energy -<bracket> < 0
    cs = sp.expand(A_ * sum(x ** 2 for x in s) - B_ ** 2)
    ok_cs = sp.expand(cs - sum(s[i] ** 2 * s[j] ** 2 * (lam[i] - lam[j]) ** 2 for i in range(3) for j in range(i + 1, 3))) == 0
    # exact side-6 value for lam = (1, -1, 0)
    tot = sp.Integer(0)
    for (s1, _c1), (s2, _c2), (s3, _c3) in itertools.product(labels(6), repeat=3):
        sv = [s1, s2, s3]
        S2 = sum(x ** 2 for x in sv)
        if S2 == 0:
            continue
        Sq = sp.sqrt(S2)
        lv = (1, -1, 0)
        a_ = sum(lv[i] ** 2 * sv[i] ** 2 for i in range(3))
        b_ = sum(lv[i] * sv[i] ** 2 for i in range(3))
        tot += -(a_ / Sq - b_ ** 2 / (2 * Sq ** 3))
    frame6 = sp.nsimplify(sp.radsimp(sp.simplify(tot / 216)))
    checks.check("D1", ok_form and ok_cs and frame6 < 0, f"under the frame F_a = s_a/l_a the sea's second-order energy is -<sum lam^2 s^2/|s| - (sum lam s^2)^2/(2|s|^3)>, and (sum lam^2 s^2)(sum s^2) - (sum lam s^2)^2 = sum_(i<j) s_i^2 s_j^2 (lam_i - lam_j)^2 >= 0, so it is negative for every nonzero stretch (side 6, lam = (1, -1, 0): {frame6}): omega^2 < 0, the uniform shear modes grow")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    v6 = e2_diag(6, (1, -1, 0), -sp.Rational(1, 2), 0)
    v8 = e2_diag(8, (1, -1, 0), -sp.Rational(1, 2), 0)
    if mut("reach3_forged"):
        v6 = -v6
    checks.check("E1", v6 < 0 and v8 < 0, f"under block 183's reach-three completions with q2 = -1/2, E2 < 0 on sides 6 and 8 ({v6}, {v8}): the modes grow")


# ============================================================================================ family F (T5)
def family_f(checks: Checks) -> None:
    eps = sp.Symbol("eps", real=True)
    ok = True
    for S in (sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]), sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])):
        d = sp.simplify(sp.exp(eps * S).det())
        want = 1
        if mut("volume_forged"):
            want = 1 + eps ** 2
        ok = ok and sp.simplify(d - want) == 0
    checks.check("F1", ok, "det exp(eps S) = exp(eps tr S) = 1 for both traceless shears, so a vacuum energy rho sqrt(det g) has no second-order term along them: a volume-only vacuum gives no gap")


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
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at E2 = 0."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Burgers", "Hopf", "Jacobi", "Ward", "Takahashi", "Wilson", "Kepler", "Bessel", "Liouville", "Paley", "Wiener", "Bloch", "Cauchy", "Schwarz", "Parker", "Friedmann", "Fierz", "Pauli")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_g(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Fierz) —", 1)
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
    "per_element: executed - the uniform traceless mode's equation from the landed action; the frame's second-order formula",
    "per_site: executed - the inequality behind the frame's sign",
    "per_mode: executed - exact E2 on sides 6 and 8 for the rule (both classes) and for q2 = -1/2; the frame on side 6",
    "per_block: executed - det exp(eps S) = 1 for the traceless shears",
    "lattice_wide: checked and not executed - the infinite lattice (floating point in the note); non-uniform modes and the sea's inertia (block 150's kinetic side); the massive sea's gap",
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
    print(f"scope: if the member sees the sea, its uniform traceless modes have omega^2 = wbar E2/(alpha tr S^2); E2 > 0 under the free-particle rule (a gap), E2 < 0 under the frame and the reach-three completions (growth), 0 for a volume-only vacuum; the supervisor's own derivation, unrefereed; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
