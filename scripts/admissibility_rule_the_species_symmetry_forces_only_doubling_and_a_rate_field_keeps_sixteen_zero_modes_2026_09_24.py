#!/usr/bin/env python3
"""Exact checks: the walk's species symmetry forces only doubling - the reversal anticommutes with the even exchange maps, so
every eigenspace is C^2 (x) W with a real structure on W; in a varying rate field every nonzero level is exactly a pair and the
sixteen zero modes of the eight species survive exactly (a harvest block recovering a statement deferred when block 70 landed, from
a Grok-refereed probes attempt; block 70 as landed supplied; not adopted).

B (T1): the exchange maps and the reversal as operator identities on the 4x4x4 torus in a varying rate field and a varying frame.
C (T2): the two-dimensional corepresentation.
D (T3): the sixteen zero modes of a rate field, and the rank modulo a prime.
E (T4): characteristic polynomials modulo p = 1000033: the uniform walk, the rate field's block, the frame's square.
Exact rational arithmetic, and certificates modulo a prime; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_THE_SPECIES_SYMMETRY_FORCES_ONLY_DOUBLING_EVERY_NONZERO_LEVEL_IN_A_VARYING_FIELD_IS_A_PAIR_AND_A_RATE_FIELD_KEEPS_EXACTLY_SIXTEEN_ZERO_MODES_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_THE_EIGHT_SPECIES_ARE_EXCHANGED_BY_SITE_SIGNS_AND_A_HALF_TURN_OF_THE_COIN_WHAT_EACH_VARYING_FIELD_BECOMES_BOUNDED_THEOREM_NOTE_2026-09-21.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_species_symmetry_forces_only_doubling_every_nonzero_level_in_a_varying_field_is_a_pair_and_a_rate_field_keeps_exactly_sixteen_zero_modes_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "No possibility is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "reversal_commutes_forged": "B",
    "corep_forged": "C",
    "zero_modes_forged": "D",
    "doubling_forged": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: each site has a domain of local possibilities, no possibility privileged (coin and half-turns separately supplied); Admissibility is not a dynamics axiom (the walk and its fields are supplied clauses)")


# ============================================================================================ the walk on even tori
PRIME = 1000033
IOTA = 649529
CZERO, CONE, CIU = (Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(0), Fr(1))


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cconj(a):
    return (a[0], -a[1])


PAULI = {
    0: ((CONE, CZERO), (CZERO, CONE)),
    1: ((CZERO, CONE), (CONE, CZERO)),
    2: ((CZERO, (Fr(0), Fr(-1))), (CIU, CZERO)),
    3: ((CONE, CZERO), (CZERO, (Fr(-1), Fr(0)))),
}


class Torus:
    def __init__(self, dims):
        self.dims = dims
        self.sites = [(x, y, z) for x in range(dims[0]) for y in range(dims[1]) for z in range(dims[2])]
        self.index = {s: i for i, s in enumerate(self.sites)}
        self.n = 2 * len(self.sites)

    def shift(self, x, a, k):
        y = list(x)
        y[a] = (y[a] + k) % self.dims[a]
        return tuple(y)

    def idx(self, x, c):
        return 2 * self.index[x] + c


def op_add(op, i, j, v):
    if v != CZERO:
        cur = op.get((i, j), CZERO)
        nv = cadd(cur, v)
        if nv == CZERO:
            op.pop((i, j), None)
        else:
            op[(i, j)] = nv


def walk_op(t, phi=None, frame=None):
    """H = sum_a sigma_a S_a, (S_a psi)(x) = (psi(x + e_a) - psi(x - e_a))/(2i); with a rate field phi (H_w = Phi H Phi), or
    block 62's site-placed frame H_E = (1/2) sum_j {E^j(x).sigma, S_j}, E^j_a = delta_aj + frame[(x, j, a)]."""
    op = {}
    for x in t.sites:
        for j in range(3):
            for sgn, coef in ((1, (Fr(0), Fr(-1, 2))), (-1, (Fr(0), Fr(1, 2)))):
                y = t.shift(x, j, sgn)
                if frame is None:
                    mat = PAULI[j + 1]
                    scale = (phi[x] * phi[y], Fr(0)) if phi is not None else CONE
                    for c in range(2):
                        for d in range(2):
                            op_add(op, t.idx(x, c), t.idx(y, d), cmul(scale, cmul(coef, mat[c][d])))
                else:
                    for c in range(2):
                        for d in range(2):
                            ent = CZERO
                            for a in range(3):
                                wa = (Fr(1 if a == j else 0) + frame[(x, j, a)] + Fr(1 if a == j else 0) + frame[(y, j, a)], Fr(0))
                                ent = cadd(ent, cmul(wa, PAULI[a + 1][c][d]))
                            op_add(op, t.idx(x, c), t.idx(y, d), cmul((Fr(1, 2), Fr(0)), cmul(coef, ent)))
    return op


COIN_OF = {(0, 0, 0): 0, (1, 1, 0): 3, (1, 0, 1): 2, (0, 1, 1): 1, (1, 0, 0): 1, (0, 1, 0): 2, (0, 0, 1): 3, (1, 1, 1): 0}


def species_map(t, n):
    """V_n = R_n (x) U_n: the site sign (-1)^(n.x) with the coin half-turn R_n (block 70's exchange maps)."""
    op = {}
    mat = PAULI[COIN_OF[n]]
    for x in t.sites:
        u = -1 if (n[0] * x[0] + n[1] * x[1] + n[2] * x[2]) % 2 else 1
        for c in range(2):
            for d in range(2):
                op_add(op, t.idx(x, c), t.idx(x, d), cmul((Fr(u), Fr(0)), mat[c][d]))
    return op


def op_mul(a, b):
    rows = {}
    for (i, j), v in b.items():
        rows.setdefault(i, []).append((j, v))
    out = {}
    for (i, k), v in a.items():
        for j, w in rows.get(k, ()):
            op_add(out, i, j, cmul(v, w))
    return out


def op_scale(a, s):
    return {k: cmul(s, v) for k, v in a.items() if cmul(s, v) != CZERO}


def theta_conj(t, a):
    """Theta O Theta^-1 = sigma_2 conj(O) sigma_2 for Theta = sigma_2 K."""
    s2 = {}
    for x in t.sites:
        for c in range(2):
            for d in range(2):
                op_add(s2, t.idx(x, c), t.idx(x, d), PAULI[2][c][d])
    return op_mul(op_mul(s2, {k: cconj(v) for k, v in a.items()}), s2)


def to_mod(v):
    re = v[0].numerator * pow(v[0].denominator, -1, PRIME)
    im = v[1].numerator * pow(v[1].denominator, -1, PRIME)
    return (re + IOTA * im) % PRIME


def dense_mod(op, n, keep=None):
    keep = list(range(n)) if keep is None else keep
    pos = {k: i for i, k in enumerate(keep)}
    m = [[0] * len(keep) for _ in keep]
    for (i, j), v in op.items():
        if i in pos and j in pos:
            m[pos[i]][pos[j]] = to_mod(v)
    return m


def rank_mod(m):
    m = [row[:] for row in m]
    rows, cols, r = len(m), len(m[0]), 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if m[i][c]), None)
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        inv = pow(m[r][c], -1, PRIME)
        for i in range(r + 1, rows):
            if m[i][c]:
                f = m[i][c] * inv % PRIME
                m[i] = [(x - f * y) % PRIME for x, y in zip(m[i], m[r])]
        r += 1
    return r


def charpoly_mod(m):
    """characteristic polynomial det(E - M) mod PRIME, low degree first, by reduction to upper Hessenberg form."""
    n = len(m)
    a = [row[:] for row in m]
    for k in range(n - 2):
        piv = next((i for i in range(k + 1, n) if a[i][k]), None)
        if piv is None:
            continue
        if piv != k + 1:
            a[k + 1], a[piv] = a[piv], a[k + 1]
            for row in a:
                row[k + 1], row[piv] = row[piv], row[k + 1]
        inv = pow(a[k + 1][k], -1, PRIME)
        for i in range(k + 2, n):
            if a[i][k]:
                f = a[i][k] * inv % PRIME
                a[i] = [(x - f * y) % PRIME for x, y in zip(a[i], a[k + 1])]
                for row in a:
                    row[k + 1] = (row[k + 1] + f * row[i]) % PRIME
    polys = [[1]]
    for k in range(n):
        nxt = [0] + polys[k]
        for i in range(len(polys[k])):
            nxt[i] = (nxt[i] - a[k][k] * polys[k][i]) % PRIME
        prod = 1
        for i in range(k - 1, -1, -1):
            prod = prod * a[i + 1][i] % PRIME
            if prod == 0:
                break
            coef = prod * a[i][k] % PRIME
            for j, v in enumerate(polys[i]):
                nxt[j] = (nxt[j] - coef * v) % PRIME
        polys.append(nxt)
    return polys[n]


def ptrim(p):
    p = [c % PRIME for c in p]
    while p and p[-1] == 0:
        p.pop()
    return p


def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % PRIME
    return ptrim(out)


def pderiv(a):
    return ptrim([i * a[i] for i in range(1, len(a))])


def pmod(a, b):
    a = ptrim(a[:])
    inv = pow(b[-1], -1, PRIME)
    while len(a) >= len(b):
        f = a[-1] * inv % PRIME
        sh = len(a) - len(b)
        for i, y in enumerate(b):
            a[sh + i] = (a[sh + i] - f * y) % PRIME
        a = ptrim(a)
    return a


def pgcd(a, b):
    a, b = ptrim(a), ptrim(b)
    while b:
        a, b = b, pmod(a, b)
    inv = pow(a[-1], -1, PRIME)
    return [x * inv % PRIME for x in a]


def rate_field(t, seed):
    state = [seed]

    def rnd(m):
        state[0] = (state[0] * 6364136223846793005 + 1442695040888963407) % (1 << 64)
        return (state[0] >> 33) % m
    return {x: Fr(10 + rnd(10), 10) for x in t.sites}


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the even species maps, the reversal, and their relations, as operator identities."""
    t = Torus((4, 4, 4))
    phi = rate_field(t, 11)
    hw = walk_op(t, phi)
    ok = True
    maps = {n: species_map(t, n) for n in COIN_OF}
    ident = {(i, i): CONE for i in range(t.n)}
    for n, v in maps.items():
        sign = -1 if sum(n) % 2 else 1
        ok = ok and op_mul(op_mul(v, hw), v) == op_scale(hw, (Fr(sign), Fr(0))) and op_mul(v, v) == ident
    even = [(1, 1, 0), (1, 0, 1), (0, 1, 1)]
    for a, b in combinations(even, 2):
        ok = ok and op_mul(maps[a], maps[b]) == op_scale(op_mul(maps[b], maps[a]), (Fr(-1), Fr(0)))
    ok = ok and op_mul(maps[(1, 1, 0)], maps[(0, 1, 1)]) == op_scale(maps[(1, 0, 1)], CIU)
    ok_theta = theta_conj(t, hw) == hw
    anti = all(theta_conj(t, maps[n]) == op_scale(maps[n], (Fr(-1), Fr(0))) for n in even)
    if mut("reversal_commutes_forged"):
        anti = all(theta_conj(t, maps[n]) == maps[n] for n in even)
    frame = {}
    state = [5]
    for x in t.sites:
        for j in range(3):
            for a in range(3):
                state[0] = (state[0] * 6364136223846793005 + 1442695040888963407) % (1 << 64)
                frame[(x, j, a)] = Fr(int((state[0] >> 33) % 21) - 10, 100)
    he = walk_op(t, frame=frame)
    ok_frame = theta_conj(t, he) == he and op_mul(op_mul(maps[(1, 1, 0)], he), maps[(1, 1, 0)]) != he
    checks.check("B1", ok and ok_theta and anti,
                 "T1(a): on the 4x4x4 torus in a varying rate field w = phi^2: every exchange map V_n = R_n U_n (site sign (-1)^(n.x), coin half-turn) squares to 1 and has V_n H_w V_n = (-1)^|n| H_w; the three even maps anticommute pairwise with V110 V011 = i V101; the reversal Theta = sigma_2 K commutes with H_w and ANTICOMMUTES with each even map (Theta V_n Theta^-1 = -V_n), with Theta^2 = -1")
    checks.check("B2", ok_frame,
                 "T1(b): a varying frame (block 62's site-placed coupling with all nine components random) commutes with Theta but not with the even maps: this fixture breaks the tested even map; bipartite spectral reversal also remains")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the two-dimensional corepresentation - symmetry forces doubling only."""
    sz, sx, sy = sp.Matrix([[1, 0], [0, -1]]), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]])
    v110, v101, v011 = sz, sx, -sy
    rel = (v110 ** 2 == sp.eye(2) and v101 ** 2 == sp.eye(2) and v011 ** 2 == sp.eye(2)
           and v110 * v101 == -v101 * v110 and v110 * v011 == -v011 * v110 and v101 * v011 == -v011 * v101
           and v110 * v011 == sp.I * v101)
    theta_ok = all(sp.simplify(sy * m.conjugate() * sy + m) == sp.zeros(2, 2) for m in (v110, v101, v011))
    theta_sq = sp.simplify(sy * sy.conjugate()) == -sp.eye(2)
    if mut("corep_forged"):
        theta_ok = all(sp.simplify(sy * m.conjugate() * sy - m) == sp.zeros(2, 2) for m in (v110, v101, v011))
    checks.check("C1", rel and theta_ok and theta_sq,
                 "T2: V110, V101, V011 -> sigma_z, sigma_x, -sigma_y with Theta -> sigma_y K satisfy every relation of T1 (involutions, pairwise anticommuting, V110 V011 = i V101, Theta V Theta^-1 = -V, Theta^2 = -1); so on an eigenspace C^2 (x) W the even maps act on the first factor and Theta = sigma_y K (x) Theta_W with Theta_W^2 = +1, a real structure: the symmetry forces even multiplicity and nothing more, never four or eight")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: a rate field keeps exactly the sixteen zero modes."""
    t = Torus((4, 4, 4))
    phi = rate_field(t, 11)
    hw = walk_op(t, phi)
    killed = True
    for k in product((0, 2), repeat=3):
        for c in range(2):
            vec = {}
            for x in t.sites:
                sgn = -1 if (k[0] * x[0] + k[1] * x[1] + k[2] * x[2]) // 2 % 2 else 1
                vec[t.idx(x, c)] = (Fr(sgn) / phi[x], Fr(0))
            out = {}
            for (i, j), v in hw.items():
                if j in vec:
                    out[i] = cadd(out.get(i, CZERO), cmul(v, vec[j]))
            killed = killed and all(v == CZERO for v in out.values())
    rank = rank_mod(dense_mod(hw, t.n))
    if mut("zero_modes_forged"):
        rank -= 1
    checks.check("D1", killed and rank == t.n - 16,
                 f"T3: ker(Phi H Phi) = Phi^-1 ker H; on the 4x4x4 torus the sixteen vectors Phi^-1 (plane wave at k in {{0, pi}}^3) (x) (coin state) are annihilated exactly by H_w in a varying rate field, and H_w has rank {rank} = 128 - 16 modulo p = 1000033 (so over Q(i) as well): exactly sixteen zero modes, the eight species times the two coin states")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: generic levels are exactly doubled."""
    t = Torus((4, 4, 4))
    uni = charpoly_mod(dense_mod(walk_op(t), t.n))
    want = [1]
    for root_sq, mult in ((0, 16), (1, 24), (2, 24), (3, 8)):
        factor = [0, 1] if root_sq == 0 else [(-root_sq) % PRIME, 0, 1]
        for _ in range(mult if root_sq else 16):
            want = pmul(want, factor)
    ok_uni = sp.isprime(PRIME) and IOTA * IOTA % PRIME == PRIME - 1 and ptrim(uni) == want
    phi = rate_field(t, 11)
    hw = walk_op(t, phi)
    plus = [t.idx(x, c) for x in t.sites for c in range(2) if (1 if c == 0 else -1) * (-1 if (x[0] + x[1]) % 2 else 1) == 1]
    blk = charpoly_mod(dense_mod(hw, t.n, plus))
    zero_order = next(i for i, c in enumerate(blk) if c % PRIME)
    q = blk[zero_order:]
    sqfree = len(pgcd(q, pderiv(q))) == 1
    if mut("doubling_forged"):
        sqfree = not sqfree
    frame = {}
    state = [5]
    for x in t.sites:
        for j in range(3):
            for a in range(3):
                state[0] = (state[0] * 6364136223846793005 + 1442695040888963407) % (1 << 64)
                frame[(x, j, a)] = Fr(int((state[0] >> 33) % 21) - 10, 100)
    f = charpoly_mod(dense_mod(walk_op(t, frame=frame), t.n))
    g = pgcd(f, pderiv(f))
    ok_frame = len(g) - 1 == 64 and pmul(g, g) == ptrim(f) and len(pgcd(g, pderiv(g))) == 1
    checks.check("E1", ok_uni,
                 "T4(a): the uniform walk on 4x4x4 has characteristic polynomial E^16 (E^2 - 1)^24 (E^2 - 2)^24 (E^2 - 3)^8 (modulo p): levels of multiplicity 16, 24, 24 and 8, where momentum and species labels coincide")
    checks.check("E2", zero_order == 8 and len(q) - 1 == 56 and q[0] % PRIME != 0 and sqfree and ok_frame,
                 f"T4(b): in the varying rate field the V110 = +1 block (64 states) has characteristic polynomial E^{zero_order} q(E) with q of degree {len(q) - 1}, q(0) != 0 and q squarefree modulo p (hence over Q(i)); V101 carries the block onto the V110 = -1 block, so every nonzero level has multiplicity exactly 2; in the varying frame the characteristic polynomial is q^2 with q of degree 64 squarefree - exact doubling at this fixture, with reversal ensuring the even lower bound. By the discriminant, the same holds outside a proper algebraic set in these fixed 4x4x4 real parameter spaces")


# ============================================================================================ family F
FENCES = (
    "This note works within block 70's exchange maps of the walk's eight species, as landed on main, with supplied rate and frame fields on even tori; it reports that the stated symmetry relations force even multiplicity, with exact doubling generic at the checked size and that a rate field keeps the species' sixteen zero modes; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Kramers", "Wigner", "Moore", "Nielsen", "Ninomiya", "Kogut", "Susskind", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the 2x2 corepresentation's relations; V_n^2 = 1 and V_n H_w V_n = (-1)^|n| H_w for all eight maps",
    "per_site: executed - the sixteen zero-mode vectors Phi^-1 (plane wave) (x) (coin) annihilated exactly at every site of the 4x4x4 torus",
    "per_mode: executed - characteristic polynomials modulo p: the uniform walk (16, 24, 24, 8), the rate field's V110 = +1 block (E^8 times a squarefree degree-56 factor), the frame's square q^2",
    "per_block: executed - the reversal's anticommutation with the even maps and commutation with the rate and frame walks, as operator identities on 128 states",
    "lattice_wide: the algebra (T1, T2) on every even torus in rate fields; T3 on every even torus for every positive rate field; T4 verified on the 4x4x4 torus and generic by the discriminant; twist fields and other sizes are not re-run; the walk and its fields are supplied",
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
    print('scope: Symmetry doubling and sixteen zero modes; generic pair multiplicity only in fixed 4-cube parameter spaces. Supplied model only; no audit verdict.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
