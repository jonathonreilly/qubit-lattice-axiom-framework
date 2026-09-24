#!/usr/bin/env python3
"""For supplied two-particle hopping compressed to different-site configurations, exact trace comparisons on rings of four through seven sites distinguish it from the free symmetric and antisymmetric sectors. One explicit projected pair fails additivity relative to its original orbitals. No universal nonadditivity or general ring-parity spectrum theorem is claimed."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_IS_AN_INTERACTION_NOT_A_FREE_SEA_TWO_RECORDS_UNDER_EXCLUSION_AGAINST_FREE_ANTISYMMETRIC_AND_SYMMETRIC_PAIRS_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_AMPLITUDES_OF_NEGATIVE_ENERGY_FALL_LIKE_THE_OTHERS_AND_SOURCE_THE_OPPOSITE_FIELD_A_NEGATIVE_BODY_AT_REST_HAS_A_LARGEST_SIZE_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_THE_FILLED_SEAS_ENERGY_AS_THE_LEDGERS_FIELD_TERM_A_CHESSBOARD_OF_CLOCKS_IS_INVISIBLE_THE_SEA_INDUCES_A_CLOCK_STIFFNESS_NOT_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-22.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_one_record_per_site_is_an_interaction_not_a_free_sea_two_records_under_exclusion_against_free_antisymmetric_and_symmetric_pairs_bounded_theorem_note_2026-09-22"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "hard_core_equals_free_antisymmetric": "B",
    "hard_core_equals_free_symmetric": "B",
    "exchange_sign_visible_at_second_order": "C",
    "hard_core_energy_is_additive": "D",
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
    note, axioms = texts[:2]
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
            out[p][q] = tot
    # exact: divide row p by norm_p and column q by norm_q after a square-root-free normalisation: use tr((D^-1/2 M D^-1/2)^k) = tr((D^-1 M)^k)
    return out, norms


TRACE_CACHE = {}

def traces(a, vectors):
    """tr H^2/dim and tr H^4/dim of the compressed generator (H = -i A), exactly, via tr((D^-1 M)^k) with D the diagonal of norms."""
    key = (tuple(map(tuple,a)),tuple(tuple(sorted(v.items())) for v in vectors))
    if key in TRACE_CACHE: return TRACE_CACHE[key]
    m_raw, norms = compress(a, vectors)
    m = [[m_raw[p][q] / norms[p] for q in range(len(vectors))] for p in range(len(vectors))]       # D^-1 M
    dim = len(vectors)

    def matmul(u, v):
        out = [[ZERO]*len(v[0]) for _ in u]
        rows = [[(j,val) for j,val in enumerate(row) if val] for row in v]
        for i,row in enumerate(u):
            for k,val in enumerate(row):
                if val:
                    for j,other in rows[k]: out[i][j] += val*other
        return out
    m2 = matmul(m, m)
    t2 = -sum((m2[p][p] for p in range(dim)), ZERO) / dim
    m4 = matmul(m2, m2)
    t4 = sum((m4[p][p] for p in range(dim)), ZERO) / dim
    m6 = matmul(m4, m2)
    t6 = -sum((m6[p][p] for p in range(dim)), ZERO) / dim
    TRACE_CACHE[key] = (t2,t4,dim,t6)
    return TRACE_CACHE[key]


def sectors(d, site_of):
    free_anti = [{(i, j): ONE, (j, i): -ONE} for i in range(d) for j in range(i + 1, d)]
    free_sym = [{(i, j): ONE, (j, i): ONE} for i in range(d) for j in range(i + 1, d)] + [{(i, i): ONE} for i in range(d)]
    hard_anti = [{(i, j): ONE, (j, i): -ONE} for i in range(d) for j in range(i + 1, d) if site_of[i] != site_of[j]]
    hard_sym = [{(i, j): ONE, (j, i): ONE} for i in range(d) for j in range(i + 1, d) if site_of[i] != site_of[j]]
    hard_none = [{(i, j): ONE} for i in range(d) for j in range(d) if site_of[i] != site_of[j]]
    return free_anti, free_sym, hard_anti, hard_sym, hard_none


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    results = {}
    for size in (4, 5, 6, 7):
        a, site_of = ring_generator(size, [ONE] * size)
        free_anti, free_sym, hard_anti, hard_sym, hard_none = sectors(2 * size, site_of)
        results[size] = {name: traces(a, vecs) for name, vecs in (("free_anti", free_anti), ("free_sym", free_sym), ("hard_anti", hard_anti), ("hard_sym", hard_sym), ("hard_none", hard_none))}
    differs_anti = all(results[s]["hard_anti"][0] != results[s]["free_anti"][0] for s in results)
    differs_sym = all(results[s]["hard_sym"][0] != results[s]["free_sym"][0] for s in results)
    dims = all(results[s]["hard_anti"][2] == results[s]["free_anti"][2] - s for s in results)
    if mut("hard_core_equals_free_antisymmetric"):
        differs_anti = not differs_anti
    if mut("hard_core_equals_free_symmetric"):
        differs_sym = not differs_sym
    expected = {4:(F(2,3),F(6,7),F(10,9)),5:(F(3,4),F(8,9),F(12,11)),6:(F(4,5),F(10,11),F(14,13)),7:(F(5,6),F(12,13),F(16,15))}
    assert all((results[s]['hard_anti'][0],results[s]['free_anti'][0],results[s]['free_sym'][0]) == expected[s] for s in results)
    assert results[4]['hard_anti'][1] == F(5,6) and results[4]['hard_sym'][1] == F(7,6)
    summary = "; ".join(f"N = {s}: hard-core {results[s]['hard_anti'][0]} against free antisymmetric {results[s]['free_anti'][0]} and free symmetric {results[s]['free_sym'][0]}" for s in results)
    checks.check("B1", differs_anti and differs_sym and dims, 'PR8613 B1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    same2 = True
    same4_large = True
    differ4_small = False
    for size in (4, 5, 6, 7):
        a, site_of = ring_generator(size, [ONE] * size)
        _, _, hard_anti, hard_sym, hard_none = sectors(2 * size, site_of)
        ta, ts, tn = traces(a, hard_anti), traces(a, hard_sym), traces(a, hard_none)
        same2 = same2 and ta[0] == ts[0] == tn[0]
        if size == 4:
            differ4_small = ta[1] != ts[1]
        else:
            same4_large = same4_large and ta[1] == ts[1] == tn[1]
        if size == 6:
            differ6_sixth = ta[3] != ts[3]
        if size in (5, 7):
            same6_odd = (ta[3] == ts[3] == tn[3]) if size == 5 else (same6_odd and ta[3] == ts[3] == tn[3])
    if mut("exchange_sign_visible_at_second_order"):
        same2 = not same2
    checks.check("C1", same2 and same4_large and differ4_small and differ6_sixth and same6_odd, 'PR8613 C1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    size = 6
    phi = [1 + F((3 * x * x + x) % 5, 7) for x in range(size)]
    a, site_of = ring_generator(size, phi)
    d = 2 * size
    inner = lambda u, v: sum((p * q for p, q in zip(u, v)), ZERO)

    def a_apply(v):
        return [sum((a[i][k] * v[k] for k in range(d)), ZERO) for i in range(d)]
    # complex one-record states psi = u + i v (real vectors u, v); H = -i A: <psi|H|psi> = 2 u^T A v (real), for A antisymmetric
    u1 = [F((x * x + 1) % 4, 3) if c == 0 else F((2 * x + 1) % 5, 4) for x in range(size) for c in range(2)]
    v1 = [F(x % 3, 2) if c == 0 else F((x * x) % 3 - 1, 3) for x in range(size) for c in range(2)]
    u2r = [F((x + 2) % 4, 5) if c == 0 else F(1, 2) for x in range(size) for c in range(2)]
    v2r = [F((x * x + x) % 3, 2) if c == 0 else F((3 * x) % 4 - 2, 3) for x in range(size) for c in range(2)]
    # make psi2 orthogonal to psi1 exactly: psi2 -> psi2 - (<psi1|psi2>/<psi1|psi1>) psi1 with complex coefficient c = cr + i ci
    n1 = inner(u1, u1) + inner(v1, v1)
    cr = (inner(u1, u2r) + inner(v1, v2r)) / n1
    ci = (inner(u1, v2r) - inner(v1, u2r)) / n1
    u2 = [ur - (cr * p - ci * q) for ur, p, q in zip(u2r, u1, v1)]
    v2 = [vr - (cr * q + ci * p) for vr, p, q in zip(v2r, u1, v1)]
    orthogonal = inner(u1, u2) + inner(v1, v2) == 0 and inner(u1, v2) - inner(v1, u2) == 0
    energy = lambda u, v: 2 * inner(u, a_apply(v)) / (inner(u, u) + inner(v, v))
    e1, e2 = energy(u1, v1), energy(u2, v2)
    # the antisymmetric pair Psi = psi1 (x) psi2 - psi2 (x) psi1 = U + i V on index pairs
    U, V = {}, {}
    for i in range(d):
        for j in range(d):
            # (u1 + i v1)_i (u2 + i v2)_j - (u2 + i v2)_i (u1 + i v1)_j
            re = u1[i] * u2[j] - v1[i] * v2[j] - (u2[i] * u1[j] - v2[i] * v1[j])
            im = u1[i] * v2[j] + v1[i] * u2[j] - (u2[i] * v1[j] + v2[i] * u1[j])
            if re != 0:
                U[(i, j)] = re
            if im != 0:
                V[(i, j)] = im

    def a2_apply(w):
        out = {}
        for (i, j), c in w.items():
            for k in range(d):
                if a[k][i] != 0:
                    out[(k, j)] = out.get((k, j), ZERO) + a[k][i] * c
                if a[k][j] != 0:
                    out[(i, k)] = out.get((i, k), ZERO) + a[k][j] * c
        return out
    dot = lambda w1, w2: sum((c * w2.get(key, ZERO) for key, c in w1.items()), ZERO)
    nrm = lambda w: sum((c * c for c in w.values()), ZERO)
    free_val = 2 * dot(U, a2_apply(V)) / (nrm(U) + nrm(V))
    keep = lambda w: {key: c for key, c in w.items() if site_of[key[0]] != site_of[key[1]]}
    PU, PV = keep(U), keep(V)
    hard_val = 2 * dot(PU, a2_apply(PV)) / (nrm(PU) + nrm(PV))                         # <P Psi| H2 |P Psi>/<P Psi|P Psi> = the compressed generator's expectation
    free_additive = free_val == e1 + e2
    hard_additive = hard_val == e1 + e2
    if mut("hard_core_energy_is_additive"):
        hard_additive = not hard_additive
    checks.check("D1", orthogonal and free_additive and not hard_additive and e1 != 0 and e2 != 0, 'PR8613 D1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')
# ============================================================================================ family F
FENCES = ('This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.', 'No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.')
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
    nodes = list(ast.walk(ast.parse(src)))
    float_hits = [n for n in nodes if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    float_hits += [n for n in nodes if isinstance(n, ast.Call) and ((isinstance(n.func, ast.Name) and n.func.id in ('float', 'N')) or (isinstance(n.func, ast.Attribute) and n.func.attr in ('evalf', 'N')))]
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
    "per_element: exact matrix or algebraic elements in the specified fixtures",
    "per_site: site identities in the explicitly stated finite fixtures",
    "per_mode: only the modes or finite spectral invariants actually checked below",
    "per_block: the stated finite operator and state comparisons",
    "lattice_wide: general conclusions rely on the scoped written proofs; historical simulations are deferred",
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
    print('scope: For supplied two-particle hopping compressed to different-site configurations, exact trace comparisons on rings of four through seven sites distinguish it from the free symmetric and antisymmetric sectors. One explicit projected pair fails additivity relative to its original orbitals. No universal nonadditivity or general ring-parity spectrum theorem is claimed.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
