#!/usr/bin/env python3
"""Finite staggered-mass state, clock and weak-field symbol identities.
No localized-body or general no-tail theorem: checkerboard modulation of a point source
retains its low-momentum content. Rapid decay needs the source's explicit smooth spectral gap.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_A_MASSIVE_BODY_AT_REST_SITS_ON_ONE_SUBLATTICE_ITS_CHESSBOARD_OF_CLOCKS_STAYS_LOCAL_AND_NEVER_ENTERS_THE_PULL_AT_ANY_POWER_OF_THE_DISTANCE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_THE_AXIOMS_OWN_GENERATOR_THE_SCALAR_HOP_SPLITS_THE_EIGHT_SPECIES_INTO_FOUR_LEVELS_OF_ONE_SENSE_AND_A_STAGGERED_TERM_GIVES_THEM_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/ADMISSIBILITY_RULE_THE_FILLED_SEAS_ENERGY_AS_THE_LEDGERS_FIELD_TERM_A_CHESSBOARD_OF_CLOCKS_IS_INVISIBLE_THE_SEA_INDUCES_A_CLOCK_STIFFNESS_NOT_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/ADMISSIBILITY_RULE_THE_STRONG_FIELD_EXACTLY_BODIES_AT_REST_MAKE_THE_CLOCK_LAW_LINEAR_IN_THE_ROOT_OF_THE_RATE_THE_LEDGER_IS_A_SURFACE_TERM_BOUNDED_BY_A_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-21.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_massive_body_at_rest_sits_on_one_sublattice_its_chessboard_of_clocks_stays_local_and_never_enters_the_pull_at_any_power_of_the_distance_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "rest_density_forged": "B",
    "moving_weight_forged": "C",
    "chessboard_field_forged": "D",
    "symbol_forged": "E",
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


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[:2]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged (the staggered mass breaks one-site translation, as block 77 notes; no general locality assertion follows); Admissibility is not a dynamics axiom (the walk, the mass, the clock laws and the members are supplied)")


# ============================================================================================ block 77's massive walk on the 4^3 torus, with Gaussian-rational amplitudes
LL = 4
SITES = list(product(range(LL), repeat=3))
S1 = sp.Matrix([[0, 1], [1, 0]])
S2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
S3 = sp.Matrix([[1, 0], [0, -1]])
SIG = (S1, S2, S3)


def eps_site(x):
    return (-1) ** sum(x)


def apply_h(psi, mass, phi=None):
    """(phi (H + m eps) phi psi)(x), H = sum_j sigma_j D_j, (D_j psi)(x) = (i/2)(psi(x - e_j) - psi(x + e_j)) (symbol sin k_j)."""
    ph = phi if phi is not None else {x: 1 for x in SITES}
    pp = {x: ph[x] * psi[x] for x in SITES}
    out = {}
    for x in SITES:
        acc = sp.zeros(2, 1)
        for j in range(3):
            xm = list(x)
            xm[j] = (xm[j] - 1) % LL
            xp = list(x)
            xp[j] = (xp[j] + 1) % LL
            acc += SIG[j] * (sp.I / 2) * (pp[tuple(xm)] - pp[tuple(xp)])
        acc += mass * eps_site(x) * pp[x]
        out[x] = (ph[x] * acc).applyfunc(sp.expand)
    return out


def density(psi, hpsi):
    return {x: sp.re(sp.expand((psi[x].H * hpsi[x])[0])) for x in SITES}


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: a massive body at rest sits on one sublattice, with a non-negative energy density summing to m."""
    mm = sp.Rational(3, 4)
    ok = True
    for n in product((0, 1), repeat=3):
        for u in (sp.Matrix([1, 0]), sp.Matrix([1, sp.I])):
            chi = {x: sp.Integer((-1) ** sum(n[i] * x[i] for i in range(3))) * (1 + eps_site(x)) * u for x in SITES}
            hchi = apply_h(chi, mm)
            ok = ok and all((hchi[x] - mm * chi[x]).applyfunc(sp.expand).is_zero_matrix for x in SITES)
            ok = ok and all(chi[x].is_zero_matrix for x in SITES if eps_site(x) == -1)
            norm = sum((chi[x].H * chi[x])[0] for x in SITES)
            dens = density(chi, hchi)
            ok = ok and sp.simplify(sum(dens.values()) / norm - mm) == 0 and all(v >= 0 for v in dens.values())
            ok = ok and all(dens[x] == 0 for x in SITES if eps_site(x) == -1)
    phi = {x: sp.Rational(2 + (x[0] + 2 * x[1] + 3 * x[2]) % 3, 3) for x in SITES}
    chi = {x: (1 + eps_site(x)) * sp.Matrix([1, 0]) for x in SITES}
    hchi = apply_h(chi, mm, phi)
    dens = density(chi, hchi)
    want = {x: mm * phi[x] ** 2 * (chi[x].H * chi[x])[0] for x in SITES}
    if mut("rest_density_forged"):
        want = {x: mm * phi[x] * (chi[x].H * chi[x])[0] for x in SITES}
    ok_clock = all(sp.simplify(dens[x] - want[x]) == 0 for x in SITES)
    checks.check("B1", ok and ok_clock,
                 "T1: on the 4^3 torus with block 77's H + m eps (m = 3/4), the eight corner-labeled spanning modes (with pairwise redundancy) e^(i pi n.x)(1 + eps)u satisfy (H + m eps) chi = m chi exactly, vanish on every odd site, and have energy density m|chi_x|^2 >= 0 on the even sites and 0 on the odd ones, summing to m; with a clock field of rational phi the density is exactly m w_x |chi_x|^2, since phi H phi at an even site reads only odd neighbours")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: a moving massive walker's density is non-negative; its mass part alternates."""
    mm = sp.Rational(3, 4)
    psi = {x: sp.I ** x[0] * (1 + sp.Rational(eps_site(x), 3)) * sp.Matrix([1, 1]) for x in SITES}
    hpsi = apply_h(psi, mm)
    ok_eig = all((hpsi[x] - sp.Rational(5, 4) * psi[x]).applyfunc(sp.expand).is_zero_matrix for x in SITES)
    norm = sum(sp.expand((psi[x].H * psi[x])[0]) for x in SITES)
    even_w = sum(sp.expand((psi[x].H * psi[x])[0]) for x in SITES if eps_site(x) == 1) / norm
    mass_part = sum(mm * eps_site(x) * sp.expand((psi[x].H * psi[x])[0]) for x in SITES) / norm
    want_even = sp.Rational(4, 5)
    if mut("moving_weight_forged"):
        want_even = sp.Rational(3, 5)
    ok_w = sp.simplify(even_w - want_even) == 0 and sp.simplify(mass_part - sp.Rational(9, 20)) == 0 and sp.simplify(mass_part - mm ** 2 / sp.Rational(5, 4)) == 0
    dens = density(psi, hpsi)
    ok_pos = all(sp.simplify(dens[x] - sp.Rational(5, 4) * sp.expand((psi[x].H * psi[x])[0])) == 0 for x in SITES)
    checks.check("C1", ok_eig and ok_w and ok_pos,
                 "T2: on the 4^3 torus the state e^(i pi x1/2)(1 + eps/3)(1, 1) is an eigenstate of H + m eps with E = 5/4 at m = 3/4 (E^2 = |sin k|^2 + m^2); its weight is 4/5 on the even sites and 1/5 on the odd ones, its mass part sum m eps |psi|^2 is 9/20 = m^2/E, and its energy density E |psi_x|^2 is non-negative at every site")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the chessboard of clocks - its field, its cost, and who feels it."""
    gam, mm, vv = sp.symbols("gamma m V", positive=True)
    ok_a = True
    for x in SITES:
        avg = sp.Rational(sum(eps_site(tuple((x[i] + (d if i == j else 0)) % LL for i in range(3))) for j in range(3) for d in (1, -1)), 6)
        ok_a = ok_a and avg == -eps_site(x)
    u_amp = -gam * mm / (12 * vv)
    if mut("chessboard_field_forged"):
        u_amp = -gam * mm / (6 * vv)
    ok_field = sp.simplify((1 - (-1)) * u_amp - (-(gam / 6) * mm / vv)) == 0
    cc = sp.symbols("c", positive=True)
    bond_sum = 0
    for x in SITES:
        for j in range(3):
            y = tuple((x[i] + (1 if i == j else 0)) % LL for i in range(3))
            bond_sum += (cc ** eps_site(x) - cc ** eps_site(y)) ** 2
    ok_cost = sp.simplify(bond_sum - 3 * len(SITES) * (cc - 1 / cc) ** 2) == 0 and sp.simplify(bond_sum.subs(cc, 2)) > 0
    ok_hops = all(cc ** eps_site(x) * cc ** eps_site(tuple((x[i] + (1 if i == 0 else 0)) % LL for i in range(3))) == 1 for x in SITES)
    ok_mass = True
    for e in (1, -1):
        lhs = mm * e * cc ** (2 * e)
        rhs = mm * (cc ** 2 - cc ** -2) / 2 + mm * e * (cc ** 2 + cc ** -2) / 2
        ok_mass = ok_mass and sp.simplify(lhs - rhs) == 0
    checks.check("D1", ok_a and ok_field and ok_cost and ok_hops and ok_mass,
                 "T3: the six-neighbour average reverses the stagger (A eps = -eps on 4^3), so the rest source (m/V) eps is solved in the simplest member's weak-field law (1 - A) u = -(gamma/6)(e - ebar) by u = -(gamma m/(12 V)) eps, a chessboard of clocks phi = c^eps that costs (2/gamma) 3V (c - 1/c)^2 > 0; every bond product phi_x phi_y is 1, so no odd-step operator feels it, but phi (m eps) phi = m (c^2 - c^-2)/2 + m eps (c^2 + c^-2)/2: a massive walker feels it as a scalar potential and a mass factor")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the staggered part of a source never enters the pull at any power of 1/R."""
    k1, k2, k3 = sp.symbols("k1:4", real=True)
    one_minus_a = 1 - (sp.cos(k1) + sp.cos(k2) + sp.cos(k3)) / 3
    lap = 2 * (3 - sp.cos(k1) - sp.cos(k2) - sp.cos(k3))
    at_pi = {k1: sp.pi, k2: sp.pi, k3: sp.pi}
    want = (2, 12)
    if mut("symbol_forged"):
        want = (0, 12)
    ok_pi = one_minus_a.subs(at_pi) == want[0] and lap.subs(at_pi) == want[1]
    t = sp.symbols("t", positive=True)
    ser_a = sp.series(one_minus_a.subs({k1: t, k2: 0, k3: 0}), t, 0, 4).removeO()
    ser_l = sp.series(lap.subs({k1: t, k2: 0, k3: 0}), t, 0, 4).removeO()
    ok_small = sp.simplify(ser_a - t ** 2 / 6) == 0 and sp.simplify(ser_l - t ** 2) == 0
    ok_zero = sp.simplify(one_minus_a - lap / 6) == 0
    gam = sp.symbols("gamma", positive=True)
    ok_kernel = sp.simplify((-(gam / 6) / one_minus_a) - (-gam / lap)) == 0
    point_source = {(0,0,0): sp.Integer(1)}
    modulated = {x: (-1)**sum(x)*v for x,v in point_source.items()}
    counter = modulated==point_source and sum(modulated.values())==1
    checks.check("E1", ok_pi and ok_small and ok_zero and ok_kernel and counter,
                 "T4: the simplest member's weak-field symbol 1 - A(k) = Delta(k)/6 and the curvature member's Delta(k) = sum 2(1 - cos k_j) vanish only at k = 0 and equal 2 and 12 at the stagger's wave vector pi(1,1,1); both give the same kernel -gamma/Delta(k), -gamma/|k|^2 near k = 0; the point-source countercontrol retains a nonzero monopole after checkerboard modulation. Only an explicitly smooth spectral source vanishing near zero has the rapid-decay lemma; no universal interbody-pull conclusion follows")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54, 55, 56, 60, 76 and 77 as landed on main (the walk and its clock, the source as the amplitudes' energy density, the simplest and the curvature members, the chessboard of clocks, and the staggered mass); it reports where a massive body's energy sits, what its chessboard part does to the clocks, and whether that part enters the pull between bodies; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Hellmann", "Feynman", "Coulomb", "Poisson", "Fourier", "Dirac", "Kogut", "Susskind", "Wilson", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the eight corner-labeled spanning modes (with pairwise redundancy) of H + m eps on every site of the 4^3 torus, with and without a rational clock field",
    "per_site: executed - the energy density of a moving eigenstate at every site; its even and odd weights and its mass part",
    "per_mode: executed - the six-neighbour average of the stagger; the chessboard field and its bond cost; the bond products; the mass term under a chessboard of clocks",
    "per_block: executed - the two members' symbols at the stagger's wave vector and near zero, and their common kernel",
    "lattice_wide: T1-T3 exact on the 4^3 torus and by proof on every even torus; T4 conditional on an explicitly smooth source spectrum vanishing near zero; the general checkerboard-locality claim is withdrawn; the walk, mass, clock laws and members supplied",
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
    print('scope: Finite band-edge states retained; false general checkerboard locality withdrawn, replaced by smooth spectral-support decay lemma. Supplied model only; no audit verdict.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
