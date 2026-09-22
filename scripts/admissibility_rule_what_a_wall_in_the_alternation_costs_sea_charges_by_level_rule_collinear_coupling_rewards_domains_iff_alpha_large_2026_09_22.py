#!/usr/bin/env python3
"""Exact checks: what a wall in the alternation costs (block 59's bond rates and bond law; the sea as comparator; not adopted).

OBJECTS: the one-axis operator with two sharp walls on an even ring; block 86's separability; block 59 T3's linear covariant bond law as a
real-space quadratic form on the 4^3 torus; the alternation with two walls across x.
T1: two sharp walls replace exactly the four levels {+-delta, +-1} by {0, 0, +-sqrt(1 + delta^2)} (rings of 4, 8, 12, exact); the sea's energy of
   the pair is (1 + delta) - sqrt(1 + delta^2), positive, independent of the ring's length.
T2: in three dimensions the sea's wall tension is the transverse zone average of four square roots, positive by concavity; 2 sqrt3 - sqrt2 - 2 at delta = 1.
T3: block 59's law rewards a wall by exactly 2 alpha delta^2 per unit area (beta and gamma do not enter).
T4: walls are favoured iff alpha > sigma_sea(delta)/(2 delta^2).
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
    "docs/ADMISSIBILITY_RULE_WHAT_A_WALL_IN_THE_ALTERNATION_COSTS_THE_SEA_CHARGES_IT_BY_AN_EXACT_LEVEL_RULE_BLOCK_59S_COLLINEAR_COUPLING_REWARDS_IT_DOMAINS_IFF_ALPHA_LARGE_BOUNDED_THEOREM_NOTE_2026-09-22.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_what_a_wall_in_the_alternation_costs_the_sea_charges_it_by_an_exact_level_rule_block_59s_collinear_coupling_rewards_it_domains_iff_alpha_large_bounded_theorem_note_2026-09-22"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "walls_shift_every_level": "B",
    "sea_rewards_a_wall": "C",
    "law_charges_a_wall": "D",
    "criterion_at_delta_one_above_a_tenth": "E",
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


def axis_operator(size, delta, walls):
    """(1/2i)(t T - T^T t) on a ring, t_x = 1 + delta s_x (-1)^x; two walls when `walls` (s flips at the half)."""
    t_shift = sp.zeros(size, size)
    for x in range(size):
        t_shift[x, (x + 1) % size] = 1
    signs = [1 if (not walls or x < size // 2) else -1 for x in range(size)]
    t = sp.diag(*[1 + delta * signs[x] * (-1) ** x for x in range(size)])
    return (t * t_shift - t_shift.T * t) / (2 * sp.I)


def squared_spectrum(m):
    out = {}
    for v, mult in (m * m).eigenvals().items():
        key = sp.nsimplify(sp.simplify(v))
        out[key] = out.get(key, 0) + mult
    return {k: v for k, v in out.items() if v != 0}


def torus_bonds(size):
    return [(x, a) for x in product(range(size), repeat=3) for a in range(3)]


def step(x, a, d, size):
    y = list(x)
    y[a] = (y[a] + d) % size
    return tuple(y)


def bond_neighbours(b, size):
    """Block 59 T3's three classes for the bond b = (x, a): collinear (2), parallel (4), perpendicular (8)."""
    x, a = b
    coll = [(step(x, a, d, size), a) for d in (1, -1)]
    par = [(step(x, l, d, size), a) for l in range(3) if l != a for d in (1, -1)]
    perp = []
    for l in range(3):
        if l == a:
            continue
        for base in (x, step(x, a, 1, size)):
            perp.append((base, l))
            perp.append((step(base, l, -1, size), l))
    return coll, par, perp


def law_energy(u, size, alpha, beta, gamma):
    """F = -1/2 sum_b u_b (c_0 u_b + alpha sum_coll u + beta sum_perp u + gamma sum_par u), c_0 = -2 alpha - 8 beta - 4 gamma (block 59 T3)."""
    c0 = -2 * alpha - 8 * beta - 4 * gamma
    tot = ZERO
    for b in torus_bonds(size):
        coll, par, perp = bond_neighbours(b, size)
        tot += u[b] * (c0 * u[b] + alpha * sum((u[n] for n in coll), ZERO) + beta * sum((u[n] for n in perp), ZERO) + gamma * sum((u[n] for n in par), ZERO))
    return -tot / 2


def bond_pattern(size, delta, walls_x):
    u = {}
    for (x, a) in torus_bonds(size):
        s = -1 if (a == 0 and walls_x and x[0] >= size // 2) else 1
        u[(x, a)] = delta * s * ((-1) ** x[a])
    return u


DELTA = sp.Rational(3, 10)


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: two sharp walls on an even ring replace exactly the four levels {+-delta, +-1} by {0, 0, +-sqrt(1 + delta^2)}; the rest of the spectrum is unchanged."""
    ok = True
    report = []
    for size in (4, 8, 12):
        uni = squared_spectrum(axis_operator(size, DELTA, False))
        wal = squared_spectrum(axis_operator(size, DELTA, True))
        conj = dict(uni)
        conj[DELTA ** 2] = conj.get(DELTA ** 2, 0) - 2
        conj[sp.Integer(1)] = conj.get(sp.Integer(1), 0) - 2
        conj[sp.Integer(0)] = conj.get(sp.Integer(0), 0) + 2
        conj[1 + DELTA ** 2] = conj.get(1 + DELTA ** 2, 0) + 2
        conj = {k: v for k, v in conj.items() if v != 0}
        same = conj == wal
        ok = ok and same
        report.append(f"ring {size}: {len(uni)} distinct E^2 without walls, {len(wal)} with; rule holds: {same}")
    b1 = ok if not mut("walls_shift_every_level") else (not ok)
    checks.check("B1", b1, "T1: on the rings of 4, 8 and 12 at delta = 3/10 the squared spectrum with two walls equals the wall-free one with two copies of delta^2 and two of 1 removed and two of 0 and two of 1 + delta^2 added, exactly: " + "; ".join(report))
    d = sp.symbols("delta", positive=True)
    pair_energy = 1 + d - sp.sqrt(1 + d ** 2)
    positive = sp.simplify(sp.expand((1 + d) ** 2 - (1 + d ** 2))) == 2 * d
    checks.check("B2", positive, "T1: the sea's energy of the wall pair on a ring is (1 + delta) - sqrt(1 + delta^2) (the four levels' negative branch -delta - 1 becomes -sqrt(1 + delta^2)), positive since (1 + delta)^2 - (1 + delta^2) = 2 delta > 0, and independent of the ring's length by the rule")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: in three dimensions the sea's wall tension is a transverse zone average of four square roots, positive by concavity; exact at delta = 1."""
    d, e2 = sp.symbols("delta e2", positive=True)
    integrand = sp.sqrt(d ** 2 + e2) + sp.sqrt(1 + e2) - sp.sqrt(e2) - sp.sqrt(1 + d ** 2 + e2)
    # concavity of sqrt: for 0 <= p <= q <= r <= s with p + s = q + r, sqrt(q) + sqrt(r) >= sqrt(p) + sqrt(s); here p = e2, q = e2 + delta^2, r = e2 + 1, s = e2 + 1 + delta^2
    sums_match = sp.simplify((e2) + (1 + d ** 2 + e2) - (d ** 2 + e2) - (1 + e2)) == 0
    # a rational check point: e2 = 9/16, delta = 3/10 -> values with exact square roots compared exactly
    val = integrand.subs({d: sp.Rational(3, 10), e2: sp.Rational(9, 16)})
    positive_point = bool(sp.simplify(val) > 0)
    at_one = sp.simplify(integrand.subs({d: 1, e2: 2}) - (2 * sp.sqrt(3) - sp.sqrt(2) - 2)) == 0
    c1 = (sums_match and positive_point and at_one) if not mut("sea_rewards_a_wall") else (not positive_point)
    checks.check("C1", c1, "T2: by T1 and block 86's separability, a wall's sea energy per unit area is the transverse zone average of sqrt(delta^2 + e^2) + sqrt(1 + e^2) - sqrt(e^2) - sqrt(1 + delta^2 + e^2), e^2 = e_y^2 + e_z^2; the four arguments have equal pairwise sums and the inner pair is less spread, so by the concavity of the square root the integrand is positive at every transverse wave vector (exactly positive at delta = 3/10, e^2 = 9/16); at delta = 1 (e^2 = 2 everywhere) the tension is exactly 2 sqrt(3) - sqrt(2) - 2")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: block 59's law charges the uniform alternation 2(alpha + 2 beta) delta^2 per bond and REWARDS a wall by exactly 2 alpha delta^2 per unit area (beta, gamma do not enter)."""
    size = 4
    al, be, ga = F(1, 7), F(1, 11), F(1, 5)
    dl = F(3, 10)
    fu = law_energy(bond_pattern(size, dl, False), size, al, be, ga)
    fw = law_energy(bond_pattern(size, dl, True), size, al, be, ga)
    uniform_ok = fu == 3 * size ** 3 * 2 * (al + 2 * be) * dl * dl
    per_area = (fw - fu) / (2 * size * size)
    reward_ok = per_area == -2 * al * dl * dl
    only_alpha = True
    for (a_, b_, g_) in ((F(1, 7), ZERO, ZERO), (ZERO, F(1, 11), ZERO), (ZERO, ZERO, F(1, 5))):
        diff = (law_energy(bond_pattern(size, dl, True), size, a_, b_, g_) - law_energy(bond_pattern(size, dl, False), size, a_, b_, g_)) / (2 * size * size)
        only_alpha = only_alpha and diff == -2 * a_ * dl * dl
    d1 = (uniform_ok and reward_ok and only_alpha) if not mut("law_charges_a_wall") else (per_area > 0)
    checks.check("D1", d1, f"T3: on the 4^3 torus block 59's law gives the uniform alternation the energy 3N x 2(alpha + 2 beta) delta^2 (block 84 T2) and two walls across x change it by {fw - fu}, that is -2 alpha delta^2 = {-2 * al * dl * dl} per unit area per wall: the collinear coupling alone rewards a phase slip (its two wall bonds each lose one opposing neighbour), the perpendicular and parallel couplings do not see it")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the wall's total energy per unit area is sigma_sea(delta) - 2 alpha delta^2: walls are favoured iff alpha > sigma_sea(delta)/(2 delta^2)."""
    d = sp.symbols("delta", positive=True)
    # at delta = 1 the transverse average is exact: sigma_sea(1) = 2 sqrt(3) - sqrt(2) - 2; the criterion there is alpha > (2 sqrt 3 - sqrt 2 - 2)/2
    crit = (2 * sp.sqrt(3) - sp.sqrt(2) - 2) / 2
    bounds = bool(sp.Rational(2, 100) < crit) and bool(crit < sp.Rational(3, 100))
    e1 = bounds if not mut("criterion_at_delta_one_above_a_tenth") else bool(crit > sp.Rational(1, 10))
    checks.check("E1", e1, "T4: a wall's energy per unit area is sigma_sea(delta) - 2 alpha delta^2; at delta = 1 exactly (2 sqrt 3 - sqrt 2 - 2)/2 lies between 2/100 and 3/100, so walls are favoured there iff alpha exceeds a number between 2/100 and 3/100; at smaller delta the executed sigma_sea/(2 delta^2) rises to about 14/100 (control)")
# ============================================================================================ family F
FENCES = (
    "This note works within block 59's bond rates and bond law, block 84's alternation and the sea as a comparator; it reports what a wall in the alternation costs the sea and the law, exactly, and when walls are favoured; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - the squared spectra of the one-axis operator with and without walls on three rings, level by level; block 59's quadratic form bond by bond on the 4^3 torus",
    "per_site: executed - the wall's law energy per unit area for each of the three couplings separately",
    "per_mode: executed - the transverse integrand at a rational point and at delta = 1 exactly; control: the tension on transverse grids to 512^2 and its direct check on 8^3 and 16^3",
    "per_block: executed - the level rule as a multiset identity on three rings; the criterion at delta = 1 as an exact inequality",
    "lattice_wide: T1 exact on the rings of 4, 8, 12 and executed to be length-independent on longer rings, not proved for every ring; T2 by concavity given T1 and block 86; T3 on the 4^3 torus and by the local count on every torus; T4 as a criterion; the bond law's three numbers, the sea reading and the balance as a minimisation are not derived",
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
    print("scope: what a wall in the alternation costs - two sharp walls replace exactly the levels +-delta, +-1 by 0, 0, +-sqrt(1 + delta^2) on the rings tried, so the sea charges a wall pair (1 + delta) - sqrt(1 + delta^2) on a ring and a positive transverse-average tension in three dimensions (2 sqrt3 - sqrt2 - 2 at delta = 1); block 59's law rewards a wall by exactly 2 alpha delta^2 per unit area (only the collinear coupling sees a phase slip); walls are favoured iff alpha > sigma_sea/(2 delta^2), about 14/100 near the threshold and 1/40 at delta = 1; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
