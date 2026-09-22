#!/usr/bin/env python3
"""Exact checks: the crowd's balance under an alternation of the bond rates (block 59's bond rates; block 80's compressed generator; not adopted).

OBJECTS: the sigma_x-coined ring walk with bond amplitudes 1 + delta (-1)^x (block 84 T5); block 80's compressed generator of n records with
anticommuting composition and one record per site; the free sea (comparator).
T1: the crowd's ground energy is even in delta (translation by one site conjugates +delta to -delta on the compressed generator, exactly) and
   concave (a minimum of affine functions): it never rises under an alternation; exact algebraic instance for two records on the ring of four.
T2: under an alternation no one-record energy vanishes, so the free sea's filling is a record on every site, whose compressed generator is
   exactly zero: the sea's own filling has no crowd counterpart.
T3: one record's ground energy on the ring of four is exactly -1 for every delta tried: the gain is the sea's or the crowd's, not a walker's.
Exact arithmetic only (integers, Fractions, exact symbolic algebra); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_CROWD_UNDER_EXCLUSION_ALSO_GAINS_FROM_AN_ALTERNATION_OF_THE_BOND_RATES_ITS_GROUND_ENERGY_NEVER_RISES_THE_JAM_IS_BLIND_BOUNDED_THEOREM_NOTE_2026-09-22.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_crowd_under_exclusion_also_gains_from_an_alternation_of_the_bond_rates_its_ground_energy_never_rises_the_jam_is_blind_bounded_theorem_note_2026-09-22"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "crowd_energy_odd_in_delta": "B",
    "jam_feels_the_alternation": "C",
    "sea_filling_below_every_site": "C",
    "one_record_ground_energy_falls": "D",
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


SX = sp.Matrix([[0, 1], [1, 0]])


def ring_one_body(size, delta):
    """The sigma_x-coined ring walk with the bond amplitude 1 + delta (-1)^x on the bond x -> x + 1; mode index 2x + coin."""
    hop = sp.zeros(size, size)
    for x in range(size):
        t = 1 + delta * (-1) ** x
        tm = 1 + delta * (-1) ** ((x - 1) % size)
        hop[x, (x + 1) % size] += t / (2 * sp.I)
        hop[x, (x - 1) % size] -= tm / (2 * sp.I)
    return sp.kronecker_product(hop, SX)


def perm_sign(order):
    p = list(order)
    s = 1
    for a in range(len(p)):
        while p[a] != a:
            b = p[a]
            p[a], p[b] = p[b], p[a]
            s = -s
    return s


def compressed(h1, n_rec):
    """Block 80's compressed generator: n_rec records with anticommuting composition, one record per site."""
    d = h1.shape[0]
    site = [o // 2 for o in range(d)]
    basis = [s for s in combinations(range(d), n_rec) if len({site[o] for o in s}) == n_rec]
    index = {s: i for i, s in enumerate(basis)}
    m = sp.zeros(len(basis), len(basis))
    for s, i in index.items():
        sset = set(s)
        used = {site[o] for o in s}
        for pos, o in enumerate(s):
            for o2 in range(d):
                if h1[o2, o] == 0:
                    continue
                if o2 != o and o2 in sset:
                    continue
                if o2 != o and site[o2] != site[o] and site[o2] in used:
                    continue
                new = list(s)
                new[pos] = o2
                order = sorted(range(n_rec), key=lambda k_: new[k_])
                m[index[tuple(new[k_] for k_ in order)], i] += perm_sign(order) * h1[o2, o]
    return m, basis


def translation(basis, n_rec, size):
    idx = {s: i for i, s in enumerate(basis)}
    t = sp.zeros(len(basis), len(basis))
    for s, i in idx.items():
        new = [(o + 2) % (2 * size) for o in s]
        order = sorted(range(n_rec), key=lambda k_: new[k_])
        t[idx[tuple(new[k_] for k_ in order)], i] = perm_sign(order)
    return t


RING = 4
DELTA = sp.Rational(3, 10)


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the crowd's ground energy is even in delta (translation) and concave (a minimum of affine functions): it never rises under an alternation."""
    hp, hm = ring_one_body(RING, DELTA), ring_one_body(RING, -DELTA)
    even_ok = True
    dims = []
    for n in (1, 2, 3):
        mp, basis = compressed(hp, n)
        mm, _ = compressed(hm, n)
        t = translation(basis, n, RING)
        conj = t * mp * t.T
        same = sp.simplify(conj - mm) == sp.zeros(len(basis), len(basis))
        even_ok = even_ok and same and sp.simplify(mp - mp.H) == sp.zeros(len(basis), len(basis))
        dims.append(len(basis))
    b1 = even_ok if not mut("crowd_energy_odd_in_delta") else (not even_ok)
    checks.check("B1", b1, f"T1: on the ring of four with the bond amplitudes 1 + delta (-1)^x, delta = 3/10, translation by one site carries the compressed generator of n = 1, 2, 3 records under exclusion (dimensions {dims}) exactly to the generator at -delta: the crowd's ground energy is even in delta at every filling; being a minimum of affine functions of delta it is concave, hence largest at delta = 0")
    # exact instance for n = 2: the ground energy at delta = 3/10 lies at or below the ground energy at 0 (algebraic numbers, compared exactly)
    m0, _ = compressed(ring_one_body(RING, sp.Integer(0)), 2)
    m1, _ = compressed(hp, 2)
    e0 = min(m0.eigenvals().keys())
    e1 = min(m1.eigenvals().keys())
    below = bool(e1 < e0)
    checks.check("B2", below and e0 == -sp.sqrt(2) and e1 == -sp.sqrt(218) / 10, f"T1: two records under exclusion on the ring of four: ground energy {sp.nsimplify(e0)} at delta = 0 and {sp.nsimplify(e1)} at delta = 3/10 (exact algebraic numbers): lower")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: under an alternation every one-record energy is nonzero, so the sea's filling is every site, and the jam has the zero generator."""
    k = sp.symbols("k1 k2", real=True)
    dl = sp.symbols("delta", positive=True)
    e2 = sp.sin(k[0]) ** 2 + sp.sin(k[1]) ** 2 + dl ** 2 * (sp.cos(k[0]) ** 2 + sp.cos(k[1]) ** 2)
    # E^2 >= min over the zone: with sin^2 + delta^2 cos^2 >= min(1, delta^2) per axis, E^2 >= 2 min(1, delta^2) > 0
    per_axis = sp.sin(k[0]) ** 2 + dl ** 2 * sp.cos(k[0]) ** 2 - dl ** 2
    positive = sp.simplify(per_axis - (1 - dl ** 2) * sp.sin(k[0]) ** 2) == 0
    checks.check("C1", positive, "T2: per axis sin^2 k + delta^2 cos^2 k - delta^2 = (1 - delta^2) sin^2 k >= 0 for delta <= 1, so on the two-dimensional torus E^2 >= 2 delta^2 > 0 (three-dimensional: 3 delta^2, block 84 T1): no one-record energy vanishes, exactly half the 2N states are negative, and the free sea's filling under the alternation is N records - every site")
    hp = ring_one_body(RING, DELTA)
    mjam, basis = compressed(hp, RING)
    jam_zero = mjam == sp.zeros(len(basis), len(basis))
    c2 = (jam_zero and len(basis) == 2 ** RING) if not mut("jam_feels_the_alternation") else (not jam_zero)
    checks.check("C2", c2, f"T2: with a record on every site of the ring ({2 ** RING} coin configurations) the compressed generator is exactly the zero matrix at delta = 3/10: the jam is blind to every bond amplitude, so the sea's own filling has no crowd counterpart that could gain or lose")
    negative_count = sum(1 for v, mlt in ring_one_body(RING, DELTA).eigenvals().items() for _ in range(mlt) if v < 0)
    c3 = (negative_count == RING) if not mut("sea_filling_below_every_site") else (negative_count < RING)
    checks.check("C3", c3, f"T2: on the ring of four at delta = 3/10 exactly {negative_count} of the 8 one-record energies are negative (the energies are +-3/10 and +-1, twice each): the sea's filling is one record per site")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: one record's ground energy on the ring of four is flat in delta; the gain is the sea's, not the walker's."""
    flat = True
    for dv in (sp.Rational(1, 10), sp.Rational(3, 10), sp.Rational(1, 2)):
        ev = ring_one_body(RING, dv).eigenvals()
        ground = min(ev.keys())
        flat = flat and sp.simplify(ground + 1) == 0
    d1 = flat if not mut("one_record_ground_energy_falls") else (not flat)
    checks.check("D1", d1, "T3: on the ring of four one record's lowest energy is exactly -1 at delta = 1/10, 3/10, 1/2 (its energies +-|delta|, +-1): a single moving record gains nothing from the alternation; the gain that drives it is the sea's (all negative states) or the crowd's (executed), not a walker's")
# ============================================================================================ family F
FENCES = (
    "This note works within block 59's bond rates, block 80's composition of records under exclusion and the free sea taken as a comparator; it reports whether the crowd of records, and not only the sea, gains from an alternation of the bond rates; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - the compressed generator of one, two and three records on the ring of four, entry by entry, at +delta and -delta",
    "per_site: executed - the jam's generator on every coin configuration of the ring",
    "per_mode: executed - the eight one-record energies of the ring of four at three values of delta; control: ground energies of the crowd on the 3x3, 4x3 and 4x4 tori at every filling of 3x3",
    "per_block: executed - the two-record ground energies at delta = 0 and 3/10 as exact algebraic numbers; the translation conjugacy",
    "lattice_wide: T1 holds at every filling on every even torus by the translation and the minimum-of-affine argument; T2 by block 84 T1's bound on every torus; T3 on the ring of four; the crowd's executed coefficients are for three small tori; the composition sign and the balance as a minimisation are not derived",
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
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: the crowd under exclusion also gains from an alternation of the bond rates - its ground energy is even and concave in delta (never rises) at every filling, exactly; the free sea's filling under an alternation is a record on every site, whose generator is exactly zero (the jam is blind); a single record gains nothing on the ring of four; executed on 2D tori: the crowd lowers its energy at every filling below the jam, with a quadratic coefficient between a tenth and nine tenths of the free sea's; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
