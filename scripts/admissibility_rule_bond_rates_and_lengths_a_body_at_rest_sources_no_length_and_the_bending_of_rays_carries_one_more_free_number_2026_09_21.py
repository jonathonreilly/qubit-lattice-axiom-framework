#!/usr/bin/env python3
"""Exact finite controls for supplied independent site and bond rates.
Fixed-state energy identities, a normalized local symbol, conditional ray accelerations
and a separate scalar weak-field cross-energy are tested, not a physical completion.
"""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import permutations, product
from math import isqrt
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "body_at_rest_has_hop_energy": "B",
    "parts_do_not_add_to_the_whole": "B",
    "bond_law_is_unique": "C",
    "anisotropic_modes_are_massless": "C",
    "locked_lengths_double_the_bending": "D",
    "bending_ignores_the_bond_rates": "D",
    "a_local_clause_sees_the_depth": "E",
    "cross_term_leaves_lengths_alone": "E",
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
AXES = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


class G:
    """A Gaussian rational re + i im."""

    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = F(re)
        self.im = F(im)

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


HALF_I = G(0, F(1, 2))
SIG = [
    [[G(0), G(1)], [G(1), G(0)]],
    [[G(0), G(0, -1)], [G(0, 1), G(0)]],
    [[G(1), G(0)], [G(0), G(-1)]],
]


def rank(rows):
    rows = [[F(c) for c in r] for r in rows]
    rk = 0
    for col in range(len(rows[0])):
        piv = next((i for i in range(rk, len(rows)) if rows[i][col] != 0), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        rows[rk] = [c / rows[rk][col] for c in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][col] != 0:
                fac = rows[i][col]
                rows[i] = [x - fac * y for x, y in zip(rows[i], rows[rk])]
        rk += 1
    return rk


# ------------------------------------------------------------------------------ the walk on a torus with bond rates and site rates
def torus(dims):
    sites = list(product(*[range(d) for d in dims]))
    bonds = [(x, tuple((x[i] + (1 if i == j else 0)) % dims[i] for i in range(3)), j) for x in sites for j in range(3) if dims[j] > 1]
    return sites, bonds


def hop_expectation(chi, idx, bond):
    """2 Re chi_y^dagger (i/2) sigma_j chi_x for the bond from x to y = x + e_j: the rate-independent hop energy per unit bond rate."""
    x, y, j = bond
    tot = G(0)
    for s in range(2):
        for s2 in range(2):
            tot = tot + chi[idx[(y, s2)]].conj() * SIG[j][s2][s] * HALF_I * chi[idx[(x, s)]]
    return 2 * tot.re


def site_expectation(chi, idx, x, matrix):
    tot = G(0)
    for s in range(2):
        for s2 in range(2):
            tot = tot + chi[idx[(x, s2)]].conj() * matrix[s2][s] * chi[idx[(x, s)]]
    return tot.re


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    dims = (3, 3, 4)
    sites, bonds = torus(dims)
    idx = {(x, s): 2 * i + s for i, x in enumerate(sites) for s in range(2)}
    n = 2 * len(sites)
    rate_c = {b: ONE + F((2 * b[0][0] + 3 * b[0][1] + 5 * b[0][2] + 7 * b[2]) % 9, 11) for b in bonds}
    rate_w = {x: ONE + F((3 * x[0] + 5 * x[1] + 7 * x[2]) % 11, 13) for x in sites}
    rest = F(2, 5)
    chi = [G(F((5 * a + 3) % 7 - 3, 4), F((3 * a + 1) % 5 - 2, 3)) for a in range(n)]
    t = {b: rate_c[b] * hop_expectation(chi, idx, b) for b in bonds}
    r = {x: rate_w[x] * rest * site_expectation(chi, idx, x, SIG[0]) for x in sites}
    total = sum(t.values(), ZERO) + sum(r.values(), ZERO)
    # <H> computed independently: build H chi and take the expectation
    hchi = [G(0)] * n
    for (x, y, j) in bonds:
        for s in range(2):
            for s2 in range(2):
                amp = SIG[j][s2][s] * HALF_I * rate_c[(x, y, j)]
                hchi[idx[(y, s2)]] = hchi[idx[(y, s2)]] + amp * chi[idx[(x, s)]]
                hchi[idx[(x, s)]] = hchi[idx[(x, s)]] + amp.conj() * chi[idx[(y, s2)]]
    for x in sites:
        for s in range(2):
            for s2 in range(2):
                hchi[idx[(x, s2)]] = hchi[idx[(x, s2)]] + SIG[0][s2][s] * (rate_w[x] * rest) * chi[idx[(x, s)]]
    energy = sum((chi[a].conj() * hchi[a] for a in range(n)), G(0))
    whole = energy.im == 0 and energy.re == total
    if mut("parts_do_not_add_to_the_whole"):
        whole = energy.re == total + ONE
    checks.check("B1", whole, f"T2: on a 3x3x4 torus with rational bond rates, site rates and amplitude, the hop energies t_b = d<H>/dlog c_b and the on-site energies r_x = d<H>/dlog w_x add up to <H> = {energy.re}: H has weight one in the rates taken together, and each rate is sourced by the energy it times")
    # a body at rest: real envelope, rest content (1, 1): no hop energy on any bond
    env = {x: ONE + F((2 * x[0] + x[1] + 4 * x[2]) % 5, 7) for x in sites}
    body = [G(0)] * n
    for x in sites:
        body[idx[(x, 0)]] = G(env[x])
        body[idx[(x, 1)]] = G(env[x])
    hops = [hop_expectation(body, idx, b) for b in bonds]
    at_rest = all(v == 0 for v in hops)
    if mut("body_at_rest_has_hop_energy"):
        at_rest = any(v != 0 for v in hops)
    # a walker with no rest energy moving along the third axis: plane wave exp(i pi z/2), content along +z
    powers = [G(1), G(0, 1), G(-1), G(0, -1)]
    wave = [G(0)] * n
    for x in sites:
        wave[idx[(x, 0)]] = powers[x[2]]
    along = sum((hop_expectation(wave, idx, b) for b in bonds if b[2] == 2), ZERO)
    across = [hop_expectation(wave, idx, b) for b in bonds if b[2] != 2]
    checks.check("B2", at_rest and along == len(sites) and all(v == 0 for v in across), "T2: the tested instantaneous real-envelope constant-spinor state has exactly zero hop energy on every one of the 108 bonds: by the ledger it sources site rates only, and no bond rate or length.  A walker with no rest energy moving along the third axis (wave vector pi/2) has all of its energy on that axis's bonds and none on the others: it sources the rates of the bonds it crosses")
    # product form: e_x = r_x + (1/2) sum of t_b over the six bonds at x
    phi = {x: ONE + F((3 * x[0] + 5 * x[1] + 7 * x[2]) % 11, 13) for x in sites}
    t2 = {b: phi[b[0]] * phi[b[1]] * hop_expectation(chi, idx, b) for b in bonds}
    ok = True
    hchi2 = [G(0)] * n
    for (x, y, j) in bonds:
        for s in range(2):
            for s2 in range(2):
                amp = SIG[j][s2][s] * HALF_I * (phi[x] * phi[y])
                hchi2[idx[(y, s2)]] = hchi2[idx[(y, s2)]] + amp * chi[idx[(x, s)]]
                hchi2[idx[(x, s)]] = hchi2[idx[(x, s)]] + amp.conj() * chi[idx[(y, s2)]]
    for x in sites:
        e_x = sum(((chi[idx[(x, s)]].conj() * hchi2[idx[(x, s)]]).re for s in range(2)), ZERO)
        shared = sum((v for b, v in t2.items() if b[0] == x or b[1] == x), ZERO) / 2
        ok = ok and e_x == shared
    checks.check("B3", ok, "T2: in block 54's product form c_b = sqrt(w_x w_y) the energy density of block 55 is half the hop energy of the six bonds at the site (plus the on-site energy): the product form makes every bond's energy slow the clocks at both its ends, in all directions alike")


# ============================================================================================ family C
def bond_neighbours():
    """The bonds nearest to the bond b0 from the origin along the third axis, sorted into orbits of the rotations that keep b0 as a set."""
    def unoriented(x, j):
        return (tuple(x), j)

    b0 = unoriented((0, 0, 0), 2)
    mid0 = (F(0), F(0), F(1, 2))
    cand = []
    for x in product(range(-2, 3), repeat=3):
        for j in range(3):
            mid = tuple(F(x[i]) + (F(1, 2) if i == j else 0) for i in range(3))
            d2 = sum(((mid[i] - mid0[i]) ** 2 for i in range(3)), ZERO)
            if 0 < d2 <= 1:
                cand.append((x, j, mid, d2))
    rots = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            parity = 1
            for i in range(3):
                for k in range(i + 1, 3):
                    if perm[i] > perm[k]:
                        parity = -parity
            if parity * signs[0] * signs[1] * signs[2] != 1:
                continue
            rots.append((perm, signs))

    def act(g, v):
        perm, signs = g
        return tuple(signs[i] * v[perm[i]] for i in range(3))

    # rotations about the midpoint of b0 that keep b0: those that map the axis e_3 to +-e_3
    keep = [g for g in rots if act(g, (0, 0, 1)) in ((0, 0, 1), (0, 0, -1))]
    orbits = []
    seen = set()
    for (x, j, mid, d2) in cand:
        if mid in seen:
            continue
        rel = tuple(mid[i] - mid0[i] for i in range(3))
        orb = set()
        for g in keep:
            img = act(g, rel)
            orb.add(tuple(img[i] + mid0[i] for i in range(3)))
        seen |= orb
        orbits.append((d2, len(orb)))
    return len(keep), sorted(orbits)


def family_c(checks: Checks) -> None:
    stabilizer, orbits = bond_neighbours()
    want = [(F(1, 2), 8), (ONE, 2), (ONE, 4)]
    family = len(orbits)
    if mut("bond_law_is_unique"):
        family = 1
    checks.check("C1", stabilizer == 8 and orbits == want and family == 3, f"T3: the bonds within one site of a bond's midpoint fall into {len(orbits)} classes under the {stabilizer} rotations that keep the bond: 8 perpendicular bonds touching it (squared distance 1/2), 2 collinear and 4 parallel (squared distance 1).  A covariant linear law for log c_b with the shift symmetry therefore has three free numbers (alpha, beta, delta) where block 53's law for site rates had none")
    # symbol at zero wave vector and along rational half-angles: M_jj = c_0 + 2 alpha cos k_j + 2 delta sum_(l != j) cos k_l, M_jl = 4 beta cos(k_j/2) cos(k_l/2)
    alpha, beta, delta = F(2), F(1, 3), F(1, 5)
    c0 = -2 * alpha - 8 * beta - 4 * delta
    m0 = [[(c0 + 2 * alpha + 4 * delta) if j == l else 4 * beta for l in range(3)] for j in range(3)]
    iso = [sum(m0[j][l] for l in range(3)) for j in range(3)]
    shear = [m0[j][0] - m0[j][1] for j in range(3)]                     # M applied to (1, -1, 0)
    mass = shear[0]
    massless_iso = all(v == 0 for v in iso)
    massive = shear == [mass, -mass, ZERO] and mass == -12 * beta
    if mut("anisotropic_modes_are_massless"):
        massive = mass == 0
    # the isotropic mode at a rational wave vector: cos(k/2) = 4/5, cos k = 7/25 on each axis
    ch, ck = F(4, 5), F(7, 25)
    iso_value = 3 * c0 + 3 * (2 * alpha * ck + 4 * delta * ck) + 6 * 4 * beta * ch * ch
    closed = -(6 * alpha + 12 * delta) * (1 - ck) - 24 * beta * (1 - ch * ch)
    # the isotropic vector is not an exact eigenvector at finite wave vector: M (1,1,1) at k = (k, 0, 0) with cos(k/2) = 4/5, cos k = 7/25
    row_along = c0 + 2 * alpha * ck + 4 * delta + 4 * beta * ch * 2                       # the bond direction along k
    row_across = c0 + 2 * alpha + 2 * delta * (ck + 1) + 4 * beta * (ch + 1)              # a direction across k
    drive = row_along - row_across                                                       # what pushes the anisotropic modes: of second order in k
    slaved = drive == -2 * (alpha - delta) * (1 - ck) - 4 * beta * (1 - ch) and drive != 0
    checks.check("C2", massless_iso and massive and iso_value == closed and slaved, f"T3: zero-momentum eigenvalues 0 and -12 beta={mass} twice; finite-wave-vector row sum and anisotropic drive checked; no global stability or decay theorem from this gap alone")
    # k=t*(1,2,3): extract the quadratic matrix coefficient from cosine expansions.
    direction=(F(1),F(2),F(3));norm=sum(v*v for v in direction)
    second=[[-alpha*direction[j]**2-delta*sum(direction[l]**2 for l in range(3) if l!=j) if j==k else -beta*(direction[j]**2+direction[k]**2)/2 for k in range(3)] for j in range(3)]
    acoustic=sum(sum(row) for row in second)/3
    checks.check("C3",acoustic==-(alpha+2*beta+2*delta)*norm/3 and acoustic!=-(alpha+2*beta+2*delta)*norm,"T3: normalized uniform-branch stiffness is (alpha+2 beta+2 delta)/3; unnormalized row summation misses the division by three")



# ============================================================================================ family D
def ray_accelerations(a, grad_a, c, grad_c, m, sines, cosines, energy):
    """Exact ray equations for E^2 = a^2 m^2 + c^2 sum sin^2 k_j with a(x), c(x): returns (v, dv/dt)."""
    s_val = a * a * m * m + c * c * sum(s * s for s in sines)
    assert energy * energy == s_val and energy > 0
    dk = [2 * c * c * sines[j] * cosines[j] for j in range(3)]
    dx = [2 * a * grad_a[l] * m * m + 2 * c * grad_c[l] * sum(s * s for s in sines) for l in range(3)]
    v = [dk[j] / (2 * energy) for j in range(3)]
    kdot = [-dx[l] / (2 * energy) for l in range(3)]
    acc = []
    for j in range(3):
        tot = ZERO
        for l in range(3):
            dvdx = (4 * c * grad_c[l] * sines[j] * cosines[j]) / (2 * energy) - dk[j] * dx[l] / (4 * energy ** 3)
            dvdk = ((2 * c * c * (cosines[j] ** 2 - sines[j] ** 2)) if j == l else ZERO) / (2 * energy) - dk[j] * dk[l] / (4 * energy ** 3)
            tot += dvdx * v[l] + dvdk * kdot[l]
        acc.append(tot)
    return v, acc


def family_d(checks: Checks) -> None:
    g = F(1, 20)
    ratios = {}
    for label, power in (("locked lengths, c = a", ONE), ("l = abar/a, c = a^2/abar", F(2)), ("bond rates that ignore the site rates", ZERO)):
        a, c = ONE, ONE                                                  # ambient values at the point; d log c = power x d log a
        grad_a = (ZERO, ZERO, g)
        grad_c = (ZERO, ZERO, power * g)
        _, slow = ray_accelerations(a, grad_a, c, grad_c, F(3, 4), (ZERO, ZERO, ZERO), (ONE, ONE, ONE), F(3, 4))
        _, ray = ray_accelerations(a, grad_a, c, grad_c, ZERO, (F(3, 5), ZERO, ZERO), (F(4, 5), ONE, ONE), F(3, 5))
        ratios[label] = (slow[2], ray[2])
    fall = -g
    want = {"locked lengths, c = a": (fall, fall), "l = abar/a, c = a^2/abar": (fall, 2 * fall), "bond rates that ignore the site rates": (fall, ZERO)}
    if mut("locked_lengths_double_the_bending"):
        want["locked lengths, c = a"] = (fall, 2 * fall)
    if mut("bending_ignores_the_bond_rates"):
        want["l = abar/a, c = a^2/abar"] = (fall, fall)
    checks.check("D1", ratios == want, "T4: for E^2 = a^2 m^2 + c^2 sum sin^2 k_j a slow body falls at -c^2 dlog a and a ray crossing the gradient bends at -c^2 dlog c, exactly on the lattice (the ray taken along an axis at sin k = 3/5): with locked lengths (c = a) the ray bends as the body falls; with l = abar/a it bends twice as much; with bond rates that ignore the site rates it does not bend at all.  The ratio applies to these local transverse components, at the same c and with nonzero parallel site-rate gradient")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    wx, wy, wbar, t = F(9, 4), F(25, 16), F(4), F(49, 9)
    def root(q):
        q = F(q)
        num, den = isqrt(q.numerator), isqrt(q.denominator)
        assert num * num == q.numerator and den * den == q.denominator
        return F(num, den)

    clauses = {
        "ratio of the two rates": lambda a, b, ref: root(a / b),
        "depth, no reference": lambda a, b, ref: 1 / root(a * b),
        "depth against the ambient rate": lambda a, b, ref: ref / root(a * b),
    }
    unchanged = {k: fn(t * wx, t * wy, t * wbar) == fn(wx, wy, wbar) for k, fn in clauses.items()}
    want = {"ratio of the two rates": True, "depth, no reference": False, "depth against the ambient rate": True}
    if mut("a_local_clause_sees_the_depth"):
        want["depth, no reference"] = True
    flat = clauses["ratio of the two rates"](wx, wx, wbar) == clauses["ratio of the two rates"](t * wx, t * wx, wbar) == 1
    checks.check("E1", unchanged == want and flat, "T5: a length is a pure number, so a clause for it must be unchanged when the unit of rate is changed (here by 49/9): a clause in the ratio of the two rates at the bond's ends is; a clause in their depth, l = 1/sqrt(w_x w_y), is not; l = wbar/sqrt(w_x w_y) is, but it needs the ambient rate — a reference to distant clocks, as block 57's front did.  This tested ratio clause gives l = 1 at uniform rates; a general invariant clause gives its constant G(1), independent of the common rate")
    # (b) a local LAW can tie them: static laws on a segment with held walls, S Lam lam + kappa Lam u = 0 (lam = log l, no direct source for a body at rest)
    n, stiff, kappa = 9, F(3), F(2)
    # u: the field of a body at rest at the middle site: Lam u = -q delta with u = 0 at the walls; solved by the explicit tent
    mid, q = 4, F(1, 5)
    u = [-(q / 2) * (mid - abs(z - mid)) * 1 for z in range(n)]
    lam_u = [2 * u[z] - u[z - 1] - u[z + 1] for z in range(1, n - 1)]
    tent_ok = all((lam_u[z - 1] == (-q if z == mid else ZERO)) for z in range(1, n - 1)) and u[0] == u[-1] == 0
    lam = [-(kappa / stiff) * v for v in u] if not mut("cross_term_leaves_lengths_alone") else [ZERO for _ in u]
    law_ok = all(stiff * (2 * lam[z] - lam[z - 1] - lam[z + 1]) + kappa * (2 * u[z] - u[z - 1] - u[z + 1]) == 0 for z in range(1, n - 1))
    ratio = 1 + kappa / stiff
    checks.check("E2", tent_ok and law_ok and ratio == F(5, 3), f"T5: a cross term between the differences of log l and of u in the field's energy gives, for a body at rest and held walls, log l = -(kappa/S) u exactly (segment of nine sites, kappa/S = 2/3): l = (wbar/w)^beta with beta free; the bending of a ray is then 1 + beta = {ratio} times the fall of a slow body; beta = 0 for the clauses of blocks 53 to 57, 1 for the comparator")


# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for local tick rates and for amplitudes timed by them, widened by a rate for every bond; it reports what such rates and the lengths they define can and cannot do; nothing is adopted and no gravitational claim is made.",
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
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Mach", "Eddington", "Soldner", "Dicke", "Riemann", "Regge", "Lame", "Hooke", "Abraham")
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
    nodes=list(ast.walk(ast.parse(src)))
    float_hits=[n for n in nodes if isinstance(n,ast.Constant) and isinstance(n.value,float)]
    float_hits += [n for n in nodes if isinstance(n,ast.Call) and ((isinstance(n.func,ast.Name) and n.func.id in ('float','N')) or (isinstance(n.func,ast.Attribute) and n.func.attr in ('evalf','N')))]
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
    "per_element: executed — hop energies on the 108 bonds and on-site energies on the 36 sites of a 3x3x4 torus for a rational amplitude, bond rates and site rates; a body at rest; a walker moving along one axis",
    "per_site: executed — block 55's energy density against half the hop energies of the six bonds at each site, in the product form",
    "per_mode: executed — the classes of bonds near a bond under the rotations that keep it; the law's matrix at zero wave vector and its isotropic mode at a rational wave vector",
    "per_block: executed — exact ray equations at rational points for three relations between bond rates and site rates; three clauses for a length under a change of the unit of rate",
    "lattice_wide: T1, T2 hold for every amplitude and all positive rates; T3 for linear covariant shift-symmetric laws reaching the bonds within one site of a bond's midpoint; T4 for rays of the stated energy function; T5(a) for every algebraic local clause l_b = G(w_x, w_y), T5(b) for the linear static laws with a cross term; that bonds have rates of their own, the law they obey and its three numbers, any reference to the ambient rate, and a rest energy are not derived",
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
    print("scope: fixed-state energy derivatives; instantaneous zero-hop state; three-coefficient bond symbol with normalized scalar stiffness divided by three; conditional local ray acceleration ratios; separate scalar linear cross-field model")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
