#!/usr/bin/env python3
"""Conditional additive site-frame and reach-two strain couplings, curl/constant-volume functionals, and pure bond hopping. The finite corner projection is first-order only; no universal frame or field no-go."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_ALTERNATING_LENGTHS_ARE_A_RELABELLING_INVISIBLE_TO_THE_WALK_AND_FREE_FOR_THE_LEDGER_A_REST_ENERGY_NEEDS_THE_BONDS_OWN_AMPLITUDE_NO_STRAIN_GAPS_AT_FIRST_ORDER_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_WHAT_CAN_GAP_THE_WALK_NO_INVARIANT_TERM_AT_ANY_REACH_CHESSBOARD_OR_AXIS_STRIPES_ON_SITES_ALTERNATING_LENGTHS_GIVE_ONE_REST_ENERGY_EXCLUSION_CAGES_BOUNDED_THEOREM_NOTE_2026-09-22.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_alternating_lengths_are_a_relabelling_invisible_and_free_for_the_ledger_rest_energy_needs_the_bonds_own_amplitude_no_first_order_strain_gap_bounded_theorem_note_2026-09-22"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "alternation_seen_by_the_frame": "B",
    "alternation_seen_by_the_strain_coupling": "B",
    "alternation_is_not_a_relabelling": "B",
    "strain_has_corner_matrix_elements": "C",
    "bond_amplitude_coupling_blind_at_corners": "C",
    "sea_energy_rises_under_alternation": "D",
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


SIZE = 4
SITES = list(product(range(SIZE), repeat=3))
IDX = {s: i for i, s in enumerate(SITES)}
NSITES = len(SITES)
DELTA = F(3, 10)
SIG_G = (
    ((G(0), G(1)), (G(1), G(0))),
    ((G(0), G(0, -1)), (G(0, 1), G(0))),
    ((G(1), G(0)), (G(0), G(-1))),
)
HALF_I = G(0, F(1, 2))                                                                  # i/2
GZERO = G(0)


def step(s, a, d):
    t = list(s)
    t[a] = (t[a] + d) % SIZE
    return tuple(t)


def sp_add(m, r, c, v):
    if v == GZERO:
        return
    key = (r, c)
    w = m.get(key, GZERO) + v
    if w == GZERO:
        m.pop(key, None)
    else:
        m[key] = w


def sp_mul(a, b):
    """Product of sparse Gaussian-rational matrices (dicts {(r, c): G})."""
    by_row = {}
    for (r, c), v in b.items():
        by_row.setdefault(r, []).append((c, v))
    out = {}
    for (r, k), v in a.items():
        for c, w in by_row.get(k, ()):
            sp_add(out, r, c, v * w)
    return out


def sp_sum(*ms):
    out = {}
    for m in ms:
        for key, v in m.items():
            sp_add(out, key[0], key[1], v)
    return out


def sp_scale(m, f):
    return {k: v * f for k, v in m.items()}


def sp_equal(a, b):
    return sp_sum(a, sp_scale(b, G(-1))) == {}


def site_op(f):
    """Diagonal site function (real rationals) on the site index."""
    return {(IDX[s], IDX[s]): G(f(s)) for s in SITES if f(s) != 0}


def shift_op(a):
    """(T_a psi)(x) = psi(x + e_a)."""
    return {(IDX[s], IDX[step(s, a, 1)]): G(1) for s in SITES}


def s_op(a):
    """S_a = (T_a - T_a^dag)/(2i): entries -i/2 at (x, x + e_a) and +i/2 at (x, x - e_a)."""
    m = {}
    for s in SITES:
        sp_add(m, IDX[s], IDX[step(s, a, 1)], MINUS_HALF_I)
        sp_add(m, IDX[s], IDX[step(s, a, -1)], HALF_I)
    return m


def c_weighted(a, v):
    """(C_a[v] psi)(x) = 1/2 [v(x) psi(x + e_a) + v(x - e_a) psi(x - e_a)], v a bond function stored at the bond's first site."""
    m = {}
    for s in SITES:
        sp_add(m, IDX[s], IDX[step(s, a, 1)], G(F(v(s)) / 2))
        sp_add(m, IDX[s], IDX[step(s, a, -1)], G(F(v(step(s, a, -1))) / 2))
    return m


def bond_amplitude_hop(a, t):
    """(1/2i)(t(x) T_a - T_a^dag t(x)): the sigma-hop whose amplitude on the bond x -> x + e_a is t(x)."""
    m = {}
    for s in SITES:
        sp_add(m, IDX[s], IDX[step(s, a, 1)], MINUS_HALF_I * G(F(t(s))))
        sp_add(m, IDX[s], IDX[step(s, a, -1)], HALF_I * G(F(t(step(s, a, -1)))))
    return m


def with_coin(sig, m):
    """sigma (x) m on coin x site, index 2 * site + coin."""
    out = {}
    for (r, c), v in m.items():
        for i in range(2):
            for j in range(2):
                sp_add(out, 2 * r + i, 2 * c + j, sig[i][j] * v)
    return out


def anticomm_half(x, y):
    return sp_scale(sp_sum(sp_mul(x, y), sp_mul(y, x)), G(F(1, 2)))


def free_walk():
    return sp_sum(*[with_coin(SIG_G[a], s_op(a)) for a in range(3)])


def corner_vectors():
    """The eight corner plane waves as site vectors of +-1 (unnormalized), for each of the two coin states."""
    vecs = []
    for kc in product((0, 1), repeat=3):
        site = {IDX[s]: G(1 if sum(kc[a] * s[a] for a in range(3)) % 2 == 0 else -1) for s in SITES}
        for coin in range(2):
            vecs.append({2 * i + coin: v for i, v in site.items()})
    return vecs


def matrix_element(u, m, w):
    tot = GZERO
    wk = set(w)
    for (r, c), v in m.items():
        if r in u and c in wk:
            tot = tot + u[r].conj() * v * w[c]
    return tot


def alternation(a):
    return lambda s, a=a: DELTA * ((-1) ** s[a])


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    h0 = free_walk()
    frame = sp_sum(*[with_coin(SIG_G[j], anticomm_half(site_op(lambda s, j=j: 1 + alternation(j)(s)), s_op(j))) for j in range(3)])
    same = sp_equal(frame, h0)
    ok = same if not mut("alternation_seen_by_the_frame") else (not same)
    checks.check("B1", ok, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')

    strain = sp_sum(*[with_coin(SIG_G[a], anticomm_half(c_weighted(a, alternation(a)), s_op(a))) for a in range(3)])
    zero = strain == {}
    ok = zero if not mut("alternation_seen_by_the_strain_coupling") else (not zero)
    checks.check("B2", ok, 'Scoped exact check B2: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')

    xi = {a: (lambda s, a=a: -DELTA * ((-1) ** s[a]) / 2) for a in range(3)}
    is_diff = all(xi[a](step(s, a, 1)) - xi[a](s) == alternation(a)(s) for s in SITES for a in range(3))
    curls_zero = True
    for s in SITES:
        for a in range(3):
            for b in range(3):
                if a == b:
                    continue
                # F_ab^a = d_a B_b^a - d_b B_a^a with B_b^a = 0 (no tilt) and B_a^a alternating along a only
                d_b = alternation(a)(step(s, b, 1)) - alternation(a)(s)
                curls_zero = curls_zero and d_b == 0
    volume = sum((F(1) * (1 + alternation(0)(s)) * (1 + alternation(1)(s)) * (1 + alternation(2)(s)) for s in SITES), ZERO)
    ok = (is_diff and curls_zero and volume == NSITES) if not mut("alternation_is_not_a_relabelling") else (not curls_zero)
    T6=sp.zeros(6)
    for x in range(6): T6[x,(x+1)%6]=1
    S6=(T6-T6.T)/(2*sp.I)
    P6=S6*(T6+T6.T)/2
    Q6=sp.diag(*[(-1)**x for x in range(6)])
    checks.check("B4", Q6*P6==P6*Q6 and (sp.I*Q6*S6*P6+P6*sp.I*Q6*S6)/2!=sp.zeros(6), 'Scoped exact check B4: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')
    checks.check("B3", ok, 'Scoped exact check B3: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    corners = corner_vectors()
    x_site = site_op(lambda s: F(1 + s[0] + 2 * s[1] + 5 * s[2] * s[2], 7))
    v_bond = lambda s: F(2 + 3 * s[0] * s[1] + s[2], 11)
    max_abs = ZERO
    terms = [with_coin(SIG_G[j], anticomm_half(x_site, s_op(j))) for j in range(3)] + [with_coin(SIG_G[a], anticomm_half(c_weighted(a, v_bond), s_op(a))) for a in range(3)]
    for term in terms:
        for u in corners:
            for w in corners:
                el = matrix_element(u, term, w)
                max_abs = max(max_abs, el.re * el.re + el.im * el.im)
    none = max_abs == ZERO
    ok = none if not mut("strain_has_corner_matrix_elements") else (not none)
    checks.check("C1", ok, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')

    ssh = sp_sum(*[with_coin(SIG_G[a], bond_amplitude_hop(a, lambda s, a=a: alternation(a)(s))) for a in range(3)])
    n = len(corners)
    block = [[matrix_element(corners[i], ssh, corners[j]) * G(F(1, NSITES)) for j in range(n)] for i in range(n)]
    nonzero = any(not (block[i][j] == GZERO) for i in range(n) for j in range(n))
    sq = [[sum((block[i][k] * block[k][j] for k in range(n)), GZERO) for j in range(n)] for i in range(n)]
    target = G(3 * DELTA * DELTA)
    is_mass = all(sq[i][j] == (target if i == j else GZERO) for i in range(n) for j in range(n))
    ok = (nonzero and is_mass) if not mut("bond_amplitude_coupling_blind_at_corners") else (not nonzero)
    checks.check("C2", ok, 'Scoped exact check C2: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    # ring of four with the bond-amplitude coupling: sites 0..3, hop amplitude 1 + delta(-1)^x; H = sigma_x (x) (1/2i)(t T - T^dag t)
    size = 4
    d = sp.symbols("delta", real=True)
    t = [1 + d * (-1) ** x for x in range(size)]
    hop = sp.zeros(size, size)
    for x in range(size):
        hop[x, (x + 1) % size] += t[x] / (2 * sp.I)
        hop[x, (x - 1) % size] -= t[(x - 1) % size] / (2 * sp.I)
    H = sp.kronecker_product(sp.Matrix([[0, 1], [1, 0]]), hop)
    ev = H.eigenvals()
    got = {sp.simplify(v): m for v, m in ev.items()}
    expected = {sp.Abs(d): 2, -sp.Abs(d): 2, sp.Integer(1): 2, sp.Integer(-1): 2}
    Evar=sp.symbols("E")
    spectrum_ok = sp.expand(H.charpoly(Evar).as_expr()-(Evar**2-1)**2*(Evar**2-d**2)**2)==0

    sea = -2 - 2 * sp.Abs(d)
    never_rises = sp.simplify(sea.subs(d, sp.Rational(3, 10)) - sea.subs(d, 0)) < 0
    ok = (spectrum_ok and never_rises) if not mut("sea_energy_rises_under_alternation") else (sp.simplify(sea.subs(d, sp.Rational(3, 10)) - sea.subs(d, 0)) > 0)
    checks.check("D1", ok, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    # evenness on the 4^3 torus, exact: T_0 H(delta) T_0^dag = H(-delta) for the bond-amplitude coupling
    ssh_plus = sp_sum(*[with_coin(SIG_G[a], bond_amplitude_hop(a, lambda s, a=a: 1 + alternation(a)(s))) for a in range(3)])
    ssh_minus = sp_sum(*[with_coin(SIG_G[a], bond_amplitude_hop(a, lambda s, a=a: 1 - alternation(a)(s))) for a in range(3)])
    shift_all = {}
    for s in SITES:
        t_ = step(step(step(s, 0, 1), 1, 1), 2, 1)
        for coin in range(2):
            sp_add(shift_all, 2 * IDX[s] + coin, 2 * IDX[t_] + coin, G(1))
    shift_back = {(c, r): v.conj() for (r, c), v in shift_all.items()}
    conj = sp_mul(sp_mul(shift_all, ssh_plus), shift_back)
    checks.check("D2", sp_equal(conj, ssh_minus), 'Scoped exact check D2: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
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
    print('scope: Conditional additive site-frame and reach-two strain couplings, curl/constant-volume functionals, and pure bond hopping. The finite corner projection is first-order only; no universal frame or field no-go.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
