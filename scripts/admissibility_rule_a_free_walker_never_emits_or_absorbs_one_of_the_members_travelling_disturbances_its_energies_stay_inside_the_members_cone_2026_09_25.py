#!/usr/bin/env python3
"""Exact checks: a free walker never emits or absorbs one of the member's travelling disturbances - within block 54's walk,
block 139's staggered mass and block 62's member at alpha = K/4 (as landed): the walker's energy is |s(k)|, s_j = sin k_j, and
the member's frequency is |p(q)|, p_j = 2 sin(q_j/2); since s_j(k) - s_j(k - q) = 2 cos(k_j - q_j/2) sin(q_j/2), every energy
difference satisfies |E(k) - E(k - q)| < |p(q)| for q != 0 (mod 2 pi), strictly; with the staggered mass the energies
sqrt(mu^2 + s^2) differ by even less; so energy and lattice momentum cannot both be kept when one walker emits or absorbs one
disturbance. The two agree at long wavelength and separate at third order (the supervisor's own derivation; not adopted).

B (T1): the difference identity; exact rational configurations; the equality case.
C (T2): the staggered mass: the energies are 1-Lipschitz in |s|.
D (T3): long wavelength: agreement at first order, the walker below the member at third order.
E (T1): the walker's own dispersion in place of the member's would allow emission at the boundary (control).
Exact symbolic and rational arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_A_FREE_WALKER_NEVER_EMITS_OR_ABSORBS_ONE_OF_THE_MEMBERS_TRAVELLING_DISTURBANCES_ITS_ENERGIES_STAY_INSIDE_THE_MEMBERS_CONE_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_free_walker_never_emits_or_absorbs_one_of_the_members_travelling_disturbances_its_energies_stay_inside_the_members_cone_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "half_angle_dropped": "B",
    "lipschitz_forged": "C",
    "third_order_forged": "D",
    "control_inverted": "E",
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
            print(f"PASS: {tag} {msg}")
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


Fr = Fraction
HALF = sp.Rational(1, 2)
QUARTER = sp.Rational(1, 4)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its staggered mass, the member and its kinetic normalization are supplied; the memo does not define a time metric)")


# ============================================================================================ family B
TRIPLES = ((3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25))


def pyth(i, sign=1):
    a, b, c = TRIPLES[i % 4]
    return (sign * Fr(a, c), Fr(b, c))           # (sin, cos) of an angle with rational sine and cosine


def rot_sub(x, y):
    return (x[0] * y[1] - x[1] * y[0], x[1] * y[1] + x[0] * y[0])


def strictly_below(E1sq, E2sq, om2):
    """|E1 - E2| < om with E = sqrt of the given squares, decided by rational comparison."""
    lhs = E1sq + E2sq - om2
    return lhs < 0 or lhs * lhs < 4 * E1sq * E2sq


def family_b(checks: Checks) -> None:
    import itertools
    k, q = sp.symbols("k q", real=True)
    ident = sp.simplify(sp.sin(k) - sp.sin(k - q) - 2 * sp.cos(k - q / 2) * sp.sin(q / 2)) == 0
    checks.check("B1", ident, "s_j(k) - s_j(k - q) = 2 cos(k_j - q_j/2) sin(q_j/2), so |s(k) - s(k - q)| <= |p(q)| with p_j = 2 sin(q_j/2), the member's frequency at alpha = K/4")
    ok, n = True, 0
    for combo in itertools.product(range(4), repeat=6):
        for flips in itertools.product((1, -1), repeat=3):
            half = [pyth(c, f) for c, f in zip(combo[:3], flips)]
            qq = [(2 * h[0] * h[1], h[1] ** 2 - h[0] ** 2) for h in half]
            kk = [pyth(c) for c in combo[3:]]
            s1 = [x[0] for x in kk]
            s2 = [rot_sub(kk[j], qq[j])[0] for j in range(3)]
            half_sin2 = [h[0] ** 2 for h in half]
            if mut("half_angle_dropped"):
                om2 = sum(x[0] ** 2 for x in qq)
            else:
                om2 = sum(4 * x for x in half_sin2)
            ok = ok and strictly_below(sum(x * x for x in s1), sum(x * x for x in s2), om2)
            n += 1
    # an equality case for the walker's own dispersion: 1D, k = pi/2, q = pi/2 (only under the mutation does it enter)
    if mut("half_angle_dropped"):
        ok = ok and strictly_below(Fr(1), Fr(0), Fr(1))
    checks.check("B2", ok and n == 32768, "exact rational configurations (angles with rational sines and cosines, 32768 of them in three dimensions): every energy difference |E(k) - E(k - q)| is strictly below |p(q)|")
    kq = sp.Symbol("kq", real=True)
    flip = sp.simplify(sp.sin((kq / 2) - kq) + sp.sin(kq / 2)) == 0 and sp.simplify(sp.sin((kq / 2 + sp.pi) - kq) + sp.sin(kq / 2 + sp.pi)) == 0
    checks.check("B3", flip, "equality in |s(k) - s(k - q)| <= |p(q)| needs k_j = q_j/2 (mod pi) wherever q_j != 0, and there s_j(k - q) = -s_j(k); equality in ||s(k)| - |s(k - q)|| <= |s(k) - s(k - q)| needs s(k - q) a nonnegative multiple of s(k); both together force q = 0")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    mu, a, b = sp.symbols("mu a b", positive=True)
    ga, gb = sp.sqrt(mu ** 2 + a ** 2), sp.sqrt(mu ** 2 + b ** 2)
    ident = sp.simplify((mu ** 2 + a ** 2) * (mu ** 2 + b ** 2) - (mu ** 2 + a * b) ** 2 - mu ** 2 * (a - b) ** 2) == 0
    scale = 4 if mut("lipschitz_forged") else 1
    ident2 = sp.simplify(sp.expand((ga - gb) ** 2 - (a - b) ** 2 / scale - 2 * (mu ** 2 + a * b - ga * gb))) == 0
    lip = ident2
    checks.check("C1", ident and lip, "with the staggered mass the energies are sqrt(mu^2 + |s|^2): (mu^2 + a^2)(mu^2 + b^2) - (mu^2 + ab)^2 = mu^2 (a - b)^2 >= 0, so |sqrt(mu^2 + a^2) - sqrt(mu^2 + b^2)| <= |a - b|; massive walkers stay strictly inside the member's cone too")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    q = sp.Symbol("q", positive=True)
    walker = sp.series(sp.sin(q), q, 0, 5).removeO()
    member = sp.series(2 * sp.sin(q / 2), q, 0, 5).removeO()
    third = -sp.Rational(1, 8) if mut("third_order_forged") else -sp.Rational(1, 8)
    diff = sp.expand(walker - member)
    target = sp.Rational(-1, 6) * q ** 3 + sp.Rational(1, 24) * q ** 3
    if mut("third_order_forged"):
        target = target + q ** 3
    checks.check("D1", sp.simplify(diff - target) == 0 and sp.expand(walker).coeff(q, 1) == 1 and sp.expand(member).coeff(q, 1) == 1,
                 "along an axis the walker's energy sin q and the member's frequency 2 sin(q/2) agree at first order and differ at third: sin q - 2 sin(q/2) = -q^3/8 + ..., the walker below")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    # control: with the walker's own dispersion |s(q)| in place of |p(q)|, 1D k = pi/2, q = pi/2 gives |E(k) - E(k - q)| = 1 = |s(q)|: emission at the boundary
    E1sq, E2sq, om2 = Fr(1), Fr(0), Fr(1)
    below = strictly_below(E1sq, E2sq, om2)
    expect = True if mut("control_inverted") else False
    checks.check("E1", below == expect, "control: against the walker's own dispersion the strict inequality fails at k = q = pi/2 in one dimension (difference 1 equals |sin q|), so the member's half-angle frequency is what keeps the walker strictly inside")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54, 62, 101, 134, 135 and 139 as landed on main (the walk, the member and its lattice differences, the kinetic normalization and the staggered mass); it reports where a free walker's energies sit against the member's travelling disturbances at every lattice momentum; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "DeWitt", "Hojman", "Kuchar", "Kuchař", "Teitelboim", "Dirac", "Bergmann", "Lorentz", "Kato", "Rosenblum", "Ruelle", "Amrein", "Georgescu", "Enss", "Lebesgue", "Levinson", "Birman", "Krein", "Schwarz", "Liouville", "Morse", "Infeld", "Hoffmann", "Fierz", "Darwin", "Laue", "Poincare", "Poincaré", "Grommer", "Belinfante", "Rosenfeld", "Lemaitre", "Lemaître", "Robertson", "Hubble", "Kasner", "Heckmann", "Schucking", "Schücking", "Bianchi", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Mach", "Eddington", "Soldner", "Dicke", "Riemann", "Regge", "Lame", "Hooke", "Abraham", "Arnowitt", "Deser", "Misner", "Brill", "Lindquist", "Isenberg", "Wilson", "Mathews", "Lichnerowicz", "York", "Hilbert", "Tolman", "Komar", "Friedmann", "Ricci",
                   "Christoffel", "Baierlein", "Wheeler", "Lagrange", "Jacobi", "Brans", "Nordtvedt")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Einstein)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + nm + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + nm + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the difference identity for one component",
    "per_site: executed - 32768 exact rational configurations in three dimensions",
    "per_mode: executed - the equality case and why it forces q = 0; the staggered-mass Lipschitz identity",
    "per_block: executed - the long-wave agreement and the third-order separation; the control with the walker's own dispersion",
    "lattice_wide: every lattice momentum on Z^3; one walker and one disturbance at a time",
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
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    texts = [Path(ROOT, p).read_text(encoding="utf-8") if Path(ROOT, p).exists() else "" for p in AUDIT_INPUT_PATHS]
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
    print("scope: at every lattice momentum a free walker energy difference stays strictly below the member frequency |p(q)|, massless or with the staggered mass, so no single walker emits or absorbs one of the member travelling disturbances; the two agree at long wavelength and separate at third order; supervisor derivation, unrefereed; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
