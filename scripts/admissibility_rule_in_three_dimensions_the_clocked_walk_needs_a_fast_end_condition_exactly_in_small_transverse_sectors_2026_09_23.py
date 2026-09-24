#!/usr/bin/env python3
"""Exact checks: in three dimensions the clocked walk needs a fast-end boundary condition exactly in the transverse sectors with
|(sin k2, sin k3)| < sinh(g/2) - including sectors whose rays turn back (supervisor's derivation extending block 108;
block 54 as landed supplied; not adopted).

B (T1): across the gradient the walk reduces to line operators with an on-site term growing with the clock.
C (T2): the scaled zero-energy recurrence is constant; exact geometric solutions with r - 1/r = +-2m.
D (T3): square-summable count at the fast end: four for m < m* = (lambda - 1)/(2 sqrt(lambda)) = sinh(g/2), two above.
E (T4): rays with m > 0 turn back before the fast end; on the line the inverse-clock sum is finite.
Exact symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_IN_THREE_DIMENSIONS_THE_CLOCKED_WALK_NEEDS_A_FAST_END_CONDITION_EXACTLY_IN_THE_SECTORS_WITH_SMALL_TRANSVERSE_MOMENTUM_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_IN_AN_EXPONENTIAL_CLOCK_FIELD_THE_WALKS_DYNAMICS_NEEDS_A_BOUNDARY_CONDITION_AT_THE_FAST_CLOCK_END_BOUNDED_THEOREM_NOTE_2026-09-23.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_in_three_dimensions_the_clocked_walk_needs_a_fast_end_condition_exactly_in_the_sectors_with_small_transverse_momentum_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
    "define a time metric",
)

MUTATION_GATE = {
    "transverse_term_unscaled": "B",
    "root_modulus_forged": "C",
    "threshold_direction_flipped": "D",
    "ray_turning_forged": "E",
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


F = Fraction
ZERO = F(0)
ONE = F(1)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[:2]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: each site has a domain of local possibilities; Admissibility is not a dynamics axiom and does not define a time metric (the walk and its clock are supplied clauses)")


# ============================================================================================ helpers (block 54's 3D walk in a clock field growing along x1)
LAM = sp.symbols("lambda", positive=True)
S1 = sp.Matrix([[0, 1], [1, 0]])
S2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
S3 = sp.Matrix([[1, 0], [0, -1]])
SIG3 = [S1, S2, S3]


def walk3d_apply(psi, L1, L, w):
    """(H_w psi)(x) for H = sum_j sigma_j D_j, D_j = (i/2)(T_j - T_j^+), (T_e psi)(x) = psi(x - e), H_w = W^(1/2) H W^(1/2);
    psi: dict (x1, x2, x3) -> 2-vector on x1 in range(L1) (open), x2, x3 periodic mod L."""
    out = {}
    for (x1, x2, x3), v in psi.items():
        out.setdefault((x1, x2, x3), sp.zeros(2, 1))
    E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    res = {}
    for x1 in range(1, L1 - 1):
        for x2 in range(L):
            for x3 in range(L):
                x = (x1, x2, x3)
                acc = sp.zeros(2, 1)
                for j, e in enumerate(E):
                    xm = (x1 - e[0], (x2 - e[1]) % L, (x3 - e[2]) % L)
                    xp = (x1 + e[0], (x2 + e[1]) % L, (x3 + e[2]) % L)
                    acc += SIG3[j] * (sp.I / 2) * (sp.sqrt(w(x1)) * sp.sqrt(w(xm[0])) * psi[xm] - sp.sqrt(w(x1)) * sp.sqrt(w(xp[0])) * psi[xp])
                res[x] = acc
    return res


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: across the gradient the walk reduces, sector by sector, to a line operator with an on-site term growing with the clock."""
    L1, L = 5, 4
    f = [sp.Matrix(sp.symbols(f"f{n}a f{n}b")) for n in range(L1)]
    w = lambda x1: LAM ** x1
    ok = True
    for q2 in range(4):
        for q3 in range(4):
            ph = lambda x2, x3: sp.I ** ((q2 * x2 + q3 * x3) % 4)
            psi = {(x1, x2, x3): ph(x2, x3) * f[x1] for x1 in range(L1) for x2 in range(L) for x3 in range(L)}
            Hpsi = walk3d_apply(psi, L1, L, w)
            s2 = [0, 1, 0, -1][q2]
            s3 = [0, 1, 0, -1][q3]
            coef = 1 if not mut("transverse_term_unscaled") else 0
            for x1 in range(1, L1 - 1):
                red = S1 * (sp.I / 2) * (sp.sqrt(w(x1)) * sp.sqrt(w(x1 - 1)) * f[x1 - 1] - sp.sqrt(w(x1)) * sp.sqrt(w(x1 + 1)) * f[x1 + 1]) + w(x1) ** coef * (s2 * S2 + s3 * S3) * f[x1]
                for x2 in range(L):
                    for x3 in range(L):
                        ok = ok and sp.simplify(Hpsi[(x1, x2, x3)] - ph(x2, x3) * red) == sp.zeros(2, 1)
    checks.check("B1", ok, "T1: for w = lambda^(x1) and a plane wave exp(i(k2 x2 + k3 x3)) across the gradient, the clocked 3D walk acts as the line operator J_k = (sigma_1 D_1)_w + w(x1)(sin k2 sigma_2 + sin k3 sigma_3): the transverse hops become an on-site term that grows with the clock (exact for all 16 transverse wave numbers of a side-4 torus, symbolic lambda)")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: dividing by lambda^n makes the zero-energy recurrence constant; its solutions are exact geometric sequences."""
    a2, a3 = sp.Rational(3, 5), sp.Rational(4, 5)
    mm = sp.Integer(1)
    ok = True
    roots = []
    for r in (sp.sqrt(1 + mm ** 2) + mm, sp.sqrt(1 + mm ** 2) - mm, -sp.sqrt(1 + mm ** 2) + mm, -sp.sqrt(1 + mm ** 2) - mm):
        c = sp.simplify((r - 1 / r) / 2)
        K = a2 * S3 - a3 * S2
        vecs = (K - c * sp.eye(2)).nullspace()
        ok = ok and len(vecs) == 1
        v = vecs[0]
        roots.append(r)
        for n0 in range(-2, 3):
            rr = r if not mut("root_modulus_forged") else 2 * r
            psi = lambda n: (rr / sp.sqrt(LAM)) ** n * v
            lhs = S1 * (sp.I / 2) * (sp.sqrt(LAM ** n0) * sp.sqrt(LAM ** (n0 - 1)) * psi(n0 - 1) - sp.sqrt(LAM ** n0) * sp.sqrt(LAM ** (n0 + 1)) * psi(n0 + 1)) + LAM ** n0 * (a2 * S2 + a3 * S3) * psi(n0)
            ok = ok and sp.simplify(lhs) == sp.zeros(2, 1)
    nu, m = sp.symbols("nu m", positive=True)
    char = set(sp.solve(sp.Eq(nu - 1 / nu, 2 * m), nu)) | set(sp.solve(sp.Eq(nu + 1 / nu, 2 * sp.sqrt(1 + m ** 2)), nu))
    prod = sp.simplify((sp.sqrt(1 + m ** 2) + m) * (sp.sqrt(1 + m ** 2) - m)) == 1
    checks.check("C1", ok and prod, "T2: in a transverse sector with |(sin k2, sin k3)| = m, J_k psi = 0 divided by lambda^n is the constant recurrence -(i/2) sqrt(lambda) sigma_1 psi(n+1) + (i/2) sigma_1 psi(n-1)/sqrt(lambda) + M psi(n) = 0; its solutions are exactly psi(n) = (r/sqrt(lambda))^n v with r - 1/r = +-2m, so |r| = sqrt(1 + m^2) + m or its inverse sqrt(1 + m^2) - m (exact at (sin k2, sin k3) = (3/5, 4/5), m = 1, at five sites, symbolic lambda)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the count of square-summable solutions at the fast end and the threshold m* = (lambda - 1)/(2 sqrt(lambda)) = sinh(g/2)."""
    m = sp.symbols("m", nonnegative=True)
    g = sp.symbols("g", positive=True)
    big = sp.sqrt(1 + m ** 2) + m
    mstar = sp.solve(sp.Eq(big, sp.sqrt(LAM)), m)
    thr = len(mstar) == 1 and sp.simplify(mstar[0] - (LAM - 1) / (2 * sp.sqrt(LAM))) == 0
    sinh = sp.simplify(((sp.exp(g) - 1) / (2 * sp.exp(g / 2))) - sp.sinh(g / 2)) == 0
    below = sp.simplify(big.subs({m: sp.Rational(1, 4), LAM: 4}) - sp.sqrt(4)) < 0 if not mut("threshold_direction_flipped") else sp.simplify(big.subs({m: sp.Rational(1, 4), LAM: 4}) - sp.sqrt(4)) > 0
    above = sp.simplify(big.subs({m: sp.Rational(1, 1), LAM: 4}) - sp.sqrt(4)) > 0
    small_ok = sp.simplify((sp.sqrt(1 + m ** 2) - m).subs(m, sp.Rational(3, 4)) - sp.Rational(1, 2)) == 0
    zone = sp.simplify(((sp.sqrt(3) + sp.sqrt(2)) ** 2) - (5 + 2 * sp.sqrt(6))) == 0 and sp.simplify(big.subs(m, sp.sqrt(2)) - (sp.sqrt(3) + sp.sqrt(2))) == 0
    equality_not_summable = sp.simplify((big**2/LAM).subs({m:sp.sqrt(2), LAM:5+2*sp.sqrt(6)})) == 1
    checks.check("D1", thr and sinh and below and above and small_ok and zone and equality_not_summable, "T3: at the fast end the two solutions with |r| = sqrt(1 + m^2) - m are always square-summable (|r|^2 < lambda); the two with |r| = sqrt(1 + m^2) + m are square-summable exactly when m < m* = (lambda - 1)/(2 sqrt(lambda)) = sinh(g/2) for lambda = exp(g) (exact); at lambda = 4, m* = 3/4: m = 1/4 has four, m = 1 has two; every sector has four once sqrt(3) + sqrt(2) < sqrt(lambda), i.e. lambda > 5 + 2 sqrt(6)")


    mm, ll, xx = sp.symbols("mm ll xx", positive=True)
    ap = sp.Matrix([[-2*mm/sp.sqrt(ll), -1/ll], [1,0]])
    am = sp.Matrix([[2*mm/sp.sqrt(ll), -1/ll], [1,0]])
    expected = xx**2 + (2+4*mm**2)*xx/ll + 1/ll**2
    chain_ok = all(sp.simplify((b*a).charpoly(xx).as_expr()-expected)==0 for a,b in [(ap,am),(am,ap)])
    # charpoly uses its own real symbol; compare via explicit determinant instead.
    chain_ok = all(sp.simplify((xx*sp.eye(2)-b*a).det()-expected)==0 for a,b in [(ap,am),(am,ap)])
    boundary = (am*ap).subs({mm:sp.Rational(3,4),ll:4})
    checks.check("D2",chain_ok and (boundary+sp.eye(2)).det()==0 and (am*ap).subs(mm,0)==-sp.eye(2)/ll,"scalar-chain two-step characteristic, including a nondecaying equality mode")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the ray picture turns back every ray with m > 0; on the line (m = 0) the inverse-clock sum toward the fast end is finite."""
    w, E, m, k1 = sp.symbols("w E m k1", positive=True)
    energy = w * sp.sqrt(sp.sin(k1) ** 2 + m ** 2)
    wmax = sp.solve(sp.Eq(energy.subs(sp.sin(k1), 0), E), w)
    turn = len(wmax) == 1 and sp.simplify(wmax[0] - E / m) == 0
    at_turn = sp.simplify(energy.subs(sp.sin(k1), 0).subs(w, E / m) - E) == 0
    factor = 2 if not mut("ray_turning_forged") else sp.Rational(1, 2)
    beyond = sp.simplify(energy.subs(sp.sin(k1), 0).subs(w, factor * E / m) - E) > 0
    bound = at_turn and beyond
    x0 = sp.symbols("x0", integer=True)
    kk = sp.symbols("kk", integer=True, nonnegative=True)
    finite = sp.summation(sp.Integer(3) ** (-(x0 + kk)), (kk, 0, sp.oo)).subs(x0, 0) == sp.Rational(3, 2)
    line_all_four = sp.simplify((sp.sqrt(1 + m ** 2) + m).subs(m, 0) - 1) == 0
    checks.check("E1", turn and bound and finite and line_all_four, "T4: along a ray in a static field the energy E = w sqrt(sin^2 k1 + m^2) is kept with m fixed, so a ray with m > 0 turns back before w exceeds E/m and never reaches the fast end, while at m = 0 all four roots have modulus one (block 108's line), where the inverse-clock sum toward the fast end is finite (3/2 at lambda = 3; a scalar series, not an arrival-time statement): the sectors 0 < m < m* need a boundary condition though no ray with that m reaches the end (symbolic)")


# ============================================================================================ family F
FENCES = (
    "This note works within the supplied clock clause and walk of blocks 53 and 54, as landed on main, and extends block 108 to three dimensions; it reports which transverse sectors of the clocked walk in an exponential clock field need a boundary condition at the fast-clock end; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "Mathematical endpoint, spectral and calculus results are explicit imports within their stated hypotheses; they supply no physical premise or audit verdict.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the characteristic roots, their product and the threshold (symbolic)",
    "per_site: executed - the 3D walk on a 5 x 4 x 4 box against the reduced line operator for 16 transverse wave numbers; exact solutions at five sites",
    "per_mode: executed - the square-summable count by sector; the ray turning point",
    "per_block: executed - the whole zone beyond lambda = 5 + 2 sqrt(6)",
    "lattice_wide: T1-T4 on Z^3 with w = lambda^(x1), sector by sector, with the limit-point/limit-circle theory for matrix three-term operators imported at definition level; block 54 as landed supplied",
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
    print("scope: the clocked 3D walk in an exponential clock field - sector by sector across the gradient, a fast-end boundary condition is needed exactly below sinh(g/2), with equality limit point; the ray picture turns back every such ray with nonzero transverse momentum; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
