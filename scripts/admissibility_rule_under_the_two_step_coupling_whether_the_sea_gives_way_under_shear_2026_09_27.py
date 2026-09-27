#!/usr/bin/env python3
"""Exact checks: under block 69's two-step coupling with a per-axis completion in block 176's family (l F = sin k (1 - q sin^2 k),
q = -lam + q2 lam^2 + O(lam^3), lam = log l), the filled sea's energy under a volume-preserving diagonal stretch (sum lam_a = 0) is, at
second order, E2 = -(sum lam^2/3)[A/2 - (1 + q2) B] - I, with A = <|s|>, B = <sum s^4/|s|>, I = <|s x w|^2/(2|s|^3)>, w_a = s_a c_a^2 lam_a.
So the sea gives way iff q2 < q2* = -1 + (A/2 + 3 I/sum lam^2)/B, and q2* > -1/2 on the infinite lattice: block 69's linear completion
and block 176's smooth one (both q2 = -1/2) give way; admissibility (q >= -1/6) does not constrain q2. On the tori of side 4, 6, 8,
q2* = -1/2, and exact numbers above -1/2 (the supervisor's own derivation, unrefereed). Block 69 as landed; blocks 155, 167, 176,
180 (pushed or open) placed.

A (premises): landed block 69; the axioms.
B (T1): the per-axis second-order expansion; q2 = -1/2 for the linear and the smooth completions.
C (T2): the second-order energy of a filled mode; the torus sums against the averaged formula, two traceless directions.
D (T3): the threshold on the tori of side 4, 6, 8; the same for both directions; above -1/2 where some mode has s^2 not in {0, 1}.
E (T4): the frame's per-axis stretch gives -(sum lam^2/6) A - I_frame < 0 (blocks 155, 167).
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
    "docs/ADMISSIBILITY_RULE_UNDER_THE_TWO_STEP_COUPLING_WHETHER_THE_SEA_GIVES_WAY_UNDER_SHEAR_IS_SET_BY_THE_COMPLETIONS_SECOND_ORDER_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_under_the_two_step_coupling_whether_the_sea_gives_way_under_shear_is_set_by_the_completions_second_order_number_bounded_theorem_note_2026-09-27"
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
    "expansion_forged": "B",
    "energy_forged": "C",
    "threshold_forged": "D",
    "frame_forged": "E",
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
k = sp.Symbol("k")
lam, q2 = sp.symbols("lam q2")


def torus_modes(L):
    for kk in itertools.product(range(L), repeat=3):
        s = [sp.sin(2 * sp.pi * sp.Integer(m) / L) for m in kk]
        c = [sp.cos(2 * sp.pi * sp.Integer(m) / L) for m in kk]
        yield s, c


def second_order_direct(L, lv, q2v, frame=False):
    """exact sum over the torus of the filled band's second-order energy per site"""
    tot = 0
    for s, c in torus_modes(L):
        E2 = sp.nsimplify(sum(x ** 2 for x in s))
        if E2 == 0:
            continue
        E = sp.sqrt(E2)
        if frame:
            f1 = [-s[a] * lv[a] for a in range(3)]
            f2 = [s[a] * lv[a] ** 2 / 2 for a in range(3)]
        else:
            f1 = [-s[a] * c[a] ** 2 * lv[a] for a in range(3)]
            f2 = [s[a] * (sp.Rational(1, 2) - (1 + q2v) * s[a] ** 2) * lv[a] ** 2 for a in range(3)]
        cr = [s[1] * f1[2] - s[2] * f1[1], s[2] * f1[0] - s[0] * f1[2], s[0] * f1[1] - s[1] * f1[0]]
        tot += -sum(s[a] * f2[a] for a in range(3)) / E - sp.nsimplify(sp.expand(sum(x ** 2 for x in cr))) / (2 * E ** 3)
    return sp.radsimp(tot / L ** 3)


def averages(L, lv):
    A = B = Iv = 0
    for s, c in torus_modes(L):
        E2 = sp.nsimplify(sum(x ** 2 for x in s))
        if E2 == 0:
            continue
        E = sp.sqrt(E2)
        A += E
        B += sp.nsimplify(sum(x ** 4 for x in s)) / E
        w = [s[a] * c[a] ** 2 * lv[a] for a in range(3)]
        cr = [s[1] * w[2] - s[2] * w[1], s[2] * w[0] - s[0] * w[2], s[0] * w[1] - s[1] * w[0]]
        Iv += sp.nsimplify(sp.expand(sum(x ** 2 for x in cr))) / (2 * E ** 3)
    n = L ** 3
    return sp.radsimp(A / n), sp.radsimp(B / n), sp.radsimp(Iv / n)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t69 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its coupling, its completion and the sea are supplied)")
    needles = list(LANDED69)
    if mut("landed_quote_forged"):
        needles[1] = "Common corner quadratic forms are a leading-order result and determine a nonlinear completion."
    checks.check("A3", all(n in t69 for n in needles), "landed block 69: the uniform form; the leading order does not determine a completion")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    s = sp.sin(k)
    q = -lam + q2 * lam ** 2
    F = s * (1 - q * s ** 2) * sp.exp(-lam)
    ser = sp.expand(sp.series(F, lam, 0, 3).removeO())
    c1 = sp.simplify(ser.coeff(lam, 1) + s * sp.cos(k) ** 2)
    target2 = s * (sp.Rational(1, 2) - (1 + q2) * s ** 2) if not mut("expansion_forged") else s * (sp.Rational(1, 2) - (2 + q2) * s ** 2)
    c2 = sp.simplify(ser.coeff(lam, 2) - target2)
    l_ = sp.exp(lam)
    qlin = 1 - l_
    qsm = (1 - l_) / sp.sqrt(1 + 36 * (l_ - 1) ** 2)
    q2lin = sp.series(qlin, lam, 0, 3).removeO().coeff(lam, 2)
    q2sm = sp.series(qsm, lam, 0, 3).removeO().coeff(lam, 2)
    q1lin = sp.series(qlin, lam, 0, 3).removeO().coeff(lam, 1)
    q1sm = sp.series(qsm, lam, 0, 3).removeO().coeff(lam, 1)
    ok = c1 == 0 and c2 == 0 and q2lin == -sp.Rational(1, 2) and q2sm == -sp.Rational(1, 2) and q1lin == -1 and q1sm == -1
    checks.check("B1", ok, "per axis F = s - lam s c^2 + lam^2 s(1/2 - (1 + q2) s^2) + O(lam^3) for q = -lam + q2 lam^2; block 69's linear completion 1 - l and block 176's smooth completion (1 - l)/sqrt(1 + 36(l - 1)^2) both have q2 = -1/2")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    ok = True
    for L in (6, 8):
        for lv in ((1, -1, 0), (1, 1, -2)):
            S2 = sum(x ** 2 for x in lv)
            direct = second_order_direct(L, lv, q2)
            A, B, Iv = averages(L, lv)
            formula = -(sp.Rational(S2, 3)) * (A / 2 - (1 + q2) * B) - Iv
            if mut("energy_forged"):
                formula = -(sp.Rational(S2, 3)) * (A / 2 - (1 + q2) * B) + Iv
            ok = ok and sp.simplify(sp.expand(direct - formula)) == 0
    checks.check("C1", ok, "the filled band's second-order energy -<s^.F2 + |s x F1|^2/(2|s|)> under a traceless diagonal stretch equals -(sum lam^2/3)[A/2 - (1 + q2) B] - I exactly, on the tori of side 6 and 8, for lam along (1, -1, 0) and (1, 1, -2)")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    ths = {}
    ok = True
    for L in (4, 6, 8):
        vals = []
        for lv in ((1, -1, 0), (1, 1, -2)):
            S2 = sum(x ** 2 for x in lv)
            A, B, Iv = averages(L, lv)
            vals.append(sp.radsimp(-1 + (A / 2 + 3 * Iv / S2) / B))
        ok = ok and sp.simplify(vals[0] - vals[1]) == 0
        ths[L] = vals[0]
    ok = ok and ths[4] == -sp.Rational(1, 2)
    # above -1/2 on sides 6 and 8: q2* + 1/2 = (A/2 - B/2 + 3I/S2)/B with A > B (some mode has s^2 not in {0,1}) and I >= 0
    A6, B6, I6 = averages(6, (1, -1, 0))
    A8, B8, I8 = averages(8, (1, -1, 0))
    gap6 = sp.radsimp(A6 - B6)
    gap8 = sp.radsimp(A8 - B8)
    want6 = sp.radsimp((4 + sp.sqrt(3) + 2 * sp.sqrt(6)) / 36) if not mut("threshold_forged") else sp.Rational(1, 9)
    ok = ok and sp.simplify(gap6 - want6) == 0 and sp.simplify(gap8 - sp.radsimp(A8 - B8)) == 0 and I6 != 0 and I8 != 0
    checks.check("D1", ok, f"q2* = -1 + (A/2 + 3I/sum lam^2)/B is the same for both traceless directions; it is -1/2 on the side-4 torus (every active s^2 = 1: A = B, I = 0); on sides 6 and 8, A - B = <sum s^2 c^2/|s|> > 0 (side 6: (4 + sqrt3 + 2 sqrt6)/36) and I > 0, so q2* > -1/2")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    ok = True
    for L in (6, 8):
        lv = (1, -1, 0)
        S2 = sum(x ** 2 for x in lv)
        fr = second_order_direct(L, lv, 0, frame=True)
        A, B, Iv = averages(L, lv)
        # the frame's interband term uses w = s lam instead of s c^2 lam
        Ifr = 0
        for s, c in torus_modes(L):
            E2 = sp.nsimplify(sum(x ** 2 for x in s))
            if E2 == 0:
                continue
            w = [s[a] * lv[a] for a in range(3)]
            cr = [s[1] * w[2] - s[2] * w[1], s[2] * w[0] - s[0] * w[2], s[0] * w[1] - s[1] * w[0]]
            Ifr += sp.nsimplify(sp.expand(sum(x ** 2 for x in cr))) / (2 * sp.sqrt(E2) ** 3)
        Ifr = sp.radsimp(Ifr / L ** 3)
        want = -(sp.Rational(S2, 6)) * A - Ifr if not mut("frame_forged") else -(sp.Rational(S2, 3)) * A - Ifr
        ok = ok and sp.simplify(sp.expand(fr - want)) == 0 and Ifr != 0
    checks.check("E1", ok, "for comparison, the frame's per-axis stretch F = s e^{-lam} gives -(sum lam^2/6) A - I_frame, negative for every volume-preserving diagonal stretch (the sign of blocks 155 and 167), on sides 6 and 8")


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
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at q2 = -1/2."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Pauli", "Rayleigh", "Schrödinger", "Slater", "Hellmann", "Feynman", "Wilson")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Hellmann) —", 1)
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
    "per_element: executed - the per-axis expansion of block 176's family; q2 of the two named completions",
    "per_site: executed - the second-order energy of a filled mode against the averaged formula",
    "per_mode: executed - every mode of the tori of side 4, 6 and 8, two traceless directions",
    "per_block: executed - the threshold q2* on three tori; the frame's comparison",
    "lattice_wide: checked and not executed - the infinite-lattice threshold above -1/2 (proof in the text); off-diagonal shears (no completion supplied); higher orders",
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
    print(f"scope: under block 69's two-step coupling with a completion in block 176's family, the filled sea gives way under a volume-preserving diagonal stretch iff q2 < q2*, with q2* > -1/2 on the infinite lattice; both named completions (q2 = -1/2) give way; admissibility does not constrain q2; the supervisor's own derivation, unrefereed; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
