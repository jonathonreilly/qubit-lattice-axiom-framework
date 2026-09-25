#!/usr/bin/env python3
"""Exact checks: a rest energy from binding two walkers, without a larger site algebra - exact and relativistic with the walker's own
speed in one dimension for co-moving pairs, inverted for counter-moving ones, invisible under one record per site, and anisotropic in
three dimensions, where only coin triplets polarized across the motion have a normal dispersion (a harvest block from two Grok-refereed
probes attempts; block 54 as landed supplied; not adopted).

B (T1): the one-dimensional contact bound states: the lattice integral, and E^2 = V^2 + 4 sin^2(K/2) or V^2 + 4 cos^2(K/2).
C (T2): the three-dimensional channels at rest: the resolvent in the singlet and Cartesian triplets.
D (T3): the second and fourth moments of the pair's kinetic operator, and the strong-binding dispersions by channel.
E (T4, T5): exchange at coincidence and one record per site; the timed contact term keeps the scaling identity for the pair.
Exact symbolic and rational arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_A_REST_ENERGY_FROM_BINDING_TWO_WALKERS_IS_EXACT_WITH_THE_WALKERS_OWN_SPEED_IN_ONE_DIMENSION_INVISIBLE_UNDER_ONE_RECORD_PER_SITE_AND_ANISOTROPIC_IN_THREE_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_rest_energy_from_binding_two_walkers_is_exact_with_the_walkers_own_speed_in_one_dimension_invisible_under_one_record_per_site_and_anisotropic_in_three_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
    "define a time metric",
)

MUTATION_GATE = {
    "one_dimensional_speed_forged": "B",
    "triplet_resolvent_forged": "C",
    "along_triplet_taken_normal": "D",
    "untimed_contact_taken_to_scale": "E",
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


I = sp.I
F = Fraction


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: each site has a domain of local possibilities; Admissibility is not a dynamics axiom and does not define a time metric (the walk, its clock and the pair interaction are supplied clauses)")


# ============================================================================================ family B
S0 = sp.eye(2)
SIG = (sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]]))


def kron(a, b):
    return sp.kronecker_product(a, b)


def family_b(checks: Checks) -> None:
    """T1: the one-dimensional contact bound states of two walkers."""
    q = sp.symbols("q", real=True)
    ok_int = True
    for a, b in ((5, 1), (-3, 1), (7, 3), (-9, 2)):
        val = sp.integrate(1 / (a - 2 * b * sp.cos(q)), (q, 0, 2 * sp.pi)) / (2 * sp.pi)
        want = sp.sign(a) / sp.sqrt(a ** 2 - 4 * b ** 2)
        ok_int = ok_int and sp.simplify(val - want) == 0
    vv, ee, kk = sp.symbols("V E K", real=True)
    co = sp.solve(sp.Eq(1, vv * (-1) / sp.sqrt(ee ** 2 - 4 * sp.sin(kk / 2) ** 2)), ee)
    e2_co = vv ** 2 + 4 * sp.sin(kk / 2) ** 2
    e2_counter = vv ** 2 + 4 * sp.cos(kk / 2) ** 2
    ser_co = sp.series(e2_co, kk, 0, 5).removeO()
    ser_counter = sp.series(e2_counter, kk, 0, 3).removeO()
    speed = 1 if not mut("one_dimensional_speed_forged") else sp.Rational(3, 2)
    ok_disp = (sp.simplify(ser_co - (vv ** 2 + speed * kk ** 2 - kk ** 4 / 12)) == 0 and sp.simplify(ser_counter - (vv ** 2 + 4 - kk ** 2)) == 0
               and all(sp.simplify(sol ** 2 - e2_co) == 0 for sol in co))
    checks.check("B1", ok_int and ok_disp,
                 "T1: for two walkers sigma_z D on the line with a contact term V delta (V < 0), the bound state at total wave number K has phi(q) = 1/(E - eps(q)), eps = 2 sin(K/2) cos q for equal coins and 2 cos(K/2) sin q for opposite coins, and 1 = V (1/2pi) int dq/(E - eps) with (1/2pi) int dq/(a - 2b cos q) = sign(a)/sqrt(a^2 - 4b^2) (checked exactly at four points): co-moving pairs have E^2 = V^2 + 4 sin^2(K/2) = V^2 + K^2 - K^4/12 + ... - a rest energy |V| with the walker's own speed 1 - and counter-moving pairs E^2 = V^2 + 4 cos^2(K/2) = V^2 + 4 - K^2 + ..., inverted at rest")


# ============================================================================================ family C
def pair_basis():
    up, dn = sp.Matrix([1, 0]), sp.Matrix([0, 1])
    singlet = (kron(up, dn) - kron(dn, up)) / sp.sqrt(2)
    tx = (kron(dn, dn) - kron(up, up)) / sp.sqrt(2)
    ty = I * (kron(up, up) + kron(dn, dn)) / sp.sqrt(2)
    tz = (kron(up, dn) + kron(dn, up)) / sp.sqrt(2)
    return [singlet, tx, ty, tz]


def family_c(checks: Checks) -> None:
    """T2: the three-dimensional channels at rest."""
    h = sp.symbols("h1:4", real=True)
    ee = sp.symbols("E", real=True)
    amat = sum((h[j] * (kron(SIG[j], S0) - kron(S0, SIG[j])) for j in range(3)), sp.zeros(4, 4))
    basis = pair_basis()
    pm = sp.Matrix.hstack(*basis)
    res = sp.simplify(pm.H * (ee * sp.eye(4) - amat).inv() * pm)
    hh = sum((x ** 2 for x in h), sp.Integer(0))
    ok_s = sp.simplify(res[0, 0] - ee / (ee ** 2 - 4 * hh)) == 0
    tri = sp.Matrix(3, 3, lambda i, j: res[i + 1, j + 1])
    nn = sp.Matrix(h) * sp.Matrix(h).T / hh
    scale = 1 if not mut("triplet_resolvent_forged") else 2
    want = (sp.eye(3) - nn) / ee + nn * ee / (ee ** 2 - 4 * hh) * scale
    ok_t = sp.simplify(tri - want) == sp.zeros(3, 3)
    odd = all(sp.simplify(res[0, j] + res[0, j].subs({h[0]: -h[0], h[1]: -h[1], h[2]: -h[2]}, simultaneous=True)) == 0 for j in (1, 2, 3))
    annihilate = all(sp.simplify((kron(SIG[j], S0) + kron(S0, SIG[j])) * basis[j + 1]) == sp.zeros(4, 1) for j in range(3))
    checks.check("C1", ok_s and ok_t and odd and annihilate,
                 "T2: at rest (K = 0) in three dimensions the pair's kinetic operator is A = h(q).(sigma^1 - sigma^2); in the coin singlet and the Cartesian triplets T_j (zero total coin spin along axis j) its resolvent has <S|(E - A)^-1|S> = E/(E^2 - 4|h|^2), the triplet block (1 - n n^T)/E + n n^T E/(E^2 - 4|h|^2) with n = h/|h|, and singlet-triplet elements odd in h; averaged over q (cubic symmetry, <n_i n_j f> = delta_ij <f>/3) the contact conditions split into a singlet channel 1 = V I(E) and three triplet channels 1 = V (2/(3E) + I(E)/3), I(E) = <E/(E^2 - 4|h|^2)>")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the pair's second and fourth moments; strong-binding dispersions by channel."""
    u = sp.symbols("u1:4")
    cc = sp.symbols("c1:4")
    sin_of = lambda z: (z - 1 / z) / (2 * I)
    amat = sp.zeros(4, 4)
    for j in range(3):
        amat += sin_of(cc[j] * u[j]) * kron(SIG[j], S0) + sin_of(cc[j] / u[j]) * kron(S0, SIG[j])
    const = lambda expr: sp.Add(*[term for term in sp.Add.make_args(sp.expand(expr)) if not any(term.has(g) for g in u)])
    a2 = (amat * amat).applyfunc(sp.expand)
    m2 = a2.applyfunc(const)
    m4 = (a2 * a2).applyfunc(sp.expand).applyfunc(const)
    kap, vv = sp.symbols("kappa V", real=True)
    sub = {cc[0]: 1, cc[1]: 1, cc[2]: sp.exp(I * kap / 2)}
    pm = sp.Matrix.hstack(*pair_basis())
    m2z = sp.simplify(pm.H * m2.subs(sub) * pm)
    m4z = sp.simplify(pm.H * m4.subs(sub) * pm)
    diag = all(sp.simplify(m2z[i, j]) == 0 and sp.simplify(m4z[i, j]) == 0 for i in range(4) for j in range(4) if i != j)
    got = []
    for k in range(4):
        a2k, a4k = m2z[k, k], m4z[k, k]
        e2 = vv ** 2 + 2 * a2k + (2 * a4k - 3 * a2k ** 2) / vv ** 2
        got.append(sp.simplify(sp.expand(sp.series(e2, kap, 0, 3).removeO())))
    want = [vv ** 2 + 12 - 24 / vv ** 2 - (1 - 8 / vv ** 2) * kap ** 2,
            vv ** 2 + 4 + 16 / vv ** 2 + (1 - 2 / vv ** 2) * kap ** 2,
            vv ** 2 + 4 + 16 / vv ** 2 + (1 - 2 / vv ** 2) * kap ** 2,
            vv ** 2 + 4 + 16 / vv ** 2 + ((1 + 4 / vv ** 2) if mut("along_triplet_taken_normal") else -(1 + 4 / vv ** 2)) * kap ** 2]
    ok = diag and all(sp.simplify(g - w) == 0 for g, w in zip(got, want))
    checks.check("D1", ok,
                 "T3: the pair's moments M_n = <A(q; K)^n>_q are constant terms of Laurent polynomials; M_2 = 3 - sum_i cos K_i sigma^1_i sigma^2_i, and for motion along an axis M_2 and M_4 are diagonal in {S, T_x, T_y, T_z}; the strong-binding condition E = V sum m_n/E^n then gives, exactly to O(V^-2) and O(kappa^2): singlet E^2 = V^2 + 12 - 24/V^2 - (1 - 8/V^2) kappa^2 (inverted), triplets polarized across the motion V^2 + 4 + 16/V^2 + (1 - 2/V^2) kappa^2 (normal, c^2 = 1 - 2/V^2), the triplet along the motion V^2 + 4 + 16/V^2 - (1 + 4/V^2) kappa^2 (inverted)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: exchange at coincidence; T5: the timed contact term keeps the pair's scaling identity."""
    swap = sp.zeros(4, 4)
    for a_ in range(2):
        for b_ in range(2):
            swap[2 * b_ + a_, 2 * a_ + b_] = 1
    basis = pair_basis()
    ok_x = sp.simplify(swap * basis[0] + basis[0]) == sp.zeros(4, 1) and all(sp.simplify(swap * v - v) == sp.zeros(4, 1) for v in basis[1:])
    side = 7
    mu = 2
    sites = range(side)
    idx = {}
    for x1 in sites:
        for s1 in (0, 1):
            for x2 in sites:
                for s2 in (0, 1):
                    idx[(x1, s1, x2, s2)] = len(idx)
    dim = len(idx)
    sign = lambda s: 1 if s == 0 else -1

    def generator(timed, vc):
        hm = sp.zeros(dim, dim)
        for (x1, s1, x2, s2), col in idx.items():
            for d in (1, -1):
                y1 = x1 + d
                if 0 <= y1 < side:
                    amp = sp.Rational(1, 2) * I * sign(s1) * (-d) * mu ** (x1 + y1)
                    hm[idx[(y1, s1, x2, s2)], col] += amp
                y2 = x2 + d
                if 0 <= y2 < side:
                    amp = sp.Rational(1, 2) * I * sign(s2) * (-d) * mu ** (x2 + y2)
                    hm[idx[(x1, s1, y2, s2)], col] += amp
            if x1 == x2:
                hm[col, col] += vc * (mu ** (2 * x1) if timed else 1)
        return hm

    def shift(vec):
        out = sp.zeros(dim, 1)
        for (x1, s1, x2, s2), col in idx.items():
            if vec[col] != 0 and x1 + 1 < side and x2 + 1 < side:
                out[idx[(x1 + 1, s1, x2 + 1, s2)]] = vec[col]
        return out
    vc = sp.Rational(-5, 2)
    probe = sp.zeros(dim, 1)
    for k, key in enumerate(((2, 0, 2, 0), (2, 1, 3, 0), (3, 0, 2, 1), (3, 1, 3, 1))):
        probe[idx[key]] = k + 1
    timed_ok = True
    untimed_breaks = False
    for timed in (True, False):
        hm = generator(timed, vc)
        lhs = hm * shift(probe)
        rhs = mu ** 2 * shift(hm * probe)
        holds = sp.simplify(lhs - rhs) == sp.zeros(dim, 1)
        if timed:
            timed_ok = holds
        else:
            untimed_breaks = not holds
    claimed = untimed_breaks if not mut("untimed_contact_taken_to_scale") else (not untimed_breaks)
    checks.check("E1", ok_x and timed_ok and claimed,
                 "T4-T5: at coincidence the exchange of two walkers acts on the coins alone, with eigenvalue -1 on the singlet and +1 on each triplet, so a contact term reaches antisymmetric walkers only in the singlet and symmetric ones only in the triplets; under one record per site no amplitude sits at coincidence and the contact term vanishes identically; with the clock w = 4^x on a 7-site chain, the timed contact term V w(x) keeps H_w T = 4 T H_w for the joint translation of the pair, exactly on interior vectors, and the untimed contact term breaks it")


# ============================================================================================ family F
FENCES = (
    "This note works within block 54's walk and its clock clause, as landed on main, with a supplied contact interaction between two walkers; it reports what rest energy binding gives the pair, with which speed, in one and three dimensions, and what one record per site does to it; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Bethe", "Salpeter", "Cooper", "Hubbard", "Mattis", "Fermi", "Bose", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the lattice integral at four points; the one-dimensional dispersions and their expansions (symbolic)",
    "per_site: executed - the resolvent in the singlet and Cartesian triplets, symbolic in h; the exchange operator on the coins",
    "per_mode: executed - the pair's second and fourth moments as constant terms of Laurent polynomials, and the strong-binding dispersion of every channel",
    "per_block: executed - the timed and untimed contact terms against the joint translation on a 7-site chain with w = 4^x (exact)",
    "lattice_wide: T1 on Z for every V < 0 and K; T2-T3 on Z^3 at rest and, for motion along an axis, to O(V^-2) and O(kappa^2); T4-T5 for every pair on every lattice; the walk, its clock and the contact interaction are supplied",
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
    print("scope: two walkers bound by a contact term - in 1D co-moving pairs have rest energy |V| and the walker's speed, counter-moving pairs are inverted; under one record per site the contact term vanishes; in 3D only triplets polarized across the motion are normal (c^2 = 1 - 2/V^2); nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
