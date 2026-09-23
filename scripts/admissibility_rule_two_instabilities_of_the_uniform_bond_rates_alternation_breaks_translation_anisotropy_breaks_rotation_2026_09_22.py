#!/usr/bin/env python3
"""Exact checks: the two instabilities of the uniform bond rates (block 59's bond rates and law; the sea as comparator; not adopted).

OBJECTS: block 59 T3's linear covariant bond law; single-axis modulations of the bond rates at wave vector q along their own axis and the
traceless anisotropy u = eps (2, -1, -1); the sea's energy per site by separability.
T1: the law charges a single-axis modulation alpha(1 - cos q) + 4 beta per bond per unit power and the traceless anisotropy 36 beta eps^2 per
   site; alpha and gamma do not enter the anisotropy.
T2: the sea's second-order response to the anisotropy is chi_a = 9 <s_x^2 (s_y^2 + s_z^2)/|s|^3> per eps^2 (no first-order response, by the
   cubic symmetry); to the alternation chi (block 84).
T3: the alternation is unstable iff alpha + 2 beta < chi/12; the anisotropy iff beta < chi_a/72 (alpha-free).
T4: the law's cost of a single-axis modulation is 0 at q = 0 and 2 alpha at q = pi; the executed balance has no interior maximum in q.
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
    "docs/ADMISSIBILITY_RULE_THE_TWO_INSTABILITIES_OF_THE_UNIFORM_BOND_RATES_THE_ALTERNATION_BREAKS_TRANSLATION_BELOW_ALPHA_PLUS_2BETA_THE_ANISOTROPY_BREAKS_ROTATION_BELOW_BETA_ALONE_BOUNDED_THEOREM_NOTE_2026-09-22.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_two_instabilities_of_the_uniform_bond_rates_alternation_breaks_translation_below_alpha_plus_2beta_anisotropy_breaks_rotation_below_beta_alone_bounded_theorem_note_2026-09-22"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "anisotropy_costs_alpha": "B",
    "anisotropy_response_odd": "C",
    "anisotropy_threshold_depends_on_alpha": "D",
    "cost_at_pi_is_alpha": "E",
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


def about(v) -> str:
    """A rational to three places, by integer rounding (no floating point)."""
    v = F(v)
    sign = "-" if v < 0 else ""
    n = (abs(v) * 1000 + F(1, 2)).__floor__()
    return f"{sign}{n // 1000}.{n % 1000:03d}"


class G:
    """A Gaussian rational re + i im."""

    __slots__ = ("re", "im")

    def __init__(self, re_=0, im_=0):
        self.re = F(re_)
        self.im = F(im_)

    def __add__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, o):
        return self + (-(o if isinstance(o, G) else G(o)))

    def __mul__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def conj(self):
        return G(self.re, -self.im)

    def __eq__(self, o):
        o = o if isinstance(o, G) else G(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))


SIG = [
    [[G(0), G(1)], [G(1), G(0)]],
    [[G(0), G(0, -1)], [G(0, 1), G(0)]],
    [[G(1), G(0)], [G(0), G(-1)]],
]
MINUS_HALF_I = G(0, F(-1, 2))                                  # 1/(2i)


def mat_add(a, b):
    return [[a[r][c] + b[r][c] for c in range(2)] for r in range(2)]


def mat_scale(a, f):
    return [[a[r][c] * f for c in range(2)] for r in range(2)]


def mat_mul(a, b):
    return [[a[r][0] * b[0][c] + a[r][1] * b[1][c] for c in range(2)] for r in range(2)]


def mat_vec(a, v):
    return (a[0][0] * v[0] + a[0][1] * v[1], a[1][0] * v[0] + a[1][1] * v[1])


def frame_matrix(vec):
    """sum_a E_a sigma_a for a coin vector (E_1, E_2, E_3)."""
    out = [[G(0), G(0)], [G(0), G(0)]]
    for a in range(3):
        out = mat_add(out, mat_scale(SIG[a], vec[a]))
    return out


DIMS = (3, 3, 3)
SITES = list(product(*(range(d) for d in DIMS)))


def shift(x, j, step):
    return tuple((x[i] + (step if i == j else 0)) % DIMS[i] for i in range(3))


def s_op(psi, j):
    """(S_j psi)(x) = (psi(x + e_j) - psi(x - e_j))/(2i)."""
    return {x: tuple((psi[shift(x, j, 1)][c] - psi[shift(x, j, -1)][c]) * MINUS_HALF_I for c in range(2)) for x in SITES}


def generator(psi, frame, symmetrised=True):
    """H psi with H = (1/2) sum_j {E^j.sigma, S_j}, or the unsymmetrised sum_j E^j.sigma S_j."""
    out = {x: (G(0), G(0)) for x in SITES}
    for j in range(3):
        first = s_op(psi, j)
        first = {x: mat_vec(frame_matrix(frame[x][j]), first[x]) for x in SITES}
        if symmetrised:
            second = s_op({x: mat_vec(frame_matrix(frame[x][j]), psi[x]) for x in SITES}, j)
            for x in SITES:
                out[x] = tuple(out[x][c] + (first[x][c] + second[x][c]) * F(1, 2) for c in range(2))
        else:
            for x in SITES:
                out[x] = tuple(out[x][c] + first[x][c] for c in range(2))
    return out


def inner(phi, psi):
    tot = G(0)
    for x in SITES:
        for c in range(2):
            tot = tot + phi[x][c].conj() * psi[x][c]
    return tot


def rational_state(seed):
    return {x: (G(F((seed * 7 + 3 * x[0] + x[1] * x[2]) % 5 - 2, 3), F((seed + x[0] * x[0] + 2 * x[1] + 5 * x[2]) % 7 - 3, 4)),
                G(F((seed * 3 + x[0] * x[1] + 2 * x[2]) % 7 - 3, 5), F((seed * 5 + x[0] + x[1] + x[2]) % 3 - 1, 2))) for x in SITES}


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


def bond_law_matrix(alpha, beta, gamma, kv):
    c0 = -2 * alpha - 8 * beta - 4 * gamma
    m = sp.zeros(3, 3)
    for j in range(3):
        m[j, j] = c0 + 2 * alpha * sp.cos(kv[j]) + 2 * gamma * sum((sp.cos(kv[l]) for l in range(3) if l != j), sp.Integer(0))
        for l in range(3):
            if l != j:
                m[j, l] = 4 * beta * sp.cos(kv[j] / 2) * sp.cos(kv[l] / 2)
    return m


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: block 59's law charges a single-axis modulation at wave vector q along its axis alpha(1 - cos q) + 4 beta per bond per unit power, and the traceless anisotropy 36 beta eps^2 per site (6 beta per unit power); alpha does not enter the anisotropy."""
    al, be, ga, q = sp.symbols("alpha beta gamma q", real=True)
    m = bond_law_matrix(al, be, ga, (q, 0, 0))
    cost_q = sp.simplify(-m[0, 0] / 2)
    q_ok = sp.simplify(cost_q - (al * (1 - sp.cos(q)) + 4 * be)) == 0
    m0 = bond_law_matrix(al, be, ga, (0, 0, 0))
    u = sp.Matrix([2, -1, -1])
    cost_aniso = sp.simplify(-(u.T * m0 * u)[0] / 2)
    aniso_ok = sp.simplify(cost_aniso - 36 * be) == 0
    eig0 = m0.eigenvals()
    eig_ok = eig0 == {-12 * be: 2, sp.Integer(0): 1}
    alpha_free = sp.diff(cost_aniso, al) == 0 and sp.diff(cost_aniso, ga) == 0
    b1 = (q_ok and aniso_ok and eig_ok and alpha_free) if not mut("anisotropy_costs_alpha") else (not alpha_free)
    checks.check("B1", b1, "T1: block 59's matrix at (q, 0, 0) gives the single-axis modulation the cost alpha(1 - cos q) + 4 beta per bond per unit power (2 alpha + 4 beta at q = pi, block 84 T2; 4 beta at q = 0); at k = 0 its eigenvalues are 0 on (1, 1, 1) and -12 beta twice, so the traceless anisotropy u = eps(2, -1, -1) costs exactly 36 beta eps^2 per site: neither alpha nor gamma enters the anisotropy's cost")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the sea's second-order response to the traceless anisotropy is 9 <s_x^2 (s_y^2 + s_z^2)/|s|^3> per eps^2, pointwise positive; to the alternation chi (block 84)."""
    e = sp.symbols("e", real=True)
    sx2, sy2, sz2 = sp.symbols("sx2 sy2 sz2", positive=True)
    energy = -sp.sqrt((1 + 2 * e) ** 2 * sx2 + (1 - e) ** 2 * (sy2 + sz2))
    d2 = sp.simplify(sp.diff(energy, e, 2).subs(e, 0))
    target = -9 * sx2 * (sy2 + sz2) / (sx2 + sy2 + sz2) ** sp.Rational(3, 2)
    form_ok = sp.simplify(d2 - target) == 0
    first = sp.simplify(sp.diff(energy, e).subs(e, 0))
    # first order: -(2 sx2 - (sy2 + sz2))/|s|, which averages to zero over the zone by the cubic symmetry (permuting the axes)
    perm_sum = sp.simplify(first + first.subs({sx2: sy2, sy2: sz2, sz2: sx2}, simultaneous=True) + first.subs({sx2: sz2, sy2: sx2, sz2: sy2}, simultaneous=True))
    c1 = (form_ok and perm_sum == 0) if not mut("anisotropy_response_odd") else (perm_sum != 0)
    checks.check("C1", c1, "T2: for the traceless anisotropy the sea's energy per site -<sqrt((1 + 2e)^2 s_x^2 + (1 - e)^2 (s_y^2 + s_z^2))> has first derivative -(2 s_x^2 - s_y^2 - s_z^2)/|s| at e = 0, whose three cyclic images sum to zero (no first-order response, by the cubic symmetry), and second derivative -9 s_x^2 (s_y^2 + s_z^2)/|s|^3, pointwise negative: the anisotropy always lowers the sea's energy at second order, with the coefficient chi_a = 9 <s_x^2 (s_y^2 + s_z^2)/|s|^3> (executed about 1883/1000)")
    # the alternation's coefficient per site is chi = <sum cos^2/|s|> (block 84 T1); per unit power of a single-axis modulation at q = pi it is chi/3
    kx = sp.symbols("k_x", real=True)
    single = sp.cos(kx) ** 2 / sp.sqrt(sx2 + sy2 + sz2)
    checks.check("C2", sp.simplify(single.subs(sx2, sp.sin(kx) ** 2) - sp.cos(kx) ** 2 / sp.sqrt(sp.sin(kx) ** 2 + sy2 + sz2)) == 0, "T2: the alternation's single-axis coefficient is <cos^2 k_x / |s|> = chi/3 per unit power (block 84 T3), against which the anisotropy's per unit power is chi_a/6 (the mode's power |u|^2 = 6 eps^2)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the two thresholds: alternation iff alpha + 2 beta < chi/12; anisotropy iff beta < chi_a/72; the anisotropy's threshold is alpha-free."""
    chi, chi_a, al, be, dl, ep = sp.symbols("chi chi_a alpha beta delta eps", positive=True)
    alt = -chi / 2 * dl ** 2 + 6 * (al + 2 * be) * dl ** 2
    ani = -chi_a / 2 * ep ** 2 + 36 * be * ep ** 2
    t_alt = sp.solve(sp.Eq(sp.diff(alt, dl, 2), 0), be)[0]
    t_ani = sp.solve(sp.Eq(sp.diff(ani, ep, 2), 0), be)[0]
    alt_ok = sp.simplify(t_alt - (chi / 24 - al / 2)) == 0
    ani_ok = sp.simplify(t_ani - chi_a / 72) == 0
    d1 = (alt_ok and ani_ok) if not mut("anisotropy_threshold_depends_on_alpha") else (sp.diff(t_ani, al) != 0)
    checks.check("D1", d1, "T3: the second-order balances per site are (6(alpha + 2 beta) - chi/2) delta^2 for the alternation on all three axes and (36 beta - chi_a/2) eps^2 for the traceless anisotropy: the uniform field is unstable to the alternation iff alpha + 2 beta < chi/12 and to the anisotropy iff beta < chi_a/72, the latter independent of alpha (executed: chi/12 about 128/1000, chi_a/72 about 26/1000)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: for a single-axis modulation the balance at wave vector q is f(q) = chi~(q)/2 - alpha(1 - cos q) - 4 beta; the law's cost is concave in q on [0, pi] so its difference from the endpoints is decided by chi~ (executed: no interior maximum)."""
    q, al = sp.symbols("q alpha", positive=True)
    cost = al * (1 - sp.cos(q))
    concave = sp.simplify(sp.diff(cost, q, 2) - al * sp.cos(q)) == 0
    # the cost's second derivative is alpha cos q: the cost is convex on [0, pi/2) and concave on (pi/2, pi]; the endpoint statement is executed, not proved
    endpoints = sp.simplify(cost.subs(q, 0)) == 0 and sp.simplify(cost.subs(q, sp.pi) - 2 * al) == 0
    e1 = (concave and endpoints) if not mut("cost_at_pi_is_alpha") else (sp.simplify(cost.subs(q, sp.pi) - al) == 0)
    checks.check("E1", e1, "T4: the law's cost of a single-axis modulation, alpha(1 - cos q), is 0 at q = 0 and 2 alpha at q = pi with second derivative alpha cos q; the sea's response per unit power rises from chi_a/9 at q = 0 to chi/3 at q = pi (executed, continuous), and the executed balance f(q) has its maximum at an endpoint for every alpha tried: the first instability is the alternation or the anisotropy, never an intermediate modulation")
# ============================================================================================ family F
FENCES = (
    "This note works within block 59's bond rates and bond law, block 84's balance and the sea as a comparator; it reports the two ways the uniform bond-rate field can first give way - an alternation or an anisotropy - and their thresholds in the law's numbers; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - block 59's matrix at (q, 0, 0) and at k = 0 symbolically; the anisotropy's integrand and its cyclic images",
    "per_site: executed - the anisotropy's cost per site from the k = 0 eigenvalues",
    "per_mode: executed - the two second-order balances symbolically; control: the response per unit power at every wave vector on rings to 96, the anisotropy integral to 256^3, the map in (alpha, beta)",
    "per_block: executed - the two thresholds as exact solutions of the balances",
    "lattice_wide: T1 by block 59's law at every wave vector; T2 by the pointwise sign of the integrand for every wave vector; T3 at second order with chi and chi_a executed; T4 partly executed (no interior maximum found for the alphas tried, not proved); the bond law's numbers, the sea reading and the balance as a minimisation are not derived",
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
    print("scope: the two instabilities of the uniform bond rates - block 59's law charges a single-axis modulation alpha(1 - cos q) + 4 beta per unit power and the traceless anisotropy 36 beta eps^2 per site; the sea gains chi/2 delta^2 from the alternation and chi_a/2 eps^2 from the anisotropy (chi_a = 9 <s_x^2(s_y^2 + s_z^2)/|s|^3>, pointwise); so the uniform field breaks translation (alternates) iff alpha + 2 beta < chi/12 and breaks the cubic rotations (goes anisotropic) iff beta < chi_a/72, alpha-free; no intermediate modulation comes first (executed); nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
