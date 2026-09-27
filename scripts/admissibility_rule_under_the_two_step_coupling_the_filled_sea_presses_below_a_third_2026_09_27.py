#!/usr/bin/env python3
"""Exact checks: under block 69's two-step coupling (the coupling blocks 120 and 136 use to source the member), a uniform stretch
H(k) = sum_a sigma_a s_a (1 + b c_a^2), 1 + b = 1/l at first order (block 69 T4), lowers a walker's energy at the rate
d log E/d log l = -(1 - sum_a s_a^4/E^2): less than the rescaled walk H/l of blocks 146 and 147 at every wave number with E > 0, equal
only in the long-wave limit. So a walker's dilation pressure is p = (1 - sum s^4/E^2) rho/3, zero where every active axis has s^2 = 1,
and the filled sea's is strictly between 0 and rho/3 (exactly 0 on the side-4 torus, 1/12 on side 6, an exact algebraic number on
side 8). And [H(b1), H(b2)] = 2i(b2 - b1)(s x w).sigma with w_a = s_a c_a^2: a stretch turns a walker's coin at fixed wave number
unless its active axes share one cos^2, so a stretch history can excite the filled sea, which the rescaled walk never does. The
supervisor's own derivation, unrefereed. Blocks 69, 120, 136, 146, 147 as landed.

A (premises): landed blocks 69, 120, 136, 146, 147; the axioms.
B (T1): the isotropic uniform form; its first-order energy change; sum s^2 c^2 = E^2 - sum s^4; the rescaled walk's rate.
C (T2): the pressure per mode and of the filled sea on the tori of side 4, 6, 8; the rescaled walk's rho/3.
D (T3): the commutator of two stretches and the interband element |s^ x w|^2; tori: none on sides 4 and 6, some on side 8.
E (T4): long-wave limits at every species point.
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
    "docs/ADMISSIBILITY_RULE_UNDER_THE_TWO_STEP_COUPLING_THE_FILLED_SEA_PRESSES_BELOW_A_THIRD_OF_ITS_ENERGY_AND_A_UNIFORM_STRETCH_CAN_EXCITE_IT_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/ADMISSIBILITY_RULE_ONLY_THE_TWO_STEP_CURRENT_CAN_SOURCE_BLOCK_62S_SYMMETRIC_MEMBER_NO_LOCAL_PLACEMENT_OF_THE_FRAME_RESPONSE_OR_OF_THE_ONE_STEP_CURRENT_KEEPS_ITS_DIVERGENCE_CONDITION_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/ADMISSIBILITY_RULE_TWO_STEP_CONTENT_KEEPS_SYMMETRIC_BOOKS_WHERE_THE_MEMBER_KEEPS_ITS_FIELDS_AND_A_BOND_SHIFT_KEEPS_EVERY_CONSTRAINT_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/ADMISSIBILITY_RULE_THE_LATTICE_EXPANDS_WITH_THE_STATIC_PULLS_COUPLING_IFF_ALPHA_EQUALS_K_OVER_FOUR_AND_TOP_SPEED_WALKERS_LOSE_ENERGY_AS_ONE_OVER_THE_LENGTH_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/ADMISSIBILITY_RULE_THE_MEMBERS_ZERO_MODE_TESTS_THE_ZERO_OF_ENERGY_IF_THE_MEMBER_SEES_THE_HALF_FILLED_SEA_A_CLOSED_LATTICE_BOUNCES_OR_CANNOT_MOVE_BOUNDED_THEOREM_NOTE_2026-09-25.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_under_the_two_step_coupling_the_filled_sea_presses_below_a_third_of_its_energy_and_a_uniform_stretch_can_excite_it_bounded_theorem_note_2026-09-27"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED69 = (
    "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]` and `H² = Σ_a[s_a + c_a Σ_j B_a^j s_jc_j]²`. Near `k = πn + q`: `H² = qᵀ(1 + B)ᵀ(1 + B)q + O(q⁴)` for every `n`.",
)
LANDED120 = ("The two-step current has a transposed identity for finite equal-energy wave sums and finite periodic eigenspaces;",)
LANDED136 = ("  - Their mean `P^B = (P″ + Q)/2` is conserved with the symmetric stress, and the energy flows as `P^B` too.",)
LANDED146 = (
    "Define scalar dilation pressure by `m'=-3p ell³`.",
    "Under the supplied uniform hopping rule the massless symbol is `H(k)/ell(t)`",
    "For positive massless-band energy per site `m=epsilon/ell`, scalar dilation pressure is rho/3.",
)
LANDED147 = (
    "For the massless symbol H(ell)=H(1)/ell, Hamiltonians commute at all positive lengths; an initially filled negative band keeps its occupations under any uniform length history.",
    "With the supplied dilation pressure `p=-dm/dlambda/(3ell³)`, the massless sea has `p=rho/3`.",
)
SIDE8 = "(sqrt(10) + 20 + 15*sqrt(2) + 10*sqrt(6))/(10*(sqrt(3) + 3*sqrt(10) + 15 + 10*sqrt(6) + 18*sqrt(2)))"

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "rate_forged": "B",
    "torus_forged": "C",
    "commutator_forged": "D",
    "limit_forged": "E",
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
I = sp.I
R = sp.Rational
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
S = sp.symbols("s1:4", real=True)
C = sp.symbols("c1:4", real=True)
b, b1, b2 = sp.symbols("b b1 b2", real=True)


def sdot(v):
    return sum((v[a] * SIG[a] for a in range(3)), sp.zeros(2))


def torus_modes(L):
    out = []
    for kk in itertools.product(range(L), repeat=3):
        s = [sp.nsimplify(sp.sin(2 * sp.pi * n / L)) for n in kk]
        c = [sp.nsimplify(sp.cos(2 * sp.pi * n / L)) for n in kk]
        out.append((kk, s, c))
    return out


def sea_ratio(L, rate):
    num = 0
    den = 0
    for kk, s, c in torus_modes(L):
        E2 = sp.nsimplify(sum(x ** 2 for x in s))
        if E2 == 0:
            continue
        E = sp.sqrt(E2)
        num += E * rate(s, c, E2)
        den += E
    return sp.simplify(num / (3 * den))


def rate_two_step(s, c, E2):
    return sp.nsimplify(1 - sum(x ** 4 for x in s) / E2)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t69, t120, t136, t146, t147 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its couplings and the stretch rules are supplied)")
    checks.check("A3", all(n in t69 for n in LANDED69) and all(n in t120 for n in LANDED120) and all(n in t136 for n in LANDED136), "landed blocks 69 (the two-step coupling's uniform form), 120 and 136 (the two-step current sources the symmetric member)")
    needles = list(LANDED146)
    if mut("landed_quote_forged"):
        needles[2] = "For positive massless-band energy per site `m=epsilon/ell`, scalar dilation pressure is rho/2."
    checks.check("A4", all(n in t146 for n in needles) and all(n in t147 for n in LANDED147), "landed blocks 146 and 147: the supplied rescaled walk H(k)/l, the dilation pressure m' = -3 p l^3, massless pressure rho/3, commuting stretches and an inert sea")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    Bm = b * sp.eye(3)
    H = sp.zeros(2)
    for a in range(3):
        H += SIG[a] * (S[a] + C[a] * sum(Bm[a, j] * S[j] * C[j] for j in range(3)))
    want = sdot([S[a] * (1 + b * C[a] ** 2) for a in range(3)])
    checks.check("B1", sp.simplify(H - want) == sp.zeros(2), "block 69 T4's uniform form at isotropic strain B = b 1 is H(k) = sum_a sigma_a s_a (1 + b c_a^2); its long-wave speed is 1 + b = 1/l")
    E2b = sum((S[a] * (1 + b * C[a] ** 2)) ** 2 for a in range(3))
    E0 = sp.sqrt(sum(x ** 2 for x in S))
    dE = sp.simplify(sp.diff(sp.sqrt(E2b), b).subs(b, 0))
    want = sum(S[a] ** 2 * C[a] ** 2 for a in range(3)) / E0
    if mut("rate_forged"):
        want = sum(S[a] ** 2 * C[a] for a in range(3)) / E0
    ok = sp.simplify(dE - want) == 0
    on_circle = {C[a] ** 2: 1 - S[a] ** 2 for a in range(3)}
    ident = sp.expand(sum(S[a] ** 2 * C[a] ** 2 for a in range(3)).subs(on_circle) - (sum(x ** 2 for x in S) - sum(x ** 4 for x in S))) == 0
    dEres = sp.simplify(sp.diff(sp.sqrt(sum((S[a] * (1 + b)) ** 2 for a in range(3))), b).subs(b, 0))
    checks.check("B2", ok and ident and sp.simplify(dEres - E0) == 0, "dE/db at b = 0 is sum_a s_a^2 c_a^2/E = (E^2 - sum_a s_a^4)/E, against E for the rescaled walk: d log E/d log l = -(1 - sum s^4/E^2) instead of -1")
    # with x_a = s_a^2 in [0, 1]: E^2 - sum s^4 = sum x_a (1 - x_a) >= 0, so r = 1 - sum s^4/E^2 = sum x(1 - x)/sum x lies in [0, 1)
    x = sp.symbols("x1:4", nonnegative=True)
    ident2 = sp.expand(sum(x) - sum(t ** 2 for t in x) - sum(t * (1 - t) for t in x)) == 0
    # kinetic reading: r = |v|^2 with v_a = s_a c_a/E, and m_eff^2 := E^2 (1 - |v|^2) = sum s^4
    E2s = sum(t ** 2 for t in S)
    v2 = sum((S[a] * C[a]) ** 2 for a in range(3)) / E2s
    r = 1 - sum(t ** 4 for t in S) / E2s
    kin = sp.simplify(sp.expand((v2 - r).subs(on_circle))) == 0 and sp.simplify(sp.expand((E2s * (1 - v2)).subs(on_circle) - sum(t ** 4 for t in S))) == 0
    checks.check("B4", kin, "r = |v|^2 with v_a = s_a c_a/E the group velocity, so p = rho |v|^2/3 is kinetic pressure; E^2 (1 - |v|^2) = sum s_a^4 =: m_eff^2, zero only at the species points")
    checks.check("B3", ident2, "with x_a = s_a^2 in [0, 1]: E^2 - sum s^4 = sum_a x_a(1 - x_a) >= 0 and sum s^4 > 0 where E > 0, so r = 1 - sum s^4/E^2 lies in [0, 1), zero iff every active axis has s^2 = 1")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    r4 = sea_ratio(4, rate_two_step)
    r6 = sea_ratio(6, rate_two_step)
    r8 = sea_ratio(8, rate_two_step)
    want8 = sp.sympify(SIDE8)
    want6 = R(1, 12) if not mut("torus_forged") else R(1, 9)
    ok = r4 == 0 and r6 == want6 and sp.simplify(r8 - want8) == 0
    res = [sea_ratio(L, lambda s, c, E2: sp.Integer(1)) for L in (4, 6, 8)]
    checks.check("C1", ok and all(x == R(1, 3) for x in res), f"the filled sea's pressure over its energy density, avg(E r)/(3 avg E): 0 on the side-4 torus, {r6} on side 6, {want8} on side 8; the rescaled walk gives 1/3 on every torus")
    # per-mode: the band top (every active axis s^2 = 1) has r = 0; a mode with one active axis has r = c^2
    s = [sp.Integer(1), sp.Integer(1), sp.Integer(0)]
    r_top = rate_two_step(s, None, sum(x ** 2 for x in s))
    s1 = [sp.Rational(3, 5), 0, 0]
    r_one = rate_two_step(s1, None, sum(x ** 2 for x in s1))
    checks.check("C2", r_top == 0 and r_one == R(16, 25), "per mode p/rho = r/3 with r = 1 - sum s^4/E^2: r = 0 at k = (pi/2, pi/2, 0) (no pressure) and r = cos^2 k = 16/25 on an axis wave with sin k = 3/5")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    w = [S[a] * C[a] ** 2 for a in range(3)]
    v1 = [S[a] + b1 * w[a] for a in range(3)]
    v2 = [S[a] + b2 * w[a] for a in range(3)]
    Hc = sdot(v1) * sdot(v2) - sdot(v2) * sdot(v1)
    cross = [S[1] * w[2] - S[2] * w[1], S[2] * w[0] - S[0] * w[2], S[0] * w[1] - S[1] * w[0]]
    fac = 2 * I * (b2 - b1) if not mut("commutator_forged") else 2 * I * (b2 + b1)
    ok = sp.simplify(Hc - fac * sdot(cross)) == sp.zeros(2)
    E2 = sum(x ** 2 for x in S)
    lag = sp.expand(sum(x ** 2 for x in cross) - (E2 * sum(t ** 2 for t in w) - sum(S[a] * w[a] for a in range(3)) ** 2))
    checks.check("D1", ok and lag == 0, "[H(b1), H(b2)] = 2i(b2 - b1)(s x w).sigma with w_a = s_a c_a^2; the interband element of dH/db is |s^ x w|^2 = (E^2 sum s^2 c^4 - (sum s^2 c^2)^2)/E^2, zero iff the active axes share one cos^2")
    counts = {}
    for L in (4, 6, 8):
        n = 0
        for kk, s, c in torus_modes(L):
            ww = [s[a] * c[a] ** 2 for a in range(3)]
            cr = [s[1] * ww[2] - s[2] * ww[1], s[2] * ww[0] - s[0] * ww[2], s[0] * ww[1] - s[1] * ww[0]]
            n += int(any(sp.simplify(t) != 0 for t in cr))
        counts[L] = n
    s = [sp.sqrt(2) / 2, sp.Integer(1), sp.Integer(0)]
    c = [sp.sqrt(2) / 2, sp.Integer(0), sp.Integer(1)]
    ww = [s[a] * c[a] ** 2 for a in range(3)]
    E2v = sum(x ** 2 for x in s)
    elem = sp.simplify((E2v * sum(t ** 2 for t in ww) - sum(s[a] * ww[a] for a in range(3)) ** 2) / E2v)
    checks.check("D2", counts[4] == 0 and counts[6] == 0 and counts[8] > 0 and elem == R(1, 12), f"modes whose coin a stretch turns: none on the side-4 and side-6 tori, {counts[8]} of 512 on side 8; at k = (pi/4, pi/2, 0) the interband element is {elem}")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    eps = sp.Symbol("eps", positive=True)
    n = sp.symbols("n1:4", real=True)
    ok = True
    for sp_pt in itertools.product((0, 1), repeat=3):
        s = [sp.sin(sp.pi * sp_pt[a] + eps * n[a]) for a in range(3)]
        E2 = sum(x ** 2 for x in s)
        r = 1 - sum(x ** 4 for x in s) / E2
        ser = sp.series(r, eps, 0, 2).removeO()
        want = 1 if not mut("limit_forged") else 0
        ok = ok and sp.simplify(ser - want) == 0
    checks.check("E1", ok, "near each of the eight species points r = 1 + O(eps^2): long waves lose energy as 1/l under both rules and press rho/3, for every species")


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
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at the band top."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Friedmann", "Parker", "Hawking", "Unruh", "Bogoliubov", "Cauchy", "Schwarz", "Landau", "Zener", "Wilson")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Parker) —", 1)
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
    "per_element: executed - block 69's uniform form at isotropic strain; the first-order energy change; the identity sum s^2 c^2 = E^2 - sum s^4; r = |v|^2 and m_eff^2 = sum s^4",
    "per_site: executed - the per-mode pressure ratio r/3 at the band top and on an axis wave",
    "per_mode: executed - the commutator of two stretches and the interband element; every mode of the tori of side 4, 6 and 8",
    "per_block: executed - the filled sea's pressure ratio on the tori of side 4, 6, 8 against the rescaled walk's 1/3; long-wave limits at the eight species points",
    "lattice_wide: checked and not executed - the infinite-lattice sea ratio strictly between 0 and 1/3 (proof in the text); finite stretch (the completion); excitation rates for a given history",
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
    print(f"scope: under block 69's two-step coupling a uniform stretch lowers a walker's energy at d log E/d log l = -(1 - sum s^4/E^2); the filled sea presses strictly below rho/3 (0, 1/12 and an exact algebraic number on the tori of side 4, 6, 8); a stretch turns the coin at fixed wave number unless the active axes share one cos^2, so it can excite the sea; the rescaled walk of blocks 146 and 147 agrees only on long waves; the supervisor's own derivation, unrefereed; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
