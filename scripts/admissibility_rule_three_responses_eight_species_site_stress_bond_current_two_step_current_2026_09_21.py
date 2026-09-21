#!/usr/bin/env python3
"""Exact checks: three responses, eight species (supplied clauses on Z^3; not adopted).

OBJECTS (supplied by blocks 54, 62, 63, 69, 70, 72): the walk's three responses to a deformation of lengths - the SITE STRESS of block 62's
nearest-neighbour frame, Theta_a^j = Re psi^dagger sigma_a S_j psi; the BOND CURRENT of the relabelling of reach two, J_a^j (block 63); the bond
current of the relabelling of reach three, K_a^j (block 69) - and block 70's exchange maps V_n. Block 72: per unit of energy density the force
density of reach three is the same for every species, and div K[phi psi] = -fP exactly on stationary states.
T1 (the table, exact, every state): Theta_a^j[V_n psi] = s_n D_a D_j Theta_a^j[psi];  J_a^j[V_n psi] = s_n D_j J_a^j[psi];  K_a^j[V_n psi] = s_n K_a^j[psi].
T2 (leading order, smooth envelopes): for the first species the three responses agree; hence for species n, Theta = D_a D_j K and J = D_j K.
T3 (the ledger's requirement by species and coupling): the frame's response differs from the species' own stress in the components with exactly
   one reflected index: the requirement is met under the frame iff sum over {a: D_a != D_j} of d_a K_a^j = 0 for each j; species (000) and (111)
   always meet it; under reach two only (000) does in general; under reach three all eight.
Exact arithmetic only (integers, Fractions, Gaussian rationals, exact symbolic algebra); the runner scans its own source for floating-point literals.
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
    "docs/ADMISSIBILITY_RULE_THREE_RESPONSES_EIGHT_SPECIES_THE_FRAMES_SITE_STRESS_HAS_THE_WRONG_SIGN_IN_SHEAR_FOR_SIX_SPECIES_ONLY_THE_TWO_STEP_CURRENT_SERVES_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_three_responses_eight_species_the_frames_site_stress_has_the_wrong_sign_in_shear_for_six_species_only_the_two_step_current_serves_all_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "site_stress_is_the_same_for_all_species": "B",
    "two_step_current_carries_a_reflection_sign": "B",
    "frame_serves_all_eight_species": "C",
    "shear_remainder_has_no_factor_two": "C",
    "site_stress_and_bond_currents_differ_at_leading_order": "D",
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


# ============================================================================================ machinery on a torus of any size
EPS = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
MINUS_I = G(0, -1)
I_UNIT = G(0, 1)


class Torus:
    def __init__(self, dims):
        self.dims = dims
        self.sites = list(product(*(range(d) for d in dims)))

    def sh(self, x, a, step=1):
        return tuple((x[i] + (step if i == a else 0)) % self.dims[i] for i in range(3))

    def up(self, f, a):
        return {x: f[self.sh(x, a, 1)] for x in self.sites}

    def dn(self, f, a):
        return {x: f[self.sh(x, a, -1)] for x in self.sites}

    def s_op(self, f, j):
        return {x: tuple((f[self.sh(x, j, 1)][c] - f[self.sh(x, j, -1)][c]) * MINUS_HALF_I for c in range(2)) for x in self.sites}

    def sg(self, a, f):
        return {x: mat_vec(SIG[a], f[x]) for x in self.sites}

    def add(self, f, g, fac=1):
        return {x: tuple(f[x][c] + g[x][c] * fac for c in range(2)) for x in self.sites}

    def scale(self, f, fac):
        return {x: tuple(f[x][c] * fac for c in range(2)) for x in self.sites}

    def times(self, w, f):
        """A real site function times a spinor field."""
        return {x: tuple(f[x][c] * w[x] for c in range(2)) for x in self.sites}

    def ham(self, f):
        out = {x: (G(0), G(0)) for x in self.sites}
        for a in range(3):
            out = self.add(out, self.sg(a, self.s_op(f, a)))
        return out

    def redot(self, f, g):
        """Re f^dagger(x) g(x) at every site."""
        return {x: (f[x][0].conj() * g[x][0] + f[x][1].conj() * g[x][1]).re for x in self.sites}

    def state(self, seed):
        return {x: (G(F((seed * 7 + 3 * x[0] + x[1] * x[2] + x[0] * x[0]) % 5 - 2, 3), F((seed + x[0] * x[2] + 2 * x[1] + 5 * x[2]) % 7 - 3, 4)),
                    G(F((seed * 3 + x[0] * x[1] + 2 * x[2] + x[1] * x[1]) % 7 - 3, 5), F((seed * 5 + x[0] + 3 * x[1] + x[2] * x[2]) % 3 - 1, 2))) for x in self.sites}

    def theta(self, psi, a, j):
        return self.redot(psi, self.sg(a, self.s_op(psi, j)))

    def current(self, psi, a, j):
        """J_a^j on the bond from x to x + e_a, stored at x."""
        sj = self.s_op(psi, j)
        first = self.redot(self.up(psi, a), self.sg(a, sj))
        second = self.redot(self.up(sj, a), self.sg(a, psi))
        return {x: (first[x] + second[x]) / 2 for x in self.sites}


def stationary_state(tor: Torus):
    """On a 4x4x4 torus: plane waves with one wave-vector component pi/2 and the coin along that axis have H psi = psi exactly (Gaussian rationals)."""
    spinors = {0: (G(1), G(1)), 1: (G(1), G(0, 1)), 2: (G(1), G(0))}
    weights = {0: G(F(2, 3), F(1, 5)), 1: G(F(-1, 2), F(3, 4)), 2: G(F(5, 7), F(-1, 3))}
    powers = [G(1), G(0, 1), G(-1), G(0, -1)]
    psi = {x: (G(0), G(0)) for x in tor.sites}
    for axis in range(3):
        for x in tor.sites:
            ph = powers[x[axis] % 4] * weights[axis]
            psi[x] = tuple(psi[x][c] + spinors[axis][c] * ph for c in range(2))
    return psi


QUARTER_OVER_I = G(0, F(-1, 4))                                 # 1/(4i)


def p_op(tor: Torus, f, j):
    """(P_j f)(x) = (f(x + 2 e_j) - f(x - 2 e_j))/(4i)."""
    return {x: tuple((f[tor.sh(x, j, 2)][c] - f[tor.sh(x, j, -2)][c]) * QUARTER_OVER_I for c in range(2)) for x in tor.sites}


def current_p(tor: Torus, chi, a, j):
    pj = p_op(tor, chi, j)
    first = tor.redot(tor.up(chi, a), tor.sg(a, pj))
    second = tor.redot(tor.up(pj, a), tor.sg(a, chi))
    return {x: (first[x] + second[x]) / 2 for x in tor.sites}


SPECIES = list(product((0, 1), repeat=3))


def species_data(n):
    d = [(-1) ** n[a] for a in range(3)]
    s = d[0] * d[1] * d[2]
    rho = [s * d[a] for a in range(3)]
    return d, s, rho


def exchange(tor: Torus, n, f):
    """V_n f: the site sign (-1)^{n.x} and the coin's half turn about the axis that rho_n keeps (none for rho_n = 1)."""
    d, s, rho = species_data(n)
    kept = [a for a in range(3) if rho[a] == 1]
    out = {}
    for x in tor.sites:
        sign = (-1) ** sum(n[a] * x[a] for a in range(3))
        v = f[x] if len(kept) == 3 else mat_vec(SIG[kept[0]], f[x])
        out[x] = tuple(v[c] * sign for c in range(2))
    return out


def same(tor, f, g, fac=1):
    return all(f[x][c] == g[x][c] * fac for x in tor.sites for c in range(2))



# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    tor = Torus((6, 6, 6))
    psi = tor.state(2)
    base = {(a, j): (tor.theta(psi, a, j), tor.current(psi, a, j), current_p(tor, psi, a, j)) for a in range(3) for j in range(3)}
    site_ok = True
    bond_ok = True
    two_step_ok = True
    for n in SPECIES:
        d, s, rho = species_data(n)
        vpsi = exchange(tor, n, psi)
        for a in range(3):
            for j in range(3):
                th, cj, ck = tor.theta(vpsi, a, j), tor.current(vpsi, a, j), current_p(tor, vpsi, a, j)
                sign_site = s * d[a] * d[j] if not mut("site_stress_is_the_same_for_all_species") else s
                sign_two_step = s if not mut("two_step_current_carries_a_reflection_sign") else s * d[j]
                site_ok = site_ok and all(th[x] == sign_site * base[(a, j)][0][x] for x in tor.sites)
                bond_ok = bond_ok and all(cj[x] == s * d[j] * base[(a, j)][1][x] for x in tor.sites)
                two_step_ok = two_step_ok and all(ck[x] == sign_two_step * base[(a, j)][2][x] for x in tor.sites)
    alive = all(any(base[key][i][x] != 0 for x in tor.sites) for key in base for i in range(3))
    checks.check("B1", site_ok and bond_ok and alive, "T1: on a 6x6x6 torus, for a rational state, all eight species and all nine components, at all 216 sites: the frame's site stress Theta_a^j of V_n psi is det(D_n) D_a D_j times that of psi, and the reach-two bond current J_a^j is det(D_n) D_j times that of psi: per unit of energy density (which picks up det(D_n)) the site stress has the opposite sign in the components with exactly one reflected index, the reach-two current in the components with a reflected momentum index")
    checks.check("B2", two_step_ok and alive, "T1: the reach-three bond current K_a^j of V_n psi is det(D_n) times that of psi in all nine components at all 216 sites, all eight species: per unit of energy density it is the same for every species")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    serves_site = [n for n in SPECIES if all(species_data(n)[0][a] * species_data(n)[0][j] == 1 for a in range(3) for j in range(3))]
    serves_bond = [n for n in SPECIES if all(species_data(n)[0][j] == 1 for j in range(3))]
    count_site = 2 if not mut("frame_serves_all_eight_species") else 8
    counts = len(serves_site) == count_site and set(serves_site) == ({(0, 0, 0), (1, 1, 1)} if count_site == 2 else set(SPECIES)) and serves_bond == [(0, 0, 0)]
    kdiv = sp.Matrix(3, 3, lambda a, j: sp.Symbol(f"dK{a}{j}"))                                 # d_a K_a^j, the nine terms of the three divergences
    factor = 2 if not mut("shear_remainder_has_no_factor_two") else 1
    remainders = True
    for n in SPECIES:
        d = species_data(n)[0]
        for j in range(3):
            frame_div = sum(d[a] * d[j] * kdiv[a, j] for a in range(3))
            own_div = sum(kdiv[a, j] for a in range(3))
            shear = sum(kdiv[a, j] for a in range(3) if d[a] != d[j])
            remainders = remainders and sp.expand(own_div - frame_div - factor * shear) == 0
            remainders = remainders and sp.expand(own_div - d[j] * own_div - (2 if d[j] == -1 else 0) * own_div) == 0
    checks.check("C1", counts and remainders, "T3: the site stress agrees with the species' own stress in all nine components for two species, (000) and (111); the reach-two current for one, (000); the reach-three current for all eight; for species n and each j the frame's divergence falls short of the species' own by exactly twice the sum of d_a K_a^j over the axes a with D_a != D_j (the shear between a reflected and an unreflected axis), and the reach-two divergence by twice the whole when D_j = -1")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    xs = sp.symbols("x1 x2 x3", real=True)
    h = sp.symbols("h", positive=True)
    comps = [sp.Function(f"u{c}", real=True)(*xs) + sp.I * sp.Function(f"v{c}", real=True)(*xs) for c in range(2)]
    pauli = ([[0, 1], [1, 0]], [[0, -sp.I], [sp.I, 0]], [[1, 0], [0, -1]])

    def shifted(f, axis, steps):
        return f + steps * h * sp.diff(f, xs[axis]) + (steps * h) ** 2 * sp.diff(f, xs[axis], 2) / 2

    conj = lambda f: f.subs(sp.I, -sp.I)
    real = lambda f: sp.expand((f + conj(f)) / 2)
    lead = lambda f: sp.expand(f).coeff(h, 1)
    agree = True
    nonzero = False
    for a in range(3):
        for j in range(3):
            s_psi = [(shifted(c, j, 1) - shifted(c, j, -1)) / (2 * sp.I) for c in comps]
            p_psi = [(shifted(c, j, 2) - shifted(c, j, -2)) / (4 * sp.I) for c in comps]
            sandwich = lambda left, right: sum(conj(left[r]) * pauli[a][r][c] * right[c] for r in range(2) for c in range(2))
            site = real(sandwich(comps, s_psi))
            up = lambda vec: [shifted(c, a, 1) for c in vec]
            bond2 = real((sandwich(up(comps), s_psi) + sandwich(up(s_psi), comps)) / 2)
            bond3 = real((sandwich(up(comps), p_psi) + sandwich(up(p_psi), comps)) / 2)
            target = real(sandwich(comps, [-sp.I * sp.diff(c, xs[j]) for c in comps]))
            same = sp.simplify(lead(site) - target) == 0 and sp.simplify(lead(bond2) - target) == 0 and sp.simplify(lead(bond3) - target) == 0
            if mut("site_stress_and_bond_currents_differ_at_leading_order"):
                same = sp.simplify(lead(site) - lead(bond3)) != 0
            agree = agree and same and sp.expand(site).coeff(h, 0) == 0
            nonzero = nonzero or sp.simplify(target) != 0
    checks.check("D1", agree and nonzero, "T2: for a smooth two-component amplitude in three dimensions (exact symbolic expansion in the lattice spacing h), the site stress, the reach-two bond current and the reach-three bond current all begin at order h with the same coefficient, Re psi^dagger sigma_a (-i d_j psi), in all nine components: for the first species the three responses agree at leading order, so for species n the site stress is D_a D_j times, and the reach-two current D_j times, the species' own stress")
# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for amplitudes on the lattice with the qubit as their coin and for three supplied couplings of lengths to them; it reports how the three responses of the walk behave under the maps that exchange its species, and what follows for the requirement a ledger places on its content; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed — each of the nine components of the three responses for V_n psi against psi, all eight species",
    "per_site: executed — those comparisons as equalities at all 216 sites of a 6x6x6 torus",
    "per_mode: executed — the leading order in the lattice spacing of the three responses for a smooth two-component amplitude in three dimensions, all nine components (exact symbolic expansion)",
    "per_block: executed — the species served by each response in all nine components (two, one, eight); the shortfall of each divergence as twice a sum of named terms, all eight species and j = 1, 2, 3",
    "lattice_wide: T1 is an identity for every state on every torus with even sides (at least six for the two-step momentum) and on the infinite lattice; T2 is the leading order for smooth envelopes; T3 combines them with block 72 T1 and T3 (restated); which coupling is supplied and which species are present are not decided",
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
    print("scope: three responses, eight species — under the exchange maps the site stress of the frame picks up D_a D_j, the reach-two current D_j, the reach-three current nothing (each times the sense of the species, as the energy density does); at leading order the three agree for the first species; so the frame sources six of the eight species with the wrong sign in the shear between a reflected and an unreflected axis, reach two sources seven with the wrong sign along a reflected axis, and only the two-step current serves all eight")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
