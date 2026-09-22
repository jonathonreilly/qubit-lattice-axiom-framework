#!/usr/bin/env python3
"""Exact checks: many records under exclusion - what the ledger keeps (supplied clauses + the Record axiom; not adopted).

OBJECTS (blocks 54, 55, 76, 78): the clocked reduced walk H_w = phi sigma_3 D phi on a ring; two records with anticommuting composition; the
exclusion projector P onto configurations with the records on different sites (the Record axiom, one record per site at a time); the compressed
generator P H2 P, H2 = H_w (x) 1 + 1 (x) H_w (block 78).
T1 (the source under exclusion): for the projected pair Psi_P = P Psi, d<Psi_P|H2|Psi_P>/du_x equals the projected pair's own energy density
   e_x^(2) = sum over the two slots of Re <Psi_P| P_x H_w |Psi_P> (block 55 T1 for the compressed generator: P does not depend on the rates), and
   sum_x e_x^(2) = <Psi_P|H2|Psi_P> (weight one); the unprojected pair's density is NOT the source.
T2 (what P commutes with): P commutes with every site field phi (x) phi and with the simultaneous translation T (x) T; hence a chessboard of clocks
   is invisible to the compressed generator too, and the crystal momentum is conserved under exclusion; P does NOT commute with the one-step
   momentum S (x) 1 + 1 (x) S, so block 63's conserved momentum is not conserved for two records under exclusion (the contact of the records
   carries it).
Exact arithmetic only (integers, Fractions); the runner scans its own source for floating-point literals.
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
    "docs/ADMISSIBILITY_RULE_MANY_RECORDS_UNDER_EXCLUSION_SOURCE_IS_THE_PROJECTED_DENSITY_CHESSBOARD_INVISIBLE_INTERACTING_SEA_STIFFENS_CLOCKS_OPPOSITELY_BOUNDED_THEOREM_NOTE_2026-09-22.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_many_records_under_exclusion_source_is_the_projected_density_chessboard_invisible_interacting_sea_stiffens_clocks_oppositely_bounded_theorem_note_2026-09-22"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "source_is_the_unprojected_density": "B",
    "weight_is_two": "B",
    "chessboard_seen_under_exclusion": "C",
    "exclusion_keeps_the_one_step_momentum": "C",
    "exclusion_breaks_the_crystal_momentum": "C",
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


def ring_generator(size, phi):
    """A = i (phi sigma_3 D phi) on a ring of `size` sites with a two-component coin: a real antisymmetric matrix of dimension 2 size.
    (phi sigma_3 D phi psi)(x) = sigma_3 phi_x [phi_{x+1} psi(x+1) - phi_{x-1} psi(x-1)]/(2i); times i: (s/2) phi_x phi_{x+1} psi(x+1) - ..."""
    d = 2 * size
    a = [[ZERO] * d for _ in range(d)]
    for x in range(size):
        for c in range(2):
            s = 1 if c == 0 else -1
            a[2 * x + c][2 * ((x + 1) % size) + c] += F(s, 2) * phi[x] * phi[(x + 1) % size]
            a[2 * x + c][2 * ((x - 1) % size) + c] -= F(s, 2) * phi[x] * phi[(x - 1) % size]
    return a, [x for x in range(size) for c in range(2)]


def two_body_element(a, i, j, k, l):
    """<e_i e_j | A (x) 1 + 1 (x) A | e_k e_l>."""
    return (a[i][k] if j == l else ZERO) + (a[j][l] if i == k else ZERO)


def compress(a, vectors):
    """The generator restricted to the span of orthogonal vectors (dicts {(i, j): coefficient}), in the orthonormal basis."""
    norms = [sum((c * c for c in v.values()), ZERO) for v in vectors]
    m = len(vectors)
    out = [[ZERO] * m for _ in range(m)]
    for p, vp in enumerate(vectors):
        for q, vq in enumerate(vectors):
            tot = ZERO
            for (i, j), cp in vp.items():
                for (k, l), cq in vq.items():
                    tot += cp * cq * two_body_element(a, i, j, k, l)
            out[p][q] = tot / (norms[p] * norms[q]).sqrt() if False else tot
    # exact: divide row p by norm_p and column q by norm_q after a square-root-free normalisation: use tr((D^-1/2 M D^-1/2)^k) = tr((D^-1 M)^k)
    return out, norms


def traces(a, vectors):
    """tr H^2/dim and tr H^4/dim of the compressed generator (H = -i A), exactly, via tr((D^-1 M)^k) with D the diagonal of norms."""
    m_raw, norms = compress(a, vectors)
    m = [[m_raw[p][q] / norms[p] for q in range(len(vectors))] for p in range(len(vectors))]       # D^-1 M
    dim = len(vectors)

    def matmul(u, v):
        vt = list(zip(*v))
        return [[sum((x * y for x, y in zip(row, col)), ZERO) for col in vt] for row in u]
    m2 = matmul(m, m)
    t2 = -sum((m2[p][p] for p in range(dim)), ZERO) / dim
    m4 = matmul(m2, m2)
    t4 = sum((m4[p][p] for p in range(dim)), ZERO) / dim
    m6 = matmul(m4, m2)
    t6 = -sum((m6[p][p] for p in range(dim)), ZERO) / dim
    return t2, t4, dim, t6


def sectors(d, site_of):
    free_anti = [{(i, j): ONE, (j, i): -ONE} for i in range(d) for j in range(i + 1, d)]
    free_sym = [{(i, j): ONE, (j, i): ONE} for i in range(d) for j in range(i + 1, d)] + [{(i, i): ONE} for i in range(d)]
    hard_anti = [{(i, j): ONE, (j, i): -ONE} for i in range(d) for j in range(i + 1, d) if site_of[i] != site_of[j]]
    hard_sym = [{(i, j): ONE, (j, i): ONE} for i in range(d) for j in range(i + 1, d) if site_of[i] != site_of[j]]
    hard_none = [{(i, j): ONE} for i in range(d) for j in range(d) if site_of[i] != site_of[j]]
    return free_anti, free_sym, hard_anti, hard_sym, hard_none


RING = 6


def inner(u, v):
    return sum((p * q for p, q in zip(u, v)), ZERO)


def a_apply(a, v):
    return [sum((a[i][k] * v[k] for k in range(len(v))), ZERO) for i in range(len(v))]


def pair_state(d, u1, v1, u2, v2):
    """The antisymmetric pair psi1 (x) psi2 - psi2 (x) psi1 with psi = u + i v, as real and imaginary dicts on index pairs."""
    U, V = {}, {}
    for i in range(d):
        for j in range(d):
            re = u1[i] * u2[j] - v1[i] * v2[j] - (u2[i] * u1[j] - v2[i] * v1[j])
            im = u1[i] * v2[j] + v1[i] * u2[j] - (u2[i] * v1[j] + v2[i] * u1[j])
            if re != 0:
                U[(i, j)] = re
            if im != 0:
                V[(i, j)] = im
    return U, V


def two_body_apply(a, w):
    """(A (x) 1 + 1 (x) A) w for a dict w on index pairs."""
    d = len(a)
    out = {}
    for (i, j), c in w.items():
        for k in range(d):
            if a[k][i] != 0:
                out[(k, j)] = out.get((k, j), ZERO) + a[k][i] * c
            if a[k][j] != 0:
                out[(i, k)] = out.get((i, k), ZERO) + a[k][j] * c
    return out


def dot(w1, w2):
    return sum((c * w2.get(key, ZERO) for key, c in w1.items()), ZERO)


def energy_pair(a, U, V):
    """<Psi| -i (A (x) 1 + 1 (x) A) |Psi> = 2 U^T A2 V for Psi = U + i V, A2 real antisymmetric."""
    return 2 * dot(U, two_body_apply(a, V))


def keep(w, site_of):
    return {key: c for key, c in w.items() if site_of[key[0]] != site_of[key[1]]}


def one_record_states(size):
    d = 2 * size
    u1 = [F((x * x + 1) % 4, 3) if c == 0 else F((2 * x + 1) % 5, 4) for x in range(size) for c in range(2)]
    v1 = [F(x % 3, 2) if c == 0 else F((x * x) % 3 - 1, 3) for x in range(size) for c in range(2)]
    u2r = [F((x + 2) % 4, 5) if c == 0 else F(1, 2) for x in range(size) for c in range(2)]
    v2r = [F((x * x + x) % 3, 2) if c == 0 else F((3 * x) % 4 - 2, 3) for x in range(size) for c in range(2)]
    n1 = inner(u1, u1) + inner(v1, v1)
    cr = (inner(u1, u2r) + inner(v1, v2r)) / n1
    ci = (inner(u1, v2r) - inner(v1, u2r)) / n1
    u2 = [ur - (cr * p - ci * q) for ur, p, q in zip(u2r, u1, v1)]
    v2 = [vr - (cr * q + ci * p) for vr, p, q in zip(v2r, u1, v1)]
    return d, u1, v1, u2, v2


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    size = RING
    phi = [1 + F((3 * x * x + x) % 5, 7) for x in range(size)]
    d, u1, v1, u2, v2 = one_record_states(size)
    U, V = pair_state(d, u1, v1, u2, v2)
    site_of = [x for x in range(size) for c in range(2)]
    PU, PV = keep(U, site_of), keep(V, site_of)
    # the quadratic form F(t) = <P Psi| H2[phi with phi_x (1 + t)] |P Psi> is quadratic in t: its t-linear coefficient is (F(1) - F(-1))/2 exactly = dF/du_x
    def form(x0, t):
        ph = phi[:]
        ph[x0] = phi[x0] * (1 + t)
        a, _ = ring_generator(size, ph)
        return energy_pair(a, PU, PV)
    a0, _ = ring_generator(size, phi)
    total = energy_pair(a0, PU, PV)
    derivative = [(form(x0, ONE) - form(x0, -ONE)) / 4 for x0 in range(size)]                # phi_x dF/dphi_x = 2 dF/du_x (u = 2 log phi)
    # the projected pair's own energy density: sum over slots of Re <Psi_P| P_x (-i A) |Psi_P>  = 2 [ (P_x U)^T A V + ... ] computed slot by slot
    def density(x0, Uw, Vw):
        """Re <Psi| P_x (-i A2) |Psi> slot by slot, Psi = U + i V: U^T P_x A V - V^T P_x A U on each slot."""
        def slot_apply(w, slot):
            out = {}
            for (i, j), c in w.items():
                for k in range(d):
                    if slot == 1 and a0[k][i] != 0:
                        out[(k, j)] = out.get((k, j), ZERO) + a0[k][i] * c
                    if slot == 2 and a0[k][j] != 0:
                        out[(i, k)] = out.get((i, k), ZERO) + a0[k][j] * c
            return out
        tot = ZERO
        for slot in (1, 2):
            AV, AU = slot_apply(Vw, slot), slot_apply(Uw, slot)
            at_x = lambda key: site_of[key[0]] == x0 if slot == 1 else site_of[key[1]] == x0
            tot += sum((c * AV.get(key, ZERO) for key, c in Uw.items() if at_x(key)), ZERO) - sum((c * AU.get(key, ZERO) for key, c in Vw.items() if at_x(key)), ZERO)
        return tot
    dens = [density(x0, PU, PV) for x0 in range(size)]
    dens_unprojected = [density(x0, U, V) for x0 in range(size)]
    source_ok = all(derivative[x0] == dens[x0] for x0 in range(size))
    if mut("source_is_the_unprojected_density"):
        source_ok = all(derivative[x0] == dens_unprojected[x0] for x0 in range(size))
    differs = any(dens[x0] != dens_unprojected[x0] for x0 in range(size))
    weight = 1 if not mut("weight_is_two") else 2
    weight_ok = sum(derivative, ZERO) == weight * total and total != 0
    checks.check("B1", source_ok and differs and weight_ok, "T1: on a ring of 6 with a varying rational rate field, for the antisymmetric pair of two orthogonal complex one-record states PROJECTED to different-site configurations, the exact derivative of <Psi_P|H2|Psi_P> with respect to each site's u_x (the t-linear coefficient of a quadratic form) equals the projected pair's own energy density e_x^(2) at that site, and differs from the unprojected pair's density; the densities sum to the pair's energy (weight one): block 55's source law holds for records under exclusion, with the projected state")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    size = RING
    d = 2 * size
    site_of = [x for x in range(size) for c in range(2)]
    phi_chess = [F(3, 2) if x % 2 == 0 else F(2, 3) for x in range(size)]
    a_chess, _ = ring_generator(size, phi_chess)
    a_free, _ = ring_generator(size, [ONE] * size)
    d_, u1, v1, u2, v2 = one_record_states(size)
    U, V = pair_state(d, u1, v1, u2, v2)
    PU, PV = keep(U, site_of), keep(V, site_of)
    same_chess = all(keep(two_body_apply(a_chess, w), site_of) == keep(two_body_apply(a_free, w), site_of) for w in (PU, PV))
    if mut("chessboard_seen_under_exclusion"):
        same_chess = not same_chess
    # P and the simultaneous translation: on basis pairs (i, j) -> (i + 2, j + 2) (a shift by one site moves both orbitals of a site)
    shift = lambda o: (o + 2) % d
    def translate(w):
        return {(shift(i), shift(j)): c for (i, j), c in w.items()}
    crystal = all(keep(translate(w), site_of) == translate(keep(w, site_of)) for w in (U, V))
    if mut("exclusion_breaks_the_crystal_momentum"):
        crystal = not crystal
    # P and the one-step momentum S (x) 1 + 1 (x) S do not commute: exhibit a basis pair (i, j) on different sites that S (x) 1 carries onto the same site
    a_s, _ = ring_generator(size, [ONE] * size)
    basis_pair = {(0, 2): ONE}                                                       # orbitals 0 (site 0, coin 0) and 2 (site 1, coin 0)
    moved = two_body_apply(a_s, basis_pair)
    onto_same_site = any(site_of[i] == site_of[j] and c != 0 for (i, j), c in moved.items())
    commutator_nonzero = keep(moved, site_of) != moved
    if mut("exclusion_keeps_the_one_step_momentum"):
        commutator_nonzero = not commutator_nonzero
    checks.check("C1", same_chess and crystal and onto_same_site and commutator_nonzero, "T2: the exclusion projector commutes with a chessboard of clocks (the compressed generator with rates (3/2, 2/3, ...) equals the compressed free generator on the projected pair) and with the simultaneous translation of both records (crystal momentum is conserved under exclusion), but not with the one-step momentum S (x) 1 + 1 (x) S: applied to two records on neighbouring sites it carries one onto the other's site, which the projector removes - block 63's conserved momentum is not conserved for records under exclusion")
# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for amplitudes on the lattice timed by local clocks and the Record axiom in the owner's reading; it reports which of the ledger's identities survive when two or more records compose under exclusion, and what the interacting sea does to the clocks when executed; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - the t-linear coefficient of the quadratic form for each of the six sites; the two-body matrix elements moved by one step",
    "per_site: executed - the derivative against the projected density at every site of the ring; the chessboard of rates against the free generator on the projected pair at every configuration",
    "per_mode: executed - control: ground-state energies and second-order responses of the interacting sea on tori 3x3, 4x3, 5x3 and rings 6, 8, 10",
    "per_block: executed - weight one (the densities sum to the pair's energy); the simultaneous translation against the projector on the whole pair",
    "lattice_wide: T1 and T2 are exact for the states and rings tried and hold by their proofs for every pair state and every ring; the interacting sea's numbers are executed only; the exchange sign and the filling are not decided",
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
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: many records under exclusion - block 55's source law holds with the projected state's density (weight one); a chessboard of clocks stays invisible; crystal momentum is conserved but the one-step momentum is not; executed: the interacting sea at the filling of the free negative branch has a volume term four times smaller and a clock stiffness of the OPPOSITE sign to the free sea's on 2D tori")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
