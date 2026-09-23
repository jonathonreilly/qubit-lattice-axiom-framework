#!/usr/bin/env python3
"""Exact checks: waves among moving records need a coupling that time reversal flips; clocked record motion never oscillates
(the owner's moving-records reading; block 95's clock-timed motion; routes to waves in the repository placed; nothing adopted).

B (T1): records on a ring of six with the clock field slaved to them (block 95), hops timed by the site left, the bond or the site entered:
   detailed balance at every move with block 95's pair law, so the generator is self-adjoint in L^2(pi): real spectrum, no oscillation,
   no orbits; contrast: a record hopping with a circulation has complex mode rates.
C (T2): a record that remembers its direction: on a line mu^2 - 2p cos(k) mu + (2p - 1) = 0, real at k = 0, diffusive density branch,
   complex only for short waves; in three dimensions the spectrum is closed under conjugation, the density branch real, direction modes
   oscillate while decaying.
D (T3): the three routes to long waves (momentum exchanged between records; a chiral pair exchange; possibility's qubit moving reversibly)
   couple two conserved things antisymmetrically at first order in k: rates +-i c|k|.
E (T3): the 24 rotations leave no vector invariant and one rank-2 form: content-blind records spread diffusively under every covariant rule.
Exact arithmetic only (integers, Fractions, exact symbolic algebra); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_WAVES_AMONG_MOVING_RECORDS_NEED_A_COUPLING_THAT_TIME_REVERSAL_FLIPS_CLOCKED_RECORD_MOTION_NEVER_OSCILLATES_BOUNDED_THEOREM_NOTE_2026-09-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_waves_among_moving_records_need_a_coupling_that_time_reversal_flips_clocked_record_motion_never_oscillates_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "records are permanent",
)

MUTATION_GATE = {
    "circulation_injected": "B",
    "circulation_hidden": "B",
    "long_wave_oscillation_forged": "C",
    "turning_biased": "C",
    "coupling_symmetrized": "D",
    "rotations_restricted_to_an_axis": "E",
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
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and records are permanent (contents never change)")


# ============================================================================================ helpers
from itertools import combinations

RING_M = {0: 35, 1: 5, 2: -13, 3: -19, 4: -13, 5: 5}     # 72 G(d) on the ring of six (block 95's zero-mean kernel, integers)


def ring_chain(n, two_a, circulate=False):
    """Records on a ring of six, clock field slaved to them with base 4: w_z = 4^(sum_r RING_M(z - r)).
    A hop x -> y runs at w_x^a w_y^(1 - a) = 2^(two_a m_x + (2 - two_a) m_y) (two_a = 2a in {0, 1, 2}); returns states, rates, law."""
    states = [frozenset(c) for c in combinations(range(6), n)]

    def m(z, C):
        return sum(RING_M[(z - r) % 6] for r in C)
    rates = {}
    for s in states:
        for x in s:
            for y in ((x + 1) % 6, (x - 1) % 6):
                if y in s:
                    continue
                s2 = (s - {x}) | {y}
                e = two_a * m(x, s) + (2 - two_a) * m(y, s)
                r = F(2) ** e
                if circulate and y == (x + 1) % 6:
                    r = r * 2
                rates[(s, s2)] = r
    law = {}
    for s in states:
        pair = sum((RING_M[(u - v) % 6] for u, v in combinations(sorted(s), 2)), 0)
        law[s] = F(2) ** ((2 - 2 * two_a) * pair)
    return states, rates, law


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: record motion in detailed balance under any clock timing is symmetrizable (real spectrum); a circulation oscillates."""
    ok = True
    count = 0
    for n in (2, 3):
        for two_a in (2, 1, 0):
            states, rates, law = ring_chain(n, two_a, circulate=mut("circulation_injected"))
            for (s, s2), r in rates.items():
                back = rates[(s2, s)]
                ok = ok and law[s] * r == law[s2] * back
                count += 1
    checks.check("B1", ok, f"T1: records on a ring of six with the clock field slaved to them (base 4, block 95's kernel), two and three records, hops timed by the site left (a = 1), the bond (a = 1/2) and the site entered (a = 0): every one of the {count} moves satisfies pi(C) rate(C -> C') = pi(C') rate(C' -> C) with block 95's pair law, exactly; the generator is therefore self-adjoint in L^2(pi): real, non-positive spectrum, every autocorrelation a nonnegative mixture of decaying exponentials - no oscillation at any wavelength, no orbit of one record about another")
    # one record on a ring of six: symmetric rates give real mode frequencies; a circulation gives complex ones
    w6 = sp.exp(sp.I * sp.pi / 3)
    cw, ccw = (sp.Integer(2), sp.Integer(1)) if not mut("circulation_hidden") else (sp.Integer(1), sp.Integer(1))
    sym_real = all(sp.im(sp.expand(sp.exp(sp.I * sp.pi * j / 3) + sp.exp(-sp.I * sp.pi * j / 3) - 2)) == 0 for j in range(6))
    circ_im = [sp.nsimplify(sp.im(sp.expand(cw * w6 ** j + ccw * w6 ** (-j) - cw - ccw))) for j in range(6)]
    oscillates = any(v != 0 for v in circ_im) and circ_im[1] == sp.sqrt(3) / 2
    checks.check("B2", sym_real and oscillates, "T1's contrast: one record on a ring of six hopping at equal rates both ways has real mode rates 2 cos(pi j/3) - 2; hopping at 2 one way and 1 the other (a circulation, not in detailed balance), the mode rates 2 omega^j + omega^-j - 3 have imaginary parts (sqrt(3)/2 at j = 1): the density wave travels round the ring")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: a record that remembers its direction: oscillating modes decay within the memory time; the density mode is diffusive."""
    k, p, mu = sp.symbols("k p mu", real=True)
    det_term = (2 * p - 1) if not mut("long_wave_oscillation_forged") else (2 * p + 1)
    M1 = sp.Matrix([[sp.exp(-sp.I * k) * p, sp.exp(-sp.I * k) * (1 - p)], [sp.exp(sp.I * k) * (1 - p), sp.exp(sp.I * k) * p]])
    cp = sp.expand(sp.simplify((M1 - mu * sp.eye(2)).det()).rewrite(sp.cos))
    want = sp.expand(mu ** 2 - 2 * p * sp.cos(k) * mu + det_term)
    cp_ok = sp.simplify(cp - want) == 0
    at0 = sp.solve(want.subs(k, 0), mu)
    real_at0 = all(sp.im(r) == 0 for r in at0) and set(sp.simplify(r) for r in at0) == {sp.Integer(1), sp.simplify(2 * p - 1)}
    lead = p * sp.cos(k) + sp.sqrt(p ** 2 * sp.cos(k) ** 2 - (2 * p - 1))
    ser = sp.simplify(sp.series(lead.subs(p, sp.Rational(3, 4)), k, 0, 4).removeO())
    diffusive = sp.simplify(ser - (1 - sp.Rational(3, 2) * k ** 2)) == 0          # p/(2(1 - p)) = 3/2 at p = 3/4
    disc_half = (p ** 2 * sp.cos(k) ** 2 - (2 * p - 1)).subs({p: sp.Rational(3, 4), k: sp.pi / 2})
    band = disc_half == sp.Rational(-1, 2)
    checks.check("C1", cp_ok and real_at0 and diffusive and band, "T2 on a line: a record that keeps its last direction with probability p and reverses otherwise has mode multipliers mu with mu^2 - 2p cos(k) mu + (2p - 1) = 0; at k = 0 they are 1 and 2p - 1 (real); the density branch is 1 - (p/(2(1 - p))) k^2 + ... (at p = 3/4: 1 - (3/2) k^2, diffusive); the branches are complex only where p^2 cos^2 k < 2p - 1 (at p = 3/4, k = pi/2 the discriminant is -1/2): short waves oscillate, long waves do not")
    # three dimensions: continue with probability p, otherwise turn to one of the other five directions
    q = sp.Rational(9, 10)
    dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    turn = [[q if i == j else (1 - q) / 5 for j in range(6)] for i in range(6)]
    if mut("turning_biased"):
        turn = [[q if i == j else ((1 - q) / 5 + (sp.Rational(1, 50) if j == 0 else 0) - (sp.Rational(1, 200) if j != 0 and j != i else 0)) for j in range(6)] for i in range(6)]
    T = sp.Matrix(turn)
    Pi = sp.Matrix(6, 6, lambda i, j: 1 if j == (i ^ 1) else 0)
    kv = (sp.pi / 2, 0, 0)
    E = sp.diag(*[sp.exp(-sp.I * sum(kv[c] * d[c] for c in range(3))) for d in dirs])
    Mk = E * T
    conj_ok = sp.simplify(Mk.conjugate() - Pi * Mk * Pi) == sp.zeros(6, 6)
    cpk = sp.Poly(sp.expand((Mk - mu * sp.eye(6)).det(method="berkowitz")), mu)
    real_coeffs = all(sp.im(c) == 0 for c in cpk.all_coeffs())
    cpr = sp.Poly([sp.re(c) for c in cpk.all_coeffs()], mu)
    n_real = sum(sp.Poly(f, mu).count_roots() * mult for f, mult in sp.sqf_list(cpr.as_expr())[1] if sp.degree(f, mu) > 0)
    lead_real = cpr.count_roots(sp.Rational(9, 10), 1) == 1
    T0 = sp.Poly(sp.expand((T - mu * sp.eye(6)).det(method="berkowitz")), mu)
    at_zero = sp.expand(T0.as_expr() - (1 - mu) * ((6 * q - 1) / 5 - mu) ** 5) == 0
    checks.check("C2", conj_ok and real_coeffs and n_real < 6 and lead_real and at_zero, f"T2 in three dimensions (continue with p = 9/10, else turn to one of the other five directions): the mode matrix M(k) = E(k)T satisfies conj(M(k)) = Pi M(k) Pi (Pi the inversion), so its spectrum is closed under conjugation; at k = 0 the multipliers are 1 and (6p - 1)/5 (five times); at k = (pi/2, 0, 0) the characteristic polynomial has real coefficients, exactly one root in (9/10, 1) (the density branch, real) and {6 - n_real} non-real roots (direction modes that oscillate while decaying)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the three routes to long waves each couple two conserved things antisymmetrically at first order in k."""
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    c, a, b, beta, mu = sp.symbols("c a b beta mu", positive=True)
    kv = sp.Matrix([k1, k2, k3])
    ksq = k1 ** 2 + k2 ** 2 + k3 ** 2
    sgn = -1 if not mut("coupling_symmetrized") else 1
    # sound: density rho and momentum g, conserved; d rho/dt = -i k.g, d g/dt = -i c^2 k rho (the momentum flips under time reversal)
    S = sp.zeros(4, 4)
    for j in range(3):
        S[0, 1 + j] = -sp.I * kv[j]
        S[1 + j, 0] = sgn * sp.I * c ** 2 * kv[j]
    cps = sp.factor(sp.expand((S - mu * sp.eye(4)).det()))
    sound = sp.simplify(cps - mu ** 2 * (mu ** 2 + c ** 2 * ksq)) == 0
    # colour pair (the mobile-record lane's curl form): dX/dt = a i k x Y, dY/dt = -b i k x X
    def cross(v):
        return sp.Matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    K = cross(kv)
    C6 = sp.zeros(6, 6)
    C6[0:3, 3:6] = a * sp.I * K
    C6[3:6, 0:3] = -b * sp.I * K
    cpc = sp.factor(sp.expand((C6 - mu * sp.eye(6)).det()))
    colour = sp.simplify(cpc - mu ** 2 * (mu ** 2 + a * b * ksq) ** 2) == 0
    # the walk: H(k) = beta sum_j sigma_j sin k_j; H^2 = beta^2 sum sin^2 k_j (the Pauli matrices anticommute)
    sx, sy, sz = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])
    H = beta * (sx * sp.sin(k1) + sy * sp.sin(k2) + sz * sp.sin(k3))
    walk = sp.simplify(H * H - beta ** 2 * (sp.sin(k1) ** 2 + sp.sin(k2) ** 2 + sp.sin(k3) ** 2) * sp.eye(2)) == sp.zeros(2, 2)
    checks.check("D1", sound and colour and walk, "T3: the three routes in the repository give long waves by coupling two conserved things antisymmetrically at first order in k: records with a direction that collisions exchange (density and momentum; block 44): characteristic polynomial mu^2 (mu^2 + c^2 |k|^2), rates +-i c|k|; record pairs with a chiral exchange rate (colour moments X, Y; the mobile-record lane, #8600): mu^2 (mu^2 + ab|k|^2)^2, rates +-i sqrt(ab)|k| with ab = gamma^2 rho_A rho_B/3; possibility's own qubit moving reversibly (the walk; block 54): H^2 = beta^2 sum sin^2 k_j, frequencies +-beta|sin k| -> +-beta|k|; made symmetric, the coupling gives real rates (growth and decay), not waves")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T3 (content-blind records): the 24 rotations leave no vector invariant and one rank-2 tensor (delta): no drift, isotropic spreading."""
    rots = []
    for perm in ((0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)):
        for signs in product((1, -1), repeat=3):
            R = sp.zeros(3, 3)
            for i in range(3):
                R[i, perm[i]] = signs[i]
            if R.det() == 1:
                rots.append(R)
    if mut("rotations_restricted_to_an_axis"):
        rots = [R for R in rots if R[2, 2] == 1]
    avg1 = sum(rots, sp.zeros(3, 3)) / len(rots)
    avg2 = sp.zeros(9, 9)
    for R in rots:
        avg2 += sp.kronecker_product(R, R)
    avg2 = avg2 / len(rots)
    delta = sp.Matrix(9, 1, lambda i, j: 1 if i in (0, 4, 8) else 0)
    iso = avg2 == delta * delta.T / 3
    checks.check("E1", len(rots) == 24 and avg1 == sp.zeros(3, 3) and iso, "T3 for content-blind records: the average of the 24 proper cubic rotations is the zero matrix (no vector is invariant, so a covariant rule gives the record density no drift), and the average of R (x) R projects onto delta_ij (the only invariant second-rank form): with one conserved number the long-wave current is -D grad(rho), and the mode is diffusive under every covariant rule, reversible or not")


# ============================================================================================ family F
FENCES = (
    "This note works within the owner's moving-records reading (records move, one per site at a time; the possibility at a site shifts as its neighbourhood changes) and block 95's clock-timed motion; it reports what record motion can and cannot do about waves and places the routes in the repository; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - detailed balance at every move of two and three records on a ring of six for three timings; the line and three-dimensional mode matrices of a record with direction memory",
    "per_site: executed - the clock field at every site of the ring from block 95's kernel; the inversion relation of the three-dimensional mode matrix",
    "per_mode: executed - mode rates of one record on a ring with and without circulation; characteristic polynomials of the three wave routes at general k; control: spectra of larger clocked chains and of the direction-memory record",
    "per_block: executed - averages of the 24 rotations on vectors and rank-2 forms",
    "lattice_wide: T1 for every finite chain in detailed balance (proof), checked on the ring; T2 exact on the line, at k = 0 and one k in three dimensions; T3 for the three linear systems at every k and for every covariant rule on content-blind records at the level of the long-wave current; the routes' own clauses are supplied",
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
    print("scope: waves among moving records - clocked record motion in detailed balance never oscillates (real spectrum, no fronts, no orbits); direction memory alone gives only decaying oscillations of short waves; long waves need two conserved things coupled by a term time reversal flips: momentum passed between records, a chiral pair exchange, possibility moving reversibly, link memory; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
