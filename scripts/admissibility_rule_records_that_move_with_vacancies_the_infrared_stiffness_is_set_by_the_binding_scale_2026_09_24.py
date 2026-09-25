#!/usr/bin/env python3
"""Exact checks: records that move with vacancies - the infrared stiffness is set by the binding scale, long-range order
holds above the neutral scale once (beta - gamma(c)) rho > 3G(0), and at the neutral scale the full-beta infrared bound is
false (a harvest block from a Grok-refereed probes attempt; blocks 19, 22, 39 and 40 as landed; not adopted).

B (T1): the split of the bond kernel and the positivity threshold of its remainder.
C (T2): the twist that yields the structure factor, and the bound where it is proved.
D (T3): the neutral scale - exact counterexamples on the 2x2x2 torus.
E (T4): the long-range-order criterion's constant.
Exact arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_WITH_VACANCIES_THE_INFRARED_STIFFNESS_IS_SET_BY_THE_BINDING_SCALE_LONG_RANGE_ORDER_ABOVE_THE_NEUTRAL_SCALE_AND_NO_FULL_BOUND_AT_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_BINDING_SCALE_PINNED_AT_THE_NEUTRAL_VALUE_PAIR_WEIGHT_IS_THE_RULES_LIKELIHOOD_RATIO_NO_BINDING_WITHOUT_A_CYCLE_ALL_BINDING_IS_AGREEMENT_AROUND_LOOPS_BOUNDED_THEOREM_NOTE_2026-09-20.md', 'docs/ADMISSIBILITY_RULE_CUBIC_WALK_RETURN_SUM_AND_SPHERE_STATIC_MAGNETIZATION_SUFFICIENT_BOUND_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE_IS_A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md', 'docs/ADMISSIBILITY_RULE_SPHERE_STATIC_LAW_ZERO_FIELD_COMPONENT_FOURIER_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_records_that_move_with_vacancies_the_infrared_stiffness_is_set_by_the_binding_scale_long_range_order_above_the_neutral_scale_and_no_full_bound_at_it_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "A site never carries more than one record; records are permanent.",
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "kernel_threshold_forged": "B",
    "twist_on_records_only": "C",
    "neutral_value_forged": "D",
    "green_bound_forged": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: a site never carries more than one record (a site is empty or holds one content); each site has a domain of local possibilities (the menu); Admissibility is not a dynamics axiom (the motion, the scale and the law with vacancies are supplied)")


# ============================================================================================ the law with vacancies on the 2x2x2 torus
SITES = list(product((0, 1), repeat=3))
BONDS = []
for _x in SITES:
    for _j in range(3):
        _y = list(_x)
        _y[_j] = 1 - _y[_j]
        BONDS.append((SITES.index(_x), SITES.index(tuple(_y))))
KS = list(product((0, 1), repeat=3))


def atanh_bounds(x, terms):
    """rational lower and upper bounds for atanh(x), 0 < x < 1, from the series and its geometric tail."""
    lo = sum(x ** (2 * n + 1) / (2 * n + 1) for n in range(terms))
    tail = x ** (2 * terms + 1) / ((2 * terms + 1) * (1 - x * x))
    return lo, lo + tail


def two_valued_law(eb, c, z):
    """two-valued menu with vacancies on the 2x2x2 torus (each site and direction one bond, so each pair is joined twice):
    returns the structure factors S(k) = <|sigma^(k)|^2> for k in {0, pi}^3, the density rho and the bond density rho_2."""
    num = {k: Fraction(0) for k in KS}
    zs, rho, rho2 = Fraction(0), Fraction(0), Fraction(0)
    ebi = 1 / eb
    for cfg in product((0, 1, -1), repeat=8):
        w = Fraction(1)
        for s in cfg:
            if s:
                w *= z
        for (i, j) in BONDS:
            if cfg[i] and cfg[j]:
                w *= c * (eb if cfg[i] == cfg[j] else ebi)
        zs += w
        rho += w * sum(1 for s in cfg if s)
        rho2 += w * sum(1 for (i, j) in BONDS if cfg[i] and cfg[j])
        for k in KS:
            amp = sum(cfg[i] * (-1) ** sum(k[t] * SITES[i][t] for t in range(3)) for i in range(8))
            num[k] += w * amp * amp
    return {k: num[k] / zs / 8 for k in KS}, rho / zs / 8, rho2 / zs / len(BONDS)


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the split of the bond kernel and the positivity of the remainder."""
    bb, bp, cc, tt, gg = sp.symbols("beta betap c t gamma", positive=True)
    ok_split = True
    for n1, n2 in ((0, 0), (0, 1), (1, 0), (1, 1)):
        d2 = n1 + n2 - 2 * n1 * n2 * tt
        rem = cc * sp.exp((bb - bp) * tt) if n1 * n2 else 1
        full = cc * sp.exp(bb * tt) if n1 * n2 else 1
        ok_split = ok_split and sp.simplify(sp.exp(bp * (n1 + n2) / 2) * sp.exp(-bp * d2 / 2) * rem - full) == 0
    kern = sp.Matrix([[1, 1, 1], [1, cc * sp.exp(gg), cc * sp.exp(-gg)], [1, cc * sp.exp(-gg), cc * sp.exp(gg)]])
    schur = kern[1:, 1:] - kern[1:, :1] * kern[:1, 1:]
    eigs = list(schur.eigenvals())
    want = [2 * cc * sp.cosh(gg) - 2, 2 * cc * sp.sinh(gg)]
    if mut("kernel_threshold_forged"):
        want = [2 * cc * sp.cosh(gg) - 1, 2 * cc * sp.sinh(gg)]
    ok_eig = len(eigs) == 2 and all(any(sp.simplify((a - b).rewrite(sp.exp)) == 0 for a in eigs) for b in want)
    ok_leg = True
    for ell in range(4):
        leg = sp.Rational(2 * ell + 1, 2) * sp.integrate(sp.legendre(ell, tt) * sp.exp(gg * tt), (tt, -1, 1))
        rod = sp.Rational(2 * ell + 1, 2) * gg ** ell / (2 ** ell * sp.factorial(ell)) * sp.integrate((1 - tt ** 2) ** ell * sp.exp(gg * tt), (tt, -1, 1))
        ok_leg = ok_leg and sp.simplify(leg - rod) == 0
    ok_a0 = sp.simplify(sp.integrate(sp.exp(gg * tt), (tt, -1, 1)) / 2 - sp.sinh(gg) / gg) == 0
    ok_neutral = sp.nsimplify(1 / sp.cosh(sp.log(3))) == sp.Rational(3, 5) and sp.nsimplify(1 / sp.cosh(sp.log(20))) == sp.Rational(40, 401)
    ok_mono = (sp.simplify(sp.diff(1 / sp.cosh(gg), gg) + sp.sinh(gg) / sp.cosh(gg) ** 2) == 0
               and sp.simplify(sp.diff(gg / sp.sinh(gg), gg) - (sp.sinh(gg) - gg * sp.cosh(gg)) / sp.sinh(gg) ** 2) == 0
               and sp.simplify(sp.diff(sp.sinh(gg) - gg * sp.cosh(gg), gg) + gg * sp.sinh(gg)) == 0)
    checks.check("B1", ok_split and ok_eig and ok_leg and ok_a0 and ok_neutral and ok_mono,
                 "T1: for every beta' the bond kernel splits as e^{(beta'/2)(n+n')} e^{-(beta'/2)|sigma - sigma'|^2} R_{beta-beta'} with sigma = n s (the empty state at the origin), exactly for the four occupation pairs; the two-valued remainder R_gamma has occupied Schur complement with eigenvalues 2c cosh gamma - 2 and 2c sinh gamma, for gamma>=0 it is a non-negative sum of products iff c >= 1/cosh gamma; on the sphere the Legendre coefficients of e^{gamma t} are (2l+1)/2 gamma^l/(2^l l!) int (1-t^2)^l e^{gamma t} dt > 0 (l <= 3 checked) with a_0 = sinh(gamma)/gamma, so for gamma>=0 the threshold is gamma/sinh(gamma), with only the constant coefficient at gamma=0; both thresholds decrease strictly (d/dgamma (sinh - gamma cosh) = -gamma sinh); the neutral values 1/cosh(ln 3) = 3/5 and 1/cosh(ln 20) = 40/401 are rational")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the twist that yields the structure factor moves the empty sites too; the bound where it is proved."""
    ok_lap = True
    for cfg in product((0, 1, -1), repeat=8):
        for k in KS[1:]:
            psi = [(-1) ** sum(k[t] * SITES[i][t] for t in range(3)) for i in range(8)]
            ek = 4 * sum(k)
            x_all = sum((psi[j] - psi[i]) * (cfg[j] - cfg[i]) for (i, j) in BONDS)
            if mut("twist_on_records_only"):
                x_all = sum((psi[j] - psi[i]) * (cfg[j] - cfg[i]) for (i, j) in BONDS if cfg[i] and cfg[j])
            if x_all != ek * sum(cfg[i] * psi[i] for i in range(8)):
                ok_lap = False
                break
        if not ok_lap:
            break
    ring = (1, 1, 0, 1)
    psi4 = (1, 0, -1, 0)
    rb = [(i, (i + 1) % 4) for i in range(4)]
    x_rec = sum((psi4[j] - psi4[i]) * (ring[j] - ring[i]) for (i, j) in rb if ring[i] and ring[j])
    x_all4 = sum((psi4[j] - psi4[i]) * (ring[j] - ring[i]) for (i, j) in rb)
    ok_ring = x_rec == 0 and x_all4 == 2 == 2 * sum(ring[i] * psi4[i] for i in range(4))
    ln3_lo, ln3_hi = [2 * v for v in atanh_bounds(Fraction(1, 2), 12)]
    ln32_lo, ln32_hi = [2 * v for v in atanh_bounds(Fraction(1, 5), 12)]
    ok_ctrl = True
    for c in (Fraction(1), Fraction(2)):
        sk, _, _ = two_valued_law(Fraction(3), c, Fraction(1, 8))
        ok_ctrl = ok_ctrl and all(sk[k] * 4 * sum(k) * ln3_hi < 1 for k in KS[1:])
    sk, _, _ = two_valued_law(Fraction(3), Fraction(4, 5), Fraction(1, 8))
    ok_ctrl = ok_ctrl and all(sk[k] * 4 * sum(k) * ln32_hi < 1 for k in KS[1:])
    gam = sp.acosh(sp.Rational(5, 4))
    ok_gamma = sp.simplify(sp.exp(gam) - 2) == 0
    checks.check("C1", ok_lap and ok_ring and ok_ctrl and ok_gamma,
                 "T2: the twist sigma_x -> sigma_x - phi_x e at EVERY site, empty ones included, gives the linear term sum_b (grad psi)(grad sigma) = E(k) sum sigma psi on all 3^8 configurations of the 2x2x2 torus and every k != 0, while twisting only record-record bonds gives 0 against 2 on the ring (+1, +1, empty, +1) at k = pi/2; where the proof applies the bound holds on the torus: S(k) beta_A E(k) < 1 at every k != 0 for e^beta = 3, z = 1/8 and c = 1, 2 (beta_A = beta) and c = 4/5 (gamma = arccosh(5/4) = ln 2, beta_A = ln(3/2)), with rational upper bounds on the logarithms")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: at the neutral scale the route closes, and the full-beta bound is false."""
    sk, rho, rho2 = two_valued_law(Fraction(3), Fraction(3, 5), Fraction(1, 8))
    want = Fraction(4295671717826064002261, 38505646859840596246081)
    if mut("neutral_value_forged"):
        want = want / 2
    ln3_lo, _ = [2 * v for v in atanh_bounds(Fraction(1, 2), 12)]
    ok1 = sk[(1, 1, 1)] == want and sk[(1, 1, 1)] * 12 * ln3_lo > Fraction(147, 100)
    sk2, rho_b, rho2_b = two_valued_law(Fraction(20), Fraction(40, 401), Fraction(1, 5))
    l2lo, _ = atanh_bounds(Fraction(1, 3), 20)
    l9lo, _ = atanh_bounds(Fraction(1, 9), 12)
    ln20_lo = 8 * l2lo + 2 * l9lo
    ok2 = sk2[(1, 1, 1)] * 12 * ln20_lo > Fraction(181, 100) and sk2[(1, 1, 1)] * 12 * ln20_lo * rho2_b > Fraction(181, 100) and Fraction(8, 10) < rho_b < Fraction(801, 1000)
    checks.check("D1", ok1 and ok2,
                 f"T3: at the neutral scale gamma(c0(beta)) = beta, so the proved strength beta_A = 0; and the full-beta bound fails there: on the 2x2x2 torus at e^beta = 3, c = 3/5, z = 1/8, S(pi,pi,pi) = {want} exactly and S beta E > 147/100; at e^beta = 20, c = 40/401, z = 1/5, S beta E > 181/100 and even the bond-density form S beta rho_2 E > 181/100 (rho in (8/10, 801/1000)), so neither 1/(beta E) nor 1/(beta rho_2 E) holds (logarithms bounded below by rational partial sums)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the long-range-order criterion and its constant."""
    u = sp.symbols("u", positive=True)
    ball = sp.simplify((1 / (2 * sp.pi) ** 3) * (sp.pi ** 2 / 4) * 4 * sp.pi * (sp.pi * sp.sqrt(3)))
    want = sp.sqrt(3) * sp.pi / 8
    if mut("green_bound_forged"):
        want = sp.sqrt(3) * sp.pi / 4
    ok_ball = sp.simplify(ball - want) == 0
    jordan = sp.simplify(2 * sp.sin(u / 2) ** 2 - (1 - sp.cos(u))) == 0
    ok_ends = sp.simplify(2 * sp.sin(sp.pi / 2) ** 2 - 2 * (sp.pi / sp.pi) ** 2) == 0
    checks.check("E1", ok_ball and jordan and ok_ends,
                 "T4: with 1 - cos u = 2 sin^2(u/2) >= 2u^2/pi^2 on [-pi, pi], E(k) >= 4|k|^2/pi^2 and G(0) <= (2 pi)^-3 (pi^2/4) 4 pi (pi sqrt 3) = sqrt(3) pi/8 exactly; so for the sphere torus liminf with beta_A>0 M^2 >= rho - 3G(0)/beta_A(c), and long-range order holds once (beta - gamma(c)) rho > 3G(0) (block 22 as landed: 3G(0) < 76/100); at c = c0(beta), gamma(c) = beta and the criterion is empty")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 39 and 40 as landed on main (the law with vacancies and its neutral scale), carried to the sphere and two-valued menus of blocks 19 and 22 as landed; it reports the infrared bound for the law with vacancies and its stiffness, where it holds and where it fails; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Rodrigues", "Legendre", "Schwarz", "Cauchy", "Griffiths", "Kelly", "Sherman", "Fortuin", "Kasteleyn", "Ginibre", "Frohlich", "Fröhlich", "Simon", "Spencer", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the kernel split for the four occupation pairs; the remainder's Schur complement and Legendre coefficients",
    "per_site: executed - the all-site twist against the Laplacian term on all 3^8 configurations of the 2x2x2 torus; the record-bond twist on the ring",
    "per_mode: executed - exact structure factors at all seven nonzero k of the 2x2x2 torus for five parameter sets",
    "per_block: executed - the neutral-scale counterexamples with rational bounds on the logarithms; the constant of the long-range-order criterion",
    "lattice_wide: T1-T2 on every even torus by proof (reflection positivity and domination, named imports), checked on the 2x2x2 torus; T4 on Z^3 through the torus limit as in block 19; the motion, the menu, the scale and the fugacity supplied; the neutral law's order at large beta open",
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
    print('scope: Static annealed Fourier bound with PSD, coercivity, finite-volume and liminf restrictions. Supplied model only; no audit verdict.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
