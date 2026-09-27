#!/usr/bin/env python3
"""Exact checks: at every wave number, a ray crossing the one-body gradient bends A[1 + rho(R - 1)] times a slow body's fall;
with block 60's crossing (the frame) A = sum n_a^2 cos 2k_a <= 1, so short off-axis waves bend less and none outruns w/l;
with block 69's reach-three coupling completed as 1 + b = 1/l, stretched regions (l > 7/6) carry waves faster than w/l and
off-axis rays bend more than three times the fall near a strong body (a harvest of probe #9018, confirmed by an other-family
referee in #9341). Blocks 59 T4, 60 T4 and 69 T4 as landed.

A (premises): landed block 59 T4's ratio, block 60 T4's one-body field, block 69 T4's uniform-strain symbol; the axioms.
B (T1): the reach-three symbol with isotropic B = b, 1 + b = 1/l, is sin k (cos^2 k + l sin^2 k)/l; the frame's is sin k/l;
   along the gradient n (with the ray crossing it) d^2(n.x)/dt^2 = -(n^T Hess_k E n) dE/ds for any E(s, k).
C (T2): the one-body ratio R = 1 - dlog l/dlog w = 1 + 2w/(w + w0) from block 60 T4's field.
D (T3, the frame): A = cos 2k per axis, rho = 1; the diagonal at tan(kappa/2) = 3/10 has A = 4681/11881 < 1/2; |d sin k/dk| <= 1.
E (T4, reach three): rho_a = cos^2/(cos^2 + l sin^2); A = 1 + (12 l - 14) k^2 + O(k^4); the axis group speed l s' = cos k (1 + 3(l - 1)
   sin^2 k) exceeds 1 near k = 0 iff l > 7/6, with maximum (19/6) sqrt(19/45) at l = 9/4; at R = 3 the diagonal ratio is
   3 + (34 l - 42) kappa^2 + O(kappa^4); the witness at Qg = 1/2, tan(kappa/2) = 1/10 is the stated rational function of G = Qg0.
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
    "docs/ADMISSIBILITY_RULE_AT_EVERY_WAVE_NUMBER_THE_FRAMES_RAYS_BEND_NO_MORE_THAN_LONG_WAVES_BUT_THE_REACH_THREE_COUPLING_LETS_STRETCHED_REGIONS_CARRY_FASTER_WAVES_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_at_every_wave_number_the_frames_rays_bend_no_more_than_long_waves_but_the_reach_three_coupling_lets_stretched_regions_carry_faster_waves_bounded_theorem_note_2026-09-27"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED59 = ("For parallel gradients, nonzero denominator, and the same local c, the ratio of the stated transverse components is `d log c/d log a`.",)
LANDED60 = ("One body: `P = Q/(1 + 2Qg_0)`, `w_0 = 1/(1 + 2Qg_0)`.",)
LANDED69 = ("For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`", "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion.")

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "symbol_forged": "B",
    "ratio_forged": "C",
    "frame_value_forged": "D",
    "threshold_forged": "E",
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
k, l, w, w0, G = sp.symbols("k l w w0 G", positive=True)


def s_frame(kk, ll):
    return sp.sin(kk) / ll


def s_reach3(kk, ll):
    return sp.sin(kk) * (sp.cos(kk) ** 2 + ll * sp.sin(kk) ** 2) / ll


def A_axis(sfun, kk, ll):
    """l^2 (s'^2 + s s'') for one axis"""
    s = sfun(k, l)
    expr = l ** 2 * (sp.diff(s, k) ** 2 + s * sp.diff(s, k, 2))
    return expr.subs({k: kk, l: ll})


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t59, t60, t69 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its couplings, the member and the ray model are supplied)")
    n60 = list(LANDED60)
    if mut("landed_quote_forged"):
        n60[0] = "One body: `P = Q/(1 + Qg_0)`, `w_0 = 1/(1 + Qg_0)`."
    ok = all(n in t59 for n in LANDED59) and all(n in t60 for n in n60) and all(n in t69 for n in LANDED69)
    checks.check("A3", ok, "landed block 59 T4: the local ratio d log c/d log a; block 60 T4: one body P = Q/(1 + 2Qg0), w0 = 1/(1 + 2Qg0); block 69 T4: the uniform-strain symbol s_a + c_a sum_j B s_j c_j, and its note that the leading order does not determine a nonlinear completion")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    b = sp.Symbol("b")
    sym69 = sp.sin(k) + sp.cos(k) * b * sp.sin(k) * sp.cos(k)      # isotropic B = b 1: s_a + c_a b s_a c_a
    target = s_reach3(k, l)
    if mut("symbol_forged"):
        target = sp.sin(k) * (sp.cos(k) ** 2 + l * sp.sin(k) ** 2)
    ok1 = sp.simplify(sym69.subs(b, 1 / l - 1) - target) == 0
    # the ray law: for E(s, k1, k2, k3) with fields varying only along n (s = n.x) and n.ydot = 0,
    # d^2(n.x)/dt^2 = -(n^T Hess_k E n) dE/ds
    s_, k1, k2, k3, n1, n2, n3 = sp.symbols("s k1 k2 k3 n1 n2 n3", real=True)
    x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
    Ef = sp.Function("E")
    E = Ef(n1 * x1 + n2 * x2 + n3 * x3, k1, k2, k3)
    X = (x1, x2, x3)
    K = (k1, k2, k3)
    nv = (n1, n2, n3)
    xdot = [sp.diff(E, kk) for kk in K]
    kdot = [-sp.diff(E, xx) for xx in X]
    npos_dot = sum(nv[i] * xdot[i] for i in range(3))
    acc = sum(sp.diff(npos_dot, X[i]) * xdot[i] + sp.diff(npos_dot, K[i]) * kdot[i] for i in range(3))
    hess = sum(nv[i] * nv[j] * sp.diff(E, K[i], K[j]) for i in range(3) for j in range(3))
    dEds = sum(nv[i] * sp.diff(E, X[i]) for i in range(3)) / (n1 ** 2 + n2 ** 2 + n3 ** 2)
    first = sum(sp.diff(npos_dot, X[i]) * xdot[i] for i in range(3))
    # the first term is (d/ds of n.grad_k E) times (n . xdot) times |n|^2, which vanishes when the ray crosses the gradient
    ok2 = sp.simplify(first - sp.diff(npos_dot, X[0]) / n1 * npos_dot) == 0
    ok2 = ok2 and sp.simplify(acc - first + hess * dEds) == 0
    checks.check("B1", ok1 and ok2, "block 69 T4 with isotropic B = b and 1 + b = 1/l gives sigma_a/l = sin k (cos^2 k + l sin^2 k)/l; for any E(n.x, k), d^2(n.x)/dt^2 = (d/ds n.grad_k E)(n.xdot) - (n^T Hess_k E n) dE/ds, so a ray crossing the gradient accelerates along it by -(n^T Hess E n) dE/ds")
    # the slow body at k = 0 falls at -(w/l)^2 dlog w for both couplings: F Hess F -> 1/(m l^2) at k = 0
    m = sp.Symbol("m", positive=True)
    ok3 = True
    for sfun in (s_frame, s_reach3):
        F = sp.sqrt(m ** 2 + sfun(k, l) ** 2)
        ok3 = ok3 and sp.simplify(sp.diff(F, k, 2).subs(k, 0) - 1 / (m * l ** 2)) == 0 and sp.simplify(sp.diff(F, l).subs(k, 0)) == 0
    checks.check("B2", ok3, "for E = w sqrt(m^2 + |s|^2) with either coupling, at k = 0 the curvature is 1/(m l^2) and the length does not enter, so a slow body at rest falls at -(w/l)^2 dlog w (block 59 T4's fall)")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    Q, g, P = sp.symbols("Q g P", positive=True)
    chi = 1 + Q * g
    N = 1 - P * g
    ww = N / chi
    ll = chi ** 2
    Rexpr = 1 - sp.diff(sp.log(ll), g) / sp.diff(sp.log(ww), g)
    w0v = P / Q
    claim = 1 + 2 * ww / (ww + w0v)
    if mut("ratio_forged"):
        claim = 1 + ww / (ww + w0v)
    ok = sp.simplify(Rexpr - claim) == 0
    far = sp.limit(claim.subs(P, Q * w0), g, 0)
    ok = ok and sp.simplify(far - (3 + w0) / (1 + w0)) == 0
    checks.check("C1", ok, "block 60 T4's one-body field chi = 1 + Qg, N = 1 - Pg, P = Q w0: the long-wave ratio R = 1 - dlog l/dlog w = 1 + 2w/(w + w0), tending to (3 + w0)/(1 + w0) far from the body, inside (1, 3) for w0 > 0")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    Af = sp.simplify(A_axis(s_frame, k, l))
    rho_f = sp.simplify(-l * sp.diff(sp.log(s_frame(k, l)), l))
    ok = sp.simplify(Af - sp.cos(2 * k)) == 0 and rho_f == 1
    t = sp.Rational(3, 10)
    ck = (1 - t ** 2) / (1 + t ** 2)
    A_diag = 2 * ck ** 2 - 1
    want = sp.Rational(4681, 11881) if not mut("frame_value_forged") else sp.Rational(4681, 11880)
    ok = ok and A_diag == want and A_diag < sp.Rational(1, 2)
    ok = ok and sp.simplify(l * sp.diff(s_frame(k, l), k) - sp.cos(k)) == 0
    checks.check("D1", ok, "the frame: A = l^2 (s'^2 + s s'') = cos 2k per axis and rho = 1, so the ratio is A R <= R; a diagonal carrier with tan(kappa/2) = 3/10 has A = 4681/11881 < 1/2, so its ratio is below 1 wherever R < 11881/4681; the group speed is w cos k/l <= w/l")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    A3 = A_axis(s_reach3, k, l)
    ser = sp.series(A3, k, 0, 5).removeO()
    ok1 = sp.simplify(ser.coeff(k, 0) - 1) == 0 and sp.simplify(ser.coeff(k, 2) - (12 * l - 14)) == 0
    rho3 = sp.simplify(-l * sp.diff(sp.log(s_reach3(k, l)), l))
    ok1 = ok1 and sp.simplify(rho3 - sp.cos(k) ** 2 / (sp.cos(k) ** 2 + l * sp.sin(k) ** 2)) == 0
    gs = sp.simplify(l * sp.diff(s_reach3(k, l), k))
    ok2 = sp.simplify(gs - sp.cos(k) * (1 + 3 * (l - 1) * sp.sin(k) ** 2)) == 0
    gser = sp.series(gs, k, 0, 3).removeO()
    thr = sp.Rational(7, 6) if not mut("threshold_forged") else sp.Rational(5, 4)
    ok2 = ok2 and sp.solve(sp.Eq(gser.coeff(k, 2), 0), l) == [thr]
    c2 = sp.Symbol("c2", positive=True)                     # cos^2 k
    speed2 = c2 * (1 + 3 * (sp.Rational(9, 4) - 1) * (1 - c2)) ** 2
    crit = sp.solve(sp.diff(speed2, c2), c2)
    ok2 = ok2 and sp.Rational(19, 45) in crit and sp.simplify(sp.sqrt(speed2.subs(c2, sp.Rational(19, 45))) - sp.Rational(19, 6) * sp.sqrt(sp.Rational(19, 45))) == 0
    # at R = 3 the diagonal ratio A[1 + 2 rho] = 3 + (34 l - 42) kappa^2 + O(kappa^4)
    kap = sp.Symbol("kappa", positive=True)
    ratio3 = A_axis(s_reach3, kap, l) * (1 + 2 * rho3.subs(k, kap))
    rser = sp.series(ratio3, kap, 0, 3).removeO()
    ok3 = sp.simplify(rser.coeff(kap, 0) - 3) == 0 and sp.simplify(rser.coeff(kap, 2) - (34 * l - 42)) == 0
    ok3 = ok3 and sp.solve(sp.Eq(34 * l - 42, 0), l) == [sp.Rational(21, 17)]
    # the witness: Qg = 1/2 (chi = 3/2, l = 9/4), w0 = 1/(1 + 2G), R = 3/(1 + w0), carrier (kappa, kappa, 0), tan(kappa/2) = 1/10
    tt = sp.Rational(1, 10)
    sk, ck = 2 * tt / (1 + tt ** 2), (1 - tt ** 2) / (1 + tt ** 2)
    lv = sp.Rational(9, 4)
    sv = sk * (ck ** 2 + lv * sk ** 2) / lv
    s1 = sp.diff(s_reach3(k, l), k)
    s2 = sp.diff(s_reach3(k, l), k, 2)
    s1v = s1.subs(l, lv).rewrite(sp.tan).subs(k, 2 * sp.atan(tt))
    s2v = s2.subs(l, lv).rewrite(sp.tan).subs(k, 2 * sp.atan(tt))
    Aw = sp.nsimplify(sp.simplify(lv ** 2 * (s1v ** 2 + sv * s2v)))
    rw = ck ** 2 / (ck ** 2 + lv * sk ** 2)
    w0v = 1 / (1 + 2 * G)
    Rw = 3 / (1 + w0v)
    ratio_w = sp.simplify(Aw * (1 + rw * (Rw - 1)))
    claim = sp.Rational(1606444785801) * (6734 * G + 3467) / (sp.Integer(2524294918129178) * (G + 1))
    ok4 = Aw == sp.Rational(1606444785801, 1061520150601) and rw == sp.Rational(1089, 1189) and sp.simplify(ratio_w - claim) == 0
    lim = sp.limit(claim, G, sp.oo)
    ok4 = ok4 and lim > 4 and claim.subs(G, 1000) > 4 and sp.diff(claim, G).subs(G, 0) > 0
    checks.check("E1", ok1 and ok2, "reach three with 1 + b = 1/l: rho_a = cos^2 k/(cos^2 k + l sin^2 k), A_a = 1 + (12 l - 14) k^2 + O(k^4); the axis group speed l s' = cos k (1 + 3(l - 1) sin^2 k) exceeds w/l near k = 0 iff l > 7/6, and at l = 9/4 reaches (19/6) sqrt(19/45) times w/l at cos^2 k = 19/45")
    checks.check("E2", ok3 and ok4, "at R = 3 the diagonal ratio is 3 + (34 l - 42) kappa^2 + O(kappa^4), above 3 iff l > 21/17; the witness at Qg = 1/2 (l = 9/4), carrier (kappa, kappa, 0) with tan(kappa/2) = 1/10: A = 1606444785801/1061520150601, rho = 1089/1189, ratio 1606444785801(6734 G + 3467)/(2524294918129178 (G + 1)), rising in G = Qg0 and above 4 for strong bodies")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 59, 60 and 69 as landed on main (the local ray comparison, the curvature member's one-body field, and the reach-three coupling at uniform strain) and asks how rays of every wave number bend against a slow body's fall; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at l = 7/6."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Berry", "Schwarzschild",
                   "Fermat", "Snell")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Fermat) —", 1)
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
    "per_element: executed - the two symbols; the acceleration identity for any E(n.x, k)",
    "per_site: executed - the one-body ratio from block 60's exact field",
    "per_mode: executed - A and rho for both couplings; the frame's diagonal value; reach three's series, thresholds and axis speed",
    "per_block: executed - the witness as an exact rational function of G",
    "lattice_wide: checked and not executed - sub-principal terms; carriers off the symmetric directions; exact trajectories through the strong region",
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
    print(f"scope: blocks 59, 60 and 69 as landed: at every wave number bending over fall is A[1 + rho(R - 1)]; the frame keeps A <= 1 and no wave above w/l; reach three completed as 1 + b = 1/l carries faster waves where l > 7/6 and bends off-axis rays more than 3 times the fall where l > 21/17 near a strong body; harvest of #9018 (confirmed by #9341); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
